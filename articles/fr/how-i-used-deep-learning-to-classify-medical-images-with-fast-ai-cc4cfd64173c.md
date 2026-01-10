---
title: Comment j'ai utilisé le Deep Learning pour classer des images médicales avec
  Fast.ai
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-27T16:53:26.000Z'
originalURL: https://freecodecamp.org/news/how-i-used-deep-learning-to-classify-medical-images-with-fast-ai-cc4cfd64173c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vyFlFjwlsfV7DX3kBDXJPQ.png
tags:
- name: AI
  slug: ai
- name: Deep Learning
  slug: deep-learning
- name: 'fastai, '
  slug: fastai
- name: Machine Learning
  slug: machine-learning
- name: 'tech '
  slug: tech
seo_title: Comment j'ai utilisé le Deep Learning pour classer des images médicales
  avec Fast.ai
seo_desc: 'By James Dietle

  Convolutional Neural Networks (CNNs) have rapidly advanced the last two years helping
  with medical image classification. How can we, even as hobbyists, take these recent
  advances and apply them to new datasets? We are going to walk th...'
---

Par James Dietle

Les réseaux de neurones convolutifs (CNN) ont rapidement progressé ces deux dernières années, aidant à la classification des images médicales. Comment pouvons-nous, même en tant qu'amateurs, prendre ces avancées récentes et les appliquer à de nouveaux ensembles de données ? Nous allons passer en revue le processus, et c'est surprenant plus accessible que vous ne le pensez.

Alors que notre famille déménageait à Omaha, ma femme (qui est en fellowship de gastro-entérologie pédiatrique) est rentrée à la maison et a dit qu'elle voulait utiliser la classification d'images pour ses recherches.

Oh, j'étais tellement prêt.

