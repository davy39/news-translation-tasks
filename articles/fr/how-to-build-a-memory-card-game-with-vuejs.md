---
title: Comment créer un jeu de mémoire avec Vue.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-24T23:20:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-memory-card-game-with-vuejs
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a11740569d1a4ca234b.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: projects
  slug: projects
- name: vue
  slug: vue
seo_title: Comment créer un jeu de mémoire avec Vue.js
seo_desc: "By Tushar Gugnani\nIf you are new to Vue and want to refresh your basics,\
  \ this fun exercise will help you build an interesting game.\nIn this post, I will\
  \ take your through the step by step process of building a memory card game in VueJS.\
  \ \nHere is what..."
---

Par Tushar Gugnani

Si vous êtes nouveau dans Vue et que vous souhaitez rafraîchir vos bases, cet exercice amusant vous aidera à construire un jeu intéressant.

Dans cet article, je vais vous guider à travers le processus étape par étape de création d'un jeu de mémoire avec VueJS.

Voici ce que vous pouvez vous attendre à apprendre à la fin de cet article :

* Comment utiliser la directive _v-for_ pour parcourir un tableau d'objets.
* Liaison dynamique de classes et de styles en utilisant la directive _v-bind_
* Comment ajouter des _Méthodes_ et des propriétés _Computées_.
* Comment ajouter des propriétés réactives à un objet en utilisant Vue.set
* Comment utiliser la méthode _setTimeout_ pour retarder l'exécution de JavaScript.
* _Clonage superficiel vs clonage profond_ des objets JavaScript.
* Comment utiliser la bibliothèque d'utilitaires _Lodash_.

Commençons par les étapes.

## Préparation - Inclusion des bibliothèques

La première étape est simple : il suffit d'importer les bibliothèques depuis le CDN dans notre balisage HTML5 de base afin que nous puissions commencer notre petit projet.

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jeu de mémoire</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <!-- version de développement, inclut des avertissements de console utiles -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
    
</body>
</html>
```

## **Permettre à l'utilisateur de voir la grille de cartes**

Ensuite, définissons le balisage HTML nécessaire, le style CSS et une instance Vue de base afin que l'utilisateur puisse voir la grille de cartes.

### Instance Vue

Créons une nouvelle instance Vue et définissons la propriété de données unique nommée cards qui contient la liste des cartes.

```js
let app = new Vue({
    el: '#app',
    data:{
            cards: [
                {
                    name: 'Pomme',
                    img: 'apple.gif',

                },
                {
                    name: 'Banane',
                    img: 'banana.gif',
 
                },
                {
                    name: 'Orange',
                    img: 'orange.jpg',

                },
                {
                    name: 'Ananas',
                    img: 'pineapple.png',

                },
                {
                    name: 'Fraise',
                    img: 'strawberry.png',

                },
                {
                    name: 'Pastèque',
                    img: 'watermelon.jpg',

                },
            ],
    },
});
```

Chaque objet du tableau contient deux propriétés : le nom de l'image (qui sera utilisé pour effectuer la correspondance) et l'image de la carte.

### Balisage HTML

Maintenant que nous avons les données prêtes dans notre instance Vue, nous pouvons utiliser la directive v-for dans VueJS pour les parcourir.

```html
    <div id="app">
    <div class="row">
        <div class="col-md-6 col-lg-6 col-xl-5 mx-auto">
             <div class="row justify-content-md-center">
                    <div v-for="card in cards" class="col-auto mb-3 flip-container">
                    <div class="memorycard">
                        <div class="front border rounded shadow"><img width="100" height="150" src="/assets/images/memorycard/pattern3.jpeg"></div>
                        <div class="back rounded border"><img width="100" height="150" :src="'/assets/images/memorycard/'+card.img"></div>
                    </div>
                 </div>
            </div>
        </div>
    </div>
    </div>
