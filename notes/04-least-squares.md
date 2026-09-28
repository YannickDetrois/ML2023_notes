---
title: "Least squares"
chapter: 4
---

# Least squares

Gram matrix $\mathbf{X}^\top \mathbf{X}\in \R^{D\times D}$. Closed form for optimal $\mathbf{w}^*$ given by $\mathbf{X}^\top \mathbf{X} \mathbf{w}^*=\mathbf{X}^\top \mathbf{y}$. The Gram matrix is invertible iff $\mathbf{X} \in \R^{N \times D}$ has full column rank. Complexity is $\mathcal{O}(ND^2+D^3)$

- $L_2$-regularisation closed form with $\lambda' = 2N \lambda$: $(\mathbf{X}^\top \mathbf{X}+\lambda'\mathbf{I}_d) \mathbf{w}^*=\mathbf{X}^\top \mathbf{y}$
- Eigenvalues of $(\mathbf{X}^\top \mathbf{X}+\lambda'\mathbf{I})$ are at least $\lambda'$
