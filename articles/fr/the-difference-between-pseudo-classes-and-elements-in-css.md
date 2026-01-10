---
title: La Différence Entre les Pseudo-Classes et les Pseudo-Éléments en CSS
subtitle: ''
author: Natalie Pina
co_authors: []
series: null
date: '2023-04-21T17:34:29.000Z'
originalURL: https://freecodecamp.org/news/the-difference-between-pseudo-classes-and-elements-in-css
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/pseudo-1.png
tags:
- name: CSS
  slug: css
seo_title: La Différence Entre les Pseudo-Classes et les Pseudo-Éléments en CSS
seo_desc: "In CSS, pseudo-classes and pseudo-elements are two types of keywords that\
  \ you can combine with selectors. They are used to target the element's state or\
  \ specific parts of an element. \nIn this article, we'll explore the differences\
  \ between the two alo..."
---

En CSS, les pseudo-classes et les pseudo-éléments sont deux types de mots-clés que vous pouvez combiner avec des sélecteurs. Ils sont utilisés pour cibler l'état de l'élément ou des parties spécifiques d'un élément. 

Dans cet article, nous explorerons les différences entre les deux, ainsi que leur histoire et les meilleures pratiques.

###### Syntaxe

* Le deux-points simple `:` fait référence aux pseudo-classes
* Le deux-points double `::` fait référence aux pseudo-éléments

## Pseudo-Classes vs Pseudo-Éléments

[Pseudo](https://www.dictionary.com/browse/pseudo#:~:text=2%20of%202)-,pseudo%2D,names%20of%20isomers%20(pseudoephedrine).) signifie faux, irréel ou faux. Le préfixe `pseudo-` est utilisé pour référencer des classes ou des éléments qui ne sont pas "réels". Non réel dans ce contexte signifie qu'il ne s'agit pas d'un élément DOM (Document Object Model), mais plutôt d'un élément virtuel créé à des fins de style. 

Pour former une meilleure définition, discutons de la différence entre les pseudo-classes et les pseudo-éléments en détail.

### Qu'est-ce qu'une Pseudo-Classe en CSS ?

Les pseudo-classes (`:`) sont principalement utilisées pour styliser un élément qui se trouve dans divers états. Lorsque l'on parle d'état, cela inclut la condition ou le comportement de l'utilisateur, par exemple hover, active, focus ou disabled. Les états impliquent généralement une interaction de l'utilisateur.

Par exemple, nous pouvons cibler tous les liens pour qu'ils aient une couleur de texte lavande lorsque l'utilisateur survole le lien.

```css
a:hover {
  color: lavender;
}

```

Inspectez les Chrome DevTools et vous trouverez d'autres exemples d'état. Ici, vous pouvez également tester et déboguer les styles appliqués en fonction de l'état (et de la pseudo-classe associée utilisée) en les activant et en les désactivant. 

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-20-at-10.13.42-AM.png)

