---
title: Qu'est-ce que la programmation réactive ? Guide du débutant pour écrire du
  code réactif
subtitle: ''
author: Pacifique Linjanja
co_authors: []
series: null
date: '2024-03-18T09:02:54.000Z'
originalURL: https://freecodecamp.org/news/reactive-programming-beginner-guide
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-14-at-17.29.29.png
tags:
- name: best practices
  slug: best-practices
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce que la programmation réactive ? Guide du débutant pour écrire
  du code réactif
seo_desc: 'Welcome to your journey through the dynamic world of reactive programming!
  This fascinating paradigm is all about building responsive, resilient, and adaptable
  applications that effortlessly manage vast amounts of data almost instantly.

  Imagine writi...'
---

Bienvenue dans votre voyage à travers le monde dynamique de la programmation réactive ! Ce paradigme fascinant consiste à construire des applications réactives, résilientes et adaptables qui gèrent sans effort de vastes quantités de données presque instantanément.

Imaginez écrire un programme qui doit réagir instantanément aux changements, qu'il s'agisse d'entrées utilisateur, de messages provenant d'autres systèmes ou de flux de données en direct. C'est là que la programmation réactive brille, en faisant un pilier du développement logiciel moderne, en particulier pour les applications web et mobiles.

Dessinons un parallèle simple avec la vie quotidienne pour rapprocher ce concept. Considérez une station de bus, un lieu familier où les gens font la queue, attendant leur bus. Chaque arrivée de bus est un événement, et la réponse des passagers, monter dans le bus, est une action déclenchée par cet événement.

