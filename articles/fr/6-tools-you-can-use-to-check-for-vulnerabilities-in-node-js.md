---
title: 6 outils que vous pouvez utiliser pour vérifier les vulnérabilités dans Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-19T11:42:14.000Z'
originalURL: https://freecodecamp.org/news/6-tools-you-can-use-to-check-for-vulnerabilities-in-node-js
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/mahmudul-hasan-shaon-QTPJWJBQO90-unsplash.jpg
tags:
- name: node js
  slug: node-js
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: vulnerabilities
  slug: vulnerabilities
- name: Web Development
  slug: web-development
seo_title: 6 outils que vous pouvez utiliser pour vérifier les vulnérabilités dans
  Node.js
seo_desc: 'By Dillion Megida

  Vulnerabilities can exist in all products. The larger your software grows, the greater
  the potential for vulnerabilities.

  Vulnerabilities create opportunities for exploits which could ruin both the user
  experience and the product it...'
---

Par Dillion Megida

Les vulnérabilités peuvent exister dans tous les produits. Plus votre logiciel grandit, plus le potentiel de vulnérabilités est grand.

Les vulnérabilités créent des opportunités pour des exploits qui pourraient ruiner à la fois l'expérience utilisateur et le produit lui-même.

De plus, dans le monde rapide d'aujourd'hui, le taux de vulnérabilités augmente à mesure que les entreprises demandent des processus de développement (ou de mise à jour) rapides. Et les exploiteurs sont partout, cherchant à en tirer profit.

C'est pourquoi il est important de vérifier les vulnérabilités dès que possible dans vos applications. Cela peut vous aider à vous assurer que le produit final est sécurisé, et vous faire économiser beaucoup de temps à long terme.

Dans cet article, nous allons examiner six outils qui vous aideront à vérifier les vulnérabilités dans Node.js.

## Vulnérabilités dans Node.js

