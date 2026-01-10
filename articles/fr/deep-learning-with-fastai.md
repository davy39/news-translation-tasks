---
title: Tutoriel sur l'apprentissage profond – Comment entraîner et déployer un modèle
  d'apprentissage profond avec fast.ai
subtitle: ''
author: Harshit Tyagi
co_authors: []
series: null
date: '2020-10-06T22:08:19.000Z'
originalURL: https://freecodecamp.org/news/deep-learning-with-fastai
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/Untitled-design.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Deep Learning
  slug: deep-learning
- name: 'fastai, '
  slug: fastai
seo_title: Tutoriel sur l'apprentissage profond – Comment entraîner et déployer un
  modèle d'apprentissage profond avec fast.ai
seo_desc: 'Deep learning is bringing revolutionary changes to many disciplines. It
  is also becoming more accessible to domain experts and AI enthusiasts with the advent
  of libraries like TensorFlow, PyTorch, and now fast.ai.

  fast.ai''s mission is to democratize ...'
---

L'apprentissage profond apporte des changements révolutionnaires à de nombreuses disciplines. Il devient également plus accessible aux experts du domaine et aux passionnés d'IA avec l'avènement de bibliothèques comme TensorFlow, PyTorch et maintenant **fast.ai**.

La mission de fast.ai est de démocratiser l'apprentissage profond. Il s'agit d'un institut de recherche dédié à aider tout le monde – d'un codeur de niveau débutant à un praticien expérimenté de l'apprentissage profond – à obtenir des résultats de classe mondiale avec des modèles et des techniques de pointe issus des dernières recherches dans le domaine.

Cet article de blog vous guidera à travers le processus de développement d'**un classificateur de chiens** en utilisant **fast.ai**. L'objectif est d'apprendre à quel point il est facile de commencer avec les modèles d'apprentissage profond et d'être capable d'obtenir des résultats presque parfaits avec une quantité limitée de données en utilisant des modèles pré-entraînés.

### Prérequis

Le seul prérequis pour commencer est que vous **sachiez coder en Python** et que vous soyez familier avec les mathématiques de niveau lycée.

### Ce que vous allez apprendre

1. Importer les bibliothèques et configurer le notebook

2. Collecte de données d'imagerie en utilisant Microsoft Azure

3. Conversion des données téléchargées en objets DataLoader

4. Augmentation des données

5. Nettoyage des données en utilisant l'entraînement du modèle

6. Exportation du modèle entraîné

7. Construction d'une application à partir de votre Jupyter Notebook

Alors, commençons.

## Comment importer les bibliothèques et configurer le notebook

