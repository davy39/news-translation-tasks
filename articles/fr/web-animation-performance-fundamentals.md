---
title: Principes de base des performances d'animation Web – Comment rendre vos pages
  fluides
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-02-28T18:49:59.000Z'
originalURL: https://freecodecamp.org/news/web-animation-performance-fundamentals
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/Antics_2-D_Animation_infobox_screenshot-1.png
tags:
- name: animation
  slug: animation
- name: CSS
  slug: css
- name: web performance
  slug: web-performance
seo_title: Principes de base des performances d'animation Web – Comment rendre vos
  pages fluides
seo_desc: "By Reza Lavarian\nWhat if I told you that web pages were interactive animations\
  \ played back by your web browser?\nWe watch various motions every time we're on\
  \ a web page. \nAnd it's not only JavaScript or CSS animations that I'm talking\
  \ about. Scrolling..."
---

Par Reza Lavarian

Et si je vous disais que les pages web étaient des animations interactives lues par votre navigateur web ?

Nous observons divers mouvements chaque fois que nous sommes sur une page web.

Et ce n'est pas seulement les animations JavaScript ou CSS dont je parle. Le défilement, le zoom pincé, la sélection de texte et même le survol d'un bouton sont techniquement des animations et fonctionnent de manière similaire.

En fait, ce sont des images séquentielles affichées rapidement pour nous donner une perception de mouvement ou simplement refléter un changement.

Chaque fois que le code JavaScript modifie la page, une zone de l'image précédente est invalidée, et le navigateur en dessine une nouvelle.

Ces changements pourraient être aussi simples que l'ajout ou la suppression d'un élément `<div>` ou la modification des styles d'un bouton.

Nous appelons ces images des **frames**.

