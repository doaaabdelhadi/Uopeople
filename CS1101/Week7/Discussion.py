colors=['white','black']
reg_colors=['#fff','#333']


#I want collect two lists every color with the its code.
##zip Function
for code_colors in zip(colors,reg_colors):
    print('zip Function with for loop:: ',code_colors)
code_colors =list(zip(colors,reg_colors))
print('zip Function with list:: ',code_colors)
lst= []    
for color in colors:
    for reg in reg_colors:
        lst.append((color,reg))
print('try to create list of tuple1:: ',lst)
lst_1=[]
for color ,reg in colors ,reg_colors:
    lst_1.append((color,reg))
print('try to create list of tuple2:: ',lst_1)        
        
##enumerate Function
str_0='ABFA'    

for index,value in enumerate(str_0):
    print('Use enumerate Function:: ',(index,value))
    
for value in str_0 :
    index= str_0.find(value)
    print('Use find method:: ',(index,value))
    
#items method
dict_0={"name":['A','B','C'],'age':[15,25,12]}
lst_t= dict_0.items()
print('Ues items method:: ',lst_t)
lst_dict=[]
for key in dict_0:
    lst_dict.append((key,dict_0[key]))
print('Use For LOOP:: ',lst_dict)
