i = 1
while ((i+1)**2-i**2) <= 168:
    i += 1
for a in range(i**2):
    if a**0.5 == int(a**0.5) and (a+168)**0.5 == int((a+168)**0.5):
        print(a-100)
