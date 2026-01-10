---
title: Créer et déployer de l'IaC en discutant avec une IA
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2023-11-01T13:39:47.000Z'
originalURL: https://freecodecamp.org/news/create-and-deploy-iac-by-chatting-with-ai
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/iacai.jpg
tags:
- name: '#IaC'
  slug: iac
- name: youtube
  slug: youtube
seo_title: Créer et déployer de l'IaC en discutant avec une IA
seo_desc: Infrastructure as Code (IaC) is a revolutionary approach to managing and
  provisioning computing infrastructure. With IaC, you can automate the process of
  provisioning, configuring, and managing infrastructure using code and software development
  techn...
---

L'infrastructure en tant que code (IaC) est une approche révolutionnaire pour gérer et provisionner l'infrastructure informatique. Avec l'IaC, vous pouvez automatiser le processus de provisionnement, de configuration et de gestion de l'infrastructure en utilisant du code et des techniques de développement logiciel. Cette approche offre une méthode plus efficace, cohérente et fiable pour gérer l'infrastructure par rapport aux méthodes manuelles traditionnelles.

Bien que l'IaC offre de nombreux avantages, il peut parfois être difficile de naviguer dans la complexité des propriétés de configuration et la variété des fonctions et commandes nécessaires pour déployer l'infrastructure. C'est là que l'intelligence artificielle (IA) entre en jeu. L'IA a le potentiel de simplifier considérablement le processus de déploiement de l'infrastructure en automatisant de nombreuses tâches complexes et fastidieuses impliquées dans l'IaC.

Nous venons de publier un cours sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à utiliser l'IA pour créer et déployer de l'IaC. Dans ce cours, vous apprendrez à utiliser les outils d'IA développés par Pulumi, une entreprise qui a fourni une subvention pour rendre ce cours possible.

À travers une série de démonstrations et d'exemples pratiques, nous vous guiderons dans le processus de création d'un projet web simple pour vous donner une idée de la puissance des outils d'IA. Nous approfondirons ensuite le concept d'infrastructure en tant que code (IaC) et vous enseignerons les bases de l'utilisation de Pulumi.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/image-3.png)
_Interface web de Pulumi AI._

Vous apprendrez à utiliser Pulumi AI pour développer de l'infrastructure, même si vous ne possédez pas les connaissances techniques des étapes exactes impliquées. De plus, nous démontrerons comment l'IA peut vous aider à rechercher dans toutes vos ressources d'infrastructure, simplifiant ainsi le processus de mise à jour.

L'adaptabilité de Pulumi AI aux entrées en langage naturel peut augmenter considérablement la productivité. Par exemple, vous pouvez entrer une requête de base comme "Montrez-moi comment exécuter nginx en tant que tâche ECS Fargate dans le VPC par défaut", et Pulumi AI traitera la demande et fournira une solution qui référence les ressources et fournisseurs AWS nécessaires. Cette adaptabilité montre la puissance et la commodité de l'utilisation de l'IA dans le domaine du développement web et du déploiement d'infrastructure.

Au sein de l'écosystème Pulumi, il existe plus de 130 fournisseurs. Certains de ces fournisseurs, comme AWS, offrent plus de 1000 ressources. En moyenne, chacune de ces ressources peut avoir environ 30 propriétés de configuration. Étant donné le grand nombre de configurations potentielles, il peut parfois être difficile de tout configurer parfaitement. C'est là que Pulumi AI se révèle utile.

Regardez le cours complet sur la chaîne YouTube freeCodeCamp.org (1 heure de visionnage).

