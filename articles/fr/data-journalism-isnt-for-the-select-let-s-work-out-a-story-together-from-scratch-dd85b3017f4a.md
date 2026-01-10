---
title: 'Guide du débutant pour le journalisme de données : construisons une histoire
  à partir de zéro'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-11T05:46:11.000Z'
originalURL: https://freecodecamp.org/news/data-journalism-isnt-for-the-select-let-s-work-out-a-story-together-from-scratch-dd85b3017f4a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*07n6A78xm2DwOM0mbeGvVA.jpeg
tags:
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: Design
  slug: design
- name: startup
  slug: startup
- name: technology
  slug: technology
seo_title: 'Guide du débutant pour le journalisme de données : construisons une histoire
  à partir de zéro'
seo_desc: 'By Mina Demian

  This is an introductory guide on how to produce the beginnings of a piece of data
  journalism. We’re going to walk through it together, as I outline the key things
  to consider before starting. We’ll cover:


  how to structure your work

  a ...'
---

Par Mina Demian

Ce guide d'introduction explique comment produire les débuts d'un article de journalisme de données. Nous allons le parcourir ensemble, tandis que j'explique les points clés à considérer avant de commencer. Nous aborderons :

* comment structurer votre travail
* un processus de base à suivre
* une étude de cas réelle pour montrer comment ce processus fonctionne

### Le journalisme de données reste une question d'histoires

Le glamour et l'éclat du journalisme de données (les [animations](http://www.slate.com/articles/life/the_history_of_american_slavery/2015/06/animated_interactive_of_the_history_of_the_atlantic_slave_trade.html), les [cartes frappantes](http://www.wired.com/2013/12/the-best-maps-of-2013/) et ces excellents [infographies](https://yalantis.com/media/content/ckeditor/2014/06/poster_coffee_2-01.jpg)) sont partout sur Internet. Il est facile de penser, alors, que cela concerne les données et à quel point vous pouvez les rendre belles, chantantes ou dansantes. Mes sages amis d'[OpenUp](http://openup.org.za/), [Raymond](http://twitter.com/rayjoe) et [Adi](http://twitter.com/SoapSudTycoon) me rappellent (ainsi qu'à l'Internet bavant dans son ensemble) que l'accent doit être mis sur le journalisme de _données_, et non sur le journalisme de _données_.

Le journalisme de données ne diffère pas du journalisme que nous connaissons et consommons chaque jour. Là où le journalisme traditionnel s'appuie sur des sources humaines (par exemple, des initiés, des experts, des universitaires et des scientifiques), le journalisme de données traite les sources de données (par exemple, des feuilles de calcul, des sites web et des bases de données) avec la rigueur et le discernement que les journalistes appliquent aux sources humaines.

Les animations et les travaux élégants aident à communiquer le produit final — l'histoire — mais ils ne remplaceront jamais l'histoire _elle-même_.

### Le grand départ

Une histoire de journalisme de données peut commencer par un événement important ou simplement par une question. Vous pouvez voir un titre d'actualité et vous demander combien _x_ il a fallu pour que _y_ se produise ? Ou vous pensez à la nourriture et vous vous demandez combien le consommateur moyen dépense en nourriture pour chiens. Les deux questions sont valides et constituent de bons points de départ pour évaluer un sujet pour le journalisme de données.

Ce que j'ai appris jusqu'à présent dans mon travail, c'est qu'il y a peu de différence entre le travail de la science de base et celui du journalisme de données. Vous faites une observation, vous formulez une question (hypothèse pour les puristes), puis vous essayez de répondre à cette question. Votre travail montrera soit que votre hypothèse initiale était effectivement incorrecte, soit que, oui, elle était effectivement correcte.

Ainsi, comme je l'ai mentionné précédemment, il ne s'agit pas des graphiques sophistiqués ou de la quantité de données que vous avez parcourues, mais de savoir _quelle est votre question_ et _l'avez-vous répondue_ ?

Ne croyez pas le battage médiatique.

#### « [Qui sont vos données et que font-elles](https://youtu.be/imqapaYAPbY?t=17) ? »

Ce guide est basé sur des données de l'agence de statistiques d'Afrique du Sud [statssa.gov.za](http://blog.minademian.com/2015/08/17/from-idea-to-the-start-of-a-story/statssa.gov.za). (Les résultats de l'enquête trimestrielle publiée à l'été 2015 montrent un taux de chômage officiel de 25 %, un chiffre alarmant.) L'agence a eu la gentillesse de publier les données dans une feuille de calcul Excel. J'écrirai des articles sur la manière de gérer les sources de données qui ne sont pas publiées dans un format facile à utiliser.

[Vous pouvez explorer le jeu de données ici](https://drive.google.com/drive/folders/1sh0UOYoJm2G_O7JbyXnMQCH2kp5LRlaI), et il y a suffisamment de feuilles pour justifier une exploration. Cette exploration est importante car, sans savoir de quoi il s'agit, ce qu'il couvre, etc., vous pourriez regarder les mauvaises données. Cela pourrait vous amener à répondre à la mauvaise question ou — le cauchemar de tout journaliste de données — perdre des heures tout en accomplissant très peu.

Alors, avant de parler du processus, examinons les données et voyons ce qu'elles nous disent. Nous ne travaillons généralement pas avec toutes les données (sauf si notre idée ou question initiale l'exige). Il est préférable de d'abord examiner toutes les données, puis de se concentrer sur une section particulière qui attire votre attention.

Les feuilles de calcul de l'agence de statistiques examinent différentes caractéristiques de la main-d'œuvre (réparties par province, âge, sexe et démographie). Même si c'est votre première fois, parcourez rapidement chaque feuille. Cela aidera à développer une éthique de travail méthodique qui est inestimable pour le journalisme de données.

Une note importante : vous n'avez besoin que d'une connaissance de base du fonctionnement d'Excel. Je ne fais pas de magie sur les feuilles de calcul, donc tout le monde peut les suivre. Pour faire court (et pour que vous ne tombiez pas dans un stupre catatonique), je vous laisse découvrir comment effectuer les manipulations de base dans Excel.

### Maintenant, le voyage commence

Nous avons parlé de ce que signifie produire un travail de journalisme de données, de la manière d'évaluer si une idée mènera à un article, et de la manière d'examiner un jeu de données. Enfin. Nous arrivons au processus, le bon côté des choses. Comment cela fonctionne-t-il ?

#### Étape 1 : Prendre une bouchée des données

Pour ce guide, je veux connaître la taille de la main-d'œuvre de chaque province en Afrique du Sud, et comment elle a évolué entre 2013 et le deuxième trimestre de 2015. Ces données sont affichées dans la première feuille de calcul. (Vous êtes libre d'examiner les autres feuilles de calcul pour voir quelles informations intéressantes vous pouvez en extraire.)

Nous sommes donc passés de la feuille de calcul originale, qui contient plus de 20 feuilles de calcul, comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/WqsSo2YVxhn7UAnZ0ikTpmtPC0qjajuYyFEi)

