---
title: Comment le code devient un dépotoir (et comment le corriger !)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-18T20:36:52.000Z'
originalURL: https://freecodecamp.org/news/fixing-code-dumping-grounds
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/ashim-d-silva-Kw_zQBAChws-unsplash.jpg
tags:
- name: clean code
  slug: clean-code
- name: Code Quality
  slug: code-quality
- name: refactoring
  slug: refactoring
seo_title: Comment le code devient un dépotoir (et comment le corriger !)
seo_desc: 'By James Hickey

  Earlier in my career, I faced a sort of career crisis.

  I was part of a team creating a large analytics platform in the automotive industry.
  This application had the typical "enterprise-y" layered architecture you would expect
  ("Busine...'
---

Par James Hickey

Plus tôt dans ma carrière, j'ai fait face à une sorte de crise professionnelle.

Je faisais partie d'une équipe créant une grande plateforme d'analyse dans l'industrie automobile. Cette application avait l'architecture en couches "entreprise" typique à laquelle on pourrait s'attendre ("Couche Métier", "Couche d'Accès aux Données", "Noyau", etc.).

On pourrait s'attendre à trouver la logique métier - la logique métier vraiment importante - intégrée quelque part dans le code de ces couches. Mais, généralement, les règles métier vraiment importantes étaient codées dans des procédures stockées.

**Les procédures stockées**, si vous ne savez pas ce que c'est, c'est comme une fonction que vous créez à l'intérieur d'une base de données qui utilise une syntaxe de type SQL pour traiter les données, les stocker, etc.

Je me demandais quel était le but des couches. Elles n'avaient aucun code sauf pour passer des données aux procédures stockées ou afficher les données retournées par l'une d'elles.

J'ai commencé à en apprendre davantage sur la programmation orientée objet, les meilleures pratiques de l'industrie, SOLID, d'autres paradigmes de programmation, l'architecture des applications, etc.

De cette crise professionnelle, j'ai découvert que ces problèmes ont déjà été résolus ! Il suffit de faire des recherches, de prendre du temps et de pratiquer pour les apprendre et devenir compétent.

## Orienté Objet ?

Une chose que j'ai découverte est que tous les projets sur lesquels j'ai travaillé et qui faisaient de la programmation "Orientée Objet" ne faisaient pas de la vraie POO. Le simple fait d'utiliser des classes ne signifie pas que vous faites de la POO. Surtout si vous utilisez des procédures stockées pour encoder toutes vos règles métier.

### Une courte parenthèse : Le grand débat

Il faut en parler : la programmation orientée objet ou la programmation fonctionnelle est-elle meilleure ?

Pour commencer, la plupart des gens ne comprennent pas ce que la POO était censée être en premier lieu. Similaire à la façon dont Agile aujourd'hui est généralement mal compris (par exemple, juste parce que vous avez des réunions quotidiennes, utilisez des points de story, kanban, etc., cela ne signifie pas que vous faites de l'Agile).

Alan Kay est considéré comme l'un des pères de la POO. [Dans un certain email](http://userpage.fu-berlin.de/~ram/pub/pub_jf47ht81Ht/doc_kay_oop_en), il a donné quelques explications franches sur ce que la POO était censée être.

> "Je pensais aux objets comme à des cellules biologiques et/ou à des ordinateurs individuels sur un réseau, ne pouvant communiquer qu'avec des messages (donc la messagerie est venue dès le début - il a fallu un certain temps pour voir comment faire de la messagerie dans un langage de programmation de manière suffisamment efficace pour être utile)...

> La POO pour moi signifie seulement la messagerie, la rétention locale et la protection et le masquage de l'état-processus, et la liaison extrêmement tardive de toutes choses...

> Mais juste pour montrer à quel point une idée peut persister, tout au long des années soixante-dix et quatre-vingt, il y avait beaucoup de gens qui essayaient de se débrouiller avec 'Appel de Procédure à Distance' au lieu de penser aux objets et aux messages."

Pour ceux qui sont familiers avec les microservices, le modèle d'acteur, et d'autres paradigmes de programmation avancés, votre sens de Spidey est en alerte. Ceux-ci sont en fait plus étroitement liés à la vraie POO.

Alors, la PF est-elle meilleure que la vraie POO ?

Je ne pense pas. Je pense qu'elles ont toutes deux leurs mérites. De nombreux langages aujourd'hui embrassent les deux paradigmes et permettent aux développeurs d'utiliser les outils et méthodes qui fonctionnent le mieux pour le problème donné !

Ce que vous trouverez généralement, ce sont des classes qui exposent toutes leurs propriétés ou membres de données internes. Une requête HTTP ou une requête de base de données remplira toutes les propriétés, et ensuite, peut-être, autre chose travaillera sur les données de cet objet.

Au lieu de ce qu'Alan Kay avait l'intention d'être de petits "paquets" qui s'envoient des messages (voir la parenthèse ci-dessus), la plupart des développeurs utilisent les objets comme de simples "conteneurs de données". Des variables glorifiées, en quelque sorte.

