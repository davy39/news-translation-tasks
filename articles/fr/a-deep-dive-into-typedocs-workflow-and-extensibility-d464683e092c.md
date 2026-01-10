---
title: Une plongée en profondeur dans le flux de travail et l'extensibilité de TypeDoc
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-11T19:46:01.000Z'
originalURL: https://freecodecamp.org/news/a-deep-dive-into-typedocs-workflow-and-extensibility-d464683e092c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZFveofx2WsPuiHo__izU1w.gif
tags:
- name: api
  slug: api
- name: documentation
  slug: documentation
- name: plugins
  slug: plugins
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Une plongée en profondeur dans le flux de travail et l'extensibilité de
  TypeDoc
seo_desc: 'By Alexander Kamenov

  This topic aims to cover the basics on how you could extend the TypeDoc library
  functionality and what are the opportunities that it provides.

  For those of you who are not familiar with TypeDoc, this is a library which allows
  you...'
---

Par Alexander Kamenov

Ce sujet vise à couvrir les bases sur la manière dont vous pourriez étendre la fonctionnalité de la bibliothèque **TypeDoc** et quelles sont les opportunités qu'elle offre.

Pour ceux d'entre vous qui ne sont pas familiers avec **TypeDoc**, il s'agit d'une bibliothèque qui vous permet de générer une documentation API basée sur vos commentaires à partir de votre code source **TypeScript**.

Par défaut, il existe deux sorties possibles :

* _Site web statique_
* _Fichier JSON._

Si vous souhaitez en savoir plus sur la configuration et les conditions d'utilisation, veuillez vous référer au [**README**](https://github.com/TypeStrong/typedoc#typedoc).

### Le problème que j'ai rencontré

Le manque de documentation est un scénario vraiment courant, et c'était le problème auquel nous avons été confrontés. Comme la plupart d'entre vous le savent probablement, le débogage et l'exploration de tout type de logiciel à des fins exploratoires prennent du temps. C'est pourquoi j'ai décidé de contribuer et de partager les connaissances que j'ai acquises lors du développement d'un [plugin](https://github.com/IgniteUI/typedoc-plugin-localization) qui offre aux utilisateurs la possibilité de localiser leur documentation dans plusieurs langues.

