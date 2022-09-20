def area(x1, y1, x2, y2, x3, y3):
 
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)

def isInside(x1, y1, x2, y2, x3, y3, x, y):
 
    # Calculate area of triangle ABC
    A = area (x1, y1, x2, y2, x3, y3)
 
    # Calculate area of triangle PBC
    A1 = area (x, y, x2, y2, x3, y3)
     
    # Calculate area of triangle PAC
    A2 = area (x1, y1, x, y, x3, y3)
     
    # Calculate area of triangle PAB
    A3 = area (x1, y1, x2, y2, x, y)
     
    # Check if sum of A1, A2 and A3
    # is same as A
    if(A == A1 + A2 + A3):
        return True
    else:
        return False

def outages(triangle, data_centers):
    ret = 0
    ta = [
    [triangle[0],triangle[1]],
    [triangle[0],triangle[1]+triangle[2]],
    [triangle[0]+triangle[2], triangle[1]]
    ]
    for data in data_centers:
        if(isInside(ta[0][0],ta[0][1],ta[1][0],ta[1][1],ta[2][0],ta[2][1],data[0],data[1])):
            ret += 1
    return ret

def main():
    data_centers = []
    triangles = []
    op = open("data_center.txt", "r")
    op = [line for line in op]
    op = [i.split(' ') for i in op]
    op = op[1:]

    for i in op:
        i[-1] = i[-1].replace('\n','')
        
        if len(i) == 2:
            data_centers.append([int(j) for j in i])
        elif len(i) == 3:
            triangles.append([int(j) for j in i])
    ret = []

    for i in triangles:
        ret.append(str(outages(i, data_centers))+'\n')
    
    a = open("ret.txt","a")
    a.writelines(ret)
    a.close()

if __name__ == "__main__":
    main()