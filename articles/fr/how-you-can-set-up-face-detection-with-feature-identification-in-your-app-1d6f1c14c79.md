---
title: Comment configurer la détection de visage avec identification des caractéristiques
  dans votre application
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-22T15:39:31.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-set-up-face-detection-with-feature-identification-in-your-app-1d6f1c14c79
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YnsDJKmh013JSYBVXZ7KDg.jpeg
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: Machine Learning
  slug: machine-learning
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment configurer la détection de visage avec identification des caractéristiques
  dans votre application
seo_desc: 'By Rohit Ramname

  Find the faces with Microsoft Cognitive Services, Azure, and JavaScript


  _Photo by [Unsplash](https://unsplash.com/photos/mMolCwtrEss?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" ...'
---

Par Rohit Ramname

#### Trouvez les visages avec Microsoft Cognitive Services, Azure et JavaScript

![Image](https://cdn-media-1.freecodecamp.org/images/K1PR2n3zSKsdfQH-BlnQD9S2XtC7rzu7O57f)
_Photo par [Unsplash](https://unsplash.com/photos/mMolCwtrEss?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Vanessa Serpas</a> sur <a href="https://unsplash.com/search/photos/face?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Qu'est-ce que la détection de visage ?

Vous avez probablement vu la détection de visage en action à de nombreuses reprises, dans différentes applications — par exemple sur votre téléphone, dans les photos sur Facebook. La détection de visage résulte en des rectangles autour des visages. Comme le suggère le nom, il s'agit simplement de détecter un visage dans une image. C'est également un cas d'utilisation de **l'apprentissage automatique**.

Dans ce tutoriel, nous allons apprendre à effectuer la détection de visage en utilisant les **Cognitive Services** de Microsoft fournis par **Azure**, ainsi que du **JavaScript** et du **CSS** simples.

### Qu'est-ce que je vais apprendre dans ce tutoriel ?

À la fin de ce tutoriel, nous devrions être en mesure d'obtenir le résultat ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/iXj0mo7EbVzNGkwwejoymi4vMpkPeoT0W0Qs)

Veuillez noter que, en plus de la détection de visage, Azure nous donne également l'âge approximatif et si la personne porte des lunettes, des caractéristiques qui peuvent être demandées dans l'URL.

Ce tutoriel garantira que nous sommes configurés avec un abonnement Azure et que nous obtenons les résultats requis.

**Cet exercice suppose que vous avez un abonnement Microsoft Azure.** Si vous n'en avez pas, vous pouvez en créer un gratuitement en allant sur le site [web](https://azure.microsoft.com/en-us/free/) de Microsoft Azure. Il vous demandera des informations sur votre carte de crédit, mais votre carte ne sera jamais débitée sauf si des services payants sont achetés (ce qui n'est pas requis pour cette démonstration).

### Commençons

Tout d'abord, nous nous connectons à notre abonnement Microsoft Azure.

Allez sur « Portal.azure.com » et connectez-vous avec votre identifiant.

Cliquez sur « Créer une ressource » et recherchez « Face ».

![Image](https://cdn-media-1.freecodecamp.org/images/pWBktCmM22poTQCu9O0ffDJ-XwuzXFR278oG)

Dans les résultats de recherche, sélectionnez Face (Catégorie : « AI + Machine Learning »).

Cliquez sur **Créer**.

Vous devrez remplir un simple formulaire qui vous demandera de :

* donner un nom à votre ressource
* sélectionner votre abonnement
* sélectionner votre géolocalisation où se trouvera principalement votre base d'utilisateurs
* sélectionner votre plan tarifaire (il existe un plan gratuit que vous pouvez sélectionner à des fins d'essai).
* puis cliquez sur « Créer »

Une fois que vous avez suivi ces étapes, Azure déployera vos services et créera des clés d'abonnement.

Ouvrez votre abonnement en cliquant dessus et allez dans la section « Vue d'ensemble ».

![Image](https://cdn-media-1.freecodecamp.org/images/F9qllAlSy-VV235jE3cTsPqJYZU7yqpFKPqp)

C'est ici que vous pouvez trouver vos clés d'abonnement et vos clés d'accès. Vous devrez envoyer une clé d'accès avec chaque en-tête d'appel API pour l'authentification.

C'est tout pour la configuration.

### Testons-le

Maintenant, nous pouvons tester si notre API fonctionne en utilisant un outil appelé [Postman](https://www.getpostman.com/apps).

**Postman est un outil très populaire pour tester les appels API.**

Ouvrez Postman et utilisez le point de terminaison dans votre abonnement Azure comme URL. Assurez-vous que l'opération sélectionnée dans la liste déroulante est « POST ».

![Image](https://cdn-media-1.freecodecamp.org/images/hP4vpX4xQ03JOgvGod30j4cdzkVbwa8bd3lQ)

Dans l'onglet « Headers », ajoutez :

* la « Key » « Ocp-Apim-Subscription-Key » avec la « Value » [vos clés d'abonnement Azure]
* la « Key » « Content-Type » avec la « Value » « application/octet-stream »

![Image](https://cdn-media-1.freecodecamp.org/images/tO2WWVz38lE8fLJcy1qLH8BUihdabaNUiSOR)

Dans l'onglet « Body », choisissez « binary » et cliquez sur « Choose Files » pour sélectionner une photo avec un visage humain.

![Image](https://cdn-media-1.freecodecamp.org/images/pgpPb-EfwRP6-GYOnLG27UNY-Q7qT5fazD5g)

Cliquez sur « Send ».

Vous devriez voir une réponse comme ci-dessous de la part des appels API des services cognitifs Azure.

```
[ { "faceId": "4f3df6bb-83d9-45ea-bac5-d60cac5a1623", "faceRectangle": { "top": 456, "left": 475, "width": 330, "height": 330 } }]
```

Azure attribue automatiquement un identifiant à chaque visage qu'il peut détecter et donne les coordonnées du visage sur cette photo.

Vous pouvez demander à Azure différentes attributs de visage. Pour la liste complète des attributs, veuillez vous référer au [site web de Microsoft](https://westus.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236).

Par exemple, pour demander si une personne porte des lunettes de soleil et obtenir un âge estimé, vous pouvez envoyer la chaîne de requête : [https://eastus.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceAttributes=age,glasses](https://eastus.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceAttributes=age,glasses,emotion). Pour cette requête, Azure enverra l'âge estimé, le type de lunettes (ou pas de lunettes) et l'analyse des émotions.

```
[ { "faceId": "f8721afb-f9d8-4372-ab43-23fd429aafbf", "faceRectangle": { "top": 640, "left": 297, "width": 202, "height": 202 }, "faceAttributes": { "age": 31, "glasses": "Sunglasses", "emotion": { "anger": 0, "contempt": 0.001, "disgust": 0, "fear": 0, "happiness": 0, "neutral": 0.998, "sadness": 0, "surprise": 0 } } }]
```

Super. Il semble que nous ayons une configuration de base prête.

Mais avant d'arrêter de lire cet article et de fermer la fenêtre...

### Passons aux choses intéressantes :

Nous allons connecter tout cela à une page web pour voir les résultats.

Nous aurons besoin d'une simple page HTML avec un **contrôle de téléchargement de fichier** afin que nous puissions sélectionner un fichier image.

```
<div id="containerDiv"> <div id="titleDiv"> Bienvenue </div> <div id="content"> <div id="btnUpload"> <div class="upload-btn-wrapper"> <button class="btn">Télécharger un fichier</button> <input type="file" name="myfile" id="upload" /> </div></div> <div id="features"> </div> <div id="imgDiv"><img id="imgx" class="imageContainer"><div id="face"></div></div></div> </div>
```

Décomposons cela pour comprendre ce que c'est.

Cette page a deux sections : le titre et le contenu.

Le titre `<div>` est assez simple. Il s'agit simplement du titre de l'application avec un identifiant.

Le contenu `<div>` a trois sections :

* le bouton de téléchargement `<button>`, qui est le bouton principal de cette application
* les caractéristiques `<div>`, qui contiendront les caractéristiques de l'image du visage
* l'image `<div>`, qui rendra l'image sélectionnée

Plus bas, la div Image a deux composants.

* l'image avec l'id `="imgx"`, qui est l'image réelle sélectionnée, et
* `<div>` avec l'id=`"face"`, qui est le rectangle d'identification du visage.

C'est tout pour la partie HTML.

### Maintenant, la partie principale — l'appel JavaScript

#### Code

Tout d'abord, ajoutez un écouteur à l'événement « File Selected » lorsqu'un fichier est sélectionné.

`document.getElementById('upload').addEventListener('change', fileChange, false);`

Ajoutez la fonction d'événement `fileChange` :

```
function fileChange(event){ if(event.target.files && event.target.files.length >= 0) { var file1= event.target.files[0]; var reader = new FileReader(); reader.onload = (event) => { document.getElementById("imgx").src=event.target.result; getFaceDetails(file1); } } reader.readAsDataURL(event.target.files[0]); }
```

Lorsque l'événement est déclenché, c'est-à-dire que le fichier est sélectionné :

* les détails de l'événement sont lus `var file1= event.target.files[0];`
* une nouvelle instance d'objet de la classe FileReader est créée `var reader = new FileReader();`
* le contenu du fichier sélectionné dans l'événement est lu `reader.readAsDataURL(event.target.files[0]);`

Maintenant, lorsque le fichier est complètement chargé, la propriété `src` de l'élément `imgx` est définie :

```
document.getElementById("imgx").src=event.target.result;
```

et il appelle la fonction qui obtiendra en interne les informations sur le visage à partir de l'image :

```
getFaceDetails(file1);
```

Regardons la fonction `getFaceDetails` :

```
function getFaceDetails(file){ var xmlHttp = new XMLHttpRequest(); var url="https://eastus.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceAttributes=age,glasses"; xmlHttp.open("POST",url,true); xmlHttp.setRequestHeader("Content-Type", "application/octet-stream");
```

```
xmlHttp.setRequestHeader("Ocp-Apim-Subscription-Key", "[Azure Face API subscription key]"); xmlHttp.send(file); xmlHttp.onreadystatechange = function (response) { if (this.readyState == 4 && this.status == 200) { let face=JSON.parse(this.responseText) var oleft = document.getElementById("imgx").offsetLeft; var otop = document.getElementById("imgx").offsetTop; document.getElementById("face").style.left=oleft+face[0].faceRectangle.left+"px"; document.getElementById("face").style.top=otop+face[0].faceRectangle.top+"px"; document.getElementById("face").style.width=face[0].faceRectangle.width+"px"; document.getElementById("face").style.height=face[0].faceRectangle.height+"px"; document.getElementById("features").innerText="Age: "+face[0].faceAttributes.age +" Glasses:"+face[0].faceAttributes.glasses ; } }}
```

**WHOA...**!! Cela semble compliqué.

#### Explication

Oui... c'est... un peu ! Mais laissez-moi expliquer.

Les premières lignes de cette fonction ouvrent simplement une requête `XMLHttpRequest` JavaScript avec une URL et des en-têtes de requête. L'URL est l'URL Azure que vous avez fournie ci-dessus dans Postman — ou que vous pouvez obtenir à partir du portail Azure.

```
var xmlHttp = new XMLHttpRequest(); var url="https://eastus.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceAttributes=age,glasses"; xmlHttp.open("POST",url,true);
```

Nous avons ensuite ajouté deux en-têtes de requête. Le premier est la clé `Ocp-Apim-Subscription-Key` et votre clé d'abonnement Azure. Le second est la clé `Content-Type` avec la valeur `application/octet-stream`. Puisque nous allons envoyer une image dans une requête, `application/octet-stream` est le type pour les données binaires.

```
xmlHttp.setRequestHeader("Ocp-Apim-Subscription-Key", "[Azure Face API subscription key]");
```

```
xmlHttp.setRequestHeader("Content-Type", "application/octet-stream");
```

Et ensuite nous faisons l'appel :

```
xmlHttp.send(file);
```

Lorsque la requête est terminée, celle-ci a un état prêt de 4. Nous obtenons les coordonnées de la partie visage de l'image au format JSON ainsi que les caractéristiques.

```
xmlHttp.onreadystatechange = function (response) { if (this.readyState == 4 && this.status == 200) { let face=JSON.parse(this.responseText)
```

Puisque nous allons rendre l'image au centre, nous avons besoin des coordonnées gauche et haut de l'image rendue. Cela nous permet de positionner notre rectangle de visage `<div>` en conséquence.

```
var oleft = document.getElementById("imgx").offsetLeft;var otop = document.getElementById("imgx").offsetTop;
```

Et maintenant, nous devons simplement dessiner un rectangle ("face" `<div>`) autour du visage sur l'image rendue.

```
document.getElementById("face").style.left=oleft+face[0].faceRectangle.left+"px"; document.getElementById("face").style.top=otop+face[0].faceRectangle.top+"px"; document.getElementById("face").style.width=face[0].faceRectangle.width+"px"; document.getElementById("face").style.height=face[0].faceRectangle.height+"px";
```

Et lire les attributs de caractéristiques également dans la div des caractéristiques.

```
document.getElementById("features").innerText="Age: "+face[0].faceAttributes.age +" Glasses:"+face[0].faceAttributes.glasses ;
```

Et cela conclut la partie JS.

Ci-dessous se trouve le style CSS de base pour le rendu. **Veuillez noter** que nous utilisons la grille CSS.

```
#containerDiv{ display:grid; grid-template-areas:  "title" "content"}
```

```
#imgDiv{ background-repeat: no-repeat; border: 1px solid #bbb; border: solid; grid-area:image;}#face{ position:absolute; border:solid; border-style: ridge; border-color: cornsilk;}#features{ grid-area:features}#titleDiv{ height: 100px; display: flex; justify-content: center; align-items: center; font-size: -webkit-xxx-large; background-color: black; color: sandybrown; font-family: sans-serif; grid-area:title;}
```

```
#content{ display:grid; justify-items:center; grid-area:content; grid-template-areas:  "upload" "features" "image"}#btnUpload{ grid-area:upload;}.upload-btn-wrapper { position: relative; overflow: hidden; display: inline-block; padding: 2%; width: 100vw; display: flex; justify-content: center; } .btn { border: 2px solid gray; color:white; background-color:cornflowerblue; padding: 8px 20px; border-radius: 8px; font-size: 20px; font-weight: bold; }  .upload-btn-wrapper input[type=file] { font-size: 100px; position: absolute; left: 0; top: 0; opacity: 0; }
```

Il est **très important** de garder la **position** du contrôle d'image (`imgx`) et de la `Face` `<div>` absolue pour un rendu correct. Sinon, la `Face` `<div>` ne sera pas rendue sur l'image. Elle sera quelque part sur le côté comme un effet en ligne.

### Nous y voilà...

Maintenant, vous pouvez ouvrir la page web, sélectionner l'image avec un visage humain et voir les résultats.

La détection de visage peut être encore améliorée en demandant des fonctionnalités supplémentaires dans l'URL d'Azure. Par exemple, vous pouvez ajouter l'affichage des sentiments.

J'espère que vous avez trouvé ce tutoriel passionnant et que vous allez construire des **choses cool** avec.

Bon apprentissage !