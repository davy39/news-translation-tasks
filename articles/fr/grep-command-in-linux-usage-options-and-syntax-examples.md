---
title: Commande Grep sous Linux – Utilisation, Options et Exemples de Syntaxe
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2023-01-17T22:40:13.000Z'
originalURL: https://freecodecamp.org/news/grep-command-in-linux-usage-options-and-syntax-examples
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/Copy-of-Copy-of-Cast-a-Function-in-SQL
seo_title: Commande Grep sous Linux – Utilisation, Options et Exemples de Syntaxe
---

Convert-Char-to-Int-SQL-Server-Example.png
tags:
- name: Linux
  slug: linux
seo_title: null
seo_desc: "Grep est une commande utile pour rechercher des motifs correspondants dans un fichier. grep\n  \ est l'abréviation de \"global regular expression print\". \nSi vous êtes un administrateur système\n  \ qui doit parcourir des fichiers journaux ou un développeur essayant de trouver certaines occurrences\n  \ dans le fichier de code, alors grep est une commande puissante à utiliser."
---

`Grep` est une commande utile pour rechercher des motifs correspondants dans un fichier. `grep` est l'abréviation de "global regular expression print". 

Si vous êtes un administrateur système qui doit parcourir des fichiers journaux ou un développeur essayant de trouver certaines occurrences dans le fichier de code, alors `grep` est une commande puissante à utiliser.

Dans cet article, nous allons discuter de la syntaxe de la commande `grep` et de son utilisation avec quelques exemples.

## Syntaxe de la commande `grep`

La syntaxe de la commande `grep` est la suivante :

```bash
grep [OPTION...] MOTIFS [FICHIER...]
```

Dans la syntaxe ci-dessus, grep recherche les MOTIFS dans chaque FICHIER. `Grep` trouve chaque ligne qui correspond au MOTIF fourni. Il est bon de fermer le MOTIF entre guillemets lorsque `grep` est utilisé dans une commande shell.

Dans cet article, nous allons discuter des options suivantes qui peuvent être utilisées avec `grep` :

* `-i`, `--ignore-case` : Ignore les distinctions de casse dans les motifs et les données d'entrée.
* `-v`, `--invert-match` : Sélectionne les lignes non correspondantes du motif d'entrée fourni.
* `-n`, `--line-number` : Préfixe chaque ligne de la sortie correspondante avec le numéro de ligne dans le fichier d'entrée.
* `-w` : Trouve le mot correspondant exactement dans le fichier d'entrée ou la chaîne.
* `-c` : Compte le nombre d'occurrences du motif fourni.

Dans les exemples suivants, nous utiliserons le fichier `fruits.txt` avec le contenu suivant :

```
pommes et poires
agrumes – oranges, pamplemousses, mandarines et citrons verts
fruits à noyau – nectarines, abricots, pêches et prunes
fruits tropicaux et exotiques – bananes et mangues
baies – fraises, framboises, myrtilles, kiwis et fruits de la passion
melons – pastèques, melons et melons miel
tomates et avocats.
```

## Comment trouver une chaîne correspondante avec `grep`

Si nous voulons trouver la chaîne "fruit" dans le fichier `fruits.txt`, nous pouvons le faire comme suit :

```bash
grep "fruit" fruits.txt
```

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-73.png)

## Comment ignorer les distinctions de casse en utilisant `-i`

Nous pouvons demander à `grep` de retourner les résultats en ignorant la casse de la chaîne correspondante. Cherchons le mot "berries" dans notre fichier exemple. Il doit correspondre à toutes les occurrences de "berries" quelle que soit leur casse.

```bash
 grep -i "berries" fruits.txt
```

Résultat :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-74.png)

## Comment sélectionner les lignes non correspondantes en utilisant `-v`

Nous pouvons inverser les résultats de la commande `grep` pour inclure les résultats non correspondants. Par exemple, si nous voulons obtenir toutes les lignes qui ne contiennent pas le mot "berries", la commande serait la suivante :

```bash
grep -v "berries" fruits.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-75.png)

Le résultat a retourné toutes les lignes qui ne contiennent pas "berries".

## Comment trouver les numéros de ligne contre l'entrée correspondante en utilisant `-n`

Il arrive que nous voulions obtenir les numéros de ligne contre la chaîne correspondante. Pour cela, nous pouvons fournir le drapeau `-n` à `grep` comme suit :

```bash
 grep -n "berries" fruits.txt
