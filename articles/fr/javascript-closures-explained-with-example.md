---
title: Fermeture en JavaScript – Expliqué avec des exemples
subtitle: ''
author: Keyur Paralkar
co_authors: []
series: null
date: '2022-04-13T18:57:03.000Z'
originalURL: https://freecodecamp.org/news/javascript-closures-explained-with-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/safar-safarov-LKsHwgzyk7c-unsplash-2.jpg
tags:
- name: closure
  slug: closure
- name: JavaScript
  slug: javascript
seo_title: Fermeture en JavaScript – Expliqué avec des exemples
seo_desc: "In this article, we are going to talk about closures in JavaScript. I'll\
  \ walk you through the definition of a closure, a simple day-to-day fetch utility\
  \ closure example, and some of the advantages and disadvantages of using closures.\
  \ \nTable of Conten..."
---

Dans cet article, nous allons parler des fermetures en JavaScript. Je vais vous expliquer la définition d'une fermeture, un exemple simple d'utilitaire de récupération du quotidien, ainsi que certains des avantages et inconvénients de l'utilisation des fermetures. 

## Table des matières

* [Prérequis](#heading-prerequis) 
* [Qu'est-ce que les fermetures](#heading-quest-ce-que-les-fermetures)?
* [Cas d'utilisation des fermetures](#heading-cas-dutilisation-des-fermetures-creation-dun-utilitaire-de-recuperation-avec-des-fermetures)
* [Avantages des fermetures](#heading-avantages-des-fermetures)
* [Inconvénients des fermetures](#heading-inconvenients-des-fermetures)
* [Résumé](#heading-resume)

Sans plus attendre, commençons.

## Prérequis

Vous devez avoir une bonne compréhension des sujets suivants pour comprendre cet article :

* Comment fonctionne le [contexte d'exécution](https://www.freecodecamp.org/news/javascript-execution-context-and-hoisting/) de JavaScript
* Qu'est-ce que l'[API Fetch](https://www.freecodecamp.org/news/javascript-fetch-api-tutorial-with-js-fetch-post-and-header-examples/) et comment l'utiliser

## Qu'est-ce que les fermetures ?

Les fermetures sont des fonctions qui ont accès aux variables présentes dans leur chaîne de portée, même si la fonction externe cesse d'exister.

Pour comprendre cela plus en détail, comprenons ce qu'est une chaîne de portée. La chaîne de portée fait référence au fait que la portée parente n'a pas accès aux variables à l'intérieur de la portée de ses enfants, mais que la portée des enfants a accès aux variables présentes dans ses portées parentes. 

Rendons cela plus clair en regardant un exemple ci-dessous :

```javascript
let buttonProps = (borderRadius) => {
	const createVariantButtonProps = (variant, color) => {
		const newProps = {
			borderRadius,
			variant,
			color
		};
		return newProps;
	}
	return createVariantButtonProps;
}
```

Comme vous pouvez le voir, nous avons une fonction appelée `buttonProps`. Cette fonction accepte `borderRadius` comme argument. Considérons la fonction `buttonProps` comme notre fonction parente.

Nous avons une autre fonction qui a été définie à l'intérieur de la fonction parente, c'est-à-dire `createVariantButtonProps`. Cette fonction acceptera `variant` et `color` comme argument et retournera un objet qui constitue une variable `borderRadius` qui est présente en dehors de sa portée.

Mais une question se pose : comment la fonction interne résout-elle les variables présentes dans la portée parente ?

Eh bien, cela est possible via la portée lexicale. En utilisant la portée lexicale, l'analyseur JS sait comment résoudre les variables présentes dans sa portée actuelle ou sait en fait comment résoudre les variables présentes dans les fonctions imbriquées. 

Ainsi, sur la base de l'explication ci-dessus, `createVariantButtonProps` aura accès aux variables présentes dans sa fonction externe `buttonProps`.

Dans l'exemple ci-dessus, la fonction interne `createVariantButtonProps` est une fermeture. Pour comprendre les fermetures en détail, nous allons d'abord passer en revue les caractéristiques des fermetures qui sont les suivantes :

* Même si la fonction externe cesse d'exister, une fermeture a toujours accès à ses variables parentes.
* Les fermetures n'ont pas accès au paramètre `args` de leur fonction externe.

Approfondissons chacun de ces points.

### Même si la fonction externe cesse d'exister, elle a toujours accès à ses variables parentes.

C'est la fonctionnalité de base de toute fermeture. C'est leur principal motto de vie, c'est-à-dire leur principe de fonctionnement.

Pour voir cela en action, nous allons maintenant exécuter la fonction `buttonProps` ci-dessus.

```js
let primaryButton = buttonProps("1rem"); 
```

L'appel de la fonction `buttonProps` nous retournera une autre fonction qui est notre fermeture.

Maintenant, exécutons cette fermeture :

```js
const primaryButtonProps = primaryButton("primary", "red");
```

Une fois la fermeture exécutée, elle retourne l'objet suivant :

```js
{
   "borderRadius":"1rem",
   "variant":"primary",
   "color":"red"
}
```

Ici, une question se pose à nouveau : comment la fonction `primaryButton` a-t-elle accès à la variable `borderRadius` qui n'était pas présente à l'intérieur ?

Si nous passons en revue la définition des fermetures et l'enchaînement des portées que nous avons discuté précédemment, cela correspond parfaitement à cette instance.

Approfondissons pourquoi les fermetures ont toujours accès aux variables définies en dehors de leur portée, même si la fonction externe cesse d'exister – par exemple, `borderRadius` ? 

La réponse est simple : les fermetures ne stockent pas de valeurs statiques. Au lieu de cela, elles stockent des références aux variables présentes dans la chaîne de portée. De cette manière, même si la fonction externe meurt, la fonction interne, qui est une fermeture, a toujours accès à ses variables parentes.

## Cas d'utilisation de la fermeture : Création d'un utilitaire de récupération avec des fermetures

Maintenant que nous avons appris ce que sont les fermetures, nous allons créer une fonction utilitaire à usage général. Elle gérera différentes méthodes de requête telles que GET et POST avec les API REST.

Pour ce cas d'utilisation, 

* Nous allons utiliser les [API JSON placeholder](https://jsonplaceholder.typicode.com/). Cela nous fournit des données factices que nous pouvons modifier en utilisant les API REST.
* Nous allons utiliser l'API [fetch](https://developer.mozilla.org/en-US/docs/Web/API/fetch) de JavaScript.

Discutons d'abord pourquoi nous devons concevoir une telle utilité. Il y a plusieurs raisons :

* Pour chaque appel de récupération, nous ne voulons pas définir l'URL de base (ou d'autres paramètres communs) tout le temps. Nous allons donc créer un mécanisme qui stockera l'URL de base/paramètres comme un état.
* Pour supprimer le code redondant.
* Pour fournir de la modularité dans la base de code.

Plongeons dans les détails de cette utilité. Notre utilitaire de récupération ressemblera à ceci :

```javascript
const fetchUtility = (baseURL, headers) => {
  const createFetchInstance = (route, requestMethod, data) => {
    const tempReq = new Request(`${baseURL}${route}`, {
      method: requestMethod,
      headers,
      data: data || null
    });
    return [fetch, tempReq];
  };

  return createFetchInstance;
};
```

* `fetchUtility` accepte deux paramètres qui sont `baseURL` et `headers`. Ceux-ci seront utilisés plus tard dans la fermeture pour construire l'URL de base ainsi que les en-têtes.
* Ensuite, nous avons `createFetchInstance`, qui accepte `route`, `requestMethod` et `data` comme paramètres. 
* Ensuite, cette fonction crée un nouvel objet de requête qui construira notre URL en utilisant le code : `${baseURL}${route}`. Nous passons également un objet qui contient le type de méthode de requête, les en-têtes et les données si disponibles.
* Ensuite, nous retournons l'instance d'une API fetch ainsi que l'objet de requête.
* Enfin, nous retournons la fonction `createFetchInstance`.

Maintenant, voyons cette fonction en action. Appelons notre fonction `fetchUtility` pour initialiser le `baseURL` :

```javascript
const fetchInstance = fetchUtility("https://jsonplaceholder.typicode.com");
```

* Si nous observons, `fetchInstance` a maintenant la valeur de la fermeture de la fonction `fetchUtility`.
* Ensuite, nous passons la route et le type de la requête à la fermeture `fetchInstance` :

```javascript
const [getFunc, getReq] = fetchInstance("/todos/1", "GET");
```

Comme vous pouvez le voir, cela nous retourne un tableau d'instance d'API fetch et le corps de la requête que nous avons configuré.

Enfin, nous pouvons utiliser l'API fetch `getFunc` pour appeler la requête `getReq` comme suit :

```javascript
getFunc(getReq)
  .then((resp) => resp.json())
  .then((data) => console.log(data));
```

Nous pouvons également créer une requête POST similaire à la requête GET ci-dessus. Nous devons simplement appeler à nouveau `fetchInstance` comme suit :

```javascript
const [postFunc, postReq] = fetchInstance(
  "/posts",
  "POST",
  JSON.stringify({
    title: "foo",
    body: "bar",
    userId: 1
  })
);
```

Et pour exécuter cette requête POST, nous pouvons faire l'opération similaire à celle que nous avons faite pour la requête GET :

```javascript
postFunc(postReq)
  .then((resp) => resp.json())
  .then((data) => console.log(data));
```

Si nous regardons de près l'exemple ci-dessus, nous pouvons voir que la fonction interne `createFetchInstance` a accès aux variables présentes dans sa chaîne de portée. Avec l'aide de la portée lexicale, lors de sa définition de `createFetchInstance`, elle résout les noms de variables. 

De cette manière, la fermeture référence les variables `baseURL` et `headers` lors de sa définition, même après que la fonction externe `fetchUtility` a cessé d'exister.

Si nous pensons aux fermetures sous un angle différent, alors les fermetures nous aident à maintenir un état comme `baseURL` et `headers` que nous pouvons utiliser dans différents appels de fonctions.

## Avantages des fermetures

Voici quelques avantages des fermetures :

* Elles vous permettent d'attacher des variables à un contexte d'exécution.
* Les variables dans les fermetures peuvent vous aider à maintenir un état que vous pouvez utiliser plus tard.
* Elles fournissent une encapsulation des données.
* Elles aident à supprimer le code redondant.
* Elles aident à maintenir un code modulaire.

## Inconvénients des fermetures

Il y a deux principaux inconvénients à l'utilisation excessive des fermetures :

* Les variables déclarées à l'intérieur d'une fermeture ne sont pas collectées par le garbage collector.
* Trop de fermetures peuvent ralentir votre application. Cela est en fait causé par la duplication de code en mémoire.

## Résumé

Ainsi, de cette manière, les fermetures peuvent être vraiment utiles si vous souhaitez traiter ou implémenter certains modèles de conception. Elles vous aident également à écrire un code propre et modulaire. 

Si vous avez aimé l'idée des fermetures, je vous recommande de lire davantage sur les sujets suivants :

* [Modèles de conception](https://www.patterns.dev/posts/classic-design-patterns/)
* [Fermetures anonymes](https://stackoverflow.com/questions/16032840/javascript-anonymous-closure)

Merci d'avoir lu !

Suivez-moi sur [Twitter](https://twitter.com/keurplkar), [GitHub](https://github.com/keyurparalkar) et [LinkedIn](https://www.linkedin.com/in/keyur-paralkar-494415107/).