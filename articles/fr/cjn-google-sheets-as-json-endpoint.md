---
title: Comment utiliser Google Sheets comme un point de terminaison JSON
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-21T23:26:00.000Z'
originalURL: https://freecodecamp.org/news/cjn-google-sheets-as-json-endpoint
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/0_kycb_xJ-enmTWhvL.png
tags:
- name: backend
  slug: backend
- name: google sheets
  slug: google-sheets
- name: json
  slug: json
seo_title: Comment utiliser Google Sheets comme un point de terminaison JSON
seo_desc: 'By Clark Jason Ngo

  UPDATE: 5/13/2020 - New Share Dialog Box steps available below.


  Thanks Erica H!


  Are you building a prototype dynamic web application and need to collaborate with
  non-developers?

  I have been to a hackathon before and experienced p...'
---

Par Clark Jason Ngo

MISE À JOUR : 13/05/2020 - Les étapes de la [Nouvelle Boîte de Dialogue de Partage](https://gsuiteupdates.googleblog.com/2020/04/new-file-sharing-dialog-google-drive.html) sont disponibles ci-dessous.

> Merci Erica H !



Êtes-vous en train de construire une application web dynamique prototype et avez besoin de collaborer avec des non-développeurs ?

J'ai déjà participé à un hackathon et j'ai vécu l'expérience de participer avec la connaissance de comment développer une application, mais j'ai manqué de compétences ou de temps pour implémenter une application web full-stack dans le sprint de 3 jours. À cette époque, mes compétences étaient bien trop faibles pour aider et j'ai été mis de côté pour regarder des tutoriels et étudier HTML et CSS.

Le résultat ? J'ai beaucoup appris, mais j'aurais souhaité pouvoir contribuer davantage.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-125.png)

Lors de l'un des hackathons auxquels j'ai récemment participé, j'ai rencontré un problème similaire. Cette fois-ci, je n'étais pas le débutant. J'avais des non-ingénieurs qui voulaient aider à construire notre application web prototype. Heureusement, nous sommes tombés sur Google Spreadsheets comme moyen pour nos non-ingénieurs de créer une maquette de notre base de données et de permettre aux développeurs back-end de se connecter au point de terminaison JSON de Google Sheets et de le parser.

Avec ce guide, vous serez en mesure de :

1. Créer une feuille de calcul dans Google Spreadsheets.
2. Publier la feuille de calcul sur le web.
3. Générer un point de terminaison JSON.
4. Ouvrir la feuille de calcul pour une collaboration publique.
5. Transmettre le point de terminaison JSON à votre développeur back-end.

Après ce tutoriel, vous serez en mesure de rejoindre des équipes et de dire : "Je peux aider avec le back-end !".

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-126.png)

### Section 1 : Créer une feuille Google Sheets

**Étape 1 :**

