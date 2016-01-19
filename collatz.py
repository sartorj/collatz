import sys,random,time
import matplotlib.pyplot as plot
nums = []

def main():    
    start = time.time()
    mode = 'default'

    if sys.argv[1] == 'help':
        print( "Usage: python collatz.py <integer value or 'r' for random>")
        sys.exit()
    elif sys.argv[1] == 'r' or sys.argv[1] == 'R':
        mode = 'random'
        randomCollatz()
    elif sys.argv[1].isdigit(): 
        #check if string in arv[1] is all numbers
        doCollatz(int(sys.argv[1]))
    else:
        print("Error: invalid input. Try an integer or 'r'.")
        sys.exit()
    elapsed = time.time() - start

    global nums
    print nums
    print("Calculation took " + str(elapsed) + " seconds.\n")    

    plotHistogram()

def randomCollatz():
    doCollatz(random.randint(1,1000))

def doCollatz(number):
    global nums
    if number ==1:
        #done
        nums.append(number)
    elif number%2 == 0:
        #even
        nums.append(number)
        doCollatz(number/2)
    else:
        #odd
        nums.append(number)
        doCollatz((3*number)+1)
    
def plotHistogram():
    global nums
    plot.hist(nums,bins=20)
    plot.show()

if __name__ == '__main__':
    main()
    
