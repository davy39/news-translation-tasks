---
title: Reconnaissance des feux de signalisation avec l'apprentissage profond
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-12T15:53:20.000Z'
originalURL: https://freecodecamp.org/news/recognizing-traffic-lights-with-deep-learning-23dae23287cc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*X7aV0pK2krETntjlmIxQhg.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: self-driving cars
  slug: self-driving-cars
seo_title: Reconnaissance des feux de signalisation avec l'apprentissage profond
seo_desc: 'By David Brailovsky

  How I learned deep learning in 10 weeks and won $5,000


  I recently won first place in the Nexar Traffic Light Recognition Challenge, computer
  vision competition organized by a company that’s building an AI dash cam app.

  In this po...'
---

Par David Brailovsky

#### Comment j'ai appris l'apprentissage profond en 10 semaines et gagné 5 000 $

![Image](https://cdn-media-1.freecodecamp.org/images/w1rKRdS-MznDPLqurd098N0RP8Y8A-2BKjzO)

J'ai récemment remporté la première place du [Nexar Traffic Light Recognition Challenge](https://challenge.getnexar.com/challenge-1), une compétition de vision par ordinateur organisée par une entreprise qui développe une application de caméra de bord basée sur l'IA.

Dans cet article, je vais décrire la solution que j'ai utilisée. J'explorerai également les approches qui ont fonctionné et celles qui n'ont pas fonctionné dans mes efforts pour améliorer mon modèle.

Ne vous inquiétez pas — vous n'avez pas besoin d'être un expert en IA pour comprendre cet article. Je me concentrerai sur les idées et les méthodes que j'ai utilisées plutôt que sur l'implémentation technique.

![Image](https://cdn-media-1.freecodecamp.org/images/gGdsB4CeozhR1HEoQz6CKkhAKJzDnEla9OSY)
_Démonstration d'un classificateur basé sur l'apprentissage profond pour la reconnaissance des feux de signalisation_

### Le défi

L'objectif du défi était de reconnaître l'état des feux de signalisation dans les images prises par les conducteurs utilisant l'application Nexar. Dans n'importe quelle image donnée, le classificateur devait indiquer s'il y avait un feu de signalisation dans la scène, et s'il était rouge ou vert. Plus précisément, il devait uniquement identifier les feux de signalisation dans la direction de conduite.

Voici quelques exemples pour clarifier :

![Image](https://cdn-media-1.freecodecamp.org/images/uMBGy8ksr1LYDX58wPHBez6CWlKjQcwBtllz)

![Image](https://cdn-media-1.freecodecamp.org/images/lcrIwmOWIMFAagY2r-rO6jukAF2FKX1vuRwN)

![Image](https://cdn-media-1.freecodecamp.org/images/7Z5Bs3bddQK0viGK4ZcR1rnh3CU1W5q4hqeO)
_Source : [Nexar challenge](https://challenge.getnexar.com/challenge-1" rel="noopener" target="_blank" title=")_

Les images ci-dessus sont des exemples des trois classes possibles que je devais prédire : pas de feu de signalisation (à gauche), feu rouge (au centre) et feu vert (à droite).

Le défi exigeait que la solution soit basée sur les [Convolutional Neural Networks](https://en.wikipedia.org/wiki/Convolutional_neural_network), une méthode très populaire utilisée dans la reconnaissance d'images avec des réseaux de neurones profonds. Les soumissions étaient notées en fonction de la précision du modèle ainsi que de la taille du modèle (en mégaoctets). Les modèles plus petits obtenaient des scores plus élevés. De plus, la précision minimale requise pour gagner était de 95 %.

Nexar a fourni 18 659 images étiquetées comme données d'entraînement. Chaque image était étiquetée avec l'une des trois classes mentionnées ci-dessus (pas de feu de signalisation / rouge / vert).

### Logiciel et matériel

J'ai utilisé [Caffe](http://caffe.berkeleyvision.org/) pour entraîner les modèles. La principale raison pour laquelle j'ai choisi Caffe était la grande variété de modèles pré-entraînés.

Python, NumPy et Jupyter Notebook ont été utilisés pour analyser les résultats, explorer les données et exécuter des scripts ad-hoc.

Les instances GPU d'Amazon (g2.2xlarge) ont été utilisées pour entraîner les modèles. Ma facture AWS s'est élevée à **263 $** (!). Pas donné. ?

Le code et les fichiers que j'ai utilisés pour entraîner et exécuter le modèle sont disponibles sur [GitHub](https://github.com/davidbrai/deep-learning-traffic-lights).

### Le classificateur final

Le classificateur final a atteint une précision de **94,955 %** sur l'ensemble de test de Nexar, avec une taille de modèle d'environ **7,84 Mo**. À titre de comparaison, [GoogLeNet](https://arxiv.org/abs/1409.4842) utilise une taille de modèle de 41 Mo, et [VGG-16](http://www.robots.ox.ac.uk/~vgg/research/very_deep/) utilise une taille de modèle de 528 Mo.

Nexar a eu la gentillesse d'accepter 94,955 % comme 95 % pour passer l'exigence minimale ?.

Le processus d'obtention d'une précision plus élevée a impliqué beaucoup d'essais et d'erreurs. Certaines approches avaient une logique derrière elles, et d'autres étaient simplement du "peut-être que cela fonctionnera". Je vais décrire certaines des choses que j'ai essayées pour améliorer le modèle, celles qui ont fonctionné et celles qui n'ont pas aidé. Les détails du classificateur final sont décrits juste après.

### Ce qui a fonctionné ?

#### [Transfer learning](http://cs231n.github.io/transfer-learning/)

J'ai commencé par essayer d'ajuster un modèle qui avait été pré-entraîné sur ImageNet avec l'architecture [GoogLeNet](https://github.com/BVLC/caffe/tree/master/models/bvlc_googlenet). Très rapidement, cela m'a permis d'atteindre une précision de >90 % ! ?

Nexar a mentionné dans la [page du défi](https://challenge.getnexar.com/challenge-1) qu'il devrait être possible d'atteindre 93 % en ajustant GoogLeNet. Je ne suis pas exactement sûr de ce que j'ai fait de travers, je pourrais y regarder.

#### [SqueezeNet](https://arxiv.org/abs/1602.07360)

> SqueezeNet : précision de niveau AlexNet avec 50 fois moins de paramètres et une taille de modèle <0,5 Mo.

Puisque la compétition récompense les solutions qui utilisent des modèles petits, j'ai décidé dès le début de chercher un réseau compact avec aussi peu de paramètres que possible qui peut encore produire de bons résultats. La plupart des réseaux récemment publiés sont _très_ profonds et ont _beaucoup_ de paramètres. [SqueezeNet](https://arxiv.org/abs/1602.07360) semblait être un très bon choix, et il avait également un modèle pré-entraîné entraîné sur ImageNet disponible dans le [Model Zoo](https://github.com/BVLC/caffe/wiki/Model-Zoo) de [Caffe](http://caffe.berkeleyvision.org/), ce qui était pratique.

![Image](https://cdn-media-1.freecodecamp.org/images/heQAr-opHTSMqRHKQ4eevvLQfizGPmPAJkfq)
_Architecture du réseau SqueezeNet. [Slides](http://www.slideshare.net/embeddedvision/techniques-for-efficient-implementation-of-deep-neural-networks-a-presentation-from-stanford" rel="noopener" target="_blank" title=")_

Le réseau parvient à rester compact en :

* Utilisant principalement des filtres de convolution 1x1 et quelques 3x3
* Réduisant le nombre de canaux d'entrée dans les filtres 3x3

Pour plus de détails, je recommande de lire cet [article de blog](https://gab41.lab41.org/lab41-reading-group-squeezenet-9b9d1d754c75#.oprbydtxv) de Lab41 ou l'[article original](https://arxiv.org/abs/1602.07360).

Après quelques allers-retours avec l'ajustement du taux d'apprentissage, j'ai pu ajuster le modèle pré-entraîné ainsi que l'entraînement à partir de zéro avec de bons résultats de précision : 92 % ! Très cool ! ?

#### Rotation des images

![Image](https://cdn-media-1.freecodecamp.org/images/seb5umUmWtSeKYVEnJPxUFNAj7fpLIuo83oU)
_Source : Nexar_

La plupart des images étaient horizontales comme celle ci-dessus, mais environ 2,4 % étaient verticales, et avec toutes sortes de directions pour "haut". Voir ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/-ef27RhMID9q0P1-YmrTYbEVOwOzEPDPQ3Il)
_Différentes orientations des images verticales. Source : [Nexar challenge](https://challenge.getnexar.com/challenge-1" rel="noopener" target="_blank" title=")_

Bien que ce ne soit pas une grande partie de l'ensemble de données, je voulais que le modèle les classe correctement aussi.

Malheureusement, il n'y avait pas de données EXIF dans les images jpeg spécifiant l'orientation. Au début, j'ai envisagé de faire une heuristique pour identifier le ciel et retourner l'image en conséquence, mais cela ne semblait pas simple.

Au lieu de cela, j'ai essayé de rendre le modèle invariant aux rotations. Ma première tentative a été d'entraîner le réseau avec des rotations aléatoires de 0°, 90°, 180°, 270°. Cela n'a pas aidé ?. Mais lorsque j'ai fait la moyenne des prédictions de 4 rotations pour chaque image, il y a eu une amélioration !

92 % → 92,6 % ?

Pour clarifier : par "moyenne des prédictions", je veux dire la moyenne des probabilités que le modèle a produites pour chaque classe à travers les 4 variations d'image.

#### Suréchantillonnage des recadrages

Pendant l'entraînement, le réseau SqueezeNet effectuait d'abord un recadrage aléatoire sur les images d'entrée par défaut, et je ne l'ai pas changé. Ce type d'augmentation de données permet au réseau de mieux généraliser.

De même, lors de la génération des prédictions, j'ai pris plusieurs recadrages de l'image d'entrée et j'ai fait la moyenne des résultats. J'ai utilisé 5 recadrages : 4 coins et un recadrage central. L'implémentation était gratuite en utilisant le code [caffe](https://github.com/BVLC/caffe/blob/master/python/caffe/classifier.py) existant pour cela.

92 % → 92,46 % ?

La rotation des images ainsi que le suréchantillonnage des recadrages ont montré une légère amélioration.

#### Entraînement supplémentaire avec un taux d'apprentissage plus faible

Tous les modèles commençaient à surajuster après un certain point. Je l'ai remarqué en observant la perte de l'ensemble de validation commencer à augmenter à un certain moment.

![Image](https://cdn-media-1.freecodecamp.org/images/7DREKKQRtlLrsNQ87SvcoAMZH29Hh0uC3o4Z)
_Perte de validation augmentant à partir de l'itération 40 000 environ_

J'ai arrêté l'entraînement à ce moment-là parce que le modèle ne généralisait probablement plus. Cela signifiait que le taux d'apprentissage n'avait pas eu le temps de décroître jusqu'à zéro. J'ai essayé de reprendre le processus d'entraînement au point où le modèle avait commencé à surajuster avec un taux d'apprentissage 10 fois inférieur à l'original. Cela améliorait généralement la précision de 0 à 0,5 %.

#### Plus de données d'entraînement

Au début, j'ai divisé mes données en 3 ensembles : entraînement (64 %), validation (16 %) et test (20 %). Après quelques jours, j'ai pensé que renoncer à 36 % des données pouvait être trop. J'ai fusionné les ensembles d'entraînement et de validation et j'ai utilisé l'ensemble de test pour vérifier mes résultats.

J'ai réentraîné un modèle avec des "rotations d'images" et un "entraînement supplémentaire à un taux plus faible" et j'ai vu une amélioration :

92,6 % → 93,5 % ?

#### Réétiquetage des erreurs dans les données d'entraînement

Lors de l'analyse des erreurs que le classificateur avait sur l'ensemble de validation, j'ai remarqué que certaines des erreurs avaient une confiance très élevée. En d'autres termes, le modèle est certain qu'il s'agit d'une chose (par exemple, feu vert) tandis que les données d'entraînement disent autre chose (par exemple, feu rouge).

![Image](https://cdn-media-1.freecodecamp.org/images/7ONBYOL6Nz1GJP7IbUjHkHta-NuhLVvWm0H8)

Remarquez que dans le graphique ci-dessus, la barre la plus à droite est assez haute. Cela signifie qu'il y a un grand nombre d'erreurs avec une confiance >95 %. En examinant ces cas de près, j'ai vu qu'il s'agissait généralement d'erreurs dans la vérité terrain de l'ensemble d'entraînement plutôt que dans le modèle entraîné.

J'ai décidé de corriger ces erreurs dans l'ensemble d'entraînement. Le raisonnement était que ces erreurs confondent le modèle, rendant plus difficile pour lui de généraliser. Même si l'ensemble de test final contient des erreurs dans la vérité terrain, un modèle plus généralisé a une meilleure chance d'avoir une précision élevée sur toutes les images.

J'ai étiqueté manuellement 709 images que l'un de mes modèles avait mal classées. Cela a changé la vérité terrain pour 337 des 709 images. Cela a pris environ une heure de travail manuel avec un [script python](https://github.com/davidbrai/deep-learning-traffic-lights/blob/14749dacf75318842f45fc5a9900c300eb83755f/analysis/label_misses.py) pour m'aider à être efficace.

![Image](https://cdn-media-1.freecodecamp.org/images/znnZb0xzwDNsGkEL1mQchvZW3UKmKhX7g0jQ)

Ci-dessus se trouve le même graphique après le réétiquetage et le réentraînement du modèle. Cela semble mieux !

Cela a amélioré le modèle précédent de :

93,5 % → 94,1 % 

#### Ensemble de modèles

L'utilisation de plusieurs modèles ensemble et la moyenne de leurs résultats ont également amélioré la précision. J'ai expérimenté avec différents types de modifications dans le processus d'entraînement des modèles impliqués dans l'ensemble. Une amélioration notable a été obtenue en utilisant un modèle entraîné à partir de zéro même s'il avait une précision inférieure à celle des modèles qui avaient été ajustés sur des modèles pré-entraînés. Peut-être que cela est dû au fait que ce modèle a appris différentes caractéristiques de celles qui avaient été ajustées sur des modèles pré-entraînés.

L'ensemble a utilisé 3 modèles avec des précisions de 94,1 %, 94,2 % et 92,9 % et ensemble a obtenu une précision de 94,8 %. ?

### Ce qui n'a pas fonctionné ?

Beaucoup de choses ! ? Espérons que certaines de ces idées pourront être utiles dans d'autres contextes.

#### Lutte contre le surajustement

En essayant de traiter le surajustement, j'ai essayé plusieurs choses, aucune n'a produit d'améliorations significatives :

* augmenter le ratio de dropout dans le réseau
* plus d'augmentation de données (déplacements aléatoires, zooms, distorsions)
* entraînement sur plus de données : utiliser une division 90/10 au lieu de 80/20

#### Équilibrage de l'ensemble de données

L'ensemble de données n'était pas très équilibré :

* 19 % des images étaient étiquetées sans feu de signalisation
* 53 % feu rouge
* 28 % feu vert.

J'ai essayé d'équilibrer l'ensemble de données en suréchantillonnant les classes moins courantes, mais je n'ai pas remarqué d'amélioration.

#### Séparation jour et nuit

Mon intuition était que la reconnaissance des feux de signalisation en plein jour et la nuit est très différente. Je pensais peut-être pouvoir aider le modèle en le séparant en deux problèmes plus simples.

Il était assez facile de séparer les images en jour et nuit en regardant leur intensité moyenne de pixel :

![Image](https://cdn-media-1.freecodecamp.org/images/cqz5z5omsUOd44Fs0gGvffsVkkzM5VCrBx4u)

Vous pouvez voir une séparation très naturelle des images avec des valeurs moyennes faibles, c'est-à-dire des images sombres, prises la nuit, et des images claires, prises le jour.

J'ai essayé deux approches, aucune n'a amélioré les résultats :

* Entraîner deux modèles séparés pour les images de jour et les images de nuit
* Entraîner le réseau à prédire 6 classes au lieu de 3 en prédisant également s'il fait jour ou nuit

#### Utilisation de meilleures variantes de SqueezeNet

J'ai expérimenté un peu avec deux variantes améliorées de SqueezeNet. La première utilisait des [connexions résiduelles](https://github.com/songhan/SqueezeNet-Residual) et la seconde était entraînée avec un entraînement [dense→sparse→dense](https://github.com/songhan/SqueezeNet-DSD-Training) (plus de détails dans l'article). Pas de chance. ?

#### Localisation des feux de signalisation

Après avoir lu un excellent [article](http://deepsense.io/deep-learning-right-whale-recognition-kaggle/) de deepsense.io sur la façon dont ils ont gagné le défi de reconnaissance des baleines, j'ai essayé d'entraîner un localisateur, c'est-à-dire identifier l'emplacement du feu de signalisation dans l'image d'abord, puis identifier l'état du feu de signalisation sur une petite région de l'image.

J'ai utilisé [sloth](http://sloth.readthedocs.io/en/latest/) pour annoter environ 2 000 images, ce qui a pris quelques heures. En essayant d'entraîner un modèle, il surajustait très rapidement, probablement parce qu'il n'y avait pas assez de données étiquetées. Peut-être que cela pourrait fonctionner si j'avais annoté beaucoup plus d'images.

#### Entraînement d'un classificateur sur les cas difficiles

J'ai choisi 30 % des images "plus difficiles" en sélectionnant les images pour lesquelles mon classificateur était moins de 97 % confiant. J'ai ensuite essayé d'entraîner un classificateur uniquement sur ces images. Aucune amélioration. ?

#### Algorithme d'optimisation différent

J'ai expérimenté très brièvement avec l'utilisation du solveur Adam de Caffe au lieu de SGD avec un taux d'apprentissage décroissant linéairement, mais je n'ai pas vu d'amélioration. ?

#### Ajout de plus de modèles à l'ensemble

Puisque la méthode d'ensemble s'est avérée utile, j'ai essayé de doubler. J'ai essayé de changer différents paramètres pour produire différents modèles et les ajouter à l'ensemble : graine initiale, taux de dropout, différentes données d'entraînement (division différente), point de contrôle différent dans l'entraînement. Aucun de ceux-ci n'a apporté d'amélioration significative. ?

### Détails du classificateur final

Le classificateur utilise un ensemble de 3 réseaux entraînés séparément. Une moyenne pondérée des probabilités qu'ils donnent à chaque classe est utilisée comme sortie. Les trois réseaux utilisaient le réseau [SqueezeNet](https://arxiv.org/abs/1602.07360), mais chacun a été entraîné différemment.

#### Modèle #1 — Réseau pré-entraîné avec suréchantillonnage

Entraîné sur l'ensemble d'entraînement réétiqueté (après correction des erreurs de vérité terrain). Le modèle a été ajusté sur la base d'un modèle pré-entraîné de SqueezeNet entraîné sur ImageNet.

Augmentation des données pendant l'entraînement :

* Miroir horizontal aléatoire
* Recadrage aléatoire de patches de taille 227 x 227 avant de les alimenter dans le réseau

Au moment du test, les prédictions de 10 variations de chaque image ont été moyennées pour calculer la prédiction finale. Les 10 variations étaient composées de :

* 5 recadrages de taille 227 x 227 : 1 pour chaque coin et 1 au centre de l'image
* pour chaque recadrage, une version miroitée horizontalement a également été utilisée

Précision du modèle sur l'ensemble de validation : 94,21 %  
Taille du modèle : ~2,6 Mo

#### Modèle #2 — Ajout d'invariance de rotation

Très similaire au Modèle #1, avec l'ajout de rotations d'images. Pendant le temps d'entraînement, les images étaient tournées aléatoirement de 90°, 180°, 270° ou pas du tout. Au moment du test, chacune des 10 variations décrites dans le Modèle #1 a créé trois autres variations en la tournant de 90°, 180° et 270°. Un total de 40 variations ont été classées par notre modèle et moyennées ensemble.

Précision du modèle sur l'ensemble de validation : 94,1 %  
Taille du modèle : ~2,6 Mo

#### Modèle #3 — Entraîné à partir de zéro

Ce modèle n'a pas été ajusté, mais plutôt _entraîné à partir de zéro_. La logique derrière cela était que même s'il atteint une précision inférieure, il apprend différentes caractéristiques sur l'ensemble d'entraînement que les deux modèles précédents, ce qui pourrait être utile lorsqu'il est utilisé dans un ensemble.

L'augmentation des données pendant l'entraînement et les tests est la même que pour le Modèle #1 : miroir et recadrage.

Précision du modèle sur l'ensemble de validation : 92,92 %  
Taille du modèle : ~2,6 Mo

#### Combinaison des modèles ensemble

Chaque modèle a produit trois valeurs, représentant la probabilité que l'image appartienne à chacune des trois classes. Nous avons moyenné leurs sorties avec les poids suivants :

* Modèle #1 : 0,28
* Modèle #2 : 0,49
* Modèle #3 : 0,23

Les valeurs des poids ont été trouvées en effectuant une recherche par grille sur les valeurs possibles et en les testant sur l'ensemble de validation. Elles sont probablement un peu surajustées à l'ensemble de validation, mais peut-être pas trop puisque c'est une opération très simple.

Précision du modèle sur l'ensemble de validation : 94,83 %  
Taille du modèle : ~7,84 Mo  
Précision du modèle sur l'ensemble de test de Nexar : 94,955 % ?

#### Exemples d'erreurs du modèle

![Image](https://cdn-media-1.freecodecamp.org/images/NEEbzZb45ZlZuRb33-lG1Xik4OTePSa8cCXs)
_Source : Nexar_

Le point vert dans le palmier produit par le reflet a probablement fait que le modèle a prédit par erreur qu'il y avait un feu vert.

![Image](https://cdn-media-1.freecodecamp.org/images/nIcOpLXRNdp5Nef8TDaXIBUumhs1sVHSZBXP)
_Source : Nexar_

Le modèle a prédit rouge au lieu de vert. Cas délicat lorsqu'il y a plus d'un feu de signalisation dans la scène.

![Image](https://cdn-media-1.freecodecamp.org/images/j8TesyVpgHE2GCrzw5qT5wWJ63yB1tc5N071)

Le modèle a dit qu'il n'y avait pas de feu de signalisation alors qu'il y avait un feu vert devant.

### Conclusion

C'était la première fois que j'appliquais l'apprentissage profond à un problème réel ! J'étais heureux de voir que cela fonctionnait si bien. J'ai appris BEAUCOUP pendant le processus et je vais probablement écrire un autre article qui, je l'espère, aidera les nouveaux venus à perdre moins de temps sur certaines des erreurs et des défis techniques que j'ai eus.

Je tiens à remercier Nexar pour avoir fourni ce grand défi et j'espère qu'ils en organiseront d'autres à l'avenir ! ?

_Si vous avez aimé lire cet article, veuillez le **partager sur les réseaux sociaux !**_

_Je serais ravi de recevoir vos commentaires et questions ci-dessous !_