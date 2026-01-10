---
title: Comment augmenter votre productivité avec les fonctionnalités des DevTools
  multi-navigateurs
subtitle: ''
author: Uma Victor
co_authors: []
series: null
date: '2024-10-03T22:58:07.840Z'
originalURL: https://freecodecamp.org/news/cross-browser-devtools-features
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/JySoEnr-eOg/upload/e3e1bb6fdf9c408f7506093587114629.jpeg
tags:
- name: Browsers
  slug: browsers
- name: Developer Tools
  slug: developer-tools
- name: Web Development
  slug: web-development
- name: Productivity
  slug: productivity
seo_title: Comment augmenter votre productivité avec les fonctionnalités des DevTools
  multi-navigateurs
seo_desc: 'Building cross-browser web applications can be a difficult task, as many
  browsers offer few debugging tools that often vary between them. Fortunately, today
  most browsers support modern standards and provide helpful features for developers.

  Major bro...'
---

La création d'applications web multi-navigateurs peut être une tâche difficile, car de nombreux navigateurs offrent peu d'outils de débogage qui varient souvent entre eux. Heureusement, aujourd'hui, la plupart des navigateurs supportent les standards modernes et fournissent des fonctionnalités utiles pour les développeurs.

Les principaux navigateurs, tels que Chrome, Firefox et Edge, mettent continuellement à jour leurs outils de développement, chaque mise à jour pouvant apporter de nouvelles fonctionnalités aux développeurs web. Ces nouvelles fonctionnalités augmentent la facilité d'utilisation en ajoutant des interfaces utilisateur intuitives, des outils de débogage plus avancés et des outils d'analyse de performance améliorés.

Rester à jour avec ces changements vous permet d'utiliser vos outils de développement [DevTools](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Tools_and_setup/What_are_browser_developer_tools) à leur plein potentiel pour faciliter votre flux de travail et accélérer la livraison de vos applications web.

## Table des matières

