---
title: Comment utiliser les hooks React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-08T09:33:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-react-hooks-ef70894d9fd
coverImage: https://cdn-media-1.freecodecamp.org/images/0*ayfiDWDbZ9rrvmd4
tags:
- name: frontend
  slug: frontend
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment utiliser les hooks React
seo_desc: 'By Sergei Gannochenko

  React 16.7.0 is finally out. It has no hooks on-board, but sooner or later, React
  Hooks will be there. So today we will have a talk so we’re ready to use it right
  away when it is time ?

  Sometimes when you write your pure functio...'
---

Par Sergei Gannochenko

React 16.7.0 est enfin sorti. Il n'a pas de hooks intégrés, mais tôt ou tard, les React Hooks seront là. Alors aujourd'hui, nous allons en parler pour être prêts à les utiliser dès qu'ils seront disponibles ?

Parfois, lorsque vous écrivez votre composant de fonction pure, vous réalisez qu'à un moment donné, vous avez besoin d'avoir une sorte de drapeau qui indique qu'une modale est ouverte, qu'un compteur est incrémenté ou... peu importe. Et puis votre deuxième pensée est : "oh, maintenant je dois migrer vers React.Component". Eh bien, avec les hooks, ce n'est plus nécessaire !

Je vais supposer que vous avez Node dans l'une des versions suivantes installées : 6.14.0, 8.10.0 ou supérieure à 9.10. Si ce n'est pas le cas, vous pouvez toujours utiliser le gestionnaire de versions de Node pour régler cela. Gardez à l'esprit cependant que nous devrons installer tous les packages globaux au cas où nous changerions de version de Node.

Cet article nécessite que vous ayez au moins une connaissance de base de React, y compris les concepts de "composant" et de "fonction pure", ainsi que "l'état" et le "cycle de vie du composant". Mais même si ce n'est pas le cas, ne vous inquiétez pas, vous rattraperez pendant le processus, ce sera amusant !

#### Étape 1 : Le Boilerplate

Ouvrez votre terminal, car nous allons utiliser un générateur de code super célèbre pour les applications React, appelé _create-react-app_ :

```
npm install create-react-app -gcreate-react-app react-hooks
```

Maintenant, nous pouvons voir un dossier appelé `./react-hooks`, alors nous y allons et considérons cela comme la racine de notre application.

