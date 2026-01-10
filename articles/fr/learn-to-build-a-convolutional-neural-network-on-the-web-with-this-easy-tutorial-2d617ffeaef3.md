---
title: Apprenez à construire un réseau de neurones convolutionnel sur le web avec
  ce tutoriel facile
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-18T10:32:13.000Z'
originalURL: https://freecodecamp.org/news/learn-to-build-a-convolutional-neural-network-on-the-web-with-this-easy-tutorial-2d617ffeaef3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aIR9I9JDL5GyVxINeQXy7g.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Apprenez à construire un réseau de neurones convolutionnel sur le web avec
  ce tutoriel facile
seo_desc: 'By John David Chibuk

  This post explains how to build your first Convolutional Neural Network (CNN) to
  detect between two image types: for example, a bunny or a puppy.

  Thanks to Google’s new web tool, getting started building and prototyping your own
  ...'
---

Par John David Chibuk

Cet article explique comment construire votre premier réseau de neurones convolutionnel (CNN) pour détecter deux types d'images : par exemple, un lapin ou un chiot.

Grâce au nouvel outil web de Google, il est assez facile de commencer à construire et à prototyper votre propre réseau de neurones.

Voici un [lien](https://drive.google.com/file/d/1a7V9Hc7ks0xxDbfCZl2_96DUGlCLuh00/view?usp=sharing) vers l'application basée sur le web. Elle vous montre le code et vous permet d'exécuter le code du notebook Jupyter "paragraphe par paragraphe" (**shift+enter**) pour vous permettre d'entraîner un modèle et ensuite le tester. Trouvez le [dépôt public Github ici](https://github.com/chibuk/simple-cnn-keras-colaboratory/tree/master).

**La première étape consiste à configurer le notebook Colab + les dossiers de données d'images sur votre propre Google Drive, alors faisons cela !**

Dans votre Google Drive, vous devrez configurer des dossiers avec des images qui stockent les données à entraîner. Vous pouvez [copier ce dossier](https://drive.google.com/drive/folders/1rcihLGtsL8WbaYhBAShz8ntqr8G9BvPP?usp=sharing) directement et le mettre dans votre propre Google Drive, puis le décompresser et le mettre dans un dossier appelé "Colab Notebooks" dans votre dossier de base Google Drive.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ALReQ6ZGyihWCrj1dxaZ6g.png)
_Capture d'écran du Google Drive personnel_

Dans le dossier images, il y a deux sous-dossiers.

> train

> test

![Image](https://cdn-media-1.freecodecamp.org/images/1*KN1hY9fwsJ4_89v45PYgQA.png)
_Capture d'écran du Google Drive personnel_

Chacun de ces dossiers contient ensuite des dossiers représentant les types d'images que vous souhaitez identifier.

> bunny

> puppy

Il devrait y avoir un dossier bunny et un dossier puppy dans chaque dossier train + test.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ec40wwNgWLfFDYwMjXp03w.png)
_Capture d'écran du Google Drive personnel_

Remplissez ces dossiers avec des images. Mettez ~80% dans le dossier train et 20% dans le dossier test.

La partie délicate du tutoriel consiste à lier correctement les dossiers dans Google Drive. Vous devez vous connecter via des clés API plusieurs fois pour établir la connexion appropriée à votre dossier Google Drive personnel.

Veuillez noter : vous devez conserver la même structure de dossiers que celle définie dans le tutoriel pour qu'il fonctionne correctement.

Dans votre dossier de base Google Drive, vous devez avoir un dossier appelé : Colab Notebooks.

À l'intérieur, il doit y avoir un répertoire appelé : Simple CNN Image Tutorial

Celui-ci doit contenir le contenu des images et du notebook Colab ci-dessus.

### Étape par étape

**Étape 1** installe les bibliothèques requises pour construire et entraîner un modèle avec TensorFlow + Keras de Google. Keras est une couche simplifiée pour faciliter l'entraînement des modèles sur TensorFlow.

**Étape 2-5** lie votre Google Drive au projet, copie les clés depuis les cellules et les colle dans le notebook au fur et à mesure qu'elles sont générées. Cela peut prendre quelques essais, mais ce n'est pas grave !

**Étape 6** Vous pouvez changer la structure, mais vous devrez mettre à jour le chemin dans le notebook pour qu'il corresponde à l'emplacement où vous avez mis le dossier de base Simple CNN Image Tutorial.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Cw3unWxH0dzAhkEjAAurjA.png)
_Capture d'écran du notebook CoLaboratory (Étape 6)_

**Étape 7** confirme que vous avez vos images chargées dans Google Drive.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qeWPe1_oEcGxPGPUBZdB0Q.png)
_Capture d'écran du notebook CoLaboratory (Étape 7)_

Pour exécuter le processus, cliquez simplement sur la première zone de paragraphe et appuyez sur "shift + enter" sur votre clavier. Cela exécute le code dans chaque cellule et vous permet de suivre le processus.

**Étape 9** entraîne votre modèle. Si tout est correctement référencé, il devrait afficher une sortie comme ceci ->

![Image](https://cdn-media-1.freecodecamp.org/images/1*bfNiqh12lfRKi19QBpOGOA.png)
_Capture d'écran du notebook CoLaboratory (Étape 9)_

Lorsque c'est terminé, votre modèle sera entraîné et vous pourrez tester des images à partir de ce que vous avez mis dans le nouveau dossier images :

![Image](https://cdn-media-1.freecodecamp.org/images/1*HwQMoikc5fHGy926WKii0g.png)
_Capture d'écran du notebook CoLaboratory (ajoutez de nouvelles images ici ou utilisez celles-ci pour essayer votre réseau entraîné !)_

Changez simplement le texte du nom de l'image dans la ligne de code :

```
test_image = image.load_img('./newimages/puppy3.jpg', target_size = (64, 64))
```

Par exemple, vous changeriez :

```
'./newimages/puppy3.jpg' en './newimages/bunny1.jpg'
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*kj0G3pgNloyY2cgUa2b3gQ.png)
_Capture d'écran du notebook CoLaboratory (Étape 10)_

Enfin, exécutez le paragraphe et voyez ce que votre modèle classe la nouvelle image !

### Félicitations, vous venez d'entraîner et de tester votre premier réseau de neurones convolutionnel — c'est génial !

![Image](https://cdn-media-1.freecodecamp.org/images/1*7gqbeeOQP1vJhLYfKkPpzQ.png)
_Crédit : [http://media.riffsy.com/images/7bafc4dc0036792b32a5e5aa6c5ac9ff/tenor.gif](http://media.riffsy.com/images/7bafc4dc0036792b32a5e5aa6c5ac9ff/tenor.gif" rel="noopener" target="_blank" title=")_