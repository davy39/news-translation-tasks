---
title: Guide de sécurité des logiciels open source – Bonnes pratiques pour sécuriser
  vos projets
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2023-02-27T22:19:21.000Z'
originalURL: https://freecodecamp.org/news/oss-security-best-practices
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/OSS-Security-Best-Practices-Handbook-Cover--1-.png
tags:
- name: DevSecOps
  slug: devsecops
- name: open source
  slug: open-source
- name: Security
  slug: security
seo_title: Guide de sécurité des logiciels open source – Bonnes pratiques pour sécuriser
  vos projets
seo_desc: "Christine Peterson coined the term \"Open Source software\" or OSS in 1998.\
  \ It refers to software that is freely available for anyone to use, modify, and\
  \ distribute. \nThe source code of OSS is openly available and anyone can modify\
  \ it who has the neces..."
---

Christine Peterson a inventé le terme "Open Source software" ou OSS en 1998. Il fait référence à des logiciels qui sont librement disponibles pour que chacun puisse les utiliser, modifier et distribuer.

Le code source de l'OSS est ouvertement disponible et toute personne ayant les compétences techniques nécessaires peut le modifier. Cela permet à une communauté de développeurs de collaborer et de contribuer au développement et à l'amélioration du logiciel.

Cela distingue l'OSS des logiciels propriétaires ou closed source, où le code source n'est pas facilement disponible.

L'OSS est souvent développé et maintenu par une communauté de bénévoles, et est généralement distribué sous une licence open source spécifique qui définit les termes d'utilisation et de distribution. Des exemples d'OSS incluent le système d'exploitation Linux, le serveur web Apache et le langage de programmation Python.

L'un des principaux avantages de l'OSS est qu'il donne aux utilisateurs plus de contrôle sur les logiciels qu'ils utilisent car ils peuvent examiner le code.

De plus, il est considéré comme plus stable et sécurisé que les logiciels propriétaires. Cela est dû au fait qu'il suit des normes ouvertes, ce qui le rend moins susceptible de disparaître si ses mainteneurs cessent de travailler dessus.

L'OSS dispose également d'une communauté d'utilisateurs et de développeurs qui peuvent aider à identifier et résoudre les problèmes. Néanmoins, il présente son propre ensemble de défis de sécurité.

## Table des matières

