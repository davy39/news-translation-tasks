---
title: Choses que j'aurais aimé savoir avant de travailler avec Electron.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-28T19:11:55.000Z'
originalURL: https://freecodecamp.org/news/lessons-learned-from-electronjs
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9abd740569d1a4ca276a.jpg
tags:
- name: Electron
  slug: electron
- name: JavaScript
  slug: javascript
- name: lessons learned
  slug: lessons-learned
- name: projects
  slug: projects
seo_title: Choses que j'aurais aimé savoir avant de travailler avec Electron.js
seo_desc: 'By Alain Perkaz

  In this article, I''ll share how you can avoid some of the mistakes I made when
  learning about Electron.js ?‍♂️. I hope it helps!

  Note: This wont be a coding tutorial, but rather a discussion about my personal
  takeaways.

  A couple of mo...'
---

Par Alain Perkaz

Dans cet article, je vais partager comment vous pouvez éviter certaines des erreurs que j'ai commises en apprenant Electron.js ?\u200d\u2642\ufe0f. J'espère que cela aidera !

**Note** : Ceci ne sera pas un tutoriel de codage, mais plutôt une discussion sur mes enseignements personnels.

Il y a quelques mois, j'ai décidé de me concentrer davantage sur le développement de mon produit secondaire, [_taggr_](https://taggr.ai/). J'ai été inspiré de le construire en raison du nombre de photos que j'ai sur mon ordinateur. 

Pour ceux d'entre nous qui gardent une sauvegarde de leurs photos, ces collections deviennent souvent si grandes et complexes qu'elles deviennent un travail à temps plein pour les gérer. Un mélange de dossiers et sous-dossiers peut contenir des sauvegardes de photos de messagerie instantanée, des photos haute résolution de votre voyage à Bali, du mariage de votre oncle ou de l'enterrement de vie de garçon de l'année dernière.

