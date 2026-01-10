---
title: Apprenez ce truc bizarre pour déboguer le CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-03T16:53:38.000Z'
originalURL: https://freecodecamp.org/news/heres-my-favorite-weird-trick-to-debug-css-88529aa5a6a3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*q6ap35H37-gXdR_ENdoxVg.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Apprenez ce truc bizarre pour déboguer le CSS
seo_desc: 'By ZAYDEK

  Designers HATE him! ?

  Learn This One Weird ? Trick To Debug CSS

  Not clickbait

  Before I get to the article, I just want to share that I’m building a product, and
  I would love to collect some data about how to better serve web developers. I c...'
---

Par ZAYDEK

#### Les designers le détestent ! ?

# Apprenez ce truc bizarre pour déboguer le CSS

#### *Pas du clickbait*

Avant de commencer l'article, je souhaite partager que je développe un produit et que j'aimerais collecter des données pour mieux servir les développeurs web. J'ai créé un [court questionnaire](https://twitter.com/username_ZAYDEK/status/1103914471267790854) à consulter avant ou après la lecture de cet article. Merci de le consulter ! Et maintenant, revenons à notre programme habituel.

Salut ! ? Je suis Zaydek ! Lorsque j'ai commencé à apprendre à créer des sites web, cela a été bien plus douloureux que prévu. Après tout, je suis un graphiste et programmeur expérimenté — comment les sites web pourraient-ils être *si* difficiles ?

