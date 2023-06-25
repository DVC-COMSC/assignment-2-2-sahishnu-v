def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    celsius = int(input('What is your degrees in celsius? '))
    fahrenheit = 9 / 5 * celsius + 32
    print (f'Fahrenheit: \t {fahrenheit:.2f}')
    return celsius, fahrenheit


if __name__ == '__main__':
    main()
