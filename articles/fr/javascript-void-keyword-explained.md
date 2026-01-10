---
title: JavaScript Void 0 – Que signifie javascript:void(0) ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-27T20:27:10.000Z'
originalURL: https://freecodecamp.org/news/javascript-void-keyword-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9811740569d1a4ca17fb.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: JavaScript Void 0 – Que signifie javascript:void(0) ?
seo_desc: 'By Dillion Megida

  The word void means "completely empty space" according to the dictionary. This term,
  when used in programming, refers to a return of "nothing" - an "empty value" so
  to speak.

  What is the void keyword?

  When a function is void, it mea...'
---

Par Dillion Megida

Le mot void signifie « espace complètement vide » selon le dictionnaire. Ce terme, lorsqu'il est utilisé en programmation, fait référence à un retour de « rien » - une « valeur vide » en quelque sorte.

## Qu'est-ce que le mot-clé void ?

Quand une fonction est void, cela signifie que la fonction ne retourne rien. Cela ressemble aux fonctions en JavaScript qui retournent `undefined` explicitement, comme ceci :

```js
function und() {
  return undefined
}
und()
```

ou implicitement, comme ceci :

```js
function und() {
}
und()
```

Quelles que soient les expressions et instructions dans les fonctions ci-dessus (ajoute 2 nombres ensemble, trouve la moyenne de 5 nombres, peu importe), aucun résultat n'est retourné.

Maintenant, nous savons ce que le mot-clé `void` signifie. Qu'en est-il de `javascript:void(0)` ?

## Qu'est-ce que `javascript:void(0)` ?

Si nous divisons cela, nous avons `javascript:` et `void(0)`. Examinons chaque partie plus en détail.

### `javascript:`

Cela est appelé une **Pseudo URL**. Lorsque le navigateur reçoit cette valeur comme valeur de `href` sur une balise d'ancrage, il interprète le code JS qui suit le deux-points (:) plutôt que de traiter la valeur comme un chemin référencé.

Par exemple :

```html
<a href="javascript:console.log('javascript');alert('javascript')">Lien</a>
```

Lorsque "Lien" est cliqué, voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-119.png)

Comme on peut le voir ci-dessus, le navigateur ne traite pas `href` comme un chemin référencé. Au lieu de cela, il le traite comme du code JavaScript commençant après "javascript:" et séparé par des points-virgules.

### `void(0)`

L'opérateur void évalue les expressions données et retourne `undefined`.

Par exemple :

```js
const result = void(1 + 1);
console.log(result);
// undefined
```

`1 + 1` est évalué mais `undefined` est retourné. Pour confirmer cela, voici un autre exemple :

```html
<body>
  <h1>Titre</h1>
  <script>
        void(document.body.style.backgroundColor = 'red',
             document.body.style.color = 'white'
        )
  </script>
</body>
```

Le résultat du code ci-dessus est :          
                 

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-122.png)

Voici un autre exemple :

```js
console.log(void(0) === undefined)
// true
```

### Combinaison de `javascript:` et `void(0)`

Parfois, vous ne voulez pas qu'un lien navigue vers une autre page ou recharge une page. En utilisant `javascript:`, vous pouvez exécuter du code qui ne change pas la page actuelle.

Cela, utilisé avec `void(0)` signifie, **ne rien faire** - ne pas recharger, ne pas naviguer, ne pas exécuter de code.

Par exemple :

```html
<a href="javascript:void(0)">Lien</a>
```

Le mot "Lien" est traité comme un lien par le navigateur. Par exemple, il est focusable, mais il ne navigue pas vers une nouvelle page.

`0` est un argument passé à `void` qui ne fait rien et ne retourne rien.

Du code JavaScript (comme vu ci-dessus) peut également être passé comme argument à la méthode `void`. Cela fait que l'élément de lien exécute du code mais maintient la même page.

Par exemple :

```js
<a id='link' href="javascript:void(
  document.querySelector('#link').style.color = 'green'
)">Lien</a>
```

Lorsque le bouton est cliqué, voici le résultat :    

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-121.png)

Avec `void`, cela indique au navigateur de ne rien retourner (ou de retourner `undefined`).

Un autre cas d'utilisation des liens avec la référence `javascript:void(0)` est que parfois, un lien peut exécuter du code JavaScript en arrière-plan, et la navigation peut être inutile. Dans ce cas, les expressions seraient utilisées comme arguments passés à `void`.

## Conclusion

Dans cet article simplifié, nous avons appris ce qu'est l'opérateur `void`, comment il fonctionne et comment il est utilisé avec la pseudo URL `javascript:` pour les attributs `href` des liens.

Cela garantit qu'une page ne navigue pas vers une autre page ou ne recharge pas la page actuelle lorsqu'elle est cliquée.