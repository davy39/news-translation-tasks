---
title: Comment quitter Vim – Tutoriel sur les commandes de sauvegarde et de sortie
  de Vim
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-21T21:52:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-exit-vim
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/exit-vim-image.jpg
tags:
- name: Productivity
  slug: productivity
- name: vim
  slug: vim
seo_title: Comment quitter Vim – Tutoriel sur les commandes de sauvegarde et de sortie
  de Vim
seo_desc: 'By Xing Liu

  I''ve been using Vim since the first year I started coding. For all the IDEs/editors
  that I have used, the Vim plugin is always the very first plugin that I install.

  I know that Vim can be challenging to work in for people who are not fami...'
---

Par Xing Liu

J'utilise Vim depuis la première année où j'ai commencé à coder. Pour tous les IDE/éditeurs que j'ai utilisés, le plugin Vim est toujours le tout premier plugin que j'installe.

Je sais que Vim peut être difficile à utiliser pour les personnes qui ne le connaissent pas. Dans cet article, nous aborderons des sujets fondamentaux comme comment quitter Vim, plutôt que de _quitter_ Vim.

J'inclurai également la commande que vous pouvez utiliser pour afficher la documentation d'aide correspondante. Pour cela, vous devez d'abord appuyer plusieurs fois sur `ESC`, puis exécuter la commande fournie, par exemple `:h vim-modes`, et appuyer sur `Enter`.

## TL;DR – Comment quitter Vim

1. Appuyez sur <kbd>ESC</kbd> une fois (*parfois deux fois*)
2. Assurez-vous d'utiliser la méthode de saisie en anglais
3. L'étape suivante dépend de l'état actuel et de vos attentes :
    - Si vous n'avez apporté aucune modification, tapez `:q` et appuyez sur <kbd>Enter</kbd>/<kbd>return</kbd>
    - Si vous avez apporté des modifications et souhaitez les **conserver**, tapez `:wq` et appuyez sur <kbd>Enter</kbd>/<kbd>return</kbd>
    - Si vous avez apporté des modifications et préférez les **abandonner**, tapez `:q!` et appuyez sur <kbd>Enter</kbd>/<kbd>return</kbd>

Si vous souhaitez comprendre plus en détail comment cela fonctionne, plongeons-nous dans le sujet.

## Quels sont les modes dans Vim ?

Il existe sept modes de BASE dans Vim et sept modes supplémentaires considérés comme des variantes des modes de BASE. Vous pouvez exécuter `:h vim-modes` dans Vim pour lire la documentation si vous souhaitez en savoir plus.

Heureusement, nous n'avons pas besoin de tous les connaître pour commencer. Mais il y a trois modes dont nous devons être conscients : `Normal Mode`, `Insert Mode` et `Command-line Mode`.

### Qu'est-ce que le mode normal dans Vim ?

Le `Normal Mode` est crucial car c'est uniquement dans le `Normal Mode` que nous pouvons exécuter des commandes (il existe des exceptions mais celles-ci dépassent le cadre de cet article).

Par exemple, si nous voulons lire la documentation de `vim-modes`, nous devons d'abord nous assurer d'être en `Normal Mode` avant de taper `:h vim-modes`. Et la manière la plus canonique d'entrer dans le `Normal Mode` est d'appuyer sur `ESC`. Même si vous êtes déjà en `Normal Mode`, appuyer sur `ESC` vous maintiendra en `Normal Mode`, donc pas d'inquiétude.

Trouvez-le dans la documentation : `:h Normal`, `:h mode-switching`.

### Qu'est-ce que le mode insertion dans Vim ?

Vous utilisez le `Insert Mode` pour éditer le fichier actuel (dans Vim, cela est normalement appelé `buffer`). Par défaut, nous sommes en `Normal Mode` juste après avoir ouvert un fichier. Si nous devons apporter des modifications au fichier actuel, nous devons d'abord passer en `Insert Mode`.

La manière la plus courante de faire cette transition est d'appuyer sur `i` en `Normal Mode` après avoir déplacé le curseur à l'endroit que nous allons éditer.

Il existe en fait de nombreuses autres façons d'entrer en `Insert Mode`, comme `o`, `O`, `a`, `A`, `I`, etc.