Allez sur [Google Sheets](https://docs.google.com/spreadsheets/u/0/)

**Étape 2 :**

Créez une nouvelle feuille de calcul

![Image](https://cdn-media-1.freecodecamp.org/images/1*2md2vMHKWXzXbWOwddzXPw.png)

### Section 2 : Publier votre Google Sheets sur le web

_Note : Nouvelle boîte de dialogue de partage mise à jour au 13/05/2020, située après l'Étape 2._

**Étape 1 :**

Cliquez sur **_Fichier_** _>_ **_Publier sur le web_**

![Image](https://cdn-media-1.freecodecamp.org/images/1*XFtPyWBYh3JX6PdQUJ5j-w.png)

**Étape 2 :**

Cliquez sur **_Publier_**, puis sur **_OK_**

![Image](https://cdn-media-1.freecodecamp.org/images/1*QtAY0n29zHviNXdsPJZaQQ.png)

**Étape 3 :**

Aucune action nécessaire ici

![Image](https://cdn-media-1.freecodecamp.org/images/1*WenBwpAkxyDc4fhGPeC6Dw.png)

### MISE À JOUR : 13/05/2020 - Nouvelle Boîte de Dialogue de Partage

**Étape 1 :**  
Cliquez sur Partager

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-108.png)

**Étape 2 :**

Cliquez sur "Changer pour toute personne disposant du lien"

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-107.png)

**Étape 3 :**

Cliquez sur "Terminé"

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-109.png)



### Section 4 : Utiliser votre Google Sheets comme point de terminaison JSON

**Étape 1 :**

Copiez l'URL du modèle et collez-la dans la barre d'adresse :

[https://spreadsheets.google.com/feeds/cells/YOURGOOGLESHEETCODE/SHEETPAGENUMBER/public/full?alt=json](https://spreadsheets.google.com/feeds/cells/1g4FBktkm7al3ZkDI8LuFXuztTqK4nY-eUYMLep6BRuw/1/public/full?alt=json)

**Étape 2 :**

Allez dans votre Google Sheets ouvert et vérifiez la barre d'adresse

![Image](https://cdn-media-1.freecodecamp.org/images/1*xRIMehCRmQxSQpAWi2bhlQ.png)
_URL de Google Sheets_

![Image](https://cdn-media-1.freecodecamp.org/images/1*AM6_ME5wgoQdtfMHFB_ipg.png)
_Code de Google Sheets_

**Étape 3 :**

Allez à l'URL du modèle et remplacez

* **_YOURGOOGLESHEETCODE_** par **_1ifbWzueslEP5-_ysP6gg7o_NaHQmqF8LlXBfStCwFMs_**
* **_SHEETPAGENUMBER_** par **_1_**

**Étape 4 :**

Récupérez l'URL JSON

[https://spreadsheets.google.com/feeds/cells/1ifbWzueslEP5-_ysP6gg7o_NaHQmqF8LlXBfStCwFMs/1/public/full?alt=json](https://spreadsheets.google.com/feeds/cells/1ifbWzueslEP5-_ysP6gg7o_NaHQmqF8LlXBfStCwFMs/1/public/full?alt=json)

![Image](https://cdn-media-1.freecodecamp.org/images/1*SU97RXIK-rFaMWEfaP1kng.png)
_Résultat de l'URL JSON_

### Section 5 : Rendre votre Google Sheets public (pour la collaboration et la saisie de données)

#### Étape 1 :

En haut à droite, cliquez sur **_Partager_**

![Image](https://cdn-media-1.freecodecamp.org/images/1*O2SCuizLuiLPFFBQVRL9vw.png)

**Étape 2 :**

Ajoutez un nom, cliquez sur **_Enregistrer_**

![Image](https://cdn-media-1.freecodecamp.org/images/1*D6leg5gLfYpoTOXlrpFUcw.png)

**Étape 3 :**

Cliquez sur **_Avancé_**

![Image](https://cdn-media-1.freecodecamp.org/images/1*k7DGUBwGJnVIdZeuaQbGlA.png)

**Étape 4 :**

Cliquez sur **_Changer_**

![Image](https://cdn-media-1.freecodecamp.org/images/1*qkKSGYrYiNp861WQjaoUKg.png)

**Étape 5 :**

Cliquez sur **_On

Public sur le web_**, puis sur **_Enregistrer_**

![Image](https://cdn-media-1.freecodecamp.org/images/1*paO-_3OAzlhzW-oZQI9udw.png)

### **Problèmes courants :**

Si vous recevez la réponse ci-dessous, veuillez vérifier votre URL et assurez-vous d'utiliser le code Google Sheets dans la barre d'adresse.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xrfoHNKtE4uld3IylAI1Lw.png)

Si vous recevez la réponse ci-dessous, veuillez revenir à la Section 2 : Publier votre Google Sheets sur le web.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZL71DxnV5Rw6asXjpjjC1Q.png)

[**Clark Jason Ngo - Assistant d'Enseignement Diplômé - Institut de Technologie - City University of Seattle |**](https://www.linkedin.com/in/clarkngo/)  
[_Rejoignez LinkedIn * Passionné de former de nouveaux développeurs logiciels. Compétences Techniques : Git, MVC, JavaScript, NodeJS, ReactJS_www.linkedin.com](https://www.linkedin.com/in/clarkngo/)