Un bon exemple ici est la [documentation API japonaise](https://jp.infragistics.com/products/ignite-ui-angular/docs/typescript/latest/) que la bibliothèque [Ignite UI for Angular](https://github.com/IgniteUI/igniteui-angular) fournit.

Je vais donc donner une explication sommaire de comment **TypeDoc** fonctionne et quelle a été l'approche adoptée lors du développement de ce plugin.

Je n'entrerai pas dans les détails de comment la bibliothèque fonctionne. Au lieu de cela, je vais essayer d'exposer uniquement les aspects les plus importants du flux d'exécution qui, à mon avis, sont la base de l'« arbre » à partir duquel vous pouvez commencer à explorer et à vous divertir dans différentes « branches ».

Alors, sans perdre plus de temps, passons à la partie essentielle.

### Comment fonctionne TypeDoc.

#### Plusieurs composants/classes que vous devez connaître :

* [Application](https://typedoc.org/api/classes/application.html) **:**
La classe d'application principale par défaut.
* [Options](https://typedoc.org/api/classes/options.html) :
Agrège et contribue aux déclarations de configuration, déclarées par des composants ou des plugins. Analyse les valeurs des **options** à partir de diverses sources (fichier de configuration, ligne de commande, arguments, etc.)
* [Converter](https://typedoc.org/api/classes/converter.html) :
Compile les fichiers sources en utilisant **TypeScript** et convertit les symboles du compilateur en réflexions.
* [ProjectReflection](https://typedoc.org/api/classes/projectreflection.html) :
Une réflexion qui représente la **racine** du **projet**.
La réflexion du **projet** agit comme un index global. Vous pouvez recevoir toutes les réflexions et les fichiers sources du projet traité via cette **réflexion**.
* [Renderer](https://typedoc.org/api/classes/renderer.html) :
Le **renderer** traite une représentation de [ProjectReflection](https://typedoc.org/api/classes/projectreflection.html), en utilisant une instance de **BaseTheme** et écrit les documents HTML émis dans un répertoire de sortie.
Simplement, le **renderer** est utilisé pour générer la sortie de la documentation.
* [EventDispatcher](https://typedoc.org/api/classes/eventdispatcher.html) :
Une classe qui fournit un canal d'événements personnalisé.
Vous pouvez lier un rappel à un événement avec 'on' ou le supprimer avec 'off'.
* [Logger](https://typedoc.org/api/classes/logger.html) :
Le logger vous offre la possibilité de journaliser sans interruption tout type d'erreurs ou de messages comme succès, avertissement, log, verbeux, etc.
* [PluginHost](https://typedoc.org/api/classes/pluginhost.html) :
Responsable de la découverte et du chargement des plugins.

### Flux d'exécution de TypeDoc :

![Image](https://cdn-media-1.freecodecamp.org/images/0*xdTMvvjTlHlIwg44)

* L'application tente de charger tous les plugins **TypeDoc** en recherchant le mot-clé **'typedocplugin'** déclaré dans votre fichier **package.json**.

* [Converter](https://typedoc.org/api/classes/converter.html) **:** Utilise l'**API TypeScript** afin de compiler le projet référencé. Si des erreurs de compilation sont détectées dans le projet, le processus de conversion se termine avec l'erreur rencontrée.
À partir du diagramme ci-dessus, vous pouvez voir que pendant le processus **Resolve Reflections**, qui vient juste après le processus de compilation, l'[EventDispatcher](https://typedoc.org/api/classes/eventdispatcher.html) émet plusieurs événements qui sont une bonne condition préalable pour manipuler ou récupérer des données.
Une fois le processus de conversion terminé, nous recevons un objet [ProjectReflection](https://typedoc.org/api/classes/projectreflection.html) qui représente le projet lui-même avec tous les fichiers et leurs commentaires.
* [Options](https://typedoc.org/api/classes/options.html) **:** Détermine ce que sera la sortie de votre documentation en fonction des [options](https://github.com/TypeStrong/typedoc#arguments) que vous avez passées. Il existe deux variantes :
 1. **Fichier JSON** : Représente une version **stringifiée** de l'objet [ProjectReflection](https://typedoc.org/api/classes/projectreflection.html). C'est ce que fait la [Serialization](https://typedoc.org/api/classes/serializer.html)
 2. **Site web HTML statique**.
* [Renderer](https://typedoc.org/api/classes/renderer.html) **:** Tout d'abord, le **renderer** doit s'assurer que le **Theme** correspondant au **site web statique de sortie** et le **répertoire de sortie** sont configurés correctement. Si tout est correct, le **renderer** commence à mapper les **Reflections** avec les **Templates** du **Theme**.
Ici, l'[RendererEvent](https://typedoc.org/api/classes/rendererevent.html) émet deux événements [BeginRenderer](https://typedoc.org/api/classes/rendererevent.html#begin)/[EndRenderer](https://typedoc.org/api/classes/rendererevent.html#end) adaptés pour manipuler les données de sortie.
* **Fin du rendu** : C'est là que le processus se termine et que la sortie de la documentation générée est fournie.

Après cette explication sommaire et cette visualisation du flux d'exécution, nous sommes prêts à passer à la suite et à voir comment procéder réellement avec l'**extensibilité**.

### Étendre TypeDoc

#### Configurer le projet :

La toute première étape que nous devons franchir est de configurer un [projet node avec npm](https://www.wolfe.id.au/2014/02/01/getting-a-new-node-project-started-with-npm/).

Déclarez ce **mot-clé `typedocplugin`** dans votre **package.json** :

Ensuite, nous devons [exporter un module](https://nodejs.org/api/modules.html#modules_exports) qui servira de point d'entrée du projet. Comment **TypeDoc** charge-t-il les plugins ? Il recherche simplement dans tous les packages **node_modules** et leurs fichiers **package.json**, et lorsqu'il rencontre ce **mot-clé**, il [requiert](https://nodejs.org/api/modules.html#modules_require_id) ce package et l'exécute en tant que fonction en passant une référence à la classe principale **Application**.

Une fois toutes ces étapes effectuées, nous avons la liberté de manipuler le processus d'exécution et les données de sortie comme nous le souhaitons **?.**

### Approches et exemples

Comme je l'ai mentionné précédemment, toutes les connaissances que je partage dans cet article ont été acquises lors du développement d'un [plugin de localisation](https://github.com/IgniteUI/typedoc-plugin-localization), que je crois fermement tire pleinement parti de ce que **TypeDoc** offre comme opportunité d'extension. Ainsi, tous les exemples et approches ci-dessous sont inspirés par l'idée et la source de cette « créature ».

Pour comprendre comment cela fonctionne, vous pouvez parcourir le fichier [README](https://github.com/IgniteUI/typedoc-plugin-localization#typedoc-plugin-localization). Il suffit de comprendre les 3 premières étapes.

Commençons par le **module principal ([index.ts](https://github.com/IgniteUI/typedoc-plugin-localization/blob/master/index.ts))** que **typedoc** exécute une fois qu'il requiert le **plugin**. Comme nous le savons déjà, une référence à la classe **Application** par défaut est passée via le rappel **require**, où vous avez accès à tous ces composants principaux dont nous avons parlé dans la section **Comment TypeDoc fonctionne**.

Grâce à toutes ces références de composants, vous êtes en mesure d'enregistrer vos propres composants personnalisés, et selon ce qu'ils étendent, un ensemble différent d'événements est fourni.

Parfois, une simple théorie est insuffisante, alors passons à la suite et voyons comment les choses se passent en pratique.

Voici les quatre choses les plus importantes que nous allons examiner :

* _Enregistrer nos propres options._
* _Manipuler ou récupérer les données pendant le processus de conversion._
* _Manipuler ou récupérer les données pendant le processus de **renderer**._

#### Enregistrer notre propre option.

Comme nous le savons déjà, toutes les inscriptions de composants se font dans le **module principal**. La partie importante ici est que, pour enregistrer un composant dans le contexte des [options](https://typedoc.org/api/classes/options.html), vous devez **étendre** la classe [OptionsComponent](https://typedoc.org/api/classes/optionscomponent.html).

La définition personnalisée du [OptionComponent](https://github.com/IgniteUI/typedoc-plugin-localization/blob/master/components/options-component.ts) ressemble à ceci :

À la fin, vous devez ajouter cette déclaration dans les options que l'application fournit.

Vous pouvez vous référer au [README](https://github.com/IgniteUI/typedoc-plugin-localization#arguments) de l'extension/plugin dont nous parlons et voir quels types d'options sont exposés et comment ils contribuent au processus.

#### Manipuler ou récupérer les données pendant le processus de conversion

Le processus d'inscription ici est le même, mais au lieu d'étendre [OptionsComponent](https://typedoc.org/api/classes/optionscomponent.html), vous devez étendre [ConverterComponent](https://typedoc.org/api/classes/convertercomponent.html).

Comme vous l'avez probablement compris, la manière dont nous interagissons avec les données est via les **événements** que l'[EventDispatcher](https://typedoc.org/api/classes/eventdispatcher.html) **émet**. Ainsi, tous les **événements** auxquels vous pouvez vous abonner dans ce contexte peuvent être trouvés et accessibles via le [**Converter**](https://typedoc.org/api/classes/converter.html).

Nous allons examiner le contexte de la fonction de rappel de l'événement [EVENT_RESOLVE](https://typedoc.org/api/classes/converter.html#event_resolve). L'événement est déclenché chaque fois que **TypeDoc** résout une **Classe**, une **Interface** ou une **Enum** ou (une **méthode**, une **propriété**, etc.) faisant partie d'une **Classe**, d'une **Interface** ou d'une **Enum** particulière. Attendez, quoi ?

D'accord, c'est un peu confus, mais le concept est aussi simple que de parcourir un tableau.

Prenons l'exemple d'une classe simple.

L'événement émettra quatre fois en référençant chaque unité par cette déclaration, transformée en [DeclarationReflection](https://typedoc.org/api/classes/declarationreflection.html) :

1. **_Émet_** _la classe avec référence à tous ses [enfants](https://typedoc.org/api/classes/declarationreflection.html#children) (**b**, **c, d**)._
2. **_Émet_** _la propriété **b** avec référence à son [parent](https://typedoc.org/api/classes/declarationreflection.html#parent) (classe **A**)._
3. **_Émet_** _la propriété **c** avec référence à son [parent](https://typedoc.org/api/classes/declarationreflection.html#parent) (classe **A**)._
4. **_Émet_** _la méthode **d** avec référence à son [parent](https://typedoc.org/api/classes/declarationreflection.html#parent) (classe **A**)._

J'espère que tout est plus clair maintenant !

Voyons comment nous pouvons nous abonner aux événements émis :

Ensuite, dans le **callback de résolution**, vous pouvez voir comment les commentaires pour chaque **Classe**, **Enum** et **Interface** sont pris et stockés dans un fichier **JSON** qui représente chaque unité (**Classe**, **Enum**, **Interface**) séparément. Par exemple, si nous avons deux classes **A** et **B**, le dossier de sortie contiendrait deux fichiers **JSON**, **A.json** et **B.json**.

L'exemple suivant représente le moment où les commentaires pour chaque **getter** et **setter** sont récupérés, ce qui est l'unité suivante de la déclaration de **Classe** dont nous avons parlé un peu plus tôt.

Ce ne sont que des exemples, bien sûr — vous pouvez faire ce que vous voulez ici.

#### Manipuler ou récupérer les données pendant le processus de Renderer

Ici, nous avons le même concept que le **Convert**, mais bien sûr, nous devons étendre une autre classe. Devinez quoi — le nom de la classe est [RendererComponent](https://typedoc.org/api/classes/renderercomponent.html), et l'objet qui contient les références d'événements est [RendererEvent](https://typedoc.org/api/classes/rendererevent.html).

La variété des événements est moindre que celle du [Converter](https://typedoc.org/api/classes/converter.html), mais les informations que les événements fournissent sont plus que suffisantes.

L'abonnement est le même :

Ici, le comportement de l'événement [RendererEvent.BEGIN](https://typedoc.org/api/classes/rendererevent.html#begin) est un peu différent. Il est déclenché une seule fois lorsque le processus **Renderer** vient de commencer. Ensuite, toutes les **reflections** que le **Converter** a créées sont prises, et avec le « pouvoir » du **forEach**, nous parcourons chaque [DeclarationReflection](https://typedoc.org/api/classes/declarationreflection.html) et la traitons :

Que fait le processus ? Il prend simplement l'emplacement des fichiers **JSON** que le **Converter** a construits et remplace le contenu de ces **JSON** par le contenu de la réflexion.

L'exemple ici fait à nouveau référence à la manipulation des **getters** et **setters** pour la **Classe** actuelle :

Bien sûr, ici aussi, vous pouvez improviser et faire ce dont vous avez besoin.

### Conclusion

Ceci n'est probablement qu'un tiers de ce que fait le plugin. Il y a beaucoup plus que je peux montrer et exposer en termes de fonctionnalités. Par exemple, comment nous avons trouvé une solution pour manipuler les **chaînes de caractères codées en dur** dans notre [thème](https://github.com/IgniteUI/igniteui-angular/tree/master/extras/docs/themes/typedoc) personnalisé. Mais le but de ce blog est axé sur l'**extensibilité** et la **manipulation** des **données**. Donc, si vous avez d'autres questions ou intérêts, vous pouvez me le faire savoir dans les commentaires ci-dessous.