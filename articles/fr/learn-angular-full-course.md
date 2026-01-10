---
title: Apprendre Angular - Cours accéléré
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-10-20T21:07:05.000Z'
originalURL: https://freecodecamp.org/news/learn-angular-full-course
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/angular.png
tags:
- name: Angular
  slug: angular
- name: youtube
  slug: youtube
seo_title: Apprendre Angular - Cours accéléré
seo_desc: 'Angular is a TypeScript-based free and open-source web application framework
  created by Google.

  We just published a 2-hour Angular crash course on the freeCodeCamp.org YouTube
  channel.

  Slobodan Gajic created this course. Slobodan has created a bunch ...'
---

Angular est un framework d'application web gratuit et open-source basé sur TypeScript, créé par Google.

Nous venons de publier un cours accéléré Angular de 2 heures sur la chaîne YouTube de freeCodeCamp.org.

Slobodan Gajic a créé ce cours. Slobodan a créé de nombreux cours incroyables sur sa propre chaîne.

Dans ce cours, vous apprendrez à utiliser toutes les parties principales d'Angular en utilisant TypeScript. À la fin, vous serez prêt à construire vos propres projets avec Angular.

Voici les sections couvertes dans ce cours :

* Composants (Components)
* Hooks de cycle de vie (Lifecycle hooks)
* Interpolation de texte
* Communication entre composants
* Styles de composants
* Ng-Content
* Instructions de template (Template Statements)
* Pipes
* Liaison de propriété (Property Binding)
* Attributs, Classes et Styles
* Liaison d'événement (Event Binding)
* Liaison bidirectionnelle (Two-way Binding)
* Directives
* Directives d'attribut
* Directives structurelles
* Injection de dépendances (Dependency Injection)
* Routage (Routing)
* Formulaires basés sur les templates (Template-Driven Forms)
* Formulaires réactifs (Reactive Forms)
* Validation de formulaire
* Client HTTP

Regardez le cours complet ci-dessous ou sur la chaîne YouTube de freeCodeCamp.org (durée de 2 heures).