1. [Attaques contre les logiciels open source](#heading-attaques-contre-les-logiciels-open-source)
2. [Attaques de la chaîne d'approvisionnement logicielle](#heading-attaques-de-la-chaine-dapprovisionnement-logicielle)
3. [Qu'est-ce que la sécurité des applications web ?](#heading-quest-ce-que-la-securite-des-applications-web)
4. [L'analogie de "l'Iceberg"](#heading-lanalogie-de-liceberg)
5. [GitHub Marketplace](#heading-github-marketplace)
6. [Comment utiliser GitHub Marketplace pour atténuer les risques dans vos projets open source](#heading-comment-utiliser-github-marketplace-pour-attenuuer-les-risques-dans-vos-projets-open-source)
7. [Analyse de la composition logicielle](#heading-analyse-de-la-composition-logicielle)
8. [Qu'est-ce que la prolifération des secrets ?](#heading-quest-ce-que-la-proliferation-des-secrets)
9. [Analyse statique du code](#heading-analyse-statique-du-code)
10. [Comment tirer parti de ChatOps](#heading-comment-tirer-parti-de-chatops)
11. [Bonnes pratiques pour les logiciels open source](#heading-bonnes-pratiques-pour-les-logiciels-open-source)
12. [Cinq conseils pour la sécurité OSS](#heading-cinq-conseils-pour-la-securite-oss)
13. [Comment faire un impact dans la communauté des logiciels open source](#heading-comment-faire-un-impact-dans-la-communaute-des-logiciels-open-source)
14. [Points clés à retenir pour la sécurité open source 101](#heading-points-cles-a-retenir-pour-la-securite-open-source-101)

## Attaques contre les logiciels open source

Dans cette section, nous allons examiner certaines des attaques les plus courantes contre les logiciels open source.

### Attaques par typosquatting

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-22-at-15.42.44.png)

Le **typosquatting**, également connu sous le nom de **détournement d'URL**, est une forme de cyberattaque où un attaquant enregistre un nom de domaine similaire à un site web bien connu, mais avec une légère faute de frappe. L'attaquant crée ensuite une fausse version du site web original dans le but de tromper les utilisateurs et de leur faire entrer leurs informations personnelles, telles que des mots de passe ou des numéros de carte de crédit.

Par exemple, si un site web populaire est [www.example.com](http://www.example.com/), un typosquatter peut enregistrer [www.examplle.com](http://www.examplle.com/), dans l'espoir que les utilisateurs tapent accidentellement la mauvaise URL et se retrouvent sur le faux site web. Le faux site web peut ressembler en tous points à l'original, rendant difficile pour les utilisateurs de réaliser qu'ils ont été redirigés vers un site différent.

Les attaques par typosquatting peuvent également avoir lieu dans l'OSS où des acteurs malveillants poussent des packages malveillants vers un registre dans l'espoir de tromper les utilisateurs et de les inciter à les installer.

Voici un exemple avec le package **react** avec une faute de frappe. Dans ce cas, vous n'installerez pas React, mais potentiellement un package malveillant qui a un objectif final complètement différent.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-22-at-15.45.41.png)
_[En savoir plus sur les attaques par typosquatting ici](https://snyk.io/blog/typosquatting-attacks/)._

Nous avons vu ces types de packages dans les registres **PyPi** et **npm**, le plus notable d'entre eux étant **crossenv**.

Le package **crossenv** a pris un nom similaire au package populaire **cross-env** et a enveloppé la même fonctionnalité, sauf qu'il capturait également les variables d'environnement et les envoyait à un serveur distant contrôlé par l'attaquant.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-13.17.27.png)
_[Lire plus sur crossenv ici](https://snyk.io/advisor/npm-package/crossenv)._

Le typosquatting peut avoir de graves conséquences, y compris le vol d'identité, la fraude financière et la propagation de logiciels malveillants.

Pour éviter de devenir victime de typosquatting, il est important de scanner attentivement les packages dans votre base de code avec des outils de sécurité et de les importer à partir de sources connues.

### Packages malveillants

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-22-at-15.50.08.png)

Les **packages malveillants**, également connus sous le nom de logiciels malveillants ou malware, sont des packages conçus intentionnellement pour nuire ou exploiter des systèmes informatiques. Ils sont souvent distribués par divers moyens, tels que des pièces jointes de courrier électronique, des sites web malveillants ou des téléchargements de logiciels infectés.

Une fois les packages malveillants installés sur un ordinateur, ils peuvent causer divers problèmes. Le principal serait le vol de données où l'attaquant peut accéder à des informations sensibles, telles que des mots de passe, des numéros de carte de crédit ou des fichiers personnels.

Il existe également des cas de perturbation du système où le malware peut endommager ou supprimer des fichiers système importants, ralentissant l'ordinateur ou le rendant inopérant. L'attaquant peut également utiliser le malware pour espionner ou surveiller les activités de la victime, y compris les frappes de touches, les e-mails et la navigation web. Et il peut se propager ou pivoter où le malware peut se répandre sur d'autres ordinateurs du même réseau, causant des dommages supplémentaires.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-22-at-15.52.28.png)

Voici un exemple avec le package malveillant **fallguys**. Les attaquants surfent généralement sur les tendances et ce jeu a été assez populaire pendant la pandémie. Les joueurs pourraient penser qu'en téléchargeant ce package, ils pourraient obtenir un avantage dans le jeu.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-22-at-15.56.48.png)
_[Lire plus sur fallguys ici](https://snyk.io/advisor/npm-package/fallguys)._

Malheureusement pour eux, ce package contient du code malveillant qui tenterait de lire des fichiers sensibles locaux et d'exfiltrer des informations via un webhook Discord. Le code accédait à des chemins spécifiques disponibles sur les systèmes Windows situés à **/AppData/Local/Google/Chrome/User Data/Default/Local Storage/leveldb**.

Il est important de prendre des mesures pour protéger votre ordinateur contre les packages malveillants, telles que maintenir votre système d'exploitation et vos logiciels à jour.

Si vous suspectez que votre ordinateur a été infecté par un malware, vous devez agir rapidement pour minimiser les dommages et empêcher la propagation de l'infection.

### Mainteneurs GitHub compromis

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-22-at-16.01.09.png)

Les **mainteneurs GitHub compromis** font référence aux individus responsables de la maintenance de projets de logiciels open source hébergés sur GitHub dont les comptes ont été piratés ou pris en charge par des attaquants.

Cela peut se produire lorsque les informations d'identification du compte GitHub du mainteneur, telles que son nom d'utilisateur et son mot de passe, sont obtenues par un attaquant par des moyens tels que des attaques de phishing, la réutilisation de mots de passe, ou en étant victime d'**ingénierie sociale** sur GitHub.

Une fois que l'attaquant a le contrôle du compte d'un mainteneur, il peut effectuer diverses actions malveillantes.

Il peut pousser des packages malveillants où un attaquant peut publier de nouveaux packages ou des mises à jour de packages existants contenant des logiciels malveillants, infectant potentiellement les utilisateurs qui les téléchargent et les installent.

Il peut propager des logiciels malveillants où un attaquant peut utiliser le compte compromis pour propager des logiciels malveillants à d'autres utilisateurs ou organisations, soit via le dépôt lui-même, soit par d'autres moyens, tels que des e-mails de phishing.

Ils peuvent également falsifier le code où un attaquant peut apporter des modifications au code dans le dépôt, introduisant des vulnérabilités ou des portes dérobées qui peuvent être utilisées pour une exploitation ultérieure.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-22-at-16.07.04.png)

Dans cet exemple avec le **package event-stream**, l'attaquant a parcouru tous les problèmes du dépôt à la recherche de fonctionnalités où il pourrait contribuer. Il a commencé à établir la confiance avec le mainteneur et les autres contributeurs en poussant des changements cosmétiques au début. Ensuite, lorsqu'il a obtenu plus de permissions, il a poussé sa charge utile malveillante dans la base de code qui ciblait un portefeuille Bitcoin.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-73.png)
_[Lire plus sur cette attaque ici](https://snyk.io/blog/a-post-mortem-of-the-malicious-event-stream-backdoor/)._

Les mainteneurs GitHub compromis représentent une menace sérieuse pour la sécurité et la stabilité de l'écosystème des logiciels open source. Il est important pour les mainteneurs de prendre des mesures pour protéger leurs comptes et surveiller leurs dépôts pour détecter les signes d'activité suspecte.

Cela peut inclure l'utilisation de mots de passe forts et uniques, l'activation de l'authentification à deux facteurs, et la révision régulière de l'activité dans leurs dépôts pour détecter tout changement inhabituel ou non autorisé.

### Protestware

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-22-at-16.10.00.png)

Le **Protestware** fait référence à des logiciels ou technologies utilisés comme forme de protestation ou d'activisme politique. Il est conçu pour défier ou perturber des systèmes, politiques ou pratiques jugés injustes ou nuisibles.

L'utilisation de protestware est controversée et peut avoir des conséquences légales, car elle implique souvent des actes illégaux ou non éthiques, tels que le piratage, l'accès non autorisé ou la perturbation de services. De plus, elle peut avoir des conséquences imprévues, telles que causer des dommages à des parties innocentes ou compromettre la sécurité des utilisateurs du logiciel.

Si vous souhaitez en savoir plus sur le protestware, vous pouvez lire cet [article](https://snyk.io/blog/protestware-open-source-types-impact/).

## Attaques de la chaîne d'approvisionnement logicielle

Une **attaque de la chaîne d'approvisionnement** se produit lorsqu'un tiers ayant accès aux données et systèmes d'une organisation est utilisé pour infiltrer l'infrastructure numérique de l'organisation.

Une vulnérabilité peut être introduite à n'importe quel point de la chaîne d'approvisionnement, y compris la conception, le développement, la fabrication, la distribution ou la livraison d'un produit ou service.

Par exemple, un attaquant peut compromettre un fournisseur de logiciels qui fournit des composants logiciels utilisés par de nombreuses organisations, ou falsifier des composants matériels pendant la fabrication ou l'expédition. L'attaquant peut ensuite utiliser la compromission pour propager des logiciels malveillants ou exfiltrer des données sensibles des systèmes de la cible.

La nature ouverte de l'OSS le rend vulnérable aux attaques de la chaîne d'approvisionnement. Dans le cas des initiatives open source, des acteurs malveillants peuvent introduire des vulnérabilités dans le logiciel produit, facilitant ainsi la propagation de nouvelles menaces aux entreprises utilisant le logiciel.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-13.05.24.png)
_Une vulnérabilité peut être introduite à n'importe quel point de la chaîne d'approvisionnement_

Dans une **attaque de la chaîne d'approvisionnement logicielle**, les attaquants utilisent du code malveillant pour compromettre un "**composant en amont**" dans la chaîne avec pour objectif final de compromettre la cible de l'attaque : le "**composant en aval**".

Compromettre le composant en amont n'est pas l'objectif final – c'est une opportunité pour les attaquants de compromettre la cible de l'attaque en insérant des logiciels malveillants ou en fournissant une porte dérobée pour un accès futur.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-13.06.03.png)

Cela n'affecte pas seulement les packages JavaScript, comme nous l'avons vu avec quelques exemples dans la section des attaques open source. C'est un problème pour tous les écosystèmes.

Nous avons eu un excellent exemple avec la vulnérabilité **Log4j** en 2021. Si vous souhaitez en savoir plus sur cette vulnérabilité, consultez ces [ressources](https://snyk.io/log4j-vulnerability-resources/).

L'une des exploits Log4j permet l'**exécution de code à distance** sur les serveurs exécutant des applications vulnérables sans nécessiter d'authentification. Cela a valu à la vulnérabilité une note de gravité de **10 sur l'échelle CVSS** (Common Vulnerability Scoring System).

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-22-at-16.30.37.png)
_[Lire plus sur RCE ici](https://security.snyk.io/vuln/SNYK-JAVA-ORGAPACHELOGGINGLOG4J-2314720)._

Log4j est utilisé dans de nombreuses applications commerciales, et les organisations peuvent être vulnérables sans savoir qu'elles utilisent effectivement la bibliothèque de journalisation.

Pour atténuer le risque d'attaques de la chaîne d'approvisionnement, les organisations doivent mettre en œuvre des mesures de sécurité tout au long de leur chaîne d'approvisionnement, y compris la réalisation de vérifications des antécédents des fournisseurs, la mise en œuvre de processus de signature de code et de démarrage sécurisé, et la surveillance régulière de leurs systèmes pour détecter les signes de compromission.

De plus, il est important de maintenir les composants logiciels et matériels à jour avec les derniers correctifs et mises à jour de sécurité pour réduire le risque d'exploitation.

### Pourquoi les attaques de la chaîne d'approvisionnement logicielle sont-elles attractives pour les hackers ?

Les **attaques de la chaîne d'approvisionnement logicielle** sont attractives pour les hackers pour plusieurs raisons.

Tout d'abord, en ciblant une vulnérabilité dans la chaîne d'approvisionnement, l'attaquant peut potentiellement compromettre de nombreuses organisations et leurs clients, plutôt qu'une seule cible. Cela permet à l'attaquant de maximiser son impact et de potentiellement voler de grandes quantités de données sensibles ou de causer des dommages généralisés.

Les attaques de la chaîne d'approvisionnement logicielle sont difficiles à détecter car elles impliquent souvent la falsification de produits ou de composants logiciels avant qu'ils n'atteignent l'organisation cible. Cela peut rendre difficile pour la cible de détecter l'attaque, surtout si l'attaquant est capable de maintenir l'accès aux systèmes compromis pendant une période prolongée.

De plus, les organisations font souvent confiance aux produits et services fournis par leurs fournisseurs, ce qui facilite l'exploitation de cette confiance et la réalisation de l'attaque par l'attaquant. De plus, les mesures de sécurité peuvent ne pas être aussi strictes pour les fournisseurs ou les vendeurs tiers, ce qui facilite la compromission de ces systèmes par l'attaquant.

Enfin, les informations et les systèmes des organisations sont souvent des cibles précieuses pour les attaquants, surtout s'ils contiennent des informations sensibles telles que la propriété intellectuelle, les données financières ou les informations personnelles. En compromettant la chaîne d'approvisionnement, l'attaquant peut accéder à ces actifs précieux.

### Pourquoi la sécurité des applications est-elle importante ?

Les applications stockent et traitent souvent des informations sensibles, telles que des données personnelles, des informations financières et de la propriété intellectuelle. Assurer la sécurité de ces applications est essentiel pour protéger ces informations sensibles contre le vol, la manipulation ou l'accès non autorisé.

De plus, les applications sont essentielles aux opérations quotidiennes de la plupart des organisations, et une faille de sécurité dans une application peut causer des perturbations significatives aux opérations commerciales et des pertes financières. En mettant en œuvre des mesures de sécurité robustes pour les applications, les organisations peuvent aider à assurer la disponibilité et la stabilité de leurs applications et maintenir la continuité des activités face aux menaces de sécurité.

Nous savons qu'une **faille de sécurité** dans une application peut nuire à la réputation d'une organisation, causant des dommages à sa marque et une perte de confiance des clients. En investissant dans la sécurité des applications, les organisations peuvent protéger leur réputation et renforcer la confiance des clients.

De plus, de nombreuses industries et organisations sont soumises à des réglementations qui les obligent à mettre en œuvre des mesures de sécurité solides pour leurs applications et à protéger les informations sensibles. Le non-respect de ces réglementations peut entraîner des sanctions légales et des pertes financières.

Enfin, une faille de sécurité dans une application peut entraîner des pertes financières pour l'organisation, telles que le coût de la remédiation, les frais juridiques et la perte d'activité due aux dommages de réputation. La mise en œuvre de mesures de sécurité robustes pour les applications peut aider à prévenir ces pertes financières et à protéger la rentabilité de l'organisation.

## Qu'est-ce que la sécurité des applications web ?

La **sécurité des applications web** fait référence aux mesures et pratiques prises pour sécuriser les sites web et les applications web contre diverses menaces de sécurité.

Elle implique la mise en œuvre d'une gamme de mesures de sécurité, y compris les contrôles d'accès, l'authentification et l'autorisation, le chiffrement, la validation des entrées, et plus encore. Ces mesures sont mises en œuvre tout au long du cycle de vie du développement logiciel (SDLC) pour identifier et résoudre les vulnérabilités de sécurité.

L'objectif de la sécurité des applications web est de garantir que les données et les systèmes accessibles par les applications web sont protégés contre l'accès non autorisé, la falsification et la destruction.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-13.07.12.png)
_Un exemple de pipeline SDLC_

Dans ce flux de travail, nous pouvons implémenter des garde-fous de sécurité à chaque étape de notre pipeline.

À l'étape de codage, nous pourrions avoir un outil de sécurité intégré dans notre IDE ou utilisant la CLI pour scanner notre code et nos packages. Nous pourrions avoir des scans déclenchés au niveau du dépôt ou intégrés dans notre pipeline CI/CD pour nous assurer que nous testons notre code. Les registres peuvent également être surveillés pour nous assurer que nous récupérons des packages ou des images non vulnérables.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-69.png)
_Sécuriser votre SDLC est crucial_

Des organisations telles que **[OWASP](https://owasp.org/)** (Open Worldwide Application Security Project) suivent les vulnérabilités trouvées et fournissent une liste que les développeurs et les équipes de sécurité peuvent utiliser comme point de départ pour leur programme de sécurité des applications.

La liste la plus récente des **OWASP Top 10** a été publiée en 2021 et inclut le contrôle d'accès rompu, les attaques par injection, les mauvaises configurations de sécurité et plus encore.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-13.40.19.png)
_[Lire les OWASP top 10 ici](https://owasp.org/Top10/)._

## L'analogie de l'Iceberg

L'analogie de "l'**Iceberg**" est souvent utilisée pour décrire les couches d'une application moderne, y compris le code de l'application, les bibliothèques open source, les conteneurs et l'infrastructure en tant que code.

L'analogie est basée sur l'idée que – tout comme un iceberg, qui n'a qu'une petite portion visible au-dessus de l'eau tandis que la majeure partie se trouve sous la surface – les applications modernes ont de nombreuses couches qui ne sont pas immédiatement visibles mais sont essentielles à leur fonctionnement.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-13.04.39.png)
_Le profil de risque de l'application moderne avec une surface d'attaque plus grande_

Au sommet de l'iceberg, nous avons le **code de l'application** visible, qui est le code que les développeurs écrivent pour créer la fonctionnalité de l'application. Mais sous la surface, il y a de nombreuses couches qui ne sont pas immédiatement visibles mais sont essentielles au fonctionnement de l'application.

La première couche sous la surface est celle des **bibliothèques open source**, qui sont souvent utilisées par les développeurs pour gagner du temps et augmenter la productivité. Ces bibliothèques contiennent du code qui a été écrit par d'autres développeurs et peut être utilisé pour effectuer des tâches courantes, telles que la gestion des requêtes HTTP ou la gestion des bases de données.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-22-at-16.48.19.png)

La couche suivante est celle des **conteneurs**, qui sont utilisés pour empaqueter et déployer des applications de manière cohérente et efficace. Les conteneurs sont utilisés pour isoler l'application du système hôte et fournir un environnement standardisé pour exécuter l'application.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-22-at-16.49.26.png)

Enfin, au bas de l'iceberg, nous avons l'**infrastructure en tant que code**, qui fait référence au code utilisé pour automatiser le déploiement et la gestion de l'infrastructure qui supporte l'application. Cela inclut des ressources telles que des machines virtuelles, des réseaux et du stockage.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-22-at-16.50.23.png)

L'analogie de l'Iceberg met en lumière la complexité des applications modernes et l'importance d'adopter une approche holistique pour les sécuriser.

Pour garantir qu'une application est sécurisée, vous devrez prendre en compte et sécuriser toutes ces couches, y compris le code de l'application, les bibliothèques open source, les conteneurs et l'infrastructure en tant que code.

### Comment implémenter le SDLC dans les projets open source

La sécurité des applications web est un aspect crucial pour garantir la sécurité d'un projet. Elle implique la mise en œuvre de mesures de sécurité tout au long du cycle de vie du développement logiciel (SDLC) pour identifier et résoudre les vulnérabilités de sécurité dans le projet et sa configuration.

Une façon de sécuriser votre projet open source est d'utiliser les outils et applications de sécurité disponibles sur le **GitHub Marketplace**. Cela pourrait également s'appliquer à vos projets personnels que vous souhaitez démontrer lors d'un entretien d'embauche !

Faire cela permettra le même niveau de protection que pour un projet propriétaire.

## GitHub Marketplace

[**GitHub Marketplace** a été introduit en 2016](https://github.blog/2017-05-22-introducing-github-marketplace-and-more-tools-to-customize-your-workflow/) et offre aux développeurs une plateforme pour trouver et intégrer des outils dans leurs flux de travail. Il propose une large gamme de produits et services, y compris :

1. **Outils de révision et d'analyse de code** : Outils pour automatiser la révision de code, analyser la qualité du code et vérifier les vulnérabilités de sécurité.
2. **Outils d'intégration et de déploiement continus** : Outils pour automatiser la construction, les tests et le déploiement du code dans des environnements de production.
3. **Outils de gestion de projet** : Outils pour suivre la progression des projets, gérer les tâches et collaborer avec d'autres membres d'une équipe de développement.
4. **Outils de communauté et de communication** : Outils pour améliorer la communication et la collaboration au sein d'une équipe de développement et avec la communauté plus large.
5. **Outils de surveillance et de performance** : Outils pour surveiller la performance et la disponibilité du code dans les environnements de production.
6. **Outils de conformité et de sécurité** : Outils pour garantir la conformité avec les réglementations et normes de l'industrie, et pour améliorer la sécurité du code.
7. **Éducation et formation** : Cours et ressources pour apprendre GitHub, le développement logiciel et les technologies connexes.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-216.png)
_[GitHub Marketplace compte plus de 10 000 actions](https://github.blog/2021-10-21-github-marketplace-welcomes-its-10000th-action)!_

Le Marketplace est conçu pour faciliter la découverte et l'intégration d'outils dans le flux de travail des développeurs, rationalisant ainsi le processus de développement et augmentant l'efficacité.

De nombreux outils et services disponibles dans le Marketplace sont créés par des développeurs tiers et sont conçus pour fonctionner de manière transparente avec GitHub. Cela permet aux développeurs de gérer leur code et leurs projets plus efficacement.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-14.09.26.png)

### Comment utiliser les applications et les actions GitHub sur GitHub Marketplace

Le processus d'utilisation d'une application ou d'une action sur GitHub Marketplace peut varier en fonction de l'outil spécifique. Vous pouvez parcourir le GitHub Marketplace pour trouver des applications et des actions qui répondent à vos besoins. Une fois que vous avez trouvé celle que vous souhaitez utiliser, cliquez dessus pour en savoir plus.

Selon l'application ou l'action, il existe plusieurs façons de l'utiliser. Certaines peuvent nécessiter une installation ou une configuration, tandis que d'autres peuvent être utilisées immédiatement.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-14.10.51.png)
_[https://github.com/marketplace/snyk](https://github.com/marketplace/snyk)_

L'application ou l'action sera accompagnée d'instructions sur la manière de l'utiliser. Vous pouvez généralement les trouver sur la page de l'application ou de l'action sur le Marketplace ou dans la documentation.

En tant que mainteneur d'un projet, vous vérifierez si cela sera un outil adapté à votre base de code. Nous pouvons voir si GitHub a vérifié l'application, les langues prises en charge, une description de l'outil, et plus d'informations sur l'organisation.

Lorsque vous faites défiler la page du produit, vous devriez voir la section **Prix et configuration**. Presque tous les outils et actions disponibles sur GitHub Marketplace ont un plan gratuit pour les dépôts publics et les projets open source.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-14.11.39.png)

Lorsque vous cliquez sur le bouton vert, **Install it for free**, vous pouvez passer en revue la commande.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-14.13.24.png)

### Que considérer lors de la sélection d'outils ou d'applications

Lors de la sélection d'outils et d'applications, il est important de prendre en compte des facteurs tels que la stack technologique utilisée, le nombre d'étapes dans le pipeline, et si vous pouvez implémenter des garde-fous à chaque étape.

Vous pouvez également considérer le but de l'outil et s'il possède les fonctionnalités dont vous avez besoin pour répondre à vos exigences. Certains outils peuvent avoir une large gamme de fonctionnalités, tandis que d'autres peuvent être plus spécialisés pour des cas d'utilisation spécifiques.

Vérifiez également si l'outil est compatible avec votre stack de développement et votre environnement. Cela inclut la compatibilité avec les langages de programmation, les frameworks, les systèmes d'exploitation et les autres outils que vous utilisez déjà.

Recherchez également des outils qui disposent d'une documentation complète, de tutoriels et de ressources de support disponibles. Cela peut vous aider à vous lancer rapidement avec l'outil et à résoudre les problèmes que vous pourriez rencontrer.

Vous pouvez vérifier les avis des utilisateurs sur l'outil pour voir ce que les autres ont vécu. Cela peut vous donner une idée des forces et des faiblesses de l'outil, ainsi que de sa qualité globale.

Enfin, n'oubliez pas de prendre en compte les implications de sécurité de l'outil, surtout s'il aura accès à des données ou systèmes sensibles. Recherchez des outils qui ont été audités de manière indépendante pour les vulnérabilités de sécurité et qui ont des pratiques de sécurité solides en place.

En prenant en compte ces facteurs, vous pouvez prendre une décision éclairée lors de la sélection d'une application ou d'un outil sur le GitHub Marketplace.

Mais surtout,

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-14.15.42.png)

## Comment utiliser GitHub Marketplace pour atténuer les risques dans votre projet open source

Vous pouvez tirer parti des applications et actions de sécurité disponibles sur GitHub Marketplace pour sécuriser votre pipeline à chaque étape de votre cycle de vie de développement logiciel.

Identifiez les exigences de sécurité pour votre cycle de vie de développement logiciel, telles que les outils de sécurité dont vous avez besoin et quand vous en avez besoin. Cela vous aidera à sélectionner les applications et actions de sécurité appropriées.

Ensuite, intégrez les outils de sécurité dans votre pipeline pour identifier les vulnérabilités et les problèmes de sécurité à chaque étape du SDLC. Par exemple, vous pouvez utiliser un outil d'analyse de code pour détecter les problèmes de sécurité dans votre code, ou un outil d'analyse de conteneurs pour identifier les vulnérabilités dans vos conteneurs.

Assurez-vous d'automatiser les vérifications de sécurité pour garantir que les problèmes de sécurité sont détectés le plus tôt possible dans le processus de développement. Cela peut aider à réduire le risque d'introduction de problèmes de sécurité dans la base de code.

Vous pouvez également configurer des politiques de sécurité pour garantir que votre équipe de développement suit les pratiques de codage sécurisé et respecte les exigences de conformité. Cela peut inclure l'imposition de l'utilisation de bibliothèques et de frameworks spécifiques, ou la mise en place de procédures de révision et de test de code sécurisé.

N'oubliez pas de surveiller et de gérer les alertes de sécurité pour garantir que les vulnérabilités et les problèmes de sécurité sont traités en temps opportun. Cela peut inclure la configuration de notifications pour les alertes de sécurité, la priorisation des vulnérabilités et le suivi de la progression de la résolution.

Si vous ne savez pas par où commencer, vous pourriez envisager de construire un **pipeline de base** qui comprendrait :

* un **outil d'analyse de la composition logicielle** pour se concentrer sur l'identification de l'open source dans une base de code afin que les mainteneurs et les contributeurs puissent gérer leur exposition aux problèmes de sécurité et de conformité des licences.
* un **outil pour prévenir la prolifération des secrets** qui est la distribution non souhaitée de secrets comme les clés API et les identifiants à travers plusieurs systèmes.
* un **outil pour couvrir l'analyse statique du code** qui est une méthode de débogage en examinant le code source avant qu'un programme ne soit exécuté où il analyse un ensemble de code par rapport à un ensemble de règles de codage.

## Analyse de la composition logicielle

L'**analyse de la composition logicielle (SCA)** est le processus d'identification et d'analyse des divers composants, bibliothèques et dépendances qui constituent une application logicielle.

L'objectif de la SCA est d'identifier toute vulnérabilité ou risque de sécurité connu dans les composants utilisés dans le logiciel, et de s'assurer que le logiciel est construit en utilisant des composants sécurisés et à jour.

La SCA est une étape importante dans le processus de développement logiciel, car elle aide à garantir que le logiciel est exempt de vulnérabilités que les attaquants pourraient exploiter.

Vous effectuez généralement la SCA à intervalles réguliers tout au long du cycle de développement, et c'est un aspect important des pratiques de développement logiciel sécurisé (telles que le cycle de vie de développement logiciel sécurisé).

Les outils et services SCA peuvent scanner le logiciel et ses composants, les comparant à une base de données de vulnérabilités et de risques de sécurité connus. Vous pouvez ensuite utiliser les résultats de l'analyse pour identifier et résoudre tout problème de sécurité, tel que des composants obsolètes ou des composants avec des vulnérabilités connues, avant qu'ils ne puissent être exploités par des attaquants.

### Analyse de la composition logicielle avec Renovate

**Mend Renovate** est un outil open source pour automatiser la gestion des dépendances dans un projet logiciel.

Comme d'autres outils de gestion des dépendances, il aide à maintenir les dépendances d'un projet à jour, réduisant ainsi le risque de vulnérabilités de sécurité et d'autres problèmes associés aux dépendances obsolètes.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-14.28.02.png)
_[https://github.com/marketplace/renovate](https://github.com/marketplace/renovate)_

Ceci est un exemple de pull request soulevée par Renovate. La pull request contiendra toutes les informations nécessaires concernant la version du package, les notes de version, et s'il y a des changements cassants avant la fusion.

### Analyse de la composition logicielle avec Dependabot

**Dependabot** est un service offert par **GitHub** qui automatise le processus de mise à jour des dépendances dans un projet logiciel. Il aide les développeurs à maintenir leurs dépendances à jour, réduisant ainsi le risque de vulnérabilités de sécurité et d'autres problèmes associés aux dépendances obsolètes.

Dependabot surveille les dépendances d'un projet et envoie des pull requests pour les mettre à jour lorsque de nouvelles versions deviennent disponibles. Les pull requests incluent des informations détaillées sur les mises à jour, y compris le nouveau numéro de version, un résumé des changements et un lien vers les notes de version. Ces informations aident les développeurs à évaluer rapidement l'impact de la mise à jour et à décider s'ils doivent la fusionner dans leur base de code.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-14.31.10.png)
_Pull request de Dependabot_

### Analyse de la composition logicielle avec Snyk

**Snyk** est un outil pour sécuriser les dépendances des logiciels open source. Il aide les développeurs à identifier et corriger les vulnérabilités dans leurs dépendances, ainsi qu'à surveiller leurs projets pour détecter les nouveaux problèmes de sécurité.

Snyk s'intègre avec les plateformes de développement populaires, telles que GitHub et GitLab. Il fournit aux développeurs des informations sur la sécurité de leurs dépendances, y compris la gravité des vulnérabilités, quand elles ont été découvertes et ce qu'il faut faire pour les corriger. L'outil fournit également des correctifs de sécurité automatisés, que vous pouvez facilement appliquer pour corriger les vulnérabilités connues.

Snyk prend en charge une large gamme de langages de programmation et de gestionnaires de packages, ce qui en fait une solution polyvalente pour sécuriser les dépendances des logiciels open source. Il fournit également des rapports et des analyses détaillés, aidant les développeurs à comprendre la posture de sécurité de leurs projets et à prendre des mesures pour résoudre les vulnérabilités de sécurité.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-14.40.03.png)
_Pull request de Snyk_

Si vous souhaitez en savoir plus sur les vulnérabilités, vous pouvez explorer la **base de données des vulnérabilités open source de Snyk**. Il s'agit d'une base de données complète qui fournit des informations sur les vulnérabilités de sécurité connues dans les packages et bibliothèques open source.

Cette base de données est constamment mise à jour avec de nouvelles vulnérabilités et offre aux utilisateurs la possibilité de rechercher des vulnérabilités par nom de package, numéro de version ou vulnérabilité spécifique.

La base de données fournit également des informations sur la gravité de chaque vulnérabilité et offre des conseils de remédiation pour aider les développeurs à résoudre les vulnérabilités identifiées dans leur code.

La base de données des vulnérabilités open source de Snyk est une ressource précieuse pour les développeurs qui construisent des applications avec des composants open source. Elle peut vous aider à identifier les problèmes de sécurité potentiels et à prendre des mesures pour les prévenir avant qu'ils ne deviennent un problème.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-22-at-22.00.09-1.png)
_[https://security.snyk.io/](https://security.snyk.io/)_

### Notifications par e-mail pour l'analyse de la composition logicielle

Lors de l'utilisation d'un outil d'analyse de la composition logicielle, les notifications par e-mail peuvent être une fonctionnalité utile pour vous aider à rester informé des vulnérabilités potentielles dans vos dépendances open source.

Vous pouvez configurer ces notifications pour fournir des alertes lorsque de nouvelles vulnérabilités sont découvertes, lorsque des vulnérabilités existantes ont été corrigées, ou lorsque de nouvelles versions de dépendances sont disponibles pour résoudre les problèmes de sécurité.

En activant ces notifications, vous pouvez rapidement identifier et répondre aux menaces de sécurité potentielles et rester à jour avec les mises à jour de vos dépendances. Cela vous aide à maintenir la sécurité de vos applications.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-14.44.35.png)
_Exemples de notifications de Dependabot et Snyk_

## **Qu'est-ce que la prolifération des secrets ?**

La **prolifération des secrets** fait référence au problème croissant des secrets non contrôlés et non sécurisés dans les projets logiciels.

Les secrets, tels que les clés API, les mots de passe et autres informations sensibles, sont couramment utilisés dans le développement logiciel pour accéder de manière sécurisée aux ressources ou protéger les données sensibles. Mais les secrets sont souvent stockés sous forme non chiffrée dans le code source, les fichiers de configuration et autres artefacts, les rendant vulnérables au vol et à la mauvaise utilisation.

La prolifération des secrets peut survenir lorsque les secrets sont partagés ou dupliqués sur plusieurs systèmes, dépôts et équipes, rendant difficile le suivi de tous et assurant qu'ils sont gérés de manière sécurisée. Cela peut entraîner une série de problèmes de sécurité et de conformité, tels que des violations de données, des accès non autorisés et des violations réglementaires.

Pour lutter contre la prolifération des secrets, les organisations et les équipes de développement logiciel doivent mettre en œuvre des stratégies efficaces pour gérer les secrets, telles que le chiffrement des informations sensibles, le stockage des secrets dans un emplacement centralisé sécurisé, et l'accès uniquement aux utilisateurs autorisés. Ils doivent également avoir des processus robustes en place pour garantir que les secrets sont gérés de manière sécurisée tout au long de leur cycle de vie, de la création à la retraite.

### Analyse de la prolifération des secrets avec GitGuardian

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-14.48.21.png)
_[https://github.com/marketplace/gitguardian](https://github.com/marketplace/gitguardian)_

**GitGuardian** est un outil de sécurité qui aide les organisations et les développeurs à identifier et prévenir les potentielles violations de sécurité dans leurs dépôts de code.

Il fonctionne en scannant le code et les fichiers de configuration en temps réel, à la recherche de secrets, tels que des clés API, des identifiants et d'autres informations sensibles, qui peuvent avoir été accidentellement commis dans un dépôt.

GitGuardian s'intègre avec les systèmes de contrôle de version populaires, tels que GitHub et GitLab, et fournit aux développeurs des notifications et alertes en temps réel lorsque des informations sensibles sont détectées dans leur code.

L'outil fournit également une analyse détaillée du niveau de risque de chaque violation, y compris le type de secret, sa source et les actions que les développeurs peuvent entreprendre pour prévenir un incident de sécurité.

GitGuardian est conçu pour fonctionner de manière transparente avec le flux de travail de développement, aidant les développeurs à se concentrer sur leur travail tout en garantissant que les informations sensibles sont protégées à tout moment.

Il fournit une gamme de fonctionnalités de sécurité et de conformité, telles que la rotation automatique des secrets, l'application des politiques et la génération de rapports, en faisant une solution complète pour la gestion de la sécurité des dépôts de code.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-14.49.22.png)
_Écran avant l'installation de GitGuardian dans votre projet_

Vous pouvez choisir d'installer GitGuardian sur tous les dépôts ou sélectionner quelques dépôts. Je recommande de l'installer sur tous les dépôts. Cela vous donnera une visibilité sur tous les projets que vous avez réalisés et s'il y a des identifiants publics disponibles.

Une fois que vous avez téléchargé vos projets, vous pouvez vérifier sur le tableau de bord pour voir quels projets ont des secrets.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-14.49.46.png)
_Tableau de bord GitGuardian_

Il est important de garder à l'esprit que ces outils ont de nombreux points d'intégration. Ici, nous parlons de GitHub, mais vous pouvez implémenter certains d'entre eux sur GitLab ou BitBucket également.

Vous pouvez également implémenter ces outils comme une étape supplémentaire dans votre pipeline CI/CD en fonction des outils que vous utilisez, tels que Circle CI, Jenkins, GitHub Actions, Azure pipelines, etc.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-14.50.48.png)
_Les outils ont généralement de nombreuses intégrations pour vos projets_

Dans ce cas particulier, pour prévenir la prolifération des secrets, je recommanderais d'ajouter une **intégration de pré-commit git hook**. En incluant une étape de pré-commit, les développeurs peuvent scanner les changements de code pour détecter les secrets potentiels avant de les commettre dans le dépôt.

## Analyse statique du code

L'**analyse statique du code** est une technique utilisée dans le développement logiciel pour analyser le code sans l'exécuter. L'analyse est effectuée par des outils qui examinent le code et identifient les vulnérabilités de sécurité potentielles, les erreurs de codage et d'autres problèmes qui peuvent affecter la qualité et la stabilité du logiciel.

Les outils d'analyse statique du code utilisent une variété de techniques, telles que la correspondance de motifs, l'analyse basée sur des règles et l'analyse du flux de données, pour identifier les problèmes potentiels dans le code. Les résultats de l'analyse sont ensuite présentés au développeur sous forme d'avertissements, d'erreurs ou d'autres notifications, que le développeur peut utiliser pour améliorer la qualité et la sécurité du code.

Vous pouvez utiliser l'analyse statique du code à différentes étapes du cycle de vie du développement logiciel, depuis la conception et le développement initiaux, jusqu'aux tests et au déploiement. Elle peut aider à identifier les vulnérabilités de sécurité, telles que l'injection SQL, le cross-site scripting (XSS) et les débordements de tampon, ainsi que les erreurs de codage et les problèmes de performance.

### Analyse statique du code avec SonarCloud

**SonarCloud** est une plateforme basée sur le cloud pour l'analyse continue de la qualité et de la sécurité du code.

SonarCloud s'intègre avec les outils de développement populaires, tels que GitHub et GitLab, et fournit aux développeurs des retours en temps réel sur la qualité et la sécurité de leur code.

La plateforme offre une large gamme de fonctionnalités, y compris des métriques de qualité de code, des alertes de sécurité et des rapports de couverture de test, ce qui en fait une solution complète pour la gestion de la qualité et de la sécurité du code.

Vous pouvez choisir entre l'application :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-14.53.03.png)
_[https://github.com/marketplace/sonarcloud](https://github.com/marketplace/sonarcloud)_

ou l'action GitHub :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-14.54.16.png)
_[https://github.com/marketplace/actions/sonarcloud-scan](https://github.com/marketplace/actions/sonarcloud-scan)_

Une fois que vous avez importé votre projet, SonarCloud analysera la base de code :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-75.png)

et vous donnera des informations sur la santé de votre projet :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-76.png)

Cela inclut les vulnérabilités de sécurité que vous pouvez filtrer par gravité. L'outil vous indiquera quelles vulnérabilités posent problème et vous donnera plus de contexte pour les corriger.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-77.png)

Ces outils vous donnent également une cartographie de votre base de code pour la couverture, afin que vous sachiez quelles parties de votre base de code améliorer (écrire plus de tests, supprimer le code dupliqué et corriger les vulnérabilités de sécurité).

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-78.png)

### Analyse statique du code avec GitHub CodeQL

**GitHub CodeQL** est un outil d'analyse de code basé sur des requêtes développé par GitHub qui aide les développeurs à trouver et corriger les vulnérabilités dans leur code. Il utilise un langage de requête puissant et flexible, appelé CodeQL, pour rechercher des problèmes de sécurité et autres bugs dans les bases de code.

Avec GitHub CodeQL, les développeurs peuvent écrire des requêtes qui identifient des motifs spécifiques de code pouvant représenter des vulnérabilités de sécurité ou d'autres problèmes. Les requêtes sont ensuite exécutées contre la base de code, et les résultats sont présentés au développeur sous forme d'alertes, de notifications ou d'autres retours.

Sur votre dépôt, cliquez sur l'onglet **Actions** et tapez CodeQL dans la barre de recherche pour trouver le workflow.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-22-at-22.18.49.png)

Vous n'avez pas besoin de créer le fichier YAML à partir de zéro. Cliquez sur **Configurer** et vous devrez simplement vérifier si les langages de programmation inclus dans le fichier YAML sont corrects.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-80.png)

Vous pouvez ensuite cliquer sur **Start commit**. Maintenant, chaque fois qu'il y a des changements dans votre base de code via une pull request – comme défini en tant que déclencheur dans le fichier YAML – l'action CodeQL analysera le code poussé et vous informera s'il y a des vulnérabilités à corriger.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-81.png)

Vous pourrez vérifier la progression du workflow sous le même onglet.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-82.png)

Voici un exemple de vulnérabilités trouvées par CodeQL dans un dépôt vulnérable :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-83.png)

Si vous cliquez sur l'une des découvertes, vous obtiendrez plus de contexte sur la vulnérabilité :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-84.png)

## **Comment tout cela fonctionne-t-il sur GitHub ?**

Vous vous demandez peut-être comment nous allons voir tous ces outils fonctionner ensemble. Eh bien, toute la magie se produira sur la pull request qui servira de source de vérité.

Lorsque qu'un contributeur soumet une pull request, cela déclenchera toutes les applications, outils et actions que vous avez implémentés dans votre pipeline.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-85.png)

Lorsque vous faites défiler vers le bas de votre pull request, vous devriez voir la liste des outils que vous avez implémentés et leurs statuts.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-87.png)

Vous verrez si les outils sont réussis ou en échec, s'ils sont requis ou non (selon le flux de travail de votre équipe), et d'autres informations dont vous avez besoin avant de fusionner la pull request dans votre branche principale.

## Comment tirer parti de ChatOps

**ChatOps** est un modèle de collaboration qui combine des outils de communication en temps réel, tels que les plateformes de chat, avec l'automatisation et les flux de travail pour permettre aux équipes de travailler plus efficacement et plus efficacement.

ChatOps rassemble les personnes, les outils et les processus dans une interface basée sur le chat, telle que Slack ou Microsoft Teams, où les membres de l'équipe peuvent communiquer, collaborer et automatiser les tâches et les flux de travail.

Avec ChatOps, les membres de l'équipe peuvent utiliser des commandes de chat pour déclencher des flux de travail automatisés, tels que le déploiement de modifications de code, les alertes de surveillance et les actions de réponse aux incidents.

Cela peut aider les équipes à travailler plus efficacement en réduisant le temps et l'effort nécessaires pour effectuer des tâches répétitives, et en améliorant la communication et la collaboration entre les membres de l'équipe.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-88.png)
_Apporter de la visibilité dans vos canaux de communication_

ChatOps peut également aider les organisations à améliorer la sécurité en fournissant un emplacement central pour que les équipes partagent des informations liées à la sécurité et collaborent sur des tâches de sécurité.

Par exemple, les incidents de sécurité peuvent être signalés et triés via la plateforme de chat, et des commandes liées à la sécurité peuvent être déclenchées pour automatiser les flux de travail de sécurité, tels que l'analyse des modifications de code pour détecter les vulnérabilités ou la vérification des mauvaises configurations de sécurité dans l'infrastructure.

### Comment utiliser Slack pour ChatOps

Vous pouvez configurer un **compte Slack gratuit** et intégrer les outils que vous avez implémentés à partir de GitHub marketplace via des webhooks ou des applications. Vous pouvez également créer des canaux spécifiques par outils ou discipline pour avoir plus de visibilité et des personnes dédiées lorsqu'un problème survient.

Voici un exemple du **GitHub Bot** sur Slack. Vous avez des informations en temps réel lorsqu'une pull request est soulevée en utilisant différentes couleurs pour traduire le statut de l'ensemble du workflow incluant tous les outils que vous avez implémentés.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-90.png)
_GitHub Bot sur Slack_

## Y a-t-il une documentation sur GitHub ?

GitHub a introduit une nouvelle fonctionnalité appelée **Tables**. Elle est conçue pour aider les équipes à suivre et gérer les éléments de travail dans un format tabulaire.

Les Tables sont un type de tableau qui fournit une interface de type feuille de calcul pour gérer les données, avec des lignes et des colonnes que vous pouvez personnaliser pour afficher différents types d'informations.

Les Tables sont hautement personnalisables, avec une variété d'options pour trier, filtrer et regrouper les données. Les utilisateurs peuvent ajouter et supprimer des colonnes, réorganiser les colonnes et même enregistrer des vues personnalisées pour une utilisation future. Vous pouvez également filtrer les tables en fonction de critères spécifiques, tels que le statut des problèmes, l'assigné ou l'étiquette.

L'un des avantages des Tables est qu'elles fournissent une vue unique de plusieurs sources de données, ce qui facilite la visualisation de l'ensemble et l'identification des schémas à travers différents éléments de travail.

Par exemple, une équipe pourrait utiliser une Table pour suivre les problèmes et les pull requests à travers plusieurs dépôts, puis les regrouper par assigné pour voir quels membres de l'équipe sont responsables de quels éléments de travail.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-225.png)
_En savoir plus sur la gestion de projet. [https://github.com/features/issues](https://github.com/features/issues)_

Les Tables ne sont qu'une façon de faire de la gestion de projet sur GitHub, qui inclut également les **Projets** et les **Jalons**.

Les Projets sont plus flexibles que les Tables, et vous pouvez les utiliser pour gérer les éléments de travail dans une variété de formats, y compris des tableaux, des listes et des chronologies.

Vous pouvez utiliser les jalons pour suivre les progrès vers des objectifs spécifiques et regrouper les problèmes et les pull requests connexes.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-15.05.11.png)
_Exemple d'une liste de Jalons et d'Étiquettes_

Sous un Jalon, vous aurez une liste de problèmes sur lesquels les développeurs peuvent travailler. N'oubliez pas d'ajouter les étiquettes, les projets et les jalons à vos pull requests pour suivre les progrès et les refléter dans les Tables ou les Projets.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-15.05.38.png)

