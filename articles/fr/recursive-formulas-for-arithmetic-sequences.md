---
title: Formules récursives pour les suites arithmétiques
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-28T00:12:00.000Z'
originalURL: https://freecodecamp.org/news/recursive-formulas-for-arithmetic-sequences
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/joe-yates-YsdtnFJEIKA-unsplash.jpg
tags:
- name: Math
  slug: math
- name: Recursion
  slug: recursion
- name: toothbrush
  slug: toothbrush
seo_title: Formules récursives pour les suites arithmétiques
seo_desc: 'What is an Arithmetic Sequence?

  A sequence is list of numbers where the same operation(s) is done to one number
  in order to get the next. Arithmetic sequences specifically refer to sequences constructed
  by adding or subtracting a value – called the c...'
---

### **Qu'est-ce qu'une suite arithmétique ?**

Une **suite** est une liste de nombres où la ou les mêmes opérations sont effectuées sur un nombre pour obtenir le suivant. Les **suites arithmétiques** font spécifiquement référence aux suites construites en ajoutant ou en soustrayant une valeur – appelée **différence commune** – pour obtenir le terme suivant. 

Afin de parler efficacement d'une suite, nous utilisons une formule qui construit la suite lorsqu'une liste d'indices est insérée. Typiquement, ces formules sont données avec des noms à une lettre, suivis d'un paramètre entre parenthèses, et l'expression qui construit la suite du côté droit.

`a(n) = n + 1`

Ci-dessus se trouve un exemple de formule pour une suite arithmétique.

### **Exemples**

Suite : 1, 2, 3, 4, … | Formule : a(n) = n + 13 

Suite : 8, 13, 18, … | Formule : b(n) = 5n - 2

### **Une formule récursive**

Remarque : Les mathématiciens commencent à compter à partir de 1, donc par convention, `n=1` est le premier terme. Nous devons donc définir quel est le premier terme. Ensuite, nous devons déterminer et inclure la différence commune. 

En regardant à nouveau les exemples,

Suite : 1, 2, 3, 4, … | Formule : a(n) = n + 1 | Formule récursive : a(n) = a(n-1) + 1, a(1) = 1

Suite : 3, 8, 13, 18, … | Formule : b(n) = 5n - 2 | Formule récursive : b(n) = b(n-1) + 5, b(1) = 3

### **Trouver la formule (étant donné une suite avec le premier terme)**

```text
1. Déterminer la différence commune
    Choisissez un terme dans la suite et soustrayez le terme qui le précède.         
2. Construire la formule
    La formule a la forme : `a(n) = a(n-1) + [différence commune], a(1) = [premier terme]`
```

### **Trouver la formule (étant donné une suite sans le premier terme)**

```text
1. Déterminer la différence commune
    Choisissez un terme dans la suite et soustrayez le terme qui le précède. 
2. Trouver le premier terme
    i. Choisissez un terme dans la suite, appelez-le `k` et appelez son indice `h`
    ii. premier terme = k - (h-1)*(différence commune)
3. Construire la formule
    La formule a la forme : `a(n) = a(n-1) + [différence commune], a(1) = [premier terme]` 
```

#### **Plus d'informations :**

Pour plus d'informations sur ce sujet, visitez

* [Wikipedia](https://en.wikipedia.org/wiki/Arithmetic_progression)