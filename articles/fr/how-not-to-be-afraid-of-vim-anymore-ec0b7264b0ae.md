---
title: Comment ne plus avoir peur de Vim
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-19T16:37:47.000Z'
originalURL: https://freecodecamp.org/news/how-not-to-be-afraid-of-vim-anymore-ec0b7264b0ae
coverImage: https://cdn-media-1.freecodecamp.org/images/0*idcJObABQVEH2BVq
tags:
- name: Productivity
  slug: productivity
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: vim
  slug: vim
seo_title: Comment ne plus avoir peur de Vim
seo_desc: 'By Neil Kakkar

  A curation of the most popular commands and how to use them

  If you’ve ever used Vim, you know how difficult it can get to reach the same speed
  as in a “normal” GUI editor. But once you do, the payoff is exponential — you get
  much more ...'
---

Par Neil Kakkar

#### Une sélection des commandes les plus populaires et comment les utiliser

Si vous avez déjà utilisé Vim, vous savez à quel point il peut être difficile d'atteindre la même vitesse que dans un éditeur GUI "normal". Mais une fois que vous y arrivez, les bénéfices sont exponentiels — vous devenez beaucoup plus efficace pour écrire du code. Bien sûr, ce n'est pas la raison principale de cet article.

La majorité du temps passe — ou devrait passer — à concevoir une solution à votre problème, et non à le coder réellement ; optimiser la vitesse à laquelle vous codez semble donc être la dernière chose sur laquelle se concentrer. Ce n'est pas un point de levier.

Cet article a pris forme pour une autre raison : la non-existence des interfaces graphiques sur les machines accessibles via SSH. Que faire maintenant ? Sur toute machine où vous avez accès au terminal et souhaitez éditer un fichier, vous avez 2 options :

1. Abandonner, essayer de fermer Vim
2. Maîtriser Vim

Se contenter de copier `[vimtutor](https://superuser.com/questions/246487/how-to-use-vimtutor)` n'aiderait personne. Ici, j'utilise donc une approche différente : j'ai compilé les meilleures fonctionnalités de Vim que j'utilise quotidiennement en tant que développeur logiciel, accompagnées de moyens mnémotechniques pour les retenir. Cela contient presque tout ce dont vous avez besoin pour l'édition et l'écriture régulières.

### Les bases

Restez avec moi, cela ne concerne pas les commandes mais l'idéologie qui les sous-tend !

#### Modes

Vim a 2 modes :

* Normal (mode Commande)
* Insertion (mode Édition)

Lorsque vous ouvrez Vim, vous commencez en mode normal. Pour revenir en mode normal à tout moment, appuyez sur la touche `ESC`. Le mode normal est celui où vous pouvez émettre des commandes : la liste des commandes est sans fin !

Il existe de nombreuses façons d'entrer en mode insertion. La plus intuitive est d'utiliser la commande `i`. `i` pour insertion. En mode normal, appuyez sur `i` et vous entrerez en mode insertion. Maintenant, tout ce que vous tapez apparaîtra dans l'éditeur. L'un des plus grands obstacles est surmonté.

Le modèle mental — pour comprendre l'idée : Puisqu'il n'y a pas d'interface graphique, il n'y a pas de concept de clics de souris. Il n'y a pas de menu pour choisir des options, il n'y a pas de clic droit. Par conséquent, vous avez besoin d'un moyen d'obtenir tout cela sur le clavier — votre seule source d'entrée.

Avoir deux modes permet d'y parvenir ! Vous pouvez considérer le mode Normal (Commande) comme la barre de menu et la souris surpuissants, tandis que le mode Insertion est comme le mode normal dans les éditeurs GUI (où ce que vous tapez apparaît à l'écran).

#### Mots

Pour Vim, les mots signifient presque la même chose que pour nous — un ensemble de caractères séparés par des espaces ou des caractères spéciaux. La commande est `w`.

