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

#### Lemma 1

<div>If \(r > s > 0\) and \(X\) is a closed ball in \(\mathbb{C}_p\) of radius \(r\), then there are two disjoint balls of radius \(s\) contained in \(X\).<br><br>

<em>Proof.</em><br>

We can write \(X = B_r(x)\) for some \(x \in \mathbb{C}_p\). Choose \(\alpha,\beta \in \mathbb{C}_p\) with \(|\alpha| < s < |\beta| < r\). Then, we claim that \(B_s(x+\alpha)\) and \(B_s(x+\beta)\) are the relevant balls.<br><br>

First, we show these are contained in \(X\). Suppose \(y \in B_s(x+\alpha)\). Then \(|y-x| = |y-(x+\alpha)+\alpha| \leq \max\{|y-(x+\alpha)|,|\alpha|\} < r\), so that \(y \in X\). The same argument works for the other ball. Finally, the two are disjoint. Indeed, if \(y\) were in both balls, then, \(|\alpha-\beta| \leq \max\{|(x+\alpha)-y|,|(x+\beta)-y|\} \leq s\), but \(|\alpha-\beta| = |\beta| > s\) since \(|\alpha| < |\beta|\).&#x25A0;</div>

Note that this is different from the real case, and works because of the nonarchimedan property of the absolute value. That is, in a real vector space, a closed ball of a fixed radius cannot contain two disjoint balls of a smaller radius unless that smaller radius is less than half of the original radius.

#### Lemma 2

<div>\(\mathbb{C}_p\) contains a countable dense subset.<br><br>

<em>Proof.</em><br>

Note that \(\mathbb{Q} \subseteq \mathbb{C}_p\). So, we can consider the algebraic closure of the former in the latter. First, note that this field \(\overline{\mathbb{Q}}\) is countable. Indeed, each element is a root of a polynomial with rational coefficients, but there are only countably many such polynomials per degree, only countably many degrees, and only finitely many roots per polynomial.

To show that it is dense, consider the closure \(Z\), and pick \(\alpha \in \mathbb{Q_p}\), the algebraic closure. Then \(\alpha\) is a root of a monic polynomial \(f \in \mathbb{Q}_p[x]\). By approximating the coefficients, we can write a sequence of polynomials \(f_n \in \QQ[x]\) approaching \(f\). But then since the roots of a polynomial are continuous functions of the coefficients, some sequence of roots \(\alpha_n\) of \(f_n\) approaches \(\alpha\). But \(\alpha_n \in \overline{\mathbb{Q}} \subseteq Z\) by construction, and \(Z\) is closed, so \(\alpha \in Z\). So, \(Z \supseteq \overline{\mathbb{Q}_p}\), and since it is closed, it contains the closure, which is all of \(\mathbb{C}_p\).&#x25A0;</div>

#### The proof