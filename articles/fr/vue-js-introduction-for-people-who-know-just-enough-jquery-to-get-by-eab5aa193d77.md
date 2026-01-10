---
title: Une introduction à Vue.js pour les personnes qui connaissent juste assez jQuery
  pour s'en sortir
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-10T23:30:41.000Z'
originalURL: https://freecodecamp.org/news/vue-js-introduction-for-people-who-know-just-enough-jquery-to-get-by-eab5aa193d77
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-8AAdexfOAK9R-AIha_PBQ.png
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: jQuery
  slug: jquery
- name: Vue.js
  slug: vuejs
- name: Web Development
  slug: web-development
seo_title: Une introduction à Vue.js pour les personnes qui connaissent juste assez
  jQuery pour s'en sortir
seo_desc: 'By Matt Rothenberg

  I’ve had a love-hate relationship with JavaScript for years.

  I got to know the language by way of the design and development community’s favorite
  whipping boy, jQuery. You see, at the time I began learning JavaScript, as a “Designe...'
---

Par Matt Rothenberg

J'ai eu une relation amour-haine avec JavaScript pendant des années.

J'ai appris à connaître le langage grâce au bouc émissaire préféré de la communauté de design et de développement, [jQuery](https://jquery.com/). Vous voyez, à l'époque où j'ai commencé à apprendre JavaScript, en tant que "Designer qui code", travailler avec jQuery était une expérience magique. Je pouvais faire apparaître et disparaître des modales avec `fadeIn` et `fadeOut`. Avec une bibliothèque tierce, je pouvais ajouter un défilement parallaxe à mon portfolio avec un simple appel de fonction. Presque tout ce que j'aurais pu rêver était encapsulé dans [un seul fichier d'environ 100 Ko](https://code.jquery.com/jquery-3.2.1.min.js)…

Et puis [Angular](https://angularjs.org/) est sorti. Je n'avais _aucun_ _choix_ que de refaire tout mon portfolio avec ce framework. Et puis [React](https://facebook.github.io/react/) est sorti. Je n'avais _aucun_ _choix_ que de refaire tout mon portfolio avec cette bibliothèque. Et puis [Vue.js](http://vuejs.org) est sorti. Je n'avais _aucun_ _choix_ que de refaire tout mon portfolio avec cette bibliothèque… Vous voyez où cela mène.

Sans blague, j'ai grandement apprécié perfectionner mes compétences en JavaScript en construisant des choses ici et là avec ces différents frameworks et bibliothèques. J'ai lu d'innombrables articles et tutoriels dans le processus, mais aucun ne m'a marqué plus que l'article de Shu Uesugi, « [React.js Introduction For People Who Know Just Enough jQuery To Get By](http://chibicode.com/react-js-introduction-for-people-who-know-just-enough-jquery-to-get-by/) ».

Shu emmène les lecteurs — qui sont supposés avoir un certain niveau de maîtrise des fondamentaux de JavaScript et de jQuery — dans un voyage à travers le monde de React alors qu'ils construisent un clone du composant « composer un tweet » de Twitter.

Ce cadre conceptuel m'a été très utile en tant que personne qui apprend mieux en faisant. En effet, chaque fois qu'une nouvelle bibliothèque JavaScript sort, je me retrouve à revenir à l'exemple de cet article pour tester les eaux. Et donc, j'aimerais emprunter ce cadre alors que je vous guide à travers mon expérience récente d'apprentissage de Vue.

Avant de commencer les étapes ci-dessous, je vous encourage vivement à lire l'article de Shu. Il fait un travail fantastique en vous guidant à travers le code jQuery que vous pourriez écrire afin d'implémenter certaines de ces fonctionnalités. Ainsi, et afin de réduire le risque de redondance, je me concentrerai sur vous montrer les tenants et aboutissants de Vue.

### Ce que nous construisons

La plupart d'entre nous tweetons (certains plus prolifiquement que d'autres). Nous sommes donc probablement familiers avec le composant d'interface utilisateur dans la capture d'écran ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*U74cvvl2oY5Yf4Kq0AMMYA.png)
_La boîte « Composer un Tweet » de Twitter_

