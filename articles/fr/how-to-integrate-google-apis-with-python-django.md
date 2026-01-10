---
title: Comment intégrer les API Google avec Python Django
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-08-17T13:32:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-integrate-google-apis-with-python-django
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/djangoapis.png
tags:
- name: Django
  slug: django
- name: youtube
  slug: youtube
seo_title: Comment intégrer les API Google avec Python Django
seo_desc: 'Google has a bunch of different APIs. It can be tricky to figure out how
  to incorporate them into a Django project.

  We just released a course on the freeCodeCamp.org YouTube channel that will teach
  you how to build a Django app that uses multiple Goo...'
---

Google dispose d'un ensemble d'API différentes. Il peut être difficile de comprendre comment les intégrer dans un projet Django.

Nous venons de publier un cours sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à construire une application Django utilisant plusieurs API Google.

Bobby Stearman a créé ce cours. Bobby est un développeur expérimenté et a créé de nombreux cours utiles sur sa chaîne YouTube.

Les API incluses dans ce cours sont l'API Google Places, l'API Google Maps, l'API Google Directions, et plus encore.

Voici les sections couvertes dans ce cours :

* Configuration et activation des API Google
* Configuration de Python et Django
* Développement backend tel que les modèles, vues et URLs
* Développement frontend tel que HTML et JavaScript
* Test de notre nouvelle application

