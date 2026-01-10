---
title: Comment télécharger de grands fichiers vers Google Colab et des notebooks Jupyter
  distants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-14T15:37:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-transfer-large-files-to-google-colab-and-remote-jupyter-notebooks-26ca252892fa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_GgmGZJnFec994dvCDpbWQ.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Google
  slug: google
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: Comment télécharger de grands fichiers vers Google Colab et des notebooks
  Jupyter distants
seo_desc: 'By Bharath Raj

  If you haven’t heard about it, Google Colab is a platform that is widely used for
  testing out ML prototypes on its free K80 GPU. If you have heard about it, chances
  are that you gave it shot. But you might have become exasperated becau...'
---

Par Bharath Raj

Si vous n'en avez pas entendu parler, [Google Colab](http://g.co/colab) est une plateforme largement utilisée pour tester des prototypes de ML sur son **GPU K80 gratuit**. Si vous en avez entendu parler, il est probable que vous l'ayez essayé. Mais vous avez peut-être été exaspéré par la complexité impliquée dans le transfert de grands ensembles de données.

Ce blog compile certaines des méthodes que j'ai trouvées utiles pour **télécharger** et **télécharger** des **grands fichiers** de votre système local vers **Google Colab**. J'ai également inclus des méthodes supplémentaires qui peuvent être utiles pour transférer des **fichiers plus petits** avec moins d'effort. Certaines des méthodes peuvent être étendues à d'autres **services de notebooks Jupyter distants**, comme Paperspace Gradient.

### Transfert de grands fichiers

La méthode la plus efficace pour transférer de grands fichiers est d'utiliser un système de stockage cloud tel que **Dropbox** ou **Google Drive**.

#### 1. Dropbox

Dropbox offre jusqu'à 2 Go d'espace de stockage gratuit par compte. Cela fixe une limite supérieure à la quantité de données que vous pouvez transférer à tout moment. Le transfert via Dropbox est relativement **plus facile**. Vous pouvez également suivre les mêmes étapes pour **d'autres services de notebooks**, tels que **Paperspace Gradient**.

**Étape 1 : Archiver et télécharger**

Télécharger un grand nombre d'images (ou de fichiers) individuellement prendra beaucoup de temps, car Dropbox (ou Google Drive) doit attribuer des identifiants et des attributs à chaque image. Par conséquent, je recommande d'archiver d'abord votre ensemble de données.

Une méthode possible d'archivage consiste à convertir le dossier contenant votre ensemble de données en un fichier « .tar ». L'extrait de code ci-dessous montre comment convertir un dossier nommé « Dataset » dans le répertoire personnel en un fichier « dataset.tar », à partir de votre terminal Linux.

```bash
tar -cvf dataset.tar ~/Dataset
```

Alternativement, vous pourriez utiliser WinRar ou 7zip, selon ce qui est le plus pratique pour vous. Téléchargez l'ensemble de données archivé sur Dropbox.

**Étape 2 : Cloner le dépôt**

Ouvrez Google Colab et démarrez un nouveau notebook.

