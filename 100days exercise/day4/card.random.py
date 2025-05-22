#Random bill genarator
import random
name=input("enter name sep with ','  :") #get user input with ,
list_name=name.split(",")
len_name=len(list_name)
random=random.randint(0,(len_name)-1)
final=list_name[random]
print(f"{final} is going to pay the Bill💲💲💲💲")
