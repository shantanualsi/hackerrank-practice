#!/bin/python

N, queries = map(int, input().split())
seqList = [[] for _ in range(N)]
lastAns = 0


def first_operation(x, y):
    seq = (x ^ lastAns) % N
    seqList[seq].append(y)


def second_operation(x, y):
    global lastAns
    seq = (x ^ lastAns) % N
    access = y % len(seqList[seq])
    lastAns = seqList[seq][access]
    print(lastAns)


for i in range(queries):
    operation, x, y = map(int, input().split()) 
    if operation == 1:
        first_operation(x, y)
    elif operation == 2:
        second_operation(x, y)
    else:
        print("Invalid Operation")
