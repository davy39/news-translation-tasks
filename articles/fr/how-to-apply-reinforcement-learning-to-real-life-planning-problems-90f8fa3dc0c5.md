---
title: Comment appliquer l'apprentissage par renforcement aux problèmes de planification
  de la vie réelle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-12T21:35:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-apply-reinforcement-learning-to-real-life-planning-problems-90f8fa3dc0c5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fFnWJvxZ1SITxjduEkIRmg.png
tags:
- name: beginner
  slug: beginner
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Reinforcement Learning
  slug: reinforcement-learning
- name: technology
  slug: technology
seo_title: Comment appliquer l'apprentissage par renforcement aux problèmes de planification
  de la vie réelle
seo_desc: 'By Sterling Osborne, PhD Researcher

  Recently, I have published some examples where I have created Reinforcement Learning
  models for some real life problems. For example, using Reinforcement Learning for
  Meal Planning based on a Set Budget and Persona...'
---

Par Sterling Osborne, Chercheur en doctorat

Récemment, j'ai publié quelques exemples où j'ai créé des modèles d'apprentissage par renforcement pour certains problèmes de la vie réelle. Par exemple, en utilisant [l'apprentissage par renforcement pour la planification des repas basée sur un budget fixe et des préférences personnelles](https://towardsdatascience.com/reinforcement-learning-for-meal-planning-based-on-meeting-a-set-budget-and-personal-preferences-9624a520cce4).

L'apprentissage par renforcement peut être utilisé de cette manière pour une variété de problèmes de planification, y compris les plans de voyage, la planification budgétaire et la stratégie commerciale. Les deux avantages de l'utilisation de l'apprentissage par renforcement sont qu'il prend en compte la probabilité des résultats et nous permet de contrôler certaines parties de l'environnement. Par conséquent, j'ai décidé d'écrire un exemple simple afin que d'autres puissent envisager comment ils pourraient commencer à l'utiliser pour résoudre certains de leurs problèmes quotidiens ou professionnels.

#### Qu'est-ce que l'apprentissage par renforcement ?

L'apprentissage par renforcement (RL) est le processus de test des actions qui sont les meilleures pour chaque état d'un environnement, essentiellement par essai et erreur. Le modèle introduit une politique aléatoire pour commencer, et chaque fois qu'une action est entreprise, une quantité initiale (connue sous le nom de récompense) est alimentée dans le modèle. Cela continue jusqu'à ce qu'un objectif final soit atteint, par exemple, vous gagnez ou perdez le jeu, où cette exécution (ou épisode) se termine et le jeu redémarre.

À mesure que le modèle traverse de plus en plus d'épisodes, il commence à apprendre quelles actions sont plus susceptibles de nous mener à un résultat positif. Par conséquent, il trouve les meilleures actions dans n'importe quel état donné, connues sous le nom de politique optimale.

![Image](https://cdn-media-1.freecodecamp.org/images/iRylN6xnM2dhQWN23vLuFMUiidpIPavDEQYE)
_Processus général de l'apprentissage par renforcement_

De nombreuses applications d'apprentissage par renforcement en ligne entraînent des modèles sur un jeu ou un environnement virtuel où le modèle peut interagir avec l'environnement de manière répétée. Par exemple, vous laissez le modèle jouer à une simulation de morpion encore et encore afin qu'il observe le succès et l'échec de l'essai de différents mouvements.

Dans la vie réelle, il est probable que nous n'ayons pas accès à entraîner notre modèle de cette manière. Par exemple, un système de recommandation dans les achats en ligne a besoin des commentaires d'une personne pour nous dire s'il a réussi ou non, et cela est limité en termes de disponibilité en fonction du nombre d'utilisateurs qui interagissent avec le site d'achat.

Au lieu de cela, nous pouvons avoir des données d'échantillon qui montrent les tendances d'achat sur une période de temps que nous pouvons utiliser pour créer des probabilités estimées. En utilisant celles-ci, nous pouvons créer ce qui est connu sous le nom de Processus de Décision de Markov Partiellement Observé (POMDP) comme moyen de généraliser la distribution de probabilité sous-jacente.

#### Processus de Décision de Markov Partiellement Observés (POMDPs)

Les Processus de Décision de Markov (MDPs) fournissent un cadre pour modéliser la prise de décision dans des situations où les résultats sont en partie aléatoires et en partie sous le contrôle d'un décideur. La caractéristique clé des MDPs est qu'ils suivent la Propriété de Markov ; tous les états futurs sont indépendants du passé étant donné le présent. En d'autres termes, la probabilité de passer à l'état suivant dépend uniquement de l'état actuel.

Les POMDPs fonctionnent de manière similaire sauf qu'il s'agit d'une généralisation des MDPs. En bref, cela signifie que le modèle ne peut pas simplement interagir avec l'environnement mais reçoit plutôt une distribution de probabilité donnée basée sur ce que nous avons observé. Plus d'informations peuvent être trouvées [ici](http://www.pomdp.org/tutorial/). Nous pourrions utiliser des méthodes d'itération de valeur sur notre POMDP, mais j'ai plutôt décidé d'utiliser l'apprentissage de Monte Carlo dans cet exemple.

### Environnement d'exemple

Imaginez que vous êtes de retour à l'école (ou peut-être que vous y êtes encore) et que vous êtes dans une salle de classe, l'enseignant a une politique stricte sur le gaspillage de papier et exige que tout morceau de papier de rebut **doit** être passé à lui à l'avant de la classe et il placera les déchets dans la poubelle.

Cependant, certains élèves de la classe se soucient peu des règles de l'enseignant et préféreraient se épargner la peine de faire passer le papier autour de la classe. Au lieu de cela, ces individus problématiques peuvent choisir de jeter le papier de rebut dans la poubelle à distance. Maintenant, cela met l'enseignant en colère et ceux qui font cela sont punis.

Cela introduit un concept très basique d'action-récompense, et nous avons un exemple d'environnement de salle de classe comme montré dans le diagramme suivant.

Notre objectif est de trouver les meilleures instructions pour chaque personne afin que le papier atteigne l'enseignant et soit placé dans la poubelle et évite d'être jeté dans la poubelle.

![Image](https://cdn-media-1.freecodecamp.org/images/IHXBDyRJ7C6BKFoubXntHGPyZaWwqgFKN4ly)

#### États et Actions

Dans notre environnement, chaque personne peut être considérée comme un **état** et elles ont une variété d'**actions** qu'elles peuvent entreprendre avec le papier de rebut. Elles peuvent choisir de le passer à un camarade de classe adjacent, de le garder ou certaines peuvent choisir de le jeter dans la poubelle. Nous pouvons donc mapper notre environnement à une disposition de grille plus standard comme montré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/AQHonaFnjleHXYU5YvrZw0nTjGAgaorMsobB)

Cela est conçu intentionnellement de sorte que chaque personne, ou état, ait quatre actions : haut, bas, gauche ou droite et chacune aura un résultat de "vie réelle" varié basé sur qui a pris l'action. Une action qui met la personne dans un mur (y compris le bloc noir au milieu) indique que la personne garde le papier. Dans certains cas, cette action est dupliquée, mais ce n'est pas un problème dans notre exemple.

Par exemple, les actions de la personne A résultent en :

* Haut = Jeter dans la poubelle
* Bas = Garder le papier
* Gauche = Passer à la personne B
* Droite = Garder le papier

### Environnement Probabiliste

Pour l'instant, le décideur qui contrôle partiellement l'environnement est nous. Nous allons dire à chaque personne quelle action elle doit prendre. Cela est connu sous le nom de **politique**.

Le premier défi auquel je suis confronté dans mon apprentissage est de comprendre que l'environnement est probablement probabiliste et ce que cela signifie. Un environnement probabiliste est lorsque nous instruisons un état à prendre une action sous notre politique, il y a une probabilité associée quant à savoir si cela est suivi avec succès. En d'autres termes, si nous disons à la personne A de passer le papier à la personne B, elle peut décider de ne pas suivre l'action instruite dans notre politique et plutôt jeter le papier de rebut dans la poubelle.

Un autre exemple est si nous recommandons des produits d'achat en ligne, il n'y a aucune garantie que la personne verra chacun d'eux.

#### Probabilités de Transition Observées

Pour trouver les probabilités de transition observées, nous devons collecter quelques données d'échantillon sur la manière dont l'environnement agit. Avant de collecter des informations, nous introduisons d'abord une politique initiale. Pour démarrer le processus, j'en ai choisi une au hasard qui semble mener à un résultat positif.

![Image](https://cdn-media-1.freecodecamp.org/images/XAfDzZytX9vrhxlhjhoCkezoOYRqOPJM0NUt)

Maintenant, nous observons les actions que chaque personne prend étant donné cette politique. En d'autres termes, disons que nous nous asseyons au fond de la classe et observons simplement la classe et observons les résultats suivants pour la personne A :

![Image](https://cdn-media-1.freecodecamp.org/images/-bldySGAig2zQknZl4Q6Ou6KroYpw62nhd7Y)
_Actions observées de la personne A_

Nous voyons qu'un papier est passé par cette personne 20 fois ; 6 fois elle l'a gardé, 8 fois elle l'a passé à la personne B et 6 autres fois elle l'a jeté à la poubelle. Cela signifie que sous notre politique initiale, la probabilité de garder ou de jeter à la poubelle pour cette personne est de 6/20 = 0,3 et de même 8/20 = 0,4 pour passer à la personne B. Nous pouvons observer le reste de la classe pour collecter les données d'échantillon suivantes :

![Image](https://cdn-media-1.freecodecamp.org/images/rLRsXRFIHwBZ956XoOmHNeNfqtSWP1Jjf36-)
_Résultat de vie réelle observé_

De même, nous calculons ensuite les probabilités pour obtenir la matrice suivante et nous pourrions utiliser cela pour simuler l'expérience. L'exactitude de ce modèle dépendra grandement du fait que les probabilités soient de vraies représentations de l'environnement entier. En d'autres termes, nous devons nous assurer que nous avons un échantillon suffisamment grand et riche en données.

![Image](https://cdn-media-1.freecodecamp.org/images/06wX9bX-2PCrssyTlgpObEvZAh9CPfeAO2I1)
_Fonction de probabilité de transition observée_

### Bandits Manchots Multi-Bras, Épisodes, Récompenses, Retour et Taux d'Actualisation

Nous avons donc nos probabilités de transition estimées à partir des données d'échantillon sous un POMDP. L'étape suivante, avant d'introduire des modèles, est d'introduire des récompenses. Jusqu'à présent, nous n'avons discuté que du résultat de l'étape finale ; soit le papier est placé dans la poubelle par l'enseignant et obtient une récompense terminale positive, soit il est jeté par A ou M et obtient une récompense terminale négative. Cette récompense finale qui met fin à l'épisode est connue sous le nom de **Récompense Terminale**.

Mais il y a aussi un troisième résultat qui est moins qu'idéal ; le papier continue à être passé et ne parvient jamais (ou prend beaucoup plus de temps que nous ne le souhaiterions) à atteindre la poubelle. Par conséquent, en résumé, nous avons trois résultats finaux :

* Le papier est placé dans la poubelle par l'enseignant et obtient une récompense terminale positive
* Le papier est jeté dans la poubelle par un élève et obtient une récompense terminale négative
* Le papier continue à être passé autour de la salle ou reste coincé sur les élèves pendant une période plus longue que nous ne le souhaiterions

Pour éviter que le papier ne soit jeté dans la poubelle, nous lui attribuons une récompense négative importante, disons -1, et parce que l'enseignant est satisfait qu'il soit placé dans la poubelle, cela obtient une récompense positive importante, +1. Pour éviter le résultat où il continue à être passé autour de la salle, nous fixons la récompense pour toutes les autres actions à une valeur négative faible, disons -0,04.

Si nous fixons cela comme un nombre positif ou nul, le modèle pourrait laisser le papier tourner en rond car il serait préférable de gagner de petits positifs plutôt que de risquer de se rapprocher du résultat négatif. Ce nombre est également très petit car il ne collectera qu'une seule récompense terminale mais pourrait prendre de nombreuses étapes pour mettre fin à l'épisode et nous devons nous assurer que, si le papier est placé dans la poubelle, le résultat positif n'est pas annulé.

Veuillez noter : les récompenses sont toujours relatives les unes aux autres et j'ai choisi des chiffres arbitraires, mais ceux-ci peuvent être modifiés si les résultats ne sont pas ceux souhaités.

Bien que nous ayons involontairement discuté des épisodes dans l'exemple, nous n'avons pas encore défini formellement cela. **Un épisode est simplement les actions que chaque papier prend à travers la salle de classe pour atteindre la poubelle, qui est l'état terminal et met fin à l'épisode**. Dans d'autres exemples, comme jouer au morpion, cela serait la fin d'un jeu où vous gagnez ou perdez.

Le papier pourrait en théorie commencer dans n'importe quel état et cela introduit pourquoi nous avons besoin de suffisamment d'épisodes pour nous assurer que chaque état et action est testé suffisamment afin que notre résultat ne soit pas entraîné par des résultats invalides. Cependant, d'un autre côté, plus nous introduisons d'épisodes, plus le temps de calcul sera long et, selon l'échelle de l'environnement, nous n'avons peut-être pas une quantité illimitée de ressources pour le faire.

Cela est connu sous le nom de **problème du bandit manchot multi-bras** ; avec un temps fini (ou d'autres ressources), nous devons nous assurer que nous testons chaque paire état-action suffisamment pour que les actions sélectionnées dans notre politique soient, en fait, les meilleures. En d'autres termes, nous devons valider que les actions qui nous ont menés à de bons résultats dans le passé ne sont pas dues à la chance pure mais sont en fait le bon choix, et de même pour les actions qui semblent mauvaises. Dans notre exemple, cela peut sembler simple avec le peu d'états que nous avons, mais imaginez si nous augmentions l'échelle et comment cela devient de plus en plus un problème.

L'objectif global de notre modèle d'apprentissage par renforcement est de sélectionner les actions qui maximisent les récompenses cumulatives attendues, connues sous le nom de retour. En d'autres termes, le **Retour** est simplement la récompense totale obtenue pour l'épisode. Une manière simple de calculer cela serait d'additionner toutes les récompenses, y compris la récompense terminale, dans chaque épisode.

Une approche plus rigoureuse consiste à considérer que les premières étapes sont plus importantes que les suivantes dans l'épisode en appliquant un facteur d'actualisation, gamma, dans la formule suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/N9nsFXRGlZtH0oKXLmdrBEIeN8fbumhvOIob)

En d'autres termes, nous additionnons toutes les récompenses mais réduisons les étapes ultérieures d'un facteur gamma à la puissance du nombre d'étapes qu'il a fallu pour les atteindre.

Si nous pensons à notre exemple, l'utilisation d'un retour actualisé devient encore plus claire à imaginer car l'enseignant récompensera (ou punira en conséquence) quiconque a été impliqué dans l'épisode mais ajustera cela en fonction de leur distance par rapport au résultat final.

Par exemple, si le papier passe de A à B à M qui le jette dans la poubelle, M devrait être puni le plus, puis B pour l'avoir passé à lui et enfin la personne A qui est encore impliquée dans le résultat final mais moins que M ou B. Cela souligne également que plus cela prend du temps (basé sur le nombre d'étapes) pour commencer dans un état et atteindre la poubelle, moins cela sera récompensé ou puni mais accumulera des récompenses négatives pour avoir pris plus d'étapes.

### Application d'un Modèle à notre Exemple

Comme notre environnement d'exemple est petit, nous pouvons appliquer chacun et montrer certains des calculs effectués manuellement et illustrer l'impact du changement de paramètres.

Pour tout algorithme, nous devons d'abord initialiser la fonction de valeur d'état, V(s), et avons décidé de définir chacune d'entre elles à 0 comme montré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/7zOfCiGWw6rsZ1teuxam57csTdFrYQtGrSqm)

Ensuite, nous laissons le modèle simuler l'expérience sur l'environnement basé sur notre distribution de probabilité observée. Le modèle commence un morceau de papier dans des états aléatoires et les résultats de chaque action sous notre politique sont basés sur nos probabilités observées. Par exemple, disons que nous avons les trois premiers épisodes simulés comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/b7jWB92ntwLYkqvYVuwAX59qd2nWRWMzGfPO)

![Image](https://cdn-media-1.freecodecamp.org/images/713X0b-2rPNLGnpEknBRVnVqgSwhj74fRPrd)

![Image](https://cdn-media-1.freecodecamp.org/images/EHE-LpztkPVMWIpKW2vJ8tpbVPP4xoHmfPRO)

Avec ces épisodes, nous pouvons calculer nos premières mises à jour de notre fonction de valeur d'état en utilisant chacun des trois modèles donnés. Pour l'instant, nous choisissons des valeurs arbitraires alpha et gamma à 0,5 pour simplifier nos calculs manuels. Nous montrerons plus tard l'impact que cette variable a sur les résultats.

Tout d'abord, nous appliquons la différence temporelle 0, le plus simple de nos modèles et les trois premières mises à jour de valeur sont les suivantes :

![Image](https://cdn-media-1.freecodecamp.org/images/PcrATwyOJ0aodrgmnjjQ1dUgfcaNso-YiXF2)

Alors, comment ces valeurs ont-elles été calculées ? Eh bien, parce que notre exemple est petit, nous pouvons montrer les calculs à la main.

![Image](https://cdn-media-1.freecodecamp.org/images/tvkHihHu-5zyh8WehUYJcpwkHKWb8MN3gIgk)

![Image](https://cdn-media-1.freecodecamp.org/images/yslW70VU1RLb3o7djaPCHPdw4kMiY1BBXibE)

![Image](https://cdn-media-1.freecodecamp.org/images/jcB4CtCcI7WNSTmFdt9aWlXXohBbZgjAqrQP)

Alors, que pouvons-nous observer à ce stade précoce ? Tout d'abord, l'utilisation de TD(0) semble injuste pour certains états, par exemple la personne D, qui, à ce stade, n'a rien gagné du fait que le papier atteint la poubelle deux fois sur trois. Leur mise à jour n'a été affectée que par la valeur de l'étape suivante, mais cela souligne comment les récompenses positives et négatives se propagent vers l'extérieur à partir du coin vers les états.

À mesure que nous prenons plus d'épisodes, les récompenses terminales positives et négatives se répandraient de plus en plus sur tous les états. Cela est montré grossièrement dans le diagramme ci-dessous où nous pouvons voir que les deux épisodes qui ont abouti à un résultat positif impactent la valeur des états Enseignant et G tandis que le seul épisode négatif a puni la personne M.

![Image](https://cdn-media-1.freecodecamp.org/images/utemVff2wrMbdDOJo5PJbFSNhrhW7fPGgrj4)

Pour montrer cela, nous pouvons essayer plus d'épisodes. Si nous répétons les trois mêmes chemins déjà donnés, nous produisons la fonction de valeur d'état suivante :

**(Veuillez noter, nous avons répété ces trois épisodes pour simplifier dans cet exemple mais le modèle réel aurait des épisodes où les résultats sont basés sur la fonction de probabilité de transition observée.)**

![Image](https://cdn-media-1.freecodecamp.org/images/RxDrPSqVzJqwwxEnQD-KXMtr1iXcPLWuhq9x)

![Image](https://cdn-media-1.freecodecamp.org/images/OMdszq1WLV91uHDHGPDAfySfuK35uoi8ieyu)

Le diagramme ci-dessus montre les récompenses terminales se propageant vers l'extérieur à partir du coin supérieur droit vers les états. À partir de cela, nous pouvons décider de mettre à jour notre politique car il est clair que la récompense terminale négative passe par la personne M et donc B et C sont impactés négativement. Par conséquent, basé sur V27, pour chaque état nous pouvons décider de mettre à jour notre politique en sélectionnant la meilleure valeur d'état suivante pour chaque état comme montré dans la figure ci-dessous

![Image](https://cdn-media-1.freecodecamp.org/images/BcBG9YpaPUC7JVm9Z6hvJBZVCaCnyUKbHoSe)

Il y a deux raisons de s'inquiéter dans cet exemple : la première est que la meilleure action de la personne A est de le jeter dans la poubelle et d'obtenir une récompense négative. Cela est dû au fait qu'aucun des épisodes n'a visité cette personne et souligne le problème du bandit manchot multi-bras. Dans cet exemple, il y a très peu d'états, donc il faudrait de nombreux épisodes pour les visiter tous, mais nous devons nous assurer que cela est fait.

La raison pour laquelle cette action est meilleure pour cette personne est que ni l'un ni l'autre des états terminaux n'ont de valeur mais plutôt les résultats positifs et négatifs sont dans les récompenses terminales. Nous pourrions alors, si notre situation l'exigeait, initialiser V0 avec des chiffres pour les états terminaux basés sur les résultats.

Deuxièmement, la valeur d'état de la personne M oscille entre -0,03 et -0,51 (environ) après les épisodes et nous devons aborder pourquoi cela se produit. Cela est causé par notre taux d'apprentissage, alpha. Pour l'instant, nous n'avons introduit que nos paramètres (le taux d'apprentissage alpha et le taux d'actualisation gamma) mais n'avons pas expliqué en détail comment ils impacteront les résultats.

Un taux d'apprentissage élevé peut faire osciller les résultats, mais inversement, il ne doit pas être si petit qu'il prend une éternité à converger. Cela est montré plus loin dans la figure ci-dessous qui démontre le V(s) total pour chaque épisode et nous pouvons clairement voir comment, bien qu'il y ait une tendance générale à la hausse, il diverge d'avant en arrière entre les épisodes. Une autre bonne explication pour le taux d'apprentissage est la suivante :

« Dans le jeu de golf, lorsque la balle est loin du trou, le joueur la frappe très fort pour se rapprocher le plus possible du trou. Plus tard, lorsqu'il atteint la zone marquée par un drapeau, il choisit un autre bâton pour obtenir un coup court précis.

Ce n'est pas qu'il ne pourra pas mettre la balle dans le trou sans choisir le bâton de coup court, il pourrait envoyer la balle au-delà de la cible deux ou trois fois. Mais ce serait mieux s'il jouait de manière optimale et utilisait la bonne quantité de puissance pour atteindre le trou. »

[**Taux d'apprentissage d'un agent Q-learning**](https://stackoverflow.com/questions/33011825/learning-rate-of-a-q-learning-agent)  
[_La question de savoir comment le taux d'apprentissage influence le taux de convergence et la convergence elle-même. Si le taux d'apprentissage est..._stackoverflow.com](https://stackoverflow.com/questions/33011825/learning-rate-of-a-q-learning-agent)

![Image](https://cdn-media-1.freecodecamp.org/images/picYFGSsrMSt1g88c09UBjtYQyA0vbsUXyjy)
_Épisode_

Il existe des méthodes complexes pour établir le taux d'apprentissage optimal pour un problème, mais, comme pour tout algorithme d'apprentissage automatique, si l'environnement est suffisamment simple, vous itérez sur différentes valeurs jusqu'à ce que la convergence soit atteinte. Cela est également connu sous le nom de descente de gradient stochastique. Dans un [projet récent de RL](https://towardsdatascience.com/creating-interactive-animation-for-parameter-optimisation-using-plot-ly-8136b2997db), j'ai démontré l'impact de la réduction d'alpha en utilisant une visualisation animée et cela est montré ci-dessous. Cela démontre l'oscillation lorsque alpha est grand et comment cela devient lissé à mesure que alpha est réduit.

![Image](https://cdn-media-1.freecodecamp.org/images/BR2fyHlcGvxCmCXSl1k-2QTjidKbM5n4S6tn)

De même, nous devons également avoir notre taux d'actualisation compris entre 0 et 1, souvent ce nombre est pris proche de 0,9. Le facteur d'actualisation nous indique à quel point les récompenses futures sont importantes ; un nombre élevé indique qu'elles seront considérées comme importantes, tandis que le rapprocher de 0 fera que le modèle considérera les étapes futures de moins en moins.

Avec ces deux éléments à l'esprit, nous pouvons changer alpha de 0,5 à 0,2 et gamma de 0,5 à 0,9 et nous obtenons les résultats suivants :

![Image](https://cdn-media-1.freecodecamp.org/images/seJwoVJfEbz2ckQLq9nZXrMbLMDhQvj5eYgY)

Parce que notre taux d'apprentissage est maintenant beaucoup plus petit, le modèle prend plus de temps à apprendre et les valeurs sont généralement plus petites. Le plus notable est pour l'enseignant qui est clairement le meilleur état. Cependant, ce compromis pour un temps de calcul accru signifie que notre valeur pour M n'oscille plus dans la mesure où elle l'était auparavant. Nous pouvons maintenant voir cela dans le diagramme ci-dessous pour la somme de V(s) suivant nos paramètres mis à jour. Bien qu'il ne soit pas parfaitement lisse, le V(s) total augmente lentement à un rythme beaucoup plus fluide qu'avant et semble converger comme nous le souhaitons mais nécessite environ 75 épisodes pour le faire.

![Image](https://cdn-media-1.freecodecamp.org/images/BSscIv0WdzkFPYZN9wd97CvJoWdxMT5loprq)

### Changer le Résultat Objectif

Un autre avantage crucial de l'apprentissage par renforcement que nous n'avons pas mentionné en détail est que nous avons un certain contrôle sur l'environnement. Actuellement, les récompenses sont basées sur ce que nous avons décidé être le meilleur pour amener le modèle à atteindre le résultat positif en aussi peu d'étapes que possible.

Cependant, disons que l'enseignant a changé et que le nouveau ne se souciait pas que les élèves jettent le papier dans la poubelle tant qu'il y arrivait. Alors nous pourrions changer notre récompense négative autour de cela et la politique optimale changera.

Cela est particulièrement utile pour les solutions commerciales. Par exemple, disons que vous planifiez une stratégie et savez que certaines transitions sont moins souhaitées que d'autres, alors cela peut être pris en compte et changé à volonté.

### Conclusion

Nous avons maintenant créé un modèle simple d'apprentissage par renforcement à partir de données observées. Il y a beaucoup de choses qui pourraient être améliorées ou approfondies, y compris l'utilisation d'un modèle plus complexe, mais cela devrait être une bonne introduction pour ceux qui souhaitent essayer et appliquer à leurs propres problèmes de la vie réelle.

J'espère que vous avez apprécié la lecture de cet article, si vous avez des questions, n'hésitez pas à commenter ci-dessous.

Merci

Sterling