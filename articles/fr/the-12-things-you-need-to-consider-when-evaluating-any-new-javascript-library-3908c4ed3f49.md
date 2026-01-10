---
title: Les 12 éléments à considérer lors de l'évaluation d'une nouvelle bibliothèque
  JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-12T20:51:41.000Z'
originalURL: https://freecodecamp.org/news/the-12-things-you-need-to-consider-when-evaluating-any-new-javascript-library-3908c4ed3f49
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PSo6PqzblBfox7FHlG_ITA.png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Les 12 éléments à considérer lors de l'évaluation d'une nouvelle bibliothèque
  JavaScript
seo_desc: 'By Sacha Greif

  How do you know if a new technology is worth investing time into?

  For this year’s State of JavaScript survey I wanted to dig a little bit deeper,
  and not only know which tools and libraries people were using, but also why they
  were usi...'
---

Par Sacha Greif

#### Comment savoir si une nouvelle technologie vaut la peine d'investir du temps ?

Pour l'enquête [State of JavaScript](http://stateofjs.com/) de cette année, je voulais creuser un peu plus profondément et non seulement savoir quels outils et bibliothèques les gens utilisaient, mais aussi _pourquoi_ ils les utilisaient.

Ce qui signifie que je devais trouver un moyen de traduire les préférences personnelles en données concrètes. Après quelques recherches, j'ai élaboré une échelle en 12 points qui couvre les principaux aspects du choix et du travail avec toute technologie.

### Passez le Quiz !

Pour vous faciliter l'application de cette échelle à n'importe quelle bibliothèque, j'ai préparé un quiz rapide qui vous guidera à travers les 12 facteurs et vous donnera une recommandation finale :

#### ➡️ [Passez le Quiz des 12 Facteurs](https://stateofjs.typeform.com/to/hTRAcc)

Si vous n'êtes pas sûr de ce qu'il faut évaluer, faites-le simplement sur une bibliothèque que vous connaissez (React, Vue, jQuery…) et voyez comment elle est notée !

