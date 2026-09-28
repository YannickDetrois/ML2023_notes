---
title: "Ethics and fairness"
chapter: 17
---

# Ethics and fairness

No fairness through unawareness! Minorities may be underrepresented → high error rates for minorities (because we aim to avoid overfitting).

Consider we have data $X$, outcome variables $Y$ and a score function $R=r(X)$ that allows to make classification decisions $D=1_{R>t}$. Furthermore, let $A$ be a RV that encodes membership status in a protected class.

|  | $D=0$ | $D=1$ |
|---|---|---|
| $Y=0$ | **<span class="c-teal">True negative</span>**<br>Probability <br>$1-\alpha$ | **<span class="c-red">Type I error</span>**<br>False positive<br>Probability <br>$\alpha$ |
| $Y=1$ | **<span class="c-red">Type II error</span>**<br>False negative<br>Probability <br>$\beta$ | **<span class="c-teal">True positive</span>**<br>Probability <br>$1-\beta$ |

- $\text{TPR} = \mathbb{P}(D=1|Y=1)$
- $\text{FPR} = \mathbb{P}(D=1|Y=0)$
- $\text{FNR} = \mathbb{P}(D=0|Y=1)$
- $\text{TNR} = \mathbb{P}(D=0|Y=0)$

<span class="c-yellow">**Fairness criteria**</span>: equalise statistical quantities involving two groups $a,b \in$ $A$

- **Independence**: $R \perp A$
  - Acceptance rate (decision $D$) does not depend on group $A$
  - $\mathbb{P}(D=1|A=a)=\mathbb{P}(D=1|A=b)$
  - Counting both true and false positive decisions, but should not compare them!
- **Separation**: $R \perp A | Y$
  - Post-hoc criterion, but compares by label
  - $\text{FPR}(a) = \mathbb{P}(D=1|Y=0, A=a) = \text{FPR}(b)$
  - $\text{FNR}(a) = \text{FNR}(b)$
- **Sufficiency**: $Y \perp A|R$
  - Meaning for predicting $Y$ we do not need to know $A$ if we have $R$
  - $\mathbb{P}(Y=1|R=r, A=a) = \mathbb{P}(Y=1|R=r, A=b)$
  - Calibrated by group, i.e. $\mathbb{P}(Y=1|R=r, A=a) = r$ implies sufficiency
- Any of these criteria are **mutually exclusive!**
  - Independence vs. sufficiency: $A \perp R$ and $A \perp Y|R \Rightarrow A \perp (Y,R) \Rightarrow A \perp Y$
  - Independence vs. separation: $A \perp R$ and $A \perp R|Y \Rightarrow A \perp Y$ or $R \perp Y$
  - Separation vs. sufficiency: $A \perp R|Y$ and $A \perp Y|R \Rightarrow A \perp (R,Y)$
