---
title: Apprenez l'analyse de données par vous-même en 30 jours
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-06-16T17:19:31.000Z'
originalURL: https://freecodecamp.org/news/teach-yourself-data-analytics-in-30-days
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/dataanalytics.png
tags:
- name: data analytics
  slug: data-analytics
- name: youtube
  slug: youtube
seo_title: Apprenez l'analyse de données par vous-même en 30 jours
seo_desc: "You can learn the basics of Data Analytics with 30 days of practice. \n\
  We just released a Data Analytics course on the freeCodeCamp.org YouTube channel.\
  \ The course includes a 40-minute video, as well as a website and Jupyter notebooks.\
  \ If you follow t..."
---

Vous pouvez apprendre les bases de l'analyse de données avec 30 jours de pratique. 

Nous venons de publier un cours d'analyse de données sur la chaîne YouTube freeCodeCamp.org. Le cours comprend une vidéo de 40 minutes, ainsi qu'un site web et des notebooks Jupyter. Si vous suivez le plan décrit dans ces ressources de cours, vous pouvez apprendre l'analyse de données en 30 jours.

David Clinton a développé ce cours. David a écrit de nombreux livres techniques populaires et créé de nombreux cours vidéo utiles.

Le cours vise à être une introduction rapide et efficace à l'analyse de données basée sur Python. L'objectif est d'amener les utilisateurs ayant une compréhension de base du fonctionnement de Python au point où ils peuvent trouver et manipuler des sources de données en toute confiance et utiliser un environnement Jupyter pour tirer des insights de leurs données. Le cours démontrera des méthodes d'analyse efficaces, mais ne cherche pas à être exhaustif. 

Le seul prérequis pour le cours est une compréhension de base de la programmation Python, ou au moins de la manière dont la programmation fonctionne en général. 

Voici les principaux sujets abordés dans ce cours :

* Installation de Python et Jupyter 
* Travail avec l'environnement Jupyter
* Trouver des sources de données et utiliser des API
* Travailler avec des données 
* Tracer des données 
* Comprendre les données

