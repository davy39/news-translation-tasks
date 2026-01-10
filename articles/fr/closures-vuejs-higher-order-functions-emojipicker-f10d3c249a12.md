---
title: Découvrez la puissance des closures dans VueJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-24T21:32:00.000Z'
originalURL: https://freecodecamp.org/news/closures-vuejs-higher-order-functions-emojipicker-f10d3c249a12
coverImage: https://s3.amazonaws.com/cdn-media-1.freecodecamp.org/ghost/2019/05/1_pc1Xhd_TAV9H8u8b-ogLPw.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
seo_title: Découvrez la puissance des closures dans VueJS
seo_desc: 'By Fabian Hinsenkamp

  Today’s frontend technology landscape requires engineers to know about a wide variety
  of technologies including frameworks, libraries and packages.

  No wonder then that vanilla JavaScript skills and in-depth knowledge might start
  ...'
---

Par Fabian Hinsenkamp

Le paysage technologique actuel du frontend exige des ingénieurs qu'ils maîtrisent une grande variété de technologies, y compris des frameworks, des bibliothèques et des packages.

Il n'est donc pas surprenant que les compétences en JavaScript vanilla et les connaissances approfondies commencent à s'amincir. Que vous appreniez JavaScript, que vous rafraîchissiez vos connaissances de base ou que vous vous prépariez pour des entretiens d'embauche → Ce tutoriel est pour vous !

Ici, vous apprendrez à quel point les closures en JavaScript pur sont puissantes. Attention, ce tutoriel vient avec un défi. ? Il s'agit de construire un élégant sélecteur d'emojis en VueJS et de tirer parti des closures en utilisant des fonctions d'ordre supérieur.

**Plongeons directement dans le vif du sujet !**

### Portée des fonctions

Bien que les closures soient l'un des concepts les plus puissants en JavaScript, elles sont souvent négligées par beaucoup.

Néanmoins, connaître les closures est fondamental car elles définissent quelles variables une fonction peut accéder pendant son exécution. Plus précisément, les closures définissent quels sont les champs d'application auxquels une fonction a accès, en commençant par le sien, à travers tous les champs d'application parents jusqu'au champ d'application global.

Pour vraiment maîtriser les closures, il est essentiel d'avoir une solide compréhension des portées. Vous avez probablement déjà expérimenté l'impact des portées vous-même. Chaque fois que vous exécutez une fonction, une portée est créée. Chaque fois que vous créez des variables dans cette fonction, celles-ci ne sont accessibles que depuis la fonction elle-même.

Au moment où une fonction est terminée (en atteignant une instruction `return` ou `}`), toutes ces variables sont détruites. La prochaine fois que vous exécutez la fonction, la même procédure est appliquée.

Regardons l'exemple suivant pour illustrer le concept.

```
function square(x){
  const squaredX = x * x;
  console.log(squaredX); // 25
  return squaredX;
}

const squaredA = square(5);

console.log(squaredA); // 25 
console.log(squaredX); // ReferenceError: squaredX is not defined
```

Pensez aux portées comme au contexte temporaire auquel seul le code de cette fonction a accès.

Alors que les portées ont une durée de vie très limitée, limitée par le temps nécessaire à l'exécution d'une fonction, en revanche, la fermeture d'une fonction est déjà créée lorsque la fonction est initialement définie. Elle subsistera également après la fin de l'exécution.

### Closures

