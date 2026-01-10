---
title: Comment utiliser les opérateurs "supérieur à" et "inférieur à" en JavaScript
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2024-02-13T11:02:26.000Z'
originalURL: https://freecodecamp.org/news/greater-than-and-less-than-operators-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/pexels-pixabay-417173--3-.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Operators
  slug: operators
seo_title: Comment utiliser les opérateurs "supérieur à" et "inférieur à" en JavaScript
seo_desc: 'In your JavaScript programs, you''ll often need to compare two values to
  see if one is greater than or less than the other. This is where the greater than
  and less than operators come in handy.

  In this article, we''ll look at how to use these operators...'
---

Dans vos programmes JavaScript, vous devrez souvent comparer deux valeurs pour voir si l'une est supérieure ou inférieure à l'autre. C'est là que les opérateurs "supérieur à" et "inférieur à" deviennent utiles.

Dans cet article, nous allons examiner comment utiliser ces opérateurs en détail à travers des exemples de code.

## Comment utiliser l'opérateur "supérieur à" `>` en JavaScript

Vous pouvez utiliser l'opérateur "supérieur à" pour vérifier si la valeur de gauche est supérieure à la valeur de droite. Il est représenté par le symbole `>`.

Le résultat retournera une valeur booléenne `true` si la valeur de gauche est supérieure à la valeur de droite, et `false` si ce n'est pas le cas.

Voici un exemple de vérification si `5` est supérieur à `3`:

```js
console.log(5 > 3); // true
```

Puisque le nombre `5` est supérieur à `3`, le résultat sera `true`.

Si nous inversons les deux valeurs, le résultat sera `false`:

```js
console.log(3 > 5); // false
```

## Comment utiliser l'opérateur "inférieur à" `<` en JavaScript

Vous pouvez utiliser l'opérateur "inférieur à" pour vérifier si la valeur de gauche est inférieure à la valeur de droite. Il est représenté par le symbole `<`.

Le résultat retournera une valeur booléenne `true` si la valeur de gauche est inférieure à la valeur de droite, et `false` si ce n'est pas le cas.

Voici un exemple qui vérifie si le nombre `3` est inférieur à `5`:

```js
console.log(3 < 5); // true
```

Puisque `3` est inférieur à `5`, le résultat sera `true`.

Mais si nous inversons les deux valeurs, le résultat sera `false`:

```js
console.log(5 < 3); // false
```

## Comment utiliser l'opérateur "supérieur ou égal à" `>=` en JavaScript

Si vous devez vérifier si la valeur de gauche est supérieure ou égale à la valeur de droite, vous pouvez utiliser l'opérateur "supérieur ou égal à". Il est représenté par le symbole `>=`.

Le résultat retournera une valeur booléenne `true` si la valeur de gauche est supérieure ou égale à la valeur de droite, et `false` si ce n'est pas le cas.

Voici un exemple qui vérifie si le nombre `5` est supérieur ou égal à `5`:

```js
console.log(5 >= 5); // true
```

Puisque le nombre `5` est égal à `5`, le résultat sera `true`.

Si nous changeons la valeur de gauche pour qu'elle soit `3`, le résultat sera `false`:

```js
console.log(3 >= 5); // false
```

## Comment utiliser l'opérateur "inférieur ou égal à" `<=` en JavaScript

Si vous devez vérifier si la valeur de gauche est inférieure ou égale à la valeur de droite, vous pouvez utiliser l'opérateur "inférieur ou égal à". Il est représenté par le symbole `<=`.

Le résultat retournera une valeur booléenne `true` si la valeur de gauche est inférieure ou égale à la valeur de droite, et `false` si ce n'est pas le cas.

Voici un exemple qui vérifie si le nombre `3` est inférieur ou égal à `5`:

```js
console.log(3 <= 5); // true
```

Si nous changeons la valeur de gauche pour qu'elle soit `6`, le résultat sera `false`:

```js
console.log(6 <= 5); // false
```

## Comment utiliser les opérateurs de comparaison dans une instruction conditionnelle

Il est courant d'utiliser les opérateurs de comparaison dans des instructions conditionnelles comme une instruction `if`.

Dans cet exemple, nous avons une application qui demande l'âge de l'utilisateur et affiche une réponse en fonction de l'âge saisi:

Pour le HTML, nous utiliserons un formulaire pour demander l'âge de l'utilisateur. Sous le formulaire, nous afficherons le message en fonction de l'âge saisi.

