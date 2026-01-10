---
title: À quel point le SDK AWS complet est-il coûteux ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-23T15:07:36.000Z'
originalURL: https://freecodecamp.org/news/just-how-expensive-is-the-full-aws-sdk-3713fed4fe70
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xFEOPesnxHTgZFBGzwQ6Kg.jpeg
tags:
- name: AWS
  slug: aws
- name: Cloud
  slug: cloud
- name: Productivity
  slug: productivity
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
seo_title: À quel point le SDK AWS complet est-il coûteux ?
seo_desc: 'By Yan Cui

  If you’re not familiar with how cold start works within the context of AWS Lambda,
  then read this post first.

  When a Node.js Lambda function cold starts, a number of things happen:


  the Lambda service has to find a server with enough capac...'
---

Par Yan Cui

*Si vous n'êtes pas familier avec le fonctionnement du cold start dans le contexte d'AWS Lambda, lisez d'abord [cet article](https://theburningmonk.com/2018/01/im-afraid-youre-thinking-about-aws-lambda-cold-starts-all-wrong/).*

Lorsqu'une fonction Lambda Node.js démarre à froid, plusieurs choses se produisent :

* le service Lambda doit trouver un serveur avec suffisamment de capacité pour héberger le nouveau conteneur
* le nouveau conteneur est initialisé
* le runtime Node.js est initialisé
* votre module de gestionnaire est initialisé, ce qui inclut l'initialisation de toutes les variables globales et fonctions que vous déclarez en dehors de la fonction de gestionnaire

Si vous activez le traçage actif pour une fonction Lambda, vous pourrez voir combien de temps est consacré à ces étapes dans X-Ray. Malheureusement, le temps nécessaire pour initialiser le conteneur et le runtime Node.js n'est pas enregistré en tant que segments. Mais vous pouvez le déduire de la différence de durée.

Ici, `Initialization` fait référence au temps nécessaire pour initialiser le module de gestionnaire.

