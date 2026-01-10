---
title: La commande Linux AWK – Exemples de syntaxe d'utilisation sous Linux et Unix
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-10-12T15:34:47.000Z'
originalURL: https://freecodecamp.org/news/the-linux-awk-command-linux-and-unix-usage-syntax-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/florian-klauer-mk7D-4UCfmg-unsplash.jpg
tags:
- name: Linux
  slug: linux
- name: unix
  slug: unix
seo_title: La commande Linux AWK – Exemples de syntaxe d'utilisation sous Linux et
  Unix
seo_desc: 'In this beginner-friendly guide, you''ll learn the very basics of the awk
  command. You''ll also see some of the ways you can use it when dealing with text.

  Let''s get started!

  What is the awk command?

  awk is a scripting language, and it is helpful when ...'
---

Dans ce guide pour débutants, vous apprendrez les bases de la commande `awk`. Vous verrez également certaines des façons dont vous pouvez l'utiliser pour traiter du texte.

Commençons !

## Qu'est-ce que la commande `awk` ?

`awk` est un langage de script, et il est utile lorsque vous travaillez en ligne de commande. C'est aussi une commande largement utilisée pour le traitement de texte.

Lorsque vous utilisez `awk`, vous pouvez sélectionner des données – un ou plusieurs morceaux de texte individuel – en fonction d'un motif que vous fournissez.

Par exemple, certaines des opérations que vous pouvez effectuer avec `awk` sont la recherche d'un mot ou d'un motif spécifique dans un texte donné, ou même la sélection d'une certaine ligne ou d'une certaine colonne dans un fichier que vous fournissez.

### La syntaxe de base de la commande `awk`

Dans sa forme la plus simple, la commande `awk` est suivie d'un ensemble de guillemets simples et d'un ensemble d'accolades, avec le nom du fichier que vous souhaitez rechercher mentionné en dernier.

Cela ressemble à ceci :

```
awk '{action}' votre_nom_de_fichier.txt
```

Lorsque vous souhaitez rechercher du texte qui a un motif spécifique ou que vous cherchez un mot spécifique dans le texte, la commande ressemblerait à ceci :

```
awk '/motif regex/{action}' votre_nom_de_fichier.txt
```

### Comment créer un fichier d'exemple

Pour créer un fichier en ligne de commande, vous utilisez la commande `touch`. Par exemple : `touch nomdefichier.txt` où `nomdefichier` est le nom de votre fichier.

Vous pouvez ensuite utiliser la commande `open` (`open nomdefichier.txt`), et un programme de traitement de texte comme TextEdit s'ouvrira où vous pourrez ajouter le contenu du fichier.

Supposons donc que vous avez un fichier texte, `information.txt`, qui contient des données séparées en différentes colonnes.

Le contenu du fichier pourrait ressembler à ceci :

```
prenom          nom             age     ville      ID

Thomas          Shelby          30      Rio        400
Omega           Night           45      Ontario    600
Wood            Tinker          54      Lisbon     N/A
Giorgos         Georgiou        35      London     300
Timmy           Turner          32      Berlin     N/A
```

Dans mon exemple, il y a une colonne pour `prenom`, `nom`, `age`, `ville` et `ID`.

À tout moment, vous pouvez afficher le contenu de votre fichier en tapant `cat fichier_texte`, où `fichier_texte` est le nom de votre fichier.

### Comment imprimer tout le contenu du fichier en utilisant `awk`

Pour imprimer *tout* le contenu d'un fichier, l'action que vous spécifiez à l'intérieur des accolades est `print $0`.

Cela fonctionnera exactement de la même manière que la commande `cat` mentionnée précédemment.

```shell
awk '{print $0}' information.txt
```

Sortie :

```
prenom          nom             age     ville      ID

Thomas          Shelby          30      Rio        400
Omega           Night           45      Ontario    600
Wood            Tinker          54      Lisbon     N/A
Giorgos         Georgiou        35      London     300
Timmy           Turner          32      Berlin     N/A
```

