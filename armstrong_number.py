"""Find the three-digit numbers equal to the sum of their cubed digits."""

def armstrong_numbers():
    return [number for number in range(100, 1000)
            if sum(int(digit) ** 3 for digit in str(number)) == number]

def find_armstrong_numbers():
    numbers = armstrong_numbers()
    for number in numbers:
        print("Armstrong number:", number)
    print(len(numbers), "three-digit Armstrong numbers found")

if __name__ == "__main__":
    find_armstrong_numbers()
