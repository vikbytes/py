# Function to check is a year is a leap year or not
def leap_year(x):
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 != 0:
                return False
        return True
    else:
        return False

print(leap_year(int(input("Year: "))))