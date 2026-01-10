---
title: Comment créer votre propre SaaS – Un clone de PagerDuty
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2022-12-20T13:47:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-your-own-saas-pagerduty-clone
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/maxresdefault.jpeg
tags:
- name: SaaS
  slug: saas
- name: youtube
  slug: youtube
seo_title: Comment créer votre propre SaaS – Un clone de PagerDuty
seo_desc: One of the best ways to learn software development is to create a slimmed-down
  version of software you use every day to get a better understanding of how it might
  work. This process helps you understand the problem space constraints and techniques
  re...
---

L'un des meilleurs moyens d'apprendre le développement logiciel est de créer une version simplifiée des logiciels que vous utilisez quotidiennement afin de mieux comprendre leur fonctionnement. Ce processus vous aide à appréhender les contraintes de l'espace de résolution de problèmes et les techniques nécessaires pour construire un cas d'utilisation réel.

Nous venons de publier un cours sur la chaîne YouTube de freeCodeCamp.org qui vous apprendra à créer votre propre application SaaS. Dans ce cas précis, un clone de PagerDuty.

Ania Kubów a développé ce cours. Elle crée des tutoriels logiciels populaires à la fois sur la chaîne freeCodeCamp et sur sa propre chaîne.

Dans ce tutoriel, Ania vous apprendra à construire un tableau de bord pour vous informer si votre application est hors service. Et si votre application tombe en panne, vous serez averti par e-mail et par SMS. Il s'agit d'un clone de la célèbre application de logiciel en tant que service (SaaS) appelée PagerDuty.

Dans ce tutoriel, nous allons recréer certains des composants clés de cette application en utilisant JavaScript pour la logique applicative, Postgres pour stocker nos données, et Twilio pour gérer les notifications SMS et le SMTP.

À la fin de ce tutoriel, vous serez capable de :

* Créer des structures de données dans Postgres pour alimenter votre application.
* Créer une UI et y injecter des données.
* Ajouter des fonctionnalités à l'UI pour interagir avec les données et les modifier.
* Et enfin, connecter Twilio et le SMTP pour envoyer des notifications par e-mail et par SMS.

Voici toutes les sections de ce cours :

* Travailler avec des composants UI pré-faits
* Configurer notre base de données Postgres
* Créer des tables dans Postgres
* Alimenter notre tableau de bord en données
* Ajouter de nouveaux incidents
* Supprimer des incidents
* La page des membres de l'équipe
* Connecter l'API Twilio et SMTP

