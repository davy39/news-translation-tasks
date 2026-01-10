---
title: 'Fondations Solides de React.js : Un Guide pour Débutants'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-31T21:06:44.000Z'
originalURL: https://freecodecamp.org/news/rock-solid-react-js-foundations-a-beginners-guide-c45c93f5a923
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wj5ujzj5wPQIKb0mIWLgNQ.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Fondations Solides de React.js : Un Guide pour Débutants'
seo_desc: 'By Rajat Saxena

  I’ve been working with React and React-Native for the last couple of months. I have
  already released two apps in production, Kiven Aa (React) and Pollen Chat (React
  Native). When I started learning React, I was searching for something...'
---

Par Rajat Saxena

Je travaille avec React et React-Native depuis les derniers mois. J'ai déjà lancé deux applications en production, [Kiven Aa](https://kivenaa.com) (React) et [Pollen Chat](https://play.google.com/store/apps/details?id=com.pollenchat.android) (React Native). Lorsque j'ai commencé à apprendre React, je cherchais quelque chose (un blog, une vidéo, un cours, peu importe) qui ne m'apprenne pas seulement à écrire des applications en React. Je voulais aussi que cela me prépare pour les entretiens.

La plupart des ressources que j'ai trouvées se concentraient sur l'un ou l'autre. Ainsi, cet article est destiné à ceux qui recherchent un mélange parfait de théorie et de pratique. Je vais vous donner un peu de théorie pour que vous compreniez ce qui se passe sous le capot, puis je vous montrerai comment écrire du code React.js.

Si vous préférez la vidéo, j'ai également ce cours entier sur YouTube. N'hésitez pas à y jeter un coup d'œil.

Plongeons-nous dans le sujet...

#### React.js est une bibliothèque JavaScript pour construire des interfaces utilisateur

Vous pouvez construire toutes sortes d'applications monopages. Par exemple, des messageries instantanées et des portails e-commerce où vous souhaitez afficher des changements sur l'interface utilisateur en temps réel.

### Tout est un composant

Une application React est composée de composants, _beaucoup de composants_, imbriqués les uns dans les autres. « Mais qu'est-ce que les composants ? », pourriez-vous demander.

Un composant est un morceau de code réutilisable, qui définit comment certaines fonctionnalités doivent apparaître et se comporter sur l'interface utilisateur. Par exemple, un bouton est un composant.

Regardons la calculatrice suivante, que vous voyez sur Google lorsque vous essayez de calculer quelque chose comme 2+2 = 4 –1 = 3 (calcul rapide !)

