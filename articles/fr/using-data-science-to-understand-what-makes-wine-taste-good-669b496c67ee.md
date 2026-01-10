---
title: Comment utiliser la science des données pour comprendre ce qui rend le vin
  bon
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-07T10:05:35.000Z'
originalURL: https://freecodecamp.org/news/using-data-science-to-understand-what-makes-wine-taste-good-669b496c67ee
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EmZW0kG4HpdoJSqqCZyiZg.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment utiliser la science des données pour comprendre ce qui rend le
  vin bon
seo_desc: 'By Ashwin Hariharan

  Data Science. It’s been touted as the sexiest job of the 21st century. Everyone — from
  companies to individuals — is trying to understand it and adopt it. And if you’re
  a programmer, you most definitely are experiencing FoMo (Fear...'
---

Par Ashwin Hariharan

Science des données. Elle a été saluée comme le [métier le plus sexy](https://hbr.org/2012/10/data-scientist-the-sexiest-job-of-the-21st-century) du 21e siècle. Tout le monde — des entreprises aux particuliers — essaie de la comprendre et de l'adopter. Et si vous êtes programmeur, vous ressentez certainement le FoMo (Fear of missing out) ! Regardez simplement à quel point le terme est devenu populaire au fil du temps :

![Image](https://cdn-media-1.freecodecamp.org/images/1*KN6Iiv_hFZstM5CgjqD7Vw.png)
_Niveau de popularité de la science des données au cours des 5 dernières années_

Le salaire moyen d'un data scientist est de plus de 120 000 $ aux États-Unis selon Indeed. Ils ont également actuellement les emplois les mieux payés, avec une médiane de [60k](https://medium.freecodecamp.org/the-6-most-desirable-coding-jobs-and-the-types-of-people-drawn-to-each-aebac45fd7f7). Glassdoor l'a également nommé "Meilleur emploi de 2016", et il a également été classé comme le meilleur emploi sur Glassdoor.

Mais quelle est cette science dont ils parlent tant ? Continuez à lire !

### Table des matières

* [Le besoin de la science des données](https://medium.com/p/669b496c67ee#9877)
* [Qui tirera le plus profit de ce tutoriel](https://medium.com/p/669b496c67ee#c496)
* [Prise en main](https://medium.com/p/669b496c67ee#9b0b)
* [Analyse des données](https://medium.com/p/669b496c67ee#5572)
* [Exploration des relations entre les caractéristiques et les techniques de visualisation des données](https://medium.com/p/669b496c67ee#7772)
* [Détection des valeurs aberrantes](https://medium.com/p/669b496c67ee#67c8)

### Quel est le besoin de la science des données ?

Pour faire simple, la science des données vous aide à être **data-driven**. Les décisions basées sur les données aident les entreprises à mieux comprendre leurs clients et à construire de grandes entreprises.

Nous vivons à l'ère de l'explosion de l'information. Les entreprises collectent différents types de données en fonction du type d'entreprise qu'elles dirigent. Par exemple — pour un magasin de détail, les données pourraient concerner les types de produits que ses clients achètent au fil du temps, et leurs montants de dépenses. Pour Netflix, cela pourrait concerner les émissions que la plupart de leurs utilisateurs regardent ou aiment et leurs données démographiques.

Les décisions commerciales reposent souvent sur beaucoup d'intuition et de connaissances du domaine. Maintenant, à mesure que les données deviennent de plus en plus volumineuses, il devient difficile pour nous de leur donner un sens. Nous ne sommes tout simplement pas équipés de la faculté mentale pour examiner de grands ensembles de données remplis de tonnes d'informations.

**Le but de la science des données est de vous raconter une histoire et de vous aider à la visualiser.**

En l'utilisant, vous pouvez :

* Obtenir de nombreuses informations à partir des données qui pourraient autrement passer inaperçues
* Prendre des décisions plus rapides, car après tout — les ordinateurs sont plus rapides que les humains !
* Éliminer beaucoup de biais qui interviennent dans la prise de décision. Tout au long de l'histoire, les humains ont toujours été assez enclins à laisser leurs sentiments et leurs préjugés obscurcir leur jugement...

![Image](https://cdn-media-1.freecodecamp.org/images/1*hGNOhIlImfphJf5E6VIB0g.jpeg)

Mais contrairement aux humains, les ordinateurs n'ont pas besoin de s'asseoir dans une réunion d'affaires et de se lancer dans un concours de pisse pour savoir pourquoi une certaine décision est meilleure que les autres.

Maintenant que nous avons compris de quoi il s'agit, il est temps de l'apprendre !

### Qui tirera le plus profit de ce tutoriel :

* Les personnes ayant quelques connaissances de base en programmation, qui veulent comprendre la science des données et ses applications.
* Les personnes qui trouvent les mathématiques et les statistiques un peu écrasantes au début.
* Si vous êtes même remotement intéressé par les vins, alors lisez-le — juste pour le plaisir !

### Commençons !

Dans ce tutoriel, vous comprendrez comment analyser un ensemble de données sur le vin, observer ses caractéristiques et en extraire différentes informations. Après avoir terminé ce tutoriel, vous :

* Comprendrez comment la science des données peut être utilisée pour analyser et obtenir des informations à partir des données.
* Deviendrez connaisseur en vin. ;-)

![Image](https://cdn-media-1.freecodecamp.org/images/1*OjVreh3NGN_FgBEQs4AMdg.jpeg)

Même si vous ne buvez pas, ce n'est pas grave — vous deviendrez tout de même un sommelier en herbe, ou un œnophile (oui, c'est un terme réel !).

Dans le [prochain article de blog](https://www.freecodecamp.org/news/using-machine-learning-to-predict-the-quality-of-wines-9e2e13d7480d/#what-is-machine-learning), vous verrez la science des données appliquée sous la forme de l'apprentissage automatique :

* Qu'est-ce que le ML, et quels types de problèmes peuvent être résolus en l'utilisant ?
* Comment entraîner un classificateur utilisant le ML pour identifier les bons vins des mauvais vins.
* Différentes métriques de performance

#### À savoir avant de lire :

Je suppose que vous avez déjà quelques connaissances en programmation. Certaines connaissances en programmation en **Python** sont nécessaires, donc si vous le connaissez, vous trouverez ce tutoriel relativement simple. Si ce n'est pas le cas, je vous recommande vivement de consulter ce cours gratuit sur [Introduction à Python](https://in.udacity.com/course/introduction-to-python--ud1110).

**Pourquoi Python ?** Parce qu'il émerge rapidement comme le langage de choix pour la [science des données](https://www.quora.com/Why-is-Python-a-language-of-choice-for-data-scientists). Il est relativement facile à apprendre, et l'écosystème Python dispose de nombreux outils et bibliothèques pour construire pratiquement n'importe quoi — allant des serveurs web, des packages pour l'apprentissage automatique, les statistiques, l'apprentissage profond, à l'IoT. Python dispose également de l'une des communautés les plus actives sur Internet, comme [stack overflow](https://medium.freecodecamp.org/a-path-for-you-to-learn-analytics-and-data-skills-bd48ccde7325).

Certaines connaissances de base des bibliothèques comme numpy et pandas seront également utiles, bien que non obligatoires.

#### **Ce dont vous aurez besoin pour ce tutoriel :**

* De préférence, une distribution basée sur Linux (Ubuntu ou Linux Mint) avec [Python](https://askubuntu.com/questions/865554/how-do-i-install-python-3-6-using-apt-get) installé.
* Installez [Anaconda](https://conda.io/docs/user-guide/install/linux.html). C'est un système de gestion de paquets et d'environnements open-source, principalement pour les programmes Python. Pour entraîner et tester nos modèles de machine learning, vous utiliserez une bibliothèque open-source très populaire appelée scikit-learn.
* Téléchargez les fichiers du projet depuis [ce dépôt](https://github.com/booleanhunter/ML-supervised-learning/tree/master/game-of-wines) sur votre machine. Ensuite, ouvrez un terminal, `cd` vers votre dossier de projet, et exécutez _pip install -r requirements.txt_ pour installer les dépendances.
* **Alternativement**, vous pouvez également télécharger les fichiers du projet sur [FloydHub](http://floydhub.com) et exécuter vos codes, sans les tracas de la configuration. Je le recommande si vous n'avez pas de système basé sur Linux.

Vous utiliserez un fichier notebook IPython (Interactive Python) pour exécuter votre code. Après avoir téléchargé les fichiers du projet, ouvrez votre terminal, `cd` vers votre dossier de projet, et exécutez `**jupyter-notebook**`_. Cela ouvrira une nouvelle fenêtre sur votre navigateur par défaut sur le port 8888. Si vous utilisez FloydHub, le même fichier notebook peut être exécuté depuis là-bas également.

Vous trouverez deux fichiers notebook IPython. Sélectionnez celui nommé `**game-of-wines.ipynb**` dans la liste. L'autre fichier notebook contient le code source complet de ce tutoriel.

#### **Comment utiliser ce notebook**

Le notebook contient déjà du code modèle et des explications dans les cellules pour vous aider à démarrer. À quelques endroits, vous trouverez que le code a déjà été écrit pour vous, juste pour faciliter les choses. Vous trouverez également des commentaires et des liens là où c'est nécessaire.

Pour exécuter le code dans une cellule, cliquez dessus avec votre souris, puis sélectionnez l'option `_run_` dans la barre de titre du livre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*q6Ckg8iquD7ALn2tEbjG6g.png)

### D'accord, Santé ! Buvons... oops, étudions nos données sur le vin.

Je cherchais sur Internet l'autre jour des données open-source intéressantes. Kaggle a une communauté très active où vous pouvez facilement rechercher différents types de jeux de données et résoudre des défis. Un autre endroit génial pour chercher des jeux de données est le [Dépôt d'apprentissage automatique de l'Université de Californie à Irvine](http://archive.ics.uci.edu/ml/index.php).

Le [dépôt UCI Machine Learning](http://archive.ics.uci.edu/ml/machine-learning-databases/wine/) contient deux ensembles de [données sur le vin](https://archive.ics.uci.edu/ml/datasets/wine+quality). Un jeu de données contient des informations sur les vins rouges, et l'autre sur les vins blancs. Votre dossier de projet contient déjà les deux. Ces vins ont été produits au [Vinho Verde](http://www.vinhoverde.pt/en/about-vinho-verde), une région au nord du Portugal.

Tout d'abord, vous allez importer quelques bibliothèques nécessaires pour notre analyse de données. Cliquez sur le bloc de cellule, puis sélectionnez la commande `run` pour les charger toutes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nQ_4BCh8KEKq32OMbMhdEQ.png)

Ensuite, nous allons charger notre jeu de données dans notre notebook et afficher les cinq premières lignes. Tapez ce code dans le bloc de cellule de votre notebook puis exécutez-le :

```python
# Charger le jeu de données des vins rouges
data = pd.read_csv("data/winequality-red.csv", sep=';')

# Afficher les cinq premiers enregistrements
display(data.head(n=5))
```

Il imprimera cette sortie :

![Image](https://cdn-media-1.freecodecamp.org/images/1*MEevsKTQqXaIHg1eKeRP6g.png)

Comme vous pouvez le voir, il y a environ 12 caractéristiques différentes pour chaque vin dans le jeu de données. La dernière colonne, **quality**, est une métrique de la qualité d'un vin spécifique, notée entre 1 et 10.

Vérifions si certaines de ces colonnes ont des informations manquantes. Tapez ceci dans le bloc de cellule :

```python
data.isnull().any()
```

La sortie nous montre qu'aucune colonne n'est vide.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XMlmIxFum_MZkl5A4CBiCw.png)

Nous pouvons obtenir des informations supplémentaires sur notre jeu de données en exécutant :

```python
data.info()
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*d-TRr6Kn1nkBwDiH5q5uLw.png)

Essayons d'effectuer une analyse préliminaire sur nos vins. Pour nos besoins, considérons tous les vins avec des notes de 7 et plus comme étant de très bonne qualité, les vins avec des notes de 5 et 6 comme étant de qualité moyenne, et les vins avec des notes inférieures à 5 comme étant de qualité insipide :

```python
n_wines = data.shape[0]

# Nombre de vins avec une note de qualité supérieure à 6
quality_above_6 = data.loc[(data['quality'] > 6)]
n_above_6 = quality_above_6.shape[0]

# Nombre de vins avec une note de qualité inférieure à 5
quality_below_5 = data.loc[(data['quality'] < 5)]
n_below_5 = quality_below_5.shape[0]

# Nombre de vins avec une note de qualité entre 5 et 6
quality_between_5 = data.loc[(data['quality'] >= 5) & (data['quality'] <= 6)]
n_between_5 = quality_between_5.shape[0]

# Pourcentage de vins avec une note de qualité supérieure à 6
greater_percent = n_above_6*100/n_wines

# Afficher les résultats
print("Nombre total de données sur le vin : {}".format(n_wines))
print("Vins avec une note de 7 et plus : {}".format(n_above_6))
print("Vins avec une note inférieure à 5 : {}".format(n_below_5))
print("Vins avec une note de 5 et 6 : {}".format(n_between_5))
print("Pourcentage de vins avec une qualité de 7 et plus : {:.2f}%".format(greater_percent))

# Quelques analyses de données supplémentaires
display(np.round(data.describe()))
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Sk_9x0mFcbqusrDeUoGzZA.png)

Vous pouvez également visualiser les distributions de qualité sur un graphique :

```python
# Visualiser les caractéristiques continues asymétriques des données originales
vs.distribution(data, "quality")
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*KFw6DmaqzElnPJPrAwkDhQ.png)

Comme vous pouvez le voir, la plupart des vins tombent sous la qualité moyenne. Il y a moins de vins qui sont de très haute qualité et de très bon goût, et très peu de vins qui ne sont pas si bons.

Nous pouvons également utiliser la méthode `**describe**` de pandas pour obtenir des statistiques utiles, telles que la moyenne, la médiane et l'écart-type des caractéristiques de nos données :

![Image](https://cdn-media-1.freecodecamp.org/images/1*mGzXh2XgumRjinbgd2a_rg.png)

Quelques statistiques utiles que vous devriez connaître :

* **Moyenne (Average)** : Peut-être la plus familière de toutes. Il suffit d'additionner toutes les valeurs d'échantillon pour une caractéristique donnée, puis de diviser par le nombre d'échantillons.
* **Médiane** : D'abord, vous arrangez toutes les valeurs d'échantillon dans l'ordre numérique, dans une liste. Le nombre du milieu dans cette liste sera la médiane.
* **Mode** : La valeur qui apparaît le plus dans une liste d'échantillons.
* **Plage** : La différence entre la valeur la plus élevée et la valeur la plus basse dans une liste.
* **Écart-type** : Il est utilisé pour mesurer la dispersion des valeurs dans un ensemble. Calculez d'abord la moyenne, puis soustrayez chaque nombre dans la liste avec la moyenne et élevez le résultat au carré. Ensuite, calculez la moyenne de ces différences au carré, et enfin calculez la racine carrée de celle-ci.

#### Maintenant, l'étape suivante est d'étudier les caractéristiques de notre jeu de données plus en détail.

La qualité du vin dépend d'un ensemble de propriétés chimiques qui affectent leur goût, leur arôme et leur saveur. Donc oui, même si la fabrication du vin est considérée comme un art, c'est en fait assez scientifique si vous y réfléchissez.

**En science des données, avoir des connaissances du domaine peut être le facteur clé de différenciation entre des insights médiocres et excellents.**

### Il est temps de devenir plus sage avec notre vocabulaire du vin !

Les vins contiennent des proportions variables de sucres, d'alcool, d'acides organiques, de sels d'acides minéraux et organiques, de [composés phénoliques](https://en.wikipedia.org/wiki/Phenolic_content_in_wine), de pigments, de substances azotées, de pectines, de gommes, de mucilage, de composés aromatiques volatils (esters, aldéhydes et cétones), de vitamines, de sels et de dioxyde de soufre.

En dégustation de vin, le terme **acidité** fait référence aux attributs frais, acides et aigres du vin. Trois acides primaires sont trouvés dans les raisins de vin — les acides tartrique, malique et citrique. Ils sont évalués en relation avec la façon dont l'acidité équilibre la douceur et les composants amers du vin, tels que les tanins.



* **Acidité fixe**  
  
L'acidité titrable, parfois appelée acidité fixe, est une mesure de la concentration totale des acides titrables et des ions hydrogène libres présents dans votre vin. Un [papier de tournesol](https://en.wikipedia.org/wiki/Litmus) peut être utilisé pour identifier si une solution donnée est acide ou basique. Les acides titrables les plus courants sont les acides tartrique, malique, citrique et carbonique. Ces acides, ainsi que beaucoup d'autres en plus petites quantités, se trouvent naturellement dans les raisins ou sont créés lors du processus de fermentation.



* **Acidité volatile**  
  
L'acidité volatile est principalement causée par des bactéries dans le vin créant de l'acide acétique — l'acide qui donne au vinaigre sa saveur et son arôme caractéristiques — et son sous-produit, l'acétate d'éthyle. L'acidité volatile pourrait être un indicateur de détérioration, ou d'erreurs dans les processus de fabrication — causées par des choses comme des raisins endommagés, du vin exposé à l'air, etc. Cela permet aux bactéries acétiques d'entrer et de prospérer, et de donner naissance à des goûts et des odeurs désagréables. Les experts en vin peuvent souvent le dire juste en le sentant !
* **Acide citrique**  
  
L'acide citrique est généralement trouvé en très petites quantités dans les raisins de vin. Il agit comme un conservateur et est [ajouté aux vins](http://wineserver.ucdavis.edu/industry/enology/methods_and_techniques/reagents/citric_acid.html) pour augmenter l'acidité, compléter une saveur spécifique ou prévenir les troubles ferriques. Il peut être ajouté aux vins finis pour augmenter l'acidité et donner une saveur "fraîche". Cependant, un ajout excessif peut ruiner le goût.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hD1dVJgzCqeJQvMaBX0m-w.jpeg)



* **Sucres résiduels**  
  
Les **sucres résiduels**, ou RS en abrégé, font référence à tout sucre naturel de raisin qui reste après que la fermentation cesse (que ce soit intentionnellement ou non). Le jus des raisins de **vin** commence par être intensément sucré, et la fermentation utilise ce **sucre** comme les levures le consomment.  
  
Lors de la vinification, la levure convertit généralement tout le sucre en alcool, ce qui donne un **vin** sec. Cependant, parfois, tout le sucre n'est pas fermenté par la levure, laissant un peu de [douceur résiduelle](http://winefolly.com/update/sugar-in-wine-misunderstanding/).  
  
Pour faire un vin qui a bon goût, la clé est d'avoir un équilibre parfait entre la douceur et l'acidité dans la boisson.



* **Chlorure**  
  
La quantité de chlorures présente dans un vin est généralement un indicateur de son "[salinité](http://www.aromadictionary.com/articles/salt_article.html)". Cela est [généralement influencé](https://www.researchgate.net/publication/276444447_Chloride_concentration_in_red_wines_Influence_of_terroir_and_grape_type) par le territoire où les raisins de vin ont poussé, les méthodes de culture, et aussi le type de raisin. Trop de salinité est considérée comme indésirable. La bonne proportion peut rendre le vin [plus savoureux](http://wineoscope.com/2015/10/02/when-a-wine-is-salty-and-why-it-shouldnt-be/).



* **Niveaux de dioxyde de soufre**  
  
Le dioxyde de soufre existe dans le vin sous forme libre et liée, et les combinaisons sont appelées _SO2 total_. C'est le conservateur le plus couramment utilisé, généralement ajouté par les producteurs de vin pour protéger le vin des effets négatifs de l'exposition à l'air et à l'oxygène. Les vins avec des teneurs en dioxyde de soufre ajouté ont généralement "Contient des sulfites" sur leurs étiquettes.  
  
Il agit comme un [agent de sanification](https://winobrothers.com/2011/10/11/sulfur-dioxide-so2-in-wine/) — l'ajouter tue généralement les bactéries ou levures indésirables qui pourraient entrer dans le vin et altérer son goût et son arôme. Il a été utilisé pour la première fois dans la [vinification](https://en.wikipedia.org/wiki/Sulfur_dioxide#In_winemaking) par les Romains, lorsqu'ils ont découvert que brûler des bougies de soufre à l'intérieur de récipients à vin vides les garde frais et sans odeur de vinaigre. Plutôt ingénieux, n'est-ce pas ?



* **Densité**  
  
Aussi connue sous le nom de gravité spécifique, elle peut être utilisée pour mesurer la concentration d'alcool dans les vins. Pendant la fermentation, le sucre dans le jus est converti en éthanol avec du dioxyde de carbone comme gaz résiduel. Surveiller la densité pendant le processus permet un contrôle optimal de cette étape de conversion pour des vins de la plus haute qualité. Les vins plus sucrés ont généralement des densités plus élevées.



* **pH**  
  
pH signifie pouvoir de l'hydrogène, qui est une mesure de la concentration des ions hydrogène dans la solution. Généralement, les solutions avec une valeur de pH inférieure à 7 sont considérées comme acides, avec certains des acides les plus forts étant proches de 0. Les solutions au-dessus de 7 sont considérées comme alcalines ou basiques. La valeur de pH de l'eau est de 7, car elle n'est ni un acide ni une base.



* **Sulfates**  
  
Les sulfates sont des sels de l'acide sulfurique. Ils ne sont pas impliqués dans la production de vin, mais certains brasseurs utilisent du sulfate de calcium — aussi connu sous le nom de gypse des brasseurs — pour corriger les carences minérales dans l'eau pendant le processus de brassage. Il ajoute également un peu de goût "piquant".



* **Alcool**  
  
Ah oui, l'alcool — la clé d'une fête réussie ! Les boissons alcoolisées existent depuis au moins la période néolithique (10 000 av. J.-C.). En boire en petites quantités vous donne des sensations chaudes et floues à l'intérieur, et vous rend plus sociable. Bien sûr, des doses plus élevées peuvent aussi vous faire perdre connaissance.

#### Boire avec diligence, mon ami scientifique des données !



### Exploration des relations entre les caractéristiques et les visualisations

Maintenant que vous avez quelques connaissances sur le vin, il est temps d'explorer davantage. Notre jeu de données contient un ensemble de caractéristiques comme nous l'avons vu ci-dessus, telles que les niveaux d'alcool, la quantité de sucre résiduel et la valeur du pH. Certaines de ces caractéristiques peuvent dépendre d'autres caractéristiques, d'autres non. Certaines d'entre elles peuvent affecter nos notes de qualité également.

**En science des données ou en apprentissage automatique, il est assez important d'étudier les caractéristiques qui composent nos données et de voir s'il existe des corrélations entre elles.**

Par exemple, le niveau de pH affecte-t-il les niveaux d'acidité fixe ? Les niveaux d'acidité volatile ont-ils quelque chose à voir avec la qualité ? Les gens trouvent-ils les vins avec plus de teneur en alcool plus savoureux ou de meilleure qualité ?

Heureusement pour nous, Python dispose de bibliothèques géniales qui font le gros du travail de fournir différents types de visualisations. Essayons de tracer un nuage de points avec nos données et observons ce qu'il nous montre.

```python
pd.plotting.scatter_matrix(data, alpha = 0.3, figsize = (40,40), diagonal = 'kde');
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*HbazuSH9ifkXt3YdLe970w.png)

À partir du nuage de points ci-dessus, nous pouvons obtenir quelques détails intéressants. Pour certaines des caractéristiques, la distribution semble être assez linéaire. Pour d'autres, la distribution semble être négativement asymétrique. Cela confirme donc nos soupçons initiaux — il y a effectivement des co-dépendances intéressantes entre certaines des caractéristiques.

Nous pouvons tracer une carte thermique des corrélations entre les caractéristiques, ce qui nous aidera à obtenir plus d'informations.

```python
correlation = data.corr()
# display(correlation)
plt.figure(figsize=(14, 12))
heatmap = sns.heatmap(correlation, annot=True, linewidths=0, vmin=-1, cmap="RdBu_r")
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*xtYwk9WXIzZYSP71pBMHPA.png)

Comme vous pouvez le voir, les carrés avec des valeurs positives montrent des corrélations directes entre les caractéristiques. Plus les valeurs sont élevées, plus ces relations sont fortes — elles seront plus rougeâtres. Cela signifie que si une caractéristique augmente, l'autre tend également à augmenter, et vice-versa.

Les carrés qui ont des valeurs négatives montrent une corrélation inverse. Plus ces valeurs deviennent négatives, plus elles sont inversement proportionnelles, et elles seront plus bleues. Cela signifie que si la valeur d'une caractéristique est plus élevée, la valeur de l'autre diminue.

Enfin, les carrés proches de zéro indiquent presque aucune co-dépendance entre ces ensembles de caractéristiques.

**Assez intéressant, n'est-ce pas ? Explorons ces corrélations plus en détail.**



* **pH vs. Acidité fixe**

```python
# Visualiser la corrélation entre le pH et l'acidité fixe

# Créer un nouveau dataframe contenant uniquement les colonnes pH et acidité fixe pour visualiser leurs corrélations
fixedAcidity_pH = data[['pH', 'fixed acidity']]

# Initialiser une grille jointe avec le dataframe, en utilisant la bibliothèque seaborn
gridA = sns.JointGrid(x="fixed acidity", y="pH", data=fixedAcidity_pH, size=6)

# Dessiner un graphique de régression dans la grille
gridA = gridA.plot_joint(sns.regplot, scatter_kws={"s": 10})

# Dessiner un graphique de distribution dans la même grille
gridA = gridA.plot_marginals(sns.distplot)
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*aYaw4DZCIuYPopEzAm2bSw.png)

Ce nuage de points montre comment les valeurs de pH changent avec les niveaux d'acidité fixe. Nous pouvons voir que, à mesure que les niveaux d'acidité fixe augmentent, les niveaux de pH diminuent. Cela a du sens, n'est-ce pas ? Un niveau de pH plus bas est, après tout, un indicateur d'une acidité élevée.



* **Acidité fixe vs. Acide citrique**

```python
fixedAcidity_citricAcid = data[['citric acid', 'fixed acidity']]
g = sns.JointGrid(x="fixed acidity", y="citric acid", data=fixedAcidity_citricAcid, size=6)
g = g.plot_joint(sns.regplot, scatter_kws={"s": 10})
g = g.plot_marginals(sns.distplot)
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*D2KxLMLEuYAH-mXc5aXyxA.png)

À mesure que la quantité d'acides citriques augmente, les niveaux d'acidité fixe augmentent également.



* **Acidité volatile vs Qualité**

```python
fig, axs = plt.subplots(ncols=1,figsize=(10,6))
sns.barplot(x='quality', y='volatile acidity', data=volatileAcidity_quality, ax=axs)
plt.title('qualité VS acidité volatile')

plt.tight_layout()
plt.show()
plt.gcf().clear()
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*XMNAItj-Vhx5MLWDE4OIGg.png)

Une qualité plus élevée est généralement associée à des niveaux d'acidité volatile bas. Cela a du sens, car l'acidité volatile est un indicateur de détérioration et pourrait donner naissance à des arômes désagréables — conformément à nos connaissances du domaine.



* **Alcool vs. Qualité**

```python
fig, axs = plt.subplots(ncols=1,figsize=(10,6))
sns.barplot(x='quality', y='alcohol', data=quality_alcohol, ax=axs)
plt.title('qualité VS alcool')

plt.tight_layout()
plt.show()
plt.gcf().clear()
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*GO-8WU9vd5F0NI1W3KgZgA.png)

Hmm. Il semble que la plupart des gens aiment généralement les vins qui contiennent un pourcentage plus élevé d'alcool, ceux qui les rendent étourdis !

Essayez d'expérimenter avec plus de caractéristiques par vous-même dans le notebook, et voyez si elles révèlent quelque chose. Si elles sont liées d'une certaine manière, quelle pourrait être la raison ? L'exploration révélerait plus d'informations cachées.

Il est utile de se rappeler que **la corrélation ne signifie pas toujours causalité**. Parfois, lorsque vous tracez des graphiques pour deux caractéristiques, cela peut vous montrer un motif qui pourrait être une coïncidence. Voici un exemple —

![Image](https://cdn-media-1.freecodecamp.org/images/1*RIUFJsPh2cSekqrrklscDg.png)
_[ici](http://philosophy.hku.hk/think/sci/inference.php" data-href="http://philosophy.hku.hk/think/sci/inference.php" class="markup--anchor markup--figure-anchor" rel="nofollow noopener noopener" target="_blank">http://philosophy.hku.hk/think/sci/inference.php</a>. Vous pouvez consulter plus d'exemples <a href="http://tylervigen.com/spurious-correlations" data-href="http://tylervigen.com/spurious-correlations" class="markup--anchor markup--figure-anchor" rel="noopener" target="_blank)._

**Alors pourquoi le faisons-nous ?** Cela sert de base utile pour voir si l'intégrité de notre jeu de données est intacte !

Par exemple, nous savons avec certitude que les niveaux de pH doivent diminuer si les niveaux d'acidité augmentent. Mais si nos graphiques montrent le contraire, alors c'est un indicateur que quelque chose ne va pas — notre jeu de données n'est pas fiable. Et cela pourrait rendre nos prédictions fausses ! C'est là que le fait d'avoir des connaissances du domaine se révèle à nouveau utile.

## Détection des valeurs aberrantes

Disons que dans le royaume des Lannister, il y a environ 10 000 adultes. La plupart d'entre eux sont de taille moyenne (plus de 5 pieds), mais il y a environ 100 personnes qui sont des nains. Ce sont aussi des valeurs aberrantes, car ce sont des valeurs extrêmes qui sortent de la plage attendue des tailles. En d'autres termes, une valeur aberrante est un point de données qui est significativement distant de la plupart des autres points de données.

**Pourquoi sont-elles importantes ?** Parce qu'elles peuvent parfois causer beaucoup de problèmes dans l'analyse des données. Disons que vous essayez de calculer la température moyenne de 10 objets sélectionnés aléatoirement dans votre pièce, et que neuf d'entre eux sont entre 20 et 25 degrés Celsius. Mais vous avez laissé votre four allumé, et il est à 175 °C. La température médiane sera entre 20 et 25 °C, mais la température moyenne sera entre 35,5 et 40 °C. Dans ce cas, la médiane reflète mieux la température d'un objet échantillonné aléatoirement, car cela correspond à ce qui est attendu dans votre pièce.

Ainsi, la détection des valeurs aberrantes est cruciale, car des valeurs très petites ou très grandes peuvent affecter négativement notre analyse de données, et par conséquent nos prédictions. Il devient donc parfois nécessaire de les supprimer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*agLdxu5nfP-2H-0xgFnUQg.jpeg)

### Méthode de Tukey pour détecter les valeurs aberrantes

J'ai lu un [très bon article](http://datapigtechnologies.com/blog/index.php/highlighting-outliers-in-your-data-with-the-tukey-method/) sur cette méthode que vous pourriez lire plus tard. Mais en bref, voici comment fonctionne la technique :

* Tout d'abord, vous commencez par diviser les données triées en **quatre** intervalles, de telle manière que les sections résultantes contiennent chacune environ 25 % du total des points de données. Les valeurs auxquelles ces intervalles sont divisés sont appelées **Quartiles**.
* Ensuite, vous soustrayez le 3ème Quartile du 1er Quartile pour obtenir l'**Intervalle Interquartile (IQR)**. C'est le milieu de 50 %, et il contient la majorité des données.
* Tout point de données qui se trouve au-delà de **1,5** fois l'IQR serait considéré comme une valeur aberrante.

Exécutez le code suivant dans le bloc de code suivant pour imprimer les valeurs aberrantes pour toutes les caractéristiques de votre jeu de données.

```python
# Pour chaque caractéristique, trouver les points de données avec des valeurs extrêmement élevées ou basses
for feature in data.keys():
    # TODO: Calculer Q1 (25ème percentile des données) pour la caractéristique donnée
    Q1 = np.percentile(data[feature], q=25)
    
    # TODO: Calculer Q3 (75ème percentile des données) pour la caractéristique donnée
    Q3 = np.percentile(data[feature], q=75)
    
    # TODO: Utiliser l'intervalle interquartile pour calculer une étape de valeur aberrante (1,5 fois l'intervalle interquartile)
    interquartile_range = Q3 - Q1
    step = 1.5 * interquartile_range
    
    # Afficher les valeurs aberrantes
    print("Points de données considérés comme des valeurs aberrantes pour la caractéristique '{}' :".format(feature))
    display(data[~((data[feature] >= Q1 - step) & (data[feature] <= Q3 + step))])
    
    # OPTIONNEL: Sélectionner les indices des points de données que vous souhaitez supprimer
    outliers = []
    # Supprimer les valeurs aberrantes, si certaines ont été spécifiées
    good_data = data.drop(data.index[outliers]).reset_index(drop = True)
```

**Et... nous avons terminé !**

J'espère que vous avez pris du plaisir avec ce tutoriel. Maintenant, vous en savez plus sur la science des données qu'avant !

![Image](https://cdn-media-1.freecodecamp.org/images/1*HXZPFY1XtYmySMtUmOZf8w.jpeg)
_Le seul moment où vous vous sentirez vraiment comme Tyrion Lannister_

Bien sûr, il y a plus que ce que l'on voit. Si vous souhaitez en savoir plus, je vous recommande vivement de consulter ces ressources :

* [Cours de statistiques et de probabilités](https://medium.freecodecamp.org/if-you-want-to-learn-data-science-take-a-few-of-these-statistics-classes-9bbabab098b9)
* [Introduction à Python pour la science des données](https://www.datacamp.com/tracks/python-programming?tap_a=5644-dce66f&tap_s=93618-a68c98)
* [Les meilleurs cours de science des données sur Internet](https://medium.freecodecamp.org/the-best-data-science-courses-on-the-internet-ranked-by-your-reviews-6dc5b910ea40)
* [Comment devenir un data scientist](https://medium.freecodecamp.org/how-to-become-a-data-scientist-2d829fa33aba)

Mais pour l'instant, prenez une pause et passez au tutoriel suivant, où vous plongerez dans des concepts fondamentaux de l'apprentissage automatique. Vous apprendrez à construire un modèle d'apprentissage automatique, auquel, si vous lui donnez des attributs de vin, il vous donnera une note de qualité précise !

[**Utilisation de l'apprentissage automatique pour prédire la qualité des vins**](https://medium.freecodecamp.org/using-machine-learning-to-predict-the-quality-of-wines-9e2e13d7480d)

> Également publié dans mon [blog tech](https://blog.booleanhunter.com/using-data-science-to-understand-what-makes-wine-taste-good/). _Aimé ce que vous avez lu ? Allez-y et [abonnez-vous](https://forum.booleanhunter.com/) ! Je ne perdrai pas votre temps._

N'hésitez pas à laisser un commentaire ci-dessous si vous avez des questions, ou si vous souhaitez un tutoriel sur un sujet intéressant.