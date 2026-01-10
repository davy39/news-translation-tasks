---
title: Comment fonctionnent les interfaces TypeScript – Expliqué avec des exemples
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-02-23T10:59:53.000Z'
originalURL: https://freecodecamp.org/news/how-typescript-interfaces-work
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Copy-of-Neon-Green-Bold-Quote-Motivational-Tweet-Instagram-Post-2--1.png
tags:
- name: TypeScript
  slug: typescript
seo_title: Comment fonctionnent les interfaces TypeScript – Expliqué avec des exemples
seo_desc: 'TypeScript, a superset of JavaScript, has gained widespread adoption among
  developers due to its ability to provide static typing, enhancing code robustness
  and maintainability.

  One of TypeScript''s key features is interfaces, which play a pivotal rol...'
---

TypeScript, un sur-ensemble de JavaScript, a gagné en adoption parmi les développeurs grâce à sa capacité à fournir une typisation statique, améliorant ainsi la robustesse et la maintenabilité du code.

L'une des fonctionnalités clés de TypeScript est les interfaces, qui jouent un rôle pivot dans la définition de la structure des objets, permettant la vérification des types et facilitant une meilleure organisation du code. Dans cet article, nous allons approfondir les interfaces TypeScript, en explorant leur syntaxe et leurs cas d'utilisation.

Vous pouvez obtenir tout le code source à partir d'[ici](https://github.com/dotslashbit/fcc-article-resources/blob/main/ts-interfaces/index.ts).

## Qu'est-ce que les interfaces TypeScript ?

À sa base, une interface en TypeScript est un contrat syntaxique qui définit la structure attendue d'un objet. Elle fournit un moyen de décrire la forme des objets, y compris leurs propriétés et méthodes, sans implémenter de fonctionnalité. Les interfaces se concentrent uniquement sur la structure et les aspects de vérification de type, permettant une meilleure compréhension et validation du code pendant le développement.

## Syntaxe des interfaces TypeScript

La syntaxe d'une interface TypeScript est simple :

```typescript
interface NomInterface {
    propriete1: type;
    propriete2: type;
    // Des propriétés et méthodes supplémentaires peuvent être définies ici
}

```

Voici une analyse des éléments de syntaxe :

* `interface` : Mot-clé utilisé pour définir une interface.
* `NomInterface` : Nom de l'interface suivant les conventions de nommage TypeScript.
* `propriete1`, `propriete2` : Propriétés de l'interface.
* `type` : Annotation de type TypeScript définissant le type de chaque propriété.

## Cas d'utilisation des interfaces TypeScript

### Comment définir des structures d'objets

Une application fondamentale des interfaces TypeScript est la définition de structures d'objets. Imaginez un scénario où vous êtes chargé de gérer diverses formes dans un projet. Ici, vous pouvez utiliser une interface pour représenter une forme géométrique générique :

```typescript
interface Forme {
  nom: string;
  couleur: string;
  aire(): number;
}

console.log("Cas d'utilisation 1 : Définition des structures d'objets");
console.log("-----------------------------------------");

// Définir une fonction pour calculer l'aire d'une forme
function calculerAire(forme: Forme): void {
  console.log(`Calcul de l'aire de ${forme.nom}...`);
  console.log(`Aire : ${forme.aire()}`);
}

// Définir un objet cercle
const cercle: Forme = {
  nom: "Cercle",
  couleur: "Rouge",
  aire() {
    return Math.PI * 2 * 2;
  },
};

// Calculer et afficher l'aire du cercle
calculerAire(cercle);

```

Sortie :

```
Cas d'utilisation 1 : Définition des structures d'objets
-----------------------------------------
Calcul de l'aire de Cercle...
Aire : 12.566370614359172

```

Dans ce cas d'utilisation, nous définissons une interface appelée `Forme` pour représenter la structure des formes géométriques. L'interface `Forme` contient les propriétés `nom` et `couleur`, toutes deux de type `string`, et une méthode `aire()` qui retourne un `number`. Nous définissons ensuite un objet cercle qui adhère à l'interface `Forme`, en spécifiant ses propriétés et en implémentant la méthode `aire()` pour calculer son aire.

### Comment vérifier les types des paramètres de fonction

Un autre rôle pivot des interfaces est la vérification des types des paramètres de fonction lors de la compilation. Considérons une fonction chargée de calculer le périmètre d'une forme :

```typescript
function calculerPerimetre(forme: Forme): number {
  // Implémentation
}

console.log("\nCas d'utilisation 2 : Vérification des types des paramètres de fonction");
console.log("----------------------------------------------");

// Tentative d'appel de la fonction avec un objet forme
console.log("Calcul du périmètre d'une forme...");
console.log(`Périmètre : ${calculerPerimetre(cercle)}`); // Erreur du compilateur : L'argument de type 'Forme' n'est pas assignable au paramètre de type 'Forme'.

