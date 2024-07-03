position=input()
letter=position[0].lower()
abc=["a","b","c"]

x=abc.index(letter)   #this tell the index number of an element
y=int(position[1])-1
print(x)
print(y)


'''nested  list practice
find the position of an 3d array'''

line1=["+","+","+"]
line2=["+","+","+"]
line3=["+","+","+"]

map=[line1,line2,line3]
p=input()  #input the position(like A1,A3,B1,B2...)
abc=['a','b','c']
letter=p[0].lower()  #1st letter upper case-lower case 
letter_index=abc.index(letter) #find index of input position
number_index=int(p[1])-1

map[number_index][letter_index]='$'  #do dry run

print(f"{line1}\n{line2}\n{line3}")

