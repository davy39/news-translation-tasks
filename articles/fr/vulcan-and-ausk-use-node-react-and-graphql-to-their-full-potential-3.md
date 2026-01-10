---
title: 'Une comparaison entre Vulcan et AUSK : comment utiliser Node, React et GraphQL
  à leur plein potentiel'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-02T14:58:50.000Z'
originalURL: https://freecodecamp.org/news/vulcan-and-ausk-use-node-react-and-graphql-to-their-full-potential-3
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/sayan_ausk_vulcan_banner_1600.png
tags:
- name: Vulcan.js
  slug: vulcan-js
- name: Apollo GraphQL
  slug: apollo
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: React
  slug: reactjs
seo_title: 'Une comparaison entre Vulcan et AUSK : comment utiliser Node, React et
  GraphQL à leur plein potentiel'
seo_desc: 'By Eric Burel

  The NRG stack for faster development

  You''ve probably never heard of either Vulcan.js or Apollo Universal Starter Kit –
  at least not yet.

  But I am pretty sure you''ve heard about React, Node.js and GraphQL. Okay, that’s
  what we call an un...'
---

Par Eric Burel

## La pile NRG pour un développement plus rapide

Vous n'avez probablement jamais entendu parler de Vulcan.js ou d'Apollo Universal Starter Kit

 au moins pas encore.

Mais je suis sûr que vous avez entendu parler de React, Node.js et GraphQL. D'accord, c'est ce qu'on appelle un euphémisme : vous avez probablement vu des millions de tweets, d'articles de blog, de meetups et de podcasts sur ces trois technologies et leurs pouvoirs magiques.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/tweet.png)
_Résume 2017-2020 en un tweet_

Il y a beaucoup de bonnes raisons pour lesquelles ces technologies sont louées par les développeurs web. Pourtant, si vous avez déjà essayé d'écrire une application JavaScript full-stack moderne à partir de zéro, vous avez peut-être remarqué la quantité de code répétitif qu'elle peut produire.

C'est particulièrement ennuyeux avec les fonctionnalités génériques : configurer l'authentification, configurer la base de données, configurer le composant principal de l'application, configurer les paramètres



Vulcan.js et AUSK visent tous deux à faire de vous un développeur JavaScript full-stack rapide et efficace. Tous deux s'appuient sur une architecture modulaire, avec React pour l'UI, Node pour le backend, et Apollo GraphQL pour la couche de communication client/serveur. Tous deux fournissent des tonnes de modules pré-codés afin que vous puissiez vous concentrer sur des fonctionnalités précieuses.

Cependant, ils adoptent chacun des approches très différentes du problème, alors j'ai pensé que vous pourriez apprécier une comparaison.

Tout d'abord, présentons les concurrents.

_Avertissement : Je suis contributeur de Vulcan.js, mais j'ai utilisé ces deux technologies pour les projets de mes clients, donc je resterai aussi objectif que possible._

## Apollo UNIVERSAL Starter Kit

![Image](https://www.freecodecamp.org/news/content/images/2019/10/ausk_400.png)

D'accord, quand ils disent universel, ils veulent dire UNIVERSEL. Avez-vous déjà vu un boilerplate JavaScript qui inclut un serveur Scala pour les gros travaux ? Et une configuration complète React Native avec Expo ? Ils règlent même le débat éternel (et ennuyeux) Angular versus React en supportant les deux.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/ausk-stack.png)
_Technologies incluses dans AUSK : Node, Scala, React, Angular et React Native, le tout lié par GraphQL. Un peu comme la cérémonie des Oscars du développement web moderne._

Je n'ai pas grand-chose à ajouter. Je veux dire, regardez à nouveau cette pile, c'est le rêve le plus fou d'un développeur web !

J'ai en fait quelque chose à ajouter : il inclut également Bootstrap et Ant Design comme frameworks de style, Knex pour se connecter à une base de données SQL (la connexion MongoDB n'est pas incluse mais facilement réalisable), et il est écrit en TypeScript. Toutes les fonctionnalités principales d'une application JS/GraphQL sont fournies dans le boilerplate (menu, auth, etc.) + quelques modules de niveau supérieur qui servent d'exemples.

