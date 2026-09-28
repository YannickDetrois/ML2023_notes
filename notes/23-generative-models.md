---
title: "Generative Models"
chapter: 23
---

# Generative Models

Creates more form the learned distribution $p(x)$. *Explicit* → learn distribution. *Implicit* → only generating samples according to distribution.

<img src="../images/23-generative-models-1.png" alt="" width="240">

<img src="../images/23-generative-models-2.png" alt="" width="528">

<span class="c-orange">**Generative Adversarial Networks**</span>: Create images from known noise distribution $p_z$. 2-player game: <span class="c-teal">generator </span><span class="c-teal">$G(\theta)$</span> vs. <span class="c-red">discriminator </span><span class="c-red">$D(\varphi)$</span> (deep NNs). $T$ steps gradient descent for steps

1. <span class="c-red">$\varphi^*\in\text{arg} \min_{\varphi \in \Phi} \mathcal{L}^\varphi(\theta^*, \varphi)$</span> → distinguishes real ($x \sim p_d$) vs. generated images $G(z)$
2. <span class="c-teal">$\theta^*\in\text{arg} \min_{\theta \in \Theta} \mathcal{L}^\theta(\theta, \varphi^*)$</span> → creates realistic images $G(z)$
3. Objective: $\min_G \max_D \mathbb{E}_{x \sim p_d}[\log D(x)] + \mathbb{E}_{z \sim p_z}[\log (1-D(G(z)))]$
4. Theoretical solution: optimum when $p_g = p_d$ with value $- \log4$

→ **Conditional GAN (CGAN)**: additional information $c$ (e.g. class labels)

<span class="c-orange">**Diffusion models**</span>: forward decomposition → add noise, backward decomposition → undo noise Use ancestral sampling starting from a pure Gaussian noise and denoising using Markov chain. Often use U-net architecture (with exponential moving average to stabilise training) with ResNet blocks and self-attention layers. To add additional information $y$ (conditional training), the probabilities of neural net $s_\theta$ should be conditional on $Y$.

<img src="../images/23-generative-models-3.png" alt="" width="1464">
