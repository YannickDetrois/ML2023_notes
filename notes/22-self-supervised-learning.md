---
title: "Self-supervised learning"
chapter: 22
---

# Self-supervised learning

Use **pretext tasks** $f:\mathbf{x}_{in} \mapsto \mathbf{x}_{out}$ that learn from unlabelled data with a function $g: \mathbf{x} \mapsto(\mathbf{x}_{in}, \mathbf{x}_{out})$ that creates the data (e.g. predict image rotation, relative patch placement) → only need to corrupt data to create training pairs

<span class="c-orange">**Masked Language Modelling (MLM)**</span>: predict hidden word `[MASK]`

- **Bidirectional Encoder Representations from Transformers (BERT)**: Encoder only, can look at both previous and following tokens. Pretext tasks: 1.predict original masked token 2. predict whether second sentence immediately follows first sentence `[CLS]` . Fine-tuned for sentiment prediction, noun/verb prediction, find start/end of passage.
- **Next token prediction - Generative Pre-trained Transformers (GPT)**: Decoder only, can look only at prior tokens (masked attention). Auto-regressive → uses previous output to compute loss (softmax cross-entropy) for next output. Fine-tuned for in-context learning or instruction following.
- **Joint Embedding Methods**: Learn encoder invariants (e.g. rotations) by creating views (rotations, distorsions) of an original image
- **Contrastive learning**: positive pair $\mathbf{x}, \mathbf{x}^+$ and negative view $\mathbf{x}^-$ → $s(f(\mathbf{x}), f(\mathbf{x}^+)) > s(f(\mathbf{x}), f(\mathbf{x}^-))$, where $s$ is a similarity function (e.g. cosine similarity)
  - **SimCLR**:
    1. classification with $N$ negative samples
    2. map encoder output to the similarity $f(\mathbf{x})=f_2 \circ f_1(\mathbf{x})$ use only $f_1$ for downstream tasks
    3. use cosine similarity with temperature scaling $\tau: s(\mathbf{e}_1, \mathbf{e}_2)=\frac{\langle\mathbf{e}_1, \mathbf{e}_2 \rangle}{||\mathbf{e}_1||_2||\mathbf{e}_2||_2}/\tau$
    4. generate views with data augmentation
  - **CLIP**: captioned images to learn a joint multimodal embedding space
