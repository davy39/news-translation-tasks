---
title: Sauter entre les mots en utilisant des raccourcis clavier dans iTerm
subtitle: ''
author: Fatos Morina
co_authors: []
series: null
date: '2018-01-28T18:49:35.000Z'
originalURL: https://freecodecamp.org/news/jump-between-words-using-keyboard-shortcuts-in-iterm-fb1a70cecf79
coverImage: https://cdn-media-1.freecodecamp.org/images/0*PgviMTnKvX_ivYIG.png
tags:
- name: education
  slug: education
- name: Life lessons
  slug: life-lessons
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Sauter entre les mots en utilisant des raccourcis clavier dans iTerm
seo_desc: iTerm is a great terminal replacement that I like to use. One feature that
  I wanted after my migration from Windows to OS X was the ability to jump between
  words in the command line, and not having to go through the whole line, character
  by character...
---

iTerm est un excellent remplacement de terminal que j'aime utiliser. Une fonctionnalité que je voulais après ma migration de Windows vers OS X était la possibilité de sauter entre les mots dans la ligne de commande, sans avoir à parcourir toute la ligne, caractère par caractère.

Il s'avère que cela est tout à fait possible et ne cause pas beaucoup de peine et d'effort de votre côté. Vous n'avez pas besoin de payer 1 BTC à Apple pour que cela fonctionne. Vous devez simplement apporter quelques modifications aux touches dans les préférences de iTerm et c'est tout.

En d'autres termes, vous n'avez pas besoin d'installer quoi que ce soit d'autre dans votre OS X. Tout ce que vous avez à faire est de faire quelques configurations dans les préférences de iTerm, et vous êtes prêt à partir.

C'est aussi simple que cela.

Commençons.

Pour que cela fonctionne avec la touche option droite, vous devez définir le modificateur de touche pour qu'il agisse comme une séquence d'échappement.

Tout d'abord, vous devez configurer votre touche gauche ⌥ pour qu'elle agisse comme un caractère d'échappement.

![Image](https://cdn-media-1.freecodecamp.org/images/rdEDhYcmDHmBVijhouwsFatN18kEY6ZD08ST align="left")

Après cela, vous pouvez soit modifier le raccourci actuel pour ⌥ ← soit en créer un nouveau, dans les touches de raccourci du profil, avec les paramètres suivants :

* Raccourci clavier : ⌥←
    
* Action : Envoyer une séquence d'échappement
    
* Esc+ : b
    

![Image](https://cdn-media-1.freecodecamp.org/images/LqVy4VYF8AHtoeyBTt5FiwraeY3X2IZrQ46j align="left")

Maintenant, nous devons répéter un processus similaire pour le raccourci clavier ⌥→ avec les paramètres suivants :

* Raccourci clavier : ⌥→
    
* Action : Envoyer une séquence d'échappement
    
* Esc+ : f
    

C'est tout ce que nous devons faire. Après avoir terminé, nous devons peut-être redémarrer iTerm pour pouvoir utiliser les modifications que nous venons d'effectuer.

Maintenant, nous pouvons sauter des mots entiers sur l'interface de ligne de commande en maintenant la touche gauche ⌥ enfoncée et en appuyant sur ← ou →.

J'espère que vous trouverez cet article utile.

*Cet article a été publié pour la première fois par l'auteur sur son* [*blog*](http://www.fatosmorina.com/jump-words-using-keyboard-shortcuts-iterm/)*.*