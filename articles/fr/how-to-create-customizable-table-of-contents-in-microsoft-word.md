---
title: Comment créer une table des matières personnalisable dans Word
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-11-23T15:34:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-customizable-table-of-contents-in-microsoft-word
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/pexels-skitterphoto-1005324.jpg
tags:
- name: how-to
  slug: how-to
- name: organization
  slug: organization
- name: writing
  slug: writing
seo_title: Comment créer une table des matières personnalisable dans Word
seo_desc: 'By MaximeF

  It''s tricky to make a good-looking and functional table of contents in Microsoft
  Word.

  You might often encounter documents that have messy tables of contents along with
  navigation panes with links to missing headings, non harmonized styles...'
---

Par MaximeF

Il est délicat de créer une table des matières esthétique et fonctionnelle dans Microsoft Word.

Vous pouvez souvent rencontrer des documents avec des tables des matières désordonnées, des volets de navigation avec des liens vers des titres manquants, des styles non harmonisés et des sections mal structurées.

Ce ne serait pas un gros problème pour des documents plus petits, mais avec des centaines de pages dans un fichier, cela ruine l'expérience utilisateur et rend la navigation d'une section à l'autre pénible. Sans parler des styles non harmonisés dans tout le fichier qui peuvent perturber la hiérarchie globale des titres.

Alors, comment construire une table des matières structurée et personnalisable avec des titres personnalisés et une numérotation esthétique ? Vous apprendrez comment faire dans ce guide.

## Comment construire une table des matières dans Microsoft Word

### Comment définir les styles de numérotation dans Word

Ce que nous allons faire en premier, c'est définir un nouveau style de liste pour créer une numérotation personnalisée pour nos titres. Allez dans l'onglet **Accueil** > section **Paragraphe** et cliquez sur le bouton de liste multiniveau. Choisissez **Définir un nouveau style de liste**.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-72.png)

Cela ouvrira la fenêtre **Définir un nouveau style de liste** que nous utiliserons pour personnaliser le style et le format de numérotation de nos titres.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-77.png)

Nommez votre style comme vous le souhaitez (ici MonNouveauStyleDeListe), puis cliquez sur le bouton **Format** > **Numérotation...** Cela ouvrira la fenêtre **Modifier la liste multiniveau**.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-79.png)

Nous allons uniquement définir la numérotation ("1)", "a)") et aucun format ou style ne sera appliqué à ce niveau. Nous définirons et appliquerons les styles et formats de police plus tard.

Prenons la numérotation suivante pour nos titres : "1.", "1.1", "1.1.1", "2.", "2.1", "2.2" et ainsi de suite.

Commencez par remplacer le caractère parenthèse par un caractère point dans le champ **Saisir le format pour le numéro**. Cela changera le format de numérotation de niveau 1 en "1.".

Ensuite, nous définirons le deuxième niveau de numérotation en cliquant sur le numéro 2 dans la liste **Cliquer sur le niveau à modifier**.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-80.png)

Changez le **Style de numéro pour ce niveau** en cliquant sur le menu déroulant associé, puis sélectionnez **1, 2, 3, ...** Vous devriez obtenir ce résultat :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-82.png)

Effacez le caractère parenthèse dans le champ **Saisir le format pour le numéro** et placez un point avant le "1". Vous devriez avoir ".1".

Maintenant, comment obtenir le style de numérotation 1.1 au niveau 2 ? Très simple ! Placez votre souris avant le ".1" dans le champ **Saisir le format pour le numéro**. Ensuite, ouvrez le menu déroulant **Inclure le numéro de niveau de** et sélectionnez **Niveau 1**.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-88.png)

Cela insérera la numérotation pour le niveau 1 avant votre numérotation pour le niveau 2. Vous devriez obtenir ce résultat :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-86.png)

L'insertion manuelle de nombres dans ce champ vous donnera des nombres statiques qui ne seront pas liés à une numérotation dynamique dans votre document. Ces nombres ne seront pas mis en surbrillance en gris dans le champ **Saisir le format pour le numéro**.