Dans cet article, je détaille les décisions qui m'ont conduit à créer un débogueur CSS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Czmfge5I4FvRyB4sJZD2RQ.png)
_[Cliquez ici](https://scrimba.com/g/gbuildablog" rel="noopener" target="_blank" title=") pour ouvrir dans Scrimba_

#### J'ai également enseigné un [cours gratuit HTML/CSS](https://scrimba.com/g/gbuildablog) sur Scrimba où j'enseigne comment construire un beau blog à partir de *zéro*. [Cliquez ici pour vous inscrire !](https://scrimba.com/g/gbuildablog) ?

#### [Scrimba.com](https://scrimba.com/g/gbuildablog) est une plateforme interactive de développement front-end où les sites web sont enregistrés sous forme d'événements — pas de vidéos — et peuvent être modifiés ! ?

### Qu'est-ce qu'un débogueur ?

Il y a une excellente citation de Donald Knuth sur le débogage. Pour paraphraser, cela donne quelque chose comme ceci.

> Quelqu'un : « Quel est le meilleur langage de programmation ? »

> Donald Knuth : « Celui qui a le meilleur débogueur. »

Je n'ai pas apprécié cette idée avant de travailler avec CSS. Les langages de programmation ont cette raisonnabilité où la logique dépasse l'opinion. Mais CSS est différent car CSS « semble » subjectif.

Alors, que pouvons-nous faire ? Eh bien, nous pouvons suivre le bon conseil de Donald Knuth et utiliser un débogueur !

Là où un langage de programmation est un outil, un débogueur est un outil que nous pouvons utiliser pour comprendre notre outil — notre code. Tous les informaticiens n'aiment pas les débogueurs, et je comprends cela.

Ne faites pas faire à l'ordinateur ce que nous ne comprenons pas. Je pense qu'il y a du mérite dans cela, mais ce dont je parle ici, c'est de révéler la structure là où elle était autrement invisible.

Prenez ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*BMu3HJzd4RAr7VHXEonMpA.png)
_[Cliquez ici](https://scrimba.com/c/c4vW9Hg" rel="noopener" target="_blank" title=") pour ouvrir dans le bac à sable de Scrimba_

Que pouvons-nous faire pour voir la structure de notre site web ? Voici deux solutions que je connais : nous pouvons créer des règles CSS ponctuelles pour mettre en évidence un élément, ou nous pouvons utiliser les outils de débogage de Chrome, Firefox ou Safari. Mais c'est *toujours* plus ou moins une solution ponctuelle. Ce dont nous avons besoin, c'est d'une solution **générale**.

### Notre débogueur

Il n'y a pas longtemps, je concevais cet en-tête, et ce n'était pas simple. L'intention était de survoler une image sur un texte multiline. Cela devrait être simple, non ?

Eh bien, CSS est l'antagoniste ? ici. Ce qui serait autrement simple dans Photoshop peut être un voyage héroïque en CSS, et cela m'a conduit à expérimenter avec `outline` :

```
* { outline: solid 0.25rem hsla(210, 100%, 100%, 0.5); }
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*t_WJXVnw_bjWhXZI8kvB9w.png)
_[Cliquez ici](https://scrimba.com/c/cJMVJfM" rel="noopener" target="_blank" title=") pour ouvrir dans le bac à sable de Scrimba_

Rien de trop spécial — juste des lignes blanches douces. Ce que nous avons, cependant, c'est une règle qui s'applique à tous les éléments tant que nous utilisons un `*` et non le nom de l'`id`, de la `class` ou de l'`element`.

Pourtant, l'introduction de `* { … }` a été profonde pour moi. Je me suis dit : « Où est-ce que je ne voudrais pas cela ? » J'ai donc ajouté quelques lignes de plus et développé un débogueur plus formel :

```
* {    color:                    hsla(210, 100%, 100%, 0.9) !important;    background:               hsla(210, 100%,  50%, 0.5) !important;    outline:    solid 0.25rem hsla(210, 100%, 100%, 0.5) !important;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*N3174yoUIeDpy6IDjkFfkA.png)
_[Cliquez ici](https://scrimba.com/c/c9kg4fZ" rel="noopener" target="_blank" title=") pour ouvrir dans le bac à sable de Scrimba_

Bien amélioré ! Ici, nous avons créé une apparence schématique pour notre site web. J'ai fait attention à ne pas utiliser de couleurs solides, mais j'ai plutôt choisi des couleurs douces ou des couleurs avec un canal alpha afin que les éléments imbriqués apparaissent plus profonds en couleur, avec des **bleus plus bleus** et des **blancs plus blancs**. J'ai également ajouté `!important` en raison des célèbres [Guerres de Spécificité CSS](https://en.wikipedia.org/wiki/cascading_style_sheets#specificity).

Ce qui peut parfois sembler être CSS qui nous embrouille, c'est la manière et le moment où la cascade s'applique. C'est-à-dire, « Comment se fait-il que les styles soient parfois appliqués et parfois non ? »

Ce n'est pas le CSS de Schrödinger, c'est une simple mathématique. CSS utilise une [calculatrice simple](https://specificity.keegan.st/) pour déterminer quelles règles sont plus spécifiques, et le résultat détermine si CSS est appliqué ou non.

![Image](https://cdn-media-1.freecodecamp.org/images/1*S_3XEtQfi_4W_3WPf7T7Ww.png)
_Une [implémentation](https://specificity.keegan.st/" rel="noopener" target="_blank" title=") du calculateur de spécificité de CSS_

La mère de toute spécificité est `!important`, qui remplace toutes les règles en ligne, les IDs, les classes et les éléments. [C'est comme l'Étoile de la Mort comparée à l'Empire](https://stuffandnonsense.co.uk/archives/css_specificity_wars.html). Malgré le fait que l'utilisation de `!important` soit généralement déconseillée, c'est parfait pour un débogueur — car nous ne livrerons pas notre site web avec celui-ci « activé ». Au lieu de cela, nous utilisons le débogueur uniquement dans la conception et le développement de notre site web.

Plus j'utilisais le débogueur, plus je réalisais que l'utilisation de `*:not(path):noth(g)` comme sélecteur était préférable. De cette façon, je n'obtiendrais pas de lignes superflues provenant de graphiques vectoriels. J'ai également remarqué que la désactivation de `box-shadow` était plus propre, car le débogueur n'a pas besoin d'une sensation de profondeur.

Donc, voici le débogueur final :

```
*:not(path):not(g) {    color:                    hsla(210, 100%, 100%, 0.9) !important;    background:               hsla(210, 100%,  50%, 0.5) !important;    outline:    solid 0.25rem hsla(210, 100%, 100%, 0.5) !important;
```

```
    box-shadow: none !important;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*q6ap35H37-gXdR_ENdoxVg.png)
_[Cliquez ici](https://scrimba.com/c/cRVVPSD" rel="noopener" target="_blank" title=") pour ouvrir dans le bac à sable de Scrimba_

Je pense que *nous*, les humains, détestons ce que nous ne comprenons pas. Et CSS ne fait pas exception. Il est mal caractérisé parce qu'il est mal compris. Je propose : **pensez à CSS comme une épée à double tranchant. Il peut être utilisé à la fois pour construire et déconstruire des sites web**. Oui, CSS n'est pas Photoshop, mais cela ne signifie pas qu'il ne peut pas faire des choses que Photoshop ne peut pas faire. Créer notre propre débogueur *est* une chose que nous *pouvons* faire.

### **Comment utiliser ce débogueur ?**

1. Allez sur [zaydek.github.io/debug.css](https://zaydek.github.io/debug.css)
2. Ajoutez aux favoris « Debug CSS » ([code source ici](https://gist.github.com/zaydek/6b2e55258734deabbd2b4a284321d6f6))
3. Cliquez sur le favori pour l'activer et le désactiver ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*-Yr09cqoVXljecLuZxclFw.gif)

#### N'oubliez pas le [cours gratuit HTML/CSS](https://scrimba.com/g/gbuildablog) sur Scrimba où j'enseigne comment construire un beau blog à partir de *zéro*. [Cliquez ici pour vous inscrire !](https://scrimba.com/g/gbuildablog) ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*Czmfge5I4FvRyB4sJZD2RQ.png)