---
title: Visualisez le graphe d'influence des langages de programmation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-30T14:38:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-visualize-the-programming-language-influence-graph-7f1b765b44d1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*B2TjLzIuTc7OgugSSt-VAA.png
tags:
- name: Gephi
  slug: gephi
- name: data
  slug: data
- name: Data Science
  slug: data-science
- name: network
  slug: network
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
seo_title: Visualisez le graphe d'influence des langages de programmation
seo_desc: 'By Peter Gleeson

  A network visualization tutorial with Gephi and Sigma.js

  Here’s a preview of what we’ll be making today: the programming languages influence
  graph. Check out the link to explore the “design influence” relationships between
  over 250 p...'
---

Par Peter Gleeson

#### Un tutoriel de visualisation de réseau avec Gephi et Sigma.js

Voici un aperçu de ce que nous allons créer aujourd'hui : [le graphe d'influence des langages de programmation](http://programming-languages.herokuapp.com/). Consultez le lien pour explorer les relations de "design influence" entre plus de 250 langages de programmation passés et présents !

### À votre tour !

Dans le monde hyperconnecté d'aujourd'hui, les réseaux sont un aspect omniprésent de la vie moderne.

Prenez le début de ma journée jusqu'à présent — j'ai utilisé le **réseau de transport** de Londres pour me rendre en ville. Ensuite, je suis allé dans une **succursale** de mon café préféré et j'ai utilisé mon Chromebook pour me connecter à leur **réseau Wi-Fi**. Ensuite, je me suis connecté aux différents sites de **réseaux sociaux** que je fréquente.

Ce n'est un secret pour personne que certaines des entreprises les plus influentes des dernières décennies doivent leur succès à la puissance des réseaux.

Facebook, Twitter, Instagram, LinkedIn et autres plateformes de médias sociaux s'appuient sur les propriétés de petit monde des réseaux sociaux. Cela leur permet de connecter leurs utilisateurs entre eux (et avec les annonceurs) de manière efficace.

Google doit une grande partie de son succès actuel à sa domination précoce du marché des moteurs de recherche — rendue possible en partie grâce à sa capacité à retourner des résultats pertinents avec l'aide de son [algorithme de réseau Page Rank](https://en.wikipedia.org/wiki/PageRank).

Le réseau de distribution efficace d'Amazon leur permet d'offrir une livraison le jour même dans certaines grandes villes.

Les réseaux sont également super-importants dans des domaines tels que l'intelligence artificielle et l'apprentissage automatique. Les [réseaux de neurones](http://neuralnetworksanddeeplearning.com/) sont un domaine de recherche très actif. De nombreux algorithmes de détection de caractéristiques, essentiels en vision par ordinateur, s'appuient fortement sur [l'utilisation de réseaux pour modéliser différentes parties des images](http://www.sci.utah.edu/~gerig/CS7960-S2010/handouts/Shi-Malik-CVPR-1997.pdf).

Une large gamme de phénomènes scientifiques peuvent également être compris en termes de modèles de réseaux. Cela inclut la [mécanique quantique](https://en.wikipedia.org/wiki/Quantum_graph), les [voies biochimiques](https://en.wikipedia.org/wiki/Metabolic_pathway), et les systèmes [écologiques](https://en.wikipedia.org/wiki/Ecological_network) et [socio-économiques](https://web.stanford.edu/~jacksonm/socialnetecon-chapter.pdf).

Étant donné leur importance indéniable, comment pouvons-nous mieux comprendre les réseaux et leurs propriétés ?

L'étude mathématique des réseaux est connue sous le nom de "[théorie des graphes](http://mathworld.wolfram.com/Graph.html)", et est l'une des branches les plus accessibles des mathématiques. Cet article vise à fournir une introduction, en supposant peu de connaissances ou d'expérience préalables.

Nous utiliserons Python 3.x et un logiciel open-source génial appelé [Gephi](https://gephi.org/) pour mettre ensemble une visualisation de réseau montrant comment une gamme de langages de programmation passés et présents sont liés par influence.

### Mais d'abord...

Qu'est-ce qu'un réseau exactement ?

Les exemples décrits ci-dessus nous donnent quelques indices. Les réseaux de transport sont composés de **destinations** connectées par des **routes**. Les réseaux sociaux sont composés d'**individus**, connectés par leurs **relations** les uns avec les autres. Les algorithmes du moteur de recherche de Google évaluent le "rang" de différentes **pages web** en regardant quelles pages **lien** vers d'autres.

Plus généralement, un réseau est tout système qui peut être décrit en termes de **nœuds** et de **liens**, ou en termes familiers, de "points et de lignes".

![Image](https://cdn-media-1.freecodecamp.org/images/wX7gSLvSAawXdKmCwDAecCgiCwDaESN4-d8v)
_Un exemple de nœuds (langages) connectés par des liens (influence de design)_

Certains systèmes sont facilement abstraits de cette manière. Les réseaux sociaux sont peut-être l'exemple le plus évident. Les systèmes de fichiers informatiques en sont un autre — les dossiers et les fichiers sont liés par leurs relations "parent" et "enfant".

Mais la vraie puissance des réseaux vient du fait que de nombreux systèmes peuvent être abstraits et modélisés en termes de réseaux, même si au premier abord ce n'est pas évident.

### Représentation des réseaux

Nous devons aller un peu au-delà des croquis sur papier pour analyser et décrire les réseaux mathématiquement. Comment pouvons-nous transformer des images de points et de lignes en nombres que nous pouvons traiter ?

Une solution consiste à établir une **matrice d'adjacence** pour représenter notre réseau.

Les matrices sont l'un de ces concepts qui peuvent sembler un peu intimidants si vous n'êtes pas familier avec eux, mais n'ayez crainte. Pensez à eux comme des grilles de nombres qui peuvent être utilisées pour effectuer de nombreux calculs en une seule fois. Voici un exemple ci-dessous :

```
      Python Java Scala C#
Python     0    1     0  0
Java       0    0     0  1
Scala      0    1     0  0
C#         0    1     0  0
```

Dans cette matrice, l'intersection de chaque ligne et colonne est soit 0 soit 1, selon que les langages respectifs sont liés ou non. Vous pouvez vérifier cela contre l'illustration ci-dessus !

Pour la plupart des usages, la matrice d'adjacence est un bon moyen de représenter un réseau mathématiquement. D'un point de vue computationnel, cependant, elle peut parfois être un peu encombrante.

Par exemple, même avec un nombre relativement modeste de nœuds (disons 1000), il y aura un nombre beaucoup plus grand d'éléments dans la matrice (par exemple, 1000² = 1 000 000).

De nombreux systèmes réels produisent des **réseaux clairsemés**. Dans ces réseaux, la plupart des nœuds ne se connectent qu'à une petite proportion de tous les autres.

Si nous représentions un réseau clairsemé de 1000 nœuds en mémoire informatique sous forme de matrice d'adjacence, nous aurions 1 000 000 octets de données stockés en RAM. La plupart seront des zéros. Il doit y avoir une manière plus efficace de procéder.

Une approche alternative consiste à travailler avec des **listes de liens** à la place. Elles sont exactement ce qu'elles disent être. Elles sont simplement une liste de paires de nœuds qui se lient les uns aux autres.

Par exemple, le réseau de langages de programmation ci-dessus peut être représenté comme suit :

```
Java, Python
Java, Scala
Java, C#
C#, Java
```

Pour les réseaux plus grands, c'est un moyen beaucoup plus efficace sur le plan computationnel de les représenter. Il est bien sûr possible de générer une matrice d'adjacence à partir d'une liste de liens (et vice versa). Ce n'est pas comme si nous devions choisir l'un ou l'autre.

Un autre moyen de représenter les réseaux sont les [listes d'adjacence](https://en.wikipedia.org/wiki/Adjacency_list). Cela liste chaque nœud suivi des nœuds auxquels il est lié. Par exemple :

```
Java: Python, Scala, C#
C#: Java
```

### Collecte de données, établissement de connexions

Tout modèle et visualisation de réseau ne sera aussi bon que les données utilisées pour le construire. Cela signifie que, tout en veillant à ce que les données soient à la fois précises et complètes, nous devons également justifier un moyen d'inférer les liens entre les nœuds.

À bien des égards, c'est _l'_étape critique. Toute analyse et inférence ultérieures faites sur le réseau dépendent de la capacité à justifier le "critère de liaison".

Par exemple, dans [l'analyse des réseaux sociaux](https://en.wikipedia.org/wiki/Social_network_analysis), vous pourriez lier les personnes en fonction de leur suivi mutuel sur les médias sociaux. En biologie moléculaire, vous pourriez lier les gènes en fonction de leur [co-expression](https://en.wikipedia.org/wiki/Gene_co-expression_network).

Souvent, la méthode utilisée pour lier les nœuds permettra d'assigner des **poids** aux liens, donnant une mesure de "force".

Par exemple, dans le contexte de la vente au détail en ligne, vous pourriez lier les produits en fonction de la fréquence à laquelle ils sont achetés ensemble. Les produits qui sont fréquemment achetés ensemble seraient liés par un **lien pondéré** plus élevé que les produits qui ne sont parfois achetés ensemble. Les produits qui sont achetés ensemble pas plus souvent que ce qui serait attendu par hasard ne seraient pas liés du tout.

Comme vous pouvez l'imaginer, les méthodes pour lier les nœuds les uns aux autres peuvent être aussi sophistiquées que vous le souhaitez.

Cependant, pour ce tutoriel, nous utiliserons un moyen plus simple de connecter les langages de programmation. Nous allons nous appuyer sur la précision de Wikipédia.

Pour nos besoins, cela devrait être bien. Le succès de Wikipédia témoigne qu'il doit faire quelque chose de bien. La méthode open-source et collaborative par laquelle les articles sont écrits devrait garantir un certain degré d'objectivité.

De plus, sa structure de page relativement cohérente en fait un terrain de jeu pratique pour essayer des techniques de web-scraping.

Un autre bonus est l'API Wikipédia extensive et [bien documentée](https://www.mediawiki.org/wiki/API:Main_page), qui facilite encore la récupération d'informations. Commençons.

### Étape 1 — Installation de Gephi

Gephi est disponible sur Linux, Mac et Windows. Vous pouvez le télécharger [ici](https://gephi.org/users/download/).

Pour ce projet, j'utilisais Lubuntu. Si vous êtes sur Ubuntu/Debian, alors vous pouvez suivre les étapes ci-dessous pour installer et exécuter Gephi. Sinon, le processus d'installation sera probablement très similaire à ce que vous connaissez.

Téléchargez la dernière version (au moment de l'écriture, c'était la v.0.9.1) de Gephi pour votre système. Une fois prêt, vous devrez extraire les fichiers.

```
cd Downloads
tar -xvzf gephi-0.9.1-linux.tar.gz
cd gephi-0.9.1/bin./gephi
```

Vous devrez peut-être vérifier votre version de la JRE Java. Gephi nécessite une version récente. Sur mon installation relativement fraîche de Lubuntu, j'ai simplement installé le default-jre, et tout a fonctionné à partir de là.

```
apt install default-jre
./gephi
```

Il y a une étape supplémentaire avant que vous ne soyez prêt à commencer. Afin d'exporter le graphe sur le Web, vous pouvez utiliser le plugin [Sigma.js](http://sigmajs.org/) pour Gephi.

À partir de la barre de menu de Gephi, choisissez l'option "Outils", et sélectionnez "Plugins".

Cliquez sur l'onglet "Plugins disponibles" et sélectionnez "SigmaExporter" (j'ai également installé JSON Exporter, car c'est un autre plugin utile à avoir sous la main).

Cliquez sur le bouton "Installer" et vous serez guidé à travers le processus. Vous devrez redémarrer Gephi une fois que vous aurez terminé.

### Étape 2 — Écriture du script Python

Ce tutoriel utilisera Python 3.x, plus quelques modules pour faciliter la vie. En utilisant l'installateur de modules pip, exécutez la commande suivante :

```
pip3 install wikipedia
```

Maintenant, dans un nouveau répertoire, créez un fichier appelé quelque chose comme `script.py`, et ouvrez-le dans votre éditeur de code/IDE préféré. Voici un aperçu de la logique principale :

1. Tout d'abord, vous aurez besoin d'une [liste de langages de programmation](https://en.wikipedia.org/wiki/List_of_programming_languages) à inclure.
2. Ensuite, parcourez cette liste et récupérez le HTML de l'article Wikipédia pertinent.
3. À partir de cela, extrayez une liste de langages de programmation que chaque langage a influencés. Ce sera un critère de liaison rapide.
4. Pendant que vous y êtes, il serait bien de récupérer quelques métadonnées sur chaque langage.
5. Enfin, vous voudrez écrire toutes les données que vous avez collectées dans un fichier .csv

Le script complet peut être trouvé dans [ce gist](https://gist.github.com/anonymous/2a6c841fe04ebc6d55acc259b4ac4f72).

#### Importer quelques modules

Dans `script.py`, commencez par importer quelques modules qui faciliteront les choses :

```python
import csv
import wikipedia
import urllib.request
from bs4 import BeautifulSoup as BS
import re
```

OK — commencez par faire une liste de nœuds à inclure. C'est là que le module [Wikipedia](https://github.com/goldsmith/Wikipedia) est utile. Il facilite l'accès à l'[API Wikipedia](https://www.mediawiki.org/wiki/API:Main_page).

Ajoutez le code suivant :

```python
pageTitle = "List of programming languages"
nodes = list(wikipedia.page(pageTitle).links)
print(nodes)
```

Si vous sauvegardez et exécutez ce script, vous verrez qu'il imprime toutes les liens de l'article Wikipedia "List of programming languages". Bien !

Cependant, il est toujours judicieux d'inspecter manuellement toute donnée collectée automatiquement. Un rapide coup d'œil révélera que, en plus de nombreux langages de programmation réels, le script a également capturé quelques liens supplémentaires.

Par exemple, vous pourriez voir "[List of markup languages](https://en.wikipedia.org/wiki/List_of_markup_languages)", "[Comparison of programming languages](https://en.wikipedia.org/wiki/Comparison_of_programming_languages)" et d'autres.

Bien que Gephi vous permette de supprimer les nœuds que vous ne souhaitez pas inclure, il ne serait pas inutile de "nettoyer" les données avant de continuer. Si rien d'autre, cela vous fera gagner du temps plus tard.

```python
removeList = [
    "List of",
    "Lists of",
    "Timeline",
    "Comparison of",
    "History of",
    "Esoteric programming language"
    ]

nodes = [i for i in nodes if not any(r in i for r in removeList)]
```

Ces lignes définissent une liste de sous-chaînes à supprimer des données. Le script parcourt ensuite les données, supprimant tous les éléments qui contiennent l'une des sous-chaînes indésirables.

En Python, cela nécessite seulement une ligne de code !

#### Quelques fonctions d'aide

Maintenant, vous pouvez commencer à scraper Wikipedia pour construire une liste de liens (et collecter des métadonnées). Pour faciliter cela, définissez d'abord quelques fonctions.

#### Récupération du HTML

La première fonction utilise le module [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) pour obtenir le HTML de la page Wikipedia de chaque langage.

```python
base = "https://en.wikipedia.org/wiki/"

def getSoup(n):
    try:
        with urllib.request.urlopen(base+n) as response:
            soup = BS(response.read(),'html.parser')
            table = soup.find_all("table",class_="infobox vevent")[0]                return table
     except:
         pass
```

Cette fonction utilise le module urllib.request pour obtenir le HTML de la page à l'adresse "https://en.wikipedia.org/wiki/" + "langage de programmation".

Cela est ensuite passé à BeautifulSoup, qui lit et analyse le HTML en un objet que nous pouvons utiliser pour rechercher des informations.

Ensuite, utilisez la méthode `find_all()` pour extraire l'élément HTML qui vous intéresse.

Ici, ce sera le tableau récapitulatif en haut de chaque article sur les langages de programmation. Comment peuvent-ils être identifiés ?

La manière la plus simple est de visiter l'une des pages des langages de programmation. Ici, vous pouvez simplement utiliser les outils de développement du navigateur pour inspecter les éléments d'intérêt.

Le tableau récapitulatif a la balise HTML `<table>` et les classes CSS "infobox" et "vevent", vous pouvez donc utiliser celles-ci pour identifier le tableau dans le HTML.

Spécifiez cela avec les arguments :

* `"table"` et
* `class_="infobox vevent"`

`find_all()` retourne une liste de tous les éléments qui correspondent aux critères. Afin de spécifier réellement l'élément qui vous intéresse, ajoutez l'index `[0]`. Si la fonction réussit, elle retourne l'objet `table`. Sinon, elle retourne `None`.

![Image](https://cdn-media-1.freecodecamp.org/images/IrVevOkpMM7vIAcU21xwTYBfEllSPVaIzI72)
_Les données que nous recherchons sont dans cet élément HTML !_

Avec toute procédure de collecte de données automatisée, il est toujours important de gérer les exceptions de manière approfondie. Sinon, dans le meilleur des cas, le script plante et vous devrez recommencer.

Dans le pire des cas, vous vous retrouverez avec un ensemble de données truffé d'incohérences et d'erreurs. Cela le rendra cauchemardesque à utiliser par la suite.

#### Récupération des métadonnées

La fonction suivante utilise l'objet `table` pour rechercher des métadonnées. Ici, elle recherche dans le tableau l'année où le langage est apparu pour la première fois.

```python
def getYear(t):
    try:
        t = t.get_text()
        year = t[t.find("appear"):t.find("appear")+30]
        year = re.match(r'.*([1-3][0-9]{3})',year).group(1)
        return int(year)
    except:
        return "Could not determine"
```

Cette courte fonction prend l'objet `table` comme argument, et utilise la fonction `get_text()` de BeautifulSoup pour produire une chaîne.

L'étape suivante consiste à créer une sous-chaîne appelée `year`. Celle-ci prend les 30 caractères après la première apparition du mot `"appear"`. Cette chaîne devrait contenir l'année où le langage est apparu pour la première fois.

Afin d'extraire uniquement l'année, utilisez une **expression régulière** (grâce au module `re`) pour faire correspondre tout caractère qui commence par un chiffre entre 1 et 3, et est suivi de trois chiffres.

```python
re.match(r'.*([1-3][0-9]{3})',year)
```

Si cela réussit, la fonction retourne `year` sous forme d'entier. Sinon, elle retourne un triste "Could not determine". Vous pourriez souhaiter scraper davantage de métadonnées — telles que le paradigme, le concepteur ou la discipline de typage.

#### Collecte des liens

Une fonction de plus pour vous — cette fois, vous allez alimenter l'objet `table` pour un langage donné, et espérons recevoir une liste d'autres langages de programmation.

```python
def getLinks(t):
    try:
        table_rows = t.find_all("tr")
        for i in range(0,len(table_rows)-1):
            try:
                if table_rows[i].get_text() == "\nInfluenced\n":
                    out = []
                    for j in table_rows[i+1].find_all("a"):
                        try:
                            out.append(j['title'])
                        except:
                            continue
                    return out
            except:
                continue
        return
    except:
        return
```

Woah, regardez toute cette imbrication... Que se passe-t-il ici alors ?

Cette fonction utilise le fait que les objets `table` ont une structure cohérente. Les informations dans le tableau sont stockées dans des lignes (la balise HTML pertinente est `<tr>`). L'une de ces lignes contiendra le texte `"\nInfluenced\n"`. La première partie de la fonction trouve quelle ligne c'est.

Une fois cette ligne trouvée, vous pouvez alors être assez sûr que la ligne suivante contient des liens vers chacun des langages de programmation influencés par le langage actuel. Trouvez ces liens en utilisant `find_all("a")` — où l'argument `"a"` correspond à la balise HTML `<a>`.

Pour chaque lien `j`, ajoutez son attribut `["title"]` à une liste appelée `out`. La raison de s'intéresser à l'attribut `["title"]` est que celui-ci correspondra _exactement_ au nom du langage tel que stocké dans `nodes`.

Par exemple, Java est stocké dans `nodes` sous le nom `"Java (programming language)"`, vous devez donc utiliser ce nom exact dans tout l'ensemble de données.

Si elle réussit, `getLinks()` retourne une liste de langages de programmation. Le reste de la fonction traite la gestion des exceptions, au cas où quelque chose irait mal à une étape quelconque.

#### Collecte des données

Enfin, vous êtes presque prêt à vous asseoir et à laisser le script faire son travail. Il collectera les données et les stockera dans deux objets de liste.

```python
edgeList = [["Source,Target"]]
meta = [["Id","Year"]]
```

Maintenant, écrivez une boucle qui appliquera les fonctions définies précédemment à chaque élément de `nodes`, et stockera les résultats dans `edgeList` et `meta`.

```python
for n in nodes:
    try:
        temp = getSoup(n)
    except:
        continue
    try:
        influenced = getLinks(temp)
        for link in influenced:
            if link in nodes:
                edgeList.append([n+","+link])
                print([n+","+link])
    except:
        continue
    year = getYear(temp)
    meta.append([n,year])
```

Cette fonction prend chaque langage dans `nodes` et tente de récupérer le tableau récapitulatif de sa page Wikipedia.

Ensuite, elle récupère tous les langages que le tableau liste comme ayant été influencés par le langage en question.

Pour chaque langage qui apparaît également dans la liste `nodes`, ajoutez un élément à `edgeList` sous la forme `["source,target"]`. De cette manière, vous construirez une liste de liens à alimenter dans Gephi.

À des fins de débogage, imprimez chaque élément ajouté à `edgeList` — juste pour être sûr que tout fonctionne comme il se doit. Si vous étiez particulièrement minutieux, vous pourriez ajouter des instructions d'impression aux clauses `except`, aussi.

Ensuite, obtenez le nom et l'année du langage, et ajoutez ceux-ci à la liste `meta`.

#### Écriture en CSV

Une fois la boucle exécutée, la dernière étape consiste à écrire le contenu de `edgeList` et `meta` dans des fichiers de valeurs séparées par des virgules (CSV). Cela se fait facilement avec le module `csv` importé précédemment.

```python
with open("edge_list.csv","w") as f: 
    wr = csv.writer(f)
    for e in edgeList:
        wr.writerow(e)

with open("metadata.csv","w") as f2:
    wr = csv.writer(f2)
    for m in meta:
        wr.writerow(m)
```

Terminé ! Enregistrez le script, et depuis le terminal exécutez :

`$ python3 script.py`

Vous devriez voir le script imprimer chaque paire source-cible au fur et à mesure qu'il construit la liste de liens. Assurez-vous que votre connexion Internet est stable, et asseyez-vous pendant que le script fait sa magie.

### Étape 3 — Construction de graphes avec Gephi

Espérons que vous avez installé et exécuté Gephi plus tôt. Maintenant, vous pouvez créer un nouveau projet et utiliser les données que vous avez collectées pour construire un graphe dirigé. Cela montrera comment différents langages de programmation se sont influencés les uns les autres !

Commencez par créer un nouveau projet dans Gephi, et basculez vers la vue "Data Laboratory". Cela fournit une interface de type tableur pour gérer les données dans Gephi. La première chose à faire est d'importer la liste de liens.

* Cliquez sur "Import spreadsheet".
* Choisissez le fichier `edge_list.csv` généré par le script Python. Assurez-vous que Gephi sait utiliser les virgules comme séparateur.
* Choisissez "Edge List" dans le type de liste.
* Cliquez sur "Next" et vérifiez que vous importez les colonnes Source et Target comme des chaînes.

Cela devrait mettre à jour le Data Lab avec une liste de nœuds. Maintenant, importez le fichier `metadata.csv`. Cette fois, assurez-vous de choisir "Nodes list" dans le type de liste.

Passez à l'onglet "Preview", et voyez à quoi ressemble le réseau.

Ah... C'est juste un peu... monochrome. Et désordonné. Comme une assiette de spaghettis. Réparons cela.

#### Le rendre joli

Il existe toutes sortes de façons de travailler sur la présentation, et c'est là qu'intervient un peu de liberté créative. Avec les visualisations de réseaux, il y a essentiellement trois choses à prendre en considération :

1. **Positionnement** Il existe plusieurs algorithmes qui peuvent générer des motifs de disposition pour un réseau. Un choix populaire est l'[algorithme de Fruchterman-Reingold](https://schneide.wordpress.com/tag/fruchterman-reingold/), qui est disponible dans Gephi.
2. **Taille** La taille des nœuds dans un graphe peut être utilisée pour représenter une propriété intéressante. Souvent, il s'agit d'une **mesure de centralité**. Il existe [de nombreuses façons de mesurer la centralité](https://en.wikipedia.org/wiki/Centrality), mais elles reflètent toutes l'"importance" d'un nœud donné, en termes de sa connectivité au reste du réseau.
3. **Coloration** Il est également possible d'utiliser la couleur pour montrer une propriété d'un nœud. Souvent, la couleur est utilisée pour indiquer la **structure communautaire**. Cela est largement défini comme un "groupe de nœuds qui sont plus connectés entre eux qu'avec le reste du graphe". Dans un réseau social, cela peut révéler des groupes d'amis, de famille ou de professionnels. Il existe plusieurs [algorithmes qui peuvent détecter la structure communautaire](https://en.wikipedia.org/wiki/Community_structure#Algorithms_for_finding_communities). Gephi est livré avec la [méthode de Louvain](https://en.wikipedia.org/wiki/Louvain_Modularity) intégrée.

Pour apporter ces modifications, vous devrez calculer quelques statistiques. Passez à la fenêtre "Overview". Ici, vous verrez un panneau à droite. Il devrait contenir un onglet "Statistics". Ouvrez-le, et vous verrez une gamme d'options.

Gephi est livré avec de nombreuses capacités statistiques intégrées. Pour chacune d'elles, cliquer sur "Run" générera un rapport qui révélera des informations sur le réseau.

Quelques-unes utiles à connaître incluent :

* **Degré moyen** Le langage moyen est connecté à environ quatre autres. Le rapport montre également un graphique de [distribution de degré](https://en.wikipedia.org/wiki/Degree_distribution). Cela révèle que la plupart des langages ont très peu de connexions, tandis qu'une petite proportion en ont beaucoup. Cela suggère que ceci est un **réseau sans échelle**. Beaucoup de recherches ont été faites sur les [réseaux sans échelle](http://barabasi.com/f/124.pdf), et les processus qui les génèrent.
* **Diamètre** Ce réseau a un diamètre de 12 — ce qui signifie que c'est le nombre de connexions le plus "large" entre deux langages. La longueur moyenne du chemin est juste en dessous de quatre. Cela signifie que, en moyenne, deux langages sont séparés par quatre liens. Ces chiffres donnent une mesure de la "taille" du réseau.
* **Modularité** Il s'agit d'un score qui montre à quel point le réseau est "compartimenté". Ici, le score de modularité est d'environ 0,53. Cela est relativement élevé, suggérant qu'il existe des modules distincts au sein de ce réseau. Encore une fois, cela indique quelque chose d'intéressant sur le système sous-jacent. Les langages tendent à se regrouper en groupes d'"influence" distincts.

En tout cas, pour modifier l'apparence du réseau, dirigez-vous vers le panneau de gauche.

Dans l'onglet "Layout", vous pouvez sélectionner quel algorithme de disposition utiliser. Cliquez sur "Run" et regardez le graphe se déplacer en temps réel ! Voyez quel algorithme de disposition vous pensez fonctionner le mieux.

Au-dessus de l'onglet Layout se trouve l'onglet "Appearance". Ici, vous pouvez jouer avec différents paramètres pour les couleurs, tailles et étiquettes des nœuds et des liens. Ceux-ci peuvent être configurés en fonction des attributs (y compris les statistiques que vous obtenez de Gephi pour calculer).

En tant que suggestion, vous pourriez :

* Colorier les nœuds par leur attribut de Modularité. Cela les colorie selon leur appartenance à la communauté.
* Dimensionner les nœuds par leur Degré. Les nœuds mieux connectés apparaîtront plus grands que les moins connectés.

Cependant, vous devriez expérimenter et trouver une disposition que vous préférez.

Une fois que vous êtes satisfait de l'apparence de votre graphe, il est temps de passer à l'étape finale — l'exportation vers le Web !

### Étape 4 — Sigma.js

Vous avez déjà construit une visualisation de réseau qui peut être explorée dans Gephi. Vous pourriez choisir de prendre une capture d'écran, ou d'enregistrer le graphe au format SVG, PDF ou PNG.

Cependant, si vous avez installé le plugin Sigma.js plus tôt, pourquoi ne pas exporter le graphe en HTML ? Cela créera une visualisation interactive que vous pourrez héberger en ligne, ou télécharger sur GitHub et partager avec d'autres.

Pour ce faire, sélectionnez "Export > Sigma.js template…" dans la barre de menu de Gephi.

Remplissez les détails comme requis. Assurez-vous de choisir dans quel répertoire vous exportez le projet. Vous pouvez changer le titre, la légende, la description, le comportement au survol et de nombreux autres détails. Lorsque vous êtes prêt, cliquez sur "OK".

Maintenant, si vous naviguez vers le répertoire où vous avez exporté le projet, vous verrez un dossier contenant tous les fichiers générés par Sigma.js.

Ouvrez `index.html` dans votre navigateur préféré. Ta-da ! Voici votre réseau ! Si vous connaissez un peu CSS et JavaScript, vous pouvez plonger dans les différents fichiers générés pour ajuster la sortie comme vous le souhaitez.

Et cela conclut ce tutoriel !

### Résumé

* De nombreux systèmes peuvent être modélisés et visualisés sous forme de réseaux. La théorie des graphes est une branche des mathématiques qui fournit des outils pour aider à comprendre les structures et les propriétés des réseaux.
* Vous avez utilisé Python pour scraper des données de Wikipedia afin de construire un graphe d'influence des langages de programmation. Le critère de liaison était de savoir si un langage donné était listé comme une influence sur la conception d'un autre.
* Gephi et Sigma.js sont des outils open-source qui vous permettent d'analyser et de visualiser des réseaux. Ils vous permettent d'exporter le réseau au format image, PDF ou Web.

Merci d'avoir lu — j'attends avec impatience vos commentaires ou questions ! Pour une ressource fantastique pour en apprendre davantage sur la théorie des graphes, consultez le livre interactif en ligne d'[Albert-László Barabási](https://en.wikipedia.org/wiki/Albert-L%C3%A1szl%C3%B3_Barab%C3%A1si) [ici](http://barabasi.com/networksciencebook/).

Le code complet de ce tutoriel peut être trouvé [ici](https://gist.github.com/anonymous/2a6c841fe04ebc6d55acc259b4ac4f72).