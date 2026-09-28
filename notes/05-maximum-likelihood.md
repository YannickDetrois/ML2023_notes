---
title: "Maximum Likelihood"
chapter: 5
---

# Maximum Likelihood

Maximising the likelihood instead of minimising the loss. Our data is $y_n = \mathbf{x}^\top_n \mathbf{w} + \epsilon_n$, where $\epsilon_n$ is a random variable (e.g. Gaussian) that is iid across $n$.

Log likelihood $\mathcal{L}_{LL}(\mathbf{w}) := \log p(\mathbf{y}|\mathbf{X}, \mathbf{w}) = \sum_{n=1}^N p(y_n|\mathbf{x}_n, \mathbf{w})$