Croyez-le ou non, ce composant d'interface utilisateur est un excellent exemple de la manière dont Vue (et React, selon Shu) pourrait améliorer votre vie en tant que développeur JavaScript/jQuery. Les éléments de ce composant sur lesquels nous allons nous concentrer aujourd'hui sont :

* La `<textarea>` où les utilisateurs peuvent entrer leur tweet
* Le `<button>` qui est activé/désactivé en fonction de la longueur du tweet
* Un compteur qui indique combien de caractères (sur 140) restent, et change de couleur pour avertir l'utilisateur de cette limite
* Une icône de caméra qui, lorsqu'elle est cliquée, permet aux utilisateurs de joindre des photos à leur tweet
* Une liste des photos qui ont été jointes
* Un bouton (par photo) pour la supprimer du tweet

#### Si vous êtes bloqué

Si à un moment donné vous tombez sur quelque chose de confus ou mal expliqué, n'hésitez pas à me tweeter à [@mattrothenberg](https://twitter.com/mattrothenberg). Gardez à l'esprit en lisant cet article : ce n'est pas vous, c'est définitivement moi.

Commençons.

#### Comment nous allons le construire

Aujourd'hui, nous allons utiliser [CodePen](https://codepen.io) pour construire notre composant « Composer un Tweet ». Pour les non-initiés, CodePen est un éditeur en ligne HTML/CSS/JavaScript similaire à [JSBin](http://jsbin.com/) ou [JSFiddle](http://jsfiddle.net). Pour chaque étape, j'intégrerai un CodePen avec le code pertinent.

### Étape 1 : Échafauder le projet

La première chose que nous devons faire, avant d'écrire du JavaScript, est d'écrire le balisage pour notre composant « Composer un Tweet ». Aujourd'hui, nous allons utiliser [Tachyons](http://tachyons.io/) pour presque tous nos besoins stylistiques (afin de ne pas avoir à écrire de CSS superflu, et de pouvoir nous concentrer sur le balisage et le JavaScript).

Je pars du principe que vous êtes assez calé en CSS, donc je ne passerai pas de temps à vous expliquer l'approche de Tachyons pour le style (tl;dr beaucoup de style, beaucoup de classes, très fonctionnel).

Dans ce CodePen, j'ai également intégré Vue via CDN. En effet, l'un des principaux arguments de vente de Vue est la simplicité avec laquelle il peut être intégré dans une nouvelle base de code ou existante.

Avec tout en place, commençons à travailler sur certaines fonctionnalités.

### Étape 2 : Implémenter la première fonctionnalité — Le bouton Tweet doit être initialement désactivé

**Description de la fonctionnalité** : Désactiver le bouton bleu Tweet jusqu'à ce qu'un utilisateur ait entré au moins un caractère dans la `textarea`.

Tout d'abord, mettons en place notre instance Vue. Comme mentionné ci-dessus, Vue a conquis le cœur et l'esprit des développeurs par sa simplicité d'installation et sa facilité d'utilisation. Nous pouvons construire une instance Vue avec le code suivant.

```
new Vue({  el: '#twitterVue',  data: {    tweet: ''  },  computed: {    tweetIsEmpty: function() {      return this.tweet.length === 0;    }  }})
```

Permettez-moi d'expliquer ce qui se passe ici —

* `el` fait référence à l'élément DOM auquel nous attachons notre instance Vue. Cela devrait vous sembler similaire à l'instanciation d'un plugin jQuery en passant un sélecteur donné, qu'il s'agisse d'un nom de classe ou d'un ID.
* `data` est un objet qui décrit le modèle de données de notre instance, ou son état. Nous pouvons accéder aux attributs spécifiés dans ce modèle à la fois dans notre HTML — via une syntaxe spéciale avec des accolades `{{tweet}}` — et dans l'instance elle-même (indice, regardez le corps de la fonction `tweetIsEmpty`)
* `computed` est un objet qui décrit, comme vous pourriez le deviner, des propriétés calculées basées sur notre modèle de données. Au lieu d'ajouter de la logique à notre HTML, il est recommandé d'encapsuler ce type d'état (ou toute valeur dérivée, d'ailleurs) via des fonctions définies sur la clé `computed` de notre instance Vue.

