---
title: Comment écrire des expressions régulières dans un fichier JSON
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-04-24T12:38:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-regular-expression-in-json-file
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/start-graph--11-.png
tags:
- name: json
  slug: json
- name: Regex
  slug: regex
seo_title: Comment écrire des expressions régulières dans un fichier JSON
seo_desc: 'JSON stands for JavaScript Object Notation. It is a text-based and lightweight
  data format for exchanging information between systems, for example, a web server
  and a web application.

  JSON files typically contain objects, arrays, strings, and numbers...'
---

JSON signifie JavaScript Object Notation. C'est un format de données basé sur du texte et léger pour échanger des informations entre des systèmes, par exemple, un serveur web et une application web.

Les fichiers JSON contiennent généralement des objets, des tableaux, des chaînes de caractères et des nombres. Mais vous pouvez également avoir des expressions régulières dans un fichier JSON. Et c'est ce que nous allons examiner dans cet article.


## Comment écrire des RegEx dans un JSON
Rappelez-vous que chaque entrée dans un fichier JSON est une paire `clé:valeur` entourée de guillemets doubles. Donc, si vous voulez écrire des RegEx dans votre fichier JSON, vous devez spécifier la clé et la valeur et entourer les deux de guillemets doubles.

La clé peut simplement être un nom arbitraire, et la valeur serait l'expression régulière elle-même. Voici un exemple de fichier JSON avec des expressions régulières :

```js
// fichier data.json

{
  "nigeriaPhone": "^(\\+?234|0)[789]\\d{9}$",
  "email": "^([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+)\\.([a-zA-Z]{2,5})$",
  "password": "^(?=.*[0-9])(?=.*[!@#\\$%^&*])[a-zA-Z0-9!@#\\$%^&*]{8,}$",
  "url": "^(http|https)://[a-zA-Z0-9-\\.]+\\.[a-zA-Z]{2,5}(/[a-zA-Z0-9-._~:/?#[\\]@!$&'()*+,;=]*)?$"
}
```


Écrire des RegEx dans un fichier JSON peut être utile lorsque vous voulez utiliser de nombreuses expressions régulières.

Au lieu d'encombrer votre fichier JavaScript, Python ou tout autre fichier de programmation avec des expressions régulières, vous pouvez les mettre toutes dans un fichier JSON. Vous pouvez ensuite importer le fichier dans votre fichier de langage de programmation et utiliser les entrées d'expressions régulières.

Cela nous amène à la manière d'utiliser un fichier JSON dans un langage de programmation. Plus précisément, nous allons voir comment faire cela en JavaScript.


## Comment utiliser une RegEx JSON dans un fichier JavaScript
Pour utiliser les RegEx de votre fichier JSON dans un fichier JavaScript, vous devez d'abord l'importer.

Un simple `import something from somefile` ne fonctionnera pas si vous voulez importer du JSON dans un fichier JS. Voici la bonne manière de le faire :

```bash
import someName from 'location/file.json' assert { type: 'json' };
```

Donc, je vais importer le fichier JSON comme ceci :

```js
import validators from './data.json' assert { type: 'json' };
```

Dans ce cas, j'importe toutes les entrées du fichier `data.json` et je les nomme `validators`. Ce nom peut être n'importe quoi.

La partie `assert { type: 'json' }` garantit que ce que j'importe est un objet JSON.

Vous pouvez ensuite enchaîner n'importe quelle clé du fichier JSON à `validators` pour voir à quoi ressemblent les entrées :

```js
import validators from './data.json' assert { type: 'json' };

console.log(validators.nigeriaPhone); // ^(\+?234|0)[789]\d{9}$
console.log(validators.email); // ^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$
console.log(validators.password); // ^(?=.*[0-9])(?=.*[!@#\$%^&*])[a-zA-Z0-9!@#\$%^&*]{8,}$
console.log(validators.url); // ^(http|https)://[a-zA-Z0-9-\.]+\.[a-zA-Z]{2,5}(/[a-zA-Z0-9-._~:/?#[\]@!$&'()*+,;=]*)?$
```

Vous pouvez même aller plus loin et tester ce que les expressions régulières valident. Voici comment j'ai validé un numéro de téléphone nigérian correct :

