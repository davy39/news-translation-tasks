---
title: Spécificateurs de format en C
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
seo_title: Spécificateurs de format en C
seo_desc: 'Format specifiers define the type of data to be printed on standard output.
  You need to use format specifiers whether you''re printing formatted output with
  printf() or  accepting input with scanf().

  Some of the % specifiers that you can use in ANSI C...'
---

Les spécificateurs de format définissent le type de données à imprimer sur la sortie standard. Vous devez utiliser des spécificateurs de format que vous imprimiez une sortie formatée avec `printf()` ou que vous acceptiez une entrée avec `scanf()`.

Voici quelques spécificateurs % que vous pouvez utiliser en ANSI C :

| Spécificateur | Utilisé Pour           |
|---------------|------------------------|
| %c            | un seul caractère      |
| %s            | une chaîne de caractères|
| %hi           | short (signé)           |
| %hu           | short (non signé)      |
| %Lf           | long double            |
| %n            | n'imprime rien         |
| %d            | un entier décimal (base 10) |
| %i            | un entier décimal (détecte la base automatiquement) |
| %o            | un entier octal (base 8) |
| %x            | un entier hexadécimal (base 16) |
| %p            | une adresse (ou pointeur) |
| %f            | un nombre à virgule flottante pour les floats |
| %u            | int décimal non signé  |
| %e            | un nombre à virgule flottante en notation scientifique |
| %E            | un nombre à virgule flottante en notation scientifique |
| %%            | le symbole %           |

## Exemples :

### Spécificateur de format `%c` pour un seul caractère :

```c
#include <stdio.h> 

int main() { 
  char first_ch = 'f'; 
  printf("%c\n", first_ch); 
  return 0; 
} 
```

**Sortie :**

```
f
```

### Spécificateur de format `%s` pour une chaîne de caractères :

```c
#include <stdio.h> 

int main() { 
  char str[] = "freeCodeCamp"; 
  printf("%s\n", str); 
  return 0; 
} 
```

**Sortie :**

```
freeCodeCamp
```

### Entrée de caractère avec le spécificateur de format `%c` :

```c
#include <stdio.h> 

int main() { 
  char user_ch; 
  scanf("%c", &user_ch); // l'utilisateur entre Y
  printf("%c\n", user_ch); 
  return 0; 
} 
```

**Sortie :**

```
Y
```

### Entrée de chaîne avec le spécificateur de format `%s` :

```c
#include <stdio.h> 

int main() { 
  char user_str[20]; 
  scanf("%s", user_str); // l'utilisateur entre fCC
  printf("%s\n", user_str); 
  return 0; 
} 
```

**Sortie :**

```
fCC
```

### Spécificateurs de format d'entier décimal `%d` et `%i` :

```c
#include <stdio.h> 

int main() { 
  int found = 2015, curr = 2020; 
  printf("%d\n", found); 
  printf("%i\n", curr); 
  return 0; 
} 
```

**Sortie :**

```
2015
2020
```

### Spécificateurs de format de nombre à virgule flottante `%f` et `%e` :

```c
#include <stdio.h>

int main() { 
  float num = 19.99; 
  printf("%f\n", num); 
  printf("%e\n", num); 
  return 0; 
}
```

**Sortie :**

```
19.990000
1.999000e+01
```

### Spécificateur de format d'entier octal `%o` :

```
#include <stdio.h> 

int main() { 
  int num = 31; 
  printf("%o\n", num); 
  return 0; 
}
```

**Sortie :**

```
37
```

### Spécificateur de format d'entier hexadécimal `%x` :

```c
#include <stdio.h> 

int main() { 
  int c = 28; 
  printf("%x\n", c); 
  return 0; 
} 
```

**Sortie :**

```
1c
```