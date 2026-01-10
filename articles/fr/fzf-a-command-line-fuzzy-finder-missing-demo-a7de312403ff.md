---
title: Pourquoi vous devriez utiliser fzf, le rechercheur flou en ligne de commande
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-19T12:25:50.000Z'
originalURL: https://freecodecamp.org/news/fzf-a-command-line-fuzzy-finder-missing-demo-a7de312403ff
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LTR424sh7y8E8rUzsUnFsQ.gif
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Pourquoi vous devriez utiliser fzf, le rechercheur flou en ligne de commande
seo_desc: 'By Alexey Samoshkin

  Missing demo found

  In this tutorial, I’ll help you take your command line habits to a next level with
  fzf . Start searching files like a pro. Learn less known features, like changing
  directory, searching through a command history,...'
---

Par Alexey Samoshkin

#### Démo manquante trouvée

Dans ce tutoriel, je vais vous aider à passer vos habitudes de ligne de commande au niveau supérieur avec `fzf`. Commencez à rechercher des fichiers comme un pro. Apprenez des fonctionnalités moins connues, comme changer de répertoire, rechercher dans l'historique des commandes, trouver le nom d'hôte pour se connecter en SSH, tuer un processus, avoir un aperçu instantané des fichiers avec surlignage syntaxique, et plus encore...

