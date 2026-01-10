---
title: The Python Decorator Handbook
subtitle: ''
author: Atharva Shah
co_authors: []
series: null
date: '2024-01-26T17:17:03.000Z'
originalURL: https://freecodecamp.org/news/the-python-decorator-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/The-Python-Decorator-Handbook-Cover.png
tags:
- name: decorator
  slug: decorator
- name: handbook
  slug: handbook
- name: Python
  slug: python
- name: Python 3
  slug: python3
seo_title: null
seo_desc: 'Python decorators provide an easy yet powerful syntax for modifying and
  extending the behavior of functions in your code.

  A decorator is essentially a function that takes another function, augments its
  functionality, and returns a new function – with...'
---

Python decorators provide an easy yet powerful syntax for modifying and extending the behavior of functions in your code.

A decorator is essentially a function that takes another function, augments its functionality, and returns a new function – without permanently modifying the original function itself.

This tutorial will walk you through 11 handy decorators to help add functionality like timing execution, caching, rate limiting, debugging and more. Whether you want to profile performance, improve efficiency, validate data, or manage errors, these decorators have got you covered!

The examples here focus on the common usage patterns and utilities of decorators that can come in handy in your day-to-day programming and save you a lot of effort. Understanding the flexibility of decorators will help you write clean, resilient, and optimized application code.

## Table of Contents

Here are the decorators covered in this tutorial:

