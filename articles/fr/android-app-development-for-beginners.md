---
title: Développement d'applications Android pour débutants
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-10-26T12:01:00.000Z'
originalURL: https://freecodecamp.org/news/android-app-development-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/firstandroid2.png
tags:
- name: Android
  slug: android
- name: youtube
  slug: youtube
seo_title: Développement d'applications Android pour débutants
seo_desc: 'Seventy-five percent of all phones are Android phones and seventy-five
  percent of all Internet users only access the Internet using their phone. So there
  is a big market for Android apps.

  We just published crash course on Android app development on t...'
---

Soixante-quinze pour cent de tous les téléphones sont des téléphones Android et soixante-quinze pour cent de tous les utilisateurs d'Internet n'accèdent à Internet qu'en utilisant leur téléphone. Il existe donc un grand marché pour les applications Android.

Nous venons de publier un cours accéléré sur le développement d'applications Android sur la chaîne YouTube freeCodeCamp.org. Ce cours est parfait si vous êtes tout nouveau dans le développement d'applications Android.

Rahul Pandey a développé ce cours. Rahul est un responsable Android chez Facebook et un conférencier à l'Université de Stanford.

Dans ce cours, vous apprendrez le développement Android en créant une calculatrice de pourboire. Ce cours ne suppose aucune expérience préalable avec Android, et à la fin, vous aurez une application que vous pourriez publier.

Vous apprendrez à créer l'interface utilisateur avec XML, et à coder la logique en utilisant le langage de programmation Kotlin. Ce sont les blocs de construction fondamentaux de toute application Android moderne.

Vous apprendrez également à utiliser le ConstraintLayout pour la disposition et deux écouteurs d'événements pour la logique de l'application. Après avoir saisi un montant de base et un pourcentage de pourboire, l'application calculera le pourboire et le total pour vous. Vous implémenterez également une animation de pourcentage de pourboire et un pied de page pour rendre notre application plus unique.

