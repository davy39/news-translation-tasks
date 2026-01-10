---
title: Comment créer un calculateur simple de Bitcoin vers USD
subtitle: ''
author: Eesa Zahed
co_authors: []
series: null
date: '2024-07-22T22:36:23.000Z'
originalURL: https://freecodecamp.org/news/build-a-bitcoin-to-usd-calculator
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/pexels-davidmcbee-730547.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Comment créer un calculateur simple de Bitcoin vers USD
seo_desc: "Welcome to this fun and hands-on project where we'll build a calculator\
  \ that converts Bitcoin to USD. You'll learn about API fetching, DOM manipulation,\
  \ and localStorage, and you'll use some basic math along the way. \nBy the end of\
  \ this tutorial, you..."
---

Bienvenue dans ce projet amusant et pratique où nous allons créer un calculateur qui convertit les Bitcoins en USD. Vous apprendrez à récupérer des données via une API, à manipuler le DOM et à utiliser localStorage, et vous utiliserez quelques notions de base en mathématiques.

À la fin de ce tutoriel, vous aurez un calculateur de prix Bitcoin fonctionnel qui récupère le prix actuel du Bitcoin, vous permet de calculer la valeur de vos avoirs en Bitcoin et sauvegarde vos données localement.

Ce projet est adapté aux débutants qui comprennent les bases du HTML, du CSS et du JavaScript vanilla.

Voici ce que nous allons créer :

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-17-at-21.39.30.png)
_Le projet finalisé !_

## Installation du projet

Créez un nouveau dossier et nommez-le en rapport avec le projet, par exemple _btc-usd-calc_. Créez un fichier intitulé _index.html_ dans votre dossier de projet.

Commencez par écrire le HTML. La page doit essentiellement contenir :

* Un titre
* Le prix actuel du Bitcoin
* Un champ de texte pour que l'utilisateur saisisse ses avoirs en Bitcoin
* Un bouton pour calculer la valeur de ses avoirs en Bitcoin
* Le montant calculé

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Calculateur Bitcoin</title>
    <link rel="shortcut icon" href="favicon.ico" type="image/x-icon" />
  </head>
  <body>
    <div class="container">
      <h1>Calculateur Bitcoin</h1>
      <main id="main">
        <p>
          <span id="currentPrice">Dernier prix :</span>
          <b>$<span id="bitcoinPrice"></span> USD</b>
        </p>
        <label for="bitcoinAmount">Combien de Bitcoins possédez-vous ?</label>
        <input type="number" id="bitcoinAmount" step="any" placeholder="0.05" />
        <button id="calculateBtn">Calculer</button>
        <br />
        <br />
        <h3 id="usdAmount"></h3>
      </main>
    </div>
    <script src="script.js"></script>
  </body>
</html>

```

Ouvrez-le dans un navigateur et vous devriez voir ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-17-at-21.44.38.png)
_Assez basique pour le moment - le style sera ajouté plus tard !_

## Récupérer l'API

Maintenant, dans le même répertoire que _index.html_, créez un nouveau fichier intitulé _script.js_.

Il est important de savoir quelle API utiliser. Je vous recommande vivement d'utiliser [celle-ci](https://api.coindesk.com/v1/bpi/currentprice.json) en suivant ce tutoriel. L'API CoinDesk est :

* Gratuite
* Rapide
* Aucun jeton API nécessaire
* Minimaliste
* Contient les informations nécessaires pour ce projet

Dans _script.js_, définissez une constante pour l'URL de l'API :

```javascript
const API_URL = "https://api.coindesk.com/v1/bpi/currentprice.json";

