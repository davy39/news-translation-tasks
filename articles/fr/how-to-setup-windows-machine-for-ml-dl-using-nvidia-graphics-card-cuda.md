---
title: Comment configurer une machine Windows pour le Machine Learning/Deep Learning
  en utilisant une carte graphique Nvidia (CUDA)
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2023-05-30T14:58:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-windows-machine-for-ml-dl-using-nvidia-graphics-card-cuda
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/arseny-togulev-MECKPoKJYjM-unsplash.jpg
tags:
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: Windows
  slug: windows
- name: WSL
  slug: wsl
seo_title: Comment configurer une machine Windows pour le Machine Learning/Deep Learning
  en utilisant une carte graphique Nvidia (CUDA)
seo_desc: "If you are learning machine learning / deep learning, you may be using\
  \ the free Google Colab. But you might wonder if the free version is adequate. \n\
  If you can afford a good Nvidia Graphics Card (with a decent amount of CUDA cores)\
  \ then you can easil..."
---

Si vous apprenez le machine learning ou le deep learning, vous utilisez peut-être [Google Colab](https://colab.research.google.com/) gratuitement. Mais vous vous demandez peut-être si la version gratuite est adéquate. 

Si vous pouvez vous offrir une bonne carte graphique Nvidia (avec un nombre décent de cœurs CUDA), alors vous pouvez facilement utiliser votre carte graphique pour ce type de travail intensif. 

Beaucoup de développeurs utilisent Linux pour cela. Mais je n'aime pas Linux en tant que système d'exploitation de bureau (ne vous offusquez pas, c'est ma préférence personnelle. Et oui, Linux est le meilleur pour tout ce qui concerne les serveurs). 

De plus, si vous possédez la dernière GPU Nvidia, vous êtes probablement déjà familier avec les tracas concernant le pilote graphique, etc.

Pour toutes ces raisons, je pensais essayer quelque chose de différent : utiliser le nouveau système d'exploitation Windows 11 pour exploiter les cœurs CUDA de ma carte graphique. 

J'ai suivi beaucoup de vidéos mais je n'ai pas réussi à l'implémenter après plusieurs tentatives, malheureusement. Il y avait un problème de compatibilité entre la dernière version de PyTorch et le noyau Windows 11 dans CUDA. Cependant, après beaucoup de recherches, j'ai découvert que WSL2 devrait fonctionner parfaitement.

Après avoir essayé pendant plus de quelques jours, j'ai réussi à configurer tout ce qui est nécessaire et je peux utiliser les cœurs CUDA de ma carte graphique sur ma machine Windows ! Une chose intéressante est que, dans ce processus, vous n'avez pas besoin de télécharger ou d'utiliser Microsoft Visual Studio 2022 et de télécharger d'énormes fichiers de 30/35 Go juste pour installer les compilateurs recommandés, etc.

Pour cette raison, j'ai écrit un manuel complet sur mon GitHub (voici le dépôt : [CUDA-WSL2-Ubuntu](https://github.com/FahimFBA/CUDA-WSL2-Ubuntu), et voici le site web : [fahimfba.github.io/CUDA-WSL2-Ubuntu](https://fahimfba.github.io/CUDA-WSL2-Ubuntu)).

J'écris également le même manuel ici. Alors, c'est parti ! 🎉

## Spécifications de mon ordinateur

Pour ce guide, j'ai utilisé ma station de travail de bureau. Si vous êtes également intéressé par les spécifications actuelles que j'ai utilisées pour cette tâche, les voici :

* Processeur : Ryzen 5 3500X 6 cœurs et 6 threads
* RAM : 32 Go DDR4 3200 MHz (16 Go + 8 Go + 8 Go)
* GPU : Zotac Nvidia GeForce RTX 3050 8 Go GDDR6
* Carte mère : Gigabyte B450M Aorus Elite
* Stockage : Gigabyte 240 Go SSD SATA
* Moniteur : MSI Optix G24 Gaming Curved 75Hz

J'utiliserai Windows 11 Pro (Version 22H2) et WSL2 (bien sûr !).

## Étape 1 : Assurez-vous d'avoir une connexion Internet et une alimentation électrique stables

Ce processus peut prendre beaucoup de temps. Assurez-vous donc d'être correctement connecté à Internet et d'avoir une alimentation électrique stable. Pour moi, cela a pris presque 7 heures au total. Vous devrez également télécharger certains packages assez volumineux en cours de route. 

Assurez-vous également d'avoir installé le dernier pilote Nvidia après avoir téléchargé le pilote officiel depuis [le site officiel de Nvidia](https://www.nvidia.com/download/index.aspx). Assurez-vous d'avoir installé toutes les mises à jour de votre Windows 11.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/win_update.png)
_mise à jour de Windows_

## Étape 2 : Télécharger la dernière version de PowerShell

J'utiliserai la dernière version de PowerShell. Vous pouvez la télécharger depuis le Microsoft Store, mais je la téléchargerai depuis le site officiel car le store peut créer des problèmes plus tard. 

Allez sur [le site officiel](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows). Cela vous redirige normalement vers la dernière version de PowerShell disponible à ce moment-là. Pour moi, la dernière version est 7.3 (24 mai 2023). Pour vous, cela peut être une version mise à jour. Ne vous inquiétez pas pour cela. Téléchargez simplement la dernière version stable.

1. Cliquez sur le bouton **Download PowerShell**.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/1-1.png)
_Bouton de téléchargement de PowerShell_