Si vous souhaitez que chaque ligne ait un numéro de ligne, vous utiliseriez la variable intégrée `NR` :

```shell
awk '{print NR,$0}' information.txt 
```

```
1 prenom        nom             age     ville      ID
2 
3 Thomas        Shelby          30      Rio        400
4 Omega         Night           45      Ontario    600
5 Wood          Tinker          54      Lisbon     N/A
6 Giorgos       Georgiou        35      London     300
7 Timmy         Turner          32      Berlin     N/A

```


### Comment imprimer des colonnes spécifiques en utilisant `awk`

Lorsque vous utilisez `awk`, vous pouvez spécifier certaines colonnes que vous souhaitez imprimer.

Pour imprimer la première colonne, vous utilisez la commande :

```shell
awk '{print $1}' information.txt
```

Sortie :

```
Thomas
Omega
Wood
Giorgos
Timmy
```

Le `$1` représente le premier champ, dans ce cas la première colonne.

Pour imprimer la deuxième colonne, vous utiliseriez `$2` :

```shell
awk '{print $2}' information.txt
```

Sortie :

```
nom

Shelby
Night
Tinker
Georgiou
Turner
```

La façon dont `awk` détermine où chaque colonne commence et se termine est avec un espace, par défaut.

Pour imprimer plus d'une colonne, par exemple la première et la quatrième colonne, vous feriez :

```shell
awk '{print $1, $4}' information.txt
```

Sortie :

```
prenom ville
 
Thomas    Rio
Omega     Ontario
Wood      Lisbon
Giorgos   London
Timmy     Berlin
```

Le `$1` représente le premier champ d'entrée (première colonne), et le `$4` représente le quatrième. Vous les séparez avec une virgule, `$1,$4`, pour que la sortie ait un espace et soit plus lisible.

Pour imprimer le dernier champ (la dernière colonne), vous pouvez également utiliser `$NF` qui représente le *dernier* champ d'un enregistrement :

```shell
awk '{print $NF}' information.txt 
```

Sortie :

```
ID

400
600
N/A
300
N/A
```


### Comment imprimer des lignes spécifiques d'une colonne

Vous pouvez également spécifier la ligne que vous souhaitez imprimer à partir de votre colonne choisie :

```shell
awk '{print $1}' information.txt | head -1 
```

Sortie :

```
prenom
```

Décomposons cette commande. `awk '{print $1}' information.txt` imprime la première colonne. Ensuite, la sortie de cette commande (que vous avez vue précédemment) est *redirigée*, en utilisant le symbole pipe `|`, vers la commande head, où son argument `-1` sélectionne la première ligne de la colonne.

Si vous vouliez deux lignes imprimées, vous feriez :

```shell
awk '{print $1}' information.txt | head -2 
```


Sortie :

```
prenom
Dionysia
```

### Comment imprimer des lignes avec un motif spécifique dans `awk`

Vous pouvez imprimer une ligne qui **commence** par une lettre spécifique.

Par exemple :

```shell
awk '/^O/' information.txt
```

Sortie :

```
Omega           Night           45      Ontario    600
```

Cette commande sélectionne toute ligne avec du texte qui *commence* par un `O`.

Vous utilisez d'abord le symbole flèche vers le haut (`^`), qui indique le début d'une ligne, puis la lettre par laquelle vous voulez qu'une ligne commence.

Vous pouvez également imprimer une ligne qui **se termine** par un motif spécifique :

```shell
awk '/0$/' information.txt 
```

Sortie :

```
Thomas          Shelby          30      Rio        400
Omega           Night           45      Ontario    600
Giorgos         Georgiou        35      London     300
```

Cela imprime les lignes qui se terminent par un `0` – le symbole `$` est utilisé après un caractère pour signifier comment une ligne se terminera.

Cette commande pourrait également être modifiée en :

```shell
awk '! /0$/' information.txt 
```