Tournez maintenant notre attention vers le HTML, vous verrez que notre balisage a légèrement changé par rapport au premier CodePen. Plus précisément, nous avons apporté trois changements.

1. Nous avons ajouté l'id `twitterVue` à la `div` la plus externe afin de pouvoir construire notre instance Vue.

```
<div id="twitterVue">...</div>
```

2. Nous avons ajouté la directive `**v-model**` à notre `textarea`, créant ainsi une [liaison bidirectionnelle](https://vuejs.org/v2/guide/forms.html) entre l'entrée de l'utilisateur et le modèle de données de notre instance. Maintenant, chaque fois qu'un utilisateur tape dans la `textarea`, l'attribut `**tweet**` du modèle de données de notre instance est automatiquement mis à jour.

```
<textarea v-model="tweet"></textarea>
```

3. Nous avons ajouté l'attribut `**:disabled**` à notre `button`. Le deux-points précédant `disabled` indique que nous souhaitons _évaluer_ le contenu entre les guillemets comme une expression JavaScript. Si nous omettions le deux-points, le contenu serait traité comme une chaîne de caractères. Vous noterez également que nous avons ajouté quelques lignes de CSS pour donner au bouton désactivé un style visuel distinct.

```
<button :disabled="tweetIsEmpty">Tweet</button>
```

```
...
```

```
button[disabled] {  cursor: not-allowed;  opacity: .5;}
```

4. Nous avons également ajouté une propriété calculée sur notre instance appelée `**tweetIsEmpty**`. Notez que cette propriété est en fait une _fonction_ qui retourne une valeur booléenne basée sur la longueur de l'attribut `tweet` de notre modèle de données. Vue rend très simple l'accès à votre modèle de données à la fois dans le HTML (comme montré ci-dessus) et dans l'instance elle-même. Grâce à la magie de la liaison de données bidirectionnelle, cette fonction est évaluée lorsque la valeur de `tweet` est mise à jour. Lorsque la fonction évalue à _vrai_, notre bouton est désactivé, et vice-versa.

```
tweetIsEmpty: function() {  return this.tweet.length === 0;}
```

Je dois admettre que cela m'a semblé être de la magie lorsque j'ai commencé avec Vue. Ce qui m'a aidé, c'est de littéralement _voir_ ce qui se passait avec notre modèle de données sous le capot alors que j'interagissais avec le composant. Puisque nous pouvons facilement accéder à notre modèle de données dans notre HTML via la syntaxe mentionnée ci-dessus avec les accolades, nous pouvons construire une boucle de retour visuelle rapide. Score !

```
<p>La valeur de <strong>tweet</strong> est : {{tweet}} </p><p>La valeur de <strong>tweetIsEmpty</strong> est : {{ tweetIsEmpty}}</p>
```

N'hésitez pas à répéter cette étape si quelque chose en cours de route était confus (soit à cause de mes pauvres compétences en écriture ou en codage, soit à cause de Vue lui-même). Envoyez un tweet ou laissez un commentaire si vous avez des questions particulières.

### Étape 3 : Implémenter la deuxième fonctionnalité — Afficher le nombre de caractères restants

**Description de la fonctionnalité** : Au fur et à mesure qu'un utilisateur tape, afficher le nombre de caractères restants (sur 140) dans le tweet. Si un utilisateur a entré plus de 140 caractères, désactiver le bouton bleu Tweet.

Jusqu'à présent, nous avons appris la liaison de données bidirectionnelle et les propriétés calculées, des concepts qui sont au cœur même de Vue. C'est notre jour de chance, car nous pouvons exploiter ces concepts pour construire notre prochaine fonctionnalité : montrer aux utilisateurs combien de caractères (sur 140) restent, et désactiver le bouton si cette limite est dépassée.

Une fois de plus, je vais vous guider à travers les changements JavaScript et HTML nécessaires pour implémenter cette fonctionnalité.

Dans notre JavaScript, nous avons fait quelques choses.

1. En tant que mesure d'entretien, nous avons énuméré la longueur maximale d'un tweet (140 caractères) comme une constante, `**MAX_TWEET_LENGTH**`.

```
const MAX_TWEET_LENGTH = 140;
```

2. Nous avons ajouté une autre propriété calculée, `**charactersRemaining**`, qui retourne dynamiquement la différence entre 140 et la longueur du tweet saisi par l'utilisateur.

```
charactersRemaining: function() {  return MAX_TWEET_LENGTH - this.tweet.length;}
```

3. Nous avons renommé l'ancienne propriété `**tweetIsEmpty**` en `**tweetIsOutOfRange**` et mis à jour la logique de la fonction en conséquence. Notez comment nous utilisons la propriété calculée `**charactersRemaining**` pour dériver _cette_ valeur. Hourra pour la réutilisation du code !

```
tweetIsOutOfRange: function() {  return this.charactersRemaining == MAX_TWEET_LENGTH       || this.charactersRemaining < 0; }
```

Du côté HTML, nous n'avons que quelques changements à faire, grâce à la puissance de la liaison de données bidirectionnelle de Vue.

```
<div class="flex items-center">  <span class="mr3 black-70">{{ charactersRemaining }}</span>  <button :disabled="tweetIsOutOfRange" class="button-reset bg-blue bn white f6 fw5 pv2 ph3 br2 dim">Tweet</button></div>
```

Pour les apprenants visuels, regardez la magie :

### Étape 4 : Implémenter la troisième fonctionnalité : Style conditionnel de l'indicateur « Caractères restants »

**Description de la fonctionnalité** : Lors de la composition d'un Tweet, la couleur de l'indicateur « caractères restants » doit changer en rouge foncé lorsque seulement vingt caractères restent, et en rouge clair lorsque dix ou moins restent.

Manipuler le style ou la classe d'un élément peut être fastidieux avec jQuery, et Vue offre une méthode beaucoup plus propre pour le faire. L'approche de Vue semble plus déclarative, en ce sens que vous décrivez _comment_ vous voulez que le style de quelque chose change (basé, par exemple, sur un état donné) et vous laissez Vue faire le travail difficile.

Dans le contexte de cette fonctionnalité, notre indicateur « caractères restants » a deux états, et une classe CSS correspondante pour chacun.

1. Lorsque entre dix et vingt caractères restent, l'indicateur doit avoir la classe `dark-red`
2. Lorsque moins de dix caractères restent, l'indicateur doit avoir la classe `light-red`

À ce stade, votre cerveau Vue devrait crier « PROPRIÉTÉS CALCULÉES ! » Alors, obéissons à ce cerveau et câblons ces propriétés.

```
underTwentyMark: function() {  return this.charactersRemaining <= 20     && this.charactersRemaining > 10;  },underTenMark: function() {  return this.charactersRemaining <= 10;}
```

Avec notre logique en place, examinons l'une des manières dont Vue gère le style conditionnel : la directive `v-bind:class`. Cette directive attend un objet dont les clés sont des classes CSS, et dont les valeurs sont les propriétés calculées correspondantes.

```
{ 'dark-red': underTwentyMark, 'light-red': underTenMark }
```

En ajoutant la directive à la balise `span` qui enferme notre indicateur « caractères restants », nous avons complété notre fonctionnalité.

```
<span   v-bind:class="{ 'dark-red': underTwentyMark, 'light-red': underTenMark }">  {{ charactersRemaining }}</span>
```

Sous le capot, et grâce à la liaison de données bidirectionnelle, Vue gérera l'ajout et la suppression de ces classes en fonction des propriétés calculées spécifiées.

### Étape 5 : Implémenter la quatrième fonctionnalité : UX « Joindre une photo »

**Description de la fonctionnalité** : Permettre aux utilisateurs de joindre une seule photo à leur tweet via une boîte de dialogue de sélection de fichier. Lorsque la photo a été téléchargée, l'afficher sous la `textarea`, et permettre aux utilisateurs de supprimer la pièce jointe en cliquant sur l'image

Avertissement : il se passe _beaucoup_ de choses dans cette section. La beauté est que, malgré cette fonctionnalité ajoutant une fonctionnalité considérable, nous n'aurons pas à écrire autant de code. Alors, commençons par décomposer la conception de l'interaction en étapes.

1. L'utilisateur clique sur le bouton « Ajouter une photo »
2. L'utilisateur voit une boîte de dialogue de sélection de fichier et peut sélectionner **une** **photo** à télécharger
3. Après avoir sélectionné la photo, une boîte apparaît sous la `textarea` avec la photo sélectionnée à l'intérieur
4. L'utilisateur clique sur le bouton **X** circulaire pour supprimer la photo
5. L'utilisateur voit l'état initial de l'étape 1

Jusqu'à présent, nous n'avons pas encore fait de gestion d'événements (écouter les clics de bouton, les changements d'entrée, etc.). Comme vous pourriez vous y attendre, Vue facilite la gestion de tels événements en nous offrant la directive `v-on` (@ pour faire court). En passant une méthode comme valeur de cette directive, nous pouvons effectivement écouter les événements DOM et exécuter du JavaScript lorsqu'ils sont déclenchés.