2.  Trouvez la dernière version de PowerShell pour `win-x64.msi`. Téléchargez celle-ci.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/2-3.png)
_fichier msi de la dernière version de PowerShell_

3.  Le processus d'installation est assez simple. Mais je vais vous guider tout au long du processus. Double-cliquez sur le fichier téléchargé. Ensuite, cliquez sur `Suivant`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/3-2.png)
_logiciel msi_

4.  Gardez tout tel quel et cliquez sur `Suivant`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/4-3.png)
_Étape suivante_

5.  Je préfère toujours garder tout tel quel et cliquer simplement sur `Suivant`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/5-4.png)
_Étape suivante_

6.  Je préfère toujours garder tout tel quel et cliquer simplement sur `Suivant`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/6-1.png)
_Étape suivante_

7.  Cliquez sur `Installer`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/7-2.png)
_Installer_

8.  Maintenant, cliquez sur `Terminer`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/8-3.png)
_Terminer_

## Étape 3 : Vérifiez votre terminal Windows

J'aime vraiment le terminal Windows, car je peux simplement basculer vers n'importe quel autre système d'exploitation WSL (Ubuntu, Kali, Git Bash, etc.) quand je veux. Mais avant de continuer, je dois m'assurer que mon terminal Windows actuel est à jour.

1. Ouvrez le **Microsoft Store** et recherchez `Windows Terminal`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/9-2.png)
_Terminal Windows sur Microsoft Store_

2.  Cliquez sur `Mettre à jour` si une mise à jour est nécessaire.

3.  Assurez-vous que vous êtes déjà sur la dernière version mise à jour du terminal Windows.

4.  Maintenant, ouvrez le terminal Windows, car nous devons d'abord changer certains paramètres. Cliquez sur `Ouvrir les paramètres`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/10-2.png)
_Personnalisation des paramètres du terminal Windows_

5.  Si vous ne voyez pas l'invite `Ouvrir les paramètres`, cliquez simplement sur la flèche déroulante, puis sur `Paramètres`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/11-2.png)
_Paramètres_

6.  Dans `Démarrage`, assurez-vous que le **profil par défaut** est défini sur `PowerShell` (le nouveau PowerShell que nous avons installé à l'étape 2). L'**application de terminal par défaut** doit être définie sur `Terminal Windows`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/12-1.png)
_Configuration de démarrage par défaut_

7.  Ensuite, cliquez sur `Enregistrer` et quittez le terminal.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/13-2.png)
_Enregistrer_

## Étape 4 : Virtualisation matérielle

Pour utiliser WSL, nous devons nous assurer que la virtualisation de notre CPU est activée. Vous pouvez vérifier l'état via le gestionnaire de tâches. Si elle est désactivée, assurez-vous d'activer la virtualisation via le BIOS. 

Vous trouverez beaucoup de vidéos YouTube à ce sujet, mais assurez-vous de suivre celle qui correspond à la marque et au modèle de votre carte mère.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/14-2.png)
_Virtualisation_

## Étape 5 : Installer WSL et Ubuntu LTS

Maintenant, nous devons installer WSL2 et Ubuntu LTS.

1. Ouvrez le terminal Windows en tant qu'**administrateur**.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/15-2.png)
_Ouvrir le terminal en tant qu'administrateur_

2.  Pour installer **WSL**, utilisez la commande `wsl --install`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/16-3.png)
_Installation de VMP_

