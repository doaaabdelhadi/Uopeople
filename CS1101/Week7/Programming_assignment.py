alphabet = "abcdefghijklmnopqrstuvwxyz"   

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"] 

def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d 

## Part1
def has_duplicates(s):
     h=histogram(s)
     for key in h:
          if h[key] >=2:
               return('has duplicates')               
     return('has no duplicates')                    
for item in test_dups:
    print(item,has_duplicates(item))
for item in test_miss:
    print(item,has_duplicates(item))

print("---- Part2 -----")    
lst=[]
lst_str=[]
tup_str= tuple()    
s=""               
def missing_letters (s):
     h =histogram(s)
     string=''.join(list(h.keys()))
     for c in alphabet:
          if c not in string:
               
               return(s,alphabet.replace(string,''),'is missing letters')
     else:
          return(alphabet,'all the letters')

for item in test_miss:
     print(missing_letters(item))


     
     