À travailler avec une seule feuille de calcul, intitulée « Tableau 1 : Population en âge de travailler (15–64 ans) », comme montré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/an86Mr2aOLTx6X3xBrrdsynfwGJsFTf0XhwZ)

Maintenant, copions les données en bas de la feuille, puisque ce sont les données que nous voulons, et collons-les dans une nouvelle feuille de calcul. Pour obtenir un jeu de données propre, supprimez la ligne avec l'en-tête « Milliers » et supprimez la cellule étiquetée « Afrique du Sud ». Supprimez également la ligne « Totaux » pour ne pas nous confondre plus tard. (Je vais ajuster toutes les valeurs pour refléter les millions dans une minute.)

Cela devrait maintenant ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/yWOca0w2kWIizHjS2DPEp48-ScJQqaMuK-oV)

Maintenant, changeons toutes les cellules pour afficher les valeurs en millions. Créez une nouvelle colonne à côté de chaque colonne existante, et multipliez la valeur par 1000. Cela ressemble maintenant à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/KJu-xx0g9xGwgXFDedYqBN7hKSfJfrOTndVM)

Supprimez toutes les bordures et les décimales, et faites en sorte que le séparateur de milliers soit une virgule. Cela aide à rendre notre tableau plus facile à lire et plus accessible. À ce stade, ce tableau devrait être prêt à être analysé.

Pas tout à fait encore. Bien qu'il soit plus propre, la structure de données dont nous avons besoin n'est pas là. Pourquoi est-ce important ? Parce que les données doivent être organisées de manière à pouvoir les agréger ou les regrouper. Les vieux sages du journalisme de données disent que si vos données ne sont pas résumées (ou agrégées), elles ne sont pas prêtes à être analysées.

#### Étape 2 : Transformer les données en une structure prête pour l'analyse/visualisation

Quels facteurs cherchons-nous à exposer à partir de ce jeu de données ? Il s'agit de la province, de l'année et du nombre total de travailleurs. Mais avant cela, nous allons créer cette nouvelle structure de données avec les colonnes suivantes :