Ce que vous trouverez également dans de nombreuses bases de code, ce sont des classes très génériques comme `User`, `Customer` ou `Order`.

Est-ce mauvais ? Eh bien, **oui**.

Permettez-moi de vous poser une question :

Est-ce que `User` est utilisé dans de nombreux endroits différents et sans rapport dans votre application ?

Par exemple, est-ce que votre classe `User` est utilisée dans la partie facturation de votre code, les parties profil utilisateur, les parties livraison, etc. ?

La plupart des systèmes font quelque chose comme ça.

Ce qui finira par se passer, c'est que, parce que ces classes sont si génériques, **elles deviennent des dépotoirs pour du code dont nous ne savons pas où il appartient.**

Au lieu de prendre le temps de réfléchir au besoin métier pour ce nouveau code que nous avons écrit, souvent nous pensons qu'il est plus facile de le mettre dans nos classes génériques. C'est tout partageable, n'est-ce pas ? Et nous sommes tous pour la réutilisation de code, n'est-ce pas ?

## Couplage

Alors... que se passe-t-il si je modifie la classe `User` pour qu'elle se conforme à une certaine logique de facturation ? Quelles sont les chances que j'aie également cassé la fonctionnalité de livraison en modifiant cette classe ? Je ne sais pas, mais c'est **plus de 0%.**

Cette classe `User` a couplé toutes vos fonctionnalités ensemble. Cela cause beaucoup de problèmes.

Idéalement, nous voulons que notre code soit orthogonal (ce n'est qu'un mot fantaisiste qui signifie que changer du code à un endroit n'affectera pas d'autres endroits sans rapport).

Nous voulons pouvoir changer la fonctionnalité de livraison, par exemple, et **ne pas avoir à tester toute notre application à nouveau.** Mais, si nous partageons notre classe `User` partout, alors, pour avoir confiance que nous n'avons rien cassé, nous devons tout re-tester.

Cela conduit à une peur de changer le code. La peur de rendre notre code meilleur. Cela conduit également à beaucoup de bugs.

Si vous construisez la fonctionnalité de paiement pour votre application - vous ne devriez pas avoir à penser si vous cassez la fonctionnalité de livraison en même temps ! Cela cause une charge cognitive énorme qui n'a pas besoin d'être là.

### Une autre parenthèse : Signal d'avertissement

