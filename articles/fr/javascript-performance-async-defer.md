---
title: Performances JavaScript – Comment améliorer la vitesse de chargement des pages
  avec async et defer
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2023-01-10T18:18:31.000Z'
originalURL: https://freecodecamp.org/news/javascript-performance-async-defer
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/freeCodeCamp-Cover.png
tags:
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: performance
  slug: performance
- name: web performance
  slug: web-performance
seo_title: Performances JavaScript – Comment améliorer la vitesse de chargement des
  pages avec async et defer
seo_desc: 'In web programming, JavaScript brings interactiveness and dynamic behaviour
  to your web pages. While HTML and CSS take care of the structure and aesthetics
  of the pages, they will be merely usable without JavaScript doing its job in the
  background.

  Y...'
---

En programmation web, JavaScript apporte de l'interactivité et un comportement dynamique à vos pages web. Alors que HTML et CSS s'occupent de la structure et de l'esthétique des pages, elles ne seront que peu utilisables sans JavaScript qui fait son travail en arrière-plan.

Vous pouvez inclure du code JavaScript dans le fichier HTML de plusieurs manières. L'approche la plus standard consiste à garder le code JavaScript dans un fichier séparé avec l'extension `.js`, puis à charger ce fichier dans le fichier HTML pour que le script soit téléchargé et exécuté.

Dans cet article, vous apprendrez la manière la plus efficace de charger un fichier JavaScript dans HTML pour améliorer la vitesse de chargement des pages de l'application. Nous allons approfondir la compréhension visuelle de deux attributs HTML spéciaux, `async` et `defer`, et comment ils aident à améliorer le chargement des pages.

Si vous aimez apprendre à partir de contenu vidéo, cet article est également disponible sous forme de tutoriel vidéo ici : 👂

