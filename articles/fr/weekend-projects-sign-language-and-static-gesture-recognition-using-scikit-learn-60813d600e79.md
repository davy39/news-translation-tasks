---
title: 'Projet de week-end : reconnaissance de la langue des signes et des gestes
  statiques avec scikit-learn'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-12-26T05:39:41.000Z'
originalURL: https://freecodecamp.org/news/weekend-projects-sign-language-and-static-gesture-recognition-using-scikit-learn-60813d600e79
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KAm4Ld62yKhVUka-r8s7zA.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: 'Projet de week-end : reconnaissance de la langue des signes et des gestes
  statiques avec scikit-learn'
seo_desc: 'By Sreehari

  Let’s build a machine learning pipeline that can read the sign language alphabet
  just by looking at a raw image of a person’s hand.


  A raw image indicating the alphabet ‘A’ in sign language

  This problem has two parts to it:


  Building a st...'
---

Par Sreehari

Construisons un pipeline d'apprentissage automatique capable de lire l'alphabet de la langue des signes simplement en regardant une image brute de la main d'une personne.

![Image](https://cdn-media-1.freecodecamp.org/images/7pGrbu5lViTLkhDfUrude0lK6CyuGNFR0VMB)
_Une image brute indiquant la lettre 'A' en langue des signes_

Ce problème se compose de deux parties :

1. Construire un reconnaisseur de gestes statiques, qui est un classificateur multi-classes prédisant les gestes statiques de la langue des signes.
2. Localiser la main dans l'image brute et alimenter cette section de l'image au reconnaisseur de gestes statiques (le classificateur multi-classes).

Vous pouvez obtenir mon exemple de code et le jeu de données pour ce projet [ici](https://github.com/mon95/Sign-Language-and-Static-gesture-recognition-using-sklearn).

### D'abord, un peu de contexte.

La reconnaissance de gestes est un problème ouvert dans le domaine de la vision par ordinateur, un champ de l'informatique qui permet aux systèmes d'émuler la vision humaine. La reconnaissance de gestes a de nombreuses applications pour améliorer l'interaction homme-machine, et l'une d'entre elles est dans le domaine de la traduction de la langue des signes, où une séquence vidéo de gestes symboliques des mains est traduite en langage naturel.

Une gamme de méthodes avancées pour cela a été développée. Ici, nous verrons comment effectuer la reconnaissance de gestes statiques en utilisant les bibliothèques scikit-learn et scikit-image.

#### Partie 1 : Construire un reconnaisseur de gestes statiques

Pour cette partie, nous utilisons un jeu de données composé d'images brutes et d'un fichier CSV correspondant avec des coordonnées indiquant la boîte englobante pour la main dans chaque image. ([Utilisez le fichier Dataset.zip pour obtenir l'exemple de jeu de données. Extrayez selon les instructions dans le fichier readme](https://github.com/mon95/Sign-Language-and-Static-gesture-recognition-using-sklearn))

Ce jeu de données est organisé par utilisateur et la structure du répertoire du jeu de données est la suivante. Les noms des images indiquent l'alphabet représenté par l'image.

```
dataset
   |----user_1
          |---A0.jpg
          |---A1.jpg
          |---A2.jpg
          |---...
          |---Y9.jpg
   |----user_2
          |---A0.jpg
          |---A1.jpg
          |---A2.jpg
          |---...
          |---Y9.jpg
   |---- ...
   |---- ...
```

Le reconnaisseur de gestes statiques est essentiellement un classificateur multi-classes qui est entraîné sur des images d'entrée représentant les 24 gestes statiques de la langue des signes (A-Y, à l'exclusion de J).

Construire un reconnaisseur de gestes statiques en utilisant les images brutes et le fichier CSV est assez simple.

![Image](https://cdn-media-1.freecodecamp.org/images/NtJOVa5UYg3XxUHAeh2B4wfY9uCwqsQ3Je3M)

Pour utiliser les classificateurs multi-classes de la bibliothèque scikit-learn, nous devons d'abord construire le jeu de données — c'est-à-dire que chaque image doit être convertie en un vecteur de caractéristiques (X) et chaque image aura une étiquette correspondant à l'alphabet de la langue des signes qu'elle représente (Y).

La clé maintenant est d'utiliser une stratégie appropriée pour vectoriser l'image et extraire des informations significatives à alimenter au classificateur. Utiliser simplement les valeurs brutes des pixels ne fonctionnera pas si nous prévoyons d'utiliser des classificateurs multi-classes simples (par opposition à l'utilisation de réseaux de convolution).

Pour vectoriser nos images, nous utilisons l'approche Histogram of Oriented Gradients (HOG), car il a été prouvé qu'elle donne de bons résultats sur des problèmes tels que celui-ci. D'autres extracteurs de caractéristiques qui peuvent être utilisés incluent les Local Binary Patterns et les filtres de Haar.

![Image](https://cdn-media-1.freecodecamp.org/images/y0EAv9vleEEaEBuqJIEUculNIa-71DX11YBf)

#### Code :

Nous utilisons pandas dans la fonction get_data() pour charger le fichier CSV. Deux fonctions — crop() et convertToGrayToHog() — sont utilisées pour obtenir le vecteur hog requis et l'ajouter à la liste des vecteurs que nous construisons, afin d'entraîner le classificateur multi-classes.

```py
# retourne le vecteur hog d'un vecteur d'image particulier
def convertToGrayToHOG(imgVector):
    rgbImage = rgb2gray(imgVector)
    return hog(rgbImage)
    
# retourne l'image rognée 
def crop(img, x1, x2, y1, y2, scale):
    crp=img[y1:y2,x1:x2]
    crp=resize(crp,((scale, scale))) 
    return crp
    
# charge les données pour la classification multiclasse
def get_data(user_list, img_dict, data_directory):
  X = []
  Y = []
  
  for user in user_list:
    user_images = glob.glob(data_directory+user+'/*.jpg')
    
    boundingbox_df = pd.read_csv(data_directory + user + '/'
 + user + '_loc.csv')
        
    for rows in boundingbox_df.iterrows():
      cropped_img = crop( img_dict[rows[1]['image']], 
                         rows[1]['top_left_x'], 
                         rows[1]['bottom_right_x'], 
                         rows[1]['top_left_y'], 
                         rows[1]['bottom_right_y'], 
                         128
                        )
       hogvector = convertToGrayToHOG(cropped_img)
       
       X.append(hogvector.tolist())
       Y.append(rows[1]['image'].split('/')[1][0])
       
    return X, Y
```

L'étape suivante consiste à encoder les étiquettes de sortie (les valeurs Y) en valeurs numériques. Nous faisons cela en utilisant l'encodeur d'étiquettes de sklearn.

Dans notre code, nous avons fait cela comme suit :

```py
Y_mul = self.label_encoder.fit_transform(Y_mul)
```

où l'objet label_encoder est construit comme suit dans le constructeur de la classe gesture-recognizer :

```py
self.label_encoder = LabelEncoder().fit(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y'])
```

Une fois cela fait, le modèle peut être entraîné en utilisant n'importe quel algorithme de classification multi-classes de votre choix dans la boîte à outils scikit-learn. Nous avons entraîné le nôtre en utilisant la [Classification par Vecteurs de Support](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html), avec un noyau linéaire.

L'entraînement d'un modèle en utilisant sklearn ne nécessite pas plus de deux lignes de code. Voici comment faire :

```py
svcmodel = SVC(kernel='linear', C=0.9, probability=True) 
self.signDetector = svcmodel.fit(X_mul, Y_mul) 
```

Les hyperparamètres (c'est-à-dire, C=0.9 dans ce cas) peuvent être ajustés en utilisant une recherche sur grille. Lisez plus à ce sujet [ici](http://scikit-learn.org/stable/modules/grid_search.html).

Dans ce cas, nous ne savons pas grand-chose sur les données en tant que telles (c'est-à-dire, les vecteurs hog). Il serait donc bon d'essayer d'utiliser des algorithmes comme xgboost (Extreme Gradient Boosting) ou des classificateurs de forêt aléatoire et de voir comment ces algorithmes performants.

#### Partie 2 : Construire le localisateur

Cette partie nécessite un peu plus d'efforts par rapport à la première.

Globalement, nous emploierons les étapes suivantes pour accomplir cette tâche.

1. **Construire un jeu de données** comprenant des images de mains et des parties qui ne sont pas des mains, en utilisant le jeu de données donné et les valeurs de boîte englobante pour chaque image.
2. **Entraîner un classificateur binaire** pour détecter les images de mains/non-mains en utilisant le jeu de données ci-dessus.
3. (Facultatif) Utiliser **l'extraction de négatifs difficiles** pour améliorer le classificateur.
4. Utiliser une **approche de fenêtre glissante** avec diverses échelles, sur l'image de requête pour isoler la région d'intérêt.

_Ici, nous n'allons pas utiliser de techniques de traitement d'image comme le filtrage, la segmentation de couleur, etc. La bibliothèque scikit-image est utilisée pour lire, rogner, redimensionner, convertir les images en niveaux de gris et extraire les vecteurs hog._

#### Construire le jeu de données main/pas main :

Le jeu de données pourrait être construit en utilisant n'importe quelle stratégie que vous aimez. Une façon de faire cela est de générer des coordonnées aléatoires et de vérifier le rapport de la surface d'intersection à la surface d'union (c'est-à-dire, le degré de chevauchement avec la boîte englobante donnée) pour déterminer s'il s'agit d'une section non-main. (Une autre approche pourrait être d'utiliser une fenêtre glissante pour déterminer les coordonnées. Mais cela est horriblement lent et inutile)

```py
"""
Cette fonction génère aléatoirement des boîtes englobantes
Retourne le vecteur hog de ces boîtes englobantes rognées avec l'étiquette
Étiquette : 1 si main, 0 sinon
"""
def buildhandnothand_lis(frame,imgset):
    poslis =[]
    neglis =[]
    
    for nameimg in frame.image:
        tupl = frame[frame['image']==nameimg].values[0]
        x_tl = tupl[1]
        y_tl = tupl[2]
        side = tupl[5]
        conf = 0
        
        dic = [0, 0]
        
        arg1 = [x_tl,y_tl,conf,side,side]
        
        poslis.append( convertToGrayToHOG(crop(imgset[nameimg],  x_tl,x_tl+side,y_tl,y_tl+side)))
        
        while dic[0] <= 1 or dic[1] < 1:
            x = random.randint(0,320-side)
            y = random.randint(0,240-side) 
            crp = crop(imgset[nameimg],x,x+side,y,y+side)
            hogv = convertToGrayToHOG(crp)
            arg2 = [x,y, conf, side, side]
            
            z = overlapping_area(arg1,arg2)
            if dic[0] <= 1 and z <= 0.5:
                neglis.append(hogv)
                dic[0] += 1
            if dic[0]== 1:
                break
        label_1 = [1 for i in range(0,len(poslis)) ]
        label_0 = [0 for i in range(0,len(neglis))]
        label_1.extend(label_0)
        poslis.extend(neglis)
        
        return poslis,label_1
```

#### Entraîner un classificateur binaire :

Une fois le jeu de données prêt, l'entraînement du classificateur peut être fait exactement comme vu précédemment dans la partie 1.

Habituellement, dans ce cas, une technique appelée [Extraction de Négatifs Difficiles](https://www.reddit.com/r/computervision/comments/2ggc5l/what_is_hard_negative_mining_and_how_is_it/) est employée pour réduire le nombre de détections de faux positifs et améliorer le classificateur. Une ou deux itérations d'extraction de négatifs difficiles en utilisant un classificateur de forêt aléatoire suffisent pour garantir que votre classificateur atteint des précisions de classification acceptables, qui dans ce cas est tout ce qui est supérieur à 80 %.

Jetez un coup d'œil au [code ici pour une implémentation d'exemple de la même chose](https://github.com/mon95/Sign-Language-and-Static-gesture-recognition-using-sklearn/blob/master/dataset/gesture_recognizer1.py#L221).

#### Détecter les mains dans les images de test :

Maintenant, pour utiliser réellement le classificateur ci-dessus, nous redimensionnons l'image de test par divers facteurs, puis utilisons une [approche de fenêtre glissante](http://www.pyimagesearch.com/2015/03/23/sliding-windows-for-object-detection-with-python-and-opencv/) sur toutes pour choisir la fenêtre qui capture parfaitement la région d'intérêt. Cela est fait en sélectionnant la région correspondant au maximum des scores de confiance alloués par le classificateur binaire (main/pas main) à travers toutes les échelles.

Les images de test doivent être redimensionnées car nous faisons glisser une fenêtre de taille fixe (dans notre cas, 128x128) sur toutes les images pour choisir la région d'intérêt, et il est possible que la région d'intérêt ne s'adapte pas parfaitement à cette taille de fenêtre.

[Implémentation d'exemple](https://github.com/mon95/Sign-Language-and-Static-gesture-recognition-using-sklearn/blob/master/dataset/gesture_recognizer1.py#L312) et [détection globale à travers toutes les échelles](https://github.com/mon95/Sign-Language-and-Static-gesture-recognition-using-sklearn/blob/master/dataset/gesture_recognizer1.py#L416).

#### Mettre tout ensemble

Après que les deux parties soient complètes, tout ce qui reste à faire est de les appeler en succession pour obtenir la sortie finale lorsqu'une image de test est fournie.

C'est-à-dire, étant donné une image de test, nous obtenons d'abord les diverses régions détectées à travers différentes échelles de l'image et choisissons la meilleure parmi elles. Cette région est ensuite rognée, redimensionnée (à 128x128) et son vecteur hog correspondant est alimenté au classificateur multi-classes (c'est-à-dire, le reconnaisseur de gestes). Le reconnaisseur de gestes prédit alors le geste désigné par la main dans l'image.

#### Points clés

Pour résumer, ce projet implique les étapes suivantes. Les liens renvoient au code pertinent dans le dépôt github.

1. [Construire le jeu de données main/pas main](https://github.com/mon95/Sign-Language-and-Static-gesture-recognition-using-sklearn/blob/master/dataset/gesture_recognizer1.py#L71).
2. [Convertir toutes les images, c'est-à-dire les sections rognées avec les gestes et les images main/pas main, en leur forme vectorisée.](https://github.com/mon95/Sign-Language-and-Static-gesture-recognition-using-sklearn/blob/master/dataset/gesture_recognizer1.py#L43)
3. [Construire un classificateur binaire pour détecter la section avec la main et construire un classificateur multi-classes pour identifier le geste en utilisant ces jeux de données.](https://github.com/mon95/Sign-Language-and-Static-gesture-recognition-using-sklearn/blob/master/dataset/gesture_recognizer1.py#L360)
4. [Utiliser les classificateurs ci-dessus l'un après l'autre pour effectuer la tâche requise.](https://github.com/mon95/Sign-Language-and-Static-gesture-recognition-using-sklearn/blob/master/dataset/gesture_recognizer1.py#L403)

[Suks](https://www.facebook.com/sukriti10.tiwari) et moi avons travaillé sur ce projet dans le cadre du cours d'apprentissage automatique que nous avons suivi à l'université. Un grand merci à elle pour toutes ses contributions !

De plus, nous voulions mentionner [Pyimagesearch](https://www.pyimagesearch.com), qui est un blog merveilleux que nous avons utilisé de manière extensive pendant que nous travaillions sur le projet ! N'hésitez pas à le consulter pour du contenu sur le traitement d'image et le contenu lié à opencv.

Santé !