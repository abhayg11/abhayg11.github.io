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

First, we show these are contained in \(X\). Suppose \(y \in B_s(x+\alpha)\). Then \(|y-x| = |y-(x+\alpha)+\alpha| \leq \max\{|y-(x+\alpha)|,|\alpha|\} < r\), so that \(y \in X\). The same argument works for the other ball. Finally, the two are disjoint. Indeed, if \(y\) were in both balls, then, \(|\alpha-\beta| \leq \max\{|(x+\alpha)-y|,|(x+\beta)-y|\} \leq s\), but \(|\alpha-\beta| = |\beta| > s\) since \(|\alpha| < |\beta|\). &#x25A0;</div>

Note that this is different from the real case, and works because of the nonarchimedan property of the absolute value. That is, in a real vector space, a closed ball of a fixed radius cannot contain two disjoint balls of a smaller radius unless that smaller radius is less than half of the original radius.

#### Lemma 2

<div>\(\mathbb{C}_p\) contains a countable dense subset.<br><br>

<em>Proof.</em><br>

Note that \(\mathbb{Q} \subseteq \mathbb{C}_p\). So, we can consider the algebraic closure of the former in the latter. First, note that this field \(\overline{\mathbb{Q}}\) is countable. Indeed, each element is a root of a polynomial with rational coefficients, but there are only countably many such polynomials per degree, only countably many degrees, and only finitely many roots per polynomial.<br><br>

To show that it is dense, consider the closure \(Z\), and pick \(\alpha \in \overline{\mathbb{Q_p}}\), the algebraic closure. Then \(\alpha\) is a root of a monic polynomial \(f \in \mathbb{Q}_p[x]\). By approximating the coefficients, we can write a sequence of polynomials \(f_n \in \mathbb{Q}[x]\) approaching \(f\). But then since the roots of a polynomial are continuous functions of the coefficients, some sequence of roots \(\alpha_n\) of \(f_n\) approaches \(\alpha\). But \(\alpha_n \in \overline{\mathbb{Q}} \subseteq Z\) by construction, and \(Z\) is closed, so \(\alpha \in Z\). So, \(Z \supseteq \overline{\mathbb{Q}_p}\), and since it is closed, it contains the closure, which is all of \(\mathbb{C}_p\). &#x25A0;</div>

#### The proof

Now, we can proceed to the proof of the theorem, that \\(\mathbb{C}_p\\) is spherically incomplete.

<div><em>Proof.</em><br>

For contradiction, assume that \(\mathbb{C}_p\) is spherically closed. Fix a sequence of real numbers \(r_0 > r_1 > r_2 > r_3 > \cdots\) converging to 1, and let \(S\) denote the set of infinite strings on the alphabet \(\{0,1\}\). We will inductively construct a closed ball corresponding to each finite string as follows: start with \(U_{\emptyset} = B_{r_0}(0)\) to be the closed ball associated with the empty string (of length 0). Then, having defined a closed ball \(U_w\) for a finite string \(w\) of length \(L\), construct \(U_{w0},U_{w1}\) using Lemma 1 as two disjoint balls of radius \(r_{L+1}\) contained in \(U_w\).<br><br>

Use Lemma 2 to fix a countable dense subset \(T \subseteq \mathbb{C}_p\). For an infinite word \(s \in S\), letting \(s_n\) denote the length \(n\) prefix, we can define

$$U_s = \bigcap_{n=1}^\infty U_{s_n}$$

By our assumption, \(U_s\) is not empty, and so contains some \(z_s\). But then \(U_s\) contains \(B_1(z_s)\) as well by our choice of radii above, and since \(T\) is dense, \(T \cap B_1(z_s) \neq \emptyset\). So, WLOG, we may choose each \(z_s \in T\). This defines a function \((f(s) = z_s) : S \to T\).<br><br>

