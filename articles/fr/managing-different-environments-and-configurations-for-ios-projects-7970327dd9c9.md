---
title: Comment gérer différents environnements et configurations pour les projets
  iOS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-18T10:51:44.000Z'
originalURL: https://freecodecamp.org/news/managing-different-environments-and-configurations-for-ios-projects-7970327dd9c9
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cb264740569d1a4cac1c3.jpg
tags:
- name: Apple
  slug: apple
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment gérer différents environnements et configurations pour les projets
  iOS
seo_desc: 'By Boudhayan Biswas

  As iOS developers, we are already aware of managing different environments like
  Development, QA, Beta, and Production. For these different environments, there are
  different server URLs, app icons, and configurations.

  So before cre...'
---

Par Boudhayan Biswas

En tant que développeurs iOS, nous sommes déjà conscients de la gestion de différents environnements comme Développement, QA, Bêta et Production. Pour ces différents environnements, il existe différentes URL de serveur, icônes d'application et configurations.

Ainsi, avant de créer une nouvelle build pointant vers un environnement, nous devons garder à l'esprit que nous devons également changer l'URL du serveur. Nous pourrions le faire en changeant une valeur de flag codée en dur dans le fichier constant ou en utilisant des macros, mais cela complique tout.

Mais si nous réfléchissons un peu, nous pouvons trouver une idée. Et en appliquant cette idée, nous pouvons facilement gérer n'importe quel scénario. L'idée est donc la suivante : si nous créons différents schémas et configurations, cela nous permet de changer les URL du serveur de l'application, l'icône de l'application, le fichier Plist et la configuration.

Dans ce tutoriel, je vais vous montrer comment gérer différents environnements en utilisant des schémas et des configurations.

Voici les étapes :

#### **Installation du projet :**

Ouvrez XCode et créez une nouvelle application à vue unique avec un nom approprié.

#### **Ajout de schéma et de configurations :**

Avant d'ajouter un schéma, nous devons savoir que chaque schéma XCode est livré avec deux configurations de build différentes : **Debug** et **Release**. Ensuite, si nous le souhaitons, nous pouvons apporter des modifications spécifiques à une configuration de build particulière.

Pour ajouter nos configurations de build, sélectionnez le projet dans le volet **Project Navigator** à gauche. Ensuite, sélectionnez **Info** parmi les deux options (**Info** et **Build Settings**). Dans **Configurations**, nous devons ajouter notre propre configuration pour les cinq environnements (Développement, Production, QA, Bêta et UAT).

![Image](https://cdn-media-1.freecodecamp.org/images/1*5IHSpl7Pm7qdzjJ0VXpO9w.png)
_Ajouter une nouvelle configuration pour un environnement (Debug et Release)_

Tout d'abord, double-cliquez sur **Debug** et renommez-le en **Debug (Développement)**. De même, double-cliquez sur **Release** et renommez-le en **Release (Développement)**. Maintenant, cliquez sur +, et sélectionnez **Dupliquer Debug (Développement)** et **Dupliquer Release (Développement)**, puis changez le nom de l'environnement dupliqué avec les autres noms disponibles.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ytKEoM7Fp-pi6eXdVde8XA.png)
_Après avoir ajouté toutes les configurations pour différents environnements_

Pour la **création de schéma**, allez dans gérer le schéma en haut à gauche de XCode. Vous pouvez voir qu'un schéma est déjà disponible. Renommez-le en **Développement —** ou vous pouvez supprimer celui existant et en ajouter un nouveau avec le nom **Développement**. Ensuite, ajoutez les quatre autres schémas pour les autres environnements.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JVJ5eY0P-wkS2ViI5rj4-w.png)
_Ajouter un nouveau schéma pour un environnement_

Oups, n'oubliez pas de cocher la case partagée. Après avoir ajouté tous les schémas, l'écran de gestion des schémas devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*v_rGZmAYjZe_p4R6usHwTg.png)
_Tous les schémas sont ajoutés_

#### Ajout du fichier de paramètres de configuration :

