---
title: Perf Machine Learning sur Rasp Pi
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-09T15:39:06.000Z'
originalURL: https://freecodecamp.org/news/perf-machine-learning-on-rasp-pi-51101d03dba2
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca36a740569d1a4ca5b6c.jpg
tags:
- name: iot
  slug: iot
- name: Machine Learning
  slug: machine-learning
- name: Raspberry Pi
  slug: raspberry-pi
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Perf Machine Learning sur Rasp Pi
seo_desc: 'By Gant Laborde

  3 Frameworks for Machine Learning on the Raspberry Pi

  The revolution of AI is reaching new heights through new mediums. We’re all enjoying
  new tools on the edge, but what are they? What products frameworks will fuel the
  inventions of ...'
---

Par Gant Laborde

#### 3 Frameworks pour le Machine Learning sur le Raspberry Pi

La révolution de l'IA atteint de nouveaux sommets grâce à de nouveaux médias. Nous profitons tous de nouveaux outils en périphérie, mais quels sont-ils ? Quels frameworks de produits alimenteront les inventions de demain ?

Si vous n'êtes pas familier avec les raisons pour lesquelles le Machine Learning change nos vies, lisez [ici](https://medium.freecodecamp.org/machine-learning-how-to-go-from-zero-to-hero-40e26f8aa6da).

Si vous êtes déjà passionné par le Machine Learning et que vous êtes intéressé à l'utiliser sur des appareils comme le Raspberry Pi, profitez-en !

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ie5y0cU3BqZkIRRKPNQtmg.png)

### Détection d'objets simple sur le Raspberry Pi

J'ai implémenté trois outils différents pour la détection sur la caméra Pi. Bien que ce soit un miracle moderne que les trois fonctionnent, il est important pour les créateurs de savoir "à quel point" à cause de #perfmatters.

Nos trois concurrents sont les suivants :

