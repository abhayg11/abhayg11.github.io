---
layout: post
title: Spherical completeness of \(\mathbb{C}_p\)
mathjax: true
---

I recently sought a proof that \\(\mathbb{C}_p\\) is not spherically complete. I've since proved this in two separate ways, which I'd like to detail here.

## The problem

Recall that \\(\mathbb{Z}\_p\\) is the ring of \\(p\\)-adic integers, the completion of the localization \\(\mathbb{Z}\_{(p)}\\) with respect to the (usual) \\(p\\)-adic absolute value; \\(\mathbb{Q}\_p\\) is the field of \\(p\\)-adic numbers, the field of fractions of \\(\mathbb{Z}\_p\\); \\(\overline{\mathbb{Q}\_p}\\) is a (fixed) algebraic closure, equipped with the unique extension of the \\(p\\)-adic absolute value; and \\(\mathbb{C}\_p = \widehat{\overline{\mathbb{Q}\_p}}\\) is the completion of \\(\overline{\mathbb{Q}\_p}\\) with respect to its absolute value, itself equipped with an extension of the absolute value.

It is well-known that \\(\mathbb{C}\_p\\) is algebraically closed and complete with respect to the absolute value. On the other hand, we will show that it is not **spherically complete**. That is, there exists a sequence of nested closed spheres (of positive radii) with empty intersection. Contrast this with [&#x21B7;Cantor's intersection theorem](https://en.wikipedia.org/wiki/Cantor%27s_intersection_theorem).

## Nonconstructive proof

First, we will describe a non-constructive proof. We need a few Lemmas first.

```latex
Lemma 1: If \(r > s > 0\) and \(X\) is a closed ball in \(\mathbb{C}_p\) of radius \(r\), then there are two disjoint balls of radius \(s\) contained in \(X\).
Proof.
We can write \(X = B_r(x)\) for some \(x \in \mathbb{C}_p\). Choose \(\alpha,\beta \in \mathbb{C}_p\) with \(|\alpha| < s < |\beta| < r\). Then, we claim that \(B_s(x+\alpha)\) and \(B_s(x+\beta)\) are the relevant balls.

First, we show these are contained in \(X\). Suppose \(y \in B_s(x+\alpha)\). Then \(|y-x| = |y-(x+\alpha)+\alpha| \leq \max\{|y-(x+\alpha)|,|\alpha|\} < r\), so that \(y \in X\). The same argument works for the other ball. Finally, the two are disjoint. Indeed, if \(y\) were in both balls, then, \(|\alpha-\beta| \leq \max\{|(x+\alpha)-y|,|(x+\beta)-y|\} \leq s\), but \(|\alpha-\beta| = |\beta| > s\) since \(|\alpha| < |\beta|\).
```
