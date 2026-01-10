---
title: 'Frappez sur une (virtuelle) boîte : Une introduction à l''audio dans A-Frame'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-07T18:34:19.000Z'
originalURL: https://freecodecamp.org/news/a-primer-on-a-frame-audio-52dd56e54876
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XnHzLrB2S17DUeetCPElXg.png
tags:
- name: A-Frame
  slug: a-frame
- name: AR
  slug: ar
- name: audio
  slug: audio
- name: 'tech '
  slug: tech
- name: vr
  slug: vr
seo_title: 'Frappez sur une (virtuelle) boîte : Une introduction à l''audio dans A-Frame'
seo_desc: 'By Berrak Nil

  A-Frame is a web framework for building virtual reality experiences. Ever since
  its introduction in late 2015, it quickly became a favorite among artists and creators
  of all backgrounds who want to experiment with WebXR.

  I am a creative...'
---

Par Berrak Nil

[A-Frame](https://aframe.io/) est un framework web pour créer des expériences de réalité virtuelle. Depuis son introduction fin 2015, il est rapidement devenu un favori parmi les artistes et créateurs de tous horizons qui souhaitent expérimenter avec [WebXR](https://github.com/immersive-web/webxr/blob/master/explainer.md).

Je suis une développeuse créative avec un background en audio. Plonger dans les possibilités sonores de cette nouvelle plateforme a été un voyage très excitant et enrichissant. La plupart de mon expérience avec A-Frame s'est limitée aux environnements standard de bureau et de smartphone, et non à la VR. Je partage mes découvertes. Je veux créer une sorte de manuel non officiel sur la façon d'implémenter, d'utiliser et de créer de l'audio dans A-Frame. Dans cette première partie, nous allons examiner comment utiliser les capacités audio prêtes à l'emploi d'A-Frame.

**Prérequis**

Cet article suppose que vous avez une certaine expérience avec A-Frame. Vous n'avez pas besoin d'être un expert, mais connaître les bases rendra le suivi de ce tutoriel plus facile. Si vous n'avez pas encore eu l'occasion de le découvrir, vous pouvez commencer [ici](https://aframe.io/docs/0.8.0/introduction/).

### Composant Son d'A-Frame

A-Frame est un framework basé sur [Three.js](https://threejs.org/). Le composant son qu'il fournit est un [wrapper](https://github.com/aframevr/aframe/blob/v0.8.0/src/components/sound.js) autour du composant [audio positionnel](https://threejs.org/docs/#api/en/audio/PositionalAudio) de Three.js (ou non positionnel selon ce que nous choisissons, mais nous y reviendrons plus tard), qui utilise l'[API Web Audio](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API).

Cela signifie que nous obtenons des fonctionnalités comme l'audio positionnel, le contrôle du volume et la lecture audio dès que nous utilisons un composant son A-Frame.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZDC3HgFpM-xU_3cfgP2vTQ.png)
_Propriétés du composant son A-Frame, capture d'écran prise depuis [A-Frame Docs](https://aframe.io/docs/0.8.0/components/sound.html" rel="noopener" target="_blank" title=")_

Mais comment ajouter ce composant à nos scènes et fournir un retour audio aux interactions utilisateur et/ou créer un [paysage sonore](https://en.wikipedia.org/wiki/Soundscape) ?

Pour démontrer cela, j'ai créé un projet A-Frame à partir de zéro. Il est basé sur les interactions utilisateur avec un ordinateur de bureau (c'est-à-dire à utiliser avec une souris et un clavier). Les principes devraient s'appliquer à d'autres types de contrôles pour la plupart.

Vous avez la possibilité de commencer avec une copie fraîche du projet [[Glitch](https://glitch.com/~a-frame-audio-tutorial-starter)][[GitHub](https://github.com/berraknil/a-frame-audio-tutorial/tree/starter)] — sans sons attachés — et de suivre en implémentant les sons fournis vous-même. Ou vous pouvez consulter la version finale [[Glitch](https://glitch.com/~a-frame-audio-tutorial-complete)][[GitHub](https://github.com/berraknil/a-frame-audio-tutorial/tree/master)] et suivre en lisant le code.

### La Cuisine

![Image](https://cdn-media-1.freecodecamp.org/images/1*XnHzLrB2S17DUeetCPElXg.png)

Avant de commencer le processus d'implémentation audio, examinons notre scène. Nous avons plusieurs modèles 3D ici (courtoisie de [Google Poly](https://poly.google.com/)). Notre [cuisine](https://poly.google.com/view/38PMRiku8qj) est un modèle complet en soi. Des éléments comme la [machine à espresso](https://poly.google.com/view/6kN4sv3u9RM), la [radio](https://poly.google.com/view/9H9k1nAXSuH), la [poêle à frire](https://poly.google.com/view/bYF5rVRy_kp) et [l'œuf](https://poly.google.com/view/dccGDIUzA2y) dessus sont des modèles séparés ajoutés à la scène par-dessus la cuisine.

Maintenant, voyons les méthodes que nous pouvons utiliser pour ajouter des sons à cette scène.

### **Sons d'Interaction Utilisateur**

Les sons d'interaction utilisateur sont généralement des sons ponctuels. Cela signifie qu'ils sont de courts échantillons qui se jouent une fois lorsqu'ils sont déclenchés. Ils ne sont pas continus ou en boucle comme l'audio d'environnement ou la musique. Ce qui signifie que nous devons trouver un moyen de placer un fichier audio dans notre scène, puis de le déclencher lorsque notre utilisateur interagit avec cet objet (par exemple, clique sur le bouton de la souris, survole, etc.).

Pour déclencher un son lors d'une interaction utilisateur, nous pouvons :

1. Placer un son sur un modèle
2. Placer un son sur une [primitive](https://aframe.io/docs/0.8.0/introduction/html-and-primitives.html), comme une géométrie de boîte
3. Placer une primitive sur un composant <a-sound>

Passons donc en revue nos options une par une et voyons les cas d'utilisation pour chacune.

#### Placer un Son sur un Modèle

![Image](https://cdn-media-1.freecodecamp.org/images/1*dBWexbENGrlzW7Dj4jvS0Q.png)

Qui ne veut pas commencer la journée avec une tasse fraîche d'espresso ? (Si ce n'est pas votre cas, n'hésitez pas à prendre un modèle de thé [d'ici](https://poly.google.com/search/tea) et à l'utiliser à la place.)

Je dirais que la moitié de la satisfaction d'avoir ce boost de caféine est le son que fait notre machine à espresso bien-aimée. Pour nous assurer que notre scène fournit ce retour sonore, nous implémentons un son qui répondra à l'interaction utilisateur.

Commençons par examiner comment fonctionne notre machine à espresso sous le capot.

Nous commençons par charger notre modèle avec le chargeur A-Frame. Ensuite, nous définissons la position, la rotation et l'échelle du modèle dans la scène, en utilisant les propriétés nommées.

Notre modèle est référencé par l'id « #coffeeMaker », au lieu du chemin relatif du fichier. Tous les modèles de ce projet sont enregistrés dans le [Système de Gestion des Actifs](https://aframe.io/docs/0.8.0/core/asset-management-system.html) au préalable.

La manière la plus simple d'ajouter un son à notre machine à espresso est d'ajouter le composant son en l'utilisant comme attribut HTML sur l'objet.

Nous référençons notre son en utilisant à nouveau le système de gestion des actifs, et nous définissons son volume à 1. Cela signifie qu'il sera entendu à 100 %. Maintenant, pour la partie la plus importante, nous définissons la propriété « on » du son à la valeur « click ». Cela signifie que lorsque l'utilisateur clique sur cet objet, le son sera déclenché.

Nous n'utilisons pas les propriétés autoplay ou loop ici, car il s'agit d'un son ponctuel qui dépend de l'interaction utilisateur. Nous laissons la propriété positionnelle à « on » par défaut. Sinon, nous entendrions le son au même niveau de volume en tout temps, peu importe notre distance par rapport à l'objet. Le son n'aurait aucun panoramique et se jouerait toujours exactement là où nous sommes, au lieu de se jouer à gauche, à droite ou derrière nous en fonction de notre position relative à l'objet.

**NOTE : Les sons positionnels comme ceux-ci doivent être rendus en mono pour faciliter la cognition spatiale du son, tandis que la musique de fond ou les ambiances audio non positionnelles doivent de préférence être rendues en stéréo.**

#### Temps de Casser quelques Œufs

Maintenant, c'est à votre tour, allez-y et implémentez le son fourni de l'œuf qui frite sur le modèle d'œuf, qui est placé sur le dessus de la poêle à frire. Pour un défi, vous pouvez également essayer d'utiliser quelques [propriétés sonores](https://aframe.io/docs/0.8.0/components/sound.html#properties) supplémentaires de votre choix. Promenez-vous dans la scène après avoir placé le son de l'œuf et testez votre implémentation pour voir si cela sonne réaliste (ou irréaliste si c'est ce que vous recherchez !)

L'avez-vous fait ?

Super !

Votre code pour le modèle d'œuf devrait maintenant ressembler approximativement à ceci (avec vos propriétés et valeurs souhaitées)

#### Placer un Son sur une Géométrie

Nous pouvons donc ajouter nos sons aux modèles en les ajoutant simplement comme un attribut HTML. Mais que faire si nous voulons mettre un son sur un objet qui fait déjà partie d'un modèle plus grand et qui n'est pas une entité séparée en soi ?

Disons que nous voulons ajouter un son à la bouteille rouge à droite, qui devrait donner l'impression que nous la ramassons lorsque nous cliquons dessus.

Si nous mettons le son sur le modèle de cuisine comme nous l'avons fait avec les modèles plus petits, cela signifierait que le son se déclencherait peu importe où nous cliquons sur le modèle lui-même, au lieu de seulement sur la bouteille comme nous le voulons.

Nous pouvons résoudre ce problème en utilisant une géométrie sur laquelle nous pouvons cliquer, en l'alignant là où se trouve la bouteille, et en ajoutant la propriété son à celle-ci.

#### L'Inspecteur A-Frame à la Rescue

Pour les prochaines étapes, je vous recommande vivement de commencer à créer et à positionner des objets à l'intérieur de votre scène directement dans le navigateur en utilisant l'[Inspecteur A-Frame](https://aframe.io/docs/0.8.0/introduction/visual-inspector-and-dev-tools.html). Vous pouvez ensuite copier et utiliser ce code au lieu de deviner où votre objet doit être positionné.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nlhq4AvrGji6G1uNNGI9Ag.gif)
_Ouvrez l'Inspecteur A-Frame en utilisant le raccourci `&lt;ctrl&gt; + &lt;alt&gt; +` i._

Commençons par créer une primitive de géométrie dans notre scène, un cylindre devrait bien fonctionner étant donné la forme de notre bouteille.

Maintenant, redimensionnez et positionnez ce cylindre en utilisant l'inspecteur A-Frame. Il peut couvrir notre bouteille et répondre à l'interaction utilisateur au bon endroit.

**NOTE : Si vous ajoutez cette géométrie à l'intérieur du modèle, cela vous permettra de déplacer ou de faire tourner le modèle parent et de préserver la position correcte de tout ce qui se trouve à l'intérieur.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*AP6J0D-ZQelnlc9alwD1lA.gif)
_Redimensionnez et positionnez le cylindre à l'intérieur de la scène en utilisant les contrôles en haut à droite_

Vous pouvez coller le code que vous avez copié depuis l'inspecteur et simplement déplacer les valeurs d'échelle, de position et de rotation à l'intérieur du <a-cylinder>.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NZ8RVt_7L_gBtpz3S-ofig.png)
_Copiez l'entité et ses propriétés en utilisant le bouton en haut à droite_

Assurez-vous de réduire l'opacité du matériau à 0, afin que notre bouteille puisse rester visible à l'intérieur de la géométrie du cylindre. En tant qu'étape finale, ajoutez le son de bouteille fourni à l'objet, comme vous l'avez fait précédemment avec la machine à espresso et l'œuf.

Maintenant, votre code de cylindre devrait ressembler à ceci...

...et répondre correctement à l'interaction utilisateur.

#### Utilisation d'un composant <a-sound>

[<a-sound>](https://aframe.io/docs/0.8.0/primitives/a-sound.html) est un wrapper primitif autour du composant son A-Frame et nous permet d'utiliser l'audio sans l'attacher à autre chose dans la scène. Cependant, si nous voulons déclencher ce son lors d'une interaction, nous avons toujours besoin d'un type de géométrie qui nous permettra d'interagir avec cet objet.

Nous pouvons placer cette géométrie n'importe où ailleurs dans la scène (pensez à un bouton de menu d'interface utilisateur qui déclenchera un son non positionnel). Ou nous pouvons la placer directement sur <a-sound> et la positionner sur l'objet dont nous voulons entendre le retour audio.

Ce qui signifie que pour ajouter un son à notre grille-pain, nous pouvons faire l'inverse de ce que nous venons de faire et créer un composant <a-sound> et y attacher une géométrie cliquable.

### Audio d'Environnement

Nous avons vu quelques-unes des façons dont nous pouvons implémenter des sons qui répondent aux interactions utilisateur. Mais qu'en est-il des sons qui ne nécessitent pas que l'utilisateur fasse quoi que ce soit pour se jouer ? Ce sont des sons qui traversent la scène du début à la fin, pour créer une atmosphère, une ambiance, un sentiment de lieu ?

Si nous regardons notre cuisine, nous pouvons voir qu'il y a un grand réfrigérateur à gauche, qui est complètement silencieux pour le moment. Sans parler du fait que, que nous en soyons conscients ou non, presque tous les environnements que nous occupons (sauf s'ils sont une [chambre anéchoïque](https://en.wikipedia.org/wiki/Anechoic_chamber)) ont ce qu'on appelle une [présence ou un ton de pièce](https://en.wikipedia.org/wiki/Presence_(sound_recording)).

Les bourdonnements électriques, les machines, les unités de climatisation et autres créent le ton de la pièce avec ou sans que nous ajoutions par-dessus acoustiquement. Donc, pour refléter cela, notre choix devrait être un son continu. Dans ce cas, un son en boucle qui est présent dans toute notre scène.

**NOTE : Le format .mp3, par sa nature, [ne boucle pas de manière transparente](https://sound.stackexchange.com/questions/25846/is-it-possible-to-loop-mp3-without-gaps) sur la plupart des plateformes, il y a toujours un très court intervalle entre les boucles qui rompt la continuité audio, et donc pour les sons en boucle, d'autres formats comme .wav ou .ogg doivent être utilisés.**

#### Ajout du Ton de Pièce

Maintenant, ajoutons le ton de pièce fourni à notre scène. Nous avons plusieurs options selon le type de projet A-Frame sur lequel nous travaillons. Si nous n'avons qu'une seule pièce — comme c'est le cas ici — nous pouvons mettre notre ton de pièce directement dans notre <a-scene>. Ou si nous avons plusieurs pièces dans notre scène avec différentes caractéristiques, nous pouvons mettre le ton de pièce dans une géométrie de plan qui pourrait agir comme le sol. Ou dans un objet <a-sound> que nous pouvons placer au centre de la pièce. Dans tous les cas, nous devons nous assurer que notre ton de pièce n'est pas positionnel, contrairement à tous les autres sons que nous avons utilisés précédemment dans ce projet.

Étant donné que nous ne travaillons qu'avec une seule pièce/environnement ici, nous pouvons mettre notre ton de pièce directement dans la scène elle-même. Nous définissons la propriété positionnelle à false, pour nous assurer que le son est entendu de manière égale dans toute la pièce.

Nous définissons également la propriété autoplay à true puisque nous n'avons pas besoin d'interaction utilisateur pour entendre le ton de la pièce.

**NOTE : L'auto-lecture audio dans la plupart des navigateurs nécessite déjà ou nécessitera une interaction utilisateur pour démarrer. Ce qui signifie que pour lire automatiquement des sons comme de la musique de fond ou de l'audio ambiant, vous devez utiliser un écran de menu ou un bouton mute/unmute ou quelque chose de similaire pour activer l'auto-lecture audio.**

### Musique

Pour la dernière pièce de notre puzzle audio, ajoutons de la musique à notre scène. Nous pouvons choisir de l'ajouter soit comme musique diégétique provenant de la radio dans notre scène, soit comme musique extra-diégétique qui n'existe pas dans le monde virtuel que nous avons créé, mais spécifiquement pour l'utilisateur/specteur/joueur qui vit et contrôle ce monde virtuel.

Pour faire cela, nous devrions placer notre musique soit sur notre caméra (<a-camera>) soit sur notre personnage à la première personne (si c'est une option) et nous assurer que l'audio n'est pas positionnel. Dans cette scène, j'ai choisi de faire le premier et de mettre la musique sur le modèle de radio comme une source à l'intérieur du monde virtuel.

Nous pouvons ajouter la piste musicale fournie (composée par moi-même) à notre modèle de radio, tout comme nous avons ajouté tous les sons jusqu'à présent.

#### Contrôle de la Lecture

Notre musique se joue chaque fois que nous cliquons sur la radio, mais que faire si nous voulons la mettre en pause puis la relancer ?

Pour avoir cette fonctionnalité, nous devons [écrire un composant A-Frame personnalisé](https://aframe.io/docs/0.8.0/introduction/writing-a-component.html). Ensuite, ajouter ce composant comme un attribut HTML à tout objet auquel nous voulons ajouter cette fonctionnalité, tout comme nous avons ajouté le composant « sound » à nos modèles auparavant.

Vous pouvez soit écrire vos composants A-Frame en ligne, soit les écrire dans un fichier JavaScript externe et ensuite les lier depuis le HTML, comme je l'ai fait pour ce projet.

Maintenant, nous avons un composant audio-toggle qui nous permet de jouer et de mettre en pause le son que nous entendons. Il nous permet également de changer la capacité d'auto-lecture via la propriété « playing ».

Et c'est tout ! [Nous avons une scène A-Frame avec de la musique, des sons d'environnement et de l'audio interactif.](https://a-frame-audio-tutorial-complete.glitch.me/)

Dans la prochaine partie, nous examinerons comment intégrer [Tone.js](https://tonejs.github.io/) à un projet A-Frame et écrire plus de composants personnalisés avec des fonctionnalités audio avancées.

Merci d'avoir lu !