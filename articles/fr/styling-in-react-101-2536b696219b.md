---
title: Comment rendre vos applications jolies avec le style dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-26T19:02:03.000Z'
originalURL: https://freecodecamp.org/news/styling-in-react-101-2536b696219b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*INQOqFg9aha-aEJbqhXQUw.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: UI
  slug: ui
seo_title: Comment rendre vos applications jolies avec le style dans React
seo_desc: 'By Vinh Le

  When it comes to styling in React, there are just so many ways and choices of technologies
  to beautify your web app. Nonetheless, based on my personal experience, it really
  depends on the UI requirements of your app to decide which to go w...'
---

Par Vinh Le

En matière de style dans React, il existe de nombreuses façons et technologies pour embellir votre application web. Néanmoins, selon mon expérience personnelle, cela dépend vraiment des exigences de l'interface utilisateur de votre application pour décider laquelle choisir.

### Est-ce trop facile ?

Si vous vous arrêtez ici et dites : « C'est facile ! Il suffit de chercher sur Google les meilleures bibliothèques d'interface utilisateur React, d'en choisir une et vous êtes prêt », alors vous n'avez peut-être pas vécu les expériences douloureuses de configuration des composants pré-stylisés dans ces bibliothèques.

Plus vous travaillez sur quelque chose, plus vous êtes familier et moins vous avez besoin de temps pour résoudre les problèmes. Le style dans React n'est pas une exception. Cependant, cela nécessite vraiment une quantité décente de temps, au moins pour moi en tant que développeur autodidacte, pour pouvoir faire un choix judicieux.

Par conséquent, mes principaux objectifs dans cet article sont de vous présenter rapidement les meilleures alternatives de style React et, plus important encore, d'essayer de vous expliquer plus en détail quand utiliser laquelle.

### Pourquoi le style ?

