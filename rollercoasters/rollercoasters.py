def rollercoaster(n: list):
    ret = 0
    i = 1
    temp = 0
    while i < len(n):
        if n[i] < n[i-1]:
            temp = 10
        else:
            temp += 10
            if temp > ret:
                ret = temp
        i += 1
    return ret

def main():
    n = open("medium_input.txt", "r")
    n = n.readlines()
    n = [int(i) for i in n]
    

    ret = open("solution.txt", "w")
    ret.write(str(rollercoaster(n)))
    ret.close()

if __name__ == "__main__":
    main()