Voici un exemple de tableau. Vous pouvez utiliser des projets ou des tableaux automatisés où les cartes se déplaceront en fonction du statut de la pull request. C'est aussi un bon moyen de montrer sur quelle fonctionnalité vous travaillez et où vous pourriez avoir besoin d'aide et de contributeurs.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-93.png)

GitHub fournit plusieurs fonctionnalités de gestion de projet qui peuvent aider les équipes à organiser et suivre leur travail.

## Bonnes pratiques pour les logiciels open source

Nous avons vu comment implémenter des garde-fous de sécurité dans vos projets. Maintenant, examinons quelques bonnes pratiques pour les logiciels open source afin de renforcer vos projets !

### Appliquer le principe du moindre privilège

Dans le contexte de GitHub, appliquer le principe du moindre privilège signifie accorder aux utilisateurs et aux services uniquement le niveau d'accès minimum nécessaire pour effectuer leurs tâches requises, et rien de plus.

Cela est important pour des raisons de sécurité, car cela aide à minimiser l'impact potentiel d'une faille de sécurité ou d'une menace interne.

Vous pouvez encourager vos contributeurs à créer des mots de passe forts et à utiliser l'authentification multifacteur pour protéger davantage leurs comptes. Vous pouvez limiter l'accès aux dépôts uniquement aux utilisateurs qui en ont besoin. Par exemple, si un utilisateur n'a besoin que d'un accès en lecture à un dépôt, ne lui donnez pas d'accès en écriture.

