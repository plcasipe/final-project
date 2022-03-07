import re

euph_list = []
x = open("euphoria.txt", "r").read().lower()
euphoria = re.split("\n", x)
for item in euphoria:
    if re.search("\d.*", item) or re.search('^00:', item):
        continue
    else:
        euph_list.append(item)

#for y in euph_list:
    #print(y)

um_list = []
uh_list = []
for word in euph_list:
    if re.search(".*um,.*", word):
        #print(word)
        um_list.append(word)
    if re.search(".*uh.*", word):
        uh_list.append(word)

#for i in um_list:
    #print(i)
#print()
#for e in uh_list:
    #print(e)



o = open("santabarb.txt", "r").read().lower()
santa = re.split("\n", o)
um2_list = []
uh2_list = []
for word in santa:
    if re.search(".*u(=*)m.*", word):
        #print(word)
        um2_list.append(word)
    if re.search(".*u(=*)h.*", word):
        uh2_list.append(word)

#for i in um2_list:
    #print(i)
print()
for e in uh2_list:
    print(e)
