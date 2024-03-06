def nawleens_countdown(number):
    """
    Counts down from the given number to 0 and prints Mardi Gras-themed strings for each number.

    Args:
        number: The starting number to count down from.
    """

    # Check if the number is valid (up to 500)
    if number > 500 or number < 0:
        print("Invalid input. Please enter a number between 0 and 500.")
        return

    # Iterate over the numbers from the input number down to 0
    for i in range(number, -1, -1):
        # Create an empty string to store the message
        message = ""

        # Concatenate the number to the message
        message += str(i) + " "

        # Check if the number is divisible by 7
        if i % 7 == 0:
            message += "Nawleens at the Mardi Gras"

        # Check if the number is divisible by 11
        if i % 11 == 0:
            message += "down in the bayou"

        # Check if the number is divisible by both 7 and 11
        if i % 7 == 0 and i % 11 == 0:
            message += ", eat'n that good nutria burgoo"

            # Check if the number is even
            if i % 2 == 0:
                message += ", gyatt thats good"

        # Check if the number is divisible by 10
        if i % 10 == 0:
            message = (
                str(i)
                + " New Orleans at Mardi Gras sitting down to eat at a fine meal at Commanders Palace."
            )

        # Otherwise, just add the word "Nawleens"
        else:
            message += "Nawleens"

        # Print the final message
        print(message)


nawleens_countdown(200)
