---
title: GitHub Codespaces vs Gitpod – Le développement Full Stack passe dans le cloud
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-30T17:10:36.000Z'
originalURL: https://freecodecamp.org/news/github-codespaces-vs-gitpod-cloud-based-dev-environments
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-josh-sorenson-1154504.jpg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: codespaces
  slug: codespaces
- name: GitHub
  slug: github
- name: Gitpod
  slug: gitpod
- name: ide
  slug: ide
- name: Visual Studio Code
  slug: vscode
seo_title: GitHub Codespaces vs Gitpod – Le développement Full Stack passe dans le
  cloud
seo_desc: 'By Nader Dabit

  Gitpod and GitHub Codespaces are cloud based developer environments that allow you
  to spin-up high-performance, automated dev environments in seconds.

  Over the past few months I have gone down the rabbit hole of cloud-based developer
  e...'
---

Par Nader Dabit

[Gitpod](https://www.gitpod.io/) et [GitHub Codespaces](https://github.com/features/codespaces) sont des environnements de développement basés sur le cloud qui vous permettent de lancer des environnements de développement automatisés et haute performance en quelques secondes.

Au cours des derniers mois, je me suis plongé dans l'univers des environnements de développement basés sur le cloud. Je déplace plusieurs de mes projets vers le cloud afin que les développeurs puissent déployer les projets en un seul clic, comme [ce marché NFT full stack](https://github.com/dabit3/polygon-ethereum-nextjs-marketplace).

Cela a été particulièrement utile pour moi, en tant qu'enseignant et créateur de contenu aidant les développeurs à apprendre à coder. Maintenant, ces développeurs peuvent déployer les projets d'exemple sans avoir à configurer leurs environnements locaux, ce qui réduit les obstacles pour eux s'ils débutent.

C'est également un gain global de productivité et d'efficacité, car je n'ai plus besoin de cloner et de configurer des projets localement lors de mises à jour. Au lieu de cela, je peux simplement cliquer sur un bouton et c'est prêt à l'emploi.

Dans cet article, je vais partager ma vision de l'écosystème ainsi qu'une comparaison des deux options principales pour accomplir cela – GitHub Codespaces et Gitpod.

Pour la transparence, Gitpod est également un sponsor de [ma chaîne YouTube](https://www.youtube.com/naderdabit). Cela dit, je choisis uniquement d'accepter des sponsors de projets que j'utilise déjà et que j'apprécie.

## **Développement basé sur le cloud – C'est la voie à suivre**

En tant que développeurs, nous aimons automatiser les choses. Nous accélérons nos propres flux de travail, automatisons l'infrastructure et les pipelines CI/CD, et créons même des outils qui [écrivent du code eux-mêmes](https://copilot.github.com/).

Si vous regardez les pipelines logiciels modernes, il y a un domaine que nous n'avons pas automatisé : nos environnements de développement. Ils sont encore fragiles, liés aux machines locales, et nécessitent des efforts de configuration et de maintenance fastidieux qui nous distraient de notre créativité et de notre productivité.

Les environnements de développement sont une source constante de friction lors de l'intégration et du développement continu (vous souvenez-vous de votre dernière discussion "ça marche sur ma machine" ?).

En tant qu'enseignant et créateur de contenu aidant les nouveaux développeurs à apprendre à coder, l'un des problèmes les plus courants n'est pas le tutoriel ou le contenu lui-même. Plutôt, c'est que l'environnement local du développeur n'est pas configuré correctement, et ce n'est souvent même pas de leur faute.

Il existe d'innombrables variantes de systèmes d'exploitation et de versions d'applications qui doivent être prises en compte.

La douleur associée aux environnements de développement locaux ne fera qu'empirer avec le temps : des charges de travail plus importantes, plus de données, plus de dépendances, plus de tests, le développement multi-services et multi-pistes sont autant de choses difficiles à prendre en compte.

## **GitHub Codespaces et Gitpod mènent la danse des environnements de développement basés sur le cloud**

Il y a quelques années, Cloud9 s'est lancé dans ce domaine en tant que première génération d'IDE navigateur. Bien que leurs idées allaient dans la bonne direction, la technologie et la communauté n'étaient pas encore prêtes.

Beaucoup de choses ont changé depuis. En plus de l'avènement et de la montée fulgurante de VS Code, il y a eu de grands progrès dans la technologie des conteneurs et des machines virtuelles qui ont rendu plus rapide, plus sécurisé, scalable et pratique l'exécution d'environnements de développement dans le cloud.

Pas surprenant que nous voyions des entreprises comme Google, Facebook, Shopify et plus récemment GitHub passer entièrement au développement logiciel dans le cloud avec des solutions internes.

Il y a quelques acteurs dans ce domaine qui ont tiré parti de ces développements – bien que certains pourraient soutenir que d'autres solutions existantes se concentrent davantage sur le prototypage et les environnements de test pour des langages spécifiques et ne sont pas un remplacement complet du développement local.

En ce qui concerne les environnements de développement basés sur le cloud qui fonctionnent pour le développement logiciel professionnel au quotidien, il y a deux options principales : [Gitpod](https://www.gitpod.io/) et [GitHub Codespaces](https://github.com/features/codespaces).

Alors, que font-ils ? Eh bien, essentiellement, ils vous permettent de lancer des **environnements de développement basés sur des tâches** dans le cloud à partir de n'importe quel contexte Git. Une fois que vous avez terminé, vous les fermez simplement.

C'est un énorme gain de productivité. Pensez au développement multi-pistes (pas de changement des paramètres de l'environnement de développement lors du passage à un autre contexte pour examiner les pull-requests), à l'intégration, à la cohérence ou simplement au travail à distance. Vous pouvez travailler depuis n'importe quel ordinateur, Chromebook ou tablette.

Dans cet article, nous allons examiner de plus près et évaluer les deux produits selon les catégories suivantes :

* Flux de travail et collaboration
* IDE
* Runtime
* Automatisation
* Open Source & Écosystème
* Disponibilité & Tarification

Plongeons-nous dedans !

## GitHub Codespaces vs Gitpod : Flux de travail

GitHub Codespaces et Gitpod sont tous deux des services qui vous permettent de faire exactement la même chose que ce que vous pourriez faire localement sur une machine Linux, avec une addition majeure : votre environnement de développement peut être configuré en tant que code et est donc versionné, reproductible et automatisable.

GitHub Codespaces vous permet de le faire avec un fichier [devcontainer.json](https://code.visualstudio.com/docs/remote/devcontainerjson-reference) et Gitpod avec un fichier [.gitpod.yml](https://www.gitpod.io/docs/references/gitpod-yml) que vous placez dans votre dépôt (nous y reviendrons plus tard). Les deux font essentiellement la même chose, comme définir quel conteneur Docker utiliser, quels scripts exécuter, et ils contrôlent quelles extensions seront disponibles dans votre Codespace (GitHub) / espace de travail (Gitpod).

Les deux produits adoptent un flux de développement logiciel qui permet aux développeurs de démarrer un environnement de développement à partir de n'importe quel contexte Git (problème, PR/MR, branches, etc.) avec un seul clic pour la tâche spécifique sur laquelle vous travaillez.

Ce flux de développement basé sur les tâches est ce qui m'a finalement convaincu de passer du développement local pour des projets réels, et après l'avoir utilisé, il semble que ce serait vraiment difficile de revenir en arrière.

Les environnements de développement deviennent simplement une ressource que je peux lancer à la demande et fermer et oublier si j'ai terminé ma tâche. Gitpod excelle dans ce flux de travail et a construit son produit autour de celui-ci.

En lisant [l'article de blog](https://github.blog/2021-08-11-githubs-engineering-team-moved-codespaces/) de l'équipe d'ingénierie de GitHub, on a l'impression qu'ils ont interne adopté un flux de travail similaire, cependant cela n'est pas natif avec Codespaces pour le moment.

![Image](https://lh4.googleusercontent.com/q0xOqarPIMDK9-hcOLujGzXbJsrkFiFyNnGmGSpkqk4u4eKGbnoHmG7cNYQlLtm_58M7rkpZ_dgHuFHyAK6o3V2rL61hfk-r87NsYTPWJS_kLQW_L9LLo0Idwg_7pq-TXh-u9MK3=s0)

![Image](https://lh6.googleusercontent.com/8LIlWDgOmEO32gO9JSUYL_5tPKr-W9g3C0mnFTuefYVWpd3ppCI4IVT8ap5jkfb2HuhVcHb3LSqkBcGHQf7wnEFVeyN7Nl5Eph2a9VndnNMlkxQBbeaktYZWJS1RhKERq4tHU9Vg=s0)

## Collaboration avec Codespaces vs Gitpod

GitHub Codespaces et Gitpod offrent tous deux des moyens de collaborer, mais ils diffèrent dans leur approche.

Sur les deux plateformes, lorsque votre environnement de développement est en cours d'exécution, vous pouvez exposer n'importe quel port TCP publiquement ou privément sur Internet. Cela permet des flux de travail où vous pouvez partager des liens vers un serveur web ou un serveur API sous forme d'URL standard.

Gitpod offre la possibilité de partager un instantané de l'espace de travail avec un collègue, mais GitHub Codespaces ne le fait pas.

GitHub Codespaces offre la possibilité de programmer en paire de manière interactive lorsque l'[extension LiveShare](https://visualstudio.microsoft.com/services/live-share/) est installée, tandis que Gitpod offre la possibilité de partager l'espace de travail lui-même avec des collaborateurs.

Une fois que Gitpod permettra la prise en charge de VS Code local (1-2 semaines à partir de la rédaction de cet article), vous pourrez également utiliser LiveShare avec Gitpod.

Voici quelques ressources supplémentaires où vous pouvez en lire plus à ce sujet.

* [https://www.gitpod.io/blog/i-said-goodbye-to-local-development-and-so-can-you#develop-a-new-feature](https://www.gitpod.io/blog/i-said-goodbye-to-local-development-and-so-can-you#develop-a-new-feature)
* [https://github.blog/2021-08-11-githubs-engineering-team-moved-codespaces/](https://github.blog/2021-08-11-githubs-engineering-team-moved-codespaces/)
* [https://visualstudio.microsoft.com/services/live-share/](https://visualstudio.microsoft.com/services/live-share/)

## Gitpod vs Codespaces IDE

Gitpod et Codespaces utilisent tous deux VS Code en amont, et VS Code standard comme IDE par défaut s'exécutant dans le navigateur. Il se comporte comme, agit comme, et est littéralement le même VS Code auquel vous êtes habitué sur votre bureau. Faites attention à cmd+W cependant :).

Étant donné que GitHub est détenu par Microsoft, je comprends que l'équipe VS Code a été fortement impliquée dans la construction de GitHub Codespaces.

L'équipe derrière Gitpod a une longue expérience dans les outils de développement open-source, et ils ont initialement créé [Theia](https://theia-ide.org/) (qui est également basé sur VS Code). Mais récemment, ils sont passés à VS Code standard et maintiennent un fork très léger de VS Code qui a également continué à gagner en adoption par d'autres équipes dans l'industrie ([https://github.com/gitpod-io/vscode/](https://github.com/gitpod-io/vscode/)).

![Image](https://lh6.googleusercontent.com/F__NabACVugaw59_F56hT_7euuIyGyGo2gUYRo3tpcRWHZRHKQpomawaGJGph2scXTsD14G-PQwy3H71DKWTU0XQs03tJSENU4IeDRxh-lXL0G3_JB1C9CqWIqPxWFhlSQsKRpy1=s0)

![Image](https://lh3.googleusercontent.com/rIv3ade5u-A027pXxPZ7K-zn--ddFchT3EbjTS-XzYD35jFZ5E-MdefIc3gch2Y5xLvSy6udUuCfWkL-CFZvlvNSkjwrun3MqwjO7ZH98qHrcyQ1HcWm7P7obCqSwVZhulNd1pLS=s0)

## Place de marché des extensions VS Code pour Codespaces et Gitpod

Avoir l'équipe VS Code derrière le produit et pouvoir accéder à toutes les extensions propriétaires (comme Liveshare, par exemple) via la place de marché Visual Studio contrôlée par Microsoft est un plus pour Codespaces.

En réponse, Gitpod a créé [https://open-vsx.org/](https://open-vsx.org/) (maintenant hébergé sous la Fondation Eclipse), qui est une place de marché neutre en termes de fournisseurs, gérée par la Fondation Eclipse pour les extensions VS Code, accessible via Gitpod.

Bien qu'il y ait presque une parité d'extensions pour les extensions VS Code les plus populaires, les excellentes extensions propriétaires de Microsoft n'ont pas trouvé leur chemin vers OpenVSX.

Au cas où vous ne trouveriez pas une extension open-source sur OpenVSX, vous pouvez déclencher l'automatisation de publication en envoyant une pull-request à [https://github.com/open-vsx/publish-extensions](https://github.com/open-vsx/publish-extensions).

### Développement à distance depuis le VS Code de bureau

Je suis un grand fan de la possibilité de me connecter depuis mon VS Code de bureau local vers un environnement de développement s'exécutant sur l'ordinateur de quelqu'un d'autre.

Les deux produits offrent cette fonctionnalité, mais le flux que Codespaces propose est supérieur à l'approche de Gitpod.

Bien que vous puissiez obtenir le même résultat avec l'[application locale](https://www.gitpod.io/blog/local-app) de Gitpod, la configuration implique plus de travail et de friction du point de vue de l'utilisateur. En demandant à l'équipe de Gitpod à ce sujet, j'ai reçu des commentaires selon lesquels ils publieront une expérience similaire en un clic à la fin du mois d'août.

### Et les autres IDE que VS Code ?

Pour GitHub Codespaces, je n'ai pas trouvé d'informations sur d'autres IDE que VS Code. Et étant donné que Microsoft est derrière les deux projets, je m'attends à ce qu'ils se concentrent probablement sur VS Code.

En revanche, Gitpod essaie de souligner que ce qu'ils ont construit est, sur le plan architectural, indépendant de l'IDE et vous permet d'exécuter n'importe quelle image d'IDE que vous pouvez exécuter à distance dans leur conteneur.

J'ai trouvé quelques modèles dans leur dépôt GitHub qui vous permettent d'exécuter la flotte de produits Jetbrains (basée sur [https://github.com/JetBrains/projector-installer](https://github.com/JetBrains/projector-installer)).

L'expérience développeur là-bas semble encore un peu maladroite. En creusant un peu plus, j'ai trouvé cette intéressante [discussion](https://youtrack.jetbrains.com/issue/IDEA-226455#focus=Comments-27-5125731.0-0) autour de l'une des fonctionnalités les plus demandées par la communauté Jetbrains qui permettrait la prise en charge à distance via SSH dès la sortie de la boîte. J'adorerais voir cela pris en charge par Gitpod et Codespaces.

![Image](https://lh4.googleusercontent.com/rmSR14doieAaSg3SibqyU7LewYPc23SlZ6ntjhnAiczvd2zQZLVgwhlWsQ58z6Ax7Xbw3f0e_aUUQYSv8c6TezMwqMSR3usbAIWEezVerseZuHjLHZl3JBhxZ1JSuXxEucoRnVR_=s0)

Voici quelques ressources pour une lecture plus approfondie :

* [https://www.theregister.com/2021/04/08/gitpod_talks_up_importance_of/](https://www.theregister.com/2021/04/08/gitpod_talks_up_importance_of/)
* [https://www.gitpod.io/blog/local-app](https://www.gitpod.io/blog/local-app)
* https://www.gitpod.io/docs/integrations/jetbrains

## Codespaces vs Gitpod Runtime

GitHub Codespaces s'exécute sur des machines virtuelles qui offrent une grande isolation dès la sortie de la boîte et sont plus faciles à provisionner et à gérer. Cependant, elles comportent également l'overhead du système d'exploitation complet, ce qui les rend plus grandes et plus lentes à démarrer ainsi que plus coûteuses.

Gitpod s'exécute sur des conteneurs légers qui démarrent rapidement et bénéficient d'une densité cloud beaucoup plus élevée (car plus de processus peuvent s'exécuter en parallèle sur le même matériel sous-jacent, il y a moins de calculs inactifs). Cela permet aux espaces de travail Gitpod de démarrer plus rapidement et d'être plus efficaces en termes de ressources – c'est-à-dire de coût et d'énergie.

L'inconvénient des conteneurs est que, par défaut, ils n'ont pas les mêmes avantages en termes d'isolation/sécurité que les machines virtuelles.

Avant l'année dernière, les droits sudo (et avec cela docker-in-docker) n'étaient pas possibles dans les espaces de travail Gitpod. Plus tôt cette année, ils ont implémenté des fonctionnalités d'isolation de namespace qui ont rendu ces deux choses possibles (voir leur [responsable de l'ingénierie expliquant comment ils ont réalisé cela](https://www.youtube.com/watch?v=iYLCHQgj0fE&t=274s)).

Codespaces et Gitpod prennent tous deux en charge docker-in-docker pour les scénarios Docker Compose et la virtualisation imbriquée qui permet d'exécuter des systèmes d'exploitation ou des appliances dans votre navigateur.

Voici quelques ressources supplémentaires pour vous sur ce sujet :

* [https://www.gitpod.io/blog/root-docker-and-vscode](https://www.gitpod.io/blog/root-docker-and-vscode)
* [https://github.com/gitpod-io/template-nixos](https://github.com/gitpod-io/template-nixos)

## Automatisation avec Codespaces et Gitpod

Les deux adoptent fortement la notion d'environnement de développement en tant que code, que Vagrant a d'abord popularisée et que Gitpod a ensuite développée.

L'idée de base derrière cela est d'appliquer les idées de l'Infrastructure as Code aux environnements de développement. Codespaces utilise un format [devcontainer.json](https://code.visualstudio.com/docs/remote/devcontainerjson-reference) comme fichier de configuration tandis que Gitpod utilise un .gitpod.yml.

Étant donné la portée et le pouvoir de distribution de Codespaces et VS Code, ma prédiction est que le format [devcontainer.json](https://code.visualstudio.com/docs/remote/devcontainerjson-reference) gagnera à long terme en tant que norme industrielle pour la configuration des environnements de développement. Comme indiqué sur leur [feuille de route](https://github.com/gitpod-io/roadmap/issues/16), Gitpod prévoit de le prendre en charge également. Pour l'instant, ils ne le font pas et utilisent un [.gitpod.yml](https://www.gitpod.io/docs/references/gitpod-yml).

Créer et configurer votre environnement de développement en tant que code n'est que la première étape vers des environnements de développement entièrement automatisés par tâche. Comme vous ne voulez pas attendre que les dépendances se téléchargent et que le code se compile chaque fois que vous démarrez un environnement de développement, les espaces de travail/codespaces doivent être préconstruits avant même que vous ne commeniez.

Gitpod prend en charge les [préconstructions](https://www.gitpod.io/docs/prebuilds) pour cela (considérez-les comme un serveur CI/CD où Gitpod préconstruit l'espace de travail complet / exécute l'automatisation à chaque commit sur Git). L'automatisation ne fonctionne que si elle est exécutée fréquemment.

Codespaces n'inclut actuellement pas les préconstructions dans leur version GA, mais ils les utilisent déjà en interne. Par conséquent, ce ne devrait être qu'une question de mois avant qu'ils ne publient également cette fonctionnalité.

Vous pouvez en lire plus ici :

* [https://www.gitpod.io/screencasts/continuously-prebuild-your-project](https://www.gitpod.io/screencasts/continuously-prebuild-your-project)
* [https://github.blog/2021-08-11-githubs-engineering-team-moved-codespaces/](https://github.blog/2021-08-11-githubs-engineering-team-moved-codespaces/)

## Codespaces et Gitpod Open Source et Écosystème

La plus grande différence entre les deux est que Gitpod est open source et que tout le monde peut contribuer au projet. Vous pouvez l'auto-héberger sur [GKE](https://www.gitpod.io/docs/self-hosted/latest/installation/on-gke), [EKS](https://www.gitpod.io/docs/self-hosted/latest/installation/on-amazon-eks), et Kubernetes vanilla.

Leur feuille de route et leur travail de développement sont publics et tout le monde peut contribuer au projet. En plus de cela, les mainteneurs et les contributeurs principaux des projets open source [bénéficient de Gitpod gratuitement](https://www.gitpod.io/docs/professional-open-source).

Avec GitHub, Microsoft possède la plateforme sociale leader pour les développeurs et ils ont intégré GitHub Codespaces comme un citoyen de première classe dans l'expérience de développement sur GitHub. Cela signifie que par défaut, l'interface utilisateur de GitHub vous montre un bouton Ouvrir dans Codespaces, qui s'intègre parfaitement dans votre flux de travail de développement.

Pour que Gitpod atteigne le même niveau d'intégration, vous devez télécharger soit l'[extension de navigateur](https://www.gitpod.io/docs/browser-extension/), soit un [bookmarklet](https://www.gitpod.io/docs/browser-bookmarklet). GitLab a un [partenariat stratégique](https://about.gitlab.com/blog/2021/07/19/teams-gitpod-integration-gitlab-speed-up-development/) avec Gitpod et a sur chaque dépôt et demande de fusion un bouton "Ouvrir dans Gitpod" intégré dans l'interface utilisateur de GitLab.

Contrairement à Microsoft, Gitpod suit une stratégie où il est neutre par défaut, n'est pas détenu par une grande entreprise technologique et est conçu de manière à s'intégrer avec les outils que les développeurs souhaitent utiliser.

Cela signifie qu'il fonctionne non seulement avec GitHub, mais aussi avec d'autres fournisseurs Git tels que GitLab et Bitbucket, et vous pouvez le déployer sur votre propre infrastructure.

## Disponibilité, Tarification et Spécifications de Codespaces vs Gitpod

Gitpod est disponible depuis plus de 2,5 ans, tandis que GitHub Codespaces est sorti de la version bêta le 11 août 2021 pour les clients disposant d'un abonnement GitHub Team ou GitHub Enterprise.

Sur la base d'un [tweet](https://twitter.com/natfriedman/status/1425508910476271624?s=20) de leur PDG, Nat Friedman, nous pouvons nous attendre à ce que les développeurs individuels aient accès à GitHub Codespaces à la fin de l'année.

GitHub Codespaces est actuellement gratuit pour toutes les organisations disposant d'un abonnement GitHub Team ou GitHub Enterprise jusqu'au 10 septembre. La facturation est basée sur le nombre de minutes pendant lesquelles un espace de travail est actif, et sur la quantité de stockage utilisée sur le disque pour chaque espace de travail jusqu'à ce qu'un utilisateur supprime l'espace de travail.

Vous pouvez [en lire plus ici](https://docs.github.com/en/codespaces/codespaces-reference/understanding-billing-for-codespaces).

Gitpod est gratuit pour les dépôts publics et privés pendant 50 heures par mois. Les mainteneurs et contributeurs principaux de projets open source bien établis peuvent demander un bon qui met à niveau leur compte pour des heures illimitées par mois.

Lisez plus sur la tarification de Gitpod dans ces ressources :

* [https://www.gitpod.io/blog/cloud-based-development-for-everyone](https://www.gitpod.io/blog/cloud-based-development-for-everyone)
* [https://www.gitpod.io/pricing](https://www.gitpod.io/pricing)
* [https://www.gitpod.io/docs/professional-open-source](https://www.gitpod.io/docs/professional-open-source)

Pour simplifier la comparaison des offres de GitHub Codespaces et Gitpod, voici trois scénarios différents utilisant les mêmes quantités de CPU, de mémoire et de stockage pour chaque cas d'utilisation.


<table style="border:none;border-collapse:collapse;table-layout:fixed;width:468pt"><colgroup><col><col><col><col></colgroup><tbody><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><br></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Chef de produit</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Développeur</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Développeur avancé</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Heures de travail</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">2h par jour, 21 jours ouvrés par mois</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">5h par jour, 21 jours ouvrés par mois</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">10h par jour, 21 jours ouvrés par mois.</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Total d'heures par mois</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">42 heures</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">105 heures</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">210 heures</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Nombre de CPU</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">8 cœurs</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">8 cœurs</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">8 cœurs</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Quantité de mémoire</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">12 Go</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">12 Go</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">12 Go</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Quantité de stockage</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">64 Go</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">64 Go</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">64 Go</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;background-color:#000000;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><br></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;background-color:#000000;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><br></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;background-color:#000000;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><br></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;background-color:#000000;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><br></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Coût total sur GitHub Codespaces</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">30,24 USD/mois pour le calcul et 2,24 USD/mois en frais de stockage supplémentaires (les 32 premiers Go par espace de travail sont gratuits)</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">75,6 USD/mois pour le calcul et 2,24 USD/mois en frais de stockage supplémentaires (les 32 premiers Go par espace de travail sont gratuits)</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">151,2 USD/mois pour le calcul et 2,24 USD/mois en frais de stockage supplémentaires (les 32 premiers Go par espace de travail sont gratuits)</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Coût total sur Gitpod</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">9 USD/mois</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">25 USD/mois</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">39 USD/mois</span></p></td></tr></tbody></table>

La quantité de CPU et de mémoire pour chaque espace de travail lancé est configurable dans GitHub Codespaces et ils offrent des SKU allant jusqu'à 32 cœurs CPU et 64 Go de RAM. Gitpod, pour le moment, ne propose pas encore de moyen d'avoir plus ou moins de ressources de calcul.

## **Voir en action**

J'espère que vous êtes aussi excité que moi après avoir entendu parler pour la première fois du concept d'environnements de développement en tant que code dans le cloud ! Essayez les deux et voyez par vous-même ce que vous en pensez.

Pour l'instant, je préfère Gitpod car il est gratuit pour mes cas d'utilisation, offre des préconstructions, est accessible à quiconque souhaite l'utiliser, est open source et peut être utilisé avec n'importe quel fournisseur Git, y compris GitHub.

### Comment commencer avec [Gitpod](http://gitpod.io) :

* Ajoutez le préfixe gitpod.io/# à n'importe quelle URL GitLab, GitHub ou Bitbucket pour plonger directement
* Ou utilisez leur [extension de navigateur](https://www.gitpod.io/docs/browser-extension/) ou [bookmarklet de navigateur](https://www.gitpod.io/docs/browser-bookmarklet) pour démarrer des espaces de travail à partir de n'importe quel contexte git
* Ou essayez leurs [modèles de démarrage rapide](https://github.com/gitpod-io?q=template-)
* Consultez mes guides [ici](https://www.youtube.com/watch?v=tXSF7lIQouQ) et [ici](https://www.youtube.com/watch?v=hUSzdIOrlY4)

### Comment commencer avec [Codespaces](https://github.com/features/codespaces) :

* Si vous êtes un client GitHub Teams ou Enterprise, cherchez un bouton "Ouvrir dans GitHub" à côté d'un dépôt
* Les développeurs individuels doivent attendre qu'il soit lancé plus largement
* Regardez [cette](https://www.youtube.com/watch?v=dMs-8QY1URw) vidéo pour un aperçu.