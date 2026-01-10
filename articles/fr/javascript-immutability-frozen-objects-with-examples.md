---
title: Immuabilité JavaScript – Objets gelés en JS expliqués avec des exemples
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2021-07-27T15:49:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-immutability-frozen-objects-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/freeCodeCamp-Cover-5.png
tags:
- name: immutability
  slug: immutability
- name: JavaScript
  slug: javascript
- name: object
  slug: object
seo_title: Immuabilité JavaScript – Objets gelés en JS expliqués avec des exemples
seo_desc: "In JavaScript, we use an Object to store multiple values as a complex data\
  \ structure. You create an object with a pair of curly braces {}. \nAn object can\
  \ have one or more properties. Each of the properties is a key-value pair separated\
  \ by a colon(:)...."
---

En JavaScript, nous utilisons un `Object` pour stocker plusieurs valeurs sous forme de structure de données complexe. Vous créez un objet avec une paire d'accolades `{}`. 

Un objet peut avoir une ou plusieurs propriétés. Chacune des propriétés est une paire clé-valeur séparée par un `deux-points (:)`. La clé doit être une chaîne de caractères ou un symbole JavaScript. La valeur peut être de n'importe quel type, y compris un autre objet.

Avec cette explication d'un objet, créons-en un pour voir comment il fonctionne :

```js
const user = {
 'name': 'Bob',
 'age': 27   
}
```

Ici, nous avons créé un objet avec deux propriétés (name, age) et leurs valeurs respectives. Nous avons créé une variable appelée `user` avec le mot-clé `const` et nous lui avons assigné l'objet comme valeur.

Par défaut, les objets sont `mutables`. Cela signifie qu'une fois créés, vous pouvez leur ajouter une nouvelle propriété, modifier la valeur d'une propriété existante, ou supprimer une propriété.

Dans mes premières années de programmation, j'ai trouvé les termes `mutable` et `immutable` très confus. Permettez-moi d'essayer de les expliquer en anglais simple. 

Mutable est quelque chose que vous pouvez changer. Immutable est simplement l'opposé de cela. Donc, la `mutabilité` est la capacité à changer au fil du temps. L'`immuabilité` signifie que quelque chose est inchangé au fil du temps.

Il pourrait y avoir des situations où vous ne voulez pas qu'un objet change de manière programmatique. Par conséquent, vous voudrez le rendre immuable. 

Lorsque qu'un objet est immuable, vous ne pouvez pas lui ajouter une nouvelle propriété, le modifier, ou supprimer une propriété existante. Il n'y a aucun moyen de l'étendre.

C'est ce qu'est un `Objet Gelé`, que nous allons apprendre, pratiquer et comprendre dans cet article.

J'ai discuté des objets gelés dans un fil Twitter récemment. N'hésitez pas à y jeter un coup d'œil. Cet article développera le fil avec plus de détails et d'exemples.

%[https://twitter.com/tapasadhikary/status/1416995389169971200]

# Comment créer un objet gelé en JavaScript

Vous pouvez geler (rendre immuable) un objet en utilisant la fonction `Object.freeze(obj)`. L'objet passé à la méthode `freeze` deviendra immuable. La méthode `freeze()` retourne également le même objet.

Créons un objet de langues supportées :

```js
const supportedLanguages = {
  'af': 'Afrikaans',
  'bn': 'Bengali',
  'de': 'Allemand',
  'en': 'Anglais',
  'fr': 'Français'
}

```

Si vous ne voulez pas que cet objet change après sa création, utilisez simplement la méthode `freeze` pour le rendre immuable.

```js
const frozenSupportedLanguages = Object.freeze(supportedLanguages);

// Les supportedLanguages et frozenSupportedLanguages sont identiques

frozenSupportedLanguages === supportedLanguages; // retourne true

```

Maintenant, essayons de changer l'un ou l'autre des objets et voyons ce qui se passe :

```js
// Ajouter une nouvelle propriété
supportedLanguages['kn'] = 'Kannada';

// Modifier une propriété existante
supportedLanguages["af"] = 'quelque chose d\'autre';

// Supprimer une propriété
delete supportedLanguages.bn; // retourne false

// afficher l'objet dans la console
console.log(supportedLanguages); // Inchangé => {af: "Afrikaans", bn: "Bengali", en: "Anglais", fr: "Français"}

```

Vous obtiendrez des erreurs lorsque vous essayez de changer un objet gelé (objet immuable) dans l'environnement JavaScript `strict`.

# Attendez – le mot-clé `const` ne fait-il pas la même chose ?

Ah, pas tout à fait. Le mot-clé `const` et `Object.freeze()` ne sont pas les mêmes choses. Lorsque vous assignez un objet à une variable créée avec le mot-clé const, vous ne pouvez pas réassigner une autre valeur. Cependant, vous pouvez modifier les objets assignés de la manière que vous voulez.

Comprenons la différence avec un exemple. Cette fois, nous prendrons le même objet `supportedLanguages` mais nous ne le gèlerons pas.

```js
const supportedLanguages = {
  'af': 'Afrikaans',
  'bn': 'Bengali',
  'de': 'Allemand',
  'en': 'Anglais',
  'fr': 'Français'
}
```

Maintenant, vous pouvez le modifier comme ceci :

```js
// Ajouter une nouvelle propriété
supportedLanguages['kn'] = 'Kannada';

// Modifier une propriété existante
supportedLanguages["af"] = 'quelque chose d\'autre';

// Supprimer une propriété
delete supportedLanguages.bn; // retourne true

// afficher l'objet dans la console
console.log(supportedLanguages);
```

Maintenant, l'objet `supportedLanguages` est changé comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-78.png)

Donc, ce changement est autorisé. Mais si vous essayez d'assigner un nouvel objet à la variable `supportedLanguages` :

```js
supportedLanguages = {'id': 'Indonésien'};
```

Vous obtiendrez cette erreur :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-79.png)

