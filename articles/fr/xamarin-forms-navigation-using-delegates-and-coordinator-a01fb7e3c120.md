---
title: Comment implémenter la navigation Xamarin.Forms en utilisant des délégués et
  des coordinateurs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-20T17:36:13.000Z'
originalURL: https://freecodecamp.org/news/xamarin-forms-navigation-using-delegates-and-coordinator-a01fb7e3c120
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jQnSCD-sqgoSDH9ucrFRKA.jpeg
tags:
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: software architecture
  slug: software-architecture
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Comment implémenter la navigation Xamarin.Forms en utilisant des délégués
  et des coordinateurs
seo_desc: 'By Rafael Fiol

  Recently I have been thinking a lot about how to best implement page navigation
  within a Xamarin.Forms mobile app. My deep-dive into this topic started when a colleague
  sent me an article entitled The Coordinator, written by Soroush Kh...'
---

Par Rafael Fiol

Récemment, j'ai beaucoup réfléchi à la meilleure façon d'implémenter la navigation entre les pages dans une application mobile Xamarin.Forms. Ma plongée en profondeur dans ce sujet a commencé lorsqu'un collègue m'a envoyé un article intitulé [The Coordinator](http://khanlou.com/2015/10/coordinators-redux/), écrit par [Soroush Khanlou](http://khanlou.com/). Au début, j'étais un passager très heureux du mouvement Coordinator. Je suppose que je le suis toujours. C'est une manière merveilleuse de penser et d'implémenter la [séparation des préoccupations](https://en.wikipedia.org/wiki/Separation_of_concerns) en ce qui concerne l'UI/UX et la navigation générale.

Les notes suivantes représentent mes réflexions sur le sujet, les apprentissages concernant une implémentation dans Xamarin.Forms, et comment les **délégués** en C# peuvent aider.

### Pourquoi les Coordinateurs ?

La solution de Soroush se concentre principalement sur les problèmes liés aux contrôleurs de vue surchargés (citant l'UIViewController iOS comme exemple principal), et suggère que la responsabilité principale d'un Coordinateur devrait être de prendre en charge la navigation et la mutation du modèle. Il déclare que :

> Lorsque nous retirons ces tâches à un contrôleur de vue, nous obtenons un contrôleur de vue qui est _inerte_. Il peut être présenté, il peut récupérer des données, les transformer pour la présentation, les afficher, mais il ne peut cruciale les altérer.

C'est bien. C'est ce que nous voulons. Cela signifie que nous pouvons réutiliser nos contrôleurs de vue comme participants dans plusieurs flux de travail, avec des Coordinateurs spécialement conçus pour chaque flux de travail. Nos Pages et View Models — dans nos applications MVVM — n'auront plus de préoccupations de navigation désordonnées.

Considérons ce scénario courant. Imaginons que votre application inclut une page de connexion. Après qu'un utilisateur a complété la page de connexion, votre application affiche ensuite une page de tableau de bord. Ensuite, dans une incarnation ultérieure de la conception de votre application, vous décidez que toutes les pages ne nécessitent pas une connexion. Que se passe-t-il si vous souhaitez réutiliser cette page de connexion ailleurs, et aller vers une page post-connexion différente selon le flux de travail qui déclenche la connexion ?

La solution évidente (et laide) consiste à commencer à parsemer vos Pages ou View Models de logique conditionnelle — normalement sous la forme d'instructions IF/THEN. Cela ne s'adapte jamais, et dans les grandes applications, vous obtenez un code très fragile.

### **Les Coordinateurs à la rescousse.**

Lorsque j'ai commencé mes expériences pour implémenter des Coordinateurs dans Xamarin.Forms, j'avais plusieurs objectifs de conception en tête.

Premièrement, cela ne concerne pas MVVM. Je n'ai pas envie d'implémenter un autre framework MVVM pour Xamarin. De plus, la navigation n'est pas une préoccupation MVVM. J'affirme que les View Models (et d'ailleurs, les Pages) ne devraient pas être conscients des autres View Models (et pages) au sein d'une application.

Deuxièmement, les Coordinateurs ne devraient rien savoir sur le View Model sous-jacent qui supporte une page. Mon désir est qu'un Coordinateur lance simplement des pages et réponde aux **hooks** exposés par ces pages. Cela est quelque peu analogue à l'idée de [webhooks](https://en.wikipedia.org/wiki/Webhook) (plus sur cela dans un instant).

Troisièmement, je voulais que l'implémentation soit simple, sans beaucoup de coercition d'objets, et sans diminuer aucune des fonctionnalités qui rendent le RAD avec Xamarin.Forms si incroyable.

### Les délégués à la rescousse.

Avant de commencer à construire des Coordinateurs, nous devons d'abord aborder un problème fondamental qui se pose avec chaque projet MVVM. Plus précisément, comment un View Model, qui gère les interactions UI, signale-t-il au flux de travail qu'il a terminé sa tâche prévue ?

En utilisant l'exemple de connexion que j'ai cité précédemment, comment le View Model signale-t-il que l'utilisateur s'est connecté avec succès (ou sans succès), et transmet-il le jeton d'accès généré et les informations utilisateur au flux de travail qui a instancié la page ? Et plus important encore, comment le View Model publie-t-il ces informations ? Existe-t-il un contrat qui peut être inspecté sans avoir à parcourir des réams de code ?

Pour moi, la solution était d'utiliser des [délégués](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/delegate). En C#, un **délégué** est une variable de type référence qui contient une référence à une méthode. Les délégués sont similaires aux pointeurs de fonction en C++. Cependant, les délégués sont sûrs et sécurisés. En utilisant des délégués, je crée des **hooks**, que l'appelant peut utiliser pour participer et influencer le flux de travail.

Par exemple, dans mon LoginViewModel, je déclare une définition de délégué, comme suit :

J'ai ajouté cela dans l'espace de noms, juste au-dessus de la déclaration réelle de ma classe LoginViewModel. Cela définit le modèle pour le délégué, pas l'implémentation réelle. Il indique à un programmeur que ce View Model effectuera un rappel lorsque la connexion sera terminée, et définit quels paramètres seront passés. Dans mon LoginViewModel, j'expose une propriété de ce type. Les utilisateurs de ce View Model peuvent s'y _attacher_, pour obtenir un rappel lorsque la connexion est terminée.

Dans le LoginViewModel, il n'y a pas d'implémentation de ce délégué. Au lieu de cela, l'appelant du View Model implémentera la méthode — généralement sous forme de méthode anonyme ou lambda — créant une sorte de modèle de rappel (ou **webhook**).

Également dans le LoginViewModel se trouve une implémentation d'une **ICommand** qui est invoquée lorsque le bouton de connexion est pressé. C'est dans cette commande, après que la connexion soit réussie, que nous invoquons le délégué. Ci-dessous se trouve un extrait de l'implémentation de la commande. J'ai omis une grande partie du code standard lié à la gestion des exceptions, etc.

Remarquez la dernière ligne, qui invoque le délégué. Remarquez également le [null conditional](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/null-conditional-operators). Le délégué n'est invoqué que s'il existe. Alors voyons comment nous pouvons utiliser cela.

### Enfilage du Hook.

Nous ne sommes pas encore tout à fait prêts à créer nos Coordinateurs. Mais nous avons résolu un objectif de conception majeur. Nous avons défini une stratégie pour que nos View Models exposent des événements importants du cycle de vie à quiconque s'y intéresse. En continuant avec l'exemple du LoginViewModel, nous pouvons nous y connecter comme suit :

Simple. Ce qui précède montre comment nous pouvons créer une méthode anonyme qui sera invoquée par notre View Model. La méthode recevra le jeton d'accès et l'objet utilisateur, afin que nous puissions _faire quelque chose d'important_ avec, comme stocker ces données et naviguer vers la page suivante, par exemple. C'est là que nos Coordinateurs interviennent. Ils utiliseront ces hooks pour faire quelque chose d'important.

### Que faire des Pages code-behind ?

Plus tôt, j'ai dit que _nous avons défini une stratégie pour que nos View Models exposent des événements importants du cycle de vie à quiconque s'y intéresse_. La question est : exactement qui s'intéresse à la fin de la connexion ? Eh bien, nos _Coordinateurs encore non définis_ s'en soucieront. Mais, rappelez-vous que mon deuxième objectif de conception stipulait :

> Les Coordinateurs ne devraient rien savoir sur le View Model sous-jacent qui supporte une page.

J'ai pris la décision que cela devait être une règle stricte. Mes Coordinateurs connaissent les pages qui composent un flux de travail, mais ne connaissent pas et n'interagissent pas avec les View Models de ces pages. En fait, mes pages code-behind créent leurs View Models en tant que propriétés _protégées_. Donc, pour garder les contrats propres, mes pages code-behind relaient simplement les invocations de délégués. Par exemple, mon code-behind de LoginPage ressemble à ceci :

Remarquez que la page code-behind s'enregistre elle-même en tant qu'objet intéressé par un rappel du View Model (ligne 12), puis — parce que le code-behind ne se préoccupe pas des questions de navigation — il relaye simplement le rappel à son propre délégué (ligne 13).

Cela peut sembler redondant, mais cela a des applications pratiques. Premièrement, cela signifie que le View Model peut exposer des méthodes de délégué qui sont privées à la page code-behind. Deuxièmement, cela signifie qu'il y a un couplage très lâche entre les Coordinateurs et les pages.

### Une implémentation de Coordinateur Xamarin

Avec cela, et mon troisième objectif de conception en tête, qui est...

> Je voulais que l'implémentation soit simple, sans beaucoup de coercition d'objets, et sans diminuer aucune des fonctionnalités qui rendent le RAD avec Xamarin.Forms si incroyable.

...J'ai décidé que les pages peuvent vivre seules, ou qu'elles peuvent avoir des Coordinateurs attachés. Il m'a fallu un certain temps pour arriver à cette décision. J'ai en fait commencé par une approche de conception Coordinator-first, où tout était piloté par un Coordinateur. J'ai rapidement trouvé que cela était terriblement limitant et super compliqué. Cela nécessitait un gestionnaire de navigation pseudo-push/pop complexe, et cela limitait ma capacité à utiliser facilement TabbedPages, MasterDetailPages, et modals. J'ai également trouvé que je poussais la logique de navigation dans les View Models. Je n'aimais pas cela.

J'ai donc opté pour une approche Page-first, où les Pages peuvent avoir un Coordinateur attaché. Cela résout un gros problème lié à la [collecte des déchets](https://docs.microsoft.com/en-us/dotnet/standard/garbage-collection/fundamentals), puisque le framework Xamarin.Forms gère déjà la rétention et la suppression des Pages en fonction des cycles de vie de visibilité. Si j'avais adopté l'approche Coordinator-first, j'aurais dû ajouter une série de logiques laides pour gérer la pile moi-même.

Avec l'approche Page-first, vous pouvez créer une Page comme vous le faites normalement, et vous pouvez passer (attacher) un coordinateur via le constructeur de la page. Donc pour la page de connexion, cela ressemble à ceci :

Le point positif de cette approche est que je peux également injecter un Coordinateur en XAML. Cela est particulièrement utile dans les situations de MasterDetailPage ou TabbedPage, où vous ne créez normalement pas les instances en code. Comme :

Avant d'entrer dans les mécanismes, examinons l'implémentation de LoginCoordinator. Plus précisément, nous nous concentrerons sur les responsabilités que ce coordinateur prend en charge, qui sont toutes encapsulées dans la méthode Start() du Coordinateur. C'est là que toute la magie — la logique de navigation — se produit.

Avant d'aller plus loin, permettez-moi d'expliquer brièvement une partie de la [logique métier](https://en.wikipedia.org/wiki/Business_logic) de l'application. Dans cette application (conçue pour les musiciens), chaque utilisateur peut appartenir à un ou plusieurs groupes. Ainsi, après l'authentification (connexion), l'utilisateur se voit présenter une liste de ses groupes. L'utilisateur en sélectionne un, et l'application complète alors le flux de travail de connexion, et affiche la page principale de détails post-connexion.

Ainsi, ce LoginCoordinator orchestrerait en fait la présentation de deux pages distinctes — la LoginPage et la BandPickerPage. Chacune des pages peut être utilisée indépendamment ou dans le cadre d'autres flux de travail.

Par exemple, la page BandPicker est utilisée dans une autre partie de l'application lorsque l'utilisateur souhaite basculer entre ses groupes actifs, sans avoir à se reconnecter. La page BandPicker ignore complètement comment elle est utilisée. Elle doit simplement se concentrer sur ce qu'elle fait — choisir des groupes.

### Le Framework

L'implémentation du Coordinateur lui-même est assez facile. Dans mon approche, il y a une interface (appelée ICoordinator) et une classe de base abstraite qui implémente partiellement cette interface. L'interface ressemble à ceci :

Chaque coordinateur doit uniquement implémenter la méthode Start(). Les deux autres méthodes — AttachToPage() et DetachFromPage() — sont implémentées dans la classe de base abstraite. Voici à quoi cela ressemble :

Les coordinateurs de l'application doivent simplement étendre cette classe de base et remplacer la méthode Start(). C'est à peu près tout. Il n'y a qu'une autre pièce dans le **framework**, qui est une simple classe de base pour les sous-classes de ContentPage. Elle ne fait rien de plus que d'appeler les méthodes AttachToPage() et DetachFromPage() des Coordinateurs passés dans le constructeur. C'est tout.

### Résumé

Un grand merci à Soroush Khanlou pour l'inspiration. J'adorerais entendre comment vous utilisez les Coordinateurs dans vos propres projets Xamarin, et toute idée que vous pourriez avoir pour améliorer l'implémentation que j'ai présentée ici.

Vous pouvez [télécharger mon exemple](https://github.com/raf66/CoordinatorExampleApp) d'application depuis GitHub.