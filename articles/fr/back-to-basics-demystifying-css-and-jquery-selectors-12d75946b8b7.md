---
title: Comment utiliser les sélecteurs jQuery et CSS, et les bases de leur fonctionnement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-04T13:15:30.000Z'
originalURL: https://freecodecamp.org/news/back-to-basics-demystifying-css-and-jquery-selectors-12d75946b8b7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fvb-U3xoZbIr_AEmPHOQjw.jpeg
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment utiliser les sélecteurs jQuery et CSS, et les bases de leur fonctionnement
seo_desc: 'By Rasheed Bustamam

  The other day, I was interviewing someone who had finished the front-end certification
  of freeCodeCamp. He had also graduated from a rather prestigious bootcamp, where
  attendees coded from 8am to 8pm for six weeks straight. Yikes!...'
---

Par Rasheed Bustamam

L'autre jour, j'interviewais quelqu'un qui avait terminé la certification front-end de freeCodeCamp. Il avait également obtenu son diplôme d'un bootcamp plutôt prestigieux, où les participants codent de 8h à 20h pendant six semaines d'affilée. Aïe !

Ses compétences en programmation étaient excellentes, mais j'ai été surpris de constater que ses connaissances en CSS étaient limitées. Et par limitées, je veux dire qu'il ne savait pas comment sélectionner une classe pour appliquer un style. Cela ne reflète pas nécessairement négativement sur lui. Si quoi que ce soit, cela met en lumière comment beaucoup de programmeurs voient le CSS.

Beaucoup de gens pensent que l'apprentissage du CSS n'est pas important, puisque les designers pourront généralement implémenter le CSS pour vous. Bien que cela soit vrai, il y a de nombreuses fois où vous (en tant que programmeur) devrez connaître quelques bases de CSS afin de sélectionner un élément et de lui dire de faire quelque chose lorsque quelque chose d'autre se produit.

