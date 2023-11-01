# Lambda function to calculate the area of a square
calculate_square_area = lambda side_length: side_length ** 2

# Lambda function to calculate the area of a rectangle
calculate_rectangle_area = lambda length, width: length * width

# Lambda function to calculate the area of a triangle
calculate_triangle_area = lambda base, height: 0.5 * base * height

sqs = int(input("Enter the side of the square"))
          
print("Enter the base and height of the triangle")
ht = int(input())
bs = int(input())

print("Enter the length and breadth of the rectangle")
l = int(input())
b = int(input())
          
square_area = calculate_square_area(sqs)
print("Area of the square:", square_area)

triangle_area = calculate_triangle_area(bs, ht)
print("Area of the triangle:", triangle_area)

rectangle_area = calculate_rectangle_area(l, b)
print("Area of the rectangle:", rectangle_area)


