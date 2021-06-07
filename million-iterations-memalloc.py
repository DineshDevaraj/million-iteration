
import timeit

def alloc_and_print(level1, level2, level3):

    l1 = [0] * level1
    printBuffer = "\n+-----+-----+-----+\n"
    
    for I in range(level1):
    
        l1[I] = [0] * level2
        
        for J in range(level2):
        
            l1[I][J] = [0] * level3
            
            for K in range(level3):
            
                printBuffer += f"| {I:3} | {J:3} | {K:3} |\n"
                
            print(printBuffer, end="")
            printBuffer = ""

    print("+-----+-----+-----+")

def one_million_pass():

    """
    select * from thousand _1000_1, thousand _1000_2;
    """

    alloc_and_print(1, 1000, 1000)

def ten_million_pass():

    """
    select * from ten _10_1
    join thousand _1000_1
    join thousand _1000_2;
    """

    alloc_and_print(10, 1000, 1000)

def hundred_million_pass():

    """
    select * from hundred _100_1
    join thousand _1000_1
    join thousand _1000_2;
    """

    alloc_and_print(100, 1000, 1000)

def half_billion_pass():

    """
    select * from five _5_1
    join hundred _100_1
    join thousand _1000_1
    join thousand _1000_2;
    """

    alloc_and_print(500, 1000, 1000)

def one_billion_pass():

    """
    select * from thousand _1000_1
    join thousand _1000_2
    join thousand _1000_3;
    """

    alloc_and_print(1000, 1000, 1000)

fh = open("timetaken.txt", "w")

fh.write("One million pass     - ")
t0 = timeit.timeit(one_million_pass, number=1)
fh.write("%0.02f\n"%(t0))
fh.flush()

fh.write("Ten million pass     - ")
t0 = timeit.timeit(ten_million_pass, number=1)
fh.write("%0.02f\n"%(t0))
fh.flush()

fh.write("Hundred million pass - ")
t0 = timeit.timeit(hundred_million_pass, number=1)
fh.write("%0.02f\n"%(t0))
fh.flush()

fh.write("Half billion pass    - ")
t0 = timeit.timeit(half_billion_pass, number=1)
fh.write("%0.02f\n"%(t0))
fh.flush()

fh.write("One billion pass     - ")
t0 = timeit.timeit(one_billion_pass, number=1)
fh.write("%0.02f"%(t0))
fh.flush()

fh.close()
