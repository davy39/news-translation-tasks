---
title: Comment j'ai construit l'application météo dans freeCodeCamp en utilisant React
  et Typescript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-29T22:18:19.000Z'
originalURL: https://freecodecamp.org/news/weather-in-react-and-typescript-4f774fc07be7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*c_otGxMhQQYeAODaylsf5A.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment j'ai construit l'application météo dans freeCodeCamp en utilisant
  React et Typescript
seo_desc: 'By Kelvin Mai

  So I finally decided to come back to freeCodeCamp and try to finish out my Front
  End Development Certificate. I had already finished all the algorithms and tutorials
  earlier last year, and the only thing missing was the projects.

  But no...'
---

Par Kelvin Mai

J'ai finalement décidé de revenir sur [freeCodeCamp](https://www.freecodecamp.org) et d'essayer de terminer mon certificat de développement Front End. J'avais déjà terminé tous les algorithmes et les tutoriels l'année dernière, et la seule chose manquante était les projets.

Mais maintenant que j'ai plus d'expérience en tant que développeur Full Stack, la plupart des projets sont un peu trop faciles pour mon niveau actuel. J'avais donc deux choix. Soit je revenais aux bases et les terminais tous en une journée, soit je faisais d'une pierre deux coups : m'amuser et expérimenter avec la technologie tout en travaillant sur ces projets. J'ai opté pour cette dernière option.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BFO5FsRp7JPwc0vc1nJlUA.png)
_Tellement proche…_

