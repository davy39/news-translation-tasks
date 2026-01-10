---
title: Java Array Methods – How to Print an Array in Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-20T22:19:03.000Z'
originalURL: https://freecodecamp.org/news/java-array-methods-how-to-print-an-array-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/Untitled-design--1-.png
tags:
- name: arrays
  slug: arrays
- name: Java
  slug: java
seo_title: null
seo_desc: "By Thanoshan MV\nAn array is a data structure used to store data of the\
  \ same type. Arrays store their elements in contiguous memory locations. \nIn Java,\
  \ arrays are objects. All methods of class object may be invoked in an array. We\
  \ can store a fixed n..."
---

By Thanoshan MV

An array is a data structure used to store data of the same type. Arrays store their elements in contiguous memory locations. 

In Java, arrays are objects. All methods of class object may be invoked in an array. We can store a fixed number of elements in an array.

Let’s declare a simple primitive type of array:

```java
int[] intArray = {2,5,46,12,34};
```

Now let’s try to print it with the `System.out.println()` method:

```java
System.out.println(intArray);
// output: [I@74a14482
```

Why did Java not print our array? What is happening under the hood?

The `System.out.println()` method converts the object we passed into a string by calling `String.valueOf()` . If we look at the `String.valueOf()` method’s implementation, we'll see this:

```java
public static String valueOf(Object obj) {
    return (obj == null) ? "null" : obj.toString();
}
```

If the passed-in object is `null` it returns null, else it calls `obj.toString()` . Eventually, `System.out.println()` calls `toString()` to print the output.

If that object’s class does not override `Object.toString()`'s implementation, it will call the `Object.toString()` method.

`Object.toString()` returns `getClass().getName()+**‘@’**`+Integer.toHexString(hashCode()) . In simple terms, it returns: “class name @ object’s hash code”.

In our previous output `[I@74a14482` , the `[` states that this is an array, and `I` stands for int (the type of the array). `74a14482` is the unsigned hexadecimal representation of the hash code of the array.

Whenever we are creating our own custom classes, it is a best practice to override the `Object.toString()` method.

We can not print arrays in Java using a plain `System.out.println()` method. Instead, these are the following ways we can print an array:

1. Loops: for loop and for-each loop 
2. `Arrays.toString()` method
3. `Arrays.deepToString()` method
4. `Arrays.asList()` method
5. Java Iterator interface
6. Java Stream API

Let’s see them one by one.

# 1. Loops: for loop and for-each loop

Here's an example of a for loop:

```java
int[] intArray = {2,5,46,12,34};

for(int i=0; i<intArray.length; i++){
    System.out.print(intArray[i]);
    // output: 25461234
}
```

All wrapper classes override `Object.toString()` and return a string representation of their value.

And here's a for-each loop:

```java
int[] intArray = {2,5,46,12,34};

for(int i: intArray){
    System.out.print(i);
    // output: 25461234
}
```

# 2. Arrays.toString() method

`Arrays.toString()` is a static method of the array class which belongs to the `java.util` package. It returns a string representation of the contents of the specified array. We can print one-dimensional arrays using this method. 

Array elements are converted to strings using the `String.valueOf()` method, like this:

```java
int[] intArray = {2,5,46,12,34};
System.out.println(Arrays.toString(intArray));
// output: [2, 5, 46, 12, 34]
```

For a reference type of array, we have to make sure that the reference type class overrides the `Object.toString()` method.

For example:

```java
public class Test {
    public static void main(String[] args) {
        Student[] students = {new Student("John"), new Student("Doe")};
        
        System.out.println(Arrays.toString(students));
        // output: [Student{name='John'}, Student{name='Doe'}]
    }
}

class Student {
    private String name;

    public Student(String name){
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "Student{" + "name='" + name + '\'' + '}';
    }
}
```

This method is not appropriate for multidimensional arrays. It converts multidimensional arrays to strings using `Object.toString()` which describes their identities rather than their contents.

For example:

```java
// creating multidimensional array
int[][] multiDimensionalArr = { {2,3}, {5,9} };

System.out.println(Arrays.toString(multiDimensionalArr));
// output: [[I@74a14482, [I@1540e19d]
```

