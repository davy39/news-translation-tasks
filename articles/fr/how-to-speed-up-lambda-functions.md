---
title: Comment accélérer vos fonctions Lambda
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-25T19:43:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-speed-up-lambda-functions
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-zhang-kaiyv-842654.jpg
tags:
- name: lambda
  slug: lambda
- name: performance
  slug: performance
seo_title: Comment accélérer vos fonctions Lambda
seo_desc: "By Ali Haydar\nLambda has gained massive popularity over the past few years.\
  \ It has various use cases, from running simple scripts to gluing flows and processes\
  \ within a serverless architecture or when running microservices. \nStill, if you've\
  \ just sta..."
---

Par Ali Haydar

Lambda a gagné une immense popularité au cours des dernières années. Il a divers cas d'utilisation, de l'exécution de scripts simples à l'assemblage de flux et de processus au sein d'une architecture serverless ou lors de l'exécution de microservices. 

Néanmoins, si vous venez de commencer à travailler dans un nouvel environnement ou une nouvelle organisation, vous pourriez vous sentir prudent quant à son utilisation en raison de sa complexité de configuration. 

Cela est compréhensible avec toute nouvelle technologie que vous vous préparez à utiliser, et être prudent est un signe de bon sens commercial. 

Un argument que vous pourriez souvent entendre est que Lambda pourrait ralentir votre opération en raison des démarrages à froid.

C'est également un sujet courant lors des entretiens techniques, il est donc utile d'approfondir un peu si vous avez un œil sur ce prochain poste de rêve en ingénierie cloud.