Au lieu de gérer l'accès sur une base individuelle, utilisez des équipes pour gérer l'accès aux dépôts. Cela facilite l'ajout ou la suppression d'utilisateurs lorsque leurs rôles changent.

Au niveau de l'organisation, commencez par définir les permissions de base à **Aucune permission** afin que l'utilisateur ne puisse cloner et tirer que les dépôts publics.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-22-at-22.41.12.png)

De plus, GitHub fournit des jetons d'accès que vous pouvez utiliser pour vous authentifier avec l'API et d'autres services GitHub. Utilisez des jetons d'accès avec le moins d'accès nécessaire pour effectuer les tâches requises.

Encouragez également les utilisateurs à utiliser des applications OAuth et des applications GitHub, qui sont plus sécurisées que les jetons d'accès personnels.

Enfin, assurez-vous de réviser régulièrement l'accès que les utilisateurs ont aux dépôts et autres ressources sur GitHub pour vous assurer qu'ils en ont toujours besoin.

### Rendre l'authentification à deux facteurs obligatoire pour tous les mainteneurs et contributeurs

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-96.png)

Rendez l'authentification à deux facteurs obligatoire pour tous les mainteneurs et contributeurs. [D'ici la fin de 2023](https://github.blog/2022-05-04-software-security-starts-with-the-developer-securing-developer-accounts-with-2fa/), GitHub exigera que tous les utilisateurs qui contribuent du code sur GitHub.com activent une ou plusieurs formes d'authentification à deux facteurs (2FA) d'ici la fin de 2023.

### Réviser les contrôles de votre projet

Dans l'onglet **Paramètres** et sous **Sécurité et analyse du code**, vous pouvez activer ou désactiver Dependabot pour l'analyse de la composition logicielle.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-15.10.22.png)
_Contrôles de Dependabot_