Il existe plus de [50 types de pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes#alphabetical_index), je vous recommande donc de parcourir toutes les possibilités.

Testez l'exemple de code ci-dessous, inspectez les pseudo-classes et essayez d'en ajouter une nouvelle. 

%[https://codepen.io/nataliepina/pen/xxyRWYm]

#### Pseudo-Classes Fonctionnelles

Une autre variation du type de pseudo-classe est la pseudo-classe fonctionnelle. Ces appels de fonction prennent en paramètre une [liste de sélecteurs](https://developer.mozilla.org/en-US/docs/Web/CSS/Selector_list#selector_list) pour faire correspondre des éléments. 

Contrairement à d'autres types de pseudo-classes qui ciblent un état statique comme hover, celles-ci peuvent cibler dynamiquement des événements et des interactions utilisateur.

```css
:is()
/* La pseudo-classe matches-any correspond à tout élément qui correspond à l'un des
sélecteurs de la liste fournie. */

:not()
/* La pseudo-classe de négation, ou matches-none, représente tout élément 
qui n'est pas représenté par son argument. */

:where()
/* La pseudo-classe d'ajustement de spécificité correspond à tout élément qui
correspond à l'un des sélecteurs de la liste fournie sans ajouter de 
poids de spécificité. */

:has()
/* La pseudo-classe relationnelle représente un élément si l'un des 
sélecteurs relatifs correspond lorsqu'il est ancré à l'élément attaché. */
```

### Qu'est-ce qu'un Pseudo-Élément en CSS ?

Les pseudo-éléments (`::`) sont utilisés pour styliser des parties spécifiques d'un élément. Ils peuvent être utilisés pour cibler la première lettre ou la première ligne. Ou ils peuvent être utilisés pour insérer du contenu avant ou après l'élément. 

Il est utile de se familiariser avec cet [index des pseudo-éléments](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements#alphabetical_index) pour en savoir plus sur les mots-clés disponibles.

Par exemple, pour créer une grande première lettre d'un paragraphe, vous pouvez le faire en utilisant `first-letter` comme ceci :

```css
p::first-letter {
  font-size: 9em;
}
```

Un autre exemple courant de pseudo-élément est d'utiliser `::before` ou `::after` pour insérer du contenu avant ou après l'élément ciblé.

Testez l'exemple de code ci-dessous pour voir comment vous pouvez utiliser `::before` et `::after` pour créer des lignes avant et après un élément de texte.

%[https://codepen.io/nataliepina/pen/qBJqpgq]

## La Différence entre `:` et `::` en CSS

Pour résumer, rappelez-vous qu'il existe une différence clé entre un deux-points simple et un deux-points double. Plus important encore, `:` fait référence aux pseudo-classes et `::` fait référence aux pseudo-éléments.

### Histoire du `::` 

Historiquement, il n'y avait qu'un seul deux-points `:` pour définir à la fois les pseudo-classes et les pseudo-éléments. La notation `::` a été introduite avec CSS3 comme moyen de différencier les deux.

Les pseudo-éléments et les pseudo-classes sont des concepts apparentés qui offrent différentes façons de styliser un élément. Par conséquent, la légère variation de syntaxe entre eux est logique.

L'utilisation de la syntaxe à deux-points simple uniquement pour les deux n'est pas recommandée, car elle est devenue obsolète. Les navigateurs accepteront toujours `:` pour les deux actuellement, pour des raisons de compatibilité ascendante. Comme il est possible de rencontrer l'une ou l'autre syntaxe, comprendre le contexte historique autour de cela est bénéfique.

## Bonnes Pratiques pour l'utilisation de `:` vs `::`

La meilleure pratique lors du choix de la syntaxe des deux-points à utiliser est de respecter les normes actuelles de CSS3. Le respect de ces normes améliorera la maintenabilité de votre base de code, il est donc utile de conserver et de faire respecter des directives à ce sujet pour votre base de code.

Cela aidera également à préparer l'avenir de votre CSS. Comme nous l'avons discuté, les navigateurs acceptent actuellement la syntaxe à deux-points simple pour les deux, mais cela ne sera peut-être pas toujours le cas. En utilisant la syntaxe à deux-points double pour les pseudo-éléments, vous pouvez aider à prévenir les erreurs et les bugs à l'avenir, à mesure que CSS continue de changer et d'évoluer.

La distinction de syntaxe entre les deux offre des améliorations de lisibilité. Cela clarifie ce que vous ciblez, et est utile lorsque vous traitez avec des sélecteurs complexes qui impliquent plusieurs pseudo-éléments et pseudo-classes ensemble.

## Conclusion

Comprendre la différence entre une pseudo-classe et un pseudo-élément est essentiel pour écrire du CSS maintenable. Les pseudo-classes sont utilisées pour cibler l'état. Les pseudo-éléments sont utilisés pour cibler des parties spécifiques d'un élément.

J'espère que cet article a aidé à comprendre les différences entre les pseudo-classes et les pseudo-éléments, ainsi que leur histoire et les meilleures pratiques lors de leur utilisation. 

Bon stylisme ! 

Si vous souhaitez en savoir plus sur CSS, vous pouvez me trouver sur [Twitter](https://twitter.com/ui_natalie).