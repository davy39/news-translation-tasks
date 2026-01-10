---
title: Algorithmes en Javascript - Recherche Binaire Expliquée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-15T09:44:40.000Z'
originalURL: https://freecodecamp.org/news/the-working-developers-guide-to-algorithms
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-19-at-15.25.42.png
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
- name: Scrimba
  slug: scrimba
seo_title: Algorithmes en Javascript - Recherche Binaire Expliquée
seo_desc: 'By Per Harald Borgen

  If you want to gain new problem-solving skills and level up your Computer Science
  knowledge, look no further than Scrimba''s free one-hour course, The Working Developer''s
  Guide To Algorithms. It was designed for those who don''t ha...'
---

Par Per Harald Borgen

Si vous souhaitez acquérir de nouvelles compétences en résolution de problèmes et améliorer vos connaissances en informatique, ne cherchez pas plus loin que le cours gratuit d'une heure de Scrimba, [Le Guide des Algorithmes pour Développeurs Actifs](https://scrimba.com/course/galgorithmsguide?utm_source=dev.to&utm_medium=referral&utm_campaign=galgorithmsguide_launch_article). Il a été conçu pour ceux qui n'ont pas de formation en informatique et qui pensent qu'ils bénéficieraient de l'apprentissage de la pensée algorithmique.

## Que fait le cours ?

Notre guide vous explique comment créer six différents algorithmes de recherche binaire. Dans le style classique de Scrimba, il contient une série de défis tout au long du parcours, afin que vous acquériez la mémoire musculaire nécessaire pour améliorer vos compétences en tant que développeur logiciel et mieux travailler avec les algorithmes à l'avenir.

Vous apprendrez :

- Recherche binaire
- Notation Big O
- Code impératif
- Récursivité
- Récursivité terminale
- Division de tableau
- Vue de tableau
- Partition

Chaque algorithme est enseigné en trois étapes :

- **Présentation** : Jonathan introduit le concept de l'algorithme.
- **Implémentation** : Nous mettons la main à la pâte en créant nos propres versions de l'algorithme.
- **Solution** : Jonathan nous montre son implémentation pour comparaison.

## Prérequis

Vous tirerez le meilleur parti de ce cours si vous avez une bonne compréhension de Javascript et si vous travaillez idéalement déjà en tant que développeur ou si vous êtes diplômé d'un Bootcamp. 

Si vous n'en êtes pas encore là, consultez les excellents tutoriels gratuits de Scrimba [Introduction à JavaScript](https://scrimba.com/course/gintrotojavascript?utm_source=dev.to&utm_medium=referral&utm_campaign=galgorithmsguide_launch_article) et [Introduction à ES6+](https://scrimba.com/course/gintrotoes6?utm_source=dev.to&utm_medium=referral&utm_campaign=galgorithmsguide_launch_article).

## Présentation de l'instructeur

Jonathan Lee Martin est un développeur logiciel, éducateur web, conférencier et auteur. Il aide d'autres développeurs à atteindre leurs objectifs professionnels et personnels à travers l'écriture, la parole, des Bootcamps immersifs, des ateliers et des tutoriels en ligne. 

Avec des clients incluant des entreprises telles que la NASA et HP, il est la personne idéale pour vous guider tout au long de ce parcours d'apprentissage. Alors, commençons !

## Recherche Binaire

