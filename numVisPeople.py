def seenPeople(heights):
    n = len(heights)
    stack = []
    res = [0] * n
    for i in range(n - 1, -1, -1):
        count = 0
        while stack:
            count += 1
            if stack[-1] < heights[i]:
                stack.pop()
            else:
                break
        res[i] = count
        stack.append(heights[i])
    return res


heights = [10, 6, 8, 5, 11, 9]
print(seenPeople(heights))
