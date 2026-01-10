---
title: Les quatre piliers de la programmation orientée objet
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2020-12-18T17:49:25.000Z'
originalURL: https://freecodecamp.org/news/four-pillars-of-object-oriented-programming
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/The-four-pillars-of-object-orientation.png
tags:
- name: JavaScript
  slug: javascript
- name: object oriented
  slug: object-oriented
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: Les quatre piliers de la programmation orientée objet
seo_desc: 'JavaScript is a multi-paradigm language and can be written following different
  programming paradigms. A programming paradigm is essentially a bunch of rules that
  you follow when writing code, to help you solve a particular problem.

  That''s what the fo...'
---

JavaScript est un langage multi-paradigme et peut être écrit en suivant différents paradigmes de programmation. Un paradigme de programmation est essentiellement un ensemble de règles que vous suivez lors de l'écriture de code, pour vous aider à résoudre un problème particulier.

C'est ce que sont les quatre piliers. Ce sont des principes de conception logicielle pour vous aider à écrire un code orienté objet propre.

Les quatre piliers de la programmation orientée objet sont : 

* Abstraction
* Encapsulation
* Héritage
* Polymorphisme

Examinons chacun d'eux de plus près.

# L'abstraction en programmation orientée objet

Abstraire quelque chose signifie cacher les détails d'implémentation à l'intérieur de quelque chose – parfois un prototype, parfois une fonction. Ainsi, lorsque vous appelez la fonction, vous n'avez pas besoin de comprendre exactement ce qu'elle fait.

Si vous deviez comprendre chaque fonction dans une grande base de code, vous ne coderiez jamais rien. Cela prendrait des mois pour finir de tout lire.

Vous pouvez créer une base de code réutilisable, simple à comprendre et facilement modifiable en abstraant certains détails. Laissez-moi vous donner un exemple :

```javascript
function hitAPI(type){
	if (type instanceof InitialLoad) {
		// Exemple d'implémentation
	} else if (type instanceof NavBar) {
		// Exemple d'implémentation
	} else {
		// Exemple d'implémentation
	}
}
```

Pouvez-vous voir dans l'exemple comment vous devez implémenter exactement ce dont vous avez besoin pour votre cas d'utilisation personnalisé ?

Chaque nouvelle API que vous devez appeler nécessite un nouveau bloc `if`, et son propre code personnalisé. Cela n'est pas abstrait car vous devez vous soucier de l'implémentation pour chaque nouveau type que vous ajoutez. Ce n'est pas réutilisable et c'est un cauchemar de maintenance.

Que pensez-vous de quelque chose comme ci-dessous ?

```javascript
hitApi('www.kealanparr.com', HTTPMethod.Get)
```

Vous pouvez maintenant simplement passer une URL à votre fonction et la méthode HTTP que vous souhaitez utiliser et c'est tout.

Vous n'avez pas à vous soucier de la façon dont la fonction fonctionne. C'est géré. Cela aide massivement à la réutilisation du code ! Et rend votre code beaucoup plus maintenable, aussi.

C'est ce que l'**Abstraction** est tout à fait. Trouver des choses qui sont similaires dans votre code et fournir une fonction ou un objet générique pour servir plusieurs endroits/avec plusieurs préoccupations.

Voici un bon exemple final d'**Abstraction** : imaginez si vous créiez une machine à faire du café pour vos utilisateurs. Il pourrait y avoir deux approches :

## Comment la créer avec l'abstraction

* Avoir un bouton avec le titre "Faire du café"

## Comment la créer sans abstraction

* Avoir un bouton avec le titre "Faire bouillir l'eau"
* Avoir un bouton avec le titre "Ajouter l'eau froide à la bouilloire"
* Avoir un bouton avec le titre "Ajouter 1 cuillère de café moulu à une tasse propre"
* Avoir un bouton avec le titre "Nettoyer les tasses sales"
* Et tous les autres boutons

C'est un exemple très simple, mais la première approche _abstrait_ la logique dans la machine. Mais la deuxième approche force l'utilisateur à comprendre comment faire du café et essentiellement à le faire lui-même.

