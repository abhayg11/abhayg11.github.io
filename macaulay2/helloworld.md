---
layout: page
title: Macaulay2
subtitle: Hello World
---

Constructing rings and finding dimensions:
```
p = 5;
S = ZZ/p[x,y,z];
I = ideal(x^2-y*z);
R = S/I;
print dim R;
print dim S;
```

Creating ring homomorphisms:
```
p = 5;
S = ZZ/p[x,y,z];
A = ZZ/p[a,b];
phi = map(A, S, {a^2, a*b, b^2});  --Specifies the images of x,y,z in A
J = ker phi;
print J;
```

The Frobenius is injective:
```
p = 5;
S = ZZ/p[x,y,z];
I = ideal(x^2-y*z);
R = S/I;
F = map(R, R, {x^p,y^p,z^p});
print ker F;
```

Creating rings/modules as images of homs:
```
p = 5;
A = ZZ/p[a,b];
S = ZZ/p[x,y,z];
I = ideal(x^2-y*z);
R = S/I;

loadPackage "PushForward";
psi = map(A, R, {a*b, a^2, b^2});
print isWellDefined psi;
M = (pushFwd(psi))#0;  --Returns a tuple, first element is the module
print rank M;
print isHomogeneous M;
print pdim M;
```
