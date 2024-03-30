while True:
    name, age, wei = __import__('sys').stdin.readline().split()
    if name == '#': break

    if int(age) > 17 or int(wei) >= 80:
        print(name, "Senior")
    else:
        print(name, "Junior")