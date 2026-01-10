---
title: Comment transformer n'importe quelle image en un croquis au crayon avec 10
  lignes de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-21T21:21:39.000Z'
originalURL: https://freecodecamp.org/news/sketchify-turn-any-image-into-a-pencil-sketch-with-10-lines-of-code-cf67fa4f68ce
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cFcDUhcYTBx4AtGpXzeyXw.png
tags:
- name: Computer Vision
  slug: computer-vision
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: Comment transformer n'importe quelle image en un croquis au crayon avec
  10 lignes de code
seo_desc: 'By Rishav Agarwal

  Use basic computer vision and Python’s Numpy library

  I have always been fascinated by computer vision, and especially by its power to
  manipulate images.

  An image is basically an array of numbers to Python. So we can perform a variet...'
---

Par Rishav Agarwal

#### _Utiliser la vision par ordinateur de base et la bibliothèque Numpy de Python_

J'ai toujours été fasciné par la vision par ordinateur, et surtout par sa puissance à manipuler des images.

Une image est essentiellement un tableau de nombres pour Python. Nous pouvons donc effectuer une variété de manipulations de matrices pour obtenir des résultats très intéressants. Dans cet article, je parle de la manière de réduire une image en un contour "crayon".

#### Les Étapes

Le processus est assez simple :

1. Convertir l'image en niveaux de gris
2. L'inverser
3. Flouter l'image inversée
4. Fusionner par incrustation (Dodge blend) l'image floutée et l'image en niveaux de gris.

Nous pouvons choisir n'importe quelle image sur Internet. Je vais opter pour cette image du joueur de cricket indien Virat Kohli :

![Image](https://cdn-media-1.freecodecamp.org/images/1*TG0CeJvuv1iwskaCQSEyNA.gif)

#### **1. Charger l'image**

```
import imageio
img="http://static.cricinfo.com/db/PICTURES/CMS/263600/263697.20.jpg"
start_img = imageio.imread(img)
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*v-q4is6XGAQ6XLYI2m7NzQ.jpeg)
_Image initiale_

Vous pouvez voir comment Python voit cette image avec l'attribut `shape` :

```
start_img.shape
(196, 160, 30)
```

Il s'agit donc d'une image à trois canaux de taille 196x160.

#### **2. Conversion en niveaux de gris**

Nous rendons ensuite l'image en noir et blanc.

Numpy n'a pas de fonction intégrée pour la conversion en niveaux de gris, mais nous pouvons facilement convertir l'image en utilisant la formule. Vous pouvez apprendre pourquoi cette formule fonctionne juste [ici](https://www.w3.org/Graphics/Color/sRGB).

```
Y= 0.299 R + 0.587 G + 0.114 B
```

Notre fonction ressemblera donc à ceci :

```
import numpy as np
def grayscale(rgb): 
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
```

Application des niveaux de gris :

```
gray_img = grayscale(start_img)
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*XOYmVdB9JvBtPAIkpnPVRw.png)
_Image en niveaux de gris_

#### **3. Inverser l'image**

Nous pouvons inverser les images simplement en soustrayant de 255, car les images en niveaux de gris sont des images 8 bits ou ont un maximum de 256 tons.

```
inverted_img = 255-gray_img
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*k47Y4d4kAFP3tTydH2xlcQ.png)
_Image inversée_

#### **4. Flouter l'image**

Nous floutons maintenant l'image inversée. Le floutage est effectué en appliquant un [filtre gaussien](https://en.wikipedia.org/wiki/Gaussian_blur) à l'image inversée. La clé ici est la variance de la fonction gaussienne ou sigma.

À mesure que sigma augmente, l'image devient plus floue. Sigma contrôle l'étendue de la variance et donc, le degré de flou.

```
import scipy.ndimage
blur_img = scipy.ndimage.filters.gaussian_filter(inverted_img,sigma=5)
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*sS1PIpHogxUKPNDRkOBLuQ.gif)
_Plus de flou en augmentant sigma_

#### **5. Incrustation (Dodge) et fusion**

Le mode de fusion [Colour Dodge](https://en.wikipedia.org/wiki/Blend_modes) divise la couche inférieure par la couche supérieure inversée. Cela éclaircit la couche inférieure en fonction de la valeur de la couche supérieure. Nous avons l'image floutée, qui met en évidence les contours les plus marqués.

Comme toutes nos images sont lues en utilisant Numpy, tous les calculs de matrices sont super rapides.

```
def dodge(front,back): 
    result=front*255/(255-back) 
    result[result>255]=255 
    result[back==255]=255 
    return result.astype('uint8')
```

```
final_img= dodge(blur_img,gray_img)
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*K8GCJlziwZm3NmONoy3B7g.png)
_Image finale_

Et c'est tout !

#### **6. Tracer et sauvegarder**

Nous pouvons tracer notre image finale en utilisant `plt.imgshow`. Notez que nous devons garder l'argument `cmap` égal à "gray".

```
import matplotlib.pyplot as plt
plt.imshow(final_img, cmap="gray")
```

Nous pouvons sauvegarder l'image en utilisant :

```
plt.imsave('img2.png', final_img, cmap='gray', vmin=0, vmax=255)
```

#### Résultat final

![Image](https://cdn-media-1.freecodecamp.org/images/1*cFcDUhcYTBx4AtGpXzeyXw.png)

#### Code entier en action

![Image](https://cdn-media-1.freecodecamp.org/images/1*h94l7xWnXk_6dbzDUuPamw.png)
_Chaque étape de l'algorithme_

Ici, nous n'avons pas beaucoup de marge de manœuvre, sauf avec le paramètre sigma lors du floutage.

À mesure que sigma augmente, l'image devient plus claire mais le temps d'exécution augmente également. Un sigma de 5 fonctionne donc bien pour nous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Xdeu0DckWzCXMX6P1TwGzA.gif)
_effet de l'augmentation de sigma_

#### Code condensé :

J'ai promis 10 lignes ou moins, alors voici :

Comme toujours, vous pouvez trouver le code détaillé complet sur mon [GitHub](https://github.com/rra94/sketchify/tree/master).

PS c'est ainsi que j'ai créé mon DP Medium. Si vous aimez ce blog, montrez un peu ❤️ :)

De plus, je ne possède pas cette image de Virat. J'espère qu'il ne m'en voudra pas !