#### Anatomie des commandes

Les commandes dans Vim suivent un schéma défini. Connaître cela aide à placer chaque commande dans une certaine catégorie de commandes, construisant ainsi un meilleur modèle mental.

Les commandes ressemblent à ceci :

[action] <nombre> [mouvement]

L'action est ce que vous voulez faire,

Le nombre est le nombre de fois que vous voulez faire cette action,

Le mouvement est la portée de cette action.

Le mouvement est la portée. Un exemple rendra cela plus clair. Supposons que nous voulons supprimer les 3 mots suivants, en commençant par le curseur. Ici, l'action est supprimer, le nombre est 3 et le mouvement est un mot. L'action de commande pour supprimer est `d`.

Ainsi, nous obtenons la commande finale : `d3w` — supprimer les 3 mots suivants.

Ometre le nombre revient à une fois.

Les mouvements peuvent être utilisés sans action, ce qui revient par défaut à la navigation. Ainsi, taper `w` en mode commande déplacera le curseur d'un mot vers l'avant.

Nous sommes maintenant bien équipés pour commencer à apprendre les commandes elles-mêmes (et une gamme de mouvements à utiliser avec elles).

### Commandes utiles

#### Comment fermer Vim

D'abord, nous ne voulons pas rester bloqués dans Vim sans plan de sortie. Ayez toujours une stratégie de sortie.

`:q` pour quitter

`:q!` pour forcer la fermeture

`:wq` pour sauvegarder et quitter

#### Actions de commande

`d` : supprimer

`i` : insérer

`p` : coller

`y` : copier

`x` : couper

`u` : **annuler**

`di` : supprimer à l'intérieur*, `yi` : copier à l'intérieur*

`v` : sélection visuelle

`/` : rechercher

`%` : correspondance de parenthèses, les développeurs se réjouissent !

`:s` : substituer ! En d'autres termes, rechercher-remplacer surpuissant

Puisque les actions sur la ligne entière sont très fréquentes, les développeurs de Vim ont créé un nouveau raccourci pour elles — omettant le besoin d'ajouter un mouvement. Répétez l'action pour l'appliquer sur la ligne entière. Par exemple :

Pour supprimer la ligne actuelle : `dd`

Pour copier la ligne actuelle : `yy`

Pratique, n'est-ce pas ?

#### Mouvements de commande

Les mouvements vont avec les actions comme nous l'avons vu, et les mouvements disponibles changent avec l'action. Cependant, certains mouvements sont assez uniformes.

`w` : début du mot suivant (nous avons déjà vu cela !)

`e` : fin du mot actuel

`b` : début du mot précédent

Touches fléchées / <h,j,k,l> : mouvements respectifs. h,j,k,l sont un substitut aux touches fléchées, et la source de vitesse dans Vim : vous n'avez pas à éloigner vos mains de la partie de frappe du clavier.

`$` : fin de ligne

`0` : début de ligne

`G` : fin de fichier

`nG` : sauter à la ligne numéro `n`

`)` : sauter en avant d'une phrase

`}` : sauter en avant d'un paragraphe

Cela aide à mieux visualiser :

```
           ge      b          w                             e
           <-     <-         --->                          --->
    This is-a line, with special/separated/words (and some more). ~
       <----- <-----         -------------------->         ----->
         gE      B                   W                       E
```

Armés de ces actions et mouvements, nous pouvons créer la plupart des commandes de base dans Vim. Voici une liste de 8 fonctions quotidiennes. Trouvez la commande pour les réaliser !

1. Supprimer les 3 lignes suivantes (y compris la ligne actuelle)
2. Copier le mot actuel — le curseur est au début du mot
3. Copier le mot actuel — il contient des caractères spéciaux — le curseur est au milieu du mot
4. Naviguer vers le bas de 10 lignes
5. Supprimer tout ce qui se trouve à l'intérieur des accolades
6. Monter de 2 paragraphes
7. Coller le texte précédemment sélectionné 5 fois.
8. Éditer là où se trouve le curseur : « I can Vim now! »

