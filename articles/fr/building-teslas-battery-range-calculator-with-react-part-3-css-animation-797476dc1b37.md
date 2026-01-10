---
title: 'Construire le calculateur d''autonomie de batterie de Tesla avec React (Partie
  3 : Animation CSS)'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-12T15:38:36.000Z'
originalURL: https://freecodecamp.org/news/building-teslas-battery-range-calculator-with-react-part-3-css-animation-797476dc1b37
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8hlNoLDBy5XWZct5tAtPoA.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: 'Construire le calculateur d''autonomie de batterie de Tesla avec React
  (Partie 3 : Animation CSS)'
seo_desc: 'By Matthew Choi

  This is the third part of Building Tesla’s Battery Range Calculator with React series.

  In part 1, we’ve created the application with only the React core, and in part 2
  we’ve transformed the application by introducing Redux, a state ma...'
---

Par Matthew Choi

Il s'agit de la troisième partie de la série Construire le calculateur d'autonomie de batterie de Tesla avec React.

Dans la partie 1, nous avons créé l'application avec uniquement le cœur de React, et dans la partie 2, nous avons transformé l'application en introduisant Redux, une solution de gestion d'état.

La partie 1, qui se concentre sur React, [est ici](https://medium.freecodecamp.com/building-teslas-battery-range-calculator-with-react-part-1-2cb7abd8c1ee) :

[**Construire le calculateur d'autonomie de batterie de Tesla avec React (Partie 1)**](https://medium.freecodecamp.com/building-teslas-battery-range-calculator-with-react-part-1-2cb7abd8c1ee)
[_Dans cette série d'articles, je vais vous guider à travers le processus de construction du calculateur d'autonomie de batterie de Tesla avec React..._medium.freecodecamp.com](https://medium.freecodecamp.com/building-teslas-battery-range-calculator-with-react-part-1-2cb7abd8c1ee)

La partie 2, qui se concentre sur Redux, [est ici](https://medium.freecodecamp.com/building-teslas-battery-range-calculator-with-react-part-2-redux-version-2ffe29018eec) :

[**Construire le calculateur d'autonomie de batterie de Tesla avec React (Partie 2 : version Redux)**](https://medium.freecodecamp.com/building-teslas-battery-range-calculator-with-react-part-2-redux-version-2ffe29018eec)
[_Ce tutoriel est la deuxième partie de la construction du calculateur d'autonomie de batterie de Tesla avec React._medium.freecodecamp.com](https://medium.freecodecamp.com/building-teslas-battery-range-calculator-with-react-part-2-redux-version-2ffe29018eec)

Si vous regardez l'application que nous avons construite jusqu'à présent, elle est un peu simple et ennuyeuse. Elle aurait l'air plus cool si nous pouvions lui donner un effet dynamique de showroom de voitures.

Lorsque l'application est chargée, ce serait bien si nos magnifiques images de voitures Tesla étaient en mouvement. Avec un peu d'effet Transformers. L'en-tête Tesla est également affiché avec un effet de fondu, et le reste des composants devrait avoir l'air un peu plus joli.

Même lorsque l'événement utilisateur se produit après le chargement, il serait plus impactant de montrer un effet visuel notable au lieu de simplement changer la valeur numérique.

Comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*eosqc6eBuYjLsLsQ.)

Vous pouvez consulter la [démo en direct](http://animation-tesla-calculator.surge.sh/).

Et voici le [code source complet](https://github.com/gyver98/part3-animation-tesla-battery-range-calculator-tutorial).

Dans la **partie 3**, nous allons examiner étape par étape le processus de rendre nos applications finies plus stylées en utilisant l'**animation CSS**.

### 1. Échauffement

Commençons par l'échauffement avant de commencer.

### 1–1. Exemple de base d'animation CSS

L'animation CSS permet à un élément de changer progressivement d'un style à un autre.

L'animation CSS se compose de deux composants :

* Un style décrivant l'animation CSS
* Un ensemble de keyframes qui indiquent les états de début et de fin du style de l'animation

Voici un exemple simple. Dans cet exemple, la couleur de fond d'un élément est progressivement changée du rouge au jaune sur 5 secondes.

Pour créer une animation CSS, vous avez besoin de deux étapes :

![Image](https://cdn-media-1.freecodecamp.org/images/0*CbLQQOKYyRDohXwk.)

> Consultez [Utiliser les animations CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations/Using_CSS_animations) pour plus de détails

### 1–2. Un autre exemple d'animation CSS

Voici ce avec quoi nous commençons. Il y a un en-tête Tesla, un titre et une belle image de voiture Tesla.

### 1–3 Faire rebondir

Voici trois éléments bien placés. Voyons ces trois éléments apparaître lentement sur un écran blanc, comme un ou deux acteurs dansant sur une scène avec rien sur le fond blanc.

Tout d'abord, définissez la séquence d'animation en utilisant des keyframes. Ensuite, appliquez la classe animate-pop-in avec la propriété d'animation définie aux éléments div et h1.

![Image](https://cdn-media-1.freecodecamp.org/images/0*JFGV83BhzDdZApUn.)

Maintenant, vous pouvez voir que les trois éléments apparaissent lentement en augmentant de taille sur 6 secondes.

### 1–4 Courbe de Bézier cubique

Dans notre exemple, nous avons utilisé ease-out avec une fonction animation-timing-function. Les fonctions d'easing spécifient le taux de changement d'un paramètre au fil du temps. Il y a quatre fonctions de timing prédéfinies que nous pouvons utiliser, elles sont ease, ease-in, ease-out, ease-in-out et linear.

* **ease** — accélère un peu au milieu, puis ralentit vers la fin
* **ease-in** — commence lentement, puis accélère jusqu'à la fin
* **ease-out** — commence rapidement, puis ralentit jusqu'à la fin
* **ease-in-out** — commence lentement, accélère jusqu'au milieu, puis ralentit jusqu'à la fin
* **linear** — vitesse d'animation constante tout au long

Il est important de noter qu'elles sont essentiellement basées sur la **courbe de Bézier**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*5T1qzxZKI8BCti9n.)

### 1–5 Créer une vitesse personnalisée

Comme dans notre vie réelle, tous les objets ne se déplacent pas à une vitesse constante, donner ces vitesses variables aux éléments à l'écran donnera un mouvement plus réaliste. En utilisant la fonction **Cubic-bezier**, nous sommes capables de créer une vitesse personnalisée.

Cependant, définir la vitesse d'animation au format de la fonction cubic-bezier n'est pas intuitif.

Voici un outil fantastique pour visualiser le fonctionnement de cubic-bezier.

![Image](https://cdn-media-1.freecodecamp.org/images/0*GA_uq9VnfsYodUVL.)

Voici un exemple d'application de la vitesse personnalisée au lieu de ease-out.

Maintenant que l'échauffement est terminé, commençons.

### 2. Exercice

Comme nous l'avons vu dans la démo, nous allons appliquer l'animation à deux points dans notre application :

* lorsqu'une application est chargée
* lorsqu'une action de l'utilisateur se produit

### 2.1 Lorsqu'une application est chargée

Regardons la disposition complète de notre application. La structure des composants de l'application que nous avons créée dans la partie 1 et la partie 2 ne change pas du tout. Il suffit de définir l'attribut d'animation et @keyframes dans le fichier CSS correspondant. Le fichier CSS à modifier est marqué en vert.

![Image](https://cdn-media-1.freecodecamp.org/images/0*uZ5xPaH4Dx681Pjs.)

### 2.1.1 Présentation d'Animista

Ne serait-il pas bien d'avoir un outil qui nous permet de voir quels effets d'animation sont possibles avant de les appliquer ? Et comment les effets apparaîtraient une fois que vous les auriez appliqués ? Comment vous pourriez combiner plusieurs propriétés d'animation en un seul endroit ? Il existe précisément un outil pour cela : [Animista](http://animista.net/).

Avec cet outil, nous pouvons toucher et tester les effets animés à volonté. Une fois que vous avez trouvé l'animation que vous aimez, cliquez sur le bouton Générer le code pour copier la valeur de la propriété d'animation et l'appliquer au CSS correspondant dans notre application.

N'oubliez pas de cliquer sur le bouton Ajouter aux Favoris et de récupérer le code des keyframes depuis la page de téléchargement.

![Image](https://cdn-media-1.freecodecamp.org/images/0*PIVWuwNHtEMnFojd.)

### 2.1.2 Configurer le code de base du projet de la partie 2

Si vous souhaitez passer directement à la partie 3 sans regarder la partie 2, vous devez d'abord construire la base de code en clonant le code de la partie 2.

* git clone [https://github.com/gyver98/redux-tesla-battery-range-calculator-tutorial](https://github.com/gyver98/redux-tesla-battery-range-calculator-tutorial)
* npm install
* npm start

Après le npm start, assurons-nous que l'application fonctionne.

### 2.1.3 En-tête Tesla

Le composant En-tête Tesla doit avoir un effet de fondu qui affiche progressivement le logo.

Tout d'abord, ouvrez le fichier **Header.css** et collez les propriétés d'animation et les valeurs des keyframes copiées depuis Animista. Ensuite, modifiez-le pour faire référence à cette classe dans le fichier **Header.js**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*HukM4NRUS6m8Kqg2.)

* Consultez [Header.css](https://gist.github.com/gyver98/6f13ec5d1fbf5aa5659b50b3a8d88c09#file-header-css)
* Consultez [Header.js](https://gist.github.com/gyver98/d1d4eb07a86f61a46b09ff83982c6cf2#file-header-js)

### 2.1.4 Titre <h1>

L'effet **focus-in-contract-bck** est susceptible de fonctionner pour le titre Tesla. Donnez l'effet d'animation de la même manière que vous l'avez fait pour l'en-tête Tesla.

Notez que l'élément de titre <h1> est défini dans App.js / App.css.

![Image](https://cdn-media-1.freecodecamp.org/images/0*VoXL1zKOOT2q1THD.)

* Consultez [App.js](https://github.com/gyver98/part3-animation-tesla-battery-range-calculator-tutorial/blob/master/src/App.js)
* Consultez [App.css](https://github.com/gyver98/part3-animation-tesla-battery-range-calculator-tutorial/blob/master/src/App.css)

### 2.1.5 TeslaCar

Pour le composant TeslaCar, qui a les effets les plus dynamiques, appliquons les deux effets suivants.

* Voiture Tesla : **slide-in-elliptic-bottom-fwd**
* Roues Tesla : **bounce-in-top**

/src/Components/TeslaCar/TeslaCar.css

```
.tesla-car-animation {  -webkit-animation: slide-in-elliptic-bottom-fwd 0.7s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;	-moz-animation: slide-in-elliptic-bottom-fwd 0.7s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;	animation: slide-in-elliptic-bottom-fwd 0.7s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;  }  
```

```
.tesla-wheels-animation {  -webkit-animation: bounce-in-top 2.3s both;  -moz-animation: bounce-in-top 2.3s both;  animation: bounce-in-top 2.3s both;}
```

```
@-webkit-keyframes slide-in-elliptic-bottom-fwd{0%{-webkit-transform:translateY(600px) rotateX(30deg) scale(0);transform:translateY(600px) rotateX(30deg) scale(0);-webkit-transform-origin:50% 100%;transform-origin:50% 100%;opacity:0}100%{-webkit-transform:translateY(0) rotateX(0) scale(1);transform:translateY(0) rotateX(0) scale(1);-webkit-transform-origin:50% -1400px;transform-origin:50% -1400px;opacity:1}}@keyframes slide-in-elliptic-bottom-fwd{0%{-webkit-transform:translateY(600px) rotateX(30deg) scale(0);transform:translateY(600px) rotateX(30deg) scale(0);-webkit-transform-origin:50% 100%;transform-origin:50% 100%;opacity:0}100%{-webkit-transform:translateY(0) rotateX(0) scale(1);transform:translateY(0) rotateX(0) scale(1);-webkit-transform-origin:50% -1400px;transform-origin:50% -1400px;opacity:1}}
```

```
@-webkit-keyframes bounce-in-top{0%{-webkit-transform:translateY(-500px);transform:translateY(-500px);-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in;opacity:0}38%{-webkit-transform:translateY(0);transform:translateY(0);-webkit-animation-timing-function:ease-out;animation-timing-function:ease-out;opacity:1}55%{-webkit-transform:translateY(-65px);transform:translateY(-65px);-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in}72%{-webkit-transform:translateY(0);transform:translateY(0);-webkit-animation-timing-function:ease-out;animation-timing-function:ease-out}81%{-webkit-transform:translateY(-28px);transform:translateY(-28px);-webkit-animation-timing-function:ease-in}90%{-webkit-transform:translateY(0);transform:translateY(0);-webkit-animation-timing-function:ease-out;animation-timing-function:ease-out}95%{-webkit-transform:translateY(-8px);transform:translateY(-8px);-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in}100%{-webkit-transform:translateY(0);transform:translateY(0);-webkit-animation-timing-function:ease-out;animation-timing-function:ease-out}}
```

```
@keyframes bounce-in-top{0%{-webkit-transform:translateY(-500px);transform:translateY(-500px);-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in;opacity:0}38%{-webkit-transform:translateY(0);transform:translateY(0);-webkit-animation-timing-function:ease-out;animation-timing-function:ease-out;opacity:1}55%{-webkit-transform:translateY(-65px);transform:translateY(-65px);-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in}72%{-webkit-transform:translateY(0);transform:translateY(0);-webkit-animation-timing-function:ease-out;animation-timing-function:ease-out}81%{-webkit-transform:translateY(-28px);transform:translateY(-28px);-webkit-animation-timing-function:ease-in}90%{-webkit-transform:translateY(0);transform:translateY(0);-webkit-animation-timing-function:ease-out;animation-timing-function:ease-out}95%{-webkit-transform:translateY(-8px);transform:translateY(-8px);-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in}100%{-webkit-transform:translateY(0);transform:translateY(0);-webkit-animation-timing-function:ease-out;animation-timing-function:ease-out}}
```

/src/Components/TeslaCar/TeslaCar.js

```
const TeslaCar = (props) => (  <div className="tesla-car tesla-car-animation">    <div className="tesla-wheels tesla-wheels-animation">          <;/div>  </div>);
```

* Consultez [TeslaCar.js](https://gist.github.com/gyver98/fedfe9ab47e7a16abeac94308a7ca68b#file-teslacar-part3-js)
* Consultez [TeslaCar.css](https://gist.github.com/gyver98/7e6bef3e05c1f3bce1d0a9a2381c5426#file-teslacar-part3-csshttps://github.com/gyver98/part3-animation-tesla-battery-range-calculator-tutorial/blob/master/src/components/TeslaCar/TeslaCar.css)

À ce stade, vous devriez voir ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*bR16Rxvlnxllgsx1.)

### 2.1.6 TeslaStats

Cette fois, donnons au composant TeslaStats un effet d'animation **slit-in-horizontal**. Donnez un délai de 2 secondes pour commencer après l'exécution de l'animation TeslaCar.

![Image](https://cdn-media-1.freecodecamp.org/images/0*spbWOTQeCqrUVXKL.)

* Consultez [TeslaStats.css](https://github.com/gyver98/part3-animation-tesla-battery-range-calculator-tutorial/blob/master/src/components/TeslaStats/TeslaStats.css)
* Consultez [TeslaStats.js](https://github.com/gyver98/part3-animation-tesla-battery-range-calculator-tutorial/blob/master/src/components/TeslaStats/TeslaStats.js)

### 2.1.7 Contrôles Tesla

Le compteur de vitesse, le compteur de température, et les composants Climat et Roues sont enveloppés dans la classe **tesla-controls**, nous pouvons donc simplement modifier App.css et App.js comme suit, sans modifier le CSS de chaque composant.

Fournissez les mêmes effets d'animation que ceux appliqués au composant TeslaStats. Donnez un délai de 2,5 secondes pour commencer après l'exécution de l'animation TeslaStats.

![Image](https://cdn-media-1.freecodecamp.org/images/0*t1pOPhXRCkOvZLUU.)

* Consultez [App.css](https://github.com/gyver98/part3-animation-tesla-battery-range-calculator-tutorial/blob/master/src/App.css)
* Consultez [App.js](https://github.com/gyver98/part3-animation-tesla-battery-range-calculator-tutorial/blob/master/src/App.js)

Voici ce que vous devriez voir :

![Image](https://cdn-media-1.freecodecamp.org/images/0*3tU3pt8uwr98NHYQ.)

Nous avons implémenté toutes les animations au moment où l'application est chargée. Maintenant, implémentons l'animation lorsqu'une action de l'utilisateur se produit.

### 2.2 Lorsqu'une action de l'utilisateur se produit

Lorsque l'utilisateur clique sur les compteurs de vitesse, de température et sur les roues, nous allons donner l'effet d'animation suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/0*5gWZanCv_hi6Jy-S.)

### 2.2.1 Compteur de vitesse

Tout d'abord, considérons ce qui se passe lorsque vous cliquez sur le compteur de vitesse.

Nous avons défini **mapStateToProps** et **mapDispatchToProps** comme un moyen de créer un conteneur TeslaSpeedCounter dans la partie 2 et de communiquer avec le Redux Store. Ensuite, nous faisons référence à l'état dans le composant TeslaCounter via **connect** et lorsque l'action se produit, nous la dispatchons vers le Redux Store pour mettre à jour le nouvel état et rendre la vue.

L'image suivante montre bien ce flux.

![Image](https://cdn-media-1.freecodecamp.org/images/0*o2yXNpGMcBekZR1D.)

Alors, comment animer lorsque le nouvel état est rendu par un événement de clic sur la vitesse ? Après avoir défini l'animation dans TeslaCounter.css, souhaitez-vous ajouter la classe flip-in-hor-top que vous souhaitez appliquer comme suit ?

```
<div className="flip-in-hor-top">  <p className="tesla-counter__number ">    { currentValue }    <span>{ initValues.unit }<;/span>  </p></div>
```

Cela n'aura aucun effet. Parce que seul le currentValue qui est mis à jour lorsque l'événement se produit est réaffiché. De plus, nous essayons d'appliquer différentes orientations aux événements de haut et de bas. Si c'est le cas, nous devons connaître la direction de l'animation ainsi que l'événement, puis nous assurer que la classe correspondante est appliquée et réaffichée.

### 2.2.2 TeslaCounter.css

Tout d'abord, définissons le code d'animation que nous voulons appliquer via Animista au fichier CSS après l'avoir copié. Ajoutez la classe d'animation suivante et les keyframes.

* flip-in-hor-bottom
* flip-in-hor-top
* keyframes flip-in-hor-bottom
* keyframes flip-in-hor-top

![Image](https://cdn-media-1.freecodecamp.org/images/0*a3c4Fxjs2OnA_gDH.)

* Consultez [TeslaCounter.css](https://github.com/gyver98/part3-animation-tesla-battery-range-calculator-tutorial/blob/master/src/components/TeslaCounter/TeslaCounter.css)

### 2.2.3 TeslaCounter.js

Pour appliquer différents effets d'animation selon l'événement de vitesse haut/bas, nous devons connaître le type de l'événement, le mettre à jour dans le store Redux avec le réducteur, et faire passer la nouvelle valeur d'état au TeslaCounter via les props. Au lieu d'ajouter ce type d'événement au store Redux, implémentons-le de manière à gérer l'**état local** du TeslaCounter. Puisque l'état local est requis, modifiez le composant fonctionnel actuel TeslaCounter en un **composant de classe**.

Nous avons également besoin de la méthode de cycle de vie de mise à jour **componentWillReceiveProps()** ici. Cette méthode est appelée lorsque les props sont passées au composant TeslaCounter. Le composant TeslaCounter a deux boutons haut/bas qui permettent à l'utilisateur de changer la valeur du compteur en cliquant dessus. Le bouton est lié à l'événement onClick et définit l'état dans le store Redux en dispatchant une action. La nouvelle valeur d'état est ensuite passée au composant TeslaCounter en tant que prop via connect() dans le conteneur TeslaCounter.

À chaque fois que l'utilisateur clique sur le bouton haut/bas, cela commence une mise à jour pour le composant TeslaCounter. La première méthode appelée sur le composant est **componentWillReceiveProps(nextProps)** en passant la nouvelle valeur de prop. Cela nous permet de comparer les props entrants avec nos props actuels et de prendre des décisions logiques basées sur la valeur. Nous pouvons obtenir nos props actuels en appelant **this.props** et la nouvelle valeur est l'argument **nextProps** passé à la méthode.

Alors, pourquoi avons-nous besoin de componentWillReceiveProps ? Il s'agit d'un hook qui nous permet de regarder la prochaine **mise à jour**. Si nous avons un état qui est un calcul de props, nous pouvons appliquer la logique ici en toute sécurité et stocker le résultat en utilisant **this.setState()**.

Ici, nous avons besoin d'un état **direction**, qui est la direction de l'animation, qui peut être obtenue en comparant la valeur actuelle avec la valeur mise à jour.

Vous pouvez voir tout le flux à travers l'image suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/0*3z3xL_MnAS6HgCkf.)

* Consultez [TeslaCounter.js](https://gist.github.com/gyver98/aba50231c963adfd7d072314d6a8e3f9#file-teslacounter-part3-js)

Maintenant, cliquez sur les compteurs de vitesse et de température pour confirmer que l'animation a été appliquée. Mais il y a un problème. Si vous cliquez alternativement sur les boutons Haut / Bas, ils fonctionnent normalement. Si vous cliquez sur le même bouton en continu, l'animation ne sera pas appliquée. Cela est dû au fait que la classe d'animation ne change que lorsque le type d'événement change.

Pour résoudre ce problème, ajoutez **animationEffect** à l'état local et utilisez setTimeout pour initialiser la classe d'animation appliquée après 0,5 seconde.

![Image](https://cdn-media-1.freecodecamp.org/images/0*v0uFl9IgHSsmpl8J.)

Maintenant, vous pouvez voir que cela fonctionne bien même si vous cliquez sur le même bouton en continu.

* Consultez [TeslaCounter.js](https://gist.github.com/gyver98/7431b3df5576de6a408121646588d578#file-final-teslacounter-part3-js)

### 2.2.4 Animation TeslaWheels

Enfin, appliquons des effets d'animation lors du clic sur les roues.

Tout d'abord, **bounce-in-top** est déjà défini dans TeslaCar.css, définissons donc une animation supplémentaire **bounce-in-bottom**. Ensuite, ouvrez le fichier TeslaCar.js et remplacez tesla-car-animation qui a été appliqué dans la section 2.1.5 TeslaCar par **tesla-wheel-animation-${props.wheelsize}**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*ASYtBrbYI-GbVMdR.)

* Consultez [TeslaCar.css](https://github.com/gyver98/part3-animation-tesla-battery-range-calculator-tutorial/blob/master/src/components/TeslaCar/TeslaCar.css)
* Consultez [TeslaCar.js](https://github.com/gyver98/part3-animation-tesla-battery-range-calculator-tutorial/blob/master/src/components/TeslaCar/TeslaCar.js)

Vous devriez avoir un calculateur d'autonomie Tesla entièrement fonctionnel avec animation :

![Image](https://cdn-media-1.freecodecamp.org/images/0*SbSA60aSiFXYfjDP.)

* Consultez le [code source complet](https://github.com/gyver98/part3-animation-tesla-battery-range-calculator-tutorial)