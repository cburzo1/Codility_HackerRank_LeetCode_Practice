def longest_cons_seq(arr):
    num = 0

    m = max(arr)

    h = [0] * (m + 1)

    for i in range(0, len(arr)):
        h[arr[i]] = 1

    count = 0

    for i in range(0, len(h)):
        if h[i] == 1:
            count += 1
        else:
            count = 0

        if count > num:
            num = count

    return num

print(longest_cons_seq([100, 4, 200, 1, 3, 2]))
print(longest_cons_seq([0,3,7,2,5,8,4,6,0,1]))
print(longest_cons_seq([1, 2, 2, 2, 3, 3]))

'''Main Take Aways: 
- My Solution uses readable explicit hash arrays. In the complete solution, I would spit the array into
buckets of negative and positive numbers. I would then repeat the algorithm above for both and compare at the 
end. The solution here is O(n) but is inefficient when it comes to space. Utilizing this method, however, does
solve the problem with hash arrays which are an important concept.

-
'''