...

Attendez...

...

Voici les solutions :

1. `d3j`
2. `yw`
3. `yiW` : le copier à l'intérieur sert à copier à l'intérieur, et `W` est ce qu'il faut copier (mot actuel). Cela est incroyablement utile, vous pouvez utiliser toutes sortes de combinaisons avec `inside` !
4. `10j`
5. `di}` : comme pour le #3.
6. `2{` : cela était légèrement plus intuitif. `{` est pour monter d'un paragraphe, `}` est pour descendre d'un paragraphe
7. `5p` : rappelez-vous les nombres optionnels de l'anatomie des commandes ? Ils peuvent être utilisés presque partout
8. `i` `I can Vim now!` : `i` est pour entrer en mode insertion, puis vous pouvez travailler comme dans un éditeur "normal"

Très bien, vous l'avez fait ! Félicitations, cela suffit pour explorer Vim par vous-même, aventurier. Le tutoriel est terminé. Bonne chance.

Si quelqu'un vous demande à propos de Vim, vous pouvez faire mieux que d'utiliser ce mème. Expliquez-le-leur, ou dirigez-les ici ;)

![Image](https://cdn-media-1.freecodecamp.org/images/QkqAG7RCyNb08rhtBYp24mYBdLK5UoHRDhII)

> *Note : Ceci est mon modèle de Vim. Ce n'est pas exactement ainsi que les choses fonctionnent en interne. Si vous consultez la documentation ( :help user-manual ), vous verrez que d est la commande, et le mouvement est iw, ou « inside word ». Il y a une déviation.  
> Pourquoi ? — parce que je pense que cela aide à mieux expliquer.

### Bonus

Voici quelques commandes supplémentaires qui s'avèrent utiles :

#### Écran divisé

`:vsplit <nomdefichier>`

Crée une division verticale. Vous permet de copier-coller d'un écran à l'autre.

Pour naviguer entre les divisions d'écran : `<ctrl-w> <ctrl-w>`

Alternativement, vous pouvez utiliser les touches fléchées / `hjkl` comme suit :

`<ctrl-w> h` pour aller à l'écran précédent.

Vous pouvez fermer les fenêtres comme vous le faites normalement (`:q`), ou —

`:only` — pour fermer toutes les autres fenêtres

#### Plusieurs onglets

`:tabnew <nomdefichier>` ouvre un nouveau fichier dans un nouvel onglet dans Vim

`:tabn` pour aller à l'onglet suivant (ou `:gt`)

`:tabp` pour aller à l'onglet précédent (ou `:gT`)

Encore une fois, vous pouvez copier-coller d'un onglet à l'autre.

Vous pouvez également mapper cette combinaison à une touche de votre choix !

J'ai essayé `<Ctrl-Tab>`, mais c'est déjà réservé. Quel dommage. Au lieu de cela, nous avons :

```
map <C-t><left> :tabp<cr>
map <C-t><right> :tabn<cr>
```

Ce qui signifie que <Ctrl-t> suivi de la touche fléchée gauche ou droite vous permettra de basculer entre les onglets.

Comment ai-je exactement trouvé ce mapping ? [Consultez ce tutoriel](http://vim.wikia.com/wiki/Mapping_keys_in_Vim_-_Tutorial_(Part_1)).

Autres articles de cette série :

* [Comment ne plus avoir peur de Python](https://medium.freecodecamp.org/how-not-to-be-afraid-of-python-anymore-b37b58871795)
* [Comment ne plus avoir peur de GIT](https://medium.freecodecamp.org/how-not-to-be-afraid-of-git-anymore-fe1da7415286)

Vous avez aimé cela ? [Ne manquez plus un article — abonnez-vous à ma liste de diffusion !](http://neilkakkar.com/subscribe/)