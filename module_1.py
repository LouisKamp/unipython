
# %% Exercise 1B
# 9/2+2
# 6+6*4
# 4/6+2
# 2-3*2-4
# (7-5)*(7+5)
# (3*(4-2*(3)+4))
# 2**3
# 3**2 - 4**2
# 2**2**3
# 2**(2**3)

import math
print(3*(2+3**2))
print(4**2+3**3+2**4+1)
print(1/(1/2+1/3+1/6))
# %% Exercise 1C

# print(math.trunc(2.6), math.floor(2.6))
# print(math.ceil(-3.6), math.trunc(-3.2))
# print(round(3.4), math.ceil(3.4))
# print(round(-3.4), math.ceil(-3.4))

math.trunc

print(round(1234.568))
print(round(1234.6))
print(round(1235))
print(round(1200))

# %% Exercise 1D

A = 30
print(math.sqrt(A/math.pi))

a = 51

b = math.log(A)
print(b)

# %% Assignment 1F

WhatISay = "Hello CodeJudge!"

print(WhatISay)

# %% Assignment 1G


A = 0.25*math.pi
b = 12
c = 10

a = math.sqrt(b**2 + c**2 - 2*b*c*math.cos(A))

print(a)

# %% Assignment 1H


a = 2
b = -5
c = 2

x1 = (-b - math.sqrt(b**2-4*a*c))/(2*a)
x2 = (-b + math.sqrt(b**2-4*a*c))/(2*a)

print(x1, x2)


# %%
