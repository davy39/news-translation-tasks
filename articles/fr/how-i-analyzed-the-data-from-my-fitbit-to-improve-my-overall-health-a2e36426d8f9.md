---
title: Comment j'ai analysé les données de mon FitBit pour améliorer ma santé globale
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-09T21:34:54.000Z'
originalURL: https://freecodecamp.org/news/how-i-analyzed-the-data-from-my-fitbit-to-improve-my-overall-health-a2e36426d8f9
coverImage: https://cdn-media-1.freecodecamp.org/images/0*tFLhws9xNR64HVbz
tags:
- name: Data Science
  slug: data-science
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
seo_title: Comment j'ai analysé les données de mon FitBit pour améliorer ma santé
  globale
seo_desc: 'By Yash Soni

  It turns out that data can keep you healthy


  _Photo Credit: [Unsplash](https://unsplash.com/@franki?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">Franki Chamaki on <a href="https://unsplash.com?utm_source...'
---

Par Yash Soni

#### Il s'avère que les données peuvent vous maintenir en bonne santé

![Image](https://cdn-media-1.freecodecamp.org/images/QZMrnNh5FJCEunBOXlCOllbiiZIZRaub1Kfq)
_Crédit Photo : [Unsplash](https://unsplash.com/@franki?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Franki Chamaki</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Les trackers d'activité physique sont devenus une catégorie de produits multimillionnaire. J'ai eu ma part de trackers sophistiqués, commençant tôt avec le [Nike Fuelband](https://www.wareable.com/fitness-trackers/not-so-happy-birthday-nike-fuelband-2351) puis le [MI activity band](https://www.mi.com/in/miband/). Personnellement, je n'ai pas pu m'adapter à aucun d'entre eux et finalement, ils ont tous fini par être une montre numérique sophistiquée qui devait être rechargée tous les quelques jours pour qu'ils indiquent l'heure correcte.

Et puis, il y a quelques mois, un ami m'a offert un [Fitbit Versa](https://www.fitbit.com/versa). Quelque chose a cliqué. Pourquoi ?

Beaucoup de choses s'étaient passées depuis que j'avais abandonné l'idée que les bracelets de santé étaient efficaces. Lorsque j'ai reçu ce cadeau, j'étais à un stade où j'étais collé à une chaise et à mon ordinateur portable. En conséquence, j'avais un problème sévère de douleur dorsale et de déséquilibre postural. Les méfaits de nombreuses années ne pouvaient pas être corrigés en quelques jours ou semaines. Luttant contre une bataille ardue contre la position assise, qui est maintenant considérée par beaucoup comme le [nouveau "tabagisme"](https://www.startstanding.org/sitting-new-smoking/), je suis devenu conscient de ma posture et de l'idée de maintenir un mode de vie actif.

Alors, j'ai décidé de donner une nouvelle chance à Fitbit et je l'ai essayé pendant une semaine. L'application Fitbit a fait un assez bon travail pour capturer et présenter les données dans un format consommable.

![Image](https://cdn-media-1.freecodecamp.org/images/OW8rJRXNpRL94YLQyv3H9J3fn6sSmrgCZuRd)

![Image](https://cdn-media-1.freecodecamp.org/images/W3lmQTP1gQr6BMKZolZng8t-jm6BUuYdCvpJ)

![Image](https://cdn-media-1.freecodecamp.org/images/xQ6WXzbyd2CoctCHdiKP0Gobe-V8X47BTHTm)
_Analyse de l'activité, des calories brûlées et du sommeil sur l'application Fitbit._

Cela faisait deux semaines depuis ma rupture avec ma montre mécanique. Intrigué par la grande variété de points de données que Fitbit pouvait capturer, une envie a commencé à voir ce qui se cache derrière les données.

![Image](https://cdn-media-1.freecodecamp.org/images/mY1YeWyGdMshlqTrJWGh6Lo-RyMmG7Dv395T)
_Le cycle d'expérimentation. [Src](https://thehealthsciencesacademy.org/health-tips/how-to-conduct-an-effective-self-experiment/" rel="noopener" target="_blank" title=")_

J'ai bientôt commencé une expérience pour voir à quel point je pouvais suivre les objectifs que je m'étais fixés. Je voulais aussi savoir s'il y avait des facteurs extrinsèques qui influençaient ces objectifs. Enfin, je voulais découvrir des résultats cachés et intéressants en cours de route. J'étais particulièrement intéressé à découvrir :

* À quel point mes journées sont-elles actives ? Est-ce que je passe un temps considérable à être sédentaire ?
* Comment ces données varient-elles en semaine par rapport aux week-ends ?
* Quels sont les facteurs qui contribuent à la plus grande dépense calorique ?
* Quels exercices sont les meilleurs et les plus faciles pour atteindre mes objectifs quotidiens ?
* Ai-je suivi un horaire de sommeil régulier ? Quels sont les facteurs qui l'influencent ?
* Comprendre les phases de sommeil et découvrir ce qu'il faut pour obtenir un meilleur sommeil profond.
* Quel est l'impact d'une session de binge-watching sur Netflix sur le sommeil du week-end ?
* Entraîner un simple modèle de Machine Learning pour voir s'il existe un motif caché pour obtenir un meilleur sommeil.

Je n'ai pas pu trouver les réponses à ces questions dans l'application standard Fitbit. J'avais besoin des données brutes.

### Obtenir les données

La première tâche était de trouver des moyens d'extraire les données de mon appareil. En parcourant les pages des développeurs, j'ai trouvé qu'ils ont une provision d'[API Web](https://dev.fitbit.com/build/reference/web-api/) pour accéder aux données des utilisateurs. En examinant ces API, j'ai été choqué de voir la quantité de données qui est capturée et sauvegardée chaque minute. Les pas parcourus, les calories brûlées, les phases de sommeil et même le [rythme cardiaque/minute](https://dev.fitbit.com/build/reference/web-api/heart-rate/) pour un jour donné sont enregistrés !

Parfois, l'attrait séducteur de connaître notre bien-être général nous fait oublier quelles informations personnelles nous [finissons par partager](https://www.bna.com/consumers-wary-healthcare-n57982091088/). En lisant leurs politiques de confidentialité, j'ai trouvé que Fitbit a mis en place des vérifications supplémentaires pour garder les données en sécurité. En tout cas, cela nécessite un article séparé à part entière, alors sans digresser de notre objectif principal, continuons.

J'ai enregistré mon application et obtenu les informations d'identification nécessaires côté client pour commencer la collecte de données. Après avoir suivi les étapes d'autorisation nécessaires, j'ai collecté et fusionné mes données quotidiennes d'activité, de sommeil et de rythme cardiaque et je les ai placées dans un fichier Excel. Après un peu de nettoyage des données, le jeu de données était prêt !

![Image](https://cdn-media-1.freecodecamp.org/images/fkeipr40UH05TkJaRBwOsL8wbP2DLSmhbWN2)

![Image](https://cdn-media-1.freecodecamp.org/images/3qRwsTxyxlSj-bS7E7Nrq4cyYnmPjim7Eoeh)
_Session d'exemple de collecte de données et le DataFrame Pandas correspondant_

_PS. L'ensemble du code peut être trouvé [ici](https://github.com/yashatgit/fitbit-analyzer) ainsi que le [Jupyter notebook](https://github.com/yashatgit/fitbit-analyzer/blob/master/Fitbit_Data_Analysis.ipynb)._

_PPS. Avertissement : Cette analyse de données est basée sur un ensemble très limité de points de données et sera difficile à généraliser à la masse. Veuillez la considérer comme une lecture amusante !_

### Analyse de l'activité

Fitbit dispose d'une large gamme de points de données pour mesurer les niveaux d'activité quotidiens. Les pas, les calories et les étages sont quelques-unes des mesures standard. Il suit également combien de minutes je passe quotidiennement à être modérément, légèrement et très actif.

Sans me soucier de la dépense calorique quotidienne, je m'étais fixé un objectif d'atteindre 8000 pas chaque jour sur mon appareil Fitbit. Les graphiques ci-dessous suggèrent que je fais en moyenne environ ~7800 pas par jour, ce qui est assez proche de mon objectif. Il existe des études qui suggèrent que l'objectif idéal est d'atteindre [10 000](https://blog.fitbit.com/should-you-really-take-10000-steps-a-day/) [pas par jour](https://www.huffingtonpost.ca/leigh-vanderloo/10000-steps-a-day_b_16077702.html), et ce sera le prochain objectif.

Du mardi au samedi étaient les jours où je faisais en moyenne environ 40 minutes de _minutes très actives_, ce qui se traduit simplement par de [l'exercice actif](https://help.fitbit.com/articles/en_US/Help_article/1853/?l=en_US&c=Topics%3ADashboard&fs=Search&pn=1). Moins de minutes le dimanche étaient purement dues à la paresse/temps de récupération. La baisse des _minutes actives_ le lundi prouve que je suis victime du blues du lundi et je pense qu'il est temps de corriger cela.

![Image](https://cdn-media-1.freecodecamp.org/images/pvzvoW8pbiJ9an-55Rh8CnNqI4BvCxoLynJM)

L'analyse de la quantité de calories brûlées par minute pour diverses activités montre quelques résultats intéressants. Bien qu'il y ait beaucoup de données similaires disponibles sur Internet, il est très difficile de généraliser ces chiffres pour tout le monde. Puisque beaucoup de cela dépend des niveaux de forme physique, des données démographiques, des compétences et surtout de la mesure dans laquelle j'apprécie de faire certains exercices spécifiques.

![Image](https://cdn-media-1.freecodecamp.org/images/YFwjh8mzMQ5EzyNzTR9W2iNUcxJwwbIZwxmA)

Il est intéressant de voir que la course à pied m'aide à brûler presque 12 calories par minute. Le [calcul est simple](https://www.dailymail.co.uk/femail/article-3827053/How-exercise-does-burn-favourite-tipple.html) : pour compenser une bière, une course de 10 minutes est ce dont j'ai besoin.

Le tennis, l'activité favorite de la liste, prend la deuxième place. C'est encore une fois un scénario gagnant-gagnant ! Il sera intéressant de voir si ce nombre change à mesure que j'améliore mes compétences.

Les chiffres de la natation ne m'ont pas choqué car je lutte encore pour maintenir mon compte de longueurs continues. Et après avoir passé un certain temps dans la piscine, l'exercice se transforme en une activité de loisir.

Il est important de noter ici que les calories brûlées ne devraient pas être la seule mesure sur laquelle ces activités peuvent être évaluées. Mais c'est la seule mesure que je peux actuellement mesurer via Fitbit.

Enfin, il est utile de voir comment les différents points de données se corrèlent les uns avec les autres. Tracer une carte thermique de corrélation aide à découvrir certains résultats.

![Image](https://cdn-media-1.freecodecamp.org/images/fV5HQJGs-Wj6sMf0WF2-S6i5yrzAFyzGaesg)

Les calories brûlées sont fortement liées à la quantité de _pas_ et de _minutes actives_. Les _minutes sédentaires_ ont une corrélation négative avec les jours de semaine, ce qui implique que je passe plus de temps à me relâcher le week-end.

### Analyse du sommeil

Le sommeil est essentiel pour aider à maintenir l'humeur, la mémoire et les performances cognitives, et il n'y a pas moyen d'y échapper. Nous passons environ un tiers de notre vie à dormir. C'est un chiffre impressionnant de **26 ans passés à dormir dans un lit** ! Bien que le métabolisme ralentisse généralement, tous les organes majeurs et les systèmes de régulation continuent de fonctionner. Par conséquent, il devient important de tirer le meilleur parti de notre sommeil.

En lisant davantage sur ce sujet, j'ai trouvé qu'il existe des moyens standard qui peuvent aider à obtenir une bonne nuit de sommeil.

* [Suivre un bon horaire de sommeil](http://time.com/3183183/best-time-to-sleep/)
* [Éviter la lumière vive/bleue la nuit avant de se coucher](https://justgetflux.com/research.html)
* Éviter la caféine plus tard dans la journée
* Dormir dans une pièce fraîche et sombre
* Dormir au moins [7 à 9 heures](https://www.sleepfoundation.org/how-sleep-works/how-much-sleep-do-we-really-need). Il existe des études qui disent que même en [5 heures](https://blog.bulletproof.com/sleep-hacking-1-million-people-prove-sleeping-5-hours-is-healther-than-sleeping-8-hours/), vous pouvez tirer le meilleur parti de votre sommeil.

Au cours de cette expérience, j'ai essayé de suivre les étapes ci-dessus pour me lier à un horaire de sommeil strict. Il était temps de les valider.

D'après les graphiques ci-dessous, j'ai trouvé que je dormais en moyenne 7 heures sans grande déviation dans les chiffres. Bien que j'aie pu me coucher avant 23 heures, les heures de réveil variaient encore de 5h30 à 7h00.

![Image](https://cdn-media-1.freecodecamp.org/images/1aoBJ18QRW91xMe3VeYvnXk0MaJKt34VSQNZ)

![Image](https://cdn-media-1.freecodecamp.org/images/NSDjE1w-cbpmfyQ0s4sW2cJJtmlpNGMEOWgx)

Bien que la durée moyenne était quelque peu similaire, la qualité globale du sommeil n'était pas la même. Certains jours, j'étais très actif même en dormant 6 heures, tandis qu'il y a eu de nombreuses occasions où, même après m'être couché tard, je ne me sentais pas frais. J'ai trouvé la réponse en analysant les mystérieux **[cycles de sommeil](https://www.sleepfoundation.org/how-sleep-works)**.

Pendant que nous dormons, notre corps passe généralement par plusieurs cycles de sommeil, alternant entre les phases suivantes :

**SOMMEIL LÉGER :** Cette phase commence généralement quelques minutes après s'être endormi. La respiration et le rythme cardiaque diminuent légèrement pendant cette phase. Le sommeil léger favorise la récupération mentale et physique.

**SOMMEIL PROFOND :** Le sommeil profond se produit généralement dans les premières heures de sommeil. La respiration devient plus lente et les muscles se détendent tandis que le rythme cardiaque devient généralement plus régulier. Lorsque nous nous réveillons en nous sentant reposés le matin, il est probable que nous avons connu des périodes solides de sommeil profond. Le sommeil profond favorise la récupération physique et certains aspects de la mémoire et de l'apprentissage.

**SOMMEIL PARADOXAL :** Le sommeil paradoxal est une période active de sommeil marquée par une intense activité cérébrale. La première phase de sommeil paradoxal se produit généralement après une phase initiale de sommeil profond. La respiration est plus rapide, irrégulière et superficielle. Les yeux bougent rapidement dans diverses directions, d'où le nom de Mouvement Rapide des Yeux - Sommeil Paradoxe. C'est la phase où nous voyons généralement des rêves pendant notre sommeil. Le sommeil paradoxal a été montré pour jouer un rôle important dans la régulation de l'humeur, l'apprentissage et la mémoire.

Le graphique ci-dessous montre que, en moyenne, mon corps passe seulement environ 17 % en sommeil profond, 19 % en sommeil paradoxal et le reste en sommeil léger ou en étant légèrement éveillé. Le graphique date-heure du sommeil léger et profond montre que ces chiffres varient beaucoup.

![Image](https://cdn-media-1.freecodecamp.org/images/5hV7luHn9ANVZ2daqzbNIKec9YOd3t-gaFY9)

![Image](https://cdn-media-1.freecodecamp.org/images/oSi2W4JKlla6RB1ufA0BBWvO-DvS3SOXiy6S)

Si nous traçons la corrélation des différentes phases de sommeil, nous voyons que le temps passé au lit est fortement corrélé avec le sommeil léger, mais il n'y a pas de forte corrélation avec le sommeil profond.

![Image](https://cdn-media-1.freecodecamp.org/images/mdlNPY-xnzrhFsQCvhY1BK55IojcCPG7aINE)

Cela signifie essentiellement que dormir plus longtemps ne garantit pas toujours un bon sommeil profond. Je pense que cela aide à valider l'apprentissage important sur le sommeil :

> [C'est la qualité du sommeil qui compte et non la quantité.](https://www.sleep.org/articles/quality-quantity-matters-sleep/)

Suivre un horaire de sommeil strict en semaine est facile, mais les week-ends sont une autre paire de manches.

![Image](https://cdn-media-1.freecodecamp.org/images/lP-H1bLB-YwClB0r0vSmoFBCG6Ifq45ul7Gw)

Le boxplot ci-dessus montre que les samedis sont les plus affectés, où le temps passé au lit varie de 5 à 9 heures. Le binge-watching sur Netflix et les fêtes de week-end sont quelques-uns des vices qui ont affecté cette routine. En revanche, le plus petit boxplot du dimanche me montre me préparant pour les matins de lundi. Il est intéressant de voir comment ces comportements corporels subconscients sont clairement exposés dans ces graphiques.

Enfin, je voulais voir si mes activités quotidiennes avaient un effet sur mon sommeil. Bien que je n'avais pas beaucoup de données pour le modèle de Machine Learning, une première exécution a montré quelques résultats intéressants. Il a prédit que le fait d'être actif dans la journée et de se coucher avant 23 heures a des contributions positives aux minutes de sommeil profond final.

Bien qu'il soit trop tôt pour le valider, je répéterai cela une fois que j'aurai plus de données sur le sommeil et des caractéristiques supplémentaires pour améliorer la précision du modèle. Les détails peuvent être trouvés dans [ce Jupyter Notebook](https://github.com/yashatgit/fitbit-analyzer/blob/master/Fitbit_Data_Analysis.ipynb).

#### Est-ce que tout cela en valait la peine ?

Cette expérience a été une expérience enrichissante. J'ai identifié quelques façons intéressantes dont mon corps répond aux stimuli externes. C'est comme une machine où ajuster certains boutons peut aider à obtenir différents résultats.

Ensuite, je prévois de mettre en place des objectifs d'activité améliorés. Je vais également essayer [certains](https://blog.bulletproof.com/binaural-beats-sleep-meditation-benefits/) [biohacks](https://blog.bulletproof.com/how-to-hack-your-sleep-the-art-and-science-of-sleeping/) pour voir s'ils ont des effets positifs sur la qualité de mon sommeil. J'envisage également de développer une application d'alarme Fitbit qui ne me réveille que lorsque j'ai acquis une quantité suffisante de sommeil de qualité (je ne suis pas sûr si cela existe déjà ?).

Enfin, je n'ai pas l'intention de qualifier cela d'_expérience_ anymore. La routine quotidienne qui semblait forcée au début est devenue une habitude maintenant. Dans le passé, j'avais rencontré de nombreux articles qui étaient des études sur l'importance de se réveiller tôt, et finalement, je l'ai adopté en première main. Cet article Medium, qui est en fait mon premier, est l'un des nombreux sous-produits de cette nouvelle habitude.

Merci d'avoir pris le temps de parcourir mes analyses. Je serais plus que reconnaissant de savoir si vous l'avez aimé et si vous avez des suggestions pour des améliorations en général ! :)