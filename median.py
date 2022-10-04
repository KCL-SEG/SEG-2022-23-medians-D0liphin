def is_even(n: int) -> bool:
    """
    returns `True` if the provided `int` is even, otherwise
    returns `False`
    """    
    return n % 2 == 0

if __name__ == "__main__":
    while True:
        try:
            user_input = input("Enter a list of numbers separated by commas:\n")
            if user_input == "exit()": break

            numbers = [float(n) for n in user_input.split(",")]
            numbers.sort()

            middle_index = len(numbers) // 2;
            if is_even(len(numbers)):
                median = (numbers[middle_index] + numbers[middle_index - 1]) / 2
            else:
                median = numbers[middle_index]
                
            print(f"median = {median}")
        except Exception as e: 
            print(e)
        else: break