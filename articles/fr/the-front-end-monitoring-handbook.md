---
title: 'Le manuel de surveillance front-end : suivi des performances, des erreurs
  et du comportement des utilisateurs'
subtitle: ''
author: Gordan Tan
co_authors: []
series: null
date: '2025-06-03T01:55:18.334Z'
originalURL: https://freecodecamp.org/news/the-front-end-monitoring-handbook
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1748915696356/6e6edeed-2f41-40f9-97d6-8cc8686c3b25.png
tags:
- name: Frontend Development
  slug: frontend-development
- name: JavaScript
  slug: javascript
- name: monitoring
  slug: monitoring
- name: frontend
  slug: frontend
seo_title: 'Le manuel de surveillance front-end : suivi des performances, des erreurs
  et du comportement des utilisateurs'
seo_desc: 'A complete frontend monitoring system is essential for tracking application
  performance, errors, and user behavior. It consists of three main components: data
  collection and reporting, data processing and storage, and data visualization.

  This article...'
---

Un système complet de surveillance front-end est essentiel pour suivre les performances de l'application, les erreurs et le comportement des utilisateurs. Il se compose de trois composants principaux : la collecte et le rapport des données, le traitement et le stockage des données, et la visualisation des données.

Cet article se concentre spécifiquement sur le premier composant – la collecte et le rapport des données – et vous montre comment construire un SDK de surveillance à partir de zéro. À la fin de cet article, vous comprendrez comment recueillir des métriques critiques sur les performances de votre application, capturer les erreurs, suivre le comportement des utilisateurs et mettre en œuvre des mécanismes de rapport efficaces.

Voici un aperçu des sujets que nous allons couvrir :

```javascript
                       ┌──────────────────────┐
                       │  Data Collection   │
                       └──────────┬──────────┘
                                  │
         ┌──────────────────────┐  │  ┌──────────────────────┐
         │                 │                     │
┌─────────┴─────────┐ ┌─────┴─────┐ ┌─────────┴─────────┐
│ Error Monitoring │ │ Performance  │     │ Behavior       │
│                  │ │ Monitoring   │     │ Monitoring     │
└─────────┬─────────┘ └─────┬─────┘     └─────────┬─────────┘
         │                  │                     │
┌─────────┴─────────┐ ┌─────┴─────┐  ┌─────────┴─────────┐
│                 │ │                 │  │                 │
│ Resource Loading│ │ Resource Loading│  │     UV, PV      │
│     Errors      │ │      Time       │  │                 │
│                 │ │                 │  │  Page Access    │
│   JS Errors     │ │  API Request    │  │     Depth       │
│                 │ │     Time        │  │                 │
│ Promise Errors  │ │                 │  │   Page Stay     │
│                 │ │   DNS, TCP,     │  │    Duration     │
│ Custom Errors   │ │ First-byte Time │  │                 │
│                 │ │                 │  │  Custom Event   │
│                 │ │   FPS Rate      │  │    Tracking     │
│                 │ │                 │  │                 │
│                 │ │ Cache Hit Rate  │  │   User Clicks   │
│                 │ │                 │  │                 │
│                 │ │  First Screen   │  │ Page Navigation │
│                 │ │  Render Time    │  │                 │
│                 │ │                 │  └─────────────────┘
│                 │ │  FP, FCP, LCP,  │
│                 │ │   FID, LCS,     │
│                 │ │ DOMContentLoaded│
│                 │ │    onload       │
└─────────────────┘ └─────────────────┘
```

Une fois les données collectées, elles doivent être rapportées à vos systèmes backend pour traitement et analyse :

```javascript
                  ┌──────────────────────┐
                  │ Data Reporting  │
                  └──────────┬──────────┘
                           │
          ┌──────────────────────┐  ┌──────────────────────┐
          │                                 │
┌─────────┴─────────┐           ┌─────────┴─────────┐
│  Reporting Methods  │           │  Reporting Timing   │
└─────────┬─────────┘           └─────────┬─────────┘
           │                                 │
     ┌─────┴─────┐               ┌─────────┴─────────┐
     │     │     │               │           │           │
┌────┴─────┐ ┌────┴─────┐ ┌─────────┴─────────┐ ┌────┴─────────────────┐
│  xhr   │ │ image  │ │ requestIdle     │ │ Upload when cache │
└─────────┘ │         │ │ Callback/       │ │ limit is reached  │
           │ setTimeout      │ │                 │
     ┌─────┴─────┐      └─────────────────────┘
     │ sendBeacon│                          │
     └───────────┘                ┌─────────────────────┐
                                  │    beforeunload    │
                                  └─────────────────────┘
```

## **Prérequis**

Avant de plonger dans ce tutoriel, vous devriez avoir :

* Des connaissances de base en JavaScript et en développement web

* Une familiarité avec les API du navigateur et la gestion des événements

* Une compréhension des concepts de programmation asynchrone

* Une certaine expérience avec les concepts d'optimisation des performances

Puisque les connaissances théoriques seules peuvent être difficiles à saisir, j'ai créé un simple [SDK de surveillance](https://github.com/woai3c/monitor-demo) qui implémente ces concepts techniques. Vous pouvez l'utiliser pour créer des démonstrations simples et mieux comprendre. La lecture de cet article tout en expérimentant avec le SDK offrira la meilleure expérience d'apprentissage.

## Table des matières

