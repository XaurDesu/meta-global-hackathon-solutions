def main():
    pr1 = open("pr1.txt", "r")
    pr1 = [int(x) for x in pr1.readlines()]

    pr2 = open("pr2.txt", "r")
    pr2 = [int(x) for x in pr2.readlines()]

    print(sum(pr1) - sum(pr2))

if __name__ == "__main__":
    main()