Avant de plonger dans notre travail de fonctionnalité, un peu de pratique en rafale.

La gestion des événements est aussi simple que d'ajouter la directive `@click` à un bouton donné et d'ajouter une méthode correspondante à la clé `methods` de notre instance Vue.

```
<button @click="logNameToConsole">Log User's Name</button>
...
methods: {  logNameToConsole: function() {    if( this.name !== 'Donald Trump' ) {      console.log(this.name);     } else {      console.warn('Sorry, I do not understand');    }  },}
```

Retour à notre travail de fonctionnalité… Dans cette étape, notre balisage et notre JavaScript ont changé de la manière suivante :

1. Nous avons ajouté un `button` avec une directive `**@click**`. Lorsque l'utilisateur clique sur ce bouton, la méthode `**triggerFileUpload**` sera appelée.

```
<button @click="triggerFileUpload">...</button>
```

Alors, dans notre JavaScript, ajoutons une clé `methods` à notre instance Vue avec ladite méthode à l'intérieur, ainsi qu'un attribut de données pour notre photo.

```
data: { photo: null},computed: {},methods: {  triggerFileUpload: function() {    this.$refs.photoUpload.click(); // LOLWUT?  },}
```

2. Il est notoirement difficile de [styliser les entrées de fichier HTML5](http://stackoverflow.com/questions/572768/styling-an-input-type-file-button). Une solution de contournement implique de mettre un `input` dans le DOM et de le cacher avec CSS. Pour que le navigateur ouvre le sélecteur de fichiers natif, cet `input` _doit_ être cliqué. Comment il est cliqué, et comment le client gère ce que l'utilisateur télécharge, est une autre question.

Dans notre balisage, nous avons ajouté un tel `input` et l'avons caché avec une classe spéciale `hide`. Nous avons également ajouté quelques autres attributs qui valent la peine d'être mentionnés :

```
<input ref="photoUpload" @change="handlePhotoUpload" type="file" class="hide">
```

* L'attribut `ref` est utilisé pour enregistrer une _référence_ à un élément DOM donné. Étant donné cette référence, nous pouvons accéder à l'élément DOM dans notre code JavaScript avec `**this.$refs.photoUpload**`. Ce qui signifie que nous pouvons déclencher programmatiquement un événement `click()` sur cet élément, contournant ainsi le défi décrit ci-dessus.
* Cliquer sur l'entrée est une chose ; gérer le fichier que l'utilisateur télécharge en est une autre. Heureusement, Vue nous permet d'attacher un gestionnaire à l'événement de changement de l'entrée via la directive `@change`. La méthode que nous passons à cette directive sera invoquée après qu'un utilisateur a sélectionné un fichier dans le sélecteur de fichiers. Cette méthode, `**handlePhotoUpload**`, est assez simple

```
handlePhotoUpload: function(e) {  var self = this;  var reader = new FileReader();        reader.onload = function(e) {    // Définir cette chaîne base 64 à la clé 'photo' de notre modèle de données    self.photo = (e.target.result);  }  // Lire le fichier téléchargé comme une chaîne base 64  reader.readAsDataURL(e.target.files[0]); }
```

Prenez une profonde inspiration, car nous avons presque terminé avec cette fonctionnalité !

Une fois qu'un utilisateur a téléchargé une photo, nous devons afficher une boîte sous la `textarea` avec la photo sélectionnée à l'intérieur. Tout comme le style conditionnel des éléments est un jeu d'enfant avec Vue, il en va de même pour le rendu conditionnel, ou l'affichage des éléments. Vous noterez que dans notre HTML, nous avons ajouté le balisage suivant sous la `textarea`.

```
<div v-if="photoHasBeenUploaded">  <figure>    <button @click="removePhoto">      ...    </button>    <img v-bind:src="photo">  </figure></div>
```

Vue offre une poignée d'aides de modèle (`v-if`, `v-show`, `v-else`, etc) pour vous aider à afficher et masquer du contenu de manière conditionnelle. Lorsque l'expression JavaScript passée à cette directive évalue à vrai, l'élément est rendu, et vice-versa.

Dans notre cas, nous avons ajouté une déclaration `**v-if**` qui évalue la propriété calculée `**photoHasBeenUploaded**`.

```
photoHasBeenUploaded: function() {  return this.photo !== null;}
```

Lorsque cette fonction évalue à vrai — lorsque la clé photo de notre modèle de données n'est pas égale à null — l'ensemble de la `div` est rendu. Voilà !

Et à l'intérieur de cette `div`, nous rendons deux éléments :

1. L'image qui a été jointe, en passant le contenu de la clé `photo` de notre modèle de données à la directive `v-bind:src` de Vue
2. Un bouton de suppression qui présente un autre exemple du gestionnaire `@click`, celui-ci invoquant une fonction qui « supprime » la photo en définissant la clé `photo` de notre modèle de données à null.

```
removePhoto: function() {  this.photo = null;}
```

Nous y sommes presque.

### Étape 6 : Correction, l'utilisateur peut joindre « _photos_ »

Donc, nous pouvons gérer efficacement un utilisateur joignant _une_ photo au Tweet, mais que se passe-t-il s'il souhaite télécharger plusieurs photos ?

À ce stade, vous devriez penser quelque chose comme : « Je suppose que le seul changement significatif ici est de pouvoir montrer _plusieurs_ images dans cette boîte qui apparaît de manière conditionnelle sous la textarea, considérant que nous avons déjà câblé nos gestionnaires d'événements… » Et vous avez raison ! Examinons les étapes que nous devons suivre

1. Nous devons mettre à jour notre modèle de données en changeant `photo` en `photos`, la nouvelle clé étant un _tableau_ de chaînes base64 (et non une seule chaîne base64)

```
data: {  photos: []},
```

2. Nous devons mettre à jour notre propriété calculée `photoHasBeenUploaded` pour vérifier la longueur de notre nouvelle clé `photos`, qui est maintenant un tableau.

```
photoHasBeenUploaded: function() {  return this.photos.length > 0;}
```

3. Nous devons mettre à jour notre gestionnaire d'événement `@change` de l'entrée pour _boucler_ sur les fichiers téléchargés et les pousser sur notre clé `photos`.

```
handlePhotoUpload: function(e) {  var self = this;  var files = e.target.files;
```

```
  for(let i = 0; i < files.length; i++) {    let reader = new FileReader();
```

```
    reader.onloadend = function(evt) {      self.photos.push(evt.target.result);    }
```

```
    reader.readAsDataURL(files[i]);  }},
```

Cependant, du côté HTML, nous devons nous aventurer en territoire inconnu. Itérer sur des données et rendre du contenu avec jQuery peut être fastidieux.

```
var array = [1, 2, 3, 4, 5];var newHTML = [];for (var i = 0; i < array.length; i++) {    console.log('UGHHHHHH');    newHTML.push('<span>' + array[i] + '</span>');}$(".element").html(newHTML.join(""));
```

Heureusement, Vue offre une abstraction sur cette procédure par le biais de la directive `v-for`. Cette directive attend que vous [fournissiez une expression sous la forme de](https://vuejs.org/v2/guide/list.html) `(thing, index) in collectionOfThings`, où `collectionOfThings` est le tableau source, `thing` est un alias pour l'élément du tableau sur lequel on itère, et `index` est, eh bien, l'index de cet élément.

Un exemple prototypique pourrait ressembler à ceci :

Là où nous avions un seul élément `figure` pour la photo téléchargée par l'utilisateur, nous aurons maintenant _N_ balises `figure` correspondant à la longueur du tableau source `photos`.

Heureusement pour nous, notre balisage n'a pas besoin de changer trop radicalement puisque la structure globale du design est toujours la même.

```
<figure v-for="(photo, index) in photos">  <button @click="removePhoto(index)">    ...  </button>  <img v-bind:src="photo" class="h3 w3"></figure>
```

Le seul changement que nous devons apporter concerne la méthode `removePhoto` qui, auparavant, définissait la clé `photo` unique de notre modèle de données à `null`. Maintenant, puisque nous avons _N_ photos, nous devons passer l'index de l'élément à la méthode `removePhoto` et extraire cet élément du tableau.

```
removePhoto: function(index) {  this.photos.splice(index, 1);}
```

### Étape 7 : Animation + Travail supplémentaire

Dans l'interface utilisateur de Twitter, le composant « Composer un Tweet » s'ouvre dans une modale. Pour notre grand final, j'aimerais appliquer toutes les techniques Vue que nous avons apprises jusqu'à présent et en introduire une autre : [transitions](https://vuejs.org/v2/guide/transitions.html).

![Image](https://cdn-media-1.freecodecamp.org/images/1*yjSu85EKvxBdwRKqIwJtVA.png)
_Cycle de vie des transitions_

Un mot d'avertissement, les transitions sont un _vaste_ sujet dans le monde Vue. Nous allons examiner et implémenter une fine tranche de cette fonctionnalité, à savoir l'intégration d'une bibliothèque d'animation tierce, [Velocity JS](http://velocityjs.org/), avec Vue.

En résumé, Vue fournit un composant `transition` qui vous permet d'ajouter des animations d'entrée/sortie pour l'élément contenu à l'intérieur, à condition que l'élément soit défini pour être affiché de manière conditionnelle via, par exemple, une directive `v-if` ou `v-show`.

```
<transition   name="modal-transition"  v-on:enter="modalEnter"   v-on:leave="modalLeave">    <div v-if="modalShowing">       <!-- Notre contenu de modale va ici ! -->    </div></transition>
```

Dans notre exemple, nous avons attaché deux méthodes qui correspondent à deux événements dans le cycle de vie de la transition : `v-on:enter` et `v-on:leave`. Nous avons ainsi ajouté ces définitions de méthodes à notre instance Vue, en nous appuyant sur Velocity JS pour faire un `fade` de notre modale en entrée et en sortie.

```
methods: {  modalEnter: function(el, done) {    Velocity(el, 'fadeIn', { duration: 300, complete: done, display: 'flex' })  },  modalLeave: function(el, done) {    Velocity(el, 'fadeOut', { duration: 300, complete: done })  }}
```

Comme mentionné ci-dessus, la `transition` se déclenchera lorsque l'élément contenu à l'intérieur sera défini pour s'afficher de manière conditionnelle. Ainsi, sur la `div` intérieure de notre composant `transition`, nous avons ajouté une déclaration `v-if` dont la valeur est un booléen `modalShowing`. Mettons à jour le modèle de données de notre instance en conséquence.

```
data: {  modalShowing: false}
```

Maintenant, lorsque nous voulons afficher la modale, tout ce que nous avons à faire est de définir ce booléen à vrai !

```
<button @click="showModal">Composer un Tweet</button>
```

Et écrire une méthode correspondante.

```
hideModal: function() {  this.modalShowing = false;},showModal: function() {  this.modalShowing = true;},
```

Avec un peu de magie CSS, nous avons également attaché un gestionnaire d'événement `click` à l'arrière-plan, afin que les utilisateurs puissent masquer la modale. Score !

```
<div   @click="hideModal"  class="backdrop"></div>
```

### Conclusion

Eh bien, j'espère que cela n'a pas été trop douloureux (et que vous avez appris une ou deux choses en cours de route). Nous n'avons jeté qu'un coup d'œil à une petite partie de ce que Vue a à offrir, bien que, comme mentionné ci-dessus, ces concepts sont cruciaux pour déverrouiller le potentiel de Vue.

J'admets qu'il est injuste de comparer Vue à jQuery. Ils sont des produits de différentes époques, avec des cas d'utilisation assez différents. Cependant, pour ceux qui ont lutté pour apprendre la manipulation du DOM et la gestion des événements à travers jQuery, j'espère que ces concepts sont un bol d'air frais que vous pouvez appliquer à votre flux de travail.