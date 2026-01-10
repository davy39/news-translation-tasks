---
title: La commande Cat sous Linux – La concaténation expliquée avec des exemples Bash
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-04T23:43:06.000Z'
originalURL: https://freecodecamp.org/news/the-cat-command-in-linux-concatenation-explained-with-bash-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b40740569d1a4ca2aaf.jpg
tags:
- name: Bash
  slug: bash
- name: Linux
  slug: linux
seo_title: La commande Cat sous Linux – La concaténation expliquée avec des exemples
  Bash
seo_desc: 'By Ryan reid

  Cat in Linux stands for concatenation (to merge things together) and is one of the
  most useful and versatile Linux commands. While not exactly as cute and cuddly as
  a real cat, the Linux cat command can be used to support a number of ope...'
---

Par Ryan reid

Cat sous Linux signifie concaténation (fusionner des éléments ensemble) et c'est l'une des commandes Linux les plus utiles et polyvalentes. Bien qu'elle ne soit pas aussi mignonne et câline qu'un vrai chat, la commande Linux `cat` peut être utilisée pour effectuer un certain nombre d'opérations utilisant des chaînes de caractères, des fichiers et des sorties.

La commande cat a trois objectifs principaux concernant les fichiers texte :

* Créer
* Lire/Afficher
* Mettre à jour/Modifier

Nous allons passer en revue chacun d'entre eux tour à tour pour montrer les commandes et les options associées à chaque opération.

## Premiers pas

Pour commencer, créons quelques fichiers appelés foo.txt et spam.txt.

Commençons par créer foo.txt avec la commande `cat > foo.txt` depuis la ligne de commande Linux.

**Avertissement : S'il existe déjà un fichier nommé foo.txt, la commande `cat` utilisant l'opérateur > l'écrasera.**

D'ici, l'invite affichera une nouvelle ligne qui nous permettra de saisir le texte que nous voulons. Pour cet exemple, nous utiliserons :

```
FILE 1
foo
bar
baz

```

Pour revenir à la ligne de commande et créer le fichier texte, nous utilisons CTRL + D.

Maintenant, créons spam.txt avec `cat > spam.txt` et insérons ce qui suit :

```
FILE 2
spam
ham
eggs

```

Si nous voulions ajouter ou annexer plus de texte à ces fichiers, nous utiliserions `cat >> FILENAME` et saisirions le texte que nous voulons utiliser.

**Notez que l'opérateur >> est utilisé pour l'ajout, contrairement à l'opérateur >.**

Au lieu de devoir ouvrir un éditeur de texte, nous avons pu créer un fichier texte simple et rapide depuis la ligne de commande, ce qui nous a fait gagner du temps et des efforts.

Le point essentiel à retenir de cette section est que nous utilisons `cat > FILENAME` pour créer ou écraser un fichier. De plus, nous pouvons utiliser `cat >> FILENAME` pour ajouter du contenu à un fichier déjà existant. Ensuite, après avoir tapé le texte souhaité, nous utilisons CTRL + D pour quitter l'éditeur, revenir à la ligne de commande et créer le fichier.

## Lecture et affichage

Maintenant que nous avons créé quelque chose, jetons un coup d'œil à ce que nous avons fait.

Remarquez que nous n'avons pas d'opérateur > ou >> dans la commande suivante, seulement cat et le nom du fichier.

La commande `cat foo.txt` affichera ce qui suit :

```
FILE 1
foo
bar
baz

```

Ainsi, `cat foo.txt` nous permettra de lire le fichier, mais voyons ce que nous pouvons faire d'autre.

Supposons que nous voulions savoir combien de lignes contient un fichier sur lequel nous travaillons. Pour cela, l'option -n est très pratique.

Avec la commande `cat -n foo.txt`, nous pouvons voir la longueur de notre fichier :

```
  1  FILE 1
  2  foo
  3  bar
  4  baz

```

Avec -n, nous pouvons avoir une idée du nombre de lignes du fichier avec lequel nous travaillons. Cela peut être utile lorsque nous itérons sur un fichier de longueur fixe.

## ConCATénation de fichiers

Ok, nous avons vu que cat peut créer et afficher des fichiers, mais qu'en est-il de la concaténation (combinaison) de ceux-ci ?

Pour cet exemple, nous utiliserons les fichiers foo.txt et spam.txt. Si nous voulons faire les choses bien, nous pouvons regarder le contenu des deux fichiers en même temps. Nous utiliserons à nouveau la commande cat, cette fois en utilisant `cat foo.txt spam.txt`.

`cat foo.txt spam.txt` donne le résultat suivant :

```
FILE 1
foo
bar
baz
FILE 2
spam
ham
eggs


```

Notez que ce qui précède ne fait qu'AFFICHER les deux fichiers. À ce stade, nous ne les avons pas encore concaténés dans un nouveau fichier.

Pour concaténer les fichiers dans un nouveau fichier, nous voulons utiliser `cat foo.txt spam.txt > fooSpam.txt`, ce qui nous donne le résultat dans un nouveau fichier fooSpam.txt.

L'utilisation de `cat fooSpam.txt` affiche ce qui suit dans le terminal :

```
FILE 1
foo
bar
baz
FILE 2
spam
ham
eggs

```

Cette commande est également utile lorsque nous voulons concaténer plus de deux fichiers dans un nouveau fichier.

Les points à retenir ici sont que nous pouvons visualiser plusieurs fichiers avec `cat FILENAME1 FILENAME 2`.

De plus, nous pouvons concaténer plusieurs fichiers en un seul avec la commande `cat FILENAME1 FILENAME 2 > FILENAME3`.

## Autres choses amusantes à faire avec Cat

Disons que nous travaillons avec un fichier et que nous obtenons sans cesse des erreurs pour une raison quelconque avant la fin du fichier – et il semble qu'il pourrait avoir plus de lignes que prévu.

Pour examiner le fichier d'un peu plus près et éventuellement résoudre notre problème, nous pouvons utiliser l'option -A. L'option -A nous montrera où les lignes se terminent par un $, elle nous montrera les caractères de tabulation avec un ^I, et elle affiche également d'autres caractères non imprimables.

Si nous regardions un exemple de fichier texte non imprimable avec `cat nonPrintExample.txt`, nous pourrions obtenir quelque chose comme ceci :

```




       






```

Ce qui est correct mais ne nous dit peut-être pas toute l'histoire d'un caractère ou d'une chaîne qui pourrait nous causer des problèmes.

Alors que `cat -A nonPrintExample.txt` pourrait nous donner une sortie plus utile :

```
^I^I$
$
^L$
$
^G^H^H^H^Y^I^N^O^P^@$
^@^@^[g^[f^[d^[g^[6^[5^[4^[6^[=$
$
$
^X$

```

Ici, nous obtenons une représentation plus claire de ce qui peut se passer entre les tabulations, les sauts de ligne, les retours chariot et d'autres caractères.

Le point à retenir ici est que `cat -A FILENAME` peut nous donner des détails plus approfondis sur le fichier avec lequel nous travaillons.

Cet article devrait vous avoir donné un bon aperçu de la commande cat, de ce qu'elle peut faire et de ses fonctionnalités.