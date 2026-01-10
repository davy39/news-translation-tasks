---
title: Apprendre les variables CSS en 5 minutes - Un tutoriel pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-20T18:32:50.000Z'
originalURL: https://freecodecamp.org/news/learn-css-variables-in-5-minutes-80cf63b4025d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*03NPOHNBLqOn5r22HrvlyQ.png
tags:
- name: coding
  slug: coding
- name: CSS
  slug: css
- name: Design
  slug: design
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
seo_title: Apprendre les variables CSS en 5 minutes - Un tutoriel pour débutants
seo_desc: 'By Per Harald Borgen

  CSS Custom Properties (also known as Variables) is a big win for front-end developers.
  It brings the power of variables to CSS, which results in less repetition, better
  readability and more flexibility.

  Plus, unlike variables fro...'
---

Par Per Harald Borgen

Les propriétés personnalisées CSS (également connues sous le nom de Variables) représentent une grande avancée pour les développeurs front-end. Elles apportent la puissance des variables à CSS, ce qui réduit la répétition, améliore la lisibilité et offre plus de flexibilité.

De plus, contrairement aux variables des préprocesseurs CSS, les variables CSS font réellement partie du DOM, ce qui présente de nombreux avantages. Elles sont donc essentiellement comme des variables SASS et LESS surpuissantes. Dans cet article, je vais vous donner un cours accéléré sur le fonctionnement de cette nouvelle technologie.

J'ai également créé un [cours gratuit et interactif en 8 parties sur les variables CSS](https://scrimba.com/g/gcssvariables?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_5_minute_article), alors consultez-le si vous souhaitez devenir un expert sur ce sujet.

