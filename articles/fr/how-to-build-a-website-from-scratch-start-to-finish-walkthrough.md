---
title: Comment construire un site web à partir de zéro – Guide complet de A à Z
subtitle: ''
author: Kunal Nalawade
co_authors: []
series: null
date: '2025-04-28T19:21:02.308Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-website-from-scratch-start-to-finish-walkthrough
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745260046049/62b5c730-dc06-49de-8bdd-2cd44facb9e9.png
tags:
- name: Web Development
  slug: web-development
seo_title: Comment construire un site web à partir de zéro – Guide complet de A à
  Z
seo_desc: 'Hi, fellow developers!

  Building a website can feel overwhelming at first – especially when you''re staring
  at a blank HTML file, wondering how it ever turns into a real website on the internet.
  If you''re new to web development, you''ve probably asked y...'
---

Bonjour, chers développeurs !

Construire un site web peut sembler intimidant au début – surtout lorsque vous regardez un fichier HTML vide, en vous demandant comment il peut se transformer en un vrai site web sur internet. Si vous êtes nouveau dans le développement web, vous vous êtes probablement demandé : *"Par où commencer ?"*

Eh bien, ce tutoriel est là pour vous guider tout au long de ce voyage. Nous allons construire un site web simple à partir de zéro et passer en revue chaque étape – jusqu'à son déploiement sur internet.

Commençons !

## Table des matières