1. [Collecter les données de performance](#heading-installation)

    * [FP (First Paint)](##heading-fp-first-paint)

    * [FCP (First Contentful Paint)](#heading-fcp-first-contentful-paint)

    * [LCP (Largest Contentful Paint)](#heading-lcp-largest-contentful-paint)

    * [CLS (Cumulative Layout Shift)](#heading-cls-cumulative-layout-shift)

    * [Événements DOMContentLoaded et Load](#heading-domcontentloaded-and-load-events)

    * [Temps de rendu de la première page](#heading-first-screen-rendering-time)

    * [Temps de requête API](#heading-api-request-timing)

    * [Temps de chargement des ressources et taux de succès du cache](#heading-resource-loading-time-and-cache-hit-rate)

    * [Cache de retour/avant du navigateur](#heading-browser-backforward-cache-bfc)

    * [FPS](#heading-fps)

    * [Temps de rendu des changements de routeur Vue](#heading-vue-router-change-rendering-time)

2. [Collecte des données d'erreur](#heading-error-data-collection)

    * [Erreurs de chargement des ressources](#heading-resource-loading-errors)

    * [Erreurs JavaScript](#heading-javascript-errors)

    * [Erreurs de promesse](#heading-promise-errors)

    * [Sourcemap](#heading-sourcemap)

    * [Erreurs Vue](#heading-vue-errors)

3. [Collecte des données de comportement](#heading-behavior-data-collection)

    * [PV et UV](#heading-pv-and-uv)

    * [Durée de la visite de la page](#heading-page-stay-duration)

    * [Profondeur d'accès à la page](#heading-page-access-depth)

    * [Clics des utilisateurs](#heading-user-clicks)

    * [Navigation de la page](#heading-page-navigation)

    * [Changements de routeur Vue](#heading-vue-router-changes)

4. [Rapport de données](#heading-data-reporting)

    * [Méthodes de rapport](#heading-reporting-methods)

    * [Temporisation du rapport](#heading-reporting-timing)

5. [Résumé](#heading-summary)

6. [Références](#heading-references)

    * [Surveillance des performances](#heading-performance-monitoring)

    * [Surveillance des erreurs](#heading-error-monitoring)

    * [Surveillance du comportement](#heading-behavior-monitoring)

## Collecter les données de performance

La surveillance des performances est cruciale pour offrir aux utilisateurs une expérience fluide et réactive. Les sites web lents entraînent des taux de rebond plus élevés et des conversions réduites. En collectant des métriques de performance, vous pouvez identifier les goulots d'étranglement, optimiser les chemins de rendu critiques et améliorer la satisfaction globale des utilisateurs.

L'équipe de développement de Chrome a proposé une série de métriques pour surveiller les performances des pages, chacune mesurant un aspect différent de l'expérience utilisateur :

* **FP (First Paint)** – Temps écoulé entre le début du chargement de la page et le moment où le premier pixel est peint à l'écran (essentiellement le temps de l'écran blanc)

* **FCP (First Contentful Paint)** – Temps écoulé entre le début du chargement de la page et le moment où une partie du contenu de la page est rendue

* **LCP (Largest Contentful Paint)** – Temps écoulé entre le début du chargement de la page et le moment où le plus grand bloc de texte ou élément image termine le rendu

* **CLS (Cumulative Layout Shift)** – Score cumulé de tous les décalages de mise en page inattendus se produisant entre le début du chargement de la page et le moment où l'état du cycle de vie de la page devient caché

Nous pouvons obtenir ces quatre métriques de performance grâce à [PerformanceObserver](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceObserver) (elles peuvent également être récupérées via `performance.getEntriesByName()`, mais cette méthode ne fournit pas de notifications en temps réel lorsque les événements se produisent). PerformanceObserver est une interface de surveillance des performances utilisée pour observer les événements de mesure des performances.

Examinons chacune de ces métriques en détail et voyons comment les implémenter dans notre SDK.

### FP (First Paint)

First Paint (FP) marque le point où le navigateur rend quelque chose de visuellement différent de ce qui était à l'écran avant la navigation. Cela pourrait être un changement de couleur de fond ou tout élément visuel indiquant à l'utilisateur que la page est en cours de chargement.

Code d'implémentation :

```javascript
const entryHandler = (list) => {
    for (const entry of list.getEntries()) {
        if (entry.name === 'first-paint') {
            observer.disconnect()
        }
        console.log(entry)
    }
}

const observer = new PerformanceObserver(entryHandler)
// La propriété buffered indique s'il faut observer les données mises en cache, 
// permettant l'observation même si le code de surveillance est ajouté après l'événement
observer.observe({ type: 'paint', buffered: true })
```

Ce code crée un nouvel PerformanceObserver qui surveille les événements de type 'paint'. Lorsque l'événement first-paint se produit, il enregistre les informations d'entrée et déconnecte l'observateur puisque nous devons capturer cet événement une seule fois par chargement de page. La méthode `observe()` de l'observateur est configurée avec `buffered: true` pour nous assurer de pouvoir attraper les événements de peinture qui se sont produits avant que notre code ne s'exécute.

La sortie de mesure FP :

```javascript
{
    duration: 0,
    entryType: "paint",
    name: "first-paint",
    startTime: 359, // Temps FP
}
```

La valeur `startTime` représente le temps de peinture dont nous avons besoin. Cette valeur (359ms dans cet exemple) nous indique combien de temps il a fallu depuis le début de la navigation jusqu'à ce que le premier changement visuel apparaisse à l'écran. Vous pouvez utiliser cette métrique pour optimiser votre chemin de rendu critique et réduire le temps que les utilisateurs passent à regarder un écran vide.

### FCP (First Contentful Paint)

FCP (First Contentful Paint) fait référence au temps écoulé entre le début du chargement de la page et le moment où une partie du contenu de la page est rendue. Le "contenu" dans cette métrique fait référence au texte, aux images (y compris les images de fond), aux éléments `<svg>` et aux éléments `<canvas>` non blancs.

[![Visualisation FCP montrant le contenu peint à l'écran](https://camo.githubusercontent.com/8a8b6762583fbb357b8ac6488a1f972e583bab8e6dfaab599e9a5ca3ea5e2403/68747470733a2f2f70362d6a75656a696e2e62797465696d672e636f6d2f746f732d636e2d692d6b3375316662706663702f61346631633962363130323934343864616532623163666235376234656637357e74706c762d6b3375316662706663702d77617465726d61726b2e696d6167653f align="left")](https://camo.githubusercontent.com/8a8b6762583fbb357b8ac6488a1f972e583bab8e6dfaab599e9a5ca3ea5e2403/68747470733a2f2f70362d6a75656a696e2e62797465696d672e636f6d2f746f732d636e2d692d6b3375316662706663702f61346631633962363130323934343864616532623163666235376234656637357e74706c762d6b3375316662706663702d77617465726d61726b2e696d6167653f)

Pour offrir une bonne expérience utilisateur, le score FCP doit être maintenu en dessous de 1,8 seconde.

[![Échelle de notation FCP : Bonne (0-1,8s), Besoin d'amélioration (1,8-3s), Mauvaise (3s+)](https://camo.githubusercontent.com/5a0734e52cbed48e8639fe185204c237fd658e5d60560b18578c848d74dac12c/68747470733a2f2f70332d6a75656a696e2e62797465696d672e636f6d2f746f732d636e2d692d6b3375316662706663702f39383138633636383739623334356533623438343566663366653031653863397e74706c762d6b3375316662706663702d77617465726d61726b2e696d6167653f align="left")](https://camo.githubusercontent.com/5a0734e52cbed48e8639fe185204c237fd658e5d60560b18578c848d74dac12c/68747470733a2f2f70332d6a75656a696e2e62797465696d672e636f6d2f746f732d636e2d692d6b3375316662706663702f39383138633636383739623334356533623438343566663366653031653863397e74706c762d6b3375316662706663702d77617465726d61726b2e696d6167653f)

Le code de mesure :

```javascript
const entryHandler = (list) => {
    for (const entry of list.getEntries()) {
        if (entry.name === 'first-contentful-paint') {
            observer.disconnect()
        }

        console.log(entry)
    }
}

const observer = new PerformanceObserver(entryHandler)
observer.observe({ type: 'paint', buffered: true })
```

Nous pouvons obtenir la valeur de FCP via le code ci-dessus :

```javascript
{
    duration: 0,
    entryType: "paint",
    name: "first-contentful-paint",
    startTime: 459, // temps fcp
}
```

La valeur `startTime` est le temps de peinture dont nous avons besoin.

### LCP (Largest Contentful Paint)

LCP (Largest Contentful Paint) fait référence au temps écoulé entre le début du chargement de la page et le moment où le plus grand bloc de texte ou élément image termine le rendu. La métrique LCP rapporte le temps de rendu relatif de la plus grande image ou bloc de texte visible dans la fenêtre d'affichage, mesuré à partir du moment où la page commence à se charger.

Un bon score LCP doit être maintenu en dessous de 2,5 secondes.

[![Échelle de notation LCP : Bonne (0-2,5s), Besoin d'amélioration (2,5-4s), Mauvaise (4s+)](https://camo.githubusercontent.com/76d0f2b9a24d36f12714e9ce39a61ce426eda6ae087c643745c71337352d5c27/68747470733a2f2f70392d6a75656a696e2e62797465696d672e636f6d2f746f732d636e2d692d6b3375316662706663702f63303930646438623034326334366432616461626135333935636136386634377e74706c762d6b3375316662706663702d77617465726d61726b2e696d6167653f align="left")](https://camo.githubusercontent.com/76d0f2b9a24d36f12714e9ce39a61ce426eda6ae087c643745c71337352d5c27/68747470733a2f2f70392d6a75656a696e2e62797465696d672e636f6d2f746f732d636e2d692d6b3375316662706663702f63303930646438623034326334366432616461626135333935636136386634377e74706c762d6b3375316662706663702d77617465726d61726b2e696d6167653f)

Le code de mesure :

```javascript
const entryHandler = (list) => {
    if (observer) {
        observer.disconnect()
    }

    for (const entry of list.getEntries()) {
        console.log(entry)
    }
}

const observer = new PerformanceObserver(entryHandler)
observer.observe({ type: 'largest-contentful-paint', buffered: true })
```

Nous pouvons obtenir la valeur de LCP via le code ci-dessus :

```javascript
{
    duration: 0,
    element: p,
    entryType: "largest-contentful-paint",
    id: "",
    loadTime: 0,
    name: "",
    renderTime: 1021.299,
    size: 37932,
    startTime: 1021.299,
    url: "",
}
```

La valeur `startTime` est le temps de peinture dont nous avons besoin. Et `element` fait référence à l'élément peint pendant LCP.

La différence entre FCP et LCP est : l'événement FCP se produit lorsque n'importe quel contenu est peint, tandis que l'événement LCP se produit lorsque le plus grand contenu finit de se rendre.

[![Comparaison des temps FCP et LCP sur la chronologie de chargement de la page web](https://camo.githubusercontent.com/ed1fac2eb0ad92326cb76a6f71f7c661164d881fe13f18e8de9a1d7f9423ad53/68747470733a2f2f70332d6a75656a696e2e62797465696d672e636f6d2f746f732d636e2d692d6b3375316662706663702f30653634363337616339643234336135383130316438656430316665383836657e74706c762d6b3375316662706663702d77617465726d61726b2e696d6167653f align="left")](https://camo.githubusercontent.com/ed1fac2eb0ad92326cb76a6f71f7c661164d881fe13f18e8de9a1d7f9423ad53/68747470733a2f2f70332d6a75656a696e2e62797465696d672e636f6d2f746f732d636e2d692d6b3375316662706663702f30653634363337616339643234336135383130316438656430316665383836657e74706c762d6b3375316662706663702d77617465726d61726b2e696d6167653f)

LCP considère ces éléments :

* Éléments `<img>`

* Éléments `<image>` à l'intérieur de `<svg>`

* Éléments `<video>` (utilisant des images de poster)

* Éléments avec des images de fond chargées via la fonction [`url()`](https://developer.mozilla.org/docs/Web/CSS/url\(\)) (n'utilisant pas de [dégradés CSS](https://developer.mozilla.org/docs/Web/CSS/CSS_Images/Using_CSS_gradients))

* Éléments de niveau bloc contenant des nœuds de texte ou d'autres éléments de texte de niveau en ligne

### CLS (Cumulative Layout Shift)

CLS (Cumulative Layout Shift) fait référence au score cumulé de tous les décalages de mise en page inattendus se produisant entre le début du chargement de la page et le moment où l'état du cycle de vie de la page devient caché.

Un "décalage de mise en page inattendu" se produit lorsque des éléments sur une page se déplacent sans interaction de l'utilisateur. Voici quelques exemples courants :

* Une bannière ou une publicité apparaît soudainement en haut de la page, repoussant le contenu vers le bas

* Une police se charge et change la taille du texte

* Une image se charge sans dimensions prédéfinies, s'étend et repousse d'autres contenus

* Un bouton apparaît en dessous de l'endroit où un utilisateur est sur le point de cliquer, l'amenant à cliquer sur le mauvais élément

Ces décalages sont frustrants pour les utilisateurs et entraînent des clics accidentels, une perte de position de lecture et une mauvaise expérience utilisateur globale. CLS aide à quantifier ce problème afin que vous puissiez identifier et corriger les éléments problématiques.

Le score de décalage de mise en page est calculé comme suit :

```javascript
score de décalage de mise en page = score d'impact × score de distance
```

Le [score d'impact](https://github.com/WICG/layout-instability#Impact-Fraction) mesure comment les éléments instables affectent la zone visible entre deux images. Le score de distance est calculé en prenant la plus grande distance qu'un élément instable a parcourue (horizontalement ou verticalement) et en la divisant par la plus grande dimension de la fenêtre d'affichage (largeur ou hauteur, selon la plus grande).

**CLS est la somme de tous les scores de décalage de mise en page.**

Un décalage de mise en page se produit lorsqu'un élément DOM change de position entre deux images rendues, comme illustré ci-dessous :

[![Visualisation du décalage de mise en page montrant le changement de position de l'élément](https://camo.githubusercontent.com/d70250d691a70bb776e1b6748c2b39c7c8ebf17a5e0299bc0bebe064a4d44d91/68747470733a2f2f70362d6a75656a696e2e62797465696d672e636f6d2f746f732d636e2d692d6b3375316662706663702f66663037643431633632343234386131623636633537363166303438326632637e74706c762d6b3375316662706663702d77617465726d61726b2e696d6167653f align="left")](https://camo.githubusercontent.com/d70250d691a70bb776e1b6748c2b39c7c8ebf17a5e0299bc0bebe064a4d44d91/68747470733a2f2f70362d6a75656a696e2e62797465696d672e636f6d2f746f732d636e2d692d6b3375316662706663702f66663037643431633632343234386131623636633537363166303438326632637e74706c762d6b3375316662706663702d77617465726d61726b2e696d6167653f)

[![Illustration du mouvement du rectangle démontrant le décalage de mise en page de haut-gauche à droite](https://camo.githubusercontent.com/826f631d4e71a8eb8f53738821f788c864988cff7fae350b77a43b3b3c22d331/68747470733a2f2f70332d6a75656a696e2e62797465696d672e636f6d2f746f732d636e2d692d6b3375316662706663702f64306435616238313030633934383961393931646430626538653139386166307e74706c762d6b3375316662706663702d77617465726d61726b2e696d6167653f align="left")](https://camo.githubusercontent.com/826f631d4e71a8eb8f53738821f788c864988cff7fae350b77a43b3b3c22d331/68747470733a2f2f70332d6a75656a696e2e62797465696d672e636f6d2f746f732d636e2d692d6b3375316662706663702f64306435616238313030633934383961393931646430626538653139386166307e74706c762d6b3375316662706663702d77617465726d61726b2e696d6167653f)

Dans le diagramme ci-dessus, le rectangle se déplace de haut-gauche vers le côté droit, comptant comme un décalage de mise en page. En termes de CLS, il existe un concept appelé "fenêtre de session" : un ou plusieurs décalages de mise en page individuels se produisant en succession rapide, avec moins d'une seconde entre chaque décalage et une durée maximale de fenêtre de 5 secondes.

[![Concept de fenêtre de session montrant plusieurs décalages de mise en page groupés dans des contraintes de temps](https://camo.githubusercontent.com/e2a49800b87d502b7a81f69ebc4259c27ec3c101faac3a65df30cd080ec29a85/68747470733a2f2f70392d6a75656a696e2e62797465696d672e636f6d2f746f732d636e2d692d6b3375316662706663702f63366166326563353639363434303133393632363435383230656662313664337e74706c762d6b3375316662706663702d77617465726d61726b2e696d6167653f align="left")](https://camo.githubusercontent.com/e2a49800b87d502b7a81f69ebc4259c27ec3c101faac3a65df30cd080ec29a85/68747470733a2f2f70392d6a75656a696e2e62797465696d672e636f6d2f746f732d636e2d692d6b3375316662706663702f63366166326563353639363434303133393632363435383230656662313664337e74706c762d6b3375316662706663702d77617465726d61726b2e696d6167653f)

Par exemple, dans la deuxième fenêtre de session illustrée ci-dessus, il y a quatre décalages de mise en page. Chaque décalage doit se produire moins d'une seconde après le précédent, et le temps entre le premier et le dernier décalage ne doit pas dépasser cinq secondes pour être considéré comme une fenêtre de session. Si ces conditions ne sont pas remplies, il est considéré comme une nouvelle fenêtre de session. Cette spécification provient de nombreuses expérimentations et recherches de l'équipe Chrome, comme détaillé dans [Evolving the CLS metric](https://web.dev/blog/evolving-cls).

CLS a trois méthodes de calcul :

1. Cumulatif

2. Moyenne de toutes les fenêtres de session

3. Maximum de toutes les fenêtres de session

#### **Cumulatif**

Cette méthode additionne tous les scores de décalage de mise en page à partir du début du chargement de la page. Cependant, cette approche désavantage les pages à longue durée de vie - plus une page est ouverte longtemps, plus le score CLS devient élevé.

#### **Moyenne de toutes les fenêtres de session**

Cette méthode calcule en fonction des fenêtres de session plutôt que des décalages de mise en page individuels, en prenant la moyenne de tous les scores des fenêtres de session. Cependant, cette approche a des limitations.

[![Comparaison des fenêtres de session avec différents scores CLS montrant les limitations de la moyenne](https://camo.githubusercontent.com/b4e2797c9a0b1de2c2f0c291374a53cfcb6b5d84c79c4d045ce2a78de1ed22fc/68747470733a2f2f70362d6a75656a696e2e62797465696d672e636f6d2f746f732d636e2d692d6b3375316662706663702f34326535323038643833663334396462383463663461323731393461353766327e74706c762d6b3375316662706663702d77617465726d61726b2e696d6167653f align="left")](https://camo.githubusercontent.com/b4e2797c9a0b1de2c2f0c291374a53cfcb6b5d84c79c4d045ce2a78de1ed22fc/68747470733a2f2f70362d6a75656a696e2e62797465696d672e636f6d2f746f732d636e2d692d6b3375316662706663702f34326535323038643833663334396462383463663461323731393461353766327e74706c762d6b3375316662706663702d77617465726d61726b2e696d6167653f)

Comme montré ci-dessus, si la première fenêtre de session a un score CLS élevé et la deuxième un score bas, les moyenner masque le comportement réel de la page. La moyenne ne reflète pas que la page avait plus de décalages au début et moins par la suite.

#### **Maximum de toutes les fenêtres de session**

C'est actuellement la méthode de calcul optimale, utilisant le score de fenêtre de session le plus élevé pour refléter le pire scénario pour les décalages de mise en page. Pour plus de détails, voir [Evolving the CLS metric](https://web.dev/blog/evolving-cls).

Voici le code d'implémentation pour la troisième méthode de calcul :

```javascript
let sessionValue = 0
let sessionEntries = []
const cls = {
    subType: 'layout-shift',
    name: 'layout-shift',
    type: 'performance',
    pageURL: getPageURL(),
    value: 0,
}

const entryHandler = (list) => {
    for (const entry of list.getEntries()) {
        // Ne compter que les décalages de mise en page sans entrée utilisateur récente.
        if (!entry.hadRecentInput) {
            const firstSessionEntry = sessionEntries[0]
            const lastSessionEntry = sessionEntries[sessionEntries.length - 1]

            // Si l'entrée s'est produite moins d'une seconde après l'entrée précédente et
            // moins de 5 secondes après la première entrée dans la session, inclure l'
            // entrée dans la session actuelle. Sinon, commencer une nouvelle session.
            if (
                sessionValue
                && entry.startTime - lastSessionEntry.startTime < 1000
                && entry.startTime - firstSessionEntry.startTime < 5000
            ) {
                sessionValue += entry.value
                sessionEntries.push(formatCLSEntry(entry))
            } else {
                sessionValue = entry.value
                sessionEntries = [formatCLSEntry(entry)]
            }

            // Si la valeur de la session actuelle est plus grande que la valeur CLS actuelle,
            // mettre à jour CLS et les entrées qui y contribuent.
            if (sessionValue > cls.value) {
                cls.value = sessionValue
                cls.entries = sessionEntries
                cls.startTime = performance.now()
                lazyReportCache(deepCopy(cls))
            }
        }
    }
}

const observer = new PerformanceObserver(entryHandler)
observer.observe({ type: 'layout-shift', buffered: true })
```

Une seule mesure de décalage de mise en page contient les données suivantes :

```javascript
{
  duration: 0,
  entryType: "layout-shift",
  hadRecentInput: false,
  lastInputTime: 0,
  name: "",
  sources: (2) [LayoutShiftAttribution, LayoutShiftAttribution],
  startTime: 1176.199999999255,
  value: 0.000005752046026677329,
}
```

Le champ `value` représente le score de décalage de mise en page.

### **Événements DOMContentLoaded et Load**

L'événement `DOMContentLoaded` est déclenché lorsque le HTML est entièrement chargé et analysé, sans attendre le chargement des CSS, des images et des iframes.

L'événement `load` est déclenché lorsque la page entière et toutes les ressources dépendantes telles que les feuilles de style et les images ont terminé leur chargement.

Bien que ces métriques de performance soient plus anciennes, elles fournissent toujours des informations précieuses sur le comportement de la page. Leur surveillance reste nécessaire.

```javascript
import { lazyReportCache } from '../utils/report'

['load', 'DOMContentLoaded'].forEach(type => onEvent(type))

function onEvent(type) {
    function callback() {
        lazyReportCache({
            type: 'performance',
            subType: type.toLocaleLowerCase(),
            startTime: performance.now(),
        })

        window.removeEventListener(type, callback, true)
    }

    window.addEventListener(type, callback, true)
}
```

### **Temps de rendu de la première page**

Dans la plupart des cas, le temps de rendu de la première page peut être obtenu via l'événement `load`. Cependant, il existe des exceptions, comme les images et les éléments DOM chargés de manière asynchrone.

```javascript
<script>
    setTimeout(() => {
        document.body.innerHTML = `
            <div>
                <!-- beaucoup de code... -->
            </div>
        `
    }, 3000)
</script>
```

Dans de tels cas, nous ne pouvons pas obtenir le temps de rendu de la première page via l'événement `load`. Au lieu de cela, nous devons utiliser [MutationObserver](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver/MutationObserver) pour obtenir le temps de rendu de la première page. MutationObserver déclenche des événements lorsque les propriétés des éléments DOM qu'il surveille changent.

Le processus de calcul du temps de rendu de la première page :

1. Utiliser MutationObserver pour surveiller l'objet document, déclenchant des événements chaque fois que les propriétés des éléments DOM changent.

2. Vérifier si l'élément DOM est dans la première page. Si c'est le cas, appeler `performance.now()` dans la fonction de rappel `requestAnimationFrame()` pour obtenir l'heure actuelle comme temps de rendu.

3. Comparer le temps de rendu du dernier élément DOM avec le temps de chargement de toutes les images de la première page, et utiliser la valeur maximale comme temps de rendu de la première page.

#### **Surveillance du DOM**

```javascript
const next = window.requestAnimationFrame ? requestAnimationFrame : setTimeout
const ignoreDOMList = ['STYLE', 'SCRIPT', 'LINK']

observer = new MutationObserver(mutationList => {
    const entry = {
        children: [],
    }

    for (const mutation of mutationList) {
        if (mutation.addedNodes.length && isInScreen(mutation.target)) {
             // ...
        }
    }

    if (entry.children.length) {
        entries.push(entry)
        next(() => {
            entry.startTime = performance.now()
        })
    }
})

observer.observe(document, {
    childList: true,
    subtree: true,
})
```

Le code ci-dessus surveille les changements du DOM tout en filtrant les balises `style`, `script` et `link`.

#### **Vérification si l'élément est dans la première page**

Une page peut avoir beaucoup de contenu, mais les utilisateurs ne peuvent voir qu'un écran à la fois. Par conséquent, lors du calcul du temps de rendu de la première page, nous devons limiter la portée au contenu visible dans l'écran actuel.

```javascript
const viewportWidth = window.innerWidth
const viewportHeight = window.innerHeight

// Vérifier si l'élément DOM est à l'écran
function isInScreen(dom) {
    const rectInfo = dom.getBoundingClientRect()
    if (
        rectInfo.left >= 0 
        && rectInfo.left < viewportWidth
        && rectInfo.top >= 0
        && rectInfo.top < viewportHeight
    ) {
        return true
    }
}
```

#### **Utilisation de** `requestAnimationFrame()` pour obtenir le temps de rendu du DOM

Lorsque les changements de DOM déclenchent l'événement MutationObserver, cela signifie seulement que le contenu du DOM peut être lu, pas qu'il a été peint à l'écran.

[![Pipeline de rendu du navigateur montrant le contenu DOM chargé mais pas encore peint](https://camo.githubusercontent.com/1c118ccd17b38cf8054796f978f864bcb055b3db7659b9c4b84acc349c978531/68747470733a2f2f70332d6a75656a696e2e62797465696d672e636f6d2f746f732d636e2d692d6b3375316662706663702f36373233306335653538666634633639396265373735383635366534353034667e74706c762d6b3375316662706663702d77617465726d61726b2e696d6167653f align="left")](https://camo.githubusercontent.com/1c118ccd17b38cf8054796f978f864bcb055b3db7659b9c4b84acc349c978531/68747470733a2f2f70332d6a75656a696e2e62797465696d672e636f6d2f746f732d636e2d692d6b3375316662706663702f36373233306335653538666634633639396265373735383635366534353034667e74706c762d6b3375316662706663702d77617465726d61726b2e696d6167653f)

Comme montré dans l'image ci-dessus, lorsque l'événement MutationObserver est déclenché, nous pouvons lire que `document.body` a déjà du contenu, mais le côté gauche de l'écran n'a encore rien peint. Par conséquent, nous devons appeler `requestAnimationFrame()` pour obtenir l'heure actuelle comme temps de rendu du DOM après que le navigateur a réussi à le peindre.

#### **Comparaison avec tous les temps de chargement des images dans la première page**

```javascript
function getRenderTime() {
    let startTime = 0
    entries.forEach(entry => {
        if (entry.startTime > startTime) {
            startTime = entry.startTime
        }
    })

    // Il faut comparer avec tous les temps de chargement des images dans la page actuelle, prendre le maximum
    // Le temps de requête de l'image doit être inférieur à startTime, le temps de fin de réponse doit être supérieur à startTime
    performance.getEntriesByType('resource').forEach(item => {
        if (
            item.initiatorType === 'img'
            && item.fetchStart < startTime 
            && item.responseEnd > startTime
        ) {
            startTime = item.responseEnd
        }
    })
    
    return startTime
}
```

#### **Optimisation**

Le code actuel a encore besoin d'optimisation, avec deux points principaux à considérer :

1. Quand devons-nous rapporter le temps de rendu ?

2. Comment gérer les éléments DOM ajoutés de manière asynchrone ?

Pour le premier point, nous devons rapporter le temps de rendu après que les changements de DOM s'arrêtent, ce qui se produit généralement après le déclenchement de l'événement de chargement. Par conséquent, nous pouvons rapporter à ce moment-là.

Pour le deuxième point, nous pouvons rapporter après le déclenchement de l'événement LCP. Que les éléments DOM soient chargés de manière synchrone ou asynchrone, ils doivent être peints, donc nous pouvons surveiller l'événement LCP et n'autoriser le rapport qu'après son déclenchement.

En combinant ces deux approches, nous obtenons le code suivant :

```javascript
let isOnLoaded = false
executeAfterLoad(() => {
    isOnLoaded = true
})

let timer
let observer
function checkDOMChange() {
    clearTimeout(timer)
    timer = setTimeout(() => {
        // Calculer le temps de rendu de la première page après le chargement et le déclenchement des événements LCP et l'arrêt des changements de l'arborescence DOM
        if (isOnLoaded && isLCPDone()) {
            observer && observer.disconnect()
            lazyReportCache({
                type: 'performance',
                subType: 'first-screen-paint',
                startTime: getRenderTime(),
                pageURL: getPageURL(),
            })

            entries = null
        } else {
            checkDOMChange()
        }
    }, 500)
}
```

La fonction `checkDOMChange()` est appelée chaque fois que l'événement MutationObserver est déclenché et doit être débouncée.

### **Temps de requête API**

Pour surveiller le temps de requête API, nous devons intercepter les requêtes XMLHttpRequest et fetch.

**Surveillance de XMLHttpRequest**

```javascript
originalProto.open = function newOpen(...args) {
    this.url = args[1]
    this.method = args[0]
    originalOpen.apply(this, args)
}

originalProto.send = function newSend(...args) {
    this.startTime = Date.now()

    const onLoadend = () => {
        this.endTime = Date.now()
        this.duration = this.endTime - this.startTime

        const { status, duration, startTime, endTime, url, method } = this
        const reportData = {
            status,
            duration,
            startTime,
            endTime,
            url,
            method: (method || 'GET').toUpperCase(),
            success: status >= 200 && status < 300,
            subType: 'xhr',
            type: 'performance',
        }

        lazyReportCache(reportData)

        this.removeEventListener('loadend', onLoadend, true)
    }

    this.addEventListener('loadend', onLoadend, true)
    originalSend.apply(this, args)
}
```

Pour déterminer si une requête XML est réussie, nous pouvons vérifier si son code de statut est compris entre 200 et 299. Si c'est le cas, la requête a réussi ; sinon, elle a échoué.

**Surveillance de fetch**

```javascript
const originalFetch = window.fetch

function overwriteFetch() {
    window.fetch = function newFetch(url, config) {
        const startTime = Date.now()
        const reportData = {
            startTime,
            url,
            method: (config?.method || 'GET').toUpperCase(),
            subType: 'fetch',
            type: 'performance',
        }

        return originalFetch(url, config)
        .then(res => {
            reportData.endTime = Date.now()
            reportData.duration = reportData.endTime - reportData.startTime

            const data = res.clone()
            reportData.status = data.status
            reportData.success = data.ok

            lazyReportCache(reportData)

            return res
        })
        .catch(err => {
            reportData.endTime = Date.now()
            reportData.duration = reportData.endTime - reportData.startTime
            reportData.status = 0
            reportData.success = false

            lazyReportCache(reportData)

            throw err
        })
    }
}
```

Pour les requêtes fetch, nous pouvons déterminer le succès en vérifiant le champ `ok` dans les données de réponse. Si c'est `true`, la requête a réussi ; sinon, elle a échoué.

**Note** : Le temps de requête API que nous surveillons peut différer de ce qui est montré dans Chrome DevTools. Cela est dû au fait que Chrome DevTools montre le temps pour l'ensemble du processus de requête HTTP et d'interface. Mais XHR et fetch sont des requêtes asynchrones – après que la requête d'interface réussit, la fonction de rappel doit être appelée. Lorsque l'événement est déclenché, la fonction de rappel est placée dans la file d'attente des messages, puis le navigateur la traite. Il y a aussi une période d'attente entre les deux.

### **Temps de chargement des ressources et taux de succès du cache**

Nous pouvons surveiller les événements `resource` et `navigation` via `PerformanceObserver`. Si le navigateur ne supporte pas `PerformanceObserver`, nous pouvons utiliser `performance.getEntriesByType(entryType)`.

Lorsque l'événement `resource` est déclenché, nous pouvons obtenir la liste des ressources correspondantes. Chaque objet de ressource contient les champs suivants :

[![Champs de l'objet de ressource dans l'interface PerformanceResourceTiming](https://camo.githubusercontent.com/cf1c72dd2f2e45626e1f601a11b5c1a9a829125d30bc291f4f2bedc8a7d2391c/68747470733a2f2f70392d6a75656a696e2e62797465696d672e636f6d2f746f732d636e2d692d6b3375316662706663702f30653663623330616539613434343762626534336266636666366336633461317e74706c762d6b3375316662706663702d77617465726d61726b2e696d6167653f align="left")](https://camo.githubusercontent.com/cf1c72dd2f2e45626e1f601a11b5c1a9a829125d30bc291f4f2bedc8a7d2391c/68747470733a2f2f70392d6a75656a696e2e62797465696d672e636f6d2f746f732d636e2d692d6b3375316662706663702f30653663623330616539613434343762626534336266636666366336633461317e74706c762d6b3375316662706663702d77617465726d61726b2e696d6167653f)

À partir de ces champs, nous pouvons extraire des informations utiles :

```javascript
{
    name: entry.name, // Nom de la ressource
    subType: entryType,
    type: 'performance',
    sourceType: entry.initiatorType, // Type de ressource
    duration: entry.duration, // Durée de chargement de la ressource
    dns: entry.domainLookupEnd - entry.domainLookupStart, // Durée DNS
    tcp: entry.connectEnd - entry.connectStart, // Durée de connexion TCP
    redirect: entry.redirectEnd - entry.redirectStart, // Durée de redirection
    ttfb: entry.responseStart, // Temps jusqu'au premier octet
    protocol: entry.nextHopProtocol, // Protocole de requête
    responseBodySize: entry.encodedBodySize, // Taille du corps de la réponse
    responseHeaderSize: entry.transferSize - entry.encodedBodySize, // Taille de l'en-tête de la réponse
    resourceSize: entry.decodedBodySize, // Taille de la ressource après décompression
    isCache: isCache(entry), // Si le cache a été atteint
    startTime: performance.now(),
}
```

#### Déterminer si la ressource a atteint le cache

Parmi ces objets de ressource, il y a un champ `transferSize` qui représente la taille de la ressource en cours de récupération, y compris les champs d'en-tête de réponse et la taille des données de réponse. Si cette valeur est 0, cela signifie que la ressource a été lue directement depuis le cache (cache forcé). Si cette valeur n'est pas 0 mais que le champ `encodedBodySize` est 0, cela signifie qu'il a utilisé le cache négocié (`encodedBodySize` représente la taille du corps des données de réponse).

```javascript
function isCache(entry) {
    // Lire directement depuis le cache ou 304
    return entry.transferSize === 0 || (entry.transferSize !== 0 && entry.encodedBodySize === 0)
}
```

Si cela ne répond pas aux conditions ci-dessus, cela signifie que le cache n'a pas été atteint. Ensuite, nous pouvons calculer le taux de succès du cache en divisant `toutes les données mises en cache/données totales`.

### **Cache de retour/avant du navigateur (BFC)**

BFC est un cache mémoire qui sauvegarde la page entière en mémoire. Lorsque les utilisateurs naviguent en arrière, ils peuvent voir la page entière immédiatement sans rafraîchissement. Selon l'article [bfcache](https://web.dev/bfcache/), Firefox et Safari ont toujours supporté BFC, tandis que Chrome ne le supporte que dans les navigateurs mobiles de haute version. Mais lorsque je l'ai testé, seul Safari le supportait – ma version de Firefox était peut-être différente.

Néanmoins, BFC a aussi des inconvénients. Lorsque les utilisateurs naviguent en arrière et restaurent la page à partir de BFC, le code original de la page ne s'exécutera pas à nouveau. Pour cette raison, les navigateurs fournissent un événement `pageshow` où nous pouvons placer le code qui doit être exécuté à nouveau.

```javascript
window.addEventListener('pageshow', function(event) {
  // Si cette propriété est vraie, cela signifie que la page a été restaurée à partir de BFC
  if (event.persisted) {
    console.log('Cette page a été restaurée à partir du bfcache.');
  } else {
    console.log('Cette page a été chargée normalement.');
  }
});
```

Pour les pages restaurées à partir de BFC, nous devons également collecter leurs métriques FP, FCP, LCP, et autres.

```javascript
onBFCacheRestore(event => {
    requestAnimationFrame(() => {
        ['first-paint', 'first-contentful-paint'].forEach(type => {
            lazyReportCache({
                startTime: performance.now() - event.timeStamp,
                name: type,
                subType: type,
                type: 'performance',
                pageURL: getPageURL(),
                bfc: true,
            })
        })
    })
})
```

Le code ci-dessus est facile à comprendre. Après le déclenchement de l'événement `pageshow`, nous soustrayons l'horodatage de l'événement de l'heure actuelle – cette différence de temps est le temps de rendu des métriques de performance.

**Note** : Pour les pages restaurées à partir de BFC, ces métriques de performance ont généralement des valeurs très petites, autour de 10 ms. Cela signifie que nous devons ajouter un champ d'identification `bfc: true` afin de pouvoir les ignorer lors de la réalisation de statistiques de performance.

### **FPS**

Nous pouvons calculer le FPS actuel de la page en utilisant `requestAnimationFrame()`.

```javascript
const next = window.requestAnimationFrame 
    ? requestAnimationFrame : (callback) => { setTimeout(callback, 1000 / 60) }

const frames = []

export default function fps() {
    let frame = 0
    let lastSecond = Date.now()

    function calculateFPS() {
        frame++
        const now = Date.now()
        if (lastSecond + 1000 <= now) {
            // Puisque now - lastSecond est en millisecondes, frame doit être multiplié par 1000
            const fps = Math.round((frame * 1000) / (now - lastSecond))
            frames.push(fps)
                
            frame = 0
            lastSecond = now
        }
    
        // Éviter de rapporter trop fréquemment, mettre en cache une certaine quantité avant de rapporter
        if (frames.length >= 60) {
            report(deepCopy({
                frames,
                type: 'performace',
                subType: 'fps',
            }))
    
            frames.length = 0
        }

        next(calculateFPS)
    }

    calculateFPS()
}
```

La logique du code est la suivante :

D'abord enregistrer un temps initial, puis chaque fois que `requestAnimationFrame()` est déclenché, incrémenter le compteur de frames de 1. Après qu'une seconde se soit écoulée, nous pouvons obtenir le taux de frames actuel en divisant `nombre de frames/temps écoulé`.

Lorsque trois valeurs FPS consécutives inférieures à 20 apparaissent, nous pouvons déterminer que la page est devenue non réactive. Cette technique est basée sur l'observation que les animations fluides nécessitent au moins 20 FPS pour paraître fluides aux utilisateurs.

```javascript
export function isBlocking(fpsList, below = 20, last = 3) {
    let count = 0
    for (let i = 0; i < fpsList.length; i++) {
        if (fpsList[i] && fpsList[i] < below) {
            count++
        } else {
            count = 0
        }

        if (count >= last) {
            return true
        }
    }

    return false
}
```

### **Temps de rendu des changements de routeur Vue**

Nous savons déjà comment calculer le temps de rendu de la première page, mais comment calculer le temps de rendu de la page causé par les changements de route dans les applications SPA ? Cet article utilise Vue comme exemple pour expliquer mon approche.

```javascript
export default function onVueRouter(Vue, router) {
    let isFirst = true
    let startTime
    router.beforeEach((to, from, next) => {
        // Le chargement de la première page a déjà d'autres métriques de temps de rendu disponibles
        if (isFirst) {
            isFirst = false
            return next()
        }

        // Ajouter un nouveau champ au routeur pour indiquer s'il faut calculer le temps de rendu
        // Seulement nécessaire pour les changements de route
        router.needCalculateRenderTime = true
        startTime = performance.now()

        next()
    })

    let timer
    Vue.mixin({
        mounted() {
            if (!router.needCalculateRenderTime) return

            this.$nextTick(() => {
                // Code qui ne s'exécute qu'après que toute la vue a été rendue
                const now = performance.now()
                clearTimeout(timer)

                timer = setTimeout(() => {
                    router.needCalculateRenderTime = false
                    lazyReportCache({
                        type: 'performance',
                        subType: 'vue-router-change-paint',
                        duration: now - startTime,
                        startTime: now,
                        pageURL: getPageURL(),
                    })
                }, 1000)
            })
        },
    })
}
```

La logique du code est la suivante :

1. Surveiller les hooks de route – lorsque des changements de route se produisent, le hook `router.beforeEach()` est déclenché. Dans la fonction de rappel de ce hook, enregistrer l'heure actuelle comme temps de début de rendu.

2. Utiliser `Vue.mixin()` pour injecter une fonction dans tous les hooks `mounted()` des composants. Chaque fonction exécute une fonction débouncée.

3. Lorsque le `mounted()` du dernier composant est déclenché, cela signifie que tous les composants sous cette route ont été montés. Nous pouvons obtenir le temps de rendu dans la fonction de rappel `this.$nextTick()`.

De plus, nous devons considérer un autre cas. Lorsque la route ne change pas, il peut aussi y avoir des changements de composants, auquel cas nous ne devons pas calculer le temps de rendu dans les hooks `mounted()` de ces composants. Par conséquent, nous devons ajouter un champ `needCalculateRenderTime` – le définir à vrai lors des changements de route pour indiquer que le temps de rendu peut être calculé.

## **Collecte des données d'erreur**

La surveillance des erreurs est un aspect crucial de la surveillance front-end qui aide à identifier les problèmes rencontrés par les utilisateurs lors de l'interaction avec votre application. En suivant et en analysant ces erreurs, vous pouvez corriger proactivement les bugs avant qu'ils n'affectent plus d'utilisateurs, améliorant ainsi à la fois l'expérience utilisateur et la fiabilité de l'application.

Dans cette section, nous explorerons comment capturer divers types d'erreurs, y compris les échecs de chargement des ressources, les erreurs d'exécution JavaScript, les promesses non gérées et les erreurs spécifiques aux frameworks.

### **Erreurs de chargement des ressources**

Les erreurs de chargement des ressources se produisent lorsque le navigateur échoue à charger des ressources externes comme des images, des feuilles de style, des scripts et des polices. Ces erreurs peuvent avoir un impact significatif sur l'expérience utilisateur en provoquant des contenus manquants, des mises en page cassées ou même en empêchant le fonctionnement des fonctionnalités principales.

L'utilisation de `addEventListener()` pour surveiller l'événement d'erreur peut capturer les erreurs de chargement des ressources.

```javascript
// Capturer les erreurs de chargement des ressources js css img...
window.addEventListener('error', e => {
    const target = e.target
    if (!target) return

    if (target.src || target.href) {
        const url = target.src || target.href
        lazyReportCache({
            url,
            type: 'error',
            subType: 'resource',
            startTime: e.timeStamp,
            html: target.outerHTML,
            resourceType: target.tagName,
            paths: e.path.map(item => item.tagName).filter(Boolean),
            pageURL: getPageURL(),
        })
    }
}, true)
```

Ce code écoute l'événement global `error` avec l'option de capture définie sur true, ce qui lui permet d'attraper les erreurs des éléments de ressource comme `<img>`, `<link>` et `<script>`. Lorsqu'une ressource échoue à se charger, il collecte des informations importantes incluant :

* L'URL de la ressource échouée

* Le type d'élément (img, link, script)

* Le HTML de l'élément qui a échoué

* Le chemin DOM vers l'élément

* L'URL de la page où l'erreur s'est produite

Avec ces données, vous pouvez identifier quelles ressources échouent le plus fréquemment, prioriser les corrections et mettre en œuvre des stratégies de repli pour les ressources critiques.

### **Erreurs JavaScript**

Les erreurs JavaScript se produisent pendant l'exécution des scripts et peuvent empêcher les fonctionnalités de fonctionner correctement. Cela inclut les erreurs de syntaxe, les erreurs de référence, les erreurs de type et d'autres exceptions d'exécution.

L'utilisation de `window.onerror` peut surveiller les erreurs JavaScript.

```javascript
// Surveiller les erreurs JavaScript
window.onerror = (msg, url, line, column, error) => {
    lazyReportCache({
        msg,
        line,
        column,
        error: error.stack,
        subType: 'js',
        pageURL: url,
        type: 'error',
        startTime: performance.now(),
    })
}
```

Ce gestionnaire capture des informations détaillées sur les erreurs JavaScript :

* Le message d'erreur

* L'URL du fichier où l'erreur s'est produite

* Le numéro de ligne et de colonne de l'erreur

* La trace de pile complète de l'erreur

Ces informations sont inestimables pour le débogage et la correction des problèmes, en particulier dans les environnements de production où le débogage direct n'est pas possible. En analysant ces erreurs, vous pouvez identifier des motifs et prioriser les corrections pour les problèmes les plus courants ou les plus impactants.

### **Erreurs de promesse**

Les applications JavaScript modernes utilisent largement les promesses pour les opérations asynchrones. Lorsqu'un rejet de promesse n'est pas géré avec `.catch()` ou un deuxième argument à `.then()`, cela entraîne un rejet non géré qui peut causer des échecs silencieux.

L'utilisation de `addEventListener()` pour surveiller l'événement unhandledrejection peut capturer les erreurs de promesse non gérées.

```javascript
// Surveiller les erreurs de promesse - inconvénient est de ne pas pouvoir obtenir les données de colonne
window.addEventListener('unhandledrejection', e => {
    lazyReportCache({
        reason: e.reason?.stack,
        subType: 'promise',
        type: 'error',
        startTime: e.timeStamp,
        pageURL: getPageURL(),
    })
})
```

Ce code capture les rejets de promesse non gérés et rapporte :

* La raison du rejet (généralement un objet d'erreur avec une trace de pile)

* L'horodatage auquel le rejet s'est produit

* L'URL de la page où le rejet s'est produit

Le suivi des rejets de promesse non gérés est particulièrement important pour les opérations asynchrones comme les appels d'API, où les erreurs pourraient autrement passer inaperçues. En surveillant ces rejets, vous pouvez vous assurer que toutes les erreurs asynchrones sont correctement gérées et résolues.

### **Sourcemap**

Généralement, le code de l'environnement de production est minifié, et les fichiers sourcemap ne sont pas téléchargés en production. Par conséquent, les messages d'erreur dans le code de l'environnement de production sont difficiles à lire. Pour cette raison, nous pouvons utiliser [source-map](https://github.com/mozilla/source-map) pour restaurer ces messages d'erreur de code minifié.

Lorsque des erreurs de code se produisent, nous pouvons obtenir le nom de fichier, le numéro de ligne et le numéro de colonne correspondants :

```javascript
{
    line: 1,
    column: 17,
    file: 'https:/www.xxx.com/bundlejs',
}
```

Ensuite, appelez le code suivant pour restaurer :

```javascript
async function parse(error) {
    const mapObj = JSON.parse(getMapFileContent(error.url))
    const consumer = await new sourceMap.SourceMapConsumer(mapObj)
    // Supprimer ./ de webpack://source-map-demo/./src/index.js file
    const sources = mapObj.sources.map(item => format(item))
    // Obtenir le numéro de ligne et de colonne d'origine et le fichier source en fonction des informations d'erreur minifiées
    const originalInfo = consumer.originalPositionFor({ line: error.line, column: error.column })
    // sourcesContent contient le code source original de chaque fichier avant la minification, trouver le code source correspondant par nom de fichier
    const originalFileContent = mapObj.sourcesContent[sources.indexOf(originalInfo.source)]
    return {
        file: originalInfo.source,
        content: originalFileContent,
        line: originalInfo.line,
        column: originalInfo.column,
        msg: error.msg,
        error: error.error
    }
}

function format(item) {
    return item.replace(/(\.\/)*/g, '')
}

function getMapFileContent(url) {
    return fs.readFileSync(path.resolve(__dirname, `./maps/${url.split('/').pop()}.map`), 'utf-8')
}
```

À chaque fois que le projet est construit, si sourcemap est activé, chaque fichier JS aura un fichier map correspondant.

```javascript
bundle.js
bundle.js.map
```

À ce stade, le fichier JS est placé sur le serveur statique pour l'accès des utilisateurs, tandis que le fichier map est stocké sur le serveur pour la restauration des messages d'erreur. La bibliothèque `source-map` peut restaurer les messages d'erreur du code minifié à leur état d'origine. Par exemple, si l'emplacement de l'erreur du code minifié est `ligne 1, colonne 47`, l'emplacement restauré pourrait être `ligne 4, colonne 10`. En plus des informations de localisation, nous pouvons également obtenir le code source original.

[![Exemple de restauration d'erreur de sourcemap montrant le code minifié vs le code original](https://camo.githubusercontent.com/be3d758960a8e8e494066820ef5708d8d06bda3df1a380bab37e007a91d16003/68747470733a2f2f70332d6a75656a696e2e62797465696d672e636f6d2f746f732d636e2d692d6b3375316662706663702f62316336623565656262376234656635396434646436616436313334383465627e74706c762d6b3375316662706663702d77617465726d61726b2e696d6167653f align="left")](https://camo.githubusercontent.com/be3d758960a8e8e494066820ef5708d8d06bda3df1a380bab37e007a91d16003/68747470733a2f2f70332d6a75656a696e2e62797465696d672e636f6d2f746f732d636e2d692d6b3375316662706663702f62316336623565656262376234656635396434646436616436313334383465627e74706c762d6b3375316662706663702d77617465726d61726b2e696d6167653f)

L'image ci-dessus montre un exemple de restauration d'erreur de code. Comme cette partie n'appartient pas à la portée du SDK, j'ai créé un autre [dépôt](https://github.com/woai3c/source-map-demo) pour gérer cela. N'hésitez pas à le consulter si vous êtes intéressé.

### **Erreurs Vue**

L'utilisation de `window.onerror` ne peut pas capturer les erreurs Vue – nous devons utiliser l'API fournie par Vue pour la surveillance.

```javascript
Vue.config.errorHandler = (err, vm, info) => {
    // Imprimer les informations d'erreur dans la console
    console.error(err)

    lazyReportCache({
        info,
        error: err.stack,
        subType: 'vue',
        type: 'error',
        startTime: performance.now(),
        pageURL: getPageURL(),
    })
}
```

## **Collecte des données de comportement**

Comprendre comment les utilisateurs interagissent avec votre application est crucial pour optimiser l'expérience utilisateur, améliorer l'engagement et atteindre les objectifs commerciaux. La surveillance du comportement suit les actions des utilisateurs, les schémas de navigation et les métriques d'engagement pour fournir des informations sur la manière dont votre application est réellement utilisée.

Dans cette section, nous explorerons comment collecter des métriques comportementales clés qui peuvent vous aider à prendre des décisions basées sur les données pour améliorer votre application.

### **PV et UV**

PV (Page View) est le nombre de vues de page, tandis que UV (Unique Visitor) est le nombre d'utilisateurs uniques visitant. PV compte chaque visite de page, tandis que UV ne compte qu'une fois par utilisateur par jour.

**Pourquoi c'est important** : Les métriques PV et UV vous aident à comprendre les schémas de trafic de votre application. Un ratio PV/UV élevé indique que les utilisateurs consultent plusieurs pages, suggérant un bon engagement. Le suivi de ces métriques au fil du temps vous aide à identifier les tendances de croissance, les schémas saisonniers et l'impact des campagnes marketing ou des mises à jour de fonctionnalités.

Pour le front-end, nous devons simplement signaler PV chaque fois qu'une page est entrée. Les statistiques UV sont gérées côté serveur, analysant principalement les données signalées pour calculer UV.

```javascript
export default function pv() {
    lazyReportCache({
        type: 'behavior',
        subType: 'pv',
        startTime: performance.now(),
        pageURL: getPageURL(),
        referrer: document.referrer,
        uuid: getUUID(),
    })
}
```

Vous pouvez utiliser ces données pour :

* Suivre les pages les plus populaires

* Identifier les pages sous-performantes qui nécessitent des améliorations

* Analyser le flux des utilisateurs à travers votre application

* Mesurer l'efficacité des nouvelles fonctionnalités ou du contenu

### **Durée de la visite de la page**

Pour obtenir la durée de la visite, il suffit d'enregistrer un temps initial lorsque les utilisateurs entrent sur la page, puis de soustraire le temps initial de l'heure actuelle lorsque les utilisateurs quittent la page. Cette logique de calcul peut être placée dans l'événement `beforeunload`.

**Pourquoi c'est important** : La durée de la visite de la page indique à quel point votre contenu est engageant. Des durées plus longues suggèrent généralement que les utilisateurs trouvent le contenu précieux, tandis que des durées très courtes peuvent indiquer de la confusion, un contenu non pertinent ou des problèmes d'utilisabilité. Cette métrique vous aide à identifier les pages qui captent efficacement l'attention des utilisateurs et celles qui nécessitent des améliorations.

```javascript
export default function pageAccessDuration() {
    onBeforeunload(() => {
        report({
            type: 'behavior',
            subType: 'page-access-duration',
            startTime: performance.now(),
            pageURL: getPageURL(),
            uuid: getUUID(),
        }, true)
    })
}
```

Avec les données de durée de visite de la page, vous pouvez :

* Identifier le contenu engageant par rapport au contenu problématique

* Établir des références pour les performances du contenu

* Détecter les problèmes potentiels d'utilisabilité (durées extrêmement courtes)

* Mesurer l'efficacité des mises à jour de contenu ou des refontes

### **Profondeur d'accès à la page**

Enregistrer la profondeur d'accès à la page est très utile. Par exemple, pour différentes pages d'activité a et b, si la page a a une profondeur d'accès moyenne de 50 % et la page b de 80 %, cela indique que la page b est plus populaire auprès des utilisateurs. Sur cette base, nous pouvons apporter des améliorations ciblées à la page a.

**Pourquoi c'est important** : La profondeur d'accès mesure jusqu'où les utilisateurs font défiler une page, révélant s'ils consultent tout votre contenu ou l'abandonnent en cours de route. Cette métrique aide à identifier les schémas d'engagement du contenu et les problèmes potentiels avec la structure du contenu ou la longueur de la page.

De plus, nous pouvons utiliser la profondeur d'accès et la durée de visite pour identifier la fraude aux commandes de commerce électronique. Par exemple, si quelqu'un entre sur la page et fait immédiatement défiler jusqu'en bas, puis attend un moment avant d'acheter, tandis qu'une autre personne fait lentement défiler la page avant d'acheter. Même s'ils ont la même durée de visite, la première personne est plus susceptible de commettre une fraude.

Le processus de calcul de la profondeur d'accès à la page est légèrement plus complexe :

1. Lorsque les utilisateurs entrent sur la page, enregistrer l'heure actuelle, la valeur scrollTop, la hauteur de la fenêtre et la hauteur totale de la page.

2. Lorsque les utilisateurs font défiler la page, l'événement `scroll` est déclenché. Dans la fonction de rappel, utiliser les données du point 1 pour calculer la profondeur d'accès à la page et la durée de visite.

3. Lorsque les utilisateurs s'arrêtent de faire défiler à un certain point pour continuer à consulter la page, enregistrer l'heure actuelle, la valeur scrollTop, la hauteur de la fenêtre et la hauteur totale de la page.

4. Répéter le point 2...

Voici le code spécifique :

```javascript
let timer
let startTime = 0
let hasReport = false
let pageHeight = 0
let scrollTop = 0
let viewportHeight = 0

export default function pageAccessHeight() {
    window.addEventListener('scroll', onScroll)

    onBeforeunload(() => {
        const now = performance.now()
        report({
            startTime: now,
            duration: now - startTime,
            type: 'behavior',
            subType: 'page-access-height',
            pageURL: getPageURL(),
            value: toPercent((scrollTop + viewportHeight) / pageHeight),
            uuid: getUUID(),
        }, true)
    })

    // Initialiser et enregistrer la hauteur d'accès actuelle et le temps après le chargement de la page
    executeAfterLoad(() => {
        startTime = performance.now()
        pageHeight = document.documentElement.scrollHeight || document.body.scrollHeight
        scrollTop = document.documentElement.scrollTop || document.body.scrollTop
        viewportHeight = window.innerHeight
    })
}

function onScroll() {
    clearTimeout(timer)
    const now = performance.now()
    
    if (!hasReport) {
        hasReport = true
        lazyReportCache({
            startTime: now,
            duration: now - startTime,
            type: 'behavior',
            subType: 'page-access-height',
            pageURL: getPageURL(),
            value: toPercent((scrollTop + viewportHeight) / pageHeight),
            uuid: getUUID(),
        })
    }

    timer = setTimeout(() => {
        hasReport = false
        startTime = now
        pageHeight = document.documentElement.scrollHeight || document.body.scrollHeight
        scrollTop = document.documentElement.scrollTop || document.body.scrollTop
        viewportHeight = window.innerHeight        
    }, 500)
}

function toPercent(val) {
    if (val >= 1) return '100%'
    return (val * 100).toFixed(2) + '%'
}
```

Avec les données de profondeur d'accès à la page, vous pouvez :

* Identifier où les utilisateurs perdent de l'intérêt pour votre contenu

* Optimiser le placement du contenu (placer les éléments importants là où les utilisateurs regardent réellement)

* Améliorer la structure du contenu long avec une meilleure hiérarchie

* Détecter les schémas de comportement inhabituels des utilisateurs qui pourraient indiquer une fraude ou des bots

### **Clics des utilisateurs**

En utilisant `addEventListener()` pour surveiller les événements `mousedown` et `touchstart`, nous pouvons collecter des informations sur la taille de chaque zone de clic, la position spécifique des coordonnées de clic dans la page, le contenu de l'élément cliqué et d'autres informations.

**Pourquoi c'est important** : Le suivi des clics révèle quels éléments les utilisateurs interagissent le plus fréquemment, vous aidant à comprendre les intérêts des utilisateurs et à optimiser le placement des éléments de l'interface utilisateur. Il aide également à identifier les problèmes d'utilisabilité où les utilisateurs pourraient cliquer sur des éléments non interactifs en attendant une réponse.

```javascript
export default function onClick() {
    ['mousedown', 'touchstart'].forEach(eventType => {
        let timer
        window.addEventListener(eventType, event => {
            clearTimeout(timer)
            timer = setTimeout(() => {
                const target = event.target
                const { top, left } = target.getBoundingClientRect()
                
                lazyReportCache({
                    top,
                    left,
                    eventType,
                    pageHeight: document.documentElement.scrollHeight || document.body.scrollHeight,
                    scrollTop: document.documentElement.scrollTop || document.body.scrollTop,
                    type: 'behavior',
                    subType: 'click',
                    target: target.tagName,
                    paths: event.path?.map(item => item.tagName).filter(Boolean),
                    startTime: event.timeStamp,
                    pageURL: getPageURL(),
                    outerHTML: target.outerHTML,
                    innerHTML: target.innerHTML,
                    width: target.offsetWidth,
                    height: target.offsetHeight,
                    viewport: {
                        width: window.innerWidth,
                        height: window.innerHeight,
                    },
                    uuid: getUUID(),
                })
            }, 500)
        })
    })
}
```

Avec ces données de clics, vous pouvez :

* Créer des cartes thermiques montrant où les utilisateurs cliquent le plus fréquemment

* Identifier les éléments non fonctionnels que les utilisateurs tentent d'interagir

* Optimiser le placement et la taille des boutons pour une meilleure conversion

* Détecter les clics de rage (plusieurs clics rapides dans la même zone) indiquant la frustration des utilisateurs

### **Navigation de la page**

En utilisant `addEventListener()` pour surveiller les événements de navigation de page `popstate` et `hashchange`, vous pouvez suivre comment les utilisateurs naviguent à travers votre application.

**Pourquoi c'est important** : Le suivi de la navigation vous aide à comprendre les schémas de flux des utilisateurs - comment les utilisateurs se déplacent entre les pages, quels chemins de navigation sont les plus courants et où les utilisateurs pourraient se perdre ou être piégés dans des boucles de navigation. Ces données sont cruciales pour optimiser la structure du site et améliorer les flux de parcours utilisateur.

```javascript
export default function pageChange() {
    let from = ''
    window.addEventListener('popstate', () => {
        const to = getPageURL()

        lazyReportCache({
            from,
            to,
            type: 'behavior',
            subType: 'popstate',
            startTime: performance.now(),
            uuid: getUUID(),
        })

        from = to
    }, true)

    let oldURL = ''
    window.addEventListener('hashchange', event => {
        const newURL = event.newURL

        lazyReportCache({
            from: oldURL,
            to: newURL,
            type: 'behavior',
            subType: 'hashchange',
            startTime: performance.now(),
            uuid: getUUID(),
        })

        oldURL = newURL
    }, true)
}
```

Avec les données de navigation, vous pouvez :

* Identifier les chemins courants des utilisateurs à travers votre application

* Détecter les impasses ou les boucles de navigation où les utilisateurs se retrouvent coincés

* Optimiser les menus de navigation en fonction des schémas d'utilisation réels

* Améliorer l'architecture de l'information pour mieux correspondre au comportement des utilisateurs

### **Changements de routeur Vue**

Pour les applications construites avec Vue, vous pouvez utiliser les hooks du routeur pour surveiller la navigation entre les routes, fournissant des informations similaires au suivi général de la navigation de page mais spécifiques au système de routage de Vue.

**Pourquoi c'est important** : Dans les applications à page unique, les événements de navigation traditionnels ne capturent pas tous les changements de route. La surveillance spécifique au framework du routeur garantit que vous ne manquez pas de données de navigation importantes dans les applications web modernes.

```javascript
export default function onVueRouter(router) {
    router.beforeEach((to, from, next) => {
        // Ne pas compter le chargement de la première page
        if (!from.name) {
            return next()
        }

        const data = {
            params: to.params,
            query: to.query,
        }

        lazyReportCache({
            data,
            name: to.name || to.path,
            type: 'behavior',
            subType: ['vue-router-change', 'pv'],
            startTime: performance.now(),
            from: from.fullPath,
            to: to.fullPath,
            uuid: getUUID(),
        })

        next()
    })
}
```

Ces données vous aident à :

* Suivre les routes les plus fréquemment consultées dans votre application Vue

* Comprendre les schémas de navigation spécifiques à la structure de votre application

* Identifier les opportunités d'optimisation potentielles dans votre configuration de routage

* Mesurer l'impact des améliorations UX sur le comportement de navigation

## **Rapport de données**

Une fois que vous avez collecté les données de performance, d'erreurs et de comportement, vous avez besoin d'un système fiable pour transmettre ces informations à votre backend pour traitement et analyse. Le rapport de données est le pont critique entre la collecte de données côté client et l'analyse côté serveur.

Un rapport de données efficace doit équilibrer plusieurs préoccupations :

1. **Fiabilité** – Assurer que les données sont transmises avec succès, en particulier les erreurs critiques

2. **Performance** – Minimiser l'impact sur l'expérience utilisateur et les performances de l'application

3. **Temporisation** – Décider quand envoyer les données pour éviter les interférences avec les interactions utilisateur

4. **Bande passante** – Gérer la quantité de données transmises pour réduire l'utilisation du réseau

Explorons les différentes méthodes et stratégies pour mettre en œuvre un rapport de données efficace.

### **Méthodes de rapport**

Les données peuvent être rapportées en utilisant les méthodes suivantes :

* [sendBeacon](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/sendBeacon)

* [XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)

* image

Mon SDK simple utilise une combinaison des première et deuxième méthodes pour le rapport. L'utilisation de sendBeacon pour le rapport présente des avantages très évidents.

**Note** : L'utilisation de la méthode `sendBeacon()` enverra les données au serveur de manière asynchrone lorsque l'agent utilisateur en a l'occasion, sans retarder le déchargement de la page ou affecter les performances de la navigation suivante. Cela résout tous les problèmes de soumission des données d'analyse : les données sont fiables, la transmission est asynchrone et cela n'affecte pas le chargement de la page suivante.

Pour les navigateurs qui ne supportent pas sendBeacon, nous pouvons utiliser XMLHttpRequest pour le rapport. Une requête HTTP se compose de deux étapes : l'envoi et la réception.

En fait, pour le rapport, nous devons simplement nous assurer que les données peuvent être envoyées – nous n'avons pas besoin de recevoir la réponse. Pour cette raison, j'ai fait une expérience où j'ai envoyé 30 Ko de données (généralement les données rapportées dépassent rarement cette taille) en utilisant XMLHttpRequest dans beforeunload, testé avec différents navigateurs, et tous ont pu envoyer avec succès. Bien sûr, cela dépend aussi des performances matérielles et des conditions réseau.

Voici un exemple d'implémentation d'une fonction de rapport qui utilise les deux méthodes :

```javascript
function report(data, isImmediate = false) {
    if (!config.reportUrl) {
        console.error('L\'URL de rapport n\'est pas définie')
        return
    }
    
    // Ajouter un horodatage et d'autres propriétés communes
    const reportData = {
        ...data,
        timestamp: Date.now(),
        userAgent: navigator.userAgent,
        userId: getUserId(),
        // Ajouter d'autres propriétés communes si nécessaire
    }
    
    // Choisir la méthode de rapport en fonction de la prise en charge du navigateur et du timing
    if (isImmediate) {
        sendData(reportData)
    } else {
        // Mettre les données en file d'attente pour un envoi par lots
        reportQueue.push(reportData)
        
        // Envoyer lorsque la file d'attente atteint le seuil
        if (reportQueue.length >= config.batchSize) {
            sendBatchData()
        }
    }
}

function sendData(data) {
    // Essayer sendBeacon en premier
    if (navigator.sendBeacon) {
        const blob = new Blob([JSON.stringify(data)], { type: 'application/json' })
        const success = navigator.sendBeacon(config.reportUrl, blob)
        
        if (success) return
    }
    
    // Revenir à XMLHttpRequest
    const xhr = new XMLHttpRequest()
    xhr.open('POST', config.reportUrl, true)
    xhr.setRequestHeader('Content-Type', 'application/json')
    xhr.send(JSON.stringify(data))
}

function sendBatchData() {
    if (reportQueue.length === 0) return
    
    const data = [...reportQueue]
    reportQueue.length = 0
    
    sendData({ type: 'batch', data })
}
```

### **Temporisation du rapport**

Il existe trois temporisations de rapport :

1. Utiliser `requestIdleCallback/setTimeout` pour un rapport différé

2. Signaler dans la fonction de rappel beforeunload

3. Mettre en cache les données signalées et signaler lorsqu'un certain montant est atteint

Il est recommandé de combiner les trois méthodes :

1. D'abord mettre en cache les données signalées, et lorsqu'un certain montant est atteint, utiliser `requestIdleCallback/setTimeout` pour un rapport différé

2. Signaler toutes les données non signalées lors de la sortie de la page

Voici comment vous pourriez implémenter cette approche combinée :

```javascript
// Cache pour stocker les rapports jusqu'à ce qu'ils soient envoyés
let reportCache = []
const MAX_CACHE_SIZE = 10
let timer = null

// Signaler les données avec requestIdleCallback lorsque le navigateur est inactif
function lazyReportCache(data) {
    reportCache.push(data)
    
    // Si le cache atteint le seuil, planifier l'envoi
    if (reportCache.length >= MAX_CACHE_SIZE) {
        // Utiliser requestIdleCallback si disponible, sinon setTimeout
        const scheduleFn = window.requestIdleCallback || setTimeout
        
        if (timer) {
            cancelScheduledReport()
        }
        
        timer = scheduleFn(() => {
            // Envoyer les données en cache en bloc
            const dataToSend = [...reportCache]
            reportCache = []
            report({
                type: 'batch',
                data: dataToSend,
            })
            timer = null
        }, { timeout: 2000 }) // Pour requestIdleCallback, timeout après 2s
    }
}

function cancelScheduledReport() {
    if (window.requestIdleCallback && timer) {
        window.cancelIdleCallback(timer)
    } else if (timer) {
        clearTimeout(timer)
    }
    timer = null
}

// Signaler toute donnée restante lorsque l'utilisateur quitte la page
function setupUnloadReporting() {
    window.addEventListener('beforeunload', () => {
        if (reportCache.length > 0) {
            // Annuler tout rapport planifié
            cancelScheduledReport()
            
            // Envoyer les données en cache restantes immédiatement
            report({
                type: 'batch',
                data: reportCache,
            }, true) // true pour l'envoi immédiat
            
            reportCache = []
        }
    })
}
```

Cette implémentation :

1. Collecte les données dans un cache jusqu'à ce qu'il atteigne un seuil

2. Utilise `requestIdleCallback` (ou `setTimeout` comme solution de repli) pour envoyer les données lorsque le navigateur est inactif

3. Assure que toute donnée restante est envoyée lorsque l'utilisateur quitte la page

4. Regroupe plusieurs rapports ensemble pour réduire les requêtes réseau

En combinant ces méthodes, vous créez un système de rapport robuste qui minimise l'impact sur les performances tout en assurant la fiabilité des données.

## **Résumé**

Dans ce guide complet, nous avons exploré comment construire un SDK de surveillance front-end complet pour collecter et rapporter des données critiques de l'application. Récapitulons ce que nous avons couvert :

1. **Surveillance des performances**

    * Nous avons mis en œuvre des méthodes pour capturer des indicateurs web clés comme FP, FCP, LCP et CLS

    * Nous avons suivi les événements de chargement de page, le temps des requêtes API et les métriques de chargement des ressources

    * Nous avons mesuré le temps de rendu de la première page et les taux de rafraîchissement pour garantir des expériences utilisateur fluides

    * Nous avons ajouté un support pour les métriques spécifiques aux SPA comme le temps de rendu des changements de routeur Vue

2. **Surveillance des erreurs**

    * Nous avons construit des systèmes pour capturer les erreurs de chargement des ressources, les exceptions JavaScript et les rejets de promesse

    * Nous avons exploré comment utiliser les sourcemaps pour rendre les erreurs de production minifiées lisibles

    * Nous avons intégré avec la gestion des erreurs spécifiques aux frameworks pour les applications Vue

3. **Suivi du comportement des utilisateurs**

    * Nous avons mis en œuvre le suivi des vues de page, de la durée de visite et de la profondeur de défilement

    * Nous avons créé des méthodes pour surveiller les clics des utilisateurs et les schémas de navigation

    * Nous avons construit un suivi personnalisé pour la navigation SPA avec Vue Router

4. **Rapport de données**

    * Nous avons développé des mécanismes de rapport robustes utilisant sendBeacon et XMLHttpRequest

    * Nous avons mis en œuvre des stratégies de temporisation de rapport intelligentes pour minimiser l'impact sur les performances

    * Nous avons créé des mécanismes de regroupement pour réduire les requêtes réseau

Construire votre propre SDK de surveillance vous donne un contrôle complet sur les données que vous collectez et la manière dont vous les traitez. Cette approche offre plusieurs avantages par rapport aux solutions tierces :

* **Confidentialité** : Vous possédez toutes les données et pouvez garantir la conformité avec les réglementations comme le RGPD

* **Performance** : Vous pouvez optimiser le SDK spécifiquement pour les besoins de votre application

* **Personnalisation** : Vous pouvez ajouter des métriques personnalisées uniques à vos exigences commerciales

* **Intégration** : Votre SDK peut facilement s'intégrer avec vos systèmes existants

Lorsque vous implémentez votre propre solution de surveillance, rappelez-vous ces bonnes pratiques :

1. **Respectez la vie privée des utilisateurs** : Ne collectez que ce dont vous avez besoin et soyez transparent à ce sujet

2. **Minimisez l'impact sur les performances** : Assurez-vous que votre surveillance ne dégrade pas l'expérience utilisateur

3. **Équilibrez les détails et le volume** : Plus de données n'est pas toujours mieux si cela submerge votre analyse

4. **Agissez en fonction des insights** : L'objectif ultime est d'améliorer votre application en fonction des données

En suivant les approches décrites dans cet article, vous serez bien équipé pour construire un système de surveillance complet qui vous aide à offrir de meilleures expériences utilisateur grâce à une prise de décision basée sur les données.

## **Références**

### **Surveillance des performances**

* [Performance API](https://developer.mozilla.org/en-US/docs/Web/API/Performance_API)

* [PerformanceResourceTiming](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming)

* [Using\_the\_Resource\_Timing\_API](https://developer.mozilla.org/en-US/docs/Web/API/Resource_Timing_API/Using_the_Resource_Timing_API)

* [PerformanceTiming](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceTiming)

* [Metrics](https://web.dev/metrics/)

* [evolving-cls](https://web.dev/evolving-cls/)

* [custom-metrics](https://web.dev/custom-metrics/)

* [web-vitals](https://github.com/GoogleChrome/web-vitals)

* [PerformanceObserver](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceObserver)

* [Element\_timing\_API](https://developer.mozilla.org/en-US/docs/Web/API/Element_timing_API)

* [PerformanceEventTiming](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceEventTiming)

* [Timing-Allow-Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Timing-Allow-Origin)

* [bfcache](https://web.dev/bfcache/)

* [MutationObserver](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver)

* [XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)

* [sendBeacon](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/sendBeacon)

### **Surveillance des erreurs**

* [noerror](https://github.com/joeyguo/noerror)

* [source-map](https://github.com/mozilla/source-map)

### **Surveillance du comportement**

* [popstate](https://developer.mozilla.org/en-US/docs/Web/API/Window/popstate_event)

* [hashchange](https://developer.mozilla.org/en-US/docs/Web/API/Window/hashchange_event)