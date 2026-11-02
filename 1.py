def square_numbers(start, end):
    squares = [i ** 2 for i in range(start, end + 1)]

    odd_squares = [num for num in squares if num % 2 != 0]
    even_squares = [num for num in squares if num % 2 == 0]

    print("Odd square values:", odd_squares)
    print("Even square values:", even_squares)


square_numbers(1, 10)