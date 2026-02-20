a = 'Good Morning'
b = "Good Mornin"

# Multiline String
c = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua'''

d = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua"""

# Quotes Inside 
x2 = "it's alright"
y2 = 'He is called "Elvis"'
y3 = "He is called 'Elvis'"

# Escape Characters
x = 'it\'s alright'
y = "He is called \"Elvis\""


text = "Hello, World"
print(text[0]) 
print(len(text))
print('W' in text)
print('i' not in text)
# Slicing
print(text[7:12])
print(text[7:])
print(text[0:5])
print(text[:5])
print(text[-6:-2])
# Modify
print(text.upper())
print(text.lower()) 
print(text.capitalize())
txt =  " Hello, World "
print(len(txt))
z = txt.strip()
print(len(z))

r = txt.replace('World', 'Class')
print(r)


# Numbers
x = 5
y = 2.5
z = 5j

print(type(x))
print(type(y))
print(type(z))

name = "Elvis"
print(type(name))

p = '7'
print(type(p))

x2 = float(x)
print(x2)

y2 = int(y)
print(y2)


name = "Alice"
print('my name is', name)

# Concatenation
fname = "James"
lname = 'Peter'
print(fname + " " + lname)
print('My name is ' + fname)

# String Format
product = "Laptop"
price = 250000
quantity = 2

print(f"Product: {product}")
print(f"Total cost: {price * quantity}")