%[https://www.youtube.com/watch?v=4sBfx3ISBdM]

## Comment chargeons-nous les scripts dans HTML ?

Commençons par comprendre les bases du chargement du code JavaScript à partir d'un fichier externe. Supposons que nous avons un fichier appelé `some-script.js` (notez l'extension du fichier. C'est .js qui signifie JavaScript) avec tout le code JavaScript.

Vous devez utiliser la balise `<script>` pour charger et exécuter ce code. L'attribut `src` de la balise <script> pointe vers le fichier JavaScript que vous souhaitez charger.

```html
<script src="some-script.js"></script>  
```

Enfin, vous devez vous assurer de placer la balise <script> soit à l'intérieur de la balise `<head>`, soit à la fin de la balise `<body>` du fichier HTML.

```html

<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Some Title</title>
  <link rel="stylesheet" href="./styles/main.css">

  <script src="some-script.js"></script>  
</head>
<body>

</body>
</html>
```

Spécifier la balise `<script>` à l'intérieur des balises `<head>` ou `<body>` a ses propres conséquences. Nous allons en apprendre davantage à leur sujet sous peu.

## Pourquoi se soucier du chargement des scripts ?

Si votre application est minuscule et traite des fichiers de script de quelques Ko, vous vous soucierez peu de la vitesse de la page et du chargement des scripts. 

Mais vous pouvez traiter des scripts plus volumineux écrits par une bibliothèque tierce ou par vous-même dans la vie réelle. Vous devez vous assurer que la vitesse de chargement de la page n'est pas dégradée à cause de cela.

Mais attendez ! Comment le fichier de script plus volumineux dégrade-t-il la vitesse de chargement de la page ? Comprenons avec la démonstration d'une application simple appelée `The Secret Santa Game`.

### Le jeu Secret Santa – Démo de la vitesse de la page

`Secret Santa Game` est un jeu simple qui sélectionne un Santa, un enfant et le cadeau que Santa doit donner à l'enfant. Chaque fois que vous cliquez sur le bouton `Play`, un nouveau Santa, un nouvel enfant et un nouveau cadeau sont sélectionnés.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screen-Recording-2023-01-05-at-5.14.51-PM.gif)
_Le jeu Secret Santa_

Le fichier HTML d'entrée crée la structure pour afficher l'image du cadeau et les noms de Santa et de l'enfant. Il comporte un bouton avec le texte `Play` et un pied de page où nous affichons un texte de copyright.

```html
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Secret Santa - V1</title>
  <link rel="stylesheet" href="./styles/main.css">

  <script src="./js/script-1.js"></script>
  <script src="./js/script-2.js"></script>
  <script src="./js/script-3.js"></script>
  
</head>
<body>
  <div class="container">
    <header>
      <h1>Secret Santa Game</h1>
    </header>
    <div class="content">
      <p id="gift-id" class="gift"></p>
      <p style="font-size: 3rem;"> 🎅 
          <strong>Santa</strong>: <span id="santa-id"></span>
      </p>
      <p style="font-size: 3rem;"> 👶 
          <strong>Child</strong>: <span id="child-id"></span>
      </p>
      <button class="play-btn" onclick="init()">Play</button>
    </div>
    <footer id="footer-id"></footer>
  </div>
</body>
</html>
```

Regardez la section `<head>` du fichier HTML. Nous chargeons trois scripts ici.

**script-1.js** : Ce fichier contient le code JavaScript responsable des mises à jour du DOM. La méthode `init()` sélectionne des valeurs aléatoires de participants et de cadeaux à rendre sur les nœuds DOM. La même méthode init est appelée lors du clic sur le bouton `Play`.

```js
const gifts = [
  'hoodie',
  'moon-light',
  'perfumes',
  'watch',
  'studio-light'
];

const participants = [
  'Alex',
  'Bob',
  'Carl',
  'Dell',
  'Emle'
];

const getRandomElem = arr => {
  return arr[Math.floor(Math.random()*arr.length)];
}

const init = () => {
  const giftElem = document.getElementById('gift-id');
  const childElem = document.getElementById('child-id');
  const santaElem = document.getElementById('santa-id');

  const child = getRandomElem(participants);
  const santa = getRandomElem(participants.filter(
      elem => elem !== child));
  const gift = getRandomElem(gifts);

  console.log(`${santa} to give ${gift} to ${child}`);

  childElem.innerText = '';
  childElem.innerText = child;
  santaElem.innerText = ''
  santaElem.innerText = santa;

  giftElem.innerHTML = '';
  const img = document.createElement('img');
  img.src = `./gift-images/${gift}.png`;
  img.alt = gift;
  img.width = '300';
  img.height = '300';
  giftElem.appendChild(img);
};

init();
```

**script-2.js** : Ce fichier JavaScript contient une petite quantité de code pour définir un texte de copyright dans l'élément de pied de page.

```js

const addToFooter = () => {
  const footerElem = document.getElementById('footer-id');
  footerElem.innerText = `CopyRight ${new Date().getFullYear()} @tapasadhikary`;
}

addToFooter();
```

**script-3.js** : Le dernier fichier JavaScript contient du code qui ne manipule pas le DOM mais apporte des fonctionnalités supplémentaires à l'application, comme des blocs publicitaires, des outils d'analyse, des chatbots, etc.

En résumé, nous avons deux scripts qui manipulent le DOM, et un qui est très petit. Le troisième ne manipule pas le DOM et apporte des fonctionnalités indépendantes à l'application.

### Le problème avec le chargement d'un fichier JavaScript dans le <head>

Alors, que se passe-t-il lorsque nous chargeons ces scripts dans la section `<head>` du fichier HTML, comme nous l'avons vu ci-dessus ? Malheureusement, nous ne verrons aucune valeur définie pour le DOM, ce qui rend la page incomplète.

Regardez l'image ci-dessous qui montre clairement les erreurs de recherche des éléments DOM comme `null` à partir de `script-1.js` et `script.js`. De plus, nous ne voyons pas l'image du cadeau et les noms des participants (Santa et l'enfant).

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-18.png)
_Erreur de rendu_

Cela se produit parce que le DOM n'était pas prêt lorsque les scripts ont été téléchargés et exécutés. 

Le navigateur analysera le document HTML de haut en bas. Lorsqu'il rencontre les scripts dans la section `<head>`, le reste de la création des éléments DOM sera mis en pause pour que les scripts soient téléchargés et exécutés. Une fois terminé, le reste du HTML sera traité pour créer les éléments DOM.

### La solution temporaire – déplacer dans le body

Alors, comment corriger ce problème ? Une solution évidente mais pas très bonne consiste à déplacer le téléchargement et l'exécution du script à la fin de la balise `<body>`. Cela garantira que tous les éléments DOM sont construits et prêts avant que nous téléchargions et exécutions les scripts. 

Devinez quoi ? L'application fonctionne cette fois sans aucune erreur.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-19.png)
_La solution temporaire a fonctionné_

Mais pourquoi est-ce une solution temporaire ? L'interactivité et le rendu des données attendent beaucoup plus longtemps, même après la construction du DOM. Beaucoup de nos utilisateurs n'utilisent peut-être pas un réseau haut débit 4G/5G. Un script volumineux prendra beaucoup de temps à télécharger et à exécuter. Le temps de téléchargement peut devenir si long que les utilisateurs finaux peuvent s'impatienter et décider d'arrêter d'utiliser l'application.

L'image ci-dessous montre un temps de chargement plus long lorsque nous exécutons la même application avec une limitation de réseau (simulation de réseau 3G) et la désactivation du cache. Comme vous pouvez le voir, le contenu du DOM a été chargé bien avant que le chargement final ne se produise.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-20.png)

Voici une information pour vous. Vous pouvez utiliser les outils de développement du navigateur pour simuler comment votre application peut se charger sur un réseau plus lent. Tous nos utilisateurs n'ont pas le réseau 4G/5G. Veuillez consulter ce tweet pour plus de détails.

%[https://twitter.com/tapasadhikary/status/1606205278969630720]

### Comprendre le problème visuellement

D'accord, comprenons maintenant ces deux situations visuellement. Une image vaut mille mots, après tout. L'image ci-dessous montre les deux situations de chargement des fichiers de script dans la balise `<header>` et à la fin de la balise `<body>`.

Dans le premier cas, nous voyons que la construction du DOM est mise en pause parce que les scripts étaient en cours de téléchargement et d'exécution. Une fois terminé, la construction du DOM reprend et se termine. Il est donc évident que, lorsque le navigateur exécutait les scripts, une bonne partie des éléments DOM n'étaient pas créés pour leur attribuer des valeurs.

Dans l'autre cas, où nous chargeons les scripts à la fin de la balise `<body>`, les éléments DOM sont entièrement prêts. À la fin, le navigateur télécharge et exécute les scripts. 

Tout a fonctionné cette fois parce que lorsque le script a été exécuté, le DOM était prêt à mettre à jour le contenu. Le temps total nécessaire pour que la page devienne entièrement opérationnelle est déterminé par le moment où les scripts sont téléchargés et exécutés à la fin.

Dans les deux cas, la séquence des scripts spécifiée est importante. Les scripts seront téléchargés et exécutés dans la même séquence spécifiée dans le document HTML.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/flow-1.png)
_Script dans Head vs Body_

## Qu'est-ce que l'attribut `async` et comment aide-t-il au chargement de la page ?

L'attribut `async` de la balise `<script>` garantit que les autres téléchargements de scripts n'attendent pas qu'un script async soit téléchargé et vice versa. Le navigateur ne bloque pas non plus la création du contenu DOM lorsqu'il rencontre le script async. Les scripts async sont téléchargés en arrière-plan et exécutés une fois terminés.

Les scripts async s'exécutent dans l'ordre `load-first`. Même si un script async plus petit est spécifié plus bas dans l'ordre dans le fichier HTML, il peut s'exécuter avant tous les autres scripts. 

Vous devez être prudent lorsque vous spécifiez l'attribut `async` à un script qui effectue une manipulation du DOM. Expérimentons un scénario délicat en utilisant notre `Secret Santa Game` !

Ajoutons l'attribut `async` à tous nos scripts sans changer leur ordre de placement dans le `<head>` du document HTML. Rappelez-vous, `script-1.js` et `script-2.js` manipulent tous deux le contenu du DOM, et `script-2.js` est plus petit en taille. `script-3` est un autre petit script qui ne manipule pas le DOM.

```js
<script async src="./js/script-1.js"></script>
<script async src="./js/script-2.js"></script>
<script async src="./js/script-3.js"></script>
```

Maintenant, lorsque vous exécutez l'application sur un réseau lent, vous pouvez voir que la séquence de chargement des scripts a changé. `script-2`, qui est petit en taille, est téléchargé en premier et s'exécute, puis `script-3`, et enfin `script-1`. Donc, leur ordre dans le document HTML n'a pas d'importance ici.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-21.png)

