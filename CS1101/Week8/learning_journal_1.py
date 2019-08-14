input_write= open('input.txt','w')
l_1= 'A l\n'
l_2= 'B m\n'
l_3= 'C l\n'

input_write.write(l_1)
input_write.write(l_2)
input_write.write(l_3)
input_write.close()

input_f= open('input.txt','a')
l_4= 'D n\n'
l_5= 'E o\n'
l_6= 'F m\n'
input_f.write(l_4)
input_f.write(l_5)
input_f.write(l_6)

input_f.close()

d= {} 
with open ('input.txt') as f:
    for line in f:
        (key,val) =line.split(' ')        
        d[key]= val.strip()
print('Dict from input_file:: ',d)
def invert_dict(d):
     inverse = dict()
     for key in d:
         val = d[key]
         for items in val:
             if items not in inverse:
               inverse[items] = [key]
             else:
                  inverse[items].append(key)
     return inverse 

print('invert_dict:: ',invert_dict(d))

with open('output.txt', 'w') as f:
    for key, value in invert_dict(d).items():
        f.write('%s:%s\n' % (key, value))


read_f = open("output.txt",'r')
print('Output file:: ')
print(read_f.read())

