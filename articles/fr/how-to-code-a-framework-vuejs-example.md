---
title: Comment coder un Framework – les premières lignes de Vue.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-25T21:38:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-code-a-framework-vuejs-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pexels-hans-middendorp-9092855.jpg
tags:
- name: framework
  slug: framework
- name: Vue.js
  slug: vuejs
seo_title: Comment coder un Framework – les premières lignes de Vue.js
seo_desc: 'By Fabio Pacific

  Have you ever wondered how frameworks are built? A couple of weeks ago I was writing
  an article and asked myself, what''s the first line of code Evan You wrote to build
  Vue.js?

  Well, thanks to Git and Evan You pushing Vue''s code to Gi...'
---

Par Fabio Pacific

Vous êtes-vous déjà demandé comment les frameworks sont construits ? Il y a quelques semaines, j'écrivais un article et je me suis demandé : quelle est la première ligne de code qu'Evan You a écrite pour construire Vue.js ?

Eh bien, grâce à Git et à Evan You qui a poussé le code de Vue sur GitHub, j'ai pu remonter le temps, comme Marty McFly avec sa machine à voyager dans le temps DeLorean. Mais je suis remonté neuf ans en arrière, en 2013, et j'ai "regardé" Evan écrire son code.

![Machine à voyager dans le temps DeLorean](https://www.freecodecamp.org/news/content/images/2022/05/217316-Back_to_the_Future-DeLorean-time_travel-car-movies-smoke.jpg)
_Photo par wallup.net_

## Quel est l'objectif de cet article ?

J'écris cet article pour vous montrer ce qui se cache derrière un outil populaire comme Vuejs et ce qui pourrait être le point de départ pour construire quelque chose de similaire. Plus précisément, nous allons examiner le point de départ d'Evan You.

Nous allons apprendre du créateur de Vue en examinant le code source de ses plus anciens commits. Nous allons étudier ce qu'il a écrit pour réaliser la première implémentation d'une application Vue et comment il a écrit la logique en JavaScript pur pour faire fonctionner la syntaxe des moustaches.

### Qu'est-ce que la syntaxe Mustache ?
Eh bien, si vous vous demandez ce qu'est la syntaxe des moustaches, laissez-moi vous expliquer. Il s'agit d'une forme basique de liaison de données utilisée par Vuejs pour interpoler du texte à l'intérieur d'un modèle.

D'après la documentation de Vue :

> Vue.js utilise une syntaxe de modèle basée sur HTML qui vous permet de lier de manière déclarative le DOM rendu aux données de l'instance Vue sous-jacente. La forme la plus basique de liaison de données est l'interpolation de texte utilisant la syntaxe "Mustache" (doubles accolades) :

`<span>Message : {{ msg }}</span>`

> La balise moustache sera remplacée par la valeur de la propriété msg de l'objet de données correspondant. Elle sera également mise à jour chaque fois que la propriété msg de l'objet de données changera.

D'accord, maintenant que vous savez ce que c'est, dans la section suivante, je répondrai à votre prochaine question...

## Qu'apprendrai-je après avoir lu cet article ?

D'accord, c'est juste, vous voulez savoir pourquoi vous devriez lire cet article et ce que vous en apprendrez.

Que vous soyez un développeur Vuejs expérimenté ou au début de votre parcours, vous apprendrez comment tout a commencé pour un outil populaire comme Vue.

Vous apprendrez également à rechercher une fonctionnalité spécifique d'un framework, à parcourir les anciens commits GitHub et à comprendre comment vous pouvez appliquer vos connaissances en JavaScript pur pour commencer à construire les premières fonctionnalités de l'un des frameworks les plus populaires de notre époque.

Dans la section suivante, nous commencerons à explorer le dépôt Vue.js. Nous examinerons les premier et deuxième commits pour comprendre quels fichiers ont été créés pour la configuration initiale du framework.

Cela nous aidera à trouver la fonctionnalité que nous recherchons (syntaxe des moustaches) et à comprendre comment la première application Vue a été créée.

## Exploration des plus anciens commits de Vue

Très bien, commençons. Si vous voulez me suivre dans ce voyage dans le temps, cliquez sur ce [lien](https://github.com/vuejs/vue/commits/0.6.0?after=218557cdec830a629252f4a9e2643973dc1f1d2d+349&branch=0.6.0&qualified_name=refs%2Ftags%2F0.6.0). Là, vous trouverez le dépôt Vuejs étiqueté 0.6.0. Nous nous intéressons à ses premier et deuxième commits.

J'ai téléchargé une copie du code source localement, précisément le code source du deuxième commit. Explorons le code.

%[https://youtu.be/jDeze8rA7cA]

## La structure des dossiers
La structure du projet dans le deuxième commit est assez simple. En plus d'un ensemble de fichiers de configuration pour jshing, grund, GitHub et les deux fichiers JSON, nous pouvons voir trois dossiers :

- test
- src
- explorations

Le dernier est une addition d'Evan. Le dossier exploration n'était pas là dans le premier commit. Et c'est là que la création réelle de Vue.js a commencé à prendre place.

Nous reviendrons ici plus tard dans l'article, mais avant cela, regardons le premier commit pour trouver les premières lignes de code d'Evan. Spoiler : tout commence par un test.


## Le premier cas de test de Vue

Les premières lignes de code sont, je crois, celles écrites dans le fichier test.js. C'est là qu'Evan a utilisé la bibliothèque Mocha pour écrire le premier cas de test de Vue et configurer le framework de tests dans le premier commit nommé [initial setup](https://github.com/vuejs/vue/commits/0.6.0?after=218557cdec830a629252f4a9e2643973dc1f1d2d+349&branch=0.6.0&qualified_name=refs%2Ftags%2F0.6.0).

Pourquoi est-ce pertinent ? Eh bien, nous ne cherchons pas seulement une fonctionnalité spécifique, mais nous voulons aussi comprendre quel est le point de départ pour construire un outil comme Vuejs.

Commencez-vous par écrire l'implémentation ? Ou écrivez-vous un cas de test de base juste pour tout configurer afin de pouvoir écrire des tests appropriés lorsque vous avez une idée de ce que vous voulez implémenter ?

Eh bien, ci-dessous vous avez votre réponse !

Vérifions le code du fichier test/test.js :

```js
var Element = require('element')

describe('Element', function () {
    it('should have a variable', function () {
        assert.equal(Element, 123)
    })
})
```

À la première ligne, il y a une instruction `require` pour importer une classe element qui sera définie quelque part plus tard dans le code. Imaginez cela comme l'ancêtre de la classe Vue.

Ensuite, la fonction `describe` de Mocha est définie pour fournir un contexte général.
À l'intérieur, une fonction `it` est appelée pour écrire le cas de test réel qui vérifie si la classe `Element` importée est égale à `123`, ce qu'elle fait en utilisant la méthode `assert.equal()`.

Pour exécuter les tests, nous devrons installer toutes les dépendances `npm i` et exécuter les tâches Grunt. Mais comme la plupart des bibliothèques utilisées sont obsolètes, nous ne le ferons pas (et ce n'est pas non plus le but de cet article et de cette vidéo).

Dans la section suivante, nous explorerons le deuxième commit dans le but d'atteindre nos objectifs – trouver la première implémentation de Vue.js et comprendre comment fonctionne la syntaxe des moustaches.

Pour cela, nous devons examiner le code source du deuxième commit, que j'ai téléchargé et que j'explore sur VSCode (si vous suivez également la vidéo).

Voici le [lien direct](https://github.com/vuejs/vue/tree/871ed9126639c9128c18bb2f19e6afd42c0c5ad9).

## La première application Vue

Dans Vue, tout ce que nous faisons est fait à l'intérieur d'une application Vue, qui est liée à une instance de la classe Vue. Nous devons donc d'abord trouver la première implémentation de cette classe et c'est là que nous trouverons la logique derrière la syntaxe des moustaches.

D'accord, nous devons regarder à l'intérieur du dossier explorations – c'est là que la magie opère.

Le fichier principal s'appelle `getset-revitis-style.html`, et ici nous pouvons voir toute la logique de la première application Vue (que vous pouvez trouver dans la balise body) et sa première implémentation (que vous pouvez trouver dans la balise `script`).

J'ai fait une copie de l'ensemble du fichier et j'ai placé tout dans un fichier index.html afin que nous puissions manipuler le code, ajouter des logs de console et explorer son fonctionnement.

Servons le fichier en utilisant `serve -s`. (Pour exécuter cette commande, vous devrez installer un package npm. Il suffit de taper dans le terminal `npm install -g serve`.)

Dans la balise body, nous pouvons voir l'application Vue, dans un `div` avec un `id` de `test`. Aujourd'hui, nous définissons notre application à l'intérieur d'un élément racine avec un id de `app` ou `root`, mais à l'époque, cela commençait avec un div de test.

```html

 <div id="test">
   <p>{{msg}}</p>
   <p>{{msg}}</p>
   <p>{{msg}}</p>
   <p>{{what}}</p>
   <p>{{hey}}</p>
  </div>
```

À l'intérieur du `div` de test, nous pouvons voir la syntaxe des doubles moustaches. Cool ! C'est la première fois qu'elle a été utilisée, mais comment fonctionne-t-elle ?

Dans la section suivante, nous explorerons la première classe Vue et chercherons la logique pour faire fonctionner ce `{{msg}}`.

## La première instance Vue

D'accord, nous avons trouvé la première utilisation de cette syntaxe, mais nous n'avons pas encore terminé. Nous voulons savoir comment elle fonctionne, vous vous souvenez ? Alors, regardons dans la balise script où nous trouverons la logique de la première classe Vue.

Evan a créé une classe appelée `Element` – souvenez-vous que nous sommes neuf ans en arrière dans le temps, et ES6 n'est pas une chose avant 2015.

La déclaration de la classe est écrite en utilisant `function Element () {}`. Il s'agit de la classe ancêtre de ce que nous connaissons aujourd'hui comme l'instance Vue que nous instancions en faisant `new Vue()`.

```js

function Element (id, initData) {
  // La première implémentation est ici
}
```

Ensuite, la première instance Vue est créée en instanciant la classe Element :

```js

var app = new Element('test', {
  msg: 'hello'
})

```

La classe attend un `id` et un `initData`. Ceux-ci sont passés à l'instance comme la valeur `test` et comme un objet `{}` avec une propriété appelée `msg`. Il s'agit de notre première implémentation de l'objet options.

D'accord, nous y arrivons. Maintenant que nous savons comment la classe a été implémentée et instanciée, regardons à l'intérieur pour trouver comment la syntaxe des doubles moustaches a été implémentée.

## Comment fonctionne la syntaxe Mustache

Nous y voilà. Le prochain bloc de code nous montrera les secrets de la syntaxe. C'est ce que nous avons cherché à comprendre, le but de l'article.

Après cela, vous serez en mesure de comprendre ce qui se cache derrière cette syntaxe et même de l'éditer et de la remplacer par la vôtre.

Vous pourriez faire quelque chose comme `[[msg]]` et peut-être l'appeler la syntaxe des doubles boîtes. 🤓

Le code ci-dessous est utilisé pour faire fonctionner la syntaxe des doubles moustaches. Entre les deux, il y a plus de code qui est responsable de la liaison des données.

```js
var bindingMark = 'data-element-binding' // <-- marque de liaison de données 

function Element (id, initData) {
// La première implémentation est ici
  var self = this,
  el = self.el = document.getElementById(id)
  //console.log(self.el)
  
  bindings = {} // la copie interne
  data = self.data = {} // l'interface externe
  content = el.innerHTML.replace(/\{\{(.*)\}\}/g, markToken)

  el.innerHTML = content


  // ....

  function markToken(match, variable) {
    console.log(match) // <-- LOG match = {{msg}}
    console.log(variable) // <-- LOG captured group as variable = msg
    //console.log(bindings)
    bindings[variable] = {}
    //console.log(bindings)

    console.log('<span ' + bindingMark + '="' + variable + '"></span>')
    return '<span ' + bindingMark + '="' + variable + '"></span>'
  }

  // ...
}
```


J'ai ajouté quelques logs de console pour comprendre ce qu'il y a dans deux paramètres clés (`match` et `variables`) et ce que la méthode `markToken` retourne.

À l'intérieur de la balise script, la première ligne est une variable `var bindingMark = 'data-element-binding'`. Cette variable sera utilisée comme un attribut de données et remplacera le contenu des accolades en utilisant la méthode replace avec une expression régulière `el.innerHTML.replace(/\{\{(.*)\}\}/g, markToken)`.

Oui, vous avez raison – derrière cette syntaxe, il y a du JavaScript pur et spécifiquement l'une des plus anciennes méthodes intégrées dans le langage.

`string.replace()` est une méthode de chaîne qui accepte deux paramètres :

- l'expression régulière
- une fonction de rappel  

Vérifiez le résultat de la regex en utilisant un site comme <regex101.com> pour voir ce qui correspond à la regex `\{\{(.*)\}\}`.

Lorsque la fonction de rappel `markToken` est appelée, nous avons accès à la correspondance et au groupe capturé, respectivement utilisés comme paramètres appelés `match` et `variables`.

Vous pouvez voir ces deux valeurs de paramètres en utilisant les logs de console que j'ai ajoutés dans le code source.

À l'intérieur de la méthode `markToken`, la première ligne après les logs de console est `bindings[variable] = {}`. Il s'agit d'une copie interne des données qui sera utilisée plus tard pour la fonctionnalité de liaison de données du framework.

Pour chaque correspondance, elle définit une nouvelle propriété dans l'objet `bindings` en tant qu'objet vide. Par exemple, si nous avons `{{msg}}`, une nouvelle propriété appelée `binginds[msg] = {}` sera créée.

Enfin, l'instruction return construit un élément `span` qui utilise la valeur de la variable `bindingMark` comme attribut de données, `data-element-binding`
et lui attribue le paramètre `variable` comme propriété.

Ainsi, au lieu de `{{mess}}`, la chaîne suivante `'<span ' + bindingMark + '="' + variable + '"></span>'` est créée. Le résultat est le code suivant :

```html
<span data-element-binding="msg"></span>
```

Le code Vue est encore à ses débuts. L'implémentation de la syntaxe des moustaches fonctionne parallèlement à la liaison de données qui n'est pas encore pleinement implémentée à ce stade du framework.

## Conclusion

Dans cet article, nous avons découvert les premières étapes qu'Evan You a prises pour construire Vue.js. Il s'agit d'une implémentation brute du framework, et nous n'avons vu qu'une petite partie de son code. Mais cela peut nous aider à comprendre comment fonctionnait l'une des fonctionnalités du framework. Et hey, les choses commencent toujours petit pour grandir avec le temps.

Faites-moi savoir si vous avez aimé ce type de contenu. Contactez-moi si vous voulez savoir ce qui se cache derrière une autre fonctionnalité de Vuejs.

Vous pouvez également envisager de vous abonner à ma [chaîne YouTube](https://www.youtube.com/channel/UCTuFYi0pTsR9tOaO4qjV_pQ).

Et vous pouvez me suivre sur [Twitter](https://twitter.com/Fab_Sky_Walker) et [Linkedin](https://www.linkedin.com/in/fabio-pacifici-com/).