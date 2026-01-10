---
title: Comment améliorer vos compétences en analyse de données avec Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-31T15:33:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-boost-your-data-analysis-skills-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/carlos-muza-hpjSkU2UYSU-unsplash.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: pandas
  slug: pandas
- name: Python
  slug: python
seo_title: Comment améliorer vos compétences en analyse de données avec Python
seo_desc: 'By Emma Coffinet

  If you''re learning Python, you''ve likely heard about sci-kit-learn, NumPy and
  Pandas. And these are all important libraries to learn. But there is more to them
  than you might initially realize.

  There are numerous tips and tricks in t...'
---

Par Emma Coffinet

Si vous apprenez Python, vous avez probablement entendu parler de sci-kit-learn, NumPy et Pandas. Et ce sont toutes des bibliothèques importantes à apprendre. Mais il y a plus à savoir qu'il n'y paraît initialement.

Il existe de nombreux conseils et astuces dans le [monde de Python](https://www.freecodecamp.org/learn) qui peuvent vous aider à accélérer vos tâches en science des données, améliorer votre code et vous aider à écrire du code plus efficacement.

J'ai donc décidé de compiler certains des conseils les plus précieux pour l'analyse de données dans cet article pour vous.

## Profiler les dataframes dans Pandas

Le rôle principal ou l'objectif du profilage est d'obtenir une compréhension claire des données. Et c'est ce que fait le package Python, Pandas Profiling. Cette méthode est simple et rapide pour effectuer l'analyse de données des dataframes dans Pandas.

Le processus d'analyse exploratoire des données inclut les fonctions Pandas df.info() et df.describe() comme premières étapes. Mais vous n'obtenez qu'un aperçu basique des données, ce qui peut ne pas être très utile si vous travaillez avec un grand ensemble de données.

La [fonction de profilage](https://www.google.com/url?sa=t&source=web&rct=j&url=https://www.kaggle.com/parulpandey/10-simple-hacks-to-speed-up-your-data-analysis&ved=2ahUKEwjJ_tzBy-LqAhVPUBUIHYomB-gQFjAMegQIARAB&usg=AOvVaw1gTlUdtw6xS0ykqe9hhU5Y) de Pandas étend également le dataframe de Pandas avec df.profile_report(), ce qui vous aide à analyser rapidement les données. Elle affiche beaucoup d'informations en une seule ligne de code, qui est également un rapport HTML interactif.

Pour un ensemble de données, le profilage Pandas calcule ces statistiques :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-50.png)

![Image](file:///C:/Users/JULIA~1.LOG/AppData/Local/Temp/lu43286f6mgz.tmp/lu43286f6mi9_tmp_9f3d0f0a74210f0d.png)

## Rendre les graphiques pandas plus interactifs

La fonction intégrée plot() de Pandas fait également partie des classes Dataframe. Cependant, cette fonction offre des visualisations qui ne sont pas très interactives et n'attirent donc pas beaucoup l'attention d'un public de science des données.

D'un autre côté, il est facile de tracer un graphique avec la fonction Pandas.DataFrame.plot(). La question est alors, comment tracer des graphiques interactifs comme Plotly en utilisant Pandas et sans apporter de modifications significatives au code ?

Vous pouvez le faire avec la bibliothèque Cufflinks, qui combine la puissance de Plotly avec la flexibilité de Pandas pour tracer rapidement.

Vous pouvez voir le résultat dans les images ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-51.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-52.png)

![Image](file:///C:/Users/JULIA~1.LOG/AppData/Local/Temp/lu43286f6mgz.tmp/lu43286f6mi9_tmp_95977e6b363dc6c.png)

![Image](file:///C:/Users/JULIA~1.LOG/AppData/Local/Temp/lu43286f6mgz.tmp/lu43286f6mi9_tmp_5a8ad0fe7da1045d.gif)

Les deux visualisations montrent les mêmes choses. La première visualisation est un graphique statique, tandis que la seconde est un graphique plus interactif (et il fournit également plus de détails que le premier). Pourtant, nous avons obtenu cela sans apporter de modifications significatives à la syntaxe.

## Commandes magiques

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-71.png)

Le terme "Commandes magiques" fait référence à un ensemble de fonctions dans les Jupyter Notebooks. Ils ont créé cet ensemble de fonctionnalités pour résoudre les nombreux problèmes courants rencontrés dans l'[analyse de données](https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-learn-data-science-python-scratch-2/).

Il existe deux types de commandes magiques. Tout d'abord, il y a les magies de ligne - celles qui ont un préfixe du caractère %. Elles fonctionnent également sur une ligne d'entrée.

Le deuxième type sont les magies de cellule - désignées par le préfixe double %%. Elles fonctionnent sur plus d'une ligne d'entrée. Si vous le définissez sur 1, vous appellerez les fonctions magiques sans avoir besoin de taper le % initial.

Certaines de ces commandes peuvent être utiles lorsque vous effectuez des tâches quotidiennes en analyse de données. Certaines d'entre elles sont :

### %pastebin

Cette fonction retourne l'URL et télécharge également le code vers Pastebin. Pastebin est un service d'hébergement de contenu en ligne où il est possible de stocker du texte brut (comme des extraits de code source) puis de partager l'URL avec d'autres personnes.

En fait, un gist Github est très similaire à Pastebin, mais avec un contrôle de version.

### %matplotlib notebook

Vous pouvez utiliser cette fonction en ligne pour rendre les graphiques Matplotlib statiques dans les notebooks Jupyter. Vous devez essayer de remplacer la partie en ligne par un notebook. Cela vous donnera des graphiques redimensionnables et zoomables rapidement.

Mais assurez-vous d'appeler la fonction avant de commencer à importer la bibliothèque Matplotlib.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-72.png)

### %run

Vous pouvez utiliser cette fonction pour exécuter un script Python dans un notebook.

### %%writefile

Cette fonction écrit le contenu de la cellule dans un fichier. Vous écrivez ensuite le code dans un autre fichier nommé foo.py avant de l'enregistrer dans le répertoire courant.

### %%latex

Cette fonction fait apparaître le contenu de la cellule sous forme de LaTeX. Elle est utile lorsque vous écrivez des équations et des formules mathématiques dans une cellule.

## Trouver et supprimer les erreurs

La fonction connue sous le nom de [débogueur interactif](https://towardsdatascience.com/10-simple-hacks-to-speed-up-your-data-analysis-in-python-ec18c6396e6b) est une autre fonctionnalité magique. Cependant, pour cet article, elle a une catégorie différente qui lui est propre.

Si vous exécutez une cellule de code et obtenez une exception, tapez %debug sous une nouvelle ligne puis exécutez-la. Cela ouvrira un environnement de débogage interactif qui vous ramène au point où l'exception s'est produite.

Vous pouvez également vérifier les valeurs des différentes variables qui ont été assignées dans le programme et, en même temps, effectuer des opérations là-bas. Après cela, si vous voulez quitter le débogueur, appuyez sur q.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-53.png)

## Utiliser l'option 'I' lors de l'exécution de scripts Python

Une façon typique d'exécuter un script Python à partir de la ligne de commande est avec hello.py. Mais si vous ajoutez un -i et exécutez le même script Python, (Python -i hello.py), vous obtenez plus d'avantages. Comment ?

Tout d'abord, après avoir atteint la [fin du programme](https://www.google.com/url?sa=t&source=web&rct=j&url=https://www.analyticsvidhya.com/blog/2019/08/10-powerful-python-tricks-data-science/&ved=2ahUKEwjJ_tzBy-LqAhVPUBUIHYomB-gQFjAAegQIAxAB&usg=AOvVaw1H3TUawIio2d4aE_ifcaP-), Python ne ferme pas l'interpréteur. Cela signifie que nous pouvons vérifier les valeurs des différentes variables et la justesse des fonctions définies dans le programme.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Pict.jpg)

Deuxièmement, il est alors facile d'invoquer le débogueur Python, surtout puisque l'interpréteur est toujours disponible par :

* Import pdb
* Pdb.pm()

À partir de là, nous pouvons rapidement atteindre le point où l'exception s'est produite et ensuite travailler sur le code.

## Supprimer et restaurer

Alors, que faites-vous lorsque vous supprimez par erreur une cellule dans votre Jupyter Notebook ? Heureusement, il existe un raccourci pour annuler cette action.

Vous pouvez récupérer ou annuler votre contenu supprimé en appuyant sur CTRL/CMD+Z.

Si vous avez supprimé une cellule entière que vous souhaitez récupérer, appuyez sur ESC+Z, ou EDIT > Undo Delete Cells.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-74.png)

## Conclusion

Cet article a partagé quelques conseils pour améliorer vos compétences en analyse de données avec Python. Ces astuces devraient vous être utiles à un moment donné dans votre parcours d'analyse de données avec Python.