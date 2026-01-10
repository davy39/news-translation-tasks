---
title: Comment écrire des conditions JavaScript plus efficaces
subtitle: ''
author: Eesa Zahed
co_authors: []
series: null
date: '2023-05-03T17:44:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-more-efficient-javascript-conditions
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/image3-1.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment écrire des conditions JavaScript plus efficaces
seo_desc: "When you're coding in JavaScript, conditions are important for developing\
  \ a functional application. \nConditional statements are important because you use\
  \ them as \"validators\" which can either return truth or false. You can then use\
  \ them to trigger fu..."
---

Lorsque vous codez en JavaScript, les conditions sont importantes pour développer une application fonctionnelle. 

Les instructions conditionnelles sont importantes car vous les utilisez comme "validateurs" qui peuvent retourner vrai ou faux. Vous pouvez ensuite les utiliser pour déclencher d'autres actions dans le programme.

Mais avec de nombreuses instructions `if` longues et désordonnées dans le programme, cela peut causer de la confusion pour les développeurs et réduire considérablement la lisibilité. C'est pourquoi il est important pour les développeurs d'implémenter des conditions plus efficaces.

## Exemple d'instruction conditionnelle

Imaginez que vous créez une application de sondage. Chaque utilisateur doit choisir sa couleur préférée, mais les seules options sont rouge, vert et bleu.

Clairement, il n'y a pas beaucoup de choix pour les utilisateurs, mais restons sur une solution simple pour l'instant.

La fonction pour voter pourrait ressembler à ceci :

```js
const vote = (color) => {
  // le code va ici
}

```

Mais que se passe-t-il si un utilisateur vote pour une couleur qui n'est pas une option valide ? Ils pourraient avoir utilisé une liste déroulante dont vous avez oublié de supprimer certaines couleurs, ou l'utilisateur pourrait avoir manipulé le JavaScript côté client.

Essayez d'imaginer si un utilisateur votait pour la couleur orange. Vous devriez utiliser une logique JavaScript pour empêcher cela.

Comment feriez-vous cela ? Vous pourriez créer une condition simple où un utilisateur ne peut choisir que le rouge :

```js
const vote = (color) => {
  if (color !== "red") {
    return "couleur invalide";
  }

  return "couleur valide";
}

```

C'est génial ! Maintenant, la première condition que la fonction vérifie est : "La couleur n'est-elle pas rouge ? Eh bien, ce n'est pas autorisé", et retourne en conséquence.

```js
vote("orange"); // "couleur invalide"

```

Maintenant, comment pouvez-vous faire en sorte que la couleur bleue soit également acceptée ? Tout ce que vous avez à faire est d'ajouter une autre condition :

```js
const vote = (color) => {
  if (color !== "red" && color !== "blue") {
    return "couleur invalide";
  }

  return "couleur valide";
}

```

Cela fonctionne aussi. Mais que faire si vous voulez vérifier que la couleur est rouge, orange, jaune, vert, bleu ou violet ? Alors le code ressemblerait à ceci :

```js
const vote = (color) => {
  if (color !== "red" && color !== "orange"  && color !== "yellow"  && color !== "green"  && color !== "blue"  && color !== "purple") {
    return "couleur invalide";
  }

  return "couleur valide";
}

vote("cyan"); // "couleur invalide"

```

Comme vous pouvez le voir, cela fonctionne définitivement. Mais le code est long, désordonné et moins lisible maintenant. Pour implémenter cela efficacement, vous devez utiliser un tableau.

### Comment faire cela en utilisant un tableau

Tout d'abord, définissez le tableau. Un bon nom de variable est `validColors` :

```js
const validColors = ["red", "orange", "yellow", "green", "blue", "purple"];

```

Vous pouvez utiliser la méthode `array.includes()` ici. La syntaxe pour cela est :

```js
array.includes(item) // retourne un booléen

```

Pour implémenter cela dans le code, la syntaxe ressemble à ceci :

```js
!validColors.includes(color)

```

Le point d'exclamation (!) au début est là parce que vous voulez savoir si la couleur n'est PAS dans le tableau `validColors`.