Dans l'ensemble, je trouve que l'idée de segmenter vos fonctionnalités/fonctions métier via différents dossiers physiques ou même des projets entièrement différents est la meilleure. [J'ai écrit à ce sujet auparavant](https://dev.to/jamesmh/the-life-changing-and-time-saving-magic-of-feature-focused-code-organization-1708).

Mais, lorsqu'il s'agit de notre code à un niveau plus profond, nous pouvons encore tendre à concevoir nos classes et objets de manière encore trop générique et entraîner beaucoup de couplage.

Chaque fois que je trouve des classes qui ont des noms simples comme `User` ou `Customer`, un signal d'avertissement se déclenche. Je préférerais voir des classes qui sont créées pour un contexte spécifique.

Par exemple, si je voyais une classe nommée `UserForAuthentication` ou `PaymentsCustomer`, alors j'aurais plus confiance que ces classes ne sont pas utilisées et réutilisées dans trop de contextes.

Voici une méthode de base qui pourrait aider à commencer à analyser vos classes. Prenez le nom de votre classe et répondez à ces questions :

Y a-t-il un sujet ? (user, client, order, etc.)

Y a-t-il un contexte pour ce sujet ? (shipping, orders, dashboard, etc.)

Y a-t-il peut-être même une action effectuée sur le sujet ? (comme nous le verrons plus en détail bientôt)

Si vous ne pouvez pas répondre à 2 de ces questions, alors je dirais qu'il y a de bonnes chances que votre classe fasse trop de choses en étant trop générique.

## L'un de ces éléments n'est pas comme les autres

Il y a un principe de programmation appelé le Principe de Responsabilité Unique.

Lorsqu'on regarde des classes ou des méthodes qui font trop de choses, utiliser le SRP comme une lumière directrice peut nous aider à faire du code qui est plus facile à maintenir, moins couplé et donc conduit à moins de bugs.

Regardons une classe `User` générique qui pourrait être similaire au code que vous avez vu auparavant :

```typescript
class User {
    public firstName: string;
    public lastName: string;
    public id: number;
    public jwtToken: string;
    public homeAddress: string;
    public creditCardNo: string;

    public getFullName(): string {
        return this.firstName + " " + this.lastName;
    }

    public decodeJwtToken(): string {
        return decode(this.jwtToken);
    }
}

```

Ça vous semble familier ?

Étant donné le nom de la classe, nous devrions commencer à être suspicieux qu'elle est trop générique.

## Vous avez du courrier

Vous avez été chargé d'ajouter une nouvelle exigence métier. Nous avons besoin que les utilisateurs puissent payer leurs produits en utilisant PayPal.

Cette classe `User` est déjà utilisée dans plusieurs endroits comme le profil utilisateur, les fonctionnalités de livraison et de paiement.

Tout ce que nous avons à faire est d'ajouter l'adresse e-mail PayPal de l'utilisateur à l'utilisateur. N'est-ce pas ?

## Le décomposer

Habituellement, vous recevrez de nouvelles exigences métier qui nécessitent _plus_ de changements à votre code que cela. Mais c'est un exemple simple.

Si nous commençons à changer cette classe `User` pour qu'elle fonctionne avec la fonctionnalité de paiement, alors nous risquons d'affecter le profil utilisateur ou la fonctionnalité de livraison (puisqu'ils utilisent également cette classe).

Que devrions-nous faire ?

La meilleure chose à faire ici est de _créer une classe utilisateur différente qui est utilisée dans chaque contexte spécifique._

De cela devraient sortir des classes comme `UserForAuthentication`, `UserProfileUser`, `ShippingUser` et `PaymentUser`.

Est-ce que ces modèles/classes vont contenir des morceaux de données similaires dont ils auront tous besoin ? Bien sûr.

Vont-ils également avoir des morceaux de données qui ne sont utilisés que dans un contexte ? Bien sûr.

Par exemple, l'`id` de l'utilisateur est nécessaire partout.

Mais, l'adresse domicile de l'utilisateur n'est nécessaire que par la livraison. Pourquoi alors, la fonctionnalité de paiement a-t-elle besoin d'accéder à ces données ? Ce n'est pas le cas.

Voici à quoi ces classes pourraient ressembler :

```typescript
class UserProfileUser {
    public firstName: string;
    public lastName: string;
    public id: number;
    public homeAddress: string;
    
    public getFullName(): string {
        return this.firstName + " " + this.lastName;
    }
}

class ShippingUser {
    public id: number;
    public homeAddress: string;
}

class UserForAuthentication {
    public id: number;
    public jwtToken: string;

    public decodeJwtToken(): string {
        return decode(this.jwtToken);
    }
}

class PaymentUser {
    public id: number;
    public creditCardNo: string;
}

```

## Gardez les choses séparées

Remarquez que l'adresse domicile est nécessaire pour `UserProfileUser` et `ShippingUser`. Est-ce mauvais ?

On nous a tant répété que dupliquer du code est une mauvaise chose. Tellement que c'est cette idée qui a causé les problèmes dont nous parlons en ce moment !

Parfois, il est préférable de "dupliquer" du code et/ou des données - s'ils sont dans des contextes différents. Encore une fois, nous voulons éviter de coupler nos fonctionnalités et classes ensemble.

Permettez-moi de vous poser une question :

_Est-il probable que le comportement de l'adresse domicile dans le profil utilisateur soit différent du comportement pour la livraison ?_

La réponse : **oui.**

Alors, nous parlons de deux choses différentes. Ce sont les mêmes données brutes mais **pas la même fonction ou concept métier**_._

La livraison a besoin de l'adresse domicile pour savoir **où envoyer les produits.**

Le profil utilisateur a besoin de l'adresse domicile **pour que l'utilisateur puisse mettre à jour ses valeurs depuis une interface utilisateur.**

_Pas les mêmes choses._

De plus, considérons qu'il pourrait également être logique d'ajouter une adresse à la classe `PaymentUser`. Mais, ce contexte devrait-il partager la même adresse que la livraison ?

Eh bien, est-il possible que votre adresse de livraison ne soit pas la même adresse que celle à laquelle vous voulez facturer ? Bien sûr ! Cela arrive tout le temps !

En utilisant le Principe de Responsabilité Unique, nous voyons que ces deux concepts/responsabilités doivent être gardés séparés.

De plus, remarquez que _la plupart_ de nos morceaux de données **ne sont pas** partagés. Le jeton JWT, par exemple, n'est nécessaire que pour authentifier un utilisateur. Pourquoi aurions-nous jamais besoin de ce morceau de données dans le code de la fonctionnalité de livraison ?

Maintenant, cette information est isolée.

**De plus, toutes les méthodes qui agissent sur ces données seront également déplacées et ne seront pas appelées de manière inappropriée par le code d'une autre fonctionnalité.**

C'était un exemple simple, et dans la plupart des cas, cela peut devenir un peu plus compliqué que nous ne le souhaiterions. À la fin, cependant, garder différents concepts métier séparés les uns des autres rendra votre code plus facile à comprendre dans un contexte spécifique, plus facile à maintenir et deviendra moins sujet aux erreurs !

Ceci est un extrait de mon livre ["Refactoring TypeScript: Keeping Your Code Healthy"](https://leanpub.com/refactoringtypescript). Cette section du livre contient **plus** de techniques pour vous aider à gérer ces types de dépotoirs. Si vous avez aimé cet article, alors [découvrez le livre pour plus de contenu comme celui-ci !](https://leanpub.com/refactoringtypescript)

Vous pouvez également [me suivre](https://twitter.com/jamesmh_dev) sur Twitter.