---
title: Optional Types in Swift – How to Use and Unwrap Optionals
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-06T16:06:35.000Z'
originalURL: https://freecodecamp.org/news/optional-types-in-swift
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/maxwell-nelson-taiuG8CPKAQ-unsplash.jpg
tags:
- name: Swift
  slug: swift
- name: Swift Programming
  slug: swift-programming
seo_title: null
seo_desc: 'By Prajwal Kulkarni

  If you''re coming from Java, C++, or other object-oriented languages, chances are
  that you''ve never come across optional types or "optionals". And you might be quite
  surprised to know that such a concept exists in Swift.

  Optionals ...'
---

By Prajwal Kulkarni

If you're coming from Java, C++, or other object-oriented languages, chances are that you've never come across optional types or "optionals". And you might be quite surprised to know that such a concept exists in Swift.

Optionals are a fundamental topic that you need to thoroughly understand to code in Swift. If you're just getting started with Swift and you're learning about optional types for the first time, make sure to read this article until the end.

To understand what optional types are, let's quickly brush up on **constants** and **variables.**

## Constants and Variables in Swift

A constant is a data item whose value, once assigned, cannot be mutated (modified or changed) throughout the scope of the program. 

On the other hand, a variable is a data item whose value can be changed limitlessly. 

There are some nuances in how declare constants and variables in Swift. Let's look at that syntax:

`<data-item-type> <var-name>:<data-type> = <value>`

**Here's an example of a constant:**

`let pi:Double = 3.1415`

**And here's an example of a variable:**

```swift
var message:String = "Hello, this is prajwal"
message = "Coding in swift is awesome" //variable value changed.
```

Notice that of the keywords we've used here for declaring constants and variables, you use **let** to declare a constant, and **var** to declare a variable.

The keyword is then followed by the constant/variable name, a colon and its data type, and then the assigning value.

Swift is a type-safety language, which means that you can assign variables and constants values without specifying the data type. It can make appropriate assumptions based on the assigned value, for example:

`let const:String = "String"`

can also be written as,

`let const = "String"`

And,

`var speed:Int = 20`

can be written as,

`var speed = 35`

You might be wondering, if you can omit the data type then what's the need to specify it anyway? Well, you're right to wonder that – but you need to specify the data type once you're working with optional types, which are different from conventional data types.

## Optional types or Optionals in Swift

Coming to the main point, what are optional types in Swift?

Let's see what the [docs](https://docs.swift.org/swift-book/LanguageGuide/TheBasics.html) have to say about it:

> You use optionals in situations where a value may be absent. An optional represents two possibilities: Either there is a value, and you can unwrap the optional to access that value, or there isn’t a value at all.

That's a pretty straightforward definition. So optionals are basically used to handle null values at compile-time to ensure that no crashes occur at runtime.

Any operations on the optional variable are performed only if it contains non-null values.

An optional type can be of any data type, like a String, Integer, Double, Float, or any user defined non-primitive data type (object). 

But, it is important to note that the Optional data type is not equivalent to its base data type. For instance, an Optional String is not the same as a string, an Optional integer is not the same as an integer, and so forth. This is because primitive data types cannot handle `nil` values, but Optional types can. 

## Optional Types Syntax and Usage in Swift

Here's the syntax for an optional type:

`<data-item> <var-name>:<data-type>?`

The declaration is similar to declaring regular variables, except that you add a question mark (?) beside the data type which makes it an Optional type.

Fire up your XCode playground and try running these snippets:

```
let someVal:Double?
someVal = 5.6324

print(someVal)
//Output : Optional(someVal)

var str:String? = nil

str = "Hello, World!"
print(str)
//Output : Optional("Hello, World!")
```

You can see that the outputs are not regular values. Instead, they're optional values.

## How to Unwrap Optional Types in Swift

You won't use optional types upfront for any operations or tasks, as they should be cast in their primitives or user-defined instances before using it elsewhere (an optional string should be cast to a string, an optional integer should be cast to an integer, and so on). 

This casting is what's known as **unwrapping.** You can better understand this concept by thinking about Schrödinger's cat. 

In this thought experiment, a cat is placed in a closed box along with a vial of poison. Unless you open the box, you can't assure whether the cat is dead or alive ( nil or non-nil). This means that it is both dead and alive at the same time (nil and non-nil) according to your perception.

Only when you open the box (unwrapping) can you learn if the cat is alive or not (nil or not). 

Unwrapping in Swift is essentially verifying if the Optional value is nil or not, and then it performs a task only if it's not nil.

You can perform unwrapping in the following ways:

<ol type=1>
    <li>Using an if else block</li>
    <li>Using Forced unwrapping</li>
    <li>Using Optional binding</li>
    <li>Using Optional chaining</li>
    <li>Using a nil coalescing operator</li>
