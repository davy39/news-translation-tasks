---
title: Une introduction aux Progressive Web Apps
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-01-29T17:00:29.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-progressive-web-apps-6aa75f32816f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sgzup5CrdXWgrbSaw4aADA.jpeg
tags:
- name: Android
  slug: android
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Une introduction aux Progressive Web Apps
seo_desc: 'Interested in learning JavaScript? Get my ebook at jshandbook.com


  Progressive Web Apps (PWA) are the latest trend in mobile application development
  using web technologies. At the time of writing (early 2018), they’re only applicable
  to Android devic...'
---

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)

Les Progressive Web Apps (PWA) sont la dernière tendance en matière de **développement d'applications mobiles** utilisant des technologies web. Au moment de l'écriture (début 2018), elles sont **uniquement applicables aux appareils Android**.

> Les PWA arrivent sur iOS 11.3 et macOS 10.13.4, très bientôt.

WebKit, la technologie sous-jacente de Safari et Mobile Safari, a récemment (août 2017) déclaré qu'ils avaient commencé à travailler sur l'introduction des Service Workers dans le navigateur. Cela signifie qu'ils seront bientôt disponibles sur les appareils iOS également. Ainsi, le concept des Progressive Web Apps sera probablement applicable aux iPhones et iPads, si Apple décide d'encourager cette approche.

Ce n'est pas une technologie révolutionnaire nouvelle, mais plutôt un nouveau terme qui identifie un ensemble de techniques ayant pour objectif de créer une meilleure expérience pour les applications basées sur le web.

### Qu'est-ce qu'une Progressive Web App

Une Progressive Web App est une application qui peut **fournir des fonctionnalités supplémentaires en fonction de ce que l'appareil supporte**, offrant une capacité hors ligne, des notifications push, une apparence et une vitesse presque natives, et une mise en cache locale des ressources.

Cette technique a été initialement introduite par Google en 2015 et s'avère apporter de nombreux avantages tant aux développeurs qu'aux utilisateurs.

Les développeurs ont accès à la création d'applications **presque de première classe** en utilisant une pile web. Cela est toujours considérablement plus facile et moins cher que de construire des applications natives, surtout lorsque l'on considère les implications de la construction et de la maintenance d'applications multiplateformes.

Les développeurs peuvent bénéficier d'une **friction d'installation réduite**, et à une époque où avoir une application dans le store n'apporte en réalité rien en termes de découvrabilité pour 99,99 % des applications, Google search peut fournir les mêmes avantages, sinon plus.

Une Progressive Web App est un site web développé avec certaines technologies qui rendent l'expérience mobile beaucoup plus agréable qu'un site web mobile optimisé normal. Cela ressemble presque à travailler sur une application native, car elle offre les fonctionnalités suivantes :

* Support hors ligne
* Charge rapidement
* Est sécurisée
* Est capable d'émettre des notifications push
* Offre une expérience utilisateur immersive et plein écran sans la barre d'URL

Les plateformes mobiles (Android au moment de l'écriture, mais ce n'est pas techniquement limité à cela) offrent un support croissant pour les Progressive Web Apps. Elles demandent même à l'utilisateur d'**ajouter l'application à l'écran d'accueil** lorsque cet utilisateur visite un tel site.

Mais d'abord, une petite clarification sur le nom. _Progressive Web App_ peut être un **terme confus**, et une bonne définition est : des applications web qui tirent parti des fonctionnalités des navigateurs modernes (comme les web workers et le manifest des applications web) pour permettre à leurs appareils mobiles de "mettre à niveau" l'application au rôle d'une application citoyenne de première classe.

### Alternatives aux Progressive Web Apps

Comment une PWA se compare-t-elle aux alternatives lorsqu'il s'agit de créer une expérience mobile ?

Concentrons-nous sur les avantages et les inconvénients de chacune, et voyons où les PWA sont un bon choix.

#### Applications mobiles natives

Les applications mobiles natives sont le moyen le plus évident de créer une application mobile. Objective-C ou Swift sur iOS, Java/Kotlin sur Android et C# sur Windows Phone.

Chaque plateforme a ses propres conventions d'UI et d'UX, et les widgets natifs fournissent l'expérience que l'utilisateur attend. Elles peuvent être déployées et distribuées via l'App Store de la plateforme.

