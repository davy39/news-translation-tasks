---
title: 'Ne vous contentez pas : comment adapter votre collection JavaScript à vos
  objectifs'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-13T19:02:14.000Z'
originalURL: https://freecodecamp.org/news/dont-settle-how-you-can-match-your-javascript-collection-to-your-goals-c94cb994be4e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2kLrLgDZjAt0P_xNrM1qtg.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Ne vous contentez pas : comment adapter votre collection JavaScript à
  vos objectifs'
seo_desc: 'By Joe Morgan

  I loved JavaScript even when the world hated it. But I always had a hard time justifying
  collections. Objects are kind of a key-value store, but not really. And they were
  horrible if you needed to sort or loop. Arrays were easier to loo...'
---

Par Joe Morgan

J'aimais JavaScript même lorsque le monde le détestait. Mais j'ai toujours eu du mal à justifier les collections. Les objets sont un peu comme un magasin clé-valeur, mais pas vraiment. Et ils étaient horribles si vous deviez trier ou boucler. Les tableaux étaient plus faciles à parcourir, mais encombrants si vous deviez extraire une valeur spécifique sans index.

La triste vérité est que la plupart du temps, les développeurs attrapaient simplement la première collection qui leur venait à l'esprit. Puis la torturaient avec des conversions pour obtenir ce dont ils avaient besoin.

C'était douloureux.

Les choses sont différentes maintenant. Il y a plus de types de collections. Il y a plus de méthodes. Il y a de meilleures techniques et même des expressions en une ligne pour passer d'un type de collection à un autre. Pourquoi semble-t-il alors que nous devinons toujours lorsque nous choisissons un type de collection ?

