

def main():
    gr = open("comersmol.txt", "r")
    gr = gr.readlines()
    gr = [i for i in gr]
    gr = [i.split(' ') for i in gr]
    
    grph = []
    for i in gr:        
        i[-1] = i[-1].replace('\n','')
        i = [int(j) for j in i]
        grph.append(i)
    grph.sort()
    graph = {}
    for i in grph:
        if i[0] not in graph.keys():
            graph[i[0]] = [i[1:]]
    print(graph)

if __name__ == "__main__":
    main()