---
title: Angular/Ionic, React, Vue ? Protégez votre application avec Stencil.js !
subtitle: ''
author: Lee Nathan
co_authors: []
series: null
date: '2019-05-31T20:51:20.000Z'
originalURL: https://freecodecamp.org/news/angular-ionic-react-vue-future-proof-your-app-with-stencil-js
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/bridge.jpg
tags: []
seo_title: Angular/Ionic, React, Vue ? Protégez votre application avec Stencil.js
  !
seo_desc: 'A Brief Intro:

  In this tutorial, I’m going to build a plain Stencil app with a working analog clock.
  I will throw in a little Ionic for convenience as well, but that’s not the focus
  here. This tutorial will cover some of the more important basics to ...'
---

## Une brève introduction :

Dans ce tutoriel, je vais créer une application Stencil simple avec une horloge analogique fonctionnelle. J'ajouterai également un peu d'Ionic pour plus de commodité, mais ce n'est pas le sujet principal ici. Ce tutoriel couvrira certaines des bases les plus importantes à connaître sur Stencil.

Bien que ce soit une introduction de bas niveau à Stencil, je vais supposer que vous avez au moins parcouru la documentation de Stencil et que vous avez une idée de base de ce que sont JSX et Stencil. Vous devriez probablement être familier avec TypeScript ou au moins ES6.

## Une introduction plus longue :

Dans un précédent article, j'ai dit que je "migrerais" vers React parce qu'il a dépassé Ionic. C'est une proposition intimidante après 3 ans dans le monde Ionic. Et si React est dépassé dans une autre année ? Heureusement, les gens chez Ionic sont parfaitement conscients de cette réalité. C'est pourquoi ils ont construit stencil.js.

Stencil utilise TypeScript et JSX comme un framework super puissant, léger et non-framework. Stencil peut être ajouté à n'importe quel autre framework ou utilisé seul pour accomplir beaucoup de ce que quelqu'un utiliserait Angular ou React.

C'est aussi rapide et facile à apprendre par rapport aux frameworks plus grands. Donc c'est un excellent moyen de se familiariser avec la façon de penser JSX/Web Component. Et si vous voulez migrer de React vers Angular, ou vice versa, Stencil peut faciliter votre chemin.

À l'avenir, j'utiliserai Stencil dans mes projets personnels. Et les composants Ionic 4 sont maintenant construits sur Stencil. Donc c'est un choix logique pour protéger vos applications contre l'avenir, que vous restiez avec Ionic/Angular ou que vous passiez à un autre framework.

En tant que note pour les débutants en JSX. Je trouve qu'il est plus facile d'oublier de tout faire en composants parfaits et de simplement écrire du HTML. Ensuite, lorsque je vois un peu de HTML que je vais utiliser plus d'une fois ou que je veux faire quelque chose de spécial, je le déplacerai dans son propre composant.

## Installation :

Tout d'abord :

npm init stencil

Sélectionnez `component` et utilisez `analog-clock-components` comme nom de votre projet, puis :

cd analog-clock-components npm install --save @ionic/core npm start

Si tout s'est bien passé, vous devriez voir la page "Home" par défaut s'afficher.

## Création de l'horloge :

Je déteste quand les tutoriels vous alourdissent avec un tas d'informations qui ne sont pas critiques pour les concepts de base. Donc c'est exactement ce que je vais faire ! Je vais créer l'horloge avec SVG. Mais hey, c'est mieux qu'un autre exemple de liste de tâches. Et je promets de garder ça simple.

**Attention !** Les balises de vos composants Stencil DOIVENT avoir 2 mots ou plus, sinon votre application échouera de manière énigmatique avec quelque chose comme "clock" n'est pas un nom d'élément personnalisé valide !

Ajoutez un dossier clock-face dans le répertoire `src/components` comme suit : `clock-face/clock-face.tsx` et ajoutez le contenu suivant.

import { Component } from '@stencil/core';

@Component({ tag: 'clock-face' }) export class ClockFace {

render() { return ( ); } }

Ensuite, ajoutez `analog-clock/analog-clock.tsx`.

import { Component } from '@stencil/core';

@Component({ tag: 'analog-clock', }) export class AnalogClock { render() { return \[

\]; } }

Et maintenant, remplacez la balise `my-component` dans `index.html` par `<analog-clock\>`

Vous devrez peut-être redémarrer l'application, mais vous devriez maintenant voir ceci comme votre page d'accueil :