But by construction, this function is injective. Indeed, if \(s \neq s'\), then these words differ for some first finite index, i.e. \(s_n \neq s_n'\), but \(s_{n-1} = s_{n-1}'\). But then \(U_{s_n}\) and \(U_{s_n'}\) were constructed as disjoint subsets of \(U_{s_{n-1}}\). Thus \(U_s\) and \(U_{s'}\) are also disjoint, as subsets of these disjoint sets, respectively. Thus we have an injection from an uncountable set to a countable set, which furnishes our contradiction. &#x25A0;</div>

## Constructive proof

Finally, we will do this explicitly, i.e. I will write a nested sequence of closed balls with empty intersection. First, let me remind you of [&#x21B7;Krasner's Lemma](https://en.wikipedia.org/wiki/Krasner%27s_lemma). Then, let me prove two more lemmas:

#### Lemma 3

<div>If
$$z_n = \sum_{k=1 \atop \gcd(p,k)=1}^{n-1} p^{-1/k}$$
and \(x_n\) is a Galois conjugate not equal to \(z_n\) itself, then \(|z_n-x_n| > p^{1/n}\).<br><br>

<em>Proof.</em><br>

First, note that inherent in this expression is a collection of choices of roots of \(p\). Then, note that

$$1+x+\cdots+x^{k-1} = \frac{x^k-1}{x-1} = \prod_{i=1}^{k-1} (x-\mu_k^i)$$

where \(\mu_k\) is a primitive \(k\)th root of unity. Evaluating at \(x=1\) gives a product of integral elements equal to \(k\). When \(\gcd(p,k)=1\), we conclude that the absolute value of each term in the product must be 1. In other words, if \(\alpha \neq 1\) is a \(k\)th root of unity, then \(|1-\alpha|=1\).<br>br>

Now, suppose \(x_n,z_n\) are as in the statement. Then the difference \(z_n-x_n\) is a sum of terms of the form \(p^{-1/k}-u\), where \(u\) is a Galois conjugate of \(p^{-1/k}\). In particular, \(u^k = 1/p\) as well, so \((p^{1/k}u)^k=1\) and \(p^{1/k}u\) is a \(k\)th root of unity. So, either \(u = p^{-1/k}\) or

$$|p^{-1/k}-u| = |p^{-1/k}||1-p^{1/k}u| = p^{1/k} \cdot 1 = p^{1/k}$$

Since \(x_n \neq z_n\), at least one of these terms is nonzero, and by the nonarchimedan property, the absolute value of the sum is the minimum of these (using that the nonzero terms have distinct absolute value). I.e. for some \(k\), we get: \(|z_n-x_n| = p^{1/k} > p^{1/n}\) as claimed. &#x25A0;</div>

#### Lemma 4

<div>For \(z_n\) as in the previous lemma, the extension \(\mathbb{Q}_p(z_1,z_2,z_3,\ldots)/\mathbb{Q}_p\) has infinite degree.<br><br>

<em>Proof.</em><br>

Note that if \(k\) is not divisible by \(p\), we have \(z_{k+1}-z_k = p^{-1/k}\), and \(|p^{-1/k}| = p^{1/k}\). But if this extension were finite, it would have value group isomorphic to \(\mathbb{Z}\). But we've found elements with absolute values arbitrarily close (but not equal) to 1, so the value group cannot be discrete. &#x25A0;</div>

#### The proof

Again, we show that \\(\mathbb{C}_p\\) is spherically incomplete.

<div><em>Proof.</em><br>

For each \(n\), let \(z_n\) be as in Lemma 3, and \(r_n = p^{1/n}\). Then, we have the closed balls \(B_{r_n}(z_n)\). First, we will show that these are nested, and second, we will show they have empty intersection.<br><br>

To begin, first note that \(r_n\) is a decreasing sequence of real numbers with limit 1. Further, if \(n\) is a multiple of \(p\), then \(z_n = z_{n+1}\). Otherwise,

$$|z_{n+1}-z_n| = |p^{-1/n}| = p^{1/n} = r_n$$

So, in either case, \(|z_{n+1}-z_n| \leq r_n\). Now, suppose that \(y \in B_{r_{n+1}}(z_{n+1})\). Then,

$$|y-z_n| \leq \max\{|y-z_{n+1}|,|z_n-z_{n+1}|\} \leq \max\{r_{n+1},r_n\} = r_n$$

as desired.<br><br>

For contradiction, assume now that \(z \in \bigcap_n B_{r_n}(z_n)\). As in the nonconstructive proof, we then get that \(B_z(1)\) is contained in this intersection, and this ball contains an element of \(\overline{\mathbb{Q}_p}\) by density. So, we can assume \(z\) is algebraic over \(\mathbb{Q}_p\). Then, for each \(n\), we have

$$|z_n-z| \leq r_n < |z_n-x_n|$$

for any Galois conjugate \(x_n \neq z_n\), invoking Lemma 3. By Krasner's lemma (which applies since \(\mathbb{Q}_p\) is nonarchimedean and complete), this implies that \(z_n \in \mathbb{Q}_p(z)\) for each \(n\). But this is a contradiction because the \(z_n\) generate an infinite extension (Lemma 4) of \(\mathbb{Q}_p\) while \(\mathbb{Q}_p(z)\) is a finite extension since \(z\) is algebraic. &#x25A0;</div>
