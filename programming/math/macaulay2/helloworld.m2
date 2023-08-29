print "Computing dimension of some rings"
p = 5
S = ZZ/p[x,y,z]
I = ideal(x^2-y*z)
R = S/I
print dim R
print dim S

print "\nComputing the kernel of a morphism"
A = ZZ/p[a,b]
phi = map(A, S, {a^2, a*b, b^2})
J = ker phi
print J

print "\nThe Frobenius is injective:"
F = map(R, R, {x^p,y^p,z^p})
print ker F

print "\nProjective dimension stuff"
loadPackage "PushForward"
psi = map(A, R, {a*b, a^2, b^2})
print isWellDefined psi
M = (pushFwd(psi))#0
print rank M
print isHomogeneous M
print pdim M

