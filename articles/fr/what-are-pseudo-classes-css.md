---
title: Qu'est-ce que les pseudo-classes CSS ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-23T14:00:00.000Z'
originalURL: https://freecodecamp.org/news/what-are-pseudo-classes-css
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pseudo-classes-thumbnail.png
tags:
- name: beginner
  slug: beginner
- name: CSS
  slug: css
- name: learning to code
  slug: learning-to-code
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce que les pseudo-classes CSS ?
seo_desc: 'By Deborah Kurata

  To make sense of CSS pseudo-classes, we need to understand state. In this context,
  the word state means a situation or condition that something is in at a particular
  point in time.

  Take the state of a stoplight, for example. At any ...'
---

Par Deborah Kurata

Pour comprendre les pseudo-classes CSS, nous devons comprendre l'état. Dans ce contexte, le mot **état** signifie une situation ou une condition dans laquelle quelque chose se trouve à un moment particulier.

Prenons l'état d'un feu de signalisation, par exemple. À tout moment, il a l'un des trois états suivants :

* État rouge : Arrêt
* État jaune : Accélérer ... oh non ! ... c'est la prudence
* Et état vert : Allez

Lorsque nous parlons de l'"état du feu de signalisation", nous faisons référence à l'une de ces trois possibilités.

Comment l'état est-il lié aux pseudo-classes ? Examinons un exemple.