![Image](https://cdn-media-1.freecodecamp.org/images/p247brEV3QCLUH97LtMsI0w7YhhekP5ZyfTd)
_Esthétique ? Fonctionnalités ? Ou les deux ?_

Une autre question extrêmement simple, n'est-ce pas ? Eh bien, si je modifie un peu cette question : « Pourquoi apprendre le style dès que vous commencez à apprendre React ? », cela pourrait peut-être activer votre flux de pensée.

Si vous êtes nouveau dans l'écosystème React, vos premiers tutoriels vous apprennent probablement comment démarrer un projet, vous montrent comment gérer les états et manipuler les props. Le style est à peine mentionné dans les premières sections des cours en ligne et donc minimalement utilisé dans vos toutes premières applications.

Avant que je ne paraisse trop sérieux à vos yeux, laissez-moi vous dire que « c'est entièrement correct ». Il n'y a absolument rien de mal à ce que vous faites. D'un autre côté, c'est encore mieux si vous mettez le style de côté au début pour vous concentrer davantage sur la logique et les fonctionnalités de l'application.

Cependant, si vous vous souciez de l'esthétique de votre travail dès le début, alors vous n'êtes probablement pas totalement satisfait de votre application fonctionnelle mais minimalement stylée.

D'accord, assez de mots. Laissez-moi résumer les avantages de styliser votre application, que ce soit dès votre premier « Hello world » ou un projet sur lequel vous travaillez actuellement :

* **Interface utilisateur belle dès le départ** — rappelez-vous pourquoi React existe ? Pour nous aider à créer une interface utilisateur dynamique. Une interface utilisateur plus polie contribue à une meilleure expérience utilisateur. Par conséquent, si nous nous mettons à la place des utilisateurs, nous réalisons simplement que le design attrayant est une partie impérative d'une application conviviale.
* **Bon environnement de développement** — surtout lorsque vous travaillez sur votre projet personnel. Si un bon design vous donne envie de l'utiliser, vous aurez peut-être plus d'inspiration pour développer une application avec une approche de conception d'abord. Encore une fois, cela vient des côtés esthétiques des choses. Si vous êtes celui qui veut simplement que cela fonctionne, cela pourrait ne pas être applicable pour vous.
* **Évitez l'accablement du style plus tard** — imaginez lorsque vous avez travaillé sur un projet pendant un certain temps et que vous regardez soudainement en arrière pour penser à la quantité de style que vous allez devoir faire. Si ce n'est qu'un projet de bac à sable, alors c'est peut-être correct. Mais si votre application nécessite plusieurs couches de conteneurs et d'éléments, et que la réactivité est une nécessité, alors ce serait une quantité de travail assez importante à venir.

**Alors, que devrais-je utiliser pour rendre mon application React belle ?**

![Image](https://cdn-media-1.freecodecamp.org/images/S28rjd2vX8bKPhxNO1m1JpYO9QvorQtJ-3lK)
_Vous avez déjà une idée, considérons maintenant les alternatives_

### Style en ligne

Cette approche est la plus facile à démarrer car elle ne nécessite aucune configuration et vous pouvez voir instantanément le résultat. Cependant, même si vous êtes familier avec CSS, méfiez-vous des fautes de frappe car elles pourraient vous causer des maux de tête :

```
<div style={{ width: 50, height: 50, background: '#000'}}>    Je suis une boîte carrée avec un fond noir</div>
```

#### **Points clés**

* Le style en ligne est fait par la **propriété style** dans n'importe quel élément DOM, il a un **type objet**, dans lequel **clé** est une propriété CSS normale, et **valeur** est la valeur CSS équivalente.
* Comme il n'y a pas de tiret comme dans de nombreuses propriétés CSS, vous devez faire attention à la capitalisation comme : `backgroundColor`, `backgroundImage`, `textAlign`, et `flexDirection`.
* C'est plus bien organisé lorsque vous définissez une variable distinctive stockant toute la logique de style :

```
const styles = {  alertMessage: { color: 'red' },  ... // autre règle de style};
```

```
<span style={styles.alertMessage}>Erreur inconnue</span>
```

* Vous pouvez faire du style conditionnel. Par exemple :

```
<span    style={{ color: this.state.isWarning ? 'red' : 'black'  }}>   Voyons si je suis un avertissement </span>. </span>
```

#### Avantages

* Facile à appliquer, aucune configuration.

#### Inconvénients

* Vos fichiers JavaScript deviendront plus désordonnés et plus longs lorsque votre projet deviendra plus complexe. Une façon de le faire est de définir des variables de style dans un fichier JavaScript externe et de les importer. Cependant, cela nécessite une étape supplémentaire et devient plus difficile à utiliser par rapport aux méthodes de style suivantes.
* Vitesse de développement plus lente causée par le rechargement de l'application. Si vous utilisez des outils comme create-react-app, votre application se rechargera à chaud chaque fois que vous apporterez des modifications. Sinon, vous devez recharger manuellement votre page pour voir les modifications. Par conséquent, selon la complexité de votre application, il faudra de plus en plus de temps pour le re-rendu.

#### Quand utiliser ?

Lorsque vous commencez à apprendre React, ce serait le moment le plus approprié pour adopter cette approche. De plus, si votre projet est petit ou si vous souhaitez simplement appliquer un style mineur à votre application. La réactivité, par exemple, n'est pas vraiment critique. Alors le style en ligne est bon à utiliser.

### CSS

D'accord, plus de CSS bizarre dans JS. Voici le CSS original que vous avez aimé :), seulement une simple configuration avant de commencer :

* Créez votre fichier CSS et importez-le dans un fichier JavaScript :

```
import './App.css';
```

* Ajoutez className à l'élément auquel vous souhaitez appliquer un style :

```
<p className='warning-message'>Avertissement</p>
```

Remarquez que c'est maintenant **className**, pas **class** normal — juste une chose typique de React.

* Suivi par vos règles de style :

```
App.css.warning-message { color: red;}
```

* Style conditionnel en définissant un nom de classe équivalent :

```
<p   className={this.state.warning ? 'warning-message' : 'normal-message'}>Avertissement</p>
```

#### Avantages

* Écrivez des règles CSS avec lesquelles vous êtes familier, moins de risque de faire des fautes de frappe.
* Bénéficiez des fonctionnalités CSS telles que les variables et les requêtes média.
* Structure de projet bien organisée.
* **Vitesse de développement plus élevée** — c'est peut-être l'avantage le plus agréable que j'ai expérimenté en développement. Lorsque vous apportez des modifications à vos fichiers CSS, votre application ne sera pas re-rendue. Par conséquent, il faudra une seconde pour que vos mises à jour s'affichent à l'écran. Plus votre application est grande et complexe, plus vous serez heureux de sauver ce temps de rechargement inutile.

#### Inconvénients

* Fonctionnalités manquantes par rapport à SCSS, que je vais explorer juste après cela.

#### Quand utiliser ?

Vous pouvez utiliser CSS dès le début, quelle que soit la taille de votre application. Comme il est presque sans configuration et que CSS est probablement familier à beaucoup, il est facile de commencer rapidement.

Si votre application devient plus grande et a un système de design encore plus complexe, envisagez de vérifier les avantages de SCSS par rapport à CSS.

Néanmoins, gardez à l'esprit que vous serez parfaitement bien avec du CSS pur. SCSS n'est pas vraiment un changement de jeu qui vous offre tous les avantages que vous n'obtiendriez pas avec CSS. Récemmment, de nouvelles fonctionnalités comme les variables arrivent pour minimiser l'écart entre CSS et ses préprocesseurs. De plus, si vous n'avez pas utilisé SCSS auparavant, cela prendra un certain temps pour vous familiariser avec.

### SCSS

C'est peut-être mon choix de prédilection pour le style React. Il reprend toute la familiarité et les avantages de CSS plus un certain nombre de fonctionnalités très utiles pour en faire un excellent package. Si vous n'êtes pas familier avec SCSS, ils ont une [documentation](https://sass-lang.com/guide) géniale pour vous.

Pour utiliser SCSS dans votre application React, cela nécessite quelques configurations. Si vous utilisez create-react-app, ce [guide](https://medium.com/@oreofeolurin/configuring-scss-with-react-create-react-app-1f563f862724) pourrait vous être utile.

Ensuite, laissez-moi vous montrer les avantages de SCSS qui en font un choix supérieur par rapport au CSS normal.

#### Nesting

Lorsque votre projet devient plus grand, il est très probable que vos fichiers CSS soient remplis de noms de classes. Les choses deviennent encore plus intimidantes lorsque votre design se compose de blocs, de conteneurs et d'éléments imbriqués. Trouver un nom de classe particulier quelque part dans un fichier de centaines de lignes est donc fatigant et chronophage. C'est là que le nesting devient pratique :

```
App.scss.intro-container {  h1 { font-size: 20px };  .nested-child {    display: block;    p {      margin: 0;    }  }}
```

Avec cette structure, par exemple, vous souhaitez changer le style d'un élément enfant à l'intérieur de votre conteneur d'introduction. Tout ce que vous avez à faire maintenant est de trouver son nom de classe, qui est `intro-container` dans ce cas. Ensuite, tous les styles de ses enfants pourraient être trouvés à l'intérieur. Beaucoup plus facile, n'est-ce pas ?

#### Mixins

L'un des plus grands avantages que les mixins apportent est de définir des points d'arrêt dans les requêtes média. Jetons un coup d'œil à cet exemple :

```
_mixins.scss
```

```
// définir le point d'arrêt pour les appareils mobiles  @mixin bp-mobile {    @media only screen and (min-device-width: 320px) and (max-device-width: 480px) {      @content;    }  }
```

De retour dans le fichier SCSS principal :

```
App.scss
```

```
body {  width: 60%; margin: 0 auto;  @include bp-mobile {    width: 90%;  }}
```

Comparé à :

```
App.css
```

```
// définir la largeur du body à 90% uniquement sur les appareils mobilesbody {  width: 60%; margin: 0 auto;}...@media only screen and (min-device-width: 320px) and (max-device-width: 480px) {  body {    @include bp-mobile {      width: 90%;    }  }}
```

Je crois que c'est beaucoup plus naturel et plus facile en SCSS. Car lorsque vous appliquez des règles de style pour un élément, vous avez une vue claire de son apparence dans d'autres viewports. Par conséquent, les modifications et ajustements sont faits directement sans le fardeau de faire défiler vers le haut dans CSS comme les gens définissent normalement les requêtes média à la fin du fichier CSS.

#### Héritage

Cela est extrêmement utile pour rendre votre code [DRY](https://en.wikipedia.org/wiki/Don't_repeat_yourself). Supposons que vous souhaitiez appliquer un arrière-plan et une bordure similaires pour 2 boutons, sauf que l'un d'eux a une couleur de texte rouge et l'autre a une couleur bleue :

```
// définir les règles communes%button-common {  background: #fff;  border: 1px solid gray;  border-radius: 3px;}
```

```
.button-red {  @extend %button-common; color: 'red' ;}
```

```
.button-blue {  @extend %button-common; color: 'blue' ;}
```

Faisons un résumé des avantages et inconvénients de SCSS :

#### Avantages

* Basiquement tous les avantages de CSS plus des fonctionnalités distinctives qui font aimer SCSS.

#### Inconvénients

* Nécessite une configuration pour être utilisé.
* Prend un certain temps à apprendre pour ceux qui ne sont pas familiers avec SCSS.

### Bibliothèques d'interface utilisateur React

Grâce à l'essor de la communauté open-source, il existe des bibliothèques d'interface utilisateur React géniales que vous pouvez utiliser dans vos projets. D'excellentes ressources sont [MaterialUI](https://github.com/mui-org/material-ui), [React-Bootstrap](https://github.com/react-bootstrap/react-bootstrap)... pour n'en nommer que quelques-unes.

Prenons MaterialUI, l'une des bibliothèques les plus populaires, comme démonstration :

#### Installation

```
npm install @material-ui/core
```

Pour utiliser cela, vous devez vous fier fortement à sa documentation, qui est bien rédigée et conçue dans, eh bien, la manière Google material. Cependant, si vous regardez un exemple de code pour ses composants, c'est un peu intimidant. Ma méthode est de simplement importer le composant que vous souhaitez utiliser, de remarquer quelques props importants, et de le personnaliser plus tard.

Supposons que nous voulons créer un bouton :

```
App.js
```

```
import { Button } from '@material-ui/core';
```

```
<Button  color='primary'  onClick={() => console.log('clicked')}  fullWidth> View </Button>
```

Boom ! Un bouton avec l'étiquette « View », de couleur bleue, ayant une valeur de largeur égale à celle de son conteneur parent, apparaît joliment à l'écran.

Tout comme cela, vous pouvez utiliser presque tous les composants de la bibliothèque. L'avantage de l'utiliser est un design material apparemment poli et moderne. Si vous souhaitez créer un composant par vous-même, cela prendra peut-être une bonne quantité de travail et votre résultat final pourrait ne pas même avoir l'air aussi bien que les composants pré-stylisés.

#### Alors pourquoi ne l'utilisons-nous pas tous ?

Tout d'abord, si le faire apparaître à l'écran semble être super facile, le personnaliser et le faire parfaitement s'intégrer dans votre système de design est absolument pas une tâche facile.

Une façon de personnaliser ces composants est de remplacer leur style, la plupart du temps via la prop style. Une autre façon est de leur donner un nom de classe, et d'écrire leur propre style en CSS. Dans ce cas, si votre CSS est totalement valide mais que votre composant ne change pas du tout, n'oubliez pas de mettre `!important` après vos règles.

#### Alors, quand utiliseriez-vous les bibliothèques d'interface utilisateur React ?

Si vous travaillez sur un projet personnel qui est petit, des bibliothèques comme MaterialUI sont agréables à utiliser. Comme vous n'aurez qu'à vous concentrer sur le côté JavaScript des choses et aurez toujours une application assez belle.

Cependant, lorsque vous prévoyez de créer une application complexe avec des couches imbriquées d'interface utilisateur, notez que parfois il pourrait être même plus rapide de créer vos propres composants réutilisables que d'essayer de personnaliser ceux pré-stylisés. Dans mon expérience personnelle, si vous avez vraiment besoin de composants particuliers où ils sont si difficiles à styliser ou à faire se comporter comme vous le souhaitez, alors vous les utilisez. Sinon, il est préférable de créer les vôtres et de tirer pleinement parti de votre contrôle sur eux.

Alors, les voici, les façons populaires de styliser dans React. Bien sûr, il existe encore de nombreuses autres bibliothèques et astuces géniales. Veuillez partager les vôtres ci-dessous dans la section des commentaires. Alors que la communauté React grandit de plus en plus, nous pouvons nous attendre à un nombre encore croissant de « stars montantes ».

De plus, les excellents mainteneurs et développeurs des bibliothèques open-source actuelles ne feront qu'essayer de rendre leurs solutions meilleures, plus polies et plus faciles à utiliser. Tout cela signifie un avenir radieux à venir :)

#### Merci d'avoir lu !

#### Dites bonjour sur les réseaux sociaux : [Facebook](https://www.facebook.com/VinhLee95), [Twitter](https://mobile.twitter.com/vinhle95), [LinkedIn](https://www.linkedin.com/in/vinhlee95/), ou mon [site personnel](http://vinhlee.com/).

#### Restez à l'écoute pour les prochains blogs technologiques 💡 ✨ 🚀

#### À bientôt !