---
title: How non-integer values are stored in a float (and why it floats)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-28T15:53:47.000Z'
originalURL: https://freecodecamp.org/news/how-non-integer-values-are-stored-in-a-float-and-why-it-floats-902effacbfb9
coverImage: https://cdn-media-1.freecodecamp.org/images/0*sgfbQZhatWzdqD46
tags:
- name: coding
  slug: coding
- name: Computer Science
  slug: computer-science
- name: interview
  slug: interview
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'By Shukant Pal

  Did you ever think how computers work on floating-point numbers? I mean — where
  does the decimal point go? What if you’re asked in an interview?


  _Photo by [Unsplash](https://unsplash.com/@jplenio?utm_source=medium&utm_medium=referral"...'
---

By Shukant Pal

Did you ever think how computers work on floating-point numbers? I mean — where does the decimal point go? What if you’re asked in an interview?

![Image](https://cdn-media-1.freecodecamp.org/images/wO60yF7x15-i5BWPFtfyz-MkgKtoqrIVY5yf)
_Photo by [Unsplash](https://unsplash.com/@jplenio?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Johannes Plenio</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

The IEEE 754 floating-point standard defines how non-integer values are encoded in fixed-size types, like the C++ float and the JavaScript Number. It gives us five different formats — but no worries, all of them are based on the same concept. In the rest of this article, I’ll call the it the IEEE 754.

If you get overwhelmed while reading all the different tricks used in the IEEE 754 — don’t worry, I’ve given enough examples at the end to get everything settled in your head.

## Concept

Just as integers can be written in any “base”, non-integral values can also be written in any base.

5.1 = 1(2²) + 0(2¹) + 1(2⁰) + 1/2¹ = 1011.1

Similarly, we can write 3.25 = 11.01, 8.75 = 1000.11. The values after the “radix” point (it’s no longer a decimal point) are multiplied by negative powers of 2.

The IEEE 754 is based around this technique. To convert any value in the IEEE 754 format, we have to follow these steps:

1. Write the number in binary form, with the radix point.
2. Format it in scientific notation so that only one digit is placed before the radix point.
3. Encode the different components as directed by the IEEE format chosen.

For example, let us take the value 934893.109375:

1. 934893.109375 can be represented exactly (more about this later) in binary form as 11100100001111101101.000111.
2. Scientific form: 1.1100100001111101101000111 x 2^-19

NOTE: Some decimal values cannot be represented exactly in base 2, just as one-third cannot be written exactly in base 10. However, you could approximate 1/3rd to be .3333333333. Similarly, the value may be approximated in base 2 (rather than being exact). For example, 1.9 is approximated as 1.11100110011001100110011 in binary (notice the repeating 0011, that’s because 1.9 is rational and the exact value would be represented by repeating it infinitely).

## The Format

The IEEE 754 defines three components that are written into a 16/32/64 or more -bit value: a sign bit, the exponent, and the mantissa.

These components are written in the following order:

* **Sign bit**(s): The sign bit has a value of 0 for positive values and 1 for negative values.
* **Exponent**(e)**:** This is equal to the exponent we get in scientific form.
* **Mantissa**(m)**:** The mantissa, or the _significand_, is the coefficient written in scientific form, just without the radix point. So the mantissa of 3.25=11.01 would be 1101 or 13.

To get our value back from IEEE 754: _V = s_ x _(m^e)_

The widths of each format are fixed, and so are the widths of the mantissa and exponents. The _width of the mantissa defines the precision, while the width of the exponent defines the range of the value._

Now, the IEEE 754 also uses some tricks to encode actual numbers, which I’ve listed below in different headings:

* Exponent bias
* Leading bit convention
* Subnormal numbers
* ±Infinity and NaN
* ±Zero (and examples in ECMAScript)

## Exponent Bias

The exponent _e_ may be negative and to support negative numbers, IEEE 754 defines the _bias_. The bias is added to the exponent to get the actual encoded exponent. For example, the binary32 format provides 8 bits to the exponents, where the bias is be 2⁷-1=127 in the exponent field. So -1 would be encoded as -1+127=128 and a +5 exponent would be encoded as 5+127=132.

The bias is chosen such that the smallest exponent would be encoded as 1 and the highest exponent would be encoded as 2⁸ - 2 = 254 (in binary32). That explains why _emin_ is -126 and _emax_ is +127.

NOTE: You might have noticed that the values 0 and 2⁸ - 1 are left out. If the exponent is encoded as zero, then the number represented is either ±∞ or NaN. If the exponent’s bits are all ones (i.e., 2⁸ - 1 = 255), then the number represented is a special subnormal one (more on those later).

## Leading Bit Convention

The left-most digit of any number written in scientific notation is never zero (unless the number itself is exactly 0). If you ever find yourself stuck with a 0 at the left, you have to decrease your exponent. For example,

0.12 x 10² = 1.2 x 10¹

Since we’re working in base two and the leading digit cannot be zero: that means the leading digit must be — 1 and only 1. This fact is exploited by the IEEE 754 and the leading bit is excluded from the encoded mantissa.

## Subnormal Numbers

The IEEE 754 defines two types of numbers: normal and subnormal. Normal numbers are, in fact, normal — they can be represented in the _m_ x 2^e format, where e is _emin_ ≤ _e_ ≤ _emax_. However, if _e_ drops below _emin_ then IEEE 754 calls them subnormal.

Since the encoded _e_ cannot go below 0, the actual exponent for subnormal numbers is always -127. Exponents below can be represented by breaking the leading bit convention and adding 0s to the left of the mantissa. This causes a loss of precision for the mantissa (as leading zeros cause the right-most bits to fall off).

```
undefined
```

// emin = -126, width of mantissa = 24 bits// 1. NORMAL Number, V = 2^-126Encoded:  m = 00000000000000000000000, e = 1  
Actual:  m = 100000000000000000000000, e = -126V = 2^-126// 2. SUBNORMAL Number, V = 2^-127Encoded:  m = 10000000000000000000000, e = 0 (e must be 0)  
Actual:   m = 10000000000000000000000, e = -127The leading bit convention doesn't work in subnormal numbers, where e = 0. This means that the encoded mantissa is the actual mantissa. The power e (actual) is always -127.The mantissa's leading bit could be 0. See the example below.// 3. SUBNORMAL Number, V = 2^-129Encoded:  m = 00100000000000000000000, e = 0 (subnormal)  
Actual:  m =  00100000000000000000000, e = -127V = 0.0100000000000000000000 x 2^-127 = 0.25 * 2^-127 = 2^-129

```
// emin = -126, width of mantissa = 24 bits

// 1. NORMAL Number, V = 2^-126

Encoded:  m = 00000000000000000000000, e = 1
Actual:  m = 100000000000000000000000, e = -126

V = 2^-126

// 2. SUBNORMAL Number, V = 2^-127

Encoded:  m = 10000000000000000000000, e = 0 (e must be 0)
Actual:   m = 10000000000000000000000, e = -127

The leading bit convention doesn't work in subnormal numbers, where e = 0. This means that the encoded mantissa is the actual mantissa. The power e (actual) is always -127.

The mantissa's leading bit could be 0. See the example below.

// 3. SUBNORMAL Number, V = 2^-129

Encoded:  m = 00100000000000000000000, e = 0 (subnormal)
Actual:  m =  00100000000000000000000, e = -127

V = 0.0100000000000000000000 x 2^-127 = 0.25 * 2^-127 = 2^-129
```

## ±Infinity and NaN

The exponent had two special values: 0 and 2⁸-1 (where that 8 is actually the width of the exponent in binary32). The former one was for subnormal numbers, while the latter one is for “special” values. 2⁸-1 is also the value when all the bits of the exponent are ones.

* If the value of the mantissa is 0, then the number represented is positive or negative infinity. The sign is determined by the sign bit.
* The value of the mantissa is non-zero, then the number represented, as a matter of fact, is ‘not a number’ or NaN. There are two types of NaNs — signaling and quiet. The type is determined by the value of the mantissa, and this article doesn’t cover that. A signaling NaN is used to terminate any numeric operation while a quiet NaN allows the operation to continue. As per my experience, you’ll never need to distinguish b/w these NaNs. They’re probably useless for you.

## The ±Zero Case

It is surprising that there are two zeros in IEEE 754 — positive and negative. For you and me, they’re identical. Any operation with +0 will give the same result if -0 is used instead, or is that true? Nope, it isn’t.

1/∞ = 0, and also 1/-∞ = 0, then 1/(1/∞) = 1/0 = ∞ and 1/(1/-∞) = ∞. The sign isn’t preserved if we use only one positive zero in the equations above. This is solved by using ±0. 1/-∞ = -0, then 1/(1/-∞)=-∞.

Again, if only 0 is used: then 4/∞=0 and -4/∞=0. However using ±0 leads to: 4/∞=+0 and -4/∞=-0.

The IEEE 754 requires, however, that any comparison b/w +0 and -0 return a positive result. In other words, +0 == -0 is true.

Most languages would hide +0 and -0 from you, and you wouldn’t be able to distinguish directly (you could if you divided by zero and tested the result for ±∞). However, JavaScript is special and provides the `Object.is(arg1, arg2)` method which would distinguish b/w +0 and -0.

```
Object.is(+0, -0);// false
```

## Examples

I promised that I would clear your brain of all confusion with my examples.

```
// All examples use binary32 here
// 1. Encode 127872.12781278 in IEEE 754

Step 1: Write in binary notation

127872.12781278 = 11111001110000000.0010000 (24-bits)

Step 2: Write in scientific notation

1.11110011100000000010000 x 2^16

Step 3: Encode

m(encoded) = 11110011100000000010000 (23-bits only)
e(encoded) = 16+127 = 143 = 10001111

(sign)(e)(m) = 0 10001111 11110011100000000010000(32-bits)

// 2. Encode (-1.25 x 2^-130) in IEEE 754

Step 1: Write in binary notation (excluding sign here)

1.25x2^-130 = 1.01 x 2^-130 (shift by 130 right to remove scale)

Step 2: Already done!!!
Step 3: Encode

As e < emin, this is a subnormal number
e = -127
V = 1.01 x 2^-130 = 0.00101 x 2^-127
m = 0.0010100000000000000000 (23-bits only, no leading bit conv.)
sign = 1

(sign)(e)(m) = 1 00000000 00010100000000000000000 (32-bits)
```

## Finally, does it float?

The title promised to answer this question. It just had to.

The name “floating-point” comes from the fact that the radix point can be placed anywhere in a number. The floating-point types can encode any number with at most a given number of digits (the mantissa limits the precision), wherever the radix point be placed (other than the fact that there may be a little loss of precision).

This is opposed to fixed-point types where the representation fixes the digits represent-able to the left and right of the radix point.

The C++ type float also comes from the floating-point system.

## Additional Info: Decimal floating-point types

(NOTE: Decimal floating-point types are not in wide use. They are more important in commerce, due to the importance of precision in monetary values.)

In 2008, the IEEE 754 added two more formats: decimal32 and decimal64. In decimal formats, the mantissa is scaled by powers of 10 instead of 2. This preserves the decimal significant digits of our input and, most importantly, does not lose precision for numbers that can be represented exactly in base 10.

However, the mantissa is encoded in base 2 (the exponent is also encoded in base 2, just that the actual value is calculated by _V_ = _m_ x _10^e_). Since the mantissa is in base 2, you cannot write it in scientific notation:

```
102 = 1.02 x 10^2 = 1.000001010001111010111000 x 10^2
202 = 2.02 x 10^2 = 10.00000101000111101011100 x 10^2
```

For example, 202 has two digits (’10’) before the radix point while 101 has only one digit (‘1’) before the radix point. There is no integral power of 10 that can be used to represent 202 in binary scientific form (with only one digit before the radix point).

NOTE: This side effect is because the mantissa and the scale factor (10) are not in the same base.

To overcome this limitation, IEEE 754 encodes numbers where the mantissa is an integer.

```
1234.31212 = 123431212 x 10^-5 = 111010110110110100100101100 x 10^-5

// The mantissa will be 111010110110110100100101100
// The exponent will be -5.
```

The decimal formats define two ways of encoding the integer mantissa: binary integer (as shown in the example above) and densely packed decimal (DPD). The decimal formats also have special tricks, which are beyond the scope of this article. I will write about them in a separate story.

Further reading from Shukant Pal:

* [Full Overview of the HTML Canvas](https://medium.com/@sukantk3.4/full-overview-of-the-html-canvas-6354216fba8d)
* [Removing Circular Dependencies in JavaScript](https://medium.com/@sukantk3.4/circular-dependencies-in-javascript-34183fc2720) (my proposal)
* [How to synchronize your game app across multiple devices](https://medium.freecodecamp.org/how-to-synchronize-your-game-app-across-multiple-devices-88794d4c95a9) (Android)
* [How to use Firebase for building Android games](https://medium.freecodecamp.org/match-making-with-firebase-hashnode-de9161e2b6a7)

I’m Shukant Pal — the creator of the Silcos kernel. I know a lot about low-level C++ code and a little about the Linux kernel’s internal code structure. I love hardware level details here and there. Follow me on my social media profiles.

