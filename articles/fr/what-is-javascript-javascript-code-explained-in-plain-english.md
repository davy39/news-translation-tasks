---
title: Qu'est-ce que JavaScript ? Le code JavaScript expliqué en anglais simple
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-08-25T15:44:41.000Z'
originalURL: https://freecodecamp.org/news/what-is-javascript-javascript-code-explained-in-plain-english
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/lagos-techie-tWjzmNXKup4-unsplash.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce que JavaScript ? Le code JavaScript expliqué en anglais simple
seo_desc: "JavaScript was created over 26 years ago and is currently one of the most\
  \ popular programming languages. But what is JavaScript? \nJavaScript is used with\
  \ HTML and CSS to create dynamic and interactive web pages and mobile applications.\
  \ We often call ..."
---

JavaScript a été créé il y a plus de 26 ans et est actuellement l'un des langages de programmation les plus populaires. Mais qu'est-ce que JavaScript ?

JavaScript est utilisé avec HTML et CSS pour créer des pages web et des applications mobiles dynamiques et interactives. Nous l'appelons souvent l'un des piliers du [développement web](https://www.freecodecamp.org/news/what-is-web-development-how-to-become-a-web-developer-career-path/).

Selon [W3Techs](https://w3techs.com/technologies/details/cp-javascript/),

> JavaScript est utilisé comme langage de programmation côté client par 97,6 % de tous les sites web.

## Histoire de JavaScript

En 1995, le développeur de Netscape, Brendan Eich, a créé la première version de JavaScript en seulement 10 jours. À sa sortie, il s'appelait Mocha, puis a été changé en LiveScript et a finalement été nommé JavaScript.

Les patrons de Brendan Eich voulaient que JavaScript ait une syntaxe similaire à celle de Java. Ils pensaient également que JavaScript allait aider à accélérer le développement web et être plus facile à apprendre par rapport à Java.

Au fil des ans, JavaScript a évolué et s'est développé en un langage polyvalent qui peut être utilisé sur le web et les applications mobiles.

## Qu'est-ce qu'ECMAScript ?

ECMAScript signifie European Computer Manufacturers Association Script. Selon la [documentation MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Language_Resources),

> **ECMAScript** est le langage de script qui forme la base de JavaScript.

L'association a créé la norme ECMA pour s'assurer que les pages web étaient cohérentes entre les différents navigateurs. En août 2021, il y a un total de 12 versions publiées d'ECMAScript.

## Java est-il identique à JavaScript ?

Même si ces deux langages ont une syntaxe similaire et partagent les quatre premières lettres de "Java", ils ne sont pas le même langage.

Voici quelques différences clés entre les deux langages.

* Java est un langage de programmation compilé. Cela signifie qu'avant l'exécution du programme, le code doit être traduit en code machine pour que l'ordinateur puisse le comprendre.
* JavaScript est un langage interprété. Dans le navigateur, un interpréteur lira le code et l'exécutera sans avoir besoin de le compiler au préalable.
* Java est utilisé comme langage côté serveur (backend) alors que JavaScript est principalement utilisé comme langage côté client (frontend). Mais JavaScript peut également être utilisé pour créer des applications web backend avec Node.js.

## Comment HTML, CSS et JavaScript fonctionnent-ils ensemble sur une page web ?

Maintenant que nous avons appris l'histoire de JavaScript, nous devons comprendre comment il fonctionne sur un site web.

HTML rend le contenu, CSS style la page pour la rendre attrayante, et JavaScript rend le site interactif. Mais que signifie interactif et comment JavaScript fonctionne-t-il avec les deux autres langages ?

Prenons un exemple pour mieux comprendre comment les trois langages fonctionnent ensemble.

Dans cet exemple, lorsque l'utilisateur clique sur un bouton, un message s'affichera avec le nombre de fois où l'utilisateur a cliqué. Lorsque le compte atteint un certain seuil, le message changera et deviendra plus sarcastique à mesure que le compte augmente.

%[https://codepen.io/jessica-wilkins/pen/xxrxwVp]

Nous utilisons HTML pour créer et afficher le bouton sur la page.

```html
<button id="btn">Cliquez-moi</button>
```

Nous avons également cet élément `p` dans notre HTML qui n'a aucun texte entre les balises d'ouverture et de fermeture. En JavaScript, le texte est ajouté une fois que l'utilisateur clique sur le bouton.

```html
<p id="para"></p>
```

Nous utilisons CSS pour styliser le bouton et le centrer sur la page.

```css
button {
  display: block;
  margin: 20px auto 10px;
  padding: 25px 20px;
  font-size: 1.4rem;
  cursor: pointer;
  border: none;
  border-radius: 50%;
  background-color: #3b5998;
  color: white;
}
```

Afin d'accéder aux éléments HTML, nous utilisons `getElementById`. C'est là que notre JavaScript intervient.

```js
const btn = document.getElementById("btn");
const para = document.getElementById("para");
```

La variable appelée `count` garde une trace du nombre de fois où l'utilisateur clique sur le bouton. Le compte est continuellement mis à jour chaque fois que le bouton est cliqué.

```js
let count = 0;
```

Ceci est le tableau des réponses qui seront affichées à l'utilisateur.

```js
const responsesArr = [
  "Vous avez cliqué sur le bouton ce nombre de fois : ",
  "Wow, vous aimez cliquer sur ce bouton. Nombre de clics sur le bouton : ",
  "Pourquoi continuez-vous à cliquer dessus ? Nombre de clics sur le bouton :",
  "Maintenant, vous êtes juste ennuyeux. Nombre de clics sur le bouton :"
];
```

Nous utilisons `addEventListener` qui indique à l'ordinateur d'écouter un événement de clic. Une fois le clic détecté, le message apparaîtra à l'écran avec le compte.

```js
btn.addEventListener("click", () => {
  count++;
  if (count < 10) {
    para.innerHTML = `${responsesArr[0]} ${count}`;
  } else if (count >= 10 && count < 15) {
    para.innerHTML = `${responsesArr[1]} ${count}`;
  } else if (count >= 15 && count < 20) {
    para.innerHTML = `${responsesArr[2]} ${count}`;
  } else {
    para.innerHTML = `${responsesArr[3]} ${count}`;
  }
});
```

Nous utilisons une instruction `if else` pour vérifier combien de fois le bouton a été cliqué et afficher un message différent en fonction de la hauteur du nombre de compte.

Si `count` est inférieur à 10, alors ce message est affiché à l'écran.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-24-at-4.26.30-PM.png)

Si `count` est entre 10 et 14, alors ce message est affiché à l'écran.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-24-at-4.27.27-PM.png)

Si `count` est entre 15 et 19, alors ce message est affiché à l'écran.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-24-at-4.28.57-PM.png)

Si `count` est 20 ou plus, alors ce message est affiché à l'écran.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-24-at-4.31.35-PM.png)

## Comment JavaScript fonctionne-t-il sur un site web réel ?

Nous venons de voir un exemple de base de la façon dont HTML, CSS et JavaScript fonctionnent ensemble. Mais comment JavaScript fonctionne-t-il sur des sites web réels ?

Prenons un exemple sur la [plateforme d'apprentissage de freeCodeCamp](https://www.freecodecamp.org/learn). Il s'agit d'un exemple de défi HTML du cours Responsive Web Design.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-24-at-4.44.19-PM.png)

Si je réussis le défi, ce message apparaîtra.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-24-at-4.45.51-PM.png)

Mais si ma réponse est incorrecte, le cours me dira où se trouve le problème.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-24-at-4.46.41-PM.png)

Mais comment freeCodeCamp sait-il si ma réponse est correcte ou non ?

freeCodeCamp écrit une série de tests pour chaque défi afin de s'assurer que le code est correct. Ces tests sont écrits en JavaScript.

Ce sont les tests JavaScript pour le défi [Ajouter des images à votre site web](https://www.freecodecamp.org/learn/responsive-web-design/basic-html-and-html5/add-images-to-your-website).

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-24-at-4.51.44-PM.png)

## Comment commencer à apprendre JavaScript

Voici une liste de ressources où vous pouvez commencer à apprendre JavaScript.

1. [Algorithmes et structures de données JavaScript](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/) (freeCodeCamp)
2. [Apprendre JavaScript - Cours complet pour débutants](https://www.youtube.com/watch?v=PkZNo7MFNFg) (chaîne YouTube freeCodeCamp)
3. [Le tutoriel moderne JavaScript](https://javascript.info/) (javascript.info)
4. [Tutoriel JavaScript](https://www.javascripttutorial.net/) (javascripttutorial.net)
5. [LearnJS](https://www.learn-js.org/) (learn-js.org)
6. [Apprendre JavaScript](https://www.codecademy.com/learn/introduction-to-javascript) (Codecademy)
7. [JavaScript](https://www.sololearn.com/learning/1024) (SoloLearn)
8. [MDN JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) (documentation web MDN)
9. [Tutoriel JavaScript pour débutants : Apprendre JavaScript en 1 heure](https://www.youtube.com/watch?v=W6NZfCO5SIk) (Programmation avec Mosh)

Une fois que vous avez appris les bases de JavaScript, vous pouvez commencer à construire vos propres projets. J'ai créé une liste de [40 projets JavaScript pour débutants](https://www.freecodecamp.org/news/javascript-projects-for-beginners/) pour vous aider à démarrer.

## Bibliothèques et frameworks JavaScript

Les bibliothèques et frameworks JavaScript ont été créés pour aider à accélérer le développement. Une fois que vous avez appris le "Vanilla" (ou JavaScript de base) JavaScript, vous pouvez commencer à apprendre une bibliothèque ou un framework.

Il existe de nombreuses options parmi lesquelles choisir, mais vous n'avez pas besoin de toutes les apprendre. Recherchez les offres d'emploi dans votre région pour voir quelles bibliothèques et frameworks sont utilisés.

Voici quelques options populaires.

* [React](https://reactjs.org/)
* [Angular](https://angular.io/)
* [Vue](https://vuejs.org/)

Voici quelques ressources d'apprentissage suggérées.

* [Cours YouTube React de freeCodeCamp](https://www.youtube.com/watch?v=nTeuhbP7wdE)
* [Cours YouTube Angular de Brad Traversy](https://www.youtube.com/watch?v=Fdf5aTYRW0E)
* [Cours YouTube Vue de Brad Traversy](https://www.youtube.com/watch?v=qZXt1Aom3Cs)

## Conclusion

JavaScript a été créé pour la première fois en 1995 et est depuis devenu un langage puissant et polyvalent utilisé pour les sites web, les jeux en ligne et les applications mobiles.

Même si Java et JavaScript ont une syntaxe similaire et partagent les quatre premières lettres de "Java", ils ne sont pas le même langage. Java est principalement utilisé comme langage côté serveur alors que JavaScript est utilisé dans le navigateur.

HTML, CSS et JavaScript sont les trois langages de base du web. HTML est pour le contenu, CSS est pour le style, et JavaScript est pour l'interactivité sur le site.

J'espère que vous avez trouvé cet article utile et je vous souhaite bonne chance dans votre parcours de développeur web.