* [Log Arguments and Return Value of a Function](#heading-log-arguments-and-return-value-of-a-function)
    
* [Get the Execution Time of a Function](#heading-get-the-execution-time-of-a-function)
    
* [Convert Function Return Value to a Specified Data Type](#heading-convert-function-return-value-to-a-specified-data-type)
    
* [Cache Function Results](#heading-cache-function-results)
    
* [Validate Function Arguments Based on Condition](#heading-validate-function-arguments-based-on-condition)
    
* [Retry a Function Multiple Times on Failure](#heading-retry-a-function-multiple-times-on-failure)
    
* [Enforce Rate Limits on a Function](#heading-enforce-rate-limits-on-a-function)
    
* [Handle Exceptions and Provide Default Response](#heading-handle-exceptions-and-provide-default-response)
    
* [Enforce Type Checking on Function Arguments](#heading-enforce-type-checking-on-function-arguments)
    
* [Measure Memory Usage of a Function](#heading-measure-memory-usage-of-a-function)
    
* [Cache Function Results with Expiration Time](#heading-cache-function-results-with-expiration-time)
    
* [Conclusion](#heading-conclusion)
    

But first, a little introduction.

## How Python Decorators Work

Before diving in, let's understand some key benefits of decorators in Python:

* **Enhancing functions without invasive changes:** Decorators augment functions transparently without altering the original code, keeping the core logic clean and maintainable.
    
* **Reusing functionality across places:** Common capabilities like logging, caching, and rate limiting can be built once in decorators and applied wherever needed.
    
* **Readable and declarative syntax:** The `@decorator` syntax simply conveys functionality enhancement at the definition site.
    
* **Modularity and separation of concerns:** Decorators promote loose coupling between functional logic and secondary capabilities like performance, security, logging etc.
    

The takeaway is that decorators unlock simple yet flexible ways of transparently enhancing Python functions for improved code organization, efficiency, and reuse without introducing complexity or redundancy.

Here is a basic example of decorator syntax in Python with annotations:

```python
# Decorator function
def my_decorator(func):

# Wrapper function
    def wrapper():
        print("Before the function call") # Extra processing before the function
        func() # Call the actual function being decorated
        print("After the function call") # Extra processing after the function
    return wrapper # Return the nested wrapper function

# Function to decorate
def my_function():
    print("Inside my function")

# Apply decorator on the function
@my_decorator
def my_function():
    print("Inside my function")

# Call the decorated function
my_function()
```

A decorator in Python is a function that takes another function as an argument and extends its behavior without modifying it. The decorator function wraps the original function by defining a wrapper function inside of it. This wrapper function executes code before and after calling the original function.

Specifically, when defining a decorator function such as `my_decorator` in the example, it takes a function as an argument, which we generally call `func`. This `func` will be the actual function that is decorated under the hood.

The wrapper function inside `my_decorator` can execute arbitrary code before and after calling `func()`, which invokes the original function. When applying `@my_decorator` before the definition of `my_function`, it passes `my_function` as an argument to `my_decorator`, so func refers to `my_function` in that context.

The wrapper function then returns the enhanced wrapped function. So now `my_function` has been decorated by `my_decorator`. When it is later called, the wrapper code inside `my_decorator` executes before and after `my_function` runs. This allows decorators to transparently extend the behavior of a function, without needing to modify the function itself.

And as you'll recall, the original `my_function` remains unchanged, keeping decorators non-invasive and flexible.

When `my_function()` is decorated with `@my_decorator`, it is automatically enhanced. The `my_decorator` function here returns a wrapper function. This wrapper function gets executed when the `my_function()` is called now.

First, the wrapper prints `"Before the function call"` before actually calling the original `my_function()` function being decorated. Then, after `my_function()` executes, it prints `"After function call"`.

So, additional behavior and printed messages are added before and after the `my_function()` execution in the wrapper, without directly modifying `my_function()` itself. The decorator allows you to extend `my_function()` in a transparent way without affecting its core logic, as the wrapper handles the enhanced behavior.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-109.png align="left")

*Applying a Decorator to a Function*

So let's start exploring the top 11 practical decorators that every Python developer should know.

## Log Arguments and Return Value of a Function

The Log Arguments and Return Value decorator tracks the input parameters and output of functions. This supports debugging by logging a clear record of data flow through complex operations.

```python
def log_decorator(original_function):
    def wrapper(*args, **kwargs):
        print(f"Calling {original_function.__name__} with args: {args}, kwargs: {kwargs}")

        # Call the original function
        result = original_function(*args, **kwargs)

        # Log the return value
        print(f"{original_function.__name__} returned: {result}")

        # Return the result
        return result
    return wrapper

# Example usage
@log_decorator
def calculate_product(x, y):
    return x * y

# Call the decorated function
result = calculate_product(10, 20)
print("Result:", result)
```

**Output:**

```javascript
Calling calculate_product with args: (10, 20), kwargs: {}
calculate_product returned: 200
Result: 200
```

In this example, the decorator function is named `log_decorator()` and accepts a function, `original_function`, as its argument. Within `log_decorator()`, a nested function called `wrapper()` is defined. This `wrapper()` function is what the decorator returns and effectively replaces the original function.

When the `wrapper()` function is invoked, it prints logging statements pertaining to the function call. Then it calls the original function, `original_function`, captures its result, prints the outcome, and returns the result.

The `@log_decorator` syntax above the `calculate_product()` function is a Python convention to apply the `log_decorator` as a decorator to the `calculate_product` function. So when `calculate_product()` is invoked, it's actually invoking the `wrapper()` function returned by `log_decorator()`. Therefore, `log_decorator()` acts as a wrapper, introducing logging statements before and after the execution of the original `calculate_product()` function.

### Usage and Applications

This decorator is widely adopted in application development for adding runtime logging without interfering with business logic implementation.

For example, consider a banking application that processes financial transactions. The core transaction processing logic resides in functions like `transfer_funds()` and `accept_payment()`. To monitor these transactions, logging can be added by including `@log_decorator` above each function.

Then when transactions are triggered by calling `transfer_funds()`, you can print the function name, arguments like the sender, receiver, and amount before the actual transfer. Then after the function returns, you can print the whether the transfer succeeded or failed.

This type of logging with decorators allows you to track transactions without adding any code to core functions like `transfer_funds()`. The logic stays clean while debuggability and observability improves. Logging messages can be directed to a monitoring dashboard or log analytics system as well.

## Get the Execution Time of a Function

This decorator is your ally in the quest for performance optimization. By measuring and logging the execution time of a function, this decorator facilitates a deep dive into the efficiency of your code, helping you pinpoint bottlenecks and streamline your application's performance.

It's ideal for scenarios where speed is crucial, such as real-time applications or large-scale data processing. And it allows you to identify and address performance bottlenecks systematically.

```python
import time

def measure_execution_time(func):
    def timed_execution(*args, **kwargs):
        start_timestamp = time.time()
        result = func(*args, **kwargs)
        end_timestamp = time.time()
        execution_duration = end_timestamp - start_timestamp
        print(f"Function {func.__name__} took {execution_duration:.2f} seconds to execute")
        return result
    return timed_execution

# Example usage
@measure_execution_time
def multiply_numbers(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

# Call the decorated function
result = multiply_numbers([i for i in range(1, 10)])
print(f"Result: {result}")
```

**Output:**

```javascript
Function multiply_numbers took 0.00 seconds to execute
Result: 362880
```

This code showcases a decorator that's designed to measure the execution duration of functions.

The `measure_execution_time()` decorator takes a function, `func`, and defines an inner function, `timed_execution()`, to wrap the original function. Upon invocation, `timed_execution()` records the start time, calls the original function, records the end time, calculates the duration, and prints it.

The `@measure_execution_time` syntax applies this decorator to functions below it, such as `multiply_numbers()`. Consequently, when `multiply_numbers()` is called, it invokes the `timed_execution()` wrapper, which logs the duration alongside the function result.

This example illustrates how decorators seamlessly augment existing functions with additional functionality, like timing, without direct modification.

### Usage and Applications

This decorator is helpful in profiling functions to identify performance bottlenecks in applications. For example, consider an e-commerce site with several backend functions like `get_recommendations()`, `calculate_shipping()`, and so on. By decorating them with `@measure_execution_time`, you can monitor their runtime.

When `get_recommendations()` is invoked in a user session, the decorator will time its execution duration by recording a start and end timestamp. After execution, it will print the time taken before returning recommendations.

Doing this systematically across applications and analyzing outputs will show you the functions that are taking an unusually long time. The development team can then optimize such functions through caching, parallel processing, and other techniques to improve overall application performance.

Without such timing decorators, finding optimization candidates would require tedious logging code additions. Decorators provide visibility easily without contaminating business logic.

## Convert Function Return Value to a Specified Data Type

The Convert Return Value Type decorator enhances data consistency in functions by automatically converting the return value to a specified data type, promoting predictability and preventing unexpected errors. It is particularly useful for downstream processes that require consistent data types, reducing runtime errors.

```python
def convert_to_data_type(target_type):
    def type_converter_decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return target_type(result)
        return wrapper
    return type_converter_decorator

@convert_to_data_type(int)
def add_values(a, b):
    return a + b

int_result = add_values(10, 20)
print("Result:", int_result, type(int_result))

@convert_to_data_type(str)
def concatenate_strings(str1, str2):
    return str1 + str2

str_result = concatenate_strings("Python", " Decorator")
print("Result:", str_result, type(str_result))
```

**Output:**

```javascript
Result: 30 <class 'int'>
Result: Python Decorator <class 'str'>
```

The above code example shows a decorator that's designed to convert the return value of a function to a specified data type.

The decorator, named `convert_to_data_type()`, takes the target data type as a parameter and returns a decorator named `type_converter_decorator()`. Within this decorator, a `wrapper()` function is defined to call the original function, convert its return value to the target type using `target_type()`, and subsequently return the converted result.

The syntax `@convert_to_data_type(int)` that's applied above a function (such as `add_values()`) utilizes this decorator to convert the return value to an integer. Similarly, for `concatenate_strings()`, passing `str` formats the return value as a string.

This example also showcases how decorators seamlessly modify function outputs to desired formats without altering the core logic of the functions.

### Usage and Application

This return value transformation decorator proves useful in applications where you need to automatically adapt functions to expected data formats.

For instance, you could use it in a weather API that returns temperatures by default in decimal format like 23.456 degrees. But the consumer front-end application expects an integer value to display.

Instead of changing the API function to return an integer, just decorate it with `@convert_to_data_type(int)`. This will seamlessly convert the decimal temperature to the integer `23`, in this example, before returning to the client app. Without any API function modification, you've reformatted the return value.

Similarly for backend processing expecting JSON, return values can be converted using the `@convert_to_data_type(json)` decorator. The core logic stays unchanged while the presentation format adapts based on your use case's needs. This avoids duplication of format handling code across functions.

Decorators externally impose required data representations for seamless integration and reusability across application layers with mismatched formats.

## Cache Function Results

This decorator optimizes performance by storing and retrieving function results, eliminating redundant computations for repeated inputs, and improving application responsiveness, especially for time-consuming computations.

```python
def cached_result_decorator(func):
    result_cache = {}

    def wrapper(*args, **kwargs):
        cache_key = (*args, *kwargs.items())

        if cache_key in result_cache:
            return f"[FROM CACHE] {result_cache[cache_key]}"

        result = func(*args, **kwargs)
        result_cache[cache_key] = result

        return result

    return wrapper

# Example usage

@cached_result_decorator
def multiply_numbers(a, b):
    return f"Product = {a * b}"

# Call the decorated function multiple times
print(multiply_numbers(4, 5))  # Calculation is performed
print(multiply_numbers(4, 5))  # Result is retrieved from cache
print(multiply_numbers(5, 7))  # Calculation is performed
print(multiply_numbers(5, 7))  # Result is retrieved from cache
print(multiply_numbers(-3, 7))  # Calculation is performed
print(multiply_numbers(-3, 7))  # Result is retrieved from cache
```

**Output:**

```javascript
Product = 20
[FROM CACHE] Product = 20
Product = 35
[FROM CACHE] Product = 35
Product = -21
[FROM CACHE] Product = -21
```

This code sample showcases a decorator that's designed to cache and reuse function call results efficiently.

The `cached_result_decorator()` function takes another function and returns a wrapper. Within this wrapper, a cache dictionary (`result_cache`) stores unique call parameters and their corresponding results.

Before executing the actual function, the `wrapper()` checks if the result for the current parameters is already in the cache. If so, it retrieves and returns the cached result – otherwise, it calls the function, stores the result in the cache, and returns it.

The `@cached_result_decorator` syntax applies this caching logic to any function, such as `multiply_numbers()`. This ensures that, upon subsequent calls with the same arguments, the cached result is reused, preventing redundant calculations.

In essence, the decorator enhances functionality by optimizing performance through result caching.

### Usage and Applications

Caching decorators like this are extremely useful in application development for optimizing performance of repetitive function calls.

For example, consider a recommendation engine calling predictive model functions to generate user suggestions. `get_user_recommendations()` prepares the input data and feeds into the model for every user request.Instead of re-running computations, it can be decorated with `@cached_result_decorator` to introduce caching layer.

Now the first time unique user parameters are passed, the model runs and the result caches. Subsequent calls with the same inputs directly return the cached model outputs, skipping the model recalculation.

This drastically improves latency for responding to user requests by avoiding duplicate model inferences. You can monitor cache hit rates to justify scaling down model server infrastructure costs.

Decoupling such optimization concerns through caching decorators rather than mixing them inside function logic improves modularity, readability and allows rapid performance gains. Caches will be configured, invalidated separately without intruding business functions.

## Validate Function Arguments Based on Condition

This one checks if input arguments meet predefined criteria before execution, enhancing function reliability and preventing unexpected behavior. It is useful for parameters requiring positive integers or non-empty strings.

```python
def check_condition_positive(value):
    def argument_validator(func):
        def validate_and_calculate(*args, **kwargs):
            if value(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                raise ValueError("Invalid arguments passed to the function")
        return validate_and_calculate
    return argument_validator

@check_condition_positive(lambda x: x > 0)
def compute_cubed_result(number):
    return number ** 3

print(compute_cubed_result(5))  # Output: 125
print(compute_cubed_result(-2))  # Raises ValueError: Invalid arguments passed to the function
```

**Output:**

```javascript
125Traceback (most recent call last):

  File "C:\\\\Program Files\\\\Sublime Text 3\\\\test.py", line 16, in <module>
    print(compute_cubed_result(-2))  # Raises ValueError: Invalid arguments passed to the function
  File "C:\\\\Program Files\\\\Sublime Text 3\\\\test.py", line 7, in validate_and_calculate
    raise ValueError("Invalid arguments passed to the function")
ValueError: Invalid arguments passed to the function
```

This code showcases how you can implement a decorator for validating function arguments.

The `check_condition_positive()` is a decorator factory that generates an `argument_validator()` decorator. This validator, when applied with `@check_condition_positive()` above the `compute_cubed_result()` function, checks if the condition (in this case, that the argument should be greater than 0) holds true for the passed arguments.

If the condition is met, the decorated function is executed – otherwise, a `ValueError` exception is raised.

This succinct example illustrates how decorators serve as a mechanism for validating function arguments before their execution, ensuring adherence to specified conditions.

### Usage and Applications

Such parameter validation decorators are extremely useful in applications to help enforce business rules, security constraints, and so on.

For example, an insurance claims processing system would have a function `process_claim()` that takes details like claim id, approver name, and so on. Certain business rules dictate who can approve claims.

Rather than cluttering the function logic itself, you can decorate it with `@check_condition_positive()` which validates if the approver role matches the claim amount. If a junior agent tries approving a large claim (thus violating the rules), this decorator would catch it by raising exception even before `process_claim()` executes.

Similarly, input data validation constraints for security and compliance can be imposed without touching individual functions. Decorators externally ensure that violated arguments never reach application risks.

Common validation patterns should be reused across multiple functions. This improves security and promotes separation of concerns by isolating constraints from core logic flow in a modular way.

## Retry a Function Multiple Times on Failure

This decorator comes handy when you want to automatically retry a function after failure, enhancing its resilience in situations involving transient failures. It is used for external services or network requests prone to intermittent failures.

```python
import sqlite3
import time

def retry_on_failure(max_attempts, retry_delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(max_attempts):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as error:
                    print(f"Error occurred: {error}. Retrying...")
                    time.sleep(retry_delay)
            raise Exception("Maximum attempts exceeded. Function failed.")

        return wrapper
    return decorator

@retry_on_failure(max_attempts=3, retry_delay=2)
def establish_database_connection():
    connection = sqlite3.connect("example.db")
    db_cursor = connection.cursor()
    db_cursor.execute("SELECT * FROM users")
    query_result = db_cursor.fetchall()
    db_cursor.close()
    connection.close()
    return query_result

try:
    retrieved_data = establish_database_connection()
    print("Data retrieved successfully:", retrieved_data)
except Exception as error_message:
    print(f"Failed to establish database connection: {error_message}")
```

**Output:**

```javascript
Error occurred: no such table: users. Retrying...
Error occurred: no such table: users. Retrying...
Error occurred: no such table: users. Retrying...
Failed to establish database connection: Maximum attempts exceeded. Function failed.
```

This example introduces a decorator that's designed for retrying function executions in the event of failures. It has a specified maximum attempt count and delay between retries.

The `retry_on_failure()` is a decorator factory, taking parameters for maximum retry count and delay, and returning a `decorator()` that manages the retry logic.

Within the `wrapper()` function, the decorated function undergoes execution in a loop, attempting a specified maximum number of times.

In case of an exception, it prints an error message, introduces a delay specified by `retry_delay`, and retries. If all attempts fail, it raises an exception indicating that the maximum attempts have been exceeded.

The `@retry_on_failure()` applied above `establish_database_connection()` integrates this retry logic, allowing for up to 3 retries with a 2-second delay between each attempt in case the database connection encounters failures.

This demonstrates the utility of decorators in seamlessly incorporating retry capabilities without altering the core function code.

### Usage and Application

This retry decorator can prove extremely useful in application development for adding resilience against temporary or intermittent errors.

For instance, consider a flight booking app that calls a payment gateway API `process_payment()` to handle customer transactions. Sometimes network blips or high loads at payment provider end could cause transient errors in API response.

Rather than directly showing failures to customers, the `process_payment()` function can be decorated with `@retry_on_failure` to handle such scenarios implicitly. Now when a payment fails once, it will seamlessly retry sending the request up to 3 times before finally reporting the error if it persists.

This provides shielding from temporary hiccups without exposing users to unreliable infrastructure behavior directly.The application also remains available reliably even if dependent services fail occasionally.

The decorator helps confine the retry logic neatly without spreading it across the API's code. Failures beyond the app's control are handled gracefully rather than directly impacting users by application faults. This demonstrates how decorators lend better resilience without complicating business logic.

## Enforce Rate Limits on a Function

By controlling the frequency of functions called, the Enforce Rate Limits decorator ensures effective resource management and guards against misuse. It is especially helpful in scenarios like API misuse or resource conservation where restricting function calls is essential.

```python
import time

def rate_limiter(max_allowed_calls, reset_period_seconds):
    def decorate_rate_limited_function(original_function):
        calls_count = 0
        last_reset_time = time.time()

        def wrapper_function(*args, **kwargs):
            nonlocal calls_count, last_reset_time
            elapsed_time = time.time() - last_reset_time

            # If the elapsed time is greater than the reset period, reset the call count
            if elapsed_time > reset_period_seconds:
                calls_count = 0
                last_reset_time = time.time()

            # Check if the call count has reached the maximum allowed limit
            if calls_count >= max_allowed_calls:
                raise Exception("Rate limit exceeded. Please try again later.")

            # Increment the call count
            calls_count += 1

            # Call the original function
            return original_function(*args, **kwargs)

        return wrapper_function
    return decorate_rate_limited_function

# Allowing a maximum of 6 API calls within 10 seconds.
@rate_limiter(max_allowed_calls=6, reset_period_seconds=10)
def make_api_call():
    print("API call executed successfully...")

# Make API calls
for _ in range(8):
    try:
        make_api_call()
    except Exception as error:
        print(f"Error occurred: {error}")
time.sleep(10)
make_api_call()
```

**Output:**

```javascript
API call executed successfully...
API call executed successfully...
API call executed successfully...
API call executed successfully...
API call executed successfully...
API call executed successfully...
Error occurred: Rate limit exceeded. Please try again later.
Error occurred: Rate limit exceeded. Please try again later.
API call executed successfully...
```

This code showcases the implementation of a rate-limiting mechanism for function calls using a decorator.

The `rate_limiter()` function, specified with maximum calls and a period in seconds to reset the count, serves as the core of the rate-limiting logic. The decorator, `decorate_rate_limited_function()`, employs a wrapper to manage the rate limits by resetting the count if the period has elapsed. It checks if the count has reached the maximum allowed, and then either raises an exception or increments the count and executes the function accordingly.

Applied to `make_api_call()` using `@rate_limiter()`, it restricts the function to six calls within any 10-second period. This introduces rate limiting without changing the function logic, ensuring that calls adhere to limits and preventing excessive use within set intervals.

### Usage and Application

Rate limiting decorators like this are very useful in application development for controlling usage of APIs and preventing abuse.

For instance, a travel booking application may rely on third party Flight Search API for checking live seat availability across airlines. While most usage is legitimate, some users could potentially call this API excessively, degrading overall service performance.

By decorating the API integration module like `@rate_limiter(100, 60)`, the application can restrict excessive calls internally, too. This would limit the booking module to make only 100 Flight API calls per minute. Additional calls get rejected directly through the decorator without even reaching actual API.

This saves downstream service from overuse enabling fairer distribution of capacity for general application functionality.

Decorators provide easy rate control for both internal and external facing APIs without changing functional code. This means you don't have to account for usage quotas while safeguarding services, infrastructure, and bounding adoption risk. And it's all thanks to application-side controls using wrappers.

## Handle Exceptions and Provide Default Response

The Handle Exceptions decorator is a safety net for functions, gracefully handling exceptions and providing default responses when they occur. It shields the application from crashing due to unforeseen circumstances, ensuring smooth operation.

```python
def handle_exceptions(default_response_msg):
    def exception_handler_decorator(func):
        def decorated_function(*args, **kwargs):
            try:
                # Call the original function
                return func(*args, **kwargs)
            except Exception as error:
                # Handle the exception and provide the default response
                print(f"Exception occurred: {error}")
                return default_response_msg
        return decorated_function
    return exception_handler_decorator

# Example usage
@handle_exceptions(default_response_msg="An error occurred!")
def divide_numbers_safely(dividend, divisor):
    return dividend / divisor

# Call the decorated function
result = divide_numbers_safely(7, 0)  # This will raise a ZeroDivisionError
print("Result:", result)
```

**Output:**

```javascript
Exception occurred: division by zero
Result: An error occurred!
```

This code showcases exception handling in functions using decorators.

The `handle_exceptions()` decorator factory, accepting a default response, produces `exception_handler_decorator()`. This decorator, when applied to functions, attempts to execute the original function. If an exception arises, it prints error details, and returns the specified default response.

The `@handle_exceptions()` syntax above a function incorporates this exception-handling logic. For instance, in `divide_numbers_safely()`, division by zero triggers an exception, which the decorator catches, preventing a crash and returning the default "An error occurred!" response.

Essentially, these decorators adeptly capture exceptions in functions, providing a seamless means of incorporating handling logic and preventing crashes.

### Usage and Applications

Exception handling decorators greatly simplify application error management and help hide unreliable behavior from users.

For example, an e-commerce website may rely on payment, inventory, and shipping services to complete orders. Instead of complex exception blocks everywhere, core order processing function like `place_order()` can be decorated to achieve resilience.

The `@handle_exceptions` decorator applied above it would absorb any third party service outage or intermittent issue during order finalization. On exception, it logs errors for debugging while serving a graceful "Order failed, please try again later" message to the customer. This avoids expose complex failure root causes like payment timeouts to end user.

Decorators shield customers from unreliable service issues without changing business code. They provide friendly default responses when errors happen. This improves customer experience

Also, decorators give developers visibility into those errors behind the scenes. So they can focus on systematically fixing the root causes of failures. This separation of concerns through decorators reduces complexity. Customers see more reliability, and you get actionable insights into faults – all while keeping business logic untouched.

## Enforce Type Checking on Function Arguments

The Enforce Type Checking decorator ensures data integrity by verifying function arguments conform to specified data types, preventing type-related errors, and promoting code reliability. It is particularly useful in situations where strict data type adherence is crucial.

```python
import inspect

def enforce_type_checking(func):
    def type_checked_wrapper(*args, **kwargs):
        # Get the function signature and parameter names
        function_signature = inspect.signature(func)
        function_parameters = function_signature.parameters

        # Iterate over the positional arguments
        for i, arg_value in enumerate(args):
            parameter_name = list(function_parameters.keys())[i]
            parameter_type = function_parameters[parameter_name].annotation
            if not isinstance(arg_value, parameter_type):
                raise TypeError(f"Argument '{parameter_name}' must be of type '{parameter_type.__name__}'")

        # Iterate over the keyword arguments
        for keyword_name, arg_value in kwargs.items():
            parameter_type = function_parameters[keyword_name].annotation
            if not isinstance(arg_value, parameter_type):
                raise TypeError(f"Argument '{keyword_name}' must be of type '{parameter_type.__name__}'")

        # Call the original function
        return func(*args, **kwargs)

    return type_checked_wrapper

# Example usage
@enforce_type_checking
def multiply_numbers(factor_1: int, factor_2: int) -> int:
    return factor_1 * factor_2

# Call the decorated function
result = multiply_numbers(5, 7)  # No type errors, returns 35
print("Result:", result)

result = multiply_numbers("5", 7)  # Type error: 'factor_1' must be of type 'int'
```

**Output:**

```javascript
Result:Traceback (most recent call last):
  File "C:\\\\Program Files\\\\Sublime Text 3\\\\test.py", line 36, in <module>
 35
    result = multiply_numbers("5", 7)  # Type error: 'factor_1' must be of type 'int'
  File "C:\\\\Program Files\\\\Sublime Text 3\\\\test.py", line 14, in type_checked_wrapper
    raise TypeError(f"Argument '{parameter_name}' must be of type '{parameter_type.__name__}'")
TypeError: Argument 'factor_1' must be of type 'int'
```

The `enforce_type_checking` decorator validates whether the arguments passed to a function match the specified type annotations.

Inside the `type_checked_wrapper`, it examines the signature of the decorated function, retrieves parameter names and type annotations, and ensures that the provided arguments align with the expected types. This includes checking positional arguments against their order, and keyword arguments against parameter names. If a type mismatch is detected, a TypeError is raised.

This decorator is exemplified by its application to the `multiply_numbers` function, where arguments are annotated as integers. Attempting to pass a string results in an exception, while passing integers executes the function without issues. This type checking is enforced without altering the original function body.

### Usage and Applications

Type checking decorators are applied to detect issues early and improve reliability. For example, consider a web application backend with a data access layer function `get_user_data()` annotated to expect integer user IDs. Its queries would fail if string IDs flow into it from frontend code.

Rather than add explicit checks and raise exceptions locally, you can use this decorator. Now any upstream or consumer code passing invalid types will be automatically caught during function execution. The decorator examines annotations versus argument types and throws errors accordingly before reaching the database layer.

This runtime protection for components through decorators ensures that only valid data shapes flow across layers, preventing obscure errors. Type safety is imposed without extra checks cluttering cleaner logic.

## Measure Memory Usage of a Function

When it comes to large dataset-intensive applications or resource-constrained environments, the Measure Memory Usage Decorator is a memory detective that offers insights into function memory consumption. It does this by optimising memory usage.

```python
import tracemalloc

def measure_memory_usage(target_function):
    def wrapper(*args, **kwargs):
        tracemalloc.start()

        # Call the original function
        result = target_function(*args, **kwargs)

        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics("lineno")

        # Print the top memory-consuming lines
        print(f"Memory usage of {target_function.__name__}:")
        for stat in top_stats[:5]:
            print(stat)

        # Return the result
        return result

    return wrapper

# Example usage
@measure_memory_usage
def calculate_factorial_recursive(number):
    if number == 0:
        return 1
    else:
        return number * calculate_factorial_recursive(number - 1)

# Call the decorated function
result_factorial = calculate_factorial_recursive(3)
print("Factorial:", result_factorial)
```

**Output:**

```javascript
Memory usage of calculate_factorial_recursive:
C:\\\\Program Files\\\\Sublime Text 3\\\\test.py:29: size=1552 B, count=6, average=259 B
C:\\\\Program Files\\\\Sublime Text 3\\\\test.py:8: size=896 B, count=3, average=299 B
C:\\\\Program Files\\\\Sublime Text 3\\\\test.py:10: size=416 B, count=1, average=416 B
Memory usage of calculate_factorial_recursive:
C:\\\\Program Files\\\\Sublime Text 3\\\\test.py:29: size=1552 B, count=6, average=259 B
C:\\\\Program Files\\\\Python310\\\\lib\\\\tracemalloc.py:226: size=880 B, count=3, average=293 B
C:\\\\Program Files\\\\Sublime Text 3\\\\test.py:8: size=832 B, count=2, average=416 B
C:\\\\Program Files\\\\Python310\\\\lib\\\\tracemalloc.py:173: size=800 B, count=2, average=400 B
C:\\\\Program Files\\\\Python310\\\\lib\\\\tracemalloc.py:505: size=592 B, count=2, average=296 B
Memory usage of calculate_factorial_recursive:
C:\\\\Program Files\\\\Sublime Text 3\\\\test.py:29: size=1440 B, count=4, average=360 B
C:\\\\Program Files\\\\Python310\\\\lib\\\\tracemalloc.py:535: size=1240 B, count=3, average=413 B
C:\\\\Program Files\\\\Python310\\\\lib\\\\tracemalloc.py:67: size=1216 B, count=19, average=64 B
C:\\\\Program Files\\\\Python310\\\\lib\\\\tracemalloc.py:193: size=1104 B, count=23, average=48 B
C:\\\\Program Files\\\\Python310\\\\lib\\\\tracemalloc.py:226: size=880 B, count=3, average=293 B
Memory usage of calculate_factorial_recursive:
C:\\\\Program Files\\\\Python310\\\\lib\\\\tracemalloc.py:558: size=1416 B, count=29, average=49 B
C:\\\\Program Files\\\\Python310\\\\lib\\\\tracemalloc.py:67: size=1408 B, count=22, average=64 B
C:\\\\Program Files\\\\Sublime Text 3\\\\test.py:29: size=1392 B, count=3, average=464 B
C:\\\\Program Files\\\\Python310\\\\lib\\\\tracemalloc.py:535: size=1240 B, count=3, average=413 B
C:\\\\Program Files\\\\Python310\\\\lib\\\\tracemalloc.py:226: size=832 B, count=2, average=416 B
Factorial: 6
```

This code showcases a decorator, `measure_memory_usage`, designed to measure the memory consumption of functions.

The decorator, when applied, initiates memory tracking before the original function is called. Once the function completes its execution, a memory snapshot is taken and the top 5 lines consuming the most memory are printed.

Illustrated through the example of `calculate_factorial_recursive()`, the decorator allows you to monitor memory usage without altering the function itself, offering valuable insights for optimization purposes.

In essence, it provides a straightforward means to assess and analyze the memory consumption of any function during its runtime.

### Usage and Applications

Memory measurement decorators like these are extremely valuable in application development for identifying and troubleshooting memory bloat or leak issues.

For example, consider a data streaming pipeline with critical ETL components like `transform_data()` that processes large volumes of information. Though the process seems fine during regular loads, high volume data like Black Friday sales could cause excessive memory usage and crashes.

Rather than manual debugging, decorating processors like @measure\_memory\_usage can reveal useful insights. It will print the top memory intensive lines during peak data flow without any code change.

You should aim to pinpoint specific stages eating up memory rapidly and address through better algorithms or optimization.

Such decorators help bake diagnostics perspectives across critical paths to recognize abnormal consumption trends early. Instead of delayed production issues, problems can be preemptively identified through profiling before release. They reduce debugging headaches and minimize runtime failures via easier instrumentation for memory tracking.

## Cache Function Results with Expiration Time

Specifically designed for outdated data, the Cache Function Results with Expiration Time Decorator is a tool that combines caching with a time-based expiration feature to make sure that cached data is regularly refreshed to prevent staleness and maintain relevance.

```python
import time

def cached_function_with_expiry(expiry_time):
    def decorator(original_function):
        cache = {}

        def wrapper(*args, **kwargs):
            key = (*args, *kwargs.items())

            if key in cache:
                cached_value, cached_timestamp = cache[key]

                if time.time() - cached_timestamp < expiry_time:
                    return f"[CACHED] - {cached_value}"

            result = original_function(*args, **kwargs)
            cache[key] = (result, time.time())

            return result

        return wrapper

    return decorator

# Example usage

@cached_function_with_expiry(expiry_time=5)  # Cache expiry time set to 5 seconds
def calculate_product(x, y):
    return f"PRODUCT - {x * y}"

# Call the decorated function multiple times
print(calculate_product(23, 5))  # Calculation is performed
print(calculate_product(23, 5))  # Result is retrieved from cache
time.sleep(5)
print(calculate_product(23, 5))  # Calculation is performed (cache expired)
```

**Output:**

```javascript
PRODUCT - 115
[CACHED] - PRODUCT - 115
PRODUCT - 115
```

This code showcases a caching decorator that has an automatic cache expiration time.

The function `cached_function_with_expiry()` generates a decorator that, when applied, utilizes a dictionary called `cache` to store function results and their corresponding timestamps. The `wrapper()` function checks if the result for the current arguments is in the cache. If present and within the expiry time, it returns the cached result – otherwise, it calls the function.

Illustrated using `calculate_product()`, the decorator initially calculates and caches the result. Subsequent calls retrieve the cached result until the expiry period, at which point the cache is refreshed through a recalculation.

In essence, this implementation prevents redundant calculations while automatically refreshing results after the specified expiry period.

### Usage and Applications

Automatic cache expiry decorators are very useful in application development for optimizing performance of data fetching modules.

For example, consider a travel website that calls backend API `get_flight_prices()` to show live prices to users. While caches reduce calls to expensive flight data sources, static caching leads to displaying stale prices.

Instead, you can use `@cached_function_with_expiry(60)` to auto-refresh every minute. Now, the first user call fetches live prices and caches them, while subsequent requests in a 60s window efficiently reuse the cached pricing. But caches automatically invalidate after the expiry period to guarantee fresh data.

This allows your to optimize flows without worrying about corner cases related to outdated representations. This decorator handles the situation reliably, keeping caches in sync with upstream changes through configurable refreshing. There's zero redundancy of recalculations, and you still get the best possible updated information to end users. Common caching patterns get packaged conveniently for reuse across codebase with customized expiry rules.

## Conclusion

Python decorators continue to see widespread usage in application development for cleanly inserting common cross-cutting concerns. Authentications, monitoring, and restrictions are some standard examples of use cases that use decorators in frameworks like Django and Flask.

The popularity of web APIs has also lead to common adoption of rate limiting and caching decorators for performance.

Decorators have actually been around since early Python releases. Guido van Rossum wrote about enhancement with decorators in a 1990 paper on Python. Later when function decorators syntax stabilized in Python 2.4 in 2004, it opened the doors for elegant solutions through oriented programming. From web to data science, they continue to empower abstraction and modularity across Python domains.

The examples in this handbook only scratch the surface of what custom tailored decorators can enable. Based on any specific objective like security, throttling user requests, transparent encryption, and so on, you can create innovative decorators to address your needs. Structuring logic processing pipelines using a composition of specialized single-responsibility decorators also encourages reuse over redundancy.

Understanding decorators not only improves development skills but unlocks ways to dictate program behaviour flexibly. I encourage you to assess common needs across your codebases that can be abstracted into standalone decorators. With some practice, it becomes easy to spot cross-cutting concerns and extend functions efficiently without breaking a sweat.

If you liked this lesson and would like to explore more insightful tech content, including Python, Django, and System Design reads, check out my [Blog](https://atharvashah.netlify.app). You can also view my projects with proof of work on [GitHub](https://github.com/HighnessAtharva) and connect with me on [LinkedIn](https://www.linkedin.com/in/atharva-shah-5873a2111/) for a chat.
