import ast

dict_1 = {'f_name':['A','B','C','B','C'],'l_name':['B','M','D'],'age':[10,15,15,12]}

with open('learning.txt', 'w') as f:
    for key, value in dict_1.items():
        f.write('%s:%s\n' % (key, value))


dict_2= {'n_name':['L','M','N','O'],'School':['H','S','P'],'City':['A_B','C_D','L_M','A_B']}

with open('learning.txt', 'a') as f:
    for key, value in dict_2.items():
        f.write('%s:%s\n' % (key, value))


##read_1 = open('learning.txt','r')
##print(read_1.read())

d= {}
lst=[]
with open ('learning.txt') as f:
    for line in f:
##        print(line)
        key =line.split(':')[0]
        val =line.split(':')[1]
        val = val.strip()
        val= ast.literal_eval(val)

        d[key]=val
##print(d)
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

print(invert_dict(d))

with open('output.txt', 'w') as f:
    for key, value in invert_dict(d).items():
        f.write('%s:%s\n' % (key, value))

read_f = open("output.txt",'r')
print(read_f.read())