```

Nous avons utilisé un balisage Bootstrap de base et la directive v-for de VueJS pour parcourir les cartes et les afficher dans un format de grille.

Chaque carte mémoire est composée de deux parties :

* front : Cela contient une image de motif commune pour toutes les cartes (vue de carte par défaut)
* back : Cela contient l'image réelle de la carte (doit être masquée par défaut)

Ajoutons un peu de CSS de base pour que nous ne montrions que la partie avant de la carte (motif de conception commun) :

```css
    .flip-container {
        -webkit-perspective: 1000;
        -moz-perspective: 1000;
        -o-perspective: 1000;
        perspective: 1000;
        min-height: 120px;
        cursor: pointer;
    }
    .front,
    .back {
        -webkit-backface-visibility: hidden;
        -moz-backface-visibility: hidden;
        -o-backface-visibility: hidden;
        backface-visibility: hidden;
        -webkit-transition: 0.6s;
        -webkit-transform-style: preserve-3d;
        -moz-transition: 0.6s;
        -moz-transform-style: preserve-3d;
        -o-transition: 0.6s;
        -o-transform-style: preserve-3d;
        -ms-transition: 0.6s;
        -ms-transform-style: preserve-3d;
        transition: 0.6s;
        transform-style: preserve-3d;
        top: 0;
        left: 0;
        width: 100%;
    }
    .back {
        -webkit-transform: rotateY(-180deg);
        -moz-transform: rotateY(-180deg);
        -o-transform: rotateY(-180deg);
        -ms-transform: rotateY(-180deg);
        transform: rotateY(-180deg);
        position: absolute;
    }
```

Actualisez la page et vous devriez voir six cartes empilées dans un format de grille faisant face à l'avant. L'image réelle de la carte est masquée à l'arrière.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-11-at-1.43.30-PM.png)
_Côté face de la carte (parcouru par la directive v-for)_

## Retourner les cartes

Ensuite, attachons un événement à nos cartes afin que, lorsqu'elles sont cliquées, elles se retournent et montrent l'image derrière elles.

Modifions notre tableau de cartes original pour ajouter une autre propriété à chaque carte. Cela déterminera si la carte est actuellement retournée.

Ajoutez le CSS suivant. Lorsque la classe flipped est ajoutée à la classe, elle montrera l'image de la carte. Cela donne également un bel effet de retournement.

```css
    .flip-container.flipped .back {
        -webkit-transform: rotateY(0deg);
        -moz-transform: rotateY(0deg);
        -o-transform: rotateY(0deg);
        -ms-transform: rotateY(0deg);
        transform: rotateY(0deg);
    }
    .flip-container.flipped .front {
        -webkit-transform: rotateY(180deg);
        -moz-transform: rotateY(180deg);
        -o-transform: rotateY(180deg);
        -ms-transform: rotateY(180deg);
        transform: rotateY(180deg);
    }
```

Utilisons l'événement de cycle de vie **created** de Vue pour ajouter la nouvelle propriété et ajouter une méthode flipCard pour retourner la carte

```js
    created(){
        this.cards.forEach((card) => {
            card.isFlipped = false;
        });
    },

    methods:{
        flipCard(card){
            card.isFlipped = true;
        }
    }
```

Tout d'abord, nous allons lier l'événement de clic aux cartes pour invoquer la méthode flipCard. Ensuite, nous allons également utiliser la directive v-bind pour lier la classe **flipped** à la carte.

```html
...
<div v-for="card in cards" class="col-auto mb-3 flip-container" :class="{ 'flipped': card.isFlipped }" @click="flipCard(card)">
 ...
```

Cela semble correct – voyons si les cartes se retournent au clic.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/cards-no-flip-vuejs-1.gif)
_La carte ne se retourne pas au clic_

Cela n'a pas fonctionné. Pourquoi ?

Revenons à notre méthode de cycle de vie created, où nous avons parcouru la liste des cartes et ajouté une nouvelle propriété nommée isFlipped. Cela semble correct – mais Vue n'a pas aimé cela.

Pour que les nouvelles propriétés d'objet soient réactives, vous devez les ajouter à l'objet en utilisant la méthode Vue.set.

```js
    created(){
        this.cards.forEach((card) => {
            Vue.set(card,'isFlipped',false)
        });
    },
