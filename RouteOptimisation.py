from geopy.distance import great_circle

def vish(middle,mini):
  #print (middle,mini)
  mini_sort=[]
  for yd in middle:
    dist = great_circle(mini, yd).km
    mini_sort.append(dist)
  #print (mini_sort)
  path=middle[mini_sort.index(min(mini_sort))]
  #print (path)
  return path 

with open('test.txt', 'r') as g:
    fcontents = g.readlines()

coordinates = ["13.0113316,77.7038889"]
middlecor = fcontents
sortcoor = []
csvfile = []
f = 0
a=[]
c=0
t = 1

main_path=[]
for i in coordinates:
  for j in middlecor:
    dist = great_circle(i, j).km
    sortcoor.append(dist)
    c = c + 1
    if c==len(middlecor):
      #print (sortcoor)
      main_path.append(middlecor[sortcoor.index(min(sortcoor))])
      next_path=middlecor.pop(sortcoor.index(min(sortcoor)))
      #print (main_path,next_path)
      for s in range(len(middlecor)):
        next_path=vish(middlecor,next_path)
        #print (next_path)
        #print (middlecor)
        main_path.append(next_path)
        #print (main_path)
        middlecor.remove(next_path)
        if len(middlecor)==0:
          break
           

   

#print (main_path)
with open('path.txt', 'w') as g:
    for a in main_path:
        g.write(str(a))