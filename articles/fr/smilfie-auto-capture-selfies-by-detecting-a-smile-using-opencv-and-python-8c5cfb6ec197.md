---
title: 'Smilefie : comment capturer automatiquement des selfies en détectant un sourire'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-07T17:47:53.000Z'
originalURL: https://freecodecamp.org/news/smilfie-auto-capture-selfies-by-detecting-a-smile-using-opencv-and-python-8c5cfb6ec197
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QV-7cBgxcxknDFjqUbFblQ.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Computer Vision
  slug: computer-vision
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: 'Smilefie : comment capturer automatiquement des selfies en détectant un
  sourire'
seo_desc: 'By Rishav Agarwal

  Ten second takeaway: use Python and OpenCV to create an app that automatically captures
  a selfie on detecting a smile. Now let’s get into it. :)

  I came across this advertisement for Oppo — the phone automatically captures a selfie
  w...'
---

Par Rishav Agarwal

Résumé en dix secondes : utilisez Python et OpenCV pour créer une application qui capture automatiquement un selfie en détectant un sourire. Maintenant, entrons dans le vif du sujet. :)

Je suis tombé sur cette [publicité](https://www.youtube.com/watch?v=aTQK2o-eW1Y) pour Oppo — le téléphone capture automatiquement un selfie lorsque la belle actrice sourit à la caméra. Cela semblait être un défi assez facile étant donné la merveilleuse bibliothèque **dlib** de Python.

Dans cet article, je vais parler de la façon dont vous pouvez créer une application similaire qui capture un selfie à partir d'une webcam en détectant un sourire. **Tout cela en ~50 lignes de code**.

### Aperçu du processus

1. Utilisez le détecteur de points de repère faciaux dans dlib pour obtenir les coordonnées de la bouche
2. Définissez un seuil de sourire, en utilisant un ratio d'aspect de la bouche (MAR)
3. Accédez à la webcam pour configurer un flux en direct
4. Capturez l'image
5. Enregistrez l'image
6. Fermez le flux de la caméra

### Bibliothèques requises

* **Numpy** : Utilisé pour les calculs et manipulations rapides de matrices.
* **dlib** : Bibliothèque contenant les points de repère faciaux.
* **Cv2** : La bibliothèque Open CV utilisée pour la manipulation et l'enregistrement d'images.
* **Scipy.spatial** : Utilisé pour calculer la distance euclidienne entre les points faciaux.
* **Imutils** : Bibliothèque pour accéder au flux vidéo.

Toutes les bibliothèques peuvent être installées en utilisant pip, **sauf** dlib. Pour dlib, nous devons installer **CMake** et **boost**. Voici comment les installer sur macOS en utilisant **brew**.

Si vous n'avez pas brew, [voici comment installer **Homebrew**](https://www.howtogeek.com/211541/homebrew-for-os-x-easily-installs-desktop-apps-and-terminal-utilities/).

#### **Installer CMake**

```
brew install cmake
```

#### **Installer boost**

```
brew install boost
brew install boost-python --with-python3
```

La deuxième commande garantit que boost est utilisable avec **Python 3**.

#### Installer dlib

Après cela, nous pouvons installer dlib en utilisant

```
pip install dlib
```

**Astuce** : J'aime utiliser **Anaconda**, un environnement virtuel pour chaque projet séparé. [Voici](https://medium.freecodecamp.org/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c) un excellent blog sur les raisons et les méthodes de gestion de l'environnement **conda**.

#### **Importer les bibliothèques**

```
from scipy.spatial import distance as dist
from imutils.video import VideoStream, FPS
from imutils import face_utils
import imutils
import numpy as np
import time
import dlib
import cv2
```

### **Détecteur de points de repère faciaux**

Le détecteur de points de repère faciaux est une API implémentée dans dlib. Il produit **68 coordonnées x-y** qui correspondent à des structures faciales spécifiques.

Cela peut être visualisé comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/x7Tv1rIkd4qoPU8ddffrT79ZhOPyNfSpQ8tk)
_Modèle d'index des points de repère faciaux pris de [PyImageSearch.com](https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/" rel="noopener" target="_blank" title=")_

Nous allons nous concentrer sur la bouche qui peut être accessible via la plage de points **[49,…, 68]**. Il y a vingt coordonnées.