With the help of `Arrays.deepToString()`, we can print multidimensional arrays.

# 3. Arrays.deepToString() method

`Arrays.deepToString()` returns a string representation of the “deep contents” of the specified array.

If an element is an array of primitive type, it is converted to a string by invoking the appropriate overloading of `Arrays.toString()` .

Here is an example of the primitive type of multidimensional array:

```java
// creating multidimensional array
int[][] multiDimensionalArr = { {2,3}, {5,9} };

System.out.println(Arrays.deepToString(multiDimensionalArr));
// output: [[2, 3], [5, 9]]
```

If an element is an array of reference type, it is converted to a string by invoking `Arrays.deepToString()` recursively.

```java
Teacher[][] teachers = 
{{ new Teacher("John"), new Teacher("David") }, {new Teacher("Mary")} };

System.out.println(Arrays.deepToString(teachers));
// output: 
[[Teacher{name='John'}, Teacher{name='David'}],[Teacher{name='Mary'}]]
```

We have to override `Object.toString()` in our Teacher class.

If you are curious as to how it does recursion, here is the [source code](http://hg.openjdk.java.net/jdk8u/jdk8u/jdk/file/be44bff34df4/src/share/classes/java/util/Arrays.java#l4611) for the `Arrays.deepToString()` method.

**NOTE:** Reference type one-dimensional arrays can also be printed using this method. For example:

```java
Integer[] oneDimensionalArr = {1,4,7};

System.out.println(Arrays.deepToString(oneDimensionalArr));
// output: [1, 4, 7]
```

# 4. Arrays.asList() method

This method returns a fixed-size list backed by the specified array.

```java
Integer[] intArray = {2,5,46,12,34};

System.out.println(Arrays.asList(intArray));
// output: [2, 5, 46, 12, 34]
```

We have changed the type to Integer from int, because List is a collection that holds a list of objects. When we are converting an array to a list it should be an array of reference type.

Java calls `Arrays._asList_`(intArray).toString() . This technique internally uses the `toString()` method of the type of the elements within the list.

Another example with our custom Teacher class:

```java
Teacher[] teacher = { new Teacher("John"), new Teacher("Mary") };

System.out.println(Arrays.asList(teacher));
// output: [Teacher{name='John'}, Teacher{name='Mary'}]
```

**NOTE:** We can not print multi-dimensional arrays using this method. For example:

```java
Teacher[][] teachers = 
{{ new Teacher("John"), new Teacher("David") }, { new Teacher("Mary") }};
        
System.out.println(Arrays.asList(teachers));

// output: [[Lcom.thano.article.printarray.Teacher;@1540e19d, [Lcom.thano.article.printarray.Teacher;@677327b6]
```

# 5. Java Iterator Interface

Similar to a for-each loop, we can use the Iterator interface to loop through array elements and print them.

Iterator object can be created by invoking the `iterator()` method on a Collection. That object will be used to iterate over that Collection’s elements.

Here is an example of how we can print an array using the Iterator interface:

```java
Integer[] intArray = {2,5,46,12,34};

// creating a List of Integer
List<Integer> list = Arrays.asList(intArray);

// creating an iterator of Integer List
Iterator<Integer> it = list.iterator();

// if List has elements to be iterated
while(it.hasNext()) {
    System.out.print(it.next());
    // output: 25461234
}
```

# 6. Java Stream API

The Stream API is used to process collections of objects. A stream is a sequence of objects. Streams don’t change the original data structure, they only provide the result as per the requested operations.

With the help of the `forEach()` terminal operation we can iterate through every element of the stream.

For example:

```java
Integer[] intArray = {2,5,46,12,34};

Arrays.stream(intArray).forEach(System.out::print);
// output: 25461234
```

Now we know how to print an array in Java.

Thank you for reading.

Cover image by [Aziz Acharki](https://unsplash.com/@acharki95?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText).

You can read my other articles on [Medium](https://medium.com/@mvthanoshan9/object-oriented-programming-principles-in-java-820919dced1a). 

**Happy Coding!**

