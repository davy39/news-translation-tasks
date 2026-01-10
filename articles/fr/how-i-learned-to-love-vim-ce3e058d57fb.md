---
title: Comment j'ai appris à aimer Vim
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-29T13:51:38.000Z'
originalURL: https://freecodecamp.org/news/how-i-learned-to-love-vim-ce3e058d57fb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BPkK5FHiS6rXsygxNoO2XA.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment j'ai appris à aimer Vim
seo_desc: 'By Sanchit Gera

  I’ve had a bitter-sweet relationship with [Vim](http://(https://vim.sourceforge.io/about.php)
  for a long time.

  Over the last couple of years, I tried to learn Vim on several occasions. Each time,
  I ended up abandoning it. Instead, I w...'
---

Par Sanchit Gera

J'ai eu une relation à la fois amère et douce avec [Vim](http://(https://vim.sourceforge.io/about.php) pendant longtemps.

Au cours des deux dernières années, j'ai essayé d'apprendre Vim à plusieurs reprises. Chaque fois, j'ai fini par l'abandonner. Au lieu de cela, je revenais à mon éditeur de texte 'principal' (généralement [Atom](https://atom.io/)).

Mais pendant quelques semaines, je me suis retrouvé incapable d'utiliser Atom. Cela était dû à un [problème de connectivité obscur](https://github.com/atom/atom/issues/2456). Cela rendait mon installation complètement inutile sur les connexions à distance.

Après être passé par les cinq étapes du deuil, j'ai décidé de me lancer et d'essayer (encore une fois) d'apprendre Vim. Cette fois, je me suis forcé à utiliser Vim, et rien que Vim.

Je sais — j'aurais pu facilement passer à un éditeur plus intuitif comme [Sublime](https://www.sublimetext.com/). Ou j'aurais même pu utiliser un IDE complet comme [IntelliJ](https://www.jetbrains.com/idea/).

Au lieu de cela, je me suis dit 'pourquoi pas'. Voici quelques-unes des choses que j'ai apprises.

![Image](https://cdn-media-1.freecodecamp.org/images/28BV5wXCwaCnAKGpyPFtgoZKCKTYqubQpH6o)
_Cela prendrait vraiment beaucoup de malchance...

### Apprendre les bases

Au cas où ce serait nouveau pour vous, Vim est un éditeur de texte apparemment archaïque. Ses racines remontent à un programme appelé Vi, qui est apparu dans les années 1970.

Une partie de l'attrait de Vim — et de son irritation — est due au fait qu'il est conçu pour fonctionner entièrement avec votre clavier. Après tout, les interfaces graphiques point-et-clic n'étaient pas vraiment une chose à l'époque où Vi a été conçu.

Vim utilise plutôt des **modes**. Il y a deux modes principaux qui peuvent être utilisés :

* Mode normal : c'est le mode que vous utilisez lorsque vous naviguez dans vos fichiers, ou que vous les éditez/manipulez. C'est le mode pour faire tout ce qui ne nécessite pas de taper du nouveau contenu. La plupart des commandes Vim sont entrées dans ce mode.
* Mode insertion : le mode insertion permet la saisie de nouveau texte. Dans ce mode, Vim se comporte plus comme un éditeur de texte 'normal', comme Atom ou Sublime. Sans l'utilisation d'une souris, bien sûr.

D'autres modes existent également dans Vim. Un exemple est le mode visuel, pour sélectionner de grands morceaux de texte. Typiquement, ces modes sont utilisés beaucoup moins fréquemment.

Vim est normalement utilisé dans un émulateur de terminal. Cependant, des distributions autonomes existent. Il est disponible sur pratiquement tous les systèmes Unix et Linux. Le grand-père de Vim, Vi, fait partie de la spécification UNIX. Il est donc préinstallé sur tous les systèmes conformes.

### Composabilité

La 'composabilité' est largement ce qui rend Vim différent des autres éditeurs. Elle donne à Vim son propre langage spécial.

Elle introduit la notion de **noms** et de **verbes** dans le contexte de l'édition et de la manipulation de texte.

Les verbes décrivent les actions que vous pouvez entreprendre (comme supprimer, changer, déplacer).

Les noms décrivent ce qui est affecté (généralement des mots, des lignes ou des endroits dans le texte).

Certains des noms/verbes couramment utilisés incluent :

```
Verbes d: supprimerc: changer (écraser)y: copier (yank)>: indenter<: désindenter
```

```
Actionsh,j,k,l: gauche, bas, haut, droitew: mot suivantb: mot précédent0: début de ligne$: fin de lignei: à l'intérieur (en excluant le caractère suivant)a: autour (en incluant les caractères encadrants)
```

Cette liste n'est pas exhaustive. Il existe des tonnes et des tonnes de raccourcis clavier disponibles. Mais vous pouvez accomplir beaucoup avec seulement les plus basiques. L'idée est d'enchaîner des combinaisons de noms, de verbes et parfois de nombres. Cela vous permet de créer des **actions** distinctes pour manipuler le texte selon vos besoins.

Par exemple, pour **s**upprimer un **m**ot, vous tapez la combinaison de touches `dw`.

Pour **s**upprimer **2 m**ots à partir de la position actuelle, vous tapez `d2w`.

Pour supprimer de la position actuelle jusqu'à la fin de la ligne, vous tapez `d$`.

Pour **s**upprimer tout ce qui se trouve **à l'intérieur** d'une paire de parenthèses, vous taperiez `di(`. Et ainsi de suite.

Cette méthode de travail peut ne pas sembler valoir la peine. Mais si vous vous forcez à utiliser les combinaisons tous les jours, elles deviendront une seconde nature. Après un certain point, la vitesse que vous gagnez en réduisant le nombre de frappes nécessaires pour faire une certaine édition est absolument passionnante. Plus sur cela ensuite.

### Vim est addictif

Oui, je sais. C'est un cliché. Mais suivez-moi.

![Image](https://cdn-media-1.freecodecamp.org/images/FNVaLYw0fzefejUZVkitBXp9cWGYmrXQkomm)

Vim a une courbe d'apprentissage notoire. Mais une fois que vous avez passé l'étape où vous maudissez constamment votre écran d'ordinateur, utiliser Vim est en fait assez amusant.

Apprendre à utiliser les commandes cryptiques de Vim vous permet de voler à travers le processus d'édition de fichiers. Après un certain temps, il semble presque faux de lever les doigts de la rangée de base du clavier, ou même d'utiliser la souris !

Après seulement un mois, je me surprends à manquer du système de navigation de Vim et d'autres raccourcis en utilisant mon ordinateur régulièrement.

En fait, à un moment donné, j'ai envisagé d'expérimenter avec [cette extension](https://chrome.google.com/webstore/detail/vimium/dbepggeogbaibhgnhhndojpepiihcmeb?hl=en) pour activer les raccourcis clavier de Vim lors de la navigation sur le web. Je sais !

Heureusement, la communauté des programmeurs reconnaît cela. La plupart des éditeurs de texte grand public ont un moyen d'activer les raccourcis clavier de Vim. Cela sort les 'Vimmeurs' de leur misère en leur donnant le meilleur des deux mondes.

### Donner une chance à Vim

La clé pour s'améliorer avec Vim est de simplement ne pas utiliser autre chose. Au lieu de cela, vous devriez vous forcer à faire tout à la manière de Vim.

Par exemple — lors de l'édition de fichiers dans Vim, essayez de ne pas revenir à vos anciennes habitudes. La plupart des gens, lorsqu'ils commencent, essaient de rester aussi loin que possible du 'mode normal'.

Au lieu de cela, ils essaient de passer autant de temps que possible en 'mode insertion'. Dans ce mode, il est facile de se sentir plus à l'aise. Il vous permet de vous en tirer en éditant votre fichier sans apprendre quoi que ce soit de nouveau. Mais c'est une erreur.

Si vous êtes vraiment intéressé à apprendre comment faire fonctionner Vim pour vous, vous devez faire un effort. Cela signifie prendre le temps de trouver la 'bonne' façon de faire quelque chose.

Si vous vous surprenez à répéter des frappes encore et encore pour accomplir une tâche, **arrêtez-vous**. Il est probable qu'il existe une meilleure façon de faire ce que vous essayez de faire.

Recherchez sur Google. Mémorisez-le. Ajoutez-le à votre arsenal. Il est beaucoup plus facile d'apprendre de nouvelles commandes de cette manière, par rapport à la lecture d'une liste de commandes et en espérant que vous aurez besoin d'en utiliser une.

Après quelques jours, vous pouvez développer un sens intuitif de quand vous gaspillez des frappes. Écoutez votre intuition.

### Apprécier (?) les éditeurs modernes

Une autre grande raison pour laquelle beaucoup de gens évitent Vim est la nature apparemment 'minimaliste' de tout cela.

Par défaut, Vim ne vient avec aucun plugin ou fonctionnalités agréables. Et ce que Vim considère comme une fonctionnalité 'agréable' est probablement très différent de ce que les programmeurs habitués aux IDE modernes considéreraient comme 'agréable'.

Vim vient avec une coloration syntaxique minimaliste (qui est désactivée par défaut). Il n'y a pas de numérotation des lignes (encore une fois, cela doit être activé séparément).

Pas de surprise, alors, que des choses comme :

* l'intégration Git par défaut
* la complétion de code 'au fur et à mesure'
* la complétion automatique des crochets
* les extraits de code
* les schémas de couleurs personnalisés

... ne viennent pas préinstallées avec Vim.

Cela peut sembler être un énorme désavantage — surtout pour les programmeurs habitués à développer dans des IDE puissants qui font beaucoup de travail lourd. Beaucoup viennent installés avec un tas de plugins et d'extensions conçus spécifiquement pour rendre votre flux de travail plus efficace.

Et il y a un certain mérite à cet argument. Vim a ses limitations.

Pourtant, d'un autre côté — même si vous appréciez ce que les IDE modernes fournissent et le travail qui va dans leur construction — vous réalisez également que la plupart des IDE (et même des éditeurs modestes comme Atom) apportent avec eux beaucoup de bloat.

Les IDE avancés sont remplis de fonctionnalités qui sont rarement utilisées par les utilisateurs moyens.

Apprendre à utiliser Vim efficacement est en partie un exercice pour déterminer quels plugins sont absolument critiques pour votre productivité. La clé est de construire un éditeur uniquement adapté à vos besoins et à votre flux de travail.

Dans de nombreux cas, l'utilisation d'un IDE complet a parfaitement du sens. Les fonctionnalités avancées peuvent largement l'emporter sur les avantages que vous obtenez en utilisant Vim.

Mais c'est quelque chose que vous devez déterminer vous-même.

Malgré sa nature minimaliste, Vim dispose d'un écosystème de plugins florissant.

Vim a des plugins pour presque tout ce que vous pouvez faire avec d'autres éditeurs. Vous devez simplement déterminer ceux dont vous avez besoin.

Ce qui m'a surpris, c'est la distance que je peux parcourir avec seulement une poignée de plugins. Ma configuration Vim comprend actuellement environ cinq ou six modules complémentaires 'essentiels'. Je ne sens pas vraiment que je manque quelque chose.

Vim n'est pas parfait. Et il n'est définitivement pas pour tout le monde.

Mais au moins, apprenez assez de Vim au cas où vous l'ouvririez accidentellement et [ne sauriez pas comment quitter](https://stackoverflow.blog/2017/05/23/stack-overflow-helping-one-million-developers-exit-vim/)... ! ;)