Clonez ce [dépôt GitHub](https://github.com/thatbrguy/Dropbox-Uploader.git). J'ai modifié le code [original](https://github.com/andreafabrizi/Dropbox-Uploader) afin qu'il puisse ajouter le jeton d'accès Dropbox depuis le notebook. Exécutez les commandes suivantes **une par une**.

```bash
!git clone https://github.com/thatbrguy/Dropbox-Uploader.git
cd Dropbox-Uploader
!chmod +x dropbox_uploader.sh
```

**Étape 3 : Créer un jeton d'accès**

Exécutez la commande suivante pour voir les instructions de configuration initiale.

```
!bash dropbox_uploader.sh
```

Il affichera des instructions sur la façon d'obtenir le jeton d'accès et vous demandera d'exécuter la commande suivante. Remplacez les lettres en gras par votre jeton d'accès, puis exécutez :

```bash
!echo "INPUT_YOUR_ACCESS_TOKEN_HERE" > token.txt
```

Exécutez **!bash dropbox_uploader.sh** à nouveau pour lier votre compte Dropbox à Google Colab. Maintenant, vous pouvez télécharger et téléverser des fichiers depuis le notebook.

**Étape 4 : Transférer le contenu**

**Télécharger vers Colab depuis Dropbox :**

Exécutez la commande suivante. L'argument est le nom du fichier sur Dropbox.

```bash
!bash dropbox_uploader.sh download YOUR_FILE.tar
```

**Télécharger vers Dropbox depuis Colab :**

Exécutez la commande suivante. Le premier argument (result_on_colab.txt) est le nom du fichier que vous souhaitez télécharger. Le deuxième argument (dropbox.txt) est le nom sous lequel vous souhaitez enregistrer le fichier sur Dropbox.

```bash
!bash dropbox_uploader.sh upload result_on_colab.txt dropbox.txt
```

#### 2. Google Drive

Google Drive offre jusqu'à 15 Go de stockage gratuit pour chaque compte Google. Cela fixe une limite supérieure à la quantité de données que vous pouvez transférer à tout moment. Vous pouvez toujours étendre cette limite à des quantités plus grandes. Colab simplifie le processus d'authentification pour Google Drive.

Cela dit, j'ai également inclus les modifications nécessaires que vous pouvez effectuer pour accéder à Google Drive depuis d'autres services de notebooks Python.

**Étape 1 : Archiver et télécharger**

Tout comme avec Dropbox, télécharger un grand nombre d'images (ou de fichiers) individuellement prendra beaucoup de temps, car Google Drive doit attribuer des identifiants et des attributs à chaque image. Je recommande donc d'archiver d'abord votre ensemble de données.

Une méthode possible d'archivage consiste à convertir le dossier contenant votre ensemble de données en un fichier « .tar ». L'extrait de code ci-dessous montre comment convertir un dossier nommé « Dataset » dans le répertoire personnel en un fichier « dataset.tar », à partir de votre terminal Linux.

```bash
tar -cvf dataset.tar ~/Dataset
```

Et encore une fois, vous pouvez utiliser WinRar ou 7zip si vous préférez. Téléchargez l'ensemble de données archivé sur Google Drive.

**Étape 2 : Installer les dépendances**

Ouvrez Google Colab et démarrez un nouveau notebook. Installez PyDrive en utilisant la commande suivante :

```bash
!pip install PyDrive
```

Importez les bibliothèques et méthodes nécessaires (les imports en **gras** ne sont nécessaires que pour Google Colab. Ne les importez pas si vous n'utilisez pas Colab).

```py
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials
```

**Étape 3 : Autoriser le SDK Google**

**Pour Google Colab :**

Maintenant, vous devez autoriser le SDK Google à accéder à Google Drive depuis Colab. Tout d'abord, exécutez les commandes suivantes :

```py
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)
```

Vous obtiendrez une invite comme indiqué ci-dessous. Suivez le lien pour obtenir la clé. Copiez et collez-la dans la boîte d'entrée et appuyez sur Entrée.

![Image](https://cdn-media-1.freecodecamp.org/images/hzfWkut06QN9A99io686hCuHLETczZemgM9Y)
_Invite pour authentifier l'utilisateur_

**Pour d'autres services de notebooks Jupyter (Ex : Paperspace Gradient) :**

Certaines des étapes suivantes sont obtenues à partir du [guide de démarrage rapide](https://pythonhosted.org/PyDrive/quickstart.html) de PyDrive.

Allez sur [APIs Console](https://console.developers.google.com/iam-admin/projects) et créez votre propre projet. Ensuite, recherchez « Google Drive API », sélectionnez l'entrée et cliquez sur « Activer ». Sélectionnez « Identifiants » dans le menu de gauche, cliquez sur « Créer des identifiants », sélectionnez « ID client OAuth ». Vous devriez voir un menu tel que l'image montrée ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/jP9acVWbTFaXXFctxTPZNSuw2EP2xqZZVg0R)

Définissez « Type d'application » sur « Autre ». Donnez un nom approprié et cliquez sur « Enregistrer ».

Téléchargez l'ID client OAuth 2.0 que vous venez de créer. **Renommez**-le en **client_secrets.json**

Téléchargez ce fichier JSON vers votre notebook. Vous pouvez le faire en cliquant sur le bouton « Télécharger » depuis la page d'accueil du notebook (montré ci-dessous). **(Note : Ne** utilisez pas ce bouton pour télécharger votre ensemble de données, car cela prendra extrêmement de temps.)

![Image](https://cdn-media-1.freecodecamp.org/images/dOEeYDLPP98VFZDSNqXTYxkzc9B6o8fsRdTn)
_Bouton de téléchargement montré en rouge_

Maintenant, exécutez les commandes suivantes :

```py
gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)
```

Le reste de la procédure est **similaire** à celle de Google Colab.

**Étape 4 : Obtenir l'ID de votre fichier**

Activez le partage de lien pour le fichier que vous souhaitez transférer. Copiez le lien. Vous pouvez obtenir un lien tel que celui-ci :

```
https://drive.google.com/open?id=YOUR_FILE_ID
```

Copiez uniquement la partie en gras du lien ci-dessus.

**Étape 5 : Transférer le contenu**

**Télécharger vers Colab depuis Google Drive :**

Exécutez les commandes suivantes. Ici, **YOUR_FILE_ID** est obtenu à l'étape précédente, et **DOWNLOAD.tar** est le nom (ou le chemin) sous lequel vous souhaitez enregistrer le fichier.

```py
download = drive.CreateFile({'id': 'YOUR_FILE_ID'})
download.GetContentFile('DOWNLOAD.tar')
```

**Télécharger vers Google Drive depuis Colab :**

Exécutez les commandes suivantes. Ici, **FILE_ON_COLAB.txt** est le nom (ou le chemin) du fichier sur Colab, et **DRIVE.txt** est le nom (ou le chemin) sous lequel vous souhaitez enregistrer le fichier (sur Google Drive).

```py
upload = drive.CreateFile({'title': 'DRIVE.txt'})
upload.SetContentFile('FILE_ON_COLAB.txt')
upload.Upload()
```

### Transfert de fichiers plus petits

Occasionnellement, vous pouvez vouloir transférer un seul fichier csv et ne pas vouloir passer par tout ce processus. Pas de soucis, il existe des méthodes beaucoup plus simples pour cela.

#### 1. Module files de Google Colab

Google Colab dispose de son module **files** intégré, avec lequel vous pouvez télécharger ou téléverser des fichiers. Vous pouvez l'importer en exécutant ce qui suit :

```
from google.colab import files
```

**Pour téléverser :**

Utilisez la commande suivante pour téléverser des fichiers vers Google Colab :

```py
files.upload()
```

Vous serez présenté avec une interface graphique avec laquelle vous pouvez sélectionner les fichiers que vous souhaitez téléverser. Il n'est **pas recommandé** d'utiliser cette méthode pour les fichiers de grande taille. C'est très lent.

**Pour télécharger :**

Utilisez la commande suivante pour télécharger un fichier depuis Google Colab :

```py
files.download('example.txt')
```

Cette fonctionnalité fonctionne mieux dans **Google Chrome**. Selon mon expérience, elle n'a fonctionné qu'une fois sur Firefox, sur environ 10 tentatives.

#### 2. GitHub

C'est une méthode un peu « hack-ish » pour transférer des fichiers. Vous pouvez créer un dépôt GitHub avec les petits fichiers que vous souhaitez transférer.

Une fois que vous avez créé le dépôt, vous pouvez simplement le cloner dans Google Colab. Vous pouvez ensuite pousser vos modifications vers le dépôt distant et tirer les mises à jour sur votre système local.

Mais notez que GitHub a une limite stricte de 25 Mo par fichier et une limite souple de 1 Go par dépôt.

> Merci d'avoir lu cet article ! Laissez quelques applaudissements si vous le trouvez intéressant ! Si vous avez des questions, vous pouvez me contacter sur les [réseaux sociaux](https://thatbrguy.github.io/) ou m'envoyer un email (bharathrajn98[at]gmail[dot]com).