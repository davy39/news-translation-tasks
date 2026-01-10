---
title: Comment nous avons réduit le gaspillage alimentaire et économisé de l'argent
  grâce au Machine Learning
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-28T15:21:17.000Z'
originalURL: https://freecodecamp.org/news/how-we-reduced-food-wastage-and-saved-money-using-machine-learning-c462aa5a3b30
coverImage: https://cdn-media-1.freecodecamp.org/images/0*slznjuTDVvxR96X7
tags:
- name: analytics
  slug: analytics
- name: Data Science
  slug: data-science
- name: food waste
  slug: food-waste
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
seo_title: Comment nous avons réduit le gaspillage alimentaire et économisé de l'argent
  grâce au Machine Learning
seo_desc: 'By Soundarya Balasubramani

  Welcome to a story of five simple students with one big goal: reducing food waste.
  In the US alone, pitched food weighs in at over 100 Empire State Buildings per year.
  Just how do five students dream of tackling this monume...'
---

Par Soundarya Balasubramani

Bienvenue dans l'histoire de cinq étudiants simples avec un grand objectif : réduire le gaspillage alimentaire. Aux États-Unis seulement, les aliments jetés pèsent plus de 100 Empire State Buildings par an. Comment cinq étudiants osent-ils rêver de s'attaquer à cette tâche monumentale, demandez-vous ? Eh bien, voici notre histoire de l'utilisation des données pour le bien.

