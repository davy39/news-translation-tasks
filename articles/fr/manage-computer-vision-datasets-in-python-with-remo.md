---
title: Comment gérer des ensembles de données de vision par ordinateur en Python avec
  Remo
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-10T19:28:08.000Z'
originalURL: https://freecodecamp.org/news/manage-computer-vision-datasets-in-python-with-remo
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/d148d60c3269c7e0a3070eec97a5e497-1.png
tags:
- name: Computer Vision
  slug: computer-vision
- name: data
  slug: data
- name: data analysis
  slug: data-analysis
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
seo_title: Comment gérer des ensembles de données de vision par ordinateur en Python
  avec Remo
seo_desc: 'By Pier Paolo Ippolito

  Computer Vision is one of the most important applications of Machine Learning. Some
  common commercial applications of Computer Vision are:


  Predictive maintenance for industrial infrastructure, oil and gas pipelines, and
  commer...'
---

Par Pier Paolo Ippolito

La vision par ordinateur est l'une des applications les plus importantes de l'apprentissage automatique. Certaines applications commerciales courantes de la vision par ordinateur sont :

* Maintenance prédictive pour les infrastructures industrielles, les pipelines de pétrole et de gaz, et l'immobilier commercial
* Automatisation de l'assurance qualité
* Inventaire des paysages et gestion des parcelles basée sur l'imagerie satellite et les vidéos de drones

Et certaines des techniques les plus courantes utilisées pour accomplir ces types de tâches sont :

* Classification d'images
* Détection d'objets
* Segmentation d'instances

Au cours de la dernière décennie, de nombreux frameworks tels que TensorFlow, Keras et PyTorch ont été développés afin de faciliter le développement de modèles basés sur la vision par ordinateur. 

Mais il est encore relativement difficile de travailler avec des données d'images en raison du prétraitement des images nécessaire, de l'étiquetage et de la visualisation des annotations.

