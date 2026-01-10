---
title: Qu'est-ce que les Progressive Web Apps ? Guide PWA pour débutants
subtitle: ''
author: Ophy Boamah
co_authors: []
series: null
date: '2024-01-18T15:56:46.000Z'
originalURL: https://freecodecamp.org/news/what-are-progressive-web-apps-pwa-guide
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Essentials.png
tags:
- name: progressive web app
  slug: progressive-web-app
- name: PWA
  slug: pwa
seo_title: Qu'est-ce que les Progressive Web Apps ? Guide PWA pour débutants
seo_desc: "Progressive Web Apps (PWAs) are simply installable web applications – websites\
  \ that you can install on your device, much like you would install an app from an\
  \ app store. \nThey bring together the best parts of using a website (easy to access,\
  \ no need ..."
---

Les Progressive Web Apps (PWA) sont simplement des applications web installables – des sites web que vous pouvez installer sur votre appareil, comme vous le feriez pour une application depuis un magasin d'applications. 

Elles combinent les meilleurs aspects de l'utilisation d'un site web (facile d'accès, pas besoin d'installer quoi que ce soit) avec les excellentes fonctionnalités des applications mobiles (rapides, peuvent fonctionner hors ligne), offrant une expérience utilisateur de haute qualité. 

Le cœur de l'utilité d'une PWA réside dans l'approche "offline-first", où les applications sont conçues pour fonctionner de manière transparente sans connexion internet constante. Cela signifie que vous pouvez toujours utiliser ces applications même lorsque votre internet est lent ou indisponible, ce qui rend les PWA très conviviales et accessibles, même là où une connexion internet n'est pas toujours fiable.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/pwaa.png)
_Graphique montrant une application native vs une application web vs une PWA_

## 5 Raisons d'utiliser une PWA au lieu d'une application native

Les Progressive Web Apps (PWA) redéfinissent le paysage de l'interaction numérique. Elles offrent une expérience hybride qui combine les meilleures fonctionnalités des applications web et mobiles. 

Examinons plus en détail pourquoi les PWA sont souvent un choix supérieur par rapport aux applications natives :

### 1. Vitesse et facilité d'installation

Les PWA éliminent le long processus de téléchargement et d'installation typique des applications natives. Vous pouvez accéder à une PWA aussi rapidement que vous chargeriez une page web, ce qui la rend aussi simple que de marquer votre site préféré – pas besoin d'attendre les téléchargements ou de naviguer dans les magasins d'applications. 

Prenez Twitter Lite, une version PWA de la populaire plateforme de médias sociaux, qui offre l'expérience complète de Twitter sans avoir besoin d'attendre le téléchargement d'une application séparée. 

### 2. Exigences de stockage minimales

L'un des avantages les plus significatifs des PWA est leurs exigences de stockage minimales. Puisqu'elles stockent principalement des données en ligne, comme les services cloud, elles occupent significativement moins d'espace sur l'appareil de l'utilisateur. 

Cette fonctionnalité est particulièrement bénéfique pour les utilisateurs avec un stockage limité sur leur appareil ou des forfaits de données coûteux. Par exemple, la PWA de Pinterest prend moins de place que sa contrepartie native mais offre toujours une expérience utilisateur riche et engageante. 

### 3. Performance hors ligne fiable

La capacité d'une PWA à fonctionner hors ligne est comme avoir un bon livre téléchargé sur votre liseuse, prêt à être apprécié même lorsque vous êtes hors de portée d'un bon signal. 

Les PWA peuvent fonctionner efficacement même dans des zones avec une connectivité internet médiocre ou inexistante, en utilisant des données mises en cache à partir d'activités en ligne précédentes. Cela garantit que les utilisateurs ont un accès ininterrompu aux fonctionnalités essentielles. 

Un exemple notable est la PWA de Starbucks, qui permet aux clients de parcourir le menu et de personnaliser les commandes, indépendamment de leur connexion internet pour une expérience utilisateur cohérente.

### 4. Développement rentable et compatibilité multi-appareils

Développer une PWA peut être plus rentable que de construire des applications natives pour diverses plateformes. Cette approche unifiée permet non seulement d'économiser du temps et des ressources de développement significatifs, mais simplifie également la maintenance et les mises à jour. 

Des entreprises comme Uber ont utilisé les PWA pour offrir une expérience utilisateur transparente sur tous les appareils sans avoir besoin de plusieurs applications natives. 

### 5. Mises à jour automatiques et notifications push