Avant de commencer à construire notre modèle, nous devons importer les bibliothèques et la fonction utilitaire requises depuis [l'ensemble de notebooks](https://github.com/fastai/fastbook) appelé [fastbook](https://github.com/fastai/fastbook). Il a été développé pour couvrir l'introduction à l'apprentissage profond en utilisant fast.ai et PyTorch.

Installons le package fastbook pour configurer le notebook :

```javascript
!pip install -Uqq fastbook
import fastbook
fastbook.setup_book()
```

Ensuite, importons toutes les fonctions et classes du package fastbook et de l'API des widgets de vision fast.ai :

```javascript
from fastbook import *
from fastai.vision.widgets import *
```

## Comment collecter des données d'imagerie en utilisant Microsoft Azure

Pour la plupart des types de projets, vous pouvez trouver des données en ligne à partir de divers [dépôts de données et sites web](https://towardsdatascience.com/data-repositories-for-almost-every-type-of-data-science-project-7aa2f98128b?source=---------6----------------------------). Pour développer un classificateur de chiens, nous avons besoin d'images de chiens. Il existe de nombreuses images de chiens disponibles sur Internet.

Pour télécharger ces images, nous allons utiliser l'[API de recherche d'images Bing](https://azure.microsoft.com/en-us/services/cognitive-services/bing-image-search-api/) fournie par Microsoft Azure. Alors, inscrivez-vous pour un compte gratuit sur Microsoft Azure et vous recevrez 200 $ de crédits.

Allez sur votre portail et créez une nouvelle ressource de service cognitif en utilisant [ce guide de démarrage rapide](https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-apis-create-account?tabs=multiservice%2Clinux). Activez l'API de recherche d'images Bing. Ensuite, à partir de l'option `Keys and Endpoint` dans le panneau de gauche, copiez les **clés** de votre ressource.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/1-2.png align="left")

Avec les clés récupérées, définissez ces clés dans l'environnement comme suit :

```javascript
key = os.environ.get('AZURE_SEARCH_KEY', '<YOUR_KEY>')
```

Maintenant, fastbook vient avec des fonctions utilitaires comme `search_images_bing` qui retourne des URL correspondant à votre requête de recherche. Vous pouvez en apprendre davantage sur ces fonctions en utilisant la fonction d'aide :

```javascript
help(fastbook)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/8-1.png align="left")

Vous pouvez vérifier la fonction `search_image_bing` dans ce guide d'aide. La fonction accepte une clé pour votre ressource que vous avez définie ci-dessus et la requête de recherche, et nous pouvons accéder aux URL des résultats de recherche en utilisant la méthode `attrgot` :

```javascript
results = search_images_bing(key, 'german shepherd dogs')
images = results.attrgot('content_url')
len(images)
```

Nous avons 150 URL d'images de chiens Berger Allemand :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/9-1.png align="left")

Maintenant, nous pouvons télécharger ces images en utilisant la fonction `download_url`. Mais définissons d'abord le type de chiens que nous voulons.

Pour ce tutoriel, je vais travailler avec trois types de chiens : les Bergers Allemands, les chiens noirs et les Labradors.

Alors, définissons une liste de types de chiens :

```javascript
dog_types = ['german shepherd', 'black', 'labrador']
path = Path('dogs')
```

Vous devrez ensuite définir le chemin où vos images seront téléchargées ainsi que les noms sémantiques du dossier pour chaque classe de chien.

```javascript
if not path.exists():
    path.mkdir()
    for t in dog_types:
        dest = (path/t)
        print(dest)
        dest.mkdir(exist_ok=True)
        results = search_images_bing(key, '{} dog'.format(t))
        download_images(dest, urls=results.attrgot('content_url'))
```

Cela créera un répertoire "dogs" qui contient également 3 répertoires pour chaque type d'image de chien.

Après cela, nous passons la requête de recherche (qui est le dog\_type) et la clé à la fonction de recherche, suivie de la fonction de téléchargement pour télécharger toutes les URL des résultats de recherche dans leurs répertoires de destination respectifs (`dest`).

Nous pouvons vérifier les images téléchargées vers un chemin en utilisant la fonction `get_image_file` :

```python
files = get_image_files(path)
files
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/10.png align="left")

### Comment vérifier les images

Vous pouvez également vérifier le nombre de fichiers/images corrompus dans les fichiers :

```javascript
corrupt = verify_images(files)
corrupt

##output: (#0) []
```

Vous pouvez supprimer tous les fichiers corrompus (le cas échéant) en mappant la méthode unlink à la liste des fichiers corrompus : corrupt.map(Path.unlink);

C'est tout, nous avons 379 images de chiens prêtes avec nous pour entraîner et valider notre modèle.

## Comment convertir les données téléchargées en objets DataLoader

Maintenant, nous avons besoin d'un mécanisme pour fournir des données à notre modèle. fast.ai a ce concept de DataLoaders qui stocke plusieurs objets DataLoader qui lui sont passés et les rend disponibles en tant qu'ensemble `training` et `validation`.

Maintenant, pour convertir les données téléchargées en un objet DataLoader, nous devons fournir quatre choses :

* Quels types de données nous utilisons

* Comment obtenir la liste des éléments

* Comment étiqueter ces éléments

* Comment créer l'ensemble de validation

Maintenant, pour créer ces objets DataLoaders avec les informations mentionnées ci-dessus, fast.ai offre un système flexible appelé **data block API**. Nous pouvons spécifier tous les détails de la création de DataLoader en utilisant les arguments et un tableau de méthodes de transformation que l'API offre :

```javascript
dogs = DataBlock(
                  blocks=(ImageBlock, CategoryBlock),
                  get_items=get_image_files,
                  splitter=RandomSplitter(valid_pct=0.2, seed=41),
                  get_y=parent_label,
                  item_tfms=Resize(128)
                  )
```

Ici, nous avons un ensemble d'arguments que nous devons comprendre :

* **blocks** – cela spécifie les variables de caractéristique (images) et la variable cible (une catégorie pour chaque image)

* **get_items** – récupère les éléments sous-jacents (qui sont des images dans notre cas) et nous avons une fonction `**get_image_files**` qui retourne une liste de toutes les images dans ce chemin.

* **splitter** – divise les données selon la méthode fournie. Nous utilisons une division aléatoire avec 20 % des données réservées pour l'ensemble de validation et avons spécifié la graine pour obtenir la même division à chaque exécution.

* **get_y** – la variable cible est appelée y. Pour créer les étiquettes, nous utilisons la fonction `**parent_label**` qui obtient le nom du dossier où le fichier réside comme son étiquette.

* **item_tfms** – nous avons des images de différentes tailles et cela pose un problème car nous envoyons toujours un lot de fichiers au modèle au lieu d'un seul fichier. Par conséquent, nous devons prétraiter ces images en les redimensionnant à une taille standard, puis les regrouper dans un tenseur pour les passer à travers le modèle. Nous utilisons ici la transformation `**Resize**`.

Maintenant, nous avons l'objet DataBlock qui doit être converti en DataLoader en fournissant le chemin vers le jeu de données :

```javascript
dls = dogs.dataloaders(path)
```

Nous pouvons ensuite vérifier les images dans l'objet dataloader en utilisant la méthode `show_batch` :

```javascript
dls.valid.show_batch()
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/2-2.png align="left")

## Augmentation des données

Nous pouvons ajouter des transformations à ces images pour créer des variations aléatoires des images d'entrée, de sorte qu'elles apparaissent différentes mais représentent toujours les mêmes faits.

Nous pouvons faire pivoter, déformer, retourner ou changer la luminosité/le contraste des images pour créer ces variations. Nous avons également un ensemble standard d'augmentations encapsulées dans la fonction `aug_transforms` qui fonctionne assez bien pour la majorité des jeux de données de vision par ordinateur.

Nous pouvons maintenant appliquer ces transformations à un lot entier d'images, car toutes les images sont de la même taille (224 pixels, standard pour les problèmes de classification d'images) en utilisant ce qui suit :

```javascript
##adding item transformations
dogs = dogs.new(
        item_tfms=RandomResizedCrop(224, min_scale=0.5),
        batch_tfms=aug_transforms(mult=2)
        )
dls = dogs.dataloaders(path)
dls.train.show_batch(max_n=8, nrows=2, unique=True)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/3-1.png align="left")