```js
import validators from './data.json' assert { type: 'json' };

const naijaNUmber = '+2348123456789';

if (naijaNUmber.match(validators.nigeriaPhone)) {
  console.log("C'est un numéro de téléphone Naija valide"); // C'est un numéro de téléphone Naija valide
} else {
  console.log("Ce n'est pas un numéro de téléphone Naija valide");
}
```

Et voici comment j'ai utilisé la clé `password` pour valider un mot de passe d'au moins huit caractères de long et contenant au moins un chiffre et au moins un caractère spécial :

```js
import validators from './data.json' assert { type: 'json' };

const pword = 'JohnDoe';

if (pword.match(validators.password)) {
  console.log("C'est un mot de passe valide");
} else {
  console.log(
    'Votre mot de passe doit comporter 8 caractères avec au moins 1 chiffre et 1 caractère spécial'
  ); // Votre mot de passe doit comporter 8 caractères avec au moins 1 chiffre et 1 caractère spécial
}
```

Malheureusement, dans certaines situations, vous obtenez une erreur si vous décidez d'utiliser directement la regex JSON sans créer une regex à partir de celle-ci. Voici un exemple avec `test()` :

```js
import validators from './data.json' assert { type: 'json' };

const naijaPhone = validators.nigeriaPhone;
console.log(naijaPhone); // Sortie : ^(\+?234|0)[789]\d{9}$

console.log(naijaPhone.test(83412343433));

/* sortie : dex.js:4 Uncaught TypeError: naijaPhone.test is not a function
    at index.js:4:24
*/
```

Vous pouvez voir que la sortie ne l'affiche pas comme une expression régulière - elle n'est pas entourée de barres obliques. Cela signifie que vous devez créer une regex à partir de celle-ci avec le constructeur regex :

```js
import validators from './data.json' assert { type: 'json' };

const naijaPhone = validators.nigeriaPhone;
console.log(naijaPhone); // Sortie : ^(\+?234|0)[789]\d{9}$

// Créer une regex à partir de validators.nigeriaPhone;
const naijaNumberRegex = new RegExp(naijaPhone);
console.log(naijaNumberRegex); // Sortie : /^(\+?234|0)[789]\d{9}$/
```

Vous pouvez voir qu'elle est maintenant entourée de barres obliques - c'est une façon d'identifier et même de créer des regex en JavaScript.

Voici comment les outils de développement de Chrome distinguent les deux :

![Screenshot-2023-04-24-at-12.22.56](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-24-at-12.22.56.png)

C'est avec cette regex que vous avez créée que vous pouvez tester le numéro :
```js
import validators from './data.json' assert { type: 'json' };

const naijaPhone = validators.nigeriaPhone;
console.log(naijaPhone); // Sortie : ^(\+?234|0)[789]\d{9}$

// Créer une regex à partir de validators.nigeriaPhone;
const naijaNumberRegex = new RegExp(naijaPhone);
console.log(naijaNumberRegex); // Sortie : /^(\+?234|0)[789]\d{9}$/

// tester avec la regex
console.log(naijaNumberRegex.test(83412343433)); // sortie : false
console.log(naijaNumberRegex.test(2348033333333)); // sortie : true
```


La raison pour laquelle cela a fonctionné avec la méthode `match()` et n'a pas fonctionné avec `test()` est la suivante :

* lorsque vous utilisez la méthode `match()`, vous pouvez passer directement la chaîne d'expression régulière que vous avez lue depuis un fichier JSON comme argument à la méthode, et JavaScript créera automatiquement une expression régulière à partir de la chaîne.

* lorsque vous utilisez la méthode `test()`, vous devez créer manuellement une expression régulière à partir de la chaîne d'expression régulière en utilisant le constructeur `new RegExp()`. Cela est dû au fait que la méthode `test()` attend un objet d'expression régulière comme argument, et non une chaîne.


## Conclusion
Vous avez vu qu'il n'y a pas de mise en garde supplémentaire impliquée dans l'écriture d'expressions régulières dans un fichier JSON - vous devez toujours suivre les mêmes règles pour écrire du JSON.

Et lorsque vous importez ce fichier JSON dans un fichier JavaScript, vous n'avez pas besoin de faire quoi que ce soit d'extraordinaire pour le faire fonctionner, autre que créer une regex à partir de celle-ci avec le constructeur `new RegExp()` dans certains cas.

Merci d'avoir lu !