Le principal point de douleur avec les applications natives est que le développement multiplateforme nécessite l'apprentissage, la maîtrise et la mise à jour de nombreuses méthodologies et meilleures pratiques différentes. Si, par exemple, vous avez une petite équipe ou que vous êtes un développeur solo construisant une application sur 3 plateformes, vous devez passer beaucoup de temps à apprendre la technologie et l'environnement. Vous passerez également beaucoup de temps à gérer différentes bibliothèques et à utiliser différents flux de travail (par exemple, iCloud ne fonctionne que sur les appareils iOS — il n'y a pas de version Android).

#### Applications hybrides

Les applications hybrides sont construites en utilisant des technologies web, mais sont déployées sur l'App Store. Au milieu se trouve un framework ou un moyen d'emballer l'application afin qu'il soit possible de l'envoyer pour examen à l'App Store traditionnel.

Certaines des plateformes les plus courantes sont Phonegap et Ionic Framework, parmi beaucoup d'autres, et généralement ce que vous voyez sur la page est une WebView qui charge essentiellement un site web local.

> J'ai initialement inclus Xamarin dans la liste, mais [Carlos Eduardo Pérez](https://medium.com/@OldManCharles97?source=responses---------0----------------) a correctement souligné que Xamarin génère du code natif.

L'aspect clé des applications hybrides est le concept **"write once, run anywhere"**. Le code des différentes plateformes est généré au moment de la construction, et vous construisez des applications en utilisant JavaScript, HTML et CSS, ce qui est amazing. Les capacités de l'appareil (microphone, caméra, réseau, GPS...) sont exposées via des API JavaScript.

Le mauvais côté de la construction d'applications hybrides est que, sauf si vous faites un excellent travail, vous pourriez vous contenter de fournir un dénominateur commun. Cela crée effectivement une application qui est sous-optimale sur toutes les plateformes car l'application ignore les directives spécifiques à la plateforme pour l'interaction homme-machine.

De plus, les performances pour les vues complexes peuvent en souffrir.

#### Applications construites avec React Native

React Native expose les contrôles natifs de l'appareil mobile via une API JavaScript, mais vous créez effectivement une application native, et non en embarquant un site web dans une WebView.

Leur devise, pour distinguer cette approche des applications hybrides, est **"learn once, write anywhere"**. Cela signifie que l'approche est la même sur toutes les plateformes, mais vous allez créer des applications complètement séparées afin de fournir une excellente expérience sur chaque plateforme.

Les performances sont comparables à celles des applications natives, puisque ce que vous construisez est essentiellement une application native qui est distribuée via l'App Store.

### Fonctionnalités des Progressive Web Apps

Dans la dernière section, vous avez vu les principaux **concurrents** des Progressive Web Apps. Alors, comment les PWA se comparent-elles à celles-ci, et quelles sont leurs principales fonctionnalités ?

Rappelez-vous — actuellement, les Progressive Web Apps sont uniquement pour les appareils Android.

#### Fonctionnalités

Les Progressive Web Apps ont une chose qui les sépare complètement des approches ci-dessus : **elles ne sont pas déployées sur l'app store.**

C'est un avantage clé. L'app store est bénéfique si vous avez la portée et la chance d'être mis en avant, ce qui peut rendre votre application virale. Mais à moins d'être dans le top 0,001 %, vous n'allez pas tirer beaucoup de bénéfices à avoir votre petite place sur l'App Store.

Les Progressive Web Apps sont **découvrables en utilisant les moteurs de recherche**, et lorsqu'un utilisateur arrive sur votre site qui a des capacités PWA, **le navigateur en combinaison avec l'appareil demande à l'utilisateur s'il veut installer l'application sur l'écran d'accueil**. C'est énorme, car le SEO régulier peut s'appliquer à votre PWA, conduisant à une beaucoup moins grande dépendance à l'acquisition payante.

Ne pas être dans l'App Store signifie **que vous n'avez pas besoin de l'approbation d'Apple ou de Google** pour être dans les poches des utilisateurs. Vous pouvez publier des mises à jour quand vous voulez, sans avoir à passer par le processus d'approbation standard qui est typique des applications iOS.

Les PWA sont essentiellement des applications HTML5/sites web responsives sur stéroïdes, avec certaines technologies clés qui ont été récemment introduites pour rendre possibles certaines des fonctionnalités clés. Si vous vous souvenez, l'iPhone original est arrivé sans l'option de développer des applications natives. Les développeurs devaient développer des applications mobiles HTML5 qui pouvaient être installées sur l'écran d'accueil, mais la technologie à l'époque n'était pas prête pour cela.

Les Progressive Web Apps **fonctionnent hors ligne**.

L'utilisation des **service workers** permet à l'application d'avoir toujours du contenu frais, qui peut être téléchargé en arrière-plan, et de fournir un support pour les **notifications push**, qui offrent de meilleures opportunités de réengagement.

De plus, la possibilité de partage offre une expérience beaucoup plus agréable pour les utilisateurs qui souhaitent partager votre application, car ils ont simplement besoin d'une URL.

### Avantages

Alors, pourquoi les utilisateurs et les développeurs devraient-ils se soucier des Progressive Web Apps ?

1. Les PWA sont plus légères. Les applications natives peuvent peser 200 Mo ou plus, tandis qu'une PWA pourrait être de l'ordre des Ko.
2. Il n'y a pas de code de plateforme natif
3. Le coût d'acquisition est plus faible (il est beaucoup plus difficile de convaincre un utilisateur d'installer une application que de visiter un site web pour obtenir la première expérience)
4. Beaucoup moins d'efforts sont nécessaires pour construire et publier des mises à jour
5. Elles ont beaucoup plus de support pour les liens profonds que les applications régulières de l'app store

