def find_and_print_letters(input_string):
    # Find the first occurrence of 'A'
    first_a_index = input_string.find('A')
    
    # If 'A' is not found, find the first 'B'
    if first_a_index == -1:
        first_b_index = input_string.find('B')
        
        # If 'B' is not found, find the first 'C'
        if first_b_index == -1:
            first_c_index = input_string.find('C')
            if first_c_index != -1:
                last_c_index = input_string.rfind('C')
                if last_c_index != -1:
                    result = input_string[first_c_index + 1:last_c_index]
                    print(result)
            else:
                print("No 'A', 'B', or 'C' found in the input.")
        else:
            last_b_index = input_string.rfind('B')
            if last_b_index != -1:
                result = input_string[first_b_index + 1:last_b_index]
                print(result)
    else:
        last_a_index = input_string.rfind('A')
        if last_a_index != -1:
            result = input_string[first_a_index + 1:last_a_index]
            print(result)
        else:
            print("Only one 'A' found in the input.")

# Example usage:
input_string = "ABCDEABCDE"
find_and_print_letters(input_string)