J'espère que la différence est claire maintenant – c'est aussi une question fréquemment posée en entretien.

# Pourquoi avons-nous besoin d'objets gelés en JavaScript ?

Encore une fois, nous avons besoin d'objets gelés lorsque nous avons besoin d'immuabilité. En programmation orientée objet, il est courant d'avoir des API que nous ne pouvons pas étendre ou modifier en dehors du contexte actuel. 

Vous vous souvenez du mot-clé `final` en Java ? Ou comment dans le langage de programmation Kotlin, les listes sont immuables par défaut ? Essayer de les muter à l'exécution provoque des erreurs. L'immuabilité est un concept essentiel à utiliser en programmation fonctionnelle.

L'immuabilité est souvent importante dans le langage de programmation JavaScript également. Vous pouvez vouloir qu'un objet de configuration soit immuable, un ensemble fixe de langues supportées pour vos applications, ou toute autre chose que vous ne voulez pas changer à l'exécution.

# Vous pouvez aussi geler un tableau

En JavaScript, les `Arrays` sont des objets sous le capot. Vous pouvez donc également appliquer `Object.freeze()` aux tableaux pour les rendre immuables.

Prenons un tableau des sens humains :

```js
const senses = ['touch', 'sight', 'hearing', 'smell', 'taste'];
```

Nous pouvons maintenant le rendre immuable comme ceci :

```js
Object.freeze(senses);
```

Maintenant, essayez de pousser un élément dans ce tableau. Ce n'est pas possible.

```js
senses.push('walking');
```

La sortie sera l'erreur suivante :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-80.png)

Essayez de supprimer un élément du tableau :

```js
senses.pop();
```

Vous obtiendrez cette erreur :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-81.png)

Veuillez noter l'erreur dans les deux cas. Il est clairement indiqué que l'ajout et la suppression de propriétés ne sont pas autorisés car l'objet sous-jacent n'est pas extensible.

# Object Freeze est superficiel

Une propriété d'objet JavaScript peut avoir un autre objet comme valeur. Cela peut aller à un niveau plus profond.

Lorsque nous gelons un objet, il s'agit d'un gel `superficiel`. Cela signifie que seules les propriétés de premier niveau sont gelées. Si l'une des valeurs des propriétés est un autre objet, cet objet interne n'est pas gelé. Vous pouvez encore y apporter des modifications.

Comprenons cela avec l'exemple d'un objet de configuration :

```js
const config = {
  'db': 'postgresql',
  'host': 'acme-ind.com',
  'password': 'fake-password',
  'port': 512,
  'admin': {
    'name': 'Tapas',
    'rights': ['create', 'update', 'delete']
  }
}
```

L'objet config a des propriétés comme db, host, password, et port avec des valeurs de type chaîne simple. Cependant, la propriété admin a un objet comme valeur. Maintenant, gelons l'objet config.

```js
Object.freeze(config);
```

Maintenant, essayons de changer le nom de la base de données.

```js
config.db = 'redis';
```

Ce n'est pas autorisé car l'objet est gelé. Cependant, vous pouvez faire ceci :

```js
config.admin.name = 'atapas';
```

Ici, nous avons changé la propriété de l'objet imbriqué. Comme le gel de l'objet est superficiel par nature, il ne nous empêchera pas de changer l'objet imbriqué. Donc, si vous affichez l'objet dans la console, voici ce que vous obtiendrez :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-82.png)

