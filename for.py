list = [2,3,4,5,6,7]

for x in list:
    if(x%2==1 and x>4):
        print(x)
        break

#for use when, you know numbers of circle
#while when, you dont undestand numbers of iterration. While user input number


for i in range(10):
    if not i%2 == 0:
        print (i+1)