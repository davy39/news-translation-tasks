---
title: Les sélecteurs CSS expliqués en achetant une voiture
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-11-21T06:07:05.000Z'
originalURL: https://freecodecamp.org/news/css-selectors-explained-by-going-car-shopping-51a383f6eb4b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EQ87S6jXZiyDzCVQMJ6mPw.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Les sélecteurs CSS expliqués en achetant une voiture
seo_desc: 'By Kevin Kononenko

  If you have ever seen a car dealership, then you can understand CSS selectors.

  When you step onto the lot of a car dealership, you’re instantly surrounded by different
  cars, colors, and years.

  And of course there’s that aggressive ...'
---

Par Kevin Kononenko

#### Si vous avez déjà vu une concession automobile, alors vous pouvez comprendre les sélecteurs CSS.

Lorsque vous entrez sur le parking d'une concession automobile, vous êtes instantanément entouré de différentes voitures, couleurs et années.

Et bien sûr, il y a ce vendeur agressif. Mais laissons-le de côté dans cette simulation.

Les voitures — et leurs caractéristiques — peuvent être catégorisées en utilisant le même système que les sélecteurs CSS. Donc, si vous pouvez comprendre les différentes façons de segmenter les voitures dans un parking de concession, alors vous pouvez comprendre les sélecteurs CSS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lwrVtbNNgHdeYnat-UtaKg.png)

Commençons par imaginer une concession automobile, en utilisant HTML :

Nous allons maintenant couvrir quatre différentes façons de styliser vos éléments HTML :

1. Par le type d'élément, c'est-à-dire <div>
2. Par classe, par exemple 'blue'
3. Par id, par exemple '123xyz'
4. Par la relation avec d'autres éléments

#### Par type d'élément

Dans notre HTML ci-dessus, chaque <div> est en réalité une voiture d'un certain type. Cela pourrait être une berline, un camion ou une décapotable. Mais ce ne sont que des variations de voitures.

Si nous voulions ajouter un style à chaque voiture, nous devrions penser aux choses que chaque voiture sur ce parking a en commun.

Voici un exemple de CSS :

D'accord, je commence par quelque chose de basique, OK ? Et oui, j'ai inventé quelques propriétés CSS pour que cela fonctionne.

Quoi qu'il en soit, il serait juste de dire que chaque voiture de ce parking est faite d'acier, a 4 roues et a une hauteur maximale de 9 pieds. Donc, chaque fois que nous ajoutons un <div> à notre HTML, il aura ces propriétés par défaut.

En fait, nous pouvons aller encore plus loin avec ce concept de voiture. Nous pouvons décomposer l'intérieur de la voiture en HTML également :

Quelles sont certaines propriétés que les sièges et les fenêtres pourraient avoir ? Elles doivent être partagées par toutes les fenêtres et tous les sièges ! Nous ferons une plongée profonde sur ce sujet plus tard dans cet article.

#### Utilisation des classes

Regardez notre premier extrait HTML, qui couvre toutes les voitures du parking. Vous pouvez voir que chaque voiture <div> a une série de classes. Ces classes sont utilisées pour assigner des propriétés communes à tous les membres de la classe.

Disons que nous attribuons la classe '2005' à différentes berlines, camions et décapotables. Eh bien, quelle est une caractéristique que beaucoup de voitures avaient en commun en 2005 ? Les lecteurs CD ! Alors, faisons cela en pseudo-CSS.

Et si nous avons la classe 'crewCab' ? Les camions avec des cabines d'équipage ont 2 rangées de sièges, avec 5 sièges au total. Donc, nous pourrions vouloir attribuer cette classe spécifiquement aux camions. Nous pouvons combiner des classes en les enchaînant.

Les classes sont un moyen plus spécifique de référencer des éléments HTML. Donc, disons que tous les véhicules sont faits d'acier, par défaut. Mais vous voulez que certains véhicules soient faits d'aluminium. Vous pouvez créer une classe 'aluminum' qui remplacera la propriété de matériau de tous les membres de la classe.

#### Utilisation de l'ID

Les éléments HTML peuvent avoir un ID. C'est le moyen le plus spécifique de référencer un seul élément, et il remplace tous les autres styles. Cet identifiant unique est un peu comme la plaque d'immatriculation de l'élément.

![Image](https://cdn-media-1.freecodecamp.org/images/1*U76THFEJoQcBTmFzX7MYUA.png)

Donc, disons que vous avez une voiture et qu'elle a la plaque d'immatriculation '123 XYZ'. Cette voiture a une couleur violette unique, parce que pour une raison quelconque, le propriétaire l'a exigé. Voici cet élément en CSS.

Les éléments ont une relation 1-à-1 avec les IDs. Tout comme avec les voitures et les plaques d'immatriculation, deux voitures ne peuvent pas avoir la même plaque d'immatriculation. C'est aussi le moyen le plus puissant d'identifier un élément, donc vous pouvez créer des exceptions uniques à toutes les autres règles qu'un élément devrait suivre.

#### Relations entre les éléments

Disons que vous voulez vous assurer que les voitures avec la classe 'leatherSeats' ont des sièges en cuir. Regardez le deuxième extrait HTML de la section 'Type d'élément'.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jcGxiBfdyRy1t7mr4mlrOg.png)

Vous auriez également pu donner à chaque <div> avec la classe 'seat' la classe 'leather' aussi. Mais voici le problème : cela ne vous permettrait pas de sélectionner uniquement les voitures avec des sièges en cuir dans leur ensemble. Vous ne pourriez sélectionner que les sièges eux-mêmes.

Donc, nous voulons donner à toute la voiture une classe 'leatherSeats' pour nous assurer de pouvoir sélectionner tout le <div> et ses enfants.

Le CSS ci-dessus sélectionnera tous les éléments avec la classe 'seat' dans un conteneur 'leatherSeats'.

Maintenant, disons que vous voulez vous assurer que le siège passager avant a des chauffe-sièges. Vous pouvez utiliser le sélecteur '~', qui est connu comme le sélecteur de frères et sœurs. Il vous permet d'assigner des styles aux éléments en fonction de leurs voisins.

Donc, vous pouvez dire :

Voici un dernier exemple. Disons qu'un modèle particulier avait une caractéristique bizarre et aléatoire. Par exemple, un camion Chevy de 2008 pourrait avoir eu des lecteurs DVD dans les sièges arrière.

Voici comment vous le transformeriez en CSS :

1. Vous devez commencer par plusieurs classes, car il s'agit d'un type de voiture très spécifique. Cela pourrait être 'div.truck.chevy.year2008'.
2. Ensuite, pensez à la façon dont vous pourrez sélectionner les sièges arrière, spécifiquement. Vous pourriez donner à la rangée une classe supplémentaire, comme '.backRow'. Ou vous pourriez utiliser le [:last-child selector](http://www.w3schools.com/cssref/css_selectors.asp).
3. Enfin, vous devez sélectionner les sièges eux-mêmes.

Réponse :

Si vous avez aimé cet article, vous pourriez également aimer mes [autres explications](https://www.rtfmanual.io/guides/) de sujets CSS et JavaScript difficiles, tels que le positionnement, le Modèle-Vue-Contrôleur et les callbacks.

Et si vous pensez que cela pourrait aider d'autres personnes dans la même situation que vous, donnez-lui un 'heart' !