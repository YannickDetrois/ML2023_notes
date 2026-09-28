---
title: "Regularisation"
chapter: 6
---

# Regularisation

Penalise complex models: $\text{min}_\mathbf{w} \mathcal{L}(\mathbf{w}) + \Omega(\mathbf{w})$

- $L_2$-regularisation (ridge): $\Omega(\mathbf{w})=\lambda||\mathbf{w}||_2^2$
  - Gradient is $2\mathbf{w}$
  - Model small in magnitude
- $L_1$-regularisation (lasso): $\Omega(\mathbf{w})=\lambda||\mathbf{w}||_1$
  - Gradient is $\text{sign}(\mathbf{w})$
  - Model is sparse
- $L_0$-regularisation (lasso): $\Omega(\mathbf{w})=\#(\mathbf{w} \neq 0)$
- Shrinkage, dropout, weight decay, early stopping
