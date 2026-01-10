---
title: Python Exit – How to Use an Exit Function in Python to Stop a Program
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-06-05T13:54:40.000Z'
originalURL: https://freecodecamp.org/news/python-exit-how-to-use-an-exit-function-in-python-to-stop-a-program
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/Shittu-Olumide-Python-Exit---How-to-Use-an-Exit-Function-in-Python-to-Stop-a-Program.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Shittu Olumide

  The exit() function in Python is used to exit or terminate the current running script
  or program. You can use it to stop the execution of the program at any point. When
  the exit() function is called, the program will immediately sto...'
---

By Shittu Olumide

The `exit()` function in Python is used to exit or terminate the current running script or program. You can use it to stop the execution of the program at any point. When the `exit()` function is called, the program will immediately stop running and exit.

The syntax of the `exit()` function is:

```py
exit([status])

```

Here, `status` is an optional argument that represents the exit status of the program. The exit status is an integer value that indicates the reason for program termination. By convention, a status of 0 indicates successful execution, and any non-zero status indicates an error or abnormal termination.

If the `status` argument is omitted or not provided, the default value of 0 is used.

Here's an example usage of the `exit()` function:

```bash
print("Before exit")
exit(1)
print("After exit")  # This line will not be executed

```

In this example, the program will print `"Before exit"`, but when the `exit()` function is called with a status of 1, the program will terminate immediately without executing the remaining code. Therefore, the line `"After exit"` will not be printed.

## How to Use the `exit()` Function in Python

Let's now write a Python script and demonstrate how you can use the exit function properly in a real world scenario.

```py
import sys

def main():
    try:
        print("Welcome to the program!")
        
        # Check for termination condition
        user_input = input("Do you want to exit the program? (y/n): ")
        if user_input.lower() == "y":
            exit_program()
        
        # Continue with other operations
        
    except Exception as e:
        print(f"An error occurred: {e}")
        exit_program()

def exit_program():
    print("Exiting the program...")
    sys.exit(0)

if __name__ == "__main__":
    main()

```

**Code explanation**:

1. The script starts by importing the `sys` module, which provides access to the `exit()` function.
2. The `main()` function serves as the entry point of the program. You can add your code and operations within this function.
3. Within the `main()` function, you can perform various operations. In this example, you simply print a welcome message and ask the user if they want to exit.
4. After receiving user input, you check if the user wants to exit by comparing their input to "y" (case-insensitive). If the condition is true, you call the `exit_program()` function to terminate the script.
5. The `exit_program()` function prints a message indicating that the program is exiting and then calls `sys.exit(0)` to terminate the program. The argument `0` passed to `sys.exit()` indicates a successful termination. You can choose a different exit code if needed.
6. Finally, you check if the script is being executed as the main module by using the `__name__` variable. If it is, you call the `main()` function to start the program.

## Best Practices When Using the `exit()` Function 

Here are some best practices for using the `exit()` function effectively:

**Import the `sys` module**: Before using the `exit()` function, you need to import the `sys` module at the beginning of your script. Include the following line of code:

```py
import sys

```

**Determine the exit condition**: Identify the condition or situation where you want to exit the program. This can be based on user input, a specific event, an error condition, or any other criteria that require the program to stop.

**Use `sys.exit()` to terminate the program**: When the exit condition is met, call the `sys.exit()` function to halt the program's execution. You can pass an optional exit status code as an argument to the function, indicating the reason for termination. 

Again, a status code of 0 is typically used to indicate successful program completion, while non-zero values represent different types of errors or exceptional conditions.

```py
if condition_met:
    sys.exit()  # Terminate the program with status code 0

```

You can also pass a status code to provide additional information:

```py
if error_occurred:
    sys.exit(1)  # Terminate the program with status code 1 indicating an error

```

**Clean up resources (optional)**: If your program uses resources that need to be properly closed or released before termination, you can include cleanup code before calling `sys.exit()`. For example, closing open files or releasing network connections. This ensures that resources are handled appropriately, even if the program is terminated unexpectedly.

**Document exit conditions**: It's important to document the specific exit conditions in your code and provide comments indicating why the program is being terminated. This helps other developers understand the purpose and behavior of the `exit()` calls.

## Conclusion

In summary, this article showed you how to utilize the `exit()` function in Python to terminate program execution. Optionally, an exit status code can be passed as an argument, providing additional information about the reason for termination.

By adhering to these best practices, you can effectively utilize the `sys.exit()` function in Python to stop a program when necessary. 

It is crucial to exercise caution and judiciously employ this function, and only use it in appropriate circumstances when you want to forcefully halt the execution of your Python script under certain conditions or when you need to terminate the program abruptly. 

Some scenarios where you might want to use the `exit()` function: error handling, conditional termination, testing and debugging, and script completion. 

Let's connect on [Twitter](https://www.twitter.com/Shittu_Olumide_) and on [LinkedIn](https://www.linkedin.com/in/olumide-shittu). You can also subscribe to my [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A) channel.

Happy Coding!

