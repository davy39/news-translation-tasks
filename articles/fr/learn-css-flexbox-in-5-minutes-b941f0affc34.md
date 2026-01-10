---
title: Apprendre CSS Flexbox en 5 minutes - Un tutoriel pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-13T18:21:53.000Z'
originalURL: https://freecodecamp.org/news/learn-css-flexbox-in-5-minutes-b941f0affc34
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SDah34Yygu4CkLUcdsSytQ.png
tags:
- name: coding
  slug: coding
- name: CSS
  slug: css
- name: responsive design
  slug: responsive-design
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Apprendre CSS Flexbox en 5 minutes - Un tutoriel pour débutants
seo_desc: 'By Per Harald Borgen

  A quick introduction to the popular layout module

  In this post, you’ll learn the basics of CSS Flexbox, which has become a must-have
  skill for web developers and designers in the last couple of years.

  We’ll be using a navbar as a...'
---

Par Per Harald Borgen

#### Une introduction rapide au module de mise en page populaire

Dans cet article, vous apprendrez les bases de CSS Flexbox, qui est devenu une compétence indispensable pour les développeurs et designers web ces dernières années.

Nous utiliserons une barre de navigation comme exemple, car c'est un cas d'utilisation très typique pour Flexbox. Cela vous introduira à ses propriétés les plus utilisées tout en laissant de côté celles qui ne sont pas aussi critiques.

J'ai également créé un cours gratuit en 12 parties sur Flexbox. [Découvrez-le ici](https://scrimba.com/g/gflexbox?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gflexbox_5_minute_article) si vous êtes intéressé !

Maintenant, commençons !

### Votre première mise en page Flexbox

Les deux principaux composants d'une mise en page Flexbox sont le **conteneur** et les **éléments**.

Voici le HTML pour notre exemple, qui contient un conteneur avec trois éléments :

```html
<nav class="container">  
  <div>Accueil</div>  
  <div>Recherche</div>  
  <div>Déconnexion</div>  
</nav>

```

Avant de transformer cela en une mise en page Flexbox, les éléments seront empilés les uns sur les autres comme ceci :