%[https://youtu.be/AAu8bjj6-UI]

## Transcription

(générée automatiquement)

Ceci est un cours Angular incroyable pour débutants, Slobodan est un développeur très expérimenté.

Et il enseigne les bases d'Angular en utilisant des diagrammes, des animations et, bien sûr, du code.

Aujourd'hui, je commence une nouvelle série de vidéos sur le framework Angular.

Et dans cette série, vous apprendrez tout ce dont vous avez besoin pour maîtriser le framework Angular.

Je commencerai par des choses basiques comme les composants et les pipes, et je progresserai lentement vers les fonctionnalités les plus complexes de ce framework.

Alors, commençons.

Dans cette section, je vais expliquer ce qu'est Angular, donner un bref aperçu de ses fonctionnalités et expliquer pourquoi vous devriez l'utiliser.

Mais avant de commencer, n'oubliez pas de consulter ma chaîne pour plus de vidéos et de tutoriels sur le développement front-end.

Maintenant, commençons.

Angular est un framework UI tranché (opinionated) pour la création d'applications mobiles et de bureau.

Et il est construit avec TypeScript par Google.

Vous en avez probablement déjà entendu parler.

De plus, il est open source et nous aide à construire des applications dynamiques et à page unique (Single Page Applications).

Il est entièrement basé sur des composants.

Il se compose de plusieurs composants, qui forment une structure en arbre avec des composants parents et enfants.

Les versions d'Angular au-delà de la version 2 sont généralement connues sous le nom d'Angular uniquement.

La toute première version d'Angular est connue sous le nom d'AngularJS.

Alors pourquoi Angular ? Eh bien, parce qu'il est supporté sur diverses plateformes (web, mobile, bureau natif), il est puissant, moderne et possède un bel écosystème.

Et c'est tout simplement génial. Laissez-moi vous donner quelques faits.

Angular vous présente non seulement les outils, mais aussi les patrons de conception (design patterns) pour construire votre projet de manière maintenable.

Lorsqu'une application Angular est conçue correctement, vous ne vous retrouvez pas avec un enchevêtrement de classes et de méthodes difficiles à modifier, et encore plus difficiles à tester.

Le code est structuré de manière pratique, et vous n'aurez pas besoin de passer beaucoup de temps pour comprendre ce qui se passe.

C'est du JavaScript, mais en mieux.

Angular est construit avec TypeScript, qui s'appuie à son tour sur ES6+.

Vous n'avez pas besoin d'apprendre un langage totalement nouveau, mais vous bénéficiez tout de même de fonctionnalités telles que le typage statique, les interfaces, les classes, les espaces de noms, les décorateurs, etc.

Pas besoin de réinventer la roue.

Avec Angular, vous avez déjà beaucoup d'outils pour commencer à concevoir une application immédiatement.

Vous avez des directives pour donner aux éléments HTML un comportement dynamique, vous pouvez dynamiser les formulaires en utilisant le contrôle de formulaire et introduire diverses règles de validation.

Vous pouvez facilement envoyer des requêtes HTTP asynchrones de divers types, vous pouvez configurer le routage avec peu de tracas, et il y a bien d'autres avantages qu'Angular peut nous offrir.

Les composants sont découplés, Angular s'efforce de supprimer le couplage étroit entre les divers composants de l'application.

L'injection se fait de manière propre, et vous pouvez remplacer divers composants facilement.

Toute la manipulation du DOM se produit là où elle doit se produire.

Avec Angular, vous ne couplez pas étroitement la présentation et la logique d'application, ce qui rend votre balisage beaucoup plus propre et simple.

Le test est au cœur du système.

Angular est conçu pour être testé de manière approfondie, et il supporte à la fois les tests unitaires et les tests de bout en bout (end-to-end).

Angular est prêt pour le mobile et le bureau, ce qui signifie que vous avez un seul framework pour plusieurs plateformes.

Angular est activement maintenu et possède une grande communauté et un vaste écosystème.

Vous pouvez trouver beaucoup de documentation sur ce framework, ainsi que de nombreux outils tiers utiles.

Le diagramme d'architecture identifie les huit principaux blocs de construction d'une application Angular.

Les applications Angular sont modulaires, et Angular possède son propre système de modularité, appelé modules Angular, ou NgModules.

Chaque application Angular possède au moins une classe de module Angular, le module racine, commodément nommé AppModule.

Bien que le module racine puisse être le seul module dans une petite application, la plupart des applications ont beaucoup plus de modules de fonctionnalités.

Chacun est un bloc de code cohérent dédié à un domaine d'application, ou à un flux de travail, ou à un ensemble de capacités étroitement liées.

Un module Angular, qu'il soit racine ou de fonctionnalité, est une classe avec un décorateur `@NgModule`.

Les templates Angular sont dynamiques.

Lorsqu'Angular les affiche, il transforme le DOM selon les instructions données par les directives.

Les métadonnées indiquent à Angular comment traiter une classe.

Le Service est une catégorie large englobant toute valeur, fonction ou fonctionnalité dont votre application a besoin.

Presque tout peut être un service.

Un service est typiquement une classe avec un but étroit et bien défini.

Il doit faire quelque chose de spécifique et le faire bien.

Les exemples incluent un service de journalisation (logging), un service de données, un bus de messages, un calculateur de taxes, la configuration de l'application.

Il n'y a rien de spécifiquement Angular concernant les services.

Angular n'a pas de définition propre d'un service.

Il n'y a pas de classe de base de service et aucun endroit pour enregistrer un service.

Pourtant, les services sont fondamentaux pour toute application Angular.

Les composants sont de grands consommateurs de services.

Maintenant, parlons plus en détail des composants.

Les composants sont le principal bloc de construction d'une application Angular.

Chaque composant se compose d'un template HTML qui déclare ce qui s'affiche sur la page, d'une classe TypeScript qui définit le comportement, d'un sélecteur CSS qui définit comment le composant est utilisé dans notre template, et optionnellement, de styles CSS appliqués au composant.

Un composant doit appartenir à un NgModule pour qu'il soit disponible pour un autre composant.

Pourquoi utilisons-nous des composants ? Il y a de nombreuses raisons, mais les principales sont : la possibilité de réutiliser notre code pour ne pas dupliquer, la simplification de l'architecture basée sur les composants, la facilité de gestion des erreurs et la décomposition de la complexité en plus petits morceaux.

Les prérequis pour ces sections sont l'installation de l'Angular CLI et la création d'un espace de travail Angular avec l'application initiale.

Si vous n'avez pas de projet, vous pouvez en créer un en utilisant `ng new nom-du-projet`, où `nom-du-projet` est le nom de votre application.

Bien que l'Angular CLI soit le moyen le plus simple de créer un composant Angular, dans ce tutoriel, nous allons créer notre composant manuellement.

Pour créer un nouveau composant :

Naviguez vers le répertoire de votre projet Angular.

Créez un nouveau fichier `hello-world.component.ts`.

En haut du fichier, ajoutez l'instruction d'importation suivante.

Après l'instruction d'importation, ajoutez un décorateur `@Component`. Le décorateur marque une classe comme un composant Angular et fournit des métadonnées qui décident comment le composant est utilisé au moment de l'exécution.

Choisissez un sélecteur CSS pour le composant.

C'est une balise que vous utiliserez dans vos fichiers de template pour afficher votre composant. Définissez le template HTML que le composant utilise pour afficher les informations.

Dans la plupart des cas, ce template est un fichier HTML séparé, mais je l'utiliserai à l'intérieur de ce fichier.

Pour définir un template comme fichier externe :

Ajoutez une propriété `templateUrl` au décorateur du composant.

Pour un template dans le même fichier, utilisez la propriété `template`.

Sélectionnez les styles pour le template du composant.

Dans la plupart des cas, vous définirez les styles pour le template d'un composant dans un fichier séparé.

Encore une fois, je l'utiliserai dans le fichier. Pour déclarer les styles d'un composant dans un fichier séparé, utilisez la propriété `styleUrls` dans le décorateur `@Component`.

Mais pour les styles à l'intérieur du composant, ajoutez la propriété `styles`. Ajoutez une instruction de classe qui inclut le code du composant.

Ici, nous pouvons définir des propriétés, des méthodes, capturer les événements du cycle de vie du composant et faire de l'injection de dépendances.

Mais j'en parlerai davantage dans la prochaine vidéo.

Maintenant, toutes les propriétés publiques définies dans la classe sont accessibles dans le template HTML.

Et c'est l'une des choses les plus puissantes ici. Je vais créer une propriété `title`, et je l'inclurai dans le HTML.

Importez ce nouveau fichier dans le module où vous souhaitez l'utiliser. Pour le rendre disponible pour toute l'application, importez-le dans le module racine.

Afin de voir notre composant, nous pouvons utiliser notre sélecteur CSS à l'intérieur de notre `app.component` ou de tout autre composant.

Et voilà votre premier composant.

Très simple, mais vous pouvez le réutiliser partout.

Dans cette section, nous parlons des hooks de cycle de vie (lifecycle hooks).

Ce sont des fonctionnalités spéciales dans Angular qui nous permettent de nous brancher et d'exécuter du code.

Et un événement spécifique du cycle de vie d'un composant ou d'une directive peut être vu comme les étapes de la vie d'un composant.

Comme tout être vivant, ils naissent, ils changent, ils grandissent et finalement ils meurent.

Avec les hooks de cycle de vie, vous pouvez obtenir un meilleur contrôle de votre application au moment où vous souhaitez les utiliser.

Par exemple, si vous voulez récupérer des données dans cette page de votre composant, vous le ferez à l'intérieur du cycle de vie `ngOnInit` lorsqu'un composant est initialisé, ou si vous avez besoin de nettoyer votre composant, de supprimer certaines souscriptions que vous pourriez avoir pour éviter les fuites de mémoire, vous le ferez à l'intérieur du cycle de vie `ngOnDestroy` juste avant que le composant ne soit détruit.

Voici la liste de tous les hooks dans l'ordre exact de leur initialisation, mais les plus utilisés sont `onInit`, `onChanges` et `onDestroy`.

Implémentons le hook `ngOnInit`.

Nous utiliserons ce hook le plus souvent. D'abord, importez une interface depuis Angular Core.

Ensuite, nous voulons implémenter cette interface à l'intérieur de notre classe.

Pour implémenter n'importe quel hook, il vous suffit d'ajouter un `ng` au nom de l'interface, et vous obtiendrez la méthode nécessaire à l'implémentation.

Dans ce cas, c'est `ngOnInit`. Nous allons créer une fonction simple pour enregistrer des valeurs dans la console.

Maintenant, je vais créer une propriété qui sauvegardera cette fonction afin que nous puissions la nettoyer à la fin.

Dans la méthode `ngOnInit`, créons une méthode `setInterval` simple qui fera un `console.log` chaque seconde.

Si vous laissez notre composant ainsi, quand le composant sera détruit, notre méthode d'intervalle continuera à écrire dans la console.

Pour corriger cet effet secondaire, nous devons utiliser le hook `ngOnDestroy`.

Importez l'interface `OnDestroy` et placez-la après `OnInit`.

Maintenant, créez la méthode `ngOnDestroy` et dans cette méthode, vous devez nettoyer cet intervalle.

Utilisez simplement une méthode `clearInterval` avec notre propriété passée en argument.

Et maintenant, notre composant a été nettoyé.

En utilisant les hooks de cycle de vie, nous allons affiner le comportement de nos composants lors de la création, de la mise à jour et de la destruction.

Ensuite, l'interpolation de texte.

L'interpolation de texte dans Angular est une technique de liaison de données unidirectionnelle utilisée pour transférer des données d'un code TypeScript vers un template HTML.

Elle utilise l'expression de template entre doubles accolades, également connue sous le nom de syntaxe moustache, pour afficher les données du composant vers la vue.

Quand avons-nous besoin de l'interpolation de texte ? Chaque fois que nous voulons rendre quelque chose de dynamique dans notre template HTML.

Pour illustrer le fonctionnement de l'interpolation, créons une nouvelle variable dans notre classe Ts.

Vous pouvez utiliser l'interpolation pour afficher la valeur de cette variable dans le template de composant correspondant.

Angular remplace `title` par la valeur de chaîne de la propriété de composant correspondante.

Dans ce cas, la valeur est "hello world".

Maintenant, parlons des expressions de template.

Une expression de template produit une valeur et apparaît entre doubles accolades.

Laissez-moi vous montrer un exemple.

Angular résout l'expression et l'assigne à une propriété d'une cible de liaison.

Les expressions de template sont similaires au JavaScript, sauf que vous ne pouvez pas utiliser d'assignations.

De plus, les opérateurs tels que `new`, `typeof` ou `instanceof` ne sont pas autorisés.

Vous ne pouvez pas utiliser d'expressions de chaînage, d'opérateurs de décrémentation ou d'incrémentation et certains des opérateurs ES2015+.

Les expressions peuvent également invoquer des méthodes.

Alors créons-en une, le nom de notre méthode sera `getName`.

Et dans cette méthode, nous retournons une valeur pour l'afficher dans notre template.

Dans ce cas, ce sera une valeur minimale.

Quelques points que je souhaite mentionner : vous devriez garder la logique d'application dans le composant autant que possible, là où il est plus facile de développer et de tester.

De plus, les expressions doivent se terminer rapidement pour garder l'expérience utilisateur aussi efficace que possible, surtout sur les appareils plus lents.

Et l'expression de template ne doit changer aucun état de l'application autre que la valeur de la propriété cible.

La lecture d'une valeur de composant ne doit pas modifier d'autres valeurs affichées.

Maintenant, apprenons à communiquer entre les composants.

Une application Angular se compose généralement de nombreux composants séparés.

Et pour les faire fonctionner ensemble, nous avons besoin de communication entre eux.

Vous pouvez considérer les composants comme les membres d'une famille.

Et si la communication entre les parents et les enfants est fluide et efficace, votre maison sera un endroit heureux.

Il existe quatre façons de communiquer entre les composants Angular : la liaison (binding) en utilisant `@Input` et `@Output`, la référence en utilisant `@ViewChild` et `@ContentChild`, l'utilisation de services et les templates.

Dans ce tutoriel, je vais couvrir les deux premières méthodes car nous n'avons pas encore abordé les services.

Le premier cas d'utilisation est lorsque nous voulons envoyer des données du parent vers l'enfant en utilisant le décorateur `@Input`.

Le décorateur `@Input` prend la valeur passée par le parent et stocke cette valeur dans la propriété de l'enfant.

Laissez-moi créer deux composants en utilisant l'Angular CLI.

Je vais exécuter les commandes suivantes : `ng generate component parent` et `ng generate component child`.

Dans notre composant enfant, je vais importer le décorateur `Input`.

Je nomme mon entrée `childMessage` de type `string`. Dans un template du même composant, j'afficherai cette propriété qui va être passée depuis un parent.

Maintenant, à l'intérieur de notre composant parent dans le template, nous voulons placer notre composant enfant et passer la valeur à la propriété d'entrée que nous venons de créer.

Le nom de la propriété est celui que nous avons défini dans le composant enfant, et la valeur sera un message "Hello".

Ensuite, nous voulons placer notre composant parent à l'intérieur de notre composant racine.

Et si nous le prévisualisons, nous pouvons voir que le message du parent a été affiché dans notre composant enfant.

Le deuxième cas d'utilisation est lorsque nous voulons envoyer des données de l'enfant vers le parent en utilisant le décorateur `@Output`.

Le décorateur `@Output` marque une propriété dans un composant enfant comme une porte par laquelle les données peuvent voyager de l'enfant vers le parent.

Cette approche est idéale lorsque vous souhaitez partager des données lors d'événements tels que des clics sur des boutons, des saisies de formulaires et d'autres événements utilisateur.

Pour lever un événement, un `@Output` doit avoir le type `EventEmitter`, qui est une classe dans Angular Core utilisée pour émettre des événements personnalisés.

Dans le composant enfant, importez les décorateurs `Input`, `Output` et `EventEmitter`.

Nous déclarons une variable `messageEvent` avec le décorateur `@Output` et nous l'initialisons à un nouvel `EventEmitter`.

Ensuite, nous créons une fonction nommée `sendMessage` qui appelle une méthode sur cet événement avec le message que nous voulons envoyer.

Enfin, nous créons un bouton pour déclencher cette fonction.

Dans le parent, je vais créer une fonction pour recevoir le message et je vais simplement afficher ce message dans une alerte à des fins de démonstration.

Maintenant, dans le template parent, appelez notre fonction une fois que l'événement du composant enfant se produit.

Et le nom de cet événement est celui que nous avons défini avec le décorateur `@Output`.

Très simple et efficace.

Comparée à toutes les autres approches de communication, la liaison (binding) est la plus propre et la plus simple, c'est la manière la plus maintenable de passer des données, car la liaison est toujours la méthode préférable que les développeurs Angular devraient considérer en premier.

Le troisième cas d'utilisation est lorsque nous voulons envoyer des données de l'enfant vers le parent en utilisant `@ViewChild`. `@ViewChild` permet au composant enfant d'être injecté dans un composant parent.

Cela donnera au parent l'accès à ses propriétés et fonctions.

L'enfant ne sera pas disponible pour donner accès tant que la vue n'aura pas été initialisée.

Cela signifie que nous devons implémenter le hook de cycle de vie `AfterViewInit` pour recevoir les données de l'enfant.

D'abord, créez une propriété `message` dans notre composant enfant.

Importez `ViewChild` et `AfterViewInit` depuis Angular Core dans notre composant parent.

Pour notre décorateur `@ViewChild`, passez notre composant enfant comme argument et nommez-le `child`.

Ensuite, implémentez le hook de cycle de vie `AfterViewInit`.

Au fait, pour en savoir plus sur les hooks Angular, consultez la partie deux de cette série de vidéos. À l'intérieur de la méthode `ngAfterViewInit`, affichez simplement la propriété `message` de notre enfant pour voir que nous y avons accès.

Et si nous lançons notre application, vous pouvez voir que nous affichons un message provenant du composant enfant.

Ensuite, nous discutons des styles de composants.

Être capable de styliser votre application est très important car cela vous permet de rendre votre application unique et attrayante.

D'une certaine manière, c'est comme un salon de beauté.

Un monde sans CSS serait un endroit laid.

Le CSS nous donne l'opportunité de jouer avec la mise en page, d'ajuster les couleurs et les polices, d'ajouter des effets, des images, et ainsi de suite. Comment ajouter des styles aux composants Angular ?

Il y a trois façons d'appliquer un style : en définissant les métadonnées `styles` ou `styleUrls`, en ligne dans le template HTML, et avec des importations CSS.

J'ai créé un composant vide avec seulement une balise `h2` dans la vue pour démontrer toutes les différentes façons de le styliser.

Vous pouvez ajouter une propriété de tableau `styles` au décorateur du composant, chaque chaîne dans le tableau définit du CSS pour ce composant. Vous pouvez charger des styles à partir de fichiers CSS externes en ajoutant une propriété `styleUrls` au décorateur d'un composant.

Et maintenant, les styles du fichier externe sont appliqués.

Ensuite, vous pouvez intégrer des styles CSS directement dans le template HTML en les plaçant à l'intérieur de balises `<style>`.

Vous pouvez également écrire des balises `<link>` dans le template HTML du composant.

Une note ici : assurez-vous d'inclure le fichier de styles lié parmi les ressources (assets) à copier sur le serveur lors de la construction (build).

Vous pouvez également importer des fichiers CSS dans les fichiers CSS en utilisant la règle standard `@import` du CSS.

J'utilise généralement cette approche pour importer des variables.

Rappel : ces styles s'appliquent uniquement à ce composant.

Ainsi, si vous aviez une balise `h1` dans un composant enfant ou parent, ils n'y seraient pas appliqués.

Par défaut, l'encapsulation de la vue est définie sur `Emulated`, ce qui émule le comportement du Shadow DOM en pré-traitant et en renommant le code CSS pour limiter efficacement la portée du CSS à la vue du composant.

Nous pouvons supprimer ces sélecteurs CSS supplémentaires en définissant `encapsulation` sur `None`.

Et maintenant, nos styles sont appliqués globalement.

Les styles globaux sont par défaut définis dans le fichier `styles.css`, et vous pouvez trouver plus de styles globaux dans le fichier `angular.json`.

Une autre chose est que si vous construisez avec le CLI, vous pouvez écrire des fichiers de style en Sass, Less ou Stylus, et spécifier ces fichiers dans les métadonnées `styleUrls` du composant avec l'extension appropriée comme dans l'exemple suivant.

Maintenant, parlons des sélecteurs spéciaux.

Utilisez le sélecteur de pseudo-classe `:host` pour cibler les styles dans l'élément qui héberge le composant (par opposition au ciblage des éléments à l'intérieur du template du composant).

