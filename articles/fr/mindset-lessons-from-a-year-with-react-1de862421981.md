---
title: Les leçons les plus importantes que j'ai apprises après un an de travail avec
  React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-30T16:36:41.000Z'
originalURL: https://freecodecamp.org/news/mindset-lessons-from-a-year-with-react-1de862421981
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TheYckj9udF4qLjoJW8sjg.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Les leçons les plus importantes que j'ai apprises après un an de travail
  avec React
seo_desc: 'By Tomas Eglinskas

  Starting out with a new technology can be quite troublesome. You usually find yourself
  in a sea of tutorials and articles, followed by millions of personal opinions. And
  every single one states that they found the “right and perfec...'
---

Par Tomas Eglinskas

Commencer avec une nouvelle technologie peut être assez problématique. On se retrouve généralement dans un océan de tutoriels et d'articles, suivis de millions d'opinions personnelles. Et chacun d'eux affirme avoir trouvé la **"bonne et parfaite méthode"**.

Cela nous laisse débattre si notre tutoriel choisi sera une perte de temps ou non.

Avant de plonger dans l'océan, nous devons comprendre les concepts sous-jacents d'une technologie. Ensuite, nous devons développer une mentalité basée sur la technologie. Si nous commençons à apprendre React, nous devons d'abord penser en React. Ce n'est que plus tard que nous pourrons commencer à mélanger diverses mentalités en une seule.

Dans cet article, nous allons aborder certaines leçons que j'ai apprises concernant cette mentalité à partir de mes expériences personnelles avec React. Nous allons parler des jours de travail et des nuits avec des projets personnels, et même de la conférence que j'ai donnée lors d'un événement local JavaScript.

Alors, c'est parti !

### React évolue, donc vous devez être à jour

Si vous vous souvenez de l'annonce initiale de la version 16.3.0, vous vous souvenez à quel point tout le monde était excité.

Voici quelques-uns des changements et améliorations que nous avons reçus :

* API de Contexte Officielle
* API createRef
* API forwardRef
* StrictMode
* Changements du Cycle de Vie des Composants

L'équipe principale de React et tous les contributeurs font un excellent travail pour améliorer la technologie que nous adorons tous. Et dans la version 16.4.0, nous avons reçu les [Événements de Pointeur](https://reactjs.org/blog/2018/05/23/react-v-16-4.html).

D'autres changements sont sûrement à venir, et ce n'est qu'une question de temps : le rendu asynchrone, la mise en cache, la version 17.0.0 et bien d'autres encore inconnus.

Donc, si vous voulez être au top, vous devez être à jour avec ce qui se passe dans la communauté.

Sachez comment les choses fonctionnent et pourquoi elles sont développées. Apprenez quels problèmes sont résolus et comment le développement est facilité. Cela vous aidera vraiment.

### N'ayez pas peur de diviser votre code en plus petits morceaux

React est basé sur les composants. Vous devriez donc tirer parti de ce concept et ne pas avoir peur de diviser les plus grandes pièces en plus petites.

Parfois, un simple composant peut être fait de 4 à 5 lignes de code, et dans certains cas, c'est tout à fait acceptable.

Faites en sorte que si une nouvelle personne arrive, elle n'ait pas besoin de jours pour comprendre comment tout fonctionne.

```
// n'est-ce pas facile à comprendre ?
```

```
return (  [   <ChangeButton    onClick={this.changeUserApprovalStatus}    text="Changeons cela !"   />,   <UserInformation status={status}/>   ]);
```

Vous n'avez pas à faire des composants qui ont tous une logique complexe intégrée. Ils peuvent être uniquement visuels. Si cela améliore la lisibilité du code et les tests, et réduit les odeurs de code futures, c'est une grande victoire pour toute l'équipe.

```
import ErrorMessage from './ErrorMessage';
```

```
const NotFound = () => (  <ErrorMessage    title="Oups ! Page non trouvée."    message="La page que vous cherchez n'existe pas !"    className="test_404-page"  />);
```

Dans l'exemple ci-dessus, les propriétés sont statiques. Nous pouvons donc avoir un composant pur qui est responsable du message d'erreur du site web `Not Found`, et rien de plus.

De plus, si vous n'aimez pas avoir des classes CSS comme noms de classe partout, je vous recommande d'utiliser des composants stylisés. Cela peut améliorer considérablement la lisibilité.

```
const Number = styled.h1`  font-size: 36px;  line-height: 40px;  margin-right: 5px;  padding: 0px;`;//..
```

```
<Container>  <Number>{skipRatePre}</Number>  <InfoName>Taux de saut</InfoName></Container>
```

Si vous avez peur de créer plus de composants à cause de la pollution de vos dossiers avec des fichiers, repensez la façon dont vous structurez votre code. J'ai été utiliser la [structure fractale](https://hackernoon.com/fractal-a-react-app-structure-for-infinite-scale-4dab943092af) et c'est génial.

### Ne vous limitez pas aux bases — devenez avancé

Vous pourriez parfois penser que vous ne comprenez pas quelque chose assez bien pour passer aux choses avancées. Mais souvent, vous ne devriez pas trop vous en soucier — relevez le défi et prouvez-vous que vous avez tort.

En abordant les sujets avancés et en vous poussant, vous pouvez comprendre davantage les bases et comment elles sont utilisées pour des choses plus grandes.

Il existe de nombreux modèles que vous pouvez explorer :

* Composants Composés
* Composants d'Ordre Supérieur
* Render Props
* Composants Intelligents/Dumb
* beaucoup d'autres (essayez le Profiling)

