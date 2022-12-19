#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Dec 19, 2022
# A program which uses lists and without functions
# to round a decimal number

# function used to calculate output
def round_decimal(decimal, places):
    # multiples inputted number by 10 to the power of places
    decimal[0] *= 10**places

    # Adds 0.5
    decimal[0] += 0.5

    # converts float to int
    decimal[0] = int(decimal[0])

    # divides by 10 to the power of places
    decimal[0] /= 10**places


def main():

    # input before sent though the try catch
    user_decimal = input("Input a decimal number: ")
    # try catch to convert input above into a float
    try:
        user_decimal_flo = float(user_decimal)
    except Exception:
        print("Inputted decimal is an invalid, use decimal numbers only!")
    else:
        # input before being sent though the try catch
        user_places = input("Enter amount to round: ")
        # try catch to convert the input above into ints
        try:
            user_places_int = int(user_places)
        except Exception:
            print("Inputted amount is an invalid amount, use integers only!")

            # Creates an empty list
        else:
            numb_list = []

            # adds first input into the list
            numb_list.append(user_decimal_flo)

            # calls the function
            round_decimal(numb_list, user_places_int)

            # uses the function to display the outcome
            print(
                f"{user_decimal_flo} rounded to {user_places_int} decimal places = {numb_list[0]}"
            )


if __name__ == "__main__":
    main()
