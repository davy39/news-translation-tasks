---
title: Qu'est-ce que les Réseaux de Neurones Graphiques ? Comment les GNN fonctionnent,
  expliqué avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-02-01T16:50:35.000Z'
originalURL: https://freecodecamp.org/news/graph-neural-networks-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/download-1.png
tags:
- name: Machine Learning
  slug: machine-learning
- name: MathJax
  slug: mathjax
- name: neural networks
  slug: neural-networks
seo_title: Qu'est-ce que les Réseaux de Neurones Graphiques ? Comment les GNN fonctionnent,
  expliqué avec des exemples
seo_desc: 'By Rishit Dagli

  Graph Neural Networks are getting more and more popular and are being used extensively
  in a wide variety of projects.

  In this article, I help you get started and understand how graph neural networks
  work while also trying to address t...'
---

Par Rishit Dagli

Les Réseaux de Neurones Graphiques deviennent de plus en plus populaires et sont utilisés de manière extensive dans une grande variété de projets.

Dans cet article, je vous aide à commencer et à comprendre comment les réseaux de neurones graphiques fonctionnent tout en essayant de répondre à la question "pourquoi" à chaque étape. 

Enfin, nous examinerons également la mise en œuvre de certaines des méthodes dont nous parlons dans cet article en code.

Et ne vous inquiétez pas – vous n'aurez pas besoin de connaître beaucoup de mathématiques pour comprendre ces concepts et apprendre à les appliquer.

## Qu'est-ce qu'un graphe ?

Pour faire simple, un graphe est une collection de nœuds et des arêtes entre les nœuds. Dans le diagramme ci-dessous, les cercles blancs représentent les nœuds, et ils sont connectés par des arêtes, les lignes de couleur rouge. 

Vous pourriez continuer à ajouter des nœuds et des arêtes au graphe. Vous pourriez également ajouter des directions aux arêtes, ce qui en ferait un graphe dirigé.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-89.png)
_Une représentation simple d'un graphe_

Quelque chose de très pratique est la matrice d'adjacence, qui est une façon d'exprimer le graphe. Les valeurs de cette matrice \(A_{ij}\) sont définies comme suit :

