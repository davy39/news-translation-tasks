---
title: Se débarrasser de node_modules avec Yarn Plug’n’Play
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-09T17:05:39.000Z'
originalURL: https://freecodecamp.org/news/getting-rid-of-node-modules-with-yarn-plugn-play-a490e5e747d7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qYAlY8Iq5S4knk93upSneA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
- name: Yarn
  slug: yarn
seo_title: Se débarrasser de node_modules avec Yarn Plug’n’Play
seo_desc: 'By Alcides Queiroz

  Reduce your install time up to 70%. Ask me how! ?


  Anyone who knows me can confirm that I’m a long-standing lover of JavaScript and
  its entire ecosystem. As a Front-end engineer, Node-based package managers have
  been a crucial part...'
---

Par Alcides Queiroz

#### Réduisez votre temps d'installation jusqu'à 70 %. Demandez-moi comment ! 💡

![Image](https://cdn-media-1.freecodecamp.org/images/F7mSgfClDgWzo8rkmxdF1mkiBw46HP5qbTRN)

Quiconque me connaît peut confirmer que je suis un amoureux de longue date de JavaScript et de tout son *écosystème*. En tant qu'ingénieur Front-end, les gestionnaires de paquets basés sur Node ont été une partie cruciale de mon ensemble d'outils depuis 2013.

Tout d'abord, j'ai utilisé Bower, qui était principalement axé sur le monde du front-end. Ensuite, en 2015, j'ai réalisé avec tristesse (ok, *pas vraiment*) que Bower était en train de mourir et que NPM, le gestionnaire de paquets par défaut pour Node, était également la voie à suivre pour le front-end. Au début, c'était étrange pour moi d'utiliser NPM pour autre chose que les modules Node, mais je me suis habitué à l'idée et j'ai migré sans problème.

Enfin, seulement un an plus tard, Facebook nous a donné Yarn, une alternative moderne et ultra-rapide à NPM. Je l'ai aimé dès le premier regard ! **Mais certaines choses étaient encore problématiques…**

### Problèmes hérités dans Yarn

Outre la vitesse, Yarn a apporté un certain nombre d'avantages par rapport à la version NPM de l'époque, tels que les fichiers de verrouillage, le mode hors ligne, la résilience du réseau, les sommes de contrôle et autres. Néanmoins, Yarn a hérité de certains problèmes connus de NPM :

#### node_modules ici, là, partout

Pour chaque projet sur votre machine qui utilise NPM ou Yarn, un dossier `node_modules` est créé. Peu importe si 10 projets utilisent la même version exacte d'un module donné, il sera copié encore et encore dans chaque dossier `node_modules` de ces projets.

#### Générer un nouveau dossier node_modules prend vraiment beaucoup de temps

Même en faisant un grand pas en avant en termes de vitesse d'installation, Yarn était limité par les contraintes de node_modules. Juste la création du dossier node_modules prend jusqu'à 70 % du temps nécessaire pour exécuter `yarn install` (avec un cache chaud). **C'est un nombre énorme de fichiers à créer à chaque installation.** Alors, ne blâmez pas Yarn.

#### Dépendances non ajoutées à package.json

Voici un scénario pour vous : Votre application fonctionne parfaitement en développement, mais plante en production. Après des heures d'investigation, vous réalisez enfin que vous avez oublié d'ajouter une dépendance à votre `package.json`. **Oui, cela peut arriver.**

#### Résolution lente des modules à l'exécution

Le temps de démarrage de votre application est fortement impacté par la manière dont Node résout les dépendances. Il perd du temps à interroger le système de fichiers pour découvrir où une dépendance donnée sera résolue.

### Yarn Plug’n’Play à la rescousse !

Tous les problèmes mentionnés ci-dessus ont été abordés par l'équipe Yarn avec la sortie de la fonctionnalité Plug’n’Play en septembre dernier.

Lorsque vous activez PnP, au lieu de copier chaque fichier nécessaire du cache vers le dossier `node_modules`, voici ce que fait Yarn :

1. Il crée un seul fichier avec des tables de résolution statiques. Ces tables contiendront un ensemble d'informations importantes, telles que : les paquets disponibles dans l'arborescence des dépendances, leurs relations entre eux et leur emplacement sur le disque.
2. Un résolveur spécial est utilisé afin d'aider Node à découvrir où chaque dépendance a été installée (sous le dossier de cache de Yarn). Il repose uniquement sur les tables de résolution qui ont été créées précédemment. Comme ces tables contiennent des informations sur l'ensemble de l'arborescence des dépendances, le processus de résolution de node_modules n'aura plus besoin de faire beaucoup d'appels `stat` et `readdir` à l'exécution, réduisant ainsi considérablement le temps de démarrage de votre application. Et comme Yarn connaît toutes vos dépendances, il se plaindra si vous essayez d'importer un module qui n'est pas présent dans votre `package.json` :

![Image](https://cdn-media-1.freecodecamp.org/images/08nON5DmVDa9ITAs2nhTlNoRqNug1C-pC1Zs)

### Utilisation de Yarn Plug’n’Play

Convertir un projet pour utiliser PnP est aussi simple que 1-2-3. Vous devez simplement ajouter une section `installConfig` à votre `package.json`, avec une clé `pnp` définie sur `true`, comme ceci :

```
{    "installConfig": {     "pnp": true   }}
```

> **Note :** Vous avez besoin de Yarn v1.12+ pour utiliser Plug’n’Play.

Après cela, exécutez simplement `yarn install` et tout ce qui se trouve dans votre dossier `node_modules` sera supprimé. Désormais, chaque dépendance sera résolue directement à partir du cache chaud de Yarn.

![Image](https://cdn-media-1.freecodecamp.org/images/PD4zmILDWgikOs6RcNxXQnmtKE8YPiu9oFwN)
_« yarn install » efface votre dossier node_modules lorsque PnP est activé_

#### Utilisation de PnP dans un nouveau projet React avec create-react-app

Si vous utilisez create-react-app 2+, la bonne nouvelle est qu'il fonctionne très bien avec Yarn Plug’n’Play ! Il suffit d'ajouter l'option `--use-pnp` à la commande `create-react-app` et vous êtes prêt à partir :

```
npx create-react-app votre-nom-d-app --use-pnp
```

![Image](https://cdn-media-1.freecodecamp.org/images/Q1KEkqQk4isuWAQUSB-kXGTIdOwZRW9oW7Qw)

#### Problèmes possibles

Comme rien n'est parfait dans le monde, PnP peut entraîner de nouveaux problèmes lorsqu'il est utilisé dans des projets reposant sur une logique d'installation personnalisée. Si vous avez besoin de plus d'informations sur ces nouveaux problèmes potentiels, [vous pouvez trouver une explication détaillée dans ce document](https://github.com/yarnpkg/rfcs/files/2378943/Plugnplay.pdf).

### Conclusion

Plug’n’Play résout certains problèmes vraiment ennuyeux dans Yarn. De plus, il améliore considérablement la mise en cache des dépendances sur les CIs, économisant du temps d'installation et permettant à nos builds d'aller droit au but : **exécuter les tests !**

Et c'est tout ! Amusez-vous bien avec Yarn PnP.