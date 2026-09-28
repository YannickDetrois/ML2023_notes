---
title: "Logistic regression"
chapter: 10
---

# Logistic regression

Logistic function $\sigma(\eta):=\frac{e^\eta}{1+e^\eta}$. We have $1-\sigma(\eta) = \frac{1}{1+e^\eta}$ and $\sigma'(\eta):=\sigma(\eta)(1-\sigma(\eta))$

Robust against outliers and unbalanced data. If $\sigma(x)>\frac{1}{2}$, then for $a > 0, \sigma(ax)>\frac{1}{2}$

<span class="c-teal">**Optimality**</span>:

- linear for $y \in \{1, 0\}$: $w_* = \text{arg} \min_w \mathcal{L} := \frac{1}{N}\sum_{n=1}^N-y_n x_n^\top w + \log (1+e^{x_n^\top w})$
- generic $h$ for $y \in \{1, 0\}$: $\mathcal{L}(y, h(x)) = -yh(x) + \log (1+e^{h(x)})$
- generic $h$ for $y \in \{-1, 1\}$: $\mathcal{L}(y, h(x)) = \log (1+e^{-yh(x)})$

**<span class="c-blue">Gradient</span>**:

- linear problem convex and $\nabla \mathcal{L}(w)=\frac{1}{N} \mathbf{X}^\top(\sigma(\mathbf{X}w)-y))$

**<span class="c-purple">Hessian</span>**:

- $\nabla^2 \mathcal{L}(w)=\frac{1}{N} \mathbf{X}^\top S \mathbf{X}$, where $S=\text{diag}[\sigma(x_n^\top w)(1-\sigma(x_n^\top w))] \geq 0$
- Hessian is psd → loss is convex
- Newton’s method: $\mathbf{w}^{(t+1)}:=\mathbf{w}^{(t)}-\gamma^{(t)} \nabla^2 \mathcal{L}(\mathbf{w^{(t)}})^{-1}\nabla \mathcal{L}(\mathbf{w^{(t)}})$

When data is linearly separable, weights $w \rightarrow \infty$ even though all points are well separated. Solution: add $L_2$ regularisation
