---
title: Un guide de GraphQL pour les développeurs front-end
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-17T21:20:07.000Z'
originalURL: https://freecodecamp.org/news/graphql-for-front-end-developers-1f59808f4435
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ATRODaaXUt35esV1CCFvwg.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Un guide de GraphQL pour les développeurs front-end
seo_desc: 'By Schalk Venter

  10 months ago, Artsy Engineering Lead, Alan Johnson proclaimed that ‘I have seen
  the future, and it looks a lot like GraphQL’.

  Fast-forward to exactly 13 days before I started this article, and Wired Magazine
  publishes a story title ...'
---

Par Schalk Venter

**Il y a 10 mois, [Artsy](https://www.artsy.net/) Engineering Lead, [Alan Johnson](http://artsy.github.io/author/alan/) a proclamé que [J'ai vu l'avenir, et il ressemble beaucoup à GraphQL](http://artsy.github.io/blog/2018/05/08/is-graphql-the-future/).**

**Avance rapide jusqu'à exactement 13 jours avant que je commence cet article, et [Wired Magazine](https://www.wired.com) publie une histoire intitulée [_Comment Facebook a changé l'informatique_](https://www.wired.com/story/how-facebook-has-changed-computing/), mettant en lumière [GraphQL](https://graphql.org/) comme l'une des technologies qui _a joué un rôle énorme non seulement dans la façon dont nous construisons nos serveurs mais aussi dans la façon dont nous écrivons du code_.**

Ce sont des affirmations audacieuses ! Je ne suis en aucun cas qualifié pour les contredire ou les confirmer. Cependant, pour moi, ce qui précède est indicatif de la rapidité astronomique avec laquelle l'écosystème GraphQL a grandi au cours des deux dernières années - peu importe que nous pensions que c'est pour le meilleur ou [pour le pire](https://news.ycombinator.com/item?id=13480049).

Cette croissance se reflète également dans mon expérience quotidienne en tant que développeur. En interne chez [OpenUp](https://openup.org.za), notre équipe a progressivement adopté GraphQL dans de plus en plus de nos produits, car il résout beaucoup de [points douloureux généralement associés aux points de terminaison de l'API REST](https://www.howtographql.com/basics/1-graphql-is-the-better-rest/). De plus, nous ne sommes pas seuls. GraphQL est largement utilisé par une gamme d'équipes technologiques internationales allant de [Pinterest](https://pinterest.com), [Twitter](https://twitter.com/), [Yelp](https://www.yelp.com/developers/graphql/guides/intro), [New York Times](https://www.nytimes.com/), [Paypal](https://www.paypal.com), [Atlassian](https://www.atlassian.com/), [Facebook](https://code.fb.com/core-data/graphql-a-data-query-language/), [Github](https://developer.github.com/v4/) ([entre autres](https://graphql.org/users/)) ; et des startups sud-africaines comme [GetTruck](https://gettruck.co.za), [Bettr](https://bettr.finance) et [Dine4Six](https://dine4six.com).

Après avoir lu l'article ci-dessus de Wired, j'ai réfléchi à mon propre parcours (parfois turbulent) à travers GraphQL, et j'ai pensé qu'il pourrait être utile de compiler un guide (espérons-le !) facile pour d'autres développeurs front-end intéressés à se lancer (et à éviter les pièges courants) dans l'apprentissage de GraphQL.

J'ai divisé le contenu ci-dessous en les sujets suivants, alors n'hésitez pas à sauter en avant si vous êtes seulement intéressé par un aspect spécifique de GraphQL :

* [Mon propre parcours d'apprentissage de GraphQL](#mon-propre-parcours-dapprentissage-de-graphql)
* [Alors, qu'est-ce que GraphQL exactement ?](#alors-quest-ce-que-graphql-exactement)
* [Quel problème GraphQL essaie-t-il de résoudre ?](#quel-probleme-graphql-essaye-t-il-de-resoudre)
* [L'équivalent GraphQL de Hello World !](#lequivalent-graphql-de-hello-world)
* [Dans quel ordre devrais-je apprendre les concepts de GraphQL ?](#dans-quel-ordre-devrais-je-apprendre-les-concepts-de-graphql)
* [Et le back-end ?](#et-le-back-end)

### Mon propre parcours d'apprentissage de GraphQL

**Lorsque j'ai entendu parler de GraphQL pour la première fois, je jouais avec une chose appelée [React](https://reactjs.org/) depuis un moment. J'avais utilisé un peu de [Backbone](http://backbonejs.org/) et [AngularJS](https://angularjs.org/) auparavant, mais aucun ne m'a vraiment marqué.**

Cependant, j'étais extrêmement excité par l'approche [fonctionnelle](https://en.wikipedia.org/wiki/Functional_programming) de React pour la gestion de l'état et l'utilisation d'un [Virtual DOM](https://reactjs.org/docs/faq-internals.html) pour réduire l'empreinte de performance des manipulations intensives du DOM. À cette époque, j'avais essentiellement créé ma propre fonction auxiliaire de type [HyperScript](https://github.com/hyperhype/hyperscript) pour faire ce qui précède et j'avais hâte de me débarrasser de cette dernière abomination en faveur de `React.createClass()` et `React.createElement()`.

Avant de donner un essai à ce qui précède dans un environnement de production, j'ai pensé qu'il était sage de demander à un membre senior de l'équipe ce qu'il pense de cette chose React. Pourtant, aucune bonne (ou peut-être prudente) action ne reste impunie : j'ai été rabroué avec le mépris habituel que beaucoup de développeurs back-end avaient à cette époque (et pour certains encore aujourd'hui) envers les frameworks JavaScript. Cependant (et peut-être comme un geste de bonne volonté), il a mentionné que cette chose GraphQL (sur laquelle l'équipe derrière React travaille) semble vraiment prometteuse.

Ce qui m'a conduit à ce qui suit :

* **Googler GraphQL.**
* **Lire quelques aperçus.**
* **Toujours ne pas avoir la moindre idée de ce qu'est GraphQL.**
* **Supposer que c'est probablement destiné aux développeurs web avec au moins un (ou plusieurs) diplôme(s) en informatique (je suppose que c'est toujours comme ça que je me sens à propos de [Web Assembly](https://webassembly.org/) et [Houdini](https://github.com/w3c/css-houdini-drafts))**
* **Continuer ma vie.**

Quelques années plus tard, après avoir été aspiré par la force gravitationnelle de la supernova front-end qu'est devenu l'écosystème React, j'ai commencé à jouer avec un autre outil appelé [Gatsby](https://www.gatsbyjs.org/). J'avais du mal à faire en sorte que [React Helmet](https://www.npmjs.com/package/react-helmet) fonctionne bien avec mon propre générateur de site statique React Frankenstein construit sur [static-site-generator-webpack-plugin](https://github.com/markdalgleish/static-site-generator-webpack-plugin).

J'ai en fait trouvé un message dans le canal `#react` [Slack](https://slack.com/) sur [ZA Tech](https://zatech.github.io/) qui encapsule bien la frustration que je ressentais à ce moment-là :

> **14 septembre 2017**

> Schalk Venter 16:02  
> Je manque peut-être quelque chose d'évident ici _?_

> Schalk Venter 16:38  
> Cependant, soit je ne comprends pas la documentation, soit le rendu côté serveur n'est pas aussi facile qu'ils le disent dans les docs. _?_

Ainsi, cette chose Gatsby semblait me donner ce que j'essayais de bricoler par d'autres moyens. Cependant, j'ai été confronté à une frustration supplémentaire lorsque j'ai réalisé que Gatsby était de mèche avec mon précédent ennemi, GraphQL (comme moyen d'interroger le front-matter et le contenu textuel des fichiers [Markdown](https://en.wikipedia.org/wiki/Markdown)). Cependant, revenir à mon bazar Frankenstein ne semblait pas non plus être une option convaincante.

_Il s'avère que je n'avais vraiment pas le choix à ce stade, je devais apprendre GraphQL._

Cela signifiait que je devais trouver des réponses aux questions suivantes :

* [Alors, qu'est-ce que GraphQL exactement ?](#alors-quest-ce-que-graphql-exactement)
* [Quel problème GraphQL essaie-t-il de résoudre ?](#quel-probleme-graphql-essaye-t-il-de-resoudre)
* [L'équivalent GraphQL de Hello World !](#lequivalent-graphql-de-hello-world)
* [Dans quel ordre devrais-je apprendre les concepts de GraphQL ?](#dans-quel-ordre-devrais-je-apprendre-les-concepts-de-graphql)
* [Et le back-end ?](#et-le-back-end)

### Alors, qu'est-ce que GraphQL exactement ?

> J'ai vu l'avenir, et il ressemble beaucoup à GraphQL. Marquez mes mots : dans 5 ans, les nouveaux développeurs full-stack ne débattront plus de la _RESTfulness_, car la conception des API REST sera obsolète. [] Il vous permet de modéliser les ressources et les processus fournis par un serveur comme un langage spécifique à un domaine (DSL). Les clients peuvent l'utiliser pour envoyer des scripts écrits dans votre DSL au serveur pour les traiter et y répondre par lots.

>  [Alan Johnson](http://artsy.github.io/author/alan/) ([GraphQL est-il l'avenir ?](http://artsy.github.io/blog/2018/05/08/is-graphql-the-future/))

**_Yikes,_ ce n'était probablement pas la réponse que je (ni vous, cher lecteur) cherchions !**

#### Domain-what-a-thing ?

Cependant, aussi effrayante que la définition ci-dessus puisse paraître, il est important de la déballer un peu si nous voulons comprendre ce qu'est exactement GraphQL.

_Commençons par le terme langage spécifique à un domaine :_

1. **Tout d'abord et avant tout,** un langage spécifique à un domaine (également appelé _mini-langage_) est un langage de programmation créé pour exprimer un type d'information numérique très spécifique et prédéfini (un domaine). Alors qu'un [langage à usage général](https://en.wikipedia.org/wiki/General-purpose_programming_language) comme [JavaScript](https://en.wikipedia.org/wiki/JavaScript) peut (similaire à un couteau suisse) être utilisé pour exprimer une gamme d'informations numériques ([et dans certains cas, même des informations que ses créateurs n'avaient pas anticipées à l'origine](http://www.jsfuck.com/)). Cela inclut tout, des primitives de bas niveau comme les [objets](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object), les [fonctions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function), les [chaînes de caractères](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String), les [symboles](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol) aux motifs de programmation généraux comme les [requêtes HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods), les manipulations de [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model) et/ou le [stockage de données en ligne](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API)). Les langages spécifiques à un domaine tendent à être plus limités (et intentionnellement) dans ce qu'ils sont capables d'exprimer par rapport aux langages de programmation à usage général.
2. **Deuxièmement,** les DSL sont souvent intégrés à d'autres DSL ou à des langages à usage général pour profiter de la fonctionnalité existante (en raison de leur portée limitée). Cependant, cela ne signifie pas que les DSL sont liés à des langages spécifiques (GraphQL étant un exemple de cela). Par exemple, le (plus ou moins obsolète maintenant) [XForms](https://en.wikipedia.org/wiki/XForms) DSL peut être utilisé à l'intérieur de [HTML](https://en.wikipedia.org/wiki/HTML) (qui est lui-même un DSL sur un autre DSL appelé [SGML](https://en.wikipedia.org/wiki/Standard_Generalized_Markup_Language)), tout en pouvant également être utilisé dans un langage à usage général comme [Java](https://en.wikipedia.org/wiki/Java_(programming_language)).

**_Cela devient un peu trop geek ?_**

D'accord, revenons-en ! Vous avez probablement plus d'expérience avec les DSL que vous ne le pensez (et pas seulement à travers HTML !), mais un ou plusieurs des éléments suivants :

* [_CSS_](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [_JSON_](https://en.wikipedia.org/wiki/JSON)
* [YAML](https://en.wikipedia.org/wiki/YAML)
* [_XML_](https://en.wikipedia.org/wiki/XML)

De plus, vous avez probablement déjà une expérience de première main de leur portée étroite. La plupart des gens lèveront les yeux au ciel si j'essaie de gérer une base de données au moyen de HTML ou de [contrôler une combinaison spatiale](https://foundation.nodejs.org/wp-content/uploads/sites/50/2017/09/Node_CaseStudy_Nasa_FNL.pdf) via CSS.

#### La vraie valeur des DSL

**Cependant, en raison de leur portée très étroite, les DSL tendent à être extrêmement expressifs (en d'autres termes, faciles à lire et à écrire) par rapport aux langages à usage général.**

_Par exemple :_

Un ami (et ex-collègue) à moi, [Greg Kempe](https://www.freecodecamp.org/news/graphql-for-front-end-developers-1f59808f4435/undefined), utilise un DSL appelé [Akoma Ntoso](http://www.akomantoso.org/) (construit sur [XML](https://en.wikipedia.org/wiki/XML)) dans son projet à but non lucratif appelé [Open By-laws](https://openbylaws.org.za). Akoma Ntoso (signifiant cœurs liés en [Akan](https://en.wikipedia.org/wiki/Akan_language)) est un DSL construit exclusivement pour exprimer des documents parlementaires, législatifs et judiciaires de manière numérique.

Par exemple, voir ci-dessous une section de [la réglementation sur les enseignes extérieures de la ville du Cap](https://openbylaws.org.za/za-cpt/act/by-law/2001/outdoor-advertising-signage/eng/) (exprimée en Akoma Ntoso) :

#### Ramener cela au développement front-end

Pour illustrer ce qui précède dans le contexte du développement front-end, nous pouvons regarder un exemple courant où nous mettons à jour le [Document Object Model](https://en.wikipedia.org/wiki/Document_Object_Model) (DOM) de notre site web via [JavaScript](https://en.wikipedia.org/wiki/JavaScript) (afin d'afficher un message spécifique lorsqu'un utilisateur est connecté) :

Vous pouvez le voir en action dans l'exemple Codepen suivant :

Aussi puissant que soit JavaScript (même avec la syntaxe ES6 ci-dessus), il n'est pas très expressif lors de la manipulation du DOM. Heureusement, il existe un DSL spécialement conçu pour mieux exprimer les nœuds DOM du navigateur. Vous le connaissez peut-être sous le nom de HTML (ou par son nom complet : Hypertext Markup Language).

Cela signifie que nous pouvons utiliser la propriété `innerHTML` (ajoutée à JavaScript avec [_Internet Explorer 4_](https://en.wikipedia.org/wiki/Internet_Explorer_4)) pour réécrire ce qui précède. La propriété `innerHTML` accepte une chaîne écrite en DSL HTML :

Comme vous pouvez le voir, nous obtenons toujours le même comportement exact :

#### Une dernière chose

Enfin, avant de nous plonger dans le DSL GraphQL lui-même, il pourrait être utile de faire une distinction entre les DSL et les langages [superset](https://en.wikipedia.org/wiki/Subset) comme [TypeScript](https://en.wikipedia.org/wiki/TypeScript) ou [Sass](https://en.wikipedia.org/wiki/Sass_(stylesheet_language)). Alors qu'un langage superset est destiné à étendre la grammaire d'un langage existant, un DSL n'a pas besoin de se conformer à un langage ou un environnement sous-jacent. Par exemple, [JSX](https://en.wikipedia.org/wiki/React_(JavaScript_library)#JSX) (construit sur [XML](https://en.wikipedia.org/wiki/XML)) peut être utilisé pour interagir directement avec le DOM du navigateur ou un [système d'exploitation mobile](https://en.wikipedia.org/wiki/Mobile_operating_system) sous la forme d'une [application mobile](https://en.wikipedia.org/wiki/Mobile_app) (au moyen de [React Native](https://facebook.github.io/react-native/)).

_Arrêtez avant de taper cette réponse en colère ! Je suis conscient que la distinction ci-dessus entre les DSL/langages à usage général et les DSL/langages superset est floue dans de nombreux cas, et (comme la différence contestée entre les sites web et les applications web) est sujette au [paradoxe de Sorites](http://Sorites paradox). Cependant, comme c'est le cas pour tous les cas du paradoxe de Sorites, les distinctions floues existent (en dépit de leur manque de rigueur scientifique) spécifiquement en raison de la valeur qu'elles fournissent lorsqu'elles expliquent la nature des expériences quotidiennes. Donc, appelons simplement la définition ci-dessus la [définition de travail](https://en.wiktionary.org/wiki/working_definition) de cet article des DSL._

### Quel problème GraphQL essaie-t-il de résoudre ?

De manière similaire à ce qui précède, GraphQL a été créé en interne par [l'équipe technique derrière Facebook](https://github.com/facebook) en 2012 en tant que DSL pour écrire des requêtes de données plus expressives (et puissantes) dans l'application mobile Facebook (vers une API de données distante).

![Image](https://cdn-media-1.freecodecamp.org/images/1*ikw1LeJXVlyPGxA7C0_svQ.png)

**Le problème : Les approches courantes de l'API [REST (ou Representational State Transfer)](https://en.wikipedia.org/wiki/Representational_state_transfer) reposent principalement sur des structures de données fixes. Cela signifie qu'après suffisamment d'itérations, la plupart des API REST finissent par nécessiter une [Hydre de Lerne](https://en.wikipedia.org/wiki/Lernaean_Hydra) de requêtes pour obtenir une pièce spécifique de données.**

En bref (comme noté par [Chimezie Enyinnaya](https://blog.pusher.com/author/mezie/), un créateur de contenu nigérian pour [Pusher](https://pusher.com/)  un service qui gère la messagerie pub/sub à distance) :

> Avec REST, nous pourrions avoir un point de terminaison `/authors/:id` pour récupérer un auteur, puis un autre point de terminaison `/authors/:id/posts` pour récupérer les publications de cet auteur particulier. Enfin, nous pourrions avoir un point de terminaison `/authors/:id/posts/:id/comments` qui récupère les commentaires sur les publications. [] Il est facile de récupérer plus de données que nécessaire avec REST, car chaque point de terminaison dans une API REST a une structure de données fixe qu'il est censé retourner chaque fois qu'il est appelé.

>  [Chimezie Enyinnaya](https://blog.pusher.com/author/mezie/) ([REST versus GraphQL](https://blog.pusher.com/rest-versus-graphql/))

En fait, cela est si courant que GraphQL n'est qu'une des plusieurs solutions qui ont été imaginées pour résoudre ce problème :

> Intéressamment, d'autres entreprises comme Netflix ou Coursera travaillaient sur des idées comparables pour rendre les interactions avec les API plus efficaces. Coursera envisageait une technologie similaire pour permettre à un client de spécifier ses besoins en données et Netflix a même open-sourcé leur solution appelée Falcor.

>  [How to GraphQL](https://www.howtographql.com) ([GraphQL fundamentals: Introduction](https://www.howtographql.com/basics/0-introduction/))

Cependant, contrairement à certaines des solutions ci-dessus, GraphQL a été publié trois ans plus tard sous la [licence MIT](https://en.wikipedia.org/wiki/MIT_License) et constitue aujourd'hui l'épine dorsale de services open-source comme [Apollo](https://www.apollographql.com/) (utilisant GraphQL pour lire et/ou modifier l'état local et distant des applications) ou même [Gatsby](https://www.gatsbyjs.org/) (utilisant GraphQL pour interroger le front-matter et le contenu textuel des fichiers markdown).

**Alors sans plus tarder, passons au cœur de cette section : Un exemple de travail concret qui illustre réellement comment GraphQL résout le problème ci-dessus.**

Pour l'argument, disons que je veux connaître le [nombre d'utilisateurs qui me suivent sur Github](https://github.com/schalkventer?tab=followers). Nous pouvons facilement récupérer les données via la méthode native JavaScript fetch (à partir de [l'API REST de Github](https://developer.github.com/v3/)), puis afficher une liste de noms d'utilisateur dans le DOM via une liste non ordonnée (au moyen de l'exemple `innerHTML` illustré ci-dessus) :

**Étonnamment simple, non ?**

Cependant, obtenir une liste de followers ne nous dit pas grand-chose. Nous voulons avoir une idée de la notoriété de ces utilisateurs sur Github (puisqu'un suivi de [Dan Abramov](https://twitter.com/dan_abramov) devrait être pondéré différemment d'un suivi de Johnny le stagiaire de l'équipe). Pour y parvenir, j'utiliserai le concept extrêmement non scientifique, que je nomme désormais _Github Equity_ (similaire au concept de moteur de recherche de [Link Equity](https://moz.com/learn/seo/what-is-link-equity)). _Github Equity_ sera calculé au moyen du nombre total de dépôts maintenus par un utilisateur et de leur propre nombre de followers.

En bref :

`Total Repositories * Total Followers`

**Plutôt facile ! Cependant, obtenir les données nécessaires pour effectuer ce calcul est un peu plus délicat, car cela nécessiterait plusieurs requêtes REST asynchrones (nécessitant une certaine orchestration au moyen de [Promesses JavaScript natives](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)) :**

En tant que requêtes de données, ce qui précède est encore bien dans les limites de ce qui serait considéré comme raisonnable. Cependant, tous les appels d'API REST nécessaires (s'exécutant en parallèle !) rendent le code extrêmement difficile à lire et à modifier. Cela signifie que même si nous n'obtenons les informations nécessaires que des 10 premiers followers, cela représenterait un total de 31 appels d'API REST. Ce qui signifie que nous atteignons rapidement la [limite de taux par défaut de l'API Github](https://developer.github.com/apps/building-github-apps/understanding-rate-limits-for-github-apps/) (une limite sur le nombre de requêtes que l'API accepte d'une IP spécifique dans un laps de temps d'une heure)

Vous pouvez voir cela se produire dans le [Codepen](https://codepen.io/schalkventer/pen/ef4598c518037d83bb006529a2d7ad30) ci-dessous, où il devrait sortir l'erreur suivante dans le DOM s'il est exécuté plusieurs fois en une seule heure (cliquez sur le bouton `rerun` dans le coin inférieur droit plusieurs fois) : `TypeError: response.map is not a function`. En d'autres termes, l'API n'a pas retourné le tableau requis (puisque `.map()` ne peut être exécuté que sur des [itérables en JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols)) :

Heureusement pour nous (en plus de l'API REST ci-dessus), Github [expose également un point de terminaison GraphQL](https://developer.github.com/v4/) au moyen de ce qui suit : `[https://api.github/graphql](https://api.github/graphql.)`[.](https://api.github/graphql.) Cela signifie que nous pouvons réécrire ce qui précède comme suit dans le DSL GraphQL :

Si vous n'avez jamais rencontré GraphQL auparavant, ce qui précède peut sembler un peu déconcertant. Cependant, nous allons déballer la syntaxe un peu dans la section à venir.

_À titre d'information, nous faisons une implémentation très bas niveau/artisanale de GraphQL à des fins illustratives. Lorsque vous rencontrez GraphQL dans la nature, vous le rencontrerez probablement au moyen de [Apollo](https://www.apollographql.com/) (développé par l'équipe derrière [Meteor](https://www.meteor.com/)) ou [Relay](https://facebook.github.io/relay/) (développé par l'équipe derrière [Facebook](https://www.facebook.com/)). Ces bibliothèques sont essentiellement juste des outils qui facilitent le travail avec GraphQL côté client._

### L'équivalent GraphQL de Hello World !

**Requêtes et Abonnements et Mutations, Oh là là !**

Personnellement, pour moi, lorsque je commence à utiliser un nouveau langage de programmation (même s'il s'agit d'un DSL comme GraphQL), il y a souvent (ce qui semble être) une quantité impossible d'informations à assimiler. Afin de rendre ce processus un peu plus gérable, je commence toujours (sans faute) par la même question : Qu'est-ce que l'équivalent Hello World ! de ce langage (souvent suivi de quelle est l'application To-do équivalente de ce langage).

En bref :

> Un programme Hello, World ! est généralement un programme informatique qui sort ou affiche le message Hello, World !. Parce qu'il est très simple dans la plupart des langages de programmation, il est souvent utilisé pour illustrer la syntaxe de base d'un langage de programmation et est souvent le premier programme que ceux qui apprennent à coder écrivent.

> Un programme Hello, World ! est traditionnellement utilisé pour introduire les programmeurs novices à un langage de programmation.

>  [Wikipedia](https://en.wikipedia) ([Hello, World ! programme](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program))

**Alors, quel est l'équivalent Hello World ! dans GraphQL ?**

Selon Julian Mayorga dans son livre, [Fullstack GraphQL](https://www.graphql.college/fullstack-graphql/), Dans sa forme la plus simple, GraphQL consiste à demander des champs spécifiques d'objets. Quelque chose appelé _requêtes spécifiées par le client_ dans la [spécification originale de GraphQL de 2015](https://facebook.github.io/graphql/July2015/) :

> Ces requêtes sont spécifiées au niveau de granularité des champs. Dans la majorité des applications client-serveur écrites sans GraphQL, le serveur détermine les données retournées dans ses divers points de terminaison scriptés. Une requête GraphQL, en revanche, retourne exactement ce qu'un client demande et rien de plus.

>  [GraphQL Working Draft (Juillet 2015](https://facebook.github.io/graphql/July2015/))

Cependant, ce qui distingue un Hello World ! GraphQL d'un (par exemple) `console.log('Hello World!')` JavaScript, c'est que nous devons connecter notre requête à quelque chose qui est interrogeable.

Heureusement, il existe [plusieurs points de terminaison GraphQL publics](https://github.com/APIs-guru/graphql-apis) disponibles sur Internet. D'un point de terminaison de l'Université de Stanford qui permet [d'interroger les données de résistance aux médicaments contre le VIH](https://hivdb.stanford.edu/page/graphiql/) à un point de terminaison qui abrite une collection de [informations démographiques publiques organisées par pays](https://countries.trevorblades.com/).

Cependant, tournons notre regard vers le pinacle de l'accomplissement technologique humain : une [Pokéapi](https://graphql-pokemon.now.sh) qui fournit _toutes les données Pokémon dont vous aurez jamais besoin._

En guise d'exercice d'échauffement, créons la requête suivante ([vous pouvez suivre si vous voulez](https://graphql-pokemon.now.sh/?query=%7B%0A%20%20pokemons%20(first%3A%2020)%20%7B%0A%20%20%20%20name%0A%20%20%7D%0A%7D)) :

```
{  pokemons (first: 20) {    name  }}
```

**_Bof !_** C'était assez décevant : une liste de 20 Pokémon du [Pokédex](https://pokedex.org/). Cependant, augmentons d'un cran et trouvons quelque chose de plus spécifique (ce qui, si vous vous en souvenez correctement, est là où GraphQL brille vraiment !).

Pour rendre cela intéressant, disons que nous voulons déterminer le poids moyen de [Pikachu](https://pokedex.org/#/pokemon/25)s évolution finale (spoiler : c'est [Raichu](https://pokedex.org/#/pokemon/26)). Nous pouvons utiliser la requête suivante ([lien vers l'exemple en direct](https://graphql-pokemon.now.sh/?query=%7B%0A%20%20pokemon(name%3A%20%22Pikachu%22)%20%7B%0A%20%20%20%20evolutions%20%7B%0A%20%20%20%20%20%20name%0A%20%20%20%20%20%20weight%20%7B%0A%20%20%20%20%20%20%20%20minimum%0A%20%20%20%20%20%20%20%20maximum%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D)) :

Il est important de noter que la requête ci-dessus est essentiellement une abréviation pour ce qui suit :

```
query GetPikachuEvolutionWeight {  pokemon(name: "Pikachu") {    evolutions {      weight {        minimum        maximum      }    }  }}
```

Le fait que GraphQL suppose que vous allez faire une requête même lorsque vous ne spécifiez pas d'action montre à quel point les requêtes sont centrales dans GraphQL.

Quoi qu'il en soit, peu importe laquelle des deux nous utilisons, nous obtiendrons la réponse JSON suivante du point de terminaison :

Cela signifie que nous pouvons simplement exécuter notre fonction `parse()` (à partir de l'exemple ci-dessus) sur cette réponse JSON, et sortir le résultat (29.5) vers le DOM.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ATRODaaXUt35esV1CCFvwg.png)

**En bref, on peut dire que les requêtes sont de petites cartes sous forme de chaînes ([non, pas ce genre](https://www.lovelyetc.com/diy-map-string-art/) !) utilisées par GraphQL pour naviguer dans une structure de données afin de trouver tous les éléments demandés en un seul voyage.**

Cela signifie que nous pouvons (pour le plaisir) écrire un ensemble similaire d'instructions du monde réel dans le DSL GraphQL :

### Dans quel ordre devrais-je apprendre les concepts de GraphQL ?

Jusqu'à présent, nous n'avons abordé que les requêtes. Cependant (et peut-être surprenant), vous pouvez aller assez loin avec GraphQL en comprenant simplement ce qui précède. Cependant, il existe plusieurs concepts supplémentaires que vous pourriez vouloir explorer si vous souhaitez utiliser GraphQL à son plein potentiel :

Outils/concepts supplémentaires utilisés par les requêtes GraphQL :

1. [**Champs**](https://www.apollographql.com/docs/resources/graphql-glossary.html#field) : Ce sont les éléments dans une requête qui, à première vue, ressemblent à des clés dans un objet JavaScript. Par exemple, `paper`, `post_office` et `travel` dans l'exemple ci-dessus.
2. [**Arguments**](https://www.apollographql.com/docs/resources/graphql-glossary.html#argument) : Informations optionnelles que nous pouvons passer aux champs. Par exemple, `type: drive` et `amount: 12` dans notre exemple ci-dessus.
3. [**Aliases**](https://www.apollographql.com/docs/resources/graphql-glossary.html#alias) : Un nom personnalisé qui doit être utilisé pour la clé JavaScript à laquelle un champ se résout. Par défaut, la clé de l'objet est le même nom que le champ. Par exemple, dans ce qui précède, `post_office` se résoudra en `{ post_office: { ... } }`. Cependant, nous pouvons l'aliaser comme suit : `postOffice: post_office`, ce qui retournera `{ postOffice: { ... } }`. Non seulement cela est utile si nous voulons rendre la clé plus sémantique ou changer la casse, mais cela est également utile lorsque nous utilisons le même champ deux fois (pour empêcher la clé par défaut du second `post_office` de remplacer la première valeur `post_office`.
4. [**Variables**](https://www.apollographql.com/docs/resources/graphql-glossary.html#variable) : Lorsque j'ai commencé à utiliser GraphQL, j'ai fait ce que tout développeur raisonnable ferait. J'ai simplement utilisé l'interpolation dynamique dans la requête (exprimée par une [littérale de gabarit](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)). En d'autres termes, je ferais ce qui suit pour notre exemple Pokémon ci-dessus : `pokemon (name: "${dynamicValue)")`. À la grande surprise des autres développeurs GraphQL (puisque j'ai essentiellement créé des effets secondaires partout !). Il s'avère que GraphQL a une fonctionnalité intégrée pour passer des valeurs externes dans une requête. En déclarant la variable à la racine de la requête. Par exemple, avec `query GetPokemonEvolutionWeight($name: string)` et `pokemon (name: $name)`, nous pouvons simplement passer un objet de variables à la requête lorsqu'elle est appelée (c'est-à-dire `{ name: 'Pikachu' }`. Notez que vous devez attribuer l'un des [types scalaires principaux de GraphQL](https://www.apollographql.com/docs/apollo-server/schemas/types.html) à une variable (par exemple, nous avons utilisé `string` ci-dessus). Il est possible de créer vos propres types personnalisés, mais cela dépasse le cadre de cet article.

De plus, vous pourriez également être intéressé à vous aventurer au-delà des requêtes uniquement (couvertes dans cet article) vers des fonctionnalités GraphQL plus avancées :

* [**Mutations**](https://graphql.org/graphql-js/mutations-and-input-types/) : Jusqu'à présent, nous n'avons récupéré des données que via GraphQL. Cependant, il est également possible d'envoyer des données via GraphQL. Cela se fait via des Mutations, qui sont l'équivalent GraphQL de [POST](https://en.wikipedia.org/wiki/POST_(HTTP)) dans les points de terminaison traditionnels de l'API REST.
* [**Abonnements**](https://www.graph.cool/docs/reference/graphql-api/subscription-api-aip7oojeiv/) : Il s'agit essentiellement de requêtes GraphQL traditionnelles à l'envers. Au lieu d'envoyer une requête au serveur pour récupérer des données, nous disons au serveur de nous informer lorsque les données changent et de nous envoyer les données mises à jour comme défini dans l'abonnement.

### Et le back-end ?

En bref, lorsque je me suis posé cette question il y a 3 ans, la réponse était un non catégorique :

**Ne vous en souciez même pas.**

De plus, je ne suis pas sûr que ma réponse ait changé depuis. Je n'ai toujours aucune idée de ce que Gatsby fait en coulisses pour convertir mon markdown (via [gatsby-transformer-remark](https://www.gatsbyjs.org/packages/gatsby-transformer-remark/)) et mon JSON (via [gatsby-transformer-json](https://www.gatsbyjs.org/packages/gatsby-transformer-json/)) en un point de terminaison GraphQL.

Ce n'est pas dû à l'apathie, bien au contraire en fait ! Je suis un grand fan de Gatsby et je travaille sur une [demande de tirage pour déclencher le préchargement des pages de manière programmatique](https://github.com/gatsbyjs/gatsby/issues/8122). Étant donné à quel point GraphQL est auto-documenté, je n'ai pas encore eu besoin de regarder sous le capot en termes de la façon dont Gatsby gère GraphQL  peu importe à quel point ma requête ou mes données deviennent complexes. De plus, il existe plusieurs autres services GraphQL que j'utilise (par exemple, [Hygraph](https://hygraph.com/), anciennement GraphCMS) où je peux dire exactement la même chose.

**Cela signifie-t-il qu'il n'y a aucune valeur à apprendre à configurer un serveur GraphQL ?**

Certes non !

Comme pour tout, comprendre comment quelque chose fonctionne sous la surface (qu'il s'agisse de JavaScript, de CSS ou même du navigateur lui-même) facilite le débogage lorsque les choses tournent mal. Cependant, le fait que je n'ai commencé à creuser le côté back-end de GraphQL que récemment montre à quel point on peut aller loin sans savoir comment le point de terminaison est créé en coulisses.

Cependant, si vous êtes intéressé à apprendre comment configurer un serveur GraphQL personnalisé, vous pouvez consulter [GraphQL pour les développeurs back-end](https://medium.com/@naidooshailen648/graphql-for-back-end-developers-b4f809417a99) par mon bon ami [Shailen Naidoo](https://www.freecodecamp.org/news/graphql-for-front-end-developers-1f59808f4435/undefined). Il est un développeur phénoménal et la raison pour laquelle je regarde même le côté back-end de GraphQL en premier lieu.

### Mot de la fin

Tout d'abord, bien joué si vous avez lu ce mur de texte entier du haut en bas. C'est assez long ! J'ai commencé à l'écrire principalement en réponse au manque d'introductions spécifiques au front-end pour GraphQL. Cela signifiait qu'il y avait beaucoup de terrain à couvrir.

Deuxièmement, je ne suis en aucun cas un expert de GraphQL, donc si j'ai manqué des ressources/références ou si vous pensez qu'elles pourraient aider les développeurs front-end à se lancer sur GraphQL, alors s'il vous plaît faites-le moi savoir dans les commentaires. Je serais plus qu'heureux de les ajouter.

Enfin, s'il y a des inexactitudes, n'hésitez pas à me le faire savoir dans les commentaires !

Si vous êtes intéressé à en apprendre davantage sur GraphQL, consultez les ressources suivantes :

* [Fullstack GraphQL](https://www.graphql.college/fullstack-graphql/) _(livre)_
* [How To GraphQL](https://www.howtographql.com/) (site web)
* [Documentation officielle de GraphQL](https://graphql.org/learn/) _(site web)_

Enfin, merci pour les commentaires et les contributions fournis par [Shailen Naidoo](https://www.freecodecamp.org/news/graphql-for-front-end-developers-1f59808f4435/undefined) et [Zeeshaan Maudarbocus](https://www.freecodecamp.org/news/graphql-for-front-end-developers-1f59808f4435/undefined).

[**Suivez-moi sur Github**](https://github.com/schalkventer), je suis toujours curieux de savoir ce que tout le monde dans le domaine de la technologie fait  donc je vous suivrai probablement en retour ! ?

[**schalkventer - Aperçu**](https://github.com/schalkventer)  
[_? Développement Front-end / ? Design UI / ? Bien Social /  Déstigmatisation de la Maladie Mentale - schalkventergit_hub.com](https://github.com/schalkventer)