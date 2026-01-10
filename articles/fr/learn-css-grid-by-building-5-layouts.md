---
title: Apprendre CSS Grid en construisant 5 mises en page en 17 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-27T00:48:35.000Z'
originalURL: https://freecodecamp.org/news/learn-css-grid-by-building-5-layouts
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/GridThumb.jpg
tags:
- name: CSS
  slug: css
- name: CSS Grid
  slug: css-grid
- name: Web Design
  slug: web-design
seo_title: Apprendre CSS Grid en construisant 5 mises en page en 17 minutes
seo_desc: 'By Thu Nghiem

  CSS Grid is a tool you can use to help create layouts for your website. It''s especially
  useful if you need to think about the position, layers, or sizes of different elements.

  CSS Grid is complicated and there are many things to learn. ...'
---

Par Thu Nghiem

CSS Grid est un outil que vous pouvez utiliser pour créer des mises en page pour votre site web. Il est particulièrement utile si vous devez réfléchir à la position, aux couches ou aux tailles des différents éléments.

CSS Grid est compliqué et il y a beaucoup de choses à apprendre. Mais la bonne nouvelle est que vous n'avez pas besoin de tout savoir en une seule fois.

Dans ce tutoriel, nous allons construire 5 mises en page différentes (expliquées comme cinq tâches séparées ci-dessous) avec CSS Grid. À la fin du tutoriel, vous serez prêt à utiliser CSS Grid dans vos prochains projets.

Si vous souhaitez coder en même temps, assurez-vous de télécharger les ressources :

