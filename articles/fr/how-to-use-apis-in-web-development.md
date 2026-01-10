---
title: Comment utiliser les API Web dans vos projets de codage
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-08-08T16:27:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-apis-in-web-development
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/APIs.jpg
tags:
- name: api
  slug: api
- name: Web Development
  slug: web-development
seo_title: Comment utiliser les API Web dans vos projets de codage
seo_desc: "By Juliet Ofoegbu\nAs a developer, what comes to mind when you hear the\
  \ word \"API\"? For me, I think of the word \"connector\", something that connects\
  \ one thing to another. \nSo, what exactly is an API? API stands for Application\
  \ Programming Interface. A..."
---

Par Juliet Ofoegbu

En tant que développeur, à quoi pensez-vous lorsque vous entendez le mot "API" ? Pour moi, je pense au mot "connecteur", quelque chose qui relie une chose à une autre. 

Alors, qu'est-ce qu'une API exactement ? [API signifie Application Programming Interface](https://www.freecodecamp.org/news/how-apis-work/). Les API connectent différentes applications logicielles, sites web et services web et leur permettent de partager des informations et d'interagir les unes avec les autres. 

Dans ce tutoriel, vous apprendrez ce que sont les API Web et pourquoi elles sont utiles. Ensuite, vous verrez comment les implémenter dans un projet React. Pour suivre cet article, vous n'aurez besoin que de quelques connaissances de base en codage.

## Qu'est-ce que les API Web ?

Les API Web permettent à différentes applications logicielles de communiquer et d'interagir les unes avec les autres via Internet. Ces API donnent aux développeurs la possibilité d'accéder à des données externes provenant de fournisseurs tiers comme les plateformes de passerelles de paiement, les plateformes de médias sociaux, les services météorologiques, les plateformes de streaming vidéo, les plateformes de cryptomonnaies, et ainsi de suite.

Imaginons que vous êtes sur le point de quitter la maison et que vous êtes sceptique quant à la météo. Vous prenez votre téléphone et ouvrez l'application météo pour vérifier quel temps il fera ce jour-là. 

N'oubliez pas qu'il y a beaucoup de personnes comme vous qui vérifieront également la météo sur leur téléphone ce jour-là. Elles peuvent se trouver dans différents endroits et vouloir vérifier quel temps il fera spécifiquement chez elles. 

Ces applications météo installées sur les téléphones des gens ne stockent pas toutes les données météorologiques dont tout le monde a besoin chaque jour. Au lieu de cela, elles utilisent une API pour se connecter à un service météo distant sur Internet. L'API donne à l'application accès aux dernières informations météorologiques comme la température, l'humidité et les prévisions météorologiques, et elle peut ensuite afficher ces informations sur l'application ou vous dire quel temps il fait ou fera.

Les API sont utilisées pratiquement partout, de la banque aux médias sociaux, en passant par la musique et le streaming vidéo, ainsi que beaucoup d'autres choses sur Internet. 

Les développeurs web s'appuient sur des données externes lors de la création d'applications web pour améliorer la fonctionnalité de leurs applications et créer une excellente expérience utilisateur pour leurs utilisateurs. 

Dans cet article, nous explorerons les avantages et les cas d'utilisation des API web dans le développement. Nous passerons également en revue les étapes de base pour intégrer une API dans une application. Prêt à plonger ? Commençons.

## Avantages de l'utilisation des API

Il y a certains avantages à utiliser des API dans la construction d'applications. Parlons-en maintenant.

### Expérience utilisateur améliorée

Les API Web améliorent l'expérience des utilisateurs en leur offrant des services comme des options de connexion aux médias sociaux, des services de géolocalisation, des prévisions météorologiques, et ainsi de suite. 

Maintenant, imaginez une situation où les utilisateurs visitent votre application logistique et ne peuvent pas effectuer des opérations complexes comme le suivi de leurs marchandises ou l'utilisation des fonctionnalités de carte. Il n'y a que des données statiques présentes. Cela ne ressemble pas à une application qui offre une bonne expérience aux utilisateurs.

C'est là que les API Web interviennent et vous permettent de fournir ces services à vos utilisateurs.

### Réduction du temps de développement

Les développeurs peuvent utiliser des API existantes pour créer des applications web avec des fonctionnalités spécifiques au lieu de les construire à partir de zéro. 

Par exemple, supposons que je veux créer une application web de commande de nourriture. J'aurais besoin d'avoir accès à une liste de plats que je souhaite proposer. Si aucune API n'était disponible sur Internet, je devrais la construire à partir de zéro ou au moins créer une base de données d'articles alimentaires directement sur mon application. 

Heureusement, il existe une liste d'[API alimentaires](https://rapidapi.com/collection/food-apis) qui rendra cela plus facile et plus rapide pour moi, afin que je n'aie pas à perdre du temps et des efforts à construire cette fonctionnalité complexe à partir de zéro. Je vais simplement me concentrer sur les aspects principaux de mon application web. C'est un autre avantage des API web dans le développement.

### Applications enrichies

Vous devrez souvent construire des applications qui fournissent des données en temps réel et à jour provenant de diverses sources afin d'enrichir vos applications. Les API peuvent vous fournir des données en temps réel sur les conditions et prévisions météorologiques, les événements sportifs, et ainsi de suite. 

Des API comme [OpenWeatherMap](https://openweathermap.org/), [SportsPageFeed](https://rapidapi.com/SportspageFeeds/api/sportspage-feeds/), et [Amazon Price](https://rapidapi.com/ajmorenodelarosa/api/amazon-price1/) ne sont que quelques exemples d'API en temps réel disponibles sur Internet. Il existe même quelques API en temps réel pour obtenir des mises à jour de prix en temps réel pour les cryptomonnaies. 

### Rester à jour

Les utilisateurs de vos applications web doivent rester informés des actualités, des prévisions météorologiques ou des mises à jour. Maintenant, si vous construisez une application avec des données statiques qui peuvent devenir obsolètes, cela pourrait poser un problème.

Pour vous assurer que les utilisateurs continuent à utiliser votre application, vous devrez revenir à votre base de code de développement et y apporter les modifications nécessaires. 

Mais si vous récupérez des données à partir d'une API, ces modifications des données sont automatiquement mises à jour sur votre application. Cela est dû au fait que les API tierces reçoivent souvent des mises à jour et des améliorations, et ainsi l'application bénéficie des fonctionnalités et mises à jour supplémentaires.

## Cas d'utilisation des API Web dans le développement Web

Ici, je vais discuter de quelques cas d'utilisation courants des API Web dans la construction d'applications Web.

### Passerelles de paiement

Lors de la construction d'un site web ou d'une application de commerce électronique, ou de toute application qui nécessite essentiellement que les utilisateurs effectuent des paiements, des API de paiement comme Paystack, Paypal et Stripe permettent aux développeurs d'intégrer une méthode de traitement des paiements sécurisée dans leurs applications.

### Intégration des médias sociaux

Je ne suis pas sûr pour vous, mais lorsque je visite une application qui nécessite que je m'inscrive et me connecte, je préfère pouvoir me connecter en utilisant une plateforme de médias sociaux ou Google. Les sites de médias sociaux tels que Twitter, Facebook et Instagram permettent aux développeurs d'inclure des options de connexion aux médias sociaux et des boutons de partage dans leurs applications en utilisant des API.

### Services météorologiques

Les API météorologiques fournissent des informations météorologiques en temps réel pour diverses régions géographiques. Vous pouvez utiliser ces API pour créer un site web ou une application fonctionnelle, comme une application météo.

### Streaming vidéo et audio

Des plateformes comme YouTube et Vimeo fournissent des API qui permettent aux développeurs d'intégrer du contenu vidéo et audio dans leurs applications web. 

Supposons que vous souhaitez créer un clone de Spotify. Vous ne pouvez certainement pas entrer toutes les musiques disponibles, une chanson après l'autre, dans l'application. Ce serait stressant et presque impossible, compte tenu des millions de chansons disponibles en ligne. 

Spotify fournit une API qui vous permet de simplement implémenter cette fonctionnalité en récupérant des données à partir d'un point de terminaison API.

### Intégration du service de messagerie

Vous avez peut-être rencontré un site web ou une application où les utilisateurs peuvent envoyer des e-mails directement depuis l'application. Vous pouvez utiliser des API de service de messagerie comme Emailjs, Sendgrid et Mailchimp pour implémenter cette fonctionnalité. 

Cela peut être utile lors de la création d'un portfolio, par exemple, car vous pouvez créer un formulaire "Contactez-moi" à partir duquel les clients potentiels peuvent vous envoyer un message pour demander vos services. Ce message, ainsi que le nom et l'e-mail de l'expéditeur, sera envoyé directement à votre adresse e-mail spécifiée.

### Géolocalisation et cartographie

Les développeurs peuvent intégrer la géolocalisation et des cartes interactives dans leurs applications en utilisant des API connexes sur Internet comme l'API Google. 

Par exemple, supposons que vous créez un site web pour un restaurant qui fonctionne hors ligne. Certains utilisateurs peuvent choisir de visiter l'emplacement en personne plutôt que de commander en ligne. Vous pouvez intégrer une API de carte interactive dans votre site web afin que les utilisateurs puissent localiser facilement le restaurant.

### Accès au contenu

Souhaitez-vous créer des applications qui récupèrent des données d'actualités provenant de divers secteurs ? Il existe de nombreuses API qui fournissent ces informations et vous pouvez les utiliser pour créer des applications web interactives. 

Par exemple, supposons que vous publiez des articles sur des plateformes comme Dev.to, Medium ou Hashnode et que vous souhaitez afficher votre travail sur votre portfolio. Au lieu d'ajouter manuellement vos blogs à votre site, vous pouvez utiliser les API de la plateforme pour les récupérer et les ajouter à votre site de portfolio.

## Comment implémenter les API Web dans vos projets

Maintenant, parlons de la manière dont vous pouvez implémenter des API dans vos applications. Je vais d'abord passer en revue le processus général, puis nous examinerons un exemple concret.

Tout d'abord, vous devrez vous inscrire sur la plateforme spécifique du fournisseur d'API que vous prévoyez d'utiliser afin d'obtenir une clé API ou un jeton d'accès. Il s'agit d'un identifiant unique donné à chaque utilisateur/développeur. 

Avant d'intégrer l'outil de traitement des paiements Paystack, par exemple, vous devrez vous inscrire et vous connecter à la plateforme avant d'obtenir accès à la clé API dans les paramètres de votre profil. 

Ces clés API peuvent être publiques ou privées. Elles peuvent également être en mode test ou en direct, comme Paystack. L'image ci-dessous montre la page des paramètres de la plateforme Paystack, où vous pouvez obtenir une clé API.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Developers---Paystack---Google-Chrome-02_08_2023-15_02_25.jpg)
_Page des paramètres de Paystack_

Ensuite, vous commencerez à faire des requêtes API. Vous devrez utiliser différentes méthodes de requête HTTP comme GET, POST, PUT et DELETE pour interagir avec ces points de terminaison API et récupérer des données de l'API. 

Enfin, vous devrez analyser les réponses de l'API. Lorsque ces données sont récupérées, les réponses de l'API sont souvent au format JSON ou XML. Vous devrez analyser ces réponses afin d'extraire les informations pertinentes pour vos applications. 

Après avoir extrait les données, selon ce que vous construisez, vous pouvez ensuite les rendre disponibles pour que les utilisateurs les utilisent et effectuent certaines opérations sur votre application.

### Exemple pratique d'utilisation des API Web

Pour vous donner une démonstration rapide de la manière dont vous pouvez utiliser les API Web dans le monde réel, je vais créer une application de base de recettes de cuisine. Cette application effectuera une opération simple de récupération de certaines données relatives aux aliments que les utilisateurs recherchent. 

Pour suivre cet exemple, vous devrez vous inscrire ou vous connecter à [Edamam](https://www.edamam.com/) (c'est gratuit). Il s'agit d'un site qui dispose d'une API de base de données alimentaires, d'une API de recherche de recettes, et ainsi de suite.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Edamam---Food-Database-API--Nutrition-API-and-Recipe-API---Google-Chrome-06_08_2023-11_36_15.png)

Après vous être connecté avec succès au site, allez dans votre tableau de bord et sélectionnez l'onglet "Applications". Cliquez sur le bouton "view" pour afficher votre **ID d'application** et votre **clé d'application**. Vous utiliserez ces valeurs dans le code principal, alors gardez-les à portée de main.

Démarrez un projet dans votre éditeur de code. Dans ce cas, nous utiliserons une application React configurée avec npm ou Vite. 

Vous utiliserez deux fichiers pour cet exemple. L'un est le fichier App.js ou App.jsx qui vient par défaut dans React. Vous créerez l'autre fichier/composant vous-même. Vous pouvez lui donner le nom que vous voulez. J'ai nommé le mien Recipe.js.

### Comment construire le composant App

Collez les lignes de code ci-dessous dans votre composant **App**. Je vais expliquer ce que signifient ces lignes de code ci-dessous :

```js
import React, { useState, useEffect } from "react";
import Recipe from "./Recipe";

function App() {
  const APP_ID = "Votre_ID_API";
  const APP_KEY = "Votre_Cle_API";

  const [recipes, setRecipes] = useState([]);
  const [search, setSearch] = useState("");
  const [query, setQuery] = useState("Riz");


  useEffect(() => {
    const getRecipes = async () => {
    const response = await fetch(`https://api.edamam.com/search?q=${query}&app_id=${APP_ID}&app_key=${APP_KEY}`
      );
      const data = await response.json();
      setRecipes(data.hits);
      console.log(data.hits);
    };
    getRecipes();
  }, [query]);

  const updateSearch = (e) => {
    setSearch(e.target.value);
  };


  const getSearch = (e) => {
    e.preventDefault();
    setQuery(search);
    setSearch("");
  };

  return (
    <>
      <section>
        <form onSubmit={getSearch}>
          <input
            type="text"
            value={search}
            onChange={updateSearch}
            placeholder="Saisir un aliment" />
          <button type="submit">
            Rechercher
          </button>
        </form>

        <article>
          {recipes.map((recipe) => (
            <Recipe
              key={recipe.recipe.label}
              title={recipe.recipe.label}
              image={recipe.recipe.image}
              ingredients={recipe.recipe.ingredients}
              cuisine={recipe.recipe.cuisineType}
              dish={recipe.recipe.dishType}
            />
          ))}
        </article>
      </section>
    </>
  );
}

