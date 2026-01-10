---
title: Comment créer un tableau de bord personnalisé avec les API WordPress et React
subtitle: ''
author: Marco Venturi
co_authors: []
series: null
date: '2022-02-18T15:59:20.000Z'
originalURL: https://freecodecamp.org/news/build-a-custom-dashboard-with-wordpress-apis-and-react
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/stephen-dawson-qwtCeJ5cLYs-unsplash.jpg
tags:
- name: React
  slug: react
- name: WordPress
  slug: wordpress
seo_title: Comment créer un tableau de bord personnalisé avec les API WordPress et
  React
seo_desc: "When you manage websites, it is all about data: views, response time, users,\
  \ bounce rate, and so on. And, if you manage websites, you've likely had to deal\
  \ with a WordPress instance at least once. \nThere are hundreds – or maybe thousands\
  \ – of WordPre..."
---

Lorsque vous gérez des sites web, tout est une question de données : vues, temps de réponse, utilisateurs, taux de rebond, etc. Et, si vous gérez des sites web, vous avez probablement dû traiter avec une instance WordPress au moins une fois. 

Il existe des centaines - voire des milliers - de plugins WordPress pour récupérer et afficher des données. Mais les API WordPress peuvent nous donner un coup de main si nous voulons construire un tableau de bord personnalisé avec certaines informations spécifiques que nous voulons obtenir. 

C'est pourquoi aujourd'hui je veux partager avec vous comment construire un service qui récupère des données depuis notre instance WordPress et les affiche dans un tableau. Pour être plus précis, je veux connaître le nombre de plugins que j'utilise et quels plugins j'ai installés précédemment que je n'utilise plus. 

## Pourquoi devrais-je savoir quels plugins WordPress j'utilise ?

J'ai toujours trouvé cette information très importante. Surtout au début de votre parcours avec WordPress, vous pourriez être tenté d'installer un plugin pour chaque fonctionnalité que vous voulez que vos sites web aient. 

Eh bien, les plugins peuvent être faciles à installer, mais ils ont aussi quelques inconvénients potentiels :

* S'ils ne sont pas mis à jour souvent, ils peuvent exposer votre site web à des attaques et vulnérabilités
* Ils peuvent rendre le temps de chargement de votre site web beaucoup plus long qu'il ne devrait l'être
* Certains plugins peuvent entrer en conflit les uns avec les autres

Je ne dis pas que vous ne devriez pas utiliser ou faire confiance aux plugins. Mais c'est quelque chose à quoi vous devez faire attention. Alors voyons comment nous pouvons avoir quelques informations utiles sur nos plugins à portée de main.

### Quels outils vais-je utiliser ?

* WordPress APIs - Je vais travailler avec le point de terminaison "plugins".
* React - Je vais créer un composant pour afficher les données. 
* Axios - Je vais l'utiliser pour appeler les API facilement.
* React-Bootstrap - J'ai choisi cette bibliothèque juste pour obtenir un composant de tableau agréable et facile à utiliser rapidement.
* Postman - C'est l'outil que j'utilise toujours pour tester les API.
* Npm - Je vais l'utiliser pour créer une application React et installer des packages.

## WordPress APIs

Comme je l'ai dit au début de cet article, je veux appeler un point de terminaison spécifique pour obtenir un JSON avec les informations sur les plugins que j'ai installés sur mon instance. Plus précisément, je veux compter les plugins que j'utilise actuellement ("active") et les plugins que je n'utilise pas ("inactive"). 

