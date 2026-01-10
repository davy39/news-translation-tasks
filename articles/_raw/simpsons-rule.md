---
title: 'Simpson''s Rule: the Formula and How it Works'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-27T22:16:00.000Z'
originalURL: https://freecodecamp.org/news/simpsons-rule
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d62740569d1a4ca3781.jpg
tags:
- name: Math
  slug: math
seo_title: null
seo_desc: 'Simpson''s rule is a method for numerical integration. In other words,
  it''s the numerical approximation of definite integrals.

  Simpson''s rule is as follows:


  In it,


  f(x) is called the integrand

  a = lower limit of integration

  b = upper limit of integr...'
---

Simpson's rule is a method for numerical integration. In other words, it's the numerical approximation of definite integrals.

Simpson's rule is as follows:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/sim1.png)

In it,

* `f(x)` is called the _integrand_
* `a` = lower limit of integration
* `b` = upper limit of integration

## Simpson's 1/3 Rule

![Image](https://www.freecodecamp.org/news/content/images/2020/02/sim01.jpg)

As shown in the diagram above, the integrand `f(x)` is approximated by a second order polynomial; the quadratic interpolant being `P(x)`.

The approximation follows,

![Image](https://www.freecodecamp.org/news/content/images/2020/02/sim3.png)

Replacing `(b-a)/2` as `h`, we get,

![Image](https://www.freecodecamp.org/news/content/images/2020/02/sim4.png)

As you can see, there is a factor of `1/3` in the above expression. That’s why, it is called **Simpson’s 1/3 Rule**.

If a function is highly oscillatory or lacks derivatives at certain points, then the above rule may fail to produce accurate results. 

A common way to handle this is by using the _composite Simpson's rule_ approach. To do this, break up `[a,b]` into small subintervals, then apply Simpson's rule to each subinterval. Then, sum the results of each calculation to produce an approximation over the entire integral. 

If the interval `[a,b]` is split up into `n` subintervals, and `n` is an even number, the composite Simpson's rule is calculated with the following formula:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/sim7.png)

where **x<sub>j</sub> = a+jh** for **j = 0,1,…,n-1,n** with **h=(b-a)/n** ; in particular, **x<sub>0</sub> = a** and **x<sub>n</sub> = b**.

### Example in C++:

To approximate the value of the integral given below where n = 8:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/sim9.png)

```c++
#include<iostream>
#include<cmath>
using namespace std;

float f(float x)
{
	return x*sin(x);	//Define the function f(x)
}

float simpson(float a, float b, int n)
{
	float h, x[n+1], sum = 0;
	int j;
	h = (b-a)/n;
	
	x[0] = a;
	
	for(j=1; j<=n; j++)
	{
		x[j] = a + h*j;
	}
	
	for(j=1; j<=n/2; j++)
	{
		sum += f(x[2*j - 2]) + 4*f(x[2*j - 1]) + f(x[2*j]);
	}
	
	return sum*h/3;
}

int main()
{
	float a,b,n;
	a = 1;		//Enter lower limit a
	b = 4;		//Enter upper limit b
	n = 8;		//Enter step-length n
	if (n%2 == 0)
		cout<<simpson(a,b,n)<<endl;
	else
		cout<<"n should be an even number";
	return 0;
}
```

## Simpson's 3/8 Rule

Simpson's 3/8 rule is similar to Simpson's 1/3 rule, the only difference being that, for the 3/8 rule, the interpolant is a cubic polynomial. Though the 3/8 rule uses one more function value, it is about twice as accurate as the 1/3 rule.

Simpson’s 3/8 rule states :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/sim6.png)

Replacing `(b-a)/3` as `h`, we get,

![Image](https://www.freecodecamp.org/news/content/images/2020/02/sim5.png)

Simpson’s 3/8 rule for n intervals (n should be a multiple of 3):

![Image](https://www.freecodecamp.org/news/content/images/2020/02/sim8.png)

where **x<sub>j</sub> = a+jh** for **j = 0,1,…,n-1,n** with **h=(b-a)/n**; in particular, **x<sub>0</sub> = a** and **x<sub>n</sub> = b**.

