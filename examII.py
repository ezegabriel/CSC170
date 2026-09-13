def filelist(a):
    file = open(a)
    d_share, d_price = {}, {}
    s_line = file.readline()
    while s_line != "":
        s_line = s_line.rstrip()
        l_line = s_line.split(",")
        del l_line[0]
        l_line[2] = l_line[2].lstrip("$")
        if not l_line[0] in d_share:
            d_share[l_line[0]] = float(l_line[1])
            d_price[l_line[0]] = float(l_line[2])
        else:
            d_share[l_line[0]] += float(l_line[1])
            d_price[l_line[0]] += float(l_line[2])
        s_line = file.readline()

    return d_share, d_price


def compute(d_share, d_price):
    
   
    l_store = []
    for key in d_share:
        l_temp = []
        l_temp.append(key)
        l_temp.append(d_share[key])
        l_temp.append(d_price[key])
        l_store.append(l_temp)

    for index in range(100):
        for pos in range(len(l_store) - 1):
            if l_store[pos] > l_store[pos + 1]:
                s_temp = l_store[pos]
                l_store[pos] = l_store[pos + 1]
                l_store[pos + 1] = s_temp

    return l_store

def amend(l_store, b):
    file = open(b, mode = "w")
    for item in l_store:
        file.write(str(item) + "\n")

def main():
    d_share, d_price = filelist("scores.txt")
    l_store = compute(d_share, d_price)
    amend(l_store, "examII.txt")

main()

