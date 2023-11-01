result = []

start = int(input("Enter the starting range (four-digit number): "))
end = int(input("Enter the ending range (four-digit number): "))

if start < 1000 or end > 9999 or start > end:
    print("Invalid range. Please enter a valid four-digit range.")
else:
    for num in range(start, end + 1):
    
        if all(int(digit) % 2 == 0 for digit in str(num)):
        
            root = int(num ** 0.5)  #taking the sqaure root
            if root * root == num:  #checking if it is a perf_square 
                result.append(num)  #adding it to the list


print("Four-digit even perfect square numbers in the given range:")
print(result)