# Comment geler profondément un objet en JavaScript

Mais comment geler profondément un objet si vous en avez besoin ou si vous le souhaitez ? Vous pouvez vouloir geler toutes les propriétés de l'objet jusqu'au niveau le plus profond possible, n'est-ce pas ? Nous pouvons faire cela en utilisant la récursivité.

En programmation, la récursivité est une méthodologie qui utilise une procédure, une fonction ou un algorithme pour s'appeler elle-même. [Consultez cet article](https://www.freecodecamp.org/news/understanding-recursion-in-programming/) pour une compréhension approfondie.

Donc, nous pouvons itérer à travers chaque propriété et appliquer récursivement la méthode freeze à tout. Cela garantira que les objets imbriqués sont également gelés. 

Pour cela, vous pouvez écrire une fonction simple comme celle-ci :

```js
const deepFreeze = obj => {
  Object.keys(obj).forEach(prop => {
    if (typeof obj[prop] === 'object') deepFreeze(obj[prop]);
  });
  return Object.freeze(obj);
};

deepFreeze(config);
```

# Quelle est la différence entre freeze(), seal() et preventExtentions() ?

Avec Object.freeze, nous obtenons une immuabilité complète. Mais il existe deux autres méthodes qui fournissent une immuabilité d'objet, seulement partiellement.

* `Object.seal` – Nous ne pouvons pas ajouter une nouvelle propriété ou supprimer des propriétés existantes d'un objet scellé avec cette méthode. Mais nous pouvons toujours mettre à jour la valeur des propriétés existantes.
* `Object.preventExtensions` – Cette méthode empêche la création de nouvelles propriétés. Mais vous pouvez mettre à jour et supprimer des propriétés existantes.

Voici un tableau pour les comparer :

|                   | Créer | Lire | Mettre à jour | Supprimer |
|-------------------|--------|------|--------------|-----------|
| freeze            |    ❌    |  ✅   |      ❌      |     ❌    |
| seal              |    ❌   |  ✅    |      ✅      |     ❌    |
| preventExtensions |    ❌    |  ✅   |      ✅      |     ✅    |



# Comment dégelé un objet gelé

Il n'y a pas de moyens simples de dégelé un objet gelé en JavaScript. 

Vous pouvez probablement simuler un dégel en faisant une copie de l'objet en maintenant le prototype. 

[Voici un package NPM](https://www.npmjs.com/package/object-unfreeze) qui fait la même chose avec une copie superficielle.

# En résumé

Pour résumer,

* Nous pouvons geler un objet pour le rendre immuable.
* Vous utilisez la méthode `Object.freeze` pour geler un objet.
* Vous ne pouvez pas créer une nouvelle propriété, modifier ou supprimer une propriété existante, ou étendre l'objet lorsqu'un gel est appliqué.
* Déclarer une variable avec le mot-clé `const` avec une valeur d'objet n'est pas la même chose que geler l'objet.
* Vous pouvez geler un tableau en utilisant la même méthode `freeze`.
* La méthode freeze effectue un gel superficiel. Utilisez la récursivité pour effectuer un gel profond.
* Les méthodes `seal()` et `preventExtentions()` fournissent une immuabilité partielle.
* Le dégel n'est pas supporté dans le langage (pour l'instant).

# Avant de terminer...

C'est tout pour l'instant. J'espère que vous avez trouvé cet article instructif et qu'il vous aide à comprendre l'immuabilité des objets plus clairement.

Connectons-nous. Vous me trouverez actif sur [Twitter (@tapasadhikary)](https://twitter.com/tapasadhikary). N'hésitez pas à me suivre. J'ai également commencé à partager des connaissances en utilisant ma [chaîne YouTube](https://youtube.com/c/TapasAdhikary?sub_confirmation=1), alors n'hésitez pas à la consulter également.

Vous pourriez également aimer ces articles :

* [Le manuel des tableaux JavaScript – Méthodes de tableau JS expliquées avec des exemples](https://www.freecodecamp.org/news/the-javascript-array-handbook/)
* [Un guide pratique de la déstructuration d'objets en JavaScript](https://blog.greenroots.info/a-practical-guide-to-object-destructuring-in-javascript)
* [JavaScript : Comparaison d'égalité avec ==, === et Object.is](https://blog.greenroots.info/javascript-equality-comparison-with-and-objectis)
* [Comment NE PAS utiliser Git en pratique. Dix usages de Git que vous devriez connaître pour éviter.](https://blog.greenroots.info/how-not-to-use-git-in-practice-ten-git-usages-you-should-know-to-avoid)