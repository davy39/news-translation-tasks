---
title: 'Quand utiliser TypeScript : un guide détaillé à travers des scénarios courants'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-19T17:23:29.000Z'
originalURL: https://freecodecamp.org/news/when-to-use-typescript-a-detailed-guide-through-common-scenarios-b0a57e57905
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ygOV4sntqZDN8t7u9n-MGw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: software design
  slug: software-design
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
seo_title: 'Quand utiliser TypeScript : un guide détaillé à travers des scénarios
  courants'
seo_desc: 'By Khalil Stemmler

  Strap yourself in. In this guide, we compare when it’s absolutely vital to be using
  TypeScript, the strictly-typed programming language, and when it makes sense to
  stick to vanilla JavaScript

  Have you heard of that little programmi...'
---

Par Khalil Stemmler

_Attachez votre ceinture. Dans ce guide, nous comparons quand il est absolument vital d'utiliser TypeScript, le langage de programmation strictement typé, et quand il est judicieux de rester avec JavaScript vanilla._

Avez-vous entendu parler de ce petit langage de programmation appelé **TypeScript** ? Vous savez, celui que Microsoft a créé ? Celui qui est un peu [en train d'exploser](https://redmonk.com/sogrady/2019/03/20/language-rankings-1-19) ?

Peut-être étiez-vous comme moi, un puriste de JavaScript. Je m'en sortais _très bien_ en construisant des choses avec React et Node sans types. Les prop types et la [validation Joi](https://github.com/hapijs/joi) me traitaient très bien, merci.

Peut-être avez-vous cédé à un moment donné et avez-vous essayé. Vous avez commencé à jouer avec. Peut-être que vous l'avez détesté parce qu'il vous rappelait Java. Peut-être que vous étiez énervé de ne pas pouvoir être super productif tout de suite.

Ce furent quelques-unes de **mes propres sentiments initiaux** lorsque j'ai commencé avec TypeScript.

Je ne voyais certainement pas le bénéfice... jusqu'à ce que je commence à rencontrer des choses vraiment ennuyeuses. Des choses comme des builds qui ne échouent pas quand ils le devraient, du code bogué et des fautes de frappe qui se retrouvent dans le code de production, en plus de trouver de plus en plus difficile d'exprimer mes designs de manière vraiment propre et orientée objet.

9 mois plus tard, après avoir utilisé TypeScript, j'ai construit de nouvelles fonctionnalités dans des applications Angular pour des clients, j'ai commencé à compiler le front-end React/Redux de [Univjobs](https://univjobs.ca) avec TypeScript et j'ai porté tous nos services backend de Node.js vanilla à TypeScript, en refactorisant d'énormes quantités de code en cours de route.

Dans cet article, nous allons examiner certains des scénarios les plus courants et identifier quand il pourrait être vital d'utiliser TypeScript, et quand nous pourrions probablement nous en passer et rester avec JavaScript _vanilla_.

### Pourquoi cette discussion est plus importante que jamais aujourd'hui

Je suis arrivé à la conclusion très importante que, selon votre situation, votre contexte, votre projet, votre niveau de compétence et d'autres facteurs, il est en fait **dangereux** pour votre projet de **ne pas** utiliser TypeScript aujourd'hui.

L'espace front-end, pour commencer, devient de plus en plus complexe. Certaines fonctionnalités qui étaient autrefois considérées comme de pointe sont désormais des hypothèses d'expérience utilisateur très standard.

Par exemple, il est presque toujours attendu que votre application continue de fonctionner hors ligne dans une certaine mesure. Et lorsque les utilisateurs sont en ligne, il est également généralement attendu qu'ils reçoivent des notifications en temps réel sans avoir à actualiser la page.

Ce sont des demandes assez élevées (mais définitivement pas irréalistes en 2019).

Avant de plonger dans différents scénarios, nous devrions en fait parler des trois catégories de problèmes logiciels vraiment difficiles à résoudre.

### 3 Catégories de Problèmes Logiciels Difficiles

De manière générale, il y en a trois. Le Problème de Système Performant, le Problème de Système Embarqué et le Problème de Domaine Complexe.

#### 1. Le Problème de Système Performant

Parlons de Twitter pendant un moment.

Twitter est en fait un concept très simple.

Vous vous inscrivez, vous publiez des tweets, vous aimez les tweets des autres et c'est à peu près tout.

Si Twitter est si simple, pourquoi quelqu'un d'autre ne pourrait-il pas le faire ?

Il est évident que le vrai défi pour Twitter n'est pas tant **ce qu'il fait**, mais plutôt **comment il est capable de faire ce qu'il fait**.

Twitter a le défi unique de servir les requêtes d'environ **500 millions d'utilisateurs chaque jour**.

Le problème difficile que Twitter résout est en fait un **problème de performance**.

Lorsque le défi est la performance, que nous utilisions un langage strictement typé ou non est beaucoup moins important.

#### 2. Le Problème de Système Embarqué

Un système embarqué est une combinaison de matériel informatique et de logiciel, dans le but de permettre le contrôle des aspects mécaniques ou électriques d'un système.

La plupart des systèmes que nous utilisons aujourd'hui sont construits sur une couche de code très complexe qui, si elle n'est pas initialement écrite, se compile généralement en C ou C++.

Coder dans ces langages n'est pas pour les âmes sensibles.

En C, il n'y a pas de concept d'objets ; et nous, en tant qu'humains, aimons les objets parce que nous pouvons facilement les comprendre. Le C est procédural et cela rend le code que nous devons écrire dans ce langage plus difficile à garder propre. Ces problèmes nécessitent également une connaissance des détails de bas niveau.

Le C++ améliore considérablement la vie car il est orienté objet, mais le défi reste fondamentalement l'interaction avec les détails matériels de bas niveau.

Parce que nous n'avons pas vraiment beaucoup de choix sur les langages que nous utilisons pour ces problèmes, il est donc irrelevant de considérer TypeScript ici.

#### 3. Le Problème de Domaine Complexe

Pour certains problèmes, le défi est moins de scalabilité en termes de gestion de plus de requêtes, mais de scalabilité en termes de **taille de la base de code**.

Les entreprises ont des **problèmes réels complexes** à résoudre. Dans ces entreprises, les plus grands défis d'ingénierie sont généralement :

* Pouvoir **logiquement** (domaines) séparer les parties de ce monolithe en applications plus petites. Et ensuite, **physiquement** (microservices pour contextes délimités) les diviser afin que des équipes puissent être assignées pour les maintenir
* Gérer l'intégration et la synchronisation entre ces applications
* Modéliser les concepts de domaine et résoudre réellement les problèmes du domaine
* Créer un langage _ubiquitaire_ (tout compris) à partager par les développeurs et les experts du domaine
* Ne pas se perdre dans la masse de code écrit et ralentir au point où il devient impossible d'ajouter de nouvelles fonctionnalités sans casser celles existantes

J'ai essentiellement décrit les types de problèmes que la [Conception Pilotée par le Domaine](https://khalilstemmler.com/articles/domain-driven-design-intro/) résout. Pour ces types de projets, vous ne penseriez même pas à ne pas utiliser un langage strictement typé comme TypeScript.

#### JavaScript Orienté Objet

Pour les problèmes de **Domaine Complexe**, si vous ne choisissez pas TypeScript et choisissez plutôt JavaScript, cela nécessitera un effort supplémentaire pour réussir. Non seulement vous devrez être **extra confortable** avec vos capacités de modélisation d'objets en JavaScript vanilla, mais vous devrez également savoir comment utiliser les 4 principes de la programmation orientée objet (encapsulation, abstraction, héritage et polymorphisme).

Cela peut être **difficile à faire**. JavaScript ne vient pas naturellement avec des concepts d'interfaces et de classes abstraites.

L'« Interface Segregation » des principes de conception SOLID n'est pas facilement réalisable avec JavaScript vanilla.

Utiliser JavaScript seul nécessiterait également un certain niveau de discipline en tant que développeur afin de garder le code propre, et cela est vital une fois que la base de code est suffisamment grande. Vous êtes également chargé de vous assurer que votre équipe partage la même discipline, expérience et niveau de connaissance sur la façon d'implémenter les modèles de conception courants en JavaScript. Si ce n'est pas le cas, vous devrez les guider.

Dans les projets pilotés par le domaine comme celui-ci, le grand avantage d'utiliser un langage strictement typé est **moins** d'exprimer **ce qui peut être fait**, mais plus d'utiliser l'encapsulation et la dissimulation d'informations **pour réduire la surface des bugs** en limitant ce que les objets de domaine sont **réellement autorisés à faire**.

Nous pouvons nous en passer sur le front-end, mais c'est une **exigence de langage difficile pour le backend** selon moi. C'est aussi la raison pour laquelle j'ai migré mes services backend Node.js vers TypeScript.

Il y a une raison pour laquelle TypeScript est appelé « **JavaScript qui scale** ».

Parmi toutes les trois catégories de problèmes logiciels difficiles, seul le Problème de Domaine Complexe est celui où TypeScript est une nécessité absolue.

En dehors de cela, il y a d'autres facteurs qui pourraient déterminer quand il est préférable d'utiliser TypeScript pour votre projet JavaScript.

### Taille du code

La taille du code est généralement liée au **Problème de Domaine Complexe**, où une grande base de code signifie un domaine complexe, mais ce n'est pas toujours le cas.

Lorsque la quantité de code d'un projet atteint une certaine taille, il devient **plus difficile** de garder une trace de tout ce qui existe et il devient **plus facile** de finir par réimplémenter quelque chose déjà codé.

**La duplication est l'ennemi d'un logiciel bien conçu et stable.**

Cela est particulièrement accentué lorsque de nouveaux développeurs commencent à coder sur une base de code déjà grande.

L'autocomplétion et Intellisense de Visual Studio Code aident à naviguer dans les grands projets. Cela fonctionne très bien avec TypeScript, mais c'est quelque peu limité avec JavaScript.

Pour les projets que je sais rester simples et petits, ou si je sais qu'ils seront jetés éventuellement, je serais moins enclin à recommander TypeScript comme une nécessité.

### Logiciel de production vs. projets personnels

Le **logiciel de production** est du code qui vous tient à cœur ou du code pour lequel vous aurez des ennuis s'il ne fonctionne pas. C'est aussi du code pour lequel vous avez écrit des tests. La règle générale est que « si vous vous souciez du code, vous devez avoir des tests unitaires pour celui-ci ».

Si vous ne vous en souciez pas, n'ayez pas de tests.

Les **projets personnels** sont auto-explicatifs. Faites ce que vous voulez. Vous n'avez aucun engagement professionnel à respecter des normes d'artisanat.

Allez-y et créez des choses ! Créez des petites choses, créez des grandes choses.

Peut-être qu'un jour vous ressentirez la douleur lorsque votre projet personnel deviendra votre projet principal, qui deviendra un logiciel de production, qui est bogué parce qu'il n'avait pas de tests ou de types... pas comme si j'y avais été ou quoi que ce soit...

#### Manque de Tests Unitaires

Il n'est pas toujours possible d'avoir des tests pour tout, parce que, eh bien — **la vie**.

Dans ce cas, je dirais que si vous n'avez pas de Tests Unitaires, la meilleure chose suivante que vous pourriez avoir est la vérification au moment de la compilation avec TypeScript. Après cela, si vous utilisez React, la meilleure chose suivante est d'utiliser la vérification à l'exécution avec les Prop types.

Cependant, la vérification au moment de la compilation n'est **pas un substitut** à l'avoir des tests unitaires. La bonne chose est que les tests unitaires peuvent être écrits dans n'importe quel langage — donc l'argument pour TypeScript ici est irrelevant. Ce qui est important, c'est que les tests soient écrits et que nous soyons confiants dans notre code.

### Startups

Utilisez définitivement ce qui vous aide à être le plus productif.

À ce stade, le langage que vous choisissez compte beaucoup moins.

La chose la plus importante pour vous à faire est de **valider votre produit**.

Choisir un langage (Java, par exemple) ou un outil (comme Kubernetes) que vous avez entendu aiderait à scaler à l'avenir (tout en étant totalement unfamiliar avec celui-ci) peut ou non être la meilleure option dans le cas d'une startup.

Selon votre stade, la chose la plus importante pour vous à faire est d'être productif.

Dans l'article célèbre de Paul Graham, [The Python Paradox](http://www.paulgraham.com/pypar.html), son point principal est que les ingénieurs de startup devraient simplement utiliser la technologie qui maximise leur productivité.

Dans l'ensemble, dans ce cas, utilisez ce avec quoi vous êtes le plus à l'aise : avec ou sans types. Vous pouvez toujours refactoriser vers un meilleur design une fois que vous savez que vous avez construit quelque chose que les gens veulent vraiment.

### Travailler en équipe

Selon la taille de votre équipe et les frameworks que vous utilisez, l'utilisation de TypeScript pourrait être un facteur décisif.

#### Grandes équipes

Lorsque les équipes sont suffisamment grandes (parce que les problèmes sont suffisamment grands), c'est une bonne raison d'utiliser un framework opinionné, comme Angular pour le front-end, et TypeScript pour le backend.

La raison pour laquelle l'utilisation d'un framework opinionné est bénéfique est que vous limitez le nombre de façons possibles pour les gens d'accomplir quelque chose. Dans Angular, il y a pratiquement une seule façon principale d'ajouter un Route Guard, d'utiliser l'Injection de Dépendances, de configurer le Routing, le Lazy-Loading et les Reactive Forms.

L'énorme avantage ici est que l'API est bien spécifiée.

Avec TypeScript, nous économisons également des quantités massives de temps et rendons la communication efficace.

La capacité de déterminer rapidement les arguments requis et leur type de retour pour toute méthode, ou la capacité de décrire explicitement l'intention du programme à travers des variables publiques, privées et protégées est incroyablement utile.

Oui, une partie de cela est possible avec JavaScript, mais c'est du bricolage.

#### Communiquer les modèles et implémenter les principes de conception

Non seulement cela, mais les **modèles de conception**, les solutions aux problèmes courants dans le logiciel, sont plus facilement communiqués à travers des langages explicitement strictement typés.

Voici un exemple JavaScript d'un modèle courant. Voyez si vous pouvez identifier ce que c'est.

```js

class AudioDevice {
  constructor () {
    this.isPlaying = false;
    this.currentTrack = null;
  }

  play (track) {
    this.currentTrack = track;
    this.isPlaying = true;
    this.handlePlayCurrentAudioTrack();
  }

  handlePlayCurrentAudioTrack () {
    throw new Error(`Erreur de responsabilité de la sous-classe`)
  }
}

class Boombox extends AudioDevice {
  constructor () {
    super()
  }

  handlePlayCurrentAudioTrack () {
    // Lecture via les haut-parleurs de la boombox
  }
}

class IPod extends AudioDevice {
  constructor () {
    super()
  }

  handlePlayCurrentAudioTrack () {
    // S'assurer que les écouteurs sont branchés
    // Lecture via l'ipod
  }
}

const AudioDeviceType = {
  Boombox: 'Boombox',
  IPod: 'Ipod'
}

const AudioDeviceFactory = {
  create: (deviceType) => {
    switch (deviceType) {
      case AudioDeviceType.Boombox:
        return new Boombox();
      case AudioDeviceType.IPod:
        return new IPod();
      default:
        return null;
    }
  } 
}

const boombox = AudioDeviceFactory
  .create(AudioDeviceType.Boombox);

const ipod = AudioDeviceFactory
  .create(AudioDeviceType.IPod);
```

Si vous avez deviné **Factory Pattern**, vous avez raison. Selon votre familiarité avec le modèle, cela n'a peut-être pas été si évident pour vous.

Regardons-le maintenant en TypeScript. Voyez combien plus d'intention nous pouvons signifier sur **AudioDevice** en TypeScript.

```js
abstract class AudioDevice {
  protected isPlaying: boolean = false;
  protected currentTrack: ITrack = null;

  constructor () {
  }

  play (track: ITrack) : void {
    this.currentTrack = track;
    this.isPlaying = true;
    this.handlePlayCurrentAudioTrack();
  }

  abstract handlePlayCurrentAudioTrack () : void;
}
```

**Améliorations immédiates**

* Nous savons que la classe est abstraite **tout de suite**. Nous devions fouiner dans l'exemple JavaScript.
* **AudioDevice** peut être instancié dans l'exemple JavaScript. C'est mauvais, nous avions l'intention que **AudioDevice** soit une classe abstraite. Et les classes abstraites ne devraient pas pouvoir être instanciées, elles sont seulement destinées à être sous-classées et implémentées par des [classes concrètes](https://khalilstemmler.com/wiki/concrete-class/). Cette limitation est correctement mise en place dans l'exemple TypeScript.
* Nous avons signalé la portée des variables.
* Dans cet exemple, **currentTrack** fait référence à une interface. Selon le **principe de conception** [Inversion des Dépendances](https://khalilstemmler.com/wiki/dependency-inversion/), nous devrions toujours dépendre des abstractions, pas des concrétions. Cela n'est pas possible dans l'implémentation JavaScript.
* Nous avons également signalé que toute sous-classe de **AudioDevice** devra implémenter **handlePlayCurrentAudioTrack** elle-même. Dans l'exemple JavaScript, nous avons exposé la possibilité pour quelqu'un d'introduire des erreurs d'exécution en essayant d'exécuter la méthode à partir de la classe abstraite illégale ou de l'implémentation de classe concrète non complète.

À retenir : Si vous travaillez dans une grande équipe et que vous devez minimiser les façons dont quelqu'un pourrait mal utiliser votre code, TypeScript est un bon moyen d'aider à résoudre cela.

### Petites équipes et styles de codage

Les petites équipes sont beaucoup plus faciles à gérer en termes de styles de codage et de communication. Associées à des outils de linting, des discussions fréquentes sur la façon dont les choses seront faites et des hooks de pré-commit, je pense que les petites équipes peuvent être vraiment performantes sans TypeScript.

Je pense que le succès est une équation impliquant la taille de la base de code et la taille de l'équipe.

**À mesure que la base de code grandit**, l'équipe pourrait constater qu'elle doit compter sur une aide du langage lui-même pour se souvenir où se trouvent les choses et comment elles devraient être.

**À mesure que l'équipe grandit**, elle pourrait constater qu'elle a besoin de plus de règles et de restrictions pour garder le style cohérent et éviter le code dupliqué.

### Frameworks

#### React & Angular

Ce qui attire beaucoup de développeurs, y compris moi-même, vers React est la capacité d'écrire du code comme vous le souhaitez et de manière élégante/intelligente.

Il est vrai que React fait de vous un meilleur développeur JavaScript car il vous force à aborder les problèmes différemment, il vous force à être conscient de comment **this binding** fonctionne en JavaScript et vous permet de composer de grands composants à partir de petits.

React vous permet également d'avoir un peu de votre propre style. Et en raison du nombre de façons dont je peux implémenter une tâche donnée, je vais le plus souvent écrire des applications React.js vanilla lorsque :

* la base de code est petite
* c'est juste moi qui la code

Et je vais la compiler avec TypeScript lorsque :

* plus de 3 personnes la codent, ou
* la base de code est censée être très grande

Je vais également optionnellement utiliser Angular pour la même raison pour laquelle je vais compiler React avec TypeScript.

### Conclusion

En conclusion, ce sont mes opinions personnelles sur quand TypeScript est absolument nécessaire et je vous invite à ne pas être d'accord avec tout cela.

C'est ce qui a fonctionné pour moi dans le passé lorsque je devais décider d'utiliser ou non TypeScript. Cependant, aujourd'hui, puisque j'ai vu la lumière, ce n'est pas beaucoup plus d'effort pour moi d'utiliser TypeScript plutôt que JavaScript vanilla, car je suis également à l'aise avec les deux et je préfère la sécurité des types.

Mes points finaux ici sont :

#### Vous pouvez toujours commencer à utiliser TypeScript progressivement

Commencez progressivement en ajoutant TypeScript et ts-node à votre package.json et en utilisant l'option **allowjs: true** dans votre fichier tsconfig.

C'est ainsi que j'ai migré toutes mes applications Node.js vers TypeScript au fil du temps.

#### Les erreurs de compilation sont meilleures que celles d'exécution

Vous ne pouvez pas argumenter contre cela. Si attraper les bugs dans le code de production est particulièrement important pour vous, TypeScript vous aidera à minimiser beaucoup de ceux-ci.

#### Si vous êtes en position de l'apprendre, apprenez-le. Cela fait des merveilles pour vos compétences en conception logicielle

Selon où vous en êtes dans votre vie et votre carrière, vous n'aurez peut-être pas le temps de l'apprendre. Si vous avez le temps, je vous recommande de commencer à l'apprendre et à apprendre les **principes de conception SOLID** et les **modèles de conception logicielle**. C'est le **moyen le plus rapide de monter en niveau en tant que Développeur Junior** selon mon opinion honnête.

J'espère que cet article vous a été utile ! Envisagez-vous d'utiliser TypeScript pour votre prochain projet ? Faites-moi savoir si vous êtes d'accord ou non dans les commentaires.

#### [Apprendre TypeScript & JavaScript Entreprise](https://khalilstemler.com)

Modèles, principes et tutoriels essentiels de développement logiciel avec JavaScript et TypeScript modernes.

> Originalement publié le [6 avril](http://khalilstemmler.com) @ [**khalilstemmler.com**](https://khalilstemmler.com)**.**