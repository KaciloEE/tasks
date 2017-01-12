def whoIsNext(names, r):
    if r > len(names):
        return  names[r%len(names)]
    else:
        return names[r-1]


print(whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52))
