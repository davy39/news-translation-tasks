---
title: Comment utiliser le prétraitement d'image pour améliorer la précision de Tesseract
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-06T13:25:41.000Z'
originalURL: https://freecodecamp.org/news/getting-started-with-tesseract-part-ii-f7f9a0899b3f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iZwvUAtgcOAVgjO23Hd2ig.jpeg
tags:
- name: 'OCR '
  slug: ocr
- name: opencv
  slug: opencv
- name: Python
  slug: python
- name: technology
  slug: technology
- name: tesseract
  slug: tesseract
seo_title: Comment utiliser le prétraitement d'image pour améliorer la précision de
  Tesseract
seo_desc: 'By Berk Kaan Kuguoglu

  Previously, on How to get started with Tesseract, I gave you a practical quick-start
  tutorial on Tesseract using Python. It is a pretty simple overview, but it should
  help you get started with Tesseract and clear some hurdles th...'
---

Par Berk Kaan Kuguoglu

Précédemment, dans [Comment commencer avec Tesseract](https://medium.com/@bkaankuguoglu/getting-started-with-tesseract-part-i-2a6a6b1cf75e), je vous ai donné un tutoriel pratique pour bien démarrer avec Tesseract en utilisant Python. C'est un aperçu assez simple, mais il devrait vous aider à commencer avec Tesseract et à surmonter certains obstacles que j'ai rencontrés lorsque j'étais à votre place. Maintenant, je suis impatient de vous montrer quelques astuces supplémentaires et des choses que vous pouvez faire avec Tesseract et OpenCV pour améliorer votre précision globale.

### Où en étions-nous la dernière fois ?

Dans [l'article précédent](https://medium.com/@bkaankuguoglu/getting-started-with-tesseract-part-i-2a6a6b1cf75e), je n'ai pas pris la peine d'entrer dans les détails pour la plupart. Mais si vous avez aimé le premier article, voici la suite ! Alors, où en étions-nous ?

Ah, nous avions un bref aperçu du redimensionnement, de la suppression du bruit et de la binarisation. Maintenant, il est temps d'entrer dans les détails et de vous montrer quelques paramètres avec lesquels vous pouvez jouer.

### Redimensionnement

Les images qui sont redimensionnées sont soit réduites, soit agrandies. Si vous êtes intéressé par la réduction de votre image, **INTER_AREA** est la méthode à utiliser. (Au fait, les paramètres _fx_ et _fy_ désignent le facteur d'échelle dans la fonction ci-dessous.)

```
img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
```

D'autre part, comme dans la plupart des cas, vous devrez peut-être redimensionner votre image à une taille plus grande pour reconnaître de petits caractères. Dans ce cas, **INTER_CUBIC** donne généralement de meilleurs résultats que les autres alternatives, bien qu'il soit également plus lent que les autres.

```
img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
```

Si vous souhaitez échanger un peu de la qualité de votre image contre des performances plus rapides, vous pouvez essayer **INTER_LINEAR** pour agrandir les images.

```
img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
```

### **Floutage**

Il est utile de mentionner qu'il existe plusieurs filtres de flou disponibles dans la [bibliothèque OpenCV](https://docs.opencv.org/3.4.0/d4/d13/tutorial_py_filtering.html). Le floutage de l'image est généralement réalisé en convoluant l'image avec un noyau de filtre passe-bas. Bien que les filtres soient généralement utilisés pour flouter l'image ou réduire le bruit, il existe quelques différences entre eux.

#### 1. Moyennage

Après avoir convolué une image avec un filtre de boîte normalisé, cela prend simplement la moyenne de tous les pixels sous la zone du noyau et remplace l'élément central. C'est assez explicite, je suppose.

```
img = cv.blur(img,(5,5))
```

#### 2. Flou gaussien

Cela fonctionne de manière similaire au moyennage, mais il utilise un noyau gaussien, au lieu d'un filtre de boîte normalisé, pour la convolution. Ici, les dimensions du noyau et les écarts types dans les deux directions peuvent être déterminés indépendamment. Le flou gaussien est très utile pour supprimer — devinez quoi ? — le bruit gaussien de l'image. En revanche, le flou gaussien ne préserve pas les bords de l'entrée.

```
img = cv2.GaussianBlur(img, (5, 5), 0)
```

#### 3. Flou médian

L'élément central dans la zone du noyau est remplacé par la médiane de tous les pixels sous le noyau. En particulier, cela surpasse les autres méthodes de floutage pour supprimer le bruit de type "poivre et sel" dans les images.

Le flou médian est un filtre non linéaire. Contrairement aux filtres linéaires, le flou médian remplace les valeurs des pixels par la valeur médiane disponible dans les valeurs du voisinage. Ainsi, le flou médian préserve les bords car la valeur médiane doit être la valeur de l'un des pixels voisins.

```
img = cv2.medianBlur(img, 3)
```

#### 4. Filtrage bilatéral

En parlant de garder les bords nets, le filtrage bilatéral est assez utile pour supprimer le bruit sans lisser les bords. Similaire au flou gaussien, le filtrage bilatéral utilise également un filtre gaussien pour trouver la moyenne pondérée gaussienne dans le voisinage. Cependant, il prend également en compte la différence de pixels lors du floutage des pixels voisins.

Ainsi, il garantit que seuls les pixels ayant une intensité similaire à celle du pixel central sont floutés, tandis que les pixels ayant des valeurs de pixels distinctes ne sont pas floutés. En faisant cela, les bords qui ont une plus grande variation d'intensité, appelés bords, sont préservés.

```
img = cv.bilateralFilter(img,9,75,75)
```

Dans l'ensemble, si vous êtes intéressé par la préservation des bords, optez pour le flou médian ou le filtrage bilatéral. En revanche, le flou gaussien est susceptible d'être plus rapide que le flou médian. En raison de sa complexité computationnelle, le filtrage bilatéral est le plus lent de toutes les méthodes.

Encore une fois, faites comme vous le sentez.

### Seuil d'image

Il n'existe pas une seule méthode de seuil d'image qui convienne à tous les types de documents. En réalité, tous les filtres se comportent différemment sur des images variées. Par exemple, alors que certains filtres binarisent avec succès certaines images, ils peuvent échouer à binariser d'autres. De même, certains filtres peuvent bien fonctionner avec des images que d'autres filtres ne peuvent pas bien binariser.

Je vais essayer de couvrir les bases ici, bien que je vous recommande de lire la documentation officielle d'[OpenCV sur le seuil d'image](https://docs.opencv.org/3.4.0/d7/d4d/tutorial_py_thresholding.html) pour plus d'informations et la théorie derrière cela.

#### 1. Seuil simple

Vous vous souvenez peut-être d'un ami vous donnant des conseils sur votre vie en disant "les choses ne sont pas toujours noires ou blanches". Eh bien, pour un seuil simple, les choses sont assez simples.

```
cv.threshold(img,127,255,cv.THRESH_BINARY)
```

D'abord, vous choisissez une valeur de seuil, disons 127. Si la valeur du pixel est supérieure au seuil, elle devient noire. Si elle est inférieure, elle devient blanche. OpenCV nous fournit différents types de méthodes de seuil qui peuvent être passées comme quatrième paramètre. J'utilise souvent le seuil binaire pour la plupart des tâches, mais pour d'autres méthodes de seuil, vous pouvez consulter [la documentation officielle](https://docs.opencv.org/3.4.0/d7/d4d/tutorial_py_thresholding.html).

#### 2. Seuil adaptatif

Plutôt que de définir une seule valeur de seuil globale, nous laissons l'algorithme calculer le seuil pour de petites régions de l'image. Ainsi, nous obtenons diverses valeurs de seuil pour différentes régions de l'image, ce qui est génial !

```
cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
```

Il existe deux méthodes adaptatives pour calculer la valeur de seuil. Alors que **Adaptive Thresh Mean** retourne la moyenne de la zone de voisinage, **Adaptive Gaussian Mean** calcule la somme pondérée des valeurs de voisinage.

Nous avons deux paramètres supplémentaires qui déterminent la taille de la zone de voisinage et la valeur constante qui est soustraite du résultat : les cinquième et sixième paramètres, respectivement.

#### 3. Seuil d'Otsu

Cette méthode fonctionne particulièrement bien avec les **images bimodales**, qui sont des images dont l'histogramme présente deux pics. Si c'est le cas, nous pourrions être intéressés par le choix d'une valeur de seuil entre ces pics. C'est ce que fait la binarisation d'Otsu.

```
cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
```

C'est assez utile pour certains cas. Mais cela peut échouer à binariser les images qui ne sont pas bimodales. Donc, veuillez prendre ce filtre avec des pincettes.

#### Types de seuillage

Vous avez peut-être déjà remarqué qu'il y a un paramètre, ou dans certains cas une combinaison de quelques paramètres, qui sont passés en arguments pour déterminer le type de seuillage, comme THRESH_BINARY. Je n'entre pas dans les détails ici maintenant, car cela est expliqué clairement dans [la documentation officielle](https://docs.opencv.org/3.4.0/d7/d4d/tutorial_py_thresholding.html).

### Et ensuite ?

Jusqu'à présent, nous avons discuté de certaines des techniques de prétraitement d'image. Vous vous demandez peut-être quand exactement vous allez mettre les mains dans le cambouis. Eh bien, le moment est venu. Avant de retourner à votre IDE Python préféré — le mien est [PyCharm](https://www.jetbrains.com/pycharm/), au fait — je vais vous montrer quelques lignes de code qui vous feront gagner du temps tout en essayant de trouver quelle combinaison de filtres et de manipulations d'image fonctionne bien avec vos documents.

Commençons par définir une fonction de commutation qui contient quelques combinaisons de filtres de seuillage et de méthodes de floutage. Une fois que vous avez compris l'idée, vous pourriez également ajouter plus de filtres, en incorporant d'autres méthodes de prétraitement d'image comme le redimensionnement dans votre ensemble de filtres.

Ici, j'ai créé 20 combinaisons différentes de méthodes de seuillage d'image, de méthodes de floutage et de tailles de noyau. La fonction de commutation, _apply_threshold_, prend deux arguments, à savoir l'image OpenCV et un entier qui désigne le filtre. De même, puisque cette fonction retourne l'image OpenCV comme résultat, elle pourrait facilement être intégrée dans notre fonction _get_string_ de l'article précédent.

```
def apply_threshold(img, argument):    switcher = {        1: cv2.threshold(cv2.GaussianBlur(img, (9, 9), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],        2: cv2.threshold(cv2.GaussianBlur(img, (7, 7), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],        3: cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
```

```
                              ...              
```

```
        18: cv2.adaptiveThreshold(cv2.medianBlur(img, 7), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2),        19: cv2.adaptiveThreshold(cv2.medianBlur(img, 5), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2),        20: cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)    }    return switcher.get(argument, "Invalid method")
```

Et voici.

```
def get_string(img_path, method):    # Lire l'image en utilisant opencv    img = cv2.imread(img_path)    # Extraire le nom du fichier sans l'extension    file_name = os.path.basename(img_path).split('.')[0]    file_name = file_name.split()[0]    # Créer un répertoire pour les sorties    output_path = os.path.join(output_dir, file_name)    if not os.path.exists(output_path):        os.makedirs(output_path)
```

```
    # Redimensionner l'image, si nécessaire.    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
```

```
    # Convertir en niveaux de gris    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # Appliquer la dilatation et l'érosion pour supprimer du bruit    kernel = np.ones((1, 1), np.uint8)    img = cv2.dilate(img, kernel, iterations=1)    img = cv2.erode(img, kernel, iterations=1)
```

```
    # Appliquer le seuil pour obtenir une image en noir et blanc uniquement    img = apply_threshold(img, method)
```

```
    # Enregistrer l'image filtrée dans le répertoire de sortie    save_path = os.path.join(output_path, file_name + "_filter_" + str(method) + ".jpg")    cv2.imwrite(save_path, img)    # Reconnaître le texte avec tesseract pour python    result = pytesseract.image_to_string(img, lang="eng")
```

```
    return result
```

### Derniers mots

Maintenant, tout ce que nous avons à faire est d'écrire une simple boucle for qui itère sur le répertoire d'entrée pour collecter les images et applique chaque filtre sur les images collectées. Je préfère utiliser _glob_, ou _os_, pour collecter les images des répertoires, et _argparse_ pour passer les arguments via le terminal, comme le ferait toute autre personne sensée.

Ici, j'ai fait à peu près la même chose que dans mon [gist](https://gist.github.com/bkaankuguoglu/111f9f5e0c30b5f57d7c5338d6dcb6fc), si vous souhaitez y jeter un coup d'œil. Cependant, n'hésitez pas à utiliser les outils avec lesquels vous êtes à l'aise.

Jusqu'à présent, j'ai essayé de couvrir quelques concepts et implémentations utiles de prétraitement d'image, bien que ce soit probablement juste la partie émergée de l'iceberg. Je ne sais pas combien de "temps libre" je vais avoir dans les semaines à venir, donc je ne peux pas vous donner un délai spécifique pour la publication de mon prochain article. Cependant, j'envisage d'ajouter au moins une autre partie à cette série qui explique quelques choses que j'ai laissées de côté, comme la rotation et la désinclinaison des images.

En attendant, le meilleur conseil est de garder votre sang-froid et de continuer à chercher des signes.[*](https://www.youtube.com/watch?v=B_CHjYoqPUU)