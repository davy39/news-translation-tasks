---
title: Comment créer des images serverless en utilisant AWS Lambda et ChartJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-19T21:40:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-serverless-images-using-aws-lambda-and-chartjs-3d18254b05ef
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UrOibhQ3ePj0qPlEQLsrhg.png
tags:
- name: AWS
  slug: aws
- name: chartjs
  slug: chartjs
- name: charts
  slug: charts
- name: serverless
  slug: serverless
seo_title: Comment créer des images serverless en utilisant AWS Lambda et ChartJS
seo_desc: 'By Martin van Vliet

  I’m working on a project to push sprint burndown information to distributed Scrum
  teams working in Slack. The entire application is serverless and running inside
  AWS. To generate burndown images I wanted to build a lambda function...'
---

Par Martin van Vliet

Je travaille sur un [projet visant à pousser des informations de burndown de sprint vers des équipes Scrum distribuées travaillant dans Slack](https://sprintlr.io). L'ensemble de l'application est serverless et s'exécute dans AWS. Pour générer des images de burndown, je voulais créer une fonction lambda qui génère une image, puis la pousse vers un bucket S3. Dans cet article, je vais décrire la solution que j'ai trouvée.

Tout d'abord, la bibliothèque de graphiques. Après avoir étudié plusieurs options, j'ai opté pour l'utilisation de la [bibliothèque ChartJS](http://www.chartjs.org/). C'est une excellente bibliothèque de graphiques en JavaScript qui peut rendre tous types de graphiques en utilisant le canvas HTML5. Très flexible et configurable, aussi. Mais comment l'exécuter, en mode headless, à l'intérieur d'une lambda ?

Ma première tentative a été de créer une lambda simple sur mon MacBook en utilisant trois packages NPM : **chart.js** et deux autres bibliothèques : [**chartjs-node-canvas**](https://www.npmjs.com/package/chartjs-node-canvas) et [**canvas-prebuilt**](https://www.npmjs.com/package/canvas-prebuilt). La première est un wrapper autour de ChartJS qui supporte le rendu des graphiques dans node. La seconde est une version native précompilée du canvas HTML5 qui permet de rendre un canvas en mode headless sans navigateur. J'ai construit la lambda avec le [framework serverless](https://serverless.com/), un outil très utile pour créer et déployer des applications serverless.

Voici ma lambda d'exemple :

Ma lambda a généré un graphique d'exemple et tout semblait bien lorsque je l'ai exécutée localement. Sur AWS, cependant, elle a échoué. Pourquoi ?

Il s'avère que ChartJS utilise des _modules NPM natifs_ pour rendre directement sur le canvas. Évidemment, les modules natifs que j'utilise sur mon MacBook ne s'exécutent pas à l'intérieur d'une lambda. Alors, que faire ?

Pour exécuter des modules natifs à l'intérieur d'une lambda, j'ai dû utiliser les bibliothèques natives dont l'[environnement d'exécution lambda](https://docs.aws.amazon.com/lambda/latest/dg/current-supported-versions.html) a besoin. J'ai donc lancé une instance de l'AMI de l'environnement d'exécution lambda sur EC2 et je m'y suis connecté. Là, j'ai pris la même lambda que j'avais construite précédemment et j'ai exécuté **npm install** sur l'instance EC2. Cela télécharge les bibliothèques NPM natives dont ChartJS a besoin, mais cette fois pour l'environnement d'exécution lambda. Avec ces bibliothèques faisant partie de la fonction lambda, ChartJS est capable de rendre une image comme il le ferait normalement. Youpi !

Contrairement aux projets NPM normaux, j'ai ajouté les modules node téléchargés dans mon dépôt git. Lors de la mise à jour ou de la construction de la lambda de graphique, faites attention à ne pas écraser vos dépendances. Un effet secondaire de cette approche est que je ne peux plus exécuter le code sur mon ordinateur portable local pour le tester.

Ensuite : stocker le fichier image généré dans un bucket S3. Cela a en fait été une tâche assez simple avec de nombreux extraits de code disponibles en ligne pour apprendre. Pour être complet, voici le mien :

C'est tout ! Maintenant, vous pouvez générer des images de manière économique, à la demande !

L'utilisation de bibliothèques natives n'est pas sans problèmes. J'ai eu tout le système qui fonctionne ou échoue en fonction de la version exacte de **canvas-prebuilt** que j'utilise. La configuration actuelle utilise en fait deux versions. Une dépendance transitive via **chartjs-node-canvas** (2.0.0-alpha.14). Une que je spécifie directement (1.6.5-prerelease.1). Si j'en enlève une, l'application échoue à démarrer en raison de certaines erreurs de liaison. Les résultats peuvent varier.

J'ai rassemblé un dépôt git avec le code d'exemple et les binaires si vous souhaitez l'essayer. [Consultez le code source](https://github.com/techfu-io/chartjs-lambda).

_Martin travaille en tant que VP Engineering pour [StackState](https://www.stackstate.com) où lui et ses équipes construisent un produit de surveillance et d'AIOps de nouvelle génération. En tant que projet parallèle, Martin travaille sur [Sprintlr](https://sprintlr.io), un outil pour améliorer les équipes Scrum distribuées, et [techfu.io](https://techfu.io), un outil pour évaluer automatiquement les talents techniques._