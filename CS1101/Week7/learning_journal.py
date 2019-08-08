dict_1 = {'id':[1,2,3],'color':['White','Black','Orange'],'reg':['#fff','#333','#fd8300']}
dict_2 = {'f_name':['A','B','C','B','C'],'l_name':['B','M','D']}
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

print(invert_dict(dict_1))
print(invert_dict(dict_2))
