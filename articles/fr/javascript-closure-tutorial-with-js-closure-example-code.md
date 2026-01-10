---
title: Tutoriel sur les fermetures JavaScript – Avec exemple de code JS de fermeture
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-27T07:07:44.000Z'
originalURL: https://freecodecamp.org/news/javascript-closure-tutorial-with-js-closure-example-code
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/closure-1.jpeg
tags:
- name: closure
  slug: closure
- name: Closure with example
  slug: closure-with-example
- name: example
  slug: example
- name: JavaScript
  slug: javascript
- name: Lexical Scoping
  slug: lexical-scoping
seo_title: Tutoriel sur les fermetures JavaScript – Avec exemple de code JS de fermeture
seo_desc: 'By Anchal Nigam

  Closures – many of you JavaScript devs have probably heard this term before. When
  I started my journey with JavaScript, I encountered closures often. And I think
  they''re one of the most important and interesting concepts in JavaScript...'
---

Par Anchal Nigam

**Fermetures** – beaucoup d'entre vous, développeurs JavaScript, avez probablement déjà entendu ce terme. Lorsque j'ai commencé mon parcours avec JavaScript, j'ai souvent rencontré des fermetures. Et je pense qu'elles sont l'un des concepts les plus importants et intéressants en JavaScript. 

Vous ne les trouvez pas intéressantes ? Cela arrive souvent lorsque vous ne comprenez pas un concept – vous ne le trouvez pas intéressant. (Je ne sais pas si cela vous arrive ou non, mais c'est mon cas). 

Alors dans cet article, je vais essayer de rendre les fermetures intéressantes pour vous.

Avant de plonger dans le monde des fermetures, comprenons d'abord la **portée lexicale**. Si vous la connaissez déjà, passez la partie suivante. Sinon, plongez dedans pour mieux comprendre les fermetures.

## Portée lexicale 

Vous pensez peut-être – je connais la portée locale et globale, mais qu'est-ce que la portée lexicale ? J'ai réagi de la même manière lorsque j'ai entendu ce terme. Pas de souci ! Examinons cela de plus près. 

C'est simple comme les deux autres portées :

```javascript
function saluerClient() {
    var nomClient = "anchal";
    function messageSalutation() {
	  console.log("Salut ! " + nomClient); // Salut ! anchal
    }
   messageSalutation();
}
```

Vous pouvez voir à partir de la sortie ci-dessus que la fonction interne peut accéder à la variable de la fonction externe. C'est la portée lexicale, où la portée et la valeur d'une variable sont déterminées par l'endroit où elle est définie/créée (c'est-à-dire sa position dans le code). Compris ? 

Je sais que ce dernier point vous a peut-être confus. Alors laissez-moi vous emmener plus loin. Saviez-vous que la portée lexicale est également connue sous le nom de **portée statique** ? Oui, c'est son autre nom. 

Il existe également la **portée dynamique**, que certains langages de programmation supportent. Pourquoi ai-je mentionné la portée dynamique ? Parce qu'elle peut vous aider à mieux comprendre la portée lexicale.

Regardons quelques exemples :

```javascript
function messageSalutation() {
  console.log(nomClient);// ReferenceError: nomClient n'est pas défini
}

function saluerClient() {
   var nomClient = "anchal";
   messageSalutation();
}

saluetClient();
```

Êtes-vous d'accord avec la sortie ? Oui, cela donnera une erreur de référence. Cela est dû au fait que les deux fonctions n'ont pas accès à la portée de l'autre, car elles sont définies séparément.

Regardons un autre exemple :

```javascript
function ajouterNombres(nombre1) {
  console.log(nombre1 + nombre2);
}

function genererAjoutNombres() {
  var nombre2 = 10;
  ajouterNombres(nombre2);
}

genererAjoutNombres();
```

La sortie ci-dessus sera 20 pour un langage à portée dynamique. Les langages qui supportent la portée lexicale donneront `referenceError: nombre2 n'est pas défini`. Pourquoi ?

Parce qu'en portée dynamique, la recherche s'effectue d'abord dans la fonction locale, puis elle passe à la fonction qui a _appelé_ cette fonction locale. Ensuite, elle recherche dans la fonction qui a appelé _cette_ fonction, et ainsi de suite, jusqu'à la pile d'appels. 

Son nom est auto-explicatif – « dynamique » signifie changement. La portée et la valeur de la variable peuvent être différentes car cela dépend de l'endroit d'où la fonction est appelée. La signification d'une variable peut changer à l'exécution. 

