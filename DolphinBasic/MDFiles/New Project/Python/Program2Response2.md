```Python
# Create function using the keyword def and name the function mardi_gras_countdown. The function takes one argument, number.
def mardi_gras_countdown(number):
    """
    Prints a countdown from the given number to 0, with Mardi Gras-themed strings.

    Args:
        number: The starting number, up to 500.
    """

    # Uses keyword if to check if the input number is under 500. If the number is greater than 500, the function prints using the keyword print an error message and exits the function using the keyword return.
    if number > 500:
        print("Error: Number must be less than or equal to 500.")
        return

    # Uses while keyword to create a loop that runs until the number is less than 0.
    while number >= 0:
        # Creates the variable output_str and sets it to the string representation of the number followed by the word "Nawleens".
        output_str = str(number) + " Nawleens"

        # Check if the is divisible by 7, and if so, adds the string " at the Mardi Gras" to the output_str. The other lines check if then number is divisible by 11 then 7, then 7 and 11, then 2, and adds the appropriate string to the output_str.
        if number % 7 == 0:
            output_str += " at the Mardi Gras"
        if number % 11 == 0:
            output_str += " down in the bayou"
        if number % 7 == 0 and number % 11 == 0:
            output_str += ", eat'n that good nutria burgoo"
            if number % 2 == 0:
                output_str += ", gyatt thats good"

        # Check if the number is divisible by 10 and if so, replaces the output_str with a new string that includes the number and the sentence "New Orleans at Mardi Gras sitting down to eat at a fine meal at Commanders Palace."
        if number % 10 == 0:
            output_str = (
                str(number)
                + " New Orleans at Mardi Gras sitting down to eat at a fine meal at Commanders Palace."
            )

        # Print the output string for a signal number and then decrement the number by 1.
        print(output_str)
        number -= 1

# Call the function mardi_gras_countdown with the argument 200.
mardi_gras_countdown(200)
```