La [documentation](https://developer.wordpress.org/rest-api/) sur les API est très détaillée et pleine d'informations et de concepts utiles. Je clique donc sur "Endpoint reference" dans la barre latérale et je fais défiler jusqu'à cliquer sur "Plugins". 

Concentrons-nous maintenant sur la section "Schema". Ici, je trouve tous les champs qui existent dans un enregistrement de plugin. La liste est assez longue, mais j'ai besoin d'un seul de ces champs : "status". La documentation dit qu'il me retourne une chaîne avec deux valeurs possibles : "inactive" ou "active". 

Voici donc l'API que j'appellerai pour récupérer les données nécessaires :

```
https://<BASE_URL>/wp-json/wp/v2/plugins
```

Jusqu'à présent, tout va bien. Il y a une autre chose à prendre en considération. Certains points de terminaison nécessitent une authentification de base pour retourner des données. Notre point de terminaison en fait partie. À partir de la version 5.6, vous pouvez passer un nom d'utilisateur et un mot de passe d'application pour appeler ce point de terminaison. 

Si vous voulez en savoir plus sur les mots de passe d'application et comment les générer, je vous recommande de consulter cet [article](https://make.wordpress.org/core/2020/11/05/application-passwords-integration-guide/) écrit par la communauté WordPress.

### Temps de tester l'API

Une fois que je sais quel point de terminaison appeler et que j'ai généré mon mot de passe d'application, je suis prêt à tester mon appel d'API avec Postman. Voici ce que j'obtiens :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/postman.png)

Comme vous pouvez le voir, j'obtiens un JSON avec les informations que je cherche : la clé "status". Maintenant, nous sommes prêts à créer notre application React !

## Codons l'application React

Il est maintenant temps de créer le front-end de notre application. Comme je l'ai dit précédemment, j'utiliserai React pour sa flexibilité, Axios pour appeler les API facilement, et React-Bootstrap pour obtenir des composants prêts à l'emploi avec un design agréable. 

Avant de commencer à écrire du code, faisons un récapitulatif de ce que je veux accomplir : je veux que mon application front-end récupère des données depuis mon instance WordPress sur le statut - actif ou inactif - des plugins installés en appelant le point de terminaison "Plugins". 

Pour ce faire, je veux que mon script effectue les actions suivantes :

1. Créer des variables pour stocker le nombre de plugins actifs et inactifs
2. Appeler le point de terminaison par un appel d'API
3. Parcourir le JSON - l'appel d'API retourne avec la logique suivante : Si la clé d'objet "status" est égale à "active", augmenter le compteur correspondant de un, sinon augmenter le compteur lié aux plugins inactifs de 1. Mettre à jour les états correspondants - précédemment définis dans le constructeur - en conséquence
4. Rendre le tableau en utilisant le composant "Table" de React-Bootstrap et passer les états dans le composant de tableau où je veux que les données soient affichées avec le nombre de plugins actifs et inactifs

Assez parlé. Il est temps de coder ! :)

Tout d'abord, je crée mon application React comme ceci :

```
npx create-react-app report
```

Ensuite, j'installe Axios et React-Bootstrap :

```
npm install axios
npm install react-bootstrap bootstrap@5.1.3
```

Tout est prêt. Maintenant, dans mon application React, je me déplace dans le répertoire /src et je crée un nouveau répertoire appelé "components" :

```
/src/components
```

Ensuite, je me déplace dans le dossier components et je crée un fichier "Report.jsx". Voici à quoi ressemble le fichier maintenant :

```jsx
import React from 'react';
import axios from 'axios';
import Table from 'react-bootstrap/Table'

class Report extends React.Component { 
  constructor(props) { 
      super(props); 
      this.state = { countActiveState: 0, countInactiveState: 0, };
  } 

  componentDidMount() {
  let countActive  = 0;
  let countInactive = 0;
  
  axios.get("https://<BASE_URL>/wp-json/wp/v2/plugins", {
    auth: {
      username: process.env.REACT_APP_USERNAME,
      password: process.env.REACT_APP_CLIENT_SECRET
    }
  })
  .then(res => {
      const plugins = res.data;
      for(let key in plugins) {
        if(plugins[key].status === "active") {
          countActive++;
          this.setState({countActiveState: countActive}); 
        }
        else{
          countInactive++;
          this.setState({countInactiveState: countInactive}); 
        }
    }
    })
    .catch(error => {
      alert("Something went wrong. Try again later.");
      console.log(error);
   })
  }

  render() { 
      return ( 
          <Table striped bordered hover >
              <thead>
                  <tr>
                  <th>Status</th>
                  <th>Plugin Amount</th>
                  </tr>
              </thead>
              <tbody>
                  <tr>
                  <th>Active</th>
                  <td>{this.state.countActiveState}</td>
                  </tr>
                  <tr>
                  <th>Inactive</th>
                  <td>{this.state.countInactiveState}</td>
                  </tr>
              </tbody>
          </Table>
      ); 
  } 
} 

export default Report;
```

