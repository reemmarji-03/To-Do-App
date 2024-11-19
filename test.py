try:
    length = float(input("Enter rectangle length: "))
    width = float(input("Enter rectangle width: "))
    if width == length:
        exit("Squares are not included")
    area = length * width
    print(f"The area is {area}")

except ValueError:
    print("Please enter a number!")