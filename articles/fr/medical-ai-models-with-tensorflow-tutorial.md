---
title: Modèles d'IA médicale avec TensorFlow – Tutoriel
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2023-08-03T13:20:47.000Z'
originalURL: https://freecodecamp.org/news/medical-ai-models-with-tensorflow-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/medicaltf2.png
tags:
- name: TensorFlow
  slug: tensorflow
- name: youtube
  slug: youtube
seo_title: Modèles d'IA médicale avec TensorFlow – Tutoriel
seo_desc: Machine learning is transforming many industries, including healthcare.
  Artificial intelligence is playing a pivotal role in saving lives and improving
  patient outcomes. And it is easier than you may think to start applying AI models
  to medical imagi...
---

L'apprentissage automatique transforme de nombreuses industries, y compris les soins de santé. L'intelligence artificielle joue un rôle pivot dans la sauvegarde de vies et l'amélioration des résultats pour les patients. Et il est plus facile que vous ne le pensez pour commencer à appliquer des modèles d'IA à l'imagerie médicale.

Nous venons de publier un cours sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à construire et évaluer des modèles d'IA médicale avec TensorFlow.

Le Dr Jason Adleberg enseigne ce cours. Il est radiologue à New York et un programmeur expérimenté, ce qui fait de lui l'instructeur parfait pour vous guider à travers ce cours.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-13.png)
_Vous utiliserez TensorFlow pour évaluer les radiographies pulmonaires._

Dans ce cours pratique, vous apprendrez à construire et évaluer des modèles d'IA en utilisant TensorFlow, l'un des frameworks d'apprentissage automatique les plus populaires et puissants. Le cours est structuré en deux parties, offrant à la fois des connaissances théoriques et une application pratique.

### Partie 1 : Construction et entraînement de modèles TensorFlow

Cette section commence par les bases, vous guidant étape par étape pour construire et entraîner un modèle TensorFlow simple mais efficace. Vous apprendrez les concepts fondamentaux de TensorFlow, obtiendrez des informations sur l'architecture des modèles et découvrirez diverses techniques pour optimiser les performances des modèles. L'expertise du Dr Adleberg vous aidera à saisir les essentiels du développement de modèles d'IA médicale.

### Partie 2 : Évaluation des modèles d'IA médicale

Une fois que vous aurez maîtrisé la construction de modèles, vous apprendrez à les évaluer. Dans cette partie du cours, vous explorerez des métriques clés comme l'AUC (Aire sous la courbe), la sensibilité et la spécificité. Ces métriques jouent un rôle vital dans l'évaluation de la précision et de la fiabilité des modèles, en particulier dans les contextes cliniques.

Voici les sections du cours, couvrant les deux parties ci-dessus.

* Commencer avec Google Colab 
* Faits sur les radiographies pulmonaires 
* Définir un problème 
* Préparer les données 
* Entraîner le modèle 
* Exécuter le modèle 
* Évaluer les performances 
* Statistiques : Histogramme, sensibilité et spécificité 
* Statistiques : Courbe AUC 
* Sauvegarder notre modèle