Vous pouvez faire de même pour l'**analyse de code** où vous pouvez configurer des workflows et des règles de protection ainsi que l'**analyse des secrets**.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-15.11.13.png)
_Contrôles de l'analyse de code_

Pour les actions GitHub, vous pouvez **Autoriser les actions sélectionnées** et inclure les actions créées par GitHub et les actions marquées d'une coche bleue pour les créateurs vérifiés ainsi qu'une sélection d'actions spécifiées vérifiées par votre équipe. Dans ce cas, seules ces actions peuvent être utilisées dans vos projets.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-98.png)
_Permissions des actions GitHub_

### Protéger votre branche principale

Protéger la branche principale sur GitHub est important car elle représente la version stable et prête pour la production de votre code. C'est la branche qui est généralement déployée dans votre environnement de production, et tout changement apporté à cette branche peut avoir un impact significatif sur la stabilité et la sécurité de votre application.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-14.37.30.png)
_GitHub vous informera si votre branche principale n'est pas protégée_

Sans protection en place, tout utilisateur ayant un accès en écriture au dépôt pourrait potentiellement apporter des modifications à la branche principale sans aucune supervision ou contrôle, ce qui peut introduire des erreurs ou des vulnérabilités difficiles à détecter et à corriger.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-99.png)

En protégeant la branche principale sur GitHub, vous pouvez imposer des politiques et des règles pour garantir que toute modification apportée à la branche principale est examinée et approuvée par les parties prenantes appropriées. Vous pouvez également garantir qu'elles répondent à certains critères, tels que le passage de tests automatisés et de vérifications de qualité du code.

