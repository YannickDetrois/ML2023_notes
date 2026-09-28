---
title: "Matrix factorisations"
chapter: 20
---

# Matrix factorisations

Aim to find $\mathbf{W} \in \R^{D\times K}$ (e.g. movies) and $\mathbf{Z^\top} \in \R^{K\times N}$ (e.g. users) such that $\mathbf{X}\approx \mathbf{WZ}^\top$, where each user and movie are described by a vector in $\R^K$ and $x_{dn}$ such that $(d,n)\in\Omega$ contains the existing rating of user $n$ for movie $d$ $(K\ll D,N)$. We are minimising:

$$
\min_{\mathbf{W,Z}} \mathcal{L}(\mathbf{W,Z}) := \frac{1}{2}\sum_{(d,n)\in\Omega}[x_{dn}-(\mathbf{WZ}^\top)_{dn}]^2
$$

Regularisation (not matrix factorisation anymore): add $\frac{\lambda_w}{2}||\mathbf{W}||^2_F$ or $\frac{\lambda_z}{2}||\mathbf{Z}||^2_F$, $\lambda_w, \lambda_z>0$

**<span class="c-orange">SGD</span>**:

- For a fixed element $(d,n)$:

  $\frac{\partial \mathcal{L}_{dn}}{\partial w_{d',k}}(\mathbf{W,Z}) = \begin{cases} -[x_{dn}-(\mathbf{WZ}^\top)_{dn}]z_{n,k} & \text{if } d'=d \\ 0 & \text{otherwise} \end{cases} \in \R^K$

  $\frac{\partial \mathcal{L}_{dn}}{\partial z_{n',k}}(\mathbf{W,Z}) = \begin{cases} -[x_{dn}-(\mathbf{WZ}^\top)_{dn}]w_{d,k} & \text{if } n'=n \\ 0 & \text{otherwise} \end{cases} \in \R^K$

**<span class="c-yellow">Alternating Least Squares (ALS)</span>**:

- Assuming no missing entries. First update $\mathbf{Z}$ with fixed $\mathbf{W}$ then $\mathbf{W}$with fixed $\mathbf{Z}$
- $\mathbf{Z}^\top:=(\mathbf{W}^\top\mathbf{W}+ \lambda_z\mathbf{I}_K)^{-1}\mathbf{W}^\top\mathbf{X}$
- $\mathbf{W}^\top:=(\mathbf{Z}^\top\mathbf{Z}+ \lambda_w\mathbf{I}_K)^{-1}\mathbf{Z}^\top\mathbf{X}$
