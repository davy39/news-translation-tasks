---
title: Comment commencer à utiliser le terminal pour être plus productif
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-07T23:35:35.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-be-more-productive-right-now-using-bash-29a976fb1ab4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*T5VYxE-aik-V7hXOaU9Wuw.jpeg
tags:
- name: '#LifeHacks'
  slug: lifehacks
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment commencer à utiliser le terminal pour être plus productif
seo_desc: 'By Luciano Strika

  As developers, the terminal can be our second home.

  However, we can’t use it until we learn how to, and need to practice using it to
  learn, really — it’s a catch-22!

  I hope this introduction will solve that puzzle for you. I want to...'
---

Par Luciano Strika

En tant que développeurs, le terminal peut être notre deuxième maison.

Cependant, nous ne pouvons pas l'utiliser tant que nous n'avons pas appris comment, et nous devons pratiquer pour apprendre, vraiment — c'est un cercle vicieux !

J'espère que cette introduction résoudra cette énigme pour vous. Je veux vous aider à commencer à utiliser le terminal tout de suite.

### Installation

Je vais d'abord couvrir les bases, donc si vous connaissez déjà tout ce qui est dans cet article, restez à l'écoute pour les prochains, où je traiterai de sujets plus avancés.

Cela étant dit, je vais commencer depuis le tout début. Si vous êtes sur Ubuntu, tout ce que vous avez à faire pour ouvrir votre terminal est d'appuyer sur _ctrl+alt+._ Sur un Mac, vous devez appuyer sur _cmd+barre d'espace_, commencer à taper _terminal_ et appuyer sur entrée lorsque l'option apparaît.

Dans les deux cas, vous devriez voir un fond sombre avec votre nom d'utilisateur suivi du nom de votre ordinateur (sous Linux) ou dans l'ordre inverse (sur un Mac).

Je vous conseille vivement d'ouvrir votre propre terminal et d'essayer ces commandes sur un répertoire vide, pour voir par vous-même et vous habituer à elles.

Vous verrez une invite vous demandant de taper des commandes. Pour entrer une commande, il suffit de la taper et d'appuyer sur entrée. Voici quelques commandes de navigation :

#### cd : Déplacer votre répertoire de travail.

```
cd <chemin relatif>
```

Cela fera pointer votre terminal vers un répertoire différent, à partir duquel vous pourrez exécuter de nouvelles commandes. Par exemple, si vous êtes dans un dossier appelé _animaux_ avec trois dossiers _chats_, _chiens_ et _tortues_, vous exécuteriez

```
cd tortues
```

pour vous déplacer dans ce répertoire. Pour remonter d'un niveau à partir du répertoire actuel (par exemple, revenir à _animaux_ depuis _tortues_), tapez

```
cd ..
```

#### mkdir et touch : Créer des dossiers ou des fichiers.

Si vous devez créer un nouveau répertoire vide, il vous suffit d'exécuter

```
mkdir <nom du répertoire>
```

Alors qu'exécuter

```
touch <nom_du_fichier>
```

créera un fichier vide dans le répertoire de travail actuel, avec le premier argument comme nom.

Si un autre fichier avec le nom donné existait déjà, cela mettra uniquement à jour la date de dernière mise à jour du fichier. Cela ne modifiera pas son contenu.

'Mais pourrais-je savoir si le fichier existe ?!' vous demandez. Eh bien, je suis content que vous posiez la question.

#### ls : Voir le contenu d'un répertoire.

La commande _ls_ liste le nom de chaque fichier et répertoire à l'intérieur du répertoire de travail actuel, par ordre alphabétique. Vous pouvez lui passer quelques arguments en utilisant des tirets, comme ceci :

```
ls -a -l
```

Dans ce cas, l'argument _-a_ fait en sorte que _ls_ affiche les fichiers invisibles. La commande _-l_ fait en sorte que la sortie ressemble à une liste. Elle affiche une ligne pour chaque élément, avec quelques données supplémentaires comme la taille de chaque fichier ou sa date de création.

Un de mes arguments préférés pour _ls_ est _-R_, qui appelle récursivement _ls_ sur chaque sous-répertoire listé pour un rapide aperçu d'un dépôt ou d'une arborescence de fichiers.

Notez que pour toutes les commandes, les arguments peuvent en fait être combinés après un seul tiret :

```
ls -alR
```

Maintenant, je vous entends demander 'Comment vais-je me souvenir de tous ces arguments et options ? Est-ce que toutes les commandes ont autant de fonctionnalités folles ?'  
Mais ne vous inquiétez pas — nous vous avons couvert.

#### man : Ne cessez jamais d'apprendre !

Si vous avez été sur Stack Overflow ou Reddit, vous avez probablement rencontré la phrase 'lisez les pages man' utilisée soit de manière éducative, soit comme une insulte.   
Je suis ici pour la première utilisation.

Essayez d'exécuter

```
man <nom de la commande>
```

Cela affichera la page man de cette commande — la documentation officielle, avec tous ses arguments et utilisations possibles. La plupart d'entre nous l'utilisent lorsque nous sommes sûrs qu'un certain programme a fait quelque chose, mais nous ne nous souvenons pas exactement de quel flag l'a fait faire. C'est aussi très bien d'appeler man sur une commande la première fois que vous l'utilisez (par exemple, si elle apparaît dans un résultat Google), pour en apprendre un peu plus à son sujet et peut-être trouver de meilleures façons de l'invoquer. Pour fermer une page man, il suffit d'appuyer sur _Q_.

#### head et tail, cat et less : Lire le contenu d'un fichier.