Le `!` est utilisé comme un `NON`, donc dans ce cas, il sélectionne les lignes qui ne se terminent pas par un `0`.

```
prenom          nom             age     ville      ID

Wood            Tinker          54      Lisbon     N/A
Timmy           Turner          32      Berlin     N/A
```

#### Comment utiliser les expressions régulières dans `awk`

Pour afficher les mots qui contiennent certaines lettres et imprimer les mots qui correspondent à un motif que vous spécifiez, vous utilisez à nouveau les barres obliques, `//`, comme montré précédemment.

Si vous voulez rechercher des mots contenant `on`, vous feriez :

```shell
awk ' /io/{print $0}' information.txt 
```

Sortie :

```
Thomas          Shelby          30      Rio        400
Omega           Night           45      Ontario    600
Giorgos         Georgiou        35      London     300
```

Cela correspond à toutes les entrées qui contiennent `io`.


Supposons que vous avez une colonne supplémentaire – une colonne `département` :

```
prenom          nom             age     ville      ID   département

Thomas          Shelby          30      Rio        400  IT
Omega           Night           45      Ontario    600  Design
Wood            Tinker          54      Lisbon     N/A  IT
Giorgos         Georgiou        35      London     300  Data
Timmy           Turner          32      Berlin     N/A  Engineering
```

Pour trouver toutes les informations des personnes travaillant dans `IT`, vous devriez spécifier la chaîne que vous recherchez entre les barres obliques, `//` :

```shell
awk '/IT/' information.txt 
```

Sortie :

```
Thomas          Shelby          30      Rio        400  IT
Wood            Tinker          54      Lisbon     N/A  IT
```

Et si vous vouliez voir uniquement les prénoms et noms des personnes travaillant dans `IT` ?

Vous pouvez spécifier la colonne comme suit :

```shell
awk '/IT/{print $1, $2}' information.txt 
```

Sortie :

```
Thomas Shelby
Wood   Tinker
```

Cela n'affichera que les première et deuxième colonnes où `IT` apparaît, au lieu de présenter tous les champs.

Lorsque vous recherchez des mots avec un motif spécifique, il peut y avoir des moments où vous devrez utiliser un caractère d'échappement, comme suit :

```shell
awk '/N\/A$/' information.txt 
```

Sortie :

```shell
Wood            Tinker          54      Lisbon     N/A
Timmy           Turner          32      Berlin     N/A
```

Je voulais trouver les lignes qui se terminent par le motif `N/A`.

Donc, lorsque je recherche entre les `' // '` comme montré jusqu'à présent, j'ai dû utiliser un caractère d'échappement (`\`) entre `N/A`, sinon j'aurais obtenu une erreur.


### Comment utiliser les opérateurs de comparaison dans `awk`

Si, par exemple, vous vouliez trouver toutes les informations des employés qui ont moins de `40` ans, vous utiliseriez l'opérateur de comparaison `<` comme suit :

```shell
awk '$3 <  40 { print $0 }' information.txt
```

Sortie :

```
Thomas          Shelby          30      Rio        400
Giorgos         Georgiou        35      London     300
Timmy           Turner          32      Berlin     N/A
```

La sortie montre uniquement les informations des personnes de moins de 40 ans.

## Conclusion

Et voilà ! Vous connaissez maintenant les bases absolues pour commencer à travailler avec `awk` et manipuler des données textuelles.

Pour en savoir plus sur Linux, freeCodeCamp dispose d'une grande variété de matériaux d'apprentissage disponibles.

En voici quelques-uns pour vous aider à commencer :

- [Linux Basics - Hands-On Workshop](https://www.youtube.com/watch?v=0Qnwqe2P3eY)
- [Linux for Ethical Hackers (Kali Linux Tutorial)](https://www.youtube.com/watch?v=lZAoFs75_cs&t=77s)
- [The Linux Command Handbook](https://www.freecodecamp.org/news/the-linux-commands-handbook/)


Merci d'avoir lu et bon apprentissage 😊