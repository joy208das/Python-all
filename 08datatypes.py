'''Data-types'''
#String

"Hello"[4]
print("hello"[0]) #this will print h
print("hello"[4]) #this will print o

#Integer
print(123+345)

#Float
print(3.14+325)

#Boolean
True
False



'''len(2362) will return error
len() function don't execute integers''' 

# name=len(input("what is your name?"))
# print("Your name has " + name +" characters")
# This wil return error,
'''we can check with type() function what kind of data-type it is
like this is integer or character type 
'''
name=input("1.what is your name?")
print(type(len(name)))

#if we input any name or character this will show <class 'int'>
'''so in this  print("Your name has " + name +" characters")
adding a integer in string ,not make any sense

so we can convert it into string data-type using str() function
'''
name=len(input("2.what is your name?"))
new=str(name)
print("Your name has " + new +" characters")