%[https://youtu.be/ywLxbDV9TBU]

### Transcription

(générée automatiquement)

Je suis Beau Carnes de FreeCodeCamp.org, et dans ce cours, je vais vous montrer comment vous pouvez utiliser l'IA pour simplifier le déploiement d'infrastructures et de sites web.
Lors de la création et du déploiement en utilisant l'infrastructure en tant que code, il peut parfois être difficile de garder une trace de toutes les propriétés de configuration et des fonctions et commandes que vous devez utiliser.
Eh bien, maintenant l'intelligence artificielle peut vous aider avec toutes ces choses.
Je vais vous montrer comment utiliser les outils d'IA créés par Pulumi.
Pulumi a fourni une subvention pour rendre ce cours possible.
Tout d'abord, je vais démontrer comment créer un projet web simple afin que vous puissiez rapidement comprendre la puissance de ces outils d'IA.
Ensuite, j'expliquerai plus en détail l'infrastructure en tant que code et vous montrerai les bases de l'utilisation de Pulumi.
Après cela, je démontrerai comment il est possible d'utiliser Pulumi AI pour développer de l'infrastructure, même si vous ne connaissez pas les étapes exactes vous-même.
Et enfin, je démontrerai comment vous pouvez utiliser l'IA pour vous aider à rechercher dans toutes vos ressources d'infrastructure afin de simplifier les mises à jour.
D'accord, commençons.
Je vais vous montrer comment utiliser Pulumi AI pour créer rapidement un bucket S3 et un site web.
Je vais simplement montrer un exemple rapide pour l'instant.
Mais plus tard dans ce cours, je vous montrerai des exemples beaucoup plus compliqués sur la façon d'utiliser Pulumi AI pour l'infrastructure en tant que code.
Mais pour l'instant, je vais simplement faire MPX, Pulumi AI.
J'ai précédemment configuré Pulumi sur mon ordinateur et également attaché AWS à Pulumi.
J'aurai un lien vers les instructions pour faire cela dans la description.
Alors maintenant, que veux-je construire ?
Eh bien, je veux construire un bucket S3.
Et je peux simplement utiliser l'anglais normal.
Il se connecte également à chat GPT ou à l'API open AI pour pouvoir gérer l'anglais simple.
Mais il peut également se connecter avec Pulumi.
Et je viens de créer un bucket.
Si je vais dans ma console AWS, et nous voyons le bucket, il est bien dans la console maintenant.
D'accord, maintenant que nous avons le bucket, ajoutons quelque chose au bucket.
Ajoutons donc un fichier index.html avec un simple jeu de devinette de nombres.
D'accord, maintenant je vais simplement demander quelle est l'URL.
D'accord, maintenant je peux simplement copier cette URL et accès refusé.
C'est en fait assez facile à corriger, je peux aller dans mon bucket ici, c'est juste à cause des permissions qui sont définies par défaut pour bloquer tout accès public.
Je vais donc simplement débloquer l'accès public.
Et ensuite, je vais aller dans index.html pour définir la permission de celui-ci.
Et ensuite, nous allons également descendre ici et activer ACL.
Ensuite, nous pouvons éditer cela.
Nous aurons donc la lecture et la liste, et je pense que les objets peuvent être rendus publics en utilisant ACL.
Maintenant, vous n'aurez peut-être pas à faire tout cela si vous l'avez déjà configuré au préalable.
Selon la façon dont vous avez configuré AWS, Pulumi peut simplement le rendre public par défaut.
Mais si vous ne l'avez pas configuré correctement, comme je ne l'avais pas configuré, vous devrez peut-être rendre tout public manuellement.
D'accord, laissez-moi simplement retourner sur le site web.
Maintenant, celui-ci l'a simplement fait de sorte que je n'ai pas réellement à entrer le nombre, je dois simplement continuer à essayer jusqu'à ce que nous obtenions le bon nombre.
En fait, je ne pense pas que ce code fonctionne du tout.
Alors voyons si nous pouvons mettre à jour le code, refaire complètement le jeu de devinette de nombres à partir de zéro.
Habituellement, vous n'allez pas avoir à coder quelque chose à partir de cela, vous allez avoir à créer de l'infrastructure.
Mais je voulais simplement montrer cet exemple de la façon dont nous pouvons réellement créer un code également.
Vous allez simplement expérimenter avec cela.
Si vous pouvez réellement créer un site web comme celui-ci, alors vous pourriez également lui dire, Oh, ajoutez du style, et ensuite il peut ajouter un style supplémentaire au site web.
Mais maintenant, passons à autre chose.
Dans cette section, je vais donner un bref aperçu de l'infrastructure en tant que code.
Après cela, je vais passer en revue les bases de Pulumi.
Et enfin, je vais démontrer comment utiliser l'IA pour simplifier et rationaliser votre infrastructure en tant que code.
N'hésitez pas à avancer si vous connaissez déjà les bases de l'infrastructure en tant que code.
L'infrastructure en tant que code est donc la pratique de gestion et de provisionnement de l'infrastructure par le biais de fichiers de définition lisibles par machine, plutôt que d'utiliser la configuration matérielle physique ou des outils de configuration interactifs.
À l'ère du cloud computing, l'infrastructure en tant que code joue un rôle pivot en garantissant que l'infrastructure est cohérente, reproductible et évolutive.
Traditionnellement, l'infrastructure était gérée manuellement par des administrateurs système configurant chaque serveur individuellement.
À mesure que l'échelle des opérations augmentait, cette approche est devenue inefficace et sujette aux erreurs.
Le besoin d'automatisation a conduit à la naissance des outils de gestion de configuration et au concept d'infrastructure en tant que code.
Voici quelques-uns des concepts et principes clés derrière l'infrastructure en tant que code.
Le premier est l'idempotence.
Cela signifie la capacité à exécuter le même code plusieurs fois sans changer le résultat après la première exécution.
Le concept suivant est l'immuabilité.
Les composants d'infrastructure ne sont jamais modifiés après leur déploiement.
Si des changements sont nécessaires, une nouvelle infrastructure est provisionnée et les anciennes sont abandonnées.
Le principe clé final est l'approche déclarative par rapport à l'approche impérative.
Alors qu'une approche déclarative spécifie l'état final souhaité, comme je veux un serveur, une approche impérative spécifie les étapes pour atteindre l'état final, comme créer un serveur, puis installer le logiciel x avec l'infrastructure en tant que code, les changements d'infrastructure sont effectués de manière systématique et reproductible, réduisant les erreurs manuelles.
Cela permet également le contrôle de version, garantissant que tous les membres de l'équipe travaillent avec les mêmes configurations.
Certains des outils populaires d'infrastructure en tant que code sont Terraform, qui est un outil qui permet aux utilisateurs de définir l'infrastructure en tant que code en utilisant un langage de configuration déclaratif qui est un langage spécifique de domaine propriétaire.
Ansible est un outil d'automatisation open source pour la gestion de configuration, le déploiement d'applications et l'automatisation des tâches.
Graph et Puppet sont des outils de gestion de configuration qui permettent de définir l'infrastructure en tant que code et de l'automatiser.
Pulumi est un outil open source qui offre la flexibilité d'utiliser n'importe quel langage de programmation pour gérer l'infrastructure.
Cela rend Pulumi largement accessible aux développeurs et ingénieurs DevOps de tout horizon.
Et nous parlerons plus de Pulumi plus tard.
Certaines des meilleures pratiques pour l'infrastructure en tant que code sont de modulariser les configurations pour s'assurer qu'elles sont réutilisables, de tester et valider régulièrement les scripts d'infrastructure en tant que code pour s'assurer qu'ils fonctionnent comme prévu, et de documenter les configurations pour la clarté et la référence future.
Regardons rapidement un exemple de code pour l'infrastructure en tant que code, nous passerons en revue le code plus en détail plus tard, je voulais simplement que vous voyiez que c'est ainsi que vous utiliseriez Pulumi pour configurer des instances EC2 dans AWS en utilisant Python, la ligne pour les structures de code offre de nombreux avantages, il est essentiel de gérer les secrets de manière sécurisée, de garantir la sécurité de l'infrastructure et de gérer la dérive potentielle de l'infrastructure, où l'état réel diverge de l'état souhaité, l'infrastructure en tant que code révolutionne la façon dont nous pensons et gérons l'infrastructure.
À mesure que le paysage technologique continue d'évoluer, l'adoption de l'infrastructure en tant que code et le fait de rester à jour avec ses meilleures pratiques seront cruciaux pour les organisations visant l'efficacité et l'évolutivité.
Maintenant, plongeons dans Pulumi.
Alors, qu'est-ce que Pulumi ?
Pulumi est une plateforme d'infrastructure en tant que code conçue pour les développeurs et les ingénieurs cloud qui souhaitent utiliser des langages de programmation polyvalents pour définir et gérer les ressources cloud.
Contrairement aux outils traditionnels d'infrastructure en tant que code qui utilisent des langages spécifiques de domaine, Pulumi permet aux utilisateurs de tirer parti de langages de programmation populaires, tels que Go, JavaScript ou TypeScript, Python et les plateformes .NET.
Pulumi fonctionne avec l'infrastructure traditionnelle comme les machines virtuelles, les réseaux et les bases de données, en plus des architectures modernes, y compris les conteneurs, les clusters Kubernetes et les fonctions serverless.
Pulumi prend en charge des dizaines de fournisseurs de services cloud, nous utiliserons Python et déployerons sur AWS, bien que cela puisse être fait avec d'autres langages de programmation et fournisseurs de cloud.
Regardons les composants clés de Pulumi.
L'un est les SDK de fournisseurs.
Ce sont des packages installables que votre programme consomme.
Pulumi prend en charge plus de 75 fournisseurs, avec de nouveaux ajoutés régulièrement.
L'interface de ligne de commande est un outil que les utilisateurs peuvent utiliser pour exécuter des prévisualisations et des mises à jour sur leurs programmes d'infrastructure.
Le backend de service est le service de stockage d'état par défaut pour tous les projets Pulumi.
Cela stocke une capture de l'état de vos ressources, connue sous le nom de point de contrôle chaque fois que vous mettez à jour vos ressources cloud en utilisant Pulumi.
Alors, regardons comment Pulumi fonctionne.
Il fonctionne en traitant le code écrit dans l'un des langages pris en charge et en générant un graphe des ressources qui doivent être créées, mises à jour ou supprimées.
Ce graphe est ensuite utilisé pour calculer l'ensemble des opérations CRUD nécessaires pour atteindre l'état souhaité de l'infrastructure.
Voici quelques-unes des principales fonctionnalités, les ressources de composants.
Ce sont des ressources qui encapsulent plusieurs ressources enfants, permettant aux utilisateurs de représenter plusieurs ressources connexes en tant qu'unité unique, les références de pile.
Cette fonctionnalité permet aux utilisateurs de créer plusieurs piles et de consommer les sorties exportées par d'autres piles en amont.
Fournisseurs dynamiques.
Cette fonctionnalité sert de solution de secours pour lorsqu'il n'y a pas de fournisseur officiel pour une ressource.
API d'automatisation.
Cette API permet aux utilisateurs d'invoquer programmatiquement les opérations CLI, permettant des scénarios de déploiement avancés.
Pulumi Insights apporte l'intelligence à l'infrastructure cloud en utilisant Pulumi.
Il comprend des fonctionnalités comme Pulumi AI, qui est un assistant IA génératif conçu pour créer une infrastructure cloud en utilisant le langage naturel, et Pulumi Resource Search, qui offre une recherche et une analyse multi-cloud sur chaque ressource cloud et environnement et organisation.
Bientôt, je montrerai comment utiliser ces deux outils.
Avec l'introduction de nouvelles commandes CLI, Pulumi Insights est désormais plus accessible aux utilisateurs, leur permettant de tirer parti de l'IA et de la recherche de ressources directement depuis le terminal.
Le modèle de programme de Pulumi commence avec le projet Pulumi à la couche la plus externe.
Cependant, les utilisateurs n'interagissent pas souvent directement avec ces projets.
Ils sont généralement créés lors de l'initialisation d'un programme Pulumi et tendent à disparaître lorsque la dernière pile au sein du projet est détruite.
À l'intérieur du projet, il y a un programme, qui est le point d'entrée principal du programme.
Si vous utilisez TypeScript, il s'agit de index.ts.
Donc, ce serait le programme, le programme principal.
C'est là que nous définissons notre infrastructure.
L'infrastructure est caractérisée par les ressources Pulumi.
Un exemple de ressource Pulumi est un bucket S3 AWS.
De telles ressources ont à la fois des entrées et des sorties.
Par exemple, spécifier le nom d'un bucket serait une entrée, tandis que le nom de la ressource Amazon du bucket ou ARN serait une sortie.
Un motif récurrent que vous remarquerez dans un programme Pulumi est la façon dont la sortie d'une ressource devient l'entrée d'une autre.
Si vous avez un bucket S3 et souhaitez définir une politique pour celui-ci, la sortie ARN du bucket servira d'entrée à la politique du bucket.
En coulisses, Pulumi gère les dépendances entre ces ressources, garantissant qu'elles sont configurées ou supprimées efficacement.
Il suit également la séquence dans laquelle les opérations doivent être exécutées.
En plus du programme, il y a aussi le concept de piles.
Une pile est essentiellement une instance de votre programme Pulumi, avec la flexibilité supplémentaire de fournir différentes valeurs de configuration pour différentes instances.
Cela est utile lorsque vous souhaitez avoir des configurations séparées pour les environnements de développement, de QA et de production.
Par exemple, dans un environnement de développement, vous pourriez opter pour des instances EC2 moins nombreuses ou moins puissantes par rapport à un environnement de production.
Cette différenciation est réalisée en utilisant la configuration de pile.
En discutant de l'architecture physique de Pulumi au niveau fondamental, nous avons nos programmes Pulumi.
Ces programmes peuvent être écrits dans divers langages, tels que Python, TypeScript, JavaScript, Go, C#, F# et Java.
Pulumi offre également un support pour YAML, principalement pour les grandes organisations passant à Pulumi à grande échelle.
Ces options s'adressent à ceux qui ont une expérience traditionnelle des opérations, qui pourraient trouver plus confortable de travailler avec YAML qu'avec des langages de programmation standard.
Le moteur Pulumi interprète votre programme Pulumi.
Le moteur Pulumi fonctionne en comparant l'état souhaité de vos programmes Pulumi avec l'état existant tel qu'enregistré dans votre fichier d'état, il identifie les divergences entre les deux et détermine quelles ressources doivent être créées, mises à jour ou supprimées.
Ce processus est facilité par les fournisseurs Pulumi.
Par exemple, dans notre exemple, nous avons mentionné le fournisseur AWS Pulumi et le fournisseur Kubernetes.
Ces fournisseurs offrent un support pour une multitude de clouds publics, de fournisseurs de logiciels en tant que service et d'autres plateformes.
Cette vaste gamme de fournisseurs garantit que les utilisateurs peuvent tirer parti de l'approche déclarative de Pulumi pour gérer les ressources sur un large éventail de services.
Maintenant, nous allons donner un bref exemple sur la façon d'utiliser Pulumi.
Ensuite, nous verrons comment utiliser les fonctionnalités d'IA.
Nous commencerons avec un répertoire vide, et nous initialiserons un programme Pulumi en utilisant la commande Pulumi new.
Lors de l'exécution de cette commande, de nombreux modèles sont affichés.
Il y en a beaucoup, il y en a 221.
Et je vais simplement aller au site web statique, AWS TypeScript.
Donc, il s'agit simplement d'un programme TypeScript pour déployer un site web statique sur AWS.
Donc, je vais mettre TypeScript AWS pour le nom du projet, la description du projet par défaut, le nom de la pile par défaut, je vais simplement utiliser cette région, qui est en fait assez proche de moi, us-west-2.
Et le reste de cela sera simplement gardé par défaut.
Donc, ces invites sont spécifiques à ce modèle, car il configure un site statique.
Après l'initialisation, le système exécute un npm install, qui sera familier à toute personne ayant de l'expérience avec node.js.
Maintenant, après l'installation, notre répertoire de projet révèle plusieurs fichiers et dossiers, nous avons un dossier node_modules, où node.js stocke les dépendances, un dossier www créé par le projet pour héberger nos fichiers de site web, le fichier git ignore.
Mais d'abord, discutons du fichier Pulumi.yaml.
Ce fichier contient les détails de configuration du projet.
Souvenez-vous, lorsque nous utilisons la commande Pulumi new et fournissons certaines entrées, ces réponses sont enregistrées dans ce fichier.
De plus, nous avons un fichier Pulumi.dev.yaml, qui est la configuration de la pile.
Nous déployons notre site statique dans différentes régions, nous pouvons créer des piles séparées avec leurs fichiers de configuration respectifs.
Donc, passons au fichier index.ts, laissez-moi le déplacer ici.
C'est le cœur de notre programme Pulumi.
Il commence par importer des bibliothèques, comme le SDK Pulumi, qui nous permet d'accéder à nos valeurs depuis notre fichier de configuration, et également le fournisseur AWS, qui va créer des ressources AWS, et un composant Pulumi appelé sync folder pour synchroniser un dossier avec notre stockage d'objets.
Ce fichier démontre également le motif d'utilisation de la sortie d'une ressource comme entrée d'une autre ressource.
Donc, je ne vais pas passer ce fichier en revue en détail complet, mais vous pouvez voir comment il crée un bucket S3.
Il configure les contrôles de propriété, configure le bloc ACL, et utilise le dossier de synchronisation dont nous avons parlé, créant un CDN Cloudflip pour distribuer le CAS sur le site web.
Donc, il s'agit simplement du modèle, et nous pouvons modifier ce modèle comme nous le souhaitons.
Et ensuite, il va simplement exporter l'URL et le nom d'hôte vers le bucket et la distribution.
Dans cet exemple, les détails d'un bucket S3 comme ses contrôles de propriété peuvent référencer une autre ressource.
Le fichier procède à la définition de diverses ressources liées au bucket et définit le dossier de synchronisation pour refléter le contenu de notre dossier www avec le bucket S3 et établit une distribution cloud front.
Et ensuite, comme nous en avons déjà parlé ici, c'est là qu'il se termine par la définition des sorties de pile en utilisant une instruction d'exportation TypeScript standard, permettant un accès externe à certaines valeurs de notre programme Pulumi.
Pour voir l'impact des configurations, nous utiliserons la commande Pulumi up.
Donc, laissez-moi revenir à la console ici.
Et nous allons faire Pulumi up.
Cela signifie mise à jour, la commande prévisualise les changements avant notre exécution réelle, garantissant que nous sommes conscients des actions que Pulumi prévoit de prendre.
Donc, c'est là qu'il confirmera si nous voulons effectuer la mise à jour.
Et je vais dire Oui, c'est ce que nous voulons faire.
Donc, après avoir tout terminé, nous pouvons vérifier le site web.
Donc, voici l'URL.
Et je vais simplement suivre le lien.
Et ça marche.
Bonjour, Pulumi ou Bonjour le monde déployé par Pulumi.
Laissez-moi vous montrer une chose de plus très rapidement.
Voyons ce qui se passe si je fais un changement.
Par exemple, je peux aller ici et je vais changer le TTL par défaut à 300.
Et ensuite je vais simplement enregistrer cela.
Et ensuite je vais simplement faire Pulumi up à nouveau.
Et vous verrez qu'il ne recréera pas chaque ressource.
Il ne fait que la mise à jour.
C'est ce que cela signifie que Pulumi est déclaratif.
Je vais dire voulez-vous effectuer la mise à jour ?
Vous dites simplement votre état souhaité et Pulumi déterminera ce qui doit être mis à jour.
Et enfin, nous pouvons utiliser la commande Pulumi destroy pour supprimer les ressources.
Ainsi, nous n'aurons plus de frais.
Donc oui, je veux détruire cela.
Et cela va simplement tout supprimer d'AWS.
Donc, si je retourne simplement à la page et que je rafraîchis, il n'y a rien là, nous obtenons le 403 interdit.
Maintenant, je vais aller à une autre page, Pulumi.com slash AI.
Nous allons parler de Pulumi AI.
Pulumi AI est accessible à Pulumi.com slash AI.
C'est gratuit pour tout le monde.
Au sein de l'écosystème Pulumi, il existe plus de 130 fournisseurs.
Certains de ces fournisseurs, comme AWS, offrent plus de 1000 ressources.
En moyenne, chacune de ces ressources peut avoir environ 30 propriétés de configuration.
Étant donné le grand nombre de configurations potentielles, il peut parfois être difficile de tout configurer parfaitement.
C'est là que Pulumi AI se révèle utile.
Pour démontrer, je vais simplement mettre une invite de base ici, je vais dire montrez-moi comment exécuter nginx en tant que tâche ECS Fargate dans le VPC par défaut.
Donc, il s'agit d'une invite en langage naturel.
Et vous voyez, j'ai simplement choisi TypeScript comme langage préféré, mais j'aurais pu choisir un autre langage.
Et vous pouvez voir qu'il génère simplement le programme.
Cela a pris une minute pour le traiter.
Vous pouvez voir que la réponse commence souvent par répéter l'invite ou la question initiale, ce qui crée une boucle de rétroaction interne, améliorant ainsi la qualité de la solution fournie.
Et nous pouvons voir tout ce qu'il suggère, comme l'utilisation du cluster ECS, il crée une définition de tâche ECS.
Et cela crée un service Fargate.
Et il passe essentiellement en revue et fait ce que nous lui avons demandé de faire.
Et ensuite, il résume essentiellement ce qu'il va faire.
Et ensuite, il vous donne simplement quelques choses différentes que vous pouvez changer, vous pouvez remplacer nginx latest par n'importe quelle image Docker de votre choix, il a été dans votre propre compte AWS, et ensuite explique simplement un peu plus.
Donc, nous pouvons simplement copier cela.
Et ensuite, je peux le mettre directement ici.
Et ensuite, vous pouvez voir qu'il y a quelques lignes ondulées ici.
Donc, c'est un processus itératif.
En fait, il n'est pas rare de rencontrer quelques erreurs.
Et ces outils, bien que puissants, ne donnent pas toujours des résultats parfaits.
Donc, les utilisateurs doivent s'attendre à un certain degré d'itération et d'affinement.
Donc, je peux regarder ici, il dit propriété rapide.
Donc, je peux simplement copier cela.
Et je vais l'apporter ici, je vais dire erreur, et je vais simplement coller l'erreur.
Et maintenant, il va la corriger pour moi, il va la mettre à jour.
Et il réalise que dans les versions plus récentes de plume, la définition de test doit être créée différemment.
D'accord, maintenant essayons de copier ce code mis à jour, je ne l'ai pas copié correctement.
Essayons à nouveau.
Cliquez sur ce bouton de copie.
D'accord, maintenant nous n'avons plus les lignes ondulées rouges ici.
Et vous pouvez voir que nous pouvons simplement passer en revue tout cela et simplement dire ce qui ne va pas et le faire corriger.
Donc, en fait, nous pouvons aller et venir comme je l'ai dit, c'est un processus itératif.
Et bien que cela ne produise pas des résultats parfaits du premier coup, ils peuvent fournir un excellent point de départ, souvent autour de 80% de précision, ce qui réduit considérablement le temps et l'effort nécessaires.
Ces outils sont particulièrement bénéfiques lorsqu'il s'agit de rappeler des configurations ou des procédures spécifiques qui ne sont pas utilisées de manière routinière.
Par exemple, si l'on doit rédiger une politique IAM pour accéder à un secret, mais que l'on ne se souvient pas des étapes exactes, des outils comme plume AI peuvent fournir une solution rapide et précise.
Plume AI est un outil puissant qui peut accélérer considérablement l'apprentissage et les applications des tâches de codage.
Maintenant, essayons un exemple plus complexe.
Ensuite, nous suivrons jusqu'à la création des ressources réelles ici, ici, nous ne allons pas réellement exécuter ce programme, mais le suivant, nous le ferons.
Donc, laissez-moi aller ici, et je vais simplement créer une nouvelle conversation en allant simplement sur plume.com slash AI à nouveau.
Maintenant, je veux créer une chaîne de fonctions serverless.
Essentiellement, je veux déployer une série de fonctions serverless qui se déclenchent les unes les autres dans un ordre spécifique.
Essentiellement, des fonctions AWS lambda qui déclenchent une autre fonction lambda et ainsi de suite.
Donc, le type d'architecture que je cherche à créer est idéal pour les tâches séquentielles, où le résultat d'un processus détermine l'entrée du processus suivant.
Maintenant, nous allons simplement faire une chaîne de fonctions très simple, ce ne sera pas comme une situation réelle.
Mais je peux vous donner un exemple de ce que vous pouvez faire avec plume AI, les chaînes de fonctions ou ce que l'on appelle parfois les pipelines ou séquences de fonctions, peuvent rationaliser les processus multi-étapes en permettant à la sortie d'une fonction de servir d'entrée à la suivante, certaines applications réelles qui pourraient être utilisées pour le traitement des commandes e-commerce, où des étapes comme la validation des commandes, le paiement et les mises à jour de l'inventaire se produisent séquentiellement, et l'analyse des données, où les données brutes subissent des étapes de nettoyage, de transformation et d'analyse.
Également, peut-être comme les flux de travail d'inscription des utilisateurs, les systèmes d'approbation de documents, la surveillance des transactions financières.
Donc, lorsque vous avez un flux de travail modulaire, il peut offrir de la flexibilité, de l'évolutivité et de la facilité de dépannage, car chaque fonction peut être gérée et optimisée individuellement.
Comme je l'ai dit, artistes, cela pourrait être une chaîne de fonctions simple, la première fonction vérifiera le nombre de caractères.
Si le nombre de caractères est correct, la deuxième fonction sera déclenchée, qui dans la deuxième fonction transformera tous les caractères en lettres majuscules et déclenchera la troisième fonction, qui enregistrera la soumission de texte.
La vérité est que, même si c'est simple, je ne sais pas personnellement comment faire cela.
Donc, nous allons utiliser plume AI pour nous aider.
D'accord, alors voyons si nous pouvons comprendre cela.
Donc, je vais dire, aidez-moi à créer une fonction AWS Lambda qui traite du texte.
La première fonction vérifiera le nombre de caractères, si le nombre de caractères est supérieur à 50 et inférieur à 1000, alors la deuxième fonction est déclenchée.
La deuxième fonction transformera les caractères en lettres majuscules et déclenchera la troisième fonction.
La fonction finale enregistrera le texte sur AWS.
D'accord, voyons simplement ce qu'il peut comprendre à partir de cette instruction.
D'accord, il crée une chaîne de fonctions AWS Lambda qui décrit les opérations de traitement de texte, vérifie la longueur de la chaîne, transforme le texte et enregistre le résultat dans un bucket S3.
Donc, il va même développer la structure du programme, créer trois fonctions AWS Lambda.
Chaque fonction est écrite en JW et intégrée directement dans le programme plume.
Donc, nous n'avons pas à les stocker ailleurs, créer une passerelle API pour servir de déclencheur pour démarrer l'enchaînement des fonctions lambda à la demande de la passerelle API, la première lambda s'exécute pour vérifier la longueur du texte d'entrée, les choses d'avocat, le circuit de lien invoque une fonction de capitalisation qui convertit les caractères en majuscules et la fonction de capitalisation invoque la fonction d'enregistrement qui enregistre le texte modifié dans le bucket S3, puis l'URL finale pour déclencher le flux de travail est exportée.
D'accord, donc c'est exactement ce que nous voulions.
Donc, voyons ce qu'il a proposé.
Donc, nous avons le vérificateur de lien lambda, et il va le créer.
Vous pouvez voir qu'il vérifie la longueur de l'utilisation des 50 et des 1000, exactement comme nous l'avons dit, et ensuite il va invoquer la fonction de capitalisation, il va invoquer la fonction de capitalisation.
Donc, regardons la fonction de capitalisation, la fonction lambda de capitalisation.
Elle va faire les majuscules, elle va invoquer la fonction d'enregistrement.
La fonction d'enregistrement va enregistrer dans un bucket S3, cela peut ne pas fonctionner exactement correctement du premier coup.
Mais vérifions simplement cela et copions le code.
Je vais simplement le coller ici.
Et ensuite, essayons simplement de comprendre quelles sont les erreurs.
Donc, je peux en fait simplement copier cette erreur ici.
Et il dit que l'argument de type runtime n'est pas assignable à un paramètre de type function args.
D'accord, donc copions simplement cette erreur.
Et ensuite, nous allons revenir ici.
Et je vais le coller.
Donc, voyons ce qu'il comprend.
Il sait que nous avons besoin des propriétés de rôle pour spécifier le rôle IM.
Et AWS lambda suppose lorsqu'il exécute votre fonction, créons un nouveau rôle IM pour chacune de vos fonctions lambda.
Et cela configure les permissions IM.
D'accord, nous devons peut-être faire quelques permissions supplémentaires, changer les permissions dans AWS également.
Mais essayons cela.
D'accord, maintenant ce n'est pas, nous n'avons pas autant de lignes ondulées rouges.
Donc, oh, d'accord.
Nous, d'accord, je vois qu'il y a quelque chose qui ne va pas ici, car il suppose qu'il dit le reste de votre configuration lambda ici.
Donc, je vais revenir ici.
Ensuite, vous sortez le code complet dont j'ai besoin.
Et ensuite, je vais dire ne pas simplement dire en fait mettre la config la config.
Maintenant, nous pourrions probablement, je pense que je dois simplement combiner ces deux codes ensemble, ce que je pourrais faire manuellement.
Mais je vais voir si cela peut le faire.
Je vais sauter un peu de l'aller-retour.
Donc, vous pouvez voir le résultat.
C'est un processus itératif pour obtenir le code correct.
Et je suis entré dans cela en sachant très peu comment mettre en œuvre ce projet.
C'était tellement plus rapide en utilisant Pulumi AI.
D'accord, donc nous avons l'URL ici 123.
Mon nom est Bo.
Mon nom est Bo.
Et voyons si cela fonctionne.
D'accord, nous avons le lien ici.
Mais voyons si les mots en majuscules sont maintenant stockés dans notre bucket S3.
D'accord, voici notre bucket et le fichier txt.
Téléchargeons-le.
Et cela a fonctionné.
Voyez, j'ai simplement ajouté ce 123 et toutes les lettres sont en majuscules.
Nous l'avons fait.
Nous avons créé une chaîne de fonctions de l'une à l'autre.
Et encore une fois, je n'avais jamais fait quelque chose comme cela auparavant.
Mais j'ai pu utiliser Pulumi AI pour le comprendre.
C'est génial.
Et maintenant, je me sens tellement plus capable de pouvoir créer pratiquement n'importe quelle sorte d'infrastructure en tant que code.
Maintenant que j'ai Pulumi AI pour m'aider.
Maintenant, voyons comment nous pouvons rechercher dans nos ressources d'infrastructure et comment l'IA peut rendre le processus plus facile.
Donc, après avoir créé des tonnes de piles et de ressources, cela peut devenir difficile de les gérer et de les suivre toutes.
Donc, laissez-moi vous montrer comment cela peut devenir plus facile.
Eh bien, voici le tableau de bord cloud de Pulumi.
Et vous pouvez voir qu'il va me montrer les membres de l'organisation, vous avez généralement plus d'un nombre de piles, et ensuite le nombre de ressources pour les grandes organisations, le nombre de ressources peut être de milliers ou même de centaines de milliers de ressources, ce qui peut amener les utilisateurs à remettre en question la pertinence de ces ressources ou leur origine, ou si vous devez en nettoyer certaines.
Donc, nous pouvons utiliser la fonction de recherche de ressources.
Lorsque vous gérez une grande organisation avec de nombreuses personnes travaillant sur diverses piles, la fonction de recherche de ressources est inestimable.
Lorsque vous êtes sur ce tableau de bord principal, vous pouvez voir l'aperçu dont je parlais, vous pouvez même voir comme quand la dernière pile a été mise à jour.
Mais si je clique sur les ressources, alors nous pouvons rechercher dans toutes les ressources.
Donc, vous pouvez voir qu'il a simplement une liste de toutes les ressources sur chaque pile.
Et il y en a simplement un tas.
Et je peux simplement rechercher des choses, comme je peux rechercher API, et ensuite il montrera tout ce qui a API, ou je pourrais rechercher Kubernetes, cela ne fait apparaître qu'une seule chose liée à Kubernetes ici.
Et vous pouvez rechercher des choses par nom, gardé haut sage.
Et nous pouvons voir toutes les fonctions qui ont toutes les ressources qui ont le mot capitalizer.
Nous avons également le filtrage avancé.
Cela fournit des informations agrégées sur les ressources, nous pouvons rechercher selon divers critères, comme je peux faire tout ce qui a à voir avec AWS, ou cela rendra les choses un peu plus jolies.
Je peux faire tout ce qui a des fournisseurs fluides AWS.
Donc, c'est le type.
Et ensuite, je peux dire tout ce type dans ce projet.
Et donc, je peux encore affiner en fonction du type, des packages, des projets ou des piles, et vous pouvez en avoir beaucoup plus en fonction du nombre de ressources que vous avez.
Donc, la fonction de recherche est très polyvalente.
Je vais simplement chercher toutes les fonctions lambda.
Donc, la syntaxe de recherche puissante permet aux utilisateurs de faire des requêtes très complexes.
Mais il y a aussi une assistance IA intégrée.
Si je clique ici, je peux basculer en utilisant Pulumi AI.
Et cela peut aider les utilisateurs à formuler des requêtes, ce qui rend le processus de recherche encore plus convivial.
Donc, je peux dire quelque chose comme tous mes buckets S3.
Et ensuite, vous pouvez simplement dire des choses en utilisant un anglais conversationnel.
Ou je peux dire quelque chose comme, qui font partie de ma fonction lamb, la chaîne de fonctions.
Et il semble en obtenir beaucoup, franchement, je ne sais même pas comment il sait que ceux-ci font partie de la chaîne de fonctions Lambda, mais il semble qu'il en a obtenu beaucoup.
Sur l'interface utilisateur, il y a aussi une API robuste pour ceux qui souhaitent construire de l'automatisation et des outils autour de Stata.
Le système comprend également les permissions des utilisateurs.
Donc, en tant qu'administrateur de l'organisation, je peux voir toutes les ressources.
Mais pour les grandes organisations avec des exigences de permission spécifiques, les utilisateurs ne verront que les ressources auxquelles ils ont accès.
Cela garantit la sécurité et la confidentialité tout en fournissant des informations précieuses.
Donc, tous ces outils aident à fournir aux utilisateurs une vue complète et manuelle de leurs ressources Pulumi.
De plus, si vous avez votre propre entrepôt de données et des outils de business intelligence, vous pouvez intégrer les données avec les outils Pulumi avec vos solutions de données existantes.
D'accord, nous avons atteint la fin du cours, vous devriez maintenant être en mesure de commencer à utiliser l'IA pour créer une infrastructure plus facilement.
Merci d'avoir regardé.