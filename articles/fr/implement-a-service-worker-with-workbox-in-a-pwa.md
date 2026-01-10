---
title: Comment implémenter un Service Worker avec WorkBox dans une Progressive Web
  App
subtitle: ''
author: Damilola Oniyide
co_authors: []
series: null
date: '2025-06-23T13:57:56.601Z'
originalURL: https://freecodecamp.org/news/implement-a-service-worker-with-workbox-in-a-pwa
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1750687028879/b12e57cb-290a-4562-8584-95eb5713a871.png
tags:
- name: PWA
  slug: pwa
- name: HTML5
  slug: html5
- name: CSS
  slug: css
- name: Service Workers
  slug: service-workers
- name: workbox
  slug: workbox
- name: progressive web apps
  slug: progressive-web-apps
- name: JavaScript
  slug: javascript
- name: manifest
  slug: manifest
seo_title: Comment implémenter un Service Worker avec WorkBox dans une Progressive
  Web App
seo_desc: 'Imagine having a web app that looks and feels just like a native mobile
  app. It launches from your home screen, runs in full-screen mode, and responds smoothly
  to your interactions. But here’s the surprising part: it wasn’t downloaded from
  an app sto...'
---

Imaginez avoir une application web qui ressemble et se comporte comme une application mobile native. Elle se lance depuis votre écran d'accueil, s'exécute en mode plein écran et répond de manière fluide à vos interactions. Mais voici la partie surprenante : elle n'a pas été téléchargée depuis un magasin d'applications. C'est une Progressive Web App (PWA).

Les PWAs apportent la puissance du web à vos doigts avec l'expérience d'une application mobile. Encore mieux ? Si vous perdez votre connexion Internet en déplacement, l'application peut toujours fonctionner, affichant vos données précédemment chargées et obtenant des mises à jour une fois que vous êtes de retour en ligne.

Dans ce tutoriel, vous apprendrez à implémenter un service worker avec WorkBox dans une application météo en utilisant HTML, CSS et JavaScript. Nous commencerons par comprendre ce qu'est une PWA, les composants principaux derrière la scène, en particulier les service workers, et comment utiliser Workbox pour supercharger votre application avec des capacités hors ligne.

## Table des matières

