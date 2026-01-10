---
title: 'Guide des Props React : 10 Modèles à Connaître'
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-02-19T17:02:51.000Z'
originalURL: https://freecodecamp.org/news/react-props-cheatsheet
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/react-props-cheatsheet-1.png
tags:
- name: cheatsheet
  slug: cheatsheet
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: 'Guide des Props React : 10 Modèles à Connaître'
seo_desc: 'Props are a powerful tool to use in React, but how do you use them effectively
  to write robust, reliable React components and applications?

  In this tutorial, we will be reviewing ten patterns you should use when working
  with props in React.

  We will n...'
---

Les props sont un outil puissant à utiliser dans React, mais comment les utiliser efficacement pour écrire des composants et applications React robustes et fiables ?

Dans ce tutoriel, nous allons passer en revue dix modèles à utiliser lors de la manipulation des props dans React.

Nous n'aborderons pas seulement ce que sont ces modèles et comment les utiliser, mais vous verrez également comment les appliquer par vous-même à travers des exemples pratiques et concrets.

Commençons !

### Vous voulez votre propre copie ?📄

**[Cliquez ici pour télécharger le guide au format PDF](https://reedbarger.com/resources/react-props-2021)** (cela prend 5 secondes).

Il contient toutes les informations essentielles ici sous forme de guide PDF pratique.

## 1. Les props React peuvent être passées conditionnellement

Les props passées aux composants peuvent être considérées comme des arguments passés à une fonction.

Si les valeurs des props ne sont pas passées à un certain composant, aucune erreur ne sera levée. Au lieu de cela, dans le composant, cette prop aura une valeur de `undefined`.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/props-1-min.gif)

Si vous souhaitez être alerté lorsqu'une valeur n'est pas passée en tant que prop à un composant, vous pouvez utiliser un outil comme prop-types ou TypeScript.

> Avec prop-types ou TypeScript, nous pouvons indiquer à React les props que nous passons pour un composant donné, quelles devraient être leurs valeurs et si elles sont optionnelles.

En React natif, soyez conscient que le passage des props peut être quelque chose que vous oubliez de faire. De plus, vous pourriez ne pas passer une certaine prop à un composant, si vous le souhaitez.

## 2. Les props React passées avec seulement leur nom ont une valeur de true

Chaque prop doit recevoir une valeur associée fournie après l'opérateur d'égalité.

Mais que se passe-t-il lorsque nous ne fournissons pas cet opérateur d'égalité ainsi qu'une valeur ?

Si vous fournissez simplement le nom de la prop sur un composant sans rien d'autre, vous passez une valeur booléenne de true pour cette prop au composant. Il n'est pas nécessaire d'écrire qu'une prop est égale à true.

Au lieu de cela, vous pouvez simplement inclure la valeur de la prop, et elle recevra la valeur booléenne true lorsque vous l'utiliserez dans un composant auquel vous la passez.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/props-2-min.gif)

## 3. Les props React peuvent être accessibles en tant qu'objet ou déstructurées

Il existe plusieurs modèles que nous pouvons utiliser pour accéder aux valeurs des props dans nos composants.

Les props peuvent être accessibles en tant qu'objet entier généralement appelé "props". Ou elles peuvent être déstructurées, puisque les props seront toujours un objet, en variables séparées.

Si vous avez beaucoup de props que vous passez à votre composant, il peut être préférable de les inclure dans l'objet props entier et d'y accéder en disant `props.propName`.

Cependant, si vous n'avez que quelques props que vous passez à votre composant, vous pouvez les déstructurer immédiatement dans les paramètres de votre composant fonctionnel.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/props-3-min.gif)

Vous pouvez utiliser la déstructuration d'objets ES6 pour inclure un ensemble d'accolades dans les paramètres de votre composant fonctionnel, et immédiatement extraire les propriétés de l'objet, ainsi que les déclarer en tant que variables séparées.

Cela réduit notre code et élimine le besoin de dire `props.propName` pour obtenir chaque valeur de prop.

## 4. Les composants React peuvent être passés en tant que props (y compris les enfants)

Nous avons vu que les props sont très flexibles, et si nous ne les passons pas à un composant, aucune erreur ne sera levée.

Cette flexibilité s'étend également à ce que nous pouvons passer en tant que prop. Non seulement les éléments JSX peuvent être passés en tant que props aux composants, mais nous pouvons également passer d'autres composants en tant que props.

En fait, il existe un type spécial de prop qui est automatiquement fourni sur l'objet props appelé `children`.

> Nous recevons tous les enfants pour un composant donné si des composants ou éléments sont passés entre les balises d'ouverture et de fermeture de ce composant.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/props-4-min.gif)

La prop children nous permet de composer nos composants de manière puissante.

Cela est particulièrement utile lorsque nous devons envelopper un composant autour d'un autre, par exemple pour le style, ou pour passer plus de données de composant aux composants enfants, pour donner deux exemples :

1. Les props children sont très utiles lorsque vous souhaitez créer un composant de mise en page générique et donner la même mise en page à tous les composants qui sont passés en tant qu'enfants.
2. De plus, les children sont utiles lorsque vous souhaitez placer un fournisseur de contexte de React context autour de votre arbre de composants pour fournir facilement ce qui est placé sur le fournisseur de contexte à tous ses composants enfants afin qu'ils puissent recevoir les mêmes données.

## 5. N'importe quoi peut être passé en tant que prop dans React (surtout des fonctions)

Toute valeur JavaScript normale peut être passée en tant que props, y compris des fonctions.

Il existe des modèles puissants qui ont émergé, grâce à la capacité de passer des fonctions en tant que props. Un modèle très courant consiste à passer une fonction à un composant enfant en tant que prop, qui peut mettre à jour l'état du composant parent, puis à l'appeler dans ce composant enfant.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/props-5-min.gif)