```

Résultat :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-76.png)

D'après le résultat, nous pouvons voir que le mot "berries" apparaît à la ligne #5 du fichier.

## Comment trouver le mot correspondant exactement dans le fichier d'entrée ou la chaîne en utilisant `-w`

Si vous souhaitez correspondre à un mot exact plutôt qu'à une simple occurrence d'un motif, vous pouvez le faire en utilisant le drapeau `-w`.

Si nous utilisons `grep` "fruit" sans aucun drapeau, il retournerait toute occurrence du mot "fruit". Cela inclurait des occurrences comme "pamplemousse", "fruit du dragon" et ainsi de suite comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-77.png)

Mais, si nous voulons seulement "fruit" dans nos résultats, nous pouvons utiliser le drapeau `-w` comme suit :

```bash
 grep -w  "fruit" fruits.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-78.png)

Voyez-vous la différence ? Le dernier résultat a retourné une seule ligne où le mot exact "fruit" a été trouvé.

## Comment compter le nombre d'occurrences du motif fourni en utilisant `-c`

Nous pouvons compter le nombre de fois où la chaîne correspondante apparaît dans le fichier. Voici comment fonctionne le drapeau `-c` :

```bash
grep -c "fruit" fruits.txt
```

Résultat :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-79.png)

Le mot "fruit" apparaît 3 fois dans le fichier.

Astuce : Le drapeau `-c` peut être très utile si vous devez compter le nombre de fois qu'un message d'erreur est apparu dans un fichier journal.

## Comment analyser les fichiers pour une entrée correspondante

Jusqu'à présent, nous avons discuté de la manière de rechercher des motifs correspondants dans un fichier ou une chaîne d'entrée. Nous pouvons également utiliser `grep` pour réduire les fichiers qui contiennent un motif correspondant. Nous pouvons utiliser les drapeaux suivants pour séparer les fichiers qui contiennent le motif correspondant :

* `-l, --files-with-matches` : Affiche le nom du fichier qui contient le motif correspondant fourni.
* `-L, --files-without-match` : Affiche le nom du fichier qui ne contient pas le motif correspondant fourni.

Supposons que nous avons les fichiers suivants dans notre dossier :

```bash
zaira@Zaira:~/grep-tutorial$ ls -lrt
total 12
-rw-r--r-- 1 zaira zaira 327 Jan 16 19:25 fruits.txt
-rw-r--r-- 1 zaira zaira  47 Jan 16 20:31 vegetables.txt
-rw-r--r-- 1 zaira zaira 194 Jan 16 20:33 more-fruits.txt
```

Les fichiers ont le contenu suivant :

```
zaira@Zaira:~/grep-tutorial$ cat fruits.txt
apples and pears
citrus – oranges, grapefruits, mandarins and limes
stone fruit – nectarines, apricots, peaches and plums
tropical and exotic – bananas and mangoes
berries – strawBERRIES, raspberries, blueberries, kiwifruit and passionfruit
melons – watermelons, rockmelons and honeydew melons
tomatoes and avocados.
```

```bash
zaira@Zaira:~/grep-tutorial$ cat more-fruits.txt
passionfruit
dragon fruit
kiwis
pears
grapefruits, mandarins and limes
stone fruit – nectarines, apricots, peaches and plums
tropical and exotic – bananas and mangoes
tomatoes and avocados.
```

```bash
zaira@Zaira:~/grep-tutorial$ cat vegetables.txt
# Vegetables only

Cabbage
Onion
Carrot
Potato
```

Ensuite, nous voulons voir les fichiers qui contiennent le motif "fruit". Nous pouvons le faire comme suit :

```bash
 grep -l "fruit" *
```

Notez que le `*` recherche tous les fichiers dans le dossier.

Voici le résultat :

```bash
zaira@Zaira:~/grep-tutorial$  grep -l "fruit" *
fruits.txt
more-fruits.txt
```

Supposons que nous voulons lister les fichiers qui ne contiennent pas le mot "fruit". Nous pouvons le faire en utilisant la commande suivante :

```bash
 grep -L "fruit" *
```

Voici le résultat :

```bash
zaira@Zaira:~/grep-tutorial$  grep -L "fruit" *
vegetables.txt
```

## Conclusion

Si vous souhaitez étudier la commande `grep` en profondeur, consultez les pages de manuel. Vous pouvez obtenir des informations supplémentaires sur la ligne de commande avec `grep --help`.

J'espère que vous avez trouvé ce tutoriel utile !

Quelle est la chose préférée que vous avez apprise dans ce tutoriel ? Faites-le moi savoir sur [Twitter](https://twitter.com/hira_zaira) !

Vous pouvez lire mes autres articles [ici](https://www.freecodecamp.org/news/author/zaira/).

Crédits image :

[Image par upklyak](https://www.freepik.com/free-vector/electronic-documents-management-doodle-concept_29314820.htm#query=file%20search&position=7&from_view=search&track=sph) sur Freepik