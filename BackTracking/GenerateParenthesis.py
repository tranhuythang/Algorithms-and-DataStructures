def GenerateParenthesis(n):
    result = []
    currentParthsStr = ["" for i in range(2*n)]
    def genParthsAtPosK(position, open_count, closed_count):
        if position == 2*n-1:
            currentParthsStr[2*n-1] = ")"
            result.append("".join(currentParthsStr))
        else:
            if open_count < n:
                currentParthsStr[position] = "("
                genParthsAtPosK(position+1, open_count+1, closed_count)
            if closed_count < open_count <= n:
                currentParthsStr[position] = ")"
                genParthsAtPosK(position+1, open_count, closed_count+1)
    genParthsAtPosK(0, 0, 0)
    return result

for i in range(5):
    result = GenerateParenthesis(i)
    print(i, '->', len(result), result)
        
        
