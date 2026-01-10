---
title: Architecture Unifiée – Une Façon Plus Simple de Construire des Applications
  Full-Stack
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-09T23:42:36.000Z'
originalURL: https://freecodecamp.org/news/full-stack-unified-architecture
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/unified-architecture-2.jpg
tags:
- name: architecture
  slug: architecture
- name: full stack
  slug: full-stack
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Web Development
  slug: web-development
seo_title: Architecture Unifiée – Une Façon Plus Simple de Construire des Applications
  Full-Stack
seo_desc: 'By Manuel Vila

  Modern full-stack apps – like single-page apps or mobile apps – usually have six
  layers


  data access

  backend model

  API server

  API client

  frontend model

  and user interface.


  By architecting in this way, you can achieve some characterist...'
---

Par Manuel Vila

Les applications full-stack modernes – comme les applications monopages ou les applications mobiles – ont généralement six couches :
- accès aux données
- modèle backend
- serveur API
- client API
- modèle frontend
- et interface utilisateur.

En architecturant de cette manière, vous pouvez obtenir certaines caractéristiques d'une application bien conçue, telles que la [séparation des préoccupations](https://en.wikipedia.org/wiki/Separation_of_concerns) ou le [couplage lâche](https://en.wikipedia.org/wiki/Loose_coupling).

Mais cela ne vient pas sans inconvénients. Cela se fait généralement au détriment d'autres caractéristiques importantes, comme la simplicité, la [cohésion](<https://en.wikipedia.org/wiki/Cohesion_(computer_science)>), et l'agilité.

Il semble que nous ne puissions pas tout avoir. Nous devons faire des compromis.

Le problème est que les développeurs construisent généralement chaque couche comme un monde complètement différent.

Même si vous implémentez les couches avec le même langage, elles ne peuvent pas communiquer facilement entre elles.