Cela aide à réduire le risque d'erreurs ou de vulnérabilités introduites dans votre environnement de production, et garantit que votre application reste stable et sécurisée.

Vous pouvez exiger que les vérifications de statut passent avant la fusion, ce qui inclurait tous les outils que vous avez implémentés dans votre flux de travail.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-15.11.59.png)
_Exiger des vérifications de statut avant la fusion_

Vous pourrez les voir lorsqu'une pull request est soulevée. Les vérifications requises auront une étiquette **Requis** à côté d'elles. Si elles échouent, la fusion est bloquée jusqu'à ce que vous corrigiez les problèmes.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-100.png)
_Résultats des vérifications de statut_

### Activer les notifications/alertes

Activer les notifications et alertes sur GitHub est important pour suivre les événements et changements importants dans vos dépôts. Cela garantira également que vous êtes informé des problèmes de sécurité ou de performance potentiels en temps opportun.

Vous pouvez personnaliser les notifications et alertes pour répondre à vos besoins. Vous pouvez inclure des choses comme les révisions de pull request, les mises à jour de problèmes, les nouveaux commentaires, les changements de code et les vulnérabilités de sécurité détectées dans vos dépendances.

En restant à jour avec ces notifications et alertes, vous pouvez vous assurer que vous êtes conscient des événements importants et pouvez agir en conséquence.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-101.png)
_Contrôler l'accès aux alertes_

