import itertools
import operator as op

MIN_VALUE = 0
MAX_VALUE = 10

def operatorDisplay(o):
    if o == op.add: return '+'
    if o == op.sub: return '-'
    if o == op.mul: return '*'
    if o == op.div: return '/'

def getSolutions(nums,solvedOrders={}):
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
                    #print('%s %s' % (numbers,len(solvedOrders)))
                    solvedOrders.setdefault(nums,set())
                    solvedOrders[nums].add((numbers,opSet))
            except ZeroDivisionError:
                continue
    return solvedOrders

def main():
    solvedOrders = {}
    # dict of solutions to optimize and deduplicate
    # keys are tuples of numbers, value is set of operation orders
    count = 0
    uniqueNums = set() # avoid same number set showing in diff orders
    # 0, 0, 4, 6 was first example hit, generated in multiple orders
    for number in xrange(10000):
        numbers = ( (number/1000)%10,(number/100)%10,(number/10)%10,number%10 )
        if tuple(sorted(numbers)) in uniqueNums:
            continue
        uniqueNums.add(tuple(sorted(numbers)))
        #print('%s %s' % (number,numbers))
        getSolutions(numbers,solvedOrders)
    for nums in sorted(solvedOrders.keys()):
        print(str(nums))
        for numbers,opSet in solvedOrders[nums]:
            print('\t(%s%s%s)%s(%s%s%s) == 24' % (numbers[0],operatorDisplay(opSet[0]),numbers[1],operatorDisplay(opSet[2]),numbers[2],operatorDisplay(opSet[1]),numbers[3]))
            count += 1
    print('\nThere are %s solutions' % count)

if __name__ == '__main__':
    main()
