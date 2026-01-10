---
title: Comment configurer CUDA et WSL2 pour Windows 11 (incluant PyTorch et TensorFlow
  GPU)
author: Md. Fahim Bin Amin
date: '2025-12-03T20:20:46.460Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-cuda-and-wsl2-for-windows-11-including-pytorch-and-tensorflow-gpu
description: 'If you’re working on complex Machine Learning projects, you’ll need
  a good Graphics Processing Unit (or GPU) to power everything. And Nvidia is a popular
  option these days, as it has great compatibility and widespread support.

  If you’re new to Machin...'
subtitle: ''
seo_title: Comment configurer CUDA et WSL2 pour Windows 11 (incluant PyTorch et TensorFlow
  GPU)
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1764786287487/f0c28401-ce77-4873-b238-59fc6b737ce7.png
tags:
- name: Machine Learning
  slug: machine-learning
- name: Windows
  slug: windows
- name: WSL
  slug: wsl
- name: GPU
  slug: gpu
- name: cuda
  slug: cuda
- name: Python
  slug: python
- name: Deep Learning
  slug: deep-learning
seo_desc: 'If you’re working on complex Machine Learning projects, you’ll need a good
  Graphics Processing Unit (or GPU) to power everything. And Nvidia is a popular option
  these days, as it has great compatibility and widespread support.

  If you’re new to Machin...'
---


Si vous travaillez sur des projets complexes de Machine Learning, vous aurez besoin d'un bon processeur graphique (ou GPU) pour tout alimenter. Et Nvidia est une option populaire de nos jours, car elle offre une excellente compatibilité et un support étendu.

