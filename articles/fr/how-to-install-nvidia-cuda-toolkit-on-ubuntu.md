---
title: Comment installer le NVIDIA CUDA Toolkit sur Ubuntu
subtitle: ''
author: Abraham Dahunsi
co_authors: []
series: null
date: '2024-01-29T21:25:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-nvidia-cuda-toolkit-on-ubuntu
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Feature-image.png
tags:
- name: Linux
  slug: linux
- name: Ubuntu
  slug: ubuntu
seo_title: Comment installer le NVIDIA CUDA Toolkit sur Ubuntu
seo_desc: 'The NVIDIA Compute Unified Device Architecture (CUDA) Toolkit is a software
  platform that allows developers to tap into the computing power of NVIDIA processing
  and GPU-accelerated applications.

  CUDA is also a programming model and an API that enable...'
---

Le NVIDIA Compute Unified Device Architecture (CUDA) Toolkit est une plateforme logicielle qui permet aux développeurs d'exploiter la puissance de calcul des processeurs NVIDIA et des applications accélérées par GPU.

CUDA est également un modèle de programmation et une API qui permettent aux programmeurs d'écrire du code pouvant s'exécuter à la fois sur le CPU et le GPU, tout en gérant le transfert de données entre eux.

En utilisant le CUDA Toolkit, vous pouvez améliorer les performances, la scalabilité et l'efficacité dans une gamme d'applications. Cela inclut le calcul, l'apprentissage profond, la vision par ordinateur, le gaming, et plus encore.

Le toolkit prend en charge les langages de programmation tels que C, C++, Fortran, Python et Java. Il s'intègre parfaitement avec des frameworks et des bibliothèques tels que TensorFlow, PyTorch, OpenCV et cuDNN.

De plus, l'utilisation du CUDA Toolkit s'étend à différents domaines, tels que la santé, la finance, la robotique, l'industrie automobile et le divertissement. Si vous cherchez à accélérer le traitement d'images ou le traitement du langage naturel, à améliorer la cryptographie ou à faire progresser les techniques de lancer de rayons, le CUDA Toolkit vous permet de résoudre les problèmes plus rapidement et plus efficacement.

En termes de compatibilité, le CUDA Toolkit offre un support pour les distributions Linux, y compris Ubuntu, Debian, Fedora, CentOS et OpenSUSE.

Dans cet article, je vais vous guider à travers le processus d'installation du CUDA Toolkit sur Ubuntu 22.04, qui est la version LTS (Long Term Support) d'Ubuntu.

## Prérequis

Pour installer le CUDA Toolkit sur Ubuntu 22.04, vous avez besoin des éléments suivants :