Je parle régulièrement de [JavaScript et de la qualité du code](https://www.youtube.com/watch?v=cT7TMzZ3Cnw&list=PL_G_ImM6b7_e9WnnY1Hmy-culcW40LX1b&index=21). J'ai [écrit des livres](https://pragprog.com/book/es6tips/simplifying-javascript) sur la nouvelle syntaxe. Mais je trouve que la plupart des développeurs, même expérimentés, ne réfléchissent pas beaucoup à leur choix de collection.

Il est temps d'y mettre fin. Non seulement nous avons des tableaux et des objets. Nous avons aussi des Maps, des Sets, des WeakMaps et des WeakSets.

Alors, lequel choisir ? Chaque collection a ses avantages et ses inconvénients. Mais en général, il y a trois grands facteurs qui devraient influencer votre choix :

* **Itérable** : Pouvez-vous parcourir la collection directement et accéder à chaque membre un par un ?
* **Clé** : Pouvez-vous trouver une valeur en utilisant une clé spéciale sans vous soucier des autres membres de la collection ?
* **Destructurable** : Pouvez-vous extraire des morceaux de la collection dans des variables rapidement et facilement ?

Chaque type de collection est fort dans certains domaines et faible dans d'autres. Il y a d'autres avantages et inconvénients, mais ce sont les trois grands pour la plupart du code.

### Tableaux

Les tableaux sont probablement les collections les plus flexibles. Cela en fait un excellent point de départ pour explorer les collections.

Voici une liste de mes professeurs de l'école primaire (les noms ont été changés pour protéger les innocents).

```
const myTeachers = ['Cooper', 'Simes', 'Butler'];
```

Les tableaux préservent l'ordre, ce qui est génial puisque c'est l'ordre correct de mes professeurs de première, deuxième et troisième année. Puisque l'ordre est significatif et que je connais la signification, je peux utiliser la **destructuration** pour extraire les éléments dans des variables.

```
const [firstGrade, secondGrade, ...others] = myTeachers.
```

La destructuration est un moyen rapide d'extraire des informations d'une collection dans des variables séparées. Elle peut également créer des sous-ensembles d'informations. La variable `firstGrade` a la valeur `Cooper`. La variable suivante, `secondGrade`, est `Simes`. La dernière variable est un peu différente, en utilisant les trois points `...`, nous sauvegardons le reste des variables, une dans ce cas, comme un tableau séparé. Cela signifie que `others` est également un tableau : `['Butler']`. Dans ce cas, les `...` sont un motif de repos. Nous sauvegardons le reste des valeurs après tout.

Revenons à ma collection de professeurs. Supposons que vous ne vous souciez pas de l'ordre dans lequel ils m'ont enseigné, vous êtes plus intéressé par une liste alphabétisée. Maintenant, avant de trier le tableau, rappelez-vous, le tri est une fonction mutante, donc l'action changera le tableau original. Et puisque l'ordre compte, vous ne voulez pas faire un changement permanent. Heureusement, ce n'est pas un gros problème puisque vous pouvez créer un nouveau tableau avec l'opérateur de propagation : `[...myTeachers]`.

La raison pour laquelle vous pouvez utiliser l'opérateur de propagation est que les tableaux ont un itérateur intégré qui vous permet d'agir sur une collection un élément à la fois. En d'autres termes, les tableaux sont **itérables**. L'opérateur de propagation prend ces éléments et crée une nouvelle liste un par un. En mettant le tout entre crochets, vous créez un nouveau tableau. La propriété itérable est également ce qui vous permet de faire des choses sympas comme boucler en utilisant `for...of` ou exécuter une fonction sur chaque élément du tableau comme vous le feriez avec les méthodes `.map` et `.reduce`.

Revenons au tri. Maintenant que vous pouvez créer un nouveau tableau, vous n'avez pas à vous soucier des mutations. La fonction de tri est une ligne.

```
const sortedTeachers = [...myTeachers].sort();
```

Puisque les tableaux sont destructurables et itérables, vous pouvez extraire des informations facilement ou accéder à chaque élément un par un. Cela semble assez génial, n'est-ce pas ? Bien sûr, les tableaux ne sont pas parfaits. Supposons que vous ne connaissiez pas l'ordre du tableau, mais que vous vouliez mon professeur de deuxième année. Maintenant, vous avez un problème. Puisque les tableaux ne sont pas clés, vous ne pouvez pas simplement extraire les informations dont vous avez besoin. Le mieux que vous puissiez faire est de créer un tableau compliqué de paires — un tableau contenant deux éléments — ainsi qu'une méthode de tableau pour trouver celle que vous voulez.

```
export const myTeacherPairs = [['first', 'Cooper'], ['second', 'Simes'], ['third', 'Butler']];
```

```
return teachers.find(teacherPair => teacherPair[0] === 'second');
```

C'est un peu encombrant. Un tableau de paires est super important et vous en verrez plus tard, mais c'est une manière assez inefficace de gérer les recherches de données.

Les problèmes sont que la collection n'est pas **clé**. Les tableaux sont bons pour beaucoup de choses, mais les magasins clé-valeur ne sont pas l'un d'eux. Vous êtes donc dans une impasse. Vous aimez les propriétés de destructuration et les itérables. Mais la récupération d'informations clé-valeur n'est pas simple. C'est généralement à ce moment-là que les développeurs se tournent vers les objets. Mais avant cela, voici un résumé des tableaux :

✅ Destructurable

✅ Itérable

❌ Clé

### Objets

La plupart des développeurs JavaScript atteignent instinctivement un objet dès qu'ils ont besoin de stocker des paires clé-valeur. Les objets en JavaScript peuvent devenir assez complexes. Pour l'exemple, pensez à eux comme un moyen simple de transmettre des données. Pas de fonctions. Pas de mot-clé `this`. Juste des paires clé-valeur.

Commencez par réécrire mon tableau de professeurs en un objet :

```
const teachers = {  first: "Cooper",  second: "Simes",  third: "Butler",};
```

Si vous deviez trouver seulement mon professeur de deuxième année et que vous ne vous souciez pas des autres parties de l'objet, vous pouvez l'extraire directement : `teachers.second`. Mieux encore, vous pouvez extraire la valeur directement dans une variable avec la destructuration. C'est une simple affectation tant que la variable correspond à la clé de l'objet.

```
const { second } = teachers;
```

La destructuration est probablement la principale raison d'utiliser des objets lors de la transmission de données. Vous pouvez facilement collecter plusieurs valeurs dans un objet, puis les transmettre à une autre fonction où vous pouvez extraire les informations à nouveau.

```
function getSecondGradeInfo({ second }) {  const school = "Lakin";  return {    school,    teacher: second  }}
```

Les choses commencent à se compliquer lorsque vous voulez itérer sur l'objet. Vous devez soit convertir une partie de l'objet en tableau, soit utiliser une boucle `for...in`.

```
Object.keys(teachers).map(grade => `${grade}:${teachers[grade]}`).join(' ');
```

```
let myTeacher = '';for(const grade in teachers) {  myTeacher += ` ${grade}:${teachers[grade]}`;}
```

Les choses deviennent déjà un peu désordonnées. Vous devez soit itérer sur les clés, soit muter une variable. Pire encore, les objets ne garantissent pas l'ordre. Vous ne pouvez jamais faire confiance à votre boucle `for...in` pour donner les résultats dans la séquence que vous souhaitez.

Tous ces problèmes proviennent du manque de propriété itérable d'un objet. `Object.keys` et `for...in` utilisent tous deux l'itérateur qui provient de la conversion des clés en tableau.

Au-delà de cela, il y a d'autres problèmes avec les objets. Il y a des options de clés limitées. Vous ne pouvez pas utiliser de [nombres](http://speakingjs.com/es5/ch17.html#object_literals) comme clés, par exemple. Ils ne sont pas aussi [performants](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Keyed_collections_Maps_Sets_WeakMaps_WeakSets) que d'autres collections. Mais pour la plupart, ils sont bons pour transmettre des données sans beaucoup de boucles.

Pour résumer :

✅ Destructurable

❌ Itérable

✅ Clé

### Maps

Les Maps sont un nouveau type de collection pour JavaScript. Ce sont des magasins clé-valeur appropriés. Ce qui est simplement une façon de dire qu'ils ont été conçus spécifiquement à cet effet. Contrairement aux objets, vous devez toujours créer explicitement une nouvelle instance :

```
const teachers = new Map();
```

Après cela, vous définissez chaque élément en passant une clé puis une valeur comme arguments.

```
teachers.set('first', 'Cooper').set('second', 'Simes').set('third', 'Butler');
```

Pour récupérer une valeur, vous appelez la méthode `get()` avec le nom de la clé.

```
teachers.get('second'); // Simes
```

Cela peut déjà sembler un peu familier. Ce n'est pas très différent de `localStorage.setItem(key, value)` que vous avez peut-être utilisé pour stocker des données entre les visites d'une webApp.

En tant que magasins clé-valeur, les maps sont assez géniales. Elles acceptent une plus grande [variété de clés](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#Objects_and_maps_compared). Et tandis que le temps de recherche d'un objet est linéaire, le temps de recherche d'une Map sera [logarithmique](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Keyed_collections_Maps_Sets_WeakMaps_WeakSets).

Mais le plus grand avantage est qu'elles ont un itérable intégré. Cela signifie que vous pouvez faire des choses comme accéder directement aux paires clé-valeur :

```
let myTeachers = '';for([grade, name] of teachers) {  myTeachers += ` ${grade}:${name}`;}
```

Quelques choses à dire à ce sujet. Il peut sembler que vous destructurez la map au début de la boucle for. En réalité, ce n'est pas le cas. Lorsque vous itérez sur une map, vous obtenez une paire avec la clé et la valeur. Vous destructurez donc en réalité un tableau.

Ensuite, vous pouvez remarquer que vous mutez toujours une variable. Ce n'est pas génial. Heureusement, puisque une map est un itérable, vous pouvez utiliser l'opérateur de propagation pour convertir la map en un tableau de paires. Cela signifie

```
[...teachers]
```

deviendra

```
[  ['first', 'Cooper'],  ['second', 'Simes'],  ['third', 'Butler'],]
```

Avec la map convertie en tableau, vous pouvez maintenant mapper les éléments pour créer votre chaîne.

```
[...teachers].map(([grade, name]) => `${grade}:${name}`).join();
```

Cela signifie que vous avez accès à toutes les méthodes de tableau en trois caractères courts.

Oh, et puisque c'est itérable, l'ordre est préservé. Si vous ajoutez votre professeur de première année au début, vous l'obtiendrez au début.

Quels sont les inconvénients ? Le plus grand est le manque de destructuration directe. Vous ne pouvez pas extraire une valeur sans soit appeler la méthode `get()`, soit en convertissant en tableau. Cela signifie que le passage de données entre les fonctions devient un peu plus verbeux. Vous ne pouvez pas non plus représenter les maps comme une chaîne JSON. Vous ne tirerez donc pas les maps d'une API de sitôt.

Néanmoins, si vous avez des données que vous savez que vous voudrez parcourir tout en conservant la capacité d'extraire rapidement des données avec une clé, les maps sont votre meilleur choix.

Pour résumer :

❌ Destructurable

✅ Itérable

✅ Clé

### Passage entre les collections

Vous avez probablement remarqué un motif frustrant. Il n'y a pas une seule collection qui puisse tout faire.

Heureusement, ce n'est pas un problème aussi grand que vous pourriez le penser.

Vous avez déjà vu que vous pouvez convertir une map en tableau avec l'opérateur de propagation. Vous pouvez également faire l'inverse et convertir un tableau en map, en le passant dans le constructeur.

Vous pouvez également accélérer le processus de création initial en passant un tableau de paires :

```
const myTeachers = [  ['first', 'Cooper'],  ['second', 'Simes'],  ['third', 'Butler'],]const teachers = new Map(myTeachers);
```

À ce stade, lorsque vous avez une map, vous avez essentiellement accès à la fois aux propriétés d'un tableau et aux propriétés d'une map avec une simple conversion.

Les objets s'améliorent. Avec `Object.entries()`, vous pouvez créer un tableau de paires à partir d'un objet.

```
const teachers = {  first: "Cooper",  second: "Simes",  third: "Butler",};
```

```
const myTeachers = Object.entries(teachers);
```

```
myTeachers[0]// ['first', 'Cooper']
```

Cela signifie que lorsque vous avez un objet, vous avez accès aux méthodes de tableau avec une simple conversion. Cependant, revenir en arrière est un peu plus difficile. Il y a actuellement une [proposition](https://github.com/tc39/proposal-object-from-entries) pour `Object.fromEntries()` qui prendra un tableau de paires et créera un objet. Mais cela reste encore un peu loin.

Cependant, une fois que cela sera disponible, vous ne serez plus bloqué dans un type de collection particulier. Et c'est la meilleure nouvelle de toutes. Une fois que vous pourrez passer facilement et rapidement entre les collections, vous pourrez commencer à tirer parti des meilleures fonctionnalités de chacune. Destructurer les valeurs lorsque c'est pratique, itérer lorsque vous en avez besoin.

En d'autres termes, vous pouvez examiner les données que vous avez et le code dont vous avez besoin et choisir le type de collection approprié. Si une autre fonction a besoin d'un type différent, écrivez une simple conversion. Plus de devinettes. Plus de frustrations. Vous pouvez adapter votre collection à vos objectifs et non votre code à votre collection.