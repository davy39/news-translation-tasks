---
title: Comment mettre à l'échelle les vues Elm avec des types de vue maître
subtitle: ''
author: Cedd Burge
co_authors: []
series: null
date: '2019-07-18T07:29:29.000Z'
originalURL: https://freecodecamp.org/news/scaling-elm-views-with-master-view-types
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/2014-Haute-Route-Imperiale51.JPG
tags:
- name: ELM
  slug: elm
- name: scaling
  slug: scaling
seo_title: Comment mettre à l'échelle les vues Elm avec des types de vue maître
seo_desc: 'A concept to help Elm Views scale as applications grow larger and more
  complicated.

  In Elm, there are a lot of great ways to scale the Model, and update, but there
  is more controversy around scaling the view. A lot of the debate is around Reusable
  Vi...'
---

Un concept pour aider les vues Elm à évoluer à mesure que les applications deviennent plus grandes et plus complexes.

Dans Elm, il existe de nombreuses façons de mettre à l'échelle le `Model` et `update`, mais il y a plus de controverse autour de la mise à l'échelle de la `view`. Une grande partie du débat porte sur [les vues réutilisables versus les composants](https://gist.github.com/rofrol/fd46e9570728193fddcc234094a0bd99#reusable-views-instead-of-nested-components). Les composants ne sont pas recommandés, mais beaucoup de gens plaident encore en leur faveur. Cet article présente une idée qui, espérons-le, renforce l'argument en faveur des vues réutilisables.

Dans presque tous les cas, le problème de mise à l'échelle se résume à l'application de la cohérence, ce qui signifie généralement permettre aux vues enfants d'apporter quelques ajustements à la vue maître, tout en ne permettant pas aux vues enfants de faire un désordre.

Je vais utiliser l'excellente application [Real World](https://github.com/rtfeldman/elm-spa-example) de Richard Feldman (spécifiquement écrite pour démontrer la mise à l'échelle dans Elm) comme exemple, car elle contient beaucoup de techniques actuelles de meilleures pratiques, elle est bien connue (2000+ étoiles et 300+ forks) et Richard est un expert Elm bien connu.

Je vais suggérer quelques améliorations à ce code, donc je veux être clair à ce stade que je ne manque de respect à personne (je parierais de grosses sommes d'argent qu'il l'a fait en environ un dixième du temps qu'il m'aurait fallu !). Vous pourriez aussi argumenter que les problèmes sont mineurs et ne valent pas la peine d'être corrigés. En fin de compte, cette décision vous appartient, mais à la fin de l'article, j'espère vous persuader qu'il y a des problèmes et qu'ils sont corrigibles si vous pensez que cela en vaut la peine.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/ski-touring.jpeg)

## Fonctions de vue maître avec conditionnelles

Une option consiste à définir une fonction de vue maître. Cette fonction prend en charge les préoccupations partagées, comme la barre d'en-tête et la disposition générale. Ensuite, elle appelle les fonctions de vue enfant en fonction de la vue actuelle et/ou a des paramètres pour contrôler le comportement spécifique de l'enfant.

Cela fonctionne, mais peut rapidement conduire à :

* Une explosion de paramètres, potentiellement forçant vos vues enfants à retourner beaucoup de choses dont elles ne se soucient pas.
* Un mélange de responsabilités entre les vues maître et enfant.
* Du code supplémentaire et de la duplication.

