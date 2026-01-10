---
title: La bibliothèque d'équipe repensée de Figma
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-19T15:07:46.000Z'
originalURL: https://freecodecamp.org/news/figmas-reimagined-team-library-fa027053c303
coverImage: https://cdn-media-1.freecodecamp.org/images/1*E_PZbYUNCYEk5zw6pM5_Zw.png
tags:
- name: Design
  slug: design
- name: Design Tools
  slug: design-tools
- name: Productivity
  slug: productivity
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: La bibliothèque d'équipe repensée de Figma
seo_desc: 'By Zach Grosser

  A new, more powerful interface for sharing Components across your organization

  The Team Library in Figma is a set of shared Components across all files in a Team.
  Components in the Team Library are accessible across any file — existin...'
---

Par Zach Grosser

#### Une nouvelle interface plus puissante pour partager des composants dans votre organisation

La bibliothèque d'équipe dans [Figma](https://www.figma.com) est un ensemble de composants partagés dans tous les fichiers d'une équipe. Les composants de la bibliothèque d'équipe sont accessibles dans n'importe quel fichier — existant ou nouveau — dans n'importe quel projet d'équipe. Si un nouveau fichier est créé dans notre équipe, avant qu'il ne contienne du contenu, il a automatiquement accès à des centaines de composants existants que nous avons publiés dans notre bibliothèque d'équipe. Non seulement cela, mais lorsque la version principale d'un composant est modifiée, Figma permet à ces modifications de se propager dans _tous_ les fichiers contenant une instance de ce composant. Et le meilleur dans tout cela, c'est que ce n'est pas une mise à jour forcée ; au lieu de cela, une notification apparaît dans chacun de ces fichiers, permettant de visualiser et d'accepter les modifications apportées à l'instance de ce composant.

