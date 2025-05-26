#num=int(input("enter the number of line to print : "))
num=10
word='*'
word1=''
for i in range(0, num):
    word1 += word
    print(word1)
for i in range(num-1, 0, -1):
     print('*' * i)
