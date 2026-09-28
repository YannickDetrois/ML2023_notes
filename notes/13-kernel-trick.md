---
title: "Kernel trick"
chapter: 13
---

# Kernel trick

Covariance matrix $\mathbf{X}^\top \mathbf{X}\in \R^{D\times D}$, Kernel matrix $\mathbf{X}\mathbf{X}^\top\in \R^{N\times N}$

→ Ridge regression $\mathbf{w}^*=\frac{1}{N}\mathbf{X}^\top (\frac{1}{N} \mathbf{X} \mathbf{X}^\top+\lambda\mathbf{I}_N)^{-1} \mathbf{y}$ complexity $\mathcal{O}(DN^2+N^3)$

**<span class="c-purple">Representer theorem</span>**: For any loss $\mathcal{L}$ there exists $\alpha_* \in \R^N$, where $R(w)$ is any increasing regularisation term, such that

$$
w_* = \mathbf{X}^\top \alpha_* \in \text{arg} \min_w \frac{1}{N}\sum_{n=1}^N \mathcal{L}(x_n^\top w, y_n) + R(w)
$$

<span class="c-purple">**Kernel trick**</span>: Kernel function $\kappa(x, x') = \phi(x)^\top \phi(x')$ → computation of linear classifiers in high-dimensional space $\phi(x_n) \in \R^{\tilde d}$ without computing directly in that space. Prediction with kernel: $y=\phi(x)^\top w_* = \sum_{n=1}^N \kappa(x, x_n)\alpha_{*n}$ (non-linear prediction in $X$ space but linear in feature space $\phi(X)$)

1. **Linear kernel**: $\kappa(x, x') = x^\top x' \rightarrow \phi(x)=x$
2. **Quadratic kernel**: $\kappa(x, x') = (x x')^2 \rightarrow \phi(x)=x^2$ (for $x, x' \in \R$)
3. **Polynomial kernel**: $\kappa(x, x') = (x_1 x_1'+x_2 x_2'+x_3 x_3')^2$<br><br>$\rightarrow \phi(x)=[x_1^2, x_2^2, x_3^2, \sqrt{2}x_1x_2, \sqrt{2}x_1x_3, \sqrt{2}x_2x_3] \in \R^6$ (for $x, x' \in \R^3$)
4. **Radial basis function (RBF) kernel**:
   1. $x, x' \in \R^d$: $\kappa(x, x') = e^{-(x-x')^\top(x-x')}$
   2. $x, x' \in \R$: $\kappa(x, x') = e^{-(x-x')^2} \rightarrow \phi(x)=e^{-x^2}(..., \frac{2^{\frac{k}{2}}x^k}{\sqrt{k!}},...)$ for $0\leq k<\infty$

Building new kernels from existing ones:

- $\kappa(x, x') = \alpha \kappa_1(x, x') + \beta \kappa_2(x, x')$ is a kernel for $\alpha, \beta \geq 0$
- $\kappa(x, x') = \kappa_1(x, x') \kappa_2(x, x')$ is a kernel

**Mercer’s condition**: $\exist \phi(x)$ such that $\kappa(x, x') = \phi(x)^\top \phi(x')$ iff

1. kernel function is symmetric: $\kappa(x, x') = \kappa(x', x)$ $\forall x, x'$
2. kernel matrix is psd: $\kappa(x, x') \geq 0$
