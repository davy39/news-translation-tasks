---
title: Functional Programming in Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-14T17:34:55.000Z'
originalURL: https://freecodecamp.org/news/functional-programming-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/lambda.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: Java
  slug: java
seo_title: null
seo_desc: "By Sameer Shukla\nFunctional programming (FP) is a programming paradigm.\
  \ It emphasizes the use of pure functions that don't have side effects and always\
  \ return the same output for a given input. \nThis article explores how to implement\
  \ FP concepts in J..."
---

By Sameer Shukla

Functional programming (FP) is a programming paradigm. It emphasizes the use of pure functions that don't have side effects and always return the same output for a given input. 

This article explores how to implement FP concepts in Java, including viewing functions as first-class citizens, chaining, and composing them to create function pipelines.

We'll also discuss the technique of currying, which allows a function that takes multiple arguments to be transformed into a chain of functions that each take a single argument. This can simplify the use of complex functions and make them more reusable. 

In this article, I'll show you examples of how to implement these concepts in Java using modern language features, like “java.util.function.Function”, “java.util.function.BiFunction”, and a user-defined TriFunction. We'll then see how to overcome its limitation using currying. 

## The `java.util.function.Function` interface

The java.util.function.Function interface is a key component of the Java 8 functional programming API. The java.util.function.Function is a functional interface in Java that takes input of type 'T' and produces an output of type 'R'. 

In functional programming, functions are first-class citizens, meaning that they can be passed around as values, stored in variables or data structures, and used as arguments or return values of other functions. 

The function interface provides a way to define and manipulate functions in Java code.

The function interface represents a function that takes one input and produces one output. It has a single abstract method, `apply()`, which takes an argument of a specified type and returns a result of a specified type. 

You can use the function interface to define new functions, as well as to manipulate and compose existing functions. For example, you can use it to convert a list of objects of one type to a list of objects of another type, or to apply a series of transformations to a stream of data.

One of the main benefits of the function interface is that it allows you to write code that is more concise and expressive. By defining functions as values and passing them around as arguments or return values, developers can create more modular and reusable code. Also, by using lambdas to define functions, Java code can be more expressive and easier to read.

You can think about `java.util.function.Function` like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-98.png)
_Function&lt;A, B&gt;_

The java.util.function.BiFunction is also a functional interface in Java that takes two inputs 'T' and 'U' and produces an output of type 'R'. In short, BiFunction takes 2 inputs and returns an output:

```
BiFunction<Integer, Integer, Integer> sum = (a, b) -> a + b;
```

 You can think about `java.util.function.BiFunction` like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-99.png)
_BiFunction&lt;A, B, C&gt;_

## Function Composition and Chaining 

Function chaining is a technique in functional programming that involves composing multiple functions into a single pipeline or chain. 

In Java FP, function chaining is often used to transform data in a series of steps, where each step applies a specific transformation to the data and passes it on to the next step in the chain.

The function interface in Java provides a powerful tool for function chaining. Each function in the chain is defined as a separate instance of the Function interface. The output of each function becomes the input to the next function in the chain. This allows for a series of transformations to be applied to the data, one after another, until the final result is produced.

### How to use the `andThen` method

The "andThen()" method is a default method provided by the function interface in Java. This method takes a sequence of two functions and applies them in succession, using the output of the first function as the input to the second function. This chaining of the functions results in a new function that combines the behavior of both functions in a single transformation. 

The syntax of `andThen` looks like this:

```java
default <V> Function<T, V> andThen(Function<? super R, ? extends V> after) 
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-107.png)
_andThen_

We can break the example down into series of steps. Initially the "multiply" function will be executed and its output passed as input to the "add" function. Then the "logOutput" function is used to log the resulting output. 

```java
public class FunctionChainingExample {

    static Logger logger = Logger.getLogger(FunctionChainingExample.class.getName());

    private static Function<Integer, Integer> multiply = x -> x * 2;

    private static Function<Integer, Integer> add = x -> x + 2;

    private static Function<Integer, Unit> logOutput = x -> {
        logger.info("Data:" + x);
        return Unit.unit();
    };

