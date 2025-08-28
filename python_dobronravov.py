def num_validation():
    while True:
        try:
            num = float(input("Enter a number greater than 7: "))
            if num > 7:
                print("Hello")
                break
            else:
                print("The number must be greater than 7.")
        except ValueError:
            print("Invalid input, please enter a number.")

    
def name_validation():
    while True:
        name = input("Enter a name (or press Enter to exit): ")
        if not name: 
            print("Exit name check.")
            break
        if name == "John":
            print("Hello, John")
            break
        else:
            print("There is no such name.")

def multiples_of_three():
    while True:
        try:
            user_input = input("Enter a sequence of numbers separated by spaces (or press Enter to exit): ")
            if not user_input:
                print('No input provided. Exiting.')
                break
            numbers = [int(i) for i in user_input.split() if int(i) % 3 == 0]
            if numbers:
                print(numbers)
            else:
                print('No numbers multiples 3 found')
        except ValueError:
            print("Invalid input, please enter only numbers separated by spaces.")


if __name__ == '__main__':
    num_validation()
    name_validation()
    multiples_of_three()
