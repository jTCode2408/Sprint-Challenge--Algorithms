#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I
a = 0
    while (a < n * n * n):
      a = a + n * n

a) only performing one operation( a+n*n) constantly, no matter the input size each time.
so Big O would be O(n)



 sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1

b) 2 loops but not the same size arr. inner loop dependent on size, and performs op on some elements
So Big O would be O(n log n)


def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

c) Recursive call but call performs 1 operation each time with call. If should not take extra time because not doing function call or any op if input is 0. 
So Big O is 0(n)

## Exercise II


Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.


-Use Binary search method.
-find midpoinnt of building floors using floor division(//2)
-if egg breaks, will have to go lower until doesnt break.
-go lower, find mid of lower floors drop. If egg breaks, go lower. If doesnt break needs to go higher and do same thing.
-if egg doesnt break, know I can go higher. 
-Go high, find mid, repeat drop process(lower,higher, mid, drop)
-will keep doing process until highest floor is found(without breaking egg)

-Using binary search would be runtime of O(log n)