![Image](https://cdn-media-1.freecodecamp.org/images/lVYnJSJJMweDcINW81DySayeqLOJRc0nlEkA)

Si vous avez étudié la conception de bases de données, vous échoueriez à votre test de conception de bases de données pour présenter cette conception de jeu de données. Ou si vous êtes programmeur, votre patron vous réprimanderait pour avoir proposé cette conception de jeu de données. Votre conférencier ou patron aurait raison de le faire. Ce n'est pas un jeu de données _normalisé_ (en termes de science informatique, optimisé). Cependant, il s'agit d'une analyse de données pour un article de journalisme de données, vous pouvez donc ignorer ces règles ! Nous devons avoir des lignes en double afin d'agréger les données plus tard (vous vous souvenez ?).

#### Étape 3 : Produire le jeu de données final

Dans la capture d'écran ci-dessus, j'ai entré les années pertinentes dans la structure. Ensuite, collez les totaux pour 2013, 2014 et 2015. Le jeu de données ressemble maintenant à [ci](https://docs.google.com/spreadsheets/d/1_9TAVYVXGOhAsfr3rXSUwJndOAmW-MOyOQtZ2MpBtWY/pubhtml?gid=1928330136&single=true&widget=true&headers=false). (Medium ne permet pas les intégrations iframe, donc j'ai plutôt fourni un lien vers le jeu de données.) Il devrait avoir 91 lignes, et seul le premier trimestre et le deuxième trimestre sont indiqués pour 2015.

Nous y sommes presque !

La dernière étape consiste à agréger les données. Prenez donc une profonde inspiration et créez un tableau croisé dynamique dans une nouvelle feuille. Nos données résumées ressemblent à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/OeoFggrG2StmeVXWo95ZPfO-0RnbSs7czPNk)

Nettoyez le tableau. Entrez le séparateur de milliers, supprimez les décimales et supprimez la cellule étiquetée « Somme des étiquettes de ligne totales ». Le tableau ressemble maintenant à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/tFSgz0MCqOjMgG-zBaeHiLw5Awqbym6zc0gS)

#### Étape 4 : Produire la visualisation

Félicitations ! Vous avez un jeu de données prêt à être visualisé.

Nous allons utiliser [Infogr.am](http://www.infogram.com) pour produire une infographie. Ce guide ne couvre pas comment s'inscrire et utiliser Infogr.am, donc (comme avec Excel) vous devrez vous familiariser avec l'outil par vous-même. Je vous assure que c'est simple et intuitif ! Vous l'utiliserez comme un professionnel en un rien de temps ! Vous verrez.

Pour créer une nouvelle infographie, choisissez n'importe quel modèle que vous aimez. La zone de travail vide ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/k91odKoXes6fXz8ZhwcI07-94H3M6SnIjsMR)

Donnez à l'infographie un titre comme « Main-d'œuvre totale dans les provinces, 2013–2015 » ou quelque chose de similaire, comme vous le jugez approprié. Ajoutez ensuite un graphique à barres groupées à partir de l'assistant popup. Vous devriez voir le nouveau graphique dans la zone de travail. (Supprimez le graphique existant qui accompagne le modèle, qui apparaît maintenant sous celui que vous venez de créer.)

Double-cliquez sur le nouveau graphique, et une interface similaire à Excel apparaîtra à l'écran. Supprimez les données de cet écran, copiez les données de la feuille de calcul Excel utilisée dans le tableau croisé dynamique, et collez-les dans l'interface de feuille de calcul Infogr.am. Cela devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/WkRRKLSQvnC6JrozTVj6ma9SptVV-ohFCKnr)

Lorsque vous collez les données, le graphique se met automatiquement à jour.

Cela commence à avoir fière allure !

Jetez un coup d'œil à l'infographie. Tout y est, mais vous ne comprendrez peut-être pas immédiatement l'infographie. Vous devez faire défiler vers le bas pour lire la légende et voir quelle couleur correspond à quelle province. Au lieu de reformater les données, cliquez sur l'icône des flèches bidirectionnelles dans le coin supérieur droit de la feuille de calcul. Cette fonction pratique inversera les lignes et les colonnes de sorte que les provinces apparaissent maintenant dans les lignes et les années dans les colonnes.

