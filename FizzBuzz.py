print ("Введите число диапозона: ")
n = int(input())
solo = []
learn = []
sl = []
nums = []

for x in range(1,n):
    if x%2 == 0:
        continue
    elif x%3 == 0 and x%5 == 0:
        sl.append(str(x) + " SoloLearn")
    elif x%3 == 0:
        solo.append(str(x) + " Solo")
    elif x%5 == 0:
        learn.append(str(x) + " Learn")
    else:
        nums.append("nums: " + str(x))

print(solo)
print(learn)
print(sl)
print(nums)