Par exemple, si une nouvelle vulnérabilité est détectée dans l'une de vos dépendances, vous pouvez recevoir une notification et prendre des mesures pour corriger la vulnérabilité ou mettre à jour la dépendance. Cela peut aider à prévenir les violations de sécurité et protéger votre application contre les attaques potentielles.

De plus, activer les notifications et alertes peut aider à améliorer la collaboration et la communication au sein de votre équipe de développement, car cela fournit une visibilité sur les activités et les progrès des membres de l'équipe. Cela peut aider à garantir que tout le monde est sur la même longueur d'onde et que des progrès sont réalisés vers les objectifs du projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-102.png)
_Assurez-vous de mettre à jour la bonne adresse e-mail pour les notifications_

### Réviser tous vos webhooks et applications

Réviser vos webhooks et applications sur GitHub est important pour la sécurité et pour garantir que vos dépôts et applications fonctionnent comme prévu.

Les webhooks sont des messages automatisés envoyés depuis GitHub vers un système externe, tel qu'un outil d'intégration continue ou un chatbot. Ces webhooks peuvent fournir un moyen puissant d'automatiser votre flux de travail de développement et de vous intégrer avec des systèmes externes, mais ils peuvent également présenter un risque de sécurité s'ils ne sont pas correctement configurés.

En révisant vos webhooks, vous pouvez vous assurer que seuls les systèmes autorisés reçoivent les messages des webhooks, et que les informations envoyées sont appropriées et ne divulguent pas d'informations sensibles.

Vous pouvez également vous assurer que les événements des webhooks sont correctement gérés et qu'il n'y a pas d'erreurs ou d'autres problèmes avec la configuration.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-103.png)
_Si vous n'avez plus besoin d'un webhook, supprimez-le de votre projet !_

De même, réviser vos applications sur GitHub peut vous aider à vous assurer qu'elles fonctionnent comme prévu et ne divulguent pas d'informations sensibles.

Les applications peuvent accéder aux données de votre dépôt et effectuer des actions en votre nom, il est donc important de réviser leurs permissions et de vous assurer qu'elles sont uniquement autorisées à effectuer les actions nécessaires.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-104.png)

En révisant vos applications, vous pouvez vous assurer qu'elles sont correctement configurées et ne divulguent pas les données de votre dépôt ou d'autres informations sensibles.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-105.png)

### Réviser la liste de contrôle de l'aperçu de la sécurité

Sous l'onglet Sécurité dans votre dépôt, vous pouvez voir la liste de contrôle de l'aperçu de la sécurité. Cela inclut une politique de sécurité et des avis de sécurité, ainsi que l'endroit où vous pouvez activer les alertes Dependabot et les alertes d'analyse de code.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-106.png)
_Aperçu de la sécurité sous l'onglet Sécurité_

Vous pouvez inclure une **politique de sécurité** en tant que fichier **SECURITY.md** dans votre projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-107.png)
_Inclure une politique de sécurité_

### Réviser la liste de contrôle du profil de la communauté

Cette section est plus axée sur la communauté OSS et les bonnes pratiques en général. Assurez-vous que votre projet inclut une description, un fichier README, ainsi qu'un code de conduite et un guide de contribution.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-109.png)
_Assurez-vous que votre profil communautaire est en bonne forme_

Vous pouvez également définir des modèles pour les problèmes ou les pull requests afin de donner des directives aux futurs contributeurs.

### Implémenter les workflows open source

L'implémentation de GitHub Actions pour les workflows open source peut aider à rationaliser le processus de développement, à garantir des résultats cohérents et fiables, et à améliorer la qualité et la sécurité globales du projet.

Un aspect important de l'implémentation de GitHub Actions pour les workflows open source est de couvrir la première interaction avec les contributeurs et de fermer les problèmes obsolètes. Cela est important car les projets open source ont souvent un grand nombre de contributeurs, et il peut être difficile de suivre toutes les interactions et les problèmes qui nécessitent de l'attention.

Vous pouvez également utiliser GitHub Actions pour automatiser le processus de réponse aux nouveaux problèmes ou pull requests, et pour aider à garantir que les problèmes sont traités en temps opportun.

Par exemple, vous pouvez créer une action qui envoie une réponse automatique aux nouveaux problèmes ou pull requests, informant le contributeur que sa demande a été reçue et est en cours de révision.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-110.png)
_[https://github.com/marketplace/actions/first-interaction](https://github.com/marketplace/actions/first-interaction)_

De plus, vous pouvez utiliser GitHub Actions pour aider à fermer les problèmes obsolètes. Cela est important car les projets open source ont souvent un grand nombre de problèmes ouverts qui peuvent ne plus être pertinents ou avoir déjà été traités. En utilisant une action pour fermer automatiquement les problèmes obsolètes après une certaine période de temps, vous pouvez aider à garder votre projet organisé et garantir que seuls les problèmes pertinents sont traités.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-112.png)
_GitHub vous informera si certains de vos problèmes semblent être obsolètes !_

Dans l'ensemble, l'implémentation de GitHub Actions pour les workflows open source est une étape importante pour rationaliser le processus de développement, améliorer la qualité et la sécurité du projet, et garantir que les problèmes sont traités de manière opportune et cohérente.

En couvrant la première interaction avec les contributeurs et en fermant les problèmes obsolètes, vous pouvez aider à garder votre projet organisé et efficace, et améliorer l'expérience globale pour les contributeurs et les utilisateurs.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-111.png)
_[https://github.com/marketplace/actions/close-stale-issues](https://github.com/marketplace/actions/close-stale-issues)_

### Mettre en avant le statut de votre projet open source

Mettre en avant le statut de votre projet open source en utilisant des étiquettes ou des balises sur votre fichier README peut être un moyen utile de communiquer des informations importantes sur votre projet aux utilisateurs et contributeurs potentiels.

Ces étiquettes peuvent fournir un aperçu rapide de l'état actuel du projet, et peuvent aider les utilisateurs et contributeurs à comprendre ce qu'ils peuvent attendre du projet.

Vous pouvez inclure des étiquettes pour indiquer le statut de votre projet. Cela pourrait inclure des étiquettes comme "actif", "mode maintenance", ou "archivé", pour informer les utilisateurs et contributeurs si le projet est encore activement développé et maintenu.

Il est important de faire savoir aux utilisateurs et contributeurs quelles sont les conditions de licence pour votre projet. Utiliser une étiquette pour indiquer le type de licence peut être un moyen rapide et facile de communiquer cette information.

Si vous utilisez des outils d'intégration continue comme Jenkins ou CircleCI, vous pouvez utiliser des étiquettes pour indiquer le statut de construction actuel du projet.

Si vous utilisez un outil de couverture de code comme Codecov, vous pouvez utiliser des étiquettes pour indiquer le pourcentage actuel de couverture de code pour le projet.

Si votre projet utilise des outils de sécurité, vous pouvez utiliser des étiquettes pour mettre en avant la santé de la sécurité pour le projet. Cela peut aider les utilisateurs à comprendre la posture de sécurité de votre projet.

Dans l'ensemble, mettre en avant le statut de votre projet en utilisant des étiquettes ou des balises sur votre fichier README peut aider à fournir des informations importantes aux utilisateurs et contributeurs potentiels, et peut faciliter leur compréhension de ce qu'ils peuvent attendre du projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-113.png)
_Un exemple d'étiquettes pour mettre en avant la santé d'un projet_

C'est aussi un bon moyen d'attirer plus de contributeurs à votre projet. Les développeurs aiment contribuer à des projets qui ont des workflows stables.

Voici un exemple de création d'un badge de statut pour CodeQL :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-114.png)

Vous devrez copier/coller le Markdown dans votre fichier README.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-115.png)

Et cela ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-116.png)

### Vérifier/Ajouter une licence

Ajouter une licence à votre projet de logiciel open source (OSS) est important pour plusieurs raisons. En ajoutant une licence, vous clarifiez pour les autres ce qu'ils peuvent et ne peuvent pas faire avec votre logiciel. Cela offre une protection juridique à la fois pour vous et pour les autres qui pourraient vouloir utiliser ou contribuer à votre projet.

Une licence facilite la compréhension par les autres développeurs de la manière dont ils peuvent utiliser et contribuer à votre projet. Cela peut aider à construire une communauté forte et engagée autour de votre logiciel.

