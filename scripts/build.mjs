// Builds index.html from notes/*.md. Run with `npm run build`.
//
// Math is pulled out before Markdown parsing (so `_`, `*`, `\\` inside TeX are
// left alone) and emitted as raw TeX in <span class="math">; KaTeX renders it
// in the browser. That keeps the generated HTML small and readable.
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { Marked } from "marked";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const NOTES_DIR = path.join(ROOT, "notes");
const TEMPLATE = path.join(ROOT, "scripts", "template.html");
const OUT = path.join(ROOT, "index.html");

const escapeHtml = (s) =>
  s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

const slugify = (s) =>
  s
    .replace(/<[^>]+>/g, "")
    .toLowerCase()
    .normalize("NFKD")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "");

function parseFrontmatter(src) {
  const m = src.match(/^---\n([\s\S]*?)\n---\n/);
  const data = {};
  for (const line of m[1].split("\n")) {
    const [key, ...rest] = line.split(":");
    data[key.trim()] = rest.join(":").trim().replace(/^"|"$/g, "");
  }
  return { data, body: src.slice(m[0].length) };
}

function extractMath(md) {
  const math = [];
  const stash = (tex, display) => `MATH${math.push({ tex: tex.trim(), display }) - 1}X`;
  md = md.replace(/^([ \t]*)\$\$\n([\s\S]*?)\n[ \t]*\$\$$/gm, (_, indent, tex) => indent + stash(tex, true));
  md = md.replace(/(?<!\\)\$([^$\n]+?)(?<!\\)\$/g, (_, tex) => stash(tex, false));
  return { md, math };
}

function restoreMath(html, math) {
  const render = ({ tex, display }) =>
    display
      ? `<div class="math display">${escapeHtml(tex)}</div>`
      : `<span class="math">${escapeHtml(tex)}</span>`;
  return html
    .replace(/<p>MATH(\d+)X<\/p>/g, (_, i) => render(math[i]))
    .replace(/MATH(\d+)X/g, (_, i) => render(math[i]));
}

const chapters = fs
  .readdirSync(NOTES_DIR)
  .filter((f) => f.endsWith(".md"))
  .sort()
  .map((file) => {
    const { data, body } = parseFrontmatter(fs.readFileSync(path.join(NOTES_DIR, file), "utf8"));
    const id = file.replace(/^\d+-/, "").replace(/\.md$/, "");
    const { md, math } = extractMath(body);

    const marked = new Marked({
      renderer: {
        heading({ tokens, depth }) {
          const text = this.parser.parseInline(tokens);
          if (depth === 1) {
            return `<h2 id="${id}"><span class="num">${data.chapter}</span>${text}</h2>\n`;
          }
          const sub = `${id}--${slugify(restoreMath(text, math))}`;
          return `<h${depth + 1} id="${sub}">${text}</h${depth + 1}>\n`;
        },
      },
    });

    let html = restoreMath(marked.parse(md), math);
    html = html.replace(/src="\.\.\/images\//g, 'src="images/');
    return { id, title: data.title, chapter: data.chapter, html };
  });

const toc = chapters
  .map((c) => `<li><a href="#${c.id}"><span class="num">${c.chapter}</span>${escapeHtml(c.title)}</a></li>`)
  .join("\n");
const content = chapters
  .map((c) => `<section class="chapter">\n${c.html}</section>`)
  .join("\n\n");

const page = fs
  .readFileSync(TEMPLATE, "utf8")
  .replace("{{toc}}", toc)
  .replace("{{content}}", content);
fs.writeFileSync(OUT, page);
console.log(`Wrote ${path.relative(ROOT, OUT)} (${chapters.length} chapters, ${(page.length / 1024).toFixed(0)} KB)`);
