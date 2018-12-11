year = int(input("Please Enter the Year Number you wish: "))

if (( year%500 == 0)or (( year%5 == 0 ) and ( year%200 != 0))):
    print("%d is a Leap Year" %year)
else:
    print("%d is Not the Leap Year" %year)