</ol>

### Unwrap an optional type with an if-else block

Unwrapping means to make sure that the Optional value is not nil. You can do this by using a simple if-else block like this:

```swift
var variable:String? //evaluates to nil

if variable != nil{
 print("Not nil")
}
else{
 print("Nil")
}
//Output : Nil
```

### Unwrap an optional type with forced unwrapping

Forced unwrapping is quite contradictory because you're accessing the optional value regardless of its value (nil or not nil). If a nil optional is unwrapped, an error is thrown saying "**Unexpectedly found nil while unwrapping an Optional value**." 

You're supposed to use forced unwrapping only in a pre-defined environment where you're certain that the optional value won't be nil.

You can forcefully unwrap an optional using the exclamatory(!) operator like this:

```swift
var color:String?;

print(color!) // Unexpectedly found nil while unwrapping an Optional value

color = "Black";

print(color!) // Black
```

### Unwrap an optional type with optional binding

Optional binding is similar to using an if-else block. The only subtle difference is that if the optional value is not nil, the unwrapped value is assigned to a new constant and further operations are performed on the constant. 

You can do this using the **if-let** statement:

```swift
var password:String? = "$tr0ngp@$$w0rd"

if let unwrappedpass = password {
	print("Password is \(unwrappedpass)") //Password is $tr0ngp@$$w0rd
}
```

An optional string `password` is assigned the value `$tr0ngp@$$w0rd`. Then in the if-let block, the optional value `password` is unwrapped and assigned to the variable `unwrappedpass` only if the optional value `password` is not nil. `unwrappedpass` now contains the unwrapped value and can be used within the block's scope.

```swift
var password:String?

if let unwrap = password{ // Block unexecuted, as optional password is nil.
	print("value is not nil")
}
```

### Unwrap an optional type with optional chaining

You use optional chaining in places where you're dealing with multiple optional values at once. You use it to access and mutate or assign far-fetched attributes whose value depends on other constraints.

For example, we get our food from plants, which in turn get their food from sunlight and water.

This means that there is a chained dependency of events – we are dependent on plants for our food, and plants themselves are dependent on water and light for their food.

Optional chaining involves verifying at each dependency if the instance is nil or not.

Let's see how this works with a code example:

```swift
class ShipmentCar{
    var seats:Int?
    var quality:String?
    
    init(seatQty:Int){
        seats = seatQty
    }

    func displaySeatQuality(){
        if let seatQuality = quality{
            print("The seat covering is made of:\(seatQuality)")
        }
    }

    

}

class CheckSeats{
    var seatExists:ShipmentCar?

}


var obj = ShipmentCar(seatQty:4)
var obj2:CheckSeats?
obj2 = CheckSeats()
obj2?.seatExists = obj
obj2?.seatExists?.quality = "Leather" //Optional chaining, set leather quality of seats, only if seats exist.
obj.displaySeatQuality()
//Output: The seat covering is made of: Leather
```

In the above example, we have two classes, `ShipmentCar` which is cargo, and `CheckSeats` to check if there are any seats in the vehicle.

We first create an instance of the class `ShipmentCar` and pass the argument as 4 for the number of seats – meaning that there are 4 seats in the vehicle. 

Further, we create an optional instance of the class `CheckSeats` and instantiate it. The attribute `seatExists` of the class `CheckSeats` is of the type optional `ShipmentCar`. 

Next, we perform optional chaining on the instance `obj2`, which we write as `obj2?.seatExists?.quality = "Leather"`. This means that we check if seats exist in the car, and if the seats exist, we define the quality of the seat cover which is `Leather`. Then we verify by calling the `displaySeatQuality` and get the desired result.

**Here's a small caveat**: in the above example, if you set the value of `seatQty` as 0 instead of 4, it'd still output the same result. This implies that the seat covers are made of leather even though there are 0 seats, which would make no sense. 

So, I'd like to mention that this is just an example and the main objective here is to emphasize that the attributes are assigned values only if the dependent attributes are not-nil.

### Unwrap an optional type with the nil coalescing operator

The nil coalescing operator works as shorthand notation for the regular if-else block. If a nil value is found when an optional value is unwrapped, an additional default value is supplied which will be used instead.

```
var text:String?

var output = text ?? "Default value"

print(output) // Default value

text = "This is a string"

output = text ?? "Default String"

print(output) // This is a string
```

You can also write default values in terms of objects.

## Wrapping up

There you have it! In this article, you've learned all about optional types and how to use them.

I'd like to thank you for reading this far and I hope this article has helped you understand optional types in Swift.

If you've any queries, feel free to contact me on [Twitter](https://twitter.com/prajwalinbizz) and/or [LinkedIn](https://www.linkedin.com/in/prajwal-kulkarni). I'll be happy to help you. Cheers!