Depuis plus de deux ans, je m'amuse avec le deep learning en tant que hobby. J'ai même écrit plusieurs articles ([ici](https://medium.com/@JamesDietle/part-of-the-fun-of-learning-data-science-is-seeing-how-quickly-it-can-relate-to-your-usual-roles-ceb7b0ff5f13) et [ici](https://medium.com/@JamesDietle/9-months-in-the-hobby-of-deep-learning-d688cce4fa2e)). Maintenant, j'avais une direction pour un problème. Malheureusement, je n'avais aucune idée de quoi que ce soit dans le tractus gastro-intestinal, et ma femme n'avait pas programmé depuis le lycée.

### **Commencez par le début**

Tout mon parcours dans le deep learning s'est fait par le biais du processus [Fast.ai](https://www.fast.ai/). Cela a commencé il y a 2 ans lorsque j'essayais de valider que tout l'IA et le Machine Learning que nous utilisions dans le domaine de la sécurité n'étaient pas surévalués ou biaisés. C'était le cas, et nous avons évité ces technologies. Le fait le plus sobre était d'apprendre que devenir un expert dans le domaine nécessite un peu d'expérimentation.

#### **Installation**

J'ai utilisé Fast.ai pour toutes les étapes, et la nouvelle version rend cela plus simple que jamais. Les moyens de créer votre environnement d'apprentissage se multiplient rapidement. Il existe maintenant des images docker, des amis Amazon et des services (comme [Crestle](https://www.crestle.com/)) qui rendent la configuration plus facile que jamais.

Que vous soyez le plus novice des débutants en codage ou un ninja expérimenté, [commencez ici](https://course.fast.ai/) sur le site web de Fast.ai.

J'ai choisi de construire ma machine d'apprentissage lors d'une itération précédente du cours. Cependant, ce n'est pas nécessaire, et je recommanderais d'utiliser un autre service à la place. Choisissez la voie la plus facile pour vous et commencez à expérimenter.

#### **Changements dans Fast.ai avec la version 3**

J'ai suivi les autres itérations de Fast.ai, et après avoir examiné le nouveau cours, j'ai remarqué à quel point tout était plus simple dans le notebook. La documentation et les exemples sont partout.

Plongeons dans [lesson1-pets](https://github.com/fastai/course-v3/blob/master/nbs/dl1/lesson1-pets.ipynb), et si vous avez configuré Fast.ai, n'hésitez pas à suivre dans votre instance personnelle de jupyter.

![Image](https://cdn-media-1.freecodecamp.org/images/u7vNdhatx2eygqg8w4IUCXuZGZuRHIx2y4f5)
_lesson1-pets de Fast.ai_

Je me suis préparé pour la première leçon (définissant généralement entre 2 classes — chats et chiens — comme je l'avais fait plusieurs fois auparavant. Cependant, j'ai vu cette fois que nous faisions quelque chose de beaucoup plus complexe concernant 33 races de chats et de chiens en utilisant moins de lignes de code.

**Le CNN était opérationnel et apprenait en 7 lignes de code !!**

Ce n'était pas le seul changement significatif. Un autre grand pas en avant était dans l'affichage des erreurs. Par exemple, nous pouvions rapidement voir un ensemble des principales pertes (éléments que nous avions prédits de manière erronée avec confiance) et les images de chiens et de chats correspondantes de notre ensemble de données ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/KWKmlZf52x6jVJPZDmtUMITcbqCbHl54Tjwh)
_Prédictions incorrectes de races de chats et de chiens_

Cette fonction était principalement un contrôle ponctuel pour les mauvaises données. S'assurer qu'un lion, un tigre ou un ours ne s'était pas glissé dans l'ensemble. Nous pouvions également voir s'il y avait des erreurs flagrantes qui étaient évidentes pour nous.

La matrice de confusion était encore plus bénéfique pour moi. Elle m'a permis de regarder l'ensemble des données pour des motifs de mauvaise classification entre les 33 races.

![Image](https://cdn-media-1.freecodecamp.org/images/sfF1pvbZpjjbu3n6GjRMuRaUbQxHAMg-jeTm)

Parmi les 33 races présentées, nous pouvions voir où nos données divergeaient et nous demander si cela avait du sens. Quelques races se sont distinguées en particulier, et voici des exemples d'images souvent confondues :

![Image](https://cdn-media-1.freecodecamp.org/images/59yz56xv0LGDuWt8T1iQuqWRP-lE74eJqUkK)
_Terrier de Staffordshire et terrier américain._

![Image](https://cdn-media-1.freecodecamp.org/images/8vnEnaLgEN6Dm9I6AeIzYzxD3-4MbV36UYMt)
_Mau égyptien et Bengal_

N'étant ni propriétaire ni passionné d'animaux, je n'aurais pas pu distinguer ces détails subtils sur les caractéristiques subtiles d'une race. Le modèle fait un bien meilleur travail que je n'aurais pu le faire ! Bien que je reçoive certainement des réponses, je suis également curieux de trouver cette caractéristique manquante ou ce morceau de données pour améliorer le modèle.

Il y a un avertissement important. Nous en sommes maintenant au point où le modèle nous enseigne sur les données. Parfois, nous pouvons nous retrouver dans un état d'esprit où la sortie est la fin du processus. Si nous tombons dans ce piège, nous pourrions manquer une opportunité fantastique de créer une boucle de rétroaction positive.

![Image](https://cdn-media-1.freecodecamp.org/images/2YFbSBKXrC8F4-AZn65WWIiJQ7rLnHkoAOBW)
_Dessin Powerpoint de 30 secondes_

Par conséquent, nous sommes un peu plus sages et un peu plus confiants dans la 4ème phase. Étant donné ces données, quelles décisions devrais-je prendre pour améliorer la précision ?

* Plus d'entraînement
* Plus d'images
* Une architecture plus puissante

Question piège ! Je vais regarder un ensemble de données différent. Approchons-nous des images d'endoscope de l'intérieur des gens.

### **Obtenez l'ensemble de données, voyez beaucoup de choses**

Pour toute personne intéressée par la gastro-entérologie, je recommande de consulter [The Kvasir Dataset](https://datasets.simula.no/kvasir/#data-collection). Une bonne description de leur site est :

> l'ensemble de données contenant des images de l'intérieur du tractus gastro-intestinal (GI). La collection d'images est classée en trois repères anatomiques importants et trois résultats cliniquement significatifs. De plus, il contient deux catégories d'images liées à l'ablation de polypes endoscopiques. Le tri et l'annotation de l'ensemble de données sont effectués par des médecins (endoscopistes expérimentés)

Il y a aussi un [article de recherche](https://www.researchgate.net/publication/316215961_KVASIR_A_Multi-Class_Image_Dataset_for_Computer_Aided_Gastrointestinal_Disease_Detection) par des experts (Pogorelov et al.) décrivant comment ils ont abordé le problème, y compris leurs résultats.

Parfait, c'est un excellent ensemble de données pour passer des animaux aux humains. Bien qu'il soit moins mignon (et inclut également des échantillons de selles), c'est quelque chose d'excitant et complet.

Alors que nous téléchargeons les données, la première chose que nous remarquons est qu'il y a 8 classes dans cet ensemble de données à classer au lieu des 33 précédentes. Cependant, cela ne devrait pas changer aucune de nos autres opérations.

![Image](https://cdn-media-1.freecodecamp.org/images/uo1ea2vqjqGnAJwIXtSBKnHIjWhRJrXi0LXx)

_Note de côté : À l'origine, j'ai passé quelques heures à scripter comment déplacer des dossiers dans des dossiers de validation, et j'ai passé un bon moment à tout configurer. L'effort de script s'est avéré être une perte de temps car il existe déjà une fonction simple pour créer un ensemble de validation._

_La leçon est « si quelque chose est pénible, il y a de fortes chances que quelqu'un de la communauté Fast.ai l'ait déjà codé pour vous. »_

### Plongeons dans le notebook

_Vous pouvez récupérer mon notebook Jupyter depuis [GitHub ici](https://github.com/jamesdietle/fastaipart3/blob/master/Kvasir-Dataset2.ipynb)._

#### **Construire pour la vitesse et l'expérimentation**

Alors que nous commençons à expérimenter, il est crucial d'obtenir le cadre correct. Essayez de configurer le minimum nécessaire pour le faire fonctionner et qui peut être mis à l'échelle plus tard. Assurez-vous que les données sont prises en charge, traitées et fournissent des sorties qui ont du sens.

Cela signifie :

* Utiliser des lots plus petits
* Utiliser un nombre inférieur d'époques
* Limiter les transformations

Si une exécution prend plus de 2 minutes, trouvez un moyen d'aller plus vite. Une fois que tout est en place, nous pouvons devenir fous.

#### Gestion des données

La priorisation, l'organisation, le toilettage et la gestion des données sont les aspects les plus importants du deep learning. Voici une image brute montrant comment la gestion des données se produit, ou vous pouvez lire la [documentation](https://docs.fast.ai/basic_data.html).

![Image](https://cdn-media-1.freecodecamp.org/images/Ni-fwUCcGWDAXcUlCqgVl8Epvi13uUqUHVwl)

Par conséquent, nous devons faire la même chose pour les données d'endoscope, et c'est une ligne de code.

![Image](https://cdn-media-1.freecodecamp.org/images/JtZ6HKXcNXHZbxTGaFNOaMEnI8zVSJeF4dgS)

Explication des variables :

* Path pointe vers nos données (#1)
* L'ensemble de validation à 20 % pour créer correctement des dataloaders
* transformations par défaut
* la taille de l'image définie à 224

C'est tout ! Le bloc de données est entièrement configuré et prêt pour la phase suivante.

#### Resnet

Nous avons des données et nous devons décider d'une architecture. De nos jours, Resnet est couramment utilisé pour la classification d'images. Il a un nombre après lui qui équivaut au nombre de couches. De nombreux [meilleurs articles](https://medium.com/@14prakash/understanding-and-implementing-architectures-of-resnet-and-resnext-for-state-of-the-art-image-cf51669e1624) existent [sur Resnet](https://medium.com/@14prakash/image-classification-architectures-review-d8b95075998f), donc, pour simplifier pour cet article :

> Plus de couches = plus précis (Hourra !)

> Plus de couches = plus de calcul et de temps nécessaires (Bof..)

Par conséquent, Resnet34 a 34 couches de détection d'images.

#### Prêt ? Je suis prêt !

Avec les données structurées, l'architecture et une métrique d'erreur par défaut, nous avons tout ce dont nous avons besoin pour que l'apprenant commence à s'ajuster.

Regardons un peu de code :

![Image](https://cdn-media-1.freecodecamp.org/images/Y-uV2EnLty823Yv1yMquSiR2aRgacmKyd1ck)

Nous voyons qu'après les cycles et 7 minutes, nous obtenons une précision de 87 %. Pas mal. Pas mal du tout.

N'étant pas médecin, j'ai un œil très non entraîné en regardant ces images. Je n'ai aucune idée de ce qu'il faut chercher, des erreurs de catégorisation, ou si les données sont bonnes. Je suis donc allé directement à la matrice de confusion pour voir où les erreurs étaient commises.

![Image](https://cdn-media-1.freecodecamp.org/images/EVJNURCQyxNtY8JnWDo7gQ-nbpxjG5P04ow2)

Parmi les 8 classes, 2 ensembles de 2 sont souvent confondus l'un avec l'autre. En tant que référence, je pouvais seulement voir s'ils sont teints, des polypes, ou autre chose. Donc, comparé à ma référence personnelle de 30 % de précision, la machine obtient un incroyable 87 %.

Après avoir regardé les images de ces 2 ensembles côte à côte, vous pouvez voir pourquoi. (Puisqu'il s'agit d'images médicales, elles pourraient être NSFW et sont présentes dans le notebook Jupyter.)

1. Les sections teintes sont confondues les unes avec les autres. Ce type d'erreur peut être attendu. Elles sont toutes les deux bleues et se ressemblent beaucoup.
2. L'œsophagite est difficile à distinguer d'une ligne Z normale. Peut-être que l'œsophagite se présente plus rouge que la ligne Z ? Je n'en suis pas certain.

Quoi qu'il en soit, tout semble bien, et nous devons améliorer notre jeu.

### Plus de couches, plus d'images, plus de puissance !

Maintenant que nous voyons notre modèle super rapide fonctionner, passons à la puissance.

* J'ai augmenté la taille de l'ensemble de données de v1 à v2. Le plus grand ensemble double le nombre d'images disponibles, passant de 4000 à 8000. _(Note : Tous les exemples de cet article montrent v2.)_
* Transformez tout ce qui a du sens. Il y a beaucoup de choses que vous pouvez ajuster. Nous allons approfondir cela sous peu.
* Comme les images de l'ensemble de données sont relativement grandes, j'ai décidé d'essayer de les agrandir. Bien que cela soit plus lent, j'étais curieux de savoir si cela permettrait de mieux distinguer les petits détails. Cette hypothèse nécessite encore quelques expérimentations.
* De plus en plus d'époques.
* Si vous vous souvenez, Resnet50 aurait plus de couches (serait plus précis) mais nécessiterait plus de temps de calcul et serait donc plus lent. Nous allons donc changer le modèle de Resnet34 à Resnet50.

#### **Transformations : Tirer le meilleur parti d'une image**

Les transformations d'images sont un excellent moyen d'améliorer la précision. Si nous apportons des changements aléatoires à une image (rotation, changement de couleur, retournement, etc.), nous pouvons donner l'impression d'avoir plus d'images à partir desquelles entraîner et nous sommes moins susceptibles de surajuster. Est-ce aussi bien que d'obtenir plus d'images ? Non, mais c'est rapide et économique.

Lors du choix des transformations à utiliser, nous voulons quelque chose qui ait du sens. Voici quelques exemples de transformations normales de la même image si nous regardions des races de chiens. Si l'une de ces images venait individuellement dans l'ensemble de données, nous penserions qu'elle a du sens. En mettant en place des transformations, nous avons maintenant 8 images au lieu d'une seule.

![Image](https://cdn-media-1.freecodecamp.org/images/HnxacZmYHwcPPBgjOeLVLBh8YllnaULywJBn)

Et si, dans la folie des transformations, nous allions trop loin ? Nous pourrions obtenir les images ci-dessous qui sont un peu trop extrêmes. Nous ne voudrions pas utiliser beaucoup de celles-ci car elles ne sont pas claires et ne s'orientent pas correctement dans une direction où nous nous attendrions à ce que les données arrivent. Bien qu'un chien puisse être incliné, il ne serait jamais à l'envers.

![Image](https://cdn-media-1.freecodecamp.org/images/MNijsrlyoAn6dSbT2SiepF27riQolrHI7LA3)

Pour les images d'endoscope, nous ne sommes pas aussi préoccupés par le fait qu'elles soient à l'envers ou trop inclinées. Un endoscope va partout et peut avoir une rotation à 360 degrés ici, donc j'ai utilisé des transformations rotationnelles à volonté. Même un peu avec la couleur car l'éclairage à l'intérieur du corps serait différent. Toutes ces transformations semblent être dans le domaine du possible.

![Image](https://cdn-media-1.freecodecamp.org/images/tpnXtApoMmk8rhYu71DdHORHiCP5oVwXHF9q)
_Exemple de polypes teints_

_(Note : la boîte verte indique la distance parcourue par l'endoscope. Par conséquent, cette technique pourrait couper la valeur qui aurait pu être fournie.)_

#### Reconstruction des données et lancement

Maintenant, nous pouvons voir comment ajouter des transformations et comment nous pourrions modifier d'autres variables pour les données :

![Image](https://cdn-media-1.freecodecamp.org/images/QUZEWFkUm8lcFXTCWXM58rplndCdQUW1A2M4)

Ensuite, nous changeons l'apprenant :

![Image](https://cdn-media-1.freecodecamp.org/images/jzQl2sQv19lAeWrUdY4B6UpXYbmo40tjy0mr)
_C'est vraiment aussi simple que ça_

Ensuite, nous sommes prêts à lancer !

![Image](https://cdn-media-1.freecodecamp.org/images/ApcLKcBsWNAF1Iz6Pw0cGx6sBVnc2tgB6NjK)

_De nombreuses époques plus tard…_

![Image](https://cdn-media-1.freecodecamp.org/images/qHbnsIFF1V209q1rVzFmzMZvE7Vz0EjN-oA4)
_Concentrez-vous simplement sur le nombre ici à droite_

93 % de précision ! Pas si mal, regardons à nouveau la matrice de confusion.

![Image](https://cdn-media-1.freecodecamp.org/images/LfwbVbdB131A6yIuizYC2KpS02lZ1KqMJZx1)

Il semble que le problème avec la classification teinte ait disparu, mais les erreurs d'œsophagite persistent. En fait, le nombre d'erreurs s'aggrave dans certaines de mes itérations.

### Peut-on exécuter cela en production ?

Oui, il existe des instructions pour héberger rapidement ces informations en tant que service web. Tant que la licence n'est pas en place et que vous ne vous opposez pas à attendre… vous pouvez l'essayer sur [Render ici](https://kvasir-demo.onrender.com/) !

![Image](https://cdn-media-1.freecodecamp.org/images/5YnqATL1HQXt7zcTcvCi2wEeXQxVLMrq43BH)

### Conclusion et suivi :

Comme vous pouvez le voir, il est simple de transférer le nouveau cours de Fast.ai à un ensemble de données différent. Beaucoup plus accessible que jamais.

Lors des tests, assurez-vous de commencer par un concept rapide pour vous assurer que tout est sur la bonne voie, puis augmentez la puissance plus tard. Créez une boucle de rétroaction positive pour vous assurer que vous êtes correctement orienté et comme mécanisme pour vous forcer à en apprendre davantage sur l'ensemble de données. Vous aurez une expérience beaucoup plus riche en faisant cela.

Quelques observations sur cet ensemble de données.

* J'essaie de résoudre ce problème de manière incorrecte. J'utilise un seul classificateur alors que ces diapositives ont plusieurs classifications. Je l'ai découvert plus tard en lisant l'article de recherche. _Ne lisez pas les articles jusqu'à la fin !_
* En tant que problème de multi-classification, je devrais inclure des boîtes de délimitation pour les caractéristiques essentielles.
* Les classifications peuvent bénéficier d'une caractéristique décrivant la distance parcourue par l'endoscope dans le corps. Des repères significatifs dans le corps aideraient à classer les images. La petite boîte verte en bas à gauche des images est une carte décrivant où se trouve l'endoscope et pourrait être une caractéristique utile à explorer.
* Si vous n'avez pas vu le nouveau cours de fast.ai, jetez un coup d'œil, il m'a fallu plus de temps pour écrire ce post que pour coder le programme, c'était si simple.

**Ressources**

* [Notebook Github](https://github.com/jamesdietle/fastaipart3/blob/master/Kvasir-Dataset2.ipynb)
* [Ensemble de données Kvasir](https://datasets.simula.no/kvasir/#data-collection)
* [KVASIR : Un ensemble de données d'images multi-classes pour la détection assistée par ordinateur des maladies gastro-intestinales](https://www.researchgate.net/publication/316215961_KVASIR_A_Multi-Class_Image_Dataset_for_Computer_Aided_Gastrointestinal_Disease_Detection) (Pogorelov, Konstantin & Randel, Kristin & Griwodz, Carsten & de Lange, Thomas & Eskeland, Sigrun & Johansen, Dag & Spampinato, Conceição & Dang Nguyen, Duc Tien & Lux, Mathias & Schmidt, Peter & Riegler, Michael & Halvorsen)
* [FastAI](https://docs.fast.ai/)
* [PyTorch](https://pytorch.org/docs/master/)
* [Vidéo YouTube sur ce sujet](https://youtu.be/GXuqT4uMKZk)