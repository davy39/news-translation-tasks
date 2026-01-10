---
title: Machine Learning Pour les Managers – Ce Que Vous Devez Savoir
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2020-08-12T18:26:04.000Z'
originalURL: https://freecodecamp.org/news/machine-learning-for-managers-what-you-need-to-know
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/ml.jpg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: Product Management
  slug: product-management
seo_title: Machine Learning Pour les Managers – Ce Que Vous Devez Savoir
seo_desc: 'If you are managing a tech team as a product or project manager, here is
  what you need to know about machine learning.

  Machine learning and deep learning have been popular buzz words for the last five
  years. The demand for .ai domains has skyrocketed...'
---

Si vous gérez une équipe technique en tant que responsable produit ou chef de projet, voici ce que vous devez savoir sur le machine learning.

Le machine learning et le deep learning sont des termes à la mode depuis les cinq dernières années. La demande pour les domaines .ai a explosé. 

Mais au-delà de tout le battage médiatique entourant le machine learning, il est difficile de saisir les concepts de base avec facilité si vous êtes un débutant absolu.

Étant donné la nature omniprésente du ML et de l'IA, presque tous les produits peuvent maintenant avoir un cas d'utilisation de machine learning. Dans cet article, nous allons donc examiner en profondeur le machine learning et vous équiper des connaissances nécessaires pour votre prochaine conversation technique.

## Qu'est-ce que le Machine Learning ?

Le machine learning est une branche de l'Intelligence Artificielle. L'Intelligence Artificielle dans son ensemble comprend de nombreux concepts généraux visant à simuler la pensée humaine. 

Le machine learning se concentre uniquement sur un aspect clé : faire apprendre aux machines.

> Le machine learning est la science qui permet aux ordinateurs de prendre des décisions sans être explicitement programmés.

Au cours de la dernière décennie, le machine learning nous a donné des voitures autonomes, la reconnaissance faciale, les chatbots et de nombreuses autres applications utiles. Le machine learning alimente tant d'outils que nous utilisons au quotidien.

## Comment Fonctionne le Machine Learning ?

Le machine learning utilise des algorithmes pour analyser d'énormes quantités de données et en tirer des conclusions. Lorsque vous combinez de grands ensembles de données avec une puissance de calcul élevée, ces algorithmes peuvent comprendre des motifs et des relations entre les données.

Par exemple, examinons un ensemble de données simple :

x = 1,2,3,4,5

y = 1,4,9,16,25