Faites un clic droit sur le projet, sélectionnez nouveau fichier, puis ajoutez un fichier de paramètres de configuration et donnez-lui le même nom que l'environnement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EWfTg9WN09lbX8v-KcHDQw.png)
_Fichier de paramètres de configuration_

Après avoir ajouté tous les fichiers de configuration, votre volet gauche du navigateur de projet devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*53B3UEp-ZMzRvQdj1EEL-w.png)
_Fichiers de configuration ajoutés_

Maintenant, la partie la plus importante commence : ajoutez votre **URL de serveur** et d'autres valeurs de clé personnalisées dans le fichier de configuration correspondant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xECXRXHZGrqvL9ijPLgGiQ.png)
_URL de serveur ajoutée dans le fichier de configuration_

#### Ajout de fichiers Plist :

Renommez le fichier info.plist en development.plist. Copiez et collez le même fichier plist pour les différents environnements à l'intérieur du projet, et renommez chaque fichier plist avec le nom de l'environnement. Vous pouvez définir certaines clés et valeurs spécifiques à l'environnement dans les fichiers plist. Après cela, ajoutez les clés du fichier de configuration aux fichiers plist comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*hMBtu6KdmmIgybiF53dSOw.png)
_Ajouter des clés dans le fichier Plist_

Maintenant, nous devons définir le chemin plist approprié pour chaque configuration de build. À partir des cibles, sélectionnez simplement un fichier plist, et renommez-le avec le même nom pour les configurations **Debug** et **Release**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*eFuPiN80FOC4Y3Ea4G2N1Q.png)
_Ajouter le chemin Plist pour la configuration de build_

![Image](https://cdn-media-1.freecodecamp.org/images/1*9H2q_Lgql8R7BKyW1sqDww.png)
_Fichiers Plist renommés_

#### Lier la configuration de build avec le fichier de configuration :

Sélectionnez toutes les configurations de build (Debug et Release) dans **Projects Info** une par une. Ensuite, définissez le fichier de configuration approprié, que vous avez ajouté au projet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*W8_auNFU_NRDcsA21Msa0w.png)
_Définir le fichier de configuration pour la configuration de build_

Après avoir ajouté tous les fichiers de configuration, vos paramètres de build devraient ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*sNPBwjaXWmYZSAe_3CdFpw.png)
_Fichier de configuration et configuration de build_

Nous avons donc maintenant lié avec succès tous les fichiers de configuration aux configurations de build respectives.

#### Lier le schéma avec la configuration de build :

Maintenant, la dernière étape consiste à lier le schéma avec la configuration de build. Pour ce faire, sélectionnez un schéma, allez dans modifier le schéma, et définissez la configuration de build appropriée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*o-OY3Yzv7GzmlSs09o2uyA.png)
_Lier le schéma et la configuration de build_

#### Prêt à exécuter le projet :

Maintenant, toute la configuration est terminée. La seule chose que vous avez à faire est de sélectionner le schéma et d'exécuter — l'environnement sera automatiquement sélectionné pour vous. Pour récupérer l'URL du serveur et d'autres valeurs, j'ai créé un fichier Environment.swift. Jetez un coup d'œil :

Pour récupérer l'URL du serveur ou d'autres paramètres dans ViewController.Swift ou tout autre fichier, vous devez écrire une seule ligne de code :

Vous pouvez également gérer différentes icônes d'application pour différents environnements à partir des paramètres de build. Ensuite, vous n'aurez qu'à regarder une seconde pour voir quelle build d'environnement est installée sur votre appareil.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GyDczhyCu8IGrR1jlS0Miw.png)

Le projet complet est disponible sur [GitHub](https://github.com/boudhayan/DemoEnvTest). Vous pouvez le télécharger si vous avez des questions.

Ne passez pas de temps supplémentaire à changer l'URL du serveur ou une autre configuration chaque fois que vous construisez votre projet. C'est le moyen le plus simple de gérer différents environnements, icônes d'application et configurations.

Si vous aimez cela, n'oubliez pas de donner un applaudissement. Cela m'inspirera davantage. Pour toute suggestion, n'hésitez pas à écrire un email à _mail2boudhayan@gmail.com._