|![cold-start-image](https://www.freecodecamp.org/news/content/images/2022/04/cold-start-image.jpeg)|
|:--:|
| Photo par [Myriams-Fotos](https://pixabay.com/users/myriams-fotos-1627417/) sur [pixabay](https://pixabay.com/photos/dawn-winter-snow-nature-frost-3142990/)|

Dans cet article, nous parlerons d'une méthode qui peut aider à améliorer les performances de vos fonctions Lambda. 

Mais commençons d'abord par un aperçu de ce qui se passe lorsque vous exécutez une fonction Lambda, en abordant les démarrages à froid.

## Comment une fonction Lambda est-elle exécutée ?

Lorsque votre fonction Lambda est déclenchée, le service Lambda exécute le code dans un "Environnement d'exécution" avec trois phases : `Init`, `Invoke` et `Shutdown`.

![execution-environment-1](https://www.freecodecamp.org/news/content/images/2022/04/execution-environment-1.png)

- Dans la phase `Init`, Lambda crée l'environnement d'exécution, télécharge le code, configure la configuration (par exemple, la mémoire) et exécute le _code_ qui se trouve en dehors de la fonction `handler`. (Vous avez peut-être déjà saisi l'essentiel de l'article à ce stade – mais continuez à lire pour une explication plus approfondie et une démonstration.)
- Dans la phase `Invoke`, Lambda exécute le code à l'intérieur de la fonction `handler`
- Dans la phase `Shutdown`, Lambda termine l'environnement

Il pourrait y avoir plusieurs `Invocations` entre une phase `Init` et une phase `Shutdown` si le Lambda a été déclenché plusieurs fois de suite dans un laps de temps relativement court (ce temps n'est pas précisément déterminé dans la documentation Lambda). 

Cela signifie que si plusieurs exécutions consécutives de la Lambda se produisent dans un court laps de temps, le service Lambda utiliserait le premier environnement d'exécution créé pour exécuter l'invocation suivante. C'est-à-dire qu'il appellerait uniquement la fonction handler avec chaque nouvel appel à la Lambda sans avoir à créer un nouvel environnement d'exécution et sans avoir à exécuter le code qui se trouve en dehors de la fonction handler.

La phase `Init` ne se produit qu'une seule fois lors de la première exécution, et nous pouvons la visualiser en deux parties (les deux s'exécutent une fois par exécution) :

- La partie où un nouvel environnement d'exécution est créé et le code est téléchargé est le _démarrage à froid_.
- La partie où le code en dehors du handler Lambda est exécuté est le code d'initialisation.

D'après la [documentation AWS](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-context.html), cette image fournit une visualisation appropriée des 3 phases :
![execution-environment-phases](https://www.freecodecamp.org/news/content/images/2022/04/execution-environment-phases.png)

La fonction INIT (le dernier bloc de la phase INIT) ne s'exécutera qu'une seule fois, ainsi que les deux premiers blocs qui forment le démarrage à froid.

Assez parlé – montrez-nous le code !

## Code de la fonction Lambda

Dans la section précédente, nous avons discuté du fait que Lambda exécuterait le code d'initialisation (code en dehors de la fonction handler) une fois lors de la première exécution. Et il exécuterait le code à l'intérieur du handler en utilisant le même environnement d'exécution si les invocations suivantes ne se produisaient pas trop loin les unes des autres. 

C'est une manière parfaite de tirer parti du code d'initialisation pour exécuter le code réutilisable et gagner du temps en réexécutant ce code à chaque fois avec chaque invocation.

Supposons que nous avons une fonction Lambda qui interagit avec une base de données DynamoDB pour récupérer un ensemble d'éléments (veuillez garder à l'esprit que ce code est à des fins de démonstration uniquement, donc ce n'est pas le plus propre que vous verrez).

Créez un fichier `index.js` :

```
const { DynamoDB } = require("@aws-sdk/client-dynamodb");

exports.handler = async (event, context) => {
  const dynamodb = new DynamoDB({ region: "ap-southeast-2" }); // création d'une nouvelle instance de DynamoDB
  const params = {
    TableName: "company",
  };

  const results = await dynamodb.scan(params); // évitez d'utiliser scan en production - c'est coûteux et peu performant

  return {
    statusCode: 200,
    body: JSON.stringify(results),
  };
};
```

Dans l'extrait précédent, le code d'initialisation est le suivant :

```
const { DynamoDB } = require('@aws-sdk/client-dynamodb');
```

Il s'exécutera une fois lors de la première exécution et ne s'exécutera pas lors des exécutions suivantes si elles se produisent dans un court laps de temps – c'est-à-dire que les exécutions suivantes se sont produites avant que la phase de Shutdown ne soit atteinte.

## Démo Lambda

Super, nous sommes maintenant prêts pour la démonstration. Dans cette section, nous allons construire l'infrastructure et tester les performances de la Lambda.

### Construire l'infrastructure

Comme ce tutoriel vise à démontrer comment améliorer les performances de notre Lambda, nous ne mettrons pas trop l'accent sur l'infrastructure en tant que code.

Suivez ces étapes pour construire et déployer votre application :

- Installez les dépendances : `npm install`
- Zippez votre fichier Lambda : `zip -r ./get-companies-lambda.zip index.js node_modules`
- Téléchargez le fichier Terraform suivant : https://gist.github.com/AHaydar/bfc173db2078b2eeb884da8632248c5d
- Appliquez les changements Terraform : `terraform apply`

Ouvrez la console AWS et validez que DynamoDB et Lambda ont été créés correctement (j'utilise la région `ap-southeast-2` dans cet exemple).

### Tester les performances

Tout d'abord, naviguez jusqu'à votre fonction Lambda dans la console AWS et cliquez sur le bouton `Test` pour exécuter votre code. Vous obtiendrez un résultat similaire à ce qui suit : ![init-duration](https://www.freecodecamp.org/news/content/images/2022/04/init-duration.png)

Remarquez ce qui suit dans la dernière ligne :

`Duration: 569.85 ms`

et

`Init Duration: 429.13 ms`

La `Init Duration` est la durée d'exécution du code en dehors du handler Lambda – c'est le code qui nécessite le SDK DynamoDB.

La `Duration` est la durée d'exécution du code à l'intérieur de votre handler Lambda – instanciation de DynamoDB en passant la région "ap-southeast-2" et analyse de la table.

Cliquez à nouveau sur le bouton `Test`. Vous devriez obtenir une réponse comme celle-ci : ![second-execution](https://www.freecodecamp.org/news/content/images/2022/04/second-execution.png)

Remarquez la dernière ligne – elle ne contient PAS de `Init Duration`. Si votre résultat incluait une Init Duration, cela signifie que l'environnement d'exécution a été arrêté avant que vous ne cliquiez à nouveau sur le bouton `Test`. Dans ce cas, cliquez une autre fois.

Ainsi, lors de la deuxième exécution, nous avons économisé la `Init Duration`. C'est un indice pour optimiser notre fonction et ajouter plus de code commun en dehors du handler Lambda. Comment pouvons-nous faire cela ?

```
const { DynamoDB } = require("@aws-sdk/client-dynamodb");

const dynamodb = new DynamoDB({ region: "ap-southeast-2" }); // création d'une nouvelle instance de DynamoDB
const params = {
  TableName: "company",
};

exports.handler = async (event, context) => {
  const results = await dynamodb.scan(params); // évitez d'utiliser scan en production - c'est coûteux et peu performant

  return {
    statusCode: 200,
    body: JSON.stringify(results),
  };
};
```

Dans l'extrait ci-dessus, j'ai déplacé l'instanciation de DynamoDB en dehors du handler, ainsi que l'objet params. 

Cela augmenterait donc le temps d'exécution du code d'initialisation (en dehors du handler lambda), qui ne s'exécute que lors de la première exécution du cycle de vie de l'environnement d'exécution. Et cela diminuerait le temps d'exécution du handler Lambda, qui se produit à chaque invocation.

Gardez à l'esprit que vous ne devriez jamais écrire de logique métier qui dépend de la présence d'un environnement d'exécution en cours d'exécution. Votre code doit toujours supposer qu'il doit initialiser l'environnement d'exécution à chaque invocation.

Quels autres conseils avez-vous pour optimiser les performances de votre Lambda ? Partagez-les avec moi sur [Twitter](https://twitter.com/Alee_Haydar) ou [LinkedIn](https://www.linkedin.com/in/ahaydar/)