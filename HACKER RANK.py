/*
1   5
 2 4
  3
  /*
  # CREATING A PATTERN GIVEN ABOVE #
  
 n=int(input())
 for i in range(1, n//2 + 2):
  for j in range(1, n + 1):
   if j==i or j==n - i + 1:
    print(j, end="")
      else:
            print(" ",end="")
    print() 
      

           
       
   
