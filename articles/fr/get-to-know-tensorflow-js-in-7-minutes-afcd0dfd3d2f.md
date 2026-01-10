---
title: Découvrez TensorFlow.js en 7 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-26T16:54:45.000Z'
originalURL: https://freecodecamp.org/news/get-to-know-tensorflow-js-in-7-minutes-afcd0dfd3d2f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*aPXPaPQHeHnMHq-j
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Deep Learning
  slug: deep-learning
- name: JavaScript
  slug: javascript
- name: Machine Learning
  slug: machine-learning
- name: TensorFlow
  slug: tensorflow
seo_title: Découvrez TensorFlow.js en 7 minutes
seo_desc: 'By ADL

  And learn how you can run ML/DL models directly in the browser

  An increasing number of developers are using TensorFlow in their machine learning
  projects. In March this year, the TensorFlow team at Google announced the arrival
  of the much-awai...'
---

Par ADL

#### Et apprenez comment exécuter des modèles ML/DL directement dans le navigateur

Un nombre croissant de développeurs utilisent TensorFlow dans leurs projets de machine learning. En mars de cette année, l'équipe TensorFlow chez Google a annoncé l'arrivée du framework JavaScript tant attendu, TensorFlow.js (qui s'appelait auparavant DeepLearn.js).

![Image](https://cdn-media-1.freecodecamp.org/images/1*F-1fq9TNjDnAYPAXnZP4Ww.png)
_Source de l'image : Site Web Tensorflow.js_

Maintenant, les développeurs peuvent construire des modèles légers et les exécuter dans le navigateur en utilisant JavaScript. Comprenons quel était le besoin pour le développement de ce framework.

#### Histoire

Avant de passer à TensorFlow.js, je voudrais commencer par TensorFlow.

TensorFlow a été développé en 2011 chez Google en tant que bibliothèque propriétaire pour les applications de Machine Learning/Deep Learning chez Google. Cette bibliothèque a été open source en 2015 sous la licence Apache.

TensorFlow est construit en C++, ce qui permet au code de s'exécuter à un très bas niveau. TensorFlow a des liaisons avec différents langages comme Python, R et Java. Cela permet à TensorFlow d'être utilisé dans ces langages.

Donc, la question évidente est : qu'en est-il de JavaScript ?

Conventionnellement, en JavaScript, le ML/DL était effectué en utilisant une API. Une API était créée en utilisant un framework, et le modèle était déployé sur le serveur. Le client envoyait une requête en utilisant JavaScript pour obtenir des résultats du serveur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PQljWmzjl-AD45YGJKROcg.png)
_Architecture Client Serveur_

En 2017, un projet appelé Deeplearn.js est apparu, qui visait à permettre le ML/DL en JavaScript, sans le tracas de l'API.

Mais il y avait des questions sur la vitesse. Il était très bien connu que le code JavaScript ne pouvait pas s'exécuter sur GPU. Pour résoudre ce problème, WebGL a été introduit. Il s'agit d'une interface de navigateur vers OpenGL. WebGL a permis l'exécution du code JavaScript sur GPU.

En mars 2018, l'équipe DeepLearn.js a été intégrée à l'équipe TensorFlow chez Google et a été renommée TensorFlow.js.

Regardez la vidéo ci-dessous pour plus de détails :

### TensorFlow.js

Tensorflow.js fournit deux choses :

* Le CoreAPI, qui traite le code de bas niveau
* LayerAPI est construit sur le CoreAPI, et facilite notre vie en augmentant le niveau d'abstraction.

#### Pour commencer

Il existe deux principales façons d'obtenir TensorFlow.js dans votre projet :

#### 1. via la balise <script>

Ajoutez le code suivant à un fichier HTML :

```
<html>  <head>    <!-- Charger TensorFlow.js -->    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@0.12.0"> </script>  </head>
```

```
<body>      Bonjour  </body></html>
```

#### 2. via NPM

Ajoutez TensorFlow.js à votre projet en utilisant yarn ou npm.

```
yarn add @tensorflow/tfjs
```

```
npm install @tensorflow/tfjs
```

Dans votre fichier js principal :

```
import * as tf from '@tensorflow/tfjs';
```

### CoreAPI

#### 1. Tenseurs

Alors, qu'est-ce qu'un Tenseur ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*V83L4ydCdk21tXjP22VjXQ.jpeg)

* Un scalaire est un nombre unique. Par exemple, x = 1
* Un vecteur est un tableau de nombres. Par exemple, _x_=[1,2]
* Une matrice est un tableau 2-D  
([[1, 2],  
 [3, 4],  
 [5, 6]])