Appeler _head_ ou _tail_ sur un fichier vous montrera ses 10 premières ou dernières lignes, respectivement.  
Voici quelques arguments sympas que vous pouvez utiliser :

* **-n <nombre**> : affiche _n_ lignes au lieu des 10 par défaut
* **-f** (pour _tail_) : Affiche les lignes en temps réel et ne s'arrête pas (parfait pour surveiller un fichier journal lorsque vous vous connectez en _ssh_ à un serveur)

Appeler _cat_ affichera simplement le contenu d'un fichier. Assurez-vous de l'utiliser sur des fichiers texte réels, ou vous verrez des choses bizarres.

Si vous appelez _cat_ sur un fichier volumineux (ou même volumineux-_ish_, pour être honnête), vous trouverez probablement assez gênant de continuer à faire défiler vers le haut et vers le bas, à la recherche des lignes pertinentes. Il existe en fait une manière plus pratique de faire cela : la commande _less_.

_less_ vous montrera _moins_ d'un fichier en chargeant son contenu de manière tamponnée. Vous pouvez faire défiler le fichier avec les touches fléchées au lieu d'utiliser la molette de la souris ou le pavé tactile, ce qui est beaucoup plus confortable. Vous pouvez également appuyer sur /, taper quelque chose et appuyer sur _Entrée_ pour rechercher dans le fichier (comme utiliser _ctrl+f_).  
Pour quitter le mode _less_, il suffit d'appuyer sur _Q_.

#### cp et mv : Copier, couper et coller.

_cp_ (copier) et _mv_ (déplacer) sont les équivalents bash de _copier_ et _couper_, respectivement. Vous pouvez les utiliser comme ceci :

```
cp <source> <destination>
```

Pour copier le(s) fichier(s) dans _source_ vers _destination_.

La source peut être soit un fichier, soit un ensemble de fichiers. Pour sélectionner plus d'un fichier, vous pouvez utiliser le caractère générique de bash : *****. Ce caractère correspondra à n'importe quelle chaîne, même vide.

Par exemple, cette commande copiera tous les fichiers dans le dossier _some_folder_ dans le dossier _some_other_folder_, situé un niveau plus haut dans le système de fichiers.

```
cp some_folder/* ../some_other_folder
```

Mais si nous voulions seulement déplacer les fichiers .txt dans un répertoire appelé _textes_, nous utiliserions :

```
cp *.txt textes/
```

puisque * correspond à n'importe quelle chaîne. Nous imposons que son extension soit _.txt._ (par exemple, _*.txt_ correspond à _filename.txt_, puisque _*_ correspond à _filename_, mais pas à _filename.xtt_, puisque même si * correspond au nom entier, il n'y a rien qui correspond à _.txt_)._

La destination peut être le chemin d'un fichier (écrasant le fichier actuel à ce chemin, s'il existe, ou en créant un nouveau sinon) si la source est un seul fichier, ou un nom de répertoire si vous souhaitez copier/déplacer plusieurs fichiers.

#### rm : Supprimer des fichiers et des répertoires.

L'inverse de _touch_, _rm_ supprime un fichier ou un répertoire.

L'utiliser dans sa forme par défaut

```
rm nom_du_fichier
```

fonctionnera pour supprimer un fichier, mais générera une erreur lors de la suppression d'un répertoire. Cela nous empêche de supprimer des fichiers importants dans un répertoire, ou un répertoire entier en pensant que c'est juste un fichier.

Pour contourner cela, si vous vous sentez courageux, ajoutez simplement _-r_, pour supprimer récursivement chaque fichier dans un répertoire jusqu'à ce qu'il soit vide, avant de le supprimer comme un sorte de supprimateur en série. Si vous ne voulez supprimer que les répertoires vides, utilisez _-d_ à la place.

Notez que vous pouvez toujours utiliser le caractère générique (*) pour supprimer de nombreux fichiers ou répertoires en une seule commande. Par exemple, appeler

```
rm *.txt
```

supprime tous les fichiers texte du répertoire de travail actuel.

#### La fin... pour l'instant.

Ouf, c'était une introduction. Vous êtes maintenant familier avec les commandes les plus courantes que vous utiliserez dans votre vie de programmation quotidienne.

Il y a beaucoup de choses que je n'ai pas encore couvertes. Je prévois de faire un suivi avec plus de cas d'utilisation, plus de commandes et plus de problèmes réels à résoudre.

Pendant que je prépare le prochain article, j'aimerais vous encourager à essayer ces commandes par vous-même. Voyez lesquelles vous font gagner du temps, et habituez-vous à ce terminal. Peut-être marquez cette page et utilisez-la comme référence. Je ne le dirai à personne.

Je vous promets, après un certain temps, vous commencerez à voir pourquoi cela en vaut la peine. (Je sais que cela m'a pris un certain temps). Finalement, vous ouvrirez instinctivement le terminal chaque fois que vous commencerez à faire quelque chose.

J'espère que vous avez trouvé une partie de cette introduction utile, et si c'est le cas, faites-le moi savoir ! J'accorde beaucoup de valeur aux retours de mes lecteurs. C'est la principale raison pour laquelle j'écris, alors dites-moi si une partie était difficile à comprendre, si certaines commandes semblent inutiles, ou si mon tutoriel est simplement trop ennuyeux. Dites-moi aussi si une partie était intéressante !

[_La partie 2 est déjà disponible_](https://medium.freecodecamp.org/command-magicks-how-to-manipulate-files-and-strings-with-the-console-3c554e64048).

_Suivez-moi pour plus de tutoriels, de conseils et d'astuces de programmation._   
_Vous pouvez également lire mes articles sur [www.datastuff.tech](http://www.dataden.tech/blog)_