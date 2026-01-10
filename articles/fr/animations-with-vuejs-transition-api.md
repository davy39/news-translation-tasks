---
title: Comment créer des animations époustouflantes avec l'API de Transition de Vue.js
subtitle: ''
author: Felix Favour Chinemerem
co_authors: []
series: null
date: '2023-10-10T15:28:04.000Z'
originalURL: https://freecodecamp.org/news/animations-with-vuejs-transition-api
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/supercharged-animations.png
tags:
- name: animations
  slug: animations
- name: api
  slug: api
- name: Vue.js
  slug: vuejs
seo_title: Comment créer des animations époustouflantes avec l'API de Transition de
  Vue.js
seo_desc: "I’m easily gripped by animations and purposeful motion on the Web – so\
  \ much so that I wrote a whole article on it. \nI’m also a big fan of the Vue.js\
  \ framework, and I’ve been building apps with it for three years.\nSo it was a delightful\
  \ surprise when ..."
---

Je suis facilement captivé par les animations et les mouvements intentionnels sur le Web – au point d'avoir écrit un [article entier](https://favourfelix.com/stories/css-and-motion-build-animations-on-the-web/) à ce sujet. 

Je suis également un grand fan du framework Vue.js, et je construis des applications avec depuis trois ans.

Ce fut donc une agréable surprise lorsque j'ai réalisé que je pouvais utiliser **uniquement** l'API de Transition dans Vue.js tout en exploitant mes compétences décentes en CSS pour animer l'entrée et la sortie d'un composant de manière si fluide.

À quel point fluide, pourriez-vous demander ? Laissez-moi vous montrer :