Vous auriez besoin de beaucoup de [code de colle](https://en.wikipedia.org/wiki/Glue_code) pour les connecter toutes, et le [modèle de domaine](https://en.wikipedia.org/wiki/Domain_model) est dupliqué à travers la stack. En conséquence, votre agilité de développement en souffre considérablement.

Par exemple, l'ajout d'un simple champ à un modèle nécessite souvent de modifier toutes les couches de la stack. Cela peut sembler un peu ridicule.

Eh bien, j'ai beaucoup réfléchi à ce problème récemment. Et je crois avoir trouvé une solution.

Voici l'astuce : bien sûr, les couches d'une application doivent être « physiquement » séparées. Mais elles n'ont pas besoin d'être « logiquement » séparées.

## L'Architecture Unifiée
<p>
	<img src="https://liaison-blog.s3.dualstack.us-west-2.amazonaws.com/images/traditional-vs-unified-architecture.svg" alt="Architecture traditionnelle vs unifiée" style="width: 100%; margin-top: 1.5rem">
</p>

En programmation orientée objet, lorsque nous utilisons l'héritage, nous obtenons certaines classes qui peuvent être vues de deux manières : physique et logique. Que veux-je dire par là ?

Imaginons que nous avons une classe `B` qui hérite d'une classe `A`. Alors, `A` et `B` peuvent être vues comme deux classes physiques. Mais logiquement, elles ne sont pas séparées, et `B` peut être vue comme une classe logique qui compose les propriétés de `A` avec ses propres propriétés.

Par exemple, lorsque nous appelons une méthode dans une classe, nous n'avons pas à nous soucier si la méthode est implémentée dans cette classe ou une classe parente. Du point de vue de l'appelant, il n'y a qu'une seule classe à considérer. Parent et enfant sont unifiés en une seule classe logique.

Et si nous appliquions la même approche aux couches d'une application ? Ne serait-ce pas génial si, par exemple, le frontend pouvait somehow hériter du backend ?

En faisant cela, le frontend et le backend seraient unifiés en une seule couche logique. Et cela éliminerait tous les problèmes de communication et de partage. En effet, les classes, attributs et méthodes du backend seraient directement accessibles depuis le frontend.

Bien sûr, nous ne voulons généralement pas exposer tout le backend au frontend. Mais il en va de même pour l'héritage de classe, et il existe une solution élégante appelée « propriétés privées ». De même, le backend pourrait exposer sélectivement certains attributs et méthodes.

Pouvoir saisir toutes les couches d'une application depuis un seul monde unifié n'est pas une petite affaire. Cela change complètement la donne. C'est comme passer d'un monde 3D à un monde 2D. Tout devient beaucoup plus facile.

[L'héritage n'est pas mauvais](https://liaison.dev/blog/articles/Do-We-Really-Need-to-Separate-the-Model-from-the-UI-9wogqr#composition-over-inheritance). Oui, il peut être mal utilisé, et dans certains langages, il peut être assez rigide. Mais lorsqu'il est correctement utilisé, c'est un mécanisme inestimable dans notre boîte à outils.

Nous avons un problème, cependant. À ma connaissance, il n'existe aucun langage permettant d'hériter des classes à travers plusieurs environnements d'exécution. Mais nous sommes des programmeurs, n'est-ce pas ? Nous pouvons construire tout ce que nous voulons, et nous pouvons étendre le langage pour fournir de nouvelles capacités.

Mais avant d'en arriver là, décomposons la stack pour voir comment chaque couche peut s'intégrer dans une architecture unifiée.

### Accès aux Données

Pour la majorité des applications, la base de données peut être abstraite en utilisant une sorte d'ORM. Donc, du point de vue du développeur, il n'y a pas de couche d'accès aux données à considérer.

Pour des applications plus ambitieuses, nous devons peut-être optimiser les schémas de base de données et les requêtes. Mais nous ne voulons pas encombrer le modèle backend avec ces préoccupations, et c'est là qu'une couche supplémentaire peut être appropriée.

Nous construisons une couche d'accès aux données pour implémenter les préoccupations d'optimisation, et cela se produit généralement tard dans le cycle de développement, si cela se produit un jour.

Quoi qu'il en soit, si nous avons besoin d'une telle couche, nous pouvons la construire plus tard. Avec l'héritage inter-couches, nous pouvons ajouter une couche d'accès aux données par-dessus la couche de modèle backend avec presque aucun changement au code existant.

### Modèle Backend

Typiquement, une couche de modèle backend gère les responsabilités suivantes :

- Façonner le modèle de domaine.
- Implémenter la logique métier.
- Gérer les mécanismes d'autorisation.

Pour la plupart des backends, il est acceptable de les implémenter tous dans une seule couche. Mais, si nous voulons gérer certaines préoccupations séparément, par exemple, nous voulons séparer l'autorisation de la logique métier, nous pouvons les implémenter dans deux couches qui héritent l'une de l'autre.

### Couches API

Pour connecter le frontend et le backend, nous construisons généralement une API web (REST, GraphQL, etc.), et cela complique tout.

L'API web doit être implémentée des deux côtés : un client API dans le frontend et un serveur API dans le backend. Cela fait deux couches supplémentaires à gérer, et cela conduit généralement à dupliquer tout le modèle de domaine.

Une API web n'est rien de plus que du code de colle, et c'est un casse-tête à construire. Donc, si nous pouvons l'éviter, c'est une amélioration massive.

Heureusement, nous pouvons tirer parti de l'héritage inter-couches à nouveau. Dans une architecture unifiée, il n'y a pas d'API web à construire. Tout ce que nous avons à faire est de faire hériter le modèle frontend du modèle backend, et c'est tout.

Cependant, il existe encore quelques bons cas d'utilisation pour construire une API web. C'est lorsque nous devons exposer un backend à certains développeurs tiers, ou lorsque nous devons nous intégrer à certains systèmes hérités.

Mais soyons honnêtes, la plupart des applications n'ont pas une telle exigence. Et lorsqu'elles en ont, il est facile de la gérer par la suite. Nous pouvons simplement implémenter l'API web dans une nouvelle couche qui hérite de la couche de modèle backend.

Plus d'informations sur ce sujet peuvent être trouvées dans [cet article](https://liaison.dev/blog/articles/How-about-interoperability-oy3ugk).

### Modèle Frontend

Puisque le backend est la source de vérité, il doit implémenter toute la logique métier, et le frontend ne doit pas en implémenter. Donc, le modèle frontend est simplement hérité du modèle backend, avec presque aucun ajout.

### Interface Utilisateur

Nous implémentons généralement le modèle frontend et l'UI dans deux couches séparées. Mais comme je l'ai montré dans [cet article](https://liaison.dev/blog/articles/Do-We-Really-Need-to-Separate-the-Model-from-the-UI-9wogqr), ce n'est pas obligatoire.

Lorsque le modèle frontend est composé de classes, il est possible d'encapsuler les vues en tant que simples méthodes. Ne vous inquiétez pas si vous ne voyez pas ce que je veux dire pour l'instant, cela deviendra plus clair dans l'exemple plus tard.

Puisque le modèle frontend est essentiellement vide (voir ci-dessus), il est acceptable d'implémenter l'UI directement dedans, donc il n'y a pas de couche d'interface utilisateur _per se_.

L'implémentation de l'UI dans une couche séparée est encore nécessaire lorsque nous voulons supporter plusieurs plateformes (par exemple, une application web et une application mobile). Mais, puisque ce n'est qu'une question d'héritage d'une couche, cela peut venir plus tard dans la feuille de route de développement.

### Mettre Tout Ensemble

L'architecture unifiée nous a permis d'unifier six couches physiques en une seule couche logique :

- Dans une implémentation minimale, l'accès aux données est encapsulé dans le modèle backend, et il en va de même pour l'UI qui est encapsulée dans le modèle frontend.
- Le modèle frontend hérite du modèle backend.
- Les couches API ne sont plus nécessaires.

Encore une fois, voici à quoi ressemble l'implémentation résultante :

<p>
	<img src="https://liaison-blog.s3.dualstack.us-west-2.amazonaws.com/images/traditional-vs-unified-architecture.svg" alt="Architecture traditionnelle vs unifiée" style="width: 100%; margin-top: .5rem">
</p>

C'est assez spectaculaire, n'est-ce pas ?

## Liaison

Pour implémenter une architecture unifiée, tout ce dont nous avons besoin est l'héritage inter-couches, et j'ai commencé à construire [Liaison](https://liaison.dev) pour atteindre exactement cela.

Vous pouvez voir Liaison comme un framework si vous le souhaitez, mais je préfère le décrire comme une extension de langage car toutes ses fonctionnalités se situent au niveau le plus bas possible – le niveau du langage de programmation.

Ainsi, Liaison ne vous enferme pas dans un framework prédéfinis, et un univers entier peut être créé par-dessus. Vous pouvez lire plus sur ce sujet dans [cet article](https://liaison.dev/blog/articles/Getting-the-Right-Level-of-Generalization-7xpk37).

Derrière la scène, Liaison repose sur un mécanisme [RPC](https://en.wikipedia.org/wiki/Remote_procedure_call). Donc, superficiellement, il peut être vu comme quelque chose comme [CORBA](https://en.wikipedia.org/wiki/Common_Object_Request_Broker_Architecture), [Java RMI](https://en.wikipedia.org/wiki/Java_remote_method_invocation), ou [.NET CWF](https://en.wikipedia.org/wiki/Windows_Communication_Foundation).

Mais Liaison est radicalement différent :

- Ce n'est pas un [système d'objets distribués](https://en.wikipedia.org/wiki/Distributed_object). En effet, un backend Liaison est sans état, donc il n'y a pas d'objets partagés entre les couches.
- Il est implémenté au niveau du langage (voir ci-dessus).
- Sa conception est simple et il expose une API minimale.
- Il n'implique aucun code boilerplate, code généré, fichiers de configuration, ou artefacts.
- Il utilise un protocole de sérialisation simple mais puissant ([Deepr](https://deepr.io)) qui permet des fonctionnalités uniques, telles que l'invocation en chaîne, le traitement par lots automatique, ou l'exécution partielle.

Liaison commence son voyage en JavaScript, mais le problème qu'il aborde est universel, et il pourrait être porté vers n'importe quel langage orienté objet sans trop de difficulté.

### Bonjour Counter

Illustrons comment fonctionne Liaison en implémentant l'exemple classique « Counter » en tant qu'application monopage.

Tout d'abord, nous avons besoin d'un code partagé entre le frontend et le backend :

```js
// shared.js

import {Model, field} from '@liaison/liaison';

export class Counter extends Model {
  // La classe partagée définit un champ pour suivre la valeur du compteur
  @field('number') value = 0;
}
```

Ensuite, construisons le backend pour implémenter la logique métier :

```js
// backend.js

import {Layer, expose} from '@liaison/liaison';

import {Counter as BaseCounter} from './shared';

class Counter extends BaseCounter {
  // Nous exposons le champ `value` au frontend
  @expose({get: true, set: true}) value;

  // Et nous exposons également la méthode `increment()`
  @expose({call: true}) increment() {
    this.value++;
  }
}

// Nous enregistrons la classe backend dans une couche exportée
export const backendLayer = new Layer({Counter});
```

Enfin, construisons le frontend :

```js
// frontend.js

import {Layer} from '@liaison/liaison';

import {Counter as BaseCounter} from './shared';
import {backendLayer} from './backend';

class Counter extends BaseCounter {
  // Pour l'instant, la classe frontend hérite simplement de la classe partagée
}

// Nous enregistrons la classe frontend dans une couche qui hérite de la couche backend
const frontendLayer = new Layer({Counter}, {parent: backendLayer});

// Enfin, nous pouvons instancier un compteur
const counter = new frontendLayer.Counter();

// Et jouer avec
await counter.increment();
console.log(counter.value); // => 1
```

Que se passe-t-il ? En invoquant `counter.increment()`, nous avons incrémenté la valeur du compteur. Remarquez que la méthode `increment()` n'est implémentée ni dans la classe frontend ni dans la classe partagée. Elle n'existe que dans le backend.

Alors, comment est-il possible que nous puissions l'appeler depuis le frontend ? C'est parce que la classe frontend est enregistrée dans une couche qui hérite de la couche backend. Donc, lorsqu'une méthode est manquante dans la classe frontend, et qu'une méthode avec le même nom est exposée dans la classe backend, elle est automatiquement invoquée.

Du point de vue du frontend, l'opération est transparente. Il n'a pas besoin de savoir qu'une méthode est invoquée à distance. Cela fonctionne simplement.

L'état actuel d'une instance (c'est-à-dire les attributs de `counter`) est automatiquement transporté dans les deux sens. Lorsque qu'une méthode est exécutée dans le backend, les attributs qui ont été modifiés dans le frontend sont envoyés. Et inversement, lorsque certains attributs changent dans le backend, ils sont reflétés dans le frontend.

> Notez que dans cet exemple simple, le backend n'est pas exactement distant. Le frontend et le backend s'exécutent dans le même runtime JavaScript. Pour rendre le backend vraiment distant, nous pouvons facilement l'exposer via HTTP. Voir un [exemple ici](https://github.com/liaisonjs/liaison/tree/master/examples/counter-via-http/src).

Et si nous passons/retournons des valeurs à/depuis une méthode invoquée à distance ? Il est possible de passer/retourner n'importe quoi qui est sérialisable, y compris des instances de classe. Tant qu'une classe est enregistrée avec le même nom dans le frontend et le backend, ses instances peuvent être automatiquement transportées.

Et si nous remplaçons une méthode entre le frontend et le backend ? Ce n'est pas différent du JavaScript régulier – nous pouvons utiliser `super`. Par exemple, nous pouvons remplacer la méthode `increment()` pour exécuter du code supplémentaire dans le contexte du frontend :

```js
// frontend.js

class Counter extends BaseCounter {
  async increment() {
    await super.increment(); // La méthode `increment()` du backend est invoquée
    console.log(this.value); // Le code supplémentaire est exécuté dans le frontend
  }
}
```

Maintenant, construisons une interface utilisateur avec [React](https://reactjs.org/) et l'approche encapsulée montrée précédemment :

```js
// frontend.js

import React from 'react';
import {view} from '@liaison/react-integration';

class Counter extends BaseCounter {
  // Nous utilisons le décorateur `@view()` pour observer le modèle et re-rendre la vue lorsque nécessaire
  @view() View() {
    return (
      <div>
        {this.value} <button onClick={() => this.increment()}>+</button>
      </div>
    );
  }
}
```

Enfin, pour afficher le compteur, tout ce dont nous avons besoin est :

```js
<counter.View />
```

Voilà ! Nous avons construit une application monopage avec deux couches unifiées et une UI encapsulée.

### Preuve de Concept

Pour expérimenter avec l'architecture unifiée, j'ai construit une [application exemple RealWorld](https://github.com/liaisonjs/react-liaison-realworld-example-app) avec Liaison.

Je peux être partial, mais le résultat me semble assez impressionnant : implémentation simple, haute cohésion du code, 100% [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself), et pas de code de colle.

En termes de quantité de code, mon implémentation est significativement plus légère que toute autre que j'ai examinée. Consultez les [résultats ici](https://github.com/liaisonjs/react-liaison-realworld-example-app/blob/master/docs/comparison.md).

Certes, l'exemple RealWorld est une petite application, mais comme il couvre les concepts les plus importants qui sont communs à toutes les applications, je suis confiant qu'une architecture unifiée peut être mise à l'échelle pour des applications plus ambitieuses.

## Conclusion

Séparation des préoccupations, couplage lâche, simplicité, cohésion et agilité.

Il semble que nous obtenons tout, finalement.

Si vous êtes un développeur expérimenté, je suppose que vous vous sentez un peu sceptique à ce stade, et c'est tout à fait normal. Il est difficile de laisser derrière soi des années de pratiques établies.

Si la programmation orientée objet n'est pas votre tasse de thé, vous ne voudrez pas utiliser Liaison, et c'est tout à fait normal également.

Mais si vous êtes adepte de la POO, veuillez garder une petite fenêtre ouverte dans votre esprit, et la prochaine fois que vous devrez construire une application full-stack, essayez de voir comment elle pourrait s'intégrer dans une architecture unifiée.

[Liaison](https://liaison.dev/) est encore à un stade précoce, mais je travaille activement dessus, et je m'attends à publier la première version bêta début 2020.

Si vous êtes intéressé, veuillez étoiler le [dépôt](https://github.com/liaisonjs/liaison) et rester informé en suivant le [blog](https://liaison.dev/blog) ou en vous abonnant à la [newsletter](https://liaison.dev/#newsletter).

_Discutez de cet article sur [Changelog News](https://changelog.com/news/how-to-simplify-fullstack-development-with-a-unified-architecture-XVOM)_.