Le prochain pilier nous montre une façon dont nous pouvons atteindre l'**Abstraction**, en utilisant l'**Encapsulation**.

# L'encapsulation en programmation orientée objet

La définition de l'encapsulation est "l'action d'enfermer quelque chose dans ou comme si dans une capsule". Supprimer l'accès à des parties de votre code et rendre les choses privées est exactement ce que l'**Encapsulation** est tout à fait (souvent, les gens s'y réfèrent comme à la dissimulation de données).

L'encapsulation signifie que chaque objet dans votre code devrait contrôler son propre état. L'état est le "snapshot" actuel de votre objet. Les clés, les méthodes sur votre objet, les propriétés booléennes et ainsi de suite. Si vous deviez réinitialiser un booléen ou supprimer une clé de l'objet, ce sont tous des changements à votre état.

Limitez les parties de votre code qui peuvent accéder. Rendez plus de choses inaccessibles, si elles ne sont pas nécessaires.

Les propriétés privées sont réalisées en JavaScript en utilisant des fermetures. Voici un exemple ci-dessous :

```javascript
var Dog = (function () {

	// Privé
	var play = function () {
		// implémentation de play
	};
    
	// Privé
	var breed = "Dalmatian"
    
	// Public
	var name = "Rex";

	// Public
	var makeNoise = function () {
 		return 'Bark bark!';
	};

 	return {
		makeNoise: makeNoise,
		name: name
 	};
})();


```

La première chose que nous avons faite a été de créer une fonction qui est immédiatement appelée (appelée une **Expression de Fonction Invocable Immédiatement**, ou IIFE pour faire court). Cela a créé un objet que n'importe qui peut accéder mais a caché certains des détails. Vous ne pouvez pas appeler `play` et vous ne pouvez pas accéder à `breed` car nous ne l'avons pas exposé dans l'objet final avec le retour.

Ce modèle particulier ci-dessus est appelé le **Revealing Module Pattern**, mais ce n'est qu'un exemple de la façon dont vous pouvez atteindre l'**Encapsulation**.

Je veux me concentrer davantage sur l'idée de l'**Encapsulation** (car elle est plus importante que d'apprendre un seul modèle et de considérer l'**Encapsulation** comme totalement complète maintenant).

Réfléchissez et pensez davantage à la façon dont vous pouvez cacher vos données et votre code, et les séparer. La modularisation et avoir des responsabilités claires est la clé de l'**Orientation Objet**.

Pourquoi devrions-nous préférer la confidentialité ? Pourquoi ne pas simplement avoir tout global ?

* Beaucoup de morceaux de code non liés deviendront dépendants/couplés les uns aux autres via la variable globale.
* Vous risquez de remplacer les variables si le nom est réutilisé, ce qui peut entraîner des bugs ou un comportement imprévisible.
* Vous risquez de vous retrouver avec du **Code Spaghetti** – du code qui est difficile à comprendre et à suivre ce qui lit et écrit dans vos variables et change l'état.

L'encapsulation peut être appliquée en séparant les longues lignes de code en fonctions séparées plus petites. Séparez ces fonctions en modules. Nous cachons les données dans un endroit où rien d'autre n'a besoin d'accès, et exposons proprement ce qui est nécessaire.

C'est l'**Encapsulation** en un mot. Lier vos données à quelque chose, qu'il s'agisse d'une classe, d'un objet, d'un module ou d'une fonction, et faire de votre mieux pour les garder aussi privées que raisonnablement possible.

# L'héritage en programmation orientée objet

L'héritage permet à un objet d'acquérir les propriétés et méthodes d'un autre objet. En JavaScript, cela est fait par **l'héritage prototypal**. 

La réutilisabilité est le principal avantage ici. Nous savons parfois que plusieurs endroits doivent faire la même chose, et ils doivent tout faire de la même manière sauf pour une petite partie. C'est un problème que l'héritage peut résoudre.

