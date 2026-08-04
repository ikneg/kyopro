n, x = map(int,input().split())
a = list(map(int, input().split()))

left = 0
right = n - 1
while left <= right:
   index = (left + right) // 2

   if a[index] == x:
      print(index + 1)
      break
   elif a[index] > x:
      right = index - 1
   else:
      left = index + 1
   
   