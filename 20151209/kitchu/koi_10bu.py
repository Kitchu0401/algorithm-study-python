day = input()
day = day[len(day) - 1]
list = input().split()

count = 0
for n in list :
    if day == n :
        count = count + 1
print( count )