## Entraînement du modèle et nettoyage des données

Il est temps d'entraîner le modèle avec ce nombre limité d'images. fast.ai offre de nombreuses architectures à utiliser, ce qui facilite l'utilisation du transfert d'apprentissage.

Nous pouvons créer un modèle de réseau de neurones convolutif (CNN) en utilisant les modèles pré-entraînés qui fonctionnent pour la plupart des applications/jeux de données.

Nous allons utiliser l'architecture ResNet, car elle est à la fois rapide et précise pour de nombreux jeux de données et problèmes. Le 18 dans `**resnet18**` représente le nombre de couches dans le réseau de neurones.

Nous passons également la métrique pour mesurer la qualité des prédictions du modèle en utilisant l'ensemble de validation du dataloader. Nous utilisons **error_rate** qui nous indique à quelle fréquence le modèle fait des prédictions incorrectes :

```javascript
model = cnn_learner(dls, resnet18, metrics=error_rate)
model.fine_tune(4)
```

La méthode `fine_tune` est analogue à la méthode `fit()` dans d'autres bibliothèques ML. Maintenant, pour entraîner le modèle, nous devons spécifier le nombre de fois (époques) où nous voulons entraîner le modèle sur chaque image.

Ici, nous entraînons pendant seulement 4 époques :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/4-1.png align="left")

Nous pouvons également visualiser les prédictions et les comparer avec les étiquettes réelles en utilisant la matrice de confusion :

```javascript
interp = ClassificationInterpretation.from_learner(learn)
interp.plot_confusion_matrix()
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/5-1.png align="left")

Comme vous pouvez le voir, nous n'avons que cinq prédictions incorrectes. Vérifions les pertes les plus élevées, c'est-à-dire les images avec la perte la plus élevée dans le jeu de données : interp.plot\_top\_losses (6, nrows=3) :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/6-1.png align="left")

Vous pouvez voir que le modèle a confondu les chiens noirs et les labradors. Ainsi, nous pouvons spécifier que ces images appartiennent à une catégorie particulière en utilisant la classe ImageClassifierCleaner.

Passez le modèle à la classe et il ouvrira un widget avec une interface graphique intuitive pour le nettoyage des données. Nous pouvons changer les étiquettes des images de l'ensemble d'entraînement et de validation et voir les images avec les pertes les plus élevées.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/7-1.png align="left")

Après avoir ajouté chaque image à leur classe correcte respective, nous devons les déplacer vers leur répertoire correct en utilisant :

```javascript
for idx,cat in cleaner.change():
    shutil.move(str(cleaner.fns[idx]), str(path/cat).split('.')[0] +"_fixed.jpg")
