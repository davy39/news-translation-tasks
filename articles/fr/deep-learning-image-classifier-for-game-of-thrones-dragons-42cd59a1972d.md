---
title: 'Jour 24 : Comment construire un classificateur d''images en Deep Learning
  pour les dragons de Game of Thrones'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-21T20:27:02.000Z'
originalURL: https://freecodecamp.org/news/deep-learning-image-classifier-for-game-of-thrones-dragons-42cd59a1972d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TM3_JUHkkaTW36uQZp9FYw.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Deep Learning
  slug: deep-learning
- name: image classification
  slug: image-classification
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
seo_title: 'Jour 24 : Comment construire un classificateur d''images en Deep Learning
  pour les dragons de Game of Thrones'
seo_desc: 'By Harini Janakiraman


  Performance of most flavors of the old generations of learning algorithms will plateau.
  Deep learning, training large neural networks, is scalable and performance keeps
  getting better as you feed them more data. — Andrew Ng


  De...'
---

Par Harini Janakiraman

> Les performances de la plupart des variantes des anciennes générations d'algorithmes d'apprentissage vont atteindre un plateau. Le deep learning, qui consiste à entraîner de grands réseaux de neurones, est scalable et les performances continuent de s'améliorer à mesure que vous leur fournissez plus de données. — _Andrew Ng_

Le deep learning ne prend pas une quantité énorme de temps ou de ressources computationnelles. Il ne nécessite pas non plus de code hautement complexe, et dans certains cas, pas même une grande quantité de données d'entraînement. Des meilleures pratiques curatées sont désormais disponibles sous forme de bibliothèques qui facilitent l'intégration et l'écriture de vos propres architectures de réseaux de neurones en utilisant une quantité minimale de code pour atteindre des précisions de prédiction de plus de 90 %.