![Image](https://cdn-media-1.freecodecamp.org/images/1*NS9DykYDyYG7__UXJdysTA.png)
_Les marqueurs rouges désignent les composants_

Comme vous pouvez le voir sur l'image ci-dessus, la calculatrice a plusieurs zones — comme la _fenêtre d'affichage des résultats_ et le _pavé numérique_. Toutes ces zones peuvent être des composants séparés ou un seul composant géant. Cela dépend de la facilité avec laquelle on peut décomposer et abstraire les choses dans React.

Vous écrivez du code pour tous ces composants séparément. Ensuite, vous les combinez sous un seul conteneur, qui est lui-même un composant React. De cette manière, vous pouvez créer des composants réutilisables et votre application finale sera une collection de composants séparés travaillant ensemble.

Voici une façon d'écrire la calculatrice, montrée ci-dessus, en React :

Oui ! Cela ressemble à du code HTML, mais ce n'en est pas. Nous explorerons cela plus en détail dans les sections suivantes.

### Configuration de notre terrain de jeu

Ce tutoriel se concentre sur les fondamentaux de React. Il n'est pas principalement orienté vers React pour le Web ou [React Native](https://facebook.github.io/react-native/) (pour construire des applications mobiles). Ainsi, nous utiliserons un éditeur en ligne afin d'éviter les configurations spécifiques au Web ou au natif avant même d'apprendre ce que React peut faire.

J'ai déjà configuré un environnement pour vous sur [codepen.io](https://codepen.io/raynesax/pen/MrNmBM). Suivez simplement le lien et lisez tous les commentaires dans les onglets HTML et JavaScript (JS).

### Contrôle des composants

Nous avons appris qu'une application React est une collection de divers composants, structurés sous forme d'arbre imbriqué. Ainsi, nous avons besoin d'un mécanisme pour passer des données d'un composant à un autre.

#### Voici les "props"

Nous pouvons passer des données arbitraires à notre composant en utilisant un objet `props`. Chaque composant dans React reçoit cet objet `props`.

Avant d'apprendre à utiliser cet objet `props`, apprenons les composants fonctionnels.

#### a) Composant fonctionnel

Un composant fonctionnel dans React consomme des données arbitraires que vous lui passez en utilisant l'objet `props`. Il retourne un objet qui décrit ce que React doit rendre sur l'interface utilisateur. Les composants fonctionnels sont également connus sous le nom de **composants sans état**.

Écrivons notre premier composant fonctionnel :

C'est aussi simple que cela. Nous avons simplement passé `props` comme argument à une fonction JavaScript ordinaire et retourné, _euh, bien, qu'était-ce que c'était ? Cette chose `<div>{props.name}`</div> ! C'est du JSX (JavaScript Extended). Nous en apprendrons davantage à ce sujet dans une section ultérieure.

Cette fonction ci-dessus rendra le HTML suivant dans le navigateur :

Lisez la section ci-dessous sur le JSX, où j'ai expliqué comment nous obtenons ce HTML à partir de notre code JSX.

Comment pouvez-vous utiliser ce composant fonctionnel dans votre application React ? Je suis content que vous ayez posé la question ! C'est aussi simple que ce qui suit :

L'attribut `name` dans le code ci-dessus devient `props.name` à l'intérieur de notre composant `Hello`. L'attribut `age` devient `props.age` et ainsi de suite.

**Rappelez-vous !** Vous pouvez imbriquer un composant React à l'intérieur d'autres composants React.

Utilisons ce composant `Hello` dans notre terrain de jeu codepen. Remplacez le `div` à l'intérieur de `ReactDOM.render()` par notre composant `Hello`, comme suit, et voyez les changements dans la fenêtre du bas.

Mais que se passe-t-il si votre composant a un état interne ? Par exemple, comme le composant compteur suivant, qui a une variable de compte interne, qui change avec les pressions sur les touches + et —.

#### b) Composant basé sur une classe

Le composant basé sur une classe a une propriété supplémentaire `state`, que vous pouvez utiliser pour stocker les données privées d'un composant. Nous pouvons réécrire notre composant `Hello` en utilisant la notation de classe comme suit. Puisque ces composants ont un état, ils sont également connus sous le nom de **composants avec état**.

Nous étendons la classe `React.Component` de la bibliothèque React pour créer des composants basés sur des classes dans React. En savoir plus sur les classes JavaScript [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes).

La méthode `render()` **doit** être présente dans votre classe car React recherche cette méthode pour savoir quelle interface utilisateur il doit rendre à l'écran.

Pour utiliser ce type d'état interne, nous devons d'abord initialiser l'objet `state` dans le constructeur de la classe de composant, de la manière suivante.

De même, les `props` peuvent être accessibles à l'intérieur de notre composant basé sur une classe en utilisant l'objet `this.props`.

Pour définir l'état, vous utilisez `setState()` de `React.Component`. Nous verrons un exemple de cela, dans la dernière partie de ce tutoriel.

**Astuce :** Ne jamais appeler `_setState()` à l'intérieur de la fonction `_render()`, car `_setState()` provoque le re-rendu du composant et cela entraînera une boucle sans fin.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rPUhERO1Bnr5XdyzEwNOwg.png)
_Un composant basé sur une classe a une propriété optionnelle « state »._

Outre `state`, un composant basé sur une classe a certaines méthodes de cycle de vie comme `componentWillMount()`. Vous pouvez les utiliser pour faire des choses, comme initialiser le `state`, mais cela est hors du cadre de cet article.

### JSX

JSX est une forme abrégée de _JavaScript Extended_ et c'est une façon d'écrire des composants `React`. En utilisant JSX, vous obtenez toute la puissance de JavaScript à l'intérieur de balises de type XML.

Vous placez des expressions JavaScript à l'intérieur de `{}` . Voici quelques exemples valides de JSX.

Le fonctionnement est le suivant : vous écrivez du JSX pour décrire à quoi votre interface utilisateur doit ressembler. Un [transpileur](https://en.wikipedia.org/wiki/Source-to-source_compiler) comme `Babel` convertit ce code en une série d'appels `React.createElement()`. La bibliothèque React utilise ensuite ces appels `React.createElement()` pour construire une structure arborescente d'éléments DOM (dans le cas de React pour le Web) ou de vues natives (dans le cas de React Native) et la conserve en mémoire.

React calcule ensuite comment il peut imiter efficacement cet arbre en mémoire de l'interface utilisateur affichée à l'utilisateur. Ce processus est connu sous le nom de [réconciliation](https://reactjs.org/docs/reconciliation.html). Une fois ce calcul terminé, React apporte les modifications à l'interface utilisateur réelle à l'écran.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ighKXxBnnSdDlaOr5-ZOPg.png)
_Comment React convertit votre JSX en un arbre qui décrit l'interface utilisateur de votre application_

Vous pouvez utiliser [Babel's online REPL](https://babeljs.io/repl) pour voir ce que React produit réellement lorsque vous écrivez du JSX.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NRuBKgzNh1nHwXn0JKHafg.png)
_Utilisez Babel REPL pour transformer JSX en JavaScript simple_

#### Puisque JSX n'est qu'un sucre syntaxique sur des appels `React.createElement()` simples, React peut être utilisé sans JSX

Maintenant que nous avons tous les concepts en place, nous sommes bien positionnés pour écrire un composant `counter` que nous avons vu précédemment sous forme de GIF.

Le code est le suivant et j'espère que vous savez déjà comment le rendre dans notre terrain de jeu.

Voici quelques points saillants concernant le code ci-dessus.

1. JSX utilise `camelCasing` donc l'attribut `button` est `onClick`, et non `onclick`, comme nous l'utilisons en HTML.
2. La liaison est nécessaire pour que `this` fonctionne sur les rappels. Voir les lignes #8 et 9 dans le code ci-dessus.

Le code interactif final se trouve [ici](https://codepen.io/raynesax/pen/QaROqK).

Avec cela, nous avons atteint la conclusion de notre cours intensif sur React. J'espère avoir éclairé le fonctionnement de React et comment vous pouvez utiliser React pour construire des applications plus grandes, en utilisant des composants plus petits et réutilisables.

Si vous avez des questions ou des doutes, contactez-moi sur Twitter [@rajat1saxena](https://twitter.com/rajat1saxena) ou écrivez-moi à [rajat@raynstudios.com](mailto:rajat@raynstudios.com).

Veuillez recommander cet article si vous l'avez aimé et partagez-le avec votre réseau. Suivez-moi pour plus de publications liées à la technologie et envisagez de vous abonner à ma chaîne [Rayn Studios](https://www.youtube.com/channel/UCUmQhjjF9bsIaVDJUHSIIKw) sur YouTube. Merci beaucoup.