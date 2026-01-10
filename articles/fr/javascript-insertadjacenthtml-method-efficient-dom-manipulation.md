---
title: Comment utiliser la méthode JavaScript insertAdjacentHTML() pour une manipulation
  efficace du DOM
subtitle: ''
author: Kamaldeen Lawal
co_authors: []
series: null
date: '2024-02-07T16:28:17.000Z'
originalURL: https://freecodecamp.org/news/javascript-insertadjacenthtml-method-efficient-dom-manipulation
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/The-JavaScript-insertAdjacentHTML
seo_title: Comment utiliser la méthode JavaScript insertAdjacentHTML() pour une manipulation
  efficace du DOM
---

Method.png
tags:
- name: DOM
  slug: dom
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'En JavaScript, les développeurs doivent pouvoir mettre à jour dynamiquement une page sans remplacer tout le contenu. Une méthode traditionnelle comme innerHTML peut causer des problèmes de performance, car ces méthodes tendent à remplacer tout le contenu d'un élément.

La...'
---

En JavaScript, les développeurs doivent pouvoir mettre à jour dynamiquement une page sans remplacer tout le contenu. Une méthode traditionnelle comme `innerHTML` peut causer des problèmes de performance, car ces méthodes tendent à remplacer tout le contenu d'un élément.

La méthode `insertAdjacentHTML()` conduit à de meilleures performances car vous l'utilisez pour insérer dynamiquement du nouveau contenu HTML sans affecter le contenu existant.

Dans ce tutoriel, nous couvrirons les points suivants :