Pour activer les hooks, nous devons nous rendre sur la liste des versions de React sur [npmjs.com](https://www.npmjs.com/package/react). Au moment où cet article a été écrit, la dernière version avec les hooks activés était [16.7.0-alpha.2](https://www.npmjs.com/package/react/v/16.7.0-alpha.2), alors installons celle-ci. Nous devons également installer un package complémentaire appelé _react-dom_ de la même version exacte.

Donc,

```
npm install react@16.7.0-alpha.2 --savenpm install react-dom@16.7.0-alpha.2 axios --save
```

N'oubliez pas de démarrer l'application :

```
npm start
```

#### Étape 2 : useState()

Trouvons le fichier `./src/App.js` et réécrivons-le comme ceci :

Et voici le premier type de hooks que nous pouvons utiliser : un hook d'état créé avec _useState()_. En gros, _useState()_ accepte la valeur initiale d'une certaine valeur et retourne un tableau, où le premier élément est une variable avec la valeur initiale, et le second est une fonction qui nous permet de changer la variable. Après avoir appelé _setCounter()_, le composant est réaffiché avec une valeur mise à jour du compteur.

Le code équivalent sans hooks serait :

Mais avec les hooks, le code est bien plus propre, et il ne repose même pas sur la programmation orientée objet et les déclarations _this_, qui peuvent parfois être vraiment cryptiques pour les développeurs JavaScript non expérimentés.

L'état peut être un objet complexe, aucun problème :

Mais selon la philosophie des hooks, il est préférable de définir deux valeurs d'état à la place :

Cela rend votre code vraiment facile à comprendre.

#### Étape 3 : useEffect()

Dans le monde React, un _effet de bord_ est une action qui est généralement exécutée sur les méthodes de cycle de vie _componentDidMount()_, _componentDidUpdate()_ et _componentWillUnmount()_ de _React.Component_. Mais que faire si nous voulons toujours avoir un effet de bord, mais avec une fonction pure ? Bien sûr ! Considérez le code :

La fonction à l'intérieur de _useEffect()_ est appelée lors du premier rendu et de tous les rendus suivants, ce qui ne fait pas vraiment de différence entre cela et si nous placions simplement le code à l'intérieur de la fonction du composant directement.

Mais, attendez. Ce n'est pas tout !

Nous pourrions faire quelques optimisations en disant à _useEffect()_ de s'exécuter uniquement lorsque certaines valeurs ont changé. Considérez ceci :

Ainsi, _useEffect()_ mémorisera la valeur de _[forBatman, forJoker]_ et ne réexécutera l'effet que si quelque chose a changé dans ces arguments.

Considérons d'autres cas d'utilisation.

#### Cas A : exécuter du code lors du démontage

Que faire si nous voulons capturer le moment où le composant est démonté ? Tout ce que nous avons à faire est de retourner une fonction comme ceci :

"SubComponent unmounted" apparaîtra dans la console dès que vous cliquerez sur le bouton "One for application" 5 fois.

#### Cas B : exécuter uniquement lors du montage et du démontage

Ce que nous pouvons également faire, c'est forcer un effet à s'exécuter uniquement lors du montage et du démontage, en passant un tableau vide comme dépendance :

Cela fonctionne parce que _[]_ reste le même pendant tout le temps où le composant est présent jusqu'à ce qu'il soit démonté, peu importe ce qui se passe.

#### Cas C : charger des données de manière asynchrone lors du montage et de la mise à jour

Le dernier cas d'utilisation que je souhaite démontrer est comment faire un effet asynchrone avec un chargement de données. Juste pour être clair, je ne pense pas que le fait d'avoir la logique de rendu des données et la logique de chargement des données au même endroit soit une bonne idée. Le principe de responsabilité unique nous dit qu'il devrait y avoir une logique de rendu pure et une logique métier riche, c'est pourquoi je vous encourage fortement à essayer _Redux_ + _Saga_. Mais je pense que c'est un bon sujet pour une autre fois.

Il y a deux moments importants à noter :

* nous ne pouvons pas utiliser _useEffect(async () => {}), les effets asynchrones ne sont pas supportés (encore), mais nous pouvons toujours utiliser des promesses,
* nous ne voulons pas que ce code s'exécute à chaque rendu, donc nous devons définir un deuxième argument pour _useEffect()_ de la bonne manière. Nous nous demandons toujours : "Qu'est-ce qui doit être changé pour réexécuter l'effet ?". La bonne réponse est "characterId".

#### Étape 4 : useRef() & useMemo()

Si nous ouvrons le code source de _React_, nous pouvons voir d'autres hooks disponibles. Parmi eux se trouve _useRef()_. Nous pouvons l'utiliser en combinaison avec _useEffect()_ pour faire certaines choses. Considérez le code :

Ce qu'il fait, c'est simplement définir la valeur d'un champ de saisie puis appeler _focus()_ dès que le composant est monté.

Un autre hook intéressant est _useMemo()_. Il nous permet essentiellement de mémoriser une valeur pendant le processus de rendu.

Pourquoi faire cela ? Eh bien, dans le cas où nous devons calculer quelque chose de raisonnablement lourd (lourd lors du rendu, hein ?), ou faire un appel distant, mais seulement lorsque certaines valeurs changent, nous pourrions utiliser _useMemo()_. Ce n'est toujours pas aussi puissant que les méthodes traditionnelles de mémorisation, car il ne peut être utilisé que lors du rendu, mais quand même...

#### Étape 5 : Sous le capot

Vous vous demandez peut-être comment cette fonctionnalité fonctionne même ? Je veux dire, les composants sont juste des fonctions pures, comment les variables préservent-elles leurs valeurs scalaires entre les appels de fonction ? Eh bien, par exemple, _useState()_ retourne un tableau, dont nous utilisons le premier argument comme un scalaire. Mais ce tableau peut être mémorisé à l'intérieur de _React_, donc la prochaine fois que le moteur de rendu est là, il sait déjà quelles valeurs mettre dans ces scalaires.

#### Étape 6 : À ne pas faire

* Tout d'abord, les hooks sont encore en phase alpha, l'API peut être modifiée à l'avenir, alors utilisez-les en production à vos risques et périls.
* Vous ne pouvez pas utiliser les hooks en dehors d'une fonction de composant, c'est simplement ainsi qu'ils fonctionnent. Mais vous pouvez faire [une composition de hooks](https://reactjs.org/docs/hooks-custom.html).
* React repose sur un **nombre** et un **ordre** d'apparition des hooks dans la fonction du composant. Alors **ne pensez même pas** à envelopper ces appels avec une logique conditionnelle de quelque sorte. Au lieu de cela, vous pouvez mettre vos _if-s_ à l'intérieur du corps d'un hook.
* À l'heure actuelle, les hooks ne fonctionnent pas pour le rendu côté serveur. J'espère que cela sera corrigé dans la version finale.

#### Conclusion

Même si les hooks ne sont pas officiellement disponibles, ils vont définitivement rendre notre vie plus facile et le code bien plus propre. Et il est toujours important d'avoir un code compréhensible, surtout lorsque l'on travaille avec React.

Merci d'avoir lu ! Si l'article vous a été utile, n'hésitez pas à le partager sur les réseaux sociaux ! :)

#### Extras

* voici [le dépôt de preuve de concept](https://github.com/awesome1888/poc_react-hooks) créé pour l'article
* envisagez de lire la [référence officielle des Hooks](https://reactjs.org/docs/hooks-reference.html) par Facebook

Bon Reacting !