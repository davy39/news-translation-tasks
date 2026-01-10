---
title: Comment créer et utiliser une couche pour vos AWS Lambdas
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-16T09:23:47.000Z'
originalURL: https://freecodecamp.org/news/lambda-layers-2f80b9211318
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kQDtO4sMgdnizh7DLdBE2g.png
tags:
- name: AWS
  slug: aws
- name: coding
  slug: coding
- name: Productivity
  slug: productivity
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
seo_title: Comment créer et utiliser une couche pour vos AWS Lambdas
seo_desc: 'By Sam Williams

  AWS Lambdas are brilliant! They simplify deploying serverless applications. They
  allow us to really quickly build prototypes and automatically scale. One of the
  issues with having every function as a separate entity is that you need t...'
---

Par Sam Williams

Les AWS Lambdas sont brillantes ! Elles simplifient le déploiement d'applications serverless. Elles nous permettent de construire rapidement des prototypes et de mettre à l'échelle automatiquement. L'un des problèmes avec le fait d'avoir chaque fonction comme une entité séparée est que vous devez inclure du code commun dans chaque Lambda.

> Si vous devez faire la même chose de la même manière trois fois, il est temps de l'automatiser — Règle de trois de l'automatisation

%[https://www.youtube.com/watch?v=5a2LS7gNECk]

### Couches

Les couches Lambda ont été créées pour résoudre ce problème de _code répété_. Leur fonctionnement est le suivant : vous déployez votre code commun dans une couche. Cela peut être votre code commun ou des packages NPM que vous utilisez toujours. Lorsque vous connectez cette couche à l'une de vos Lambdas, vous pouvez accéder à tout le code commun depuis l'intérieur de votre Lambda.

Cela signifie que vous n'avez pas à copier le même fichier dans chaque dossier Lambda ou à créer votre propre dépôt 'common' que vous devez inclure.

### Installation d'une couche

Puisqu'une couche est simplement une collection de code, nous pouvons commencer par créer un nouveau dossier pour cette couche. J'aime avoir toutes mes couches dans un dossier à côté de mon dossier Lambdas. Nous pouvons créer un nouveau dossier de couche appelé _DemoLayer_ qui doit avoir un dossier pour le runtime qu'il va utiliser. Pour cet exemple, nous allons utiliser _nodejs_, nous créons donc ce dossier.

```bash
mkdir -p lambdaLayers/DemoLayer/nodejs
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*PIfYqz7wFGNQxnF97h99Lw.png)

En utilisant notre terminal, nous pouvons naviguer vers le dossier _DemoLayer_ et initialiser NPM.

```bash
cd lambdaLayers/DemoLayer/nodejs
npm init
```

Acceptez toutes les valeurs par défaut dans la configuration NPM, et vous aurez le fichier _package.json_ généré dans votre dossier.

Pour notre première couche, nous allons importer la bibliothèque _moment_. C'est le même processus que vous utiliseriez pour ajouter n'importe quel package NPM à la couche.

```bash
npm install --save moment
```

#### Déploiement de notre couche

Maintenant que nous avons le code commun dans notre dossier, nous devons le déployer. Pour ce faire, nous devons zipper tout le dossier, puis le télécharger en tant que couche Lambda. Pour zipper le contenu du dossier, vous pouvez naviguer dans le dossier _DemoLayer_ et exécuter une commande _zip_ sur le contenu du dossier.

```bash
cd ../
zip -r demoLayer.zip ./*
```

Vous devriez maintenant voir un fichier `demoLayer.zip` dans votre dossier. Nous pouvons maintenant aller dans la console AWS pour créer notre couche.

Dans la console AWS, naviguez vers AWS Lambda, et sur le côté gauche, nous devrions avoir des options incluant _Layers_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*J04fWaAc04iOFUBFSIPkgg.png)

Dans le menu des couches, nous avons l'option de créer une nouvelle couche. En cliquant dessus, cela ouvre les options de configuration où nous pouvons donner un nom à la couche, une description, télécharger le fichier zip que nous venons de créer et sélectionner les runtimes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lA4CyPZr32jHLu7w-76mkQ.png)

### Test de la couche

Avec la couche créée, nous pouvons tester si tout fonctionne. Pour ce faire, nous pouvons créer une nouvelle Lambda appelée _DemoWithLayer_ qui s'exécute sur node 8.10. À l'intérieur de cette Lambda, nous pouvons ajouter ce code :

```js
const moment = require('moment');

exports.handler = async (event) => {
    let momentNow = moment.now();
    
    const response = {
        statusCode: 200,
        body: JSON.stringify({momentNow}),
    };
    return response;
};
```

Nous pouvons tester ce qui se passe lorsque nous exécutons cela sans la couche en créant un événement de test. Dans le coin supérieur droit de la console Lambda, cliquez sur _select a test event_ puis sur _configure test events_. Cela ouvre une fenêtre de configuration où nous créons le blob JSON qui est envoyé au gestionnaire. Comme nous n'utilisons pas l'objet event, nous pouvons passer les valeurs par défaut, donner un nom à ce test et le créer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KhQ2qNZY0uIJkSUeBeQEpw.png)

Nous pouvons maintenant cliquer sur le bouton _Test_ pour exécuter notre Lambda. Cela donne ce message :

![Image](https://cdn-media-1.freecodecamp.org/images/1*t81K9fcj9ZZHyA6IJ9tvVA.png)

Cela est dû au fait que notre Lambda n'a pas le module _moment_ installé. Nous pouvons maintenant ajouter notre nouvelle couche à la Lambda et relancer le test.

Pour ajouter une couche, cliquez sur le bouton _Layers_ sous le bouton _DemoWithLayer_. Faites défiler jusqu'en bas de la page vers la section _Referenced layers_ et cliquez sur le bouton _add a layer_. Dans la fenêtre contextuelle, nous pouvons sélectionner notre _DemoLayer_ dans la liste déroulante et sélectionner la version la plus élevée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sB0HC6rsFrYOzaTMLOvrVg.png)

Ajoutez cela à la Lambda et assurez-vous de sauvegarder les modifications de la Lambda. Lorsque nous relançons le test, nous obtenons une réponse de succès. Vous pouvez utiliser ce processus pour supprimer de nombreux packages communs de vos Lambdas.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Xc59dAEq2aYdk4WlrdYFXg.png)