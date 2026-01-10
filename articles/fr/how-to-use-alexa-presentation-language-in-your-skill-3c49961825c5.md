---
title: Comment utiliser le langage de présentation Alexa dans votre compétence
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-05T17:08:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-alexa-presentation-language-in-your-skill-3c49961825c5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Yhxg6EjPOGffEe0-01U-RQ.png
tags:
- name: Alexa Skills
  slug: alexa-skills
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: Comment utiliser le langage de présentation Alexa dans votre compétence
seo_desc: 'By Garrett Vargas

  Amazon recently released the Alexa Presentation Language (APL). APL provides a richer
  display for multimodal skills. It is based on modern frameworks that separate display
  elements from data sources. It gives you the flexibility to ...'
---

Par Garrett Vargas

Amazon a récemment publié le langage de présentation Alexa (APL). APL offre un affichage plus riche pour les compétences multimodales. Il est basé sur des frameworks modernes qui séparent les éléments d'affichage des sources de données. Il vous donne la flexibilité d'inclure de nombreux éléments visuels tels que des graphiques, des images et des diaporamas, et vous permet d'adapter l'affichage pour différents appareils.

Dans cet article, je vais vous expliquer comment j'ai mis à jour l'une de mes compétences pour utiliser APL. Vous pouvez également utiliser ces conseils et techniques si vous créez une nouvelle compétence.

