---
title: J'ai créé un jeu de rôle en JavaScript. Vous pouvez le faire aussi. Voici comment.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-02T19:20:55.000Z'
originalURL: https://freecodecamp.org/news/learning-javascript-by-making-a-game-4aca51ad9030
coverImage: https://cdn-media-1.freecodecamp.org/images/1*dT0K035G8ZPYB6qWv4Vy1Q.png
tags:
- name: GameDev
  slug: gamedev
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: Life lessons
  slug: life-lessons
- name: Web Development
  slug: web-development
seo_title: J'ai créé un jeu de rôle en JavaScript. Vous pouvez le faire aussi. Voici
  comment.
seo_desc: 'By Robert Skalko

  So you want to try and make a game, but are a bit intimidated? Don’t worry, I was
  too!

  I was afraid of using objects, for example. They were this big spooky thing that
  I shelved away for later. But now I use them all the time!

  I’m go...'
---

Par Robert Skalko

Alors, vous voulez essayer de créer un jeu, mais vous êtes un peu intimidé ? Ne vous inquiétez pas, moi aussi je l'étais !

J'avais peur d'utiliser des objets, par exemple. C'étaient ces grandes choses effrayantes que j'ai mises de côté pour plus tard. Mais maintenant, je les utilise tout le temps !

Je vais vous guider à travers toutes les étapes que j'ai suivies pour construire mon jeu de rôle en JavaScript.

Voici mon jeu en cours d'exécution sur CodePen. (Notez qu'il n'est pas encore optimisé pour les mobiles) :

**Premièrement**, choisissez le type de votre jeu. Est-ce un puzzle ? Un RPG ? Un hack & slash ? Très bien, réfléchissez maintenant aux difficultés techniques de le créer. Un jeu de puzzle nécessiterait beaucoup de JavaScript compliqué. Un hack & slash aurait besoin d'un équilibrage minutieux, et ainsi de suite.

De plus, décidez si vous voulez que ce soit un jeu pour navigateur, un jeu mobile, ou les deux (un jeu "web natif").

Par exemple, mon jeu ne peut pas bien s'adapter à un écran mobile, car le joueur a 24 sorts. Ce n'est pas confortable de cliquer sur ces petits boutons sur un petit écran, donc je devrais redessiner le jeu pour mobile.

**Deuxièmement**, écrivez _toutes_ les choses que vous devez programmer pour réellement créer le jeu. Pour moi, c'était :

* un système d'inventaire
* un générateur d'objets
* un système de statistiques du joueur
* un système de sauvegarde

**Troisièmement**, commencez à créer votre jeu en résolvant ces problèmes un par un.

### Besoin d'aide pour créer le jeu ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*aEC1UYYqmYtobaoaCTqg0Q.jpeg)

Il est beaucoup plus facile de décomposer votre jeu en petites tâches. Vous ne créez pas un jeu, vous créez un système d'inventaire. Ensuite, vous créez un système de combat. Et ainsi de suite.

Sauf si vous êtes déjà bon en dessin — ou si vous voulez passer des mois ou des années à devenir bon — utilisez ces outils pour créer des actifs qui rendront votre jeu attrayant :

