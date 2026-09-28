---
title: "Optimisation"
chapter: 3
---

# Optimisation

Find $\mathbf{w}^* \in \R^D$ such that it is $\text{min}_\mathbf{w} \mathcal{L}(\mathbf{w})$

<span class="c-yellow">**Grid search**</span>: $n$ parameters per dimension → $n^D$ evaluations and no guarantee to find minimum

<span class="c-orange">**Gradient descent**</span>: $\nabla \mathcal{L}(\mathbf{w}) := \left[ \frac{\partial \mathcal{L}(\mathbf{w})}{\partial w_1}, ..., \frac{\partial \mathcal{L}(\mathbf{w})}{\partial w_D} \right] \in \R^D$

- $\mathbf{w}^{(t+1)}:=\mathbf{w}^{(t)}-\gamma \nabla \mathcal{L}(\mathbf{w^{(t)}})$
- Linear MSE: $\mathbf{e = y-Xw}$
  - $\mathcal{L}(\mathbf{w}) = \frac{1}{2N}\mathbf{e}^\top\mathbf{e}$
  - $\nabla \mathcal{L}(\mathbf{w}) = -\frac{1}{N}\mathbf{X}^\top\mathbf{e}$
  - Global complexity $\mathcal{O}(ND)$

<span class="c-brown">**SGD**</span>:

- $\mathbf{w}^{(t+1)}:=\mathbf{w}^{(t)}-\gamma \nabla \mathcal{L}_n(\mathbf{w^{(t)}})$
- Cheap but unbiased estimate of the gradient
- Global complexity $\mathcal{O}(D)$

**<span class="c-red">Mini-batch SGD</span>**:

- $g:=\frac{1}{|B|} \sum_{n \in B}\nabla \mathcal{L}_n(\mathbf{w^{(t)}})$, B is a subset of the N samples
- $\mathbf{w}^{(t+1)}:=\mathbf{w}^{(t)}-\gamma g$

<span class="c-blue">**Subgradient descent**</span>:

- Convexity for differentiable functions: $\mathcal{L}(\mathbf{u}) \geq \mathcal{L}(\mathbf{w})+\nabla \mathcal{L}(\mathbf{w})^\top(\mathbf{u}-\mathbf{w})$
- Subgradient $g \in \partial \mathcal{L}$: $\mathcal{L}(\mathbf{u}) \geq \mathcal{L}(\mathbf{w})+g^\top(\mathbf{u}-\mathbf{w})$

**<span class="c-teal">Projected gradient descent</span>**:

- Intersections of convex sets are convex
- Projection on convex constraint set $\mathcal{C}$ after each gradient descent step
- Turn into unconstrained problem: penalty function if not in $\mathcal{C}$
