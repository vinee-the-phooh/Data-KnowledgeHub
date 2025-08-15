#Python can change variable data type from one type to another.
# This is called type conversion.
# There are two types of type conversion:
# 1. Implicit Type Conversion: Python automatically converts one data type to another.
# 2. Explicit Type Conversion: The user converts the data type using the type() function.


# Implicit Type Conversion
a = 5
b = 2.5
c = a + b  # a is int, b is float, c will be float

print("Implicit Type Conversion:")
print("a:", a, "type:", type(a))
print("b:", b, "type:", type(b))
print("c:", c, "type:", type(c))

# Explicit Type Conversion
x = 5
y = 2.5
z = int(y)  # converting float to int
print("\nExplicit Type Conversion:")
print("x:", x, "type:", type(x))
print("y:", y, "type:", type(y))
print("z:", z, "type:", type(z))


# Converting int to float
a = 10
b = float(a)  # converting int to float
print("\nConverting int to float:")
print("a:", a, "type:", type(a))
print("b:", b, "type:", type(b))


# Converting float to string
c = 3.14
d = str(c)  # converting float to string
print("\nConverting float to string:")
print("c:", c, "type:", type(c))
print("d:", d, "type:", type(d))


# Converting string to int
e = "123"
f = int(e)  # converting string to int
print("\nConverting string to int:")
print("e:", e, "type:", type(e))
print("f:", f, "type:", type(f))

# Converting string to float
g = "456.78"
h = float(g)  # converting string to float
print("\nConverting string to float:")
print("g:", g, "type:", type(g))
print("h:", h, "type:", type(h))

# Converting boolean to int
i = True
j = int(i)  # converting boolean to int
print("\nConverting boolean to int:")
print("i:", i, "type:", type(i))
print("j:", j, "type:", type(j))

# Converting int to boolean
k = 0
l = bool(k)  # converting int to boolean
print("\nConverting int to boolean:")
print("k:", k, "type:", type(k))
print("l:", l, "type:", type(l))

# Converting list to tuple
m = [1, 2, 3]
n = tuple(m)  # converting list to tuple
print("\nConverting list to tuple:")
print(f"List : {m}")
print("m:", m, "type:", type(m))
print("n:", n, "type:", type(n))
print(f"Tuple : {n}")

# Converting tuple to list
o = (4, 5, 6)
p = list(o)  # converting tuple to list
print("\nConverting tuple to list:")
print(f"Tuple : {o}")
print("o:", o, "type:", type(o))
print("p:", p, "type:", type(p))
print(f"List : {p}")

# Converting set to list
q = {7, 8, 9}
r = list(q)  # converting set to list
print("\nConverting set to list:")
print(f"Set : {q}")
print("q:", q, "type:", type(q))
print("r:", r, "type:", type(r))
print(f"List : {r}")

# Converting list to set
s = [10, 11, 12]
t = set(s)  # converting list to set
print("\nConverting list to set:")
print(f"List : {s}")
print("s:", s, "type:", type(s))
print("t:", t, "type:", type(t))
print(f"Set : {t}")

# Converting dictionary keys to list
u = {'a': 1, 'b': 2, 'c': 3}
v = list(u.keys())  # converting dictionary keys to list
print("\nConverting dictionary keys to list:")
print(f"dictionary keys : {u.keys()}")
print("u:", u, "type:", type(u))
print("v:", v, "type:", type(v))
print(f"Key List: {v}")

# Converting dictionary values to list
w = list(u.values())  # converting dictionary values to list
print("\nConverting dictionary values to list:")
print(f"dictionary values: {u.values()}")
print("w:", w, "type:", type(w))
print(f"dictionary values Lis: {w}")

# Converting dictionary items to list
x = list(u.items())  # converting dictionary items to list
print("\nConverting dictionary items to list:")
print(f"dictionary Items: {u.items()}")
print("x:", x, "type:", type(x))
print(f"dictionary Items List: {x}")

# Converting list to string
y = ['Hello', 'World']
z = ' '.join(y)  # converting list to string
print("\nConverting list to string:")
print("y:", y, "type:", type(y))
print("z:", z, "type:", type(z))

# Converting string to list
a = "Python is fun"
b = a.split()  # converting string to list
print("\nConverting string to list:")
print("a:", a, "type:", type(a))
print("b:", b, "type:", type(b))

