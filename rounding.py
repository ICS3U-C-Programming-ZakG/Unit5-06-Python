#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Dec. 6, 2023
# This program rounds numbers and uses pass by reference.


def round_decimal(num_one, round_places):
    # calculations to round number
    num_one[0] = num_one[0] * 10**3 + 0.5
    num_one[0] = int(num_one[0])
    num_one[0] = num_one[0] / 10**3


def main():
    # introduce program to user
    print("This program rounds decimals.")

    # declare variable
    user_num_one = []

    # get user inputs
    user_number = input("Please enter a number: ")
    user_round_num = input("Please enter the number of places you want to round: ")

    # try casting first input to a float
    try:
        num_one_float = float(user_number)

        # append user input to table
        user_num_one.append(num_one_float)

        # try casting second number to an integer
        try:
            round_num = int(user_round_num)

            # call function
            round_decimal(user_num_one, round_num)

            # display result to user
            print(
                "The decimals rounded to {} decimals places equals: {}".format(
                    user_round_num, user_num_one[0]
                )
            )

        # catch invalid inputs for second number
        except Exception:
            print(
                "You must enter a whole number which {} is not".format(user_round_num)
            )

    # catch invalid inputs for first number
    except Exception:
        print("You must enter a decimal number.")


if __name__ == "__main__":
    main()
