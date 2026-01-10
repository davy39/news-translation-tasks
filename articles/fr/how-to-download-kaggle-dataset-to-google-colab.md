---
title: Comment télécharger un jeu de données Kaggle directement dans un notebook Google
  Colab
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2024-02-08T19:39:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-download-kaggle-dataset-to-google-colab
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Kaggle-to-Colab.png
tags:
- name: Data Science
  slug: data-science
- name: Google Colab
  slug: google-colab
- name: kaggle
  slug: kaggle
- name: Machine Learning
  slug: machine-learning
seo_title: Comment télécharger un jeu de données Kaggle directement dans un notebook
  Google Colab
seo_desc: 'Kaggle is a popular data science-based competition platform that has a
  large online community of data scientists and machine learning engineers.

  The platform contains a ton of datasets and notebooks that you can use to learn
  and practice your data sc...'
---

[Kaggle](https://www.kaggle.com/) est une plateforme de compétition basée sur la science des données qui possède une grande communauté en ligne de scientifiques des données et d'ingénieurs en machine learning.

La plateforme contient une multitude de jeux de données et de notebooks que vous pouvez utiliser pour apprendre et pratiquer vos compétences en science des données et en machine learning. Ils ont même des compétitions auxquelles vous pouvez participer.

Kaggle offre une plateforme 100% gratuite pour tous les utilisateurs – mais il y a certaines restrictions selon les ressources que vous utilisez. 

Par exemple, vous pouvez utiliser leur système CPU pendant un temps illimité. Mais il y a des limitations strictes sur l'utilisation du GPU et du TPU. Vous pouvez utiliser leur GPU pendant 30 heures et leur TPU pendant 20 heures par semaine. Cela se réinitialise chaque semaine, et vous obtenez alors 30 heures d'utilisation du GPU et 20 heures d'utilisation du TPU au début de la nouvelle semaine.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_14-21.png)
_Site Web de Kaggle_

En parallèle de Kaggle, il existe d'autres plateformes populaires pour les ingénieurs en machine learning et les scientifiques des données – comme [Google Colaboratory](https://colab.google/), ou Google Colab en abrégé.

Dans Google Colab, vous pouvez également utiliser leur CPU et GPU, mais les versions gratuites ont plus de limitations que le compte Kaggle gratuit. Dans Google Colab, vous ne pouvez pas obtenir de puissance de calcul GPU tant qu'ils ne vous l'ont pas allouée depuis leurs unités gratuites. Vous ne savez pas combien d'heures vous pouvez utiliser, et vous ne savez même pas si vous avez une chance d'obtenir des unités dans les prochains jours. 

Pour obtenir toutes les fonctionnalités, vous devez souscrire à leurs plans pro qui sont assez coûteux.

Mais parfois, vous pouvez toujours vouloir utiliser Colab, dans la plupart des cas pour des tâches courtes. Dans Colab, vous pouvez connecter directement votre Google Drive et utiliser vos jeux de données depuis là. Vous pouvez également stocker votre sortie du notebook vers Google Drive si vous le souhaitez.

Lorsque vous travaillez sur un projet, cependant, parfois vous voudrez utiliser des jeux de données de Kaggle dans Google Colab. Vous devrez donc télécharger le jeu de données depuis Kaggle et le téléverser vers le stockage temporaire de Colab ou votre Google Drive. 

Vous pouvez probablement deviner que c'est un processus très chronophage. 

Mais il existe un moyen de télécharger directement un jeu de données Kaggle en utilisant un appel API dans le notebook de Google Colab ! Dans cet article, je vais vous montrer comment vous pouvez faire cela.

## Table des matières

J'ai divisé ce tutoriel en parties séparées pour une meilleure compréhension. Vous pouvez obtenir un aperçu clair de l'ensemble de l'article ici :

* [Types de jeux de données Kaggle](#heading-types-de-jeux-de-donnees-kaggle)
* [Prérequis](#heading-prerequis)
* [Configuration de Google Colab pour utiliser l'API Kaggle](#heading-installation-de-google-colab-pour-utiliser-lapi-kaggle)
* [Installer la bibliothèque Kaggle](#heading-installer-la-bibliothèque-kaggle)
* [Monter Google Drive sur Colab](#heading-monter-google-drive-sur-colab)
* [Ajouter le jeton API Kaggle au notebook Colab](#heading-ajouter-le-jeton-api-kaggle-au-notebook-colab)
* [Télécharger un jeu de données Kaggle](#heading-télécharger-un-jeu-de-données-kaggle)
* [Télécharger un jeu de données de compétition Kaggle](#heading-télécharger-un-jeu-de-données-de-compétition-kaggle)
* [Télécharger un fichier spécifique d'un jeu de données de compétition Kaggle](https://www.freecodecamp.org/news/p/906afd5c-ae59-4f19-9fe3-662d110d63a7/download-specifc-file-from-kaggle-competition-dataset)
* [Conclusion](#heading-conclusion)

## Vidéo

Si vous souhaitez regarder toutes les étapes dans une vidéo, vous avez de la chance – j'ai fait cette vidéo juste pour vous :

%[https://www.youtube.com/watch?v=7Z0s-XDXR1E]

## Types de jeux de données Kaggle

Normalement, Kaggle propose deux types de jeux de données : des jeux de données typiques que n'importe qui peut téléverser, et des jeux de données de compétition. Dans les jeux de données de compétition, les organisateurs de la compétition ajoutent/téléversent généralement les jeux de données. 

Bien que vous puissiez télécharger un jeu de données Kaggle facilement, vous ne pouvez pas télécharger un jeu de données de compétition si vous ne participez pas à cette compétition. Mais certaines compétitions restent ouvertes, et vous pouvez accéder à leurs jeux de données via "Soumission tardive". Assurez-vous simplement de vérifier.

## Prérequis

Pour suivre ce tutoriel et en tirer le meilleur parti, vous aurez besoin d'un compte Kaggle, et cela est complètement gratuit. Rendez-vous simplement sur le site officiel de [Kaggle](https://www.kaggle.com/), et créez un compte si vous n'en avez pas déjà un.

Vous aurez également besoin de l'API de Kaggle. Rendez-vous dans les [paramètres](https://www.kaggle.com/settings) de votre compte Kaggle. Allez dans la section API, et cliquez sur "Créer un nouveau jeton". Gardez à l'esprit que Kaggle ne vous permet pas de conserver plusieurs jetons. Vous ne pouvez utiliser qu'un seul jeton actif pour votre compte Kaggle.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_14-52.png)
_Jeton API Kaggle_

Cela vous donnera un fichier `kaggle.json`. Conservez-le en sécurité, car vous en aurez besoin plus tard.

Vous avez également besoin d'un compte Google si vous souhaitez utiliser Google Colab. Vous en avez peut-être déjà un, mais si ce n'est pas le cas, allez-y et créez un nouveau compte Google.

Maintenant, vous pouvez stocker votre JSON Kaggle dans votre Google Drive. Je préfère créer un nouveau dossier et y conserver mon fichier JSON afin de pouvoir l'appeler dans Colab quand je le souhaite.

## Comment configurer Google Colab pour utiliser l'API Kaggle

Vous pouvez simplement ouvrir n'importe quel notebook Colab où vous souhaitez utiliser l'API Kaggle pour télécharger le jeu de données.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_15-45.png)
_Google Colab_

### Installer la bibliothèque Kaggle

Vous devez installer la bibliothèque Python Kaggle avant de commencer à travailler avec Kaggle. Vous pouvez simplement l'installer dans le notebook colab en utilisant la commande `! pip install kaggle`.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_15-46.png)
_Installer la bibliothèque Kaggle dans colab_

### Monter Google Drive sur Colab

Maintenant, vous devez monter votre Google Drive sur le notebook Colab, puisque vous avez téléversé votre fichier `kaggle.json` à l'intérieur de votre Google Drive.

Vous pouvez simplement le faire en utilisant les deux lignes de code données ci-dessous :

```python
from google.colab import drive
drive.mount('/content/drive')
```

Assurez-vous de lui donner la permission d'accéder à votre Google Drive :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_15-48.png)
_Donner l'accès à Google Drive_

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_15-49.png)
_Monter Google Drive_

Si vous actualisez l'icône du dossier monté, vous verrez votre Google Drive et tout son contenu dans le notebook.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_15-49_1.png)
_Trouver MyDrive dans le Notebook_

### Ajouter le jeton API Kaggle au notebook Colab

Maintenant, vous devez ajouter le jeton API Kaggle au notebook. Mais avant cela, vous pouvez simplement créer un répertoire temporaire pour Kaggle à l'emplacement de l'instance temporaire sur le lecteur Colab en utilisant la commande `! mkdir ~/.kaggle`.

Maintenant, vous devez copier votre fichier JSON téléversé dans ce répertoire temporaire Kaggle. Vous avez besoin de l'URL où vous avez téléversé votre fichier JSON précédemment. Vous pouvez obtenir ce lien directement depuis le dossier du lecteur dans le notebook.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-08-155504.png)
_Copier l'emplacement du fichier JSON_

Vous pouvez obtenir le chemin directement comme ceci. 

Ensuite, vous pouvez utiliser la commande de copie comme ci-dessous :

```bash
! cp kaggle_json_path ~/.kaggle/
```

Par exemple, mon fichier JSON est situé à "/content/drive/MyDrive/Kaggle_API/kaggle.json", donc ma commande serait :

```bash
! cp /content/drive/MyDrive/Kaggle_API/kaggle.json ~/.kaggle/
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_15-58_1.png)
_Copier le fichier JSON_

Maintenant, vous devez changer les permissions du fichier en lecture/écriture pour le propriétaire uniquement pour des raisons de sécurité.

Vous pouvez utiliser la commande ci-dessous pour y parvenir :

```bash
! chmod 600 ~/.kaggle/kaggle.json
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_15-59.png)
_Changer les permissions du fichier kaggle.json_

## Comment télécharger le jeu de données Kaggle

Pour télécharger un jeu de données typique de Kaggle, vous devez d'abord trouver le jeu de données sur Kaggle.

Supposons que je veux télécharger le jeu de données suivant depuis Kaggle :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_16-01.png)
_Jeu de données exemple_

Vérifiez l'URL complète du jeu de données, qui dans ce cas est :

[https://www.kaggle.com/datasets/mdfahimbinamin/fastsurfer-processed-3d-brain-mri-from-adni](https://www.kaggle.com/datasets/mdfahimbinamin/fastsurfer-processed-3d-brain-mri-from-adni)

%[https://www.kaggle.com/datasets/mdfahimbinamin/fastsurfer-processed-3d-brain-mri-from-adni]

Nous avons besoin de la chaîne "nom_de_compte_du_propriétaire_du_jeu_de_données/chemin_du_jeu_de_données". À partir de l'URL, le nom de compte du propriétaire du jeu de données est mdfahimbinamin. Le chemin du jeu de données est fastsurfer-processed-3d-brain-mri-from-adni.

Donc, pour télécharger ce jeu de données exact depuis Kaggle vers votre Google Colab, votre commande serait :

```bash
! kaggle datasets download mdfahimbinamin/fastsurfer-processed-3d-brain-mri-from-adni
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_16-06.png)
_Téléchargement du jeu de données Kaggle dans votre notebook Colab_

L'ensemble du processus se déroule sur le PC Cloud de Google. Donc, la vitesse de téléchargement devrait être assez rapide.

Par défaut, les jeux de données viennent sous forme de fichier `.zip`. Donc, si vous devez les décompresser, vous pouvez simplement utiliser la commande ci-dessous :

```bash
! unzip chemin_du_jeu_de_données.zip
```

Par exemple, le nom/chemin de mon jeu de données était "fastsurfer-processed-3d-brain-mri-from-adni". Donc, j'utiliserai la commande suivante :

```bash
! unzip fastsurfer-processed-3d-brain-mri-from-adni.zip
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_16-09.png)
_Décompresser le jeu de données Kaggle_

C'est tout ! 😊

## Comment télécharger un jeu de données de compétition Kaggle

Avant de télécharger un jeu de données de compétition, vous devez vous assurer que vous avez rejoint cette compétition ou que vous avez sélectionné "Soumission tardive" en utilisant le même compte Kaggle que vous utilisez pour le jeton API Kaggle.

Supposons que je rejoins la compétition ConnectX sur Kaggle.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_16-15.png)
_Compétition Connect X_

Je dois cliquer sur "Rejoindre la compétition" pour obtenir l'accès à leur jeu de données.

Mais si je veux télécharger un jeu de données d'une compétition passée, je dois rejoindre leur "Soumission tardive" pour obtenir leur jeu de données.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_16-16.png)
_Rejoindre une compétition passée_

Après avoir cliqué sur "Soumission tardive", je dois récupérer l'URL. Cette fois, j'utilise le jeu de données de Classification Binaire avec un jeu de données de désabonnement bancaire. L'URL complète est : [https://www.kaggle.com/competitions/playground-series-s4e1/overview](https://www.kaggle.com/competitions/playground-series-s4e1/overview)

À partir de l'URL, je peux voir que le jeu de données est situé à "playground-series-s4e1". Donc, j'utiliserai la commande suivante pour télécharger le jeu de données dans mon notebook Google Colab :

```bash
! kaggle competitions download playground-series-s4e1
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_16-19.png)
_Télécharger le jeu de données_

C'est tout ! 😊

## Comment télécharger un fichier spécifique d'un jeu de données de compétition Kaggle

Supposons que je veux télécharger un fichier spécifique d'un jeu de données de compétition Kaggle. Je peux aussi faire cela.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_16-21.png)
_Jeu de données_

Dans le jeu de données utilisé ci-dessus, vous pouvez voir qu'il y a 3 fichiers. Supposons que je veux télécharger uniquement le fichier `test.csv`. 

Pour ce faire, la commande serait structurée comme suit : `! kaggle competitions download chemin_du_jeu_de_données -f nom_du_fichier_avec_extension`.

Donc, ma commande serait :

```bash
! kaggle competitions download playground-series-s4e1 -f test.csv
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-08_16-23.png)
_Télécharger un fichier spécifique_

C'est tout ! 😊

## Conclusion

J'espère que vous avez acquis des informations précieuses grâce à cet article.

Si vous avez apprécié les procédures étape par étape, n'oubliez pas de me le faire savoir sur [Twitter/X](https://twitter.com/Fahim_FBA) ou [LinkedIn](https://www.linkedin.com/in/fahimfba/).

Vous pouvez également me suivre sur [GitHub](https://github.com/FahimFBA) si vous êtes intéressé par l'open source. Assurez-vous de consulter [mon site web](https://fahimbinamin.com/) ([https://fahimbinamin.com/](https://fahimbinamin.com/)) également !

Si vous aimez regarder des vidéos sur la programmation et la technologie, vous pouvez également consulter ma [chaîne YouTube](https://www.youtube.com/@FahimAmin?sub_confirmation=1). Vous pouvez également consulter mes autres écrits sur [Dev.to](https://dev.to/fahimfba).

Je vous souhaite le meilleur pour votre parcours en programmation et en développement. 😊

Vous pouvez le faire ! Ne lâchez rien, jamais ! 💔