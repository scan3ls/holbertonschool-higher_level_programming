def fizzbuzz():
    # fizzbuzz - print 1-99 replacing multiples of three with Fizz
    #                       replacing multiples of fize with Buzz
    #                       replacing multiples of both with FizzBuzz

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
