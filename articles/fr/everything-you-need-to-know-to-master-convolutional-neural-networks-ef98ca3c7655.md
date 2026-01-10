---
title: Tout ce que vous devez savoir pour maîtriser les Réseaux de Neurones Convolutifs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-26T20:16:26.000Z'
originalURL: https://freecodecamp.org/news/everything-you-need-to-know-to-master-convolutional-neural-networks-ef98ca3c7655
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-Rip5afVhP2NlhVYfPp_mA.jpeg
tags:
- name: Computer Vision
  slug: computer-vision
- name: Data Science
  slug: data-science
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: 'tech '
  slug: tech
seo_title: Tout ce que vous devez savoir pour maîtriser les Réseaux de Neurones Convolutifs
seo_desc: 'By Tirmidzi Faizal Aflahi

  Look at the photo below:


  _Courtesy of [Pix2PixHD](https://github.com/NVIDIA/pix2pixHD" rel="noopener" target="blank"
  title=")

  That is not a real photo. You can open the image in a new tab and zoom into the
  image. Do you see...'
---

Par Tirmidzi Faizal Aflahi

Regardez la photo ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/Qo6M5bDKw4FummLtjX8NrAwl6hbz8uDtw9ut)
_Courtoisie de [Pix2PixHD](https://github.com/NVIDIA/pix2pixHD" rel="noopener" target="_blank" title=")_

**Ce n'est pas une vraie photo**. Vous pouvez ouvrir l'image dans un nouvel onglet et zoomer sur l'image. Voyez-vous les mosaïques ?

L'image est en fait générée par un programme appelé Intelligence Artificielle. Cela ne semble-t-il pas réaliste ? C'est génial, n'est-ce pas ?

Cela ne fait que 7 ans que la technologie a été rendue publique par Alex Krizhevsky et ses amis via la compétition ImageNet. Cette compétition est une compétition annuelle de Vision par Ordinateur pour catégoriser les images en 1000 classes différentes. Des Malamutes d'Alaska au papier toilette. Alex et ses amis ont construit quelque chose appelé AlexNet, et il a remporté la compétition avec une large marge entre lui et la deuxième place.

Cette technologie est appelée **Réseau de Neurones Convolutifs**. C'est une sous-branche des Réseaux de Neurones Profonds qui performe exceptionnellement bien dans le traitement des images.

![Image](https://cdn-media-1.freecodecamp.org/images/Fao8o7A2hPuF04JmdAL4fdh-P1CFodRdi985)
_Courtoisie de ImageNet_

L'image ci-dessus est le taux d'erreur produit par le logiciel qui a remporté la compétition il y a plusieurs années. En 2016, **il est en fait meilleur que la performance humaine** qui était d'environ 5%.

L'introduction de l'Apprentissage Profond dans ce domaine est en fait _révolutionnaire_ plus que simplement changeante.

### Architecture des Réseaux de Neurones Convolutifs

Alors, comment cette technologie fonctionne-t-elle ?

![Image](https://cdn-media-1.freecodecamp.org/images/iZ-JSs6hw3oDgPEn8Lw3wHdQDr4xNoU1tvjV)

Les Réseaux de Neurones Convolutifs performe mieux que les autres architectures de Réseaux de Neurones Profonds grâce à leur processus unique. Au lieu de regarder l'image un pixel à la fois, **les CNNs regroupent plusieurs pixels ensemble** (un exemple de pixel 3×3 comme dans l'image ci-dessus) afin qu'ils puissent comprendre un motif temporel.

D'une autre manière, les CNNs peuvent « voir » un groupe de pixels formant une ligne ou une courbe. Grâce à la nature profonde des Réseaux de Neurones Profonds, au niveau suivant, ils verront non pas le groupe de pixels, mais des groupes de lignes et de courbes formant certaines formes. Et ainsi de suite jusqu'à ce qu'ils forment une image complète.

![Image](https://cdn-media-1.freecodecamp.org/images/ogzEWfxkTLd-tGiwOIUvieopX-1rAioqoFSC)
_Réseau de Neurones Convolutifs Profonds par [Mynepalli](https://www.researchgate.net/figure/Learning-hierarchy-of-visual-features-in-CNN-architecture_fig1_281607765" rel="noopener" target="_blank" title=")_

Il y a beaucoup de choses que vous devez apprendre si vous voulez comprendre les CNNs, des choses très basiques, comme un noyau, des couches de pooling, et ainsi de suite. Mais de nos jours, **vous pouvez simplement plonger et utiliser de nombreux projets open source pour cette technologie.**

Cela est en fait vrai grâce à la technologie appelée **Apprentissage par Transfert**.

### Apprentissage par Transfert

L'Apprentissage par Transfert est une technique qui réutilise le modèle d'Apprentissage Profond terminé dans une autre tâche plus spécifique.

Par exemple, disons que vous travaillez dans une entreprise de gestion de trains et que vous souhaitez évaluer si vos trains sont à l'heure ou non. Et vous ne voulez pas ajouter une autre main-d'œuvre juste pour cette tâche.

**Vous pouvez simplement réutiliser un modèle de Réseau de Neurones Convolutifs d'ImageNet, peut-être ResNet (le gagnant de 2015) et ré-entraîner le réseau avec les images de votre flotte de trains. Et vous vous en sortirez très bien.**

Il y a deux principaux avantages concurrentiels lorsque vous utilisez l'Apprentissage par Transfert.

1. **Nécessite moins d'images pour bien performer que l'entraînement à partir de zéro**. La compétition ImageNet dispose d'environ 1 million d'images pour l'entraînement. En utilisant l'apprentissage par transfert, vous pouvez utiliser seulement 1000 ou même 100 images et bien performer car il est déjà entraîné avec ces 1 million d'images.
2. **Nécessite moins de temps pour atteindre de bonnes performances**. Pour être aussi bon qu'ImageNet, vous devrez entraîner le réseau pendant des jours, et cela ne compte pas le temps nécessaire pour modifier le réseau s'il ne fonctionne pas bien. En utilisant l'apprentissage par transfert, vous n'aurez besoin que de quelques heures ou même de minutes pour terminer l'entraînement pour certaines tâches. Beaucoup de temps économisé.

### Classification d'Images à Génération d'Images

Grâce à l'apprentissage par transfert, de nombreuses initiatives sont apparues. Si vous pouvez traiter certaines images et nous dire de quoi il s'agit, pourquoi ne pas construire l'image elle-même ?

_Défis acceptés !_

**Les Réseaux Antagonistes Génératifs** entrent en scène.

![Image](https://cdn-media-1.freecodecamp.org/images/zkTwwVivOhYrDKvsNo5bAaPiO8g-6NI8jXnM)
_CycleGAN par [Jun-Yan Zhu](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix" rel="noopener" target="_blank" title=")_

Cette technologie peut générer des images en utilisant certaines entrées.

Elle peut générer une photo réaliste à partir d'une peinture dans un type appelé CycleGAN que je vous montre dans la photo ci-dessus. Dans un autre cas d'utilisation, elle peut également générer une image d'un sac à partir de quelques croquis. Elle peut même générer une photo de haute résolution à partir d'une photo de basse résolution.

![Image](https://cdn-media-1.freecodecamp.org/images/JxxgUM7CBe1EGYEN2QHAfzkN6Lw6QSC4JCpo)
_[Super Resolution Generative Adversarial Network](https://github.com/tensorlayer/srgan" rel="noopener" target="_blank" title=")_

Incroyable, n'est-ce pas ?

Bien sûr. Et vous pouvez commencer à apprendre à les construire maintenant. Mais comment ?

### Tutoriel sur les Réseaux de Neurones Convolutifs

Alors, commençons. Vous apprendrez que commencer sur ce sujet est facile, très facile. Mais le maîtriser est d'un autre niveau.

Mettons de côté la maîtrise pour l'instant.

![Image](https://cdn-media-1.freecodecamp.org/images/7RlbToHPUJgIejBUne2NDMQWhDss3fTZ4S78)
_Photo par [Unsplash](https://unsplash.com/photos/5A06OWU6Wuc?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Thomas Verbruggen</a> sur <a href="https://unsplash.com/search/photos/columnar-cactus?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Après avoir parcouru pendant plusieurs jours, j'ai trouvé ce projet qui est vraiment adapté pour vous pour commencer.

### [Identification de Cactus Aériens](https://www.kaggle.com/c/aerial-cactus-identification)

Ceci est un projet de tutoriel de [Kaggle](https://www.kaggle.com/). Votre tâche est d'identifier s'il y a des cactus colonnaires dans une image aérienne.

Assez simple, n'est-ce pas ?

Vous recevrez 17 500 images à travailler et devrez étiqueter 4 000 images qui n'ont pas été étiquetées. Votre score est de 1 ou 100 % si les 4 000 images sont correctement étiquetées par votre programme.

![Image](https://cdn-media-1.freecodecamp.org/images/y6aBaIA1GC7twlFe4uFq6RY5dykaTDMG3xVX)
_Cactus_

Les images sont assez similaires à ce que vous voyez ci-dessus. Une photo d'une région qui peut ou non contenir un groupe de cactus colonnaires. Les photos sont de 32×32 pixels. Et elles montrent des cactus dans différentes directions puisque ce sont des photos aériennes.

Alors, qu'avez-vous besoin ?

### Réseaux de Neurones Convolutifs avec Python

Oui, Python, le langage populaire pour l'Apprentissage Profond. Avec de nombreux choix disponibles, vous pouvez pratiquement faire des essais et des erreurs pour chaque choix. Les choix sont :

1. **Tensorflow**, la bibliothèque d'Apprentissage Profond la plus populaire. Construite par des ingénieurs de Google et dispose de la plus grande base de contributeurs et de fans. Parce que la communauté est si grande, vous pouvez facilement trouver la solution à votre problème. Il a **Keras** comme enveloppe d'abstraction de haut niveau, qui est si favorable pour un débutant.
2. **Pytorch**. Ma bibliothèque d'Apprentissage Profond préférée. Construite purement sur Python et suivant les avantages et inconvénients de Python. Les développeurs Python seront extrêmement familiers avec cette bibliothèque. Elle dispose d'une autre bibliothèque appelée **FastAI** qui donne l'abstraction que Keras a pour Tensorflow.
3. **MXNet**. La bibliothèque d'Apprentissage Profond par Apache.
4. **Theano**. Prédécesseur de Tensorflow
5. **CNTK**. Microsoft a également sa propre bibliothèque d'Apprentissage Profond.

Pour ce tutoriel, utilisons ma préférée, Pytorch, complétée par son abstraction, FastAI.

Avant de commencer, vous devez installer Python. Allez sur le [site web de Python](https://www.python.org/downloads/) et téléchargez ce dont vous avez besoin. Vous devez vous assurer que vous installez la **version 3.6+**, ou elle peut ne pas être supportée par les bibliothèques que vous allez utiliser.

Maintenant, ouvrez votre ligne de commande ou terminal et installez ces éléments

```
pip install numpy pip install pandas pip install jupyter
```

**Numpy** sera utilisé pour stocker les images entrées. Et **pandas** pour travailler avec les fichiers CSV. Jupyter notebook est ce dont vous avez besoin pour coder de manière interactive avec Python.

Ensuite, allez sur le [site web de Pytorch](https://pytorch.org/) et téléchargez ce dont vous avez besoin. Vous pourriez avoir besoin de la version CUDA pour accélérer votre vitesse d'entraînement. Mais assurez-vous que vous avez la version 1.0+ pour Pytorch.

Après cela, installez torchvision et FastAI :

```
pip install torchvision pip install fastai
```

Exécutez Jupyter avec la commande **jupyter notebook** et il ouvrira une fenêtre de navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/DZEbPNLsV51dIziniiLp0Z6KtlqUaUzjk2rL)

Maintenant, vous êtes prêt à commencer.

### Préparer les Données

Importez le code nécessaire :

```
import numpy as npimport pandas as pd from pathlib import Path from fastai import * from fastai.vision import * import torch %matplotlib inline
```

Numpy et Pandas sont toujours nécessaires pour tout ce que vous voulez faire. FastAI et Torch sont votre bibliothèque d'Apprentissage Profond. Matplotlib Inline sera utilisé pour afficher les graphiques.

Maintenant, téléchargez les fichiers de données depuis le [site web de la compétition](https://www.kaggle.com/c/aerial-cactus-identification/data).

Extrayez le fichier zip de données et placez-les à l'intérieur du dossier du notebook Jupyter.

Disons que vous avez nommé votre notebook Cacti. Votre structure de dossier serait comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/R5fQ0dLngqrAVLPRl8J8lFxgqr4yhXQmm3yg)

Le **dossier Train** contient toutes les images pour votre étape d'entraînement.

Le **dossier Test** contient toutes les images pour la soumission.

Le **fichier CSV Train** contient les données d'entraînement ; mappant le nom de l'image avec la colonne has_cactus qui donne une valeur de 1 si elle a un cactus ou 0 sinon.

Le **fichier CSV Sample Submission** contient tout le formatage pour la soumission que vous devez faire. Les noms de fichiers indiqués là sont égaux à tous les fichiers à l'intérieur du dossier Test.

```
train_df = pd.read_csv("train.csv")
```

Chargez le fichier CSV Train dans un data frame.

```
data_folder = Path(".") train_images = ImageList.from_df(train_df, path=data_folder, folder='train')
```

Créez un générateur de chargement en utilisant la méthode **ImageList from_df** pour mapper le data frame train_df avec les images à l'intérieur du dossier train.

### Augmentation des Données

Ceci est une technique pour **créer plus de données à partir de vos données existantes**. Une image de chat retournée verticalement est toujours un chat. En faisant cela, vous pouvez essentiellement multiplier votre ensemble de données par deux, quatre fois, ou même seize fois.

Vous aurez besoin de cette technique si vous avez très peu de données à travailler.

```
transformations = get_transforms(do_flip=True, flip_vert=True, max_rotate=10.0, max_zoom=1.1, max_lighting=0.2, max_warp=0.2, p_affine=0.75, p_lighting=0.75)
```

FastAI vous donne une méthode de transformation pour faire tout cela, appelée **get_transform**. Vous pouvez faire un retournement vertical, horizontal, une rotation, un zoom, ajouter de la lumière/brillance, et déformer l'image.

Vous pouvez jouer avec les paramètres que j'ai indiqués ci-dessus pour voir comment cela va ressembler. Ou vous pouvez [ouvrir la documentation](https://docs.fast.ai/vision.transform.html) et la lire en détail.

Bien sûr, appliquez la transformation à votre liste d'images :

```
train_img = train_img.transform(transformations, size=128)
```

Le paramètre size sera utilisé pour redimensionner l'entrée pour correspondre au réseau de neurones que vous allez utiliser. Le réseau que je vais utiliser s'appelle **DenseNet**, qui a remporté le prix du meilleur article à ImageNet 2017, et il a besoin d'images de 128×128 pixels.

### Préparation à l'Entraînement

Après avoir chargé vos données, vous devez vous préparer et préparer vos données pour la phase la plus importante de l'Apprentissage Profond appelée Entraînement. **En gros, c'est l'Apprentissage dans l'Apprentissage Profond**. Il apprend à partir de vos données et se met à jour en conséquence afin qu'il ait de bonnes performances sur vos données.

```
test_df = pd.read_csv("sample_submission.csv") test_img = ImageList.from_df(test_df, path=data_folder, folder='test')
```

```
train_img = train_img           .split_by_rand_pct(0.01)           .label_from_df()           .add_test(test_img)           .databunch(path='.', bs=64, device=torch.device('cuda:0'))                       .normalize(imagenet_stats)
```

Pour l'étape d'entraînement, vous devez diviser une partie de vos données d'entraînement en une petite portion appelée **données de validation**. Vous ne pouvez pas toucher ces données car elles seront votre outil de validation. **Lorsque votre Réseau de Neurones Convolutifs performe bien sur les données de validation, il performera probablement bien sur les données de test** qui seront soumises.

FastAI a la méthode pratique appelée **split_by_rand_pct** pour diviser une portion de vos données en données de validation.

Il a également la méthode **databunch** pour effectuer un traitement par lots. J'ai utilisé 64 comme taille de lot car c'est ce que limite mon GPU. Si vous n'avez pas de GPU, omettez le paramètre **device**.

Ensuite, la méthode **normalize** est appelée pour normaliser vos images car vous allez utiliser un réseau pré-entraîné. **imagenet_stats** normalisera les images selon la manière dont le réseau pré-entraîné a été entraîné pour la compétition ImageNet.

Ajouter les données de test à la liste d'images d'entraînement facilite la prédiction ultérieure sans plus de prétraitement. N'oubliez pas, ces images ne seront pas entraînées et n'iront pas dans votre validation. Vous voulez simplement prétraiter les données de la même manière que les images d'entraînement.

```
learn = cnn_learner(train_img, models.densenet161, metrics=[error_rate, accuracy])
```

Vous avez terminé la préparation de vos données d'entraînement. Maintenant, créez une méthode d'entraînement avec **cnn_learner**. Comme je l'ai dit avant, j'utiliserai DenseNet comme réseau pré-entraîné. Vous pouvez utiliser un autre réseau offert dans [TorchVision](https://pytorch.org/docs/stable/torchvision/models.html).

### La Technique One-Cycle

Vous pouvez commencer votre entraînement maintenant. Mais, il y a toujours une confusion lors de l'entraînement de tout Réseau de Neurones Profonds, y compris les Réseaux de Neurones Convolutifs. C'est **choisir le bon taux d'apprentissage**. L'algorithme est appelé Descente de Gradient, et il essaiera de diminuer l'erreur définie avec un paramètre appelé taux d'apprentissage.

![Image](https://cdn-media-1.freecodecamp.org/images/c1KIT8wg1bopl2bJ8tEXgTE-a37PwRBJFNrF)

**Un taux d'apprentissage plus grand rend les étapes d'entraînement plus rapides**, mais il est sujet à dépasser les limites. Cela rend possible pour l'erreur de sortir de contrôle comme dans l'image ci-dessus. Alors qu'**un taux d'apprentissage plus petit rend les étapes d'entraînement plus lentes**, mais il ne sortira pas de contrôle.

Donc, choisir le bon taux d'apprentissage est vraiment important. Rendez-le suffisamment grand sans sortir de contrôle.

C'est plus facile à dire qu'à faire.

Alors, une personne appelée Leslie Smith a créé une technique appelée [1-cycle policy](https://sgugger.github.io/the-1cycle-policy.html).

Intuitivement, vous pourriez vouloir trouver / forcer plusieurs taux d'apprentissage et **en trouver un avec une erreur presque minimale mais ayant de l'espace pour s'améliorer**. Essayons-le dans notre code.

```
learn.lr_find() learn.recorder.plot()
```

Il imprimera quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/zw79NSmNj8dcbd0t3Ua5pBQFNsy6hzsiumVD)

Le minimum devrait être 10⁻¹. Donc, je pense que nous pouvons utiliser quelque chose de plus petit que cela mais pas trop petit. Peut-être **3 * 10⁻²** est un bon choix. Essayons-le !

```
lr = 3e-02 learn.fit_one_cycle(5, slice(lr))
```

Entraînez pendant plusieurs étapes (j'ai choisi 5, ni trop grand ni trop petit), et voyons le résultat.

![Image](https://cdn-media-1.freecodecamp.org/images/a2BKjtyc5jOPIkMlofT2QCrXdgYYtGGAJ4VX)

**Attendez, quoi ?**

Notre solution simple nous donne une précision de 100 % pour notre division de validation ! C'est en fait efficace. Et il ne faut que six minutes pour s'entraîner. Quelle chance ! **Dans la vie réelle, vous ferez plusieurs itérations juste pour découvrir quels algorithmes sont meilleurs que les autres.**

J'ai hâte de soumettre ! Haha. **Prédisons le dossier de test et soumettons le résultat.**

```
preds,_ = learn.get_preds(ds_type=DatasetType.Test) test_df.has_cactus = preds.numpy()[:, 0]
```

Parce que vous avez déjà mis les images de test dans la liste d'images d'entraînement, vous n'aurez pas besoin de prétraiter et de charger vos images de test.

```
test_df.to_csv('submission.csv', index=False)
```

Cette ligne créera un fichier CSV contenant les noms des images et une colonne has_cactus pour toutes les 4 000 images de test.

Lorsque j'ai essayé de soumettre, je me suis en fait rendu compte que vous devez soumettre le CSV via un noyau Kaggle. J'ai manqué cela.

![Image](https://cdn-media-1.freecodecamp.org/images/DFBYT7cE69bKw439uShdmeHBwnNN9QOq8GUS)
_Courtoisie de [Kaggle](https://www.kaggle.com/" rel="noopener" target="_blank" title=")_

Mais, heureusement, **le noyau est en fait le même que votre notebook Jupyter**. Vous pouvez simplement copier-coller toutes les choses que vous avez construites dans votre notebook et soumettre là-bas.

Et **BAM** !

![Image](https://cdn-media-1.freecodecamp.org/images/R34ss1jMs-UJUVNLeQE8-qOtHRrovBptiryf)

Bon sang ! J'obtiens 0,9999 pour le score public. C'est vraiment bien. Mais, bien sûr, je veux obtenir un score parfait si ma première tentative est comme ça.

Alors, j'ai fait quelques ajustements dans le réseau et une fois de plus, BAM !

![Image](https://cdn-media-1.freecodecamp.org/images/d8BptL2rdf6599N1MEmGnLfzxOgYkDsPwqKm)

J'ai réussi ! Vous pouvez aussi. Ce n'est en fait pas si difficile.

(En passant, ce classement a été pris le 13 avril, donc je pourrais avoir chuté dans le classement maintenant...)

### Ce que j'ai appris

Ce problème est facile. Donc, vous ne ferez face à aucun défi bizarre en le résolvant. Cela en fait l'un des projets les plus adaptés pour commencer.

Hélas, parce que beaucoup de gens obtiennent un score parfait sur celui-ci, je pense que l'administrateur doit créer un autre ensemble de tests pour la soumission. Un plus difficile peut-être.

Quelle que soit la raison, il n'y a pas de barrière pour vous pour essayer cela. **Vous pouvez essayer cela maintenant et obtenir de bons résultats.**

![Image](https://cdn-media-1.freecodecamp.org/images/eFxKKzNLkMLki84lBbzy9zVUcyTI2lgjTDbA)
_Photo par [Unsplash](https://unsplash.com/photos/rGG-BCtNiuo?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Mario Mrad</a> sur <a href="https://unsplash.com/search/photos/vision?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Réflexions finales

Les Réseaux de Neurones Convolutifs sont si utiles pour diverses tâches. De la reconnaissance d'images à la génération d'images. Analyser des images de nos jours n'est pas aussi difficile qu'avant. Bien sûr, vous pouvez aussi le faire si vous essayez.

Commencez simplement, choisissez un bon projet de Réseau de Neurones Convolutifs et obtenez de bonnes données.

Bonne chance !

_Cet article est initialement publié sur mon blog à [thedatamage](https://thedatamage.com/convolutional-neural-network-explained/).