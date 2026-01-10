---
title: 'Modèles de résolution de problèmes pour les entretiens techniques : le modèle
  du compteur de fréquence expliqué'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-18T21:48:23.000Z'
originalURL: https://freecodecamp.org/news/solve-technical-interview-questions-using-frequency-counter
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/beach.jpg
tags:
- name: career advice
  slug: career-advice
- name: careers
  slug: careers
- name: Interview tips
  slug: interview-tips
- name: Interviews
  slug: interviews
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
seo_title: 'Modèles de résolution de problèmes pour les entretiens techniques : le
  modèle du compteur de fréquence expliqué'
seo_desc: "By Martin Cartledge\nIn my last article, I shared my thoughts on how to\
  \ prepare for a software developer interview. \nIn this article, I am going to switch\
  \ gears a bit and talk about common patterns you can use to solve problems in technical\
  \ interviews..."
---

Par Martin Cartledge

Dans mon dernier article, j'ai partagé mes réflexions sur la façon de [se préparer à un entretien pour développeur logiciel](https://www.martincartledge.io/prepare-for-software-developer-interview/).

Dans cet article, je vais changer un peu de cap et parler des modèles courants que vous pouvez utiliser pour résoudre des problèmes lors d'entretiens techniques. Nous allons discuter en profondeur du modèle de _compteur de fréquence_ pour vous aider à le maîtriser efficacement.

## Qu'est-ce que le modèle "Compteur de fréquence" ?

Le modèle du Compteur de fréquence utilise un objet ou un ensemble pour collecter des valeurs et la fréquence de ces valeurs.

Ce modèle est souvent utilisé avec un `tableau` ou une `chaîne de caractères`, et permet d'éviter les boucles imbriquées (complexité temporelle quadratique `O(n²)`).

## Quand dois-je utiliser le modèle du Compteur de fréquence ?

Le modèle du Compteur de fréquence est le plus utile lorsque vous avez plusieurs morceaux de données que vous souhaitez comparer entre eux. Laissez-moi vous guider à travers un exemple pour voir le Compteur de fréquence en action.

## L'exercice "sameSquared"

* Écrire une fonction appelée `sameSquared` qui accepte deux tableaux
* La fonction doit retourner `true` si _chaque_ valeur du premier tableau a sa valeur correspondante au carré dans le second tableau
* La fréquence des valeurs doit être la même

### Quel est le résultat optimal ?

Après avoir écrit notre fonction, nous devrions nous attendre à ce que notre fonction `sameSquared` retourne ces valeurs.

`sameSquared([1, 2, 3], [4, 1, 9]); // true`

`sameSquared([1, 2, 3], [1, 9]); // false`

`sameSquared([1, 2, 1], [4, 4, 1]); // false`

`sameSquared([2, 3, 6, 8, 8], [64, 36, 4, 9, 64]); // true`

### Pour commencer

Tout d'abord, en utilisant le mot-clé `function`, nous créons une fonction avec l'identifiant `sameSquared` :

```javascript
function sameSquared() {

```

Notre fonction `sameSquared` a besoin de deux paramètres, un premier tableau et un second tableau. Dans cet exemple, nous passons ces valeurs `[1, 2, 3]` et `[4, 1, 9]`.

```javascript
function sameSquared(firstArr, secondArr) {

    
```

### Vérifier les cas limites

À l'intérieur de notre bloc de fonction, nous voulons aborder quelques cas limites. Tout d'abord, nous devons vérifier que les deux paramètres ont des valeurs vraies, c'est-à-dire _non_ `null`, `undefined`, etc.

Nous pouvons vérifier une valeur fausse en utilisant l'opérateur `!`. Si `firstArr` ou `secondArr` est faux, nous retournons `false`.

```javascript
function sameSquared(firstArr, secondArr) {
  if (!firstArr || !secondArr) return false;
```

Le prochain cas limite que nous voulons prendre en compte est de nous assurer que la longueur des deux tableaux est la même. Si elles sont différentes, nous savons qu'elles ne peuvent _pas_ contenir une quantité égale de valeurs partagées.

En vérifiant la propriété `length` sur les deux paramètres, nous pouvons déterminer si elles sont les mêmes. Si elles ne le sont pas, nous retournons `false`.

```javascript
function sameSquared(firstArr, secondArr) {
  if (!firstArr || !secondArr) return false;
  if (firstArr.length !== secondArr.length) return false;
```

### Construire un "dictionnaire" pour éviter les boucles imbriquées

Nous devons garder une trace de toutes les valeurs dans au moins l'un des tableaux. Pour ce faire, et pour éviter une boucle imbriquée, nous pouvons stocker ces valeurs dans une table de hachage (objet). J'appellerai la mienne `lookup`.

```javascript
function sameSquared(firstArr, secondArr) {
  if (!firstArr || !secondArr) return false;
  if (firstArr.length !== secondArr.length) return false;

  const lookup = {};
```

En utilisant une boucle `for of`, nous itérons à travers le `firstArr`. À l'intérieur du bloc `for of`, nous assignons la clé au résultat de `value * value`.