```

Maintenant, les cartes devraient se retourner au clic :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/card-flip-vuejs.gif)

Très bien, bon travail. Passons à la suite.

## **Doublez et mélangez**

Oui, c'est ça ! Pour faire un jeu de mémoire avec ces cartes, nous devons avoir exactement une paire de chaque carte. Nous devons également mélanger l'ordre des cartes à chaque fois que le jeu est chargé.

Définissons une nouvelle propriété dans notre instance Vue nommée memoryCards. Ici, nous stockerons les cartes qui seront jouées (c'est-à-dire doubler la quantité de cartes réelles et aussi les mélanger).

```js
...
memoryCards: [],
...
```

### Doubler

Pour créer deux copies de toutes les cartes, concaténons le tableau de cartes pour créer et l'assigner à la propriété memoryCards.

Changez la directive v-for dans le balisage HTML pour parcourir la propriété memoryCards au lieu de cards :

```html
<div v-for="card in memoryCards" class="col-auto mb-3 flip-container" :class="{ 'flipped': card.isFlipped }" @click="flipCard(card)">
```

Ensuite, modifiez la méthode de cycle de vie **created** pour assigner le tableau concaténé dans memoryCards :

```js
    created(){
        this.cards.forEach((card) => {
            Vue.set(card,'isFlipped',false)
        });

        var cards1 = this.cards;
        var cards2 = this.cards;
        this.memoryCards = this.memoryCards.concat(cards1, cards2);
    },
```

Cela semble simple, n'est-ce pas ?

Mais cela ne va pas fonctionner correctement. Il y a deux problèmes avec ce code :

1. L'assignation directe de this.cards dans cards1 ne va pas créer une autre copie de l'objet cards. cards1 fait toujours référence à l'objet original.
2. Puisque cards1 et cards2 font toujours référence au même objet, cela signifie que nous avons concaténé deux tableaux qui pointent vers le même tableau d'objets.

Changer une propriété de l'objet dans l'objet memoryCards changera le tableau original ainsi que sa propre paire dans le tableau.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/card-double-flip-problem.gif)

Eh bien, c'est un problème.

Si vous cherchez des solutions pour copier correctement un tableau ou un objet afin qu'il ne fasse pas référence au tableau original, vous pourriez trouver des solutions qui font une copie superficielle du tableau.

### Qu'est-ce qu'une copie superficielle ?

Une copie superficielle fait référence au fait qu'un seul niveau est copié. Cela fonctionnera bien pour un tableau ou un objet contenant uniquement des valeurs primitives.

Une façon de faire une copie superficielle est via l'opérateur de propagation, qui dans notre cas sera quelque chose comme le code ci-dessous :

```js
...
   var cards1 = [...this.cards];
   var cards2 = [...this.cards];
   this.memoryCards = this.memoryCards.concat(cards1, cards2);
...
```

Mais ce n'est pas la solution pour nous, car dans notre cas nous avons un tableau d'objets et non de valeurs primitives. Ainsi, notre problème peut être résolu si nous faisons une copie profonde de notre tableau.

### Qu'est-ce qu'une copie profonde ?

Pour les objets et tableaux contenant d'autres objets ou tableaux, la copie de ces objets nécessite une copie profonde. Sinon, les modifications apportées aux références imbriquées modifieront les données imbriquées dans l'objet ou le tableau original.

Il existe plusieurs façons de faire une copie profonde, mais nous allons opter pour la manière la plus simple et la plus courante en utilisant la bibliothèque **Lodash**.

Maintenant, qu'est-ce que la bibliothèque **Lodash** ?

Lodash facilite JavaScript en éliminant les tracas de travailler avec des tableaux, des nombres, des objets, des chaînes, etc.

Pour notre cas, Lodash a une méthode pour effectuer deepCopy qui le rend ridiculement simple.

Tout d'abord, incluez Lodash dans votre page en le téléchargeant ou en le référençant via le CDN.

```html
<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.15/lodash.min.js"></script>
```

Ensuite, vous pouvez utiliser la méthode **cloneDeep** de Lodash pour effectuer la copie profonde de notre tableau de cartes.

```js
 var cards1 = _.cloneDeep(this.cards);
 var cards2 = _.cloneDeep(this.cards);
 this.memoryCards = this.memoryCards.concat(cards1, cards2);
```

### Mélanger

Maintenant, nous voulons mélanger le tableau concaténé. Lodash a également une méthode pour mélanger. Utilisons la méthode et simplifions également le code pour concaténer et mélanger en une seule ligne.

```js
created(){
        this.cards.forEach((card) => {
            Vue.set(card,'isFlipped',false)
        });

        this.memoryCards = _.shuffle(this.memoryCards.concat(_.cloneDeep(this.cards), _.cloneDeep(this.cards)));
    },
