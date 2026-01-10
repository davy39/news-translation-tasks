---
title: Comment créer facilement des thèmes avec les variables CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-23T17:09:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-easily-create-themes-with-css-variables-2d0f4cfa5b9a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*blhp0Jh_MceZD4hnTgX6qw.png
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
seo_title: Comment créer facilement des thèmes avec les variables CSS
seo_desc: 'By Per Harald Borgen

  One of the best use cases for CSS Variables is theme creation. And by that, I don’t
  only mean changing themes for your entire app, as that’s probably not something
  you need to do very often. What’s more relevant is the ability to...'
---

Par Per Harald Borgen

L'un des meilleurs cas d'utilisation des variables CSS est la création de thèmes. Et par là, je ne veux pas dire uniquement changer les thèmes de toute votre application, car ce n'est probablement pas quelque chose que vous devez faire très souvent. Ce qui est plus pertinent, c'est la capacité de créer facilement des *thèmes spécifiques aux composants*.

Cela pourrait, par exemple, être lorsque vous devez marquer un produit de commerce électronique comme *ajouté au panier*. Ou peut-être que votre site a une section admin qui inclut une section de barre latérale plus sombre.

Les **variables CSS** vous permettent de le faire de manière plus simple et plus flexible que ce qui était possible auparavant. Dans cet article, je vais expliquer exactement comment.

J'ai également créé un screencast sur la création de thèmes dans mon cours gratuit [8-part CSS Variables course.](https://scrimba.com/g/gcssvariables?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_create_themes) Si vous êtes intéressé à en apprendre plus sur le cours, consultez [cet article](https://medium.freecodecamp.org/want-to-learn-css-variables-heres-my-free-8-part-course-f2ff452e5140).

### L'installation

Nous allons travailler avec un site portfolio comme exemple. Notre objectif est de pouvoir mettre en avant l'un des projets de notre portfolio afin qu'il se distingue du reste. Techniquement, nous allons le faire en ajoutant une classe à l'élément spécifique que nous voulons mettre en avant.

Voici à quoi ressemble le site portfolio initialement :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Eu0wU_hiyqOqrhyxNamvsg.png)

Je ne vais pas parler du HTML du site, car il est assez simple, et je suppose que vous connaissez le HTML. Cependant, si vous êtes intéressé à bidouiller le code, j'ai créé un terrain de jeu Scrimba pour cela [ici.](https://scrimba.com/c/cBBeZuL?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_create_themes)

Maintenant, passons directement au CSS. Voici notre feuille de style avant que nous ayons commencé à utiliser les variables CSS :

```css
html, body {  
  background: #ffeead;  
  color: #ff6f69;  
}

h1, p {  
  color: #ff6f69;  
}

#navbar a {  
  color: #ff6f69;  
}

.item {  
  background: #ffcc5c;  
}

button {  
  background: #ff6f69;  
  color: #ffcc5c;  
}

```

Comme vous pouvez le voir, nous n'utilisons ici que trois couleurs : `#ffeead`, `#ff9f96` et `#ffcc5c`. Cependant, nous les réutilisons beaucoup. C'est donc un cas d'utilisation parfait pour les variables CSS.

Pour commencer à les utiliser, nous devons d'abord déclarer nos variables. Nous allons le faire dans la pseudo-classe `:root` :

```css
:root {  
  --red: #ff6f69;  
  --beige: #ffeead;  
  --yellow: #ffcc5c;  
}

```

Ensuite, nous allons simplement remplacer nos valeurs hexadécimales par les variables :

```css
html, body {  
  background: var(--beige);  
  color: var(--red);  
}

h1, p {  
  color: var(--red);  
}

#navbar a {  
  color: var(--red);  
}

.item {  
  background: var(--yellow);  
}

button {  
  background: var(--red);  
  color: var(--yellow);  
}

```

Maintenant, nous avons le pouvoir des variables dans notre CSS, ce qui signifie que nous pouvons simplement changer le `--red` en autre chose, et il sera mis à jour dans tout notre site.

Si vous avez du mal à comprendre ce qui se passe ici, veuillez consulter mon article [Learn CSS Variables in 5 minutes](https://medium.freecodecamp.org/learn-css-variables-in-5-minutes-80cf63b4025d), ou inscrivez-vous au [cours.](https://scrimba.com/g/gcssvariables?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_create_themes)

### Créer un thème

Maintenant, créons le thème. Nous voulons la capacité d'ajouter une classe `.featured` à l'un de nos quatre éléments de projet, et ainsi faire en sorte que cet élément se distingue des autres. Plus précisément, nous allons changer le rouge en `#ff5564` et le jaune en `#ffe55b`.

Voici à quoi cela ressemblera dans le balisage :

```html
<div class="item **featured**">  
  <h1>project d</h1>  
  <button>learn more</button>  
</div>

```

Ce changement devrait affecter le style à quatre endroits différents :

* couleur de fond de la `<div>`
* couleur du `<h1>`
* couleur de fond du `<button>`
* couleur du `<button>`

#### L'ancienne méthode

La façon dont nous devions résoudre cela auparavant était de créer un sélecteur CSS personnalisé pour chaque élément à l'intérieur de l'élément `.featured`, comme ceci :

```css
.featured {  
  background: #ffe55b;  
}

.featured > h1 {  
  color: #ff5564;  
}

.featured > button {  
  background: #ff5564;   
  color: #ffe55b;  
}

```

Cette approche n'est pas très flexible. Si vous deviez ajouter un autre élément à l'intérieur de vos éléments de portfolio, vous devriez écrire des sélecteurs spécifiques pour eux également.

#### La nouvelle méthode

Avec les variables CSS, cependant, cela devient beaucoup plus facile. Nous allons simplement remplacer les variables à l'intérieur de la classe `.featured` comme ceci :

```css
.featured {  
  --yellow: #ffe55b;  
  --red: #ff5564;  
}

```

Comme les variables CSS sont héritées, tous les éléments à l'intérieur de `.featured` qui référencent `--red` ou `--yellow` utilisent maintenant les valeurs locales et non les valeurs globales. Ainsi, les éléments `<button>` ou `<h1>` utilisent automatiquement les valeurs locales pour les variables.

Voici comment cela se présente sur la page.

![Comme vous pouvez le voir, l'élément 'project d' semble un peu différent des autres.](https://cdn-media-1.freecodecamp.org/images/1*QYSniAuCy5MkF202RvMUDQ.png)

Comme vous pouvez le voir, l'élément 'project d' semble un peu différent des autres.

Sympa, non ?

Imaginez simplement comment cela serait si nous construisions un composant plus complexe, par exemple, un élément de produit dans une application de commerce électronique. Il pourrait inclure des titres, des sous-titres, des paragraphes, des images, des légendes, des boutons, des évaluations et bien plus encore. Il est beaucoup plus facile et plus flexible de simplement inverser la valeur de certaines variables au lieu de créer des sélecteurs personnalisés pour chacun des descendants.

Si vous êtes intéressé à en apprendre plus sur cette technologie, veuillez consulter mon cours interactif gratuit [8-part interactive CSS Variables course](https://scrimba.com/g/gcssvariables?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_create_themes) sur Scrimba.

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le co-fondateur de [Scrimba](https://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_create_themes) – la manière la plus facile d'apprendre à coder. Vous devriez consulter notre [bootcamp de design web responsive](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_create_themes) si vous voulez apprendre à construire des sites web modernes de manière professionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gcssvariables_create_themes)_