export default App;
```

Alors, que fait le code ci-dessus ? Ce composant App est le composant principal pour rendre l'ensemble de l'application alimentaire.

* Tout d'abord, nous importons les hooks `useState` et `useEffect` car ils sont utilisés pour gérer l'état et le cycle de vie de l'application.
* Rappelez-vous l'ID de l'API et la clé de l'API que vous avez obtenus sur le site Web d'Edamam sur votre profil, car vous en aurez besoin maintenant. Remplacez ceux dans le code ci-dessus par vos propres valeurs.
* Ensuite, nous allons définir trois états. Le premier état, `recipes`, sera utilisé pour stocker un tableau d'objets de recettes qui seront récupérés depuis l'API Edamam. Le deuxième état, `search`, stockera l'entrée de l'utilisateur pour rechercher une recette alimentaire particulière. Le dernier état, `query`, représentera la chaîne de requête qui sera utilisée pour récupérer la recette alimentaire en fonction de l'entrée des utilisateurs.
* Le hook `useEffect` sera implémenté ici pour récupérer les recettes alimentaires de l'API lorsque l'état `query` change. Il envoie une requête à l'API avec l'entrée de l'utilisateur (stockée dans l'état `query`) et définit les recettes récupérées dans l'état `recipes`.
* La fonction `updateSearch` met à jour l'état de recherche chaque fois que l'utilisateur tape quelque chose dans le champ de saisie de recherche. La fonction `getSearch` est déclenchée lorsque l'utilisateur soumet le formulaire, et elle met à jour l'état `query` avec la valeur de recherche pour récupérer les recettes appropriées.
* Ce composant App va ensuite parcourir l'état `recipes` en utilisant la fonction map et rendre le composant Recipe pour chaque recette. Ensuite, il transmet les données de la recette en tant que props au composant. Le composant Recipe a été importé dans la deuxième ligne de code.

### Comment fonctionne l'API

Alors, comment fonctionne cette API qui nous permet de nous y connecter et de récupérer des informations ? Passons en revue comment nous utilisons cette API externe fournie par Edamam pour récupérer les données de recettes dans l'application.

Tout d'abord, nous avons notre point de terminaison API. Un point de terminaison est comme une URL que vous pouvez utiliser pour faire des requêtes afin d'obtenir des informations sur quelque chose. Dans cette application simple, le point de terminaison API est composé de l'`APP_ID` et de l'`APP_KEY` (jetons d'authentification) ainsi que de la requête de recherche de l'utilisateur – [`https://api.edamam.com/search?q=${query}&app_id=${APP_ID}&app_key=${APP_KEY}`](https://api.edamam.com/search?q=$%7Bquery%7D&app_id=$%7BAPP_ID%7D&app_key=$%7BAPP_KEY%7D). 

