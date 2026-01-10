---
title: Comment écrire du code JavaScript plus propre avec l'opérateur ternaire
subtitle: ''
author: Oluwadamisi Samuel
co_authors: []
series: null
date: '2024-10-25T16:23:29.878Z'
originalURL: https://freecodecamp.org/news/write-cleaner-javascript-code-with-the-ternary-operator
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1729865186546/5c28c610-6540-4363-814d-c3c0c532be69.png
tags:
- name: Programming Tips
  slug: programming-tips
- name: Beginner Developers
  slug: beginners
- name: JavaScript
  slug: javascript
- name: coding
  slug: coding
seo_title: Comment écrire du code JavaScript plus propre avec l'opérateur ternaire
seo_desc: When you're coding in JavaScript, handling decisions through conditional
  statements is one of the core tasks you'll frequently encounter. One of the most
  commonly used methods for this is the ternary operator. But what exactly is it,
  and when should ...
---

Lorsque vous codez en JavaScript, la gestion des décisions par le biais d'instructions conditionnelles est l'une des tâches principales que vous rencontrerez fréquemment. L'une des méthodes les plus couramment utilisées pour cela est l'opérateur ternaire. Mais qu'est-ce que c'est exactement, et quand devez-vous l'utiliser plutôt que l'instruction if-else traditionnelle ?

Dans cet article, nous allons plonger dans l'opérateur ternaire, son fonctionnement et quand il est le bon choix par rapport à d'autres structures conditionnelles.

## Table des matières