```

Sortie :

```
Cas d'utilisation 2 : Vérification des types des paramètres de fonction
----------------------------------------------
Calcul du périmètre d'une forme...

```

```
Erreur : L'argument de type 'Forme' n'est pas assignable au paramètre de type 'Forme'.

```

Ici, nous démontrons comment les interfaces permettent la vérification des types des paramètres de fonction. Nous avons une fonction `calculerPerimetre()` qui prend un objet de type `Forme` comme paramètre. Lorsque nous tentons d'appeler cette fonction avec un objet `cercle`, TypeScript génère une erreur de compilation car l'objet `cercle` ne correspond pas précisément à l'interface `Forme` attendue, assurant ainsi la sécurité des types pendant le développement.

### Comment implémenter des contrats de classe

Les interfaces servent également de moyen efficace pour imposer des contrats sur les classes, garantissant qu'elles adhèrent à des propriétés et méthodes spécifiques. Illustrons cela en créant une classe `Cercle` qui implémente l'interface `Forme` :

```typescript
class Cercle implements Forme {
  constructor(public nom: string, public couleur: string, public rayon: number) {}

  aire(): number {
    return Math.PI * this.rayon * this.rayon;
  }
}

console.log("\nCas d'utilisation 3 : Implémentation des contrats de classe");
console.log("------------------------------------------");

// Créer une instance de la classe Cercle
const monCercle = new Cercle("Mon Cercle", "Bleu", 3);

// Afficher l'aire du cercle
console.log(`Aire de ${monCercle.nom} : ${monCercle.aire()}`);

```

Sortie :

```
Cas d'utilisation 3 : Implémentation des contrats de classe
------------------------------------------
Aire de Mon Cercle : 28.274333882308138

```

Ici, nous démontrons comment les interfaces permettent la vérification des types des paramètres de fonction. Nous avons une fonction `calculerPerimetre()` qui prend un objet de type `Forme` comme paramètre. Lorsque nous tentons d'appeler cette fonction avec un objet `cercle`, TypeScript génère une erreur de compilation car l'objet `cercle` ne correspond pas précisément à l'interface `Forme` attendue, assurant ainsi la sécurité des types pendant le développement.

### Comment étendre les interfaces

Les interfaces peuvent étendre d'autres interfaces, permettant la composition et la réutilisation des définitions d'interfaces. Étendons l'interface `Forme` pour inclure des propriétés supplémentaires pour les formes 3D :

```typescript
interface Forme3D extends Forme {
  volume(): number;
}

console.log("\nCas d'utilisation 4 : Extension des interfaces");
console.log("----------------------------------");

// Définir une fonction pour calculer le volume d'une forme 3D
function calculerVolume(forme: Forme3D): void {
  console.log(`Calcul du volume de ${forme.nom}...`);
  console.log(`Volume : ${forme.volume()}`);
}

// Définir une classe pour une forme 3D
class Sphere implements Forme3D {
  constructor(public nom: string, public couleur: string, public rayon: number) {}

  aire(): number {
    return 4 * Math.PI * this.rayon ** 2;
  }

  volume(): number {
    return (4 / 3) * Math.PI * this.rayon ** 3;
  }
}

// Créer une instance de la classe Sphere
const maSphere = new Sphere("Ma Sphere", "Verte", 4);

// Calculer et afficher le volume de la sphère
calculerVolume(maSphere);

```

Sortie :

```
Cas d'utilisation 4 : Extension des interfaces
----------------------------------
Calcul du volume de Ma Sphere...
Volume : 268.082573106329

```

Ici, nous démontrons comment les interfaces permettent la vérification des types des paramètres de fonction. Nous avons une fonction `calculerPerimetre()` qui prend un objet de type `Forme` comme paramètre. Lorsque nous tentons d'appeler cette fonction avec un objet `cercle`, TypeScript génère une erreur de compilation car l'objet `cercle` ne correspond pas précisément à l'interface `Forme` attendue, assurant ainsi la sécurité des types pendant le développement.

## Conclusion

En conclusion, les interfaces TypeScript se révèlent être des outils puissants pour définir des contrats au sein de votre base de code, assurant la sécurité des types et favorisant la maintenabilité du code. En utilisant les interfaces, vous pouvez établir des attentes claires pour les structures d'objets, les paramètres de fonction, les contrats de classe, et plus encore.

Que vous travailliez sur une application modeste ou un projet d'entreprise étendu, maîtriser les interfaces est indispensable pour créer un code TypeScript propre, fiable et maintenable.

Si vous avez des commentaires, envoyez-moi un message sur [Twitter](https://twitter.com/introvertedbot) ou [LinkedIn](https://www.linkedin.com/in/sahil-mahapatra/).