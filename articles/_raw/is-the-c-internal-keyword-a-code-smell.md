---
title: Is the C# internal keyword a code smell?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-15T19:06:56.000Z'
originalURL: https://freecodecamp.org/news/is-the-c-internal-keyword-a-code-smell
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/0_agwE-xG4Q7OZDDgC-1.jpg
tags:
- name: best practices
  slug: best-practices
- name: C
  slug: c
- name: clean code
  slug: clean-code
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
seo_title: null
seo_desc: 'By shani fedida

  In this post, I am going to show why I think the internal keyword, when put on class
  members, is a code smell and suggest better alternatives.

  What is the internal keyword?

  In C# the internal keyword can be used on a class or its memb...'
---

By shani fedida

In this post, I am going to show why I think the internal keyword, when put on class members, is a code smell and suggest better alternatives.

### What is the internal keyword?

In C# the internal keyword can be used on a class or its members. It is one of the C# [access modifier](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/access-modifiers)s. Internal types or members are accessible **only within** **files in the same assembly**. ([C# internal keyword documentation](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/internal)).

### Why we need the internal keyword?

“A common use of internal access is in component-based development because it **enables a group of components to cooperate in a private manner without being exposed to the rest of the application code**. For example, a framework for building graphical user interfaces could provide Control and Form classes that cooperate by using members with internal access. Since these members are internal, they are not exposed to code that is using the framework.” ([C# internal keyword documentation](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/internal))

These are the use cases I saw for using the internal keyword on a class member:

* Call a class’s private function within the same assembly.
* In order to test a private function, you can mark it as internal and exposed the dll to the test DLL via [InternalsVisibleTo](https://docs.microsoft.com/en-us/dotnet/api/system.runtime.compilerservices.internalsvisibletoattribute?view=netframework-4.8).

Both cases can be viewed as a [code smell,](https://enterprisecraftsmanship.com/2017/10/23/unit-testing-private-methods/) saying that this private function should be public.

### Let's see some examples

Here is a simple example. a function in one class wants to access a private function of another class.

```c#
class A{
	public void func1(){
		func2();
	}
	private void func2(){}
}

class B{
	public void func(A a){
		a.func2(); //Compilation error 'A.func2()' is inaccessible due to its protection level
	}
}
```

The solution is simple — just mark A::func2 as public.

Let's look at a bit more complex example:

```c#
public class A{
	public void func1(){}
	private void func2(B b){}
}

internal class B{
	public void func3(A a){		
		a.func2(this); //Compilation error 'A.func2(B)' is inaccessible due to its protection level
	}
}
```

What’s the problem? just mark func2 as public as we did before.

```c#
public class A{
	public void func1(){ ... }
	public void func2(B b){ ...} // Compilation error: Inconsistent accessibility: parameter type 'B' is less accessible than method 'A.func2(B)' 
}

internal class B{
	public void func3(A a){		
		a.func2(this); 
	}
}
```

But we can’t ?. B is an internal class so it cannot be part of the signature of a public function of a public class.

Those are the solutions I found, ordered by easiness:

1. Mark the function with the internal keyword

```c#
public class A{
	public void func1(){ }
	internal void func2(B b){}
}

internal class B{
	public void func3(A a){		
		a.func2(this); 
	}
	
}
```

2. Create an internal interface

```c#
internal interface IA2{
	void func2(B b);
}

public class A:IA2{
	public void func1(){
		var b = new B();
		b.func3(this);
	}
	void IA2.func2(B b){} //implement IA2 explicitly because func2 can't be public
}

internal class B{
	public void func3(A a){ 
		((IA2)a).func2(this); //use interface instead of class to access func2	
	}
	
}
```

3. Extract A.func2 to another internal class and use it instead of A.func2.

```c#
internal class C{
	public void func2(B b){
	 //extract A:func2 to here
	}
}

public class A{
	public void func1(){}
	private void func2(B b){
		new C().func2(b); 
	}
}

internal class B{
	public void func3(){	//a is no longer needed	
		new C().func2(this); //use internal class instead of private function
	}
	
}
```

4. Decouple the function from internal classes and make it public. This is much dependant on what the function is doing with its inputs. decouple the internal classes can be very easy, very hard and even impossible (without ruing the design).

#### But we don’t have public classes we use interfaces…

Let's look at some more real-world example:

```c#
public interface IA{
	void func1();
}

internal class A : IA {
	public void func1(){}
	private void func2(B b){}
}

internal class B{
	public void func3(IA a){		
		a.func2(this);  //Compilation error IA' does not contain a definition for 'func2' and no extension method 'func2' accepting a first argument of type 'IA' could be found

	}	
}
```

Let's see how the previous solutions are adapted to this example:

1. Mark function with Internal. this means you will need to cast to class in order to call the function so _This will work only if class A is the only one that implements the interface_, meaning IA is not mocked in tests and there isn’t another production class that implements IA.

```c#
public interface IA{
	void func1();
}

internal class A : IA {
	public void func1(){}
	internal void func2(B b){}
}

internal class B{
	public void func3(IA a){		
		((A)a).func2(this); //cast to A in order to accses func2

	}	
}
```

2. Create an internal interface that extends the public interface.

```c#
internal interface IExtendedA : IA{
	void func2(B b);
}

public interface IA{
	void func1();
}

internal class A : IExtendedA {
	public void func1(){}
	public void func2(B b){}
}

internal class B{
	public void func3(IExtendedA a){		
		a.func2(this);

	}	
}
```

3. Extract A.func2 to another internal class and use it instead of A.func2.

4. Decouple the function from internal classes and add it to the public interface.

We can see that the **internal keyword is the easiest solution**, but there are other solutions using the **traditional building blocks of OOP: classes and interfaces**. We can see that the 2nd solution — adding an internal interface is not much harder than marking the function with the internal keyword.

### Why not use the internal keyword?

As I showed in the previous examples, using the **internal keyword is the easiest solution**. But you are going to have a hard time in the future if you will need to:

* Move the public class A to another DLL (since the internal keyword will no longer apply to the same dll)
* Create another production class that implements IA
* Mock IA in tests

You may think “But this is just one line of code, I or anyone else can change it easily if needed”. **Now** you have **one** line of code that looks like that:

```c#
((MyClass)a).internalFunction
```

but if others will need to call this function too this **line will be copy-pasted around** inside the DLL.

### My Conclusion

I think marking a class member with the internal keyword **is a code smell**. In the examples I showed above it is the **easiest** solution, BUT can cause problems in the future. Creating an **internal interface is almost as easy and more explicit.**

### Compare to C++

The C++ “friend” keyword is similar to the C# internal keyword. It allows a class or a function to access private members of a class. The difference is it allows access to **specific** class or function and **not** **all the classes in the same DLL.** In my opinion, this is a better solution than the C# internal keyword.

### Further Reading

[**Practical uses for the "internal" keyword in C#**](https://stackoverflow.com/questions/165719/practical-uses-for-the-internal-keyword-in-c-sharp)  
[**Why does C# not provide the C++ style 'friend' keyword?**](https://stackoverflow.com/questions/203616/why-does-c-sharp-not-provide-the-c-style-friend-keyword)

  

