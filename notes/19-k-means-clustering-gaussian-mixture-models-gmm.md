---
title: "K-Means Clustering, Gaussian Mixture Models (GMM)"
chapter: 19
---

# K-Means Clustering, Gaussian Mixture Models (GMM)

## <u>K-Means Clustering</u>

**<span class="c-purple">Objective</span>**:

- For all $N$ data vectors $x_n \in \R^D$: find cluster means $\mu_1, ..., \mu_K$ and cluster assignments $z_{nk} = \begin{cases} 1 & \text{if } x_n \in \text{cluster} K \\ 0 & \text{if } x_n \notin \text{cluster} K \end{cases} \in \R^D$
- Assuming $K$ is known, we are searching $\min_{z, \mu} \mathcal{L}(z, \mu) = \sum^N \sum^K z_{nk} ||x_n-\mu_k||^2_2$

**<span class="c-yellow">Algorithm</span>**: Initialise $\mu_k$ $\forall k$, then

1. For all $n$ compute $z_n$ given $\mu$ (cost $\mathcal{O}(NKD)$) → $z^{(t+1)}:=\text{arg} \min_z \mathcal{L}(z, \mu^{(t)})$<br> <br>$z_{nk} = \begin{cases} 1 & \text{if } k = \text{arg} \min_j ||x_n-\mu_j||^2_2 \\ 0 & \text{otherwise}\end{cases}$
2. For all $k$ compute the group means $\mu_k$ given $z$ (cost $\mathcal{O}(NKD)$)

   → $\mu^{(t+1)}:=\text{arg} \min_\mu \mathcal{L}(z^{(t)}, \mu)$ and $\mu_k = \frac{\sum^N z_{nk}x_n}{\sum^N z_{nk}}$

3. Repeat until there is no more change in assignment → no more change of the $\mu_k$

→ Convergence to a <u>local optimum</u> is assured since each step decreases the cost

<span class="c-teal">**K-means as matrix factorisation**</span>:

$\min_{z, \mu} \mathcal{L}(z, \mu) = \sum^N \sum^K z_{nk} ||x_n-\mu_k||^2_2 = ||\mathbf{X}^\top - \mathbf{MZ}^\top||^2_F$

The matrix $\mathbf{M} \in \R^{D\times K}$ contains the $K$ mean vectors $\mu_K$ and $\mathbf{Z^\top} \in \R^{K\times N}$ contains the $N$ assignment vectors. Convex in $\mathbf{M}$ and $\mathbf{Z}$ but not jointly convex.

Frobenius norm: $||A||_F = \sqrt{\sum^M \sum^N |a_{mn}|^2} = \sqrt{\text{tr}(A^*A)}$

## <u>Gaussian Mixture Models</u>

- Elliptical clusters and soft-assignment
- Bayes’ Law: $p(a, b)=p(a|b)p(b)$
- Multivariate normal distribution<br><br>$f(\mathbf{x};\mathbf{\mu},\mathbf{\Sigma}) = \frac{1}{(2\pi)^{k/2}|\mathbf{\Sigma}|^{1/2}} \exp\left(-\frac{1}{2}(\mathbf{x}-\mathbf{\mu})^T\mathbf{\Sigma}^{-1}(\mathbf{x}-\mathbf{\mu})\right)$
- Added $\Sigma \in \R^{D^2 \times K}$ (covariance matrices) and $\Pi \in \R^K$ (cluster probabilities) such that $p(z_n = k) = \pi_k$ where $\pi_k > 0$ for all $k$ and $\sum_{k=1}^{K} \pi_k =1$

  → <span class="c-orange">New parameters </span><span class="c-orange">$\theta = \{\mu_1, ..., \mu_K, \Sigma_1, ..., \Sigma_K, \pi\}$</span>

- marginal likelihood $p(x_n|\theta)=\sum_{k=1}^K\pi_k \mathcal{N}(x_n|\mu_k, \Sigma_k)$ → $\mathcal{O}(D^2K)$ parameters left
- Searching $\theta^* = \text{arg}\max_\theta \sum_{n=1}^N\log\sum_{k=1}^K \pi_k\mathcal{N}(x_n|\mu_k, \Sigma_k)$
  - Not convex, not identifiable (permutation), not bounded ($\sigma \rightarrow 0)$

## <u>Expectation-Maximisation (EM) algorithm</u>

- In short: $\theta^{(t+1)}:= \text{arg}\max_\theta \sum_{n=1}^N \mathbb{E}_{p(z_n|x_n, \theta^{(t)})}[\log p(x_n, z_n|\theta)]$
- **<span class="c-red">Expectation step</span>**: find lower bound $\underline{\mathcal{L}}$ such that $\mathcal{L}(\theta) \geq \underline{\mathcal{L}}(\theta, \theta^{(t)})$ and $\mathcal{L}(\theta^{(t)}) = \underline{\mathcal{L}}(\theta^{(t)}, \theta^{(t)})$
  - Concavity of log: Jensen’s inequality: $\log \left(\sum_{k=1}^K q_kr_k\right) \geq \sum_{k=1}^K q_k\log r_k$ for $r_k >0$ and $\sum_k q_k = 1$
  - Jensen’s inequality with $q_k = \frac{\pi_k^{(t)} \mathcal{N}(x_n|\mu_k^{(t)}, \Sigma_k^{(t)})}{\sum_{k=1}^K\pi_k^{(t)} \mathcal{N}(x_n|\mu_k^{(t)}, \Sigma_k^{(t)})}$ and $r_k = \frac{\pi_k \mathcal{N}(x_n|\mu_k, \Sigma_k)}{q_k}$
- **<span class="c-purple">Maximisation step</span>**:
  - $\theta^{(t+1)}=\text{arg}\max_\theta \underline{\mathcal{L}}(\theta, \theta^{(t)})$
  - $\mu_k^{(t+1)}:=\frac{\sum_n q_{kn}^{(t)} x_n}{\sum_n q_{kn}^{(t)}}$
  - $\Sigma_k^{(t+1)}:=\frac{\sum_n q_{kn}^{(t)} (x_n-\mu_k^{(t+1)})(x_n-\mu_k^{(t+1)})^\top}{\sum_n q_{kn}^{(t)}}$
  - $\pi_k^{(t+1)}:=\frac{1}{N}\sum_n q_{kn}^{(t)}$
- **<span class="c-blue">Posterior distribution</span>**:
  - $p(x_n, z_n|\theta) = p(x_n| z_n,\theta)p(z_n|\theta) = p(z_n | x_n,\theta)p(x_n|\theta)$
  - $\text{joint} = \text{likelihood} \cdot \text{prior} = \text{posterior} \cdot \text{marginal likelihood}$
  - $\text{joint} = \mathcal{N}(x_n|\mu_k, \Sigma_k) \cdot \pi_k = q_{kn} \cdot \sum_{k=1}^K\pi_k \mathcal{N}(x_n|\mu_k, \Sigma_k)$
