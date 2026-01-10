---
title: Une introduction aux outils Microsoft alimentés par l'IA
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-04T18:41:38.000Z'
originalURL: https://freecodecamp.org/news/ai
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/Microsoft-Ai-1.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
seo_title: Une introduction aux outils Microsoft alimentés par l'IA
seo_desc: 'By Pier Paolo Ippolito

  Introduction

  Microsoft is nowadays one of the major providers for AI powered cloud services.
  In fact, according to a RightScale''s survey carried out in 2018, Microsoft Azure
  Cloud services are currently second just to Amazon AW...'
---

Par Pier Paolo Ippolito

## **Introduction**

Microsoft est aujourd'hui l'un des principaux fournisseurs de services cloud alimentés par l'IA. En fait, selon une enquête de RightScale menée en 2018, les services cloud Microsoft Azure sont actuellement deuxièmes, juste derrière Amazon AWS (Figure 1). 

Dans cet article, je vais considérer Microsoft comme une étude de cas, car le PDG de Microsoft, Satya Nadella, a récemment partagé l'intérêt de Microsoft à faire de l'IA une partie vitale de leur entreprise [1]. 

> _"Pour être le leader dans ce domaine, il ne suffit pas d'avoir des capacités d'IA que nous pouvons exercer—il faut aussi la capacité de démocratiser l'IA afin que chaque entreprise puisse vraiment en bénéficier."_                     - Satya Nadella

