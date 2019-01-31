Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.

##### Note:
This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

For example, given the array  there are  elements, two positive, two negative and one zero. Their ratios would be ,  and . It should be printed as
```
0.400000
0.400000
0.200000
```

##### Function Description

Complete the plusMinus function in the editor below. It should print out the ratio of positive, negative and zero items in the array, each on a separate line rounded to six decimals.

plusMinus has the following parameter(s):

- arr: an array of integers

##### Input Format

The first line contains an integer, n, denoting the size of the array. 
The second line contains  space-separated integers describing an array of numbers .

##### Constraints



##### Output Format

You must print the following 3 lines:

1. A decimal representing of the fraction of positive numbers in the array compared to its size.
2. A decimal representing of the fraction of negative numbers in the array compared to its size.
3. A decimal representing of the fraction of zeros in the array compared to its size.

##### Sample Input
```
6
-4 3 -9 0 4 1     
```

##### Sample Output
```
0.500000
0.333333
0.166667
````

##### Explanation

There are 3 positive numbers, 2 negative numbers, and 1 zero in the array.
The proportions of occurrence are positive: , negative:  and zeros: .
