---
layout: post
title: Spherical completeness of \(\mathbb{C}_p\)
mathjax: true
---

I recently sought a proof that \\(\mathbb{C}_p\\) is not spherically complete. I've since proved this in two separate ways, which I'd like to detail here.

## The problem

Recall that \\(\mathbb{Z}_p\\) is the ring of \\(p\\)-adic integers, the completion of the localization \\(\mathbb{Z}_{(p)}\\) with respect to the (usual) \\(p\\)-adic absolute value; \\(\mathbb{Q}_p\\) is the field of \\(p\\)-adic numbers, the field of fractions of \\(\mathbb{Z}_p\\); \\(\overline{\mathbb{Q}_p}\\) is a (fixed) algebraic closure, equipped with the unique extension of the \\(p\\)-adic absolute value; and \\(\mathbb{C}_p = \widehat{\overline{\mathbb{Q}_p}}\\) is the completion of \\(\overline{\mathbb{Q}_p}\\) with respect to its absolute value, itself equipped with an extension of the absolute value.

It is well-known that \\(\mathbb{C}_p\\) is algebraically closed and complete with respect to the absolute value. On the other hand, we will show that it is not **spherically complete**. That is, there exists a sequence of nested closed spheres (of positive radii) with empty intersection. Contrast this with [&#x21B7;Cantor's intersection theorem](https://en.wikipedia.org/wiki/Cantor%27s_intersection_theorem).

## Nonconstructive proof

