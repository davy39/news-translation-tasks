---
title: Comment créer un réseau de neurones en JavaScript en seulement 30 lignes de
  code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-17T12:55:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-neural-network-in-javascript-in-only-30-lines-of-code-343dafc50d49
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Z6kowWUGajls6aYusTy4oA.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: JavaScript
  slug: javascript
- name: Machine Learning
  slug: machine-learning
- name: technology
  slug: technology
seo_title: Comment créer un réseau de neurones en JavaScript en seulement 30 lignes
  de code
seo_desc: 'By Per Harald Borgen

  In this article, I’ll show you how to create and train a neural network using Synaptic.js,
  which allows you to do deep learning in Node.js and the browser.

  We’ll be creating the simplest neural network possible: one that manages ...'
---

Par Per Harald Borgen

Dans cet article, je vais vous montrer comment créer et entraîner un réseau de neurones en utilisant [Synaptic.js](https://synaptic.juancazala.com/#/), qui vous permet de faire du deep learning dans Node.js et le navigateur.

Nous allons créer le réseau de neurones le plus simple possible : un réseau capable de résoudre l'équation [XOR](https://en.wikipedia.org/wiki/Exclusive_or).

J'ai également créé un tutoriel interactif Scrimba sur cet exemple, alors consultez-le également :

![Dans le tutoriel Scrimba, vous pourrez manipuler le code à tout moment.](https://cdn-media-1.freecodecamp.org/images/1*RcK-DD5atXLQ6C4Q-K3yyg.png)
_[Dans le tutoriel Scrimba, vous pourrez manipuler le code à tout moment.](https://scrimba.com/casts/cast-1980?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gneuralnetworks_create_neural_network)_

Ou si vous êtes intéressé par un cours complet sur les réseaux de neurones en JavaScript, consultez notre [cours gratuit sur Brain.js chez Scrimba](https://scrimba.com/g/gneuralnetworks?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gneuralnetworks_create_neural_network).

![Cliquez sur l'image pour accéder au cours](https://cdn-media-1.freecodecamp.org/images/1*c1h9Q0lvSdhy5lrmMAq1Pw.png)
_[Cliquez ici pour accéder au cours](https://scrimba.com/g/gneuralnetworks?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gneuralnetworks_create_neural_network)_

Mais avant de regarder le code, passons en revue les bases des réseaux de neurones.

### Neurones et synapses

Le premier élément constitutif d'un réseau de neurones est, eh bien, les [neurones](https://medium.com/learning-new-stuff/how-to-learn-neural-networks-758b78f2736e).

Un neurone est comme une fonction, il prend quelques entrées et retourne une sortie.

Il existe de nombreux types de neurones différents. Notre réseau va utiliser des [neurones sigmoïdes](https://en.wikipedia.org/wiki/Sigmoid_function), qui prennent n'importe quel nombre et le compressent à une valeur entre `0` et `1`.

Le cercle ci-dessous illustre un neurone sigmoïde. Son entrée est `5` et sa sortie est `1`. Les flèches sont appelées synapses, qui relient le neurone à d'autres couches du réseau.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TGn24UaXx1LNcyuiySa0NQ.png)

Alors **pourquoi** le nombre rouge est-il `5` ? Parce que c'est la somme des trois synapses qui se connectent au neurone, comme le montrent les trois flèches à gauche. Décomposons cela.

À l'extrême gauche, nous voyons deux valeurs plus une valeur dite **biais**. Les valeurs sont `1` et `0` qui sont les nombres verts. La valeur de biais est `-2` qui est le nombre marron.

Tout d'abord, les deux entrées sont multipliées par leurs **poids**, qui sont `7` et `3` comme le montrent les nombres bleus.

Enfin, nous additionnons cela avec le biais et nous obtenons `5` ou le nombre rouge. C'est l'entrée de notre neurone artificiel.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CjCW6wYx4zYF_X6OnaDCNQ.png)

Comme il s'agit d'un neurone sigmoïde qui comprime toute valeur entre 0 et 1, la sortie est réduite à `1`.

Si vous connectez un réseau de ces neurones ensemble, vous avez un réseau de neurones. Cela se propage vers l'avant de l'entrée à la sortie, via des neurones qui sont connectés les uns aux autres par des synapses. Comme sur l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*9dt933ts_01LH25ERAM8mw.png)

Le but d'un réseau de neurones est de l'entraîner à faire des généralisations, comme reconnaître des chiffres manuscrits ou des spams. Et être bon en généralisation est une question d'avoir les bons **poids** et les bonnes valeurs de **biais** à travers le réseau. Comme avec les nombres bleus et marron dans notre exemple ci-dessus.

Lors de l'entraînement du réseau, vous lui montrez simplement des tonnes d'exemples comme des chiffres manuscrits, et vous faites en sorte que le réseau prédise la bonne réponse.

Après chaque prédiction, vous calculerez **à quel point** la prédiction était fausse, et vous ajusterez les poids et les valeurs de biais afin que le réseau devine un peu plus correctement la prochaine fois. Ce processus d'apprentissage est appelé rétropropagation. Faites cela des milliers de fois et votre réseau deviendra bientôt bon en généralisation.

Comment la rétropropagation fonctionne techniquement est hors du cadre de ce tutoriel, mais voici les trois meilleures sources que j'ai trouvées pour la comprendre :

* [A Step by Step Backpropagation Example](http://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/) — par [Matt Mazur](https://medium.com/u/f481b80ce964)
* [Hackers Guide to Neural Nets](http://karpathy.github.io/neuralnets/) — par [Andrej Karpathy](https://medium.com/u/ac9d9a35533e)
* [NeuralNetworksAndDeepLarning](http://neuralnetworksanddeeplearning.com/chap1.html) — par [Michael Nielsen](https://twitter.com/michael_nielsen)

### Le code

Maintenant que vous avez une introduction de base, plongeons dans le code. La première chose que nous devons faire est de créer les couches. Nous faisons cela avec la fonction `new Layer()` dans synaptic. Le nombre passé à la fonction dicte combien de neurones chaque couche doit avoir.

Si vous êtes confus sur ce qu'est une **couche**, consultez le [screencast](https://scrimba.com/casts/cast-1980?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gneuralnetworks_create_neural_network) ci-dessus.

const { Layer, Network } = window.synaptic;

var inputLayer = new Layer(2);  
var hiddenLayer = new Layer(3);  
var outputLayer = new Layer(1);

Ensuite, nous allons connecter ces couches ensemble et instancier un nouveau réseau, comme ceci :

inputLayer.project(hiddenLayer);  
hiddenLayer.project(outputLayer);

var myNetwork = new Network({  
input: inputLayer,  
hidden: [hiddenLayer],  
output: outputLayer  
});

Donc, c'est un réseau 2-3-1, qui peut être visualisé comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*IjY3wFF24sK9UhiOlf36Bw.png)

Maintenant, entraînons le réseau :

```js
// entraîner le réseau - apprendre XOR

var learningRate = 0.3;

for (var i = 0; i < 20000; i++) {  
  // 0,0 => 0  
  myNetwork.activate([0,0]);  
  myNetwork.propagate(learningRate, [0]);

  // 0,1 => 1  
  myNetwork.activate([0,1]);  
  myNetwork.propagate(learningRate, [1]);

  // 1,0 => 1  
  myNetwork.activate([1,0]);  
  myNetwork.propagate(learningRate, [1]);

  // 1,1 => 0  
  myNetwork.activate([1,1]);  
  myNetwork.propagate(learningRate, [0]);  
}

```

Ici, nous exécutons le réseau 20 000 fois. Chaque fois, nous propagons vers l'avant et vers l'arrière quatre fois, en passant les quatre entrées possibles pour ce réseau : `[0,0] [0,1] [1,0] [1,1]`.

Nous commençons par faire `myNetwork.activate([0,0])`, où `[0,0]` est le point de données que nous envoyons dans le réseau. C'est la propagation vers l'avant, également appelée **activation** du réseau. Après chaque propagation vers l'avant, nous devons faire une rétropropagation, où le réseau met à jour ses propres poids et biais.

La rétropropagation est faite avec cette ligne de code : `myNetwork.propagate(learningRate, [0])`, où le `learningRate` est une constante qui indique au réseau combien il doit ajuster ses poids chaque fois. Le deuxième paramètre `0` représente la sortie correcte étant donné l'entrée `[0,0]`.

**Le réseau compare ensuite sa propre prédiction à l'étiquette correcte. Cela lui indique à quel point il avait raison ou tort.**

Il utilise la comparaison comme base pour corriger ses propres poids et valeurs de biais afin qu'il devine un peu plus correctement la prochaine fois.

Après avoir fait ce processus 20 000 fois, nous pouvons vérifier à quel point notre réseau a appris en activant le réseau avec toutes les quatre entrées possibles :

```js
console.log(myNetwork.activate([0,0]));   
// -> [0.015020775950893527]

console.log(myNetwork.activate([0,1]));  
// -> [0.9815816381088985]

console.log(myNetwork.activate([1,0]));  
// ->  [0.9871822457132193]

console.log(myNetwork.activate([1,1]));  
// -> [0.012950087641929467]

```

Si nous arrondissons ces valeurs à l'entier le plus proche, nous obtiendrons les bonnes réponses pour l'équation XOR. Hourra !

Et c'est à peu près tout. Même si nous n'avons fait qu'effleurer la surface des réseaux de neurones, cela devrait vous donner assez pour commencer à jouer avec Synaptic par vous-même et continuer à apprendre par vous-même. [Leur wiki](https://github.com/cazala/synaptic/wiki) contient beaucoup de bons tutoriels.

Enfin, assurez-vous de partager vos connaissances en créant un [Scrimba](http://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gneuralnetworks_create_neural_network) screencast ou en écrivant un article lorsque vous apprenez quelque chose de nouveau ! :)

## PS : Nous avons plus de cours gratuits pour vous !

Si vous cherchez votre prochain défi, nous avons plusieurs autres cours gratuits que vous pouvez consulter sur [Scrimba.com](https://scrimba.com/?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gneuralnetworks_create_neural_network). En voici trois qui pourraient vous intéresser :

* [Réseaux de neurones en JavaScript](https://scrimba.com/g/gneuralnetworks?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gneuralnetworks_create_neural_network)
* [Introduction à ES6+](https://scrimba.com/g/gintrotoes6?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gneuralnetworks_create_neural_network)
* [Apprendre D3 JS](https://scrimba.com/g/gd3js?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gneuralnetworks_create_neural_network)

Bon codage !