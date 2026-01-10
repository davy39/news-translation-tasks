---
title: Comment suivre et analyser les Web Vitals pour améliorer le SEO
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-19T12:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-track-and-analyze-web-vitals-to-improve-seo
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/vitals.png
tags:
- name: analytics
  slug: analytics
- name: data
  slug: data
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: SEO
  slug: seo
- name: Software Engineering
  slug: software-engineering
- name: web vitals
  slug: web-vitals
seo_title: Comment suivre et analyser les Web Vitals pour améliorer le SEO
seo_desc: "By Adam Henson\nGood news - we now have a brand new set of standards by\
  \ which to judge our search engine's worthiness! ? \nIf you're like me, you may\
  \ not have been jumping for joy when you read Google's announcement of its upcoming\
  \ search algorithm cha..."
---

Par Adam Henson

Bonne nouvelle - nous avons maintenant un tout nouvel ensemble de normes pour juger de la valeur de notre moteur de recherche ! ? 

Si vous êtes comme moi, vous n'avez peut-être pas sauté de joie en lisant [l'annonce de Google concernant son prochain changement d'algorithme de recherche](https://webmasters.googleblog.com/2020/05/evaluating-page-experience.html). Mais après avoir pris le temps de respirer, je crois que c'est un changement positif. 

L'annonce met l'accent sur l'_expérience_ de la page web et son rôle dans l'avenir de l'indexation de recherche. En suivant cette nouvelle direction, nous pouvons non seulement offrir une meilleure expérience aux utilisateurs de sites web, mais aussi établir des stratégies efficaces pour améliorer le SEO.

## Qu'est-ce que les Web Vitals ?

Les métriques suivantes englobent les Web Vitals telles que définies au moment de la rédaction de cet article.

* [First Contentful Paint (FCP)](https://web.dev/fcp/) mesure le temps écoulé entre le début du chargement de la page et le moment où une partie du contenu de la page est rendue à l'écran.
* [First Input Delay (FID)](https://web.dev/fid/) mesure le temps écoulé entre le moment où un utilisateur interagit pour la première fois avec une page et le moment où le navigateur est en mesure de répondre à cette interaction.
* [Largest Contentful Paint (LCP)](https://web.dev/lcp/) rapporte le temps de rendu du plus grand élément de contenu visible dans la fenêtre d'affichage.
* [Time to First Byte (TTFB)](https://web.dev/time-to-first-byte/) est le temps nécessaire pour qu'un navigateur d'utilisateur reçoive le premier octet du contenu de la page.
* [Cumulative Layout Shift (CLS)](https://web.dev/cls/) mesure la somme totale de tous les scores de déplacement de mise en page individuels pour chaque _déplacement de mise en page inattendu_ qui se produit pendant toute la durée de vie d'une page. Pour calculer le _score de déplacement de mise en page_, le navigateur examine la taille de la fenêtre d'affichage et le mouvement des éléments instables dans la fenêtre d'affichage entre deux images rendues.

## Pourquoi les Web Vitals sont-elles importantes ?

Ces dernières années, [Lighthouse](https://developers.google.com/web/tools/lighthouse), un outil automatisé open-source pour améliorer la qualité des pages web, a été largement adopté comme norme industrielle. 

Un autre projet Google appelé [Web Vitals](https://github.com/GoogleChrome/web-vitals) a émergé, dérivant des métriques à partir de **vrais utilisateurs** d'une manière qui correspond précisément à la façon dont elles sont mesurées par Chrome et rapportées à d'autres outils Google. 

Avec cela, nous pouvons établir une perspective d'expérience de page d'un point de vue SEO, analyser et ajuster en conséquence. ?

> Les Core Web Vitals sont le sous-ensemble des Web Vitals qui s'appliquent à toutes les pages web, doivent être mesurées par tous les propriétaires de sites et seront mises en avant dans tous les outils Google. Chacune des Core Web Vitals représente une facette distincte de l'expérience utilisateur, est mesurable [sur le terrain](https://web.dev/user-centric-performance-metrics/#how-metrics-are-measured) et reflète l'expérience réelle d'un résultat critique [centré sur l'utilisateur](https://web.dev/user-centric-performance-metrics/#how-metrics-are-measured).

%[https://web.dev/vitals/]

## Web Vitals dans Google Search Console

Search Console fournit des rapports sur la manière dont les vrais utilisateurs accèdent à un site web et une variété de données sur ces utilisateurs. 

Les Core Web Vitals sont rapportées sous forme de résumé montrant le nombre total d'URL qui sont bonnes, nécessitent des améliorations ou sont simplement mauvaises. ?

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screen-Shot-2020-06-17-at-11.30.00-PM.png)
_Google Search Console Core Web Vitals_

## Envoyer les Web Vitals à Google Analytics et les visualiser dans Data Studio

Search Console fournit un résumé des résultats dans le grand schéma des choses, mais pour obtenir des rapports détaillés, nous pouvons aller plus loin. Le [projet GitHub Web Vitals documente une méthode de capture des métriques en tant qu'événements d'analyse](https://github.com/GoogleChrome/web-vitals#send-the-results-to-google-analytics) qui peuvent être visualisés sous forme de graphiques dans Google Data Studio.

Avertissement : Je n'ai pas personnellement réussi à connecter les événements Web Vitals Analytics à Data Studio, et la documentation est actuellement insuffisante. Mais je mettrai à jour cet article dès que je pourrai rassembler un exemple.

## Visualiser et analyser les Web Vitals en temps réel avec Automated Lighthouse Check

![Image](https://www.freecodecamp.org/news/content/images/2020/06/web-vitals-screenshot-2000.png)
_[Démonstration des Web Vitals avec Automated Lighthouse Check](https://www.automated-lighthouse-check.com/dashboard/demo/web-vitals)_

Google Analytics et Data Studio sont des outils puissants qui offrent de grandes perspectives. Et surtout, ils sont gratuits ! 

Automated Lighthouse Check est un site web qui surveille les sites web avec Lighthouse et offre maintenant une implémentation des Web Vitals. Vous pouvez intégrer un extrait JS sur votre site web et commencer à collecter les métriques Web Vitals en temps réel. 

Un avantage de cet outil est son processus de configuration simple et son filtrage facile. Vous pouvez [filtrer les données par URL ainsi que par navigateur, système d'exploitation et appareil](https://www.foo.software/web-vitals).

## Conclusion

Le chemin vers le succès en SEO est sinueux, mais heureusement, nous avons maintenant un ensemble de directives plus concrètes. Si votre objectif est d'atteindre un classement élevé sur le moteur de recherche de Google, il est bon d'utiliser les outils et projets recommandés par Google, y compris Lighthouse et Web Vitals.