![Image](https://www.freecodecamp.org/news/content/images/2019/05/clock-1.png align="left")

*mon horloge époustouflante*

Ce morceau de SVG était assez indolore, juste un cercle et quelques lignes avec un peu de style pour l'esthétique. Le style peut et doit être appliqué avec CSS dans une application non triviale.

Remarquez que j'ai utilisé la balise `<svg>` comme racine de ce composant. Génial ! Jusqu'à présent, cette horloge n'a raison que deux fois par jour, alors ajoutons quelques props pour la rendre ajustable. Je vais également ajouter des fonctions pour convertir l'heure en degrés afin de faire tourner les aiguilles. Et je vais mettre à jour le SVG pour pouvoir faire tourner ces aiguilles.

import { Component, Prop } from '@stencil/core';

@Component({ tag: 'clock-face' }) export class ClockFace { @Prop() hour: number; @Prop() minute: number; @Prop() second: number;

hourToDegrees(): number { return Math.floor(this.minute / 2) + (this.hour \* 30); }

minuteToDegrees(): number { return Math.floor(this.second / 10) + (this.minute \* 6); }

secondToDegrees(): number { return this.second \* 6; }

render() {

return ( &lt;line id="hour-hand" transform={`rotate(${this.hourToDegrees()}, 100, 100)`} x1="100" y1="100" x2="100" y2="60" stroke="black" stroke-width="10" stroke-linecap="round"/&gt; &lt;line id="minute-hand" transform={`rotate(${this.minuteToDegrees()}, 100, 100)`} x1="100" y1="100" x2="100" y2="30" stroke="black" stroke-width="8" stroke-linecap="round"/&gt; &lt;line id="second-hand" transform={`rotate(${this.secondToDegrees()}, 100, 100)`} x1="100" y1="100" x2="100" y2="30" stroke="black" stroke-width="2" stroke-linecap="round"/&gt; ); } }

Et voilà. Mon composant peut maintenant accepter des variables entrantes via le décorateur @Prop() et changer la façon dont il est affiché en fonction de ces variables. Voyons cela en action en mettant à jour la balise clock-face en `<clock-face hour={12} minute={34} second={56}/>` J'ai enveloppé les nombres dans des accolades pour qu'ils soient passés en tant que nombres au lieu de chaînes de caractères.

![Image](https://www.freecodecamp.org/news/content/images/2019/05/clock-2.png align="left")

*mon horloge mise à jour ; toujours juste deux fois par jour*

## Faire fonctionner l'horloge :

Si vous remarquez, l'horloge n'a aucune logique interne ni capacité de gestion du temps. Il est préférable de garder vos composants aussi simples que possible. Les Web Components sont un peu comme la programmation fonctionnelle en ce sens qu'ils doivent faire une seule chose. Stencil s'appuie sur le paradigme fonctionnel en rendant les props immuables afin que le composant ne puisse pas affecter quoi que ce soit en dehors de lui-même. Ils peuvent déclencher des événements, mais c'est tout.

Maintenant, je vais ajouter des getters à `analog-clock.ts` pour qu'il commence à fonctionner.

import { Component } from '@stencil/core';

@Component({ tag: 'analog-clock', }) export class AnalogClock { get hour(): number { let h: any = new Date().getHours(); return h; }

get minute(): number { let m: any = new Date().getMinutes(); return m; }

get second(): number { let s: any = new Date().getSeconds(); return s; }

render() { return (

); } }

Wow ! Regardez cette horloge aller... nulle part. L'heure est correcte, mais elle ne fonctionne pas. Si ceux d'entre vous qui suivez ce tutoriel à la maison sont familiers avec la famille Angular, vous pourriez vous attendre à une horloge qui fonctionne à ce stade. Cependant, Stencil ne ré-affiche que dans certaines conditions. Cela évite l'effet de train fou que les développeurs Angular connaissent trop bien. Si vous obtenez une boucle dans votre code ou si vous avez beaucoup de logique dans une méthode qui est appelée depuis HTML ou un getter, votre application peut ralentir jusqu'à s'arrêter complètement. Il est encore possible que cela arrive avec Stencil, mais cela devrait presque être délibéré.

Pour que Stencil ré-affiche, vous devez utiliser des décorateurs comme @Prop() ou @State() pour indiquer à Stencil quelles données sont suffisamment importantes pour provoquer le ré-affichage de la vue. Le décorateur d'état est utilisé pour gérer les variables internes, donc je vais l'utiliser. Je vais également utiliser le cycle de vie du composant pour que le minuteur ne commence pas avant que le composant ne se charge et pour qu'il s'arrête lorsque le composant se décharge.

import { Component, State } from '@stencil/core';

@Component({ tag: 'analog-clock', }) export class AnalogClock { timer: number;

@State() time: number = Date.now();

componentDidLoad() { this.timer = window.setInterval(() =&gt; { this.time = Date.now(); }, 250); }

componentDidUnload() { clearInterval(this.timer); }

get hour(): number { return new Date(this.time).getHours(); }

get minute(): number { return new Date(this.time).getMinutes(); }

get second(): number { return new Date(this.time).getSeconds(); }

render() { return ( ); } }

![Image](https://www.freecodecamp.org/news/content/images/2019/05/clock-3.gif align="left")

*Et maintenant, mon horloge fonctionne joyeusement.*

## Changer le fuseau horaire (en quelque sorte) :

Ensuite, je vais ajouter un curseur pour me permettre de choisir un fuseau horaire. Je ne vais pas réellement incorporer les fuseaux horaires. C'est une fonctionnalité complexe qui nécessite une autre bibliothèque ([comme moment.js pour les fuseaux horaires](https://momentjs.com/timezone/)) pour être gérée correctement. Je vais simplement décaler l'heure de plus ou moins 12 heures. C'est une solution un peu bricolée, mais elle illustrera comment obtenir des données d'un composant, ce qui est une chose critique à savoir.

Maintenant, je vais ajouter un composant time-zone-slider comme je l'ai fait avec l'horloge analogique, comme ceci `time-zone-slider/time-zone-slider.tsx`.

import { Component, Prop, Event, EventEmitter } from '@stencil/core'; import '@ionic/core';

@Component({ tag: 'time-zone-slider' }) export class TimeZoneSlider { @Prop() offset: number; @Event() timeZoneChanged: EventEmitter;

positionChanged(event: CustomEvent) { this.timeZoneChanged.emit(event.detail.value) }

render() { return ( &lt;ion-range debounce={500} max={12} min={-12} pin={true} snaps={true} step={1} value={this.offset} onIonChange={event =&gt; this.positionChanged(event)} &gt; -1212 ); } }

Remarquez que j'ai importé la bibliothèque `@ionic/core` ici. Cela peut être excessif, surtout dans une application où vous n'avez pas l'intention d'utiliser des composants Ionic. J'ai simplement trouvé que c'était le moyen le plus facile d'implémenter un curseur pour que je puisse terminer ce tutoriel avant la fin de l'année.

Ce composant n'a également aucune logique interne. Il ne gère même pas son propre état. Il reçoit le décalage en tant que @Prop(). Et lorsque le curseur bouge, il émet un @Event() vers le parent, lui faisant savoir la nouvelle valeur. C'est ensuite la responsabilité du parent de gérer l'état et de mettre à jour l'enfant lorsque le décalage change. Ou le parent peut également transmettre une valeur gérée par l'état de l'un de **ses** ancêtres.

import { Component, State, Listen } from '@stencil/core';

@Component({ tag: 'analog-clock', }) export class AnalogClock { timer: number;

@State() time: number = Date.now(); @State() timeZone: number = 0; @Listen('timeZoneChanged') timeZoneChangedHandler(event: CustomEvent) { this.timeZone = event.detail; }

componentDidLoad() { this.timer = window.setInterval(() =&gt; { this.time = Date.now(); }, 250); }

componentDidUnload() { clearInterval(this.timer); }

get hour(): number { return new Date(this.time).getHours(); }

get minute(): number { return new Date(this.time).getMinutes(); }

get second(): number { return new Date(this.time).getSeconds(); }

render() { return (

&lt;clock-face hour={this.hour + this.timeZone} minute={this.minute} second={this.second}/&gt;

  
); } }

Dans analog-clock, j'ai simplement ajouté un gestionnaire d'état timeZone. J'ai également ajouté le décorateur @Listen() à la fonction `timeZoneChangedHandler`. Cette fonction met à jour l'état timeZone. J'ai changé l'élément `clock-face` pour décaler l'heure en fonction du timeZone. Enfin, j'ai ajouté l'élément curseur et j'ai transmis le timeZone actuel, complétant ainsi la boucle.

#### Résumé :

J'ai à peine effleuré environ 80 % de ce que vous devez savoir pour commencer à utiliser Stencil. Nous avons couvert la création et l'implémentation de composants et la gestion de leurs cycles de vie. Nous avons couvert le déclenchement et l'écoute d'événements. Nous avons couvert le passage de données aux composants enfants avec Props. Et nous avons couvert la gestion de l'état interne des composants. Cela représente en fait environ la moitié des fonctionnalités répertoriées dans la section Composants de la documentation de Stencil.