Par exemple, nous pouvons écrire le code suivant.

Nous pouvons styliser l'hôte avec un sélecteur donné en utilisant la forme fonctionnelle comme suit.

Et si vous ajoutez la classe `active` au composant hôte, vous pouvez voir que les styles sont appliqués.

Maintenant, parlons de `:host-context`.

Parfois, il est utile d'appliquer des styles basés sur une condition à l'extérieur de la vue du composant.

Par exemple, une classe de thème CSS peut être appliquée à l'élément `body` du document.

Et vous voulez changer l'apparence de votre composant en fonction de cela.

L'exemple suivant applique un style de couleur d'arrière-plan à tous les éléments `h2` à l'intérieur du composant uniquement si un élément ancêtre a la classe CSS `theme-light`.

Maintenant, si vous allez à l'élément racine et ajoutez la classe `theme-light`, vous pouvez voir ces styles.

Et c'est tout.

Maintenant, voyons ce qu'est `ng-content`.

`ng-content` utilise la projection de contenu pour prendre le HTML d'un autre composant et l'afficher à l'intérieur de lui-même.

Pour moi, c'est semblable à un projecteur de film, où vous avez une fente pour insérer votre contenu, qui va être affiché sur l'écran.

C'est un outil très puissant lorsque vous construisez des composants destinés à être réutilisés.

Je le vois utilisé de manière extensive dans des frameworks tels qu'Angular Material.

Quand voulez-vous utiliser `ng-content` ? Chaque fois que vous voulez injecter n'importe quel type de HTML dans un composant, vous pouvez le faire avec `ng-content`.

J'ai deux composants, `child` et `root`, pour démontrer cette fonctionnalité. À l'intérieur du composant enfant, je vais créer du contenu statique.

Je vais donc ajouter un titre `h2`.

Et en dessous de ce titre, je veux montrer ce contenu dynamique.

Je vais donc créer une balise `<ng-content>`.

Avec l'élément `ng-content` en place, les utilisateurs de ce composant peuvent maintenant projeter leur propre message dans le composant.

Pour ce faire, laissez-moi insérer un enfant à l'intérieur de notre composant racine et je passerai un paragraphe avec un message.

Comme vous pouvez le voir, l'élément `ng-content` est un espace réservé (placeholder) qui ne crée pas de véritable élément DOM.

Maintenant, un composant peut avoir plusieurs fentes (slots).

Chaque fente peut spécifier un sélecteur CSS qui détermine quel contenu va dans cette fente.

Ce modèle est appelé projection de contenu multi-fentes.

Vous pouvez accomplir cette tâche en utilisant l'attribut `select` de `ng-content`. À l'intérieur de notre composant enfant, ajoutons une autre balise `ng-content`. Nous pouvons faire en sorte que notre composant ressemble à une carte de questions-réponses.

Ainsi, dans le premier `ng-content`, ajoutez le sélecteur `question` et mettez un second `ng-content` avec le sélecteur `answer`.

Maintenant, nous pouvons utiliser les sélecteurs pour envoyer différents contenus.

Dans notre composant racine, je vais créer un titre avec le sélecteur `question`, et je taperai ce texte de question.

En dessous, je créerai un paragraphe avec un sélecteur `answer`, et je taperai un texte de réponse.

De plus, il existe d'autres moyens de créer une projection de contenu multi-fentes, mais nous n'avons pas encore abordé les conditionnels.

Comme vous pouvez le voir, il est vraiment facile de créer des composants dynamiques réutilisables.

Cette approche peut être utilisée pour des interfaces utilisateur beaucoup plus complexes.

Mais je vous ai montré cet exemple simple pour comprendre le concept.

Ensuite, discutons des instructions de template (template statements).

Une instruction de template est quelque chose qui répond à un événement déclenché par une cible comme un élément, un composant ou une directive.

