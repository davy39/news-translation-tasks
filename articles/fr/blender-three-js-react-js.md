---
title: Comment implémenter un modèle Blender dans une application React.js en utilisant
  Three.js
subtitle: ''
author: Matthes B.
co_authors: []
series: null
date: '2023-08-17T14:58:49.000Z'
originalURL: https://freecodecamp.org/news/blender-three-js-react-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/pexels-chevanon-photography-1335971.jpg
tags:
- name: animations
  slug: animations
- name: React
  slug: react
- name: three.js
  slug: three-js
seo_title: Comment implémenter un modèle Blender dans une application React.js en
  utilisant Three.js
seo_desc: "In this step-by-step guide, you'll learn how to build a basic Blender file\
  \ with incorporated fundamental animations. After that, you'll learn how to integrate\
  \ Three.js with your React apps using React Three Fiber. \nGetting familiar with\
  \ these concept..."
---

Dans ce guide étape par étape, vous apprendrez à créer un fichier Blender de base avec des animations fondamentales intégrées. Ensuite, vous apprendrez à intégrer Three.js avec vos applications React en utilisant React Three Fiber. 

Se familiariser avec ces concepts peut vous aider à vous assurer que vos prochaines applications React.js se démarquent.

## **\ud83d\udd10** Voici ce que nous allons couvrir :

* Création d'un modèle Blender, incluant des animations, des matériaux et le processus d'exportation.
* Construction d'une application React.js intégrée avec Three.js via React Three Fiber.
* Incorporation de votre modèle Blender personnellement créé dans l'application React.js.

## **\ud83d\udcdd** Prérequis :

* Une compréhension fondamentale du logiciel 3D Blender est recommandée.
* Une familiarité de base avec React.js est requise.
* Aucune expérience préalable avec Three.js n'est nécessaire.

## Table des matières