Ajouter une licence à votre projet peut aider à éviter les confusions et les malentendus sur ce qui est autorisé et ce qui ne l'est pas. Cela peut aider à prévenir les problèmes et les litiges à l'avenir.

Si vous ne savez pas par où commencer, vous pouvez choisir une licence open source qui convient à votre projet [ici](https://choosealicense.com/). GitHub peut ensuite générer la licence sélectionnée que vous pouvez ajouter à votre projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-117.png)
_Choisissez la bonne licence pour votre projet_

Vous pouvez ensuite modifier certaines informations comme l'année ou le nom complet. La licence sera alors enregistrée sous forme de fichier LICENSE.md ou LICENSE.txt dans votre dépôt.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-118.png)

## 5 conseils pour la sécurité OSS

Maintenant que nous avons une meilleure compréhension de ce à quoi ressemble une application moderne, comment la protéger en utilisant certains outils et comment renforcer vos projets, laissez-moi partager avec vous 5 conseils de sécurité.

### Conseil #1 – Adopter une approche DevSecOps

Adopter une approche DevSecOps est une étape importante vers la construction de logiciels sécurisés et résilients. DevSecOps rassemble les équipes de développement, de sécurité et d'exploitation pour garantir que la sécurité est une partie intégrante du cycle de vie du développement logiciel dès le début.

En intégrant la sécurité à chaque étape du processus de développement, les organisations peuvent identifier et résoudre les problèmes de sécurité dès le début, et construire des logiciels plus sécurisés.

DevSecOps implique l'utilisation d'outils de sécurité automatisés, de tests continus et d'analyse de code pour identifier les vulnérabilités, et garantir que la sécurité est intégrée à chaque aspect du processus de développement logiciel.

Cette approche peut aider les organisations à réduire le risque de violations de sécurité, et à construire des logiciels plus sécurisés et résilients capables de résister aux menaces évolutives.

Vous pouvez en apprendre davantage sur DevSecOps [dans ce cours de Beau Carnes](https://www.freecodecamp.org/news/what-is-devsecops/).

### Conseil #2 – Traiter les vulnérabilités open source

Traiter les vulnérabilités open source est crucial pour maintenir la sécurité des applications logicielles. Les bibliothèques et frameworks open source sont largement utilisés par les développeurs pour construire des logiciels, mais ils peuvent également introduire des vulnérabilités que les attaquants peuvent exploiter.

Pour traiter ces vulnérabilités, les organisations peuvent utiliser une variété d'outils et de techniques, telles que l'analyse de la composition logicielle et le scanning des vulnérabilités, pour identifier et suivre les vulnérabilités dans les composants open source.

Elles peuvent également prioriser et remédier à ces vulnérabilités en utilisant une approche basée sur les risques, qui implique d'évaluer la probabilité et l'impact d'une vulnérabilité, puis de prioriser les problèmes les plus critiques pour la remédiation.

De plus, les organisations peuvent tirer parti des bases de données de vulnérabilités open source et des divulgations de vulnérabilités pilotées par la communauté pour rester à jour sur les dernières vulnérabilités et problèmes de sécurité.

### Conseil #3 – Automatiser les tâches de sécurité simples

Automatiser les tâches de sécurité est une étape cruciale vers l'obtention d'une posture de sécurité plus efficace et plus efficiente. En automatisant les tâches de sécurité répétitives, les organisations peuvent libérer leurs équipes de sécurité pour se concentrer sur des problèmes plus complexes et critiques.

Cela peut également aider à améliorer la cohérence des processus de sécurité, réduire les erreurs et les omissions, et permettre une détection et une réponse plus rapides aux incidents de sécurité.

Vous pouvez appliquer l'automatisation à diverses tâches de sécurité, y compris le scanning des vulnérabilités, l'analyse de code, les tests de sécurité, le contrôle d'accès, la réponse aux incidents et la surveillance de la conformité.

### Conseil #4 – Être conscient de vos propres actifs

Être conscient de vos propres actifs et de votre visibilité est un aspect crucial pour maintenir une posture de sécurité solide. Les organisations doivent avoir une compréhension claire de leur propre infrastructure, systèmes et données, et s'assurer qu'elles ont une visibilité sur tous les aspects de leurs opérations.

Cela inclut la surveillance de leurs réseaux, applications et terminaux pour détecter les signes de compromission, ainsi que la révision régulière de leurs contrôles d'accès et privilèges pour s'assurer qu'ils sont appropriés et à jour.

De plus, les organisations doivent être conscientes de leurs actifs publics et prendre des mesures pour réduire leur exposition aux menaces potentielles, telles que l'utilisation de pare-feux, de pare-feux d'applications web et d'autres mesures de sécurité.

### Conseil #5 – Fournir une formation en sécurité pour les développeurs

Dans le monde d'aujourd'hui marqué par des violations de sécurité et des cyberattaques fréquentes, il est crucial que les développeurs aient une bonne compréhension des meilleures pratiques en matière de sécurité. La formation en sécurité pour les développeurs peut les aider à comprendre comment écrire du code sécurisé, identifier les vulnérabilités et adopter des mesures de sécurité tout au long du cycle de vie du développement logiciel.

En fournissant une formation en sécurité aux développeurs, les organisations peuvent s'assurer que leurs développeurs sont équipés des connaissances et des compétences nécessaires pour construire des applications sécurisées et prévenir les incidents de sécurité.

La formation en sécurité peut également aider à créer une culture de sensibilisation à la sécurité au sein de l'organisation, et garantir que tous les membres de l'équipe comprennent l'importance de la sécurité et sont capables de contribuer aux efforts de sécurité de l'organisation.

Vous pouvez utiliser la plateforme **Snyk Learn** comme point de départ. Snyk Learn enseigne aux développeurs comment rester en sécurité avec des leçons interactives explorant les vulnérabilités dans une variété de langages et d'écosystèmes.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-22-at-23.19.51.png)
_La plateforme Snyk Learn. https://learn.snyk.io/_

## Comment faire un impact dans la communauté des logiciels open source

**Hacktoberfest** est un événement annuel sponsorisé par DigitalOcean et GitHub, où des développeurs du monde entier contribuent à des projets open source tout au long du mois d'octobre.

L'événement vise à encourager les contributions aux projets open source et est ouvert à tous, quel que soit le niveau de compétence.

Pour participer, les développeurs doivent s'inscrire sur le site web de Hacktoberfest, puis effectuer quatre pull requests valides sur n'importe quel projet open source participant sur GitHub.

Une fois les pull requests acceptées, le développeur recevra un t-shirt gratuit en édition limitée. Hacktoberfest est un excellent moyen pour les développeurs de s'impliquer dans la communauté open source et de contribuer à des projets qu'ils utilisent et sur lesquels ils comptent.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-22-at-23.21.48.png)
_https://hacktoberfest.com/_

**The Big Fix** est un événement mondial organisé par Snyk, conçu pour aider les organisations à maintenir leurs dépendances open source sécurisées et à jour.

L'événement se déroule généralement sur une période d'un mois et propose une série d'activités telles que des sessions de codage en direct, des webinaires et des sessions de questions-réponses avec des experts de Snyk.

L'objectif de l'événement The Big Fix est d'encourager les développeurs à prendre des mesures proactives pour maintenir la sécurité et l'intégrité de leurs logiciels open source et de les éduquer, ainsi que les professionnels de la sécurité, sur les meilleures pratiques pour sécuriser leurs applications.

En participant à l'événement The Big Fix et en corrigeant au moins une vulnérabilité, les développeurs recevront un t-shirt gratuit en édition limitée.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-22-at-23.25.47.png)
_https://snyk.io/events/the-big-fix/_

## Points clés à retenir pour la sécurité open source 101

1. La mise en œuvre de pratiques de développement logiciel sécurisées est cruciale pour se protéger contre les cyberattaques et sauvegarder les données des utilisateurs.
2. Les projets open source peuvent bénéficier de l'utilisation d'outils de sécurité tels que l'analyse de la composition logicielle, l'analyse statique du code et les scanners de vulnérabilités pour identifier et remédier aux risques de sécurité potentiels.
3. Le marketplace GitHub offre une variété d'applications et d'actions de sécurité qui peuvent être utilisées tout au long du cycle de vie du développement logiciel pour automatiser les tâches de sécurité, imposer les meilleures pratiques et protéger le projet contre les vulnérabilités.
4. Pratiquer une bonne hygiène de sécurité, telle que l'activation des notifications et des alertes, la révision des webhooks et des applications, et la protection de la branche principale, peut aider à prévenir l'accès non autorisé et les violations de données.
5. Fournir une formation en sécurité pour les développeurs peut aider à sensibiliser à l'importance de la sécurité et garantir que les pratiques de codage sécurisé sont intégrées dans le processus de développement logiciel.

J'espère que cet article vous aidera à améliorer la posture de sécurité de vos projets !

Vous pouvez me suivre sur [Twitter](https://twitter.com/SonyaMoisset) ou sur [LinkedIn](https://www.linkedin.com/in/sonyamoisset/). N'oubliez pas de #**GetSecure**, #**BeSecure** & #**StaySecure** !

Oh, et une dernière chose avant de partir...

## NE PUSHEZ PAS VOS CLÉS SUR GITHUB !!!

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-15.38.21.png)