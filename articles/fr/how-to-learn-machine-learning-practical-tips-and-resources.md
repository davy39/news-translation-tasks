---
title: Comment apprendre le Machine Learning – Conseils et ressources pour apprendre
  le ML de manière pratique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-07T17:28:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-learn-machine-learning-practical-tips-and-resources
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/Article-Visual-Template.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
seo_title: Comment apprendre le Machine Learning – Conseils et ressources pour apprendre
  le ML de manière pratique
seo_desc: "By Yacine Mahdid\nA lot of people want to learn machine learning these\
  \ days. But the daunting bottom-up curriculum that most ML teachers propose is enough\
  \ discourage a lot of newcomers. \nIn this tutorial I flip the curriculum upside\
  \ down and will outl..."
---

Par Yacine Mahdid

Beaucoup de gens veulent apprendre le machine learning ces jours-ci. Mais le programme intimidant de bas en haut que la plupart des enseignants en ML proposent est suffisant pour décourager de nombreux nouveaux venus. 

Dans ce tutoriel, je retourne le programme à l'envers et vais décrire ce que je pense être le moyen le plus rapide et le plus facile d'acquérir une solide compréhension du ML.

### Table des matières

Le programme que je propose ici est un processus en plusieurs étapes en boucle qui se déroule comme suit :