![Image](https://cdn-media-1.freecodecamp.org/images/BPHlsWqIAroX3tV0uIHmC0LZaMotfWjJsejy)

Ou bien, vous pouvez continuer à lire pour en savoir plus sur chaque facteur et voir comment ils peuvent être appliqués.

### Note : À propos de l'enquête State of JavaScript

Comme je l'ai mentionné, j'ai initialement développé cette échelle comme moyen d'obtenir des données plus granulaires pour l'enquête annuelle [State of JavaScript](http://stateofjs.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/vidyXkeKU1T83ZLUYmmnMZbCzpp8mU2T813d)

Si vous souhaitez contribuer et aider à identifier les dernières tendances dans l'écosystème JavaScript, [allez répondre à l'enquête](http://stateofjs.com) !

Revenons maintenant à l'échelle en 12 points.

### Les Facteurs

Voici la liste complète :

1. **✨ Fonctionnalités**
2. **? Stabilité**
3. **⚡ Performance**
4. **? Écosystème de paquets**
5. **? Communauté**
6. **? Courbe d'apprentissage**
7. **? Documentation**
8. **? Outillage**
9. **?✨ Historique**
10. **? Équipe**
11. **⚙️ Compatibilité**
12. **? Dynamisme**

Je vais expliquer l'importance de chaque facteur et vous donner une grille de notation pour vous montrer comment l'évaluer. Passons en revue la liste !

### ✨ Fonctionnalités

La première raison pour laquelle vous choisirez une technologie est probablement ce qu'elle fait.

Mais la question clé ici est de savoir jusqu'où aller. React est probablement la bibliothèque front-end la plus populaire actuellement, mais une plainte courante est qu'elle ne fait pas assez, laissant des choses comme le routage et la gestion d'état à des bibliothèques tierces comme React-Router et Redux.

En fait, c'est une grande partie de l'attrait de Vue, le principal concurrent de React. En fournissant des paquets officiels pour ces cas d'usage courants, il a réussi à offrir une solution plus complète et à gagner beaucoup de terrain.

D'un autre côté, si vous allez trop loin, vous pourriez vous retrouver avec un framework gonflé et complexe qui essaie de tout faire pour tout le monde.

Parfois, une approche minimaliste est ce dont vous avez besoin. Des bibliothèques comme Lodash ou Ramda vous permettent de remplacer vos boucles for imbriquées et désordonnées par des expressions fonctionnelles concises, et cela suffit à en faire des outils inestimables.

Encore une fois, tout est une question de trouver le bon équilibre !

#### Système de notation

* **A** : Déverrouille des choses qui n'étaient tout simplement pas possibles avant.
* **B** : Vous permet de faire les mêmes choses qu'avant, mais de manière meilleure.
* **C** : Fait moins que les solutions actuelles.

### ? Stabilité

Vous pouvez avoir le framework le plus élégant et le plus complet qui soit, mais cela ne servira pas à grand-chose si les développeurs rencontrent des erreurs toutes les deux minutes.

Pour cette raison, de nombreux outils dans l'écosystème JavaScript actuel se concentrent sur l'ajout de stabilité et de sécurité à la pile. Il suffit de regarder les succès de TypeScript et Flow, ou même des langages comme Reason.

Et du côté de la couche de données, le système de types de GraphQL contribue également à garantir que tout fonctionne sans accroc.

#### Système de notation

* **A** : Moins de bugs, et les problèmes deviennent plus faciles à déboguer et à résoudre.
* **B** : L'adoption de la technologie n'a pas d'impact sur la stabilité de votre logiciel.
* **C** : De nouveaux bugs et problèmes apparaissent comme conséquence directe de l'adoption de la technologie.

### ⚡ Performance

Si vous avez déjà pratiqué les arts martiaux, vous savez que l'un des meilleurs atouts que vous pouvez avoir est la _vitesse_, et non la force.

De même, toutes les fonctionnalités du monde ne servent à rien si votre application met 15 secondes à charger. À ce moment-là, l'utilisateur a déjà fermé l'onglet et vous avez perdu le combat avant même qu'il ne commence !

Dans l'écosystème JavaScript, il suffit de regarder [Preact](https://preactjs.com/) pour voir un exemple de mise au point sur la vitesse : son API est identique à celle de React, donc il ne cherche pas à rivaliser sur la force des fonctionnalités. Mais en étant plus léger et plus rapide à charger que React, il vous permet d'économiser des millisecondes précieuses et d'améliorer les performances de votre application web.

#### Système de notation

* **A** : Bundle plus léger, temps de chargement plus rapides, ou autres améliorations de performance.
* **B** : L'adoption de la technologie n'a pas d'impact sur la performance de votre logiciel.
* **C** : L'adoption de la technologie ralentit de manière mesurable votre application.

### ? Écosystème de paquets

Avant d'investir dans une nouvelle technologie, il est important de regarder l'écosystème qui s'est développé autour.

Non seulement un écosystème de paquets dynamique est un énorme gain de temps puisqu'il vous permet de profiter du travail des autres, mais c'est aussi un signe que la technologie a atteint un certain niveau de maturité. Pour cette raison, des paquets tiers bien maintenus sont l'un des meilleurs signes possibles que les développeurs ont adopté une technologie pour le long terme.

#### Système de notation

* **A** : L'écosystème a des solutions sans ambiguïté pour les préoccupations courantes ; les paquets tiers sont bien maintenus et bien documentés.
* **B** : Écosystème de paquets en développement avec de nombreuses nouvelles options concurrentes.
* **C** : Aucun écosystème de paquets à proprement parler, beaucoup de travail manuel requis.

### ? Communauté

Un autre facteur à considérer est la communauté globale. Un forum dédié ou un canal Slack peut être d'une grande aide lorsque vous rencontrez des problèmes.

![Image](https://cdn-media-1.freecodecamp.org/images/PPAbpAV8OeyXs7HpsONNyQJOFjAbnJFB4CLu)
_[Spectrum](https://spectrum.chat/" rel="noopener" target="_blank" title=") est un terrain d'entente de plus en plus populaire entre les salons de discussion et les forums traditionnels._

Il est également utile d'avoir un dépôt existant de réponses Stack Overflow à consulter. Et bien sûr, une page d'issues GitHub bien maintenue est un must !

#### Système de notation

* **A** : Forum et/ou salon de discussion (Slack/Discord/etc.) avec une activité quotidienne, les issues GitHub sont traitées dans la journée. De nombreuses questions Stack Overflow ont des réponses.
* **B** : Forum et/ou salon de discussion avec une activité peu fréquente.
* **C** : Aucune communauté au-delà de GitHub.

### ? Courbe d'apprentissage

Une courbe d'apprentissage facile rend beaucoup plus probable que les développeurs donneront une chance à votre framework ou bibliothèque. Il est tentant de penser que si une technologie est vraiment disruptive, les gens surmonteront tous les obstacles, mais ce n'est souvent tout simplement pas vrai.

Un concept étroitement lié (mais parfois opposé) est la courbe d'adoption. Lorsqu'il a été lancé pour la première fois, [Meteor](http://meteor.com/) était extrêmement facile à utiliser (du moins par rapport aux alternatives existantes), mais il exigeait que vous adoptiez toute sa pile à la fois, ce qui le rendait très difficile à implémenter pour les projets existants.

React est également célèbre pour sa courbe d'apprentissage difficile : pour les développeurs habitués à séparer HTML et JavaScript, l'utilisation de JSX peut être difficile. Vue, en revanche, rend le démarrage beaucoup plus facile sans avoir à repenser la façon dont vous pensez au codage front-end.

#### Système de notation

* **A** : Possible de commencer en une seule journée.
* **B** : Environ une semaine nécessaire avant de devenir productif.
* **C** : Plus d'une semaine nécessaire pour apprendre les bases.

### ? Documentation

Une grande partie d'une courbe d'apprentissage facile est d'avoir une excellente documentation. Cela est plus difficile à réaliser que cela n'y paraît, car les personnes qui écrivent la documentation sont généralement celles qui ont le plus d'expérience ; ce qui signifie qu'elles sont également les plus éloignées de l'expérience du nouveau développeur.

Ainsi, écrire une bonne documentation nécessite d'oublier ce que vous savez pendant un instant et de vous mettre à la place de quelqu'un qui découvre votre technologie.

![Image](https://cdn-media-1.freecodecamp.org/images/gx6MSYtn9YlONOliEwLA07k0hQPzKuv7pldZ)
_La documentation de Vue.js est à la fois bien conçue et bien écrite._

Cela nécessite également d'anticiper les problèmes courants, de comprendre le modèle mental de l'utilisateur, et surtout de tout garder à jour à mesure que votre base de code évolue ! Et tout cela prend un temps précieux loin du codage réel…

Étant donné tous ces facteurs, vous pouvez comprendre pourquoi une bonne documentation est une chose rare et précieuse !

#### Système de notation

* **A** : Site de documentation dédié, screencasts, projets exemples, tutoriels, documentation API, et code bien commenté.
* **B** : Read Me basique et documentation API.
* **C** : Read Me très succinct, la seule façon de savoir comment utiliser la bibliothèque est de regarder son code.

### ? Outillage

Tout comme la documentation, l'outillage est l'une de ces choses qui peuvent sembler une distraction secondaire pour certains mainteneurs, mais qui est en réalité vitale pour la popularité et le succès de toute technologie.

![Image](https://cdn-media-1.freecodecamp.org/images/W5mW8fZMfEEVdmMf5XPdtfSSsNtptGDlOamo)
_Les DevTools de Redux à eux seuls valent la peine d'être considérés._

Je crois qu'une grande raison derrière le succès de Redux est son incroyable extension de navigateur Devtools, qui vous permet de visualiser le store Redux et les actions de manière très conviviale. De même, le excellent support de TypeScript par VS Code a fait des merveilles pour son adoption.

#### Système de notation

* **A** : Deux ou plus parmi : extensions de navigateur, extensions d'éditeur de texte, utilitaire CLI, services SaaS tiers dédiés.
* **B** : Un parmi : extensions de navigateur, extensions d'éditeur de texte, utilitaire CLI, services SaaS tiers dédiés.
* **C** : Aucun outillage externe.

### ?✨ Historique

À la fin de la journée, même la bibliothèque la plus élégante et la mieux documentée sera facilement écartée comme un simple feu de paille si elle n'existe que depuis six mois.

Nous pouvons tous raconter des histoires d'adoption du prochain grand truc, pour revenir en rampant vers le bon vieux Rails/PHP/*insérer ici une technologie éprouvée* lorsque les choses commencent à mal tourner.

![Image](https://cdn-media-1.freecodecamp.org/images/1AaI7f2T0wZ6-AW4G9g1falTwSWg0OEIK48g)
_Express : toujours un concurrent même après toutes ces années_

Pour cette raison, rien ne peut battre un historique solide. Express est l'un des exemples : il a été initialement publié en 2010, mais est toujours considéré comme le framework serveur Node.js par défaut malgré le rythme rapide de l'écosystème JavaScript.

#### Système de notation

* **A** : Existe depuis 4 ans ou plus, adopté par de grandes entreprises et des consultancies technologiques bien connues.
* **B** : Existe depuis 1 à 4 ans, utilisé par des adopteurs précoces et des consultancies à plus petite échelle.
* **C** : Existe depuis moins d'un an, aucune réelle adoption pour l'instant.

### ? Équipe

Tous les projets n'ont pas un historique existant. Lorsqu'une bibliothèque est toute nouvelle, comment jugez-vous son potentiel ? Une méthode fiable est de regarder qui se cache derrière.

Lorsque React est sorti pour la première fois, le fait que ce n'était ni plus ni moins que Facebook qui le soutenait était un grand argument pour au moins l'essayer. Facebook a ensuite sorti Relay et GraphQL, montrant que le succès de React n'était pas un coup de chance !

![Image](https://cdn-media-1.freecodecamp.org/images/cDZb2K2jI518D0NmjO1FX68-LkbJPqHHpe8h)
_Google Open Source : plus de 2000 projets couvrant le bureau, le mobile, et plus._

Et les grandes entreprises ont également plus de ressources à investir : Google a pu continuer à maintenir l'Angular.js original même après avoir sorti des versions plus récentes et incompatibles.

Bien sûr, cela ne signifie pas que les mainteneurs solitaires ne peuvent pas également créer des innovations majeures. C'est ainsi que Vue.js est né après tout, sans parler de 99 % de tous les logiciels open-source.

#### Système de notation

* **A** : Maintenu par une grande entreprise avec une équipe dédiée à l'open-source.
* **B** : Maintenu par une équipe de taille moyenne d'ingénieurs avec des historiques individuels solides.
* **C** : Mainteneur solitaire travaillant indépendamment.

### ⚙️ Compatibilité

Le grand avantage de l'adoption de bibliothèques de pointe est qu'elles évoluent généralement assez rapidement. Malheureusement, cela peut aussi être un inconvénient majeur !

Un rythme d'amélioration rapide peut également signifier des changements fréquents qui cassent la compatibilité lorsque de nouvelles meilleures pratiques remplacent les anciens modèles, laissant les adopteurs précoces payer les coûts de refactoring.

React Router a généré beaucoup de plaintes lorsqu'ils ont décidé de changer complètement leur API entre les versions 3 et 4. Et il en a été de même pour Angular lorsqu'ils sont passés d'Angular.js au nouveau juste Angular.

Les mises à jour fréquentes sont amusantes et excitantes lorsque vous commencez un nouveau projet, mais une fois que votre application est en production, la dernière chose que vous voulez est de devoir passer des semaines de refactoring et de débogage chaque fois qu'une nouvelle version d'une bibliothèque sort.

#### Système de notation

* **A** : Les mises à jour sont principalement rétrocompatibles, les dépréciations sont gérées avec des avertissements, et les versions plus anciennes incompatibles sont maintenues pendant deux ans ou plus.
* **B** : Les changements cassants se produisent mais sont bien documentés et sont déployés progressivement.
* **C** : Mises à jour fréquentes cassantes nécessitant un refactoring majeur sans les conseils appropriés.

### ? Dynamisme

Dernier point, mais non des moindres, le dynamisme. En d'autres termes, le battage médiatique.

Le battage médiatique est souvent perçu comme une mauvaise chose (ne tombez pas victime du battage médiatique), comme un indicateur de style plutôt que de substance. Mais ce n'est pas toujours le cas.

Avec suffisamment de dynamisme, un nouveau projet logiciel peut attirer plus d'utilisateurs et plus de contributeurs, ce qui signifie que les bugs sont trouvés et corrigés plus rapidement, qu'un écosystème de paquets peut se développer, et que tout le monde finit par être mieux loti.

![Image](https://cdn-media-1.freecodecamp.org/images/FEHGvt7qEHqpX68FPpXtVLep1wkX9CcN8RuY)
_JavaScript Rising Stars, notre projet traçant la croissance des bibliothèques JavaScript populaires_

Mais oui, il y a aussi l'autre côté de la médaille : trop de battage médiatique trop tôt peut exposer les utilisateurs potentiels à une version inachevée truffée de problèmes, les décourageant pour de bon. Comme on dit, on n'a qu'une seule chance de faire une première impression.

#### Système de notation

* **A** : Niveau de battage médiatique à plus de 9000 : en tête de Hacker News, des milliers d'étoiles GitHub, des conférences dans les grands événements.
* **B** : Un certain intérêt autour du lancement initial, des centaines d'étoiles GitHub.
* **C** : Développeur solitaire travaillant dans l'obscurité. Un jour, je leur montrerai ! Je leur montrerai à tous !!

### Mise à jour : Quelques facteurs supplémentaires

Certains d'entre vous ont suggéré quelques autres facteurs intéressants à examiner. Quelque chose à considérer pour une potentielle version 2.0 de l'échelle !

* **Évolutivité** : à quel point la technologie fonctionne-t-elle bien pour les grands projets.
* **Adoption** : qui d'autre utilise actuellement la technologie ?
* **Compatibilité** : à quel point la technologie fonctionne-t-elle bien avec les autres technologies existantes ?
* **Découplage** : à quel point il est facile de migrer hors de la technologie si vous souhaitez arrêter de l'utiliser ?

### Étude de cas : Apollo Client

Appliquons notre système de notation à une bibliothèque réelle : [Apollo Client](https://github.com/apollographql/apollo-client).

![Image](https://cdn-media-1.freecodecamp.org/images/XXcqlgMj6hXveo-8JWEyXxCHu09aklqzP6Oi)
_Apollo Client_

Apollo est un client GraphQL, en d'autres termes, c'est une bibliothèque qui interrogera un endpoint GraphQL et chargera ses données sur le client pour vous. Il gère également des choses comme la mise en cache, en s'assurant que les données ne sont pas dupliquées, et envoie lesdites données à votre bibliothèque front-end de choix.

Voyons comment il se comporte avec notre système de notation !

#### ✨ Fonctionnalités : B

Apollo vous donne de meilleures façons d'interroger les données, donc c'est plutôt une amélioration progressive par rapport aux outils existants.

#### ? Stabilité : A

L'adoption d'Apollo et de GraphQL facilite le raisonnement sur vos données et le suivi des problèmes.

#### ⚡ Performance : B

Apollo inclut des outils pour optimiser le chargement de vos données, mais globalement, il ne devrait pas avoir un impact démesuré sur les performances de votre application, dans un sens comme dans l'autre.

#### ? Écosystème de paquets : A

Apollo prend en charge des paquets appelés [links](https://www.apollographql.com/docs/link/#linkslist) afin d'activer des fonctionnalités supplémentaires.

#### ? Communauté : B

Apollo dispose d'un salon de discussion Slack très actif, mais selon mon expérience, les questions peuvent parfois rester sans réponse et il peut être difficile d'obtenir des réponses des membres occupés de l'équipe principale.

#### ? Courbe d'apprentissage : B

Apprendre toutes les nuances d'Apollo peut en fait être un défi, surtout si vous apprenez à utiliser GraphQL en même temps.

#### ? Documentation : A

Bonne documentation bien maintenue fournie pour plusieurs frameworks front-end, ainsi que des bases de code exemples.

#### ? Outillage : A

Extension de navigateur et une plateforme [metrics](https://www.apollographql.com/engine/) dédiée.

#### ?✨ Historique : B

Apollo lui-même est encore relativement nouveau, mais c'est aussi le cas de l'espace GraphQL en général.

#### ? Équipe : A

Équipe hautement compétente et bien financée avec de l'expérience dans le lancement d'autres projets open-source ([Meteor](http://meteor.com/)).

#### ⚙️ Stabilité : B

Mise à jour cassante de la v1 à la v2, mais globalement une bonne stabilité et une rétrocompatibilité depuis.

#### ? Dynamisme : B

Apollo n'est peut-être pas encore un nom connu, mais c'est le principal acteur dans son niche malgré l'avance de Relay.

#### Note globale : A ✨

Avec 29 points sur un maximum de 36, Apollo s'en sort vraiment bien ! Même s'il y aura toujours des domaines à améliorer, il est facile de voir pourquoi il a été adopté en production par de nombreuses équipes qui ont besoin d'une manière fiable de gérer les données GraphQL.

### Autres approches

Les gens de NPMS ont mis en place [un système de notation similaire](https://npms.io/about), automatisé à partir des données GitHub et NPM. Cela rend leur notation moins subjective, mais d'un autre côté, elle ne couvre pas des choses comme la documentation ou la communauté.

Du côté des données brutes, vous pouvez également obtenir quelques statistiques intéressantes avec NPM Trends :

![Image](https://cdn-media-1.freecodecamp.org/images/9kWi9wu6EnMAdvS80GTY8QkczMZFfopW40bv)
_NPM Trends_

Et en savoir plus sur les bibliothèques actuellement populaires sur Best of JS :

![Image](https://cdn-media-1.freecodecamp.org/images/Zmb9zNPTaMXGupSBBzzIo2rroBrMfw2RAMbR)
_Best of JS_

Et bien sûr, il y a toujours [les résultats de l'enquête State of JS de l'année dernière](https://2017.stateofjs.com/) :

![Image](https://cdn-media-1.freecodecamp.org/images/0L1S4aGClqR8O8vKhUFrGICcZ-56yBfZzWuZ)
_Les résultats de l'enquête State of JavaScript 2017_

Et vous, comment évaluez-vous habituellement les bibliothèques ? Laissez un commentaire pour me le faire savoir !

### Conclusion

Cette échelle n'est en aucun cas une mesure absolue de la valeur d'une bibliothèque. Après tout, cela restera toujours en grande partie subjectif et dépendra fortement de votre projet et de vos besoins.

Néanmoins, nous espérons qu'elle pourra servir de point de départ utile. À défaut, elle peut servir de liste de contrôle pour vous assurer de ne rien négliger d'important avant de faire ce grand saut vers l'avenir !