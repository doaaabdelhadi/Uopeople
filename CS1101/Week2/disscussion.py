#Example1
#define a function ex take an argument
def ex (a):
    print(a)

x = 25
print('call function ex in Example1')
ex(x)


#Example2
# call function ex

# take value
print('Example2')
print('call function ex with value')
ex('Hello World!')

# take varible (float)

y= 24.5
print('call function ex with variale')

ex(y)

# expression
print('call function ex with expression')

ex('Welcome' + 'back')

#Example 3

#def function with local varablie

def local_var(x,y):
    c= x+y
    print(c)

#call function local_var
local_var(x,y)
# call the local variable outside the function return error.
##print(c)


# Example 4

def unique_name(len):
    print(len)

print(len)

## invalid  syntax
def unique_name1(try):
    print(return)

##print(return)

##example5

#global variable 
fullname='Mo salah'
## define the function with local veriable the same name of global veriable.
def same_name(fname, lname):
    fullname = fname+' '+lname
    print(fullname)
#call the function same_name

same_name('Mo','Trika')

#print the global variable.

print(fullname)
