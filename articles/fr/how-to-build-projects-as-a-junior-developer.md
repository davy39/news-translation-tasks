---
title: Comment construire des projets réussis en tant que développeur junior
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2023-11-21T21:25:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-projects-as-a-junior-developer
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/scott-graham-5fNmWej4tAA-unsplash.jpg
tags:
- name: 'Junior developer '
  slug: junior-developer
- name: projects
  slug: projects
- name: Web Development
  slug: web-development
seo_title: Comment construire des projets réussis en tant que développeur junior
seo_desc: "Several months ago, I stumbled upon a coding challenge that intrigued me.\
  \ Here's what it was:\nhttps://twitter.com/hussien_coding/status/1576929379736727554\n\
  \ \nThe task was seemingly simple: build six squares with no color, make each square\
  \ turn green ..."
---

Il y a plusieurs mois, je suis tombé sur un défi de codage qui m'a intrigué. Le voici :

%[https://twitter.com/hussien_coding/status/1576929379736727554] 

La tâche semblait simple : construire six carrés sans couleur, faire en sorte que chaque carré devienne vert lorsqu'on clique dessus. Ensuite, lorsque le dernier carré devient vert, les faire tous revenir à leur état initial dans l'ordre inverse de celui dans lequel ils ont été cliqués.

J'étais enthousiaste à l'idée de tester les compétences de certains développeurs juniors avec lesquels je travaillais et qui débutaient dans le domaine de la technologie, alors je leur ai partagé le défi. Mais les résultats n'étaient pas ceux que j'attendais.

Malgré sa simplicité apparente, le défi a donné des résultats variés. Certains étudiants ont réussi à créer une solution fonctionnelle, tandis que d'autres ont eu du mal avec les concepts de programmation requis.

C'est alors que j'ai réalisé que cela pourrait être une grande opportunité pour beaucoup de gens. Donc, si vous êtes un développeur junior et que vous trouvez difficile de créer vos propres projets de portfolio/démo, ne craignez rien ! Cet article vous guidera à travers le processus de construction réussie d'un projet avec une approche simple.

## À qui s'adresse cet article ?

Cet article est spécialement conçu pour les développeurs juniors qui pourraient avoir du mal à créer leurs propres projets personnels.

Si vous vous retrouvez souvent à dépendre de tutoriels ou si vous avez l'impression de manquer de créativité pour créer des projets de manière indépendante, alors cet article est pour vous.

## Commencer

Examinons le défi que j'ai envoyé aux étudiants :

```plaintext
Construire six carrés sans couleur 
Chaque fois que vous cliquez sur l'un d'eux, il devient vert 
Lorsque le dernier carré devient vert, ils reviennent tous à leur état initial dans l'ordre inverse de celui dans lequel ils ont été cliqués (pas tous en même temps)
```

Si vous étiez l'un des étudiants confrontés à ce défi, que feriez-vous en premier ? Bien qu'il puisse être tentant de se lancer directement dans le codage, il est important de reconnaître que **l'écriture de code** est en fait **la dernière étape** de la construction d'un projet.

Alors, quelle est la première étape ? La première étape est de **réfléchir**. Oui, je veux dire littéralement s'arrêter et réfléchir au problème que vous essayez de résoudre.

## Comment réfléchir au problème

Lorsqu'on aborde un projet, il est important de le considérer comme un problème qui nécessite une solution. Prenez le temps de bien considérer le problème, puis décomposez-le en parties plus petites.

Pour ce faire, vous pourriez trouver utile de vous éloigner de votre ordinateur et de prendre un crayon et une feuille de papier.

Par exemple, face à un défi quelconque, vous pouvez commencer par décomposer le projet en parties plus faciles à gérer. Cela pourrait inclure :

1. Créer les six carrés
   
2. Déterminer un moyen de changer leur couleur lorsqu'on clique dessus
   
3. Créer un mécanisme pour suivre quels carrés ont été cliqués
   
4. Concevoir une méthode pour que les carrés reviennent à leur état initial dans l'ordre inverse de celui dans lequel ils ont été cliqués


Peu importe la taille d'un projet, il est toujours important de le décomposer en parties plus petites. Cela facilite la gestion de chaque pièce individuelle une à la fois tout en restant organisé et concentré.

Alors, face à un grand projet, ne vous laissez pas intimider. Au lieu de cela, prenez le temps de le décomposer en parties plus petites et concentrez-vous sur la gestion de chaque partie individuellement. En faisant cela, vous serez en mesure de rester organisé, concentré et finalement plus performant dans votre projet.

Après avoir pris le temps de bien considérer le défi, j'ai pu trouver une solution potentielle. Voici ce que j'ai imaginé :

```plaintext
// étape 1 : créer les six carrés

- CRÉER six boutons individuels en HTML 
- DONNER à chaque bouton un nom de classe "square" 
- LEUR DONNER des identifiants uniques

// étape 2 : Déterminer un moyen de changer leur couleur lorsqu'on clique dessus

- AJOUTER un écouteur d'événement CLICK à chaque bouton
- APPLER une fonction appelée UpdateSquares() qui change la couleur d'un bouton cliqué

// étape 3 : Créer un mécanisme pour suivre quels carrés ont été cliqués

- CRÉER un tableau appelé `array_sqr` qui stocke l'identifiant unique d'un bouton cliqué
- Lorsqu'un bouton a été cliqué, ajouter l'identifiant au tableau

// étape 4 : concevoir une méthode pour que les carrés reviennent à leur état initial dans l'ordre inverse de celui dans lequel ils ont été cliqués

- Lorsque `array_sqr.length == 6`, appeler une fonction appelée ReverseSquares()
- Dans la fonction ReverseSquares(), parcourir `array_sqr`
- À l'intérieur de la boucle, SÉLECTIONNER chaque bouton avec les identifiants uniques dans `array_sqr`
- RETIRER la couleur verte du bouton sélectionné
```

Après avoir bien réfléchi à votre projet, vous pouvez maintenant passer à l'étape suivante, qui consiste à construire réellement votre projet.

## Comment résoudre le problème et construire la solution

Après avoir bien considéré le défi, il est temps de passer à la construction du projet. Passons en revue les étapes :

### Étape 1 : Créer les six carrés

Dans cette étape, nous avons trois choses à faire : créer six boutons individuels en HTML, donner à chaque bouton le nom de classe "square", et leur donner des identifiants uniques.

Vous pouvez le faire en HTML comme ceci :

```html
<body>
    <div class="wrapper">
        <button class="square" id="1">
            Bouton 1
        </button>
        <button class="square" id="2">
            Bouton 2
        </button>
        <button class="square" id="3">
            Bouton 3
        </button>
        <button class="square" id="4">
            Bouton 4
        </button>
        <button class="square" id="5">
            Bouton 5
        </button>
        <button class="square" id="6">
            Bouton 6
        </button>
    </div>
</body>
<script src="script.js"></script>
```

Ci-dessus, nous avons simplement créé les boutons avec des identifiants uniques comme nous l'avons écrit.

### Étape 2 : Déterminer un moyen de changer leur couleur lorsqu'on clique dessus.

Dans cette étape, nous avons simplement deux tâches : AJOUTER un écouteur d'événement CLICK à chaque bouton, puis appeler une fonction appelée `UpdateSquares()` qui change la couleur d'un bouton cliqué.

Nous allons le faire en JavaScript, donc nous allons créer un nouveau fichier appelé `script.js` avec le code suivant :

```js
const buttons = document.querySelectorAll(".square");

for (const button of buttons) {
    button.addEventListener("click", UpdateSquares);
}

function UpdateSquares(event) {
    const btn = event.target;
    btn.style.backgroundColor = 'green';
    array_sqr.push(btn.id);
}
```

### Étape 3 : Créer un mécanisme pour suivre quels carrés ont été cliqués.

Dans l'étape suivante, nous devons créer un tableau vide appelé `array_sqr` qui stocke l'identifiant unique d'un bouton cliqué. Ensuite, lorsqu'un bouton a été cliqué, nous devons ajouter l'identifiant au tableau. En modifiant notre code pour atteindre l'objectif ci-dessus, nous avons ceci :

```js

let array_sqr = []; // créer le tableau vide

function UpdateSquares(event) {
    const btn = event.target;
    btn.style.backgroundColor = 'green';
    array_sqr.push(btn.id); // ajouter l'identifiant au tableau
}
```

Dans le code ci-dessus, tout ce que nous avons fait est de suivre la manière dont les boutons sont cliqués en les stockant dans un tableau.

### Étape 4 : Concevoir une méthode pour que les carrés reviennent à leur état initial dans l'ordre inverse de celui dans lequel ils ont été cliqués.

Dans cette dernière étape, nous devons appeler une fonction ReverseSquares() lorsque `array_sqr.length == 6`.

Dans la fonction `ReverseSquares()`, parcourir `array_sqr`. À l'intérieur de la boucle, sélectionner chaque bouton avec les identifiants uniques dans `array_sqr` et retirer la couleur verte du bouton sélectionné.

Voici le code pour faire cela :

```js
const buttons = document.querySelectorAll(".square");

for (const button of buttons) {
    button.addEventListener("click", UpdateSquares);
}

let array_sqr = [];

function UpdateSquares(event) {
    const btn = event.target;
    btn.style.backgroundColor = 'green';
    array_sqr.push(btn.id);

    if (array_sqr.length == 6) {
        ReverseSquares();
    }
}

function ReverseSquares() {
    array_sqr.reverse();

    for (const id of array_sqr) {
        const reverse_btn = document.getElementById(id);

        // Retirer la couleur 
        reverse_btn.style.backgroundColor = 'white';

        /* Vider également le tableau */
        array_sqr = [];
    }
}
```

Avec le code ci-dessus, nous avons pratiquement terminé le projet, et il fonctionne comme prévu. Jetez un œil à la démonstration ci-dessous :

%[https://codepen.io/Spruce_khalifa/pen/PoVReva] 

La seule chose restante à résoudre est que, pour le moment, toutes les couleurs sont retirées en même temps. Nous devons donc résoudre ce problème, ce qui nous mènera au dernier aspect de la construction de notre projet.

## Comment améliorer la solution

Notre projet a actuellement un problème où la couleur est retirée de tous les carrés en même temps. Nous devons donc corriger cela.

Chaque projet doit subir cette étape cruciale de mises à jour et de corrections. Il est très difficile de construire un projet parfait du premier coup. Je n'ai même pas construit la démonstration de ce tutoriel du premier coup.

Améliorer votre projet peut parfois être encore plus difficile que de construire le projet lui-même. Fait amusant : il m'a fallu plus de temps pour faire en sorte que les couleurs changent à des intervalles différents que pour écrire le code de la démonstration que j'ai utilisée dans ce tutoriel.

Cette étape implique généralement beaucoup de recherches sur Google et parfois même demander de l'aide aux autres. C'est tout à fait acceptable de le faire – cela ne fait pas de vous un mauvais développeur.

Maintenant que nous avons clarifié cela, améliorons notre projet. Tout ce que nous avons à faire est de modifier la fonction `ReverseSquares()` comme suit :

```js
function ReverseSquares() {
    array_sqr.reverse();
    // Utiliser une boucle for..of pour appliquer des délais différents pour chaque bouton
    for (const [index, id] of array_sqr.entries()) {
        const reverse_btn = document.getElementById(id);

        // Retirer la couleur après un délai, avec un délai croissant pour chaque bouton
        setTimeout(() => {
            reverse_btn.style.backgroundColor = 'white';
        }, index * 1000);

        /* Vider également le tableau */
        array_sqr = [];
    }
}
```

Lorsque tout est assemblé, vous avez une solution qui fonctionne. Elle n'est peut-être pas parfaite, mais elle fonctionne – et c'est une victoire.

%[https://codepen.io/Spruce_khalifa/pen/qBgoYer] 

## Résumé

Créer des projets personnels en tant que développeur junior peut sembler difficile. Mais en suivant une approche systématique de réflexion, de planification de votre code, de codage réel, puis d'amélioration de votre solution, vous pouvez construire avec succès des projets qui mettent en valeur vos compétences et votre créativité.

N'ayez pas peur de décomposer les grands projets en parties plus petites et plus faciles à gérer. Et n'oubliez pas que l'amélioration est une partie intégrale du processus de développement.

Si vous avez des questions, n'hésitez pas à m'envoyer un message sur Twitter à l'adresse [@sprucekhalifa](https://twitter.com/sprucekhalifa), et n'oubliez pas de me suivre pour plus d'informations et de mises à jour. Bon codage !

Photo par [Scott Graham](https://unsplash.com/@homajob?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) sur [Unsplash](https://unsplash.com/photos/person-holding-pencil-near-laptop-computer-5fNmWej4tAA?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)