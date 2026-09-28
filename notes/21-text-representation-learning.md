---
title: "Text representation learning"
chapter: 21
---

# Text representation learning

Use <u>log of co-occurence</u> counts of words $w_d$ and context words $w_n$ → sparse matrix $\in \N^{D \times N}$

- Same objective as matrix factorisations, except for adding a weighting term $f_{dn}$ in the sum. For **GloVe**, we have $f_{dn}:=\min\{1, (\frac{n_{dn}}{n_{max}})^\alpha\}$ for $\alpha\in [0, 1]$
- Rows of $\mathbf{W} \in \R^{D\times K}$ and $\mathbf{Z} \in \R^{N\times K}$ are word (or context word) representations
- **Skip-Gram** model (word2vec): use binary classification to separate <span class="c-teal">real</span> word pairs $(w_d, w_n)$ (appearing together in context window size 5) from <span class="c-red">fake</span> word paris (random words)
- **FastText**: matrix factorisation to learn sentence $s_n$ representations (supervised $(s_n,y_n)$). $y_n \in \{-1, 1\}$ and $f$ is a linear classifier loss, $x_n$ the bag-of-words (no ordering!) representation of $s_n$. Minimising

$$
\min_{\mathbf{W,Z}} \mathcal{L}(\mathbf{W,Z}) := \sum_{s_n}f(y_n\mathbf{WZ}^\top x_n)
$$
