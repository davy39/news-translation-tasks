---
title: Le guide de 10 minutes pour devenir développeur web full stack junior
subtitle: ''
author: Chris Blakely
co_authors: []
series: null
date: '2019-03-15T15:10:24.000Z'
originalURL: https://freecodecamp.org/news/the-10-minute-roadmap-to-becoming-a-junior-full-stack-web-developer-1131d4ffc48
coverImage: https://cdn-media-1.freecodecamp.org/images/1*H5_yjO8LxdW-cwkyLTuRBQ.jpeg
tags:
- name: career advice
  slug: career-advice
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Le guide de 10 minutes pour devenir développeur web full stack junior
seo_desc: 'So you have started your journey into the world of web development. But
  what do you learn first? The Internet is overloaded with a wealth of information
  about the millions of different technologies that a web developer can know.

  It’s not hard to see ...'
---

Vous avez donc commencé votre voyage dans le monde du développement web. Mais que devez-vous apprendre en premier ? Internet est surchargé d'une multitude d'informations sur les millions de technologies différentes qu'un développeur web peut connaître.

Il n'est pas difficile de voir à quel point tout cela peut être confus et décourageant. En tant qu'ancien développeur junior, je connais la lutte.

Ce guide a été assemblé sur la base de mon expérience dans l'industrie en tant que développeur junior. Ce guide est également un résumé des choses que j'attendrais d'un développeur junior en tant que responsable d'équipe.

Il y a beaucoup d'informations ici - alors prenez une boisson, installez-vous confortablement et commençons !

#### Les incontournables

Quelle que soit votre voie et vos objectifs de carrière, il y a certaines choses que tout développeur doit savoir.

* **Git/Contrôle de source** — Tout bon développeur devra savoir utiliser Git, surtout dans un environnement d'équipe. Apprenez donc à cloner des dépôts, à faire des commits, à créer des branches et à fusionner du code
* **Débogage** — Frontend ou backend, il y aura des bugs. Familiarisez-vous avec les outils de débogage de votre IDE. À propos des IDE...
* **IDE** — Il existe de nombreux IDE que vous pouvez utiliser, alors choisissez-en un et apprenez à le connaître. Votre IDE est votre meilleur ami, et connaître les raccourcis et les outils fera de vous un meilleur développeur. Personnellement, je recommande d'utiliser VS Code.
* **Méthodologies (Agile/SCRUM/Kanban)** — Lorsque vous travaillez en équipe, il est probable que vous utilisiez une méthodologie de développement de produit, alors assurez-vous d'être familier avec leur fonctionnement

### Front-end

