"""One-off conversion of the Notion HTML export into one Markdown file per chapter.

Usage: python scripts/convert_notion.py notion-export/index.html
Requires beautifulsoup4. Writes notes/*.md and images/*.png.

Math is kept as TeX ($...$ inline, $$...$$ display), Notion text colors become
<span class="c-COLOR">, underlines become <u>.
"""
import re
import shutil
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote

from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = Path(__file__).resolve().parent.parent
NOTES_DIR = ROOT / "notes"
IMAGES_DIR = ROOT / "images"


def slugify(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def escape_md(text):
    # Only the characters that would otherwise change meaning mid-line.
    return re.sub(r"([\\*_`\[\]<>$])", r"\\\1", text)


class Converter:
    def __init__(self, src_dir, slug):
        self.src_dir = src_dir
        self.slug = slug
        self.image_count = 0

    # ---- inline -------------------------------------------------------------

    def inline(self, node):
        if isinstance(node, NavigableString):
            text = str(node).replace("﻿", "").replace("​", "")
            return escape_md(re.sub(r"\s*\n\s*", " ", text))
        if not isinstance(node, Tag):
            return ""
        classes = node.get("class", [])
        if "notion-text-equation-token" in classes:
            return "$" + node.find("annotation").text.strip() + "$"
        inner = "".join(self.inline(c) for c in node.children)
        if node.name == "br":
            return "<br>"
        if not inner.strip():
            return inner
        if node.name in ("strong", "b"):
            return self.wrap(inner, "**")
        if node.name in ("em", "i"):
            return self.wrap(inner, "*")
        if node.name == "code":
            return "`" + node.get_text() + "`"
        if node.name == "a":
            return f"[{inner}]({node['href']})"
        if node.name == "mark":
            color = next((c[len("highlight-"):] for c in classes if c.startswith("highlight-")), "default")
            if color == "default":
                return inner
            return f'<span class="c-{color}">{inner}</span>'
        if node.name == "span" and "border-bottom" in (node.get("style") or ""):
            return f"<u>{inner}</u>"
        return inner

    @staticmethod
    def wrap(inner, marker):
        # Markdown emphasis cannot start/end with whitespace; keep it outside.
        lead = inner[: len(inner) - len(inner.lstrip())]
        trail = inner[len(inner.rstrip()):]
        return f"{lead}{marker}{inner.strip()}{marker}{trail}"

    def inline_children(self, node):
        return self.clean("".join(self.inline(c) for c in node.children))

    @staticmethod
    def clean(text):
        text = re.sub(r"[ \t]+", " ", text).strip()
        return re.sub(r"^(?:<br>\s*)+|(?:\s*<br>)+$", "", text)

    # ---- blocks -------------------------------------------------------------

    def blocks(self, node, indent=""):
        """Convert the block children of `node` to a list of Markdown blocks."""
        out = []
        inline_buf = []  # stray inline content directly inside a block container

        def flush():
            text = self.clean("".join(inline_buf))
            if text:
                out.append(indent + text)
            inline_buf.clear()

        for child in node.children:
            if isinstance(child, Tag) and self.is_block(child):
                flush()
                block = self.block(child, indent)
                if block:
                    out.append(block)
            else:
                inline_buf.append(self.inline(child))
        flush()
        return out

    @staticmethod
    def is_block(tag):
        return tag.name in ("p", "h1", "h2", "h3", "ul", "ol", "figure", "table", "div", "details")

    def block(self, tag, indent):
        classes = tag.get("class", [])
        if tag.name == "p":
            # Notion puts indented child blocks inside the <p>; split them out.
            return "\n\n".join(self.blocks(tag, indent)) or None
        if tag.name in ("h1", "h2", "h3"):
            # Chapter title is h1, Notion's h3 sub-headings become h2.
            return indent + "## " + self.inline_children(tag)
        if tag.name in ("ul", "ol"):
            return self.list_block(tag, indent)
        if tag.name == "figure" and "image" in classes:
            return indent + self.image(tag)
        if tag.name == "table":
            return self.table(tag, indent)
        if (tag.name == "figure" and "equation" in classes) or "equation-container" in classes:
            tex = tag.find("annotation").text.strip()
            return f"{indent}$$\n{indent}{tex}\n{indent}$$"
        if tag.name == "div":
            return "\n\n".join(self.blocks(tag, indent)) or None
        raise ValueError(f"Unhandled block <{tag.name} class={classes}>")

    def list_block(self, tag, indent):
        ordered = tag.name == "ol"
        number = int(tag.get("start", 1))
        items = []
        for li in tag.find_all("li", recursive=False):
            marker = f"{number}. " if ordered else "- "
            number += 1
            child_indent = indent + " " * len(marker)
            parts = self.blocks(li, child_indent) or [child_indent]
            item = indent + marker + parts[0][len(child_indent):]
            for part in parts[1:]:
                # Nested lists attach directly; other blocks need a blank line
                # or they'd merge into the item's first paragraph.
                is_list = re.match(r" *(?:- |\d+\. )", part)
                item += ("\n" if is_list else "\n\n") + part
            items.append(item)
        return "\n".join(items)

    def image(self, figure):
        img = figure.find("img")
        src = self.src_dir / unquote(img["src"])
        self.image_count += 1
        name = f"{self.slug}-{self.image_count}{src.suffix}"
        shutil.copy(src, IMAGES_DIR / name)
        width = re.search(r"width:(\d+)", img.get("style", ""))
        caption = figure.find("figcaption")
        alt = caption.get_text(strip=True) if caption else ""
        # Keep Notion's display width as a hint; plain Markdown images can't carry it.
        if width:
            return f'<img src="../images/{name}" alt="{alt}" width="{width.group(1)}">'
        return f"![{alt}](../images/{name})"

    def table(self, tag, indent):
        rows = [[self.inline_children(c).replace("|", "\\|") for c in tr.find_all(["th", "td"])]
                for tr in tag.find_all("tr")]
        lines = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * len(rows[0])]
        lines += ["| " + " | ".join(r) + " |" for r in rows[1:]]
        return "\n".join(indent + line for line in lines)


