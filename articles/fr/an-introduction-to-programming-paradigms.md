---
title: Paradigmes de programmation – Exemples de paradigmes pour débutants
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2022-05-02T16:42:37.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-programming-paradigms
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/anne-nygard-OJzEnupZWGM-unsplash.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: Functional Programming
  slug: functional-programming
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: General Programming
  slug: programming
seo_title: Paradigmes de programmation – Exemples de paradigmes pour débutants
seo_desc: 'Hi everyone! In this article we''re going to take a look at programming
  paradigms, a fancy title to describe popular ways or styles to organize your programming.

  I''ll try to break it down in pieces and give a simple explanation of each paradigm.
  This ...'
---

Bonjour à tous ! Dans cet article, nous allons examiner les paradigmes de programmation, un titre sophistiqué pour décrire les méthodes ou styles populaires d'organisation de votre programmation.

Je vais essayer de le décomposer en morceaux et donner une explication simple de chaque paradigme. Ainsi, vous pourrez comprendre de quoi parlent les gens lorsqu'ils disent "orienté objet", "fonctionnel" ou "déclaratif".

Ce sera une introduction théorique superficielle et brève plus que tout autre chose, bien que nous allons également voir quelques exemples de pseudo-code et de code.

Je prévois d'explorer chaque paradigme en profondeur avec des exemples pratiques en JavaScript à l'avenir, alors suivez-moi (liens en bas de page) si vous êtes intéressé par ce type d'article. ;)

C'est parti !

## Table des matières

