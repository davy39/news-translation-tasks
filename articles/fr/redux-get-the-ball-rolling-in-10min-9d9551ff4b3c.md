---
title: Comment démarrer avec Redux en dix minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-16T12:56:18.000Z'
originalURL: https://freecodecamp.org/news/redux-get-the-ball-rolling-in-10min-9d9551ff4b3c
coverImage: https://cdn-media-1.freecodecamp.org/images/0*0OdJkNC70fPI3dih
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment démarrer avec Redux en dix minutes
seo_desc: 'By Eduardo Vedes

  Hi everyone ❤️

  For a while now I’ve been hearing my friends and colleagues complaining about how
  hard it was to get into Redux.

  I run a freeCodeCamp Study Group in the South of Portugal, Faro, so every week I
  try to motivate and ment...'
---

Par Eduardo Vedes

Salut à tous 

Depuis un certain temps, j'entends mes amis et collègues se plaindre de la difficulté à se lancer dans Redux.

Je dirige un groupe d'étude [freeCodeCamp](https://www.freecodecamp.org/) dans le sud du Portugal, à Faro. Chaque semaine, j'essaie de motiver et de mentor des codeurs qui ont beaucoup de difficultés à se lancer dans la programmation.

Dan Abramov a créé un cours d'introduction incroyable à Redux, que j'ai eu le plaisir de voir sur [egghead.io](https://egghead.io/courses/getting-started-with-redux), couvrant tous les aspects de Redux. De plus, le site de documentation Redux, [ici](https://redux.js.org/), est très complet.

Mais pour une raison quelconque, beaucoup de gens ne comprennent toujours pas Redux.

Le fait est que Redux a une courbe d'apprentissage considérable pour les débutants !

Vous devez comprendre beaucoup d'abstractions, adopter une approche plus fonctionnelle de la programmation en JavaScript, connaître de nombreuses fonctionnalités d'ES6 et bien comprendre de nombreux concepts JavaScript tels que l'immuabilité.

Ainsi, cela peut être très difficile pour ceux d'entre vous qui ont commencé React il y a quelques mois et qui sont très enthousiastes à l'idée d'abstraire votre état dans un store Redux.

Vous entendez les discussions autour de la machine à café sur la façon dont Redux excelle, sur la programmation propre, les sources uniques de vérité et les trois principes qui animent cette énorme bibliothèque "minuscule" (2kB)...

Alors, ne vous inquiétez pas, vous êtes au bon endroit ! Cet article est pour vous ! Et je vais vous montrer avec une approche de principe d'application d'abord à quel point il est facile de démarrer avec Redux.

Beaucoup d'encre a déjà été versée sur ce sujet, mais commençons. Laissez-moi essayer de vous présenter aussi rapidement que possible Mr. Redux dans un contexte React.

Pour commencer cette tâche herculéenne, je vais vous montrer comment créer une application de compteur très simple avec l'histoire utilisateur suivante :

1. afficher le nombre de comptage actuel ;
2. fournir à l'utilisateur deux boutons, pour incrémenter et décrémenter le nombre de comptage.

D'accord, à ce stade, vous pensez : je pourrais faire cela très rapidement avec un état local.

Vrai ! Et c'est la voie, mon ami ! Nous allons commencer avec un exemple React simple qui utilise un état local et nous allons transformer l'application en une application React-Redux.

Mais avant cela, laissez-moi vous présenter les concepts de base et les objectifs de Redux dans une introduction rapide.

### 01. Concepts de base

Redux a été créé par [Dan Abramov](https://twitter.com/dan_abramov), et il est défini comme un "conteneur d'état prévisible pour les applications JavaScript".

La motivation de Dan pour créer Redux était que la complexité des SPA augmentait beaucoup. Et nous étions laissés seuls pour gérer l'état de nos données avec deux concepts difficiles pour l'esprit humain à raisonner : **mutation** et **asynchronicité**. Il les appelle "**Mentos et Coke** — Les deux peuvent être formidables séparément, mais ensemble ils créent un désordre".

Ainsi, Redux propose de décrire l'état entier de votre application comme un objet simple. Pour changer quelque chose dans l'état, vous devez envoyer des actions. Les actions sont des objets JavaScript simples qui décrivent ce qui est arrivé à votre application.

Enfin, pour lier les actions et l'état ensemble, nous écrivons une fonction appelée un réducteur. Un réducteur est simplement une fonction JavaScript qui prend l'état et l'action comme arguments et retourne le nouvel état de l'application.

#### **Trois Principes de Redux :**

1. Source unique de vérité : l'état de votre application entière est stocké dans un arbre d'objets au sein d'un seul **store**.
2. L'état est en lecture seule. Cela signifie que la seule façon de changer l'état est d'émettre une **action** (un objet décrivant ce qui s'est passé).
3. Les changements sont effectués avec des **fonctions pures**. Les fonctions pures sont des fonctions qui retournent une valeur dépendant uniquement de la valeur de ses arguments. Elles n'ont pas d'effets secondaires observables. Lorsque vous appelez la même fonction avec le même argument, vous obtenez toujours la même valeur de retour. Les fonctions pures ne modifient pas non plus les arguments qu'elles reçoivent. Elles retournent en fait un nouvel objet, tableau ou fonction avec les modifications apportées.

### **02. L'Application Compteur (React avec état local, pas de Redux ici)**

D'accord, les amis, revenons à ce que nous faisions, créons notre petite application de compteur avec uniquement un état local.

Pour démarrer ce type de modèles, j'utilise toujours create-react-app (CRA) avec bootstrap (juste pour rendre les choses simples mais un peu plus élégantes).

J'ai gardé le src/index.js qui appelle le composant <App /> (jouant le rôle de la vue principale de l'application) et j'ai créé un petit composant avec état appelé Counter.

