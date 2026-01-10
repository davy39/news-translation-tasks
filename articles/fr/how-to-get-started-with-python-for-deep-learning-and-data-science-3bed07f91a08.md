---
title: Comment commencer avec Python pour le Deep Learning et la Data Science
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-06T17:39:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-python-for-deep-learning-and-data-science-3bed07f91a08
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7aJPlxn8gwhI7JjcBFr-tQ.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: Comment commencer avec Python pour le Deep Learning et la Data Science
seo_desc: 'By Joseph Lee Wei En

  A step-by-step guide to setting up Python for a complete beginner


  You can code your own Data Science or Deep Learning project in just a couple of
  lines of code these days. This is not an exaggeration; many programmers out there
  ...'
---

Par Joseph Lee Wei En

#### Un guide étape par étape pour configurer Python pour un débutant complet

![Image](https://cdn-media-1.freecodecamp.org/images/f2tiBCqS6IVb1yWNurylwXhNi4fEDOeiVlib)

Vous pouvez coder votre propre projet de Data Science ou de Deep Learning en seulement quelques lignes de code de nos jours. Ce n'est pas une exagération ; de nombreux programmeurs ont fait le travail difficile d'écrire des tonnes de code pour que nous puissions l'utiliser, afin que tout ce que nous ayons à faire soit du plug-and-play plutôt que d'écrire du code à partir de zéro.

Vous avez peut-être vu certains de ces codes dans des articles de blog sur la Data Science ou le Deep Learning. Peut-être avez-vous pensé : « Eh bien, si c'est vraiment si facile, alors pourquoi ne pas essayer moi-même ? »

Si vous êtes un débutant en Python et que vous souhaitez vous lancer dans ce voyage, alors cet article vous guidera à travers vos premiers pas. Une plainte courante que j'entends de la part des débutants complets est qu'il est assez difficile de configurer Python. Comment démarrer tout cela en premier lieu afin que nous puissions utiliser du code de Data Science ou de Deep Learning en plug-and-play ?

Cet article vous guidera étape par étape pour configurer Python pour vos projets de Data Science et de Deep Learning. Nous allons :

* Configurer Anaconda et Jupyter Notebook
* Créer des environnements Anaconda et installer des packages (du code que d'autres ont écrit pour rendre notre vie extrêmement facile) comme tensorflow, keras, pandas, scikit-learn et matplotlib.

Une fois que vous avez configuré ce qui précède, vous pouvez construire votre premier réseau de neurones pour prédire les prix des maisons dans ce tutoriel ici :

[Construisez votre premier réseau de neurones pour prédire les prix des maisons avec Keras](https://medium.com/intuitive-deep-learning/build-your-first-neural-network-to-predict-house-prices-with-keras-eb5db60232c)

### Configuration d'Anaconda et de Jupyter Notebook

Le principal langage de programmation que nous allons utiliser s'appelle Python, qui est le langage de programmation le plus courant utilisé par les praticiens du Deep Learning.

La première étape consiste à télécharger Anaconda, que vous pouvez considérer comme une plateforme pour utiliser Python « prêt à l'emploi ».

Visitez cette page : [https://www.anaconda.com/distribution/](https://www.anaconda.com/distribution/) et faites défiler vers le bas pour voir ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/Y9PBNXOl0NLmLPp1DBpQrodepqZ0UCwk6KWT)
_Télécharger Anaconda_

Ce tutoriel est écrit spécifiquement pour les utilisateurs de Windows, mais les instructions pour les utilisateurs d'autres systèmes d'exploitation ne sont pas si différentes. Assurez-vous de cliquer sur « Windows » comme votre système d'exploitation (ou quel que soit le système d'exploitation que vous utilisez) pour vous assurer que vous téléchargez la version correcte.

Ce tutoriel utilisera Python 3, alors cliquez sur le bouton vert de téléchargement sous « Python 3.7 version ». Une fenêtre contextuelle devrait apparaître pour que vous cliquiez sur « Enregistrer » dans le répertoire de votre choix.

![Image](https://cdn-media-1.freecodecamp.org/images/nIBsLmbM3QXFAvKh5DvOgQTAvaIlaEzbtmIO)

Une fois le téléchargement terminé, suivez simplement les étapes de configuration comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/j7MTrYBa-vBDFljeE6ELgJ2Rb1r8XJwfppgg)
_Cliquez sur Suivant_

![Image](https://cdn-media-1.freecodecamp.org/images/xIqTDiWBgQIDNdr6ZKUbe0cD2YDdcHG0znwT)
_Cliquez sur « J'accepte »_

![Image](https://cdn-media-1.freecodecamp.org/images/JK4bVL-3d5CAoMaLIFdWKKN6fOY6iEe54KP2)
_Cliquez sur Suivant_

![Image](https://cdn-media-1.freecodecamp.org/images/82jlqCIonJ-6eSkwL7yIfWZfV8Zw4V6oJayA)
_Choisissez un dossier de destination et cliquez sur Suivant_

![Image](https://cdn-media-1.freecodecamp.org/images/irLpIjKObhEjNp9fguypnF8AQo4FvglVqHDY)
_Cliquez sur Installer avec les options par défaut, et attendez quelques instants pendant qu'Anaconda s'installe_

![Image](https://cdn-media-1.freecodecamp.org/images/cAyLf4jFGXquhZynYWlPinokrY-ZP6RGstLu)
_Cliquez sur Ignorer car nous n'utiliserons pas Microsoft VSCode dans nos tutoriels_

![Image](https://cdn-media-1.freecodecamp.org/images/qdbsbeVWov2V5zW0RXjZSNnYxRFmVivKC3Jn)
_Cliquez sur Terminer, et l'installation est terminée !_

Une fois l'installation terminée, allez dans votre menu Démarrer et vous devriez voir certains logiciels nouvellement installés :

![Image](https://cdn-media-1.freecodecamp.org/images/tOWuum3G7ONEAIhgmji6dYRurvqA5Z2lI1jw)
_Vous devriez voir ceci dans votre menu Démarrer_

Cliquez sur Anaconda Navigator, qui est un hub tout-en-un pour naviguer dans les applications dont nous avons besoin. Vous devriez voir une page d'accueil comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/pGBii7zWZSsvRP9qrBXbRFusVmj5lgcSCIe4)
_Écran d'accueil d'Anaconda Navigator_

Cliquez sur « Lancer » sous Jupyter Notebook, qui est le deuxième panneau sur mon écran ci-dessus. Jupyter Notebook nous permet d'exécuter du code Python de manière interactive sur le navigateur web, et c'est là que nous écrirons la plupart de notre code.

Une fenêtre de navigateur devrait s'ouvrir avec la liste de votre répertoire. Je vais créer un dossier sur mon bureau appelé « Tutoriel Intuitive Deep Learning ». Si vous naviguez vers le dossier, votre navigateur devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/Q7CdWULn4gjQ8GPSGnzIUfvSoD3Dt2dOj-Ud)
_Navigation vers un dossier appelé Tutoriel Intuitive Deep Learning sur mon bureau_

En haut à droite, cliquez sur Nouveau et sélectionnez « Python 3 » :

![Image](https://cdn-media-1.freecodecamp.org/images/27sYFSx5iqHK-y-cxD9sMXXkg7zP9brYRsyS)
_Cliquez sur Nouveau et sélectionnez Python 3_

Une nouvelle fenêtre de navigateur devrait s'ouvrir comme ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/k9-ZWdXld94RG03TXpaM-ELcFerj-kmY7Ldw)
_Fenêtre contextuelle du navigateur_

Félicitations — vous avez créé votre premier notebook Jupyter ! Maintenant, il est temps d'écrire du code. Les notebooks Jupyter nous permettent d'écrire des extraits de code et ensuite d'exécuter ces extraits sans exécuter le programme complet. Cela nous aide peut-être à regarder toute sortie intermédiaire de notre programme.

Pour commencer, écrivons du code qui affichera quelques mots lorsque nous l'exécuterons. Cette fonction s'appelle _print_. Copiez et collez le code ci-dessous dans la boîte grise de votre notebook Jupyter :

```
print("Hello World!")
```

Votre notebook devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/felCZ7xmEgHusNkuzlT5KwoGnjFZl23INRRJ)
_Entrez du code dans notre notebook Jupyter_

Maintenant, appuyez sur Alt-Entrée sur votre clavier pour exécuter cet extrait de code :

![Image](https://cdn-media-1.freecodecamp.org/images/0q66xA7p0oKXMFqmtv0ZzH1ZLGp37LeZ8MKT)
_Appuyez sur Alt-Entrée pour exécuter cet extrait de code_

Vous pouvez voir que le notebook Jupyter a affiché les mots « Hello World! » sur le panneau d'affichage sous l'extrait de code ! Le nombre 1 a également rempli les crochets, ce qui signifie que c'est le premier extrait de code que nous avons exécuté jusqu'à présent. Cela nous aidera à suivre l'ordre dans lequel nous avons exécuté nos extraits de code.

Au lieu de Alt-Entrée, notez que vous pouvez également cliquer sur Exécuter lorsque l'extrait de code est mis en surbrillance :

![Image](https://cdn-media-1.freecodecamp.org/images/ZSo3TOPK1RIkjPhlyrfWhPcscCaYf72XEqOT)
_Cliquez sur Exécuter dans le panneau_

Si vous souhaitez créer de nouveaux blocs gris pour écrire plus d'extraits de code, vous pouvez le faire sous Insérer.

![Image](https://cdn-media-1.freecodecamp.org/images/8PmsMQDCyquKK3GSM9cUWCw1bDOkGedAvsB2)

Jupyter Notebook vous permet également d'écrire du texte normal au lieu de code. Cliquez sur le menu déroulant qui dit actuellement « Code » et sélectionnez « Markdown » :

![Image](https://cdn-media-1.freecodecamp.org/images/R2LdzqHjihNjlx54HHyoSm3qFUurL0fPDbav)

Maintenant, notre boîte grise qui est marquée comme markdown n'aura pas de crochets à côté. Si vous écrivez du texte dans cette boîte grise maintenant et appuyez sur Alt-Entrée, le texte sera rendu comme du texte brut comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/Yb7GdouMsQTeD3136CkR0TxPBZ81w98BBUIP)
_Si nous écrivons du texte dans notre boîte grise marquée comme markdown, appuyer sur Alt-Entrée le rendra comme du texte brut._

Il y a quelques autres fonctionnalités que vous pouvez explorer. Mais maintenant, nous avons configuré Jupyter notebook pour commencer à écrire du code !

### Configuration de l'environnement Anaconda et installation des packages

Maintenant, nous avons configuré notre plateforme de codage. Mais allons-nous écrire du code de Deep Learning à partir de zéro ? Cela semble être une chose extrêmement difficile à faire !

La bonne nouvelle est que beaucoup d'autres ont écrit du code et l'ont mis à notre disposition ! Avec la contribution du code des autres, nous pouvons manipuler des modèles de Deep Learning à un niveau très élevé sans avoir à nous soucier de tout implémenter à partir de zéro. Cela rend extrêmement facile pour nous de commencer à coder des modèles de Deep Learning.

Pour ce tutoriel, nous allons télécharger cinq packages que les praticiens du Deep Learning utilisent couramment :

* Tensorflow
* Keras
* Pandas
* Scikit-learn
* Matplotlib

La première chose que nous allons faire est de créer un environnement Python. Un environnement est comme une copie de travail isolée de Python, de sorte que tout ce que vous faites dans votre environnement (comme l'installation de nouveaux packages) n'affectera pas les autres environnements. Il est bon de créer un environnement pour vos projets.

Cliquez sur Environnements dans le panneau de gauche et vous devriez voir un écran comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/wKXNPPjAOJAtpF7h2qDmHRWPJcZPSTxwXGqA)
_Environnements Anaconda_

Cliquez sur le bouton « Créer » en bas de la liste. Une fenêtre contextuelle comme celle-ci devrait apparaître :

![Image](https://cdn-media-1.freecodecamp.org/images/JYiSWmlNr70YIJmJIzeiwgu4ZGDnGRH1sLH2)
_Une fenêtre contextuelle comme celle-ci devrait apparaître._

Nommez votre environnement et sélectionnez Python 3.7, puis cliquez sur Créer. Cela peut prendre quelques instants.

Une fois cela fait, votre écran devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/ZP0bAkPwg2ehjpiEbfqefPLsV4N7ao6tcqMM)

Remarquez que nous avons créé un environnement « intuitive-deep-learning ». Nous pouvons voir quels packages nous avons installés dans cet environnement et leurs versions respectives.

Maintenant, installons quelques packages dont nous avons besoin dans notre environnement !

Les deux premiers packages que nous allons installer s'appellent Tensorflow et Keras, qui nous aident à utiliser du code plug-and-play pour le Deep Learning.

Dans Anaconda Navigator, cliquez sur le menu déroulant où il est actuellement écrit « Installé » et sélectionnez « Non installé » :

![Image](https://cdn-media-1.freecodecamp.org/images/vQgrLpY-TCpmVQNpE8Qj8lDOXZiMSrnxOxbw)

Une liste complète de packages que vous n'avez pas installés apparaîtra comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1AMaD4UNcBGBOhnRYTkTOA4z7VMXsxi3nVgx)

Recherchez « tensorflow », et cochez les cases pour « keras » et « tensorflow ». Ensuite, cliquez sur « Appliquer » en bas à droite de votre écran :

![Image](https://cdn-media-1.freecodecamp.org/images/42cYM75C41sZ0XQB2VM8SCCE5Smvaa5uFRxo)

Une fenêtre contextuelle devrait apparaître comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/Grmx5-30t2TXd0n20TM3ySlKEp5xStkbQsuC)

Cliquez sur Appliquer et attendez quelques instants. Une fois cela fait, nous aurons Keras et Tensorflow installés dans notre environnement !

En utilisant la même méthode, installons les packages « pandas », « scikit-learn » et « matplotlib ». Ce sont des packages courants que les data scientists utilisent pour traiter les données ainsi que pour visualiser de beaux graphiques dans Jupyter notebook.

Voici ce que vous devriez voir sur votre Anaconda Navigator pour chacun des packages.

**Pandas :**

![Image](https://cdn-media-1.freecodecamp.org/images/VJAyfunO6Bli1IzzaYyr7tPImAmYqtpW87l8)
_Installation de pandas dans votre environnement_

**Scikit-learn :**

![Image](https://cdn-media-1.freecodecamp.org/images/f7d8Fc8ijy-9aXb-nBYSh8mZyMKZedqp-xtw)
_Installation de scikit-learn dans votre environnement_

**Matplotlib :**

![Image](https://cdn-media-1.freecodecamp.org/images/OsHyfrHq4ipaGbL4yzm8FrJguUuZdGTcbLLS)
_Installation de matplotlib dans votre environnement_

Une fois cela fait, retournez à « Accueil » dans le panneau de gauche d'Anaconda Navigator. Vous devriez voir un écran comme ceci, où il est écrit « Applications sur intuitive-deep-learning » en haut :

![Image](https://cdn-media-1.freecodecamp.org/images/pNCTBZKHAKE3o1PqfPMaLo6c-adW8W7sMk70)

Maintenant, nous devons installer Jupyter notebook dans cet environnement. Cliquez donc sur le bouton vert « Installer » sous le logo de Jupyter notebook. Cela prendra quelques instants (encore une fois). Une fois l'installation terminée, le panneau de Jupyter notebook devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/utwIe99nFcwxxpNPDn-1Hufq2PzvnAXrLdvG)

Cliquez sur Lancer, et l'application Jupyter notebook devrait s'ouvrir.

Créez un notebook et tapez ces cinq extraits de code et cliquez sur Alt-Entrée. Ce code indique au notebook que nous allons utiliser les cinq packages que vous avez installés avec Anaconda Navigator plus tôt dans le tutoriel.

```
import tensorflow as tf
```

```
import keras
```

```
import pandas
```

```
import sklearn
```

```
import matplotlib
```

Si aucune erreur ne s'affiche, alors félicitations — vous avez tout installé correctement :

![Image](https://cdn-media-1.freecodecamp.org/images/saAFY17Par0VXZyDXdi332aKEXsLIZ9527a8)
_Un signe que tout fonctionne !_

Maintenant que nous avons tout configuré, nous allons commencer à construire notre premier réseau de neurones ici :

[**Construisez votre premier réseau de neurones pour prédire les prix des maisons avec Keras**](https://medium.com/intuitive-deep-learning/build-your-first-neural-network-to-predict-house-prices-with-keras-eb5db60232c)  
[_Un guide complet étape par étape pour les débutants pour construire votre premier réseau de neurones en quelques lignes de code comme un Deep..._medium.com](https://medium.com/intuitive-deep-learning/build-your-first-neural-network-to-predict-house-prices-with-keras-eb5db60232c)

Si vous avez eu des difficultés avec l'une des étapes ci-dessus, n'hésitez pas à commenter ci-dessous et je vous aiderai !

**À propos de l'auteur :**

Bonjour, je suis [Joseph](http://ai.stanford.edu/~josephlee) ! J'ai récemment obtenu mon diplôme de l'Université de Stanford, où j'ai travaillé avec Andrew Ng dans le [Stanford Machine Learning Group](https://stanfordmlgroup.github.io/). Je veux rendre les concepts de Deep Learning aussi intuitifs et aussi faciles à comprendre que possible par tout le monde, ce qui a motivé ma publication : [Intuitive Deep Learning](https://medium.com/intuitive-deep-learning).