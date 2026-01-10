---
title: Comment définir l'infrastructure cloud avec l'AWS Cloud Development Kit
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2022-01-20T15:48:29.000Z'
originalURL: https://freecodecamp.org/news/aws-cloud-development-kit-crash-course
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/AWSCDK.png
tags:
- name: AWS
  slug: aws
- name: youtube
  slug: youtube
seo_title: Comment définir l'infrastructure cloud avec l'AWS Cloud Development Kit
seo_desc: Instead of setting up your cloud infrastructure manually, it can be easier
  and safer to use code. The AWS Cloud Development Kit (CDK) is an open-source software
  development framework to define your cloud application resources using familiar
  programmi...
---

Au lieu de configurer manuellement votre infrastructure cloud, il peut être plus facile et plus sûr d'utiliser du code. L'AWS Cloud Development Kit (CDK) est un framework de développement logiciel open-source pour définir les ressources de votre application cloud en utilisant des langages de programmation familiers.

Nous venons de publier un cours accéléré sur la chaîne YouTube freeCodeCamp.org qui vous apprendra tout sur l'AWS CDK et comment l'utiliser.

Matt Martz a créé ce cours. Il est ingénieur, AWS Community Builder et se décrit comme un fanboy du CDK.

Après avoir appris les bases de l'AWS CDK, Matt vous emmènera dans un speedrun de l'atelier officiel CDK. Ensuite, vous apprendrez des sujets avancés tels que les tests et les meilleures pratiques.

Voici les sections de ce cours :

* Introduction au cours accéléré CDK
* Ce que nous allons couvrir
* Ressources
* Bases du CDK
* Qu'est-ce que les Constructs CDK ?
* Exemples de Constructs de niveau 3
* Synthèse, Assets, Bootstrapping et Déploiement
* Speedrun de l'atelier CDK - Préparation Cloud9
* Speedrun de l'atelier CDK - Nouveau Projet
* Speedrun de l'atelier CDK - Bonjour, CDK
* Speedrun de l'atelier CDK - Écriture de Constructs
* Speedrun de l'atelier CDK - Utilisation des bibliothèques de Constructs
* Speedrun de l'atelier CDK - Test des Constructs
* CDK Avancé
* Plus de ressources et remerciements !