[Basé sur les directives de timing de frame du W3C](https://www.w3.org/TR/frame-timing/#h-introduction), le navigateur web doit être capable d'afficher soixante frames par seconde (60 fps).

Bien sûr, une frame reste à l'écran s'il n'y a pas de changement.

Et si je vous montrais quelques exemples ?

Lorsque vous faites défiler une page, le navigateur affiche les zones hors écran du document à mesure que vous faites défiler vers le bas (ou vers le haut).

L'image ci-dessous montre les frames séquentielles produites et affichées pendant quelques secondes de défilement.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/animation-scroll-2.png)
_Frames générées pendant quelques secondes de défilement_

Et comme vous pouvez le voir, chaque frame a été affichée pendant 16,7 ms (60 fps).

J'ai utilisé [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) pour créer l'enregistrement ci-dessus. Vous pouvez le reproduire si vous le souhaitez. Dans DevTools, allez dans le panneau **Performance**, et cliquez sur le bouton d'enregistrement. Ensuite, faites défiler la page pendant quelques secondes, et arrêtez l'enregistrement.

Vous verrez un aperçu comme celui ci-dessus.

Même lorsque vous sélectionnez un morceau de texte, de nouvelles frames sont affichées à mesure que vous sélectionnez plus de lettres et de lignes.

Dans l'enregistrement ci-dessous, je déplace la souris sur la timeline pour rejouer la sélection de texte :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/text-select.gif)

Pourquoi dois-je savoir cela ? pourriez-vous demander.

Lorsque une page ne répond pas rapidement aux interactions de l'utilisateur ou a des mouvements saccadés, quelque chose ne va pas.

Et c'est généralement dû au fait que le **thread principal** du navigateur est si occupé qu'il ne peut pas livrer les frames à temps (plus d'informations à ce sujet ci-dessous).

Dans ce guide, j'expliquerai comment les navigateurs transforment le code en pixels et comment nous pouvons travailler avec eux pour offrir une expérience utilisateur agréable.

Je me concentrerai sur Google Chrome pour cet article. Cependant, les concepts de haut niveau sont les mêmes pour tous les navigateurs.

Il y a beaucoup de théories à couvrir ici, et j'espère que cela ne vous dérange pas.

Michael Jordan a dit : "Gardez les fondamentaux, et le niveau de tout ce que vous faites s'élèvera."

Faites-moi confiance, connaître ces théories ne sera pas sans récompense !

Vous aurez une nouvelle perspective sur la façon dont les pages web changent. Et nous passerons à beaucoup d'actions à la fin.

## Fréquence de rafraîchissement ou fréquence d'images ?

L'appareil d'affichage moyen rafraîchit l'écran soixante fois par seconde (60 Hz).

Pour les yeux humains, toute fréquence supérieure à 12 Hz est perçue comme un mouvement. [Cet article de Paul Bakaus](https://paulbakaus.com/tutorials/performance/the-illusion-of-motion/) fait un excellent travail d'explication.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Animhorse.gif)
_**[CC BY-SA 2.5 ](https://en.wikipedia.org/wiki/Frame_rate#/media/File:Animhorse.gif">Cheval animé</a>** (12 dessins par seconde) par <a href="https://en.wikipedia.org/wiki/User:Janke">**Janke**</a>, sous licence **<a href="https://creativecommons.org/licenses/by-sa/2.5/)**_

Il existe des écrans avec des fréquences de rafraîchissement plus élevées comme 120 Hz ou 144 Hz, mais 60 Hz est la norme pour la plupart des appareils d'affichage.

La fréquence de rafraîchissement est différente de la **fréquence d'images**, cependant.

La fréquence de rafraîchissement est le nombre de fois qu'un appareil d'affichage rafraîchit une image en une seconde. La fréquence d'images est un nombre arbitraire d'images (dans un système de film), capturées ou dessinées en une seconde.

Par exemple, la fréquence standard pour l'enregistrement de films est [24 fps](https://www.masterclass.com/articles/how-frame-rates-affect-film-and-video#3-standard-frame-rates-for-film-and-tv), même si ce n'est pas la fréquence de rafraîchissement maximale d'une télévision moderne.

Dans ce cas, les appareils d'affichage utilisent un algorithme pour répéter des frames spécifiques afin de rendre la fréquence d'images compatible avec leur fréquence de rafraîchissement. Cela signifie que vous pouvez regarder un film à 24 fps sur une télévision à 144 Hz à la fréquence d'origine de 24 fps.

Pourquoi la fréquence d'images est-elle même importante pour les pages web, pourriez-vous demander ?

Un utilisateur qui joue à des jeux à 120 fps remarquerait un défilement de page lent sur le même ordinateur.

Ils n'apprécieront pas non plus les animations web à une fréquence inférieure à 60 fps.

Êtes-vous déjà tombé sur ces sites web avec beaucoup de publicités et de GIF ? Je quitte généralement ces pages rapidement car je sais que trouver un autre site web me ferait gagner du temps !

## Il y a une date limite pour produire chaque frame

Il faut du temps au navigateur pour dessiner une nouvelle frame.

Afficher soixante frames par seconde signifie que chaque frame doit être prête à l'écran en 16,7 ms (1 sec ÷ 60).

Sinon, la frame serait **retardée** ou **perdue**. Ce problème est souvent appelé **jank** sur une page web.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/plane-1.gif)
_Une animation avec des frames perdues et des retards_

Notre priorité absolue est donc claire maintenant : nous devons rendre nos pages [sans jank](http://jankfree.org/) 👆.

Mais d'abord, nous devons savoir comment tout fonctionne.

## Comment une frame est produite

Le navigateur web génère une nouvelle frame parce que quelque chose a changé sur la page. Et il doit refléter ce changement.

Une page web change lorsque :

**L'utilisateur interagit avec la page**. Ils font défiler, zoom pincé, cliquent, sélectionnent un morceau de texte, etc.

**Un morceau de code JavaScript change la page**. Par exemple, il ajoute un élément `<div>` ou change un style CSS.

Chaque changement déclenche une séquence de tâches, qui résulte en une seule frame.

Cette séquence de tâches est connue sous le nom de **pixel pipeline**, **rendering waterfall**, ou **rendering pipeline**.

Et voici à quoi cela ressemble d'un point de vue de haut niveau :

* **Évaluation JavaScript** – le navigateur : oh, quelque chose a changé ! Je dois générer une nouvelle frame.
* **Calcul de style** – le navigateur : maintenant, je dois appliquer la classe `some-class` à cet élément `<div>`.
* **Mise en page (reflow)** – le navigateur : je vois que certains éléments ont de nouveaux styles maintenant. Je dois calculer combien d'espace ils prennent à l'écran et où ils doivent être positionnés en fonction de ces styles. De plus, je dois calculer la géométrie de tous les autres éléments affectés par ce changement !
* **Peinture** – le navigateur : maintenant, je dois regrouper les éléments (qui ont une sortie) en plusieurs couches et convertir chaque couche en une représentation bitmap dans la mémoire ou la RAM vidéo.
* **Composition** – le navigateur : maintenant, je dois combiner ces bitmaps dans l'ordre défini pour former la frame finale.

Les mêmes étapes sont également suivies lorsque la page web est rendue pour la première fois.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/pipeline-1.png)
_Le pixel pipeline_

Chaque activité du pipeline déclenche son activité suivante. Par exemple, la mise en page déclenche la peinture, et cela continue jusqu'à la dernière étape.

Nous devons être attentifs à chaque activité dans le pipeline car chacune peut contribuer à de faibles performances.

Apprenons à les connaître un peu mieux.

### Évaluer JavaScript – lorsque le code JavaScript s'exécute

Vous modifiez généralement la page à partir de votre code JavaScript.

Beaucoup d'entre nous suppriment un élément comme ceci :

```javascript
let myBox = document.querySelector('.my-box')

if (myBox) {
 myBox.remove()
}
```

Ou le cachent de cette manière :

```javascript
let myBox = document.querySelector('.my-box')

if (myBox) {
  myBox.style.display = 'none'
}
```

Ou ajoutent un sélecteur CSS à sa liste de classes :

```javascript
let myBox = document.querySelector('.my-box')

if (myBox) {
  myBox.classList.add('my-special-box')
}
```

Ces changements invalident une portion du document et font que le navigateur produit une nouvelle frame.

### Style – quels styles CSS vont avec quel élément

Ensuite, le navigateur web associe les nouveaux styles aux éléments respectifs en fonction des sélecteurs correspondants.

Par exemple, si vous ajoutez la classe `my-special-box` à la liste de classes d'un élément :

```javascript
let myBox = document.querySelector('.my-box')

if (myBox) {
  myBox.classList.add('my-special-box')
}
```

Cette étape est celle où les styles respectifs sont calculés et appliqués à votre élément.

De plus, comme vous le savez probablement, [les éléments HTML et les styles sont convertis en arbres DOM et CSSOM, respectivement](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/constructing-the-object-model).

Le navigateur utilise ces structures de données en interne. Mais il les expose également à JavaScript via les [API du navigateur](https://www.decodingweb.dev/books/decoding-web-development/front-end-skills-to-get-you-started#web-apis). C'est ainsi que nous avons manipulé le document dans les exemples précédents – nous avons utilisé l'API DOM.

Le navigateur web **combine** le DOM et le CSSOM pour créer un arbre de tous les éléments visibles dans la balise `<body>` avec leurs styles CSS calculés.

Cet arbre est appelé **arbre de rendu**, **arbre de rendu** ou **arbre de frame**.

Les pseudo-éléments CSS, qui ont `content`, seront également dans l'arbre de rendu.

L'objectif est maintenant de transformer l'arbre de rendu en une image.

### Mise en page – pour recalculer la géométrie des éléments après un changement

La géométrie d'un élément HTML peut affecter les frères et sœurs et les enfants.

Lorsque votre code ajoute (ou supprime) un élément ou change son style, le navigateur recalcule la _nouvelle_ dimension et position de cet élément.

Il calcule également la dimension et la position de chaque frère/enfant qu'il peut affecter.

Par exemple, si vous augmentez le `margin-top` d'un paragraphe avec JavaScript, il repoussera tous les éléments suivants sur le document.

Ou si la `width` d'un conteneur devient plus petite, ses enfants pourraient devoir réduire leur taille également.

Cela dit, un simple changement de la géométrie d'un élément peut forcer le navigateur à recalculer la géométrie de centaines d'autres éléments affectés (directement ou indirectement) par le changement.

Le navigateur utilise l'arbre de rendu pour recalculer la géométrie de chaque élément visible dans la fenêtre.

Ce processus est également connu sous le nom de **reflow**.

## Peinture – Lorsque le code est converti en pixels

À ce stade, le navigateur web a toutes les structures de données dont il a besoin. Les styles sont calculés, et la mise en page est prête.

Selon le moteur de rendu (Blink, Gecko, etc.), plus d'abstractions et de structures de données auxiliaires sont créées en interne. Mais comme les internes du navigateur tendent à changer assez fréquemment, nous garderons notre discussion aussi générale que possible.

L'étape suivante consiste à transformer le code en pixels. Ce processus est appelé peinture.

À cette étape, le moteur de rendu du navigateur crée une [liste d'affichage](https://en.wikipedia.org/wiki/Display_list) de commandes de dessin pour chaque élément de l'arbre de rendu.

Ces commandes ressemblent à des commandes de dessin de base : **dessiner un rectangle**, **dessiner un cercle** ou **dessiner un morceau de texte à ces coordonnées**.

Google Chrome utilise [Skia](https://skia.org/) pour effectuer le travail de dessin. Skia est une bibliothèque graphique 2D qui fournit des API standard sur diverses plateformes.

Chrome enregistre ces commandes dans un objet Skia `[SkPicture](https://api.skia.org/classSkPicture.html)`. SkPicture a une méthode `playback`, qui envoie les commandes de dessin une par une au canevas spécifié.

Finalement, la sortie des listes d'affichage serait un ensemble de **bitmaps**.

Pour nous assurer que nous sommes tous sur la même page, définissons rapidement ce qu'est un bitmap.

Vous savez peut-être qu'un pixel (élément d'image) est le plus petit élément d'une image numérique. Chaque image est une grille de pixels (a*b), et chaque pixel a une couleur spécifique. Ces pixels ensemble forment l'image.

Maintenant, qu'est-ce qu'un bitmap ?

Bitmap (dans un contexte graphique) est une méthode de stockage des informations de couleur de chaque pixel sous forme d'un ensemble de bits.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Twitter-post---59.png)
_**[CC0 1.0](https://en.wikipedia.org/wiki/Raster_graphics#/media/File:Rgb-raster-image.svg">Le visage souriant</a>** (remixé), sous licence **<a href="https://creativecommons.org/publicdomain/zero/1.0/deed.en)**_

Dans l'image ci-dessus, trois pixels sont mis en évidence avec leurs informations de couleur (un mélange de rouge, vert et bleu).

Ces valeurs ensemble forment le bitmap de l'image.

D'autre part, un bitmap est la manière dont les ordinateurs stockent les images dans la mémoire ou un dispositif de stockage.

Transformer le contenu d'une page web en bitmaps est connu sous le nom de **peinture** ou **rasterisation**.

Rien n'est encore peint, cependant. Cette étape est plus une configuration de peinture (ou pré-peinture) que le travail de peinture réel.

### Les éléments sont peints sur plusieurs couches

Le travail de peinture réel est effectué à la discrétion du compositeur plus tard. Mais le moteur de rendu fournit suffisamment d'indices au compositeur sur la manière dont les éléments doivent être peints sur plusieurs couches.

Certains éléments sont regroupés en une seule couche et rasterisés ensemble (ils partagent le même bitmap). Cependant, certains éléments sont peints sur une couche dédiée.

Par exemple, dans l'animation ci-dessous, les éléments sont peints sur quatre couches :

%[https://youtu.be/sSgtcdklEgQ]

Vous pouvez voir ces couches dans le panneau Layers.

Pour activer le panneau Layers, dans Chrome DevTools, maintenez ⌘+⇧+P (ou Ctrl+⇧+P) pour activer la Palette de commandes. Ensuite, tapez "Show Layers" et exécutez-le.

Ces couches (également connues sous le nom de composite layers) rendent la composition possible.

Ces composite layers sont ensuite combinées dans l'ordre défini et forment l'image finale (plus d'informations à ce sujet ci-dessous).

Les composite layers sont similaires aux couches dans les éditeurs de graphiques raster tels que Photoshop. En gérant les formes comme des couches, le designer peut transformer une forme sans affecter les autres formes.

Si vous vouliez changer quelque chose sur une image aplatie, vous devriez peut-être tout redessiner.

Comme Photoshop, peindre des éléments sur des couches séparées permet au navigateur web de réduire considérablement le travail de peinture.

Ainsi, si un élément sur une couche est invalidé (il est changé), seules les zones invalidées (tuiles) de la couche respective doivent être repeintes.

Le moteur de rendu considère divers facteurs pour prendre les décisions de couche. Par exemple, si l'opacité CSS d'un élément changera à l'exécution, il sera rasterisé sur une couche dédiée.

Vous pouvez également promouvoir un élément à être peint sur une couche dédiée avec les propriétés CSS `will-change` ou `translateZ(0)`.

Vous devriez toujours promouvoir une couche pour une raison, cependant.

Avoir de nombreuses couches entraînera des coûts en mémoire et en temps de traitement. Cela peut devenir problématique sur les appareils à capacité limitée.

### Composition : lorsque la frame finale est générée

Le compositeur reçoit une liste d'affichage du moteur de rendu avec des structures de données auxiliaires.

Son travail (entre autres) est d'organiser le dessin des éléments en plusieurs couches.

Selon ce qui se trouve sur la page (et ses styles), la peinture peut être effectuée par logiciel (rasterisation logicielle) ou directement sur le GPU (rasterisation matérielle).

Voici comment cela fonctionne sur Google Chrome (pour les autres navigateurs, vous devriez consulter leurs documents de conception) :

Dans le cas de la rasterisation logicielle, les commandes graphiques sont exécutées par un ensemble de threads de travail de rasterisation, puis les bitmaps générés sont partagés avec le GPU sous forme de textures.

Cependant, si la rasterisation matérielle intervient, Skia génère les bitmaps directement sur le GPU en émettant des commandes de bas niveau vers l'API graphique du système d'exploitation.

Une fois les couches prêtes, le compositeur peut appliquer des transformations de niveau compositeur (comme `transform` et `opacity`) sur chaque couche.

Et enfin, il combine (composite) les couches en une seule. Si l'accélération matérielle est activée, la composition sera également effectuée sur le GPU – en émettant des commandes de bas niveau vers l'API graphique du système d'exploitation.

Rappelez-vous cette partie car elle joue un grand rôle dans l'optimisation des performances d'animation.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-16-at-18.01.03-1.png)
_Couches après avoir été composées_

Chaque fois que je pense aux composite layers, cela me rappelle l'ancienne production d'animation sur celluloïd, où chaque frame était dessinée sur une feuille de celluloïd transparente.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/cel-animation-frame.jpeg)
_[CC BY-NC 2.0](https://www.flickr.com/photos/gogdog/5281815537">**Mon GunBuster Animation Cel**</a>, sous licence **<a href="https://creativecommons.org/licenses/by-nc/2.0/)**_

L'arrière-plan était un dessin statique, et l'animateur le décalait vers la gauche d'un pouce (avec un rouleau) et plaçait la prochaine frame de celluloïd dessus.

Cette technique a considérablement réduit le travail de dessin et a aidé les studios d'animation à distribuer le travail de conception à plusieurs équipes.

Vous pouvez regarder cette vidéo de la production d'animation de Disney [Blanche-Neige](https://www.youtube.com/watch?v=aQkJM13PMKw) si vous êtes curieux de cette ancienne méthode de production.

La composition dans les navigateurs a un but similaire : **minimiser le travail de peinture lorsqu'un changement se produit.**

C'est la dernière étape du pipeline – où une nouvelle frame est née.

## Comment optimiser les activités du pipeline

Une question reste cependant. Comment puis-je éviter les mouvements saccadés des pages et arrêter d'ennuyer mes utilisateurs ?

Voici quelques choses que vous devriez faire.

### Connaître les changements les plus coûteux

Tous les changements n'impliquent pas toutes les activités du pixel pipeline. Certains changements nécessitent moins de travail et peuvent sauter une étape ou deux.

Tout changement de la géométrie d'un élément (lorsque vous changez la hauteur, la largeur, la gauche, le haut, le bas, la droite, le remplissage, la marge, etc.) implique tout le pipeline.

Ce type de changement est le changement le plus coûteux que vous puissiez apporter à une page web.

Parfois, c'est nécessaire, mais parfois, c'est totalement évitable (je vous dirai comment).

![Image](https://www.freecodecamp.org/news/content/images/2022/02/pipeline-full-1.png)
_Toutes les étapes du pixel pipeline_

### Optimiser le travail de peinture

Si vous changez la propriété `background-color` d'une div, le navigateur n'aura pas à recalculer sa géométrie – car vous n'avez changé que la couleur.

Cela signifie que le navigateur web **saute l'étape de mise en page** cette fois et passe directement à la peinture.

La peinture reste une tâche coûteuse. Cependant, vous pouvez l'optimiser en réduisant la complexité de la peinture – en choisissant des styles plus simples plutôt que des styles compliqués.

Par exemple, les ombres de texte ou les dégradés sont plus coûteux qu'une simple couleur de fond.

Demandez-vous toujours si vous pouvez choisir un ensemble de styles moins coûteux. Parfois, ils ne font aucune différence en termes d'esthétique.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/pipeline-paint.png)
_Pixel pipeline sans l'étape de mise en page_

### **Utiliser des transformations uniquement composées**

Certains changements ne nécessiteront pas de mise en page et de peinture car le compositeur peut les appliquer seul.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/pipeline-composite.png)
_Le pixel pipeline sans mise en page et peinture_

Voici la liste des changements que le navigateur peut faire à moindre coût au moment de la composition :

* **Repositionnement** avec transform : `translate(mpx, npx)`
* **Rotation** avec `transform:rotate(xdeg)`
* **Mise à l'échelle** avec `transform: scale(x)`
* **Opacité** avec `opacity(x)`

Ces propriétés CSS semblent être tout ce dont vous avez besoin lorsque vous apportez une modification à une page (eh bien, la plupart du temps) !

Mieux encore, si l'accélération matérielle est maintenue, le compositeur peut utiliser la puissance de calcul du GPU pour appliquer ces transformations. Les GPU sont créés pour ce type de charge de travail.

Ainsi, selon la modification que nous apportons au DOM, le processus sera l'un de ces trois scénarios.

* JavaScript → Style → Mise en page → Peinture → Composition
* JavaScript → Style → Peinture → Composition
* JavaScript → Style → Composition

**"La performance est l'art d'éviter le travail."**

Et bien sûr, le dernier scénario est la route la moins coûteuse à choisir.

### Essayez de réduire la charge de travail du thread principal

Un navigateur web est essentiellement un [programme informatique](https://www.decodingweb.dev/books/processing-fundamentals/how-a-computer-program-works), et en tant que programme informatique, il aura un ou plusieurs processus en mémoire pendant son exécution.

La plupart des navigateurs ont une architecture multi-processus, où les activités sont distribuées sur plusieurs threads de différents processus (comme le processus Renderer et le processus GPU, le processus Browser, etc.).

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Google-chrome-processes.png)
_Le processus Renderer et GPU dans Google Chrome_

Dans le cas de Chrome, JavaScript, Style, Layout, paint setup se produisent dans le thread principal du processus Renderer (chaque onglet a un Renderer dédié).

C'est presque tout !

Le contenu HTML que votre navigateur récupère initialement via une [requête HTTP](https://www.decodingweb.dev/books/decoding-web-development/http) est analysé sur un thread dédié, mais le rendu et tout contenu que vous ajoutez est analysé sur le thread principal.

Cela dit, l'accent doit être mis sur le fait de soulager le thread principal. Et en retour, cela nous aide à avoir une fréquence d'images constante.

Le site [CSS Triggers](https://csstriggers.com/) peut vous aider à comprendre comment la modification d'une propriété CSS déclenche la mise en page, la peinture et la composition.

Vous pouvez également utiliser cette feuille de triche que j'ai créée :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Twitter-post---55.png)
_Propriétés CSS et leur étape initiale dans le pixel pipeline_

### Assurez-vous que vos rappels JavaScript attrapent le train !

D'accord, maintenant nous savons comment aider le navigateur à faire moins d'étapes (quand c'est possible !), mais il y a une autre chose à considérer.

Qu'il s'agisse d'une animation ou d'un changement ponctuel, nous devons nous assurer que nos changements sont synchronisés avec la fréquence d'images à laquelle le navigateur affiche le contenu.

Que signifie-t-il même ? Vous pourriez demander.

Imaginez un train en mouvement avec de nombreux wagons.

Ce train se déplace rapidement, et vous avez 16,7 ms pour dessiner une image et la jeter dans chaque wagon (tout en bougeant).

Si vous ne parvenez pas à charger un wagon en 16,7 ms, il s'arrêtera brièvement jusqu'à ce que vous jetiez l'image.

<iframe src="https://giphy.com/embed/TlK63EDww4g4tXUd0gE" width="480" height="320" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/train-subway-station-TlK63EDww4g4tXUd0gE">via GIPHY</a></p>

Ce train en mouvement peut être n'importe quel mouvement sur la page web. Il pourrait s'agir d'une animation, d'une transition, d'un défilement de page, d'une sélection de texte ou de tout autre mouvement.

Si le train doit s'arrêter pour vous, il livrera les frames avec un retard. Les utilisateurs le remarqueront, et ils ne l'aimeront pas !

Chaque fois que vous voulez changer la page, vous devez somehow glisser votre travail dans un créneau de 16,7 ms sans le ralentir.

Parfois, c'est délicat à faire, cependant.

De nombreux développeurs utilisent encore `setInterval()` pour créer une boucle temporisée. Par exemple, pour répéter une action ou créer une animation.

Il y a un problème avec `setInterval()`, cependant. Il n'a pas assez de précision pour exécuter votre code à la fréquence exacte que vous définissez.

Si vous définissez l'intervalle pour répéter votre code toutes les 16,7 ms, votre code pourrait s'exécuter à n'importe quel moment pendant chaque créneau de 16,7 ms.

Ainsi, si nous avons 16,7 ms pour apporter une modification, générer la frame et la charger sur son wagon dédié, nous devons nous assurer que notre code s'exécute dès le début de chaque créneau de 16,7 ms.

Sinon, cela nécessiterait plus de 16,7 ms pour se terminer, et il ne sera pas prêt pour le créneau actuel.

Et si il y avait un moyen d'exécuter le rappel dès le début de chaque créneau de 16,7 ms ?

`RequestAnimationFrame()` a été conçu juste pour cela.

Il garantit que vos rappels sont exécutés dès le début de la frame suivante.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/requestanimationframe.png)
_requestAnimationFrame() v.s. setInterval()_

De cette manière, votre code a une chance plus élevée de se terminer dans les 10 ms pour laisser suffisamment de temps au navigateur web pour faire ses trucs internes dans la durée totale de 16,7 ms.

Ainsi, au lieu de :

```javascript
setInterval(
	() => {
    	// faire un changement
    },
    16.7
)
```

Vous pouvez faire :

```javascript
const animateSomething = function () {
	// faire un changement
    
    // Prochain appel
    requestAnimationFrame(animateSomething)
}

// Premier appel manuel pour démarrer l'animation
requestAnimationFrame(animateSomething)
```

Un autre avantage de l'utilisation de `requestAnimationFrame` est que le navigateur peut exécuter votre animation plus efficacement.

Par exemple, si l'utilisateur passe à un autre onglet, le navigateur mettra en pause l'animation. Cela réduit le temps de traitement et la durée de vie de la batterie.

## Comment optimiser une animation – Voyez-le en action

Comme promis, il est temps de faire quelques expériences.

Pour cette expérience, j'ai créé une animation de deux manières différentes.

L'animation concerne un avion volant à l'horizon au coucher du soleil.

Dans la première approche, j'ai utilisé toutes les propriétés déclenchant la mise en page (left & top) sans me soucier des compromis de performance.

J'ai également utilisé `setInterval` avec une fréquence de 16,7 ms pour ma boucle temporisée.

Dans la deuxième approche, j'ai refactorisé le code et utilisé des styles uniquement de compositeur. J'ai également promu mon élément en mouvement (l'avion) avec la propriété `will-change` pour m'assurer qu'il aura sa propre couche.

J'ai également remplacé `setInterval` par `requestAnimationFrame` pour un meilleur timing.

Pour simuler le mouvement de l'avion, j'ai utilisé `Math.sine()` avec quelques ajustements. Le chemin de voyage est également dessiné avec un graphique sinusoïdal basé sur SVG.

Voici le [lien CodePen](https://codepen.io/lavary/pen/YzEpLbE) de la première approche :

%[https://codepen.io/lavary/pen/YzEpLbE]

Et [la deuxième approche](https://codepen.io/lavary/pen/eYvOojp) avec la promotion de couche (`will-change: transform`), des styles uniquement de compositeur (`transform: translate()`), et `requestAnimationFrame` :

%[https://codepen.io/lavary/pen/eYvOojp]

### Comparons les deux approches

L'une des métriques que vous pouvez utiliser est la fréquence d'images. Elle vous aide à surveiller la cohérence des frames pendant un mouvement.

Jetez un coup d'œil à l'enregistrement ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/animation-paint.png)

Vous pouvez voir le compteur FPS dans l'image ci-dessus (en haut à gauche de la capture d'écran). Bien que la capture d'écran montre 90 fps, les barres jaunes/rouges indiquent que certaines frames ont été manquées ou retardées.

Le journal des événements (en bas à droite) montre toutes les étapes impliquées pendant l'enregistrement : **Recalculer le style > Mise en page > Peinture > Composition des couches.**

Pour activer le compteur FPS, dans Chrome DevTools, maintenez ⌘+⇧+P (ou Ctrl+⇧+P) pour activer la Palette de commandes. Ensuite, tapez `FPS meter` et choisissez Afficher le compteur de frames par seconde (FPS).

Et voici un guide rapide pour le lire :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/FPS-meter.png)
_Compteur FPS_

Maintenant, mesurons la deuxième approche :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/animation-composite.png)

Dans le deuxième enregistrement, le FPS moyen est de 118,8 sans frames manquantes ou perdues.

Le journal des événements confirme également qu'aucune mise en page et aucun travail de peinture n'ont été nécessaires, et que le compositeur a fait tout le travail (Recalculer le style → Composite Layer).

Vous pouvez également utiliser l'outil **Paint Flashing** de Chrome pour voir quelles parties de la page sont repeintes. Cela est utile pour détecter les travaux de peinture indésirables pendant les interactions de l'utilisateur.

Dans l'exemple de l'avion, la zone repeinte (l'avion en mouvement) est affichée sous forme de rectangles à bordure verte.

%[https://youtu.be/1rd2aemUGCE]

L'activation du paint flashing pour la deuxième approche ne montrera rien car il n'y a pas de travail de peinture pendant l'animation.

La question est : un utilisateur peut-il remarquer cette amélioration ?

Voyons voir.

Voici les deux animations au ralenti (10x ralenties) pour voir s'il y a un changement :

%[https://youtu.be/X05WCbC-ITY]

Je vous laisse en juger.

## Trop long ; n'ai pas lu ?

Pour avoir des mouvements fluides sur votre page, tout ce que vous avez à faire est de vous assurer que :

* Les frames sont livrées à temps
* Les frames sont livrées à temps **de manière constante**

Et voici une liste de contrôle pour y parvenir :

* Assurez-vous que vos changements JavaScript se produisent au début de chaque frame en utilisant `requestAnimationFrame`.
* Lorsque vous changez la dimension d'un élément, utilisez `transform:scale()` plutôt que `height` & `width`.
* Pour déplacer les éléments, utilisez toujours `transform: translate()` plutôt que les coordonnées (`top`, `right`, `bottom`, et `left`).
* Réduisez la complexité de la peinture en utilisant des styles CSS simples plutôt que des styles coûteux. Par exemple, si possible, utilisez des couleurs unies plutôt que des dégradés ou des ombres.
* Normalisez l'utilisation des transitions sur les versions mobiles. Bien que la capacité de calcul des téléphones mobiles soit limitée, l'UX des versions mobiles contient souvent plus de transitions/effets en raison de leur petit écran.
* Utilisez les outils de développement de votre navigateur pour diagnostiquer les performances d'animation. Utilisez des outils tels que Paint Flashing et FPS meter pour affiner vos animations.
* Utilisez le panneau Performance de DevTool pour voir comment votre code s'exécute sur des appareils bas de gamme.

Vous pouvez appliquer ces micro-optimisations lorsque vous effectuez tout type de changement. Que vous créiez une animation JavaScript ou CSS, ou que vous apportiez simplement une modification ponctuelle avec JavaScript.

C'était la phrase d'ouverture de ce guide :

> Et si je vous disais que les pages web étaient des animations interactives lues par votre navigateur web.

Mais, et si je vous disais maintenant que ce n'était que la partie émergée de l'iceberg ?!

Ne vous inquiétez pas, vous pouvez déjà faire beaucoup pour rendre vos pages web agréables à l'œil.

Si vous voulez porter vos connaissances en performance au niveau supérieur, je tiens à jour une [page dédiée pour collecter des ressources sur les performances web de divers créateurs](https://www.decodingweb.dev/courses/web-performance). Consultez-la !

Si vous avez des questions ou des commentaires ou s'il y a quelque chose que j'ai manqué (ou que j'ai mal compris), n'hésitez pas à me le faire savoir sur **@lavary_** sur Twitter.

Merci d'avoir lu !

### Attributions :

* Image du post : **[Antics 2-D Animation of White Rabbit](https://commons.wikimedia.org/wiki/File:Antics_2-D_Animation_infobox_screenshot.png)** (l'image a été recadrée) par **Antics Workshop** sous **[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)**