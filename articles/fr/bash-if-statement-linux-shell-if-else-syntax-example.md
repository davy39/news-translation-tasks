---
title: Instruction If Bash – Exemple de syntaxe If-Else du shell Linux
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-11-14T15:37:54.000Z'
originalURL: https://freecodecamp.org/news/bash-if-statement-linux-shell-if-else-syntax-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/Copy-of-Copy-of-read-write-files-python--4-.png
tags:
- name: Bash
  slug: bash
- name: Linux
  slug: linux
seo_title: Instruction If Bash – Exemple de syntaxe If-Else du shell Linux
seo_desc: 'When coding, you might need to make decisions based on certain conditions.
  Conditions are expressions that evaluate to a boolean expression (true or false).

  Statements that help to execute different code branches based on certain conditions
  are known...'
---

Lors de la programmation, vous pourriez avoir besoin de prendre des décisions basées sur certaines conditions. Les conditions sont des expressions qui évaluent une expression booléenne (`true` ou `false`).

Les instructions qui aident à exécuter différentes branches de code basées sur certaines conditions sont connues sous le nom d'instructions conditionnelles.

`if...else` est l'une des instructions conditionnelles les plus couramment utilisées. Comme d'autres langages de programmation, le scripting Bash supporte également les instructions `if...else`. Et nous allons les étudier en détail dans cet article de blog.

## Syntaxe des instructions `if`

Vous pouvez utiliser les instructions `if` de diverses manières. La structure générique des instructions `if` est la suivante :

* Utilisation d'une instruction `if` uniquement : `if...then...fi`
* Utilisation d'un `if` avec une instruction `else` : `if...then...else...fi`
* Utilisation de plusieurs instructions `else` avec `if` : `if..elif..else..fi`

## Comment utiliser l'instruction `if`

Lorsque vous utilisez une seule instruction `if`, la syntaxe est la suivante :

```bash
if [ condition ]
then
	instruction
fi
```

> Notez que les espaces font partie de la syntaxe et ne doivent pas être supprimés.

Passons en revue un exemple où nous comparons deux nombres pour voir si le premier nombre est le plus petit.

```bash
#! /bin/sh

a=5
b=30

if [ $a -lt $b ]
then
        echo "a est inférieur à b"
fi
```

Si vous exécutez l'extrait ci-dessus, la condition `if [ $a -lt $b ]` évalue à `True`, et l'instruction à l'intérieur de l'instruction if s'exécute.

**Sortie :**

```bash
a est inférieur à b
```

## Comment utiliser l'instruction `if .. else`

Lorsque vous utilisez une instruction `if` et que vous souhaitez ajouter une autre condition, la syntaxe est la suivante :

```bash
if [ condition ]
then
	instruction
else
	faire ceci par défaut
fi
```

Voyons un exemple où nous voulons savoir si le premier nombre est supérieur ou inférieur au second. Ici, `if [ $a -lt $b ]` évalue à faux, ce qui fait que la partie `else` du code s'exécute.

```bash
#! /bin/sh

a=99
b=45

if [ $a -lt $b ]
then
        echo "a est inférieur à b"
else
        echo "a est supérieur à b"
fi
```

**Sortie :**

```bash
a est supérieur à b
```

## Comment utiliser les instructions `if..elif..else`

Supposons que vous souhaitiez ajouter d'autres conditions et comparaisons pour rendre le code dynamique. Dans ce cas, la syntaxe ressemblerait à ceci :

```bash
if [ condition ]
then
	instruction
elif [ condition ] 
then
	instruction 
else
	faire ceci par défaut
fi
```

Pour créer des comparaisons significatives, nous pouvons également utiliser AND `-a` et OR `-o`.

Dans cet exemple, nous allons déterminer le type de triangle en utilisant ces conditions :

* `Scalène` : Un triangle où chaque côté est de longueur différente.
* `Isocèle` : Un triangle où 2 côtés sont égaux.
* `Équilatéral` : Un triangle où tous les côtés sont égaux.

```bash
read a
read b
read c

if [ $a == $b -a $b == $c -a $a == $c ]
then
echo EQUILATERAL

elif [ $a == $b -o $b == $c -o $a == $c ]
then
echo ISOSCELES
else
echo SCALENE

fi
```

Dans l'exemple ci-dessus, le script demanderait à l'utilisateur de saisir les trois côtés du triangle. Ensuite, il comparerait les côtés et déterminerait le type de triangle.

```
3
4
5
SCALENE
```

## Conclusion

Vous pouvez facilement diviser votre code en branches basées sur des conditions comme `if..else` et rendre le code plus dynamique. Dans ce tutoriel, vous avez appris la syntaxe de `if...else` ainsi que quelques exemples.

J'espère que vous avez trouvé ce tutoriel utile.

Quelle est la chose préférée que vous avez apprise dans ce tutoriel ? Faites-le moi savoir sur [Twitter](https://twitter.com/hira_zaira) !

Vous pouvez lire mes autres articles [ici](https://www.freecodecamp.org/news/author/zaira/).