* [Comment utiliser Scroll Into View dans DevTools](#heading-comment-utiliser-scroll-into-view-dans-devtools)
    
* [Comment utiliser les raccourcis de la console dans DevTools](#heading-comment-utiliser-les-raccourcis-de-la-console-dans-devtools)
    
* [Comment bloquer les requêtes de ressources pour les tests de sites web dans DevTools](#heading-comment-bloquer-les-requetes-de-ressources-pour-les-tests-de-sites-web-dans-devtools)
    
* [Comment modifier et renvoyer une requête réseau dans DevTools](#heading-comment-modifier-et-renvoyer-une-requete-reseau-dans-devtools)
    
* [Comment détecter le code source inutilisé dans DevTools](#heading-comment-detecter-le-code-source-inutilise-dans-devtools)
    
* [Comment activer l'arborescence d'accessibilité dans DevTools](#heading-comment-activer-larborescence-daccessibilite-dans-devtools)
    
* [Résumé](#heading-resume)
    

Dans cet article, nous allons découvrir quelques bonnes fonctionnalités des DevTools multi-navigateurs et discuter de leur utilisation.

Commençons !

## Comment utiliser Scroll Into View dans DevTools

Lors du débogage, il peut y avoir beaucoup de nœuds HTML à parcourir pour trouver où se situe votre problème. La plupart du temps, lorsque vous trouvez le nœud, vous ne le verrez pas tant que vous n'aurez pas fait défiler la page jusqu'à lui.

La fonctionnalité Scroll Into View permet de faire apparaître facilement le nœud DOM dans le [viewport](https://developer.mozilla.org/en-US/docs/Web/CSS/Viewport_concepts) en faisant un clic droit et en sélectionnant Scroll Into View dans Chrome, Firefox et Edge.

Cette fonctionnalité permet de gagner beaucoup de temps lors du débogage de problèmes CSS ou pour vérifier le placement correct des éléments sur une page, vous assurant de pouvoir localiser rapidement les éléments sur la page via les nœuds HTML sans avoir besoin de faire défiler manuellement de nombreuses lignes de contenu.

Dans l'image ci-dessous, nous essayons de trouver un élément `h2` qui est imbriqué dans plusieurs couches d'autres éléments.

![option scroll into view devtools](https://cdn.hashnode.com/res/hashnode/image/upload/v1727896981592/d326d8f8-6b79-4c0f-b7b6-d58d2f90344b.jpeg align="center")

Dans l'image ci-dessus, au lieu de faire défiler toute la page pour repérer l'élément `h2`, nous avons fait un clic droit et utilisé la fonctionnalité Scroll Into View pour faire apparaître instantanément l'élément `h2`. Nous pouvons étendre cette fonctionnalité pour faire d'autres choses avec l'élément une fois que nous avons fait défiler jusqu'à lui. Nous pouvons ajuster les propriétés CSS en temps réel via le panneau des styles et même trouver et corriger les problèmes de mise en page.

## Comment utiliser les raccourcis de la console dans DevTools

Il existe de nombreux raccourcis qui peuvent être utilisés dans la Console pour vous permettre, en tant que développeur, de déboguer plus rapidement. L'un d'eux est le raccourci `$_`. Ce raccourci retourne la valeur de la dernière [expression](https://en.wikipedia.org/wiki/Expression_\(computer_science\)) évaluée par la Console. Supposons, par exemple, que nous avons une fonction multiplicatrice :

Dans l'image ci-dessous, vous pouvez voir comment le raccourci `$_` est utilisé comme une variable spéciale dans la Console du navigateur pour stocker la dernière expression évaluée :

![raccourci $_ utilisé dans la Console](https://cdn.hashnode.com/res/hashnode/image/upload/v1727897503037/54aa559d-1ac2-4cf2-95f9-60f4d3c73520.png align="left")

Sans le raccourci `$_`, vous devriez soit retaper l'appel de fonction entier, soit stocker le résultat dans une variable comme ceci :

```javascript
let result = multiply(5)
result(4) // retourne 20
```

Dans le code ci-dessus, la fonction `multiply(5)` doit retourner une fonction et assigner la fonction à result, qui est ensuite appelée avec `4` comme paramètre `result(4)`.

Je suis sûr que vous pouvez voir comment cela introduit déjà une certaine redondance et des étapes supplémentaires qui peuvent être fastidieuses lorsque vous traitez des opérations plus complexes ou lorsque vous effectuez plusieurs étapes de calculs. C'est là que le raccourci `$_` brille. Lorsque nous exécutons le code `multiply(5)` dans la Console, une fonction est retournée et stockée dans la variable `$_` par la Console, à laquelle nous pouvons accéder en utilisant le raccourci `$_`.

Un autre raccourci consiste à utiliser `$0` pour accéder aux nœuds depuis la Console. `$0` peut être utilisé pour accéder au nœud actuellement sélectionné dans l'arborescence DOM depuis la Console. Lorsque vous inspectez une page web avec DevTools, vous parcourez souvent l'arborescence DOM dans le panneau Éléments pour trouver l'élément qui vous intéresse. Une fois que vous cliquez sur un élément dans ce panneau, DevTools suit interne cet élément, et il devient l'élément actuellement sélectionné.

Le `$0` est un raccourci qui fait référence à l'élément actuellement sélectionné dans la Console, vous pouvez donc le manipuler directement dans la Console sans avoir à écrire une requête pour le sélectionner à nouveau.

La capture d'écran ci-dessous montre comment nous pouvons utiliser `$0` dans la Console pour accéder au nœud sélectionné dans l'arborescence DOM et changer la couleur de fond en ce que nous voulons.

![raccourcis de la console](https://cdn.hashnode.com/res/hashnode/image/upload/v1727897399339/97ac2466-75b6-44ea-91b7-e0dee47e5ada.jpeg align="left")

Dans l'image ci-dessus, nous avons commencé par inspecter l'élément souhaité dans le panneau des éléments. Maintenant, au lieu de requêter à nouveau l'élément en utilisant `document.querySelector('#element')`, vous pouvez simplement utiliser `$0` pour le manipuler directement comme ceci :

```javascript
$0.style.backgroundColor = 'lightblue';
```

Ce code change la couleur de fond de la `<div>` sélectionnée en un bleu clair doux. Ce qui rend vraiment `$0` utile dans ce cas, c'est qu'il vous permet de faire référence directement à l'élément exact que vous avez choisi dans le DOM, vous assurant que vous travaillez avec le bon élément, même dans les cas où les éléments sont générés dynamiquement ou profondément imbriqués.

## Comment bloquer les requêtes de ressources pour les tests de sites web dans DevTools

La fonctionnalité de blocage des requêtes de ressources des DevTools est une fonctionnalité importante pour les développeurs web afin de tester comment leurs sites web se comportent lorsque certaines ressources ne peuvent pas être chargées.

Cette fonctionnalité vous permet de simuler des situations où une image, un JavaScript, un CSS ou un [domaine](https://en.wikipedia.org/wiki/Domain_name) entier devient inaccessible, et vous pouvez voir comment votre page web se comporterait dans cette situation.

Les ressources demandées par le navigateur ne sont pas toujours garanties d'être téléchargées, ce qui peut entraîner des expériences inattendues pour les utilisateurs de votre site web. Vous pouvez bloquer les requêtes vers une ressource sur Chrome, Firefox et Edge et tester comment votre site se comporte.

Sur Chrome et Edge :

* Dans le panneau Réseau, faites un clic droit sur la ressource que vous souhaitez bloquer et sélectionnez Bloquer l'URL de la requête.
    
* Actualisez le site web, et la ressource bloquée ne sera pas téléchargée et n'affectera pas la page web.
    

Dans l'image ci-dessous, nous utilisons l'option Bloquer l'URL de la requête dans l'onglet Réseau pour bloquer une requête CSS et voir à quoi ressemblera la page web si le fichier CSS sélectionné échoue à se charger.

![blocage des requêtes](https://cdn.hashnode.com/res/hashnode/image/upload/v1727897541622/739a0a25-09bd-4e25-86c0-e5d1a0264131.png align="left")

Dans l'image ci-dessus, nous pouvons voir toutes les requêtes réseau faites par la page web, y compris les requêtes pour les images, les fichiers CSS, les fichiers JavaScript, etc. Dans mon cas, j'ai filtré pour n'afficher que les fichiers CSS.

À partir de là, vous pouvez faire un clic droit sur le fichier CSS dans le panneau Réseau et sélectionner Bloquer l'URL de la requête. Cette action empêchera le navigateur de charger le fichier CSS spécifique la prochaine fois que la page sera actualisée.

En bloquant la requête, nous pouvons surveiller les comportements étranges et également mesurer comment l'absence de la ressource bloquée peut affecter le temps de chargement de la page et les performances.

Sur Firefox :

* Dans le panneau Réseau, faites un clic droit sur la ressource que vous souhaitez bloquer et sélectionnez Bloquer l'URL.
    
* Rechargez la page.
    

J'ai utilisé cela pour tester comment mon site se comporte lorsque je ne charge pas un fichier JavaScript particulier. Cette fonctionnalité peut aider les développeurs à déboguer les problèmes qui peuvent survenir lorsque les utilisateurs désactivent JavaScript.

## Comment modifier et renvoyer une requête réseau dans DevTools

L'une des fonctionnalités les plus cool des DevTools est la possibilité de modifier et de renvoyer des [requêtes réseau](https://en.wikipedia.org/wiki/Request%E2%80%93response) directement dans le navigateur. Cette fonctionnalité peut être vraiment utile pour déboguer un problème de requête réseau. Par exemple, des scénarios où vous souhaitez voir comment les modifications des paramètres de requête, des en-têtes ou du corps affectent la réponse du serveur, sans avoir à apporter de modifications au code frontal ou à redémarrer l'ensemble du processus de requête.

Lors de l'envoi d'une requête réseau, les requêtes envoyées à un service backend peuvent échouer ou ne pas répondre avec les données prévues. Il est fastidieux de devoir recharger toute la page pour réessayer la requête, c'est pourquoi la fonctionnalité Modifier et Renvoyer est utile.

Dans le navigateur Edge et Firefox, vous pouvez modifier et renvoyer une requête réseau en faisant un clic droit sur la requête que vous souhaitez modifier ou renvoyer et en sélectionnant Modifier et Renvoyer, comme dans l'image ci-dessous.

![Modifier et rejouer](https://cdn.hashnode.com/res/hashnode/image/upload/v1727897585816/68169a1f-987c-457a-a8ee-4335c2d88793.png align="left")

Dans l'image ci-dessus, nous avons essayé de nous connecter à un site web. Lorsque l'utilisateur soumet ses identifiants, le formulaire envoie une requête `POST` à un point de terminaison API, `/auth/login`, avec le nom d'utilisateur et le mot de passe de l'utilisateur.

Parfois, le serveur peut retourner une erreur `400` Bad Request, et pour déboguer l'erreur et découvrir pourquoi, nous devons réessayer la requête. Nous ne voulons pas continuer à remplir le formulaire, nous utilisons donc la fonctionnalité Modifier et Renvoyer comme montré ci-dessous.

![modifier les requêtes xhr](https://cdn.hashnode.com/res/hashnode/image/upload/v1727897620865/48eeb4fa-4bc4-44fb-b274-a23c5b037e1d.png align="left")

L'image ci-dessus est la Console réseau ou une barre latérale qui s'ouvrira lorsque vous cliquez sur Modifier et Renvoyer, montrant les détails de la requête. Ici, vous pouvez modifier :

* URL : Si nécessaire, vous pouvez modifier l'URL ou ajouter des paramètres de requête.
    
* En-têtes : Vous pourriez remarquer un en-tête Content-Type manquant ou incorrect, que vous pouvez corriger ici.
    
* Corps : C'est ici que vous pouvez ajuster la charge utile, comme corriger les champs de nom d'utilisateur ou de mot de passe.
    

Dans les navigateurs Chrome, la fonctionnalité de modification et de renvoi ne fonctionne que pour les requêtes [XHR](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest), et vous pouvez l'utiliser en faisant un clic droit sur la requête et en sélectionnant rejouer.

## Comment détecter le code source inutilisé dans DevTools

L'outil Coverage dans DevTools permet aux développeurs de repérer les zones de leurs fichiers JavaScript et CSS qui restent inutilisées pendant les étapes de chargement et d'interaction d'une page web. C'est une fonctionnalité importante pour améliorer les performances web en réduisant la taille des fichiers et en éliminant le code inutile pour des temps de chargement de page plus rapides et une meilleure expérience utilisateur.

Supprimer le code JS et CSS inutilisé est un excellent moyen d'économiser la bande passante de vos utilisateurs. L'outil Coverage vous permet de trouver le code inutilisé dans votre code source, et soit de le supprimer, soit de le différer jusqu'à ce que le morceau de code soit nécessaire.

Sur Chrome et Edge :

* Dans DevTools, appuyez sur `Ctrl/cmd+Shift+P`, tapez coverage et sélectionnez Start instrumenting coverage, actualisez la page, puis appuyez sur entrer.
    
* Vous verrez un tableau de fichiers JS et CSS avec une colonne d'octets inutilisés.
    
* Cliquez sur l'un des fichiers pour l'ouvrir. La ligne sur le côté indique quelle section de code n'est pas inutilisée en rouge.
    

Dans l'image ci-dessous, nous identifions le code CSS inutilisé pour potentiellement le supprimer ou différer le chargement du code.

![Supprimer le code inutilisé](https://cdn.hashnode.com/res/hashnode/image/upload/v1727898041299/ef5feb00-38db-4893-90db-275721c26399.png align="left")

Dans l'image ci-dessus, après l'enregistrement, l'outil Coverage affichera une liste des fichiers CSS et JavaScript chargés par la page, ainsi que des métriques détaillées :

* Total Bytes : La taille du fichier.
    
* Unused Bytes : Le nombre d'octets dans le fichier qui n'ont pas été utilisés.
    
* Visualisation de l'utilisation : Une barre visuelle représentant la proportion de code utilisé par rapport au code inutilisé.
    

Sur Safari : Dans le panneau Sources, ouvrez la barre de navigation latérale de gauche et cliquez sur n'importe quel fichier JS. En haut à droite de la barre d'outils, cliquez sur l'icône de couverture `c` et actualisez votre page. Vous pourrez voir que les sections de code non exécutées sont grisées.

## Comment activer l'arborescence d'accessibilité dans DevTools

L'[arborescence d'accessibilité](https://developer.mozilla.org/en-US/docs/Glossary/Accessibility_tree) est similaire à l'arborescence DOM des éléments et est utilisée par les technologies d'assistance telles que les lecteurs d'écran pour lire le contenu web. Les développeurs peuvent utiliser cette fonctionnalité pour déboguer les problèmes d'accessibilité sur leurs sites web. Les navigateurs Chromium utilisent l'[API d'accessibilité de Chrome](https://developer.chrome.com/docs/extensions/reference/api/accessibilityFeatures) pour rendre cela possible, tandis que Firefox dispose de son propre outil d'accessibilité.

Sur Chrome et Edge :

* Dans la page des paramètres, sélectionnez l'onglet Expériences.
    
* Cochez la case pour l'option Activer l'affichage complet de l'arborescence d'accessibilité dans le panneau Éléments.
    
* Actualisez DevTools et allez dans l'outil Éléments.
    
* Dans le coin supérieur droit de la vue des éléments, cliquez sur Passer à la vue de l'arborescence DOM.
    

Par exemple, dans l'image ci-dessous, nous vérifions si les liens et les boutons de notre site web sont reconnus correctement et accessibles aux utilisateurs qui dépendent des lecteurs d'écran :

![Activer l'arborescence d'accessibilité](https://cdn.hashnode.com/res/hashnode/image/upload/v1727898388525/1a73f242-5ccd-48ea-b167-440205285ba4.png align="left")

Avec l'arborescence d'accessibilité activée, vous pouvez voir une version simplifiée de l'arborescence DOM, centrée sur les éléments pertinents pour l'accessibilité. Lorsque vous sélectionnez un élément dans l'arborescence d'accessibilité pour voir ses propriétés, l'arborescence affiche le rôle de l'élément, son nom et d'autres attributs importants, tels que aria-label s'ils sont présents.

Vous verrez également si l'élément est focusable et quelles sont ses propriétés d'accessibilité calculées.

Cela aide beaucoup car si l'élément n'apparaît pas correctement dans l'arborescence d'accessibilité ou manque d'attributs essentiels, vous devrez peut-être ajuster votre HTML ou les attributs [ARIA](https://www.w3.org/WAI/standards-guidelines/aria/) pour améliorer l'accessibilité.

Sur Firefox :

* Dans les DevTools de Firefox, cliquez sur l'onglet accessibilité et développez le nœud document.
    
* Vous pouvez cliquer sur différents nœuds pour voir leurs propriétés.
    
* Les problèmes d'accessibilité pour les nœuds seront affichés dans l'onglet Vérifications.
    

## Résumé

En résumé, rester à jour avec les dernières fonctionnalités des DevTools multi-navigateurs vous fera gagner du temps en tant que développeur web. Cet article aborde des conseils d'inspection d'éléments, quelques raccourcis de la Console pour faciliter votre processus de débogage, et quelques conseils utiles pour la surveillance du réseau.

Espérons que vous continuerez à explorer et à utiliser davantage de fonctionnalités des DevTools pour améliorer votre expérience de développeur.