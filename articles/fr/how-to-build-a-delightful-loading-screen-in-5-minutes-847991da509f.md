---
title: Comment créer un écran de chargement agréable en 5 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-21T04:37:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-delightful-loading-screen-in-5-minutes-847991da509f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AF1rXY_iumutiVOMSXf_LQ.gif
tags:
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment créer un écran de chargement agréable en 5 minutes
seo_desc: 'By Emmanuel Ohans

  First, here is what we will build. Set your timer!


  _Here’s the [DEMO](https://codepen.io/ohansemmanuel/pen/ZxOjGx" rel="noopener" target="blank"
  title=") we’ll build.

  Does this look familiar?

  If yes, that’s because you’ve seen this...'
---

Par Emmanuel Ohans

Tout d'abord, voici ce que nous allons construire. Réglez votre minuteur !

![Image](https://cdn-media-1.freecodecamp.org/images/W4zbRnaocoYYCf1YLdaAsMdLXnfm7-Dhclyc)
_Voici la [DÉMO](https://codepen.io/ohansemmanuel/pen/ZxOjGx" rel="noopener" target="_blank" title=") que nous allons construire._

Cela vous semble familier ?

Si oui, c'est parce que vous l'avez vu quelque part — [Slack](https://slack.com) !

Apprenons quelques choses en recréant cela avec juste du CSS et un peu de bon vieux HTML.

Si vous êtes enthousiaste à l'idée d'écrire du code, allez sur [Codepen](http://codepen.io) et créez un nouveau pen.

Maintenant, c'est parti !

#### 1. Le Balisage

Le balisage requis pour cela est assez simple. Le voici :

```
<section class="loading">
```

```
Pour de nouvelles couleurs de barre latérale, cliquez sur le nom de votre espace de travail, puis sur Préférences > Barre latérale > Thème
```

```
<span class="loading__author"> - Vos amis chez Slack</span>;    <span class="loading__anim"></span>
```

```
</section>
```

Simple, n'est-ce pas ?

Si vous n'êtes pas sûr de savoir pourquoi les noms de classe ont des tirets bizarres, j'ai expliqué la raison derrière cela dans [cet article](https://medium.freecodecamp.org/css-naming-conventions-that-will-save-you-hours-of-debugging-35cea737d849).

Il y a un tas de texte, et une balise `.loading__anim` pour "impersonner" l'icône animée.

Le résultat de cela est la vue simple ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/QVYp5Lz5g0YvKYbO1Stn2RQ9EjziWauo0a1r)
_Pas si mal, n'est-ce pas ?_

#### 2. Centrer le Contenu

Le résultat n'est pas le plus joli à regarder. Assurons-nous que l'élément de section `.loading` entier soit centré dans la page.

```
body {  display: flex;  justify-content: center;  align-items: center;  min-height: 100vh;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/3XoIKO5ikLjWJdBaJa2S0lgf25W3djMnLsJV)
_Maintenant centré !_

Cela semble mieux ?

#### 3. Styliser le Texte de Chargement

Je sais. Nous arriverons bientôt à la partie animée. Pour l'instant, stylisons le texte `.loading` pour qu'il ait l'air beaucoup mieux.

```
.loading {  max-width: 50%;  line-height: 1.4;  font-size: 1.2rem;  font-weight: bold;  text-align: center;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/ZoTXHeMu0cqNBwyUuaccOeuA6yigyvMhR7u7)

#### 4. Styliser le Texte de l'Auteur pour qu'il ait l'air légèrement différent.

```
.loading__author {  font-weight: normal;  font-size: 0.9rem;  color: rgba(189,189,189 ,1);  margin: 0.6rem 0 2rem 0;  display: block;}
```

Et voilà !

![Image](https://cdn-media-1.freecodecamp.org/images/z6mbVcXOJZ0gBMogVez923ylx5Bqmjbkegsm)

#### 5. Créer le Chargeur Animé

L'étape tant attendue est arrivée. Ce sera la plus longue des étapes, car je vais prendre le temps de m'assurer que vous comprenez comment cela fonctionne.

Si vous êtes bloqué, laissez un commentaire et je serai heureux de vous aider.

Hé, regardez à nouveau le chargeur.

![Image](https://cdn-media-1.freecodecamp.org/images/3HiHd00VoFzzTMjo80NwZP6M3FTmFcgnZlRr)

Vous remarquerez que la moitié de son trait est bleue et l'autre moitié est grise. D'accord, c'est réglé. De plus, les éléments `HTML` ne sont pas arrondis par défaut. Tout est un élément _box_. Le premier vrai défi sera de donner à l'élément `.loading__anim` des bordures à moitié.

Ne vous inquiétez pas si vous ne comprenez pas cela encore. Je reviendrai dessus.

Tout d'abord, définissons les dimensions du chargeur.

```
.loading__anim {  width: 35px;  height: 35px; }
```

Pour l'instant, le chargeur est sur la même ligne que le texte. C'est parce que c'est un élément `span` qui se trouve être un élément **inline** `HTML`.

Assurons-nous que le chargeur soit sur une autre ligne, c'est-à-dire qu'il commence sur une autre ligne contrairement au comportement par défaut des éléments `inline`.

```
.loading__anim {   width: 35px;   height: 35px;   display: inline-block;  }
```

Enfin, assurons-nous que le chargeur ait une bordure définie.

```
.loading__anim {   width: 35px;   height: 35px;   display: inline-block;   border: 5px solid rgba(189,189,189 ,0.25);  }
```

Cela donnera une bordure _grisâtre_ de `5px` autour de l'élément.

Voici le résultat de cela.

![Image](https://cdn-media-1.freecodecamp.org/images/hc9QIUgPfSH6F0T7xggQ8FD93L2S-hoXDsiZ)
_Vous voyez les bordures grises, n'est-ce pas ?_

Pas si génial — encore. Améliorons cela.

Un élément a quatre côtés, `top`, `bottom`, `left`, et `right`

La déclaration `border` que nous avons définie précédemment a été appliquée à tous les côtés de l'élément.

Pour créer le chargeur, nous avons besoin que deux côtés de l'élément aient des couleurs différentes.

Peu importe les côtés que vous choisissez. J'ai utilisé les côtés `top` et `left` ci-dessous

```
.loading__anim {  width: 35px;  height: 35px;  display: inline-block;  border: 5px solid rgba(189,189,189 ,0.25);  border-left-color: rgba(3,155,229 ,1);  border-top-color: rgba(3,155,229 ,1);  }
```

Maintenant, les côtés `left` et `top` auront une couleur _bleutée_ pour leurs bordures. Voici le résultat de cela :

![Image](https://cdn-media-1.freecodecamp.org/images/T67pvUHFrwm8ngqtjDpRQlnsTsv5F8m-tYGE)
_hmmmm. cela a l'air bien._

Nous arrivons quelque part !

Le chargeur est rond, PAS rectangulaire. Changeons cela en donnant à l'élément `.loader__anim` un `border-radius` de `50%`

Maintenant, nous avons cela :

![Image](https://cdn-media-1.freecodecamp.org/images/-ivf-cy5qBLeR63-BgXvQinQN1-hCHLnKHzm)

Pas si mal, n'est-ce pas ?

La dernière étape est de l'animer.

```
@keyframes rotate { to {  transform: rotate(1turn) }}
```

Espérons que vous avez une idée de comment fonctionnent les [animations CSS](https://www.w3schools.com/css/css3_animations.asp). `1turn` est égal à `360deg`, c'est-à-dire qu'un tour complet fait 360 degrés.

Et appliquez-le comme ceci :

```
animation: rotate 600ms infinite linear;
```

Yo ! Nous l'avons fait. Est-ce que tout cela a du sens ?

Au fait, voyez le résultat ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/pIrqjvWR4GWuXlRnDP74790SedXbHTQvtyO3)
_lo hicimos! (Espagnol)_

Assez cool, n'est-ce pas ?

Si l'une des étapes vous a confus, laissez un commentaire et je serai heureux de vous aider.

### Prêt à devenir Pro ?

J'ai créé un guide CSS gratuit pour faire décoller vos compétences CSS, immédiatement. [Obtenez l'ebook gratuit](https://pages.convertkit.com/0c2c62e04a/60e5d19f9b).

![Image](https://cdn-media-1.freecodecamp.org/images/CguQzx6sEQ6HhauYMmL8b2Ekf-AvJgqlwZ2b)
_Sept secrets CSS que vous ne connaissiez pas_