Répétons les mêmes étapes pour le niveau 3. Sélectionnez le niveau **3** dans la liste **Cliquer sur le niveau à modifier**. Sélectionnez le bon **Style de numéro pour ce niveau** dans le menu déroulant. Supprimez les caractères indésirables et ajoutez un point avant le "1".

Ensuite, placez votre souris avant le ".1" dans le champ **Saisir le format pour le numéro** et ouvrez le menu déroulant **Inclure le numéro de niveau de** et sélectionnez **niveau 2**. Ajoutez un point avant le "1" du niveau 2 dans le champ **Saisir le format pour le numéro**. Ensuite, ouvrez **Inclure le numéro de niveau de** et sélectionnez **niveau 1**. Vous devriez obtenir ce résultat :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-89.png)

Vous pouvez modifier le caractère espace suivant le numéro en cliquant sur **Plus >>** puis **Suivre le numéro avec** et sélectionnez ce que vous voulez. Ici, je vais utiliser **Caractère de tabulation** pour tous mes niveaux.

Cliquez sur le bouton **OK** et vous avez terminé pour la partie numérotation ! Vous n'aurez pas à refaire ces étapes car les styles que vous définissez peuvent être disponibles d'un document Word à l'autre. Nous en parlerons plus tard.

Votre style de liste devrait être disponible en cliquant sur le bouton **Liste multiniveau** dans la section **Paragraphe** de l'onglet **Accueil**.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-90.png)

Nous allons maintenant définir nos styles de titre.

### Comment définir les styles de titre dans Word

Dans l'onglet **Accueil** et sous la section **Style**, cliquez sur la flèche vers le bas à côté des différents styles disponibles.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/2021-11-20-11_57_32-Document1---Word.png)

Puis cliquez sur **Créer un style**.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-92.png)

Donnez un nom à votre nouveau style. Il est bon de pratique d'inclure le numéro de niveau où vous allez appliquer ce titre pour faciliter le suivi de votre hiérarchie de titres. Je vais nommer le mien NouveauStyle1 pour le niveau 1. Puis cliquez sur **Modifier**.

Si vous avez cliqué sur **OK** trop vite, ne vous inquiétez pas – vous pouvez trouver votre style et le modifier à tout moment dans la section style. Vous pouvez l'éditer en faisant un clic droit dessus et en cliquant sur **Modifier...**

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-94.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-95.png)

Nous allons appliquer un formatage à notre style de titre.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-96.png)

Commencez par ouvrir le menu déroulant **Style basé sur** et sélectionnez **Titre 1** pour le niveau 1. C'est une étape importante pour que Word comprenne le niveau de hiérarchie du titre. Vous appliquerez cette étape à chaque niveau (Titre 2 pour votre style de niveau 2, Titre 3 pour votre style de niveau 3...).

Ouvrez ensuite le menu **Style pour le paragraphe suivant** et sélectionnez Normal. Cela empêchera toute mise en forme de s'appliquer automatiquement aux lignes de texte suivantes que vous tapez.

Ouvrez le menu **Format** et ouvrez le menu **Numérotation...**. Assurez-vous que Aucun est sélectionné, puis cliquez sur **OK**. Cela empêchera tout conflit avec la numérotation que nous avons définie précédemment.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-97.png)

Vous pouvez ensuite sélectionner toute mise en forme de police que vous souhaitez. Voici ce que j'ai choisi :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-98.png)

Créons un style pour les niveaux 2 et 3 en suivant les mêmes étapes. Assurez-vous d'avoir la numérotation définie sur **Aucun** à chaque fois. Voici ce que j'ai pour le niveau 2 :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-99.png)

Et le niveau 3 :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-100.png)

Nous allons maintenant lier nos styles de titre avec notre style de numérotation.

