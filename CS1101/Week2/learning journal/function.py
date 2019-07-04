#define pi as float type
pi = 3.141592653589793
#define function print_volume 
def print_volume(r):
    print(4/3*pi*r**3)

r0 = 5
r1 = 3
r2 = 5.5
#print_volume when r =5
print('print_volume when r =5')
print_volume(r0)
#print_volume when r =3
print('print_volume when r =3')
print_volume(r1)
#print_volume when r =5.5
print('print_volume when r =5.5')
print_volume(r2)

##print_volume('r') ## return error.


# function full name will take the first and last name as paramters

def full_name(fname,lname):
    print(fname + ' ' + lname)
#full_name with str letter
print('full_name with str letter')
full_name('Mo','Trike')
#full_name with str number
print('full_name with str number')
#full_name with int and float
full_name('22.22','22')

print('full_name with int and float')

full_name(22.22,22)