Lorsque l'utilisateur entre un élément de recherche et le soumet, l'application envoie une requête à ce point de terminaison.

L'application qui envoie cette requête demande simplement au serveur, dans ce cas, le serveur Edamam, de fournir une réponse contenant les données de recette pour l'élément alimentaire entré. 

Vous pouvez utiliser une fonction `fetch` pour faire cette requête. Dans cette application, la fonction `getRecipes` utilise l'état `query` pour spécifier le type de recettes à récupérer.

Ensuite, le serveur API Edamam traite cette requête et envoie une réponse contenant les données demandées. Les réponses API viennent sous différentes formes comme JSON, XML, CSV, et ainsi de suite. Dans ce cas, la réponse est au format JSON, et elle contient un tableau d'objets de recettes.

La dernière étape implique la mise à jour de l'état. La fonction `setRecipes` est utilisée pour mettre à jour l'état `recipes` avec un tableau d'objets de recettes que la réponse API fournit. Le composant est réaffiché, et l'application affiche ensuite les informations de recette mises à jour sur la page.  

### Comment construire le composant Recipe

Passons maintenant au composant **Recipe**. Ce composant affiche les détails de la recette alimentaire qui sera récupérée de l'API. 

```js
import React from "react";

const Recipe = ({ image, title, cuisine, dish, ingredients }) => {
  return (
    <>
      <section>
          <div>
            <article>
              <figure>
                <img src={image} alt="nourriture" />
              </figure>
              <div>
                <h2>{title}</h2>
                <p>Type de cuisine : {cuisine}</p>
                <p>Type de plat : {dish}</p>
                <div>
                  <p>Ingrédients :</p>
                  <ol>
                    {ingredients.map((ingredient) => (
                      <li>• {ingredient.text}</li>
                    ))}
                  </ol>
                </div>
              </div>
            </article>
          </div>
      </section>
    </>
  );
};

export default Recipe;
```

