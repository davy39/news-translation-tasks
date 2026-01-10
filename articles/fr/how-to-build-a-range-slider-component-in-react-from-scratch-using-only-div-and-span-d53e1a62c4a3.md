---
title: Comment créer un composant curseur de plage dans React à partir de zéro en
  utilisant uniquement <div> et <span>
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-08T21:41:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-range-slider-component-in-react-from-scratch-using-only-div-and-span-d53e1a62c4a3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iSkeoPHBQubtAL4fV4h9xQ.png
tags:
- name: components
  slug: components
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Comment créer un composant curseur de plage dans React à partir de zéro
  en utilisant uniquement <div> et <span>
seo_desc: 'By Rajesh Pillai

  In this article we will build a React range slider component step by step using
  only . We will enable it with touch support.

  What can you do with a piece of about 50 ?

  Build a slider control from scratch. If this sounds interesting, ...'
---

Par Rajesh Pillai

Dans cet article, nous allons créer un composant curseur de plage React étape par étape en utilisant uniquement <div>. Nous allons l'activer avec la prise en charge du tactile.

Que pouvez-vous faire avec environ 50 <div> ?

Créer un contrôle curseur à partir de zéro. Si cela vous semble intéressant, alors suivez le guide.

![Image](https://cdn-media-1.freecodecamp.org/images/QEwCv3lfVNUfQ1OBmNv06P0gCVvRiDwoyb2A)

Le résultat final ressemblera à l'animation ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/3doGzBVGEKKvAJHv-dl3PXsZ62GZ-wg3hlx7)

Veuillez noter que j'ai développé ce composant comme exercice pédagogique pour mes étudiants du cours [ReactJS — Beyond the Basics sur Udemy](https://www.udemy.com/reactjs-beyond-the-basics/?couponCode=MEDIUM_500), il peut donc avoir certains cas particuliers (que je corrigerai au fur et à mesure).

Vous pourriez utiliser un contrôle de plage HTML5 et le personnaliser. Mais je voulais adopter une approche différente et construire quelque chose à partir de zéro. Et le résultat est ce que vous voyez ici.

Notre composant curseur sera composé des trois éléments suivants :

* Une plage de curseur
* Les contrôles du curseur
* La plage de sélection actuelle

### Définition de l'état pour notre composant

Commençons par définir notre état. Je ne vous montre que la partie importante du code. Pour le code source complet, veuillez vous référer au lien à la fin de l'article.

```
state = {      slots: 24,      start: 0,      end: 10,      labelMode: "mid",   // mid, long}
```

L'état contient les propriétés suivantes.

* slots : Nombre total de slots à dessiner (dans ce cas, je l'utilise comme sélecteur de temps, donc il aura 24 slots horaires)
* start : La valeur de début de la sélection
* end : La valeur de fin de la sélection
* labelMode : Actuellement non utilisé. Mais peut être utilisé pour personnaliser le rendu des étiquettes de l'échelle.

### La partie return de la méthode render

Examinons maintenant la partie return de la méthode render. La méthode render() sera lentement composée de petits morceaux de fonctionnalités.

```
return (        <div>          <h2>React Slider</h2>          <div className="example-1">            <div className="slider-container">             <div className="slider-scale">                 {scale}              </div>              <div className="slider">                  {slider}              </div>              <div className="slider-selected-scale">                  {currentScale}              </div>            </div>          </div>        </div>);
```

Pour ceux qui lisent sur mobile, l'image ci-dessous peut être utile, car parfois Medium casse le formatage du code.

![Image](https://cdn-media-1.freecodecamp.org/images/fmu5JvCqMDyJ8VDtwyeNScNlgydLc7MZdqWV)

Si vous regardez le code, il y a seulement trois parties importantes :

* variable scale
* variable slider
* variable currentScale

Les trois variables ci-dessus seront responsables du rendu des parties correctes du curseur global.

### Dissection de la méthode render()

Initialisons quelques variables. Les JSX `scale`, `slider` et `currentScale` seront créés dans la boucle for définie ci-dessous.

```
render () { let scale = []; let slider=[]; let currentScale = []; let minThumb = null; let maxThumb = null
```

```
..... // reste du code }
```

#### Créer le JSX pour la variable 'scale'

Créer le JSX pour la variable scale est assez simple. Nous parcourons simplement la valeur des slots dans l'état et poussons un <div> dans le tableau scale avec la classe CSS requise pour le style.

La condition if garantit que nous n'imprimons l'étiquette que pour i = 0, i = 12 ou i = 24 (un peu comme une plage médiane). N'hésitez pas à personnaliser cela.

```
for (let i = 0; i <= this.state.slots;i++) {        let label = "";                if (i == 0 || i == 12 || i == 24) {          label = i;        }                scale.push(          <div             key={i}             className="slot-scale">            {label}          </div>        );
```

Voici le code en format image :

![Image](https://cdn-media-1.freecodecamp.org/images/ya7pdynXtp7ethqBzlALLU8zx57PghfpjfG7)

#### Créer le JSX pour la variable 'currentScale'

Continuons avec la même boucle for et créons le JSX 'currentScale'. Nous sommes toujours dans la même boucle for, donc environ 24 divs seront créés selon la valeur dans this.state.slots.

Le currentScale a une classe de 'slot-scale-selected'.

```
let currentLabel = "";        if (i === this.state.start || i === this.state.end) {   currentLabel = i;}        currentScale.push(   <div       key={i}       className="slot-scale-selected">            {currentLabel}    </div> );
```

![Image](https://cdn-media-1.freecodecamp.org/images/K8tMqK3APpa7vyi186bmW3Pze0ebX-9laxfv)

Le code est assez similaire au JSX 'scale' que nous avons créé.

#### Créer le JSX pour la variable 'slider'

Écrivons une fonction pour rendre le JSX 'slider'. Le curseur a besoin de deux pouces, un pour le minimum et un pour le maximum.

Initialisons d'abord la variable thumb en fonction de la valeur 'i'. Si 'i' est le même que this.state.start, alors nous définissons la variable minThumb. Sinon, si la valeur de 'i' est la même que this.state.end, alors nous initialisons la variable maxThumb.

```
if (i === this.state.start) {   minThumb = <this.MinSlider />} else if (i === this.state.end) {   maxThumb = <this.MaxSlider />} else {   minThumb = null;   maxThumb = null;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/dvDNWJiBE0qleprPJYPC6yQBhedxr0KRq8TY)

#### Créer le JSX pour le 'slider'

Le morceau de code important ici est l'événement dragover. Cela est nécessaire pour que le drop HTML fonctionne correctement.

```
let lineClass = "line";        if (i >= this.state.start && i < this.state.end) {   lineClass += " line-selected";}slider.push(   <div         data-slot={i}        onDragOver={this.onDragOver}         onTouchMove = {this.onDragOver}        onTouchEnd = {this.onDrop}        onDrop = {this.onDrop}        key={i}         className="slot">           <div  data-slot={i} className={lineClass}/>           <span className="scale-mark"></span>           {minThumb}           {maxThumb}    </div> );
```

![Image](https://cdn-media-1.freecodecamp.org/images/xOUMWRHUNkJZLc1HVq7ihuhjI4O32BLCsyeA)

La variable slider a besoin de deux morceaux de fonctionnalités supplémentaires pour représenter le pouce min et max sur le curseur.

Le JSX du slider a des gestionnaires d'événements supplémentaires pour gérer l'événement drop/touchend. Nous allons examiner les gestionnaires d'événements sous peu.

La classe 'lineClass' style/affiche la ligne sur le curseur, et la classe 'line-selected' style la plage actuellement sélectionnée.

Écrivons maintenant les fonctions MinSlider et MaxSlider en dehors de la méthode render.

#### La fonction MinSlider() pour rendre le pouce min

Examinons le code. Les props importantes sont les événements liés au glissement et l'attribut draggable. L'attribut draggable rendra cet élément glissable.

Nous ajoutons également le gestionnaire d'événements tactiles. Veuillez vous référer au lien en bas de l'article pour ajouter le polyfill de prise en charge tactile pour l'API HTML5.

```
MinSlider=()=> {  return (     <div data-slider="min"            onDragStart={this.onDragStart}            onTouchStart={this.onDragStart}           draggable className="slider-thumb slider-thumb-min">     </div>  );}
```

#### La fonction MaxSlider() pour rendre le pouce min

Le MaxSlider est presque le même que le MinSlider à l'exception des données et du className.

```
MaxSlider=()=> {  return (      <div data-slider="max"          onDragStart={this.onDragStart}           onTouchStart={this.onDragStart}        draggable className="slider-thumb slider-thumb-max">              </div>   );}
```

L'image du code est donnée ci-dessous pour référence.

![Image](https://cdn-media-1.freecodecamp.org/images/4vI2mOLaFiwUgpnUVe3zXD0vx3w4jbeOJB0o)

### Gestion des événements

Examinons maintenant les gestionnaires d'événements de glissement/tactile définis dans notre <div> pour contrôler le mouvement de l'élément curseur.

#### dragover :

L'événement dragover est nécessaire pour prendre en charge la zone de dépôt lors de l'utilisation de l'API de glissement/dépose HTML5. La seule chose que nous devons faire ici est d'invoquer preventDefault sur l'objet événement.

```
onDragOver = (e) => {    e.preventDefault();}
```

#### dragstart :

Le dragstart nous permet de stocker quel curseur est en cours de glissement. Veuillez noter que je n'utilise pas l'objet dataTransfer ici, mais simplement une variable d'instance pour stocker cela.

```
onDragStart = (e) => {   let slider  = e.target.dataset.slider;   this.sliderType = slider;}
```

La valeur de e.target.dataset.slider est soit « min » soit « max », indiquant quel curseur est en cours de glissement.

#### ondrop :

L'événement ondrop capture où le pouce est déposé (sur quelle échelle).

Voici le flux important dans l'événement ondrop :

* Récupérer la source (si le pouce min/max)
* Obtenir le slot (où le dépôt se produit)
* Validations
* Mettre à jour le slot (dans l'état)
* Réinitialiser le sliderType.

```
onDrop = (e, target) => {      let source = this.sliderType;      let slot = Number(e.target.dataset.slot);           if (isNaN(slot)) return;            if (source === "min") {        if (slot >= this.state.end) return;        this.setState({          start: slot        },()=>{          console.log(this.state);        })      } else if (source === "max") {        if (slot <= this.state.start) return;        this.setState({          end: slot        },()=>{          console.log(this.state);        })      }     this.sliderType = null;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/13wMILHS9heXZUOf5pegbiq34G2o6Gom1onc)

#### Le code source complet/et la démonstration peuvent être vus ici [http://jsbin.com/remodat/edit?output](https://jsbin.com/remodat/edit?js,console)

Puisque j'utilise les fonctionnalités de glissement et de dépôt HTML5 pour ajouter la prise en charge tactile, veuillez ajouter cette référence de polyfill à votre fichier html.

[**Bernardo-Castilho/dragdroptouch**](https://github.com/Bernardo-Castilho/dragdroptouch/blob/master/DragDropTouch.js)  
[_dragdroptouch - Polyfill qui active la prise en charge du glissement-dépose HTML5 sur les appareils mobiles (tactiles)._github.com](https://github.com/Bernardo-Castilho/dragdroptouch/blob/master/DragDropTouch.js)

### Todos

* Extraire la logique vers une classe de composant séparée
* Tester et ajouter la personnalisation.

### Historique

* 21-Mai-2018 — Première version

P.S : Ce composant est le résultat d'une tentative de codage très rapide. Cela sera refactorisé.

**Promotion** : Si vous souhaitez soutenir notre programme open source [Maîtriser l'ingénierie Full Stack en 12 à 20 semaines](https://codeburst.io/mastering-front-end-engineering-in-12-to-20-weeks-for-beginners-and-experienced-alike-6dc5172e3295), voici un coupon spécial de 10 $ pour les lecteurs de Medium pour mon prochain cours en direct [ReactJS-Beyond the basics](https://www.udemy.com/reactjs-beyond-the-basics/?couponCode=MEDIUM_500) sur Udemy (MEDIUM_500 est le code de coupon, qui est déjà marqué dans l'URL ci-dessus)