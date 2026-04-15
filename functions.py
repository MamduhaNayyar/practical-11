#fiunction def
def greet (name):
    print("hello", name)

greet("Momo")
#local and global variable
y=20
def prints ():
     print(y)

prints()
def change():
    global y
    y=30

change()
prints()
#immutable and mutable objects
#mutable
a=[1,2,3,4]
b=a
print(a)
print(b)

a.append(5)
print(a)
print(b)
#immutable
x=10
y=x
print(x)
print(y)
x=x+10
print(x)
print(y)
#immutable
text="hello"
text="H"+text[1:]
print(text)
#default argument
def greet(name="Guest"):
    print("Hello", name)

greet("Ali")   # uses provided value
greet()        # uses default value