```

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vue-flip-proper.gif)

Les cartes sont maintenant mélangées et retournées comme prévu.

Passons à la suite !

## Correspondance des cartes

L'étape suivante consiste à faire correspondre les cartes retournées. Un utilisateur est autorisé à retourner un maximum de deux cartes à la fois. Si elles sont identiques, c'est une correspondance ! Si elles ne le sont pas, alors nous les retournons.

Attaquons-nous à cela.

Nous allons ajouter une nouvelle propriété à chaque carte pour suivre si la carte a déjà été appariée. Modifiez la méthode created pour inclure ce code :

```js
this.cards.forEach((card) => {
    Vue.set(card,'isFlipped',false);
    Vue.set(card,'isMatched',false);
});
```

Créez une nouvelle propriété de données pour stocker les cartes retournées :

```js
flippedCards: [],
```

Ensuite, nous modifions la méthode flipCard pour effectuer la correspondance :

```js
flipCard(card){
    card.isFlipped = true;

    if(this.flippedCards.length < 2)
        this.flippedCards.push(card);
    if(this.flippedCards.length === 2)    
        this._match(card);
},

_match(card){

    if(this.flippedCards[0].name === this.flippedCards[1].name)
        this.flippedCards.forEach(card => card.isMatched = true);
    else
        this.flippedCards.forEach(card => card.isFlipped = false);
    
    this.flippedCards = [];
},

