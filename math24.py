'''
Code to find Math24 solutions to a supplied number set and
also to generate sets and solutions
'''

import itertools
import operator as op
import sys


def getSolutionsSingleSet(nums,solvedOrders={}):
    operators = set([op.add,op.sub,op.mul,op.div])
    uniqueOperatorSets = list(itertools.permutations(operators,3))
    for opSet in uniqueOperatorSets:
        for numbers in itertools.permutations(nums):
            numbers = tuple(numbers)
            if nums in solvedOrders and (numbers,opSet) in solvedOrders[nums]:
                continue
            try:
                a = opSet[0](numbers[0],numbers[1])
                b = opSet[1](numbers[2],numbers[3])
                if opSet[2](a,b) == 24:
                    solvedOrders.setdefault(nums,set())
                    solvedOrders[nums].add((numbers,opSet))
            except ZeroDivisionError:
                continue
    return solvedOrders

def getSolutionsMultiSets(minVal,maxVal):
    # dict of solutions to optimize and deduplicate
    # keys are tuples of numbers, value is set of operation orders
    solvedOrders = {}
    # avoid same number set showing in diff orders
    # 0, 0, 4, 6 was first example hit, generated in multiple orders
    uniqueNums = set()
    numRange = xrange(minVal,maxVal)
    for n1,n2,n3,n4 in itertools.combinations_with_replacement(numRange,4):
        numbers = ( n1,n2,n3,n4 )
        if tuple(sorted(numbers)) in uniqueNums:
            continue
        uniqueNums.add(tuple(sorted(numbers)))
        getSolutionsSingleSet(numbers,solvedOrders)
    return solvedOrders

def operatorDisplay(o):
    if o == op.add: return '+'
    if o == op.sub: return '-'
    if o == op.mul: return '*'
    if o == op.div: return '/'

def printSolutions(solutions):
    if len(solutions) == 0:
        print('No solution')
    for nums in sorted(solutions.keys()):
        print(str(nums))
        for numbers,opSet in solutions[nums]:
            print('\t(%s%s%s)%s(%s%s%s) == 24' % (
                numbers[0],
                operatorDisplay(opSet[0]),
                numbers[1],
                operatorDisplay(opSet[2]),
                numbers[2],
                operatorDisplay(opSet[1]),
                numbers[3]
            ))

def main():
    '''
    usage:
       python math24.py
          will print all solutions for values minVal=0 to maxVal=10
       python math24.py minVal maxVal
          will print all solutions for values in minVal,maxVal range provided
       python math24.py 5 6 6 7
          will print all solutions for 4 values provided
    '''
    if len(sys.argv) == 5:
        solutions = getSolutionsSingleSet(
            (int(sys.argv[1]),
             int(sys.argv[2]),
             int(sys.argv[3]),
             int(sys.argv[4])
            ))
        printSolutions(solutions)
        return
    
    minVal = 0
    maxVal = 10
    if len(sys.argv) == 3:
        minVal = int(sys.argv[1])
        maxVal = int(sys.argv[2])
    solvedOrders = getSolutionsMultiSets(minVal,maxVal)
    printSolutions(solvedOrders)
    # tally unique solutions
    count = 0
    for nums in sorted(solvedOrders.keys()):
        count += len(solvedOrders[nums])
    print('\nThere are %s solutions' % count)

if __name__ == '__main__':
    main()