* **[Étape 0 : Immergez-vous dans le domaine du Machine Learning](#heading-immersion-dans-le-domaine-du-machine-learning)**
* **[Étape 1 : Étudiez un projet qui ressemble à votre objectif final](#heading-etudiez-un-projet-qui-ressemble-a-votre-objectif-final)**
* **[Étape 2 : Apprenez le langage de programmation](#heading-apprenez-le-langage-de-programmation)**
* **[Étape 3 : Apprenez les bibliothèques de haut en bas](#heading-apprenez-les-bibliotheques-de-haut-en-bas)**
* **[Étape 4 : Réalisez un projet qui vous passionne en maximum un mois](#heading-realisez-un-projet-qui-vous-passionne-en-maximum-un-mois)**
* **[Étape 5 : Identifiez une lacune dans vos connaissances et apprenez à son sujet](#heading-identifiez-une-lacune-dans-vos-connaissances-et-apprenez-a-son-sujet)**
* **[Étape 6 : Répétez les étapes 0 à 5](#heading-repetez-les-etapes-0-a-5)** 

Ceci est un plan d'apprentissage en boucle car la sixième étape est en fait un GOTO à l'Étape 0 !

En guise de mise en garde, ce programme peut vous sembler étrange. Mais je l'ai testé en bataille lorsque j'enseignais le machine learning à des étudiants de premier cycle à l'Université McGill. 

J'ai essayé de nombreuses itérations de ce programme, en commençant par l'approche théorique supérieure de bas en haut. Mais en pratique, cette approche pragmatique de haut en bas est celle qui donne les meilleurs résultats. 

Une critique commune que je reçois est que les gens qui ne commencent pas par les bases, comme les statistiques ou l'algèbre linéaire, auront une mauvaise compréhension du machine learning et ne sauront pas ce qu'ils font lorsqu'ils modélisent. 

En théorie, oui, c'est vrai et c'est pourquoi j'ai commencé à enseigner le ML avec l'approche de bas en haut. En pratique, cela n'a jamais été le cas.

Ce qui s'est réellement passé, c'est que parce que les étudiants savaient comment faire la modélisation de haut niveau, ils étaient beaucoup plus enclins à se plonger dans les détails de bas niveau par eux-mêmes, car ils voyaient le bénéfice direct que cela apporterait à leurs compétences de haut niveau. 

Ce contexte qu'ils ont été capables de se donner n'aurait pas été là s'ils avaient commencé par le bas – et c'est là que je crois que la plupart des enseignants perdent leurs étudiants.

Tout cela étant dit, plongeons dans le plan d'apprentissage réel ! 🚀🚀🚀

## Étape 0 : Immergez-vous dans le domaine du Machine Learning

La toute première partie de l'apprentissage de quoi que ce soit est de prendre le temps de comprendre où les choses se terminent et où se situe votre intérêt. 

Cela aura deux principaux avantages :

* Connaître la taille du domaine vous permettra de savoir que vous ne manquez rien, ce qui augmentera votre concentration.
* Il sera plus facile de tracer un chemin dans votre modèle mental si vous savez à quoi ressemble le paysage dans lequel vous vous promenez.

![moutons broutant, avec les puissants himalayas en arrière-plan](https://images.unsplash.com/photo-1565618408142-2b7446ec7c5a?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDE2fHxzaGVlcHxlbnwwfHx8fDE2MjQxMjA0Njg&ixlib=rb-1.2.1&q=80&w=2000)
_Imaginez que vous êtes un mouton dans un pâturage. Il est important que vous sachiez où se trouvent les limites et où l'herbe a meilleur goût : Photo par [Unsplash](https://unsplash.com/@aranya00?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">ARANYA KAR</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Afin de vous immerger correctement dans le domaine et d'affiner votre plan d'apprentissage, vous devriez répondre à ces trois questions dans l'ordre :

* **Que peut-on faire avec le Machine Learning ?**
* **Que voulez-vous faire avec le Machine Learning ?**
* **Comment faire cette chose spécifique ?**

Ces questions vous permettront de vous concentrer sur quelque chose de très spécifique et de gérable à apprendre, tout en vous permettant de voir le tableau d'ensemble.

Examinons chacune de ces questions un peu plus en détail.

### Que peut-on faire avec le Machine Learning ? 

Cette question est très large et changera d'un mois à l'autre. La grande chose avec ce programme est que à chaque passage à travers les étapes, vous passerez du temps à apprendre ce qui est possible dans le domaine. 

Cela vous permettra d'affiner votre modèle mental du Machine Learning. Donc si vous n'avez pas une image 100% précise de ce qui est possible lors de votre premier passage, ce n'est pas grave. Une compréhension approximative est meilleure que rien.

![Image](https://images.unsplash.com/photo-1519904981063-b0cf448d479e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDR8fGhpZ2h8ZW58MHx8fHwxNjI0MTIxNzYy&ixlib=rb-1.2.1&q=80&w=2000)
_Pensez à cette question comme à l'ascension d'une montagne brumeuse et à la prise de notes du paysage en contrebas : Photo par [Unsplash](https://unsplash.com/@lux17?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Lucas Clara</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Voici un bref aperçu de ce que vous pouvez faire avec le machine learning, des aspects techniques aux applications pratiques.

#### Sujets techniques du Machine Learning

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-22.png)
_Tâche de classification utilisant SVM_

* **Apprentissage supervisé :** Ce type d'apprentissage implique de donner une entrée et une sortie étiquetée à un modèle pour l'entraîner. Une fois l'entraînement terminé, vous devriez techniquement être capable de lui donner une entrée et il générera la bonne sortie. 
* **Apprentissage non supervisé :** Cet apprentissage implique une entrée sans sortie. Vous demandez au modèle de donner un sens aux motifs dans les données.
* **Apprentissage par renforcement :** Cette configuration de ML implique un agent, un environnement, des actions que l'agent peut effectuer, et des récompenses. Cela ressemble un peu à la façon dont vous dresseriez un chien avec des friandises.
* **Apprentissage en ligne :** Ce type d'apprentissage peut être à la fois supervisé et non supervisé. La particularité est que le modèle peut être mis à jour "en ligne" au fur et à mesure que le flux de données arrive.
* **Apprentissage par transfert :** Ce type d'apprentissage consiste à utiliser un modèle déjà entraîné comme point de départ pour une tâche d'apprentissage différente. Cela accélère considérablement l'apprentissage de la deuxième tâche.
* **Apprentissage d'ensemble :** Cette technique de ML implique de mettre ensemble plusieurs prédicteurs entraînés (les uns après les autres ou en prenant un vote de la sortie) et d'utiliser cet ensemble de prédicteurs comme prédicteur final.

Il existe de nombreuses autres variantes du machine learning, mais celles-ci sont un bon point de départ.

#### Modèles courants de Machine Learning

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-23.png)
_[L'un des types de modèles les plus compliqués appelé Réseau de Neurones Profond](https://github.com/ashishpatel26/Tools-to-Design-or-Visualize-Architecture-of-Neural-Network)._

* **Régression linéaire :** C'est la bonne vieille formule `y = ax + b` qui fonctionne en fait assez bien pour beaucoup de problèmes. Cela devrait être le point de départ pour la plupart des analyses.
* **Régression logistique :** C'est un type de modèle qui modélise la probabilité d'une classe ou de plusieurs classes. Même si elle a régression dans le nom, c'est un modèle de classification.
* **Arbre de décision :** Le modèle d'arbre de décision crée un arbre de 'décisions' ou de formules, qui, lorsqu'elles sont suivies, mènent à la sortie souhaitée. Ces types de modèles sont importants car ils sont faciles à comprendre et à inspecter une fois entraînés.
* **Machine à vecteurs de support (SVM) :** Imaginez ce modèle comme construisant un plan qui sépare deux classes avec une largeur maximale entre elles. C'est un peu plus compliqué que cela, mais imaginez une ligne avec une épaisseur et vous êtes à moitié là.
* **Naive Bayes :** Ces types de classifieurs utilisent le théorème de Bayes qui suppose que toutes les caractéristiques sont indépendantes les unes des autres. Ce n'est rarement le cas, c'est pourquoi il est appelé naïf. Il fonctionne néanmoins surprenamment bien en pratique même lorsque cette hypothèse ne tient pas.
* **k-plus proches voisins :** Ce type de classifieur ne nécessite pas d'entraînement, il mémorise simplement tous les éléments du jeu de données. Il peut ensuite vous donner une sortie basée sur la distance de l'entrée avec les autres points du jeu de données.
* **K-Means :** Ce modèle non supervisé, donné un nombre de clusters, déterminera à quel cluster appartiennent les points. Il le fera en modifiant de manière répétée le centroïde de chaque cluster jusqu'à ce qu'il converge vers quelque chose de stable.
* **Forêt aléatoire :** C'est une technique d'ensemble qui utilise beaucoup de classifieurs d'arbres de décision très simples. La sortie du modèle est la classe sortie par le plus grand nombre d'arbres de décision.
* **Algorithmes de réduction de dimensionnalité :** Il existe une grande variété d'algorithmes de réduction de dimensionnalité, l'analyse en composantes principales en étant un. Le principe de tous ces algorithmes est qu'ils peuvent créer une cartographie à partir du jeu de données avec beaucoup de dimensions (caractéristiques) vers une représentation avec moins de dimensions. Lorsqu'il cartographie vers 2 ou 3 dimensions, il nous permet de visualiser un jeu de données à haute dimension en 2D ou 3D.
* **XGBoost :** Ce modèle est un modèle boosté par gradient régulé. En un mot, il a des apprenants faibles configurés en série au lieu de en parallèle (comme la forêt aléatoire). C'est un très bon modèle et il est généralement un performant de premier plan dans les compétitions de machine learning.
* **Réseau de neurones profond :** Ces types de modèles sont un domaine entier à part. Basiquement, ce sont des prédicteurs faibles mis à la fois en série et en parallèle. Ces modèles sont capables de construire une représentation hiérarchique des données qui donne de grands résultats. Ils sont notoirement capricieux (pour dire le moins) à entraîner en raison de leur haute capacité. Il existe de nombreuses architectures possibles pour ces modèles, comme les CNNs et les Transformers.

Il existe de nombreux modèles de machine learning. Mais heureusement, vous n'avez pas besoin de tous les connaître pour être compétent en machine learning. 

En fait, si vous connaissez la **Régression linéaire**, **SVM**, **XGBoost** et une forme de **Réseau de neurones profond**, vous êtes prêt pour la plupart des problèmes. Mais apprendre comment le modèle apprend vous donne plus de flexibilité mentale et vous permet de penser différemment aux problèmes.

#### Applications courantes du Machine Learning

C'est un domaine où les choses changeront radicalement d'un mois à l'autre. Basiquement, dans tout domaine où des données sont collectées, vous pouvez ajouter du ML au mélange. 

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-24.png)
_[Type d'application de ML appelé segmentation d'image](https://www.analyticsvidhya.com/blog/2019/04/introduction-image-segmentation-techniques-python/) (utile pour les voitures autonomes)._

Le point ici est que l'ampleur et la profondeur de l'application du ML sont en constante expansion. Donc ne vous inquiétez pas trop si vous pensez n'avoir qu'une compréhension superficielle de ce qui est possible.

* **Vision par ordinateur :** Le Machine Learning (et le Deep Learning plus particulièrement) sont actuellement à un point où ils sont assez bons pour tout ce qui concerne les images et la reconnaissance d'objets. Il existe également des types d'analyses génératives que vous pouvez faire où les réseaux de neurones sont capables de générer une image en utilisant des astuces architecturales spécifiques (GAN ou Neural Style Transfer, par exemple).
* **Traitement du langage naturel (NLP) :** Cela inclut de nombreux sous-sujets comme : répondre à des questions, traduction, classification de documents ou génération de texte.
* **Diagnostic médical :** Lorsque vous traitez des images médicales, il est assez courant d'utiliser des techniques de vision par ordinateur pour les analyser. Mais le diagnostic médical peut également inclure des lectures qui ne sont pas basées sur des images, comme la concentration d'une certaine hormone dans un échantillon de sang.
* **Bioinformatique :** C'est un domaine très large qui chevauche de nombreuses autres techniques. En général, la bioinformatique utilise des techniques de machine learning pour traiter les bio-données et leurs analyses. Ici, vous pouvez penser au repliement des protéines comme un type de tâche en bioinformatique qui repose fortement sur le machine learning.
* **Détection des valeurs aberrantes :** Reconnaître quand quelque chose fait partie d'une catégorie ou quand il est si éloigné de la majorité des données qu'il doit être une valeur aberrante est un exercice très important dans de nombreux domaines.
* **Prévision météorologique :** Tout ce qui a vraiment à voir avec une quantité massive de points de données sur une période sera un bon candidat pour l'application du machine learning. La prévision météorologique est un type de problème dans lequel il y a beaucoup de données disponibles tout au long du temps. 

Cette liste pourrait continuer pendant un moment. Le point ici est de faire une bonne carte de ce qui est possible afin que vous vous sentiez ancré dans la prochaine phase de votre parcours d'apprentissage.

### Que voulez-vous faire avec le Machine Learning ? 

Cette question est la plus importante. Vous ne pourrez pas faire tout ce qui est possible en Machine Learning (ou dans tout autre domaine). Vous devez être très sélectif quant à ce que vous pensez être une bonne utilisation de votre temps et ce qui ne l'est pas.

Une façon de faire ce choix est de classer vos intérêts par ordre décroissant. 

![Journée de travail](https://images.unsplash.com/photo-1517817748493-49ec54a32465?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDV8fG5vdGVzfGVufDB8fHx8MTYyNDEyNDA4OQ&ixlib=rb-1.2.1&q=80&w=2000)
_Prenez un bon vieux stylo et du papier et classez ces sujets d'apprentissage 📺 : Photo par [Unsplash](https://unsplash.com/@adolfofelix?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Adolfo Félix</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Ensuite, sélectionnez simplement votre intérêt le plus important et épinglez-le quelque part où vous pouvez le voir. C'est ce que vous allez apprendre et rien d'autre jusqu'à ce que vos classements changent. 

Et gardez à l'esprit que vous pouvez définitivement changer vos intérêts. Si vous êtes très intéressé par un sujet spécifique mais, après avoir appris davantage à son sujet, il n'est plus aussi intéressant, alors il est acceptable d'abandonner le sujet et d'en prendre un autre. C'est toute la raison pour laquelle vous faites cette première étape de planification.

Ici, s'il y a de nombreux sujets qui vous intéressent, je vous conseille fortement de vous engager à n'en choisir qu'un pour un cycle. Tous les sujets sont interconnectés d'une certaine manière. Approfondir un sujet vous permettra de voir ces connexions. Sauter superficiellement d'un sujet à l'autre ne le fera pas.

Si je devais apprendre quelque chose de nouveau maintenant dans ma 100ème passe à travers ce programme d'apprentissage, je me plongerais dans les **Graph Neural Networks** et leur application dans la **Gestion de la Chaîne d'Approvisionnement**.

### Comment faire cette chose spécifique ?

Maintenant que vous savez ce qui vous intéresse et où cela se situe par rapport au contexte général, passez du temps à comprendre comment les gens le font. 

![Image](https://images.unsplash.com/photo-1606857521015-7f9fcf423740?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDV8fG9mZmljZXxlbnwwfHx8fDE2MjQxMjQ1ODc&ixlib=rb-1.2.1&q=80&w=2000)
_Que utilisent-ils, quelle est leur configuration ? Photo par [Unsplash](https://unsplash.com/@israelandrxde?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Israel Andrade</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Passer du temps à comprendre ce sur quoi vous allez passer des semaines (ou plus) à étudier est très important. Être capable de gagner du contexte pour ancrer ce que vous allez apprendre et savoir ce que vous n'avez pas besoin de savoir vous fera gagner beaucoup de temps et d'énergie.

Cela vous aidera également à comprendre ce sur quoi vous n'avez pas vraiment besoin de concentrer votre énergie. Par exemple, si vous trouvez que la plupart des gens n'utilisent pas HTML, CSS et JavaScript dans leur travail quotidien en ML, ne vous concentrez pas sur ces technologies.

En termes de ce que les gens utilisent en ML, il existe une large gamme de langages de programmation et d'outils en fonction de l'application. Vous avez des outils en C++, Java, Lua, Swift, JavaScript, Python, R, Julia, MATLAB, Rust... et la liste est longue.

Mais la densité des praticiens est assez concentrée autour de Python et de son écosystème de packages. Python est un langage de programmation relativement facile à comprendre avec un écosystème florissant. Cela signifie que les personnes qui veulent construire des outils de machine learning sont plus susceptibles de développer ces outils avec une interface Python. 

Les outils réels ne sont généralement pas développés en Python pur, cependant, car le langage est assez lent. Mais puisque ils ont une interface directe avec Python, l'utilisateur ne saura pas que c'est en fait une bibliothèque C++ enveloppée dans Python. 

Si vous n'avez pas compris cette dernière partie, ce n'est pas grave. Gardez simplement à l'esprit que Python + les bibliothèques en Python sont un pari très sûr à apprendre.

#### Outils à utiliser pour le Machine Learning

Les outils habituels à apprendre pour le ML sont les suivants :

* [**Python**](https://www.python.org/) pour la programmation de haut niveau
* [**Pandas**](https://pandas.pydata.org/) pour la manipulation de jeux de données
* [**Numpy**](https://numpy.org/) pour le calcul numérique sur CPU
* [**Scikit-learn**](https://scikit-learn.org/stable/) pour les modèles de machine learning non basés sur le deep learning
* [**Tensorflow**](https://www.tensorflow.org/) ou [**Pytorch**](https://pytorch.org/) pour les modèles de machine learning basés sur le Deep Learning
* Bibliothèques de haut niveau pour le Deep Learning comme [**Keras**](https://keras.io/) et [**fast.ai**](https://www.fast.ai/)
* Bases de [**Git**](https://git-scm.com/) pour travailler sur votre projet
* [**Jupyter Notebook**](https://jupyter.org/) ou [**Google Colab**](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjxoMiDw7jxAhWVK80KHUXiCTYQFjAAegQIBxAD&url=https%3A%2F%2Fresearch.google.com%2Fcolaboratory%2F&usg=AOvVaw38J01zt_Dlb6pQ1fe6FGrI) pour l'expérimentation de code

Il existe de nombreux autres outils que vous pouvez utiliser, [comme beaucoup plus](https://github.com/josephmisiti/awesome-machine-learning#python)! Soyez conscient de leur existence, mais ne stressez pas trop si vous n'êtes pas au courant de la toute dernière bibliothèque. Les technologies mentionnées ci-dessus sont suffisamment bonnes pour la plupart des projets. 

Mais il existe certaines bibliothèques que vous devrez peut-être ajouter à votre pile car elles sont spécialisées pour votre domaine d'étude.

Dans mon cas, pour étudier les **Graph Neural Networks** et leur application dans la **Gestion de la Chaîne d'Approvisionnement**, il semble que tous ces packages soient corrects. Cependant, il existe des packages plus spécialisés dans Pytorch comme la bibliothèque [Pytorch geometric](https://github.com/rusty1s/pytorch_geometric) qui accéléreraient mon développement de Graph Neural Networks. 

Ainsi, ma pile ressemblerait à ceci : 

**Python + Pandas + Pytorch + Pytorch geometric + Git + Colab** 

Je sais que cette pile est bonne pour mon cas d'utilisation puisque j'ai étudié comment les gens développaient dans ce sous-domaine spécifique et c'est ce qu'ils utilisent.

## Étape 1 : Étudiez un projet qui ressemble à votre objectif final

Maintenant que vous savez exactement ce que vous voulez faire et que vous avez une idée approximative de la manière dont vous allez faire cette chose spécifique, il est temps d'être plus précis.

La meilleure façon d'apprendre en profondeur comment faire quelque chose est de regarder un expert réel travailler. Vous pouvez voir cela comme un apprentissage asynchrone.

![Ingénieurs de diffusion travaillant en studio](https://images.unsplash.com/photo-1581092922699-2766a7278454?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDd8fGFwcHJlbnRpY2V8ZW58MHx8fHwxNjI1NTAwMzcy&ixlib=rb-1.2.1&q=80&w=2000)
_Vous et votre mentor découvrant à quoi servent toutes les lumières clignotantes : Photo par [Unsplash](https://unsplash.com/@thisisengineering?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">ThisisEngineering RAEng</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Pouvoir voir le résultat final de l'endroit où vous voulez être en action vous donnera plus de contexte pour ancrer votre apprentissage que toute théorie.

Pour ce faire, la meilleure façon est de vous rendre sur GitHub ou Kaggle et de consulter des projets publics. Passez en revue quelques-uns jusqu'à ce que vous trouviez celui qui vous parle. 

Cela pourrait être une bibliothèque complète, une simple analyse ou une IA prête pour la production. Quoi que ce soit, trouvez-en quelques-uns et sélectionnez ensuite le projet qui vous intéresse le plus.

Une fois que vous avez ce projet, prenez le temps de parcourir la documentation, la structure de la base de code et le code. Vous serez probablement perdu. Surtout si vous ne savez pas grand-chose sur la façon de coder. Mais c'est un sentiment positif lorsque vous apprenez quelque chose de nouveau !

Prenez quelques notes sur les motifs répétés que vous voyez, les éléments intéressants que vous comprenez ou les sujets que vous ne comprenez pas vraiment. Marquez ce projet et revenez-y lorsque vous aurez avancé dans votre parcours d'apprentissage.

Un bon endroit pour commencer à chercher est [cette liste sur GitHub](https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code). Cependant, une simple recherche sur [Kaggle](https://www.kaggle.com/) ou GitHub avec des mots-clés liés à vos intérêts en machine learning fera l'affaire.

Pour mon plan d'apprentissage spécifique, un bon projet simple est celui-ci de [Thomas Kipf](https://github.com/tkipf/pygcn). Il est suffisamment simple pour que je puisse le parcourir et comprendre ce qui se passe à chaque section, tout en apprenant les bases de la structure.

## Étape 2 : Apprenez le langage de programmation

Maintenant que vous avez une image très claire de l'endroit où vous devez aller et de ce que vous devez apprendre, il est temps de comprendre le code.

Le code sera très probablement basé sur Python, mais selon ce que vous voulez apprendre et le projet que vous avez marqué, vous pourriez vous retrouver avec Julia, C++, Java ou autres. 

Quel que soit le langage, vous devriez prendre le temps d'apprendre les bases afin de comprendre comment assembler des scripts.

Un très bon cours pour apprendre suffisamment de Python afin d'être fonctionnel est le [cours de calcul scientifique avec Python de freeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/) ou le [très court cours de Python de Kaggle](https://www.kaggle.com/learn/python). 

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Capture.PNG)
_Je recommande vivement celui de freeCodeCamp !_

Vous n'avez pas besoin de comprendre 100% du fonctionnement du langage. À chaque passage dans ce programme, passez un peu de temps à affiner vos connaissances du langage de programmation que vous choisissez afin que l'apprentissage soit itératif.

Dans mon cas pour mon plan d'apprentissage, le cours de freeCodeCamp ferait l'affaire.

## Étape 3 : Apprenez les bibliothèques de haut en bas

Une chose que je vois souvent dans les programmes de machine learning est qu'ils commencent à implémenter certains des algorithmes à partir de zéro après avoir appris les bases du ML. 

Bien que je pense que c'est un excellent projet à faire en soi, je ne pense pas que cela doive être le principal objectif au début de votre parcours d'apprentissage du machine learning.

La principale raison est que presque personne n'implémente des algorithmes à partir de zéro, sauf les personnes qui font les packages que les développeurs utilisent. Même alors, ils s'appuient souvent sur d'autres packages faits par des spécialistes de l'algèbre linéaire pour faire une grande partie du travail de bas niveau.

Tout cela pour dire que bien qu'avoir une forte compréhension de la manière dont les choses fonctionnent sous le capot est un net positif, je ne pense pas que cela doive être un objectif précoce.

Ce que je recommande fortement à ce stade est d'apprendre la bibliothèque de plus haut niveau dans le langage de programmation que vous choisissez, qui vous permettra d'atteindre les résultats finaux. Apprenez à utiliser ce package de très haut niveau suffisamment pour créer quelque chose qui fonctionne. 

Vous manquerez définitivement de compréhension quant à pourquoi quelque chose fonctionne ou non à ce stade, mais cela n'a pas trop d'importance.

Ce qui compte, c'est d'être capable de faire bouger vos mains avec les outils que les experts utilisent réellement au quotidien. Une fois que vous aurez à peu près compris ce que fait la bibliothèque de haut niveau, vous devriez passer à une bibliothèque légèrement plus bas niveau. 

Assurez-vous de ne pas aller trop loin dans l'apprentissage de la bibliothèque, cependant (si vous êtes au niveau [LAPACK](http://www.netlib.org/lapack/) en lisant sur Fortran, vous êtes allé trop loin !!).

Pour mon projet, la principale bibliothèque que je dois apprendre est Pytorch ou son wrapper de haut niveau, donc [un cours pratique de fast.ai](https://course.fast.ai/) ferait l'affaire.

## Étape 4 : Réalisez un projet qui vous passionne en maximum un mois

Maintenant vient la partie où la plupart de l'apprentissage aura lieu. À ce stade, vous devriez avoir les connaissances minimales nécessaires pour assembler un projet qui a une utilité minimale. 

Juste une note – si vous vous sentez totalement confiant en commençant le projet que vous planifiez, vous n'avez pas avancé assez vite à travers les étapes 0 à 3.

Pensez à quelque chose dans votre domaine d'intérêt que vous aimeriez vraiment créer et développer. Ne devenez pas trop fou sur le projet, cependant, car il devrait prendre entre 1 semaine et 1 mois maximum pour être terminé. 

**Mettez cette date dans votre calendrier avec une notification.** Avoir un projet limité dans le temps est à la fois motivant et juste assez stressant pour que vous le terminiez.

L'idée ici est de lutter suffisamment sur un projet de taille moyenne pour comprendre où se trouvent vos principales lacunes en connaissances et pour vivre ce qu'un développeur en machine learning vit réellement. 

En allant en mode libre sans le harnais d'un cours ou d'un livre, vous pourrez faire les parties réelles d'un projet de ML qui sont difficiles :

* Planifier, définir le périmètre et suivre la progression de votre projet de ML
* Lire la documentation en ligne sur les bibliothèques
* Lire StackOverflow, les fils de discussion GitHub, un article de blog d'un ingénieur aléatoire et un forum d'aide cryptique sur ce bug 📺.
* Construire votre projet de manière sous-optimale et l'améliorer au fil du temps.
* Déboguer le surapprentissage, le sous-apprentissage et les problèmes de généralisation.

Pour choisir un projet qui vous intéresse, je suggère de faire ces trois petits exercices :

* Réfléchissez profondément à ce qui vous intéresse actuellement 
* Consultez une liste d'idées de projets
* Jetez un coup d'œil aux jeux de données ouverts

En faisant un mélange de ces trois choses, vous serez en mesure de former plus de contexte sur ce qui est possible. Vous pourrez également mixer et associer vos intérêts pour créer quelque chose de vraiment à vous.

Cette [liste sur Github](https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code) devrait être un très bon endroit pour obtenir de l'inspiration sur un mini-projet à faire. Vous pouvez ensuite combiner cela avec le [moteur de recherche de jeux de données Google](https://datasetsearch.research.google.com/) afin de trouver des données qui correspondent à votre projet.

⚠️ Ne sous-estimez pas l'importance des données. ⚠️  
Même si vous avez de très bonnes idées, si aucune donnée n'est disponible, cela entravera gravement votre progression. 

Pour mes intérêts, j'ai trouvé ce jeu de données intéressant sur la [Chaîne d'approvisionnement mondiale d'une entreprise minière](https://figshare.com/articles/dataset/Mining_Company_s_Global_Supply_Chain_Logistics_Data_for_a_Medium_Size_Excavator_Extended_Dataset/2749120/1) avec suffisamment de données pour en faire quelque chose. Mon projet consistera à modéliser les données sous forme de graphe et à utiliser des Graph Neural Networks pour déduire les prix de vente d'une excavatrice qui est le sujet central de ce jeu de données.

## Étape 5 : Identifiez une lacune dans vos connaissances et apprenez à son sujet

À ce stade, vous avez passé du temps à élaborer votre projet et vous êtes réellement impressionné par la distance que vous avez parcourue avec lui. Il est probablement loin de ce que vous aviez en tête, cependant, et vous avez rencontré d'innombrables problèmes sur votre chemin. 

Maintenant, vous réalisez à quel point vous en savez peu et qu'il y a certaines parties de vos connaissances que vous devez vraiment combler.

![Vivre les meilleurs moments de leur vie.](https://images.unsplash.com/photo-1573269354259-8c108692afa1?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDE1fHxzdW4lMjBwZW9wbGV8ZW58MHx8fHwxNjI1NTAwODU0&ixlib=rb-1.2.1&q=80&w=2000)
_Vous vous réjouissant de votre ignorance nouvellement découverte ! Félicitations 👍 : Photo par [Unsplash](https://unsplash.com/@daniel_joshua_?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Daniel Joshua</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

C'est génial ! Faites une liste de toutes les lacunes que vous avez vues en cours de route et classez-les par ordre de priorité estimée. Cela peut être difficile pour vous, puisque tout semblera très important à ce stade. Mais faire l'exercice de prendre une décision consciente sur ce qu'il faut apprendre ensuite est presque aussi précieux que l'apprentissage lui-même.

Voici la partie étrange : éliminez tout de votre liste et n'apprenez que le morceau de connaissance le plus important.

Quand je dis éliminer, je le pense vraiment. Supprimez tout sauf le premier. Lorsque vous faites une autre passe dans cette boucle, votre estimation de ce qu'il faut apprendre ensuite sera principalement fausse et vous manquerez d'autres morceaux de connaissance plus critiques que vous ne connaissiez pas.

Maintenant que vous n'avez plus qu'un seul élément à apprendre, donnez-vous entre 1 jour et 1 semaine pour apprendre ce sujet particulier. Cela peut sembler très court, mais ce que vous voulez vraiment ici, c'est d'aller juste assez loin dans la connaissance pour être fonctionnel pour votre prochaine ronde d'apprentissage. 

![Designer esquissant des Wireframes](https://images.unsplash.com/photo-1434030216411-0b793f4b4173?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDJ8fGxlYXJuaW5nfGVufDB8fHx8MTYyNDEyNzY5NA&ixlib=rb-1.2.1&q=80&w=2000)
_Étudiez ce petit morceau de connaissance très dur pendant une courte période de temps : Photo par [Unsplash](https://unsplash.com/@craftedbygc?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Green Chameleon</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

En pratique, ce qui peut arriver, c'est que vous allez assez loin dans ce sujet pour remarquer comment il se lie à d'autres sujets importants (comme la probabilité, les statistiques, ou même l'algèbre linéaire maudite). 

Jetez un coup d'œil à ces liens, suivez-les si vous en avez envie, et renforcez votre modèle mental du machine learning afin de le rendre plus précis.

## Étape 6 : Répétez les étapes 0 à 5

Votre premier passage dans ce pipeline sera probablement moyen au mieux. Mais vous aurez appris beaucoup plus en très peu de temps que tout ce que vous auriez pu accomplir avec l'approche de bas en haut.

La valeur que vous tirerez de cette méthode augmente assez rapidement à chaque passage dans le pipeline. Chaque tour sera plus facile et vous aurez une image plus claire du domaine.

Cette méthodologie est basée sur la méthodologie lean que j'ai appris à appliquer dans ma [startup](https://axya.co/en/) avec grand succès. Faire plusieurs itérations sur le sujet que vous optimisez est le moyen le plus rapide d'atteindre votre objectif.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-168.png)
_Cycle lean en trois étapes, image prise [ici](https://www.calltheone.com/en/consultants/build-measure-learn-cycle-lean-startup)._

Dans l'année, vous pourriez être en mesure d'empiler 12 passages à travers ce pipeline, ce qui signifie 12 projets de machine learning et une compréhension très pratique du domaine.

Cette méthode vous rendra à la fois très embauvable et vous donnera les outils dont vous avez besoin pour vous améliorer, tout seul.

De plus, en tant que note à part pour les personnes déjà familières avec le machine learning, **c'est la descente de gradient**. Vous faites littéralement une descente de gradient sur le problème "apprendre le machine learning" en faisant un petit pas dans le plan de coût de votre ignorance. 

Vous faites même une variante de la descente de gradient qui regarde vers l'avant dans le plan de coût et est capable de ralentir (passer plus de temps sur un projet ou un concept d'apprentissage) ou d'accélérer (sauter lorsque le sujet n'est pas si pertinent pour votre compréhension). C'est [Nesterov-accelerated gradient](https://youtu.be/6FrBXv9OcqE) en un mot 😄 (lol désolé pour ce bit) !

![Image](https://www.freecodecamp.org/news/content/images/2021/06/maxresdefault.jpg)
_C'est vous dans votre plan de coût d'ignorance du machine learning qui descend waaaaaay down._

## Résumé et conclusion

En résumé, vous devriez :

1. Découvrir à quoi ressemble le domaine du ML et en faire une carte mentale.
2. Trouver un projet cool que vous aimeriez faire et l'étudier.
3. Apprendre le langage de programmation requis.
4. Apprendre suffisamment de bibliothèques pour pouvoir faire quelque chose d'utile.
5. Faire un projet pendant [1 semaine, 1 mois].
6. Apprendre une chose que vous avez vue comme une grande lacune dans vos connaissances.
7. Et réitérer !

J'espère que cela a été utile, n'hésitez pas à me contacter via [LinkedIn](https://www.linkedin.com/in/yacine-mahdid-809425163/) si vous avez des opinions fortes sur ce processus. De plus, si vous voulez en savoir plus sur un sujet spécifique de machine learning, consultez ma [chaîne YouTube](https://www.youtube.com/channel/UCts-XMcexTiPSR8QbyRGFxA).

Passez une excellente journée 👋

# Ressources utiles pour le Machine Learning

Dans cette section, je vais partager une collection de ressources d'apprentissage que je recommande pour les personnes souhaitant commencer à apprendre. Ce n'est pas une liste exhaustive, mais ce sera un bon point de départ pour les personnes souhaitant obtenir un premier bon modèle mental du Machine Learning.

## Livres sur le Machine Learning

### Les éléments de l'apprentissage statistique par Astie et al.

Un classique dans la communauté du machine learning, je recommande vivement de passer du temps avec ce livre encore et encore.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-26.png)
_Grand livre d'introduction !_

### Intelligence artificielle, une approche moderne (3ème édition)

Cela vous donnera un bon aperçu du domaine plus large de l'intelligence artificielle qui n'inclut pas nécessairement le machine learning.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-27.png)
_Ce livre relie tout le domaine de l'IA/ML/DL assez bien_

### Le livre du Deep Learning

Grand classique dans le domaine du deep learning, c'est surprenamment un livre très accessible si vous avez quelques notions d'algèbre linéaire (il y a une introduction au début).

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-29.png)
_La couverture est très soignée car elle a été générée par un réseau de neurones profond_

### Python Data Science Handbook : Outils essentiels pour travailler avec les données

Vraiment excellent livre pour pouvoir améliorer vos compétences en science des données dans Pandas et Numpy. Cela rendra votre code beaucoup plus compact, efficace et lisible.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-30.png)
_Gardez-le près de votre bureau et faites les exercices_

### Hands-On Machine Learning avec Scikit-Learn, Keras et TensorFlow : Concepts, outils et techniques pour construire des systèmes intelligents

Si vous deviez choisir un livre pour vous lancer, ce serait celui-ci. Très complet et pratique.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-31.png)
_Prenez soit le lézard HD ou celui en niveaux de gris, les deux sont très solides !_

### Deep Learning avec Pytorch

J'adore ce livre car il donne un aperçu direct par les créateurs de Pytorch sur leur philosophie (et il y a quelques exemples de neurosciences intéressants là-dedans que je suis toujours heureux de voir).

![Image](https://www.freecodecamp.org/news/content/images/2021/07/71sXWAx3ktL.jpg)
_Les visuels pour celui-ci sont très bien faits, surtout la partie sur les tenseurs._

## Blogs sur le Machine Learning

### Machine Learning Mastery

Si vous finissez par googler beaucoup de choses sur un projet (comme tout être humain), vous finirez assez souvent sur ce blog : [machinelearningmastery](https://machinelearningmastery.com).

Il est assez bien écrit et le SEO que cette personne a réussi à obtenir sur le site pour les sujets liés au ML est assez impressionnant.

### Analytics Vidhya

Le deuxième blog que vous trouverez probablement sur Google est celui-ci, [analyticsvidhya](https://www.analyticsvidhya.com). Il peut sembler un peu plus spammy que le précédent, mais il y a encore beaucoup de contenu intéressant.

### Distill

Un journal très riche visuellement pour les sujets de machine learning : [distill.pub](https://distill.pub/)

Il semble qu'ils prennent une année sabbatique car toute l'équipe a brûlé, mais néanmoins, il y a du contenu de haute qualité en ML.

## Communauté de Machine Learning

### r/MachineLearning

[Grande communauté](https://www.reddit.com/r/MachineLearning/) pour obtenir les derniers développements en machine learning et/ou pour obtenir un avis sur les événements actuels dans la communauté ML.

Elle partage du contenu de haute qualité, et en traînant là-bas pendant un moment, vous aurez une idée de ce que les autres dans le domaine pensent.

Elle génère également de bonnes pépites d'apprentissage comme [celle-ci](https://www.reddit.com/r/MachineLearning/comments/5z8110/d_a_super_harsh_guide_to_machine_learning/) :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Capture-1.PNG)
_Ceci est très direct, mais toujours pertinent._

### r/LearnMachineLearning

C'est une [excellente communauté pour les nouveaux venus](https://www.reddit.com/r/learnmachinelearning/) pour poser des questions, publier vos projets ou obtenir de l'inspiration à partir du travail des autres.

## Événements de Machine Learning

### Conférence MAIN (Montréal AI et Neuroscience)

Je suis partial ici car c'est une conférence qui réunit deux de mes intérêts : les neurosciences et le machine learning : [lien 2020](https://www.main2020.org/) & [vidéo YouTube](https://www.youtube.com/channel/UCddp3o-ctW8rmYtfdDfVUkA)

De plus, comme elle est organisée à Montréal et que j'habite à proximité, je peux généralement y faire un saut pour voir quelles sont les dernières avancées en neurosciences computationnelles.

### Conférence NeurIPS (Neural Information Processing Systems)

Celle-ci est la [conférence mythique sur le machine learning](https://nips.cc/) sur les réseaux de neurones.

Elle est devenue un peu surpeuplée ces dernières années, au point que son utilité a été remise en question. Néanmoins, si vous ne pouvez pas y assister, vérifier ce sur quoi travaillent les chercheurs qui y sont acceptés est une bonne idée.

Il y en a [beaucoup d'autres](https://www.guide2research.com/topconf/machine-learning) et c'est une bonne idée d'aller à des conférences de temps en temps pour voir des recherches vraiment de pointe. Cela peut être un peu écrasant, mais c'est une grande expérience d'apprentissage.

## Cours en ligne sur le Machine Learning

### Fast AI

Si je devais recommander un cours en ligne, ce serait [celui de FastAI](https://course.fast.ai/#How-do-I-get-started?).

Il incarne en fait cette approche pragmatique-allant-droit-à-l'action dont j'ai parlé dans cet article de blog + l'enseignant est très divertissant. 

### Andrew Ng ML (bien sûr)

Si j'en avais un deuxième à recommander, je choisirais [le cours d'Andrew Ng sur le machine learning](https://www.coursera.org/learn/machine-learning).

### Cours YouTube de Machine Learning et d'analyse de données de freeCodeCamp

freeCodeCamp propose de nombreux cours de Machine Learning et d'analyse de données sur sa chaîne YouTube, comme :

* [Python pour la bioinformatique](https://www.freecodecamp.org/news/python-for-bioinformatics-use-machine-learning-and-data-analysis-for-drug-discovery/)
* [Cours accéléré sur Python et scikit-learn](https://www.freecodecamp.org/news/learn-scikit-learn/)
* [Plongez dans le Deep Learning](https://www.freecodecamp.org/news/learn-deep-learning-from-the-president-of-kaggle/)
* [Comment analyser des données avec Python, Pandas et NumPy](https://www.freecodecamp.org/news/how-to-analyze-data-with-python-pandas/)
* [Deep learning avec PyTorch](https://www.freecodecamp.org/news/free-deep-learning-with-pytorch-live-course/)
* Et bien sûr, [Python pour tout le monde du Dr. Chuck](https://www.freecodecamp.org/news/python-for-everybody/)

Il y en a beaucoup plus d'où ceux-ci viennent – il suffit de se rendre sur la chaîne YouTube de freeCodeCamp et de rechercher ce que vous voulez apprendre.