Regardez le cours complet ci-dessous ou sur [la chaîne YouTube freeCodeCamp.org](https://www.youtube.com/watch?v=_vCT42vDfgw) (2 heures de visionnage).

%[https://www.youtube.com/watch?v=_vCT42vDfgw]

## Transcription

(générée automatiquement)

Apprenez à utiliser Django avec six API Google différentes dans ce cours de Bobby Stearman.

Hey, tout le monde, c'est Bobby de Decoding ici.

Et dans ce cours, je vais vous guider et vous montrer comment construire une application Django qui utilise six API Google différentes.

Alors commençons avec la visite guidée.

Si vous regardez mon écran, vous pouvez voir que j'ai déjà l'application ouverte sur la page de connexion.

Donc si nous cliquons sur s'inscrire, car nous n'avons pas actuellement de compte utilisateur, il y a Bobby stemmen.

Et nous aurons un nom d'utilisateur. Cela doit être un email, Bobby at did demo.com.

Mot de passe, j'utiliserai Fred Fred one.

Confirmer le mot de passe, Fred, Fred one, nous avons aussi une bascule pour afficher les mots de passe, elle convertit une entrée de mot de passe en entrée de texte.

Donc vous pouvez voir qu'ils correspondent.

Si je clique sur S'inscrire, lorsque je clique sur S'inscrire, nous utiliserons la version trois du logiciel recapture.

C'est un produit Google qui note une soumission de formulaire.

Et plus le score est élevé, plus il est probable qu'il s'agisse d'un être humain réel qui soumet le formulaire, c'est génial.

Le fait que nous ayons cet élément dans le coin inférieur droit de l'écran suggère que le logiciel fonctionne.

Donc cette inscription devrait obtenir un message qui dit merci de vous être inscrit et sera ensuite redirigé vers la page de compte utilisateur.

Le compte utilisateur, l'utilisateur peut alors mettre à jour son profil avec une adresse.

Et c'est là que nous utilisons l'API Google Places.

Donc c'est prédictif.

Donc lorsque je tape dans l'entrée, Google prédira l'adresse dans le pays qui est prédéfini dans les paramètres, dot p y, et vous donnera un certain nombre d'adresses différentes qui correspondent à la recherche.

Alors allons-y avec 123.

Et cela donne quelques adresses différentes, cette adresse 123 Victoria Street, lorsque je clique dessus, elle pré-remplit certaines entrées cachées.

Et ensuite j'ai l'option de mettre à jour.

Votre profil a été mis à jour.

D'accord, donc c'est l'une des API.

L'autre est en route.

Donc cette application vous permettra de mettre un point de départ, donc une origine, un point de passage, un, un point de passage, deux et la destination.

Et lorsque nous soumettons cela, ou en fait, lorsque nous avons terminé la quatrième entrée ici, programmatiquement, elle créera une chaîne de paramètres et nous redirigera vers une URL différente, et elle affichera la carte.

Alors ajoutons quelques adresses.

Donc nous irons à une, high streets, Sutton eally, ils auront une autre, high one High Street, had them easily.

Donc c'est tout autour de mon quartier.

Ensuite, nous allons à une, High Street, stratum ealey.

Et enfin, nous ferons un marché.

facilement.

Les voilà.

Lorsque je clique dessus, il dira alors bien, vous avez complété les quatre points de passage.

Et si vous regardez en haut ici, c'est créer une chaîne de paramètres fantaisiste, mais l'URL est map.

Donc il montre la longitude et la latitude de départ et de destination, la durée de l'origine à la destination, la distance entre l'origine et la destination, et ensuite il affichera une carte, ce qui est brillant.

Et si je clique ensuite, cliquez ici pour les directions, il démasquera alors certains éléments en HTML.

Et il vous montrera chaque étape nécessaire de l'origine à la destination.

Donc c'est l'application que j'ai construite.

C'est celle que nous allons parcourir dans ce cours, je passerai en revue chaque étape nécessaire, depuis l'activation des API chez Google et recapture, en commençant un nouveau projet, en construisant le backend, en construisant le frontend et en testant complètement l'application.

Alors sans plus attendre, passons à la section une.

Hey, tout le monde, c'est Bobby de decode ici et dans ce segment, nous allons configurer deux clés d'API Google.

Ces clés d'API nous permettront d'interagir avec six API Google.

La première que nous allons examiner aujourd'hui est quelque chose appelé google recaptcha.

C'est un logiciel qui empêche les logiciels malveillants d'interagir avec votre site web.

Donc, essentiellement, il garde les indésirables à l'écart et permet aux vrais humains de soumettre des formulaires.

Vous avez déjà rencontré cela sur les sites web d'autres personnes, vous remplissez un formulaire et lorsque vous soumettez ce formulaire, on vous présente neuf images et on vous demande de sélectionner toute image qui peut contenir un bus, un avion ou une moto.

Et si vous sélectionnez les bonnes images, vous pouvez alors soumettre le formulaire, c'est une soumission de formulaire basée sur un défi.

Et c'est la version deux, nous n'utiliserons pas la version deux aujourd'hui, nous utiliserons la version trois.

Celle-ci n'est pas basée sur un défi.

Au lieu de cela, Google attribue un score à chaque soumission de formulaire selon certains critères.

Plus le score est élevé, plus il est probable qu'il s'agisse d'un être humain réel qui soumet le formulaire, c'est génial.

Le fait que nous ayons cet élément dans le coin inférieur droit de l'écran suggère que le logiciel fonctionne.

Donc c'est ce que nous allons configurer aujourd'hui.

Et après cela, nous irons sur Google Cloud, et nous configurerons une autre clé d'API qui nous permettra de configurer et d'activer cinq API : Places, Directions, Distance Matrix, géocodage et Maps JavaScript.

Alors passons directement à la configuration de recapture.

Si vous regardez mon écran, il s'ouvre sur google.com, slash recapture slash about sur cette page, vous trouverez toutes les informations dont vous avez besoin pour en savoir un peu plus sur recapture.

Mais ce qu'il fait, certains cas d'utilisation et aussi l'histoire parce qu'il a évolué au fil des ans, lorsque vous êtes sur ce site, assurez-vous d'avoir un compte Google, vous en aurez besoin, cliquez sur la console d'administration V3.

Vous pouvez voir ici que j'ai six sites, j'utilise cela depuis un certain temps, et beaucoup de mes clients aiment utiliser recapture.

Mais que vous ayez déjà configuré cela sur votre machine ou non, vous devez suivre ce processus.

Donc vous devez cliquer sur le petit bouton plus ici, qui est pour créer un nouveau site.

Alors créons votre site.

Et nous l'appellerons Google Django tutorial, nous utiliserons reCAPTCHA version trois.

Encore une fois, il est indiqué vérifier la demande avec un score.

C'est ce que nous voulons, la version deux vérifie la demande avec un défi.

Donc nous cliquerons sur la version trois.

Et ensuite vous devez ajouter le domaine.

Donc nous faisons cela dans un environnement de développement.

Donc c'est sur ma machine locale, et nous utiliserons Django.

Donc le domaine dans ce cas est localhost.

Vous n'avez pas besoin de mettre le port d'un spa pour l'instant, j'ai un port local.

Et ensuite cliquez sur Accepter.

Et soumettre.

Les voilà.

Donc il crée une clé et une clé secrète pour travailler avec les API.

Si vous avez déjà fait cela, vous le savez, mais si ce n'est pas le cas, j'aime considérer les clés API comme ceci.

Une clé API est l'équivalent d'un nom d'utilisateur.

Et une clé secrète API est l'équivalent d'un mot de passe, essayez simplement de les garder secrètes, car vous ne voulez pas que les gens obtiennent vos clés et fassent des appels fictifs.

Donc voici copier la clé du site, j'aime simplement les mettre dans un bloc-notes pour pouvoir les utiliser plus tard.

J'en ai un ouvert ici.

Donc nous capturons la clé de soulignement, et nous collons la clé en arrière sur le site web.

Nous copierons la clé secrète.

Et nous la mettrons ici aussi.

Vous pouvez voir ici que j'en ai une autre appelée Google égale, c'est la clé API que nous allons configurer maintenant.

C'est tout ce que nous devons faire pour configurer recapture.

Le reste est fait dans le code en Python, ou dans ce cas, le framework web Django, que nous allons configurer dans le prochain segment.

Donc nous allons continuer maintenant.

Et nous allons configurer la clé API Google qui nous permettra de travailler avec Places, Directions, Distance Matrix, géocodage et Maps JavaScript. Ce que vous devez faire, c'est visiter le site cloud.google.com.

Et c'est le site web.

Vous aurez besoin d'un compte Google.

Vous pouvez voir que j'ai mon icône ici, mon logo, et la configuration est en train de décoder.

Lorsque vous êtes configuré sur Google, vous devez cliquer sur console.

Il vous emmènera à votre console d'accueil.

Et ensuite vous devez configurer un nouveau projet.

Donc si vous regardez simplement ce que j'ai fait ici.

sur ici, cliquez simplement sur la liste déroulante.

Et ensuite vous pouvez configurer un nouveau projet.

Et nous appellerons cela Google Django tutorial.

Cliquez sur Créer.

Et ensuite, lorsqu'il a terminé, vous pouvez alors sélectionner le nouveau projet que je viens de faire, il fait sa magie.

seulement prendre une seconde.

D'accord, c'est complet.

Donc maintenant cliquez sur le projet que nous venons de configurer.

Et voici la nouvelle page d'accueil Google Django tutorial.

Vous devez maintenant cliquer sur API et services.

Lorsque vous y êtes, vous avez l'option de cliquer sur Activer les API et services.

Mais d'abord, nous devons cliquer sur les identifiants, nous devons configurer la clé API, cliquez sur cliquez sur les banjos.

Cela sera une ardoise vide, nous devons maintenant quitter cliquer sur Créer des identifiants.

Cela nous permettra de sélectionner différentes options.

Mais celle que nous voulons aujourd'hui est la clé API, cliquez sur la clé API.

Les voilà, copiez la clé API.

Et sauvegardez cela dans le bloc-notes.

Les voilà de retour sur le site web.

Fermer.

Maintenant, nous ne l'avons pas nommé, nous pouvons le nommer en cliquant sur ce petit stylo ici pour éditer la clé API.

Et ici, vous pouvez restreindre la clé API à certaines adresses IP.

Changer le nom, ce que nous allons faire, c'est Google Django.

clé de tutoriel.

Et sauvegarder.

Au moment où vous verrez ce tutoriel, ce tutoriel sera mort, c'est-à-dire qu'il sera supprimé de Google.

Donc il n'y a aucun risque ici.

C'est la clé, nous avons configuré la clé maintenant, nous devons maintenant activer les API.

Donc si nous allons dans le tableau de bord, encore une fois, cette option ici, donc plus, activer les services API là.

Et parce que les cartes sont le service API le plus populaire que Google fournit, il est tout en haut, cliquez sur Voir tout 17, il y en a pas mal.

Faites défiler vers le bas, il y a tout un tas d'API différentes ici.

La première que nous devons examiner est l'API Places.

Je ne vais pas passer en revue ce que chacune d'entre elles fait spécifiquement, mais chacune d'entre elles, à votre rythme, cliquez dessus, et cela vous donne un aperçu de ce qu'elles font exactement.

Maintenant, nous utiliserons Places pour pré-remplir les adresses lors de la création d'un compte dans notre projet.

Donc vous commencez à taper une adresse, et il prédira quelle est l'adresse que vous recherchez.

Et vous pouvez simplement la sélectionner, et elle pré-remplit toutes les adresses, la ville, la ville, le comté et le code postal, et ainsi de suite.

Et vous pouvez toujours extraire la longitude et la latitude, ce qui est très, très utile.

Donc cliquons sur Activer.

Cela prendra une seconde.

Et maintenant que cela est terminé et activé, nous devons maintenant chercher l'API Directions.

Donc vous pouvez revenir à l'aperçu et cliquer sur activer les API et revenir au tableau de bord principal.

Mais parce que nous en avons activé une maintenant, cela vous donne ensuite quelques options d'autres API avec lesquelles vous pouvez travailler.

Donc regardons l'API Directions.

cliquez sur activer cette prochaine API, donc les directions, la distance, le géocodage et les cartes JavaScript, ce sont les API que nous allons utiliser pour calculer différents itinéraires et distances entre deux points géographiques, donc deux longitudes et latitudes.

Donc c'est l'API Directions, nous avons maintenant besoin de la matrice de distance.

Nous allons l'activer rapidement.

Certaines d'entre elles sont assez explicites, pour être franc.

La suivante est le géocodage Google.

Eh bien, voici que cela nous permet de géocoder certains points.

Donc l'API de géocodage permettra cela.

Enfin, nous devons trouver l'API JavaScript Maps et l'activer.

Et cela nous permettra d'écrire un peu de JavaScript pour faire les appels eux-mêmes, car nous ne ferons pas d'appels API depuis Django, les appels eux-mêmes seront gérés en JavaScript.

Donc cliquons sur l'API JavaScript Maps.

Activer.

Les voilà.

Donc pour récapituler, dans ce segment, nous avons créé deux clés API.

L'une d'elles est avec google recaptcha version trois, cela nous permettra de nous assurer que de vrais humains soumettent des formulaires sur notre projet et d'empêcher les indésirables de soumettre ces formulaires.

Et ensuite nous avons créé une autre API sur Google Cloud et activé les API Google Places, Google Directions, Google Distance Matrix, Google Geocoding et Google Maps JavaScript.

Cela nous permettra à nos utilisateurs de compléter ou de commencer à taper leur adresse, et cela prédira où ils vivent et ils pourront sélectionner une adresse.

Et aussi ils pourront alors ajouter deux points différents.

Donc deux emplacements dans n'importe quel pays donné, et notre projet calculera alors l'itinéraire et la distance entre ces points.

D'accord, c'est la fin de ce segment.

Merci d'avoir regardé.

Cela commence à configurer le projet dans le prochain segment.

Merci.

Au revoir.

Hey, tout le monde, c'est Bobby de Decoded ici.

Et dans ce segment, je vais vous montrer tout ce que vous devez faire pour commencer à construire cette application Google API.

Donc nous utiliserons un framework web Python appelé Django et nous travaillerons sur la façon de démarrer un nouveau projet, comment créer une application, comment configurer certaines paramètres et fichiers statiques tels que CSS, JavaScript et images, et aussi jouer avec le comp. URL.

Maintenant, si vous êtes familier avec Django, vous savez ce que tout cela signifie.

Cependant, si vous êtes un débutant absolu, je vais vous montrer rapidement un peu sur Python et Django, et une bibliothèque que nous allons utiliser, qui est virtual MV wrapper dash lorsque dans mon cas, parce que j'utilise une machine Windows, donc si vous regardez sur mon écran, j'ai le site web Python ouvert sur leur page de téléchargements.

Si vous n'avez pas téléchargé Python sur votre machine, vous devrez le faire, j'ai un lien vers une vidéo qui est en haut de l'écran maintenant et qui vous montrera exactement ce que vous devez faire pour installer Python et aussi configurer une bibliothèque appelée Virtual envy wrapper.

Et c'est cette page ici.

Donc c'est sur un dépôt dans pyp.org.

Comme je le dis, regardez la vidéo, suivez toutes ces étapes, installez Python sur votre machine, installez virtuellement un V wrapper sur votre machine, et vous serez prêt à partir.

Le troisième onglet ici est le site web Django project.com.

Donc c'est le framework web Django.

Donc il est dit ici que Django facilite la construction d'applications web plus rapidement avec moins de code, c'est exactement ce qu'il fait.

Et c'est ce qui m'a attiré vers Django il y a cinq ou six ans, je l'utilise depuis assez longtemps, il est facile à apprendre, la documentation est absolument fantastique.

Et ils ont un assez bon tutoriel sur le site web, nous devons cliquer sur le lien Get Started with Django ici, et vous y allez.

Mais c'est ce que nous allons utiliser dans le segment d'aujourd'hui pour commencer.

Donc ce que nous allons faire, nous allons commencer par ouvrir une invite de commande.

Et si vous avez déjà configuré virtuellement un V wrapper, alors vous pouvez commencer à utiliser certaines commandes.

C'est pourquoi je vous ai demandé de suivre cette vidéo.

Parce que si vous n'aviez pas configuré virtuellement un V wrapper, alors vous ne pourriez pas utiliser les mêmes commandes que je vais utiliser aujourd'hui.

Donc ce que je vais faire tout de suite, je vais CD dans mon répertoire de développement.

Et ce que je vais faire, c'est que je vais configurer un nouveau virtuel E et V.

Et la façon de le faire est MK virtuel e m v.

Et ensuite avec un espace, vous nommez cet E et V.

Donc nous allons l'appeler comme le projet.

Donc nous allons faire did Django Google API tutorial.

D'accord, cliquez sur Entrée.

Et cela va faire toute la configuration nécessaire sur votre machine.

Et cela va configurer un virtuel E et V.

Donc ce que je vais faire, je vais vous montrer rapidement ce que cela vient de faire.

Donc si je clique sur mes répertoires ici, nous allons dans mon propre.

Donc si nous allons à Bobby, qui est la configuration par défaut, cela va configurer un fichier E et V dans votre répertoire utilisateur.

Donc vous pouvez voir ici que j'ai des envies, et je viens de configurer did Django Google API tutorial.

Si je l'ouvre, lib site packages, ce sont tous les packages de site dont nous avons besoin pour travailler avec Python.

Donc ils viennent directement de la boîte.

Donc lorsque vous configurez un virtuel E et V, c'est ce que vous obtenez.

Nous allons ensuite installer Django et quelques autres bibliothèques et elles s'ajoutent à chaque fois que nous faisons pip install une bibliothèque.

Cela s'ajoute à notre virtuel E et V.

Donc c'est ce que nous venons de faire en ajoutant en utilisant make virtual E et V.

Retournez dans notre invite de commande.

Et ce que nous allons faire maintenant, c'est pip install Django for plus enter was asked, donc j'ai probablement survolé cela, mais la commande PIP est essentiellement un gestionnaire de packages standard, et permet d'installer et de maintenir des packages pour Python.

Donc nous utilisons pip install pour installer certains packages à partir du dépôt public tel que p ypi.

Et je viens de faire pip install Django.

Si je retourne dans mon répertoire envy que je vous ai montré il y a un instant, vous pouvez voir maintenant que nous avons le package Django ici, et dans Django, il vient directement de la boîte, il vient avec un tas de répertoires différents, et modèles et vues et tout ce qui s'ensuit, et c'est essentiellement comment Django fonctionne.

Donc nous allons faire des appels, créer des modèles, créer des vues et des formulaires.

Et tout interagit avec ces répertoires et fichiers ici.

Donc nous avons maintenant un environnement virtuel entièrement configuré et Django installé, nous pouvons maintenant démarrer un nouveau projet.

Donc vous devez taper Django dash admin, puis appeler start project et ensuite vous devez nommer le projet.

Donc nous allons l'appeler exactement comme ça.

Même que l'environnement de développement ou l'environnement virtuel, désolé, did Django Google API tutorial ? D'accord, cela devrait être fait.

Donc si j'ouvre mon répertoire à nouveau, le voilà Bobby développement.

Et ici nous avons did Django Google API tutorial, ouvrez-le.

Et c'est ce qui vient directement de la boîte, nous avons un fichier manage.py.

Et ensuite nous avons le répertoire principal ici, activer les paramètres, les URLs, vous avez ASCII ou whisky et vous avez un init, Dunder init file là.

Donc cela a très bien fonctionné, nous devons maintenant créer notre première application.

Donc Django nous permettra d'avoir de nombreuses applications fonctionnant dans un projet.

Donc ce que nous devons faire est d'ouvrir notre invite de commande, et nous devons maintenant CD dans did Jango.

Google API tutorial.

Et maintenant que nous avons le projet là, nous pouvons maintenant accéder au fichier manage.py.

Et c'est le fichier manage.py qui est dans le projet principal ici.

Donc nous faisons un appel à manage dot p y.

Donc nous disons Python, manage dot p y start app.

Et nous appellerons celui-ci main.

D'accord, super.

J'ai ouvert mon répertoire à nouveau, nous avons maintenant une application ici appelée main.

Et directement de la boîte, elle vient avec quelques fichiers.

Donc vous avez un répertoire de migrations vide.

C'est ce qui est utilisé lorsque nous créons des modèles.

Et vous migrez ces modèles vers une base de données, nous avons un fichier admin, un fichier X, nous avons un fichier modèles, c'est là que vous hébergez tous les modèles pour le projet, les tests et les vues, nous allons créer un ou deux autres fichiers, mais c'est ce qui vient directement de la boîte.

Nous sommes maintenant au point où nous allons commencer à écrire du code.

Pour ce faire, nous aurons besoin d'un éditeur de texte, j'utilise Sublime Text.

Mais il y a tellement d'éditeurs de texte différents, utilisez celui que vous préférez, et ensuite vous pouvez commencer à coder.

Donc ce que nous allons faire, nous allons ouvrir Sublime Text dans notre répertoire que nous venons de créer did Django Google API tutorial.

Donc le voilà.

C'est le projet dans Sublime Text, vous pouvez voir que nous avons notre fichier manage.py ici, nous avons le répertoire du projet principal, que vous pouvez ouvrir et vous pouvez regarder ces fichiers.

Et ensuite nous avons l'application principale que nous avons ici, nous allons concentrer notre temps dans settings dot p y, et vous êtes ELLs dot p y aujourd'hui, qui est le fichier URL comp.

Donc nous allons ouvrir le settings dot p y, en premier lieu.

Et si je fais défiler vers le bas, vous avez tout un tas de code ici qui vient directement de la boîte de Django, c'est très, très standard.

Nous devons cependant changer une partie de ce code.

Et c'est ce que nous allons faire tout de suite.

Donc en haut du fichier settings.py, ici, vous avez from path lib import path qui est requis.

Mais nous avons aussi besoin d'une autre importation.

C'est import OS pour le système d'exploitation.

Cette bibliothèque nous permet d'accéder à des choses comme les variables d'environnement, d'accord, et nous allons faire défiler un peu plus bas.

Si nous construisions cela dans un environnement de production ou pour une application de production, alors je ferais quelque chose avec une clé secrète ici, j'utiliserais des bibliothèques comme Django decoupled pour supprimer les informations sensibles du projet.

Mais comme nous ne faisons rien de tel, et que ce n'est qu'un tutoriel, je vais simplement le laisser tel quel.

Donc si vous faites défiler plus bas, encore une fois, nous avons autorisé les hôtes, c'est quelque chose de plus pour la production.

Vous avez ensuite les applications installées.

Ce sont les applications installées qui viennent directement de la boîte.

Mais nous avons créé une application ici appelée may have you look in apps, le nom de celle-ci est main.

D'accord, donc c'est ce que nous devons référencer dans settings dot p y.

Donc si nous entrons quelques fois, juste pour ajouter un peu d'espace blanc.

Ajoutez simplement une chaîne appelée main, puis une virgule, une virgule finale.

Donc cela indique à Django que l'application que nous venons de créer est effectivement incluse dans le projet.

Ensuite, si vous faites défiler un peu plus bas, nous avons middleware.

Nous ne jouerons pas avec cela ici.

Mais il y a certaines bibliothèques que nous nécessitons ou d'autres applications nécessitent.

Et elles ont besoin que vous ayez certaines modifications de middleware.

Routes URL comp, pas besoin de changer cela, modèles.

Nous ne changerons pas cela, application whisky, pas de changement, pas de changement avec la base de données non plus.

Maintenant, si je devais faire cette application pour une application de production, j'utiliserais probablement une base de données comme PostgreSQL.

Mais nous utiliserions simplement la base de données qui vient directement de la boîte, il n'y a pas de mal à cela, donc le code de langue, il est par défaut en us, je suis en Grande-Bretagne, donc en GB.

Et ensuite en bas ici, nous avons une variable ici appelée static URL.

Maintenant, nous allons créer cette application et elle aura l'air fantastique.

Pour ce faire, nous devons utiliser des fichiers tels que les feuilles de style en cascade, ou CSS et les fichiers Java scripts ou j s, et aussi des images telles que des logos et des choses comme ça.

Donc nous devons configurer les fichiers statiques dans le settings dot p y.

Et comment nous faisons cela, c'est que nous ajoutons une variable appelée static files underscore does.

C'est une liste.

Et ici, nous avons, nous appelons la bibliothèque OS que nous venons d'importer.

path, qui était également important en haut de la page.

Et puis nous avons joint, et nous avons joint le répertoire de base.

Et nous l'appelons static.

C'est le seul changement que nous devons ajouter ici pour les fichiers statiques, l'URL static reste la même, mais nous en avons également besoin ici appelé static route.

Les voilà.

Et c'est OS dot path, dot join dot, puis parenthèse et puis c'est encore base Dir.

Mais celui-ci est static.

CDN.

D'accord, ce sont les seuls changements que nous devons apporter à Settings dot p y en ce qui concerne les fichiers statiques.

Vous avez besoin de ces variables pour que cela fonctionne et serve les fichiers CSS et JavaScript au projet, au frontend, je ne ferai pas de plongée plus profonde que cela.

Nous avons maintenant besoin de trois variables de plus.

La première s'appellera Google API key.

Laissons cela comme une chaîne vide pour l'instant, nous avons besoin de re recapture.

Cool, cette clé recapture à nouveau, vide, et nous aurons recapture cool, sa clé secrète secrète sauvegardée avec une clé secrète.

Les voilà.

Et ce que je vais faire, c'est ouvrir les notes que j'ai prises dans le dernier segment.

Et nous avons besoin de notre, il semble que je n'ai pas dit la clé secrète.

Mais nous allons l'obtenir.

Nous allons la sauvegarder maintenant.

C'était la clé API Google.

Les voilà.

Et la clé secrète, je devrais l'obtenir de recapture dans quelques instants.

En fait, faisons cela maintenant.

Capture.

L'un des sites que nous faisions était celui-ci, Google Django.

Et je crois que nous avons les clés que nous avons.

D'accord, nous copions la clé secrète.

Retour dans notre projet.

Et nous sauvegardons cela et recapture la clé secrète.

Les voilà.

C'est le fichier settings dot p y complet, nous n'avons pas besoin de faire plus de configuration là-dedans.

Le prochain changement est dans URLs dot p y.

Et ce que nous devons faire dans ce fichier, c'est que nous devons avoir le chemin, nous devons l'importer, nous devons le faire depuis django.com.

Maintenant, lorsque je référence les répertoires Django, je référence littéralement ceux dans le fichier MV.

Donc retournez ici, lib site packages.

Vous vous souvenez lorsque nous configurions l'environnement virtuel, si nous allons maintenant dans Django, et dans le projet ici, Django dot URLs.

Nous allons dans Django et allons dans URLs.

Nous référençons ces fichiers ici et les fonctions et classes dans ces fichiers.

C'est exactement ce que nous faisons.

C'est ainsi que nous les importons dans le projet.

D'accord.

Donc depuis django.com import settings.

Donc nous importons maintenant, entre autres, tout ce que nous avons dans ce fichier ici.

Ensuite, depuis Django, dot content, dot URLs dot static, import, static, cela semble correct.

D'accord, donc nous avons besoin de Django qui vient avec admin.

Et j'ai déjà été payé directement depuis la boîte.

Mais nous devons ajouter un autre chemin ici.

Et celui-ci sera vers nos URLs principales que nous n'avons pas encore ajouté ce fichier, mais nous allons le référencer maintenant.

Donc est path.

Et ce que nous devons faire, c'est utiliser cet include que nous venons d'importer.

Et c'est main, et nous aurons un fichier dans cette application principale appelé URLs.

Et ensuite nous utiliserons namespace equals, cela s'appellera main.

Magnifique, ce sont les motifs d'URL dont nous avons besoin.

Nous avons également besoin d'un autre paramètre ici pour les fichiers statiques.

Et ce que nous faisons, c'est si settings dot debug, nous référençons debug, qui est dans settings.py, en haut, donc il est par défaut vrai.

Donc lorsque nous sommes en développement, lorsque debug est vrai, lorsque vous avez un problème avec votre code, ou que vous rencontrez une erreur à l'écran, ce qui est très pratique, mais vous n'avez pas cela, vous n'auriez pas debug défini comme vrai en production.

Donc s'il est défini sur vrai, ce qui est actuellement le cas, nous devons ajouter aux motifs d'URL.

Et comment vous faites cela, c'est URL add equals static, c'est la bibliothèque que nous avons ici.

Et ensuite nous voulons settings dot static URL.

Et ensuite nous voulons document route.

Equals settings dot static route.

Et c'est tout.

Donc le settings dot static URL, c'est ce que nous avons configuré dans le fichier settings.py.

Donc l'URL statique, et la route statique est aussi celle-ci que nous avons configurée également.

Donc nous avons maintenant configuré le fichier settings dot p y, et le fichier URLs comp correctement.

Et cela devrait maintenant fonctionner.

Une dernière chose avant de clore ce segment.

Et c'est que nous référençons un fichier URL qui n'est pas là.

Donc si nous allons dans main, nouveau fichier, et nous appellerons cela you are ours dot p y, nous créerons la liste nécessaire qui est requise pour la conversion d'URL.

Donc nous dirons from Django dot URLs, import path from Dart, donc cela référencera un fichier de vues, qui est ici.

Import views, donc nous importerons tout depuis views.

app name.

Donc c'est ce que nous avons appelé l'application en tant qu'espace de noms dans l'URL comp, main.

Et ensuite nous voulons you are l patterns equals, et c'est une liste vide.

Nous ajouterons cela dans une autre section.

D'accord, donc juste un récapitulatif de ce que nous avons parcouru aujourd'hui.

Nous avons configuré un nouveau projet Django, nous avons créé une nouvelle application, nous avons ajusté le fichier settings.py, nous avons configuré les fichiers statiques dans les paramètres et l'URL Comm.

Et nous avons ensuite ajouté les motifs d'URL dans la configuration d'URL également.

Donc nous sommes maintenant prêts à partir.

Nous sommes prêts à commencer à coder cette application.

Et nous le ferons dans le prochain segment.

Donc merci d'avoir regardé.

À bientôt.

Au revoir.

Tout le monde est publié et décodé ici.

Et dans cette section, nous allons suivre là où nous nous sommes arrêtés dans la précédente où nous avons commencé un nouveau projet Django.

Dans cette section, nous allons développer le backend.

Ce que je veux dire par là, c'est que nous allons créer des modèles, ou un modèle, en fait, vous savez, nous utilisons un modèle de profil qui étend le modèle d'utilisateur intégré qui vient directement de la boîte de Django.

La raison pour laquelle nous faisons cela est que nous voulons que nos utilisateurs aient la capacité de s'inscrire et de se connecter et de créer votre profil.

C'est ainsi que nous allons utiliser l'API recapture et l'API Google Places.

D'accord, nous allons également créer quelques formulaires, quelques vues et URLs et quelques mixins pour les vues.

Ces mixins nous aideront essentiellement à rendre notre code un peu plus facile à lire.

Et ces mixins seront recyclables.

Nous pouvons les utiliser dans d'autres applications également, ce qui est génial.

Et ensuite nous allons également créer les répertoires de modèles, donc cela sera considéré comme le backend.

Dans la section suivante, nous allons examiner le frontend qui concerne tous les fichiers HTML, CSS, Cascading Style Sheets et JavaScript.

Donc sans plus attendre, passons directement à cela.

Vous pouvez voir sur mon écran ici que j'ai quatre onglets ouverts, tous sur Doc's dot Django calm dot com.

Comme je l'ai dit dans la dernière section, la documentation Django est sans égal.

Et je voulais juste passer rapidement en revue cela parce que nous travaillons avec des modèles, nous travaillons avec des signaux, des formulaires de modèle et des vues.

Donc pour ceux qui sont absolument, eh bien, ils sont nouveaux dans Django, cela va être assez utile.

Donc qu'est-ce qu'un modèle, un modèle est une source d'information définitive unique sur vos données, contient les champs et comportements essentiels des données que vous stockez.

Généralement, chaque modèle correspond à une seule table de base de données.

Donc les modèles se traduisent par des tables de base de données.

Comme je l'ai dit dans la dernière vidéo, nous allons utiliser SQL lite, qui vient directement de la boîte de Django, vous pouvez passer à quelque chose comme PostgreSQL.

Mais nous ne le faisons pas dans cette application.

Donc lorsque nous construisons notre modèle de profil utilisateur, nous allons utiliser des choses appelées champs de modèle.

Et le plus important, nous allons utiliser des champs char et des champs float et des choses comme ça.

Mais le plus important que nous utilisons est le champ one to one, qui lie le profil utilisateur au modèle utilisateur intégré, qui vient directement de la boîte avec Django.

Et nous allons créer le profil utilisateur en utilisant des signaux.

Donc c'est des modèles, une vue très, très rapide de haut en bas des modèles.

Et de toutes façons, lisez bien ces pages de docs lorsque vous aurez un peu plus de temps, signaux.

Donc nous allons créer un fichier signals.py.

Cela gérera la logique de création du profil utilisateur lorsqu'un utilisateur est créé.

Donc nous allons utiliser post save et receive un décorateur.

Pour faire cela.

Je vous montrerai ce que tout cela signifie lorsque nous y arriverons.

Ensuite, nous avons des formulaires de modèle.

Donc nous créons un formulaire de modèle.

Donc ce sera un formulaire de modèle lié directement au modèle de profil utilisateur.

Nous allons également créer deux autres formulaires, ces formulaires hériteront de certaines classes de formulaire intégrées que Django a directement dans la boîte, l'une d'elles est un formulaire de création d'utilisateur.

Et l'autre est un formulaire d'authentification.

Ces formulaires gèrent la logique de l'inscription et de la connexion parfaitement.

Donc cela signifie simplement que nous n'avons pas à gérer toute cette logique, nous pouvons simplement appeler form dot save.

Et cela fait tout cela en arrière-plan, ce qui est génial.

Django est tout au sujet d'obtenir autant de résultats avec aussi peu d'entrées que possible.

Donc si nous pouvons nous en sortir en utilisant certains modèles et classes intégrés et formulaires et choses comme ça, nous le ferons.

Donc oui, comme je le dis, nous allons utiliser le formulaire de création d'utilisateur pour construire un formulaire utilisateur.

Et nous allons utiliser le formulaire d'authentification pour construire un formulaire d'authentification.

Et ensuite nous allons regarder la vue.

Donc nous allons créer des vues basées sur des classes et des vues basées sur des fonctions, je trouve que certains tutoriels en ligne se concentrent sur l'une ou l'autre.

Et lorsque vous êtes nouveau dans Django, cela peut être assez déroutant, surtout si vous avez concentré votre attention sur les vues basées sur des fonctions.

Les vues basées sur des classes peuvent alors sembler un peu étranges.

Donc je fais un peu des deux dans ce tutoriel, juste pour aider les nouveaux débutants.

Donc passons directement à cela.

Vous pouvez voir que c'est là que nous nous sommes arrêtés.

Oui.

D'accord.

Donc si nous ouvrons notre invite de commande, vous pouvez voir que j'ai mon environnement virtuel lancé, et je suis dans le bon fichier.

Maintenant, nous allons travailler avec des API.

Comme vous le savez, c'est tout le but de ce tutoriel.

Et dans Django, il y a une excellente bibliothèque appelée requests qui nous aide énormément avec les appels API.

Donc tout ce que vous avez à faire pour l'installer est d'utiliser la commande PIP.

Donc pip install requests.

Super.

Et cela sera maintenant dans notre fichier E et V que je vous ai montré il y a deux vidéos.

Maintenant, ce que nous devons faire est de démarrer une nouvelle application.

Donc nous allons Python manage.py start app, et nous appellerons cela users.

C'est super.

Si je regarde maintenant dans Sublime Text, vous devriez maintenant voir un répertoire utilisateurs, ce qui est super.

Il est pratiquement vide, mais nous allons commencer à le développer dans une seconde.

Donc la première chose que nous devons faire lorsque nous démarrons une nouvelle application est d'aller dans set this dot p y et d'enregistrer cette application dans les applications installées.

Donc users training comm comma, et il y a quelques autres variables dont nous avons besoin dans settings dot p y que j'ai oubliées dans la dernière section.

Donc nous allons le faire maintenant.

Je vais copier beaucoup de code depuis mon autre écran dans cette section, car cela fera gagner beaucoup de temps, cela rendra la section beaucoup plus courte et j'espère pouvoir retenir votre attention un peu plus longtemps.

Comme nous utilisons la logique de connexion, de déconnexion, de connexion et de déconnexion, nous allons ajouter quelques variables dans settings dot p y, c'est une URL de connexion.

Donc c'est là que les utilisateurs se connecteront.

Donc nous n'avons pas encore créé cette URL.

Mais nous le ferons dans cette section, nous avons une URL de redirection de connexion, qui est account, cela agira comme la page d'accueil.

Maintenant, il y aura un décorateur.

Donc un décorateur login required sur cette vue.

Donc lorsque quelqu'un visite la page d'accueil ou la page d'index, il sera redirigé vers cette page de connexion.

Mais cela fonctionne pour cette application.

Donc je l'ai gardé ici.

Et enfin, nous avons une redirection de déconnexion.

Donc lorsque quelqu'un s'inscrit, il redirige cet utilisateur vers la connexion.

Donc ce sont les trois variables dont nous avons besoin dans settings, dot p y.

Et il y a une dernière variable avant de passer à l'URL comp, et c'est le pays de base.

Donc le JavaScript que j'ai dans son projet utilise un code de pays.

Et il utilise ce code lors de la prédiction des adresses pour l'API Places.

Donc vous pouvez le changer en quelque chose comme fr pour la France, et d'autres codes de pays.

Mais cela signifie simplement que nous pouvons le changer dans les paramètres sans avoir à le changer dans le JavaScript.

Donc maintenant nous devons aller dans le fichier URL comp et ajouter les utilisateurs au motif d'URL.

Donc nous allons faire cela rapidement.

Juste copier cela, il n'est pas nécessaire de toujours le taper à partir de zéro, ou bien cela aide lorsque vous apprenez Django.

Mais ma frappe est terrible.

Donc j'ai tendance à parsemer ces applications de fautes de frappe et cela cause toute une série de problèmes.

Donc c'est tout ce que nous devons ajouter dans le fichier URL comp, c'est sauvegardé.

Donc c'est le paramètre, nous fermons ceux-ci.

Et maintenant ce que nous devons faire est d'aller dans les URLs principales, et ce que nous allons faire est de copier cela dans les utilisateurs dans un nouveau fichier, nous allons changer le nom de l'application en utilisateurs.

Et nous allons sauvegarder cela sous le nom de URLs dot p y, car nous référençons cela dans URL comp, p y.

Les voilà.

D'accord, donc maintenant nous sommes prêts à partir, nous sommes prêts à commencer les modèles maintenant.

Donc nous ne créons aucun modèle dans Maine, Maine sera utilisé pour quelques vues, comme les routes et la carte.

Et les utilisateurs géreront toute la logique d'authentification.

Donc nous ajouterons les modèles ici.

Donc si je prends simplement mon code, et je vais le copier et je vais littéralement le déposer ici, puis vous expliquer ce que je fais.

Donc le from django.db import models vient directement de la boîte, et ensuite nous sommes installés.

Donc nous importions l'utilisateur, qui est le modèle d'utilisateur intégré dont je parle sans cesse.

Donc vous vous habituerez à écrire cela.

Donc Django dot contrib dot auth dot models import user, je l'ai normalement dans chacun de mes vues.

Donc vous vous habituez à écrire cela assez souvent.

Nous avons ensuite le profil utilisateur, qui est une classe et tout mot de passe models dot model.

Dans mes modèles, j'ai généralement un horodatage et une mise à jour, cela me permet de suivre quand un modèle a été créé.

Donc nous utilisons l'auto add aussi dans auto now add equals true.

Et la mise à jour est aussi maintenant, donc chaque fois qu'un profil est créé, cela capturera la date et l'heure.

Et chaque fois qu'un profil est mis à jour, il mettra également à jour ce champ avec la nouvelle date et l'heure lorsqu'il a été mis à jour, puis quel utilisateur, c'est l'important et c'est le champ one to one dont je parlais, vous passez par le modèle utilisateur.

Et ensuite vous avez aussi underlay equals models dot cascade, je déplace cela, vous pouvez tout lire.

Donc cela signifie que si l'utilisateur était supprimé, alors ce profil utilisateur serait ensuite supprimé également.

Donc il n'y a pas de profil dans la base de données qui n'est pas lié à un utilisateur réel, vous pouvez aussi avoir quelque chose comme set null là.

Donc si l'utilisateur était supprimé, cela serait toujours dans la base de données, mais il serait null.

Ensuite, tout un tas de champs char.

Avec left, ceux-ci seront créés comme des noms analogues aux utilisateurs vides equals true car les utilisateurs ajouteront une adresse une fois qu'ils se seront inscrits.

Donc nous avons un champ char pour l'adresse, Max length 100, vous devez avoir cela, un mot-clé max length, car sinon cela ne fonctionnera tout simplement pas.

Et nous avons ville, comté, code postal, pays, longitude et latitude.

Ils sont tous remplis lorsqu'un formulaire est soumis depuis le frontend, que nous allons examiner sous peu.

Capture score, c'est le score de recapture.

Donc pour moi, lorsque quelqu'un s'inscrit, nous allons utiliser l'API de recapture pour noter la soumission, plus le score est élevé, plus il est probable qu'il s'agisse d'un être humain réel qui soumet le formulaire, ce score est transmis et enregistré dans ce champ en tant que champ float.

Le score le plus élevé que vous pouvez obtenir est 1.0.

Donc il est par défaut à 0.0 a profile est un champ booléen.

Donc c'est un simple vrai ou faux, il est par défaut à faux.

Donc lorsqu'un utilisateur s'inscrit, il n'a pas de profil lorsqu'il ajoute une adresse et une longitude et une latitude.

Cela sera alors changé en vrai.

Enfin, nous avons un booléen inactif.

Je l'ai toujours dans mes modèles, il est par défaut à vrai mais nous avons la possibilité de le changer en faux si jamais vous voulez fermer un modèle.

Et enfin, nous avons une fonction Dunder string, pass resell from was returning an F string self dot user.

D'accord, donc c'est le modèle.

Comme je le dis, cela se traduit directement par la base de données.

Donc lorsque nous faisons des migrations et migrons, cela deviendra une table de base de données.

Donc c'est notre modèle.

Nous devons maintenant créer quelques formulaires.

Donc si je clique sur ajouter un nouveau fichier, et enregistrer sous, et nous appellerons cela forms dot p y.

Les voilà.

Donc nous avons trois formulaires, un formulaire utilisateur, un formulaire auth, et un formulaire de profil utilisateur.

Donc nous importons quelques morceaux ici, laissez-moi vous faciliter un peu la tâche.

Donc nous importons model form, comme je le dis, nous avons quelques formulaires de classe intégrés qui viennent directement de la boîte, user creation form et authentication form.

Encore une fois, nous importons le modèle utilisateur intégré, puis nous importons form de Django, et enfin, le profil utilisateur des modèles que nous venons de créer.

C'est tout ce dont nous avons besoin dans ce fichier, nous avons ensuite le premier formulaire utilisateur, celui-ci hérite du formulaire de création d'utilisateur.

D'accord.

Donc ce que vous devez faire, c'est créer quelques variables.

Donc first name est forms, character fields.

Donc en tant que char field, Max length 30.

C'est exactement ce que le champ est dans le modèle utilisateur intégré.

En fait, puis nous commençons avec le formulaire de profil utilisateur, cela pourrait avoir un peu plus de sens.

Donc ce n'est qu'un formulaire de modèle, mais ils sont plus ou moins exactement les mêmes.

Donc address, vous pouvez voir ici, cette adresse est directement liée au champ d'adresse du profil utilisateur.

Et encore une fois, c'est un champ de caractères, qui est le même que dans le modèle, la longueur maximale est de 100, ce qui correspond à la longueur maximale dans le modèle.

Donc nous avons essayé de garder les formulaires de modèle identiques à ce qu'ils seraient dans les modèles eux-mêmes, nous avons required true, donc ce champ doit être complété pour que le formulaire soit soumis.

Et ensuite nous utilisons visit a socket widget equals form.

Et ceci sera une entrée cachée.

Donc le widget dans un formulaire de modèle qui se traduit en éléments HTML.

Donc ceci créera un élément d'entrée caché, et il sera rendu sur le fichier HTML.

Donc vous pourriez aussi avoir une entrée de texte, vous pourriez avoir une entrée de mot de passe, ou vous pourriez avoir toute une gamme de choses différentes.

Et vous pouvez aussi passer des choses comme des classes, et des placeholders et des choses comme ça.

Et c'est ainsi que nous pouvons changer l'apparence du formulaire sur le frontend.

Parce qu'un formulaire très, très basique de Django ne semble pas trop bien à moins que vous n'ajoutiez des morceaux, comme des classes et des IDs et des noms et ensuite ajoutez un peu de CSS.

Donc c'est le formulaire de profil utilisateur, aka dit un formulaire de modèle, nous avons address, town, county, postcode, country, longitude et latitude, ils seront les éléments d'entrée qui seront en fait cachés sur le fichier HTML, puis nous avons class matter, le modèle auquel nous lions ceci est user profile, et puis nous avons un tuple dans fields avec tous les noms de champs.

D'accord, donc c'est le profil utilisateur.

Donc je vais commencer là.

Et puis cela laissera faire un peu plus de sens lorsque nous regarderons uniform.

Donc comme je le dis, hérite du formulaire de création d'utilisateur.

Donc le prénom, très similaire au formulaire de profil utilisateur, nous utilisons un champ char, la longueur maximale est de 30.

Parce que le modèle utilisateur intégré, le champ first name a une longueur maximale de 30.

Encore une fois, rich required True, et dans ce widget est une entrée de texte, et nous passons à travers comme un attribut placeholder est votre prénom, nous faisons la même chose pour le nom de famille, sauf que nous changeons le placeholder, le nom d'utilisateur est en fait un champ email dans ce cas, donc lorsque quelqu'un s'inscrit, le nom d'utilisateur est un email plutôt qu'un simple nom d'utilisateur.

Et puis nous avons password one et password two.

Donc dans celui-ci, vous pouvez voir que nous passons en fait une classe également aux attributs car nous pouvons ensuite basculer entre une entrée de mot de passe et une entrée de texte.

Donc nous y voilà, nous ajoutons ensuite un champ token.

Donc celui-ci pour le token reCAPTCHA, il sera une entrée cachée, mais cela capturera le token lorsque nous traitons le formulaire en utilisant reCAPTCHA.

version trois, puis nous avons la classe meta models, user et les champs sont, comme vous pouvez le voir, ici, ils sont les mêmes que ce que nous avons au-dessus, puis nous avons votre formulaire, votre formulaire est un peu plus court avec un nom d'utilisateur et un mot de passe, un champ email, qui est une entrée de texte et un champ char avec une entrée de mot de passe.

Et encore une fois, en héritant du formulaire d'authentification, cela signifie que lorsque nous appelons form dot save, il fait toute la logique en arrière-plan, ce qui est fantastique.

Donc ce sont tous les formulaires, nous n'avons pas besoin de nous embêter avec eux.

C'est tout pour ce projet.

Nous n'avons pas besoin de plus de formulaires que cela, Figes, ouvrez cela.

La prochaine chose que nous devons vraiment faire est de créer les mixins.

Donc allons-y et faisons cela.

Et nous les ajouterons au répertoire principal dans un nouveau fichier.

Et nous l'enregistrerons sous le nom de mixings dot p y.

Encore une fois, je vais le prendre directement de mon autre écran ici.

Et coller.

D'accord, il y en a quelques-uns, l'un d'eux s'appelle directions, c'est une fonction que nous allons utiliser pour faire des appels API.

Donc ceux-ci sont assez importants.

Donc nous allons les passer en revue, nous apportons quelques éléments, l'un d'eux est un bien de l'UE, cela vient de URL lib dot pass où nous importons URL encode, cela est pour une fonction de redirection de God, que je vais expliquer dans une seconde.

Mais vous pouvez voir que nous importons requests, car nous allons faire un appel API.

Et quelques autres éléments, Jason daytime, format, timespan pour l'API Directions, et aussi JSON response, car nous faisons un mixin.

Pour Ajax.

Donc c'est la fonction form errors.

Maintenant, j'utilise ce genre de défaut que j'utilise lorsque je traite des formulaires.

Donc si je surcharge jamais la méthode form valid, et s'il y a une erreur, alors nous appelons form errors.

Et cela retourne essentiellement une chaîne de toutes les erreurs que vous pouvez transmettre au frontend, ce qui est assez pratique avec Ajax.

Le suivant est une fonction appelée reCAPTCHA.

validation.

Et nous transmettons le token, c'est l'appel API à recapture.

Donc le token est transmis depuis le frontend dans la vue.

Et nous créons une variable appelée results.

Et nous faisons une requête POST à cette URL.

D'accord, donc c'est google.com reCAPTCHA, API site verify.

Et puis nous créons un dictionnaire de données.

Et dans ce dictionnaire, nous transmettons le secret en tant que mot-clé.

Et c'est la clé privée recapture que nous avons dans nos paramètres.

Et aussi la réponse, nous transmettons un token.

C'est l'appel API, c'est très, très facile.

Et puis nous retournons result dot Jason.

Donc nous avons juste notifié la réponse.

Et c'est ce que nous utilisons lorsque nous créons des vues et quelques minutes.

C'est une fonction géniale.

Donc ce que cela fait, c'est qu'il utilise l'URL dans le code.

Mais si vous transmettez des paramètres, et l'URL à cette fonction, elle retourne essentiellement une chaîne qui peut être ajoutée à une URL, et la chaîne ressemblera à quelque chose comme couleur égale bleu.

Et taille égale grande, d'accord, et cette chaîne de paramètres peut aller, vous pouvez avoir toute une gamme de paramètres différents là-dedans.

Mais cela signifie simplement qu'elle peut être ajoutée à une URL, et ensuite lorsque vous êtes redirigé vers cette URL, vous pouvez faire quelque chose avec ces paramètres en utilisant request dot get dot get.

Et nous utilisons en fait cela dans cette application.

Donc c'est une petite fonction géniale que nous utilisons.

Donc c'est le mixin AJAX, j'ai obtenu cela, c'est une sorte de mixin par défaut que nous utilisons, bien que je surcharge souvent la fonction form valid.

Mais je l'ai écrit pour un appel AJAX, donc nous pouvons Ajax ou cinq soumissions de formulaire.

Cela signifie que sur un frontend, le HTML n'a pas besoin de se recharger.

Donc vous soumettez le formulaire, vous obtenez la réponse, et ensuite vous faites quelque chose avec.

Et vous pouvez changer des morceaux en utilisant JavaScript.

Donc j'ai cela comme un moyen de Ajax de fire dans les formulaires Django.

Donc nous avons la méthode form invalid, et nous avons form valid.

Et les deux retournent des réponses JSON aux vues que nous allons utiliser.

Enfin, nous avons la fonction directions, en passant par arcs et mots-clés.

Ensuite, nous avons tout un tas de variables ici.

Donc à partir des mots-clés, nous obtenons lat, a long a et tout un tas d'autres longitudes et latitudes.

Donc lat a et long a, c'est notre origine.

Donc c'est là que nous commençons en termes de points de passage.

B est là où nous arrivons, donc c'est notre destination.

Et ensuite nous avons C et D.

Ce sont les points de passage, j'ai limité cela à deux points de passage.

Donc au total, vous avez quatre destinations différentes.

Mais il n'y a aucune raison pour que vous ne puissiez pas en avoir plus, juste dans cette application, nous en avons deux.

Donc nous avons un départ, deux points de passage et une destination.

Et ces trois variables utilisent f string pour créer des chaînes à partir de ces variables ici.

Donc que l'origine ressemblera à quelque chose comme cinq 7.17 4.6.

Oui, ce serait la chaîne pour l'origine.

D'accord, même chose avec la destination.

Mais avec le point de passage, vous pouvez voir que nous nous connectons avec une barre, puis nous utilisons requests dot get.

Donc c'est une requête get.

Et nous sauvegardons cela dans une variable de résultats.

Donc nous faisons une requête get à cette URL.

Et ensuite nous passons pour un dictionnaire de paramètres.

Nous passons par l'origine, le mot de passe de destination, et les points de passage.

Et enfin, la clé.

Donc c'est la clé API Google que nous avons regardée dans la première section.

D'accord, directions, cela essaie simplement de trouver les résultats et de les sauvegarder dans une nouvelle variable.

Si directions a un statut de OK, alors nous travaillons à travers cette logique ici.

Et ensuite nous retournerons tout cela, donc il retourne l'origine, donc l'origine est en fait en dehors de l'instruction if.

Donc il les retourne quoi qu'il arrive.

Donc si c'est OK, nous cherchons les mots-clés roots et legs dans le fichier Jason.

Nous n'allons pas passer par cela pour l'instant.

Mais pendant cela, l'un des sections, je pourrais vous montrer à quoi ressemble la réponse JSON.

Ensuite, nous stipulons une distance, une durée et une liste de routes ici.

Et ensuite nous parcourons toutes les jambes.

Et nous continuons à ajouter et à ajouter et à ajouter la distance, la même durée.

Et c'est ce que nous transmettons à l'instruction de retour ici, la durée ici, vous pouvez voir en fait, que nous utilisons format timespan pour reformater la durée en quelque chose que nous pouvons réellement faire.

D'accord, donc c'est tout ce qu'ils sont, tous les mixins.

Nous n'avons pas besoin de les examiner en détail, mais nous allons les utiliser dans les vues.

Donc si nous retournons aux utilisateurs dans les vues, si je copie maintenant toutes mes vues.

Donc nous avons quelques vues ici, laissez-moi les minimiser pour les rendre un peu plus faciles à regarder.

Comme je le dis, j'ai quelques vues basées sur des classes.

Et j'ai quelques vues basées sur des fonctions.

Ce sont des vues basées sur des classes.

Celle-ci hérite de template view, vous avez sign up view qui est aussi une vue basée sur des classes.

Et nous utilisons form view avec le mixin AJAX.

Même chose pour sign in, sign out, c'est juste une vue basée sur une fonction, et c'est aussi profile view.

Donc c'est un mélange vraiment varié.

Et espérons que vous pouvez comprendre la logique différente.

Nous apportons tout un tas de morceaux de Django.

Donc nous avons render redirect, reverse, nous utilisons le décorateur login required.

Donc cela empêche les personnes qui n'ont pas été authentifiées de voir certaines choses dans les vues, import bringing in user le modèle utilisateur intégré.

Nous utilisons ensuite login, logout on authenticate, ceux-ci sont fantastiques.

Ils font tout le travail lourd avec l'authentification des utilisateurs.

Nous apportons settings, settings, JSON response.

Et ensuite ce sont les vues génériques intégrées.

Nous avons form view, template view.

Et enfin, parce que nous utilisons login required sur une vue basée sur une classe, nous devons apporter method decorator, nous apportons ensuite ce qui est le mauvais nom, cela doit être tutorial.

Nous apportons maintenant les mixins que nous venons de construire, et les formulaires.

D'accord, donc commençons rapidement avec account view.

C'est la vue d'accueil qu'elle sera.

Et elle hérite de la template view.

Donc c'est une vue de template de classe, nous devons appeler le nom de template ou créer une variable de nom de template et stipuler exactement où se trouve ce que nous allons rendre cette vue.

Et ce sera dans les utilisateurs compte que HTML, nous n'avons pas encore créé ce fichier HTML, mais nous le ferons dans la prochaine vidéo.

Puis dans le prochain segment, ce que nous faisons, nous surchargeons la méthode dispatch en utilisant le décorateur de méthode et en passant par login required.

Donc par ce petit morceau ici, les trois lignes de code ici, ce que cela fera, c'est empêcher quiconque n'ayant pas été authentifié de voir cette vue.

Et s'ils n'ont pas été authentifiés, parce que nous avons cela dans view settings.py.

Donc nous avons log, login redirect URL, désolé, l'URL de login, elle sera lue, l'utilisateur sera redirigé vers cette URL.

Donc si quelqu'un va à account et qu'il n'est pas connecté, il sera redirigé vers sign in lorsqu'il se connecte et que cela fonctionne, il sera redirigé vers account.

D'accord, donc c'est ainsi que cela fonctionne.

Donc c'est la vue account.

Nous avons ensuite profile view, qui est une vue basée sur une fonction, ce que nous faisons, nous créons quelques variables, nous avons user et user profile depuis request.

Le formulaire est le formulaire de profil utilisateur, et nous avons mot de passe instance equals user profile.

Ces deux ici, je vais les supprimer et je vais les ajouter en haut de l'écran, donc ils sont un peu globaux.

Et nous allons les mettre en majuscules.

Donc ce sont les messages par défaut et les résultats parce que nous sommes Ajax refine les formulaires.

Donc cela sera mot de passe, si jamais il y a une erreur, et cela sera montré sur un frontend.

Donc comme nous utilisons un Ajax pour soumettre le formulaire, nous avons f request.is.

ajax, puis nous faisons autre chose.

C'est une requête get.

Et ensuite nous passons par contexte, un dictionnaire de contexte.

Donc nous avons form, qui est un formulaire de profil utilisateur.

Et ensuite nous ajoutons quelques mots-clés.

Le premier est Google API key, et le second est based country depuis settings, d'accord.

Et ensuite nous retournons render le fichier HTML de profil, et nous passons par le dictionnaire de contexte.

C'est ainsi que vous passez le contexte dans une vue basée sur une fonction, légèrement différent dans une vue basée sur une classe, mais j'en viendrai à cela dans une seconde.

Mais si c'est Ajax, alors le formulaire est un formulaire de profil utilisateur, et les données sont égales aux données post du request.

Et l'instance est user profile.

Si le formulaire est valide, vous sauvegardez le formulaire.

Et vous vous souvenez, lorsque j'ai dit que nous allions ajouter lorsque nous ajoutons un profil, nous basculons ensuite le champ Hasbro profile à vrai.

Donc c'est ce que nous faisons là.

Donc une fois que nous avons ajouté l'adresse et la longitude latitude, nous sauvegardons ensuite has profile est vrai, et nous sauvegardons l'objet à nouveau, nous passons par Success, le message est votre profil a été mis à jour.

Si elsif n'est pas valide, nous appelons la fonction form error que nous avons créée il y a un instant.

Ensuite, nous créons un dictionnaire de données, result equals result et le mot-clé message est message, nous le passons en arrière vers le frontend en tant que réponse JSON, en passant par les données, tour d'arrêt du profil, mais c'est essentiellement comment nous sommes gérés dans la configuration d'un profil contre un compte.

Ensuite, nous avons une vue de sign up.

Regardez, nous avons le mixin Ajax, laissez-moi simplement amener cela un peu, mais le mixin AJAX.

Et nous avons aussi le form view.

Donc en tant que form view, vous devez dire quel est le template que nous devons rendre, qui est un sign up HTML.

La classe de formulaire est le formulaire utilisateur que nous avons construit il y a un instant, et une URL de succès peut être simplement une barre oblique, nous utilisons Ajax pour soumettre le formulaire.

Et selon la réponse que nous obtenons du backend, nous redirigerons ou non.

Donc nous n'utiliserons pas l'URL de succès, en fait, mais vous en avez besoin parce que nous utilisons form view.

Encore une fois, nous n'en avons pas besoin, je l'ai déjà en haut de l'écran, puis ce que nous avons, c'est recapture.

Donc vous vous souvenez, j'ai dit que nous regardions, nous avons un mot de passe de contexte et une fonction de vue basée sur une fonction comme celle-ci.

Oui, en tant que dictionnaire, dans une vue basée sur une classe, vous devez appeler la méthode get context data.

Et ensuite, une fois que vous avez appelé cela, vous pouvez alors ajouter un mot-clé au contexte et retourner le contexte.

Donc nous ajoutons recapture psyching au contexte, et c'est la clé dans les paramètres.

Et ensuite nous surchargeons le form valid, la méthode form valid dans le mixin AJAX.

Et nous faisons cela parce que nous avons besoin d'une nouvelle logique ici, parce que nous traitons avec recapture.

Donc nous, nous appelons cela si self dot request est Ajax.

Donc si c'est un appel AJAX, alors ce que nous faisons, c'est que nous obtenons le token à partir des données nettoyées du formulaire.

Donc c'est l'entrée cachée que nous avions dans le formulaire, puis nous appelons la fonction de validation recapture que nous avons créée dans les mixins.

Et nous passons ce token, d'accord.

Donc selon la réponse, si c'est un succès, alors nous inscrivons cet utilisateur.

D'accord, donc nous sauvegardons le formulaire, vous vous souvenez, le formulaire a le formulaire de création d'utilisateur, qui fait tout le travail lourd, comme je le dis, donc nous devons simplement sauvegarder le formulaire et il crée cet utilisateur et ce profil utilisateur avec un signal, nous sauvegardons l'email.

Donc nous sauvegardons le nom d'utilisateur dans le champ email, car nous utilisons un email comme nom d'utilisateur, et nous sauvegardons le profil, l'objet, puis, nous avons utilisé un profil, nous sauvegardons le score de capture dans le champ de score de capture du profil utilisateur, et ensuite nous sauvegardons le profil utilisateur.

Donc c'est ce que nous faisons.

Enfin, nous appelons login.

D'accord, donc nous nous sommes connectés, vous passez la demande, nous passons l'objet, qui est le modèle utilisateur de construction.

Et ensuite cela n'est pas nécessaire.

Si vous utilisez quelque chose comme all off où vous avez plusieurs backends, alors vous devez stipuler quel backend vous utilisez.

Mais vous pouvez l'avoir là de toute façon, cela n'a pas vraiment d'importance.

Le résultat est un succès.

Et les messages, merci de vous être inscrit, nous créons un dictionnaire de données et nous le passons par une réponse JSON.

D'accord, donc c'est la vue de sign up.

Sign in view, encore une fois, Ajax form view, form view, encore une fois, nous faisons toute cette logique, comme nous l'avons fait ci-dessus, c'est juste un peu différent parce que les modèles sont légèrement différents.

Nous n'avons pas besoin de passer un contexte.

Mais nous devons surcharger le form valid.

Donc encore une fois, très similaire à ci-dessus, juste nous avons le nom d'utilisateur et un mot de passe.

Et ce que nous devons faire est d'appeler user equals authenticate.

Et ensuite nous authentifions cet utilisateur, si user n'est pas none, nous les connectons.

D'accord.

Et si ce n'est pas le cas, nous appelons alors une erreur de formulaire.

Donc nous n'avons pas nécessairement besoin de cela parce que nous utilisons le formulaire d'authentification.

Mais parce que nous appelons également le formulaire de zone, je l'ai simplement laissé là, c'est probablement superflu aux exigences pour être franc, mais c'est la vue de sign in.

Et enfin, nous avons une vue de sign up, qui est une vue basée sur une fonction.

Et tout ce qu'elle fait, c'est de se déconnecter et de mettre, et nous passons par votre demande.

Et ensuite, une fois déconnecté, vous êtes redirigé vers la page de connexion.

Ce sont nos vues.

J'essaie de passer en revue celles-ci, mais d'être aussi détaillé que possible.

Donc vous comprenez réellement la logique de ce que j'ai fait ici.

Comme je le dis, j'ai juste identifié dans la vue de sign in qu'elle n'a pas nécessairement besoin de ressembler à cela, vous pourriez techniquement, techniquement, vous pourriez simplement utiliser le mixin de formulaire AJAX et il sauvegardera le formulaire.

Mais l'une des principales raisons est que nous pouvons avoir ce message de succès parce que les mixins, si vous regardez sur le mixin ici, il n'y a pas de message, c'est très, très basique.

D'accord, ensuite les URLs.

À l'instant, nous n'avons rien là, mais ce que nous devons faire est de copier et coller tout cela.

Donc nous importons les vues que nous venons de créer, le nom de l'application est les utilisateurs et dans les Euro patterns, rappelez-vous, account est la page d'accueil.

Donc c'est une vue basée sur une classe.

Donc vous devez appeler la méthode as view.

Donc as views dot account, account view.as view, vous n'avez pas besoin de faire cela pour profile, car c'est une vue basée sur une fonction.

Mais normalement, et je ne sais pas pourquoi j'ai fait cela, mais nous allons profile underscore view, normalement, sur une vue basée sur une fonction, je fais cela et je pense que c'est la syntaxe normale.

Donc nous allons revenir dans view, ce qui signifie que sinon cela ne l'aimera pas.

Donc retour dans les URLs, et je vais sauvegarder cela.

Donc les vues de profil que profile view n'ont pas besoin d'appeler as view car c'est une vue basée sur une fonction et le nom est profile, nous avons sign up, sign in et sign out.

Ce sont deux, à la fois basés sur des classes et celui-ci est basé sur une fonction.

Donc c'est la syntaxe dont vous avez besoin.

D'accord.

Donc si c'est une vue basée sur une classe, vous appelez l'AZ view, c'est une vue basée sur une fonction, vous n'avez pas besoin de le faire, et ce sont nos URLs.

Et nous tirons déjà de ces URLs dans l'URL comp, avec cette ligne ici.

D'accord.

Je viens de remarquer que j'ai oublié quelque chose de fondamental.

Donc nous avons besoin d'un fichier signals py.

Donc Nouveau Fichier, Enregistrer sous, cela sera signals dot p y.

Et ce dont nous avons besoin ici, c'est tout cela.

Donc nous importons posts, save from signals, ils utilisent le modèle, nous avons besoin d'un décorateur de réception.

Et nous avons aussi besoin du profil utilisateur que nous avons créé dans les modèles.

Donc le décorateur de réception a besoin de post save et de l'expéditeur pour faire quoi que ce soit.

Donc l'expéditeur est l'utilisateur dans ce cas.

Donc ce que nous écoutons, c'est un signal du modèle utilisateur.

Et la fonction est create profile, nous passons par l'expéditeur, qui est l'utilisateur, l'instance de l'utilisateur créé et les arguments de mot-clé, si créé.

Donc si l'utilisateur est créé, nous créons alors un profil utilisateur.

Et l'utilisateur parce que c'est un champ one to one equals instance, d'accord, c'est ce que nous mettons dans les signaux.

Mais pour s'assurer que cela se déclenche réellement lorsque nous lançons le serveur local, nous devons aller dans les apps.

Et deaf, ready parser lui-même.

Et nous importons users dot signals.

Et c'est tout ce que nous devons faire.

Donc ces deux lignes de code seront responsables du lancement de ce signal.

D'accord.

Et maintenant nous devons nous concentrer sur l'application principale.

Donc si je vais ici, et que je regarde les URLs, nous faisons face, nous faisons les URLs en premier.

Donc main est juste responsable de deux URLs, l'une d'elles est root, c'est là que vous allez ajouter les différentes adresses pour vos directions.

Et lorsque vous complétez la quatrième direction, elle capte alors les quatre et vous redirige, vous redirige vers cette URL, qui est map.

D'accord.

Donc ensuite nous irons à View.

D'accord, donc nous regardons simplement render, redirect et reverse, nous importons settings.

Et c'est faux.

Les voilà.

Et nous avons juste besoin de directions.

Vous vous souvenez, que les mixins que nous avons créés plus tôt ? Eh bien, c'est ce que nous importons ici.

Et ensuite nous avons une vue basée sur une fonction, les deux sont des vues basées sur une fonction.

Donc def route, et nous créons un dictionnaire de contexte ici et nous le passons au fichier root HTML.

Vue très, très basique, elle ne fait pas grand-chose.

La plupart de cela ou la plupart du travail lourd sur cette vue sera fait en utilisant l'API et le JavaScript, que nous verrons dans la prochaine section.

Donc ensuite, la dernière vue que nous allons examiner aujourd'hui est map, c'est là que nous avons notre carte et nos directions d'itinéraire rendues.

Donc c'est la partie amusante.

Donc nous allons passer par tout un tas de paramètres.

Donc si vous vous souvenez dans notre mixin, si vous vous souvenez dans le mixin, nous avons ce que les paramètres de redirection seront responsables de la création d'une chaîne de paramètres qui sera passée à la vue principale et elle contiendra tous les mots-clés tels que lat, a long a lat, B Long Bay et ainsi de suite.

Nous savons que a et long a sont tous deux l'origine, le point de départ, B est la destination et C et D sont les points de passage, d'accord ? Nous savons cela parce que c'est ainsi que nous avons créé les directions, la fonction est également dans le mixin.

Donc nous disons que s'il y a un lat, a que B que C que D, alors faisons cet appel de directions, d'accord, sinon.

Donc si quelqu'un essaie de visiter les cartes sans ces chaînes de paramètres, il sera simplement redirigé vers la route principale.

Donc retournez à la route et dites le refaire.

D'accord, mais s'il y a un lot A, B, C, et D, il essaiera d'appeler les directions depuis le mixin.

Et il passe simplement par A, B, vous savez, et ainsi de suite.

D'accord.

Et c'est ce que nous avons intégré dans les mixins, si vous vous souvenez, les voilà.

Donc ce sont les arguments de mot-clé.

Donc c'est ce que nous passons depuis la vue, comme un lot, un lot, B, B, C, C, D, D, d'accord.

Et c'est le F, c'est le L.

Donc cela va rediriger.

Mais si cela ne redirige pas, alors cela créera un dictionnaire de contexte.

Il y a beaucoup de choses ici, nous passons par la clé API, le pays de base, le pays, tout cela est requis pour l'appel API que nous allons faire.

Et tout cela deviendra clair lorsque nous commencerons à écrire le JavaScript, passe par toutes les longitudes et latitudes, et ainsi de suite.

Plus, il passe par l'origine, la destination et les directions, car nous en avons besoin pour les rendre sur le fichier HTML, qui est map dot htm, l.

Donc ce sont toutes les vues, ce sont les URLs, les modèles, et ainsi de suite.

Cela nous laisse avec la création d'un répertoire de modèles.

Donc nous n'avons rien là.

Il y a quelques façons de faire cela.

Maintenant, si vous créez des applications réutilisables, c'est-à-dire ces applications que vous pouvez télécharger sur p IP, que d'autres personnes peuvent installer, alors il est probablement préférable pour vous d'avoir des modèles dans l'application elle-même.

Donc tout est contenu en un seul.

Mais comme nous ne faisons pas cela, vous n'avez pas besoin de le faire.

Donc tout ce que vous avez à faire est d'ajouter un répertoire ici dans le répertoire principal, qui sera un nouveau dossier.

Nous appellerons cela templates.

Et tout ce dont nous aurons besoin est un nouveau répertoire là pour les utilisateurs.

Et nous en aurons besoin d'un là pour Maine.

Donc lorsque nous référençons Maine slash map dot html, nous chercherons un fichier ici, si je sauvegarde cela sous le nom de map dot html, cette vue cherchera dans main format HTML.

Donc nous chercherons cela.

C'est ainsi que cela fonctionne.

La seule chose est que ce projet n'est pas configuré pour chercher des modèles dans ce répertoire, nous devons aller dans settings.py et lui dire où chercher.

Vous faites cela en allant dans les modèles, vous allez dans les does, et tout ce que vous avez à faire, parce que c'est dans le répertoire principal, vous devez mettre templates.

Et c'est tout.

D'accord, j'espère que cela a été un bon équilibre pour passer en revue tout cela.

Donc vous pouvez le parcourir rapidement, sans sauter certaines choses fondamentales.

Nous avons couvert beaucoup de terrain, nous avons commencé une nouvelle application utilisateur, nous avons construit un modèle, quelques formulaires de modèle et vues à partir des URLs, vous savez, nous avons reconfiguré les paramètres, l'URL comp, nous avons configuré les modèles, nous avons couvert beaucoup de terrain, mais en termes de backend en termes de Django, cette application est complète.

Elle ne fonctionnera pas.

Cependant, parce que nous n'avons rien, comme CSS, HTML, ou JavaScript.

C'est ce que nous allons examiner dans la prochaine section.

Mais une chose en fait, je viens de remarquer aussi que dans notre fichier settings.py, nous référençons un répertoire qui n'est pas là pour le statique.

Maintenant, c'est une correction facile.

Nouveau Dossier, et nous allons simplement l'appeler static.

Super.

C'est notre répertoire statique.

Et c'est à cela que cela fait référence.

D'accord, bien.

C'est la fin de cette section.

J'espère que vous l'avez appréciée.

Et j'ai hâte de passer en revue les prochains morceaux.

Merci.

Et au revoir.

Tout le monde, c'est probablement de décodé ici, et dans cette section, nous allons suivre là où nous nous sommes arrêtés dans la précédente où nous avons développé le backend de ce projet Django.

Dans cette section, nous allons jouer avec le frontend.

Donc nous allons créer des fichiers HTML, CSS, JavaScript, jQuery, Ajax et les API Google.

Donc c'est la partie amusante du projet en fait, car c'est là que toutes sortes de chaînes sont assemblées.

Donc sans plus attendre, passons directement à cela.

Si vous regardez sur l'écran ici, je suis ouvert sur les Doc's Django pour les balises de modèle.

J'ai créé une vidéo sur ma chaîne de décodage qui fait une plongée profonde sur les balises de modèle et les filtres.

Donc si vous voulez comprendre ce qu'ils sont, alors n'hésitez pas à regarder cela plutôt que de me faire passer par cette page.

Mais nous allons travailler avec beaucoup de balises de modèle aujourd'hui.

Donc lisez et regardez et ensuite revenez, je suppose.

Mais allez, sautez directement dans Sublime Text.

C'est le projet où nous nous sommes arrêtés.

Dans la dernière section, vous pouvez voir ici que nous avons créé un répertoire statique et un répertoire de modèles.

C'est ce que nous avons fait dans les deux ou trois dernières minutes de la dernière section.

C'est ce que nous avons fait.

Et nous avons main, les autres utilisateurs là.

Donc ce que nous allons faire maintenant, c'est créer le premier fichier HTML, et il doit être dans les modèles en tant que base.

Donc nouveau fichier, et nous l'appellerons Enregistrer sous base dot html.

D'accord, et je ne vais pas l'écrire à partir de zéro, car cela prendrait une éternité, je n'ai pas conçu cette application pour être basique, vous savez, elle a l'air assez bien en fait, elle fonctionne, vous pouvez la redimensionner, elle est réactive.

Donc il y a beaucoup de choses qui se passent.

Donc ce que je vais faire, je vais tout simplement copier, copier et coller tout cela.

Et je vais vous expliquer ce que je fais.

Déplaçons cela un peu par ici.

Donc tout d'abord, il y a une balise de modèle ici, qui dit load static.

C'est une balise de modèle qui nous permet d'accéder à nos fichiers statiques.

Maintenant, les fichiers statiques, comme configuré dans settings dot P, tandis que p y sont tous dans ce répertoire ici, comme nous sommes en développement.

Cependant, si nous étions en production, alors vous configureriez les fichiers statiques d'une manière légèrement différente, et peut-être les servirez-vous au projet via un bucket s3 ou quelque chose comme ça, ou des espaces digitalocean.

Donc cette balise de modèle load static nous permet d'accéder aux fichiers dans le répertoire statique, nous avons un peu de HTML ici, je ne vais pas faire de plongée profonde du tout.

Mais nous avons ceci est le main que tous ces liens ici, ce sont mes polices.

Donc nous utilisons Korea prymatt decoding, nous avons ensuite une feuille de style que nous référençons main dot CSS, nous allons jouer avec cela dans une seconde.

Donc cette partie ici appelle un CDN, essentiellement.

Et c'est pour toaster.

Donc nous allons utiliser des alertes toaster pour afficher les messages du backend.

Donc si vous vous souvenez, dans les vues, nous avons ce message, par défaut à il y avait une erreur.

Et le résultat est une erreur.

Eh bien, cela va montrer un message toaster rouge.

Si vous ne savez pas ce que c'est, si je retourne dans mon navigateur, j'ai des exemples de toaster ici.

Donc c'est un succès.

haut droit.

Mais nous pouvons avoir un bas droit, que je crois avoir dans ce projet, show toast, le voilà.

Et il peut, vous pouvez avoir ce que vous voulez là-dedans, vous pouvez test show toast, le voilà test.

D'accord, donc c'est ce que nous utilisons dans ce projet.

Retour dans le projet ici, retour dans la base.

Donc c'est le CSS qui est requis pour toaster et nous le mettons toujours dans la tête, vous avez ensuite block, extend head, donc nous utilisons une balise de modèle de bloc.

D'accord, donc cela nous permet d'étendre les scripts de tête qui sont sous la loi, donc j'ai quelques notes ici aussi.

body.

Donc nous avons ensuite nav, nous utilisons une balise include de modèle, nous n'avons même pas encore créé cela.

Donc je vais le faire maintenant rapidement.

Donc nouveau dossier, et celui-ci doit s'appeler partials.

Et dans partials, nous avons besoin d'un nouveau fichier appelé nav HTML.

D'accord, donc cela va maintenant être récupéré depuis celui-ci ici.

Retour à la base.

Et donc cette balise include de modèle, plutôt que d'avoir tout le code, cela sera dans nav HTML, utilisez l'inclusion qui interjecte cet élément HTML dedans, puis nous avons cette div.

Donc ne vous inquiétez pas trop de ceux-ci.

Les classes, je vais créer un peu de CSS, car je les ai nommées de manière spécifique pour qu'elles soient rendues joliment et aient l'air génial sur le frontend.

Si vous vous souvenez lorsque nous avons regardé la démo de l'application, elle a l'air assez bien, non ? Donc nous avons ensuite inclus partials logo, hate logo, HTML.

Donc créons cela.

Je ne peux pas parler aujourd'hui, créons cela rapidement.

Nouveau Fichier.

Plus, sauvegardez cela sous le nom de logo dot html.

Je vais amener ce code dans une seconde.

En tout cas, sauvegardez, et ensuite nous avons un bloc.

Donc ces blocs nous permettent d'étendre certaines parties de cette base.

Dans d'autres modèles, cela aura plus de sens dans une seconde.

Et il s'appelle content.

Donc nous avons block, extent head block content, et nous en avons un autre ici, extend footer.

Donc ce sont nos scripts de pied de page.

Donc tout d'abord, nous utilisons quelque chose appelé jQuery.

C'est une bibliothèque JavaScript, je crois, la plus populaire, et elle nous permet d'accéder à des choses comme Ajax, donc nous pouvons faire une soumission de formulaire asynchrone, par exemple, nous soumettons le formulaire et nous obtenons la réponse et rien ne se recharge sur la page HTML.

Tout est fait de manière asynchrone.

Donc c'est pourquoi nous avons besoin de jQuery.

Mais vous pouvez obtenir ce code depuis code.jquery.com.

Et vous obtenez la version la plus récente.

Ensuite, nous avons le JavaScript de toaster, qui est tout cela, vous pouvez obtenir visiter ce CDN JS calm et obtenir la dernière version depuis là, puis nous avons un bloc pour étendre le pied de page, encore une fois, il nous permet d'étendre cette partie de ce HTML dans un autre document.

Et enfin, nous référençons main dot j s.

Donc il y a deux fichiers dans static dont nous avons besoin.

Donc nouveau fichier, et nous l'enregistrerons sous le nom de main dot j, s, ce sera un fichier JavaScript, enregistrer sous, et nous l'appellerons main, non, nous n'étions pas.

Nouveau Fichier.

Enregistrer sous, cela sera main dot CSS.

Donc nous y voilà, nous avons maintenant le CSS principal et le JavaScript principal, donc nous les référençons dans base HTML.

Donc même si nous n'avions rien à payer, ces fichiers, nous ne rencontrerons aucune erreur.

Et ensuite nous fermons le body dans HTML.

Donc c'est base HTML, nous n'avons pas besoin de faire autre chose dans ce fichier, tout ce que nous devons faire maintenant est de créer les documents qui étendront ces blocs.

D'accord, donc le premier que nous allons examiner est l'index ou dans ce cas, il sera account, qui est dans users.

Donc créez un nouveau fichier.

Comme nous sauvegardons, nous l'appellerons count, dot html, en fait, nous avons besoin d'un autre ici appelé profile, sauvegardez sous un autre ici appelé sign in as underscore, sauvegardez sous un autre appelé sign out.

Et pendant que j'y suis, je vais aussi faire la carte.

Donc les modèles sont globalement pour obtenir la carte et nous allons route safe, bien, cela peut fermer certains de ceux-ci, j'en ai trop en haut.

C'est une très mauvaise habitude que j'ai.

Les voilà.

Bien.

Donc ensuite, ce que nous allons faire, nous allons regarder account.

D'accord, donc c'est notre page d'accueil.

Donc je vais copier.

Et je vais coller cela.

Donc étend le base dot html.

Donc c'est l'extension de cela, d'accord, comme une autre balise de modèle que Django a load static.

D'accord, donc nous avons maintenant accès à static à nouveau, nous ne l'ajoutons pas, cela n'a pas nécessairement besoin d'être là, mais cela ne fait de mal à personne.

Donc nous allons l'ajouter si je voulais ajouter un script là, par exemple.

Oui, donc avec ADD script, vous pourriez alors ajouter quelque chose là.

Mais nous ne le faisons pas, donc nous ne le ferons pas.

Mais c'est un bloc de contenu.

Donc c'est le contenu qui sera injecté, si vous voulez, dans cette section ici.

D'accord, donc block content.

Donc block content, block content, d'accord.

Donc nous sauvegardons simplement cela.

Donc nous avons une balise h3, comme vous le savez, c'est un cours Django Google API.

Et c'est le compte utilisateur.

Et ensuite nous avons une div, qui est un conteneur.

Donc nous allons référencer ces classes dans le CSS, mais je ne vais pas m'attarder trop sur le CSS.

Cela concerne davantage les API et JavaScript.

Donc nous allons faire cela rapidement dans une seconde.

Ensuite, nous avons des balises h4, donc les détails du compte utilisateur, et ensuite nous avons un tableau, d'accord.

Et dans ce tableau, nous avons un en-tête de tableau, il a une tête, et ensuite une case vide, désolé, un champ et ensuite un champ vide.

Donc il n'y a pas d'en-tête là du tout.

Maintenant, nous avons un corps de tableau, et ensuite pour chaque ligne, donc nous avons le nom d'utilisateur, request dot user, dot username.

Donc Django utilise quelque chose appelé context processes qui passe toujours par request à HTML, donc vous pouvez toujours accéder à request.

Par conséquent, vous pouvez toujours accéder à request dot user.

Et des champs tels que user dot user name, vous pouvez accéder à des choses comme dans notre cas, ce sera request dot user dot user profile dot address, des choses comme ça, faire des requêtes telles que si request.user.is authenticated.

Donc c'est vraiment très pratique que ce contexte processor soit utilisé plus que tout autre chose.

La ligne suivante, nous avons le nom.

Et ensuite nous avons donc nous utilisons un filtre.

Donc c'est un filtre de modèle, request dot user dot first name, title.

Donc cela mettra une lettre majuscule au début du nom et ensuite un espace last name.

Donc first name, last name.

Et ensuite nous faisons une instruction if ici.

Donc un if else.

Donc si request dot user dot user profile dot has profile.

Donc s'ils ont ajouté une adresse, affichez ceci, qui est une ligne de tableau, détails de notre adresse, puis je montrerai l'adresse, la ville, le comté, le code postal, sinon.

Donc s'ils ne l'ont pas, donc s'ils viennent de s'inscrire, cela leur montrera un profil, et il aura une balise a avec un href et un lien.

Donc nous utilisons une balise a URL de modèle pour le profil de l'utilisateur.

Donc ce serait simplement un hyperlien où ils peuvent cliquer dessus, et cela les emmènera au profil, afin qu'ils puissent ensuite sélectionner cette adresse.

Donc c'est pourquoi j'ai ce has profile dans un champ sur le modèle de profil utilisateur.

C'est tout.

C'est tout ce qui se passe dans account.

Pas grand-chose d'autre.

Donc développons le profil.

Coller et sauvegarder un peu plus dans ce Gannett étend la base appelée load static.

Maintenant, nous avons le block content.

Donc encore une fois, c'est le block, puis nous avons extend footer.

Donc si nous nous souvenons dans la base, nous avons cette extension, cette extension footer ici.

Le main j s est toujours le dernier JavaScript que nous chargeons, c'est juste la façon dont je le fais.

Cela signifie que tout ce qui est au-dessus de cela, je peux le référencer.

Donc je peux définitivement savoir que tout Ajax que j'écris dans main dot j.

s, cela fonctionnera parce que jQuery est chargé en premier, d'accord.

Et un block étend footer.

Tout cela est chargé avant mon jour.

Donc je peux en fait référencer toutes les variables qui sont énoncées dans le block étend footer.

Donc dans le profil, nous avons extend footer.

Et ensuite nous avons un script.

Donc c'est un script JavaScript.

Et nous créons deux variables.

Une variable est Google API key.

Si vous vous souvenez, nous passons cela.

Permettez-moi de vous rappeler profile view.

Dans le contexte, nous passons Google API key et base country à travers le contexte.

C'est ainsi que nous y accédions ici.

D'accord.

Donc nous allons créer une variable JavaScript.

Donc nous pouvons y accéder dans le fichier main j.

s.

Nous l'appelons Google API key.

Et nous utilisons le filtre safe.

Donc cela créera simplement une chaîne de cette clé API.

Même chose pour base country, le script suivant est un fichier appelé Google Places, dot j.

s.

Nous ne l'avons pas encore.

Donc nous allons le créer maintenant.

Donc c'est Google Places.

Enregistrer sous API dot j.

s.

Super.

Retour dans le profil.

Donc cela référence maintenant un fichier qui est là, cela fonctionnera.

Aller dans les conteneurs, ce sont les principaux morceaux et morceaux.

Donc nous avons une instruction if ici avec un else donc si la request dot user dot user profile a un profil, montrer tout cela sinon, ajouter une adresse, d'accord ? Et si cas donc nous avons, et si je vais bien, j'essaie juste de comprendre ce que j'ai fait ici.

Donc c'est l'entrée de l'adresse Google, non ? D'accord.

Donc ici, c'est l'entrée principale pour l'API Google Places.

Donc cette entrée ici est l'entrée où l'utilisateur commence à taper une adresse.

Et l'API Google prédit ce qu'ils essaient de taper.

Et ensuite elle retourne l'adresse, ils la sélectionnent, lorsqu'ils la sélectionnent, elle remplit alors toutes ces entrées ici, que je vais vous montrer ce que je fais dans une seconde, laissez-moi juste couvrir cela d'abord.

Donc s'ils ont un profil, il affichera le profil.

D'accord, donc il affichera l'adresse, et ensuite il aura un changement d'adresse.

Et ensuite il aura ou sinon il aura ajouter une adresse.

Donc si cela change l'adresse, vous pouvez alors changer l'adresse pour la nouvelle, vous taperez dans une adresse, vous la sélectionnez, elle changera.

Si ce n'est pas le cas, vous ajoutez simplement une adresse.

Donc c'est l'entrée principale que vous voyez ici, nous avons le nom Google address, l'ID est ID Google address, nous allons les référencer dans l'API Google a Places, juste pour référence, puis nous avons un formulaire.

Et ensuite c'est la fin de cela, vraiment.

Donc nous allons regarder ce formulaire.

Donc l'idée est profile form, nous allons créer un appel AJAX en utilisant jQuery sur celui-ci.

Donc c'est le nom que nous allons référencer profile form.

La méthode est post et l'action est pour slash profile.

Donc c'est essentiellement l'URL vers laquelle nous allons envoyer l'appel AJAX, qui est, si nous regardons dans les URLs, ici.

Donc comme le profil est le nom, et cela est assigné à views dot profile view.

Oh, d'accord, donc regardons le formulaire.

Donc comme c'est un formulaire, nous devons utiliser une autre balise de modèle et cela ajoutera une entrée cachée avec un jeton CSRF.

Donc le jeton CSRF signifie cross site request forgery token et c'est un jeton appliqué aux formulaires lorsque vous soumettez le formulaire.

Il sait que c'est vous qui le faites et pas un vaurien qui le fait depuis ailleurs.

Et ce que nous faisons ensuite, c'est que nous créons ces étiquettes.

Donc l'adresse est en fait maintenant, celles-ci sont cachées, non ? Donc cette classe est hidden L.

Et elle est cachée.

D'accord.

Et la raison pour laquelle nous faisons cela est que dans le JavaScript dans le main j s, nous écrivons une fonction pour afficher ces éléments cachés lorsque nous sélectionnons une adresse, et c'est pourquoi nous le faisons.

Donc l'étiquette elle-même est cachée, classe hidden L, et est cachée.

Et form dot address, si vous vous souvenez, c'est une entrée cachée.

Donc nous avons des formes d'entrée cachée, désolé, entrée cachée.

Donc tous ceux-ci sont cachés.

Donc ils seront rendus comme des entrées cachées ici, comme l'est l'étiquette.

Donc l'étiquette et l'entrée sont cachées, puis vous avez la ville, le comté, le code postal, le pays, la longitude, la latitude, aucun de ceux-ci ne sera affiché jusqu'à ce que l'utilisateur sélectionne l'adresse.

Et ensuite nous avons une fonction JavaScript qui démasquera tous ces éléments, le bouton pour soumettre est désactivé.

Donc vous ne pouvez pas soumettre le formulaire jusqu'à ce qu'une adresse ait été sélectionnée.

Et nous ajoutons un ID à ce bouton de profil, car nous l'avons référencé et nous cliquons dessus programmatiquement lorsque l'adresse a été sélectionnée.

D'accord, donc c'est le profil HTML.

Ensuite, regardons sign in a gay et laissez-moi prendre mes notes.

Et sign in.

Copier à travers.

Coller étend la base, même que nous chargeons le statique, toujours le même, puis nous avons le block content.

D'accord, pas grand-chose d'autre dans celui-ci.

Mais nous avons une balise h3, et ensuite nous avons deux conteneurs ici.

Donc c'est, encore une fois, c'est un formulaire.

Oui, donc contre CSRF CSRF token, l'ID sign in form, post sign in.

D'accord, donc j'ai l'ID, la méthode et l'action, toujours dans le formulaire en tant qu'attributs.

De cette façon, lorsque nous faisons l'appel dans le JavaScript, c'est beaucoup plus facile de comprendre ce qui se passe.

Label encore, donc nous créons un label.

La différence est que celui-ci n'est pas caché dans le formulaire dot username, car nous utilisons dans une vue de formulaire, vous accédez au formulaire à partir de l'objet de formulaire, donc c'est form dot username, et comme l'entrée.

Donc si vous regardez les formulaires, username, password, fields, username, password, c'est ainsi que nous référençons le numéro dans le cas de sign in, c'est pourquoi nous avons form dot username, form dot password, puis nous avons label.

Donc c'est show password.

Donc si vous vous souvenez dans les formulaires, nous avons une classe.

Permettez-moi de vous montrer.

Classe password.

D'accord.

Donc ce que je fais dans signing, c'est on click, donc c'est une petite case à cocher, non ?

Donc le CSS la rendra jolie, mais essentiellement, c'est une case à cocher.

Donc si elle n'est pas cochée, ce sera une entrée de mot de passe.

Mais lorsqu'ils cliquent dessus, elle devient cochée pour commencer.

Et elle appelle une fonction appelée show password ou show p word.

Maintenant, cette fonction, je vais l'écrire dans le fichier JavaScript principal, et elle basculera essentiellement cette entrée de mot de passe en une entrée de texte.

Donc vous pouvez en fait voir le mot de passe, d'accord, ce qui est assez standard sur les sites web.

Et ensuite un bouton est submit et sign in.

D'accord, facile et simple.

Le suivant, sign out.

Désolé, sign up.

Maintenant, cela devrait être sign up, nous le savons.

Les voilà.

Sign up.

Donc nous allons copier et nous allons coller.

Comme nous avons plus de choses dans celui-ci.

Donc en étendant le fichier base HTML, et nous chargeons le statique, des trucs standard gratuits.

Et celui-ci, nous étendons la tête, nous y reviendrons dans une seconde.

Nous avons un block tank, nous avons un formulaire.

Et nous étendons le pied de page.

Donc si vous vous souvenez, dans la vue de sign up, nous jouons avec les contacts en utilisant la méthode get context data.

Et nous passons trois recapture site key, d'accord, qui est la clé publique de recapture.

Et nous créons une variable recapture site key que nous pouvons référencer dans le JavaScript que nous n'avons pas encore écrit.

D'accord.

Le formulaire est assez standard, similaire à ce que nous venons de faire, CSRF token.

Ensuite, nous avons le prénom, le nom de famille, le nom d'utilisateur, le mot de passe un, le mot de passe deux différences.

Nous avons token dans celui-ci.

Donc le token, si vous vous souvenez dans les formulaires, nous l'avons ajouté comme une entrée cachée, et c'est ainsi que nous allons gérer le token reCAPTCHA.

D'accord, donc c'est une entrée cachée, vous ne verrez pas cela lorsqu'elle est rendue.

Ensuite, nous avons cette petite case à cocher pour afficher le mot de passe à nouveau et un bouton de soumission d'inscription.

D'accord, donc c'est le formulaire.

Et ce que nous avons en haut ici, c'est un script.

Donc la source est l'URL https google.com reCAPTCHA.

api.js JavaScript.

Donc c'est le JavaScript que nous tirons directement de Google.

Et nous passons par le, notre reCAPTCHA.

psyche.

Donc c'est ainsi qu'il sait que c'est nous qui faisons l'appel à recapture.

Parce que le psyche que nous avons configuré lorsque nous avons configuré recapture dans la première section, nous le lions à cette clé API.

Donc et c'est l'appel JavaScript en tant que script que nous mettons dans l'extend head.

Donc essentiellement, ce script, étant dans cet extend head est l'équivalent de se trouver dans, eh bien, il sera là mais sans la tête.

Donc imaginez, imaginez cela, d'accord, donc c'est ce que nous faisons en ajoutant cela à l'extend head.

Donc c'est le JavaScript, tant que le contenu est heureux.

C'est la page de signup.

Donc maintenant, regardons la carte principale.

En fait, regardons les parcelles rapidement.

Copier les parcelles.

D'accord, donc c'est le logo.

Donc c'est essentiellement une balise a.

Et si je sauvegarde cela, donc si vous cliquez sur le logo, cela vous emmène au compte utilisateur, qui est la page d'accueil, et il référence, je pense que c'est la première fois que vous voyez cela dans ce tutoriel, load static.

Donc c'est ainsi que vous référencez le statique.

Lorsque vous chargez le statique, vous pouvez ensuite utiliser la balise de modèle statique.

Si vous ne l'aviez pas chargé, cela ne fonctionnerait pas.

Et nous cherchons dans le branding.

Donc dans le statique, nouveau dossier, branding, et il essaie de trouver un GIF, qui est un dead logo GIF, nous allons l'ajouter dans une seconde, ce qui ne posera aucun problème.

Et ensuite nous allons ajouter le Nef, il y a beaucoup d'instructions if dans celui-ci.

Rien de trop fantaisiste pour être franc, il y a une instruction if else.

Donc si la request dot user est authentifiée, donc s'ils sont connectés, ils verront ceci maintenant.

S'ils ne le sont pas, ils verront cette nav, d'accord.

Donc regardez si, donc lorsque vous entrez sur le site pour la première fois, si vous n'êtes pas connecté, vous ajouterez si le chemin de connexion.

Donc si l'URL est sign in, alors cela sign in sera actif.

D'accord.

Donc sur le côté maintenant, il y aura une lueur violette, si ce n'est pas le cas, il sera vide.

Si c'est sign up, il y aura une lueur violette, si ce n'est pas le cas, il sera vide, c'est ce que font ces instructions if, c'est juste pour montrer si c'est actif ou non.

S'ils sont authentifiés, et que le chemin de la requête est égal à la barre oblique, qui est la page d'accueil.

Encore une fois, actif si ce n'est pas le cas, même chose pour le profil, la route, la carte.

D'accord, donc il montre simplement différentes navigations.

Pour être franc, fermons cela.

Fermons cela.

Fermons sign up, sign in profile et account ou gardons la base ouverte.

Nous allons fermer cela.

Et maintenant nous allons faire map.

Donc copier.

C'est la carte ou coller cela, il y a beaucoup plus de choses ici.

Enregistrer.

D'accord, donc map étend le base HTML load static.

Dans celui-ci.

Encore une fois, nous passons par recapture.

Donc recapture site key, d'accord.

Et pour être franc, nous n'en avons probablement pas besoin, c'est probablement un vestige, mais je le laisse là.

Parce que nous ne faisons pas d'appel reCAPTCHA dans map.

Nous ne le faisons que dans, sign up.

D'accord, donc nous avons ensuite une balise h3, et nous avons un conteneur.

Donc qu'est-ce qui se passe ici ? Nous avons, je vais, vous savez quoi ? Laissez-moi faire root first.

Nasty read first.

D'accord, c'est root.

Oui.

Donc root est l'URL où nous ajoutons la longitude et la latitude pour l'origine, les points de passage et la destination.

Et map est ce qui est rendu, c'est le dernier point dans le temps, en fait, donc laissez-moi regarder rapidement.

Donc je viens de coller tout cela, cela étend la base, charge le statique.

Et ensuite, encore une fois, nous avons recapture.

Nous n'en avons pas besoin.

Je suis sûr que je peux le supprimer.

Mais je ne vais pas le faire parce que je ne l'ai pas testé.

Et je sais que cela fonctionne dans l'autre projet.

Mais nous ne faisons pas techniquement un appel recapture.

Donc je suis, vous savez ce que je veux dire, cela n'a pas besoin d'être.

D'accord, puis nous avons la balise h3, et ensuite nous avons les entrées.

Donc c'est la même chose que le compte, pas de profil.

Donc dans le profil, si vous vous souvenez, nous avons cette entrée ici.

Et nous l'appelons ID Google address, la différence ici dans les racines est que nous en avons quatre.

Donc si vous regardez ici, j'ai ID Google address, dash a, dash B.

Donc rappelez-vous, le début et la fin.

Ne me demandez pas pourquoi je n'ai pas fait ABCD.

Cela semblait logique à l'époque, mais en regardant en arrière, j'aurais probablement dû, j'aurais dû faire A, B, C et D au lieu de faire A et B, c'est le point A, B est la destination et un système de points de passage.

En jour, une supposition, parce que vous pouvez faire plus de points de passage.

Donc ce serait C, D, E, F, G de cette façon, mais bon, la logique était là quand je le construisais.

Donc ce sont les entrées.

Donc lorsque vous tapez ici, il prédira l'adresse lorsque vous tapez dans C, il prédira l'adresse, et ainsi de suite.

Et lorsque vous sélectionnez chacun d'eux, il ajoute ensuite les coordonnées géographiques, la longitude et la latitude à chacune de ces entrées cachées ici.

Donc cette classe est geo idées lat a long a, d'accord, et ensuite elle ajoute une valeur.

J'utiliserai JavaScript pour ajouter cette valeur.

Oui, nous n'en avions pas besoin.

reCAPTCHA en haut de l'écran, car même en passant par la clé reCAPTCHA, donc je peux la supprimer de map aussi.

Faisons, faisons cela.

Il n'y a aucun intérêt à cela, bns.

Donc sauvegardez le retour à root.

Donc c'est l'extend footer.

Donc nous avons un script ici, quelques variables, Google API key et base country.

Et aussi nous référençons ensuite le Google Places, waypoints j s, car dans celui-ci nous devons le faire.

Donc en ajouter un autre.

Et sauvegardez-nous.

Et c'était Google waypoints API dot j, s, waypoints.

Regardons ce qui était probablement faux.

Google Places, waypoints, points.

Et ensuite si nous supprimons cela, nous y voilà, nous avons maintenant ce fichier.

Donc c'est la référence à un fichier qui est en fait là.

D'accord, donc maintenant nous allons regarder le dernier document HTML, qui est map dot html.

Donc si nous allons ici, je l'ai collé il y a un instant.

En tout cas, vous pouvez voir que nous avons beaucoup de choses en cours.

C'est là que nous rendons la carte de Google.

Donc regardons cela, regardons le pied de page d'abord.

Donc nous passons à travers si vous regardez la carte, vue, dans le contexte, nous passons à travers tout cela, d'accord, donc nous passons à travers la clé, le pays de base lat long les données, les données dans les cartes, nous obtenons toutes celles-ci.

Et nous créons, dans ce cas, nous créons une chaîne, nous utilisons toujours le même filtre, sinon JavaScript ne l'aime pas.

Et puis vous avez, nous créons des variables, beaucoup, beaucoup plus longtemps, beaucoup plus longtemps, un NBC D, origine, destination et directions, nous allons en avoir besoin dans l'API Google Places et Google Places, waypoints.

Et aussi, Google Maps JavaScript, que nous n'avons pas encore créé.

Donc Nouveau Fichier, Enregistrer sous Google Maps dot j s.

D'accord, donc nous aurons besoin de tout cela dans Google Maps, d'accord.

Ensuite, une autre balise h3.

Et nous allons nous concentrer sur cela.

Tout d'abord, nous regardons le tableau dans le conteneur.

Donc c'est le conteneur de la carte.

C'est la route de la carte.

Donc nous allons référencer cela dans l'ID de la carte, non ? Parce que les scripts Java dans les fichiers Google j s que nous venons de créer, ils vont essentiellement rendre les cartes et tout le reste, tout le routage et autres dans cet élément appelé une route de carte et seront référencés dans map pre dans le JavaScript.

Ensuite, si nous regardons les choses dans le tableau, j'ai un autre tableau.

Donc nous avons le début de la destination, une durée et la distance, c'est un peu l'en-tête du tableau.

Et nous tirons de directions, origine, directions, destination.

Donc c'est ce qui vient lorsque nous appelons.

Si vous vous souvenez, nous avons des directions ici.

Donc nous passons des directions à travers le contexte.

Et c'est essentiellement un dictionnaire.

Donc nous référençons des mots-clés dans ce dictionnaire directions, tels que l'origine, la destination, la durée et la distance.

Et c'est ce qui est rendu ici.

Ensuite, nous avons des directions, et nous avons ID dir toggle, donc c'est JavaScript void, h ref.

Et ensuite nous avons on click directions toggle.

Donc c'est ainsi que vous voyez les directions, il ne montre pas les directions dans le tissu jusqu'à ce que vous les basculiez.

D'accord, donc c'est juste un petit lien que nous avons là.

Et ensuite nous avons un autre tableau.

Donc nous avons un en-tête de tableau, directions, distance, durée, et c'est là que se rend tout l'itinéraire.

Donc pour chaque jambe, dans directions dot route, nous faisons une boucle for et un compteur.

Et ensuite nous faisons cette boucle for ici.

Avec dist duration text, nous créons ces variables que nous pouvons référencer ici.

Et ils sont dans leg dot steps dans un pied, nous faisons une boucle for dans leg dot steps, créons trois variables, distance, que duration est là et text say, est-ce parce que c'est du HTML brut qui vient de Google.

Et c'est pourquoi nous avons besoin de sauvegarder, car il rendra en fait ce HTML correctement dans le site web.

Et c'est tout.

C'est la carte.

D'accord, la prochaine chose que nous devons faire, tous nos HTML sont complets, nous devons maintenant ajouter un peu de CSS.

Ce que nous allons faire, je ne vais pas perdre votre temps sur le CSS, ce tutoriel d'application était tout sur vous montrer les API Google et Django.

Le CSS n'est pas une réflexion après coup.

C'est très, très important.

Cela le fait paraître fantastique.

Mais vous savez, nous pourrions passer une heure à passer en revue le CSS, ce qui n'est pas nécessairement important.

Mais vous pouvez voir, je référence le body.

Je dis que la famille de polices pour ce fichier particulier est Korea prime, ce qui est correct.

L'élément map root.

Donc c'est ce que nous venons de regarder ici.

Où est-il ? Donc map route, donc nous référençons différents éléments dans chacun des fichiers HTML.

Donc nous avons map container.

Donc j'ai probablement un pour si je cherche.

Le voilà, body HTML map container height 100%.

Après qu'ils aient besoin de chercher des fleurs tout en haut, mais ensuite j'ai le logo, j'ai un côté maintenant.

Donc cela vous montre à quoi ressemble le niveau de signe, puis nous avons quelques médias écran.

Donc cela dépend de la taille de l'écran, de la façon dont il est rendu.

Ce sont à quoi ressemblent les entrées.

Donc une entrée de texte, un email, une entrée de mot de passe, nous avons select text area, c'est ainsi qu'il est rendu, c'est ainsi qu'il apparaît, nous avons une largeur de 100%, un rembourrage de 12, et ainsi de suite.

D'accord, donc nous n'avons pas besoin de perdre notre temps sur cela, ce que nous ne ferons donc pas.

La prochaine chose est le JavaScript principal.

Donc si je vais dans le main, colle cela, tout en bas ici, nous avons du code directement de Django.

C'est une fonction JavaScript pour obtenir le jeton CSRF à partir d'un cookie et ensuite le transmettre avec un appel AJAX, c'est un moyen de contourner pour s'assurer que le bon jeton CSRF est transmis lorsqu'un formulaire est soumis.

D'accord, donc c'est très important que vous ayez cela dans votre fichier JavaScript, lorsque vous soumettez un Ajax.

Donc allons tout en haut du fichier, il y a un peu d'ouverture, comme directions toggle, si vous vous souvenez, dans les cartes, j'ai vu cela quelque part, hey, mec, donc nous avons un petit lien ici.

Et il dit, cliquez ici pour ouvrir la route, essentiellement.

Donc vous pouvez voir la route pour la carte.

Et c'est un clic, vous avez appelé direction toggle.

Et tout ce qu'il fait, c'est qu'il ouvre, supprime l'attribut caché et ajoute un nouvel élément.

Donc nous n'avons pas nécessairement besoin de passer par le JavaScript lui-même.

Mais c'est ce qu'il fait.

Lorsque vous cliquez sur ce toggle, il appelle cette fonction JavaScript.

Et il fait un fondu dans le tableau des directions, sinon vous faites un fondu.

Donc vous l'affichez soit, soit vous le cachez, l'un ou l'autre.

Show it up.

C'est pour toaster.

Donc nous appelons Shola.

Chaque fois que nous faisons un appel AJAX.

Et cela dépend si c'est un succès.

Ou s'il y a une redirection, par exemple, nous passons par tous ces mots-clés, tous ces mots-clés ici.

S'il y a une URL de redirection, et nous appelons ce toaster, house, nous appelons ce toaster.

Donc ce que cela fait, c'est qu'il récupère le titre.

Donc dans ce cas, cela pourrait être un succès, ce message pourrait être merci de vous être connecté.

Et il crée un toaster.

Donc si vous regardez les exemples, encore une fois, cela crée un toaster basé sur tout cela.

Donc si nous ajoutons un bouton de fermeture dans la barre de progression, et ensuite tap show test, dit créer un toaster unique et c'est ce que je fais dans le JavaScript là.

D'accord ? Donc c'est la fonction appelée show that show password.

D'accord ? C'est ce qui est appelé lorsque vous cliquez sur moi pour ouvrir sign up.

est-ce qu'ils vont donc show p word.

D'accord.

Donc c'est une fonction JavaScript qui a été appelée.

Et ce qu'elle fait, c'est que si le type est password, le changer en text, sinon le changer en password, juste un petit toggle.

D'accord, nous créons une variable appelée temp button text.

Donc c'est le texte qui se trouve sur un bouton de soumission.

Donc cela pourrait être sign up sign in.

Donc cela sert à stocker ou cela sera utilisé pour stocker ce qu'un bouton est actuellement nommé.

Et ensuite vous avez un custom form submit post.

Donc lorsque nous soumettons un formulaire, ce qu'il fait, c'est qu'il désactive le bouton, il ajoute un spinner, et il sauvegarde le texte actuel dans cet élément.

Et ensuite, lorsque c'est complet, lorsque le formulaire est soumis, et que tout s'est bien passé, alors nous appelons cela, donc custom form submit response.

Et ce qu'il fait, c'est qu'il supprime l'attribut disabled et il ajoute le texte, qui était avant, donc l'idée est que lorsque vous soumettez un formulaire, il ajoute un spinner disant loading, et ensuite lorsque le formulaire est soumis, il revient à sign up.

C'est tout ce qu'il fait.

Et nous appelons simplement custom form submit post et custom form submit response lorsque nous appelons un Ajax.

Et ensuite nous avons form controls.

Donc nous utilisons strict, mais c'est une variable form controls et est égale à une fonction.

Donc c'est une sorte de fonction JavaScript générale que nous faisons ici.

Et en dessous, c'est lorsque nous initialisons les form controls.

Donc c'est un jQuery document ready.

Donc lorsque pour lorsque le HTML a été rendu, alors nous appelons les form controls, et nous les initialisons.

Donc tout ce qui se trouve ici gagnera.

Donc form controls, nous avons quelques formulaires.

Le premier est user sign up, nous avons sign in user profile, et nous retournons et nous initialisons et fonction, nous initialisons ces formulaires.

Donc chacun d'eux fonctionne certainement.

Donc nous allons nous concentrer sur l'un d'eux.

Donc nous avons l'un de ceux-ci pour chacun des formulaires que nous avons créés.

D'accord.

Donc formulaires, donc nous regardons l'utilisateur est le formulaire utilisateur, qui est le formulaire d'inscription, non ? Oui.

Et nous l'appelons, donc nous regardons sign up, nous allons regarder le formulaire.

Donc sign up form.

D'accord.

Donc c'est ce que nous référençons.

Maintenant, c'est ce que nous essayons de soumettre depuis le frontend, c'est nous qui soumettons un formulaire depuis le frontend, le traitons dans le backend, et modifions la page si nécessaire.

Nous ne rechargeons pas, ce qui est un appel AJAX.

Donc c'est le formulaire d'inscription utilisateur, le formulaire, donc nous créons une variable form, laissez-moi rendre cela un peu plus facile pour vous à voir.

ici aussi.

Donc nous créons une variable form.

Donc ce formulaire, nous utilisons la fonction Ajax.

Donc votre petit signe dollar, Id signup form.

Donc le formulaire est le formulaire d'inscription qui se trouve dans l'inscription, HTML, c'était celui-ci.

Ensuite, nous avons form dot submit function.

Donc c'est lorsque nous soumettons le formulaire, c'est ce que nous faisons, nous empêchons le comportement par défaut.

Donc si nous cliquons sur Soumettre sur le formulaire HTML, il ferait simplement sa fonction par défaut, qui est de soumettre le formulaire au backend en ajoutant event dot prevent default, cela empêche cela de se produire.

Donc cela arrête complètement cela de se produire.

Et ensuite, il passe par ce morceau de code ici.

D'accord, donc nous avons custom form, submit post, nous l'appelons, vous vous souvenez, nous avons ajouté un petit chargeur au bouton.

Et ensuite nous avons google recaptcha.

Ready.

Donc nous avons déjà chargé cela dans ce document HTML particulier comme ce script ici.

Donc nous pouvons maintenant accéder à g recapture.

Donc g recapture dot ready function.

Donc ensuite, ce que nous faisons, c'est G recapture dot execute.

Donc nous passons par le reCAPTCHA psyche qui est passé en bas de cette page, d'accord ? L'action est slash, car c'est la page d'accueil, non ? Donc c'est l'index.

Donc dot then function.

Donc c'est le token, c'est le token que nous obtenons de G recapture le google recaptcha.

Donc document dot get element by ID, ID token dot value.

Donc c'est la valeur du token qui est égale au token.

Donc cet élément caché a maintenant une valeur du token, et ensuite nous le soumettons au backend, donc var form data equals form, qui est ici serialize.

Nous appelons la fonction serialize, et ensuite nous appelons un, nous faisons un appel AJAX.

D'accord.

Donc l'URL est l'attribut action du formulaire.

Sur le formulaire, l'attribut est un sign up.

D'accord ? main, puis wet sorry, méthodes.

Donc l'attribut méthode du formulaire, nous avons ensuite post.

Donc c'est un appel post.

Désolé, une requête post.

Et ensuite les données, nous transmettons les données de formulaire sérialisées.

Nous avons une méthode de succès et une méthode d'erreur.

Donc si quelque chose ne va pas, nous appelons la réponse personnalisée.

Donc form submit response.

Donc le bouton sur le formulaire reviendra à la normale, puis nous montrerons une alerte, qui sera une erreur, il y a eu une erreur, veuillez réessayer.

Et ensuite nous faisons un console log qui ne s'affichera que si le debug est vrai.

D'accord, si c'est faux, il ne montrera rien.

Mais cela montrera une erreur s'il y a un problème.

Cependant, si c'est un succès, pouvons-nous appeler custom forms et met si le résultat est égal à succès, parce que nous sommes, si vous vous souvenez, dans la logique de la vue, où nous surchargeons la fonction form valid et si nous montrons la vue de sign up, donc c'est un succès.

Si recapture fonctionne, alors répondez avec succès.

Si ce n'est pas le cas, alors nous allons appeler.

Donc il a un formulaire invalide, nous allons appeler une méthode d'erreur de formulaire dans le mixin.

Donc si c'est un succès, nous redirigeons vers la page d'accueil.

Si ce n'est pas le cas, nous redirigeons vers false.

Nous ne faisons essentiellement rien.

Donc ensuite, ce que nous faisons, c'est que nous appelons une alerte show, vous ne pouvez pas vraiment voir cela, n'est-ce pas, nous montrons une alerte, et nous passons par le résultat de l'appel, le message, et ensuite le résultat en minuscules.

Et ensuite avec cela, nous passons par la redirection, car nous redirigeons vers la page d'accueil.

D'accord, donc c'est la logique du formulaire d'inscription en JavaScript.

C'est ainsi que nous traitons le formulaire sur le frontend, nous faisons la même chose.

Donc la raison pour laquelle je suis passé par cela et assez en détail, c'est parce que nous utilisons recapture, alors que ces autres formulaires, n'étaient pas le cas.

Donc il n'y a pas de gv capture du tout.

C'est juste basique, nous obtenons le formulaire, nous créons form day, il fera un appel AJAX avec les attributs, action, méthode et form data.

Nous avons un console log Jason, nous n'en avons pas nécessairement besoin.

C'est pour les tests.

Donc c'est la fonction de connexion, la soumission du formulaire de connexion, puis nous avons le profil utilisateur.

D'accord, donc cela sera appelé lorsque nous cliquons programmatiquement sur le bouton de soumission du formulaire dans la route.

Désolé, désolé, c'est dans le profil, mes excuses.

Donc c'est pour le formulaire de profil avec un formulaire de profil.

Si vous regardez, le bouton est désactivé.

Si vous ne pouvez pas, vous ne pouvez pas réellement cliquer sur le bouton de soumission.

Donc ce que nous faisons, c'est que nous cliquons programmatiquement sur ce bouton de soumission lorsque nous obtenons la réponse de Google.

Donc nous allons soumettre ce formulaire en JavaScript depuis le Google.

Où est-il dans le statique depuis l'un de ceux-ci, probablement Google Places API.

Donc lorsque nous obtenons le résultat de Google, nous allons alors supprimer l'attribut disabled du bouton de formulaire.

Et ensuite nous allons cliquer sur le bouton programmatiquement, comme je le dis, donc il n'y a pas de différence, rien de fantaisiste ici.

Ils sont tous très, très similaires.

Mais ils sont les trois formulaires et ils sont dans le main js.

Donc sauvegardons cela.

Nous avons fait le CSS, nous avons fait le JavaScript, maintenant nous devons concentrer notre temps sur Google Maps, Google Places et les points de passage.

D'accord, maintenant, ce que nous devons faire, c'est ajouter le JavaScript à Google Maps.

Copier, Coller.

Donc laissez-moi ouvrir cela un peu.

D'accord, donc tout en haut de la page ici, nous appelons cela donc est-ce que get script et nous appelons maps dot Google API's comm nous passons par la clé API Google.

Et ensuite à la fin de cela, nous ajoutons un S, et libraries equals places.

Donc c'est l'appel que vous devez faire pour avoir accès à tout ce dont nous avons besoin dans Google Maps.

Et c'est ce qui sera utilisé pour rendre la carte dans map dot html.

Donc ce sera la carte avec l'itinéraire à travers les points de passage.

D'accord ? Donc lorsque c'est fait, donc une fois que vous avez ce script fait, et fait cette fonction ici, donc est Google dot maps dot event, add Dom listener, window load, et ensuite vous initialisez la carte.

D'accord, donc c'est juste un appel get script standard pour les API Google, puis c'est la fonction de carte.

D'accord.

Donc nous avons une variable de direction service et directions display.

Et ensuite une variable très variable de map.

Donc nous faisons une nouvelle Google Maps.

Et nous cherchons map route.

Donc c'est l'élément que je vous ai montré dans le HTML de la carte.

Donc c'est là que la carte sera rendue.

D'accord.

Zoom est sept.

Je ne me souviens même pas de ce que cela signifie.

Et ensuite nous centrons la carte contre la latitude et la longitude.

Donc c'est le point de départ.

Donc c'est le centre de la carte.

Et ensuite directions display, vous définissez map, et vous définissez la variable map.

Et ensuite vous calculez et affichez l'itinéraire.

Donc c'est le direction service et directions display que nous allons référencer dans cette fonction ici appelée calculate display route.

Vous avez quelques constantes, donc waypoints, c'est le C et le D.

D'accord, stop over true.

Donc c'est ainsi que nous créons des points de passage.

Et ensuite nous calculons l'itinéraire en utilisant cette fonction ici.

Donc nous passons par direction, service et direction à display.

D'accord, et c'est ce que nous appelons ici en fait.

Donc lorsque nous calculons l'affichage de l'itinéraire, ce sont les deux bits que nous appelons, qui sont ici.

Ils sont venus directement de Google Maps direction service.

Donc nous les tirons ici, direction, service dot route.

Origin, est origin.

Et ils passent dans la destination et les points de passage, ce sont les variables que nous passons, si vous vous souvenez de ici, d'accord, donc origin destination et les points de passage les constantes ici.

D'accord ? C'est ce que Google exige pour rendre cette carte.

Donc optimiser les points de passage est égal à vrai.

Le mode de déplacement est la conduite.

Et ensuite nous avons une fonction de réponse de statut.

Donc si le statut est OK, donc si cela fonctionne, alors directions display set directions response else, déclenchez une alerte.

D'accord.

Donc c'est ainsi que cela fonctionne.

Et c'est le JavaScript de Google Maps.

Donc nous devons regarder l'API Google Places.

nous allons le coller là.

Laissez-moi l'ouvrir un peu.

Encore une fois, nous faisons un autre get script, même chose, pas de différence.

La seule différence est qu'au lieu d'utiliser map, nous utilisons complete, qui est juste un service différent.

D'accord, donc nous laissons autocomplete, donc nous avons cela ici.

Et ensuite nous avons une fonction in it autocomplete.

Donc autocomplete equals, donc nous faisons un nouveau Google dot maps dot places autocomplete.

Et ensuite nous cherchons un élément dans le HTML, qui est ID Google address, si nous regardons le profil, c'est ici, Id Google address.

Donc nous cherchons cet élément.

D'accord.

types, son adresse et restrictions de composants.

Donc le pays, c'est là que nous passons le pays de base.

D'accord.

Donc c'est settings dot bass country, et c'est actuellement défini sur UK, mais si vous le définissez, envoyez-le dans settings dot p y à un pays différent, alors cela devrait techniquement fonctionner.

D'accord.

Donc nous avons autocomplete, add listener change places, donc chaque fois que vous changez l'adresse dans l'entrée, il complétera automatiquement.

D'accord, donc on place changed.

Donc si vous cliquez sur une adresse différente, alors il exécutera ce morceau de logique ici.

D'accord, donc l'autocomplétion, c'est au fur et à mesure que vous tapez, il changera et prédira les adresses.

Mais si vous cliquez sur l'adresse, il exécutera ce code.

Donc vous avez un lieu, donc c'est un complété, vous obtenez le lieu, geocoder, vous faites du géocodage là.

C'est pourquoi nous avons activé cette API, l'adresse.

Donc encore une fois, nous obtenons la valeur des entrées que nous venons de sélectionner.

Et ensuite nous avons geo coder dot geo code, nous passons par l'adresse.

Et ensuite si le statut est OK, donc si l'adresse est correcte, alors nous obtenons la longitude et la latitude de la réponse.

Et nous les ajoutons aux éléments qui ont l'ID de ID underscore latitude et longitude.

D'accord, donc ces deux entrées ont maintenant été remplies.

Et ensuite nous passons par cette logique pour obtenir l'adresse de la rue, la route, le code postal et tout le reste.

Et nous les ajoutons aux éléments correspondants, d'accord, donc je ne vais pas nécessairement passer par eux.

Mais en faisant une boucle sur une réponse de Google, et nous extrayons le numéro de la rue, la route, et nous les sauvegardons dans l'ID de la ville, le comté, le pays, et ainsi de suite.

Ensuite, nous ajoutons l'adresse à, nous ajoutons la valeur à l'ID de l'adresse, et ensuite nous démasquons tous les éléments.

Donc rappelez-vous, tout ce qui a une classe d'élément caché devient démasqué.

Enfin, nous faisons un fondu.

Donc je m'excuse.

Vous trouvez tous les éléments cachés et ignorez le jeton CSRF, et ensuite vous les faites apparaître.

C'est ainsi que cela fonctionne.

Je m'excuse.

Et ensuite, ce que vous faites, vous obtenez le bouton de profil, vous supprimez l'attribut disabled.

Et ensuite, ce que vous faites, c'est que vous soumettez le formulaire, d'accord.

Donc nous ne soumettons pas programmatiquement le formulaire, nous supprimons le disabled, et ensuite l'utilisateur peut soumettre le formulaire.

C'est ainsi que cela fonctionne.

Donc d'accord, Google Places API j.

s, c'est tout.

Et ensuite si nous copions rapidement les points de passage, nous allons simplement les parcourir rapidement.

Jours heureux, non ? Encore un autre Git script, différence étant ici, c'est en fait exactement le même que Google Places API.

D'accord, très, très, très similaire.

C'est juste que ce JavaScript est légèrement différent car nous l'utilisons pour quatre entrées différentes.

Donc au lieu de Google Places API, s, j, s, où il n'y a pas de champs auto, j'ai juste A, B, C, et D, car nous les utilisons simplement pour les points de passage.

Donc encore une fois, dans autocomplete, donc je ne vais pas passer par la logique d'ajout de l'adresse dans la ville et le comté aux éléments cachés, si vous n'en avez pas besoin, ou d'obtention d'une longitude et d'une latitude.

Mais vous verrez ici que ce que nous faisons, c'est que nous parcourons une boucle des champs auto.

Et nous obtenons un et nous cherchons l'ID Google address et nous ajoutons les champs, donc cela devient alors, si c'est un, cela devient la destination, désolé, l'origine, si c'est B, c'est le point de passage un, si c'est C, c'est le point de passage deux, et si c'est D, c'est la destination.

Donc c'est la logique que j'ai dû mettre ici pour utiliser l'API Google sur quatre champs de complétion automatique différents.

Donc c'est l'autocomplétion.

Et ensuite nous avons on place change.

Donc encore une fois, c'est la même chose que Google Places API, c'est juste que j'ai dû adapter la logique pour qu'elle fonctionne et identifie le bon élément d'entrée en fonction du champ de l'ou d'un champ.

D'accord, donc nous passons par le A, B, C, ou D.

Et nous cherchons ID Google address, Addy.

D'accord.

Donc ce que je fais, c'est non, non différent, pas de changement massif par rapport à Google Places API j s, mais ensuite nous appelons calc route, qui est ici.

Donc c'est la fonction que nous appelons.

Et c'est ce que nous utilisons pour créer la requête URL.

D'accord.

Donc nous faisons un encode you are I component, donc nous, ce que nous faisons, c'est que lorsque nous sélectionnons ces quatre points de passage, nous finissons par créer un paramètre URL, et nous l'ajoutons à l'URL.

Et ensuite, c'est en fait assez clé.

Et ensuite, ce que nous faisons, c'est que nous appelons window dot location, assign, et ensuite nous redirigeons l'utilisateur vers l'URL root, désolé, l'URL map, et ensuite nous ajoutons la requête.

Donc la requête serait quelque chose comme, boop boop, lat a, il y aura un point d'interrogation, et il sera lat, a equals 57.4.

Et lasts so long, j'espère que cela a du sens.

Wood equals four is 5.666312, whatever.

Et ensuite, il sera joint avec une barre.

Et ensuite, vous en faites un autre et un autre et un autre.

Donc la chaîne de paramètres finira par être assez encombrante.

Mais elle sera ajoutée à l'URL et l'utilisateur est ensuite assigné à la nouvelle URL avec une chaîne de paramètres.

Et ensuite dans la carte.

View, laissez-moi revoir le main, où sommes-nous, les vues principales, vous pouvez voir que nous essayons en fait de capter cette chaîne de paramètres.

Donc si lat a est trouvé dans request dot get dot get, alors nous pouvons faire quelque chose avec.

Donc c'est ce que nous essayons de faire dans les points de passage.

Encore une fois, ce code sera sur GitHub donc vous pouvez bien le regarder.

Et assurez-vous que vous êtes familier avec.

Mais j'espère que j'ai maintenant passé en revue cela assez en profondeur pour que vous le compreniez sans aller trop loin, mais je vous ai en fait perdu.

Donc je vais terminer cette section ici.

Et dans la section suivante, nous testerons l'application et nous assurerons qu'elle fonctionne parfaitement.

Et ce sera la fin du tutoriel.

Donc merci d'avoir regardé, et je vous verrai dans le prochain segment.

Merci.

Au revoir.

Tout le monde est probablement de décodé ici.

Et dans cette section, qui est la section finale, je vais passer en revue quelques débogages et tests généraux de l'application pour m'assurer qu'elle fonctionne comme prévu.

Donc passons directement à cela.

Si vous regardez sur l'écran, j'ai mon invite de commande ouverte, j'ai mon environnement virtuel lancé et je suis dans le bon répertoire.

À ce stade, si vous aviez suivi le tutoriel sur Django Doc's, vous auriez fait certaines de ces commandes dès le début du projet, mais je ne les ai pas encore faites.

Je ne les ai pas faites pour une raison, en fait.

Donc ce que j'aime faire, c'est me plonger dans un projet et ensuite commencer à faire les migrations plutôt que de le faire dès le début.

C'est vraiment une question de préférence personnelle.

Donc ce que nous devons faire, c'est que nous devons faire quelques commandes ici.

Donc tout d'abord, nous devons faire des migrations.

Donc Python managed.py make migrations, celles-ci, cela va faire quelques fichiers de migration piwi et un cache des migrations de modèle et d'autres morceaux si cela va fonctionner.

Aidez-nous, était un point, je Chi donc de human friendly import format timespan no model names human friendly donc est-ce que je peux regarder rapidement.

J'ai un drôle de sentiment que nous devons installer, c'est juste appelé human friendly.

Donc allons-y, pip install human friendly, brillant, Make migrations.

Les voilà, cela a fonctionné, puis ce que nous allons faire, c'est que nous allons migrer.

Donc si nous ouvrons maintenant Sublime Text, vous verrez que nous avons quelques fichiers supplémentaires ici maintenant.

Donc nous avons db.sq, light three.

Donc c'est pour la base de données.

Donc dans les utilisateurs, lorsque j'ai un PI cache, et dans les migrations, nous devrions avoir un gars, donc vous avez initial.

Donc si nous devions faire un changement dans le modèle, et ensuite exécuter les migrations, encore une fois, cela créerait en fait un nouveau fichier.

Et il ferait une liste de tous les changements que vous faites.

Et toutes les modifications, toutes les créations et mises à jour et choses comme ça.

Main n'aura pas, il aura le poi cache, mais les migrations seront vides, car nous n'avons pas de modèles.

D'accord.

Donc ce sont les migrations que nous avons faites, vous vous attendez à ce que cela ressemble à cela.

Donc nous avons des dépendances du modèle off user, que nous avons, vous savez, c'est le champ one to one.

Et ensuite vous avez l'ID, timestamp Date field, dadda, dadda, dadda, cela, d'accord, donc c'est ce que nous avons fait en faisant des migrations.

Si nous exécutons maintenant le serveur, disons Python manage.py run server, espérons que nous pourrons voir à quoi ressemble le projet sur notre navigateur.

Donc allons-y, Ctrl Shift et ouvrons un écran incognito.

Juste pour le mettre à niveau un peu.

Et si nous allons, localhost avec le port 1000.

Magnifique, j'espérais que c'était comme ça.

Donc vous pouvez voir ici que c'est parti.

Connexion point d'interrogation suivant.

D'accord, donc la page des comptes nous a redirigés vers la connexion.

D'accord.

Donc nous n'avons pas de compte.

Donc nous allons nous inscrire.

Les voilà.

Donc l'objet n'a pas d'attribut recapture public key.

Donc qu'avons-nous fait ici ? Donc si nous allons dans les paramètres, droits, d'accord, donc nous allons appeler cela public key.

Et nous allons regarder mon autre projet pour voir ce que j'ai appelé.

Cela, donc comme faible, les voilà.

Donc et celui-ci n'est pas secret key, nous devons appeler cela private key.

Donc d'accord, donc cela va maintenant réinitialiser le serveur, cela fonctionne maintenant.

Et si nous retournons, c'est ce que vous voyez sur l'écran ici, parce que nous avons debug défini sur vrai.

Si cela était défini sur faux, vous ne le verriez pas.

Les voilà.

Bien.

C'est tout notre travail.

Et donc c'est la page d'inscription.

D'accord, donc allons-y Bobby Stearman, nom d'utilisateur, Bobby at did coding.com mot de passe, ce gars.

P word.

Allons-y.

Mot de passe 123455, cliquez sur Afficher le mot de passe, il le montrera, d'accord.

12345.

Et la raison pour laquelle il le montre, c'est parce que je bascule entre un champ de mot de passe et un champ de texte.

D'accord.

Donc cliquez sur S'inscrire, vous pouvez voir ici, le fait que nous avons cet élément reCAPTCHA en bas de l'écran, ce qui suggère qu'il fonctionne réellement.

Donc cliquons sur S'inscrire.

C'était trop courant.

Donc vous devez avoir un bon mot de passe.

Donc allons-y.

Allons-y.

Fred.

Fred, un.

Ne supposez pas que cela va être très, nous y voilà.

Merci de vous être inscrit.

Donc le fait qu'il y ait une erreur et qu'il y ait un message montre que les erreurs de formulaire fonctionnent réellement dans un mixin, ce qui est fantastique.

Donc maintenant que nous sommes connectés, nous sommes maintenant dans la page des comptes, qui est la page d'accueil, non ? Si nous ne sommes pas connectés, cela nous redirigera vers la page de connexion.

Donc le nom d'utilisateur est decoding user name est Bobby Stearman.

Créons un profil.

Donc c'est le recap, pas le recapture.

C'est le JavaScript de Google Places.

Donc Viper 123.

Tout va bien, cela ne fonctionne pas.

D'accord, cela ne fonctionne pas, inspecter, console.

Échec du chargement de la ressource.

Le serveur a répondu avec un statut de 404.

Donc Google Places dot j s ne peut pas être trouvé.

D'accord, intéressant.

Donc static Google Places parce que ce n'est pas get this Google Places.

C'est bien, c'est une erreur de ma part.

D'accord.

Donc si nous actualisons la page, cela fonctionnera maintenant car ce fichier a été modifié, le nom a été modifié.

Donc si nous allons maintenant à 123, cette page ne peut pas charger les cartes correctement, possédez-vous ce site web ? Intéressant.

Ensuite, vous continuez à déboguer cela rapidement.

D'accord, j'ai compris ce que c'était, c'était parce que je n'avais pas activé la facturation sur l'API.

Et vous devez le faire pour que cela fonctionne.

Donc allez-y et faites cela sur vos clés API.

Donc si je vais maintenant, 123, le voilà.

Et ensuite nous allons cliquer sur Buckingham Palace.

Et ensuite nous allons démasquer tous ces éléments cachés, et nous allons cliquer sur Mettre à jour.

Votre profil a été mis à jour.

Magnifique.

Il devrait maintenant, nous y voilà.

Brillant.

Donc utilisez un profil.

Si nous cliquons sur cela, vous pouvez changer l'adresse.

Donc comme créer ou mettre à jour, ce qui est génial.

Nous avons ensuite root.

Donc ce sont les quatre, donc c'est l'adresse de départ, le point de passage.

Un, deux et la destination.

Voyons si cela fonctionne.

Donc je vais aller avec D'accord, je connais cette adresse.

Je vais aller avec un.

Cherry Orchard.

Les voilà.

Je vais en faire un autre.

D'accord, un High Street Stretton.

Les voilà.

Non, pas celui-là.

Un high streets.

Stress him, ou cliquez sur celui-là.

Et enfin, nous allons avec un marché.

uk.

Et maintenant que j'ai complété les quatre points de passage.

Pouvez-vous voir cela ? Donc nous avons map point d'interrogation, puis nous avons lat a, et il y a long a, que B, long B, C a créé cette chaîne de paramètres, c'est ce qui est utilisé dans la vue.

D'accord, donc nous allons dans la vue dans Maine.

Les voilà.

Donc il capte tous ceux de la chaîne de paramètres.

D'accord.

Donc nous avons le début de la destination, la durée, la distance, la direction, c'est à peu près ça.

Pour être franc, si vous allez faire ce petit trajet, c'est exactement la distance à laquelle je m'attendrais.

C'est la carte.

Sutton had them stratum eally.

Brillant.

Si nous cliquons sur cela, cela fonctionnera-t-il ? Jours heureux, et ce sont les directions.

Vérifions simplement que la déconnexion fonctionne.

Les voilà.

Donc site cette vérification de connexion, aussi.

Donc comme Bobby did coding.com était-ce Fred, Fred one, je pense que l'utilisateur vérifie l'affichage des mots de passe.

Connexion.

Vous êtes maintenant connecté.

Tout fonctionne comme prévu, je suis ravi.

Donc nous y voilà.

Voici votre application Django qui fonctionne avec deux clés API Google et six API Google différentes, dont l'une est recapture.

Et les autres sont un tas d'API de cartes.

Donc nous pouvons faire des adresses prédictives.

Nous pouvons utiliser des cartes, nous pouvons utiliser des points de passage.

C'est fantastique.

Et cela a l'air assez bien aussi.

Donc vous pouvez trouver ce code sur mon GitHub, le lien du dépôt GitHub sera dans la description.

Merci d'avoir regardé, et je vous verrai dans le prochain tutoriel.

Merci.

Au revoir.