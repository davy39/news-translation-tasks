---
title: Les réseaux de neurones de deep learning expliqués en anglais simple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-28T20:17:06.000Z'
originalURL: https://freecodecamp.org/news/deep-learning-neural-networks-explained-in-plain-english
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a02740569d1a4ca22ff.jpg
tags:
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
seo_title: Les réseaux de neurones de deep learning expliqués en anglais simple
seo_desc: 'By Nick McCullum

  Machine learning, and especially deep learning, are two technologies that are changing
  the world.

  After a long "AI winter" that spanned 30 years, computing power and data sets have
  finally caught up to the artificial intelligence alg...'
---

Par Nick McCullum

[L'apprentissage automatique](https://gumroad.com/l/pGjwd), et surtout le deep learning, sont deux technologies qui changent le monde.

Après un long "hiver de l'IA" qui a duré 30 ans, la puissance de calcul et les ensembles de données ont enfin rattrapé les algorithmes d'intelligence artificielle proposés pendant la seconde moitié du vingtième siècle. 

Cela signifie que les modèles de deep learning sont enfin utilisés pour faire des prédictions efficaces qui résolvent des problèmes réels.

Il est plus important que jamais pour les data scientists et les ingénieurs logiciels d'avoir une compréhension de haut niveau du fonctionnement des modèles de deep learning. Cet article expliquera l'histoire et les concepts de base des réseaux de neurones de deep learning en anglais simple. 

## **L'histoire du Deep Learning**

[Le deep learning](https://nickmccullum.com/python-deep-learning/what-is-deep-learning/) a été conceptualisé par [Geoffrey Hinton](https://en.wikipedia.org/wiki/Geoffrey_Hinton) dans les années 1980. Il est largement considéré comme le père fondateur du domaine du deep learning. Hinton travaille chez Google depuis mars 2013, lorsque sa société, DNNresearch Inc., a été acquise.

La principale contribution de Hinton au domaine du deep learning a été de comparer les techniques d'apprentissage automatique au cerveau humain.

Plus spécifiquement, il a créé le concept de "réseau de neurones", qui est un algorithme de deep learning structuré de manière similaire à l'organisation des neurones dans le cerveau. Hinton a adopté cette approche parce que le cerveau humain est sans doute le moteur de calcul le plus puissant connu aujourd'hui.

La structure créée par Hinton a été appelée un réseau de neurones artificiels (ou réseau de neurones artificiels en abrégé). Voici une brève description de leur fonctionnement :

* Les réseaux de neurones artificiels sont composés de couches de nœuds
* Chaque nœud est conçu pour se comporter de manière similaire à un neurone dans le cerveau
* La première couche d'un réseau de neurones est appelée la couche `input`, suivie des couches `hidden`, puis enfin la couche `output`
* Chaque nœud du réseau de neurones effectue un certain type de calcul, qui est transmis à d'autres nœuds plus profonds dans le réseau de neurones

Voici une visualisation simplifiée pour démontrer comment cela fonctionne :

![Une visualisation d'un réseau de neurones artificiels](https://nickmccullum.com/images/python-deep-learning/what-is-deep-learning/artificial-neural-net.png)

Les réseaux de neurones représentaient une avancée immense dans le domaine du deep learning.

Cependant, il a fallu des décennies pour que l'apprentissage automatique (et surtout le deep learning) gagne en importance.

Nous explorerons pourquoi dans la section suivante.

## **Pourquoi le Deep Learning n'a pas immédiatement fonctionné**

Si le deep learning a été conçu à l'origine il y a des décennies, pourquoi ne commence-t-il à prendre de l'ampleur qu'aujourd'hui ?

C'est parce que tout modèle de deep learning mature nécessite une abondance de deux ressources :

* Données
* Puissance de calcul

À l'époque de la naissance conceptuelle du deep learning, les chercheurs n'avaient pas accès à suffisamment de données ou de puissance de calcul pour construire et entraîner des modèles de deep learning significatifs. Cela a changé avec le temps, ce qui a conduit à la prééminence du deep learning aujourd'hui.

# **Comprendre les neurones en Deep Learning**

[Les neurones](https://nickmccullum.com/python-deep-learning/understanding-neurons-deep-learning/) sont un composant critique de tout modèle de deep learning.

En fait, on pourrait dire que vous ne pouvez pas comprendre pleinement le deep learning sans avoir une connaissance approfondie du fonctionnement des neurones.

Cette section vous présentera le concept de neurones en deep learning. Nous parlerons de l'origine des neurones de deep learning, de la manière dont ils ont été inspirés par la biologie du cerveau humain, et de l'importance des neurones dans les modèles de deep learning aujourd'hui.

## **Qu'est-ce qu'un neurone en biologie ?**

Les neurones en deep learning ont été inspirés par les neurones du cerveau humain. Voici un diagramme de l'anatomie d'un neurone cérébral :

![L'anatomie d'un neurone dans le cerveau](https://nickmccullum.com/images/python-deep-learning/understanding-neurons-deep-learning/neuron-anatomy.png)

Comme vous pouvez le voir, les neurones ont une structure assez intéressante. Des groupes de neurones travaillent ensemble à l'intérieur du cerveau humain pour effectuer les fonctionnalités dont nous avons besoin dans notre vie quotidienne.

La question que [Geoffrey Hinton](https://en.wikipedia.org/wiki/Geoffrey_Hinton) a posée lors de ses recherches séminales sur les réseaux de neurones était de savoir si nous pouvions construire des algorithmes informatiques qui se comportent de manière similaire aux neurones du cerveau. L'espoir était qu'en imitant la structure du cerveau, nous pourrions capturer une partie de ses capacités.

Pour ce faire, les chercheurs ont étudié la manière dont les neurones se comportaient dans le cerveau. Une observation importante était qu'un neurone seul est inutile. Au lieu de cela, vous avez besoin de _réseaux_ de neurones pour générer une fonctionnalité significative.

C'est parce que les neurones fonctionnent en recevant et en envoyant des signaux. Plus spécifiquement, les `dendrites` du neurone reçoivent des signaux et transmettent ces signaux à travers l'`axone`.

Les `dendrites` d'un neurone sont connectées à l'`axone` d'un autre neurone. Ces connexions sont appelées `synapses`, un concept qui a été généralisé au domaine du deep learning.

## **Qu'est-ce qu'un neurone en Deep Learning ?**

Les neurones dans les modèles de deep learning sont des nœuds à travers lesquels les données et les calculs circulent.

Les neurones fonctionnent comme suit :

* Ils reçoivent un ou plusieurs signaux d'entrée. Ces signaux d'entrée peuvent provenir soit de l'ensemble de données brutes, soit de neurones positionnés à une couche précédente du réseau de neurones.
* Ils effectuent certains calculs.
* Ils envoient certains signaux de sortie aux neurones plus profonds dans le réseau de neurones via une `synapse`.

Voici un diagramme de la fonctionnalité d'un neurone dans un réseau de neurones de deep learning :

![La fonction d'un neurone dans un modèle de deep learning](https://nickmccullum.com/images/python-deep-learning/understanding-neurons-deep-learning/neuron-functionality.png)

Parcourons ce diagramme étape par étape.

Comme vous pouvez le voir, les neurones dans un modèle de deep learning sont capables d'avoir des synapses qui se connectent à plus d'un neurone dans la couche précédente. Chaque synapse a un `poids` associé, qui impacte l'importance du neurone précédent dans le réseau de neurones global.

Les poids sont un sujet très important dans le domaine du deep learning car l'ajustement des poids d'un modèle est le moyen principal par lequel les modèles de deep learning sont entraînés. Vous verrez cela en pratique plus tard lorsque nous construirons nos premiers réseaux de neurones à partir de zéro.

Une fois qu'un neurone reçoit ses entrées des neurones de la couche précédente du modèle, il additionne chaque signal multiplié par son poids correspondant et les transmet à une fonction d'activation, comme ceci :

![La fonction d'activation d'un neurone](https://nickmccullum.com/images/python-deep-learning/understanding-neurons-deep-learning/activation-function.png)

La fonction d'activation calcule la valeur de sortie pour le neurone. Cette valeur de sortie est ensuite transmise à la couche suivante du réseau de neurones via une autre synapse.

Cela sert de vue d'ensemble des neurones de deep learning. Ne vous inquiétez pas si c'était beaucoup à assimiler - nous en apprendrons beaucoup plus sur les neurones dans le reste de ce tutoriel. Pour l'instant, il suffit que vous ayez une compréhension de haut niveau de leur structure dans un modèle de deep learning.

# **Fonctions d'activation en Deep Learning**

[Les fonctions d'activation](https://nickmccullum.com/python-deep-learning/deep-learning-activation-functions/) sont un concept central à comprendre en deep learning.

Elles permettent aux neurones d'un réseau de neurones de communiquer entre eux via leurs synapses.

Dans cette section, vous apprendrez à comprendre l'importance et la fonctionnalité des fonctions d'activation en deep learning.

## **Que sont les fonctions d'activation en Deep Learning ?**

Dans la section précédente, nous avons appris que les neurones reçoivent des signaux d'entrée de la couche précédente d'un réseau de neurones. Une somme pondérée de ces signaux est alimentée dans la fonction d'activation du neurone, puis la sortie de la fonction d'activation est transmise à la couche suivante du réseau.

Il existe quatre principaux types de fonctions d'activation que nous discuterons dans ce tutoriel :

* Fonctions de seuil
* Fonctions sigmoïdes
* Fonctions rectificatrices, ou ReLUs
* Fonctions tangente hyperbolique

Travaillons sur ces fonctions d'activation une par une.

## **Fonctions de seuil**

Les fonctions de seuil calculent un signal de sortie différent selon que leur entrée se situe au-dessus ou en dessous d'un certain seuil. Rappelez-vous, la valeur d'entrée d'une fonction d'activation est la somme pondérée des valeurs d'entrée de la couche précédente dans le réseau de neurones.

Mathématiquement parlant, voici la définition formelle d'une fonction de seuil de deep learning :

![Fonctions de seuil](https://nickmccullum.com/images/python-deep-learning/deep-learning-activation-functions/threshold-function.png)

Comme le suggère l'image ci-dessus, la fonction de seuil est parfois également appelée fonction `unit step`.

Les fonctions de seuil sont similaires aux variables booléennes en programmation informatique. Leur valeur calculée est soit `1` (similaire à `True`) soit `0` (équivalent à `False`).

## **La fonction sigmoïde**

La fonction sigmoïde est bien connue dans la communauté des data scientists en raison de son utilisation dans la [régression logistique](https://nickmccullum.com/python-machine-learning/logistic-regression-python/), l'une des techniques principales d'apprentissage automatique utilisées pour résoudre les [problèmes de classification](https://nickmccullum.com/python-machine-learning/classification-performance-measurement/).

La fonction sigmoïde peut accepter n'importe quelle valeur, mais calcule toujours une valeur entre `0` et `1`.

Voici la définition mathématique de la fonction sigmoïde :

![Fonctions sigmoïdes](https://nickmccullum.com/images/python-deep-learning/deep-learning-activation-functions/sigmoid-function.png)

Un avantage de la fonction sigmoïde par rapport à la fonction de seuil est que sa courbe est lisse. Cela signifie qu'il est possible de calculer des dérivées en tout point de la courbe.

## **La fonction rectificatrice**

La fonction rectificatrice n'a pas la même propriété de lissité que la fonction sigmoïde de la section précédente. Cependant, elle est encore très populaire dans le domaine du deep learning.

La fonction rectificatrice est définie comme suit :

* Si la valeur d'entrée est inférieure à `0`, alors la fonction renvoie `0`
* Sinon, la fonction renvoie sa valeur d'entrée

Voici ce concept expliqué mathématiquement :

![Fonctions rectificatrices](https://nickmccullum.com/images/python-deep-learning/deep-learning-activation-functions/rectifier-function.png)

Les fonctions rectificatrices sont souvent appelées fonctions d'activation `Rectified Linear Unit`, ou `ReLUs` en abrégé.

## **La fonction tangente hyperbolique**

La fonction tangente hyperbolique est la seule fonction d'activation incluse dans ce tutoriel qui est basée sur une identité trigonométrique.

Sa définition mathématique est ci-dessous :

![Fonction tangente hyperbolique](https://nickmccullum.com/images/python-deep-learning/deep-learning-activation-functions/hyperbolic-tangent-function.png)

La fonction tangente hyperbolique est similaire en apparence à la fonction sigmoïde, mais ses valeurs de sortie sont toutes décalées vers le bas.

# **Comment fonctionnent vraiment les réseaux de neurones ?**

Jusqu'à présent dans ce tutoriel, nous avons discuté de deux des éléments de base pour construire des réseaux de neurones :

* Neurones
* Fonctions d'activation

Cependant, vous êtes probablement encore un peu confus quant à [comment fonctionnent vraiment les réseaux de neurones](https://nickmccullum.com/python-deep-learning/how-do-neural-networks-really-work/).

Ce tutoriel rassemblera les pièces que nous avons déjà discutées afin que vous puissiez comprendre comment les réseaux de neurones fonctionnent en pratique.

## **L'exemple que nous utiliserons dans ce tutoriel**

Ce tutoriel travaillera à travers un exemple concret étape par étape afin que vous puissiez comprendre comment les réseaux de neurones font des prédictions.

Plus spécifiquement, nous traiterons des évaluations de propriétés.

Vous savez probablement déjà qu'il y a un _ton_ de facteurs qui influencent les prix des maisons, y compris l'économie, les taux d'intérêt, son nombre de chambres/salles de bain, et son emplacement.

La haute dimensionnalité de cet ensemble de données en fait un candidat intéressant pour construire et entraîner un réseau de neurones.

Un avertissement concernant cette section est que le réseau de neurones que nous utiliserons pour faire des prédictions _a déjà été entraîné_. Nous explorerons le processus d'entraînement d'un nouveau réseau de neurones dans la section suivante de ce tutoriel.

## **Les paramètres de notre ensemble de données**

Commençons par discuter des paramètres de notre ensemble de données. Plus spécifiquement, imaginons que l'ensemble de données contient les paramètres suivants :

* Superficie en pieds carrés
* Chambres
* Distance du centre-ville
* Âge de la maison

Ces quatre paramètres formeront la couche d'entrée du réseau de neurones artificiels. Notez qu'en réalité, il y a probablement _beaucoup plus de paramètres_ que vous pourriez utiliser pour entraîner un réseau de neurones à prédire les prix des logements. Nous avons limité ce nombre à quatre pour garder l'exemple raisonnablement simple.

## **La forme la plus basique d'un réseau de neurones**

Dans sa forme la plus basique, un réseau de neurones n'a que deux couches - la couche d'entrée et la couche de sortie. La couche de sortie est le composant du réseau de neurones qui fait réellement des prédictions.

Par exemple, si vous vouliez faire des prédictions en utilisant un modèle de somme pondérée simple (également appelé modèle de régression linéaire), votre réseau de neurones prendrait la forme suivante :

![Un réseau de neurones basique](https://nickmccullum.com/images/python-deep-learning/how-do-neural-networks-really-work/basic-neural-network.png)

Bien que ce diagramme soit un peu abstrait, le point est que la plupart des réseaux de neurones peuvent être visualisés de cette manière :

* Une couche d'entrée
* Possiblement quelques couches cachées
* Une couche de sortie

C'est la couche cachée de neurones qui rend les réseaux de neurones si puissants pour calculer des prédictions.

Pour chaque neurone dans une couche cachée, il effectue des calculs en utilisant certains (ou tous) des neurones de la dernière couche du réseau de neurones. Ces valeurs sont ensuite utilisées dans la couche suivante du réseau de neurones.

## **Le but des neurones dans la couche cachée d'un réseau de neurones**

Vous vous demandez probablement - que signifie exactement chaque neurone dans la couche cachée ? Dit différemment, comment les praticiens de l'apprentissage automatique doivent-ils interpréter ces valeurs ?

En général, les neurones dans les couches intermédiaires d'un réseau de neurones sont activés (ce qui signifie que leur fonction d'activation retourne `1`) pour une valeur d'entrée qui satisfait certaines sous-propriétés.

Pour notre modèle de prédiction des prix des logements, un exemple pourrait être les maisons de 5 chambres avec de petites distances du centre-ville.

Dans la plupart des autres cas, décrire les caractéristiques qui causeraient l'activation d'un neurone dans une couche cachée n'est pas si facile.

## **Comment les neurones déterminent leurs valeurs d'entrée**

Plus tôt dans ce tutoriel, j'ai écrit « Pour chaque neurone dans une couche cachée, il effectue des calculs en utilisant certains (ou tous) des neurones de la dernière couche du réseau de neurones. »

Cela illustre un point important - chaque neurone dans un réseau de neurones n'a pas besoin d'utiliser tous les neurones de la couche précédente.

Le processus par lequel les neurones déterminent quelles valeurs d'entrée utiliser de la couche précédente du réseau de neurones est appelé _entraînement_ du modèle. Nous en apprendrons davantage sur l'entraînement des réseaux de neurones dans la section suivante de ce cours.

## **Visualisation du processus de prédiction d'un réseau de neurones**

Lors de la visualisation d'un réseau de neurones, nous dessinons généralement des lignes de la couche précédente à la couche actuelle chaque fois que le neurone précédent a un poids supérieur à `0` dans la formule de somme pondérée pour le neurone actuel.

L'image suivante aidera à visualiser cela :

![Un réseau de neurones complet](https://nickmccullum.com/images/python-deep-learning/how-do-neural-networks-really-work/completed-neural-network.png)

Comme vous pouvez le voir, toutes les paires de neurones n'ont pas de synapse. `x4` n'alimente que trois des cinq neurones de la couche cachée, par exemple. Cela illustre un point important lors de la construction de réseaux de neurones - tous les neurones d'une couche précédente ne doivent pas être utilisés dans la couche suivante d'un réseau de neurones.

# **Comment les réseaux de neurones sont entraînés**

Jusqu'à présent, vous avez appris ce qui suit sur les réseaux de neurones :

* Qu'ils sont composés de neurones
* Que chaque neurone utilise une fonction d'activation appliquée à la somme pondérée des sorties de la couche précédente du réseau de neurones
* Une vue d'ensemble sans code de la manière dont les réseaux de neurones font des prédictions

Nous n'avons pas encore couvert une partie très importante du processus d'ingénierie des réseaux de neurones : comment les réseaux de neurones sont entraînés.

Maintenant, vous apprendrez comment les réseaux de neurones sont entraînés. Nous discuterons des ensembles de données, des algorithmes et des principes généraux utilisés dans l'entraînement des réseaux de neurones modernes qui résolvent des problèmes réels.

## **Codage en dur vs. Codage souple**

Il existe deux principales façons de développer des applications informatiques. Avant de se plonger dans la manière dont les réseaux de neurones sont entraînés, il est important de s'assurer que vous comprenez la différence entre le `codage en dur` et le `codage souple` des programmes informatiques.

Le codage en dur signifie que vous spécifiez explicitement les variables d'entrée et vos variables de sortie souhaitées. Dit différemment, le codage en dur ne laisse aucune place à l'ordinateur pour interpréter le problème que vous essayez de résoudre.

Le codage souple est tout le contraire. Il laisse de la place au programme pour comprendre ce qui se passe dans l'ensemble de données. Le codage souple permet à l'ordinateur de développer ses propres approches de résolution de problèmes.

Un exemple spécifique est utile ici. Voici deux instances de la manière dont vous pourriez identifier des chats dans un ensemble de données en utilisant des techniques de codage souple et de codage en dur.

* **Codage en dur :** vous utilisez des paramètres spécifiques pour prédire si un animal est un chat. Plus spécifiquement, vous pourriez dire que si le poids et la longueur d'un animal se situent dans certaines
* **Codage souple :** vous fournissez un ensemble de données contenant des animaux étiquetés avec leur type d'espèce et des caractéristiques de ces animaux. Ensuite, vous construisez un programme informatique pour prédire si un animal est un chat ou non en fonction des caractéristiques de l'ensemble de données.

Comme vous pouvez l'imaginer, l'entraînement des réseaux de neurones relève de la catégorie du codage souple. Gardez cela à l'esprit lorsque vous progressez dans ce cours.

## **Entraînement d'un réseau de neurones à l'aide d'une fonction de coût**

Les réseaux de neurones sont entraînés à l'aide d'une `fonction de coût`, qui est une équation utilisée pour mesurer l'erreur contenue dans la prédiction d'un réseau.

La formule d'une fonction de coût de deep learning (dont il en existe beaucoup - ceci est juste _un_ exemple) est ci-dessous :

![Équation de la fonction de coût](https://nickmccullum.com/images/python-deep-learning/how-neural-networks-are-trained/cost-function-equation.png)

_Note : cette fonction de coût est appelée `mean squared error`, c'est pourquoi il y a un MSE du côté gauche du signe égal._

Bien qu'il y ait beaucoup de mathématiques dans cette équation, elle peut être résumée comme suit :

`Prenez la différence entre la valeur de sortie prédite d'une observation et la valeur de sortie réelle de cette observation. Élevez cette différence au carré et divisez-la par 2.`

Pour réitérer, notez que ceci est simplement _un_ exemple de fonction de coût qui pourrait être utilisée en apprentissage automatique (bien qu'elle soit admise comme le choix le plus populaire). Le choix de la fonction de coût à utiliser est un sujet complexe et intéressant en soi, et hors du cadre de ce tutoriel.

Comme mentionné, le but d'un réseau de neurones artificiels est de minimiser la valeur de la fonction de coût. La fonction de coût est minimisée lorsque la valeur prédite par votre algorithme est aussi proche que possible de la valeur réelle. Dit différemment, le but d'un réseau de neurones est de minimiser l'erreur qu'il fait dans ses prédictions !

## **Modification d'un réseau de neurones**

Après la création d'un réseau de neurones initial et l'imputation de sa fonction de coût, des modifications sont apportées au réseau de neurones pour voir si elles réduisent la valeur de la fonction de coût.

Plus spécifiquement, le composant réel du réseau de neurones qui est modifié est le poids de chaque neurone à sa synapse qui communique avec la couche suivante du réseau.

Le mécanisme par lequel les poids sont modifiés pour déplacer le réseau de neurones vers des poids avec moins d'erreur est appelé `descente de gradient`. Pour l'instant, il suffit que vous compreniez que le processus d'entraînement des réseaux de neurones ressemble à ceci :

* Des poids initiaux pour les valeurs d'entrée de chaque neurone sont assignés
* Des prédictions sont calculées en utilisant ces valeurs initiales
* Les prédictions sont alimentées dans une fonction de coût pour mesurer l'erreur du réseau de neurones
* Un algorithme de descente de gradient modifie les poids pour les valeurs d'entrée de chaque neurone
* Ce processus est continué jusqu'à ce que les poids cessent de changer (ou jusqu'à ce que la quantité de leur changement à chaque itération tombe en dessous d'un seuil spécifié)

Cela peut sembler très abstrait - et c'est OK ! Ces concepts sont généralement compris uniquement lorsque vous commencez à [entraîner vos premiers modèles d'apprentissage automatique](https://gumroad.com/l/pGjwd).

## **Pensées finales**

Dans ce tutoriel, vous avez appris comment les réseaux de neurones effectuent des calculs pour faire des prédictions utiles.

Si vous êtes intéressé à en apprendre davantage sur la construction, l'entraînement et le déploiement de modèles d'apprentissage automatique de pointe, mon eBook [Pragmatic Machine Learning](https://gumroad.com/l/pGjwd) vous apprendra à construire 9 modèles d'apprentissage automatique différents en utilisant des projets réels. 

Vous pouvez déployer le code de l'eBook sur votre GitHub ou portfolio personnel pour le montrer à des employeurs potentiels. Le livre sera lancé le 3 août - [précommandez-le maintenant avec 50% de réduction](https://gumroad.com/l/pGjwd) !