La plupart de mes compétences incluent un support multimodal utilisant l'[Interface d'affichage](https://developer.amazon.com/docs/custom-skills/display-interface-reference.html). J'ai décidé d'apprendre APL en mettant à jour l'une de mes compétences existantes. Je me suis concentré sur ma compétence [Video Poker](https://www.amazon.com/Garrett-Vargas-Video-Poker/dp/B07465B5ZK) parce que je n'étais pas satisfait de l'expérience client existante.

Video Poker présente aux utilisateurs une main de poker de 5 cartes, avec la possibilité de garder et de défausser des cartes avant de tirer pour compléter une main. Les utilisateurs peuvent le faire par commande vocale (« garder la première carte » ou « garder la paire de valets »), ou en touchant les cartes sur un affichage visuel. **ListTemplate2** était la meilleure façon de faire cela avec l'Interface d'affichage. Cependant, cela venait avec la limitation de n'autoriser que trois cartes à l'écran à la fois et de mettre des nombres sous chaque carte dans la liste.

![Image](https://cdn-media-1.freecodecamp.org/images/jMxKMUHlUnJBPaXP4c5kx7rCPL1WFe3DEqhJ)
_Video Poker utilisant la directive d'affichage ListTemplate2_

En utilisant APL, j'ai modifié une mise en page ListTemplate2 pour réduire la taille des éléments de la liste, diminuer l'espacement entre eux et faire tenir une main complète de cinq cartes à l'écran. J'ai pu supprimer les nombres des éléments de la liste et mettre du texte indiquant quelles cartes étaient gardées en gras et en rouge. J'ai pu optimiser la mise en page pour différentes dimensions d'écran, comme les petits affichages comme l'Echo Spot.

![Image](https://cdn-media-1.freecodecamp.org/images/jd4xu4HhI8hhfhPXvDtzJMByErFxomzeWU6r)
_Video Poker utilisant un modèle APL modifié à partir de ListTemplate2_

#### Outil d'auteur APL

La façon dont j'ai fait cela était à travers l'[Outil d'auteur APL](https://developer.amazon.com/alexa/console/ask/displays). Cet outil pratique fournit une liste de différentes conceptions visuelles que vous pouvez utiliser comme base pour créer des visuels convaincants pour votre compétence. Il vous permet également de sauvegarder et de télécharger des mises en page, afin que vous puissiez les extraire vers votre code de compétence, ou les télécharger si vous faites des mises à jour hors ligne. Pour ce cas d'utilisation, j'ai commencé avec l'**Échantillon de liste d'images en avant**, qui est basé sur ListTemplate2.

![Image](https://cdn-media-1.freecodecamp.org/images/Z2PFZCT6MUCN64bPTQ9qRs4XBXem42fTGEqB)
_Sélection d'une conception visuelle à partir de l'outil d'auteur APL_

Une fois que vous avez sélectionné cette conception visuelle dans l'outil, vous verrez un exemple générique d'une liste avec des échantillons de fromage. Vous verrez le document APL en bas de l'écran séparé en deux onglets :

* « Image Forward List Sample » qui fournit la mise en page
* L'onglet « Data JSON » qui fournit une vue des données du document.

![Image](https://cdn-media-1.freecodecamp.org/images/AJFvDwilgG-7N3H4tH0f6tq73tvsNnr8lSGG)
_Édition de votre document APL dans l'outil d'auteur_

Prenez un moment pour parcourir le JSON à la fois dans l'onglet Image Forward List Sample (le code de mise en page) et l'onglet Data JSON (le code de contenu). Vous remarquerez dans la mise en page qu'il y a plusieurs références à des valeurs encadrées dans `${}` telles que `${payload.listTemplate2ListData.listPage.listItems.length}`. Si vous regardez dans le fichier de contenu, vous verrez que cela correspond à un chemin vers une valeur dans le contenu. C'est ainsi qu'APL lie les données à la couche de présentation et vous permet de faire des changements.

#### Mise à jour des sources de données

En premier lieu, je voulais mettre à jour les données pour qu'elles affichent des images de cartes et du texte pertinents pour ma compétence. Ainsi, lorsque j'ai commencé à mettre à jour la mise en page elle-même, j'ai pu voir à quoi cela ressemblerait avec mes images réelles. L'outil d'auteur montre vos images d'écran rendues en temps réel, ce qui est pratique à utiliser lorsque vous essayez de perfectionner votre mise en page. Pour mettre à jour les données, j'ai suivi les étapes suivantes :

* Cliquez sur l'onglet Data JSON
* Dans `listTemplate2Metadata`, changez les éléments `title` et `logo` en quelque chose de pertinent pour Video Poker
* Dans cet même élément, changez l'`url` dans les champs `backgroundImages.sources` pour pointer vers l'image de fond que je voulais utiliser
* Dans `listTemplate2ListData.listPage`, j'ai mis à jour chacun des éléments dans le tableau `listItems`. Plus précisément, j'ai mis à jour ce tableau pour avoir 5 éléments (mes cartes), avec `listItemIdentifier` et `token` définis sur « card.x » (où x varie de 0 à 4). J'ai supprimé le `secondaryText` puisque je ne voulais qu'une seule ligne de texte (qui serait soit vide, soit « HELD »). J'ai mis à jour les `image.sources` pour pointer vers des URL contenant mes images de cartes. Pour l'instant, j'ai simplement sélectionné quelques images de cartes au hasard — le code de ma compétence mettra à jour les données pendant le jeu avec la main réelle de l'utilisateur
* Mettez à jour le texte d'indice pour utiliser une transformation. Plutôt que de coder en dur la chaîne d'indice avec le mot-clé Alexa, vous pouvez utiliser une transformation pour changer un indice en un qui utilise le mot de réveil associé à l'appareil, au cas où l'utilisateur l'aurait changé. Vous faites cela en supprimant le `hintText` de listTemplate2ListData et en ajoutant ce qui suit dans votre lastTemplate2Metadata :

```
"properties": {    "hintText": "select number 1"},"transformers": [    {        "inputPath": "hintText",        "transformer": "textToHint"    }],
```

Une fois que j'ai apporté ces modifications aux sources de données, mon image ressemblait à ceci — assez similaire à la compétence telle qu'elle existe avec l'affichage ListTemplate2, ce qui est logique puisque à ce stade, j'utilise toujours la mise en page basée sur ListTemplate2 et n'ai apporté que des modifications de contenu.

![Image](https://cdn-media-1.freecodecamp.org/images/2w4rK8o0mL8as6gmh7utg757rRzeYHfBWjVK)
_Vue mise à jour avec le contenu pertinent de Video Poker_

#### Mise à jour de la mise en page

Maintenant, la partie amusante — mettre à jour la mise en page pour obtenir cinq images à l'écran en même temps. Pour cette partie, j'ai apporté des modifications à la mise en page dans l'onglet « Image Forward List Sample ». Pour apporter ces modifications, j'ai cliqué sur le curseur qui vous permet de basculer entre une vue visuelle des composants APL imbriqués et une vue JSON brute. Je trouve que la visualisation du document JSON complet est plus facile à consulter que de cliquer sur chaque composant et d'éditer le JSON dans le composant. Mais vous pouvez jouer avec et suivre l'approche qui vous semble la plus naturelle.

Avant de parler des modifications que j'ai apportées, je voulais souligner certains des éléments de ce modèle de mise en page :

* Il y a un nœud `ListTemplate2` dans le JSON qui fournit deux conteneurs dans un nœud `items` — l'un qui s'applique aux écrans circulaires (comme l'Echo Spot) et l'autre pour les autres types d'écrans. Dans ce blog, je vais me concentrer sur les affichages non-Spot, mais vous devez apprécier que vous pouvez également apporter des modifications spécifiques à différentes mises en page d'écran.
* En regardant le deuxième conteneur que nous allons modifier, vous verrez un ensemble d'`items` incluant une Image (l'image de fond), un **AlexaHeader** (le titre à l'écran), une **Sequence** (qui est la liste des cartes), et un **AlexaFooter** (l'indice en bas de l'écran)
* Vous verrez que la Sequence pointe vers `HorizontalListItem`, qui est un autre conteneur dans ce document JSON. Il contient des éléments composés d'une Image et de deux éléments Text (le texte principal et le texte secondaire)

Avec ce contexte en tête, j'ai apporté les modifications suivantes à ce document :

* Dans le `HorizontalListItem`, j'ai changé les dimensions de l'élément Image — plus précisément, j'ai défini `height` à 40vh et `width` à 17vw. Cela définit la hauteur de chaque carte à 40 % de la hauteur de la fenêtre, et la largeur à 17 % de la largeur de la fenêtre.
* J'ai ensuite mis à jour `midWidth` à 100. Cela réduit la largeur de chaque élément de la liste et permet aux cinq images de cartes d'apparaître à l'écran
* J'ai changé `paddingLeft` et `paddingRight` à 6 pour réduire la quantité d'espace entre les éléments
* J'ai ajouté `paddingTop` et l'ai défini à 100 pour ajouter une séparation entre l'en-tête et les images des cartes
* J'ai supprimé l'élément Text secondaire puisque je n'ai pas deux lignes de texte sur mon affichage
* J'ai changé l'élément Text principal pour qu'il ne dessine pas l'ordinal. Ainsi, `text` dans cet élément est passé de `<b>${ordinal}.</b>${data.textContent.primaryText.text}` à `<b>${data.textContent.primaryText.text}</b>`.
* Dans cet même élément, je voulais que le texte soit rouge et centré. J'ai réalisé cela en ajoutant un champ `textAlign` avec une valeur de « center », et un champ `color` avec une valeur de « red ».
* Pour obtenir le texte d'indice de l'emplacement approprié (maintenant partie des métadonnées plutôt que des données de la liste), j'ai dû mettre à jour l'élément AlexaFooter pour obtenir l'indice de `${payload.listTemplate2Metadata.properties.hintText}`

Enfin, j'ai dû rendre les cartes de ma liste sélectionnables, afin de pouvoir répondre lorsque l'utilisateur touche l'une d'entre elles sur l'écran. Pour ce faire, j'ai dû changer les éléments associés à l'élément `Sequence` d'un `FullHorizontalListItem` à un `TouchWrapper` qui contenait à son tour un `FullHorizontalListItem`. En code, cela signifie que j'ai changé ceci :

```
"item": [  {    "type": "FullHorizontalListItem",    "listLength": "${payload.listTemplate2ListData.listPage.listItems.length}"  }]
```

en ceci :

```
"item": [  {    "type": "TouchWrapper",    "onPress": {      "type": "SendEvent",      "arguments": [        "${data.token}"      ]    },    "item": {      "type": "FullHorizontalListItem",      "listLength": "${payload.listTemplate2ListData.listPage.listItems.length}"    }  }]
```

Notez l'élément `onPress` dans cet élément. Plus précisément, la liste des arguments. Vous pouvez spécifier un tableau de différents arguments à envoyer à votre compétence lorsqu'un élément est sélectionné. Comme mon code existant traitait le token de la carte sélectionnée, j'ai décidé de continuer à faire de même pour minimiser la quantité de code que je devais changer. Mais vous pourriez également passer `${ordinal}` qui vous indiquerait l'index de l'élément sélectionné sans avoir à traiter le token.

#### Mises à jour du code de la compétence

Une fois que vous avez apporté des modifications dans l'outil d'auteur, vous pouvez sélectionner le bouton Exporter le code qui emballera votre mise en page et vos fichiers de données en un seul fichier JSON pour vous. J'ai choisi d'utiliser deux fichiers JSON différents dans mon code, l'un appelé main que j'ai utilisé pour la mise en page et un autre appelé datasources que j'ai utilisé pour les données. J'aime garder la séparation de la mise en page et du contenu dans mon code source comme une bonne pratique générale. Il était surprenant que l'outil d'auteur d'Amazon n'encourage pas cela non plus.

Maintenant que nous avons téléchargé le document et le contenu, nous devons apporter des modifications au code pour l'incorporer et mettre à jour les données lorsque l'utilisateur joue avec notre compétence. Nous pouvons le faire en manipulant les éléments de données et en les renvoyant ensuite à la compétence. J'ai utilisé la fonctionnalité d'intercepteur de réponse d'Alexa (dont je parle dans un [article de blog séparé](https://medium.freecodecamp.org/how-to-improve-your-code-with-alexa-response-interceptors-2b3e73721fc)). Je charge la source de données à partir d'un fichier JSON, puis je mets à jour les cartes et le texte dans la structure avant de l'envoyer à Alexa. Je fais cela avec le code suivant :

```
const main = require('./main.json');const datasource = require('./datasource.json');
```

```
function drawTable(handlerInput) {  const event = handlerInput.requestEnvelope;  const attributes = handlerInput.attributesManager.getSessionAttributes();  const game = attributes[attributes.currentGame];  let i;  let cardText;  let url;
```

```
  // Mettre à jour les images  for (i = 0; i < game.cards.length; i++) {    const card = game.cards[i];    url = GetCardURL(card);    cardText = (card.hold) ? 'HELD' : '';    datasource.listTemplate2ListData.listPage.listItems[i]      .textContent.primaryText.text = cardText;    datasource.listTemplate2ListData.listPage.listItems[i]      .image.sources[0].url = url;    datasource.listTemplate2ListData.listPage.listItems[i]      .image.sources[1].url = url;  }  // Donner un indice approprié  if (game.state === 'FIRSTDEAL') {      if (game.cards[0].hold) {        datasource.listTemplate2ListData.hintText = 'discard the first card';      } else {        datasource.listTemplate2ListData.hintText = 'hold the first card';      }      datasource.listTemplate2Metadata.title = 'Select cards to hold or say Deal';    } else {      datasource.listTemplate2ListData.hintText = 'deal';      datasource.listTemplate2Metadata.title = 'Your last hand';    }  }  return handlerInput.responseBuilder    .addDirective({      type: 'Alexa.Presentation.APL.RenderDocument',      version: '1.0',      document: main,      datasources: datasource,    });}
```

Le deuxième endroit où j'ai dû apporter une modification de code était pour gérer l'utilisateur touchant l'un des éléments de ma liste. Dans mon ancien code, je analysais les tokens d'éléments de la forme « card.x » où x est la position ordinale de la carte dans la liste. Avec une Interface d'affichage, cela signifiait rechercher une requête `ElementSelected`. Dans APL, votre code recevra un `APL.Presentation.APL.UserEvent`, et vous pouvez traiter la requête comme suit pour déterminer quelle carte a été sélectionnée :

```
module.exports = {  canHandle(handlerInput) {    const request = handlerInput.requestEnvelope.request;       // Était-ce un élément tactile sélectionné ?    if (request.type === 'Alexa.Presentation.APL.UserEvent') {      return ((request.source.type === 'TouchWrapper')        && (request.source.handler === 'Press'));    }    return false;  },  handle(handlerInput) {    let index;    const event = handlerInput.requestEnvelope;    // Était-ce un élément tactile sélectionné ?    if (event.request.type === 'Alexa.Presentation.APL.UserEvent') {      const cards = event.request.arguments[0].split('.');      if (cards.length === 2) {        index = cards[1];      }            // Faire quelque chose avec la carte sélectionnée...
```

```
    }  },};
```

Avec ces changements, j'avais une compétence Video Poker beaucoup plus propre, qui est sûre de ravir mes clients plus que l'ancien format que j'utilisais. Je n'ai fait qu'effleurer les capacités d'APL. Mais je peux dire qu'il ouvrira un nouveau monde de possibilités pour les compétences multimodales pilotées par la voix ! Faites-moi savoir dans les commentaires vos propres apprentissages avec ce nouveau framework.