Regardez le cours ci-dessous ou [sur la chaîne YouTube freeCodeCamp.org](https://youtu.be/FjrKMcnKahY) (1 heure de visionnage).

%[https://youtu.be/FjrKMcnKahY]

## Transcription

(autogénérée)

Dans ce cours pour débutants, vous apprendrez à créer une application Android avec Rahul Pandey.

Rahul est un ingénieur Android chez Facebook et un conférencier à l'Université de Stanford. Nous allons créer une application Android à partir de zéro, nous commencerons avec un projet vide et finirons avec quelque chose que vous pouvez réellement utiliser, et même publier sur le Play Store. Nous allons créer une calculatrice de pourboire, où vous pouvez entrer un montant de base, un pourcentage de pourboire, et l'application calculera le pourboire et le montant total pour vous.

Nous allons créer cette application en utilisant le langage de programmation Kotlin.

Je vais donc supposer que vous avez quelques bases en programmation.

Mais si vous êtes nouveau dans Kotlin, je laisserai un lien dans la description vers une rapide introduction de 12 minutes sur le langage que j'ai faite.

Je suis Rahho, j'enseigne Android sur YouTube et hors YouTube depuis un moment maintenant.

Alors, quand vous êtes prêt, commençons et créons cette application ensemble.

Il y a trois choses que je veux aborder dans cette vidéo.

Premièrement, je veux passer en revue les principales fonctionnalités de l'application de calculatrice de pourboire.

Deuxièmement, je vais expliquer les concepts principaux d'Android que nous allons couvrir en la construisant.

Et troisièmement, parce que je garde l'application délibérément très simple, je veux également souligner certains des concepts Android que nous ne rencontrerons pas en la construisant.

Et ceux-ci seront couverts dans des applications Android plus sophistiquées ou compliquées plus tard.

J'ai mentionné plus tôt comment vous pourriez aller de l'avant et publier cette application sur le Google Play Store dès que vous avez terminé le tutoriel.

Et c'est exactement ce que j'ai fait.

Donc, si vous voulez essayer ce que nous allons construire, n'hésitez pas à vérifier le lien dans la description et à le télécharger sur l'un de vos appareils Android.

Faisons donc une démonstration de l'application pour que nous puissions avoir une idée des principales fonctionnalités que nous allons construire.

Dans cet exemple, je suis sorti pour un dîner solo très somptueux, et j'ai dépensé 83,15 $.

Et je laisse un pourboire assez généreux de 24 % et l'application calcule automatiquement le pourboire et le montant total.

Pour simplifier un peu les calculs, pourquoi ne pas mettre à jour le montant de base à 100 $.

Et ce que vous pouvez voir, c'est que le clavier qui apparaît ne nous permet de saisir que des nombres et des décimales, ce qui est logique car nous traitons avec des devises ici.

Et si je suis vraiment satisfait du service que j'ai reçu lors du repas, je pourrais augmenter le pourcentage de pourboire et le porter au maximum de 30 %.

Et deux choses se produisent ici.

La première est que nous mettons à jour dynamiquement les calculs du pourboire et du montant total à 30.

Et la somme est de 130.

Mais aussi, nous mettons à jour la description de ce pourcentage de pourboire.

Donc, il est passé de génial à incroyable et est également devenu cette couleur verte plus vive.

D'un autre côté, si j'étais vraiment mécontent du service, je pourrais ne pas laisser de pourboire.

Et nous considérons cela comme un mauvais pourboire.

Et vous pouvez voir comment la couleur a été mise à jour en cette couleur rouge.

Et puis en bas ici dans le pied de page, nous avons également un moyen de personnaliser l'application pour que vous puissiez dire qui l'a faite ou d'où vous venez.

Les concepts que nous couvrons dans la calculatrice de pourboire sont les mêmes concepts qui sont fondamentaux pour chaque application Android.

Le premier est la création de l'interface utilisateur.

Chaque application a besoin d'une interface utilisateur.

Et le composant principal que nous allons utiliser ici est un ConstraintLayout, qui contiendra les autres widgets, par exemple, le TextView, ou le SeekBar, pour entrer le pourcentage de pourboire.

Deuxièmement, chaque application Android intéressante va écouter et réagir à l'entrée de l'utilisateur.

Nous avons donc deux façons de saisir des données dans notre application : l'une est de saisir le montant de base.

Et la seconde est le pourcentage de pourboire.

Et en fonction de cela, nous devons réagir et mettre à jour l'interface utilisateur de manière appropriée.

Et troisièmement, nous avons à peine effleuré la surface du style et de l'animation sur Android. Je vais vous montrer comment mettre à jour certaines des couleurs et aussi vous montrer comment faire une animation avec la description du pourboire et changer sa couleur dynamiquement.

Il y a aussi beaucoup de choses que nous ne allons pas couvrir dans la calculatrice de pourboire.

Et c'est important afin de réduire la portée et de rendre cette application vraiment rapide et simple à construire.

Si vous êtes nouveau dans Android, premièrement, nous n'allons pas avoir plusieurs écrans.

Ce qui signifie que nous n'avons pas à traiter avec des choses comme la navigation ou la pile de retour dans Android.

Et en fait, le seul écran que nous avons est en réalité assez simple, car nous n'avons pas de données de liste que nous devons gérer.

Deuxièmement, nous n'avons rien à faire avec le réseau et Internet.

Dès que vous commencez à parler à une API ou à un serveur, les choses deviennent beaucoup plus compliquées car vous devez gérer la programmation asynchrone et la gestion de ces données.

Et troisièmement, nous ne traitons pas du tout avec le stockage, tout sera local et en mémoire.

Nous n'allons donc pas écrire dans une base de données ou sur le disque ou dans le cloud.

Et ces trois choses rendent l'application beaucoup plus simple à construire.

Donc, je suis sûr que lorsque vous construisez cela et que vous entrez dans un restaurant, vous allez être super populaire car vous pourrez calculer le pourboire facilement et littéralement votre nom sera sur l'application.

Donc, je vous verrai dans la prochaine vidéo.

Dans cette vidéo, nous allons commencer avec le tout nouveau projet Android Studio et disposer les vues pour notre calculatrice de pourboire. En particulier, nous allons disposer huit vues où les quatre vues de texte de gauche décriront le contenu de ce qui est affiché à droite.

La première chose que nous allons faire est de créer un tout nouveau projet Android Studio.

Donc, j'ai Android Studio qui tourne ici, et je fais tourner Arctic Fox, mais n'importe quelle version récente devrait faire l'affaire, tapez sur nouveau projet.

Et je vais choisir le modèle d'activité vide.

Ces autres modèles sont parfois utiles, mais ils apportent beaucoup de code inutile dans notre application, ce qui peut être confus.

Donc, généralement, je vais simplement choisir activité vide.

Appelons notre application Tippie.

Le nom du package, généralement ce que je fais, c'est que je prends mon nom de domaine ou mon adresse e-mail et je l'inverse.

Donc, je vais le laisser tel quel et choisir un emplacement, assurez-vous d'avoir Kotlin, sélectionnez ce langage.

Et je vais choisir la version minimale du SDK API 21.

Maintenant, je vais taper sur terminer.

Et la toute première chose que j'aime faire chaque fois que j'ai un tout nouveau projet est simplement d'essayer d'exécuter le code de démarrage.

Parce que si nous ne pouvons même pas exécuter le code de démarrage, alors quelque chose a déjà mal tourné.

Assurons-nous que nous sommes à un bon point connu avant de commencer à écrire du code.

Lorsque nous créons un nouveau projet dans Android Studio, cela prendra un certain temps pour tout configurer.

Pour exécuter notre application, nous pouvons aller dans le menu déroulant et choisir de déployer notre application soit sur un émulateur, soit sur un appareil physique.

Donc, je vais choisir Pixel 2 API 29, qui est un émulateur que j'ai créé auparavant, appuyer sur ce triangle vert pour démarrer notre émulateur s'il n'existe pas déjà, puis construire et déployer notre projet sur cet émulateur.

Et vous verrez le statut en bas d'Android Studio pour voir la progression actuelle.

Cela peut prendre une minute ou deux.

Mais quand c'est fait, l'application sera automatiquement envoyée à l'appareil et mise au premier plan.

Donc, tout ce que nous avons à faire est d'attendre jusqu'à ce que nous voyions une action sur l'émulateur.

D'accord, super.

Cela semble prometteur.

Nous voyons une application appelée Tippie s'ouvrir sur l'émulateur avec le texte Hello World, qui est la valeur par défaut pour un projet vide.

Et cela nous donne confiance que nous sommes capables d'exécuter le projet de base avec succès.

Entrons dans Android Studio et passons une minute rapide à parler des fichiers de démarrage.

Et en fait, c'est assez simple car il n'y a que deux fichiers dont nous allons nous soucier : main activity dot kotlin et activity main dot XML. Vous pouvez penser à une activité en terminologie Android comme représentant un écran.

Donc avec le projet que nous avons, pour l'instant, nous n'avons qu'un seul écran.

Et cela est appelé l'activité principale ou l'écran principal.

Et c'est la logique métier que nous définissons ici dans ce fichier appelé main activity.

En particulier, le code de démarrage nous donne une fonction ou une méthode qui est déjà en cours de substitution.

Et cela s'appelle onCreate, le système Android appellera ou invoquera automatiquement cette fonction lorsque notre application démarre, lorsqu'elle crée notre écran.

Et la ligne importante ici est la ligne neuf setcontentview r dot layout activity main.

Donc R signifie ressources.

Donc ce que nous disons ici, c'est que le contenu ou l'interface utilisateur de notre écran devrait être le fichier de disposition dans les ressources, défini à activity main dot XML.

Et en effet, si nous sautons à la définition de cela, nous pouvons voir que cela va directement à activity main dot XML.

Donc je vais minimiser la fenêtre d'outil de projet ici pour nous donner plus d'espace.

Et cela minimise également le volet des attributs.

Voici exactement ce que nous voyons dans l'application, juste une toile vierge avec HelloWorld.

Et en particulier, si vous regardez l'arbre des composants ici, il peut être minimisé pour vous.

Mais vous pouvez l'expanser en tapant ici, nous pouvons voir que l'élément parent est quelque chose appelé un constraint layout.

Et il a exactement un enfant appelé un TextView, ou une étiquette.

Et cela a un attribut qui a la valeur hello world.

Et c'est ainsi que nous voyons le texte Hello World dans notre application en cours d'exécution.

Dans cette vidéo, nous allons passer tout notre temps dans activity main dot XML, car nous ne nous soucions que de la construction de l'interface utilisateur pour notre application.

Et en particulier, voici comment nous voulons finir, nous allons avoir huit composants dans l'écran.

À gauche, nous avons quatre vues de texte différentes, vous pouvez penser à un texte comme une étiquette, qui n'est pas modifiable par l'utilisateur.

À droite, nous avons les composants réels décrits par le TextView.

Donc nous avons un edit text en haut, qui permet à l'utilisateur de saisir un montant de facture, nous avons une seek bar, qui permet à l'utilisateur de saisir un pourcentage de pourboire, et ensuite deux autres textes en bas pour le montant du pourboire et le montant total.

Il y a une autre chose que je veux souligner avant de commencer à construire notre disposition, c'est qu'il existe plusieurs perspectives de notre interface utilisateur. Ce que nous regardons par défaut est un aperçu de la conception, qui est ce qui apparaîtra réellement sur votre émulateur ou appareil.

Mais vous pouvez également passer à l'onglet code, qui est le XML sous-jacent réel.

Donc vous pouvez voir comment nous avons le constraint layout et ensuite une vue enfant, la vue de texte, comme dans la conception.

Split signifie que vous regardez les deux.

Et la plupart de notre temps sera passé à regarder l'aperçu de la conception.

Et ce que nous pouvons faire, c'est aller dans la palette et glisser-déposer différents composants comme une vue de texte ou un texte éditable que nous voulons.

Et encore une fois, cela sera représenté dans l'onglet code.

Donc gardez simplement à l'esprit qu'il y a une correspondance un à un entre les modifications que vous apportez dans l'aperçu de la conception et le XML sous-jacent.

Donc pour l'instant, revenons à la conception, supprimons les composants que nous avons, donc nous avons un seul constraint layout sans enfants.

La documentation décrit le constraint layout comme un moyen de créer des dispositions grandes et complexes avec une hiérarchie de vues plates.

Nous sommes capables de décrire la relation entre les vues frères et les dispositions parentales à travers un ensemble de contraintes que nous définissons.

Et cela permet au système Android de disposer élégamment notre interface utilisateur sur des téléphones ou des tablettes de différentes tailles.

Et l'important ici est qu'il n'y a pas de groupes de vues imbriqués.

Sur Android, si vous avez une hiérarchie de vues très profondément imbriquée, cela conduit à une dégradation des performances et à quelque chose que nous appelons le jank, ou le lag de l'interface utilisateur.

Et donc le constraint layout nous permet de créer des vues complexes sans avoir de groupes de vues imbriqués.

Revenant au projet de calculatrice de pourboire, nous allons disposer les huit vues à l'écran ici dans un seul parent constraint layout, il n'y aura pas de groupes de vues imbriqués, ce qui est aussi bien que possible, pas de disposition relative ou de dispositions linéaires à l'intérieur de notre parent constraint layout.

Donc même si vous n'avez jamais travaillé avec le constraint layout auparavant, prenez un moment maintenant pour réfléchir à la manière dont vous pourriez positionner les vues à l'écran ici les unes par rapport aux autres, de sorte que nous puissions le décrire dans une hiérarchie de vues plates.

De retour dans Android Studio, la première chose que nous allons faire est de faire glisser une TextView représentant le composant en haut à gauche de notre écran, qui est la TextView représentant la table de base.

La première chose que je fais chaque fois que je fais glisser un composant est de mettre à jour l'ID pour qu'il soit plus significatif.

Donc je vais l'appeler TV base label et mettre à jour le texte pour qu'il soit base.

Et ce que vous remarquerez ici, c'est qu'Android Studio se plaint que cette TextView manque de contraintes.

Donc elle n'a que des positions de conception, elle sautera à la position 00, qui est le coin supérieur gauche de l'écran au moment de l'exécution, sauf si nous ajoutons des contraintes.

Et c'est tout l'intérêt du constraint layout, nous devons contraindre chaque composant verticalement et horizontalement.

Donc verticalement, ce que nous allons faire est de faire glisser ce point d'ancrage supérieur de la TV base label et de le faire glisser vers le haut de l'écran.

Et puis dans l'onglet attributs, nous allons spécifier la marge de la distance à laquelle nous voulons qu'elle soit du haut de l'écran, et je vais dire 48 en haut.

De même, nous voulons spécifier une marge gauche, donc nous allons faire glisser le point d'ancrage gauche et le faire glisser vers le parent et spécifier cela à 32 dP de l'extrémité gauche de l'écran.

Donc maintenant vous pouvez voir que l'erreur a disparu, nous allons faire le même processus maintenant pour les trois autres textes à gauche de l'écran.

En commençant par celui juste en dessous du label de base, c'est un TV tip percent label.

Auteur du texte ici pour être 24%.

La TextView en dessous de cela sera le TV tip label.

Le texte sera tip.

Et enfin, nous aurons le TV total label.

Et le texte ici sera total.

Donc nous avons le même problème où nous devons contraindre tous ceux-ci horizontalement et verticalement, verticalement, ce que nous allons faire est de prendre le point d'ancrage supérieur pour chaque TextView et de le faire glisser vers le composant au-dessus.

Et nous allons spécifier une marge de 32 dP, ce qui signifie que chaque texte devrait vivre 32 pixels à 32 dP en dessous du texte au-dessus, cela va faire glisser le point d'ancrage supérieur et le faire glisser vers le point d'ancrage inférieur du texte au-dessus.

Et encore, faire la même chose 32 dP contraindre chacune de ces vues verticalement.

Maintenant, comment faire horizontalement, si nous revenons à l'état final souhaité, ce que vous remarquerez, c'est que si nous traçons une ligne verticale ici, tous les composants du côté gauche, ils seront tous alignés sur l'extrémité droite de ce texte supérieur, ce TV base table.

C'est ainsi que nous voulons les contraindre horizontalement.

Et nous pourrions en fait faire cela dans l'onglet Design, vous pourriez dire aligner et puis aligner les bords droits.

Mais je voudrais vous montrer comment faire cela dans l'onglet Code.

Donc si j'ouvre l'onglet Code, comme nous en avons parlé, chaque changement que vous faites dans l'onglet Design a un changement correspondant dans l'onglet Code.

Donc maintenant nous avons quatre textures et c'est exactement ce que nous pouvons voir ici nous avons 1234, comme nous en avons parlé, il y a maintenant une erreur dans le fait que nous ne contraignons pas ceux-ci horizontalement.

C'est pourquoi nous avons ce soulignement rouge.

La contrainte verticale est ce que vous pouvez voir ici.

Donc ce que nous communiquons avec cette ligne est que le haut du TV tip percent label devrait être exactement égal au bas du TV basic, qui est un TextView au-dessus, avec une marge de 32 dP, ce qui signifie que vous voulez qu'il soit 32 pixels en dessous du composant au-dessus.

Donc de même, ce que nous voulons faire est de spécifier que la fin de ce composant, le TV tip percent label devrait être égal à la fin du TV base label.

Et nous voulons que cela soit appliqué à chacun des composants du côté gauche. Avec cela, vous pouvez voir comment cette erreur a disparu.

Et si nous revenons à l'onglet Design, vous pouvez voir comment tout est maintenant aligné.

Une autre chose que je veux souligner ici est que l'espace de noms des outils est uniquement utilisé à des fins de rendu de l'aperçu de la conception.

Parce que nous avons maintenant pleinement contraint chacune de ces vues horizontalement et verticalement, nous n'en avons pas réellement besoin.

Donc je vais sélectionner chacun de ceux-ci et les supprimer.

Et une autre chose est que je suis assez grand sur avoir un style cohérent et un ordre des différents noms d'attributs.

Par exemple, ici nous avons la balise de fin sur la même ligne ou nouvelle ligne.

Et pour le corriger automatiquement pour nous, je peux appuyer sur double shift, puis simplement rechercher re format.

Et il y a un raccourci pour reformater le code.

Si je fais cela, alors vous pouvez voir comment Android Studio nous a aidés à le corriger dans tout le fichier, ce que j'aime beaucoup plus.

D'accord, donc revenons dans l'onglet Design.

Et avant de passer au composant du côté droit de l'écran, une chose que je veux faire est juste quelques ajustements de design rapides.

Tout d'abord, je veux rendre le texte un peu plus grand ici.

Donc je vais faire l'apparence du texte moyenne, vous pouvez voir comment cela l'a agrandi.

Et puis ce TV tip present label est un peu unique, car il représente la valeur de ce que l'utilisateur a réellement choisi.

Donc pour indiquer qu'il est un peu différent des autres, je vais le rendre en gras ici.

Cool, j'aime ça.

Maintenant, réfléchissons aux quatre composants du côté droit de l'écran.

Celui-ci va être edit text, celui en dessous est seekbar.

Et puis en dessous, nous avons deux text views.

Donc, faisons glisser un edit text.

Et celui que nous allons faire glisser est celui qui dit un nombre de décimales.

Et la différence entre tous ces différents edit text est en fait assez simple.

C'est simplement le type d'entrée.

Parce que nous traitons avec la devise, nous voulons des nombres et des décimales dans les nôtres.

En dessous de cela, nous allons avoir une seek bar.

Et puis en dessous de cela, nous allons faire glisser deux TextView.

D'accord, mettons à jour les ID ici pour qu'ils soient plus sensés.

Donc cela va s'appeler at base amount.

Ensuite, nous avons la seekbar tip.

Ensuite, nous avons TV tip amount.

Et enfin, nous avons le TV total amount.

Mettons à jour le texte ici pour qu'il soit 103 point 11.

Et celui-ci, je pense que nous avons dit 1996.

Faisons quelques ajustements de design avant de positionner ces éléments.

Donc ces textures de fond, ce sont les parties les plus importantes de toute l'application.

Donc je vais rendre le texte grand.

La seekbar, je vais spécifier une largeur codée en dur de 200 dP pour la rendre un peu plus large.

Et puis il y a aussi un attribut ici appelé Max, qui est le montant maximum que la seekbar contiendra.

Et cela sera 30.

Parce que nous n'autorisons que jusqu'à 30%.

Pour le edit text, je vais définir les EMAS à huit, ce qui signifie combien de caractères de large, combien de caractères de large sera ce edit text et huit est suffisant pour nous, je vais augmenter la taille du texte à 24 SP.

Et puis enfin, je vais ajouter un indice ici ou un espace réservé, qui est le montant de la facture pour que l'utilisateur sache à quoi sert ce edit text.

Maintenant, réfléchissons à la manière de positionner ceux-ci.

Donc verticalement, les deux textures du bas doivent être alignées verticalement, donc je vais les sélectionner toutes les deux et puis aligner les centres verticaux.

Et de même pour celles au-dessus de celles-ci.

Et de même pour le pourcentage de pourboire et la seekbar.

Et vous pouvez voir comment dans l'onglet Design, nous sommes en fait capables de voir cet aperçu agréable des contraintes qui sont ajoutées.

Pour le montant de la facture.

Réfléchissons à la manière de le contraindre horizontalement, il sera à 32 dP de la TextView correspondante du côté gauche.

Et horizontalement, tous les autres composants du côté droit, ces trois du bas doivent être alignés sur l'extrémité gauche du montant de la facture edittext, il faut les sélectionner tous et je vais spécifier que les bords gauches doivent tous être alignés.

Cela a l'air bien.

La seule chose que nous devons faire maintenant est que si nous survolons ici, il nous manque une contrainte verticale sur le edit text.

Donc pour faire cela, je vais aller dans l'onglet code.

Voici le edit text at base amount.

Et la manière dont nous allons communiquer le positionnement vertical est en considérant le haut de cet élément par rapport au haut de la vue supérieure gauche qui est un TV base table et de même, le bas de cette vue devrait également être le bas du TV base table.

Donc il sera exactement au milieu verticalement.

Donc si vous revenez à l'onglet Design, vous pouvez voir que maintenant les erreurs ont disparu.

Et vous pouvez voir visuellement à quoi ressemblent ces contraintes.

Si vous revenez à l'onglet Design, encore une fois, nous n'avons plus besoin de cet espace de noms des outils, car nous contraignons tout.

Reformatons le code très rapidement.

Et puis une autre chose que je veux faire est, même si ce n'est pas nécessaire, pour les besoins de l'information du développeur, j'aimerais les étiqueter avec un commentaire.

Ce sont les vues du côté gauche.

Et puis après pour TextView, en commençant par le edit text, ce sont les vues du côté droit.

C'est bien de voir à quoi cela ressemble.

D'accord, super.

Comme nous nous y attendions, cela reflète presque exactement ce que nous voyons dans l'aperçu de la conception.

La seule chose que je veux corriger ici ou améliorer est qu'il est un peu étrange que nous ayons déjà des valeurs pour le pourboire et le montant total, même si l'utilisateur n'a rien saisi.

Et c'est exactement le but de l'espace de noms des outils dont nous avons parlé plus tôt.

Donc ce que je vais faire est de sélectionner la TextView correspondante.

Et plutôt que d'avoir un texte ici, je vais faire défiler vers le bas.

Je vais déplacer cela dans la zone de texte de la clé.

Et c'est l'espace de noms des outils.

Donc je vais déplacer ceux-ci dans le texte des outils.

Et puis enfin, la même chose ici.

Juste pour vous montrer ce que cela a fait, si nous revenons à l'onglet code, si vous regardez le TV tip percent label maintenant au lieu d'avoir l'attribut de texte Android, c'est maintenant l'attribut de texte des outils.

Si nous exécutons l'application une dernière fois, voyons l'impact que cela a sur la disposition initiale.

Super, cela a l'air assez bien.

Espérons que cette vidéo vous a donné une bonne idée de la puissance du constraint layout.

Une chose que je peux vous montrer pour démontrer ce que nous avons fait est qu'avec ces huit vues à l'écran, elles sont toutes situées au lieu d'un seul parent.

Et si je fais glisser cette TextView en haut à gauche, tout bouge en conséquence, ce qui est une très belle façon de contraindre relativement toutes les vues les unes aux autres.

Donc le travail dans la prochaine vidéo est en fait de connecter la logique métier dans l'activité principale, afin que nous puissions réagir à l'entrée et calculer le pourboire et le total.

À bientôt dans la prochaine vidéo.

Dans la dernière vidéo, nous avons disposé les huit vues à l'écran pour notre application de calculatrice de pourboire.

Dans cette vidéo, nous voulons ajouter la logique métier pour rendre notre application interactive. Nous aimerions pouvoir faire en sorte que lorsque l'utilisateur fait glisser la barre de recherche, nous voulons mettre à jour l'étiquette du pourcentage de pourboire.

Et lorsqu'ils entrent un montant de base, nous voulons prendre cette valeur et calculer le pourboire et le montant total.

En particulier, vous remarquerez qu'il n'y a pas de bouton Soumettre.

Donc dès que l'utilisateur change le montant de base ou le pourcentage de pourboire, nous voulons calculer dynamiquement le pourboire et le montant total lorsque quelque chose change.

Donc, comme premier exercice, ce que je veux pouvoir faire est que dès que l'utilisateur change la valeur sur une seekbar, je veux pouvoir mettre à jour l'étiquette du pourcentage.

Donc, pour ce faire, la première chose que nous allons faire est d'obtenir une référence aux vues de l'écran dont nous avons réellement besoin pour pouvoir lire des données ou les modifier.

Et il y a en fait cinq widgets différents à l'écran qui nous intéressent : l'étiquette du pourcentage de pourboire et puis tous les quatre composants du côté droit de l'écran.

Donc, dans Android Studio, la manière dont nous allons faire cela est de déclarer un tas de variables ici pour chacun des composants.

Par exemple, nous avons le edit text, ce sera at base amount.

Et le type de celui-ci va être un type edit text.

Mais ne vous inquiétez pas trop de la syntaxe ici.

Si c'est confus, tout ce que nous disons est une variable privée.

C'est une initialisation tardive car nous allons l'initialiser à l'intérieur de la méthode onCreate et non dans le constructeur, c'est pourquoi c'est une initialisation tardive, c'est une variable et que nous l'appelons at base mount, la convention que je suis est que le nom de la variable est exactement égal au nom de l'ID.

Donc maintenant dans le onCreate.

Après le set content view, nous allons dire at base mount find view by ID et base amount.

Et nous allons répéter cela maintenant pour les quatre autres composants à l'écran.

Donc nous avons un seekbar tip.

Et le type ici est seekbar.

Et puis nous avons TV tip percent.

Cela va être text to you.

Et puis nous avons deux autres textes pour nous.

L'un est TV tip amount, et l'autre est TV total amount.

Maintenant, je vais simplement obtenir des références à tous ceux-ci à l'intérieur de onCreate, et enfin nous avons le montant total.

Donc, revenant à notre objectif, la première chose que vous voulez faire est lorsque l'utilisateur fait glisser la barre de recherche, nous voulons être informés des changements de cette entrée utilisateur, puis mettre à jour l'étiquette TV tip percent pour l'indiquer.

Donc, en fait, laissez-moi mettre à jour le nom de la variable ici pour qu'elle soit TV 2% label pour la cohérence.

Et la manière dont nous sommes informés des changements sur la barre de recherche est en ajoutant un écouteur dessus, il dira seek bar tip dot set on seek bar change listener.

Et maintenant, nous devons dire à l'Android Studio ce qui devrait se passer lorsque la barre de recherche a changé.

Et la syntaxe ici est que nous allons dire object, seek bar.on, seekbar, change listener.

Et puis nous allons définir cette classe à l'intérieur ici.

Et Android Studio va nous aider à implémenter cela, vous aurez ce soulignement rouge sous l'objet pour taper sur cette ampoule rouge et taper sur implémenter les membres.

Il y a trois méthodes que nous devons substituer afin de nous conformer à la définition de cet écouteur de changement de barre de recherche.

Et Android Studio va nous aider avec cela.

Et ne vous inquiétez pas trop.

Encore une fois, la syntaxe est confuse.

Les détails ici sont que nous définissons une classe anonyme qui implémente cette interface.

Donc si je vais à la définition ici, vous pouvez voir que c'est une interface publique, qui a ces trois méthodes exactement que nous avons substituées.

Et maintenant, c'est à nous de dire au système ce qui devrait se passer lorsque chacune de ces méthodes est appelée.

Et en fait, nous ne nous soucions pas vraiment de on start tracking touch ou on stop tracking touch.

Donc je vais supprimer les deux dues ici, et laissons une implémentation vide.

Avant de mettre à jour l'interface utilisateur, ajoutons d'abord une instruction de journalisation dans Android pour déterminer plus facilement ce qui se passe.

Donc je vais taper logged on i et c'est une méthode qui prend deux paramètres.

Le premier est une chaîne, que j'appellerai tack, je vais définir plus tard.

Et le second est aussi une chaîne, qui est un message ou une instruction de journalisation.

Et je vais dire on progress changed, qui est un nom de méthode, ainsi que la progression, qui est la valeur actuelle de la barre de recherche.

Donc définissons cette balise, je vais aller en haut de la classe et définir une private const Val tag.

Et la convention ici est que chaque fois que vous avez un type de journalisation, la balise est généralement le nom de la classe.

D'accord, essayons.

Donc l'idée ici est que chaque fois que la progression a changé sur la barre de recherche, ce qui signifie que l'utilisateur fait glisser, nous allons imprimer la valeur actuelle montrée dans logcat, qui est où les logs sortent.

Donc ouvrons logcat.

Ouvrons l'émulateur.

Et les logs qui nous intéressent sont ceux de notre application uniquement, qui est calm, calm, rk Pandey Tippi et nous nous intéressons également uniquement aux logs de niveau info car c'est ce que log.io représente, les logs de niveau info.

Nous nous intéressons également uniquement aux logs qui ont cette balise particulière, qui est main activity.

Donc ajoutons main activity comme filtre.

Et ici, lorsque nous changeons la barre de recherche, vous pouvez voir comment nous obtenons une ligne de sortie logcat, et elle représente exactement ce qu'est l'indicateur actuel de la barre de recherche.

Donc si nous allons jusqu'au maximum, nous voyons 30 comme nous nous y attendons, et si nous revenons tout en bas, nous allons à zéro.

Donc maintenant, mettons à jour l'interface utilisateur.

Et en particulier, nous voulons mettre à jour l'étiquette TV tip percent pour indiquer la progression actuelle de la barre de recherche.

Donc nous allons dire TV 2%, l'attribut de texte de cela, nous allons le définir égal à la progression.

Mais en fait, nous voulons que la progression soit représentée comme une chaîne, et non un int.

Et aussi nous voulons concaténer un signe de pourcentage après.

Donc nous allons dire dollar sign progress, qui est la manière dont nous faisons l'interpolation de chaîne en kotlin.

Similaire à ce que nous avons fait dans une instruction de journalisation, et puis ajouter un signe de pourcentage à la fin.

Essayons.

Donc lorsque nous faisons glisser la barre de recherche, vous pouvez voir comment l'étiquette TV tip percent est mise à jour en synchronisation avec la progression actuelle de la barre de recherche, ce qui est génial.

Une amélioration ici, cependant, est qu'initialement, nous n'indiquons aucun pourcentage de pourboire dans l'étiquette.

Et pour corriger cela, définissons une autre constante, que nous appellerons initial tip present.

Donc nous aurons une private const Val initial tip present, et nous la définirons égale à 15.

Donc initialement, le pourboire par défaut sera de 15%.

Avec cela, définissons la constante avant de faire quoi que ce soit dans l'écouteur, super dans la méthode onCreate, nous allons dire seek bar tip dot progress est égal à initial tip percent.

Et nous voulons également mettre à jour l'étiquette de manière appropriée.

Donc nous allons dire TV tip percent label dot text est égal à initial tip percent, avec le signe de pourcentage après.

Maintenant, lorsque nous exécutons l'application, nous devrions voir au lieu de l'étiquette 2% vide, nous devrions voir 15% comme nous le faisons et l'indicateur de la barre de progression est exactement au milieu de la largeur de toute la barre de recherche.

Ensuite, similaire à la manière dont nous avons pu réagir aux changements dans la barre de recherche, nous voulons également pouvoir réagir aux changements dans le texte éditable. Il y a donc une méthode analogue sur le ET base mount que nous appellerons add text change listener.

Et la syntaxe est similaire, nous passons un objet ici, qui est une classe anonyme, une implémentation du text watcher.

Et nous allons avoir Android Studio nous aider une fois de plus, il y a quelques méthodes que nous devons substituer.

Donc je vais taper sur cette ampoule rouge et implémenter les membres trois, les substituer toutes.

Et puis similaire à avant, la seule chose qui nous intéresse est after text change, je vais supprimer le corps de l'implémentation ici.

Juste pour avoir une meilleure compréhension de ce qui se passe ici.

Encore une fois, ajoutons une instruction de journalisation après le changement de texte.

dollar sign ups.

D'accord, essayons.

Donc dollar sign s est le paramètre passé.

Et c'est en fait ce que l'utilisateur tape à ce moment-là.

Exécutez cela, ouvrons logcat une fois de plus.

D'accord, donc comme avant, si je modifie la barre de recherche, vous pouvez voir qu'elle change de manière appropriée.

Et puis si j'ajoute la valeur dans le texte éditable, vous pouvez voir 800, il est mis à jour de manière appropriée dans le journal.

Deux notes rapides.

Premièrement, je vois parfois des étudiants trébucher lorsqu'ils invoquent des fonctions en kotlin.

Le MSG que vous voyez lorsque nous appelons log into est un indice d'Android Studio sur ce que ce paramètre représente.

Donc si vous tapez réellement MSG, cela conduira à une erreur de compilation.

Donc assurons-nous que vous ne faites pas cela.

Deuxièmement, je veux démystifier ce que signifie le mot-clé object.

Donc les expressions d'objet comme nous les utilisons jusqu'à présent, sont des exemples de la manière de créer des classes anonymes, qui sont des classes à usage unique qui sont couramment utilisées pour implémenter des interfaces.

Donc nous avons à la fois text watcher et on seekbar change listener comme interfaces définies par le système Android.

Et ces méthodes que nous substituons seront automatiquement invoquées pour nous lorsque l'utilisateur effectue l'action appropriée sur le texte éditable ou la barre de recherche sous-jacente.

Donc maintenant nous avons tous les ingrédients en place pour rendre cette application fonctionnelle.

Chaque fois que le texte éditable change, je vais appeler une méthode appelée compute, tip, et total.

Et c'est en fait ce qui prendra les valeurs du texte éditable et de la barre de recherche et mettra à jour le pourboire et le montant total de manière appropriée.

Donc cette méthode n'existe pas encore.

Mais encore une fois, utilisons l'utilité d'Android Studio et faisons-la créer cette fonction pour nous à l'intérieur de main activity.

Et il y a quelques choses qui doivent se passer dans cette méthode.

Premièrement, nous voulons obtenir la valeur du basic tip present.

Deuxièmement, nous aimerions calculer le pourboire et le total.

Et troisièmement, nous devons mettre à jour l'interface utilisateur pour montrer ces valeurs.

Donc pour obtenir la valeur du basic tip, c'est assez simple, nous regardons simplement le texte éditable at base amount, nous prenons le texte, et puis nous appelons to string dessus.

Et puis sur une chaîne, nous savons qu'elle va être une devise comme une décimale, donc nous allons appeler to double dessus, afin de la transformer en un nombre avec lequel nous pouvons travailler.

Et nous allons appeler cela base amount.

Et puis de même, pour le 2%, nous voulons obtenir la valeur de la progression sur la barre de recherche, cet attribut appelé progress, et cela sera sauvegardé dans une variable que je vais appeler tip percent.

Assez suivant, nous voulons calculer le montant du pourboire et le montant total.

Donc le montant du pourboire va être le montant de base, multiplié par le pourcentage de pourboire divisé par 100.

Par exemple, si le montant de base est de 100 $, j'ai dépensé 100 $ pour un repas, et le pourcentage de pourboire est de 20, alors je m'attends à ce que le montant du pourboire soit de 20 $.

Donc ce serait 20 divisé par 100 est 20% fois 100.

Et cela me donne 20 $.

Donc ce sera tip amount.

Et puis nous avons le montant total, et le montant total sera simplement le montant de base, plus le montant du pourboire.

D'accord, enfin, nous devons mettre à jour l'interface utilisateur.

Et encore une fois, cela s'avère assez simple, car nous avons une référence aux deux vues de texte qui montrent le pourboire et le montant total, qui est TV tip amount, et nous allons définir l'attribut de texte là pour être tip amount.

Et cela va générer une erreur car tip amount est un nombre, c'est un double, mais nous avons en fait besoin de quelque chose appelé une séquence de caractères.

Et pour lui donner une séquence de caractères, nous pouvons simplement appeler to string dessus.

Et puis de même, nous devons dire TV total amount est que l'attribut de texte ici doit être le montant total to string.

Et cela devrait être un signe plus.

Attendez, c'est tout le cerveau de notre application.

Donc si nous exécutons cela, alors ce que nous faisons est que chaque fois que la valeur du texte éditable a changé, nous allons appeler cette méthode et nous devrions mettre à jour l'interface utilisateur pour avoir le montant correct pour le pourboire et le montant total, n'est-ce pas, donc nous avons 15%.

Pour le pourboire, si j'ajoute 100 $ ici, alors vous voyez immédiatement que nous obtenons le calcul correct du pourboire et du montant total.

Et nous aimerions avoir la même logique exécutée si je change la barre de recherche, le 2%.

Et cela s'avère être très facile, car nous avons abstrait toute la logique dans cette méthode.

Donc je vais appeler compute tip et total, juste ici dans on progress changed.

D'accord, donc si vous essayez cela maintenant, nous devrions avoir une application assez fonctionnelle.

Donc similaire à avant, si je mets 100.

Ici, nous calculons correctement 115.

Et si je change le pourcentage, vous pouvez voir qu'il est mis à jour de manière appropriée.

D'accord, donc cela fonctionne en fait assez bien.

Mais il y a deux choses que je pense être incorrectes ou qui pourraient être améliorées.

Mais prenez juste un moment maintenant pour réfléchir aux deux améliorations que vous pourriez apporter à l'application que nous avons maintenant, essayez de jouer avec, voyez si vous pouvez identifier des problèmes.

D'accord, donc la première amélioration que nous pouvons faire est en fait un bug.

Donc remarquez ce qui va se passer maintenant si je fais un retour arrière sur le montant de base, de sorte qu'il n'y ait rien là, donc vous pouvez voir que l'application a en fait planté.

Donc si nous regardons logcat, jetons un coup d'œil à ce qui était en fait l'erreur.

Donc je vais faire défiler jusqu'en haut de la trace de la pile.

Et vous pouvez voir ici que nous avons une exception de format de nombre.

C'est la partie importante, il y a une chaîne vide.

Et la trace de la pile nous dit exactement où le problème s'est produit, c'est à main activity ligne 58.

Et donc le problème qui se produit est que lorsque le texte éditable a une valeur vide, alors cela n'a pas de sens d'essayer de convertir une chaîne vide en un double.

La toute première chose que nous ne devrions pas faire ici est en fait de vérifier si at base amount done dot txt, si cela est vide, alors nous devons faire un retour anticipé.

De plus, nous devrions effacer les valeurs des TV tip et total amount.

Parce que si le texte éditable est vide, cela signifie qu'il n'y a rien à taper.

Et nous devrions ne rien montrer pour ces deux textures, puis nous appelons return, afin qu'aucune des autres parties de la fonction ne soit exécutée.

La deuxième amélioration que nous allons faire concerne le formatage de la sortie du pourboire et du montant total.

Ce n'est pas très perceptible lorsque nous entrons 100 pour le montant de base.

Mais si nous ajoutons 100.9, alors vous pouvez voir que le montant total devient très long et encombrant.

Parce que nous traitons avec de la monnaie, nous devrions vraiment exiger qu'il y ait exactement deux points décimaux dans le pourboire et le montant total.

Et la manière dont nous allons faire cela est juste ici, au lieu d'appeler simplement to string, nous voulons formater la chaîne avant de la mettre dans le TextView.

Donc la manière dont nous faisons cela est en utilisant cette méthode de format.

Donc nous définissons le format comme ceci percent.to F, ce qui signifie que nous voulons seulement deux chiffres après la virgule. format.

Et nous passons le montant du pourboire.

Et puis de même pour le montant total, un percent dot two f format.

Essayons.

Pour, espérons-le, maintenant, dans ce scénario, nous devrions en fait finir avec 116.04 au lieu de cette très longue décimale qui s'est produite 100 tout de suite, vous pouvez voir au lieu d'avoir seulement un point décimal maintenant nous en avons deux.

Et le vrai test est lorsque je tape 100.9.

Maintenant, l'affichage de cela est bien meilleur, nous avons 116.04 plutôt que cette énorme décimale qui devient illisible.

Donc à ce stade, nous avons une application très fonctionnelle, ce que nous avons fait est d'obtenir des références aux vues pertinentes sur la disposition, puis d'ajouter des écouteurs à la barre de recherche et au texte éditable car il n'y a pas de bouton Soumettre.

À chaque fois qu'il y a un changement dans la barre de recherche ou le texte éditable, nous calculons dynamiquement le pourboire et le montant total et mettons à jour les vues de manière appropriée dans ce calcul de pourboire et de montant total.

Donc dans la prochaine vidéo, ce que je veux vous montrer est quelques améliorations de style ainsi qu'une manière de le personnaliser et d'ajouter une animation vraiment cool.

Donc je vous verrai dans la prochaine vidéo.

À ce stade, nous avons terminé l'implémentation de notre calculatrice de pourboire.

Dans cette vidéo, notre objectif est d'ajouter de la couleur, de l'animation et de la personnalisation à l'application.

Donc nous allons commencer par le pied de page en bas.

Beaucoup d'applications ou de sites web ont cela où il est dit, vous savez, fait avec amour en Californie ou fait avec amour par cette personne.

Donc nous allons commencer par ajouter un texte en bas de l'écran.

Donc, entrons dans Android Studio, ouvrons l'activité main dot XML et faisons défiler jusqu'en bas et nous allons faire glisser un TextView ici.

Donnons-lui un ID de TV footer.

Et puis le texte sera fait avec amour par raw et bien sûr vous pouvez personnaliser comme vous voulez le contraindre.

Nous allons avoir cela horizontalement au centre de l'écran.

Donc nous allons ajouter une gauche et une droite Straight pour le centrer, et puis nous allons le mettre à 32 dP du bas de l'écran.

Je veux aussi ajouter quelques ajustements de style différents ici.

Le premier est tout en majuscules, je veux que tout ici soit en majuscules.

Et je veux changer la police pour qu'elle soit sans serif, condensée, légère.

Et puis enfin, je veux rendre ce texte un peu plus grand, apparence, poids moyen.

Et enfin, je veux changer le mot amour avec l'emoji.

Et vous pouvez soit l'ajouter à votre clavier, soit une autre façon de faire est si vous cherchez sur Google l'emoji cœur, alors le premier résultat qui apparaît, me donne une option ici pour copier et coller l'emoji.

collez cela.

Et cela a l'air un peu bizarre dans l'aperçu, mais cela s'affiche correctement lorsque vous le rendez dans le design.

Et si nous le vérifions dans l'application.

Super, cela a l'air assez bien.

La prochaine chose que j'aime faire est un peu le schéma de couleurs.

Donc nous nous éloignons de ces couleurs de barre d'état par défaut, couleur primaire dans ce fond blanc.

Donc laissez-moi expliquer d'où viennent ces couleurs.

Il y a un fichier très important qui doit exister dans chaque application Android.

Et cela s'appelle le fichier manifest Android.

Donc si nous l'ouvrons, alors ce fichier décrit tous les différents composants de votre application, les permissions, par exemple, si votre application a besoin de la permission Internet, et bien plus encore.

Et la ligne importante pour nous est juste ici à la ligne 11, où nous décrivons le thème de notre application, et c'est un fichier qui est automatiquement créé pour nous lorsque nous créons le projet vide.

Donc je vais sauter à la définition ici.

Et vous verrez que vous avez deux fichiers différents ici, un pour le thème normal et un pour le thème de nuit.

Et celui que nous regardons actuellement est normal, je vais l'ouvrir.

Et c'est ici que nous obtenons les couleurs pour l'application par défaut que nous avons.

Donc pour mettre à jour les couleurs, nous allons devoir définir de nouvelles couleurs et ensuite les remplacer ici, nous pouvons voir où se trouve ce fichier en cliquant sur cette option, sélectionner Ouvrir le fichier, et nous pouvons voir qu'il se trouve à l'intérieur des ressources, valeurs, et le répertoire des thèmes.

Et les couleurs sont également définies à l'intérieur de colors XML dans le répertoire des valeurs.

Et chacune des couleurs est définie comme une valeur hexadécimale, violet, 500, et ainsi de suite.

Donc notre travail est de déterminer quelles couleurs nous voulons, et puis de les ajouter ici.

Et puis nous les référencerons à l'intérieur du fichier XML des thèmes.

Donc pour déterminer quelles couleurs vous voulez, il y a quelques options différentes, je vais vous montrer ce que je fais généralement si vous allez sur color.adobe.com.

Il y a cet outil vraiment sympa où vous déterminez quel type de schéma de couleurs vous voulez.

Donc il y a quelques options différentes ici, vous pouvez choisir la règle d'harmonie des couleurs, analogue monochrome chromatique triade, et ainsi de suite.

Une fois que vous êtes satisfait de quelque chose, alors vous pouvez faire défiler vers le bas et obtenir les valeurs hexadécimales ici.

Donc j'ai déjà fait cet exercice.

Et voici les couleurs que j'ai trouvées, je vais en avoir une qui s'appelle bleu primaire, bleu plus foncé et bleu de fond.

Donc, allons-y dans le XML des couleurs et définissons ceux-ci pour le premier qui va s'appeler bleu primaire maintenant a cette valeur.

Le suivant est bleu de fond, ou le suivant est un bleu plus foncé.

Et enfin, nous avons le bleu de fond.

Donc maintenant dans le XML des thèmes, j'ai mis à jour la couleur primaire pour qu'elle soit bleu primaire.

Et puis j'ai mis à jour la variante primaire pour qu'elle soit bleu plus foncé, et cela va être la couleur de la barre d'état.

Et puis enfin, afin d'avoir une couleur de fond sur toute l'application, je vais ajouter un autre attribut ici, qui s'appelle couleur de fond, Android couleur de fond.

Et cela va être le bleu de fond que nous avons.

Essayons.

Super, cela a l'air génial.

Donc nous nous rapprochons maintenant de l'état final souhaité, nous avons le pied de page, et nous avons la couleur personnalisée.

La dernière chose dont je veux parler est cette animation sur la description du pourboire.

Et voici en fait à quoi cela ressemble.

Alors que l'utilisateur fait défiler, nous allons mettre à jour dynamiquement la couleur de ce mot qui est utilisé pour décrire le pourcentage actuel de pourboire, et il passera du rouge si c'est un très mauvais pourboire à un vert vraiment vif si c'est un très bon pourboire.

Non seulement cela, mais nous allons également changer ce mot ou cet adjectif utilisé pour décrire le pourcentage de pourboire.

Donc cela donne à l'utilisateur un retour interactif vraiment agréable sur le type de pourboire qu'ils laissent.

D'accord, donc la première chose que nous allons faire est de simplement ajouter un text you besoin de la barre de recherche et d'augmenter la distance verticale entre ces deux textes.

Donc fermez ces autres fenêtres d'édition car nous n'avons plus besoin de les regarder.

Dans l'activité main.

Ce que nous allons faire est d'abord augmenter la distance entre le 24% qui est l'étiquette 2% et le TV tip label.

Augmentons la marge ici à 56 Ensuite, faisons glisser un autre text you.

Et nous l'appellerons TV tip description.

Et puis le texte devrait être vide, car cela dépendra du pourcentage initial de pourboire, qui est défini par programmation.

Mais pour avoir une meilleure idée de ce à quoi cela pourrait ressembler, nous allons utiliser un espace de noms d'outils et dire acceptable ici.

Cela a l'air bien.

Et maintenant nous devons positionner cela horizontalement et verticalement.

Donc verticalement, il sera juste en dessous de la barre de recherche, et nous ajouterons une marge ici de peut-être 8 dp.

Et puis nous voulons que ces deux éléments soient alignés horizontalement.

Donc les centres horizontaux, super.

Et vous pouvez voir comment il a ajouté les contraintes de gauche et de droite.

Donc il sera exactement au milieu.

Et vous pouvez voir que l'erreur a également disparu.

Donc maintenant dans MainActivity, nous devons obtenir une référence à ce TextView.

Donc disons que l'ID ici était TV tip description.

Donc quand je dis TV tip description, obtenir une référence à cela ici.

Et chaque fois que le C part est changé, c'est là que nous avons le potentiel maintenant, de mettre à jour le langage sur ce texte, vous voulez avoir une autre méthode ici appelée update tip description.

Et laissons Enter nous aider à créer cela car cette méthode n'existe pas encore.

Et une chose que nous allons faire en fait est en tant que paramètre dans la méthode de mise à jour des descriptions de pourboires, j'aimerais passer dans la progression et la progression.

Et encore une fois, energy video peut maintenant nous aider à ajouter cela comme un paramètre dans la fonction que nous avons définie.

Tapez sur cette ampoule rouge, et laissez Enter nous aider à ajouter le paramètre et tout ce que j'ai fait ici est ajouté un paramètre.

Et au lieu de l'appeler progression, je vais l'appeler tip percent.

Et c'est ce que j'ai tapé.

Donc maintenant l'idée est que sur la base de la valeur de tip percent, nous aimerions pouvoir dire TV tip description dot txt, et nous aimerions pouvoir le définir comme étant quelque chose comme bon.

Et bien sûr, ce bon changera en fonction de la valeur.

Et la construction en kotlin.

Pour pouvoir décider de la valeur de quelque chose en fonction d'un ensemble de conditionnels s'appelle when, qui est similaire à un switch en Java.

Donc je vais sauvegarder notre description de tip est égale à when et puis selon la valeur de 2% nous prendrons certaines actions.

Donc si la description de tip, si 10% est entre zéro et neuf, alors la chaîne devrait être pauvre.

Si c'est entre 10 et 14, nous l'appellerons acceptable 15 et 19, ce sera bon.

Et quand c'est entre 20 et 24.

Ce sera génial.

Et il devrait y avoir une période supplémentaire ici.

Et enfin, n'importe quoi d'autre signifiant que la valeur est au-dessus de 24 alors nous dirons incroyable.

Et donc maintenant au lieu d'utiliser bon ici, nous dirons description de tip.

Et enfin avant de tester cela, une autre chose que je veux faire est tout au début, lorsque nous configurons notre écran, qui est, vous savez, dans la méthode onCreate, dès que nous obtenons toutes les références à chacune des vues, nous aimerions également appeler cette méthode update tip description juste ici avec le pourcentage initial de tip juste pour que le langage soit toujours en synchronisation avec ce avec quoi nous commençons.

Essayons.

Donc maintenant, espérons que nous devrions voir un text you juste en dessous de la barre de recherche et le texte dans ce text you devrait changer selon ce que nous avons sélectionné via la barre de recherche.

D'accord, cela semble déjà prometteur car initialement le 2% est de 15, ce qui signifie que nous tombons dans cette branche de l'instruction wine et cela signifie que la valeur devrait être bonne.

C'est bien.

Et puis si nous le ramenons à zéro, nous obtenons pauvre et si nous allons jusqu'au bout, nous devrions obtenir incroyable ce que nous faisons.

Une chose rapide à faire est de revenir dans activity main.

Je veux définir le poids de la police de ceci pour qu'il soit gras.

Le textile devrait être en gras pour le faire ressortir un peu plus.

Enfin, la dernière chose que je veux montrer est cette animation de couleur interactive où si l'utilisateur choisit un très bon pourboire, nous montrons un vert vif et si l'utilisateur choisit un mauvais pourboire, alors nous montrons une couleur rouge indiquant que quelque chose ne va pas.

Revenant dans Android Studio dans l'activité minute kotlin, la mise à jour de la description du pourboire est l'endroit où nous allons ajouter la logique pour mettre à jour la couleur en fonction du pourcentage de pourboire.

La question est comment calculer dynamiquement une couleur en fonction d'un entier, la manière dont nous allons faire cela est à travers un concept appelé interpolation, qui est en fait un mot fantaisiste pour quelque chose qui est conceptuellement assez simple.

Si je vous dis que je cours 100 miles, et que j'ai terminé 75% du chemin, alors vous me diriez que je suis environ au 75ème mile.

Et ce que vous faites dans votre tête est une interpolation linéaire, vous supposez que je cours à une vitesse constante en commençant à zéro et en terminant à 100.

Par conséquent, je suis à 75 miles, la même chose s'applique exactement ici.

Chaque couleur peut être représentée comme un entier.

Donc si je donne un pourboire de 20%, alors nous sommes à deux tiers du chemin entre la couleur la plus mauvaise et la couleur la meilleure, qui sont deux entiers.

Et tout ce que nous devons faire est un peu de maths simples afin de calculer exactement quelle est cette valeur de couleur, pour la description du pourboire.

La première chose que nous allons faire est de définir la couleur pour le pire investissement en pourboire.

Donc ouvrez colors, XML, et ajoutons la couleur words tip color, best tip et j'ai choisi une couleur rouge et verte comme nous en avons parlé, nous allons coller ces valeurs pour la couleur worse et la couleur best.

Donc nous avons ceux-ci définis.

Et maintenant notre travail est simplement de faire un peu de maths à zéro, nous devrions montrer le pire pourboire à 30, nous devrions montrer le meilleur pourboire et tout le reste est une valeur intermédiaire.

et cela s'avère être si courant que Android a en fait quelque chose appelé un évaluateur RGB pour aider avec cela, où nous représentons les couleurs comme des valeurs entières.

A signifie alpha, RGB est rouge, vert, bleu, et il aidera à calculer la couleur pour nous.

Donc en revenant dans main activity, nous allons définir une couleur.

Et celle-ci proviendra de argb evaluator dot evaluate.

Et puis cela prend trois paramètres.

L'un est la fraction de l'endroit où nous sommes sur cette barre de progression entre zéro et 32, le deuxième est une valeur de départ, qui est la couleur la plus mauvaise et la valeur de fin est la meilleure couleur.

Donc la fraction sera simplement le pourcentage de pourboire, qui est le paramètre passé 10 divisé par le montant maximum de pourboire qui est 30.

Et cela va être seapark tip dot max.

Ensuite, nous devons obtenir la couleur la plus mauvaise.

Et la manière dont nous allons faire cela est context compat dot get color pass in this qui fait référence au contexte et puis la couleur réelle que nous venons de définir dans le XML des couleurs, qui est color first.

Et puis enfin, nous allons fournir la meilleure couleur ici.

Un problème que vous remarquerez est qu'il y a une incompatibilité de type, nous avons besoin d'un float, mais nous avons trouvé un entier.

Par défaut, parce que le numérateur et le dénominateur sont tous deux des entiers, nous allons faire une sorte de troncature, que nous ne voulons pas.

Donc la manière de gérer cela est de convertir l'un des numérateurs ou dénominateurs en une valeur float.

Et cela résoudra le problème.

Donc maintenant nous avons cette couleur, tout ce que nous devons faire est de définir la couleur sur le texte de description du pourboire, set text color, avec la couleur.

Et enfin, avant d'essayer cela, nous devons convertir le résultat de l'appel de la fonction evaluate en un entier, car nous savons que les valeurs que nous calculons sont des entiers, donc la couleur devrait être un int.

Et maintenant nous devrions pouvoir compiler et exécuter cela sans problème.

Donc deux choses devraient se passer maintenant.

L'une est que nous devrions mettre le texte en gras.

Et deuxièmement, il devrait y avoir une couleur appliquée immédiatement.

Et en fonction du pourcentage que nous choisissons, elle devrait s'adapter également.

D'accord, cela a l'air bien.

Donc initialement, nous avons une couleur juste entre le vert et le rouge.

Et si je descends jusqu'à zéro, vous pouvez voir comment cela change en rouge.

Et si je monte jusqu'au meilleur pourboire, qui est 30, vous pouvez voir comment cela se transforme lentement du rouge au vert.

J'aime beaucoup cela juste parce que cela semble beaucoup plus interactif et dynamique maintenant par rapport à ce que nous avions avant.

D'accord, donc faisons un dernier essai.

Nous allons mettre 9 $ ici pour la facture.

Et puis lorsque je fais défiler, vous pouvez voir comment tout est mis à jour de manière appropriée.

Si je fais un retour arrière, il n'y a pas de plantage, je peux entrer un autre montant.

Et tout fonctionne comme nous nous y attendons.

Super.

Donc si c'est votre première application Android, c'est incroyable.

Félicitations.

Faites-le moi savoir dans un commentaire.

La raison pour laquelle j'ai vraiment aimé la calculatrice de pourboire, c'est qu'il y a tant de façons d'étendre ce projet de base que nous avons pour le rendre plus intéressant.

Donc quelques idées que j'ai eues : numéro un, vous pourriez diviser la facture par n personnes.

Donc vous pourriez imaginer que vous sortez dîner avec un certain nombre de personnes, vous ajoutez trois ou quatre et puis vous devriez diviser ce montant total par trois ou quatre afin de faciliter le paiement pour tout le monde d'un certain montant.

Deuxièmement, vous pourriez ajouter un bouton ou un composant qui permet à l'utilisateur d'arrondir le montant final vers le haut ou vers le bas.

Donc il n'y a pas besoin de gérer la monnaie.

Et bien sûr, il y a beaucoup plus que vous pourriez faire en termes de design ou de mises à jour de couleur.

Donc ce que je recommande maintenant est de compléter un nombre quelconque d'extensions, d'autres que nous avons mentionnées, ou quelque chose que vous avez imaginé vous-même, et puis vous pouvez plus ou moins publier exactement ce que vous avez sur le Play Store.

Je ne vais pas passer par cela ici, mais je vais laisser une vidéo dans la description où je parle de la manière de faire cela et j'espère que vous utiliserez cette calculatrice de pourboire comme point de départ dans votre parcours en tant que développeur Android et que vous construirez beaucoup plus d'applications à l'avenir.

Si vous avez aimé cela, laissez un like et un commentaire.

Nous aimerions avoir de vos nouvelles.

Merci beaucoup d'avoir regardé et je vous verrai dans la prochaine vidéo.

Au revoir