
import timeit

def do_nothing(level1, level2, level3):

    for I in range(level1):
        for J in range(level2):
            for K in range(level3):
                pass

def one_million_pass():

    """
    select * from thousand _1000_1, thousand _1000_2 limit 0 offset 1 000 000;
    """

    do_nothing(1, 1000, 1000)

def ten_million_pass():

    """
    select * from ten _10_1
    join thousand _1000_1
    join thousand _1000_2
    limit 0 offset 100 000 000;
    """

    do_nothing(10, 1000, 1000)

def hundred_million_pass():

    """
    select * from hundred _100_1
    join thousand _1000_1
    join thousand _1000_2
    limit 0 offset 100 000 000;
    """

    do_nothing(100, 1000, 1000)

def half_billion_pass():

    """
    select * from five _5_1
    join hundred _100_1
    join thousand _1000_1
    join thousand _1000_2
    limit 0 offset 500 000 000;
    """

    do_nothing(500, 1000, 1000)

def one_billion_pass():

    """
    select * from thousand _1000_1
    join thousand _1000_2
    join thousand _1000_3
    limit 0 offset 1000 000 000;
    """

    do_nothing(1000, 1000, 1000)

print("One million pass     - ", end="")
t1 = timeit.timeit(one_million_pass, number=1)
print("%0.02f"%(t1))

print("Ten million pass     - ", end="")
t1 = timeit.timeit(ten_million_pass, number=1)
print("%0.02f"%(t1))

print("Hundred million pass - ", end="")
t1 = timeit.timeit(hundred_million_pass, number=1)
print("%0.02f"%(t1))

print("Half billion pass    - ", end="")
t1 = timeit.timeit(half_billion_pass, number=1)
print("%0.02f"%(t1))

print("One billion pass     - ", end="")
t1 = timeit.timeit(one_billion_pass, number=1)
print("%0.02f"%(t1))
