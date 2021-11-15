"""
    List all the ways to decompose a positive number as a sum of positive integers
"""
def DecomposeAsSumOfPosInt(n):
    currentSum = [0 for i in range(n)]
    result = []
    def assign(i):
        temp_sum = sum(currentSum[:i:])
        if temp_sum >= n:
            result.append(currentSum[:i:])
        else:
            for k in range(1, n-temp_sum+1):
                currentSum[i] = k
                assign(i+1)
    assign(0)
    return result

def main():
    for n in range(1, 10):
        print(n,'->', DecomposeAsSumOfPosInt(n))
if __name__ == "__main__":
    main()



