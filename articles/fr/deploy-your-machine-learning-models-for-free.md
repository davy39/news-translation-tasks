---
title: Comment déployer gratuitement un modèle de Machine Learning – 7 plateformes
  cloud de déploiement de modèles ML
date: '2021-02-11T16:17:37.000Z'
author: freeCodeCamp
authorURL: https://www.freecodecamp.org/news/author/davis/
originalURL: https://freecodecamp.org/news/deploy-your-machine-learning-models-for-free
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/pexels-christina-morillo-1181341.jpg
tags:
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
seo_desc: "By Davis David\nI remember the first time I created a simple machine learning\
  \ model. It was a model that could predict your salary according to your years of\
  \ experience. And after making it, I was curious about how I could deploy it into\
  \ production. \n..."
---


Je me souviens de la première fois où j'ai créé un modèle simple de Machine Learning. C'était un modèle capable de prédire votre salaire en fonction de vos années d'expérience. Après l'avoir conçu, j'étais curieux de savoir comment je pouvais le déployer en production.

<!-- more -->

Si vous apprenez le Machine Learning, vous avez peut-être déjà rencontré ce défi dans des tutoriels en ligne ou des livres. Vous pouvez trouver `le code source ici`[1] si cela vous intéresse.

Il m'a été très difficile de déterminer où je pouvais déployer mon modèle. J'ai essayé de le déployer sur une plateforme d'hébergement web, mais il était ardu de configurer et d'exécuter l'application Flask qui servait mon modèle.