Explorez-les tous, et vous saurez pourquoi et où ils sont utilisés. Vous deviendrez plus à l'aise avec React.

```
// cela ressemble à de la magie ?// ce n'est pas si difficile quand on essaie
```

```
render() {  const children = React.Children.map(this.props.children,   (child, index) => {      return React.cloneElement(child, {        onSelect: () => this.props.onTabSelect(index)    });     });   return children;}
```

De plus, n'ayez pas peur d'essayer quelque chose de nouveau au travail — dans certaines limites, bien sûr ! Ne vous contentez pas d'expérimenter sur des projets personnels.

Les gens poseront des questions, et c'est normal. Votre tâche est de défendre votre travail et vos décisions avec des arguments solides.

Votre objectif devrait être de résoudre un problème existant, de faciliter le développement futur, ou simplement de nettoyer du code spaghetti. Même si vos suggestions sont rejetées, vous rentrerez chez vous en sachant plus qu'en restant silencieux.

### Ne compliquez pas trop les choses

Cela peut sembler être un contre-argument, mais c'est différent. Dans la vie, et partout, nous devons avoir un équilibre. Nous ne devons pas sur-ingénier pour frimer. Nous devons être pratiques. Écrivez du code qui est facile à comprendre et qui remplit son but.

Si vous n'avez pas besoin de Redux, mais que vous voulez l'utiliser parce que tout le monde l'utilise sans connaître son vrai but, ne le faites pas. Ayez une opinion et n'ayez pas peur de vous défendre si les autres vous poussent.

Parfois, vous pourriez penser qu'en utilisant les dernières technologies et en écrivant du code complexe, vous dites au monde :

"Je ne suis pas un junior, je deviens un mid/senior. Regardez ce que je peux faire !"

Pour être honnête, c'était ma mentalité au début de mon parcours de développeur. Mais avec le temps, vous comprenez que le code qui a été écrit sans frimer ou parce que "ça marche" est plus facile à vivre.

1. Les collègues peuvent travailler sur vos projets et vous n'êtes pas la seule personne responsable du développement / de la correction / des tests &**lt;insérer la tâche>.
2. L'équipe peut comprendre ce que les autres ont fait sans s'asseoir pendant une longue réunion. Quelques minutes suffisent pour discuter.
3. Lorsque votre collègue part en vacances pendant deux semaines, vous pouvez reprendre sa tâche. Et vous n'aurez pas à travailler dessus pendant 8 heures, car cela peut être fait en une heure.

Les gens respectent les personnes qui facilitent la vie des autres. Ainsi, si votre objectif est de gagner du respect, de monter en grade et de vous améliorer, visez à coder pour l'équipe et non pour vous-même.

Vous deviendrez le joueur d'équipe préféré de tous.

### Refactorisez, refactorisez et refactorisez — c'est normal

Vous changerez d'avis des dizaines de fois, bien que le chef de projet changera d'avis plus souvent. Les autres critiqueront votre travail, et vous le critiquerez. En conséquence, vous devrez changer votre code de nombreuses, nombreuses fois.

Mais ne vous inquiétez pas, c'est un processus d'apprentissage naturel. Sans fautes et erreurs, nous ne pouvons pas nous améliorer.

Plus nous tombons, plus il devient facile de se relever.

Mais voici un conseil : assurez-vous de tester votre logiciel actuel. Tests de fumée, unitaires, d'intégration, de snapshot — n'en ayons pas honte.

Tout le monde a fait face ou fera face à un scénario où un test aurait pu sauver un temps précieux.

Et si vous, comme beaucoup de gens, pensez que c'est une perte de temps, essayez de penser un peu différemment.

1. Vous n'aurez pas à vous asseoir avec votre collègue pour expliquer comment les choses fonctionnent.
2. Vous n'aurez pas à vous asseoir avec votre collègue pour expliquer pourquoi les choses ont cassé.
3. Vous n'aurez pas à corriger les bugs pour votre collègue.
4. Vous n'aurez pas à corriger les bugs qui ont été trouvés après 3 semaines.
5. Vous aurez le temps de faire ce que vous voulez.

Et ce sont des avantages assez grands.

### Si vous l'aimez, vous prospérerez

Au cours de l'année précédente, mon objectif était de devenir meilleur avec React. Je voulais donner une conférence à ce sujet. Je voulais que les autres en profitent avec moi.

Je pouvais rester toute la nuit à coder sans arrêt, à regarder diverses conférences et à profiter de chaque minute.

Le fait est que si vous voulez quelque chose, d'une manière ou d'une autre, tout le monde commence à vous aider. Et le mois dernier, j'ai donné ma première conférence sur React à un public de 200 personnes.

Pendant cette période d'un an, je suis devenu plus fort et plus à l'aise avec React — les divers modèles, paradigmes et fonctionnements internes. Je peux avoir des discussions avancées et enseigner aux autres sur des sujets que je craignais d'aborder.

Et aujourd'hui, je ressens toujours la même excitation et le même plaisir que ceux que je ressentais il y a un an.

Par conséquent, je recommanderais à tout le monde de se demander : "Aimez-vous ce que vous faites ?"

Si ce n'est pas le cas, continuez à chercher cette pièce spéciale dont vous pouvez parler pendant des heures, apprendre chaque nuit et être heureux.

Parce que nous devons trouver quelque chose qui est le plus proche de nos cœurs. Le succès ne peut pas être forcé, il doit être atteint.

Si je pouvais remonter un an dans le temps, voici ce que je me dirais pour me préparer avant le grand voyage à venir.

Merci d'avoir lu !

Si vous avez trouvé cet article utile, ???.