Si vous débutez en Machine Learning, un compte gratuit sur [Kaggle](https://www.kaggle.com/) ou [Colab](https://colab.research.google.com/) pourrait vous suffire. Mais ce ne sera plus le cas lorsque vous voudrez aller plus loin. Vous aurez besoin d'un GPU, ce qui peut devenir coûteux si vous l'utilisez continuellement sur le cloud.

Mais il y a une bonne nouvelle : vous pouvez utiliser le GPU Nvidia de votre ordinateur (GTX/RTX) assez facilement et effectuer des tâches liées au machine learning directement sur votre machine locale. Ce qui est génial, c'est que cela ne vous coûtera rien d'autre que l'électricité consommée !

Lorsque vous exécutez des modèles de Machine Learning sur vos machines locales, le système d'exploitation le plus approprié est un système basé sur Linux, comme Ubuntu. Mais Windows s'est beaucoup amélioré à cet effet. Si vous utilisez le dernier Windows 11, vous pouvez exploiter le Sous-système Windows pour Linux (WSL) et utiliser votre GPU directement pour les flux de travail liés au Machine Learning.

Ce processus peut cependant être assez délicat, tout comme le fait de rendre deux Frameworks de Machine Learning populaires, TensorFlow et PyTorch, compatibles avec le GPU de votre système sous Windows 11. C'est pourquoi j'ai écrit ce guide complet pour vous faciliter la tâche.

Dans ce guide, je vais vous aider à configurer CUDA sur le Sous-système Windows pour Linux 2 (WSL2) afin que vous puissiez exploiter votre GPU Nvidia pour des tâches de machine learning.

En suivant ces étapes, vous serez en mesure d'exécuter des Frameworks de ML comme TensorFlow et PyTorch avec l'accélération GPU sur Windows 11.

Gardez à l'esprit que ce guide suppose que vous possédez un GPU Nvidia compatible. Assurez-vous de consulter la [liste officielle de compatibilité de Nvidia](https://developer.nvidia.com/cuda-gpus) avant de continuer.

J'ai également préparé une vidéo pour vous aider à suivre les directives appropriées tout au long de cet article.

%[https://youtu.be/qOJ49nkU4rY] 

De plus, si ce tutoriel vous aide, n'oubliez pas d'ajouter une étoile au dépôt GitHub [CUDA-WSL2-Ubuntu-v2](https://github.com/FahimFBA/CUDA-WSL2-Ubuntu-v2). Si vous rencontrez des problèmes ou si vous avez des suggestions/améliorations, n'hésitez pas à ouvrir un ticket (issue) dans le dépôt GitHub. Actuellement, le site web en direct est disponible sur [ml-win11-v2.fahimbinamin.com](https://ml-win11-v2.fahimbinamin.com/).

## Table des matières

1. [Prérequis](#heading-prérequis)
    
2. [Windows Terminal](#heading-windows-terminal)
    
3. [Windows PowerShell (Le plus récent et le meilleur)](#heading-windows-powershell-le-plus-récent-et-le-meilleur)
    
4. [Configurer Windows Terminal](#heading-configurer-windows-terminal)
    
5. [Configuration de mon ordinateur](#heading-configuration-de-mon-ordinateur)
    
6. [Virtualisation du processeur](#heading-virtualisation-du-processeur)
    
7. [Installer WSL2](#heading-installer-wsl2)
    
8. [Installer la dernière version LTS d'Ubuntu via WSL2](#heading-installer-la-dernière-version-lts-dubuntu-via-wsl2)
    
9. [Mettre à jour et mettre à niveau les paquets Ubuntu](#heading-mettre-à-jour-et-mettre-à-niveau-les-paquets-ubuntu)
    
10. [Installer et configurer Miniconda](#heading-installer-et-configurer-miniconda)
    
11. [Installer Jupyter & Ipykernel](#heading-installer-jupyter-et-ipykernel)
    
12. [Pilote Nvidia](#heading-pilote-nvidia)
    
13. [Installer les dépendances CUDA](#heading-installer-les-dépendances-cuda)
    
14. [CUDA Toolkit](#heading-cuda-toolkit)
    
15. [Ajouter le chemin au profil du shell pour CUDA](#heading-ajouter-le-chemin-au-profil-du-shell-pour-cuda)
    
16. [Version de nvcc](#heading-version-de-nvcc)
    
17. [SDK cuDNN](#heading-sdk-cudnn)
    
18. [TensorFlow GPU](#heading-tensorflow-gpu)
    
    * [Vérifier TensorFlow GPU](#heading-vérifier-tensorflow-gpu)
        
19. [PyTorch GPU](#heading-pytorch-gpu)
    
    * [Vérifier PyTorch GPU](#heading-vérifier-pytorch-gpu)
        
    * [Vérifier PyTorch & TensorFlow GPU dans Jupyter Notebook](#heading-vérifier-pytorch-et-tensorflow-gpu-dans-jupyter-notebook)
        
20. [Conclusion](#heading-conclusion)
    

## Prérequis

Avant de commencer, assurez-vous de remplir les conditions suivantes :

* Système d'exploitation Windows 11
    
* GPU Nvidia (série GTX/RTX)
    
* Accès administrateur à votre PC
    
* Au moins 30 Go d'espace disque libre
    
* Connexion Internet pour les téléchargements
    
* Derniers pilotes Nvidia installés
    

## Windows Terminal

Tout d'abord, vous devez vous assurer que Windows Terminal est correctement installé sur votre système d'exploitation. C'est la toute nouvelle application de terminal pour les utilisateurs d'outils en ligne de commande et de shells comme l'Invite de commande, PowerShell et WSL. Vous pouvez le télécharger sur le [Microsoft Store](https://apps.microsoft.com/detail/9N0DX20HK701?hl=en-us&gl=BD&ocid=pdpshare).

![Aperçu de Windows Terminal sur Windows 11](https://cdn.hashnode.com/res/hashnode/image/upload/v1764094104150/c73ae561-6888-4eea-9419-186c6659a62f.png align="center")

Après vous être assuré qu'il est correctement installé, vous pouvez passer aux étapes suivantes.

## Windows PowerShell (Le plus récent et le meilleur)

Windows PowerShell est un shell de ligne de commande moderne et mis à jour de Microsoft. Vous pouvez y utiliser directement certaines commandes spécifiques à Linux. Il est doté de suggestions de commandes intégrées. Vous pouvez le télécharger sur la [page officielle GitHub](https://github.com/PowerShell/PowerShell/releases/).

![Aperçu de Windows PowerShell sur GitHub](https://cdn.hashnode.com/res/hashnode/image/upload/v1764094138179/78315197-f4f2-4df4-b022-37cb9e74cda2.png align="center")

Téléchargez le dernier programme d'installation x64 et installez-le. Après vous être assuré qu'il est correctement installé, vous pouvez passer aux étapes suivantes.

## Configurer Windows Terminal

Vous devez maintenant configurer votre Windows Terminal pour utiliser PowerShell comme shell par défaut. C'est facultatif et vous pouvez ignorer cette étape, mais je vous recommande de le faire pour une meilleure expérience.

Ouvrez Windows Terminal. Cliquez sur l'icône de flèche vers le bas dans la barre de titre et sélectionnez "Paramètres".

![Aperçu de la fenêtre des paramètres de Windows PowerShell](https://cdn.hashnode.com/res/hashnode/image/upload/v1764094162440/6ea767c8-da3b-4280-84f8-0eb2b0647a46.png align="center")

Dans l'onglet Paramètres, sous "Démarrage", trouvez le menu déroulant "Profil par défaut". Sélectionnez "PowerShell" dans la liste.

Maintenant, pour "Application de terminal par défaut", sélectionnez "Windows Terminal".

Par défaut, Windows PowerShell affiche toujours le numéro de version dans la barre de titre. Si vous souhaitez le désactiver, sélectionnez le profil "PowerShell" dans la barre latérale gauche. Cliquez sur le champ "Ligne de commande" et ajoutez un argument `--nologo` à la fin de la commande. Après cela, la ligne devient `"C:\Program Files\PowerShell\7\pwsh.exe" --nologo`.

![Aperçu du paramètre --nologo de Windows PowerShell](https://cdn.hashnode.com/res/hashnode/image/upload/v1764094185648/3641d5f0-ba34-44b9-8a63-86b53068d02e.png align="center")

Si vous n'utilisez pas fréquemment d'autres shells et que vous souhaitez les masquer dans la liste déroulante, vous devrez sélectionner ces profils un par un dans la barre latérale gauche. Faites défiler vers le bas et activez l'option "Masquer le profil de la liste déroulante". Cela masquera ce shell spécifique du menu déroulant.

Par exemple, je masque le profil **Azure Cloud Shell** car je ne l'utilise pas fréquemment :

![Aperçu du masquage des profils dans Windows Terminal](https://cdn.hashnode.com/res/hashnode/image/upload/v1764094214632/73add1b7-bcdd-4368-86a6-975fa2f72b54.png align="center")

Cliquez maintenant sur le bouton "Enregistrer" en bas à droite pour appliquer les modifications. Fermez Windows Terminal pour le moment.

## Configuration de mon ordinateur

J'ai pensé qu'il serait utile de partager la configuration actuelle de mon ordinateur afin que vous ayez une idée claire de l'installation que j'utilise dans ce guide. Voici les détails :

| **Composant** | **Spécification** |
| --- | --- |
| **Processeur** | AMD Ryzen 7 7700 8-Core Processor (8 cœurs 16 threads) |
| **RAM** | 64 Go DDR5 6000MHz |
| **Stockage** | SSD NVMe Samsung 980 de 1 To, HDD de 4 To, SSD SATA de 2 To |
| **GPU** | NVIDIA GeForce RTX 3060 12 Go GDDR6 |
| **Système d'exploitation** | Windows 11 Pro Version 25H2 |

Maintenant que vous avez une idée de la configuration de mon ordinateur, nous pouvons passer aux étapes suivantes.

## Virtualisation du processeur

Comme nous allons utiliser WSL2, nous devons nous assurer que la virtualisation du processeur est activée. Pour vérifier si la virtualisation est activée ou non depuis Windows, ouvrez simplement le Gestionnaire des tâches de Windows. Allez dans l'onglet Performance et sélectionnez CPU dans la barre latérale gauche. Dans le coin inférieur droit, vous verrez l'état de la virtualisation. S'il affiche "Activé", vous pouvez continuer. S'il affiche "Désactivé", vous devez l'activer dans le BIOS.

![Aperçu de l'état activé de la virtualisation dans le Gestionnaire des tâches de Windows](https://cdn.hashnode.com/res/hashnode/image/upload/v1764094252181/29efa40c-ec0a-4d99-adb7-50596348a1aa.png align="center")

⚠️ Vous devez vous assurer que la virtualisation du processeur est activée dans les paramètres de votre BIOS. Différents fabricants ont différentes manières d'accéder au BIOS. Généralement, vous pouvez y accéder en appuyant sur la touche Suppr ou F2 pendant le processus de démarrage. Une fois dans le BIOS, recherchez les paramètres liés à "Virtualization Technology" ou "Intel VT-x"/"AMD-V" et assurez-vous qu'ils sont activés. Enregistrez les modifications et quittez le BIOS.

## Installer WSL2

Ouvrez Windows Terminal ou Windows PowerShell en tant qu'administrateur. Exécutez la commande suivante pour installer WSL2 ainsi que la dernière distribution Ubuntu LTS :

```powershell
wsl.exe --install
```

Cela installera le Sous-système Windows pour Linux 2 (WSL2). Une fois l'installation terminée, vous serez invité à redémarrer votre ordinateur. Faites-le pour finaliser l'installation.

![Aperçu de l'installation de WSL dans Windows PowerShell](https://cdn.hashnode.com/res/hashnode/image/upload/v1764094306994/41db30c0-ecb9-4436-a425-8a059b199c42.png align="center")

⚠️ Si vous rencontrez des problèmes lors de l'installation, reportez-vous à la [documentation officielle de Microsoft](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting) pour le dépannage des problèmes d'installation de WSL.

## Installer la dernière version LTS d'Ubuntu via WSL2

Ouvrez à nouveau Windows Terminal ou Windows PowerShell avec les privilèges d'administrateur. Si vous souhaitez vérifier les distributions Linux disponibles à l'installation via WSL, exécutez la commande suivante :

```powershell
wsl.exe --list --online
```

![Aperçu des distributions WSL disponibles dans Windows PowerShell](https://cdn.hashnode.com/res/hashnode/image/upload/v1764094455888/8f1f2382-41cc-410f-a7b9-a47d3bb634b6.png align="center")

Pour installer une distribution spécifique, exécutez la commande suivante :

```powershell
wsl.exe --install <DistroName>
```

Nous allons installer la dernière distribution Ubuntu LTS. À l'heure actuelle, la dernière version LTS est Ubuntu 24.04. Mais je préfère installer `Ubuntu` directement car cela pointe toujours vers la dernière version LTS. Exécutez donc la commande suivante :

```powershell
wsl.exe --install Ubuntu
```

Vous devez lui donner un nom de compte utilisateur par défaut. Pour ma part, je choisis `fahim`.

![Aperçu de l'installation d'Ubuntu dans Windows PowerShell](https://cdn.hashnode.com/res/hashnode/image/upload/v1764094505280/9beb24de-54da-4e0c-993d-b15f985867e3.png align="center")

Il est également livré avec un bel outil de gestion GUI pour WSL.

![Aperçu de l'outil de gestion GUI de WSL](https://cdn.hashnode.com/res/hashnode/image/upload/v1764094530944/89073fb9-881f-48bd-b5ef-a0b08f74e4c5.png align="center")

Vous pouvez y configurer beaucoup de choses, notamment la restriction des cœurs, de la RAM, de l'espace disque et de nombreuses spécifications à partir de la fenêtre des paramètres GUI.

![Aperçu de la fenêtre des paramètres GUI de WSL (Mémoire & Processeur)](https://cdn.hashnode.com/res/hashnode/image/upload/v1764094551095/66aea1e1-e204-4115-80e0-b3dea2d7a2ac.png align="center")

## Mettre à jour et mettre à niveau les paquets Ubuntu

Ouvrez votre terminal Ubuntu depuis Windows Terminal. Tout d'abord, nous devons mettre à jour et mettre à niveau les paquets existants vers leurs dernières versions.

Pour mettre à jour le système Ubuntu, utilisez simplement la commande suivante :

```bash
sudo apt update -y
```

![Aperçu de la commande apt update dans le terminal Ubuntu](https://cdn.hashnode.com/res/hashnode/image/upload/v1764094594281/be41e056-7e55-4139-b84b-6b7921a2d435.png align="center")

Pour mettre à niveau tous les paquets en même temps, utilisez simplement la commande suivante :

```bash
sudo apt upgrade -y
```

![Aperçu de la commande apt upgrade dans le terminal Ubuntu](https://cdn.hashnode.com/res/hashnode/image/upload/v1764094627958/b1c17b1c-5290-470b-aafe-5b89bb03bd01.png align="center")

⚠️ Assurez-vous d'avoir une connexion Internet stable pendant le processus de mise à jour et de mise à niveau pour éviter toute interruption.

## Installer et configurer Miniconda

En Machine Learning, nous devons gérer plusieurs environnements avec différentes versions de paquets. Conda est un système de gestion de paquets et d'environnements populaire qui facilite la création et la gestion d'environnements isolés pour différents projets. Nous allons installer Miniconda, un installeur minimal pour Conda, pour gérer nos environnements Python. Mais si vous préférez Anaconda, vous pouvez l'installer à la place.

Allez sur le site officiel de Miniconda. Actuellement, l'installeur Miniconda se trouve dans Anaconda [ici](https://www.anaconda.com/docs/getting-started/miniconda/install). Si le site officiel est mis à jour, vous pouvez toujours rechercher "Miniconda installer" sur Google pour trouver la dernière version. De plus, vous pouvez créer un ticket dans le [dépôt GitHub officiel de ce projet](https://github.com/FahimFBA/CUDA-WSL2-Ubuntu-v2/issues) pour m'en informer.

![Aperçu du site officiel de Miniconda](https://cdn.hashnode.com/res/hashnode/image/upload/v1764094667031/7ee2c854-88b6-49ce-8c04-41bf0a052c90.png align="center")

Comme nous l'installons à l'intérieur de WSL, nous devons sélectionner l'installation macOS/Linux. Sélectionnez ensuite Linux Terminal Installer et choisissez Linux x86 pour télécharger l'installeur.

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

Cela téléchargera l'installeur dans votre répertoire WSL. Utilisez ensuite la commande suivante pour l'installer correctement :

```bash
bash ~/Miniconda3-latest-Linux-x86_64.sh
```

⚠️ Assurez-vous d'être dans le bon répertoire où l'installeur a été téléchargé. Si vous l'avez téléchargé dans un autre emplacement, ajustez le chemin en conséquence. Remplacez également bash par zsh ou sh si vous utilisez un shell différent.

![Aperçu de l'installation de Miniconda dans le terminal WSL Ubuntu](https://cdn.hashnode.com/res/hashnode/image/upload/v1764094706995/3a317eb9-0340-4a84-8826-45324c93dd2f.png align="center")

Assurez-vous de choisir correctement l'option d'initialisation. Je préfère garder l'environnement conda actif chaque fois que j'ouvre un nouveau shell. Par conséquent, j'ai choisi "Yes".

![Aperçu de l'option d'initialisation de Miniconda pendant l'installation](https://cdn.hashnode.com/res/hashnode/image/upload/v1764094727839/f3fc8902-0c37-432c-a912-a92810e89fd1.png align="center")

Assurez-vous que l'installation réussit sans aucune erreur.

![Aperçu d'une installation réussie de Miniconda dans le terminal WSL Ubuntu](https://cdn.hashnode.com/res/hashnode/image/upload/v1764094754454/53dfd998-62c9-4c2a-a71e-0d33e123e027.png align="center")

Pour que les modifications prennent effet, vous pouvez fermer et rouvrir le shell actuel. Mais vous pouvez aussi le faire sans fermer le shell en appliquant la commande ci-dessous.

```bash
source ~/.bashrc
```

⚠️ Si vous utilisez un shell différent comme zsh ou fish, assurez-vous de sourcer le fichier de configuration approprié (par exemple, ~/.zshrc pour zsh).

## Installer Jupyter & Ipykernel

Je préfère utiliser Jupyter Notebook pour exécuter mes expériences de machine learning. Il offre un environnement interactif pour le codage et l'analyse de données. Nous allons installer Jupyter Notebook et Ipykernel pour exécuter des notebooks Jupyter dans notre environnement conda. Nous ferons cela dans tous les environnements conda en commençant par l'environnement **base**. Cela nous aide également à conserver le noyau de l'environnement conda à l'intérieur de Jupyter Notebook.

Tout d'abord, assurez-vous d'être dans l'environnement conda base. Vous verrez (base) sur le côté gauche du terminal.

![Aperçu de l'environnement conda base dans le terminal WSL Ubuntu](https://cdn.hashnode.com/res/hashnode/image/upload/v1764094812122/66ad5de8-7553-42da-b920-78d20c3bdc9a.png align="center")

Installez maintenant Jupyter et Ipykernel en appliquant la commande suivante :

```bash
conda install jupyter ipykernel -y
```

Assurez-vous d'accepter les conditions d'utilisation de Conda.

![Aperçu de l'installation de Jupyter et Ipykernel dans le terminal WSL Ubuntu](https://cdn.hashnode.com/res/hashnode/image/upload/v1764094839808/90fe3dcf-053d-4bc7-a031-22f81eb706ca.png align="center")

Maintenant, je vais créer un environnement conda séparé pour TensorFlow et PyTorch GPU. Vous pouvez les installer directement dans l'environnement base ou dans tout autre environnement selon votre préférence. Je ne spécifie aucune version particulière de Python lors de la création de l'environnement. Il installera automatiquement la dernière version stable de Python.

```bash
conda create -name ml -y
```

![Aperçu de la création d'un nouvel environnement conda nommé 'ml' dans le terminal WSL Ubuntu](https://cdn.hashnode.com/res/hashnode/image/upload/v1764094865498/ac9ef1f1-4494-4221-8376-5e257c4f9243.png align="center")

Pour activer un environnement conda spécifique, vous devez utiliser la commande suivante :

```bash
conda activate <conda-env-name>
```

Par exemple, si je veux activer mon environnement **ml** nouvellement créé, j'utiliserai cette commande :

```bash
conda activate ml
```

Si vous n'êtes pas sûr des environnements conda installés sur votre système, vous pouvez vérifier tous les environnements conda disponibles et installés en exécutant la commande suivante :

```bash
conda env list
```

## Pilote Nvidia

Assurez-vous d'avoir les derniers pilotes Nvidia installés sur Windows. WSL2 utilise le pilote Windows, donc aucune installation de pilote séparée n'est nécessaire dans Ubuntu. Vous pouvez télécharger les derniers pilotes sur le [site officiel de Nvidia](https://www.nvidia.com/Download/index.aspx).

![Aperçu de la page de téléchargement des pilotes Nvidia](https://cdn.hashnode.com/res/hashnode/image/upload/v1764094915617/cd9b0bfc-77a1-45f1-9dab-4349c8f489ef.png align="center")

Si vous venez d'installer le dernier pilote GPU, redémarrez votre ordinateur après l'installation pour vous assurer que les modifications prennent effet. Vous pouvez utiliser soit le pilote GeForce Game Ready, soit le pilote NVIDIA Studio. Je recommande d'utiliser le pilote Studio pour une meilleure stabilité avec les applications créatives et de ML.

## Installer les dépendances CUDA

Vous pourriez rencontrer des problèmes si les dépendances CUDA ne sont pas correctement installées. Je vous recommande d'installer les dépendances requises avant de continuer :

```bash
sudo apt install gcc g++ build-essential
```

Après avoir installé les dépendances, vous pourrez vérifier l'installation de CUDA si vous avez eu des problèmes précédemment.

## CUDA Toolkit

TensorFlow GPU est très exigeant concernant la version de CUDA. Nous devons donc installer une version spécifique du CUDA Toolkit qui est compatible avec la version de TensorFlow que nous allons installer.

Pour comprendre exactement quelle version de CUDA est compatible avec quelle version de TensorFlow, vous pouvez consulter la matrice de support officielle de TensorFlow GPU [ici](https://www.tensorflow.org/install/pip).

![Aperçu du support TensorFlow GPU dans la documentation officielle](https://cdn.hashnode.com/res/hashnode/image/upload/v1764095089103/87a44961-9426-4d20-95ac-cde06961b41a.png align="center")

Au moment où j'écris cet article, la documentation de TensorFlow GPU indique que nous devrions avoir le CUDA Toolkit 12.3. Je vais donc m'assurer d'installer exactement cette version. Vous pouvez simplement cliquer sur le lien de cette version dans la documentation officielle et cela vous redirigera vers la page de téléchargement officielle du CUDA Toolkit de Nvidia. Si le lien est mis à jour à l'avenir, vous pouvez toujours rechercher "Nvidia CUDA Toolkit" sur Google pour trouver la dernière version.

![Aperçu du site officiel de Nvidia CUDA Toolkit](https://cdn.hashnode.com/res/hashnode/image/upload/v1764095106589/19689d63-5ebd-4783-8da4-e3dedd277efb.png align="center")

Comme TensorFlow GPU demande précisément la version 12.3, je vais sélectionner exactement la version 12.3.0.

Sur la page de téléchargement du CUDA Toolkit, assurez-vous de choisir le système d'exploitation Linux, l'architecture x86\_64, la distribution WSL-Ubuntu, la version 2.0 et le type d'installeur runfile(local).

⚠️ Comme nous utilisons Ubuntu dans notre WSL2, vous pouvez également choisir Ubuntu comme système d'exploitation. Mais je préfère choisir WSL-Ubuntu pour une meilleure compatibilité.

![Aperçu de la page de téléchargement de CUDA Toolkit 12.3 pour WSL-Ubuntu](https://cdn.hashnode.com/res/hashnode/image/upload/v1764095151533/b6996611-d4ce-4e07-9c73-30bdc93dbf19.png align="center")

Après avoir sélectionné ces options, vous obtiendrez les commandes de téléchargement. Vous devez les appliquer séquentiellement. Assurez-vous de **ne pas cocher "Kernel Objects" pendant l'installation de CUDA**.

![Aperçu des commandes de téléchargement de CUDA Toolkit 12.3 pour WSL-Ubuntu](https://cdn.hashnode.com/res/hashnode/image/upload/v1764095169368/c2f81594-536f-4788-b765-1aab3b040fa7.png align="center")

⚠️ Veillez à copier et coller les commandes une par une dans votre terminal WSL Ubuntu pour télécharger et installer correctement le CUDA Toolkit. Si vous rencontrez des problèmes liés aux dépendances CUDA, consultez rapidement la section [Installer les dépendances CUDA](#heading-installer-les-dépendances-cuda), où j'ai expliqué comment installer correctement les dépendances CUDA.

## Ajouter le chemin au profil du shell pour CUDA

Après avoir installé le CUDA Toolkit, nous devons ajouter les binaires CUDA à notre profil de shell pour un accès facile. Cela nous permettra d'exécuter des commandes CUDA depuis n'importe quel répertoire du terminal.

Notez que, selon le shell que vous utilisez (bash, zsh, etc.), vous devez ajouter le chemin CUDA au fichier de configuration approprié. Assurez-vous de remplacer **.bashrc** par **.zshrc** ou d'autres fichiers de configuration si vous utilisez un shell différent.

Pour ajouter le chemin des binaires CUDA, suivez la commande ci-dessous :

```bash
echo 'export PATH=/usr/local/cuda-12.3/bin:$PATH' >> ~/.bashrc
```

Vous devez utiliser le chemin mis à jour où vous l'avez installé. Votre terminal l'affichera après l'installation de CUDA :

![Aperçu du chemin d'installation de CUDA dans le terminal WSL Ubuntu](https://cdn.hashnode.com/res/hashnode/image/upload/v1764095215437/15768563-c956-472e-9633-95b3dd1cb7a3.png align="center")

Maintenant, vous devez ajouter le chemin à l'intérieur du chemin de la bibliothèque (Library path). Utilisez simplement le chemin exact où vous avez installé CUDA. Votre terminal listera le chemin correctement.

```bash
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-12.3/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
```

![Aperçu du chemin de la bibliothèque CUDA dans le terminal WSL Ubuntu](https://cdn.hashnode.com/res/hashnode/image/upload/v1764095242744/3c708db4-d267-4043-aa11-d04d890904f9.png align="center")

Après avoir ajouté ces chemins, vous devez sourcer le profil du shell pour que les modifications prennent effet. Vous pouvez le faire en exécutant la commande suivante :

```bash
source ~/.bashrc
```

## Version de nvcc

NVCC signifie Nvidia CUDA Compiler. C'est essentiellement un pilote de compilateur pour la plateforme CUDA qui permet aux développeurs d'écrire des programmes parallèles s'exécutant sur les GPU Nvidia. Comme nous avons déjà installé le toolkit CUDA, nous devons voir si le compilateur est également correctement activé. Pour vérifier cela, nous devons vérifier la version.

Vérifiez que CUDA est correctement installé en consultant la version :

```bash
nvcc --version
```

![Aperçu de la vérification de la version de nvcc dans le terminal WSL Ubuntu](https://cdn.hashnode.com/res/hashnode/image/upload/v1764095277858/2d1ded0a-01ac-4f78-9f6c-ac499d623207.png align="center")

Si la sortie affiche la bonne version de CUDA, alors vous avez installé avec succès le CUDA Toolkit dans votre environnement WSL2 Ubuntu.

## SDK cuDNN

Le SDK cuDNN (CUDA Deep Neural Network) est une [bibliothèque de primitives accélérée par GPU pour les réseaux de neurones profonds](https://developer.nvidia.com/cudnn), développée par Nvidia. Il fournit des blocs de construction hautement optimisés pour les opérations courantes de deep learning, accélérant considérablement les processus d'entraînement et d'inférence des modèles d'IA sur les GPU Nvidia.

Note : Même si TensorFlow GPU suggère une version spécifique de cuDNN, il est souvent compatible avec plusieurs versions. Pour cette raison, je recommande de télécharger la dernière version de cuDNN compatible avec votre version installée de CUDA. Vous pouvez trouver la page de téléchargement de cuDNN [ici](https://developer.nvidia.com/cudnn-downloads).

Sélectionnez le système d'exploitation Linux, l'architecture x86\_64, la distribution Ubuntu, la version 24.04, le type d'installeur deb (local), la configuration FULL. Après avoir sélectionné ces options, vous obtiendrez les commandes de téléchargement. Vous devez les appliquer séquentiellement.

![Aperçu des commandes de téléchargement de cuDNN pour Ubuntu 24.04](https://cdn.hashnode.com/res/hashnode/image/upload/v1764095312370/1fca5959-f492-4160-8027-deec0674863b.png align="center")

⚠️ Veillez à copier et coller les commandes une par une dans votre terminal WSL Ubuntu pour télécharger et installer correctement le SDK cuDNN. Si vous rencontrez des problèmes liés aux dépendances CUDA, consultez rapidement la section [Installer les dépendances CUDA](#heading-installer-les-dépendances-cuda), où j'ai expliqué comment installer correctement les dépendances CUDA.

## TensorFlow GPU

Maintenant, nous allons installer TensorFlow GPU dans notre environnement conda. Assurez-vous d'avoir activé l'environnement conda où vous souhaitez l'installer. Je vais l'installer dans mon environnement **ml** précédemment créé. Pour l'activer, j'utiliserai la commande suivante :

```bash
conda activate ml
```

⚠️ Assurez-vous d'avoir activé le bon environnement conda avant d'installer TensorFlow GPU. Vous verrez le nom de l'environnement dans l'invite du terminal.

![Aperçu de l'activation de l'environnement conda 'ml' dans le terminal WSL Ubuntu](https://cdn.hashnode.com/res/hashnode/image/upload/v1764095398777/0c7d8813-eb6c-4e2e-bad9-1fc7d344d7a2.png align="center")

J'installerai ipykernel et jupyter dans ce nouvel environnement.

```bash
conda install jupyter ipykernel -y
```

Maintenant, pour installer TensorFlow GPU, j'utiliserai simplement la commande suivante :

```bash
pip install tensorflow[and-cuda]
```

Cela peut prendre quelques minutes selon votre vitesse de connexion Internet. Soyez patient et attendez la fin de l'installation.

### Vérifier TensorFlow GPU

Après avoir installé TensorFlow GPU, nous devons vérifier qu'il fonctionne correctement avec le support GPU. Ouvrez un shell Python dans votre terminal Ubuntu et exécutez les commandes suivantes :

```bash
python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```

Si la sortie affiche une liste de périphériques GPU disponibles, alors TensorFlow GPU est installé avec succès et fonctionne correctement.

![Aperçu de la vérification de TensorFlow GPU dans le terminal WSL Ubuntu](https://cdn.hashnode.com/res/hashnode/image/upload/v1764095453933/ccda58fc-9ae9-4185-9c78-6196c98d8b7c.png align="left")

## PyTorch GPU

Maintenant, nous allons installer PyTorch GPU dans notre environnement conda. Assurez-vous d'avoir activé l'environnement conda où vous souhaitez l'installer. Je vais l'installer dans mon environnement ml précédemment créé. Pour l'activer, j'utiliserai la commande suivante :

```bash
conda activate ml
```

L'installation de PyTorch GPU est très simple. Vous pouvez utiliser le générateur de commandes d'installation officiel de PyTorch [ici](https://pytorch.org/get-started/locally/).

Assurez-vous de sélectionner PyTorch Build comme la dernière version Stable, votre OS comme Linux, le Package comme Pip, le Language comme Python. Pour la Compute Platform, sélectionnez la version CUDA qui correspond à votre CUDA Toolkit installé. Pour moi, c'est CUDA 12.3. Mais si vous ne trouvez pas la version exacte, choisissez la plus proche. Comme CUDA 12.3 n'est pas disponible pour moi actuellement, je choisis CUDA 12.6.

Après avoir sélectionné ces options, vous obtiendrez la commande d'installation. Vous devez l'appliquer dans votre terminal WSL Ubuntu.

![Aperçu du générateur de commandes d'installation de PyTorch](https://cdn.hashnode.com/res/hashnode/image/upload/v1764095511862/6f631369-c8db-4681-9d1c-669ad88df69d.png align="center")

Cela peut prendre quelques minutes selon votre vitesse de connexion Internet. Soyez patient et attendez la fin de l'installation.

![Aperçu de l'installation de PyTorch GPU dans le terminal WSL Ubuntu](https://cdn.hashnode.com/res/hashnode/image/upload/v1764095532246/56232263-36ea-4043-9881-df162965c514.png align="center")

### Vérifier PyTorch GPU

Après avoir installé PyTorch GPU, vérifiez qu'il fonctionne correctement avec le support GPU. Ouvrez un shell Python dans votre terminal Ubuntu et exécutez les commandes suivantes :

```bash
python3 - << 'EOF'
import torch
print(torch.cuda.is_available())
print(torch.cuda.device_count())
print(torch.cuda.current_device())
print(torch.cuda.device(0))
print(torch.cuda.get_device_name(0))
EOF
```

La sortie devrait ressembler à la capture d'écran, affichant :

* **True** : Le GPU est disponible pour PyTorch
    
* **1** : Nombre de périphériques CUDA détectés
    
* **0** : Index du périphérique CUDA actif actuel
    
* Une représentation de l'objet périphérique
    
* **NVIDIA GeForce RTX 3060** (ou le nom de votre GPU)
    

![Aperçu de la vérification de PyTorch GPU dans le terminal WSL Ubuntu](https://cdn.hashnode.com/res/hashnode/image/upload/v1764095584921/69269152-7ea6-404b-b1ca-8534b51f2491.png align="center")

### Vérifier PyTorch & TensorFlow GPU dans Jupyter Notebook

Maintenant que l'environnement est entièrement configuré, nous allons vérifier le support GPU directement dans Jupyter Notebook. Cela garantit que PyTorch et TensorFlow peuvent tous deux détecter et utiliser votre GPU avec succès.

#### 1\. Tester PyTorch GPU

Créez un nouveau Jupyter Notebook et exécutez les commandes suivantes une par une :

```python
import torch

print(torch.cuda.is_available())
print(torch.cuda.device_count())
print(torch.cuda.current_device())
print(torch.cuda.device(0))
print(torch.cuda.get_device_name(0))
```

Si tout est configuré correctement, vous verrez votre GPU (par exemple **NVIDIA GeForce RTX 3060**) correctement détecté :

![Aperçu de la vérification de PyTorch GPU dans Jupyter Notebook](https://cdn.hashnode.com/res/hashnode/image/upload/v1764095624229/f94c97a0-2e44-45ad-a2a8-52f40c922482.png align="center")

#### 2\. Tester TensorFlow GPU

Ensuite, exécutez le code suivant pour vérifier si TensorFlow détecte votre GPU :

```python
import tensorflow as tf

print(tf.config.list_physical_devices('GPU'))
```

Vous pouvez également vérifier le nombre de GPU détectés :

```python
print("Num GPUs Available:", len(tf.config.list_physical_devices('GPU')))
```

Enfin, exécutez la validation GPU intégrée de TensorFlow (les avertissements sont normaux) :

```python
import tensorflow as tf

assert tf.test.is_gpu_available()
assert tf.test.is_built_with_cuda()
```

![Initialisation de TensorFlow GPU et sortie de validation CUDA](https://cdn.hashnode.com/res/hashnode/image/upload/v1764095666216/f9017979-b5c9-4b86-9f60-d9aaa2fe8ac1.png align="center")

Si les journaux de TensorFlow affichent votre modèle de GPU (tel que **RTX 3060**), alors TensorFlow GPU est installé avec succès et fonctionne pleinement dans Jupyter Notebook.

## Conclusion

Merci beaucoup d'avoir lu jusqu'au bout. J'espère que vous avez pu configurer correctement votre ordinateur sous Windows 11 pour exécuter presque tout type d'expériences basées sur le Machine Learning.

Pour obtenir plus de contenu comme celui-ci, vous pouvez me suivre sur [LinkedIn](https://www.linkedin.com/in/fahimfba/) et [X](https://x.com/Fahim_FBA). Vous pouvez également consulter [mon site web](https://www.fahimbinamin.com/) et me suivre sur [GitHub](https://github.com/FahimFBA) si vous vous intéressez à l'open source et au développement.