    public static Unit execute(Integer input) {
        Function<Integer, Unit> pipeline = multiply
                                               .andThen(add)
                                               .andThen(logOutput);
        return pipeline.apply(input);
    }

    public static void main(String[] args) {
        execute(10);
    }

}
```

The the above code snippet showcases the creation of three functions, namely multiply, add, and logOutput. 

The function `multiply` accepts an integer input and produces an integer output, just like the `add` function. But, the `logOutput` function accepts an integer input and returns nothing (as represented by the Unit object, which implies the absence of a value). 

The `execute` function chains the three functions together, where the output of multiply is utilized as the input for the add function, and the resulting output of add is passed to the logOutput function for logging purposes. The above example showcases function chaining using the `andThen` default method. 

### How to use the `compose` method

Unlike the `andThen` method, the `compose` method is another default method provided by the function interface in Java. It applies the first function to the output of the second function. 

This means that the second function is applied to the input first, and then the first function is applied to the output of the second function. As a result, a chain of functions is created where the output of the second function becomes the input of the first function. 

The compose function looks like this:

```java
default  Function<V, R> compose(Function<? super V, ? extends T> before)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-118.png)
_compose_

When to use `andThen` vs `compose` depends on the order in which you want the functions to be applied.

If you want to apply the functions in the order they are defined, from left to right, then you should use the `andThen` method. This method applies the first function to the input, and then applies the second function to the output of the first function. 

This is useful when you want to chain together functions that process the input data in a specific order.

On the other hand, if you want to apply the functions in the opposite order, from right to left, then you should use the `compose` method. This method applies the second function to the input, and then applies the first function to the output of the second function. 

This is useful when you want to chain together functions that need to be applied in the opposite order of the way they are defined.

In general, you should use `andThen` when you want to apply the functions in the order they are defined, and use `compose` when you want to apply the functions in the opposite order. But the choice between the two methods ultimately depends on the specific requirements of your use case.

```
 public static Unit compose(Integer input) {
        Function<Integer, Unit> pipeline = logOutput
                                            .compose(add)
                                            .compose(multiply);
        return pipeline.apply(input);
    }
```

In the `compose` example, the functions are executed in a right-to-left order. Firstly, `multiply` is executed and its output is passed to the `add` function. Then, the resulting output of the `add` function is passed to `logOutput` for logging purposes.

### How to use the `apply()` function 

The `apply()` method takes an input and returns a result. It is used to apply a function to an argument and compute a result.

The `apply()` function is a method of functional interfaces, such as the function interface, that takes an argument of a specified type and returns a result of a specified type. It is the single abstract method of these interfaces, which is required for them to be used as functional interfaces.

The `apply()` function defines the behavior of the functional interface. When an instance of a functional interface is created, the `apply()` function is implemented to define what the functional interface does when it is called with an argument.

```
Function<Integer, Integer> multiply = x -> x * x;
        int result = multiply.apply(5);
```

In this code, we define a function called `multiply` that takes an integer argument and returns the square of that integer. We then call the `apply()` function on this function, passing in the integer value of 5. The `apply()` function executes the lambda expression defined in the `square` Function, and returns the result of the computation, which in this case is 25.

Let's understand by looking at a real-world example, FileReaderPipeline.

```
public class FileReaderPipeline {

    static Function<String, String> trim = String::trim;
    static Function<String, String> toUpperCase = String::toUpperCase;
    static Function<String, String> replaceSpecialCharacters = 
    	str -> str.replaceAll("[^\\p{Alpha}]+", "");

    static Function<String, String> pipeline = 
                                trim
                                  .andThen(toUpperCase)
                                  .andThen(replaceSpecialCharacters);

 public static void main(String[] args) throws IOException {
        try (BufferedReader reader = new BufferedReader(new 	FileReader("example.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String result = pipeline.apply(line);
                System.out.println(result);
            }
        }
    }
}
```

The above code defines a FileReaderPipeline class, which reads lines from a file, processes them through a pipeline of functions, and prints the resulting output.