C'est précisément ce qui s'est passé avec notre application. L'avis de copyright sous le bouton `Play` ne s'affiche pas. Nous apprenons de l'erreur que l'élément `footer` n'était pas disponible dans le DOM pour que le script ajoute les textes souhaités.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-22.png)

Maintenant, examinons le téléchargement et l'exécution du script avec l'attribut `async`. 

Comme vous pouvez le voir, le navigateur ne mettra pas en pause pendant que le script est téléchargé. Le script commence à s'exécuter immédiatement après son téléchargement. Il n'y a aucune garantie que le DOM pertinent soit chargé dans le navigateur lorsqu'un script async s'exécute.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/flow-3.png)
_Introduction de l'attribut async_

En résumé, n'utilisez pas l'attribut `async` avec des scripts qui manipulent le DOM. Utilisez `async` avec des scripts externes à l'application qui ne manipulent pas le DOM. Les scripts comme les bibliothèques, les chatbots, les outils d'analyse, etc., sont des cas appropriés où vous devez envisager d'utiliser l'attribut `async`.

## Qu'est-ce que l'attribut `defer` et comment aide-t-il au chargement de la page ?

La dernière et la plus efficace façon de charger un script est d'utiliser l'attribut `defer`. L'attribut `defer` fonctionne principalement comme l'attribut `async` mais présente quelques différences clés.