```html
<h1 class="title">Quel âge avez-vous?</h1>

<main>
  <form id="form">
    <div class="input-container">
      <label for="age">Entrez votre âge: </label>
      <input type="number" id="age" required min="1" max="120" />
    </div>

    <button class="submit-btn" id="submit-btn">Soumettre l'âge</button>
  </form>

  <p class="result-para" id="result"></p>
</main>
```

Ensuite, nous utiliserons une méthode appelée `getElementById` pour parcourir le document HTML afin de trouver les éléments qui correspondent aux identifiants que nous spécifions.

Nous pouvons utiliser la méthode pour obtenir l'élément de formulaire, la saisie de l'âge et le paragraphe de résultat, et les assigner à des variables `const`:

```js
const ageInput = document.getElementById("age");
const form = document.getElementById("form");
const resultParagraph = document.getElementById("result");
```

Nous voulons ensuite créer un tableau de chaînes pour montrer à l'utilisateur en fonction de son âge.

```js
const responsesArr = [
  "Oh wow! Vous n'êtes qu'un enfant.",
  "Bien! Il semble que vous soyez assez âgé pour conduire aux États-Unis.",
  "Génial! Il semble que vous soyez assez âgé pour voter aux États-Unis.",
  "Cool! Il semble que vous soyez assez âgé pour boire aux États-Unis.",
];
```

Ensuite, nous devons créer une fonction appelée `displayResponse` avec un paramètre appelé `age`. Cette fonction sera responsable de l'affichage des messages en fonction de l'âge saisi.

```js
function displayResponse(age) {

}
```

À l'intérieur de cette fonction, nous devons vérifier si l'âge de l'utilisateur est inférieur à `16`. Si c'est le cas, nous afficherons le premier message du tableau `responsesArr`.

Nous utiliserons la propriété `textContent` pour changer le texte à l'intérieur de l'élément `resultParagraph`.

```js
if (age < 16) {
  resultParagraph.textContent = responsesArr[0];
}
```

Si l'utilisateur a entre `16` et `18` ans, nous afficherons le deuxième message du tableau `responsesArr`.

```js
else if (age >= 16 && age < 18) {
    resultParagraph.textContent = responsesArr[1];
  }
```

Si l'utilisateur a entre `18` et `21` ans, nous afficherons le troisième message du tableau `responsesArr`.

```js
else if (age >= 18 && age < 21) {
    resultParagraph.textContent = responsesArr[2];
}
```

Si l'utilisateur a `21` ans ou plus, nous afficherons le dernier message du tableau `responsesArr`.

```js
else {
    resultParagraph.textContent = responsesArr[3];
  }
```

La dernière partie de cette fonction est de réinitialiser le formulaire après que l'utilisateur a soumis son âge.

```js
ageInput.value = "";
```

Voici la fonction complète:

```js
function displayResponse(age) {
  if (age < 16) {
    resultParagraph.textContent = responsesArr[0];
  } else if (age >= 16 && age < 18) {
    resultParagraph.textContent = responsesArr[1];
  } else if (age >= 18 && age < 21) {
    resultParagraph.textContent = responsesArr[2];
  } else {
    resultParagraph.textContent = responsesArr[3];
  }
  ageInput.value = "";
}
```

La dernière partie de cette application consiste à ajouter un écouteur d'événement qui vérifie lorsque l'utilisateur soumet son entrée dans le formulaire, et affiche ce message en fonction de l'âge saisi.

Nous allons utiliser la méthode `addEventListener` pour écouter l'événement `submit` sur le formulaire. Lorsque le formulaire est soumis, nous allons empêcher le comportement par défaut du formulaire et appeler la fonction `displayResponse` avec la valeur de la saisie de l'âge.

```js
form.addEventListener("submit", (e) => {
  e.preventDefault();
  displayResponse(ageInput.value);
});
```

Voici un exemple interactif complet sur CodePen:

%[https://codepen.io/Jessica-Wilkins-the-flexboxer/pen/zYbMBaP]

## Conclusion

Travailler avec des opérateurs de comparaison comme les opérateurs "supérieur à", "supérieur ou égal à", "inférieur à" et "inférieur ou égal à" est une tâche courante en JavaScript. Ils sont utilisés pour comparer deux valeurs et retourner une valeur booléenne `true` ou `false` en fonction de la comparaison.

J'espère que vous avez apprécié cet article et que vous l'avez trouvé utile.

Bon codage!