* [Un GPU NVIDIA pris en charge avec une capacité de calcul minimale de 3.0](https://developer.nvidia.com/cuda-gpus)

* [Un pilote NVIDIA compatible avec la version du CUDA Toolkit](https://docs.nvidia.com/deploy/cuda-compatibility/)

Dans ce guide, j'utiliserai une [instance GPU Paperspace](https://docs.paperspace.com/core/compute/machine-types) avec le système d'exploitation Ubuntu 22.04 LTS.

Veuillez noter que vous pouvez utiliser tout autre fournisseur de services cloud, comme Google Cloud et Vultr, ou même votre propre ordinateur, tant qu'il répond aux exigences listées ci-dessus.

Pour commencer, vous devrez créer un nouvel utilisateur, comme `seconduser`, puis basculer vers le nouvel utilisateur.

## Installer le CUDA Toolkit

Vous pouvez installer CUDA en utilisant le fichier de version ou alternativement, en utilisant Conda. Dans ce guide, nous installerons CUDA avec le fichier de version depuis l'archive officielle du Toolkit.

### Étape 1 : Télécharger le fichier de version de CUDA.

```bash
 $ wget https://developer.download.nvidia.com/compute/cuda/12.0.1/local_installers/cuda_12.0.1_525.85.12_linux.run
```

### Étape 2 : Exécuter le fichier de version.

```bash
 $ sudo sh cuda_12.0.1_525.85.12_linux.run
```

Vous serez invité à accepter le Contrat de Licence Utilisateur Final, puis appuyez sur `Entrée` pour configurer votre installation.

Une fois l'installation terminée, vous devriez voir une sortie similaire à celle-ci :

![carbon--6-](https://www.freecodecamp.org/news/content/images/2024/01/carbon--6-.png align="left")

## Configuration et Vérification

### Étape 1 : Configurer le serveur

Configurez le serveur pour qu'il fonctionne avec le CUDA toolkit. Déplacez le chemin CUDA vers le `PATH` du système, puis ajoutez le chemin de la bibliothèque CUDA Toolkit au `LD_LIBRARY_PATH` afin que le chargeur de liens du toolkit CUDA soit mis à jour avec l'emplacement des bibliothèques partagées.

```bash
  $ echo "export PATH=/usr/local/cuda-12.0/bin${PATH:+:${PATH}}" >> /home/seconduser/.bashrc
```

```bash
  $ echo "export LD_LIBRARY_PATH=/usr/local/cuda-12.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}" >> /home/seconduser/.bashrc
```

### Étape 2 : Activer l'environnement

Après avoir configuré le serveur pour qu'il fonctionne avec le CUDA toolkit, activez les modifications des variables d'environnement afin que le système puisse trouver et utiliser CUDA.

```bash
$ source /home/seconduser/.bashrc
```

### Étape 3 : Vérifier l'installation

```bash
 $ nvidia-smi
```

Sortie :

![carbon--7-](https://www.freecodecamp.org/news/content/images/2024/01/carbon--7-.png align="left")

### Étape 4 : Vérifier l'installation du package.

Vérifiez que le package du CUDA Toolkit est installé avec succès sur votre serveur.

```bash
 $ nvcc --version
```

Sortie :

![carbon--8-](https://www.freecodecamp.org/news/content/images/2024/01/carbon--8-.png align="left")

## Test

Pour tester vos programmes CUDA nouvellement installés, vous utiliserez des scripts de test déjà prêts par CUDA qui vous permettront de vérifier de manière exhaustive la compatibilité et la fonctionnalité de votre environnement CUDA.

### Étape 1 : Cloner le dépôt des scripts de test

```bash
 $ git clone https://github.com/NVIDIA/cuda-samples.git
```

### Étape 2 : Aller dans le répertoire contenant le script d'exemple deviceQuery.

```bash
 $ cd cuda-samples/Samples/1_Utilities/deviceQuery
```

### Étape 3 : Compiler le script.

```bash
 $ make
```

### Étape 4 : Exécuter le script.

```bash
 $ ./deviceQuery
```

Votre sortie devrait ressembler à celle ci-dessous si votre programme CUDA a exécuté le script avec succès :

![carbon--9-](https://www.freecodecamp.org/news/content/images/2024/01/carbon--9-.png align="left")

## Conclusion

Dans cet article, vous avez appris comment installer le CUDA Toolkit sur Ubuntu 22.04.

Voici quelques bonnes pratiques pour utiliser CUDA sur Ubuntu :

* Gardez votre système et vos pilotes NVIDIA à jour pour assurer la compatibilité et la stabilité du CUDA Toolkit.

* Utilisez le CUDA APT PPA pour installer et mettre à jour le CUDA Toolkit facilement et rapidement.

* Utilisez les options et les flags du compilateur nvcc pour optimiser et déboguer votre code CUDA.

* Utilisez les bibliothèques et les outils CUDA pour améliorer et simplifier votre processus de développement CUDA.

* Suivez les normes de codage CUDA et les bonnes pratiques pour écrire un code CUDA efficace et maintenable.

Voici quelques ressources pour en apprendre davantage sur CUDA :

* [Documentation officielle de CUDA](https://docs.nvidia.com/cuda/)

* [Tutoriel de révision CUDA](https://riptutorial.com/cuda/example/13338/compiling-and-running-the-sample-programs)

* [Lire les Docs : Dire Bonjour à CUDA](https://cuda-tutorial.readthedocs.io/en/latest/tutorials/tutorial01/)