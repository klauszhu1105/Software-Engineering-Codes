def alternate_merge(list1, list2):
    merged_list = []
    for pair in zip(list1, list2):  
        for item in pair:
            merged_list.append(item)
    return merged_list

def parse_list(input_str):
    # Remove square brackets and split by comma
    input_str = input_str.strip().strip("[]")
    
    # Split elements and remove extra spaces
    elements = [elem.strip() for elem in input_str.split(",")]
    
    # Convert numeric values to integers if possible
    for i in range(len(elements)):
        if elements[i].isdigit():  # Check if it's a number
            elements[i] = int(elements[i])

    return elements

while True:
    # Get user input
    user_input = input("Enter two lists in the format: [a,b,c], [1,2,3] (or type 'q' to quit): ").strip()
    
    if user_input.lower() == 'q':
        print("Exiting the program.")
        break

    try:
        # Ensure proper format with two lists separated by `], [`
        if "], [" not in user_input:
            raise ValueError("Invalid format. Please enter two lists in the correct format.")

        # Splitting and processing each list
        list1_str, list2_str = user_input.split("], [")
        list1 = parse_list(list1_str + "]")  # Add back the closing bracket
        list2 = parse_list("[" + list2_str)  # Add back the opening bracket

        # Check if both lists are of equal length
        if len(list1) != len(list2):
            print("Error: The two lists must be of equal length.")
        else:
            # Merge the lists
            merged_result = alternate_merge(list1, list2)
            print("Merged List:", merged_result)

    except Exception as e:
        print("Error:", str(e))