### Concepts de base

* **Responsive** : l'UI s'adapte à la taille de l'écran de l'appareil
* **Sensation d'application** : cela ne ressemble pas à un site web mais plutôt à une application (autant que possible)
* **Support hors ligne** : il utilisera le stockage de l'appareil pour fournir une expérience hors ligne
* **Installable** : le navigateur de l'appareil invite l'utilisateur à installer votre application
* **Réengagement** : les notifications push aident les utilisateurs à redécouvrir votre application une fois installée
* **Découvrable** : les moteurs de recherche et l'optimisation SEO peuvent fournir beaucoup plus d'utilisateurs que l'app store
* **Frais** : l'application se met à jour elle-même et le contenu une fois qu'elle est en ligne
* **Sécurisée** : elle utilise HTTPS
* **Progressive** : elle fonctionnera sur n'importe quel appareil, même les plus anciens, même si elle a moins de fonctionnalités (par exemple, juste comme un site web, non installable)
* **Liable** : il est facile de pointer vers elle en utilisant des URL

### Service Workers

Une partie de la définition des Progressive Web Apps est qu'elles doivent fonctionner hors ligne.

Puisque la chose qui permet à l'application web de fonctionner hors ligne est le Service Worker, cela implique que **les Service Workers sont une partie obligatoire d'une Progressive Web App**.

ATTENTION : Les Service Workers sont actuellement uniquement supportés par Chrome (Desktop et Android), Firefox et Opera. Voir [http://caniuse.com/#feat=serviceworkers](http://caniuse.com/#feat=serviceworkers) pour des données mises à jour sur le support.

ASTUCE : Ne confondez pas les Service Workers avec les Web Workers. Ce sont des choses complètement différentes.

Un Service Worker est un fichier JavaScript qui agit comme un intermédiaire entre l'application web et le réseau. Grâce à cela, il peut fournir des services de cache, accélérer le rendu de l'application et améliorer l'expérience utilisateur.

Pour des raisons de sécurité, seuls les sites HTTPS peuvent utiliser les Service Workers, et c'est l'une des raisons pour lesquelles une Progressive Web App doit être servie via HTTPS.

Les Service Workers ne sont pas disponibles sur l'appareil la première fois que l'utilisateur visite l'application. Lors de la première visite, le service worker est installé, puis lors des visites suivantes sur des pages séparées du site, ce Service Worker sera appelé.

> **Consultez le [guide complet des Service Workers](https://flaviocopes.com/service-workers/)**

### Le Manifest de l'Application

Le Manifest de l'Application est un fichier JSON que vous pouvez utiliser pour fournir à l'appareil des informations sur votre Progressive Web App.

Vous ajoutez un lien vers le manifest dans **chaque** en-tête de chaque page de votre site web :

```
<link rel="manifest" href="/manifest.webmanifest">
```

Ce fichier indiquera à l'appareil comment définir :

* Le nom et le nom court de l'application
* Les emplacements des icônes, en diverses tailles
* L'URL de démarrage, relative au domaine
* L'orientation par défaut
* L'écran de démarrage

#### Exemple

```
{   "name": "The Weather App",   "short_name": "Weather",   "description": "Exemple de Progressive Web App",   "icons": [{    "src": "images/icons/icon-128x128.png",    "sizes": "128x128",    "type": "image/png"   }, {     "src": "images/icons/icon-144x144.png",    "sizes": "144x144",     "type": "image/png"   }, {     "src": "images/icons/icon-152x152.png",    "sizes": "152x152",     "type": "image/png"   }, {     "src": "images/icons/icon-192x192.png",    "sizes": "192x192",     "type": "image/png"   }, {     "src": "images/icons/icon-256x256.png",     "sizes": "256x256",     "type": "image/png"   }],   "start_url": "/index.html?utm_source=app_manifest",   "orientation": "portrait",   "display": "standalone",   "background_color": "#3E4EB8",  "theme_color": "#2F3BA2" }
```

Le Manifest de l'Application est un projet de travail du W3C, accessible à l'adresse [https://www.w3.org/TR/appmanifest/](https://www.w3.org/TR/appmanifest/)

### L'App Shell

L'App Shell n'est pas une technologie mais plutôt un **concept de design**. Il vise à charger et à rendre le conteneur de l'application web en premier, et le contenu réel peu après, pour donner à l'utilisateur une belle impression d'application.

Prenez, par exemple, la suggestion des directives d'interface humaine d'Apple d'utiliser un écran de démarrage qui ressemble à l'interface utilisateur. Cela fournit un indice psychologique qui a été trouvé pour réduire la perception que l'application mettait longtemps à charger.

#### Mise en cache

L'App Shell est mise en cache séparément du contenu, et elle est configurée de sorte que la récupération des éléments de construction de la coque à partir du cache prend très peu de temps.

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)