```js
<script defer src="./js/script-1.js"></script>
<script defer src="./js/script-2.js"></script>
<script defer src="./js/script-3.js"></script>

```

Comme `async`, `defer` télécharge le script en arrière-plan, mais il n'interrompra jamais le rendu de la page pendant son exécution. 

Regardez l'image ci-dessous, où nous avons ajouté le flux de téléchargement et d'exécution de l'attribut `defer`.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/flow.png)
_Introduction de l'attribut defer_

Comme vous pouvez le voir, le script avec l'attribut `defer` est téléchargé en parallèle avec le document de la page. Cependant, il ne s'exécute qu'après le chargement du document. S'il y a plusieurs scripts avec les attributs `defer`, ils s'exécutent tous dans la séquence avant l'événement `DOMContentLoaded`. 

C'est la différence la plus significative avec `async`, où les scripts s'exécutent dès qu'ils sont chargés sans suivre aucun ordre.

En résumé, utilisez l'attribut `defer` avec les scripts qui manipulent le DOM. Cela améliorera le chargement de la page en téléchargeant les scripts en arrière-plan et en les exécutant après que le DOM soit prêt.

## Voici un rapide récapitulatif

Faisons un rapide récapitulatif des choses que nous avons apprises dans cet article :

* Le meilleur endroit pour la balise `<script>` dans un document HTML est à l'intérieur des balises `<head>...</head>`. Cependant, vous pouvez rencontrer des problèmes pour définir le contenu du DOM.
* Placer la balise `<script>` à la fin de la balise `<body>` est une manière idéale de gérer les scripts.
* HTML fournit les attributs `async` et `defer` pour charger la page plus rapidement et minimiser le retard de chargement des scripts plus volumineux en les téléchargeant en arrière-plan.
* Utilisez `async` pour les scripts externes qui ne manipulent pas le DOM. `async` ne garantit pas l'interruption du rendu de la page lorsque le script s'exécute.
* Utilisez `defer` pour tous les scripts qui manipulent le DOM. Les scripts avec l'attribut `defer` s'exécutent dans la séquence à la fin du chargement de la page.

## Avant de terminer...

C'est tout pour l'instant. J'espère que vous avez trouvé cet article informatif et perspicace. Tout le code source utilisé dans cet article peut être trouvé sur [ce dépôt GitHub](https://github.com/atapas/youtube/tree/main/javascript/load-async-defer).

Restez en contact.

* [ABONNEZ-VOUS](https://www.youtube.com/tapasadhikary?sub_confirmation=1) à ma chaîne YouTube si vous voulez apprendre JavaScript, ReactJS, Node.js, Git, et tout sur le développement web de manière pratique.
* [Suivez-moi sur Twitter](https://twitter.com/tapasadhikary) ou [LinkedIn](https://www.linkedin.com/in/tapasadhikary/) si vous ne voulez pas manquer la dose quotidienne de conseils en développement web et en programmation.
* Découvrez mes travaux open source sur [GitHub](https://github.com/atapas).
* Suivez-moi sur [Showwcase](https://www.showwcase.com/atapas398) pour un apprentissage basé sur la communauté.

À bientôt avec mon prochain article. En attendant, prenez soin de vous et restez heureux.