[Vous voulez apprendre les variables CSS ? Voici mon cours gratuit en 8 parties !](https://medium.freecodecamp.org/want-to-learn-css-variables-heres-my-free-8-part-course-f2ff452e5140)

### Pourquoi apprendre les variables CSS ?

Il y a de nombreuses raisons d'utiliser des variables en CSS. L'une des plus convaincantes est qu'elles réduisent la répétition dans votre feuille de style.

![Image](https://cdn-media-1.freecodecamp.org/images/1*03NPOHNBLqOn5r22HrvlyQ.png)

Dans l'exemple ci-dessus, il est beaucoup mieux de créer une variable pour la couleur `#ffeead` plutôt que de la répéter comme nous le faisons ici :

![Image](https://cdn-media-1.freecodecamp.org/images/1*de4-CIacmaMo9PO6PlTkyQ.png)

Non seulement cela rendra votre code plus facile à lire, mais cela vous donnera également plus de flexibilité, au cas où vous souhaiteriez changer cette couleur.

Cela a effectivement été possible avec les variables SASS et LESS depuis des années. Cependant, il y a quelques grands avantages avec les variables CSS.

1. Elles ne nécessitent aucune transpilation pour fonctionner, car elles sont natives du navigateur. Vous n'avez donc besoin d'aucune configuration pour commencer, contrairement à SASS et LESS.
2. Elles vivent dans le DOM, ce qui ouvre un grand nombre d'avantages, que je vais aborder dans cet article et dans mon prochain cours.

Maintenant, commençons à apprendre les variables CSS !

### Déclarer votre première variable CSS

Pour déclarer une variable, vous devez d'abord décider dans quel scope la variable doit vivre. Si vous voulez qu'elle soit disponible globalement, définissez-la simplement sur la pseudo-classe `:root`. Elle correspond à l'élément racine dans votre arbre de document (généralement la balise `<html>`).

Comme les variables sont héritées, cela rendra votre variable disponible dans toute votre application, car tous vos éléments DOM sont des descendants de la balise `<html>`.

```css
:root {  
  --main-color: #ff6f69;  
}

```

Comme vous pouvez le voir, vous déclarez une variable de la même manière que vous définissez n'importe quelle propriété CSS. Cependant, la variable doit commencer par deux tirets.

Pour accéder à une variable, vous devez utiliser la fonction `var()`, et passer le nom de la variable en tant que paramètre.

```css
#title {  
  color: var(--main-color);  
}

```

Et cela donnera à votre titre la couleur `#f6f69` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*gv5ZAXzaLMT2nQVvmBei5w.png)

### Déclarer une variable locale

Vous pouvez également créer des variables locales, accessibles uniquement par l'élément dans lequel elles sont déclarées et par ses enfants. Cela a du sens si vous savez qu'une variable ne sera utilisée que dans une partie spécifique (ou des parties) de votre application.

Par exemple, vous pourriez avoir une boîte d'alerte qui utilise un type spécial de couleur qui n'est pas utilisé ailleurs dans l'application. Dans ce cas, il pourrait être judicieux d'éviter de la placer dans le scope global :

```css
.alert {  
  --alert-color: #ff6f69;  
}

```

Cette variable peut maintenant être utilisée par ses enfants :

```css
.alert p {  
  color: var(--alert-color);  
  border: 1px solid var(--alert-color);  
}

```

Si vous essayiez d'utiliser la variable `alert-color` ailleurs dans votre application, par exemple dans la barre de navigation, cela ne fonctionnerait tout simplement pas. Le navigateur ignorerait simplement cette ligne de CSS.

### Une meilleure réactivité avec les variables

Un grand avantage des variables CSS est qu'elles ont accès au DOM. Ce n'est pas le cas avec LESS ou SASS, car leurs variables sont compilées en CSS régulier.

En pratique, cela signifie que vous pouvez, par exemple, changer les variables en fonction de la largeur de l'écran :

```css
:root {  
  --main-font-size: 16px;  
}

@media all and (max-width: 600px) {  
  :root {  
    --main-font-size: 12px;  
  }  
}

```

Et avec ces quatre lignes de code simples, vous avez mis à jour la taille de police principale dans toute votre application lorsqu'elle est consultée sur des petits écrans. Plutôt élégant, n'est-ce pas ?

### Comment accéder aux variables avec JavaScript

Un autre avantage de vivre dans le DOM est que vous pouvez accéder aux variables avec JavaScript, et même les mettre à jour, par exemple, en fonction des interactions de l'utilisateur. Cela est parfait si vous souhaitez donner à vos utilisateurs la possibilité de modifier votre site web (comme ajuster la taille de la police).

Continuons avec l'exemple du début de cet article. Récupérer une variable CSS en JavaScript prend trois lignes de code.

```js
var root = document.querySelector(':root');  
var rootStyles = getComputedStyle(root);  
var mainColor = rootStyles.getPropertyValue('--main-color');

console.log(mainColor);   
//--> '#ffeead'

```

Pour mettre à jour la variable CSS, appelez simplement la méthode `setProperty` sur l'élément dans lequel les variables ont été déclarées et passez le nom de la variable en tant que premier paramètre et la nouvelle valeur en tant que second.

```js
root.style.setProperty('--main-color', '#88d8b0')

```

Cette couleur principale peut changer l'apparence de toute votre application, elle est donc parfaite pour permettre aux utilisateurs de définir le thème de votre site.

![En mettant à jour une seule variable, vous pouvez changer la couleur de la barre de navigation, du texte et des éléments.](https://cdn-media-1.freecodecamp.org/images/1*ludyq87oDilcmJR98bcGwA.gif)

En mettant à jour une seule variable, vous pouvez changer la couleur de la barre de navigation, du texte et des éléments.

### Support des navigateurs

Actuellement, 77 pour cent du trafic mondial des sites web supporte les variables CSS, avec près de 90 pour cent aux États-Unis. Nous utilisons déjà les variables CSS sur [Scrimba.com](http://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_5_minute_article) depuis un certain temps, car notre audience est assez avertie en technologie et utilise principalement des navigateurs modernes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oCt-OblOjurKizk-SAITwg.png)

Ok, c'est tout. J'espère que vous avez appris quelque chose !

Si vous voulez l'apprendre correctement, assurez-vous de consulter [mon cours gratuit sur les variables CSS chez Scrimba.](https://scrimba.com/g/gcssvariables?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_5_minute_article)

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le co-fondateur de [Scrimba](https://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_5_minute_article) – la manière la plus facile d'apprendre à coder. Vous devriez consulter notre [bootcamp de design web réactif](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_5_minute_article) si vous voulez apprendre à construire des sites web modernes de manière professionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gcssvariables_5_minute_article)_