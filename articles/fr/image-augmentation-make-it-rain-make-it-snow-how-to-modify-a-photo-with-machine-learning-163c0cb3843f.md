---
title: 'Augmentation d''images : faites pleuvoir, faites neiger. Comment modifier
  des photos pour entraîner des voitures autonomes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-09T04:02:55.000Z'
originalURL: https://freecodecamp.org/news/image-augmentation-make-it-rain-make-it-snow-how-to-modify-a-photo-with-machine-learning-163c0cb3843f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WIFnuUgYya_oEEGrx650DQ.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: image processing
  slug: image-processing
- name: Machine Learning
  slug: machine-learning
- name: self-driving cars
  slug: self-driving-cars
- name: 'tech '
  slug: tech
seo_title: 'Augmentation d''images : faites pleuvoir, faites neiger. Comment modifier
  des photos pour entraîner des voitures autonomes'
seo_desc: 'By Ujjwal Saxena

  Image Augmentation is a technique for taking an image and using it to generating
  new ones. It’s useful for doing things like training a self-driving car.

  Think of a person driving a car on a sunny day. If it starts raining, they may ...'
---

Par Ujjwal Saxena

L'augmentation d'images est une technique qui consiste à prendre une image et à en générer de nouvelles. Elle est utile pour faire des choses comme entraîner une voiture autonome.

Imaginez une personne conduisant une voiture par une journée ensoleillée. Si la pluie commence à tomber, elle peut initialement trouver difficile de conduire sous la pluie. Mais lentement, elle s'y habitue.

Un réseau de neurones artificiels trouve également déroutant de conduire dans un nouvel environnement, sauf s'il l'a déjà vu. Il existe diverses techniques d'augmentation comme le retournement, la translation, l'ajout de bruit ou le changement de canal de couleur.

Dans cet article, j'explorerai la partie météo de cela. J'ai utilisé la bibliothèque **OpenCV** pour traiter les images. Je l'ai trouvé assez facile après un certain temps, et j'ai pu introduire divers scénarios météorologiques dans une image.

J'ai poussé un **Jupyter Notebook** entièrement implémenté avec lequel vous pouvez jouer sur [GitHub](https://github.com/ujjwalsaxena).

Commençons.

Je vais d'abord vous montrer une image de test originale et ensuite l'augmenter.