Avez-vous compris l'essentiel de la portée dynamique ? Si oui, alors rappelez-vous simplement que la portée lexicale est son opposé.

En portée lexicale, la recherche s'effectue d'abord dans la fonction locale, puis elle passe à la fonction à l'intérieur de laquelle _cette_ fonction est définie. Ensuite, elle recherche dans la fonction à l'intérieur de laquelle _cette_ fonction est définie, et ainsi de suite. 

Ainsi, **lexicale** ou **portée statique** signifie que la portée et la valeur d'une variable sont déterminées par l'endroit où elle est définie. Cela ne change pas. 

Regardons à nouveau l'exemple ci-dessus et essayons de déterminer la sortie par vous-même. Juste un petit changement – déclarez `nombre2` en haut :

```javascript
var nombre2 = 2;
function ajouterNombres(nombre1) {
  console.log(nombre1 + nombre2);
}

function genererAjoutNombres() {
  var nombre2 = 10;
  ajouterNombres(nombre2);
}

genererAjoutNombres();

```

Savez-vous quelle sera la sortie ? 

Correct – c'est 12 pour les langages à portée lexicale. Cela est dû au fait que d'abord, il regarde dans la fonction `ajouterNombres` (portée la plus interne), puis il recherche vers l'intérieur, où cette fonction est définie. Comme il obtient la variable `nombre2`, la sortie est donc 12.

Vous vous demandez peut-être pourquoi j'ai passé autant de temps sur la portée lexicale ici. C'est un article sur les fermetures, pas sur la portée lexicale. Mais si vous ne connaissez pas la portée lexicale, vous ne comprendrez pas les fermetures. 

Pourquoi ? Vous aurez votre réponse lorsque nous examinerons la définition d'une fermeture. Alors, revenons aux fermetures.

## Qu'est-ce qu'une fermeture ? 

Regardons la définition d'une fermeture :

> Une fermeture est créée lorsqu'une fonction interne a accès aux variables et arguments de sa fonction externe. La fonction interne a accès à :   
> 1. Ses propres variables.  
> 2. Les variables et arguments de la fonction externe.  
> 3. Les variables globales.

Attendez ! Est-ce la définition d'une fermeture ou de la portée lexicale ? Les deux définitions semblent identiques. Comment sont-elles différentes ? 

Eh bien, c'est pourquoi j'ai défini la portée lexicale ci-dessus. Parce que les fermetures sont liées à la portée lexicale/statique. 

Regardons à nouveau sa définition qui vous dira comment les fermetures sont différentes.

> Une fermeture est lorsqu'une fonction est capable d'accéder à sa portée lexicale, même lorsque cette fonction est exécutée en dehors de sa portée lexicale.

Ou,

> Les fonctions internes peuvent accéder à la portée de leur parent, même après que la fonction parent a déjà été exécutée.

Confus ? Ne vous inquiétez pas si vous n'avez pas encore compris. J'ai des exemples pour vous aider à mieux comprendre. Modifions le premier exemple de portée lexicale :

```javascript
function saluerClient() {
  const nomClient = "anchal";
  function messageSalutation() {
    console.log("Salut ! " + nomClient);
  }
  return messageSalutation;
}

const appelerSaluetClient = saluerClient();
applerSaluetClient(); // sortie – Salut ! anchal
```

La différence dans ce code est que nous retournons la fonction interne et l'exécutons plus tard. Dans certains langages de programmation, la variable locale existe pendant l'exécution de la fonction. Mais une fois la fonction exécutée, ces variables locales n'existent plus et ne seront plus accessibles. 

Cependant, ici, la scène est différente. Après que la fonction parent est exécutée, la fonction interne (fonction retournée) peut toujours accéder aux variables de la fonction parent. Oui, vous avez deviné juste. Les fermetures en sont la raison. 

La fonction interne préserve sa portée lexicale lorsque la fonction parent est exécutée et donc, plus tard, cette fonction interne peut accéder à ces variables. 

Pour mieux le comprendre, utilisons la méthode `dir()` de la console pour examiner la liste des propriétés de `appelerSaluetClient` :

