---
title: Qu'est-ce qui rend Redux si génial ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-13T17:58:43.000Z'
originalURL: https://freecodecamp.org/news/whats-so-great-about-redux-ac16f1cc0f8b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BpaqVMW2RjQAg9cFHcX1pw.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Redux
  slug: redux
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce qui rend Redux si génial ?
seo_desc: 'By Justin Falcone

  Redux elegantly handles complex state interactions that are hard to express with
  React’s component state. It is essentially a message-passing system, like the kind
  seen in Object-Oriented programming, but implemented as a library in...'
---

Par Justin Falcone

Redux gère élégamment les interactions d'état complexes qui sont difficiles à exprimer avec l'état des composants React. C'est essentiellement un système de passage de messages, comme celui vu en programmation orientée objet, mais implémenté sous forme de bibliothèque plutôt que dans le langage lui-même[¹](#535d). Comme en OOP, Redux inverse la responsabilité du contrôle du demandeur au receveur — l'UI ne manipule pas directement l'état mais envoie plutôt un message à l'état pour qu'il l'interprète.

À travers ce prisme, un store Redux est un objet, les reducers sont des gestionnaires de méthodes, et les actions sont des messages. `store.dispatch({ type: "foo", payload: "bar" })` est équivalent au `store.send(:foo, "bar")` de Ruby. Les middlewares sont utilisés de manière similaire à la programmation orientée aspect (par exemple, `before_action` de Rails) et `connect` de React-Redux est une injection de dépendances.

#### Pourquoi est-ce souhaitable ?

* L'inversion de contrôle décrite ci-dessus garantit que l'UI n'a pas besoin d'être mise à jour si l'implémentation des transitions d'état change. L'ajout de fonctionnalités complexes comme la journalisation, l'annulation ou même le débogage par voyage dans le temps est presque trivial. Les tests d'intégration se résument à vérifier que la bonne action est dispatchée ; le reste peut être testé unitairement.
* L'état des composants React est assez maladroit pour l'état qui touche plusieurs parties de votre application, comme les informations utilisateur et les notifications. Redux vous offre un arbre d'état indépendant de votre UI pour gérer ces préoccupations transversales. De plus, avoir votre état en dehors de l'UI facilite des choses comme la persistance — vous n'avez besoin de gérer la sérialisation vers localStorage ou les URLs qu'à un seul endroit.
* Les « reducers » de Redux offrent une flexibilité incroyable pour gérer les actions — composition, dispatch multiple, même analyse de style `method_missing`.

#### Ce sont tous des cas inhabituels. Qu'en est-il des cas courants ?

Eh bien, voilà le problème.

* Une action _pourrait_ être interprétée comme une transition d'état complexe, mais la plupart d'entre elles définissent une seule valeur. Les applications Redux finissent par avoir un tas d'actions qui définissent une seule valeur ; cela rappelle distinctement l'écriture manuelle de fonctions setters en Java.
* Un fragment d'état _pourrait_ être utilisé dans toute votre application, mais la plupart des états correspondent 1:1 à une seule partie de l'UI. Placer cet état dans Redux plutôt que dans l'état du composant ajoute simplement de l'_indirection_ sans _abstraction_.
* Une fonction reducer _pourrait_ faire toutes sortes de bizarreries de métaprogrammation, mais dans la plupart des cas, elle se contente de dispatcher en fonction du champ type de l'action. Cela est bien dans des langages comme Elm et Erlang, où la correspondance de motifs est concise et très expressive, mais plutôt maladroit en JavaScript avec des instructions `switch`.

Mais la chose vraiment insidieuse, c'est que lorsque vous passez tout votre temps à faire le code standard pour les cas courants, vous oubliez que de meilleures solutions pour les cas spéciaux _existent même_. Vous rencontrez une transition d'état complexe et vous la résolvez avec une fonction qui dispache une douzaine d'actions différentes de définition de valeur. Vous dupliquez l'état dans le reducer plutôt que de distribuer une seule tranche d'état dans l'application. Vous copiez et collez des cas de switch dans plusieurs reducers au lieu de les abstraire dans des fonctions partagées.

