---
title: Les meilleures ressources que j'ai utilisées pour m'auto-apprendre le Machine
  Learning
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-12T19:39:11.000Z'
originalURL: https://freecodecamp.org/news/the-best-resources-i-used-to-teach-myself-machine-learning-part-1-292232d167
coverImage: https://cdn-media-1.freecodecamp.org/images/1*92h6Lg1Bu1F9QqoVNrkLdQ.jpeg
tags:
- name: AI
  slug: ai
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: Les meilleures ressources que j'ai utilisées pour m'auto-apprendre le Machine
  Learning
seo_desc: 'By Gwendolyn Faraday


  The field of machine learning is becoming more and more mainstream every year. With
  this growth come many libraries and tools to abstract away some of the most difficult
  concepts to implement for people starting out.

  Most people...'
---

Par Gwendolyn Faraday

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-57.png)

Le domaine du machine learning devient de plus en plus grand public chaque année. Avec cette croissance viennent de nombreuses bibliothèques et outils pour abstraire certains des concepts les plus difficiles à implémenter pour les débutants.

La plupart des gens diront que vous avez besoin d'un diplôme de niveau supérieur en ML pour travailler dans l'industrie. Si vous aimez travailler avec des données et des mathématiques pratiques, alors je dirais que ce n'est pas vrai. Je n'ai pas obtenu de diplôme universitaire en Machine Learning ou en données, pourtant je travaille avec le ML en ce moment dans une startup. Je veux partager ce que j'ai utilisé pour apprendre et comment j'en suis arrivée là dans l'espoir que cela aidera quelqu'un d'autre.

### Pour commencer

Je connaissais déjà Python lorsque j'ai commencé, mais si ce n'est pas votre cas, je recommande d'apprendre d'abord le Python de base et intermédiaire. Le langage est assez facile à apprendre comparé à d'autres. Python est également le foyer de la plus grande communauté de data science/ML, donc il y a des tonnes d'outils pour vous aider pendant que vous apprenez.