Regardez le cours complet ci-dessous ou sur [la chaîne YouTube freeCodeCamp.org](https://www.youtube.com/watch?v=T-H4nJQyMig) (1 heure de visionnage).

%[https://www.youtube.com/watch?v=T-H4nJQyMig]

### Transcription

(générée automatiquement)

AWS cloud development kit est un outil open source qui permet aux développeurs d'utiliser leurs langages de programmation préférés pour écrire du code d'infrastructure pour AWS. Matt marks est un AWS community builder, et il vous apprendra à utiliser l'AWS cloud development kit.

Hey, je suis Matt Martz.

Je suis un AWS community builder.

Et je suis ici pour vous donner un CDK Crash Course de Free Code Camp.

Vous êtes peut-être ici parce que vous en avez marre de provisionner manuellement vos ressources via la console.

Ou peut-être comme moi, vous détestez écrire du yaml.

Mais le CDK a aussi été beaucoup dans l'actualité récemment.

En décembre, la version deux est devenue généralement disponible.

La version deux était une amélioration massive par rapport à la version un, puisque il n'y a qu'une seule bibliothèque NPM stable à installer, au lieu d'une pour chaque module.

Parmi d'autres améliorations, le CDK a également été mis en avant de manière assez proéminente dans le keynote reinvent du Dr. Vogel.

Et le livre CDK a été publié.

Le livre CDK a été écrit par un groupe des héros AWS, et il approfondira davantage que ce qui sera couvert dans ce cours accéléré, il y aura des chevauchements, mais je recommande toujours fortement le livre.

Alors, que couvrirons-nous dans ce cours ? Je vais commencer par passer en revue les bases des définitions CDK de l'application, des piles, des constructs et comment tout cela se rapporte à CloudFormation.

Ensuite, je vais faire un speedrun de 30 minutes de l'atelier CDK, qui est un atelier fourni par AWS, et il est disponible sur CDK workshop.com.

À partir de là, nous aborderons des sujets avancés comme les tests et les meilleures pratiques.

Ce cours est divisé en chapitres sur YouTube.

Donc, si vous avez des domaines d'intérêt particuliers, n'hésitez pas à sauter d'un chapitre à l'autre.

Je fournirai également des liens de timestamp dans la description avec des informations supplémentaires.

Cela inclura une documentation utile, des blogs, des liens, ou toute autre chose.

Je vais passer très rapidement à travers l'atelier CDK, mais vous devriez le faire vous-même.

La meilleure façon d'apprendre le CDK est de l'utiliser.

Et puisque c'est une vidéo YouTube, n'hésitez pas à m'accélérer, me ralentir, ou revoir des sections si vous en avez besoin.

Si vous pensez que j'ai oublié quelque chose dans ce cours accéléré, ou que vous n'avez pas compris quelque chose, faites-le moi savoir dans les commentaires ou suivez-moi sur Twitter et contactez-moi là-bas.

Je serai heureux de vous aider.

Voici quelques autres ressources que je voudrais spécifiquement mentionner.

La communauté CDK sur Slack est très active.

Elle est remplie de personnes amicales et compétentes qui adorent aider.

Les auteurs du livre CDK sont également très actifs là-bas.

En parlant de cela, avez-vous entendu dire qu'il y a un livre CDK maintenant.

En dehors de cela, il y a aussi le CBK day qui est une conférence annuelle liée au CDK.

L'année dernière, j'ai donné une présentation éclair de 15 minutes sur la création de jots vérifiables avec CDK.

Et j'ajouterai un lien à cela ci-dessous.

Et avec cela, j'espère que vous êtes au bon endroit.

Passons aux bases.

CDK signifie cloud development kit.

C'est un logiciel open source fourni par AWS qui vous permet d'écrire du code impératif pour générer des modèles CloudFormation déclaratifs.

Il vous permet de définir le comment afin que vous puissiez obtenir le quoi, ce qui signifie que vous pouvez vous concentrer davantage sur l'architecture de votre application plutôt que sur les détails fastidieux des rôles IAM et des déclarations de politique.

CDK est disponible en JavaScript, TypeScript, Python, Java, C sharp, et il est en préversion pour les développeurs pour go. CDK lui-même est basé sur no GS.

Même si vous utilisez l'un des autres langages, le code CDK lui-même sera exécuté via no GS.

Donc no J S est une exigence.

D'accord, donc CDK génère CloudFormation.

Mais qu'est-ce que CloudFormation ? CloudFormation est un service AWS qui provisionne les ressources et les piles AWS.

Les ressources AWS sont des choses comme les fonctions lambda, les buckets s3, les tables DynamoDB, presque tout ce que AWS offre.

Une pile CloudFormation est simplement une collection de ressources AWS.

CloudFormation utilise des fichiers JSON ou YAML comme modèle qui décrit l'état souhaité de toutes les ressources dont vous avez besoin pour déployer votre application.

La pile implémente et gère le groupe de ressources décrit dans votre modèle et elle permet l'état et les dépendances de ces ressources à être gérés ensemble.

Lorsque vous mettez à jour un modèle CloudFormation, il crée un ensemble de modifications.

Un ensemble de modifications est un aperçu des modifications qui seront exécutées par les opérations de pile pour créer, mettre à jour ou supprimer des ressources afin que le modèle devienne synchronisé.

Donc CDK génère CloudFormation et CloudFormation provisionne les ressources AWS.

À quoi ressemble l'application CDK et comment cela se rapporte-t-il ? La racine de CDK est l'application CDK.

C'est un construct qui coordonne le cycle de vie des piles à l'intérieur.

Il n'y a pas d'équivalent CloudFormation pour une application.

Dans l'application, vous pouvez avoir plusieurs piles CDK, et les piles CDK peuvent même avoir des piles imbriquées.

Les piles CDK sont équivalentes une à une avec les piles CloudFormation, et les piles imbriquées sont également équivalentes une à une avec les piles CloudFormation.

Lorsque vous exécutez CDK, synth ou CDK deploy, la sortie est le modèle CloudFormation pour cette structure d'application.

L'application CDK est un construct de route spécial qui orchestrate le cycle de vie des piles et des ressources à l'intérieur.

Le cycle de vie de l'application construit l'arbre de l'application dans une approche de haut en bas, puis il exécute les méthodes pour les constructs à l'intérieur.

Vous n'avez généralement pas besoin d'interfacer directement avec les méthodes prepare, validate ou synthesize des constructs, mais elles peuvent être remplacées.

La phase finale du cycle de vie de l'application est la phase de déploiement, où l'artefact de formation de cloud est téléchargé vers cloud formation.

L'unité de déploiement dans CDK est appelée une pile.

Toutes les ressources définies dans le cadre d'une pile, directement ou indirectement, sont provisionnées en tant qu'unité unique. Les piles CDK ont les mêmes limitations que les piles CloudFormation.

Les piles sont puissantes dans cloud formation.

Afin de déployer un modèle dans plusieurs environnements, vous devez utiliser les paramètres de cloud formation.

Mais ceux-ci ne sont résolus que pendant le déploiement.

Dans cloud formation, si vous souhaitez inclure conditionnellement une ressource en fonction d'un paramètre, vous devez utiliser la condition CloudFormation.

Mais dans CDK, vous n'avez pas à utiliser l'un ou l'autre, vous pouvez simplement utiliser une instruction if pour vérifier une valeur si la ressource doit être définie ou non, cela finit par être beaucoup plus simple.

Vous pouvez utiliser les paramètres et conditions de cloud formation dans CDK.

Mais ils sont découragés puisque ils ne sont résolus que pendant le déploiement, ce qui est bien après la synthèse CDK.

Nous avons beaucoup entendu parler des constructs.

Mais qu'est-ce que c'est ? Il y a quatre niveaux de constructs.

Les constructs de niveau zéro sont simplement des ressources de base.

Tous les niveaux supérieurs héritent du niveau zéro, il n'y a pas de type spécifique lié à celui-ci.

Les constructs de niveau un sont des représentations un à un des ressources CloudFormation.

Ils sont tous préfacés dans l'API CDK avec les lettres C F n, ce qui est une forme courte de CloudFormation.

La façon dont je m'en souviens est que le niveau un est un à un avec CloudFormation.

Les constructs de niveau deux ne sont pas des constructs de niveau un améliorés ou étendus.

Ils sont fournis par l'équipe CDK et offrent des méthodes d'assistance et des valeurs par défaut sensées.

Les constructs de niveau trois sont des combinaisons de constructs, qui pourraient être un mélange de constructs de niveau un, deux et trois ensemble.

Plus souvent qu'autrement, vous interagirez avec des constructs de niveau deux ou trois.

Certains modules dans CDK n'ont pas encore de constructs de niveau deux.

Mais presque tous les constructs de niveau un existent pour l'API CloudFormation correspondante.

L'équipe CDK est très rapide pour implémenter les changements aux constructs de niveau un et aux constructs de niveau deux les plus fréquemment utilisés.

Pour le construct de niveau un, regardons le module de l'analyseur d'accès.

Dans ce cas, le module n'a pas de constructs de niveau deux disponibles, donc il n'y a que le construct CFN analyzer de niveau un.

Comme vous pouvez le voir, ceci est une représentation un à un avec l'API CloudFormation.

Le construct CFN analyzer a les mêmes propriétés définies que l'API CloudFormation pour le même.

Il y a aussi de nouvelles méthodes utilitaires d'assistance sur le construct CFN analyzer.

Pour le construct de niveau deux, regardons le construct de table DynamoDB.

Il n'a pas de préfixe CFN et inclut de nombreuses valeurs par défaut sensées.

Par exemple, le mode de facturation est par défaut pay per request, sauf si vous spécifiez des régions de réplication.

Si vous spécifiez des régions de réplication, il devient provisionné et si il devient provisionné, les capacités de lecture et d'écriture par défaut sont définies et par défaut à cinq. La politique de suppression par défaut de la table est conservée.

Et la table a des méthodes d'assistance pour créer des index secondaires globaux ou locaux, et pour créer différents niveaux d'accès à la table et à ses flux.

Pour les constructs de niveau trois, le CDK ne propose rien de spécifique prêt à l'emploi.

Ceux-ci tendent à être créés au niveau de l'organisation individuelle ou de la communauté, et fournis sous forme de bibliothèques.

Un exemple de construct de niveau trois serait de créer un bucket notifiant.

Ce construct crée un bucket s3 ainsi qu'un sujet SNS.

Il ajoute ensuite une notification de création d'objet provenant du bucket s3 pour cibler le sujet SNS.

Tout ce que vous avez à faire pour utiliser cela est d'ajouter un nouveau bucket notifiant à votre application.

Et il provisionnera automatiquement toutes ces ressources.

Il y a plusieurs excellentes ressources dans la communauté que je voudrais également mentionner.

CDK patterns.com est une ressource qui vous permet de rechercher des exemples fournis par la communauté, et elle est référencée par les différents composants utilisés à l'intérieur.

AWS propose également une autre extension open source du CDK avec leurs AWS solutions constructs.

Celles-ci fournissent des modèles multi-services bien architecturés pour définir rapidement des solutions en code pour des modèles fréquemment utilisés.

Cela est disponible sous forme de bibliothèque NPM que vous pouvez installer et utiliser directement.

Il y a aussi le construct hub.

Le construct hub est une destination centrale pour découvrir et partager des modèles de conception d'applications cloud et des architectures de référence conçus pour CDK, CDK pour Kubernetes, et CDK.

Pour TerraForm, et d'autres outils basés sur des constructs, construct hub extrait du registre NPM, tous les constructs CDK qui supportent plusieurs langages et sont correctement annotés.

Super.

Donc je pense que nous avons une bonne compréhension des constructs.

Maintenant, approfondissons un peu.

Comment générons-nous le modèle CloudFormation.

Pour ce faire, l'application doit être synthétisée.

Pour cela, nous pouvons exécuter CDK.

Puisque cela parcourt l'arbre de l'application et invoque la synthèse sur tous les constructs, cela finit par générer des ID uniques pour les ressources CloudFormation et génère le EML respectif ainsi que tous les assets nécessaires.

D'accord, donc qu'est-ce que les assets ? Les assets sont les fichiers regroupés dans les applications CDK.

Ils incluent des choses comme le code du gestionnaire lambda, les images Docker, les versions de couches, les fichiers allant dans un bucket s3, etc.

Ils peuvent représenter tout artefact dont l'application a besoin.

Lorsque vous exécutez CDK synth ou deploy, ceux-ci sont sortis dans un dossier CDK dot out sur votre machine locale.

D'accord, donc que fait CDK avec ces assets ? Comment sont-ils mis dans CloudFormation ? Eh bien, c'est là que le bootstrapping entre en jeu.

Le bootstrapping crée une pile de formation de cloud CDK toolkit déployée dans votre compte.

Ce compte inclut un bucket s3 et diverses autorisations nécessaires pour que CDK effectue les déploiements et télécharge les assets.

Le bootstrapping est requis lorsque votre application a des assets ou que vos modèles CloudFormation deviennent plus grands que 50 kilo-octets.

Donc, c'est presque toujours requis, vous allez presque toujours avoir un type d'asset dans votre pile.

Pour la version deux de CDK, un accès administrateur est nécessaire pour créer les rôles dont la pile CDK toolkit a besoin afin d'effectuer les déploiements.

Vous n'aurez pas besoin d'un accès administrateur après que CDK soit bootstrappé.

Avec le bootstrapping terminé, nous pouvons passer au déploiement.

Lorsque vous exécutez CDK deploy, l'application est initialisée ou construite dans un arbre d'application.

Une fois la construction terminée, l'application passe par les étapes de préparation, de validation et de synthèse.

Ainsi, chaque construct appelle sa méthode prepare, puis chaque construct appelle sa méthode validate.

Et ensuite chaque construct appelle sa méthode synthesized.

Jusqu'à ce point, c'est ce que CDK nous a envoyé.

À partir de là, l'application télécharge le modèle et tous les autres artefacts vers cloud formation, et le déploiement de cloud formation commence.

Une fois ce transfert effectué, tout est entre les mains de CloudFormation.

Maintenant que nous avons défini certaines des pièces de base de CDK, passons à l'atelier.

L'atelier s'arrête à CDK workshop calm.

Vous devriez faire cela en premier et ensuite revenir.

Parfait.

Une fois que vous revenez, nous ferons le tour rapide de 30 minutes de l'atelier.

Nous allons commencer cet atelier en créant un environnement cloud nine.

Pour ce faire, je vais emprunter quelques instructions à l'atelier CDK pipelines, il va avoir un écran et je m'inscris pour Cloud Nine qui a un accès complet.

Cela va être utilisé pour le bootstrapping du compte pour CDK.

Les liens de la version deux pour l'atelier CDK pipelines seront dans la description ci-dessous.

C'est un excellent atelier et vous devriez le travailler si vous avez le temps.

Tout d'abord, nous allons aller à la console cloud nine et créer un environnement.

Je vais simplement le nommer CDK workshop, et nous n'avons pas besoin de description.

Ensuite, nous sélectionnons un type d'instance, j'ai fait cet atelier avec une instance T trois small.

Mais le M cinq large serait probablement mieux.

Toutes les autres options peuvent utiliser les valeurs par défaut.

Pendant que CLOUD NINE se lance, je veux noter que les instances T trois small et N cinq large ne sont pas éligibles pour le niveau gratuit.

Donc cela pourrait vous coûter un peu d'argent.

J'ai obtenu quelques erreurs de mémoire vers la fin avec l'instance T trois small.

Mais cela a quand même fonctionné.

Pour créer le rôle IAM.

L'atelier CDK pipelines a un lien profond qui vous emmènera à la page de création de rôle.

À partir de là, nous confirmons qu'il s'agit d'une entité de service AWS et pour easy to et ensuite aller aux permissions.

Assurez-vous que l'accès administrateur est sélectionné.

Nous n'avons pas besoin de nouvelles balises, donc nous pouvons sauter cela.

Et ensuite nous allons lui donner un nom, nous allons nommer cela CDK admin et créer le rôle.

Avec le rôle créé, nous pouvons revenir à l'atelier CDK pipeline et voir que nous devons en fait aller et attacher le rôle à l'instance EC deux.

Il y a un lien profond.

Mais puisque nous avons nommé l'instance EC deux, quelque chose d'autre, nous devons en fait aller à la console EC deux, aller aux instances.

Et ensuite sélectionner l'instance avec notre instance cloud nine qui est en cours d'exécution.

Aller aux actions, sécurité et modifier le rôle Iam.

À partir de là, nous allons sélectionner les rôles IAM que nous venons de créer CDK admin et l'enregistrer.

Maintenant, si nous allons à l'atelier CDK, Cloud Nine et que nous actualisons, il aura automatiquement le rôle dont nous avons besoin.

Ensuite, nous devons faire un peu de ménage et de configuration dans cloud nine, nous allons supprimer les informations d'identification temporaires gérées par AWS.

Celles-ci nous empêchent d'utiliser le rôle que nous avons attaché à l'instance facile à deux de Cloud Nine, dans le coin supérieur droit de cloud nine, allez dans les paramètres et faites défiler jusqu'aux paramètres AWS et désactivez les informations d'identification temporaires gérées par AWS.

Pour être doublement sûr que les informations d'identification ont disparu, nous allons supprimer le dossier des informations d'identification.

Ensuite, nous allons faire un peu de configuration de l'environnement, nous devons installer JQ en utilisant yum.

Et ensuite nous allons exporter quelques variables d'environnement avec les informations du compte AWS.

Pour vérifier que la région AWS a été définie correctement, nous allons faire cette commande de test.

Et enfin, nous allons exporter l'ID de compte et la région et nous assurer que AWS est configuré correctement.

Maintenant, nous devons nous assurer que Cloud Nine utilise les bonnes instances faciles à utiliser avec le bon rôle Iam.

Pour ce faire, nous allons utiliser cette commande STS get color identity.

Elle va échouer ici parce que nous avons en fait nommé le rôle CDK admin.

Donc si nous mettons à jour la commande pour vérifier CDK admin, nous obtiendrons que le rôle im est valide comme ceci.

À ce stade, nous pouvons revenir à l'atelier CDK intro.

Nous allons aller à l'onglet prérequis et commencer à vérifier les choses pour nous assurer que tout est comme il devrait être.

L'AWS CLI est déjà installé et nous avons déjà configuré le compte AWS et l'utilisateur.

Ensuite, nous voulons nous assurer que nous avons une bonne version de node installée dans Cloud Nine, CLOUD NINE vient avec Node installé.

Donc vérifions simplement la version.

Et ici la version 16 est correcte.

Nous allons également vouloir vérifier CDK.

Maintenant, ceci est un atelier CDK 2.

Donc nous voulons nous assurer que nous avons effectivement augmenté la version de CDK.

Donc si nous faisons NPM i pour installer AWS CDK.

Globalement, nous allons obtenir cette erreur parce qu'il est l'instance Cloud Nine de easytouse weird, donc vous devez en fait forcer.

Dans ce cas, le tutoriel CDK pipeline passe également par cela.

Maintenant que nous l'avons installé de force, nous pouvons voir que la version 2.3 est installée.

Nous utilisons déjà AWS cloud nine, nous venons de vérifier la version CDK.

Et cela conclut les prérequis.

Ensuite, nous pouvons commencer l'atelier réel.

Alors commençons, nous allons au CDK.

Et à l'étape suivante, la première chose que nous devons faire est de créer un répertoire dans lequel travailler.

Donc nous allons créer le répertoire CDK workshop et changer dedans.

Maintenant, nous devons en fait admettre le projet.

Donc nous allons exécuter CDK et l'application d'exemple avec le langage TypeScript.

Cela crée un dépôt Git, et NPM installe toutes les dépendances pour un projet CDK deux de base. CDK deux est une amélioration massive par rapport à la version un de CDK car il intègre tous les modules stables en une seule dépendance NPM. La version un de CDK avait des bibliothèques NPM individuelles pour chaque module comme DynamoDB, lambda SNS, etc.

Dans la version deux, vous n'avez qu'une seule, et cela évite beaucoup d'enfer de gestion des dépendances.

Maintenant que le projet thug est initialisé, CDK workshop va vouloir que nous exécutions la commande watch en arrière-plan pour compiler le TypeScript en JavaScript.

Donc nous allons créer un nouveau terminal, changer de répertoires dans le dossier du projet, puis exécuter la commande NPM run watch en arrière-plan.

Avec cela fait, nous pouvons passer à l'étape suivante et vérifier la structure du projet de ce qui a été initialisé jusqu'à présent.

Donc retournons à l'environnement Cloud Nine, nous allons ouvrir le dossier du projet, et commençons à regarder quelques fichiers.

Commençons là où CDK commence avec le fichier TypeScript bin slash CDK workshop.

Ce fichier instancie l'application CDK en créant des piles.

C'est-à-dire, lorsque vous exécutez CDK center CD kit, boy, il commence ici pour générer les modèles CloudFormation.

Les piles CDK sont équivalentes une à une avec les piles CloudFormation.

Une application peut avoir plusieurs piles, et chaque pile créerait une nouvelle pile dans cloud formation.

Dans le cas de notre application d'exemple, il n'y a qu'une seule pile, la pile CDK workshop.

Donc regardons cela ensuite.

La pile d'exemple est assez simple.

Elle utilise deux constructs de niveau deux.

Un pour créer un SQ SQ et un pour créer un sujet SNS, puis abonne la file d'attente au sujet.

C'est tout.

L'atelier entre dans des détails similaires avec ceux-ci.

Mais passons à notre premier CDK synth.

Comme décrit précédemment, lorsque les applications CDK sont exécutées, elles produisent un modèle AWS CloudFormation pour chaque pile définie dans l'application.

En revenant à cloud nine, exécutons CDK Seth, je vais sortir vers un fichier de modèle dot Yamo pour le rendre un peu plus facile à lire.

Maintenant, il y a deux concepts importants que je veux souligner ici.

CDK est à la fois impératif, il décrit comment l'application sera construite.

Mais il est aussi idempotent, étant donné les mêmes entrées, il produira les mêmes sorties.

Voyez ici, nous utilisons le même code entre le CDK workshop et mon instance cloud nine.

Et le cloud formation qui a été généré est le même.

Par exemple, les hachages de hachage de ressource correspondent entre les deux.

C'est parce que nous avons utilisé toutes les mêmes entrées que le CDK workshop.

Si je changeais l'ID du sujet ou de la file d'attente, le hachage changerait et nous aurions autre chose.

Cela va être important dans les tests unitaires plus tard.

Maintenant que nous avons synthétisé, déployons.

Pour ce faire, nous devons bootstrapper le compte. Ouvrons une nouvelle fenêtre de console et allons à cloud formation.

Et dans ce compte, le seul qui fonctionne en ce moment devrait être celui qui est utilisé pour cloud nine.

Juste ici.

Donc retournons au terminal Cloud Nine et exécutons le Bootstrap.

C'est pourquoi nous avions besoin de créer un rôle im avec un accès administrateur.

Et c'est en fait la seule fois où vous avez besoin d'un accès admin lorsque vous bootstrappez le compte.

Pour que CDK déploie des applications, il doit stocker les assets quelque part.

Le Bootstrap crée son propre modèle de formation de cloud que nous verrons lorsque nous retournerons à cloud formation.

Et cela inclut un certain nombre de rôles et de politiques qui lui permettent de stocker des assets pour le déploiement.

Comme vous pouvez le voir ici, la pile CDK toolkit vient d'être créée à partir du processus de bootstrap.

Maintenant, si nous revenons à cloud nine, nous pouvons en fait exécuter la commande deploy.

La commande deploy resynthétise l'application.

Et s'il y a des changements de politique IAM dans le recensement, il les affichera et demandera de s'assurer que vous voulez continuer.

Ici, puisque nous abonnons la file d'attente au sujet, une politique IAM doit être en place pour que cela se produise.

Donc oui, nous voulons que cela se produise.

Donc déployons-le.

Pendant que CloudFormation se lance, si nous actualisons CloudFormation, nous verrons que la création de la pile CDK workshop est en cours.

Et nous pouvons en fait voir les ressources au fur et à mesure qu'elles sont créées.

Donc ici, nous pouvons voir qu'il y a une entrée de métadonnées ainsi que la file d'attente et le sujet, mais il n'y a pas encore d'abonnement réel ou de politiques liées à celui-ci.

Maintenant que la création est terminée, nous pouvons revenir aux ressources et voir que oui, il y a une politique de file d'attente et un abonnement.

C'était amusant.

Mais maintenant, mettons-nous les mains dans le cambouis.

L'atelier CDK va vous guider à travers quelques étapes à ce stade.

Nous allons nettoyer la pile en supprimant le sujet SNS et le SQ sq.

Et ensuite nous allons créer une simple API gateway soutenue par lambda.

Donc commençons.

Nous allons supprimer le code d'exemple de notre pile.

Et ensuite nous allons faire une diff pour voir ce qu'il montre.

Revenez au fichier de pile.

Et supprimez la file d'attente, le sujet et le sujet qui ajoute la description ainsi que les imports.

Cela se trouve sur la commande CDK diff.

Ce que CDK diff fait, c'est qu'il resynthétise l'application CloudFormation et compare le yaml de l'un à l'autre.

Et nous pouvons voir ici qu'il détruit la file d'attente, la politique de file d'attente, l'abonnement et le sujet.

Ensuite, nous pouvons CDK deploy, pendant qu'il déploie, la seule chose que la pile CloudFormation devrait avoir est l'entrée de métadonnées CDK.

Jusqu'à ce que nous retournions à cloud formation, nous pouvons vérifier la progression de cela en actualisant les ressources au fur et à mesure qu'elles progressent.

Ils sont terminés. Maintenant, retournons à cloud nine et créons le lambda.

Nous allons créer un dossier appelé lambda, et y mettre un fichier hello.js.

À l'intérieur de celui-ci, nous mettrons un peu de code lambda de base.

Ensuite, nous devons créer le lambda dans la pile, nous ajouterons l'importation lambda de CDK pour ensuite créer la fonction lambda réelle.

L'un des plus grands avantages de la création de ressources AWS en utilisant CDK est l'IntelliSense.

Ayant importé de AWS lambda, je peux créer une nouvelle fonction en utilisant new lambda dot function, passer la pile et l'ID du lambda et lui donner quelques propriétés.

Dans ce cas, nous devions trouver le runtime en utilisant lambda.runtime.no, Gs 14 où le code vit, que nous utilisons code dot from asset et ensuite lambda, qui télécharge le dossier lambda en tant qu'asset vers s3.

Et ensuite ils étaient les gestionnaires.

Dans ce cas, nos gestionnaires et Hello, le fichier Hello, et il est nommé gestionnaire.

Maintenant, nous pouvons exécuter la diff.

Et cela nous montrera qu'il va créer un rôle im pour le lambda et la fonction lambda elle-même.

Ce qui me semble bien.

Donc déployons-le.

Je vais accélérer un peu cette partie.

Et nous pouvons voir la fonction et le rôle dans cloud formation.

Donc testons le lambda lui-même.

Dans la zone de source de code de la console lambda, nous pouvons créer un événement de test en cliquant sur le bouton de test.

Nous sélectionnerons API gateway AWS proxy, car finalement, nous connecterons cela à une API gateway.

N'oubliez pas de lui donner un nom.

Et il n'aime pas les espaces.

Et appuyez sur créer.

Que recevons-nous ? Testons à nouveau, il invoquera le lambda.

Et maintenant nous pouvons voir le statut de 200.

Et que le corps a la bonne réponse.

Donc ajoutons une API gateway.

Tout d'abord, nous importerons le module API gateway de CDK.

Et ensuite nous créerons une API REST lambda.

Les API REST lambda sont simplement des API REST avec un proxy glouton qui envoie tout au lambda défini.

Nous passerons le construct de pile et donnerons à l'API REST un ID.

Et ensuite nous lui dirons notre fonction hello en tant que gestionnaire d'API.

Maintenant, nous pouvons exécuter une diff.

Et je montrerai également qu'il n'y a en fait aucune API gateway déjà définie en allant à la console API gateway.

Et ici, il n'y a pas d'API.

Donc déployons-le.

Je vais accélérer cela à nouveau.

Mais ce qu'il fait, c'est qu'il crée un tas de ressources automatiquement.

Il y a l'API gateway elle-même, les permissions pour la gateway, et pour qu'elle invoque le lambda, etc., etc.

Maintenant que c'est fait, nous pouvons voir que nous sommes passés de trois ressources à 15 dans CloudFormation.

Et tout cela a été géré avec quelques lignes de code.

Et si je vais et que j'actualise la page lambda, nous pouvons voir que l'API gateway est ajoutée à la console lambda en tant que déclencheur.

De même, nous pouvons voir que l'API est définie sur la console API gateway.

Donc testons-la.

Nous allons récupérer l'URL de l'API qui a été automatiquement sortie dans le cadre du déploiement, et lui envoyer une requête curl.

Bien.

Et essayons-en une autre.

Très bien.

Tout ce que nous avons fait jusqu'à présent, c'est utiliser quelques constructs de niveau deux.

Créons notre propre construct de niveau trois.

Nous allons créer un lambda intercepteur qui écrit dans la table DynamoDB, puis invoque tout lambda en aval ciblé.

Commençons.

Nous allons créer un nouveau fichier de script de type hit counter dans le dossier lib, et y mettre un peu de code de construct de base.

Tout ce que cela fait, c'est étendre le construct et définir les props.

Ensuite, créons notre lambda intercepteur et dans le dossier lambda, nous allons créer hit counter dot j, s.

Et nous allons copier le code de l'atelier.

Ce que fait ce code, c'est qu'il utilise deux modules du SDK AWS pour interagir à la fois avec Dynamo DB et lambda, nous utiliserons Update Item de Dynamo DB pour incrémenter un compteur de hits pour un chemin.

Et nous utiliserons le client lamda pour invoquer le lambda en aval, puis retourner la réponse de ce lambda avec la table et lambda qui seront passés à ce lambda intercepteur via des variables d'environnement.

Maintenant que c'est fait, nous devons créer à la fois la table et le lambda, nous allons ajouter le module DynamoDB de CDK.

Et ensuite créer la table en utilisant new DynamoDB dot table, nous allons passer le construct de pile et donner à la table un ID.

Et DynamoDB doit également définir une clé de partition.

Donc nous allons le faire également.

Ensuite, nous allons créer le lambda, cela suit le même modèle que précédemment, faire lambda dot function, passer cela, lui donner un ID et définir le runtime qui est no Jess.

Le gestionnaire, qui dans ce cas est hit counter dot handler et ensuite le code provenant de code dot from asset lambda, nous devons passer les variables d'environnement.

Et je vais faire une petite modification à l'ID lambda juste pour être cohérent avec l'atelier.

Maintenant, nous allons vouloir exposer le lamda comme une propriété en lecture seule du construct.

Donc ajoutez cette ligne Public Read Only à la classe.

Et nous allons assigner le lambda à la propriété.

Maintenant, ce construct est génial tel quel, mais il n'est utilisé nulle part.

Donc corrigeons cela.

Nous allons revenir à la pile principale de l'atelier.

Et utiliser le construct.

C'est le même modèle qu'un construct de niveau deux.

Donc nous pouvons faire un nouveau hit counter, passer dans la pile, lui donner un ID.

Et dans notre cas, les propriétés ici sont le lambda en aval que nous voulons invoquer.

Donc nous allons définir downstream à Hello.

Et je vais faire un truc pour importer le hit counter depuis le fichier local.

Mais maintenant nous devons faire en sorte que l'API utilise ce lambda à la place.

Donc nous allons déplacer l'API ci-dessous et changer le gestionnaire de l'API de hello à hello avec counter et c'est pourquoi nous exposons la propriété Read Only pour le gestionnaire, c'est pour que l'API ait en fait accès au lambda à l'intérieur du construct.

Donc déployons-le.

Avec un peu de magie d'édition, nous allons sauter en avant à nouveau.

Maintenant que nous sommes déployés, nous pouvons le tester.

L'atelier CDK intègre des pièges pour exposer certaines choses intéressantes sur les constructs LTU.

Comme nous pouvons le voir, la requête ici a échoué.

Pour voir pourquoi, nous devons regarder les logs.

Donc passons à la console lambda dans la console.

Cliquez sur l'onglet Monitor, et cliquez sur view logs dans cloud watch.

Si nous allons au dernier flux de logs, nous pouvons voir qu'il y a une erreur d'invocation, et c'est à cause d'une exception Access Denied.

Et si vous lisez un peu plus loin, il dit essentiellement que le lambda n'est pas autorisé à effectuer Dynamo DB Update Item sur la ressource.

Nous ne lui avons jamais donné la permission.

Donc retournons au fichier hit counter.

Nous allons utiliser les tables L pour appliquer les bonnes déclarations de politique au lamda.

L'atelier a également oublié d'ajouter la permission pour que le lambda puisse invoquer le lambda en aval.

Donc nous allons simplement ajouter cela maintenant.

Maintenant, si nous déployons à nouveau, et sautons en avant et testons la fonction, nous obtiendrons une réponse réussie car tout a les bonnes permissions.

À partir de là, si nous allons à Dynamo DB, et actualisons les éléments dans la table, nous pouvons voir que les bons endpoints sont suivis.

De l'atelier CDK, nous allons npm installer la bibliothèque CDK Dynamo table viewer dans notre projet.

Avec elle installée, nous pouvons passer à notre pile et importer le table viewer depuis la bibliothèque.

Ensuite, nous allons créer une nouvelle instance de celui-ci.

Cette bibliothèque table viewer est un construct L trois car elle regroupe plusieurs constructs L deux ensemble, tout comme nous l'avons fait avec le construct hit counter L trois que nous avons fait dans la section précédente.

Le construct table viewer s'attend à ce que nous passions la table DynamoDB de notre autre construct, mais nous ne l'avons pas exposée.

Donc retournons à notre construct, ajoutons la propriété table et assignons la table à cette propriété.

Avec cela, nous pouvons passer la propriété hello avec counter dot table dans notre construct tiers.

Maintenant, si nous déployons et sautons en avant, nous verrons que le construct table viewer a créé une API gateway séparée et son propre endpoint défini dans les sorties.

Si nous y allons, il finira par afficher ce qui se trouve dans la table DynamoDB.

Tester les constructs est l'une des choses les plus puissantes à propos de CDK.

L'atelier CDK vous guide à travers deux types de tests, les tests d'assertion et les tests de validation.

Pour le premier test d'assertion, nous allons créer une pile et utiliser notre construct hit counter puis vérifier qu'une table DynamoDB a été créée.

Donc retournons au code.

Créons le test et supprimons les anciens. Maintenant nous pouvons l'exécuter.

Et une table DynamoDB a été créée.

Ensuite, nous passerons à la vérification du lambda.

La bibliothèque CDK assertions a quelques fonctionnalités utiles comme capture, qui peut intercepter différentes propriétés dans le cadre de la synthèse du modèle.

Dans ce cas, nous utilisons CAPTCHA pour vérifier que la fonction en aval correcte et les noms de table sont passés dans le lambda hit counter.

Lorsque nous exécutons ce test, nous nous attendons à ce qu'il échoue parce que je n'ai pas copié les références de la sortie synthétisée.

Mais le faire échouer le rend en fait plus facile à les trouver.

Donc nous allons prendre les bons noms et mettre à jour le test avec les bons.

Maintenant, lorsque nous l'exécutons, il passera.

Ensuite, adoptons une mentalité de développement piloté par les tests.

Et disons que nous voulons nous assurer que notre table utilise le chiffrement côté serveur, nous pouvons affirmer que la ressource de table DynamoDB a le chiffrement côté serveur activé.

Donc lorsque nous exécutons le test, il échouera.

D'un point de vue développement, cela signifie que nous devons revenir au construct et nous assurer que le chiffrement côté serveur est activé.

Maintenant, si nous exécutons le test à nouveau, il passera.

Puisque nous ne voulons pas vraiment cela, je vais le supprimer du construct et supprimer le test.

Ensuite, parlons des tests de validation.

Disons que dans le cadre de votre construct, vous voulez vous assurer qu'un nombre sain d'unités de capacité de lecture est utilisé dans la table DynamoDB.

Nous pouvons ajouter une propriété de capacité de lecture qui est passée dans le construct.

L'utiliser dans la table.

Et ensuite dans le constructeur, nous pouvons valider que la valeur passée est raisonnable, disons entre cinq et 20.

Si ce n'est pas le cas, nous lancerons une erreur.

Maintenant, ajoutons un test qui passe une valeur hors de portée à un trois et vérifions que l'erreur est lancée.

Lorsque nous exécutons le test, il passera parce que l'erreur est lancée.

Cette erreur serait lancée dans le cadre de la synthèse de la pile.

Donc voyons cela, nous allons revenir à notre pile d'atelier.

Ajouter une valeur de capacité de lecture hors limites et exécuter la synthèse de la pile.

Comme vous pouvez le voir, les tests de validation sont super utiles.

Dans mon travail, je les utilise pour aider à faire respecter certaines conventions de nommage, et aussi pour journaliser ou lancer des avertissements de dépréciation lorsque les entrées ou les valeurs par défaut des propriétés changent.

Bon travail avec l'atelier.

Maintenant que l'atelier est terminé, nous pouvons passer à des sujets avancés comme les aspects et les meilleures pratiques.

Dans l'atelier, nous avons passé en revue les assertions granulaires en vérifiant des choses comme le nombre de tables créées et en nous assurant que le chiffrement était activé.

Nous vérifions pour nous assurer que les variables d'environnement lambda passées sont les bonnes.

Mais vous pourriez également utiliser les tests de snapshot pour vérifier l'ensemble du modèle si vous voulez le faire et utiliser les fonctionnalités de correspondance de snapshot de gests.

Nous avons également passé en revue les tests de validation dans le cadre de l'atelier.

Nous avons vérifié les propriétés passées dans le construct pour nous assurer que les unités de capacité de lecture étaient dans une plage spécifique.

Dans mon organisation, nous utilisons également cela pour aider à faire respecter certaines conventions de nommage ainsi que pour lancer des avertissements de dépréciation dans le cas où nous devons changer significativement le construct.

Dans ce cas, les avertissements ne bloqueront pas le déploiement, mais ils apparaîtront dans la console lors de la synthèse de déploiement, où les développeurs peuvent les récupérer et les corriger.

Vous n'êtes pas limité à simplement journaliser les erreurs dans la console, lorsque vous envoyez, vous exécutez le code réel.

Donc vous pourriez également journaliser vers un service externe comme un service de plateforme qui suit les déploiements, ou journaliser vers cloud watch lui-même.

La dernière forme de test est le test d'intégration.

Avec CDK, vous pouvez utiliser les ressources personnalisées AWS pour tester que les ressources fonctionnent ensemble correctement dans le cadre du déploiement CloudFormation.

Si quelque chose se casse, il annulera automatiquement le déploiement CloudFormation.

CDK dispose d'un framework de fournisseur pour l'interface avec les ressources personnalisées CloudFormation.

Ces ressources personnalisées vous permettent d'écrire une logique de provisionnement personnalisée et des modèles que CloudFormation exécute chaque fois que vous créez, mettez à jour ou supprimez des piles.

Nous pouvons utiliser cela pour effectuer des tests d'intégration dans notre pile.

Disons que vous avez un bus d'événements, un lamda.

Et une table DynamoDB que vous voulez vous assurer interagissent les uns avec les autres.

Vous pourriez utiliser le framework de fournisseur pour lancer un lambda pour émettre un événement de test sur un Event Bus, tout cela dans le cadre du déploiement CloudFormation.

Et ensuite la ressource personnalisée peut interroger DynamoDB en attendant le changement.

Si le changement ne se produit pas dans un délai déterminé, la construction échouera et CloudFormation annulera automatiquement les changements.

Matt Morgan a un excellent article de blog à ce sujet appelé testing the async cloud with AWS CDK.

Le livre CDK a également une section à ce sujet.

Un autre sujet avancé pour le CDK sont les aspects. Les aspects sont un outil très puissant dans CDK.

Il y a un moyen d'appliquer une opération à tous les constructs dans une portée donnée.

L'aspect pourrait modifier les constructs, comme en ajoutant des balises, ou il pourrait vérifier quelque chose ou l'état des constructs, comme s'assurer que tous les buckets sont chiffrés.

Pendant la phase de préparation, CDK appelle la méthode visit de l'objet pour le construct et chacun de ses enfants dans un ordre de haut en bas.

La méthode visit est libre de changer n'importe quoi dans le construct.

Dans cet exemple, la classe de vérification de la version du bucket implémente une méthode visit qui vérifie si la versioning du bucket s3 est activée.

Ici, elle lance une erreur, mais vous pourriez tout aussi facilement modifier le construct pour activer la versioning.

Tout ce qui est appliqué à la pile, c'est-à-dire chaque construct dans la pile, est évalué par cette méthode visit.

C'est pourquoi nous devons vérifier l'instance du nœud évalué pour nous assurer qu'il s'agit du CFN bucket.

Les nœuds finiront tous par être le construct de niveau un de la ressource en question.

Même si vous utilisez un construct de bucket de niveau deux dans votre code de pile.

Pour les meilleures pratiques, AWS divise ses recommandations de meilleures pratiques en quatre domaines différents.

Organisation, codage, construct et application.

Pour les meilleures pratiques d'organisation, AWS recommande d'avoir une équipe d'experts CDK aider à établir des normes et à former ou mentor des développeurs dans l'utilisation de CDK.

Cela ne doit pas être une grande équipe.

Cela pourrait être aussi petit qu'une ou deux personnes ou cela pourrait être un centre d'excellence si vous avez une grande organisation.

AWS recommande également la pratique de déployer dans plusieurs comptes AWS.

Par exemple, avoir des comptes de production, de QA et de développement séparés.

Vous devriez utiliser des outils d'intégration continue et de déploiement continu comme CDK pipelines pour déployer au-delà des comptes de développement.

Pour les meilleures pratiques de codage, AWS recommande de n'ajouter de la complexité que là où vous en avez réellement besoin.

Ne concevez pas pour tous les scénarios possibles dès le départ.

Donc le principe keep it simple, stupid.

Il recommande également d'utiliser le framework well architected. Les applications AWS CDK sont un mécanisme pour codifier et livrer les meilleures pratiques well architected.

En suivant ces principes, vous pouvez créer et partager des composants qui les implémentent.

Plus tôt, j'ai déclaré qu'il est possible d'avoir plusieurs applications dans un projet, ce qui est vrai, mais ce n'est pas recommandé.

La meilleure pratique est de ne pas faire cela et de n'avoir qu'une seule application par dépôt.

Dans un monde CI CD, les changements d'une application pourraient déclencher inutilement le déploiement d'une autre application, même si elle n'a pas changé.

Enfin, votre code CDK et le code qui implémente votre logique d'exécution doivent être dans le même package.

Ils n'ont pas besoin de vivre dans des dépôts ou des packages séparés.

Pour les meilleures pratiques de construct, vous devriez construire des constructs de vos unités logiques de code.

Si vous construisez régulièrement des sites web avec des buckets s3, des API gateways et des lambdas, faites-en un construct et utilisez ensuite le construct dans votre pile.

C'est une mauvaise pratique d'utiliser des recherches de variables d'environnement dans vos constructs.

Les recherches de variables d'environnement doivent se faire au niveau supérieur d'une application CDK, puis être passées aux piles et aux constructs en tant que propriétés.

En utilisant des recherches de variables d'environnement, et des constructs, vous perdez la portabilité et rendez vos constructs plus difficiles à réutiliser.

Si vous évitez les recherches de réseau pendant la synthèse et modélisez toutes vos étapes de production en code, vous pouvez exécuter une suite complète de tests unitaires au moment de la construction de manière cohérente dans tous les environnements.

Faites attention à la manière dont vous factorisez votre code, ce qui peut entraîner des changements dans l'ID logique.

L'ID logique est dérivé de l'ID que vous spécifiez lorsque vous instanciez un construct, et de la position du construct dans l'arbre de l'application.

Changer l'idée logique d'une ressource entraîne le remplacement de la ressource par une nouvelle lors du prochain déploiement, ce que vous ne voulez presque jamais.

Les constructs sont géniaux, mais ils ne sont pas conçus pour faire respecter la conformité.

La conformité est mieux adaptée à l'utilisation des politiques de contrôle de service et des limites de permission.

Pour les meilleures pratiques d'application, prenez vos décisions au moment de la synthèse.

N'utilisez pas les conditions et paramètres de cloud formation.

Par exemple, une pratique courante de CDK consistant à itérer sur une liste et à instancier un construct pour chacun n'est pas possible en utilisant les expressions CloudFormation.

Traitez CloudFormation comme un détail d'implémentation et non comme une cible de langage.

Vous n'écrivez pas de modèles CloudFormation, vous écrivez du code qui génère ceux-ci.

Si vous omettez les noms des ressources, CDK les générera pour vous.

Et il le fera de manière à ne pas causer de problèmes lorsque vous finirez par refactoriser votre code plus tard.

CDK fait de son mieux pour vous empêcher de perdre des données en définissant par défaut des politiques qui conservent tout ce que vous créez.

Mais Cloud watch est cher.

Passez en revue et définissez vos propres politiques de conservation.

CDK dispose également de méthodes d'assistance qui videront un bucket s3 en utilisant une ressource personnalisée avant de détruire une pile, ce qui est très utile.

Envisagez de garder les ressources avec état comme les bases de données dans une pile séparée des ressources sans état.

Vous pouvez activer la protection contre la terminaison pour les piles avec état, tout en la gardant désactivée pour les piles sans état.

Les ressources avec état sont plus sensibles au renommage des constructs, ce qui est une autre raison de les garder dans une pile séparée.

Cela réduit le risque lorsque vous réorganisez votre application plus tard.

Le déterminisme est la clé des déploiements CDK réussis.

Le contexte CDK est un mécanisme pour enregistrer un instantané des valeurs non déterministes provenant de la synthèse.

Cela permet aux opérations de synthèse futures de produire le même modèle exact.

Les valeurs non déterministes résultent de l'utilisation de choses comme des constructs à partir de la recherche où vous recherchez une ressource externe.

Ces valeurs de LOOKUP sont mises en cache dans CDK context dot JSON.

Les méthodes de commodité d'octroi vous permettent de simplifier grandement le processus IAM.

La définition manuelle des rôles ou l'utilisation de rôles prédéfinis dans votre compte AWS entraîne une grande perte de flexibilité dans la conception de vos applications.

Les politiques de contrôle de service et les limites de permission sont de meilleures alternatives aux rôles prédéfinis.

Une autre meilleure pratique de CDK est de créer une pile pour chaque environnement.

Lorsque vous synthétisez votre application, l'assemblage cloud créé dans le dossier CDK dot out contient un modèle séparé pour chaque environnement.

Votre build entier est déterministique.

La plupart des constructs de niveau deux dans CDK ont des méthodes de commodité pour aider à la création de métriques, que vous pouvez facilement utiliser pour générer des tableaux de bord et des alarmes CloudWatch, utilisez-les.

Enfin, il y a quelques autres ressources que je voudrais mentionner.

Free Code Camp a un excellent article de blog sur la façon d'utiliser CDK version deux pour créer une application serverless à trois niveaux.

J'ai plusieurs articles sur mon blog liés à CDK, mais l'un en particulier montre à quel point l'utilisation d'un langage de programmation général permet d'étendre encore plus le CDK.

Dans mes spécifications Open API à partir de CDK.

Sans déployer d'abord l'article, je montre comment vous pouvez parcourir la structure des endpoints d'une API gateway pendant la synthèse pour produire une spécification Open API en premier sans déployer.

Enfin, le framework serverless stack est assez génial.

Il étend le CDK et permet le développement local de lambda.

Il a une console assez géniale pour l'observabilité lors du développement.

Cela vaut définitivement la peine de vérifier si vous êtes arrivé jusqu'ici dans la leçon, merci d'avoir regardé.

Merci.

Vous pouvez me suivre sur Twitter à marks codes.

Et mes autres réseaux sociaux et mes articles de blog sont situés à marks dot codes.

C'était un Free Code Camp CDK Crash Course.

Merci, au revoir.