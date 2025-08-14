def longest_common_substring(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    max_len = 0
    end_index_s1 = 0  # track where the substring ends in s1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:  #just checking s1 == s2 (using -1 to get first element(0,0))
                dp[i][j] = dp[i - 1][j - 1] + 1  #adding from top-left 

                if dp[i][j] > max_len:    #if dp[i][j] changed from 2 to 3, it gets updated
                    max_len = dp[i][j]
                    end_index_s1 = i
            else:
                dp[i][j] = 0

    # Extract substring from s1 using recorded length and end index
    return s1[end_index_s1 - max_len: end_index_s1]   #what haapens is : end_index is 7 - max_length is 3 = 7-3 = 4 so, 4:7 (i.e pot)


# getting input string
s1=input().strip()
s2=input().strip()
print(longest_common_substring(s1,s2)) 