[![Graphique des recherches Sweeper vs Splitter.](https://dev-to-uploads.s3.amazonaws.com/i/iphh9m8t8a0jgq94w926.png)](https://scrimba.com/p/pk57XHz/cPJqarfK?utm_source=dev.to&utm_medium=referral&utm_campaign=galgorithmsguide_launch_article)
_Cliquez sur l'image pour accéder au cours._

Dans [le premier cast](https://scrimba.com/p/pk57XHz/cPJqarfK?utm_source=dev.to&utm_medium=referral&utm_campaign=galgorithmsguide_launch_article), Jonathan introduit les concepts de **notation Big-O** et de **recherche binaire**, l'algorithme avec lequel nous allons travailler.

La **notation Big-O** est un moyen de décrire la performance dans le pire des cas d'un algorithme. Un Big O de O(n) signifie que si un tableau a une longueur de n éléments, le temps d'exécution sera proportionnel à n. En d'autres termes, un tableau de sept entrées prendra 7 recherches dans le pire des cas, tout comme un tableau de 7 millions d'entrées prendra 7 millions d'entrées dans le pire des cas. Nous pouvons également dire que le temps d'exécution de cet algorithme est linéaire, comme illustré dans le graphique ci-dessus.

La **recherche binaire** est l'une des plusieurs stratégies pour répondre à la question "Où cet élément apparaît-il dans une liste ?"

Lors de la réponse à cette question, il y a deux approches principales :

- **Sweeper** : Vérifier chaque élément de la liste jusqu'à ce que l'élément correct soit trouvé.
- **Splitter** / **Recherche Binaire** : Diviser la liste en deux, vérifier si vous êtes allé trop loin ou pas assez loin pour localiser l'élément, rechercher soit à droite soit à gauche respectivement et répéter jusqu'à ce que l'élément soit localisé.

Nous pouvons penser à ces approches en termes de vérification d'un ancien annuaire téléphonique en papier. L'approche sweeper impliquerait de parcourir chaque entrée une par une depuis le début jusqu'à ce que la bonne soit trouvée. L'approche splitter est celle que la plupart des gens utiliseraient - ouvrir le livre au hasard et voir si vous devez aller vers l'avant ou vers l'arrière jusqu'à ce que l'entrée soit localisée.

La recherche binaire est plus efficace que l'approche sweeper, particulièrement pour les listes plus grandes. Mais elle ne fonctionne que lorsque la liste a déjà été triée. 

Alors que l'approche sweeper a un temps d'exécution linéaire (voir graphique ci-dessus) et un Big O de O(n), l'approche splitter a un temps d'exécution sous-linéaire et un Big O de O(log n).

## Impératif

[Dans le premier cast de défi](https://scrimba.com/p/pk57XHz/czkBGrtD?utm_source=dev.to&utm_medium=referral&utm_campaign=galgorithmsguide_launch_article), Jonathan nous encourage à mettre la main à la pâte en implémentant la recherche binaire dans un style traditionnel, c'est-à-dire avec un Big O de O(n), en utilisant une quantité fixe de mémoire et des boucles.

Jonathan nous fournit une suite de tests que nous pouvons utiliser pour nous assurer que notre solution est réussie et nous encourage à essayer le défi nous-mêmes avant de consulter son implémentation. Pas de spoilers ici, alors rendez-vous sur le cast pour essayer par vous-même.

Bien que cette solution soit courte et proche de la formulation originale de la recherche binaire, vous avez probablement remarqué que la solution était difficile à écrire et pas la meilleure solution d'un point de vue artisanat logiciel. Continuez à lire pour découvrir des moyens d'améliorer la solution...

## Récursivité

[Dans ce cast](https://scrimba.com/p/pk57XHz/c2Pr87c4?utm_source=dev.to&utm_medium=referral&utm_campaign=galgorithmsguide_launch_article), nous examinons l'amélioration de notre recherche binaire en implémentant une nouvelle version avec quelques contraintes. Bien que notre solution doive encore avoir un Big O de O(n), elle ne doit pas utiliser de boucles et doit utiliser la récursivité. Toutes les variables doivent être initialisées avec l'opérateur `const` afin qu'elles ne puissent pas être mutées.

Jonathan nous lance avec une version squelette de la solution puis nous encourage à essayer le défi par nous-mêmes :

```js
let binarySearchWithRecursion = (array, element, compare = defaultCompare) => {
	return -1;
};

export default binarySearchWithRecursion;
```

Si vous avez complété ce défi, vous avez probablement vu que cette solution est beaucoup plus facile à lire mais assez verbeuse. Dans le pire des cas, elle peut également entraîner une récursivité infinie. Continuez avec le cours pour voir s'il existe des moyens de rationaliser la solution...

## Récursivité Terminale

Le défi pour [le prochain cast](https://scrimba.com/p/pk57XHz/ceMQgZTB?utm_source=dev.to&utm_medium=referral&utm_campaign=galgorithmsguide_launch_article) est d'améliorer notre implémentation précédente en réduisant la duplication.

Jonathan nous avertit que la solution semblera pire que les deux solutions précédentes, cependant, elle nous prépare à certaines optimisations meilleures plus loin. Rendez-vous sur le cours maintenant pour essayer le défi par vous-même et voir la solution de Jonathan.

## Division de Tableau

Si vous avez complété le défi précédent, vous avez peut-être senti que nous passons encore beaucoup d'informations supplémentaires dans notre recherche binaire via la récursivité. [Ce cast](https://scrimba.com/p/pk57XHz/cEKyndHw?utm_source=dev.to&utm_medium=referral&utm_campaign=galgorithmsguide_launch_article) examine une manière de nettoyer cela appelée **division de tableau**.

Nous pouvons penser à la division de tableau en termes de notre exemple d'annuaire téléphonique précédent - chaque fois que nous décidons que la moitié de l'annuaire est irrelevante, nous la déchirons simplement et la jetons. De même, notre prochaine solution devrait ignorer toutes les parties du tableau qui n'incluent pas notre entrée souhaitée.

Pour nous aider à atteindre cet objectif, Jonathan nous lance avec un peu de code squelette :

```js
let binarySearchWithArraySplitting = (
	array,
	element,
	compare = defaultCompare
) => {
	return -1;
};
```

Ensuite, comme d'habitude, il nous donne carte blanche pour essayer la solution par nous-mêmes avant de nous guider à travers sa propre implémentation.

Bien que ce soit une méthode élégante de recherche binaire, parce qu'elle implique de faire une copie d'une partie du tableau, elle n'a plus un Big O de O(n) et a une utilisation de mémoire plus élevée et un temps d'exécution plus lent. Continuez avec le cours pour découvrir s'il existe un moyen de retrouver une performance plus élevée avec une solution de code similaire...

## Vue de Tableau

[Dans ce cast](https://scrimba.com/p/pk57XHz/cmdvdnhb?utm_source=dev.to&utm_medium=referral&utm_campaign=galgorithmsguide_launch_article), nous cherchons des moyens de fusionner la performance plus élevée de nos solutions précédentes avec l'élégance de la division de tableau. Pour ce faire, nous créons un objet de type tableau qui répond aux mêmes méthodes qu'un tableau. Nous allons ensuite injecter cet objet à la place du tableau original.

Jonathan nous lance en initialisant une fonction `ArrayView` qui retourne un objet qui attend trois arguments : `array`, `start` et `end`. Lorsqu'elle est invoquée, `ArrayView` doit retourner un objet avec quatre méthodes, `length`, `toArray`, `slice` et `get`.

```js
export let ArrayView = (
    array,
    start = 0,
    end = array.length,
) => ({
    length: end - start,
    toArray: () => array.slice(start, end),
    slice: () => ,
    get: () => ,
});

let binarySearchWithArrayView = (array, ...args) =>
    binarySearchWithArraySplitting(ArrayView(array), ...args)
```

Notre défi est d'implémenter les méthodes `slice` et `get` de `ArrayView` sans faire de copie du tableau original. Cliquez pour essayer et puis voir la présentation de Jonathan.

Bien que cette solution produise un meilleur code, plus lisible, elle est plus longue que certaines de nos solutions précédentes. Continuez avec le cours pour voir si nous pouvons conserver les avantages de `ArrayView` tout en soulevant encore plus de logique du code de recherche binaire...

## Partition de Tableau

Dans [le dernier cast de défi](https://scrimba.com/p/pk57XHz/c8rZqEsV?utm_source=dev.to&utm_medium=referral&utm_campaign=galgorithmsguide_launch_article) du cours, Jonathan nous donne pour objectif d'extraire une partie de la logique de rebond cryptique de notre version précédente dans une structure de données.

Pour cela, nous avons besoin d'une structure de données simple qui retourne la partie centrale, gauche ou droite d'un tableau. Pour nous lancer, Jonathan met en place une fonction `ArrayPartition` :

```js
export let ArrayPartition = (array, pivot) => ({
	left: () => array.slice(0, pivot),
	middle: () => array.get(pivot),
	right: () => array.slice(pivot + 1, array.length),
});
```

Ensuite, Jonathan met en place une nouvelle version de la recherche binaire appelée `binarySearchWithPartition`, qui a une signature de départ identique à `binarySearchWithArraySplitting` :

```js
let binarySearchWithPartition = (array, element, compare = defaultCompare) => {
	if (array.length === 0) {
		return -1;
	}
	const middle = Math.floor(array.length / 2);
	const comparison = compare(element, array.get(middle));

	if (comparison === 0) {
		return middle;
	}

	//logique de rebond
	const [left, right] =
		comparison === -1 ? [0, middle - 1] : [middle + 1, array.length];
	//fin de la logique de rebond

	const subIndex = binarySearchWithArraySplitting(
		array.slice(left, right),
		element,
		compare
	);

	return subIndex === -1 ? -1 : left + subIndex;
};

let binarySearchWithPartitionAndView = (array, ...args) =>
	binarySearchWithPartition(ArrayView(array), ...args);
```

Notre défi maintenant est de réécrire `binarySearchWithPartition` sans aucune de la logique de `rebond` mise en évidence ci-dessus, au lieu de créer une partition de tableau et de faire des appels à ses méthodes left, middle et right.

Rendez-vous sur le cours maintenant pour essayer le défi par vous-même. Comme le souligne Jonathan, ce défi est délicat, donc il est acceptable de passer à sa solution si vous êtes bloqué trop longtemps, mais essayez d'abord par vous-même.

## Conclusion

Vous êtes arrivé à la fin du cours - excellent travail ! Nous avons couvert plusieurs approches de la recherche binaire, chacune avec ses propres avantages et inconvénients, et nous avons construit une excellente mémoire musculaire pour travailler efficacement avec les algorithmes. 

Maintenant que vous avez vu six approches différentes de la recherche binaire, vous remarquerez probablement qu'elle apparaît dans de nombreux endroits différents en programmation.

Le cours complet de Jonathan présentant 10 algorithmes sortira à la fin de l'année, mais en attendant, j'espère que vous pourrez mettre à profit vos nouvelles compétences en recherche binaire.

Bon codage :)

%[https://www.youtube.com/watch?v=v684EuCrPAM]