![Image](https://cdn-media-1.freecodecamp.org/images/DPVOfe-5jaoOME91KftyK1dlzvHu2FYMyzrO)

### **Ensoleillé et ombragé**

Après avoir ajouté un effet ensoleillé et ombragé aléatoire, la luminosité de l'image change. Il s'agit d'une transformation facile et rapide à effectuer.

```
def add_brightness(image):    image_HLS = cv2.cvtColor(image,cv2.COLOR_RGB2HLS) ## Conversion en HLS    image_HLS = np.array(image_HLS, dtype = np.float64)     random_brightness_coefficient = np.random.uniform()+0.5 ## génère une valeur entre 0,5 et 1,5    image_HLS[:,:,1] = image_HLS[:,:,1]*random_brightness_coefficient ## met à l'échelle les valeurs de pixels vers le haut ou vers le bas pour le canal 1 (Luminosité)    image_HLS[:,:,1][image_HLS[:,:,1]>255]  = 255 ## Définit toutes les valeurs supérieures à 255 à 255    image_HLS = np.array(image_HLS, dtype = np.uint8)    image_RGB = cv2.cvtColor(image_HLS,cv2.COLOR_HLS2RGB) ## Conversion en RGB    return image_RGB
```

La luminosité d'une image peut être modifiée en changeant les valeurs de pixels du canal "Luminosité" - canal 1 de l'image dans l'espace couleur HLS. La conversion de l'image en RGB donne la même image avec un éclairage amélioré ou supprimé.

![Image](https://cdn-media-1.freecodecamp.org/images/tny-s9fdRMRzn1zfmy1e3OIK82csRqGJ5Yv1)
_Ensoleillé_

![Image](https://cdn-media-1.freecodecamp.org/images/D-cHi--aKE1HWME2vjtrkshXS8JIbAvljuOx)
_Ombragé_

### **Ombres**

Pour une voiture, une ombre n'est rien d'autre que les parties sombres d'une image, qui peuvent aussi être lumineuses à certains moments. Ainsi, une voiture autonome doit toujours apprendre à conduire avec ou sans ombres. Le changement aléatoire de la luminosité sur les collines ou dans les bois perturbe souvent la perception d'une voiture si elle n'est pas correctement entraînée. Cela est encore plus fréquent les jours ensoleillés et avec des bâtiments de hauteurs différentes dans une ville, permettant aux rayons de lumière de passer à travers.

La luminosité est bonne pour la perception, mais une luminosité inégale, soudaine ou trop importante crée des problèmes de perception. Générons quelques fausses ombres.

```
def generate_shadow_coordinates(imshape, no_of_shadows=1):    vertices_list=[]    for index in range(no_of_shadows):        vertex=[]        for dimensions in range(np.random.randint(3,15)): ## Dimensionnalité du polygone d'ombre            vertex.append(( imshape[1]*np.random.uniform(),imshape[0]//3+imshape[0]*np.random.uniform()))        vertices = np.array([vertex], dtype=np.int32) ## sommets d'une seule ombre         vertices_list.append(vertices)    return vertices_list ## Liste des sommets d'ombre
```

```
def add_shadow(image,no_of_shadows=1):    image_HLS = cv2.cvtColor(image,cv2.COLOR_RGB2HLS) ## Conversion en HLS    mask = np.zeros_like(image)     imshape = image.shape    vertices_list= generate_shadow_coordinates(imshape, no_of_shadows) #3 obtenir la liste des sommets d'ombre    for vertices in vertices_list:         cv2.fillPoly(mask, vertices, 255) ## ajout de tous les polygones d'ombre sur le masque vide, 255 seul indique uniquement le canal rouge        image_HLS[:,:,1][mask[:,:,0]==255] = image_HLS[:,:,1][mask[:,:,0]==255]*0.5   ## si le canal rouge est chaud, la luminosité du canal "Luminosité" de l'image est réduite     image_RGB = cv2.cvtColor(image_HLS,cv2.COLOR_HLS2RGB) ## Conversion en RGB    return image_RGB
```

La fonction `fillPoly()` d'OpenCV est vraiment pratique dans ce cas. Créons quelques sommets aléatoires et imposons le polygone sur un masque vide en utilisant `fillPoly()`. Une fois cela fait, la seule chose restante à faire est de vérifier le masque pour les pixels chauds et de réduire la "Luminosité" dans l'image HLS partout où ces pixels chauds sont trouvés.

![Image](https://cdn-media-1.freecodecamp.org/images/uUsWjNO5bi7SPGP6DsfUdmtY-onV4tblz7eG)
_Polygone d'ombre aléatoire sur la route_

### **Neige**

C'est quelque chose de nouveau. Nous nous demandons souvent comment notre véhicule se comporterait sur des routes enneigées. Une façon de tester cela est de prendre des photos de routes couvertes de neige ou de faire quelque chose sur les images pour obtenir un effet similaire. Cet effet n'est pas une alternative complète aux routes enneigées, mais c'est une approche qui vaut la peine d'être essayée.

```
def add_snow(image):    image_HLS = cv2.cvtColor(image,cv2.COLOR_RGB2HLS) ## Conversion en HLS    image_HLS = np.array(image_HLS, dtype = np.float64)     brightness_coefficient = 2.5     snow_point=140 ## augmentez cela pour plus de neige    image_HLS[:,:,1][image_HLS[:,:,1]<snow_point] = image_HLS[:,:,1][image_HLS[:,:,1]<snow_point]*brightness_coefficient ## met à l'échelle les valeurs de pixels vers le haut pour le canal 1 (Luminosité)    image_HLS[:,:,1][image_HLS[:,:,1]>255]  = 255 ## Définit toutes les valeurs supérieures à 255 à 255    image_HLS = np.array(image_HLS, dtype = np.uint8)    image_RGB = cv2.cvtColor(image_HLS,cv2.COLOR_HLS2RGB) ## Conversion en RGB    return image_RGB
```

Oui ! C'est tout. Ce code blanchit généralement les parties les plus sombres de l'image, qui sont principalement des routes, des arbres, des montagnes et d'autres caractéristiques du paysage, en utilisant la même méthode d'augmentation de la "Luminosité" HLS utilisée dans les autres approches ci-dessus. Cette technique ne fonctionne pas bien pour les images sombres, mais vous pouvez la modifier pour qu'elle le fasse. Voici ce que vous obtenez :

![Image](https://cdn-media-1.freecodecamp.org/images/6ZAXeTp2IK9QmJN8f9hUTqwrVMWNbVuOSANj)
_l'hiver est là_

Vous pouvez ajuster certains paramètres dans le code pour plus ou moins de neige que cela. J'ai testé cela sur d'autres images aussi, et cette technique me donne des frissons.

### **Pluie**

Oui, vous avez bien entendu. Pourquoi pas la pluie ? Lorsque les humains éprouvent des difficultés à conduire sous la pluie, pourquoi les véhicules devraient-ils en être épargnés ? En fait, c'est l'une des situations pour lesquelles je veux que ma voiture autonome soit le plus entraînée. Les routes glissantes et les visions floues sont risquées, et les voitures doivent savoir comment les gérer.

```
def generate_random_lines(imshape,slant,drop_length):    drops=[]    for i in range(1500): ## Si vous voulez une pluie intense, essayez d'augmenter cela        if slant<0:            x= np.random.randint(slant,imshape[1])        else:            x= np.random.randint(0,imshape[1]-slant)        y= np.random.randint(0,imshape[0]-drop_length)        drops.append((x,y))    return drops            def add_rain(image):        imshape = image.shape    slant_extreme=10    slant= np.random.randint(-slant_extreme,slant_extreme)     drop_length=20    drop_width=2    drop_color=(200,200,200) ## une nuance de gris    rain_drops= generate_random_lines(imshape,slant,drop_length)        for rain_drop in rain_drops:        cv2.line(image,(rain_drop[0],rain_drop[1]),(rain_drop[0]+slant,rain_drop[1]+drop_length),drop_color,drop_width)    image= cv2.blur(image,(7,7)) ## les vues pluvieuses sont floues        brightness_coefficient = 0.7 ## les jours de pluie sont généralement ombragés     image_HLS = cv2.cvtColor(image,cv2.COLOR_RGB2HLS) ## Conversion en HLS    image_HLS[:,:,1] = image_HLS[:,:,1]*brightness_coefficient ## met à l'échelle les valeurs de pixels vers le bas pour le canal 1 (Luminosité)    image_RGB = cv2.cvtColor(image_HLS,cv2.COLOR_HLS2RGB) ## Conversion en RGB    return image_RGB
```

Ce que j'ai fait ici, c'est que j'ai à nouveau généré des points aléatoires sur toute l'image, puis utilisé la fonction `line()` d'OpenCV pour générer de petites lignes sur toute l'image. J'ai également utilisé une inclinaison aléatoire dans les gouttes de pluie pour avoir une sensation de pluie réelle. J'ai également réduit la luminosité de l'image car les jours de pluie sont généralement ombragés, et aussi flous à cause de la pluie. Vous pouvez changer la dimension de votre filtre de flou et le nombre de gouttes de pluie pour l'effet désiré.

Voici le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/buoiIOE1acHFNb6-nFEqEMGH7Tlq7fE82mEV)
_Fausse pluie mais pas beaucoup de flou_

### **Brouillard**

C'est encore un autre scénario qui entrave beaucoup la vision d'une voiture autonome. Des flocons blancs flous dans l'image rendent très difficile de voir au-delà d'un certain étirement et réduisent la netteté de l'image.

L'intensité du brouillard est un paramètre important pour entraîner une voiture sur la quantité de gaz à donner. Pour coder une telle fonction, vous pouvez prendre des patches aléatoires de toute l'image, et augmenter la luminosité de l'image dans ces patches. Avec un simple flou, cela donne un bel effet brumeux.

```
def add_blur(image, x,y,hw):    image[y:y+hw, x:x+hw,1] = image[y:y+hw, x:x+hw,1]+1    image[:,:,1][image[:,:,1]>255]  = 255 ## Définit toutes les valeurs supérieures à 255 à 255    image[y:y+hw, x:x+hw,1] = cv2.blur(image[y:y+hw, x:x+hw,1] ,(10,10))    return image
```

```
def generate_random_blur_coordinates(imshape,hw):    blur_points=[]    midx= imshape[1]//2-hw-100    midy= imshape[0]//2-hw-100    index=1    while(midx>-100 or midy>-100): ## génération radiale des coordonnées        for i in range(250*index):            x= np.random.randint(midx,imshape[1]-midx-hw)            y= np.random.randint(midy,imshape[0]-midy-hw)            blur_points.append((x,y))        midx-=250*imshape[1]//sum(imshape)        midy-=250*imshape[0]//sum(imshape)        index+=1    return blur_points    def add_fog(image):    image_HLS = cv2.cvtColor(image,cv2.COLOR_RGB2HLS) ## Conversion en HLS    mask = np.zeros_like(image)     imshape = image.shape    hw=100    image_HLS[:,:,1]=image_HLS[:,:,1]*0.8    haze_list= generate_random_blur_coordinates(imshape,hw)    for haze_points in haze_list:         image_HLS[:,:,1][image_HLS[:,:,1]>255]  = 255 ## Définit toutes les valeurs supérieures à 255 à 255        image_HLS= add_blur(image_HLS, haze_points[0],haze_points[1], hw) ## ajout de tous les polygones d'ombre sur le masque vide, 255 seul indique uniquement le canal rouge    image_RGB = cv2.cvtColor(image_HLS,cv2.COLOR_HLS2RGB) ## Conversion en RGB    return image_RGB
```

Coder cela a été le plus difficile de toutes les fonctions ci-dessus. J'ai essayé une approche radiale pour générer des patches ici. Puisque par un jour de brouillard, généralement la plupart du brouillard est à l'extrémité éloignée de la route et à mesure que nous approchons, la vision se dégage.

![Image](https://cdn-media-1.freecodecamp.org/images/Wb0JBy40QWvfm65-n0GHn24MOBHXnSrPRRzt)
_Autoroute brumeuse_

C'est une tâche vraiment difficile pour une machine de détecter les voitures et les voies à proximité dans une telle condition brumeuse, et c'est une bonne façon d'entraîner et de tester la robustesse du modèle de conduite.

### Pluie torrentielle

J'ai pensé à améliorer un peu la partie pluie en combinant brouillard et pluie. Comme il y a toujours un peu de brume pendant les pluies et c'est bon d'entraîner la voiture pour cela aussi. Aucune nouvelle fonction n'est requise pour cela. Nous pouvons obtenir l'effet en appelant les deux séquentiellement.

![Image](https://cdn-media-1.freecodecamp.org/images/MzAyhI05YhGfg9hN7Adb-40MM2iZ3pCtqvtn)

La voiture à droite est à peine visible sur cette image, et c'est un scénario du monde réel. Nous pouvons à peine distinguer quoi que ce soit sur la route sous une pluie battante.

J'espère que cet article vous aidera à entraîner le modèle dans diverses conditions météorologiques. Pour mon code complet, vous pouvez visiter mon [profil GitHub](https://github.com/UjjwalSaxena). Et j'ai écrit beaucoup d'autres articles, que vous pouvez lire sur [Medium](https://medium.com/@er.ujjwalsaxena) et sur mon [site WordPress](https://erujjwalsaxena.wordpress.com/).

Profitez-en !