Les PWA se mettent à jour de manière transparente, comme une page web chargeant le dernier contenu à chaque visite. Les utilisateurs ont toujours accès à la version la plus récente de l'application sans passer par le processus de mises à jour manuelles. Cette fonctionnalité garantit que les utilisateurs ne sont pas gênés par des versions obsolètes, un problème courant avec les applications natives. 

Par exemple, la PWA de Google Maps intègre automatiquement les dernières fonctionnalités et améliorations sans intervention de l'utilisateur. En plus de rester à jour, les PWA peuvent engager les utilisateurs avec des notifications push, comme les applications natives, les tenant informés et impliqués sans avoir besoin de visiter le magasin d'applications. 

![Image](https://www.freecodecamp.org/news/content/images/2024/01/pwass.png)
_Infographie d'une Progressive Web App (PWA) mettant en avant ses fonctionnalités : adaptabilité sur différents appareils, sécurité, fonctionnalité hors ligne, performance rapide, mises à jour et notifications push._

## Concepts de base des PWA

Pour bien comprendre le potentiel et la fonctionnalité des Progressive Web Apps, il est essentiel de connaître leurs composants fondamentaux. Ces concepts de base définissent non seulement la structure et le comportement des PWA, mais les distinguent également des applications web traditionnelles.

### Service Workers : L'épine dorsale des PWA

Les service workers sont des scripts qui s'exécutent en arrière-plan, séparément de votre page web. Ils agissent comme un proxy entre l'application web et le réseau. 

Considérez les service workers comme des assistants en coulisses pour votre application web. Leur principale tâche est de gérer la communication de votre application avec internet. 

Ils peuvent sauvegarder des parties importantes de votre application sur l'appareil de l'utilisateur, ce qui signifie que votre application peut fonctionner même sans internet. Ils sont également responsables de la mise à jour discrète du contenu de l'application et peuvent envoyer des notifications, comme une application native sur votre téléphone.

### Le Manifest de l'application : L'identité de votre PWA

Le manifest de l'application web est un fichier JSON essentiel car il indique à l'appareil de l'utilisateur comment votre application doit apparaître et se comporter. 

C'est comme la carte d'identité de votre application – il inclut le nom de l'application, les icônes qu'elle utilise, la première page qu'elle doit ouvrir et comment elle doit s'afficher (comme en plein écran). Ce fichier donne à votre application web l'impression d'être une application régulière, permettant aux utilisateurs de l'« installer » sur leur écran d'accueil.

### Mise en cache : La clé de la fonctionnalité hors ligne

Une mise en cache efficace est vitale pour une expérience hors ligne robuste. La mise en cache est comme la mémoire de votre application. Elle stocke des parties importantes de votre application pour qu'elles puissent être chargées rapidement plus tard, même sans internet. Elle est cruciale pour faire fonctionner votre application hors ligne. 

Il existe différentes façons de gérer la mise en cache, comme cache-first (où l'application vérifie le cache avant internet), network-first (l'inverse), et stale-while-revalidate (un mélange des deux). Le choix dépend de ce que fait votre application et du type d'informations qu'elle traite, affectant la manière dont votre application stocke et récupère ses données.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/pwa-components.png)
_Icônes représentant les composants clés d'une PWA : Service worker, Manifest et HTTPS_

## Aperçu de la construction d'une PWA

Construire une Progressive Web App (PWA) peut sembler complexe, mais c'est tout à fait gérable lorsque vous le décomposez en étapes. Dans cet article, je vais vous donner un aperçu du processus – et dans mon prochain tutoriel, j'entrerai dans les détails du processus.

### 1. Commencez par une page web de base :

Créez un site web simple en utilisant HTML pour la structure, CSS pour le style et JavaScript pour la fonctionnalité.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Liste de tâches PWA d'Ophy</title>
</head>
<body>
    <h1>Liste de tâches d'Ophy</h1>
    <input type="text" id="todo-input" placeholder="Ajouter une nouvelle tâche...">
    <button onclick="addTask()">Ajouter</button>
    <ul id="todo-list">
        <!-- Les tâches iront ici -->
    </ul>

    <script src="app.js"></script>
</body>
</html>

```

```css
body {
    font-family: 'Arial', sans-serif;
}

#todo-list {
    list-style-type: none;
}

#todo-list li {
    padding: 5px;
    margin: 5px;
    background-color: #f2f2f2;
    border-radius: 3px;
}

