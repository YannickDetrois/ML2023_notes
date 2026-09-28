---
title: "Loss functions"
chapter: 2
---

# Loss functions

Desirable: symmetric around 0, penalise large and very large mistakes similarly

- $\text{MSE(w)} = \frac{1}{N} \sum_{n=1}^{N} e_n^2 = \frac{1}{N} \sum_{n=1}^{N} [y_n - f_\mathbf{w}(\mathbf{x}_n)]^2$ → not good for outliers
- $\text{MAE(w)} = \frac{1}{N} \sum_{n=1}^{N} |e_n| = \frac{1}{N} \sum_{n=1}^{N} |y_n - f_\mathbf{w}(\mathbf{x}_n)|$ → good for outliers

## Convexity

Function $h(u)$ is convex if for any $u, v \in \R^D$ and for any $0 \leq \lambda \leq 1$ we have:

$$
h(\lambda u + (1-\lambda)v) \leq \lambda h(u) + (1-\lambda)h(v)
$$

A strictly convex function has a unique global minimum. For convex functions, every local minimum is a global minimum. Sums of convex functions and compositions of convex functions with convex non-decreasing functions are convex.
