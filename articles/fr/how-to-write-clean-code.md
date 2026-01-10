---
title: Comment écrire du code propre – Conseils et bonnes pratiques (Guide complet)
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2023-05-15T14:43:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-clean-code
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-ken-tomita-389819.jpg
tags:
- name: best practices
  slug: best-practices
- name: clean code
  slug: clean-code
seo_title: Comment écrire du code propre – Conseils et bonnes pratiques (Guide complet)
seo_desc: 'Hi everyone! In this handbook we''re going to talk about writing "clean"
  code. It''s a topic that used to confuse me a bit when I was starting out as a programmer,
  and I find that it has many nuances and possible interpretations.

  So in this article we''...'
---

Bonjour à tous ! Dans ce guide, nous allons parler de l'écriture de code "propre". C'est un sujet qui me confusait un peu lorsque je débutais en tant que programmeur, et je trouve qu'il comporte de nombreuses nuances et interprétations possibles.

Dans cet article, nous allons donc parler de ce que signifie le terme "code propre", pourquoi c'est important, et comment évaluer si une base de code est propre ou non. Vous apprendrez également quelques bonnes pratiques et conventions à suivre pour rendre votre code plus propre.

C'est parti !

# Table des matières

* [Que signifie écrire du "code propre" et pourquoi devrais-je m'en soucier ?](#heading-quest-ce-que-le-code-propre-et-pourquoi-est-ce-important)
    
* [Comment puis-je évaluer si une base de code est propre ou non ?](#heading-comment-evaluer-si-une-base-de-code-est-propre-ou-non)
    
* [Conseils et conventions pour écrire un code plus propre](#heading-conseils-et-conventions-pour-ecrire-un-code-plus-propre)
    
    * [Efficacité, efficience et simplicité](#heading-efficacité-efficience-et-simplicité)
        
    * [Format et syntaxe](#heading-format-et-syntaxe)
        
    * [Nommage](#heading-nommage)
        
    * [Concis versus clair](#heading-concis-versus-clair)
        
    * [Réutilisabilité](#heading-reutilisabilité)
        
    * [Flux d'exécution clair](#heading-flux-dexeecution-clair)
        
    * [Principe de responsabilité unique](#heading-principe-de-responsabilité-unique)
        
    * [Avoir une "source unique de vérité"](#heading-avoir-une-source-unique-de-vérité)
        
    * [N'exposer et ne consommer que les informations nécessaires](#heading-nexposer-et-ne-consommer-que-les-informations-nécessaires)
        
    * [Modularisation](#heading-modularisation)
        
    * [Structures de dossiers](#heading-structures-de-dossiers)
        
    * [Documentation](#heading-documentation)
        
* [Conclusion](#heading-conclusion)
    

# Que signifie écrire du "code propre" et pourquoi devrais-je m'en soucier ?

Le code propre est un terme utilisé pour décrire du code informatique facile à lire, comprendre et maintenir. Le code propre est écrit de manière à le rendre simple, concis et expressif. Il suit un ensemble de conventions, de normes et de pratiques qui le rendent facile à lire et à suivre.

Le code propre est exempt de complexité, de redondance et d'autres odeurs de code et anti-modèles qui peuvent le rendre difficile à maintenir, déboguer et modifier.

Je ne peux pas assez insister sur l'importance du code propre. Lorsque le code est facile à lire et à comprendre, il facilite le travail des développeurs sur la base de code. Cela peut conduire à une productivité accrue et à une réduction des erreurs.

De plus, lorsque le code est facile à maintenir, cela garantit que la base de code peut être améliorée et mise à jour au fil du temps. Cela est particulièrement important pour les projets à long terme où le code doit être maintenu et mis à jour pendant des années.

# Comment puis-je évaluer si une base de code est propre ou non ?

Vous pouvez évaluer la propreté du code de diverses manières. Une bonne documentation, un formatage cohérent et une base de code bien organisée sont autant d'indicateurs de code propre.

Les revues de code peuvent également aider à identifier les problèmes potentiels et à garantir que le code suit les meilleures pratiques et conventions.

Les tests sont également un aspect important du code propre. Ils aident à garantir que le code fonctionne comme prévu et peuvent détecter les erreurs tôt.

Il existe plusieurs outils, pratiques et conventions que vous pouvez mettre en œuvre pour garantir une base de code propre. En mettant en œuvre ces outils et pratiques, les développeurs peuvent créer une base de code facile à lire, comprendre et maintenir.

Il est également important de se rappeler qu'il y a une part inévitable de subjectivité liée à ce sujet, et qu'il existe un certain nombre d'opinions et de conseils différents. Ce qui peut sembler propre et génial pour une personne ou un projet peut ne pas l'être pour une autre personne ou un autre projet.

Mais il existe tout de même quelques conventions générales que nous pouvons suivre pour obtenir un code plus propre, alors plongeons-nous dans cela maintenant.

# Conseils et conventions pour écrire un code plus propre

## Efficacité, efficience et simplicité

Chaque fois que je dois réfléchir à la manière d'implémenter une nouvelle fonctionnalité dans une base de code déjà existante, ou à la manière d'aborder la solution d'un problème spécifique, je priorise toujours ces trois choses simples.

### Efficacité

Tout d'abord, notre code doit être **efficace**, c'est-à-dire qu'il doit résoudre le problème qu'il est censé résoudre. Bien sûr, c'est l'attente la plus basique que nous puissions avoir pour notre code, mais si notre implémentation ne fonctionne pas réellement, il est inutile de penser à autre chose.

### Efficience

Deuxièmement, une fois que nous savons que notre code résout le problème, nous devons vérifier s'il le fait **efficacement**. Le programme s'exécute-t-il en utilisant une quantité raisonnable de ressources en termes de temps et d'espace ? Peut-il s'exécuter plus rapidement et avec moins d'espace ?

La complexité algorithmique est quelque chose dont vous devez être conscient afin d'évaluer cela. Si vous n'êtes pas familier avec cela, vous pouvez consulter [cet article que j'ai écrit](https://www.freecodecamp.org/news/introduction-to-algorithms-with-javascript-examples/#algorithmic-complexity).

Pour développer le sujet de l'efficience, voici deux exemples de fonction qui calcule la somme de tous les nombres dans un tableau.

```javascript
// Exemple inefficace
function sumArrayInefficient(array) {
  let sum = 0;
  for (let i = 0; i < array.length; i++) {
    sum += array[i];
  }
  return sum;
}
```

Cette implémentation de la fonction `sumArrayInefficient` parcourt le tableau en utilisant une boucle `for` et ajoute chaque élément à la variable `sum`. C'est une solution valide, mais elle n'est pas très efficace car elle nécessite de parcourir tout le tableau, quelle que soit sa longueur.

```javascript
// Exemple efficace
function sumArrayEfficient(array) {
  return array.reduce((a, b) => a + b, 0);
}
```

Cette implémentation de la fonction `sumArrayEfficient` utilise la méthode `reduce` pour additionner les éléments du tableau. La méthode `reduce` applique une fonction à chaque élément du tableau et accumule le résultat. Dans ce cas, la fonction ajoute simplement chaque élément à l'accumulateur, qui commence à 0.

C'est une solution plus efficace car elle ne nécessite qu'une seule itération sur le tableau et effectue l'opération de somme sur chaque élément au fur et à mesure.

### Simplicité

Et enfin vient la **simplicité**. C'est le plus difficile à évaluer car c'est subjectif, cela dépend de la personne qui lit le code. Mais quelques directives que nous pouvons suivre sont :

1. Pouvez-vous facilement comprendre ce que fait le programme à chaque ligne ?
    
2. Les fonctions et les variables ont-elles des noms qui représentent clairement leurs responsabilités ?
    
3. Le code est-il correctement indenté et espacé avec le même format tout au long de la base de code ?
    
4. Y a-t-il une documentation disponible pour le code ? Les commentaires sont-ils utilisés pour expliquer les parties complexes du programme ?
    
5. À quelle vitesse pouvez-vous identifier dans quelle partie de la base de code se trouvent certaines fonctionnalités du programme ? Pouvez-vous supprimer/ajouter de nouvelles fonctionnalités sans avoir besoin de modifier de nombreuses autres parties du code ?
    
6. Le code suit-il une approche modulaire, avec différentes fonctionnalités séparées en composants ?
    
7. Le code est-il réutilisé lorsque cela est possible ?
    
8. Les mêmes décisions d'architecture, de conception et d'implémentation sont-elles suivies de manière égale tout au long de la base de code ?
    

En suivant et en priorisant ces trois concepts d'efficacité, d'efficience et de simplicité, nous pouvons toujours avoir une ligne directrice à suivre lorsque nous réfléchissons à la manière d'implémenter une solution. Maintenant, développons quelques-unes des directives qui peuvent nous aider à simplifier notre code.

## Format et syntaxe

L'utilisation d'un formatage et d'une syntaxe cohérents dans une base de code est un aspect important de l'écriture de code propre. Cela est dû au fait que le formatage et la syntaxe cohérents rendent le code plus lisible et plus facile à comprendre.

Lorsque le code est cohérent, les développeurs peuvent facilement identifier les motifs et comprendre comment le code fonctionne, ce qui facilite le débogage, la maintenance et la mise à jour de la base de code au fil du temps. La cohérence aide également à réduire les erreurs, car elle garantit que tous les développeurs suivent les mêmes normes et conventions.

Voici quelques-unes des choses auxquelles nous devrions penser concernant le format et la syntaxe :

* **Indentation et espacement**
    

```javascript
// mauvaise indentation et espacement
const myFunc=(number1,number2)=>{
const result=number1+number2;
return result;
}

// bonne indentation et espacement
const myFunc = (number1, number2) => {
    const result = number1 + number2
    return result
}
```

Ici, nous avons un exemple de la même fonction, l'une faite sans indentation ni espacement, et l'autre correctement espacée et indentée. Nous pouvons voir que la deuxième est clairement plus facile à lire.

* **Syntaxe cohérente**
    

```javascript
// Fonction fléchée, pas de points-virgules, pas de return
const multiplyByTwo = number => number * 2

// Fonction, points-virgules, return
function multiplyByThree(number) {
    return number * 3;
}
```

Encore une fois, voici des fonctions très similaires implémentées avec une syntaxe différente. La première est une fonction fléchée, sans points-virgules ni return, tandis que l'autre est une fonction commune qui utilise des points-virgules et un return.

Les deux fonctionnent et sont très bien, mais nous devrions viser à toujours utiliser la même syntaxe pour des opérations similaires, car cela devient plus uniforme et lisible tout au long de la base de code.

Les linters et les formateurs de code sont de grands outils que nous pouvons utiliser dans nos projets pour automatiser les conventions de syntaxe et de formatage dans notre base de code. Si vous n'êtes pas familier avec ces outils, [consultez cet autre article que j'ai écrit](https://www.freecodecamp.org/news/using-prettier-and-jslint/).

* **Conventions de cas cohérentes**
    

```javascript
// camelCase
const myName = 'John'
// PascalCase
const MyName = 'John'
// snake_case
const my_name = 'John'
```

Même chose pour la convention de cas que nous choisissons de suivre. Toutes ces options fonctionnent, mais nous devrions viser à utiliser de manière cohérente la même convention dans tout notre projet.

## Nommage

Nommer les variables et les fonctions de manière claire et descriptive est un aspect important de l'écriture de code propre. Cela aide à améliorer la lisibilité et la maintenabilité de la base de code. Lorsque les noms sont bien choisis, les autres développeurs peuvent rapidement comprendre ce que fait la variable ou la fonction, et comment elle est liée au reste du code.

Voici deux exemples en JavaScript qui démontrent l'importance d'un nommage clair et descriptif :

```javascript
// Exemple 1 : Mauvaise nomination
function ab(a, b) {
  let x = 10;
  let y = a + b + x;
  console.log(y);
}

ab(5, 3);
```

Dans cet exemple, nous avons une fonction qui prend deux paramètres, les ajoute à une valeur codée en dur de 10, et enregistre le résultat dans la console. Le nom de la fonction et les noms des variables sont mal choisis et ne donnent aucune indication de ce que fait la fonction ou de ce que représentent les variables.

```javascript
// Exemple 1 : Bonne nomination
function calculateTotalWithTax(basePrice, taxRate) {
  const BASE_TAX = 10;
  const totalWithTax = basePrice + (basePrice * (taxRate / 100)) + BASE_TAX;
  console.log(totalWithTax);
}

calculateTotalWithTax(50, 20);
```

Dans cet exemple, nous avons une fonction qui calcule le prix total d'un produit incluant les taxes. Le nom de la fonction et les noms des variables sont bien choisis et donnent une indication claire de ce que fait la fonction et de ce que représentent les variables.

Cela rend le code plus facile à lire et à comprendre, surtout pour les autres développeurs qui pourraient travailler avec la base de code à l'avenir.

## Concis versus clair

Lorsque l'on écrit du code propre, il est important de trouver un équilibre entre concision et clarté. Bien qu'il soit important de garder le code concis pour améliorer sa lisibilité et sa maintenabilité, il est tout aussi important de s'assurer que le code est clair et facile à comprendre. Écrire un code trop concis peut entraîner de la confusion et des erreurs, et peut rendre le code difficile à utiliser pour les autres développeurs.

Voici deux exemples qui démontrent l'importance de la concision et de la clarté :

```javascript
// Exemple 1 : Fonction concise
const countVowels = s => (s.match(/[aeiou]/gi) || []).length;
console.log(countVowels("hello world"));
```

Cet exemple utilise une fonction fléchée concise et une regex pour compter le nombre de voyelles dans une chaîne donnée. Bien que le code soit très court et facile à écrire, il peut ne pas être immédiatement clair pour les autres développeurs comment fonctionne le motif regex, surtout s'ils ne sont pas familiers avec la syntaxe regex.

```javascript
// Exemple 2 : Fonction plus verbeuse et plus claire
function countVowels(s) {
  const vowelRegex = /[aeiou]/gi;
  const matches = s.match(vowelRegex) || [];
  return matches.length;
}

console.log(countVowels("hello world"));
```

Cet exemple utilise une fonction traditionnelle et une regex pour compter le nombre de voyelles dans une chaîne donnée, mais le fait de manière claire et facile à comprendre. Le nom de la fonction et les noms des variables sont descriptifs, et le motif regex est stocké dans une variable avec un nom clair. Cela permet de voir facilement ce que fait la fonction et comment elle fonctionne.

Il est important de trouver un équilibre entre concision et clarté lors de l'écriture de code. Bien que le code concis puisse améliorer la lisibilité et la maintenabilité, il est important de s'assurer que le code reste clair et facile à comprendre pour les autres développeurs qui pourraient travailler avec la base de code à l'avenir.

En utilisant des noms de fonctions et de variables descriptifs, et en utilisant un formatage de code clair et lisible et des commentaires, il est possible d'écrire un code propre et concis qui est facile à comprendre et à utiliser.

## Réutilisabilité

La réutilisabilité du code est un concept fondamental en ingénierie logicielle qui fait référence à la capacité du code à être utilisé plusieurs fois sans modification.

L'importance de la réutilisabilité du code réside dans le fait qu'elle peut grandement améliorer l'efficacité et la productivité du développement logiciel en réduisant la quantité de code qui doit être écrite et testée.

En réutilisant le code existant, les développeurs peuvent gagner du temps et des efforts, améliorer la qualité et la cohérence du code, et minimiser le risque d'introduire des bugs et des erreurs. Le code réutilisable permet également des architectures logicielles plus modulaires et évolutives, facilitant la maintenance et la mise à jour des bases de code au fil du temps.

```javascript
// Exemple 1 : Pas de réutilisabilité
function calculateCircleArea(radius) {
  const PI = 3.14;
  return PI * radius * radius;
}

function calculateRectangleArea(length, width) {
  return length * width;
}

function calculateTriangleArea(base, height) {
  return (base * height) / 2;
}

const circleArea = calculateCircleArea(5);
const rectangleArea = calculateRectangleArea(4, 6);
const triangleArea = calculateTriangleArea(3, 7);

console.log(circleArea, rectangleArea, triangleArea);
```

Cet exemple définit trois fonctions qui calculent respectivement l'aire d'un cercle, d'un rectangle et d'un triangle. Chaque fonction effectue une tâche spécifique, mais aucune d'entre elles n'est réutilisable pour d'autres tâches similaires.

De plus, l'utilisation d'une valeur PI codée en dur peut entraîner des erreurs si la valeur doit être modifiée à l'avenir. Le code est inefficace car il répète la même logique plusieurs fois.

```javascript
// Exemple 2 : Implémentation de la réutilisabilité
function calculateArea(shape, ...args) {
  if (shape === 'circle') {
    const [radius] = args;
    const PI = 3.14;
    return PI * radius * radius;
  } else if (shape === 'rectangle') {
    const [length, width] = args;
    return length * width;
  } else if (shape === 'triangle') {
    const [base, height] = args;
    return (base * height) / 2;
  } else {
    throw new Error(`Shape "${shape}" not supported.`);
  }
}

const circleArea = calculateArea('circle', 5);
const rectangleArea = calculateArea('rectangle', 4, 6);
const triangleArea = calculateArea('triangle', 3, 7);

console.log(circleArea, rectangleArea, triangleArea);
```

Cet exemple définit une seule fonction `calculateArea` qui prend un argument `shape` et un nombre variable d'arguments. En fonction de l'argument `shape`, la fonction effectue le calcul approprié et retourne le résultat.

Cette approche est beaucoup plus efficace car elle élimine le besoin de répéter le code pour des tâches similaires. Elle est également plus flexible et extensible, car des formes supplémentaires peuvent être facilement ajoutées à l'avenir.

## Flux d'exécution clair

Avoir un flux d'exécution clair est essentiel pour écrire du code propre car cela rend le code plus facile à lire, comprendre et maintenir. Le code qui suit une structure claire et logique est moins sujet aux erreurs, plus facile à modifier et à étendre, et plus efficace en termes de temps et de ressources.

D'un autre côté, le code spaghetti est un terme utilisé pour décrire du code qui est compliqué et difficile à suivre, souvent caractérisé par des blocs de code longs, enchevêtrés et désorganisés. Le code spaghetti peut être le résultat de mauvaises décisions de conception, d'un couplage excessif ou d'un manque de documentation et de commentaires appropriés.

Voici deux exemples de code JavaScript qui effectuent la même tâche, l'un avec un flux d'exécution clair, et l'autre avec du code spaghetti :

```javascript
// Exemple 1 : Flux d'exécution clair
function calculateDiscount(price, discountPercentage) {
  const discountAmount = price * (discountPercentage / 100);
  const discountedPrice = price - discountAmount;
  return discountedPrice;
}

const originalPrice = 100;
const discountPercentage = 20;
const finalPrice = calculateDiscount(originalPrice, discountPercentage);

console.log(finalPrice);

// Exemple 2 : Code spaghetti
const originalPrice = 100;
const discountPercentage = 20;

let discountedPrice;
let discountAmount;
if (originalPrice && discountPercentage) {
  discountAmount = originalPrice * (discountPercentage / 100);
  discountedPrice = originalPrice - discountAmount;
}

if (discountedPrice) {
  console.log(discountedPrice);
}
```

Comme nous pouvons le voir, l'exemple 1 suit une structure claire et logique, avec une fonction qui prend les paramètres nécessaires et retourne le résultat calculé. D'un autre côté, l'exemple 2 est beaucoup plus compliqué, avec des variables déclarées en dehors de toute fonction et plusieurs instructions if utilisées pour vérifier si le bloc de code s'est exécuté avec succès.

## Principe de responsabilité unique

Le principe de responsabilité unique (SRP) est un principe en développement logiciel qui stipule que chaque classe ou module ne doit avoir qu'une seule raison de changer, ou en d'autres termes, chaque entité dans notre base de code doit avoir une seule responsabilité.

Ce principe aide à créer du code facile à comprendre, maintenir et étendre.

En appliquant le SRP, nous pouvons créer du code plus facile à tester, réutiliser et refactoriser, puisque chaque module ne gère qu'une seule responsabilité. Cela rend moins probable les effets secondaires ou les dépendances qui peuvent rendre le code plus difficile à travailler.

```javascript
// Exemple 1 : Sans SRP
function processOrder(order) {
  // valider la commande
  if (order.items.length === 0) {
    console.log("Erreur : La commande n'a pas d'articles");
    return;
  }
  
  // calculer le total
  let total = 0;
  order.items.forEach(item => {
    total += item.price * item.quantity;
  });
  
  // appliquer les réductions
  if (order.customer === "vip") {
    total *= 0.9;
  }
  
  // sauvegarder la commande
  const db = new Database();
  db.connect();
  db.saveOrder(order, total);
}
```

Dans cet exemple, la fonction `processOrder` gère plusieurs responsabilités : elle valide la commande, calcule le total, applique les réductions et sauvegarde la commande dans une base de données. Cela rend la fonction longue et difficile à comprendre, et tout changement dans une responsabilité peut affecter les autres, rendant la maintenance plus difficile.

```javascript
// Exemple 2 : Avec SRP
class OrderProcessor {
  constructor(order) {
    this.order = order;
  }
  
  validate() {
    if (this.order.items.length === 0) {
      console.log("Erreur : La commande n'a pas d'articles");
      return false;
    }
    return true;
  }
  
  calculateTotal() {
    let total = 0;
    this.order.items.forEach(item => {
      total += item.price * item.quantity;
    });
    return total;
  }
  
  applyDiscounts(total) {
    if (this.order.customer === "vip") {
      total *= 0.9;
    }
    return total;
  }
}

class OrderSaver {
  constructor(order, total) {
    this.order = order;
    this.total = total;
  }
  
  save() {
    const db = new Database();
    db.connect();
    db.saveOrder(this.order, this.total);
  }
}

const order = new Order();
const processor = new OrderProcessor(order);

if (processor.validate()) {
  const total = processor.calculateTotal();
  const totalWithDiscounts = processor.applyDiscounts(total);
  const saver = new OrderSaver(order, totalWithDiscounts);
  saver.save();
}
```

Dans cet exemple, la fonction `processOrder` a été divisée en deux classes qui suivent le SRP : `OrderProcessor` et `OrderSaver`.

La classe `OrderProcessor` gère les responsabilités de validation de la commande, de calcul du total et d'application des réductions, tandis que la classe `OrderSaver` gère la responsabilité de sauvegarde de la commande dans la base de données.

Cela rend le code plus facile à comprendre, tester et maintenir, puisque chaque classe a une responsabilité claire et peut être modifiée ou remplacée sans affecter les autres.

## Avoir une "source unique de vérité"

Avoir une "source unique de vérité" signifie qu'il n'y a qu'un seul endroit où une donnée ou une configuration particulière est stockée dans la base de code, et toute autre référence à celle-ci dans le code renvoie à cette source unique. Cela est important car cela garantit que les données sont cohérentes et évite la duplication et l'incohérence.

Voici un exemple pour illustrer le concept. Supposons que nous avons une application qui doit afficher les conditions météorologiques actuelles dans une ville. Nous pourrions implémenter cette fonctionnalité de deux manières différentes :

```javascript
// Option 1 : Pas de "source unique de vérité"

// fichier 1 : weatherAPI.js
const apiKey = '12345abcde';

function getCurrentWeather(city) {
  return fetch(`https://api.weather.com/conditions/v1/${city}?apiKey=${apiKey}`)
    .then(response => response.json());
}

// fichier 2 : weatherComponent.js
const apiKey = '12345abcde';

function displayCurrentWeather(city) {
  getCurrentWeather(city)
    .then(weatherData => {
      // afficher weatherData sur l'UI
    });
}
```

Dans cette option, la clé API est dupliquée dans deux fichiers différents, ce qui rend plus difficile la maintenance et la mise à jour. Si nous devons changer la clé API, nous devons nous souvenir de la mettre à jour dans les deux endroits.

```javascript
// Option 2 : "Source unique de vérité"

// fichier 1 : weatherAPI.js
const apiKey = '12345abcde';

function getCurrentWeather(city) {
  return fetch(`https://api.weather.com/conditions/v1/${city}?apiKey=${apiKey}`)
    .then(response => response.json());
}

export { getCurrentWeather, apiKey };


// fichier 2 : weatherComponent.js
import { getCurrentWeather } from './weatherAPI';

function displayCurrentWeather(city) {
  getCurrentWeather(city)
    .then(weatherData => {
      // afficher weatherData sur l'UI
    });
}
```

Dans cette option, la clé API est stockée dans un seul endroit (dans le fichier `weatherAPI.js`) et exportée pour que d'autres modules l'utilisent. Cela garantit qu'il n'y a qu'une seule source de vérité pour la clé API et évite la duplication et l'incohérence.

Si nous devons mettre à jour la clé API, nous pouvons le faire en un seul endroit et tous les autres modules qui l'utilisent obtiendront automatiquement la valeur mise à jour.

## N'exposer et ne consommer que les données nécessaires

Un principe important de l'écriture de code propre est de n'exposer et ne consommer que les informations nécessaires à une tâche particulière. Cela aide à réduire la complexité, augmenter l'efficacité et éviter les erreurs qui peuvent survenir de l'utilisation de données inutiles.

Lorsque des données non nécessaires sont exposées ou consommées, cela peut entraîner des problèmes de performance et rendre le code plus difficile à comprendre et à maintenir.

Supposons que vous avez un objet avec plusieurs propriétés, mais que vous n'avez besoin d'utiliser que quelques-unes d'entre elles. Une façon de faire serait de référencer l'objet et les propriétés spécifiques chaque fois que vous en avez besoin. Mais cela peut devenir verbeux et sujet aux erreurs, surtout si l'objet est profondément imbriqué. Une solution plus propre et plus efficace serait d'utiliser la déstructuration d'objet pour n'exposer et ne consommer que les informations dont vous avez besoin.

```javascript
// Objet original
const user = {
  id: 1,
  name: 'Alice',
  email: 'alice@example.com',
  age: 25,
  address: {
    street: '123 Main St',
    city: 'Anytown',
    state: 'CA',
    zip: '12345'
  }
};

// N'exposer et ne consommer que les propriétés name et email
const { name, email } = user;

console.log(name); // 'Alice'
console.log(email); // 'alice@example.com'
```

## Modularisation

La modularisation est un concept essentiel dans l'écriture de code propre. Elle fait référence à la pratique de décomposer un code volumineux et complexe en modules ou fonctions plus petits et plus faciles à gérer. Cela rend le code plus facile à comprendre, tester et maintenir.

L'utilisation de la modularisation offre plusieurs avantages tels que :

1. Réutilisabilité : Les modules peuvent être réutilisés dans différentes parties de l'application ou dans d'autres applications, ce qui permet de gagner du temps et des efforts dans le développement.
    
2. Encapsulation : Les modules permettent de masquer les détails internes d'une fonction ou d'un objet, en exposant uniquement l'interface essentielle au monde extérieur. Cela aide à réduire le couplage entre différentes parties du code et à améliorer la qualité globale du code.
    
3. Évolutivité : En décomposant un code volumineux en morceaux modulaires plus petits, vous pouvez facilement ajouter ou supprimer des fonctionnalités sans affecter l'ensemble de la base de code.
    

Voici un exemple en JavaScript d'un morceau de code qui effectue une tâche simple, l'un n'utilisant pas la modularisation et l'autre implémentant la modularisation.

```javascript
// Sans modularisation
function calculatePrice(quantity, price, tax) {
  let subtotal = quantity * price;
  let total = subtotal + (subtotal * tax);
  return total;
}

// Sans modularisation
let quantity = parseInt(prompt("Entrez la quantité : "));
let price = parseFloat(prompt("Entrez le prix : "));
let tax = parseFloat(prompt("Entrez le taux de taxe : "));

let total = calculatePrice(quantity, price, tax);
console.log("Total : $" + total.toFixed(2));
```

Dans l'exemple ci-dessus, la fonction `calculatePrice` est utilisée pour calculer le prix total d'un article donné sa quantité, son prix et son taux de taxe. Cependant, cette fonction n'est pas modularisée et est étroitement couplée avec la logique d'entrée et de sortie de l'utilisateur. Cela peut rendre difficile le test et la maintenance.

Maintenant, voyons un exemple du même code utilisant la modularisation :

```javascript
// Avec modularisation
function calculateSubtotal(quantity, price) {
  return quantity * price;
}

function calculateTotal(subtotal, tax) {
  return subtotal + (subtotal * tax);
}

// Avec modularisation
let quantity = parseInt(prompt("Entrez la quantité : "));
let price = parseFloat(prompt("Entrez le prix : "));
let tax = parseFloat(prompt("Entrez le taux de taxe : "));

let subtotal = calculateSubtotal(quantity, price);
let total = calculateTotal(subtotal, tax);
console.log("Total : $" + total.toFixed(2));
```

Dans l'exemple ci-dessus, la fonction `calculatePrice` a été divisée en deux fonctions plus petites : `calculateSubtotal` et `calculateTotal`. Ces fonctions sont maintenant modularisées et sont responsables du calcul du sous-total et du total, respectivement. Cela rend le code plus facile à comprendre, tester et maintenir, et le rend également plus réutilisable dans d'autres parties de l'application.

La modularisation peut également faire référence à la pratique de diviser des fichiers de code uniques en de nombreux fichiers plus petits qui sont ensuite compilés en un seul (ou moins de fichiers). Cette pratique a les mêmes avantages dont nous venons de parler.

Si vous souhaitez savoir comment implémenter cela en JavaScript en utilisant des modules, [consultez cet autre article que j'ai écrit](https://www.freecodecamp.org/news/modules-in-javascript/).

## Structures de dossiers

Choisir une bonne structure de dossiers est une partie essentielle de l'écriture de code propre. Une structure de projet bien organisée aide les développeurs à trouver et modifier le code facilement, réduit la complexité du code et améliore la scalabilité et la maintenabilité du projet.

D'un autre côté, une mauvaise structure de dossiers peut rendre difficile la compréhension de l'architecture du projet, la navigation dans la base de code et peut entraîner de la confusion et des erreurs.

Voici des exemples de bonne et de mauvaise structure de dossiers en utilisant un projet React comme exemple :

```javascript
// Mauvaise structure de dossiers
my-app/
├── App.js
├── index.js
├── components/
│   ├── Button.js
│   ├── Card.js
│   └── Navbar.js
├── containers/
│   ├── Home.js
│   ├── Login.js
│   └── Profile.js
├── pages/
│   ├── Home.js
│   ├── Login.js
│   └── Profile.js
└── utilities/
    ├── api.js
    └── helpers.js
```

Dans cet exemple, la structure du projet est organisée autour des types de fichiers, tels que les composants, les conteneurs et les pages.

Mais cette approche peut entraîner de la confusion et de la duplication, car il n'est pas clair à quel endroit appartiennent les fichiers. Par exemple, le composant `Home` est présent à la fois dans les dossiers `containers` et `pages`. Cela peut également rendre difficile la recherche et la modification du code, car les développeurs peuvent avoir besoin de naviguer dans plusieurs dossiers pour trouver le code dont ils ont besoin.

```javascript
// Bonne structure de dossiers
my-app/
├── src/
│   ├── components/
│   │   ├── Button/
│   │   │   ├── Button.js
│   │   │   ├── Button.module.css
│   │   │   └── index.js
│   │   ├── Card/
│   │   │   ├── Card.js
│   │   │   ├── Card.module.css
│   │   │   └── index.js
│   │   └── Navbar/
│   │       ├── Navbar.js
│   │       ├── Navbar.module.css
│   │       └── index.js
│   ├── pages/
│   │   ├── Home/
│   │   │   ├── Home.js
│   │   │   ├── Home.module.css
│   │   │   └── index.js
│   │   ├── Login/
│   │   │   ├── Login.js
│   │   │   ├── Login.module.css
│   │   │   └── index.js
│   │   └── Profile/
│   │       ├── Profile.js
│   │       ├── Profile.module.css
│   │       └── index.js
│   ├── utils/
│   │   ├── api.js
│   │   └── helpers.js
│   ├── App.js
│   └── index.js
└── public/
    ├── index.html
    └── favicon.ico
```

Dans cet exemple, la structure du projet est organisée autour des fonctionnalités, telles que les composants, les pages et les utils. Chaque fonctionnalité a son propre dossier, qui contient tous les fichiers liés à cette fonctionnalité.

Cette approche facilite la recherche et la modification du code, car tous les fichiers liés à une fonctionnalité sont situés dans le même dossier. Elle réduit également la duplication et la complexité du code, car les fonctionnalités sont séparées et leurs fichiers associés sont organisés ensemble.

En général, une bonne structure de dossiers doit être organisée autour des fonctionnalités, et non des types de fichiers, et doit faciliter la recherche et la modification du code. Une structure claire et logique peut rendre un projet plus facile à maintenir, comprendre et développer, tandis qu'une structure confuse et incohérente peut entraîner des erreurs et de la confusion.

Si vous êtes intéressé à en apprendre davantage sur ce sujet, [dans cet article que j'ai écrit sur l'architecture logicielle](https://www.freecodecamp.org/news/an-introduction-to-software-architecture-patterns/#different-folder-structures-to-know) j'ai développé le sujet des structures de dossiers et des modèles bien connus que vous pouvez suivre.

## Documentation

La documentation est une partie essentielle de l'écriture de code propre. Une documentation appropriée aide non seulement le développeur qui a écrit le code à mieux le comprendre à l'avenir, mais facilite également la lecture et la compréhension de la base de code par d'autres développeurs. Lorsque le code est bien documenté, cela peut faire gagner du temps et des efforts dans le débogage et la maintenance du code.

La documentation est particulièrement importante dans les cas où des solutions simples et faciles à comprendre ne peuvent pas être implémentées, les cas où la logique métier est assez complexe, et les cas où des personnes non familières avec la base de code doivent interagir avec celle-ci.

Une façon de documenter le code est d'utiliser des commentaires. Les commentaires peuvent fournir un contexte et expliquer ce que fait le code. Mais il est important d'utiliser les commentaires avec sagesse, en ne commentant que là où c'est nécessaire et en évitant les commentaires redondants ou inutiles.

Une autre façon de documenter le code est d'utiliser la documentation intégrée. La documentation intégrée est intégrée dans le code lui-même et peut être utilisée pour expliquer ce que fait une fonction ou un morceau de code spécifique. La documentation intégrée est souvent utilisée en combinaison avec des outils comme [JSDoc](https://jsdoc.app/), qui fournit une norme pour documenter le code en JavaScript.

Des outils comme Typescript peuvent également fournir une documentation automatique pour notre base de code, ce qui est extrêmement utile.

Si vous souhaitez en savoir plus sur Typescript, j'ai écrit [un guide pour débutants il y a quelque temps](https://www.freecodecamp.org/news/an-introduction-to-typescript/#otherfunctionalitiesoftypescript).

Et enfin, des outils comme Swagger et Postman peuvent être utilisés pour documenter les API, fournissant un moyen de comprendre facilement comment interagir avec elles.

Si vous êtes intéressé à savoir comment implémenter, tester, consommer et documenter pleinement les API, j'ai récemment écrit deux guides pour les [API REST](https://www.freecodecamp.org/news/build-consume-and-document-a-rest-api/) et les [API GraphQL](https://www.freecodecamp.org/news/building-consuming-and-documenting-a-graphql-api/).

# **Con**clusion

Eh bien, tout le monde, comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau.

Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/germancocca/) ou [Twitter](https://twitter.com/CoccaGerman). À la prochaine !

![Image](https://www.freecodecamp.org/news/content/images/2023/05/giphy.gif align="left")