C'est donc la même chose que si quelqu'un vous appelle (ce qui est un événement) et que vous répondez à cet appel téléphonique (ce qui est la réponse et, dans notre exemple, l'instruction de template).

Elle produit des effets secondaires car elle modifie les champs dans le composant.

Maintenant, je vais vous montrer comment mettre à jour les propriétés de classe en utilisant une instruction de template.

J'ai un composant vide et dans notre template, je vais créer une propriété booléenne nommée `showText` avec une valeur `false`.

En dessous, je vais créer une méthode nommée `toggleText`, elle ne va rien retourner pour le moment.

Tout ce que nous allons faire ici est de basculer notre valeur `showText` à chaque appel de méthode.

Habituellement, nous utiliserions ce genre de propriété pour basculer l'état dans la vue, mais nous n'avons pas encore abordé les conditionnels.

Donc, dans le template, je vais créer un bouton qui répondra à un événement de clic et il appellera cette méthode `toggleText`.

En dessous, j'afficherai l'état de la propriété `showText`.

Et maintenant, quand je clique sur le bouton, vous pouvez voir qu'il bascule sa valeur en utilisant l'instruction de template.

Et dans cet exemple, `toggleText` est l'instruction de template.

Ce contexte d'instruction peut également se référer aux propriétés du propre contexte du template.

Dans l'exemple suivant, `toggleText` prend l'objet d'événement du template comme argument.

Si vous enregistrez cet objet, vous pouvez voir qu'il contient diverses informations sur une cible et l'événement qui s'est produit.

Passer des arguments peut être très utile lorsque vous soumettez des formulaires ou que vous parcourez des tableaux, et que vous avez besoin d'accéder à un élément spécifique.

Une note ici : le contexte d'une instruction de template peut être l'instance de la classe du composant ou le template lui-même.

À cause de cela, les instructions de template ne peuvent se référer à rien dans l'espace de noms global, comme `window` ou `document`.

Par exemple, une instruction de template ne peut pas appeler `console.log` ou `Math.max` directement.

Pipes.

Les pipes sont simplement des fonctions que vous pouvez utiliser dans vos templates pour accepter n'importe quelle valeur d'entrée et retourner une valeur formatée.

Dans ce cas, vous pouvez voir vos données comme de l'argile brute, prête à être moulée.

Au début, ce n'est pas très joli ou clair à quoi cela sert.

Mais avec un peu de travail et de moulage, vous pouvez obtenir le résultat final que vous souhaitez.

Angular fournit des pipes intégrés pour les transformations de données typiques comme `DatePipe`, `UpperCasePipe`, `CurrencyPipe`, `PercentPipe`, et d'autres similaires.

Dans mon `app.component`, je vais définir une propriété avec une valeur `new Date()`.

Si nous affichons simplement notre objet date dans notre template, vous pouvez voir quel genre de format nous obtenons.

Ce n'est pas très convivial pour l'utilisateur.

Maintenant, rendons-le plus joli.

Pour appliquer un pipe, utilisez l'opérateur pipe (`|`) à l'intérieur d'une expression de template avec le nom du pipe, qui est `date` pour le pipe de date intégré. Maintenant, c'est beaucoup plus lisible.

Une note ici : le `DatePipe` n'est exécuté que lorsqu'il détecte un changement pur de la valeur d'entrée.

Un changement pur est soit un changement d'une valeur d'entrée primitive (chaîne, nombre, booléen ou symbole), soit un changement de référence d'objet (Date, Array, Function ou Object).

Si vous n'aimez toujours pas le format de sortie de vos données, vous pouvez l'affiner en utilisant des paramètres optionnels.

Il existe des options prédéfinies comme `short` ou `long`, ou vous pouvez le personnaliser complètement.

Par exemple, quatre `E` pour le jour de la semaine, quatre `M` pour le mois, un `d` minuscule pour le jour du mois et un `y` minuscule pour l'année.

Vous pouvez également enchaîner plusieurs pipes, il vous suffit d'ajouter un autre opérateur pipe et un nom de pipe.

Maintenant, nous pouvons aussi créer des pipes personnalisés.

Créons un pipe de salutation simple qui concaténera "Hello" au nom passé.

J'utiliserai l'Angular CLI pour générer ce fichier pour moi.

Tapez `ng generate pipe` et le nom est `greetings`.

Dans notre pipe, nous avons du code standard généré.

Vous pouvez voir que le décorateur `@Pipe` a été importé avec une propriété `name`, que nous pouvons utiliser pour appeler notre pipe dans nos templates.

De plus, il y a une interface `PipeTransform` qui doit être implémentée.

Cette interface nécessite que la méthode `transform` soit implémentée.

Et cette méthode reçoit une valeur passée depuis un template.

Dans notre cas, ce sera une chaîne de caractères.

Et le second paramètre est pour les paramètres optionnels du pipe lui-même.

Le type de retour dans notre cas va être une chaîne de caractères.

Maintenant, tout ce que nous allons faire ici est de concaténer "Hello " à la chaîne passée et de la retourner.

Maintenant, dans notre template, nous pouvons appeler notre pipe personnalisé avec le nom `greetings` que nous avons défini, et je passerai "world" comme chaîne.

Voilà comment vous créez des pipes personnalisés.

Les pipes Angular sont des fonctionnalités très simples mais utiles fournies par Angular, et vous les utiliserez beaucoup.

Encore une fois, pour une liste détaillée de tous les pipes, consultez le lien de la documentation dans la description.

Maintenant, discutons de la liaison de propriété (property binding).

La liaison de propriété déplace une valeur dans une seule direction.

C'est donc une rue à sens unique.

Elle va de la propriété de la classe vers la propriété de l'élément cible.

La liaison de propriété dans Angular vous aide à définir des valeurs pour les propriétés des éléments HTML ou des directives.

Avec la liaison de propriété, vous pouvez faire des choses comme basculer la fonctionnalité d'un bouton, définir des chemins de manière programmatique et partager des valeurs entre les composants.

Pour lier la propriété `src` d'un élément image à une propriété de composant, placez la cible `src` entre crochets, suivie d'un signe égal, puis de la propriété.

La propriété ici est `itemImageUrl`.

Déclarez la propriété `itemImageUrl` dans la classe, dans ce cas, `app.component`.

Un point de confusion courant est entre l'attribut `colspan` et la propriété `colSpan`.

Remarquez que ces deux noms ne diffèrent que par une seule lettre.

Si vous écriviez quelque chose comme ça, vous obtiendriez une erreur d'analyse de template car l'interpolation et la liaison de propriété ne peuvent définir que des propriétés, pas des attributs.

Au lieu de cela, vous utiliseriez la liaison de propriété et l'écririez ainsi.

Un autre exemple est la désactivation d'un bouton lorsque le composant indique qu'il est inchangé.

Pour désactiver la fonctionnalité en fonction d'une valeur booléenne, liez la propriété `disabled` à une propriété dans la classe qui est `true` ou `false`.

Parce que la valeur de la propriété `isUnchanged` est `true` dans le `app.component`, Angular désactive le bouton.

Souvent, l'interpolation et la liaison de propriété peuvent obtenir le même résultat.

Les paires de liaisons suivantes font la même chose.

Une note : l'évaluation d'une expression de template ne doit avoir aucun effet secondaire visible.

Vous ne devriez rien assigner dans l'expression de template ou utiliser des opérateurs d'incrémentation ou de décrémentation.

Si vous aviez une expression qui changeait la valeur de quelque chose d'autre que vous liiez, le changement de valeur serait un effet secondaire.

Maintenant, voyons nos liaisons d'attribut, de classe et de style.

En utilisant ces liaisons, vous pouvez améliorer l'accessibilité, styliser dynamiquement votre application et mettre à jour les classes à la volée.

D'abord, parlons de la liaison d'attribut.

La liaison d'attribut dans Angular vous aide à définir des valeurs d'attributs directement.

Il est recommandé de définir une propriété d'élément avec une liaison de propriété chaque fois que cela est possible.

Cependant, parfois vous n'avez pas de propriété d'élément à lier.

Dans ces situations, vous pouvez utiliser la liaison d'attribut. La syntaxe de liaison d'attribut ressemble à la liaison de propriété, mais au lieu d'une propriété d'élément entre crochets, vous faites précéder le nom de l'attribut du préfixe `attr` suivi d'un point.

Ensuite, vous définissez la valeur de l'attribut avec une expression qui se résout en une chaîne.

Un autre cas d'utilisation courant pour la liaison d'attribut est avec l'attribut `colspan` dans les tableaux.

Lier l'attribut `colspan` vous aide à garder vos tableaux dynamiques de manière programmatique.

Selon la quantité de données que votre application insère dans un tableau, le nombre de colonnes ou l'étendue des lignes (row span) pourrait changer.

Pour utiliser la liaison d'attribut avec l'attribut `<td> colspan`, spécifiez l'attribut `colspan` en utilisant cette syntaxe : définissez `[attr.colspan]` égal à une expression.

Dans cet exemple, nous lions l'attribut `colspan` à l'expression `1 + 1`.

Cette liaison fait en sorte que la ligne du tableau s'étende sur deux colonnes.

Parfois, il y a des différences entre le nom de la propriété et celui de l'attribut.

`colspan` est un attribut de ligne de tableau, tandis que `colSpan` avec un S majuscule est une propriété. Lors de l'utilisation de la liaison d'attribut, utilisez `colspan` avec un s minuscule.

Pour plus d'informations sur la façon de se lier à la propriété `colSpan`, consultez la vidéo sur la liaison de propriété.

Passons maintenant à la liaison de classe.

Vous pouvez utiliser la liaison de classe pour ajouter et supprimer des noms de classes CSS de l'attribut `class` d'un élément.

Pour créer une liaison de classe unique, utilisez le préfixe `class` suivi d'un point et du nom de la classe CSS.

Angular ajoute la classe lorsque l'expression liée est vraie (truthy).

Et il supprime la classe lorsque l'expression est fausse (falsy), à l'exception de `undefined`.

Pour lier plusieurs classes, utilisez `[class]` défini sur une expression.

L'expression peut être l'une des suivantes : une chaîne de noms de classes délimités par des espaces, un objet avec des noms de classes comme clés et des expressions vraies/fausses comme valeurs, ou un tableau de noms de classes.

Avec le format objet, Angular n'ajoute une classe que si sa valeur associée est vraie.

Et enfin, parlons de la liaison de style.

Vous pouvez utiliser la liaison de style pour définir des styles dynamiquement.

Pour créer une liaison de style unique, utilisez le préfixe `style` suivi d'un point et du nom de la propriété de style CSS. Angular définit la propriété à la valeur de l'expression liée, qui est généralement une chaîne.

Optionnellement, vous pouvez ajouter une extension d'unité comme `em` ou un pourcentage, ce qui nécessite un type numérique.

Vous pouvez écrire un nom de propriété de style soit en format avec tirets (kebab-case), soit en format chameau (camelCase).

Pour basculer plusieurs styles, liez à l'attribut `[style]`. L'expression de style peut être une liste de styles sous forme de chaîne ou un objet avec des noms de styles comme clés et des valeurs de styles comme valeurs. Notez que la liaison d'un tableau à `style` n'est pas supportée.

Cette fois, je parle de la liaison d'événement (event binding).

La liaison d'événement vous permet d'écouter et de répondre aux actions de l'utilisateur telles que les frappes au clavier, les mouvements de souris, les clics et les touchers.

C'est semblable à la pêche au bouchon, car vous attendez qu'un poisson morde à l'hameçon.

Et une fois qu'il mord, vous répondez rapidement.

Pour lier un événement, vous utilisez la syntaxe de liaison d'événement d'Angular.

La syntaxe consiste en un nom d'événement entre parenthèses à gauche d'un signe égal et une instruction de template à droite.

Dans cet exemple, le nom de l'événement est `click` et l'instruction de template est `onSave()`.

Nous pouvons maintenant définir la méthode `onSave()` dans notre classe Ts.

Et une fois que nous cliquons sur notre bouton, cet événement a été lié et notre méthode est exécutée.

Nous pouvons également nous lier à des événements personnalisés.

Pour démontrer cela, je vais créer un composant `item-details`.

Dans ce composant, je vais créer un `EventEmitter` avec le décorateur `@Output`, qui expose notre propriété aux composants parents.

Ensuite, je vais créer une méthode `deleteDummy`, qui émettra simplement notre propriété une fois que nous l'appellerons.

Maintenant, je vais définir un bouton et lier cette méthode à un événement de clic.

Ensuite, je placerai notre composant `item-details` dans notre `app.component`.

Et je me lierai à l'événement personnalisé `deleteRequest` que nous venons de créer.

J'appelle la méthode `deleteItem()`.

Et j'utiliserai le paramètre `$event` pour capturer la chaîne envoyée avec cet événement.

Et maintenant, je vais définir la méthode `deleteItem()` dans notre classe et simplement enregistrer ce que nous avons reçu.

Voilà comment vous vous liez à un événement personnalisé.

Maintenant, voyons la connexion par liaison bidirectionnelle (two-way binding).

La liaison bidirectionnelle est le concept de partage et de don.

Ce que vous donnez est ce que vous pouvez attendre des autres.

Pourquoi la liaison bidirectionnelle ? Elle donne aux composants de votre application un moyen de partager des données. Utilisez la liaison bidirectionnelle pour écouter les événements et mettre à jour les valeurs simultanément entre les composants parents et enfants.

La syntaxe de liaison bidirectionnelle d'Angular est une combinaison de crochets et de parenthèses `[()]`.

Cette syntaxe combine les crochets de la liaison de propriété avec les parenthèses de la liaison d'événement.

Je vais créer un composant `sizer`.

Dans notre composant, je vais définir une propriété `sizeValue` et un événement `sizeChange`.

La propriété `size` est une entrée (`@Input`), de sorte que les données peuvent circuler vers le composant `sizer`.

L'événement `sizeChange` est une sortie (`@Output`), ce qui permet aux données de circuler du composant `sizer` vers le composant parent.

Ensuite, il y a deux méthodes qui diminuent la taille de la police et augmentent la taille de la police.

Ces deux méthodes utilisent `resize` pour changer la valeur de la propriété `size` dans les limites des valeurs min/max, et pour émettre un événement qui transmet la nouvelle valeur de taille.

Dans le template du composant `sizer`, je vais créer deux boutons qui lient chacun l'événement de clic aux méthodes `inc` et `dec`.

Lorsque l'utilisateur clique sur l'un des boutons, le composant `sizer` appelle la méthode correspondante.

Les deux méthodes `inc` et `dec` appellent la méthode `resize` avec un `+1` ou `-1`, qui à son tour lève l'événement `sizeChange` avec la nouvelle valeur de taille.

Et en dessous d'eux, j'ajouterai un label qui affiche la propriété `size` et ajuste dynamiquement sa propre taille de police.

Dans notre composant racine `app.component`, j'inclurai un composant `app-sizer`, et j'utiliserai la liaison bidirectionnelle pour lier la propriété `fontSizePx` au composant `sizer`.

Et en dessous de cela, j'ajouterai un `div` qui utilisera cette propriété pour ajuster la taille de son texte.

Dans le `app.component`, `fontSizePx` établit la valeur de taille initiale du composant `sizer` en définissant la valeur à 16.

Cliquer sur le bouton met à jour le `fontSizePx` du `app.component`. La valeur révisée de `fontSizePx` met à jour la liaison de style, ce qui rend le texte affiché plus grand ou plus petit.

La syntaxe de liaison bidirectionnelle est un raccourci pour une combinaison de liaison de propriété et de liaison d'événement.

La liaison du composant `sizer` avec une liaison de propriété et une liaison d'événement séparées est la suivante.

La variable `$event` contient les données de l'événement `sizeChange` du composant `sizer`. Angular assigne la valeur de `$event` à `fontSizePx` du `app.component` lorsque l'utilisateur clique sur les boutons.

Pour utiliser la liaison bidirectionnelle avec des éléments de formulaire, nous avons besoin de `ngModel`, que je couvrirai dans la section sur les formulaires.

Les suivants sont les variables de template.

Les variables de template vous aident à utiliser les données d'une partie d'un template dans une autre partie du template.

C'est une variable qui est créée et qui identifie un composant ou un élément à l'intérieur du template lui-même.

C'est donc comme le numéro de téléphone d'un composant, que vous pouvez utiliser pour appeler au cas où vous auriez besoin de quelque chose de sa part.

Avec les variables de template, vous pouvez effectuer des tâches telles que répondre à la saisie de l'utilisateur ou affiner finement la syntaxe de vos applications.

Dans le template, vous utilisez le symbole dièse `#` pour déclarer une variable de template.

La variable de template suivante `#phone` déclare une variable `phone` sur un élément `input`. Vous pouvez vous référer à une variable de template n'importe où dans le template du composant.

Ici, un bouton plus bas dans le template se réfère à la variable `phone`.

Maintenant, nous pouvons définir la méthode `callPhone` et enregistrer la valeur passée, qui est la valeur réelle de l'entrée.

Alors, quelle est la portée d'une variable de template ? Vous pouvez vous référer à une variable de template n'importe où à l'intérieur de son template environnant.

Les directives structurelles telles que `*ngIf` et `*ngFor`, que nous couvrirons dans les vidéos suivantes, ou `<ng-template>`, agissent comme une limite de template ; vous ne pouvez pas accéder aux variables de template en dehors de ces limites.

Alors, pouvons-nous accéder aux variables dans un template imbriqué ? Un template interne peut accéder aux variables de template que le template externe définit.

Dans l'exemple suivant, changer le texte dans l'entrée change la valeur dans le `span` parce qu'Angular met immédiatement à jour les changements de la variable de template `ref1`.

Dans ce cas, il y a un `ng-template` implicite autour d'un `span` et la définition de la variable est en dehors de celui-ci.

C'est donc la même chose que de se lier explicitement comme ceci.

Cependant, accéder à cette variable de template depuis l'extérieur du template parent ne fonctionne pas, c'est la même chose que d'écrire ce qui suit.

Et c'est tout pour les variables de template.

Maintenant, discutons des directives. C'est la même chose que si vous étiez le PDG d'une entreprise et que vous donniez des directives à vos employés sur la façon de se comporter et sur ce qu'il faut faire dans certaines situations.

Que sont les directives ?

Les directives sont des classes qui ajoutent un comportement supplémentaire aux éléments de votre application Angular.

Avec les directives intégrées d'Angular, vous pouvez gérer les formulaires, les listes, les styles et ce que les utilisateurs voient.

Les différents types de directives Angular sont les suivants :

Les composants : des directives avec un template. Ce type de directive est le type de directive le plus courant.
Les directives d'attribut : des directives qui modifient l'apparence ou le comportement d'un élément, d'un composant ou d'une autre directive.
Les directives structurelles : des directives qui modifient la mise en page du DOM en ajoutant et en supprimant des éléments du DOM.

Aujourd'hui, nous parlons des directives d'attribut intégrées.

Une directive d'attribut écoute et modifie le comportement d'autres éléments HTML, attributs, propriétés et composants.

De nombreux modules Angular tels que `RouterModule` et `FormsModule` définissent leurs propres directives d'attribut.

Les directives d'attribut les plus courantes sont les suivantes :

`ngClass` : ajoute et supprime un ensemble de classes CSS.
`ngStyle` : ajoute et supprime un ensemble de styles HTML.
`ngModel` : ajoute une liaison de données bidirectionnelle à un élément de formulaire HTML.

Comment ajouter et supprimer des classes avec `ngClass` ?

Vous pouvez ajouter ou supprimer plusieurs classes CSS simultanément avec `ngClass`.

Pour ajouter ou supprimer une seule classe, utilisez la liaison de classe plutôt que `ngClass`.

Sur l'élément que vous souhaitez styliser, ajoutez `[ngClass]` et définissez-le égal à une expression.

Dans notre classe, définissons `isSpecial` comme `true`. Parce que `isSpecial` est vrai, `ngClass` applique la classe `special` au `div`.

Pour utiliser `ngClass` avec une méthode, ajoutez la méthode à la classe du composant.

Dans l'exemple suivant, `setCurrentClasses` définit la propriété `currentClasses` avec un objet qui ajoute ou supprime trois classes basées sur l'état vrai ou faux de trois autres propriétés du composant.

Chaque clé de l'objet est un nom de classe CSS.

Si une clé est vraie, `ngClass` ajoute la classe ; si une clé est fausse, `ngClass` supprime la classe.

Les valeurs booléennes sont codées en dur juste pour la démonstration.

Dans le template, ajoutez la liaison de propriété `ngClass` à `currentClasses` pour définir les classes de l'élément.

Et maintenant, nous pouvons prévisualiser nos classes.

Maintenant, parlons de `ngStyle`.

Vous pouvez utiliser `ngStyle` pour définir plusieurs styles en ligne simultanément en fonction de l'état du composant.

Pour utiliser `ngStyle`, ajoutez une méthode à la classe du composant.

Ajoutez un objet vide `currentStyles`.

Dans l'exemple suivant, `setCurrentStyles` définit la propriété `currentStyles` avec un objet qui définit trois styles, et une liaison de propriété `ngStyle` à `currentStyles`.

Pour ce cas d'utilisation, Angular applique les styles lors de l'initialisation et en cas de changements.

Pour ce faire, l'exemple complet appelle `setCurrentStyles` initialement avec `ngOnInit`.

Et la dernière dans la vidéo d'aujourd'hui est `ngModel`. Vous pouvez utiliser la directive `ngModel` pour afficher une propriété de données et mettre à jour cette propriété lorsque l'utilisateur effectue des changements.

Importez `FormsModule` et ajoutez-le à la liste des importations de `NgModule`.

Je vais créer un label et une entrée pour cet exemple.

Ajoutez une liaison `ngModel` sur un élément de formulaire HTML et définissez-la égale à la propriété, ici `name`.

Maintenant, si vous définissez la propriété à l'intérieur de notre classe de composant, vous pouvez voir comment la directive `ngModel` ajoute une liaison de données bidirectionnelle à notre entrée.

Cette syntaxe `ngModel` ne peut définir qu'une propriété liée aux données.

Lorsque vous écrivez un composant Angular, vous n'avez pas besoin d'un accesseur de valeur ou de `ngModel` si vous nommez la valeur et les propriétés d'événement selon la syntaxe de liaison bidirectionnelle d'Angular.

Et c'est tout pour cette section.

Dans cette section, nous continuons avec les directives Angular.

Construisons une directive d'attribut.

Créons un fichier `highlight.directive.ts`, ce qui est la convention que vous devriez toujours suivre.

Ensuite, importez le décorateur `Directive` depuis le noyau et implémentez ce décorateur avec la propriété `selector`.

Pour moi, ce sera `[appHighlight]`.

Ensuite, nous voulons exporter notre classe.

Et la dernière chose que nous voulons est d'importer cela dans notre tableau de déclarations dans `AppModule`.

C'est notre code de base pour une directive, que vous pouvez également obtenir avec la commande `ng generate directive highlight`.

Importez `ElementRef` depuis Angular Core.

`ElementRef` accorde un accès direct à l'élément DOM hôte via sa propriété `nativeElement`.

Ajoutez `ElementRef` dans le constructeur de la directive pour injecter une référence à l'élément DOM hôte, l'élément auquel vous appliquez `appHighlight`.

Ajoutez la logique à la classe de la directive `highlight` qui définit l'arrière-plan en jaune.

Pour utiliser la directive `highlight`, ajoutez un élément paragraphe au template HTML avec la directive comme attribut.

Angular crée une instance de la classe `HighlightDirective` et injecte la référence à l'élément paragraphe dans le constructeur de la directive, ce qui définit le style d'arrière-plan de l'élément `p` en jaune.

Maintenant, voyons comment détecter quand un utilisateur passe la souris sur l'élément ou en sort, et comment répondre en définissant ou en effaçant la couleur de surbrillance.

Importez `HostListener` depuis Angular Core. Ajoutez-le aux gestionnaires d'événements qui répondent lorsque la souris entre ou sort, chacun avec un décorateur `@HostListener`.

Avec le décorateur `@HostListener`, vous pouvez vous abonner aux événements de l'élément DOM qui héberge une directive d'attribut.

Le paragraphe dans ce cas. Les gestionnaires délèguent à une méthode utilitaire `highlight` qui définit la couleur sur l'élément DOM hôte.

La couleur d'arrière-plan apparaît lorsque le pointeur survole l'élément paragraphe et disparaît lorsque le pointeur s'en éloigne.

Maintenant, voyons comment nous pouvons rendre la directive dynamique pour pouvoir l'utiliser à différents endroits avec différentes couleurs.

Dans le fichier `highlight.directive.ts`, importez `Input` depuis Angular Core, ajoutez une propriété d'entrée `appHighlight`.

Le décorateur `@Input` ajoute des métadonnées à la classe qui rendent la propriété `appHighlight` de la directive disponible pour la liaison.

Dans `app.component.ts`, ajoutez une propriété `color` au composant.

Pour appliquer simultanément la directive et la couleur, utilisez la liaison de propriété avec le sélecteur de directive `appHighlight` en le définissant égal à `color`.

La liaison d'attribut `appHighlight` effectue deux tâches : elle applique la directive de surbrillance à l'élément paragraphe et définit la couleur de surbrillance de la directive avec la liaison de propriété.

Et c'est tout pour celle-ci.

C'est la dernière section sur les directives.

Alors, voyons ce que sont les directives structurelles.

Les directives structurelles sont responsables de la mise en page HTML.

Elles façonnent ou remodèlent la structure du DOM, typiquement en ajoutant, supprimant et manipulant les éléments hôtes auxquels elles sont attachées.

Cette section présente les directives structurelles intégrées les plus courantes.

`*ngIf` : crée ou supprime conditionnellement des sous-vues du template.
`*ngFor` : répète un nœud pour chaque élément d'une liste.
`[ngSwitch]` : un ensemble de directives qui basculent entre des vues alternatives.

Vous pouvez ajouter ou supprimer un élément en appliquant une directive `*ngIf` à un élément hôte.

Lorsque `*ngIf` est faux, Angular supprime un élément et ses descendants du DOM.

Angular dispose ensuite de leurs composants, ce qui libère de la mémoire et des ressources. Pour ajouter ou supprimer un élément, liez le `*ngIf` à une expression de condition telle que `isActive` dans cet exemple.

Lorsque l'expression `isActive` retourne une valeur vraie, `*ngIf` ajoute le `div` au DOM.

Lorsque l'expression est fausse, `*ngIf` supprime le `div` du DOM.

C'est plus simple, n'est-ce pas ?

Maintenant, parlons de `*ngFor`.

Vous pouvez utiliser la directive `*ngFor` pour présenter une liste d'éléments.

Créons un tableau d'objets avec une propriété `name` à l'intérieur.

Définissez un bloc de HTML qui détermine comment Angular affiche un seul élément.

Pour lister vos éléments, assignez le raccourci `let item of items` à `*ngFor`. La chaîne `let item of items` demande à Angular de faire ce qui suit :

Stocker chaque élément du tableau `items` dans la variable de boucle locale `item`, rendre chaque élément disponible pour le template HTML à chaque itération.

Traduire `let item of items` en un `<ng-template>` autour de l'élément hôte.

Répéter le `<ng-template>` pour chaque élément de la liste.

Au fait, vous pouvez obtenir l'index de `*ngFor` dans une variable d'entrée de template et l'utiliser dans le template. Dans le `*ngFor`, ajoutez un point-virgule et `let i = index` au raccourci.

L'exemple suivant capture l'index dans une variable nommée `i` et l'affiche à côté du nom de l'élément.

Et la dernière directive dont nous allons parler est `switch`, semblable à l'instruction `switch` de JavaScript.

`ngSwitch` affiche un élément parmi plusieurs éléments possibles en fonction d'une condition de commutation.

Angular ne place que l'élément sélectionné dans le DOM.

`ngSwitch` est un ensemble de trois directives :

`ngSwitch` : une directive d'attribut qui modifie le comportement de ses directives compagnes.
`*ngSwitchCase` : directive structurelle qui ajoute son élément au DOM lorsque sa valeur liée est égale à la valeur de commutation.
`*ngSwitchDefault` : directive structurelle qui ajoute son élément au DOM lorsqu'il n'y a pas de `*ngSwitchCase` sélectionné.

Je vais modifier le tableau `items` pour qu'il ne contienne qu'un seul élément.

Sur un élément tel qu'un `div`, ajoutez `[ngSwitch]` lié à une expression qui retourne la valeur de commutation, telle que `name`.

Bien que la valeur `name` dans cet exemple soit une chaîne, la valeur de commutation peut être de n'importe quel type. Liez à `*ngSwitchCase` et `*ngSwitchDefault` sur les éléments pour les cas.

Et maintenant, selon la valeur de `item.name`, l'affichage sur la page change.

Si vous n'avez pas fourni de cas pour la valeur du nom, le `default` sera exécuté.

Ensuite, nous discutons de l'injection de dépendances (dependency injection).

Les dépendances sont des services ou des objets dont une classe a besoin pour remplir sa fonction.

L'injection de dépendances, ou DI, est un patron de conception dans lequel une classe demande des dépendances à des sources externes plutôt que de les créer elle-même.

Vous pouvez voir cela comme si vous ajoutiez une extension à votre navigateur ou une application à un téléphone.

Une fois que vous l'ajoutez, vous vous dotez de nouvelles fonctionnalités et caractéristiques.

Créons un service que nous pouvons injecter dans nos composants.

Créez un nouveau fichier avec le nom `log.service.ts`.

Importez le décorateur `Injectable` depuis Angular Core.

Ensuite, pour les métadonnées `providedIn`, ajoutez la valeur `'root'`, ce qui signifie que nous allons fournir le service à la racine de l'application et qu'il est visible dans toute l'application.

Exportez notre classe `LogService` et à l'intérieur de ce service, nous voulons ajouter notre méthode `logMessage`, qui enregistrera simplement les messages passés.

Pour la clarté et la maintenabilité, il est recommandé de définir les composants et les services dans des fichiers séparés. Maintenant, injectez notre `LogService` dans le fichier `app.module.ts` dans le tableau `providers`.

Injecter des services a pour résultat de les rendre visibles pour un composant.

Pour injecter une dépendance dans le constructeur d'un composant, fournissez un argument de constructeur avec le type de dépendance.

L'exemple suivant spécifie le `LogService` dans le constructeur du `app.component`. Le type de `logService` est `LogService`.

Maintenant, nous pouvons référencer notre `LogService` dans notre composant et appeler notre méthode à partir de celui-ci pour passer notre message et, comme vous pouvez le voir, elle est exécutée comme prévu.

Nous pouvons utiliser cette approche pour injecter des bibliothèques tierces dans d'autres modules qui sont disponibles dans le framework Angular.

Alors injectons le module `Renderer2` qui est utilisé pour le rendu personnalisé et la mise à jour du DOM.

Importez `Renderer2` depuis Angular Core et injectez-le à l'intérieur du constructeur.

De plus, nous aurons besoin de `ElementRef`, que nous pouvons utiliser pour référencer nos éléments DOM, ou le composant hôte dans notre cas.

Maintenant, à l'intérieur du cycle de vie `ngOnInit`, appelez la méthode `setStyle` du renderer et définissez la couleur de l'élément natif hôte en rouge.

Cette méthode change la couleur du texte de nos composants.

Et comme vous pouvez le voir, avec l'injection de dépendances, nous obtenons l'accès à plus de fonctionnalités et de méthodes.

C'est tout ce qu'il y a à savoir.

Le sujet suivant est très important : le routage (routing).

Le routeur Angular est une partie centrale de la plateforme Angular.

Il permet aux développeurs de construire des applications à page unique avec plusieurs vues et la navigation entre ces vues.

Nous pouvons comparer le routage de nos applications à la navigation d'un avion.

Le pilote définit les coordonnées de vol (dans notre cas, le chemin de la route), et l'avion atterrit à l'endroit désiré ou sur la page désirée dans notre application.

Souvent, les avions transportent des marchandises ou du fret et les routes transportent des paramètres, des informations et des données.

Et malheureusement, certaines choses s'écrasent ou se perdent.

Et pour les routes, nous obtenons parfois des erreurs 404. Pour utiliser le routeur Angular, une application doit avoir au moins deux composants afin de pouvoir naviguer de l'un à l'autre.

Pour créer un composant en utilisant le CLI, entrez ce qui suit sur la ligne de commande, où `first` est le nom de votre composant : `ng generate component first`.

Répétez cette étape pour un deuxième composant ou donnez-lui un nom différent. Ici, le nouveau nom est `second`.

Ce guide fonctionne avec une application Angular générée par le CLI.

Si vous travaillez manuellement, assurez-vous d'avoir `<base href="/">` dans le `<head>` de votre fichier `index.html`.

Ceci suppose que le dossier `app` est la racine de l'application et qu'il utilise `/`. Créez un nouveau module pour le routage nommé `app-routing.module.ts`.

Définissez `const routes: Routes = [...]`.

Ici, nous définirons nos chemins (paths) et composants.

À l'intérieur du tableau `imports` de `@NgModule`, ajoutez `RouterModule.forRoot(routes)`, puis exportez le `RouterModule` afin qu'il puisse être importé dans le module racine.

À la fin, définissez la classe `AppRoutingModule`. Importez `AppRoutingModule` dans `AppModule` et ajoutez-le au tableau `imports`.

Maintenant, définissez vos routes dans votre tableau `routes`.

Chaque route dans ce tableau est un objet JavaScript qui contient deux propriétés.

La première propriété `path` définit le chemin de l'URL pour la route.

La deuxième propriété `component` définit le composant qu'Angular doit utiliser pour le chemin correspondant.

Maintenant que vous avez défini vos routes, vous pouvez les ajouter à votre application.

D'abord, ajoutez des liens vers les deux composants.

Assignez l'attribut `routerLink` à une balise d'ancrage (`<a>`) à laquelle vous souhaitez ajouter la route.

Définissez la valeur de l'attribut sur le composant à afficher lorsqu'un utilisateur clique sur chaque lien.

Ensuite, mettez à jour le template de votre composant pour inclure `<router-outlet>`.

Cet élément informe Angular de mettre à jour la vue de l'application avec le composant pour la route sélectionnée.

Vous pouvez ajouter l'attribut `routerLinkActive` si vous souhaitez styliser le lien actif.

Une note : l'ordre des routes est important car le routeur utilise une stratégie de "premier match gagnant" lors de la correspondance des routes.

Ainsi, les routes plus spécifiques doivent être placées au-dessus des routes moins spécifiques.

Souvent, lorsqu'un utilisateur navigue dans l'application, vous souhaitez passer des informations d'un composant à un autre.

Pour ce faire, vous utilisez l'interface `ActivatedRoute`.

D'abord, importez `ActivatedRoute` et `ParamMap` dans votre composant.

Injectez une instance de `ActivatedRoute` en l'ajoutant au constructeur de votre application.

Mettez à jour la méthode `ngOnInit` pour accéder à l' `ActivatedRoute` et suivre le paramètre `id`.

Maintenant, nous devons ajuster nos routes pour passer également les paramètres `id`.

Pour cela, ajoutez deux-points et le nom de votre paramètre dans le chemin.

Et ensuite, nous pouvons ajouter des valeurs d'ID à nos liens.

Voilà comment vous passez et récupérez des données d'un composant à un autre.

Une application qui fonctionne bien doit gérer avec élégance le cas où un utilisateur tente de naviguer vers une partie de votre application qui n'existe pas.

Pour ajouter cette fonctionnalité à votre application, vous configurez une route générique (wildcard route).

Le routeur Angular sélectionne cette route chaque fois que l'URL demandée ne correspond à aucun chemin de routeur.

Pour configurer une route générique, ajoutez le code suivant à votre définition de routes.

Pour la propriété `component`, vous pouvez définir n'importe quel composant de votre application.

Les choix courants incluent un composant spécifique à l'application "Page non trouvée".

Mais ici, je redirige simplement vers le premier composant.

Et maintenant, si vous naviguez vers n'importe quel chemin aléatoire, cela nous donnera toujours le premier composant.

À mesure que votre application devient plus complexe, vous pourriez vouloir créer des routes relatives à un composant autre que votre composant racine.

Ces types de routes imbriquées sont appelés routes enfants.

Cela signifie que vous ajoutez un deuxième `<router-outlet>` à l'application car il s'ajoute au `<router-outlet>` du `app.component`.

Dans cet exemple, il y a deux composants enfants supplémentaires, `ChildA` et `ChildB`.

Ici, `FirstComponent` a sa propre navigation et un deuxième `<router-outlet>` en plus de celui du `app.component`.

De plus, je vais créer deux routes enfants avec les `routerLink` de `child-a` et `child-b`.

Maintenant, je vais créer deux composants supplémentaires avec l'Angular CLI et les nommer `ChildAComponent` et `ChildBComponent`.

Chaque route enfant est comme n'importe quelle autre route, en ce sens qu'elle a besoin à la fois d'un chemin et d'un composant.

La seule différence est que vous placez les routes enfants dans un tableau `children` à l'intérieur de la route parente.

Maintenant, si vous naviguez vers l'une des routes enfants, nous obtenons le composant enfant correspondant.

Utilisez les gardes de route (route guards) pour empêcher les utilisateurs de naviguer vers des parties d'une application sans autorisation.

Les gardes de route suivants sont disponibles dans Angular : `canActivate`, `canActivateChild`, `canDeactivate`, `resolve` et `canLoad`. Créez un service pour votre garde.

`ng generate guard your-guard`.

Dans votre classe de garde, implémentez la garde que vous souhaitez utiliser. L'exemple suivant utilise `canActivate` pour protéger la route.

Maintenant, selon votre logique, elle peut retourner `true` ou `false`.

Habituellement, elle vérifie si l'utilisateur est connecté ou s'il a les privilèges pour accéder à la page. Dans votre module de routage, utilisez la propriété appropriée dans votre configuration de routes ; ici, `canActivate` indique au routeur de médiatiser la navigation vers cette route particulière.

Maintenant, si vous réglez la garde sur `false`, nous ne pouvons pas accéder à la route.

Sinon, nous le pouvons.

Et c'est tout pour le routage dans cette section.

Après celle-ci, nous couvrons un concept encore plus important : les formulaires Angular.

Commençons par les formulaires basés sur les templates (template-driven forms).

Je sais que cela semble impossible, mais il fut un temps où il n'y avait ni internet ni même d'ordinateur.

Ainsi, à cette époque, nous devions remplir de bons vieux formulaires papier lorsque nous voulions consulter un médecin ou demander divers documents personnels.

Les formulaires web ne sont donc rien d'autre, sauf qu'ils sont numériques.

Angular supporte deux approches de conception pour les formulaires interactifs.

Les formulaires basés sur les templates conviennent aux formulaires petits ou simples.

Tandis que les formulaires réactifs sont plus évolutifs et conviennent aux formulaires complexes.

Ce tutoriel vous montre comment construire un formulaire à partir de zéro.

D'abord, importez `FormsModule` dans votre module racine d'application.

Construisons d'abord notre classe de données qui définit un modèle de données reflété dans notre formulaire.

J'aurai trois propriétés : `id`, `name` et `species`.

Maintenant, importons notre classe dans le `app.component`.

Définissez un tableau de espèces.

Maintenant, créez un modèle à partir de la classe.

Ici, nous utilisons des données fictives.

Mais dans votre application réelle, vous utiliseriez un service pour obtenir les données de l'API et les sauvegarder.

De plus, ajoutons une propriété `submitted`, qui changera selon l'état du formulaire, et une méthode `onSubmit`.

Ensuite, dans notre fichier HTML, nous allons créer un formulaire qui reflète notre modèle de données.

Créez un formulaire et à l'intérieur, deux `div` pour deux champs.

Le premier sera l'entrée pour le nom.

Et j'ajoute un label et l'attribut `required` à notre entrée.

Et le second sera un `select`, qui bouclera à travers un tableau d'espèces pour montrer toutes les valeurs du tableau.

Comme pour l'entrée, j'ajoute un label pour notre `select`.

Et j'ajouterai également l'attribut `required`.

Ensuite, j'utiliserai `*ngFor` pour parcourir toutes les valeurs et les afficher.

Si vous lancez l'application maintenant, vous verrez la liste des espèces dans le contrôle de sélection.

Les éléments d'entrée ne sont pas encore liés aux valeurs de données ou aux événements.

Ils sont donc encore vides et n'ont aucun comportement.

L'étape suivante consiste à lier les contrôles d'entrée aux propriétés correspondantes avec la liaison bidirectionnelle afin qu'ils répondent à la saisie de l'utilisateur en mettant à jour le modèle de données, et répondent également aux changements programmatiques des données en mettant à jour l'affichage.

La directive `ngModel` déclarée dans le `FormsModule` vous permet de lier les contrôles de votre formulaire basé sur les templates aux propriétés de votre modèle de données.

Ajoutez la directive `ngModel` en utilisant la syntaxe de liaison bidirectionnelle pour le nom en utilisant `model.name`.

Et pour l'espèce, utilisez la valeur `model.species`.

Lorsque vous utilisez `ngModel` sur un élément, vous devez définir un attribut `name` pour cet élément.

Angular utilise le nom assigné pour enregistrer l'élément avec la directive `ngForm` attachée à l'élément de formulaire parent.

Ainsi, afin d'enregistrer notre formulaire, ajoutez une variable de référence de template en utilisant la valeur `ngForm`.

La variable de template est maintenant une référence à l'instance de la directive `ngForm` qui régit le formulaire dans son ensemble.

Afin de tester notre application, placez l'objet modèle dans notre template avec un pipe JSON.

Maintenant, si vous mettez à jour vos champs de formulaire, vous verrez que le modèle est mis à jour.

Maintenant, l'utilisateur doit pouvoir soumettre ce formulaire après l'avoir rempli. Créez un bouton de soumission en bas.

Le bouton de soumission au bas du formulaire ne fait rien de lui-même, mais il déclenche un événement de soumission de formulaire en raison de son type `submit`.

Pour répondre à cet événement :

Liez l'événement `ngSubmit` du formulaire à la méthode `onSubmit()` du composant.

Utilisez la variable de référence de template `#petForm`.

Pour accéder au formulaire qui contient le bouton de soumission et créer une liaison d'événement.

Vous lierez la propriété du formulaire qui indique sa validité globale à la propriété `disabled` du bouton de soumission.

Lancez l'application maintenant.

Remarquez que le bouton est activé.

Bien qu'il ne fasse encore rien d'utile.

Supprimez la valeur du nom.

Cela viole la règle `required`, donc désactivez le bouton de soumission.

Pour montrer une réponse à la soumission du formulaire, vous pouvez masquer la zone de saisie des données et afficher autre chose à sa place.

Enveloppez tout le formulaire dans un `div` et liez sa propriété `hidden` à la propriété `submitted` du composant.

Le formulaire principal est visible dès le début car la propriété `submitted` est fausse jusqu'à ce que vous soumettiez le formulaire. Pour afficher autre chose pendant que le formulaire est dans l'état soumis, ajoutez le HTML suivant sous le nouveau wrapper `div`, ajoutez les propriétés que vous avez mises à jour et le bouton d'édition.

Si l'utilisateur veut mettre à jour les champs à nouveau.

Et maintenant, voyons comment cela fonctionne.

C'est tout pour les formulaires basés sur les templates.

Maintenant, dans la section suivante, nous allons voir comment nous pouvons prendre plus de contrôle sur nos formulaires et comment créer des formulaires réactifs.

Les formulaires réactifs fournissent une approche pilotée par le modèle pour gérer les entrées de formulaire, dont les valeurs changent au fil du temps.

Chaque changement de l'état du formulaire retourne un nouvel état, ce qui maintient l'intégrité du modèle entre les changements.

Ajoutons un contrôle de formulaire de base.

Pour utiliser les contrôles de formulaire réactifs, importez `ReactiveFormsModule` du package `@angular/forms` et ajoutez-le au tableau `imports` de votre `NgModule`.

Pour enregistrer un seul contrôle de formulaire, importez la classe `FormControl` et créez une nouvelle instance de `FormControl` pour la sauvegarder en tant que propriété de classe.

Utilisez le constructeur de `FormControl` pour définir sa valeur initiale, qui dans ce cas est une chaîne vide.

En créant ces contrôles dans votre classe de composant, vous obtenez un accès immédiat pour écouter, mettre à jour et valider l'état de l'entrée du formulaire.

Après avoir créé un contrôle dans la classe du composant, vous devez l'associer à un élément de contrôle de formulaire dans le template. Liez le template avec un `FormControl` en utilisant la liaison `[formControl]` fournie par la directive `FormControlDirective`, qui est également incluse dans le `ReactiveFormsModule`.

En utilisant la syntaxe de liaison de template, le contrôle de formulaire est maintenant enregistré sur l'élément d'entrée `name` dans le template. Vous pouvez afficher la valeur de l'une des manières suivantes : via l'observable `valueChanges` où vous pouvez écouter les changements de la valeur du formulaire dans le template en utilisant le pipe `async` ou dans la classe du composant en utilisant la méthode `subscribe`, ou avec la propriété `value`, qui vous donne un instantané de la valeur actuelle.

L'exemple suivant vous montre comment afficher la valeur actuelle en utilisant l'interpolation dans le template.

La valeur affichée change au fur et à mesure que vous mettez à jour l'élément de contrôle de formulaire.

Les formulaires réactifs ont des méthodes pour changer la valeur d'un contrôle de manière programmatique, ce qui vous donne la flexibilité de mettre à jour la valeur sans interaction de l'utilisateur.

L'exemple suivant ajoute une méthode à la classe du composant pour mettre à jour la valeur du contrôle à "Nancy" en utilisant la méthode `setValue()`.

Mettez à jour le bouton du template pour simuler une mise à jour du nom.

Lorsque vous cliquez sur le bouton "Update Name", la valeur saisie dans l'élément de contrôle de formulaire est reflétée comme sa valeur actuelle.

Le modèle de formulaire est la source de vérité pour le contrôle.

Ainsi, lorsque vous cliquez sur le bouton, la valeur de l'entrée est modifiée à l'intérieur de la classe du composant, remplaçant sa valeur actuelle.

Un formulaire contient généralement plusieurs contrôles liés.

Les formulaires réactifs offrent deux façons de regrouper plusieurs contrôles liés dans un seul formulaire d'entrée.

La première méthode, `FormGroup`, définit un formulaire avec un ensemble fixe de contrôles que vous pouvez gérer ensemble.

Et la seconde méthode, `FormArray`, définit un formulaire dynamique où vous pouvez ajouter et supprimer des contrôles au moment de l'exécution.

Importez les classes `FormGroup` et `FormControl` du package `@angular/forms`.

Créez une propriété dans la classe du composant nommée `profileForm` et initialisez-la avec une nouvelle instance de `FormGroup`.

Pour initialiser le `FormGroup`, fournissez au constructeur un objet de clés nommées mappées à leur contrôle.

Pour le `profileForm`, ajoutez deux instances de `FormControl` avec les noms `firstName` et `lastName`.

Les contrôles de formulaire individuels sont maintenant collectés au sein d'un groupe.

Après avoir défini un modèle, vous devez mettre à jour le template pour refléter le modèle dans la vue.

J'ajoute deux entrées et deux labels qui correspondent à notre modèle.

La directive `formControlName` lie chaque entrée individuelle au contrôle de formulaire défini dans le `FormGroup`.

La directive `ngForm` écoute l'événement de soumission émis par l'élément de formulaire et émet un événement `ngSubmit` que vous pouvez lier à une fonction de rappel (callback).

Ajoutez un écouteur d'événement `ngSubmit` à la balise `form` avec la méthode de rappel `onSubmit()`.

La méthode `onSubmit()` capture la valeur actuelle de `profileForm`.

Ici, vous allez simplement enregistrer la valeur du formulaire.

L'événement de soumission est émis par la balise `form` en utilisant l'événement DOM natif, vous déclenchez l'événement en cliquant sur un bouton de type `submit`.

Cela permet à l'utilisateur d'appuyer sur la touche Entrée pour soumettre le formulaire complété.

Ajoutez un bouton au bas du formulaire pour déclencher la soumission du formulaire.

Et c'est tout pour les formulaires réactifs.

Dans la section suivante, nous allons voir comment nous pouvons améliorer nos formulaires.

Ainsi, dans cette section, nous couvrons la validation de formulaire.

Ce tutoriel vous montrera comment valider la saisie de l'utilisateur depuis l'interface utilisateur et afficher des messages de validation utiles dans les formulaires réactifs et basés sur les templates.

Tout ce que vous voulez stocker dans votre base de données doit avoir plusieurs niveaux de validation. Voyez la validation comme une audition ou un entretien d'embauche où quelqu'un se présente à vous et vous décidez s'il passera ou non.

Pour ajouter une validation à un formulaire basé sur les templates, vous ajoutez les mêmes attributs de validation que vous le feriez avec la validation de formulaire HTML native.

Angular utilise des directives pour faire correspondre ces attributs avec des fonctions de validation dans le framework.

Chaque fois que la valeur d'un contrôle de formulaire change, Angular exécute la validation et génère soit une liste d'erreurs de validation qui aboutit à un statut invalide, soit un statut valide.

Je vais créer un champ de chaîne `name` à l'intérieur de notre classe de composant.

Ensuite, dans notre fichier HTML, j'ajouterai un champ de texte d'entrée avec l'attribut `required` et une longueur minimale (`minlength`) de quatre.

Je lie la propriété d'entrée `name` à `ngModel`, et j'exporte `ngModel` vers une variable locale appelée `nameModel`. `ngModel` reflète de nombreuses propriétés de son instance de contrôle de formulaire sous-jacente.

Ainsi, vous pouvez utiliser ce template pour vérifier les états de contrôle tels que `valid` et `dirty`.

Le `*ngIf` de l'élément `div` révèle un ensemble de messages imbriqués, mais seulement si le nom est invalide et que le contrôle est soit `dirty` (modifié), soit `touched` (visité).

Chaque `div` imbriqué peut présenter un message personnalisé pour l'une des erreurs de validation possibles.

Ce sont des messages pour `required` et `minlength`.

Maintenant, si nous tapons quelque chose et laissons le champ vide, nous obtiendrons le message d'erreur de validation.

Et il en va de même si nous saisissons une valeur de moins de quatre caractères.

Dans un formulaire réactif, la source de vérité est la classe du composant.

Au lieu d'ajouter des validateurs via des attributs dans le template, vous ajoutez des fonctions de validation directement au modèle de contrôle de formulaire dans la classe du composant.

Les mêmes validateurs intégrés qui sont disponibles sous forme d'attributs dans les formulaires basés sur les templates, tels que `required` et `minlength`, sont tous disponibles en tant que fonctions de la classe `Validators`.

Pour mettre à jour la validation du formulaire afin qu'il soit un formulaire réactif, utilisez certains des mêmes validateurs intégrés.

Dans cet exemple, le contrôle `name` configure deux validateurs intégrés : `Validators.required` et `Validators.minLength(4)`.

Ces validateurs sont synchrones, ils sont donc passés comme second argument.

Notez que vous pouvez supporter plusieurs validateurs en passant les fonctions dans un tableau.

Cet exemple ajoute également une méthode getter.

Dans un formulaire réactif, vous pouvez toujours accéder à n'importe quel contrôle de formulaire via la méthode `get` sur son groupe parent.

Mais parfois, il est utile de définir des getters.

C'est un raccourci pour le template.

Dans notre template, ajoutez `formGroup` à notre formulaire.

Et maintenant, la seule chose que nous devons changer dans notre template pour le rendre réactif est de supprimer `ngModel` et de lier notre contrôle `name` à `formControlName`.

Ce formulaire diffère de la version basée sur les templates en ce qu'il n'exporte plus de directives.

Au lieu de cela, il utilise le getter `name` défini dans la classe du composant. Notez que l'attribut `required` est toujours présent dans le template.

Bien qu'il ne soit pas nécessaire pour la validation, il doit être conservé à des fins d'accessibilité.

Nous sommes enfin arrivés à la fin de ce long tutoriel, et nous allons couvrir la communication en utilisant le Client HTTP.

Imaginez que vous dirigez une station de télévision ou un journal.

Et si vous perdiez la communication avec les reporters ? Vous vous retrouveriez avec un journal vide ou aucune émission d'information. C'est la même chose avec les applications web.

Sans communication avec le backend, nos applications seront vides, sans informations ni instructions provenant du serveur.

La plupart des applications front-end ont besoin de communiquer avec un serveur via le protocole HTTP pour télécharger ou téléverser des données et accéder à d'autres services backend.

Avant de pouvoir utiliser le Client HTTP, vous devez importer le module `HttpClientModule` d'Angular.

La plupart des applications le font dans le module racine `AppModule`.

Créons un service de données.

Le cas d'utilisation le plus courant est d'injecter `HttpClient` dans un service.

Et de l'utiliser dans toute l'application. Vous pouvez ensuite injecter le service `HttpClient` comme une dépendance d'une classe d'application, comme le montre cet exemple.

Maintenant, voyons comment nous pouvons récupérer des données d'un serveur.

Pour ce faire, nous allons utiliser la méthode `get()` de `HttpClient`.

D'abord, injectez `HttpClient` dans notre service.

Ensuite, créez la méthode `getData()` et à l'intérieur de cette méthode, nous récupérerons nos données.

La méthode `get()` prend deux arguments : l'URL du point de terminaison (endpoint) à partir duquel récupérer les données et un objet d'options que vous utilisez pour configurer la requête afin d'ajouter des choses comme des paramètres à votre requête.

Pour ce tutoriel, j'ai trouvé un service d'API de cocktails gratuit.

Le lien sera dans la boîte de description ci-dessous. Entrez l'URL, et aucun paramètre supplémentaire n'est requis dans ce cas.

Maintenant, dans notre `app.component`, nous injectons le service de données dans le constructeur. À l'intérieur de la méthode `ngOnInit`, appelons notre méthode `getData()`.

Parce que la méthode du service retourne un observable, le composant s'abonne à la valeur de retour de la méthode.

Je vais juste faire un `console.log` du résultat.

Et voilà comment vous obtenez des données du serveur.

Dans un monde idéal, tout fonctionne comme par magie.

Mais nous ne vivons pas dans un monde idéal, heureusement, et nous perdons parfois la connexion avec l'API.

Nous devons donc gérer les erreurs lorsqu'elles surviennent.

Si la requête échoue sur le serveur, `HttpClient` retourne un objet d'erreur au lieu d'une réponse réussie.

Ajoutons un `pipe` sur notre méthode `get` et utilisons `catchError` pour l'intercepter.

Je vais enregistrer l'erreur à des fins de développement et retourner `throwError` avec un message.

Cela devrait être utilisé dans votre application pour montrer à l'utilisateur que sa requête a échoué.

Sans notification, il ne saurait pas ce qui se passe.

Et n'oubliez pas d'importer les packages manquants.

Maintenant, nous pouvons changer l'URL pour casser la requête.

Et pour voir l'erreur, nous ne voulons généralement pas voir cette vue dans nos applications.

Mais nous devons être prêts pour cela quand cela arrive.

`HttpClient`, en plus de `get`, possède également une méthode `post()` pour soumettre des données au serveur.

Par exemple, si vous soumettez un formulaire, nous avons des requêtes `delete()` pour supprimer des données de la base de données évidemment, une requête `put()` qui remplace une ressource avec des données mises à jour.

Maintenant, la plupart des API nécessitent une clé d'authentification avec leurs requêtes.

Alors voyons comment nous pouvons ajouter cela. J'ai trouvé cette base de données du Seigneur des Anneaux qui nécessite une clé d'authentification.

Créons un objet `httpOptions` avec la propriété `headers`.

Cette propriété sera un nouvel objet `HttpHeaders`, et nous passerons deux propriétés.

`Content-Type` est `application/json`, ce qui signifie que nous utilisons du JSON comme contenu, et `Authorization`, où nous entrons notre clé API. `Bearer` est le type d'autorisation, suivi de la clé.

Afin d'obtenir votre clé personnelle, vous devez vous inscrire. Le lien est dans la boîte de description ci-dessous.

Maintenant, mettez à jour le point de terminaison de l'API.

Et si vous essayez de l'appeler sans passer les `httpOptions`, vous pouvez voir que nous obtenons une erreur.

Mais si nous ajoutons l'autorisation, la requête est réussie.

Félicitations, vous avez regardé jusqu'au bout.

C'était un très long tutoriel et j'espère que vous avez appris beaucoup de nouvelles choses.

De plus, n'oubliez pas de vous abonner à Free Code Camp.

Et si vous voulez voir plus de tutoriels comme celui-ci, n'oubliez pas de consulter ma chaîne.

Mon nom est Slobodan, et je vous verrai dans l'une des prochaines vidéos ou tutoriels.

Prenez soin de vous.

À bientôt.