Chaque fois que nous utilisons l'héritage, nous essayons de faire en sorte que le parent et l'enfant aient une **forte cohésion**. La cohésion est la relation de votre code. Par exemple, le type `Bird` étend-il le type `DieselEngine` ?

Gardez votre héritage simple à comprendre et prévisible. N'héritez pas d'un endroit complètement non lié parce qu'il y a une méthode ou une propriété dont vous avez besoin. L'héritage ne résout pas ce problème particulier.

Lorsque vous utilisez l'héritage, vous devriez nécessiter la plupart des fonctionnalités (vous n'avez pas toujours besoin de tout). 

Les développeurs ont un principe appelé le **principe de substitution de Liskov**. Il stipule que si vous pouvez utiliser une classe parente (appelons-la `ParentType`) partout où vous utilisez un enfant (appelons-le `ChildType`) – et `ChildType` hérite de `ParentType` – alors vous passez le test. 

La principale raison pour laquelle vous échoueriez ce test est si `ChildType` supprime des choses du parent. Si `ChildType` supprimait des méthodes qu'il a héritées du parent, cela entraînerait des `TypeError` où des choses sont indéfinies que vous ne vous attendez pas à l'être.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-146.png)
_Les flèches semblent aller dans le mauvais sens. Mais l'Animal est la base - le parent._

La chaîne d'héritage est le terme utilisé pour décrire le flux d'héritage du prototype de l'objet de base (celui dont tout le reste hérite) à la "fin" de la chaîne d'héritage (le dernier type qui hérite – **Dog** dans l'exemple ci-dessus).

Faites de votre mieux pour garder vos chaînes d'héritage propres et sensées. Vous pouvez facilement finir par coder des anti-modèles lorsque vous utilisez l'**Héritage** (appelé l'**anti-modèle de base fragile**). Cela se produit lorsque vos prototypes de base sont considérés comme "fragiles" parce que vous faites un changement "sûr" à l'objet de base et commencez ensuite à casser tous vos enfants.

# Le polymorphisme en programmation orientée objet

Le polymorphisme signifie "la condition de se produire sous plusieurs formes différentes." C'est exactement ce que le quatrième et dernier pilier concerne – les types dans les mêmes chaînes d'héritage pouvant faire différentes choses.

Si vous avez utilisé l'héritage correctement, vous pouvez maintenant utiliser les parents comme leurs enfants de manière fiable. Lorsque deux types partagent une chaîne d'héritage, ils peuvent être utilisés de manière interchangeable sans erreurs ni assertions dans votre code.

À partir du dernier diagramme, nous pourrions avoir un prototype de base qui s'appelle `Animal` qui définit `makeNoise`. Ensuite, chaque type étendant ce prototype peut remplacer pour faire son propre travail personnalisé. Quelque chose comme ceci :

```javascript
// Configurons un exemple Animal et Dog
function Animal(){}
function Dog(){}

Animal.prototype.makeNoise = function(){
	console.log("Base noise");
};

// La plupart des animaux que nous codons ont 4 pattes. Cela peut être remplacé si nécessaire
Animal.prototype.legs = 4;

Dog.prototype = new Animal();

Dog.prototype.makeNoise = function(){
	console.log("Woof woof");  
};

var animal = new Animal();
var dog = new Dog();

animal.makeNoise(); // Base noise
dog.makeNoise();    // Woof woof- cela a été remplacé
dog.legs;           // 4! Cela a été hérité
```

`Dog` étend `Animal` et peut utiliser la propriété `legs` par défaut. Mais il est également capable de faire sa propre implémentation pour faire son propre bruit.

Le vrai pouvoir du polymorphisme est de partager des comportements et de permettre des remplacements personnalisés.

# Conclusion

J'espère que cela a expliqué ce que sont les quatre piliers de la programmation orientée objet et comment ils conduisent à un code plus propre et plus robuste.

Je partage mes écrits sur [Twitter](https://twitter.com/kealanparr) si vous avez aimé cet article et voulez en voir plus.