```

La logique ici est simple : nous continuons à ajouter des cartes au tableau flippedCards jusqu'à ce qu'il y ait deux cartes.

Une fois qu'il y a deux cartes, nous effectuons la correspondance.

* Si le nom des deux cartes est le même, nous marquons les cartes comme appariées en définissant la propriété isMatched sur true.
* Sinon, nous définissons la propriété isFlipped sur false.

Nous vidons le tableau flippedCards après cela.

Ajoutez une nouvelle propriété CSS pour estomper les cartes qui correspondent :

```css
.matched{
   opacity: 0.3;
}
```

Ajoutez une liaison de classe au conteneur pour ajouter des cartes appariées si la propriété est définie sur true :

```html
:class="{ 'flipped': card.isFlipped, 'matched' : card.isMatched }"
```

Ici, la logique fonctionne bien, mais tout se passe trop vite pour que le joueur comprenne ce qui se passe. Si les cartes ne correspondent pas, elles sont retournées avant même que l'utilisateur ne puisse voir la carte révélée.

Utilisons la méthode setTimeout de JavaScript pour ajouter un délai délibéré de quelques microsecondes.

```js
_match(card){
    if(this.flippedCards[0].name === this.flippedCards[1].name){
        setTimeout(() => {
            this.flippedCards.forEach(card => card.isMatched = true);
            this.flippedCards = [];
        }, 400);
    }
    else{
        setTimeout(() => {
            this.flippedCards.forEach((card) => {card.isFlipped = false});
            this.flippedCards = [];
        }, 800);
    }
},
```

Nous avons ajouté un délai de 400 microsecondes avant de les marquer comme appariées, et 800 microsecondes pour retarder avant de les retourner.

Modifiez également la méthode flipCard pour ne pas retourner les cartes lorsque

* La carte est déjà appariée
* La carte est déjà retournée
* L'utilisateur a déjà retourné deux cartes

```js
flipCard(card){

    if(card.isMatched || card.isFlipped || this.flippedCards.length === 2)
            return;

    card.isFlipped = true;

    if(this.flippedCards.length < 2)
        this.flippedCards.push(card);
    if(this.flippedCards.length === 2)    
        this._match(card);
},
```

![Image](https://www.freecodecamp.org/news/content/images/2020/06/flipping-cards-memory.gif)

Nous y sommes presque, il ne reste que quelques étapes.

## Terminer le jeu

Le jeu est marqué comme terminé lorsque toutes les cartes sont appariées.

Écrivons rapidement la condition de code pour cela. Nous introduisons une nouvelle propriété de données dans notre instance Vue :

```js
...
finish: false
```

Ensuite, nous modifions la méthode de correspondance pour vérifier si toutes les cartes sont appariées après chaque correspondance réussie.

```js
setTimeout(() => {
    this.flippedCards.forEach(card => card.isMatched = true);
    this.flippedCards = [];

    // Toutes les cartes appariées ?
    if(this.memoryCards.every(card => card.isMatched === true)){
        this.finish = true;
    }

}, 400);
```

Nous utilisons la méthode **every** des tableaux JavaScript qui évalue la condition donnée pour la vérité, si ce n'est pas le cas, elle retourne false.

## Garder une trace du nombre total de tours et du temps total

Nous avons construit le jeu, alors maintenant, rendons-le plus intéressant en lui donnant quelques touches finales. Nous allons ajouter combien de tours un utilisateur a pris, et aussi comment il se débrouille en termes de temps pris pour compléter le jeu.

Tout d'abord, nous introduirons quelques nouvelles propriétés de données :

```js
start: false
turns: 0,
totalTime: {
    minutes: 0,
    seconds: 0,
},
```

Une fois que deux cartes sont retournées, nous augmenterons le compteur. Ainsi, nous modifierons la méthode _match pour incrémenter les tours.

```js
...
_match(card){

    this.turns++;
    
    ...
```

Ensuite, nous modifions la méthode flipCard pour démarrer le chronomètre :

```js
flipCard(card){

    if(card.isMatched || card.isFlipped || this.flippedCards.length === 2)
            return;

    
    if(!this.start){
        this._startGame();
    }
    
    ...
    ...
```

Ajoutez deux nouvelles méthodes pour démarrer l'horloge une fois le jeu commencé :

```js
_startGame(){
    this._tick();
    this.interval = setInterval(this._tick,1000);
    this.start = true;
},

_tick(){
    if(this.totalTime.seconds !== 59){
         this.totalTime.seconds++;
         return
     }

     this.totalTime.minutes++;
     this.totalTime.seconds = 0;
},
```

Nous utilisons des propriétés calculées pour ajouter un '0' devant les minutes et les secondes lorsqu'elles sont à un seul chiffre :

```js
computed:{
    sec(){
        if(this.totalTime.seconds < 10){
            return '0'+this.totalTime.seconds;
        }
        return this.totalTime.seconds;
    },
    min(){
        if(this.totalTime.minutes < 10){
            return '0'+this.totalTime.minutes;
        }
        return this.totalTime.minutes;
    }
}
```

Ajoutez le HTML suivant juste au-dessus de votre HTML pour afficher le nombre total de tours et le temps total :

```html
<div class="d-flex flex-row justify-content-center py-3">
    <div class="turns p-3"><span class="btn btn-info">Tours : <span class="badge" :class="finish ? 'badge-success' : 'badge-light'">{{turns}}</span> </span></div>
    <div class="totalTime p-3"><span class="btn btn-info">Temps total : <span class="badge" :class="finish ? 'badge-success' : 'badge-light'">{{min}} : {{sec}}</span></span></div>
</div>
```

Modifiez la condition de fin de jeu pour arrêter le chronomètre une fois le jeu terminé :

```js
if(this.memoryCards.every(card => card.isMatched === true)){
    clearInterval(this.interval);
    this.finish = true;
}
```

## Réinitialiser

Nous en sommes à notre dernière étape – bon travail si vous êtes arrivé à ce point.

Ajoutons un bouton pour réinitialiser le jeu :

```html
<div class="totalTime p-3"><button class="btn btn-info" @click="reset" :disabled="!start">Redémarrer</button></div>
```

Liez l'événement de clic à la méthode reset :

```js
reset(){
    clearInterval(this.interval);

    this.cards.forEach((card) => {
        Vue.set(card, 'isFlipped',false);
        Vue.set(card, 'isMatched',false);
    });

    setTimeout(() => {  
        this.memoryCards = [];
        this.memoryCards = _.shuffle(this.memoryCards.concat(_.cloneDeep(this.cards), _.cloneDeep(this.cards)));
        this.totalTime.minutes = 0;
        this.totalTime.seconds = 0;
        this.start = false;
        this.finish = false;
        this.turns = 0;
        this.flippedCards = [];
           
        }, 600);
    
},
```

Nous effaçons le chronomètre, remélangeons les cartes et réinitialisons tous les champs à leur valeur par défaut.

Nous modifions également la méthode de cycle de vie created pour appeler la méthode reset afin d'éviter la duplication de code :

```js
created(){
    this.reset();
},
```

Et voilà ! Vous avez maintenant un jeu de mémoire en VueJS.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/memory-game-success.gif)



*Si vous cherchez à apprendre les bases de VueJS avec des exercices pratiques amusants comme celui-ci, vous pouvez lire la série de tutoriels VueJS sur mon blog personnel [5Balloons VueJS Course](https://www.5balloons.info/vuejs-tutorials-course-introduction/).*