Regardez le cours complet ci-dessous ou sur [la chaîne YouTube de freeCodeCamp.org](https://youtu.be/4xuBT3BbsYU) (durée : 1 heure).

%[https://youtu.be/4xuBT3BbsYU]

## Transcription de la vidéo

(générée automatiquement)

Bonjour à tous sur la chaîne freeCodeCamp. Dans ce tutoriel, je vais construire un outil que toute application de startup devrait avoir.

Je vais construire un tableau de bord pour vous informer si votre application est en panne. Et si c'est le cas, elle vous avertira par e-mail et par SMS.

En d'autres termes, un clone de la célèbre application SaaS PagerDuty.

Je m'appelle Ania Kubow. Je suis créatrice de cours ici sur freeCodeCamp, ainsi que sur ma propre chaîne.

Et je serai votre guide pour ce merveilleux tutoriel sur la construction de cette plateforme aujourd'hui.

L'un des meilleurs moyens d'apprendre le développement logiciel est de créer une version simplifiée des logiciels que vous utilisez tous les jours pour mieux comprendre comment ils pourraient fonctionner.

Ce processus vous aide à comprendre les contraintes et les techniques requises pour construire un cas d'utilisation réel. PagerDuty est génial car il aide à alerter les équipes sur les incidents de haute priorité comme les pannes web ou les problèmes de sécurité en utilisant des stratégies de configuration pré-configurées et des notifications multi-canaux.

Dans ce tutoriel, nous allons recréer certains des composants clés de cette application en utilisant JavaScript pour notre logique applicative.

Postgres pour stocker nos données, les résultats des autres interfaces utilisateur et les flux de travail back-end.

Et enfin Twilio pour gérer les notifications SMS ainsi que le SMTP.

À la fin de ce tutoriel, vous serez capable de créer des structures de données dans Postgres pour alimenter votre application.

Cela inclura la création d'une table d'incidents ainsi qu'une table de membres d'équipe. Nous injecterons ensuite ces données dans notre UI afin de pouvoir les voir et interagir avec elles.

Comme vous le verrez ici sous l'onglet des incidents et l'onglet des membres de l'équipe, nous récupérons toutes ces données.

L'onglet Membres de l'équipe nous aidera également à voir qui travaille sur quoi, ainsi que leurs horaires de service afin que nous puissions savoir qui est d'astreinte.

Et quand nous pourrons également voir tous les incidents qui sont actuellement reconnus et en cours de traitement, ainsi que les filtrer pour n'afficher que ceux assignés à un utilisateur spécifique.

Nous ajouterons des fonctionnalités pour afficher les données si nous cliquons sur des lignes spécifiques, et bien plus encore. Nous ajouterons également la possibilité d'ajouter des membres d'équipe depuis l'interface ainsi que d'ajouter de nouveaux incidents via l'interface, et de supprimer un membre d'équipe ou une interface.

Il se passe donc beaucoup de choses ici.

Et enfin, nous connecterons Twilio et le SMTP. Afin de pouvoir envoyer des notifications par e-mail et par SMS aux membres de notre équipe au cas où le site web tomberait théoriquement en panne.

Cette vidéo est créée grâce à une subvention de Retool, la solution locale pour construire des outils et des plateformes internes.

Alors, qu'attendons-nous ? C'est parti. D'accord, allons-y.

Tout d'abord, je vais juste créer une nouvelle application.

Je vais donc cliquer ici.

Et je vais l'appeler pager duty clone.

D'accord, et cliquez sur créer l'application.

Voilà, nous venons de créer notre application, c'est essentiellement notre zone de travail.

Et je vais commencer par faire glisser des éléments d'UI pour que cela ressemble à un clone de PagerDuty.

La première chose que je vais faire est de faire glisser un conteneur d'onglets, car nous allons avoir deux onglets ici, l'un pour voir les incidents et l'autre pour voir tous les membres de notre équipe.

Faisons en sorte que cela se reflète ici.

Nous pouvons également renommer ce composant UI.

Je peux donc l'appeler main tabs si je le souhaite.

D'accord, super.

Et ici, je vais juste changer cela pour dire incidents.

Et celui-ci pour dire membres de l'équipe.

Nous créons donc littéralement notre conteneur d'onglets, juste comme ça.

Nous pouvons bien sûr aussi changer les couleurs de ceci.

Si vous mettez en évidence tout le composant UI, puis descendez ici, je peux choisir la couleur d'arrière-plan de l'en-tête, la couleur d'arrière-plan du pied de page, ou je pourrais juste choisir l'arrière-plan, je vais choisir Canvas pour qu'il corresponde à l'arrière-plan que nous avons.

D'accord, et si nous le voulions un peu plus foncé, nous pouvons aussi choisir notre propre couleur personnalisée.

Par exemple, je pourrais mettre l'hexadécimal E, E, E, ou juste trois E pour faire court.

Et cela sera également appliqué.

Merveilleux.

Pour se débarrasser de la troisième vue que nous n'allons pas utiliser, allez simplement ici et supprimez-la de la vue.

Voilà, une vue et une deuxième vue.

Nous pouvons également personnaliser les couleurs sélectionnées.

Je vais opter pour le vert pour l'instant car je pense que c'est plus joli.

D'accord.

Merveilleux.

Maintenant, sous incidents, que voulons-nous afficher ? Eh bien, nous devrions probablement avoir une sorte d'en-tête, n'est-ce pas.

Alors choisissons une option de texte, nous allons avoir un texte simple, ou une zone de texte, ou un éditeur de texte enrichi, ou même du texte éditable, je vais juste choisir l'option texte.

Et nous pouvons même choisir si nous souhaitons utiliser des éléments HTML pour décider de la taille de chaque élément de texte.

Je peux donc avoir "incidents sur toutes les équipes" comme titre, juste comme ça.

Et c'est stylisé comme un titre d'élément h1.

Si vous vouliez donner un style personnalisé à cet élément h1, c'est également possible, d'accord, tout ce que vous auriez à faire est d'aller dans scripts et styles et d'ajouter du CSS personnalisé pour tout ce document.

Nous ne allons pas faire cela maintenant.

Mais je pensais que cela valait la peine de vous en donner un aperçu.

Ensuite, qu'est-ce que je veux ? Eh bien, nous pouvons avoir des séparateurs pour séparer tout ce qui se trouve ici.

Je vais en fait utiliser un séparateur pour séparer le titre du tableau que nous allons insérer.

Maintenant, insérons un tableau.

Notre tableau pour le moment ne va pas signifier grand-chose.

D'accord, il va juste avoir des données fictives.

Il y a des données fictives qui sont injectées, nous allons tout supprimer car nous allons utiliser des données réelles provenant d'une base de données Postgres que nous allons créer.

Laissez donc cela vide pour l'instant.

En attendant, je vais aussi faire glisser du texte pour le mettre en dessous ici.

Et je vais utiliser l'élément H5 cette fois, donc un en-tête plus petit pour dire, vos incidents ouverts, puis faites glisser un peu plus de texte, afin que nous puissions réellement voir ces incidents.

Pour l'instant, je vais mettre zéro déclenché et mettre cela en rouge.

Le texte sera donc "danger".

Et puis copiez et collez cela.

Et cette fois, ce sera pour afficher nos incidents reconnus.

Et je vais changer cette couleur pour qu'elle soit "info".

D'accord, merveilleux.

Il y a beaucoup de choses que vous pouvez faire avec le style de ce texte, je vais le laisser comme ça pour l'instant.

Et nous allons choisir ce nombre dynamiquement en fonction de, vous l'avez deviné, notre base de données.

En fait, je vais juste copier ceci et le coller parce que nous allons faire glisser cela vers la droite et voir tous nos incidents ouverts également.

Nous avons donc vos incidents ouverts, ayons aussi tous les incidents ouverts.

Et encore une fois, nous allons injecter ce nombre dynamiquement sur le composant text 7 et le composant text 5.

Super.

Maintenant, je vais ajouter un bouton, ce bouton une fois cliqué, va nous aider à ajouter un nouvel incident à notre base de données.

Nous pouvons donc faire cela depuis notre UI, ce qui est plutôt cool.

Et ce bouton, nous pouvons le styliser.

Je peux avoir un incident si je le souhaite.

Et faisons-le bleu, vert juste pour correspondre au reste de ce tableau.

Et je peux même choisir de le rendre un peu plus grand.

Ensuite, je vais juste utiliser un conteneur pour contenir un tas de choses que je veux ajouter ensuite.

Je vais donc le mettre ici comme ça pour l'instant.

Et cette fois, en fait, je vais me débarrasser de l'en-tête.

Nous pouvons faire cela, nous pouvons sélectionner tout le composant UI, puis je peux choisir de masquer l'en-tête.

Donc pour le moment, nous ne montrons que le corps, si vous vouliez montrer le pied de page, vous pouvez le faire.

C'est totalement à vous de décider.

D'accord, merveilleux.

Nous avons donc un conteneur, je vais en fait en avoir deux, donc je vais juste en faire glisser un autre juste en dessous ici.

D'accord, voilà.

Celui-ci encore, je ne veux pas d'en-tête affiché, donc je vais le masquer maintenant et le premier, nous allons juste afficher qui est d'astreinte.

Je vais donc juste mettre le titre ici "d'astreinte".

D'accord, et je vais le mettre en vert.

Je vais donc changer la couleur du texte en vert.

Nous pouvons aussi le mettre en gras si nous le souhaitons.

D'accord, je vais juste utiliser une balise d'ouverture et de fermeture pour cela pour mettre ce nom en gras. La prochaine chose que je vais faire glisser est un endroit pour afficher réellement celui qui est actuellement d'astreinte.

Pour l'instant, je vais juste mettre x x x car nous ne savons pas encore qui est d'astreinte.

Parce que, encore une fois, nous allons obtenir cela de notre base de données.

Je vais aussi m'assurer que c'est un élément h3, juste comme ça, juste pour m'assurer que c'est un peu plus gras.

Et nous pouvons même utiliser un avatar.

Je peux donc simplement faire glisser un composant pré-fait.

C'est vrai, cela nous montrera notre avatar.

Pour le moment.

Encore une fois, c'est juste basé sur mes informations, mes détails d'utilisateur, je suis l'utilisateur actuel de cette application.

Mais nous allons écraser cela.

En fait, pour ne pas oublier de le faire, je vais juste mettre x x x pour tout cela afin que nous n'oubliions pas d'ajouter cela dynamiquement.

Super.

Maintenant, nous pouvons mettre un séparateur ou nous pouvons ajouter un pied de page, c'est totalement à vous de décider.

Choisissons d'ajouter un pied de page.

Et dans le pied de page, ici, je vais ajouter plus d'informations, je vais faire glisser un composant texte, juste comme ça.

Et ici, je vais mettre en gras "vous êtes d'astreinte pour".

Et encore une fois, cela sera alimenté dynamiquement, je vais essentiellement créer une liste de tags.

Nous pouvons donc trouver ces tags ici aussi.

Et je vais juste les mettre en dessous.

Juste comme ça.

D'accord, donc cela va afficher ce pour quoi nous sommes d'astreinte en tant que personne d'astreinte.

Ici, encore une fois, je vais juste faire glisser un peu plus de texte, cela va dire "et d'astreinte maintenant".

Allons-y et mettons cette couleur en vert.

Et ici, nous allons juste lister tous les incidents pour lesquels nous sommes actuellement d'astreinte.

D'accord, je vais mettre des x pour l'instant car cela sera alimenté dynamiquement.

Et nous allons également montrer le service de la personne actuelle qui est d'astreinte.

Pour que ce soit vraiment évident.

Je vais mettre encore une fois en gras "votre service", puis fermer cette balise.

Et ensuite afficher réellement les deux heures de service ainsi que quelques informations de contact.

Cela va donc être "de", nous allons mettre notre heure de début de service, et cela va être "à" et nous allons mettre l'heure de fin de service de la personne actuelle d'astreinte.

Et ici, je vais juste mettre des informations comme contact.

Et puis je vais mettre info @ freecodecamp.org en prétendant que c'est l'application PagerDuty de freeCodeCamp pour apporter des modifications à votre service.

Merveilleux.

C'est vraiment tout.

D'accord, c'est pour afficher tous les incidents.

Bien sûr, nous n'avons pas encore connecté cela à des données.

Travaillons sur l'onglet des membres de l'équipe ensuite.

Donc, tout comme avec l'onglet des membres de l'équipe, en fait, ce que je vais faire est super simple, je vais juste copier ceci, je vais copier le séparateur, nous allons copier le bouton.

Et je vais aussi copier ce conteneur et cliquer sur Command C.

Et à l'intérieur d'ici, je vais juste le coller.

D'accord, cela se ressemble un peu.

Nous allons changer ce titre pour dire, membres de l'équipe, d'accord.

Et sur le bouton Ajouter un incident, eh bien, je vais mettre ajouter un nouveau membre d'équipe, bien sûr, car il s'agit des membres de l'équipe.

Et ici, eh bien, supprimons cela, nous ne voulons pas vraiment cela, je vais juste montrer le membre de l'équipe sélectionné dans le tableau que nous allons avoir, nous n'allons pas avoir d'avatar.

Alors supprimons cela, nous n'allons pas avoir "votre d'astreinte pour", à la place, nous allons avoir "opérations assignées".

Afin que nous puissions voir les opérations assignées qui sont là pour l'utilisateur.

D'accord, voilà, nous avons les mêmes opérations qui seront visualisées sous forme de liste de tags.

Et je vais aussi mettre les dates de service pour l'utilisateur que nous sélectionnons.

D'accord, donc encore une fois, en gras, je vais juste mettre "dates de service" et fermer cela.

D'accord, et encore une fois, mettons "de" "à" et ensuite je vais aussi mettre l'e-mail de la personne que nous voulons contacter.

D'accord, donc notre e-mail va y aller.

Super.

Maintenant, un petit plus est aussi de faire glisser un tableau, car cela va montrer tous nos membres d'équipe à partir de, vous l'avez deviné, notre base de données Postgres.

Alors allons-y et supprimons toutes ces données.

Ce sont des données factices qui ont été transmises.

Et enfin, en dehors des incidents et en dehors des membres, donc en dehors de tout ce conteneur d'onglets, je vais avoir un autre conteneur.

D'accord, je vais mettre un conteneur.

En fait, créons un formulaire, car essentiellement, nous allons envoyer quelque chose d'ici, nous allons envoyer un e-mail.

D'accord.

Voilà, il y a un formulaire d'e-mail pour nous.

Et je vais juste mettre "compositeur d'e-mail", car c'est ce que je veux construire, faisons du titre de ceci l'en-tête, je vais changer la couleur de l'en-tête.

Si nous trouvons l'arrière-plan de l'en-tête, je vais juste opter pour "highlight" comme couleur de choix.

Et changeons le bouton de soumission pour, je vais en faire un "warning".

D'accord, et ici je vais mettre "envoyer à", et ensuite quiconque nous mettons en évidence parmi les membres de l'équipe sera la personne qui recevra cet e-mail.

Cela va donc être assez cool.

Et une autre chose que nous pouvons faire est d'utiliser l'éditeur de texte enrichi.

Maintenant nous avons tout un composant d'éditeur de texte enrichi, c'est plutôt cool.

D'accord, imaginez essayer de coder cela vous-même.

Et ici, nous allons mettre Salut, et nous allons juste mettre l'utilisateur sélectionné de notre tableau.

C'est tout.

C'est ce que nous avons construit jusqu'à présent.

Maintenant, passons à la liaison de tout cela.

Pour ce tutoriel, je vais utiliser render.com. render.com est essentiellement un moyen pour nous d'héberger notre base de données de manière non payante.

D'accord, alors s'il vous plaît, allez sur le tableau de bord, inscrivez-vous, allez sur le tableau de bord.

Et nous allons nous connecter, je vais juste choisir de me connecter avec Google.

D'accord, veuillez choisir votre propre façon de vous connecter, c'est à vous de décider.

Et une fois que vous y êtes, vous devez cliquer sur New, et c'est une base de données Postgres que nous allons créer qui est hébergée sur render, je vais l'appeler pager duty car c'est pour cela que je crée cette base de données, je suis d'accord pour que la base de données soit générée aléatoirement, ainsi que le nom d'utilisateur.

Et nous allons juste sélectionner le niveau gratuit et cliquer sur create database.

D'accord, c'était vraiment aussi simple que cela, c'est en cours de création.

En attendant, je vais aller ici et aller dans resources.

Allons-y et créons une nouvelle ressource, ce sera une base de données Postgres SQL, je vais juste l'appeler pager duty, car ce sera facile pour nous de trouver l'hôte.

Eh bien, c'est ceci.

Je vais donc copier ce nom d'hôte, comme ça.

Mais ensuite je vais aussi devoir ajouter .oregon-postgres.render.com.

Assurez-vous donc d'ajouter cela, gardez le port à 5432.

Comme vous le voyez ici, le nom de la base de données est pager duty.

Alors mettons cela ici.

Et comme authentification, nous allons utiliser le nom d'utilisateur de la base de données, qui est ceci, et le mot de passe de la base de données.

Voici le mot de passe, veuillez utiliser le vôtre car celui-ci ne fonctionnera plus après ce tutoriel.

Voilà.

Je vais cliquer sur connect using SSL.

Et testons si cela fonctionne.

Et la connexion est un succès.

C'est parce que nous avons laissé l'adresse, l'adresse IP partout, d'accord.

Mais si vous vouliez, vous savez, la garder un peu privée, vous pourriez envisager d'ajouter ces adresses IP.

Super.

Créons une ressource.

Revenons aux ressources.

Et maintenant je vais juste fermer cela et rafraîchir ceci.

Afin qu'il charge les dernières ressources.

Et je vais choisir pager duty comme nom de ressource, c'est juste celle que j'ai faite.

D'accord, je vais donc utiliser cette UI pour ajouter les tables réelles que je vais utiliser pour ce projet.

D'accord, je vais donc créer ma première table.

Je vais utiliser la commande Create Table.

Et je vais créer une table d'incidents.

D'accord, ouvrez vos parenthèses et définissons ce qui va aller dans notre table.

Eh bien, je vais mettre un ID, qui va prendre une valeur entière (integer), je vais mettre un niveau d'urgence (urgency) qui va juste prendre un varchar 30.

Donc 30 caractères, essentiellement, je vais avoir "triggered" (déclenché). Est-ce un événement déclenché ? Eh bien, c'est oui ou non.

Je vais donc avoir un Booléen pour cela.

Ensuite, je vais aussi avoir "acknowledged" (reconnu), ce sera aussi un Booléen, ainsi que "resolved" (résolu), qui sera également un Booléen.

Ensuite, nous allons avoir une description de l'incident lui-même.

Cela va prendre un varchar.

Et je vais en fait limiter cela à 30.

D'accord, nous ne voulons pas qu'ils soient trop longs, et ensuite "assigned to" (assigné à), et cela va prendre un entier.

En fait, cela va prendre l'ID d'un employé.

Et je vais aussi avoir une date de création (created date), qui va prendre une date.

Voilà à quoi ressemble ma table, n'oubliez pas de terminer avec des points-virgules.

Vérifions si cela fonctionne, je vais cliquer sur Save and Run.

Et super, cela semble avoir fonctionné, nous n'avons pas d'erreurs.

Et nous allons appeler cela playground pour l'instant, car j'utilise essentiellement cela comme un petit mini terrain de jeu pour ajouter nos tables.

D'accord, c'était une chose que nous avons faite, vous pouvez garder cela ici, si vous le souhaitez.

En fait, je vais juste mettre cela en commentaire.

Parce que je vais créer une nouvelle table pour créer la table team, cela va prendre notre équipe.

Alors de quoi notre équipe va-t-elle être composée ? Eh bien, chaque membre de l'équipe va avoir un ID, qui, je dirais, doit être un entier, ils vont avoir un prénom (first name), que je vais prendre comme varchar de personnages, mettons 30.

Encore une fois, un nom de famille (last name), pour lequel je vais être super stricte aussi.

Bien sûr, vous n'êtes pas obligé d'en avoir 30, je choisis cela pour l'instant.

Et un e-mail, varchar mettons 225 points de large, d'accord, vous pouvez avoir des nombres de caractères plus élevés, si vous le souhaitez.

Ensuite, je vais avoir un numéro de téléphone de votre coéquipier, qui sera une valeur entière, et un Avatar, qui sera en fait une URL vers une image sur Internet.

Et ensuite nous allons avoir "on call" (d'astreinte) pour vérifier s'ils sont d'astreinte ou non.

Et cela va être une valeur booléenne, ainsi qu'un début de service (shift start).

Et cela va être une date, une valeur de fin de service (shift end), qui sera également une date, et les incidents sur lesquels ils travaillent, qui sera du texte, mais ce sera aussi un tableau de textes.

C'est comme ça que je l'écrirais.

Super.

Et terminez par quelques points-virgules.

Et cliquez sur save and run.

Voilà, nous venons d'ajouter notre table pour les membres de l'équipe.

Je vais donc mettre cela en commentaire.

Je vais aller de l'avant et ajouter deux incidents juste pour commencer afin que nous ayons des choses avec lesquelles jouer.

Je vais donc insérer dans la table appelée incidents.

Et nous allons insérer un ID et une valeur d'urgence, une valeur déclenchée, une valeur reconnue, une valeur résolue ou une description assignée à en s'assurant de l'orthographier exactement de la même manière que nous l'avons fait ici.

Date de création.

Et cela devrait être tout.

Ce sont donc les valeurs que nous voulons insérer, récupérons les valeurs réelles.

Pour la valeur de l'ID, je vais mettre l'incident ID numéro un, nous allons mettre l'urgence comme la chaîne de caractères "high" ainsi que le déclenché sera true.

La reconnaissance sera true et résolu sera false.

Nous avons donc mis des valeurs booléennes pour cela.

Et maintenant je vais juste mettre une description de cet incident, ce sera "DevOps escalation".

Juste comme ça, il sera assigné à l'employé avec l'ID 201.

Et ensuite nous allons juste mettre une date à laquelle cela a été créé, je vais mettre une date dans le passé, d'accord, parce que, vous savez, nous ne voulons pas tout mettre à la date d'aujourd'hui.

Voilà.

D'accord, et n'oubliez pas de terminer par un point-virgule.

D'accord, voici notre point-virgule, et cliquez sur save and run.

Super.

Et cela a été exécuté avec succès.

C'est donc un incident, ajoutons-en un autre.

Celui-ci va avoir la valeur de deux.

Mettons l'urgence comme "low".

Ajoutons true, peut-être false false, cette fois pour déclenché, reconnu et résolu.

Celui-ci peut être appelé "Security ops escalation" en s'assurant d'orthographier security correctement.

Il sera assigné à l'utilisateur 201 également.

Et mettons cela peut-être un jour plus tôt.

Je clique sur Save and Run.

Super.

Et je vais juste mettre cela en commentaire.

Je vais maintenant insérer dans team donc je ne vais insérer qu'une seule personne ici je pense que ce sera bien, nous devons obtenir l'ID, nous obtenons aussi le prénom de la personne que nous insérons, et le nom de famille en s'assurant que cela correspond exactement à ce que nous avons dans cette table.

Ensuite, c'est l'e-mail.

Ensuite, c'est le numéro de téléphone.

Ensuite, c'est l'Avatar.

Et je vais avoir "on call".

C'est le début du service (shift start).

Fin du service (shift end), et les incidents qui leur sont attachés.

Encore une fois, assurez-vous simplement que tout est bien orthographié, car ensuite nous allons mettre les valeurs.

Et la valeur de ceci, eh bien, ce sera le membre de l'équipe numéro 201, le nom sera Ania.

Et leur nom de famille sera Kubo.

Maintenant mon adresse e-mail, je vais juste la mettre comme la chaîne de caractères Ania @ freecodecamp.org.

Le numéro de téléphone, je vais juste mettre un faux numéro de téléphone pour l'instant.

Et comme avatar, eh bien, je vais juste utiliser mon avatar de freeCodeCamp.

S'il vous plaît, assurez-vous de prendre une image dont vous savez qu'elle ne risque pas d'être retirée d'Internet, ou alternativement stockez-les vous-même sur imager.com.

Ou vous pouvez les mettre sur une base de données externe telle qu'AWS, par exemple.

Je vais donc copier cette adresse d'image.

Et je vais juste la coller comme ça.

Maintenant, après l'avatar, je vais juste spécifier si cette personne est d'astreinte, je vais mettre true.

Et ensuite je vais aussi mettre une heure de début de service inventée, une heure de fin de service inventée sous forme de chaîne de caractères, puis un tableau.

Nous pouvons littéralement mettre le mot array comme ça.

Et ensuite je vais mettre "dev ops escalation" et "security ops escalation" comme incidents assignés à cet utilisateur.

D'accord, n'oubliez pas de terminer par des points-virgules, cliquez sur save and run, il est dit entier hors de portée (integer out of range), c'est bon, je vais juste changer le format du dossier.

Et maintenant je vais ajouter ce numéro de téléphone Twilio en m'assurant d'ajouter 001 devant et cliquez sur Run and safe.

Maintenant, il est dit entier hors de portée, ce qui est assez étrange, je ne pense pas que cela devrait être hors de portée.

Mais c'est bon, nous devrons peut-être en faire une chaîne de caractères à la place.

Alors allons-y et faisons-en une chaîne de caractères, je vais en fait juste mettre cela en commentaire, nous allons supprimer la table DROP TABLE team.

Essentiellement, nous allons la supprimer, car nous devons changer le type de données du numéro de téléphone.

Assurez-vous donc de supprimer cela.

Et maintenant je peux recréer une table.

C'est bien pour tous ceux qui ont peut-être fait une erreur au départ.

Et je vais juste changer cela en varchar également.

Cela ne prendra donc pas une chaîne de caractères.

Enregistrez cela et exécutez-le pour créer à nouveau cette table, le numéro étant un e-mail.

Et maintenant nous pouvons insérer dans Tim, après avoir mis cela en commentaire.

Enregistrez et exécutez.

Et super.

Nous avons maintenant ajouté notre premier membre d'équipe, je vais donc mettre cela en commentaire pour l'instant.

D'accord, c'était notre terrain de jeu.

Et maintenant je vais récupérer des données que nous pouvons injecter dans notre première table de tous les incidents.

Créons une nouvelle ressource.

Et assurons-nous que le résultat est pager duty.

Je vais juste faire select all from the table incidents.

Et cliquez sur Save and Run.

Voyons à quoi cela ressemble.

Et en effet, nous récupérons deux incidents.

Je vais renommer cela get incidents car c'est essentiellement ce que fait cette requête.

Et maintenant ici, au lieu d'ajouter des données manuellement, je peux faire get incidents et obtenir les données de ces incidents afin qu'elles s'injectent là et qu'elles soient automatiquement mappées sur ces jolies lignes de tableau.

Ce qui est cool, c'est que si vous voulez voir tout l'objet de données qui revient, vous pouvez, tout ce que vous avez à faire est d'aller dans l'état (state) et de récupérer les incidents et voici les données et vous verrez toutes ces informations comme les tableaux que nous pouvons utiliser.

D'accord, c'est juste dans cet onglet sur la gauche ici, je vais minimiser ce panneau de gauche maintenant.

C'est donc ce que j'ai fait.

Continuons à travailler là-dessus.

Une autre chose cool que nous pouvons faire est d'ajuster les colonnes que vous voulez voir ou modifier ou quoi que ce soit de ce genre.

Par exemple, je peux choisir de masquer la description si je veux.

Je vais donc sélectionner tout le tableau.

Et je vais choisir de masquer la description en appuyant sur ce petit œil ici, je vais aussi masquer le assigned to, je vais garder la date de création.

Et je peux même, si je veux, ajouter une nouvelle colonne, ajouter une colonne personnalisée.

Et cette colonne va m'aider à supprimer des incidents si je veux.

Pour le moment, je ne vais rien mettre ici à part décider que ce sera un bouton.

D'accord, c'est mon bouton.

Et la valeur de ceci va juste dire, delete.

Voilà, nous pouvons bien sûr réduire la taille des colonnes si nous le souhaitons, et de manière générale, jouer un peu mieux avec cela.

Je suis donc contente de ce tableau.

Changeons maintenant la valeur de ce zéro codé en dur.

Et je peux le faire facilement, je peux littéralement obtenir les données d'incidence.

Et je peux regarder à l'intérieur pour voir combien d'objets triggered sont à true, n'est-ce pas.

Pour cela, je vais utiliser la méthode filter.

Et je vais parcourir chaque élément, d'accord, en filtrant essentiellement chacun d'eux, et en utilisant i comme représentation de chaque élément que nous filtrons.

Et si i égale true, je vais obtenir la longueur de ce tableau.

Comme vous le verrez ici, deux incidents sont déclenchés.

Et si nous regardons ici, en effet, deux incidents sont déclenchés.

Si nous faisons la même chose pour acknowledge, nous devrions obtenir un incident reconnu.

Réessayons, nous utiliserons les deux accolades car c'est ainsi que nous faisons les choses dans Retool afin d'obtenir des valeurs à partir des requêtes.

La requête que nous avons écrite s'appelle Get incidents, n'est-ce pas.

Je récupère donc essentiellement le nom de tout ce que nous avons appelé cette requête et j'en extrais les données.

Et je vais cette fois filtrer par le acknowledged, donc je vais récupérer acknowledged et utiliser la méthode filter dessus pour filtrer essentiellement et si i ou chaque élément de ce tableau est égal à true, je vais obtenir la longueur totale du tableau.

Et en effet, nous obtenons un un.

Encore une fois, des accolades, afin d'accéder aux données des requêtes, la requête à laquelle je voulais accéder est la requête get incidents, vous pouvez voir toutes les informations qui reviennent ici.

Et encore une fois, si vous voulez vraiment voir tout l'objet, nous pouvons regarder ici.

J'ai donc incidents, je suis allée dans l'objet de données d'incidents, puis je suis allée dans le tableau acknowledged, et j'ai filtré tout ce qui est égal à true et j'ai obtenu la longueur de ce tableau.

Compris ? Cool.

D'accord, pour faire vos incidents ouverts, nous allons devoir faire autre chose, car nous allons devoir récupérer l'utilisateur.

D'accord, faisons peut-être cela ensuite.

Maintenant, qui était l'utilisateur ? Eh bien, je pense que l'utilisateur devrait être celui qui est d'astreinte, n'est-ce pas.

Allons-y et créons une nouvelle requête de ressource, je vais l'appeler get user.

Et je vais sélectionner tout de team cette fois.

Donc la table team où on call égale true, je vais enregistrer et exécuter ceci.

Voilà, cela revient avec un utilisateur et à tout moment, nous ne devrions vraiment avoir qu'une seule personne d'astreinte, n'est-ce pas.

C'est une sorte de règle qui devrait être faite dans le backend, ce n'est pas une chose de frontend.

Nous pouvons donc simplement supposer que cela reviendra avec un utilisateur à tout moment.

Ce sera donc un utilisateur.

Et je vais filtrer les incidents par l'utilisateur.

Essayons une autre ressource.

Je vais écrire filter incidents.

Et je vais sélectionner tout, de incidents.

où assigned to égale et ensuite je vais juste récupérer les données de l'utilisateur.

C'est donc notre requête get user.

Nous allons obtenir l'ID mais seulement obtenir le premier ID du tableau car nous supposons qu'il n'y en a qu'un seul, donc cela devrait être bon.

Et n'oubliez pas vos points-virgules à la fin, donc je vais juste enregistrer et exécuter cela.

En m'assurant d'orthographier incidents correctement là-bas.

Exécutez cela à nouveau.

D'accord, deux éléments reviennent.

C'est parce qu'en effet, deux éléments me sont assignés, Ania Kuba, car mon ID utilisateur est 201.

Super.

Une fois que nous aurons ajouté plus d'incidents ici, vous verrez comment cela change.

Cela signifie que je peux maintenant utiliser ma requête filter incidents pour les mettre à jour dynamiquement.

Encore une fois, utilisez nos accolades, filter incidents est la requête que je veux utiliser, je veux en extraire les données.

Et je veux obtenir le tableau triggered.

Et je veux le filtrer en fonction de si j'ai l'élément ici dans ce tableau égal à true, et je veux obtenir sa longueur.

D'accord, deux seront déclenchés, c'est correct, car je ne regarde que mes incidents ouverts.

Et pour le moment, je suis la seule utilisatrice ici.

Encore une fois, vous l'avez deviné, nous allons prendre les accolades, nous allons prendre les incidents filtrés.

Récupérons donc les données de filter incidents.

Et cette fois, nous allons récupérer le tableau acknowledged et le filtrer en bouclant sur i et si i égale true, nous allons obtenir la longueur de ce tableau à la fin.

Merveilleux.

Tout cela se présente bien.

Nous pouvons maintenant aussi remplir ceci car nous récupérons techniquement l'utilisateur.

Nous pouvons donc utiliser cette requête, exécutons-la à nouveau et voyons à quoi elle ressemble pour savoir qui est d'astreinte, n'est-ce pas ? Je peux donc utiliser mes accolades, pour aller dans la requête get user et obtenir les données et obtenir le prénom qui nous revient.

D'accord, je vais obtenir le prénom.

Et je pourrais aussi mettre le nom de famille, j'ai littéralement juste mis un espace là, cela fonctionnera, je vais récupérer les données de get user. Last Name, super.

Et pareil pour l'avatar, eh bien, je vais récupérer les données de get user, Avatar cette fois, et juste aller dans le premier élément de ce tableau.

Pareil pour l'e-mail.

Sur l'étiquette ici, je vais juste aller dans les données de get user pour l'e-mail et obtenir le premier élément du tableau.

En fait, peut-être devrions-nous avoir cela sur la légende réelle de l'étiquette.

Et ici, nous aurons juste le prénom à nouveau.

Je vais donc prendre tout cela et le coller sur l'étiquette ici.

Nous pouvons aussi essentiellement mapper ce que sont les tags.

Et ici nous allons obtenir les incidents, n'est-ce pas, alors débarrassons-nous de ces accolades, get user data incidents.

Et nous allons devoir aller dans le premier élément de ce tableau.

Et voilà.

Ces incidents ont maintenant été mappés ici.

Super.

Faisons de même pour ici.

Je vais juste montrer tous les incidents, je vais récupérer les incidents des données utilisateur.

Et en fait, si je traite cela comme un élément, nous pouvons simplement mettre le tableau ici comme ça.

D'accord, c'est quelque chose que j'ai fait.

Maintenant, à partir d'ici, je vais retourner dans l'utilisateur pour les données et obtenir le shift start.

Et encore une fois, ici, je vais obtenir les données utilisateur, cette fois shift end, super.

Nous avons donc rempli tout cela à partir de la requête get user.

C'est pas cool ? L'étape suivante consistait à travailler sur l'ajout d'un incident.

Pour cela, je vais en fait créer une modale qui va apparaître.

En fait, allons-y et mettons cela ici.

Et je vais supprimer ce bouton.

Supprimez-le, et je vais changer le texte de ceci pour qu'il soit add incident.

Réduisons cela pour le moment.
Ainsi que l'état.

L'arrière-plan de l'accent sera vert.

Nous allons juste le rendre un peu plus grand.

D'accord, c'est notre modale.

Et ici je vais juste mettre quelques tags.

Je vais faire glisser du texte, et cela va dire add incident.

Je vais en faire un élément h2, add incident.

Juste comme ça.

Mettons aussi un séparateur, je vais le mettre juste ici.

Et ensuite je vais créer une entrée numérique (number input).

Une spécifiquement pour mettre des chiffres.

Juste comme ça avec une étiquette "incident ID".

Super.

Ensuite, je vais créer une liste déroulante (drop down).

Je vais avoir cette sélection déroulante, juste comme ça.

Et je vais mettre la valeur de l'étiquette comme urgency.

Et je vais coder mes options en dur, l'option 1 sera high, l'option 2 sera medium.

Et l'option 3 sera bien sûr low.

Ce sont mes options.

Et si vous laissez l'étiquette vide, elle prendra simplement la valeur par défaut.

Et cela me convient.

Ensuite, je vais juste créer quelques interrupteurs (switches).

C'est parce que je vais traiter des valeurs booléennes, donc cela me va, je vais en avoir un pour triggered.

Ayons-en un aussi pour acknowledged.

Et enfin, ayons-en un pour resolved.

D'accord, ce sont mes trois options juste là.

Vous pouvez bien sûr les styliser autant que vous le souhaitez.

Ensuite, nous allons avoir une entrée de description.

Pour cela, je pense que nous devrions juste avoir du texte.

Je vais donc mettre une entrée de texte.

C'est pourquoi j'ai gardé la description courte, max 30 caractères, car vous savez, ce n'est pas beaucoup pour travailler.

Et nous pouvons aussi limiter cela.

Nous pouvons limiter la valeur.

Vous pouvez avoir une longueur maximale de 30, juste comme ça.

Et allons-y et mettons description ici.

Et enfin, ayons une autre liste déroulante de sélection.

Sélectionner.

Et ici, nous allons sélectionner à qui cela est assigné.

Je vais mettre assigned to.

Et au lieu d'avoir des options, je vais mapper les options, cette fois, la source de données pour cela, eh bien, nous allons devoir récupérer tous les membres de l'équipe, n'est-ce pas, alors allons-y et écrivons une nouvelle requête, je vais l'appeler get team et nous allons récupérer tous les membres de l'équipe.

Et la requête pour cela est select all from Team et exécutez-la.

Ce sera donc la source de données, get team.

Et cela va s'auto-remplir pour vous.

Et super, c'est fantastique, c'est exactement ce que je veux.

D'accord, nous pouvons maintenant choisir quel membre de l'équipe sélectionner d'une manière si agréable.

D'accord, et quel que soit celui que nous sélectionnons, il va en fait choisir l'ID de cet élément.

Si je me sélectionne, la valeur de ceci, quand il est sélectionné, sera 201.

Donc lisible, puis pratique.

Super.

Et enfin, je vais juste mettre un bouton, qui va soumettre cette modale.

Je vais donc juste mettre Submit, et nous pouvons réellement rendre la hauteur de cette modale dynamique en fonction de ce qu'il y a à l'intérieur.

Je peux faire "hug content", et cela se produira.

D'accord, merveilleux.

Maintenant, écrivons une requête pour ajouter un incident.

Donc add incident, juste comme ça en s'assurant que la ressource est pager duty.

Et encore une fois, nous allons essentiellement utiliser ce morceau de code.

Je vais donc copier tout cela, car c'est le code dont nous aurons besoin pour ajouter un nouvel incident, bien sûr quand il sera décommenté.

C'est ce que nous allons insérer dans la table incidents.

Cependant, cette fois, les valeurs ne seront pas codées en dur.

Elles seront en fait tirées d'ici.

Je vais donc utiliser mes accolades pour accéder à ce composant qui s'appelle number input 1 et obtenir sa valeur.

Si vous passez la souris dessus, vous verrez ce zéro, eh bien si je change cela, cela changera et vous verrez que la valeur est maintenant deux.

D'accord, c'est littéralement récupérer la valeur de cette entrée, cette deuxième est l'urgence, n'est-ce pas.

Et ce composant s'appelle select 1.

Je vais donc prendre select 1 et obtenir sa valeur une fois de plus.

Si je choisis high, ce sera maintenant high.

Merveilleux.

J'espère que cela commence à avoir du sens.

Ensuite, nous allons passer à ces interrupteurs.

Ce sera donc switch 1, 2 et 3.

Encore une fois, je vais juste utiliser mes accolades pour obtenir la valeur de switch 1, la valeur de switch 2, tant que ceux-ci sont bien sûr dans le bon ordre.

Et ensuite la valeur de switch 3.

Et enfin, je vais juste minimiser cela, nous devons obtenir la description qui est text input 1, et la valeur de select 2.

La description va donc aller ici.

Et c'est text input value 1, je crois, oui, text input 1 et select 2.

Donc la valeur de select 2, et nous allons juste obtenir la date d'aujourd'hui.

Je vais donc utiliser le nouvel objet date de JavaScript pour faire cela, encore une fois, assurez-vous qu'il est entre accolades, et appelez-le simplement.

C'est ce que j'ai fait, je récupère essentiellement les valeurs de toutes ces entrées, essayons de remplir cela.

Allons-y, incident numéro trois, urgence high, déclenché, reconnu, non résolu, description, eh bien, je peux mettre tout ce que je veux, mettons deployment.

Et assigné à, eh bien je suis la seule ici pour le moment.

Super.

Et maintenant ce bouton, eh bien, nous devons déclencher la requête add incident que nous venons d'écrire.

Je vais donc ajouter un écouteur d'événement pour contrôler la requête qui a été générée pour moi add incidents car je suis actuellement sur cette requête.

Et nous allons déclencher cela.

D'accord, cela me semble super.

Maintenant, avant de soumettre cela, je vais exécuter cette requête avec toutes ces valeurs remplies, vous verrez les valeurs que nous allons essentiellement mettre, elles ont toutes été remplies maintenant.

Et si cela fonctionne, eh bien en cas de succès (on success), je veux en fait faire quelques choses, n'est-ce pas, je veux récupérer tous les incidents à nouveau.

Donc les incidents les plus récents, et je veux aussi que la modale se ferme.

Je vais donc contrôler un composant cette fois.

Et ce composant est la modale.

Allons-y et trouvons-la.

Et je veux qu'elle se ferme, nous pouvons aussi ajouter d'autres choses amusantes comme des confettis si nous voulons.

Confettis, allons-y et faisons cela.

Et enregistrez.

Je n'ai pas exécuté cela car je veux le déclencher en appuyant sur ce bouton.

Je vais donc cliquer ici, nous avons eu une erreur, déboguons.

Il semblerait que j'aie juste mis une chaîne de caractères supplémentaire, je n'ai pas supprimé ces chaînes correctement.

Alors maintenant enregistrons.

Réessayons.

Et cliquez sur Submit.

Et super, cela a fonctionné.

Et tada, nous avons récupéré les nouveaux incidents.

Et cela a mis à jour notre tableau.

C'est donc génial.

Et vous verrez que cela a été mis à jour pour oh, cela n'a pas été mis à jour.

C'est parce que nous devons bien sûr aussi exécuter la méthode filter incidents également.

Donc en cas de succès de l'ajout d'un incident, ajoutons aussi get filtered incidents.

D'accord, voilà.

Maintenant je viens de l'exécuter à nouveau.

Nous aurions donc ajouté les mêmes choses à nouveau, car comme vous le verrez, ces informations sont toujours là.

Travaillons maintenant sur la suppression de ce troisième, d'accord, parce que nous n'en voulons pas, mais au moins nous savons que cela fonctionne.

Et cela fonctionne et tout se met à jour.

Travaillons maintenant sur la suppression d'un incident.

Celui-ci, je vais l'appeler delete incident.

La ressource sera pager duty, et tout ce que je vais faire est delete from incidents where ID equals et ensuite c'est table 1 selected row data id.

Cela va poser un problème.

C'est parce que, vous savez, si nous supprimons essentiellement celui-ci, il va regarder l'ID et il va supprimer les deux.

Gardez donc à l'esprit que chaque fois que vous ajoutez un incident, cet ID doit être unique.

Enregistrez cela et en cas de succès de ceci, eh bien encore une fois, je vais essentiellement récupérer tous les incidents et exécuter la requête filter incidents une fois de plus.

Alors enregistrons cela.

Et maintenant connectons ce bouton à cela.

Trouvons ce bouton personnalisé que nous avons fait et au clic, nous allons exécuter une requête, et cette requête est delete incident.

D'accord, c'est ce que nous voulons qu'il se passe.

Maintenant, essayons.

Je vais cliquer sur delete incident.

Et cela devrait supprimer et cela a supprimé tous ces incidents, et cela a récupéré tous les incidents à nouveau, afin que nous puissions les voir dans le tableau.

Et cela a mis à jour ceux-ci en fonction de la requête filter incident et de la requête get incident.

Merveilleux.

Je suis vraiment contente de cela.

Continuons.

D'accord, il est temps de passer à la page des membres de l'équipe.

Ici, allons-y et utilisons la requête get team afin de remplir ce tableau.

Encore une fois, j'utiliserai mes accolades, pour récupérer la requête get team et les données qui en proviennent.

Et cela devrait automatiquement mettre à jour mon tableau juste ici.

Encore une fois, nous pouvons choisir quelles colonnes masquer, je vais donc masquer la colonne avatar, cette fois, je vais masquer le numéro de téléphone, je vais aussi masquer le début du service et la fin du service ainsi que les incidents, d'accord, et je vais ajouter une colonne personnalisée une fois de plus, pour pouvoir supprimer cet utilisateur.

Ce sera donc un bouton.

Allons-y et faisons cela.

Voilà, il y a un bouton qui dit delete après avoir mis à jour la valeur.

Super.

Avant de supprimer quoi que ce soit, remplissons ce conteneur avec l'utilisateur sélectionné, et ajoutons la fonctionnalité pour ajouter un nouveau membre d'équipe.

Pour ce faire, je vais en fait renommer ce composant, comme je l'ai mentionné, c'est quelque chose que vous pouvez faire.

Je vais donc l'appeler team table.

D'accord.

Et cela le rend plus raisonnable lorsque j'utilise ce tableau.

Donc la team table, je peux littéralement utiliser mes accolades pour accéder au composant team table et obtenir les données de la ligne sélectionnée.

Et je pourrais juste saisir le prénom, si je le souhaite, de cette ligne sélectionnée.

Et bien sûr, je pourrais le faire pour le nom de famille aussi.

Encore une fois, ce seront des accolades.

Et je vais juste utiliser team table selected row data Last Name, cette fois.

Et merveilleux.

Super, nous pouvons aussi utiliser l'avatar que j'ai caché du tableau, mais il existe toujours.

Si je veux juste aller chercher une image, juste comme ça.

Et maintenant je peux aller dans la team table sur les données de sélection et obtenir l'avatar car il existe.

Ici, même si c'est une colonne supprimée.

Encore une fois, si vous voulez jeter un coup d'œil aux objets pour cela, regardez simplement ici, regardez get team data.

Et nous récupérons les données de la ligne sélectionnée, l'avatar.

Et c'est l'URL que je récupère.

Super.

Et maintenant remplissons ces autres composants.

Ici encore une fois, je supprimerais tout cela et j'utiliserais les données de la ligne sélectionnée de team table pour obtenir le tableau d'incidents qui sera mappé sur ces tags.

Et vous savez quoi faire, cela devrait être facile.

Maintenant, retournons dans les données de la ligne sélectionnée de team table et récupérons l'heure de début du service.

Et ensuite récupérons aussi l'heure de fin du service.

Donc team table, select data, shift end est ce que je veux.

Et ici je vais juste afficher l'adresse e-mail.

Donc encore une fois, Team table selected row data dot email.

Merveilleux.

Et c'était très indolore.

Maintenant, passons à l'ajout d'un nouveau membre d'équipe.

Pour cela, je vais en fait utiliser les composants de modale.

Je vais juste mettre cela ici pour l'instant et supprimer ce bouton.

Je vais donc supprimer cela et déplacer ceci.

Déplacez le bouton de la modale juste ici.

Je vais le rendre un peu plus grand.

Et bien sûr, nous pouvons le styliser.

Je vais tout mettre en vert.

Et ensuite changeons la police de ceci pour que ce soit "add new team member".

Super.

Alors maintenant travaillons sur la modale.

Pour cela, je vais juste faire glisser du texte, faisons-en un élément h3.

Et cela va dire "add a new team member".

Juste comme ça.

Et je vais l'étirer, je vais aussi avoir un autre séparateur comme nous l'avons fait précédemment.

Je peux mettre ce séparateur juste ici.

Et ensuite ajoutons quelques entrées.

Je vais mettre une entrée numérique.

Et cela va dire, Team Member ID.

Changeons le texte de l'étiquette pour dire, Team Member ID.

Ayons aussi juste une entrée de texte, ce sera pour le prénom.

Et nous allons aussi en avoir une pour le nom de famille, aussi.

Changeons cela pour dire, first name.

Et je vais littéralement copier et coller.

Pour que la deuxième apparaisse.

Je peux donc changer cela en last name, nous allons aussi avoir l'e-mail.

Il y a une entrée d'e-mail spéciale que nous pouvons utiliser.

Voilà, je vais juste la faire glisser comme ça et la mettre ici.

Peut-être mettons deux points là, juste pour que cela ressemble à la même chose.

Et ensuite nous allons avoir un numéro de téléphone.

Eh bien, c'est en fait une entrée de texte comme nous le savons, car nous avons changé cela pour être une entrée de texte.

Je vais donc mettre phone number comme ça.

Et c'est aussi une image d'avatar.

Eh bien, ce sera juste une URL vers quelque chose sur Internet, comme nous l'avons mentionné, pour l'instant, bien sûr, vous n'êtes pas obligé de l'avoir comme ça, vous pouvez lier cela à une base de données AWS si vous souhaitez stocker des images.

Ensuite, nous devons avoir une case à cocher (checkbox) pour nous permettre de vérifier si quelqu'un est d'astreinte ou non.

D'accord, alors mettons on call ici, et ensuite quelqu'un peut choisir de sélectionner cela ou non, ce sera à lui de décider.

Nous avons aussi un sélecteur de date (date picker).

Je vais donc juste mettre ce sélecteur de date juste ici.

Et par défaut, cela vous montrera la date d'aujourd'hui, que vous pouvez ensuite changer.

Et je vais changer cette étiquette en start dates.

Et créons une date de fin, un, deux, donc date de fin de chaque service.

Et enfin, nous allons aussi avoir une sélection multiple (multiple select), d'accord, car nous pouvons choisir plusieurs opérations assignées à un utilisateur.

Je vais juste changer cela en operations.

Et codons les options en dur, la première sera email ops escalation, juste comme ça.

La deuxième sera security ops escalation.

Et la troisième sera DevOps escalation.

Je vais juste mettre dev ops escalation juste comme ça.

D'accord, donc maintenant les gens peuvent en sélectionner plusieurs, ce qui est plutôt cool.

Et puis enfin, ayons un bouton de soumission.

Je vais donc me débarrasser de cela et trouver un bouton pour que les gens puissent soumettre ces réponses.

Voilà.

Et changeons cela pour dire, Submit.

Merveilleux, je pense que cela se présente bien.

Maintenant, passons à l'écriture d'une requête pour cela.

Ce sera add team member.

Changeons cela pour dire add team member, assurez-vous simplement que c'est la bonne ressource.

Et ensuite nous allons aussi insérer dans donc c'est là que notre terrain de jeu devient utile, nous allons insérer dans team, je vais tout saisir de team member, le coller, décommenter cela et juste changer les valeurs.

La valeur de ceci sera celle de number input 2.

Saisissons donc la valeur de number input 2.

Ce sera la valeur de text input 2, alors débarrassez-vous de cette entrée, la valeur de text input 2, et ensuite nous avons la valeur de text input 3.

Donc la valeur de text input 3, nous aurons aussi email 1, donc débarrassez-vous de cette chaîne, la valeur de input email 1.

Nous avons ensuite le numéro de téléphone, qui est text input 4.

Allons-y et mettons la valeur de text input 4.

Ensuite nous avons l'avatar, n'est-ce pas, qui sera la valeur de text input 5.

Débarrassons-nous de cette valeur de text input 5.

Et ensuite nous avons une case à cocher.

La case à cocher est checkbox 1 et ensuite nous mettons à jour 1 pour ajouter la valeur de multi select 1, c'est vraiment facile à retenir, la valeur de checkbox 1, ce sera date 1.

Donc la valeur de date 1, ce sera la valeur de date 2.

Et ce sera les options de multi select ou la valeur de multi select 1.

Super.

Maintenant enregistrons cela, je vais en fait aussi ajouter des choses à faire en cas de succès car en cas de succès, nous voulons, essentiellement nous récupérons l'équipe, n'est-ce pas, donc cela se produira en cas de succès.

Et ensuite ayons aussi des confettis, parce que pourquoi pas, fermons aussi la modale.

Nous allons donc cette fois contrôler un composant et trouver la deuxième modale que nous avons faite.

Faites défiler vers le bas pour modal 2, et ensuite nous voulons la fermer.

D'accord.

C'est ce que nous voulons faire en cas de succès.

Maintenant je vais enregistrer cela et connecter le bouton Submit pour exécuter cette requête.

Ajoutons simplement un gestionnaire d'événements, contrôlons la requête add team member.

Merveilleux, essayons.

Je vais mettre employé 2 2 je vais mettre Beau Carnes et comme e-mail, je vais juste mettre beau @ freecodecamp.org.

Et comme numéro de téléphone, je vais juste en inventer un.

D'accord, juste comme ça.

Et comme image d'avatar, je vais juste en prendre une sur Internet.

D'accord, je vais copier l'adresse de l'image.

Et juste coller cela, il ne sera pas d'astreinte.

Et mettons sa date de début au 11.

Et la date de fin au 14.

Et les opérations auxquelles il va être assigné ?

Eh bien, voyons voir.

Je pense qu'il y a juste email ops, et security DevOps aussi.

Maintenant cliquons sur Submit.

Et super, Beau a été ajouté.

C'est merveilleux.

Et enfin, ajoutons un moyen de supprimer réellement un membre de l'équipe.

Je vais en fait écrire une nouvelle requête.

Ajoutons une nouvelle requête de ressource, ce sera delete team member.

Assurez-vous que la ressource est correcte.

Et nous allons delete from team where the ID equals the team table selected row data ID, n'est-ce pas, parce que nous sommes ici, si nous sélectionnons celui-ci, et que nous voulons le supprimer, nous voulons juste nous assurer que c'est le bon ID.

Et c'est ainsi que nous allons supprimer ce membre de l'équipe.

En cas de succès, nous allons bien sûr devoir réexécuter la requête pour obtenir tous les membres de l'équipe.

Donc get team et enregistrez.

Et maintenant nous devons juste connecter ce bouton.

Trouvons ce bouton.

Et au clic, nous voulons exécuter une requête.

Et cette requête est de supprimer un membre de l'équipe.

D'accord, voilà.

Et si on essayait ?

Allons-y.

Je vais supprimer ce membre de l'équipe.

Et merveilleux, voilà.

Et je vais juste le rajouter.

Heureusement, tout cela est encore là, car je n'ai pas effacé cela.

Je l'ai fait exprès, juste pour que ce soit facile pour nous pour ce tutoriel, je vais juste cliquer sur Submit.

Voilà Beau à nouveau.

Maintenant pour le compositeur d'e-mail, eh bien, ce serait assez agréable d'avoir le prénom de celui que je mets en évidence qui s'affiche.

C'est donc ce que je vais faire.

Je vais une fois de plus utiliser les données de sélection de team table pour obtenir le prénom de cette personne.

D'accord, voilà.

Il est dit Salut, Bo.

C'est donc la valeur par défaut de tout notre éditeur de texte enrichi et mettez une virgule là aussi.

Et ici aussi, nous pouvons montrer à qui nous envoyons cela.

Je peux donc utiliser team table selected row data email cette fois.

Super.

Pour le moment, il affiche Bo, si je me sélectionne, bien sûr, cela se met à jour, mais cela se met à jour aussi et ensuite je peux écrire un e-mail et l'envoyer mais bien sûr pour cela nous devons connecter cela.

Ce que je vais faire aussi, c'est que chaque fois que nous envoyons un e-mail, je vais aussi envoyer une notification par SMS.

C'est donc deux ressources que nous devons ajouter.

Allons-y.

Je vais aller dans Resources.

Et connectons notre Twilio auquel nous nous sommes inscrits auparavant.

S'il vous plaît, allez trouver Twilio ici.

C'est Twilio.

Et je vais faire Twilio.

Récupérons le compte sID.

Voici mon sID de compte.

Récupérons le jeton d'authentification (auth token).

Voici mon jeton d'authentification, je vais le supprimer.

Alors ne pensez pas qu'il fonctionnera encore si vous l'utilisez.

Je vais juste sélectionner ceci car il ne me permet pas de mettre à jour les adresses IP.

Et testons la connexion.

Cette connexion est réussie.

Et créons une ressource.

Merveilleux.

C'est maintenant fait, je vais enregistrer ces changements.

Et revenons aux ressources.

Et cette fois, je vais créer une autre ressource.

Cette fois, ce sera pour l'envoi d'e-mails, je vais juste faire défiler vers le bas jusqu'à une précédente que j'ai faite et la reconfigurer.

Voici les paramètres dont vous avez besoin.

Cependant, vous devez avoir un Google Workspace, qui est un espace de travail payant pour que cela fonctionne maintenant.

Mes identifiants Google Workspace sont Ania @ codewithania.com.

Et ensuite je vais juste mettre mon mot de passe pour cet e-mail.

D'accord, c'est ce que vous devez faire, testons la connexion.

Et ensuite nous allons juste devoir autoriser les applications moins sécurisées.

Allez simplement dans votre console d'administration.

Et je vais juste chercher un moyen de contrôler l'accès aux applications moins sécurisées.

D'accord, c'est ici, nous allons dans les paramètres.

Et ensuite nous allons dans l'accès et le contrôle des données et les applications moins sécurisées.

Et je vais autoriser les utilisateurs à gérer les applications moins sécurisées.

Super.

C'est pour tous les utilisateurs de mon entreprise.

Et cette connexion est un succès.

Voilà, nous l'avons fait.

Super.

Maintenant retournons à notre application, je vais me débarrasser de cela.

Maintenant connectons cela, je vais juste créer une nouvelle requête.

Créons une nouvelle requête de ressource, ce sera pour envoyer un e-mail.

Et cette fois la ressource, eh bien, ce sera Gmail.

Et l'e-mail de l'expéditeur (from email) sera juste de Ania @ codewithania.com.

Et l'e-mail du destinataire (to email) sera essentiellement celui que nous sélectionnons, n'est-ce pas, la ligne sélectionnée.

Allons donc dans les données de la ligne sélectionnée de team table, e-mail, où vous pouvez avoir un CCI ou un CC, je ne vais pas en mettre.

Et cela va juste dire "e-mail du clone de PagerDuty".

Et le corps.

Eh bien, ce sera juste le corps de notre éditeur de texte enrichi.

Nous allons donc aller dans rich text editor 1 et obtenir la valeur.

D'accord, super.

Et en cas de succès.

Ayons aussi juste quelques confettis, et enregistrons cela.

Et maintenant connectons-le au bouton du formulaire.

Gestionnaire d'événements au clic, nous allons contrôler la requête sent email, car c'est la requête sur laquelle nous sommes maintenant.

Il l'a donc détectée.

Une autre chose que je veux faire est d'envoyer un message texte indiquant que nous avons reçu un e-mail.

Il y aura donc une autre requête de ressource send text.

Et cette fois, ce sera la ressource Twilio que nous venons de créer.

Et utilisez Twilio.

D'accord, cela a été pré-configuré pour moi.

Et c'est l'opération que nous devons faire.

C'est une requête POST, c'est le point de terminaison et il a rempli mon compte Sid, c'est bien aussi.

Eh bien, à qui nous allons envoyer cela.

Je vais mettre mon propre numéro de téléphone dans un instant pour tester cela.

Mais bien sûr, normalement vous iriez dans les données de la ligne sélectionnée de team table et récupéreriez le numéro de téléphone, n'est-ce pas.

Juste comme ça, alors allons-y et sélectionnons quelqu'un.

Je suis sélectionnée donc cela devrait faire apparaître mon numéro de téléphone.

Le corps, je vais juste mettre "vous avez une notification par e-mail du clone de PagerDuty", et de, eh bien de sera mon numéro de téléphone Twilio qui est en fait ceci, vous pouvez l'obtenir de Twilio également.

Si vous n'avez pas de "from" ici, n'hésitez pas à ajouter un paramètre en cliquant ici.

D'accord, super.

C'est ce que nous voulons faire et ajoutons juste quelques confettis pour quand cela s'enregistre.

Et je vais attacher cela à ce bouton aussi.

Donc déclencheur d'envoi de texte.

D'accord, donc ces deux choses vont se produire.

Maintenant, parce que bien sûr, ce numéro n'existe pas vraiment, je vais mettre mon numéro de téléphone.

Alors s'il vous plaît, ne regardez pas.

Et enregistrons cela et testons.

Et super.

Cela a fonctionné, j'aurais dû recevoir un SMS.

Alors vérifions.

Tout d'abord, je vais juste exécuter ceci et voir si cela a fonctionné.

Et déboguons.

D'accord, juste pour vous assurer que vous avez votre e-mail le même que celui que vous utilisez dans l'application.

Et cela devrait fonctionner.

Vérifions le compte Gmail.

Je vais juste me connecter et vérifier si j'ai reçu un e-mail.

Et c'est le cas.

D'accord, voici mon e-mail.

Bien sûr, il arrive en HTML.

Nous allons donc probablement devoir formater cela un peu mieux.

Mais au moins, il envoie quelque chose.

Voilà.

Nous avons terminé notre application PagerDuty.

La voici dans toute sa splendeur.

Elle fonctionne.

L'API Twilio fonctionne.

L'API SMTP fonctionne.

Nous utilisons une base de données Postgres, nous pouvons ajouter des incidents, des membres d'équipe, supprimer des membres d'équipe, supprimer des incidents.

C'est magnifique.

J'espère que ce tutoriel a été utile.

Et j'espère que vous vous êtes amusés en apprenant et je vous dis à bientôt.