Décortiquons cela en morceaux plus petits et voyons ce qui se passe :

```
import React from 'react';
import axios from 'axios';
import Table from 'react-bootstrap/Table'
```

J'importe Axios et le composant "Table" de la bibliothèque React-bootstrap.

```
constructor(props) { 
      super(props); 
      this.state = { countActiveState: 0, countInactiveState: 0, };
  } 
```

Dans le constructeur, je définis deux états : countActiveState et countInactiveState. Je les initialise tous les deux à 0.

```jsx
componentDidMount() {
    let countActive  = 0;
    let countInactive = 0;
```

Je déclare deux variables et les initialise à 0 : `countActive` pour stocker le nombre de plugins actifs et `countInactive` pour stocker le nombre de plugins inactifs.

```jsx
axios.get("https://<BASE_URL>/wp-json/wp/v2/plugins", {
      auth: {
        username: process.env.REACT_APP_USERNAME,
        password: process.env.REACT_APP_CLIENT_SECRET
      }
    })
```

J'utilise Axios pour effectuer un appel GET au point de terminaison "Plugins". Je passe également les identifiants pour l'authentification de base.

```jsx
.then(res => {
      const plugins = res.data;
      for(let key in plugins) {
        if(plugins[key].status === "active") {
          countActive++;
          this.setState({countActiveState: countActive}); 
        }
        else{
          countInactive++;
          this.setState({countInactiveState: countInactive}); 
        }
    }
    })
    .catch(error => {
      alert("Something went wrong. Try again later.");
      console.log(error);
   })
  }
```

Ensuite, après avoir stocké les données de réponse dans une variable appelée "plugins", je parcours le JSON et dis : "pour chaque objet JSON, vérifiez si la clé "status" est égale à "active". Si c'est le cas, augmentez la variable countActive de 1 et définissez countActiveState égal à countActive, sinon augmentez la variable countInactive de 1 et définissez countInactiveState égal à countInactive".

```jsx
render() { 
      return ( 
          <Table striped bordered hover >
              <thead>
                  <tr>
                  <th>Status</th>
                  <th>Plugin Amount</th>
                  </tr>
              </thead>
              <tbody>
                  <tr>
                  <th>Active</th>
                  <td>{this.state.countActiveState}</td>
                  </tr>
                  <tr>
                  <th>Inactive</th>
                  <td>{this.state.countInactiveState}</td>
                  </tr>
              </tbody>
          </Table>
      ); 
  } 
} 

export default Report;
```

Ensuite, je rends le composant Table et je passe countActiveState et countInactiveState où je veux que les données soient affichées.

Enfin, je vais dans le fichier App.js et j'ajoute le composant Report :

```jsx
import './App.css';
import Report from './components/Report';

function App() {

  return (
    <div className="App">
      <h1>WordPress Stats Dashboard</h1>
      <Report/>
    </div>
  );
}

export default App;
```

Je démarre l'application :

```
npm start
```

Et la magie opère ! :)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/frontend.png)

### Et voilà !

Donc, ce n'est qu'un exemple rapide de la façon dont vous pouvez facilement construire votre tableau de bord personnalisé pour récupérer et visualiser des données depuis votre instance WordPress. 

Vous pouvez utiliser n'importe quel type de représentation graphique des données, comme des graphiques à barres ou des camemberts. C'est à vous de choisir ! 

N'oubliez pas de jeter un coup d'œil à mon [dépôt](https://github.com/mventuri/react-dashboard-wordpress-api) sur GitHub. N'hésitez pas à partager cet article et vos commentaires. :)