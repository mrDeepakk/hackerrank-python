thickness=int(input())  #for input 
c='H'
# TOP CONE
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
    
# TOP PILLAR

for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
    
#MIDDLE PART
# mid=round((thickness+1)/2)


for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))
    
#LOWER PILLAR

for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
    
#LOWER SIDE CONE

for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))










    
