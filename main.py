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
    solutions = []
    for opSet in uniqueOperatorSets:
        for numbers in itertools.permutations(nums):
            numbers = tuple(numbers)
            if (opSet,numbers) in solvedOrders:
                assert 'hit it'
                continue
            try:
                a = opSet[0](numbers[0],numbers[1])
                b = opSet[1](numbers[2],numbers[3])
                if opSet[2](a,b) == 24:
                    #print('%s %s' % (numbers,len(solvedOrders)))
                    solvedOrders.add((opSet,numbers))
                    solutions.append((opSet,numbers))
            except ZeroDivisionError:
                continue
    return solutions

def main():
    count = 0
    for number in xrange(10000):
        numbers = [number/1000,(number/100)%10,(number/10)%10,number%10]
        #print('%s %s' % (number,numbers))
        solutions = getSolutions(numbers)
        for opSet,nums in solutions:
            print('(%s%s%s)%s(%s%s%s) == 24' % (nums[0],operatorDisplay(opSet[0]),nums[1],operatorDisplay(opSet[2]),nums[2],operatorDisplay(opSet[1]),nums[3]))
        if len(solutions) > 0:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