![Image](https://cdn-media-1.freecodecamp.org/images/a0a2gn4-IbAt9j6FWCR112Vh96LGKoIQu0cN)

Un développeur front-end peut généralement effectuer les tâches suivantes :

* Implémenter un design en utilisant HTML/CSS
* Interagir avec le DOM en utilisant JavaScript
* Interagir avec une API en utilisant FETCH API ou similaire

Plongeons dans cela un peu plus en détail.

#### HTML/CSS

C'est le pain et le beurre du développement front-end. HTML est utilisé pour positionner et placer des éléments sur une page web, tandis que CSS est utilisé pour _styliser_ ces éléments.

Un développeur web front-end junior sera censé bien connaître tout cela. Il est important de savoir :

* Utiliser HTML pour créer une page web
* Styliser des éléments en utilisant CSS
* Différentes façons d'appliquer CSS à HTML — styles en ligne, feuilles de style, etc.

Une fois que vous avez maîtrisé les bases, jetez un coup d'œil aux fonctionnalités plus avancées :

* CSS Grid & Flexbox pour les mises en page et le positionnement plus facile des éléments
* SCSS pour rendre le CSS normal plus gérable grâce à l'utilisation de variables

Consultez [css-tricks.com](https://css-tricks.com/snippets/css/complete-guide-grid/) pour un guide complet sur CSS. C'est l'une des meilleures ressources disponibles.

> CONSEIL BONUS - Créez quelques projets en CSS/HTML pour vous entraîner. Ne vous inquiétez pas d'utiliser JavaScript ou des API pour l'instant, concentrez-vous **uniquement** sur les éléments CSS/HTML.

Nous devenons maintenant des experts en CSS/HTML ! 💡

#### Frameworks

L'étape suivante est de se familiariser avec les frameworks CSS. Ce sont essentiellement des éléments et des styles "prêts à l'emploi" que vous pouvez utiliser dans vos projets. La plupart des entreprises les utilisent car cela fait gagner du temps à leurs développeurs qui n'ont pas à réinventer la roue. Il existe une pléthore de frameworks, mais je vous suggère d'en choisir un et de vous familiariser avec lui. Ils sont généralement tous assez similaires et une fois que vous êtes familier avec un, il est facile de maîtriser les autres.

#### Bootstrap

Ma suggestion personnelle est d'apprendre **Bootstrap** ([getbootstrap.com](https://getbootstrap.com/)). Il est très populaire et utilisé par de nombreuses entreprises.

"Attendez, pourquoi ai-je dû apprendre CSS/HTML à partir de zéro si je peux simplement utiliser un framework ?!"

Bonne question. Oui, il existe des frameworks, et bien que de nombreuses entreprises les utilisent, vous devrez souvent personnaliser les choses de temps en temps en fonction du projet. Pour cela, vous devrez connaître les bases.

#### Designs Réactifs

De nos jours, il est important de prendre en compte les nombreux appareils mobiles lors de la création de designs front-end. Heureusement pour nous, les frameworks CSS dont nous avons parlé jusqu'à présent (Bootstrap, CSS Grid, Flexbox, etc.) rendent la création de designs réactifs vraiment facile.

* **Media Queries.** En plus de savoir comment utiliser CSS pour créer des designs réactifs, vous devrez comprendre comment utiliser les **media queries** pour définir comment les éléments doivent apparaître pour différentes tailles d'écran.
* **Évitez d'utiliser des pixels pour les tailles.** Je vous suggère d'utiliser les unités **rem** plutôt que les pixels. Une image avec une largeur de 100px aura toujours une largeur de 100px quelle que soit la taille de l'écran. Essayez d'utiliser des unités telles que **rem**, **vh** et **vw**, pour obtenir des designs réactifs.

> **CONSEIL BONUS** - Souvent, vous devez développer une application qui utilise à la fois des écrans mobiles et plus grands. Concentrez-vous d'abord sur le mobile lors de la création de designs, et ajoutez les media queries pour les écrans plus grands ensuite.

#### JavaScript

JavaScript est le langage de programmation du web. Si vous voulez être un développeur front-end performant, vous devez connaître JavaScript. Et vraiment bien le connaître. Oui, il existe des frameworks, mais tout comme nous avons appris les bases de HTML et CSS avant de nous lancer dans les frameworks, nous ferons de même ici. Cela fera de vous un meilleur développeur à long terme. Car les frameworks viennent et partent, mais les éléments de base du langage restent les mêmes.

Au minimum, en tant que développeur junior, vous devrez connaître :

* Les objets, fonctions, conditionnelles, boucles et opérateurs
* Les modules
* Les tableaux (y compris comment les manipuler)
* Récupérer des données d'une API en utilisant FETCH API
* Manipuler le DOM et utiliser les événements
* Async/Await (Plus un sujet avancé optionnel, mais vraiment impressionnant si vous le connaissez)
* JSON
* ES6+
* Tests (Jest, Enzyme, Chai, etc.)

Un développeur junior n'est pas censé tout savoir sur ces sujets, mais plus vous en savez, mieux c'est. Une fois que vous pouvez créer une _application web basique sans tutoriels_, vous pouvez être sûr que vous connaissez JavaScript.

Si vous voulez vraiment devenir un expert en JavaScript, comprendre pleinement le langage et vous démarquer de la foule, voici quelques excellentes ressources pour apprendre les sujets JavaScript plus avancés :

* [eloquentjavascript.net](http://eloquentjavascript.net/)
* [freeCodeCamp.org](https://www.chrisblakely.dev/the-10-minute-road-map-to-becoming-a-junior-full-stack-web-developer/freeCodeCamp.org)
* [github.com/getify/You-Dont-Know-JS](https://github.com/getify/You-Dont-Know-JS)

Non seulement ces ressources vous enseignent JavaScript, mais vous apprendrez également beaucoup de concepts de programmation en général. Sérieusement, si vous apprenez les ressources dans les ressources ci-dessus, vous serez un développeur junior vraiment performant - certains seniors que j'ai rencontrés ne connaissent pas ce genre de choses !

Quelques idées de projets :

* Créez un jeu Super Mario (vous apprendrez JavaScript, la manipulation du DOM et l'utilisation des événements)
* Créez un tableau de bord affichant quelques statistiques tirées d'une API. Par exemple, un tableau de bord Twitter, un tableau de bord GitHub ou tout ce que vous aimez (vous apprendrez à travailler avec des API et JSON)
* Ne vous inquiétez pas de l'apparence des choses ici. Concentrez-vous sur l'apprentissage de JavaScript, pas sur le CSS/HTML. Vous pourrez toujours l'embellir plus tard si vous le souhaitez !

#### Frameworks JS

Il existe de nombreux frameworks JS, choisissez-en un et apprenez-le bien. Les plus populaires actuellement sont **Angular.js**, **React.js** et **Vue.js**. Ce sont tous des choix solides et ils ne vont nulle part de sitôt. Personnellement, je recommande React.js, mais vous pouvez essayer d'autres et voir lequel vous préférez.

Note rapide — Si vous avez appris les bases de JavaScript et que vous avez une solide fondation, l'apprentissage des frameworks devrait être un jeu d'enfant ! Quel que soit le framework que vous choisissez, assurez-vous de bien le connaître.

**Vous n'avez pas besoin de tous les connaître**, cela semble plus impressionnant si vous connaissez un framework **REELLEMENT** bien, plutôt que d'avoir des connaissances mineures sur plusieurs frameworks différents.

#### React

Il bénéficie d'un énorme soutien de **Facebook**, d'une grande communauté en ligne et est le plus populaire dans l'industrie en ce moment.

Si vous avez suivi les étapes ci-dessus et appris un peu de JavaScript, alors apprendre React ne devrait pas être trop difficile. En tant que développeur junior, vous voulez vous assurer que vous maîtrisez les concepts de base de React :

* Comprendre que React est basé sur des composants, et comment les composants fonctionnent
* Utiliser State & Props dans vos composants
* JSX et comment l'utiliser pour rendre des éléments HTML sur une page web
* Comment et quand les composants se re-rendent
* Utiliser les hooks React
* NPM, Webpack et Babel

> **CONSEIL BONUS** — Encore une fois, en tant que développeur junior, vous ne serez pas censé connaître React de fond en comble. Donc, pour pratiquer les compétences décrites ci-dessus, essayez de créer quelques projets :

* Reconstruisez certains de vos projets JavaScript précédents pour utiliser React
* Créez une **application calculatrice** (Une bonne façon de pratiquer la gestion d'état, car beaucoup d'actions de l'utilisateur devront mettre à jour l'état. Indice : Essayez d'utiliser les hooks React)
* Créez votre propre **Twitter**, **GitHub**, ou **fil d'actualités**. Utilisez les API publiques pour obtenir les données, et affichez-les dans votre application.
* Encore une fois, ne vous inquiétez pas de rendre votre application parfaite, ou de la faire paraître super sexy. Concentrez-vous sur le fait de la faire fonctionner, et concentrez-vous sur l'apprentissage des concepts React.

#### Gestion d'état (par exemple Redux)

Une fois que vous avez maîtrisé les concepts de base de React, l'étape suivante est de comprendre **Redux**. Redux est essentiellement un framework de gestion d'état, qui complète fortement React. Considérez-le comme une base de données front-end qui contient l'état de votre application web en un seul endroit, facile à gérer.

Il y a beaucoup de pièces mobiles dans Redux, alors ne vous inquiétez pas si vous vous sentez submergé (je suis encore en train d'apprendre les tenants et aboutissants !). Vous n'aurez besoin de connaître Redux que lorsque vous travaillerez avec des applications web à grande échelle. Concentrez-vous sur la compréhension des fondamentaux et de la gestion d'état en utilisant React.

Il existe un certain nombre d'outils disponibles pour vous aider à déboguer React/Redux (ce qui fait partie des raisons pour lesquelles je l'aime)

* [React Dev Tools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en)
* [Redux Dev Tools](https://github.com/zalmoxisus/redux-devtools-extension)

#### Navigateurs Web

En tant que développeur front-end, il est important de connaître les navigateurs web. Chrome, Firefox et Edge sont les principaux. Vous devrez avoir une idée de base sur :

* Les outils de débogage (par exemple, les outils de développement Chrome)
* Travailler avec les méthodes de stockage (stockage local, stockage de session, cookies)
* Les fonctionnalités du navigateur — le plus gros problème du développement web est de développer en gardant à l'esprit la compatibilité avec les navigateurs. Gardez un œil sur [**whatwebcando.today**](https://whatwebcando.today/) pour vous assurer que votre code supporte les navigateurs nécessaires.

#### Déploiement et Hébergement

Un développeur front-end doit savoir comment déployer et héberger une application web. C'est bon pour vos portfolios, vos connaissances et généralement pour obtenir un emploi. Je recommande d'utiliser un service géré (c'est-à-dire, laissez quelqu'un d'autre faire le travail difficile pour vous) tel que

* GitHub Pages
* Heroku
* Netlify
* Digital Ocean
* AWS
* Firebase

Personnellement, je recommande **Netlify** ou **Heroku**. Cela rend le déploiement et l'hébergement d'applications super facile via l'interface utilisateur. Chacun de ces services propose un niveau gratuit, donc cela ne devrait pas vous coûter beaucoup pour les exécuter. L'inconvénient de ces services est qu'ils ne vous donnent pas l'_accès plus fin_ dont certains développeurs pourraient avoir besoin, comme les services de messagerie, SSH ou FTP. Si vous ne savez pas ce que c'est, vous n'en avez probablement pas besoin, donc le service simple fera très bien l'affaire.

Si vous décidez de devenir super chic et d'héberger certains de vos projets sur un domaine personnalisé (comme `<votre-nom>.com`), je recommande **NameCheap** pour les noms de domaine. Encore une fois, vraiment facile à utiliser et les domaines sont, eh bien, bon marché. 💡

### Back-end

![Image](https://cdn-media-1.freecodecamp.org/images/xDVVuZJUUqhk28LTGvkKagi7BKTrMKHR77K1)

En résumé, c'est là que les données du front-end sont sauvegardées. Par exemple, lorsqu'un utilisateur crée un Tweet, cela passe par le serveur et est sauvegardé dans la base de données.

Un développeur back-end peut généralement effectuer les tâches suivantes :

* Créer des API que le front-end utilisera (généralement en retournant du JSON)
* Écrire la logique métier et la logique de validation
* Intégrations avec des API tierces
* Sauvegarder et lire des données depuis une base de données

#### Langages de Programmation

Il existe de nombreux langages de programmation parmi lesquels choisir. Des millions. Mais ne vous inquiétez pas, les principaux sont :

* Java
* C#
* Python
* Node.js (Ce n'est pas techniquement un langage, mais plutôt un environnement d'exécution qui vous permet d'exécuter JavaScript sur le serveur)
* Go
* PHP (uniquement si vous êtes intéressé par le développement WordPress)

Encore une fois, mon conseil est d'en choisir un et de bien l'apprendre. Je suggère d'utiliser **Node.js**, car vous êtes déjà dans l'état d'esprit d'apprendre JavaScript. Node.js rend vraiment facile la création d'API REST, ce qui est l'une des principales tâches qu'un développeur junior sera censé faire.

Quel que soit le langage que vous choisissez, assurez-vous de connaître les éléments suivants ;

* Créer des API
* Les bases du langage (créer des fonctions, utiliser des conditionnelles, des opérateurs, des variables, etc)
* Comment se connecter à une base de données
* Comment interroger une base de données
* Gestion des packages
* Écrire des tests

Si vous avez décidé d'apprendre Node.js, beaucoup de cela vous sera familier. **N'essayez pas de tous les apprendre !** En tant que développeur junior, vous n'en aurez pas besoin. Choisissez le langage qui correspond le mieux à vos objectifs (si c'est le développement web, n'importe lequel d'entre eux fera l'affaire) et concentrez-vous dessus et apprenez-le bien. Bien sûr, si vous êtes curieux à propos d'autres langages (Node.js et Python sont assez différents), alors n'hésitez pas à satisfaire votre curiosité et à jouer avec eux.

#### REST API & JSON

Créer une bonne API REST est l'un des principaux travaux pour un développeur back-end. Vous devrez savoir :

* Les différents verbes et à quoi ils servent
* Comment créer une bonne réponse
* Comment gérer les requêtes
* Authentifier les requêtes
* Comment documenter votre API

Les **API REST** sont le pont entre le développement back-end et front-end, alors assurez-vous de comprendre comment elles fonctionnent.

**JSON** est le principal langage utilisé pour transférer des données via une API REST. Les données sont représentées sous forme d'_objets et de tableaux_. Encore une fois, si vous avez appris JavaScript ou le développement front-end en utilisant les étapes décrites ci-dessus, cela vous sera familier.

#### Bases de données & DevOps

![Image](https://cdn-media-1.freecodecamp.org/images/z1aN6gbVKd8vKlXHCQgvoheoUDH2FJvR3iva)

C'est essentiellement le côté infrastructure du développement web. Je ne dirais pas qu'une connaissance approfondie de tout cela est une exigence pour un développeur junior. Je dirais presque le contraire, et que vous n'avez vraiment besoin de connaître tout cela en profondeur que si vous cherchez à vous lancer dans le domaine du DevOps. Les domaines généraux que vous devez connaître sont :

* Comment gérer une base de données
* Les différentes plateformes d'hébergement (AWS, Azure, Google, etc)
* CICD et outils tels que Jenkins, GitLab, etc
* Journalisation et surveillance

Selon votre équipe ou votre entreprise, il peut y avoir d'autres équipes ou personnes pour gérer cela. C'est toujours un ensemble de compétences intéressant et impressionnant à avoir, alors si vous êtes curieux et que vous avez un peu de temps libre, apprendre quelques compétences en bases de données et DevOps vous mènera loin.

### Sujets Avancés

![Image](https://cdn-media-1.freecodecamp.org/images/gT62Q5jgzsdlcZnzN-QFNO9vT8RBsQndSXt5)

Ci-dessous se trouvent quelques sujets avancés que je recommande une fois que vous avez maîtrisé ce qui précède. Il y a déjà beaucoup à apprendre, donc je ne vais pas entrer dans les détails ici, mais n'hésitez pas à sauter/survoler cette section pour l'instant et à revenir plus tard.

#### Authentification utilisant JWT/OAuth

C'est une approche courante dans l'industrie qui authentifie et autorise les utilisateurs (par exemple, la connexion).

Plus d'informations à : [https://oauth.net/2/](https://oauth.net/2/)

#### Design Patterns

Les design patterns sont des _solutions courantes à des problèmes courants_. Apprendre les design patterns facilitera la résolution de problèmes et fera de vous un meilleur développeur.

* Plus d'informations (exemple Java) : [github.com/iluwatar/java-design-patterns](https://github.com/iluwatar/java-design-patterns)
* Plus d'informations (JavaScript) : [github.com/fbeline/Design-Patterns-JS](https://github.com/fbeline/Design-Patterns-JS)

> **CONSEIL BONUS** — Il existe de nombreux design patterns, alors n'essayez pas de tous les apprendre en même temps. Au lieu de cela, _familiarisez-vous avec eux_, et lorsque vous rencontrez un problème dans le cadre d'un projet, voyez quels design patterns sont disponibles pour vous.

#### Applications Web Progressives et Développement Mobile

Les **applications web progressives** sont essentiellement des applications web qui fonctionnent comme des applications natives sur le téléphone d'un utilisateur. Plutôt cool, non ? Jetez-y un coup d'œil si vous avez le temps.

Plus d'informations à : [developers.google.com/web/progressive-web-apps/](https://developers.google.com/web/progressive-web-apps/)

D'autres options incluent :

**React Native** — vous permet d'écrire du code React qui est compilé pour Android/IOS

**Flutter** — similaire à React Native, mais utilise le langage de programmation Dart

Cela consiste à rendre le code front-end côté serveur, qui est ensuite retourné et affiché dans le navigateur. Un sujet avancé, qui a ses propres mérites tels que les avantages en termes de SEO et de vitesse.

Plus d'informations à : [medium.freecodecamp.org/demystifying-reacts-server-side-render-de335d408fe4](https://medium.freecodecamp.org/demystifying-reacts-server-side-render-de335d408fe4)

#### Utilisation de la ligne de commande (SSH/Bash, etc.)

Parfois, vous devrez utiliser la ligne de commande lorsqu'une interface graphique n'est pas disponible. À un niveau très basique, vous devrez savoir comment :

* Se connecter à un serveur en utilisant SSH
* Naviguer en utilisant des commandes (cd, ls, etc.)
* Éditer des fichiers en utilisant vim (ou similaire. Voici une feuille de triche [vim.rtorr.com](https://vim.rtorr.com/))

Merci d'avoir lu !

Pour recevoir les derniers guides et cours pour développeurs juniors directement dans votre boîte de réception, assurez-vous de rejoindre la liste de diffusion à [www.chrisblakely.dev](https://www.chrisblakely.dev/#signup)

_Publié à l'origine sur [www.chrisblakely.dev](https://www.chrisblakely.dev/the-10-minute-road-map-to-becoming-a-junior-full-stack-web-developer/) le 15 mars 2019._