* Ce composant prend certaines props en entrée : image, title, cuisine, dish et ingredients. Chacune d'elles contient des détails de la recette alimentaire.
* Le composant Recipe affiche ensuite les détails de la recette en utilisant ces props. Chaque recette est affichée sous forme de carte avec les informations suivantes : l'image de la recette, le titre de la recette, le type de cuisine et de plat, et les ingrédients affichés sous forme de liste ordonnée avec chaque ingrédient en tant qu'élément de liste.

En résumé, le composant App utilise le composant Recipe pour afficher les recettes alimentaires en fonction de l'entrée de recherche de l'utilisateur. Chaque recette est affichée sous forme de carte avec ses détails correspondants. Et c'est tout. C'est ainsi que l'on construit une application web simple de recettes alimentaires. 

### Ajouter un peu de style (facultatif)

Si vous avez suivi pour construire cette application simple, votre application ne sera pas très belle car aucun style n'a été ajouté. Allez-y et stylez votre application comme vous le souhaitez. Voici à quoi ressemble la mienne après le style :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/food-recipe.png)

La raison pour laquelle mon application affiche par défaut des recettes de riz est que dans le composant App où j'ai défini l'état `query`, j'ai défini la valeur initiale de l'état à "Riz". Vous pouvez la définir à n'importe quel plat que vous souhaitez comme des nouilles, des hamburgers, et ainsi de suite.