En utilisant dlib, nous pouvons obtenir ces caractéristiques avec le code suivant :

```
shape_predictor = "../shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(shape_predictor)
(mStart, mEnd) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]
```

`(mStart, mEnd)` nous donne les premières et dernières coordonnées pour la bouche.

Vous pouvez télécharger le fichier de points de repère pré-entraîné [ici](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2) ou simplement [m'envoyer un email](mailto:rra.iitk@gmail.com) et je vous l'enverrai. N'oubliez pas de l'extraire.

### La fonction sourire

L'image ci-dessous montre uniquement les vingt coordonnées de la bouche :

![Image](https://cdn-media-1.freecodecamp.org/images/NeL2-TugkLgWxgvJTLb3qb1Y1PHINVo0yXpZ)
_Partie de la bouche recadrée de [PyImageSearch.com](https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/" rel="noopener" target="_blank" title=")_

J'ai créé un ratio d'aspect de la bouche (MAR) inspiré de deux articles sur la détection des clignements d'yeux. Il s'agit de [Real-Time Eye Blink Detection using Facial Landmarks](http://vision.fe.uni-lj.si/cvww2016/proceedings/papers/05.pdf)_._ et [Eye blink detection with OpenCV, Python, and dlib](https://www.pyimagesearch.com/2017/04/24/eye-blink-detection-opencv-python-dlib/). Le deuxième article développe le premier. Les deux discutent d'un ratio d'aspect, dans ce cas pour les yeux (EAR) :

![Image](https://cdn-media-1.freecodecamp.org/images/SGhh5QLStuWyQp-wZbrrqyrMpO7MiSwIMs2J)
_Les six points de repère faciaux pour l'œil._

La formule pour l'EAR est :

D = distance entre p1 et p4

L = moyenne de la distance entre p2 et p6 ; p3 et p5

![Image](https://cdn-media-1.freecodecamp.org/images/10jBkgyiCKZn78dtG0QmVfsa5PNSmh2FUDKJ)
_Équation de l'EAR_

```
EAR = L/D
```

Dans notre cas, le MAR est simplement défini comme la relation des points montrés ci-dessous

![Image](https://cdn-media-1.freecodecamp.org/images/QwHmcIumrY-z-gEECt3U9QtfDqHRUdYwN0N4)
_La partie de la bouche extraite de la figure ci-dessus_

Nous calculons la distance entre p49 et p55 comme D, et nous faisons la moyenne des distances entre :

p51 et p59

p52 et p58

p53 et p57

Appelons cela L, en utilisant la même structure de nommage :

![Image](https://cdn-media-1.freecodecamp.org/images/Uf9mPQOzmVvjepNh7lNmriCOO7c3unXHSlsP)
_Équation du MAR_

```
MAR = L/D
```

Voici la fonction pour calculer le MAR.

```
def smile(mouth):
    A = dist.euclidean(mouth[3], mouth[9])
    B = dist.euclidean(mouth[2], mouth[10])
    C = dist.euclidean(mouth[4], mouth[8])
    L = (A+B+C)/3
    D = dist.euclidean(mouth[0], mouth[6])
    mar = L/D
    return mar
```

**Astuce** : Lorsque nous découpons le tableau, le point _49_ devient le premier élément du tableau (0) et tous les autres indices sont ajustés en conséquence :

Sourire avec la bouche fermée augmente la distance entre p49 et p55 et diminue la distance entre les points supérieur et inférieur. Ainsi, L diminuera et D augmentera.

Sourire avec la bouche ouverte entraîne une diminution de D et une augmentation de L.

Voyez comment le MAR change lorsque je change les formes de la bouche :

![Image](https://cdn-media-1.freecodecamp.org/images/jd5C0ikecDvdslCS9k3REIawOdi0-urNXZnv)
_Le MAR change avec les traits du visage_

Sur cette base, j'ai défini un sourire comme étant un MAR de **< .3 ou > .38**. J'aurais pu prendre simplement **D** car D augmentera toujours lorsque quelqu'un sourit. Mais D ne sera pas le même pour tous, car les gens ont des formes de bouche différentes.

Ce sont des estimations approximatives et peuvent inclure d'autres émotions comme "awe". Pour surmonter cela, vous pouvez créer un modèle plus avancé. Vous pourriez prendre en compte plus de traits faciaux, ou simplement entraîner un classificateur d'émotions basé sur la vision par ordinateur.

Maintenant que nous avons une fonction sourire, nous pouvons implémenter la capture vidéo.

### Capture vidéo

#### Accéder à la webcam

Nous pouvons accéder à la webcam via la bibliothèque imutils en utilisant la commande suivante. `cv2.namedWindow` crée une nouvelle fenêtre :

```
vs = VideoStream(src=0).start()
fileStream = False
time.sleep(1.0)
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
```

#### Détection du visage

Nous arrivons maintenant à la boucle principale où la magie opère. Tout d'abord, nous capturons une seule image et la convertissons en niveaux de gris pour un calcul facile. Nous utilisons cela pour détecter le visage. `cv2.convexHull(mouth)` détecte le contour de la bouche et `cv2.drawContours` dessine un contour vert autour.

```
while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)
    for rect in rects:
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        mouth = shape[mStart:mEnd]
        mar = smile(mouth)
        mouthHull = cv2.convexHull(mouth)
        cv2.drawContours(frame, [mouthHull], -1, (0, 255, 0), 1)
```

**Astuce** : cette configuration peut détecter **plusieurs** sourires dans une seule image.

#### Auto-capture

Ensuite, nous définissons la condition d'auto-capture :

```
if mar <= .3 or mar > .38:
    COUNTER += 1
else:
    if COUNTER >= 15:
        TOTAL += 1
        frame = vs.read()
        time.sleep(0.3)
        img_name = "opencv_frame_{}.png".format(TOTAL)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        cv2.destroyWindow("test")
    COUNTER = 0
```

Ici, je considère qu'un sourire est "digne d'un selfie" si la personne le maintient pendant une demi-seconde, ou 30 images.

Nous vérifions si le MAR est **< .3 ou > .38** pendant au moins 15 images, puis nous enregistrons la 16ème image. Le fichier est enregistré dans le même dossier que le code avec le nom "opencv_frame_<counter>.png".

J'ai ajouté quelques fonctions `time.sleep` pour fluidifier l'expérience. Les téléphones contournent généralement ces problèmes matériels en utilisant des astuces comme des animations ou des écrans de chargement.

**Astuce** : Cette partie est à l'intérieur de la boucle while.

Nous affichons également le MAR sur l'image avec la fonction `cv2.putText` :

```
cv2.putText(frame, "MAR: {}".format(mar), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
```

**Astuce** : Mon Mac a une caméra de 30 fps, donc j'ai utilisé 30 comme nombre d'images. Vous pouvez changer cela en conséquence. Une manière plus simple est de trouver le fps en utilisant la fonction fps dans imutils.

### Quitter le flux vidéo

Enfin, ajoutez une commande de sortie qui arrête le flux vidéo lorsque la touche "q" est pressée. Cela est réalisé en ajoutant :

```
key2 = cv2.waitKey(1) & 0xFF
if key2 == ord('q'):
    break
```

Enfin, nous détruisons la fenêtre en utilisant

```
cv2.destroyAllWindows()
vs.stop()
```

et nous avons terminé !

Le code entier en action :

![Image](https://cdn-media-1.freecodecamp.org/images/PCbadKbc66wwGKIaXBgHBNAIuhKnap6fwylR)
_Enregistré en utilisant Quicktime_

Vous pouvez trouver le code entier sur mon [GitHub](https://github.com/rra94/smilfie).

C'était une application de base de la bibliothèque dlib. À partir de là, vous pouvez passer à la création de choses comme vos propres [filtres snapchat](https://github.com/charlielito/snapchat-filters-opencv), des systèmes de [surveillance domestique high-tech](https://github.com/BrandonJoffe/home_surveillance), ou même un détecteur de bonheur post-orwellien.

[Tweetez-moi](https://twitter.com/r15hav) si vous finissez par faire d'autres choses cool avec cela ou si vous trouvez un meilleur détecteur de sourire. Une autre idée cool est de faire un peu de post-traitement sur l'image capturée (comme dans la publicité) pour rendre la photo plus belle.

Merci d'avoir lu. Si vous avez aimé ce que vous avez lu, applaudissez et suivez-moi. Cela signifierait beaucoup et m'encouragerait à écrire plus. Restons en contact sur [Twitter](https://twitter.com/r15hav) et [Linkedin](https://www.linkedin.com/in/rragarwal/) également :)