Lien : [https://github.com/sysgears/apollo-universal-starter-kit](https://github.com/sysgears/apollo-universal-starter-kit)

## Vulcan : au-delà de l'universel, isomorphe

![Image](https://www.freecodecamp.org/news/content/images/2019/10/vulcan.png)

Vous vous souvenez de Meteor et Telescope ? Je sais que l'écosystème JS évolue rapidement, mais cette ère dorée n'était il y a que 2 ou 3 ans.

Meteor était le premier framework à exploiter pleinement la combinaison de JavaScript côté serveur et côté client, en permettant d'écrire du code isomorphe qui s'exécute dans les deux environnements. Telescope était une application boilerplate Meteor destinée à profiter pleinement de son architecture orientée packages.

Bien qu'il soit encore utilisé dans de nombreuses applications professionnelles et connu par un grand nombre de développeurs, Meteor est limité par certaines limitations techniques qui empêchent une utilisation plus large : son système de build incompatible avec webpack, son gestionnaire de packages qui est maintenant surpassé par NPM, ou son protocole d'échange de données en temps réel consommateur de RAM.

Et je n'ai pas encore découvert de framework qui rende les développeurs aussi productifs que Meteor. Mais ne vous inquiétez pas, il y a maintenant un sérieux concurrent. Vous l'avez deviné : Vulcan !

L'utilisation d'Apollo GraphQL et une architecture modulaire rationnelle permettent à Vulcan de surmonter les limitations de Meteor tout en profitant des mêmes avantages : architecture entièrement modulaire, programmation déclarative, isomorphisme, etc.

Vulcan est destiné à être le Rails de l'écosystème JavaScript. Facile à prendre en main mais suffisamment complet pour écrire n'importe quelle application.

[Consultez mon article précédent pour une description plus complète des modèles Vulcan ciblant la vitesse de développement](http://:%20https://medium.com/dailyjs/write-less-code-ship-more-apps-how-vulcan-js-makes-me-an-efficient-developer-71c829c76417).

Lien : [http://vulcanjs.org/](http://vulcanjs.org/)

## #1 : Framework VS Boilerplate

Première différence majeure entre ces outils : AUSK est un boilerplate, tandis que Vulcan est un framework. Où se situe la distinction, vous pourriez vous demander ?

### Vulcan, un framework

Un framework est destiné à rendre le développeur plus efficace au quotidien en fournissant un ensemble spécifique de fonctions et d'aides. Il est généralement conçu pour rester séparé de votre application. Vous pouvez mettre à jour votre application de temps en temps lorsqu'une nouvelle version du framework est publiée.

Nous distinguons généralement les frameworks et les bibliothèques en fonction du niveau de spécialisation. Un framework permet généralement de fournir des fonctionnalités de niveau métier, tandis qu'une bibliothèque est un outil technique plus spécialisé. Mais les deux fonctionnent principalement de la même manière.

La limitation avec les frameworks ou les bibliothèques est que vous pouvez vous sentir perdu lorsqu'ils vous abandonnent. Que faites-vous lorsque le bug n'est pas dans votre application, mais dans React ou Apollo ?

Ma règle d'or est que lorsque vous utilisez un framework, vous devez être prêt à contribuer à son développement, au moins en ouvrant des issues chaque fois que vous rencontrez un bug.

### AUSK, un boilerplate

Un boilerplate est un morceau de code bien écrit avec un environnement de développement entièrement fonctionnel. C'est tout. Avec un boilerplate, il est plus difficile de suivre les mises à jour car le code du boilerplate n'est pas clairement séparé de votre application. Un peu comme Create React App après avoir éjecté.

Il fournit généralement seulement quelques méthodes personnalisées. Vous vous sentirez plus rapide dans le premier mois et vous bénéficierez d'une architecture testée en conditions réelles, mais votre vitesse de croisière finira par être à peu près la même qu'avec ou sans boilerplate.

Un boilerplate offre beaucoup plus de liberté qu'un framework, mais aussi moins d'impact sur votre efficacité.

## #2 Courbe d'apprentissage

### Vulcan : GraphQL simplifié

Vulcan peut être un bon moyen de comprendre GraphQL car
 vous n'avez pas besoin d'écrire réellement du GraphQL. Le framework génère le schéma GraphQL et les résolveurs pour vous en fonction de votre modèle de données. En utilisant des outils de développement comme GraphiQL ou GraphQL Voyager, vous pouvez visualiser et jouer avec le schéma pour comprendre comment vos fonctionnalités se traduisent en GraphQL.

La deuxième étape consiste à comprendre la logique de Vulcan lui-même. Un tutoriel interactif est inclus dans l'application "Vulcan Starter" pour vous aider dans le processus.

### AUSK : pour les puristes

L'architecture d'AUSK est beaucoup plus proche de ce à quoi les développeurs Express sont habitués. Imaginez votre application Express canonique, mais avec GraphQL installé et une architecture basée sur des packages. Pas de surprises.

Cela signifie également que vous devrez comprendre les bases de GraphQL pour utiliser AUSK, en plus bien sûr de Node, Express et React et de la base de données que vous utilisez (mais c'est la même chose pour Vulcan). Heureusement, il fournit quelques exemples pour vous aider dans le processus, y compris la création et la liste de données et même le téléchargement de fichiers.

### Conclusion : Les développeurs full-stack ont beaucoup à maîtriser

L'écosystème JavaScript est de plus en plus mature, ce qui signifie également qu'il est plus difficile à apprendre et à comprendre pour les débutants.

Pour profiter pleinement de ces technologies, vous aurez besoin d'au moins quelques connaissances en développement JavaScript moderne et React.

Ne vous attendez pas à être pleinement productif dès le premier jour. Cela dit, il existe de nombreux cours, gratuits ou payants, pour apprendre le développement JavaScript full-stack moderne. Étudier AUSK et Vulcan peut être une source d'inspiration incroyable.

## #3 Vitesse de développement

### Vulcan : automatiser toutes les choses

Lorsque bien utilisé, [Vulcan est incroyablement rapide pour livrer des fonctionnalités](https://www.freecodecamp.org/news/how-i-built-an-app-with-vulcan-js-in-four-days-6368814077b1/). Cela est dû au fait qu'il repose beaucoup sur la génération automatisée, donc il peut produire les parties les plus pertinentes d'une application en quelques heures, à condition que votre modèle de données soit correctement défini.

Ce modèle est appelé programmation déclarative : vous "déclarez" comment votre application fonctionne et laissez le framework faire le travail. C'est difficile à implémenter mais peut être extrêmement puissant.

### AUSK : plus de liberté

Puisque AUSK est axé sur le boilerplate, il est un peu plus difficile d'ajouter des fonctionnalités de base car c'est un processus en plusieurs étapes :

* écrire votre schéma GraphQL
* même chose pour les résolveurs, les mutations
* même chose pour votre modèle de base de données (en utilisant Knex ou Mongoose)
* même chose pour vos composants React
* 


Cependant, si vous devez écrire une fonctionnalité personnalisée, ce sera plus facile avec AUSK qu'avec Vulcan. Donc si vous avez très peu de modèles de données mais des fonctionnalités complexes, AUSK sera plus efficace que Vulcan.

Heureusement, il y a des travaux en cours pour rendre AUSK plus déclaratif, grâce à un système de schéma inspiré de la conception pilotée par le domaine, [domain-schema](https://github.com/sysgears/domain-schema).

### Conclusion : sélectionnez le bon outil pour le bon cas d'utilisation

Il n'existe pas de technologie universelle magique pour le développement full-stack JS. La vitesse de développement avec chaque framework dépend beaucoup du cas d'utilisation sous-jacent. Je tends à préférer Vulcan pour les plateformes orientées données et les outils professionnels, et AUSK pour les plateformes SaaS B2C qui nécessitent plus de fonctionnalités personnalisées.

## #4 Communauté, support et maturité

### Vulcan : héritier de Meteor

Vulcan est un framework de Sacha Greif, qui est un développeur Meteor de longue date et très investi dans la communauté JavaScript ([State of JS](https://stateofjs.com/) et [State of CSS](https://stateofcss.com/) entre autres).

Il existe un Slack actif où les débutants et autres passionnés peuvent rapidement trouver des réponses à leurs questions.

### AUSK : un projet activement maintenu

AUSK est maintenu par [SysGears](https://sysgears.com/), en particulier par Victor Vlasenko, le fondateur de l'entreprise.

Le projet est associé à Gitter. Lors de ma dernière mission freelance avec AUSK, Victor a répondu très rapidement à mes problèmes et questions. Il a même fusionné le support Storybook après que je l'ai essayé.

### Conclusion : petites mais riches communautés

Les deux technologies sont utilisées en production dans de multiples projets, donc elles sont déjà sûres à utiliser. Les communautés grandissent activement et sont accueillantes pour les débutants.

Si vous devez construire une équipe, ne vous attendez pas à trouver des freelances qui connaissent précisément ces technologies, elles sont trop spécifiques. Concentrez-vous plutôt sur la recherche de développeurs JavaScript full-stack qui pourront les apprendre rapidement. Alternativement, vous pouvez aller à la source et trouver de vrais spécialistes parmi les communautés [Vulcan](http://slack.vulcanjs.org/) ou [AUSK](https://gitter.im/sysgears/apollo-fullstack-starter-kit).

## #5 Déploiement

Pas grand-chose à comparer, les deux frameworks permettent le déploiement sur des plateformes offrant des services gratuits comme Zeit Now et Heroku ainsi que le déploiement sur votre propre serveur personnalisé.

## #6 Évolutivité du code et modèles modulaires

### Vulcan : partager les efforts

Un avantage d'un framework est le partage des efforts. L'utilisation finale est plus claire, et permet ainsi d'intégrer diverses optimisations au sein du framework lui-même.

Vulcan fournit des modèles comme les callbacks/hooks, l'amélioration et l'enregistrement central pour profiter pleinement de son architecture orientée packages. Par exemple, nous sommes capables d'ajouter Material UI à une application, y compris le SSR, sans changer une seule ligne de code dans le module Vulcan Core.

Plus précisément, Vulcan fournit différentes méthodes `register` pour chaque structure de données, comme `registerComponent`, et aussi des callbacks, comme `router.wrapper` qui permettent d'envelopper le composant racine `App` React. Vous n'avez besoin d'importer votre fichier qu'une seule fois au niveau d'entrée du package (fichiers `main`).

### AUSK : commencer sur la bonne voie, finir par vous-même

L'architecture modulaire limite la tentation d'écrire du code spaghetti. Elle favorise la réutilisation du code à travers les applications. Chaque package possède un fichier `index.ts` qui déclare les middlewares pertinents, les fonctions de démarrage, les fonctions graphQL partagées avec d'autres modules.

Le module bien nommé `module` fournit des classes pour chaque environnement pour enregistrer un nouveau module, comme `ServerModule` et `ClientModule`. C'est le seul module qui est réellement utilisé directement au niveau de l'application.

```
export default new ServerModule({
    onAppCreate: [ callback1, callback2]
})
```

En interne, tous les modules seront fusionnés en un seul grand module, qui sera finalement utilisé pour créer l'application. Par exemple, tous les callbacks `onAppCreate` seront exécutés les uns après les autres.

C'est un modèle relativement propre et une architecture très intelligente. Je veux dire, même le gestionnaire de modules est un module, n'est-ce pas magnifique ?

Mais le reste dépend de vous. Bien, vous pourrez optimiser tout ! Alors, allez-vous découpler vos résolveurs GraphQL et votre base de données Mongo ? En utilisant quels outils ? Comment allez-vous convertir votre schéma GraphQL en projections Mongo ? Allez-vous écrire des connecteurs, utiliser DataLoader ?

Voici le point : écrire une application évolutive est difficile. Très difficile. Si vous voulez apprendre, alors c'est bien pour vous. Je suis très heureux d'utiliser AUSK pour cette raison, faire les choses par vous-même est le meilleur moyen d'apprendre.

### Conclusion : êtes-vous averse au risque ?

Pour AUSK et Vulcan, l'évolutivité du code signifie une architecture modulaire. Chaque fois que le code devient trop complexe ou illisible, la solution est simple : le découper en morceaux plus petits et plus simples.

L'architecture de Vulcan est plus audacieuse, tout peut être modulaire. Cette ambition comporte un risque, il peut parfois être difficile de savoir qui a enregistré quoi et quand.

Les modèles modulaires d'AUSK sont plus faciles à lire, mais aussi un peu moins puissants. Il peut par exemple être difficile d'ajouter des fonctionnalités globales complexes sans toucher au code du package principal. Pourtant, ils sont définitivement suffisants pour la plupart des cas d'utilisation, vous n'avez pas besoin d'être un puriste de la modularité pour écrire de bonnes applications.

## #6 Mobile

### Vulcan : avec Cordova

Meteor, sur lequel Vulcan est basé, intègre Cordova. Ainsi, votre application web peut être bundlée en tant qu'application mobile avec une seule ligne de commande.

Cependant, Vulcan ne fournit pas d'outils pour les applications natives. Bien sûr, vous pouvez toujours créer une application React Native indépendante et la connecter à Vulcan. Des améliorations sur le système d'authentification (actuellement la dernière partie de Vulcan vraiment dépendante de Meteor) sont prévues dans les mois à venir pour faciliter de telles connexions.

### AUSK : avec React Native

Combiner à la fois une configuration pour React "vanilla" et React Native est l'une des meilleures fonctionnalités d'AUSK. Après tout, c'est un kit de démarrage universel ! Je ne fais pas beaucoup de mobile moi-même, mais c'est rassurant de pouvoir créer rapidement une application mobile native partageant le même serveur que mon interface web.

### Conclusion : AUSK est meilleur pour le mobile-first

AUSK sera plus adapté si vous avez spécifiquement besoin d'écrire une application mobile. Néanmoins, Vulcan permet de construire une application mobile à partir de votre code en une seule ligne de commande, ce qui est acceptable si la version mobile est plus secondaire pour vous.

## #7 Changer l'UI : un problème difficile

Créer un framework full-stack qui permet de changer instantanément de bibliothèque UI est un rêve seulement réalisé à l'ère du CSS. Vous vous souvenez de ces sites web qui permettaient de changer de thème en cliquant sur un seul bouton ?

![Image](https://www.freecodecamp.org/news/content/images/2019/10/fire.png)
_Quel logo pouvons-nous choisir pour notre belle lib CSS-in-JS ? Je ne sais pas, une sorte de femme guerrière badass ? Oui, ça a tout son sens

 créateurs de [Emotion](https://github.com/emotion-js/emotion), probablement_

Ensuite, les nations JS ont attaqué. En utilisant des composants React, il est très difficile de fournir une telle fonctionnalité (sauf pour les changements de couleur triviaux), car le style et le design sont maintenant très liés aux composants React/Angular/Vue sous-jacents.

Chaque bibliothèque UI React a sa propre façon de définir un bouton, sans même parler du thème. C'est un problème pour les technologies full-stack comme AUSK et Vulcan, car le choix d'un framework de style est une question de goût. Ils ne peuvent pas simplement proposer un choix définitif et vous forcer à vous y tenir. Bootstrap n'est plus en monopole et chaque développeur a sa bibliothèque préférée.

Pour aborder ce problème, les deux ont une approche similaire. Ils ont écrit un ensemble canonique de composants avec Bootstrap, puis ont essayé de permettre le remplacement de ces composants par une autre bibliothèque comme Ant Design ou Material UI.

Cela rend le code étrange. Par exemple, le bouton AUSK prendra une prop `color`, car c'est ainsi que fonctionne Bootstrap. Si vous passez à Ant Design, vous devrez également utiliser la prop color, même si Ant Design utilise une prop `type` à la place.

Puisque la sélection du framework UI se fait généralement une seule fois, être obligé d'utiliser un ensemble non canonique de props pendant tout le développement semble un prix très élevé pour le support de plusieurs frameworks UI.

Pendant le développement, je suggérerais d'éviter d'utiliser ces composants pré-codés pour une UI personnalisée autant que possible. Ils sont cool pour construire l'exemple et les fonctionnalités génériques fournies par le boilerplate/framework, mais pas tellement lorsqu'il s'agit d'écrire les parties personnalisées de votre application.

Utilisez plutôt les composants sous-jacents fournis par Ant Design ou Bootstrap ou Material UI en fonction de votre choix, et essayez d'écrire votre propre bibliothèque UI. Vous pourriez consulter Storybook pour vous aider dans le processus, car il est inclus dans AUSK et Vulcan.

## #8 COMBAT LIBRE

Si je devais retenir des fonctionnalités différenciantes spécifiques à chacune de ces technologies, ce seraient celles-ci.

### Vulcan

Le système de schéma. À ma connaissance, aucun framework n'est capable de générer la structure de la base de données, les points d'entrée du serveur, la couche de communication client/serveur, et un frontend prêt pour la production (formulaires, listes, etc.) à partir d'un seul schéma JSON.

Vulcan.js peut le faire tout en utilisant les dernières technologies JS.

### AUSK

Je n'ai pas réussi à n'en choisir qu'une seule, donc mes fonctionnalités préférées d'AUSK seraient TypeScript et React Native.

Il y a eu des débats pendant quelques années autour des avantages de JavaScript typé statiquement, que ce soit pour préférer Flow ou TypeScript
 Et TypeScript a définitivement gagné le combat. Travailler avec TypeScript est possible dans Vulcan mais, en raison de l'utilisation de Meteor, cela semble actuellement peu naturel et la compilation est lente. AUSK utilise TypeScript par défaut et c'est génial.

Et React Native
 eh bien, il y a aussi des débats sur la pertinence de l'utilisation de React pour écrire des applications mobiles. Vous pouvez choisir de vous en tenir à une application web responsive, mais au moins vous savez que tout est configuré pour vous, étant donné que la configuration d'un environnement de développement pour React Native n'est pas toujours une tâche facile.

---

## Alors, avez-vous fait votre choix ?

Il y a tant de points à prendre en considération comme la performance, la sécurité, le DevOps, la gestion de l'authentification
 Choisir le bon outil pour construire votre application JavaScript n'est certainement pas un choix facile. J'espère que cet article vous a donné des informations précieuses pour vous aider dans cette décision.

Si vous vous sentez encore hésitant, contactez-moi sur le Slack de Vulcan, je serais ravi d'y répondre :)

Vous pouvez également diriger toute question sur AUSK à Victor Vlasenko et son équipe chez [SysGears](https://sysgears.com/), et rejoindre le [Slack dédié de Vulcan](http://slack.telescopeapp.org/) pour accéder à la communauté Vulcan.

Mon dernier conseil sera aussi simple : donnez une chance à Vulcan et AUSK, ils valent votre temps !

_Merci à Sacha Greif et Victor Vlasenko pour avoir révisé cet article._

<a href="https://twitter.com/lbke_fr">
<img src="https://www.freecodecamp.org/news/content/images/2019/10/Medium-follow-2019.png" alt="Bannière Twitter LBKE" />
</a>

---

Je suis le co-fondateur de l'entreprise française Lebrun Burel Knowledge Engineering (LBKE)

 [https://www.lbke.fr](https://www.lbke.fr)

_Toujours heureux de parler de code, de machine learning, d'innovation et d'entrepreneuriat !_