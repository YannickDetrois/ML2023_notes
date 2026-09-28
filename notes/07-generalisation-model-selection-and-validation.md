---
title: "Generalisation, model selection and validation"
chapter: 7
---

# Generalisation, model selection and validation

Generalisation gap: how far is the test from the true error?

Given $K$ different models $f_K$, an iid test set $\text{S}_\text{test}\sim \mathcal{D}$ (that follows the true data distribution) and a loss $\mathcal{L} \in [a, b]$:

$$
\mathbb{P} \left[ \max_K|\mathcal{L}_\mathcal{D}(f_K)-\mathcal{L}_{\text{S}_\text{test}}(f_K)| \geq \sqrt{\frac{(b-a)^2\ln(\frac{2K}{\delta})}{2|\text{S}_\text{test}|}} \right] \leq \delta
$$

To remove the absolute value, put 2 in front of the square root and take the values of $K$ for which the functions $f_{\hat k}$ and $f_{k^*}$ have the smallest empirical or true risk respectively.

<u>Hoeffding inequality</u> $\forall \epsilon \geq 0$, $\Theta_n$ are the loss functions

$$
\mathbb{P} \left[ |\frac{1}{N}\sum_{n=1}^N \Theta_n - \mathbb{E}[\Theta]| \geq \epsilon \right] \leq 2e^{{\frac{-2N\epsilon^2}{(b-a)^2}}}
$$

<u>Hoeffding lemma</u> $\forall s \geq 0$, and RV $\mathbf{X} \in [a,b]$ with $\mathbb{E}[\mathbf{X}] = 0$

$$
\mathbb{E} \left[ e^{sX} \right] \leq e^{{\frac{1}{8}s^2(b-a)^2}}
$$

K-fold cross validation returns an unbiased estimate of the generalisation-error and its variance
