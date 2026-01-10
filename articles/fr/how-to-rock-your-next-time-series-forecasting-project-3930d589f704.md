---
title: Comment réussir votre prochain projet de prévision de séries temporelles
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-29T15:43:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-rock-your-next-time-series-forecasting-project-3930d589f704
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UAOHYeh9LCDFdNvAUSHDDg.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Productivity
  slug: productivity
- name: project management
  slug: project-management
- name: technology
  slug: technology
seo_title: Comment réussir votre prochain projet de prévision de séries temporelles
seo_desc: 'By Kirill Dubovikov

  Time series forecasting is a task of great importance. It has a wide variety of
  applications ranging from sales forecasting to anomaly detection in complex manufacturing
  processes.

  Yet, it is quite different from traditional machi...'
---

Par Kirill Dubovikov

La prévision de séries temporelles est une tâche de grande importance. Elle a une large variété d'applications allant de la prévision des ventes à la détection d'anomalies dans des processus de fabrication complexes.

Pourtant, elle est assez différente des méthodes traditionnelles d'apprentissage automatique.

Les projets de prévision ont de nombreuses subtilités dont vous devez être conscient pour réussir la tâche à accomplir. Dans cet article, nous explorerons les points clés qui vous aideront à terminer la tâche avec succès. Lisez la suite pour découvrir ceux que vous pourriez manquer.

### Recherchez vos méthodes