Le code complet pour cela est :

```js
const validColors = ["red", "orange", "yellow", "green", "blue", "purple"];

const vote = (color) => {
  if (!validColors.includes(color)) {
    return "couleur invalide";
  }

  return "couleur valide";
}

```

Ce code est beaucoup plus facile à lire et à éditer. Et il sera beaucoup plus facile d'ajouter de nouvelles couleurs au tableau `validColors`.

Et vous pouvez tester le code pour vous assurer qu'il fonctionne :

```js
const validColors = ["red", "orange", "yellow", "green", "blue", "purple"];

const vote = (color) => {
  if (!validColors.includes(color)) {
    return "couleur invalide" ;
  }

  return "couleur valide";
}

console.log(vote("red")); // "couleur valide"
console.log(vote("orange")); // "couleur valide"
console.log(vote("yellow")); // "couleur valide"
console.log(vote("green")); // "couleur valide"
console.log(vote("blue")); // "couleur valide"
console.log(vote("purple")); // "couleur valide"

console.log(vote("cyan")); // "couleur invalide"
console.log(vote("black")); // "couleur invalide"

```

Maintenant, cette implémentation utilise beaucoup moins de code et est plus lisible. 

### Pourquoi les tableaux sont plus efficaces que les instructions switch

C'est beaucoup plus facile que d'utiliser une instruction switch, qui ressemblerait à ceci :

```js
const validColors = ["red", "orange", "yellow", "green", "blue", "purple"];

const vote = (color) => {
  switch (color) {
    case "red":
        console.log("vous avez voté rouge");
        break;
    case "orange":
        console.log("vous avez voté orange");
        break;
    case "yellow":
        console.log("vous avez voté jaune");
        break;
    case "green":
        console.log("vous avez voté vert");
        break;
    case "blue":
        console.log("vous avez voté bleu");
        break;
    case "purple":
        console.log("vous avez voté violet");
        break;
    default:
        console.log("couleur invalide");
    }
}

```

Comme vous pouvez le voir, cela utilise beaucoup plus de code. Un autre problème surgirait si vous deviez ajouter une autre couleur comme option valide. Au lieu de simplement mettre à jour un tableau, vous devriez éditer soigneusement une instruction switch, ce qui a un potentiel plus élevé de casser quelque chose dans le code.

### Le problème avec les instructions conditionnelles imbriquées

Pour un autre exemple, essayons d'ajouter le nom de l'utilisateur lors du vote. Le nom doit être inférieur ou égal à 15 caractères.

```js
const validColors = ["red", "orange", "yellow", "green", "blue", "purple"];

const vote = (name, color) => {
  if (!validColors.includes(color)) {
    return "couleur invalide" ;
  } else {
    if (name.length > 15) {
      return "le nom est trop long";
    }
  }

  return "nom et couleur valides";
}

console.log(vote("bob", "red")); // "nom et couleur valides"

```

Le code fonctionne correctement, mais est difficile à lire et peut causer de la confusion si plus de code est ajouté. Vous pouvez nettoyer cela en ne imbriquant pas les conditions.

```js
const validColors = ["red", "orange", "yellow", "green", "blue", "purple"];

const vote = (name, color) => {
  if (!validColors.includes(color)) {
    return "couleur invalide" ;
  }
  
  if (name.length > 15) {
    return "le nom est trop long";
  }

  return "nom et couleur valides";
}

console.log(vote("bob", "red")); // "nom et couleur valides"

```

Cela fonctionne bien, car le code vérifie d'abord si la couleur est valide, puis il vérifie si le nom est valide. Le code est également beaucoup plus facile à lire maintenant.

Cela a l'air bien ! J'espère que cela vous a aidé à comprendre comment écrire des conditions plus efficaces en JavaScript.

## Conclusion

N'hésitez pas à consulter mon [GitHub](https://github.com/eesazahed) et [Replit](https://replit.com/@eesazahed) pour voir mes projets.

Si vous souhaitez me contacter, mon adresse email est eszhd1 (at) gmail.com