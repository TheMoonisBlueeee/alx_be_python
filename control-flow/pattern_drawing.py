pattern=int(input("Enter the size of the pattern:"))

for i in range(1,11):
    product= pattern * i
    print(f"{pattern} * {i} = {product}")
