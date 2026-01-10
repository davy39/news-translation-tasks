---
title: Introduction d'un poète au développement web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-15T16:00:00.000Z'
originalURL: https://freecodecamp.org/news/a-poets-introduction-to-web-development
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca172740569d1a4ca4ea0.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: learning to code
  slug: learning-to-code
- name: Web Development
  slug: web-development
seo_title: Introduction d'un poète au développement web
seo_desc: 'By Usheninte Dangana

  I honestly feel that coding is the best thing, after baked bread. The freedom it
  offers - financial and otherwise - is a high motivator, and gives the welcoming
  feeling that makes most people choose to learn to code.

  Let''s get to...'
---

Par Usheninte Dangana

Je pense honnêtement que le codage est la meilleure chose, après le pain cuit au four. La liberté qu'il offre - financière et autre - est un grand motivateur, et donne cette sensation d'accueil qui pousse la plupart des gens à choisir d'apprendre à coder.

Commençons.

---

### Qu'est-ce que le développement web ?

Pour la plupart des gens, cela implique le développement web statique, avec **HTML**, **CSS** et **JavaScript**. Cela signifie généralement le développement web sans le surcoût des bibliothèques ou frameworks UI comme React, Angular ou Vue.

Alors, qu'est-ce qui compose un site web ? Généralement, le tableau ci-dessous l'explique de manière simple :

Éléments | Utilisation
---|---
HTML | Structure
CSS | Style
JS | Interactivité

HTML signifie **HyperText Markup Language** et est responsable de la structure des sites web. Pensez-y comme une sorte de squelette.

CSS signifie **Cascading StyleSheets**, et effectue la majeure partie du travail de style et de design qui entre dans les sites web. CSS ajoute un élément esthétique supplémentaire au développement web, et donne cet élément essentiel d'assaisonnement au plat qu'est un site web. Pensez-y comme une sorte de peau.

JS signifie **JavaScript**, et cela ajoute la couche d'interactivité essentielle à tout sur le web. Pensez-y comme les nerfs d'un site web. JavaScript fait rebondir les choses, les fait tournoyer et faire d'autres choses amusantes. C'est une grande litote - cependant, vous voyez le tableau. ?

Voici une page web basique qui contient tous les éléments ci-dessus. Cependant, cela est loin d'être de qualité production.

```html
<!-- HTML -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Introduction Web des Poètes</title>

  <!-- CSS -->
  <style>
    h1 {
      color: #3cb271;
    }
  </style>
  <!-- Fin du CSS -->

</head>
<body>

  <h1>Bonjour :)</h1>

  <p></p>
  
  <!-- JavaScript -->
  <script>
    var text = document.querySelector("p");

    text.innerHTML = "Bonjour Lecteurs !";
  </script>
  <!-- Fin du JavaScript -->

</body>
</html>
<!-- Fin du HTML -->
```

Ici, le style est intégré et attaché à la section head du document HTML. La section `<head></head>` d'un document HTML contient les informations les plus importantes concernant un site web.

La section suivante `<body></body>` contient des informations qui seront affichées dans la fenêtre du navigateur. Dans ce cas, une simple balise `<h1>` (ou élément **header 1**) qui montre aux utilisateurs un grand message de bienvenue.

Voici une [démonstration en direct](https://codepen.io/usheninte/full/KjxJVb) du code ci-dessus.

Le CSS intégré ne fait pas grand-chose ici. Il ne change que la couleur de l'élément `h1` en une nuance de vert :

![Image](https://www.freecodecamp.org/news/content/images/2019/07/3cb271---green.png)
_#3cb271 - VERT_



Si vous regardez le code, il y a une balise de paragraphe vide. Il s'agit de la balise d'ouverture et de fermeture `<p></p>`, qui n'a rien entre les deux. Pourtant, le texte "**Bonjour Lecteurs !**" peut être vu dans la fenêtre du navigateur de démonstration. Il s'agit d'une petite démonstration de la puissance de JavaScript.

La balise de paragraphe a d'abord été ciblée avec `document.querySelector("p")`, qui a sélectionné l'élément dans le document HTML, avec la balise `<p>`. Elle a ensuite été enregistrée dans une variable avec `var text`, le **deuxième mot** ici étant le **nom de la variable**.

La deuxième ligne dans la balise `<script></script>`, où le JavaScript réside dans ce document HTML, fait quelque chose de beau. Elle cible la variable nouvellement créée `text` en utilisant la propriété DOM HTML de **innerHTML**, avec la ligne suivante :

```js
text.innerHTML = "Bonjour Lecteurs !";
```

Cela remplit ensuite la variable **text** avec le texte "**Bonjour Lecteurs !**", et ainsi, la balise `<p></p>` avec le même contenu textuel.

```js
var text = document.querySelector("p");

text.innerHTML = "Bonjour Lecteurs !";
```

---

### Le DOM - Document Object Model

![Image](https://www.freecodecamp.org/news/content/images/2019/07/html-dom.png)
_Source : ([https://www.w3schools.com/whatis/whatis_htmldom.asp](https://www.w3schools.com/whatis/whatis_htmldom.asp))_

Ce que nous avons fait dans l'exemple ci-dessus, c'est trouver un élément HTML dans le DOM et mettre à jour son contenu en utilisant Vanilla JS. Le JavaScript pur (ou _Vanilla JS_) est un terme utilisé pour désigner la syntaxe et les fonctionnalités naturelles de JavaScript sans aucune interférence de Framework ou de Bibliothèque.

Le **HTML DOM** fonctionne de deux manières - à la fois comme un **Modèle d'Objets** pour HTML et une **API** pour JavaScript. Il est généralement responsable de l'interactivité au sein des sites web.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/html-dom-2.png)
_Source : ([https://www.w3schools.com/whatis/whatis_htmldom.asp](https://www.w3schools.com/whatis/whatis_htmldom.asp))_

La manipulation du DOM est une partie importante du développement web, car elle aide les développeurs à créer des sites web plus dynamiques et visuellement attrayants.

---

J'espère que vous avez passé un bon moment à lire ceci. Il s'agit d'un aperçu très introductif du développement web. Vous pouvez suivre le programme [Responsive Web Design](https://learn.freecodecamp.org/) de **freeCodeCamp** pour avoir une meilleure compréhension des concepts de développement web.

> N'oubliez pas de faire quelques projets aussi ! ?