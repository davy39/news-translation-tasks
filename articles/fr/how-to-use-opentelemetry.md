---
title: Comment utiliser OpenTelemetry pour comprendre les performances logicielles
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-06-24T16:50:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-opentelemetry
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/opentelemetry-course.jpg
tags:
- name: analytics
  slug: analytics
- name: youtube
  slug: youtube
seo_title: Comment utiliser OpenTelemetry pour comprendre les performances logicielles
seo_desc: 'If you want good performance in your application, you need to collect data
  to figure out where to make improvements. That''s where OpenTelemetry comes in.

  OpenTelemetry offers a single set of APIs and libraries that standardize how you
  collect and tra...'
---

Si vous voulez de bonnes performances dans votre application, vous devez collecter des données pour déterminer où apporter des améliorations. C'est là qu'intervient OpenTelemetry.

OpenTelemetry offre un ensemble unique d'API et de bibliothèques qui standardisent la manière dont vous collectez et transférez les données de télémétrie. OpenTelemetry fournit une spécification pour l'instrumentation afin que vous puissiez envoyer des données à différents backends de votre choix.

Nous venons de publier un cours complet sur OpenTelemetry sur la chaîne YouTube de freeCodeCamp.org.

Ce cours a été rendu possible grâce à une subvention de [New Relic](https://www.newrelic.com), une plateforme d'observabilité qui aide les développeurs à surveiller et à déboguer leurs applications.

Ania Kubów a créé ce cours. Ania est une éducatrice logicielle populaire et elle vous aidera à comprendre pleinement comment utiliser OpenTelemetry dans vos projets.

Dans ce cours, vous apprendrez à utiliser OpenTelemetry pour obtenir une observabilité complète de la pile des performances et du comportement de vos projets logiciels.

Voici les sujets abordés dans ce cours :

* Qu'est-ce qu'OpenTelemetry ?
* Qu'est-ce que les Microservices ?
* Qu'est-ce que l'Observabilité ?
* M.E.L.T
* Histoire
* Configuration de notre Projet
* Qu'est-ce que le Tracing ?
* Contexte et Propagation
* Configuration de notre Tracing
* Qu'est-ce que les Métriques ?
* Cas d'utilisation pour OpenTelemetry
* Configuration du Tracing Distribué
* Utilisation d'autres Outils d'Analyse - New Relic
* Où aller ensuite

Regardez le cours ci-dessous ou [sur la chaîne YouTube de freeCodeCamp.org](https://youtu.be/r8UvWSX3KA8) (1 heure de visionnage).

%[https://youtu.be/r8UvWSX3KA8]

## Transcription de la Vidéo

(Générée automatiquement)

Bonjour, internet, et bienvenue dans ce cours entièrement dédié à OpenTelemetry.

Dans ce cours, je vais vous montrer comment vous pouvez obtenir une observabilité complète de la pile des performances et du comportement de votre projet logiciel en utilisant OpenTelemetry avec l'outil d'analyse de votre choix.

Si vous voulez pouvoir dire pourquoi votre projet ou votre application fonctionne trop lentement, est cassé, ou si vous voulez simplement améliorer la qualité de son code.

Cette vidéo est pour vous.

Mais d'abord, que voulons-nous dire exactement par OpenTelemetry ? Eh bien, commençons par le nom lui-même, nous avons "open" comme dans open source, et "telemetry", qui est une collection automatisée de mesures ou d'autres données à des points distants.

Et cette transmission automatique à l'équipement de réception pour la surveillance.

Le mot télémétrie vient en fait du mot grec "Teller", ou distant, et "metron", pour mesurer.

Et c'est exactement ce que nous allons faire, nous allons faciliter une manière de mesurer les performances de tout ce que nous utilisons dans notre application à distance.

Avec n'importe quelle application, lorsque vous voulez commencer à examiner ce type de données, vous avez deux parties qui doivent se rejoindre.

La première consiste à déterminer comment générer et transmettre ces données.

Et ensuite, la deuxième partie consiste à décider ce que vous allez faire avec ces données.

En d'autres termes, comment allez-vous les analyser ? OpenTelemetry traite de cette partie.

Jusqu'à présent, il n'y avait pas de manière réellement standardisée de décrire ce que votre système fait.

Cela est dû au fait que nous aimons tous penser différemment, utiliser différents langages de programmation, différentes machines, et une combinaison de différentes manières.

C'était un problème, surtout pour ceux qui voulaient construire des outils d'observabilité.

Au cœur du projet OpenTelemetry se trouve exactement cela, une standardisation pour décrire ce que font les systèmes distribués, peu importe le langage de programmation ou les systèmes informatiques que vous utilisez.

Aujourd'hui, le projet OpenTelemetry peut être décrit comme une collection d'outils, d'API et de SDK, utilisés pour instrumenter, générer, collecter et exporter des données de télémétrie, afin que nous puissions les analyser plus tard avec la plateforme de notre choix. En standardisant nos données, nous ne sommes pas liés à quoi que ce soit à long terme.

Et cela rend le passage d'un outil d'analyse à l'autre super facile, cela n'affectera pas vos données historiques.

Comme je l'ai mentionné au début, il s'agit d'un projet open source.

Il est composé de nombreux développeurs et de leurs contributions.

Si nous jetons un coup d'œil à GitHub ici pour le projet, vous verrez qu'il est super transparent.

Vous pouvez voir le Comité de Gouvernance, vous pouvez voir le comité technique.

Si vous êtes intéressé à vous impliquer, veuillez rejoindre leur liste de diffusion et assister aux réunions communautaires.

Vous pouvez même voir toutes les réunions auxquelles vous êtes invité à participer.

Avant de commencer, je veux juste aborder un peu ce que nous allons apprendre dans ce cours.

Alors, décomposons cela.

D'accord, donc dans ce cours, nous allons d'abord examiner ce que sont les microservices, suivis par ce qu'est l'observabilité, puis nous allons examiner MELT, suivis par l'histoire d'OpenTelemetry, puis nous allons commencer par configurer un projet.

Nous allons ensuite parler de tracing, de tracing distribué et de contexte et de propagation avant d'ajouter le tracing à notre projet.

Nous passerons ensuite à l'examen des métriques avant de terminer enfin sur nos projets distribués.

Je terminerai ce cours par où aller ensuite.

Nous attendons de nos sites web, applications et services en ligne qu'ils se chargent presque instantanément, n'est-ce pas ? Pensez à la frustration que certains d'entre nous ressentent lorsque les sites web mettent plus de deux secondes à se charger.

En arrière-plan, un exploit d'ingénierie est nécessaire pour maintenir un système global en fonctionnement afin de vous assurer d'avoir accès à Netflix ou Instagram.

À seulement un clic, examinons Netflix pendant une minute.

Netflix, à son apogée, consomme 37 % de la bande passante internet aux États-Unis, des milliers de personnes cliquent sur lecture en même temps, avec une activité culminant le soir.

Cependant, en tant que plateforme mondiale, c'est un pic constant.

Le défi est de faire fonctionner un service sans perte tout en traitant plus de 400 milliards d'événements par jour, et 17 gigaoctets par seconde pendant les pics.

Dans la vidéo d'aujourd'hui, nous allons approfondir les types de systèmes qui alimentent ces services incroyables et comment nous pouvons utiliser les données pour obtenir une visibilité plus profonde sur les insights de ces systèmes complexes.

Historiquement, les développeurs construisaient des applications en monolithes avec de grandes bases de code complexes, un seul monolithe contiendra tout le code pour toutes les activités commerciales et les applications effectuées.

C'est bien si vous avez une petite application.

Mais que se passe-t-il si votre application s'avère être un succès, les utilisateurs l'aimeront et commenceront à en dépendre, le trafic augmente considérablement, et toujours inévitablement, les demandes d'améliorations et de fonctionnalités supplémentaires.

Ainsi, plus de développeurs sont recrutés pour travailler sur l'application croissante.

Avant trop longtemps, votre application devient une grosse boule de boue.

Une situation où aucun développeur ne comprend l'intégralité de l'application.

Votre application autrefois simple est maintenant devenue plus grande et complexe.

Plusieurs équipes de développement indépendantes travaillent simultanément.

Travaillant sur la même base de code et modifiant simultanément les mêmes sections de code, il devient alors pratiquement impossible de savoir qui travaille sur quoi, la poésie entre en collision, la qualité du code en souffre, il devient de plus en plus difficile pour les équipes de développement individuelles d'apporter des modifications sans avoir à calculer quel sera l'impact sur les autres équipes et les équipes peuvent perdre de vue comment ce code pourrait être incompatible avec d'autres, entre autres problèmes.

Cela entraîne généralement des applications plus lentes et moins fiables, sans parler de calendriers de développement de plus en plus longs.

Les microservices arrivent, le principe principal derrière une architecture de microservices est que les applications sont plus simples à construire et à maintenir lorsqu'elles sont décomposées en plus petits morceaux.

Lorsque vous utilisez des microservices, vous isolez les fonctionnalités logicielles en plusieurs modules indépendants qui sont individuellement responsables de l'exécution de tâches autonomes précisément définies.

Ces modules communiquent entre eux via des API simples.

Les architectures de microservices vous permettent de diviser les applications en services distincts et indépendants, chacun géré par différentes équipes.

Cela conduit naturellement à déléguer les responsabilités pour construire des applications hautement évolutives, permettant un travail indépendant sur des services individuels sans impacter le travail des autres développeurs dans d'autres groupes travaillant sur la même application globale.

Cependant, essayer d'obtenir une visibilité sur ce système peut être très difficile.

Lorsque vous avez des centaines de services et d'applications, votre demande a voyagé à travers le débogage et le dépannage peut être un cauchemar.

C'est là qu'intervient OpenTelemetry.

Comme nous l'avons déjà effleuré, la télémétrie est définie comme la science ou le processus de collecte d'informations sur des objets qui sont éloignés et l'envoi des informations quelque part électroniquement.

Maintenant.

L'observabilité signifie à quel point vous pouvez comprendre ce qui se passe en interne dans un système basé sur ses sorties.

Surtout lorsque les systèmes deviennent plus distribués et complexes.

Il est difficile de voir ce qui se passe à l'intérieur de votre application et pourquoi les choses peuvent mal tourner.

Lorsque l'on parle d'observabilité, nous devons définir les types de données nécessaires pour comprendre les performances et la santé de notre application de manière générale, les métriques, les événements, les journaux et les traces.

Met, les métriques sont des mesures collectées à intervalles réguliers doivent avoir un horodatage et un nom, une ou plusieurs valeurs numériques et un compte du nombre d'événements représentés.

Celles-ci incluent le taux d'erreur, le temps de réponse ou la sortie.

Un événement est une action discrète se produisant à tout moment dans le temps.

Prenons un distributeur automatique.

Par exemple, un événement pourrait être le moment où un utilisateur effectue un achat à partir de la machine.

L'ajout de métadonnées aux événements les rend beaucoup plus puissants.

Avec l'exemple du distributeur automatique, nous pourrions ajouter des attributs supplémentaires tels que la catégorie de l'article et le type de paiement.

Cela permet de poser des questions telles que combien d'argent a été gagné à partir de chaque catégorie d'article, ou quel est le type de paiement le plus courant utilisé.

Les journaux proviennent directement de votre application, exportant des données détaillées et un contexte détaillé autour d'un événement.

Ainsi, les ingénieurs peuvent recréer ce qui s'est passé milliseconde par milliseconde.

Vous avez probablement journalisé quelque chose lorsque vous utilisez des choses comme system out print, ou console log traces suivent une demande de la demande initiale à la sortie retournée.

Il nécessite la chaîne causale des événements pour déterminer les relations entre différentes entités.

Les traces sont très précieuses pour mettre en évidence les inefficacités, les goulots d'étranglement et les obstacles dans l'expérience utilisateur, car elles peuvent être utilisées pour montrer la latence de bout en bout des cœurs individuels et une architecture distribuée.

Cependant, obtenir ces données est très difficile.

Vous devriez instrumenter manuellement chaque service un par un, couche par couche.

Cela prendra autant de temps que l'écriture du code lui-même, ce qui est ennuyeux.

Heureusement, il existe certains projets open source ainsi que des entreprises qui rendent cela beaucoup plus facile. Aujourd'hui, en 2016, OpenTracing a été publié en tant que projet CNCF axé uniquement sur le tracing distribué.

Parce que les bibliothèques étaient légères et simples, elles pouvaient être utilisées pour s'adapter à tout cas d'utilisation.

Bien qu'il ait facilité l'instrumentation des données, il a rendu difficile l'instrumentation des logiciels qui étaient livrés sous forme de binaires sans beaucoup de travail d'ingénierie manuelle.

En 2018, un projet similaire appelé OpenCensus a été open source par Google, qui prenait en charge à la fois la capture de la permission de retracing et des métriques.

Bien qu'il ait facilité l'obtention de données de télémétrie à partir de logiciels livrés sous forme de binaires comme Kubernetes et des bases de données, il a rendu difficile l'utilisation de l'API pour instrumenter des implémentations personnalisées, non incluses dans le cas d'utilisation par défaut.

Les deux projets ont pu rendre l'observabilité facile pour les applications modernes et accélérer l'adoption généralisée du tracing distribué par l'industrie du logiciel.

Cependant, les développeurs devaient choisir entre deux options avec des avantages et des inconvénients.

Il s'avère que les approches des deux projets étaient complémentaires plutôt que contradictoires.

Il n'y avait aucune raison pour laquelle nous ne pouvions pas avoir à la fois l'API neutre du fournisseur abstrait et une implémentation par défaut bien supportée.

Fin 2019, les deux projets ont fusionné pour former OpenTelemetry.

Cela a avancé l'idée d'avoir une seule norme pour l'observabilité au lieu de deux normes concurrentes.

D'accord, donc d'abord, commençons par comprendre exactement ce qui va se passer.

Afin que nous puissions voir ce qui se passe dans notre application.

Ici, nous avons notre projet.

Considérez le projet comme un projet que nous avons créé avec nos éditeurs de code de choix.

Par exemple, si nous l'exécutons, il s'exécute localement sur nos machines.

Disons aussi que ce projet est conçu pour écouter les requêtes.

Comme écouter une requête GET, par exemple, nous avons décidé que nous voulons mesurer les performances de notre application en fonction des requêtes qu'elle fait.

Pour ce faire, la première étape, comme nous l'avons mentionné au début, serait d'implémenter OpenTelemetry dans le projet.

Nous faisons cela pour nous aider à standardiser les données.

Une fois que nous avons implémenté OpenTelemetry et standardisé les données, nous devons réfléchir à ce que nous allons faire avec les données, comment nous allons les visualiser, et ainsi de suite.

Pour cela, nous pouvons utiliser un outil d'analyse.

Par outil d'analyse, je veux dire tout type d'outil qui vous donne de l'observabilité. Nous allons examiner quelques-uns de ces outils, l'un qui se concentre spécifiquement sur le tracing, l'un qui se concentre spécifiquement sur les métriques, et l'un qui examine tout sur une seule plateforme.

Nous allons ensuite envoyer nos données à notre outil d'analyse de choix.

Ici, nous avons un exemple de ce à quoi nos données peuvent ressembler dans une application de tracing telle que zipkin, une application de métriques telle que Prometheus, et un outil d'observabilité tel que New Relic qui nous donnera un aperçu de tout ainsi que d'autres insights plus personnalisés sur une seule plateforme.

Nous aborderons chacun de ces outils dans leurs sections dédiées.

Commençons par implémenter OpenTelemetry en premier.

D'accord, donc avant de commencer, le seul prérequis que je vais vous demander est d'avoir Docker téléchargé sur votre machine.

Docker est une plateforme de conteneurs pour le développement et la livraison rapides de microservices.

Et si vous ne connaissez pas beaucoup les conteneurs et les microservices, restez avec moi pour l'instant.

J'ai une section dédiée à ces deux sujets à venir après cette section.

Pour ceux d'entre vous qui ne l'ont pas, veuillez vous rendre sur le site web de Docker et suivre les instructions.

Afin de vous installer.

Personnellement, je choisirais de télécharger Docker Desktop.

Comme je travaille sur un Mac, je choisis l'option Mac.

Une fois que vous avez terminé, assurez-vous que votre Docker Desktop est en cours d'exécution sur un Mac, je survolerais simplement l'icône comme ceci.

Vous verrez si vous ouvrez la plateforme que je n'ai actuellement aucun conteneur en cours d'exécution.

Avoir un conteneur sera important lorsque nous en viendrons à utiliser les outils d'analyse, tels qu'un backend de tracing comme zipkin.

Une fois que nous avons tous Docker en cours d'exécution, commençons.

Ouvrons notre terminal.

Maintenant, je vais naviguer vers un dossier où j'aime stocker tous mes projets.

Il s'appelle développement.

Veuillez choisir un répertoire dans lequel vous souhaitez travailler.

Maintenant, une fois ici, en utilisant la commande Mk dir, je vais créer un dossier pour le nouveau projet que je suis sur le point de commencer.

Je vais l'appeler open telemetry starting out.

Veuillez noter que si vous utilisez un terminal différent, d'autres commandes peuvent devoir être utilisées.

Maintenant, entrons dans le projet en utilisant la commande cd.

La première chose que je vais faire est de démarrer notre conteneur.

Pour qu'il soit prêt pour la section suivante.

Donc, comme mentionné, la première chose dont vous avez besoin avant de pouvoir commencer à collecter des traces est un backend de tracing comme zipkin, auquel vous pouvez exporter des traces. Pour configurer zipkin aussi rapidement que possible, exécutez le dernier conteneur Docker zipkin, en exposant le port 9411.

Si vous ne pouvez pas ou ne voulez pas exécuter un conteneur Docker, vous pouvez également choisir de télécharger zipkin directement.

Donc, juste pour que vous le sachiez, c'est aussi une option.

Si vous voulez explorer cette option plus en détail, je vous suggère de visiter le site web de zipkin.

Donc, voici la commande pour exécuter notre conteneur.

Et voilà, nous avons maintenant cet identifiant de conteneur, cela a fonctionné.

Ensuite, nous devons obtenir un fichier package JSON dans notre projet, nous pouvons le faire en tapant NPM.

En l'ayant, un fichier package JSON facilitera la gestion et l'installation de tous les packages dont nous avons besoin pour le projet.

Si vous obtenez des erreurs, cela pourrait être parce que vous n'avez pas installé no js et NPM.

Si c'est le cas, veuillez visiter node j s.org.

Afin de vous installer avec cela en suivant les instructions de téléchargement.

D'accord, donc nous avons initialisé l'utilitaire, je vais simplement appuyer sur entrer pour tous ces champs, il me demande de répondre.

Donc entrer et, et, et, et entrer.

D'accord, nous avons terminé la création de notre fichier package JSON pour l'instant.

Si nous listons tous les fichiers de notre projet, en utilisant la commande ls, vous verrez le fichier juste là.

Maintenant, enfin, je dois créer un fichier app js.

Donc un fichier JavaScript et le mettre dans le projet, certains d'entre vous peuvent avoir une approche différente pour ajouter des fichiers à un projet.

Donc c'est totalement à vous, peu importe comment vous souhaitez créer ce fichier.

Mais une fois que nous avons terminé, nous devons maintenant ouvrir notre projet.

Comme j'utilise VS code, je vais utiliser la commande code afin d'ouvrir notre projet.

Et voilà.

Il y a un dossier avec un fichier app js et un fichier package JSON.

Vous verrez que le fichier package JSON contient toutes les invites que nous avons reçues, comme j'ai sauté toutes les invites, il s'agit simplement des entrées par défaut standard ou aucune entrée du tout.

Si vous allez dans le fichier app js, vous verrez également qu'il est actuellement vide, il n'a rien dedans.

D'accord, donc la première chose que je dois faire est de changer cela pour pointer vers le fichier app js que nous avons créé et non vers l'index j s car il n'y a pas de fichier index js.

Et juste pour le plaisir, ce n'est pas nécessaire, je vais remplir la description de mon projet.

Donc open telemetry costs.

La chose suivante que je veux faire est simplement d'ajouter un script de démarrage.

Donc pour ce script, je vais exécuter node app j s.

D'accord, maintenant pour la partie amusante, commençons à ajouter quelques packages.

Pour commencer à utiliser open telemetry, nous allons devoir installer certains de ses packages.

En utilisant NPM II ou install pour faire court.

Je vais stocker le package open telemetry core, le package open telemetry node opentelemetry plugin http opentelemetry.

plugin HTTP s, open telemetry exporters zipkin pour nous préparer à la section suivante sur le tracing open telemetry pour la section suivante à un express le seul non open telemetry.

D'accord, donc nous avons besoin de tous ceux-ci pour installer.

D'accord, et super.

Donc ceux-ci ont l'air bien.

Donc si nous regardons ici, voici les packages que nous venons d'installer.

Ils ont automatiquement peuplé notre fichier package JSON.

Donc cela a l'air bien.

Nous en avons manqué un.

Donc retournons et utilisons NPM II ou install pour faire court et installons Open telemetry plug in Express.

Et nous avons terminé.

D'accord, maintenant passons à notre fichier app js.

La première chose que je vais faire est de définir un port pour nous.

Donc const port, process et V port ou une chaîne de Port 8080 Ensuite, nous allons avoir besoin d'Express.

Donc const Express.

Et Express est l'un des packages que nous avons installés.

Donc celui-ci juste ici.

Donc nous devons dire à notre fichier que cette const nécessite Express.

Nous allons ensuite appeler Express et le stocker en tant que const app.

La première chose que je veux faire est simplement obtenir un message dans notre console log pour nous faire savoir que tout va bien, et que nous écoutons et sur quel port.

Donc, juste pour récapituler, ce que je fais ici, c'est faire démarrer un serveur par l'application.

Et ensuite, avec ce code, je le fais écouter notre port défini pour toute requête.

D'accord, ensuite, je vais coller ce morceau de code super basique.

Ce code est un exemple d'une route très basique.

Le routage fait référence à la manière dont les points de terminaison d'une application répondent aux requêtes des clients.

Nous avons défini la route en utilisant les méthodes de l'objet Express app qui correspondent aux méthodes HTTP.

Par exemple, app get gère les requêtes GET.

Ces méthodes de routage spécifient une fonction de rappel appelée lorsque l'application reçoit une requête vers la route spécifiée et une méthode HTTP.

En d'autres termes, il écoute les requêtes qui correspondent aux routes et méthodes spécifiées.

Dans ce cas, la racine est notre page d'accueil, nous voulons essentiellement tracer chaque fois qu'une requête GET est faite à la page d'accueil.

Nous ferons cela dans la section suivante.

Maintenant que nous avons terminé l'installation de base, il est maintenant temps pour nous de parler du tracing.

Donc, comme vous le savez, OpenTelemetry nous permet essentiellement de standardiser nos données.

La partie suivante consiste à visualiser les données de manière à pouvoir analyser ce qui se passe en coulisses, nous le ferons avec un système de tracing.

En ingénierie logicielle, le tracing implique une utilisation spécialisée de la journalisation pour enregistrer des informations sur l'exécution d'un programme.

Ces informations sont généralement utilisées par les programmeurs pour déboguer en utilisant les informations contenues dans un journal de trace pour diagnostiquer tout problème qui pourrait survenir avec un logiciel ou une application particulier.

Le tracing distribué, cependant, également appelé tracing de requêtes distribuées, est une méthode utilisée pour déboguer et surveiller les applications construites en utilisant une architecture de microservices.

Le tracing distribué aide à localiser où les échecs se produisent et ce qui cause les mauvaises performances.

Donc, comme nous pouvons maintenant le voir, pouvoir obtenir des données de tracing de télémétrie est assez important pour les performances globales d'une application.

Cependant, comme nous l'avons discuté dans l'introduction, en raison des systèmes utilisant tous types de langages, frameworks et infrastructures différents, c'est une chose difficile à faire sans une sorte d'approche commune.

C'est pourquoi OpenTelemetry peut aider autant avec le tracing distribué.

En fournissant un ensemble commun d'API, de SDK et de protocoles filaires.

Il donne aux organisations un service d'intégration unique et bien supporté pour la télémétrie de tracing distribué de bout en bout.

Pour ce cours, le traceur que nous allons utiliser s'appelle zipkin.

Zipkin est un système de tracing distribué qui aide à rassembler les données de timing nécessaires pour résoudre les problèmes de latence et les architectures de services.

Circuit a été créé à l'origine par Twitter.

Et il est actuellement géré par l'organisation bénévole open zipkin.

J'utilise zipkin pour aucune autre raison que j'ai dû en choisir un.

Mais n'hésitez pas à choisir n'importe quel système de tracing backend que vous souhaitez, le choix vous appartient entièrement.

En général, une fois les traces implémentées dans les applications, elles enregistrent essentiellement le timing et les métadonnées sur les opérations qui ont lieu.

Un exemple de cela est lorsqu'un serveur web enregistre exactement quand il reçoit une requête.

Et quand il envoie une réponse.

Ces données sont généralement représentées par une barre, comme ceci, et portent le nom officiel de spam.

Donc dans cet exemple, nous avons deux services et un tas de spans.

Pour expliquer cela, imaginez que cela représente votre application préférée de livraison de nourriture.

Donc imaginez que vous passez une commande.

Maintenant, quelques choses vont se produire, chacune représentée par un span.

Vous envoyez des informations d'avant en arrière entre les services afin d'effectuer le paiement, de trouver un livreur le plus proche de vous, et de notifier ce livreur avec votre commande.

Chacune de ces opérations génère un spam vous montrant le travail effectué pour que cela se produise.

Dans ce cas, les spans ont des relations implicites, donc parent et enfant mais aussi des services individuels et la trace.

Comme vous pouvez le voir, chacun des spans commence à un point différent et prend une quantité de temps différente.

Nous appelons cela la latence et la latence du réseau.

En un mot, la latence est le délai entre une action et une réponse à cette action.

La latence du réseau fait référence à des délais spécifiques qui se produisent au sein d'un réseau.

La latence est généralement mesurée en millisecondes et est inévitable en raison de la manière dont les réseaux communiquent entre eux.

Elle dépend de plusieurs aspects d'un réseau et peut varier si l'un d'eux est modifié.

Les erreurs sur la plupart des systèmes sont généralement assez faciles à repérer.

Si votre barre se termine en rouge ou similaire, par exemple, vous savez qu'une erreur s'est produite.

Maintenant, il est temps pour nous de regarder le contexte et la propagation.

Ces deux concepts nous permettront de mieux comprendre le sujet du tracing.

Donc, comme nous le savons, le tracing distribué nous permet de corréler les événements à travers les limites des services.

Mais comment trouvons-nous ces corrélations ? Pour cela, les composants de notre système distribué doivent être capables de collecter, stocker et transférer des métadonnées ? Nous appelons ces métadonnées contexte.

Le contexte est divisé en deux types, le contexte de span et le contexte de corrélation.

Le contexte de span représente les données requises pour déplacer les informations de trace à travers les limites.

Il contient les métadonnées suivantes.

Nous avons un trace ID, un span ID, les trace flags et le trace state de ce contexte de liaison.

Et ensuite, nous avons le contexte de corrélation.

Un contexte de corrélation transporte des propriétés définies par l'utilisateur.

Cela inclut généralement des choses telles qu'un identifiant client, des fournisseurs, le nom du corbillard, la région de données et d'autres télémétries qui vous donnent des insights de performance spécifiques à l'application.

Le contexte de corrélation n'est pas requis et les composants peuvent choisir de ne pas transporter ou stocker ces informations.

Un contexte contiendra généralement des informations afin que nous puissions identifier le span actuel et la trace, et la propagation est le mécanisme que nous utilisons pour regrouper notre contexte et le transférer à travers les services afin que nous ayons le contexte et la propagation.

Ensemble.

Ces deux concepts représentent le moteur derrière le tracing distribué.

Si vous souhaitez en savoir plus sur ces deux sujets et faire une plongée en profondeur, veuillez visiter le site web d'OpenTelemetry.

Pour les besoins de ce tutoriel, cependant, une connaissance de base ci-dessus suffira.

Donc, juste pour vous donner un petit aperçu, dans cette section suivante, nous allons passer en revue comment initialiser d'abord un traceur global et après cela initialiser et enregistrer un exportateur de trace.

D'accord, donc nous voici où nous nous sommes arrêtés.

Maintenant, dans la dernière section, nous avons exécuté le dernier conteneur Docker zipkin en exposant le port 9411.

Si nous visitons effectivement localhost 9411, nous verrons l'interface utilisateur zipkin qui fait partie de cela.

Donc nous y sommes, c'est ce que nous allons utiliser pour visualiser nos traces.

D'accord, continuons.

Ensuite, créons un fichier nommé tracing et j s et ajoutons le code suivant.

Ce n'est que le code d'exemple fourni par opentelemetry.

Si vous visitez leur site web, vous verrez que je copie simplement ce code ici et le colle dans mon projet.

Vous verrez également que ce fichier utilise deux des packages que nous avons installés dans la configuration initiale.

Une fois que nous avons collé cela, nous devons initialiser et enregistrer un exportateur de trace.

Nous avons déjà fait une partie de cela, car nous avons installé deux packages nécessaires pour cette partie dans la section de configuration initiale.

Et c'est le package open telemetry tracing et le package open telemetry export to zipkin.

Donc, tout d'abord, créons un nouvel exportateur zipkin.

Donc, ajoutez un processeur de span, un nouveau processeur de span simple.

Cela provient du package open telemetry tracing, comme vous pouvez le voir, cela est apparu en haut des nouvelles de l'exportateur.

Et cela provient également d'un autre package.

Donc, le package open telemetry exporters, il peut être emballé comme vous pouvez le voir en train d'apparaître en haut, cela peut ne pas s'afficher automatiquement pour vous.

C'est juste l'éditeur de code que j'utilise.

Donc, vous devrez peut-être taper ces deux-là, puis le nom du service et choisir un service maintenant.

Je vais mettre Getting Started mais vous pouvez le remplacer par votre propre nom de service.

D'accord, cela a l'air bien.

Et le fichier app js aussi.

D'accord, super.

Tout le tracing et la civilisation devraient se produire avant que votre code d'application ne s'exécute.

Le moyen le plus simple de faire cela est d'initialiser le tracing dans un fichier séparé qui est requis en utilisant l'option node r avant que votre code d'application ne s'exécute, je vais vous montrer ce que je veux dire par cela.

Donc, maintenant, si vous exécutez votre application avec node, notre tracing j s et app j s, votre application créera et propagera des traces sur HTTP.

Donc, exécutons cela.

Et maintenant, envoyons des requêtes à l'application via HTTP.

Nous pouvons le faire simplement en actualisant la page localhost 8080, vous verrez des traces exportées vers notre backend de tracing, elles ressemblent à ceci.

Donc, vous verrez que nous faisons une requête GET à la page d'accueil, qui répond avec hello world.

Et ici, nous avons getting started.

Comme c'est ce que nous avons appelé notre nom de service.

Nous obtenons également une heure de début et une durée en tant que span.

Maintenant, à mesure que vous utilisez cela plus souvent, certains spans peuvent sembler être dupliqués, mais ils ne le sont pas.

C'est parce que certaines applications peuvent être à la fois le client et le serveur pour ces requêtes.

Si c'est le cas, vous verrez un span qui est le timing de la requête côté client, et un span qui est le timing de la requête côté serveur, partout où ils ne se chevauchent pas est le temps réseau.

D'accord, maintenant je vais vous montrer un autre exemple.

Donc, juste pour différencier, je vais changer le nom de mon service en get date.

Maintenant, je vais aller dans mon fichier app js.

Je vais simplement copier ce morceau de code ici.

Et coller.

Maintenant, je veux essentiellement écouter chaque fois qu'une requête GET est faite à la date du parc.

En d'autres termes, si quelqu'un maintenant allait sur localhost 8080 slash date, c'est nous qui faisons une requête GET, nous pourrons également voir répondre avec la date réelle.

Donc, allons-y, retournons à notre localhost 8080 et tapons slash date.

Oups, j'ai arrêté mon application en cours d'exécution, assurons-nous qu'elle est en cours d'exécution.

Donc, je vais simplement redémarrer cela.

D'accord, et actualisons notre page.

Et super, voici notre objet avec la date d'aujourd'hui.

Incroyable.

Donc maintenant, si nous visitons localhost 9411, donc le port que nous avons exposé, et cliquons sur exécuter une requête, nous verrons toutes les requêtes qui ont été faites.

Donc, nous y voilà, nous pouvons maintenant voir notre service get date.

Et pour l'instant, la seule requête que nous avons et qu'il écoute est la requête GET.

Maintenant, j'ai en fait renommé le service, donc si je visite la page d'accueil, vous verrez que cette requête est également stockée sous le nom de service get date, vous pouvez dire laquelle c'est par l'horodatage.

D'accord, continuons.

D'accord, nous avons maintenant terminé avec une implémentation de base du tracing.

Cependant, nous ne faisons littéralement qu'effleurer la surface.

Dans la partie projet de notre cours, je vais vous montrer comment utiliser OpenTelemetry pour instrumenter un système distribué.

Par cela, je veux dire que je vais vous montrer comment tracer plusieurs services et leurs interactions les uns avec les autres si ceux-ci existent.

Dans cette section suivante, nous allons apprendre comment collecter des métriques avec OpenTelemetry et utiliser Prometheus comme plateforme de surveillance qui collecte des métriques à partir de cibles de surveillance en récupérant des points de terminaison HTTP de métriques sur ces cibles.

Dans cette section, je vais vous montrer comment installer, configurer et surveiller notre application rapide avec Prometheus et OpenTelemetry.

Nous allons télécharger, installer et exécuter Prometheus pour exposer des données de séries temporelles sur des hôtes et des services.

Contrairement au tracing qui fonctionne en spans, les métriques sont une représentation numérique des données mesurées sur des intervalles de temps.

Les métriques peuvent exploiter la puissance de la modélisation mathématique et de la prédiction pour déduire le comportement d'un système sur des intervalles de temps dans le présent et le futur.

Puisque les nombres sont optimisés pour le stockage, le traitement, la compression et la récupération, les métriques permettent une rétention plus longue des données ainsi qu'une interrogation plus facile.

Cela rend les métriques parfaitement adaptées à la création de tableaux de bord reflétant les tendances historiques.

Les métriques permettent également une réduction progressive de la résolution des données.

Après une certaine période de temps, les données peuvent être agrégées en fréquence quotidienne ou hebdomadaire.

Regardons cela en action.

Dans cette section, je vais utiliser Prometheus comme backend de métriques.

Maintenant que nous avons configuré des traces de bout en bout, nous pouvons collecter et exporter quelques métriques de base.

Tout d'abord, je vais arrêter cela.

Allons sur la page de téléchargement de Prometheus et téléchargeons la dernière version.

Permettez pour votre système d'exploitation.

Comme j'utilise un Mac, je vais cliquer sur celui-ci.

Une fois que cela est téléchargé, ouvrez une ligne de commande et utilisez CD ou la commande cd pour aller dans le répertoire où vous avez téléchargé le fichier tarball de Prometheus.

Dans mon cas, ce sera le répertoire Téléchargements.

Maintenant, je dois le décompresser dans le répertoire nouvellement créé, assurez-vous de remplacer le nom du fichier par votre fichier téléchargé.

Donc, n'utilisez pas nécessairement celui-ci.

Et maintenant, allons dans le répertoire.

Si je liste tous les fichiers et dossiers, vous verrez un fichier nommé permit this yamo, c'est le fichier utilisé pour configurer permit Yes, pour l'instant, assurez-vous simplement que permit est démarré en exécutant le binaire dot four slash promethease dans le dossier et naviguez vers localhost 9090.

D'accord, super.

Et voici notre interface utilisateur de promethease.

Donc vous verrez que ce serveur est prêt à recevoir des requêtes web.

Donc cela devrait être bon.

Je vais simplement ouvrir un nouvel onglet ici pour que je puisse le laisser en cours d'exécution.

Et je vais ouvrir notre répertoire en utilisant le raccourci VS code.

Une fois que nous avons confirmé que permit the US a démarré, nous devons remplacer le contenu du fichier primitives yamo par ce qui suit.

Donc, littéralement, supprimez tout et mettez ce morceau de code beaucoup plus court.

Cela définira l'intervalle de scrape à toutes les 15 secondes.

Nous sommes maintenant prêts à surveiller notre application Node JS.

Dans cette section suivante, nous devons initialiser la bibliothèque de métriques open telemetry requise, initialiser un compteur et collecter des métriques et initialiser et enregistrer un exportateur de métriques.

Pour ce faire, nous allons devoir installer certaines bibliothèques, nous allons avoir besoin du package open telemetry metrics.

Donc, allons-y et installons cela.

Naviguons d'abord vers notre projet.

Donc, ne faites pas cela dans le répertoire que nous venons de télécharger.

Et ici, tapez NPM II ou installez Open telemetry metrics.

Super, nous sommes maintenant prêts à initialiser un compteur et à collecter des métriques.

Nous avons d'abord besoin d'un compteur pour créer et surveiller des métriques, un compteur et open telemetry est le mécanisme utilisé pour créer et gérer des métriques, des étiquettes, un exportateur de métriques, créez un fichier nommé monitoring j s.

Donc, un fichier JavaScript et la racine de votre dossier et ajoutez le code suivant.

Donc, nous aurons besoin du package open telemetry metrics pour ce Kant's.

Et nous allons obtenir le fournisseur de compteurs de celui-ci et par celui-ci, je veux dire le package open telemetry metrics, nous allons ensuite créer une nouvelle constante de console de compteurs.

Et nous allons utiliser le fournisseur de compteurs que nous allons créer un nouveau fournisseur de compteurs et utiliser get meter, ainsi que je vais simplement mettre votre nom de compteur pour l'instant, nous pouvons changer cela quand nous voulons.

Maintenant, nous pouvons exiger ce fichier à partir de votre code d'application et utiliser le compteur pour créer et gérer des métriques.

La plus simple de ces métriques est un compteur.

Dans cette partie suivante, nous allons créer une exportation à partir de notre fichier monitoring js, une fonction middleware qu'express peut utiliser pour compter toutes les requêtes faites par route.

Donc, tout d'abord, nous devons modifier le fichier IO monitoring j s.

Donc, une fois de plus, je vais simplement copier ce code d'exemple des projets open source open telemetry afin de nous aider à compter les requêtes et le coller dans mon fichier monitoring j s.

Ensuite, nous devons importer et utiliser ce middleware dans notre code d'application.

Donc, notre fichier app js.

Donc, nous devons obtenir count all requests à partir de notre fichier monitoring js.

Donc, le module export, nous le faisons en tapant const count all requests require monitoring j s.

Donc, littéralement, nous utilisons cela ici.

Maintenant, utilisons-le.

Tapez app use count all requests et appelez-le maintenant lorsque vous faites des requêtes à votre service, votre compteur comptera toutes les requêtes.

Parfait.

Ensuite, examinons l'initialisation et l'enregistrement d'un exportateur de métriques, les métriques de compteur ne sont utiles que si vous pouvez les exporter quelque part où vous pouvez les voir.

Pour cela, nous allons utiliser Prometheus, la création et l'enregistrement d'un exportateur de métriques est très similaire à l'exportateur de tracing ci-dessus, vous devez d'abord installer l'exportateur Prometheus en exécutant la commande suivante.

Donc, je vais simplement utiliser npm install et open telemetry exporter permit this next step, nous devons ajouter plus de code à notre fichier monitoring js.

Donc, une fois de plus, je vais copier le code qui nous est donné par opentelemetry pour commencer, et le coller dans mon fichier monitoring js.

Ne vous inquiétez pas, je vais partager ce dépôt avec vous tous afin que si vous êtes bloqué, vous puissiez vous référer à mon projet terminé.

Maintenant, dans un onglet séparé, laissez cela en cours d'exécution et montrez que Prometheus est en cours d'exécution en exécutant le binaire Prometheus de plus tôt et démarrez votre application.

Nous le faisons en utilisant le script que nous avons écrit.

Donc, NPM start, vous devriez voir le point de terminaison de scrape de promethease et le HTTP localhost 94644 slash metrics, ainsi que l'écoute des requêtes sur localhost 8080.

Maintenant, chaque fois que vous naviguez vers localhost 8080, vous devriez voir Hello, dans votre navigateur et vos métriques, et Prometheus devrait se mettre à jour, vous pouvez vérifier les métriques actuelles en naviguant vers localhost 9464, slash metrics, qui devrait ressembler à ceci, vous devriez également être en mesure de voir les métriques collectées dans votre interface web Prometheus, nous pouvons également ajouter plus de routes dans notre fichier app js.

Allons-y et faisons cela pour voir à quoi cela ressemblerait.

Donc, je vais simplement ajouter un peu de code pré-écrit ici.

Et c'est une route de niveau intermédiaire, et une autre route qui a le pot backend.

Donc maintenant, nous avons notre date, notre page d'accueil de la section précédente, notre route backend maintenant, et une route de niveau intermédiaire, ainsi qu'une nouvelle route de page d'accueil.

J'aurai également besoin d'axios pour cela.

Donc, un autre package qui m'aidera à faire ces requêtes.

Donc, allons-y et importons cela dans mon projet.

Et bien, c'est fait.

Exécutons NPM start.

D'accord, maintenant vérifions que tout fonctionne comme prévu.

La page d'accueil répond maintenant avec Hello backend.

C'est en fait parce que nous avons deux routes de page d'accueil.

Donc, je vais simplement me débarrasser de l'autre dans un peu.

La route backend répond avec Hello back end, la route date répond avec la date d'aujourd'hui.

Donc, cela a l'air bien.

Donc, je vais simplement supprimer la route de page d'accueil initiale que nous avions et qui répond avec hello world et garder la nouvelle.

D'accord, et maintenant visitons middle tier.

Et nous obtenons une réponse de Hello backend.

Et enfin, visitons matrix où nous obtenons un compteur de requêtes de toutes les routes que nous avons visitées.

D'accord.

Donc, cela semble fonctionner, nous avons visité toutes les routes, et le compteur semble fonctionner correctement.

Maintenant, allons-y et voyons cela dans l'interface utilisateur de Prometheus.

Donc, nous allons devoir choisir quelque chose à exécuter.

Et voilà.

Maintenant, avant de passer à notre projet, je pensais que nous pourrions prendre un peu de temps pour comprendre exactement quels problèmes peuvent être détectés.

Avec OpenTelemetry.

Voici juste une liste que je vais passer en revue avec vous.

En commençant par le backend.

Dans le backend avec OpenTelemetry, vous pouvez détecter une mauvaise logique ou une entrée utilisateur, conduisant à des exceptions, des appels en aval mal implémentés.

Par exemple, vers des infrastructures comme des bases de données ou des API en aval, conduisant à des temps de réponse exceptionnellement longs.

Ou vous pouvez détecter un code peu performant sur une seule API, conduisant à des temps de réponse exceptionnels.

Sur le front-end, avec OpenTelemetry, vous pouvez détecter une mauvaise logique ou une entrée utilisateur conduisant à des erreurs JavaScript.

Vous pouvez également l'utiliser pour trouver un JavaScript mal implémenté, rendant votre interface utilisateur prohibitivement lente, malgré des API performantes.

Et vous pouvez même l'utiliser pour localiser une lenteur spécifique à une région géographique nécessitant une distribution géographique.

Et enfin, pour l'infrastructure, vous pouvez l'utiliser pour identifier des voisins bruyants s'exécutant sur un hôte, épuisant les ressources des autres applications, des changements de configuration, conduisant à une dégradation des performances, un audit de version.

Donc, des vérifications de vulnérabilité zéro jour, en s'assurant que les changements de configuration ont été appliqués, ou simplement une mauvaise configuration avec votre DNS rendant vos applications inaccessibles.

Donc, voici une liste de problèmes que vous pouvez détecter avec OpenTelemetry.

Maintenant que nous avons couvert cela, passons à notre projet.

Et dans cette partie du cours, je veux vous montrer ce qui se passe lorsque vous construisez une application avec un backend plus compliqué qui traite avec deux services.

C'est un projet hypothétique que vous pouvez adapter à ce que vous souhaitez, c'est une application qui obtient des films pour votre base de données.

À la fin du projet, vous serez en mesure de tracer exactement comment nous avons obtenu les films, et combien de temps chaque étape a pris.

D'accord, donc voici un projet que j'ai pré-fait, grâce à la communauté open source et inspiré par un contributeur d'OpenTelemetry, Alan Storm.

C'est un projet qui a deux services, avec un service dépendant de l'autre, mais pas l'inverse.

Dans ce projet, j'ai un service principal de tableau de bord, ainsi que le service de films, qui retournera tous les films pour notre application.

La disposition de ce projet est similaire à ce que nous avons fait dans la configuration du tracing.

Cependant, au lieu d'avoir un fichier tracing js séparé pour tracer chaque service, le code est directement dans chaque fichier.

Donc, comme vous pouvez le voir, chaque service est à la racine de notre projet.

Et je vais simplement minimiser cela pour que nous puissions voir le code un peu mieux maintenant.

Depuis le début de notre cours, cela devrait vous être familier.

Donc, pour rappel, OpenTelemetry nécessite que nous instancions un fournisseur de traces, que nous configurions ce fournisseur de traces avec un exportateur et que nous installions des plugins OpenTelemetry pour instrumenter des modules nœuds spécifiques.

Parlons du code.

Donc, nous pouvons voir ici, pour rafraîchir, surtout comme il est organisé différemment de ce que nous avons vu dans l'implémentation de base.

Donc, tout d'abord, nous allons obtenir le fournisseur de traces de nœud du package open telemetry node.

Un fournisseur de traces est ce qui nous aidera à créer des traces sur no Jess.

Ensuite, nous obtiendrons l'exportateur de spans de console et le processeur de spans simple du package open telemetry tracing.

Et ensuite, nous devons obtenir l'exportateur zipkin du package open telemetry exporter zipkin.

Maintenant que nous avons ce qui est nécessaire, continuons.

Donc, pour l'instant, nous avons fait un programme de tracing.

Et pour générer les spans si vous vous souvenez, nous avons installé un plugin appelé Open telemetry plugin dash HTTP, l'objet node a trace provider est assez intelligent pour remarquer la présence d'un plugin et le charger.

Ce code crée un fournisseur de traces et ajoute un processeur de spans à celui-ci.

Le processeur de traces nécessite un exportateur.

Donc, nous l'instancions également.

Tous deux sont responsables de la sortie des données de télémétrie de votre service et dans un autre système.

Avec ce code, nous créons un exportateur, puis utilisons cet exportateur lors de la création d'un processeur de spans, puis ajoutons ce processeur de spans à notre fournisseur de traces.

D'accord, donc c'est ce que fait ce code.

Donnons un nom à notre service.

Maintenant, je l'ai laissé vide.

Donc, allons-y et remplissons cela.

Comme ce service va traiter le service principal, je vais simplement l'appeler dashboard service.

Ici, nous instancions un exportateur zipkin.

Et ensuite, nous l'ajoutons au fournisseur de traces.

Nous devons bien sûr obtenir Express du package Express.

Et donc un serveur et écouter sur le port 3000 sur une connexion.

L'application ne répondra actuellement à aucune requête de quelque partie que ce soit, car nous n'avons encore rien écrit.

Je voulais répondre avec le tableau de bord lui-même et les films du service de films.

Mais avant de faire cela, nous devons construire notre fichier movies js.

Donc, ce fichier est exactement le même que l'autre fichier, juste peut-être avec du code à différents endroits.

Utilise un port différent.

Dans ce fichier, je veux m'occuper des films.

Donc, je vais simplement renommer ce nom de service en movies service.

Si je lançais ce service, nous écouterions sur le port 3000.

Maintenant, je vais déterminer comment notre application répond à une requête GET à l'endpoint des films.

Donc, je vais simplement écrire get, puis je vais simplement mettre le chemin des films.

Donc, je l'invente.

C'est une fonction asynchrone, et je vais passer une requête et une réponse.

D'accord, donc nous y voilà.

Et ensuite, je vais simplement taper rest type Jason en tant que chaîne.

Et réponse, envoyer Jason stringify.

Et je vais simplement envoyer un objet film avec, disons, un tableau de films.

Donc, mettons quelques objets dans notre tableau, je vais faire en sorte que le tableau ait des objets film.

Et chaque objet film aura un nom.

Donc, un nom comme Jaws, un genre.

Donc, par exemple, Jaws est un thriller en tant que chaîne, et c'est mon premier objet.

Et ensuite, je vais simplement faire un autre objet rapidement.

Cette fois, mettons un type de film différent.

Donc, je vais simplement mettre la chaîne de Ani, et encore une fois, mettons un genre.

Donc, je fais simplement le même objet film, juste avec un nom et un genre différents.

Je vais mettre famille et faire un autre objet.

Je vais m'arrêter après celui-ci, car c'est juste à des fins d'illustration.

Et mettons Jurassic Park comme nom et mettons action comme genre.

D'accord, c'est tout.

C'est notre tableau de trois objets film.

D'accord, maintenant, lançons notre application.

Donc, allons effectivement sur localhost 3000, et mettons le chemin des films.

Donc, ce que je fais, c'est que je demande l'URL.

Et bien sûr, notre application va l'écouter et faire une trace.

Donc, maintenant, allons sur l'interface utilisateur de zipkin et recherchons les traces récentes, nous verrons que nous avons enregistré une trace de service unique.

Cependant, si nous regardons dans les détails de la trace, nous verrons que ces traces ne ressemblent pas aux traces que nous avons vues précédemment.

Dans nos exemples précédents, un span était égal à un service.

Cependant, un span est simplement une période de temps liée à d'autres périodes de temps, nous pouvons utiliser un span pour mesurer n'importe quelle partie individuelle de notre service.

Le plugin d'instrumentation automatique Express crée des spans qui mesurent les actions au sein du framework Express, nous pouvons l'utiliser pour découvrir combien de temps chaque middleware a pris pour s'exécuter, combien de temps votre gestionnaire Express a pris pour s'exécuter, et ainsi de suite.

Il vous donne des insights non seulement sur ce qui se passe avec le service dans son ensemble, mais aussi sur les parties individuelles de votre système Express.

C'est le rôle que jouent la plupart des plugins de contrat dans le projet OpenTelemetry.

Les plugins de base sont préoccupés par le fait de s'assurer que chaque requête est liée à une seule trace.

Mais les plugins de contrat créeront des spans spécifiques au comportement d'un framework particulier.

D'accord, super.

Continuons.

Donc maintenant que nous avons fait cela, je veux vous montrer comment utiliser OpenTelemetry pour instrumenter un système distribué.

C'est à cela que sert notre fichier dashboard js, je veux essentiellement que mon fichier dashboard js appelle également le service de films.

Donc, commençons à écrire ce code.

La première chose que je vais faire est en fait utiliser la bibliothèque node fetch que nous n'avons pas encore installée.

Donc, ce service utilise la bibliothèque node fetch pour appeler notre service de films.

Allons-y et installons cela.

Donc, je vais simplement prendre mon terminal et taper NPM I pour installer et node batch.

D'accord, maintenant, une fois de plus, je vais devoir taper apt get, puis utiliser la route du dashboard et ensuite écrire une fonction asynchrone, donc une fonction asynchrone et passer une requête et une réponse.

Maintenant, je vais écrire ici que j'ai besoin de récupérer des données à partir d'un deuxième service.

Et c'est le service de films.

Je vais simplement écrire un peu de pseudocode pour nous rappeler cela, fetch data running from second service et My second service est le service de films.

D'accord, maintenant, je vais écrire une fonction qui nous aidera essentiellement à obtenir tout le contenu de l'URL du service de films.

Donc, essentiellement notre objet avec les trois films dans un tableau ou des objets de film dans un tableau.

Donc, commençons à écrire cette fonction, je vais écrire cette fonction et passer deux paramètres.

Donc, chaque fois que je passe une URL dans cette fonction et un fetch, donc le fetch va en fait utiliser notre bibliothèque node fetch, puis je vais utiliser ces deux paramètres pour obtenir essentiellement le corps de cette URL.

Donc, je vais utiliser une promesse pour faire cela, nouvelle promesse, je vais passer résoudre et rejeter.

Et ensuite, je vais utiliser fetch pour récupérer l'URL.

Et ensuite, tout ce qui se trouve dans le corps, je vais utiliser donc fetch URL, résoudre rejeter, puis Russ, Russ text, puis body.

Donc, c'est ma fonction pour obtenir le contenu de l'URL.

Passons à l'utilisation de cela.

D'accord, je vais en fait changer cela.

Je n'aime pas la façon dont cela est écrit.

Et je veux le rendre cohérent avec le bas.

Donc, je vais simplement changer cela.

Donc, cela semble un peu plus propre, c'est juste une autre façon d'écrire des fonctions.

Donc, juste pour que cela soit cohérent avec cela.

D'accord.

Donc, une fois de plus, allons-y vers le code que j'ai pré-écrit.

Et ici, je vais récupérer des données en cours d'exécution à partir du deuxième service.

Donc, le service de films, je vais en fait enregistrer le contenu de l'URL en tant que films.

Donc, const movies, await et utiliser la fonction que nous avons pré-écrite pour passer l'URL.

Donc, l'URL que nous voulons obtenir le contenu est HTTP localhost 3004 slash movies.

Donc, nous y voilà, c'est ju L.

C'est la même URL que j'ai écrite ici.

Donc, URL U, r, l, c'est ce que nous avons fait.

Et ensuite, j'aurai besoin de require node fetch.

Donc, je vais chercher à droite require et le package node fetch, je vais mettre rest type Jason, et rez send Jason stringify.

Et maintenant, je vais écrire le mot dashboard.

D'accord, donc je crée un objet, et je vais écrire dashboard, et ensuite tout ce que nous avons enregistré en tant que films devrait apparaître ici.

Donc, essentiellement, le contenu de l'URL apparaîtra ici.

D'accord, donc maintenant je ne peux pas exécuter ce fichier.

Donc, je pourrais exécuter ce fichier, mais nous verrons une erreur.

C'est parce que notre fichier dépend du service de films qui est en cours d'exécution.

Donc, je vais vous montrer maintenant, je vais taper node dashboard, j.

s.

Donc, il écoute sur localhost 3001.

Cependant, si je visite localhost 3001 pour slash dashboard, j'obtiens une erreur.

C'est parce que nous avons besoin que notre service de films soit en cours d'exécution.

Donc, allons-y et faisons en sorte que cela soit vrai.

Je vais simplement ouvrir un nouvel onglet et taper node movies j s.

D'accord, cela ne fonctionne pas et écoute sur le port localhost 3000.

Donc, voici nos films.

Et actualisons ou relançons le dashboard.

Donc, une fois de plus, node dashboard, j s.

Et ensuite, actualisons notre page.

Incroyable, nous verrons notre objet dashboard avec le contenu de l'URL du chemin slash movies.

Incroyable.

Donc, cela fonctionne bien.

Notre code fonctionne comme il se doit.

Maintenant, voyons à quoi cela ressemble dans notre interface utilisateur zipkin.

Donc, je vais simplement relancer la requête et regarder notre dernière.

Et nous y voilà.

Donc, pour réitérer cela en un mot, le service de tableau de bord dépend d'un service de films pour le remplir.

C'est vrai pour de nombreuses applications avec lesquelles vous interagissez aujourd'hui, et c'est pourquoi cet exemple est celui que je voulais vous montrer pour notre projet.

Maintenant, nous pouvons voir ici que chaque span des services sont liés ensemble.

Le plugin HTTP d'OpenTelemetry s'est occupé de cela pour nous, le plugin node fetch utilise la fonctionnalité sous-jacente de node j, s, HTTP et HTTPS pour faire des requêtes.

Donc, voici comment instrumenter une application en utilisant OpenTelemetry.

Comme c'est assez cool, comme vous pouvez voir notre service de tableau de bord, et ensuite vous pouvez voir exactement à quel moment il va au service get movies, et ensuite revenir.

D'accord, cela nous amène à la fin de notre projet.

J'espère que vous avez apprécié cette section.

Ceci n'est bien sûr que la surface de ce que vous pouvez faire avec OpenTelemetry.

Il y a beaucoup plus à cela.

Mais jusqu'à ce que vous maîtrisiez les fondamentaux, j'espère sincèrement que vous pourrez suivre ce cours encore et encore jusqu'à ce que vous vous sentiez plus à l'aise pour construire vos propres projets.

Jusqu'à présent, dans ce projet, nous avons directement obtenu des données d'une application et envoyé les données à zipkin.

Mais que se passe-t-il si nous voulons essayer de les envoyer à un autre backend pour traiter nos données de télémétrie ? Cela signifie-t-il que nous devrions réinstrumenter toute notre application ? Eh bien, les incroyables contributeurs à OpenTelemetry ont trouvé une solution pour résoudre ce problème.

Le collecteur OpenTelemetry est un moyen pour les développeurs de recevoir, traiter et exporter des données de télémétrie vers plusieurs backends.

Il prend en charge les formats de données d'observabilité open source comme zipkin, Jaeger, Prometheus ou flume bit, les envoyant à un ou plusieurs backends open source ou commerciaux.

Dans cette section suivante, je vais vous montrer comment l'utiliser.

D'accord, donc pour cette section, et en utilisant le collecteur OpenTelemetry, nous allons utiliser New Relic comme notre outil d'observabilité de choix.

Tout ce que je vais faire, c'est me rendre sur New Relic et m'inscrire.

Ensuite, vous verrez quelques questions, veuillez répondre à celles-ci du mieux que vous pouvez.

Donc, par exemple, où vous stockez vos données, et cliquez simplement sur enregistrer, votre compte sera alors configuré.

Une fois que vous arrivez à cette page, je vais simplement vous demander de ne pas interagir avec quoi que ce soit pour l'instant, et de vous rendre sur one dot new relic.com.

Une fois ici, je vais vous demander d'aller dans le menu déroulant de votre profil et de cliquer sur API keys.

Une fois ici, je vais vous demander de vous diriger vers la création d'une nouvelle clé et de simplement sélectionner ingest license.

Je vais nommer cela otol example.

Et je vais simplement lui donner quelques notes pour que nous puissions suivre nos clés API.

Et super, notre clé API est maintenant créée.

Copions-la et continuons.

La prochaine chose que nous allons faire est en fait d'obtenir notre collecteur OpenTelemetry.

Pour cela, je vais me rendre sur le compte GitHub de New Relic dans lequel je peux obtenir les exemples OpenTelemetry.

Donc, je vais simplement vous demander de cloner ce dépôt dans votre machine locale.

Je l'ai déjà fait.

Donc, je vais simplement aller de l'avant et me rendre à ce dépôt maintenant.

Et le voilà.

Une fois ici, je vais vous demander de naviguer vers les collecteurs et notre exporter Docker otol config yamo file, car nous allons devoir le modifier un peu.

Donc, veuillez vous rendre ici maintenant.

Et je vais simplement vous demander d'ajouter une petite ligne de code.

Cette ligne de code ajoutera zipkin comme récepteur, un récepteur est conscient que les données entrent dans le collecteur OpenTelemetry.

Donc, parce que nous avons déjà notre application configurée pour utiliser zipkin, nous allons dire au collecteur OpenTelemetry, hé, nous allons vous envoyer des données sous la forme de zipkin.

Donc, c'est ce qui se passe, nous ajoutons zipkin comme récepteur et ensuite nous lui donnons un point de terminaison, qui dans ce cas est 0.0 dot 09411.

Maintenant, parce que zipkin rapporte des données de tracing, nous allons ajouter zipkin comme récepteur de tracing sous service.

Et c'est tout.

La prochaine chose que nous devons faire est d'aller dans le fichier Docker compose yamo, et de nous assurer que le conteneur Docker qui exécute ce collecteur OpenTelemetry est en fait capable de recevoir les données via le même port qu'il aurait si c'était zipkin.

Donc, nous allons ajouter le port 9411, comme ceci et l'enregistrer.

Maintenant, selon le readme pour exécuter cela, nous devons utiliser la clé API que nous venons de créer.

Donc, dans mon terminal, je vais simplement exporter la clé API New Relic que je viens de créer avec cette commande.

Ensuite, nous devons lancer le conteneur Docker avec cette commande, en nous assurant bien sûr que nous sommes dans le bon répertoire.

Donc, c'est de ma faute.

Allons dans ce répertoire.

Donc, le nr exporter Docker.

Et une fois de plus, nous exécutons le conteneur Docker.

et merveilleux.

Maintenant, retournons à notre projet de tableau de bord de films sur lequel nous avons travaillé dans ce cours.

Donc, maintenant, je dois simplement modifier notre app ever since Thirdly, pour qu'il fonctionne avec le collecteur OpenTelemetry.

Pour que cela fonctionne, nous devons changer deux choses, nous devons changer l'URL qui est signalée.

Donc, celle-ci ici, je vais simplement l'utiliser comme ceci.

Donc, nous devons faire cela pour le tableau de bord et aussi pour le service de films.

Et c'est tout.

Maintenant, je vais simplement réinstaller toutes les dépendances pour ceux qui nous rejoignent ici et j'ai pris ce projet de la description ci-dessous.

Et ensuite, lançons les deux services, comme nous l'avons fait précédemment dans ce tutoriel.

Merveilleux.

D'accord, maintenant, je vais simplement appeler les services en visitant le service de tableau de bord.

Pour rappel, le service de tableau de bord dépend du service de films, je vais l'appeler plusieurs fois, afin que nous puissions obtenir beaucoup de données avec lesquelles travailler.

Donc, peut-être juste quelques autres.

D'accord, terminé.

Continuons.

Maintenant que nous avons notre application et que nous avons réussi à instrumenter le collecteur OpenTelemetry qui transmet nos données à New Relic, nous devrions maintenant être en mesure de visualiser nos données.

Pour cela, nous devons aller dans l'onglet Explorer sur New Relic.

Et une fois ici, nous verrons les deux services, le service de tableau de bord et le service de films, tout comme dans la section précédente sur le tracing distribué.

Approfondissons davantage.

Comme vous pouvez le voir dans le service de tableau de bord, il y avait un pic.

Découvrons ce qui se passait.

Donc, il semble qu'il y avait 18 traces avec neuf spans et deux entités pour le service de tableau de bord.

Cela semble correct.

Super.

Et si nous creusons plus profondément, vous verrez le microservice avec lequel notre service de tableau de bord communiquait pour résoudre le résultat final.

Merveilleux.

Comme vous pouvez le voir, nous pouvons obtenir beaucoup de données géniales pour faire des choses comme obtenir l'analyse de la cause racine de ce qui pourrait mal fonctionner dans votre application, vérifier comment vos microservices performants, et bien plus encore.

D'accord, et nous y voilà.

C'était notre cours OpenTelemetry, avant de terminer, je veux juste prendre un moment pour récapituler ce que nous avons appris dans ce cours.

Donc, pour récapituler, dans ce cours, nous avons appris à configurer le backend pour un projet.

Ensuite, nous avons appris à implémenter le tracing dans notre projet, ainsi que les métriques si nécessaire.

Et ensuite, nous avons également examiné deux services et comment ils communiquent.

Grâce au tracing distribué.

J'espère que vous vous sentez maintenant à l'aise en connaissant les avantages de l'utilisation d'OpenTelemetry, ainsi qu'en ayant une bonne compréhension de la manière dont vous pourriez procéder à son implémentation dans vos projets Node JS.

Si vous vous demandez où aller ensuite, avec vos nouvelles connaissances, je vous suggère d'apprendre sur la surveillance de l'infrastructure et la surveillance de l'expérience numérique.

Ce sont deux autres façons de visualiser, analyser et résoudre les problèmes de votre pile logicielle entière.

Je vous laisse avec cela et un lien vers New Relic pour en savoir plus et obtenir un compte gratuit sans date d'expiration.

Merci beaucoup encore pour avoir regardé et je vous verrai bientôt.