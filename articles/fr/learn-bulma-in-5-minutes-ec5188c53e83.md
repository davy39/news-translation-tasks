---
title: Apprendre Bulma CSS en 5 minutes - Un tutoriel pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-06T10:00:36.000Z'
originalURL: https://freecodecamp.org/news/learn-bulma-in-5-minutes-ec5188c53e83
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-rRVJ7pa3DUFN4Bul4e_CA.png
tags:
- name: CSS
  slug: css
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Apprendre Bulma CSS en 5 minutes - Un tutoriel pour débutants
seo_desc: 'By Per Harald Borgen

  Bulma is a simple, elegant, and modern CSS framework that a lot of developers prefer
  over Bootstrap. Personally, I think Bulma has a better design by default, and it
  also feels more light-weight.

  In this tutorial, I’ll give you a...'
---

Par Per Harald Borgen

Bulma est un framework CSS simple, élégant et moderne que de nombreux développeurs préfèrent à Bootstrap. Personnellement, je pense que Bulma a un meilleur design par défaut, et il semble également plus léger.

Dans ce tutoriel, je vais vous donner une introduction super rapide à la bibliothèque.

Nous avons également créé un cours gratuit sur Bulma. [Cliquez ici pour le découvrir !](https://scrimba.com/g/gbulma?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gbulma_5_minute_article)

![Vous pouvez cliquer sur l'image pour accéder au cours](https://cdn-media-1.freecodecamp.org/images/1*5XEOKibPcmV1oPB4ZFxNsg.png)
_[Vous pouvez cliquer ici pour accéder au cours.](https://scrimba.com/g/gbulma?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gbulma_5_minute_article)_

### L'installation

Configurer Bulma est super facile, et vous pouvez le faire de plusieurs manières différentes, que vous préfériez [NPM](https://www.npmjs.com/package/bulma), le télécharger directement [depuis la documentation](https://bulma.io/), ou utiliser un [CDN](https://cdnjs.cloudflare.com/ajax/libs/bulma/0.6.2/css/bulma.min.css). Nous allons simplement lier un CDN depuis notre fichier HTML, comme ceci :

```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.6.2/css/bulma.min.css">
```

Cela nous donnera accès aux classes Bulma. Et c'est en fait tout ce que Bulma est - une collection de classes.

### Modificateurs

La première chose que vous devriez apprendre sur Bulma est les classes modificateurs. Celles-ci vous permettent de définir des styles alternatifs pour presque tous les éléments Bulma. Elles commencent toutes par `is-*` ou `has-*`, et vous remplacez le `*` par le style que vous souhaitez.

Pour bien comprendre ce concept, commençons par examiner les boutons.

### Boutons

Pour transformer un bouton normal en bouton Bulma, nous allons simplement lui donner la classe `button`.

```html
<button class="button">Cliquez ici</button>
```

Ce qui donne le style suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*03TOy6dVBDCPvrlardUBHw.png)

Comme vous pouvez le voir, il a un beau design plat par défaut. Pour changer le style, nous allons utiliser les modificateurs Bulma. Commençons par rendre le bouton plus grand, vert et avec des coins arrondis :

```html
<button class="button **is-large is-success is-rounded**">Cliquez ici</button>
```

Le résultat est un bouton agréable à regarder :

![Image](https://cdn-media-1.freecodecamp.org/images/1*3p5bTMdQbPYx_DeNQo7sgA.png)

Vous pouvez également utiliser des modificateurs pour contrôler l'état des boutons. Ajoutons, par exemple, la classe `is-focused`, qui ajoute une bordure autour :

![Image](https://cdn-media-1.freecodecamp.org/images/1*mk04rubImZHTpMNPhsn-TQ.png)

Enfin, utilisons également l'un des modificateurs `has-*`. Ceux-ci contrôlent généralement ce qui se trouve à l'intérieur de l'élément. Dans notre cas, le texte. Ajoutons `has-text-weight-bold`.

Voici le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/1*H30F0Q92eL_IGipfEE3lWg.png)

Je vous recommande de jouer avec des combinaisons des différentes classes afin de comprendre à quel point ce système est flexible. Les combinaisons sont presque infinies. Consultez la [section boutons](https://bulma.io/documentation/elements/button/) dans la documentation pour plus d'informations.

### Colonnes

Au cœur de tout framework CSS se trouve la manière dont ils résolvent les colonnes, car cela est pertinent pour presque tous les sites web que vous construirez. Bulma est basé sur Flexbox, il est donc vraiment simple de créer des colonnes. Créons une ligne avec quatre colonnes.

```html
<div class="columns">  
  <div class="column">Première colonne</div>
  <div class="column">Deuxième colonne</div>
  <div class="column">Troisième colonne</div>
  <div class="column">Quatrième colonne</div>
</div>
```

Tout d'abord, nous créons un conteneur `<div>` avec une classe `columns`, puis nous donnons à chacun des enfants une classe `column`. Cela donne le résultat suivant :

![J'ai également ajouté une bordure autour des colonnes pour les rendre plus apparentes.](https://cdn-media-1.freecodecamp.org/images/1*p0XiWjzp00GGdgrmrCtwYA.png)

J'ai également ajouté une bordure autour des colonnes pour les rendre plus apparentes.

Notez que vous pouvez ajouter autant de colonnes que vous le souhaitez. Flexbox se charge de diviser l'espace équitablement entre elles.

Pour donner des couleurs aux colonnes, nous pouvons remplacer le texte à l'intérieur par une balise `<p>`, et lui donner la classe `notification` et un modificateur `is-*`. Par exemple :

Première colonne

Faisons cela en utilisant les modificateurs `is-info`, `is-success`, `is-warning` et `is-danger`, ce qui donne le résultat suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*7c9Ygeq5NbrBYQfnVUFDwA.png)

La classe `notification` est en fait destinée à alerter les utilisateurs sur quelque chose, car elle vous permet de remplir l'arrière-plan avec une couleur en utilisant les modificateurs `is-*`. Ici, cela fonctionne bien pour séparer les colonnes.

Nous pouvons également contrôler facilement la largeur d'une colonne. Ajoutons le modificateur `is-half` à la colonne verte.

```html
<div class="column is-half">    
```

Ce qui fait que la deuxième colonne occupe maintenant la moitié de la largeur, tandis que les trois autres prennent chacune un tiers de la moitié restante.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2oogxdeNyRZ7Y9oxLXNqBg.png)

Voici les options que vous pouvez utiliser pour contrôler la largeur des colonnes :

* `is-three-quarters`
* `is-two-thirds`
* `is-half`
* `is-one-third`
* `is-one-quarter`
* `is-four-fifths`
* `is-three-fifths`
* `is-two-fifths`
* `is-one-fifth`

### Hero

Enfin, apprenons également à créer un hero dans Bulma. Nous allons utiliser la balise sémantique `<section>`, et lui donner une classe `hero` et `is-info` pour lui donner une couleur. Nous devons également ajouter un enfant `<div>` avec la classe `hero-body`.

```html
<section class="hero is-success">  
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*mRUKo5nMrlRmNRlFhFxXqA.png)

Afin de faire en sorte que ce hero fasse quelque chose de significatif, nous allons ajouter un élément conteneur à l'intérieur du corps et ajouter un titre et un sous-titre.

```html
<div class="container">
  <h1 class="title">Titre principal</h1>
  <h2 class="subtitle">Sous-titre principal</h2>
</div>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*zgiaCn1QmbMn-r4d-p9exA.png)

Maintenant, cela commence à bien paraître ! Si nous voulons qu'il soit plus grand, nous pouvons simplement ajouter `is-medium` sur la balise `<section>` elle-même.

```html
<section class="hero is-info is-medium">  ...</section>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*7jJFSeUFbzSuavVUpVV7Zw.png)

Et c'est tout !

Vous avez maintenant une idée de base de comment Bulma fonctionne. Et le meilleur, c'est que le reste de la bibliothèque est aussi intuitif et facile que les concepts que vous avez vus jusqu'à présent. Donc, si vous comprenez cela, vous comprendrez le reste sans problème.

N'oubliez pas de consulter le [cours gratuit sur Bulma sur Scrimba](https://scrimba.com/g/gbulma?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gbulma_5_minute_article) si vous voulez en apprendre plus !

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le co-fondateur de [Scrimba](https://scrimba.com) - la manière la plus facile d'apprendre à coder. Vous devriez consulter notre [bootcamp de design web responsive](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gbulma_5_minute_article) si vous voulez apprendre à construire des sites web modernes de manière professionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gbulma_5_minute_article)_