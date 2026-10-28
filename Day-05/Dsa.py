# def permute(arr, start):

#     if start == len(arr):
#         print(arr)
#         return

#     for i in range(start, len(arr)):

#         # MAKE CHOICE
#         arr[start], arr[i] = arr[i], arr[start]
#         print(i,start)

#         # CONTINUE
#         permute(arr, start + 1)
#         print(i,start)
#         # UNDO CHOICE
#         arr[start], arr[i] = arr[i], arr[start]

# arr=[1,3,4]
# permute(arr,0)


lt = [1, 2, 3, 4, 5 ,6]
left=0
right=len(lt)-1
target=10
while left<=right:
    if lt[left]+lt[right]==target:
        print(left,right)
        break
    elif lt[left]+lt[right]<target:
        left=left+1
    elif lt[left]+lt[right]>target:
        right=right-1
else:
    print('not found')


arr = [2, 1, 5, 2, 3, 2]
target = 7
for i in range(len(arr)):
    sum=sum+arr[i]
    