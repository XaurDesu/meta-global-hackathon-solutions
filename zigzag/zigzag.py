def zigs(lines, nums):
    for i in lines:
        if i in nums:
            nums.remove(i)
    return nums

def squares(minimat, nums):
    for i in range(len(minimat)):
        for j in range(len(minimat[0])):
            if minimat[i][j] in nums:
                nums.remove(minimat[i][j])
    return nums

def zigzag(matrix):
    nums = ['0','1','2','3','4','5','6','7','8']
    for i in matrix:
        while ' ' in i:
            i.remove(' ')
    for i in matrix:
        while '\n' in i:
            i.remove('\n')

    zigs_line1 = []
    for i in range(len(matrix)):
        zigs_line1.append(matrix[i][i])
    nums = zigs(zigs_line1, nums)

    minimat = []
    for i in range(0,3):
        a = []
        for j in range(0,3):
            a.append(matrix[i][j])
        minimat.append(a)

    nums = squares(minimat, nums)

    zags_line = []
    i = 1
    j = len(matrix)-1
    while i < len(matrix):
        zags_line.append(matrix[i][j])
        i += 1
        j -= 1
    nums = zigs(zags_line, nums)

    return(int(nums[0]))

def get_lines(n, line_numbers):
    return (x for i, x in enumerate(n) if i in line_numbers)

def main():
    n = open("zigzag_medium.txt", "r")
    i = int(n.readline())
    print(i)

    puzzles = []
    x = 0
    n = n.readlines()
    problems = []

    probs = 0
    x = 0
    while probs < i:
        temp = [x for x in n[x:x+9]]
        t = []
        for j in temp:
            j = [x for x in j]
            t.append(j)
        problems.append(t)

        x += 10
        probs += 1

    ret = []
    for i in problems:
        ret.append(zigzag(i))

    for i in ret:
        print(i)

if __name__ == "__main__":
    main()