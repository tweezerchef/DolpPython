def mardi_gras_countdown(number):
    """
    Prints a countdown from the given number to 0, with Mardi Gras-themed strings.

    Args:
        number: The starting number, up to 500.
    """

    # Check if the input number is valid
    if number > 500:
        print("Error: Number must be less than or equal to 500.")
        return

    # Loop through the numbers in descending order
    while number >= 0:
        # Initialize the output string
        output_str = str(number) + " Nawleens"

        # Check if the number is divisible by 7, 11, or both
        if number % 7 == 0:
            output_str += " at the Mardi Gras"
        if number % 11 == 0:
            output_str += " down in the bayou"
        if number % 7 == 0 and number % 11 == 0:
            output_str += ", eat'n that good nutria burgoo"
            if number % 2 == 0:
                output_str += ", gyatt thats good"

        # Check if the number is divisible by 10
        if number % 10 == 0:
            output_str = (
                str(number)
                + " New Orleans at Mardi Gras sitting down to eat at a fine meal at Commanders Palace."
            )

        # Print the output string
        print(output_str)

        # Decrement the number
        number -= 1


mardi_gras_countdown(200)
