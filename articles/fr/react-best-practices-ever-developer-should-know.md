---
title: Meilleures pratiques React que chaque développeur devrait connaître
subtitle: ''
author: Prankur Pandey
co_authors: []
series: null
date: '2024-10-03T16:51:27.436Z'
originalURL: https://freecodecamp.org/news/react-best-practices-ever-developer-should-know
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1727898200192/2b6b5882-f4e7-4cb5-9f97-4974669825fc.webp
tags:
- name: React
  slug: reactjs
- name: best practices
  slug: best-practices
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Meilleures pratiques React que chaque développeur devrait connaître
seo_desc: The more I study React.js, the more I fall in love with it. No doubt that
  it’s one of the most useful and loved front-end JavaScript libraries out there.
  And the improvements that the React team have made lately don’t just affect developers,
  but also...
---

Plus j'étudie React.js, plus je tombe amoureux de cette bibliothèque. Il ne fait aucun doute que c'est l'une des bibliothèques JavaScript front-end les plus utiles et appréciées. Et les améliorations récentes apportées par l'équipe React ne profitent pas seulement aux développeurs, mais aussi à ceux qui utilisent des applications construites avec React.

[Dans un article précédent](https://www.freecodecamp.org/news/learn-react-hooks-with-example-code/), j'ai parlé de divers Hooks React et de leur fonctionnement, avec des exemples de code et des explications détaillées.

Dans ce guide, je vais aborder certaines choses importantes que j'ai apprises en développant des applications React. Ces apprentissages sont optimisés pour l'utilisation des Hooks React. Nous allons démystifier quelques mythes courants, simplifier des concepts communs et optimiser votre code pour obtenir les meilleures performances.

### Ce que nous allons couvrir :

* [Comment ce guide vous sera-t-il utile ?](#heading-comment-ce-guide-vous-sera-utile)

* [Prérequis](#heading-prerequis)

* [L'état React doit être immutable](#heading-letat-react-doit-etre-immutable)

* [Ne pas utiliser l'état pour tout](#heading-ne-pas-utiliser-letat-pour-tout)

* [Dériver des valeurs sans état](#heading-deriver-des-valeurs-sans-etat)

* [Calculer des valeurs sans effets](#heading-calculer-des-valeurs-sans-effets)

* [Les clés doivent être uniques](#heading-les-cles-doivent-etre-uniques)

* [Utiliser useEffect en dernier recours](#heading-utiliser-useeffect-en-dernier-recours)

* [Conclusion](#heading-conclusion)

## Comment ce guide vous sera-t-il utile ?

Imaginons que vous avez un couteau et que je vous demande de découper des formes dans un morceau de tissu. Vous pourriez le faire, mais cela prendrait du temps et serait difficile avec un couteau. Au lieu de cela, que se passerait-il si je vous donnais une paire de ciseaux bien aiguisés et que je vous demandais de découper les motifs ? Ce serait beaucoup plus facile, n'est-ce pas ?

Ce guide est comme cette approche optimisée de découper du tissu avec des ciseaux au lieu d'un couteau. Je vais vous apprendre à utiliser React plus facilement, sans autant de difficultés. Nous discuterons des aspects importants du fonctionnement des Hooks React, et nous aborderons également quelques bonnes et mauvaises pratiques.

## Prérequis

Il n'y a qu'un seul prérequis principal pour suivre ce guide : vous devez avoir utilisé les Hooks React au moins une fois. Et par là, j'entends avoir développé une application avec React qui tire parti de la puissance des Hooks.

Cet article s'adresse à tous ceux qui souhaitent utiliser les Hooks React à leur plein potentiel.

## L'état React doit être immutable

Vous êtes-vous déjà demandé pourquoi React fait tant d'histoires sur l'immuabilité ? 🤔 En tant que débutant, vous pourriez penser que les mutations de JavaScript sont parfaitement acceptables. Après tout, nous ajoutons ou supprimons des propriétés d'objets et manipulons des tableaux avec facilité.

Mais voici le twist : dans React, l'immuabilité ne consiste pas à ne jamais changer l'état, mais à garantir la cohérence.

Lorsque vous modifiez l'état directement, React ne peut pas détecter les changements de manière fiable. Cela signifie que votre interface utilisateur pourrait ne pas se mettre à jour comme prévu. Le truc ? Remplacez les anciennes données par de nouvelles copies.

Par exemple, si vous devez ajouter un utilisateur, vous devez créer un nouveau tableau avec le nouvel utilisateur inclus, plutôt que de le pousser directement dans le tableau existant.

```javascript
const updatedUsers = [...users, newUser];
```

Le code `const updatedUsers = [...users, newUser];` utilise l'opérateur de décomposition pour créer un nouveau tableau, `updatedUsers`, qui combine les `users` existants avec `newUser`.

Cette approche maintient l'immuabilité dans React en ne modifiant pas le tableau `users` d'origine. Au lieu de cela, elle crée une nouvelle représentation de l'état, permettant à React d'optimiser le rendu et de garantir des changements d'état prévisibles. Lorsque vous mettez à jour l'état en utilisant `setUsers(updatedUsers);`, React re-rend la composante basée sur ce nouveau tableau, en respectant les meilleures pratiques de gestion d'état.

Cela garantit que React détecte le changement et re-rend votre composant en douceur.

## Ne pas utiliser `useState` pour tout

Temps de confession : je mettais tout dans `useState` sans réfléchir à deux fois. 🚀 Mais voici le scoop : tout n'a pas besoin d'être dans l'état. L'état est puissant, mais en abuser peut conduire à un code complexe et inefficace.

Envisagez des alternatives comme l'état du serveur, l'état de l'URL ou le stockage local. Pour les données du serveur, des bibliothèques comme React Query sont un game changer. Elles gèrent la récupération et la mise en cache afin que vous n'ayez pas à le faire manuellement. Pour l'état de l'URL, utilisez des hooks comme `useLocation` de React Router ou les méthodes intégrées de Next.js.

Liste de contrôle avant d'utiliser useState :

* Cette valeur est-elle simple et dérivable pendant le rendu ?

* Une bibliothèque gère-t-elle déjà cet état ?

* Doit-elle déclencher un re-rendu ?

* Si vous répondez « non » à toutes ces questions, vous n'avez peut-être pas besoin de `useState` du tout.

## Dériver des valeurs sans état

Voici un truc peu connu : les valeurs dérivées n'ont pas besoin de vivre dans l'état. 🚀 Si vos données peuvent être calculées à partir des états ou des props existants, calculez-les directement pendant le rendu.

Par exemple, le formatage d'une date peut être fait à la volée sans hooks supplémentaires :

```javascript
const formattedDate = new Date(date).toLocaleDateString();
```

Le code `const formattedDate = new Date(date).toLocaleDateString();` dérive une chaîne de date formatée à partir d'une entrée de `date` donnée sans la stocker dans l'état du composant. En créant `formattedDate` comme une constante, il calcule la valeur à la volée chaque fois qu'il est appelé, reflétant l'état actuel de `date`.

Cette approche évite une gestion d'état inutile, simplifie la logique de rendu et garde le composant efficace, car les valeurs dérivées sont recalculées uniquement lorsque les données sous-jacentes changent. Ainsi, elle promeut un style de programmation propre et fonctionnel dans React.

Cela garde vos composants propres et évite les mises à jour d'état inutiles.

## Calculer des valeurs sans effets

Arrêtez d'utiliser useEffect pour des calculs simples ! 🔥 Si votre valeur peut être calculée directement à partir de l'état ou des props et n'implique pas d'effets secondaires, faites-le pendant le rendu. Pour les calculs coûteux, enveloppez-les dans useMemo pour optimiser les performances :

```javascript
const expensiveValue = useMemo(() => computeExpensiveValue(data), [data]);
```

Le code `const expensiveValue = useMemo(() => computeExpensiveValue(data), [data]);` utilise le hook `useMemo` pour calculer une valeur (`expensiveValue`) basée sur l'entrée `data` sans déclencher d'effets secondaires.

Il mémorise le résultat de `computeExpensiveValue(data)`, le recalculant uniquement lorsque `data` change. Cette approche empêche les recalculs inutiles à chaque rendu, améliorant les performances pour les calculs coûteux.

En s'appuyant sur `useMemo`, le composant dérive efficacement la valeur en fonction de ses props ou de son état actuels, gardant le processus de rendu efficace et concentré sur les dernières données.

Cela réduit la complexité de votre code et garde vos composants concentrés.

## Les clés doivent être uniques

Coupable comme accusé : j'ai utilisé des index de tableau comme clés dans des listes auparavant. 😅 Mais saviez-vous que cela peut conduire à des bugs ? React s'appuie sur des clés uniques pour identifier les éléments, et l'utilisation de valeurs non uniques peut tout mélanger.

Générez des IDs uniques en utilisant crypto.randomUUID() mais assurez-vous de le faire uniquement lorsque votre état est mis à jour, et non à chaque rendu. Pour les objets, envisagez d'ajouter une propriété id :

```javascript
const itemWithId = items.map(item => ({ ...item, id: generateUniqueId() }));
```

Le code `const itemWithId =` [`items.map`](http://items.map)`(item => ({ ...item, id: generateUniqueId() }));` crée un nouveau tableau, itemWithId, où chaque élément du tableau items est augmenté avec un id unique.

L'opérateur de décomposition (`...item`) copie les propriétés de chaque élément, tandis que `generateUniqueId()` génère un nouvel identifiant unique. Cela garantit que chaque élément a une clé distincte, ce qui est crucial pour les composants React lors du rendu des listes.

Les clés uniques aident React à gérer efficacement les mises à jour, à identifier les changements et à optimiser les performances de rendu en distinguant les différents éléments de la liste.

## Ne pas oublier les dépendances

L'un des pièges cruels de React : oublier les dépendances dans `useEffect` peut conduire à des fermetures obsolètes. 😱 Par exemple, si votre `useEffect` n'inclut pas les dépendances dont il a besoin, il pourrait ne pas se mettre à jour comme prévu.

Vérifiez toujours vos tableaux de dépendances :

```javascript
useEffect(() => {
  // Logique de l'effet
}, [dependency]);
```

Le code `useEffect(() => { /* Logique de l'effet */ }, [dependency]);` définit un effet secondaire dans un composant React qui s'exécute lorsque la `dependency` spécifiée change. Il est essentiel d'inclure toutes les dépendances pertinentes dans le tableau des dépendances pour s'assurer que l'effet se comporte correctement.

Oublier des dépendances peut conduire à l'utilisation de valeurs obsolètes ou incorrectes dans l'effet, car React pourrait ne pas le réexécuter lorsque nécessaire. Inclure toutes les dépendances aide à maintenir la synchronisation entre l'état du composant et l'effet, garantissant un comportement prévisible et empêchant les bugs potentiels liés aux mises à jour manquantes.

Si votre interface utilisateur ne se met pas à jour correctement, c'est souvent le coupable.

## Utiliser `useEffect` en dernier recours

Voici un conseil pro : ne vous précipitez pas pour utiliser `useEffect`. 👨‍💻 C'est puissant mais peut conduire à un code désordonné si utilisé en excès. Les frameworks React fournissent des solutions pour gérer les effets secondaires de manière plus élégante. Pour la récupération de données, envisagez des bibliothèques comme TanStack Query ou SWR qui gèrent les requêtes et la mise en cache efficacement, conduisant à une meilleure expérience utilisateur.

Stratégies alternatives :

* Dérivez les valeurs directement.

* Répondez aux événements avec des gestionnaires.

Récupérez les données sur le serveur ou avec des bibliothèques dédiées.

## Conclusion

React est une bibliothèque robuste, mais savoir comment l'utiliser efficacement peut faire toute la différence. Ces leçons ne sont qu'un début.

Avoir une idée approfondie des tenants et aboutissants de toute technologie vous aide pendant le développement et l'optimisation.

React Js est la bibliothèque parfaite pour le développement moderne, elle a tout à offrir pour le développement et l'optimisation.

Merci d'avoir lu, et bon codage ! 🎉

* Suivez-moi sur X : [Twitter de Prankur](https://x.com/prankurpandeyy)

* Suivez-moi sur LinkedIn : [LinkedIn de Prankur](https://linkedin.com/in/prankurpandeyy)

* Consultez mon portfolio ici : [Portfolio de Prankur](https://prankurpandeyy.netlify.app)