* Un tenseur est un tableau _n-_dimensionnel avec _n_>2

TensorFlow.js a des fonctions utilitaires pour les cas courants comme les scalaires, les tenseurs 1D, 2D, 3D et 4D, ainsi qu'un certain nombre de fonctions pour initialiser les tenseurs de manière utile pour le machine learning.

#### Exemples de code

tf.tensor():

```
// Passez un tableau de valeurs pour créer un vecteur.tf.tensor([1, 2, 3, 4]).print();
```

tf.scalar():

```
tf.scalar(3.14).print();
```

Et ainsi de suite…

Regardez la vidéo ci-dessous pour obtenir une compréhension approfondie des tenseurs dans TensorFlow.js :

#### 2. Variables et opérations

Les tenseurs sont des structures de données immuables. Cela signifie que leurs valeurs ne peuvent pas être changées une fois qu'elles sont définies.

Cependant, `tf.variable()` est introduit dans TensorFlow.js. Le cas d'utilisation réel pour `tf.variable()` est lorsque nous devons changer les données fréquemment, comme lors de l'ajustement des poids du modèle en Machine Learning.

Exemple de code :

```
const x = tf.variable(tf.tensor([1, 2, 3]));x.assign(tf.tensor([4, 5, 6]));x.print();
```

#### Opérations

Il existe diverses opérations dans TensorFlow.js. Afin d'effectuer des calculs mathématiques sur les tenseurs, nous utilisons des opérations. Les tenseurs sont immuables, donc toutes les opérations retournent toujours de nouveaux tenseurs et ne modifient jamais les tenseurs d'entrée. Donc `tf.variable()` peut être utilisé afin d'économiser de la mémoire.

Examinons quelques opérations :

