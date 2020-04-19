s = "string"
print(f"i is {s}")

i = 28
print(f"i is {i}")

f = 2.8
print(f"f is {f}")

b = False
print(f"b is {b}")

n = None
print(f"n is {n}")

#x = input()

x = -45

if int(x) > 0:
    print("x is positive")
elif int(x) < 0:
    print("x is negative")
else:
    print("x is zero")

name = "Alice"
coordinates = (10.0, 20.0)
names = ["Alice", "Bob", "Charlie"]

print(name)
print(coordinates[1])
print(names[0])

for i in range(5):
    print(i)

for name in names:
    print(name)

atypes = ["Alice", 10, False, (10.0, 20.0)]

for atype in atypes:
    print(atype)

#sets
s = set()
s.add(1)
s.add("name")
s.add(2)
s.add(2)
s.add((10,0,20,0,30,0))
print(s)

#dictionary
ages = {"Alice": 22, "Bob": 27}
ages["Charlie"] = 30
print(ages)
ages["Alice"] +=1
print(ages)
ages["Hybrid"] = (10.0,20.0)
print(ages)
ages["Objecthybrid"] = {"ob1": 22, "ob2": 27}
print(ages)
print(ages["Objecthybrid"]["ob1"])