---
title: Pourquoi vous devriez utiliser l'indentation en colonnes pour améliorer la
  lisibilité de votre code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-26T04:43:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-columnize-your-code-to-improve-readability-f1364e2e77ba
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EWTTZDqP8okovm5BF4QPFA.png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Pourquoi vous devriez utiliser l'indentation en colonnes pour améliorer
  la lisibilité de votre code
seo_desc: 'By Leonardo Carreiro

  I think that the most important aspect of programming is the readability of the
  source code that you write or maintain. This involves many things, from the syntax
  of the programming language, to the variable names, comments, and ...'
---

Par Leonardo Carreiro

Je pense que l'aspect le plus important de la programmation est la lisibilité du code source que vous écrivez ou maintenez. Cela implique de nombreuses choses, de la syntaxe du langage de programmation, aux noms des variables, commentaires et indentation. Ici, je discute de ce dernier point, **l'indentation**.

Ce n'est pas une question de taille d'indentation, ou du choix entre les tabulations et les espaces, ou si cela devrait être requis dans un langage comme Python. Beaucoup de gens aiment utiliser une longueur maximale de ligne pour chaque ligne de code, généralement 80 ou 120 caractères. Avec cette idée, il n'y a pas de longueur maximale, et parfois vous devrez utiliser la barre de défilement horizontale. Mais ne paniquez pas, ce n'est pas pour tout le code — c'est juste pour certaines parties.

### Quatre exemples d'améliorations utilisant l'indentation du code

#### Premier exemple

Jetez un œil à ce code :

La lisibilité n'est pas très bonne, et vous pourriez finir avec quelque chose comme ceci pour éviter le désordre :

Et vos sept lignes sont devenues presque 40 lignes. Cela avec seulement trois ou quatre propriétés par objet. Si c'était huit propriétés, cela deviendrait 70 lignes.