Par exemple, [Green Sock Animation Platform (GSAP)](https://greensock.com/) est probablement trop orienté programmation pour être centré sur les designers. Il nécessite un développeur ayant des connaissances en CSS ainsi qu'en programmation.

Je ne dis pas que chaque développeur doit être un maître en CSS. Mais je pense que si vous voulez vous appeler un développeur full-stack, vous devriez connaître les bases du CSS. Et les bases commencent avec le **sélecteur**.

Avertissement : les sélecteurs jQuery ne sont pas réellement uniques à jQuery — ce sont en fait des sélecteurs CSS. Cependant, si vous êtes comme moi, vous avez appris jQuery avant d'apprendre correctement le CSS, et donc vous avez automatiquement associé les sélecteurs à jQuery. Bien que cet article porte sur les sélecteurs CSS, il vous aidera également si vous avez besoin de quelques clarifications sur les sélecteurs jQuery.

### Le Sélecteur CSS

Je trouve toujours utile de jouer avec le code, alors voici un simple CodePen pour jouer avec les sélecteurs de base.

En HTML, il y a trois façons d'étiqueter ou de catégoriser des éléments. La première façon est la plus large : par nom de balise. Par exemple, vous pouvez sélectionner **tous** les `div` de votre page en utilisant le sélecteur simple `div`. Hé, c'était facile !

La deuxième façon est probablement celle que vous utiliserez le plus : l'attribut `class`. Vous pouvez sélectionner par classe en utilisant un point (`.`), donc dans l'exemple ci-dessus, pour sélectionner **tous** les éléments avec la classe `section`, j'utilise `.section` comme sélecteur.

La troisième façon est souvent surutilisée, mais reste utile, et c'est l'attribut `id`. Les IDs doivent identifier vos éléments, tout comme votre numéro de sécurité sociale (aux États-Unis) pourrait vous identifier en tant que personne. Cela signifie que les IDs doivent être uniques dans toute la page. Pour sélectionner un élément avec un ID spécifique, vous utilisez le hashtag (`#`), ou [octothorpe](https://en.wiktionary.org/wiki/octothorpe) comme j'aime l'appeler. Pour sélectionner l'élément avec l'ID `other`, j'utilise `#other`.

Ce sont les sélecteurs les plus basiques. Pour récapituler :

* sélectionner par nom de balise (aucun préfixe)
* sélectionner par nom de classe (préfixe de `.`)
* sélectionner par ID (préfixe de `#`)

Ces trois sélecteurs seuls vous permettront de sélectionner presque n'importe quoi sur votre page web.

### Quiz 1

1. Comment sélectionneriez-vous toutes les balises de paragraphe sur la page ? (indice : les balises de paragraphe sont `p`)
2. Comment sélectionneriez-vous tous les éléments avec la classe `button-text` ?
3. Comment sélectionneriez-vous l'élément avec l'ID `form-userinput` ?

N'hésitez pas à partager vos réponses dans les commentaires !

### Tous les IDs doivent-ils être uniques ?

C'est une petite digression que je trouve très importante. Mais si vous êtes seulement ici pour apprendre à utiliser les sélecteurs, n'hésitez pas à passer à la section suivante.

Avec un nom comme ID, vous supposeriez que chaque ID HTML **doit** être unique ou votre document HTML ne fonctionnera pas. Après tout, essayer d'avoir deux variables `const` fera crier de nombreux éditeurs, alors HTML ne crierait-il pas aussi ?

Le problème est que HTML **ne** criera pas. En fait, personne ne vous dira même qu'il y a quelque chose de mal. Vous pourriez trouver un bug qui provient d'un ID non unique. Mais vous allez devenir fou en essayant de trouver la cause racine du bug, car c'est une défaillance très subtile.

L'exemple ci-dessus démontre pourquoi avoir des IDs dupliqués pourrait causer un problème sur votre page web. Premièrement, il y a en fait deux `div` avec l'ID `other`. Si vous commentez les styles pour `#other`, vous verrez que **les deux** éléments sont en fait stylisés. Cela pourrait vous faire penser, « bien, je peux utiliser les IDs et les noms de classe de manière interchangeable ! »

Pas si vite. Si vous regardez dans le panneau JavaScript, vous verrez que j'ai sélectionné des éléments particuliers en fonction de leur étiquette d'élément : nom de balise, nom de classe ou ID. Vous remarquerez que `document.getElementsByTagName` et `document.getElementsByClassName` retournent une collection de tous les éléments HTML correspondants. `document.getElementById` retourne uniquement le premier élément HTML qu'il peut trouver avec l'ID correspondant. Vous pouvez vérifier cela en décommentant la fonction `getVanillaSelectors` et en vérifiant la console.

![Image](https://cdn-media-1.freecodecamp.org/images/-OPGCXaiU08Jk822L-vhfNCJvRgMkrbYwwGI)
_Utilisation de document.getElement(s)By[Type]_

Pour compliquer davantage les choses, si vous utilisez la méthode `querySelectorAll` de JavaScript (qui prend un sélecteur CSS en entrée), vous obtenez un résultat totalement différent.

![Image](https://cdn-media-1.freecodecamp.org/images/QAIsIoGAXcjxUU3103l-WiGng4GhA2WpZgfp)
_Utilisation de document.querySelectorAll_

Et juste pour vous embrouiller, jQuery fait quelque chose de différent malgré une syntaxe similaire à `querySelectorAll`.

![Image](https://cdn-media-1.freecodecamp.org/images/7ZCdtrLSCPzJJlXgYD9ltvbmq9Nkffj49vkr)
_Utilisation du sélecteur jQuery_

Je n'ai aucune explication pour le comportement différent. Cependant, je peux vous dire comment l'éviter. Voici mes règles :

1. Ne jamais utiliser les IDs. Utilisez les attributs `class` à la place.
2. Si je dois utiliser un ID, je le nomme de manière à ce qu'il soit unique même si un élément similaire existe sur la page ; par exemple `menu-item-01`

Parfois, les formulaires et leurs champs de saisie peuvent avoir besoin d'avoir des IDs. Dans ce cas, vous pouvez suivre la règle numéro 2. Voici comment je nommerais un formulaire pour l'inscription d'un utilisateur :

```
<form id="user-signup">  <input id="user-signup-userid" label="user id" />  <input id="user-signup-password" label="password" /></form>
```

De cette façon, si j'ai deux formulaires sur la même page (disons `user-signup` et `user-signin`), ils sont garantis d'avoir des IDs uniques. Même si les champs userID sont similaires entre les formulaires.

### Combinaison de Sélecteurs

Parfois, un seul sélecteur ne suffit tout simplement pas. Parfois, vous devez obtenir chaque `div` qui a un nom de classe `section`. D'autres fois, vous avez besoin de chaque élément avec un nom de classe `section` qui est un élément enfant d'un `div` avec l'ID `user-signup`. Il existe de nombreuses autres combinaisons possibles de sélecteurs.

Dans cette section, vous apprendrez trois façons de **combiner** des sélecteurs, et je suis convaincu que celles-ci conviendront à 90 % de vos besoins. Si vous trouvez que plus de 11 % de vos besoins ne sont pas satisfaits, venez vous plaindre à moi et je modifierai cela pour dire 89 % de vos besoins :).

Comme avant, commençons par un CodePen :

#### Combinaison de sélecteurs pour un seul élément

D'accord, commençons par combiner des sélecteurs pour un seul élément. Cela signifie sélectionner l'élément qui a le nom de balise `x`, ET le nom de classe `y`, ET l'ID `z`. Bien sûr, vous n'avez pas besoin des trois, mais vous pouvez combiner les trois.

Disons que nous voulons sélectionner tous les `div` avec la classe `item`. Pour ce faire, nous combinons les deux : `div.item`. Cela va du plus général au plus spécifique de gauche à droite. Cela sélectionne toutes les balises `div` qui ont également le nom de classe `item`. Il est important de noter qu'il n'y a **aucun** espace entre `div` et `.item`. Ajouter un espace change le sélecteur **complètement**, comme je vais le voir dans la section suivante.

Si vous décommentez le CSS correspondant, vous verrez que la `section` avec le nom de classe `item` n'est pas devenue rouge. C'est parce que ce n'est pas une balise `div`.

Vous pouvez faire ce même schéma avec les noms de classe et les IDs. Mais si vous avez l'ID d'un élément, vous pouvez tout aussi bien utiliser simplement l'ID. Il n'y a aucune raison de sélectionner un ID avec un nom de classe spécifique, car si vous avez suivi les règles des IDs ci-dessus, vous n'avez qu'un seul élément avec cet ID de toute façon.

Mais, juste pour parité, voici un exemple de sélection du `div` avec la classe `item` et l'ID `other` : `div.item#other`. Encore une fois, de gauche à droite, cela va du plus général au plus spécifique.

Très probablement, vous utiliserez cette syntaxe pour sélectionner un élément qui a plusieurs classes. Pour ce faire, il suffit de séparer toutes les classes avec des points. Pour sélectionner tous les éléments qui ont les deux classes `item` et `section`, vous utiliseriez `.item.section`. L'ordre n'a pas d'importance lorsque vous faites cela, donc `.section.item` fonctionnera également.

Ce petit truc vous permettra d'être plus spécifique dans vos sélecteurs.

#### Le sélecteur "enfant"

La deuxième façon dont vous pouvez combiner des sélecteurs est en utilisant le sélecteur "enfant", comme j'aime l'appeler. Il y a deux façons de faire cela, alors je vais commencer par la plus générale.

Tout d'abord, vous pouvez sélectionner **n'importe quel** enfant d'un certain élément en ajoutant un espace. Par exemple, pour sélectionner tous les enfants `item` de l'élément `#other`, ce serait `#other .item`. Remarquez l'espace entre les sélecteurs.

Deuxièmement, vous pouvez sélectionner les enfants **immédiats** d'un certain élément en utilisant le `>`. Un "enfant immédiat" d'un élément est celui qui n'est qu'un niveau profond. Dans l'exemple, il y a deux éléments `.item` contenus dans l'élément `#other`, mais l'un des éléments `.item` est enveloppé dans un élément `.wrapper`, donc celui-ci **n'est** pas un enfant immédiat.

Pour vous donner une visualisation, si vous réduisez tout ce qui se trouve sous l'élément `#other`, vous verriez ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0RUimDp2bmfxmjcXSseuU3mKkJQcEF8WQxEm)
_Enfants réduits_

Ce sont les deux seuls **enfants directs** de l'élément `#other`. Pour sélectionner uniquement l'enfant direct `.item` de `#other`, vous utiliseriez `#other > .item`, ce qui sélectionnerait l'enfant direct, mais **pas** celui sous `.wrapper`. Astucieux, n'est-ce pas ?

### Quiz 2

1. Comment sélectionneriez-vous toutes les balises de paragraphe qui appartiennent aux éléments `section` ? (indice : les balises de paragraphe sont `p`)
2. Comment sélectionneriez-vous tous les éléments avec la classe `button-text`, qui sont des descendants des éléments avec la classe `button` ?
3. Comment sélectionneriez-vous l'élément avec la classe `form-input` qui est un **enfant direct** des éléments `form` ?
4. **Question bonus** : expliquez ce que ce sélecteur sélectionne : `header.title > form.user-signup button.button-danger`

Comme avant, n'hésitez pas à partager vos réponses dans les commentaires !

#### Tout mettre ensemble — littéralement

Vous pouvez combiner des sélecteurs combinés. Vraiment. La question bonus ci-dessus montre un exemple, mais j'ai ajouté quelques combinaisons à la fin de l'exemple codepen.

Par exemple, vous pouvez choisir tous les `.item` qui sont des enfants des `div` avec la classe `parent-item` en utilisant `div.parent-item .item`. Whoa !

Vous pouvez choisir des descendants directs également. Par exemple, pour sélectionner tous les `div` avec la classe `item` qui sont des descendants directs des `div` avec la classe `parent-item` : `div.parent-item > div.item`.

Et enfin, juste pour vous embrouiller, vous pouvez parcourir tout l'arbre DOM : `div.parent-item .coolest-item .item`. La classe `item` qui est enfant de la classe `coolest-item` qui est enfant du `div` avec la classe `parent-item`.

Notez qu'il n'est généralement **pas** bon d'aller au-delà de deux ou trois niveaux de profondeur lors de la nesting des sélecteurs. Ensuite, vous entrez dans des domaines étranges de spécificité que vous pouvez résoudre plus efficacement en nommant mieux vos classes CSS. Mais cela est hors du cadre de cet article. Si vous voulez en savoir plus, faites-le moi savoir et j'écrirai à ce sujet.

### Bonus : Utilisation de Chrome DevTools pour obtenir un sélecteur

Vous pouvez utiliser Chrome DevTools pour obtenir le sélecteur de n'importe quel élément que vous pouvez sélectionner sur le DOM. Voici comment :

1. Ouvrez Chrome DevTools. Puisque vous sélectionnez un élément, allez-y et faites un clic droit sur l'élément que vous voulez sélectionner et cliquez sur "Inspecter" :

![Image](https://cdn-media-1.freecodecamp.org/images/GtfJwCPIBiQk6MwKL2Gh0SXrQP3-9U7gFRvZ)
_Oui, c'est une photo de moi en train d'écrire cet article_

2. Faites un clic droit sur l'élément DOM que vous voulez sélectionner et survolez "Copier", puis cliquez sur "Copier le sélecteur" :

![Image](https://cdn-media-1.freecodecamp.org/images/uA07RG3g28FPzm2R5kxisTCOoyNdebyozg76)
_Je préfère le thème sombre._

3. C'est tout ! Le sélecteur que j'ai copié, au fait, est `#editor_93 > section > div.section-content > div:nth-child(3) > p.graf.graf — p.graf-after — figure.graf — trailing`.is-selected. Vous pouvez copier le sélecteur dans `document.querySelector` ou jQuery et obtenir l'élément.

![Image](https://cdn-media-1.freecodecamp.org/images/PRajyQG7HxHQEEqeg83AGYzMOOCiF9VP8K7L)
_Ceci est le sélecteur pour l'image ci-dessus._

J'espère que cet article a été utile ! Si vous l'avez apprécié, donnez-moi quelques applaudissements pour que plus de gens le voient. Merci !