Trouvez-le dans la documentation : `:h Insert`, `:h i_<Esc>`, `:h o`, `:h O`, `:h a`, `:h A`, `:h I`.

### Qu'est-ce que le mode ligne de commande dans Vim ?

Le `Command-line Mode` est normalement un mode "de courte durée", que vous utilisez pour exécuter des "commandes Ex" (à ne pas confondre avec les "commandes" en `Normal Mode`).

Fait amusant : Vim est en fait une contraction de `Vi Improved` et il est basé sur un autre éditeur de texte nommé `[vi](https://en.wikipedia.org/wiki/Vi)`. Et `vi` est basé sur un éditeur de ligne nommé `[ex](https://en.wikipedia.org/wiki/Ex_(text_editor))`. `vi` et `ex` ont tous deux été développés par [Bill Joy](https://en.wikipedia.org/wiki/Bill_Joy).

Un autre fait amusant pour les utilisateurs de macOS : il n'y a que `Vim` sur macOS et la commande `vi` est liée symboliquement à `vim`. Notez également que la "commande Ex" en `Command-line Mode` est différente de la "commande" en `Normal Mode`.

Vous pouvez entrer en `Command-line Mode` en tapant `:` en `Normal Mode`. Par exemple, si vous exécutez les commandes ci-dessus pour voir la documentation, vous utilisez en fait le `Command-line Mode` dès que vous tapez `:`.

De même, appuyez sur `ESC` si vous souhaitez revenir en `Normal Mode`.

Trouvez-le dans la documentation : `:h Command-line`, `:h cmdline-lines`.

## Comment quitter Vim

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-169.png)
_documentation de `:h quit`_

Si vous regardez la documentation de `:h quit`, notez que `quit` est précédé de `:`. Cela signifie que `quit` est utilisé dans le `Command-line Mode`.

Pour entrer en `Command-line Mode`, nous devons d'abord nous assurer d'être en `Normal Mode`, puis simplement taper `:`. Maintenant que nous sommes en `Command-line Mode`, tapez simplement `quit` et appuyez sur `Enter` ou `return`.

Vous pouvez également remarquer le `:q` là, qui est en fait la version abrégée de la commande `:quit`. Cela dit, nous pouvons également quitter Vim en exécutant `:q`.

Il est mentionné, cependant, que cette commande échouera "lorsque des modifications ont été apportées et que Vim refuse d'abandonner le buffer actuel" (si vous vous souvenez encore, le buffer est simplement le(s) fichier(s) ouvert(s), rien de compliqué).

Dans ce cas, nous devons utiliser `:wq`, qui signifie "écrire et quitter". Vous pouvez trouver cela dans la documentation sous `:h :wq`.

`:x` est une autre commande qui fonctionne **presque de la même manière** que `:wq`. Selon `:h :x`, elle est "comme :wq, mais écrit uniquement lorsque des modifications ont été apportées".

La différence ici est que `:wq` sauvegardera le fichier que vous ayez apporté des modifications ou non. `:x` ne sauvegardera pas le fichier si vous n'avez apporté aucune modification. Ce qui compte ici est l'heure de modification d'un fichier, puisque `:wq` mettra à jour l'heure de modification mais pas `:x`.

Il arrive parfois que nous ne voulions pas conserver les modifications que nous avons apportées. À ce stade, nous avons besoin de la commande `:q!`. Le `!` est normalement appelé "bang", ce qui fait de `q!` quelque chose comme "quitter de force".

Notez bien que si vous utilisez cette méthode, vous PERDREZ toutes les modifications que vous avez apportées à ce fichier et il n'y a _presque_ aucun moyen de les récupérer.

## Comment résoudre les problèmes de sortie de Vim

### Que faire si je ne veux pas entrer en `Command-line Mode` ?

Pas de problème. En `Normal Mode`, vous pouvez également appuyer sur `ZZ` ou `ZQ` pour quitter Vim. Où `ZZ` est identique à `:x` et `ZQ` est identique à `:q!`.

Ici, `ZZ` et `ZQ` sont considérés comme des commandes du `Normal Mode` tandis que `:x` et `:q!` sont des commandes Ex.

### Que faire si `:wq` échoue ?

Cela est légitime puisque `:wq` peut échouer lorsque le fichier est en lecture seule ou que le nom du fichier est manquant.