La valeur dans cette paire clé/valeur sera un _compteur de fréquence_ qui reflète le nombre de fois qu'une valeur spécifique est "vue" dans le `firstArr`.

Tout d'abord, nous vérifions si `lookup` contient une entrée pour `value * value`, si c'est le cas, nous ajoutons `1` à celle-ci. Si ce n'est pas le cas, nous assignons la valeur à `0` puis nous ajoutons `1`.

```javascript
function sameSquared(firstArr, secondArr) {
  if (!firstArr || !secondArr) return false;
  if (firstArr.length !== secondArr.length) return false;

  const lookup = {};

  for (value of firstArr) {
    lookup[value * value] = (lookup[value * value] || 0) + 1;
  }
```

Une fois que le `firstArr` a fini de boucler, le `lookup` devrait contenir ces valeurs :

```javascript
{
  1: 1,
  4: 1,
  9: 1
}
```

### Comparer les valeurs des tableaux

Maintenant que nous avons itéré à travers toutes les valeurs du `firstArr` et que nous les avons stockées sous leur valeur respective _au carré_, nous voulons comparer ces valeurs aux valeurs du `secondArr`.

Nous commençons par créer une autre boucle `for of`. Sur la première ligne à l'intérieur de notre nouveau bloc `for of`, nous écrivons une instruction conditionnelle pour vérifier si la valeur actuelle de notre `secondArr` n'est _pas_ à l'intérieur de notre `lookup`. Si ce n'est pas le cas, nous arrêtons la boucle et retournons `false`.

Si la valeur du `secondArr` est dans notre `lookup`, nous voulons décrémenter la valeur de cette entrée. Nous pouvons le faire en utilisant l'opérateur d'assignation `-=`.

```javascript
function sameSquared(firstArr, secondArr) {
  if (!firstArr || !secondArr) return false;
  if (firstArr.length !== secondArr.length) return false;

  const lookup = {};
  for (value of firstArr) {
    lookup[value * value] = (lookup[value * value] || 0) + 1;
  }
  for (secondValue of secondArr) {
    if (!lookup[secondValue]) return false;
      lookup[secondValue] -= 1;
    }
```

Après avoir fini de boucler à travers le `secondArr`, notre `lookup` devrait avoir ces valeurs :

```javascript
{
  1: 0,
  4: 0,
  9: 0
}
```

### Finaliser notre fonction "sameSquared"

Si nous finissons d'itérer à travers le `secondArr` sans retourner `false`, cela signifie que notre `firstArr` contient toutes les valeurs qui sont dans un état au carré dans le `secondArr`. Par conséquent, nous retournons `true` à l'extérieur de la boucle `for of`.

```javascript
function sameSquared(firstArr, secondArr) {
  if (!firstArr || !secondArr) return false;
  if (firstArr.length !== secondArr.length) return false;

  const lookup = {};
  for (value of firstArr) {
    lookup[value * value] = (lookup[value * value] || 0) + 1;
  }
  for (secondValue of secondArr) {
    if (!lookup[secondValue]) return false;
    lookup[secondValue] -= 1;
  }
  return true;
}
```

Laissez-moi vous montrer un autre exemple qui est très couramment utilisé dans les évaluations de codage (vous avez donc peut-être déjà vu ce problème).

## L'exercice "isAnagram"