Dans l'application Real World, un paramètre de type `Page` est passé à la vue maître afin qu'elle puisse rendre un lien de la barre de navigation actif. Il y a une [grande instruction case](https://github.com/rtfeldman/elm-spa-example/blob/b5064c6ef0fde3395a7299f238acf68f93e71d03/src/Page.elm#L113) qui utilise ce paramètre pour déterminer quel lien est actif, et il serait beaucoup plus facile pour l'enfant de simplement spécifier cela.

La [ligne ci-dessous](https://github.com/rtfeldman/elm-spa-example/blob/b5064c6ef0fde3395a7299f238acf68f93e71d03/src/Main.elm#L85) montre la vue maître passant `Page.Home`, qui doit correspondre à `Home.view home`. Il est facile de se tromper, il n'y a pas d'aide du compilateur ou du système de types, et vraiment, c'est la responsabilité de la vue enfant de spécifier cela.

`viewPage Page.Home GotHomeMsg (Home.view home)`

Il y a une certaine duplication lors de la [création du NavBarLink Html](https://github.com/rtfeldman/elm-spa-example/blob/b5064c6ef0fde3395a7299f238acf68f93e71d03/src/Page.elm#L62), et la fonction `linkTo` acceptera n'importe quel Html, bien que seul un Html très particulier soit valide.

## Convention et confiance

Une autre possibilité est que les vues enfants soient responsables de la cohérence des éléments partagés, par convention et confiance.

On pourrait dire que cela se produit également dans l'application Real World. Les vues [Home](https://github.com/rtfeldman/elm-spa-example/blob/b5064c6ef0fde3395a7299f238acf68f93e71d03/src/Page/Home.elm#L146), [Article](https://github.com/rtfeldman/elm-spa-example/blob/b5064c6ef0fde3395a7299f238acf68f93e71d03/src/Page/Article.elm#L119) et [Profile](https://github.com/rtfeldman/elm-spa-example/blob/b5064c6ef0fde3395a7299f238acf68f93e71d03/src/Page/Profile.elm#L197) ont toutes le concept de bannière. La bannière est différente dans chaque vue, mais elle est censée être un élément visuel cohérent et reconnaissable (essentiellement, c'est le titre/en-tête de la vue). Les vues ne partagent aucun code pour ces bannières, et en conséquence, elles n'ont pas la même taille ou la même couleur. Vous pourriez théoriquement essayer d'imposer une convention en utilisant des tests, mais ce serait difficile et probablement pas utile.

## Fonctions d'assistance

Une autre possibilité est que les vues enfants soient responsables de la cohérence des éléments partagés, mais en utilisant certaines fonctions d'assistance. C'est définitivement un pas en avant, et c'est probablement la solution la plus courante que je vois dans la nature. Les fonctions peuvent être placées dans le même fichier et être proches les unes des autres. Cela rend plus facile de voir qu'elles sont liées et représentent le même élément visuel, et plus facile de les rendre cohérentes.

Cependant, il y a encore quelques inconvénients. Le principal est que les vues enfants doivent savoir utiliser les fonctions d'assistance, et il n'y a rien qui impose cela. Ce n'est pas un gros problème lorsque vous n'avez qu'un seul élément partagé et une seule fonction à appeler, mais à mesure que les applications deviennent plus grandes, vous finissez par avoir une explosion combinatoire de différences dans les éléments visuels partagés. La plupart des gens maîtrisent cela en fournissant un certain nombre de petites fonctions ciblées pour les diverses différences. Ensuite, la vue enfant doit connaître toutes ces fonctions, et comment les composer, et il n'y a pas d'aide du compilateur.

Encore une fois, cela se produit probablement dans l'application Real World : par exemple dans [cette partie de la fonction Profile.view](https://github.com/rtfeldman/elm-spa-example/blob/b5064c6ef0fde3395a7299f238acf68f93e71d03/src/Page/Profile.elm#L211), qui doit savoir comment utiliser les fonctions d'assistance `viewTabs`, `Feed.viewArticles` et `Feed.viewPagination`, et quel Html elles doivent contenir.

## Mise à l'échelle avec les types de vue maître

Pour surmonter ces problèmes, je propose d'utiliser un `Type` pour définir la structure de votre site (je nomme plutôt pompeusement cela un "Type de Vue Maître"). Les vues enfants retournent ensuite ce type, et la vue maître le prend comme paramètre et retourne le html.

Pour les exemples de l'application Real World que nous avons examinés, le Type de Vue Maître est ci-dessous (`Viewer` est la personne qui regarde la page dans l'application Real World). Vous pourriez avoir des types de bannière plus généraux ici, comme AvatarBanner, ou même IconBanner (au lieu de ViewerBanner) selon votre domaine.

```elm
type alias Page =
    {   activeNavBarLink: NavBarLink
		, banner: Banner
        , body: Html Msg
    }
	
type Banner =
    TextBanner TextBannerProperties
    | ViewerBanner Viewer
    | ArticleBanner Viewer ArticlePreview

type NavBarLink =
    NavBarLink NavBarLinkProperties

```

Pour démontrer cela, j'ai créé un dépôt avec uniquement les [parties En-tête et Bannière de l'application Real World](https://github.com/ceddlyburge/elm-without-master-view-types) puis créé un nouveau dépôt après avoir refactorisé pour utiliser un [Type de Page Maître](https://github.com/ceddlyburge/elm-master-view-types/blob/master/src/Page.elm), un [Type de NavBarLink](https://github.com/ceddlyburge/elm-master-view-types/blob/master/src/NavBarLink.elm) et un [Type de Bannière](https://github.com/ceddlyburge/elm-master-view-types/blob/master/src/Banner.elm). Vous pouvez parcourir le code pour vous faire une idée de son fonctionnement.

À mon avis, l'utilisation d'un Type de Page Maître présente les avantages suivants :

* L'écriture du code de la vue maître est plus facile
* L'écriture du code de la vue enfant est plus facile
* La communication et la compréhension sont améliorées, car les concepts d'UI ont maintenant des noms
* La thématisation / la refonte d'un site est beaucoup plus facile
* Les packages Elm peuvent fournir des modèles d'UI

La vue maître peut définir précisément ce qu'elle acceptera / prendra en charge via les types, avec des [types d'union](https://guide.elm-lang.org/types/custom_types.html) et des [types opaques](https://medium.com/@ckoster22/advanced-types-in-elm-opaque-types-ec5ec3b84ed2). Les combinaisons non supportées peuvent être rendues non représentables ou non créables.

Dans mon dépôt d'exemple, le [type NavBarLink est opaque](https://github.com/ceddlyburge/elm-master-view-types/blob/master/src/NavBarLink.elm), donc il n'est possible de créer que des NavBarLinks supportés (`home`, `article` et `viewer`). De manière similaire, [Banner est un type d'union](https://github.com/ceddlyburge/elm-master-view-types/blob/master/src/Banner.elm), ce qui signifie que seules les variantes supportées peuvent être représentées.

Il serait possible pour un programmeur de simplement changer ces fichiers, mais un programmeur compétent reconnaîtrait les motifs et les suivrait. Si cela ne suffit pas et que vous êtes paranoïaque, vous pouvez alors exiger un examen de code plus strict sur de tels fichiers, en tirant potentiellement parti de la fonctionnalité [CODEOWNERS](https://help.github.com/en/articles/about-code-owners) sur GitHub et GitLab. Dans l'extrême, vous pouvez fournir les modules via un package elm, et restreindre l'accès en push au dépôt sous-jacent.

Les vues enfants n'ont pas à faire plus que créer une instance des types. Les fonctions d'assistance retournent toutes des types, il est donc facile de voir quelles fonctions peuvent être utilisées dans un contexte particulier, et il est impossible d'utiliser des fonctions dans le mauvais contexte. Par exemple, si une fonction retourne un `HeaderBarLink`, il est impossible d'utiliser par erreur cette fonction pour créer un lien dans le `FooterBar`, ou ailleurs sur la page. Les vues enfants peuvent également laisser une partie de la complexité à la vue maître. Par exemple, la vue enfant peut définir une liste d'options parmi lesquelles choisir, et la vue maître peut rendre cela en utilisant des boutons, une liste déroulante ou une liste d'autocomplétion, selon le nombre d'options.

Le type de page maître fournit également des noms pour les concepts d'UI, qui peuvent ensuite être discutés. Par exemple, un designer pourrait dire "Déplaçons les NavBarLinks vers le côté gauche", et tout le monde saurait ce qu'il veut dire. Un propriétaire de produit pourrait dire "Créons une nouvelle page avec un IconBanner, et nous utiliserons l'API météo actuelle pour l'icône" et encore une fois, tout le monde saurait ce qu'ils veulent dire. Vous pouvez consulter cet [excellent article de thoughtworks](https://www.thoughtworks.com/insights/blog/ui-components-design) pour plus de détails à ce sujet.

Puisque la responsabilité de transformer le Type de Vue Maître en html est entièrement au même endroit, il est facile d'apporter des changements drastiques à l'apparence et à la convivialité d'un site web, et de faire de la thématisation. Ces changements et thèmes peuvent modifier le Css _et le Html_, ce que les techniques de thématisation normales ne peuvent tout simplement pas faire. Pragmatiquement, votre Type de Vue Maître aura souvent une propriété `body: Html Msg` (pour permettre aux vues enfants une flexibilité complète sur les parties spécifiques à l'enfant de la page) donc il y aurait encore un peu de code à corriger, mais ce sera définitivement beaucoup plus facile.

Enfin, cela ouvre la possibilité de fournir des thèmes et des mises en page de sites prêts à l'emploi sous forme de packages. Cela vous permettrait de simplement faire ce qui suit pour obtenir une application fonctionnelle, complète avec la mise en page et le style :

* `create-elm-app`
* `elm install elm-bootstrap-starter-template`
* Écrire un peu de code pour créer le Type de Page Maître
* `elm-app start`

Les entreprises pourraient créer des packages comme ceux-ci pour garantir une apparence et une convivialité cohérentes dans leurs applications. Des designs et des mises en page open source pourraient émerger et devenir courants, de la même manière que Bootstrap a révolutionné la conception html et css. Les développeurs avec des compétences limitées en design (comme moi) pourraient se concentrer sur les parties qu'ils maîtrisent le mieux (la logique), mais toujours produire des sites web élégants en utilisant ces packages.

Pour démontrer cela, j'ai créé un [package de vue maître de démarrage bootstrap](https://package.elm-lang.org/packages/ceddlyburge/elm-bootstrap-starter-master-view/latest/). Il imite la mise en page et le design du [modèle de démarrage bootstrap](https://getbootstrap.com/docs/4.0/examples/starter-template/). J'ai ensuite utilisé ce package dans une application de démonstration elm. Vous pouvez [parcourir l'application de démonstration](https://elm-bootstrap-starter.netlify.com/) pour voir à quoi elle ressemble, et [voir la source](https://github.com/ceddlyburge/elm-bootstrap-starter-demo) pour voir comment elle fonctionne.

Tous ces avantages viennent à un coût faible ou négatif. Il y a un peu plus de code pour les nouveaux types, mais une certaine duplication est supprimée. Vous pouvez consulter la source des dépôts de l'application Real World [avant](https://github.com/ceddlyburge/elm-without-master-view-types) et [après la refactorisation pour utiliser un Type de Page Maître](https://github.com/ceddlyburge/elm-master-view-types) pour plus de détails.

## Conclusions

Les Types de Vue Maître apportent de nombreux avantages (le code de vue est plus facile à écrire et à maintenir, les concepts d'UI sont nommés et les packages d'UI sont possibles) pour un coût faible ou nul. Ils devraient améliorer le code de toute application Elm qui a des problèmes autour de l'application de la cohérence (tout en permettant la flexibilité) dans leur code de vue, ce qui, selon mon expérience, est le cas de la plupart des applications moyennes et grandes.