Il est facile de rejeter cela comme une simple « erreur d'opérateur » — ils n'ont pas lu le manuel, un mauvais artisan blame ses outils — mais la fréquence de ces problèmes devrait soulever quelques inquiétudes. Que dit-on d'un outil si la plupart des gens l'utilisent mal ?

#### Dois-je donc éviter Redux pour les cas courants et le réserver pour les cas spéciaux ?

C'est le conseil que l'équipe Redux vous donnera — et c'est le conseil que je donne à mes propres membres d'équipe : je leur dis de l'éviter jusqu'à ce que l'utilisation de setState devienne vraiment insoutenable. Mais je ne peux pas me résoudre à suivre mes propres règles, car il y a toujours _une_ raison pour laquelle vous voulez utiliser Redux. Vous pourriez avoir un tas d'actions `set_$foo`, mais la définition de toute valeur _met également_ à jour l'URL, ou réinitialise une valeur plus transitoire. Peut-être avez-vous une correspondance claire 1:1 de l'état à l'UI, mais vous _voulez également_ avoir de la journalisation ou de l'annulation.

La vérité est que je ne sais pas comment écrire, et encore moins _enseigner_, un « bon Redux ». Chaque application sur laquelle j'ai travaillé est pleine de ces anti-modèles Redux, soit parce que je n'ai pas pu penser à une meilleure solution moi-même, soit parce que je n'ai pas pu convaincre mes coéquipiers de la changer. Si le code d'un « expert » Redux est médiocre, quel espoir a un novice ? Si quoi que ce soit, j'essaie simplement de contrebalancer l'approche dominante « Redux pour tout ! » dans l'espoir qu'ils pourront comprendre Redux à leur manière.

#### Que faire dans ce cas ?

Heureusement, Redux est suffisamment flexible pour que des bibliothèques tierces puissent s'intégrer avec lui pour gérer les cas courants — [Jumpstate](https://github.com/jumpsuit/jumpstate) par exemple. Et pour être clair, je ne pense pas qu'il soit faux pour Redux de se concentrer sur les choses de bas niveau. Mais l'externalisation de ces fonctionnalités de base à des tiers crée une charge cognitive supplémentaire et une opportunité de discussions interminables — chaque utilisateur doit essentiellement construire son propre framework à partir de ces parties.

#### Certaines personnes aiment ce genre de choses.

Et j'en fais partie ! Mais tout le monde ne l'est pas. J'adore personnellement Redux et je l'utilise pour presque tout ce que je fais, mais j'_adore aussi_ essayer de nouvelles configurations Webpack. Je ne suis pas représentatif de la population générale. Je suis _autonomisé_ par la flexibilité d'écrire mes propres abstractions sur Redux, mais à quel point suis-je autonomisé par les abstractions écrites par un ingénieur senior qui ne les a jamais documentées et qui a démissionné il y a six mois ?

Il est tout à fait possible de _ne jamais_ rencontrer les problèmes difficiles que Redux est particulièrement bon à gérer, surtout si vous êtes junior dans une équipe où ces tickets vont aux ingénieurs plus seniors. Votre expérience de Redux est « cette bibliothèque bizarre que tout le monde utilise où vous devez écrire tout trois fois ». Redux est suffisamment simple pour que vous _puissiez_ l'utiliser mécaniquement, sans compréhension approfondie, mais c'est une expérience sans joie et peu gratifiante.

Cela me ramène à une question que j'ai soulevée plus tôt : que dit-on d'un outil si la plupart des gens l'utilisent mal ? Un outil manuel de qualité n'est pas seulement utile et durable — il est agréable à utiliser. L'endroit le plus confortable pour le tenir est le bon endroit pour le tenir. Il est conçu non seulement pour sa tâche mais aussi pour son utilisateur. Un outil de qualité reflète l'empathie de l'artisan pour l'utilisateur.

Où est notre empathie ? Pourquoi « vous le faites mal » est-il notre réaction, et non « nous pourrions rendre cela plus facile à utiliser » ?

Il existe un phénomène lié dans les cercles de programmation fonctionnelle que j'aime appeler la _Malediction du Tutoriel de Monade_ : expliquer comment ils fonctionnent est trivial, mais expliquer pourquoi ils sont précieux est surprenamment difficile.