Les vulnérabilités de sécurité sont très courantes dans [Node.js](https://nodejs.org/en/). En tant que développeurs, nous continuons à utiliser des [outils open source](https://opensource.com/tags/javascript) parce que nous ne voulons pas réinventer la roue. Cela rend le développement plus facile et plus rapide pour nous, mais en même temps, cela introduit des vulnérabilités possibles dans nos applications.

Le meilleur que nous puissions faire pour nous-mêmes est de vérifier continuellement les packages que nous utilisons, car plus nous utilisons de dépendances, plus il y a de place pour plus de vulnérabilités.

Vérifier manuellement les dépendances peut être stressant et peut augmenter le temps de développement. Et aller en ligne pour découvrir à quel point un package est vulnérable avant de l'installer peut être chronophage, surtout pour une application avec [de nombreuses dépendances](https://en.wikipedia.org/wiki/Dependency_hell).

C'est pourquoi nous avons besoin d'outils automatisés pour nous aider dans ce processus.

## Outils pour vérifier les vulnérabilités dans Node.js

### 1. Retire.js

![Retire-js](https://www.freecodecamp.org/news/content/images/2020/06/retire-js.jpeg)

[Retire.js](http://retirejs.github.io/retire.js) aide les développeurs à détecter les versions de bibliothèques ou de modules avec des vulnérabilités connues dans les applications Node.js.

Il peut être utilisé de quatre manières :

- Un scanner en ligne de commande pour scanner une application Node.js.
- Un plugin Grunt (`grunt-retire`), utilisé pour scanner les applications compatibles avec Grunt.
- Des extensions de navigateur (Chrome et Firefox). Celles-ci scannent les sites visités pour détecter les références à des bibliothèques non sécurisées et affichent des avertissements dans la console du développeur.
- Un plugin Burp et OWASP Zap, utilisé pour les tests de pénétration.

### 2. WhiteSource Renovate

![WhiteSource Renovate](https://www.freecodecamp.org/news/content/images/2020/06/renovate.png)

WhiteSource Renovate est un outil open source multiplateforme et multilingue de WhiteSource qui effectue des mises à jour automatiques des dépendances dans les mises à jour logicielles.

Il offre des fonctionnalités telles que des demandes de tirage automatiques lorsque les dépendances doivent être mises à jour, prend en charge de nombreuses plateformes, une modification facile, et bien plus encore. Tous les journaux de modifications et les historiques de commits sont inclus dans chaque mise à jour de l'application.

Il peut être utilisé de diverses manières, telles que :

- Un outil en ligne de commande pour automatiser le processus de mise à jour des dépendances vers des dépendances invulnérables.
- Une application GitHub pour effectuer le processus d'automatisation sur les dépôts GitHub.
- Des applications GitLab pour intégrer le processus d'automatisation sur les dépôts GitLab.

WhiteSource Renovate dispose également d'une solution sur site qui étend l'outil CLI pour ajouter plus de fonctionnalités, rendant ainsi vos applications plus efficaces.

### 3. OWASP Dependency-Check

![OWASP Dependency-Check](https://www.freecodecamp.org/news/content/images/2020/06/dependency-check.jpeg)

Dependency-Check est un outil d'[analyse de composition logicielle (CPA)](https://en.everybodywiki.com/Software_Composition_Analysis) utilisé pour gérer et sécuriser les logiciels open source.

Les développeurs peuvent l'utiliser pour identifier les vulnérabilités divulguées publiquement dans Node.js, Python et Ruby.

L'outil inspecte les dépendances du projet pour recueillir des informations sur chaque dépendance. Il détermine s'il existe un identifiant [Common Platform Enumeration (CPE)](https://en.m.wikipedia.org/wiki/Common_Platform_Enumeration) pour une dépendance donnée, et si trouvé, il génère une liste d'entrées associées [Common Vulnerability and Exposure (CVE)](https://cve.mitre.org/).

Dependency-Check peut être utilisé comme un outil CLI, un plugin [Maven](https://en.m.wikipedia.org/wiki/Apache_Maven), une [tâche Ant](https://ant.apache.org/manual/Tasks/ant.html) et un [plugin Jenkins](https://en.m.wikipedia.org/wiki/Jenkins_(software)).

### 4. OSS INDEX

![OSS INDEX](https://www.freecodecamp.org/news/content/images/2020/06/oss-index.png)

L'[OSS Index](https://ossindex.sonatype.org/) permet aux développeurs de rechercher des millions de composants pour découvrir ceux qui sont vulnérables et ceux qui ne le sont pas. Cela assure aux développeurs que les composants qu'ils prévoient d'utiliser sont bien protégés.

Ils fournissent également aux développeurs divers outils et plugins pour les langages de programmation comme JavaScript.

Cela leur permet de scanner les projets pour détecter les vulnérabilités open source ainsi que d'intégrer la sécurité dans le processus de développement du projet.

### 5. Acutinex

![ACUTINEX](https://www.freecodecamp.org/news/content/images/2020/06/acutinex-1.png)

[Acunetix](https://www.acunetix.com/website-scan-acunetix/) est un scanner de sécurité pour les applications web qui permet aux développeurs d'identifier les vulnérabilités dans les applications Node.js et leur permet de corriger les vulnérabilités pour empêcher les pirates. Il est livré avec un essai de 14 jours pour tester les applications.

Les avantages de l'utilisation d'Acunetix pour scanner les applications web sont nombreux. Certains d'entre eux sont :

- Tests pour plus de 3000 vulnérabilités
- Analyse des liens externes pour les malwares et les URL de phishing
- Scanning de HTML, JavaScript, applications monopage et services web

### 6. NODEJSSCAN

![NODEJSSCAN](https://www.freecodecamp.org/news/content/images/2020/06/nodejsscan.png)

[NodeJsScan](https://github.com/ajinabraham/NodeJsScan) est un scanner de code de sécurité statique. Il est utilisé pour découvrir les vulnérabilités de sécurité dans les applications web, les services web et les applications serverless.

Il peut être utilisé comme un outil [CLI](https://en.wikipedia.org/wiki/Command-line_interface) (qui permet à NodeJsScan d'être intégré avec des pipelines CI/CD), une application basée sur le web, et dispose également d'une API Python.

## Conclusion

Les packages, bibliothèques et composants pour les applications Node.js sont publiés régulièrement, et le fait qu'ils soient open source laisse place à des vulnérabilités. Cela est vrai que vous travailliez avec Node.js, des vulnérabilités Apache Struts, ou tout autre framework open source.

Les développeurs doivent surveiller les vulnérabilités dans les nouvelles versions des packages et savoir quand il est nécessaire de mettre à jour les packages. Les outils ci-dessus peuvent faciliter le processus de création de produits efficaces et fiables.