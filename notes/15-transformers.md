---
title: "Transformers"
chapter: 15
---

# Transformers

Transformer $f:sequence \rightarrow sequence$. Applicable across any modality (everything can be a token), good for long-range dependencies in text, self-attention scales quadratically but highly parallelisable

<img src="../images/15-transformers-1.png" alt="" width="336">

## Input Transformations

$Input \rightarrow tokens \in \R^D$

- for each word in text→ token ID → vector in $\R^D$
- for each patch in image → flatten $\in \R^{F}$ → multiply by embedding matrix $\mathbf{W} \in \R^{F\times D}$

## Transformer block

$tokens \in \R^D \rightarrow tokens \in \R^D$

- <span class="c-teal">**Attention**</span>: $A:tokens \rightarrow tokens$
  - <span class="c-blue">Query tokens</span> $Q \in \R^{T_{out}\times D_K}$<br><br><span class="c-blue">Key tokens</span> $K \in \R^{T_{in}\times D_K}$
  - mixes info between tokens ~ weighted average with weights $p_{i,j}$ based on how similar $q_i$ and $k_j$ are: $P=\text{softmax}\left(\frac{QK^\top}{\sqrt{D_K}}\right)$, where $\text{softmax}(\mathbf{x})_i=\frac{e^{x_i}}{\sum_j e^{x_j}}$
- <span class="c-teal">**Self-Attention**</span>: $T=T_{in}=T_{out}$, $X\in \R^{T \times D}$
  - <span class="c-blue">Queries</span> $Q = XW_Q \in \R^{T\times D_K}$<br><br><span class="c-blue">Keys</span> $K = XW_K\in \R^{T\times D_K}$<br><br><span class="c-blue">Values</span> $V = XW_V\in \R^{T\times D}$
  - Output $Z=\text{softmax}\left(\frac{X W_Q W_K^\top X^\top}{\sqrt{D_K}}\right) X W_V = \text{softmax}\left(\frac{QK^\top}{\sqrt{D_K}}\right) V$
  - Run $H$ self-attention heads in parallel and linearly combine the outputs
- <span class="c-teal">**MLP**</span>: mixes information within tokens $\text{MLP}(X)=\varphi(XW_1)W_2$ ← learned $W$
- <span class="c-teal">**Other blocks**</span>: Layer Normalisation, Skip connections + add positional embedding!

## Output Transformations

$tokens \in \R^D \rightarrow output$

- Simple: linear or small MLP, task dependent (classification/multiple outputs)
