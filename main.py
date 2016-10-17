import itertools
import operator as op

MIN_VALUE = 0
MAX_VALUE = 10

def operatorDisplay(o):
    if o == op.add: return '+'
    if o == op.sub: return '-'
    if o == op.mul: return '*'
    if o == op.div: return '/'

solvedOrders = set() # set of tuples of numbers, to optimize and deduplicate

def getSolutions(nums):
    global solvedOrders
    operators = set([op.add,op.sub,op.mul,op.div])
    uniqueOperatorSets = list(itertools.permutations(operators,3))
    for opSet in uniqueOperatorSets:
        for numbers in itertools.permutations(nums):
            numbers = tuple(numbers)
            if (numbers,opSet) in solvedOrders:
                continue
            try:
                a = opSet[0](numbers[0],numbers[1])
                b = opSet[1](numbers[2],numbers[3])
                if opSet[2](a,b) == 24:
                    #print('%s %s' % (numbers,len(solvedOrders)))
                    solvedOrders.add((numbers,opSet))
            except ZeroDivisionError:
                continue
    return solvedOrders

def main():
    global solvedOrders
    for number in xrange(10000):
        numbers = [(number/1000)%10,(number/100)%10,(number/10)%10,number%10]
        #print('%s %s' % (number,numbers))
        getSolutions(numbers)
    for nums,opSet in solvedOrders:
        print('(%s%s%s)%s(%s%s%s) == 24' % (nums[0],operatorDisplay(opSet[0]),nums[1],operatorDisplay(opSet[2]),nums[2],operatorDisplay(opSet[1]),nums[3]))
    print(len(solvedOrders))

if __name__ == '__main__':
    main()