```

La prochaine étape consiste à ajouter un écouteur d'événement pour appeler l'API une fois le contenu de la page chargé. Vous pouvez le faire en ajoutant le code suivant directement sous la constante API_URL :

```javascript
document.addEventListener("DOMContentLoaded", async () => {
  // Exécute une fonction asynchrone une fois le contenu du DOM chargé
  let bitcoinPrice; // Initialise la variable

  try {
    const response = await fetch(API_URL);
    // Attend une réponse de la requête HTTP envoyée à l'URL de l'API

    const data = await response.json();
    // Attend le contenu JSON de la réponse

    bitcoinPrice = data.bpi.USD.rate_float.toFixed(2);
    // Réassigne la variable bitcoinPrice à la valeur USD du Bitcoin, arrondie aux 2 décimales les plus proches.
  } catch {
    console.log("erreur !"); // En cas d'erreur
  }

  console.log(bitcoinPrice); // Affiche le prix dans la console
});

```

En cas d'erreur, le programme nous en informera dans la console. Sinon, `bitcoinPrice` sera affiché dans la console. Vous pouvez le tester maintenant et voir si vous obtenez le prix actuel du Bitcoin !

## Comment implémenter localStorage

Fondamentalement, `localStorage` est une fonctionnalité présente dans la plupart des navigateurs web (voir quelles versions le supportent [ici](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage#browser_compatibility)) qui sauvegarde des informations afin qu'elles soient conservées dans la mémoire du navigateur même après la fermeture de la page ou du navigateur.

Commençons par modifier quelques lignes :

```javascript
document.addEventListener("DOMContentLoaded", async () => {
  let bitcoinPrice = localStorage.getItem("lastBitcoinPrice");
  // Récupère le dernier prix Bitcoin enregistré dans localStorage, s'il existe
  // Note : Il devrait être null la première fois que vous essayez d'exécuter la page

  try {
    const response = await fetch(API_URL);
    const data = await response.json();
    bitcoinPrice = data.bpi.USD.rate_float.toFixed(2);
    // bitcoinPrice sera réécrit
    
    localStorage.setItem("lastBitcoinPrice", bitcoinPrice);
    // Sauvegarde le prix le plus récent dans localStorage
  } catch {
    console.log("erreur !");
  }

  console.log(bitcoinPrice);
});

```

## Comment implémenter la manipulation du DOM

Le Document Object Model (DOM) est une interface qui permet des interactions de programmation avec des documents web. Essentiellement, la manipulation du DOM avec JavaScript nous permet de mettre à jour certaines parties ou la totalité d'un document.

Dans ce projet, nous l'utiliserons pour afficher le prix actuel du Bitcoin et la valeur calculée. Nous l'utiliserons également pour récupérer la valeur saisie par l'utilisateur dans le champ de texte `#bitcoinAmount` lorsque le bouton de calcul est cliqué.

Implémentons la manipulation du DOM :

```javascript
document.addEventListener("DOMContentLoaded", async () => {
  const main = document.getElementById("main");
  const bitcoinPriceElement = document.getElementById("bitcoinPrice");
  const bitcoinAmountInput = document.getElementById("bitcoinAmount");
  const calculateBtn = document.getElementById("calculateBtn");
  const usdAmountElement = document.getElementById("usdAmount");

  let bitcoinPrice = localStorage.getItem("lastBitcoinPrice");

  try {
    const response = await fetch(API_URL);
    const data = await response.json();
    bitcoinPrice = data.bpi.USD.rate_float.toFixed(2);
    localStorage.setItem("lastBitcoinPrice", bitcoinPrice);

    bitcoinPriceElement.textContent = bitcoinPrice;
    // Définit le contenu textuel de bitcoinPriceElement au bitcoinPrice actuel
  } catch {
    if (bitcoinPrice) {
      // S'il existe un bitcoinPrice dans localStorage...
      bitcoinPriceElement.textContent = bitcoinPrice;
      // ...affiche ce qui est sauvegardé dans localStorage
    } else {
      main.innerHTML = "<p>Impossible de récupérer le prix du Bitcoin :(</p>";
      return;
    }
  }

  console.log(bitcoinPrice);
});
```

## Comment calculer la valeur actuelle du portefeuille