%[https://vimeo.com/872452747]

Dans cet article, nous allons construire une application de films simple avec des fonctionnalités de filtrage intégrées. À la fin, vous devriez avoir une solide compréhension des composants intégrés `<Transition>` et `<TransitionGroup>` dans Vue.js et comment ils gèrent de manière transparente les animations d'entrée et de sortie dans Vue.js.

## Prérequis

Attendez ! Nous avons besoin de quelques outils dans notre boîte à outils avant de plonger dans cette aventure. Cet article est conçu pour être accessible aux débutants, mais pour garantir un parcours fluide, voici ce dont vous aurez besoin :

* Une compréhension de base du HTML, du CSS et du Javascript.
* Une [compréhension de base des Transitions et Animations en CSS](https://www.freecodecamp.org/news/css-transition-vs-css-animation-handbook/).
* Une [connaissance de base du framework Vue.js](https://www.freecodecamp.org/news/vue-3-full-course/).
* Vous pouvez également accéder à l'application de films de base sans les transitions [ici](https://github.com/felixfavour/supercharged-animations-vue), mais seulement si vous pensez que c'est la partie ennuyeuse ;)
* Enfin, mais non des moindres, une bonne musique de fond – je vous laisse choisir celle-ci vous-même, [mais il y a toujours la radio freeCodeCamp](https://coderadio.freecodecamp.org/).

Ok, maintenant nous sommes prêts à commencer.

## Qu'est-ce que l'API de Transition ?

L'API de Transition se compose principalement des composants intégrés `<Transition>` et `<TransitionGroup>` dans Vue.

Le composant `<Transition>` est utilisé pour animer des éléments ou composants uniques. En revanche, le `<TransitionGroup>` est utilisé pour animer plusieurs éléments dans une liste en conjonction avec la directive v-for dans Vue.

### Comment ajouter des animations avec le composant `<Transition>`

Le composant `<Transition>` est un composant intégré qui est généralement enveloppé autour de tout élément ou composant racine pour des avantages d'animation. Les animations sont déclenchées lorsque l'élément ou le composant interne est montré ou caché en utilisant des directives Vue courantes comme v-show ou v-if.

Ce composant est "intégré" car il n'a pas besoin d'être importé dans le template pour être fonctionnel. Il est reconnu par le compilateur de template Vue.

Nous pouvons essayer cela en ajoutant un v-show à notre conteneur `.header-filters` d'abord et en enveloppant le conteneur dans le composant `<Transition>` comme ci-dessous :

```html
<Transition>
  <div v-show="filtersVisible" class="header-filters">
    <input type="search" v-model="searchQuery" placeholder="Rechercher des Films">
    <div class="button-group">
      <button @click="query = ''" :class="{ active: query === '' }">Effacer les Filtres</button>
      <button @click="query = '2021'" :class="{ active: query === '2021' }">2021</button>
      <button @click="query = 'Action'" :class="{ active: query === 'Action' }">Action</button>
    </div>
  </div>
</Transition>

```

Nous pouvons ensuite finaliser l'animation en incluant des spécifications de style pour les animations d'entrée et de sortie. Si vous êtes familier avec les Animations et Transitions CSS, le mode de fonctionnement est assez similaire. Si ce n'est pas le cas, voici un [cours accéléré](https://favourfelix.com/stories/css-and-motion-build-animations-on-the-web/).

```css
.v-move,
.v-enter-active,
.v-leave-active {
  transition: 0.3s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
  transform: translateY(10px);
}

```

Et maintenant, vous devriez avoir vos animations fluides pour les éléments racine uniques avec le composant `<Transition>`. 

![Image](https://www.freecodecamp.org/news/content/images/2023/10/ezgif.com-video-to-gif--1-.gif)
_Illustration de l'effet du composant Transition lorsqu'un élément est caché et montré._

Et si vous voulez quelque chose de similaire à la vidéo que j'ai partagée plus tôt ? Quelque chose de plus captivant ? Eh bien, voyons le composant `<TransitionGroup>`.

### Comment ajouter des animations de liste avec le composant `<TransitionGroup>`

Le composant `<TransitionGroup>` est enveloppé autour d'une liste pour animer l'insertion, la suppression et le changement d'ordre des éléments qui sont rendus dans cette liste. Cette liste est généralement créée avec la directive v-for.

Contrairement au composant `<Transition>`, les éléments ou composants enveloppés dans le composant `<TransitionGroup>` doivent avoir des attributs de clé uniques.

```html
<TransitionGroup>
  <MovieCard v-for="movie in filteredMovies" :key="movie.title" :movie="movie" />
</TransitionGroup>
```

Outre les instructions ci-dessus, le composant `<TransitionGroup>` a un mode d'intégration et de fonctionnement similaire à celui du composant `<Transition>`.

## Comment identifier et nommer les Transitions

Un problème courant lors de l'utilisation des composants `<Transition>` et `<TransitionGroup>` est d'avoir plusieurs instances de ces composants dans votre application et d'utiliser différentes transitions d'entrée et de sortie pour des instances spécifiques. C'est pourquoi nous nommons les composants `<Transition>` et `<TransitionGroup>`.

Les composants `<Transition>` et `<TransitionGroup>` acceptent une prop `name` qui aide à identifier et à regrouper les transitions.

```html
<TransitionGroup name="list">
  <MovieCard v-for="movie in filteredMovies" :key="movie.title" :movie="movie" />
</TransitionGroup>

```

La prop `name` détermine également le nom de la classe pour le style des transitions d'entrée et de sortie comme ci-dessous :

```css
.list-move,
.list-enter-active,
.list-leave-active {
  transition: 0.3s ease;
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateY(10px);
}


```

Remarquez que la prop `name` passée dans le code `<TransitionGroup>` ci-dessus est "list", et elle est utilisée comme préfixe dans les styles pour les transitions d'entrée et de sortie dans le code CSS ci-dessus.

## Comment personnaliser les animations d'entrée et de sortie avec CSS

Dans cet article, nous avons utilisé la propriété CSS `transition` pour aider avec des animations d'entrée et de sortie subtiles. Mais les composants `<Transition>` et `<TransitionGroup>` supportent également la propriété `animation` en CSS pour des animations beaucoup plus complexes avec plusieurs images clés.

Voici un exemple de la façon dont nous pouvons utiliser la propriété `animation` dans notre composant `<Transition>` :

### Template

```html
<Transition name="bounce">
  <div v-show="filtersVisible" class="header-filters">
    <input type="search" v-model="searchQuery" placeholder="Rechercher des Films">
    . . .
  </div>
</Transition>


```

### Styles

```css
.bounce-enter-active {
  animation: bounce-in 0.5s;
}
.bounce-leave-active {
  animation: bounce-in 0.5s reverse;
}
@keyframes bounce-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.25);
  }
  100% {
    transform: scale(1);
  }
}

```

Si le concept des images clés ou de la propriété d'animation en CSS ne vous est pas très clair, n'hésitez pas à [obtenir une rapide introduction aux animations en CSS](https://favourfelix.com/stories/css-and-motion-build-animations-on-the-web/).

## Mouvement intentionnel sur le Web

Dans toute discussion sur les animations et transitions web, il est crucial d'aborder le "pourquoi" derrière elles. Pourquoi devrions-nous inclure du mouvement sur le web, et est-ce vraiment indispensable ?

Le mouvement sur le web sert un but qui va bien au-delà de la simple esthétique. C'est un outil puissant pour transmettre des messages à vos utilisateurs. Qu'il s'agisse d'élever votre narration, de fournir des retours utilisateur, ou de captiver leur attention, les animations peuvent jouer un rôle pivot dans l'amélioration de l'expérience de vos utilisateurs.

Les jours où les animations étaient ajoutées uniquement à des fins décoratives sont révolus. Dans le paysage web moderne, chaque image clé doit être conçue de manière réfléchie avec un but clair, et l'utilisateur doit toujours être au cœur de vos décisions de conception.

Cela dit, assurez-vous de ne pas trop utiliser les animations – car trop d'éléments en mouvement peuvent être distractifs et nuire à l'expérience utilisateur. Tout est une question d'équilibre.

## Conclusion

Ouf, c'était une aventure excitante ! J'espère que vous l'avez appréciée. Cet article a partagé beaucoup de choses, et je suis ravi de voir comment vous allez utiliser ces informations. J'adorerais savoir si vous avez construit quelque chose de cool en le lisant.

N'hésitez pas non plus à consulter la documentation officielle de Vue [documentation](https://vuejs.org/guide/built-ins/transition.html) pour voir ce qui est possible avec l'API de Transition.

Enfin, amusez-vous à créer des expériences délicieuses avec l'animation, mais n'oubliez jamais que les animations CSS ne sont utiles à vos utilisateurs que lorsqu'elles sont intentionnelles. Si vous avez trouvé cet article utile, n'hésitez pas à vous connecter sur [favourfelix.com](http://favourfelix.com/) pour voir ce que je fais d'autre.