string=input("enterstring:")
charecterCount=0
wordcount=1
for i in string:
    charecterCount=charecterCount+1
    if (i==''):
        wordcount=wordcount+1
print("number of word in the string")
print(wordcount)
print("number of charecters in the string")
print(charecterCount)