Regardez le cours complet sur [la chaîne YouTube freeCodeCamp.org](https://youtu.be/8m3LvPg8EuI) (1 heure de visionnage).

%[https://youtu.be/8m3LvPg8EuI]

### Transcription du cours (autogénérée)

L'apprentissage automatique est utilisé pour sauver des vies dans l'industrie médicale.

Dans ce cours, vous apprendrez à construire et évaluer des modèles d'IA avec TensorFlow.

C'est un excellent projet réel pour améliorer vos compétences en apprentissage automatique.

Le Dr Jason Adelberg enseigne ce cours.

Il est radiologue à New York et aussi programmeur.

Alors commençons à apprendre.

Salut tout le monde, je m'appelle Jason.

Je suis médecin et programmeur informatique à New York.

Et aujourd'hui, nous allons parler de la construction et de l'évaluation de modèles d'IA médicale avec TensorFlow.

Ce tutoriel d'aujourd'hui aura deux parties.

La première partie consistera à construire et entraîner un modèle TensorFlow vraiment simple.

Et la deuxième partie consistera à passer en revue les statistiques, l'évaluation de notre modèle, et nous parlerons de métriques comme l'AUC, la sensibilité, la spécificité.

Cela sera vraiment utile, surtout si nous sommes intéressés à le déployer dans l'espace clinique.

Je voulais rendre un grand hommage au Dr Walter Wiggins pour avoir inspiré ce tutoriel.

Voici son Twitter et voici le mien.

Et avec cela, commençons.

Très bien, donc aujourd'hui nous allons utiliser Google Colab.

Google Colab est un site web vraiment cool grâce auquel vous pouvez exécuter différentes parties de code Python.

Si vous ne l'avez jamais utilisé auparavant, c'est relativement facile.

Nous commencerons par cliquer sur connecter ici.

Et ensuite, dans ce tutoriel, tous ces différents blocs de code ici, ceux-ci sont connus sous le nom de cellules, et nous pouvons cliquer sur le bouton lecture ici à gauche pour tout faire fonctionner.

Cette première cellule sera simplement nous téléchargeant un tas de choses, donc c'est une bonne façon de commencer.

Très bien, donc aujourd'hui nous allons travailler avec des radiographies pulmonaires.

Et les radiographies pulmonaires sont l'étude d'imagerie la plus courante réalisée dans les hôpitaux, dans les services d'urgence, dans les milieux ambulatoires.

C'est généralement l'une des toutes premières choses que les médecins veulent savoir si vous ne vous sentez pas bien.

Maintenant, il y a un certain nombre de choses et de structures que vous pouvez voir sur une radiographie pulmonaire, alors passons-les rapidement en revue.

Voici une radiographie pulmonaire normale.

Vous pouvez voir les poumons.

Vous pouvez voir le cœur ici au milieu.

Vous pouvez voir l'aorte sortant du cœur et fournissant du sang au reste du corps.

Vous pouvez voir un certain nombre de structures squelettiques.

Par exemple, voici votre clavicule.

Vous pouvez voir toutes les côtes ici des deux côtés.

Vous pouvez voir la vertèbre ici au milieu.

Cette ligne ici s'appelle votre diaphragme.

Elle fait le tour comme ça.

Et cela sépare votre poitrine, votre thorax, de votre abdomen.

Sous cette ligne se trouve votre foie.

Votre rate est ici.

Et cette petite bulle d'air assise ici, c'est votre estomac, qui dans ce cas n'a qu'un peu d'air.

Et encore, c'est une radiographie pulmonaire normale.

Aujourd'hui, nous allons utiliser un ensemble de données assez important de radiographies pulmonaires appelé N-ray.

Et il s'agit d'un ensemble de données open source de quelques milliers de radiographies pulmonaires, qui contient huit étiquettes différentes.

Voici les huit étiquettes différentes disponibles pour nous dans cet ensemble de données.

Et celles-ci représentent huit choses assez couramment vues sur les radiographies.

Ce n'est pas tout ce que vous pouvez voir qui peut mal tourner dans une radiographie pulmonaire, mais ce sont certaines des choses les plus courantes au monde.

Et passons-les rapidement en revue.

Ici, nous avons l'atélectasie.

C'est lorsqu'une petite partie du poumon se dégonfle un peu.

Donc, c'est ici.

En gros, cette chose en forme de coin ici dans le lobe supérieur droit.

Ici, nous avons la cardiomégalie.

La cardiomégalie est lorsque vous avez un cœur vraiment gros.

Plus précisément, c'est lorsque la longueur du cœur est plus de 50 % de la longueur côte à côte.

Et c'est un signe de maladie cardiaque.

Ici, nous avons un épanchement pleural.

C'est lorsque vous avez quelque chose qui est essentiellement assis juste à l'extérieur du poumon dans ce qu'on appelle l'espace pleural, qui n'est pas vraiment censé être rempli de quoi que ce soit.

Celui-ci ici, c'est un infiltrat.

Et c'est lorsque vous avez quelque chose assis à l'intérieur des alvéoles des poumons.

Ce n'est pas censé être là.

Il y a quelques choses différentes qui peuvent faire cela, mais la plupart du temps cela signifie que vous avez une pneumonie.

Dans cette radiographie, nous avons une masse.

C'est cette densité arrondie ici dans l'apex du lobe supérieur gauche ou sur le dessus du poumon.

Une masse est quelque chose qui fait plus de trois centimètres de diamètre.

Et avec la masse, vous savez, encore une fois, cela dépend du contexte, mais généralement nous sommes un peu inquiets ici de quelque sorte de tumeur.

C'est un nodule, et un nodule est une masse qui est plus petite que trois centimètres.

Donc, c'est un peu plus difficile à voir.

Voici une pneumonie.

Une pneumonie est une infection à l'intérieur de vos alvéoles.

Encore une fois, ce n'est pas comme mutuellement exclusif avec l'infiltrat.

Et enfin, mais non des moindres, c'est un pneumothorax.

Et vous savez comment dans celui-ci nous avons dit que vous pouvez avoir parfois un peu de liquide assis dans l'espace plural.

Eh bien, ici vous avez de l'air dans l'espace plural.

Et cela est également connu sous le nom de poumon effondré.

J'évoque tout cela parce que certaines de ces conditions sont un peu plus faciles à voir et d'autres sont un peu plus difficiles à voir.

Par exemple, vous pouvez parier que vous pouvez avoir certaines de ces conditions. Par exemple, vous pouvez parier qu'une masse, qui est à nouveau de plus de trois centimètres, vous pouvez parier que cela sera plus facile pour nous à voir qu'un nodule.

Et donc, il devrait être plus facile pour un ordinateur de voir cela que de voir cela, de voir un nodule.

Vous savez, en gros, à quel point notre modèle est bon dépendra en partie de la technologie que nous utilisons, mais en partie des données elles-mêmes, en général.

Vous savez, si vous avez plus de données, c'est mieux.

Si vous avez une plus grande diversité de données, comme différents types de nodules, etc., le modèle fonctionnera un peu mieux.

Mais la qualité des étiquettes compte vraiment aussi.

Maintenant que nous avons examiné les huit découvertes différentes, l'étiquette électronique est disponible pour nous dans notre ensemble de données, choisissons-en une pour le modèle d'IA.

Je vais donc choisir la cardiomégalie.

Et examinons les données pour voir un peu plus sur les différentes images que nous avons.

Je vais donc cliquer ici sur le bouton du dossier et cliquer ici sur le dossier d'IA médicale et ici sur les images.

Et voici juste un exemple aléatoire que nous allons ouvrir.

Vous pouvez voir que c'est un exemple de radiographie pulmonaire ici.

Également dans les données que nous avons téléchargées, il y a toutes les images là.

Et voici une grande feuille de calcul de toutes les images que nous avons à notre disposition avec toutes les étiquettes dessus.

Par exemple, voici, vous savez, 100 images ou plus avec les étiquettes juste là dans cette colonne.

Je vais prendre le chemin de ce fichier.

Et le mettre ici.

Et voici juste une autre façon dont nous pouvons nous assurer que le python de notre google collab peut tout voir.

Cela montre simplement les cinq premières lignes qui se trouvent être des atélectasies.

D'accord, ensuite, je vais chercher les lignes de cette colonne où l'étiquette est égale à notre découverte.

Et nous ferons la même chose pour les cas où il n'y a aucune découverte.

Celles-ci vont nous servir de négatifs.

Nous voulons nous assurer que nous avons suffisamment d'images pour entraîner un modèle ici.

Pour cette ligne ici, je vais simplement m'assurer que nous avons suffisamment d'exemples de cas positifs.

Cela nous montre donc que nous avons 146 exemples de cardiomégalie que nous pouvons utiliser aujourd'hui.

C'est assez bien.

Un concept pour la construction de modèles d'IA est que vous voulez séparer les données en un ensemble d'entraînement et un ensemble de test.

Généralement, vous faites environ 80 % pour l'entraînement et 20 % pour le test.

Qu'est-ce que cela signifie ? Eh bien, vous savez, le modèle d'IA va être enseigné, va apprendre ce qui est quoi à partir de notre ensemble de données d'entraînement.

Mais pour savoir s'il fonctionne ou non, nous voulons lui montrer des images qu'il n'a jamais vues auparavant.

Et cela va être notre ensemble de données de test, qui est les 20 % restants de toutes ces images.

Je vais donc définir cela manuellement maintenant, comme ceci.

Et ensuite, je vais préciser exactement le nombre d'images que nous allons utiliser pour notre ensemble de données d'entraînement.

Je vais donc dire que ce nombre est 80 % de ce que nous avons à travailler aujourd'hui.

Et la même chose pour notre ensemble de données de test.

Affichons-les juste pour nous assurer qu'ils ont du sens.

Et vous pouvez voir que nous allons, et comme vous pouvez le voir, nous utiliserons 116 cas positifs pour notre ensemble de données d'entraînement et 29 cas positifs pour notre ensemble de données de test.

Ici, vous pouvez voir que nous en avons beaucoup, nous avons beaucoup d'exemples négatifs.

Donc notre facteur limitant aujourd'hui va être le nombre de cas positifs.

Pour cet exemple, aujourd'hui, nous allons faire une division 50-50 où nous voulons avoir un nombre égal de cas positifs et négatifs pour notre entraînement et pour notre test.

Nous allons donc simplement préciser cela ici.

Ici, je vais simplement rassembler les lignes qui vont aller dans notre ensemble de données d'entraînement.

Cela ressemblera à ceci.

Donc ici, je vais simplement rassembler les lignes qui vont aller dans notre ensemble de données d'entraînement.

Et la même chose pour notre ensemble de données de test.

Et la même chose pour notre ensemble de données de test.

Cool.

D'accord, super.

Très bien, maintenant que nous savons combien d'images nous avons à travailler, nous allons simplement les déplacer vers différents dossiers.

Et nous verrons quelques exemples des images avec Python pour nous assurer que nous sommes prêts à partir.

Nous allons donc simplement créer quelques répertoires.

Voici notre répertoire racine avec toutes les images dedans.

Et voici comment je choisis de créer quelques nouveaux répertoires.

Nous allons en créer un comme ceci pour notre découverte.

Nous allons en créer un pour notre ensemble de données de test.

Nous allons en créer un pour notre ensemble de données d'entraînement.

Et ensuite, nous allons faire la même chose, mais simplement créer des dossiers négatifs au lieu des dossiers positifs aussi.

Et négatif signifie simplement qu'il n'y a aucune découverte.

Comme ça.

Maintenant, nous allons procéder et simplement déplacer ces fichiers.

Et nous allons faire cela en itérant à travers les lignes de notre cadre de données qui nous intéressent.

Nous prêtons donc un peu d'attention au nombre exact d'images que nous devons déplacer.

Mais voici où, par exemple, les exemples positifs d'entraînement se trouvent.

Ils sont comme ceci, comme défini dans notre fichier CSV.

Voici où nous allons les déplacer.

Et ceci est, encore une fois, la manière dont nous l'avons défini dans le bloc de code ci-dessus.

Et cette ligne ici, c'est ce qui fait réellement le déplacement.

Nous allons l'essayer rapidement juste pour nous assurer que cela fonctionne.

Si cela fonctionne, nous pouvons double vérifier en cliquant ici.

Nous allons dans images.

Attendez une minute.

Allons à cardiomégalie.

Et vous pouvez voir que maintenant nous avons créé quelques dossiers de test, quelques dossiers d'entraînement, et ceci devrait être un grand nombre des images ici, n'est-ce pas ? Maintenant, je vais simplement copier et coller ceci.

Et au lieu de faire les positifs dans notre ensemble de données d'entraînement, je vais faire les positifs dans notre ensemble de données de test.

Parce que notre ensemble de données d'entraînement est 80 % de tout ceci, ceci est plus ou moins comme la 80ème ligne de pourcentage de toutes les choses positives que nous avons.

Et ensuite, nous allons déplacer ceci vers la partie de test.

Je vais simplement ajuster cela ici.

Et ensuite, nous allons faire la même chose pour nos négatifs.

Maintenant, je vais simplement copier et coller ces lignes.

Je vais simplement changer positifs en négatifs.

Positif en négatif.

Ici et ici.

Terminé.

Je vais procéder et simplement copier ceci ici.

Cool.

Maintenant que nous avons tout déplacé, utilisons simplement Python pour montrer tout directement dans ce notebook, juste pour nous assurer que ce que nous faisons a du sens et est approprié.

Je vais donc définir deux tableaux.

Et ensuite, c'est quelque chose que nous avons déclaré dans le premier bloc de code lorsque nous avons commencé aujourd'hui.

Mais juste pour insister, décrivons cela.

Ici, nous allons simplement montrer des versions plus petites des images que nous chargeons.

Et ensuite, nous allons simplement montrer six exemples.

Et c'est la manière dont nous allons le charger.

Et c'est la manière dont nous allons le charger dans Python lui-même.

image point open image path point resize image width image height image height comme cela positive images append.

Et ceci est essentiellement une fonction d'aide que nous avons déclarée tout en haut.

Image comme cela.

Et je m'assurerai que je l'ai bien orthographié.

Je vais simplement faire la même chose pour les images négatives.

Donc encore une fois, ce sont les images qui n'ont aucune découverte.

Comme cela.

Maintenant que nous avons tout chargé, nous allons procéder et simplement tout montrer avec matplotlib.

Et donc nous allons procéder et montrer six images.

Donc ce seront nos six images qui ont une cardiomégalie.

Cela ira là.

Et ensuite, nous allons faire la même chose.

Je copie et colle ceci pour les images négatives.

Donc je vais simplement ajuster cela.

Je vais ajuster cela.

Et nous n'utilisons pas, encore une fois, le point entier avec les images négatives est de montrer celles qui n'ont aucune découverte.

Donc allons-y et cliquons sur lecture.

Ici, vous pouvez voir qu'il nous montre six exemples de cardiomégalie à partir du dossier qu'il a créé.

Et pour moi, tous ceux-ci semblent être des cas définitifs de cardiomégalie.

Vous pouvez voir que le cœur ici est définitivement agrandi.

Il fait plus de la moitié de la poitrine.

Et ici, ceux-ci semblent être des cas sans découverte.

Donc ici, le cœur est de taille normale et il n'y a pas vraiment grand-chose d'autre qui se passe.

D'accord, nous avons donc visualisé nos données.

Nous avons tout déplacé et nous savons que nous voulons construire un modèle d'IA pour la cardiomégalie.

Dans cette partie, nous allons en fait construire le modèle TensorFlow.

Il existe de nombreuses façons différentes d'aborder la construction de modèles et nous pourrions passer une heure sur ce sujet seul.

Mais en gros ici, je veux parler de deux concepts différents pour cette partie.

Le premier s'appelle l'apprentissage par transfert.

Et le deuxième concept s'appelle l'augmentation des données.

Nous allons utiliser ces deux choses aujourd'hui.

Très bien, donc cette première ligne ici, cela va nous faire charger notre modèle directement via TensorFlow lui-même.

Et nous allons simplement définir la taille de l'image avec laquelle il va travailler, dont nous avons un peu parlé plus tôt, mais celles-ci vont être un peu plus petites, essentiellement des versions réduites de notre radiographie pulmonaire.

Ce trois ici indique qu'il s'agit essentiellement d'une image à trois canaux, comme une image en couleur, n'est-ce pas, comme rouge, vert et bleu.

Maintenant, il est vrai que, vous savez, nos radiographies pulmonaires sont en fait toutes des nuances de gris, mais nous allons simplement le mettre là parce que c'est un peu plus facile.

Et ensuite, celui-ci, include top equals false.

Nous y reviendrons, mais cela va essentiellement nous permettre de personnaliser notre modèle pour faire ce que nous voulons faire ici.

Cela devrait être des poids au pluriel.

Et maintenant, nous utilisons à nouveau le réseau ImageNet ici.

Mais ce que nous allons faire, c'est, par-dessus tout cela, pour la dernière couche de notre modèle, nous allons lui faire dire s'il pense qu'il y a une cardiomégalie ou non.

Nous allons donc simplement le définir manuellement ici.

Cela parle essentiellement du type exact de sortie que nous voulons que notre modèle produise.

Donc cela prend simplement cette dernière couche, et ici nous allons définir cela en disant que nous voulons dire soit oui ou non, positif ou négatif.

Donc c'est la manière dont nous pouvons faire cela.

C'est simplement des choses pour, encore une fois, nous aider dans notre grande tâche, qui consiste à dire oui ou non, cardiomégalie ou non cardiomégalie.

Je vais dire oui ou non, et ensuite je vais dire oui ou non.

Donc c'est simplement des choses pour, encore une fois, nous aider dans notre grande tâche, qui consiste à dire oui ou non, cardiomégalie ou non cardiomégalie.

Toutes ces décisions ici, nous pourrions en parler pendant très longtemps, mais je vais sauter certains des détails ici.

Et s'il y a quelque chose à mettre un x là, d'accord.

D'accord, en ce qui concerne le modèle, nous avons donc ce modèle avec une dernière couche légèrement personnalisée.

Et maintenant, nous allons simplement procéder et le compiler.

Ici, nous allons simplement dire que nous nous intéressons à la précision, en gros, donc à quel point notre modèle est précis entre dire si quelque chose est positif ou négatif, et c'est un peu la métrique que nous allons utiliser pour nous aider à déterminer si notre modèle fonctionne ou non.

Oh, et ensuite une autre chose est que nous devrions mettre un signe égal là, et cela nous aiderait aussi.

D'accord, maintenant que tout cela est fait, nous allons procéder et simplement définir un tas de choses qui aident essentiellement à pointer notre modèle vers les bonnes informations.

Donc si vous vous souvenez, toutes nos images sont cachées là.

Le répertoire où tout est situé pour l'imagerie des trucs d'entraînement est comme ceci.

Pour le test, c'est à peu près la même chose, mais comme ceci, changez ceci ici.

Et ensuite cela continue.

Donc la façon dont nous avons structuré nos données est que nous avons des sous-dossiers dans notre répertoire d'entraînement qui s'appellent positif, un appelé négatif, que nous allons mettre ici.

Cela ressemble à ceci.

Comme ceci.

Et ensuite la même chose existe également pour nos données de test.

Donc je vais faire ces changements ici, ici, ici et là.

Je vais cliquer sur lecture ici.

D'accord, donc le prochain concept dont je veux parler est quelque chose appelé augmentation des données.

Comme nous en avons discuté plus tôt, nous avons un tas d'images disponibles pour nous avec la cardiomégalie, mais ce n'est pas une tonne.

Il y a des moyens par lesquels nous pouvons essentiellement créer plus de données d'entraînement pour nous-mêmes, et cela s'appelle l'augmentation des données.

Donc ce que nous allons utiliser ici est essentiellement un concept vraiment cool appelé générateur d'images.

Et c'est essentiellement quelque chose qui va regarder toutes les images que nous avons et les ajuster un peu pour que nous générions des données à partir des données que nous avons déjà.

Maintenant, il y a beaucoup de façons différentes d'augmenter les données, de les ajuster, mais celles-ci sont celles que nous allons utiliser aujourd'hui.

Et, vous savez, si vous jouez avec cela un peu par vous-même, vous êtes libre de, vous savez, expérimenter avec différentes idées ici.

Donc que faisons-nous ? Donc tout d'abord, toutes ces méthodes ici génèrent essentiellement des images supplémentaires qui sont légèrement ajustées à partir de nos images.

Donc spécifiquement, cela va générer des images qui sont légèrement tournées d'un côté ou de l'autre, qui sont légèrement déplacées, comme étirées, qui sont cisillées, et qui sont également zoomées.

Une chose importante avec l'augmentation des données est qu'elle ne va pas être simplement zoomée.

Une chose importante avec l'augmentation pour les données médicales est que, vous savez, il y a des pensées différentes sur cela, mais lorsqu'il s'agit de retourner des images, vous savez, une radiographie pulmonaire n'est jamais vraiment retournée, n'est-ce pas ? Comme, vous savez, votre cœur est toujours comme, vous savez, vous êtes, vous savez, lorsque vous prenez une radiographie pulmonaire, comme, à l'endroit, n'est-ce pas ? Comme votre estomac est toujours en dessous de vos poumons.

Donc si nous devions retourner les données à l'envers, cela ne serait pas nécessairement vraiment utile pour notre modèle d'IA.

En ce qui concerne le retournement horizontal, vous savez, je pense qu'il n'y a pas vraiment de consensus sur cela lorsqu'il s'agit d'imagerie médicale ou spécifiquement de radiographies pulmonaires.

Il est vrai que nos corps ne sont pas complètement symétriques, même si nous aimons prétendre qu'ils le sont, donc votre cœur est un peu plus du côté gauche.

Il existe une condition où votre cœur peut être plus du côté droit, mais ce n'est pas super courant.

Donc je vais simplement dire que nous ne allons pas retourner les choses horizontalement pour ne pas confondre notre modèle, mais c'est un choix que vous pourriez faire si vous le souhaitiez.

Pour nos données de test, nous ne voulons définitivement pas augmenter, ne voulons pas du tout toucher à nos données de test.

Donc c'est juste une ligne où, vous savez, nous créons un générateur d'images, mais tout ce que nous faisons ici est simplement redéfinir les nombres qui sont à l'intérieur de notre, de chaque pixel, en gros.

Donc ce n'est pas vraiment en train de faire quoi que ce soit, n'est-ce pas ? Cela dit essentiellement qu'au lieu que chaque pixel aille de zéro à 255, il sera entre zéro et un.

D'accord, allons-y et cliquons là.

Cela fonctionne.

Donc c'est l'augmentation des images.

Et maintenant, ceci est quelque chose que nous devons utiliser afin de faire entraîner notre modèle, appelé un générateur d'entraînement et de test.

Et c'est essentiellement la manière dont nous le faisons ici.

Donc à partir du répertoire, que nous avons déjà, la taille cible et ensuite nous allons simplement faire la même chose pour le test juste en dessous.

Et ensuite, vous savez, bien sûr, nous devons simplement ajuster certaines de ces choses ici pour cette partie particulière.

Nous allons procéder et simplement définir le nombre d'étapes que nous allons utiliser pour cela, qui est essentiellement parce que nous avons une taille de lot de un.

Il se trouve que c'est la même chose, il se trouve que c'est comme toutes les images que nous utilisons.

Donc, je veux dire, c'est une façon de le faire, comme la façon dont nos données sont structurées.

Comme la façon dont nos données sont structurées.

Donc encore une fois, les étapes d'entraînement sont égales à la longueur de ce dossier fois deux.

Et ensuite pour le test, nous allons procéder et dire que c'est comme ceci.

Et ensuite nous avons en fait tapé cela de travers ici.

Donc allons-y et corrigeons cela rapidement.

Cela se fait comme cela.

Et ensuite cela se fait comme ceci.

Et vous pouvez voir ici que lorsque nous cliquons, donc il a trouvé 232 images pour la partie d'entraînement et 60 images pour la partie de test.

Et encore une fois, cela est assez proche d'une division à 80 % et 20 %.

Très bien, nous avons tout configuré.

Nous avons notre modèle prêt à partir.

Nous avons nos données prêtes à partir.

C'est la partie cool.

Maintenant, nous allons enfin exécuter notre modèle et le laisser s'entraîner.

Pour ce faire, c'est la méthode que nous allons utiliser.

Nous allons utiliser ce qu'on appelle model.fit.

Nous allons le pointer vers le générateur d'entraînement dont nous avons parlé plus tôt.

Nous allons simplement mentionner exactement le nombre d'étapes par époque.

Et une époque est essentiellement un passage à travers toutes les données.

Donc dans cet exemple particulier, nous allons simplement lui demander de regarder toutes les images 20 fois afin de faire l'entraînement.

Et ensuite, nous allons également le pointer vers l'ensemble de validation.

C'est notre ensemble de test, les 20 % que nous avons sectionnés qu'il n'a jamais vus auparavant.

Et lorsque nous cliquons sur lecture, vous pouvez voir que vous pouvez voir que j'ai mal orthographié epochs.

Et ensuite, finalement, il va réellement commencer à faire son travail.

Maintenant, la façon dont nous l'avons formaté pour ce tutoriel aujourd'hui, cela ne devrait pas vraiment prendre trop de temps pour passer à travers toutes les données.

Mais cela prendra environ quelques minutes ou plus.

Donc nous allons simplement cliquer sur lecture et ensuite nous reculer.

Nous reviendrons dans quelques minutes.

Très bien, nous sommes de retour.

Cela fait trois minutes d'entraînement, ce qui n'est vraiment pas beaucoup de temps du tout.

Mais c'est bon.

C'est suffisant pour que nous comprenions certains des concepts avec lesquels nous travaillons aujourd'hui.

Donc maintenant, ce que nous allons faire, c'est voir exactement à quel point il a bien fait son travail au fil du temps.

Donc, en gros, nous allons simplement tracer comment la précision a changé.

Et c'est essentiellement la précision pour l'ensemble d'entraînement, qui devrait augmenter au fil du temps.

Et ensuite, c'est la précision pour l'ensemble de validation, l'ensemble de données de test, qui est essentiellement la précision pour les données qu'il n'a jamais vues auparavant.

Donc nous espérons que cela augmente.

Mais, vous savez, c'est pourquoi nous avons dû le garder séparé, car cela nous montrera en fait s'il fait du bon travail ou non.

Je fais la même chose pour la perte.

Et, en gros, la perte est une autre façon abstraite de penser à la qualité du travail qu'il fait.

Donc la perte est, vous savez, vous voulez que votre précision augmente au fil du temps, et vous voulez que votre perte diminue au fil du temps.

Et la perte est essentiellement une façon mathématique de parler de la manière dont le réseau devrait être et de la manière dont le réseau est actuellement.

Donc je vais tracer en utilisant matplotlib, différentes choses liées à la perte et liées à la précision au fur et à mesure qu'elles changent au fil du temps.

Nous ferons la même chose ici, mais pour l'ensemble de données de validation.

Et encore une fois, cela va être la précision d'entraînement et de test au fur et à mesure qu'elle change au fil du temps.

Je vais simplement mettre cela ici comme ceci.

Cliquons sur lecture.

Et cela est en fait assez encourageant.

Donc, vous savez, au fur et à mesure que cette chose a fonctionné pendant quelques minutes, seulement après quelques minutes, elle a commencé à comprendre ce qui était quoi, ce qui était la cardiomégalie et ce qui ne l'était pas.

Donc l'ensemble de données d'entraînement, nous nous attendons à ce que cela augmente.

Nous nous attendons à ce que cela devienne plus précis au fil du temps.

Mais l'ensemble de données de test, nous espérons qu'il devient plus précis.

Et comme vous pouvez le voir, il l'a fait.

Donc lorsqu'il a commencé, il avait une chance de 50-50.

Mais après seulement quelques minutes d'entraînement, il est devenu environ 70 % ou plus précis.

Et, vous savez, c'est mieux que de lancer une pièce de monnaie.

Je vais également procéder et faire la même chose pour la perte, qui est une autre façon de penser à la qualité du travail de notre modèle.

Et donc, au lieu de la précision, nous allons simplement tracer la perte.

Et je vais simplement modifier cela ici pour que nous ayons une meilleure idée de ce qui se passe.

Donc voici notre perte.

Et comme vous pouvez le voir, cela diminue beaucoup au fil du temps.

Nous pourrions encore, vous savez, nous pourrions zoomer sur cela pour voir un peu plus, mais c'est un peu l'idée de base ici.

Très bien, maintenant que nous avons entraîné un modèle, voyons à quel point il est performant.

Et cette section aura essentiellement deux parties.

Donc d'abord, nous allons simplement jouer avec quelques images pour voir ce que le modèle pense.

Et ensuite, nous examinerons systématiquement toutes les images avec des statistiques, en pensant à des choses comme la sensibilité, la spécificité et l'AUC, ou l'aire sous la courbe.

Vous savez, je pense que ce qui distingue les applications de l'IA en médecine est l'attention à tous ces détails, car je pense que, vous savez, ces métriques sont vraiment importantes lorsqu'il s'agit de réfléchir à savoir si, vous savez, cela est vraiment quelque chose qui va finalement aider les gens.

Très bien, donc commençons par deux méthodes d'assistance différentes.

Cette première ici sera simplement une petite méthode d'assistance pour charger une image comme ceci.

Nous allons la redimensionner pour qu'elle corresponde à la taille requise par notre modèle, ce qui ressemble à cela.

Et nous devons faire une parenthèse réelle ici.

À partir de là, elle sera chargée dans un tableau numpy.

C'est quelque chose que nous devons utiliser juste pour la convertir de zéro à 255.

Cela signifie que chaque pixel passera d'une valeur comprise entre zéro et 255 à zéro et un.

Cela garantit simplement que le tableau a trois valeurs différentes pour le rouge, le vert et le bleu.

Même si c'est vrai, nous n'utilisons pas vraiment cela, car les radiographies sont généralement toutes en gris.

D'accord, et ensuite cette ligne ici.

C'est ce qui va être retourné.

Donc cette ligne model.predict.

C'est ainsi que nous allons interagir avec notre modèle pour retourner une valeur entre zéro et un, où zéro signifie que le modèle pense qu'il n'y a aucune découverte, et un signifie qu'il pense qu'il y a une découverte, qui ici est la cardiomégalie.

Nous allons faire une autre méthode d'assistance ici, et c'est une sorte de vérification de cohérence pour nous.

Donc ce que cela va finalement faire, c'est nous montrer une image.

Cela va nous montrer le chemin de fichier réel qui lui est associé.

Allons-y et chargeons cela ici.

Et ensuite, parce que notre modèle nous retourne une valeur entre zéro et un, ce que nous allons faire, c'est définir un point de coupure, que je vais dire être 0,5, où si la prédiction est supérieure à 0,5, alors le modèle va penser que c'est positif, n'est-ce pas ? Donc dans ce cas, le modèle va penser qu'il a une cardiomégalie.

Et cela aura un peu plus de sens dans une minute une fois que nous aurons utilisé cette méthode, mais cela montre simplement toutes les différentes informations sur l'image pendant que nous faisons la prédiction.

Donc c'est la manière dont je vais simplement accéder à toutes ces informations.

Devinez, plus, score, d'accord.

Et ensuite, une fois que nous sommes ici, cela va simplement utiliser matplotlib pour tout faire fonctionner.

Allons-y et cliquons sur lecture.

Assurons-nous que nous avons ajouté tous les signes plus.

Et encore une fois, vous savez, une chose qui est vraiment importante est que nous voulons être systématiques dans la manière dont nous évaluons toutes nos données.

Donc ce que nous allons faire ici, c'est que nous allons itérer à travers toutes les images, toutes les images de notre ensemble de test, et essayer de simplement, de manière systématique, comme organisée, comprendre ce que je pensais de tout.

Cela va être vraiment important lorsqu'il s'agit d'obtenir des choses comme la sensibilité et la spécificité, dont je reviendrai dans une seconde.

Mais en gros, ce que nous allons faire ici, c'est que nous allons passer à travers toutes les images négatives, donc toutes les images dans lesquelles il n'y a aucune découverte.

Cela a été étiqueté, c'est-à-dire, comme aucune découverte.

Et nous allons simplement faire des prédictions sur chacune d'entre elles.

Donc nous avons ce tableau appelé tableau de résultats.

Et en gros, ce que nous allons faire, c'est simplement créer ce genre de tableau de résultats avec toutes les informations qui nous intéressent.

Donc chaque ligne du tableau de résultats va être le nom du fichier, comme l'image elle-même, si elle avait une étiquette positive ou négative.

Ce sont toutes les images négatives ici, donc elle va avoir une étiquette négative.

La supposition, donc ce qu'elle a pensé.

Et ensuite la confiance, qui est à nouveau ce nombre entre 0 et 1, où nous utilisons une coupure de 0,5 pour positif versus négatif, ou cardiomégalie versus non cardiomégalie.

Cette première partie concernait toutes les images négatives.

Et maintenant nous allons faire la même chose avec toutes les images positives.

Je vais simplement changer cela ici, car encore une fois, ce sont des étiquettes positives.

À ce stade, nous aurons un tableau avec un tas de choses dedans, avec un tas de prédictions pour toutes les images de test positives et négatives.

Ce que je vais faire ici, c'est simplement trier ce tableau sur la dernière colonne, qui est la colonne de confiance.

Donc en gros, il va nous montrer dans l'ordre ce qu'il a vraiment pensé être de la cardiomégalie, et ensuite il va nous montrer ce qu'il a vraiment pensé ne pas être de la cardiomégalie, ce qui n'était aucune découverte.

Nous allons créer un cadre de données à partir de tous ces résultats ici.

Et ensuite, pour que nous puissions être organisés, nous allons créer une liste réelle de noms de colonnes aussi, ce qui serait utile.

Chemin du fichier, nom du fichier, étiquette, supposition, confiance.

Et ensuite, une fois que nous cliquons ici, cela va passer en revue et faire une supposition sur toutes les différentes images de notre ensemble de test.

D'accord, faisons défiler.

Encore une fois, ce tableau que nous avons créé, ou ce cadre de données que nous avons créé, prenons un coup d'œil pour nous assurer que cela a du sens.

Cool.

Et voici les cinq premières lignes, n'est-ce pas ? Donc voici cinq images de notre ensemble de données où ce sont les cinq images que notre modèle a pensé avoir le plus de cardiomégalie.

D'accord, donc cette méthode d'assistance que nous avons faite plus tôt, où c'était comme une vérification de cohérence pour voir si notre modèle fonctionnait réellement, allons-y et faisons un appel à cela.

Donc d'abord, nous allons simplement prendre un nombre aléatoire, comme à partir de l'ensemble de test.

Et ensuite, nous allons prendre une ligne aléatoire de notre cadre de données, qui est comme toutes les prédictions sur l'ensemble de test.

Et c'est cette méthode d'assistance que nous avons utilisée plus tôt, n'est-ce pas ? Donc voici une image aléatoire.

Vous pouvez voir qu'elle a été étiquetée comme ayant une cardiomégalie, et le modèle a deviné qu'il y avait une cardiomégalie.

Voici un exemple où cela n'a pas été étiqueté comme ayant une cardiomégalie.

Je suis d'accord, je pense que c'est un cœur normal.

Et notre modèle a également pensé qu'il n'y avait pas de cardiomégalie.

Voici un exemple où il a été étiqueté comme ayant une cardiomégalie, et notre modèle s'est trompé.

Voici un exemple où le modèle a dit qu'il y avait une cardiomégalie, et il a été étiqueté également comme ayant une cardiomégalie.

Et juste en le vérifiant, je pense que c'est un cœur assez gros, donc je dois être d'accord avec cela.

Nous pouvons cliquer sur ce bouton un grand nombre de fois différentes pour voir s'il était précis ou non.

Nous pouvons également utiliser certains nombres, comme la sensibilité et la spécificité, l'AUC, pour nous aider à avoir une meilleure idée s'il fait du bon travail ou non.

Donc nous en viendrons là dans une seconde, mais allons-y et montrons tout le cadre de données maintenant.

Ou plutôt, montrons chaque cinquième ligne du cadre de données, juste pour avoir une autre idée de ce qu'il avait.

Donc cela va montrer le nom du fichier, s'il a été étiqueté comme positif ou négatif, s'il a été étiqueté comme positif ou négatif, et essentiellement la confiance qu'il avait.

Donc en regardant cet aperçu vraiment rapide, il semble qu'il ait fait un travail assez décent, mais certains de ceux-ci au milieu ne m'ont pas convaincu.

En d'autres termes, vous savez, lorsqu'il était vraiment confiant qu'il y avait une cardiomégalie, il avait raison.

Lorsqu'il était vraiment confiant qu'il n'y avait pas de cardiomégalie, il avait raison.

Mais certains de ceux-ci au milieu, c'était un peu incertain.

Maintenant, je veux montrer les mêmes informations sous forme d'histogramme, et c'est bien car cela va commencer à nous faire réfléchir à certaines de ces statistiques dont nous avons parlé plus tôt.

Donc c'est la manière dont je vais construire l'histogramme.

Je vais prendre la même chose ici pour les étiquettes négatives.

Et ensuite, cela va utiliser la fonction histogramme de map plot lib.

C'était un peu un mot compliqué, mais juste un peu plus de choses pour configurer ce graphique d'histogramme.

Axe des x, titre, scores de confiance pour différentes images.

Et faire une légende.

D'accord.

Plot.show.

Et ici, vous pouvez commencer à voir exactement à quel point il a bien fait son travail.

Nous allons procéder et simplement écarter cette légende un peu.

Et c'est un peu mieux, n'est-ce pas ? Donc vous pouvez voir que lorsque le modèle était assez confiant, il avait raison des deux côtés.

Donc chaque exemple proche de un, il avait raison.

Chaque exemple proche de zéro, il avait raison.

Mais au milieu, c'était un peu incertain.

Dans l'ensemble, c'est en fait assez décent, cependant, à mon avis.

Maintenant, allons-y et regardons un score de confiance.

Donc maintenant, réfléchissons à, vous savez, si...

Plus tôt, nous avions mentionné que, vous savez, encore une fois, le modèle retournait une valeur entre zéro et un.

Et nous utilisions comme 50 ou 0,5 comme seuil.

Donc si c'était au-dessus de 0,5, nous dirions que c'était positif, que le modèle pensait qu'il y avait une cardiomégalie.

Et si le modèle retournait un nombre entre zéro et 0,5, nous penserions qu'il n'y avait aucune découverte.

Voyons si peut-être c'était le meilleur nombre à utiliser.

Donc ici, nous allons créer une fonction d'assistance.

Appelée createWithCutoff qui va essentiellement redessiner notre histogramme, mais maintenant nous allons parler des faux négatifs, des faux positifs, des vrais négatifs et des vrais positifs.

Donc cette ligne ici, cela dit, trouvons tout ce qui a été étiqueté comme positif.

Et le modèle pensait que c'était positif, ou il pensait que la valeur de confiance était plus que cela.

Cela va nous donner un tableau de toutes les valeurs de confiance qui sont au-dessus de notre seuil.

Faisons la même chose avec les faux positifs, les vrais négatifs et les faux négatifs.

Donc pour les faux positifs, cela signifie que l'étiquette réelle était en fait négative, mais nous pensions qu'elle était positive.

Pour les vrais négatifs, cela signifie que l'étiquette réelle était négative, et notre modèle a dit qu'elle était inférieure au seuil.

Et je vais procéder et corriger cela ici avant d'oublier.

Et ensuite pour les faux négatifs, enfin, cela va signifier que, vous savez, cela a été étiqueté comme positif, mais le modèle a accidentellement pensé qu'il était inférieur à notre valeur de seuil.

Ici, nous allons simplement faire un autre histogramme, mais nous allons simplement l'ajuster un peu.

Donc maintenant, au lieu d'avoir deux couleurs différentes, nous allons avoir quatre couleurs différentes, une pour chacune de ces quatre catégories dont nous avons parlé.

Cela va être assez similaire sinon.

Et ensuite, toutes ces choses ici vont être essentiellement les mêmes que la dernière fois.

Donc je ne vais pas passer à travers tout cela à nouveau.

Je vais simplement taper un autre titre, donc les scores de confiance pour différentes images.

Cette ligne ici, cela va dessiner une ligne verticale qui nous aide à différencier où se trouve cette valeur de seuil, et je reviendrai à cela dans une seconde quant à pourquoi nous nous soucions de cela.

Nous allons le mettre en haut à droite.

D'accord, et maintenant cette partie ici est assez importante.

Donc maintenant, nous allons calculer la sensibilité.

Donc la sensibilité est essentiellement quelque chose que nous utilisons pour voir si nous devons inclure quelque chose.

Comme un test de dépistage, généralement, vous voulez avoir une sensibilité élevée pour cela.

Et la formule pour la sensibilité est les vrais positifs sur les vrais positifs plus les faux négatifs.

Donc une autre façon de dire cela est que quelque chose qui est vraiment sensible a un faible nombre de faux négatifs.

Il peut avoir beaucoup de faux positifs, donc il peut simplement penser que tout est positif, mais au moins nous évitons les faux négatifs de cette manière.

Et ensuite, vous savez, le schéma général des choses est que une fois que nous avons un test confirmatoire, alors nous voulons une spécificité élevée.

Donc pour cela, c'est un peu l'inverse où nous voulons qu'il y ait un faible taux de faux positifs.

Donc, vous savez, quelque chose qui est comme un exemple de cela, comme si vous vous souvenez, vous savez, en 2020, lorsque nous voulions en savoir plus sur le fait qu'une personne avait le COVID, vous pouviez utiliser un test de dépistage.

Parfois, cela pouvait être comme le test d'écouvillonnage ou un test de salive.

Je suppose que c'était une chose.

Mais finalement, le test PCR était le plus spécifique.

Donc c'était comme le test plus confirmatoire.

Beaucoup de tests de dépistage avaient des faux positifs élevés, mais le test PCR, c'était comme beaucoup plus précis.

Mais le test PCR était un peu plus spécifique.

Ici, je vais simplement l'écrire sur la chose elle-même.

D'accord.

Et ici, nous allons procéder et dire que nous voulons un seuil de 0,5.

Essayons cela.

D'accord.

Et comme vous pouvez le voir, maintenant que nous avons défini un seuil de 0,5, nous pouvons commencer à penser aux vrais positifs, aux faux positifs, aux vrais négatifs et aux faux négatifs.

Donc ici, vous pouvez voir que si nous utilisons un niveau de confiance de 0,5, nous avons un taux relativement faible de faux positifs, mais une quantité plus élevée de faux négatifs.

Voyons si nous changeons cette valeur pour qu'elle soit quelque chose comme cela.

Comment cela change-t-il notre sensibilité et notre spécificité ? Eh bien, si nous abaissons cela, alors nous avons une sensibilité plus élevée, mais nous avons une spécificité pire.

Et en gros, le tableau général ici est que beaucoup de tests en médecine luttent avec cela.

Comme, vous savez, comment définissons-nous une valeur de seuil pour savoir si quelqu'un a une maladie ? Par exemple, si vous avez le diabète, vous pouvez obtenir un test appelé A1C qui regarde essentiellement la quantité de sucre dans votre sang au fil du temps.

Et, vous savez, quelle devrait être la valeur de seuil pour quelqu'un qui a le diabète versus quelqu'un qui n'a pas le diabète ? Maintenant, la réponse à cela est 6,5.

Et beaucoup de tests ont été effectués pour déterminer quelle est la meilleure valeur pour ce test particulier.

Mais ici, nous réfléchissons à quelque chose de similaire.

Je veux dire, quelle est la valeur de seuil pour savoir si notre modèle pense que vous avez une cardiomégalie ou non ? Et le concept important ici est que, vous savez, nous avons arbitrairement choisi 0,5, mais cela pourrait ne pas être la meilleure valeur.

Et beaucoup de problèmes qui pourraient ne pas être la meilleure valeur.

Et, vous savez, en fin de compte, si notre objectif est de construire quelque chose qui peut regarder une radiographie pulmonaire et diagnostiquer une maladie, nous voulons être totalement sûrs que quelle que soit la valeur de seuil qu'il a pour dire oui ou non, nous voulons être sûrs que c'est la meilleure valeur de seuil.

Donc pour cette prochaine partie, nous allons parler de la courbe ROC, ou courbe des caractéristiques de fonctionnement du récepteur, qui est liée à l'AUC, ou aire sous la courbe.

Et ce concept est essentiellement comment nous pouvons déterminer quelle est la meilleure valeur de seuil pour ce test particulier, pour ce modèle d'IA particulier, qui va encore une fois dire oui ou non.

Donc, construisons une méthode pour créer une courbe AUC.

Et en gros, ce qu'une courbe AUC va faire, c'est qu'elle va faire chaque valeur de seuil possible entre 0 et 1.

Elle va calculer la sensibilité et la spécificité pour toutes ces valeurs et classifications possibles.

Et cela va nous donner beaucoup plus d'informations grâce auxquelles nous pourrons ensuite déterminer quelle est la meilleure valeur de seuil.

Donc ce que nous allons faire ici, c'est que nous allons alimenter cette chose avec toutes les suppositions qu'elle a faites plus tôt.

Donc nous allons lui faire passer chacune d'entre elles et en gros créer maintenant cette courbe AUC.

Donc c'est en gros simplement en train de passer à travers toutes les suppositions qu'elle a faites.

Et nous allons le prendre de cette manière.

D'accord, donc maintenant nous allons simplement retourner en gros tous les nombres de vrais positifs, faux positifs, vrais négatifs et faux négatifs.

Nous allons calculer manuellement la sensibilité, dont nous avons parlé plus tôt.

Donc nous allons procéder et le faire de cette manière, comme ceci.

La spécificité va être comme ceci.

Oups.

D'accord, c'est un peu la première étape.

Et maintenant que nous avons créé cette fonction, courbe AUC, résultats triés.

Maintenant, en gros à partir de là, nous allons simplement créer une ligne qui en gros enchaîne toutes ces différentes sensibilités et spécificités pour toutes ces différentes valeurs de seuil possibles.

Et maintenant que nous avons toutes ces différentes valeurs aussi, nous allons nous assurer que nous calculons ce qu'on appelle l'aire sous la courbe, qui représente essentiellement numériquement la qualité de ce modèle.

Ou en d'autres termes, c'est essentiellement à quel point notre courbe AUC est proche d'être parfaite.

Donc voici juste un peu de code pour créer un graphique en ligne.

D'accord, voici le reste du code.

Et maintenant, une fois que nous allons exécuter, vous pouvez voir que notre courbe AUC est en fait assez bonne.

Elle a une aire assez élevée de 0,923.

Une chose un peu bizarre à propos de cette courbe, de ce graphique entier, c'est que vous remarquez que l'axe des x ici est un peu à l'envers, comme un moins la spécificité.

La raison en est que, en gros, vous savez, à mesure que la sensibilité augmente, à mesure qu'un test devient plus sensible, il devient moins spécifique.

Donc à mesure que le nombre de faux négatifs diminue, le nombre de faux positifs va augmenter.

Donc ici, vous savez, comme ce point sur la courbe ici, ce test est super sensible, ce qui signifie vraiment qu'il n'a pas vraiment beaucoup de faux négatifs.

Mais vous pouvez voir qu'il va y avoir beaucoup de faux positifs, donc il ne va pas être aussi spécifique qu'il pourrait l'être.

Dans l'ensemble, c'est une assez bonne courbe ROC.

Et vous savez, étant donné que nous n'avons entraîné ce modèle que pendant trois minutes, et que nous ne lui avons fourni que 100 images au lieu de milliers d'images, c'est assez encourageant.

Vous savez, si nous devions refaire cette expérience avec un modèle beaucoup plus puissant, avec beaucoup plus d'images, et avec beaucoup plus de temps d'entraînement, donc trois minutes, quelque chose comme peut-être, vous savez, toute la nuit ou autre chose.

Il n'y a aucune raison pour que cette courbe ROC ne puisse pas se rapprocher beaucoup de un.

Mais encore une fois, 0,923 est déjà assez bon tel quel.

Si vous voulez aller de l'avant et sauvegarder votre modèle, c'est assez facile à faire avec la base de code que nous utilisons.

Vous pouvez simplement faire model.save.

Nous allons l'enregistrer dans la partie contenu.

Et nous allons simplement le mettre comme ceci pour que vous puissiez peut-être le trouver un peu plus facilement.

Vous pourriez aussi vouloir tout compresser.

Et ce qui est vraiment cool avec Colab, c'est que vous pouvez faire exactement cela en appuyant sur le point d'exclamation lorsque vous commencez dans Colab qui nous permet de faire des commandes shell.

Donc si vous voulez essayer tout cela ici, nous allons cliquer sur lecture.

Et dans une minute, vous verrez que le modèle est essentiellement enregistré ici et compressé.

Cela a pris environ deux minutes ou plus pour tout compresser, mais en tout cas, cliquez simplement sur cette icône ici.

Et voici notre modèle qui fait environ un gigaoctet ou plus.

Cliquez sur ces trois points, téléchargez, et ensuite cela l'enregistrera sur votre ordinateur en une minute ou plus.

D'accord, cela conclut à peu près cette présentation.

Si vous avez des questions, n'hésitez pas à me contacter sur ce compte Twitter ci-dessus ou commentez cette vidéo ci-dessous.

Et j'espère que vous avez apprécié cela et merci pour votre attention.

Merci pour votre temps.