Les deux bibliothèques de deep learning les plus populaires sont : (1) pytorch créé par Facebook (nous utiliserons fastai aujourd'hui, qui est construit sur pytorch) et (2) le framework keras-tensorflow créé par Google.

### Le Projet

Nous allons construire un classificateur d'images en utilisant le modèle de réseau de neurones convolutifs (CNN) pour prédire si une image donnée est celle de Drogon ou de Vicerion (y a-t-il des fans de Game of Thrones ici ? Applaudissez pour dire oui !).

Vous pouvez adapter cet énoncé de problème à tout type de classification d'images qui vous intéresse. Voici quelques idées : chat ou chien (classique du deep learning 101), si une personne porte des lunettes ou non, bus ou voiture, hot dog vs pas hot dog (les fans de Silicon Valley disent aussi oui ! ;) ).

### Étape 1 : Installation

Vous pouvez utiliser n'importe quelle plateforme de cloud computing accélérée par GPU pour exécuter votre modèle. Pour les besoins de ce blog, nous utiliserons [Paperspace](https://www.paperspace.com/) (le plus abordable). Des instructions complètes sur la manière de le mettre en place et de le faire fonctionner sont disponibles [**ici**](https://github.com/reshamas/fastai_deeplearn_part1/blob/master/tools/paperspace.md).

Une fois configuré, vous pouvez lancer Jupyter notebook sur cette machine en utilisant la commande suivante :

```
jupyter notebook
```

Cela vous donnera une URL localhost que vous pouvez ouvrir dans votre navigateur et remplacer « localhost » par l'adresse IP de votre machine pour lancer votre notebook.

![Image](https://cdn-media-1.freecodecamp.org/images/gtn9GKmqFmghPbs7fLu6SzJ1hSid9GNpKNvV)

Vous pouvez maintenant copier le notebook iPython et les fichiers de dataset dans la structure de répertoire ci-dessous à partir de [**mon dépôt github**](https://github.com/harinij/100DaysOfCode/tree/master/Day%20023%20-%20Image%20Classifier%20using%20deep%20learning%20CNN%20model).

![Image](https://cdn-media-1.freecodecamp.org/images/3cvYJGymYABQJWr4bP6G29kZDkQSJUUFBGhp)

**Note** : N'oubliez pas d'éteindre la machine depuis la console Paperspace une fois que vous avez terminé pour éviter d'être facturé par erreur.

### **Étape 2 : Entraînement**

Suivez les instructions dans le notebook pour initialiser les bibliothèques nécessaires à cet exercice, et pointez vers l'emplacement du PATH de votre répertoire de données. Notez que chaque bloc de code peut être exécuté en utilisant « shift+enter ». Au cas où vous auriez besoin d'informations supplémentaires sur les commandes de Jupyter notebook, vous pouvez en lire plus [ici](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Notebook%20Basics.html).

Maintenant, en ce qui concerne la partie entraînement du classificateur d'images, les trois lignes de code suivantes forment le cœur de la construction du modèle de deep learning :

1. **data** : représente les ensembles de données de validation et d'entraînement.
2. **learn** : contient le modèle
3. **learn.fit(learning_rate,epoch)** : Ajuste le modèle en utilisant deux paramètres — taux d'apprentissage et époques.

![Image](https://cdn-media-1.freecodecamp.org/images/GSWXa64C56P8YNg4WPrlSvlAjdiTTq0abWP0)

Nous avons défini le taux d'apprentissage à « 0.01 » ici. Le taux d'apprentissage doit être un nombre suffisamment petit pour que vous parcouriez l'image par étapes incrémentielles de ce facteur afin d'apprendre avec précision. Mais il ne doit pas être trop petit non plus, car cela entraînerait trop d'étapes/trop de temps pour apprendre. La bibliothèque dispose d'une méthode de recherche de taux d'apprentissage « lr_find() » pour trouver le taux optimal.

L'époque est définie à « 3 » dans le code ici et elle représente le nombre de fois où vous devez exécuter le lot. Nous pouvons exécuter autant de fois que nous le souhaitons, mais après un certain point, la précision commencera à se dégrader en raison du surapprentissage.

![Image](https://cdn-media-1.freecodecamp.org/images/sas5SvMYXGfSQyeiKB96YURdhkad6r7BrtH2)

### **Étape 3 : Prédiction**

Nous allons maintenant exécuter la prédiction sur les données de validation en utilisant le modèle entraîné.

![Image](https://cdn-media-1.freecodecamp.org/images/oTZaAYbeABWT0tGnDEtEP7elcN5nb7lNB9Gp)

Pytorch donne un log de prédiction, donc pour obtenir la probabilité, vous devez obtenir e à la puissance en utilisant numpy. Suivez les instructions étape par étape dans le notebook de mon [**dépôt github**](https://github.com/harinij/100DaysOfCode/tree/master/Day%20023%20-%20Image%20Classifier%20using%20deep%20learning%20CNN%20model). Une probabilité proche de 0 implique qu'il s'agit d'une image de Drogon et une probabilité proche de 1 implique qu'il s'agit d'une image de Viserion.

### **Étape 4 : Visualisation**

La fonction de traçage peut être utilisée pour mieux visualiser les résultats de la prédiction. Les images ci-dessous vous montrent les données de validation correctement classées avec 0,2–0,3 indiquant qu'il s'agit de Drogon et une probabilité de 0,7–0,8 indiquant qu'il s'agit de Viserion.

![Image](https://cdn-media-1.freecodecamp.org/images/zf74Dk3FGDS3F3sd5WiGDpH-4vshGm3O-i1Z)

![Image](https://cdn-media-1.freecodecamp.org/images/3i82iaVHQHUPrEtOMufWCPPAuRu3iqeAhlE8)

![Image](https://cdn-media-1.freecodecamp.org/images/oQw5JxD8sAhzcnxAiwklzpUy2c4ph8UnbCSZ)

Vous pouvez également voir certaines des prédictions incertaines si elles restent proches de la probabilité de 0,5.

![Image](https://cdn-media-1.freecodecamp.org/images/USlRGvhRFoBP-JmY719kyZaKr-geDY4cldoS)

Le classificateur d'images peut, dans certains scénarios, avoir des prédictions incertaines, par exemple dans le cas d'images à longue queue, car il capture un petit morceau du carré à la fois.

Dans ces cas, des techniques d'amélioration peuvent être effectuées pour obtenir de meilleurs résultats, telles que l'augmentation des données, l'optimisation du taux d'apprentissage, l'utilisation de taux d'apprentissage différentiels pour différentes couches et l'augmentation au moment du test. Ces concepts avancés seront explorés dans de futurs articles.

Ce blog a été inspiré par la vidéo CNN de fastai. Pour obtenir une compréhension approfondie et continuer votre quête en Deep Learning, vous pouvez suivre la célèbre série de cours d'Andrew Ng sur [coursera](https://www.deeplearning.ai/).

_Si vous avez aimé cela, applaudissez **? s** afin que d'autres puissent le voir aussi ! Suivez-moi sur Twitter @[H**ariniLabs**](https://twitter.com/harinilabs) ou M[**edium**](https://medium.com/@harinilabs) pour obtenir des mises à jour de nouveaux articles ou simplement pour dire Bonjour :)_

_PS : Inscrivez-vous à ma newsletter [**ici**](http://harinilabs.com/womenintech.html) pour être le premier à recevoir du nouveau contenu et elle est remplie de doses d'inspiration du monde de #[**WomenInTech**](http://harinilabs.com/womenintech.html) — et oui, les hommes peuvent aussi s'inscrire :)_