Vous pouvez regarder le cours complet ci-dessous ou [sur la chaîne YouTube freeCodeCamp.org](https://www.youtube.com/watch?v=jcTj6FgWOpo).

Assurez-vous de consulter également le site web accompagnant : [https://stories.thedataproject.net/](https://stories.thedataproject.net/)

%[https://www.youtube.com/watch?v=jcTj6FgWOpo]

### Transcription complète

(remarque : autogénérée)

David Clinton a écrit et créé de nombreux livres techniques populaires et cours vidéo.

Ce cours d'analyse de données, ainsi que le site web accompagnant et les notebooks Jupyter, vous aideront à apprendre l'analyse de données en 30 jours.

Bienvenue dans mon cours, je suis vraiment heureux de vous avoir ici.

Et je suis encore plus heureux que vous ayez décidé de rejoindre la fête de l'analyse de données.

Qui suis-je ? Je suis l'auteur de plus d'une douzaine de livres sur l'administration Linux et AWS, la sécurité numérique, et des dizaines de cours sur Pluralsight.

J'ai également une poignée d'articles ici même sur le site d'actualités de Free Code Camp.

Mais je n'écris que sur des sujets.

Espérons que, lorsque vous aurez terminé ce contenu, vous serez en train d'utiliser des données pour changer le monde.

Puisque vous avez déjà vu ma déclaration selon laquelle cela ne vous prendra que 30 jours, je devrais expliquer ce que cela va réellement vous montrer : les outils dont vous aurez besoin pour trouver et manipuler des données brutes, et utiliser divers outils de graphique pour vous aider à comprendre et interpréter ces données.

Mais ne vous attendez pas à ce que nous couvions un programme complet de science des données ici, complet avec le calcul à une et plusieurs variables, la résolution algorithmique de problèmes, ou même l'apprentissage automatique.

Cela nécessiterait beaucoup plus de temps et d'efforts.

Si c'est ce que vous recherchez, consultez le nouveau contenu de science des données que Free Code Camp est en train de mettre en ligne, il y a autre chose que vous n'obtiendrez pas de ces vidéos : l'expérience.

Une fois que vous aurez regardé l'ensemble du cours, vous ne pourrez probablement toujours pas faire grand-chose par vous-même.

La valeur de l'expérience pratique réelle réside dans les erreurs que vous faites, vous savez, les erreurs de syntaxe, ne pas comprendre correctement ce que fait votre code, ou ne pas tenir compte des restrictions spécifiques à l'environnement.

Diagnostiquer et travailler à travers ces erreurs est là où vous commencerez vraiment à prendre les choses en main et à accomplir de grandes choses.

Alors, où obtiendrez-vous cette expérience ? Si vous êtes ambitieux et que vous avez des idées de projets passionnants, par tous les moyens, plongez-vous et essayez.

Mais si vous pensez avoir encore besoin de conseils, alors j'ai tout ce dont vous avez besoin sur mon site stories.thedataproject.net, vous pouvez travailler à travers les exercices dans chacune des huit histoires de données que vous trouverez là-bas.

Si vous recherchez une compétence spécifique, l'index des objectifs d'apprentissage ici vous dirigera directement vers le chapitre où vous le trouverez, tout cela est disponible pour tous et gratuitement.

Si vous préférez travailler avec un vrai livre, vous pouvez acheter le même contenu dans ce format.

Mais ne pensez pas que quelque chose manque sur le site web gratuit. Mais pour l'instant, parlons des outils d'analyse de données.

Il existe de nombreuses façons de consommer des données, celle que vous choisissez reflétera vos besoins spécifiques et votre confort avec diverses compétences.

Les tableurs, comme vous le savez probablement déjà, sont bien plus que de simples calculatrices sophistiquées ou des endroits pour garder vos chiffres de budget familial.

Ils viennent également avec des fonctions puissantes, des intégrations externes et des capacités de graphique.

Des outils de force entreprise comme Tableau, Splunk ou Microsoft Power BI sont également excellents pour traiter des chiffres et visualiser des insights, que vous pouvez ensuite partager avec les membres de votre équipe.

Alors, quel est le grand avantage de Python ? Eh bien, l'écosystème Python est beaucoup, beaucoup plus large que ces outils construits à des fins spécifiques.

Et la communauté Python met à disposition toutes sortes de bibliothèques et modules utiles spécifiques aux données.

Lorsque vous laissez Python libre contre vos données.

Vous avez toutes les ressources d'un langage de programmation industriel complet à portée de main.

Ce n'est pas ce que vous pouvez faire avec.

C'est trouver quelque chose que vous ne pouvez pas faire.

D'accord, mais qu'en est-il de Jupiter ? Jupiter est une plateforme open source dans laquelle vous pouvez charger vos données et exécuter votre code Python.

C'est un peu comme un environnement de développement intégré comme Microsoft Visual Studio.

Et bien que les notebooks Jupyter puissent être utilisés avec un nombre croissant de langages et pour autant de tâches que vous pouvez imaginer, ils sont surtout connus et aimés comme un hôte pour les exploits de données Python.

Il fut un temps où les lignes de code que vous écriviez pour vos programmes étaient enregistrées dans un seul fichier texte dont le nom se terminait par un suffixe .py.

Lorsque vous vouliez exécuter votre code pour voir comment les choses se passaient.

Vous le faisiez à partir de la ligne de commande ou d'un éditeur de code source puissant et compliqué comme Visual Studio.

Mais pour que quelque chose fonctionne, tout devait fonctionner.

Cela rendrait plus difficile le dépannage lorsque quelque chose ne se passait pas selon les spécifications.

Mais cela rendrait également beaucoup plus difficile de jouer avec des détails spécifiques juste pour voir ce qui se passe.

Et cela rendait également difficile le partage de versions en direct de votre code sur Internet.

Comme nous le verrons bientôt, les notebooks Jupyter vous permettent d'exécuter votre code une ligne à la fois, ou entièrement.

Cette flexibilité facilite la compréhension de votre code et, lorsque les choses tournent mal, le dépannage.

Les notebooks, soit dit en passant, sont des fichiers basés sur JSON qui déplacent effectivement l'environnement de traitement pour à peu près n'importe quel code de programmation orienté données de votre serveur ou station de travail vers votre navigateur web.

Vous pouvez télécharger Jupiter sur votre PC ou un serveur privé et accéder à l'interface via n'importe quel navigateur avec accès réseau.

Ou vous pouvez exécuter des notebooks sur des services d'hébergement tiers comme Google Colab, ou pour un coût, des fournisseurs de cloud comme Amazon SageMaker Studio Notebooks, ou Microsoft Azure Notebooks.

Jupiter existe en trois versions.

Les deux que vous êtes le plus susceptible de rencontrer sont les notebooks classiques et le nouveau Jupiter Lab.

Les deux fonctionnent bien dans votre navigateur.

Mais Jupiter Lab vient avec plus d'extensions et vous permet de travailler avec plusieurs fichiers de notebooks et un accès terminal dans un seul onglet de navigateur.

J'utiliserai l'environnement de notebook classique pour les démonstrations de ce cours, mais il n'y a généralement aucun problème à transférer des notebooks entre les versions.

Le troisième, pour être complet, est Jupiter Hub.

Une version serveur construite pour fournir un accès authentifié aux notebooks à plusieurs utilisateurs, vous pouvez servir jusqu'à 100 utilisateurs ou plus à partir d'un seul serveur cloud en utilisant le plus petit Jupiter Hub.

Pour des déploiements plus importants impliquant des clusters de serveurs, il serait probablement préférable d'utiliser une version Kubernetes connue sous le nom de Zero to Jupiter Hub avec Kubernetes.

Mais tout cela est bien au-delà de la portée de ce cours.

Notre prochaine tâche est de construire notre environnement de travail.

En supposant que vous avez décidé d'héberger Jupiter sur votre propre machine, vous aurez besoin de Python installé.

La bonne nouvelle est que la plupart des systèmes d'exploitation viennent avec Python préinstallé, vous pouvez confirmer que vous avez une version à jour de Python en ouvrant une invite de commande et en tapant Python --version ou parfois Python3 --version, si Python est installé, vous verrez probablement quelque chose comme ceci.

Assurez-vous simplement que vous avez Python 3 installé et non l'ancien et non sécurisé Python 2.

Si vous devez installer Python manuellement, vous feriez mieux d'utiliser la documentation officielle de Python, qui sera la source la plus complète et à jour disponible, compatible avec le système d'exploitation que vous utilisez.

Il est important de noter que toutes les versions de Python, même celles de la série 3.x, ne se comporteront pas nécessairement exactement comme vous l'attendez.

Vous pourriez, par exemple, constater que vous avez besoin d'une bibliothèque écrite pour la version 3.9.

Mais qu'il n'y a aucun moyen de la faire fonctionner sur votre système 3.7.

Mettre à niveau votre version système vers 3.9 pourrait bien fonctionner pour vous.

Mais cela pourrait également entraîner des conséquences inattendues et désagréables.

Il est difficile de savoir quand une bibliothèque Python particulière pourrait également être nécessaire à votre système d'exploitation principal.

Si vous retirez la version originale de la bibliothèque, vous pourriez finir par désactiver le système d'exploitation lui-même.

Et ne pensez pas que cela n'arrivera pas.

J'ai moi-même endommagé mon système d'exploitation de cette manière il y a quelques mois à peine.

Une solution consiste à exécuter Python pour votre projet dans un environnement virtuel spécial isolé de votre système d'exploitation principal.

De cette façon, vous pouvez installer toutes les bibliothèques et versions que vous souhaitez sans avoir à vous soucier d'endommager votre système de travail.

Vous pouvez le faire en utilisant un conteneur virtuel à grande échelle exécutant une image Docker ou, comme je préfère, LXD, ou sur une instance cloud AWS autonome.

Mais vous pouvez également utiliser le module venv de Python, vous voulez lire la documentation officielle pour les instructions spécifiques à l'environnement virtuel de votre système d'exploitation hôte.

Quelle que soit la version de Jupiter que vous choisissez, si vous décidez de l'installer et de l'exécuter localement, le projet Jupiter recommande officiellement de le faire via la distribution Python Anaconda et son gestionnaire de paquets binaires conda.

Différents guides pour le faire sont disponibles pour divers systèmes d'exploitation hôtes, mais cette page officielle est un bon point de départ.

Comme vous pouvez le voir, le gestionnaire de paquets Python PIP est également une option.

Une fois tout cela terminé, vous devriez pouvoir ouvrir un notebook directement dans votre navigateur et vous mettre immédiatement au travail.

Pour moi, la fonctionnalité la plus puissante d'un notebook est la manière dont vous pouvez exécuter des sous-ensembles de votre code dans des cellules individuelles.

Cela facilite la décomposition de programmes longs et complexes en extraits facilement lisibles et exécutables.

Avec une cellule sélectionnée.

Cliquer sur le bouton Exécuter exécutera uniquement le code de cette cellule.

Remarquez comment la boîte à gauche obtient un numéro représentant la position séquentielle de l'exécution.

À mesure que vous deviendrez plus familier avec Jupiter, vous prendrez probablement l'habitude d'exécuter des cellules en utilisant Ctrl et Entrée plutôt qu'un clic de souris, vous pouvez insérer une nouvelle cellule juste après celle qui est actuellement sélectionnée en cliquant sur le bouton plus.

Les flèches haut et bas déplacent les cellules comme vous pourriez vous y attendre, haut et bas.

Les cellules, par défaut, sont formatées pour gérer le code, Python 3 dans mon cas, mais elles peuvent également être définies pour le markdown, ce qui peut être pratique pour documenter vos notebooks, ou rendre les nouvelles sections plus faciles à trouver.

Un seul hashtag en markdown, par exemple, représente un titre de sélection de niveau supérieur, l'exécution de la cellule imprimera le texte pour correspondre à votre instruction de formatage.

Les emplacements précis et l'apparence des boutons que vous utiliserez pour faire tout cela varieront entre les différentes versions de Jupiter, mais toutes les fonctions de base sont universellement disponibles.

Quelles que soient les valeurs que votre code crée, elles resteront dans la mémoire du noyau jusqu'à ce que la sortie d'une cellule particulière ou pour l'ensemble du noyau soit effacée.

Cela vous permet de réexécuter des cellules précédentes ou suivantes pour voir quel impact le changement pourrait avoir.

Cela signifie également que la réinitialisation de votre environnement pour un nouveau départ complet est aussi simple que de sélectionner redémarrer le noyau et effacer toutes les sorties.

Toutes les fonctionnalités de Python ne seront pas disponibles dès le départ.

Parfois, comme vous l'avez vu juste avant, vous devrez dire à Python de charger un ou plusieurs modules via des déclarations dans votre code.

Mais certains modules doivent être installés manuellement à partir de la ligne de commande de l'hôte avant de pouvoir être importés.

Pour de tels cas, Python recommande leur programme d'installation Pip, ou dans certains cas, l'outil conda de la distribution Anaconda.

Vous pouvez en savoir plus sur l'utilisation de PIP pour l'entretien et l'alimentation appropriés de votre système Python dans le site de documentation utile de Python.

D'accord, voici où nous commençons le vrai travail.

Nous allons nous rendre sur Internet pour trouver des données fiables qui nous aideront à répondre à une question du monde réel.

Et nous utiliserons une API publique pour obtenir les données.

Ensuite, nous examinerons les données pour avoir une idée de leur formatage actuel et de ce qu'il faudra pour les corriger.

Après avoir appliqué le formatage nécessaire, afin que notre code puisse les lire facilement, nous fusionnerons plusieurs ensembles de données pour pouvoir rechercher des corrélations, puis nous expérimenterons avec des outils de graphique pour trouver celui qui représente nos données de la manière la plus intelligible.

Quel est le problème que nous essayons de résoudre ? Je suis curieux de voir si les salaires versés aux travailleurs américains au cours des 20 dernières années ont, en moyenne, augmenté, en supposant qu'ils ont augmenté, j'aimerais également savoir si l'argent supplémentaire dans leurs poches a également augmenté leur niveau de vie réel ? Pour répondre à ces questions, nous allons accéder à deux ensembles de données collectés et maintenus par le Bureau of Labor Statistics du gouvernement américain.

L'une des nombreuses choses agréables à propos du Bureau of Labor Statistics, généralement appelé BLS, est qu'ils fournissent une API pour l'accès depuis nos scripts Python.

Pour que cela fonctionne, vous devez connaître l'adresse de l'endpoint BLS correspondant à la série de données spécifique dont vous avez besoin pour que le code Python initie la demande, et pour les demandes de volume plus élevé, une clé API BLS.

L'obtention des adresses des endpoints de série dont vous avez besoin peut nécessiter quelques recherches sur le site web du BLS.

Cependant, les ensembles de données les plus populaires sont accessibles via une seule page.

Cela vous montre à quoi cela ressemble, y compris les codes d'endpoint comme lns, un un et beaucoup de zéros pour la population active civile, vous pouvez également rechercher des ensembles de données sur cette page.

La recherche d'un ordinateur, par exemple, vous mènera à une liste qui inclut le salaire horaire moyen tentant pour les occupations informatiques et mathématiques de niveau 11 à Austin, Round Rock, Texas.

Les informations que vous découvrirez en développant cette sélection incluront son ID de série, qui est le point de terminaison car je sais que vous pouvez à peine contenir votre curiosité.

Je cliquerai et vous montrerai qu'il s'avère que les professions informatiques et mathématiques de niveau 11 à Austin, Round Rock, Texas, pouvaient s'attendre à gagner 51,76 $ de l'heure en 2019.

Alors, comment transformer ces ID de série en données compatibles avec Python ? Écrire manuellement des requêtes get et put peut être très fastidieux, et il faudra de nombreuses tentatives avant d'obtenir exactement ce qu'il faut.

Pour éviter tout cela, j'ai décidé d'utiliser une bibliothèque Python tierce appelée BLS.

qui est disponible via le dépôt GitHub de notre partage de roses, vous installez la bibliothèque sur votre machine hôte, en utilisant pip install BLS.

C'est tout ce qu'il faudra.

Pendant que nous sommes ici, nous pourrions aussi bien activer notre clé API BLS.

Vous vous inscrivez pour l'API à partir de cette page, et ils vous enverront un e-mail avec votre clé et une URL de validation sur laquelle vous devrez cliquer.

Une fois que vous avez votre clé, vous l'exportez vers l'environnement de votre système sur Linux ou Mac OS, cela signifierait exécuter quelque chose comme ceci, où votre clé est substituée à la fausse que j'utilise ici, je vais utiliser l'API pour demander l'indice des prix à la consommation des États-Unis, IPC, et les statistiques sur les salaires entre 2002 et 2020.

L'IPC est une mesure du prix d'un panier de biens de consommation essentiels.

C'est un indicateur important des changements du coût de la vie, qui à son tour est un indicateur de la santé générale de l'économie.

Nos données sur les salaires proviendront de l'indice des coûts d'emploi du BLS, couvrant les salaires et les salaires des travailleurs de l'industrie privée dans tous les secteurs et professions.

Un indice d'emploi en croissance suggérerait à première vue que les choses s'améliorent pour la plupart des gens.

Cependant, voir les tendances moyennes des salaires de l'emploi de manière isolée n'est pas très utile.

Après tout, le salaire le plus élevé ne vous sera pas très utile si vos dépenses de base sont encore plus élevées.

L'objectif est donc de tirer à la fois les ensembles de données IPC et salaires, puis de les corrélier à la recherche de motifs.

Cela nous montrera comment les salaires ont évolué par rapport aux coûts.

Maintenant, laissez-moi vous montrer comment cela fonctionne réellement.

Avec des endpoints valides pour les deux ensembles de données que nous allons utiliser, nous sommes prêts à commencer à creuser pour l'IPC et l'or de l'emploi.

L'importation de ces quatre bibliothèques, y compris BLS, nous donnera tous les outils dont nous aurons besoin.

pandas signifie Python pour l'analyse de données, qui est une bibliothèque pour travailler avec des données sous forme de data frames.

Les data frames sont peut-être la structure la plus importante que vous utiliserez lorsque vous apprendrez à traiter de grands ensembles de données.

NumPy est une bibliothèque pour exécuter des fonctions mathématiques sur de grands tableaux de données.

Et matplotlib est une bibliothèque pour tracer des données dans des graphiques visuels de divers types.

Lors de l'importation d'une bibliothèque, vous lui attribuez le nom que vous utiliserez pour l'invoquer.

Vous pouvez choisir à peu près n'importe quoi, mais pandas est souvent représenté par PD, NumPy par NP et matplotlib par PLT. J'importe également la bibliothèque BLS que nous avons installée un peu plus tôt, qui sera invoquée en utilisant son nom réel, BLS.

J'exécuterai cette cellule.

Maintenant, je passe l'endpoint BLS pour la série de données IPC à la commande BLS get series de la bibliothèque BLS.

Le code de l'endpoint lui-même a bien sûr été copié depuis la page des ensembles de données populaires sur le site web du BLS. J'assignerai la série de données qui revient à un data frame en utilisant la variable CPI, puis j'enregistrerai le data frame dans un fichier CSV local.

Ce n'est pas nécessaire, mais vous pourriez trouver plus facile de travailler avec les données lorsqu'elles sont enregistrées localement.

Ensuite, je chargerai les données depuis le nouveau fichier CSV en utilisant la commande pan das PD read CSV contre le nom du fichier.

J'assignerai le nom de variable CPI data au nouveau data frame qui sort de l'autre extrémité.

Exécuter simplement CPI data imprimera les cinq premières et dernières lignes du data frame.

La colonne de date contient des valeurs de mois et d'année.

Et la deuxième colonne contient nos données réelles.

J'aimerais simplifier les en-têtes pour les rendre plus faciles à utiliser.

Je vais donc utiliser l'attribut des colonnes pan das, je préfère définitivement cette méthode.

Cependant, nous devrons également voir les données sur les salaires pour savoir si le format utilisé est compatible avec notre ensemble CPI.

Je vais donc extraire la série de données sur les salaires en utilisant la bibliothèque BLS et l'assigner au data frame des salaires.

Une fois de plus, je vais l'enregistrer dans un fichier CSV local et lire ces données dans un nouveau data frame appelé df.

Je vais nettoyer mes en-têtes de colonne et utiliser head pour n'imprimer que les cinq premières lignes de données, vous devriez remarquer deux choses.

Ces données ne sont pas livrées en incréments mensuels, mais trimestriels, une seule entrée pour tous les trois mois.

Et le format de la date est différent.

Au lieu d'un numéro de mois, il y a q1 ou q2.

Si vous voulez que Python synchronise entre nos deux ensembles de données, nous devrons faire un peu d'édition.

Je vais le faire en remplaçant chaque point de données de mars, c'est-à-dire toute entrée de date contenant la chaîne dash 03 dans sa valeur de date par la chaîne q one June, c'est-à-dire une chaîne incluant dash 06, nous obtiendrons q2 et ainsi de suite.

Comme vous pouvez le voir maintenant, lorsque j'imprime simplement la colonne de date, certaines valeurs ont été mises à jour dans le nouveau format.

Mais le reste d'entre eux sont à partir de ce point inutiles et nous causeront des ennuis, nous devrons donc nous en débarrasser complètement.

Je vais le faire en créant un nouveau data frame appelé New CPI et en y lisant le contenu de l'ancien data frame CPI data.

Mais j'utiliserai la fonction pan das string dot contains pour identifier toutes les lignes du data frame qui contiennent un tiret.

Et en spécifiant false, en les supprimant, nous ne serons laissés qu'avec des points de données trimestriels correctement formatés.

Et j'ai dit, je vais enregistrer ce data frame dans un fichier CSV pour remarquer comment nous sommes passés de 232 lignes à seulement 77.

Juste parce que je suis paranoïaque, je vais créer un nouveau data frame appelé New df.

Ainsi, l'ancien data frame df sera toujours disponible pour moi, au cas où je ferais accidentellement un gâchis avec ce que nous allons faire ensuite, avec nos données toutes nettoyées, nous sommes prêts à commencer notre analyse.

Nous avons un gros problème ici, les données de l'ensemble CPI viennent en valeurs de points absolues.

Alors que les salaires sont rapportés en pourcentages mesurant la croissance, comme il n'y a aucun moyen de les comparer avec précision.

Pour une chose, chaque ligne de nos données de salaires est le pourcentage auquel les salaires, quel que soit le trimestre, auraient eu le taux actuel continué pendant une année complète de 12 mois.

Ainsi, non seulement ces valeurs ne correspondent pas aux données de prix CPI absolues, mais elles ne sont même pas techniquement vraies pour leur propre période.

Ainsi, lorsque nous sommes informés que le taux pour le premier trimestre de 2002 était de 3,5 %.

Cela signifie que si les salaires continuaient à augmenter au taux actuel du premier trimestre, pendant une année complète de 12 mois, la croissance annuelle moyenne aurait été de 3,5 %, mais pas de 14 %, ce qui signifie que les chiffres avec lesquels nous allons travailler devront être ajustés.

C'est parce que la croissance réelle pendant, disons, les trois mois de 2002, le premier trimestre n'était pas de 3,5 %, mais seulement un quart de cela, soit 0,875 %.

Si je ne fais pas cet ajustement, mais continue à mapper les chiffres de croissance trimestrielle aux prix CPI trimestriels qui sont calculés, la sortie calculée nous amènerait à penser que les salaires augmentent si rapidement qu'ils se détachent de la réalité.

Maintenant, je devrais vous avertir que la résolution de ce problème de compatibilité nécessitera quelques mathématiques fictives, je vais diviser chaque taux de croissance trimestriel par quatre ou en d'autres termes, je vais prétendre que les changements réels des salaires pendant ces trois mois étaient exactement un quart du taux rapporté d'une année sur l'autre.

Je suis sûr que ce n'est presque certainement pas vrai.

Et c'est une simplification grossière.

Cependant, pour le grand tableau historique que j'essaie de dessiner ici, c'est probablement assez proche.

Maintenant, cela nous laissera encore avec un nombre qui est un pourcentage, mais le nombre CPI correspondant que nous comparons est à nouveau une figure de point.

Pour résoudre ce problème.

Je vais appliquer une autre pièce de falsification.

Pour convertir ces pourcentages afin qu'ils correspondent aux valeurs CPI, je vais créer une fonction, je vais alimenter la fonction avec la valeur CPI du premier trimestre 2002 de départ de 170 7.1.

Ce sera ma ligne de base.

Je donnerai à cette variable le nom new num.

Pour chaque itération, la fonction fera à travers les lignes de ma série de données de salaires, je diviserai la valeur de salaire actuelle x par 400.

D'où ai-je obtenu ce nombre 100 convertit simplement le pourcentage en 3.5, etc, en un décimal 0.035.

Et les quatre réduiront le taux annuel ou 12 mois à un taux trimestriel couvrant trois mois pour convertir cela en un nombre utilisable, je le multiplie par la valeur actuelle de new num, puis j'ajoute new num au produit.

Cela devrait nous donner une approximation de la valeur CPI originale ajustée par le pourcentage de croissance des salaires lié.

Mais bien sûr, ce ne sera pas un nombre qui a un équivalent direct dans le monde réel.

Au lieu de cela, c'est, comme je l'ai dit, une approximation arbitraire de ce que ce nombre aurait pu être.

Mais encore une fois, je pense que cela sera assez proche pour nos besoins.

Prenez un moment pour lire la fonction.

Global new num déclare une variable comme globale.

Cela me permet de remplacer la valeur originale de new num par la sortie de la fonction, afin que le pourcentage dans la ligne suivante soit ajusté par la valeur mise à jour.

Remarquez également comment les chaînes de caractères seront ignorées.

Et enfin, remarquez comment la série de données mise à jour remplira la nouvelle variable de données de salaires.

Vérifions que les nouvelles données ont l'air bien.

Notre prochaine tâche sera de fusionner nos deux data frames puis de tracer leurs données.

Ne partez pas.

Il reste à fusionner nos deux séries de données afin que Python puisse les comparer.

Mais puisque nous avons déjà fait tout le nettoyage et la manipulation, cela se passera sans encombre.

Je vais créer un nouveau data frame appelé merge data et l'alimenter avec l'URL Put up this PD merge function, je fournis simplement les noms de mes deux data frames et spécifie que la colonne de date devrait être l'index.

Ce n'était pas difficile.

Jetons un coup d'œil.

Toutes nos données sont là, nous pouvons scanner visuellement les colonnes CPI et salaires et rechercher toute relation inhabituelle.

Mais cela va à l'encontre du but.

L'analyse de données Python consiste à laisser notre code faire cela pour nous.

Traçons la chose.

Ici, nous allons dire à plot de prendre notre data frame merge data et de créer un graphique à barres.

Parce qu'il y a une quantité terrible de données ici, je vais étendre la taille du graphique avec une valeur de taille fixe manuelle, je définis l'axe x pour utiliser les valeurs dans la colonne de date.

Et encore, parce qu'il y en a tant, je vais faire pivoter les étiquettes de 45 degrés pour les rendre plus lisibles.

Enfin, je vais définir les étiquettes pour les axes x et y.

C'est ce qui sort de l'autre extrémité, à cause de l'encombrement, ce n'est pas particulièrement facile à lire.

Mais vous pouvez voir que les barres de salaires orange sont pour la plupart plus hautes que les barres CPI bleues.

Cela signifie que les salaires connaissent un taux de croissance plus élevé que le CPI, nous aurons une tentative d'analyse de certaines de ces données un peu plus tard, y a-t-il un moyen plus facile d'afficher toutes ces données, vous pariez qu'il y en a, je peux changer la valeur de kind de bar à line, et les choses s'amélioreront instantanément.

Voici comment le nouveau code fonctionnera en tant que graphique en ligne et avec la grille.

Python, ainsi que ses bibliothèques associées, nous donne la capacité d'utiliser une bien plus grande variété d'outils de traçage que simplement des graphiques à barres et en lignes.

Nous allons explorer seulement deux d'entre eux ici, les graphiques de dispersion et les histogrammes.

Nous parlerons également un peu de la manière dont les lignes de régression fonctionnent et des types d'informations qu'elles peuvent nous montrer.

Nous commencerons par les graphiques de dispersion.

Ce code provient du chapitre sur les droits de propriété et le développement économique de mon site web Teach Yourself data analytics, vous pouvez vous mettre à jour sur le contexte là-bas.

Mais le code que vous regardez provient de deux sources de données, la mesure de la Banque mondiale du produit intérieur brut par habitant par pays et les données de l'indice de liberté économique du site heritage.o

rg, j'ai fusionné les données des deux data frames en celui-ci appelé merge data, je vais créer un simple graphique de dispersion.

Avec cette commande en une seule ligne, nous pouvons clairement voir un motif, plus le produit intérieur brut par habitant est élevé, ce qui signifie que plus l'activité économique qu'un pays génère est importante, plus le point d'un pays est susceptible de tomber à droite sur l'axe des x.

Et plus à droite, plus le score de liberté économique est élevé.

Bien sûr, il y a des anomalies dans nos données.

Il y a des pays dont la position semble hors de portée de tous les autres, ce serait bien si nous pouvions somehow voir quels pays sont ceux-là, et ce serait également bien si nous pouvions quantifier la relation statistique précise entre nos deux valeurs, plutôt que de devoir deviner visuellement.

Nous commencerons par visualiser ces anomalies dans nos données.

Pour que cela se produise.

tous les éléments importants, un autre couple de bibliothèques qui font partie de la famille d'outils plotly, vous devrez peut-être les installer manuellement sur votre hôte en utilisant pip install plotly.

Avant que ceux-ci ne fonctionnent.

À partir de là, nous pouvons exécuter p x scatter, et le pointer vers notre data frame merge data, en associant la colonne score avec l'axe x et la valeur avec l'axe y.

Ainsi, nous pourrons survoler un point et voir les données qu'il représente.

Nous ajouterons l'argument hover data et lui dirons d'inclure les données du pays et du score.

Cette fois, lorsque vous exécutez le code, vous obtenez le même joli graphique.

Mais si vous survolez un point avec votre souris, vous verrez également ses valeurs de données.

Dans cet exemple, vous pouvez voir que le petit mais riche pays du Luxembourg a un score de liberté économique de 75,9

et un PIB par habitant de plus de 121 000 $.

Vous pouvez de même repérer d'autres pays à l'une ou l'autre extrémité du graphique, nous pouvons en apprendre davantage sur la relation statistique entre nos valeurs en ajoutant une ligne de régression, une mesure de la valeur R au carré des données.

Nous avons déjà vu comment notre graphique montrait une tendance visible vers le haut et vers la droite.

Mais nous avons également vu qu'il y avait des valeurs aberrantes.

Pouvons-nous être confiants que les valeurs aberrantes sont les exceptions et que la relation globale entre nos deux sources de données est solide.

Il n'y a que tant de choses que nous pouvons supposer sur la base de la visualisation du graphique, à un moment donné, nous aurons besoin de chiffres concrets pour décrire ce que nous regardons.

Une simple analyse de régression linéaire peut nous donner une mesure de la force de la relation entre une variable dépendante et le modèle de données.

r au carré est un nombre entre zéro et 100 %.

Où 100 % indiquerait un ajustement parfait.

Bien sûr, dans le monde réel, un ajustement à 100 % est presque impossible.

Vous jugerez de l'exactitude de votre modèle ou hypothèse dans le contexte des données avec lesquelles vous travaillez, comment pouvez-vous ajouter une ligne de régression à un graphique de pandas ? Il existe, comme toujours, de nombreuses façons de procéder, j'aime la simplicité et l'approche de la ligne de tendance OLS est aussi simple que possible, il suffit d'ajouter un argument de ligne de tendance au code que nous avons déjà utilisé.

C'est tout.

Oh, OLS, au fait, signifie ordinary least squares, qui est un type de régression linéaire.

Et voici à quoi cela ressemble avec notre ligne de régression.

Lorsque je survole la ligne, je montre une valeur R au carré de 0,550451.

Ou en d'autres termes, environ 35 %.

Pour nos besoins, je considère cela comme une corrélation assez forte.

Un histogramme est un outil de traçage qui décompose vos données en bins. Un bin est en fait une approximation d'un intervalle statistiquement approprié entre les ensembles de vos données. Les bins tentent de deviner la fonction de densité de probabilité (PDF) qui représentera le mieux les valeurs que vous utilisez réellement.

Mais ils peuvent ne pas s'afficher exactement comme vous le pensez, surtout lorsque vous utilisez une valeur par défaut.

Je vais illustrer comment cela fonctionne ou plutôt comment cela ne fonctionne pas.

En utilisant les données du chapitre "Les anniversaires font-ils des athlètes d'élite ?" sur le site web.

Comme vous pouvez le voir là-bas, j'ai extrait l'API semi-officielle de la LNH pour les dates de naissance d'environ 1100 joueurs actuels de la LNH.

Mon objectif était de visualiser la distribution de leurs dates de naissance sur les 12 mois pour voir si leurs naissances étaient concentrées dans une saison particulière de l'année.

Lorsque j'ai affiché les données à l'aide d'un histogramme, nous n'avons pas vu le motif que nous attendions.

En fait, le motif n'était pas vraiment représentatif du monde réel.

C'est parce que les histogrammes sont excellents pour montrer les distributions de fréquence en regroupant les points de données en bins.

Cela peut nous aider à visualiser rapidement l'état d'un très grand ensemble de données où la précision granulaire se mettra en travers, mais cela peut être trompeur pour des cas d'utilisation comme le nôtre.

Puisque nous cherchions une cartographie littérale des événements aux dates du calendrier.

Même en définissant le nombre de bins à 12 pour correspondre au nombre de mois ne nous aidera pas, car un histogramme ne collera pas nécessairement à ces frontières exactes.

Ce dont nous avons vraiment besoin ici, c'est d'un bon vieux graphique à barres qui incorpore nos chiffres de comptage de valeurs, je vais transmettre les résultats de value counts à un data frame appelé df one, puis tracer cela sous forme de simple graphique à barres.

Dans le module suivant, nous allons parler de la compréhension de nos visualisations de données et de l'intégration de ce que nous voyons dans nos notebooks Jupyter avec ce qui se passe dans le monde réel.

Restez à l'écoute.

Nous sommes censés faire de l'analyse de données ici, comme regarder de jolis graphiques n'est probablement pas le but.

Les ensembles de données CPI et salaires que nous avons tracés dans le chapitre précédent, par exemple, nous ont montré une corrélation générale claire.

Mais il y avait quelques anomalies visuellement reconnaissables.

À moins de pouvoir relier ces anomalies à des événements historiques et les expliquer dans un contexte historique, nous n'obtiendrons pas toute la valeur de nos données.

Mais même avant d'en arriver là, nous devrions confirmer que nos graphiques ont réellement du sens dans le contexte de leurs sources de données.

En travaillant avec nos exemples BLS, examinons les graphiques pour comparer les données CPI et salaires avant et après notre manipulation.

De cette façon, nous pouvons être sûrs que nos mathématiques et particulièrement nos mathématiques fictives n'ont pas trop faussé les choses.

Voici à quoi ressemblent nos données CPI lorsqu'elles sont tracées en utilisant les données brutes.

C'est certainement un graphique chargé, mais vous pouvez clairement voir la pente ascendante douce ponctuée par une poignée de sauts soudains.

Ensuite, nous verrons ces mêmes données après avoir supprimé trois des quatre points de données mensuels, les mêmes hauts et bas sont toujours visibles.

Étant donné nos objectifs globaux.

Je catégoriserais notre transformation comme un succès.

Maintenant, qu'en est-il des données sur les salaires ici, parce que nous passons des pourcentages à la monnaie, la transformation était plus intrusive, et les risques de mauvaise représentation étaient plus grands.

Nous devrons également prendre en compte la manière dont un pourcentage s'affichera différemment d'une valeur absolue.

Voici les données originales.

Remarquez comment il n'y a pas de courbe cohérente, ni vers le haut ni vers le bas.

C'est parce que nous mesurons le taux de croissance tel qu'il a eu lieu au sein de chaque trimestre individuel, et non la croissance elle-même.

Maintenant, comparez cela avec ce graphique en ligne de ces données de salaires maintenant converties en valeurs basées sur la monnaie.

La courbe douce que vous voyez a un certain sens, il s'agit après tout de la croissance réelle, et non des taux de croissance, mais il est également possible de reconnaître quelques endroits où la courbe s'accentue et d'autres où elle s'aplanit un peu plus.

Pourquoi les pentes sont-elles si lisses en comparaison avec les données basées sur les pourcentages ? Regardez les étiquettes de l'axe des y.

Le graphique de l'indice est mesuré en points entre 180 et 280.

Alors que le graphique en pourcentage va de zéro à 3,5.

C'est l'échelle qui est différente.

Dans l'ensemble, je crois que nous pouvons conclure en toute sécurité que ce que nous avons produit est une bonne correspondance avec nos données sources.

Établir un certain contexte historique pour vos données nécessitera de rechercher des anomalies et de les associer à des événements historiques connus.

C'est quelque chose que je fais longuement dans le chapitre Vérification de la réalité des salaires et de l'IPC sur le site web.

Si vous êtes intéressé, je suis sûr que vous travaillerez ce matériel par vous-même.

Mais je pense que vous avez vu assez ici pour avoir une idée de la manière dont le traçage de la bonne visualisation peut être utile.  
  
Mais cela nous amène à la fin de ce cours particulier, comme je l'ai mentionné à plusieurs reprises, le programme complet est disponible sur mon site the data project dotnet, et vous êtes plus que bienvenu pour rejoindre tous les enfants cool là-bas et être en contact si vous avez quelque chose à ajouter à la conversation.

L'essentiel est de réaliser que la fin de ce cours n'est en aucun cas la fin de votre éducation en analyse de données.

Me regarder exécuter calmement des échantillons de code propres et nets n'est pas vraiment de l'apprentissage.

À moins que vous ne soyez une race très spéciale de génie, vous ne commencerez pas à comprendre comment tout cela fonctionne vraiment.

Jusqu'à ce que vous plongiez et que vous travailliez les choses par vous-même.

Je dis travailler les choses.

Mais ce que je veux vraiment dire, c'est ne pas travailler les choses parce que ce sont les erreurs et la frustration qui sont les meilleurs enseignants.

N'imaginez pas que mon code Python est simplement venu à exister un après-midi tranquille.

Alors que je sirotais un bon café chaud.

Tout d'abord, je ne bois pas de café.

Mais plus important encore, il n'y avait rien de calme à ce sujet.

Il y a eu des échecs humiliants, des reformulations, des recommencements et d'innombrables visites à stack overflow avant que les choses ne commencent à prendre forme.

Mais plus j'ai fait face à des problèmes et les ai surmontés, plus le processus s'est ancré dans mon esprit, et meilleur je suis devenu.

Et il en sera de même pour vous, soyez simplement préparé aux moments difficiles à venir.

Avant que vous ne partiez tous et que vous ne continuiez votre journée, passons un moment ou deux à réviser tout ce que nous avons vu ici.

Nous avons parlé des nombreuses façons dont vous pouvez travailler avec les notebooks Jupyter, y compris les plateformes en ligne comme Google Collaboratory, et l'hébergement local soit de Jupiter lab ou de notebooks classiques, nous nous sommes présentés à l'environnement Jupiter, en apprenant sur les cellules, les noyaux et l'environnement opérationnel.

Nous avons vu comment nous pouvons trouver des données via des API publiques et comment intégrer les informations d'identification de l'API dans notre environnement Python.

Les bibliothèques et modules Python ont été notre prochain focus, y compris comment importer des bibliothèques appropriées pour nous permettre de nettoyer et manipuler efficacement nos données.

Et enfin, en nous tournant vers une véritable analyse de données.

Nous avons appris quelques bases du traçage, y compris le travail avec des graphiques de dispersion, des lignes de régression et des histogrammes.

Et nous avons conclu le chœur avec une rapide discussion sur la manière d'utiliser nos visualisations de données pour intégrer nos insights avec le monde réel.

J'espère que cela a été utile pour vous et je vous invite à consulter certains de mes autres contenus sur mon site web principal.

Prenez soin de vous.