* [Tâches-Design](https://bit.ly/38TbZum)
* [CSS-Grid-Starter](https://bit.ly/38MyQYy)

Voici une vidéo que vous pouvez regarder si vous souhaitez compléter cet article :

%[https://www.youtube.com/watch?v=CC2HkBZuReY]

Voici les deux premières mises en page que nous allons construire :

![Texte Alternatif](https://dev-to-uploads.s3.amazonaws.com/i/xciaiefay1v6in3hegmw.png)
_Tâche 1 et tâche 2_

## 1 : Comment construire une pile de crêpes avec CSS Grid

Pour la première tâche, nous devons créer une mise en page de pile de crêpes. Pour créer cette mise en page, nous pouvons faire trois rangées en utilisant `grid-template-rows: auto 1fr auto`. La deuxième rangée avec une valeur de `1fr` s'étendra autant que possible, tandis que les deux autres n'auront que suffisamment d'espace pour envelopper leur contenu.

Ainsi, pour obtenir cette mise en page, tout ce que nous avons à faire est de donner au conteneur les paramètres suivants :

```css
.task-1.container {
  display: grid;
  height: 100vh;

  grid-template-rows: auto 1fr auto;
}

```

et vous pouvez voir cette mise en page partout, par exemple, dans l'un de mes tutoriels :

![Texte Alternatif](https://dev-to-uploads.s3.amazonaws.com/i/srqeinbsoirmayvi2uvf.png)

Voici le [lien YouTube](https://youtu.be/d-qVF18Q7es) si vous souhaitez regarder et coder en même temps.

## 2 : Comment construire une mise en page de grille simple à 12 colonnes avec CSS Grid

La grille de base à 12 colonnes existe depuis toujours. Et avec CSS Grid, elle est encore plus facile à utiliser. Dans cette tâche simple, nous devons donner à `item-1` quatre colonnes et à `items-2` six colonnes.

Tout d'abord, nous devons créer 12 colonnes. Nous pouvons le faire avec `grid-template-columns: repeat(12, 1fr);` :

```css
.task-2.container {
  display: grid;
  height: 100vh;

  grid-template-columns: repeat(12, 1fr);
  column-gap: 12px;

  align-items: center;
}

```

Remarquez ici que nous avons également un écart de `12px` entre chaque colonne. Similaire à Flex, nous pouvons également utiliser `align-items` et `justify-content`.

La prochaine chose que nous devons faire est de dire quelles colonnes les éléments doivent occuper :

Pour l'élément 1, nous voulons qu'il commence à la colonne 2 et se termine à la colonne 6. Nous avons donc :

```css
.task-2 .item-1 {
  grid-column-start: 2;
  grid-column-end: 6;
}

```

Remarquez que l'élément n'inclura pas la colonne 6, seulement les colonnes 2, 3, 4 et 5.

Nous pouvons également obtenir le même effet en écrivant :

```css
.task-2 .item-1 {
  grid-column-start: 2;
  grid-column-end: span 4;
}

```

ou

```css
.task-2 .item-1 {
  grid-column: 2 / span 4;
}

```

Avec la même logique, nous aurons ce qui suit pour l'élément 2 :

```css
.task-2 .item-2 {
  grid-column: 6 / span 6;
}

```

Vous pouvez voir des mises en page à 12 colonnes partout – voici un tutoriel où j'utilise cette technique.

![Texte Alternatif](https://dev-to-uploads.s3.amazonaws.com/i/bj6vyu3smpr4705k8ynq.png)

Voici le [lien YouTube](https://www.youtube.com/watch?v=XXDOUuzzUOY&t=16s&ab_channel=ThuNghiem) si vous souhaitez regarder et coder en même temps.

## 3 : Comment construire une mise en page responsive avec et sans `grid-template-areas`

Je vais vous montrer _deux options_ ici. Pour la première option, nous allons utiliser la grille à 12 colonnes que nous avons apprise dans la deuxième tâche.

Pour la deuxième option, nous allons utiliser une propriété appelée `grid-template-areas`.

![Texte Alternatif](https://dev-to-uploads.s3.amazonaws.com/i/z65zhc0qjbotart85kny.png)

### Première option : Comment utiliser la grille à 12 colonnes

#### Mobile

C'est assez simple. Nous pouvons utiliser ce que nous avons appris de la première tâche, et faire en sorte que la section principale s'étende. Nous pouvons également donner à la grille un `gap: 24px` comme sur le bureau. Il y aura des colonnes, pas seulement des rangées :

```css
.task-3-1.container {
  display: grid;
  height: 100vh;

  grid-template-rows: auto auto 1fr auto auto auto;
  gap: 24px;
}

```

#### Tablette

Sur une tablette, où l'écran est plus large que `720px`, nous voulons avoir 12 colonnes et 4 rangées. La troisième rangée s'étendra autant que possible :

```css
@media (min-width: 720px) {
  .task-3-1.container {
    grid-template-columns: repeat(12, 1fr);
    grid-template-rows: auto auto 1fr auto;
  }
}

```

Maintenant que nous avons 12 colonnes, nous devons dire combien de colonnes chaque élément doit occuper :

```css
@media (min-width: 720px) {
 
  // La section d'en-tête prend 12 colonnes
  .task-3-1 .header {
    grid-column: 1 / span 12;
  }

  // La section de navigation prend également 12 colonnes
  .task-3-1 .navigation {
    grid-column: 1 / span 12;
  }

  // La section principale prend 10 colonnes à partir de la colonne 3
  .task-3-1 .main {
    grid-column: 3 / span 10;
  }

  // La barre latérale prend 2 colonnes à partir de la colonne 1
  .task-3-1 .sidebar {
    grid-column: 1 / span 2;
    grid-row: 3;
  }

  // La section des annonces prend 2 colonnes à partir de la colonne 1
  .task-3-1 .ads {
    grid-column: 1 / span 2;
  }

  // La section de pied de page prend 10 colonnes à partir de la colonne 3
  .task-3-1 .footer {
    grid-column: 3 / span 10;
  }
}

```

Remarquez ici que nous devons donner à `.task-3-1 .sidebar` `grid-row: 3;` car la barre latérale vient après la section `main` dans le DOM.

#### Bureau

Pour la vue bureau, nous travaillerons avec un écran plus grand que `1020px`. Comme nous avons déjà 12 colonnes, nous devons maintenant dire combien de colonnes il doit utiliser :

```css
@media (min-width: 1020px) {

  // La navigation prend 8 colonnes à partir de la colonne 3
  .task-3-1 .navigation {
    grid-column: 3 / span 8;
  }

  // La section principale prend 8 colonnes à partir de la colonne 3
  .task-3-1 .main {
    grid-column: 3 / span 8;
  }

  // La barre latérale commence à la rangée 2 et se termine à la rangée 4
  .task-3-1 .sidebar {
    grid-row: 2 / 4
  }

  // La section des annonces prend 2 colonnes à partir de la colonne 11
  // elle prend également 2 rangées à partir de la rangée 2 et se termine à la rangée 4
  .task-3-1 .ads {
    grid-column: 11 / span 2;
    grid-row: 2 / 4;
  }

  // La section de pied de page prend 12 colonnes à partir de la colonne 1
  .task-3-1 .footer {
    grid-column: 1 / span 12;
  }
}
```

### Exemple réel

Vous pouvez trouver une mise en page similaire sur la page d'accueil de Dev.to :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Screenshot-2021-01-27-at-0.36.34.png)

### Deuxième option : Comment utiliser `grid-template-areas`

Avant d'utiliser `grid-template-areas`, nous devons définir la zone de l'élément en utilisant `grid-area` :

```css
.task-3-2 .header {
  grid-area: header;
}

.task-3-2 .navigation {
  grid-area: nav;
}

.task-3-2 .ads {
  grid-area: ads;
}

.task-3-2 .sidebar {
  grid-area: sidebar;
}

.task-3-2 .main {
  grid-area: main;
}

.task-3-2 .footer {
  grid-area: footer;
}

```

Après avoir défini les zones des éléments, tout ce que nous avons à faire est de donner au conteneur la position en utilisant `grid-template-areas` :

#### Mobile

```css
.task-3-2.container {
  display: grid;
  height: 100vh;

  gap: 24px;

  // Création de 6 rangées et la 3ème rangée s'étend autant que possible
  grid-template-rows: auto auto 1fr auto auto auto;

  // Définition du modèle
  grid-template-areas:
    "header"
    "nav"
    "main"
    "sidebar"
    "ads"
    "footer";
}

```

Ainsi, sur mobile, nous créons 1 colonne et 6 rangées. Et la rangée numéro 3, qui est la rangée principale, doit s'étendre autant que possible.

Cela facilite également les choses si, plus tard, vous souhaitez changer l'ordre/la position de l'élément. Par exemple, si nous voulons avoir la navigation avant l'en-tête, nous pouvons faire :

```css
...
 grid-template-areas:
    "nav"
    "header"
    "main"
    "sidebar"
    "ads"
    "footer";
...
```

#### Tablette

```css
@media (min-width: 720px) {
  .task-3-2.container {
    // Création de 4 rangées et la 3ème rangée s'étend autant que possible
    grid-template-rows: auto auto 1fr auto;
    
    // Définition du modèle (3 colonnes)
    grid-template-areas:
      "header header header"
      "nav nav nav "
      "sidebar main main"
      "ads footer footer";
  }
}

```

Avec le code ci-dessus, si l'écran est plus large que 720px, nous voulons créer 3 colonnes et 4 rangées. L'en-tête et la navigation occupent tous deux 3 colonnes.

Sur la troisième et quatrième rangée, la barre latérale et les annonces prennent 1 colonne, tandis que le contenu principal et le pied de page prennent 2 colonnes.

#### Bureau

```css
@media (min-width: 1020px) {
  .task-3-2.container {
    // Création de 4 rangées et la 3ème rangée s'étend autant que possible
    grid-template-rows: auto auto 1fr auto;
    
    // Définition du modèle (4 colonnes)
    grid-template-areas:
      "header header header header"
      "sidebar nav nav ads"
      "sidebar main main ads"
      "footer footer footer footer";
  }
}


```

Ici, nous trouvons une logique similaire à la vue tablette. Pour le bureau, nous créons 4 colonnes et 4 rangées et le placement selon la valeur de `grid-template-areas`.

### Lequel choisir ?

**Utilisation de la grille à 12 colonnes** :

✅ Facile et rapide à démarrer
✅ Facile à maintenir pour les mises en page axées sur les colonnes
❌ Difficile à organiser les éléments dans des mises en page complexes

Vous devriez utiliser la grille à 12 colonnes pour des mises en page moins complexes qui se concentrent principalement sur l'arrangement des colonnes.

**Utilisation de `grid-template-areas`** :

✅ Flexible pour les mises en page complexes
✅ Facile à visualiser
❌ Prend plus de temps à implémenter

Vous devriez utiliser `grid-template-areas` pour des mises en page plus complexes où vous devez vous soucier des positions ou des tailles de nombreux éléments.

Les deux options ont des avantages et des inconvénients, mais vous devriez choisir celle qui est la plus facile pour vous et qui a du sens dans votre scénario particulier.

## 4 : Comment construire une mise en page responsive sans requêtes média dans CSS Grid

![Texte Alternatif](https://dev-to-uploads.s3.amazonaws.com/i/61w4dsetc7xtq4uspz8v.png)

C'est surprenant de voir à quel point c'est simple. Nous pouvons le faire avec une seule ligne de code : `grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));`, comme ceci :

```css
.task-4.container {
  display: grid;
  gap: 24px;

  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
}

```

Nous venons de créer une mise en page de colonnes flexible et avons spécifié que la colonne ne doit jamais être inférieure à 150px et doit partager l'espace de manière égale.

## 5 : Comment construire une grille d'échecs 12 x 12 avec CSS Grid

Pour la dernière tâche, je veux vous montrer que non seulement nous pouvons définir le nombre de colonnes, mais nous pouvons également définir le nombre de rangées en utilisant CSS Grid.

```css
.task-5.container {
  display: grid;
  height: 100vh;

  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: repeat(12, 1fr);
}

```

Maintenant, nous pouvons placer les éléments où nous voulons. Donc pour créer cette mise en page :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Screenshot-2021-01-27-at-0.49.40.png)

Nous pouvons faire ceci :

```css
...
// Le premier élément commence à la colonne 1 et s'étend sur 3 colonnes
// et à partir de la rangée 1 et s'étend sur 3 colonnes
.task-5 .item-1 {
    grid-row: 1 / span 3;
    grid-column: 1 / span 3;
}

// Le deuxième élément commence à la colonne 4 et s'étend sur 3 colonnes
// et à partir de la rangée 4 et s'étend sur 3 colonnes
.task-5 .item-2 {
    grid-row: 4 / span 3;
    grid-column: 4 / span 3;
}

// Le premier élément commence à la colonne 7 et s'étend sur 3 colonnes
// et à partir de la rangée 7 et s'étend sur 3 colonnes
.task-5 .item-3 {
    grid-row: 7 / span 3;
    grid-column: 7 / span 3;
}

// Le premier élément commence à la colonne 10 et s'étend sur 3 colonnes
// et à partir de la rangée 10 et s'étend sur 3 colonnes
.task-5 .item-4 {
    grid-row: 10 / span 3;
    grid-column: 10 / span 3;
}
```

## Conclusion

Merci d'avoir lu cet article. Ce sujet appartient à la série de vidéos que je mettrai à jour sur [Learn.DevChallenges.io](https://learn.devchallenges.io/). Donc pour rester à jour, suivez-moi sur les réseaux sociaux ou abonnez-vous à ma [Chaîne YouTube](https://www.youtube.com/channel/UCmSmLukBF--YrKZ2g4akYAQ?sub_confirmation=1). Sinon, bon codage et à bientôt dans la prochaine vidéo et les prochains articles 👋.

## __________ 🐣 À propos de moi __________

Je suis un développeur full-stack, un designer UX/UI et un créateur de contenu. Vous pouvez mieux me connaître dans cette courte vidéo :

%[https://youtu.be/qCkmFd-72JY]

* Je suis le fondateur de [DevChallenges](https://devchallenges.io/)
* Abonnez-vous à ma [Chaîne YouTube](https://www.youtube.com/channel/UCmSmLukBF--YrKZ2g4akYAQ?sub_confirmation=1)
* Suivez-moi sur [Twitter](https://twitter.com/thunghiemdinh)
* Rejoignez [Discord](https://discord.com/invite/3R6vFeM)