* [Game-Icons.net](http://game-icons.net) — ces icônes sont amusantes et faciles à colorier
* [Open Game Art](http://opengameart.org) — obtenez des actifs du domaine public
* [Bulk Resize Photos](http://bulkresizephotos.com) — un excellent outil pour créer vos propres petites icônes
* [CSS Sprite Generator](http://spritegen.website-performance.org) — vous aide à créer des spritesheets CSS pour vos icônes

### Problèmes que j'ai rencontrés et comment je les ai résolus

#### Spritesheets

Prévoyez-vous d'avoir plus de 20 images dans votre jeu ? Si oui, vous ne voulez pas créer 20 images avec des liens vers chacune d'elles. Vous pourriez penser que 20 images, ce n'est pas beaucoup, mais si vous décidez d'en ajouter 50 de plus ? C'est là que les [spritesheets](http://spritegen.website-performance.org) sont utiles. Placez quelques images dessus, copiez le fichier CSS dans votre projet, et ajoutez simplement la classe à votre élément qui correspond à l'image souhaitée.

#### Sauvegarder l'état de votre jeu

Voulez-vous que votre jeu soit sauvegardé ? Vous pouvez choisir entre utiliser le LocalStorage du navigateur et stocker des choses sur un serveur. Les serveurs nécessitent des connaissances en backend. Si vous n'en avez pas, je suggère d'utiliser le LocalStorage. Il sauvegarde le jeu tant que l'utilisateur ne le supprime pas avec un outil de nettoyage. Voici comment je l'ai fait :

![Image](https://cdn-media-1.freecodecamp.org/images/1*8mlKqFNdm2SFjSooVGFsKg.png)

En gros, sauvegardez toutes vos données dans un objet, puis mettez à jour vos éléments au chargement. Utilisez la méthode JSON stringify et analysez-la plus tard.

#### Modularisez votre code

Déterminez quelles parties doivent être codées en dur et quelles parties doivent être modularisées. J'ai commencé par coder en dur les sorts, ce qui est rapidement devenu compliqué. J'avais besoin de 24 de ces fonctions, ainsi que de 24 fonctions ifCritical.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tCuUgl39v-PFS4KJaLjZWw.png)
_Je jure que je n'ai pas écrit ça ! Euh... J'ai été forcé !_

![Image](https://cdn-media-1.freecodecamp.org/images/1*4FoWNMmrj3KZnxYoeVPqyQ.png)
_Il a même une fonction qui peut ajouter des fonctionnalités personnalisées !_

Maintenant, vous pourriez demander, comment fonctionne le deuxième sort ? J'ai une fonction playerAttack() qui utilise l'objet sort pour faire des choses :

* Elle exécute d'abord la fonction de mise à jour des sorts, qui appelle l'objet sorts. Ensuite, le sort prend vos statistiques actuelles et les transforme en valeurs comme "dégâts" et "coût de mana".
* Elle vérifie si les dégâts sont supérieurs à 0. Si oui, elle inflige des dégâts au boss et affiche les dégâts, quel sort les a infligés, et le montant. Elle fait cela pour la plupart des autres valeurs aussi. Vous pourriez penser qu'une vérification de supérieur à zéro est inutile, mais vous changerez d'avis lorsque le jeu dira que vous avez infligé 0 dégâts et restauré 0 mana.
* Ensuite, elle exécute une fonction personnalisée, si le sort en a une. Cela pourrait être utilisé pour donner aux sorts des effets spéciaux qui ne sont pas possibles à travers notre fonction d'attaque principale.

#### La boucle de jeu

Pour moi, la boucle de jeu vérifie et met à jour les choses : les statistiques du joueur, si le joueur est mort, si le joueur vient de monter de niveau, si un boss est mort, et ainsi de suite.

Vous devrez comprendre cela par vous-même. Je pense que c'est une bonne expérience d'apprentissage. Réfléchissez à ce que les vérifications et mises à jour doivent faire et quand elles doivent s'exécuter. Par exemple, avec une vérification de niveau, je l'ai réglée pour qu'elle s'exécute toutes les 20 secondes puisque monter de niveau n'est pas si important.

Mais j'ai aussi une vérification de la mort du boss qui s'exécute toutes les secondes après le début du combat. Pourquoi ? Pour que les joueurs n'aient pas à attendre 20 secondes pour qu'un boss meure.

D'autres choses n'ont même pas besoin d'être dans une boucle. Les fonctions peuvent simplement être appelées lorsqu'elles sont nécessaires. Prenez ma fonction de mise à jour des sorts, par exemple. Elle n'est appelée que lorsqu'un joueur utilise un sort.

### Quelques choses que j'ai apprises :

* Les objets sont bons. Ainsi, lorsque vous devez sauvegarder des données, vous devez simplement sauvegarder l'objet — pas les 50 variables individuelles.
* Définissez toujours les timeouts et les intervalles comme variables, afin qu'ils puissent être effacés plus tard — sauf s'ils sont des effets permanents et que vous êtes sûr de ne jamais avoir besoin de les effacer.
* Un gros fichier JavaScript pourrait ne pas être une bonne idée. CodePen ne permet qu'un seul fichier JavaScript, mais idéalement, vous devriez tout séparer en modules.
* Si vous ne vous inquiétez pas des performances, vous pouvez simplement copier et coller l'objet lorsqu'il doit être mis à jour — pas besoin de mettre à jour la moitié des valeurs individuellement. Si l'objet est énorme, vous pouvez même définir l'objet d'abord comme une variable comme : **var object;** et ensuite le construire en utilisant une autre fonction lorsque vous voulez qu'il soit mis à jour. Je l'ai fait avec mes sorts. Chaque fois que le joueur lance un sort, la fonction updateSpell() définit d'abord l'objet sorts, calcule tous les dégâts et les statistiques, puis lance le sort.

### Choses amusantes sur lesquelles j'ai fait des compromis :

* Les coûts de mana des compétences sont par niveau de boss, car s'ils étaient au niveau du joueur, je punirais les joueurs pour avoir monté de niveau. Cela a également rendu les boss de niveau supérieur beaucoup plus difficiles, ce que j'ai aimé.
* Les objets sont créés avec toutes les statistiques, mais elles ne sont pas affichées si elles sont à 0. Ainsi, je n'ai pas besoin de vérifier les valeurs non définies, et je peux éviter d'afficher les statistiques si elles sont générées à 0. Double victoire !
* J'ai beaucoup simplifié les buffs et les debuffs. En gros, il y a une var buffStat, nerfStat, totalStat et stat. Ainsi, les buffs ou les debuffs ne s'accumulent jamais.
* Avec les boss, la compétence nerf stat ne le réduit pas réellement à 0. C'est beaucoup plus sophistiqué que cela. Il réduit la statistique de 9999999, puis vérifie si elle est inférieure à 0. Si oui, il la définit à 0. Donc si vous arrivez à atteindre un niveau où vous avez des statistiques qui sont en milliards, je devrais peut-être ajouter plus de zéros.

Tout cela m'a appris que je devrais planifier un peu plus à l'avance, même si je ne fais qu'un projet amusant pour développer mes propres compétences.

De plus, j'ai maintenant une bien meilleure compréhension de la façon dont les bugs apparaissent : parfois, vous ne réalisez pas tous les cas limites où les choses peuvent se casser plus tard. Et c'est là que les bugs mordent.

### Bugs et Exploits

![Image](https://cdn-media-1.freecodecamp.org/images/1*VsmyUTc8fhqfX9haZAtXDA.jpeg)

Celui-ci m'a émerveillé, et m'a un peu effrayé. Je ne pouvais pas croire que mon chef-d'œuvre parfait contenait des bugs !

D'accord, j'exagère un peu. Mais j'ai sous-estimé le nombre de choses qui pouvaient mal tourner sans même que je m'en rende compte.

Voici quelques bugs et exploits qui sont apparus, qui me viennent à l'esprit :

1. Vous pouviez changer les niveaux de boss pendant un combat contre un boss, et obtenir de meilleurs butins de cette façon
2. Les barres de PV et de Mana débordaient parfois
3. Vous pouviez attaquer le boss avant même que le combat ne commence. Parlez d'un coup de poing en traître !
4. Le Mana pouvait devenir négatif, ce qui vous empêchait de pouvoir effectuer même des attaques de base, qui est le moyen principal de restaurer votre mana.
5. Les soins augmentaient temporairement votre santé maximale.
6. Un sort n'était pas réellement cliquable la plupart du temps à cause d'un problème CSS
7. Attaquer alors que vous n'êtes pas en combat mettait vos sorts en cooldown infini

Tout cela semble horrifiant, n'est-ce pas ? Dans un MMORPG, ces choses seraient exploitées dès le premier jour et ruineraient tout !

Eh bien, la bonne nouvelle est que la plupart d'entre eux étaient facilement corrigibles — généralement avec moins d'une ligne de code.

D'autres bugs, cependant, m'ont obligé à repenser complètement tout le système. Avec le système de sorts, je suis passé de l'écriture de 3 fonctions entières pour chaque sort à n'avoir besoin que d'un petit objet qui ne prend que quelques secondes de modification.

Encore une fois, voici mon jeu si vous voulez l'essayer (notez qu'il n'est pas optimisé pour les appareils mobiles) :

Et voici le code (qui est également open source et modifiable sur CodePen) :

[**RobertSkalko/LOOT-RPG-v1.0**](https://github.com/RobertSkalko/LOOT-RPG-v1.0)  
[_LOOT-RPG-v1.0 - Tuez des boss, obtenez du BUTIN !_github.com](https://github.com/RobertSkalko/LOOT-RPG-v1.0)

Gardez à l'esprit que je suis un débutant (seulement 2 mois de programmation) donc certaines de mes solutions peuvent être améliorées. Espérons cependant que je vous ai au moins donné les bases pour vous lancer !

Amusez-vous à créer votre jeu JavaScript !