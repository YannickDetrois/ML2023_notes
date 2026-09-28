---
title: "Nearest Neighbour Classifiers"
chapter: 12
---

# Nearest Neighbour Classifiers

KNN can be used for:

- <span class="c-yellow">**regression**</span>: for point $x$, find the $K$ closest points $y_k$ (the $K$ points in the neighbourhood) → the estimate is then given by $f_K(x)=\frac{1}{K} \sum^Ky_k$
- **<span class="c-yellow">classification</span>**: get $K$ closest neighbours of $x$ and count how many are in groups $a$ or $b$ → assign group of point $x$ depending on the majority group in the neighbourhood

Small $K$ → complex decision boundary → low bias, high variance (overfitting)

Large $K$ → when $k=N$ prediction is constant → high bias, low variance

<span class="c-teal">**Curse of dimensionality**</span>: $N$ i.i.d. points uniform in $[0,1]^d \rightarrow \mathbb{P}(\exist x_i \in \square^d) = 1-(1- r^d)^N$

<span class="c-teal">**Generalisation bound for 1-NN**</span>: $\mathbf{X} \times \mathbf{Y} = [0,1]^d \times \{0,1\}$

- Bayes classifier minimises $\mathcal{L}$ over all classifiers $f_*(x)= 1_{\eta(x)\geq\frac{1}{2}}$ where<br> <br>$\eta(x)=\mathbb{P}(Y=1|X=x)$
- Bayes risk: $\mathcal{L}(f_*)=\mathbb{P}(f_*(X)\neq Y)=\mathbb{E}_{X\sim \mathcal{D_X}}[\min\{\eta(x), 1-\eta(x)\}]$
- <u>Assumption</u>: $\exist c \geq 0$, $\forall x, x' \in X$: $|\eta(x)-\eta(x')| \leq c||x-x'||_2$ (Lipschitz with ct. c)<br>→ nearby points are likely to share the same label
- <u>Claim</u>: $\mathbb{E}_{S_{train}}[\mathcal{L}(f_{S_{train}})] \leq 2 \mathcal{L}(f_*) + 4c \sqrt{d}N^{-\frac{1}{d+1}}$
- To achieve constant error we need $N \propto d^{\frac{d+1}{2}}$
- $\mathbb{P}(Y'\neq Y) \leq 2\min\{\eta(x), 1- \eta(x)\}+c||x-x'||$
- Let $p_k = \mathbb{P}(X \in \text{Box}_k)$, then sample $X$ has probability $1-(1-p_k)^N$ to have a neighbour in $S_{train}$ in the box at distance $\leq \sqrt{d}\epsilon$ ($\epsilon$ is Box edge lenght) and probability $(1-p_k)^N$ to not have a neighbour in the box (closest neighbour $\leq \sqrt{d}$)
- $\mathbb{E}[||X-\text{nbh}(X)||] \leq \sum_k p_k[(1-p_k)^N \sqrt{d} + (1-(1-p_k)^N) \sqrt{d}\epsilon]$
- Local averaging methods aim to approximate the Bayes’ predictor directly by approximating the conditional distribution $\hat p(y|x)$. For $N \rightarrow \infty$, 1-NN is competitive with Bayes’ classifier