![Image](https://cdn-media-1.freecodecamp.org/images/oJHJ0JDLY-CfzclwpKjswAorw17pnVNoP26N)

La trace ci-dessus est pour la fonction ci-dessous, qui nécessite le SDK AWS et rien d'autre. Comme vous pouvez le voir, ce simple `require` a ajouté 147 ms au cold start.

```
const AWS = require('aws-sdk')module.exports.handler = async () => {}
```

Considérez cela comme le coût de faire des affaires lorsque votre fonction doit interagir avec des ressources AWS. Mais, si vous n'avez besoin d'interagir qu'avec un seul service (par exemple DynamoDB), vous pouvez économiser un peu de temps d'initialisation avec cette ligne unique.

```
const DynamoDB = require('aws-sdk/clients/dynamodb') const documentClient = new DynamoDB.DocumentClient()
```

Cela nécessite le client DynamoDB directement sans initialiser tout le SDK AWS. J'ai mené une expérience pour voir combien de temps de cold start vous pouvez économiser avec ce simple changement.

*Le mérite revient à mon collègue [**Justin Caldicott**](https://www.linkedin.com/in/justin-caldicott-96b36a9/) pour avoir piqué ma curiosité et fait une grande partie de l'analyse initiale.*

En plus du SDK AWS, nous nécessitons souvent le SDK XRay et l'utilisons pour auto-instrumenter le SDK AWS. Malheureusement, le package `aws-xray-sdk` a également quelques bagages supplémentaires dont nous n'avons pas besoin. Par défaut, il supporte les applications Express.js, MySQL et Postgres. Si vous êtes seulement intéressé par l'instrumentation du SDK AWS et des modules `http`/`https`, alors vous n'avez besoin que du `aws-xray-sdk-core`.

![Image](https://cdn-media-1.freecodecamp.org/images/oA2OPpll77iNxdSt70GgZsvjww92JXt44144)

### Méthodologie

J'ai testé plusieurs configurations :

* [sans SDK AWS](https://github.com/theburningmonk/aws-sdk-coldstart-overhead/blob/master/functions/no-aws-sdk.js)
* [en nécessitant uniquement le client DynamoDB](https://github.com/theburningmonk/aws-sdk-coldstart-overhead/blob/master/functions/dynamodb-only.js)
* [en nécessitant le SDK AWS complet](https://github.com/theburningmonk/aws-sdk-coldstart-overhead/blob/master/functions/aws-sdk.js)
* [en nécessitant uniquement le SDK XRay (sans SDK AWS)](https://github.com/theburningmonk/aws-sdk-coldstart-overhead/blob/master/functions/aws-xray-sdk-require-only.js)
* [en nécessitant le SDK XRay et en instrumentant le SDK AWS](https://github.com/theburningmonk/aws-sdk-coldstart-overhead/blob/master/functions/aws-xray-sdk.js)
* [en nécessitant le SDK XRay Core et en instrumentant le SDK AWS](https://github.com/theburningmonk/aws-sdk-coldstart-overhead/blob/master/functions/aws-xray-sdk-core.js)
* [en nécessitant le SDK XRay Core et en instrumentant uniquement le client DynamoDB](https://github.com/theburningmonk/aws-sdk-coldstart-overhead/blob/master/functions/trace-dynamodb-only.js)

Chacune de ces fonctions est tracée par X-Ray. Le taux d'échantillonnage est fixé à 100 %, afin de ne rien manquer. Nous ne nous intéressons qu'à la durée du segment **Initialization**, car il correspond au temps nécessaire pour initialiser ces dépendances.

![Image](https://cdn-media-1.freecodecamp.org/images/vti9c-ncmZmjEhZ1EAsigD4Izw5ytDib-vIx)

Le cas `no AWS SDK` est notre groupe témoin. Nous pouvons voir combien de temps chaque dépendance supplémentaire ajoute à notre durée d'**Initialization**.

Pour collecter un ensemble de données statistiquement significatif, j'ai décidé d'automatiser le processus en utilisant Step Functions.

![Image](https://cdn-media-1.freecodecamp.org/images/WLmC8wSjkh5BzqCqZ8Lt1h6PjX3-XXPCQVO2)

* La machine d'état prend une entrée `{ functionName, count }`.
* L'étape `SetStartTime` ajoute l'horodatage UTC actuel à l'état d'exécution. Cela est nécessaire car nous avons besoin de l'heure de début de l'expérience pour récupérer les traces pertinentes de X-Ray.
* L'étape `Loop` déclenche le nombre souhaité de cold starts pour la fonction spécifiée. Pour déclencher des cold starts, je mets à jour programmatiquement une variable d'environnement avant d'invoquer la fonction. De cette manière, je m'assure que chaque invocation est un cold start.

![Image](https://cdn-media-1.freecodecamp.org/images/n53oR25NejQ5zkTR3Ac1Lu4qstHCrm9dOI1E)

* L'étape `Wait30Seconds` s'assure que toutes les traces sont publiées vers XRay avant que nous tentions de les analyser.
* L'étape `Analyze` récupère toutes les traces pertinentes dans XRay et produit plusieurs statistiques autour de la durée d'**Initialization**.

Chaque configuration est testée sur 1000 cold starts. Parfois, les traces XRay sont incomplètes (voir ci-dessous). Ces traces incomplètes sont exclues dans l'étape `Analyze`.

![Image](https://cdn-media-1.freecodecamp.org/images/njYdfDGCkx4x0o4zurYChzt7jsDVUqwpgU2F)
*où est le segment AWS::Lambda:Function ?*

Chaque configuration est également testée avec WebPack (en utilisant le plugin [serverless-webpack](https://github.com/serverless-heaven/serverless-webpack)). *Merci à [Erez Rokah](https://www.freecodecamp.org/news/just-how-expensive-is-the-full-aws-sdk-3713fed4fe70/undefined) pour la suggestion.*

### Les Résultats

Voici les temps d'**Initialization** pour tous les cas de test.

![Image](https://cdn-media-1.freecodecamp.org/images/cAjSzzz77ppKqsM1osUtqn6-OlhkUpN-LA0g)

![Image](https://cdn-media-1.freecodecamp.org/images/XehPjBmG-NAXGOMkt5CMl0FrqmUfGXYFGN7S)

Observations clés :

* WebPack améliore le temps d'**Initialization** dans tous les cas.
* Sans aucune dépendance, le temps d'**Initialization** moyenne seulement 1,72 ms sans WebPack et 0,97 ms avec WebPack.
* L'ajout du SDK AWS comme seule dépendance ajoute en moyenne 245 ms sans WebPack. Cela est assez significatif. L'ajout de WebPack n'améliore pas significativement les choses non plus.
* En nécessitant uniquement le client DynamoDB (le changement en une ligne discuté précédemment), on économise jusqu'à 176 ms ! Dans 90 % des cas, l'économie était de plus de 130 ms. Avec WebPack, l'économie est encore plus dramatique.
* Le coût de la nécessité du SDK XRay est à peu près le même que celui du SDK AWS.
* Il n'y a pas de différence statistiquement significative entre l'utilisation du SDK XRay complet et du SDK XRay Core. Avec ou sans WebPack.

*Initialement publié sur [theburningmonk.com](https://theburningmonk.com/2019/03/just-how-expensive-is-the-full-aws-sdk/) le 23 mars 2019.*