* [Introduction à la méthode `insertAdjacentHTML()`](#heading-introduction-a-la-methode-insertadjacenthtml)
* [Syntaxe de la méthode `insertAdjacentHTML()`](#heading-syntaxe-de-la-methode-insertadjacenthtml)
* [Options de placement dans la](#options-de-placement-dans-la-methode-insertadjacenthtml) [méthode `insertAdjacentHTML()`](#options-de-placement-dans-la-methode-insertadjacenthtml)
* [Support des navigateurs pour la méthode `insertAdjacentHTML()`](#support-des-navigateurs-pour-la-methode-insertadjacenthtml)
* [Bonnes pratiques pour utiliser la](#bonnes-pratiques-pour-utiliser-la-methode-insertadjacenthtml) [méthode `insertAdjacentHTML()`](#bonnes-pratiques-pour-utiliser-la-methode-insertadjacenthtml)
* [Conclusion](#heading-conclusion)

## Introduction à la méthode `insertAdjacentHTML()`

La méthode `insertAdjacentHTML()` fournit un moyen efficace de manipuler la structure d'une page web sans remplacer tout le contenu d'un élément. C'est aussi la méthode de choix pour insérer des éléments HTML ou des éléments de texte à une position spécifique.

`insertAdjacentHTML` est une méthode en JavaScript qui permet d'insérer des éléments HTML ou du texte à une position spécifique par rapport à un élément donné dans le DOM (Document Object Model). Cette méthode offre une flexibilité dans la manipulation de la structure d'une page web de manière dynamique.

## Syntaxe de la méthode `insertAdjacentHTML()`

Voici à quoi ressemble la syntaxe de la méthode `insertAdjacentHTML()` :

```javascript
HTMLelement.insertAdjacentHTML(position, element);

```

La méthode `insertAdjacentHTML` prend deux paramètres :

1. **position** : Ce paramètre est une représentation sous forme de chaîne de caractères de l'endroit où le nouveau HTML doit être inséré par rapport à l'`targetElement`. Il doit correspondre à l'une des chaînes suivantes :

* `**"beforebegin"**` : La valeur de chaîne `beforebegin` de la méthode `insertAdjacentHTML()` insère l'élément HTML immédiatement avant l'élément spécifié dans le `DOM`.
* `**"afterbegin"**` : La valeur de chaîne `afterbegin` de la méthode `insertAdjacentHTML()` insère l'élément HTML à l'intérieur de l'`targetElement`, juste avant son premier enfant.
* `**"beforeend"**` : `beforeend` est une valeur de chaîne de la méthode `insertAdjacentHTML()` qui insère un élément HTML à l'intérieur de l'`targetElement`, après son dernier enfant.
* `**"afterend"**` : La valeur de chaîne `afterend` de la méthode `insertAdjacentHTML()` insère un élément HTML immédiatement après l'élément spécifié dans le `DOM`.

2. **element** : L'élément à insérer dans l'arborescence `DOM`.

## Options de placement dans la méthode `insertAdjacentHTML()`

Maintenant que vous avez vu les quatre paramètres possibles de la méthode `insertAdjacentHTML()`, voyons comment ils fonctionnent avec du code.

* `beforebegin` : Voici un exemple utilisant le paramètre `beforebegin` dans le code :

```javascript

const targetElement = document.querySelector('h1');
targetElement.insertAdjacentHTML('beforebegin', '<h2>Lawal</h2>');
```

Voici le résultat :

![beforebegin](https://www.freecodecamp.org/news/content/images/2024/02/beforebegin.png)
_beforebegin_

Rappelons que la valeur de chaîne `beforebegin` de la méthode `insertAdjacentHTML()` insère l'élément HTML immédiatement avant l'élément spécifié dans le `DOM`.

Dans le résultat du code ci-dessus, notre nouvel élément HTML inséré `h3` a été inséré avant notre `targetElement` `h2`. J'ai stylisé notre `targetElement` en ajoutant une bordure pour une illustration facile.

* `afterbegin` : voici un exemple d'utilisation du paramètre `afterbegin` dans le code :

```javascript
const targetElement = document.querySelector('h1');
targetElement.insertAdjacentHTML('afterbegin', '<h2>Lawal</h2>');

```

Et voici le résultat :

![afterbegin](https://www.freecodecamp.org/news/content/images/2024/02/afterbegin.png)
_afterbegin_

Comme défini ci-dessus, la valeur de chaîne `afterbegin` de la méthode `insertAdjacentHTML()` insère l'élément HTML à l'intérieur de l'`targetElement`, juste avant son premier enfant.

En vérifiant le résultat de notre code, vous pouvez réaliser que notre nouvel élément HTML inséré `h3` a été inséré à l'intérieur de notre `targetElement` `h2`. Encore une fois, j'ai stylisé notre `targetElement` en ajoutant une bordure pour une illustration facile.

* `beforeend` : voici un exemple d'utilisation de `beforeend` dans le code :

```javascript
const targetElement = document.querySelector('h1');
targetElement.insertAdjacentHTML('beforeend', '<h2>Lawal</h2>');
```

Et voici le résultat :

![beforeend](https://www.freecodecamp.org/news/content/images/2024/02/beforeend.png)
_beforeend_

La définition générale de `beforeend` est qu'il s'agit d'une valeur de chaîne de la méthode `insertAdjacentHTML()` qui insère un élément HTML à l'intérieur de l'`targetElement`, après son dernier enfant.

D'après le résultat du code, notre nouvel élément `HTML` inséré `h3` a été inséré à l'intérieur de notre `targetElement` `h2` après son enfant. J'ai stylisé notre `targetElement` en ajoutant une bordure pour une illustration facile.

* `afterend` : voici un exemple d'utilisation de `afterend` dans le code :

```javscript
const targetElement = document.querySelector('h1');
targetElement.insertAdjacentHTML('afterend', '<h2>Lawal</h2>');
```

Et voici le résultat :

![afterend](https://www.freecodecamp.org/news/content/images/2024/02/afterend.png)
_afterend_

Comme vous le savez maintenant, `afterend` est une valeur de chaîne de la méthode `insertAdjacentHTML()` qui insère un élément `HTML` immédiatement après l'élément spécifié dans le `DOM`.

Dans le code ci-dessus, notre nouvel élément HTML inséré `h3` a été inséré immédiatement après notre `targetElement` `h2`. J'ai stylisé notre `targetElement` en ajoutant une bordure pour une illustration facile.

## Support des navigateurs pour la méthode `insertAdjacentHTML()`

La méthode `insertAdjacentHTML()` est une méthode largement supportée sur laquelle vous pouvez compter pour vos besoins de manipulation du `DOM` dans différents navigateurs modernes.

Pour voir les navigateurs qui supportent cette méthode, consultez le résumé ci-dessous :

![compatibilité des navigateurs](https://www.freecodecamp.org/news/content/images/2024/02/browser-compat.png)
_compatibilité des navigateurs_

1. **Edge** : Supporté dans toutes les versions.
2. **Chrome** : Supporté dans toutes les versions.
3. **Opera** : Supporté dans toutes les versions.
4. **Safari** : Supporté dans toutes les versions, sauf les versions 3.1-3.2
5. **Firefox** : Supporté dans toutes les versions, sauf les versions 2-7

## Bonnes pratiques pour utiliser la méthode `insertAdjacentHTML()`

Pour utiliser efficacement la méthode `insertAdjacentHTML()`, voici quelques bonnes pratiques à suivre :

### Comprendre la méthode

Comprendre comment la méthode fonctionne vous aide à spécifier la position pour insérer votre contenu HTML. Comprenez les différentes positions et choisissez en fonction de vos besoins.

```javascript
// Insérer le contenu HTML après l'élément cible
document.getElementById('div').insertAdjacentHTML('afterend', '<div>Nouveau contenu avant l'élément cible</div>');

```

### Utilisez-la avec parcimonie

Une utilisation excessive des méthodes d'insertion d'éléments HTML dynamiques est mauvaise pour la maintenance du code.

Pour une application simple, une manipulation directe du `DOM` fera le travail.

```javascript
// Considérez l'utilisation de ceci :
let newElement = document.createElement('div');
newElement.textContent = 'Nouvel élément';
element.appendChild(newElement);


// Au lieu de ceci :
element.insertAdjacentHTML('beforeend', '<div>Nouvel élément</div>');
```

### Soyez conscient des performances

Si vous insérez fréquemment de grandes quantités de contenu HTML, la manipulation du `DOM` peut être coûteuse en termes de performance. Essayez de minimiser les mises à jour du `DOM`, surtout dans les scénarios de performance :

```javascript


// Considérez l'utilisation de l'insertion par lots :
let section = '';
data.forEach(item => {
  section += `<div>${item}</div>`;
});
element.insertAdjacentHTML('beforeend', section);


// Au lieu d'insérer un par un dans une boucle :
data.forEach(item => {
  element.insertAdjacentHTML('beforeend', `<div>${item}</div>`);
});
```

### Gestion des erreurs

Lors de l'utilisation de la méthode `insertAdjacentHTML()`, si le contenu HTML que vous essayez d'insérer est invalide, la méthode peut lever une erreur. Utilisez des blocs try-catch pour gérer ces situations de manière appropriée.

```javascript
const div  = document.getElementById('div');

try {
    // Vérifier si la valeur de div est vraie
    if (div.insertAdjacentHTML) {
        div.insertAdjacentHTML('beforeend', '<div>Nouvel Élémen</div>');
    } else {
        throw new Error('insertAdjacentHTML n'est pas supporté.');
    }
} catch (error) {
    // Gestion de l'erreur
    
    console.error('Erreur :', error.message);
    

    // Code alternatif
    div.innerHTML += '<div>Solution de repli : Nouvel Élément</div>';
}

```

## Conclusion

Dans ce tutoriel, vous avez appris la syntaxe et les options de placement de la méthode `insertAdjacentHTML()`. Nous avons également examiné la compatibilité des navigateurs et quelques bonnes pratiques lors de l'utilisation de la méthode `insertAdjacentHTML()`.