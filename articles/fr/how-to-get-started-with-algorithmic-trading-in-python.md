---
title: Comment commencer avec le trading algorithmique en Python
subtitle: ''
author: Harshit Tyagi
co_authors: []
series: null
date: '2021-01-04T17:56:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-algorithmic-trading-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/Fashion-Beauty-Lifestyle-Youtube-Channel-Art--2-.png
tags:
- name: Advanced Mathematics
  slug: advanced-mathematics
- name: data analysis
  slug: data-analysis
- name: Data Science
  slug: data-science
- name: Python
  slug: python
seo_title: Comment commencer avec le trading algorithmique en Python
seo_desc: 'When I was working as a Systems Development Engineer at an Investment Management
  firm, I learned that to succeed in quantitative finance you need to be good with
  mathematics, programming, and data analysis.

  Algorithmic or Quantitative trading can be ...'
---

Lorsque je travaillais en tant qu'ingénieur en développement de systèmes dans une société de gestion d'investissements, j'ai appris que pour réussir en finance quantitative, il faut être bon en mathématiques, en programmation et en analyse de données.

Le [trading algorithmique ou quantitatif](https://www.freecodecamp.org/news/algorithmic-trading-in-python/) peut être défini comme le processus de conception et de développement de stratégies de trading statistiques et mathématiques. C'est un domaine extrêmement sophistiqué de la finance.

**Alors, la question est : comment commencer avec le trading algorithmique ?**

Je vais vous guider à travers cinq sujets essentiels que vous devriez étudier afin de vous frayez un chemin dans ce monde fascinant du trading.

Je préfère personnellement Python car il offre le bon degré de personnalisation, de facilité et de rapidité de développement, de frameworks de test, et de vitesse d'exécution. Pour cette raison, tous ces sujets sont axés sur [**Python pour le Trading**](https://medium.com/datadriveninvestor/getting-starting-with-algorithmic-trading-with-python-1ae169cc1705).

## 1. Apprendre la [Programmation Python](https://www.freecodecamp.org/learn/)

Afin d'avoir une carrière florissante en science des données en général, vous avez besoin de solides fondamentaux. Quel que soit le langage que vous choisissez, vous devez comprendre en profondeur certains sujets dans ce langage.

Voici ce que vous devriez chercher à maîtriser dans l'écosystème Python pour la science des données :

* [**Configuration de l'environnement**](https://towardsdatascience.com/ideal-python-environment-setup-for-data-science-cdb03a447de8) — cela inclut la création d'un environnement virtuel, l'installation des packages requis, et le [travail avec les notebooks Jupyter](https://towardsdatascience.com/the-complete-guide-to-jupyter-notebooks-for-data-science-8ff3591f69a4) ou Google Colabs.

* **Structures de données** — certaines des structures de données pythoniques les plus importantes sont les listes, les dictionnaires, les tableaux NumPy, les tuples et les ensembles. J'ai rassemblé [quelques exemples](https://medium.com/p/python-fundamentals-for-data-science-6c7f9901e1c8) dans l'article lié pour que vous appreniez ceux-ci.

* **Programmation Orientée Objet** — En tant qu'analyste quantitatif, vous devez vous assurer que vous êtes bon pour écrire du code bien structuré avec des classes correctement définies. Vous devez apprendre à utiliser des objets et leurs méthodes tout en utilisant des packages externes comme Pandas, NumPy, SciPy, et ainsi de suite.

Le programme de freeCodeCamp propose également une certification en [Analyse de Données avec Python](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-course/) pour vous aider à commencer avec les bases.

## Apprendre à analyser des données financières

L'analyse de données est une partie cruciale de la finance. En plus d'apprendre à manipuler des dataframes avec Pandas, il y a quelques sujets spécifiques auxquels vous devriez prêter attention lors de la manipulation de données de trading.

### Comment explorer les données en utilisant Pandas

L'un des packages les plus importants de la stack Python pour la science des données est sans aucun doute Pandas. Vous pouvez accomplir presque toutes les tâches majeures en utilisant les fonctions définies dans le package.

Concentrez-vous sur la création de dataframes, le filtrage (`loc`, `iloc`, `query`), les statistiques descriptives (résumé), les jointures/merges, le regroupement et la sous-sélection.

### Comment traiter les données de séries temporelles

Les données de trading concernent toutes l'analyse des séries temporelles. Vous devez apprendre à rééchantillonner ou réindexer les données pour changer la fréquence des données, de minutes en heures ou des données OHLC de fin de journée en données de fin de semaine.

Par exemple, vous pouvez convertir des séries temporelles de 1 minute en données de séries temporelles de 3 minutes en utilisant la fonction resample :

```python
df_3min = df_1min.resample('3Min', label='left').agg({'OPEN': 'first', 'HIGH': 'max', 'LOW': 'min', 'CLOSE': 'last'})
```

## 3. Comment écrire des algorithmes de trading fondamentaux

Une carrière en finance quantitative nécessite une solide compréhension des tests d'hypothèses statistiques et des mathématiques. Une bonne maîtrise des concepts tels que le calcul multivarié, l'algèbre linéaire, la théorie des probabilités vous aidera à poser de bonnes bases pour la conception et l'écriture d'algorithmes.

Vous pouvez commencer par calculer des moyennes mobiles sur les données de prix des actions, écrire des stratégies algorithmiques simples comme le croisement de moyennes mobiles ou la stratégie de retour à la moyenne, et apprendre le trading basé sur la force relative.

Après avoir fait ce petit mais significatif saut de pratique et de compréhension du fonctionnement des algorithmes statistiques de base, vous pouvez vous pencher sur les domaines plus sophistiqués des techniques d'apprentissage automatique. Ceux-ci nécessitent une compréhension plus approfondie des statistiques et des mathématiques.

Voici deux livres avec lesquels vous pouvez commencer :

* [Quantitative Trading: How to build your own Algorithmic Trading Business](http://www.amazon.com/gp/product/0470284889/ref=as_li_tf_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0470284889&linkCode=as2&tag=quant0f-20) — Par Dr. Ernest Chan

* Livre sur [Algorithmic Trading and DMA](http://www.amazon.com/gp/product/0956399207/ref=as_li_tf_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0956399207&linkCode=as2&tag=quant0f-20) — Par Barry Johnson

Et voici quelques cours qui vous aideront à commencer avec Python pour le Trading et qui couvrent la plupart des sujets que j'ai abordés ici :

* [Python for Trading par Multi Commodity Exchange proposé par Quantra](https://quantra.quantinsti.com/course/python-for-trading?utm_source=harshit_tyagi&utm_medium=affiliate&utm_campaign=python_finance_article)

* [Algorithmic Trading with Python](https://www.freecodecamp.org/news/algorithmic-trading-using-python-course/) — un cours gratuit de 4 heures de Nick McCullum sur la chaîne YouTube freeCodeCamp

Vous pouvez obtenir 10 % de réduction sur le cours Quantra en utilisant mon code **HARSHIT10**.

## 4. Apprendre le Backtesting

Une fois que vous avez terminé de coder votre stratégie de trading, vous ne pouvez pas simplement la tester sur le marché en direct avec un capital réel, n'est-ce pas ?

L'étape suivante consiste à exposer cette stratégie à un flux de données de trading historiques, ce qui générerait des signaux de trading. Les transactions effectuées accumuleraient alors un profit ou une perte (P&L) associé, et l'accumulation de toutes les transactions vous donnerait le P&L total. Cela s'appelle le backtesting.

Le backtesting nécessite que vous soyez bien versé dans de nombreux domaines, comme les mathématiques, les statistiques, l'ingénierie logicielle et la microstructure du marché. Voici quelques concepts que vous devriez apprendre pour avoir une compréhension décente du backtesting :

* Vous pouvez commencer par comprendre les indicateurs techniques. Explorez le package Python appelé TA_Lib pour utiliser ces indicateurs.

* Employez des indicateurs de momentum comme le SAR parabolique, et essayez de calculer le coût de transaction et le glissement.

* Apprenez à tracer les rendements cumulés de la stratégie et étudiez la performance globale de la stratégie.

* Un concept très important qui affecte la performance du backtest est le biais. Vous devriez apprendre sur le biais d'optimisation, le biais de prévision, la tolérance psychologique et le biais de survivance.

## 5. Métriques de performance — Comment évaluer les stratégies de trading

Il est important pour vous de pouvoir expliquer votre stratégie de manière concise. Si vous ne comprenez pas votre stratégie, il y a des chances que, lors de toute modification externe de la réglementation ou de changement de régime, votre stratégie commence à se comporter anormalement.

Une fois que vous comprenez la stratégie avec confiance, les métriques de performance suivantes peuvent vous aider à apprendre à quel point la stratégie est bonne ou mauvaise :

* **Ratio de Sharpe** — caractérise de manière heuristique le ratio risque/récompense de la stratégie. Il quantifie le rendement que vous pouvez accumuler pour le niveau de volatilité subi par la courbe de capital.

* **Volatilité** — quantifie le « risque » lié à la stratégie. Le ratio de Sharpe incarne également cette caractéristique. Une volatilité plus élevée d'un actif sous-jacent conduit souvent à un risque plus élevé dans la courbe de capital et cela se traduit par des ratios de Sharpe plus petits.

* **Drawdown Maximum** — la plus grande baisse en pourcentage globale de pic à creux sur la courbe de capital de la stratégie. Les drawdowns maximum sont souvent étudiés en conjonction avec les stratégies de momentum car elles en souffrent. Apprenez à le calculer en utilisant la bibliothèque `numpy`.

* **Capacité/Liquidité** — détermine la scalabilité de la stratégie pour un capital supplémentaire. De nombreux fonds et sociétés de gestion d'investissements souffrent de ces problèmes de capacité lorsque les stratégies augmentent en allocation de capital.

* **TCAC** — mesure le taux de croissance moyen d'une stratégie sur une période de temps. Il est calculé par la formule : (rendements cumulés de la stratégie)^(252/nombre de jours de trading) — 1

## Ressources supplémentaires

Cet article a servi de programme suggéré pour vous aider à commencer avec le trading algorithmique. C'est une bonne liste de concepts à maîtriser.

Maintenant, la question est : quelles ressources peuvent vous aider à vous mettre à niveau avec ces sujets ?

Voici quelques livres classiques et cours utiles avec des devoirs et des exercices que j'ai trouvés utiles :

* **[Cours]** [Cours Python pour le Trading par Multi Commodity Exchange proposé par Quantra](https://quantra.quantinsti.com/course/python-for-trading?utm_source=harshit_tyagi&utm_medium=affiliate&utm_campaign=python_finance_article) **[Code Promo : HARSHIT10]**

* **[Livre]** [Quantitative Trading: How to Build Your Own Algorithmic Trading Business](http://www.amazon.com/gp/product/0470284889/ref=as_li_tf_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0470284889&linkCode=as2&tag=quant0f-20) — Ernest Chan

* **[Cours]** [Cours de trading du Dr. Ernest Chan sur la plateforme Quantra](https://quantra.quantinsti.com/courses?utm_source=harshit_tyagi&utm_medium=affiliate&utm_campaign=python_finance_article)

* **[Livre]** [Python for Finance — Yves Hilpisch](https://www.amazon.in/Python-Finance-Yves-Hilpisch/dp/1491945281)

* **[Revues]** : [arXiv](http://arxiv.org/archive/q-fin), [Mathematical finance de Wiley](http://onlinelibrary.wiley.com/journal/10.1111/%28ISSN%291467-9965), [computational finance](http://www.risk.net/type/journal/source/journal-of-computational-finance).

### [Data Science avec Harshit](https://www.youtube.com/c/DataSciencewithHarshit?sub_confirmation=1)

%[https://www.youtube.com/watch?v=yapSsspJzAw&t]

Avec cette chaîne, je prévois de lancer quelques [séries couvrant tout l'espace de la science des données](https://towardsdatascience.com/hitchhikers-guide-to-learning-data-science-2cc3d963b1a2?source=---------8------------------). Voici pourquoi vous devriez vous abonner à la [chaîne](https://www.youtube.com/channel/UCH-xwLTKQaABNs2QmGxK2bQ) :

* Cette série couvrira tous les tutoriels de qualité requis/demandés sur chacun des sujets et sous-sujets comme les [Fondamentaux de Python pour la Science des Données](https://towardsdatascience.com/python-fundamentals-for-data-science-6c7f9901e1c8?source=---------5------------------).

* [Mathématiques et dérivations](https://towardsdatascience.com/practical-reasons-to-learn-mathematics-for-data-science-1f6caec161ea?source=---------9------------------) expliquées sur pourquoi nous faisons ce que nous faisons en ML et Deep Learning.

* [Podcasts avec des Data Scientists et Ingénieurs](https://www.youtube.com/watch?v=a2pkZCleJwM&t=2s) chez Google, Microsoft, Amazon, etc., et PDG de grandes entreprises axées sur les données.

* [Projets et instructions](https://towardsdatascience.com/building-covid-19-analysis-dashboard-using-python-and-voila-ee091f65dcbb?source=---------2------------------) pour mettre en œuvre les sujets appris jusqu'à présent. Apprenez les nouvelles certifications, Bootcamp, et ressources pour réussir ces certifications comme cet [Examen de Certification Développeur TensorFlow par Google](https://youtu.be/yapSsspJzAw).

Si ce tutoriel vous a été utile, vous devriez consulter mes cours de science des données et d'apprentissage automatique sur [Wiplane Academy](https://www.wiplane.com/). Ils sont complets mais compacts et vous aident à construire une solide fondation de travail à présenter.