* Écrire une fonction appelée `isAnagram` qui accepte deux chaînes de caractères
* La fonction doit retourner `true` si les deux paramètres de chaînes sont des [anagrammes](https://en.wikipedia.org/wiki/Anagram) l'un de l'autre

### Quel est le résultat optimal ?

Après avoir écrit notre fonction, nous devrions nous attendre à ce que notre fonction `isAnagram` retourne ces valeurs.

`isAnagram("silent", "listen"); // true`

`isAnagram("martin", "nitram"); // true`

`isAnagram("cat", "tag"); // false`

`isAnagram("rat", "tar"); // true`

### Pour commencer

Tout d'abord, en utilisant le mot-clé `function`, nous créons une fonction avec l'identifiant `isAnagram` :

```javascript
function isAnagram() {

```

Notre fonction `isAnagram` a besoin de deux paramètres, une première `chaîne` et une seconde `chaîne`. Dans cet exemple, nous passons ces valeurs, `silent` et `listen`.

```javascript
function isAnagram(firstStr, secondStr) {

```

### Vérifier les cas limites

Sur les premières lignes de notre bloc de fonction, nous voulons aborder quelques cas limites, tout comme dans le premier exemple.

Similaire à `isAnagram`, nous devons vérifier que les deux paramètres ont des valeurs vraies, c'est-à-dire _non_ `null`, `undefined`, etc. Nous pouvons vérifier une valeur fausse en utilisant l'opérateur `!`. Si `firstStr` ou `secondStr` est faux, nous retournons `false`.

```javascript
function isAnagram(firstStr, secondStr) {
  if (!firstStr || !secondStr) return false;
```

Le prochain cas limite que nous voulons prendre en compte est de nous assurer que la longueur des deux tableaux est la même. Si elles sont différentes, nous savons qu'elles ne peuvent _pas_ contenir un nombre égal de valeurs partagées.

En vérifiant la propriété `length` sur les deux paramètres, nous pouvons déterminer si elles sont les mêmes. Si elles ne le sont pas, nous retournons `false`

```javascript
function isAnagram(firstStr, secondStr) {
  if (!firstStr || !secondStr) return false;
  if (firstStr.length !== secondStr.length) return false;
```

### Construire un "dictionnaire" pour éviter les boucles imbriquées

Rappelez-vous, nous utilisons le modèle du compteur de fréquence et nous devons garder une trace de toutes les valeurs dans au moins l'un des tableaux. Maintenant, nous savons que la meilleure façon de gérer cela est de stocker ces valeurs dans une table de hachage (objet). Pour garder les choses cohérentes, j'appellerai la mienne `lookup` à nouveau.

```javascript
function isAnagram(firstStr, secondStr) {
  if (!firstStr || !secondStr) return false;
  if (firstStr.length !== secondStr.length) return false;

  const lookup = {};
```

En utilisant une boucle `for of`, nous itérons à travers le `firstStr`. À l'intérieur du bloc `for of`, nous assignons la clé au résultat de l'expression `value * value`.

La valeur dans cette paire clé/valeur sera un _compteur de fréquence_ qui reflète le nombre de fois qu'une valeur spécifique est "vue" dans le `firstStr`.

En utilisant un opérateur ternaire, nous vérifions si `lookup` contient une entrée pour `value * value`, si c'est le cas, nous utilisons l'opérateur d'assignation `+=` pour incrémenter la valeur de `1`. Si ce n'est pas le cas, nous assignons simplement la valeur à `1`.

```javascript
function isAnagram(firstStr, secondStr) {
	if (!firstStr || !secondStr) return false;
    if (firstStr.length !== secondStr.length) return false;

	const lookup = {};

	for (first of firstStr) {

    	lookup[first] ? (lookup[first] += 1) : (lookup[first] = 1);

  }
```

Une fois que le `firstStr` a fini de boucler, le `lookup` devrait contenir ces valeurs :

```javascript
{
  s: 1,
  i: 1,
  l: 1,
  e: 1,
  n: 1,
  t: 1
}
```

### Comparer les valeurs des tableaux

Maintenant que nous avons itéré à travers toutes les valeurs du `firstStr` et que nous avons stocké leurs valeurs, nous voulons comparer ces valeurs aux valeurs du `secondStr`.

Nous commençons par créer une autre boucle `for of`. Sur la première ligne à l'intérieur de notre nouveau bloc `for of`, nous écrivons une instruction conditionnelle pour vérifier si la valeur actuelle de notre `secondStr` n'est _pas_ à l'intérieur de notre `lookup`. Si ce n'est pas le cas, nous voulons arrêter l'itération et retourner `false`.

Sinon, si la valeur du `secondStr` _est_ dans notre `lookup`, nous voulons décrémenter la valeur de cette entrée. Nous pouvons le faire en utilisant l'opérateur d'assignation `-=`.

```javascript
function isAnagram(firstStr, secondStr) {
  if (!firstStr || !secondStr) return false;
  if (firstStr.length !== secondStr.length) return false;

  const lookup = {};

  for (first of firstStr) {
    lookup[first] ? (lookup[first] += 1) : (lookup[first] = 1);
  }

  for (second of secondStr) {
    if (!lookup[second]) return false;
    lookup[second] -= 1;
  }
```

Après avoir fini de boucler à travers le `secondStr`, notre `lookup` devrait avoir ces valeurs :

```javascript
{
  s: 0,
  i: 0,
  l: 0,
  e: 0,
  n: 0,
  t: 0
}
```

### Finaliser notre fonction "isAnagram"

Si nous finissons d'itérer à travers le `secondStr` sans retourner `false`, cela signifie que notre `firstStr` contient toutes les valeurs qui sont dans le `secondStr`. Par conséquent, nous retournons `true` à l'extérieur de la boucle `for of`.

```javascript
function isAnagram(firstStr, secondStr) {
  if (!firstStr || !secondStr) return false;
  if (firstStr.length !== secondStr.length) return false;

  const lookup = {};

  for (first of firstStr) {
    lookup[first] ? (lookup[first] += 1) : (lookup[first] = 1);
  }

  for (second of secondStr) {
    if (!lookup[second]) return false;
    lookup[second] -= 1;
  }
  return true;
}
```

## En résumé

J'espère que cet aperçu approfondi du modèle du Compteur de fréquence a été utile. Maintenant que vous savez comment fonctionne ce modèle, je suis convaincu que vous serez en mesure d'impressionner votre interlocuteur en montrant vos compétences à un niveau encore plus élevé.

Dans mon prochain article, je discuterai d'un autre modèle courant de résolution de problèmes appelé la Fenêtre glissante. Merci de votre lecture, et bon entretien !