---
title: Programmation Impérative vs Déclarative – la Différence Expliquée en Français
  Simple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-08T18:32:24.000Z'
originalURL: https://freecodecamp.org/news/imperative-vs-declarative-programming-difference
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/imperative-vs-declarative-programming-difference.jpg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
seo_title: Programmation Impérative vs Déclarative – la Différence Expliquée en Français
  Simple
seo_desc: 'By Mike Zetlow

  As a coding instructor, it’s my duty to send programmers out into the world thinking
  in new ways. A major shift in thinking occurs when we switch from imperative to
  declarative programming.

  Once my students have learned basic JavaScrip...'
---

Par Mike Zetlow

En tant qu'instructeur de codage, c'est mon devoir d'envoyer des programmeurs dans le monde en pensant de nouvelles manières. Un grand changement de pensée se produit lorsque nous passons de la programmation impérative à la programmation déclarative.

Une fois que mes étudiants ont appris les bases de JavaScript, nous passons en revue la programmation fonctionnelle et les méthodes de tableau utilisées dans un style de codage déclaratif. C'est là que leurs cerveaux commencent à éclater et à grésiller et à fondre comme des guimauves sur un feu.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/marshmellows-on-grill-crop-1.jpg)

## Qu'est-ce que la Programmation Impérative ?

En tant que débutant, vous avez probablement surtout codé dans un style impératif : vous donnez à l'ordinateur un ensemble d'instructions à suivre et l'ordinateur fait ce que vous voulez dans une séquence facile à suivre.

Imaginez que nous avons une liste des mots de passe les plus couramment utilisés dans le monde :

```javascript
const passwords = [
   "123456",
   "password",
   "admin",
   "freecodecamp",
   "mypassword123",
];
```

Notre application va vérifier le mot de passe de l'utilisateur lors de l'inscription et ne pas lui permettre de créer un mot de passe qui figure dans cette liste.

Mais avant de faire cela, nous voulons affiner cette liste. Nous avons déjà du code qui ne permet pas à l'utilisateur de s'inscrire avec un mot de passe de moins de 9 caractères. Nous pouvons donc réduire cette liste aux mots de passe de 9 caractères ou plus pour accélérer notre vérification.

De manière impérative, nous écririons :

```javascript
// utilisant la constante passwords ci-dessus

let longPasswords = [];
for (let i = 0; i < passwords.length; i++) {
   const password = passwords[i];
   if (password.length >= 9) {
      longPasswords.push(password);
   }
}

console.log(longPasswords); // logs ["freecodecamp", "mypassword123"];
```

1. Nous créons une liste vide appelée `longPasswords`.
2. Ensuite, nous écrivons une boucle qui s'exécutera autant de fois qu'il y a de mots de passe dans la liste `passwords` originale.
3. Ensuite, nous obtenons le mot de passe à l'index de l'itération de la boucle où nous nous trouvons.
4. Ensuite, nous vérifions si ce mot de passe est supérieur ou égal à 9 caractères.
5. Si c'est le cas, nous le mettons dans la liste `longPasswords`.

L'un des points forts de la programmation impérative est qu'elle est facile à comprendre. Comme un ordinateur, nous pouvons suivre étape par étape.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/steps-crop.jpg)

## Qu'est-ce que la Programmation Déclarative ?

Mais il existe une autre façon de penser au codage – comme un processus de définition constante de ce que sont les choses. Cela s'appelle la programmation déclarative.

La programmation impérative et déclarative atteignent les mêmes objectifs. Ce sont simplement des façons différentes de penser au code. Elles ont leurs avantages et inconvénients et il y a des moments pour utiliser les deux.

Bien que la programmation impérative soit plus facile à comprendre pour les débutants, la programmation déclarative nous permet d'écrire un code plus lisible qui reflète exactement ce que nous voulons voir. Combinée avec de [bons noms de variables](https://github.com/10xcodecamp/javascript-conventions-and-code-style), elle peut être un outil puissant.

Ainsi, au lieu de donner à l'ordinateur des instructions étape par étape, nous déclarons ce que nous voulons et nous attribuons cela au résultat d'un processus.

```javascript
// utilisant la constante passwords ci-dessus

const longPasswords = passwords.filter(password => password.length >= 9);

console.log(longPasswords); // logs ["freecodecamp", "mypassword123"];
```

La liste des `longPasswords` est définie (ou déclarée) comme la liste des `passwords` filtrée pour ne contenir que les mots de passe de 9 caractères ou plus.

Les méthodes de programmation fonctionnelle en JavaScript nous permettent de déclarer les choses de manière propre.

* **Ceci est une liste de mots de passe.**
* **Ceci est une liste de mots de passe longs uniquement.** (Après avoir exécuté `filter`.)
* **Ceci est une liste de mots de passe avec des identifiants.** (Après avoir exécuté `map`.)
* **Ceci est un seul mot de passe.** (Après avoir exécuté `find`.)

L'un des points forts de la programmation déclarative est qu'elle nous oblige à demander ce que nous voulons en premier. C'est dans la nomination de ces nouvelles choses que notre code devient expressif et explicite.

Et lorsque nos collègues développeurs viennent et regardent notre code, ils peuvent trouver des bugs plus facilement :

« Vous appelez cette variable 'index' ce qui me fait attendre un nombre, mais je vois qu'elle est le résultat de `filter` qui retourne un tableau. Qu'est-ce que c'est que ça ? »

![Image](https://www.freecodecamp.org/news/content/images/2020/10/women-coding-at-home-crop.jpg)

J'encourage les apprenants à écrire du code déclaratif aussi souvent que possible, en définissant constamment (et en refactorisant pour redéfinir) ce que sont les choses.

Plutôt que de garder un processus impératif entier dans votre tête, vous pouvez garder une **chose** plus tangible dans votre tête avec une définition claire.

_Mike Zetlow est l'Instructeur Principal chez [10x Code Camp](https://www.10xcodecamp.com/)._