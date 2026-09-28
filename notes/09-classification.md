---
title: "Classification"
chapter: 9
---

# Classification

The optimal classification performance is the **Bayers classifier** $:= g_* = \text{arg} \min_g \mathcal{L}_\mathcal{D}(g)$

$g_*(x) = \text{arg} \max_{y \in \{ -1, 1\}} \mathbb{P}(Y=y|X=x)$

## Loss functions

- (0-1 Loss) → $\mathcal{L}(y, y')=1_{y \neq y'}$ which is 1 if $y \neq y'$ and 0 if $y = y'$
- True risk for classification for a predictor $g$ → $\mathcal{L}_\mathcal{D}(g)=\mathbb{E}_\mathcal{D}[1_{Y \neq g(X)}] = \mathbb{P}_\mathcal{D}[Y \neq g(X)]$
- Convex and continuous losses ($\eta = yx^\top w)$:
  - quadratic loss $:= (1-\eta)^2$ → symmetric but only works for $[-\infty, 2]$
  - hinge loss $:= [1-\eta]_+$ → penalty on $[-\infty, 2]$ (prediction wrong or not confident)
  - logistic loss $:= \frac{\ln(1+e^{-\eta})}{\ln(2)}$ → always penalising

<span class="c-orange">Non-parametric</span>

Approximate conditional distribution $\mathbb{P}(Y=y|X=x)$ via local averaging (KNN)

<span class="c-blue">Parametric</span>

Approximate true distribution $\mathcal{D}$ via training data → minimise empirical risk (ERM)

Instead of learning function $g: X\rightarrow \{-1, 1\}$, we learn a continuous function $h$ and predict with $g(x) = \text{sign}(h(x))$. We replace the 0-1 loss by a convex and continuous surrogate $\phi$:

$$
\min_{h\in \mathcal{H}} \frac{1}{N} \sum_{n=1}^N \phi(y_nh(x_n))
$$

In the over-parameterisation $(n<<d)$ regime, the training data is well fit with a regressor → a good regressor can be used as a classifier