$$A_{ij} = \left\{\begin{array}{ c l }1 & \quad \textrm{si une arête existe } j \rightarrow i \\  0  & \quad \textrm{si aucune arête n'existe} \end{array} \right.$$

Une autre façon de représenter la matrice d'adjacence consiste simplement à inverser la direction, donc dans la même équation \(A_{ij}\) sera 1 s'il y a une arête \(i \rightarrow j\) à la place. 

La dernière représentation est en fait ce que j'ai étudié à l'école. Mais souvent dans les articles de Machine Learning, vous trouverez la première notation utilisée – donc pour cet article, nous allons nous en tenir à la première représentation.

Il y a beaucoup de choses intéressantes que vous pourriez remarquer à partir de la matrice d'adjacence. Tout d'abord, vous pourriez remarquer que si le graphe est non dirigé, vous obtenez essentiellement une matrice symétrique et des propriétés plus intéressantes, surtout avec les valeurs propres de cette matrice. 

Une telle interprétation qui serait utile dans ce contexte est de prendre les puissances de la matrice \((A^n)_{ij}\) qui nous donne le nombre de (directed ou undirected) walks de longueur \(n\) entre les nœuds \(i\) et \(j\).

## Pourquoi travailler avec des données sous forme de graphes ?

Les graphes sont utilisés dans toutes sortes de scénarios courants et ont de nombreuses applications possibles. 

Probablement l'application la plus courante de la représentation des données par des graphes est l'utilisation de graphes moléculaires pour représenter des structures chimiques. Ceux-ci ont aidé à prédire les longueurs de liaison, les charges et de nouvelles molécules.

Avec les graphes moléculaires, vous pouvez utiliser le Machine Learning pour prédire si une molécule est un médicament puissant. 

Par exemple, vous pourriez entraîner un réseau de neurones graphiques pour prédire si une molécule inhibe certaines bactéries et l'entraîner sur une variété de composés dont vous connaissez les résultats.

Ensuite, vous pourriez essentiellement appliquer votre modèle à n'importe quelle molécule et découvrir qu'une molécule précédemment négligée fonctionnerait en fait comme un excellent antibiotique. C'est ainsi que [Stokes et al.](https://www.sciencedirect.com/science/article/pii/S0092867420301021) dans leur article (2020) ont prédit un nouvel antibiotique appelé Halicin.

Un autre article intéressant de DeepMind ([ETA Prediction with Graph Neural Networks in Google Maps](https://arxiv.org/abs/2108.11482), 2021) a modélisé les cartes de transport sous forme de graphes et a exécuté un réseau de neurones graphiques pour améliorer la précision des ETAs jusqu'à 50% dans Google Maps. 

Dans cet article, ils partitionnent les itinéraires de voyage en super segments qui modélisent une partie de l'itinéraire. Cela leur a donné une structure de graphe sur laquelle ils exécutent un réseau de neurones graphiques.

Il y a eu d'autres articles intéressants qui représentent des données naturellement présentes sous forme de graphes (réseaux sociaux, circuits électriques, diagrammes de Feynman et plus) qui ont fait des découvertes significatives également. 

Et si vous y réfléchissez, un réseau de neurones standard peut également être représenté sous forme de graphe 🧠.

## Que pouvons-nous faire avec les Réseaux de Neurones Graphiques ?

Commençons d'abord par ce que nous pourrions vouloir faire avec notre réseau de neurones graphiques avant de comprendre comment nous pourrions le faire. 

Un type de sortie que nous pourrions vouloir de notre réseau de neurones graphiques est au niveau du graphe entier, pour avoir un seul vecteur de sortie. Vous pourriez relier ce type de sortie à la prédiction de l'ETA ou à la prédiction de l'énergie de liaison à partir d'une structure moléculaire des exemples dont nous avons parlé.

Un autre type de sortie que vous pourriez vouloir est les prédictions au niveau des nœuds ou des arêtes et obtenir un vecteur pour chaque nœud ou arête. Vous pourriez relier cela à un exemple où vous devez _classer_ chaque nœud dans la prédiction ou probablement prédire l'angle de liaison pour toutes les liaisons données la structure moléculaire.

Vous pourriez également être intéressé à répondre à la question "Où devrais-je placer une nouvelle arête ou un nouveau nœud" ou prédire où une arête ou un nœud pourrait apparaître. Nous pourrions non seulement obtenir cette prédiction à partir du graphe, mais nous pourrions également transformer d'autres données en un graphe.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-90.png)
_Définir ce que nous voulons que notre GNN fasse_

Comme vous l'avez peut-être deviné avec le réseau de neurones graphiques, nous voulons d'abord générer un graphe de sortie ou des latents à partir desquels nous pourrions ensuite travailler sur cette grande variété de tâches standard. 

Donc, essentiellement, ce que nous devons faire _à partir du graphe latent_ (caractéristiques pour chaque nœud représentées comme \(\vec{h_i}\)) pour les prédictions au niveau du graphe est :

* d'abord trouver un moyen d'agréger tous les vecteurs (comme simplement les additionner), et 
* puis créer une fonction pour obtenir les prédictions :

$$\vec{Z_G} = f(\sum_i \vec{h_i})$$

Et maintenant, il est assez simple de montrer à un niveau élevé ce que nous devons faire à partir des latents pour obtenir nos sorties. 

Pour les sorties au niveau des nœuds, nous aurions simplement un vecteur de nœud passé dans notre fonction et obtenir les prédictions pour ce nœud :

$$\vec{Z_i} = f(\vec{h_i})$$

## Le problème des entrées de taille variable

Maintenant que nous savons ce que nous pouvons faire avec les réseaux de neurones graphiques et pourquoi vous pourriez vouloir représenter vos données sous forme de graphes, voyons comment nous pourrions procéder à l'entraînement sur des données graphiques.

Mais d'abord, nous avons un problème entre les mains : les graphes sont essentiellement des entrées de taille variable. Dans un réseau de neurones standard, comme le montre la figure ci-dessous, la couche d'entrée (représentée dans la figure par \(x_i\)) a un nombre fixe de neurones. Dans ce réseau, vous ne pouvez pas soudainement appliquer le réseau à une entrée de taille variable.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-99.png)
_Pourquoi le réseau de neurones standard ne fonctionnera pas ?_

Mais si vous vous souvenez, vous pouvez appliquer des réseaux de neurones convolutionnels sur des entrées de taille variable. 

Mettons cela en termes d'un exemple : vous avez une convolution avec le nombre de filtres \(K=5\), l'étendue spatiale \(F=2\), le pas \(S=4\), et aucun remplissage zéro \(P=0\). Vous pouvez passer des entrées \((256 \times 256 \times 3)\) et obtenir des sorties \((64 \times 64 \times 5)\) (\(\left \lfloor{\frac{256-2+0}{4}+1}\right \rfloor\)) et vous pouvez également passer des entrées \((96 \times 96 \times 6)\) et obtenir des sorties \((24 \times 24 \times 5)\) et ainsi de suite – c'est essentiellement indépendant de la taille. 

Cela nous fait nous demander si nous pouvons tirer quelque inspiration des réseaux de neurones convolutionnels.

Une autre façon vraiment intéressante de résoudre le problème des tailles d'entrée variables qui s'inspire de la physique vient de l'article [Learning to Simulate Complex Physics with Graph Networks](https://arxiv.org/abs/2002.09405) de DeeepMind (2020). 

Commençons par prendre quelques particules \(i\) et chacune de ces particules a une certaine localisation \(\vec{r_i}\) et une certaine vitesse \(\vec{v_i}\). Supposons que ces particules ont des ressorts entre elles pour nous aider à comprendre les interactions.

Maintenant, ce système est, bien sûr, un graphe : vous pouvez prendre les particules comme des nœuds et les ressorts comme des arêtes. Si vous vous souvenez de la physique simple du lycée, \(force = masse \cdot accélération\) – et, bien, quelle est une autre façon dans ce système de désigner la force totale agissant sur la particule ? C'est la somme des forces agissant sur toutes les particules voisines. 

Vous pouvez maintenant écrire (\(e_{ij}\) représente les propriétés de l'arête ou du ressort entre i et j) :

$$m\frac{\mathrm{d} \vec{v_i}}{\mathrm{d}t} = \sum_{j \in \textrm{ voisins de } i } \vec{F}(\vec{r_i}, \vec{r_j}, e_{ij})$$

Quelque chose que je voudrais attirer votre attention ici est que cette loi de force est toujours la même. Peut-être y a-t-il des différences dans les propriétés du ressort ou de l'arête, mais vous pouvez toujours appliquer la même loi. Vous pouvez avoir différents nombres de nœuds et d'arêtes et vous pouvez toujours appliquer la même équation de mouvement.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/download-2.png)
_Visualisation des solutions présentées pour les entrées de taille variable_

Si vous regardez de près, les intuitions que nous avons discutées pour contourner le problème des entrées fixes ont un aspect de similarité entre elles : il est assez clair en écrivant que la deuxième approche prend en compte les nœuds et les arêtes voisins et crée une fonction (ici la force) de ceux-ci. Je voulais souligner que la façon dont les réseaux de neurones convolutionnels fonctionnent n'est pas très différente.

## Comment apprendre à partir des données dans un graphe

Maintenant que nous avons discuté de ce qui pourrait nous inspirer pour créer un réseau de neurones graphiques, essayons maintenant d'en construire un. Ici, nous verrons comment nous pouvons apprendre à partir des données résidant dans un graphe. 

Nous commencerons par parler du "**Neural Message Passing**" qui est _analogue_ aux filtres dans un réseau de neurones convolutionnel ou à la force dont nous avons parlé dans la section précédente.

Donc, supposons que nous avons un graphe avec 3 nœuds (dirigés ou non dirigés). Comme vous l'avez peut-être deviné, nous avons une valeur correspondante pour chaque nœud \(x_1\), \(x_2\) et \(x_3\). 

Tout comme n'importe quel réseau de neurones, notre objectif est de trouver un algorithme pour mettre à jour ces valeurs de nœuds, ce qui est analogue à une couche dans le réseau de neurones graphiques. Et puis vous pouvez bien sûr continuer à ajouter de telles couches.

Alors, comment faites-vous ces mises à jour ? Une idée serait d'utiliser les arêtes dans notre graphe. Aux fins de cet article, supposons que parmi les 3 nœuds, nous avons une arête pointant de \(x_3 \rightarrow x_1\). Nous pouvons envoyer un message le long de cette arête qui transportera une valeur qui sera calculée par un réseau de neurones.

Pour ce cas, nous pouvons l'écrire comme ci-dessous (et nous allons décomposer ce que cela signifie aussi) :

$$\vec{m_{31}}=f_e(\vec{h_3}, \vec{h_1}, \vec{e_{31}})$$

Nous utiliserons nos mêmes notations :

* \(m_31\) est le message passé du nœud 3 au nœud 1, 
* \(\vec{h_3}\) est la valeur que le nœud 3 a, 
* \(\vec{e_{31}}\) est la valeur de l'arête entre le nœud 3 et le nœud 1, et 
* \(f_e\) représente la fonction "quelque réseau de neurones" qui dépend de toutes ces valeurs, souvent appelée la fonction de message.

Et disons que nous avons également une arête de \(x_2 \rightarrow x_1\). Nous pouvons appliquer la même expression que nous avons créée ci-dessus, en remplaçant simplement les numéros de nœuds. 

Si vous avez plus de nœuds, vous voudrez faire cela pour chaque arête pointant vers le nœud 1. Et le moyen le plus simple de les accumuler est de les additionner simplement. Regardez de près et vous verrez que cela est vraiment similaire à l'intuition des particules que nous avons discutée plus tôt !

Maintenant, vous avez une valeur agrégée des messages arrivant au nœud 2, mais vous devez encore mettre à jour ses poids. Nous utiliserons donc un autre réseau de neurones \(f_v\) souvent appelé le réseau de mise à jour. Il dépend de deux choses : votre valeur originale du nœud 3 bien sûr et l'agrégat des messages que nous avions.

En mettant simplement ces éléments ensemble non seulement pour le nœud 3 dans notre exemple mais pour n'importe quel nœud dans n'importe quel graphe, nous pouvons l'écrire comme :

$$\vec{h_i^{\prime}} = f_v(h_i, \sum_{j \in N_i} \vec{m_{ij}})$$

\(\vec{h_i^{\prime}}\) sont nos valeurs de nœuds mises à jour, et \(\vec{m_{ij}}\) sont les messages arrivant au nœud \(i\) que nous avons calculés plus tôt. 

Vous appliqueriez ensuite ces deux mêmes réseaux de neurones \(f_e\) et \(f_v\) pour chacun des nœuds composant le graphe. 

Une chose vraiment importante à noter ici est que les deux réseaux de neurones où nous devons mettre à jour nos valeurs de nœuds fonctionnent sur des entrées de **taille fixe** comme un réseau de neurones standard. Généralement, les deux réseaux de neurones dont nous avons parlé \(f_e\) et \(f_v\) sont de petits MLP.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-130.png)
_Visualisation des Réseaux de Neurones à Passage de Messages_

Plus tôt, nous avons parlé des différents types de sorties qui nous intéressent d'obtenir de nos réseaux de neurones graphiques. Vous avez peut-être déjà remarqué que lors de l'entraînement de notre modèle de la manière dont nous en avons parlé, nous serons en mesure de générer les prédictions au niveau des nœuds : un vecteur pour chaque nœud. 

Pour effectuer la classification de graphes, nous voulons essayer d'agréger toutes les valeurs de nœuds que nous avons après avoir entraîné notre réseau. Nous utiliserons une couche de lecture ou de pooling (il est assez clair comment le nom vient). 

Généralement, nous pouvons créer une fonction \(f_r\) dépendant de l'ensemble des valeurs de nœuds. Mais elle doit également être indépendante de la permutation (ne doit pas dépendre de votre choix d'étiquetage des nœuds), et elle devrait ressembler à ceci :

$$y^{\prime} = f_r({x_i \vert i \in \textrm{ graphe} })$$

La manière la plus simple de définir une fonction de lecture serait de faire la somme de toutes les valeurs de nœuds. Ensuite, trouver la moyenne, le maximum, ou le minimum, ou même une combinaison de ces propriétés invariantes par permutation qui conviennent le mieux à la situation. Votre \(f_r\), comme vous l'avez peut-être deviné, peut également être un réseau de neurones qui est souvent utilisé en pratique.

Les idées et les intuitions dont nous venons de parler créent les Message Passing Neural Networks (MPNNs), l'un des réseaux de neurones graphiques les plus puissants, proposé pour la première fois dans [Neural Message Passing for Quantum Chemistry](http://proceedings.mlr.press/v70/gilmer17a.html) (Gilmer et al. 2017).

### Comment changer les valeurs des arêtes

Il semble maintenant que nous avons effectivement créé un réseau de neurones graphiques général. Mais vous pouvez voir que notre réseau de messages nécessite \(e_{ij}\), la propriété de l'arête – tout comme vous initialisez aléatoirement les valeurs des nœuds au début. 

Mais tandis que les valeurs des nœuds changent à chaque étape, les valeurs des arêtes sont également initialisées par vous – mais elles ne sont pas changées. Donc, nous devons essayer de généraliser cela aussi, une extension de ce que nous venons de voir.

En comprenant comment fonctionnent les mises à jour des nœuds, je pense que vous pouvez très facilement appliquer quelque chose de similaire pour une fonction de mise à jour des arêtes également. 

\(U_{edge}\) est un autre réseau de neurones standard :

$$e_{ij}^{\prime} = U_{edge}(e_{ij}, x_i, x_j)$$

Quelque chose que vous pourriez également faire avec ce cadre est que les sorties par \(U_{edge}\) sont déjà des propriétés au niveau des arêtes – alors pourquoi ne pas les utiliser simplement comme mon message ? Eh bien, vous pourriez faire cela aussi.

### Discussion sur les Message Passing Neural Networks

Les Message Passing Neural Networks (MPNN) sont les couches de réseaux de neurones graphiques les plus générales. Mais cela nécessite le stockage et la manipulation des messages des arêtes ainsi que des caractéristiques des nœuds. 

Cela peut devenir un peu problématique en termes de mémoire et de représentation. Donc, parfois, ceux-ci souffrent de problèmes de scalabilité et, en pratique, sont applicables à des graphes de petite taille. 

Comme le dit Petar Veličković, "les MPNN sont les MLP du domaine des graphes". Nous examinerons quelques extensions des MPNN ainsi que comment implémenter un MPNN en code.

Vous pouvez assez facilement appliquer exactement ce dont nous avons parlé dans PyTorch ou TensorFlow – mais essayez de le faire et vous verrez que cela fait exploser la mémoire.

Habituellement, ce que nous faisons avec les réseaux de neurones standards est de travailler sur des lots de données. Donc, vous passez généralement un tableau d'entrée de forme [taille du lot, # de neurones d'entrée] au réseau de neurones pour le faire fonctionner efficacement. 