* [Qu'est-ce qu'un paradigme de programmation](#heading-qu-est-ce-qu-un-paradigme-de-programmation)
    
* [Ce qu'un paradigme de programmation n'est pas](#heading-ce-qu-un-paradigme-de-programmation-n-est-pas)
    
* [Pourquoi devrais-je m'en soucier ?](#heading-pourquoi-devrais-je-m-en-soucier)
    
* [Paradigmes de programmation populaires](#heading-paradigmes-de-programmation-populaires)
    
    * [Programmation impérative](#heading-programmation-imperative)
        
    * [Programmation procédurale](#heading-programmation-procedurale)
        
    * [Programmation fonctionnelle](#heading-programmation-fonctionnelle)
        
    * [Programmation déclarative](#heading-programmation-declarative)
        
    * [Programmation orientée objet](#heading-programmation-orientee-objet)
        
* [Résumé](#heading-resume)
    

# Qu'est-ce qu'un paradigme de programmation ?

Les paradigmes de programmation sont différentes façons ou styles dans lesquels un programme ou un langage de programmation donné peut être organisé. Chaque paradigme se compose de certaines structures, fonctionnalités et opinions sur la manière dont les problèmes de programmation courants doivent être abordés.

La question de savoir pourquoi il existe de nombreux paradigmes de programmation différents est similaire à celle de savoir pourquoi il existe de nombreux langages de programmation. Certains paradigmes sont mieux adaptés à certains types de problèmes, il est donc logique d'utiliser différents paradigmes pour différents types de projets.

De plus, les pratiques qui constituent chaque paradigme se sont développées au fil du temps. Grâce aux avancées tant logicielles que matérielles, différentes approches ont vu le jour qui n'existaient pas auparavant.

Et enfin, je pense qu'il y a la créativité humaine. En tant qu'espèce, nous aimons simplement créer des choses, améliorer ce que les autres ont construit dans le passé, et adapter les outils à nos préférences ou à ce qui nous semble plus efficace.

Tout cela aboutit au fait qu'aujourd'hui nous avons de nombreuses options à choisir lorsque nous voulons écrire et structurer un programme donné. 🤘

# Ce qu'un paradigme de programmation n'est pas

Les paradigmes de programmation ne sont pas des langages ou des outils. Vous ne pouvez pas "construire" quoi que ce soit avec un paradigme. Ils sont plutôt comme un ensemble d'idéaux et de directives sur lesquels de nombreuses personnes se sont mises d'accord, suivies et développées.

Les langages de programmation ne sont pas toujours liés à un paradigme spécifique. Il existe des langages qui ont été construits avec un certain paradigme à l'esprit et qui ont des fonctionnalités qui facilitent ce type de programmation plus que d'autres ([Haskel](https://www.haskell.org/) et la programmation fonctionnelle en est un bon exemple).

Mais il existe également des langages "multi-paradigmes", ce qui signifie que vous pouvez adapter votre code pour qu'il corresponde à un certain paradigme ou à un autre (JavaScript et Python sont de bons exemples).

En même temps, les paradigmes de programmation ne sont pas mutuellement exclusifs, dans le sens où vous pourriez utiliser des pratiques de différents paradigmes en même temps sans aucun problème.

# Pourquoi devrais-je m'en soucier ?

![Image](https://www.freecodecamp.org/news/content/images/2022/04/whatever-yeah-1.gif align="left")

Réponse courte : culture générale.

Réponse longue : Je trouve intéressant de comprendre les nombreuses façons dont la programmation peut être faite. Explorer ces sujets est un bon moyen d'ouvrir votre esprit et de vous aider à penser en dehors des sentiers battus et en dehors des outils que vous connaissez déjà.

De plus, ces termes sont beaucoup utilisés dans le monde de la programmation, donc avoir une compréhension de base vous aidera à mieux comprendre d'autres sujets également.

# Paradigmes de programmation populaires

Maintenant que nous avons introduit ce que sont et ne sont pas les paradigmes de programmation, passons en revue les plus populaires, expliquons leurs principales caractéristiques et comparons-les.

Gardez à l'esprit que cette liste n'est pas exhaustive. Il existe d'autres paradigmes de programmation non couverts ici, bien que je vais couvrir les plus populaires et les plus largement utilisés.

## Programmation impérative

La programmation impérative consiste en des ensembles d'instructions détaillées qui sont données à l'ordinateur pour qu'il les exécute dans un ordre donné. Elle est appelée "impérative" parce qu'en tant que programmeurs, nous dictons exactement ce que l'ordinateur doit faire, de manière très spécifique.

La programmation impérative se concentre sur la description de *comment* un programme fonctionne, étape par étape.

Disons que vous voulez cuire un gâteau. Votre programme impératif pour le faire pourrait ressembler à ceci (je ne suis pas un grand cuisinier, alors ne me jugez pas 😲) :

```plaintext
1- Verser de la farine dans un bol
2- Verser un couple d'œufs dans le même bol
3- Verser un peu de lait dans le même bol
4- Mélanger les ingrédients
5- Verser le mélange dans un moule
6- Cuire pendant 35 minutes
7- Laisser refroidir
```

En utilisant un exemple de code réel, disons que nous voulons filtrer un tableau de nombres pour ne garder que les éléments plus grands que 5. Notre code impératif pourrait ressembler à ceci :

```javascript
const nums = [1,4,3,6,7,8,9,2]
const result = []

for (let i = 0; i < nums.length; i++) {
    if (nums[i] > 5) result.push(nums[i])
}

console.log(result) // Sortie : [ 6, 7, 8, 9 ]
```

Voyez que nous disons au programme d'itérer à travers chaque élément du tableau, de comparer la valeur de l'élément avec 5, et si l'élément est plus grand que 5, de le pousser dans un tableau.

Nous sommes détaillés et spécifiques dans nos instructions, et c'est ce que représente la programmation impérative.

## Programmation procédurale

La programmation procédurale est une dérivation de la programmation impérative, ajoutant à celle-ci la fonctionnalité des fonctions (également connues sous le nom de "procédures" ou "sous-routines").

Dans la programmation procédurale, l'utilisateur est encouragé à subdiviser l'exécution du programme en fonctions, comme moyen d'améliorer la modularité et l'organisation.

En suivant notre exemple de gâteau, la programmation procédurale pourrait ressembler à ceci :

```plaintext
function verserIngredients() {
    - Verser de la farine dans un bol
    - Verser un couple d'œufs dans le même bol
    - Verser un peu de lait dans le même bol
}

function melangerEtTransfereDansMoule() {
    - Mélanger les ingrédients
    - Verser le mélange dans un moule
}

function cuireEtLaisserRefroidir() {
    - Cuire pendant 35 minutes
    - Laisser refroidir
}

verserIngredients()
melangerEtTransfereDansMoule()
cuireEtLaisserRefroidir()
```

Vous pouvez voir que, grâce à la mise en œuvre des fonctions, nous pourrions simplement lire les trois appels de fonctions à la fin du fichier et avoir une bonne idée de ce que fait notre programme.

Cette simplification et cette abstraction sont l'un des avantages de la programmation procédurale. Mais à l'intérieur des fonctions, nous avons toujours le même vieux code impératif.

## Programmation fonctionnelle

La programmation fonctionnelle pousse le concept de fonctions un peu plus loin.

Dans la programmation fonctionnelle, les fonctions sont traitées comme des **citoyens de première classe**, ce qui signifie qu'elles peuvent être assignées à des variables, passées en arguments et retournées par d'autres fonctions.

Un autre concept clé est l'idée de **fonctions pures**. Une fonction **pure** est une fonction qui ne dépend que de ses entrées pour générer son résultat. Et étant donné la même entrée, elle produira toujours le même résultat. De plus, elle ne produit aucun effet de bord (tout changement en dehors de l'environnement de la fonction).

Avec ces concepts à l'esprit, la programmation fonctionnelle encourage les programmes écrits principalement avec des fonctions (surprise 😲). Elle défend également l'idée que la modularité du code et l'absence d'effets de bord facilitent l'identification et la séparation des responsabilités au sein de la base de code. Cela améliore donc la maintenabilité du code.

En revenant à l'exemple de filtrage de tableau, nous pouvons voir qu'avec le paradigme impératif, nous pourrions utiliser une variable externe pour stocker le résultat de la fonction, ce qui peut être considéré comme un effet de bord.

```javascript
const nums = [1,4,3,6,7,8,9,2]
const result = [] // Variable externe

for (let i = 0; i < nums.length; i++) {
    if (nums[i] > 5) result.push(nums[i])
}

console.log(result) // Sortie : [ 6, 7, 8, 9 ]
```

Pour transformer cela en programmation fonctionnelle, nous pourrions le faire comme ceci :

```javascript
const nums = [1,4,3,6,7,8,9,2]

function filterNums() {
    const result = [] // Variable interne

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > 5) result.push(nums[i])
    }

    return result
}

console.log(filterNums()) // Sortie : [ 6, 7, 8, 9 ]
```

C'est presque le même code, mais nous enveloppons notre itération dans une fonction, dans laquelle nous stockons également le tableau de résultats. De cette manière, nous pouvons nous assurer que la fonction ne modifie rien en dehors de sa portée. Elle ne crée qu'une variable pour traiter ses propres informations, et une fois l'exécution terminée, la variable disparaît également.

## Programmation déclarative

La programmation déclarative consiste à cacher la complexité et à rapprocher les langages de programmation du langage et de la pensée humains. C'est l'opposé direct de la programmation impérative dans le sens où le programmeur ne donne pas d'instructions sur *comment* l'ordinateur doit exécuter la tâche, mais plutôt sur *quel* résultat est nécessaire.

Cela sera beaucoup plus clair avec un exemple. En suivant la même histoire de filtrage de tableau, une approche déclarative pourrait être :

```javascript
const nums = [1,4,3,6,7,8,9,2]

console.log(nums.filter(num => num > 5)) // Sortie : [ 6, 7, 8, 9 ]
```

Voyez que avec la fonction filter, nous ne disons pas explicitement à l'ordinateur d'itérer sur le tableau ou de stocker les valeurs dans un tableau séparé. Nous disons simplement ce que nous voulons ("filter") et la condition à remplir ("num > 5").

Ce qui est bien avec cela, c'est que c'est plus facile à lire et à comprendre, et souvent plus court à écrire. Les fonctions `filter`, `map`, `reduce` et `sort` de JavaScript sont de bons exemples de code déclaratif.

Un autre bon exemple sont les frameworks/bibliothèques JS modernes comme React. Prenez ce code par exemple :

```javascript
<button onClick={() => console.log('Vous avez cliqué sur moi !')}>Cliquez sur moi</button>
```

Ici, nous avons un élément bouton, avec un écouteur d'événement qui déclenche une fonction console.log lorsque le bouton est cliqué.

La syntaxe JSX (ce que React utilise) mélange HTML et JS dans la même chose, ce qui la rend plus facile et plus rapide à écrire des applications. Mais ce n'est pas ce que les navigateurs lisent et exécutent. Le code React est ensuite transpilé en HTML et JS réguliers, et c'est ce que les navigateurs exécutent en réalité.

JSX est déclaratif, dans le sens où son but est de donner aux développeurs une interface plus conviviale et plus efficace pour travailler.

Une chose importante à noter sur la programmation déclarative est que sous le capot, l'ordinateur traite ces informations comme du code impératif de toute façon.

En suivant l'exemple du tableau, l'ordinateur itère toujours sur le tableau comme dans une boucle for, mais en tant que programmeurs, nous n'avons pas besoin de coder cela directement. Ce que fait la programmation déclarative, c'est **cacher** cette complexité de la vue directe du programmeur.

Voici une belle [comparaison entre la programmation impérative et déclarative](https://www.youtube.com/watch?v=E7Fbf7R3x6I).

## Programmation orientée objet

L'un des paradigmes de programmation les plus populaires est la programmation orientée objet (POO).

Le concept central de la POO est de séparer les préoccupations en entités qui sont codées comme des objets. Chaque entité regroupera un ensemble donné d'informations (propriétés) et d'actions (méthodes) qui peuvent être effectuées par l'entité.

La POO fait un usage intensif des classes (qui sont un moyen de créer de nouveaux objets à partir d'un modèle ou d'un modèle que le programmeur définit). Les objets qui sont créés à partir d'une classe sont appelés instances.

En suivant notre exemple de pseudo-code de cuisine, disons maintenant que dans notre boulangerie nous avons un cuisinier principal (appelé Frank) et un cuisinier assistant (appelé Anthony) et chacun d'eux aura certaines responsabilités dans le processus de cuisson. Si nous utilisions la POO, notre programme pourrait ressembler à ceci.

```plaintext
// Créer les deux classes correspondant à chaque entité
class Cuisinier {
	constructor constructor (nom) {
        this.nom = nom
    }

    melangerEtCuire() {
        - Mélanger les ingrédients
    	- Verser le mélange dans un moule
        - Cuire pendant 35 minutes
    }
}

class AssistantCuisinier {
    constructor (nom) {
        this.nom = nom
    }

    verserIngredients() {
        - Verser de la farine dans un bol
        - Verser un couple d'œufs dans le même bol
        - Verser un peu de lait dans le même bol
    }
    
    laisserRefroidirLeGateau() {
    	- Laisser refroidir
    }
}

// Instancier un objet à partir de chaque classe
const Frank = new Cuisinier('Frank')
const Anthony = new AssistantCuisinier('Anthony')

// Appeler les méthodes correspondantes à partir de chaque instance
Anthony.verserIngredients()
Frank.melangerEtCuire()
Anthony.laisserRefroidirLeGateau()
```

Ce qui est bien avec la POO, c'est qu'elle facilite la compréhension d'un programme, grâce à la séparation claire des préoccupations et des responsabilités.

Dans cet exemple, je n'ai fait qu'effleurer la surface des nombreuses fonctionnalités de la POO. Si vous souhaitez en savoir plus, voici deux excellentes vidéos expliquant les bases de la POO :

* [Vidéo POO 1](https://www.youtube.com/watch?v=cg1xvFy1JQQ)
    
* [Vidéo POO 2](https://www.youtube.com/watch?v=pTB0EiLXUC8)
    

Et [voici une belle comparaison entre la programmation impérative, fonctionnelle et orientée objet](https://www.youtube.com/watch?v=08CWw_VD45w).

## Résumé

Comme nous l'avons vu, les paradigmes de programmation sont différentes façons d'aborder les problèmes de programmation et d'organiser notre code.

Les paradigmes impératif, procédural, fonctionnel, déclaratif et orienté objet sont certains des paradigmes les plus populaires et largement utilisés aujourd'hui. Et connaître les bases à leur sujet est bon pour la culture générale et également pour mieux comprendre d'autres sujets du monde de la programmation.

Comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau. Si vous le souhaitez, vous pouvez également me suivre sur [linkedin](https://www.linkedin.com/in/germancocca/) ou [twitter](https://twitter.com/CoccaGerman).

À bientôt et à la prochaine ! =D

![Image](https://www.freecodecamp.org/news/content/images/2022/04/200.gif align="left")