[Apprendre Python : freeCodeCamp Python Crash Course](https://www.youtube.com/watch?v=rfscVS0vtbw)

Cela étant dit, la première chose à faire est de télécharger « The Machine Learning Podcast » par OCDevel ([overcast.fm](https://overcast.fm/itunes1204521130/machine-learning-guide), [iTunes](https://itunes.apple.com/us/podcast/machine-learning-guide/id1204521130)) dans votre application de podcast préférée. Écoutez les 10 à 15 premiers épisodes. Ils sont très bons pour donner un aperçu de l'écosystème du machine learning et il y a aussi des ressources recommandées qui sont liées sur le [site OCDevel](http://ocdevel.com/mlg).

### Outils

Anaconda & Jupyter Notebook — Ce sont des incontournables pour le ML et la data science. Suivez les [instructions ici](https://jupyter.org/install) pour les installer et les configurer.

[Visual Studio Code](https://code.visualstudio.com/) avec [Plugin Python](https://code.visualstudio.com/docs/languages/python) — Je n'aurais jamais pensé recommander un produit Microsoft, mais je suis honnêtement impressionnée par leur engagement open source ces derniers temps. C'est maintenant mon éditeur de code préféré, même pour faire certaines choses en Python — comme déboguer du code.

[Kaggle.com](https://www.kaggle.com/) est le meilleur endroit pour trouver des jeux de données lorsque vous commencez. Allez-y et inscrivez-vous pour un compte et explorez le site. Vous remarquerez qu'il y a de nombreuses compétitions pour les personnes de tous niveaux d'expérience et même des tutoriels pour les accompagner (comme [celui-ci pour débutants](https://www.kaggle.com/c/titanic#tutorials) sur le Titanic). Ces jeux de données seront très utiles pour vous entraîner tout en apprenant les bibliothèques Python.

### Bibliothèques Python

Ensuite, il est important d'apprendre les bibliothèques Python courantes pour travailler avec des données : Numpy, Matplotlib, Pandas, Scikit-Learn, etc. Je recommande de commencer par [ce cours de datacamp](https://campus.datacamp.com/courses/intro-to-python-for-data-science). Il passe en revue quelques bases que vous pouvez sauter ou utiliser pour révision et la section Numpy est une bonne introduction.

Pandas est un incontournable mais prend aussi un peu de temps à maîtriser car il fait tant de choses. Il est construit sur Numpy et est utilisé pour nettoyer, préparer et analyser les données. Il dispose également d'outils intégrés pour des choses comme la visualisation. J'ai utilisé de nombreuses ressources pour apprendre Pandas et m'entraîner avec. En voici quelques-unes :

1. [Apprendre Pandas sur Kaggle](https://www.kaggle.com/learn/pandas)
2. [Cours vidéo sur Pandas](https://www.youtube.com/playlist?list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y) | [Cahier du cours](https://nbviewer.jupyter.org/github/justmarkham/pandas-videos/blob/master/pandas.ipynb)
3. Exemples supplémentaires de Jupyter Notebook : [Bases](https://nbviewer.jupyter.org/github/fonnesbeck/Bios8366/blob/master/notebooks/Section2_1-Introduction-to-Pandas.ipynb) | [Tracé avec Matplotlib & Pandas](https://nbviewer.jupyter.org/github/fonnesbeck/Bios8366/blob/master/notebooks/Section0_2-Plotting-and-Visualization.ipynb) | [Et bien d'autres](https://github.com/fonnesbeck/Bios8366/tree/master/notebooks)

Après Pandas vient Scikit-Learn. C'est ici que les choses commencent à être appliquées davantage aux algorithmes réels de machine learning. Scikit-Learn est une bibliothèque Python scientifique pour le machine learning.

La meilleure ressource que j'ai trouvée pour cela jusqu'à présent est le livre « [Hands on Machine Learning with Scikit-Learn and Tensorflow](https://www.amazon.com/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/1491962291/ref=sr_1_4) ». Je pense qu'il fait un très bon travail pour vous enseigner étape par étape avec des exemples pratiques. La première moitié concerne Scikit-Learn, donc j'ai fait cette partie en premier puis je suis revenue à la partie Tensorflow.

Il existe de nombreuses autres bibliothèques Python comme Keras et PyTorch, mais j'aborderai celles-ci plus tard. Cela fait déjà beaucoup à apprendre :)

### Apprentissage superficiel

C'est la première étape dans le machine learning. Scikit-Learn dispose de fonctions d'apprentissage superficiel comme la régression linéaire intégrées dans la bibliothèque. Le livre Scikit-Learn que j'ai mentionné ci-dessus enseigne de nombreux types d'algorithmes courants de machine learning et vous permet de pratiquer avec des exemples concrets.

Bien que ce soit bien, j'ai encore trouvé utile de suivre également le cours de Machine Learning d'Andrew Ng de Stanford. [Il est disponible pour être audité gratuitement sur Coursera](https://www.coursera.org/learn/machine-learning#syllabus) (il existe un podcast pour ce cours sur iTunes, mais il est un peu difficile à suivre et bien plus vieux qu'une décennie). La qualité de l'enseignement est incroyable et c'est l'une des ressources les plus recommandées en ligne (ce n'est pas la plus facile à suivre, c'est pourquoi je la recommande ici).

Commencez à suivre lentement le cours d'Andrew Ng et ne vous frustrez pas si vous ne comprenez pas quelque chose. J'ai dû le mettre de côté et le reprendre plusieurs fois. J'ai également suivi Matlab à l'université, qui est le langage qu'il utilise dans le cours, donc je n'ai pas eu de problème avec cette partie. Mais si vous voulez utiliser Python à la place, vous pouvez trouver [les exemples traduits en ligne](https://github.com/kaleko/CourseraML).

### Mathématiques :)

Oui, les mathématiques sont nécessaires. Cependant, je ne pense pas qu'une approche intense, axée sur les mathématiques, soit la meilleure façon d'apprendre ; c'est intimidant pour beaucoup de gens. Comme le suggère OCDevel dans son podcast (lié ci-dessus), passez la plupart de votre temps à apprendre le machine learning pratique et peut-être 15 à 20 % à étudier les mathématiques.

Je pense que la première étape ici est d'apprendre/rafraîchir les statistiques. Cela peut être plus facile à digérer et être à la fois beaucoup plus amusant et pratique. Après les statistiques, vous devrez définitivement apprendre un peu d'algèbre linéaire et un peu de calcul pour vraiment savoir ce qui se passe dans le deep learning. Cela prendra un certain temps, mais voici quelques-unes des ressources que je recommande pour cela.

**Ressources en statistiques :**

1. Je pense que les cours de statistiques sur Udacity sont assez bons. Vous pouvez commencer par [celui-ci](https://www.udacity.com/course/intro-to-statistics--st101) puis explorer les autres qu'ils offrent.
2. J'ai adoré le livre, « [Naked Statistics](https://www.amazon.com/Naked-Statistics-Stripping-Dread-Data/dp/039334777X/ref=sr_1_1) ». Il est rempli d'exemples pratiques et agréable à lire.
3. Il est également utile de comprendre les statistiques bayésiennes et comment elles diffèrent des modèles fréquentistes et classiques. [Ce cours Coursera](https://www.coursera.org/learn/bayesian-statistics) fait un excellent travail en expliquant ces concepts — il y a aussi [une partie 2 du cours ici](https://www.coursera.org/learn/mcmc-bayesian-statistics).

**Ressources en algèbre linéaire :**

1. Le livre, « [Linear Algebra, Step by Step](https://www.amazon.com/Linear-Algebra-Step-Kuldeep-Singh/dp/0199654441/ref=sr_1_7) » est excellent. C'est comme un manuel de lycée/université mais bien écrit et facile à suivre. Il y a aussi beaucoup d'exercices pour chaque chapitre avec des réponses à la fin.
2. [Série vidéo Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) — Les explications mathématiques de 3blue1brown sont incroyables. Je recommande vivement son contenu mathématique.
3. Il y a un aperçu de l'algèbre linéaire dans le cours d'Andrew Ng également, mais je pense que les deux ressources que je liste ci-dessus sont un peu plus faciles à utiliser pour apprendre le sujet.

**Ressources en calcul :**

J'avais suivi quelques années de calcul auparavant, mais j'ai encore dû me rafraîchir la mémoire. J'ai acheté un manuel d'occasion pour Calc. 1 dans une librairie locale pour commencer. Voici quelques ressources en ligne qui m'ont également aidé.

1. [Série vidéo Essence of Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)
2. [Understanding Calculus](https://www.thegreatcoursesplus.com/understanding-calculus) de The Great Courses Plus

**Autres mathématiques utiles :**

1. [Mathematical Decision Making](https://www.thegreatcoursesplus.com/mathematical-decision-making-predictive-models-and-optimization) de The Great Courses Plus

### Deep Learning

Après avoir appris quelques mathématiques et les bases de la data science et du machine learning, il est temps de plonger dans plus d'algorithmes et de réseaux de neurones.

Vous avez probablement déjà eu un aperçu du deep learning avec certaines des ressources que j'ai mentionnées dans la partie 1, mais voici quelques ressources vraiment bonnes pour vous introduire aux réseaux de neurones. Au moins, elles seront une bonne révision et combleront quelques lacunes pour vous.

1. [Série de 3blue1brown expliquant les réseaux de neurones](https://www.youtube.com/watch?v=aircAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
2. [Liste de lecture d'introduction au Deep Learning de Deeplizard](https://www.youtube.com/watch?v=gZmobeGL0Yg&list=PLZbbT5o_s2xq7LwI2y8_QtvuXZedL6tQU)

Pendant que vous travaillez sur le cours Stanford d'Andrew Ng, je recommande de consulter fast.ai. Ils ont plusieurs cours vidéo pratiques de haute qualité qui peuvent vraiment aider à apprendre et à cimenter ces concepts. Le premier est [Practical Deep Learning for Coders](http://course.fast.ai/) et le second — tout juste sorti — est [Cutting Edge Deep Learning For Coders, Part 2](http://course.fast.ai/part2.html). J'ai appris tant de choses en regardant et en re-regardant certaines de ces vidéos. Une autre fonctionnalité incroyable de fast.ai est [le forum communautaire](https://forums.fast.ai/) ; probablement l'un des forums IA les plus actifs en ligne.

### Bibliothèques de Deep Learning en Python

Je pense qu'il est bon d'apprendre un peu de chacune de ces trois bibliothèques. Keras est un bon point de départ car son API est conçue pour être plus simple et plus intuitive. En ce moment, j'utilise presque exclusivement PyTorch, qui est mon préféré personnel, mais elles ont toutes des avantages et des inconvénients. Il est donc bon de savoir laquelle choisir dans différentes situations.

**Keras**

* [Liste de lecture Deeplizard Keras](https://www.youtube.com/watch?v=RznKVRTFkBY&list=PLZbbT5o_s2xrwRnXk_yCPtnqqo4_u2YGL) — Cette chaîne a des explications et des exemples vraiment bons. Vous pouvez suivre les vidéos gratuitement, ou avoir accès aux cahiers de code également en [vous abonnant sur Patreon](https://www.patreon.com/deeplizard) au niveau de 3 $ (USD).
* J'ai également trouvé la [documentation pour Keras](https://keras.io/) être assez bonne
* Datacamp a de nombreux tutoriels bien écrits pour le ML et Keras comme [celui-ci](https://www.datacamp.com/community/tutorials/deep-learning-python)

**Tensorflow**

* La section Tensorflow du livre, « [Hands on Machine Learning with Scikit-Learn and Tensorflow](https://www.amazon.com/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/1491962291/ref=sr_1_4) » (mentionné également ci-dessus)
* [Série Deeplizard Tensorflow](https://www.youtube.com/watch?v=HEQDRWMK6yY&list=PLZbbT5o_s2xr83l8w44N_g3pygvajLrJ-)

**PyTorch**

* [Série Deeplizard Pytorch](https://www.youtube.com/watch?v=v5cngxo4mIg&list=PLZbbT5o_s2xrfNyHZsM6ufI0iZENK9xgG)
* [Bootcamp Pytorch d'Udacity](https://www.udacity.com/course/deep-learning-pytorch--ud188) — Je suis actuellement le nanodiplôme de Deep Reinforcement Learning d'Udacity et j'ai trouvé leur section PyTorch plus tôt dans le cours très bonne. Ils sont sur le point de le lancer gratuitement au public ! [Voici certains de leurs cahiers PyTorch sur Github](https://github.com/udacity/DL_PyTorch).
* [Fast.ai](http://www.fast.ai/) est également construit avec PyTorch — Vous apprendrez cette bibliothèque si vous suivez leurs cours.

### Blogs et articles de recherche

J'ai trouvé très utile de lire les recherches actuelles pendant que j'apprends. Il existe de nombreuses ressources qui aident à rendre les concepts compliqués, et les mathématiques qui les sous-tendent, plus faciles à digérer. Ces articles sont également beaucoup plus amusants à lire que vous ne le pensez.

1. [Blog fast.ai](http://www.fast.ai/topics/)
2. [Distill .pub](https://distill.pub/) — Recherche en Machine Learning expliquée clairement
3. [Two Minute Papers](https://www.youtube.com/user/keeroyz) — Courtes vidéos de décomposition d'articles de recherche en IA et autres
4. [Arvix Sanity](http://www.arxiv-sanity.com/) — Outil plus intuitif pour rechercher, trier et sauvegarder des articles de recherche
5. [Feuille de route des articles de Deep Learning](https://github.com/floodsung/Deep-Learning-Papers-Reading-Roadmap)
6. [Subreddit Machine Learning](https://www.reddit.com/r/MachineLearning/) — Ils ont des fils de discussion « qu'est-ce que vous lisez » discutant des articles de recherche
7. [Arxiv Insights](https://www.youtube.com/channel/UCNIkB2IeJ-6AmZv7bQ1oBYg) — Cette chaîne a quelques excellentes décompositions d'articles de recherche en IA

### Éducation audio-supplementaire

1. [The Data Skeptic](https://dataskeptic.com/podcast/) — Ils ont beaucoup de bons épisodes plus courts, appelés [mini] où ils couvrent des concepts de machine learning
2. [Software Engineering Daily Machine Learning](https://itunes.apple.com/us/podcast/machine-learning-software-engineering-daily/id1230807136?mt=2)
3. [Podcast Machine Learning d'OCDevel](https://itunes.apple.com/us/podcast/machine-learning-guide/id1204521130) — J'ai déjà mentionné celui-ci, mais je le liste à nouveau au cas où vous l'auriez manqué

### Ressources d'apprentissage supplémentaires

* [E-book Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/)
* [Machine Learning Yearning](https://www.deeplearning.ai/machine-learning-yearning/) (brouillon gratuit) par Andrew Ng

### La fin

Merci d'applaudir si cela a été utile :)

Réseaux sociaux : [@gwen_faraday](https://twitter.com/gwen_faraday)

*Si vous connaissez d'autres ressources qui sont bonnes, ou voyez que je manque quelque chose, veuillez laisser des liens dans les commentaires. Merci.*