1. [\ud83d\udcad Qu'est-ce que Three.js et Blender ?](#heading-quest-ce-que-threejs-et-blender)
2. [\ud83d\udd27 Comment configurer React.js avec Three.js](#heading-comment-configurer-reactjs-avec-threejs)
3. [**\ud83d\udd28** Comment créer un modèle Blender](#heading-comment-creer-un-modele-blender)
4. [**\u270f\ufe0f** Cuisson de texture pour les matériaux procéduraux](#heading-cuisson-de-texture-pour-les-materiaux-proceduraux)
5. [**\u2712\ufe0f** Comment implémenter le modèle Blender dans l'application React.js](#heading-comment-implementer-le-modele-blender-dans-lapplication-reactjs)
6. [**\ud83d\udcc4** Informations supplémentaires](#heading-informations-supplementaires)
7. [**\ud83d\udccb** Conclusion](#heading-conclusion)

## \ud83d\udcad Qu'est-ce que Three.js et Blender ?

Three.js est une bibliothèque JavaScript qui fonctionne comme une API, vous permettant d'afficher des modèles 3D dans des navigateurs web. 

Utiliser Three.js vous aide à intégrer de manière transparente l'interactivité et des fonctionnalités distinctives dans votre site web. 

Blender est un logiciel robuste conçu pour créer et affiner des modèles 3D. Sa polyvalence offre des opportunités illimitées, répondant à un large spectre de visions créatives.

Au-delà de ses capacités d'affichage, Blender vous fournit une série d'outils incluant des caméras, des éclairages, et même des améliorations post-production.

Lorsque ces outils sont utilisés ensemble, ils facilitent une créativité sans limites, vous permettant de traduire de manière transparente vos créations artistiques dans votre prochain projet de site web.

## \ud83d\udd27 Comment configurer React.js avec Three.js

Pour commencer le processus, installez l'application React.js :

`npx create-react-app my-app`

Ensuite, nous installerons Three.js et [React Three Fiber](https://docs.pmnd.rs/react-three-fiber/getting-started/installation). React Three Fiber sert de moteur de rendu React pour Three.js, exploitant la puissance des composants React pour simplifier l'intégration de Three.js dans un environnement React.js :

`npm install three @react-three/fiber`

Pour une expérience enrichie avec Three.js, nous intégrerons également [React Three Drei](https://www.npmjs.com/package/@react-three/drei), un package qui introduit une assortiment d'aides pour divers scénarios Three.js, incluant plusieurs contrôles de caméra, par exemple :

`npm install @react-three/drei`

### Extension glTF Tools

Je recommande également d'installer l'extension **glTF Tools**. Bien que ce ne soit pas strictement nécessaire, cette extension peut vous aider à effectuer diverses tâches. 

Si vous utilisez Visual Studio Code comme votre environnement de développement intégré (IDE), vous pouvez ajouter l'extension de manière pratique via l'onglet des extensions. Encore une fois, cette extension est optionnelle, mais elle peut simplifier considérablement certains processus plus tard. Je l'utiliserai tout au long de ce tutoriel :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/React1.0.PNG)
_Extension **gltf Tools** dans Visual Studio Code_

### Configuration terminée pour Three.js dans React.js

Les dépendances dans le fichier `package.json` de notre application React.js apparaissent maintenant comme suit :

```javascript
"dependencies": {
    "@react-three/drei": "^9.80.2",
    "@react-three/fiber": "^8.13.6",
    "@testing-library/jest-dom": "^5.17.0",
    "@testing-library/react": "^13.4.0",
    "@testing-library/user-event": "^13.5.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1",
    "three": "^0.155.0",
    "web-vitals": "^2.1.4"
  },
```

Ces dépendances sont suffisantes pour accomplir une variété de tâches avec Three.js dans un environnement React.js. Bien sûr, vous pouvez incorporer toute bibliothèque supplémentaire que vous pourriez désirer pour des fins au-delà de l'intégration de Three.js.

En plus de cela, j'ai également rendu le code de ce tutoriel disponible sur [GitHub](https://github.com/Matthes-Baer/blender-threejs-reactjs-article-app). Cela vous permettra d'accéder rapidement aux informations sans avoir à faire défiler tout l'article.

## \ud83d\udd28 Comment créer un modèle Blender

Pour commencer, notre première tâche consiste à créer un modèle Blender qui sera ensuite intégré dans notre application React.js. Pour cette étape, considérons une scène dans l'onglet **Layout** où nous avons trois objets : deux sphères et un plan. Vous pouvez ajouter de tels objets avec le raccourci `Shift + A` dans Blender.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/blenderFirstImage.PNG)
_Scène Blender avec deux sphères et un plan dans l'onglet **Layout**_

Cette composition inclut simplement un plan et deux sphères, sans détails supplémentaires. Bien sûr, vous pouvez travailler sur des conceptions de scènes et de modèles plus élaborées selon vos préférences. 

Mais pour illustrer le processus fondamental d'incorporation de vos modèles Blender personnalisés dans React.js, cet exemple de base nous suffira.

### Comment ajouter des animations au modèle

Maintenant, notre attention se porte sur l'introduction d'animations de base à tous les trois objets dans cette scène Blender. Ces animations peuvent faciliter le mouvement, la rotation, ou même des ajustements d'échelle pour les objets, permettant des transformations dynamiques.

Pour ajouter des animations dans Blender pour vos objets, vous pouvez passer à l'onglet **Animation**, à côté des onglets **Shading** et **Rendering**.

Dans l'onglet Animation, vous pouvez ajouter des points à une certaine frame. Par exemple, si vous voulez déplacer une sphère un peu vers la gauche, commencez par ajouter une frame clé de départ (clic droit sur l'objet, choisissez "Insert Keyframe", puis sélectionnez "Location"). 

Ensuite, avancez de quelques frames sur la timeline d'animation de l'objet, ajustez la position de l'objet, et répétez le même processus. De cette façon, vous aurez deux frames clés : celle initiale et la nouvelle position.

Rappelez-vous, ce mouvement est dans une seule direction. Si vous voulez répéter l'animation, elle se déplacera vers le nouvel emplacement puis reviendra à sa position initiale avec un saut. 

Pour rendre le mouvement plus fluide, vous pouvez copier la frame clé initiale et l'insérer à la fin. Cela fera en sorte que l'objet revienne avec un mouvement fluide après avoir atteint le nouvel emplacement. C'est aussi ainsi que j'ai configuré les frames clés dans notre modèle Blender.

Bien sûr, vous pouvez ajouter plus de frames clés pour créer des animations plus complexes. Ceci n'est qu'une introduction de base pour commencer avec les animations Blender. Comme de nombreux aspects de Blender, il y a beaucoup plus à explorer et à apprendre.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/blenderSecondImage.PNG)
_Ajout d'animations à tous les trois objets dans l'onglet **Animation**_

Dans ce contexte, il n'est pas nécessaire d'avoir une compréhension approfondie des spécificités de ces animations que nous avons ajoutées ici. Donc, vous n'avez pas vraiment besoin de savoir à quelle position exacte la première sphère est déplacée par l'animation. 

Le point clé est de reconnaître leur présence, car elles seront intégrées dans notre application React.js à une étape ultérieure afin que nous puissions les activer dans le navigateur.

### Comment ajouter des couleurs

Ensuite, nous ajouterons quelques couleurs simples pour la petite sphère et le plan sous-jacent, que vous pouvez faire dans l'onglet **Shading**, par exemple.

Pour des couleurs de base, vous pouvez également aller dans la section **Material Properties** de l'objet (clic droit sur l'objet, puis choisissez la deuxième catégorie avant-dernière en bas). Mais je veux me concentrer sur une situation spécifique que vous pourriez rencontrer avec vos modèles plus tard. Par conséquent, je vais utiliser exclusivement l'onglet **Shading** pour définir les couleurs des objets dans ce tutoriel.

Dans l'onglet **Shading**, vous pouvez ajouter des nœuds en bas de l'écran. Ces nœuds peuvent modifier la couleur et la texture d'un objet, entre autres. Vous trouverez également des nœuds `Vector` et `Shader` qui, lorsqu'ils sont combinés, peuvent créer des visuels uniques pour vos objets. 

Tous ces ajustements s'appliquent à un matériau spécifique. Donc, si vous voulez le même visuel pour différents objets, vous pouvez simplement appliquer le même matériau à eux.

Les nœuds `Principled BSDF` et `Material Output` sont initialement générés lorsque nous ouvrons l'onglet **Shading** pour rechercher le matériau d'un de nos objets pour la première fois. Les deux nœuds sont assez basiques.

Le `Principled BSDF` a beaucoup de paramètres avec lesquels vous pouvez jouer. Dans notre cas, nous voulons simplement changer la propriété `Base Color` en une couleur bleue.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/blender3.0.PNG)
_Matériau d'une sphère où nous ajustons simplement la `Base Color` dans le nœud `Principled BSDF`_

Pour la sphère plus grande, une application de matériau similaire est utilisée. Mais, contrairement au nœud `Principled BSDF`, nous utiliserons le nœud `Glossy BSDF` qui est un nœud de la catégorie `Shader`. Cela nous aidera à reconnaître un problème potentiel que vous pourriez rencontrer lors de la conception d'un modèle Blender pour votre application React.js – que vous verrez plus tard.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/blender3.2-1.PNG)
_Utilisation du nœud `Glossy BSDF` pour ajouter un matériau à la grande sphère_

Une fois que nous avons fait cela, nous sommes prêts à exporter notre modèle Blender. Notez que cette version est considérablement simplifiée. Vous pouvez travailler sur des conceptions de modèles plus détaillées adaptées à vos préférences. Cependant, le flux de travail global reste similaire.

### Comment exporter le modèle

Pour exporter le modèle, nous devons générer un fichier `.glb/.gltf`. Cela est crucial car Three.js attend des formats de fichiers particuliers pour la compatibilité, et dans ce cas, un fichier `.glb` ou `.gltf` est conforme aux exigences de la bibliothèque.

Donc, une fois que vous avez terminé de créer votre modèle avec des objets, des animations, des couleurs, et plus encore, vous pouvez faire ce qui suit :

1. Cliquez sur l'onglet **File** situé dans le coin supérieur gauche.
2. Choisissez **Export** parmi les options qui apparaissent. Maintenant, une variété de formats d'exportation sera affichée.
3. Si vous prévoyez d'utiliser votre modèle avec Three.js dans votre application, vous devez choisir l'option `glTF 2.0 (.glb/.gltf)`, comme je l'ai mentionné précédemment.

Après avoir sélectionné cette option, une nouvelle fenêtre s'ouvrira. Cette fenêtre vous permet de choisir le dossier où vous souhaitez enregistrer votre fichier. 

Sur le côté droit de cette fenêtre, il y a des choix supplémentaires. Vous pouvez décider quels objets spécifiques vous souhaitez exporter, par exemple. Dans la plupart des situations, les paramètres par défaut devraient bien fonctionner. Rappelez-vous simplement que vous pouvez ajuster ces paramètres à votre guise si nécessaire.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/blender3.1-1.png)
_Rappelez-vous d'exporter avec le format `glTF 2.0 (.glb/.gltf)`._

### Comment visualiser le modèle exporté

Ensuite, passons à Visual Studio Code et naviguons vers le dossier où nous avons stocké notre fichier exporté. 

Dans ce répertoire, vous trouverez un fichier `.glb`. En revenant à la configuration de l'extension **glTF Tools** précédente, vous pouvez simplement faire un clic droit sur le fichier `.glb` afin de trouver deux options supplémentaires positionnées en bas, appelées `glTF: Import from GLB` et `glTF: Validate a GLB or GLTF file`.

Dans ce scénario, nous opterons pour l'option `glTF: Import from GLB`. Cette action générera un fichier `.gltf` dans le même dossier, dans notre cas `blenderFile.gltf`.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/blender4.0.png)
_Génération d'un fichier `.gltf` à partir du fichier `.glb` original que nous avons exporté dans Blender avec l'extension **glTF Tools**_

Nous avons choisi cette approche pour apporter une accessibilité améliorée au fichier `.gltf`, permettant une visualisation directe dans Visual Studio Code via l'extension **glTF Tools**. Cela peut être très utile pour vérifier votre fichier avant son implémentation réelle.

Si nous accédons au fichier `.gltf` nouvellement créé, nous pouvons observer un ensemble d'informations basées sur le modèle Blender. Il est important de noter que les spécificités pourraient différer dans votre cas, car elles sont adaptées pour refléter les attributs des objets et des scènes dans votre projet Blender.

Si nous regardons dans le coin supérieur droit, il y a un symbole qui ressemble à un cube avec un cône à côté. En cliquant sur ce symbole, vous pouvez prévisualiser votre scène Blender directement dans votre IDE. Cette fonctionnalité est exclusivement accessible pour le fichier `.gltf` et non applicable au fichier `.glb` dans ce cas.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/blender4.5.png)
_Le fichier `.gltf` nouvellement créé avec l'option de visualiser le modèle directement dans Visual Studio Code (dans le coin supérieur droit, encerclé en rouge)_

Il est intéressant de noter que vous n'êtes pas obligé de faire cela via l'extension **glTF Tools**. Alternativement, divers sites web vous permettent de télécharger votre fichier pour visualisation. Mais j'ai personnellement trouvé cette approche dans l'IDE particulièrement pratique. Elle centralise le processus, vous permettant d'évaluer l'intégrité de votre fichier avant de l'implémenter réellement. 

Si vous trouvez des erreurs, cette pratique vous permet de découvrir à l'avance si le problème est basé sur une exportation de fichier problématique ou simplement une négligence d'implémentation dans votre application React.js. Par conséquent, je recommande vivement d'évaluer votre fichier de modèle après son exportation depuis Blender.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/blender5.0.PNG)
_Visualisation du modèle Blender avec **glTF Tools** dans Visual Studio Code_

En utilisant l'extension **glTF Tools** pour visualiser notre modèle Blender dans Visual Studio Code, nous pouvons voir que les trois objets sont correctement reconnus. La petite sphère et le plan sont affichés dans leurs couleurs prévues.

Mais la grande sphère n'a pas la couleur attendue assignée et apparaît simplement avec une couleur blanche par défaut à la place. 

Cette divergence soulève la question : qu'est-ce qui a conduit à cette anomalie ? C'est dans des circonstances comme celle-ci que l'on démontre à quel point il est utile de prévisualiser votre modèle avant de l'intégrer dans votre application React.js.

En examinant votre modèle à ce stade, vous pouvez affirmer que le problème provient du modèle Blender lui-même plutôt que du processus d'implémentation, étant donné que nous n'avons encore rien implémenté. 

Cette évaluation pré-implémentation s'avère pratique et vous permet de diagnostiquer et de résoudre les complications potentielles avant de procéder au processus d'implémentation dans React.js.

## \u270f\ufe0f Cuisson de texture pour les matériaux procéduraux

En résumé, Blender offre la flexibilité d'utiliser des nœuds procéduraux pour vos matériaux. Bien que ces nœuds fonctionnent de manière transparente dans Blender, ils ne sont pas directement compatibles avec d'autres moteurs de jeu ou frameworks logiciels tels que Three.js. 

Pour en savoir plus, envisagez de regarder la vidéo suivante. En seulement 10 minutes, elle démontre le processus de cuisson de texture, qui résout efficacement le problème en question. 

%[https://www.youtube.com/watch?v=AioskAgcU2U]

Personnellement, confronté à ce défi et initialement incertain de sa nature, j'ai trouvé cette vidéo être une ressource précieuse pour obtenir des informations plus approfondies sur le sujet.

Dans notre scénario spécifique, bien que nous ne rencontrions pas une situation aussi complexe que celle vue dans la vidéo, nous sommes toujours confrontés à l'utilisation de nœuds qui manquent de compatibilité directe avec divers outils logiciels.

Ensuite, nous allons brièvement parcourir les étapes mentionnées dans la vidéo. Cependant, si vous êtes intéressé à approfondir ce processus, je vous recommande vivement de regarder la vidéo.

### Comment créer un nœud de texture d'image

Pour commencer, dans l'onglet **Shading** pour le matériau contenant le nœud `Glossy BSDF`, nous introduirons un nœud `Image Texture` et le connecterons à une nouvelle image (en cliquant sur `New`). 

Nous laisserons les paramètres à leurs valeurs par défaut, ce qui signifie une largeur et une hauteur de `1024px`. L'utilisation de valeurs plus grandes prolongera considérablement le temps de traitement que nous allons rencontrer. Cependant, il est important de noter qu'une texture plus grande peut offrir plus de détails et une apparence globale améliorée. 

Dans notre situation actuelle, nous visons un processus rapide. Mais pour des projets plus importants, la qualité visuelle pourrait être cruciale. Dans de tels cas, opter pour une résolution plus élevée pourrait être souhaitable.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/blender6.0-1.PNG)
_Création d'un nœud `Image Texture` et assignation d'une nouvelle image avec les paramètres par défaut_

### Comment appliquer le processus Smart UV Project

Ensuite, nous devons utiliser l'option `Smart UV Project` située dans l'onglet **UV Editing**. Essentiellement, cette action déploie les faces de l'objet particulier sur une texture. 

Ce processus nous permet de spécifier quelles parties de la texture doivent être colorées et modifiées dès que nous sommes de retour dans l'onglet **Shading**. Pour rendre ce processus efficace, nous devons sélectionner toutes les faces de la grande sphère.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/blender7.0.png)
_Sélection de toutes les faces de l'objet dans l'onglet **UV Editing** et application de `Smart UV Project` sur celui-ci_

Une fois que nous avons terminé cette étape et utilisé les paramètres par défaut pour la procédure `Smart UV Project`, l'image de gauche – précédemment présentant une grille – affichera maintenant les formes de la sphère à laquelle nous avons appliqué ce processus. Dans notre situation, il semble que la texture ait capturé divers angles de notre sphère.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/blender8.0.PNG)
_La texture après `Smart UV Project`_

Selon l'objet spécifique, vous devrez peut-être ajuster les paramètres présentés après avoir cliqué sur le bouton `Smart UV Project`. Si vous rencontrez des défis avec un objet particulier, la vidéo que j'ai partagée précédemment peut vous donner des conseils supplémentaires sur cet aspect.

Généralement, pour atténuer les problèmes, vous devez optimiser la disposition de votre objet lors de sa phase de création. Éviter l'introduction de bords excessifs à des emplacements spécifiques peut prévenir des problèmes comme le clipping, par exemple.

### Le processus de cuisson

Maintenant, retournons à l'onglet **Shading**, où nous accéderons aux `Render Properties` sur le côté droit (représenté par le petit symbole d'écran ou de télévision). Si ce n'est pas déjà sélectionné, choisissez `Cycles` comme votre `Render Engine`. Ensuite, naviguez vers la catégorie `Bake`, qui est située sous la catégorie `Performance`.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/blender9.0-1.PNG)
_Option `Bake` dans l'onglet **Shading** dans les `Render Properties`_

Avec les paramètres par défaut existants, vous pouvez procéder en cliquant sur le bouton `Bake` tout en vous assurant que le nœud `Image Texture` et la grande sphère sont sélectionnés. 

Gardez à l'esprit que j'ai intégré une lumière `Sun` dans ma scène, car ce processus de cuisson prend en compte l'éclairage de la scène. Sans un éclairage suffisant, le résultat pourrait apparaître excessivement sombre.

Après une période de traitement (qui pourrait être plus longue si vous avez utilisé des dimensions plus grandes pour l'image du nœud `Image Texture`), le processus de cuisson se terminera. Cela aboutit à l'application de la texture sur l'image du `Image Texture`. Au lieu d'obtenir la texture du nœud `Shader` nommé `Glossy BSDF`, nous avons maintenant accès à celle-ci via une image texture "normale" régulière.

Ensuite, nous pouvons établir une connexion du nœud `Image Texture` au nœud `Material Output`, implémentant ainsi avec succès notre matériau. À ce stade, il n'y a pas de différence significative par rapport à la méthode précédente où nous avions le nœud `Principled BSDF` connecté à l'entrée `Surface` du nœud `Material Output`.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/blender10.0.PNG)
_Nœud `Image Texture` avec la texture "cuite" est connecté au nœud `Material Output` au lieu du nœud `Glossy BSDF`_

### Comment voir le résultat final

Maintenant, nous pouvons exporter le fichier à nouveau, répéter le même processus que précédemment dans notre IDE avec **glTF Tools** et visualiser le fichier `.gltf` avec l'extension. En examinant le résultat, vous pourriez remarquer qu'il ne correspond pas exactement à la version que nous avions en utilisant le nœud `Glossy BSDF` dans Blender. Cette différence peut être principalement attribuée aux conditions d'éclairage dans la scène Blender.

Gardez à l'esprit que l'approche que j'ai décrite n'est pas l'utilisation typique pour le processus de cuisson, puisque dans ce cas, vous auriez également pu choisir une couleur de base similaire avec le nœud `Principled BSDF` et obtiendriez à peu près la même solution, par exemple.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/blender11.0.PNG)
_Vue finalisée avec **glTF Tools**, incluant la texture "cuite" pour la grande sphère_

J'ai introduit le processus de cuisson basé sur une expérience personnelle. Il y a eu des cas où j'ai rencontré une situation où les matériaux apparaissaient différemment dans Blender par rapport à leur implémentation dans une application React.js avec Three.js. Cette situation m'a incité à explorer le concept de cuisson, qui s'est avéré être une solution utile.

Pour résumer, si vous vous trouvez dans une situation où vos matériaux n'apparaissent pas comme prévu dans votre application React.js avec Three.js, envisager le processus de cuisson et rechercher ce sujet peut fournir des informations précieuses. Cela peut être particulièrement bénéfique pour les personnes qui sont nouvelles dans Blender.

## \u2712\ufe0f Comment implémenter le modèle Blender dans l'application React.js

Pour implémenter le fichier Blender, nous pouvons utiliser un raccourci vraiment utile (source : [https://github.com/pmndrs/gltfjsx](https://github.com/pmndrs/gltfjsx)) :

`npx gltfjsx public/blenderFileName.glb`

Il est important de noter que vous devez stocker votre fichier Blender dans le dossier `public` de votre application React.js pour cette étape. Il est également important de souligner que vous avez besoin de React Three Drei pour utiliser cet assistant. Donc dans notre cas, nous pouvons utiliser directement ce raccourci sans avoir besoin de préparations supplémentaires.

Après avoir exécuté ce raccourci, nous obtenons le fichier suivant :

```javascript
/*
Généré automatiquement par : https://github.com/pmndrs/gltfjsx
Commande : npx gltfjsx@6.1.4 public/blenderStuff/blenderFile.glb
*/

import { useLayoutEffect, useRef } from "react";
import { useGLTF, useAnimations } from "@react-three/drei";

export function Model(props) {
  const group = useRef();
  const { nodes, materials, animations } = useGLTF(
    "./blenderStuff/blenderFile.glb"
  );
  const { actions } = useAnimations(animations, group);

  return (
    <group ref={group} {...props} dispose={null}>
      <group name="Scene">
        <mesh
          name="Cube"
          geometry={nodes.Cube.geometry}
          material={materials.Material}
          position={[-0.07, 0.16, -0.27]}
          scale={[1, 0.03, 1]}
        />
        <mesh
          name="Sphere"
          geometry={nodes.Sphere.geometry}
          material={materials["Material.002"]}
          position={[-0.62, 0.43, -0.79]}
          rotation={[-0.01, 0.11, -0.02]}
          scale={0.09}
        />
        <mesh
          name="Sphere001"
          geometry={nodes.Sphere001.geometry}
          material={materials["Material.001"]}
          position={[0.4, 0.55, 0.15]}
          scale={0.41}
        />
      </group>
    </group>
  );
}

useGLTF.preload("./blenderStuff/blenderFile.glb");
```

À première vue, vous pouvez voir que ce processus a ajouté de nombreux éléments, donc nous n'avons pas besoin d'ajouter grand-chose de notre côté.

Un aspect important à configurer est le chemin dans le hook `useGLTF`. Dans mon cas, le chemin exact à incorporer est `./blenderStuff/blenderFile.glb` (cela s'applique également à `useGLTF.preload()`). Cela est dû au fait que j'ai créé un sous-dossier nommé `blenderStuff` dans mon répertoire `public`.

### Comment ajouter un wrapper Canvas et d'autres composants

Avec cette configuration en place, nous sommes maintenant prêts à utiliser le composant `Model`. Mais pour intégrer efficacement ce composant `Model` à l'emplacement souhaité, nous devons apporter quelques ajustements dans le composant parent. 

Dans mon cas, j'ai choisi de l'implémenter dans le fichier principal `App.js`. Et j'ai attribué une hauteur de `100vh` à la classe CSS de `App` pour garantir l'affichage souhaité.

```javascript
import "./App.css";
import { Model } from "./BlenderFile";
import { Canvas } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";

function App() {
  return (
    <div className="App">
      <Canvas camera={{ fov: 64, position: [-2, 2, 0] }}>
        <ambientLight intensity={5} />
        <OrbitControls enableZoom={true} />
        <Model />
      </Canvas>
    </div>
  );
}

export default App;
```

De manière générale, vous aurez besoin d'un composant pour encapsuler tous les éléments liés à Three.js. Dans le composant `Canvas`, il y a une opportunité de configurer divers paramètres. Dans mon cas spécifique, j'ajuste la position initiale de la caméra.

La lumière pour le composant joue un rôle crucial. Dans notre cas, nous avons utilisé `ambientLight` qui ajoutera une lumière à toute la scène. Sans un éclairage adéquat, votre scène pourrait apparaître excessivement sombre ou même entièrement noire malgré la présence de couleurs d'objets. Vous pouvez également utiliser des sources de lumière supplémentaires comme le composant `spotLight`.

Le composant `OrbitControls`, accessible depuis la bibliothèque d'assistance Drei, améliore votre interactivité en permettant le défilement et la rotation dans le modèle directement dans le navigateur. Cette seule ligne de code améliore considérablement les options d'interactivité de l'utilisateur.

Rappelez-vous que votre composant `Canvas` peut accueillir plusieurs modèles. Vous pouvez également appliquer sélectivement des composants comme `OrbitControls` à des modèles Blender spécifiques, adaptant ainsi leur comportement. 

Pour ce faire, vous devrez créer un composant parent pour chaque scène que vous souhaitez intégrer dans le `Canvas`. Dans chaque nouveau composant parent, incorporez votre composant de modèle Blender, ainsi que tous les composants d'assistance supplémentaires que vous souhaitez ajouter. 

Cette approche s'avère particulièrement avantageuse lorsque différents modèles nécessitent des éclairages différents ou des positions de caméra uniques, par exemple.

### Comment implémenter les animations

À ce stade, nous avons établi un environnement `Canvas` Three.js fonctionnel, présentant notre modèle Blender. Mais il est important de se rappeler que nous avons également introduit des animations de base, qui ne sont pas encore opérationnelles.

Pour résoudre ce problème, nous pouvons exploiter le hook `useAnimations` pré-implémenté.

```javascript
  const { actions, names } = useAnimations(animations, group);

  useLayoutEffect(() => {
    names.forEach((animation) => {
      actions?.[animation]?.play();
    });
  }, [actions, names]);
```

En incorporant cette implémentation, toutes les animations associées à ce modèle Blender commenceront à jouer lors du rendu de la page. Ce comportement inclut également une boucle indéfinie pour chaque animation.

## \ud83d\udcc4 Informations supplémentaires

Bien que ce tutoriel se soit principalement concentré sur l'intégration d'un modèle Blender dans une application React.js en utilisant Three.js, il existe un monde de potentiel inexploité dans Three.js que nous n'avons pas couvert.

Bien que nous ne l'ayons pas utilisé dans cet exemple de base, vous pouvez introduire le Post Processing à vos modèles Three.js dans React.js. La bibliothèque [React Three Postprocessing](https://www.npmjs.com/package/@react-three/postprocessing) sert d'outil précieux à cet égard. Elle vous permet d'élever vos scènes Three.js avec des effets sophistiqués comme les effets Bloom ou Noise, qui peuvent ajouter une dimension plus avancée à vos visualisations.

De plus, lorsque vous travaillez sur des projets futurs avec Three.js, envisagez d'explorer la bibliothèque [React Spring](https://docs.pmnd.rs/react-three-fiber/tutorials/using-with-react-spring) qui s'intègre bien avec React Three Fiber. React Spring offre l'opportunité d'incorporer des animations personnalisées dans vos scènes Three.js, en plus des animations directement intégrées dans Blender. 

Par exemple, vous pourriez faire en sorte qu'un objet spécifique dans votre scène devienne plus grand ou plus petit en cliquant dessus. Comme pour d'autres aspects de Three.js, cet aspect pourrait améliorer l'interactivité et pourrait valoir la peine de s'y investir.

Au fait, si vous trouvez que vos images s'exécutent à un taux plus bas, envisagez de basculer l'accélération matérielle dans les paramètres de votre navigateur pour potentiellement améliorer les performances.

## \ud83d\udccb Conclusion

À ce stade, nous avons réussi à créer un modèle Blender avec des animations et des matériaux. Ensuite, nous l'avons intégré dans notre application React.js en utilisant React Three Fiber.

Bien que l'exemple que nous avons examiné ici était assez basique, l'approche d'intégration reste la même pour des modèles Blender plus complexes. Les fonctions fondamentales de Three.js peuvent être combinées avec des aides supplémentaires pour améliorer vos scènes. 

En plus du Post Processing, des animations supplémentaires ou également des matériaux Blender spécifiques, des aspects comme les caméras et les lumières sont souvent les plus importants lorsque l'on vise à améliorer l'impact visuel de vos modèles Blender dans les scènes Three.js.