Si vous regardez les nombres ci-dessus, vous verrez que la relation entre x et y est que y est le carré de x (c'est-à-dire, y = x²).

En machine learning, le travail d'un algorithme est de trouver cette fonction qui définit la relation entre l'entrée et la sortie. Une fois cette fonction établie, il est facile de prédire les valeurs futures.

Par exemple, si x est 10, y est 100.

Bien que cet exemple soit trop simple, il devrait vous donner une idée de la façon dont les modèles de machine learning fonctionnent.

Considérons un ensemble de données complexe comme la prédiction des prix de l'immobilier.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/1.png)

Cet ensemble de données contiendra des codes postaux, des superficies en pieds carrés et de nombreuses autres entrées avec le prix comme sortie. Si vous avez un ensemble de données avec des milliers de ces caractéristiques d'entrée et le prix final, vous pouvez entraîner un modèle pour prédire le prix moyen en fonction de nouvelles entrées.

Les problèmes de machine learning impliquent généralement la recherche de la relation entre les entrées et les sorties pour trouver la « fonction d'hypothèse ». Dans notre exemple précédent, la fonction d'hypothèse était y = x².

Les fonctions d'hypothèse du monde réel sont beaucoup plus complexes que cela. Nous utilisons ensuite cette fonction pour trouver des réponses à des entrées personnalisées.

En résumé, le machine learning, dans la plupart des cas, est une statistique avancée combinée à une capacité de calcul. Aujourd'hui, le machine learning alimente des technologies comme la reconnaissance faciale, [l'analyse de sentiment](https://medium.com/manishmshiva/a-complete-guide-to-sentiment-analysis-and-its-applications-72adb3b057f5), et bien d'autres.

## Types d'Algorithmes d'Apprentissage

Examinons les types de problèmes que vous rencontrerez lorsque vous travaillerez avec le machine learning. Tout d'abord, il existe trois façons de faire apprendre aux machines.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/ml-1.png)

### Apprentissage Supervisé

Dans l'apprentissage supervisé, vous fournissez des entrées claires à un algorithme de machine learning. L'algorithme sait quoi apprendre à partir des données et les conclusions attendues de celles-ci.

Par exemple, pour reconnaître la différence entre un chat et un chien, vous entraînez un algorithme avec des milliers d'images. Chacune de ces images sera étiquetée en conséquence.

Une fois que vous exécutez ces données à travers l'algorithme, celui-ci apprend et comprend les différences. Ainsi, il peut prédire, avec une précision raisonnable, si une nouvelle image est un chat ou un chien.

### Apprentissage Non Supervisé

L'étiquetage des données est important pour construire un modèle supervisé. Cependant, les entreprises collectent de grands ensembles de données au quotidien. Étiqueter ces ensembles de données pour faciliter le travail d'un modèle de machine learning n'est pas une approche élégante pour aborder ce problème.

C'est là que l'apprentissage non supervisé intervient. Vous pouvez utiliser des algorithmes d'apprentissage non supervisé pour regrouper les données en fonction des attributs disponibles. Ces données peuvent ensuite être alimentées dans des modèles d'apprentissage supervisé pour obtenir une précision de prédiction plus élevée.

Les modèles d'apprentissage non supervisé sont plus difficiles que les modèles d'apprentissage supervisé. [Vous pouvez trouver plus d'informations et d'exemples ici](https://www.mathworks.com/discovery/unsupervised-learning.html), et vous pouvez [en apprendre davantage sur les algorithmes importants de machine learning ici](https://www.freecodecamp.org/news/a-no-code-intro-to-the-9-most-important-machine-learning-algorithms-today/).

### Apprentissage par Renforcement

Aucun algorithme de machine learning n'est précis à 100 %. Le niveau de précision dépend de l'ensemble de données avec lequel vous entraînez l'algorithme.

Cela signifie qu'après avoir entraîné un algorithme, de nouveaux ensembles de données peuvent être disponibles. Ces ensembles de données pourraient avoir le potentiel d'améliorer considérablement la précision de votre modèle.

Vous pouvez utiliser l'apprentissage par renforcement pour ces types de scénarios. L'apprentissage par renforcement est le concept de mise à jour de l'algorithme pendant qu'il est en production. Les modèles d'apprentissage par renforcement peuvent se réentraîner en fonction de nouvelles entrées.

Par exemple, une voiture autonome peut apprendre un nouveau type de terrain après l'avoir traversé. Cela sera pris en compte par l'algorithme de la voiture autonome la prochaine fois qu'elle devra choisir un itinéraire.

## Types de Problèmes de Machine Learning

Les problèmes de Machine Learning peuvent être classés en quatre sous-catégories en fonction du type de résultat que vous recherchez.

### Classification

Les modèles de classification produisent un résultat qui appartient à un ensemble fini. Des exemples de modèles de classification incluent spam/non spam, 0 ou 1 (classification binaire), positif/négatif/neutre, et ainsi de suite.

### Régression

Les modèles de régression produisent des résultats qui appartiennent à une plage. Des exemples incluent la prédiction des prix du marché boursier, la prévision météorologique, et plus encore. Ceux-ci ne sont pas limités à un ensemble fini de valeurs et sont donc appelés problèmes de régression.

### Clustering

Le clustering est un concept clé dans l'apprentissage non supervisé. Le clustering vous aide à regrouper les données qui ont des attributs similaires. Une fois ces groupes établis, il devient plus facile de les entraîner en utilisant des modèles supervisés. 

[En savoir plus sur le clustering ici](https://www.freecodecamp.org/news/how-to-build-and-train-k-nearest-neighbors-ml-models-in-python/).

### Réduction de Dimensionalité

La réduction de dimensionalité est une autre technique d'apprentissage non supervisé. En utilisant la réduction de dimensionalité, vous pouvez réduire un ensemble de données complexe avec des milliers de caractéristiques en un ensemble simple avec peut-être une centaine d'entrées.

Similaire au clustering, la réduction de dimensionalité est souvent utilisée pour réduire le bruit des grands ensembles de données avant de les alimenter dans des modèles d'entraînement supervisés. 

[Vous pouvez trouver un article plus approfondi sur la réduction de dimensionalité ici](https://machinelearningmastery.com/dimensionality-reduction-for-machine-learning/).

## Qu'est-ce que le Deep Learning ?

![Image](https://www.freecodecamp.org/news/content/images/2020/08/1-1.png)

Le deep learning est le Machine Learning dopé.

Il existe de nombreux algorithmes en machine learning. Celui qui se distingue est le Réseau de Neurones.

La différence entre les autres algorithmes de machine learning et un réseau de neurones est que vous pouvez empiler des réseaux de neurones ensemble – autant que vous le souhaitez.

Cela nous aide à résoudre des problèmes complexes comme la reconnaissance faciale et les voitures autonomes, car ces types de problèmes viennent avec des milliers d'entrées en temps réel. 

En utilisant des réseaux de neurones, vous pouvez résoudre presque n'importe quel problème complexe avec une grande précision, si vous avez les données et la puissance de calcul nécessaires pour que le modèle fonctionne.

Les réseaux de neurones existent depuis des décennies, mais c'est la disponibilité de grands ensembles de données et de puissance de calcul qui les a ramenés à la vie. Aujourd'hui, le deep learning est l'un des domaines les plus passionnants de l'industrie.

## Pourquoi Avez-Vous Besoin du Machine Learning ?

Examinons quelques solutions populaires de machine learning que nous utilisons chaque jour.

### Assistants Vocaux

![Image](https://www.freecodecamp.org/news/content/images/2020/08/siri.png)

Vous êtes-vous déjà demandé comment Siri peut comprendre et interpréter vos commandes vocales ? La réponse est le machine learning. Vous pouvez trouver un assistant vocal dans presque tous les smartphones maintenant, grâce aux avancées en [Traitement du Langage Naturel](https://www.freecodecamp.org/news/learn-natural-language-processing-no-experience-required/).

Bien qu'il soit difficile pour les ordinateurs de comprendre le langage naturel, grâce au machine learning, nous avons Alexa, Cortana et Siri.

### Recommandations de Produits

![Image](https://www.freecodecamp.org/news/content/images/2020/08/product.jpg)

Les moteurs de recommandation sont un cas d'utilisation rentable pour les entreprises de commerce électronique. Si vous pouvez trouver les bons produits à recommander, il y a des chances que votre client effectue plusieurs achats.

Les algorithmes de machine learning peuvent comprendre le comportement des utilisateurs à partir des achats passés. Cela les aide à recommander des produits similaires lorsqu'un client fait ses achats sur votre site web.

Les recommandations ne sont pas limitées au commerce électronique. Cela s'applique aux produits comme Spotify ou Netflix qui recommandent la musique ou les films que vous aimez.

### Chatbots

![Image](https://www.freecodecamp.org/news/content/images/2020/08/chatbot.png)

Le support client peut faire ou défaire votre entreprise, surtout si vous êtes une startup. Plus vous attirez d'utilisateurs, plus vous devez fournir de support client.

Les chatbots sont un énorme gain de temps lorsqu'il s'agit d'interagir avec les clients. Puisque la majorité de vos clients auront des questions communes, vous pouvez concevoir un chatbot capable de répondre aux questions redondantes.

Vous n'avez pas à embaucher des professionnels supplémentaires du service client ou à faire attendre vos clients dans une file d'attente. Les chatbots font gagner du temps et de l'argent aux entreprises, grâce au Machine Learning.

### Filtrage de Spam

![Image](https://www.freecodecamp.org/news/content/images/2020/08/spam.png)

Le filtrage de spam est une application simple mais puissante du Machine Learning. C'est la raison pour laquelle Gmail ou Outlook peuvent filtrer les emails de spam pour vous avec une grande précision.

Les systèmes de filtrage de spam sont également conçus pour apprendre de l'expérience. Ce modèle, également appelé apprentissage par renforcement, peut mieux comprendre vos préférences lorsque vous marquez un email comme spam.

Nous avons maintenant des boîtes de réception plus propres, grâce au Machine Learning.

### Traduction de Langue

![Image](https://www.freecodecamp.org/news/content/images/2020/08/language-1.jpeg)

Que ferions-nous sans Google Translate ? Les moteurs de traduction de langue basés sur le machine learning économisent des millions aux entreprises chaque année.

Avant le machine learning, les services de traduction étaient entièrement alimentés par des humains. Grâce au machine learning, vous pouvez traduire de grands ensembles de données dans n'importe quelle langue en quelques minutes.

## Outils et Frameworks

Le machine learning et le deep learning sont réalisés en utilisant différentes bibliothèques et frameworks. Bien que d'autres langages aient leurs propres outils, Python est généralement le langage préféré pour le machine learning.

Voici quelques frameworks Python que vous pouvez utiliser pour construire votre prochain produit de machine learning ou de deep learning.

* [Scikit-learn](https://scikit-learn.org/) – Populaire pour les problèmes de machine learning. Grande communauté de support. Non adapté aux modèles complexes de deep learning.
* [Tensorflow](https://www.tensorflow.org/) – Framework de deep learning le plus populaire. Développé par Google. Supporte tous les modèles complexes de deep learning comme les CNNs et les RNNs
* [PyTorch](https://pytorch.org/) – Développé par Facebook, scalable et offre des performances élevées.

[J'ai récemment écrit un article de blog sur les frameworks populaires de deep learning si vous êtes intéressé](https://medium.com/manishmshiva/a-detailed-comparison-of-the-popular-deep-learning-frameworks-a0f65fddf276).

## Conclusion

Le machine learning a le potentiel de transformer chaque industrie. Des assistants vocaux aux voitures autonomes, les applications du machine learning sont partout autour de nous aujourd'hui. Il peut vous aider à mieux comprendre vos clients et à prendre des décisions plus intelligentes avec les données.

J'espère que cet article vous a aidé à bien comprendre les concepts de machine learning et de deep learning. Si vous êtes fasciné par le machine learning autant que moi, consultez le [cours de Machine Learning sur Coursera](https://www.coursera.org/learn/machine-learning) du Prof. Andrew Ng.

_Je écris régulièrement sur le Machine Learning, la Cybersécurité et DevOps. Vous pouvez vous inscrire à ma [newsletter hebdomadaire](https://www.manishmshiva.com/) ici._