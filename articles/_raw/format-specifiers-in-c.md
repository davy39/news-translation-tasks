---
title: Format Specifiers in C
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-22T21:32:00.000Z'
originalURL: https://freecodecamp.org/news/format-specifiers-in-c
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d9c740569d1a4ca38a4.jpg
tags:
- name: C
  slug: c-3
- name: General Programming
  slug: programming
- name: programming languages
  slug: programming-languages
seo_title: null
seo_desc: 'Format specifiers define the type of data to be printed on standard output.
  You need to use format specifiers whether you''re printing formatted output with
  printf() or  accepting input with scanf().

  Some of the % specifiers that you can use in ANSI C...'
---

Format specifiers define the type of data to be printed on standard output. You need to use format specifiers whether you're printing formatted output with `printf()` or  accepting input with `scanf()`.

Some of the % specifiers that you can use in ANSI C are as follows:

| Specifier | Used For           |
|-----------|--------------------|
| %c        | a single character |
| %s        | a string           |
| %hi       | short \(signed\)   |
| %hu       | short \(unsigned\) |
| %Lf       | long double        |
| %n	    | prints nothing     |
| %d	    | a decimal integer (assumes base 10) |
| %i	    | a decimal integer (detects the base automatically) |
| %o	    | an octal (base 8) integer |
| %x	    | a hexadecimal (base 16) integer |
| %p	    | an address (or pointer) |
| %f	    | a floating point number for floats |
| %u	    | int unsigned decimal |
| %e	    | a floating point number in scientific notation |
| %E	    | a floating point number in scientific notation |
| %%	    | the % symbol |

## Examples:

### `%c` single character format specifier:

```c
#include <stdio.h> 

int main() { 
  char first_ch = 'f'; 
  printf("%c\n", first_ch); 
  return 0; 
} 
```

**Output:**

```
f
```

### `%s` string format specifier:

```c
#include <stdio.h> 

int main() { 
  char str[] = "freeCodeCamp"; 
  printf("%s\n", str); 
  return 0; 
} 
```

**Output:**

```
freeCodeCamp
```

### Character input with the `%c` format specifier:

```c
#include <stdio.h> 

int main() { 
  char user_ch; 
  scanf("%c", &user_ch); // user inputs Y
  printf("%c\n", user_ch); 
  return 0; 
} 
```

**Output:**

```
Y
```

### String input with the `%s` format specifier:

```c
#include <stdio.h> 

int main() { 
  char user_str[20]; 
  scanf("%s", user_str); // user inputs fCC
  printf("%s\n", user_str); 
  return 0; 
} 
```

**Output:**

```
fCC
```

### `%d` and `%i` decimal integer format specifiers:

```c
#include <stdio.h> 

int main() { 
  int found = 2015, curr = 2020; 
  printf("%d\n", found); 
  printf("%i\n", curr); 
  return 0; 
} 
```

**Output:**

```
2015
2020
```

### `%f` and `%e` floating point number format specifiers:

```c
#include <stdio.h>

int main() { 
  float num = 19.99; 
  printf("%f\n", num); 
  printf("%e\n", num); 
  return 0; 
}
```

**Output:**

```
19.990000
1.999000e+01
```

### `%o` octal integer format specifier:

```
#include <stdio.h> 

int main() { 
  int num = 31; 
  printf("%o\n", num); 
  return 0; 
}
```

**Output:**

```
37
```

### `%x` hexadecimal integer format specifier:

```c
#include <stdio.h> 

int main() { 
  int c = 28; 
  printf("%x\n", c); 
  return 0; 
} 
```

**Output:**

```
1c
```


