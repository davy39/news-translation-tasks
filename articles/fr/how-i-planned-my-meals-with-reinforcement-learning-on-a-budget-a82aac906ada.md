---
title: Comment j'ai planifié mes repas avec l'apprentissage par renforcement sur un
  budget
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-16T16:00:10.000Z'
originalURL: https://freecodecamp.org/news/how-i-planned-my-meals-with-reinforcement-learning-on-a-budget-a82aac906ada
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DJoo_O-eNQAnYrc4blWzAg.jpeg
tags:
- name: budget
  slug: budget
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Reinforcement Learning
  slug: reinforcement-learning
- name: technology
  slug: technology
seo_title: Comment j'ai planifié mes repas avec l'apprentissage par renforcement sur
  un budget
seo_desc: 'By Sterling Osborne, PhD Researcher

  Following my recent article on applying Reinforcement Learning to real life problems,
  I decided to demonstrate this with a small example. The aim is to create an algorithm
  that can find a suitable choice of food pr...'
---

Par Sterling Osborne, Chercheur en doctorat

Suite à [mon récent article sur l'application de l'apprentissage par renforcement à des problèmes de planification de la vie réelle](https://medium.freecodecamp.org/how-to-apply-reinforcement-learning-to-real-life-planning-problems-90f8fa3dc0c5), j'ai décidé de démontrer cela avec un petit exemple. L'objectif est de créer un algorithme capable de trouver un choix approprié de produits alimentaires pour respecter un budget et répondre à mes préférences personnelles.

J'ai également publié la description, les données et le noyau de code sur Kaggle, que vous pouvez trouver [ici](https://www.kaggle.com/osbornep/reinforcement-learning-for-meal-planning-in-python/notebook).

N'hésitez pas à me faire savoir si vous avez des questions ou des suggestions.

![Image](https://cdn-media-1.freecodecamp.org/images/LZJGp50r3YXHLlCWaMEoqYBhRwvpxdjsdgwa)
_Photo : Pixabay_

### Objectif

Lors des courses alimentaires, il existe de nombreux produits différents pour le même ingrédient à choisir dans les supermarchés. Certains sont moins chers, d'autres sont de meilleure qualité. Je souhaite créer un modèle qui, pour les ingrédients requis, puisse sélectionner les produits optimaux nécessaires pour préparer un repas qui soit à la fois :

1. Dans mon budget
2. Répond à mes préférences personnelles

Pour ce faire, je vais d'abord construire un modèle très simple capable de recommander les produits qui sont en dessous de mon budget avant d'introduire mes préférences.

La raison pour laquelle nous utilisons un modèle est que nous pourrions, en théorie, étendre le problème pour considérer de plus en plus d'ingrédients et de produits, ce qui rendrait le problème au-delà de la possibilité de tout calcul mental.

### Méthode

Pour y parvenir, je vais construire un simple modèle d'apprentissage par renforcement et j'utiliserai l'apprentissage Monte Carlo pour trouver la combinaison optimale de produits.

Tout d'abord, définissons formellement les parties de notre modèle comme un processus de décision de Markov :

* Nous avons un nombre fini d'ingrédients nécessaires pour préparer un repas et sont considérés comme nos **États**
* Il existe les produits finis possibles pour chaque ingrédient et sont donc les **Actions de chaque état**
* Nos préférences deviennent les **Récompenses individuelles** pour la sélection de chaque produit, nous aborderons cela plus en détail plus tard

L'apprentissage Monte Carlo combine la qualité de chaque étape pour atteindre un objectif final et nécessite que, afin d'évaluer la qualité de toute étape, nous devions attendre et voir le résultat de toute la combinaison. Ce processus est répété encore et encore dans des épisodes avec de nombreux produits différents jusqu'à ce qu'il trouve la sélection qui semble conduire à un résultat positif de manière répétée. C'est le processus d'apprentissage par renforcement où notre environnement est simulé sur la base des connaissances sur les coûts et les préférences que nous avons obtenues.

Monte Carlo est souvent évité en raison du temps nécessaire pour parcourir tout le processus avant de pouvoir apprendre. Cependant, dans notre problème, il est nécessaire car notre vérification finale pour établir si la combinaison de produits sélectionnés est bonne ou mauvaise est d'additionner le coût réel de ceux sélectionnés et de vérifier si cela est inférieur ou supérieur à notre budget. De plus, au moins à ce stade, nous ne considérerons pas plus de quelques ingrédients et donc le temps pris n'est pas significatif à cet égard.

![Image](https://cdn-media-1.freecodecamp.org/images/5XabGzV2o9PFKK7nUoP-QHSShPx6a2ur1XdM)
_[https://www.tractica.com/artificial-intelligence/reinforcement-learning-and-its-implications-for-enterprise-artificial-intelligence/](https://www.tractica.com/artificial-intelligence/reinforcement-learning-and-its-implications-for-enterprise-artificial-intelligence/" rel="noopener" target="_blank" title=")_

### Données d'exemple

Pour cette démonstration, j'ai créé des données d'exemple pour un repas où nous avons 4 ingrédients et 9 produits, comme le montre le diagramme ci-dessous.

Nous devons sélectionner un produit pour chaque ingrédient du repas.

Cela signifie que nous avons 2 x 2 x 2 x 3 = 24 sélections possibles de produits pour les 4 ingrédients.

J'ai également inclus le coût réel pour chaque produit et V_0.

V_0 est simplement la qualité initiale de chaque produit pour répondre à nos exigences et nous la définissons à 0 pour chacun.

![Image](https://cdn-media-1.freecodecamp.org/images/eCjXwnetr8IA787ykWpZq4k6OdbHEroKoA5M)
_Diagramme montrant les choix de produits possibles pour chaque ingrédient_

Tout d'abord, nous importons les packages et les données requis.

![Image](https://cdn-media-1.freecodecamp.org/images/IJ5NNxRwWJQ8QcwXNicYIDoxXZjcEGzOdzRz)

![Image](https://cdn-media-1.freecodecamp.org/images/YvGNf8QiGazYIDSMQhdmNWKU8TnfviITZHrd)

### Application du modèle en théorie

Pour l'instant, je n'introduirai aucune récompense individuelle pour les produits. Au lieu de cela, je me concentrerai simplement sur le fait que la combinaison de produits sélectionnés est en dessous de notre budget ou non. Ce résultat est défini comme la **Récompense terminale** de notre problème.

Par exemple, disons que nous avons un budget de 30 £, alors le choix :

a1→b1→c1→d1

Alors le coût réel de cette sélection est :

10 £ + 8 £ + 3 £ + 8 £ = 29 £ < 30 £

Et donc, notre récompense terminale est :

R_T=+1

Alors que,

a2→b2→c2→d1

Alors le coût réel de cette sélection est :

6 £ + 11 £ + 7 £ + 8 £ = 32 £ > 30 £

Et donc, notre récompense terminale est :

R_T=-1

Pour l'instant, nous disons simplement à notre modèle si le choix est bon ou mauvais et nous observerons ce que cela fait aux résultats.

### Apprentissage du modèle

Alors, comment notre modèle apprend-il réellement ? En bref, nous faisons en sorte que notre modèle essaie de nombreuses combinaisons de produits et, à la fin de chacune, nous lui disons si son choix était bon ou mauvais. Avec le temps, il reconnaîtra que certains produits mènent généralement à un bon résultat, tandis que d'autres non.

Ce que nous finissons par créer, ce sont des valeurs pour la qualité de chaque produit, notées V(a). Nous avons déjà introduit le V(a) initial pour chaque produit, mais comment passons-nous de ces valeurs initiales à la capacité de prendre une décision ?

Pour cela, nous avons besoin d'une **Règle de mise à jour**. Cela indique au modèle, après chaque fois qu'il a présenté son choix de produits et que nous lui avons dit si sa sélection est bonne ou mauvaise, comment ajouter cela à nos valeurs initiales.

Notre règle de mise à jour est la suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/tBfSiFmawCqLJM2rP0VpSrWRa7btGNT4iOiw)

Cela peut sembler inhabituel au premier abord, mais en mots, nous mettons simplement à jour la valeur de toute action, V(a), d'un montant qui est soit un peu plus si le résultat était bon, soit un peu moins si le résultat était mauvais.

G est le **Retour** et est simplement la récompense totale obtenue. Actuellement dans notre exemple, il s'agit simplement de la récompense terminale (+1 ou -1 selon le cas). Nous réintroduirons cela plus tard lorsque nous inclurons les récompenses individuelles des produits.

Alpha, α, est le **Taux d'apprentissage** et nous démontrerons plus tard comment cela affecte les résultats, mais pour l'instant, l'explication simple est : « Le taux d'apprentissage détermine dans quelle mesure les informations nouvellement acquises remplacent les anciennes informations. Un facteur de 0 fait que l'agent n'apprend rien, tandis qu'un facteur de 1 fait que l'agent ne considère que les informations les plus récentes. » ([https://en.wikipedia.org/wiki/Q-learning](https://en.wikipedia.org/wiki/Q-learning))

### Petite démonstration de la mise à jour des valeurs

Alors, comment utilisons-nous cela avec notre modèle ?

Commençons par un tableau qui contient chaque produit et son V_0(a) initial :

![Image](https://cdn-media-1.freecodecamp.org/images/dKkesqok94JNwSZHLDBzEdKnmyKP5NmqwERQ)

Nous choisissons maintenant une sélection aléatoire de produits, chaque combinaison est connue sous le nom d'**épisode**. Nous définissons également α=0,5 pour l'instant, juste pour simplifier les calculs.

Par exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/rAPEHqEY3U0XJekgOwusn6dYbxpQgHQ4ghhl)

Par conséquent, toutes les actions qui mènent à ce résultat positif sont également mises à jour pour produire le tableau suivant avec V1(a) :

![Image](https://cdn-media-1.freecodecamp.org/images/GSmEiJ8IZIYsbsUaieXz4jBQfjeL3wzch1HC)

Alors essayons à nouveau en choisissant un autre épisode aléatoire :

![Image](https://cdn-media-1.freecodecamp.org/images/r7aeYiWCHv9zR0d9e5E2QbbKaN17BjllHdz-)

Par conséquent, nous pouvons ajouter V2(a) à notre tableau :

![Image](https://cdn-media-1.freecodecamp.org/images/E3Y525fxV7LX8vcdTvqVNyaGT0GAQ8vkLb4I)

### Sélection d'action

Vous avez peut-être remarqué dans la démonstration que j'ai simplement sélectionné aléatoirement les produits dans chaque épisode. Nous pourrions faire cela, mais utiliser un processus de sélection complètement aléatoire peut signifier que certaines actions ne sont pas sélectionnées assez souvent pour savoir si elles sont bonnes ou mauvaises.

De même, si nous allions dans une autre direction et décidions de sélectionner les produits de manière avide, c'est-à-dire ceux qui ont actuellement la meilleure valeur, nous pourrions manquer celui qui est en fait meilleur mais qui n'a jamais eu sa chance. Par exemple, si nous choisissions les meilleures actions de V2(a), nous obtiendrions a2, b1, c1 et d2 ou d3, qui offrent tous deux une récompense terminale positive. Par conséquent, si nous utilisions un processus de sélection purement avide, nous ne considérerions jamais d'autres produits, car ceux-ci continuent de fournir un résultat positif.

Au lieu de cela, nous mettons en œuvre une sélection d'action **epsilon-greedy** où nous sélectionnons aléatoirement des produits avec une probabilité ε, et sélectionnons de manière avide des produits avec une probabilité 1-ε où :

![Image](https://cdn-media-1.freecodecamp.org/images/w7prUkGhYtx6PfE16dfGTFC2QTZG0DhbEWRy)

Cela signifie que nous allons atteindre le choix optimal de produits rapidement, car nous continuons à tester si les produits « bons » sont en fait optimaux. Mais cela laisse également de la place pour explorer d'autres produits occasionnellement, juste pour s'assurer qu'ils ne sont pas aussi bons que notre choix actuel.

### Construction et application de notre modèle

Nous sommes maintenant prêts à construire un modèle simple comme le montre la fonction MCModelv1 ci-dessous.

Bien que cela semble complexe, je n'ai rien fait de plus que d'appliquer les méthodes précédemment discutées de manière à ce que nous puissions varier les entrées et obtenir des résultats. Je l'admets, c'était ma première tentative de le faire et donc mon codage peut ne pas être parfaitement écrit mais devrait être suffisant pour nos besoins.

Pour calculer la récompense terminale, nous utilisons actuellement la condition suivante pour vérifier si le coût total est inférieur ou supérieur à notre budget :

![Image](https://cdn-media-1.freecodecamp.org/images/3Wqi4imz2FQDmGOWAj96pNV3lhw6PcEv-BwO)

![Image](https://cdn-media-1.freecodecamp.org/images/Sh2bBPQoanKimfAFPNLATlzHIRVZeMsapqVI)

**Le code complet du modèle est trop grand pour être affiché ici, mais peut être trouvé sur la page [Kaggle](https://www.kaggle.com/osbornep/reinforcement-learning-for-meal-planning-in-python/notebook) liée.**

#### Nous exécutons maintenant notre modèle avec quelques variables d'exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/wsawgTD72Mfaf2GqTzg9-2EPXgWHV7Jcx2Cq)

Dans notre fonction, nous avons 6 sorties du modèle :

* Mdl[0] : Retourne la somme de tous les V(a) pour chaque épisode
* Mdl[1] : Retourne la somme des V(a) pour les produits les moins chers, possibles à définir en raison de la simplicité de nos données d'exemple
* Mdl[2] : Retourne la somme des V(a) pour les produits non les moins chers
* Mdl[3] : Retourne les actions optimales du dernier épisode
* Mdl[4] : Retourne le tableau de données avec le V(a) final ajouté pour chaque produit
* Mdl[5] : Montre l'action optimale à chaque épisode

Il y a beaucoup à retenir de cela, alors passons en revue chaque point et établissons ce que nous pouvons apprendre pour améliorer notre modèle.

#### Actions optimales du dernier épisode

Tout d'abord, voyons ce que le modèle suggère de sélectionner. Dans cette exécution, il suggère des actions, ou produits, qui ont un coût total inférieur au budget, ce qui est bien.

Cependant, il y a encore plus que nous pouvons vérifier pour nous aider à comprendre ce qui se passe.

Tout d'abord, nous pouvons tracer le V total pour toutes les actions, et nous voyons que cela converge, ce qui est idéal. Nous voulons que notre modèle converge afin que, lorsque nous essayons plus d'épisodes, nous nous rapprochions de plus en plus du choix optimal de produits. La raison pour laquelle la sortie converge est que nous réduisons le montant qu'il apprend chaque fois d'un facteur de α, dans ce cas 0,5. Nous montrerons plus tard ce qui se passe si nous varions cela ou si nous ne l'appliquons pas du tout.

Nous avons également tracé la somme de V pour les produits que nous savons être les moins chers, sur la base de la possibilité d'évaluer la petite taille de l'échantillon, et les autres séparément. Encore une fois, les deux convergent positivement, bien que les produits moins chers semblent avoir des valeurs légèrement plus élevées.

![Image](https://cdn-media-1.freecodecamp.org/images/4WTvyb0pa3be9kJmsvP8PQsIGSce2EdbQPLj)

![Image](https://cdn-media-1.freecodecamp.org/images/UFFckpQP0O2XLeE49eoTeaiVWmKY-fScgvJ0)

#### Alors pourquoi cela se produit-il et pourquoi le modèle a-t-il suggéré les actions qu'il a faites ?

Pour comprendre cela, nous devons disséquer les suggestions faites par le modèle à chaque épisode et comment cela se rapporte à notre retour.

Ci-dessous, nous avons pris l'action optimale pour chaque état. Nous pouvons voir que les actions suggérées varient grandement entre les épisodes et que le modèle semble décider très rapidement ce qu'il veut suggérer.

Par conséquent, j'ai tracé le coût total des actions suggérées à chaque épisode et nous pouvons voir que les actions varient initialement puis se stabilisent et que le coût total résultant est inférieur à notre budget. Cela nous aide grandement à comprendre ce qui se passe.

Jusqu'à présent, tout ce que nous avons dit au modèle, c'est de fournir une sélection qui est en dessous du budget et il l'a fait. Il a simplement trouvé une réponse qui est en dessous du budget comme requis.

Alors, quelle est la prochaine étape ? Avant d'introduire les récompenses, je veux démontrer ce qui se passe si je varie certains des paramètres et ce que nous pouvons faire si nous décidons de changer ce que nous voulons que notre modèle suggère.

![Image](https://cdn-media-1.freecodecamp.org/images/A5ywpBkRB2P3G-8WCwYu1-HQ2lAuON565bS3)

![Image](https://cdn-media-1.freecodecamp.org/images/LrC00RigDKHw90YQMaAnKVxogZJ9urKzrtP8)

![Image](https://cdn-media-1.freecodecamp.org/images/pMFzDzpPZRDDzpSpUuEb7mUbhLCKHD93kldf)

### Effet du changement de paramètres et comment changer l'objectif du modèle

Nous avons quelques paramètres qui peuvent être modifiés :

1. Le budget
2. Notre taux d'apprentissage, α
3. Notre paramètre de sélection d'action, ε

#### Variation du budget

Tout d'abord, observons ce qui se passe si nous rendons notre budget soit impossiblement bas, soit élevé.

Un petit budget signifie que nous n'obtenons qu'une récompense négative, ce qui signifie que nous allons forcer notre V à converger négativement, alors qu'un budget trop élevé fera converger notre V positivement, car toutes les actions sont continuellement positives.

![Image](https://cdn-media-1.freecodecamp.org/images/ClL2XcjSAPq4hzJWOLLygAyYiI4QS7-hmmYi)

![Image](https://cdn-media-1.freecodecamp.org/images/ePz3LMNDjQN1FQGHdcYHEF65gA9A1MOu7Ywh)

Ce dernier semble être ce que nous avions lors de notre première exécution, beaucoup d'épisodes mènent à des résultats positifs et donc de nombreuses combinaisons de produits sont possibles et il y a peu de distinction entre les produits les moins chers et les autres.

Si, au lieu de cela, nous considérons un budget qui est raisonnablement bas étant donné les prix des produits, nous pouvons voir une tendance où les produits les moins chers semblent converger positivement et les produits plus chers convergent négativement. Cependant, la fluidité de ceux-ci est loin d'être idéale, les deux semblent osciller grandement entre chaque épisode.

![Image](https://cdn-media-1.freecodecamp.org/images/9vYicIrKqHGM8unbhIyICWNeKLD7FRe0zKbm)

![Image](https://cdn-media-1.freecodecamp.org/images/sboascUNlUZ1xKs64W5x4g7Jd0tVOK4NYG3l)

Alors, que pouvons-nous faire pour réduire les « pics » des sorties ? Cela nous amène à notre prochain paramètre, alpha.

### Variation d'Alpha

#### Une bonne explication de ce qui se passe avec notre sortie en raison d'alpha est décrite par l'utilisateur de Stack Overflow VishalTheBeast :

> « Le taux d'apprentissage indique l'ampleur de l'étape qui est entreprise vers la solution.

> Il ne doit pas être un nombre trop grand car il peut osciller continuellement autour des minima et il ne doit pas être un nombre trop petit sinon il faudra beaucoup de temps et d'itérations pour atteindre les minima.

> La raison pour laquelle une décroissance est conseillée dans le taux d'apprentissage est que, initialement, lorsque nous sommes à un point totalement aléatoire dans l'espace de solution, nous devons faire de grands bonds vers la solution et plus tard, lorsque nous nous en approchons, nous faisons de petits sauts et donc de petites améliorations pour enfin atteindre les minima.

> L'analogie peut être faite comme suit : dans le jeu de golf, lorsque la balle est loin du trou, le joueur la frappe très fort pour se rapprocher le plus possible du trou. Plus tard, lorsqu'il atteint la zone marquée, il choisit un autre bâton pour obtenir un tir court précis.

> Donc, ce n'est pas qu'il ne pourra pas mettre la balle dans le trou sans choisir le bâton de tir court, il peut envoyer la balle au-delà de la cible deux ou trois fois. Mais ce serait mieux s'il joue de manière optimale et utilise la bonne quantité de puissance pour atteindre le trou. Il en va de même pour le taux d'apprentissage décroissant. » — [source](https://stackoverflow.com/questions/33011825/learning-rate-of-a-q-learning-agent)

Pour mieux démontrer l'effet de la variation de notre alpha, j'utiliserai un graphique animé créé avec Plot.ly.

J'ai écrit un guide plus détaillé sur la façon de faire cela [ici](https://towardsdatascience.com/creating-interactive-animation-for-parameter-optimisation-using-plot-ly-8136b2997db).

Dans notre première animation, nous varions alpha entre 1 et 0,1. Cela nous permet de voir que lorsque nous réduisons alpha, notre sortie se lisse quelque peu, mais elle reste assez brute.

Cependant, même si les résultats se lissent, ils ne convergent plus en 100 épisodes et, de plus, la sortie semble alterner entre chaque alpha. Cela est dû à une combinaison de petits alphas nécessitant plus d'épisodes pour apprendre et notre paramètre de sélection d'action epsilon étant de 0,5. Essentiellement, la sortie est encore décidée par le hasard la moitié du temps et donc nos résultats ne convergent pas dans le cadre des 100 épisodes.

![Image](https://cdn-media-1.freecodecamp.org/images/aB38O-aTjeYWBdtMd9NRPAmkFpfCKfzR0qPB)

L'exécution de cela à travers nos graphiques animés produit quelque chose de similaire à ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/wVLIs9ttJH3P27B50Xf9rCYg0x4YxU6otsy5)

### Variation d'Epsilon

Avec les résultats précédents à l'esprit, nous fixons maintenant alpha à 0,05 et varions epsilon entre 1 et 0 pour montrer l'effet de la sélection complètement aléatoire des actions à la sélection avide des actions.

Les graphiques ci-dessous montrent trois instantanés de la variation d'epsilon, mais la version animée peut être consultée dans le [noyau Kaggle](https://www.kaggle.com/osbornep/reinforcement-learning-for-meal-planning-in-python/notebook).

Nous voyons qu'avoir un epsilon élevé crée des résultats très sporadiques. Par conséquent, nous devrions sélectionner quelque chose de raisonnablement petit comme 0,2. Bien qu'avoir epsilon égal à 0 semble bien en raison de la fluidité de la courbe, comme nous l'avons mentionné précédemment, cela peut nous mener à un choix très rapidement mais qui peut ne pas être le meilleur. Nous voulons un peu de hasard pour que le modèle puisse explorer d'autres actions si nécessaire.

![Image](https://cdn-media-1.freecodecamp.org/images/MSioaunlsQvp2AADkQjHB0R6X6yAfTEAIn0Q)

![Image](https://cdn-media-1.freecodecamp.org/images/Rnmcx-e31oLcKZA9-M4fyHHs5MOdTPoQXmdW)

![Image](https://cdn-media-1.freecodecamp.org/images/R8FGYGkQjh55aapbnQs3TS1dBsC7iU7uKLaX)

### Augmentation du nombre d'épisodes

Enfin, nous pouvons augmenter le nombre d'épisodes. Je me suis abstenu de le faire plus tôt car nous exécutions 10 modèles dans une boucle pour produire nos graphiques animés et cela aurait fait exploser le temps nécessaire pour exécuter le modèle.

Nous avons noté qu'un alpha faible nécessiterait plus d'épisodes pour apprendre, nous pouvons donc exécuter notre modèle pour 1000 épisodes.

Cependant, nous remarquons toujours que la sortie oscille, mais, comme mentionné précédemment, cela est dû à notre objectif étant simplement de recommander une combinaison qui est en dessous du budget. Ce que cela montre, c'est que le modèle ne peut pas trouver la meilleure combinaison unique lorsqu'il y en a beaucoup qui rentrent dans notre budget.

Par conséquent, que se passe-t-il si nous changeons légèrement notre objectif afin que nous puissions utiliser le modèle pour trouver la combinaison de produits la moins chère ?

![Image](https://cdn-media-1.freecodecamp.org/images/2h7mS1jrLjv3KD47T77ARG-2tTscftXWGJUI)

![Image](https://cdn-media-1.freecodecamp.org/images/9xMMzsxigFz4Zx3n-womG45Q4qzWsYtvEBx4)

### Changement de l'objectif de notre modèle pour trouver la combinaison de produits la moins chère

L'objectif de cela est de séparer plus clairement les produits les moins chers des autres, et il nous fournit presque toujours la combinaison de produits la moins chère.

Pour ce faire, tout ce que nous devons faire est d'adapter légèrement notre modèle pour fournir une récompense terminale qui est relative à la distance en dessous ou au-dessus du budget de cette combinaison dans l'épisode.

Cela peut être fait en changeant le calcul pour le retour à :

![Image](https://cdn-media-1.freecodecamp.org/images/xW4GsM4rWI0XRPjxKYPn7dFmg5nz8DtuLeBM)

Nous voyons maintenant que la séparation entre les produits les moins chers et les autres est accentuée.

Cela démontre vraiment la flexibilité de l'apprentissage par renforcement et la facilité avec laquelle il peut être adapté en fonction de vos objectifs.

![Image](https://cdn-media-1.freecodecamp.org/images/u8R2pcQCWZhl2tCIZ3nu2cFF90oMWhISSXJy)

### Introduction des préférences

Jusqu'à présent, nous n'avons pas inclus de préférences personnelles pour les produits. Si nous voulions inclure cela, nous pouvons simplement introduire des récompenses pour chaque produit tout en ayant une récompense terminale qui encourage le modèle à rester en dessous du budget.

Cela peut être fait en changeant le calcul pour le retour à :

![Image](https://cdn-media-1.freecodecamp.org/images/8S-ifGXjN3WYCyYpGgC2LYU2EJukmVB5XUo2)

Alors, pourquoi notre calcul de retour est-il maintenant comme cela ?

Tout d'abord, nous voulons toujours que notre combinaison soit en dessous du budget, donc nous fournissons les récompenses positives et négatives pour être au-dessus et en dessous du budget, respectivement.

Ensuite, nous voulons tenir compte de la récompense de chaque produit. Pour nos besoins, nous définissons les récompenses comme une valeur entre 0 et 1. Le retour MC est formellement calculé en utilisant ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1vJAlBcCYSLMbG41EbcNi5TkW191DHCXR2hz)

γ est le facteur d'actualisation et cela nous indique combien nous valorisons les étapes ultérieures par rapport aux étapes précédentes. Dans notre cas, toutes les actions sont également importantes pour atteindre le résultat souhaité d'être en dessous du budget, donc nous définissons γ=1.

Cependant, pour nous assurer que nous atteignons l'objectif principal d'être en dessous du budget, nous prenons la moyenne de la somme des récompenses pour chaque action afin que cela soit toujours inférieur à 1 ou -1, respectivement.

Encore une fois, le modèle complet peut être trouvé dans le [noyau Kaggle](https://www.kaggle.com/osbornep/reinforcement-learning-for-meal-planning-in-python/notebook) mais est trop grand pour être lié ici.

### Introduction des préférences en utilisant les récompenses

Supposons que nous avons décidé que nous voulions les produits a1 et b2, nous pourrions ajouter une récompense à chacun. Voyons ce qui se passe si nous faisons cela dans la sortie et les graphiques ci-dessous. Nous avons légèrement changé notre budget car a1 et b2 s'additionnent à 21 £, ce qui signifie qu'il n'y a aucun moyen de sélectionner deux produits supplémentaires qui le mettraient en dessous d'un budget de 23 £.

L'application d'une récompense très élevée force le modèle à choisir a1 et b2, puis à travailler autour pour trouver des produits qui le mettront en dessous de notre budget.

J'ai gardé la comparaison entre les produits les moins chers et les autres pour montrer que le modèle ne valorise plus les moins chers. Au lieu de cela, nous obtenons la sortie a1, b2, c1 et d3, qui a un coût total de 25 £. Cela est à la fois en dessous de notre budget et inclut nos produits préférés.

![Image](https://cdn-media-1.freecodecamp.org/images/4CBCAhqhP1HzYgZgYyK4ugbTUHHdCHl0uEg0)

![Image](https://cdn-media-1.freecodecamp.org/images/Szh6HaR-2PnC7tACxh9OI4B3z5YMUpEo-vyP)

Essayons un autre signal de récompense. Cette fois, je donne une certaine récompense à chacun mais je veux qu'il fournisse la meilleure combinaison de mes récompenses qui nous maintient toujours en dessous du budget.

Nous avons les récompenses suivantes :

![Image](https://cdn-media-1.freecodecamp.org/images/H-EJrGUSdqRcbj5QpAQ29VxP8YbGiGF8Jvyy)

L'exécution de ce modèle plusieurs fois montre qu'il :

* Sélectionne souvent a1 car celui-ci a une récompense beaucoup plus élevée
* Choisit toujours c1, car les récompenses sont les mêmes mais il est moins cher
* A du mal à choisir entre b1 et b2 car les récompenses sont de 0,5 et 0,6 mais les coûts sont de 8 £ et 11 £ respectivement
* Sélectionne généralement d3 car il est significativement moins cher que d1 même si la récompense est légèrement inférieure

![Image](https://cdn-media-1.freecodecamp.org/images/f7kOKIZRdMFsAY5DgTUEK9xb5JOkpMfKjn5n)

![Image](https://cdn-media-1.freecodecamp.org/images/1e31yEJBL6uufYC8-ByEst2QyrZMCx-gFggI)

### Conclusion

Nous avons réussi à construire un modèle d'apprentissage par renforcement Monte Carlo pour :

1. recommander des produits en dessous d'un budget,
2. recommander les produits les moins chers, et
3. recommander les meilleurs produits en fonction d'une préférence qui est toujours en dessous d'un budget.

En cours de route, nous avons démontré l'effet du changement de paramètres dans l'apprentissage par renforcement et comment la compréhension de ceux-ci nous permet d'atteindre un résultat souhaité.

Il y a beaucoup plus que nous pourrions faire, à mon avis, l'objectif final serait de l'appliquer à une vraie recette et à des produits d'un supermarché où le nombre accru d'ingrédients et de produits doit être pris en compte.

J'ai créé ces données d'exemple et ce problème pour mieux comprendre l'apprentissage par renforcement et j'espère que vous le trouverez utile.

Merci d'avoir lu !

Sterling Osborne