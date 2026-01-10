---
title: Comment créer un CMS de base avec Google Sheets et React
subtitle: ''
author: Marco Venturi
co_authors: []
series: null
date: '2024-03-06T17:55:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-basic-cms-with-google-sheets-and-reactjs
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/--1.png
tags:
- name: cms
  slug: cms
- name: google sheets
  slug: google-sheets
- name: React
  slug: react
seo_title: Comment créer un CMS de base avec Google Sheets et React
seo_desc: "In today's digital landscape, creating a content management system (CMS)\
  \ that is both cost-effective and easy to maintain can be difficult, especially\
  \ if you're operating on a tight budget. \nThis tutorial will show you a solution\
  \ that leverages Googl..."
---

Dans le paysage numérique actuel, créer un système de gestion de contenu (CMS) à la fois économique et facile à maintenir peut être difficile, surtout si vous travaillez avec un budget serré. 

Ce tutoriel vous montrera une solution qui utilise Google Sheets comme base de données improvisée et React pour construire le frontend. Cela vous permettra de contourner efficacement le besoin d'un serveur dédié ou d'un système de base de données traditionnel. 

Cette approche réduit non seulement les coûts généraux associés au développement web, mais simplifie également les mises à jour et la gestion du contenu. C'est une solution idéale si vous cherchez à lancer votre propre CMS simple sans investissement substantiel.

Cette solution convient aux freelances au début de leur carrière et aux clients qui ne peuvent pas investir beaucoup dans leur site web.

## Pourquoi Google Sheets ?

Opter pour Google Sheets comme épine dorsale de votre CMS revient à sa simplicité, sa flexibilité et son coût réduit.

Le développement web traditionnel nécessite un serveur backend pour traiter les données, une base de données pour stocker les informations et un frontend pour afficher le contenu. Mais chaque couche ajoute de la complexité et des coûts. 

Google Sheets, en revanche, agit comme une interface hautement accessible et intuitive qui élimine le besoin d'un serveur et d'une base de données. Il permet à vos utilisateurs de mettre à jour le contenu en temps réel, comme tout CMS, mais sans les coûts habituels de configuration et de maintenance. Cela en fait un excellent choix pour les particuliers, les petites entreprises ou toute personne cherchant à déployer une application web rapidement et avec un minimum de dépenses. 

## Pour commencer

Avant de plonger dans le code, assurez-vous d'avoir Node.js et npm installés sur votre système. Ces outils nous permettront de créer une application React et de gérer ses dépendances. 

Commençons maintenant avec Google Sheets.

### Étape 1 : Configurer votre Google Sheets

1. Allez dans votre Google Sheets
2. Ouvrez la feuille que vous souhaitez utiliser ou créez-en une nouvelle
3. Cliquez sur `Extensions` dans le menu
4. Ensuite, cliquez sur `Apps Script`

Dans l'éditeur Apps Script, vous pouvez écrire un script pour servir d'endpoint. Voici un script qui retourne le contenu d'une feuille Google en format JSON :

```javascript
function convertRangeToJson(data) {
  var jsonArray = [];

  // Vérifie si les données sont vides ou ne contiennent pas assez de lignes pour les en-têtes et au moins une ligne de données
  if (!data || data.length < 2) {
    // Retourne un tableau vide ou un message significatif selon les besoins
    return jsonArray; // ou return 'No data available';
  }

  var headers = data[0];
  for (var i = 1, length = data.length; i < length; i++) {
    var row = data[i];
    var record = {};

    for (var j = 0; j < row.length; j++) {
      record[headers[j]] = row[j];
    }

    jsonArray.push(record);
  }

  return jsonArray;
}
```

Ensuite :

1. Cliquez sur `Fichier` > `Enregistrer`, et donnez un nom à votre projet
2. Cliquez sur `Déployer` > `Nouveau déploiement`.
3. Cliquez sur `Sélectionner le type` et choisissez `Application web`.
4. Remplissez les détails de votre déploiement. Sous `Exécuter en tant que`, choisissez si le script doit s'exécuter en tant que votre compte ou en tant que l'utilisateur accédant à l'application web. Sous `Qui a accès`, choisissez qui peut accéder à votre application web.
5. Cliquez sur `Déployer`.

Il se peut que vous soyez invité à autoriser le script à accéder à vos feuilles Google. Suivez les invites pour ce faire.

Après le déploiement, vous recevrez une URL pour votre application web. C'est votre endpoint API.