1. [Commencer avec l'idée du site web](#heading-commencer-avec-lidee-du-site-web)
    
2. [Comment configurer le projet](#heading-comment-configurer-le-projet)
    
3. [Comment construire le site web](#heading-comment-construire-le-site-web)
    
4. [Comment tester le code](#heading-comment-tester-le-code)
    
5. [Comment pousser votre code vers le contrôle de version](#heading-comment-pousser-votre-code-vers-le-controle-de-version)
    
6. [Déploiement et hébergement](#heading-deploiement-et-hebergement)
    

## Commencer avec l'idée du site web

Nous allons construire une application météo simple qui affiche la météo du jour dans votre ville. Elle aura les fonctionnalités suivantes :

* Recherche par nom de ville : L'utilisateur entre le nom de la ville et récupère les informations météo
    
* Affichage des informations météo suivantes : température, condition météo et vitesse du vent
    
* Gestion des erreurs
    

Il s'agit d'un site web simple avec des fonctionnalités assez basiques, et il devrait être relativement facile à construire.

Avant de commencer, passons en revue quelques prérequis. Je suppose que vous êtes déjà familiarisé avec les bases de HTML, CSS et JavaScript. Connaître Git serait utile, mais ce n'est pas nécessaire – vous pouvez toujours suivre les étapes de cet article.

## Comment configurer le projet

Commençons par configurer le projet. Pour garder les choses simples, nous allons utiliser uniquement HTML, CSS et JavaScript pour construire le site web. Donc, créons les fichiers suivants :

```bash
weather-app/
├── index.html
├── style.css
└── script.js
```

Ensuite, pour obtenir les données météo, nous allons utiliser une API météo open-source de [Open-Meteo](https://open-meteo.com), car elle est gratuite et ne nécessite pas de clé API. Elle nous fournira la température, la vitesse du vent et les conditions météo.

Avant de plonger vraiment dans le sujet, assurez-vous d'avoir Git installé sur votre système. Si vous n'avez pas Git, vous pouvez vous référer à [Git SCM](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) pour un guide d'installation sur Mac et Windows. Si vous n'êtes pas familiarisé avec Git, consultez les guides suivants pour commencer :

* [Apprendre les bases de Git en moins de 10 minutes](https://www.freecodecamp.org/news/learn-the-basics-of-git-in-under-10-minutes-da548267cc91/)
    
* [Livre complet sur Git et GitHub + bases du contrôle de version](https://www.freecodecamp.org/news/gitting-things-done-book/)
    
* [Commencer avec GitHub](https://docs.github.com/en/get-started/start-your-journey)
    

Maintenant, vous pouvez créer et initialiser votre dépôt Git. Pour initialiser un dépôt local, exécutez la commande suivante à l'intérieur de votre répertoire de projet :

```bash
git init
```

Ensuite, allez sur GitHub et créez un nouveau dépôt avec le même nom que votre projet. Référez-vous au [guide de démarrage rapide](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories) si vous n'êtes pas familiarisé avec le processus. Exécutez les commandes affichées à l'écran une fois que vous avez créé le dépôt.

Une fois que vous avez terminé ces étapes, nous sommes prêts à commencer le processus de développement.

## Comment construire le site web

Dans cette phase, nous allons développer ou coder notre site web. En regardant les designs et les exigences, nous déciderons comment aborder le développement de chaque composant.

Il s'agit d'un site web simple et petit avec peu d'exigences. Nous n'utiliserons donc aucun framework, juste du HTML, CSS et JavaScript simples. Mais, selon la complexité des exigences, vous pourriez décider d'utiliser des frameworks comme React, Angular, etc.

Tout d'abord, créons une mise en page de base de la page web avec HTML :

```xml
 <div class="container">
      <h1>Application Météo</h1>
      <div class="searchContainer">
        <input
          class="inputField"
          id="cityField"
          placeholder="Entrez le nom de la ville..."
          type="text"
        />
        <button id="searchBtn">Rechercher</button>
      </div>
      <div id="weatherContainer">
        <h2 id="cityName"></h2>
        <p id="temperature"></p>
        <p id="condition"></p>
        <p id="windSpeed"></p>
      </div>
      <p id="errorMessage"></p>
    </div>
    <script src="script.js"></script>
```

Nous avons ajouté les éléments suivants :

* Un conteneur de recherche qui contiendra notre champ de recherche avec une entrée pour saisir le nom de la ville, et un bouton Rechercher
    
* Un autre conteneur qui affichera les informations météo ou un message d'erreur une fois que l'utilisateur clique sur Rechercher
    

Ensuite, stylisons-le avec CSS :

```css
.container {
  max-width: 400px;
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  margin: auto;
}

.searchContainer {
  margin: 20px 0;
}

.inputField {
  padding: 10px;
  width: 70%;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.searchBtn {
  padding: 10px;
  background: #007bff;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}

#weatherContainer {
  display: none; /* Masquer jusqu'à ce que les données soient disponibles pour l'affichage */
}

#errorMessage {
  color: red;
  font-weight: bold;
}
```

Avec HTML et CSS, nous avons construit un site web statique qui ressemble à ceci :

![Interface utilisateur statique rendue](https://cdn.hashnode.com/res/hashnode/image/upload/v1742722248758/46e8d7d8-c1dd-47d8-9697-03fb9d07229f.png align="center")

Maintenant, ajoutons quelques fonctionnalités avec JavaScript. Nous allons appeler les endpoints suivants :

* `/v1/search` pour obtenir la longitude et la latitude par nom de ville
    
* `v1/forecast` pour obtenir les informations météo
    

Tout d'abord, ajoutons un gestionnaire `onclick` à notre bouton :

```javascript
document.getElementById("searchBtn").addEventListener("click", () => {
  const city = document.getElementById("cityField").value.trim();
  if (city) {
    getCoordinates(city);
  } else {
    showError("Veuillez entrer un nom de ville");
  }
});
```

En cliquant sur le bouton de recherche, les deux API ci-dessus doivent être appelées, l'une après l'autre. Appelons la première API dans la méthode `getCoordinates` :

```javascript
async function getCoordinates(city) {
  showError("");
  try {
    const response = await fetch(
      `https://geocoding-api.open-meteo.com/v1/search?name=${city}&count=1`
    );

    if (!response.ok) {
      throw new Error("Ville non trouvée");
    }

    const data = await response.json();
    if (!data.results || data.results.length === 0) {
      throw new Error("Lieu non trouvé");
    }

    const { latitude, longitude, name, country } = data.results[0];
    getWeather(latitude, longitude, name, country);
  } catch (error) {
    showError(error.message);
  }
}
```

Ici, nous appelons la première API pour récupérer les coordonnées, et vérifions si la réponse est positive. Si ce n'est pas le cas, nous lançons une erreur et l'affichons dans le DOM. Si les coordonnées sont récupérées avec succès, nous passons à l'étape suivante et obtenons les données météo pour ces coordonnées :

```javascript
async function getWeather(latitude, longitude, city, country) {
  try {
    const response = await fetch(
      `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current_weather=true`
    );

    if (!response.ok) {
      throw new Error("Données météo non disponibles");
    }

    const data = await response.json();
    displayWeather(data.current_weather, city, country);
  } catch (error) {
    showError(error.message);
  }
}
```

Ici, nous faisons la même chose, gérons les erreurs et affichons les données météo à l'écran, dans la méthode `displayWeather` :

```javascript
function displayWeather(weather, city, country) {
  const weatherContainer = document.getElementById("weatherContainer");
  const cityHeader = document.getElementById("cityName");
  const temp = document.getElementById("temperature");
  const condition = document.getElementById("condition");
  const windSpeed = document.getElementById("windSpeed");

  const weatherCondition =
    weatherDescriptions[weather.weathercode] || "Condition inconnue";

  weatherContainer.style.display = "block";
  cityHeader.textContent = `${city}, ${country}`;
  temp.textContent = `Température : ${weather.temperature}°C`;
  condition.textContent = `Condition : ${weatherCondition}`;
  windSpeed.textContent = `Vitesse du vent : ${weather.windspeed} km/h`;
}
```

Ensuite, la méthode `showError` contient notre logique de gestion des erreurs. Elle affichera toute erreur à l'écran.

```javascript
function showError(message) {
  const weatherContainer = document.getElementById("weatherContainer");
  weatherContainer.style.display = "none";
  const errorPara = document.getElementById("errorMessage");
  errorPara.textContent = message;
}
```

Très bien, nous avons terminé la partie développement ! Maintenant, il est temps de tester notre code.

## Comment tester le code

Chaque fois que vous développez une fonctionnalité, vous voulez vous assurer de la tester minutieusement. Une façon de tester est de considérer toutes les façons dont un utilisateur pourrait interagir avec votre site web. Ensuite, vérifiez comment votre site web se comporte dans chaque scénario ou cas de test.

Tout d'abord, voyons si le site web fonctionne comme prévu lorsqu'un nom de ville valide est donné. Entrez un nom de ville et cliquez sur rechercher – il devrait afficher les informations météo comme ceci :

![Données météo visibles pour Mumbai](https://cdn.hashnode.com/res/hashnode/image/upload/v1743082937133/ab532ffe-2a48-4101-9d04-7c2eb10d944b.png align="center")

Ensuite, testons notre gestion des erreurs, en ajoutant du charabia dans l'entrée :

![Entrée charabia entraîne Lieu non trouvé](https://cdn.hashnode.com/res/hashnode/image/upload/v1743082992278/8b8629a4-db3a-45b6-87fd-295be4386941.png align="center")

Avec cette entrée, notre API échoue, et retourne l'erreur ci-dessus, qui est correctement affichée.

Rappelez-vous que notre site web est vraiment simple, donc nous n'avons pas beaucoup de cas de test. Mais dans un site web réel, une bonne pratique est de faire une liste de cas de test, et de tester votre site web contre chacun d'eux.

Dans ce contexte, nous effectuons des tests fonctionnels pour nous assurer que le site web se comporte comme prévu dans différents scénarios. Cela inclut le test des fonctionnalités principales comme la recherche d'une ville et la gestion des erreurs. Ce type de test est crucial car il vérifie que l'application effectue correctement ses fonctions prévues.

En plus de cela, vous pouvez effectuer d'autres types de tests sur un site web :

* Tests unitaires : Tester des composants individuels ou des morceaux de code en isolation
    
* Tests d'intégration : Tester les interactions entre différents composants du site web
    
* Tests de bout en bout : Tester l'ensemble du flux de l'application du début à la fin
    

Une fois que vous êtes sûr que le site web fonctionne comme prévu, il est temps de pousser votre code vers un dépôt distant comme GitHub et de le publier en production – c'est-à-dire sur internet.

## Comment pousser votre code vers le contrôle de version

Avant de continuer, vous vous demandez peut-être pourquoi le contrôle de version est important. Le contrôle de version vous aide à suivre les changements dans votre code de manière organisée. Voici les avantages :

* Si quelque chose ne fonctionne pas dans votre code, vous pouvez revenir à une version précédente si nécessaire.
    
* Votre projet est stocké en toute sécurité sur GitHub, donc vous ne perdrez pas votre progression.
    
* Avec les [branches](https://www.atlassian.com/git/tutorials/using-branches), vous pouvez travailler sur différentes fonctionnalités en même temps, sans qu'elles n'interfèrent les unes avec les autres, ou avec le code principal. Cela est utile surtout lorsqu'il y a plusieurs personnes travaillant sur le projet.
    
* Les plateformes de déploiement et d'hébergement comme Netlify s'intègrent parfaitement avec les systèmes de contrôle de version comme GitHub.
    

Poussons notre code vers GitHub maintenant. Assurez-vous d'avoir exécuté toutes les commandes qui sont affichées lorsque vous créez le dépôt pour la première fois.

Exécutez les commandes suivantes :

```bash
git add .
git commit -m "Ajout des informations météo avec appels API"
git push origin main
```

La première commande ajoute vos changements à la [zone de transit](https://git-scm.com/about/staging-area). La deuxième valide vos changements localement, tandis que la dernière les pousse vers le dépôt distant.

Ici, nous avons poussé le code directement vers `master`. Mais généralement, vous travaillerez sur une fonctionnalité dans une branche séparée et créerez une [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests#) (ou merge request), après quoi votre code peut être [fusionné](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request) dans la branche master/main.

Maintenant que votre code est poussé vers GitHub, nous allons passer au déploiement et à l'hébergement. Vous pouvez trouver le dépôt git de mon code [ici](https://github.com/KunalN25/test-weather-app).

## Déploiement et hébergement

Avant de plonger dans ces étapes, comprenons d'abord ce que signifient déploiement et hébergement. En termes simples, le déploiement consiste à prendre votre site web et à le mettre sur Internet, tandis que les services d'hébergement stockent votre site web pour s'assurer qu'il est accessible aux personnes en ligne.

Nous allons utiliser Netlify, une plateforme conviviale pour les débutants qui vous permet de déployer des sites web directement depuis votre dépôt GitHub. C'est parfait pour déployer des sites web simples construits avec HTML, CSS et JavaScript. Vous obtenez également une URL gratuite avec votre site web (ou vous pouvez payer pour un nom de domaine).

Pour commencer, visitez d'abord [netlify.com](https://www.netlify.com), et inscrivez-vous avec votre email ou votre compte GitHub. Une fois connecté, vous verrez une page d'accueil. Cliquez sur "Add new site" → "Import an existing project".

![Page d'accueil de Netlify](https://cdn.hashnode.com/res/hashnode/image/upload/v1744635933602/b092d758-ceec-4980-a36f-7e2d863ff5b6.png align="center")

Ensuite, connectez votre compte GitHub en autorisant Netlify à accéder à vos dépôts GitHub. Il affichera une liste de tous vos dépôts GitHub. Recherchez votre dépôt `test-weather-app`, ou quel que soit le nom que vous lui avez donné, et sélectionnez-le.

Ensuite, vous serez accueilli avec la page suivante pour entrer les configurations. Comme notre projet n'utilise aucun framework, nous n'avons pas besoin de spécifier de commandes de construction. Donc, nous laissons la plupart des champs vides et cliquons sur "Deploy".

![Configuration du site web](https://cdn.hashnode.com/res/hashnode/image/upload/v1744635796692/3176dc6c-5f3c-4abf-948f-dda44536dce0.png align="center")

Netlify déployera votre site en quelques minutes et vous fournira le lien. Vous pouvez trouver cet exemple de site web en visitant le lien suivant :

[https://testweatherapp11.netlify.app](https://testweatherapp11.netlify.app)

Netlify vous donnera également la possibilité d'acheter un domaine personnalisé. Donc, si vous visez à construire un site web réel pour en tirer profit, vous pouvez utiliser cette option.

Si vous souhaitez apporter des modifications, Netlify les déployera automatiquement lorsque vous les pousserez vers GitHub.

## Conclusion

Et voilà, votre site web est en ligne sur internet. C'est tout ce qu'il a fallu. Vous venez d'écrire du code sur votre machine locale, de construire une page web simple à partir de zéro, et maintenant elle est en ligne sur internet pour que d'autres personnes l'utilisent. N'est-ce pas formidable !

Maintenant que vous avez appris à construire un site web à partir de zéro et à le déployer sur internet, voici quelques points supplémentaires à retenir :

* Le développement de sites web n'est pas encore terminé. À mesure que vous continuez à construire des choses, votre site web évoluera. Vous explorerez différents designs, corrigerez des bugs et améliorerez les fonctionnalités en fonction des retours.
    
* À mesure que votre site web grandit, vous devrez également penser à ses performances, avec une utilisation accrue, et à sa sécurité, pour vous protéger, vous et vos utilisateurs, contre les attaques.
    
* J'ai décrit un processus très simplifié. Habituellement, il y a une collecte des exigences, une création de design de site web et des estimations avant même de commencer le développement.
    
* Vous collaborerez également avec d'autres personnes telles que des designers, des ingénieurs backend, des chefs de produit et des parties prenantes.
    
* Souvent, un site web est développé par incréments, c'est-à-dire qu'une version basique du site web avec des fonctionnalités de base sera publiée en premier, comme nous l'avons fait. Ensuite, pour chaque fonctionnalité, tout le processus, de la conception à la développement et aux tests jusqu'au déploiement, est suivi.
    
* Pour rendre votre site web utilisable par tous, y compris les personnes ayant divers handicaps, vous voudrez suivre les meilleures pratiques d'accessibilité web. Il existe un certain nombre de pratiques que vous devriez suivre pendant la phase de développement. Je les ai décrites en détail dans mon [manuel d'accessibilité web ici](https://www.freecodecamp.org/news/the-web-accessibility-handbook/).
    

## Conclusion

Le voyage de la construction d'un site web à partir de zéro et de sa mise en ligne sur internet est gratifiant à bien des égards. À travers ce processus, vous acquérez des compétences précieuses en développement web, et vous vous améliorez dans l'utilisation du contrôle de version pour suivre votre travail. Et partager ce que vous avez construit avec la communauté est si satisfaisant.

Dans ce tutoriel, j'ai expliqué un processus très simplifié, mais rappelez-vous que les projets réels impliquent souvent plus de complexité, y compris la collaboration, l'optimisation des performances et les considérations de sécurité.

À mesure que vous continuez à développer vos compétences, vous serez confronté à de nouveaux défis et aurez de grandes opportunités pour améliorer la fonctionnalité et l'expérience utilisateur de votre site web. Embrassez le processus d'apprentissage et savourez la satisfaction de voir votre création prendre vie sur internet. Bon codage !

Si vous avez des questions ou besoin de clarifications supplémentaires, n'hésitez pas à demander. Vos retours sont toujours appréciés et valorisés ! Connectez-vous avec moi sur [Twitter](https://x.com/i/flow/login?redirect_after_login=%2FKunal_N25) pour plus de mises à jour et de discussions. Merci d'avoir lu, et j'ai hâte de vous voir la prochaine fois !