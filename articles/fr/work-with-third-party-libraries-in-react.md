---
title: Comment travailler avec des API tierces dans React en créant une application
  Web de taux de change de crypto-monnaies
subtitle: ''
author: Chidera Humphrey
co_authors: []
series: null
date: '2024-01-10T15:24:13.000Z'
originalURL: https://freecodecamp.org/news/work-with-third-party-libraries-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/20240105_040821_0000-3.png
tags:
- name: api
  slug: api
- name: React
  slug: react
- name: Web Applications
  slug: web-applications
seo_title: Comment travailler avec des API tierces dans React en créant une application
  Web de taux de change de crypto-monnaies
seo_desc: 'Working with APIs is crucial to any web application. And as a frontend
  developer, knowing how to connect your apps with third-party APIs is an important
  skill to have.

  In this article, you''ll learn how to connect your app and fetch data from a third-...'
---

Travailler avec des API est crucial pour toute application web. Et en tant que développeur frontend, savoir comment connecter vos applications avec des API tierces est une compétence importante à avoir.

Dans cet article, vous apprendrez comment connecter votre application et récupérer des données à partir d'une API tierce en construisant une application web de change de crypto-monnaies en React.

## Table des matières

* [Prérequis](#prérequis)
    
* [Comment configurer le projet](#comment-configurer-le-projet)
    
    * [Initialiser un nouveau projet React](#initialiser-un-nouveau-projet-react)
        
    * [Installer les dépendances nécessaires](#installer-les-dépendances-nécessaires)
        
    * [Configurer la structure de votre projet](#configurer-la-structure-de-votre-projet)
        
* [Comment construire l'interface utilisateur](#comment-construire-linterface-utilisateur)
    
* [Comment récupérer des données avec React Query](#comment-récupérer-des-données-avec-react-query)
    
* [Comment afficher les données dans l'interface utilisateur](#comment-afficher-les-données-dans-linterface-utilisateur)
    
* [Gestion des erreurs](#gestion-des-erreurs)
    
* [Conclusion](#conclusion)
    

## Prérequis

Ce tutoriel suppose que vous avez des connaissances de base en React. De plus, vous devriez être capable de travailler avec Axios, spécifiquement pour effectuer des appels API.

De plus, vous aurez besoin d'une clé API de [RapidAPI](https://rapidapi.com) pour suivre ce tutoriel.

## Comment configurer le projet

### Initialiser un nouveau projet React

Utilisez la commande suivante pour initialiser un nouveau projet React en utilisant Vite : `npm create vite@latest`

Suivez ensuite les invites qui apparaissent.

[Vite](https://vitejs.dev/guide/) est un outil de construction qui permet un rechargement rapide de vos applications React. Pour plus d'informations sur Vite, vous pouvez consulter leur documentation officielle.

### Installer les dépendances nécessaires

Pour ce tutoriel, vous aurez besoin de quelques packages :

* Axios : une bibliothèque pour effectuer des appels API basés sur des promesses.
    
* react-query : une bibliothèque de récupération de données qui gère la mise en cache, le chargement et l'état d'erreur de notre appel API.
    
* antd (Ant Design) : une bibliothèque d'interface utilisateur de composants React pré-construits.
    

Utilisez la commande suivante pour installer ces packages : `npm install react-query antd axios`

### Configurer la structure de votre projet

Dans cette section, vous allez créer quelques dossiers à l'intérieur du dossier `src`. Cela permet de garder la structure de votre application propre et facile à utiliser.

À l'intérieur du dossier `src`, créez un nouveau dossier appelé `components`.

À l'intérieur du dossier `components`, créez trois dossiers : `fetchData`, `UI` et `currencies`.

Avec la configuration du projet terminée, passons à la construction de l'application.

## Comment construire l'interface utilisateur

Dans cette section, vous allez créer l'interface utilisateur de l'application. Il y aura peu ou pas de logique.

Accédez au dossier `UI` à l'intérieur du dossier `components`.

Créez un nouveau fichier, `ExchangeRateUI.jsx`, à l'intérieur du dossier `UI`.

Ajoutez le code suivant à l'intérieur du fichier `ExchangeRateUI.jsx` :

```js
import { Typography, Card } from "antd";

export function ExchangeRateUI(props) {
 return (
   <div className="exchange-rate-ui">
     <Card
       extra={3}
       bordered={false}
       style={{ width: 350, backgroundColor: "#4d4add", color: "#fff" }}
       size="default"
     >
       <Typography.Paragraph style={{ color: "#fff" }}>Bitcoin</Typography.Paragraph>
     </Card>
   </div>
 );
}
```

Dans le code ci-dessus, vous avez utilisé les composants `Card` et `Typography` de la bibliothèque d'interface utilisateur Ant Design pour créer l'interface utilisateur de notre application.

Ensuite, accédez au dossier `currencies` et créez un fichier `currencies.jsx`.

Ajoutez le code suivant à l'intérieur de `currencies.jsx` :

```js
export const cryptocurrencies = [
  { value: "BTC", label: "Bitcoin" },
  { value: "ETH", label: "Ethereum" },
  { value: "BCH", label: "Bitcoin Cash" },
  { value: "XRP", label: "Ripple" },
  { value: "SOL", label: "Solana" },
  { value: "ADA", label: "Cardano" },
  { value: "BNB", label: "Binance Coin" },
];

export const fiatCurrencies = [
  { value: "USD", label: "US Dollar" },
  { value: "GBP", label: "British Pound" },
  { value: "EUR", label: "Euro" },
  { value: "NGN", label: "Naira" },
  { value: "CNY", label: "Chinese Yuan" },
  { value: "RUB", label: "Russian Ruble" },
  { value: "SGD", label: "Singaporean Dollar" },
];
```

Dans le code ci-dessus, vous avez créé deux tableaux, `fiatCurrencies` et `cryptocurrencies`, et exporté ces tableaux. Ils seront utilisés par les composants `Select` d'Ant Design.

Ensuite, créez un fichier, `ExchangeRate.jsx`, à l'intérieur du dossier `components`.

Ajoutez le code suivant à l'intérieur du fichier `ExchangeRate.jsx` :

```js
import { useState } from "react";
import { Typography, Select } from "antd";
import { cryptocurrencies, fiatCurrencies } from "./currencies/currencies.jsx";
import { ExchangeRateUI } from "./UI/ExchangeRateUI.jsx";

function ExchangeRate() {
  const [fromCurrency, setFromCurrency] = useState(cryptocurrencies[0].value);
  const [toCurrency, setToCurrency] = useState(fiatCurrencies[0].value);

  const handleFromCurrencyChange = (e) => {
    setFromCurrency(e);
    console.log(e);
  };

  const handleToCurrencyChange = (e) => {
    setToCurrency(e);
    console.log(e);
  };

  return (
    <section className="exchange-rate">
      <Typography.Title style={{ color: "#4d4add" }} level={2}>
        Exchange Rate
      </Typography.Title>
      <Typography.Text>
        Get the latest exchange rate of cryptocurrencies in your favorite
        currency
      </Typography.Text>
      <section className="select-group" style={{ display: "flex", marginTop: "1rem", gap: "1rem", justifyContent: "space-around" }}>
        <Select defaultValue={cryptocurrencies[0].value} options={cryptocurrencies} onChange={handleFromCurrencyChange} />
        <Select defaultValue={fiatCurrencies[0].value} options={fiatCurrencies} onChange={handleToCurrencyChange} />
      </section>
      <section style={{ marginTop: "1rem" }}>
        <ExchangeRateUI />
      </section>
    </section>
  );
}

export default ExchangeRate;
```

Dans le composant `ExchangeRate`, vous avez importé les tableaux `fiatCurrencies` et `cryptocurrencies` depuis le dossier `currencies`. Les tableaux `fiatCurrencies` et `cryptocurrencies` sont utilisés par le composant `Select` pour afficher les devises sélectionnées que vous souhaitez convertir.

Le hook `useState` est utilisé pour suivre les devises sélectionnées.

L'instruction `return` rend le composant `ExchangeRateUI`.

Mettez à jour votre fichier `App.jsx` avec le code suivant : `import ExchangeRate from './components/ExchangeRate.jsx' function App(){ return ( <ExchangeRate/> ) } export default App;`

Si vous avez suivi chaque étape correctement, votre application web devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/GIF-240109_045936-1-.gif align="left")

*GIF de l'interface utilisateur de l'application crypto*

Maintenant que l'interface utilisateur de l'application est configurée, passons à l'implémentation de la logique de récupération des données.

## Comment récupérer des données avec React Query

Dans cette section, vous allez implémenter la logique de récupération des données.

Remplacez le code dans le fichier `App.jsx` par le code suivant :

```js
import { QueryClient, QueryClientProvider } from "react-query";
import ExchangeRate from "./components/ExchangeRate.jsx";

const queryClient = new QueryClient(); // Instanciez une nouvelle instance QueryClient

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <ExchangeRate />
    </QueryClientProvider>
  );
}

export default App;
```

Dans le code ci-dessus, vous avez créé un `queryClient` en utilisant `QueryClient()` de `react-query`. Le `queryClient` est passé au `QueryClientProvider` via les props `client`. Cela permet aux composants enfants d'avoir accès au `queryClient`, qui sera utilisé pour la récupération des données.

React-query vient avec de bonnes configurations par défaut, mais vous allez modifier certaines de ces configurations par défaut. Cela permet d'éviter la limitation de débit due à des requêtes excessives vers l'API.

Remplacez la déclaration `queryClient` par le code suivant dans votre `App.jsx` :

```js
// code précédent

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      method: "GET", // Méthode HTTP par défaut pour les requêtes
      refetchOnWindowFocus: false, // Désactiver le rafraîchissement automatique lors de la mise au point de la fenêtre
      refetchInterval: 60000, // Rafraîchir les requêtes toutes les 60 secondes
    },
  },
});

// code restant
```

Dans le code ci-dessus, vous empêchez le composant de se rafraîchir lorsque vous remettez le focus sur la page web. De plus, vous augmentez le temps de rafraîchissement en arrière-plan à six secondes.

Après avoir apporté les modifications, votre `App.jsx` devrait ressembler à ceci :

```js
import { QueryClient, QueryClientProvider } from "react-query";

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false, // Désactiver le rafraîchissement automatique lors de la mise au point
      refetchInterval: 60000, // Rafraîchir les requêtes toutes les 60 secondes
    },
  },
});

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <ExchangeRate />
    </QueryClientProvider>
  );
}

export default App;
```

Ensuite, vous allez créer la fonction de récupération des données dans le dossier `fetchData`.

Créez un nouveau fichier appelé `fetchData.jsx` dans le dossier `fetchData`.

Ajoutez le code suivant dans le fichier `fetchData.jsx` :

```js
import axios from 'axios' 

export function getExchangeRate(fromCurrency, toCurrency){ 

    const options = { 
        method: 'GET', 
        url: 'https://alpha-vantage.p.rapidapi.com/query', 
        params: { from_currency: fromCurrency, function: 'CURRENCY_EXCHANGE_RATE', to_currency: toCurrency }, 
        headers: { 'X-RapidAPI-Key': 'YOUR API KEY', 'X-RapidAPI-Host': 'alpha-vantage.p.rapidapi.com' } 
    }; 
    
    return axios.request(options)
        .then(res => { return res.data; })
        .catch((err) => { return err; }) 

}
```

Dans le code ci-dessus, vous avez utilisé Axios pour récupérer des données de l'API AlphaVantage via RapidAPI.

N'oubliez pas de remplacer `YOUR API KEY` par votre clé API de RapidAPI.

Accédez à votre composant `ExchangeRate`, et ajoutez le code suivant :

```js
import { useQuery } from 'react-query';
import { getExchangeRate } from './fetchData/fetchData.jsx';

function ExchangeRate() {
  // code précédent

  const dependencies = {
    fromCurrency: fromCurrency,
    toCurrency: toCurrency,
  };

  const { data, isLoading, isError, error } = useQuery({
    queryKey: ["exchangeRate", dependencies],
    queryFn: () => fetchData(fromCurrency, toCurrency),
    staleTime: 1000 * 60,
    retry: 1,
    retryDelay: 6000,
  });

  // code supplémentaire
}
```

Dans le code ci-dessus, vous avez utilisé le hook `useQuery` pour récupérer les données de taux de change avec des paramètres spécifiés.

Le hook `useQuery` retourne un objet avec de nombreuses propriétés, mais les propriétés suivantes sont celles qui nous intéressent :

* `data` : contient les données récupérées.
    
* `isLoading` : indique si les données sont encore en cours de récupération.
    
* `isError` : indique si une erreur s'est produite lors de la récupération.
    
* `error` : contient les détails de l'erreur en cas de problème.
    

La `queryKey` est un tableau représentant un identifiant unique pour cette requête, et `staleTime` définit le cache pour considérer les données comme obsolètes après une minute. `retry` et `retryDelay` contrôlent les tentatives de nouvelle requête.

Examinons la propriété `data`.

La propriété `data` est l'objet de réponse qui est retourné avec succès de notre appel à l'API AlphaVantage.

La propriété `data` ressemble à ceci :

```sh
{
  "Realtime Currency Exchange Rate": {
    "1. From_Currency Code": "BTC",
    "2. From_Currency Name": "Bitcoin",
    "3. To_Currency Code": "USD",
    "4. To_Currency Name": "United States Dollar",
    "5. Exchange Rate": "44138.96000000",
    "6. Last Refreshed": "2024-01-05 00:16:03",
    "7. Time Zone": "UTC",
    "8. Bid Price": "44138.96000000",
    "9. Ask Price": "44138.97000000"
  }
}
```

Nous ne sommes intéressés que par la propriété `5. Exchange Rate` de la propriété `data`, car elle contient le taux de change.

Puisque nous n'avons besoin que de `5. Exchange Rate`, passez-le en tant que props au composant `ExchangeRateUI`.

Après avoir apporté les modifications, votre composant `ExchangeRate` devrait ressembler à ceci :

```js
import React, { useState, useEffect } from 'react';
import { Typography, Select, Spin } from 'antd';
import { cryptocurrencies, fiatCurrencies } from './currencies/currencies.jsx';
import { ExchangeRateUI } from './UI/ExchangeRateUI.jsx';
import { useQuery } from 'react-query';
import { fetchData } from './fetchData/fetchData.jsx';

function ExchangeRate() {
  const [fromCurrency, setFromCurrency] = useState(cryptocurrencies[0].value);
  const [toCurrency, setToCurrency] = useState(fiatCurrencies[0].value);
  const [currencySymbol, setCurrencySymbol] = useState("Bitcoin");

  const handleFromCurrencyChange = (e) => {
    setFromCurrency(e);
    console.log(e);
  };

  const handleToCurrencyChange = (e) => {
    setToCurrency(e);
    console.log(e);
  };

  useEffect(() => {
    const fromCurrencyLabel = cryptocurrencies.find(currency => currency.value === fromCurrency)?.label;
    setCurrencySymbol(fromCurrencyLabel);
  }, [fromCurrency]);

  const dependencies = { fromCurrency: fromCurrency, toCurrency: toCurrency };
  const { data, isLoading, isError, error } = useQuery({
    queryKey: ["exchangeRate", dependencies],
    queryFn: () => fetchData(fromCurrency, toCurrency),
    staleTime: 1000 * 60,
    retry: 1,
    retryDelay: 60000
  });

  console.log(data);

  return (
    <section className="exchange-rate">
      <Typography.Title style={{ color: "#4d4add" }} level={2}>Exchange Rate</Typography.Title>
      <Typography.Text>Get the latest exchange rate of cryptocurrencies in your favorite currency</Typography.Text>
      <section className="select-group" style={{ display: "flex", marginTop: "1rem", gap: "1rem", justifyContent: "space-around" }}>
        <Select defaultValue={cryptocurrencies[0].value} options={cryptocurrencies} onChange={handleFromCurrencyChange} />{' '}
        <Select defaultValue={fiatCurrencies[0].value} options={fiatCurrencies} onChange={handleToCurrencyChange} />
      </section>
      <section style={{ marginTop: '1rem' }}>
        {isLoading ? (
          <Spin tip="Fetching results" spinning size="large" />
        ) : isError ? (
          <div>Error: {error.message}</div>
        ) : (
          <div>
            <ExchangeRateUI price={data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]} dataObj={dependencies} currencySymbol={currencySymbol} />
          </div>
        )}
      </section>
    </section>
  );
}

export default ExchangeRate;
```

Dans le code ci-dessus, vous avez utilisé l'opérateur ternaire pour rendre différents contenus en fonction de l'état de la récupération des données.

`currencySymbol` est utilisé pour suivre la crypto-monnaie dont vous vérifiez le taux de change.

Ouvrez votre console et vous devriez voir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot_20240105-015827-1-.jpg align="left")

Maintenant que vous avez terminé l'implémentation de la logique de récupération des données, passons à l'affichage des données dans l'interface utilisateur.

## Comment afficher les données dans l'interface utilisateur

Dans cette section, vous allez ajouter les dernières touches à l'application web.

Mettez à jour votre fichier `ExchangeRateUI.jsx` avec le code suivant :

```js
import React from "react";
import { Typography, Card } from "antd";

export function ExchangeRateUI(props) {
  const { price, dataObj, currencySymbol } = props;
  const toCurrency = dataObj.toCurrency;
  let value = Number(price);
  let currencyCode = toCurrency;

  let currency = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: currencyCode,
  });

  let formattedCurrency = currency.format(value);

  return (
    <div className="exchange-rate-ui">
      <Card extra={currencySymbol} bordered={false} style={{ width: 350, backgroundColor: "#4d4add", color: '#fff' }} size="default">
        <Typography.Paragraph style={{ color: "#fff" }}>{formattedCurrency}</Typography.Paragraph>
      </Card>
    </div>
  );
}
```

Comprenons ce qui se passe dans le code ci-dessus.

Tout d'abord, vous prenez le prix brut représentant le taux de change, vous assurez qu'il est traité comme un nombre, déterminez le code de la devise, puis formatez la valeur numérique en une chaîne de devise conviviale. Cette devise formatée est utilisée pour l'affichage dans l'interface utilisateur afin de fournir une représentation claire et standardisée du taux de change.

Ensuite, la devise formatée est affichée dans un composant `Card` stylisé d'Ant Design. La `Card` inclut le `currencySymbol` en tant qu'élément supplémentaire. La couleur de fond, la largeur et la couleur du texte sont stylisées pour une interface utilisateur visuellement attrayante.

Votre application devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/GIF-240109_050748-1-.gif align="left")

*GIF de l'application crypto complète et fonctionnelle*

Félicitations. Vous avez construit une application web de taux de change de crypto-monnaies en React.

## Gestion des erreurs

La gestion des erreurs est un aspect crucial du développement d'applications web. En effet, les applications web et les logiciels en général peuvent subir des plantages et des temps d'arrêt.

Dans React, lorsque votre application plante, elle affiche généralement un écran blanc/vide. Cela ne constitue pas une bonne expérience utilisateur. Vous voudrez afficher une sorte d'information à vos utilisateurs si votre application plante.

Dans cette section, vous allez utiliser le composant `ErrorBoundary` pour gérer les plantages de l'application.

Créez un fichier appelé `ErrorBoundary.jsx` dans le dossier `src`.

Ajoutez le code suivant dans le fichier `ErrorBoundary.jsx` :

```js
import React from "react";
import { Typography } from "antd";

export default class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    // Mettre à jour l'état pour que le prochain rendu affiche l'interface de repli.
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    // Vous pouvez également journaliser l'erreur dans un service de rapport d'erreurs
    console.error("Erreur capturée : ");
  }

  render() {
    if (this.state.hasError) {
      // Vous pouvez rendre n'importe quelle interface de repli personnalisée
      return <Typography.Title level={4}>Quelque chose s'est mal passé.</Typography.Title>;
    }

    return this.props.children;
  }
}
```

Dans le code ci-dessus, vous affichez le message "Quelque chose s'est mal passé" s'il y a une erreur lors du rendu de votre application.

Mettez à jour votre fichier `index.jsx` avec le code suivant :

```js
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import ErrorBoundary from './ErrorBoundary';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <ErrorBoundary>
      <App />
    </ErrorBoundary>
  </React.StrictMode>
);
```

Visitez la [documentation React](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary) pour plus d'informations sur ErrorBoundary.

## Conclusion

Cet article vous a guidé à travers la manière de travailler avec des API tierces dans React en construisant une application web de taux de change de crypto-monnaies.

Mais ne vous arrêtez pas ici. Vous pouvez améliorer ce projet en ajoutant une fonctionnalité de nouvelles et en le stylisant à votre goût. De plus, vous pouvez décider de supporter plus de devises.

### Ressources supplémentaires

* [Documentation React-query](https://tanstack.com/query/v3/docs/react/guides/paginated-queries)
    
* [Bibliothèque d'interface utilisateur Ant Design](https://ant.design/components)