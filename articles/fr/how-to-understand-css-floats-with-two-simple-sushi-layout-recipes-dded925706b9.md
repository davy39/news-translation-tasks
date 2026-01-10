---
title: Comment comprendre les floats CSS avec deux recettes de disposition de sushi
  simples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-25T14:27:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-understand-css-floats-with-two-simple-sushi-layout-recipes-dded925706b9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OyZdQ37Bw7O86Br_2gZgXA.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment comprendre les floats CSS avec deux recettes de disposition de
  sushi simples
seo_desc: 'By Anabella Spinelli

  A few weeks ago I decided I should admit to all the things I’ve never understood
  about basic CSS. I would try to do a deep and conscious dive into them and get them.
  It seemed that now, more than a couple years after learning abo...'
---

Par Anabella Spinelli

Il y a quelques semaines, j'ai décidé d'admettre toutes les choses que je n'ai jamais comprises sur le CSS de base. J'ai essayé de plonger profondément et consciemment dans ces concepts et de les _comprendre_. Il semblait que maintenant, plus de deux ans après avoir appris le CSS pour la première fois, je pouvais utiliser toute l'expérience que j'ai acquise à mon avantage. Cette fois, cela devrait être plus facile et plus clair.

Je me suis aussi dit : _Je ne peux pas être la seule à lutter avec ces propriétés pour la énième (ou première) fois._ Documenter mon voyage dans les propriétés les plus insaisissables du CSS ferait une excellente série d'articles que d'autres pourraient utiliser.

Le mois dernier, j'ai commencé avec une [introduction aux mystérieux appariements de la propriété position](https://medium.freecodecamp.org/an-intro-to-the-mysterious-pairings-of-css-position-flavors-92b3625176ea). Voici ma deuxième étape dans ce voyage :

La propriété `float`, sous forme de recettes de cuisine.

#### Index des recettes

* **Rangs de sushi** — faire en sorte que les éléments couvrent une rangée complète de manière uniforme
* **Bouillon clarifié** — faire en sorte que le contenu situé sous les floats se comporte normalement

### Rangs de sushi ?

Nous allons utiliser des floats et des valeurs en pourcentage pour distribuer les éléments uniformément sur toute la largeur (du conteneur). Tout comme les rangs de sushi dans une assiette.

#### Ingrédients :

* 1 conteneur ou plateau
* Quelques morceaux de sushi que vous devez distribuer côte à côte.
* Le signe `%`
* 1 `float: left;`

#### Instructions :

Préparez vos morceaux de sushi, c'est-à-dire les éléments que vous souhaitez afficher en rangée. Ils pourraient être des makis, des cartes d'items, des nigiris, des icônes, tout ce qui convient à votre goût.

Vous pouvez également ajouter n'importe quel style non positionnel : couleurs, alignement de texte, polices, sauce soja.

Placez-les à l'intérieur d'un conteneur **block**, comme un plateau. Dans sa forme la plus basique, ce devrait être une div (mais vous pouvez utiliser d'autres éléments sémantiques HTML5 tels que header, footer, section, article, main). Ajoutez une classe descriptive pour eux. J'utiliserai `nigiri`.

Maintenant, sur la classe `nigiri`, nous allons appliquer quelques styles, y compris notre `**float: left;**`. Prenez un moment et lisez-les :

Ce que fait `**float: left;**` est de dire à chaque élément de se coller à un côté — dans ce cas, à gauche — et de se tenir côte à côte dans une rangée de gauche à droite.

Notez que nous ajoutons une `height` au plateau. Normalement, nous n'en aurions pas besoin : le plateau s'étendrait pour s'adapter à ce qu'il contient. Mais les éléments flottants, comme nos nigiris, sont différents. Ils n'occupent pas d'espace réel dans le Document et n'affectent pas les autres éléments non flottants. C'est pourquoi nous utilisons une hauteur fixe, en pixels, pour le plateau.

Maintenant, vous devriez voir tous vos éléments sur une seule rangée. Mais quelque chose ne va pas. Ils s'entassent tous à gauche et vous avez probablement beaucoup d'espace vide sur le côté droit de votre plateau.

Nous devons les espacer uniformément.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PTeK-2AbKxznolPfgWC6JQ.jpeg)

Nous pouvons le faire en définissant la largeur des nigiris pour qu'elle soit relative à leur conteneur (le plateau dans ce cas) en utilisant une valeur en pourcentage.

**Voici la partie délicate** : le pourcentage que vous devez définir dépendra de 3 choses

* le nombre d'items que vous avez
* leur structure interne (padding)
* et l'espace que vous souhaitez entre eux.

