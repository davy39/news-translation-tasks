---
title: Le Guide Incomplet du Deep Learning
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-30T00:11:47.000Z'
originalURL: https://freecodecamp.org/news/the-incomplete-deep-learning-guide-2cc510cb23ee
coverImage: https://cdn-media-1.freecodecamp.org/images/1*b1id84UJ0U-DlzdkUyKgEQ.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Le Guide Incomplet du Deep Learning
seo_desc: 'By Sanny Kim

  From Self-Driving Cars to Alpha Go to Language Translation, Deep Learning seems
  to be everywhere nowadays. While the debate whether the hype is justified or not
  continues, Deep Learning has seen a rapid surge of interest across academia ...'
---

Par Sanny Kim

Des voitures autonomes à Alpha Go en passant par la traduction linguistique, le Deep Learning semble être partout de nos jours. Alors que le débat sur la justification de ce battage médiatique continue, le Deep Learning a connu une augmentation rapide de l'intérêt à travers le milieu universitaire et l'industrie au cours des dernières années.

Avec autant d'attention sur le sujet, de plus en plus d'informations ont été récemment publiées, allant des divers MOOCs aux livres en passant par les chaînes YouTube. Avec une telle quantité de ressources à portée de main, il n'y a jamais eu de meilleur moment pour apprendre le Deep Learning.

Pourtant, un effet secondaire d'un tel afflux de matériel facilement disponible est la surcharge de choix. Avec des milliers et des milliers de ressources, lesquelles valent la peine d'être consultées ?