![Image](https://cdn-media-1.freecodecamp.org/images/iXHjTDv9FFfDA2fnIvojr2s5AA3y0PNvBFgm)
_démo rapide_

Aujourd'hui, je vais vous parler d'un outil qui peut diviser votre vie technologique en parties "avant" et "après". Croyez-moi, ce n'est pas une hyperbole. Rencontrez [fzf](https://github.com/junegunn/fzf), qui signifie "fuzzy finder". Comme le définit, **c'est un rechercheur flou polyvalent en ligne de commande**. Cela ne semble pas très descriptif et attrayant pour ceux qui en entendent parler pour la première fois. Mais c'est un projet très populaire, classé à environ 21 000 étoiles [sur Github](https://github.com/junegunn/fzf). Il est donc temps de lever le brouillard et d'obtenir une vision plus approfondie.

Cet article accompagne [mon récent screencast](https://www.youtube.com/watch?v=qgG5Jhi_Els) sur le sujet. Donc, si vous êtes une personne qui apprend en regardant, consultez-le. Sinon, consultez-le aussi ?, car des outils comme `fzf` sont mieux introduits avec une démo en direct plutôt qu'avec des tonnes de texte.

Comme la page du projet `fzf` n'a pas encore de vidéo de démo, j'ai appelé cet article "démo manquante trouvée". Mais maintenant, cette vidéo a déjà été intégrée dans le dépôt `fzf` et est devenue une partie du [readme du projet](https://github.com/junegunn/fzf#demo).

### Recherche de fichiers

Les personnes habituées à un environnement en ligne de commande sont probablement familières avec le concept de filtres Unix. Cela consiste à composer plusieurs utilitaires indépendants ensemble dans un pipeline pour produire la sortie souhaitée étape par étape. Par exemple, ce pipeline produit une liste de chaînes :

```
$ yes | head -10 | awk '{ print NR, NR % 2 == 0 ? "even" : "odd" }'
```

```
1 odd2 even3 odd4 even5 odd6 even7 odd8 even9 odd10 even
```

Chaque programme agit comme un filtre. En termes simples, `fzf` est juste un autre filtre Unix. Il lit les lignes depuis `stdin`, lance un dialogue de recherche interactif, et écrit finalement les éléments sélectionnés vers `stdout`. Le point clé et la différence avec des outils comme GNU `find`, c'est son dialogue de recherche interactif qui filtre les éléments instantanément au fur et à mesure que vous tapez.

![Image](https://cdn-media-1.freecodecamp.org/images/EATLQiPcYRHl0IpEhyE0aups3iUThho5j7Vu)
_"fzf" en tant que filtre unix interactif_

Cela peut ne pas sembler très pratique jusqu'à présent, mais le cas d'utilisation principal de `fzf` est de rechercher des fichiers en ligne de commande. Avec la correspondance floue et le retour instantané, vous n'êtes qu'à quelques caractères de trouver le bon fichier, peu importe à quel point il est profondément perdu dans la hiérarchie des répertoires. Pas besoin de revenir à votre gestionnaire de fichiers, de parcourir la hiérarchie des répertoires, de copier le chemin d'un fichier et de le coller dans le shell. Comparez les workflows "gestionnaire de fichiers" vs "fzf" ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/YrD36K2ENGCVEPlslYvMzSwTG1xTsZRiIlHS)
_comparaison fzf vs gestionnaire de fichiers_

`fzf` supporte la correspondance floue, donc vous pouvez simplement taper plusieurs caractères à la suite et il correspondra aux lignes contenant ces caractères dispersés dans la chaîne. Alternativement, préfixez un terme de recherche avec une apostrophe, comme `'string`, pour opter uniquement pour des correspondances exactes, ou exécutez `fzf --exact`.

![Image](https://cdn-media-1.freecodecamp.org/images/3-ePamsGZmgtdsmzIF3IbbZJCTUkNslI-BDk)
_correspondance floue vs exacte_

Il ne supporte pas les expressions régulières ou les motifs glob, donc le motif `*.sh` ne fonctionnerait pas. Mais gardez-le simple — la productivité et la vitesse sont votre objectif aujourd'hui. Vous n'avez pas de temps à perdre pour composer et taper des expressions régulières correctes. Au lieu de cela, tapez simplement plusieurs mots, ou même des parties de mots, délimités par un espace, et cela couvrira >90% des cas d'utilisation. Pour les 10% restants, utilisez ^ et $ pour correspondre au début et à la fin de la chaîne respectivement, et utilisez ! pour négocier la correspondance.

![Image](https://cdn-media-1.freecodecamp.org/images/kV5hgH2rvYEEBRMWUnjsDwBIL7LN9mU3C5E6)
_syntaxe de correspondance fzf_

Imprimer les fichiers sélectionnés sur une ligne de commande n'est pas très utile, donc généralement la recherche est combinée avec une action supplémentaire. Par exemple, vous pouvez l'ouvrir avec Vim, ou transmettre les éléments sélectionnés au programme suivant.

```
# Ouvrir le fichier dans Vim
vim -o `fzf`
```

```
# Imprimer les infos pour chaque fichier sélectionné
fzf | xargs ls -l
```

### Complétion floue pour bash et zsh

Pour le rendre plus pratique, la complétion floue peut être déclenchée si le mot avant le curseur se termine par la séquence de déclenchement qui est par défaut `**`. Par exemple, tapez `vim ~/path/**` et appuyez sur `TAB`. Voilà, fzf intervient !

![Image](https://cdn-media-1.freecodecamp.org/images/PvhRo5LV4UvRpN8gCoo-1tJ0s5Imyal0Hjbb)
_Complétion floue à double étoile_

La séquence `**` déclenche le rechercheur `fzf` et ressemble à `*` qui est utilisé pour l'expansion native du shell. À un moment donné, vous pourriez même oublier la présence de `fzf` et avoir l'impression que c'est une fonctionnalité native du shell.

[Le format est le suivant](https://github.com/junegunn/fzf#fuzzy-completion-for-bash-and-zsh), où `FUZZY_PATTERN` est facultatif.

```
COMMAND [DIRECTORY/][FUZZY_PATTERN]**<TAB>
```

Si vous n'aimez pas la séquence `**`, vous pouvez utiliser des raccourcis clavier. `CTRL+T` déclenche `fzf` et colle le fichier sélectionné sur la ligne de commande, tandis que `ALT+C` change vers le répertoire sélectionné.

### Changer de répertoire

D'accord, assez parlé de la recherche de fichiers. Parlons d'autres applications utiles. Changer de répertoire de travail est une opération si courante. Mais néanmoins, je suis toujours un peu bloqué en essayant de me rappeler et de taper le bon chemin de répertoire, en faisant plusieurs erreurs en cours de route. Cela ralentit mon rythme. Même les complétions zsh ne compensent pas cela. Mais avec `fzf`, changer de répertoire est un jeu d'enfant, peu importe à quel point il est profond et éloigné. Il suffit de taper `cd **` et vous y êtes presque.

![Image](https://cdn-media-1.freecodecamp.org/images/t8dzyyZ0vMSFwpFU7PgKtfH86AhM3C6fIvoH)
_changer de répertoire est un jeu d'enfant_

Remarquez que pendant que fzf indexe votre arbre de répertoires, vous pouvez commencer à rechercher immédiatement. Changer de répertoire est mon cas d'utilisation préféré, et la correspondance floue excelle vraiment ici. Cela nécessite de votre part le même effort pour changer de répertoire, qu'il soit à un niveau de profondeur ou à dix niveaux de profondeur.

Le raccourci `ALT+C` est une autre façon de déclencher `fzf` en mode changement de répertoire.

### Historique des commandes

Vous utilisez peut-être le raccourci clavier `Ctrl+R` pour rechercher dans votre historique de commandes. Super, mais que diriez-vous de le supercharger avec le rechercheur flou ? Regardez et comparez.

![Image](https://cdn-media-1.freecodecamp.org/images/y2wgBR9TUloRfQVgpmChaTtTrrjHfrQR374y)
_Recherche dans l'historique des commandes_

Il colle l'élément sélectionné sur la ligne de commande, afin que vous puissiez le modifier davantage.

### Rechercher le nom d'hôte pour se connecter en SSH

Si vous êtes un développeur backend et que vous travaillez avec plusieurs serveurs distants, vous pourriez apprécier la combinaison `ssh+fzf`. Utilisez la même séquence de déclenchement à double étoile et tapez `ssh **`. Elle extrait les adresses IP et les noms d'hôte récemment utilisés de votre `~/.ssh/config` et affiche un rechercheur interactif.

![Image](https://cdn-media-1.freecodecamp.org/images/-khneINrdlXrPo00zg2ZcZc4jrnrVOKZSpUn)
_combo "fzf + ssh"_

### Envoyer un signal à un processus

Parfois, nous voulons envoyer un signal à un processus, mais d'abord nous devons obtenir son PID par nom. Habituellement, on utilise `pgrep <process_name>` pour résoudre le PID suivi d'un `kill <process_pid>` en se référant à ce PID. Avec fzf, vous pouvez combiner les deux étapes. Tapez `kill <TAB>` et fzf intervient en listant tous vos processus. Pas besoin de passer à un moniteur de processus dédié, comme "Activity Monitor" sur Mac.

![Image](https://cdn-media-1.freecodecamp.org/images/BvbjoYPcKfZPTGuEV2XyhTfelQ69EIA4EP2-)
_Trouver un processus et envoyer un signal_

### Prévisualiser les fichiers pendant la recherche

Supposons que vous recherchez des fichiers, mais parfois le nom du fichier lui-même ne vous dit pas assez. Vous pourriez donc vouloir jeter un coup d'œil au contenu d'un fichier pour prendre une décision. `fzf` vous couvre également ici.

![Image](https://cdn-media-1.freecodecamp.org/images/l3wJ44GjRyqJN8iyiDBmrGIH8EdpYwZZergy)
_Fenêtre de prévisualisation_

Par défaut, j'ai la fenêtre de prévisualisation désactivée, mais je l'active lorsque je veux jeter un coup d'œil aux fichiers. De plus, je l'ai améliorée avec une sortie colorée et un surlignage syntaxique en utilisant [bat](https://github.com/sharkdp/bat) comme commande de prévisualisation.

### Personnalisation

Il existe deux principales façons de personnaliser la version standard de `fzf` :

* Changer le comportement du dialogue de recherche (fenêtre de prévisualisation, raccourcis clavier, dimensions, actions personnalisées, etc). Voir la variable d'environnement `FZF_DEFAULT_OPTS`.
* Changer le backend de recherche sous-jacent. Par défaut, il utilise l'utilitaire GNU `find`, mais vous pouvez passer à des outils plus avancés comme [fd](https://github.com/sharkdp/fd) ou [ripgrep](https://github.com/BurntSushi/ripgrep). Premièrement, c'est plus rapide que l'utilitaire `find` standard. Deuxièmement, ces outils respectent les règles `.gitignore`, donc vous n'obtenez pas de fichiers `node_modules` ou `.git` dans vos résultats de recherche. Vous [pouvez également utiliser](https://github.com/junegunn/fzf#git-ls-tree-for-fast-traversal) `git ls-tree` pour lister les fichiers lorsque vous êtes dans un dépôt Git. Voir la variable d'environnement `FZF_DEFAULT_COMMAND`.

La configuration est effectuée via les variables d'environnement. Voici un extrait de ma configuration. Je ne suis pas sûr qu'il fonctionnerait tel quel si copié-collé, il manque probablement d'autres dépendances. Mais cela donne simplement une idée de l'apparence de la configuration.

### Fzf et Vim

Jusqu'à présent, nous n'avons vu que l'utilisation en ligne de commande. Mais `fzf` est également fourni en tant que [plugin Vim](https://github.com/junegunn/fzf.vim). Et croyez-moi, si vous êtes un utilisateur de Vim, cela vaut la peine de l'ajouter à votre `vimrc`. L'utilisation de Vim est hors du cadre de cet article, sinon personne ne le lirait ?. Mais j'en parle en détail dans la deuxième partie de m[a vidéo,](https://www.youtube.com/watch?v=qgG5Jhi_Els) également liée au début de l'article.

Si vous êtes impatient, voici un petit extrait pour attirer votre attention. Utilisez la commande `:grep` pour une recherche de texte dans tout le projet, ouvrez les correspondances dans la fenêtre `fzf` en mode plein écran, filtrez davantage les correspondances dans `fzf`, et sautez à la correspondance sélectionnée. Et n'oubliez pas l'aperçu instantané du fichier à la position précise de la ligne. C'est génial, n'est-ce pas ?

![Image](https://cdn-media-1.freecodecamp.org/images/ADmJjvj-Jy35K2UAyAfpnUx8mi-1MqdRl-IJ)
_fzf ❤️ vim_

### Conclusion

J'espère que vous êtes impressionné par la superbe utilité de [fzf](https://github.com/junegunn/fzf). Il y a des chances que vous soyez déjà prêt à l'installer et à l'essayer.

Gardez à l'esprit que `fzf` n'est pas seulement pour la recherche de fichiers, bien que ce soit sa fonctionnalité principale. Comme vous pouvez le voir, "**recherche + action**" est un principe général, mais il est abstrait et suffisamment puissant pour fonctionner avec tout type de liste : fichiers, répertoires, processus, noms d'hôte, etc. Souvenez-vous au début de cet article — **fzf est juste un filtre Unix**. Libérez votre imagination, nourrissez-le avec n'importe quelle liste, et adaptez-le à vos propres besoins. Vous pourriez trouver de l'inspiration dans une [richesse d'exemples](https://github.com/junegunn/fzf/wiki/examples).

Au fait, appréciez la supériorité de la philosophie Unix. `fzf` est un excellent exemple de programme qui adhère à ces principes.

* laissez le programme faire une chose et la faire bien (principe de responsabilité unique)
* rendez-le suffisamment abstrait pour être agnostique des détails ou types de données irrelevants
* composez des programmes individuels séparés en utilisant des interfaces bien définies et standard.

Restez fidèle à ces principes dans votre carrière de développement logiciel. Connaître les principes fondamentaux qui sous-tendent la naissance et la mort rapides de multiples outils, langages et frameworks est ce qui différencie les développeurs professionnels des amateurs.

### Ressources

junegunn/fzf: Un rechercheur flou en ligne de commande — [https://github.com/junegunn/fzf](https://github.com/junegunn/fzf)

Vim universe. fzf — rechercheur flou en ligne de commande — YouTube — [https://www.youtube.com/watch?v=qgG5Jhi_Els](https://www.youtube.com/watch?v=qgG5Jhi_Els)

Ma chaîne YouTube. Il n'y a que quelques vidéos, car je fais mes premiers pas dans la création de screencasts. Soyez patient, je promets de faire plus de vidéos. Alexey Samoshkin — YouTube — [https://www.youtube.com/channel/UCfju8u-YOpNMO4CbyzIsc9Q](https://www.youtube.com/channel/UCfju8u-YOpNMO4CbyzIsc9Q).

sharkdp/fd: Une alternative simple, rapide et conviviale à 'find' — [https://github.com/sharkdp/fd](https://github.com/sharkdp/fd)

BurntSushi/ripgrep: ripgrep recherche récursivement des répertoires pour un motif regex — [https://github.com/BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)

junegunn/fzf.vim: fzf vim — [https://github.com/junegunn/fzf.vim](https://github.com/junegunn/fzf.vim)