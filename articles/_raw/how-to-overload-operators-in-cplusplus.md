---
title: How to Overload Operators in C++
subtitle: ''
author: Abhilekh gautam
co_authors: []
series: null
date: '2021-03-15T13:52:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-overload-operators-in-cplusplus
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6043a406a7946308b76830ab.jpg
tags:
- name: C++
  slug: c-2
- name: General Programming
  slug: programming
seo_title: null
seo_desc: "Classes are user-defined types. They allow us to represent the meaning\
  \ of various entities. Defining an operator for a class gives us a better way to\
  \ deal with objects. \nSo how can we define operators for our classes, and how should\
  \ we use such opera..."
---

[Classes](https://www.freecodecamp.org/news/how-classes-work-in-cplusplus/) are user-defined types. They allow us to represent the meaning of various entities. Defining an operator for a class gives us a better way to deal with objects. 

So how can we define operators for our classes, and how should we use such operators? I will show you how in this article.

Let's begin!

## What are Operators in C++?

Operators are symbols which are used to perform operations on various operands. For example:

```c++
int x = 5;
int y = 10;

int z = x + y;
```

For the above example `+` is an operator which performs the addition operation on the two operands `x` and `y`.

## What is Operator Overloading in C++?

Let's check out an example first.

```c++
int x=5;
int y= 10;

int z = x+y;//z==15

string s1="Abhi";
string s2="gautam";

string s3= s1+s3;//s3==Abhigautam

```

Have you ever wondered about this type of code **–** why is `z== 15` and `s3== Abhigautam`? This is because operators have different meanings for different types of operands. 

For an integer type, the `+` operator gives the sum of two numbers, and for the string type it concatinates (joins) them.

So, operator overloading is all about giving new meaning to an operator. But:

<ul>
    <li>You cannot set new meaning to an operator for a built-in type.</li>
    <li>You cannot create new operators.</li>
</ul>

So, basically what I mean is you cannot redefine an operator and you can't create a new operator, either.

If you wished to create new operator like `**` for exponential purposes, you couldn't do it.

### How does overloading work?

So operator overloading lets us define the meaning of an existing operator (note that you cannot overload some operators) for the operands of a user defined type (for example, a class is a user defined type).

Overloaded operators are just functions (but of a special type) with a special keyword `operator` followed by the symbol of the operator to be overloaded.

```c++
/*overloading + for class type object*/

return_type operator+(params..){}
```

As I already mentioned, overloaded operators are just a special type of functions. They must have a return type, and parameters are always optional (as per their requirements).

So let's overload some operators for our class now to see how it works:

```c++
class Complex{
int real,imag;
public:
Complex(int re,int im):real(re),imag(im){}
Complex(){
real = 0;
imag = 0;
}
void display() const;
//overloading operators
Complex operator+(const Complex);
Complex operator-(const Complex);
};
```

Here we have two functions as a member function with the syntax mentioned above. So first let's understand the syntax.

```
Complex operator+(const Complex);
Complex operator-(const Complex);
```

Both of the functions here return an object of `Complex` type. The operator keyword followed by the operators symbol tells us which operator is being overloaded.

We also have a display function to allow us to see the display of the object's member values. We will substituted this with the overloaded operator (`<<`) later in the post.

```c++
void Complex::display(){
if(imag<0)
cout<<real<<imag<<"i"<<'\n';
else
cout<<real<<'+'<<imag<<"i"<<'\n';
}
```

## How to Overload the Binary Plus (+) Operator in C++

Let's overload the `+` operator now.

```c++
Complex Complex::operator+(const Complex c1){
Complex temp;
temp.real = real + c1.real;
temp.imag = imag + c1.imag;
return temp;
}
```

After this definition, if we do the following:

```
Complex c1(2,2);
Complex c2(2,2);
Complex c3 = c1+c2;
c3.display();
```

It should be clear that c1+c2 is equivalent to this:

```c++
c1.operator+(c2);


```

and

```c++
operator(c1,c2);
```

After the call to the member function display, the output looks like this:

```
4+4i
```

So basically we defined the meaning of the `+` operator for our object of type `Complex`.

## How to Overload the Binary Minus (-) Operator in C++

Now let's overload the minus operator.

```c++
Complex Complex::operator-(const Complex c1){
Complex temp;
temp.real = real - c1.real;
temp.imag = imag - c1.imag;
return temp;
}
```

So this is how we overload operators in c++. Let's now discuss the number of parameters that should be passed in the function.

The number of parameters passed to the function is equal to the number of operands taken by the operator. 

But in case of a (non-static) member function, the number of parameters reduces by one. This is because the (non-static) member function somehow knows the object it was invoked for.

Isn't that fun? Let's now overload more operators for our class.

```c++
bool operator!=(const Complex);
bool operator==(const Complex);
```

## How to Overload the Not Equal To (!=) Operator in C++

So our function definition for the `!=` operator function will be this:

```c++
bool Complex::operator!=(const Complex c1){
if(real!=c1.real || real!=c1.imag){
    return true;
}
else
return false;
}
```

The return type is a bool, so it returns either true or false.

## How to Overload the Equal To (==) Operator in C++

Similarly for the operator `==`: 

```c++
bool Complex::operator==(const Complex c1){
  if(real == c1.real && imag == c1.imag){
    return true;
  }
  else
  return false;
}
```

### How to Overload the Get From (<<) Operator in C++

So let's now overload the `<<` operator. It will be fun!

Let's see the function declaration first:

```c++
friend ostream& operator<<(ostream&,Complex);

```

There are few changes from the previous functions. Let's understand it more clearly.

The function is a friend function. This means that it is not within the scope of any class and cannot be invoked by an object. Also the function returns a reference to the ostream object and it takes two arguments as parameters:

<ul>
    <li>Reference to an ostream object.</li>
    <li>Reference to an object of class type.</li>
 <ul/>

You might be wondering why a friend function? Let's talk about why we need friend functions now.

If an operator function is a (non-static) member function, then the left hand side operand will be bound to the **`this`** pointer that refers to the object which is calling the function.

But we don't want it to be here in the case of the `<<` operator because the left hand side operand for the `<<` operator should be `cout`. And `cout` is an object of ostream. So to avoid the binding with the object, we used a friend function here.

We can define the `<<` operator like this for our class.

```c++
ostream& operator<<(ostream& os,Complex c1){
if(c1.imag<0)
os<<c1.real<<c1.imag<<"i";
else
os<<c1.real<<"+"<<c1.imag<<"i";

return os;
}
```

So in this way we can overload most of the operators for our class.

## Some Operators Can't Be Overloaded in C++

We cannot overload the following operators in c++:

<ul>
    <li>:: (scope resolution operator)</li>
    <li>. (dot operator)</li>
    <li>.* (member selection through pointer)</li>
</ul>

> They take a name, rather than a value, as their second operand and provide a primary means of referring to members. Allowing them to be overloaded would lead to subtleties. [Stroustroup, 1994]

Moreover the ternary operator (?:) and the named operators **sizeof** and **typeid** also cannot be overloaded.

### Errors to Keep in Mind

Also remember that the following declaration is an error:

```c++
int operator+(int,int);
/*error : cannot redefine operators for built in type.*/
```

As mentioned earlier, Redefining an operator for built in type is an error.

### One last point

You should not overload operators like `&&` and `||` . This is because these operators have a particular order in which an operand is evaluated. Since overloaded operators are just function calls, we cannot guarantee the order of evaluation of the operands.

## That's it!

Happy Coding!

You can read my other blogs [here.](https://abhilekhblogs.blogspot.com/)

