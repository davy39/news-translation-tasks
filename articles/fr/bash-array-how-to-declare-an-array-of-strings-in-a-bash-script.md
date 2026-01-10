---
title: Tableaux Bash – Comment déclarer un tableau de chaînes dans un script Bash
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-09-09T14:50:00.000Z'
originalURL: https://freecodecamp.org/news/bash-array-how-to-declare-an-array-of-strings-in-a-bash-script
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/pexels-belle-co-1000445.jpg
tags:
- name: arrays
  slug: arrays
- name: Bash
  slug: bash
- name: command line
  slug: command-line
seo_title: Tableaux Bash – Comment déclarer un tableau de chaînes dans un script Bash
seo_desc: "By Veronica Stork\nBash scripts give you a convenient way to automate command\
  \ line tasks. \nWith Bash, you can do many of the same things you would do in other\
  \ scripting or programming languages. You can create and use variables, execute\
  \ loops, use con..."
---

Par Veronica Stork

Les scripts Bash vous offrent un moyen pratique d'automatiser les tâches en ligne de commande. 

Avec Bash, vous pouvez faire beaucoup des mêmes choses que dans d'autres langages de script ou de programmation. Vous pouvez créer et utiliser des variables, exécuter des boucles, utiliser la logique conditionnelle et stocker des données dans des tableaux. 

Bien que la fonctionnalité puisse être très familière, la syntaxe de Bash peut être délicate. Dans cet article, vous apprendrez comment déclarer des tableaux et comment les utiliser dans votre code.

## Comment déclarer un tableau en Bash

Déclarer un tableau en Bash est facile, mais faites attention à la syntaxe. Si vous avez l'habitude de programmer dans d'autres langages, le code peut sembler familier, mais il existe des différences subtiles faciles à manquer.

Pour déclarer votre tableau, suivez ces étapes :

1. Donnez un nom à votre tableau
2. Suivez ce nom de variable d'un signe égal. Le signe égal _ne doit pas_ avoir d'espaces autour
3. Encerclez le tableau de _parenthèses_ (pas de crochets comme en JavaScript)
4. Tapez vos chaînes en utilisant des guillemets, mais _sans virgules_ entre elles

Votre déclaration de tableau ressemblera à ceci : 

```sh
myArray=("cat" "dog" "mouse" "frog")
```

C'est tout ! C'est aussi simple que cela.

## Comment accéder à un tableau en Bash

Il existe plusieurs façons de parcourir votre tableau. Vous pouvez soit parcourir les éléments eux-mêmes, soit parcourir les indices.

### Comment parcourir les éléments d'un tableau

Pour parcourir les éléments du tableau, votre code devra ressembler à ceci : 

```sh
for str in ${myArray[@]}; do
  echo $str
done
```

Pour décomposer cela : cela ressemble quelque peu à l'utilisation de `forEach` en JavaScript. Pour chaque chaîne (str) dans le tableau (myArray), imprimez cette chaîne. 

La sortie de cette boucle ressemble à ceci :

```
cat
dog
mouse
frog
```

**Note** : Le symbole `@` dans les crochets indique que vous parcourez _tous_ les éléments du tableau. Si vous omettiez cela et écriviez simplement `for str in ${myArray}`, seule la première chaîne du tableau serait imprimée. 

### Comment parcourir les indices d'un tableau

Alternativement, vous pouvez parcourir les indices du tableau. Cela ressemble à une boucle `for` en JavaScript, et est utile lorsque vous souhaitez pouvoir accéder à l'index de chaque élément. 

Pour utiliser cette méthode, votre code devra ressembler à ce qui suit :

```sh
for i in ${!myArray[@]}; do
  echo "element $i is ${myArray[$i]}"
done
```

La sortie ressemblera à ceci :

```
element 0 is cat
element 1 is dog
element 2 is mouse
element 3 is frog
```

**Note** : Le point d'exclamation au début de la variable `myArray` indique que vous accédez aux _indices_ du tableau et non aux éléments eux-mêmes. Cela peut être déroutant si vous avez l'habitude que le point d'exclamation indique la négation, alors faites attention à cela. 

**Autre note** : Bash ne nécessite généralement pas d'accolades pour les variables, mais il en a besoin pour les tableaux. Vous remarquerez donc que lorsque vous référencez un tableau, vous le faites avec la syntaxe `${myArray}`, mais lorsque vous référencez une chaîne ou un nombre, vous utilisez simplement un signe dollar : `$i`.

## Conclusion

Les scripts Bash sont utiles pour créer un comportement automatisé en ligne de commande, et les tableaux sont un excellent outil que vous pouvez utiliser pour stocker plusieurs morceaux de données. 

Les déclarer et les utiliser n'est pas difficile, mais c'est différent des autres langages, alors faites attention pour éviter les erreurs.