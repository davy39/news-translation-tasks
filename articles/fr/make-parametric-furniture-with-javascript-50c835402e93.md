---
title: Comment créer des meubles paramétriques avec JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-02T22:30:16.000Z'
originalURL: https://freecodecamp.org/news/make-parametric-furniture-with-javascript-50c835402e93
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JQqo3bzhfEBTxs8bvu1qrw.png
tags:
- name: Design
  slug: design
- name: GitHub
  slug: github
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment créer des meubles paramétriques avec JavaScript
seo_desc: 'By O-LAP

  This guide will help you create a piece of parametric furniture. Check out one of
  the designs from our gallery to find one you like. You can read more about the project
  here.

  This tutorial assumes that you have an understanding of Javascript...'
---

Par O-LAP

Ce guide vous aidera à créer un meuble paramétrique. [Consultez](https://o-lap.org/app.html?a=amitlzkpa&r=o-lap_plato) l'un des designs de notre galerie pour en trouver un qui vous plaît. Vous pouvez en savoir plus sur le projet [ici](https://o-lap.github.io/home).

Ce tutoriel suppose que vous avez une compréhension de JavaScript, Git (bases) et [ThreeJS](https://threejs.org/). (Il suffit d'avoir travaillé avec eux une fois).

Commençons.

### Installation

Obtenez le projet de démarrage en clonant `[https://github.com/O-LAP/starter_project.git](https://github.com/O-LAP/starter_project.git.)`. Le `starter_project` contient des fichiers en place pour vous permettre d'exécuter et de tester votre design dans un environnement de développement. Une fois que vous le poussez et l'enregistrez avec l'application principale, il fonctionne également sans problème avec le framework.

Le projet de démarrage est configuré pour montrer un simple cube qui peut être contrôlé en utilisant des paramètres dans le navigateur. Cet exercice remplacera ce cube par notre propre design.

Vous pouvez ouvrir le fichier `dev.html` dans un navigateur pour voir à quoi il ressemble actuellement.

Vous pouvez changer les curseurs sur le côté droit qui modifient les proportions du cube. Vous verrez un groupe de contrôles sous « Environment » en bas à droite. Essayez d'activer l'interrupteur « Show Section ». Il montre des sections du cube qui peuvent être fabriquées.

Nous pouvons utiliser ces sections pour fabriquer le cube avec du bois réel.

Lorsque vous cliquez sur le bouton « Download », il vous donnera un fichier CAO (.obj) que vous pouvez alimenter dans une machine CNC pour le fabriquer. Vous pouvez en savoir plus sur ce processus [ici](https://github.com/O-LAP/home/blob/master/faq.md).

Voici un exemple de chaise fabriquée en utilisant cette technique :

![Image](https://cdn-media-1.freecodecamp.org/images/nJCOzTVUgJAGHMHzJ6DUIOChhKf7iDIlQlbb)

### Parcours du code

Commençons par faire un cylindre paramétrique (que vous pouvez imaginer comme un petit tabouret) pour remplacer le cube. Le dossier `designs` contient tous les fichiers dont vous avez besoin pour le design.

Le fichier `Design.js` contient un exemple de code montrant un cube qui peut être modifié de manière paramétrique.

Le fichier `dev.html` est le harnais de développement qui émule l'application web OLAP. (Ce fichier devra être copié manuellement lors des mises à jour.)

Le framework nécessite que la logique de design soit capturée dans un objet JavaScript appelé `Design` dans le fichier `Design.js`.

```
Design.info = { ... };Design.inputs = { ... };Design.inputState = { ... };Design.init = async function() { ... };Design.updateGeom = async function(group, sliceManager) { ... };
```

`Design.inputs` est l'endroit où vous spécifiez les paramètres pour votre design. Il est configuré pour le cube. Modifions-le pour le rendre adapté à notre sphère.

Nous allons garder les choses très simples et n'utiliser que `height` et `width` pour notre cylindre.

Mettez à jour `Design.inputs` pour qu'il ressemble à ceci.

```
Design.inputs = {    "width": {         "type": "slider",        "label": "Largeur",        "default": 150,        "min": 100,        "max": 200    },    "height": {         "type": "slider",                               "label": "Hauteur",        "default": 150,        "min": 100,        "max": 200    }}
```

Maintenant, si vous ouvrez `dev.html`, cela devrait ressembler à quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/7OS0MXJTSb49EcVOxvOXv1QzPZv1gSCR6q04)

### Ajout de géométrie

Maintenant, nous allons créer un cylindre au lieu d'un cube.

Le design est mis à jour chaque fois qu'une valeur de paramètre est modifiée et au chargement initial. Il passe un `THREE.Object3D` vide qui est le conteneur pour vous permettre d'ajouter des géométries et un `SliceManager` que vous pouvez utiliser pour spécifier comment faire les 'slices' pour le design. Les références de l'appel de mise à jour précédent sont abandonnées et de nouvelles instances pour chaque appel sont utilisées.

```
Design.updateGeom = async function(group, sliceManager) { ... };
```

Examinons à quoi ressemble la méthode `updateGeometry` pour le cube.

```
Design.updateGeom = async function(group, sliceManager) {  var geometry = new THREE.BoxGeometry( 200, Design.inputState.height, Design.inputState.width * ((Design.inputState.doubleWidth) ? 2 : 1) );  var material = getMaterial(Design.inputState.colour, Design.inputState.finish);  var cube = new THREE.Mesh( geometry, material );  sliceManager.addSliceSet({uDir: true, start: -80, end: 80, cuts: 3});  sliceManager.addSliceSet({uDir: false, start: -90, end: 90, cuts: 4});  group.add( cube );}
```

Vous pouvez utiliser `Design.inputState` pour accéder à l'ensemble de valeurs actuel défini par l'utilisateur pour les paramètres à tout moment.

Par exemple, pour accéder à la valeur du paramètre `height`, vous pouvez utiliser `Design.inputState.height`.

Les quatre premières lignes sont du code pur [threeJS](https://threejs.org/), où il crée une simple `BoxGeometry` basée sur les valeurs des paramètres. C'est la partie principale de votre design que vous modifierez dans l'étape suivante pour créer un design utilisant les valeurs des paramètres. La partie après cela avec les `sliceManager`s gère la façon dont les profils de section sont créés pour votre design. Plus d'informations sur le découpage ci-dessous.

Nous allons modifier cette méthode pour qu'elle ressemble à ceci :

```
Design.updateGeom = function(group, sliceManager) {  var geometry = new THREE.CylinderGeometry( Design.inputState.width -100, Design.inputState.width, Design.inputState.height, 32 );  var material = new THREE.MeshStandardMaterial( {color: 0x00BFFF } );  var cylinder = new THREE.Mesh( geometry, material );  sliceManager.addSliceSet({uDir: true, start: -80, end: 80, cuts: 3});  sliceManager.addSliceSet({uDir: false, start: -90, end: 90, cuts: 4});  group.add( cylinder );}
```

Nous remplaçons les 3 lignes qui créaient le cube par 3 lignes qui créent un cylindre. Nous utilisons la largeur et la hauteur des paramètres de design et une couleur fixe.

Nous conservons les mêmes paramètres de découpage qu'auparavant et mettons à jour la dernière ligne pour ajouter le cylindre au lieu du cube.

Enregistrez et essayez d'actualiser la page pour voir le changement. Vous devriez voir quelque chose comme ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/vaCx8l3sFofcRehFCfE4UxHBvm-j43PkZ7sh)

Essayez de jouer avec les paramètres et vérifiez comment les sections apparaissent pour ce design. Vous pouvez travailler avec n'importe quel maillage threeJS pour définir la géométrie de votre design.

Toute géométrie passée dans le `group` est "découpée" par la configuration de découpage selon les paramètres fournis.

Ce rapide aperçu a démontré comment vous pouvez construire des géométries de base de manière paramétrique. Vous pouvez adapter cette logique pour créer tout type de géométrie paramétrique qui peut être fabriquée en meubles.

Consultez [cet](https://medium.com/@olapdesign/design-for-a-rocking-chair-8a1a1e109d7f) article pour comprendre l'utilisation des techniques computationnelles pour la conception de meubles.

### Soumettre votre design

Une fois que vous avez un design qui vous satisfait, vous pouvez passer à la soumission de votre design si vous le souhaitez.

Pour ce guide de démarrage rapide, nous allons soumettre notre design à une galerie de test que nous maintenons. Tous les designs enregistrés dans la galerie de test sont périodiquement effacés.

Les designs seront acceptés dans le dépôt principal/test via des pull requests. Cela permettra une discussion significative dans le processus d'ajout/publication.

Allez à :

`[https://github.com/O-LAP/home/edit/master/data/TEST_DesignCollection.js](https://github.com/O-LAP/home/edit/master/data/TEST_DesignCollection.js.)`[.](https://github.com/O-LAP/home/edit/master/data/TEST_DesignCollection.js.)

Si c'est la première fois que vous ajoutez un design, vous serez invité à fork le dépôt. Faites-le.

Ajoutez le lien vers votre dépôt (par exemple `https://github.com/amitlzkpa/o-lap_plato`) à la liste à l'intérieur de `TEST_DesignCollection`. Assurez-vous de vérifier que vous avez les virgules au bon endroit.

Faites une seule modification à la fois. Toute proposition avec plus d'une modification sera rejetée, même si tout le reste est en place. Cliquez pour proposer le changement. Il sera modéré par l'un des mainteneurs, et si une discussion supplémentaire est nécessaire, elle aura lieu sur cette page.

Si votre design est accepté... hourra ! Nous avons un Michel-Ange en devenir ! Vous pouvez vérifier votre design en allant sur le lien : `http://o-lap.org/test.html?a=<github-user-name>&r=<olap-repo-name>`

_La plupart des soumissions au dépôt de test seront acceptées._ En tant que communauté, nous espérons que le même processus sera utilisé pour modérer les designs qui ne répondent pas aux exigences.

Lien de soumission (Principal) : `https://github.com/O-LAP/home/edit/master/data/OLAP_DesignCollection.js`
Lien de soumission (Test) : `https://github.com/O-LAP/home/edit/master/data/TEST_DesignCollection.js`
Galerie de designs (Principal) : `https://O-LAP.github.io/home/designs.html`
Galerie de designs (Test) : `https://O-LAP.github.io/home/test.html`
App : `http://o-lap.org/app.html?a=<github-user-name>&r=<olap-repo-name>&m=test`

### Comment publier une mise à jour pour votre design

Pour apporter des mises à jour au fichier de design, vous n'avez pas à mettre à jour votre fichier en même temps. En fait, il est préférable d'apporter vos modifications en petites étapes sous forme de commits séparés. Avec chaque commit, incluez une description significative de ce que vous avez modifié, ainsi que comment et pourquoi vous avez apporté les modifications.

Mettez à jour le fichier `Design.js` pour apporter uniquement la modification de mise à jour de version.

**Modifiez le numéro de version à `"version": "x.y.z"`, (ligne 11) à l'intérieur de `Design.js`**
_x.y.z (x : changements majeurs ; y : changements mineurs ; z : ajustements) (plus de détails)[[https://semver.org/](https://semver.org/)]_

### Comment fork un autre design

Ouvrez bash/terminal/invite de commande dans un dossier. Exécutez `git clone <repo que vous voulez fork>`. `Ouvrez Design.js` et apportez vos modifications.

_Vous voudrez peut-être renommer le dossier comme vous voulez nommer votre design_.

Après avoir terminé vos modifications, réinitialisez la version du design à `1.0.0` en modifiant `"version": "x.y.z"`, (ligne 11) à l'intérieur de `Design.js`. Mettez à jour d'autres informations comme `name, short_desc, long_desc, message` etc.

_Commencez à considérer ce design comme un nouveau design à partir de maintenant_.

Si vous voulez continuer à tirer les changements du dépôt parent, suivez cette [page](https://gist.github.com/CristinaSolana/1885435). Soumettez votre design forké comme un nouveau design en suivant le processus `Soumettre votre design`.

Vous êtes prêt !

### Un peu plus en profondeur

Jusqu'à présent, nous avons rapidement parcouru quelques choses. Maintenant que vous avez une meilleure compréhension, nous allons regarder un peu plus en profondeur.

#### Informations sur le design

En haut, vous verrez les méta-informations du design qui ressemblent à ceci :

```
Design.info = {  "name": "Boxy",  "designer": "Roxy",  "version": "1.0.0",  "license": "MIT",  "short_desc": "Fichier de design de modèle démontrant la configuration du projet.",  "long_desc": "",  "url": null,  "message": "Contrôlez les paramètres du cube en utilisant ces contrôles.",  "tags": [ "", "" ]}
```

Cela est utilisé pour afficher des informations sur le design dans la galerie.

![Image](https://cdn-media-1.freecodecamp.org/images/cPpDrNJKdE1woXLlRpzOpqbPEhvs2shLt21v)

#### Types d'entrée

Pour vous donner le contrôle sur vos paramètres d'entrée, vous pouvez spécifier différents types d'entrée.

```
Design.inputs = { ... };
```

Il existe 4 types de paramètres que vous pouvez fournir — `slider`, `bool`, `select` et `text`.
`slider` est utilisé pour permettre à l'utilisateur de choisir une valeur numérique dans une plage continue. Les valeurs sont en entiers.
`bool` permet à l'utilisateur de choisir une valeur oui/non.
`select` permet à l'utilisateur de sélectionner une valeur dans une liste de valeurs.
`text` prend une entrée pour les valeurs de texte.
Pour ajouter un paramètre à votre design, vous devez l'enregistrer en ajoutant une paire clé-valeur à `Design.input`.

#### Découpage

Le découpage est le processus d'extraction de sections droites de votre design que nous pouvons utiliser pour fabriquer le design.

Lisez la [FAQ](https://github.com/O-LAP/home/blob/master/faq.md) pour comprendre le processus.

Utilisez le `sliceManager` pour communiquer au framework comment vous voulez que le design soit découpé.

Nous faisons cela en passant un objet `config` au SliceManager. Si nous voulons créer des tranches le long de l'axe X à -80 et aller jusqu'à +80 avec 3 tranches également réparties dans cette plage (toutes les distances sont en millimètres), nous passons un objet qui ressemble à ceci :

`{uDir: true, start: -80, end: 80, cuts: 3}`

Pour créer un autre ensemble de tranches le long de l'axe Y qui commencent à -90 et vont jusqu'à +90 avec 4 coupes, nous passons un objet comme ceci :

`{uDir: true, start: -90, end: 90, cuts: 4}`

_Assurez-vous de spécifier la configuration de découpage juste avant d'ajouter la géométrie._ Généralement, avec deux ensembles de tranches dans des directions opposées, vous devriez avoir des designs qui peuvent être fabriqués. Mais vous devez être prudent quant à la manière dont vous pensez à cela dans votre design.

Lisez les [directives de conception](https://github.com/O-LAP/home/blob/master/guidelines.md) pour mieux comprendre cela.

### Prochaines étapes

Ce guide vous a accompagné à travers les étapes nécessaires pour obtenir les bons fichiers, créer un design à partir de zéro et le soumettre.

Pour mieux comprendre la conception de meubles paramétriques, consultez l'[article de conception](https://medium.com/@olapdesign/design-for-a-rocking-chair-8a1a1e109d7f). Expérimentez avec le concept et son potentiel créatif (contraint par les limitations de production physique).

Pour soumettre des designs à la galerie principale, assurez-vous de lire les [directives de conception](https://github.com/O-LAP/home/blob/master/guidelines.md).

_Article par Amit Nambiar pour O-lap_