Allez dans l'onglet **Accueil**, section **Paragraphe**, **Liste multiniveau**. Ensuite, faites un clic droit sur le style de liste de numérotation que nous avons créé dans la première partie et cliquez sur **Modifier**.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-101.png)

Ouvrez la fenêtre de numérotation en cliquant sur **Format**. Sélectionnez le niveau 1 et dans le menu déroulant **Lier le niveau au style**, sélectionnez le style de niveau 1 que vous avez créé pour votre titre de niveau 1. Vous devriez obtenir ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-102.png)

Répétez ces étapes pour les niveaux 2 et 3.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-103.png)

Puis cliquez sur OK.

### Comment appliquer vos nouveaux styles de titre

Essayons maintenant d'appliquer nos nouveaux styles de titre. Tapez Titre 1 dans votre document sans appliquer de formatage.

Si vous avez déjà un format appliqué, vous pouvez le supprimer en cliquant dans le paragraphe et en appliquant le style **Normal** dans la section **Styles**. Cela est utile pour supprimer tout formatage ou style indésirable que vous pourriez trouver.

Maintenant, cliquez dans le texte Titre 1 et cliquez sur votre style nouvellement créé pour le niveau 1. Cela appliquera votre style de niveau 1 à tout le paragraphe.

Si vous allez dans l'onglet **Affichage**, vous pouvez vérifier le **Volet de navigation** et voir que "1. Titre 1" vient d'apparaître comme un titre sélectionnable dans le panneau de navigation de gauche, vous permettant d'y accéder rapidement.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-105.png)

Essayons également nos autres styles de titre. Tapez le texte sans formatage, placez votre souris dans le paragraphe pertinent, puis cliquez sur vos styles nouvellement créés pour les appliquer. Vous devriez obtenir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-106.png)

Comme vous pouvez le voir dans le panneau de gauche, tous mes titres apparaissent de manière structurée avec une numérotation harmonisée. Vous pouvez réduire ou développer ceux-ci pour naviguer plus rapidement. Il y a également un moteur de recherche disponible en haut de ce panneau.

Vous pouvez maintenant insérer une table des matières structurée en allant dans l'onglet **Références** > **Table des matières** > **Table automatique 1**. Vous devriez maintenant avoir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-110.png)

Vous pouvez personnaliser cette table des matières pour n'afficher que les titres jusqu'à un certain niveau en cliquant sur **Table des matières** > **Table des matières personnalisée** > diminuer le nombre de **Niveaux à afficher** > **OK**.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-111.png)

### Comment conserver vos styles dans Word

Pour le moment, ces styles de titre ne sont disponibles que dans ce fichier Word. Nous allons les rendre disponibles chaque fois que nous ouvrons Word ainsi que les rendre transférables à d'autres personnes.

Ouvrez l'onglet Développeur dans Word. Si vous ne le voyez pas affiché, cliquez sur **Fichier** > **Options** > **Personnaliser le ruban** > Cochez **Développeur** dans le panneau de droite > **OK**.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-107.png)

Une fois dans l'onglet **Développeur**, allez dans **Modèle de document** > **Organisateur**.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-108.png)

Dans le panneau de gauche (dans Document1 pour moi), vous pouvez voir les styles disponibles dans ce fichier. Dans le panneau de droite se trouvent les styles disponibles dans le Normal.dotm qui vous permet de stocker des styles qui seront disponibles chaque fois que vous ouvrez Word.

Sélectionnons tous nos styles nouvellement créés, puis cliquez sur **Copier->**. Vous devriez obtenir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-109.png)

Maintenant, si vous ouvrez un autre fichier, vos styles seront directement disponibles dans la section des styles. Cela peut être utile si vous souhaitez transférer des styles parmi votre groupe et harmoniser la structure et le format de vos fichiers.

### C'est tout !

Voilà ! Vous êtes maintenant capable de construire un document Word structuré avec des styles de titres personnalisables et un volet de navigation fiable.