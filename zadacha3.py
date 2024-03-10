def nearby(data, places=1):
    return list(filter(lambda x: '0' * places in x, data))


data = ["100100011",
        "0001100001",
        "100001001",
        "1110010111"]

print(*nearby(data, places=4), sep='\n')
