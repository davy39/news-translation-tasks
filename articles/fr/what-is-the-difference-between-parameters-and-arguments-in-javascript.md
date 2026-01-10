---
title: Paramètres vs Arguments en JavaScript – Quelle est la différence ?
subtitle: ''
author: Segun Ajibola
co_authors: []
series: null
date: '2022-09-28T21:18:15.000Z'
originalURL: https://freecodecamp.org/news/what-is-the-difference-between-parameters-and-arguments-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Parameters-vs-Arguments.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Paramètres vs Arguments en JavaScript – Quelle est la différence ?
seo_desc: 'JavaScript is one of the most popular programming languages out there for
  web development.

  The dynamic values passed in a JavaScript function can change when the function
  gets called in another location in the code. The keywords we use to name these ...'
---

JavaScript est l'un des langages de programmation les plus populaires pour le développement web.

Les valeurs dynamiques transmises à une fonction JavaScript peuvent changer lorsque la fonction est appelée à un autre endroit du code. Les mots-clés que nous utilisons pour nommer ces données sont les paramètres et les arguments, mais certains développeurs les confondent.

Dans cet article, vous en apprendrez plus sur les paramètres et les arguments, ce qu'ils sont, ainsi que l'endroit et le moment où les utiliser.

### Table des matières

* Introduction aux fonctions JavaScript
* Comment utiliser les paramètres et les arguments dans une fonction
* La puissance des arguments
* Conclusion

## Introduction aux fonctions JavaScript

L'un des blocs de construction fondamentaux de la programmation JavaScript est la fonction. C'est un bloc de code conçu pour effectuer une tâche particulière.

Les fonctions sont du code réutilisable que vous pouvez utiliser n'importe où dans votre programme. Elles éliminent le besoin de répéter le même code tout le temps.

Pour utiliser les fonctions de manière efficace, vous pouvez leur passer des valeurs.

Voici un exemple de fonction :

```javascript
function add(){
	return 2 + 3
}

add()
```

Il s'agit d'une déclaration de fonction, le nom de la fonction est `add`, et elle a été appelée après la fonction avec `add()`. Le résultat de la fonction sera 5.

Introduisons les paramètres et les arguments dans la fonction.

## Comment utiliser les paramètres et les arguments dans une fonction

Jetez un œil à notre code de fonction maintenant :

```javascript
function add(x, y){
	return x + y
}

add(2, 3)
```

Nous avons introduit x et y ici et changé l'emplacement du 2 et du 3. x et y sont les paramètres tandis que 2 et 3 sont les arguments ici.

Un **paramètre** est l'une des variables d'une fonction. Et lorsqu'une méthode est appelée, les **arguments** sont les données que vous passez dans les paramètres de la méthode.

Lorsque la fonction est appelée avec `add(2, 3)`, les arguments 2 et 3 sont assignés à x et y, respectivement. Cela signifie que dans la fonction, x sera remplacé par 2 et y sera remplacé par 3.

Si la fonction est appelée avec un argument différent, la même chose s'applique. Les paramètres sont comme des espaces réservés pour les arguments de la fonction.

## La puissance des arguments

Nous pouvons utiliser les arguments plus efficacement lorsque nous voulons rendre les fonctions plus réutilisables, ou lorsque nous voulons rendre l'appel de fonctions à l'intérieur d'autres fonctions plus puissant.

Voici un exemple :

```javascript
function add(x, y){
	return x + y
}

function multiply(a, b, c){ // a = 1, b = 2, c = 3
	const num1 = add(a, b) // num1 = add(1, 2) = 3
	const num2 = add(b, c) // num2 = add(2, 3) = 5
    
	return num1 * num2 // 15
}

multiply(1, 2, 3)
// retourne 15
```

La première fonction `add()` a deux paramètres, x et y. La fonction retourne l'addition des deux paramètres.

La deuxième fonction `multiply()` a trois paramètres : à l'intérieur de la fonction, deux variables y sont déclarées, `num1` et `num2`. `num1` stockera la valeur du résultat de `add(a, b)`, et `num2` stockera la valeur du résultat de `add(b, c)`. À la fin, la fonction `multiply` retournera la valeur de `num1` multipliée par `num2`.

`multiply` est appelée avec trois arguments qui sont 1, 2 et 3. `add(a, b)` sera `add(1, 2)` ce qui retournera 3. `add(b, c)` sera `add(2, 3)` ce qui retournera 5.

`num1` aura la valeur 3 tandis que `num2` sera 5. `num1 * num2` retournera 15.

Les arguments sont passés dans la fonction `multiply` qui sont également utilisés comme arguments pour la fonction `add`.

## Conclusion

L'utilisation des paramètres et des arguments peut parfois être déroutante, surtout si vous venez de les apprendre. Mais si vous apprenez d'abord correctement ce qu'est une fonction et comment elle fonctionne, vous comprendrez facilement les paramètres et les arguments.

Merci d'avoir lu cet article. Si vous l'avez apprécié, n'hésitez pas à le partager pour aider d'autres développeurs.

Vous pouvez me joindre sur [Twitter](https://twitter.com/iamsegunajibola), [LinkedIn](https://www.linkedin.com/in/segunajibola/) et [GitHub](https://github.com/segunajibola).

Bon apprentissage.