L'idée dont je parle est d'utiliser quelque chose comme ceci (je l'appelle du code "indenté en colonnes") :

#### Deuxième exemple

Ce n'est pas seulement pour les littéraux d'objets. Cela peut être utilisé pour n'importe quel morceau de code qui est un groupe de lignes similaires. Ce processus peut être rapide. Vous pouvez copier la première ligne, la coller, puis réécrire les parties changeantes dans chaque ligne.

Cela peut être utilisé dans les `import` JS également. Comparez ces deux versions :

Ces treize imports sont ordonnés alphabétiquement par le chemin. Tous proviennent du dossier `vs` — cinq de `vs/base` et huit de `vs/platform`.

Vous ne pouvez pas voir cela sans bouger les yeux d'avant en arrière sur chaque ligne. Faire cela est ennuyeux. Bien sûr, vous n'avez pas besoin de faire des statistiques sur la façon dont vos fichiers importent d'autres fichiers. Mais à un moment donné, vous lirez ce code pour voir si vous avez importé quelque chose depuis le bon fichier, ou si un fichier a déjà été importé.

Maintenant, voyez comment cela ressemble lorsque le même code est indenté en colonnes :

Cela ne le rend-il pas un peu meilleur ?

#### Troisième exemple

Dans cet exemple, nous avons une déclaration de méthode du compilateur TypeScript :

Encore une fois, vous pouvez voir la différence entre les lignes plus facilement. Cela vous aide à lire les cinq lignes en même temps, en dépensant beaucoup moins d'efforts. Et, si vous devez ajouter un paramètre dans chacune de ces 5 lignes, vous pouvez le faire en une seule fois, en utilisant le [curseur multiline](https://stackoverflow.com/a/30039968) dans presque tous les éditeurs de code.

#### Quatrième exemple

Voici le dernier exemple, avec l'original et la comparaison ensemble :

**Avantages** :

* Votre code semble plus propre.
* Votre code a une lisibilité améliorée
* Vous pouvez être en mesure de réduire le nombre de lignes dans votre code

**Inconvénients** :

* L'option de formatage automatique des éditeurs de code peut interférer avec la mise en page
* Lorsque vous ajoutez une ligne à un bloc de lignes, parfois vous devez changer toutes les autres lignes
* Cela peut prendre du temps pour écrire du code

### Quels outils peuvent aider à atteindre cela ?

J'ai fait l'indentation de cette manière, manuellement, pendant un certain temps. C'est ennuyeux, mais une fois que vous commencez à le faire, vous ne pouvez plus vous arrêter. Vous regardez votre code, toutes ces lignes répétées qui pourraient être indentées en colonnes pour être plus lisibles, et vous ne pouvez pas continuer sans le faire. C'est addictif.

J'utilise Visual Studio et Visual Studio Code, donc j'ai essayé de trouver une extension ou un plugin qui aide à atteindre cela. Je n'en ai trouvé aucun. Alors en novembre 2017, j'ai commencé à créer ma propre extension pour Visual Studio Code et je l'ai nommée [Smart Column Indenter](https://marketplace.visualstudio.com/items?itemName=lmcarreiro.vscode-smart-column-indenter).

J'ai publié une première version **utilisable** le même mois. Jetez un œil à son fonctionnement :

![Image](https://cdn-media-1.freecodecamp.org/images/1*gIMmQyMNnEpLgqAUcDTOUA.gif)
_"Smart Column Indenter" pour Visual Studio Code_

Il y a des domaines où l'extension pourrait être améliorée. Actuellement, elle ne fonctionne qu'avec les fichiers `*.ts`, `*.js` et `*.json`. Je pense qu'elle pourrait aider avec les fichiers XML et HTML également, comme l'indentation en colonnes des mêmes attributs de balises répétées, ou différentes balises qui sont répétées dans un groupe de lignes.

Une fois le code sélectionné pour l'indentation en colonnes, l'algorithme fonctionne en trois étapes :

1. Analyse lexicale (ou tokenisation) du code. J'ai installé le [package npm TypeScript](https://www.npmjs.com/package/typescript) comme dépendance et utilisé l'API du compilateur pour éviter de réinventer la roue ici.
2. Exécuter l'algorithme de la [Plus Longue Sous-Séquence Commune (LCS)](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem) en passant chaque ligne de code comme une séquence de tokens. C'est la partie difficile. Beaucoup de références sur Internet parlent de la LCS pour seulement deux séquences en entrée, ce qui est facilement résolu avec la **programmation dynamique**. Comme nous voulons généralement indenter en colonnes plus de deux lignes de code, le problème devient celui de trouver la plus longue séquence commune (LCS) de plusieurs chaînes. [C'est un problème NP-difficile](http://ieeexplore.ieee.org/document/5530316/?reload=true). Comme il s'agit d'un problème générique, j'ai créé un package npm séparé ([multiple-lcs](https://www.npmjs.com/package/multiple-lcs)) avec une implémentation basique pour y parvenir. Ce n'est pas la meilleure solution dans certains cas, mais c'est utilisable.
3. Réécrire le code pour indenter en colonnes les tokens qui apparaissent dans la LCS. Chaque token dans la LCS est placé dans une nouvelle colonne.

Pour certains types de tokens, comme les chaînes de caractères ou les noms de variables, le nom du type est utilisé au lieu du contenu dans l'algorithme LCS. Le résultat est une sous-séquence plus grande.

J'ai mis toute la logique dans un package npm séparé ([smart-column-indenter](https://www.npmjs.com/package/smart-column-indenter)). Si vous voulez créer une extension ou un plugin similaire pour un autre IDE basé sur JavaScript, vous pouvez utiliser ce package.

Ma raison initiale de créer cette solution était une preuve de concept. J'aimerais savoir ce que les autres programmeurs pensent de ma solution. **Si vous l'avez aimée, applaudissez s'il vous plaît**.

Si vous avez des critiques constructives, ou si vous connaissez d'autres outils qui font la même chose, laissez un commentaire. Voici un [article que j'ai trouvé utile](http://www.draconianoverlord.com/2016/09/16/one-true-way-of-indenting.html).

Merci d'avoir lu.

**Mise à jour (2018-03-29)** : Après sa publication il y a quelques jours, j'ai reçu beaucoup de retours, la plupart négatifs, mais merci à tous quand même, c'est bien de savoir pourquoi beaucoup de gens ne l'aiment pas. J'ai découvert plus tard que les gens appellent généralement cela "l'alignement de code", vous ne trouverez rien sur "l'indentation en colonnes", donc si vous voulez en savoir plus, cherchez "l'alignement de code" à la place. Je l'ai fait, et j'ai trouvé un intéressant [article de blog de Terence Eden](https://shkspr.mobi/blog/2014/11/why-i-vertically-align-my-code-and-you-should-too/), comme la plupart des commentaires négatifs concernent les problèmes de fusion VCS, l'historique et les diffs sales, je vais copier sa conclusion : "Si nos outils rendent la compréhension de ces idées plus difficile, ce sont les outils qui doivent changer — pas nous."

**Mise à jour (2018-05-03)** : Comme si quelqu'un de l'équipe GitHub avait lu les commentaires négatifs sur l'alignement de code ici, [vous pouvez maintenant ignorer les espaces blancs dans la révision de code](https://blog.github.com/2018-05-01-ignore-white-space-in-code-review/).

**Mise à jour (2018-05-20)** : Si vous utilisez Visual Studio (pas Code), [Shadman Kudchikar](https://www.freecodecamp.org/news/how-to-columnize-your-code-to-improve-readability-f1364e2e77ba/undefined) a créé une extension similaire, vous pouvez en lire plus [ici](https://medium.com/@kudchikarsk/sharp-column-indenter-visual-studio-extension-d167aaddf11f) ou la télécharger [ici](https://marketplace.visualstudio.com/items?itemName=kudchikarsk.sharp-column-indenter).

### Anecdote

Nous avons maintenant des écrans de 22" avec une résolution de 1920x1080. Il n'y a aucune raison de se limiter à 80 caractères par ligne, bien que vous deviez décider de la limite maximale. L'origine de cette limite de 80 caractères est :

![Image](https://cdn-media-1.freecodecamp.org/images/1*UV-JCMR337fEAsvCF2eVuw.jpeg)
_[Plus d'une personne s'est demandé cela](https://softwareengineering.stackexchange.com/a/148678" rel="noopener" target="_blank" title=")._