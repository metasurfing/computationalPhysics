import numInt

def f(x):
    return x**4 - 2*x + 1

N = 3
a = 0.0
b = 2.0

s = numInt.gaussQuadInt1D(f,a,b,N)

xk, wk = numInt.gaussxwab(a,b,N)

s1 = numInt.gaussQuadInt1D(f,a,b,N,xk,wk)

print(s)
print(s1)
