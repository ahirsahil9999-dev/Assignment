# Given the following code, identify whether the variable 'count' is local
# or global in each function, and explain what will be printed when run:

""" 
count = 10
def update_count():
    count = 5
    print('Inside:', count)

update_count()
print('Outside:', count)
"""

"""
output : 
inside : 5
outside : 10

Variable created inside a function it's called as local variable
Variable created outside a function it's called as global variable
"""