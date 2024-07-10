user_input = input("Enter words: ")
emtystr = ""
emtylist= []

for i in user_input:
    if i != " ":
        emtystr += i
    else:
        if emtystr:  
            emtylist.append(emtystr)
            emtystr = ""
if emtystr:
    emtylist.append(emtystr)

print(emtylist)