Mais faisons-en trois oiseaux d'une pierre — parce que j'avais envie d'écrire un tutoriel/guide depuis un moment. Aujourd'hui, ce que nous allons aborder, c'est le projet [Show The Local Weather](https://www.freecodecamp.org/challenges/show-the-local-weather). Mais cette fois, il combinera React et Typescript ! Vous pouvez consulter le code finalisé dans ce [dépôt GitHub](https://github.com/kelvin-mai/tsx-weather), ainsi qu'une démonstration en direct [ici](https://kelvin-mai.github.io/tsx-weather/).

### **Contexte**

D'abord, pourquoi voudrais-je faire cela ? Eh bien, voici la chose : je suis passé d'Angular 5 à React pendant un certain temps. Et je préfère React en tant que framework. Il est petit et concis, mais possède toutes les fonctionnalités nécessaires pour créer une application monopage entièrement fonctionnelle. Quant à Angular, il est bien trop volumineux pour que je l'apprécie pour une application aussi petite que celle-ci… mais il utilise Typescript !

TypeScript est un sur-ensemble de JavaScript qui ajoute de nombreuses fonctionnalités qui manquent simplement à JavaScript, même avec les améliorations d'ES6/7. Il est surtout connu pour son typage statique. Je me suis donc demandé si je pouvais obtenir le meilleur des deux mondes. La réponse a été un OUI retentissant !… Redux non inclus. (Je veux dire, vous pouvez inclure Redux, mais jusqu'à présent, c'a été un casse-tête à configurer, donc je ne le ferai pas pour ce guide.)

![Image](https://cdn-media-1.freecodecamp.org/images/1*D1a6zvkRnvj7okzDiGMQeA.png)
_Les Histoires Utilisateur_

Pour ce projet, nous allons nous concentrer sur le strict minimum des Histoires Utilisateur, car mon objectif est la technologie plutôt que des fonctionnalités supplémentaires. Ainsi, l'API que nous allons utiliser pour cette application sera [Wunderround](https://www.wunderground.com/weather/api/). Elle est parfaite pour ce que nous construisons, car ils offrent des températures en Fahrenheit et en Celsius et fournissent également des icônes pour les différentes conditions météorologiques. Cela signifie moins de travail programmatique de notre côté.

### Étape 0 : Installation

J'utiliserai `create-react-app` pour ce projet, avec le script React personnalisé pour Typescript, afin que nous puissions conserver la configuration zéro et la facilité d'utilisation. Un bon article sur la configuration d'une application React avec TypeScript a été écrit par [Trey Huffine](https://levelup.gitconnected.com/@treyhuffine) et peut être trouvé [ici](https://levelup.gitconnected.com/typescript-and-react-using-create-react-app-a-step-by-step-guide-to-setting-up-your-first-app-6deda70843a4).

Je vous suggère définitivement de consulter cet article pour une configuration plus approfondie. Mais sans plus attendre, nous allons exécuter la ligne suivante dans le terminal.

```
create-react-app weather --scripts-version=react-scripts-tsnpm install --save core-decorators
```

Je parlerai des décorateurs un peu plus tard. Sachez simplement que c'est une fonctionnalité intéressante que j'avais vraiment hâte d'essayer. Mais pour pouvoir l'utiliser, nous devons modifier notre fichier `tsconfig.json` pour inclure les décorateurs expérimentaux. Pour ce faire, ajoutez simplement la ligne de code en gras.

```
{   "compilerOptions": {// ...code caché...    "noUnusedLocals": true,    "experimentalDecorators": true   } // ...plus de code caché...}
```

Et puisque j'ai [Prettier](https://github.com/prettier/prettier-vscode) installé sur mon environnement de développement, j'ai dû modifier mon fichier `tslint.json` car le lint était en conflit avec le formateur. Si vous avez une configuration de développement similaire, je vous suggère de supprimer toutes les règles tslint afin de ne pas vous encombrer de la configuration. Le fichier devrait ressembler à ceci une fois que vous avez terminé.

La structure de dossiers que je vais utiliser ressemblera à ce qui suit. Vous pouvez créer, supprimer et déplacer des fichiers en conséquence.

```
weather-app/ .gitignore node_modules/ public/ src/    assets/     | - - loader.svg     | - - logo.svg    components/     | - - Weather.tsx     | - - WeatherDisplay.tsx   styles/     | - - App.css     | - - WeatherDisplay.css  |  index.tsx   |  registerServiceWorker.ts  |  App.tsx  |  index.css   | - - config.ts   | - - types.ts package.json tsconfig.json tsconfig.test.json tslint.json
```

D'accord, le pire est passé ! Nous avons enfin configuré notre application. Plongeons dans le code.

### Étape 1 : Styling

Je veux d'abord m'occuper du style. Je ne suis pas un grand designer, donc tout ce que j'ai vraiment fait, c'est relooker les styles par défaut de `create-react-app` pour avoir le thème vert de freeCodeCamp. J'ai également rendu le bouton plus ressemblant à un bouton et, bien sûr, plus vert. Vous êtes libre de vous lâcher si vous êtes un maître en CSS. Vous pouvez également télécharger des fichiers image [ici](https://github.com/kelvin-mai/tsx-weather/tree/master/src/assets) et les placer dans votre dossier `assets/`.

### Étape 2 : D'accord, j'ai menti… Plus de configuration

Mais ne vous inquiétez pas, cette fois c'est du vrai code. Commençons par la partie facile : ajouter votre API et vos clés API. Rien de nouveau ici — cela ressemble exactement à du JavaScript normal pour l'instant.

Maintenant, pour la partie spécifique à TypeScript, nous devons spécifier les types. Eh bien, nous n'avons pas à le faire, mais nous devrions définitivement le faire. La raison derrière le typage statique est qu'il nous offre une sécurité. Contrairement au JavaScript normal, notre code ne s'exécutera pas si les choses sont du mauvais type. Essentiellement, cela signifie que le compilateur ne nous permettra tout simplement pas d'écrire du mauvais code.

Comme vous pouvez le voir, ce n'est pas trop effrayant. Il suffit d'ajouter le type après un deux-points. Les types primitifs (string, number, boolean) sont pris en charge dès le départ. Avec les objets, il est bon de créer un nouveau type spécifique à cet objet particulier comme vu dans `WeatherData` avec `DisplayLocation`.

J'ai été un peu paresseux, car la forme des données provenant de notre API est beaucoup plus grande, et j'aurais pu créer l'objet entier. Mais j'ai opté pour ne prendre que ce dont j'avais besoin et jeter le reste, c'est pourquoi ce fichier `types.ts` est aussi petit.

### Étape 3 : React — La partie amusante

Je vais sauter les fichiers `[index.tsx](https://github.com/kelvin-mai/tsx-weather/blob/master/src/index.tsx)` et `[App.tsx](https://github.com/kelvin-mai/tsx-weather/blob/master/src/components/App.tsx)` car il n'y a vraiment rien de nouveau là-bas. Sachez simplement que les imports sont différents en raison de la stricte politique de TypeScript concernant les modules. Au lieu de cela, nous allons passer en revue le composant de présentation en premier.

Je préfère toujours déstructurer `Component` et `Fragment` de React, au lieu d'appeler `React.Component`, car cela réduit la redondance. Et pour les Fragments, si vous n'avez jamais joué avec eux auparavant, c'est essentiellement une div qui n'apparaît pas dans le balisage HTML.

Vous remarquerez également que j'ai ajouté des interfaces en haut. Une interface spécifie à quoi nos props et notre état doivent ressembler. Et si vous ne l'avez pas remarqué, le truc de TypeScript est d'ajouter des types à tout, c'est donc ce qui se passe ci-dessus dans les chevrons `<Props, State>`. Si vous êtes familier avec les types de props, cela fait la même chose, mais je trouve que c'est beaucoup plus propre.

La chose suivante est le symbole `@` étrange. Eh bien, c'est un décorateur ! Je voulais à l'origine connecter Redux pour montrer une version beaucoup plus compliquée, mais l'`autobind` fera l'affaire pour l'instant.

Un décorateur est essentiellement une fonction qui enveloppe la classe et applique les attributs nécessaires. Il nous permet également d'utiliser `export default` en haut, ce qui est simplement une préférence personnelle.

```
@decorateexport default Class {}
```

```
// est la même chose que
```

```
export default decorate(Class)
```

Dans ce cas, autobind, comme son nom l'indique, liera automatiquement `this` à tout afin que nous n'ayons pas à nous soucier des problèmes de liaison. Et venant d'un langage plus orienté objet, ces méthodes de classe seront beaucoup plus propres que le contournement JavaScript avec les fonctions fléchées.

```
classMethod = () => {   console.log('quand vous utilisez des flèches, vous ne avez pas à vous soucier du mot-clé "this"');}
```

```
classMethod () {   console.log('à cause de javascript, vous devez vous soucier du mot-clé "this" ici');}
```

Et maintenant, enfin, nous passons à la majeure partie de notre logique, qui va résider dans le composant `Weather.tsx`.

La première chose que vous remarquerez est le `?` dans l'interface. J'ai mentionné que nous devrions définitivement définir des types pour nos props, mais que se passe-t-il lorsque vous savez avec certitude qu'il ne sera pas défini avant l'appel API ? Eh bien, nous pouvons définir des types optionnels avec un point d'interrogation.

Ce qui se passe en arrière-plan, c'est que la variable `weatherData` n'est autorisée à être qu'un type `WeatherData` ou indéfini. De plus, rappelez-vous que notre type `WeatherData` n'est qu'une sous-section de ce que wunderground offre. Plus tôt, j'ai mentionné que nous n'allions prendre que les données dont nous avions besoin de l'API — eh bien, c'est ce que fait cette énorme déstructuration à la ligne 55.

Ai-je mentionné que vous pouvez spécifier les types de retour attendus des fonctions ? C'est ce qui se passe ici avec `getCurrentPosition`, car je voulais m'assurer qu'il retourne une promesse.

Le raisonnement ici est que je ne voulais pas appeler `getCurrentWeather` avant d'avoir la géolocalisation correcte, ce qui signifie que nous traitons des événements asynchrones. Async signifie toujours Promesses, donc c'est ce qui va se passer.

Un mot d'avertissement : l'API de géolocalisation native prend beaucoup de temps à obtenir un résultat sans passer d'options. J'ai opté pour ne pas ajouter d'options car cela me donnait des erreurs à l'époque.

Et je crois que ce sont toutes les nouvelles choses qui se passent dans cette application grâce à TypeScript. Tout le reste devrait être familier si vous connaissez React. Mais espérons que vous pouvez voir les avantages de ce sur-ensemble, car il ajoute à la fois de la sécurité à notre code ainsi que quelques super pouvoirs sympas.

### Étape 4 : Terminé !

![Image](https://cdn-media-1.freecodecamp.org/images/1*W_edOJ7mRloyIKi6WBJfBQ.png)
_Le Produit Fini_

Vous l'avez fait ! Vous avez terminé une application qui montre la météo à votre position actuelle. Et en faisant cela, vous avez couvert une bonne partie de TypeScript ainsi que son incorporation dans React.

Bien sûr, il peut définitivement y avoir des améliorations, comme une option pour rechercher et afficher d'autres lieux. Et l'interface utilisateur peut définitivement être retravaillée. Mais si vous n'avez pas déjà terminé l'application météo sur freeCodeCamp, vous avez déjà dépassé les attentes pour cette tâche.