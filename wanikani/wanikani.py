import itertools
from math import floor
from operator import indexOf
import numpy as np
def wanikani(kanji, questions):
    q_num = kanji*2
    
    q_left = q_num - questions
    q_answered = q_num - q_left
    


    questions = itertools.product(*[[0,1] for i in range(q_left)])
    questions = [sum(i) for i in questions]

    questions.remove(0)
    if q_left%2 != 0:
        possible = [i+1 for i in range(0,q_left)]
    else:
        possible = [i for i in range(kanji-q_answered,q_left+1)]

    for i in set(questions):
        if i not in possible:
            try:
                while True:
                    questions.remove(i)
            except ValueError:
                pass
    q_weight = [questions.count(i) for i in set(questions)]
    q_weight = [((q_weight[i]/len(set(questions)))*(list(set(questions))[i])) for i in range(0, len(q_weight))]
    q_weight = [i/sum(q_weight) for i in q_weight]

    ret = [q_weight[i]*possible[i] for i in range(0, len(possible))]
    print(list(questions))
    print(possible)
    print(q_weight)
    print(sum(ret))


def main():
    print("wanikani")
    op = open("wk.txt", "r")
    op = [line for line in op]
    op = [i.split(' ') for i in op]
    op = op[1:]
    
    ret = []
    for i in op:        
        i[-1] = i[-1].replace('\n','')
        i = [int(j) for j in i]
    for i in op:
        wanikani(int(i[0]),int(i[1]))
if __name__ == "__main__":
    main()