3.  Ensuite, il installera automatiquement la dernière version LTS d'Ubuntu.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/18-2.png)
_Installation d'Ubuntu_

4.  Après la fin des tâches, il vous demandera de redémarrer votre PC. Enregistrez votre travail et redémarrez simplement votre ordinateur.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/19-3.png)
_Redémarrer le PC_

5.  Après avoir redémarré le PC, il ouvrira automatiquement le terminal et vous demandera le nom d'utilisateur et le mot de passe pour votre système d'exploitation Linux.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/20-1.png)
_Après avoir redémarré le PC_

6.  Donnez le nom d'utilisateur et le mot de passe. Assurez-vous d'utiliser le même mot de passe dans le champ Retaper le mot de passe !

![Image](https://www.freecodecamp.org/news/content/images/2023/05/21-1.png)
_nom d'utilisateur et mot de passe_

7.  Après un certain temps, il installera les composants nécessaires.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/22-1.png)
_Ubuntu complet_

8.  Maintenant, assurez-vous que **WSL2** devient le WSL par défaut dans ce terminal. Appliquez la commande `wsl --set-default-version 2`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/23-1.png)
_WSL 2 par défaut_

9.  Si vous souhaitez vérifier l'état des systèmes d'exploitation WSL (combien de systèmes d'exploitation sont disponibles, combien sont en cours d'exécution ou arrêtés), utilisez la commande `wsl --list --verbose`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/24-1.png)
_État des systèmes d'exploitation_

Ici, il m'indique que j'ai **Ubuntu** installé sur ma version WSL 2 et qu'il est actuellement arrêté.

10.  Cependant, après avoir travaillé sur un système d'exploitation WSL, si vous souhaitez l'éteindre, vous pouvez utiliser la commande `wsl -t nom_distro`. Pour moi, c'est Ubuntu, donc j'ai utilisé `wsl -t Ubuntu`. `t` représente la commande de **terminaison** ici.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/25-2.png)
_Commande de terminaison_

11.  Si vous avez plusieurs systèmes d'exploitation dans WSL et que vous souhaitez exécuter une distribution spécifique, utilisez la commande `wsl --distribution nom_distribution`. Par exemple, si je veux exécuter spécifiquement Ubuntu, la commande serait `wsl --distribution Ubuntu`. Si vous n'avez qu'une seule distribution, vous n'avez pas nécessairement besoin de vous en soucier.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/26-1.png)
_exécuter une distribution spécifique_

12.  Vous pouvez simplement utiliser `exit` pour quitter une distribution depuis le terminal. Cela n'éteint pas nécessairement la distribution. Vous pouvez utiliser spécifiquement la commande de terminaison pour cela. Mais voici quelques commandes couramment utilisées.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/27-1.png)
_commande couramment utilisée_

13.  Après avoir installé une distribution, vous pourrez également la voir et y accéder en utilisant le menu déroulant du terminal Windows.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/28-1.png)
_le menu déroulant pour les autres distributions_

## Étape 6 : Configurer Ubuntu LTS

Nous devons maintenant mettre à jour et installer quelques applications.

1. Ouvrez Ubuntu en utilisant n'importe quelle méthode dans le terminal Windows. Vous pouvez évidemment utiliser l'application dédiée **Ubuntu**. Mais je préfère toujours le terminal car je peux utiliser plusieurs distributions différentes et applications en ligne de commande ici.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/29.png)
_démarrer Ubuntu_

2.  Mettez à jour le système en utilisant la commande `sudo apt update`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/30.png)
_mise à jour_

3.  Si vous obtenez des erreurs lors de la mise à jour/mise à niveau indiquant qu'il ne peut pas atteindre le serveur, changez le serveur de noms avec la commande `echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf > /dev/null`.

4.  Après la mise à jour, mettez à niveau le système en utilisant `sudo apt upgrade`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/31.png)
_Mise à niveau_

![Image](https://www.freecodecamp.org/news/content/images/2023/05/32.png)
_Mise à niveau du système_

Vous pouvez effacer le terminal en utilisant la commande `clear`.

5.  CUDA fonctionne avec C. Nous devons donc installer le compilateur gcc en premier. Utilisez la commande `sudo apt install gcc --fix-missing`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/33.png)
_gcc_