**tf.add() — Ajoute deux [tf.Tensor](https://js.tensorflow.org/api/0.12.0/#class:Tensor)s élément par élément**

```
const a = tf.tensor1d([1, 2, 3, 4]);const b = tf.tensor1d([10, 20, 30, 40]);a.add(b).print();  // ou tf.add(a, b)
```

Il existe de nombreuses opérations dans TensorFlow.js. Vous pouvez consulter la [documentation](https://js.tensorflow.org/api/0.12.0/#Operations) pour d'autres opérations. Je vais démontrer une autre opération ici : **tf.matmul()**

**tf.matmul() — Calcule le produit scalaire de deux matrices, A * B.**

```
const a = tf.tensor2d([1, 2], [1, 2]);const b = tf.tensor2d([1, 2, 3, 4], [2, 2]);
```

```
a.matMul(b).print();  // ou tf.matMul(a, b)
```

Regardez la vidéo ci-dessous pour une compréhension approfondie des variables et des opérations :

#### **3. Gestion de la mémoire**

La gestion de la mémoire est la clé dans les tâches de Machine Learning/Deep Learning, car elles sont généralement coûteuses en calcul.

TensorFlow.js fournit deux principales façons de gérer la mémoire :

1. tf.dispose()
2. tf.tidy()

Ils font tous les deux généralement la même chose, mais ils le font de différentes manières.

#### tf.tidy()

Cela exécute la fonction fournie `fn` et après son exécution, nettoie tous les tenseurs intermédiaires alloués par `fn` sauf ceux retournés par `fn`.

`tf.tidy()` aide à éviter les fuites de mémoire. En général, il enveloppe les appels aux opérations dans `[tf.tidy()](https://js.tensorflow.org/api/0.12.0/#tidy)` pour un nettoyage automatique de la mémoire.

Exemple de code :

```
const y = tf.tidy(() => {   // aa, b, et two seront nettoyés lorsque tidy se terminera.   const two= tf.scalar(2);   const aa = tf.scalar(2);   const b = aa.square();   console.log('numTensors (dans tidy): ' + tf.memory().numTensors);   // La valeur retournée à l'intérieur de la fonction tidy sera retournée   // à travers tidy, dans ce cas à la variable y.   return b.add(two);});console.log('numTensors (hors tidy): ' + tf.memory().numTensors);y.print();
```

#### tf.dispose()

Élimine tout [tf.Tensor](https://js.tensorflow.org/api/0.12.0/#class:Tensor) trouvé dans l'objet mentionné.

Exemple de code :

```
const two= tf.scalar(2);
```

```
two.dispose()
```

### LayersAPI

Les couches sont le bloc de construction principal pour construire un modèle ML/DL. Chaque couche effectuera généralement un calcul pour transformer son entrée en sortie. Sous le capot, chaque couche utilise le CoreAPI de Tensorflow.js.

Les couches prendront automatiquement en charge la création et l'initialisation des diverses variables/poids internes dont elles ont besoin pour fonctionner. Donc, fondamentalement, cela facilite la vie en augmentant le niveau d'abstraction.

Nous allons créer un exemple simple de réseau feed forward en utilisant le LayerAPI. Le réseau Feed Forward que nous allons construire est le suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*BIpRgx5FsEMhr1k2EqBKFg.gif)
_L'image est la mienne_

#### Code :

Index.html

```
<html><head><title></title><script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@0.12.0"> </script><script src="main.js" type="text/javascript"></script>
```

```
</head>
```

```
<body>Démo Tensorflow JS
```

```
</body></html>
```

main.js

```
const model = tf.sequential();
```

```
// config pour la coucheconst config_hidden = {  inputShape:[3],  activation:'sigmoid',  units:4}const config_output={  units:2,  activation:'sigmoid'}
```

```
// définition de la couche cachée et de la couche de sortieconst hidden = tf.layers.dense(config_hidden);const output = tf.layers.dense(config_output);
```

```
// ajout des couches au modèlemodel.add(hidden);model.add(output);
```

```
// définition d'un optimiseurconst optimize=tf.train.sgd(0.1);
```

```
// config pour le modèleconst config={optimizer:optimize,loss:'meanSquaredError'}
```

```
// compilation du modèlemodel.compile(config);
```

```
console.log('Modèle compilé avec succès');
```

```
// Données d'entraînement fictivesconst x_train = tf.tensor([  [0.1,0.5,0.1],  [0.9,0.3,0.4],  [0.4,0.5,0.5],  [0.7,0.1,0.9]])
```

```
// Étiquettes d'entraînement fictivesconst y_train = tf.tensor([  [0.2,0.8],  [0.9,0.10],  [0.4,0.6],  [0.5,0.5]])
```

```
// Données de test fictivesconst x_test = tf.tensor([  [0.9,0.1,0.5]])
```

```
train_data().then(function(){  console.log('L\'entraînement est terminé');  console.log('Prédictions :');  model.predict(x_test).print();})
```

```
async function train_data(){  for(let i=0;i<10;i++){  const res = await model.fit(x_train,y_train,epoch=1000,batch_size=10);   console.log(res.history.loss[0]);  }}
```

Sortie :

![Image](https://cdn-media-1.freecodecamp.org/images/1*e3eBJbrquB8p0XMQe5bdCQ.png)

Regardez les vidéos ci-dessous pour une compréhension approfondie et une explication du code :

Je comprends que ceci est un petit aperçu de la bibliothèque Tensorflow.js. Je pense que cela peut être un point de départ avant de lire la [documentation](https://js.tensorflow.org/api/0.12.0/) et de passer à quelques applications réelles.

Je vais publier des exemples réels utilisant TensorFlow.js comme suit :

Plus d'exemples réels à venir bientôt…[Restez à l'écoute](https://goo.gl/u72j6u)…

### Mon avis sur cela

C'est excellent pour les codeurs qui sont familiers avec JavaScript et qui essaient de trouver leur chemin dans le monde ML/DL !

Cela simplifie beaucoup les choses pour les personnes venant d'un milieu non-ML/DL, mais qui cherchent à comprendre ce domaine. Les cas d'utilisation pour cela sont nombreux, et je pense personnellement que c'est quelque chose dont nous avons besoin en ce moment.

Dans mon prochain article et vidéo, je parlerai de [ML5](https://ml5js.org/) qui est construit sur TensorFlow.js. [ML5](https://ml5js.org/) est construit à l'Université de New York et est en développement actif.

Que pensez-vous de TensorFlow.js ? Faites-le moi savoir dans la section des commentaires ci-dessous. Si vous aimez cet article, vous aimerez aussi mes [Vidéos sur Youtube.](https://goo.gl/u72j6u)

Si vous avez aimé mon article, **veuillez cliquer sur le ? ci-dessous A**nd suivez-moi sur M**edium** & :

![Image](https://cdn-media-1.freecodecamp.org/images/1*z8B3R6kZjTkMKPv3MnUYxg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*-etmF1WRWkvWO6cSol7f1w.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*7DWddirTA0TDNoAL34xjag.png)

Si vous avez des questions, n'hésitez pas à me le faire savoir dans un commentaire ci-dessous ou sur [**Twitter**](https://twitter.com/I_AM_ADL).