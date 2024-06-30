def main():
    # Input the number
    N = int(input('Enter the number N: '))
    result = []

    """
    ########################################
    Code Your Program here
    ########################################
    """
    # create a definiton for "calculate_power_of_2" in order to calculate result
    def calculate_powers_of_2(n):
        result=[] # initialize an empty list named "result" to store the powers of 2
        for i in range(n + 1): # use the range(n+1) function to create a sequence of numbers from 0 to N
            result.append(2 ** i)# for each value of i in the loop, calculate 2 raised to the power of i
        return result #return the list of powers of 2
    result = calculate_powers_of_2(N)
    print(result)
    

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