Dans le cadre de cet article, je vais vous présenter [Remo](https://remo.ai/), une bibliothèque Python gratuite conçue pour aider les développeurs à travailler sur des tâches de vision par ordinateur. Remo peut vous aider à :

* Organiser et visualiser des images et des annotations
* Annoter efficacement
* Travailler et collaborer en équipe sur les données

Remo peut être utilisé soit dans un Jupyter Notebook, soit dans l'environnement Google Colab. Dans cet article, tout le code sera basé sur la configuration Google Colab et le notebook complet est librement disponible à [ce lien](https://colab.research.google.com/drive/1G0X6ieL9_O5jbdpPPG72nulNhxKELwzd?usp=sharing).

## Comment Remo améliore la gestion des images

Il existe un certain nombre d'outils d'annotation ouverts hérités pour les images disponibles. [LabelImg](https://github.com/tzutalin/labelImg) est l'un des plus populaires. 

Comparé à ces outils, Remo offre des outils intelligents pour annoter plus efficacement (par exemple, des raccourcis et xclick draw) et des fonctionnalités qui vous aident à collaborer et à organiser votre travail. Vous pouvez marquer les images comme Terminées ou À faire, les trier et les rechercher, et ainsi de suite – ce qui est très utile lorsque vous travaillez avec des milliers d'images.

Mais la gestion des ensembles de données est là où Remo est très innovant. Actuellement, les images dans les projets de vision par ordinateur sont généralement stockées sous forme de fichiers plats dans un disque dur local ou un stockage Cloud, et les annotations sont enregistrées sous forme de fichiers XML/JSON/csv bruts. 

Pour les visualiser, vous ouvrirez généralement chaque fichier individuellement et essayerez d'imaginer où se trouvent les annotations, ou vous les tracerez une par une en Python. 

Au lieu de cela, Remo vous donne un contrôle et une visibilité complets sur toutes les données.

## Démonstration du fonctionnement de Remo

Tout d'abord, nous devons installer toutes les dépendances nécessaires. Cela peut être facilement fait dans Google Colab en exécutant les deux lignes de code suivantes :

```python
!pip install remo
!python -m remo_app init --colab
```

Une fois que nous avons installé Remo, nous pouvons alors créer un ensemble de données en utilisant quelques images d'exemple librement disponibles sur Amazon Web Services.

```python
import remo
import pandas

link = ['https://remo-scripts.s3-eu-west-1.amazonaws.com/open_images_sample_dataset.zip']

df = remo.create_dataset(name = 'Exemple d'ensemble de données d'images',
                    urls = link, 
                    annotation_task = "Détection d'objets")
                    
# Sortie
# Acquisition des données - terminée                          
# Traitement des fichiers d'annotation : 1 sur 1 fichiers                                  
# Traitement des données - terminé       
# Téléchargement des données terminé
```

En exécutant la commande Remo **list_datasets()**, nous pouvons facilement vérifier quels ensembles de données nous avons actuellement disponibles.

```python
remo.list_datasets()

# Sortie
# [Dataset  1 - 'Exemple d'ensemble de données d'images' - 10 images]
```

Nous sommes maintenant prêts à utiliser l'interface graphique de Remo afin d'inspecter notre ensemble de données et de voir les différentes options disponibles. 

Dans la Figure 1, vous verrez un simple exemple de la facilité avec laquelle il est possible de visualiser et d'annoter nos données en utilisant Remo.

```python
df.view()
```

![Image](https://www.freecodecamp.org/news/content/images/2020/11/remo.gif)
_Figure 1 : Prétraitement des données GUI de Remo_

Un autre avantage important de l'utilisation de Remo est qu'il vous permet d'obtenir rapidement des statistiques clés sur l'ensemble de données, soit par le biais de code Python, soit par l'interface utilisateur. 

Cela peut être particulièrement utile lorsque vous essayez de comprendre comment les annotations sont distribuées entre différentes images et si la distribution globale des classes est équilibrée ou non.

```python
df.get_annotation_statistics()

# Sortie
# [{'ID de l'ensemble d'annotations': 1,
#  'Nom de l'ensemble d'annotations': 'Détection d'objets',
#  'date_de_création': None,
#  'date_de_dernière_modification': '2020-11-28T22:04:48.263767Z',
#  'n_classes': 18,
#  'n_images': 10,
#  'n_objets': 98,
#  'top_3_classes': [{'count': 27, 'name': 'Fruit'},
#   {'count': 12, 'name': 'Équipement sportif'},
#   {'count': 10, 'name': 'Bras humain'}]}]
```

Vous pouvez voir des résultats similaires en utilisant l'interface graphique de Remo (Figure 2).

```python
df.view_annotation_stats()
```

![Image](https://www.freecodecamp.org/news/content/images/2020/11/remo2.gif)
_Figure 2 : Fonctionnalités statistiques de Remo_

Enfin, si vous avez utilisé l'interface Remo pour ajouter des annotations aux différentes images de votre ensemble de données, celles-ci peuvent être automatiquement exportées au format CSV. Cela vous permet de les utiliser plus tard et de tirer parti de la fonction **export_annotations_to_file()** de Remo. 

```python
df.export_annotations_to_file('images_annotations.zip', annotation_format='csv', export_tags = False)
```

## Conclusion

Pour résumer, certaines des fonctionnalités clés fournies par Remo sont :

* Capacités de gestion des ensembles de données
* Plusieurs formats de fichiers pris en charge ainsi que des tâches de vision par ordinateur
* Interface conviviale et outils d'annotation améliorés
* Collaboration facile sur un projet
* Prise en charge de l'utilisation de machines virtuelles

Si vous êtes intéressé à en savoir plus sur Remo (comme comment intégrer Remo avec d'autres frameworks tels que PyTorch) ou comment configurer ce flux de travail dans un environnement Jupyter Notebook, la [documentation officielle de Remo](https://remo.ai/docs/) est un excellent point de départ. 

_J'espère que vous avez apprécié cet article, merci pour votre lecture !_

## Contactez-moi

Si vous souhaitez rester informé de mes derniers articles et projets, [suivez-moi sur Medium](https://medium.com/@pierpaoloippolito28?source=post_page---------------------------) et abonnez-vous à ma [liste de diffusion](http://eepurl.com/gwO-Dr?source=post_page---------------------------). Voici quelques-uns de mes détails de contact :

* [Linkedin](https://uk.linkedin.com/in/pier-paolo-ippolito-202917146?source=post_page---------------------------)
* [Blog personnel](https://pierpaolo28.github.io/blog/?source=post_page---------------------------)
* [Site web personnel](https://pierpaolo28.github.io/?source=post_page---------------------------)
* [Patreon](https://www.patreon.com/user?u=32155890)
* [Profil Medium](https://towardsdatascience.com/@pierpaoloippolito28?source=post_page---------------------------)
* [GitHub](https://github.com/pierpaolo28?source=post_page---------------------------)
* [Kaggle](https://www.kaggle.com/pierpaolo28?source=post_page---------------------------)

Photo de couverture provenant de la [documentation Remo](https://remo.ai/).