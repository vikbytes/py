def print_trianglar_numbers(n):
    i = 1
    while i < n+1:
        z = (i*(i+1)) / 2
        print(i,"\t",z)
        i = i+1

print_trianglar_numbers(int(input("Number: ")))
