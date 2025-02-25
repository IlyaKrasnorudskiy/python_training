def reverseList(head):
    ind = -1
    nechet = (len(head)//2) + 1
    for i in range(0, len(head)):
        if i == nechet:
            break
        head[i], head[ind] = head[ind], head[i]
        ind = ind - 1
    return head
print(reverseList([1,2,3,4,5]))