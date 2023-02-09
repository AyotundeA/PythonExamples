# Simple Strings
course = 'Hello there!'
# Cloning Strings
another = course[:]
print(course[:5])
print(another)
# Format Strings
first = 'Joe'
last = 'White'
message = first + ' [' + last + '] is a code'
msg = f' {first} [{last}] is a coder'
print(msg)

# String Methods
method = 'Python Examples'
print(course.upper())
print(course.lower())
print(course.find('P'))
print(course.replace('Examples', 'Great Examples'))