Maintenant, notre nombre de neurones d'entrée ici n'est pas le même que mis en évidence précédemment, et oui, les réseaux de neurones convolutionnels traitent des images de taille arbitraire. Mais lorsque vous pensez en termes de lots, vous avez besoin que toutes les images aient les mêmes dimensions.

Il y a plusieurs choses que vous pourriez faire :

* Opérer avec un seul graphe à la fois (bien sûr très inefficace)
* Vous pourriez également agréger vos graphes en un grand graphe et ne pas permettre aux messages de passer d'un des plus petits graphes à un autre petit graphe. Cela introduirait des complications lors de la réalisation de prédictions au niveau du graphe et vous devriez adapter votre fonction de lecture.
* Vous pourriez également utiliser des Ragged Tensors qui sont des tenseurs de longueur variable : un excellent tutoriel peut être trouvé [ici](https://www.tensorflow.org/guide/ragged_tensor).
* Tirer à nouveau l'inspiration des CNN : vous pourriez utiliser le remplissage de sorte que votre lot ait, par exemple, des graphes de différentes tailles. Donc, vous prenez simplement un graphe avec 7 nœuds et définissez les 3 nœuds restants à 0. Il en va de même pour un graphe avec 8 nœuds, définissez les 2 nœuds restants à 0.

## Autres architectures GNN populaires

Dans cette section, je vais vous donner un aperçu de quelques autres couches de réseaux de neurones graphiques largement utilisées. 

Nous ne regarderons pas l'intuition derrière chacune de ces couches et comment chaque partie s'assemble dans la fonction de mise à jour. Au lieu de cela, je vais simplement vous donner un aperçu de haut niveau de ces méthodes. Vous pourriez certainement lire les articles originaux pour obtenir une meilleure compréhension.

### Graph Convolutional Networks

L'une des architectures GNN les plus populaires est [Graph Convolutional Networks](https://arxiv.org/abs/1609.02907) (GCN) par Kipf et al. qui est essentiellement une méthode spectrale. 

Les méthodes spectrales fonctionnent avec la représentation d'un graphe dans le [domaine spectral](https://arxiv.org/abs/1312.6203). Spectral ici signifie que nous utiliserons les vecteurs propres du Laplacien. 

Les GCN sont basés sur ChebNets qui proposent que la représentation des caractéristiques de tout vecteur ne devrait être affectée que par son voisinage à k-sauts. Nous calculerions notre convolution en utilisant les polynômes de Chebyshev.

Dans un GCN, cela est simplifié à \(K=1\). Nous commencerons par définir une matrice de degré (sommation ligne par ligne de la matrice d'adjacence) :

$$\tilde{D}_{ij}=\sum_j\tilde{A}_{ij}$$

La règle de mise à jour du réseau de convolution graphique après avoir utilisé une normalisation symétrique peut être écrite où H est la matrice des caractéristiques et W est la matrice des poids entraînables :

$$H^{\prime}=\sigma(\tilde{D}^{-1/2} \tilde{A}\tilde{D}^{-1/2} HW)$$

Nœud par nœud, vous pouvez écrire cela comme où \(N_i\) et \(N_j\) sont les tailles des voisinages des nœuds :

$$\vec{h_i^{\prime}} = \sigma(\sum_{i \in N_j} \frac{1}{\sqrt{|N_i||N_j|}} W \vec{h_j^{\prime}} )$$

Bien sûr, avec GCN, vous n'avez plus de caractéristiques d'arêtes, et l'idée qu'un nœud peut envoyer une valeur à travers le graphe que nous avions avec MPNN dont nous avons discuté plus tôt.

### Graph Attention Network

Rappelez-vous la règle de mise à jour nœud par nœud dans GCN que nous venons de voir ? \(\frac{1}{\sqrt{|N_i||N_j|}}\) est dérivé de la matrice de degré du graphe. 

Dans [Graph Attention Network](https://arxiv.org/abs/1710.10903) (GAT) par Veličković et al., ce coefficient \(\alpha_{ij}\) est calculé implicitement. Donc pour une arête particulière, vous prenez les caractéristiques du nœud émetteur, du nœud récepteur, et des caractéristiques de l'arête également et vous les passez à travers une fonction d'attention.

$$a_{ij}=a(\vec{h_i}, \vec{h_j}, \vec{e_{ij}})$$

\(a\) pourrait être n'importe quel mécanisme d'auto-attention apprenable et partagé comme les transformers. Ceux-ci pourraient ensuite être normalisés avec une fonction softmax à travers le voisinage :

$$\alpha_{ij}=\frac{e^{a_{ij}}}{\sum_{k \in N_i} e^{a_{ik}}}$$

Cela constitue la règle de mise à jour du GAT. Les auteurs émettent l'hypothèse que cela pourrait être significativement stabilisé avec une auto-attention multi-têtes. Voici une visualisation par les auteurs de l'article montrant une étape du GAT.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-131.png)
_Une seule étape du GAT_

Cette méthode est également très scalable car elle devait calculer un _scalaire_ pour l'influence de la forme du nœud i au nœud j et noter un vecteur comme dans MPNN. Mais cela n'est probablement pas aussi général que les MPNN, cependant.

## Implémentation de code pour les Réseaux de Neurones Graphiques

Avec plusieurs frameworks comme PyTorch Geometric, TF-GNN, Spektral (basé sur TensorFlow) et plus, il est en effet assez simple d'implémenter des réseaux de neurones graphiques. Nous verrons quelques exemples ici en commençant par les MPNNs.

Voici comment vous créez un réseau de neurones à passage de messages similaire à celui de l'article original "Neural Message Passing for Quantum Chemistry" avec PyTorch Geometric :

```python
import torch.nn as nn
import torch.nn.functional as F
import torch_geometric.transforms as T
from torch_geometric.utils import normalized_cut
from torch_geometric.nn import NNConv, global_mean_pool, graclus, max_pool, max_pool_x


def normalized_cut_2d(edge_index, pos):
    row, col = edge_index
    edge_attr = torch.norm(pos[row] - pos[col], p=2, dim=1)
    return normalized_cut(edge_index, edge_attr, num_nodes=pos.size(0))


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        nn1 = nn.Sequential(
            nn.Linear(2, 25), nn.ReLU(), nn.Linear(25, d.num_features * 32)
        )
        self.conv1 = NNConv(d.num_features, 32, nn1, aggr="mean")

        nn2 = nn.Sequential(nn.Linear(2, 25), nn.ReLU(), nn.Linear(25, 32 * 64))
        self.conv2 = NNConv(32, 64, nn2, aggr="mean")

        self.fc1 = torch.nn.Linear(64, 128)
        self.fc2 = torch.nn.Linear(128, d.num_classes)

    def forward(self, data):
        data.x = F.elu(self.conv1(data.x, data.edge_index, data.edge_attr))
        weight = normalized_cut_2d(data.edge_index, data.pos)
        cluster = graclus(data.edge_index, weight, data.x.size(0))
        data.edge_attr = None
        data = max_pool(cluster, data, transform=transform)

        data.x = F.elu(self.conv2(data.x, data.edge_index, data.edge_attr))
        weight = normalized_cut_2d(data.edge_index, data.pos)
        cluster = graclus(data.edge_index, weight, data.x.size(0))
        x, batch = max_pool_x(cluster, data.x, data.batch)

        x = global_mean_pool(x, batch)
        x = F.elu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        return F.log_softmax(self.fc2(x), dim=1)
```

Vous pouvez trouver un notebook Colab complet démontrant l'implémentation [ici](https://colab.research.google.com/drive/11gtwzl_E4TWqEswwv5mZh4ZWHRz0b3PA?usp=sharing), et il est en effet assez lourd. Il est assez simple de l'implémenter dans TensorFlow également, et vous pouvez trouver un tutoriel complet sur [Keras Examples ici](https://keras.io/examples/graph/mpnn-molecular-graphs).

L'implémentation d'un GCN est également assez simple avec PyTorch Geometric. Vous pouvez facilement l'implémenter avec TensorFlow également, et vous pouvez trouver un notebook Colab complet [ici](https://colab.research.google.com/drive/1Dgs2rpYleGGTYg0ciCX792zGpfQrtp4p?usp=sharing).

```python
class Net(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = GCNConv(dataset.num_features, 16, cached=True,
                             normalize=not args.use_gdc)
        self.conv2 = GCNConv(16, dataset.num_classes, cached=True,
                             normalize=not args.use_gdc)

    def forward(self):
        x, edge_index, edge_weight = data.x, data.edge_index, data.edge_attr
        x = F.relu(self.conv1(x, edge_index, edge_weight))
        x = F.dropout(x, training=self.training)
        x = self.conv2(x, edge_index, edge_weight)
        return F.log_softmax(x, dim=1)
```

Et maintenant, essayons d'implémenter un GAT. Vous pouvez trouver le notebook Colab complet [ici](https://colab.research.google.com/drive/1gzRJsRbUUVesxj5bxMz3zkapwdeTuR8F?usp=sharing).

```python
class Net(torch.nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()

        self.conv1 = GATConv(in_channels, 8, heads=8, dropout=0.6)
        # Sur le jeu de données Pubmed, utilisez heads=8 dans conv2.
        self.conv2 = GATConv(8 * 8, out_channels, heads=1, concat=False,
                             dropout=0.6)

    def forward(self, x, edge_index):
        x = F.dropout(x, p=0.6, training=self.training)
        x = F.elu(self.conv1(x, edge_index))
        x = F.dropout(x, p=0.6, training=self.training)
        x = self.conv2(x, edge_index)
        return F.log_softmax(x, dim=-1)
```

## Conclusion

Merci d'être resté avec moi jusqu'à la fin. J'espère que vous avez appris une ou deux choses sur les réseaux de neurones graphiques et que vous avez apprécié de lire comment ces intuitions pour les réseaux de neurones graphiques se forment en premier lieu.

Si vous avez appris quelque chose de nouveau ou apprécié la lecture de cet article, veuillez le partager afin que d'autres puissent le voir. En attendant, à la prochaine publication !

Enfin, pour le lecteur motivé, parmi d'autres, je vous encourage également à lire l'article original "The Graph Neural Network Model" où le GNN a été proposé pour la première fois, car il est vraiment intéressant. Une archive en accès libre de l'article peut être trouvée [ici](https://persagen.com/files/misc/scarselli2009graph.pdf). Cet article s'inspire également de [Theoretical Foundations of Graph Neural Networks](https://www.youtube.com/watch?v=uF53xsT7mjc) et [CS224W](http://web.stanford.edu/class/cs224w/index.html) que je vous suggère de consulter.

Vous pouvez également me trouver sur Twitter [@rishit_dagli](https://twitter.com/rishit_dagli), où je tweete sur le machine learning et un peu sur Android.