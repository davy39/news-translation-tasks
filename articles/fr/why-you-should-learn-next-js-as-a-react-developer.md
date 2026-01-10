---
title: Pourquoi vous devriez apprendre Next.js en tant que développeur React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-10T16:42:06.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-learn-next-js-as-a-react-developer
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/fccposter.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Next.js
  slug: nextjs
- name: React
  slug: react
seo_title: Pourquoi vous devriez apprendre Next.js en tant que développeur React
seo_desc: "By Mehul Mohan\nWe can all likely agree on one thing: React is one of the\
  \ most popular solutions out there for building interactive web applications, both\
  \ small and large. \nAnd it is used by so many startups and companies that it is\
  \ a very valuable sk..."
---

Par Mehul Mohan

Nous pouvons tous probablement convenir d'une chose : React est l'une des solutions les plus populaires pour construire des applications web interactives, petites et grandes.

Et il est utilisé par tant de startups et d'entreprises qu'il s'agit d'une compétence très précieuse à avoir de nos jours.

J'ai découvert Next.js il y a quelques années, et j'ai été intrigué par ce qu'il essayait d'accomplir.

Dans cet article, je vais décrire mon parcours personnel avec Next.js. Je vais également discuter de pourquoi je crois que c'est le bon moment pour l'ajouter à votre stack React.

## Le Web des débuts

Au milieu des années 2000, lorsque le web était jeune et en croissance, les développeurs sont passés des pages HTML statiques à des solutions plus robustes et dynamiques.