```

## Comment exporter le modèle entraîné

Après quelques tours de réglage des hyperparamètres, et une fois que vous êtes satisfait de votre modèle, vous devez l'enregistrer afin de pouvoir le déployer sur un serveur pour qu'il soit utilisé en production.

Lors de l'enregistrement d'un modèle, nous avons l'architecture du modèle et les paramètres entraînés qui sont de valeur pour nous. fast.ai offre la méthode `export()` pour enregistrer le modèle dans un fichier pickle avec l'extension `.pkl`.

```javascript
model.export()
path = Path()
path.ls(file_exts='.pkl')
```

Nous pouvons ensuite charger le modèle et faire des inférences en passant une image au modèle chargé :

```javascript
model_inf = load_learner(path/'export.pkl')
```

Utilisez ce modèle chargé pour faire des inférences :

```javascript
model_inf.predict('dogs/labrador/00000000.jpg')
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/11.png align="left")

Nous pouvons vérifier les étiquettes à partir du vocabulaire du dataloader du modèle :

```javascript
model_inf.dls.vocab
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/12.png align="left")

## Comment construire une application à partir de votre Jupyter Notebook

L'étape suivante consiste à créer une application que nous pouvons partager avec nos amis, collègues, recruteurs et autres.

Pour créer une application, nous devons ajouter des éléments interactifs afin de pouvoir essayer et tester les fonctionnalités de l'application. Nous devons également la rendre disponible sur le web en tant que page web, ce qui inclut son déploiement via un framework comme Flask ou simplement en utilisant Voila.

Vous pouvez utiliser Voila pour convertir ce Jupyter Notebook en une application autonome. Je ne l'ai pas couvert ici, mais vous pouvez consulter mon [blog/vidéo](https://medium.com/r?url=https%3A%2F%2Ftowardsdatascience.com%2Fbuilding-covid-19-analysis-dashboard-using-python-and-voila-ee091f65dcbb) qui couvre tout le processus.

### Déploiement de votre modèle

J'ai couvert le déploiement d'un modèle ML dans mon article [ici](https://towardsdatascience.com/deploying-a-trained-ml-model-using-flask-541520b3cbe9). Mais si vous voulez une autre méthode facile et gratuite pour déployer votre application Voila, vous pouvez utiliser [Binder](https://mybinder.org/).

Suivez ces étapes pour déployer l'application sur Binder :

1. Ajoutez votre notebook à un [dépôt GitHub](http://github.com/).

2. Insérez l'URL de ce dépôt dans le champ URL de Binder.

3. Changez le menu déroulant du fichier pour sélectionner plutôt l'URL.

4. Dans le champ "URL à ouvrir", entrez `/voila/render/<_name>_.ipynb`

5. Cliquez sur le bouton de presse-papiers en bas à droite pour copier l'URL et collez-la quelque part en sécurité.

6. Cliquez sur Lancer.

Et voilà, votre classificateur de chiens est en ligne !

Si vous préférez me regarder passer par toutes ces étapes, voici la version vidéo de ce blog :

%[https://youtu.be/pNaCrhxmN1w]

### [Data Science avec Harshit](https://www.youtube.com/c/DataSciencewithHarshit?sub_confirmation=1)

%[https://youtu.be/yapSsspJzAw]

Avec cette chaîne, je prévois de lancer une couple de [séries couvrant tout l'espace de la science des données](https://towardsdatascience.com/hitchhikers-guide-to-learning-data-science-2cc3d963b1a2?source=---------8------------------). Voici pourquoi vous devriez vous abonner à la [chaîne](https://www.youtube.com/channel/UCH-xwLTKQaABNs2QmGxK2bQ) :

* Ces séries couvriraient tous les tutoriels de qualité requis/demandés sur chacun des sujets et sous-sujets comme [les fondamentaux de Python pour la science des données](https://towardsdatascience.com/python-fundamentals-for-data-science-6c7f9901e1c8?source=---------5------------------).

* [Mathématiques et dérivations](https://towardsdatascience.com/practical-reasons-to-learn-mathematics-for-data-science-1f6caec161ea?source=---------9------------------) expliquées sur pourquoi nous faisons ce que nous faisons en ML et en apprentissage profond.

* [Podcasts avec des scientifiques et ingénieurs de données](https://www.youtube.com/watch?v=a2pkZCleJwM&t=2s) chez Google, Microsoft, Amazon, etc., et PDG de grandes entreprises axées sur les données.

* [Projets et instructions](https://towardsdatascience.com/building-covid-19-analysis-dashboard-using-python-and-voila-ee091f65dcbb?source=---------2------------------) pour mettre en œuvre les sujets appris jusqu'à présent. Apprenez à connaître de nouvelles certifications, Bootcamp et ressources pour obtenir ces certifications comme cet [examen de certification de développeur TensorFlow par Google](https://youtu.be/yapSsspJzAw).

Si ce tutoriel était utile, vous devriez consulter mes cours de science des données et d'apprentissage automatique sur [Wiplane Academy](https://www.wiplane.com/). Ils sont complets mais compacts et vous aident à construire une base solide de travail à présenter.