![Page web montrant les styles de liens d'élément d'ancrage par défaut.](https://www.freecodecamp.org/news/content/images/2023/01/Figure-1.png)
_Figure 1. Styles de liens par défaut_

Sur la page web de la Figure 1, remarquez que les liens vers GitHub et LinkedIn sont actuellement bleus et soulignés. Cliquez sur un lien et vous voyez qu'il devient rouge comme montré dans la Figure 2.

![Page web montrant le style actif de lien d'élément d'ancrage par défaut.](https://www.freecodecamp.org/news/content/images/2023/01/Figure-2.png)
_Figure 2. Style de lien actif par défaut_

Cliquez sur le lien, et il devient violet comme vous pouvez le voir dans la Figure 3.

![Page web montrant le style visité de lien d'élément d'ancrage par défaut.](https://www.freecodecamp.org/news/content/images/2023/01/Figure-3.png)
_Figure 3. Style de lien visité par défaut_

Nous ajoutons des liens à une page HTML en utilisant des éléments d'ancrage, désignés par un "a".

```html
<a href="http://www.github.com">GitHub</a>
<a href="#">LinkedIn</a>
```

Comme vous l'avez vu dans les figures, par défaut, l'élément d'ancrage a plusieurs états : bleu lorsqu'il n'a pas encore été cliqué, rouge lorsqu'il est actif, et violet lorsqu'il a été cliqué.

Si nous stylisons simplement un élément d'ancrage, en utilisant un sélecteur d'élément CSS comme montré ci-dessous, le lien n'aura aucune de ces colorations supplémentaires pour les différents états.

```css
a {
  color: darkslategray;
}
```

Comment styliser ces états d'ancrage ? Vous l'avez deviné ! Avec des pseudo-classes. Examinons ce que sont les pseudo-classes et passons en revue deux exemples. Vous pouvez voir la vidéo associée ici :

%[https://youtu.be/-zWasID5o9M]

## **Qu'est-ce qu'une pseudo-classe ?**

Une **pseudo-classe** CSS est un nom fantaisiste pour un mot-clé ajouté à un sélecteur CSS qui identifie l'état de l'élément HTML. Nous pouvons ensuite styliser l'élément lorsqu'il est dans cet état particulier.

Pour ajouter une pseudo-classe à un sélecteur, ajoutez un deux-points et le nom de la pseudo-classe :

```css
a:active {
  color: orange;
}
```

Le a:active ajoute la pseudo-classe active au sélecteur d'élément d'ancrage. Nous pouvons ensuite styliser le lien d'ancrage pour qu'il ait un certain aspect lorsqu'il est dans son état actif.

Examinons deux exemples utilisant des pseudo-classes.

## Comment styliser les états d'ancrage

Un élément d'ancrage a quatre états :

* link : lorsque le lien n'a pas encore été cliqué.
* visited : lorsque le lien a été cliqué (cliquer sur un lien "visite" cette page liée, d'où le nom "visited").
* hover : lorsque la souris survole le lien.
* active : pour le moment où la souris est cliquée sur le lien

Nous stylisons ces états en utilisant des pseudo-classes. Dans l'exemple ci-dessous, nous spécifions le sélecteur d'élément "a" (ou ancrage), un deux-points, et le nom de l'état de l'ancrage.

```css
a:link {
  color: slategray;
}
a:visited {
  color: darkslategray;
}
a:hover {
  color: yellow;
}
a:active {
  color: orange;
}
```

Il est recommandé de déclarer ces pseudo-classes dans la feuille de style dans cet ordre en raison des règles de précédence CSS. Trouvez plus d'informations sur les règles de précédence CSS [ici](https://youtu.be/8qLTN5TKdcA). En bref, les styles déclarés plus tard remplacent ceux déclarés plus tôt. Pour l'élément d'ancrage, nous voulons que l'état actif prenne le dessus, c'est pourquoi il est le dernier.

Utilisez ces états selon vos besoins lorsque vous stylisez vos ancres.

Pour voir ces états en action et essayer vos propres styles personnalisés, consultez [ce projet](https://stackblitz.com/edit/pseudo-classes-deborahk).

Maintenant, examinons un autre type d'élément HTML, l'élément de case à cocher.

## Comment styliser l'état coché d'une case à cocher

Ici, nous avons une case à cocher pour "Ajoutez-moi à votre liste de diffusion". Elle est actuellement dans un état "non coché".

![Affichage d'une case à cocher par défaut avec le texte : "Ajoutez-moi à votre liste de diffusion"](https://www.freecodecamp.org/news/content/images/2023/01/Figure-4.png)
_Figure 4. Case à cocher par défaut_

Voici la même case à cocher dans l'état "coché" avec un style par défaut. Nous voulons styliser l'état "coché" pour ajouter notre propre apparence personnalisée.

![Style de case à cocher cochée par défaut avec couleur de fond bleue](https://www.freecodecamp.org/news/content/images/2023/01/Figure-5-1.png)
_Figure 5. Style de case à cocher cochée par défaut_

Disons que nous voulons changer la couleur de fond, peut-être que le bleu entre en conflit avec notre design. Et nous voulons changer la bordure en supprimant la bordure existante et en ajoutant notre propre couleur de contour. Comme ceci :

### HTML

```html
<input type="checkbox" id="mailing-list">
<label for="mailing-list">Ajoutez-moi à votre liste de diffusion</label>
```

### CSS

```css
#mailing-list:checked {
  border: none;
  accent-color: white;
  outline: 2px solid orange;
}
```

Ici, nous utilisons un sélecteur d'identifiant CSS et une pseudo-classe pour styliser l'état coché d'une case à cocher. Nous supprimons la bordure, définissons la couleur de fond (appelée `accent-color`), et fournissons notre propre contour orange.

L'état coché résultant ressemble à ceci :

![Style de case à cocher personnalisé sans couleur de fond et avec une bordure orange](https://www.freecodecamp.org/news/content/images/2023/01/Figure-5.png)
_Figure 6. Style de case à cocher cochée personnalisé_

Utilisez cette technique pour donner à vos pages web un look personnalisé.

Pour voir ces états en action et essayer vos propres styles personnalisés, consultez [ce projet](https://stackblitz.com/edit/pseudo-classes-deborahk).

## Conclusion

Une pseudo-classe est un mot-clé ajouté à un sélecteur qui stylise l'état d'un élément. Nous avons vu comment ajouter des pseudo-classes pour les états d'élément d'ancrage et pour l'état coché d'une case à cocher.

De nombreux autres éléments HTML ont également des états, et nous pouvons styliser ces états en utilisant des pseudo-classes. Pour une liste de ces pseudo-classes, voir la [documentation MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes).

Pour plus d'informations sur le stylisme avec CSS, consultez mon cours : ["Introduction en douceur à CSS pour les débutants"](https://www.youtube.com/playlist?list=PLErOmyzRKOCptjkM-mOfveYlgKQEx1AAf) et abonnez-vous à [ma chaîne YouTube](https://www.youtube.com/@deborah_kurata).

Feu vert ... allez ! Maintenant, allons-y et stylisons nos états d'éléments.