Cela nous a donné la capacité de créer des pages avec du contenu dynamique en utilisant des technologies comme PHP (à l'époque, JavaScript était très jeune et non performant).

Vous pouviez avoir une seule page **profile.php** et elle pouvait gérer Alice, Bob, John, Mehul, et toutes les 15 000 personnes enregistrées sur votre site web – très pratique.

Puis est venue l'ère de JavaScript. Les gens ont commencé à réaliser qu'il y avait ce langage supporté pour le web qui pouvait être utilisé pour tant de choses.

Vous pouviez configurer la soumission dynamique de formulaires, des requêtes HTTP en arrière-plan, de beaux effets de défilement, et même créer des pages web à la volée.

L'essor de JavaScript et des bibliothèques comme jQuery a permis aux développeurs web de créer de belles interfaces entièrement personnalisables avec JavaScript.

Bientôt, chaque développeur web a commencé à pousser de plus en plus de JavaScript sur le réseau vers le client. Bien sûr, la technologie a évolué, les téléphones mobiles et les PC sont devenus meilleurs avec plus de RAM et de cœurs, mais JavaScript a commencé à évoluer plus rapidement.

Plus de fonctionnalités, plus de caractéristiques, et plus de frameworks signifiaient une meilleure expérience utilisateur et la capacité de créer une sensation d'application sur le web.

Mais cela signifiait aussi pousser de plus en plus de JavaScript sur le réseau vers des appareils qui ne pouvaient pas suivre les limites évolutives de JavaScript.

## Le Web a été conçu pour HTML

![Image](https://www.freecodecamp.org/news/content/images/2020/08/meme.jpg)

Les anciens appareils mobiles lents ont commencé à abandonner - les temps de chargement sont devenus élevés, il y avait plus de lag, les moteurs JS étaient moins puissants, et il y avait tout simplement trop de JavaScript à analyser !

Avec des frameworks comme React et Angular, vous poussez essentiellement d'énormes bundles JavaScript vers les clients qui doivent d'abord télécharger les petites pages HTML.

Les développeurs web qui sont passés de l'ère PHP (HTML rendu côté serveur) à l'ère JavaScript (HTML rendu côté client) ont bientôt commencé à réaliser qu'ils avaient fait une grosse erreur.

React était génial pour l'interactivité et les composants haute performance, mais le fait que les gens aient commencé à utiliser ces outils pour construire **tout** a commencé à poser des problèmes pour les clients.

Une simple page **À propos de nous**, qui pourrait être une page HTML/CSS statique très simple, était maintenant une page avec un bundle JS énorme. Le navigateur devait d'abord télécharger, puis analyser, puis exécuter, et enfin changer le DOM pour afficher le contenu.

C'était mauvais pour tout le monde. Les clients avaient des temps de chargement plus longs. Les navigateurs devaient travailler dur pour exécuter JS (les navigateurs analysent et exécutent HTML/CSS très efficacement). Et les moteurs de recherche comme Google et Bing avaient du mal à comprendre de quoi parlait votre page, car votre code source ne contenait jamais le vrai contenu. Il était toujours intégré quelque part dans votre bundle JS.

Les gens aimaient React et des outils similaires. Mais ils comprenaient aussi les implications de l'exécution de trop de JS côté client.

D'un autre côté, ils aimaient la façon dont PHP fonctionnait, mais ils n'aimaient pas son architecture. Alors, quelle était la solution ?

## Le rendu côté serveur (SSR) – le meilleur des deux mondes

Lorsque les développeurs ont réalisé que pousser trop de code React sur le client était un problème, ils se sont dit : Hé, est-il possible de coder en React, mais d'envoyer des documents HTML aux clients ?

Après tout, une fois que le code React a fini de s'exécuter, tout ce que vous avez vraiment, c'est un document HTML.

Alors ils l'ont fait. Le rendu côté serveur (SSR) pour React est né.

Maintenant, avec SSR, vous pouvez écrire du code React, l'exécuter d'une manière ou d'une autre sur le serveur (qui était plus puissant que votre appareil client typique – comme un téléphone mobile), puis envoyer le document HTML au client.

Gagnant-gagnant pour tout le monde. Vous, en tant que développeur, pouvez coder en React – la technologie que vous aimez. Et le visiteur sur votre site obtient un document HTML simple (avec du contenu visible, et un peu de JS réhydraté), qui obtient un énorme boost de performance. De plus, Google vous aime maintenant.

Qui ne voudrait pas de ça ?

## Mais c'était trop difficile

Le rendu côté serveur semblait définitivement être la solution à ce problème. Mais le problème ? C'était trop difficile à configurer correctement.

Une mise en cache et une invalidation de cache appropriées ? Pouvez-vous éventuellement créer des fichiers HTML statiques pour les pages qui ne changeaient pas ? Comment devriez-vous construire une expérience de navigation transparente sur votre site web même si vous avez du HTML rendu côté serveur ? Comment devriez-vous réduire la charge sur vos serveurs, ou générer du contenu à la demande ?

Et par-dessus tout, comment configurez-vous toute cette architecture ? Bien sûr, React et le web fournissent toutes les API pour cela, mais elles sont assez verbeuses et généralement une configuration ponctuelle.

Si vous êtes quelqu'un qui construit réellement quelque chose de précieux, après un certain temps, vous voudrez que la majorité de votre temps soit consacrée à la **logique métier** de votre application, et non à la logique sous-jacente.

## Présentation de Next.js

Next.js est un framework né dans le ciel. Il est livré avec :

1. Les meilleures pratiques SEO
2. La mise en cache et l'optimisation statique automatique intégrées
3. Des pages entièrement rendues côté serveur
4. Un support React à 100%
5. Un support des fonctions Lambda (routes API)
6. Un réglage fin de votre configuration webpack/babel si nécessaire
7. Et bien plus encore !

Il abstrait toutes ces configurations de performance et de développement dont vous avez besoin avec une application React typique et vous permet de vous concentrer uniquement sur ce qui compte – votre code de logique métier.

J'ai eu ma première expérience avec Next.js il y a 2 ans, lorsqu'il était très jeune.

Mais Next.js 9.5 a été publié cette année avec tant de fonctionnalités. Et je pense qu'il est sûr de dire qu'il s'agit de l'un des outils les plus puissants disponibles dans l'écosystème du développement web, surtout si vous êtes un développeur React.

Je fais tourner codedamn (une plateforme pour les développeurs pour apprendre à coder) moi-même sur Next.js. Il y a un énorme boost de performance sur le site par rapport à votre application React régulière.

Si vous êtes un développeur React en 2020, l'une des meilleures compétences que vous pouvez apprendre est Next.js. Voici quelques avantages qu'il vous offre en tant que développeur :

1. Définitivement une technologie émergente – plus d'opportunités d'emploi et de possibilités
2. Les pages rendues côté serveur signifient de meilleures performances – plus de clients pour vous
3. Le SEO pour vos sites web est intégré – les moteurs de recherche vous adorent
4. Tous les avantages d'avoir un serveur en place – routes API, récupération de contenu dynamique, et fonctionnalité stale-while-revalidate (oh, j'adore celle-ci)
5. Une grande compétence technique sur votre CV

## Quelques fonctionnalités de Next.js qui m'enthousiasment

Next.js évolue vraiment vite. Ils déprécient les anciennes fonctionnalités et introduisent de nouvelles choses brillantes tout le temps.

À ce jour, je suis super intéressé par le framework dans son ensemble, mais voici quelques-unes de mes préférences :

### #1 Régénération statique incrémentielle stable

Simplement parlant, cette fonctionnalité vous permet de générer du contenu statique _dynamiquement_. Attendez, quoi ? Voyons un exemple rapide :

Disons que vous avez un site web de blog (comme celui-ci) avec beaucoup d'articles. Lorsque quelqu'un visite `/news/[link]` (où `[link]` est n'importe quoi), vous voulez lui servir la page statique aussi vite que possible.

Mais il est possible que vous ne vouliez pas créer _toutes_ les pages statiques au moment de la construction car cela vous prendrait beaucoup de temps. Dans quelques cas, ce n'est pas possible du tout au moment de la construction.

De plus, parfois votre contenu _peut_ changer, comme une rapide édition de blog - donc vous ne voulez pas vraiment une page complètement statique pour toujours non plus. Alors, quelle est la solution ?

En utilisant Next.js 9.5+, vous pouvez maintenant générer des pages statiques dynamiquement vers le chemin dynamique et les rafraîchir.

Cela signifie que une fois que Next récupère cette URL particulière, il l'enregistrera comme une page statique et la servira statiquement chaque fois que quelqu'un visite le chemin. En même temps, il sera ouvert à l'acceptation de nouveaux chemins dynamiquement.

Non seulement vous pouvez faire cela, avec un paramètre de révalidation, vous pouvez également spécifier que Next.js doit mettre à jour vos pages statiques une fois toutes les X secondes en arrière-plan s'il y a un changement !

### #2 Support de Webpack 5

Next.js se dirige également vers le support de Webpack 5. C'est excitant car Webpack 5 apporte quelques optimisations de performance et de bundle et abandonne le support des choses dépréciées dans webpack 4, rendant le cœur _plus léger_.

Cela signifie que vos applications Next.js seront plus rapides que jamais et plus robustes.

### #3 Abandon de getInitialProps

Je n'aimais pas personnellement le concept d'avoir une seule fonction s'exécuter dans les deux environnements - getInitialProps.

Heureusement, Next.js a compris qu'il existait une bien meilleure solution et ils ont introduit getServerSideProps et getStaticProps comme deux grandes méthodes avec de bons noms.

`getServerSideProps`, comme son nom l'indique, vous permet d'injecter des props dans votre page Next.js à partir du serveur lui-même. Et `getStaticProps` permet à Next.js de créer des sorties statiques au moment de la construction.

`getStaticProps` combiné avec la régénération statique incrémentielle est une fonctionnalité redoutable à mon avis. Vous obtenez de nombreux avantages d'un backend dynamique sans avoir de backend dynamique.

### #4 Mise en cache persistante pour les bundles de pages

Next.js supporte également maintenant les caches persistants pour les pages qui ne sont pas modifiées. Auparavant, lorsque vous livriez une nouvelle application Next.js, Next.js jetait toute l'application et l'utilisateur devait retélécharger tout le CSS/JS, même si ces bundles étaient inchangés.

Dans la dernière version de Next.js publiée la semaine dernière, nos amis chez Vercel ont introduit la mise en cache persistante, ce qui est à nouveau une chose absolument géniale à avoir en termes de performance.

### #5 Support intégré pour les modules Sass et TypeScript

S'il y a une chose que j'aime plus que JavaScript, c'est TypeScript. Et Sass est également génial. La plupart des gens que je connais utilisent Sass pour alimenter leur CSS, et cela offre une excellente expérience développeur.

Next.js offre depuis longtemps un excellent support pour TypeScript intégré. Mais récemment, ils ont ajouté un **support basé sur les modules** pour Sass également.

Cela signifie que vos styles peuvent maintenant être écrits en Sass, locaux à vos modules, avec mise en cache et révalidation - tout géré en interne par Next.js.

On dirait qu'ils veulent vraiment que vous développiez les meilleurs produits en vous concentrant uniquement sur la logique métier.

## Apprendre Next.js [un cours]

Je crée un cours vidéo exclusif sur Next.js avec les meilleures pratiques, les dernières mises à jour du framework, et des choses super cool que vous pouvez faire avec. J'inclus une série de projets complets avec le framework afin que vous obteniez une compréhension approfondie de la façon de travailler avec cet outil.

Si vous êtes intéressé, inscrivez-vous pour un accès anticipé en utilisant ce [lien vers le formulaire Google](https://forms.gle/5eZAR3rZvexzBcno7) et je m'assurerai de vous contacter lorsque ce sera prêt.

## Conclusion

Je mise tout sur Next.js. La vitesse à laquelle ils itèrent et développent le concept de SSR et le rendent disponible pour tant de monde est tout simplement stupéfiante.

Si vous vous êtes inscrit en utilisant le lien du formulaire ci-dessus, attendez-vous à avoir de mes nouvelles bientôt avec du contenu génial pour vous.

N'hésitez pas à me contacter sur les réseaux sociaux pour partager ce que vous pensez : [Twitter](https://twitter.com/mehulmpt) et [Instagram](https://instagram.com/mehulmpt).