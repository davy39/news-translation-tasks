---
title: Opérateurs Java – &, && (ET) || (OU) Opérateurs Logiques
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-02-08T18:38:13.000Z'
originalURL: https://freecodecamp.org/news/java-operator-and-or-logical-operators
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/logic.jpg
tags:
- name: Java
  slug: java
seo_title: Opérateurs Java – &, && (ET) || (OU) Opérateurs Logiques
seo_desc: "We use operators in most programming languages to perform operations on\
  \ variables. \nThey are divided into various categories like arithmetic operators,\
  \ assignment operators, comparison operators, logical operators, and so on. \nIn\
  \ this article, we wil..."
---

Nous utilisons des opérateurs dans la plupart des langages de programmation pour effectuer des opérations sur des variables. 

Ils sont divisés en diverses catégories comme les opérateurs arithmétiques, les opérateurs d'affectation, les opérateurs de comparaison, les opérateurs logiques, et ainsi de suite. 

Dans cet article, nous allons parler de l'opérateur bitwise **ET**, et des opérateurs logiques **ET** (`&&`) et **OU** (`||`). 

## Comment utiliser l'opérateur bitwise `ET`

Le symbole `&` désigne l'opérateur bitwise **ET**. Il évalue la valeur binaire des nombres donnés. Le résultat binaire de ces nombres nous sera retourné en base 10. 

Lorsque l'opérateur `&` commence son opération, il évaluera la valeur des caractères dans les deux nombres en commençant par la gauche.

Regardons un exemple pour mieux comprendre :

```java
System.out.println(10 & 12);
// retourne 8
```

Décomposons cela.

La valeur binaire de 10 est 1010

La valeur binaire de 12 est 1100

Voici quelque chose que vous devez avoir à l'esprit avant de commencer l'opération :

* 1 et 0 => 0
* 0 et 1 => 0
* 1 et 1 => 1
* 0 et 0 => 0

Alors, effectuons l'opération.

Le premier caractère pour 10 est 1 et le premier caractère pour 12 est également 1 donc :

1 et 1 = 1.

Passons aux deuxièmes caractères – 0 pour 10 et 1 pour 12 :

1 et 0 = 0.

Pour les troisièmes caractères – 1 pour 10 et 0 pour 12 :

1 et 0 = 0.

Pour les quatrièmes caractères – 0 pour 10 et 0 pour 12 :

0 et 0 = 0.

Maintenant, combinons tous les caractères retournés. Nous aurions 1000.

La valeur binaire 1000 en base 10 est 8 et c'est pourquoi notre opération a retourné 8.

## Comment utiliser l'opérateur logique `ET`

Notez que nous utilisons des opérateurs logiques pour évaluer des conditions. Ils retournent soit `true` soit `false` en fonction des conditions données.

Le symbole `&&` désigne l'opérateur **ET**. Il évalue deux déclarations/conditions et retourne vrai uniquement lorsque les deux déclarations/conditions sont vraies.

Voici à quoi ressemble la syntaxe :

```txt
déclaration1/condition1 && déclaration2/condition2
```

Comme vous pouvez le voir ci-dessus, il y a deux déclarations/conditions séparées par l'opérateur. L'opérateur évalue la valeur des deux déclarations/conditions et nous donne un résultat – vrai ou faux.

Voici un exemple :

```java
System.out.println((10 > 2) && (8 > 4));
// vrai
```

L'opération retournera `true` parce que les deux conditions sont vraies – 10 est supérieur à 2 **et** 8 est supérieur à 4. Si l'une des conditions avait une logique fausse, alors nous obtiendrions `false`.

Pour mieux comprendre l'opérateur `&&`, vous devez savoir que les deux conditions doivent être vraies pour obtenir une valeur de `true`. 

Voici un autre exemple qui retourne `false` :

```java
System.out.println((2 > 10) && (8 > 4));
// false
```

Ici, 2 n'est pas supérieur à 10 mais 8 est supérieur à 4 – donc nous obtenons un `false` retourné. Cela est dû au fait que l'une des conditions n'est pas vraie.

* Si les deux conditions sont vraies => `true`
* Si l'une des deux conditions est fausse => `false`
* Si les deux conditions sont fausses => `false`

## Comment utiliser l'opérateur logique `OU`

Nous utilisons le symbole `||` pour désigner l'opérateur **OU**. Cet opérateur ne retournera `false` que lorsque les deux conditions sont fausses. Cela signifie que si les deux conditions sont vraies, nous obtiendrons `true` retourné, et si l'une des deux conditions est vraie, nous obtiendrons également une valeur de `true` retournée.

Voici la syntaxe :

```txt
déclaration1/condition1 || déclaration2/condition2
```

Passons en revue quelques exemples.

```
System.out.println((6 < 1) || (4 > 2));  
// vrai
```

Cela retourne `true` parce qu'une des conditions est vraie.

* Si les deux conditions sont vraies => `true`
* Si l'une des conditions est vraie => `true`
* Si les deux conditions sont fausses => `false`

## Conclusion

Dans cet article, nous avons appris comment utiliser l'opérateur bitwise `&` en Java et comment l'opération est effectuée pour nous donner un résultat. 

Nous avons également appris comment utiliser les opérateurs logiques **`&&`** et **`||`** en Java. Nous avons appris quelle valeur chaque opération retourne en fonction des conditions impliquées dans l'opération. 

Bon codage !