* [Ce que nous allons couvrir](#heading-ce-que-nous-allons-couvrir)
    
* [Qu'est-ce qu'une Progressive Web App (PWA) ?](#heading-quest-ce-quune-progressive-web-app-pwa)
    
* [Qu'est-ce qui rend une application web "Progressive" ?](#heading-quest-ce-qui-rend-une-application-web-progressive)
    
* [Composants d'une PWA](#heading-composants-dune-pwa)
    
* [Qu'est-ce qu'un Service Worker dans une PWA ?](#heading-quest-ce-quun-service-worker-dans-une-pwa)
    
* [Pourquoi utiliser Workbox au lieu de Service Workers manuels ?](#heading-pourquoi-utiliser-workbox-au-lieu-de-service-workers-manuels)
    
* [Introduction à WorkBox](#heading-introduction-a-workbox)
    
* [Configuration du projet](#heading-configuration-du-projet)
    
* [Création de la structure HTML hors ligne](#heading-creation-de-la-structure-html-hors-ligne)
    
* [Stylisation avec CSS](#heading-stylisation-avec-css)
    
* [Comment configurer app.js et config.js](#heading-comment-configurer-appjs-et-configjs)
    
* [Comment créer un fichier Manifest](#heading-comment-creer-un-fichier-manifest)
    
* [Comment ajouter WorkBox à votre fichier service-worker.js](#heading-comment-ajouter-workbox-a-votre-fichier-service-workerjs)
    
* [Comment créer votre Service Worker dans le fichier service-worker.js](#heading-comment-creer-votre-service-worker-dans-le-fichier-service-workerjs)
    
* [Comment configurer l'installation de l'application](#heading-comment-configurer-linstallation-de-lapplication)
    
* [Comment installer l'application météo](#heading-comment-installer-lapplication-meteo)
    
* [Conclusion](#heading-conclusion)
    

## Ce que nous allons couvrir

* **Configuration du projet** : Nous allons construire une simple application météo en utilisant HTML, CSS et JavaScript. Cette approche est parfaite pour ce tutoriel car elle garde les choses simples et accessibles tout en se concentrant sur les concepts principaux des PWA sans la complexité supplémentaire des frameworks comme React ou Vue.
    
* **Transformer l'application en PWA** : Ensuite, nous allons passer en revue le concept de Progressive Web App, en couvrant les fonctionnalités clés et les meilleures pratiques des PWA.
    
* **Implémentation du Service Worker via WorkBox** : Enfin, nous allons approfondir le fonctionnement des service workers et explorer pourquoi l'utilisation de Workbox simplifie le processus.
    

Voici à quoi ressemblera l'application finale :

![Interface de l'application Weatherly montrant la météo de Tokyo avec une température de 24°C, des nuages couverts, une fonctionnalité de recherche de ville et un bouton de services de localisation](https://cdn.hashnode.com/res/hashnode/image/upload/v1747272664555/8ec876bc-0881-4a63-8010-02136de91db3.png align="center")

### **Public cible**

Ce tutoriel s'adresse aux développeurs web de tous niveaux. Que vous soyez nouveau dans les Progressive Web Apps (PWA) ou que vous commeniez à explorer les service workers, ce guide vous accompagnera à travers les concepts principaux et démontrera pourquoi l'utilisation d'une bibliothèque soutenue par Google comme Workbox pour implémenter des service workers peut être plus efficace qu'une implémentation manuelle.

### **Prérequis**

Avant de commencer

1. Obtenez une clé API gratuite sur le site [OpenWeatherAPI](https://openweathermap.org/)
    
2. Assurez-vous d'être familier avec HTML, CSS et JavaScript.
    
3. Si vous êtes nouveau dans les PWA, vous pourriez vouloir lire quelques articles introductifs pour obtenir un aperçu rapide.
    
    * [Progressive web apps](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps)
        
    * [Workbox](https://web.dev/articles/workbox)
        

## Qu'est-ce qu'une Progressive Web App (PWA) ?

Une PWA est une application web qui combine le meilleur du web et des applications mobiles. Elle est construite en utilisant des technologies web standard comme HTML, CSS et JavaScript, mais elle se comporte et se sent comme une application mobile native sur votre téléphone ou tablette.

Pensez à des applications comme Instagram Web, Twitter Lite ou Spotify Web Player. Même si vous n'utilisez pas une application native depuis un magasin d'applications :

* Vous pouvez toujours faire défiler votre flux, voir des médias et envoyer des messages.
    
* Elle fonctionne même sur des réseaux lents ou instables.
    
* Vous pouvez l'installer sur votre écran d'accueil et la lancer comme une application régulière.
    
* Vous recevez même des notifications push comme une application mobile !
    

Avec les PWA, vous obtenez la portée du web et le sentiment d'une application sans le stockage lourd ou le processus d'installation.

## Qu'est-ce qui rend une application web "Progressive" ?

Une PWA n'est pas n'importe quel site web. Elle est construite pour améliorer progressivement l'expérience utilisateur, en fonction de leur appareil et des capacités de leur navigateur. Voici les caractéristiques principales qui définissent une PWA :

* **Réactive** : Fonctionne sur toutes les tailles d'écran, c'est-à-dire les téléphones, tablettes et ordinateurs de bureau.
    
* **Fiable** : Se charge instantanément, même hors ligne ou sur des réseaux médiocres.
    
* **Installable** : Peut être ajoutée à l'écran d'accueil sans avoir besoin d'un magasin d'applications.
    
* **Engageante** : Prend en charge des fonctionnalités comme les notifications push et la synchronisation en arrière-plan.
    

## **Composants d'une PWA**

Avant que votre application web puisse être considérée comme une PWA, elle doit inclure les éléments suivants :

### Un Manifest d'application web

Le manifest d'application web est un fichier JSON qui indique au navigateur les informations sur votre application web, comment elle doit apparaître et se comporter lorsqu'elle est installée sur un appareil utilisateur.

Pensez à cela comme la carte de visite de votre application. Il inclut des détails comme :

* **Nom de l'application et nom court** – Comment votre application est étiquetée sur l'écran d'accueil ou la liste des applications.
    
* **Icônes** – Images utilisées pour les icônes de l'application sur différentes tailles d'écran et résolutions.
    
* **Couleur du thème et couleur de fond** – Définit l'apparence de l'interface utilisateur de votre application et de l'écran de chargement.
    
* **URL de démarrage** – La page qui s'ouvre lorsque l'application est lancée.
    
* **Mode d'affichage** – Contrôle si l'application s'ouvre dans un onglet du navigateur, en plein écran ou dans une fenêtre de type natif.
    
* **Captures d'écran** – Images de prévisualisation facultatives qui montrent à quoi ressemble votre application sur différents appareils dans les magasins d'applications ou les invites d'installation.
    

### Un Service Worker

Il s'agit d'un script qui s'exécute en arrière-plan. Il gère le comportement hors ligne, la mise en cache, la synchronisation en arrière-plan et les notifications push nécessaires pour faire fonctionner votre PWA.

Plus de détails sur le service worker seront discutés plus tard dans cet article.

### HTTPS

Les PWA doivent être servies via HTTPS. Ce n'est pas facultatif. Voici pourquoi :

* Il protège les utilisateurs en assurant un transfert de données sécurisé.
    
* Il permet des fonctionnalités importantes comme les service workers et les notifications push.
    
* Les navigateurs n'autoriseront pas les service workers à s'enregistrer sur des origines non sécurisées.
    

Si vous testez localement, vous pouvez utiliser [`localhost`](http://localhost) (qui est traité comme sécurisé), mais pour la production, votre site doit avoir un certificat SSL.

## Qu'est-ce qu'un Service Worker dans une PWA ?

Dans les PWA, un service worker est un fichier JavaScript qui s'exécute en arrière-plan, séparé de votre application principale, et agit comme un proxy réseau. Il peut :

* Mettre en cache des ressources et les servir hors ligne
    
* Intercepter des requêtes réseau et appliquer des stratégies de mise en cache
    
* Gérer les synchronisations en arrière-plan
    
* Gérer les notifications push
    

Pensez à cela comme l'assistant derrière la scène de votre application—il la fait charger rapidement, fonctionne hors ligne et reste à jour, même lorsque vous ne regardez pas.

## Pourquoi utiliser Workbox au lieu de Service Workers manuels ?

Les service workers sont essentiels pour créer une PWA, mais commencer avec eux peut être difficile. Écrire du code de service worker à partir de zéro peut souvent être fastidieux et sujet aux erreurs. Par exemple, vous devriez :

* Configurer manuellement les stratégies de mise en cache
    
* Gérer les mises à jour des service workers
    
* Écrire et maintenir beaucoup de code répétitif
    

Workbox, une bibliothèque de Google, facilite les choses en permettant aux développeurs de se concentrer sur ce qui compte, sans se soucier des parties compliquées des service workers.

Cependant, il est toujours important de comprendre comment fonctionnent les service workers, car ils gèrent certaines tâches complexes en arrière-plan.

Voici les principales choses qu'un service worker (avec ou sans Workbox) fait :

* **Événement d'installation** : Configurer le cache
    
* **Événement d'activation** : Nettoyer les anciens caches
    
* **Événement de récupération** : Intercepter les requêtes réseau et servir depuis le cache
    

Avec Workbox, ceux-ci sont enveloppés dans des fonctions faciles à utiliser.

## Introduction à WorkBox

Workbox est une collection de bibliothèques qui aide les développeurs à construire des service workers efficaces rapidement, avec les meilleures pratiques intégrées. Il prend en charge des stratégies comme :

* `CacheFirst` : Charger depuis le cache, revenir au réseau
    
* `NetworkFirst` : Essayer le réseau, revenir au cache
    
* `StaleWhileRevalidate` : Servir depuis le cache et mettre à jour en arrière-plan
    

### Comprendre les modules Workbox

Workbox est plus qu'un simple outil. C'est une collection de modules puissants, chacun conçu pour simplifier différentes parties du travail avec les service workers. Ces modules sont flexibles et peuvent être utilisés dans trois contextes clés :

* **Contexte du Service Worker** – À l'intérieur de votre fichier de service worker, où vous gérez la mise en cache, le routage et d'autres tâches en arrière-plan.
    
* **Contexte de la Fenêtre** – À l'intérieur de votre application principale (le JS côté client), où vous enregistrez et communiquez avec le service worker.
    
* **Intégration des Outils de Construction** – Des outils comme Webpack utilisent Workbox pour générer des fichiers de service worker et des manifestes de précache pendant votre processus de construction.
    

Décomposons certains des modules les plus populaires et essentiels que Workbox offre :

1. **workbox-routing**
    

Ce module gère le routage des requêtes réseau au sein de votre service worker. Pensez à cela comme un directeur de trafic qui écoute les événements `fetch` et décide quoi en faire.

**Cas d'utilisation** : Router les requêtes API vers le réseau tout en routant les requêtes de ressources statiques vers le cache.

2. **workbox-strategies**
    

C'est ici que les stratégies de mise en cache comme `CacheFirst`, `NetworkFirst` et `StaleWhileRevalidate` sont utilisées. Il fournit une API propre et cohérente pour gérer la manière dont votre application répond à différentes requêtes.

**Cas d'utilisation** : Appliquer différents comportements de mise en cache pour les images, les polices ou les données dynamiques avec un code minimal.

3. **workbox-precaching**
    

Ce module gère le précache en stockant les ressources statiques pendant la phase d'installation du service worker. Il facilite la mise en cache des fichiers à l'avance et garantit que les mises à jour sont gérées efficacement.

**Cas d'utilisation** : Pré-charger les ressources essentielles (comme HTML, CSS et les images de logo) afin que votre application se charge instantanément, même hors ligne.

4. **workbox-expiration**
    

Il est utilisé comme un plugin avec les stratégies de mise en cache. Ce module ajoute une expiration intelligente du cache. Vous pouvez automatiquement supprimer les anciens éléments ou les éléments excessifs du cache en fonction de leur durée de stockage ou du nombre d'éléments existants.

**Cas d'utilisation** : Garder la taille de votre cache sous contrôle sans suivre et supprimer manuellement les fichiers obsolètes.

**workbox-window**

Ce module est conçu pour le côté navigateur (fenêtre) de votre application. Il simplifie l'enregistrement du service worker et vous permet de communiquer facilement avec le service worker depuis votre page.

**Cas d'utilisation** : Détecter lorsqu'un nouveau service worker est disponible et inviter l'utilisateur à actualiser l'application pour la mettre à jour.

Vous pouvez utiliser WorkBox via :

* npm
    
* CDN (que nous utiliserons ici pour simplifier)
    

## Configuration du projet

Commençons par créer notre structure de projet :

```plaintext
weather-pwa/
├── index.html
├── style.css
├── js/
│   ├── app.js
│   └── install.js
├── service-worker.js
├── images/
│   └── [vos fichiers et dossiers d'images ici]
├── manifest.json
├── config.js  
└── offline.html
```

### La structure HTML

Tout d'abord, construisons notre fichier `index.html` :

```xml

<!DOCTYPE html>
<html lang="en">
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link rel="icon" href="/images/logo.png" type="image/png">
        <meta name="description" content="Simple Weather Progressive Web App" />
        <link rel="stylesheet" href="/styles.css" />
        <title>Weatherly</title>
    </head>
   
    
<body>
    <header class="header">
        <img loading="lazy" class="logo" src="images/logo.png" alt="Weatherly Logo">
        <h1>Weatherly</h1>
    </header>

    <main class="main">
        <div class="weather-card">
            <div class="location-container">
                <input type="text" id="location-input" placeholder="Enter city name">
                <button id="search-btn">Search</button>
                <button id="locationBtn">📍 Use My Location</button>
                <button id="installBtn" style="display: none;">Install App</button>
            </div>
             
            <div id="offline-message" class="offline-message">
                You are currently offline. Weather data may not be up-to-date.
            </div>

            
            <div class="error">
                <p id="error-message"></p>
            </div>
            
            <div id="weather-container" class="weather-container">
                <h3>Your last searched location weather:</h3>
                <div class="location-info">
                    <h2 id="city"></h2>
                    <p id="date"></p>
                </div>
                
                <div class="current-weather">
                    <img loading="lazy" id="weather-icon" src="" alt="Weather icon">
                    <div class="temperature-container">
                        <h3 id="temperature"></h3>
                        <p id="weather-description"></p>
                    </div>
                </div>
                
                <div class="weather-details">
                    <div class="detail">
                        <img loading="lazy" id="humidity-icon" src="/images/humidity.png" alt="Humidity icon">
                        <span class="label">Humidity</span>
                        <span id="humidity" class="value"></span>
                    </div>
                    <div class="detail">
                        <img loading="lazy" id="wind-icon" src="/images/wind.png" alt="Wind icon">
                        <span class="label">Wind</span>
                        <span id="wind" class="value"></span>
                    </div>
                </div>
            </div>

            <!-- Your location weather -->
            <div class="location-weather">
                <h3>Your location's weather:</h3>
                <div class="weather-info" id="weatherInfo">
                    
                </div>
            </div>
        </div>
    </main>
    
    <footer>
        <p>Made with ❤️ by <a href="www.linkedin.com/in/damilola-oniyide">Damilola Oniyide</a>
    </footer>
    <script type="module" src="/js/app.js" defer></script>
</body>
</html>
```

## Création de la structure HTML hors ligne

Le fichier `offline.html` est la page que les utilisateurs verront lorsqu'ils perdront la connexion réseau et essaieront de naviguer vers une page qui n'est pas mise en cache.

```xml
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="theme-color" content="#2196f3">
  <title>Weatherly - Offline</title>
  <link rel="stylesheet" href="/styles.css">
  <style>
    .offline-icon {
      font-size: 5rem;
      margin-bottom: 1.5rem;
      color: #2196f3;
    }
    
    .offline-message {
      font-size: 1.5rem;
      margin-bottom: 1.5rem;
    }
    
    .offline-subtext {
      font-size: 1rem;
      margin-bottom: 2rem;
      color: #666;
    }
    
    .retry-button {
      padding: 0.75rem 1.5rem;
      background-color: #2196f3;
      color: white;
      border: none;
      border-radius: 12px;
      font-size: 1rem;
      cursor: pointer;
      transition: background-color 0.3s;
    }
    
    .retry-button:hover {
      background-color: #2980b9;
    }
  </style>
</head>
<body>
  <header>
    <h1>Weatherly</h1>
  </header>
  
  <main>
    <div class="app-container">
      <div class="weather-card">
        <div class="offline-container">
          <div class="offline-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16">
              <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
              <path d="M7 6.5C7 7.328 6.552 8 6 8s-1-.672-1-1.5S5.448 5 6 5s1 .672 1 1.5zm-2.715 5.933a.5.5 0 0 1-.183-.683A4.498 4.498 0 0 1 8 9.5a4.5 4.5 0 0 1 3.898 2.25.5.5 0 0 1-.866.5A3.498 3.498 0 0 0 8 10.5a3.498 3.498 0 0 0-3.032 1.75.5.5 0 0 1-.683.183zM10 8c-.552 0-1-.672-1-1.5S9.448 5 10 5s1 .672 1 1.5S10.552 8 10 8z"/>
            </svg>
          </div>
          <h2 class="offline-message">You're offline</h2>
          <p class="offline-subtext">Please check your internet connection and try again.</p>
          <button class="retry-button" onclick="window.location.href='/'">Retry</button>
        </div>
      </div>
    </div>
  </main>
  
  <footer>
    <p>Made with ❤️ by Damilola Oniyide</p>
  </footer>
</body>
</html>
```

## Stylisation avec CSS

Maintenant, créons notre fichier `style.css` pour un design réactif et convivial :

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f5f5f5;
    color: #333;
    line-height: 1.6;
}

.header {
    background-color: #2196f3;
    color: white;
    padding: 1rem;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.header h1 {
    font-size: 1.5rem;
}


.header img {
    width: 55px;
    height: 55px;
    border: #ffff 1px solid;
    margin-right: 4px;
    border-radius: 10%;
}


.main {
    padding: 1rem;
    max-width: auto;
    margin: 0 auto;
}

.weather-card {
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    padding: 1.5rem 3rem;
    margin-top: 1rem;
}

/* Location input styles */
.location-container {
    display: flex;
    margin-bottom: 1.5rem;
    justify-content: center;
}

#location-input {
    flex: 1;
    padding: 0.75rem;
    border: 1px solid #ddd;
    border-radius: 4px 0 0 4px;
    font-size: 1rem;
    max-width: 240px;
}

#location-input:focus {
    outline: none;
    border-color: #2196f3;
}
#location-input::placeholder {
    color: #999;
}   

#search-btn, #locationBtn {
    background-color: #2196f3;
    color: white;
    border: none;
    padding: 0.75rem 1rem;
    border-radius: 0 4px 4px 0;
    cursor: pointer;
    font-size: 1rem;
    margin-right: 2.5px;
}


#installBtn {
    background-color: #2196f3;
    color: white;
    border: none;
    padding: 0.75rem 1rem;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
    
}

#search-btn:focus, #locationBtn:focus, #installBtn:focus {
    outline: none;
    box-shadow: 0 0 5px rgba(33, 150, 243, 0.5);
}
#search-btn:hover, #locationBtn:hover, #installBtn:hover {
    background-color: #1976d2;
}

.error, .loading {
    text-align: center;
    font-weight: bold;
    font-size: 14px;
    margin-top: 10px;
    display: none;;
}

.error-message {
    color: #d32f2f;

}
/* Weather display styles */
.weather-container {
    display: none 
}

#weather-icon {
    width: 1000px; 
    height: 100px;
  }
  
.current-weather{
    margin-bottom: 2rem;
    display: flex;
    justify-content: center;
}

.location-weather{
    margin-top: 2rem;
    display: flex;
    justify-content: center;
    flex-direction: column;
}


#weather-icon {
    width: 80px;
    height: 80px;
    margin-right: 1rem;
}

.location-info {
    margin-bottom: 1rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.location-info h2,  .current-weather h3, .weather-container h3, .location-weather h3 {
    font-size: 1.8rem;
    margin-bottom: 0.25rem;
}



.location-info p, .current-weather p {
    color: #666;
    font-size: 1.4rem;
}

.temperature-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-bottom: 1rem;
}

.temperature-container h3 {
    font-size: 2.5rem;
    margin-bottom: 0.25rem;
}

.temperature-container p {
    color: #666;
    text-transform: capitalize;
}

.weather-details {
    display: flex;
    justify-content: center;
    background-color: #f9f9f9;
    border-radius: 4px;
    padding: 1rem;
}

#humidity-icon, #wind-icon{
    width: 40px;
    height: 40px;
}

.detail {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 0 1rem;
    text-align: center;
}

.label {
    font-size: 0.9rem;
    color: #666;
    margin-bottom: 0.25rem;
}

.value {
    font-size: 1.2rem;
    font-weight: 500;
}

/* Error and offline message styles */
.error-message {
    color: #d32f2f;
    text-align: center;
    margin-top: 1rem;
    display: none;
} 

.offline-message {
    background-color: #ffab91;
    color: #7f0000;
    padding: 0.75rem;
    text-align: center;
    margin-top: 1rem;
    border-radius: 4px;
    display: none;
}


/* 5 days forecast weather */
.forecast-container {
    display: flex;
    justify-content: space-around;
    gap: 1rem;
}

.forecast-item {
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    padding: 1rem 4rem;
    text-align: center;
}



footer {
    background-color: #2196f3;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: .7rem 0;
}

footer p, footer a {
    color: #f9f9f9;
    font-weight: 500;
}
/* Responsive styles */
@media (max-width: 480px) {
    .header h1 {
        font-size: 1.2rem;
    }

    .location-container {
        flex-direction: column;
        align-items: center;
        gap: .6rem
    }
    
    
    .current-weather {
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .weather-container h3,  .location-weather h3, .forecast h3 {
        font-size: 1.5rem;
    }
    
    #weather-icon {
        margin-right: 0;
        margin-bottom: 1rem;
    }

    .forecast-container {
        flex-direction: column;
        align-items: center;
    }
}
```

## Comment configurer `app.js` et `config.js`

Maintenant, créons notre fichier `app.js` pour ajouter des fonctionnalités à l'application météo. Avant de continuer, assurez-vous d'avoir obtenu votre **clé API** depuis [OpenWeather](https://openweathermap.org/). Pour les meilleures pratiques, stockez votre clé API dans un fichier séparé comme `config.js` pour garder les choses organisées et éviter de coder en dur les données sensibles.

Voici à quoi votre `config.js` devrait ressembler :

```javascript
export const CONFIG = {
    WEATHER_API_KEY: "WRITE-YOUR-API-KEY-HERE",
};
```

Assurez-vous d'ajouter le fichier `config.js` à `.gitignore` pour éviter de divulguer des informations sensibles sur une plateforme publique comme GitHub.

Maintenant, passons à `app.js`. C'est ici que la logique principale de votre application météo résidera. Vous pouvez maintenant référencer votre clé API en utilisant `Weather_API_KEY` depuis le fichier `config.js`.

Voici la structure de votre fichier `app.js` :

```javascript
import { CONFIG } from './config.js';
const BASE_URL = `https://api.openweathermap.org/data/2.5/weather?&appid=${CONFIG.WEATHER_API_KEY}&units=metric&q=`;

const cityName = document.getElementById('location-input');
const searchButton = document.getElementById('search-btn');
const weatherIcon = document.getElementById('weather-icon');
const locationBtn = document.getElementById('locationBtn');
const weatherInfo = document.getElementById('weatherInfo');


function getWeatherIcon(condition) {
  switch (condition) {
    case "Clear":
      return "images/weather-icons/clear.png";
    case "Clouds":
      return "images/weather-icons/clouds.png";
    case "Drizzle":
      return "images/weather-icons/drizzle.png";
    case "Rain":
      return "images/weather-icons/drizzle.png";
    case "Mist":
      return "images/weather-icons/mist.png";
    case "Snow":
      return "images/weather-icons/snow.png";
    default:
      return "images/weather-icons/default.png";
  }
}
//Search for weather by city name
async function checkWeatherBySearch(city){
    if(city.length == 0) {
        document.getElementsByClassName('error')[0].style.display = 'block';
        document.getElementsByClassName('error')[0].innerHTML = "Please enter a city name!";
        document.getElementsByClassName('error')[0].style.color = 'red';
        document.getElementById('weather-container').style.display = 'none'; 
        return;
    }
    const response = await fetch(BASE_URL + city);
    document.getElementsByClassName('error')[0].style.display = 'block';
    document.getElementsByClassName('error')[0].innerHTML = "Wait a sec, your location's data will be displayed soon!";

    if (response.status == 404) {
        document.getElementsByClassName('error')[0].style.display = 'block';
        document.getElementsByClassName('error')[0].innerHTML = "City not found! Please enter a valid city name.";
        document.getElementsByClassName('error')[0].style.color = 'red';
        document.getElementById('weather-container').style.display = 'none';       
    } else {
      const data = await response.json();
      document.getElementById('weather-container').style.display = 'block';
      document.getElementsByClassName('error')[0].style.display = 'none';
      localStorage.setItem('lastCity', city);
      document.getElementById('city').innerHTML = data.name;
      document.getElementById('date').innerHTML = new Date(data.dt * 1000).toLocaleDateString();
      document.getElementById("temperature").innerHTML = Math.round(data.main.temp) + "°C";
      document.getElementById("humidity").innerHTML = data.main.humidity + "%";
      document.getElementById("wind").innerHTML = data.wind.speed + "m/s";
      document.getElementById('weather-description').innerHTML = data.weather[0].description;
      const weatherCondition = data.weather[0].main;
      weatherIcon.src = getWeatherIcon(weatherCondition);
    }
}

 // display next 5-day forecast by coordinates
function display5DaysForecast(forecast) {
   const fragment = document.createDocumentFragment(); 
    const forecastWrapper = document.createElement('div');
    forecastWrapper.className = 'forecast';
  
    const heading = document.createElement('h3');
    heading.innerHTML = "Your location's next 5 days forecast:";
  
    const container = document.createElement('div');
    container.className = 'forecast-container';
  
    const addedDates = new Set();
    const today = new Date().toDateString();

    forecast.forEach((entry) => {
      const entryDateObj = new Date(entry.dt * 1000);
      const entryDateStr = entryDateObj.toDateString();
    
      if (entryDateStr !== today && !addedDates.has(entryDateStr)) {
        addedDates.add(entryDateStr);
        if (addedDates.size > 6) return;

    
        const condition = entry.weather[0].main;
        const iconSrc = getWeatherIcon(condition);
  
        const forecastItem = document.createElement('div');
        forecastItem.className = 'forecast-item';
  
        const date = document.createElement('p');
        date.id = 'date';
        date.innerHTML = `<strong>${new Date(entry.dt * 1000).toLocaleDateString()}</strong>`;
  
        const icon = document.createElement('img');
        icon.loading = 'lazy';
        icon.id = 'weather-icon';
        icon.src = iconSrc;
        icon.alt = `${condition} icon`;
  
        const tempContainer = document.createElement('div');
        tempContainer.className = 'temperature-container';
  
        const temp = document.createElement('h3');
        temp.id = 'temperature';
        temp.innerHTML = `${Math.round(entry.main.temp)} °C`;
  
        const description = document.createElement('p');
        description.id = 'weather-description';
        description.innerHTML = `${entry.weather[0].description}`;
  
        tempContainer.appendChild(temp);
        tempContainer.appendChild(description);
        forecastItem.appendChild(date);
        forecastItem.appendChild(icon);
        forecastItem.appendChild(tempContainer);
        container.appendChild(forecastItem);
      }
    });
  
    forecastWrapper.appendChild(heading);
    forecastWrapper.appendChild(container);
    fragment.appendChild(forecastWrapper);
    weatherInfo.appendChild(fragment); 
}

// Fetch next 5-day forecast by coordinates
function get5DaysForecast(lat, lon) {
    fetch(
      `https://api.openweathermap.org/data/2.5/forecast?lat=${lat}&lon=${lon}&appid=${CONFIG.WEATHER_API_KEY}&units=metric`
    )
      .then(res => res.json())
      .then(data => {
        requestIdleCallback(() => {
          setTimeout(() => display5DaysForecast(data.list), 0);
        });        
      })
      .catch(() => {
        weatherInfo.innerHTML = 'Error fetching forecast data.';
    });
}
  
 // Display current weather data
function displayUserWeather(data) {
    const weatherCondition = data.weather[0].main;
    const iconSrc = getWeatherIcon(weatherCondition);

    weatherInfo.innerHTML = `
      <h2 id="city">${data.name}, ${data.sys.country}</h2>

      <div class="current-weather">
        <img loading="lazy" id="weather-icon" src="${iconSrc}" alt="Weather icon">
        <div class="temperature-container">
          <h3 id="temperature"> ${Math.round(data.main.temp)} °C</h3>
          <p id="weather-description">${data.weather[0].description}</p>
        </div>
      </div>

      <div class="weather-details">
        <div class="detail">
          <img loading="lazy" id="humidity-icon" src="/images/humidity.png" alt="Humidity icon">
          <span class="label">Humidity</span>
          <span id="humidity" class="value"> ${data.main.humidity}%</span>
        </div>
        <div class="detail">
          <img loading="lazy" id="wind-icon" src="/images/wind.png" alt="Wind icon">
          <span class="label">Wind</span>
          <span id="wind" class="value"> ${data.wind.speed} m/s</span>
        </div>
      </div>
    `;
  }

// Fetch weather by coordinates
function getWeatherByCoords(lat, lon) {
    fetch(
      `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${CONFIG.WEATHER_API_KEY}&units=metric`
    )
      .then(res => res.json())
      .then(data => {
        displayUserWeather(data);
        get5DaysForecast(lat, lon);
      })
      .catch(() => {
        weatherInfo.innerHTML = 'Please turn on your device&apos;s location to get weather data.';;
      });
  }

// Event listeners for search button and input field
cityName.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') checkWeatherBySearch(cityName.value);
});

  // Search button click event
searchButton.addEventListener('click', ()=>{
    checkWeatherBySearch(cityName.value);
});

// Geolocation button
locationBtn.addEventListener('click', () => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        pos => {
          const { latitude, longitude } = pos.coords;
          getWeatherByCoords(latitude, longitude);
        },
        () => {
          weatherInfo.innerHTML = 'Unable to retrieve location.';
        }
      );
    } else {
      weatherInfo.innerHTML = 'Geolocation not supported.';
    }
});


// Load last searched city
window.onload = () => {
    const lastCity = localStorage.getItem('lastCity');
    if (lastCity) {
        checkWeatherBySearch(lastCity);
    }

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          pos => {
            const { latitude, longitude } = pos.coords;
            getWeatherByCoords(latitude, longitude);
          },
          () => {
            weatherInfo.innerHTML = 'Unable to retrieve location.';
          }
        );
      } else {
        weatherInfo.innerHTML = 'Geolocation not supported.';
      }
};
```

Maintenant que nous avons notre application météo, allons plus loin pour en faire une application web progressive.

## Comment créer un fichier Manifest

Nous devons créer un fichier `manifest.json`, une partie critique pour faire de votre application une PWA. Nous utiliserons également [**pwa-asset-generator**](https://www.npmjs.com/package/pwa-asset-generator), un outil CLI qui vous aide à générer toutes les icônes et écrans de démarrage nécessaires à partir d'une seule image (comme votre logo). Cet outil met également à jour votre `manifest.json` et injecte éventuellement des balises `<link>` pertinentes dans `index.html`.

Voici le fichier `manifest.json` contenant les propriétés clés qui définissent le comportement et l'apparence de l'application web progressive lorsqu'elle est installée.

```json
{
  "name": "Weatherly",                      // Le nom complet de votre application qui peut être montré aux utilisateurs.
  "short_name": "Weatherly",               // Un nom plus court utilisé lorsque l'espace est limité, comme sur l'écran d'accueil.
  "description": "A simple weather Progressive Web App", // Une courte description de ce que fait votre application.
  "start_url": "/index.html",              // La page qui s'ouvre lorsque l'application est lancée depuis l'écran d'accueil.
  "display": "standalone",                 // Fait en sorte que l'application ressemble à une application native sans l'interface utilisateur du navigateur (comme la barre d'adresse).
  "background_color": "#ffffff",           // La couleur de fond utilisée lorsque l'application est en cours de chargement.
  "theme_color": "#2196f3",                // La couleur principale de l'interface utilisateur de l'application, comme la barre d'état.
  "orientation": "portrait",                // Verrouille l'orientation de l'écran en mode portrait.
   "screenshots": [                         // Aide à montrer aux utilisateurs un aperçu de votre application avant de l'installer — surtout dans des endroits comme l'invite "Ajouter à l'écran d'accueil" sur Android ou dans les magasins d'applications qui prennent en charge les PWA.
        {
          "src": "images/screenshots/desktop-screenshot.png",
          "sizes": "1337x645",
          "type": "image/png",
          "form_factor": "wide"
        },
        {
          "src": "images/screenshots/mobile-screenshot.png",
          "sizes": "720x1417",
          "type": "image/png",
          "form_factor": "narrow"
        }
      ]
}
```

### Comment générer des icônes et des écrans de démarrage

À l'intérieur de votre dossier `images`, créez un nouveau dossier appelé `assets`. Cela stockera toutes les icônes et écrans de démarrage générés. Lorsque votre application est lancée depuis l'écran d'accueil, ces écrans de démarrage aideront à améliorer l'expérience utilisateur sur les appareils iOS.

Exécutez la commande suivante pour générer les ressources PWA, mettre à jour le `manifest.json` et injecter des balises `<link>` dans `index.html`

```powershell
npx pwa-asset-generator logo.png ./images/assets -m manifest.json -i index.html
```

### Balises de lien injectées dans `index.html`

Une fois la commande exécutée avec succès, une série de balises `<link>` et `<meta>` seront automatiquement ajoutées à l'en-tête `<head>` de votre `index.html`. Ces balises garantissent la prise en charge des écrans de démarrage et des icônes sur divers appareils Apple :

```xml
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <!-- Autres balises meta/link -->

  <link rel="apple-touch-icon" href="images/assets/apple-icon-180.png">
  <meta name="mobile-web-app-capable" content="yes">

  <link rel="apple-touch-startup-image" href="images/assets/apple-splash-2048-2732.jpg" media="(device-width: 1024px) and (device-height: 1366px) and (orientation: portrait)">
  <link rel="apple-touch-startup-image" href="images/assets/apple-splash-2732-2048.jpg" media="(device-width: 1024px) and (device-height: 1366px) and (orientation: landscape)">
  <!-- ...plus de balises d'écran de démarrage pour divers appareils... -->
</head>
```

Voici à quoi devrait ressembler le fichier `manifest.json` maintenant :

```json
{
    "name": "Weatherly",
    "short_name": "Weatherly",
    "description": "A simple weather Progressive Web App",
    "start_url": "/index.html",
    "display": "standalone",
    "background_color": "#ffffff",
    "theme_color": "#2196f3",
    "orientation": "portrait",
    "icons": [
        [
            {
              "src": "images/assets/manifest-icon-192.maskable.png",
              "sizes": "192x192",
              "type": "image/png",
              "purpose": "any"
            },
            {
              "src": "images/assets/manifest-icon-192.maskable.png",
              "sizes": "192x192",
              "type": "image/png",
              "purpose": "maskable"
            },
            {
              "src": "images/assets/manifest-icon-512.maskable.png",
              "sizes": "512x512",
              "type": "image/png",
              "purpose": "any"
            },
            {
              "src": "images/assets/manifest-icon-512.maskable.png",
              "sizes": "512x512",
              "type": "image/png",
              "purpose": "maskable"
            }
          ]
        ],
    "screenshots": [
        {
          "src": "images/screenshots/desktop-screenshot.png",
          "sizes": "1337x645",
          "type": "image/png",
          "form_factor": "wide"
        },
        {
          "src": "images/screenshots/mobile-screenshot.png",
          "sizes": "720x1417",
          "type": "image/png",
          "form_factor": "narrow"
        }
      ]
    }
```

Vous pouvez ensuite lier votre fichier manifest à votre fichier HTML :

```json
<link rel="manifest" href="manifest.json" />
```

## Comment ajouter WorkBox à votre fichier `service-worker.js`

Dans ce tutoriel, WorkBox sera ajouté à `index.html` via CDN. Vous pouvez copier le code d'importation ci-dessous ou visiter WorkBox pour obtenir le lien. Vous pouvez ensuite l'ajouter au fichier `index.html` en plaçant l'URL à l'intérieur d'une balise `<script>`. Vous pouvez copier le code d'importation ci-dessous ou visiter le site Web de WorkBox pour obtenir le dernier lien.

```javascript
importScripts('https://storage.googleapis.com/workbox-cdn/releases/6.5.4/workbox-sw.js');
```

## Comment créer votre Service Worker dans le fichier `service-worker.js`

Ici, nous allons implémenter les fonctionnalités nécessaires pour faire de l'application météo une PWA

### **Étape 1 :** Activer immédiatement le nouveau Service Worker

Ajoutez `workbox.core.skipWaiting()` pour que le nouveau service worker installé devienne actif immédiatement au lieu d'attendre que l'ancien soit supprimé dans le fichier `service-worker.js`.

```javascript
workbox.core.skipWaiting();
```

### **Étape 2 :** Prendre le contrôle des onglets ouverts

Ajoutez `workbox.core.clientsClaim()` pour vous assurer que le service worker activé prend le contrôle de toutes les pages actuellement ouvertes, afin que la dernière version de votre application fonctionne immédiatement sur tous les onglets après son activation.

```javascript
workbox.core.clientsClaim();
```

### **Étape 3 :** Vérifier si Workbox est chargé

Avant d'utiliser Workbox, assurez-vous qu'il est correctement chargé.

```js
if (workbox) {
  console.log('Workbox loaded successfully');
} else {
  console.log('Workbox failed to load');
}
```

Cela confirme que l'objet `workbox` est disponible et prêt à être utilisé. Sinon, le message de secours dans le bloc `else` sera affiché.

Nous procédons ensuite à la création des fonctions à l'intérieur du bloc `if`

### **Étape 4 :** Pré-mettre en cache les fichiers principaux

La pré-mise en cache des fichiers essentiels permet à votre application de fonctionner hors ligne. Cela met en cache la coque de votre application (HTML, CSS, JS), afin qu'elle se charge même sans connexion réseau.

```js
workbox.precaching.precacheAndRoute([
    { url: '/index.html', revision: '3' },
    { url: '/style.css', revision: '11' },
    { url: '/app.js', revision: '7' },
    { url: '/images/logo.png', revision: '3' },
    { url: '/manifest.json', revision: '5' },
    { url: '/offline.html', revision: '1' },
  ]);
```

La `révision` aide à mettre à jour les fichiers mis en cache lorsque des modifications sont apportées.

### **Étape 5 :** Mettre en cache les réponses de l'API de manière dynamique

Configurez une route pour mettre en cache les données de votre API météo en utilisant la stratégie de mise en cache `NetworkFirst`. Cela indique à Workbox d'essayer d'abord de récupérer des données fraîches depuis le réseau. Si le réseau échoue, il sert la version mise en cache à la place.

```js
 // Cache API requests 
  workbox.routing.registerRoute(
    ({ url }) => url.origin === 'https://api.openweathermap.org',
    new workbox.strategies.NetworkFirst({
      cacheName: 'weather-api-cache',
      plugins: [
        new workbox.expiration.ExpirationPlugin({
          maxAgeSeconds: 24 * 60 * 60,
          maxEntries: 10,
        }),
      ],
    })
  );
```

### **Étape 6 :** Mise en cache dynamique des images

Cette fonction permet la mise en cache dynamique des images en utilisant la stratégie `StaleWhileRevalidate`. Lorsqu'un utilisateur demande une image, Workbox la sert d'abord depuis le cache (si disponible) pour des temps de chargement plus rapides, tout en récupérant simultanément une version mise à jour depuis le réseau pour actualiser le cache. Cela garantit que les utilisateurs obtiennent une réponse rapide sans manquer de contenu mis à jour. C'est une manière intelligente de gérer les images en équilibrant vitesse et fraîcheur.

```javascript
// Cache images
  workbox.routing.registerRoute(
    ({ request }) => request.destination === 'image',
    new workbox.strategies.StaleWhileRevalidate({
      cacheName: 'image-cache',
    })
  );
```

### **Étape 7 :** Servir les ressources mises en cache

Les fichiers statiques couramment utilisés (comme HTML, CSS, JS, polices, etc.) sont servis rapidement depuis le cache. Il utilise la stratégie `CacheFirst`, ce qui signifie que le service worker cherchera d'abord dans le cache et ne récupérera depuis le réseau que si le fichier n'est pas déjà stocké. Le cache est nommé `"static-cache"` et il est configuré pour supprimer automatiquement les éléments plus anciens que sept jours à l'aide du plugin `expiration`. Cela aide à garder le cache frais et évite de prendre trop de place.

```javascript
  // Serve Cached Resources 
  workbox.routing.registerRoute(
    ({url}) => url.origin === self.location.origin,  
    new workbox.strategies.CacheFirst({
      cacheName: 'static-cache',  
      plugins: [
        new workbox.expiration.ExpirationPlugin({
          maxAgeSeconds: 7 * 24 * 60 * 60,  // Cache static resources for 7 days
        }),
      ],
    })
  );
```

### **Étape 8 :** Mettre en cache les pages HTML avec prise en charge hors ligne

La page `index.html` sera gérée en utilisant la stratégie NetworkFirst. Cela signifie que le service worker essaie d'abord de récupérer la dernière version depuis le réseau. Si l'utilisateur est hors ligne ou si le réseau échoue, il revient à la version mise en cache. Le cache est nommé `"pages-cache"` et la page de secours hors ligne (`offline.html`) est retournée lorsque la page demandée n'est pas disponible. Cela garantit que les utilisateurs peuvent toujours naviguer dans l'application même sans connexion Internet.

```javascript
// Serve HTML pages with Network First and offline fallback
workbox.routing.registerRoute(
  ({ request }) => request.mode === 'navigate',
  async ({ event }) => {
    try {
      const response = await workbox.strategies.networkFirst({
        cacheName: 'pages-cache',
        plugins: [
          new workbox.expiration.ExpirationPlugin({
            maxEntries: 50,
          }),
        ],
      }).handle({ event });
      return response || await caches.match('/offline.html');
    } catch (error) {
      return await caches.match('/offline.html');
    }
  }
);
```

### Étape 9 : Gérer lorsque Workbox ne se charge pas

Vous devez toujours fournir une solution de secours au cas où quelque chose se passerait mal. Le bloc `if` aura un bloc `else` pour attraper les problèmes pendant le développement et le débogage.

```js
else {
     console.log('Workbox failed to load');
}
```

Une fois que le service worker a terminé de gérer les différentes conditions dans le bloc `if-else`, nous ajoutons une étape de nettoyage générale pour supprimer les caches obsolètes ou inutilisés.

### **Étape 10 :** Nettoyer les caches obsolètes

Pendant la phase d'activation du service worker, les anciens caches ou ceux inutilisés sont supprimés. Il compare tous les noms de cache existants avec une liste de ceux actuels (`precache`, `weather-api-cache`, `image-cache`, `pages-cache`, et `static-resources`). Si un cache ne correspond pas à la liste actuelle, il est supprimé. Cela aide à garder l'application légère et garantit que les données obsolètes ne persistent pas.

```javascript
// Clean up old/unused caches during activation
self.addEventListener('activate', event => {
  const currentCaches = [
    workbox.core.cacheNames.precache,
    'weather-api-cache',
    'image-cache',
    'pages-cache',
    'static-cache'
  ];

  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (!currentCaches.includes(cacheName)) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
```

Voici à quoi devrait ressembler votre fichier `service-worker.js` :

```javascript
importScripts('https://storage.googleapis.com/workbox-cdn/releases/6.5.4/workbox-sw.js');

// Force waiting service worker to become active
workbox.core.skipWaiting();
workbox.core.clientsClaim();

if (workbox) {
  console.log('Workbox loaded successfully');

  // Precache critical files with revisions (update revisions when files change)
  workbox.precaching.precacheAndRoute([
    { url: '/index.html', revision: '3' },
    { url: '/style.css', revision: '11' },
    { url: '/app.js', revision: '7' },
    { url: '/images/logo.png', revision: '3' },
    { url: '/manifest.json', revision: '5' },
    { url: '/offline.html', revision: '1' },
  ]);

  // Cache API requests 
  workbox.routing.registerRoute(
    ({ url }) => url.origin === 'https://api.openweathermap.org',
    new workbox.strategies.NetworkFirst({
      cacheName: 'weather-api-cache',
      plugins: [
        new workbox.expiration.ExpirationPlugin({
          maxAgeSeconds: 24 * 60 * 60,
          maxEntries: 10,
        }),
      ],
    })
  );

  // Cache images
  workbox.routing.registerRoute(
    ({ request }) => request.destination === 'image',
    new workbox.strategies.StaleWhileRevalidate({
      cacheName: 'image-cache',
    })
  );

    // Serve Cached Resources 
  workbox.routing.registerRoute(
    ({url}) => url.origin === self.location.origin,  
    new workbox.strategies.CacheFirst({
      cacheName: 'static-cache',  
      plugins: [
        new workbox.expiration.ExpirationPlugin({
          maxAgeSeconds: 7 * 24 * 60 * 60,  // Cache static resources for 7 days
        }),
      ],
    })
  );

  // Serve HTML pages with Network First and offline fallback
workbox.routing.registerRoute(
  ({ request }) => request.mode === 'navigate',
  async ({ event }) => {
    try {
      const response = await workbox.strategies.networkFirst({
        cacheName: 'pages-cache',
        plugins: [
          new workbox.expiration.ExpirationPlugin({
            maxEntries: 50,
          }),
        ],
      }).handle({ event });
      return response || await caches.match('/offline.html');
    } catch (error) {
      return await caches.match('/offline.html');
    }
  }
);
} else {
  console.log('Workbox failed to load');
}

// Clean up old/unused caches during activation
self.addEventListener('activate', event => {
  const currentCaches = [
    workbox.core.cacheNames.precache,
    'weather-api-cache',
    'image-cache',
    'pages-cache',
    'static-cache'
  ];

  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (!currentCaches.includes(cacheName)) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
```

## Comment configurer l'installation de l'application

Le code pour installer l'application sera écrit dans `install.js` en suivant les étapes ci-dessous :

### **Étape 1 :** Enregistrer le Service Worker

Enregistrez le service worker pour l'activer et l'exécuter dans votre application.

```javascript
if('serviceWorker' in navigator){
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/service-worker.js').then(reg => {
        reg.onupdatefound = () => {
          const newWorker = reg.installing;
          newWorker.onstatechange = () => {
            if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
              window.location.reload();
            }
          };
        };
      });
    })
 }
```

### Étape 2 : Activer l'invite d'installation personnalisée

Ensuite, nous allons permettre aux utilisateurs d'installer la PWA météo avec un bouton personnalisé. À l'intérieur du fichier `install.js`, ajoutez l'événement `beforeinstallprompt` qui intercepte l'invite par défaut et affiche votre bouton d'installation à la place. Lorsqu'il est cliqué, il déclenche l'invite d'installation.

```javascript

  let deferredPrompt;

document.addEventListener('DOMContentLoaded', () => {
  const installBtn = document.getElementById('installBtn');

  window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;

    // Show the button
    installBtn.style.display = 'block';

    installBtn.addEventListener('click', () => {
      // Directly triggered by user click
      installBtn.style.display = 'none';

      // Show the install prompt
      deferredPrompt.prompt();

      deferredPrompt.userChoice.then((choiceResult) => {
        if (choiceResult.outcome === 'accepted') {
          console.log('User accepted the install prompt');
        } else {
          console.log('User dismissed the install prompt');
        }
        deferredPrompt = null;
      });
    });
  });
```

L'événement `appinstalled` confirme l'installation réussie.

```javascript

window.addEventListener('appinstalled', () => {
    console.log('PWA was installed');
  });
});
```

### Étape 3 : Ajouter une balise de script pour importer `install.js` dans `index.html`

Ajoutez la balise `<script>` pour `install.js` à l'intérieur du fichier `index.html` pour inclure la logique d'installation.

```xml
 <script type="module" src="/js/install.js"></script>
```

## Comment installer l'application météo

Vous pouvez choisir d'installer l'application Weatherly sur votre téléphone ou votre bureau. Voici une démonstration de la manière de l'installer sur votre téléphone mobile :

Ouvrez l'application [Weatherly](https://weatherly-taupe-two.vercel.app/) dans votre navigateur. Vous devriez voir un bouton **"Installer l'application"**, comme montré dans l'image ci-dessous. Cliquez sur le bouton pour continuer.

![Interface de l'application Weatherly montrant le bouton Installer l'application ainsi que le champ de recherche de ville, les services de localisation et l'historique météo de Tokyo](https://cdn.hashnode.com/res/hashnode/image/upload/v1747272209446/2ade0ad7-eda5-46df-b443-a1efce90003b.png align="center")

Après avoir cliqué, un aperçu de l'application apparaîtra avec une option **"Installer"**, comme montré ci-dessous. Cliquez sur le bouton Installer.

![Dialogue d'installation PWA du navigateur montrant l'aperçu de l'application Weatherly avec le bouton Installer et la description de l'application.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748387183047/b6be3b6c-6550-4c94-a453-eb928cc70dbe.png align="center")

Une fois l'installation terminée, l'application Weatherly apparaîtra sur votre écran d'accueil, comme une application native. Et c'est tout ! Votre application météo est maintenant une Progressive Web App (PWA).

## Conclusion

Les Progressive Web Apps combinent le meilleur des expériences web et des applications natives, et les service workers sont l'épine dorsale de cette fonctionnalité. Avec des outils comme Workbox, vous n'avez pas à vous soucier de la gestion manuelle de la mise en cache, du support hors ligne ou de la synchronisation en arrière-plan. Ses API simples et ses stratégies intégrées facilitent la création d'applications web rapides, fiables et installables. Qu'il s'agisse d'une petite application météo comme [Weatherly](https://weatherly-pwa.vercel.app/) ou d'un projet plus complexe, Workbox vous aide à offrir une expérience utilisateur fluide.

Vous pouvez consulter le projet complet et les ressources sur [GitHub](https://github.com/LolaVictoria/weatherly)