```javascript
console.dir(appelerSaluetClient);
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/closure.png)

À partir de l'image ci-dessus, vous pouvez voir comment la fonction interne préserve sa portée parent (`nomClient`) lorsque `saluetClient()` est exécutée. Et plus tard, elle a utilisé `nomClient` lorsque `appelerSaluetClient()` a été exécutée.

J'espère que cet exemple vous a aidé à mieux comprendre la définition ci-dessus d'une fermeture. Et peut-être que maintenant vous trouvez les fermetures un peu plus amusantes. 

Alors, quoi de neuf ? Rendons ce sujet plus intéressant en regardant différents exemples.

## Exemples de fermetures en action

```javascript
function compteur() {
  let compte = 0;
  return function() {
    return compte++;
  };
}

const valeurCompte = compteur();
valeurCompte(); // 0
valeurCompte(); // 1
valeurCompte(); // 2
```

Chaque fois que vous appelez `valeurCompte`, la valeur de la variable compte est incrémentée de 1. Attendez – pensiez-vous que la valeur de compte est 0 ? 

Eh bien, ce serait faux car une fermeture ne fonctionne pas avec une valeur. Elle stocke la **référence** de la variable. C'est pourquoi, lorsque nous mettons à jour la valeur, cela se reflète dans le deuxième ou troisième appel et ainsi de suite car la fermeture stocke la référence. 

Vous vous sentez un peu plus clair maintenant ? Regardons un autre exemple :

```javascript
function compteur() {
  let compte = 0;
  return function () {
    return compte++;
  };
}

const valeurCompte1 = compteur();
const valeurCompte2 = compteur();
valeurCompte1();  // 0
valeurCompte1();  // 1
valeurCompte2();   // 0
valeurCompte2();   // 1

```

  
J'espère que vous avez deviné la bonne réponse. Si ce n'est pas le cas, en voici la raison. Comme `valeurCompte1` et `valeurCompte2`, tous deux préservent leur propre portée lexicale. Ils ont des environnements lexicaux indépendants. Vous pouvez utiliser `dir()` pour vérifier la valeur `[[scopes]]` dans les deux cas.

Regardons un troisième exemple.

Celui-ci est un peu différent. Dans celui-ci, nous devons écrire une fonction pour obtenir la sortie :

```javascript
const appelAjoutNombre = ajouterNombre(7);
appelAjoutNombre(8) // 15
apelAjoutNombre(6) // 13
```

Simple. Utilisez vos nouvelles connaissances sur les fermetures :

```javascript
function ajouterNombre(nombre1) {
  return function (nombre2) {
    return nombre1 + nombre2;
  };
}
```

Maintenant, regardons quelques exemples délicats :

```javascript
function compterLeNombre() {
  var tableauStockage = [];
  for (var x = 0; x < 9; x++) {
    tableauStockage[x] = function () {
      return x;
    };
  }
  return tableauStockage;
}

const appelerFonctionsInternes = compterLeNombre();
applerFonctionsInternes[0]() // 9
appelerFonctionsInternes[1]() // 9
```

Chaque élément de tableau qui stocke une fonction vous donnera une sortie de 9. Avez-vous deviné juste ? Je l'espère, mais laissez-moi vous dire la raison. Cela est dû au comportement de la fermeture. 

La fermeture stocke la **référence**, pas la valeur. La première fois que la boucle s'exécute, la valeur de x est 0. Ensuite, la deuxième fois x est 1, et ainsi de suite. Parce que la fermeture stocke la référence, chaque fois que la boucle s'exécute, elle change la valeur de x. Et à la fin, la valeur de x sera 9. Donc `appelerFonctionsInternes[0]()` donne une sortie de 9. 

Mais que faire si vous voulez une sortie de 0 à 8 ? Simple ! Utilisez une fermeture. 

Réfléchissez-y avant de regarder la solution ci-dessous :

```javascript
function appelerLeNombre() {
  function obtenirTousLesNombres(nombre) {
    return function() {
      return nombre;
    };
  }
  var tableauStockage = [];
  for (var x = 0; x < 9; x++) {
    tableauStockage[x] = obtenirTousLesNombres(x);
  }
  return tableauStockage;
}

const appelerFonctionsInternes = appelerLeNombre();
console.log(appelerFonctionsInternes[0]()); // 0
console.log(appelerFonctionsInternes[1]()); // 1
```

Ici, nous avons créé une portée séparée pour chaque itération. Vous pouvez utiliser `console.dir(tableauStockage)` pour vérifier la valeur de x dans `[[scopes]]` pour différents éléments de tableau.

C'est tout ! J'espère que vous pouvez maintenant dire que vous trouvez les fermetures intéressantes.

Pour lire mes autres articles, consultez mon profil [ici](https://www.freecodecamp.org/news/author/anchal).