![man-5723449_1920](https://www.freecodecamp.org/news/content/images/2021/02/man-5723449_1920.jpg)

J'ai alors décidé d'explorer différentes plateformes spécifiquement créées pour le déploiement de modèles de Machine Learning (ou disposant d'un environnement adapté pour supporter ma stack de modèles).

> Ce n'est que lorsqu'un modèle est pleinement intégré aux systèmes de l'entreprise que nous pouvons extraire une réelle valeur de ses prédictions. - Christopher Samiullah

Dans cet article, vous découvrirez différentes plateformes qui peuvent vous aider à déployer vos modèles de Machine Learning en production (gratuitement) et à les rendre utiles.

J'ai également inclus d'excellentes ressources pour vous aider à commencer le déploiement de votre modèle sur une plateforme spécifique.

**Note :** Les plateformes mentionnées dans cet article proposent des forfaits **free tier** (niveau gratuit) qui vous permettent d'utiliser leurs produits ou services jusqu'à une **limite d'utilisation gratuite** spécifiée. Si vous souhaitez obtenir des services illimités, vous serez facturé selon la tarification du service.

## À qui s'adresse cet article ?

Cet article s'adresse à ceux qui ont créé un modèle de Machine Learning sur une machine locale et souhaitent explorer les plateformes potentielles pour déployer ce modèle.

Il s'adresse également à ceux qui recherchent une plateforme alternative pour déployer leurs modèles de Machine Learning.

C'est parti ! 🚀

## Option de déploiement de modèle de Machine Learning n°1 : Algorithmia

[Algorithmia][2] est un outil de MLOps (machine learning operations) fondé par [Diego Oppenheimer][3] et [Kenny Daniel][4] qui offre un moyen simple et rapide de déployer votre modèle de Machine Learning en production.

![Algorithmia](https://www.freecodecamp.org/news/content/images/2021/02/Algorithmia.png)

Algorithmia 

Algorithmia se spécialise dans les **"algorithmes en tant que service"** (algorithms as a service). Il permet aux utilisateurs de créer des extraits de code qui exécutent le modèle ML, puis de les héberger sur Algorithmia. Vous pouvez ensuite appeler votre code via une API.

Désormais, votre modèle peut être utilisé pour différentes applications de votre choix, telles que des applications web, des applications mobiles ou du e-commerce, par un simple appel API depuis Algorithmia.

![supported-programming-languages](https://www.freecodecamp.org/news/content/images/2021/02/supported-programming-languages.PNG)

Langages de programmation supportés

L'avantage d'Algorithmia est qu'il sépare les problématiques de Machine Learning du reste de votre application. Dans ce cas, vous devez appeler votre modèle et obtenir des prédictions via un appel API. Votre application sera ainsi libérée des contraintes liées à l'environnement de Machine Learning.

Voici une excellente ressource pour en savoir plus sur Algorithmia :

- [Comment déployer votre modèle NLP en production sous forme d'API avec Algorithmia][5]

## Option de déploiement de modèle de Machine Learning n°2 : PythonAnywhere

PythonAnywhere est une autre plateforme en tant que service (PaaS) bien connue et en pleine croissance, basée sur le langage de programmation Python. Elle facilite l'exécution de programmes Python dans le cloud et offre un moyen simple d'héberger vos applications web basées sur Python.

![pythonAnywhere](https://www.freecodecamp.org/news/content/images/2021/02/pythonAnywhere.PNG)

PythonAnywhere

Vous pouvez utiliser n'importe quel framework web Python comme Flask pour déployer votre modèle de Machine Learning et l'exécuter sur la plateforme PythonAnywhere en quelques minutes seulement.

Gardez à l'esprit que PythonAnywhere ne supporte pas les GPU. Si vous avez un modèle de Deep Learning reposant sur CUDA et GPU, vous devrez trouver un serveur adapté pour répondre aux exigences de votre modèle (consultez les plateformes suivantes).

Voici des ressources pour apprendre à exécuter votre modèle de Machine Learning sur PythonAnywhere :

- [Déployer des modèles de Machine Learning gratuitement][6]
- [Comment déployer et héberger un modèle de Machine Learning][7]

## Option de déploiement de modèle de Machine Learning n°3 : Heroku

Heroku est une plateforme cloud en tant que service (PaaS) qui aide les développeurs à déployer, gérer et mettre à l'échelle rapidement des applications modernes sans les tracas liés à l'infrastructure.

![1_H_nSB0PYTzIxnG9GhNU5vg](https://www.freecodecamp.org/news/content/images/2021/02/1_H_nSB0PYTzIxnG9GhNU5vg.jpeg)

Heroku 

Si vous souhaitez déployer votre modèle pour la première fois, je vous recommande d'essayer Heroku car il est flexible et facile à utiliser.

Il offre une large gamme de services et d'outils pour accélérer votre développement et vous évite de tout recommencer à zéro. Il supporte également plusieurs langages de programmation largement utilisés comme Python, Java, PHP, Node, Go, Ruby, Scala et Clojure.

L'avantage de Heroku est qu'il facilite la création, le déploiement et la gestion de votre application. Vous pouvez le faire directement depuis la ligne de commande en utilisant la [Heroku CLI][8] (disponible pour les utilisateurs Windows, Linux et Mac).

Concernant le déploiement, vous pouvez uploader votre modèle de Machine Learning entraîné et votre code source sur Heroku en liant votre dépôt GitHub à votre compte Heroku.

Voici des ressources pour apprendre à déployer votre modèle sur la plateforme Heroku :

- [Comment développer un projet de Machine Learning de bout en bout et le déployer sur Heroku avec Flask][9]
- [Créer et déployer votre première application Flask en utilisant Python et Heroku][10]

> "Comme le rapporte [VentureBeat][11], environ 90 % des modèles de Machine Learning ne parviennent jamais en production. En d'autres termes, seul un jour de travail sur dix d'un data scientist finit par produire quelque chose d'utile pour l'entreprise." - Rhea Moutafis

## Option de déploiement de modèle de Machine Learning n°4 : Google Cloud Platform

Google Cloud Platform (GCP) est une plateforme proposée par Google qui fournit une série de services de cloud computing tels que le calcul (Compute), le stockage et les bases de données (Storage and Database), l'Intelligence Artificielle (AI) / le Machine Learning (ML), le réseau, le Big Data, ainsi que l'identité et la sécurité.

![gcp](https://www.freecodecamp.org/news/content/images/2021/02/gcp.png)

Google Cloud

Google Cloud Platform propose des environnements d'infrastructure en tant que service (IaaS), de plateforme en tant que service (PaaS) et de calcul serverless.

Google Cloud offre 300 $ de crédit gratuit sur 12 mois, mais vous devrez ajouter les détails de votre carte de crédit pour vérifier que vous n'êtes pas un robot. La plateforme ne vous facturera pas tant que vous ne déciderez pas de passer à un compte payant.

Google Cloud Platform propose trois façons de déployer votre modèle de Machine Learning.

### Google AI Platform

Google AI Platform fournit des services complets de Machine Learning. Les Data Scientists et les ingénieurs en Machine Learning peuvent utiliser cette plateforme pour travailler plus efficacement sur des projets de Machine Learning, de l'idéation au déploiement.

![google-AI-platform](https://www.freecodecamp.org/news/content/images/2021/02/google-AI-platform.png)

Services de Google Cloud AI Platform

Avec Google AI Platform, vous aurez accès à toutes ses ressources sous un même toit. Cela inclut la préparation des données, l'entraînement des modèles, le réglage des paramètres, le déploiement des modèles et le partage des modèles de Machine Learning avec d'autres développeurs.

Pour en savoir plus sur Google AI Platform, vous pouvez consulter le site web de la plateforme [ici][12].

### Google App Engine

Google App Engine est une plateforme en tant que service (PaaS) fournie par Google qui supporte le développement et l'hébergement de différentes applications web scalables.

![appengine](https://www.freecodecamp.org/news/content/images/2021/02/appengine.png)

Google App Engine

Google App Engine propose une fonctionnalité d'auto-scaling qui alloue automatiquement des ressources afin que votre application web puisse gérer davantage de requêtes.

Il supporte les langages de programmation populaires, notamment Python, PHP, Node.js, Java, Ruby, C# et Go.

Par conséquent, vous pouvez déployer votre modèle sur Google App Engine en utilisant le framework Flask ou tout autre framework que vous connaissez.

Pour en savoir plus, vous pouvez visiter la plateforme [ici][13].

### Google Cloud Functions

Google Cloud Functions est une plateforme de calcul serverless qui propose des fonctions en tant que service (FaaS) pour exécuter votre code sans aucune gestion de serveur.

Tout ce que vous avez à faire est d'écrire un petit bloc de code (fonction) dans n'importe quel langage de programmation supporté, puis de l'héberger sur Google Cloud Functions. Dans ce cas, vous n'avez pas à affronter les difficultés liées à la maintenance de votre propre serveur.

![1_MeXs5Ot8X49Fn1vE_13ukA](https://www.freecodecamp.org/news/content/images/2021/02/1_MeXs5Ot8X49Fn1vE_13ukA.png)

Google Cloud Functions

Toutes les fonctions créées et hébergées sur Google Cloud Functions seront exécutées dans le cloud en cas de besoin. Vous pouvez appeler des fonctions cloud dans votre application en utilisant différents [déclencheurs (triggers)][14]. La méthode la plus courante consiste à utiliser des appels HTTP.

Par conséquent, vous pouvez déployer votre modèle de Machine Learning avec un bloc de code supporté pour l'exécution sur Google Cloud Functions et appeler la requête HTTP pour la prédiction depuis votre application web ou tout autre système.

Voici quelques ressources pour apprendre à déployer votre modèle sur Google Cloud Platform :

- [Comment passer de zéro à héros avec Google Cloud Platform][15]
- [Comment déployer des modèles Fast.ai sur Google Cloud Functions pour les prédictions][16]

## Option de déploiement de modèle de Machine Learning n°6 : Microsoft Azure Functions

Azure Functions est un service cloud serverless fourni par Microsoft Azure sous forme de fonctions en tant que service (FaaS). Azure Functions aide les développeurs à se décharger des tâches de gestion d'infrastructure pour se concentrer sur l'exécution de leurs applications.

![1_I39WMuYsU_2BgGAgAePCuw](https://www.freecodecamp.org/news/content/images/2021/02/1_I39WMuYsU_2BgGAgAePCuw.png)

Microsoft Azure Functions

> "Vous vous concentrez sur les morceaux de code qui comptent le plus pour vous, et Azure Functions s'occupe du reste." [Page Azure Functions][17].

Avec le serverless, vous pouvez écrire un extrait de code qui exécute votre modèle, puis déployer le code et le modèle de Machine Learning sur Azure Functions et l'appeler pour la prédiction sous forme d'API. Azure Functions est similaire à Google Cloud Functions.

Azure Functions supporte différentes fonctions développées en C#, F#, Node.js, Python, PHP, JavaScript, Java 8, PowerShell Core et TypeScript.

Si vous avez un modèle de Machine Learning volumineux, Azure Functions est le bon choix pour vous. Il supporte le déploiement de packages ML de grande taille tels que les frameworks de Deep Learning (TensorFlow et PyTorch).

Voici des ressources pour apprendre à déployer votre modèle dans Azure Functions :

- [Azure Functions pour le ML][18]
- [Déploiement serverless efficace de modèles PyTorch sur Azure][19]

## Option de déploiement de modèle de Machine Learning n°7 : AWS Lambda

AWS Lambda est un service de calcul serverless fourni par Amazon dans le cadre d'Amazon Web Services. AWS Lambda vous aide à exécuter votre code sans gérer l'infrastructure sous-jacente.

![1_w3p_NfmQOrnGEN39pTC38g](https://www.freecodecamp.org/news/content/images/2021/02/1_w3p_NfmQOrnGEN39pTC38g.jpeg)

AWS Lambda

Avec Lambda, vous pouvez uploader votre code dans une image de conteneur ou un fichier zip. Lambda allouera automatiquement la puissance de calcul pour exécuter votre code en fonction des requêtes ou événements entrants, sans que vous n'ayez besoin de configurer quoi que ce soit.

AWS Lambda permet à votre code d'être associé à d'autres ressources AWS telles qu'une table Amazon DynamoDB, un bucket Amazon S3, une notification Amazon SNS et un flux Amazon Kinesis.

Par conséquent, vous pouvez facilement déployer votre modèle de Machine Learning sur AWS Lambda, et vous pouvez y accéder via une API en utilisant Amazon API Gateway.

Vous pouvez écrire des fonctions Lambda dans les langages de programmation supportés suivants : Python, Java, Go, PowerShell, Node.js, Ruby et C#.

![aws-lambda-how-it-works](https://www.freecodecamp.org/news/content/images/2021/02/aws-lambda-how-it-works.png)

Comment fonctionne le déploiement AWS Lambda

AWS Lambda est très peu coûteux car vous ne payez que lorsque vous invoquez la fonction Lambda (c'est-à-dire lorsque vous effectuez des requêtes de prédiction). Cela peut permettre d'économiser beaucoup d'argent par rapport au coût de fonctionnement de conteneurs ou de machines virtuelles.

Si vous souhaitez surveiller les fonctions Lambda que vous avez créées, AWS Lambda le fera pour vous.

AWS Lambda surveillera les métriques en temps réel, notamment les taux d'erreur, le nombre total de requêtes, l'utilisation de la concurrence au niveau de la fonction, la latence et les requêtes limitées (throttled) via Amazon CloudWatch.

Vous pouvez ensuite consulter les statistiques de chaque fonction Lambda en utilisant la console AWS Lambda ou la console Amazon CloudWatch.

Voici quelques ressources pour apprendre à déployer votre modèle dans Azure Functions :

- [Leçons tirées du déploiement de modèles de Machine Learning sur AWS Lambda][20]
- [Déploiement de modèles de Machine Learning en tant qu'APIs serverless][21]
- [Comment déployer des modèles de Deep Learning avec AWS Lambda et TensorFlow][22]

## Et une option bonus de déploiement de modèle de Machine Learning : la bibliothèque m2cgen

J'ai une option bonus pour vous si les plateformes mentionnées ci-dessus ne correspondent pas à vos besoins. Savez-vous qu'il est possible de transformer votre modèle de Machine Learning entraîné dans le langage de programmation de votre choix ?

Oui, vous pouvez convertir votre modèle en utilisant la bibliothèque Python [m2cgen][23] développée par [Bayes' Witnesses][24]. m2cgen (Model 2 Code Generator) est une bibliothèque Python simple qui convertit un modèle de Machine Learning entraîné dans différents langages de programmation.

Elle supporte actuellement 14 langages de programmation différents, dont Go, C#, Python, PHP et JavaScript. La bibliothèque m2cgen supporte les modèles de régression et de classification de scikit-learn et des frameworks de Gradient Boosting tels que XGBoost et LightGBM (Light Gradient Boosting Machine).

Pour en savoir plus sur cette bibliothèque, je vous recommande de lire [mon guide sur m2cgen ici][25]. J'y explique comment utiliser la bibliothèque, puis comment convertir un modèle de Machine Learning entraîné dans trois langages de programmation différents avant d'effectuer une prédiction.

Cette bibliothèque Python vous aidera à déployer votre modèle dans des environnements où vous ne pouvez pas installer votre stack Python pour supporter la prédiction de votre modèle.

## Conclusion

Le déploiement de Machine Learning est l'une des compétences importantes que vous devriez posséder si vous comptez travailler sur des projets de Machine Learning. Les plateformes mentionnées ci-dessus peuvent vous aider à déployer votre modèle et à le rendre utile plutôt que de le garder sur votre machine locale.

**Félicitations** 👏👏**,** vous êtes arrivé à la fin de cet article ! J'espère que vous avez appris quelque chose de nouveau qui vous aidera dans votre carrière.

Si vous avez appris quelque chose de nouveau ou si vous avez apprécié la lecture de cet article, n'hésitez pas à le partager afin que d'autres puissent le voir. D'ici là, rendez-vous dans le prochain post ! Vous pouvez également me retrouver sur Twitter [@Davis\_McDavid][26].

[1]: https://github.com/Davisy/Model-Deployment-by-using-Flask
[2]: https://algorithmia.com/
[3]: https://www.linkedin.com/in/doppenheimer/
[4]: https://www.linkedin.com/in/kennydaniel
[5]: https://www.freecodecamp.org/news/deploy-ml-model-to-production-as-api/
[6]: https://medium.com/analytics-vidhya/how-to-deploy-simple-machine-learning-models-for-free-56cdccc62b8d
[7]: https://medium.com/@kaustuv.kunal/how-to-deploy-and-host-machine-learning-model-de8cfe4de9c5
[8]: https://devcenter.heroku.com/articles/heroku-cli
[9]: https://www.freecodecamp.org/news/end-to-end-machine-learning-project-turorial/
[10]: https://www.kdnuggets.com/2020/09/flask-app-using-python-heroku.html
[11]: https://venturebeat.com/2019/07/19/why-do-87-of-data-science-projects-never-make-it-into-production/
[12]: https://cloud.google.com/ai-platform
[13]: https://cloud.google.com/appengine
[14]: https://cloud.google.com/functions/docs/calling
[15]: https://www.freecodecamp.org/news/google-cloud-platform-from-zero-to-hero/
[16]: https://jianjye.medium.com/how-to-deploy-fast-ai-models-to-google-cloud-functions-for-predictions-e3d73d71546b
[17]: https://docs.microsoft.com/en-us/azure/azure-functions/?WT.mc_id=ignite-event-toanglin
[18]: https://medium.com/microsoftazure/azure-functions-for-ml-4440bee58621
[19]: https://medium.com/pytorch/efficient-serverless-deployment-of-pytorch-models-on-azure-dc9c2b6bfee7
[20]: https://www.freecodecamp.org/news/what-we-learned-by-serving-machine-learning-models-using-aws-lambda-c70b303404a1/
[21]: https://aws.amazon.com/blogs/machine-learning/deploying-machine-learning-models-as-serverless-apis/
[22]: https://aws.amazon.com/blogs/machine-learning/how-to-deploy-deep-learning-models-with-aws-lambda-and-tensorflow/
[23]: https://github.com/BayesWitnesses/m2cgen
[24]: https://github.com/BayesWitnesses
[25]: https://www.freecodecamp.org/news/transform-machine-learning-models-into-native-code-with-zero-dependencies/
[26]: https://twitter.com/Davis_McDavid