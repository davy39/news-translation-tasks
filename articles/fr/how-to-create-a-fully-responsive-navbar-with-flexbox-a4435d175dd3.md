---
title: 'Tutoriel Flexbox : Apprenez à coder une barre de navigation responsive avec
  CSS Flexbox'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-29T09:07:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-fully-responsive-navbar-with-flexbox-a4435d175dd3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CZikqoB4iZIIrV_rAW_qdg.gif
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Tutoriel Flexbox : Apprenez à coder une barre de navigation responsive
  avec CSS Flexbox'
seo_desc: 'By Per Harald Borgen

  In this article, I’ll explain how to create a navbar which adapts to various screen
  sizes using Flexbox along with media queries.

  This tutorial can also be found as an interactive screencast in my free Flexbox
  course at Scrimba.

  ...'
---

Par Per Harald Borgen

Dans cet article, je vais expliquer comment créer une barre de navigation qui s'adapte à différentes tailles d'écran en utilisant Flexbox ainsi que des media queries.

Ce tutoriel peut également être trouvé sous forme de screencast interactif [dans mon cours gratuit sur Flexbox chez Scrimba](https://scrimba.com/g/gflexbox?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gflexbox_tutorial_article).

Pour en savoir plus sur le cours, consultez [cet](https://medium.freecodecamp.org/i-just-launched-a-free-full-length-flexbox-course-where-you-can-build-projects-interactively-1860e3d3c4af) article.

#### L'installation

Commençons par le balisage pour une barre de navigation très simple :

```html
<nav>  
  <ul class="container">  
    <li>Accueil</li>  
    <li>Profil</li>  
    <li class="search">  
      <input type="text" class="search-input" placeholder="Rechercher">  
    </li>  
    <li>Déconnexion</li>  
  </ul>  
</nav>

```

L'élément `<ul>` est notre conteneur flex et les éléments `<li>` sont nos éléments flex. Pour en faire une mise en page Flexbox, nous allons faire :

```css
.container {  
  display: flex;  
}

```

Ce qui donnera le résultat suivant :

![J'ai ajouté un peu de style, mais cela n'a rien à voir avec Flexbox.](https://cdn-media-1.freecodecamp.org/images/1*bEclbRvpLBeEd8oRddNFaQ.png)

  
J'ai ajouté un peu de style, mais cela n'a rien à voir avec Flexbox.

Comme vous pouvez le voir, nous avons un peu d'espace supplémentaire sur le côté droit. Cela est dû au fait que Flexbox dispose les éléments de gauche à droite, et chaque élément n'est large que ce que son contenu le force à être.

Puisque le conteneur flex est par défaut un élément de niveau bloc (et est plus large que les quatre éléments), nous obtenons l'écart à la fin.

La raison pour laquelle l'élément de recherche est plus large que les autres est que les champs de saisie sont par défaut définis à `size="20"`, que les différents navigateurs et systèmes d'exploitation interprètent de différentes manières.

### Réactivité #1

Pour donner à notre barre de navigation une réactivité de base, nous allons simplement donner à l'élément de recherche une valeur flex de 1.

```css
.search {  
  flex: 1;  
}

```

Cela entraîne l'expansion et la réduction de l'élément de recherche avec la largeur du conteneur, ce qui signifie que nous n'aurons pas d'espace supplémentaire sur le côté droit.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BZnmPAc4fNPNGkjCPS22kw.gif)

Bien qu'il soit logique de faire en sorte que l'élément de recherche s'agrandisse tandis que les autres restent fixes, on pourrait soutenir qu'il peut devenir trop large par rapport aux autres. Donc, si vous préférez que tous les éléments s'agrandissent avec la largeur du conteneur, vous pouvez simplement donner à tous les éléments une valeur `flex` de 1.

```css
.container > li {  
  flex: 1;  
}

```

Voici comment cela se passe :

![Image](https://cdn-media-1.freecodecamp.org/images/1*pXzuCWHyvuyQ3JZQPoWclA.gif)

Vous pouvez également donner aux éléments différentes valeurs flex, ce qui les ferait grandir à des vitesses différentes. N'hésitez pas à expérimenter cela [dans ce terrain de jeu Scrimba.](https://scrimba.com/c/cpJV3S3?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gflexbox_tutorial_article)

Pour le reste du tutoriel, nous continuerons avec la première solution, où les éléments de recherche sont les seuls à avoir une valeur `flex`.

### Réactivité #2

Notre barre de navigation fonctionne bien sur les écrans larges. Cependant, sur des écrans plus étroits, elle rencontre des problèmes, comme vous pouvez le voir ici :

![Image](https://cdn-media-1.freecodecamp.org/images/1*PCmf5iZCXLYIckEjMBbv4g.gif)

À un moment donné, il n'est plus viable d'avoir tous les éléments sur la même ligne, car le conteneur devient trop étroit. Pour résoudre ce problème, nous allons ajouter une media query où nous allons diviser nos quatre éléments en deux lignes. La media query se déclenchera lorsque l'écran sera large de 600px :

```css
@media all and (max-width: 600px) {  
    
  .container {  
    flex-wrap: wrap;  
  }  
    
  .container > li {  
    flex-basis: 50%;  
  }

}

```

Tout d'abord, nous permettons à la mise en page Flexbox de s'enrouler avec `flex-wrap`. Cela est par défaut défini sur `nowrap`, nous devons donc le changer en `wrap`.

La chose suivante que nous faisons est de définir la valeur `flex-basis` des éléments à 50%. Cela indique à Flexbox de faire en sorte que chaque élément prenne 50% de la largeur disponible, ce qui donne deux éléments par ligne, comme ceci :

![Note : J'ai également centré le texte de l'espace réservé dans le champ de recherche.](https://cdn-media-1.freecodecamp.org/images/1*Xr3MxBFPb2-GTX7cDuKbVQ.png)

  
Note : J'ai également centré le texte de l'espace réservé dans le champ de recherche.

Nous avons maintenant deux états différents. Cependant, cette mise en page ne fonctionne toujours pas sur les très petits écrans, comme les écrans mobiles en mode portrait.

Si nous continuons à réduire l'écran, il finira par ressembler à l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*k_HzX7UVF152TVc1sfbhKg.png)

Ce qui s'est passé ici, c'est que la deuxième ligne ne peut plus contenir deux éléments.

Les éléments de déconnexion et de recherche sont simplement trop larges, car vous ne pouvez pas les réduire en dessous de leur largeur minimale, qui est la largeur dont ils ont besoin pour remplir le contenu à l'intérieur.

Les éléments d'accueil et de profil peuvent encore apparaître sur la même ligne, donc Flexbox leur permettra de le faire. Ce n'est pas optimal, car nous voulons que toutes nos lignes se comportent de la même manière.

### Réactivité #3

Donc, dès qu'une des lignes ne peut plus contenir deux éléments en largeur, nous voulons qu'aucune des lignes n'ait deux éléments en largeur. En d'autres termes, sur les très petits écrans, nous allons en fait rendre la barre de navigation verticale. Nous allons empiler les éléments les uns sur les autres.

Pour y parvenir, nous devons simplement changer notre largeur de 50% à 100%, afin que chaque ligne ne contienne qu'un seul élément. Nous allons ajouter ce point d'arrêt à 400px.

```css
@media all and (max-width: 400px) {  
  .container > li {  
    flex-basis: 100%;  
  }  
  .search {  
    order: 1;  
  }  
}

```

En plus de cela, je souhaite placer l'élément de recherche en bas, c'est pourquoi je cible également la recherche et lui donne une valeur `order` de 1.

Cela donne le résultat suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*6Xgs5YcKu9Obq3dgk4qLZA.png)

La raison pour laquelle `order: 1;` place l'élément de recherche en bas est que les éléments flex ont par défaut une valeur de zéro, et tout élément ayant une valeur supérieure à celle-ci sera placé après les autres.

Pour voir comment tout cela se passe, voici le gif du haut de l'article :

![Image](https://cdn-media-1.freecodecamp.org/images/1*CZikqoB4iZIIrV_rAW_qdg.gif)

Félicitations ! Vous savez maintenant comment créer une barre de navigation entièrement responsive en utilisant Flexbox et des media queries.

Si vous êtes intéressé à en savoir plus sur Flexbox, je vous recommande de consulter [mon cours gratuit chez Scrimba.](https://scrimba.com/g/gflexbox?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gflexbox_tutorial_article)

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le co-fondateur de [Scrimba](https://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gflexbox_tutorial_article) – la manière la plus facile d'apprendre à coder. Vous devriez consulter notre [bootcamp de design web responsive](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gflexbox_tutorial_article) si vous voulez apprendre à construire des sites web modernes de manière professionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gflexbox_tutorial_article)_