Pour vous donner une idée de ce que vous avez fait jusqu'à présent, voici la structure de votre feuille :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Schermata-2024-03-04-alle-16.49.37.png)
_À quoi votre feuille devrait ressembler actuellement_

Et voici le JSON que vous obtenez lorsque vous appelez l'endpoint :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/postman_I.png)
_JSON_

### Étape 2 : Créer votre application React

Avec votre API Google Sheets prête, il est temps de créer l'application React qui récupérera et affichera ces données.

Tout d'abord, créez une application React. Exécutez la commande suivante dans votre terminal pour créer une nouvelle application React :

```bash
npx create-react-app google-sheets-cards
cd google-sheets-cards
npm start
```

Vous pouvez également [utiliser des outils de construction modernes comme Vite](https://www.freecodecamp.org/news/get-started-with-vite/) à cette fin, car CRA n'est plus la méthode recommandée pour construire une application React.

Ensuite, créez le composant de carte. À l'intérieur du répertoire `src`, créez un fichier nommé `Card.js`. Ce composant sera responsable de l'affichage de chaque enregistrement de données :

```jsx
// src/Card.js
function Card({ title, content }) {
  return (
    <div className="card">
      <h1>{title}</h1>
      <p>{content}</p>
    </div>
  );
}

export default Card;
```

Il est maintenant temps de récupérer et d'afficher vos données dans App.js. Modifiez le fichier `App.js` pour inclure la logique de récupération des données de votre API Google Sheets et utilisez le composant Card pour les afficher :

```jsx
// src/App.js
import React, { useEffect, useState } from 'react';
import Card from './Card';
import './App.css'; // Assurez-vous de créer quelques styles de base pour les cartes dans App.css

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('YOUR_ENDPOINT_URL') // Remplacez par votre URL d'endpoint réelle
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error('Erreur lors de la récupération des données :', error));
  }, []);

  return (
    <div className="App">
      <h1>Données de Google Sheets</h1>
      <div className="cards-container">
        {data.map((item, index) => (
          <Card key={index} title={item.Title} content={item.Content} />
        ))}
      </div>
    </div>
  );
}

export default App;
```

Ensuite, vous pouvez styliser vos cartes. Ajoutez le CSS suivant dans `App.css` pour un style de base des cartes :

```css
.card {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  margin: 10px;
  padding: 10px;
  display: inline-block;
  background: #f9f9f9;
}

.cards-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
```

### Étape 3 : Exécuter votre application React

Avec tout configuré, vous pouvez maintenant exécuter votre application React et voir les données de Google Sheets affichées dans votre navigateur. Pour ce faire, suivez ces étapes :

Tout d'abord, démarrez l'application React. Dans votre terminal, naviguez jusqu'au répertoire racine de votre application React si vous n'y êtes pas déjà. Exécutez la commande suivante pour démarrer le serveur de développement :

```bash
npm start
```

Cette commande compile votre application React et l'ouvre dans votre navigateur web par défaut. Vous devriez voir une page web avec un titre "Données de Google Sheets", et en dessous, une série de cartes, chacune affichant un titre et un contenu récupérés depuis vos données Google Sheets. 

Voici, en fait, ce que nous obtenons :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Schermata-2024-03-04-alle-16.52.22.png)
_Données de Google Sheets et Carte 1, Carte 2 et Carte 3 affichées à l'écran_

Vous pouvez maintenant consulter vos données. Chaque carte sur la page correspond à une ligne dans votre Google Sheets, avec les champs de titre et de contenu affichés comme spécifié dans votre composant Card. Si vous apportez des modifications à vos données Google Sheets, vous pouvez actualiser la page web pour voir les changements reflétés immédiatement.

Vous pouvez déployer votre application React sur l'un des nombreux services que vous pouvez trouver en ligne tels que Github Actions ou Netlify. C'est un moyen simple et efficace d'héberger votre application frontend gratuitement avec des performances significatives. 

## Conclusion

Félicitations ! Vous avez créé une application web dynamique qui récupère des données depuis une feuille Google et les affiche en utilisant React. 

Cette approche offre une manière flexible et simple de gérer le contenu de votre application sans avoir besoin d'un serveur backend ou d'une base de données.

Google Sheets sert de plateforme accessible et collaborative pour gérer les données, tandis que React vous permet de construire une interface utilisateur réactive et interactive. Ensemble, ils fournissent une combinaison puissante pour créer des applications web qui peuvent être rapidement mises à jour et facilement maintenues.