#### Allez-vous sérieusement glisser un tutoriel sur les monades au milieu de cet article ?

Les monades sont un motif courant en Haskell utilisé pour travailler avec une large gamme de calculs — listes, gestion des erreurs, état, temps, IO. Il existe un sucre syntaxique, sous la forme de la notation `do`, qui permet de représenter des séquences d'opérations monadiques d'une manière qui ressemble un peu à du code impératif, un peu comme les générateurs en javascript peuvent rendre le code asynchrone synchronisé.

Le premier problème est que décrire les monades en termes de ce pour quoi elles sont utilisées est inexact. [Les monades ont été introduites en Haskell pour gérer les effets secondaires et le calcul séquentiel](http://homepages.inf.ed.ac.uk/wadler/papers/marktoberdorf/baastad.pdf), mais les monades en tant que concept abstrait n'ont rien à voir avec les effets secondaires ou les séquences ; elles sont un ensemble de règles pour la façon dont une paire de fonctions devrait interagir et n'ont aucune signification inhérente. Le concept d'associativité _s'applique_ à l'arithmétique et aux opérations sur les ensembles et à la concaténation de listes et à la propagation des nulls mais il existe pleinement indépendamment d'eux.

Le deuxième problème est que tout exemple concis d'une approche monadique de X est plus verbeux — et donc au moins _visuellement_ plus complexe — que l'approche impérative. Les types d'option explicites à la `Maybe` sont plus sûrs que la vérification des `null` implicites mais entraînent plus de code, plus laid. La gestion des erreurs avec les types `Either` est souvent plus simple à suivre que le code qui peut `throw` de n'importe où, mais lancer est certainement plus concis que la propagation manuelle des valeurs. Et les effets secondaires — état, IO, etc. — sont triviaux dans un langage impératif. Les enthousiastes de la programmation fonctionnelle (moi y compris) soutiendraient que les effets secondaires sont _trop faciles_ dans ces langages, mais convaincre quelqu'un que tout type de programmation est trop facile est une vente difficile.

La vraie valeur n'est visible qu'à l'échelle macro — non seulement que l'un de ces cas d'utilisation suit les lois des monades, mais que tous suivent les _mêmes_ lois. Un ensemble d'opérations qui fonctionne dans un cas peut fonctionner dans _tous_ les cas : zipper une paire de listes en une liste de paires est « la même chose » que fusionner une paire de promesses en une seule promesse qui se complète avec une paire de résultats.

#### Cela mène-t-il quelque part ?

Le point est que Redux a le même problème — il est difficile à enseigner non pas parce qu'il est difficile mais plutôt parce qu'il est si _simple_. La compréhension n'est pas tant une question de connaissance que de confiance dans l'idée centrale de telle sorte que nous puissions déduire tout le reste par induction.

Il est difficile de partager cette compréhension parce que les idées centrales sont des truismes banals (éviter les effets secondaires) ou abstraits au point d'être dénués de sens (`(prevState, action) => nextState`). Tout exemple concret unique ne sert à rien ; ils montrent la verbosité de Redux sans démontrer son expressivité.

Une fois que nous sommes ✨éclairés✨, beaucoup d'entre nous oublient immédiatement ce que cela faisait avant. Nous oublions que notre éclaircissement n'est venu que par nos propres échecs et incompréhensions répétés.

#### Que proposez-vous donc ?

J'aimerais que nous admettions que nous avons un problème. Redux est [simple, mais il n'est pas facile](https://www.infoq.com/presentations/Simple-Made-Easy). C'est un choix de conception valide, mais c'est néanmoins un compromis. Beaucoup de gens bénéficieraient d'un outil qui échangerait un peu de la simplicité contre la facilité d'utilisation. Mais de grandes parties de la communauté ne reconnaîtront même pas qu'un compromis a été fait !

Je pense qu'il est intéressant de comparer React et Redux car, bien que React soit un logiciel bien plus compliqué et ait une surface d'API significativement plus grande, il semble somehow plus facile à utiliser et à comprendre. Les seules fonctionnalités d'API absolument nécessaires de React sont `React.createElement` et `ReactDOM.render` — l'état, le cycle de vie des composants, même les événements DOM auraient pu être gérés ailleurs. Intégrer ces fonctionnalités dans React l'a rendu plus compliqué, mais elles l'ont aussi rendu _meilleur_.

« L'état atomique » est un concept abstrait qui peut informer votre travail une fois que vous le comprenez, mais `setState` est une méthode que vous pouvez appeler sur un composant React qui gère l'état atomique pour vous, que vous le compreniez ou non. Ce n'est pas une solution parfaite — elle est moins efficace que de remplacer l'état directement ou de le muter et de forcer une mise à jour, et elle a quelques pièges lorsqu'elle est appelée de manière asynchrone — mais React est bien meilleur avec `setState` en tant que méthode appelable plutôt qu'en tant que terme de vocabulaire.

À la fois l'équipe Redux et la communauté sont [fortement opposées à l'expansion de la surface de l'API de Redux](https://github.com/reactjs/redux/issues/2295), mais l'approche actuelle consistant à coller un tas de petites bibliothèques ensemble est fastidieuse même pour les experts et incompréhensible pour les débutants. Si Redux ne peut pas s'étendre pour avoir un support intégré pour les cas courants, il a besoin d'un framework « béni » pour prendre cette place. [Jumpsuit](https://github.com/jumpsuit/jumpsuit) pourrait être un bon début — il réifie les concepts d'« actions » et d'« état » en fonctions appelables tout en préservant leur nature plusieurs-à-plusieurs — mais la bibliothèque réelle n'a pas autant d'importance que l'acte de bénédiction lui-même.

L'ironie dans tout cela est que la _raison d'être_ de Redux est « l'expérience du développeur » : Dan a construit Redux parce qu'il voulait comprendre et recréer le débogueur voyageur dans le temps d'Elm. Mais alors qu'il développait sa propre identité — alors qu'il devenait le runtime OOP de facto de l'écosystème React — il a abandonné une partie de cette concentration sur le DX en échange de la configurabilité. Cela a permis à l'écosystème Redux de s'épanouir, mais il y a une absence remarquable où un framework humain et curaté devrait être. Nous, la communauté Redux, sommes-nous prêts à le créer ?

_Merci à [Matthew McVickar](https://www.freecodecamp.org/news/whats-so-great-about-redux-ac16f1cc0f8b/undefined), [a pile of moss](https://www.freecodecamp.org/news/whats-so-great-about-redux-ac16f1cc0f8b/undefined), [Eric Wood](https://www.freecodecamp.org/news/whats-so-great-about-redux-ac16f1cc0f8b/undefined), [Matt DuLeone](https://twitter.com/Crimyon), et [Patrick Thomson](https://twitter.com/importantshock) pour la relecture._

_Notes de bas de page :_

**[1] Pourquoi faites-vous une distinction entre react / JS et la programmation orientée objet ? JavaScript EST orienté objet, juste pas basé sur les classes.**

La programmation orientée objet, comme la programmation fonctionnelle, est une méthodologie, pas une fonctionnalité de langage. Certains langages _supportent_ mieux ce style que d'autres, ou ont une bibliothèque standard conçue pour le style, mais si vous êtes suffisamment dédié à la tâche, vous pouvez écrire dans un style orienté objet dans n'importe quel langage.

JavaScript a une structure de données qu'il appelle un Object, et _la plupart_ des valeurs dans le langage peuvent être traitées comme des objets, dans le sens où il existe des méthodes que vous pouvez appeler sur chaque valeur sauf pour `null` et `undefined`. Mais avant l'arrivée des Proxies dans ES6, chaque appel de "méthode" sur un objet était une recherche de dictionnaire ; `foo.bar` va toujours trouver une propriété nommée "bar" sur foo ou sa chaîne de prototypes. Contrastez cela avec un langage comme Ruby, où `foo.bar` envoie le message `:bar` à foo -- ce message peut être _intercepté_ et _interprété_, il n'a pas besoin d'être une recherche de dictionnaire.

Redux est essentiellement un système d'objets plus lent mais plus sophistiqué sur le système existant de JavaScript, où les reducers et les middlewares agissent comme des interprètes et des interceptors autour de l'objet JavaScript qui contient réellement l'état. [[retour](#6a79)]