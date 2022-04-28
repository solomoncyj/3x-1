a = 0
n = 0

while True:
    a = a + 1
    n = a
    l = 0
    while n != 1:
        if (n % 2) == 0:
            n = n / 2
            l = l + 1
        else:
            n = (n * 3) + 1
            l = l + 1
    end = "number " + (str(a)) + " length of nuber runs " + (str(l))
    print(end)
    with open("out.txt", "a") as o:
        o.write(end)
        o.write("\n")
