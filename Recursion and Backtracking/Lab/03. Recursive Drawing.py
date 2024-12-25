number = int(input())


def recursive_drawing(number):

        if number == 0:
          return

        print("*" * number)

        recursive_drawing(number - 1)

        print("#" * number)


recursive_drawing(number)