![Image](https://cdn-media-1.freecodecamp.org/images/J9RaHAcVdZVOXjztzgAJFoKNa4maw8EchVmZ)

Dans le cadre du cours [Columbia Business School, _Analytics in Action_](https://www8.gsb.columbia.edu/courses/mba/2017/fall/b8146-001), nous nous sommes associés à une startup innovante de livraison de nourriture pour minimiser leurs déchets et réduire les dépenses. Le cours associe des équipes de 4 à 6 étudiants à de vraies entreprises pour résoudre des problèmes grâce à l'analytique.

Notre équipe diverse était composée de trois MBAs et de deux data scientists de l'École d'Ingénierie et des Sciences Appliquées. Nos parcours incluent la finance, le capital-risque, l'ingénierie et les sous-marins. Nous nous sommes associés à [Good Uncle](https://www.gooduncle.com/), une startup innovante et technologique qui apporte les meilleurs plats du pays sur les campus universitaires à travers les États-Unis.

![Image](https://cdn-media-1.freecodecamp.org/images/j-eMVOMn1p42ko8kDC4jbGvVLVoO0H3dVJ41)

![Image](https://cdn-media-1.freecodecamp.org/images/dY7297LDgh5xWd4Ge-YRGQX7MGSKFXcPDrxi)

![Image](https://cdn-media-1.freecodecamp.org/images/0XorY7naV6x9IEy9MHqWRhatyXUj46tCOvNT)
_L'application Good Uncle en action_

### Le Problème

Toute la préparation des aliments de Good Uncle commence dans une grande cuisine centrale dans le Delaware, près d'une semaine avant qu'un client ne passe sa commande. Ce modèle commercial ne laisse aucun temps à l'entreprise pour s'adapter à la demande ; en d'autres termes, le gaspillage alimentaire est particulièrement sensible à la précision de leur prévision de demande.

D'autres entreprises alimentaires surveillent leur inventaire et peuvent commander des réapprovisionnements qui arrivent avant que le restaurant ne soit en rupture de stock. Good Uncle doit commander des tomates et de la mozzarella plusieurs jours avant que l'idée de commander des pizza-rolls ne traverse l'esprit du client.

![Image](https://cdn-media-1.freecodecamp.org/images/BBNG0b8DagmINrs3YiJ5J1x6NgF0Jsy-j0Tg)

![Image](https://cdn-media-1.freecodecamp.org/images/zY8stMxrnsqSgzmzz-Y4Z8Zso9pyc4ahKR7b)

![Image](https://cdn-media-1.freecodecamp.org/images/MNL9-1PrL4z53gZh4nI59Tfrzv2bwUzq89lh)
_1. Pré-cuire la nourriture dans un lieu central, 2. Livrer à un marché local, 3. Terminer la cuisson pendant le transport pour la livraison._

### Notre Parcours

Nous avons d'abord rencontré [Matt, le PDG et fondateur de Good Uncle](https://www.linkedin.com/in/mattdoumar/), dans son bureau principal à Midtown Manhattan. Après avoir discuté des tenants et aboutissants de l'entreprise, nous sommes partis avec les données du _Printemps 2018_ pour l'Université de Syracuse et avons enfilé nos gants de nettoyage.

Nous avons ajouté toutes les fonctionnalités externes que nous pouvions imaginer, y compris la météo de [DarkSky](https://darksky.net/dev), les événements de StubHub, et, bien sûr, le calendrier académique du site web de l'école. Armés d'un arsenal de fonctionnalités descriptives, nous avons commencé à ajuster les modèles immédiatement. Beaucoup de modèles.

Notre processus a commencé avec l'objectif ambitieux de modéliser la demande au niveau le plus granulaire. Lorsque modèle après modèle a lamentablement échoué, nous avons canalisé notre frustration et avons cherché de l'aide auprès de nos professeurs inestimables et de notre brillant assistant. Nous avons réalisé que nous avions engagé un combat avec un adversaire redoutable : la prévision de séries temporelles à demande éparse.

Nous nous sommes plongés dans les données et avons recherché des moyens sensés de regrouper les points de vente ensemble. Nous devions éliminer cette rareté en agrégeant les ventes sur une base spatiotemporelle. Parce que les camions de nourriture se déplacent à travers les points de dépôt tout au long de la journée, nous devions examiner plusieurs méthodes de regroupement.

Avec des combinaisons à deux chiffres de techniques de modélisation et de regroupements de données, nous nous sommes tournés vers le benchmarking afin d'affiner notre choix de modèle et notre produit final pour Good Uncle.

Bien que notre objectif ait toujours été la prédiction de la demande, nous avons réalisé que notre cible réelle était la ligne de fond. Nous avons quantifié la valeur monétaire de commander trop ou trop peu d'un article donné au menu, et nous avons utilisé cela pour établir une équation cible. Pour comparer les modèles, nous avons optimisé pour le profit et avons trouvé que les arbres XGBoost et la régression de Poisson étaient les leaders évidents du groupe. Avec une dignité restaurée et beaucoup plus de confiance, nous avons fait le passage aux données en temps réel.

À peu près à mi-chemin du semestre _Automne 2018_, nous avons extrait un dump de données de l'entreprise et avons commencé à optimiser les modèles en temps réel. Les résultats parlent d'eux-mêmes dans la section ci-dessous.

### La Solution : **ATTENTION : Jargon technique à venir**

Nous avons lutté entre plus d'une demi-douzaine de techniques de modélisation, pivotant constamment à mesure que de nouvelles données et insights entraient en jeu. Nous avons travaillé avec la régression linéaire, la modélisation autorégressive, la régression de Poisson, la forêt aléatoire, les arbres de décision boostés par gradient extrême, et ainsi de suite. À la fin, le modèle parfait n'était pas un seul, mais une combinaison de deux modèles différents.

Nous avons réalisé que ce n'était pas seulement un problème de prévision de la demande, mais aussi de prévision des stocks, nous avons donc combiné les modèles de machine learning ci-dessus avec le célèbre [_modèle du vendeur de journaux utilisé pour la gestion des stocks_](https://en.wikipedia.org/wiki/Newsvendor_model).

![Image](https://cdn-media-1.freecodecamp.org/images/oSSTZ2xrQ-fmXEWX5ayYxukpOuvsR8XeafsW)

Tout d'abord, nous avons alimenté les données d'entrée dans le modèle linéaire généralisé de Poisson (GLM) et les modèles d'arbres boostés par gradient. La sortie des deux modèles a été utilisée comme entrées pour le modèle du vendeur de journaux, transformant l'équation ci-dessus en :

![Image](https://cdn-media-1.freecodecamp.org/images/sCFLesPbMOQB4g3Y4oeew4OeR47X8TRtqmh3)

La sortie finale a donné la prévision de la demande, et, en entraînant le modèle et en le validant avec divers niveaux de service (allant de 0,1 à 0,99), nous avons pu trouver le niveau optimal.

### Résultat :

Le graphique ci-dessous donne un aperçu de la manière dont notre modèle surpasse la méthode actuelle (appelons-la le modèle de GU). La meilleure façon de comparer notre nouvelle méthode à l'ancienne était de trouver le sous-approvisionnement (offre inférieure à la demande) et le surapprovisionnement (offre supérieure à la demande), qui a été tracé ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/FjhccEeZbAZicgI9tjpVyCgtaxz-McPdgSe3)

À partir de ce graphique, nous pouvons voir deux principaux enseignements.

* Nous pouvons être flexibles dans la définition de nos niveaux de sous-approvisionnement et de surapprovisionnement, alors que cette flexibilité n'est pas possible pour le modèle de GU (qui prend une valeur constante).
* Nous pouvons atteindre un surapprovisionnement _ainsi qu'un_ sous-approvisionnement moindres par rapport au modèle de Good Uncle pour des niveaux de service compris entre 0,67 et 0,91.

Nous avons réalisé qu'en fixant le niveau de service optimal à 0,68, notre modèle était capable d'économiser _~70 $ par rapport au modèle de GU_ pour un seul article alimentaire par trajet sur 10 jours. Mais nous voulions aller plus loin. Nous avons donc exécuté le modèle pour les 10 articles alimentaires les plus achetés sur les deux trajets et les regroupements, et nous avons obtenu le tableau pratique montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/xIm63xpJTXSdimAIJLf0dbVmR6HSPQHuzmmY)
_Économies/jour sur les dix articles alimentaires les plus populaires via les trajets et les regroupements_

Notre modèle a été capable d'économiser de l'argent sur tous les articles sauf un (il n'aime tout simplement pas l'assiette de porc effiloché BBQ !). Enfin, pour montrer clairement la puissance du modèle, nous avons extrapolé la valeur en dollars pour un semestre entier en l'exécutant sur tous les trajets et regroupements pour les 10 articles les plus populaires.

**_Nous avons observé une économie potentielle de 29 256 $ pour les 10 articles alimentaires les plus achetés sur tous les points de dépôt (par trajet) en seulement 1 semestre, sur un seul campus._**

### En Conclusion

Cela a été la plus grande opportunité académique de notre mandat, allant bien au-delà des murs de la classe. Nous avons passé un si bon moment à travailler avec de nouveaux amis et nous avons tant appris des professeurs, et, bien sûr, des merveilleuses personnes de Good Uncle. Non seulement nous avons bu à la lance à incendie de l'analytique des données, mais nous avons partagé le parcours d'une startup innovante et en pleine croissance et avons appris des meilleurs entrepreneurs de NYC.

### L'Équipe

L'équipe était composée de 5 membres : [Bowen Bao](https://www.linkedin.com/in/bowen-bao/), [Don Holder](https://www.linkedin.com/in/don-holder-8b72a0122/), [Jack Spitsin](https://www.linkedin.com/in/jackspitsin/), [Nicolai Mouhin](https://www.linkedin.com/in/nicolai-mouhin/) et moi-même. Cet article a été écrit dans le cadre d'un effort d'équipe.

******************************************************************

_Si vous avez trouvé cela utile, faites [**Follow me**](https://medium.com/@poojabalasubramani) pour plus d'articles. Saviez-vous que vous pouvez_ ? m_ore than once? Try it out! ?_I _love writing about social issues, products, the technology sector and my graduate school experience in the US. Here is my pe[**rsonal blog.**](http://poojabalasubramani.wordpress.com/) **If** youre a curious soul looking to learn everyday, heres a Sl[**ack Group t**](https://poojabalasubramani.com/2018/12/18/exciting-news-an-update-to-the-slack-group/)hat I created for you to join._

_The best way to get in touch with me is via [Instagram](https://www.instagram.com/thecuriousmaverick/)_ and [**Facebook**](https://www.facebook.com/pooja.balasubramani?ref=bookmarks). I share some interesting content there. To know more about my professional life, check out my [**LinkedIn**](https://www.linkedin.com/in/soundarya-balasubramani/). Happy reading!