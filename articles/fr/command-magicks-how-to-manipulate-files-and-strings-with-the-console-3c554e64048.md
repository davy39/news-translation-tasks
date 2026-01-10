---
title: 'Magies de Commande : Comment Manipuler des Fichiers et des Chaînes avec la
  Console'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-17T19:33:08.000Z'
originalURL: https://freecodecamp.org/news/command-magicks-how-to-manipulate-files-and-strings-with-the-console-3c554e64048
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8SjtkPp6PLAWGnOXY-xxhg.jpeg
tags:
- name: Computer Science
  slug: computer-science
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: 'Magies de Commande : Comment Manipuler des Fichiers et des Chaînes avec
  la Console'
seo_desc: 'By Luciano Strika

  As developers, there are lots of repetitive things we do every day that take away
  our precious time. Finding ways to automate and optimize those processes is usually
  very lucrative.

  Many times we find ourselves sifting through a pro...'
---

Par Luciano Strika

En tant que développeurs, il y a beaucoup de choses répétitives que nous faisons chaque jour et qui prennent notre temps précieux. Trouver des moyens d'automatiser et d'optimiser ces processus est généralement très rentable.

Souvent, nous nous retrouvons à parcourir la sortie d'un programme à la recherche des informations pertinentes et à les déplacer manuellement dans un autre fichier, à convertir toutes les lettres majuscules d'une phrase en minuscules, ou à supprimer tous les caractères non numériques d'un fichier. Le genre de tâches ennuyeuses, répétitives et sujettes aux erreurs qui peuvent s'accumuler si nous les faisons à la main, et se transformer en un vrai casse-tête.

Il est de notoriété publique que nous devrions faire ces choses de manière programmatique et non manuelle. Souvent, le problème se situe dans cette zone idéale où coder un script entier pour cela, même en Python, semble excessif. Faire la chose à la main prendra trop de temps ou générera trop d'erreurs.

Heureusement, beaucoup de ces tâches ont déjà été codées par des personnes bien plus intelligentes que nous. Elles peuvent être accessibles avec seulement quelques pressions de touches. Elles sont toutes disponibles sous forme de commandes shell, et je vais vous en montrer quelques-unes aujourd'hui. Si vous êtes complètement nouveau dans le terminal et que vous ne savez pas comment naviguer dans votre système de fichiers ou faire des tâches similaires, je vous suggère de lire [mon introduction précédente au terminal](https://medium.freecodecamp.org/how-you-can-be-more-productive-right-now-using-bash-29a976fb1ab4).

Alors, sans plus tarder, laissez-moi vous présenter les sorts les plus utiles que tout sorcier du codage devrait connaître.

#### echo : Faire apparaître une chaîne dans la console

Avant de pouvoir plonger dans les arts de la divination et de la transformation, un vrai sorcier de la programmation doit maîtriser l'art de la conjuration. 
La commande echo, suivie d'une chaîne, fera simplement en sorte que la console affiche ce qui a été donné en entrée. Par exemple, exécuter la ligne suivante :

```
echo "hello world!"
```

produira la sortie suivante :

```
hello world!
```

Cela peut sembler trivial pour l'instant, mais je vous promets que cela sera utile à l'avenir.

#### cat : Montrer la vraie forme de l'entrée

Appeler la commande cat sur un fichier affichera son contenu dans le terminal. 
Par exemple, nous avons un répertoire contenant les fichiers 'file1.txt' et 'file2.txt'. Les deux fichiers contiennent le texte 'this is a file'. Appeler :

```
cat file1.txt
```

affichera le contenu du fichier :

```
this is a file
```

Notez que l'argument de la commande cat peut être n'importe quel nom de style shell. Nous pouvons utiliser le caractère générique *, pour correspondre à n'importe quelle chaîne. De cette façon, nous pourrions afficher les contenus de différents fichiers les uns après les autres, comme ceci :

```
cat *.txt
```

Dans ce cas, * correspond à la fois à file1 et file2, et ils se terminent tous les deux par .txt, donc ils sont tous les deux imprimés. La sortie de cette commande serait :

```
this is a filethis is a file
```

Rappelez-vous de cette commande — aucun sorcier n'est vraiment complet sans un chaton.

#### grep : trouver une aiguille dans une botte de foin

Passant à la divination, grep est le sort pour trouver une sous-chaîne dans une chaîne. 
Appeler

```
grep <some string> filename
```