La programmation réactive fonctionne de manière similaire. Elle traite des flux de données (comme l'horaire des bus arrivants) et la propagation des changements (un nouveau bus arrivant), permettant aux applications de répondre en temps réel (tout comme les passagers réagissent en montant dans le bus). Cela vous semble familier ?

Dans cet article, nous plongerons dans l'essence de la programmation réactive, en nous concentrant sur sa mise en œuvre en utilisant JavaScript/TypeScript dans l'environnement Node.js. Nous garderons également un œil sur un contexte global qui s'applique à de nombreux langages de programmation et frameworks.

Nous garderons les choses simples et engageantes, en utilisant un langage simple et des exemples pratiques. À la fin de ce guide, vous aurez une base solide en concepts de programmation réactive et une expérience pratique de la construction d'un système de notification en temps réel.

Que vous soyez nouveau dans le concept ou que vous cherchiez à affiner vos compétences, ce guide est conçu pour démystifier la programmation réactive et vous montrer sa puissance en action. Commençons ce voyage passionnant ensemble !

## **Ce que nous allons couvrir :**

1. [Comprendre les flux et les observables](#heading-comprendre-les-flux-et-les-observables)
2. [La programmation réactive en JavaScript/TypeScript et au-delà](#heading-la-programmation-reactive-en-javascripttypescript-et-au-dela)
3. [Comment construire un système de notification en temps réel avec Node.js](#heading-comment-construire-un-systeme-de-notification-en-temps-reel-avec-nodejs)  
 [Introduction au système de notification](#heading-introduction-au-systeme-de-notification)  
 [Configuration du projet : Commencer avec Node.js et TypeScript](#heading-configuration-du-projet-commencer-avec-nodejs-et-typescript)  
 [Comment implémenter les fonctionnalités principales](#heading-comment-implementer-les-fonctionnalites-principales-construire-un-systeme-de-notification-en-temps-reel)
4. [Meilleures pratiques et pièges courants](#heading-meilleures-pratiques-et-pieges-courants)
5. [Conclusion](#heading-conclusion)
6. [Ressources](#heading-ressources)

## Comprendre les flux et les observables

Plongeons au cœur de la programmation réactive : les flux et les observables. Ces concepts sont les éléments de base des applications réactives, leur permettant de traiter les données de manière dynamique et réactive. Pour comprendre leur importance, revisitons notre analogie de la station de bus.

Imaginez que la station de bus soit équipée d'un écran numérique affichant des mises à jour en temps réel des arrivées, départs et retards de bus. Cet écran reçoit constamment des données sur les bus, ce flux d'informations est ce que nous appelons un "flux". Chaque nouvelle donnée (comme l'arrivée d'un bus) peut être considérée comme un "événement" dans ce flux.

### Flux : Le flux de données

En programmation, un flux est une séquence de données continues mises à disposition au fil du temps. Les flux peuvent être n'importe quoi : mouvements de souris, frappes de touches, tweets, ou même des mises à jour en temps réel du marché boursier. Ils ne sont pas si différents de l'écran numérique de la station de bus, qui reçoit un flux continu d'informations sur les bus.

En bref, un flux est une collection de valeurs poussées au fil du temps, l'intervalle entre deux valeurs différentes peut être contrôlé (flux planifiés) ou aléatoire (on ne sait jamais quand quelqu'un va nous envoyer un message, n'est-ce pas ?).

Les flux peuvent émettre trois choses différentes : une valeur (d'un certain type), une erreur, ou un signal "complété". Prenons l'exemple d'un système de notification. D'un côté, nous avons un client (application mobile, application web, etc.) qui s'est abonné à un groupe WhatsApp. Chaque fois qu'il y a un nouveau message dans ce groupe, l'application réagira en envoyant une notification push à l'utilisateur, mais nous ne savons jamais quand ces messages arriveront.

La figure 1 ci-dessous montre une illustration de ce qui peut être considéré comme un flux. Après un certain temps, la valeur peut changer, notifiant chaque client qui s'est abonné au flux qu'une nouvelle valeur est disponible. Cela donne aux clients la possibilité de se désabonner à tout moment.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Guessing-game-Page-4.drawio--1-.png)
_Figure 1 : Illustration de ce qu'est un flux, un abonnement et un désabonnement_

Comme vous pouvez le voir sur l'image ci-dessus, à partir du moment où un client se désabonne, il cesse de recevoir de nouvelles valeurs du flux.

### Observables : Réagir aux données

Un observable est un type de flux que vous pouvez observer, vous permettant d'écouter et de réagir aux données entrantes.

Pour illustrer, considérons l'écran numérique d'une station de bus comme le flux. Alors que vous attendez et regardez les informations sur l'arrivée de votre bus, vous êtes similaire à un observable. Lorsque l'arrivée de votre bus est affichée (un événement), vous réagissez en vous préparant à monter à bord.

Les observables sont caractérisés par les trois aspects suivants :

1. **Cycle de vie des données :** Un observable est un type primitif qui peut contenir zéro ou plusieurs valeurs. Ces valeurs sont poussées sur n'importe quelle durée, déterminant le cycle de vie du flux.
2. **Annulable :** Les observables peuvent être annulés à tout moment. En informant le producteur que vous n'avez plus besoin de mises à jour, vous pouvez annuler un abonnement à un observable.
3. **Évaluation paresseuse :** Les observables sont paresseux, ce qui signifie qu'ils n'effectuent aucune action tant que vous ne vous y abonnez pas. De même, ils cessent leurs opérations lorsqu'ils sont désabonnés. Cela contraste avec les Promesses, qui sont impatientes et doivent être réglées chaque fois qu'elles sont invoquées avant que le traitement ne se poursuive.

### Pourquoi les flux et les observables sont importants

Les flux et les observables sont cruciaux en programmation réactive car ils permettent aux applications de gérer des données qui changent au fil du temps, tout comme les informations constamment mises à jour sur l'écran de la station de bus.

Ils permettent aux applications de réagir instantanément aux nouvelles données, qu'il s'agisse d'un clic de l'utilisateur ou de la réception de messages d'un service web.

### Opérateurs

Les flux seuls sont utiles, car ils permettent à plusieurs observateurs de s'y abonner pour leurs mises à jour. Les choses deviennent plus intéressantes lorsque vous souhaitez manipuler un flux. Les flux peuvent être transformés et même combinés, en utilisant des opérateurs.

RxJS, par exemple, contient des centaines d'opérateurs inspirés de certaines méthodes bien connues des tableaux JavaScript comme map, filter, reduce, etc.

Les opérateurs sont simplement des fonctions qui prennent un observable et retournent un observable avec une opération appliquée.

Regardons deux opérations essentielles : **mapping et filtering**. Jetez un œil à l'animation suivante :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/map-filter-stream-e0e9503b758fe89104ae60e0ecd48995.gif)
_Figure 2 : opérateurs sur un observable - [source](https://reactive.how/filter)_

Dans la _Figure 2_ ci-dessus, pour l'opérateur `map`, lorsque l'observable d'entrée émet une valeur, elle est traitée par la fonction `isEven` et la valeur résultante est émise comme valeur pour l'observable de sortie.

Pour l'opérateur `filter`, lorsque le flux d'entrée émet une valeur, elle est donnée à la même fonction, qui émet une valeur pour l'observable de sortie lorsqu'elle remplit la condition. Sinon, elle est ignorée. L'entrée est un observable, et l'opérateur retourne un autre observable.

## La programmation réactive en JavaScript/TypeScript et au-delà

Dans le monde de JavaScript et TypeScript, en particulier dans l'environnement Node.js, les flux et les observables sont conçus avec à la fois grâce et efficacité.

Node.js offre un support intégré pour les flux, permettant des capacités puissantes de gestion de données pour les applications côté serveur. De plus, les bibliothèques et frameworks construits sur le paradigme de la programmation réactive, tels que RxJS pour JavaScript/TypeScript, fournissent aux développeurs des outils puissants pour créer des applications réactives.

RxJS, par exemple, est une bibliothèque spécialement conçue pour la programmation réactive en JavaScript/TypeScript. Elle fournit une vaste collection d'opérateurs pour créer, combiner et manipuler des observables. Avec RxJS, les développeurs peuvent gérer des scénarios complexes de flux de données avec facilité, grâce à son API intuitive et son ensemble d'opérateurs étendu.

Mais la programmation réactive ne se limite pas à JavaScript/TypeScript et Node.js. De nombreux autres langages de programmation ont leurs propres implémentations des paradigmes et bibliothèques de programmation réactive.

Par exemple, des langages comme Java ont RxJava, Kotlin a RxKotlin, et Swift a RxSwift. Ces bibliothèques offrent des fonctionnalités similaires à RxJS mais sont adaptées à leurs écosystèmes de langage respectifs.

Quelle que soit le langage de programmation que vous utilisez, les principes de la programmation réactive restent applicables. Que vous travailliez en JavaScript, Java, Kotlin, Swift ou tout autre langage, vous pouvez tirer parti de la programmation réactive pour construire des applications réactives, évolutives et maintenables.

Les concepts de flux, d'observables et d'opérateurs transcendent les barrières linguistiques, fournissant aux développeurs une boîte à outils puissante pour gérer les flux de données asynchrones et créer des expériences utilisateur dynamiques.

## Mettre tout cela ensemble

Imaginez que nous développons une fonctionnalité pour notre application de station de bus qui notifie les utilisateurs lorsque leur bus approche. En utilisant RxJS, nous pouvons créer un observable qui représente le flux de données d'arrivée des bus. Chaque fois que le statut d'un bus est mis à jour, par exemple lorsqu'il est à 10 minutes, l'observable émet un événement. Notre application peut s'abonner à ces événements (les observer) et réagir en envoyant une notification à l'utilisateur : "Votre bus est en route !"

Ce scénario montre la puissance de la programmation réactive avec les flux et les observables. Non seulement elle permet une réactivité en temps réel, mais elle simplifie également la gestion des flux de données asynchrones, rendant notre code plus propre et plus intuitif.

Cette compréhension fondamentale des flux et des observables est votre premier pas dans le monde de la programmation réactive. Alors que nous avançons, rappelez-vous de l'écran numérique de la station de bus et de la manière dont il se met constamment à jour. Nos applications, tout comme un voyageur attentif, doivent être prêtes à répondre à ces mises à jour aussi efficacement que possible.

Avec RxJS et les concepts de flux et d'observables, nous sommes équipés pour relever ces défis de front, créant des applications qui non seulement répondent mais dépassent les attentes des utilisateurs en termes de réactivité et de performance.

S'engager avec ces concepts ne consiste pas seulement à comprendre la théorie, c'est aussi à voir l'immense potentiel qu'ils déverrouillent pour développer des applications dynamiques et centrées sur l'utilisateur. Alors que nous plongeons dans des exemples pratiques, gardez à l'esprit l'analogie de la station de bus, elle vous aidera à saisir les aspects plus complexes de la programmation réactive de manière simple et directe.

## Comment construire un système de notification en temps réel avec Node.js

Dans cette section, nous allons entreprendre un voyage pour créer un système de notification en temps réel en utilisant Node.js. Imaginez un scénario où les utilisateurs d'une application web doivent recevoir des mises à jour instantanées sur divers événements, tels que de nouveaux messages, notifications ou alertes système.

Notre objectif est de construire un système robuste et efficace qui livre ces notifications de manière transparente en temps réel.

### Introduction au système de notification

Avant de plonger dans la mise en œuvre technique, imaginons comment notre système de notification en temps réel fonctionnera. Les utilisateurs interagiront avec le système via une interface web, où ils pourront s'abonner à différents types de notifications en fonction de leurs préférences.

Ces notifications pourraient inclure de nouveaux messages dans une salle de chat, des mises à jour sur des documents partagés, ou des alertes pour des événements système importants. Nous essaierons de garder cela très simple, puisque le but est vraiment de commencer avec le paradigme.

### Interactions clés avec le système

1. **Abonnement de l'utilisateur :** Les utilisateurs auront la possibilité de s'abonner à des types spécifiques de notifications, adaptant leur expérience à leurs préférences et besoins.
2. **Livraison en temps réel :** Une fois abonnés, les utilisateurs recevront des notifications instantanément dès qu'elles se produisent, assurant une communication et une réactivité en temps opportun.
3. **Notifications actionnables :** Les notifications seront actionnables, permettant aux utilisateurs d'interagir avec elles directement depuis l'interface. Par exemple, cliquer sur une notification pourrait ouvrir la salle de chat ou le document correspondant.

Avec cette vision en tête, procédons à la configuration de notre projet Node.js et posons les bases de notre système de notification en temps réel. Nous commencerons par configurer l'environnement du projet et installer les dépendances nécessaires, y compris RxJS, pour alimenter notre implémentation de programmation réactive.

### Configuration du projet : Commencer avec Node.js et TypeScript

Avant de pouvoir plonger dans la mise en œuvre de notre système de notification en temps réel, nous devons configurer notre environnement de projet Node.js. Cela implique de configurer TypeScript pour une vérification de type améliorée et d'activer RxJS pour exploiter la puissance de la programmation réactive.

Parcourons les étapes pour mettre notre projet en route :

#### Étape #1  Initialiser un nouveau projet Node.js

Commencez par créer un nouveau répertoire pour votre projet et naviguez dedans :

```bash
$ mkdir systeme-de-notification-en-temps-reel
$ cd systeme-de-notification-en-temps-reel

```

Ensuite, initialisez un nouveau projet Node.js en utilisant npm ou yarn :

```bash
$ npm init -y

```

ou

```bash
$ yarn init -y
```

#### Étape #2  Installer les dépendances

Maintenant, installons les dépendances nécessaires pour notre projet. Nous aurons besoin de TypeScript pour la vérification de type et la compilation, ainsi que de RxJS pour la programmation réactive :

```bash
$ npm install typescript rxjs

```

ou

```bash
$ yarn add typescript rxjs

```

#### Étape #3  Configurer TypeScript

Créez un fichier **`tsconfig.json`** à la racine de votre projet pour configurer TypeScript :

```json
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "CommonJS",
    "outDir": "./dist",
    "strict": true},
  "include": ["src/**/*"]
}

```

Cette configuration définit la cible de compilation à ESNext, active la vérification de type stricte et spécifie le répertoire de sortie pour les fichiers TypeScript compilés.

#### Étape #4  Configurer la structure du projet

Créez un répertoire **`src`** pour stocker vos fichiers source TypeScript :

```bash
$ mkdir src

```

Votre structure de projet devrait maintenant ressembler à ceci :

```markdown
systeme-de-notification-en-temps-reel/
 src/
 node_modules/
 package.json
 tsconfig.json

```

Maintenant, créez un fichier TypeScript d'exemple dans le répertoire **`src`** pour vérifier que TypeScript fonctionne correctement :

```tsx
// src/index.ts
const message: string = 'Bonjour le monde !';
console.log(message);

```

Pour exécuter le fichier, vous pouvez utiliser Node, ou tout autre runtime JS comme Bun, en utilisant la commande suivante :

```bash
# assurez-vous que bun est installé avec la commande bun -v
# puis exécutez
$ bun run src/index.ts

```

Assurez-vous d'obtenir le "Bonjour le monde" dans la console avant de passer à l'étape suivante

#### Étape #5  Compiler TypeScript

Compilez votre code TypeScript en exécutant :

```bash
# puis compilez le projet
$ npx tsc
```

Cela générera des fichiers JavaScript dans le répertoire **`dist`** selon la configuration spécifiée dans **`tsconfig.json`**.

Avec notre projet configuré et TypeScript configuré, nous sommes prêts à commencer à implémenter les fonctionnalités principales de notre système de notification en temps réel.

Passons à la création d'observables, à l'application d'opérateurs et à la gestion des notifications en temps réel dans notre application.

### Comment implémenter les fonctionnalités principales : Construire un système de notification en temps réel

Maintenant, plongeons dans l'implémentation des fonctionnalités principales de notre système de notification en temps réel. Nous allons créer des observables pour représenter différents types d'événements, appliquer des opérateurs pour filtrer et transformer ces flux d'événements, et enfin nous abonner à ces observables pour gérer efficacement les notifications en temps réel.

#### Comment créer des observables  Modélisation des flux d'événements

Dans notre système de notification, nous aurons divers flux d'événements représentant différents types de notifications. Ceux-ci pourraient inclure de nouveaux messages, des mentions d'utilisateurs, des alertes système, et plus encore.

Rappelez-vous, tout peut être observable, car cela est très important lors de la construction de programmes réactifs. En utilisant RxJS ([https://rxjs.dev/guide/overview](https://rxjs.dev/guide/overview)), vous pouvez manipuler n'importe quel type de flux de manière observable.

Avant de commencer, voyons ce que je veux dire par là.

Étant donné un bouton écoutant un événement de clic, JavaScript peut capturer l'événement comme ceci :

```tsx
<button id='btn'>Cliquez-moi</button>

// dans le fichier js
const btn = document.getElementById("btn");
btn.addEventListener("click", (event) => {
  console.log('Bouton cliqué');
});
```

Bien que cela fonctionne parfaitement, ce n'est pas réactif. Que faire si vous souhaitez combiner l'événement de clic avec un autre événement, tel qu'un minuteur ou une requête HTTP ? C'est là que la programmation réactive intervient.

Avec la programmation réactive, vous pouvez traiter tous ces événements comme des flux de données et les combiner de manière déclarative et composable.

Imaginez un scénario où nous devons imprimer un message lorsque deux événements de clic se produisent dans un intervalle de 5 secondes, ou imprimer un message avec un tableau de positions que la souris a occupées sur le navigateur entre deux événements de clic. Ou imprimer un message lorsque l'utilisateur clique sur le bouton et la touche Entrée dans un intervalle de 2 secondes.

Tous ces scénarios sont possibles avec la programmation impérative habituelle mais peuvent nécessiter un code plus complexe, et penser de manière réactive peut devenir une nécessité.

Essayons de construire le premier scénario de manière habituelle, puis nous verrons comment la programmation réactive peut nous aider à le rendre plus lisible et maintenable.

```tsx
const btn = document.getElementById("btn");

let clickCount = 0;
let lastClickTime = 0;

btn.addEventListener("click", (event) => {
  clickCount++;
  if (clickCount === 1) {
    lastClickTime = new Date().getTime();
  } else if (clickCount === 2) {
    if (new Date().getTime() - lastClickTime < 5000) {
      console.log('Deux clics en moins de 5 secondes');
    }
    clickCount = 0;
  }
});

```

Maintenant, voyons comment nous pouvons obtenir le même résultat en utilisant une approche de programmation réactive avec `rxjs` dans l'extrait de code suivant :

```tsx
import { fromEvent } from 'rxjs';
import { buffer, debounceTime, filter } from 'rxjs/operators';

const btn = document.getElementById("btn");
const btnClick$ = fromEvent(btn, 'click');
btnClick$.pipe(
  buffer(btnClick$.pipe(debounceTime(5000))),
  filter(clickArray => clickArray.length === 2)
).subscribe(() => {
  console.log('Deux clics en moins de 5 secondes');
});

```

Dans le code ci-dessus, nous avons utilisé la fonction `fromEvent` de `rxjs` ([https://rxjs.dev/api/index/function/fromEventPattern](https://rxjs.dev/api/index/function/fromEventPattern)) pour créer un observable à partir de l'événement de clic sur le bouton. Nous avons ensuite utilisé les opérateurs `buffer` et `debounceTime` pour tamponner les événements de clic et filtrer ceux qui se sont produits dans un intervalle de 5 secondes.

Cela nous a permis de gérer facilement le scénario de deux clics se produisant dans un intervalle de 5 secondes, le tout de manière déclarative et composable. Le symbole `$` est une notation courante pour identifier un flux, bien qu'entièrement optionnelle, vous pourriez avoir besoin de l'utiliser lorsque vous travaillez sur un projet collaboratif, car il est très courant de le voir.

Comme vous pouvez le voir, l'approche de programmation réactive est beaucoup plus déclarative et composable, peut-être pas intuitive lors de la première utilisation, mais la rendant plus facile à comprendre et à maintenir. Ceci est un exemple très basique, mais il montre la puissance de la programmation réactive lors de la gestion de combinaisons d'événements complexes.

La programmation réactive vous permet de traiter tous les événements comme des flux de données et de les manipuler de manière déclarative et composable, facilitant la gestion de scénarios complexes et de code maintenable.

** Exercice pratique :** Pour vous familiariser davantage, essayez de construire le deuxième scénario en utilisant les deux méthodes et voyez comment vous pouvez gérer des événements complexes en utilisant très peu de lignes de code

Maintenant que vous avez une idée de la manière dont vous pouvez transformer presque n'importe quoi en un observable, mettons-nous au travail et codons notre système de notification d'exemple. Ce sera un exemple très basique, le but est de montrer comment vous pouvez bénéficier de la programmation réactive lors de la gestion d'une combinaison complexe d'événements ou d'un flux de données intensives dans vos futures applications.

Commençons par créer des observables pour représenter ces flux d'événements :

```tsx
// src/observables.ts
import { Observable } from 'rxjs';

// Observable pour les nouveaux messages
export const newMessage$ = new Observable<string>((subscriber) => {
  // Simuler la réception de nouveaux messages
  setInterval(() => {
    subscriber.next('Nouveau message reçu');
  }, 3000);
});

// Observable pour les mentions d'utilisateur
export const userMentions$ = new Observable<string>((subscriber) => {
  // Simuler les mentions d'utilisateur
  setInterval(() => {
    subscriber.next('Vous avez été mentionné dans un message');
  }, 5000);
});

// Observable pour les alertes système
export const systemAlerts$ = new Observable<string>((subscriber) => {
  // Simuler les alertes système
  setInterval(() => {
    subscriber.next('Alerte système : Serveur en panne');
  }, 10000);
});

```

Dans le code ci-dessus, nous avons créé trois observables en utilisant la classe `Observable` de `rxjs` ([https://rxjs.dev/guide/observable](https://rxjs.dev/guide/observable)) : `newMessage$`, `userMentions$`, et `systemAlerts$`.

Chacun de ces observables émet une nouvelle valeur à différents intervalles. L'observable `newMessage$` émet un nouveau message toutes les 3 secondes, l'observable `userMentions$` émet un nouveau message toutes les 5 secondes, et l'observable `systemAlerts$` émet un nouveau message toutes les 10 secondes. Maintenant que nous avons nos observables configurés, nous pouvons nous y abonner et gérer les valeurs émises dans notre application.

#### Comment appliquer des opérateurs  Transformation des flux d'événements

Ensuite, appliquons des opérateurs pour filtrer et transformer nos flux d'événements afin de générer des notifications exploitables. Nous utiliserons des opérateurs comme **`filter`**, **`map`**, et **`merge`** pour traiter les flux de données entrants et générer des notifications significatives :

```tsx
// src/operators.ts
import { newMessage$, userMentions$, systemAlerts$ } from './observables';
import { merge, map, filter } from 'rxjs';

// Combiner plusieurs flux d'événements en un seul
export const combinedNotifications$ = merge(
  newMessage$.pipe(map(message => `Nouveau message : ${message}`)),
  userMentions$.pipe(map(mention => `Vous avez été mentionné : ${mention}`)),
  systemAlerts$.pipe(map(alert => `Alerte système : ${alert}`))
);

// Filtrer les notifications en fonction des préférences de l'utilisateur
export const filteredNotifications$ = combinedNotifications$.pipe(
  filter(notification => notification.startsWith('Nouveau message'))
);

```

Dans le code ci-dessus, nous avons créé trois observables : `newMessage$`, `userMentions$`, et `systemAlerts$`. Chacun de ces observables émet une nouvelle valeur à différents intervalles. L'observable `newMessage$` émet un nouveau message toutes les 3 secondes, l'observable `userMentions$` émet un nouveau message toutes les 5 secondes, et l'observable `systemAlerts$` émet un nouveau message toutes les 10 secondes.

#### Comment gérer les notifications en temps réel  S'abonner aux observables

Enfin, abonnons-nous à nos observables pour gérer les notifications en temps réel dans notre application. Nous allons nous abonner au flux de notifications combinées et afficher les notifications à l'utilisateur dans une interface client simulée :

```tsx
// src/index.ts
import { combinedNotifications$, filteredNotifications$ } from './operators';

// S'abonner aux notifications combinées et les afficher dans l'UI
combinedNotifications$.subscribe(notification => {
  // Simuler l'affichage des notifications dans l'UI
  console.log('Affichage de la notification :', notification);
});

// S'abonner aux notifications filtrées en fonction des préférences de l'utilisateur
filteredNotifications$.subscribe(notification => {
  // Simuler l'affichage des notifications filtrées dans l'UI
  console.log('Affichage de la notification filtrée :', notification);
});

```

Dans l'extrait de code ci-dessus, nous avons créé deux observables : `combinedNotifications$` et `filteredNotifications$`. Le premier combine plusieurs flux d'événements en un seul en utilisant l'opérateur merge. Le second filtre les notifications en fonction des préférences de l'utilisateur en utilisant l'opérateur filter. Nous nous abonnons ensuite à ces observables et affichons les notifications dans l'UI.

Testons à nouveau les choses en utilisant `bun` :

```bash
$ bun run src/index.ts

```

Vous devriez obtenir la sortie suivante :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-14-at-16.02.15.png)
_Figure 3 : sortie du terminal lors de l'exécution du projet_

Comme vous pouvez le voir, les notifications sont affichées dans l'UI comme prévu, et elles continuent d'arriver à mesure que de nouveaux événements sont émis, jusqu'à ce que le programme soit arrêté.

Une autre façon d'arrêter de recevoir des notifications est de se désabonner des observables, en ajoutant une condition qui exécutera le bloc suivant :

```tsx
combinedNotifications$.unsubscribe();

```

 **À vous de jouer :**  
N'hésitez pas à interagir avec le code et à explorer comment les observables et les opérateurs fonctionnent ensemble pour gérer efficacement les notifications en temps réel. Expérimentez avec différents flux d'événements et filtres pour adapter les notifications à vos préférences, en vous assurant d'utiliser autant d'opérateurs RxJS que possible. En codant, envisagez des cas d'utilisation réels et comment ce système de notification peut être appliqué à diverses applications.

Vous pouvez trouver le code source complet de cet article dans le dépôt GitHub suivant : [https://github.com/pacyL2K19/rx-programming-real-time-sample](https://github.com/pacyL2K19/rx-programming-real-time-sample). N'hésitez pas à laisser une étoile si vous le trouvez utile.

## Meilleurs pratiques et pièges courants

La programmation réactive est un paradigme puissant, mais elle s'accompagne de son propre ensemble de meilleures pratiques et de pièges potentiels.

Explorons quelques considérations clés lors de la programmation réactive dans des applications réelles :

### Meilleurs pratiques :

Voici quelques-unes des meilleures pratiques à suivre lors de la construction d'applications de manière réactive :

* **Déclaratif et composable :** Tirez parti de la nature déclarative et composable de la programmation réactive pour gérer des flux d'événements et des flux de données complexes. Utilisez des opérateurs pour transformer et combiner des observables de manière claire et maintenable.
* **Gestion des erreurs :** Implémentez des mécanismes de gestion des erreurs robustes pour gérer les exceptions ou les échecs dans vos flux d'événements. Utilisez des opérateurs comme `catchError` ([https://rxjs.dev/api/operators/catchError](https://rxjs.dev/api/operators/catchError)) ou `retryWhen` ([https://rxjs.dev/api/index/function/retryWhen](https://rxjs.dev/api/index/function/retryWhen)) pour gérer les erreurs avec grâce.
* **Gestion de la mémoire :** Soyez attentif à la gestion de la mémoire lors de la programmation avec des observables. Désabonnez-vous des observables lorsqu'ils ne sont plus nécessaires pour éviter les fuites de mémoire et la consommation inutile de ressources.
* **Tests :** Écrivez des tests unitaires complets pour vos observables et opérateurs afin de garantir qu'ils se comportent comme prévu. Utilisez des bibliothèques de test comme `Jest` ou `Mocha` pour tester votre code réactif.

### Pièges courants :

* **Surutilisation des opérateurs :** Évitez de surutiliser les opérateurs, en particulier dans les flux d'événements complexes. Bien que la gestion de flux de données/événements complexes puisse conduire à utiliser plus d'un opérateur, une surutilisation des opérateurs peut conduire à un code difficile à comprendre et à maintenir, cherchez toujours une utilisation optimale des opérateurs.
* **Complexité :** Méfiez-vous des flux d'événements et des flux de données trop complexes. Efforcez-vous de garder votre base de code réactive simple et intuitive pour éviter la confusion et les bugs.
* **Performance :** Gardez un œil sur la performance lors de la programmation réactive. Le traitement intensif des données et les combinaisons d'événements complexes peuvent impacter les performances si elles ne sont pas gérées avec soin, en particulier en sachant quand s'abonner et quand se désabonner des observables, en s'assurant que les ressources sont utilisées de manière optimale.

En suivant les meilleures pratiques et en étant conscient des pièges courants, vous pouvez exploiter tout le potentiel de la programmation réactive tout en garantissant la maintenabilité et la performance de vos applications.

## Conclusion

La programmation réactive est un paradigme transformateur qui permet aux développeurs de construire des applications réactives, évolutives et efficaces. En tirant parti des principes des flux, des observables et des opérateurs, les développeurs peuvent gérer des flux de données complexes et des opérations asynchrones avec facilité.

Que vous construisiez des tableaux de bord en temps réel, des applications IoT ou des plateformes de trading financier, la programmation réactive fournit une boîte à outils polyvalente et puissante pour gérer les flux de données dynamiques. Alors que vous continuez votre voyage avec la programmation réactive, rappelez-vous les concepts de base des flux et des observables.

Embrassez la nature déclarative et composable de la programmation réactive, et explorez la vaste gamme d'opérateurs disponibles pour transformer et combiner des observables. En faisant cela, vous déverrouillerez tout le potentiel de la programmation réactive et créerez des applications qui répondent aux exigences du développement logiciel moderne.

### Ressources

* [La programmation réactive et son effet sur la performance et le processus de développement](https://lup.lub.lu.se/luur/download?func=downloadFile&recordOId=8932146&fileOId=8932147) Par Gustav Hochbergs
* [L'introduction à la programmation réactive que vous avez manquée](https://gist.github.com/staltz/868e7e9bc2a7b8c1f754) Par André Staltz
* [Le combat pour la performance](https://devm.io/java/the-fight-for-performance-157515) Par Arne Limburg
* [Introduction à la programmation réactive](https://developer.ibm.com/series/learning-path-introduction-to-reactive-systems/) par IBM