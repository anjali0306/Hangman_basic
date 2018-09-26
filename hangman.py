
word=raw_input("Please have any word ")
word1=list(word)
print word1
print len(word1)
for i in range(len(word)):
    x=raw_input("please guess the letters of the word ")
    print x
    if x==word1[i]:
       print(x)
    else:
       print("_")
