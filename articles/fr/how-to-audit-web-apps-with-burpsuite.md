---
title: Comment utiliser Burp Suite pour auditer des applications web - Aperçu de l'outil
  de pentest et de bug bounty
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2023-01-17T14:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-audit-web-apps-with-burpsuite
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/burpsuite-article-image.png
tags:
- name: Application Security
  slug: application-security
- name: bug bounty
  slug: bug-bounty
- name: cybersecurity
  slug: cybersecurity
- name: penetration testing
  slug: penetration-testing
seo_title: Comment utiliser Burp Suite pour auditer des applications web - Aperçu
  de l'outil de pentest et de bug bounty
seo_desc: 'What is Burp Suite?

  Burp Suite is a powerful and widely-used web application testing platform. It helps
  security engineers identify potential risks in web applications.

  Burp Suite is also widely used by bug-bounty hunters. Since Burp Suite is a fully...'
---

## Qu'est-ce que Burp Suite ?

Burp Suite est une plateforme puissante et largement utilisée pour tester les applications web. Elle aide les ingénieurs en sécurité à identifier les risques potentiels dans les applications web.

Burp Suite est également largement utilisé par les chasseurs de primes de bogues. Puisque Burp Suite est une plateforme complète d'audit web, il dispose de nombreux outils pour vous aider à découvrir des bugs dans les applications web. Vous pouvez également utiliser des modules tiers pour améliorer davantage les capacités de Burp Suite.

Burp Suite est un outil essentiel pour toute équipe de test de sécurité. Dans cet article, nous allons examiner de plus près les principaux composants de Burp Suite, y compris le proxy, l'intruder et le repeater.

## **Burp Proxy**

L'un des composants clés de Burp Suite est le Burp Proxy. Cet outil vous permet d'intercepter et d'inspecter le trafic entre votre navigateur et la cible.

En interceptant ce trafic, vous pouvez comprendre exactement quelles données sont envoyées et reçues. Cela est utile pour identifier les vulnérabilités potentielles ou les mauvaises configurations dans l'application.

Le proxy est particulièrement utile pour identifier des problèmes tels que le cross-site scripting (XSS) et l'injection SQL.

Le XSS est un type de vulnérabilité de sécurité qui permet à un attaquant d'injecter du code malveillant dans une page web. L'injection SQL permet à un attaquant d'injecter du code SQL malveillant dans une application web.

En identifiant ces types de problèmes, vous pouvez prendre des mesures pour les atténuer et améliorer la sécurité de votre application.

De plus, Burp Proxy nous permet de transférer les requêtes à d'autres outils Burp avant de les envoyer à la cible. Cela nous permet d'analyser davantage le trafic et d'inspecter les requêtes et réponses individuelles. Cela peut être utile pour identifier des motifs ou des anomalies qui pourraient indiquer une vulnérabilité.

## **Burp Repeater**

Un autre composant clé de Burp Suite est le Burp Repeater. Le Repeater est un outil puissant qui vous permet de tester l'application en envoyant des requêtes personnalisées et en analysant les réponses.

L'un des principaux avantages du Repeater est sa capacité à identifier des vulnérabilités qui pourraient ne pas être visibles lors des analyses automatisées. Les analyses automatisées sont utiles pour identifier une large gamme de vulnérabilités courantes, mais elles peuvent ne pas être en mesure de détecter tous les problèmes.

Le Repeater nous donne un meilleur contrôle sur le processus de test. Il nous permet d'affiner nos tests pour identifier des vulnérabilités spécifiques. Par exemple, nous pourrons identifier une vulnérabilité en envoyant une requête avec une entrée spécifique.

En analysant la réponse, nous pouvons constater que l'application se comporte de manière inattendue. Cela indiquera la possibilité d'une vulnérabilité. Cette vulnérabilité pourrait ne pas être détectée lors d'une analyse automatisée, mais elle pourrait potentiellement être exploitée par un attaquant.

Le Repeater peut également tester la résilience de l'application à des types spécifiques d'attaques. Par exemple, vous pouvez utiliser le Repeater pour envoyer une série de requêtes afin de tester la capacité de l'application à gérer les attaques par injection SQL ou par cross-site scripting (XSS).

En comprenant le comportement de l'application dans ces scénarios, vous pouvez prendre des mesures pour améliorer sa sécurité.

## **Burp Intruder**

L'un des outils les plus puissants de Burp Suite est le Burp Intruder. Cet outil vous permet de lancer des attaques automatisées sur des applications web pour tester leur sécurité.

Avec le Burp Intruder, vous pouvez tester une large gamme de vulnérabilités. Cela inclut l'injection SQL, le cross-site scripting (XSS) et la traversée de répertoires. L'intruder est très flexible, nous permettant de personnaliser nos attaques.

Nous pouvons également utiliser l'intruder pour effectuer des audits spécifiques tels que le forçage brutal, les attaques par dictionnaire et le fuzzing. L'Intruder nous permet également de cibler des zones spécifiques de l'application en sélectionnant des paramètres personnalisés.

Étant donné les dégâts que l'Intruder peut causer s'il est utilisé sans précaution, Burp Suite a mis en place une limitation de débit dans l'édition communautaire. Cela signifie que vous ne pouvez utiliser l'Intruder que pour un certain nombre de requêtes, comme le forçage brutal d'un formulaire de connexion, dans la version gratuite de l'outil.

Si vous prévoyez d'utiliser Burp Suite pour auditer vos applications professionnelles, envisagez d'acheter une licence commerciale. Cela vous donnera accès à toutes les fonctionnalités de Burp Suite sans aucune limite de débit.

## **Autres outils Burp**

Burp Suite comprend également de nombreux outils supplémentaires. Ceux-ci incluent le spider, le scanner, le décodeur, le séquencer et le comparateur.

Ces outils servent d'utilitaires dans les audits généraux des applications web. Par exemple, le spider peut aider à découvrir et à cartographier le contenu et la structure d'une application web. Nous pouvons utiliser le scanner pour effectuer des analyses automatisées de vulnérabilités.

Le décodeur aide à décoder et à analyser les données encodées, tandis que le séquencer nous permet de tester l'aléatoire des jetons et des identifiants de session. Le comparateur compare le comportement de différentes requêtes et réponses.

En plus de ceux-ci, il existe également de nombreux modules tiers disponibles dans Burp Suite. Ces modules étendent davantage les capacités de Burp Suite pour nous aider à tester nos applications web.

## **Résumé**

En conclusion, Burp Suite est un ensemble puissant d'outils pour l'audit des applications web. Il inclut une gamme d'outils et de fonctionnalités pour tester la sécurité des applications web.

Le proxy, l'intruder et le repeater sont certains des principaux composants de Burp Suite, chacun ayant une fonction spécifique pour identifier et évaluer les risques de sécurité.

Avec l'aide de ces outils, les professionnels de la sécurité et les testeurs peuvent identifier et atténuer les risques dans les applications web. Avec des fonctionnalités complètes d'audit web, c'est également un outil essentiel pour les chasseurs de primes de bogues.

J'espère que vous avez apprécié cet article. Vous pouvez trouver plus d'informations sur mes articles et vidéos sur [mon site web](https://www.manishmshiva.com/).