Si vous voulez jouer avec le code, vous pouvez le cloner depuis mon dépôt GitHub [ici](https://github.com/evedes/counter-app/tree/LocalStateApp) (garder à l'esprit qu'il est sur la branche LocalStateApp).

Alors, jetons un coup d'œil à ce dont nous avons besoin pour construire notre simple App.

![Image](https://cdn-media-1.freecodecamp.org/images/D7oGMjmZhHbkH-5aGrsFYyVbB2wKJ32Cl57F)
_src/index.js_

Aussi simple que cela soit prêt à l'emploi.

![Image](https://cdn-media-1.freecodecamp.org/images/LfeiVOAtJvydP5pSf8ngcWyM4FRzYLZ7idsL)
_src/App.js_

Je commence mon composant App en initialisant l'état avec une variable count qui par défaut est définie à zéro.

![Image](https://cdn-media-1.freecodecamp.org/images/WIyCmKfV29XKwuI7fIdkAftQcOB15ifHGpfO)
_méthode render()_

J'ai construit une méthode render très simple qui déstructure le count de l'état et affiche du texte. Elle appelle également le composant avec état Counter en lui passant la valeur du count, et appelle une petite méthode appelée renderButtons() pour rendre les boutons d'incrémentation/décrémentation.

![Image](https://cdn-media-1.freecodecamp.org/images/AjPshHrGsV12IhBPxjHOsywqUw2lt12XF5uG)
_Composant avec état Counter_

![Image](https://cdn-media-1.freecodecamp.org/images/QcurtfDoH4MBEwlsgK5qPubRpUJKKqaUJAoa)
_méthode renderButtons_

Les boutons appellent une méthode appelée updateCounter() et lui passent le type de mise à jour que nous voulons.

Ici, nous construisons déjà notre chemin vers Redux. Un détail des actions dans Redux est que, en plus d'être des objets simples qui dépendent de vous, elles doivent avoir une propriété type qui n'est pas indéfinie. (Gardez cela à l'esprit pour l'instant.)

![Image](https://cdn-media-1.freecodecamp.org/images/CR5ah94vMgnrFPzGljH2gEjLATrC2Om2VH4K)
_méthode updateCounter_

Ainsi, voici notre méthode updateCounter qui est très similaire à ce qu'est un réducteur dans Redux. Elle obtient l'état actuel de l'application, elle obtient l'action souhaitée, et à la fin, elle retourne le nouvel état de votre application.

Pas de magie du tout ! Redux est si naturel et facile que vous ne sentirez pas la différence du tout puisque vous connaissez deux ou trois petits détails qui rendent les choses très complexes et difficiles à comprendre.

Voici le résultat final de notre application :

![Image](https://cdn-media-1.freecodecamp.org/images/G9qdpo7NBsiR3KR4s75hrwaUHwHDKchE6J2o)
_Résultat de l'Application Compteur avec état local_

### 03. L'Application Compteur (avec état Redux)

D'accord, les amis ! Décomposons ce que nous avons fait jusqu'à présent.

Pour installer Redux, vous devez faire :

_npm install --save redux react-redux_

![Image](https://cdn-media-1.freecodecamp.org/images/wYWi4Ky3cZ0LFSXnxCayMxQ-FNBbQ7CU-lLT)
_package.json après l'installation de redux_

Ainsi, après avoir installé Redux, vos dépendances dans package.json devraient ressembler à ceci ?.

Maintenant, quoi ?

Cassons notre application ! Mais pas trop ! ?

Ainsi, ma première étape sera de supprimer l'état du composant App et de créer un store Redux dans index.js :

![Image](https://cdn-media-1.freecodecamp.org/images/-o10x3etp2xA3IkZhRpSPqlbp5GMQN4qtUoM)
_src/index.js : création d'un store dans Redux et passage d'informations à notre App principale._

Qu'avons-nous fait ici ? 

Nous avons modifié notre fichier principal index.js pour créer un Store Redux et le passer en tant que prop à notre composant <App />.

Vous avez peut-être remarqué les deux imports en haut : Provider et createStore.

Vous remarquerez également l'utilisation du HOC <Provider> autour de <App/>. Il fonctionne de l'extérieur en enveloppant notre application principale (il peut également envelopper le Router) afin de passer ses fonctions d'API en tant que props à notre application principale.

Mais attendez !

Qu'est-ce que le réducteur dans cette définition de variable ?

![Image](https://cdn-media-1.freecodecamp.org/images/Hueg-SUiUsvJeetET3WkSkKXZRl-vcydyVo8)
_création du store_

Oh, il nous manque le réducteur !

Ainsi, le store doit recevoir au moins une fonction de réducteur pour savoir comment les changements d'état opèrent.

Faisons-le !

Dans notre ancienne application, nous avions cette méthode updateCounter que nous disions être un peu un réducteur.

Ainsi, déplaçons-la vers index.js (vous pouvez également l'extraire dans un autre fichier et l'importer, mais gardons les choses simples pour l'instant).

![Image](https://cdn-media-1.freecodecamp.org/images/yqCK0TQoc2Kaykgi3dK9MG4Y7wGxlL7G35mf)

Ainsi, nous avons extrait la méthode updateCounter de notre composant App et nous l'avons un peu modifiée pour lui donner plus de contexte.

Nous l'avons appelée reducer. C'est le réducteur que nous voulons passer à la méthode createStore.

Nous avons également ajouté state comme argument car lorsque nous l'avons extrait du contexte du composant <App />, il n'est plus conscient d'aucun état. Nous avons également arrêté d'utiliser setState et avons commencé à retourner le nouveau count en fonction du type d'action que nous recevons (déstructuré de l'argument action).

Nous avons utilisé les fonctionnalités d'ES6 pour définir un initialState par défaut si state est indéfini. Souvenez-vous de ce que je vous ai dit ci-dessus ?, que state ne pouvait pas être indéfini. C'est l'une des conditions du réducteur Redux.

Mis à part cela, rien de nouveau pour tout le monde ! Devinez quoi ? Nous avons notre réducteur prêt et prêt à faire son travail !

Maintenant, concentrons-nous sur les actions !

Dans notre ancienne application, elles étaient l'invocation de updateCounter. Mais maintenant, comme vous vous en souvenez, nous devons utiliser la méthode dispatch() de Redux pour envoyer des actions, donc nous devons ajouter cette couche de l'API à notre application.

![Image](https://cdn-media-1.freecodecamp.org/images/244AJTbrC81zHYEVOusrww8FyczOb3U3uNjf)

Nous avons modifié seulement deux choses, les amis ! Nous avons obtenu la méthode dispatch, en la déstructurant des props. Souvenez-vous du HOC <Provider /> ? Son rôle est d'introduire ces quelques méthodes Redux dans votre application principale.

Au lieu d'appeler this.updateCounter, nous appelons maintenant une fonction updateCounter détachée en lui fournissant le type d'action (comme nous le faisions déjà dans l'ancienne application).

Voyons maintenant quelle est la nouvelle fonction updateCounter :

![Image](https://cdn-media-1.freecodecamp.org/images/Q3ZHdtRMkZvZEHqBGsFugjM4eht0XwB5JR2S)
_action updateCounter_

D'accord, rien de nouveau, nous recevons simplement la méthode dispatch et la retournons avec le type d'action que nous voulons déclencher.

À ce stade, nous avons déjà créé le store. Nous avons créé le réducteur pour obtenir l'état précédent de l'application et l'action et retourner le nouvel état. Nous avons construit une fonction d'action pour envoyer les actions de notre application.

Quoi de plus ? Cela devrait fonctionner maintenant ! Pourquoi ne fonctionne-t-il pas ?

Ohhh ! Notre composant App doit être connecté à Redux !

Ainsi, c'est notre dernière étape, tout le monde ! ?

![Image](https://cdn-media-1.freecodecamp.org/images/dsSibG5XXn43RklxNHQlBa8YlwQ66dwsmjmd)
_import connect de react-redux_

Nous commençons par importer la méthode connect de react-redux (dans notre fichier App.js).

Maintenant, à la fin de notre fichier, où nous faisons l'export default de notre composant, nous devons faire la connexion :

![Image](https://cdn-media-1.freecodecamp.org/images/EEdYOhBPEnPdtgEO0AL5KSofchFKn2QpM7uw)
_connect et mapStateToProps_

D'accord ! Souvenez-vous que nous avons supprimé l'état local de notre composant App ?

Alors... comment injectons-nous l'état du store dans notre composant ?

Nous devons faire un "mapStateToProps" ! Habituez-vous à cela car cela sera toujours nécessaire. Le composant App recevra le nouvel état en tant que prop. Vous n'avez plus de this.state !!

mapStateToProps obtient l'état de la méthode connect (HOC) et le lie au composant App.

Et c'est tout, tout le monde ! À ce stade, votre application devrait fonctionner.

N'hésitez pas à jeter un coup d'œil au code dans mon dépôt GitHub (branche ReduxStateApp) [ici](https://github.com/evedes/counter-app/tree/ReduxStateApp).

Bien sûr, il y a beaucoup de choses à apprendre après cela, mais c'est la première étape principale pour vous pour comprendre comment démarrer avec Redux.

Maintenant, je vous demande de faire le devoir : vérifiez les deux applications ! Assurez-vous de comprendre toutes les étapes et comparez-les. Mettez beaucoup de _console.log_ pour comprendre ce qui se passe, et surtout acceptez qu'il y a une API dans Redux qui a quelques règles strictes. Tout n'est pas si logique pour un niveau d'entrée comme on s'y attendrait ! Mais ce ne sont que de bonnes douleurs de croissance pour le bien de JavaScript !

Souvenez-vous toujours de rester fort et de continuer à coder, tout le monde 

Et gardez votre douleur sous contrôle avec un bon et chaud  

### 04. Bibliographie

01. [Documentation Redux](https://redux.js.org/)

02. Cours de Dan Abramov sur [Getting Started With Redux](https://egghead.io/courses/getting-started-with-redux) sur egghead.io