![Image](https://www.freecodecamp.org/news/content/images/2023/05/34.png)
_installation de gcc_

![Image](https://www.freecodecamp.org/news/content/images/2023/05/35.png)
_fin de l'installation_

## Étape 7 : Installer CUDA

Il est maintenant temps d'installer CUDA depuis [le site officiel de Nvidia](https://developer.nvidia.com/cuda-downloads).

Assurez-vous de sélectionner les éléments suivants :

* **Système d'exploitation** : Linux <br>
* **Architecture** : x86_64 <br>
* **Distribution** : WSL-Ubuntu <br>
* **Version** : 2.0 <br>
* **Type d'installateur** : deb(local) <br> 

![Image](https://www.freecodecamp.org/news/content/images/2023/05/36.png)
_Nvidia - CUDA_

Cela fournira les commandes nécessaires.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/37.png)
_commandes CUDA_

Votre tâche consiste maintenant à appliquer chaque commande en série dans le terminal Ubuntu WSL. Assurez-vous d'utiliser la première commande deux fois. Cela résout normalement le problème de keyring plus tard.

Gardez également à l'esprit que ces commandes peuvent changer plus tard. Suivez donc toujours le site officiel. Pour ce guide, j'utiliserai la commande exacte que j'ai utilisée pour configurer CUDA sur ma machine.

1. `wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin`

![Image](https://www.freecodecamp.org/news/content/images/2023/05/38.png)
_1ère commande_

J'ai utilisé la même commande à nouveau après avoir terminé les transactions précédentes.

2.  `wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin`

![Image](https://www.freecodecamp.org/news/content/images/2023/05/39.png)
_1ère commande_

3.  `sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600`

![Image](https://www.freecodecamp.org/news/content/images/2023/05/40.png)
_2ème commande_

4.  `wget https://developer.download.nvidia.com/compute/cuda/12.1.1/local_installers/cuda-repo-wsl-ubuntu-12-1-local_12.1.1-1_amd64.deb`

![Image](https://www.freecodecamp.org/news/content/images/2023/05/41.png)
_3ème commande_

Cela prend normalement beaucoup de temps car il télécharge un gros fichier (taille de fichier supérieure à 2 Go).

![Image](https://www.freecodecamp.org/news/content/images/2023/05/42.png)
_gros fichier_

5.  `sudo dpkg -i cuda-repo-wsl-ubuntu-12-1-local_12.1.1-1_amd64.deb`

![Image](https://www.freecodecamp.org/news/content/images/2023/05/43.png)
_4ème commande_

6.  `sudo cp /var/cuda-repo-wsl-ubuntu-12-1-local/cuda-*-keyring.gpg /usr/share/keyrings/`

![Image](https://www.freecodecamp.org/news/content/images/2023/05/44.png)
_5ème commande_

7.  Ensuite, mettez à jour le système en utilisant `sudo apt-get update`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/45.png)
_mise à jour du système_

![Image](https://www.freecodecamp.org/news/content/images/2023/05/46.png)
_mise à jour_

8.  `sudo apt-get -y install cuda`

![Image](https://www.freecodecamp.org/news/content/images/2023/05/47.png)
_installation de CUDA_

![Image](https://www.freecodecamp.org/news/content/images/2023/05/48.png)
_fin de l'installation de CUDA_

## Étape 8 : Post-installation

Le [guide d'installation officiel de CUDA de Nvidia](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html) nous indique d'ajouter `export PATH=/usr/local/cuda-12.1/bin${PATH:+:${PATH}}` à la variable **PATH**.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/49.png)
_chemin_

J'ai changé la version de CUDA `cuda-12.1` selon la version de CUDA installée. Assurez-vous de faire de même pour votre version mise à jour de CUDA.

Faites ce qui suit pour cela :

1. Ouvrez Ubuntu dans le terminal Windows.
2. Allez dans le répertoire racine en utilisant `cd ~`. Ensuite, ouvrez le `bashrc` dans nano en utilisant `nano .bashrc`

![Image](https://www.freecodecamp.org/news/content/images/2023/05/50.png)
_racine_

3.  Allez à la fin du fichier et copiez-collez le chemin là. Pour moi, le chemin est `export PATH=/usr/local/cuda-12.1/bin${PATH:+:${PATH}}`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/51.png)
_chemin_

Ensuite, utilisez `Ctrl` + `X` pour fermer. Assurez-vous d'utiliser `Y` pour enregistrer dans le même fichier.

4.  Pour appliquer les changements, utilisez `source ~/.bashrc`. Vous pouvez vérifier le chemin en utilisant `echo $PATH`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/52.png)
_vérification du chemin_

## Étape 9 : Nvidia CUDA Toolkit

Installez le Nvidia Cuda Toolkit en utilisant `sudo apt install nvidia-cuda-toolkit`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/53.png)
_toolkit 1_

![Image](https://www.freecodecamp.org/news/content/images/2023/05/54.png)
_toolkit 2_

Vous pouvez vérifier les versions du pilote et de CUDA en utilisant `nvidia-smi`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/55.png)
_smi_

Assurez-vous également de vérifier si le pilote du compilateur Nvidia Cuda a été installé ou non en utilisant `nvcc -V`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/56.png)
_nvcc_

## Étape 9 : Confirmez que Python est installé

Maintenant, assurez-vous que Python 3 est installé sur votre système. Vous pouvez vérifier la version en utilisant `python3 --version`. Si cela indique que "python3 est introuvable" ou quelque chose de similaire, installez Python.

Installez **PIP** en utilisant `sudo apt-get install python3-pip`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/57.png)
_installation de pip_

## Étape 10 : Installer PyTorch

Pour installer PyTorch, allez sur [le site officiel de PyTorch](https://pytorch.org/get-started/locally/). Ensuite, assurez-vous de sélectionner les sections pertinentes. Après cela, il vous fournira une commande. Vous devez utiliser la commande dans votre terminal Ubuntu.

Pour moi, les sélections étaient :

* Version de PyTorch : Stable (2.0.1) - Assurez-vous de toujours sélectionner la dernière version stable
* Votre OS : Linux
* Package : Pip
* Langage : Python
* Plateforme informatique : CUDA 11.8 - Assurez-vous de sélectionner la dernière version disponible de CUDA

Après cela, j'ai obtenu la commande `pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/58.png)
_commande PyTorch_

J'ai simplement utilisé cette commande exacte dans mon terminal Ubuntu.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/59.png)
_commande PyTorch_

Il télécharge également un gros fichier qui peut prendre beaucoup de temps si vous avez une connexion Internet plus lente comme moi !

![Image](https://www.freecodecamp.org/news/content/images/2023/05/60.png)
_téléchargement de PyTorch_

## Étape 11 : Disponibilité de CUDA

Vous pouvez vérifier directement si CUDA a été installé ou non en exécutant deux lignes de code Python dans le terminal.

* Exécutez Python dans le terminal en utilisant `python3`.
* Importez torch en utilisant `import torch`.
* Vérifiez la disponibilité de CUDA en utilisant `torch.cuda.is_available()`.

Si cela retourne `True`, alors vous avez réussi à installer CUDA sur votre système !

![Image](https://www.freecodecamp.org/news/content/images/2023/05/61.png)
_cuda oui_

## Étape 12 : Paramètres du développeur Nvidia

Vous devez activer les paramètres du développeur Nvidia pour utiliser CUDA via WSL. Suivez simplement ce processus :

1. Ouvrez le **Panneau de configuration Nvidia**.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/62.png)
_panneau de configuration Nvidia_

2.  Cliquez sur "Accepter et continuer".

![Image](https://www.freecodecamp.org/news/content/images/2023/05/63.png)
_accepter_

3.  Dans le Panneau de configuration Nvidia, cliquez sur Bureau > Activer les paramètres du développeur. Si "Activer les paramètres du développeur" n'a pas de coche, cliquez dessus pour activer cette fonctionnalité.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/64.png)
_pas de coche_

![Image](https://www.freecodecamp.org/news/content/images/2023/05/65.png)
_coche_

4.  La section **Développeur** sera visible. Cliquez sur **Gérer les compteurs de performance du GPU**.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/66.png)
_compteurs GPU_

5.  Cochez le bouton radio sur "Autoriser l'accès aux compteurs de performance du GPU à tous les utilisateurs".

![Image](https://www.freecodecamp.org/news/content/images/2023/05/67.png)
_coche_

6.  Cliquez sur "Appliquer" et "Oui" pour approuver les changements de manière permanente.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/68.png)
_approuver les changements_

7.  À la fin, cela devrait ressembler à ceci. 

![Image](https://www.freecodecamp.org/news/content/images/2023/05/69.png)
_final_

8.  Vous pouvez à nouveau vérifier la disponibilité de CUDA comme précédemment.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/70.png)
_disponibilité de CUDA_

## Étape 12 : Installer Jupyter Notebook

Je préfère généralement Jupyter Notebook. Vous pouvez l'installer de diverses manières, comme `pip install notebook`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/71.png)
_notebook 1_

![Image](https://www.freecodecamp.org/news/content/images/2023/05/72.png)
_notebook 2_

Mais je préfère la commande `pip install jupyter notebook`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/73.png)
_jupyter notebook_

Pour ouvrir un Jupyter Notebook, vous pouvez simplement utiliser `jupyter notebook` dans le terminal.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/74.png)
_notebook cli_

Le notebook s'ouvrira instantanément et vous pourrez utiliser l'URL donnée pour l'ouvrir dans votre navigateur web :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/75.png)
_ouvrir le notebook dans le navigateur_

## Étape 13 : Exécuter quelques tests

J'ai exécuté deux codes pour vérifier les performances de mon CUDA.

1. Ouvrez un script Python3 dans le notebook.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/76.png)
_ouvrir le script_

2.  J'ai utilisé le code suivant pour vérifier s'il utilise mon CPU ou CUDA de mon GPU :

```python
import torch

if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")
print("using", device, "device") 
```

![Image](https://www.freecodecamp.org/news/content/images/2023/05/77.png)
_cuda_

3.  Pour la comparaison de performance entre mon CPU et mon GPU (CUDA), j'ai utilisé le code suivant :

```python
import time

matrix_size = 32*512

x = torch.randn(matrix_size, matrix_size)
y = torch.randn(matrix_size, matrix_size)

print("************* VITESSE CPU *******************")
start = time.time()
result = torch.matmul(x, y)
print(time.time() - start)
print("vérifier l'appareil:", result.device)

x_gpu = x.to(device)
y_gpu = y.to(device)
torch.cuda.synchronize()

for i in range(3):
    print("************* VITESSE GPU *******************")
    start = time.time()
    result_gpu = torch.matmul(x_gpu, y_gpu)
    torch.cuda.synchronize()
    print(time.time() - start)
    print("vérifier l'appareil:", result_gpu.device)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/05/78.png)
_CPU vs GPU_

J'ai également fait des comparaisons côte à côte entre [Google Colab](https://colab.research.google.com/) et mon ordinateur. Vous pouvez les vérifier également.

| Essai | Google Colab                                                                               | Mon ordinateur                                                                               |
| --- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| 1   | [Google Colab](https://github.com/FahimFBA/CUDA-WSL2-Ubuntu/blob/main/GoogleCollab1.ipynb) | [Mon PC](https://github.com/FahimFBA/CUDA-WSL2-Ubuntu/blob/main/CUDA%20_TEST_Fahim1.ipynb) |
| 2   | [Google Colab](https://github.com/FahimFBA/CUDA-WSL2-Ubuntu/blob/main/GoogleCollab2.ipynb) | [Mon PC](https://github.com/FahimFBA/CUDA-WSL2-Ubuntu/blob/main/CUDA%20_TEST_Fahim2.ipynb) |


Le résultat indique déjà que mon PC fonctionne mieux que Google Colab.

## Étape 14 : Supprimer le fichier CUDA Deb

Si vous pensez ne plus avoir besoin du fichier deb CUDA, vous pouvez le supprimer en utilisant la commande suivante :

```bash
rm filename
```

Pour moi, c'était ceci :

```bash
rm cuda-repo-wsl-ubuntu-12-1-local_12.1.1-1_amd64.deb
```

Cela ne supprime pas CUDA de votre système. Cela supprime simplement le fichier deb de votre système.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/79.png)
_supprimer deb_

## Conclusion

J'espère que vous avez réussi à installer CUDA sur votre système Windows 11 en utilisant WSL2. Si vous avez des questions, n'hésitez pas à me contacter via [Twitter](https://twitter.com/Fahim_FBA) ou [LinkedIn](https://www.linkedin.com/in/fahimfba/).

Assurez-vous également de me suivre sur [GitHub](https://github.com/FahimFBA) et de mettre une étoile (🔊) au [dépôt](https://github.com/FahimFBA/CUDA-WSL2-Ubuntu) !

Vous pouvez également [vous abonner à ma chaîne YouTube](https://www.youtube.com/@FahimAmin?sub_confirmation=1) pour plus de contenu vidéo utile.

Si vous êtes intéressé, vous pouvez également consulter mon site web : [https://fahimbinamin.com/](https://fahimbinamin.com/)

Merci d'avoir lu l'article entier jusqu'à présent. Passez une excellente journée ! 😊

Image de couverture : Photo de [Arseny Togulev](https://unsplash.com/@tetrakiss?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/photos/MECKPoKJYjM?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)