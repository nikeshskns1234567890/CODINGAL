a=90

if a > 70:
    print("amazing")
else:
    print("on snap!")


if a > 8:
    if a > 12:
        if a > 16:
            print(a)
else:
    print("nothing happened")


if a < 20:
    print("printing something")
elif a < 4:
    print("printing something")
elif a < 2:
    print("printing something")
else:
    print("shit yaar")

import datetime

k = datetime.datetime(2025, 3, 1)

print(datetime.datetime.now())     # current date & time
print(k.astimezone())              # convert 'k' to local timezone
