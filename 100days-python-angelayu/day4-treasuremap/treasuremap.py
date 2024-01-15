line1 = [" "," "," "]
line2 = [" "," "," "]
line3 = [" "," "," "]
map = [line1,line2,line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? X axis is A-C,Y axis is 1 - 3")
#####
a1=line1[0]
a2=line2[0]
a3=line3[0]
b1=line1[1]
b2=line2[1]
b3=line3[1]
c1=line1[2]
c2=line2[2]
c3=line3[2]
print(map[position])
#####
print(f"{line1}\n{line2}\n{line3}")