def merge_adjacent_lists(md):
    # Notion wraps every list item in its own <ul>/<ol>; the blank line between
    # consecutive items would make the list "loose". Join them back up.
    return re.sub(r"(\n *(?:- |\d+\. )[^\n]*)\n\n(?= *(?:- |\d+\. ))", r"\1\n", md)


def main(export_path):
    export_path = Path(export_path)
    soup = BeautifulSoup(export_path.read_text(encoding="utf-8"), "html.parser")
    for style in soup.select(".page-body style"):
        style.decompose()
    # Notion nests identical formatting many levels deep (<strong><strong>…,
    # <mark class=x><strong><mark class=x>…); keep only the outermost.
    for tag in soup.select(".page-body strong, .page-body mark, .page-body em"):
        if tag.find_parent(lambda p: p.name == tag.name and p.get("class") == tag.get("class")):
            tag.unwrap()

    NOTES_DIR.mkdir(exist_ok=True)
    IMAGES_DIR.mkdir(exist_ok=True)

    for details in soup.select(".page-body > details"):
        title = details.summary.get_text(strip=True)
        number, name = re.match(r"(\d+)\.\s*(.*)", title).groups()
        slug = f"{int(number):02d}-{slugify(name)}"
        conv = Converter(export_path.parent, slug)
        body = "\n\n".join(conv.blocks(details.select_one(".indented")))
        # Repeat merging: each pass joins pairs, overlapping matches need another pass.
        for _ in range(3):
            body = merge_adjacent_lists(body)
        front = f'---\ntitle: "{name}"\nchapter: {int(number)}\n---\n\n# {name}\n\n'
        (NOTES_DIR / f"{slug}.md").write_text(front + body + "\n", encoding="utf-8")
        print(f"{slug}.md  ({conv.image_count} images)")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ROOT / "notion-export" / "index.html")