> L'utilisation de cette fonction qui est passée pour mettre à jour l'état du parent et effectuer une fonction est appelée "remonter l'état".

De plus, il existe d'autres modèles, tels que le modèle render props, qui impliquent également de passer une fonction à un composant enfant pour qu'elle soit ensuite rappelée et effectue une fonction inter-composants.

## 6. Mettre à jour la valeur d'une prop React avec l'état

Les props ne peuvent pas être mises à jour directement.

Pour passer une valeur de prop à un composant, nous ne pouvons pas, dans ce composant fonctionnel, tenter de changer immédiatement la valeur de cette prop.

> Les valeurs des props doivent être pures. En d'autres termes, elles ne peuvent pas être mutées ou changées directement.

Nous savons que dans React, si nous voulons changer des valeurs au fil du temps, le moyen approprié de le faire est avec l'état.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/props-6-min.gif)

Si nous souhaitons passer une valeur de prop à un composant et la changer plus tard, nous pouvons la donner à un hook React stateful pour stocker cette valeur en tant que variable. Ensuite, nous pouvons la mettre à jour plus tard en utilisant la fonction setter appropriée. Nous pouvons le faire avec le hook `useState` ou le hook `useReducer`, par exemple.

## 7. Les props React peuvent être étalées individuellement

Que se passe-t-il si nous avons un objet dont les propriétés nous voulons passer en tant que valeurs de props individuelles ?

Cet objet a beaucoup de propriétés, cependant. Devons-nous créer manuellement des props individuelles et définir la prop à `object.propertyName` ?

Non – au lieu de faire cela pour chaque propriété, nous pouvons très facilement prendre l'objet et étaler ses propriétés à un composant en tant que valeurs de props individuelles en utilisant l'opérateur de propagation d'objet `{...myPropObject}`.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/props-7-min.gif)

En utilisant cette syntaxe, qui est une fonctionnalité d'ES7, cela nous permet de créer automatiquement des props individuelles selon les noms des propriétés d'un objet, sans avoir à écrire tous ces noms de propriétés.

C'est très pratique lorsque vous travaillez avec de grands objets ayant beaucoup de propriétés que vous souhaitez passer en tant que props individuelles à un composant.

## 8. Les props React peuvent recevoir une valeur par défaut si aucune n'est fournie

Que se passe-t-il si nous savons déjà que nous passons une prop à une instance d'un composant, mais que nous ne passons pas cette prop à une autre instance de celui-ci ?

Ou peut-être que je sais que la prop pourrait ne pas avoir de valeur. Que faisons-nous pour lui donner une valeur par défaut au lieu de simplement la valeur `undefined` si aucune valeur de prop n'est passée ?

Si nous utilisons la déstructuration pour accéder à cette prop dans notre composant fonctionnel, nous pouvons utiliser l'opérateur d'égalité pour lui donner une valeur par défaut. Ainsi, si aucune valeur de prop n'est passée pour cette prop, nous pouvons utiliser l'opérateur d'égalité à côté et la définir à une meilleure valeur par défaut.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/props-8-min.gif)

Définir une valeur par défaut est très important car la valeur par défaut normale pour une prop est `undefined`. Cela peut nous aider à éviter les erreurs qui pourraient résulter de l'absence de la valeur de prop attendue.

## 9. Les props React peuvent être renommées pour éviter les erreurs

De plus, que se passe-t-il s'il y a un conflit de nommage avec l'une de nos props ?

Que se passe-t-il si nous utilisons un nom de prop dans de nombreux composants déjà et que nous voyons qu'il y a une autre valeur dans notre composant qui a le même nom de variable ?

Au lieu de devoir aller partout et renommer toutes nos valeurs de prop sur toutes nos instances de nos composants, nous pouvons simplement utiliser un deux-points après ce nom de prop, si nous la déstructurons, pour lui donner un alias.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/props-9-min.gif)

En d'autres termes, nous lui donnons un nom différent juste dans cette instance. Cela évitera le conflit de nommage ainsi que l'erreur.

## 10. Ne tentez pas de déstructurer les props React plusieurs fois

Si nous déstructurons un objet de notre objet props, soyez conscient qu'il est possible de déstructurer cette prop encore plus loin dans ses propriétés constitutives.

Cependant, il n'est généralement pas recommandé de le faire à moins que vous ne soyez très confiant que cet objet aura toujours ces propriétés.

Si l'une de ces propriétés est manquante et que vous tentez de la déstructurer à plusieurs niveaux de profondeur, cela peut vous donner une erreur assez désagréable lorsque vous essayez d'accéder à une propriété qui n'existe pas.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/props-10-min.gif)

Notez que vous pouvez utiliser la déstructuration autant que vous le souhaitez, mais cela peut être difficile à lire jusqu'à un certain point et cela peut également être peu fiable. Si vous essayez d'accéder à une propriété sur un objet, qui peut ne pas exister, cela provoquera une erreur.

## Vous voulez garder ce guide pour référence future ?

**[Cliquez ici pour télécharger le guide au format PDF](https://reedbarger.com/resources/react-props-2021).**

Voici 3 avantages rapides que vous obtenez lorsque vous téléchargez la version :

* Vous obtiendrez des tonnes de snippets de code copiables pour une réutilisation facile dans vos propres projets.
* C'est un excellent guide de référence pour renforcer vos compétences en tant que développeur React et pour les entretiens d'embauche.
* Vous pouvez prendre, utiliser, imprimer, lire et relire ce guide littéralement où vous le souhaitez.

## Devenez un Développeur React Professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*