Maintenant, l'objectif d'un calculateur Bitcoin est de calculer la valeur d'un portefeuille Bitcoin, et pas nécessairement le prix actuel.

Par exemple, le prix actuel du Bitcoin pourrait être de 60 000 USD. Si vous possédez 2 Bitcoins, votre portefeuille vaut 120 000 USD. Si vous possédez la moitié (0,5) d'un Bitcoin, votre portefeuille vaut 30 000 USD.

Récupérons le montant de Bitcoin que l'utilisateur possède (`bitcoinAmount`) depuis localStorage.

```javascript
// continuer après console.log(bitcoinPrice);

let bitcoinAmount = localStorage.getItem("bitcoinAmount");

```

Calculez le montant en USD avec cette fonction :

```javascript
const calculateUSDAmount = () => {
  bitcoinAmount = bitcoinAmountInput.value || 0;
  // bitcoinAmount sera réassigné à ce qui est dans le champ de saisie sur le front-end, sinon sa valeur par défaut sera zéro

  const usdAmount = bitcoinAmount * bitcoinPrice;
  // Supposons que vous avez 2 Bitcoins et que le prix est de 60000.
  // 2 * 60000 = 120000

  usdAmountElement.innerHTML = `<b>$${usdAmount.toFixed(
    2
  )} USD</b> de Bitcoin.`;
  // Arrondir aux 2 décimales les plus proches et l'afficher
};

```

Vous vous souvenez quand nous avons récupéré `bitcoinAmount` depuis localStorage ? Maintenant, lorsque la page se charge, définissons la valeur du champ de saisie sur le front-end à `bitcoinAmount`.

```javascript
  if (bitcoinAmount) {
    bitcoinAmountInput.value = bitcoinAmount;
    // Définit la valeur du champ de saisie à bitcoinAmount

    calculateUSDAmount();
    // Calcule et met à jour le front-end
  }
```

Pour que l'utilisateur puisse mettre à jour son `bitcoinAmount`, ajoutons un écouteur d'événement lorsque le bouton `calculateBtn` est cliqué :

```javascript
  calculateBtn.addEventListener("click", () => {
    localStorage.setItem("bitcoinAmount", bitcoinAmountInput.value);
    // Sauvegarde la valeur du champ de saisie dans localStorage

    calculateUSDAmount();
    // Calcule et met à jour le front-end
  });

```

Tout le JavaScript devrait maintenant être complet.

## Code JavaScript complet

Votre code entier devrait ressembler à ceci (à part les commentaires et la mise en forme) :

```javascript
const API_URL = "https://api.coindesk.com/v1/bpi/currentprice.json";

document.addEventListener("DOMContentLoaded", async () => {
  const main = document.getElementById("main");
  const bitcoinPriceElement = document.getElementById("bitcoinPrice");
  const bitcoinAmountInput = document.getElementById("bitcoinAmount");
  const calculateBtn = document.getElementById("calculateBtn");
  const usdAmountElement = document.getElementById("usdAmount");

  let bitcoinPrice = localStorage.getItem("lastBitcoinPrice");

  try {
    const response = await fetch(API_URL);
    const data = await response.json();
    bitcoinPrice = data.bpi.USD.rate_float.toFixed(2);
    localStorage.setItem("lastBitcoinPrice", bitcoinPrice);

    bitcoinPriceElement.textContent = bitcoinPrice;
    // Définit le contenu textuel de bitcoinPriceElement au bitcoinPrice actuel
  } catch {
    if (bitcoinPrice) {
      // S'il existe un bitcoinPrice dans localStorage...
      bitcoinPriceElement.textContent = bitcoinPrice;
      // ...affiche ce qui est sauvegardé dans localStorage
    } else {
      main.innerHTML = "<p>Impossible de récupérer le prix du Bitcoin :(</p>";
      return;
    }
  }

  console.log(bitcoinPrice);

  let bitcoinAmount = localStorage.getItem("bitcoinAmount");

  const calculateUSDAmount = () => {
    bitcoinAmount = bitcoinAmountInput.value || 0;
    // bitcoinAmount sera réassigné à ce qui est dans le champ de saisie sur le front-end, sinon sa valeur par défaut sera zéro

    const usdAmount = bitcoinAmount * bitcoinPrice;
    // Supposons que vous avez 2 Bitcoins et que le prix est de 60000.
    // 2 * 60000 = 120000

    usdAmountElement.innerHTML = `<b>$${usdAmount.toFixed(
      2
    )} USD</b> de Bitcoin.`;
    // Arrondir aux 2 décimales les plus proches et l'afficher
  };

  if (bitcoinAmount) {
    bitcoinAmountInput.value = bitcoinAmount;
    // Définit la valeur du champ de saisie à bitcoinAmount

    calculateUSDAmount();
    // Calcule et met à jour le front-end
  }

  calculateBtn.addEventListener("click", () => {
    localStorage.setItem("bitcoinAmount", bitcoinAmountInput.value);
    // Sauvegarde la valeur du champ de saisie dans localStorage
  
    calculateUSDAmount();
    // Calcule et met à jour le front-end
  });
});

```