![Image](https://cdn-media-1.freecodecamp.org/images/ZEejfpeLF5YQrRxvmRapJ9iyCSVvrl4oTzqb)
_Nouvelle interface disponible à la base du panneau de gauche._

Aujourd'hui, une mise à jour majeure de la bibliothèque d'équipe a été publiée. Le panneau de gauche dans Figma, autrefois simplement la liste des calques, dispose d'une nouvelle interface en bas. Par défaut, ce panneau vous permet de voir tous vos calques et objets dans le fichier, comme vous pouviez le faire auparavant, et dispose désormais de deux nouveaux espaces dédiés : les composants de fichier et la bibliothèque d'équipe, qui peuvent être basculés en bas du panneau ou avec des raccourcis clavier : alt + 1 pour la liste des calques, alt + 2 pour les composants de fichier, et alt + 3 pour la bibliothèque d'équipe (bien que Chrome OS intercept actuellement ce raccourci clavier).

![Image](https://cdn-media-1.freecodecamp.org/images/YlK-BT489DdnhCqrelzc0--iGftiJiPOIlsN)
_Vue de la bibliothèque d'équipe dans le panneau de gauche de l'application de bureau Figma._

À mesure qu'un système de design s'étend, maintenir la cohérence peut devenir plus difficile. Chez Square, nous utilisons les bibliothèques d'équipe pour organiser les actifs couramment partagés entre les équipes Communications et Social. Des actifs comme les palettes de couleurs unifiées et les ensembles d'icônes créés par l'équipe Marketing, les logos d'entreprise et les appareils [de Facebook](http://facebook.design) sont tous utilisés fréquemment. Après avoir utilisé plusieurs solutions de gestion d'actifs, avoir une version unifiée et mise à jour des actifs directement accessible dans l'application de design est incroyablement puissant. Tant de problèmes liés à la construction de systèmes de design et de bibliothèques d'actifs ont été résolus.

Mais ne vous sentez pas limité aux seuls actifs d'icônes. Selon [les propres mots de Figma](https://www.figma.com/features), vous pouvez « créer des systèmes de design avec des composants d'interface utilisateur liés que toute l'équipe peut utiliser ». Un composant est n'importe quel objet ou groupe d'objets que vous prévoyez d'utiliser à plusieurs endroits, mais pour lesquels vous souhaitez conserver la possibilité de modifier les propriétés dans toutes leurs versions (similaire aux Symboles dans d'autres applications). Vous pourriez créer des mises en page d'écran complexes ou des pages web avec des centaines d'objets dans un cadre et le transformer en un composant à partager avec votre équipe.

### Utilisation des composants

Les composants peuvent être une simple ligne ou forme, ou un ensemble extrêmement complexe d'objets dans un cadre, et tout ce qui se trouve entre les deux. Les composants sont des éléments qui peuvent être réutilisés dans un fichier de design ou une équipe. Prenons l'exemple d'un simple bouton. Je veux que tous les boutons de mon design aient le même design de base : coins arrondis, fond rouge, taille et style de texte, etc. Je crée donc mon premier bouton avec toutes les propriétés définies comme je les aime.

![Image](https://cdn-media-1.freecodecamp.org/images/7gRwotBHXVVy99hXqJ5LbTpsUi-B5uxgltpm)
_L'icône qui ressemble à quatre carrés en forme de losange apparaît dans la barre de menu de Figma lorsqu'un objet, un groupe ou un cadre est sélectionné._

![Image](https://cdn-media-1.freecodecamp.org/images/0td1-8QwDWysqYKc5ErZs9m-CRnWYjZoZu3d)
_Le menu clic droit sur un objet, un groupe ou un cadre expose également les options de composant._

Ensuite, je fais un composant à partir de mon premier bouton. Vous pouvez sélectionner n'importe quel objet, puis cliquer sur le bouton Composant en haut de l'interface Figma, utiliser le raccourci clavier macOS : option + commande + K, ou faire un clic droit sur l'objet et sélectionner « Créer un composant ».

Pour créer plus de boutons, je duplique le nouveau composant de bouton ou je fais glisser une nouvelle copie depuis la liste des composants de fichier dans le panneau de gauche. Ces nouveaux boutons sont appelés Instances, et ils référencent et conservent tous les propriétés du composant à partir duquel ils ont été créés, également connu sous le nom de composant principal. Si j'ajuste la couleur ou la police dans le bouton du composant principal, toutes les instances dans mon fichier seront mises à jour pour correspondre, instantanément.

J'ai utilisé des composants dans un [modèle de présentation open-source](https://medium.com/swlh/presentation-template-for-figma-2b97fdefdacd), en configurant les titres des diapositives comme un composant et des instances de ce composant. Maintenant, lorsque je dois personnaliser une nouvelle présentation avec une police et une palette de couleurs différentes, cela prend quelques secondes.

![Image](https://cdn-media-1.freecodecamp.org/images/msLsvZOREAADb1CcK7SQmLcaiGGvxKp1Xk0w)
_En utilisant des composants et des instances, un groupe de zones de texte dans plusieurs cadres peut avoir leurs propriétés ajustées en même temps._

Toute personne ayant accès au fichier peut également apporter des modifications aux composants. Par exemple, partager un fichier avec un correcteur permet de mettre à jour le texte dans un composant principal et de faire en sorte que ses modifications de texte se propagent à toutes les instances.

L'utilisation de composants dans un fichier me semblait déjà magique et a toujours été un gain de temps énorme à mesure qu'un fichier grandit avec plus de cadres et d'instances. Mais la vraie magie réside dans l'utilisation de composants dans plusieurs fichiers, grâce à la bibliothèque d'équipe.

Si je prends un composant de bouton et que je le publie dans la bibliothèque d'équipe, alors n'importe qui dans mon équipe peut y accéder et l'utiliser dans ses fichiers, et tout nouveau fichier créé dans l'équipe y a également accès. Cela signifie que les designers peuvent commencer à construire immédiatement ; en utilisant des composants de base de notre système de design.

Avec le temps, les propriétés du bouton peuvent avoir besoin d'être ajustées. En revenant au composant principal de ce bouton, en faisant un clic droit sur une instance de celui-ci ou sur le composant lui-même dans le panneau de la bibliothèque d'équipe, et en ajustant sa couleur, par exemple, notifie chaque fichier contenant une instance qu'une mise à jour est disponible. Un point de notification bleu apparaît sur l'icône de la liste des composants de fichier à la base du panneau de gauche. Un bouton « Publier les modifications » en haut de la liste des composants mène à une fenêtre modale pour confirmer les modifications. Une fois les modifications publiées dans la bibliothèque d'équipe, tout fichier utilisant une instance de ce composant recevra une notification dans le coin inférieur droit pour examiner la ou les mises à jour. Cliquer sur « Examiner » vous permet de voir ce qui a été modifié, par qui et quand. Une fois accepté, la ou les instances dans votre fichier seront mises à jour immédiatement pour se conformer au composant principal. Et vous pouvez choisir de ne pas accepter ces modifications et les instances de votre fichier resteront inchangées.

![Image](https://cdn-media-1.freecodecamp.org/images/G2Rwcgw25E1UmUVxL98nE33OmmPbjyQWfBMx)
_Notification dans le fichier lorsqu'une ou plusieurs instances dans votre fichier ont leur composant principal mis à jour._

### Sélection et publication de composants de fichier vers la bibliothèque d'équipe

1. Sélectionnez l'objet, le groupe ou le cadre
2. Cliquez sur le bouton Composant en haut de l'interface Figma, utilisez le raccourci clavier macOS : option + commande + K, ou faites un clic droit sur l'objet et sélectionnez « Créer un composant »
3. Passez à l'onglet Composant en sélectionnant le bouton bascule à la base de la liste des calques, ou utilisez le raccourci clavier macOS : alt + 2
4. Faites un clic droit sur les composants pour les ajouter à la bibliothèque d'équipe, ou utilisez « Publier le fichier dans la bibliothèque » sous votre liste de composants pour pousser **tous** les composants de ce fichier vers la bibliothèque d'équipe
5. Passez à l'onglet Bibliothèque d'équipe en sélectionnant le bouton bascule à la base du panneau, ou utilisez le raccourci clavier macOS : alt + 3

Maintenant, vous pouvez rechercher ou naviguer vers n'importe quel composant qui a été publié dans votre équipe, par n'importe quel contributeur.

Pour placer une instance d'un composant dans votre fichier : faites glisser depuis le panneau de la bibliothèque d'équipe vers n'importe quel fichier. Cette instance continue d'être attachée au composant principal du fichier de votre équipe dont elle provient (et il pourrait provenir d'un autre membre de votre équipe), sauf si vous faites un clic droit et sélectionnez « Détacher l'instance » (raccourci clavier macOS : option + commande + B)

Vous pouvez également ajouter une description à vos composants, visible dans la bibliothèque d'équipe pour ajouter un contexte supplémentaire pour votre équipe. Sélectionnez le composant principal et ajoutez une description dans le panneau de droite. Les descriptions apparaissent au survol dans la liste des composants et dans la bibliothèque d'équipe.

![Image](https://cdn-media-1.freecodecamp.org/images/SMX4rX2ioWXzw-vwnqrVd97Fet37yYjoSM-m)
_Ajoutez une description à vos composants dans le panneau de droite de Figma._

Lisez _encore plus_ sur les composants ici :

[**Les composants dans Figma**](https://blog.figma.com/components-in-figma-e7e80fcf6fd2)
[_Aujourd'hui, nous sommes ravis de publier les composants dans Figma. En apportant des concepts comme la composition, l'héritage et des possibilités illimitées..._blog.figma.com](https://blog.figma.com/components-in-figma-e7e80fcf6fd2)

### Astuce pro

Vous pouvez définir l'arrière-plan d'une vignette de composant dans la liste des composants et la bibliothèque d'équipe en plaçant un cadre derrière le composant et en changeant sa couleur. Cela est très pratique avec des composants plus clairs, comme des icônes blanches ou grises.

![Image](https://cdn-media-1.freecodecamp.org/images/i2t5AHEi4z62connnOj7Yq5-jJ5NkTMr3ZHG)
_La création d'un cadre derrière un composant et le changement de la couleur de remplissage modifieront la couleur de la vignette du composant dans la liste des composants de fichier et le panneau de la bibliothèque d'équipe._

Un grand merci à l'équipe de Figma ! Qui continue de construire des fonctionnalités incroyables comme celle-ci, et a le [cycle de publication le plus rapide](http://releases.figma.com) que j'aie jamais vu.

**_Il y a déjà 464 composants dans la bibliothèque d'équipe de Square !_**

_Avis de non-responsabilité : Vous avez peut-être trouvé cet article via de la publicité sur Twitter ou Facebook. Figma n'a pas sponsorisé la rédaction de cet article, et fait de la publicité avec ma permission car ils ont également pensé que cela serait utile pour d'autres designers._