* [Qu'est-ce que l'opérateur ternaire ?](#heading-quest-ce-que-loperateur-ternaire)
    
* [L'opérateur ternaire vs if-else](#heading-loperateur-ternaire-vs-if-else)
    
* [Opérateurs ternaires imbriqués (et pourquoi les éviter)](#heading-operateurs-ternaires-imbriques-et-pourquoi-les-eviter)
    
* [L'opérateur ternaire vs switch](#heading-loperateur-ternaire-vs-switch)
    
* [Cas d'utilisation exemple pour l'opérateur ternaire](#heading-cas-dutilisation-exemple-pour-loperateur-ternaire)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce que l'opérateur ternaire ?

L'opérateur ternaire est une manière abrégée d'écrire des instructions conditionnelles en JavaScript. Il vous permet d'exécuter l'une des deux expressions en fonction d'une condition, le tout en une seule ligne. Bien que cela puisse sembler compliqué, sa syntaxe est simple et intuitive une fois que vous comprenez comment il fonctionne.

Voici la structure de base :

```javascript
condition ? expressionSiVrai : expressionSiFaux; 
```

En termes simples, si la `condition` est évaluée à vrai, `expressionSiVrai` sera exécutée. Si elle est évaluée à faux, `expressionSiFaux` sera exécutée. L'opérateur ternaire tire son nom du fait qu'il implique trois parties : une condition, une expression vraie et une expression fausse.

## Comment utiliser l'opérateur ternaire

Commençons par un exemple de base :

```javascript
let age = 18;

let peutVoter = age >= 18 ? 'Oui' : 'Non';

console.log(peutVoter);  // Sortie : "Oui"
```

Dans cet exemple, l'opérateur ternaire vérifie si l'`age` est supérieur ou égal à 18. Si c'est le cas, la variable `peutVoter` est définie sur `'Oui'` - sinon, elle est définie sur `'Non'`. C'est une alternative concise à la structure if-else plus traditionnelle.

## L'opérateur ternaire vs `if-else`

L'opérateur ternaire est souvent utilisé comme raccourci pour les instructions `if-else` lorsque la condition est simple et peut être exprimée clairement en une ligne. Voyons comment une instruction if-else gérerait la même logique que dans l'exemple précédent :

```javascript
let age = 18;
let peutVoter;

if (age >= 18) {
  peutVoter = 'Oui';
} else {
  peutVoter = 'Non';
}

console.log(peutVoter);  // Sortie : "Oui"
```

### Quelle est la différence entre l'opérateur ternaire et if-else ?

* **Concisité** : L'opérateur ternaire est significativement plus court, car il vous permet d'écrire des conditionnelles en une seule ligne. Cela peut rendre votre code plus propre et plus facile à lire dans certains scénarios.
    
* **Lisibilité** : gardez à l'esprit que la lisibilité peut en souffrir si la condition ou les expressions deviennent trop complexes. Si vous traitez avec plusieurs conditions ou des expressions longues, l'opérateur ternaire peut rendre le code plus difficile à comprendre. L'instruction if-else traditionnelle est plus propre et un meilleur choix dans ce cas.
    

### Ternaire vs if-else : lequel est le meilleur ?

Utilisez l'opérateur ternaire lorsque vous devez prendre une décision rapide et simple dans votre code. Évitez de l'utiliser si la condition ou les expressions sont complexes. Dans ces cas, if-else est généralement un meilleur choix pour la clarté.

### Opérateurs ternaires imbriqués (et pourquoi les éviter)

Un piège courant lors de l'utilisation de l'opérateur ternaire est de les imbriquer. Bien qu'il soit possible d'imbriquer des opérateurs ternaires, cela peut rapidement conduire à un code difficile à lire et à maintenir.

Voici un exemple d'opérateur ternaire imbriqué :

```javascript
let score = 85;

let note = score >= 90 ? 'A' : score >= 80 ? 'B' : 'C';

console.log(note);  // Sortie : "B"
```

Bien que ce code fonctionne, il n'est pas aussi lisible qu'il pourrait l'être. Votre code devient rapidement désordonné, et lors de la collaboration sur un projet avec d'autres membres de l'équipe, cela peut devenir un problème si votre code n'est pas lisible.

### Comment refactoriser les opérateurs ternaires imbriqués

Au lieu d'imbriquer des opérateurs ternaires, il est souvent préférable d'utiliser une structure if-else ou d'employer une autre approche comme une instruction switch s'il y a plusieurs conditions.

Voici comment la logique ci-dessus serait avec `if-else` :

```javascript
let score = 85;
let note;

if (score >= 90) {
  note = 'A';
} else if (score >= 80) {
  note = 'B';
} else {
  note = 'C';
}

console.log(note); 
// Sortie : "B"
```

Cette version est beaucoup plus facile à lire et à maintenir, surtout si vous avez des conditions supplémentaires à vérifier.

## Opérateur ternaire vs `switch`

Bien que l'`opérateur ternaire` et les `instructions if-else` gèrent bien la logique conditionnelle, il arrive que vous deviez comparer une seule variable à de nombreuses valeurs ou résultats possibles. Dans ce cas, l'instruction `switch` est votre meilleur choix.

### Comment utiliser l'instruction Switch

Nous utilisons `switch` lorsqu'il y a plusieurs valeurs possibles pour une variable. L'opérateur `ternaire` est idéal pour des vérifications simples vrai/faux, mais `switch` facilite la gestion de plusieurs options.

```javascript
let jour = 3;
let nomJour;

switch (jour) {
  case 1:
    nomJour = 'Lundi';
    break;
  case 2:
    nomJour = 'Mardi';
    break;
  case 3:
    nomJour = 'Mercredi';
    break;
  default:
    nomJour = 'Inconnu';
}

console.log(nomJour);
// Sortie : "Mercredi"
```

Dans ce code :

1. Nous définissons `jour` à 3. L'objectif est de faire correspondre ce nombre à un jour de la semaine.
    
2. Nous utilisons une instruction `switch` pour vérifier la valeur de `jour` :
    
    * Si `jour` est 1, il attribue `'Lundi'` à `nomJour` et `break` quitte le bloc `switch`.
        
    * Si `jour` est 2, il attribue `'Mardi'` à nomJour et `break` quitte le bloc `switch`..
        
    * Si jour est 3, il attribue 'Mercredi' à nomJour et `break` quitte le bloc `switch`
        
3. Si `jour` n'est pas 1, 2 ou 3, le cas `default` s'exécute, définissant `nomJour` sur `'Inconnu'`. Puisque `jour` est 3 dans cet exemple, `nomJour` est défini sur `'Mercredi'`, et c'est ce qui est imprimé.
    

### Quand utiliser switch au lieu de ternaire

* **Conditions multiples** : Si vous vérifiez plusieurs valeurs possibles pour une seule variable, `switch` est plus approprié qu'un opérateur ternaire ou `if-else`.
    
* **Lisibilité** : L'instruction `switch` organise la logique conditionnelle complexe de manière lisible, alors que tenter d'atteindre le même résultat avec des opérateurs ternaires serait fastidieux et difficile à maintenir.
    

### Considérations de performance

D'un point de vue performance, il y a peu de différence entre l'utilisation d'un opérateur ternaire et d'une instruction if-else. Les moteurs JavaScript sont optimisés pour gérer les deux efficacement.

La véritable préoccupation est la clarté et la maintenabilité du code. Si votre opérateur ternaire rend le code plus difficile à lire, le léger gain de performance (s'il y en a) n'en vaudra pas la peine.

## Cas d'utilisation exemple pour l'opérateur ternaire

Dans les frameworks JavaScript modernes comme React, l'opérateur ternaire est souvent utilisé pour le rendu conditionnel. Voici un exemple :

```javascript
const estConnecte = true;

return (
  <div>
    {estConnecte ? <p>Bienvenue à nouveau !</p> : <p>Veuillez vous connecter.</p>}
  </div>
);
```

Cela rend le code concis et lisible, surtout lorsqu'il s'agit de la logique de rendu de l'interface utilisateur où une décision simple doit être prise en fonction d'un état ou d'une propriété.

## Conclusion

L'opérateur `ternaire` est un outil puissant en JavaScript, vous permettant d'écrire des conditionnelles concises et claires. Cependant, ce n'est pas toujours la meilleure option. Si vos conditions sont complexes ou si la lisibilité est en jeu, il est préférable de rester avec les instructions `if-else` ou même une instruction `switch`.

Points clés à retenir :

* Utilisez l'opérateur `ternaire` pour des conditionnelles simples, en une ligne.
    
* Évitez d'imbriquer les opérateurs ternaires pour garder votre code lisible.
    
* Pour des conditions complexes ou des vérifications multiples, `if-else` ou `switch` sont de meilleurs choix.
    

Avec la pratique, vous aurez une idée de quand l'opérateur `ternaire` a du sens, vous aidant à écrire du code JavaScript plus propre et plus efficace.

Connectez-vous avec moi sur [LinkedIn](https://www.linkedin.com/in/samuel-oluwadamisi-01b3a4236/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3BxAUJMbSgQTeDtb7n2d0mQQ%3D%3D) et [Twitter](https://twitter.com/Data_Steve_) si vous avez trouvé cela utile.