```

```javascript
function addTask() {
    var input = document.getElementById('todo-input');
    var newTask = input.value;
    if (newTask) {
        var listItem = document.createElement('li');
        listItem.textContent = newTask;
        document.getElementById('todo-list').appendChild(listItem);
        input.value = ''; // Effacer l'entrée
    }
}
```

### 2. Créez un fichier Manifest :

Dans le fichier manifest, écrivez le nom de votre application, les icônes qu'elle utilise et la première page qu'elle doit ouvrir. Cela fait que votre site web se comporte plus comme une application que vous pouvez installer.

```json
{
    "name": "Liste de tâches d'Ophy",
    "short_name": "OphyToDo",
    "icons": [
        {
            "src": "favicon.ico",
            "sizes": "64x64 32x32 24x24 16x16",
            "type": "image/x-icon"
        }
    ],
    "start_url": "/",
    "display": "standalone",
    "theme_color": "#000000",
    "background_color": "#ffffff"
}

```

### 3. Configurez un Service Worker :

Dans votre fichier JavaScript principal, ajoutez un service worker. Il s'agit d'un script spécial qui fonctionne séparément de votre site web.

Le travail du service worker est de gérer la façon dont votre application stocke et récupère les données, en particulier pour une utilisation hors ligne.

```javascript
self.addEventListener('install', function(event) {
    // Effectuer les étapes d'installation
    var CACHE_NAME = 'ophy-todo-cache-v1';
    var urlsToCache = [
        '/',
        '/styles.css',
        '/app.js'
    ];

    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(function(cache) {
                console.log('Cache ouvert');
                return cache.addAll(urlsToCache);
            })
    );
});

```

En suivant ces étapes, vous pourrez créer une PWA simple que les utilisateurs peuvent installer et utiliser, même lorsqu'ils sont hors ligne.

## Cas d'utilisation réels pour les PWA

Ces exemples concrets démontrent les avantages pratiques et l'impact des stratégies "offline-first" :

1. **Starbucks** : Starbucks dispose d'une PWA qui permet aux clients de consulter le menu et de commander des boissons et de la nourriture même lorsqu'ils sont hors ligne. Cela améliore non seulement l'expérience des clients, mais aide également à augmenter les ventes et l'interaction des clients avec la marque, car ils peuvent commander à tout moment et n'importe où.
2. **Khan Academy** : Khan Academy, un site éducatif bien connu, dispose d'une PWA permettant aux étudiants de télécharger et d'accéder à des leçons et des cours sans connexion internet. Cette fonctionnalité est particulièrement utile pour ceux qui se trouvent dans des zones avec un internet peu fiable, garantissant un apprentissage ininterrompu. Tout comme la PWA de Starbucks, l'utilisation de cette technologie par Khan Academy améliore l'expérience utilisateur, rendant l'éducation plus accessible et flexible.
3. **Trivago** : Trivago, un moteur de recherche d'hôtels populaire, a développé une PWA pour améliorer l'expérience utilisateur, en particulier pour les voyageurs avec des connexions internet instables. La PWA permet aux utilisateurs de parcourir les offres et informations d'hôtels hors ligne, rendant la planification de voyages plus flexible et accessible. Cela a conduit à une augmentation de l'engagement des utilisateurs et à des taux de conversion plus élevés, car les voyageurs peuvent continuer à interagir avec l'application même dans des zones avec une mauvaise connectivité.
4. **Forbes** : Forbes, une société médiatique mondiale de premier plan, a lancé une PWA pour améliorer l'expérience mobile de ses lecteurs. La PWA a considérablement réduit les temps de chargement et permis la lecture d'articles hors ligne. Cette innovation a non seulement amélioré l'engagement des utilisateurs, mais a également entraîné une augmentation notable de la lecture et du temps passé sur le site. La PWA de Forbes démontre comment les médias peuvent tirer parti des stratégies "offline-first" pour atteindre et fidéliser un public plus large, indépendamment de leur connectivité internet.

## Conclusion

Les PWA changent la donne dans le développement web, apportant des fonctionnalités que nous voyons habituellement dans les applications natives sur le web. 

Elles offrent un mélange de l'accessibilité des applications web avec l'expérience utilisateur engageante des applications natives. Elles représentent une solution innovante pour les entreprises et les développeurs cherchant à maximiser la portée et la fonctionnalité tout en minimisant les coûts et la complexité. 

Les PWA ne sont pas seulement une tendance passagère – elles sont la prochaine grande chose dans la façon dont nous créons et utilisons les applications web. En se concentrant sur le fonctionnement hors ligne, les PWA offrent une expérience plus fiable et conviviale. 

Que vous soyez simplement curieux ou prêt à commencer à construire, les ressources suivantes restent d'excellents points de départ pour explorer les possibilités des applications web "offline-first".

* [Liste de contrôle PWA de Google](https://developers.google.com/web/progressive-web-apps/checklist)
* [MDN Web Docs sur les Service Workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)
* [Web.dev pour les tutoriels PWA](https://web.dev/progressive-web-apps/)