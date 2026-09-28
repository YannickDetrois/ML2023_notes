---
title: "Adversarial machine learning"
chapter: 16
---

# Adversarial machine learning

Adversarial risk of classifier $f$: $R_\epsilon(f)=\mathbb{E}_\mathcal{D}\left[ \max_{\hat x, ||\hat x- X|| \leq \epsilon} 1_{f(\hat x)\neq Y} \right]$ → optimise the input $x$ to get maximum error (easy if already misclassified, else need to optimise). Use smooth classification loss $\ell$ instead of (0-1): output before classification is $g$, classify with $\text{sign}(g(x))$. Then the objective is equivalent to $\max_{\hat x, ||\hat x- X|| \leq \epsilon} \ell(yg(\hat x)) \Leftrightarrow \max_{||\delta|| \leq \epsilon} \nabla_x \ell(yg(x))^\top \delta$ because $g(x+\delta) \approx g(x) + \delta^\top\nabla_x g(x)$ (Taylor series)

**<span class="c-blue">White box attacks</span>**: model $g$ is known

- compute gradient $\nabla_x \ell$ during back-propagation to move in the direction opposite to the right classification
- one-step attack:
  - $\ell_2$ norm: $\hat x = x-\epsilon y \frac{\nabla_x g(x)}{||\nabla_x g(x)||_2}$
  - $\ell_\infty$ norm: $\hat x = x-\epsilon y \cdot \text{sign}(\nabla_x g(x))$
- multi-step attack: Projected Gradient Descent (PGD): iteratively update $\delta$ and project back on the feasible set $||\delta||\leq \epsilon$
  - $\ell_2$ norm: $\delta^{t+1} = \Pi_{B_2(\epsilon)} \left[\delta^t+\alpha \frac{\nabla \tilde \ell (x+ \delta^t)}{||\nabla \tilde \ell (x+ \delta^t)||_2} \right]$ <br>with <br>$\Pi_{B_2(\epsilon)}(\delta) = \begin{cases}\epsilon \cdot \delta/||\delta||_2 & \text{if } ||\delta||_2 \geq \epsilon \\ \delta & \text{otherwise}\end{cases}$
  - $\ell_\infty$ norm: $\delta^{t+1} = \Pi_{B_\infty(\epsilon)} \left[\delta^t+\alpha \cdot \text{sign}( \nabla \tilde \ell (x+ \delta^t)) \right]$<br>with <br>$\Pi_{B_\infty(\epsilon)}(\delta)_i = \begin{cases}\epsilon \cdot \text{sign}(\delta_i) & \text{if } |\delta_i| \geq \epsilon \\ \delta_i & \text{otherwise}\end{cases}$

<span class="c-blue">**Black box attacks**</span>: model $g$ unknown

- <u>score-based</u>: we can query model scores $g(x)$ → approximate gradient using finite difference
- <u>decision-based</u>: we can query only prediction $f(x)$
- <u>transfer attacks</u>: train $\hat f \approx f$ on similar data → transfer white box ($\hat f$) attack on $f$<br>Query with unlabelled data to obtain <br>$\{x_n, f(x_n)\}$ → model stealing

**<span class="c-blue">Create robust models</span>**:

- Minimise the adversarial risk → train model on best adversarial example $\hat x_n^*$
- increased computational time + robustness/accuracy tradeoff (non-robust feature may be more accurate but can have high adversarial risk while robust has less than ideal accuracy but better resistance to attacks)