First, three functions `trim`, `toUpperCase`, and `replaceSpecialCharacters` are defined using method references and lambda expressions. `trim` removes leading and trailing whitespace from a String, `toUpperCase` converts the string to uppercase, and `replaceSpecialCharacters` removes any non-alphabetic characters from the string.

Next, a function pipeline is created using the `andThen` method, which chains the three functions together. The input to the pipeline function is a String, and the output is also a String. When a String is passed to the pipeline function, it first removes any leading or trailing whitespace, then converts the string to uppercase, and finally removes any non-alphabetic characters.

Finally, in the `main` method, the program reads lines from a file (in this example, "example.txt") using a `BufferedReader`. Each line is processed through the pipeline function using the `apply` method, which applies each function in the pipeline in sequence, and returns the resulting output. The resulting output is then printed to the console using `System.out.println`.

## Function Currying

The Java util package contains two functional interfaces known as "Function<A, B>" and "BiFunction<A, B, C>". The `Function` interface takes a single input and produces an output, whereas the `BiFunction` interface takes two inputs and produces an output. Here is an illustration:

```
 Function<String, String> toUpper = str -> str.toUpperCase();
 BiFunction<Integer, Integer, Integer> sum = (a, b) -> a + b;
```

This is a clear constraint as there are only two functions, with one accepting a single input and the other accepting two inputs. Consequently, if we need a function that takes three inputs, we must construct our own customized function. 

To this end, let's design a function that accepts three inputs and name it `TriFunction`. Here is an example implementation:

```
@FunctionalInterface
public interface TriFunction<A, B, C, O> {
    O apply(A a, B b, C c);

    default <R> TriFunction<A, B, C, O> andThen(TriFunction<A, B, C, O> after) {
        return (A a, B b, C c) -> after.apply(a,b,c);
    }
}
```

```
TriFunction<Integer, Integer, Integer, Integer> sum = (a, b, c) -> a + b + c;																
int result = sum.apply(1, 2, 3);
```

In situations where we require more parameters than what the available functions can accept, we can leverage currying to overcome this limitation. 

We can refactor the previous function using currying, which involves decomposing a function that takes multiple arguments into a sequence of functions, each of which accepts only one argument. This is in line with the definition of currying, which is a technique employed in Functional Programming.

```
Function<Integer, Function<Integer, Function<Integer, Integer>>> 	sumWithThreeParams = (a) -> (b) -> (c) -> a + b + c;
                                                                       Function<Integer, Function<Integer, Function<Integer, Function<Integer, Integer>>>> sumWithFourParams = (a)->(b)->(c)->(d) -> a + b + c + d; 
                                                                                                                    
                                                                                                                 
                                                                                                                         
```

The above declares a new `Function` named `sumWithThreeParams` that takes an `Integer` input. It returns a new `Function` that takes an `Integer` input and returns yet another new `Function` that takes an `Integer` input and returns an `Integer` output. Similarly a new Function named `sumWithFourParams` is created. 

Note that the curried function `sumWithThreeParams` and `sumWithFourParams` allows us to partially apply arguments to the function, which can be useful in situations where we have some of the inputs available but not all of them

```
Function<Integer, Function<Integer, Integer>> partialSumWithTwoParams 									= sumWithThreeParams.apply(5);
                                                                        Function<Integer, Integer> partialSumWithOneParams 
								 = partialSumWithTwoParams.apply(10);

                                                                        int c = 15;
int result = partialSumWithOneParams.apply(c);
System.out.println(result); //30
```

## Conclusion

In this article, we covered the implementation of functional programming (FP) concepts in Java, such as treating functions as first-class citizens, composing them into pipelines, and utilizing currying to simplify complex functions. 

We have provided examples using modern language features like `java.util.function.Function` and `java.util.function.BiFunction`, as well as a user-defined `TriFunction` with currying to overcome its limitations. 

By applying these techniques, developers can write more concise, reusable, and maintainable code in Java. 

With the growing popularity of FP in the industry, understanding and implementing these concepts is becoming increasingly important for Java developers. 

After reading this article, if you have found it useful and would like to explore more practical examples, [please visit the repository](https://github.com/sameershukla/JavaFPLearning) and consider giving it a star.