affichera chaque ligne du fichier spécifié où la chaîne donnée apparaît.

Si nous voulons qu'elle apparaisse non seulement dans sa forme exacte mais aussi avec une casse différente, nous devons passer l'argument **-i**, pour ignorer la casse.

Si nous l'appelons sur différents fichiers dans une seule commande, nous obtiendrons une liste de chaque fichier avec des lignes correspondant au motif. Par exemple, dans le répertoire précédent, appeler

```
grep "this" *.txt
```

donnera

```
file1.txt: this is a file
file2.txt: this is a file
```

#### sed : transformer une chaîne en une autre

La commande sed est un sort de transmutation. Elle prend le contenu d'un fichier et le transforme en un autre. Il existe de nombreuses façons de l'utiliser. Certaines que je confesse connaître peu. (Si vous lisez ceci et pensez à des choses cool que sed fait et que je ne mentionne pas, dites-le-moi dans les commentaires, car j'adore apprendre de nouveaux tours). L'une des plus courantes consiste à remplacer les parties d'une chaîne qui correspondent à un motif, par différentes chaînes.

Cela se fait en appelant

```
sed "s/regexp/replacement/optional_flags" file_name
```

Ce que cela fera est :

* Rechercher chaque ligne qui correspond à la regexp dans le fichier file_name
* Remplacer la première instance de _regexp_ de cette ligne par _replacement_
* Afficher la chaîne résultante dans la console (sans altérer le fichier !).

Si nous fournissons le drapeau g à la fin (comme ceci s/old/new/g), il correspondra à toutes les instances sur chaque ligne, au lieu de seulement la première. Utiliser l'argument **-i** (pour in-place) écrira réellement dans le fichier d'entrée.

Par exemple, appeler

```
sed "s/is/was/g" file1.txt
```

affichera

```
thwas was a file
```

Si nous voulons ne correspondre qu'aux mots entiers, nous devons mettre le caractère \b autour de la regexp, comme ceci

```
sed "s/\\bis\\b/was/g" file1.txt
```

pour enfin obtenir

```
this was a file
```

## Combiner nos sorts : Les Opérateurs

Maintenant que vous êtes compétent dans quatre nouvelles écoles de magie, chacune avec son sort caractéristique. Mais pour devenir un vrai sorcier, vous devez apprendre à lier les fils de la magie en motifs impressionnants. Pour ce faire, vous utiliserez trois outils puissants.

#### | (Pipe) Opérateur

L'opérateur pipe prend la sortie de la commande précédente et l'écrit dans l'entrée de la commande suivante, créant un pipeline. 
Par exemple, appeler

```
cat *.txt | grep "is"
```

récupérera d'abord le contenu de tous les fichiers texte dans le répertoire de travail actuel. Ensuite, il recherchera chaque ligne qui contient la chaîne "is", avant de finalement les imprimer.

#### > (write) Opérateur

L'opérateur write écrira son entrée dans sa sortie — généralement un fichier.

Ainsi, par exemple, un moyen rapide de créer un fichier texte avec 'this is a file' comme contenu serait d'appeler

```
echo "this is a file" > some_file.txt
```

Voyez comment tout ce sort de conjuration s'additionne réellement ? Je vous avais dit que ce serait utile.

Notez que si le fichier existait déjà, cela écrasera son contenu, sans même demander. Dans le cas où ce n'est pas ce que nous voulions, nous devons utiliser notre dernier outil :

#### >> (append) Opérateur

L'opérateur >> écrira son entrée dans sa sortie, sauf qu'il n'écrasera pas ce qui s'y trouve déjà.

C'est tout, nous avons terminé ce tutoriel et vous êtes maintenant l'apprenti d'un sorcier. Allez pratiquer vos nouvelles compétences en lancement de sorts, et vous pourrez me remercier plus tard. N'oubliez pas de vérifier les pages man pour toutes ces commandes si vous êtes bloqué ou si vous ne vous souvenez pas de ce que faisaient certains drapeaux — un sorcier n'est jamais loin de ses livres.

_Veuillez envisager de [soutenir mon habitude d'écrire](https://www.buymeacoffee.com/strikingloo) avec un petit don._

_Suivez-moi sur Medium pour plus de tutoriels, de conseils et d'astuces. Cet article a également été publié sur [datastuff.tech](http://www.datastuff.tech/programming/files-strings-shell-tutorial/), mon nouveau site web. Allez y faire un tour !_