![Image](https://www.freecodecamp.org/news/content/images/2019/10/stacking-up-cloud-vendors-2018-right-scale-1.png)
_Figure 1 : Principaux fournisseurs de cloud en 2018 [2]_

Je vais maintenant vous présenter certains des différents outils Microsoft qui sont actuellement disponibles et quelques alternatives fournies par la concurrence. Enfin, nous nous concentrerons sur les prochaines étapes en matière de recherche.

## Outils Microsoft AI

Microsoft Azure propose actuellement une large gamme de services qui peuvent être utilisés pour créer toutes sortes de solutions alimentées par l'IA. Certains des plus importants sont : 

* Azure Machine Learning Service
* Azure Machine Learning Studio
* Auto Machine Learning (ML)
* Azure Internet des Objets (IoT)

### Azure Machine Learning Service

Azure Machine Learning vous permet de créer, former et tester des modèles de Machine Learning et de Deep Learning en utilisant les services cloud Microsoft. 

De cette manière, vous n'avez plus à vous soucier des contraintes de mémoire et de puissance de calcul de votre machine locale, car tout le travail est exécuté sur les serveurs Microsoft.

Lors de l'utilisation d'Azure Machine Learning, toutes les principales bibliothèques Python sont préinstallées (par exemple, Tensorflow, PyTorch, scikit-learn), réduisant ainsi le temps de configuration à un minimum. Cela permet aux développeurs de créer rapidement de nouveaux modèles sans aucune contrainte ou configuration environnementale.

### Azure Machine Learning Studio

Azure Machine Learning Studio permet aux utilisateurs d'effectuer des tâches de Machine Learning sans avoir besoin d'expérience en programmation. 

Les modèles de ML sont créés et testés simplement en utilisant une interface visuelle en glissant-déposant tous les composants du modèle (Figure 2). Une fois qu'un modèle est prêt à être déployé dans le monde réel, il peut ensuite être facilement exporté hors de la plateforme Azure ML Studio.

Actuellement, Azure Machine Learning Studio est principalement adapté aux tâches de clustering, de classification et de régression. De plus, si vous le souhaitez, il est possible d'ajouter du code en Python ou R dans Azure Machine Learning Studio pour ajouter plus de fonctionnalités au flux de travail.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/b391e301d2372a1c42bed40506a6ab5e7c072bb3_azure-ml-studio-1.jpg)
_Figure 2 : Classification binaire dans Azure Machine Learning Studio [3]_

### Auto Machine Learning (ML)

L'Automated Machine Learning est actuellement l'un des sujets les plus brulants dans le domaine de l'IA. 

Aujourd'hui, les Data Scientists et les ingénieurs en Machine Learning passent beaucoup de leur temps à essayer d'identifier le meilleur modèle de Machine Learning et les hyper-paramètres à utiliser pour chaque tâche de prédiction différente. 

AutoML vise plutôt à automatiser ce processus en créant des logiciels capables d'identifier et de tester correctement les modèles de Machine Learning (Figure 3).  

![Image](https://www.freecodecamp.org/news/content/images/2019/10/flow2.png)
_Figure 3 : Azure AutoML [4]_

L'Automated Machine Learning est encore un domaine en grand développement et il peut être utilisé dès maintenant (avec des résultats satisfaisants) pour un nombre limité de tâches. 

AutoML peut être actuellement implémenté en utilisant les outils Microsoft, soit avec Azure Machine Learning, soit avec [ML.NET](https://dotnet.microsoft.com/apps/machinelearning-ai/ml-dotnet). Pour le moment, seuls les problèmes de classification et de prévision/régression peuvent être résolus en utilisant les services Microsoft. 

AutoML peut plutôt être implémenté en Python en utilisant des bibliothèques telles que [Auto-sklearn](https://github.com/automl/auto-sklearn), [TPOT](https://github.com/EpistasisLab/tpot) et [H2O](http://docs.h2o.ai/h2o/latest-stable/h2o-docs/automl.html). L'application de l'AutoML dans des domaines comme l'apprentissage non supervisé est actuellement encore en développement.

### Azure Internet des Objets (IoT)

Azure est capable de fournir des solutions à la fois pré-customisées et entièrement personnalisables pour les services IoT (Figure 4). De cette manière, Azure est capable de fournir des solutions pour les débutants et les experts en IoT. 

Microsoft Azure vous permet de mettre facilement à l'échelle les systèmes IoT pour inclure des appareils de différents fabricants et fournit également un support pour les services d'analyse et de Machine Learning.

Si vous cherchez une explication plus détaillée sur la manière dont l'Internet des Objets va changer notre vie et comment il peut être implémenté en utilisant les services cloud, consultez [mon précédent article de blog](https://www.freecodecamp.org/news/introduction-to-iot-internet-of-things/).

![Image](https://www.freecodecamp.org/news/content/images/2019/10/1519855877803.jpg)
_Figure 4 : Flux de travail des appareils IoT [5]_

## Recherche en Intelligence Artificielle

Microsoft démontre maintenant un énorme intérêt pour l'IA. Actuellement, certains de ses services tels que Cortana, Skype ou Office 365 commencent déjà à faire un usage intensif de l'IA. De plus, en 2018 seulement, Microsoft a acquis 5 entreprises d'IA.

Microsoft a également décidé de créer une organisation appelée Microsoft Research AI pour travailler sur les développements futurs des produits d'IA. Certains des principaux sujets actuellement en recherche sont : le biais dans l'IA, l'éthique et l'interprétabilité.

### Biais dans l'IA

Selon [Rich Caruana](https://www.microsoft.com/en-us/research/people/rcaruana/), un chercheur senior chez Microsoft, Microsoft travaille actuellement sur la création d'un outil de détection de biais [6]. 

Chaque modèle de Machine Learning est formé en utilisant certaines données d'entrée. Cependant, parfois, les données d'entrée peuvent contenir une forme de biais qui pourrait compromettre la capacité du modèle à faire des prédictions correctes (par exemple, favoriser une classe par rapport à une autre). Tester un modèle formé en utilisant un outil de détection de biais pourrait donc être d'une grande aide pour minimiser ce risque.

En attendant, d'autres entreprises comme Facebook et IBM travaillent également sur la mise en œuvre d'outils similaires pour leurs entreprises respectives [6, 7]. 

### Éthique

En avril 2019, la Commission européenne a publié une liste de [lignes directrices éthiques pour une IA digne de confiance](https://ec.europa.eu/digital-single-market/en/news/ethics-guidelines-trustworthy-ai). Ces principes, en plus de l'application précédente du [RGPD (Règlement Général sur la Protection des Données)](https://digitalguardian.com/blog/what-gdpr-general-data-protection-regulation-understanding-and-complying-gdpr-data-protection), ont défini un chemin assez clair sur la manière dont les utilisateurs finaux devraient avoir accès à des produits équitables/non biaisés et sur la manière dont leurs données personnelles devraient être protégées. 

De grandes entreprises comme Google, Facebook et Microsoft ont déjà commencé à travailler dans cette direction. Des techniques telles que [Differential Privacy et Federated Learning](https://towardsdatascience.com/ai-differential-privacy-and-federated-learning-523146d46b85) ont été créées afin de protéger la vie privée des utilisateurs dans les applications d'IA.

> "L'Intelligence Artificielle apporte de grandes opportunités, mais aussi de grandes responsabilités. Nous en sommes à ce stade avec l'IA où les choix que nous faisons doivent être fondés sur des principes et une éthique – c'est la meilleure façon de garantir un avenir que nous voulons tous."                                                         - Satya Nadella [8]

### Interprétabilité

L'utilisation de l'IA dans les applications de prise de décision (comme la médecine ou le droit) a récemment suscité certaines préoccupations tant pour les individus que pour les autorités. Cela est dû au fait que, lors de l'utilisation de modèles de Machine Learning complexes ou de réseaux de neurones profonds, il n'est actuellement pas possible (du moins dans une large mesure) de comprendre le processus de prise de décision que l'algorithme effectue lorsqu'il doit accomplir une tâche prédéterminée.

Une solution possible à ce problème est l'IA explicable (XAI). Les principaux objectifs de l'XAI sont de faire en sorte que les machines s'expliquent elles-mêmes et de réduire l'impact des algorithmes biaisés. 

Différents algorithmes ont été implémentés au cours des dernières années afin de rendre les modèles plus explicables. Certains exemples sont : Reversed Time Attention Model (RETAIN), Local Interpretable Model-Agnostic Explanations (LIME) et Layer-wise Relevance Propagation (LRP). Ceux-ci peuvent être implémentés en utilisant des bibliothèques Python telles que ELI5, Skater, SHAP et Microsoft InterpretML.

Si vous êtes intéressé à en savoir plus sur l'IA explicable, vous pouvez trouver plus d'informations [ici](https://towardsdatascience.com/need-for-explainability-in-ai-and-robotics-75dc6077c9fa).

## **Contacts**

Si vous souhaitez rester informé de mes derniers articles et projets, [suivez-moi](https://medium.com/@pierpaoloippolito28?source=post_page---------------------------) et abonnez-vous à ma [liste de diffusion](http://eepurl.com/gwO-Dr?source=post_page---------------------------). Voici quelques-unes de mes coordonnées :

* [Linkedin](https://uk.linkedin.com/in/pier-paolo-ippolito-202917146?source=post_page---------------------------)
* [Blog Personnel](https://pierpaolo28.github.io/blog/?source=post_page---------------------------)
* [Site Web Personnel](https://pierpaolo28.github.io/?source=post_page---------------------------)
* [Profil Medium](https://towardsdatascience.com/@pierpaoloippolito28?source=post_page---------------------------)
* [GitHub](https://github.com/pierpaolo28?source=post_page---------------------------)
* [Kaggle](https://www.kaggle.com/pierpaolo28?source=post_page---------------------------)

[Source de la photo de couverture](https://2s7gjr373w3x22jf92z99mgm5w-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/MS-Research-AI.png).

## Bibliographie

[1] Microsoft CEO Satya Nadella On The Extraordinary Potential Of AI. Forbes, [Bob Evans](https://www.forbes.com/sites/bobevans1/). Consulté à l'adresse : [https://www.forbes.com/sites/bobevans1/2018/06/04/microsoft-ceo-satya-nadella-on-the-extraordinary-potential-of-ai/#3c3c6383162f](https://www.forbes.com/sites/bobevans1/2018/06/04/microsoft-ceo-satya-nadella-on-the-extraordinary-potential-of-ai/#3c3c6383162f)

[2] Top cloud providers 2018: How AWS, Microsoft, Google, IBM, Oracle, Alibaba stack up. ZDNet, [Larry Dignan](https://www.zdnet.com/meet-the-team/us/larry-dignan/). Consulté à l'adresse : [https://www.zdnet.com/article/top-cloud-providers-2018-how-aws-microsoft-google-ibm-oracle-alibaba-stack-up/](https://www.zdnet.com/article/top-cloud-providers-2018-how-aws-microsoft-google-ibm-oracle-alibaba-stack-up/)

[3] Code free Data Science Microsoft Azure Machine Learning. Consulté à l'adresse : [https://gilberttanner-homepage.cdn.prismic.io/gilberttanner-homepage/b391e301d2372a1c42bed40506a6ab5e7c072bb3_azure-ml-studio-1.jpg](https://gilberttanner-homepage.cdn.prismic.io/gilberttanner-homepage/b391e301d2372a1c42bed40506a6ab5e7c072bb3_azure-ml-studio-1.jpg)

[4] Tutorial: Use automated machine learning to predict taxi fares. Microsoft Azure Documentation. Consulté à l'adresse : [https://docs.microsoft.com/en-us/azure/machine-learning/service/tutorial-auto-train-models](https://docs.microsoft.com/en-us/azure/machine-learning/service/tutorial-auto-train-models)

[5] Smart Devices and Analytics Spur Innovation in the Internet of Things. Eric Wetjen, MathWorks. Consulté à l'adresse : [https://www.mathworks.com/company/newsletters/articles/smart-devices-and-analytics-spur-innovation-in-the-internet-of-things.html](https://www.mathworks.com/company/newsletters/articles/smart-devices-and-analytics-spur-innovation-in-the-internet-of-things.html)

[6] Microsoft Creating Tool to Weed Out AI Bias. Dominique Adams, DIGIT. Consulté à l'adresse : [https://digit.fyi/microsoft-ai-bias-detection/](https://digit.fyi/microsoft-ai-bias-detection/)

[7] IBM launches tool aimed at detecting AI bias. Zoe Kleinman, BBC. Consulté à l'adresse : [https://www.bbc.co.uk/news/technology-45561955](https://www.bbc.co.uk/news/technology-45561955)

[8] Guidelines released for ethical and trustworthy AI. [Cornelia Kutterer - Senior Director EU Government Affairs, AI, Privacy & Digital Policies, Microsoft](https://blogs.microsoft.com/eupolicy/author/corneliakutterer/). Consulté à l'adresse : [https://blogs.microsoft.com/eupolicy/2019/04/09/ethical-guidelines-trustworthy-ai/](https://blogs.microsoft.com/eupolicy/2019/04/09/ethical-guidelines-trustworthy-ai/)