![J'ai ajouté un peu de style, mais cela n'a rien à voir avec Flexbox.](https://cdn-media-1.freecodecamp.org/images/1*egtZCVQirK8mJiacL98eBA.png)

J'ai ajouté un peu de style, mais cela n'a rien à voir avec Flexbox.

Pour transformer cela en une mise en page Flexbox, nous donnerons simplement au **conteneur** la propriété CSS suivante :

```css
.container {  
    display: flex;  
}

```

Cela positionnera automatiquement les éléments correctement le long de l'axe horizontal.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DMA-NUgXG15-qDBAnLu3tA.png)

Si vous souhaitez voir le code réel, vous pouvez vous rendre sur [ce terrain de jeu Scrimba.](https://scrimba.com/c/c3zpnuB?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gflexbox_5_minute_article)

Maintenant, mélangeons un peu ces éléments.

### Justifier le contenu et aligner les éléments

**Justify-content** et **align-items** sont deux propriétés CSS qui nous aident à distribuer les éléments dans le conteneur. Elles contrôlent la manière dont les éléments sont positionnés le long de l'**axe principal** et de l'**axe transversal**.

Dans notre cas (mais pas toujours), l'axe principal est horizontal et l'axe transversal est vertical :

![Image](https://cdn-media-1.freecodecamp.org/images/1*SDah34Yygu4CkLUcdsSytQ.png)

Dans cet article, nous ne regarderons que `justify-content`, car j'ai constaté que j'utilise beaucoup plus cette propriété que `align-items`. Cependant, dans [mon cours Flexbox](https://scrimba.com/g/gflexboxhttps://scrimba.com/c/c3zpnuB?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gflexbox_5_minute_article), j'explique les deux propriétés en détail.

Centrons tous les éléments le long de l'**axe principal** en utilisant `justify-content` :

```css
.container {  
    display: flex;  
    justify-content: center;  
}

```

![Image](https://cdn-media-1.freecodecamp.org/images/1*1NQGeHIcXFdlYsNwP-kuXQ.png)

Ou nous pouvons le définir sur `space-between`, ce qui ajoutera de l'espace entre les éléments, comme ceci :

```css
.container {  
    display: flex;  
    justify-content: space-between;  
}

```

![Image](https://cdn-media-1.freecodecamp.org/images/1*rYctxBrNeO2019wscgaaQA.png)

Voici les valeurs que vous pouvez définir pour `justify-content` :

* flex-start (**par défaut**)
* flex-end
* center
* space-between
* space-around
* space-evenly

Je vous recommande de jouer avec ces valeurs et de voir comment elles se comportent sur la page. Cela devrait vous donner une compréhension appropriée du concept.

### Contrôler un seul élément

Nous pouvons également contrôler des **éléments** individuels. Supposons, par exemple, que nous voulons garder les deux premiers éléments sur le côté gauche, mais déplacer le bouton `déconnexion` sur le côté droit.

Pour ce faire, nous utiliserons la bonne vieille technique consistant à définir la marge sur `auto`.

```css
.logout {  
    margin-left: auto;  
}

```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Z9GbnGBvlJdIYjiH3DQbbQ.png)

Si nous voulions que l'élément `recherche` et l'élément `déconnexion` soient poussés vers le côté droit, nous ajouterions simplement la `margin-left` à l'élément `recherche` à la place.

```css
.search {  
    margin-left: auto;  
}

```

Cela poussera l'élément de recherche aussi loin que possible vers le côté droit, ce qui poussera à son tour l'élément de déconnexion avec lui :

![Image](https://cdn-media-1.freecodecamp.org/images/1*C5bwvvQjhgnrufVNo4jfwA.png)

### La propriété flex

Jusqu'à présent, nous n'avons eu que des éléments de largeur fixe. Mais que faire si nous voulons qu'ils soient responsives ? Pour y parvenir, nous avons une propriété appelée `flex`. Elle rend les choses beaucoup plus faciles que l'ancienne méthode utilisant des pourcentages.

Nous ciblerons simplement tous les éléments et leur donnerons une valeur `flex` de `1`.

```css
.container > div {  
    flex: 1;  
}

```

![Image](https://cdn-media-1.freecodecamp.org/images/1*fI8C475J2qbF5LMu82voEQ.png)

Comme vous pouvez le voir, cela étire les éléments pour remplir tout le conteneur.

Dans de nombreux cas, vous voudrez probablement que l'un des éléments prenne la largeur supplémentaire, et ainsi ne définir qu'un seul d'entre eux pour avoir une largeur flexible. Nous pouvons, par exemple, faire en sorte que l'élément `recherche` prenne tout l'espace supplémentaire :

```css
.search {  
    flex: 1;  
}

```

![Image](https://cdn-media-1.freecodecamp.org/images/1*7nmqNtWDHHh7pCgsUAUXfw.png)

Avant de terminer cet article, je tiens à mentionner que la propriété flex est en réalité un raccourci pour trois propriétés : **flex-grow**, **flex-shrink** et **flex-basis**. Cependant, apprendre ces propriétés prend plus de cinq minutes, donc cela dépasse le cadre de ce tutoriel.

Si vous êtes intéressé à les apprendre, je vous explique en détail les trois propriétés dans [mon cours gratuit sur Flexbox.](https://scrimba.com/g/gflexboxhttps://scrimba.com/c/c3zpnuB?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gflexbox_5_minute_article)

Maintenant que vous avez appris les bases, vous serez définitivement prêt à suivre mon cours complet et à devenir un maître de Flexbox !

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le co-fondateur de [Scrimba](https://scrimba.comhttps://scrimba.com/c/c3zpnuB?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gflexbox_5_minute_article) – la manière la plus simple d'apprendre à coder. Vous devriez consulter notre [bootcamp de design web responsif](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gflexbox_5_minute_article) si vous souhaitez apprendre à construire des sites web modernes de manière professionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gflexbox_5_minute_article)_