Il s'agit d'une application simple démontrant comment utiliser les API dans une application. En tant que développeurs, vous devrez peut-être construire des projets plus complexes qui nécessiteront de récupérer des données à partir d'une API. L'exemple ci-dessus devrait vous donner une idée de la manière dont vous pouvez le faire.

Il est important de noter que les API Web peuvent être intégrées dans d'autres types d'applications en plus des applications Web. Vous pouvez également les utiliser dans des applications mobiles et des applications de bureau. 

## Conclusion

Savoir comment utiliser les API Web est un concept essentiel pour les développeurs à apprendre afin de construire des applications interactives qui améliorent l'expérience utilisateur. 

Dans cet article, vous avez appris les avantages et les cas d'utilisation des API Web, et comment implémenter des API dans le développement. Vous pouvez donc maintenant construire des applications qui intègrent des API. 

Une compétence importante pour les développeurs est la capacité à lire et à comprendre la documentation des API, car cela vous donnera une idée de la manière d'intégrer une API particulière dans votre projet.

Vous cherchez une vidéo YouTube qui couvre tout ce qu'un développeur backend, frontend, mobile ou d'applications doit savoir sur les API ? Consultez cette vidéo freeCodeCamp sur [YouTube](https://www.youtube.com/watch?v=WXsD0ZgxjRw). 

Bon codage !