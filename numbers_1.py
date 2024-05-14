for i in range(1, 10):
    if i == 7:
        break
    print("Outer loop:", i)
    for j in range(1, 4):
        if j == 3:
            continue
        print("Inner loop:", j)
