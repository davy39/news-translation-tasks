---
title: Comment créer des applications mobiles multiplateformes en utilisant rien de
  plus qu'un balisage JSON
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-12T21:17:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-cross-platform-mobile-apps-using-nothing-more-than-a-json-markup-f493abec1873
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9pjDQEEtAL-QAqXOf7kmBA.png
tags:
- name: mobile
  slug: mobile
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment créer des applications mobiles multiplateformes en utilisant rien
  de plus qu'un balisage JSON
seo_desc: 'By Ethan

  For the past few months, I’ve been working on a new way to build cross-platform,
  native iOS and Android apps called Jasonette.

  It lets you describe an entire app with nothing but a single JSON markup.

  If your app consists entirely of JSON, i...'
---

Par Ethan

Depuis quelques mois, je travaille sur une nouvelle façon de créer des applications **multiplateformes et natives [iOS](https://github.com/Jasonette/JASONETTE-iOS) et [Android](https://github.com/Jasonette/JASONETTE-Android)** appelées [Jasonette](https://www.jasonette.com).

Cela vous permet de décrire une application entière avec rien de plus qu'un simple balisage JSON.

Si votre application est entièrement composée de JSON, elle peut être traitée comme n'importe quelle autre donnée. Et elle peut être servie à distance depuis le cloud à la demande.

La logique de l'application n'a plus besoin d'être codée en dur sur l'appareil, et vous pouvez la mettre à jour autant que vous le souhaitez simplement en mettant à jour votre JSON côté serveur. Votre application sera fraîchement chargée depuis le serveur à chaque ouverture.

Regardez la vidéo ci-dessous pour une rapide introduction :

Jasonette a de nombreuses parties différentes. Vous pouvez exprimer des fonctions, des templates, des styles, et plus encore, tout en utilisant [un balisage JSON](https://docs.jasonette.com). Et en conséquence, vous pouvez écrire une application mobile native super sophistiquée de manière entièrement [Modèle — Vue — Contrôleur](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller).

Dans cet article, je vais vous montrer spécifiquement la partie « Vue » :

1. Comment Jasonette exprime divers motifs d'interface utilisateur multiplateformes en JSON.
2. Comment il implémente ces mappages JSON-to-Native en interne.

### Structure de base

Sous le capot, Jasonette fonctionne de manière similaire à un navigateur web. Mais au lieu d'interpréter un balisage HTML et de dessiner une vue web, Jasonette récupère un balisage JSON et construit une vue native, à la volée.

Le balisage est simplement un fichier JSON qui suit certaines [conventions prédéfinies](http://docs.jasonette.com/). Tout d'abord, il commence par une clé `$jason`, qui a deux enfants : `head` et `body`, et ressemble à ceci :

```
{  "$jason": {    "head": {      .. métadonnées sur le document ...    },    "body": {      .. contenu réel à afficher sur la vue ..    }  }}
```

### Philosophie de conception

Lorsque j'ai commencé à concevoir la syntaxe JSON pour décrire les vues natives, j'avais quelques contraintes en tête :

1. **Native** — Il y a une raison pour laquelle iOS et Android ont créé leurs propres systèmes de mise en page natifs. Les systèmes de mise en page conçus pour l'ère du bureau ne se traduisent pas toujours bien dans le monde des petits appareils. La syntaxe doit exprimer la mise en page sous-jacente de la manière la plus native possible pour les mobiles.
2. **Multiplateforme** — Pourtant, elle doit être multiplateforme. Par exemple, iOS a quelque chose appelé [autolayout](https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/AutolayoutPG) et [visual format language](https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/AutolayoutPG/VisualFormatLanguage.html), mais ceux-ci ne sont pas implémentés nativement sur Android, donc ce n'est pas la bonne solution.
3. **Simple mais expressif** — Il doit être facilement exprimé dans un format JSON simple et facile à composer dans une structure sophistiquée.

Lorsque vous regardez comment la plupart des applications mobiles sont construites, elles se résument toutes à un petit nombre de motifs d'interface courants :

1. Liste déroulante verticale
2. Liste déroulante horizontale
3. Positionnement absolu
4. Grille

Regardons les trois premiers, car ils sont les plus largement utilisés.

### 1. Sections — Description des listes déroulantes

Le motif d'interface utilisateur le plus fréquemment utilisé est les **listes déroulantes**. Dans Jasonette, nous les appelons `sections`.

Il existe deux types de sections : **Vertical** et **Horizontal**. Les sections verticales défilent verticalement, et les sections horizontales horizontalement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wFCoMe1t9-cQC0_n6qzJDw.gif)

![Image](https://cdn-media-1.freecodecamp.org/images/1*bUsEMmJFz-Wezi0IBKp8NA.gif)
_Une seule section verticale avec plusieurs éléments (Gauche) — Plusieurs sections horizontales (Droite)_

#### Implémentation — Sections verticales

C'est probablement l'interface utilisateur la plus fréquemment utilisée pour afficher des données sur les appareils mobiles. Sur iOS, Jasonette l'implémente avec [UITableView](https://developer.apple.com/reference/uikit/uitableview). Sur Android, elle est implémentée avec [RecyclerView](https://developer.android.com/reference/android/support/v7/widget/RecyclerView.html).

```
{  "body": {    "sections": [{      "items": [        {"type": "label", "text": "Item 1"},        {"type": "label", "text": "Item 2"},        {"type": "label", "text": "Item 3"}      ]    }]  }}
```

Sur iOS, le balisage JSON ci-dessus crée une UITableView avec trois [UITableViewCells](https://developer.apple.com/reference/uikit/uitableviewcell), chacune contenant une [UILabel](https://developer.apple.com/reference/uikit/uilabel), avec les attributs `text` correspondants.

Sur Android, il crée une RecyclerView avec trois éléments, chacun étant une [TextView](https://developer.android.com/reference/android/widget/TextView.html) qui affiche les attributs `text` correspondants.

Tous ceux-ci sont construits par programmation sans aucune utilisation de [Storyboards](https://developer.apple.com/library/content/documentation/General/Conceptual/Devpedia-CocoaApp/Storyboard.html) (iOS) ou de [fichiers de mise en page XML](https://developer.android.com/guide/topics/resources/layout-resource.html) (Android) afin de s'assurer que chaque détail est programmable dynamiquement.

#### Implémentation — Sections horizontales

En termes de syntaxe, les sections horizontales ne sont pas très différentes, tout ce que vous avez à faire est de définir le **type** comme **"horizontal"**, et les éléments s'affichent horizontalement.

```
{  "body": {    "sections": [{      "type": "horizontal",      "items": [        {"type": "label", "text": "Item 1"},        {"type": "label", "text": "Item 2"},        {"type": "label", "text": "Item 3"}      ]    }]  }}
```

* Remarque : La syntaxe pour la section horizontale est simple, mais en interne, elle est en fait assez complexe. Les sections horizontales sur iOS ont été implémentées avec [UICollectionView](https://developer.apple.com/reference/uikit/uicollectionview). C'est une technique bien connue, mais en gros, une UICollectionView à défilement horizontal est intégrée dans sa parent UITableView (qui défile verticalement). Et sur Android, elle est implémentée de manière similaire, mais en utilisant des RecyclerViews imbriquées.

### 2. Items — Description de la mise en page dans chaque unité de défilement

Maintenant que nous comprenons comment la vue de niveau supérieur est structurée, regardons les `items`. Chaque section est composée de plusieurs unités de `items` défilables. Notez que chaque item a une dimension fixe et rien à l'intérieur de l'item lui-même ne défile.

Un item peut être :

* Juste un seul composant comme un `label`, `image`, `button`, `textarea`, etc.
* Une combinaison de tous ces composants

L'implémentation de cette partie n'était pas aussi simple que l'implémentation des `sections`, car j'ai dû choisir un moyen **multiplateforme, natif, simple et expressif** pour former une mise en page super sophistiquée.

Heureusement, iOS et Android ont des systèmes de mise en page natifs très similaires appelés [**UIStackView**](https://developer.apple.com/reference/uikit/uistackview) et [**LinearLayout**](https://developer.android.com/reference/android/widget/LinearLayout.html), respectivement. Et ces schémas de mise en page sont à leur tour similaires à [**CSS Flexbox**](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Using_CSS_flexible_boxes), donc je dirais que c'est aussi multiplateforme que possible.

Enfin, ces systèmes de mise en page sont infiniment composables. Comme on peut le voir ci-dessous, vous pouvez créer une mise en page verticale, une mise en page horizontale, ou imbriquer une mise en page verticale dans une mise en page horizontale, et ainsi de suite, de manière récursive.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yTWO4ovQpMQ6IgQEnn0dZg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*tY1RHjSm3Tcq0fH8i14QjQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*RNk5pUFc00k9mMfMJT5Gnw.png)

Pour créer une mise en page verticale, vous définissez le type comme **vertical**, puis vous définissez ses **components** :

```
{  "items": [{    "type": "vertical",    "components": [      {        "type": "label",        "text": "First"      },       {        "type": "label",        "text": "Second"      },       {        "type": "label",        "text": "Third"      }    ]  }]}
```

Même chose avec la mise en page horizontale. Il suffit de définir le type comme **horizontal** à la place :

```
{  "items": [{    "type": "horizontal",    "components": [      {        "type": "image",        "url": "http://i.giphy.com/LXONhtCmN32YU.gif"      },       {        "type": "label",        "text": "Rick"      }    ]  }]}
```

L'imbrication des mises en page est aussi simple que de spécifier une mise en page comme composant d'une autre mise en page.

```
{  "items": [{    "type": "horizontal",    "components": [      {        "type": "image",        "url": "http://i.giphy.com/LXONhtCmN32YU.gif"      },       {        "type": "vertical",        "components": [{          "type": "label",          "text": "User"        }, {          "type": "label",          "text": "Rick"        }]      }    ]  }]}
```

Je n'ai pas parlé de la fonctionnalité de style ici pour des raisons de brièveté, mais vous pouvez styliser chaque composant individuel ainsi que la mise en page elle-même pour vous assurer que la mise en page ressemble exactement à ce que vous vouliez. Tout ce que vous avez à faire est d'ajouter des objets `style` décrivant `font`, `size`, `width`, `height`, `color`, `background`, `corner_radius`, `opacity`, etc.

### 3. Layers — AKA **"positionnement absolu"**

Parfois, vous pouvez vouloir positionner des éléments à des endroits précis de l'écran sans défilement. En termes CSS, nous appellerions cela **"positionnement absolu"**. Jasonette supporte cela à travers ce qu'on appelle `layers`.

Actuellement, les layers supportent deux types de composants enfants : `image` et `label`. Vous pouvez placer ces composants n'importe où sur l'écran de cette manière. Voici un exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/1*BnNhx6BaYXIbEbM-ksdMVQ.gif)
_Une application Jasonette avec des éléments de layer_

Dans cet exemple, nous avons deux labels (les messages de température et de météo) et une image (l'icône de l'appareil photo) sur l'écran, dont les coordonnées ont été explicitement définies pour s'assurer qu'ils restent en place sans défilement. Le balisage ressemblerait à ceci :

```
{  "$jason": {    "body": {      "style": {        "background": "camera"      },      "layers": [        {          "type": "label",          "text": "22°C",          "style": {            "font": "HelveticaNeue-Light",            "size": "20",            "top": "50",            "left": "50%-100",            "width": "200",            "align": "center"          }        },        {          "type": "label",          "text": "few clouds",          "style": {            "font": "HelveticaNeue",            "size": "15"          }        },        {          "type": "image",          "url": "https://s3.amazonaws.com/.../camera%402x.png",          "style": {            "bottom": "100",            "width": "30",            "color": "#ffffff",            "right": "30"          }        }      ]    }  }}
```

Étonnamment, c'est tout ce que vous devez savoir pour construire n'importe quel type de vue sophistiquée que vous pouvez imaginer sur les appareils mobiles.

Tout comme vous pouvez construire n'importe quoi avec des blocs Lego simples, vous pouvez composer ces composants et mises en page de base de différentes manières pour créer n'importe quelle vue sophistiquée.

Voici quelques exemples, 100% construits en composant les éléments d'interface utilisateur mentionnés ci-dessus :

* [Instagram UI](https://github.com/Jasonette/Instagram-UI-example)
* [Twitter UI](https://github.com/Jasonette/Twitter-UI-example)

![Image](https://cdn-media-1.freecodecamp.org/images/1*v9RxUZ-8XzLfDTfI3gmx6A.gif)

![Image](https://cdn-media-1.freecodecamp.org/images/1*ScwI7a4_oVcOIKcIe0pI1w.gif)

### Au-delà des vues

Si vous avez lu jusqu'ici, vous pensez peut-être :

1. "Wow, c'est cool ! Je veux essayer ça !", ou
2. "Oui, vous pouvez probablement construire une application jouet, mais il n'y a aucun moyen de construire une application de production en utilisant cette méthode !"

Comme je l'ai brièvement mentionné ci-dessus, ceci n'est que la partie **"Vue"** de Jasonette, qui est la partie la plus simple. Mais ce qui est vraiment puissant avec Jasonette, c'est que vous pouvez aller beaucoup plus loin et [écrire un programme déclaratif complet en JSON](http://docs.jasonette.com/actions/).

Vous pouvez attacher des actions aux éléments de l'interface utilisateur, qui sont déclenchées lorsque l'utilisateur les touche. Vous pouvez également déclencher ces actions les unes après les autres via des rappels de succès/erreur. Vous pouvez également écouter certains événements et déclencher automatiquement ces actions.

Tout comme cela, lorsque vous pouvez décrire non seulement une **"Vue"** mais aussi la logique **"Modèle"** et **"Contrôleur"** (tout en JSON), **vous pouvez tout faire**.

### Qu'est-ce qui est possible ?

Puisque tout ce dont vous avez besoin est un serveur qui envoie du JSON, Jasonette est complètement agnostique en termes de plateforme. Il n'y a pas de technologie serveur propriétaire dont vous devez dépendre. Tout ce dont vous avez besoin est du JSON.

Et le JSON peut provenir de n'importe où, d'un appareil local, à des serveurs distants, voire d'un [**raspberry pi**](https://www.raspberrypi.org/documentation/remote-access/web-server/nginx.md) !

1. **Vous avez une application web ?** : Si vous avez déjà une application web, vous pouvez instantanément créer une application mobile native pour votre **application Node.js, Rails, Django, PHP, ou vraiment n'importe quelle application web**, simplement en faisant des requêtes à votre point de terminaison API.
2. **Vous n'avez même pas besoin d'un serveur :** Puisque vous pouvez intégrer un modèle-vue-contrôleur entier dans un seul fichier JSON autonome, vous pouvez pratiquement le stocker et le servir depuis n'importe où. Vous pouvez même créer une application à partir d'un fichier JSON statique servi depuis un Pastebin ou Github !
3. **Transformez n'importe quel site web HTML en application :** Jasonette dispose d'un puissant parseur HTML-to-JSON alimenté par la [bibliothèque cheerio](https://github.com/cheeriojs/cheerio) qui vous permet de transformer n'importe quel HTML en un objet JSON. Et vous savez déjà ce que nous pouvons faire lorsque nous avons du JSON — vous pouvez construire une vue native à partir du JSON transformé ! De cette manière, vous pouvez construire une application native à partir d'un site web qui n'a même pas d'API. Bien sûr, la méthode recommandée est d'utiliser du JSON chaque fois que vous le pouvez, mais c'est vraiment cool quoi qu'il en soit.

Je pourrais continuer indéfiniment, mais voici quelques exemples :

Une **application de partage de photos** qui vous permet de prendre une photo en utilisant l'appareil photo de l'appareil et de la télécharger sur S3, puis de publier l'entrée sur votre propre serveur, créant un flux :

[**Jasonette/s3-upload-example**](https://github.com/Jasonette/s3-upload-example)
[_s3-upload-example - Une application Jasonette pour télécharger une image sur S3 en utilisant $network.upload_github.com](https://github.com/Jasonette/s3-upload-example)

![Image](https://cdn-media-1.freecodecamp.org/images/1*ogHwfXGMOO0Rxq41OpOmrQ.gif)

Une application **Eliza Chatbot** alimentée par Node.js pour iOS et Android :

[**Jasonette/eliza-example**](https://github.com/Jasonette/eliza-example)
[_eliza-example - Application Eliza sur l'iPhone_github.com](https://github.com/Jasonette/eliza-example)

![Image](https://cdn-media-1.freecodecamp.org/images/1*eJquEW8bzx4TtyC1vlPbFQ.gif)

**Une application de microblog**, complète avec gestion de session :

[**Jasonette/token-authentication-example**](https://github.com/Jasonette/token-authentication-example)
[_token-authentication-example - Une application de microblog Jasonette, construite avec rails (côté serveur), utilisant devise pour implémenter..._github.com](https://github.com/Jasonette/token-authentication-example)

![Image](https://cdn-media-1.freecodecamp.org/images/1*_rwBdkRfkQbbRQsrzJwoDg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*jam-klQNXQT6eXgReqUwPw.png)

Une application de télécommande pour les bots Slack :

[**Contrôlez à distance vos bots Slack avec JSON**](http://blog.jasonette.com/2017/01/17/build-a-slackbot-with-jasonette/)
[_Il y a quelques jours, @shaunymca a partagé un projet vraiment cool sur notre chaîne slack. Si vous y réfléchissez, c'est un..._blog.jasonette.com](http://blog.jasonette.com/2017/01/17/build-a-slackbot-with-jasonette/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*4nqPy7lMIyRK1x1sKC4O3g.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*T39jur9f4VZkUbHs59II6Q.png)

Une application d'exemple qui transforme une page web HTML en JSON puis la transforme en une application native :

[**gliechtenstein/iosdevweekly.json**](https://github.com/gliechtenstein/iosdevweekly.json)
[_iosdevweekly.json - Application native pour iOS Dev Weekly, écrite en JSON pur._github.com](https://github.com/gliechtenstein/iosdevweekly.json)

![Image](https://cdn-media-1.freecodecamp.org/images/1*jRDkqas9wMe65O1EgXS_ww.gif)

### Conclusion

Jasonette est un projet jeune. J'ai open-sourcé [la version iOS](https://github.com/Jasonette/JASONETTE-iOS) fin 2016, et [la version Android](https://github.com/Jasonette/JASONETTE-Android) un mois plus tard.

Mais il a [déjà grandi pour devenir une communauté vibrante de contributeurs et de créateurs](http://blog.jasonette.com/2017/01/12/Jasonette-2016-in-review/) et est en développement actif. J'espère que cette technologie permettra à quiconque (pas seulement aux développeurs) de construire des applications sans effort.

Ça a l'air bien ? Consultez le site web [ici](https://www.jasonette.com).

Enfin, vous pouvez trouver les dépôts Github ici : [iOS](https://github.com/Jasonette/JASONETTE-iOS) et [Android](https://github.com/Jasonette/JASONETTE-Android) (**Les contributions sont les bienvenues !**)