Testez-le dans le navigateur et amusez-vous avec !

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-18-at-13.11.56.png)

## Comment ajouter du style

Pour le moment, il n'y a pas de CSS, donc cela semble assez basique. Vous êtes libre de personnaliser le style selon vos préférences.

Si vous souhaitez le styliser comme je l'ai fait, suivez les instructions en ajoutant cette ligne à la fin de `<head>` :

```html
   <link rel="stylesheet" href="style.css" />
</head>
```

Ensuite, créez un nouveau fichier intitulé _style.css_ dans le même répertoire que _index.html_.

Écrivez le code suivant dans _style.css_ :

```css
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap");

body {
  font-family: "Inter", sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f5f5f5;
}

.container {
  max-width: 50rem;
  margin: 5rem auto;
  background-color: #fff;
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: 0 0 1rem rgba(0, 0, 0, 0.1);
}

#main {
  width: 50%;
  margin: auto;
}

h1 {
  text-align: center;
  font-size: 3rem;
  margin-bottom: 2rem;
  background-image: linear-gradient(to right, #4b0bff, #68b2ff);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

h3 {
  font-weight: normal;
}

button {
  padding: 0.5rem 0.75rem;
  border: none;
  background-color: #007bff;
  color: #fff;
  cursor: pointer;
  border-radius: 0.5rem;
  transition: 0.3s;
  margin-left: 0.25rem;
}

button:hover {
  background-color: #0056b3;
}

label {
  display: block;
  margin-bottom: 1rem;
}

input[type="number"] {
  padding: 0.5rem;
  font-size: 1rem;
  border: none;
  background-color: #e3e3e3;
  border-radius: 0.5rem;
}

@media (prefers-color-scheme: dark) {
  body {
    color-scheme: dark;
    color: white;
    background: #2b0057;
  }

  h1 {
    background-image: linear-gradient(to right, #4facfe, #00f2fe);
  }

  .container {
    background: #16022c;
  }

  input[type="number"] {
    background-color: #33194d;
  }
}

```

Vous devriez voir ceci si vous êtes en mode sombre :

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-18-at-13.17.06.png)
_Mode sombre_

Et ceci si vous êtes en mode clair :

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-18-at-13.16.52.png)
_Mode clair_

Et c'est tout !

Vous pouvez le voir sur GitHub ici : [https://github.com/eesazahed/bitcoin-calc/](https://github.com/eesazahed/bitcoin-calc/)

Voici l'aperçu en direct : [https://eesazahed.github.io/bitcoin-calc/](https://eesazahed.github.io/bitcoin-calc/)

## **Conclusion**

N'hésitez pas à consulter mon [LinkedIn](https://www.linkedin.com/in/eszhd/) ou [GitHub](https://github.com/eesazahed).

Si vous souhaitez me contacter, mon adresse email est eszhd1 (at) gmail.com