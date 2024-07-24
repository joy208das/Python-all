'''how title work 
joy= Joy
diYA=Diya'''

def format(j,d):

    j_name=j.title()
    d_name=d.title()

    return j_name,d_name

print(format("joy","DiYA"))


'''if we return this
f"{j_name} {d_name}"

this will print just Joy Diya
'''