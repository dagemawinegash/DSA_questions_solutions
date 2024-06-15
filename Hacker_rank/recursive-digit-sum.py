import os

def superDigit(n, k):
    def helper(x):
        if len(x) == 1:
            return int(x)
        digit_sum = sum(int(char) for char in x)
        return helper(str(digit_sum))
    
    initial_sum = sum(int(char) for char in n)
    
    total_sum = initial_sum * k
    
    return helper(str(total_sum))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