Garder de telles collections toujours bien organisées est **fastidieux** (croyez-moi, j'ai essayé pendant des années). Il est également difficile de découvrir les photos que vous aimez le plus, cachées au fond des dossiers. 

Ainsi, [_taggr_](https://taggr.ai/) est une application de bureau qui résout ce problème. Elle permet aux utilisateurs de **redécouvrir** leurs souvenirs tout en préservant leur **vie privée**.

Je développe [_taggr_](https://taggr.ai/) en tant qu'application de bureau multiplateforme. Ici, je vais partager certaines des choses que j'ai apprises sur le développement d'applications multiplateformes avec [Electron.js](https://www.electronjs.org/) et que j'aurais aimé savoir dès le début. Commençons !

## Contexte 

Avant de présenter mes enseignements sur ce voyage en cours avec Electron, je voudrais donner un peu plus de contexte sur moi-même et les exigences de [_taggr_](https://taggr.ai/).

Chaque développeur vient d'un milieu différent, et il en va de même pour les exigences des applications qu'ils développent. 

Contextualiser les choix que j'ai faits pour ce projet peut aider les futurs développeurs à sélectionner les bons outils en fonction de leurs besoins et de leur expertise (plutôt que ce qui est à la mode – GitHub ?, je vous regarde).

![Image](https://www.freecodecamp.org/news/content/images/2020/05/train.gif)
_Le développement JavaScript en un mot. Source : [giphy](https://giphy.com/gifs/train-hype-FY2ew2Zii9VOE" rel="noopener)._

Comme mentionné précédemment, dès le début, j'ai imaginé [_taggr_](https://taggr.ai/) comme une application multiplateforme. L'application effectuerait toutes les opérations de prétraitement et de calculs de machine learning nécessaires côté client en raison de l'accent mis sur la vie privée. 

En tant que one-man show, je voulais pouvoir écrire mon application une fois et la déployer sur différents systèmes sans perdre la tête.

De mon côté, je suis un ingénieur front-end amoureux du web et de JavaScript. J'ai précédemment travaillé avec Java et C#, mais j'apprécie la flexibilité que le web offre et son écosystème vibrant. 

Ayant vécu personnellement la douleur d'utiliser des outils comme [Eclipse RCP](https://wiki.eclipse.org/Rich_Client_Platform) pour construire des applications côté client auparavant, je savais que je ne voulais plus travailler avec cette technologie.

En bref, mes exigences de stack pour taggr se résument à quelque chose comme ceci :

* Il devrait fournir un **support multiplateforme**, idéalement au niveau du framework. ?
* Il devrait me permettre d'**écrire le code une fois**, et de l'ajuster pour chaque plateforme si nécessaire. ?\ufe0f
* Il devrait permettre **l'accès aux capacités de machine learning**, indépendamment de l'environnement hôte, sans runtimes spécifiques à installer. Il devrait être facile à configurer. ?
* Si possible, il devrait **utiliser les technologies web**. Ce serait bien de tirer parti de mes connaissances existantes. ?

Comme vous pouvez le voir, les exigences ne se lisent pas comme : **Je devrais utiliser React avec Redux, des observables et WebSockets**. Ce sont des détails d'implémentation de bas niveau, et ils devraient être décidés _quand et si_ le besoin se présente. 

Choisissez le bon outil pour le travail plutôt que de choisir une stack dès le début, en ignorant les problèmes à résoudre.

Ainsi, après des recherches frénétiques sur Google, j'ai décidé d'essayer Electron. Je n'avais pas utilisé ce framework auparavant, mais je savais que de nombreuses entreprises l'utilisaient avec succès dans des produits tels que [Atom](https://atom.io/), [VS Code](https://code.visualstudio.com/), [Discord](https://discord.com/), [Signal](https://signal.org/#signal), [Slack](https://slack.com/) et plus encore.

Open-source et avec une compatibilité prête à l'emploi avec les écosystèmes JS et Node (Electron est construit en utilisant Chromium et Node), Electron.js était un outil attrayant pour le travail à accomplir. 

Je ne vais pas entrer trop dans les détails concernant le reste de la stack, car j'ai répété les changements des parties centrales (persistence et couches de vue) lorsque nécessaire, et cela sort du cadre de cet article. 

Cependant, je voudrais mentionner [Tensorflow.js](https://www.tensorflow.org/js), qui permet d'exécuter l'entraînement et de déployer des modèles ML directement dans le navigateur (avec WebGL) et Node (avec des liaisons C), sans installer de runtimes spécifiques pour le ML sur l'hôte.

Donc, de retour à Electron – pensant que c'était parfait, le plaisir a commencé. ??

Assez parlé du contexte. Plongeons dans les enseignements.

## 1. Commencez petit (et lentement) ?

Ce n'est pas un nouveau concept, mais cela vaut la peine d'être rappelé périodiquement. Juste parce qu'il existe une tonne de projets de démarrage [starter projects](https://github.com/sindresorhus/awesome-electron#boilerplates) avec Electron disponibles, cela ne signifie pas que vous devriez en choisir un tout de suite.

**Attendez. Quoi ?**

> Lent est fluide, et fluide est rapide.\u200a\u2014\u200aProverbe de la Marine

### Avec la commodité vient la complexité

Bien que ces starters incluent de nombreuses intégrations utiles (Webpack, Babel, Vue, React, Angular, Express, Jest, Redux), ils ont aussi leurs problèmes. 

En tant que novice avec Electron, j'ai décidé d'opter pour un modèle léger qui incluait les bases pour 'créer, publier et installer des applications Electron' sans les clochettes et sifflets supplémentaires. Pas même Webpack au début.

Je recommande de commencer avec quelque chose de similaire à [electron-forge](https://www.electronforge.io/) pour démarrer rapidement. Vous pouvez configurer votre graphe de dépendances et votre structure par-dessus pour apprendre les ficelles d'Electron. 

Lorsque les problèmes surviennent (et ils le feront), vous serez mieux loti si vous construisez votre projet de démarrage personnalisé plutôt que d'en choisir [un](https://github.com/electron-react-boilerplate/electron-react-boilerplate/blob/master/package.json) avec +30 scripts npm et +180 dépendances pour commencer.

Cela dit, une fois que vous vous sentez à l'aise avec les bases d'Electron, n'hésitez pas à passer à la vitesse supérieure avec Webpack/React/Redux/LeProchainFrameworkÀLaMode. Je l'ai fait **incrémentalement** et quand c'était nécessaire. N'ajoutez pas une base de données en temps réel à votre application de liste de tâches juste parce que vous avez lu un article cool à ce sujet quelque part.

## 2. Structurez votre application de manière réfléchie ?\u200d\u2642\ufe0f

Celui-ci a pris un peu plus de temps à être correct que je ne suis heureux de l'admettre. ?

Au début, **il peut être tentant de mélanger le code UI et Backend** (accès aux fichiers, opérations CPU étendues), mais les choses deviennent complexes assez rapidement. Alors que mon application grandissait en fonctionnalités, en taille et en complexité, maintenir une base de code UI+Backend enchevêtrée est devenu plus compliqué et sujet aux erreurs. De plus, le couplage rendait difficile le test de chaque partie en isolation.

Lorsque vous construisez une application de bureau qui fait plus qu'une page web intégrée (accès à la base de données, accès aux fichiers, tâches CPU intensives...), je recommande **de découper l'application en modules** et de réduire le couplage. Les tests unitaires deviennent un jeu d'enfant, et il y a un chemin clair vers les tests d'intégration entre les modules. Pour [_taggr_](https://taggr.ai/), j'ai suivi de manière lâche la structure proposée [ici](https://blog.axosoft.com/electron-things-to-know/).

En plus de cela, il y a **la performance**. Les exigences et les attentes des utilisateurs sur ce point peuvent varier considérablement en fonction de l'application que vous construisez. Mais bloquer les threads principaux ou de rendu avec des appels coûteux n'est jamais une bonne idée.

## 3. Concevez en gardant à l'esprit le modèle de threading ?

Je ne vais pas entrer trop dans les détails ici – je me contente principalement de renforcer ce qui est expliqué de manière géniale dans la [documentation officielle](https://www.electronjs.org/docs/tutorial/performance).

Dans le cas spécifique de [_taggr_](https://taggr.ai/), il y a de nombreuses opérations intensives en CPU, GPU et IO de longue durée. Lorsque vous exécutez ces opérations dans le thread principal ou de rendu d'Electron, le compteur FPS chute de 60, rendant l'UI lente.

Electron offre plusieurs alternatives pour **délester ces opérations des threads principaux et de rendu**, telles que [WebWorkers](https://developer.mozilla.org/en-US/docs/Web/API/Worker), [Node Worker Threads](https://nodejs.org/api/worker_threads.html), ou des instances [BrowserWindow](https://www.electronjs.org/docs/api/browser-window). Chacune a ses avantages et ses inconvénients, et le cas d'utilisation auquel vous êtes confronté déterminera celle qui est la mieux adaptée.

Quelle que soit l'alternative que vous choisissez pour délester les opérations des threads principaux et de rendu (quand c'est nécessaire), **considérez comment l'interface de communication sera**. Il m'a fallu un certain temps pour trouver une interface qui me satisfaisait, car elle impacte fortement la structure et le fonctionnement de votre application. J'ai trouvé utile d'expérimenter différentes approches avant d'en choisir une. 

Par exemple, si vous pensez que l'interface de passage de messages de WebWorkers n'est pas la plus facile à déboguer, essayez [comlink](https://github.com/GoogleChromeLabs/comlink).

![Image](https://www.freecodecamp.org/news/content/images/2020/05/sponge.gif)
_Sponge Bob sait mieux. Source : [giphy](https://giphy.com/embed/jV4wbvtJxdjnMriYmY" rel="noopener)_

## 4. Testez ❌, testez ❌, et testez ✅\ufe0f

Ce n'est pas une nouvelle, n'est-ce pas ? J'ai voulu ajouter ce point en dernier, en raison de quelques 'problèmes' anecdotiques que j'ai récemment rencontrés. Étroitement lié aux premier et deuxième points, construire votre projet de démarrage personnalisé et faire des erreurs tôt vous fera gagner un temps précieux de débogage plus tard dans le développement.

Si vous avez suivi mes recommandations pour diviser l'UI et le Backend de l'application en modules avec une interface propre entre les deux, la configuration de tests Unitaires et d'Intégration automatisés devrait être facile. À mesure que l'application mûrit, vous pourriez vouloir ajouter un support pour les [tests e2e](https://www.electronjs.org/spectron) également.

### Extraction de la localisation GPS ?\ufe0f

Il y a deux jours, lors de l'implémentation de la fonctionnalité d'extraction de la localisation GPS pour [_taggr_](https://taggr.ai/), une fois les tests unitaires au vert et la fonctionnalité fonctionnant en développement (avec Webpack), j'ai décidé de l'essayer dans l'environnement de production. 

Bien que la fonctionnalité fonctionnait bien en développement, elle a lamentablement échoué en production. Les informations EXIF des photos étaient lues en binaire et traitées par une bibliothèque tierce. Bien que les informations binaires étaient correctement chargées dans les deux environnements (vérifié avec [diff](https://www.lifewire.com/compare-two-text-files-linux-3861434)), la bibliothèque tierce a échoué lors de l'analyse de ces données dans la build de production. Excusez-moi, ??

**Solution** : J'ai découvert que les paramètres d'encodage dans les environnements de développement et de production définis par Webpack n'étaient pas les mêmes. Cela a provoqué l'analyse des données binaires en UTF-8 en développement mais pas en production. Le problème a été résolu en configurant les en-têtes d'encodage appropriés dans les fichiers HTML chargés par Electron.

### Photos bizarres ?

Lorsque vous manipulez et travaillez avec des images, vous pourriez penser que si un JPEG 'fonctionne simplement' sur votre ordinateur, c'est un JPEG valide. **Faux**.

En travaillant avec la bibliothèque de traitement d'images Node [_sharp_](https://sharp.pixelplumbing.com/), le redimensionnement de certaines images JPEG a fait planter l'application. Après avoir regardé de près, la cause était des images JPEG incorrectes générées par le [firmware Samsung](https://github.com/lovell/sharp/issues/1578). ?\u200d\u2642\ufe0f

**Solution** : configurer des limites d'erreur améliorées dans l'application (ex. blocs try-catch), ajuster le module d'analyse JPEG, et suspecter tout. ?\ufe0f

## Résumé

Les écosystèmes Node et JavaScript sont en plein essor, avec de nombreux outils puissants créés et partagés chaque jour.

Le nombre d'options rend difficile le choix d'un chemin clair pour commencer à construire votre nouvelle application Electron géniale. Quels que soient vos frameworks de choix, je recommanderais de se concentrer sur les points suivants :

1. **Commencez petit** et ajoutez de la complexité de manière incrémentielle.
2. **Structurez votre application de manière réfléchie**, en gardant les préoccupations backend et UI modulaires.
3. **Concevez en gardant à l'esprit le modèle de threading**, même lorsque vous construisez de petites applications.
4. **Testez et testez à nouveau**, pour attraper la plupart des erreurs tôt et éviter les maux de tête.

Merci d'être resté jusqu'à la fin ! ?

[_taggr_](https://taggr.ai/) est une application de bureau multiplateforme qui permet aux utilisateurs de **redécouvrir** leurs **souvenirs** numériques tout en préservant leur **vie privée**. L'open-alpha arrive bientôt sur Linux, Windows et Mac OS. Alors gardez un œil sur [Twitter](https://twitter.com/TaggrOfficial) et [Instagram](https://www.instagram.com/taggrofficial/), où je poste des mises à jour de développement, des fonctionnalités à venir et des nouvelles.