Inspiré par l'excellent [Guide sur l'apprentissage du développement Blockchain](https://medium.freecodecamp.org/the-authoritative-guide-to-blockchain-development-855ab65b58bc) de Haseeb Qureshi, voici ma tentative de partager les ressources que j'ai trouvées tout au long de mon parcours. Comme je prévois de mettre à jour continuellement ce guide (via [ce dépôt GitHub](https://github.com/sannykim/deep-learning-guide)) avec des informations mises à jour et meilleures, j'ai jugé ce travail en cours comme un **guide incomplet**.

À ce jour, toutes les ressources de ce guide sont gratuites grâce à leurs auteurs.

**Public Cible**

* Toute personne qui souhaite approfondir le sujet, chercher une carrière dans ce domaine, ou aspirer à acquérir une compréhension théorique du Deep Learning

**Objectifs de cet Article**

* Donner un aperçu et un sens de la direction dans l'océan de ressources
* Donner un chemin clair et utile vers l'apprentissage de la théorie et du développement du Deep Learning
* Donner quelques conseils pratiques sur la façon de maximiser votre expérience d'apprentissage

**Plan**

Ce guide est structuré de la manière suivante :

* **Phase 1** : Prérequis
* **Phase 2** : Fondamentaux du Deep Learning
* **Phase 3** : Créer Quelque Chose
* **Phase 4** : Approfondir
* **Phase X** : Continuer à Apprendre

La durée de votre apprentissage dépend de nombreux facteurs, tels que votre dévouement, votre formation et votre engagement en temps. Et selon votre formation et les choses que vous souhaitez apprendre, n'hésitez pas à sauter à n'importe quelle partie de ce guide. La progression linéaire que j'esquisse ci-dessous est simplement le chemin que j'ai trouvé utile pour moi-même.

### **Phase 1 : Prérequis**

Permettez-moi d'être clair dès le début. Les prérequis dont vous avez besoin dépendent des objectifs que vous souhaitez poursuivre. Les fondations dont vous avez besoin pour mener des recherches en Deep Learning diffèrent des choses dont vous avez besoin pour devenir un praticien (les deux ne sont, bien sûr, pas mutuellement exclusifs).

Que vous n'ayez aucune connaissance en codage ou que vous soyez déjà un expert en R, je recommanderais toujours d'acquérir une connaissance pratique de Python, car la plupart des ressources sur le Deep Learning nécessitent de connaître Python.

#### **Codage**

Alors que Codecademy est un excellent moyen de commencer à coder dès le début, les conférences MIT 6.0001 sont une introduction incroyable au monde de l'informatique. Il en va de même pour CS50, le célèbre cours d'introduction à l'informatique de Harvard, mais CS50 se concentre moins sur Python. Pour les personnes qui préfèrent lire, le livre interactif en ligne _How To Think Like A Computer Scientist_ est la voie à suivre.

* [Conférence MIT 6.0001](https://www.youtube.com/watch?v=ytpJdnlu9ug&list=PLUl4u3cNGP63WbdFxL8giv4yhgdMGaZNA)
* [CodeCademy](https://www.codecademy.com/learn/learn-python)
* [How to think like a Computer Scientist](http://interactivepython.org/runestone/static/thinkcspy/index.html)
* [Harvard CS50](https://www.edx.org/course/cs50s-introduction-computer-science-harvardx-cs50x)

![Image](https://cdn-media-1.freecodecamp.org/images/1*LiNKLtHxyV582I5qXc1A1g.png)

#### **Mathématiques**

Si vous souhaitez simplement appliquer des techniques de Deep Learning à un problème que vous rencontrez ou acquérir une compréhension de haut niveau du Deep Learning, il n'est dans la plupart des cas pas nécessaire de connaître ses fondements mathématiques. Mais, selon mon expérience, il a été significativement plus facile de comprendre et même plus gratifiant d'utiliser des frameworks de Deep Learning après s'être familiarisé avec ses fondements théoriques.

Pour de telles intentions, les bases du calcul, de l'algèbre linéaire et des statistiques sont extrêmement utiles. Heureusement, il existe de nombreuses excellentes ressources mathématiques en ligne.

Voici les concepts les plus importants que vous devriez connaître :

1. Calcul à plusieurs variables

* Différenciation
* Règle de la chaîne
* Dérivées partielles

2. Algèbre linéaire

* Définition des vecteurs et matrices
* Opérations et transformations de matrices : addition, soustraction, multiplication, transposée, inverse

3. Statistiques et probabilités

* Idées de base comme la moyenne et l'écart type
* Distributions
* Échantillonnage
* Théorème de Bayes

Cela dit, il est également possible d'apprendre ces concepts simultanément avec la Phase 2, en cherchant les mathématiques chaque fois que vous en avez besoin.

Si vous souhaitez plonger directement dans le calcul matriciel utilisé en Deep Learning, consultez [The Matrix Calculus You Need For Deep Learning](https://arxiv.org/abs/1802.01528) par Terence Parr et Jeremy Howard.

**Calcul**

Pour le calcul, je choisirais entre les conférences MIT OCW, les conférences du Prof. Leonard et Khan Academy.

Les conférences MIT sont idéales pour les personnes à l'aise avec les mathématiques et recherchant une introduction rapide mais rigoureuse au calcul.

Les conférences du Prof. Leonard sont parfaites pour toute personne qui n'est pas trop familière avec les mathématiques, car il prend le temps d'expliquer tout de manière très compréhensible.

Enfin, je recommanderais Khan Academy pour les personnes qui ont simplement besoin d'un rappel ou qui souhaitent obtenir un aperçu aussi rapidement que possible.

* [MIT 18.01 Calcul à une variable](https://www.youtube.com/watch?v=jbIQW0gkgxo&t=1s)
* [Prof Leonard Calcul 1](https://www.youtube.com/watch?v=fYyARMqiaag&list=PLF797E961509B4EB5)
* [Khan Academy Calcul 1](https://www.khanacademy.org/math/calculus-1)

**Algèbre linéaire**

Pour l'algèbre linéaire, j'ai vraiment apprécié la série de conférences du Professeur Strang et son livre accompagnateur sur l'algèbre linéaire (MIT OCW). Si vous êtes intéressé à passer plus de temps sur l'algèbre linéaire, je recommanderais les conférences MIT, mais si vous souhaitez simplement apprendre les bases rapidement ou obtenir un rappel, Khan Academy est parfaite pour cela.

Pour une approche plus pratique du codage, consultez le cours d'algèbre linéaire computationnelle de Rachel Thomas (de fast.ai).

* [MIT 18.06 Algèbre linéaire](https://www.youtube.com/watch?v=ZK3O402wf1c&list=PLE7DDD91010BC51F8)
* [Khan Academy Algèbre linéaire](https://www.khanacademy.org/math/linear-algebra)
* [Algèbre linéaire computationnelle de Rachel Thomas](https://www.youtube.com/watch?v=8iGzBMboA0I&index=1&list=PLtmWHNX-gukIc92m1K0P6bIOnZb-mg0hY)

Enfin, cette [révision](http://cs229.stanford.edu/section/cs229-linalg.pdf) du cours CS229 de Stanford offre une référence utile à laquelle vous pouvez toujours revenir.

Pour le calcul et l'algèbre linéaire, les séries Essence of Calculus et Essence of Linear Algebra de 3Blue1Brown sont de magnifiques matériaux complémentaires pour acquérir une compréhension plus intuitive et visuelle du sujet.

* [3Blue1Brown Essence of Calculus](https://www.youtube.com/watch?v=WUvTyaaNkzM&list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)
* [3Blue1Brown Essence of Linear Algebra](https://www.youtube.com/watch?v=kjBOesZCoqc&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)

**Statistiques et Probabilités**

Harvard a mis toutes ses conférences Stats 110, enseignées par le Prof. Joe Blitzstein, sur YouTube. Elles commencent par les probabilités et couvrent un large éventail de sujets d'introduction aux statistiques. Les problèmes pratiques et le contenu peuvent être difficiles à certains moments, mais c'est l'un des cours les plus intéressants qui existent.

Au-delà du cours de Harvard, Khan Academy et Brandon Foltz ont également du matériel de haute qualité sur YouTube.

* [Harvard Statistics 110](https://www.youtube.com/watch?v=KbB0FjPg0mw&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo)
* [Khan Academy Statistiques & Probabilités](https://www.khanacademy.org/math/statistics-probability)
* [Brandon Foltz's Statistics 101](https://www.youtube.com/user/BCFoltz/videos)

De manière similaire à l'algèbre linéaire, le cours CS229 de Stanford offre également une belle [révision](http://cs229.stanford.edu/section/cs229-prob.pdf) de la théorie des probabilités que vous pouvez utiliser comme point de référence.

### **Phase 2 : Fondamentaux du Deep Learning**

![Image](https://cdn-media-1.freecodecamp.org/images/0*qk29lzFi8rE10bdN)
_[Source de l'image](https://www.kdnuggets.com/2017/08/first-steps-learning-deep-learning-image-classification-keras.html" rel="noopener" target="_blank" title=")_

Avec la pléthore de ressources gratuites de deep learning en ligne, le paradoxe du choix devient particulièrement apparent. Lesquelles dois-je choisir, lesquelles sont les mieux adaptées pour moi, où puis-je apprendre le plus ?

#### **MOOCs**

Tout aussi important que l'apprentissage de la théorie est la pratique de vos nouvelles connaissances, c'est pourquoi mon choix préféré de MOOCs serait un mélange de [_deeplearning.ai_](https://www.coursera.org/specializations/deep-learning) d'Andrew Ng (plus théorique) et de [_fast.ai_](http://course.fast.ai/) de Jeremy Howard et Rachel Thomas (plus pratique).

Andrew Ng est excellent pour expliquer la théorie de base derrière le Deep Learning, tandis que fast.ai est beaucoup plus axé sur le codage pratique. Avec les fondements théoriques de deeplearning.ai, le code et les explications de Jeremy Howard deviennent beaucoup plus intuitifs, tandis que la partie codage de fast.ai est super utile pour ancrer vos connaissances théoriques dans une compréhension pratique.

Puisque deeplearning.ai se compose de cinq cours et fast.ai de deux parties, je structurerais mon apprentissage de la manière suivante :

1. Regarder les conférences des cours I, II, IV et V de Deep Learning.ai
2. Suivre la partie I de Fast.ai
3. Regarder le cours III de Deeplearning.ai
4. Optionnel : Faire les devoirs de deeplearning.ai
5. Répéter les étapes 1-4 ou passer à la phase III

La raison pour laquelle je sauterais d'abord les devoirs de deeplearning.ai est que j'ai trouvé les exemples de codage et les devoirs de fast.ai beaucoup plus pratiques que les devoirs de deeplearning.ai.

Si vous souhaitez réitérer le matériel du cours deeplearning.ai (c'est-à-dire la répétition pour renforcer votre mémoire), alors essayez les devoirs. Contrairement à fast.ai, qui utilise PyTorch et sa propre bibliothèque fastai, ils utilisent principalement Keras. Donc, c'est une bonne opportunité de se familiariser avec un autre framework de Deep Learning.

La partie 2 de Fast.ai traite de sujets assez avancés et nécessite une bonne maîtrise de la théorie ainsi que des aspects de codage du Deep Learning, c'est pourquoi je la mettrais dans la phase IV de ce guide.

**Conseil** : Vous pouvez librement regarder les vidéos de deeplearning.ai sur Coursera, mais vous devez acheter la spécialisation pour faire les devoirs. Si vous ne pouvez pas vous permettre les frais de spécialisation de Coursera, demandez une [bourse](https://learner.coursera.help/hc/en-us/articles/209819033-Apply-for-Financial-Aid) !

Pour les personnes qui préfèrent lire des livres, Michael Nielsen a publié un livre d'introduction gratuit sur le [Deep Learning](http://neuralnetworksanddeeplearning.com/) qui intègre également des exemples de codage en Python.

Pour vraiment tirer parti de fast.ai, vous aurez besoin d'un GPU. Mais heureusement, Google offre un environnement similaire à Jupyter Notebooks appelé [Google Colaboratory](https://colab.research.google.com/) qui vient avec un accès gratuit au GPU. Quelqu'un a déjà fait un tutoriel sur la façon d'utiliser Colab pour Fast.ai. Donc, consultez cela [ici](https://towardsdatascience.com/fast-ai-lesson-1-on-google-colab-free-gpu-d2af89f53604). Kaggle a également commencé à fournir un accès à un GPU Nvidia K80 gratuit sur leurs [Kernels](https://www.kaggle.com/dansbecker/running-kaggle-kernels-with-a-gpu).

![Image](https://cdn-media-1.freecodecamp.org/images/1*uYfELO7WCrolbOPY36obgA.png)
_Google Colaboratory_

AWS offre également aux étudiants jusqu'à 100 $ en crédits (selon que votre collège fait partie de leur programme), que vous pouvez utiliser pour leurs instances GPU.

#### **Matériel Complémentaire Non-MOOC**

Ne vous fiez pas uniquement à un seul moyen d'information. Je recommande de combiner le visionnage de vidéos avec le codage et la lecture.

**YouTube**

Tout comme dans sa série sur le calcul et l'algèbre linéaire, 3Blue1Brown donne l'une des explications les plus intuitives sur les réseaux de neurones. Computer Phile et Brandon offrent également de grandes explications sur le Deep Learning, chacun avec une perspective légèrement différente. Enfin, sentdex peut être utile car il met immédiatement les concepts en code.

* [3Blue1Brown Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
* [Computer Phile Neural Networks](https://www.youtube.com/playlist?list=PLzH6n4zXuckoezZuZPnXXbvN-9jMFV0qh)
* [Brandon Rohrer Neural Networks](https://www.youtube.com/watch?v=ILsA4nyG7I0)
* [Practical Machine Learning sentdex](https://www.youtube.com/watch?v=OGxgnH8y2NM&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v)

**Blogs pour Débutants**

Les blogs sont également un moyen phénoménal de réitérer sur les connaissances nouvellement acquises, d'explorer de nouvelles idées ou d'approfondir un sujet.

[Distill.pub](https://distill.pub/) est l'un des meilleurs blogs que je connaisse dans le domaine du Deep Learning et au-delà. La manière dont ses éditeurs abordent des sujets comme la [Visualisation des Caractéristiques](https://distill.pub/2017/feature-visualization/) ou le [Momentum](https://distill.pub/2017/momentum/) est simplement claire, dynamique et engageante.

Bien que plus mis à jour, l'ancien [blog d'Andrej Karpathy](http://karpathy.github.io/) contient quelques articles classiques sur des sujets tels que les [RNNs](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) qui valent la peine d'être consultés.

Enfin, les publications Medium comme FreeCodeCamp et Towards Data Science publient régulièrement des articles intéressants allant de l'[Apprentissage par Renforcement](https://simoninithomas.github.io/Deep_reinforcement_learning_Course/) à la [Détection d'Objets](https://towardsdatascience.com/deep-learning-for-object-detection-a-comprehensive-review-73930816d8d9).

**Codage**

Familiarisez-vous avec le code ! Savoir comment tracer des graphiques, gérer des données désordonnées et faire du calcul scientifique est crucial en Deep Learning, c'est pourquoi des bibliothèques comme Numpy ou Matplotlib sont omniprésentes. Donc, pratiquer et utiliser ces outils vous aidera définitivement en cours de route.

Jupyter Notebook

* [Introduction, Configuration et Visite Guidée](https://www.youtube.com/watch?v=HW29067qVWk)
* [Tutoriel Complet de DataCamp sur Jupyter Notebook](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook?utm_source=adwords_ppc&utm_campaignid=1366776656&utm_adgroupid=57448230227&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=1t1&utm_creative=265681164941&utm_targetid=aud-364780883969:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9042585&gclid=Cj0KCQjwxtPYBRD6ARIsAKs1XJ4XsOoAhoDXVUIxahP5aX2Ign1X8w1IKQ3RSAvfwnzh9m6rSPLMX1waAs3NEALw_wcB)

Les Jupyter Notebooks peuvent être un excellent outil mais présentent définitivement certains inconvénients. Consultez la présentation informative et pleine de memes de Joel Grus [_I don't Like Notebooks_](https://docs.google.com/presentation/d/1n2RlMdmv1p25Xy5thJUhkKGvjtV-dkAIsUXP-AL4ffI/preview?slide=id.g362da58057_0_1) pour être conscient de ces pièges.

Numpy

* [Tutoriel Numpy de Stanford CS231](http://cs231n.github.io/python-numpy-tutorial/)
* [Tutoriel Numpy de DataCamp](https://www.datacamp.com/community/tutorials/python-numpy-tutorial)

Pandas

* [Série de Tutoriels Complets de Data School sur l'Analyse de Données avec Pandas](https://www.youtube.com/watch?v=yzIMircGU5I&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y)
* [Série de Tutoriels Courts de Code Basics sur Pandas](https://www.youtube.com/watch?v=CmorAWRsCAw&list=PLeo1K3hjS3uuASpe-1LjfG5f14Bnozjwy)

Scikit-learn

* [Série de Tutoriels Scikit-learn de Data School](https://www.youtube.com/watch?v=elojMnjn4kk&list=PL5-da3qGB5ICeMbQuqbbCOQWcS6OYBr5A)

Matplotlib

* [Série Matplotlib de Sentdex](https://www.youtube.com/watch?v=q7Bo_J8x_dw&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF)
* [Tutoriels Vidéo Matplotlib](https://www.youtube.com/watch?v=b3lK639ymu4&list=PLNmACol6lYY5aGQtxghQTq0bHXYoIMORy)

Et si vous êtes bloqué avec un concept ou un extrait de code, googlez-le ! La qualité des réponses sera très variable, mais des sites comme Quora, Stackoverflow ou le forum excellent de PyTorch sont certainement des sources que vous pouvez exploiter. Reddit peut parfois offrir de bonnes explications, dans des formats comme [ELI5](https://www.reddit.com/r/explainlikeimfive/) (Explique-moi comme si j'avais cinq ans) lorsque vous êtes complètement perplexe face à un nouveau sujet.

### **Phase 3 : Créer Quelque Chose**

![Image](https://cdn-media-1.freecodecamp.org/images/0*OkIR1OXNOOSEG8wr)
_[Source de l'image](https://theaijournal.com/2018/05/03/pytorch-for-computer-vision-2-gpu-in-deep-learning-do-you-need-one/" rel="noopener" target="_blank" title=")_

Bien que vous devriez définitivement jouer avec le code et l'utiliser avec des ensembles de données/problèmes externes tout en suivant le cours fast.ai, je pense qu'il est crucial de mettre en œuvre votre propre projet également. Le cours III de deeplearning.ai est un excellent guide sur la façon de structurer et d'exécuter un projet de Machine Learning.

#### **Brainstorming d'Idées**

Commencez par brainstormer des idées qui vous semblent réalisables avec les connaissances que vous venez d'acquérir, regardez les ensembles de données ouvertement disponibles et pensez aux problèmes que vous pourriez vouloir résoudre avec le Deep Learning. Consultez ces [Projets](https://github.com/NirantK/awesome-project-ideas) pour vous inspirer !

#### **Ou Utiliser Kaggle**

Sinon, une façon facile de commencer avec un projet est de participer à une [compétition Kaggle](https://www.kaggle.com/competitions) (actuelle ou passée) ou d'explorer leur vaste quantité d'[ensembles de données ouverts](https://www.kaggle.com/datasets).

Kaggle offre une excellente passerelle vers la communauté ML. Les gens partagent des Kernels (leur marche à suivre pour un problème donné) et discutent activement des idées, ce que vous pouvez apprendre. Cela devient particulièrement intéressant après la fin d'une compétition, lorsque les équipes commencent à publier leurs solutions dans les forums de discussion, ce qui implique souvent des approches créatives de la compétition.

#### **Choisir un Framework**

Quel que soit le Framework de Deep Learning avec lequel vous vous sentez le plus à l'aise, choisissez-en un ! Je choisirais soit PyTorch soit Keras, car ils sont tous deux relativement faciles à apprendre et ont une communauté très active.

#### **Réfléchir**

Après avoir terminé votre projet, prenez un jour ou deux pour réfléchir à ce que vous avez accompli, à ce que vous avez appris et à ce que vous pourriez améliorer à l'avenir. C'est aussi le moment idéal pour écrire votre premier article de blog ! C'est une chose de penser que vous comprenez quelque chose et une autre de le transmettre aux autres.

Quincy Larson, le fondateur de FreeCodeCamp, a donné une présentation très utile sur la façon d'écrire un article de blog technique [ici](https://www.youtube.com/watch?v=YODPgBadj80).

### **Phase 4 : Approfondir**

![Image](https://cdn-media-1.freecodecamp.org/images/1*5JBur4NMDjQE7EkXHt4C5w.jpeg)
_Fait Amusant : Les auteurs du réseau Inception original ont utilisé ce meme dans leur article officiel comme source d'inspiration ! | [Source de l'image](https://knowyourmeme.com/memes/we-need-to-go-deeper" rel="noopener" target="_blank" title=")_

Maintenant que vous avez construit quelques connaissances fondamentales en Deep Learning et que vous avez traversé votre première expérience pratique, il est temps d'aller plus loin !

À partir de là, il y a des tonnes de choses que vous pouvez faire. Mais la première chose que je ferais est de suivre la partie 2 de Fast.ai [Cutting Edge Deep Learning For Coders](http://course.fast.ai/part2.html). Comme le nom le suggère, vous apprendrez certaines des choses les plus avancées en Deep Learning : des GANs à la traduction neuronale en passant par la super résolution ! Le cours vous donnera un aperçu de certains des sujets les plus chauds en Deep Learning en ce moment, avec un fort accent sur la vision par ordinateur et le traitement du langage naturel (NLP). J'apprécie particulièrement le cours car Jeremy Howard ne donne pas seulement des explications très claires, mais il entre vraiment dans le code nécessaire pour permettre ces idées.

Après fast.ai, voici quelques-unes des choses que vous pouvez faire :

* Plonger profondément dans un sujet tel que la vision par ordinateur, le NLP ou l'apprentissage par renforcement
* Lire des articles et/ou réimplémenter des idées d'un article
* Faire plus de projets et/ou acquérir de l'expérience de travail en Deep Learning
* Suivre des blogs, écouter des podcasts et rester à jour

#### **Plongées Profondes**

**Vision par Ordinateur**

Le meilleur endroit pour continuer votre parcours en vision par ordinateur est définitivement le cours CS231n de Stanford, également appelé _Convolutional Neural Networks for Visual Recognition_. Ils ont non seulement toutes leurs vidéos de conférences en ligne, mais leur site web offre également des [notes de cours](http://cs231n.github.io/) et des [devoirs](http://cs231n.stanford.edu/2017/syllabus.html) ! Fast.ai Partie 2 et deeplearning.ai vous donneront une bonne base pour le cours, car CS231n ira beaucoup plus loin en termes de théorie derrière les CNNs et les sujets connexes.

Bien que les deux versions couvrent principalement les mêmes sujets, ce qui signifie également _choisissez le style d'enseignement de la version que vous préférez_, les dernières conférences diffèrent légèrement. Par exemple, 2017 incorpore une conférence sur les modèles génératifs et 2016 a une conférence invitée de Jeff Dean sur le Deep Learning chez Google. Si vous voulez voir comment était la vision par ordinateur avant que le Deep Learning ne décolle, l'Université de Floride centrale (UCF) a un cours de vision par ordinateur de 2012 enseignant des concepts tels que les caractéristiques SIFT.

* [Stanford CS231n (2017)](https://www.youtube.com/watch?v=vT1JzLTH4G4&list=PLC1qU-LWwrF64f4QKQT-Vg5Wr4qEE1Zxk)
* [Stanford CS231n (2016)](https://www.youtube.com/watch?v=NfnWJUyUJYU&list=PLkt2uSq6rBVctENoVBg1TpCC7OQi31AlC)
* [UCF Computer Vision (2012](https://www.youtube.com/watch?v=715uLCHt4jE&list=PLd3hlSJsX_ImKP68wfKZJVIPTd8Ie5u-9))

**Traitement du Langage Naturel**

Stanford propose un cours assez complet appelé CS224n _Natural Language Processing with Deep Learning_, qui, de manière similaire à CS231n, a non seulement téléchargé ses vidéos de conférences, mais héberge également un site web pratique avec des [diapositives de conférences, des devoirs, des solutions de devoirs](http://web.stanford.edu/class/cs224n/syllabus.html) et même des [projets de classe des étudiants](http://web.stanford.edu/class/cs224n/reports.html) !

Oxford propose également une série de conférences très intéressante sur le NLP en coopération avec DeepMind. Bien qu'elle dispose d'un [dépôt GitHub](https://github.com/oxford-cs-deepnlp-2017/lectures) utile avec des diapositives et des pointeurs vers des lectures supplémentaires, elle manque de la partie devoirs du CS224 de Stanford. Les cours se chevauchent dans une certaine mesure, mais pas au point qu'il ne vaut pas la peine de regarder les deux cours.

* [Stanford NLP avec Deep Learning (2017)](https://www.youtube.com/watch?v=OQQ-W_63UgQ&list=PL3FW7Lu3i5Jsnh1rnUwq_TcylNr7EkRe6)
* [Oxford Deep Learning pour NLP avec DeepMind (2017)](https://www.youtube.com/watch?v=RP3tZFcC2e8&list=PL613dYIGMXoZBtZhbyiBqb0QtgK6oJbpm)

**Deep Learning Général**

Pour les personnes qui ne sont toujours pas sûres de ce qui les passionne le plus dans le Deep Learning, l'Université Carnegie Mellon (CMU) propose un cours sur les _Topics in Deep Learning_, qui introduit une large gamme de sujets allant des Machines de Boltzmann Restreintes au Deep Reinforcement Learning. Oxford propose également un cours de Deep Learning, qui peut vous donner une compréhension mathématique plus ferme des concepts que vous avez appris dans deeplearning.ai et fast.ai, c'est-à-dire des choses comme la régularisation ou l'optimisation.

Un livre qui pourrait vous aider dans n'importe quel domaine du Deep Learning est _The Deep Learning Book_ de Ian Goodfellow et al., qui est le livre le plus complet sur la théorie du Deep Learning que je connaisse. Des cours comme le cours de NLP d'Oxford utilisent également ce livre comme matériel complémentaire.

Il est également notable que les conférences de recherche de haut niveau comme NIPS ou ICML, qui diffusent les articles de Deep Learning de pointe, publient régulièrement leurs vidéos de discours principaux et de tutoriels.

* [Cours CMU Topics in Deep Learning (2017)](https://www.youtube.com/watch?v=fDlOQrLX8Hs&list=PLpIxOj-HnDsOSL__Buy7_UEVQkyfhHapa)
* [Cours Oxford Deep Learning (2015)](https://www.youtube.com/watch?v=PlhFWT7vAEw&list=PLjK8ddCbDMphIMSXn-w1IjyYpHU3DaUYw)
* [Deep Learning Book par Ian Goodfellow et al.](https://www.deeplearningbook.org/)
* [Vidéos de Conférence NIPS](https://nips.cc/Conferences/2017/Videos) (2017), [ICML](https://icml.cc/Conferences/2017/Videos) (2017), [ICLR](https://www.facebook.com/pg/iclr.cc/videos/) (2018)

**Apprentissage par Renforcement**

Comme l'apprentissage par renforcement (RL) n'est couvert ni par deeplearning.ai ni par fast.ai, je regarderais d'abord l'introduction à RL d'Arxiv Insight et les vidéos RL de Jacob Schrum, qui sont des explications extrêmement compréhensibles du sujet. Ensuite, dirigez-vous vers l'article de blog d'Andrej Karpathy sur le Deep Reinforcement Learning et lisez les chapitres 1-2 de la thèse de doctorat d'Andrew Ng (comme suggéré par le [site web de Berkeley CS 294](http://rll.berkeley.edu/deeprlcoursesp17/#prerequisites)) pour obtenir une introduction aux processus de décision de Markov. Ensuite, le cours de David Silver (Deep Mind) sur RL vous donnera une base solide pour passer au cours CS294 de Berkeley sur le Deep RL.

Alternativement, il existe des sessions enregistrées d'un bootcamp Deep RL à Berkeley et d'une école d'été RL à l'Institut de Montréal pour les algorithmes d'apprentissage avec des intervenants comme Pieter Abbeel et Richard Sutton. Ce dernier a également co-écrit un manuel d'introduction sur RL, qui peut actuellement être consulté ouvertement dans sa 2e édition en tant que brouillon (les chapitres 3 et 4 sont des lectures préalables pour CS294).

De plus, Udacity dispose d'un [dépôt GitHub](https://github.com/udacity/deep-reinforcement-learning) fabuleux avec des tutoriels, des projets et une feuille de triche de leur cours _payant_ Deep RL. Une autre ressource qui a été publiée récemment est le cours en cours de Deep RL de Thomas Simonini, qui est très facile à suivre et pratique dans sa méthodologie de codage.

* [Vidéo d'Introduction à RL d'Arxiv Insight](https://www.youtube.com/watch?v=JgvyzIkgxF0)
* [Introduction à RL de Jacob Schrum](https://www.youtube.com/watch?v=3T5eCou2erg&list=PLWi7UcbOD_0u1eUjmF59XW2TGHWdkHjnS)
* [Article de Blog d'Andrej Karpathy sur le Deep Reinforcement Learning](http://karpathy.github.io/2016/05/31/rl/)
* [Chapitre 1-2 de la Thèse de Doctorat d'Andrew Ng sur les Processus de Décision de Markov](http://rll.berkeley.edu/deeprlcoursesp17/docs/ng-thesis.pdf)
* [Cours de David Silver sur l'Apprentissage par Renforcement](https://www.youtube.com/watch?v=2pWv7GOvuf0&list=PLzuuYNsE1EZAXYR4FJ75jcJseBmo4KQ9-)
* [Cours Berkeley CS294 Deep Reinforcement Learning (2017)](http://rll.berkeley.edu/deeprlcoursesp17/))
* [Berkeley CS294 Deep Reinforcement Learning (2018, session en cours)](http://rail.eecs.berkeley.edu/deeprlcourse/)
* [Reinforcement Learning: An Introduction (Livre Brouillon, 2018)](http://incompleteideas.net/book/bookdraft2018jan1.pdf)
* [Berkeley Deep RL Bootcamp (2017)](https://www.youtube.com/watch?v=qaMdN6LS9rA&list=PLAdk-EyP1ND8MqJEJnSvaoUShrAWYe51U)
* [MILA Reinforcement Learning Summer School (2017)](https://mila.quebec/en/cours/deep-learning-summer-school-2017/))
* [Dépôt GitHub Udacity Deep RL](https://github.com/udacity/deep-reinforcement-learning)
* [Cours Deep RL de Thomas Simonini](https://simoninithomas.github.io/Deep_reinforcement_learning_Course/)

**Machine Learning (qui n'est pas nécessairement du Deep Learning)**

Il y a certainement de la valeur à connaître diverses idées de Machine Learning qui sont venues avant le Deep Learning. Que ce soit la régression logistique ou la détection d'anomalies, le cours classique de Machine Learning d'Andrew Ng est un excellent point de départ. Si vous voulez un cours plus rigoureux mathématiquement, Caltech a un MOOC superbement plus théorique. Le professeur Ng écrit également un livre avec les meilleures pratiques de ML, pour lequel vous pouvez accéder aux premiers chapitres de son brouillon.

* [Cours de Machine Learning d'Andrew Ng (2012)](https://www.coursera.org/learn/machine-learning)
* [Cours de Machine Learning Caltech CS156 (2012)](http://work.caltech.edu/telecourse.html)
* [Livre Machine Learning Yearning par Andrew Ng](http://www.mlyearning.org/)

**Voitures Autonomes**

Les voitures autonomes sont l'un des domaines d'application les plus intéressants pour le Deep Learning. Il est donc assez incroyable que le MIT propose son propre cours sur ce sujet. Le cours vous donnera une vue d'ensemble des introductions à des sujets tels que la perception et la planification de mouvement, ainsi que des informations d'experts de l'industrie comme le co-fondateur d'Aurora.

Si vous êtes davantage intéressé par la partie vision par ordinateur de la conduite autonome, quelques chercheurs de l'ETH Zurich et de l'Institut Max Planck pour les systèmes intelligents ont écrit une étude approfondie sur le sujet. De plus, ICCV a téléchargé les diapositives d'une série de tutoriels en 8 parties, qui contiennent des informations utiles sur la fusion de capteurs et la localisation.

En ce qui concerne les projets, je jetterais un coup d'œil aux projets du nanodiplôme _payant_ de voiture autonome d'Udacity, que vous pouvez trouver _librement_ sur GitHub. Udacity offre régulièrement des bourses. Par exemple, [l'année dernière](https://www.udacity.com/scholarships/lyft) en coopération avec Lyft pour son cours d'introduction aux voitures autonomes. Donc, soyez à l'affût de cela également !

* [Cours MIT Self-Driving Cars (2018)](https://www.youtube.com/watch?v=-6INDaLcuJY&list=PLrAXtmErZgOeiKm4sgNOknGvNjby9efdf)
* [Computer Vision for Autonomous Vehicles: Problems, Datasets and State-of-the-Art (2017)](https://arxiv.org/pdf/1704.05519.pdf)
* [Tutoriel ICCV sur la Vision par Ordinateur pour la Conduite Autonome (2015)](https://sites.google.com/site/cvadtutorial15/materials)
* [Idées de Projets de Voiture Autonome d'Udacity](https://github.com/ndrplz/self-driving-car)

#### **Renforcer votre compréhension des concepts fondamentaux**

Vous continuerez à rencontrer des concepts fondamentaux tels que les pertes, les régularisations, les optimiseurs, les fonctions d'activation et la descente de gradient, donc acquérir une intuition pour eux est crucial. Deux articles qui expliquent très bien la descente de gradient et la rétropropagation :

* [Article de Blog de Sebastian Ruder sur la Descente de Gradient](http://ruder.io/optimizing-gradient-descent/)
* [Rétropropagation CS231n](http://cs231n.github.io/optimization-2/)

**Lire des Articles**

Bien qu'Arxiv soit d'une importance primordiale dans la diffusion rapide et ouverte des idées de recherche en Deep Learning, cela peut devenir écrasant très rapidement avec l'afflux d'articles sur la plateforme.

Pour cette raison, Andrej Karpathy a construit [_Arxiv Sanity_](http://www.arxiv-sanity.com/), un outil qui vous permet de filtrer et de suivre les articles selon vos préférences.

Voici quelques articles séminales des dernières années, commençant par les articles ImageNet (AlexNet, VGG, InceptionNet, ResNet) qui ont eu une influence énorme sur la trajectoire du Deep Learning.

* [AlexNet](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf) (2012), [VGG](https://arxiv.org/abs/1409.1556) (2014), [InceptionNet](https://arxiv.org/pdf/1409.4842.pdf) (2014), [ResNet](https://arxiv.org/abs/1512.03385) (2015)
* [Réseaux Antagonistes Génératifs (2014)](https://arxiv.org/abs/1406.2661)
* [Article Yolo sur la Détection d'Objets (2015)](https://arxiv.org/abs/1506.02640)
* [Jouer à Atari avec l'Apprentissage par Renforcement Profond (2013)](https://arxiv.org/pdf/1312.5602.pdf)

![Image](https://cdn-media-1.freecodecamp.org/images/1*ukSvzmeK1f2H9NiWp3Isrw.png)
_Architecture Originale du Réseau InceptionNet | [Source de l'image](http://joelouismarino.github.io/images/blog_images/blog_googlenet_keras/googlenet_diagram.png" rel="noopener" target="_blank" title=")_

**Chaînes YouTube**

_Arxiv Insights_, _CodeEmperium_ et _Yannic Kilcher_ sont les chaînes YouTube les plus sous-estimées sur le Deep Learning avec certaines des explications les plus claires sur les autoencodeurs et l'attention.

Une autre chaîne YouTube qui mérite d'être mentionnée est _Lex Fridman_, qui est l'instructeur principal du cours de voitures autonomes du MIT. Il a également enseigné le cours du MIT sur l'intelligence générale artificielle, qui comprend des conférences fascinantes sur le méta-apprentissage, la conscience et l'intelligence.

Et enfin, aucune liste YouTube ne pourrait omettre _Siraj Rival_. Certains le détestent, d'autres l'adorent. Cela dépend vraiment de ce que vous préférez et de ce que vous voulez tirer de telles vidéos. Pour moi, je ne suis pas très compatible avec sa façon d'enseigner, mais j'apprécie la variété de contenu qu'il publie et la valeur de divertissement qu'il fournit.

* [Arxiv Insights](https://www.youtube.com/channel/UCNIkB2IeJ-6AmZv7bQ1oBYg/videos)
* [CodeEmperium](https://www.youtube.com/channel/UC5_6ZD6s8klmMu9TXEB_1IA/videos)
* [Yannic Kilcher](https://www.youtube.com/channel/UCZHmQk67mSJgfCCTn7xBfew/videos)
* [Lex Fridman](https://www.youtube.com/user/lexfridman)
* [Siraj Rival](https://www.youtube.com/channel/UCWN3xxRkmTPmbKwht9FuE5A/featured)

**Podcasts**

Les podcasts sont un excellent moyen d'entendre diverses personnes sur une grande variété de sujets. Deux de mes podcasts préférés, qui produisent beaucoup de contenu lié au Deep Learning, sont _Talking Machines_ et _This Week in ML & AI_ (TWiML&AI). Par exemple, écoutez le récent [podcast](https://www.thetalkingmachines.com/episodes/icml-2018-jennifer-dy) de Talking Machine à l'ICML 2018 ou le [podcast](https://twimlai.com/twiml-talk-176-openai-five-with-christy-dennison/) de TWiML avec Christy Dennison d'OpenAI Five !

* [Talking Machines](https://www.thetalkingmachines.com/)
* [This Week in ML & AI](https://twimlai.com/)

[**OpenAI Five avec Christy Dennison - TWiML Talk #176**](https://twimlai.com/twiml-talk-176-openai-five-with-christy-dennison/)  
[_Aujourd'hui, nous sommes rejoints par Christy Dennison, ingénieure en Machine Learning chez OpenAI. Depuis qu'elle a rejoint OpenAI plus tôt cette année..._twimlai.com](https://twimlai.com/twiml-talk-176-openai-five-with-christy-dennison/)

**Blogs**

Comme mentionné précédemment, je suis un grand fan de _Distill.pub_, et l'un de ses éditeurs, _Chris Olah_, a également d'autres articles de haute qualité sur son blog personnel.

Un autre blog vraiment prometteur est _The Gradient_, qui fournit des aperçus bien écrits et clairs des dernières découvertes de recherche ainsi que des perspectives sur l'avenir du domaine. Sebastian Ruder est l'un des auteurs contributeurs de The Gradient et, comme Chris Olah, son blog contient également du contenu génial, en particulier pour les sujets liés au NLP. Le dernier blog n'est pas vraiment un blog, mais plutôt un hub pour les plans d'étude de papiers spécifiques tels que AlphaGo Zero ou InfoGans.

Pour chacun de ces sujets, _Depth First Learning_ publie des programmes qui vous permettent d'apprendre les idées des papiers à leur cœur.

* [Distill.pub](https://distill.pub/)
* [Chris Olah](http://colah.github.io/)
* [The Gradient](https://thegradient.pub/)
* [Sebastian Ruder](http://ruder.io/#open)
* [Depth First Learning](http://www.depthfirstlearning.com/)

#### **Demandes de Recherche**

Au cas où vous souhaiteriez commencer vos propres recherches, voici quelques pointeurs vers des sujets que d'autres personnes ont demandés pour la recherche.

* [Sebastian Ruder NLP](http://ruder.io/requests-for-research/)
* [OpenAI Reinforcement Learning](https://blog.openai.com/requests-for-research-2/)
* [AI Open Network](https://ai-on.org/)

#### **Rester à Jour**

Croyez-le ou non, mais l'un des meilleurs moyens de rester informé des progrès du Deep Learning est Twitter. Des tonnes de chercheurs utilisent la plateforme pour partager leurs publications, discuter d'idées et interagir avec la communauté.

Certaines des personnes à suivre sur Twitter :

* [hardmaru](https://twitter.com/hardmaru)
* [Jeremy Howard](https://twitter.com/jeremyphoward)
* [Rachel Thomas](https://twitter.com/math_rachel)
* [Sebastian Ruder](https://twitter.com/seb_ruder)
* [Fei Fei Li](https://twitter.com/drfeifei)
* [Smerity](https://twitter.com/Smerity)
* [François Chollet](https://twitter.com/fchollet)

### **Phase X : Continuer à Apprendre**

Le domaine évolue rapidement, alors continuez à apprendre et profitez du voyage.

#### **Dépôt GitHub**

Puisque le guide ci-dessus est un instantané des ressources que j'aime à l'instant, il changera et évoluera sûrement au cours des prochaines années. Donc, pour mettre à jour ce guide à l'avenir avec de meilleures informations et plus de retours d'autres personnes, j'ai créé [ce dépôt GitHub](https://github.com/sannykim/deep-learning-guide), que je vais essayer de maintenir régulièrement.

N'hésitez pas à contribuer au guide et à envoyer des pull requests !