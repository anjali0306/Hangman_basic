
word=["hello"]

y=[]
for i in range (0,5):
    x=raw_input("Please guess the letters of the word ")
    print x
    y.append(x)
    print y
for i in y:
    if i in word[0]:
        print("yes")
    else:
       print("no")