![Image](https://cdn-media-1.freecodecamp.org/images/3IEq8mM956m4YxZWJOn3TolJwCMgbT3Pk1gN)

Essayez toujours d'afficher les valeurs sur le graphique, le cas échéant. Cliquez donc sur le bouton « Afficher les valeurs » et les totaux s'afficheront sur le graphique. Cliquez également sur le bouton « Paramètres » et faites défiler vers le bas pour ajouter « total (en millions) » dans la zone de texte de l'axe X. Cela aide le lecteur (et vous) à mieux comprendre le graphique.

Cliquez sur le bouton « Publier » pour donner un titre à votre graphique. Décidez ensuite si vous souhaitez que le graphique soit interactif ou une image. Voici à quoi ressemblerait l'image finale :

![Image](https://cdn-media-1.freecodecamp.org/images/UmHeH7lX-xu6ab0-1mXridcr-T9pFyp1kfHw)

Et vous avez produit votre première visualisation. Faites-vous une tape dans le dos, prenez un café ou une bière, et préparez-vous car vous venez de commencer le processus.

Avant d'examiner le reste du travail, revoyons ce que nous avons fait :

1. Nous avons examiné une source de données et extrait les données que nous voulons. Dans ce cas, nous avons demandé : « Quelle était la taille de la main-d'œuvre en Afrique du Sud entre 2013 et 2015 ? »
2. Nous avons suivi un processus de base de nettoyage, de formatage, de transformation et de résumé des données jusqu'à ce que nous produisions un tableau montrant les données dont nous avons besoin.
3. Nous avons ensuite inséré les données dans notre outil de visualisation et produit une infographie, comme montré ci-dessus.

À ce stade, vous êtes si excité que vous sautez sur Twitter ou votre email, et envoyez votre travail à toutes les personnes que vous connaissez.

Attendez ! Pas encore.

### **Que signifient vraiment vos résultats ?**

Oui, vous avez analysé les données et répondu à votre question. La province de Gauteng avait la plus grande main-d'œuvre pendant la période que nous avons sélectionnée, mais elle diminue depuis 2013. La main-d'œuvre du Cap-Nord a été constamment inférieure à 5 millions depuis 2013. Mais _pourquoi_ ?

C'est pourquoi le premier paragraphe de cet article avait cette qualification espiègle — « les débuts d'une histoire » — car maintenant commence le journalisme tel que vous le connaissez ou avez été formé à le faire. À ce stade, faites ce qui suit :

* contactez des analystes, des experts ou des universitaires pour interpréter et commenter les données.
* examinez d'autres jeux de données ou demandez à des experts d'expliquer le contexte des résultats, en fonction de l'ampleur de l'histoire ou des instructions de votre rédacteur en chef.
* analysez/visualisez d'autres jeux de données pour tester et affiner vos résultats.
* faites tout ce qui est nécessaire pour vous assurer que l'article est équilibré et juste.

Après avoir terminé une ou plusieurs de ces étapes, écrivez l'article final. Incluez l'infographie produite ci-dessus et soumettez-la pour publication. Si vous gérez votre propre blog ou site web, publiez-la en direct.

### Il n'y a pas de place comme la fin !

Et c'est la fin. J'espère que vous êtes arrivé jusqu'ici et que votre appétit a été aiguisé pour faire plus de travail (et plus sophistiqué) dans le journalisme de données.

Si quelque chose n'a pas fonctionné pour vous, ou si vous avez besoin d'aide pour une section, suivez-moi sur [Twitter](http://twitter.com/minaddotcom) et nous pourrons le résoudre ensemble.

### Ressources

J'ai inclus ci-dessous toutes les feuilles de calcul, outils et liens afin que vous puissiez reprendre ce guide à tout moment et voir comment je suis arrivé à l'infographie finale.

* [Feuille de calcul originale de l'agence nationale de statistiques](https://drive.google.com/file/d/0B4RhkUC9QKOnV1pXbUlCY2diSlE/view?usp=sharing) en Afrique du Sud
* Ma [feuille de calcul](https://docs.google.com/spreadsheets/d/1_9TAVYVXGOhAsfr3rXSUwJndOAmW-MOyOQtZ2MpBtWY/edit?usp=sharing) avec une feuille de calcul pour chaque étape montrée dans les captures d'écran ci-dessus
* [Infogr.am](http://www.infogr.am/)

_Mina Demian est un ingénieur front-end vivant à Stockholm, en Suède. Cet article a été [publié à l'origine sur son blog personnel](http://blog.minademian.com/2015/08/17/from-idea-to-the-start-of-a-story/), pendant son temps en tant que journaliste et vérificateur de faits. Il s'adonne encore à l'analyse et à la visualisation de données._