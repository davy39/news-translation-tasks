---
title: La commande Cat sous Linux – Comment créer un fichier texte avec Cat ou Touch
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-11T00:57:51.000Z'
originalURL: https://freecodecamp.org/news/the-cat-command-in-linux-how-to-create-a-text-file-with-cat-or-touch
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a5d740569d1a4ca2531.jpg
tags:
- name: Linux
  slug: linux
seo_title: La commande Cat sous Linux – Comment créer un fichier texte avec Cat ou
  Touch
seo_desc: 'By Hughie Coles

  The cat command is a very popular and versatile command in the ''nix ecosystem.  There
  are 4 common usages of the cat command. It can display a file, concatenate (combine)
  multiple files, echo text, and it can be used to create a new f...'
---

Par Hughie Coles

La commande `cat` est une commande très populaire et polyvalente dans l'écosystème 'nix. Il existe 4 usages courants de la commande `cat`. Elle peut afficher un fichier, concaténer (combiner) plusieurs fichiers, écho du texte, et elle peut être utilisée pour créer un nouveau fichier.

## Affichage d'un fichier

L'utilisation la plus courante de la commande cat est d'afficher le contenu d'un fichier. Voici un exemple que vous pouvez essayer.

```sh
echo "Dance, Dance" > cat_create #créer un fichier
cat cat_create
```

Dans cet exemple simple, nous utilisons une combinaison de `echo` et d'une redirection pour créer un fichier contenant "Dance, Dance". Nous utilisons ensuite la commande `cat` pour afficher le contenu.

La sortie est la suivante :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-11.png)
_La sortie des commandes d'exemple_

## (Con)cat

L'exemple précédent est en fait un cas spécifique de la fonction principale de la commande cat, qui est de concaténer des fichiers pour l'affichage. Si nous utilisons la commande de la même manière, mais que nous lui donnons deux fichiers ou plus, elle affiche alors la concaténation des fichiers.

Si nous exécutons les commandes suivantes :

```sh
echo "This is how we do it" > test1 #créer le 1er fichier
echo "*This is how we do it*" > test2 #créer le 2ème fichier
cat test1 test2

```

La sortie est le contenu du 1er fichier, suivi du contenu du 2ème fichier. Vous pouvez donner plusieurs fichiers à cat et il les concaténera (combinera) tous. Remarquez cependant que la commande cat insère automatiquement un saut de ligne entre les sorties.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-12.png)
_La sortie de deux fichiers concaténés_

`cat` fournit également des options pour faire des choses comme afficher les caractères non imprimables (-v), ou numéroté vos lignes (-n). Une explication complète peut être trouvée [dans les pages man](https://man7.org/linux/man-pages/man1/cat.1.html).

## Écho

Ceci est une utilisation moins courante de `cat`, mais c'est la base de la section suivante. Si vous exécutez la commande `cat` sans arguments, `cat` s'exécutera en mode interactif et écho tout ce que vous tapez jusqu'à ce que vous quittiez la commande.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-13.png)
_Exécution de cat en mode interactif_

Dans l'exemple ici, j'ai tapé un mot par ligne. Chaque fois que j'ai appuyé sur entrée, la ligne a été écho.

Vous pouvez également rediriger du texte vers `cat`, auquel cas ce texte est écho. Par exemple :

```sh
echo "Piping fun" | cat

```

Cela donnera la sortie suivante :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-14.png)
_Redirection de texte vers cat_

## Création d'un fichier

Dans les exemples précédents, nous avons utilisé la commande `echo` redirigée vers un fichier pour créer de nouveaux fichiers. Cat peut être utilisé de manière similaire. En fait, nous pouvons utiliser la fonctionnalité de concaténation et d'écho de `cat` pour créer des fichiers.

Nous pouvons créer un fichier contenant la concaténation de plusieurs fichiers comme ceci :

```sh
echo "File 1 Contents" > file1
echo "File 2 Contents" > file2
echo "File 3 Contents" > file3
cat file1 file2 file3 > combined_file
cat combined_file
```

Dans l'exemple ci-dessus, nous créons 3 fichiers en utilisant `echo`, nous combinons les 3 fichiers en un seul en utilisant `cat`, puis nous affichons le nouveau fichier combiné en utilisant `cat`.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-15.png)
_Le résultat des commandes ci-dessus. Nous avons créé 3 fichiers, puis nous les avons combinés en un seul fichier en utilisant cat_

Nous pouvons également utiliser le mode interactif de `cat` pour créer un fichier avec le texte que nous tapons dans le terminal.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-16.png)

Chaque fois que vous appuyez sur entrée, cela valide le texte dans le fichier. Si vous avez du texte non validé et que vous quittez, il ne sera pas capturé dans le fichier.

C'est une façon fantastique de créer un fichier rapidement avec la possibilité de saisir le contenu du fichier.

## Utilisation de Touch pour créer un fichier à la place

Parfois, vous avez juste besoin qu'un fichier existe. En alternative à l'utilisation de `cat` pour créer un fichier, vous pouvez utiliser la commande `touch`.

La commande `touch` a été conçue pour mettre à jour le timestamp de modification d'un fichier, mais elle est couramment utilisée comme moyen rapide de créer un fichier vide. Voici un exemple de cette utilisation :

```sh
touch new_file_name
```

La commande touch peut créer plusieurs fichiers, mettre à jour les timestamps de modification et/ou de création, et bien d'autres choses utiles. [Les pages man complètes peuvent être trouvées ici.](https://www.man7.org/linux/man-pages/man1/touch.1.html)

Touch est couramment utilisé pour s'assurer qu'un fichier existe, et est une excellente commande si vous avez besoin d'un fichier vide rapidement.

## Résumé

Cat est une commande très utile. Vous pouvez l'utiliser pour créer, afficher et combiner des fichiers texte très rapidement et facilement.

Si vous avez juste besoin qu'un fichier existe, mais que cela ne vous dérange pas (ou que vous le requérez) qu'il soit vide, utiliser `touch` est une excellente alternative.

Hughie Coles est un développeur principal chez Index Exchange. Il écrit sur l'architecture logicielle, la mise à l'échelle, le leadership et la culture. Pour plus de ses écrits, consultez son blog sur medium.