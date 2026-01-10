---
title: Actualiser la Page en JavaScript – Tutoriel JS Recharger la Fenêtre
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-06-27T17:41:15.000Z'
originalURL: https://freecodecamp.org/news/refresh-the-page-in-javascript-js-reload-window-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/cover-template--4-.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Actualiser la Page en JavaScript – Tutoriel JS Recharger la Fenêtre
seo_desc: 'When you''re developing applications like a blog or a page where the data
  may change based on user actions, you''ll want that page to refresh frequently.

  When the page refreshes or reloads, it will show any new data based off those user
  interactions. G...'
---

Lorsque vous développez des applications comme un blog ou une page où les données peuvent changer en fonction des actions de l'utilisateur, vous voudrez que cette page s'actualise fréquemment.

Lorsque la page s'actualise ou se recharge, elle affichera les nouvelles données basées sur ces interactions utilisateur. Bonne nouvelle – vous pouvez implémenter ce type de fonctionnalité en JavaScript avec une seule ligne de code.

Dans cet article, nous allons apprendre comment recharger une page web en JavaScript, ainsi que voir d'autres situations où nous pourrions vouloir implémenter ces rechargements et comment le faire.

### Voici un Scrim Interactif sur Comment Actualiser la Page en JavaScript

<iframe src="https://scrimba.com/scrim/cQ4ZKmt3?embed=freecodecamp,mini-header" width="100%" height="420"></iframe>

## Comment Actualiser une Page en JavaScript avec `location.reload()`

Vous pouvez utiliser la méthode JavaScript `location.reload()` pour recharger l'URL actuelle. Cette méthode fonctionne de manière similaire au bouton Actualiser du navigateur.

La méthode `reload()` est la méthode principale responsable du rechargement de la page. D'autre part, `location` est une interface qui représente l'emplacement réel (URL) de l'objet auquel elle est liée – dans ce cas, l'URL de la page que nous voulons recharger. Elle peut être accessible via `document.location` ou `window.location`.

Voici la syntaxe pour recharger une page :

```js
window.location.reload();
```

**Note :** Lorsque vous lisez certaines ressources sur « l'actualisation de page en JavaScript », vous rencontrerez diverses explications indiquant que la méthode de rechargement prend des valeurs booléennes comme paramètres et que `location.reload(true)` aide à forcer le rechargement afin de contourner son cache. Mais ce n'est pas le cas.

Selon la [Documentation MDN](https://developer.mozilla.org/en-US/docs/Web/API/Location/reload), un paramètre booléen ne fait pas partie de la spécification actuelle pour `location.reload()` — et en fait, il n'a *jamais* fait partie d'aucune spécification pour `location.reload()` jamais publiée.

Des navigateurs comme Firefox, en revanche, supportent l'utilisation d'un paramètre booléen non standard connu sous le nom de `forceGet` pour `location.reload()`, qui indique à Firefox de contourner son cache et de forcer le rechargement du document actuel.

En dehors de Firefox, tout paramètre que vous spécifiez dans un appel `location.reload()` dans d'autres navigateurs sera ignoré et n'aura aucun effet.

## Comment Effectuer un Rechargement/Actualisation de Page en JavaScript Lorsqu'un Bouton est Cliqué

Jusqu'à présent, nous avons vu comment fonctionne le rechargement en JavaScript. Maintenant, voyons comment vous pouvez implémenter cela lorsqu'un événement se produit ou lorsqu'une action comme un clic sur un bouton se produit :

```js
<button type="button" onClick="window.location.reload()">
   Recharger la Page
</button>
```

**Note :** Cela fonctionne de manière similaire à lorsque nous utilisons `document.location.reload()`.

## Comment Actualiser/Recharger une Page Automatiquement en JavaScript

Nous pouvons également permettre à une page de s'actualiser après un temps fixe en utilisant la méthode `setTimeOut()` comme vu ci-dessous :

```js
setTimeout(() => {
  document.location.reload();
}, 3000);
```

En utilisant le code ci-dessus, notre page web se rechargera toutes les 3 secondes.

Jusqu'à présent, nous avons vu comment utiliser la méthode de rechargement dans notre fichier HTML lorsque nous l'attachons à des événements spécifiques, ainsi que dans notre fichier JavaScript.

## Comment Actualiser/Recharger une Page en Utilisant la Fonction History en JavaScript

La fonction History est une autre méthode pour actualiser une page. La fonction history est utilisée comme d'habitude pour naviguer en arrière ou en avant en passant soit une valeur positive soit négative.

Par exemple, si nous voulons revenir en arrière, nous utiliserons :

```js
history.go(-1);
```

Cela chargera la page et nous emmènera à la page précédente que nous avons visitée. Mais si nous voulons seulement actualiser la page actuelle, nous pouvons le faire en ne passant aucun paramètre ou en passant `0` (une valeur neutre) :

```js
history.go();
history.go(0);
```

**Note :** Cela fonctionne également de la même manière que nous avons ajouté la méthode `reload()` à la méthode `setTimeOut()` et à l'événement de clic en HTML.

## Conclusion

Dans cet article, nous avons appris comment actualiser une page en utilisant JavaScript. Nous avons également clarifié une idée fausse courante qui conduit les gens à passer des paramètres booléens dans la méthode `reload()`.

Merci d'avoir lu !

Embarquez pour un voyage d'apprentissage ! [Parcourez plus de 200 articles d'experts sur le développement web](https://joelolawanle.com/contents). Consultez [mon blog](https://joelolawanle.com/posts) pour plus de contenu captivant de ma part.