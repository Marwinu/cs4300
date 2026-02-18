# Check if a number is zero, positive, negative
def define_state(numbers):
    if numbers > 0:
        return "positive"
    elif numbers < 0:
        return "negative"
    else:
        return "zero"


# Return list of prime numbers
def first_prime_nums(numbers):
    prime_nums = []
    num = 2

    while len(prime_nums) < numbers:  # keeps going until number of primes is met
        if num <= 1:   
            is_prime = False
        else:
            is_prime = True
            # divisibility from2 up to sqrt(num)
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:   # divisor found
                    is_prime = False
                    break
        if is_prime:
            prime_nums.append(num)
        num += 1
    return prime_nums


# Returns a sum of numbers
def sum_nums(numbers):
    total = 0
    i = 1
    while i <= numbers:
        total += i
        i += 1
    return total

if __name__ == "__main__":
    try:
        number = int(input("Enter a number to check its state, positive, negative, or zero: "))
        print(f"{number} is {define_state(number)}")

        prime_count = int(input("Enter the number of prime numbers to print: "))
        print(f"Primes: {first_prime_nums(prime_count)}")

        total_sum = int(input("How many numbers to sum: "))
        print(f"Sum: {sum_nums(total_sum)}")

    except ValueError:
        print("Invalid input! Please enter integers only.")