![Image](https://cdn-media-1.freecodecamp.org/images/bAd0qz2jSIO2atDsxIZnx2-8ABNd0QBnMhRy)

Il est crucial d'étudier votre problème en détail et de planifier avant de vous engager dans des actions qui affecteront le succès de votre projet.

#### 1. Étudiez votre théorie

Avant de vous lancer dans un projet de modélisation, assurez-vous de comprendre la théorie si ce n'est pas déjà fait. [Forecasting: Principles and Practice](https://otexts.org/fpp2/) est une ressource très solide qui peut esquisser les bases de manière pratique et concise.

#### 2. Étudiez le domaine

Avant de discuter des détails du projet, assurez-vous de comprendre les bases. Apprenez autant que possible sur le domaine d'activité dans lequel vous allez opérer. Google peut vous aider à commencer. Comprenez les définitions clés et les modèles commerciaux courants. Sans cette étape, vous pourriez finir par faire des mois de travail pour rien. Vous ne voulez pas échouer parce que vous avez résolu un problème qui n'a pas de sens commercial.

#### 3. Étudiez le problème

La première chose à faire dans tout projet de science des données est d'étudier le problème. Et je ne parle pas de discuter avec votre client pendant 15 minutes et d'écrire une compréhension initiale. Vous devriez tout remettre en question et être sceptique (dans le bon sens).

Rappelez-vous que la science des données est un domaine relativement nouveau dans le monde des applications pratiques. Cela signifie que **la vision de votre client peut être incomplète**. Pour les aider, vous devez comprendre leur entreprise et leur problème aussi profondément que possible.

Travaillez avec les exigences, digérez-les mot par mot et ressentez le problème à résoudre. Ensuite, essayez de comprendre l'entreprise derrière le problème.

Est-ce que cela a du sens du point de vue économique ? Quel est l'objectif final de votre client ? Cela peut ne pas être des profits directs, mais il doit y avoir un objectif. Résoudre le problème que votre client vous demande aide-t-il vraiment à atteindre cet objectif ?

Si ce n'est pas le cas, essayez de déterminer ce qui peut être changé avec votre client. N'ayez pas peur de poser des questions — le succès du projet en dépend.

### Trouver les bonnes données

![Image](https://cdn-media-1.freecodecamp.org/images/xdrYcaR9HaaKK5l1eVc2Lb1b1W1fvSg2N2fP)
_Photo par Franki Chamaki sur Unsplash_

À ce stade, nous devrions avoir une bonne compréhension de notre problème et de notre domaine. Ensuite, nous examinerons l'importance de la recherche et de la remise en question des données.

#### 4. Pensez aux métriques et à l'évaluation

Ensuite, vous devriez penser à l'évaluation. Et je ne parle pas de la validation du modèle, mais d'une évaluation qui a du sens pour le client. Souvent, ils ne viendront pas avec une métrique commerciale prête à l'emploi, c'est votre responsabilité de travailler avec eux sur ce point. À la fin, vous devriez avoir une définition mathématique solide de la manière dont vos prévisions affectent l'objectif final du projet.

Et s'il vous plaît, n'essayez pas d'utiliser des métriques de validation conventionnelles en science des données telles que MAPE, MAE, RMSE comme principale métrique du projet. Ce sont de bonnes métriques pour des fins de validation, bien qu'elles puissent encore vous induire en erreur dans un contexte commercial.

Par exemple, prenons que nous avons des données de ventes pour différents articles. Le client nous a demandé d'estimer les ventes futures sur un horizon de deux mois. De plus, elle nous a donné des données historiques sur la stratégie actuelle de prévision des ventes (par exemple, réalisée par des analystes à la main).

Par exemple, votre nouveau modèle d'apprentissage profond détruit la stratégie existante avec une différence de 30 % en MAPE. Vous pourriez le déployer en production et échouer misérablement pour les raisons suivantes :

* Votre modèle **sous-estime** fréquemment par rapport à la stratégie actuelle. L'erreur peut être petite et n'affecter que légèrement le MAPE, mais commercialement, une sous-estimation de 4 % par rapport à leur approche actuelle peut être une catastrophe.
* Votre modèle réduit les ventes excédentaires possibles d'une grande marge. Dans de nombreux cas, cela n'impressionnera pas le client. À la fin, ils peuvent même vous demander d'utiliser l'intervalle de confiance supérieur pour réduire les risques de sous-estimation.
* Le MAPE (métrique choisie) n'a pas de sens pour le client et est difficile à comprendre pour les personnes qui liront le rapport.

Assurez-vous toujours d'avoir une stratégie d'évaluation de modèle solide. C'est votre ceinture de sécurité, et il est préférable d'en avoir une plutôt que de ne pas en avoir, n'est-ce pas ?

#### 5. Regardez vos données

Faites vos devoirs d'analyse exploratoire des données (EDA). Il peut être très tentant de sauter cette partie. "Nous le ferons plus tard, c'est sûr ! Je vais juste regarder comment certains modèles performants." C'est ce que vous pourriez penser. [Mangez vos crapauds en premier](https://www.fastcompany.com/1592454/work-smart-do-your-worst-task-first-or-eat-live-frog-every-morning). Tracez des graphiques, recherchez des valeurs aberrantes, vérifiez les motifs étranges. Si vous avez de nombreuses séries temporelles, regardez leurs sommes si cela a du sens de le faire.

Communiquez toutes les découvertes au client. Si quelque chose dans les données n'est pas compréhensible et clair, cela doit être clarifié dès que possible.

Vous pourriez avoir des bugs dans le code, ou votre framework pourrait avoir des bugs aussi, ou peut-être que le pipeline d'exportation des données du client pourrait également être bogué. Vérifiez double le parsing des dates. Déclarez toujours délibérément le format de date pour votre framework. Par exemple, la bibliothèque pandas de Python peut échouer silencieusement lors du parsing des dates dans différentes locales.

Même si vous ne trouvez aucun bug, votre client pourrait être surpris par vos découvertes. Des motifs saisonniers inhabituels et des découvertes d'anomalies peuvent également fournir une valeur énorme. Votre client pourrait ne pas être conscient de ces éléments car ils n'ont pas regardé les données de la manière dont vous le faites.

#### 6. Regardez vos données À NOUVEAU

Faites plus d'EDA. Je ne peux pas assez insister sur l'importance de cela.

#### 7. Écrivez des tests pour le chargement et le prétraitement des données

Écrivez des tests automatisés pour votre pipeline de données. Les tests vous rendront la pareille et vous feront gagner du temps plus tard.

#### 8. Réfléchissez aux métriques commerciales

Vos métriques commerciales sont-elles définies ? Votre client a-t-il convenu de celles-ci et chaque partie est-elle claire pour eux ? Avez-vous des fonctions pour les calculer implémentées et correctement testées ? Si ce n'est pas le cas, alors il est temps de s'arrêter et de faire cette partie.

Si vous continuez en espérant que le MAPE ou le RMSE suffiront pour une métrique commerciale, vous pourriez vous retrouver dans l'embarras. Cela rendra vos rapports difficiles à comprendre et augmentera vos chances de résoudre la mauvaise tâche.

### La simplicité est la clé

![Image](https://cdn-media-1.freecodecamp.org/images/N9U43H8K8z0a0ULimWe9r9xD2duqeNcpT4BZ)

Enfin, n'oublions pas la simplicité. Les cinq derniers points explorent la valeur derrière les choses simples : des modèles simples, des doubles vérifications et la communication.

#### 9. Commencez par la moyenne

Avant de vous lancer dans le machine learning, vérifiez comment les modèles simples fonctionnent, comme la prédiction de la moyenne. Non, vraiment.

Quelques exemples :

* Prédire la moyenne mobile des dernières N semaines
* Prédire les quantiles mobiles
* Prédire la moyenne mobile exponentielle
* Utiliser des règles heuristiques pour les jours fériés et les événements réguliers. Une moyenne avec un multiplicateur peut faire des merveilles pour le Nouvel An

Cela vous donnera une base solide. Il peut être difficile à croire, mais dans certains cas, vous pourriez même constater que c'est la meilleure solution possible. Pour cette raison exacte, nous avons créé un module entier dédié aux règles heuristiques et aux modèles statistiques simples dans notre framework de prévision.

#### 10. Choisissez le bon modèle

Enfin, la partie amusante. Essayez autant de modèles que vous pouvez vous permettre. Faites un test initial sur une large gamme de modèles, filtrez-les et ajustez les meilleurs.

Méfiez-vous des exigences non fonctionnelles. Mesurez toujours le temps nécessaire pour ajuster le modèle. Votre tâche peut avoir des limitations qui affecteront votre choix :

* Temps d'exécution, surtout si vous avez des dizaines de milliers de séries temporelles pour lesquelles faire des prévisions
* Ressources computationnelles disponibles

#### 11. Mesurez la performance

Calculez vos métriques commerciales et techniques en utilisant la validation croisée des séries temporelles. Utilisez autant de plis que possible pour obtenir des estimations précises. Recherchez vos résultats si vous voyez quelque chose d'inhabituel. Performance extrêmement bonne ? Performance extrêmement mauvaise ? Ce sont souvent des signes d'avertissement.

#### 12. Vérifiez tout à nouveau

Vérifiez-vous. Vérifiez votre client. Écrivez quelques tests si possible.

#### 13. Préparez des rapports et communiquez clairement

Maintenant, il est temps de communiquer et de présenter vos résultats et découvertes. Recherchez les consommateurs de vos résultats. Connaissent-ils le machine learning ou la prévision de séries temporelles ? Sont-ils compétents en informatique ? Si c'est le cas, cette partie peut être facile.

Si ce n'est pas le cas, essayez d'utiliser le moins possible le jargon statistique et de machine learning. Préparez des définitions claires si vous ne pouvez pas vous passer de termes complexes. Utilisez des graphiques avec des titres, des légendes et des noms d'axes. L'objectif final est de communiquer vos résultats aussi clairement que possible. Personne ne pourra utiliser vos résultats s'ils ne les comprennent pas. Et personne ne pourra repérer une erreur si vous vous cachez derrière des descriptions complexes et des formules cryptiques.

### Conseils généraux pour le déroulement de l'ensemble du projet

* Communiquez davantage. Je ne peux pas insister davantage sur ce point. À la fin, la communication est susceptible d'être plus importante que toute votre puissance de 100 modèles.
* Débarrassez-vous du jargon complexe
* Plongez dans l'entreprise

### Conclusion

![Image](https://cdn-media-1.freecodecamp.org/images/3LazLBqqRo0kgvWhmL6YbUn7N4ohhQiyrbry)

Nous avons exploré certains points clés qui vous aideront à réussir un projet de prévision de séries temporelles. Certains d'entre eux peuvent sembler intuitifs et vous pourriez penser que vous ne ferez jamais ces erreurs, mais assurez-vous de vous vérifier. Souvent, la chose la plus facile à échouer est la plus évidente.

S'il vous plaît, [partagez l'article](https://ctt.ac/79dT2) s'il vous a aidé. Envisagez également de lui donner quelques applaudissements ? .

Suivez-moi sur ? T[witter](https://twitter.com/kdubovikov), ?Me[dium a](https://medium.com/@dubovikov.kirill) et ???Linke[dIn.](https://www.linkedin.com/in/kirill-dubovikov-2a20b154/)