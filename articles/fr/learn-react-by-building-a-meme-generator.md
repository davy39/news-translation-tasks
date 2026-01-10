---
title: Apprendre React en créant un générateur de memes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-23T18:29:43.000Z'
originalURL: https://freecodecamp.org/news/learn-react-by-building-a-meme-generator
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/o60oxupyz8cfce0cknvz.png
tags:
- name: projects
  slug: projects
- name: React
  slug: reactjs
- name: Tutorial
  slug: tutorial
seo_title: Apprendre React en créant un générateur de memes
seo_desc: 'By Bob Ziroll

  Memes are great - they''re such a fun way of describing ideas and opinions. So it''s
  no coincidence that I picked a meme generator app as the capstone project in my
  free React course on Scrimba. The app works by pulling a random meme imag...'
---

Par Bob Ziroll

Les memes sont géniaux - ils sont une façon si amusante de décrire des idées et des opinions. Il n'est donc pas surprenant que j'aie choisi une application de générateur de memes comme projet final de mon [cours gratuit sur React](https://scrimba.com/g/glearnreact) sur Scrimba. L'application fonctionne en tirant une image de meme aléatoire d'une API et en plaçant votre texte par-dessus pour créer votre propre meme personnalisé. 

Dans cet article, je vais donc vous donner un guide étape par étape pour créer l'application. Si vous êtes un jour confus, vous pouvez également suivre ces étapes dans le cours Scrimba, en commençant par [cette conférence](https://scrimba.com/p/p7P5Hd/c6K77um). 

Et si vous aimez mon style d'enseignement et êtes d'humeur pour un défi plus difficile après avoir terminé ce tutoriel, veuillez consulter [mon prochain cours avancé](https://scrimba.com/g/greact) sur Scrimba.

> Note : Vous devriez déjà être assez familier avec certains des concepts fondamentaux de React, comme les composants, l'état, les props et les méthodes de cycle de vie. De plus, ce tutoriel n'utilise pas les Hooks, mais dans mon prochain cours, nous couvrirons les Hooks en profondeur et nous aurons beaucoup de pratique à les utiliser.

## 1. Création du code de base et rendu d'un composant App

![Création de la tâche de code de base](https://miro.medium.com/max/1396/1*Sigh_tXDKPjQpBlWsvj1lQ.png)

La première chose que nous devons faire est de créer le code de base pour l'application. Pour ce faire, nous importons `React` et `ReactDOM` et utilisons `ReactDOM` pour rendre un composant appelé `App`, que nous créerons plus tard. Nous plaçons ensuite le composant `App` à la 'racine'. Nous importons également `App` depuis son fichier `"./App"`, que nous créerons bientôt.

```js
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));
```

Nous créons ensuite notre fichier `App.js`. Dans celui-ci, nous créons un composant fonctionnel appelé `App` qui, pour l'instant, retourne un simple `<h1>`. Nous l'exportons ensuite. Le `<h1>` nous permet de vérifier que l'application s'affiche correctement à l'écran.

```js
import React from 'react';
function App() {
  return <h1>Bonjour le monde !</h1>;
}
export default App;
```

Le résultat obtenu est le suivant :
![Bonjour le monde rendu](https://miro.medium.com/max/1686/1*nQjf71dDnfwHqoT3Pw4tag.png)

## 2. Création des composants Header et MemeGenerator

![Création des composants Header et MemeGenerator](https://miro.medium.com/max/1196/1*QZ7p26lRlGRepBrT4i8r3Q.png)

Ensuite, nous créons les composants Header et MemeGenerator. Le Header n'affichera que des éléments, tandis que MemeGenerator appellera l'API et conservera les données dans l'état.

Commençons par créer le fichier `Header.js`. Puisque Header est un composant utilisé uniquement pour l'affichage, il doit être un composant fonctionnel. Pour l'instant, le composant doit retourner un simple `<h1>`. Après l'avoir créé, nous exportons Header.

```js
import React from 'react';
function Header() {
  return <h1>EN-TÊTE</h1>;
}
export default Header;
```

Ensuite, nous créons le fichier `MemeGenerator.js`. Comme le composant `MemeGenerator` contiendra des données et effectuera des appels à une API, il doit être un composant de classe. Nous devons toujours importer React, et comme il s'agira d'un composant de classe, nous importerons également `Component` (qui est une [importation nommée](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import#Import_a_single_export_from_a_module)).

MemeGenerator a besoin d'un `constructor()` qui appelle `super()` et, comme il contiendra un état, nous ajoutons un état vide pour l'instant. Comme dans le composant Header, nous rendons un simple `<h1>` pour commencer. Nous exportons ensuite MemeGenerator.

```js
import React, { Component } from 'react';
class MemeGenerator extends Component {
  constructor() {
    super();
    this.state = {}; // état vide
  }
  render() {
    return <h1>SECTION GÉNÉRATEUR DE MEMES</h1>;
  }
}
export default MemeGenerator;
```

Maintenant, nous importons Header et MemeGenerator dans `App.js` et créons une instance de chacun dans notre composant App. Pour afficher correctement les composants, nous les enveloppons dans une `<div>`.

```js
import React from 'react';
import Header from './Header';
import MemeGenerator from './MemeGenerator';
function App() {
  return (
    <div>
      <Header />
      <MemeGenerator />
    </div>
  );
}
export default App;
```

## 3. Compléter le composant Header.

Pour compléter le composant `<Header>`, nous ajoutons une image de trollface en insérant une balise `<img>` et en définissant la source sur l'URL de l'image. Nous ajoutons ensuite une balise `<p>` avec le nom de notre application et nous les enveloppons dans la balise sémantique HTML5 `<header>`.

```js
function Header() {
  return (
    <header>
      <img
        src='http://www.pngall.com/wp-content/uploads/2016/05/Trollface.png'
        alt='Problème ?'
      />
      <p>Générateur de Mèmes</p>
    </header>
  );
}
```

Comme le style est hors du cadre de ce cours, les styles CSS ont déjà été créés et appliqués à la balise `<header>`. Le résultat est le suivant :

![En-tête rendu](https://miro.medium.com/max/1142/1*tQ0B2usG9sXABiSHaSeXOQ.png)

Cela dit, les apprenants peuvent toujours jouer avec le style et perfectionner leurs compétences CSS par eux-mêmes. Avec le `<Header/>` maintenant complet, le reste du défi se déroulera dans `<MemeGenerator/>`

## 4. Initialisation de l'état

![Tâche d'initialisation de l'état](https://miro.medium.com/max/1394/1*-rcc61OqQ7n3qtCS8gcjLg.png)

Nous devons maintenant initialiser l'état afin qu'il sauvegarde un texte supérieur, un texte inférieur et une image aléatoire, qui est déjà fournie.

Pour ce faire, nous construisons l'objet vide que nous avons placé dans `<MemeGenerator/>` lorsque nous l'avons initialement construit. Nous initialisons `topText` et `bottomText` comme des chaînes vides et `randomImg` comme l'URL fournie.

```js
class MemeGenerator extends Component {
  constructor() {
    super();
    this.state = {
      topText: '',
      bottomText: '',
      randomImg: 'http://i.imgflip.com/1bij.jpg'
    };
  }
}
```

## 5. Effectuer l'appel à l'API

![Tâche d'appel à l'API](https://miro.medium.com/max/1448/1*1fSA7JfSJxQ0RnnreAH1ww.png)

Ensuite, nous effectuons un appel à l'API vers l'URL fournie et sauvegardons les données retournées (qui est un tableau trouvé dans `response.data.memes`) dans une nouvelle propriété d'état appelée `allMemeImgs`.
Lorsque nous devons charger des données à partir d'un endpoint pour les utiliser dans notre composant, un bon endroit pour faire la demande est la méthode de cycle de vie `componentDidMount()`. Dès que le composant est monté, nous utilisons la fonction native `fetch()` pour appeler l'URL fournie.

```js
componentDidMount() {
  fetch("https://api.imgflip.com/get_memes")
}
```

Cela retourne une promesse que nous transformons en un objet Javascript avec la méthode `.json()`.

```js
componentDidMount() {
  fetch("https://api.imgflip.com/get_memes")
    .then(response => response.json())
}
```

Ensuite, nous obtenons la réponse qui nous est utile en extrayant le tableau des memes de `response.data`.

```js
componentDidMount() {
fetch("https://api.imgflip.com/get_memes")
  .then(response => response.json())
  .then(response => {
  const { memes } = response.data
  })
}
```

Maintenant, nous sauvegardons les résultats dans une nouvelle propriété d'état appelée `allMemeImgs`. Pour ce faire, nous initialisons `allMemeImgs` comme un tableau vide.

```js
this.state = {
  topText: '',
  bottomText: '',
  randomImg: 'http://i.imgflip.com/1bij.jpg',
  allMemeImgs: []
};
```

Maintenant, de retour dans `componentDidMount()`, nous définissons l'état. Comme nous ne nous intéressons pas à ce qu'était l'état précédent, nous définissons `allMemeImgs` sur memes.

```js
componentDidMount() {
  fetch("https://api.imgflip.com/get_memes")
    .then(response => response.json())
    .then(response => {
  const { memes } = response.data
  this.setState({ allMemeImgs: memes })
  })
}
```

Pour nous assurer que cela fonctionne, nous utilisons `console.log` pour afficher le premier élément, qui ressemble à ceci :

![Sortie de console.log](https://miro.medium.com/max/1844/1*_Pn6VWqZsUFKMhbjVsAx-A.png)

Voici un aperçu de l'ensemble de la fonction `componentDidMount()`.

```js
componentDidMount() { // s'assurer que les données sont récupérées au début
  fetch("https://api.imgflip.com/get_memes") // appel à l'URL
    .then(response => response.json()) // transformer la promesse en objet JS
    .then(response => {
  const { memes } = response.data // extraire le tableau des memes de response.data
  console.log(memes[0]) // vérifier que les données sont présentes
  this.setState({ allMemeImgs: memes }) // définir l'état allMemeImgs
})
}
```

## 6. Création du formulaire de saisie

Nous voulons maintenant créer un formulaire qui permettra éventuellement à l'utilisateur de saisir les textes supérieur et inférieur. Nous le faisons avec une balise HTML `<form>` et un simple `<button>` qui dit 'Gen'. Nous le stylisons avec le CSS pré-fournis.

```js
render() {
  return (
    <div>
      <form className="meme-form">
        <button>Gen</button>
      </form>
    </div>
  )
}
```

![Bouton Gen rendu](https://miro.medium.com/max/1008/1*ruWrn2bd-PiHLu4T3sYMBg.png)

## 7. Ajout de champs de saisie au formulaire

![Tâche d'ajout de champs de saisie](https://miro.medium.com/max/1672/1*hJOUoYcmSIv6bV-eHH5m_w.png)

Ensuite, nous devons ajouter les deux champs de saisie (un pour le texte supérieur et un pour le texte inférieur). Le formulaire doit être un formulaire contrôlé, nous devons donc ajouter tous les attributs nécessaires pour que cela fonctionne. Nous créerons le gestionnaire `onChange` plus tard.

Nous créons deux champs de saisie qui ont tous deux le type `text` et des attributs de nom appropriés (`topText` et `bottomText`). Au lieu d'utiliser des étiquettes, nous utilisons des placeholders : 'Texte supérieur' et 'Texte inférieur'.

Enfin, pour faire de ceci un [formulaire contrôlé](https://reactjs.org/docs/forms.html#controlled-components), nous définissons la valeur comme étant égale à la valeur actuelle dans `state` avec `{this.state.topText}` et `{this.state.bottomText}`.

```js
render() {
  return (
    <div>
      <form className="meme-form">
        <input
          type="text"
          name="topText"
          placeholder="Texte supérieur"
          value={this.state.topText}
        />
        <input
          type="text"
          name="bottomText"
          placeholder="Texte inférieur"
          value={this.state.bottomText}
        />
        <button>Gen</button>
      </form>
    </div>
  )
}
```

## 8. Création du gestionnaire onChange.

![Tâche de création du gestionnaire onChange](https://miro.medium.com/max/1430/1*AO9cOxV8fnVCXxTyjQCPvw.png)

Maintenant, nous créons le gestionnaire onChange, qui mettra à jour l'état correspondant à chaque changement du champ de saisie.

Tout d'abord, nous créons une fonction `handleChange()` qui reçoit un événement.

```js
handleChange(event) {

}
```

Maintenant, nous définissons le `onChange` des deux champs de saisie pour qu'il soit égal à `handleChange`.

```js
<form className='meme-form'>
  <input
    type='text'
    name='topText'
    placeholder='Texte supérieur'
    value={this.state.topText}
    onChange={this.handleChange}
  />
  <input
    type='text'
    name='bottomText'
    placeholder='Texte inférieur'
    value={this.state.bottomText}
    onChange={this.handleChange}
  />
  <button>Gen</button>
</form>
```

Nous devons nous souvenir de lier la méthode dans le constructeur — un piège courant pour les développeurs React.

```js
constructor() {
  super()
  this.state = {
    topText: "",
    bottomText: "",
    randomImg: "http://i.imgflip.com/1bij.jpg",
    allMemeImgs: []
  }
  this.handleChange = this.handleChange.bind(this)
}
```

Pour tester la nouvelle fonction `handleChange()`, nous ajoutons un simple `console.log` :

```js
handleChange(event) {
  console.log("Ça marche !")
}
```

Si elle est correctement déclenchée, vous verrez quelque chose comme ceci :
![console.log("Ça marche !") rendu](https://miro.medium.com/max/308/1*wGS5bSipqBwpoqKqeC6dVg.png)

Maintenant, pour remplir la fonction `handleChange()`. Pour ce faire, nous voulons extraire les propriétés name et value de event.target afin de pouvoir obtenir le nom de l'état que nous devons mettre à jour (`topText` ou `bottomText`) et la valeur qui est tapée dans la boîte.

```js
handleChange(event) {
  const { name, value } = event.target
}
```

Nous allons maintenant utiliser ceux-ci pour mettre à jour l'état. Comme nous ne nous intéressons pas à ce qu'était l'état précédent, nous pouvons simplement fournir un objet dans lequel nous définissons le `[name]` à la valeur tapée dans le champ de saisie.

```js
handleChange(event) {
const {name, value} = event.target
this.setState({ [name]: value })
}
```

## 9. Affichage d'une image de meme avec les textes supérieur et inférieur

Nous voulons maintenant que l'application affiche une image de meme avec les textes supérieur et inférieur. Nous insérons une balise `<img>` sous le `<form>` et définissons `randomImg`, que nous avons initialisé comme source en utilisant `src={this.state.randomImg}`. Nous ajoutons ensuite deux balises `<h2>` qui affichent le texte correspondant qui est également sauvegardé dans l'état. Tout cela est enveloppé dans une `div` et stylisé avec la classe `meme` pré-fournie.

```js
<div className='meme'>
  <img src={this.state.randomImg} alt='' />
  <h2 className='top'>{this.state.topText}</h2>
  <h2 className='bottom'>{this.state.bottomText}</h2>
</div>
```

Nous pouvons maintenant tester l'application en tapant dans les zones de texte. Comme l'état est correctement défini à chaque frappe, le texte affiché sur l'image change chaque fois que nous tapons.

![Exemple rendu des progrès jusqu'à présent](https://miro.medium.com/max/1014/1*avFJ4IjRQZhrN4gdrZHa8g.png)

## 10. Affichage d'une image de meme aléatoire avec les textes supérieur et inférieur

![Tâche d'affichage d'une image de meme aléatoire](https://miro.medium.com/max/1570/1*xTuNOCWGvQV1sVuw0tgpzQ.png)

Maintenant, nous devons créer une méthode qui affiche une image de meme qu'elle choisit aléatoirement dans notre tableau `allMemeImgs` lorsque le bouton `Gen` est cliqué. La propriété de l'image choisie dans le tableau est `.url`.
Nous pouvons décomposer cette tâche en parties plus petites.

Tout d'abord, nous définissons le `onSubmit` du formulaire pour qu'il soit égal au nom de notre nouvelle méthode, que nous appellerons `handleSubmit()`.

`<form className="meme-form" onSubmit={this.handleSubmit}>`

Nous créons maintenant la fonction `handleSubmit()` au-dessus de la fonction `render()`. Nous devons empêcher le comportement par défaut de l'événement, sinon, la méthode essaiera de rafraîchir la page.

```js
handleSubmit(event) {
  event.preventDefault()
}
```

Nous devons également lier `handleSubmit()` dans notre `constructor()`.

```js
constructor() {
  super()
  this.state = {
    topText: "",
    bottomText: "",
    randomImg: "http://i.imgflip.com/1bij.jpg",
    allMemeImgs: []
  }
  this.handleChange = this.handleChange.bind(this)
  this.handleSubmit = this.handleSubmit.bind(this)
}
```

Maintenant, nous devons obtenir un nombre aléatoire, obtenir le meme de cet index et définir `randomImg` sur l'`.url` de l'élément aléatoire.

```js
handleSubmit(event) {
  event.preventDefault()
  // obtenir un entier aléatoire (index dans le tableau)
  // obtenir le meme de cet index
  // définir `randomImg` sur l'`.url` de l'élément aléatoire que j'ai obtenu
}
```

Pour obtenir un nombre aléatoire, nous utilisons `Math.floor(Math.random)`. Pour nous assurer qu'il s'agit de l'un des index de notre tableau `allMemeImgs`, nous multiplions par la longueur du tableau.

```js
const randNum = Math.floor(Math.random() * this.state.allMemeImgs.length);
```

Nous définissons maintenant `randMemeImg` pour qu'il soit égal à `allMemeImgs`, avec l'index de `allMemeImgs` comme étant le `randNum` que nous venons d'obtenir. Nous ajoutons ensuite `.url` à la fin.

```js
const randMemeImg = this.state.allMemeImgs[randNum].url;
```

Maintenant, tout ce que nous avons à faire est de mettre à jour l'état en mettant à jour la propriété randomImg avec `randMemeImg`.

```js
this.setState({ randomImg: randMemeImg });
```

Notre fonction `handleSubmit()` complète ressemble à ceci :

```js
handleSubmit(event) {
  event.preventDefault()
  const randNum = Math.floor(Math.random() * this.state.allMemeImgs.length)
  const randMemeImg = this.state.allMemeImgs[randNum].url
  this.setState({ randomImg: randMemeImg })
}
```

## Générateur de Mèmes Complété

![Application Fonctionnelle](https://miro.medium.com/max/1008/1*ysbU1jxRIcNYCeZmhBdN6g.png)

Nous avons maintenant terminé l'application de générateur de memes, et nous obtenons une image différente à chaque fois que nous cliquons sur le bouton `Gen`, qui est ensuite superposée avec le texte que nous avons saisi.

Pour approfondir notre apprentissage, nous pourrions jouer avec le code et voir si nous pouvons l'améliorer, ou essayer d'obtenir des images d'une API différente. Pour une pratique vraiment intensive, nous pourrions même supprimer tout le code et essayer de le reconstruire à partir de zéro.

Félicitations pour avoir suivi le tutoriel et appris toutes les compétences utilisées dans ce projet.

Et si vous êtes prêt pour cela, consultez mon prochain [cours avancé](https://scrimba.com/g/greact), car il vous mènera à un niveau professionnel en React !