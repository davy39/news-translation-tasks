---
title: Tutoriel sur l'API Giphy – Comment générer des GIFs de texte animé avec ReactJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-26T21:44:01.000Z'
originalURL: https://freecodecamp.org/news/giphy-api-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/giphy-API-tutorial.png
tags:
- name: api
  slug: api
- name: CSS
  slug: css
- name: frontend
  slug: frontend
- name: gif
  slug: gif
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Tutoriel sur l'API Giphy – Comment générer des GIFs de texte animé avec
  ReactJS
seo_desc: 'By Charles M.

  In this tutorial you will create an app that generates dynamic animated text using
  Giphy''s API with ReactJS.

  After that I''ll go over some of the other API features Giphy provides that you
  can use to make other interesting projects.

  You ...'
---

Par Charles M.

Dans ce tutoriel, vous allez créer une application qui génère du texte animé dynamique en utilisant l'API de Giphy avec ReactJS.

Ensuite, je passerai en revue certaines des autres fonctionnalités de l'API que Giphy propose et que vous pouvez utiliser pour réaliser d'autres projets intéressants.

Vous pouvez trouver [le code du tutoriel ici](https://github.com/renaissanceengineer/reactjs-giphy-api-tutorial).

## Tutoriel Vidéo

Pour voir un aperçu du produit final en action, vous pouvez regarder le début de cette vidéo. Si vous préférez suivre un tutoriel vidéo plutôt que de lire (ou en plus de la lecture), vous pouvez également suivre le reste de la vidéo.

%[https://www.youtube.com/watch?v=H8JpzxRoS18]

## Introduction

Pour commencer, vous aurez besoin d'un environnement de développement de base pour ReactJS. J'utiliserai create-react-app comme modèle de projet de départ.

Ensuite, vous devrez visiter la [page des développeurs de Giphy](https://developers.giphy.com) et créer un compte pour obtenir votre clé API. Une fois que vous avez créé votre compte, vous verrez un tableau de bord comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/giphy-dashboard.PNG)

Vous devez cliquer sur "créer une App" et choisir l'option SDK pour votre application. Votre tableau de bord vous présentera alors une clé API que vous utiliserez pour faire des appels à l'API Giphy.

### Comment configurer le fichier et le dossier de l'application

La structure de ce tutoriel sera standard pour les projets ReactJS. À l'intérieur du répertoire `src`, créez un répertoire `components` et créez deux fichiers, `Error.js` et `TextList.js`.

Vous devez également créer un fichier `.env` à la racine du projet que vous utiliserez pour stocker votre clé API. Quel que soit le nom que vous donnez à votre variable, vous devez ajouter REACT_APP devant, comme ceci :

`REACT_APP_GIPHY_KEY=apikeyhere`

### Installer Giphy JS-fetch

La dernière chose que vous devez faire est d'installer la bibliothèque d'assistance de l'API Giphy, que vous pouvez faire en utilisant la commande suivante :

`npm install @giphy/js-fetch-api`

## Appel à l'API Giphy

La première tâche pour créer cette application consiste à créer un formulaire d'entrée pour accepter le texte que vous souhaitez générer à partir de l'API Giphy. Vous utiliserez ensuite cette entrée de texte et l'enverrez comme une requête API.

Avant d'afficher ces données de réponse, testons-les simplement en faisant la requête API puis en enregistrant la réponse. Écrivez le code suivant dans votre fichier `App.js` :

```js
import { GiphyFetch } from '@giphy/js-fetch-api'
import {useState} from 'react'
import TextList from './components/TextList'
import Error from './components/Error'
import './App.css';

const giphy = new GiphyFetch(process.env.REACT_APP_GIPHY_KEY)

function App() {
  const [text, setText] = useState('')
  const [results, setResults] = useState([])
  const [err, setErr] = useState(false)

  const handleInput = (e) => {
    setText(e.target.value)
  }

  const handleSubmit = (e) => {
    if(text.length === 0) {
      
      //définir l'état d'erreur sur vrai
      setErr(true)
      return
    }

    console.log(text)

    const apiCall = async () => {
      const res = await giphy.animate(text, {limit: 20})
      console.log(res.data)
      setResults(res.data)
    }
    
    apiCall()
    setText('')
    setErr(false)

  }
  
  return (
    <div className="App">
      <h1>Générateur de texte animé</h1>
      <h3>Tapez du texte dans le formulaire et cliquez sur soumettre</h3>
      <input className='input-field' value={text} onChange={handleInput} />
      <button className='submit-btn' onClick={handleSubmit}>Soumettre</button>
    </div>
  );
}
export default App;
```

Examinons ce qui se passe dans ce code :

`const giphy = new GiphyFetch(process.env.REACT_APP_GIPHY_KEY)` est l'endroit où vous utilisez la bibliothèque d'assistance Giphy pour créer l'objet que vous utiliserez pour interagir avec l'API Giphy.

`process.env.REACT_APP_GIPHY_KEY` est la manière dont votre clé API est passée en argument depuis le fichier `.env`. Vous pouvez également passer votre clé API sous forme de chaîne, mais vous ne voudrez pas faire cela en production car quelqu'un pourrait voler et utiliser votre clé.

À l'intérieur du composant principal App, vous créez trois morceaux d'état en utilisant des hooks. Le premier est `text` qui stockera l'entrée de l'utilisateur. C'est ce qui sera passé à l'API comme argument pour générer du texte.

`err` sera utilisé pour rendre conditionnellement une erreur plus tard si l'utilisateur tente de soumettre une chaîne vide.

Et `results` est un tableau vide qui sera utilisé pour stocker les résultats de la réponse de l'API.

Si vous exécutez le code et vérifiez votre console de développeur, vous devriez voir que l'API Giphy a retourné un tableau avec 20 objets.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/console-results.PNG)

## Comment afficher les données avec React

Maintenant que les données sont correctement stockées dans l'état, tout ce que vous avez à faire est d'afficher ces données avec JSX. Pour gérer cela, nous allons terminer ces deux composants que nous avons créés précédemment.

Tout d'abord, nous allons créer un simple composant d'erreur qui peut afficher un message personnalisé. Placez le code suivant dans `Error.js` à l'intérieur de votre dossier components :

```js
const Error = (props) => {
    if(!props.isError) {
        return null
    }

    return (
        <p className='error'>{props.text}</p>
    )
}

export default Error
```

Le composant `Error` est très simple. Il prend l'état `err` et une chaîne de texte comme props, et si la valeur est vraie, il rendra le texte. Si `err` est faux, il retourne null.

Ensuite, le composant TextList qui prendra l'état `results` comme props et affichera les données dans votre application :

```js
const TextList = (props) => {
  const items = props.gifs.map((itemData) => {
    return <Item url={itemData.url} />;
  });
  return <div className="text-container">{items}</div>;
};
const Item = (props) => {
  return (
    <div className="gif-item">
      <img src={props.url} />
    </div>
  );
};
export default TextList;
```

Ce composant est un peu plus compliqué, voici ce qui se passe :

Le composant `Item` accepte la valeur URL qui se trouve dans chaque valeur retournée par l'API. Il utilise cette URL comme source pour l'élément image.

Le tableau d'état `results` du composant App est passé au composant TextList en tant que `gifs`. Le tableau est mappé pour générer tous les composants `Item` pour tous les résultats et assigné à la variable `items` puis retourné à l'intérieur d'une div conteneur. Nous styliserons ce conteneur plus tard pour créer une mise en page de grille.

### Comment importer les composants dans l'application principale

Maintenant, vous devez simplement utiliser ces composants terminés dans votre JSX. Le code final de votre fichier `App.js` devrait ressembler à ceci :

```js
import TextList from './components/TextList'
import Error from './components/Error'
import { GiphyFetch } from '@giphy/js-fetch-api'
import {useState} from 'react'
import './App.css';

const giphy = new GiphyFetch(process.env.REACT_APP_GIPHY_KEY)

function App() {
  const [text, setText] = useState('')
  const [results, setResults] = useState([])
  const [err, setErr] = useState(false)

  const handleInput = (e) => {
    setText(e.target.value)
  }

  const handleSubmit = (e) => {
    if(text.length === 0) {
      
      //définir l'état d'erreur sur vrai
      setErr(true)
      return
    }

    console.log(text)

    const apiCall = async () => {
      const res = await giphy.animate(text, {limit: 20})
      
      setResults(res.data)
    }
    
    apiCall()
    //changer l'état d'erreur en faux
    setText('')
    setErr(false)

  }
  
  return (
    <div className="App">
      <h1>Générateur de texte animé</h1>
      <h3>Tapez du texte dans le formulaire et cliquez sur soumettre</h3>
      <input className='input-field' value={text} onChange={handleInput} />
      <button className='submit-btn' onClick={handleSubmit}>Soumettre</button>
      <Error isError={err} text='besoin d\'une longueur supérieure à 0 pour l\'entrée'/>
      {results && <TextList gifs={results}  />}
    </div>
  );
}
export default App;
```

Les seuls changements ici sont les deux dernières lignes ajoutées dans l'instruction return :

Le composant `Error` reçoit l'état `err` et une prop `text` qui ne sera rendue que si une erreur se produit.

Dans cette application, il n'y a qu'une seule condition d'erreur au cas où l'entrée est vide, mais vous pourriez ajouter des vérifications supplémentaires avec des messages d'erreur personnalisés également.

Ensuite, nous utilisons le rendu conditionnel avec l'opérateur logique `&&`. Cela fait que le composant `TextList` ne se rend que si le tableau des résultats n'est pas vide, ce qui signifie que la réponse de l'API est revenue avec succès avec nos gifs.

Si vous exécutez votre code à ce stade, vous devriez voir une application fonctionnelle mais peu esthétique. Si vous utilisez le champ d'entrée et cliquez sur le bouton de soumission, les gifs devraient être retournés et affichés dans votre application.

## Comment ajouter du style avec CSS

La dernière chose à faire est de rendre l'application un peu plus joli. N'hésitez pas à personnaliser l'un de ces styles si vous souhaitez ajuster l'apparence des choses. Placez ce code dans votre fichier `App.css` :

```css
.App {
  text-align: center;
}

.error {
  color: #b50000;
  font-size: 20px;
  font-weight: 500;
}


.input-field {
  font-size: 20px;
  vertical-align: middle;
  transition: .5s;
  border-width: 2px;
  margin: 5px;
}

.input-field:focus {
  box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
  outline: none;
}

.input-field:hover {
  box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
  
}

.submit-btn {
  background-color: rgb(19, 209, 235);
  color: #fff;
  padding: 6px 30px;
  vertical-align: middle;
  outline: none;
  border: none;
  font-size: 16px;
  transition: .3s;
  cursor: pointer;
}

.submit-btn:hover {
  background-color: rgb(10, 130, 146);
}

.text-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.gif-item {
  flex-basis: 19%;
}

img {
  max-width: 100%;
}

@media screen and (max-width: 992px) {
  .gif-item {
    flex-basis: 31%;
  }
}

@media screen and (max-width: 600px) {
  .gif-item {
    flex-basis: 48%;
  }
}

```

Rien de fou avec le CSS. Juste un peu de style pour le bouton de soumission et une ombre de boîte pour le champ d'entrée.

Il y a aussi quelques requêtes média pour un design réactif qui change le nombre de colonnes en fonction de la taille de l'écran.

## Autres fonctionnalités de l'API Giphy

L'API de texte animé n'est qu'une des fonctionnalités disponibles dans l'API Giphy. Je vais passer en revue quelques autres fonctionnalités qui pourraient être utiles dans le cadre d'un projet ou comme projet solo.

### Emoji animé

Le point de terminaison Emoji est très simple en termes d'utilisation. Il retourne une série d'emojis animés, tout comme l'API de texte animé que vous avez utilisée ci-dessus, sauf que vous n'avez pas besoin de lui passer d'arguments. Un exemple d'appel API :

`const data = await gf.emoji()`

Ce point de terminaison pourrait être utile si vous construisez une application de chat et que vous souhaitez faciliter l'utilisation des emojis dans les messages des utilisateurs.

### Composants d'interface utilisateur pré-construits

Si vous n'avez pas envie de vous amuser avec une tonne de code personnalisé comme nous l'avons fait dans ce tutoriel, Giphy propose en fait des composants pour ReactJS et JavaScript régulier.

Vous pouvez créer une grille très similaire à celle que nous avons créée dans ce tutoriel avec seulement quelques lignes de code :

```js
import { Grid } from '@giphy/react-components'
import { GiphyFetch } from '@giphy/js-fetch-api'

// utilisez @giphy/js-fetch-api pour récupérer des gifs
// demandez une nouvelle clé Web SDK. Utilisez une clé séparée pour chaque plateforme (Android, iOS, Web)
const gf = new GiphyFetch('votre clé Web SDK')

// récupérez 10 gifs à la fois lorsque l'utilisateur fait défiler (le décalage est géré par la grille)
const fetchGifs = (offset: number) => gf.trending({ offset, limit: 10 })

// Composant React
ReactDOM.render(<Grid width={800} columns={3} gutter={6} fetchGifs={fetchGifs} />, target)
```

Vous obtenez quelques fonctionnalités bonus supplémentaires comme des mises à jour dynamiques automatiques pour récupérer plus de contenu lorsque les utilisateurs font défiler jusqu'en bas de la grille.

Vous pouvez choisir entre des modèles qui gèrent presque tout ou simplement un composant Grid qui vous donne un peu plus de contrôle.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/giphy-ui-kits.PNG)

Voici une [démo interactive](https://codesandbox.io/s/giphyreact-components-hbmcf?from-embed) fournie par Giphy.

### API des tendances

Ce point de terminaison retourne une liste de contenu constamment mis à jour basé sur l'engagement des utilisateurs et ce qui est actuellement populaire sur Giphy.

### API de recherche

Ce point de terminaison est similaire au point de terminaison de texte animé, vous devez simplement passer une requête de recherche comme paramètre et vous obtiendrez un tableau de gifs qui correspondent.

Il existe de nombreux autres points de terminaison d'API disponibles. Vous pouvez voir le reste dans la [documentation de l'API de Giphy](https://developers.giphy.com/docs/api/endpoint).

## Conclusion

C'est tout pour ce tutoriel ! J'espère que vous l'avez trouvé intéressant et que vous réaliserez des projets sympas en utilisant l'API Giphy.

Si vous êtes intéressé par un tas d'autres API cool que vous pouvez utiliser pour réaliser des projets de portfolio, vous pouvez également regarder cette vidéo qui passe en revue 8 autres API que je trouve vraiment cool.

%[https://youtu.be/3ZRBDIA8C6E]