## create color string
colors='orange black bule green pink'
print('colors: ',colors)
## split color
lst_colors = colors.split( )
print('split color: ',lst_colors)

#delet elements with three methods
lst_colors.remove('black')
lst_colors.pop(0)
del lst_colors[1] 
print('del_colors: ',lst_colors)

## sort the lst

lst_colors=sorted(lst_colors)
print('sort_color: ',lst_colors)

## add four elements

lst_colors.append('black')
lst_colors=lst_colors+['orange','green']
lst_colors.insert(3,'red')
print('add new colors: ',lst_colors)
### join lst_colors to string

delimiter=' '
colors_1= delimiter.join(lst_colors)
print('join lst_colors: ',colors_1)

##part2
print('...part2...')
##Nested lists
Nest_lst=[['orange','black','red','blue'],['code_11','code_15','code_17','code_20']]
print('Nested list: ',Nest_lst)
###The “*” operator

lst=lst_colors
lst=lst *2
print('The “*” operator: ',lst)

##List slices
print('List slices: ', lst[5:])

##The “+=” operator
lst=lst +Nest_lst
print('The “+=” operator: ',lst)

### A list filter
new_lst=[]
def fliter_lst(lst):
    for items in lst:
        if type(items) is list:
            new_lst.append(items)
    return(new_lst)

print('A list filter: ',fliter_lst(lst))

#A list operation that is legal but does the "wrong" thing, not what the programmer expects 
lst_names =['Mo Trike','Ronaldo','Messi']
lst_names=lst_names.sort()
print(lst_names)