1. [**Vanilla Raspberry Pi 3 B+**](https://www.raspberrypi.org/blog/raspberry-pi-3-model-bplus-sale-now-35/) — Aucune optimisation, mais simplement l'utilisation d'un framework TensorFlow sur l'appareil pour une reconnaissance simple.
2. [**Intel's Neural Compute Stick 2**](https://software.intel.com/en-us/neural-compute-stick) — Le dernier dispositif USB d'Intel pour les réseaux neuronaux, promettant 8x perf par rapport au premier bâton ! Environ 80 $ USD.
3. [**Xnor.ai**](https://www.xnor.ai) — Un framework propriétaire qui reconfigure votre modèle pour fonctionner efficacement sur du matériel plus petit. La logique binaire de Xnor réduit les flottants 32 bits à des opérations 1 bit, vous permettant d'optimiser les modèles de deep learning pour des appareils simples.

Évaluons les trois avec une détection d'objets simple sur une caméra !

![Image](https://cdn-media-1.freecodecamp.org/images/1*XCtxmYeXSc9hiResMDbXVA.png)

### Vanilla Raspberry Pi 3 B+

Un Raspberry Pi est comme une petite machine Linux faible pour 40 $. Il vous permet d'exécuter des applications et du code de haut niveau sur des appareils comme l'IoT rendu facile. Bien que cela semble signifier que je peux utiliser le machine learning de laptop sur l'appareil, il y a un gros piège. Le RPi a un [processeur ARM](https://whatis.techtarget.com/definition/ARM-processor), et cela signifie que nous devrons recompiler notre framework, c'est-à-dire TensorFlow, pour tout faire fonctionner.

> ⚠️ Bien que ce ne soit pas difficile, c'est LENT. Attendez-vous à ce que cela prenne un très... très... long moment. C'est pretty much le sort de tout ce qui est compilé sur le Raspberry Pi.

#### Installation

Voici toutes les étapes que j'ai suivies, y compris la configuration de la caméra Pi pour la détection d'objets. Je l'inclus simplement pour la postérité. N'hésitez pas à sauter la lecture.

Installez pi, puis la caméra, puis modifiez le fichier `/boot/config.txt`
Ajoutez `disable_camera_led=1` à la fin du fichier et redémarrez.

### Meilleur de désactiver le mode économiseur d'écran, car certaines commandes de suivi peuvent prendre des heures
```
sudo apt-get install xscreensaver
xscreensaver
```

Puis désactivez l'économiseur d'écran dans l'onglet "Mode d'affichage".
### Maintenant, obtenez Tensorflow installé
```
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get update
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev libqtgui4 python3-pyqt5
pip3 install tensorflow
sudo apt-get install libjpeg-dev zlib1g-dev libxml2-dev libxslt1-dev
pip3 install pillow jupyter matplotlib cython
pip3 install lxml # celui-ci prend beaucoup de temps
pip3 install python-tk
```

### OpenCV
```
sudo apt-get install libtiff5-dev libjasper-dev libpng12-dev
Sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt-get install qt4-dev-tools
pip3 install opencv-python
```

### Installer Protobuff
```
sudo apt-get install autoconf automake libtool curl
```
Ensuite, téléchargez protobuff et décompressez-le.  
https://github.com/protocolbuffers/protobuf/releases



Ensuite, entrez dans le dossier et exécutez la commande suivante qui peut rendre l'ordinateur inutilisable pendant les 2 prochaines heures.  Utilisez ctrl + alt + F1 pour passer en mode terminal uniquement et libérer toute la RAM de l'interface utilisateur.  Fermez le processus x avec control + c si nécessaire.   Vous pouvez ensuite exécuter la commande longue durée.  Nom d'utilisateur de base "pi" et mot de passe "raspberry"
```
make && make check
```
Vous pouvez ensuite installer simplement avec
```
sudo make install
cd python
export LD_LIBRARY_PATH=../src/.libs
python3 setup.py build --cpp_implementation
python3 setup.py test --cpp_implementation
sudo python3 setup.py install --cpp_implementation
export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=cpp
export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION_VERSION=3
sudo ldconfig
```

Une fois cela fait, vous pouvez nettoyer certains résidus d'installation avec sudo apt-get autoremove, supprimer le téléchargement tar.gz puis enfin redémarrer avec sudo reboot now qui vous ramènera à une interface fenêtrée

### Configurer Tensorflow
```
mkdir tensorflow1 && cd tesorflow1
git clone --recurse-submodules \ https://github.com/tensorflow/models.git
modifier ~/.bashrc pour contenir une nouvelle variable d'environnement nommée PYTHONPATH comme suit
export PYTHONPATH=$PYTHONPATH:/home/pi/tensorflow1/models/research:/home/pi/tensorflow1/models/research/slim
```

Maintenant, allez au zoo : https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md
Nous prendrons le ssdlite_mobilenet, qui est le plus rapide ! Wget le fichier puis tar -xzvf le résultat tar.gz et supprimez l'archive une fois décompressée. Faites cela dans le dossier `object_detection` dans votre dossier local `tensorflow1`. Maintenant, remontez dans le répertoire de recherche. Ensuite, exécutez :
```
protoc object_detection/protos/*.proto --python_out=.
```
Cela a converti les fichiers protos de détection d'objets en python dans le dossier proto

# Installation terminée !!

Un grand merci à [Edje Electronics](https://www.youtube.com/channel/UCLuS8eZl3_nKKq85gPS62lQ) pour avoir partagé leur sagesse sur la configuration, une ressource indispensable pour ma propre configuration et mon code.

Une fois que j'ai réussi à faire fonctionner Tensorflow, j'ai pu exécuter la reconnaissance d'objets (avec le code d'exemple fourni) sur Mobilenet à raison de 1 à 3 images par seconde.

![Image](https://cdn-media-1.freecodecamp.org/images/0*6AAvPd52hXAY42QV)

#### Résultats du Vanilla Pi

Pour une détection de base, 1 à 3 images par seconde ne sont pas mauvaises. Supprimer l'interface graphique ou réduire la qualité de l'entrée de la caméra accélère la détection. Cela signifie que l'outil pourrait être un excellent détecteur pour une simple détection. Quelle excellente base ! Voyons si nous pouvons l'améliorer avec les outils disponibles.

### Intel's Neural Compute Stick 2

Ce concept m'excite. Pour ceux d'entre nous qui n'ont pas de GPU facilement disponibles, s'entraîner sur le terrain plutôt que dans le cloud, et déplacer cette vitesse intense vers le Raspberry Pi est tout simplement excitant. J'ai manqué le bâton original, le "Movidius", mais d'après ce graphique, il semble que j'ai choisi un excellent moment pour acheter !

![Image](https://cdn-media-1.freecodecamp.org/images/0*BvMaSJQsL52PIyK_.jpg)

#### Installation

Mon Intel NCS2 est arrivé rapidement et j'ai apprécié le déballage du matériel réel pour accélérer mon entraînement. C'était probablement le dernier moment où j'étais excité.

Tout d'abord, l'USB prend beaucoup de place. Vous voudrez obtenir un câble pour le tenir à l'écart de la base.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jsB8SEZrmnY5V8gXne3pFA.jpeg)

C'est un peu ennuyeux mais bon. La partie vraiment ennuyeuse était d'essayer de faire fonctionner mon NCS 2.

Il y a beaucoup de tutoriels pour le NCS par des tiers, et les suivre m'a amené à un point où je pensais que la clé USB pouvait être cassée !

Tout ce que j'ai trouvé sur le NCS n'a pas fonctionné (me disant que le bâton n'était pas branché !), et tout ce que j'ai trouvé sur le NCS2 était assez confus. [Pendant un moment, le NCS2 ne fonctionnait même pas sur les processeurs ARM !](https://ncsforum.movidius.com/discussion/comment/4202)

> ?????????????????

Après beaucoup de fausses pistes, j'ai finalement trouvé et commencé à compiler des exemples en C++ (désolé Python) qui ne comprenaient que les caméras USB (désolé PiCam). La compilation des exemples était douloureuse. Souvent, tout le Raspberry Pi devenait inutilisable, et je devais redémarrer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WYgHc8_hie3jwVEAU_Qe0Q.jpeg)
_bloqué à 81% pendant 24 heures_

Toute l'expérience d'intégration a été plus douloureuse que la recompilation de Tensorflow sur le Pi brut. Heureusement, j'ai tout fait fonctionner !

**Le résultat !? ??????????????????????**

#### **Résultats du bâton NC2**

**6 à 8 images par seconde... ÊTES-VOUS SÉRIEUX !? Après tout ça ?**

**Ce doit être une erreur, laissez-moi exécuter le projet `perfcheck`.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*WbhdU_Ut0K9BDN2U1F9NVw.jpeg)

**10 images par seconde...**

**D'après les vidéos sur le NCS original en python, j'ai vu environ 10fps.. où est le boost 8x ? Où est la raison pour un matériel de 80 $ attaché à un appareil de 40 $ ? Dire que j'ai été déçu par le NCS2 d'Intel est un euphémisme. L'expérience utilisateur et les résultats finaux étaient frustrants, pour le dire légèrement.**

### **Xnor.ai**

![Image](https://cdn-media-1.freecodecamp.org/images/1*relSMp3LUrMmQSpzzupksw.jpeg)

**Xnor.ai est une solution logicielle autonome pour déployer des modèles de deep learning rapides et précis sur des appareils à faible coût. Comme de nombreux passionnés de logique discrète l'ont peut-être remarqué, Xnor est le complément logique de l'opérateur bitwise XOR. Si cela ne signifie rien pour vous, ce n'est pas grave. Sachez simplement que les personnes qui ont créé l'algorithme YOLO font allusion à l'utilisation de l'opérateur logique pour compresser des calculs complexes 32 bits en 1 bit en utilisant cette opération peu coûteuse et en gardant une trace de la pile CPU.**

**En théorie, éviter de tels calculs complexes requis par les GPU devrait accélérer l'exécution sur les appareils en périphérie. Voyons si cela fonctionne !**

#### **Installation**

**L'installation était incroyablement facile. J'avais une démonstration de détection d'objets opérationnelle en 5 minutes. **_5 MINUTES !_**

**Le truc avec Xnor.ai est que, comme le bâton NCS2, le modèle est modifié et optimisé pour le tissu matériel sous-jacent. Contrairement à l'installation hasardeuse d'Intel, tout est enveloppé dans un code Python (ou C) convivial.**

**`model = xnornet.Model.load_built_in()`**

**C'est simple et agréable.**

**Mais cela ne signifie rien si la performance n'y est pas. Chargeons leur modèle de détection d'objets.**

**Encore une fois, aucune complexité, ils en ont un sans superposition, et un avec. Puisque les autres (sauf pour perfcheck sur NCS2) étaient avec des superpositions, utilisons celui-ci.**

#### **Résultats de Xnor.ai**

**PERFORMANCE À COUPER LE SOUFFLE. Je n'obtiens pas seulement une statistique sur la rapidité avec laquelle l'inférence pourrait fonctionner, mais j'obtiens également un FPS global avec ma superposition qui a surpassé tout le reste.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*bJM6E_o4omDdQo4KLFwEGQ.jpeg)

**PLUS DE 12 FPS et une vitesse d'inférence supérieure à 34 FPS !?**

**Ce débit incroyable est atteint sans achat de matériel supplémentaire !? Je déclarerais Xnor le gagnant à ce stade, mais cela semble un peu trop évident.**

**J'ai pu chauffer mon appareil et ouvrir un navigateur en arrière-plan pour le faire descendre à 8+ FPS, mais même alors, c'est un gagnant clair !**

![Image](https://cdn-media-1.freecodecamp.org/images/1*dvybusIlJOxVNemjLytUsA.gif)
_L'hype de Xnor est réel_

**Le seul point négatif que je peux vous donner sur Xnor.ai est que je ne sais pas combien cela coûte. Le modèle d'évaluation a une limite de 13 500 inférences par démarrage.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*x_6iL1fZ6gKqYBK9M05lpg.png)

**En leur envoyant un e-mail pour obtenir les prix, ils commencent tout juste à entrer dans une utilisation non commerciale, donc ils n'ont pas encore créé de système de tarification. Heureusement, le modèle d'évaluation conviendrait à la plupart des amateurs et des prototypes.**

### **En résumé :**

**Si vous devez prendre en compte une variété de modèles, vous pourriez être très bien en configurant votre Raspberry Pi à partir de zéro. Cela en ferait une excellente ressource pour tester de nouveaux modèles et vraiment personnaliser votre expérience.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*iI4IXTmT-wm8tu6sik_oNw.png)

**Lorsque vous êtes prêt à expédier, il ne fait aucun doute que les frameworks NCS2 et Xnor.ai accélèrent les choses. Il ne fait également aucun doute que Xnor.ai a surpassé le NCS2 à la fois en intégration et en performance. Je ne suis pas sûr quel est le modèle de tarification de Xnor.ai, mais ce serait le facteur final dans ce qui est clairement un framework supérieur.**

#### **Mises à jour post-publication :**

**Voici un excellent article de blog sur la configuration du NCS2**

**[Getting Started with the Intel Neural Compute Stick 2 and the Raspberry Pi](https://medium.com/@aallan/getting-started-with-the-intel-neural-compute-stick-2-and-the-raspberry-pi-6904ccfe963)**  
**[_Getting started with Intel's Movidius hardware_medium.com](https://medium.com/@aallan/getting-started-with-the-intel-neural-compute-stick-2-and-the-raspberry-pi-6904ccfe963)**

**De plus, si vous cherchez à jouer avec Xnor.ai, le lien est [www.xnor.ai/ai2go](http://www.xnor.ai/ai2go)**

![Image](https://cdn-media-1.freecodecamp.org/images/1*kePT6qGxTucg__Uz9IC_mQ.png)

**[Gant Laborde](https://www.freecodecamp.org/news/perf-machine-learning-on-rasp-pi-51101d03dba2/undefined) est le Chief Technology Strategist chez [Infinite Red](http://infinite.red), un auteur publié, professeur adjoint, conférencier public mondial et scientifique fou en formation. Applaudissez/suivez/[tweetez](https://twitter.com/GantLaborde) ou visitez-le [à une conférence](http://gantlaborde.com/).**

**Attendez-vous à plus d'articles de blog sur le edge à venir !**

#### **Avez-vous un moment ? Lisez plus par Gant**

**[Avoid Nightmares — NSFW JS](https://shift.infinite.red/avoid-nightmares-nsfw-js-ab7b176978b1)**  
**[_Client-side indecent content checking for the soul_shift.infinite.red](https://shift.infinite.red/avoid-nightmares-nsfw-js-ab7b176978b1)**