Comme mentionné précédemment, les closures sont responsables de la définition des variables accessibles dans la portée d'une exécution de fonction. Il est essentiel de comprendre que les closures ne fournissent pas de copies des variables disponibles, mais des références à celles-ci. Si vous n'êtes pas familier avec les références de JavaScript, consultez cet [article](https://codeburst.io/explaining-value-vs-reference-in-javascript-647a975e12a0).

```
let globalString = 'A'

function hello(){
  const localString = 'C'
  console.log(globalString, localString);
}

hello(); // A C

globalString = "B";

hello(); // B C
```

L'exemple semble probablement très familier — ce n'est rien de spécial. Cela explique pourquoi nous réalisons à peine à quel point les closures peuvent être puissantes, car il est très courant de ne définir des fonctions que dans la portée globale.

Cependant, lorsque des fonctions sont définies dans la portée d'une autre fonction, les closures permettent des techniques et des motifs puissants. Dans une architecture orientée objet, les closures offrent un moyen simple mais efficace d'établir la **confidentialité des données**. Dans des architectures plus fonctionnelles, les closures sont essentielles aux **fonctions d'ordre supérieur** et à l'**application partielle** et au **currying**, deux techniques de programmation plus avancées.

### Fonctions d'ordre supérieur

Une fonction qui opère sur d'autres fonctions, soit en les prenant comme arguments, soit en les retournant, est appelée une **fonction d'ordre supérieur**.

```
function createMultiplier(multiplier){
  return function(value){
    return value * multiplier;
  }
}

const multiplyBy2 = createMultiplier(2);

console.log(multiplyBy2(5)); //10
```

Ici, nous pouvons enfin expérimenter la puissance des closures. Même si `createMultiplier` a déjà été exécuté avec succès, nous pouvons toujours accéder à sa propriété initiale `multiplier`.

Cela est possible car les closures conservent la référence des variables. Celles-ci peuvent même s'étendre sur plusieurs portées et ne sont pas détruites lorsque le contexte se termine. De cette manière, nous pouvons toujours accéder à une instance spécifique d'une variable locale.

### Confidentialité des données

```
function privateVariables(){
  let privateValue = 100;
  return {
    get: function(){
      return privateValue;
    }
  }
}

console.log(privateVariables().get()); //100
```

Comment les closures nous permettent-elles de mettre en œuvre la confidentialité des données ?

Nous pouvons simplement enfermer des variables et n'autoriser que les fonctions dans la portée de la fonction conteneur (externe) à y accéder.

Vous ne pouvez pas accéder aux données depuis une portée externe sauf par les méthodes privilégiées de l'objet. Ce modèle nous permet également de programmer selon une interface et non selon l'implémentation elle-même.

### Défi de codage : Sélecteur de tons d'emojis

![Image](https://cdn-media-1.freecodecamp.org/images/0*WbJiwUu1oJnUM-GY.png)

Super, c'est toute la théorie dont nous avons besoin pour construire quelque chose de puissant dans VueJS et tirer parti de la puissance des closures !

En fait, les fonctions d'ordre supérieur sont le cas d'utilisation le plus intéressant, car nous avons déjà un concept de confidentialité des données dans VueJS.

En gros, les composants offrent déjà une interface à travers les propriétés et l'objet de données qui n'est pas accessible de l'extérieur.

Il s'agit d'un composant qui permet à l'utilisateur de choisir le ton de la peau en fonction d'une sélection de tous les tons disponibles, similaire à l'expérience utilisateur connue pour envoyer des SMS sur un smartphone.

Techniquement, vous devriez essayer de créer un composant qui reçoit un seul emoji en tant que props et utilise des fonctions d'ordre supérieur pour créer plusieurs gestionnaires d'événements de clic afin de sélectionner différents tons.

Vous pouvez consulter le [bac à sable](https://codesandbox.io/s/pw940vx207?fontsize=14) pour le code !

### Indice

Les emojis peuvent être stockés sous forme de codes hexadécimaux HTML dans des valeurs de chaîne. L'emoji des mains jointes est &#x1F64F. Pour changer le ton, attachez un code de couleur à celui-ci. Vous pouvez trouver les codes [ici](https://emojiterra.com/folded-hands/).

> _&#x1F64F + &#x1F3FD = ??_

### Extension du défi de construction

Vous voulez aller plus loin et vraiment voir si vous maîtrisez les closures ? Alors passez plusieurs emojis et faites en sorte que vous puissiez changer le ton de la peau de plusieurs emojis un à la fois. ?

### Conclusion

Les closures sont la raison pour laquelle nous pouvons accéder aux variables des portées parentales alors que les fonctions associées peuvent avoir déjà terminé.

Nous pouvons utiliser ce comportement de JavaScript dans VueJS pour construire dynamiquement des méthodes basées sur des arguments dynamiques sans polluer nos composants avec une grande variété de variables et de méthodes.

Merci d'avoir lu ?

---

Publié à l'origine sur mon blog à l'adresse [https://hinsencamp.com](https://hinsencamp.com/article/closures-vue/).