Souhaitez-vous qu'ils se collent les uns aux autres ou ont-ils besoin d'une marge entre eux ? Si les morceaux de sushi ont un _padding de riz_, cela les rendra plus grands que leur contenu. Vous devrez compenser cela en diminuant leur largeur. Pour cela, il est également conseillé d'utiliser des % dans les valeurs de padding.

Je sais que tout cela peut être confus. Voici une illustration artisanale en une seule presse que j'espère pourra l'illustrer clairement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vEajpTwwxymHQr89D8ez1Q.jpeg)
_Chaque nigiri représente 33,33 % de la largeur totale du plateau : 2 % pour la marge de chaque côté, 2 % pour le padding de chaque côté et ensuite 29,33 % de leur largeur réelle._

Mais ceci est une recette, pas un cours de maths. Pour vous faciliter la tâche, chers lecteurs, voici quelques combinaisons courantes pour des éléments côte à côte et espacés avec une marge, tous avec un padding de riz de 1 % :

Vous avez peut-être remarqué le schéma ici : nous supposons que les éléments ont 1 % de **padding**. Ils doivent compenser cela en soustrayant 2 % (1 % pour chaque côté) du pourcentage de largeur de l'élément. Il en va de même pour notre **marge** de respiration de 1 %. Maintenant, il est plus logique de ne pas utiliser une largeur de 33,33 % pour 3 éléments en rangée. Au lieu de cela, définissez-la à 29,33 % après avoir laissé 2 % pour le padding et 2 % pour la marge de chaque côté.

Soupir... c'était _beaucoup_ de maths. Ok, donc maintenant, peu importe combien de morceaux votre rouleau de sushi est coupé, vous savez comment les présenter joliment sur un plateau.

Si vous souhaitez jouer avec cette configuration, voici [un CodePen](https://codepen.io/andiemusik/pen/OwRVMK) spécialement conçu pour cela.

_Et si vous aimez le CSS sushi, ne manquez pas le très inspirant [CSS Sushi Board](https://codepen.io/sashatran/pen/bgZVdm) de Sasha Tran._

### Bouillon clarifié ?

La soupe parfaite à avoir avec des sushis flottants, tout en s'assurant que vos portions ne finissent pas par nager dedans.

#### Ingrédients :

* Un conteneur ou plateau avec des sushis flottants
* Une soupe ou un bouillon à suivre après.
* Un `clear: broth;`

#### Instructions :

Une fois que votre rangée de morceaux de sushi flottants est prête, placez votre conteneur de soupe en dessous dans le html.

Nos sushis sont censés flotter "au-dessus" du flux du Document et ne pas affecter les autres éléments. Si nous ne sommes pas prudents, ils pourraient finir par flotter dans la soupe et le sushi-ramen n'est pas quelque chose pour lequel le monde est prêt.

Rappelez-vous que les éléments flottants n'ont pas de hauteur réelle dans le Document. Cela signifie également qu'ils ne "poussent" pas la soupe vers le bas. Maintenant, regardez ce désordre horrible :

Pour prévenir cette atrocité, nous devons ajouter notre `clear: broth;`... je veux dire `**both**;` !

Nous avons deux options ici :

Nous pouvons simplement mettre la soupe dans un bol ou un conteneur et donner au bol un style `clear: both;`. Cela fera plus ou moins le travail, _mais_ cela entraînera des choses comme `**margin-top**` qui ne fonctionneront pas du tout sur le bol.

Donc, si nous voulons que les morceaux de sushi soient complètement protégés de l'inondation de soupe — et ne perdre aucune fonctionnalité en cours de route — nous devons les contenir dans une assiette avec un bord haut. Pour y parvenir, nous ajouterons un pseudo-élément `**:after**` à l'assiette de sushi (c'est-à-dire le conteneur de nos petits éléments flottants) :

Voici ci-dessous un autre exemple avec lequel vous pouvez jouer. J'ai rendu le plateau visible en utilisant la hauteur et la couleur de fond. Même si ce n'est **pas** nécessaire pour que la soupe soit bien placée, cela la rend simplement plus élégante ?

Pensez à cela comme à faire en sorte que le plat de sushi ait un mur sud très haut afin d'empêcher toute soupe de déborder. Mais... comme... un _joli_ mur.

_Tout est bien, je suis super contente que vous soyez arrivé jusqu'ici et j'espère que ce petit livre de recettes vous a aidé à mieux comprendre comment fonctionnent les floats... et comment **nous** pouvons travailler avec les floats. Restez à l'écoute pour plus de plongées profondes dans des choses basiques mais insaisissables comme celle-ci_ ?