Notez que lorsque le fichier est en lecture seule, Vim ne vous empêchera pas d'ouvrir et d'éditer le fichier. Vous pouvez également constater que `:wq!` ne fonctionnera pas non plus à ce moment-là. Vous pourriez finir par abandonner toutes les modifications avec `:q!` et ouvrir le même fichier précédé de `sudo` et faire les mêmes modifications une fois de plus.

Une chose que vous pourriez faire est de sauvegarder ce fichier dans un autre répertoire où vous avez la permission d'écriture, comme `~` ou même `/tmp`. Ensuite, déplacez-le dans le répertoire où vous n'avez pas la permission d'écriture.

Pour y parvenir, vous pouvez exécuter `:w ~/my-backup-file` qui sauvegardera ce fichier sous `~`. Ensuite, vous pouvez utiliser la commande `mv` pour déplacer ce fichier. Notez également que c'est ce que vous devez faire lorsque Vim se plaint que le nom du fichier est manquant.

Il existe une autre solution directement dans Vim. Vous pourriez exécuter cette commande : `:w !sudo tee %`. Ici, `!sudo` signifie exécuter la commande sudo dans votre environnement shell.

Par exemple, `:ls` listera tous les buffers dans Vim mais `:!ls` exécutera la commande `ls` à partir du shell et affichera le résultat. `tee` copie de l'entrée standard (a.k.a. `stdin`) vers la sortie standard (a.k.a. `stdout`). `%` fait référence au nom de fichier actuel.

Cela signifie que nous utilisons la commande `sudo` de l'environnement shell, copions le contenu du fichier actuel (note : version modifiée) de Vim, et redirigeons le contenu modifié vers le fichier (qui est référencé en utilisant le nom de fichier).

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-170.png)
_Avertissement de modification du contenu du fichier_

Vous remarquerez l'avertissement ci-dessus. Cet avertissement se produit parce que le contenu du fichier a été mis à jour dans l'environnement shell sans l'attention de Vim. Donc Vim considère cela comme un changement externe et vous informe de ce qui s'est passé.

Vous pouvez simplement appuyer sur `Enter` à ce moment-là puisque vous avez fait le changement externe intentionnellement.

Vous pouvez également remarquer que le contenu modifié du fichier s'affiche également au-dessus du message d'avertissement. Cela est attendu puisque cela provient du `stdout`. Si vous ne voulez pas le voir, vous pouvez faire `:w !sudo tee% >/dev/null`, ce qui supprimera le `stdout` de `tee`.

### Que faire si je suis perdu et dois forcer la fermeture ?

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-171.png)

Eh bien, si nous essayons de quitter en appuyant sur `control + c`, Vim nous montrera les informations ci-dessus. Mais vous pouvez toujours contourner cela par `Ctrl + Alt + Delete` sur Windows ou `Forcer à quitter...` sur macOS.

La prochaine fois que vous essayez d'ouvrir le même fichier à nouveau, vous _devriez_ voir ceci (ici j'utilise un fichier nommé `foo.txt` comme exemple) :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-173.png)
_fichier d'échange_

Ne paniquez pas – cela est attendu, puisque Vim essaie de vous aider à récupérer vos modifications précieuses que vous auriez pu perdre.

En vérifiant le répertoire, vous trouverez un fichier avec l'extension `.swp`. Il s'agit d'un fichier `swap` (documentation : `:h swap-file`) :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-174.png)
_fichier d'échange .swp_

Nous verrons ce qui suit si nous appuyons sur `R` pour récupérer :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-177.png)
_récupération .swp_

Après avoir appuyé sur `Enter`, vous remarquerez maintenant que les modifications que vous avez apportées précédemment sont de retour. Et après avoir terminé le processus de récupération, vous pouvez simplement supprimer le fichier `.swp` afin de ne plus voir l'erreur ci-dessus.

## **Conclusion**

Dans cet article, nous avons couvert quelques fondamentaux sur les modes de Vim et comment quitter Vim. Nous avons également appris à résoudre les problèmes courants lors de la sortie de Vim.

Merci d'avoir lu. Il y a beaucoup plus à apprendre en ce qui concerne Vim. Mais n'hésitez pas à explorer la documentation d'aide de Vim si vous souhaitez en savoir plus.