---
title: Guide de localisation – Comment traduire votre site web dans différentes langues
  du monde [Livre complet]
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2023-09-28T18:17:44.000Z'
originalURL: https://freecodecamp.org/news/localization-book-how-to-translate-your-website
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/Localization-Course-Handbook-Cover-Version-4.png
tags:
- name: book
  slug: book
- name: i18n
  slug: i18n
- name: localization
  slug: localization
- name: translation
  slug: translation
seo_title: Guide de localisation – Comment traduire votre site web dans différentes
  langues du monde [Livre complet]
seo_desc: 'Welcome! In a global world where information is available to everyone in
  just a few clicks, adapting your website and resources to other languages and cultures
  is essential to succeed.

  This book will teach you the fundamentals of localization and how...'
---

Bienvenue ! Dans un monde globalisé où l'information est accessible à tous en quelques clics, adapter votre site web et vos ressources à d'autres langues et cultures est essentiel pour réussir.

Ce livre vous enseignera les fondamentaux de la localisation et comment traduire votre site web pour atteindre une communauté mondiale d'utilisateurs sans aucune barrière linguistique.

## 🔹 Par où commencer

Mais par où commencer ?

C'est une question importante que les gestionnaires se posent souvent lorsqu'ils décident d'adapter leurs produits et de devenir multilingues.

Dans ce livre, vous apprendrez tous les fondamentaux de la localisation d'un point de vue conceptuel et pratique.

Vous apprendrez comment localiser des fichiers, des sites web, des jeux et tout autre type de ressource sur [Crowdin](https://crowdin.com/), la plateforme de gestion de localisation basée sur le cloud qui propulse l'effort de localisation de freeCodeCamp.

**Nous aborderons les points suivants :** 

* [freeCodeCamp comme exemple concret](#heading-freecodecamp-comme-exemple-concret)
* [Un effort de localisation par des humains, pour des humains](#heading-un-effort-de-localisation-par-des-humains-pour-des-humains)
* [Quels sont les fondamentaux de la localisation ?](#heading-quels-sont-les-fondamentaux-de-la-localisation)
* [Qu'est-ce que la localisation ?](#heading-questce-que-la-localisation)
* [Traduction vs Localisation](#heading-traduction-vs-localisation)
* [Importance de la localisation](#heading-importance-de-la-localisation)
* [Terminologies de la localisation](#heading-terminologies-de-la-localisation)
* [Traduction vs Relecture](#heading-traduction-vs-relecture)
* [Quels types de ressources peuvent être localisées ?](#heading-quels-types-de-ressources-peuvent-etre-localisees)
* [Formats de fichiers courants](#heading-formats-de-fichiers-courants)
* [Phases et rôles de la localisation](#heading-phases-et-roles-de-la-localisation)
* [Fondamentaux de Crowdin pour les projets de localisation](#heading-fondamentaux-de-crowdin-pour-les-projets-de-localisation)
* [Terminologies importantes pour Crowdin](#terminologies-importantes-pour-crowdin)
* [Premiers pas avec Crowdin](#heading-premiers-pas-avec-crowdin)
* [Comment créer un compte Crowdin](#heading-comment-creer-un-compte-crowdin)
* [Comment personnaliser votre profil Crowdin](#heading-comment-personnaliser-votre-profil-crowdin)
* [Comment créer un projet sur Crowdin](#heading-comment-creer-un-projet-sur-crowdin)
* [Aperçu du projet](#heading-apercu-du-projet)
* [Comment personnaliser les paramètres de votre projet dans Crowdin](#heading-comment-personnaliser-les-parametres-de-votre-projet-dans-crowdin)
* [Comment supprimer un projet dans Crowdin](#heading-comment-supprimer-un-projet-dans-crowdin)
* [Comment téléverser des fichiers vers votre projet Crowdin](#heading-comment-televerser-des-fichiers-vers-votre-projet-crowdin)
* [Comment commencer à traduire](#heading-comment-commencer-a-traduire)
* [Comment utiliser l'éditeur de traduction](#heading-comment-utiliser-lediteur-de-traduction)
* [Modes de l'éditeur de traduction](#heading-modes-de-lediteur-de-traduction)
* [Comment passer à un autre fichier](#heading-comment-passer-a-un-autre-fichier)
* [Comment voir toutes les chaînes](#heading-comment-voir-toutes-les-chaines)
* [Comment traduire les langues RTL](#heading-comment-traduire-les-langues-rtl)
* [Comment télécharger le(s) fichier(s) traduit(s)](#heading-comment-telecharger-les-fichiers-traduits)
* [Comment utiliser la mémoire de traduction (TM)](#heading-comment-utiliser-la-memoire-de-traduction-tm)
* [Glossaire](#heading-glossaire)
* [Vérifications d'assurance qualité (QA) dans Crowdin](#heading-verifications-dassurance-qualite-qa-dans-crowdin)
* [Comment téléverser des traductions existantes](#heading-comment-televerser-des-traductions-existantes)
* [Comment pré-traduire votre projet](#heading-comment-pre-traduire-votre-projet)
* [Traduction hors ligne](#heading-traduction-hors-ligne)
* [Explorer les projets publics](#heading-explorer-les-projets-publics)
* [Crowdin pour les équipes et les organisations](#heading-crowdin-pour-les-equipes-et-les-organisations)
* [Comment inviter des membres et des contributeurs au projet](#heading-comment-inviter-des-membres-et-des-contributeurs-au-projet)
* [Rôles du projet](#heading-roles-du-projet)
* [Comment assigner ou modifier les rôles](#heading-comment-assigner-ou-modifier-les-roles)
* [Gestionnaires de projet](#heading-gestionnaires-de-projet)
* [Tâches](#heading-taches)
* [Rapports de projet](#heading-rapports-de-projet)
* [Conversations sur Crowdin](#heading-conversations-sur-crowdin)
* [Intégrations Crowdin et outils de productivité](#heading-integrations-crowdin-et-outils-de-productivite)
* [Comment traduire un site web sur Crowdin](#heading-comment-traduire-un-site-web-sur-crowdin)
* [L'effort de traduction de freeCodeCamp](#heading-leffort-de-traduction-de-freecodecamp)

Êtes-vous prêt ? Commençons !

## 🔹 freeCodeCamp comme exemple concret

freeCodeCamp.org est un exemple concret d'organisation et de projet open-source qui a adopté le concept de localisation pour atteindre une communauté mondiale.

Notre programme de codage est disponible dans de nombreuses langues, notamment :

* Anglais.
* Espagnol.
* Chinois.
* Italien.
* Portugais.
* Ukrainien.
* Japonais.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/freecodecamp-language-dropdown-1.png)
_Comment choisir une langue sur freeCodeCamp._

Notre communauté travaille activement à la traduction de freeCodeCamp dans de nombreuses langues du monde, notamment :

* Arabe.
* Azéri.
* Bengali.
* Chinois simplifié.
* Néerlandais.
* Français.
* Allemand.
* Hébreu.
* Hindi.
* Indonésien.
* Italien.
* Japonais.
* Coréen.
* Népalais.
* Persan.
* Portugais.
* Roumain.
* Espagnol.
* Swahili.
* Turc.
* Ukrainien.
* Ourdou, et plus encore.

Nous avons de nombreuses langues mondiales disponibles pour la localisation et nous gérons également des publications localisées, des chaînes YouTube, des forums, etc.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/freecodecamp-crowdin-project.png)
_Projet de localisation du programme de codage et langues disponibles._

## 🔹 Un effort de localisation par des humains, pour des humains

Notre processus de localisation est axé sur ce qui compte le plus : notre incroyable communauté d'apprenants qui se réveillent chaque jour avec l'envie d'acquérir de nouvelles compétences.

Nous pensons que la langue et la culture ne doivent pas être des barrières à l'apprentissage. La connaissance doit être accessible dans le monde entier.

C'est pourquoi nous avons lancé ce processus et pourquoi nous poursuivrons nos efforts de localisation jusqu'à ce que nous atteignions notre objectif de garantir l'accès au savoir partout dans le monde.

L'un des aspects clés de notre processus de localisation est qu'il est géré et dirigé par des humains, pour des humains. Les traductions sont écrites et approuvées par des membres de notre incroyable communauté et de notre équipe.

Soyons honnêtes, n'importe qui peut dire quand une traduction a été générée automatiquement. Elle est beaucoup plus littérale, manque de clarté et semble déconnectée du contexte et du ton original du texte.

Les traducteurs humains sont bien meilleurs pour adapter les langues et traduire les phrases d'une manière qui semble plus naturelle dans différentes langues et cultures.

Chez freeCodeCamp, nous avons une communauté incroyable de contributeurs qui consacrent leur temps à traduire notre contenu et une équipe formidable de membres du personnel qui supervisent le processus avec l'objectif ultime de publier des traductions de haute qualité pour nos apprenants.

Depuis que nous avons lancé notre effort de localisation, plus de 2 000 traducteurs et plus de 60 relecteurs nous ont aidés à accomplir notre mission.

💡 **Conseil :** Si cela vous semble intéressant et que vous souhaitez rejoindre l'effort de traduction de freeCodeCamp, veuillez lire nos [directives de contribution](https://contribute.freecodecamp.org/#/index). À la fin de cet article, vous trouverez plus d'informations sur notre effort de localisation.

Gérer un projet d'une telle envergure avec une communauté mondiale de contributeurs peut sembler compliqué, n'est-ce pas ? Comment pouvons-nous accomplir tout cela en tant qu'organisation à but non lucratif ?

Vous obtiendrez des réponses à ces questions dans ce livre.

Nous couvrirons tous les fondamentaux de la localisation, ainsi que les fonctionnalités de base et avancées de [Crowdin](https://crowdin.com/).

Êtes-vous prêt ? Commençons.

## 🔹 Quels sont les **fondamentaux** de la **localisation ?**

Nous allons commencer par un aperçu des fondamentaux du processus de localisation et des étapes à suivre pour vous assurer que votre produit peut être utilisé sans aucune barrière linguistique ou culturelle.

### Qu'est-ce que la localisation ?

Tout d'abord, définissons la **localisation**.

Selon le [dictionnaire Cambridge](https://dictionary.cambridge.org/dictionary/english/localization), la localisation est définie comme :

> Le processus d'organisation d'une entreprise ou d'une industrie de manière à ce que ses activités principales se déroulent dans des zones locales plutôt qu'au niveau national ou international.

Dans le contexte des produits et services, la localisation signifie essentiellement les adapter à la langue et à la culture d'une population spécifique. Cela s'applique également aux produits logiciels car ils doivent aussi être adaptés à différentes cultures.

### Traduction vs Localisation

Vous serez peut-être surpris d'apprendre que le concept de localisation est différent de celui de traduction. Il est en fait plus large.

Le [dictionnaire Cambridge](https://dictionary.cambridge.org/dictionary/english/translation) définit la traduction comme :

> L'activité ou le processus consistant à changer les mots d'une langue en mots d'une autre langue ayant la même signification.

Notez la partie clé de cette définition : \"changer les mots pour garder la même signification.\"

La traduction consiste à changer les mots d'une langue vers une autre langue pour conserver leur sens original. C'est très utile mais un peu limité car son but est de dire exactement la même chose dans une langue différente.

Cependant, la localisation peut aller au-delà pour mieux adapter le contenu à une autre culture ou à un autre pays.

Par exemple, la localisation est particulièrement utile pour les campagnes de marketing et les publicités qui tentent d'atteindre des publics et de les convaincre d'acheter leurs produits. Certaines cultures peuvent mieux accepter certaines couleurs, ou avoir des expressions locales ou de l'argot avec lesquels la population locale est plus familière.

Dans ce cas, localiser la campagne est préférable à une traduction littérale mot à mot.

La **localisation continue** pousse ce concept un peu plus loin. Elle consiste à localiser un produit en continu au fur et à mesure qu'il est mis à jour ou étendu dans un cycle de développement de produit agile. Elle est souvent utilisée pour localiser des produits logiciels.

## Importance de la localisation

Pourquoi devriez-vous localiser votre produit ou votre plateforme ? Eh bien, le monde est très diversifié, et les différentes cultures ont leurs coutumes distinctives et parlent des langues différentes.

Saviez-vous que, selon la [Linguistic Society of America](https://www.linguisticsociety.org/content/how-many-languages-are-there-world), il existe plus de 6 000 langues dans le monde ?

Parmi les 20 langues les plus parlées au monde, on trouve celles-ci :

* Anglais.
* Chinois mandarin.
* Hindi.
* Espagnol.
* Français.
* Arabe.
* Bengali.
* Portugais.
* Ourdou.
* Allemand.
* Japonais.

💡 **Conseil :** Vous pouvez trouver plus d'informations sur les langues par nombre total de locuteurs dans [cet article](https://en.wikipedia.org/wiki/List_of_languages_by_total_number_of_speakers).

Une grande partie de la population mondiale n'est pas bilingue. Tout le monde n'a pas la possibilité d'apprendre et de maîtriser l'anglais comme langue seconde, mais chaque personne dans le monde est un utilisateur potentiel de votre produit ou plateforme.

C'est pourquoi la localisation peut être si importante pour vous.

Par exemple, si vous créez une plateforme éducative, vous pourrez atteindre les gens et accomplir votre mission à l'échelle mondiale en localisant votre site web et votre contenu.

Si vous construisez un produit ou une plateforme commerciale, chaque personne dans le monde peut être un utilisateur potentiel.

Ne laissez pas la langue devenir une barrière pour atteindre vos utilisateurs. La localisation peut être votre meilleure alliée.

## Terminologies de la localisation

Maintenant que vous savez pourquoi la localisation est si importante, plongeons dans quelques terminologies importantes que vous rencontrerez très souvent dans le contexte de la traduction et de la localisation.

### Internationalisation

> L'action de devenir ou de faire en sorte que quelque chose devienne international.  
> — [Dictionnaire Cambridge](https://dictionary.cambridge.org/dictionary/english/internationalization).

Dans le contexte de la localisation d'un produit logiciel, cela implique également d'adapter l'interface utilisateur pour fonctionner avec d'autres langues et de s'assurer qu'elle est prête à être traduite.

### Culturalisé

> Dérivant de, imposé par ou conditionné par la culture.  
> — [Dictionnaire Merriam-Webster](https://www.merriam-webster.com/dictionary/culturalized).

Chaque culture a des traditions et un vocabulaire différents. La culture peut jouer un rôle clé dans la manière dont les communautés adoptent les produits, les campagnes et les plateformes. Comprendre comment les adapter est très important pour réussir.

### Pseudolocalisation

Le préfixe _pseudo_ est défini comme :

> Prétendu et non réel.  
> — [Dictionnaire Cambridge](https://dictionary.cambridge.org/dictionary/english/pseudo).

C'est exactement ce qu'est la pseudolocalisation. C'est un processus de création de fausses traductions qui servent d'espaces réservés pour les traductions réelles dans une plateforme ou un produit.

Vous vous demanderez peut-être : \"Pourquoi aurions-nous besoin d'utiliser de fausses traductions ?\"

La réponse est que nous les utilisons pour vérifier si notre logiciel est prêt à gérer plusieurs langues avant même que le processus de traduction ne commence.

Vérifier si une langue qui a tendance à avoir des mots plus longs ou plus courts fonctionne bien avec notre interface utilisateur actuelle et vérifier si les langues s'écrivant de droite à gauche s'affichent correctement sont des cas d'utilisation courants.

Ce processus est également utile pour trouver toutes les chaînes qui pourraient encore être codées en dur dans les fichiers sources du projet. Vous devrez peut-être les déplacer vers le fichier de ressources où vous conservez toutes les chaînes de votre projet.

C'est l'objectif principal de la pseudolocalisation : vérifier si tout est prêt pour commencer à traduire.

### Traduction automatique (MT)

> Le processus d'utilisation de l'intelligence artificielle pour traduire automatiquement du texte d'une langue à une autre sans intervention humaine.  
> — [Amazon Web Services](https://aws.amazon.com/what-is/machine-translation/).

Nous parlerons de ce terme plus en détail car la plateforme de gestion de localisation que nous utiliserons pour traduire nos ressources possède cette fonctionnalité, et elle peut nous faire gagner beaucoup de temps.

### Mémoire de traduction (TM)

> Une base de données qui stocke des \"segments\", qui peuvent être des phrases, des paragraphes ou des unités de type phrase (en-têtes, titres ou éléments d'une liste) qui ont été précédemment traduits, afin d'aider les traducteurs humains.  
> — [Wikipedia](https://en.wikipedia.org/wiki/Translation_memory).

Grâce à cette fonctionnalité, vous pouvez enregistrer les traductions précédentes et les \"réutiliser\" pour gagner du temps.

💡 **Conseil :** Notez que les acronymes (MT et TM) sont très similaires mais ils sont différents. Prenez un moment pour comprendre les différences entre ces deux concepts car vous les verrez fréquemment dans ce livre.

### Grands modèles de langage (LLM)

> Algorithmes d'apprentissage profond capables de reconnaître, de résumer, de traduire, de prédire et de générer du contenu à l'aide de très grands ensembles de données.  
> — [Nvidia](https://www.nvidia.com/en-us/glossary/data-science/large-language-models/).

Ces termes sont fondamentaux si vous cherchez à vous plonger dans la traduction et la localisation.

Vous pouvez également trouver des mots qui utilisent des chiffres pour représenter des abréviations. On les appelle des numéronymes.

* **L10n** : ce numéronyme signifie Localisation. Le nombre 10 représente les 10 lettres entre le **l** au début et le **n** à la fin.
* **i18n** : ce numéronyme signifie Internationalisation (oui, c'est un mot très long !). Le nombre 18 représente les 18 lettres entre le **i** au début et le **n** à la fin.

💡 **Conseil :** Parfois, vous pouvez trouver L10n avec le L en majuscule ou en minuscule, comme ceci : l10n. Mettre le L en majuscule est utile pour le distinguer du i dans le numéronyme i18n (ils peuvent se ressembler beaucoup dans certains types de polices).

## Traduction vs Relecture

Un autre aspect important que vous devriez également connaître est la différence entre traduire et relire.

La **traduction** consiste à changer les mots d'une langue à une autre dans le but de conserver le même sens.

Mais une fois que les traducteurs ont terminé leur travail, l'équipe de localisation devra également réviser, éditer et approuver les traductions pour s'assurer que tout est précis et correct. Ce processus de vérification des traductions est appelé **relecture** (ou proofreading).

La traduction et la relecture sont des étapes différentes du processus de localisation. Nous examinerons ces processus plus en détail, et vous apprendrez les étapes impliquées et le rôle des membres de l'équipe pour s'assurer que le contenu est correctement localisé.

## Quels types de ressources peuvent être localisées ?

Quand on parle de traduction et de localisation, la première chose qui vient à l'esprit est la traduction de fichiers contenant du texte, n'est-ce pas ?

Mais ce n'est pas le seul type de ressource que nous pouvons localiser. Nous pouvons localiser des documents, des feuilles de calcul, des sites web, des jeux, des dialogues, des scripts, de l'audio, de la vidéo, des graphiques, etc.

Pensez aux podcasts et aux vidéos. Ils peuvent être localisés avec des voix off. Il nous suffit de traduire leurs transcriptions, de remplacer l'audio original et de synchroniser la narration traduite.

Les légendes et les sous-titres peuvent également être localisés. C'est aussi une forme de texte, mais elle provient d'une source vidéo. Vous pouvez voir comment différents types de fichiers peuvent être étroitement liés dans le processus de localisation.

Enfin, nous pouvons localiser des graphiques tels que des fichiers images, des campagnes de marketing visuel, des publicités, et plus encore.

Le point principal à souligner ici est que la localisation et la traduction ne se limitent pas aux ressources écrites. Il existe une grande variété de ressources que nous pouvons localiser pour atteindre un public plus large.

## Formats de fichiers courants

Dans la section précédente, nous avons parlé des différents types de ressources qui peuvent être traduites. Parlons maintenant des formats de fichiers que vous trouverez habituellement dans le contexte de la traduction. Vous pouvez également les trouver dans la plateforme de gestion de localisation sur laquelle nous allons travailler.

💡 **Conseil :** Même si vous n'utilisez pas ces formats de fichiers pour le moment, il est toujours utile de comprendre ce qu'ils font et ce qu'ils représentent. Ils peuvent s'avérer utiles à l'avenir, ou dans les cas où vous les trouverez dans la documentation d'un outil de localisation que vous utilisez.

### Fichiers CSV (Valeurs séparées par des virgules)

* Extension de fichier : `**.csv**`
* Il s'agit d'un format de fichier texte dans lequel les valeurs sont séparées par des virgules.
* Stocke des données tabulaires telles que des nombres et du texte.
* Chaque ligne représente généralement un enregistrement.
* Couramment utilisé pour l'échange de données et peut être traité à l'aide de langages de programmation.

### Fichiers HTML

* Extension de fichier : `**.html**`
* HTML signifie HyperText Markup Language.
* Il est utilisé pour représenter la structure et le contenu d'un site web.
* Si vous ouvrez ce fichier dans un navigateur, vous verrez le contenu du site web.

### Fichiers JSON

* Extension de fichier : `**.json**`
* JSON signifie JavaScript Object Notation.
* Stocke des données dans un format texte simple basé sur des paires clé-valeur.
* Utilisé pour l'échange de données, en particulier sur le web parce qu'il est léger.

### Fichiers Markdown

* Extension de fichier : `**.md**`
* Utilisé pour créer du texte formaté.
* C'est un langage de balisage léger avec une syntaxe spécifique.
* Les applications courantes incluent la rédaction de documentation logicielle, d'articles de blog et d'articles.

### Fichiers PO (Portable Object)

* Extension de fichier : `**.po**`.
* Utilisé par le système `**gettext**`, qui est couramment utilisé pour écrire des programmes multilingues. Il est également largement utilisé dans l'implémentation de `**GNU gettext**`.
* `**gettext**` est un standard dans de nombreux moteurs de développement de jeux, comme l'Unreal Engine. Il est utilisé dans de nombreux langages de programmation, notamment C, C++, PHP et Python.

### Fichier texte

* Extension de fichier : `**.txt**`
* Utilisé pour stocker du texte brut.
* Il ne contient pas d'images ou de caractères non textuels.

### XML (Extensible Markup Language)

* Extension de fichier : `**.xml**`
* Utilisé pour stocker, partager et reconstruire des données arbitraires.
* Couramment utilisé pour échanger des données sur Internet.
* De nombreux frameworks de localisation utilisent XML. Par exemple, Android utilise un format de fichier basé sur XML pour stocker du texte traduisible.

### Fichiers XLIFF

* Extension de fichier : `**.xliff**`
* XLIFF signifie XML Localization Interchange File Format.
* Utilise un format basé sur XML.
* Utilisé pour standardiser la manière dont les données localisables peuvent être transmises entre les outils de localisation.

### Fichiers XLSX

* Extension de fichier : `**.xlsx**`
* Utilisé pour stocker des données dans des feuilles de calcul.
* C'est une abréviation de \"Microsoft Excel Spreadsheet\".

### Fichiers RESX

* Extension de fichier : `**.resx**`
* Utilisé par les applications .NET pour stocker des ressources pouvant être localisées.
* Utilise un format de fichier basé sur XML.

Ce sont les formats de fichiers les plus utilisés que vous pouvez trouver dans les projets de localisation, mais il existe plus d'une centaine de formats de fichiers que vous pouvez utiliser.

Crowdin, la plateforme de gestion de localisation que nous utiliserons dans ce livre, prend en charge plus de 100 formats de fichiers.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/supported-formats.png)
_Aperçu des [formats pris en charge](https://store.crowdin.com/categories/file-formats) dans Crowdin._

## Phases et rôles de la localisation

Génial. Maintenant que vous en savez plus sur les types de fichiers que vous pourriez trouver dans un projet de localisation, allons un peu plus loin et voyons ce processus du point de vue de la gestion de projet.

Quelles étapes sont nécessaires pour localiser un projet ? Par où devriez-vous commencer ? Voici des étapes pour vous aider à répondre à ces questions :

### Étape n°1 - Définir la portée et les objectifs du projet

Avant de commencer à localiser un fichier, il est important de prendre un moment pour analyser la portée et les objectifs de votre projet.

Posez-vous les questions suivantes :

* Quel est votre public cible ?
* Qu'essayez-vous d'accomplir en localisant vos ressources ?
* Comment allez-vous atteindre ces objectifs ?
* Quelles parties de votre site web, jeu, vidéo ou ressource devez-vous localiser ?
* Avez-vous besoin de le traduire ou de le localiser (l'adapter) ? Parfois, la traduction peut suffire.
* Si vous devez l'adapter à d'autres cultures, comment y parviendrez-vous ?
* Demanderez-vous conseil à des personnes qui comprennent ces cultures ? Si oui, comment les contacterez-vous ?
* Si vous parlez d'autres langues, pouvez-vous traduire les ressources vous-même ou avez-vous besoin d'aide en fonction de la complexité de votre projet ?
* Quel est votre budget disponible ?
* Vos objectifs sont-ils réalistes compte tenu de votre budget actuel ?

Vous devez également déterminer qui va traduire vos ressources :

* Allez-vous traduire les ressources vous-même ?
* Allez-vous impliquer votre base d'utilisateurs ou votre communauté dans l'effort de traduction ?
* Allez-vous embaucher une équipe ou utiliser les services d'un fournisseur de traduction ?
* Allez-vous utiliser des processus automatisés comme la traduction automatique pour traduire ou pré-traduire des ressources avec l'intelligence artificielle ?

💡 **Conseil :** Crowdin propose une option pour embaucher leurs services de localisation et les services de leurs partenaires dans la Marketplace Crowdin.

Définir des objectifs clairs et réalistes peut être très utile pour éviter tout défi inattendu au cours du processus.

Notez vos objectifs et assurez-vous d'avoir un aperçu des étapes à suivre pour démarrer, exécuter et terminer le processus de localisation.

### Étape n°2 - Créer les fichiers sources à localiser

Maintenant que vous avez des objectifs clairs et une portée de projet bien définie, il est indispensable de disposer des fichiers sources du projet. Ce sont les fichiers que votre équipe de localisation va localiser.

Vous devez vous assurer que vous disposez de tous les fichiers sources et ressources nécessaires avant de commencer le processus de localisation.

Bien sûr, vous pouvez toujours ajouter de nouvelles ressources et du contenu plus tard dans le processus, mais avoir une idée initiale claire de la complexité d'un projet sera utile plus tard en termes de gestion du temps et de budget requis.

### Étape n°3 - Préparer votre logiciel pour l'internationalisation

Avant que le processus de localisation ne commence, vous devez préparer votre produit pour l'internationalisation, ce qui est très spécifique à la technologie utilisée.

C'est particulièrement vrai pour les produits logiciels. Les outils que vous utilisez pour internationaliser une application React.js peuvent être très différents des outils que vous utilisez pour une application Android, une application iOS ou un jeu.

Cependant, les approches et les concepts que vous utiliserez sont essentiellement les mêmes.

Vous devez réfléchir à la manière dont vous adapterez votre interface utilisateur et vos services à d'autres langues. Par exemple, certaines langues peuvent avoir des mots plus longs ou plus courts que la langue source et cela peut modifier l'affichage des éléments.

S'assurer que tout ressemble à ce que vous aviez prévu est très important, avant même que les traducteurs et les relecteurs ne s'impliquent dans le processus.

Une autre étape clé consiste à s'assurer que tout votre texte traduisible est séparé de votre code. Lorsque vous traduisez un logiciel, tout le texte traduisible est extrait dans un fichier de ressources qui peut être partagé avec des traducteurs ou téléversé sur une plateforme de gestion de localisation.

L'équipe Crowdin recommande de stocker les fichiers plus volumineux, tels que les pages HTML et les modèles d'e-mails, dans un répertoire séparé et de conserver un répertoire par langue cible. Ils suggèrent que \"si vous traduisez votre contenu dans 5 langues cibles, vous auriez 5 copies de vos fichiers de ressources avec les 'étiquettes d'interface' et 5 répertoires avec tous les autres actifs comme les fichiers HTML.\"

Si vous développez une application web, vous devrez également implémenter un routage multilingue. Votre application doit permettre aux utilisateurs de sélectionner leur langue préférée.

Pour ce faire, vous avez deux options. Vous pouvez :

* Ajouter le code de langue dans le nom de domaine. Par exemple : `**fr.exemple.com**`.
* Ajouter le code de langue à l'URL. Par exemple : **`exemple.com/fr`**.

Ceci est recommandé pour l'optimisation des moteurs de recherche (SEO).

Votre logiciel doit également être capable de gérer et d'afficher des nombres, des dates et des devises adaptés, car la localisation peut également impliquer de les adapter à différents formats pour différentes cultures.

Le contexte sera également très important. De nombreux outils d'internationalisation créent des fichiers de ressources avec une seule paire clé-valeur pour chaque morceau de texte. Ils associent chaque morceau de texte dans la langue source à sa traduction correspondante.

Mais il est très important de s'assurer que les fichiers de ressources de votre projet incluent également des informations contextuelles sur le contenu ou les éléments qui les entourent. Cela peut être très utile pour les traducteurs car ils peuvent choisir les meilleures traductions possibles en fonction du contexte entourant la chaîne.

Enfin, votre application doit également être capable de gérer correctement la pluralisation, car différentes langues peuvent avoir des formes plurielles différentes.

💡 **Conseil :** Certaines de ces fonctionnalités peuvent être disponibles avec le kit de développement logiciel (SDK) que vous utilisez, mais vous devrez peut-être en ajouter certaines à l'aide de bibliothèques tierces. Il est toujours important de considérer et de vérifier cela.

### Étape n°4 - Assembler une équipe

Si vous analysez la portée du projet et décidez que vous ne pouvez pas le réaliser seul, il est temps d'assembler une équipe.

Vous pouvez embaucher une équipe ou, si vous êtes une organisation à but non lucratif comme freeCodeCamp, utiliser le crowdsourcing pour demander de l'aide à votre communauté pour les traductions. Vous pourriez être surpris par le nombre de membres généreux et bienveillants de votre communauté qui seront prêts à vous aider à atteindre vos objectifs.

Une fois que vous avez votre équipe, vous pouvez leur assigner des rôles :

* Les **Traducteurs** utilisent la plateforme de gestion de localisation que vous avez choisie pour traduire les ressources.
* Les **Relecteurs** révisent, éditent et approuvent les traductions. Il est toujours utile de revoir les traductions pour corriger les fautes de frappe ou les incohérences.
* Les **Développeurs** travaillent sur l'intégration des outils que vous choisissez pour automatiser le processus de localisation.
* Les **Gestionnaires de projet** coordonnent les tâches du projet. Ils assignent les traducteurs et les relecteurs à des tâches spécifiques pour s'assurer que le projet avance aussi vite que possible.

### Étape n°5 - Choisir les outils de localisation

Choisir le bon outil de localisation peut être essentiel pour atteindre vos objectifs. Dans le monde de la localisation, il existe un outil appelé Système de gestion de traduction (TMS).

Ce type de système est conçu pour vous aider à automatiser les tâches répétitives dans le but d'optimiser le flux de travail de votre équipe. Les humains auront toujours un rôle à jouer dans le processus de localisation, mais avec l'aide d'un système de gestion de traduction, ils peuvent atteindre leurs objectifs beaucoup plus rapidement.

Habituellement, ces systèmes peuvent être intégrés à des systèmes de gestion de contenu (CMS) pour importer automatiquement du contenu d'autres plateformes, telles que des plateformes de blogs. Une fois importé, vous pouvez le localiser et l'exporter afin de publier les versions traduites.

Avec les intégrations appropriées, les systèmes de gestion de traduction peuvent également vérifier s'il y a eu des changements dans les fichiers sources et importer automatiquement le nouveau contenu pour commencer à le localiser.

Un exemple concret de ce processus se trouve juste à côté de nous — freeCodeCamp traduit ses fichiers sources dans Crowdin. Lorsqu'un fichier du programme de freeCodeCamp change, le nouveau contenu est mis à jour automatiquement dans le système, afin que les contributeurs puissent le traduire et le publier très rapidement.

L'automatisation de ce processus peut être très utile, en particulier pour les grandes organisations ayant différents projets et fichiers, afin que vous n'ayez pas à suivre ces changements manuellement.

### Étape n°6 - Traduire les ressources

Si vous avez déjà choisi un système de gestion de traduction ou un autre outil utile, il est temps de commencer à traduire les ressources.

Habituellement, ces plateformes divisent le contenu source en ce qu'elles appellent des \"chaînes\" (strings), qui sont des parties du texte original que vous pouvez traduire. Les traducteurs traduiront les chaînes et enregistreront leurs traductions.

Le logiciel se chargera de stocker et de combiner les chaînes pour les remplacer au bon endroit dans votre fichier.

### Étape n°7 - Relire les traductions

La relecture est l'une des parties les plus importantes du processus car c'est comme la dernière étape d'assurance qualité effectuée par des humains.

Les relecteurs doivent vérifier si les traductions sont exactes et s'il existe une meilleure façon de les adapter à la culture ou à la langue. Ils peuvent également vérifier s'il y a des fautes de frappe ou des mots mal orthographiés, et si le format correct est utilisé. Ils peuvent éditer et approuver les chaînes traduites.

Parfois, ils peuvent trouver une virgule en trop, un emoji manquant, un espace supplémentaire ou une lettre manquante, et ces petits détails comptent vraiment pour l'expérience utilisateur, cette étape doit donc être prise très au sérieux.

### Étape n°8 - Exporter les ressources localisées

Après avoir relu et approuvé toutes les traductions, la prochaine chose à faire est d'exporter les ressources localisées finales.

Si votre projet est petit, vous pouvez choisir de le faire manuellement. Mais si votre projet est plus complexe, vous pouvez choisir d'automatiser ce processus avec différentes intégrations sur votre système de gestion de localisation.

Par exemple, Crowdin propose des intégrations avec différentes plateformes, notamment GitHub, Google Drive, Google Sheets, Dropbox, MailChimp, etc.

Si vos traductions sont prêtes et approuvées et que vous avez configuré une intégration GitHub, les fichiers traduits seront mis à jour automatiquement dans le dépôt de votre projet. Vous pouvez même configurer l'endroit où les fichiers traduits seront stockés.

### Étape n°9 - Vérifier les changements

Les projets et les plateformes peuvent évoluer au fil du temps. Les fichiers peuvent changer à mesure que vous ajoutez de nouvelles fonctionnalités et du contenu. C'est particulièrement vrai pour freeCodeCamp puisque nous ajoutons du nouveau contenu et mettons à jour notre contenu existant régulièrement.

Alors, comment pouvons-nous gérer ces changements et tout de même garder notre plateforme correctement localisée ?

Grâce à Crowdin, nous pouvons utiliser des intégrations pour être informés des modifications apportées aux fichiers et nous pouvons savoir si nous avons de nouvelles chaînes à traduire.

Lorsque cela se produit, notre incroyable équipe de contributeurs et de membres du personnel commencera à traduire et à relire les nouvelles chaînes, répétant ce cycle chaque fois que nous devons ramener le pourcentage de traduction à 100 %.

## 🔹 **Fondamentaux de Crowdin pour les projets de localisation**

Maintenant que nous avons couvert les concepts fondamentaux de la localisation, nous allons les utiliser dans la plateforme de gestion de localisation qui propulse l'effort de localisation de freeCodeCamp.

### Qu'est-ce qu'une plateforme de gestion de localisation ?

Il s'agit d'une plateforme qui vous aide, vous et votre équipe, à localiser vos ressources, produits et plateformes de manière efficace grâce à l'automatisation, des services basés sur le cloud et des intégrations avec d'autres plateformes.

Nous avons déjà parlé des plateformes de gestion de traduction, n'est-ce pas ?

Les plateformes de gestion de localisation sont très similaires, mais elles vous aident à localiser vos produits, ce qui est encore plus large que la simple traduction du texte mot à mot.

### Qu'est-ce que Crowdin ?

Crowdin est une plateforme de gestion de localisation qui peut être décrite comme :

> Une solution basée sur le cloud qui simplifie la gestion de la localisation pour votre équipe. ([Source : Crowdin](https://crowdin.com/))

![Image](https://www.freecodecamp.org/news/content/images/2023/09/crowdin-landing-page.png)
_Page d'accueil de Crowdin._

L'équipe mentionne que : \"C'est l'endroit idéal pour gérer efficacement tout votre contenu multilingue. Il vous permet de rationaliser le processus de localisation et de maintenir votre flux de travail agile.\"

Cette plateforme est également idéale pour les équipes et les organisations qui prévoient de localiser leur contenu dans plusieurs langues.

Voici le [site officiel de Crowdin](https://crowdin.com/) au cas où vous voudriez y jeter un coup d'œil :

%[https://crowdin.com/]

Vous appliquerez vos connaissances en localisation sur cette plateforme, et vous apprendrez même comment localiser un site web en quelques minutes seulement grâce aux services et intégrations de Crowdin.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/crowdin-workflow.png)
_Flux de travail Crowdin. Image tirée du [site officiel](https://crowdin.com/) de Crowdin._

### Le fondateur de Crowdin

[Serhiy Dmytryshyn](https://crowdin.com/page/about-crowdin) est le fondateur et PDG de Crowdin. Il a lancé l'entreprise en 2009 et elle compte aujourd'hui plus de 2 millions d'utilisateurs enregistrés dans plus de 160 pays.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Founder-and-CEO-of-Crowdin.png)
_[Serhiy Dmytryshyn](https://crowdin.com/page/about-crowdin), fondateur et PDG de Crowdin._

Nous avons eu l'occasion de le rencontrer et de lui demander comment il décrirait Crowdin en cinq mots. Sa réponse a été :

> Localisation continue pour les entreprises modernes.  
> — Serhiy Dmytryshyn

Sa vision est que Crowdin soit la meilleure plateforme pour localiser des produits qui évoluent constamment et pour des projets qui n'auront peut-être jamais de version finale car ils seront continuellement améliorés, étendus et mis à jour, tels que les produits logiciels.

freeCodeCamp en est un exemple. Nous ajoutons et mettons à jour constamment notre contenu, ce qui signifie que nous avons également besoin d'un processus de localisation efficace et agile pour maintenir notre plateforme accessible et à jour pour notre communauté mondiale.

L'[objectif principal](https://crowdin.com/page/about-crowdin) de Crowdin est de :

> Étendre le potentiel de la localisation agile.

Mais qu'est-ce que la localisation agile ? Voyons cela.

### Qu'est-ce que la localisation agile ?

La localisation agile est un processus dans lequel la localisation est intégrée dans un cycle de développement de produit agile, dans le but de localiser le produit aussi rapidement que possible au fur et à mesure de son évolution.

**💡 Conseil :** Un cycle de développement de produit agile est un cycle dans lequel un produit est constamment mis à jour selon une approche itérative.

Un processus de localisation agile diffère du processus de localisation traditionnel en ce que les traductions ne sont pas seulement écrites une seule fois puis ajoutées au produit final. Elles sont continuellement ajoutées et mises à jour au fur et à mesure que le produit change.

Cela semble génial, n'est-ce pas ?

Mais des mises à jour constantes nécessitent également une gestion constante, un travail d'équipe, des téléversements et téléchargements de fichiers, des déploiements de plateforme, etc.

Ce processus pourrait devenir compliqué très rapidement si votre équipe ne dispose pas des bons outils, mais avec une plateforme de gestion de localisation comme Crowdin, vous et votre équipe pouvez gagner du temps et atteindre vos objectifs plus efficacement.

### Avantages de Crowdin

Voyons quelques-unes des raisons pour lesquelles vous devriez utiliser Crowdin :

* Vous pouvez connecter votre projet à des services externes via des intégrations pour automatiser une partie du processus de localisation.
* Vous pouvez stocker vos traductions sur leurs services basés sur le cloud et accorder l'accès aux membres de l'équipe et aux contributeurs du monde entier.
* Vous pouvez générer automatiquement des traductions automatiques lorsqu'une ressource est créée et demander aux traducteurs de les vérifier et de les éditer pour gagner du temps.
* Votre équipe peut vérifier la qualité et le format des traductions grâce aux fonctionnalités d'assurance qualité, de vérification orthographique et de relecture de Crowdin.
* Vous pouvez générer des rapports, communiquer avec les membres de l'équipe en interne, attribuer des rôles et des autorisations, inviter de nouveaux membres, et bien plus encore.

Fondamentalement, c'est une plateforme qui facilitera grandement le processus de localisation pour vous et votre équipe.

### Plan gratuit de Crowdin

Une excellente chose à propos de Crowdin est qu'ils proposent un plan complètement gratuit avec toutes les fonctionnalités essentielles pour que les traducteurs commencent à localiser leur contenu.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/crowdin-free-plan.png)
_Fonctionnalités gratuites de Crowdin._

Oui, c'est gratuit ! Il vous suffit de créer un compte et vous pourrez :

* Créer un nombre illimité de projets publics que tout le monde peut voir et auxquels tout le monde peut contribuer.
* Ajouter un nombre illimité de traducteurs à vos projets publics.
* Créer un projet privé.
* Héberger jusqu'à 60 000 mots dans vos traductions.
* Utiliser des fonctionnalités utiles pour améliorer l'efficacité des traducteurs.
* Ajouter une intégration à votre projet (nous parlerons des intégrations dans un instant).

Lorsque vous vous inscrivez et créez votre compte, vous pouvez également commencer un essai gratuit de 14 jours de leur plan Team et ils ont également une période d'essai de 30 jours pour leur plan Business.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/free-trial.png)
_Foire aux questions (FAQ)._

Crowdin propose également [d'autres plans](https://crowdin.com/pricing#annual) pour répondre à vos besoins.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/crowdin-pricing.png)
_Les plans parmi lesquels vous pouvez choisir._

### Crowdin pour les projets open-source et les institutions éducatives

En tant qu'organisation à but non lucratif, freeCodeCamp bénéficie d'une licence spéciale que Crowdin accorde aux projets open-source et aux institutions éducatives pour soutenir leur mission.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/crowdin-for-nonprofits.png)
_Foire aux questions (FAQ)._

Si vous représentez un projet open source ou une institution éducative, vous pouvez contacter Crowdin pour une [demande Open Source](https://crowdin.com/page/open-source-project-setup-request) ou une [demande de licence académique](https://crowdin.com/page/academic-license-project-setup-request).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/crowdin-for-open-source.png)
_Crowdin pour l'Open Source._

L'équipe Crowdin vous assistera, vous et votre organisation.

## Terminologies importantes pour utiliser Crowdin

Avant de passer à la pratique avec les fonctionnalités de Crowdin, parlons un peu des terminologies importantes pour travailler avec les plateformes de gestion de localisation.

Vous trouverez ces termes très souvent dans les sections qui suivent, alors parlons-en en détail.

### Chaînes (Strings)

Lorsque vous téléversez une ressource sur Crowdin, la plateforme doit diviser le texte en plus petits \"segments\" qui peuvent être traduits et enregistrés individuellement jusqu'à ce que toutes les traductions soient prêtes. Ces segments du texte original sont ce que nous appelons des \"chaînes\". Une fois qu'elles ont été traduites et approuvées, elles peuvent être combinées pour générer la version localisée de la ressource.

**💡 Conseil :** Vous pouvez considérer les chaînes comme les plus petites unités du processus de traduction. Nous ne traduisons pas le texte mot à mot. Nous les traduisons chaîne par chaîne.

### Langue source

La langue source est la langue originale de la ressource. Par exemple, la langue source de freeCodeCamp est l'anglais puisque le programme et la documentation sont créés en anglais.

### Langue cible

C'est la langue dans laquelle nos ressources sont traduites. Par exemple, les projets de freeCodeCamp ont différentes langues cibles car nous traduisons nos ressources dans différentes langues.

### Mémoire de traduction (TM)

C'est comme une base de données où nous stockons tous les \"segments\" précédemment traduits de notre projet. Nous pouvons stocker des phrases, des paragraphes ou d'autres unités de texte avec leurs segments sources correspondants. L'objectif est de réutiliser les mêmes traductions plus tard dans les projets lorsque nous les retrouvons. C'est une fonctionnalité qui peut vous faire gagner beaucoup de temps car il ne faut que quelques secondes pour choisir une traduction enregistrée. Nous pouvons les adapter si nécessaire, mais nous aurons toujours une base sur laquelle travailler.

### Traduction automatique (MT)

Ce processus implique un logiciel informatique traduisant automatiquement les ressources de votre projet sans aucune intervention humaine. Habituellement, l'intelligence artificielle et l'apprentissage automatique font partie de ce processus. Les traducteurs et les relecteurs peuvent ensuite prendre les traductions générées par ordinateur et les adapter ou les corriger au besoin.

💡 **Conseil :** Veuillez noter que la mémoire de traduction (TM) et la traduction automatique (MT) sont très différentes même si leurs acronymes sont très similaires. Cela peut être un peu déroutant au début, mais rappelez-vous toujours que \"mémoire\" fait référence à une base de données de traductions et \"machine\" fait référence à un processus de traduction automatisé.

### Vérifications QA

QA signifie \"Quality Assurance\" (Assurance Qualité). C'est le processus consistant à vérifier si les traductions ont le format et l'orthographe corrects. Crowdin dispose de nombreuses fonctionnalités de QA qui peuvent aider votre équipe à trouver et à corriger toute erreur potentielle.

### Glossaire

Il s'agit d'une base de données de termes importants dans votre projet avec leurs significations correspondantes. L'objectif de la création et de la maintenance d'un glossaire est de donner à vos traducteurs plus de contexte sur les termes et de les aider à choisir les traductions les plus précises.

### Capture d'écran (Screenshot)

Une image de ce que vous pouvez voir sur l'écran de votre ordinateur à un moment donné. Elle est stockée sous forme de fichier image.

### Crowdsourcing

Il s'agit d'une pratique de localisation basée sur la coopération communautaire. Fondamentalement, si vous êtes une organisation et que votre objectif est de traduire vos ressources dans de nombreuses langues, vous pouvez demander l'aide de votre communauté. L'effort de traduction de freeCodeCamp est un exemple de crowdsourcing.

### Pré-traduction

Il s'agit d'une technique automatisée que vous pouvez utiliser dans Crowdin pour pré-traduire votre projet automatiquement en utilisant soit la traduction automatique (MT), soit la mémoire de traduction (TM). Ensuite, vos traducteurs peuvent vérifier les traductions générées par ordinateur et les adapter au besoin.

### Intégrations

Ce sont des connexions que vous pouvez établir entre Crowdin et d'autres applications ou services, tels que GitHub, Google Drive, Google Sheets, etc. C'est ainsi que freeCodeCamp maintient son dépôt GitHub traduit. Lorsque nous ajoutons de nouvelles chaînes, elles sont automatiquement téléversées sur Crowdin et les contributeurs peuvent commencer à travailler dessus.

### Webhooks

Ce sont des \"messages\" automatisés qu'une application ou une plateforme enverra à une autre application ou plateforme lorsque des événements spécifiques se produisent. Dans Crowdin, vous pouvez les envoyer lorsque les traductions sont terminées, lorsque les fichiers sont relus, etc.

### Interface de ligne de commande (CLI)

Il s'agit d'une interface utilisateur textuelle que nous pouvons utiliser pour interagir avec un programme informatique en saisissant des commandes. Crowdin dispose d'une interface de ligne de commande (CLI) appelée Crowdin Console Client qui vous permet de synchroniser les ressources de localisation avec votre projet.

### Interface de programmation d'application (API)

Il s'agit d'un intermédiaire qui permet à deux applications de communiquer entre elles en envoyant des informations selon des protocoles spécifiques. Crowdin dispose également d'une API qui peut vous aider à intégrer la localisation dans votre processus de développement.

### Variables personnalisées

Dans Crowdin, vous pouvez spécifier des variables qui ne doivent pas être traduites. Elles seront mises en évidence dans les chaînes sources que les traducteurs peuvent voir. Pour activer cette fonctionnalité, vous devrez contacter l'équipe d'assistance de Crowdin.

## Premiers pas avec Crowdin

Après cette introduction détaillée mais super importante sur les fondamentaux de la localisation, il est maintenant temps de passer à la pratique et de commencer à travailler sur Crowdin.

### Comment créer un compte Crowdin

Si votre objectif est de créer un projet sur Crowdin, vous devrez créer un compte si vous n'en avez pas déjà un.

Pour ce faire, rendez-vous sur [crowdin.com](https://crowdin.com/).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/crowdin-landing-page-signed-out.png)
_Page d'accueil de Crowdin._

Cliquez sur Sign up (S'inscrire).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/sign-up.png)
_Bouton d'inscription._

3. Créez votre compte en remplissant et en soumettant le formulaire. Vous devrez saisir votre e-mail, votre nom d'utilisateur et votre mot de passe. Vous devrez également accepter les conditions en cochant la case.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/sign-up-form.png)
_Formulaire d'inscription._

**💡 Conseil :** Après votre inscription, vous devrez confirmer votre adresse e-mail. Vous recevrez un e-mail de Crowdin avec un lien sur lequel vous pourrez cliquer pour accéder à votre profil. Vous devriez voir un message de confirmation indiquant que votre e-mail a été confirmé.

Après vous être inscrit (ou connecté si vous avez déjà un compte), vous verrez votre nouveau profil Crowdin où vous pourrez gérer vos projets, les membres de votre équipe, les flux de travail, l'activité, etc.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/new-profile.png)
_Nouveau profil Crowdin._

🎉 Félicitations ! Vous avez maintenant votre compte Crowdin et vous êtes prêt à commencer à personnaliser votre profil.

### Comment personnaliser votre profil Crowdin

Pour personnaliser votre profil :

Cliquez sur la petite image de profil en haut à droite, et choisissez \"Settings\" (Paramètres) dans le menu déroulant.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/settings-menu.png)
_Personnaliser votre profil._

Vous verrez votre profil et les informations que vous pouvez personnaliser, telles que votre :

* Image de profil.
* Nom complet, nom d'utilisateur et e-mail.
* Entreprise et titre de poste.
* Genre.
* Une brève description de vous.
* Langue, fuseau horaire et format de l'heure.
* Langues préférées.
* Apparence (clair, sombre ou basé sur votre heure locale).
* Confidentialité. Par défaut, votre profil est public. Cochez cette option si vous souhaitez rendre votre profil privé.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/black-profile-1.png)
_Paramètres du compte > Profil._

💡 **Conseil :** À partir de cette page, vous pouvez également supprimer votre compte. Vous verrez un bouton rouge en bas et un avertissement sur les conséquences d'une telle action. Vous ne devez cliquer sur ce bouton que si vous êtes absolument sûr de vouloir supprimer tous vos projets et les données qui y sont associées.

### Comment créer un projet sur Crowdin

Maintenant que vous savez comment personnaliser votre profil, créons un projet. Vous pouvez créer un projet à partir de votre page de profil.

Si vous êtes dans une autre partie de la plateforme, vous pouvez revenir à votre profil en cliquant sur votre petite image de profil en haut à droite et en cliquant sur \"Profile\", comme vous pouvez le voir dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/go-back-to-profile.png)
_La page de profil._

Pour créer un projet, cliquez sur le bouton \"Create Project\" (le vert ou le gris, ils sont tous deux équivalents).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/create-a-profile.png)
_Créer un projet (bouton vert)._

![Image](https://www.freecodecamp.org/news/content/images/2023/09/create-a-profile-2-1.png)
_Créer un projet (bouton gris)._

Vous verrez une page où vous pourrez remplir les informations de base sur votre projet, telles que :

* Nom.
* Adresse du projet. C'est l'URL de votre projet. Si l'adresse de votre projet comporte plusieurs mots, séparez-les par des tirets (-).
* Paramètres de confidentialité (public ou privé).
* La langue source.
* La ou les langue(s) cible(s).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/create-a-project.png)
_Création d'un projet._

💡 **Conseil :** L'adresse de votre projet doit être unique. Elle sera remplie automatiquement lorsque vous écrirez le nom de votre projet. Si elle est déjà prise par un autre utilisateur, vous verrez un avertissement rouge et vous devrez en choisir une autre.

Vous pouvez choisir autant de langues cibles que nécessaire. Cochez simplement leurs cases et elles seront ajoutées.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/target-languages.png)
_Langues cibles._

Voici ce que vous devriez voir lorsque vous commencez à choisir vos langues cibles :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/target-languages-selected.png)
_Choix de quelques langues cibles._

Vous avez également la possibilité de pré-remplir la sélection avec les 30 langues les plus utilisées sans les sélectionner manuellement :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/select-top-30-languages.png)
_Sélectionner les 30 langues principales._

💡 **Conseil :** Vous pouvez également créer des langues personnalisées ou copier la sélection que vous avez faite pour un autre projet.

Si vous choisissez d'ajouter une langue personnalisée, vous verrez ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/adding-a-custom-language.png)
_Ajout de langues personnalisées._

Puisqu'il s'agit d'une langue complètement personnalisée, vous devrez spécifier :

* Le nom de la langue.
* S'il s'agit d'un dialecte d'une autre langue.
* Le code de cette langue sur Crowdin.
* Son code à trois lettres.
* Son code de paramètres régionaux (locale-code).
* Si le texte sera écrit de gauche à droite ou de droite à gauche.
* La forme plurielle.

3. Après avoir rempli toutes ces informations, vous êtes prêt à créer votre projet. Cliquez simplement sur le bouton \"Create Project\" en bas de la page.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/create-project.png)

💡 **Conseil :** Vous pouvez également cliquer sur \"Cancel\" (Annuler) et revenir à cette page si vous souhaitez recommencer.

Maintenant, vous devriez pouvoir voir votre projet. Bien sûr, il sera vide au début mais ne vous inquiétez pas. Nous nous en occuperons dans un instant. 😉

![Image](https://www.freecodecamp.org/news/content/images/2023/09/project-dashboard.png)
_Nouveau projet._

### Aperçu du projet

Faisons un tour rapide du projet.

Tout d'abord, vous pouvez voir le nom du projet avec ses paramètres de confidentialité actuels. Mon projet de démonstration est privé. Vous pouvez créer un nombre illimité de projets publics ou un projet privé avec votre compte Crowdin gratuit.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/project-dashboard-name.png)

À côté du nom du projet, vous verrez deux boutons : \"Invite People\" (Inviter des gens) et \"Buy Translations\" (Acheter des traductions).

Vous pouvez inviter des membres de l'équipe à rejoindre votre projet (nous verrons comment faire dans ce livre) et vous pouvez également acheter des traductions auprès de Crowdin.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/project-dashboard-buttons.png)

Vous pouvez également trouver tous les onglets dont vous avez besoin pour accéder aux outils disponibles pour votre projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/project-dashboard-tabs.png)

Vous serez par défaut dans l'onglet \"Sources\", où vous pourrez voir les fichiers sources que vous avez téléversés et les chaînes de votre projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/project-dashboard-sources.png)

**💡 Conseil :** Vous pourrez également créer des dossiers et ajouter des fichiers.

Voyons les autres onglets :

#### Onglet Dashboard (Tableau de bord)

C'est ici que vous verrez la liste des langues cibles du projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/dashboard-target-languages.png)
_Onglet Dashboard._

#### Onglet Translations (Traductions)

C'est ici que vous pouvez téléverser des traductions existantes, télécharger vos traductions sous forme de fichier zip, des lots de fichiers cibles, et configurer la livraison de contenu par voie hertzienne (over-the-air).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/translations-tab.png)
_Onglet Translations._

#### Onglet Screenshots (Captures d'écran)

C'est ici que vous pouvez téléverser des captures d'écran de votre projet pour aider vos traducteurs en leur donnant plus de contexte sur les chaînes qu'ils traduisent.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/screenshots-tab.png)
_Onglet Screenshots._

#### Onglet Tasks (Tâches)

C'est ici que vous pouvez créer et assigner des tâches aux membres de votre équipe.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/tasks-tab.png)
_Onglet Tasks._

#### Onglet Members (Membres)

C'est ici que vous pouvez voir tous les membres de votre projet avec leurs rôles respectifs, la date à laquelle ils ont rejoint le projet, et les actions que vous pouvez entreprendre pour chaque membre.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/members-tab.png)
_Onglet Members._

#### Onglet Integrations (Intégrations)

C'est ici que vous pouvez ajouter des intégrations à votre projet et voir toutes les intégrations que votre projet possède actuellement.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/integrations-tab.png)
_Onglet Integrations._

#### Onglet Reports (Rapports)

C'est ici que vous pouvez voir et générer des rapports sur l'activité de votre projet, y compris la traduction et la relecture.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/reports-tab.png)
_Onglet Reports._

#### Onglet Activity (Activité)

C'est ici que vous pouvez voir l'activité du projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/activity-tab.png)
_Onglet Activity._

#### Onglet Discussions

C'est ici que vous pouvez ouvrir des sujets de discussion pour débattre des aspects du projet avec votre équipe.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/discussions-tab.png)
_Onglet Discussions._

#### Onglet Tools (Outils)

C'est ici que vous trouverez plus d'informations sur l'outil de ligne de commande, l'API, les Webhooks et Crowdin In-Context (un outil pour traduire des applications web avec un aperçu en temps réel).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/tools-tab.png)
_Onglet Tools._

#### Onglet Settings (Paramètres)

C'est ici que vous pouvez personnaliser les paramètres du projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/settings-tab.png)
_Onglet Settings._

En parlant de paramètres de projet, plongeons dans les paramètres que vous pouvez personnaliser pour votre projet.

### Comment personnaliser les paramètres de votre projet dans Crowdin

Vous trouverez différentes catégories de paramètres de projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/settings-tab-1.png)
_Onglet Settings._

#### Paramètres généraux

Les paramètres généraux incluent :

* Nom.
* Description publique.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/general-settings-1.png)
_Paramètres généraux._

* Branding, y compris un domaine personnalisé et un logo de projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/branding-1.png)
_Paramètres de Branding._

* Badges pour montrer la progression du processus de localisation.
* Une option pour supprimer le projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-2023-09-18-at-8.25.48-PM.png)
_Badges et suppression d'un projet._

#### Confidentialité et collaboration

Dans cette catégorie, vous trouverez des paramètres pour gérer la confidentialité et les notifications de votre projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/privacy-and-collaboration.png)
_Confidentialité et collaboration._

Vous pouvez gérer la visibilité de votre projet dans les paramètres de visibilité du projet. Vous pouvez définir votre projet comme public ou privé.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/project-visibility.png)

Ensuite, nous avons les paramètres de confidentialité. Vous pouvez lire une courte description de chacun de ces paramètres sous chaque élément correspondant. Pour activer un paramètre, cochez sa case.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/privacy-settings.png)
_Paramètres de confidentialité par défaut. Vous pouvez les personnaliser selon vos besoins._

Enfin, les paramètres de notifications pour les traducteurs, les gestionnaires de projet et les développeurs peuvent également être personnalisés. Cochez simplement les notifications que vous souhaitez activer.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-2023-09-18-at-8.29.36-PM.png)
_Paramètres de notifications._

#### Langues

Dans la catégorie des langues, vous pouvez modifier les langues source et cible de votre projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/languages-settings.png)
_Paramètres de langues._

#### Vérifications d'assurance qualité (QA)

Je vous avais promis que ce serait important, n'est-ce pas ? Nous y voilà. Dans la catégorie assurance qualité (QA), vous pouvez activer les vérifications QA et choisir les vérifications QA spécifiques que vous souhaitez avoir dans votre projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/qa-checks.png)
_Catégorie Vérifications QA._

Crowdin [mentionne](https://support.crowdin.com/qa-checks/) que :

> L'objectif principal des vérifications d'assurance qualité (QA) est de vous aider à gérer efficacement les différents aspects linguistiques des traductions et de vous assurer qu'elles sont formatées de la même manière que les chaînes sources et qu'elles s'intégreront tout aussi bien à l'interface utilisateur. Certains problèmes typiques de vérification QA incluent des virgules oubliées, des espaces en trop ou des fautes de frappe.  
>   
> Il est recommandé de revoir et de résoudre tous les problèmes de vérification QA avant de construire votre projet et de télécharger les traductions.

Ces vérifications d'assurance qualité incluent :

* Traductions vides.
* Problèmes de longueur.
* Incohérence des balises.
* Incohérence des espaces.
* Incohérence des variables.
* Incohérence de la ponctuation.
* Incohérence de la casse des caractères.
* Incohérence des caractères spéciaux.
* Problèmes de \"traduction incorrecte\" signalés par les membres du projet.
* Fautes d'orthographe.
* Erreurs de syntaxe ICU (International Components for Unicode).
* Terminologie cohérente suivant le glossaire du projet.
* Traduction en double.
* Syntaxe FTL.
* Syntaxe Android.

Après avoir sélectionné les vérifications QA que vous souhaitez activer, cliquez simplement sur le bouton \"Save\" et vos modifications seront enregistrées.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/save-qa-checks.png)
_Bouton Save._

#### Mémoires de traduction

Vous trouverez également une catégorie pour les paramètres des mémoires de traduction.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/translation-memories.png)
_Catégorie Mémoires de traduction._

Nous parlerons des mémoires de traduction en détail plus tard, mais sachez que c'est ici que vous pouvez personnaliser tous les paramètres de cette fonctionnalité utile.

#### Glossaires

Vous pouvez également gérer vos glossaires à partir de la catégorie Glossaires.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/glossaries.png)
_Catégorie Glossaires._

Vous pouvez vérifier vos glossaires assignés et cliquer sur les liens pour voir les enregistrements de chaque glossaire. En haut, vous trouverez également un lien vers l'[application Translate Glossary](https://crowdin.com/store/apps/glossary-translate-app).

#### Import

Dans Crowdin, vous pouvez importer des chaînes sources et personnaliser des paramètres tels que la gestion des chaînes en double et le comptage des mots.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/import-category.png)
_Paramètres d'importation._

#### Export

La catégorie d'exportation contient des paramètres utiles pour l'exportation de vos fichiers traduits.

Vous pouvez choisir de :

* Enregistrer les informations de contexte dans les fichiers.
* Ignorer les chaînes non traduites.
* Ignorer les fichiers non traduits.
* Exporter uniquement les traductions approuvées.
* Remplir automatiquement les dialectes régionaux.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/export.png)
_Paramètres d'exportation._

#### Étiquettes (Labels)

Les étiquettes peuvent être utiles pour ajouter du contexte aux chaînes et les organiser par sujets. Elles peuvent être utiles lorsque vous souhaitez rechercher des chaînes spécifiques.

Vous pouvez ajouter des étiquettes à partir de cette catégorie dans les paramètres :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/labels.png)
_Paramètres d'étiquettes._

![Image](https://www.freecodecamp.org/news/content/images/2023/09/creating-a-label.png)
_Création d'une nouvelle étiquette._

#### Configuration de l'analyseur (Parser Configuration)

Avec la configuration de l'analyseur, vous pouvez configurer la manière dont Crowdin importe et exporte les types de fichiers sélectionnés pour répondre à vos besoins.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/parser-configuration.png)
_Catégorie Configuration de l'analyseur._

#### Processeurs de fichiers (File Processors)

Le dernier groupe dans les paramètres est Processeurs de fichiers, qui vous permet de personnaliser la manière de traiter les formats de fichiers pris en charge.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/file-processors.png)
_Catégorie Processeurs de fichiers._

## Comment supprimer un projet dans Crowdin

Si jamais vous avez besoin de supprimer un projet, n'oubliez pas que vous pouvez le faire en allant dans l'onglet \"Settings\" et en cliquant sur l'onglet \"General\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/settings-tab-1.png)
_Settings > General._

En bas, vous trouverez un bouton rouge \"Delete Project\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/delete-a-project-2.png)
_Supprimer le projet._

## Comment téléverser des fichiers vers votre projet Crowdin

Maintenant que vous savez comment personnaliser les paramètres de votre projet, ajoutons réellement un fichier au projet. Vous pouvez soit téléverser vos fichiers de projet manuellement, soit automatiser ce processus via des intégrations.

### Comment téléverser des fichiers manuellement

Téléversons un exemple de fichier PDF avec du texte et des images.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/demo-pdf-document-1.png)
_Notre fichier PDF de démonstration. Nous allons le traduire dans Crowdin._

Pour téléverser des fichiers :

1. Allez dans votre projet.
2. Allez dans l'onglet \"Sources\".
3. Cliquez sur le bouton vert \"Add File\" ou sur le bouton gris \"Upload Files\" (voir la capture d'écran ci-dessous).
4. Choisissez le fichier que vous devez téléverser depuis votre système de fichiers.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/upload-files-sources.png)
_Téléverser des fichiers ou utiliser des fichiers d'exemple._

💡 **Conseil :** Pour explorer le fonctionnement de Crowdin, vous pouvez également ajouter des fichiers d'exemple Crowdin en cliquant sur le bouton \"Use Samples\".

Après avoir téléversé votre fichier, vous le verrez listé :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/upload-files.png)
_Téléversement d'un fichier._

Vous devrez peut-être attendre quelques secondes avant que le fichier ne soit traité. Ensuite, vous verrez le nombre total de chaînes pour votre fichier.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/upload-finished.png)
_Téléversement terminé._

💡 **Conseil :** Vous pouvez également glisser-déposer votre fichier dans la zone des fichiers de l'onglet \"Sources\" et votre fichier sera téléversé automatiquement.

Si vous cliquez sur les trois petits points à droite, vous verrez plus d'options pour ce fichier, notamment :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/uploaded-file-options.png)
_Options supplémentaires._

* Paramètres.
* Progression.
* Voir les chaînes.
* Ouvrir dans l'éditeur.
* Télécharger la source.
* Renommer.
* Supprimer.

### Comment téléverser des fichiers automatiquement

L'un des aspects clés de Crowdin est la facilité avec laquelle il est possible de le connecter à d'autres services via des intégrations, pour téléverser automatiquement vos fichiers et synchroniser vos traductions.

Par exemple, freeCodeCamp a configuré une intégration GitHub, nous pouvons donc synchroniser automatiquement les fichiers de notre projet lorsque nous ajoutons de nouvelles chaînes qui doivent être traduites sur Crowdin.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/github-integration-2.png)
_Intégration GitHub._

Vous pouvez également trouver des centaines d'intégrations sur le [Crowdin store](https://store.crowdin.com/) pour connecter votre projet à des services externes.

Crowdin dispose également d'une interface de programmation d'application (API) pour les développeurs.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/crowdin-api.png)
_La [documentation](https://developer.crowdin.com/api/v2/) de l'API Crowdin._

L'équipe Crowdin la [décrit](https://developer.crowdin.com/api/v2/) comme :

> Une API RESTful complète qui vous aide à intégrer la localisation dans votre processus de développement. Les points de terminaison que nous utilisons vous permettent de passer facilement des appels pour récupérer des informations et exécuter les actions nécessaires.

Avec cette API, vous pouvez :

* Créer des projets pour la traduction.
* Ajouter et mettre à jour des fichiers.
* Télécharger des traductions, et plus encore.

C'est un excellent moyen d'automatiser votre processus de localisation. Vous pouvez en savoir plus sur l'API Crowdin dans la [documentation officielle](https://developer.crowdin.com/api/v2/).

Et la troisième option pour téléverser des fichiers automatiquement est d'utiliser l'interface de ligne de commande (CLI).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/crowdin-cli-1.png)
_L'interface de ligne de commande (CLI) Crowdin._

Avec cette interface, vous pouvez :

* Automatiser le processus de téléversement des fichiers.
* Télécharger les traductions automatiquement et les enregistrer aux bons emplacements.
* Téléverser des traductions existantes.
* Intégrer Crowdin avec d'autres outils comme Git.

Pour en savoir plus sur la CLI Crowdin, consultez [ce tutoriel](https://www.youtube.com/watch?v=0duN4khpWjM) créé par l'équipe Crowdin.

Maintenant que vous savez comment téléverser vos fichiers sur Crowdin manuellement et automatiquement, voyons comment vous et votre équipe pouvez commencer à traduire.

## Comment commencer à traduire

Une fois votre fichier téléversé, il est temps de commencer à traduire. Vous pouvez commencer à le traduire vous-même ou demander à votre équipe de commencer à travailler sur les traductions.

💡 **Conseil :** Vous pouvez assigner des fichiers spécifiques à vos traducteurs et relecteurs grâce à la fonctionnalité des tâches.

Supposons que vous traduisiez les fichiers vous-même.

Pour commencer, vous devez vous rendre dans l'onglet Dashboard du projet et sélectionner la langue dans laquelle vous allez traduire votre fichier dans la liste des langues cibles que vous avez choisies lors de la création du projet.

Je vais choisir l'espagnol pour cette démonstration.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/list-of-target-languages.png)
_Tableau de bord._

Vous verrez tous les fichiers de votre projet pour cette langue cible spécifique.

Sur la page de la langue, vous pouvez vérifier la progression de la traduction et de la relecture de chaque fichier, traduire et relire, et téléverser ou télécharger vos traductions et fichiers sources.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/project-files-in-spanish.png)
_Liste des fichiers à traduire en espagnol._

Vous pouvez cliquer sur le nom du fichier que vous souhaitez traduire. Cela vous mènera à l'éditeur de traduction et vous verrez votre fichier dans l'aperçu.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/translation-editor.png)
_L'éditeur de traduction._

Lorsque vous téléversez un fichier, Crowdin le divise en chaînes. Ce processus peut nécessiter certaines conversions de format en fonction du type de fichier que vous téléversez.

Selon la [documentation de Crowdin](https://support.crowdin.com/supported-formats/#converted-file-formats) :

> Lors de l'importation, certains formats de fichiers sont automatiquement convertis en d'autres formats pour être ensuite analysés et traités.   
>   
> Vous pouvez voir la liste des formats de fichiers initiaux et les formats de fichiers vers lesquels ils sont convertis dans le tableau ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/file-formats-table.png)
_Conversion des formats de fichiers. Image tirée de la [documentation Crowdin](https://support.crowdin.com/supported-formats/#converted-file-formats)._

Nous pouvons voir que les fichiers PDF sont convertis en fichiers DOCX, le type de fichier que nous créons habituellement dans un éditeur de texte.

Ensuite, pour exporter le fichier, [Crowdin mentionne également](https://support.crowdin.com/supported-formats/#converted-file-formats) que :

> Par défaut, nous exportons les traductions dans le même format que les fichiers sources. Par exemple, si vous téléversez un fichier XML sur Crowdin, vous aurez le fichier XML exporté.

## Comment utiliser l'éditeur de traduction

Voici la disposition de l'éditeur de traduction que vous verrez par défaut lorsque vous cliquerez sur un fichier. Elle s'appelle le Mode Confortable (Comfortable Mode).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/translation-editor.png)
_L'éditeur de traduction._

Il comporte quatre sections principales :

* La barre latérale gauche (en violet ci-dessous).
* La zone centrale supérieure (en jaune ci-dessous).
* La zone centrale inférieure (en orange ci-dessous).
* La barre latérale droite (en bleu ci-dessous).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/translation-editor-sections.png)
_L'éditeur de traduction en mode confortable._

Parlons de chaque section.

### Barre latérale gauche

* Encadrée en violet dans le diagramme précédent.
* Vous montre toutes les chaînes de votre document et un aperçu de votre fichier source.
* Vous trouverez des outils utiles en haut tels que (de gauche à droite) : la recherche de chaînes dans le fichier, le changement de vue vers une liste de toutes les chaînes, la mise en évidence des chaînes traduites et non traduites, l'affichage de l'aperçu de la traduction, le basculement de l'échelle et l'ajout d'une chaîne.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/toolbar-options.png)
_Barre latérale gauche - Barre d'outils en haut._

Si vous cliquez sur le premier bouton (de gauche à droite) après le champ de recherche de fichier, vous pouvez changer la vue pour voir une liste de toutes les chaînes au lieu de l'aperçu du fichier.

Maintenant, vous verrez une liste de toutes les chaînes sur la gauche :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/list-of-all-strings.png)
_Vue en liste simple._

Vous pouvez toujours cliquer à nouveau sur ce bouton pour revenir au mode précédent, où vous pouvez voir les chaînes dans le contexte et la mise en page d'origine du fichier source, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/translation-editor.png)
_Mode de traduction WYSIWYG (\"What You See Is What You Get\")._

Ici, vous verrez que les chaînes sont mises en évidence dans différentes couleurs.

* Le rouge signifie que la chaîne n'a pas été traduite.
* Le jaune signifie que la chaîne est partiellement traduite.
* Le bleu signifie que la chaîne a été traduite.
* Le gris signifie que la chaîne est masquée et visible uniquement par les gestionnaires de projet et les relecteurs.

Lorsque vous commencerez à relire les chaînes, vous verrez également :

* Une coche jaune si la chaîne est partiellement approuvée (si certaines formes plurielles ne sont pas approuvées).
* Une coche verte si la chaîne a été approuvée.

You may also see a comment icon if a contributor has left a comment on a string or if it has marked the comment as an issue.

### Zone centrale supérieure

* Encadrée en jaune dans le diagramme ci-dessous.
* C'est ici que vous pouvez traduire une chaîne. Il vous suffit de la sélectionner dans la barre latérale gauche et elle apparaîtra dans cette zone.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/translation-editor-sections.png)
_L'éditeur de traduction en mode confortable._

Cliquons sur une chaîne et voyons ce qui se passe :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/selecting-a-strings.png)
_Sélection d'une chaîne._

Génial ! La chaîne est maintenant sélectionnée comme \"Source String\" (Chaîne source) et nous pouvons commencer à la traduire :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/writing-translations.png)
_Traduire une chaîne._

Les trois outils que vous pouvez voir en bas sont (de gauche à droite) :

* **Copy Source :** pour conserver la structure initiale de la chaîne.
* **Clear :** pour effacer rapidement la traduction.
* **Text Selection Mode :** pour copier une partie de la traduction à partir de la mémoire de traduction (TM) ou des traductions automatiques (MT).

Si vous cliquez sur les trois points en haut, vous verrez des options supplémentaires pour la chaîne, notamment :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/strings-translation-options.png)
_Options de traduction de chaîne._

* Masquer la chaîne.
* Copier l'URL de la chaîne.
* Copier le squelette source.
* Historique des traductions.
* Voir la chaîne en contexte.

Lorsque vous écrivez votre traduction, vous verrez vos traductions dans l'aperçu. La chaîne sera mise en évidence en jaune s'il s'agit de la chaîne sélectionnée.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/preview-with-partially-translated-string.png)
_Traduction dans l'aperçu (barre latérale). La chaîne traduite est en espagnol dans l'aperçu._

Pour enregistrer votre traduction, cliquez sur le bouton vert \"Save\".

Après cela, vous pouvez passer à la chaîne suivante et vous verrez la chaîne précédemment traduite mise en évidence dans une couleur différente (bleu).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/translated-saved-string.png)
_Traduction enregistrée._

Pour revenir à la chaîne précédente, cliquez simplement dessus ou cliquez sur la flèche gauche à côté de \"Source String\".

Si vous revenez à la chaîne, vous verrez quelque chose de nouveau dans la zone centrale inférieure.

Parlons de la zone centrale inférieure.

### Zone centrale inférieure

* Encadrée en orange dans le diagramme ci-dessous.
* Cette section contient les traductions effectuées par d'autres contributeurs (le cas échéant), les suggestions de la mémoire de traduction (TM), les suggestions de traduction automatique (MT) et les traductions dans d'autres langues.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/translation-editor-sections.png)
_L'éditeur de traduction en mode confortable._

**💡 Conseil :** Si vous cliquez sur une suggestion, elle apparaîtra automatiquement dans le champ de saisie de la traduction.

Voici l'état actuel de notre projet. Nous avons cette chaîne traduite et vous pouvez voir la traduction espagnole dans la section centrale inférieure (cadre orange ci-dessous).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/back-to-translated-string.png)
_Section centrale inférieure._

Pour chaque traduction, vous verrez :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/approve-string-translation.png)
_Traduction._

* La traduction dans la langue cible.
* L'utilisateur Crowdin qui a enregistré la traduction.
* Quand elle a été enregistrée.
* Sa note actuelle (les autres membres du projet peuvent voter pour ou contre une traduction).
* Un bouton de coche pour approuver la traduction (comme un relecteur).
* Un bouton de corbeille pour supprimer la traduction.

Si vous êtes le propriétaire du projet ou si vous avez des autorisations de relecture, vous pouvez approuver vous-même la traduction de la chaîne. Cependant, il est toujours recommandé de demander à un autre membre de l'équipe de vérifier votre chaîne pour éviter tout problème courant.

Pour approuver la traduction, cliquez simplement sur le bouton de coche à côté de la traduction.

Maintenant, vous verrez la chaîne approuvée mise en évidence en vert dans l'aperçu :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/approved-string.png)
_Chaîne approuvée mise en évidence en vert._

La chaîne traduite indiquera désormais qui l'a approuvée et quand elle a été approuvée :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/back-to-approved-string-1.png)

### Barre latérale droite

Et enfin (mais non le moindre !), nous avons la barre latérale droite.

* Encadrée en bleu dans le diagramme ci-dessous.
* C'est ici que vous pouvez écrire des commentaires, effectuer des recherches dans la TM, rechercher des termes dans votre glossaire, ajouter de nouvelles applications et trouver les applications que vous avez ajoutées via le [Crowdin Store](https://crowdin.com/store/apps).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/translation-editor-sections.png)
_L'éditeur de traduction en mode confortable._

Pour écrire un commentaire, allez simplement dans les commentaires sur la barre latérale et écrivez votre commentaire dans le champ de saisie de texte en bas. Vous pouvez marquer le commentaire comme un problème si nécessaire.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/writing-a-comment-1.png)
_Écrire un commentaire._

💡 **Conseil :** Vous devez écrire votre commentaire en utilisant la langue source du projet, afin que les autres membres de l'équipe et les gestionnaires de projet puissent le comprendre.

Si vous cliquez sur la deuxième option de cette barre latérale, vous pourrez rechercher dans votre mémoire de traduction les traductions précédentes.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/translation-memory.png)
_Recherche dans la mémoire de traduction (TM)._

Dans la troisième option, vous pouvez rechercher des termes liés à la chaîne actuellement sélectionnée dans votre glossaire.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/glossary.png)
_Recherche de termes._

Ce qui est vraiment génial avec cette fonction de recherche de termes, c'est que, [selon Crowdin](https://support.crowdin.com/online-editor/#section-4) :

> Si le terme spécifique n'est pas disponible dans le glossaire du projet, le système vous montrera les explications de Wikipedia.

Cela peut être très utile pour mieux comprendre le contexte d'un terme lorsque vous traduisez une ressource.

Et la dernière option est une icône plus qui vous mènera au Crowdin Store, où vous trouverez des applications et des intégrations pour votre projet et vous pourrez y accéder sur la barre latérale.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/add-apps.png)
_Aller au Crowdin Store._

## Modes de l'éditeur de traduction

L'éditeur de traduction dispose de trois modes pour personnaliser la mise en page d'une manière qui répond à vos besoins — Mode Confortable, Mode Côte à côte et Mode Multilingue.

### Mode Confortable

* Principalement utilisé pour les traductions.
* Il comporte les quatre sections principales que nous avons vues dans la section précédente.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/comfortable-mode.png)
_Mise en page en mode confortable._

### Comment changer de mode

Pour passer à un autre mode, vous devez cliquer sur l'icône de menu en haut à gauche de l'éditeur de traduction :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/change-mode-1.png)
_Cliquez sur cette icône de menu._

Ensuite, cliquez sur \"View\" et choisissez le mode que vous souhaitez voir :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/view-change-mode.png)
_Changer la vue de l'éditeur._

### Mode Côte à côte (Side-by-Side Mode)

* Principalement utilisé par les gestionnaires et les relecteurs pour approuver les meilleures traductions et par les traducteurs pour voter pour les traductions à la suite.

La première fois que vous passerez à cette vue, vous verrez quelques conseils utiles :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/tip-1.png)
_Réviser ou effectuer des traductions._

![Image](https://www.freecodecamp.org/news/content/images/2023/09/tip-2.png)
_Approuver plusieurs traductions à la fois._

![Image](https://www.freecodecamp.org/news/content/images/2023/09/tip-3.png)
_Passer à la vue confortable pour effectuer de nouvelles traductions._

![Image](https://www.freecodecamp.org/news/content/images/2023/09/tip-4.png)
_C'est tout les amis !_

Voici ce que vous verrez lorsque vous entrerez en mode côte à côte. Prenez un moment pour le voir en détail et explorer les changements :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/side-by-side-mode.png)
_Mode Côte à côte_

Pour voir tous les statuts de chaînes possibles en mode côte à côte, revenons au mode confortable pour traduire et enregistrer une autre chaîne (mais nous n'approuverons pas la chaîne cette fois).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/string-translation-2.png)
_Traduction d'une autre chaîne._

Dans la vue côte à côte, nous avons maintenant une chaîne traduite, une chaîne approuvée et des chaînes que nous devons encore traduire.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/side-by-side-with-multiple-strings.png)
_Mode Côte à côte._

Commençons par un tour rapide. Vous avez quatre zones que vous pouvez redimensionner selon vos besoins :

* En haut à gauche, on trouve la liste des chaînes. Vous pouvez sélectionner plusieurs chaînes pour des opérations groupées telles que l'approbation de plusieurs chaînes en un seul clic.
* En bas à gauche, on trouve l'aperçu du fichier source.
* En haut à droite, on trouve les détails de la chaîne.
* En bas à droite, on trouve les traductions actuelles et les suggestions. C'est très similaire à ce que vous voyez en mode confortable.

#### Barre d'outils

![Image](https://www.freecodecamp.org/news/content/images/2023/09/toolbar.png)
_Barre d'outils._

En haut de la liste des chaînes, vous verrez plusieurs outils, notamment (de gauche à droite) :

* Rechercher une chaîne.
* Changer les critères de tri.
* Longueur de la chaîne dans le fichier source et dans la version traduite.
* Bouton Save.
* Bouton Cancel.
* Copy source.
* Approve string.
* Add string.
* Edit string.
* Plus d'options.

Si vous ouvrez le menu \"More options\" en cliquant sur les trois points, vous verrez plus d'options utiles pour la ou les chaîne(s) sélectionnée(s).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/more-options-2.png)
_Plus d'options._

#### Comment trier les chaînes

Vous remarquerez que, par défaut, les chaînes seront triées par leur statut.

**💡 Conseil :** Les chaînes non traduites seront affichées en premier, vous ne verrez donc pas les chaînes dans l'ordre dans lequel elles apparaissent dans le fichier source.

Vous pouvez modifier les critères de tri en cliquant sur l'icône de filtre à côté du champ de recherche.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/filtering-strings.png)
_Filtrage des chaînes._

Dans ce mode, vous verrez également différentes références visuelles du statut de chaque chaîne.

Ici, nous pouvons voir :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/types-of-strings.png)
_Statut de la chaîne._

* Une chaîne non traduite en rouge.
* Une chaîne traduite en bleu.
* Une chaîne approuvée avec une coche verte.
* Une chaîne masquée en gris.

### Mode Multilingue

Génial. Passons maintenant au mode multilingue. Ce mode est principalement utilisé par les traducteurs et les relecteurs pour travailler avec plusieurs langues en même temps.

💡 **Conseil :** Vous pouvez travailler sur jusqu'à dix langues simultanément.

Pour passer à ce mode, cliquez sur l'icône du menu principal en haut. Sélectionnez ensuite \"View\" et choisissez \"Multilingual\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/multilingual-view.png)
_Passer au mode multilingue._

Lorsque vous choisissez \"Multilingual\", vous devrez choisir les langues avec lesquelles vous prévoyez de travailler.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/languages.png)
_Langues pour le mode multilingue._

Choisissons l'espagnol et le japonais juste pour voir comment fonctionne ce mode. Cliquez dessus puis cliquez sur le bouton \"Apply\".

Vous devriez voir ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/multilingual-mode.png)
_Mode multilingue._

Chaque chaîne aura un champ de texte où vous pourrez écrire la traduction pour chacune des langues cibles sélectionnées.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/string-in-multilingual.png)

Lorsque vous travaillez en mode multilingue, vous pouvez basculer entre deux vues possibles :

* Vue en liste (List View).
* Vue en grille (Grid View).

Voici un exemple de la vue en liste :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/multilingual-mode.png)
_Vue en liste en mode multilingue._

Pour passer à la vue en grille, vous devez cliquer sur le bouton dans la barre d'outils en haut :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/multilingual-mode-copy.png)
_Basculer entre la vue en liste et en grille._

Les autres parties de l'éditeur et les outils de ce mode sont très similaires à la vue côte à côte que vous connaissez déjà.

## Comment passer à un autre fichier

Vous souhaiterez peut-être passer à un autre fichier après avoir traduit toutes les chaînes d'un fichier différent. C'est très facile à faire.

Pour ce faire :

Cliquez sur le menu principal en haut à gauche.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/main-menu-button.png)
_Menu principal._

Allez dans File puis choisissez \"Open...\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/open-another-file-1.png)
_Ouvrir un fichier._

Choisissez le fichier que vous souhaitez ouvrir et cliquez sur \"Open\" (ou double-cliquez sur le nom du fichier).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/open-file-menu.png)
_Liste des fichiers._

💡 **Conseil :** Vous pouvez également accéder à la liste des fichiers beaucoup plus rapidement en cliquant directement sur le nom du fichier.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/file-click-on-file.png)
_Cliquez sur le nom du fichier._

Vous serez dirigé vers le fichier que vous avez choisi.

### Comment voir toutes les chaînes

Si jamais vous avez besoin de voir une liste de toutes les chaînes d'un projet, il vous suffit de :

Aller au menu principal en haut à gauche.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/main-menu-button.png)
_Menu principal._

Aller dans \"File\", puis sélectionner \"All Strings\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/all-strings-1.png)
_Voir toutes les chaînes._

Vous verrez une liste de toutes les chaînes du projet, leur statut et leurs traductions.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/all-strings-list.png)
_Toutes les chaînes._

## Comment traduire les langues RTL

Alors que certaines langues comme l'espagnol et l'italien s'écrivent de gauche à droite (LTR), d'autres langues comme l'arabe et l'ourdou s'écrivent de droite à gauche (RTL).

[Crowdin mentionne](https://support.crowdin.com/online-editor/#translating-rtl-languages) que :

> Lors de la traduction entre des langues LTR et RTL, certains éléments du champ de traduction de l'éditeur peuvent ne pas s'afficher de la même manière qu'ils le seront une fois exportés.

Pour s'assurer que les traductions s'afficheront correctement dans le fichier exporté, Crowdin recommande :

1. De cliquer sur le bouton \"Copy Source\" lors de la rédaction des traductions. C'est le premier bouton de la barre d'outils.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/toolbar-copy-source-1.png)
_Le bouton \"Copy Source\"._

2. De traduire le texte dans votre langue cible.

3. De laisser toutes les variables ou balises exactement telles quelles, même si elles n'ont pas l'air identiques. Elles seront dans la bonne position lorsque vous exporterez un fichier.

💡 **Conseil :** Crowdin [suggère](https://support.crowdin.com/online-editor/#translating-rtl-languages) d'utiliser l'[application Unicode Table](https://store.crowdin.com/unicode) pour copier et coller les marques de droite à gauche et de gauche à droite, en changeant la direction du texte là où c'est nécessaire.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-77.png)
_Exemple de traduction d'une langue RTL tiré de la [documentation Crowdin](https://support.crowdin.com/online-editor/#translating-rtl-languages)._

### Paramètres de l'éditeur de traduction

Vous pouvez également personnaliser les paramètres de l'éditeur de traduction.

Pour accéder à ces paramètres, cliquez sur l'icône d'engrenage en haut à droite de l'éditeur de traduction.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/editor-settings.png)
_Paramètres de l'éditeur de traduction._

Vous verrez une liste des paramètres que vous pouvez personnaliser.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/editor-settings-1.png)
_Paramètres de l'éditeur (Partie 1)_

La première partie de ces paramètres comprend :

* Le pourcentage de correspondance minimum pour afficher les suggestions de la mémoire de traduction.
* Si les traductions doivent être vérifiées pour les problèmes d'assurance qualité (QA).
* Si l'éditeur doit compléter automatiquement ce que vous écrivez et vous montrer une liste de prédictions.
* Si vous souhaitez approuver les traductions automatiquement. Cela peut être utile si vous traduisez et relisez le projet vous-même.
* Si vous souhaitez passer automatiquement à la chaîne suivante.
* Le thème de couleur pour l'éditeur de traduction (clair, sombre ou automatique).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/editor-settings-2-1.png)
_Paramètres de l'éditeur (Partie 2)._

Si vous faites défiler vers le bas, vous trouverez d'autres paramètres, tels que :

* Si l'éditeur ne doit afficher que le début de la chaîne source dans une vue compacte.
* Si vous souhaitez afficher l'aperçu de la traduction pour les chaînes traduites.
* Comment les balises HTML doivent être affichées. Vous pouvez les afficher ou les masquer.
* Si les caractères non imprimables doivent être affichés ou non.
* Si le champ de traduction doit être mis en évidence.
* Si vous souhaitez activer la vérification orthographique en temps réel.
* La langue de l'interface utilisateur de votre éditeur de traduction.

Vous pouvez personnaliser ces paramètres selon vos besoins.

### Raccourcis clavier

Une autre fonctionnalité de productivité clé pour les traducteurs et les relecteurs sur Crowdin est l'utilisation de raccourcis clavier.

Pour voir tous les raccourcis clavier disponibles pour votre système d'exploitation, cliquez simplement sur l'icône du clavier en haut à droite.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/keyboard-shortcuts-button-1.png)
_Ouvrir les raccourcis clavier._

Voici les raccourcis clavier pour Windows :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-78.png)
_Raccourcis clavier (Windows). Capture d'écran de la [documentation Crowdin](https://support.crowdin.com/online-editor/#helpful-tips)._

Et voici les raccourcis clavier pour macOS :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/keyboard-shortcuts-macos-1.png)
_Raccourcis clavier (macOS)._

Si vous faites défiler vers le bas, vous trouverez d'autres raccourcis clavier pour macOS.

## Comment télécharger le(s) fichier(s) traduit(s)

Une fois votre projet traduit et approuvé, vous devrez le télécharger.

Dans Crowdin, vous avez trois options différentes pour télécharger des fichiers. Vous pouvez télécharger l'intégralité du projet, télécharger tous les fichiers du projet dans une langue spécifique, ou télécharger un fichier spécifique dans une langue spécifique.

Voyons ces options plus en détail.

### Comment télécharger l'intégralité du projet

Si vous avez besoin de télécharger l'intégralité du projet :

1. Allez dans votre projet.
2. Allez dans l'onglet \"Translations\".
3. Dans la section \"Download as ZIP\", cliquez sur le bouton \"Build & Download\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/download-project-1.png)
_Télécharger en tant que ZIP._

Vous verrez une barre de progression pendant que Crowdin construit le projet, puis votre téléchargement commencera.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/progress-bar.png)
_Build & Download._

Le fichier ZIP contiendra des dossiers pour chaque langue. Les noms des dossiers seront leurs codes de langue correspondants.

### Comment télécharger tous les fichiers dans une langue cible

Cette option est utile si vous devez télécharger tous les fichiers traduits dans une langue cible spécifique.

1. Allez dans votre projet.
2. Allez dans l'onglet \"Translations\".
3. Dans la section \"Download as ZIP\", sélectionnez la langue.
4. Cliquez sur le bouton \"Build & Download\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/download-language-1.png)
_Télécharger en tant que ZIP._

### Comment télécharger un fichier dans une langue cible

La troisième option consiste à télécharger un seul fichier dans une langue cible spécifique.

Pour ce faire :

1. Allez dans votre projet.
2. Allez dans l'onglet Dashboard.
3. Choisissez la langue cible.
4. Cliquez sur le fichier.
5. Cliquez sur les trois points à droite pour voir les options supplémentaires (voir la capture d'écran ci-dessous).
6. Cliquez sur \"Download\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/download-one-file.png)
_Télécharger un fichier dans une langue cible._

Le téléchargement devrait commencer et vous devriez avoir votre fichier traduit prêt en quelques secondes ou minutes.

Vous pouvez également automatiser le processus d'exportation ou de téléchargement de vos fichiers traduits avec les intégrations Crowdin.

## **Comment utiliser la mémoire de traduction (TM)**

Beau travail jusqu'ici. Maintenant que vous connaissez les fonctionnalités de base de l'éditeur de traduction, parlons de fonctionnalités plus avancées telles que la mémoire de traduction.

Nous verrons comment vous pouvez :

* Créer une mémoire de traduction.
* Gérer la mémoire de traduction.
* Télécharger et téléverser une mémoire de traduction.
* Assigner une mémoire de traduction à un projet.

💡 **Conseil :** N'oubliez pas que la TM est comme une base de données de chaînes que nous avons traduites précédemment dans notre projet et leurs traductions correspondantes. La réutilisation des traductions précédentes peut nous faire gagner beaucoup de temps.

Êtes-vous prêt ? Commençons.

### Comment créer une mémoire de traduction (TM)

Pour créer une TM pour votre projet, vous devez :

1. Aller sur votre profil. Vous pouvez le faire en cliquant sur \"Profile\" dans le menu déroulant qui s'affiche lorsque vous cliquez sur votre image de profil en haut à droite.
2. Aller dans l'onglet \"Resources\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/resources-1.png)
_Onglet Resource dans le profil._

3. Si vous avez déjà un projet créé, vous verrez une TM pour ce projet. Vous pouvez également créer une nouvelle TM, indépendamment d'un projet (vous pourrez l'assigner à un projet plus tard).

[Crowdin mentionne](https://support.crowdin.com/translation-memory/#creating-tm) que :

> Outre les TM de projet qui sont automatiquement créées avec les projets respectifs, vous pouvez également créer des TM séparées, les remplir avec le contenu approprié en téléversant vos TM existantes au format TMX, XLSX ou CSV, puis assigner ces TM aux projets nécessaires.

4. Pour créer une nouvelle TM, cliquez sur le bouton vert \"Create TM\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/create-TM-1.png)
_Créer une TM._

5. Complétez les informations pour votre nouvelle TM, telles que son nom, sa langue, et si vous souhaitez l'assigner à un projet existant.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/create-translation-memory.png)
_Créer une mémoire de traduction._

Je vais créer une nouvelle TM appelée \"Demo TM\" en anglais. Pour l'instant, je ne l'assignerai à aucun projet.

Voyons ce qui se passe :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/demo-translation-memory.png)
_Nouvelle TM._

🎉 Génial. Nous voyons maintenant la nouvelle TM dans la liste.

### Comment gérer la mémoire de traduction (TM)

Si vous cliquez sur les trois points à droite de la TM pour afficher les options supplémentaires, vous verrez les options suivantes :

* Upload (Téléverser).
* Download (Télécharger).
* Edit (Modifier).
* View Records (Voir les enregistrements).
* Delete (Supprimer).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/additional-options-1.png)
_Options supplémentaires pour une mémoire de traduction._

Si vous sélectionnez une TM en cochant sa case, vous pouvez la supprimer, la modifier ou voir ses enregistrements.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/manage-tm-2.png)

Puisque notre nouvelle TM est récente (et donc vide), voyons les enregistrements de la TM pour notre projet de cours freeCodeCamp.

Si vous cliquez dessus, vous verrez une liste de tous les enregistrements stockés dans la TM :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/translation-memory-strings-1.png)
_Mémoire de traduction (TM)._

À partir d'ici, vous pouvez :

* Modifier les enregistrements.
* Supprimer les enregistrements.
* Rechercher des enregistrements spécifiques correspondant à la casse, à la phrase entière et trouver une correspondance exacte.
* Masquer ou afficher des colonnes spécifiques.

### Comment téléverser et télécharger une mémoire de traduction (TM)

Dans l'onglet \"Resources\" de votre projet, vous pouvez également téléverser et télécharger une TM.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/tm-records-download-upload.png)
_Barre d'outils des ressources._

Le fichier doit être dans l'un des formats suivants :

* TMX
* XLSX
* CSV

Pour téléverser une TM :

* Cliquez sur le bouton \"Upload\".
* Choisissez votre fichier dans votre système de fichiers.
* Faites correspondre chaque colonne à la langue correspondante.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/tm-records-download-upload.png)
_Le bouton \"Upload\"._

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-79.png)
_Correspondance des colonnes avec leurs langues respectives. Image tirée de la [documentation Crowdin](https://support.crowdin.com/translation-memory/#downloading-and-uploading-tm)._

Pour télécharger une mémoire de traduction :

* Cliquez sur le bouton \"Download\".
* Sélectionnez le format de fichier (soit TMX, XLSX ou CSV).
* Choisissez si vous souhaitez télécharger toutes les langues ou seulement une paire de langues spécifique.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/tm-records-download-upload.png)
_Le bouton \"Download\"._

![Image](https://www.freecodecamp.org/news/content/images/2023/09/download-tm.png)
_Télécharger la TM._

Le téléchargement devrait commencer après avoir cliqué sur le bouton vert \"Download\".

Voici le fichier CSV que nous obtenons lorsque nous exportons la mémoire de traduction de notre projet de cours freeCodeCamp :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-2023-09-19-at-5.19.49-PM.png)
_Fichier CSV exporté._

### Comment assigner une mémoire de traduction à un projet

Pour assigner une TM existante à un projet :

1. Allez dans votre projet.
2. Allez dans l'onglet \"Settings\".
3. Allez dans \"Translation Memories\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/assign-tm.png)
_Onglet Settings._

4. Faites défiler vers le bas pour trouver \"Assigned Translation Memories\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/assigned-tm.png)

5. Sélectionnez les mémoires de traduction que vous souhaitez assigner à votre projet.

[Crowdin mentionne](https://support.crowdin.com/translation-memory/#prioritizing-tm) que :

> Lorsque vous assignez quelques TM au projet, vous pouvez définir la priorité nécessaire pour chacune d'elles. Par conséquent, les suggestions de TM provenant de la TM ayant la priorité la plus élevée seront affichées en premier lieu.

💡 **Conseil :** Un nombre plus élevé représente une priorité plus élevée. Si une TM a une priorité de 5, elle sera supérieure à une priorité de 1.

Vous pouvez également modifier la TM par défaut en cliquant sur l'icône d'étoile correspondante.

**Important :** Veuillez noter que Crowdin a récemment éliminé le besoin d'utiliser des flux de travail personnalisés pour appliquer automatiquement les correspondances de mémoire de traduction. Vous pouvez désormais activer la mémoire de traduction dans les paramètres du projet, comme vous pouvez le voir ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-13.png)
_Comment activer la pré-traduction par mémoire de traduction pour le nouveau contenu dans les paramètres du projet. Capture d'écran fournie par l'équipe Crowdin._

## Glossaire

Génial ! Maintenant que vous connaissez les aspects les plus importants de la TM sur Crowdin, jetons un coup d'œil aux glossaires.

💡 **Conseil :** Rappelez-vous qu'un glossaire vous permet de stocker et de gérer la terminologie de votre projet pour aider vos traducteurs avec plus de contexte et de définitions.

### Comment créer un glossaire

Lorsque vous créez un projet, un glossaire est automatiquement créé, mais vous pouvez également en créer de nouveaux qui sont indépendants de tout projet.

Pour créer un glossaire :

* Allez sur votre profil.
* Allez dans \"Resources\".
* Cliquez sur \"Glossaries\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/glossaries-tab.png)
_Glossaires_

Vous verrez un glossaire pour chaque projet que vous avez créé sur Crowdin.

* Cliquez sur le bouton vert \"Create Glossary\".
* Choisissez un nom et une langue pour votre glossaire.
* Si nécessaire, assignez-le à un projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/create-a-glossary.png)
_Assigner à un glossaire._

Après cela, vous verrez votre nouveau glossaire dans la liste des glossaires. J'ai créé un nouveau glossaire appelé \"Demo Glossary\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/demo-glossary.png)
_Liste des glossaires._

### Comment gérer les termes du glossaire

Vous pouvez ajouter, modifier et supprimer des concepts et des termes de vos glossaires. Voyons comment vous pouvez le faire étape par étape.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/empty-glossary.png)
_Nouveau glossaire vide._

**💡 Conseil :** Sur Crowdin, un concept n'est pas la même chose qu'un terme. Un concept est plus large qu'un terme. Voici ce que dit la [documentation](https://support.crowdin.com/glossary/#managing-glossary-concepts-and-terms) à propos de leur différence :

> Un concept intègre des termes de glossaire et leurs variations avec de multiples traductions et d'autres informations pertinentes.

Pour ajouter un concept, cliquez sur le bouton vert \"Add concept\" :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/add-concept-2.png)
_Ajouter un concept._

Vous devrez écrire des informations sur le nouveau concept :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-2023-09-19-at-6.08.32-PM.png)
_Dialogue d'ajout de concept._

La [documentation Crowdin](https://support.crowdin.com/glossary/#managing-glossary-concepts-and-terms) décrit les détails de concept suivants :

> **Définition :** définition du concept.  
> **Sujet :** une branche de connaissance à laquelle le concept est lié.  
> **Note :** de courtes notes sur un concept qui pourraient être utiles aux traducteurs.  
> **URL :** URL de la page web contenant des informations pertinentes sur un concept.  
> **Figure :** URL de l'image correspondante.

Elle mentionne également les détails de **terme** suivants :

> **Partie du discours :** par exemple, nom, verbe, adjectif, etc.  
> **Type :** par exemple, forme complète, acronyme, abréviation, etc.  
> **Statut :** préféré, admis, non recommandé, obsolète.  
> **Genre :** genre du terme.  
> **Description :** description du terme.  
> **Note :** de courtes notes sur un terme qui pourraient être utiles aux traducteurs.  
> **URL :** URL de la page web contenant des informations pertinentes sur un terme.

Après avoir créé le terme, vous le verrez dans la liste des termes du glossaire :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/glossary-term-demo.png)

Pour modifier ou supprimer un terme de glossaire, cliquez sur les trois points à droite pour voir les options supplémentaires et choisissez une option.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/glosssary-term-1.png)
_Terme de glossaire._

Vous pouvez télécharger ou téléverser un glossaire dans les formats suivants :

* TBX (v2)
* TBX (v3)
* CSV
* XLSX

Cliquez simplement sur le bouton correspondant et vous pourrez choisir un fichier à téléverser ou le format du fichier à télécharger.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/download-upload.png)
_Téléverser et télécharger un glossaire._

[Crowdin suggère](https://support.crowdin.com/glossary/#downloading-and-uploading-glossary) que :

> Si vous téléversez un glossaire aux formats de fichiers CSV ou XLS/XLSX, sélectionnez la langue pour chaque colonne et la valeur de la colonne (terme, description ou partie du discours) dans la boîte de dialogue de configuration.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-80.png)
_Sélection des colonnes. Image tirée de la [documentation Crowdin](https://support.crowdin.com/glossary/#downloading-and-uploading-glossary)._

### Comment assigner un glossaire à un projet

Il est très facile d'assigner un glossaire à un projet sur Crowdin.

Il vous suffit de :

* Aller dans votre projet.
* Aller dans l'onglet \"Settings\".
* Aller dans \"Glossaries\".
* Sélectionner le glossaire (ou les glossaires) que vous souhaitez assigner à votre projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/glossaries-demo.png)
_Glossaires du projet._

**💡 Conseil :** Pour modifier le glossaire par défaut d'un projet, cliquez simplement sur l'icône d'étoile du glossaire correspondant. L'étoile gris foncé marque le glossaire par défaut actuel.

Vous pouvez également partager des glossaires sur tous vos projets en cochant l'option \"Share Glossaries\" dans votre profil :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/share-glossaries.png)
_Partager les glossaires._

### Comment traduire le glossaire

Traduire votre glossaire peut être très utile pour utiliser les termes de manière cohérente dans vos langues cibles.

Pour traduire votre glossaire, Crowdin recommande d'utiliser l'application gratuite [Translate Glossary](https://crowdin.com/store/apps/glossary-translate-app).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/translate-glossary.png)
_Application Translate Glossary._

Si vous installez l'application, vous pourrez traduire votre glossaire directement sur Crowdin et choisir quels projets doivent avoir accès à cette application.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/install-translate-glossary.png)
_Installer l'application._

## Vérifications d'assurance qualité (QA) dans Crowdin

L'assurance qualité est essentielle pour tout type de projet et c'est particulièrement vrai pour les projets de localisation. Une petite faute de frappe ou d'orthographe peut faire toute la différence pour vos utilisateurs.

C'est pourquoi Crowdin a mis en œuvre des fonctionnalités d'assurance qualité efficaces pour vous aider à fournir les traductions de haute qualité que vos utilisateurs méritent.

Selon [Crowdin](https://support.crowdin.com/qa-checks/) :

> Les vérifications QA aident à détecter certaines erreurs courantes facilement et rapidement. Il est recommandé de revoir et de résoudre tous les problèmes de vérification QA avant de construire votre projet et de télécharger les traductions.

Les problèmes détectés par les vérifications QA incluent :

* Fautes de frappe.
* Virgules manquantes.
* Espaces en trop.
* Autres erreurs courantes.

### Comment configurer les vérifications d'assurance qualité (QA)

Pour configurer les vérifications QA et choisir ce que vous souhaitez vérifier dans les chaînes traduites, il vous suffit de :

* Aller dans votre projet.
* Aller dans l'onglet \"Settings\".
* S'assurer que \"Enable QA Checks\" est sélectionné.
* Sélectionner ce que vous souhaitez vérifier.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/qa-checks-settings.png)
_La catégorie Vérifications QA._

Vous pouvez vérifier :

* Si une traduction est vide.
* Si la traduction est plus longue que la limite de longueur prédéfinie (si elle existe).
* Incohérence des balises.
* Incohérence des espaces.
* Incohérence des variables.
* Incohérence de la ponctuation.
* Incohérence de la casse des caractères.
* Incohérence des caractères spéciaux.
* Problèmes de \"traduction incorrecte\".
* Problèmes d'orthographe.
* Erreurs de syntaxe ICU.
* Cohérence avec les termes du glossaire.
* Traduction en double.
* Erreurs de syntaxe FTL.
* Erreurs de syntaxe Android.

**💡 Conseil :** Pour chacune de ces vérifications QA, vous pouvez choisir si vous souhaitez afficher un avertissement à l'utilisateur lors de l'enregistrement de la chaîne ou si vous souhaitez aller plus loin et afficher une erreur.

Pour enregistrer vos modifications, cliquez sur le bouton vert \"Save\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/qa-save-button.png)
_Enregistrer les vérifications QA._

### Comment vérifier le statut de l'assurance qualité

Les relecteurs et les gestionnaires de projet peuvent voir les problèmes trouvés par les vérifications d'assurance qualité.

Pour voir le statut actuel, il vous suffit de :

* Aller dans votre projet.
* Aller dans l'onglet \"Dashboard\".
* Trouver le statut \"QA Checks\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/qa-checks-status-1.png)
_Vérifications QA sans aucun problème._

Vous verrez l'un des statuts suivants :

* **Off** : Lorsque les vérifications QA ne sont pas activées.
* **In Progress** : Lorsque les vérifications QA sont en cours.
* **No Issues** : Lorsque les vérifications QA n'ont trouvé aucun problème.
* **Issues Found** : Lorsque les vérifications QA ont trouvé des problèmes.

Si vous essayez d'enregistrer une chaîne présentant un problème de vérification QA, vous verrez un avertissement ou une erreur. Vous pouvez l'enregistrer quand même, mais vous devriez toujours essayer de corriger ces problèmes en premier.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/qa-warning.png)
_Un avertissement suite à l'ajout d'espaces supplémentaires._

💡 **Conseil :** Cliquer sur le bouton \"Autofix\" sur l'avertissement tentera de corriger le problème automatiquement. Vous pouvez également l'enregistrer quand même ou annuler.

Ceci est une image d'exemple de la documentation Crowdin montrant ce que vous devriez voir si des problèmes d'assurance qualité sont trouvés dans votre projet :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-81.png)
_Problèmes de vérifications QA trouvés. Image tirée de la [documentation Crowdin](https://support.crowdin.com/qa-checks/)._

L'assurance qualité est une étape très importante que vous devez absolument prendre très au sérieux lors de votre processus de localisation.

## Comment téléverser des traductions existantes

Génial. Si vous avez des traductions existantes, vous pouvez également les téléverser dans votre projet.

Vous avez trois options :

* Les téléverser via l'onglet Translations.
* Les téléverser via la page de la langue.
* Les téléverser via l'éditeur de traduction.

### Comment téléverser via l'onglet Translations

Pour les téléverser via l'onglet Translations :

* Allez dans votre projet.
* Allez dans \"Upload existing translations\".
* Glissez-déposez vos traductions existantes ou sélectionnez les fichiers dans votre système de fichiers.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/translations-tab-upload.png)
_Téléverser des traductions via l'onglet Translations._

Selon Crowdin, les [formats pris en charge](https://support.crowdin.com/uploading-translations/#key-value-formats) pour le téléversement des traductions incluent ceux qui ont une structure clé-valeur, tels que :

> Android XML, macOS/iOS Strings, Stringsdict, JSON, Chrome JSON, GO JSON, i18next JSON, FBT JSON, XLIFF, XLIFF 2.0, Java Properties, Play Properties, Java Properties XML, RESX, RESW, RES JSON, YAML, INI, Joomla INI, JS, FJS, PO, TS, QT TS, Blackberry, Symbian, Flex, BADA, TOML, Coffee, DKLANG, XAML, SRT, VTT, VTT2, SBV, SVG, DTD, CSV, RC, WXL, Maxthon, Haml, XLSX, PLIST, PHP, ARB, VDF.

Crowdin [mentionne également](https://support.crowdin.com/uploading-translations/#text-and-html-based-formats) que :

> Pour les fichiers qui n'ont pas de structure définie, le téléversement de la traduction est géré par une technologie expérimentale d'apprentissage automatique.  
>   
> Cela inclut les formats de fichiers suivants : HTML, Front Matter HTML, Markdown, Front Matter Markdown, TXT, Generic XML, Web XML, DOCX, HAML, IDML, DITA, Wiki, FLSNP, MIF et ADOC.

### Comment téléverser via la page de la langue

Pour les téléverser via la page de la langue :

* Allez dans votre projet.
* Allez dans \"Dashboard\".
* Choisissez une langue cible.
* Choisissez un fichier mais au lieu de cliquer dessus, cliquez sur les trois points à sa droite pour afficher plus d'options.
* Cliquez sur \"Upload Translations\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/upload-translations-language-page-2-1.png)
_Téléverser des traductions depuis la page de la langue._

Lorsque vous cliquez sur cette option, vous verrez certains paramètres pour le téléversement et pour l'attribution des traductions. Cochez les options dont vous avez besoin pour votre projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/upload-options.png)

### Comment téléverser via l'éditeur de traduction

Enfin, vous pouvez également téléverser des traductions directement depuis l'éditeur de traduction.

Pour ce faire :

* Cliquez sur le menu principal.
* Dans File, sélectionnez \"Upload Translations...\"

![Image](https://www.freecodecamp.org/news/content/images/2023/09/upload-from-editor.png)
_Téléverser des traductions depuis l'éditeur de traduction._

### Formats de fichiers pris en charge sur Crowdin

Jusqu'à présent, nous avons mentionné différents formats de fichiers avec lesquels vous pouvez travailler sur Crowdin. Mais Crowdin prend en charge plus de 100 formats de fichiers.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/100-file-formats.png)
_Prend en charge plus de 100 formats de fichiers._

![Image](https://www.freecodecamp.org/news/content/images/2023/09/supported-file-formats.png)
_Formats de fichiers pris en charge dans le Crowdin Store._

Vous pouvez vérifier les formats de fichiers pris en charge dans les ressources suivantes :

* [Formats pris en charge](https://support.crowdin.com/supported-formats/).
* [Formats de fichiers dans le Crowdin Store](https://store.crowdin.com/categories/file-formats).

## Comment pré-traduire votre projet

Si votre objectif est de gagner du temps et d'améliorer votre productivité, la pré-traduction via la traduction automatique (MT) peut être exactement ce dont vous avez besoin.

Il s'agit d'un processus automatisé qui applique des traductions générées par ordinateur à votre projet lorsque vous téléversez un fichier. Sur Crowdin, vous pouvez configurer des moteurs de traduction automatique pour utiliser cette fonctionnalité.

Vous avez deux alternatives pour mettre en œuvre ce processus :

* Manuel.
* Automatisé.

### Pré-traduction manuelle

Pour pré-traduire votre contenu manuellement via la traduction automatique (MT) :

* Allez dans votre projet.
* Allez dans l'onglet \"Dashboard\".
* Cliquez sur \"Pre-translation\".
* Sélectionnez via TM (mémoire de traduction) ou via MT (traduction automatique).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/pretranslation-1.png)
_Pré-traduction._

Si vous choisissez \"via MT\" (traduction automatique), vous devrez choisir votre moteur de traduction, les langues cibles et les fichiers que vous souhaitez pré-traduire. Vous pouvez également ajouter des étiquettes.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/translation-engine.png)
_Pré-traduire votre projet via MT._

### Pré-traduction automatisée

Si vous choisissez d'automatiser le processus, le système pré-traduira automatiquement votre nouveau contenu.

Récemment, Crowdin a ajouté la possibilité d'activer la pré-traduction par traduction automatique pour le nouveau contenu dans les paramètres du projet. Si vous activez cette option et que vous téléversez du nouveau contenu dans votre projet, le système le traduira automatiquement.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image--1-.png)
_Activer la pré-traduction par traduction automatique pour le nouveau contenu. Capture d'écran fournie par l'équipe Crowdin._

## Traduction hors ligne

Parfois, vous pouvez avoir besoin de travailler hors ligne. Crowdin dispose également d'une excellente fonctionnalité pour cela, dans les situations où vous ou les membres de votre équipe souhaiteriez travailler sur les traductions hors ligne.

Pour activer ou désactiver cette fonctionnalité :

* Allez dans votre projet.
* Allez dans l'onglet \"Settings\".
* Allez dans \"Privacy and Collaboration\".
* Cochez (ou décochez) l'option \"Allow offline translation\".

**💡 Conseil :** Cette fonctionnalité peut être activée ou désactivée par les gestionnaires de projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/settings-tab-offline-1.png)
_Autoriser la traduction hors ligne._

Chaque fichier peut être téléchargé via l'éditeur ou via la page de la langue.

### Comment télécharger un fichier via l'éditeur

Pour télécharger un fichier via l'éditeur de traduction :

* Cliquez sur le menu principal en haut à gauche.
* Allez dans File
* Cliquez sur \"Download\" ou \"Export in XLIFF\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/download-files.png)
_Télécharger le fichier via l'éditeur._

### Comment télécharger un fichier via la page de la langue

Pour télécharger un fichier via la page de la langue :

* Allez dans votre projet.
* Allez dans \"Dashboard\".
* Sélectionnez une langue.
* Dans la liste des fichiers, cliquez sur les trois points à côté du fichier que vous souhaitez télécharger pour afficher plus d'options.
* Sélectionnez \"Download\" ou \"Export in XLIFF\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/language-download-1.png)
_Télécharger le fichier via la page de la langue._

### Comment télécharger tous les fichiers pour une langue cible

Si vous devez télécharger tous les fichiers pour une langue cible :

* Allez dans votre projet.
* Allez dans \"Dashboard\".
* Sélectionnez une langue.
* Cliquez sur l'icône de flèche vers le haut et vers le bas (voir la capture d'écran ci-dessous).
* Sélectionnez \"Download translations\" ou \"Export in XLIFF\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/download-files-from-language-1.png)
_Télécharger toutes les traductions._

## Explorer les projets publics

Maintenant que vous connaissez certaines des fonctionnalités les plus importantes de Crowdin, vous vous demandez peut-être aussi comment explorer d'autres projets en cours de traduction sur Crowdin.

Si vous cliquez sur \"Projects\" en haut puis que vous sélectionnez \"Explore Public Projects\", vous verrez une page où vous pourrez explorer les projets publics par sujet et trouver les projets populaires sur Crowdin.

Vous pouvez également filtrer les projets en effectuant une recherche dans la barre de recherche.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/explore-crowdin.png)
_Explorer Crowdin._

🎉 Félicitations. Nous venons d'atteindre la fin de la deuxième partie du livre, qui était axée sur les fondamentaux de Crowdin.

Nous allons maintenant voir comment les équipes et les organisations peuvent utiliser Crowdin pour gérer efficacement leurs projets.

## 🔹 **Crowdin pour les équipes et les organisations**

Génial ! Voyons maintenant comment Crowdin peut vous aider si vous travaillez en équipe sur un projet de localisation ou si vous êtes le fondateur ou le gestionnaire d'une organisation intéressée par la localisation d'un produit ou d'une plateforme.

Nous verrons comment vous pouvez inviter des membres, attribuer des rôles et des tâches, et générer des rapports.

### Comment inviter des membres et des contributeurs au projet

Pour inviter des membres à votre projet :

* Allez dans votre projet.
* Allez dans l'onglet \"Members\".
* Cliquez sur le bouton vert \"Invite\".

💡 **Conseil :** Vous pouvez également cliquer sur le bouton gris \"Invite People\" en haut à gauche pour accéder aux mêmes options.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/members-tab-2-2.png)
_L'onglet Members._

Vous devrez saisir des informations pour ces options avant d'envoyer la ou les invitation(s) :

* Rôle.
* E-mail ou nom d'utilisateur Crowdin.
* Message.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/invite-members.png)
_Envoi d'une invitation._

Si vous cliquez sur \"Select role\", vous devriez voir ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/select-role.png)
_Sélection d'un rôle._

Par défaut, le rôle \"Translator\" sera sélectionné.

Vous verrez également trois champs où vous pourrez choisir les langues auxquelles vous souhaitez attribuer ce rôle. Par exemple, un contributeur pourrait être traducteur pour le japonais et traducteur et relecteur pour l'espagnol.

**💡 Conseil :** Si vous laissez ce champ vide, le rôle s'appliquera à toutes les langues, mais vous pouvez également choisir des langues spécifiques.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/select-role-copy.png)
_Choix de langues spécifiques._

Nous parlerons plus en détail des rôles des membres dans un instant.

💡 **Conseil :** Vous pouvez également modifier le(s) rôle(s) d'un membre dans la section Profil.

Une fois que vous êtes prêt, cliquez sur \"Save\" et vous reviendrez aux options principales. Cliquez sur \"Done\" lorsque vous êtes prêt à envoyer les invitations.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/invite-members.png)
_Envoi d'une invitation._

### Comment envoyer des liens d'invitation

Si vous souhaitez inviter les membres de votre équipe via un lien au lieu de leur envoyer une invitation directe, vous pouvez également le faire.

Cliquez simplement sur le bouton \"Get Link\" en bas pour copier le lien et l'envoyer à la personne que vous souhaitez inviter à votre projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/invite-members-link.png)
_Obtenir un lien d'invitation._

Vous verrez un message de confirmation en haut.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/link-copied-to-clipboard.png)
_Message de confirmation._

Ensuite, vous pouvez coller le lien partout où vous en avez besoin, comme dans un e-mail.

### Comment gérer les liens d'invitation

Pour gérer vos liens d'invitation, cliquez sur l'option \"Manage Links\" :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/manage-links.png)
_Gérer les liens._

Vous verrez une liste de tous les liens d'invitation que vous avez générés, la date à laquelle vous les avez générés et le(s) rôle(s) que vous avez accordé(s) à l'invité.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/invitation-links.png)
_Liens d'invitation qui ont été générés._

**💡 Conseil :** Vous pouvez les copier à nouveau en cliquant sur l'icône de lien à leur droite ou les révoquer en cliquant sur \"Revoke link\".

Si vous cliquez sur \"Done\", vous reviendrez à l'écran précédent et vous pourrez cliquer sur le bouton \"X\" en haut pour le fermer.

## Rôles du projet

Parlons maintenant des différents rôles que vous pouvez attribuer aux membres de votre équipe. Lisons les descriptions des rôles fournies par Crowdin dans la [documentation](https://support.crowdin.com/modifying-project-participants-roles/) :

### Propriétaire (Owner)

> Une personne qui a créé un projet et en a le contrôle total. Le propriétaire peut inviter et gérer les membres du projet, créer des projets, téléverser des fichiers sources et de traduction vers le projet, configurer des intégrations, etc.

### Gestionnaire (Manager)

> Possède des droits similaires à ceux d'un propriétaire de projet, à l'exception de la possibilité de gérer certaines ressources du propriétaire (par exemple, la configuration des moteurs de traduction automatique, les flux de travail personnalisés, etc.) et de supprimer des projets.

### Coordinateur de langue (Language Coordinator)

> Peut gérer certaines fonctionnalités d'un projet uniquement dans les langues auxquelles il a accès.   
>   
> Les coordinateurs de langue peuvent traduire et approuver des chaînes, gérer les membres du projet et les demandes d'adhésion, générer des rapports de projet, créer des tâches et pré-traduire le contenu du projet.   
>   
> Contrairement aux gestionnaires, ils n'ont pas accès aux autres paramètres du projet (par exemple, les fichiers du projet, les intégrations, etc.).

### Développeur

> Peut téléverser des fichiers, modifier le texte traduisible, connecter des intégrations et utiliser l'API. Ne peut pas gérer les tâches, les membres et les rapports du projet.

### Relecteur (Proofreader)

> Peut traduire et approuver des chaînes. N'a pas accès aux paramètres du projet.

### Traducteur

> Peut traduire des chaînes et voter pour les traductions ajoutées par d'autres membres.

### Bloqué (Blocked)

> N'a pas accès au projet.

### Comment assigner ou modifier les rôles

Vous avez deux options pour assigner ou modifier le rôle d'un membre du projet.

Vous pouvez soit :

* Définir le rôle dans l'invitation.
* Définir le rôle sur la page de profil du membre.

#### Comment définir le rôle dans l'invitation

Vous pouvez choisir le rôle lorsque vous envoyez une invitation à un nouveau membre.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/select-role.png)
_Définition du rôle dans l'invitation._

#### Comment définir le rôle dans la page de profil

Vous pouvez également vous rendre dans l'onglet \"Permissions\" de la page de profil du membre pour choisir les rôles que vous souhaitez lui attribuer et pour choisir les langues que vous souhaitez lui affecter.

Ceci est un exemple tiré de la [documentation](https://support.crowdin.com/modifying-project-participants-roles/#languages-permissions) de Crowdin :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-82.png)
_Définition des rôles dans l'onglet \"Permissions\". Image tirée de la [documentation](https://support.crowdin.com/modifying-project-participants-roles/#languages-permissions) de Crowdin._

Cliquez sur le bouton \"Save\" pour enregistrer vos modifications.

## Gestionnaires de projet

Les gestionnaires de projet jouent un rôle clé pour votre équipe et pour votre projet. Ils peuvent avoir un contrôle illimité sur l'ensemble du projet et ils peuvent vous aider à coordonner et à assigner des tâches aux membres de l'équipe.

### Comment ajouter un gestionnaire de projet

Voyons comment vous pouvez ajouter un gestionnaire de projet à votre projet. Vous pouvez attribuer le rôle de Manager à un membre lorsque vous lui envoyez une invitation :

* Allez dans votre projet.
* Allez dans l'onglet \"Members\".
* Cliquez sur \"Invite\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/invite-button-4.png)
_Onglet Members._

Cliquez sur \"Translator\". Vous verrez tous les rôles possibles.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/select-role-manager-1.png)
_Sélectionner un rôle._

Choisissez \"Manager\". Cela accordera au membre un contrôle illimité sur l'ensemble du projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/manager-1.png)
_Rôle de Manager._

Alternativement, vous pouvez inviter un Manager depuis votre page de profil :

* Allez sur votre profil.
* Allez dans l'onglet \"Managers\".
* Cliquez sur \"Add Manager\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/managers-tab-profile-2.png)
_Ajouter un Manager._

Vous devrez maintenant saisir le nom ou le nom d'utilisateur du gestionnaire, le message, les autorisations que vous souhaitez accorder et les projets qui seront gérés par ce gestionnaire.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/invite-manager-from-profile.png)
_Inviter un Manager._

### Modification des autorisations du gestionnaire

Vous pouvez également modifier les autorisations du gestionnaire sur Crowdin.

Pour ce faire :

1. Allez sur votre profil.
2. Allez dans l'onglet \"Managers\". Vous verrez une liste des gestionnaires que vous avez ajoutés à vos projets.
3. Double-cliquez sur le gestionnaire que vous souhaitez modifier.

Ceci est un exemple tiré de la [documentation Crowdin](https://support.crowdin.com/manager-permissions/#editing-manager-permissions) :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-83.png)
_Exemple d'onglet Managers. Image tirée de la [documentation Crowdin](https://support.crowdin.com/manager-permissions/#editing-manager-permissions)._

4. Mettez à jour les autorisations pour ce gestionnaire.

5. Cliquez sur le bouton \"Save\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/edit-permissions.png)
_Image tirée de la [documentation Crowdin](https://support.crowdin.com/manager-permissions/#editing-manager-permissions)._

### Comment supprimer un gestionnaire

Pour supprimer un gestionnaire :

* Allez sur votre profil.
* Allez dans l'onglet \"Managers\".
* Sélectionnez le gestionnaire que vous souhaitez supprimer.
* Cliquez sur \"Remove\".

### Gestionnaire vs Relecteur

Sur Crowdin, les gestionnaires et les relecteurs présentent certaines différences dans leurs rôles et autorisations.

Pour expliquer cela plus en détail, l'équipe Crowdin souligne cette question importante dans la [documentation](https://support.crowdin.com/modifying-project-participants-roles/#qa) :

> Q : _Je suis propriétaire d'un projet. Dois-je inviter un gestionnaire ou un relecteur ?_  
>   
> R : La principale différence entre un gestionnaire et un relecteur est la suivante : en plus d'approuver les traductions ajoutées par les traducteurs, les gestionnaires peuvent également inviter et supprimer des membres du projet, téléverser des fichiers sources et de traduction vers le projet, configurer des intégrations, etc.  
>   
> Si vous souhaitez avoir un membre du projet qui doit avoir accès aux fonctionnalités mentionnées ci-dessus, vous devez inviter un gestionnaire de projet. Alternativement, si vous prévoyez de gérer le projet vous-même, il suffira d'inviter un relecteur.

## Tâches

L'organisation est la clé du succès de tout projet et Crowdin le sait pertinemment. C'est pourquoi ils ont intégré des outils très utiles appelés tâches sur leur plateforme pour vous aider à organiser votre projet et à coordonner les tâches entre les membres de votre équipe.

Avec les tâches, vous pouvez assigner des fichiers spécifiques à vos traducteurs et relecteurs, définir des dates d'échéance, recevoir des notifications, discuter des tâches avec d'autres membres de l'équipe, et même diviser les mots d'un même fichier entre différents membres de l'équipe.

Vous pouvez également suivre le statut de chaque tâche dans un tableau visuel où vous pouvez glisser-déposer vos tâches d'un statut à l'autre.

Cela semble génial, n'est-ce pas ? Voyons les tâches plus en détail.

### Comment créer une nouvelle tâche

Pour créer une nouvelle tâche :

* Allez dans votre projet.
* Cliquez sur le bouton \"Create Task\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/tasks-tab-section-1.png)
_Tâches sur Crowdin._

💡 **Conseil :** Une tâche ne peut être assignée qu'à un seul projet.

Après avoir cliqué sur le bouton, vous verrez un formulaire où vous pourrez saisir tous les détails de votre nouvelle tâche.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/new-task-1.png)
_Création d'une nouvelle tâche._

Les détails que vous pouvez saisir pour une tâche incluent :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/task-2.png)
_Informations sur la tâche (Partie 1)._

* Nom.
* Description.
* Type (traduire ou relire par ses propres traducteurs ou par des fournisseurs).
* Date d'échéance (facultatif).
* Chaînes assignées à la tâche (toutes les chaînes du ou des fichier(s) sélectionné(s) ou seulement les chaînes modifiées pendant une période spécifique).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/task-3.png)
_Informations sur la tâche (Partie 2)_

* Filtrer par étiquettes (les étiquettes que les chaînes de la tâche doivent avoir).
* Exclure des étiquettes (les étiquettes que les chaînes de la tâche ne doivent pas avoir).
* Vous pouvez choisir si vous souhaitez ignorer les chaînes qui sont déjà incluses dans d'autres tâches pour éviter le travail en double par les membres de votre équipe.
* Fichiers qui doivent être traduits ou relus.
* La ou les langue(s) cible(s). Si la tâche comporte plus d'une langue cible, le système créera une tâche pour chaque langue cible.
* Pour assigner des membres de l'équipe à la tâche pour chaque langue cible, cliquez sur l'option \"Assign\" à côté de chaque langue.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/assign-task-1.png)
_Bouton Assign._

Lorsque vous cliquez sur \"Assign\", vous verrez les options suivantes :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/assign-members-1.png)
_Assigner des membres de l'équipe._

* Sélectionnez l'utilisateur ou les utilisateurs que vous souhaitez assigner à la tâche. Vous pouvez rechercher des utilisateurs à l'aide de l'outil de filtrage.
* Si vous devez supprimer un utilisateur, cliquez simplement dessus dans la liste de droite. Vous pouvez vider la liste en cliquant sur l'icône de la corbeille.

💡 **Conseil :** Vous pouvez également choisir si vous souhaitez diviser les fichiers pour assigner plusieurs utilisateurs au même fichier.

* Une fois que vous avez sélectionné tous les utilisateurs, cliquez sur le bouton \"Apply\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/select-all-users.png)
_Utilisateurs sélectionnés pour la tâche._

Vous verrez l'image de profil des membres de l'équipe assignés dans leur(s) langue(s) correspondante(s).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/assigned-members-list-1.png)
_Membre de l'équipe assigné._

Cliquez sur \"Create Task\" pour ajouter la nouvelle tâche. Vous verrez maintenant le tableau de bord des tâches avec une nouvelle tâche dans chaque langue cible que vous avez sélectionnée.

Dans ce cas, j'ai sélectionné l'espagnol et je me suis assigné à la tâche :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/task-board-1.png)
_Tableau de bord des tâches._

### Le tableau des tâches

Il est maintenant temps d'utiliser le tableau des tâches. Ce tableau est très utile pour voir toutes les tâches de votre projet et suivre leur statut.

Vous remarquerez immédiatement qu'il existe trois statuts possibles pour une tâche :

* To Do (À faire)
* In Progress (En cours)
* Done (Terminé)

**💡 Conseil :** Les gestionnaires de projet peuvent déplacer une tâche d'un statut à un autre en la faisant glisser et en la déposant.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/task-board-1.png)
_Tableau de bord des tâches._

Pour voir toutes les tâches dans une langue cible spécifique, cliquez simplement sur cette langue et vous les verrez sous forme de \"cartes\" avec leurs informations correspondantes.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/task-board-2-1.png)
_Tableau des tâches._

**💡 Conseil :** Si une tâche vous est assignée, vous verrez une étoile grise à côté du nom de la tâche. Vous pouvez également rechercher des tâches et les filtrer.

### Comment filtrer les tâches par membres

Vous pouvez voir toutes les tâches assignées à un membre spécifique de l'équipe en utilisant des filtres.

* Cliquez sur \"Filters\".
* Cliquez sur \"All users\" (à côté de \"Filter by\").
* Recherchez le nom d'utilisateur du membre de l'équipe.
* Cliquez sur le nom d'utilisateur.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/filter-by-members-1.png)
_Filtrer les tâches par membres._

💡 **Conseil :** Pour effacer le filtre, cliquez sur l'option \"Clear filter\" à droite.

### Détails de la tâche

Les détails de la tâche correspondent aux informations de base et à la structure d'une tâche. Avec les détails, vous pouvez voir :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-2023-09-20-at-10.17.37-AM.png)
_Une tâche._

* Si la tâche vous est assignée (une étoile grise).
* Numéro de la tâche.
* Nom de la tâche.
* Date de création de la tâche.
* S'il sera traduit et relu par votre propre équipe ou par des fournisseurs.
* Les photos de profil des membres de l'équipe assignés à la tâche.
* Nombre de mots.
* Nombre de commentaires sur la tâche.

Si vous cliquez sur la tâche, vous verrez un aperçu plus détaillé :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/detailed-task-view.png)
_Détails de la tâche._

### Comment ajouter des commentaires à une tâche

Si vous faites défiler vers le bas, vous aurez également la possibilité d'ajouter des commentaires à la tâche.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/detailed-task-view-2-copy-1.png)
_Ajouter des commentaires à une tâche._

### Comment changer le statut d'une tâche

À partir de cette vue détaillée, vous pourrez également modifier le statut de la tâche en cliquant simplement sur un bouton :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/change-status-1.png)
_Options de tâche._

Si vous modifiez le statut d'une tâche à l'aide de ces boutons, vous verrez également le changement reflété sur le tableau des tâches principal, ce qui équivaudrait à la faire glisser et à la déposer dans un nouveau statut.

### Comment gérer les tâches

Si vous cliquez sur une tâche pour vérifier ses détails, puis que vous cliquez sur les trois points en haut à droite pour afficher plus d'options, vous pourrez modifier, fermer et supprimer la tâche.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/edit-a-task-2.png)
_Plus d'options pour gérer les tâches._

### Comment modifier une tâche

Voici ce que vous verrez si vous essayez de modifier une tâche :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/editing-a-task.png)
_Vue de modification de tâche._

C'est très similaire à ce que nous avons vu lors de la création de la tâche. Vous pouvez modifier les chaînes assignées, les fichiers, les dates, et vous pouvez même réinitialiser la portée de la tâche et la progression pour les fichiers assignés.

### Comment fermer une tâche

Pour fermer une tâche, vous pouvez cliquer sur \"Close\" :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/edit-a-task-2.png)
_Plus d'options pour gérer les tâches._

### Comment voir toutes les tâches fermées

Pour voir toutes vos tâches fermées, vous devrez :

* Aller dans votre projet.
* Aller dans l'onglet \"Tasks\".
* Sélectionner \"Closed\" (à côté de \"All\").

![Image](https://www.freecodecamp.org/news/content/images/2023/09/closed-tasks.png)

💡 **Conseil :** \"Done\" (Terminé) et \"Closed\" (Fermé) sont un peu différents. Une tâche peut avoir le statut \"Done\" mais ne pas être fermée. Lorsqu'une tâche a le statut \"Done\", vous verrez un bouton sur la carte pour la fermer, comme dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/close-task-when-done-1.png)
_Bouton de fermeture sur une tâche marquée comme \"Done\"._

### Comment rouvrir une tâche

Si vous fermez une tâche et réalisez ensuite que vous devez la rouvrir, il vous suffit de :

* Ouvrir les détails de la tâche fermée.
* Cliquer sur les trois points à droite pour voir les options supplémentaires.
* Choisir \"Reopen\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/reopen-task.png)
_Rouvrir une tâche._

Vous verrez maintenant la tâche rouverte dans la colonne \"To do\" du tableau des tâches.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/todo-task-1.png)
_Tâche rouverte._

### Comment supprimer une tâche

Pour supprimer une tâche :

* Ouvrez les détails de la tâche.
* Cliquez sur les trois points.
* Sélectionnez \"Delete\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/delete-a-task.png)
_Supprimer une tâche._

### Comment voir toutes les tâches qui vous sont assignées

Si vous contribuez à un projet, vous pouvez voir toutes les tâches qui vous sont assignées en suivant ces étapes :

* Allez sur votre profil.
* Allez dans l'onglet \"To do\".
* Vous verrez toutes les tâches qui vous sont assignées et vos tâches archivées.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/see-all-my-tasks-1.png)
_L'onglet \"To Do\" sur le profil._

💡 **Conseil :** En haut, vous trouverez également un champ de recherche pour filtrer vos tâches et une option pour filtrer les tâches par projet.

Voici les informations de base que vous verrez pour chaque tâche dans cette vue :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/todo-tasks-profile.png)
_Tâche dans l'onglet \"To Do\" sur le profil._

* Numéro de la tâche.
* Statut de la tâche.
* Projet.
* Langue cible.
* Nombre de mots.

Vous verrez également ces deux options pour :

* Ouvrir l'éditeur de traduction et commencer à travailler sur la tâche.
* Archiver la tâche.

### Question importante sur les tâches

Crowdin mentionne cette [question importante dans la documentation](https://support.crowdin.com/enterprise/tasks/#qa) :

> **Q : _Comment les mises à jour du fichier source affectent-elles les tâches de traduction et de relecture existantes ?_**  
>   
> R : Après la mise à jour du fichier source, la liste des chaînes sources incluses dans la tâche sera mise à jour de la manière suivante :  
>   
> - Les chaînes supprimées du fichier source lors de la mise à jour seront supprimées de la tâche.  
> - Les chaînes modifiées marquées avec l'option _Keep Translations_ apparaîtront dans la tâche avec le nouveau texte modifié.  
> - Les chaînes nouvellement ajoutées n'affecteront en rien la tâche existante.  
>   
> Si le fichier source est restauré à la révision contenant les chaînes supprimées, elles réapparaîtront dans la tâche.

## Rapports de projet

En tant que propriétaire ou gestionnaire de projet, les rapports peuvent être très utiles pour comprendre les progrès et l'activité actuels de votre équipe.

Crowdin dispose d'une fonctionnalité de rapports où vous pouvez vérifier le statut de votre projet. Voici un rapport du projet de démonstration avec lequel nous avons travaillé jusqu'à présent :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/project-reports.png)
_Onglet Reports._

Pour accéder au rapport de votre projet :

* Allez dans votre projet.
* Allez dans l'onglet \"Reports\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-2023-09-20-at-11.31.20-AM.png)
_Rapport Partie 1._

Vous verrez le statut du projet par défaut et vous pourrez passer aux rapports de coûts si nécessaire.

Ici, vous pouvez voir quelques captures d'écran avec le type de données que vous pouvez analyser et visualiser avec ces rapports :

* Taille totale du projet et nombre de chaînes traduisibles.
* Langue source et langue cible.
* Nombre de membres.
* Nombre de gestionnaires.
* Nombre de mots traduisibles.
* Nombre de mots masqués.
* Nombre de mots en double.
* Nombre de mots traduits.
* Nombre de mots approuvés.
* Nombre de nouveaux membres.
* Nombre de membres actifs.

Vous pouvez voir ces rapports avec leur pourcentage d'augmentation ou de diminution correspondant par rapport à la période que vous avez sélectionnée.

Vous trouverez également des graphiques de l'activité de traduction avec leurs légendes correspondantes.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-2023-09-20-at-11.34.02-AM.png)
_Rapport (Partie 2)._

Vous trouverez des graphiques de l'\"Activité de relecture\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-2023-09-20-at-11.34.11-AM.png)

Et des graphiques de l'\"Activité des chaînes sources\", et ainsi de suite.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-2023-09-20-at-11.34.13-AM.png)

Vous pouvez également modifier l'unité du rapport en cliquant sur cette option :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/report-unit.png)

Vous pouvez choisir :

* Chaînes.
* Mots.
* Caractères sans espaces.
* Caractères avec espaces.

Dans la [documentation Crowdin](https://support.crowdin.com/project-reports/?q=reports), vous trouverez des exemples du graphique de l'activité de traduction, du graphique de l'activité de relecture et du graphique de l'activité des chaînes sources :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/translation-activity-chart-1.png)
_Activité de traduction. Image tirée de la [documentation Crowdin](https://support.crowdin.com/project-reports/?q=reports)._

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-2023-09-20-at-11.41.30-AM.png)
_Activité de relecture. Image tirée de la [documentation Crowdin](https://support.crowdin.com/project-reports/?q=reports)._

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-2023-09-20-at-11.41.46-AM.png)
_Activité des chaînes sources. Image tirée de la [documentation Crowdin](https://support.crowdin.com/project-reports/?q=reports)._

### Rapport sur les membres les plus actifs

Les membres de votre équipe sont fondamentaux pour votre processus de localisation. Avoir un rapport détaillé de vos membres les plus dévoués et productifs est toujours utile.

Pour générer un rapport sur vos membres les plus actifs :

* Allez dans votre projet.
* Allez dans l'onglet \"Reports\".
* Cliquez sur \"Top Members\".
* Sélectionnez une plage de dates dans le calendrier.
* Cliquez sur \"Generate\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/top-members-report.png)

Vous verrez une liste de vos membres les plus actifs avec :

* Leurs langues cibles
* Combien de chaînes ils ont traduites
* Mots cibles
* Combien de chaînes ils ont approuvées
* Combien de votes ils ont soumis.

Vous pouvez également exporter votre rapport au format XLSX, CSV ou JSON et afficher ou masquer des colonnes spécifiques.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/export-report-1.png)
_Options d'exportation._

![Image](https://www.freecodecamp.org/news/content/images/2023/09/show-or-hide-columns.png)
_Afficher ou masquer des colonnes._

## Conversations sur Crowdin

La communication est essentielle pour tout projet réussi. Vous et les membres de votre équipe pouvez communiquer directement sur Crowdin grâce à la fonctionnalité des conversations.

Avec cette fonctionnalité, vous pouvez communiquer avec un ou plusieurs membres de l'équipe dans un chat privé. Chaque conversation a un sujet, vous pouvez donc les retrouver facilement.

### Comment accéder aux conversations

Pour accéder à vos conversations :

Cliquez sur l'icône des conversations en haut à droite, à côté de votre photo de profil.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/conversation-button-1.png)
_Bouton de conversation._

Allez dans \"Create Conversation\".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/create-conversations-1.png)
_Créer une conversation._

Vous pouvez rechercher des utilisateurs par leur nom ou leur nom d'utilisateur et vous pouvez également filtrer les utilisateurs par projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/filter-users.png)
_Filtrer les utilisateurs._

Ceci est un exemple tiré de la [documentation Crowdin](https://support.crowdin.com/conversations/) :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-86.png)
_Conversation. Image tirée de la [documentation Crowdin](https://support.crowdin.com/conversations/)._

### Comment gérer les conversations et les messages

Pour les conversations, vous pouvez :

* Changer le sujet pour tous les utilisateurs de la conversation.
* Mettre la conversation en sourdine pour ne plus recevoir de notifications.
* Ajouter des utilisateurs.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-87.png)
_Exemple de conversation. Image tirée de la [documentation Crowdin](https://support.crowdin.com/conversations/)._

Pour les messages individuels au sein d'une conversation, vous pouvez :

* Partager le message dans la même conversation ou dans une autre conversation.
* Marquer le message comme non lu.
* Modifier vos messages.
* Supprimer vos messages.
* Signaler comme spam.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-88.png)
_Exemple de gestion des messages. Image tirée de la [documentation Crowdin](https://support.crowdin.com/conversations/#messages)._

🎉 Génial. Vous connaissez maintenant les fonctionnalités les plus importantes de Crowdin pour les équipes et les organisations.

Voyons maintenant comment vous pouvez intégrer Crowdin à d'autres services et comment vous pouvez installer des applications pour améliorer votre productivité.

## 🔹 Intégrations Crowdin et outils de productivité

L'une des caractéristiques clés de Crowdin est sa connectivité. Vous pouvez connecter votre projet à différents services externes pour importer et exporter vos fichiers et traductions selon vos besoins.

## Qu'est-ce qu'une intégration ?

Sur Crowdin, une intégration est une \"connexion\" que vous pouvez établir entre votre projet et un service externe pour synchroniser automatiquement vos fichiers entre ces plateformes.

Sur le [Crowdin store](https://store.crowdin.com/), vous trouverez plus de 600 applications et intégrations que vous pouvez ajouter à votre projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Crowdin-store.png)
_Le Crowdin Store._

Vous pouvez les filtrer par :

* Collections.
* Catégories.
* Partenaires.
* Vérifications QA.

Pour vous donner une idée des types d'applications et d'intégrations que vous pouvez trouver, voici quelques-unes des applications et intégrations phares :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/featured-integrations.png)
_Applications et intégrations phares._

Parlons de quelques-unes d'entre elles plus en détail.

### Intégration GitHub

Si votre projet est hébergé sur un dépôt GitHub, l'[intégration GitHub](https://store.crowdin.com/github) pourrait être exactement ce dont vous avez besoin.

> L'intégration de Crowdin avec GitHub synchronise les fichiers sources et de traduction entre votre dépôt GitHub et votre projet de traduction dans Crowdin. Tous les fichiers traduits et approuvés seront automatiquement poussés sous forme de pull request vers la branche l10n du dépôt GitHub.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/GitHub-integration.png)
_Intégration GitHub._

Pour en savoir plus sur cette intégration, vous pouvez consulter [ce tutoriel](https://www.youtube.com/watch?v=8baL6VWnnZg) créé par Crowdin.

### GitHub Crowdin Action

Si vous avez besoin de téléverser et de télécharger des fichiers de votre dépôt GitHub vers votre projet Crowdin automatiquement, cette action peut vous être très utile.

La [GitHub Crowdin Action](https://store.crowdin.com/github-action) peut :

* Téléverser des fichiers sources vers Crowdin.
* Téléverser des traductions vers Crowdin.
* Télécharger des traductions depuis Crowdin.
* Créer une PR avec les traductions.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/github-crowdin-action.png)
_GitHub Crowdin Action._

Pour en savoir plus sur la GitHub Crowdin Action, consultez [ce tutoriel](https://www.youtube.com/watch?v=5b7BMuCoKGg) créé par l'équipe Crowdin.

### Intégration Google Drive

Google Drive est très utile pour créer, héberger et partager des documents. Avec l'intégration Google Drive, vous pouvez traduire vos fichiers très facilement sur Crowdin.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/google-drive-integration.png)
_Intégration Google Drive._

Pour en savoir plus sur cette intégration, vous pouvez consulter [ce tutoriel](https://www.youtube.com/watch?v=M_WbdDQmEP8) créé par l'équipe Crowdin.

### AI Assistant

Avec la montée en popularité des grands modèles de langage (LLM), l'intelligence artificielle est devenue un outil très important pour la traduction et la localisation.

Crowdin dispose d'un [AI Assistant](https://store.crowdin.com/localization-ai) très utile que vous pouvez installer pour vous aider, vous et votre équipe. Il est décrit comme :

> Un chatbot IA pour traducteurs construit sur l'API ChatGPT d'OpenAI. La première version de cette application fonctionne comme un copilote pour les traducteurs. ([Source : Crowdin](https://store.crowdin.com/localization-ai))

![Image](https://www.freecodecamp.org/news/content/images/2023/09/ai-assistant.png)
_AI Assistant._

Crowdin mentionne que l'AI Assistant possède ces fonctionnalités intéressantes :

> Notre AI Assistant dispose d'une fonction d'ingénierie de prompt, permettant aux traducteurs de personnaliser les prompts avant de commencer un projet de traduction. En conséquence, ils peuvent facilement modifier le contexte, améliorant la précision et la pertinence des traductions.

Pour en savoir plus sur cette intégration, consultez [ce tutoriel](https://www.youtube.com/watch?v=DSEu0iQanc4) créé par l'équipe Crowdin.

### Intégration Visual Studio Code

Si vous êtes un développeur qui travaille avec [Visual Studio Code](https://store.crowdin.com/visual-studio-code), Crowdin a également pensé à vous car l'équipe a développé une extension pour vous aider à traduire votre projet.

> Intégrez vos projets Visual Studio Code avec Crowdin pour optimiser le processus de localisation. Le [Plugin IDE](https://marketplace.visualstudio.com/items?itemName=Crowdin.vscode-crowdin) permet de téléverser instantanément de nouvelles chaînes sources vers votre projet Crowdin et de télécharger les traductions. ([Source : Crowdin](https://store.crowdin.com/visual-studio-code))

![Image](https://www.freecodecamp.org/news/content/images/2023/09/visual-studio-code.png)
_Intégration Visual Studio Code._

![Image](https://www.freecodecamp.org/news/content/images/2023/09/vs-code-extension.png)
_Le Marketplace des extensions._

Vous pouvez en savoir plus sur cette extension dans sa [documentation officielle](https://marketplace.visualstudio.com/items?itemName=Crowdin.vscode-crowdin) sur le Marketplace des extensions Visual Studio Code.

### Video Captions Translator

Si vous ou votre organisation avez besoin de traduire des sous-titres vidéo, Crowdin propose également une intégration pour cela. Elle s'appelle [Video Captions Translator](https://store.crowdin.com/video-captions-translator).

> Des traductions professionnelles pour les sous-titres vidéo. Configurez l'intégration une fois, définissez votre flux de travail de localisation et passez moins de temps à gérer les traductions.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/video-captions-translator.png)
_Video Captions Translator._

Pour en savoir plus sur la traduction des sous-titres YouTube avec Crowdin, vous pouvez consulter [ce tutoriel](https://store.crowdin.com/video-captions-translator) créé par l'équipe Crowdin.

### Intégration Google Sheets

Si vous utilisez [Google Sheets](https://store.crowdin.com/spreadsheet-crowdin) pour gérer vos clés de localisation, vous pouvez ajouter cette intégration à votre projet pour mapper vos colonnes à leurs champs correspondants sur Crowdin, notamment :

* Clé (Key).
* Texte source.
* Langues cibles (toutes les langues du projet).
* Étiquettes (Labels).
* Contexte.
* Longueur maximale de la traduction.

Veuillez noter que l'équipe Crowdin mentionne que :

> Il est à noter que cette intégration ne synchronisera que la première feuille de votre document Google Sheets.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/google-sheets.png)
_Intégration Google Sheets._

Pour en savoir plus sur l'intégration Google Sheets, consultez [ce tutoriel](https://www.youtube.com/watch?v=7tOanqDiIJ8) créé par l'équipe Crowdin.

### Suggestions Diff Checker

Si vous avez déjà demandé un outil qui pourrait aider vos traducteurs et relecteurs à comparer très facilement les traductions avec des repères visuels, cette application est faite pour vous.

Crowdin décrit [Suggestions Diff Checker](https://store.crowdin.com/diff-checker) comme :

> Une aide précieuse pour les relecteurs et les traducteurs qui compare deux traductions et montre la différence entre elles.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/suggestions-diff-checker.png)
_Suggestions Diff Checker._

### Proofreading Diff

La relecture est une tâche très importante pour le processus de localisation. Les relecteurs peuvent éditer les traductions et s'assurer qu'elles sont aussi précises que possible.

Avec l'application de rapport [Proofreading Diff](https://store.crowdin.com/proofreading-diff), vous pouvez :

> Suivre et analyser les changements effectués pendant le processus de relecture. Cet outil peut vous aider à fournir un retour d'information complet aux traducteurs sur leur travail.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/proofreading-diff.png)
_Proofreading Diff._

### Video Preview

Traduire les sous-titres d'une vidéo sans regarder la vidéo simultanément peut être assez difficile car avoir le contexte complet d'une chaîne est très utile pour la traduire avec précision.

C'est pourquoi Crowdin a créé une application de productivité pour traducteurs appelée [Video Preview](https://store.crowdin.com/preview-video). Ils la décrivent comme :

> Un outil pratique qui peut être utile lorsque vous avez des sous-titres vidéo à traduire. Il vous permet de spécifier l'URL de la vidéo pour chaque fichier de sous-titres, et permet aux traducteurs de prévisualiser la vidéo tout en travaillant sur la traduction.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/video-preview.png)
_Video Preview._

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-96.png)
_Video Preview en action. Image tirée de la [documentation Crowdin](https://store.crowdin.com/preview-video)._

### Glossary Editor

C'est une autre application Crowdin utile pour gérer les glossaires de votre projet.

Crowdin mentionne que le [Glossary Editor](https://store.crowdin.com/glossary-edit-app) :

> Vous permet d'ajouter et de modifier les termes de vos glossaires directement dans l'éditeur Crowdin.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/glossary-editor.png)
_Glossary Editor._

### Project Duplicator

Avez-vous déjà souhaité pouvoir utiliser un projet comme modèle pour un autre projet et vous épargner tout le temps de configuration initiale ?

Si c'est le cas, alors [Project Duplicator](https://store.crowdin.com/create-project-app) est exactement ce qu'il vous faut :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/project-duplicator.png)
_Project Duplicator._

Avec Project Duplicator, vous pouvez copier les paramètres suivants d'un projet :

* Langue source.
* Vérifications d'assurance qualité.
* Chaînes sources.
* Traductions.
* Mémoire de traduction.
* Notifications.
* Mappage de langue (Language Mapping).

### Intégration Unity

Si vous êtes un développeur de jeux et que vous travaillez avec Unity, cette intégration est exactement ce dont vous avez besoin.

Avec l'[intégration Unity](https://store.crowdin.com/unity), vous pouvez :

> Traduire le contenu de vos tableaux (chaînes et actifs) et télécharger les traductions dans Unity.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/unity.png)
_Intégration Unity._

Ceci est une capture d'écran officielle du plugin Crowdin pour Unity :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-101.png)
_Image tirée de la [documentation Crowdin](https://store.crowdin.com/unity)._

### Is Crowdin slow for everyone or just me?

Oui, c'est le nom officiel d'un outil de productivité pour traducteurs dans Crowdin ! 🙂 C'est un widget de performance pour mesurer votre connexion Internet.

Crowdin [mentionne](https://store.crowdin.com/internet-speed) qu'il peut être utile pour :

> Savoir immédiatement si la lenteur que vous ressentez est causée par votre connexion Internet ou s'il s'agit d'un problème de performance de Crowdin.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/is-crowdin-slow.png)
_Est-ce que Crowdin est lent pour tout le monde ou juste pour moi ?_

Ceci est une capture d'écran officielle du widget :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-97.png)
_Image tirée de la [documentation Crowdin](https://store.crowdin.com/internet-speed)._

### Convertisseur d'unités (Units Converter)

Vous avez appris que la localisation est plus large que la traduction. Les unités en sont un excellent exemple.

Lorsque vous localisez un produit qui inclut des unités de longueur, de surface, de masse, de volume, de température, de vitesse, etc., vous devez avoir un outil à portée de main pour les convertir rapidement pendant que vous localisez votre contenu.

Crowdin mentionne que :

> L'application est particulièrement pratique lors de la localisation pour des cultures qui utilisent des systèmes de mesure différents.

C'est là que l'[application Units Converter](https://store.crowdin.com/units_converter) peut vous faire gagner beaucoup de temps car vous pouvez l'avoir sur votre éditeur de traduction et convertir rapidement des unités sans interrompre votre processus de localisation pour aller vers un autre outil.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/units-converter.png)
_Convertisseur d'unités._

Ceci est une capture d'écran officielle de l'application :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-98.png)
_Application Units Converter. Image tirée de la [documentation Crowdin](https://store.crowdin.com/units_converter)._

### Screenshots Uploader

Le contexte visuel est essentiel pour rédiger des traductions de haute qualité.

L'application [Screenshots Uploader](https://store.crowdin.com/screenshots-uploader) :

> Facilite la réception d'un contexte visuel pour votre équipe.

Vous pouvez :

* Autoriser les traducteurs à téléverser des captures d'écran.
* Coller des captures d'écran à partir de l'historique de votre presse-papiers sans les enregistrer sur votre appareil.
* Modifier les captures d'écran avant de les téléverser avec des outils utiles comme le recadrage, le zoom, etc.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/screenshots-uploader.png)
_Screenshots Uploader._

### Directory Notifications

L'application [Directory Notifications](https://store.crowdin.com/directory-notification) est utile pour les propriétaires et les gestionnaires de projet car Crowdin va :

> Envoyer une notification par e-mail chaque fois qu'un répertoire de fichiers de votre projet Crowdin est traduit ou relu.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/directory-notifications.png)
_Directory Notifications._

Ceci est une capture d'écran officielle de l'application :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-100.png)
_Image tirée de la [documentation Crowdin](https://store.crowdin.com/directory-notification)._

### Emoji Input for Editor

Les emojis sont géniaux, n'est-ce pas ? Je pense que nous sommes tous d'accord là-dessus. 😁

Heureusement pour nous, Crowdin propose un [Emoji Input pour l'éditeur de traduction](https://store.crowdin.com/emoji). Ils le décrivent comme :

> Une application de liste d'emojis pour l'éditeur Crowdin pour un accès facile avec une fonctionnalité de recherche étendue.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/emoji-input.png)
_Saisie d'emojis pour l'éditeur._

Ceci est une capture d'écran officielle de l'application :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-99.png)
_Image tirée de la [documentation Crowdin](https://store.crowdin.com/emoji)._

### Emoji Mismatch

Et maintenant, plongeons dans les vérifications d'assurance qualité (QA) automatisées et utiles pour notre projet qui sont disponibles pour les comptes Crowdin Enterprise.

La première est [Emoji Mismatch](https://store.crowdin.com/emoji-mismatch-custom), qui peut nous aider à trouver :

> Les emojis manquants, superflus ou mal assortis dans la traduction.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Emoji-Mismatch.png)
_Emoji Mismatch._

Veuillez noter que cela fonctionne avec Crowdin Enterprise.

### Space After Punctuation

Il s'agit d'un outil d'assurance qualité très utile que vous pouvez ajouter à votre projet.

Crowdin mentionne que [Space After Punctuation](https://store.crowdin.com/space-after-punctuation-custom) :

> Vérifie si la traduction contient les espaces après les symboles de ponctuation.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/space-after-punctuation.png)
_Espace après la ponctuation._

Veuillez noter que cela fonctionne avec Crowdin Enterprise.

### Localisation d'URL (URL Localization)

Il s'agit d'un outil d'assurance qualité que vous pouvez également installer pour votre projet. Avec la [localisation d'URL](https://store.crowdin.com/url-localization-custom), vous pouvez vérifier :

> Les erreurs dans les URL de la traduction selon la configuration de la vérification QA.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/url-localization.png)
_Localisation d'URL._

Veuillez noter que cela fonctionne avec Crowdin Enterprise.

### Mots en double (Duplicated Words)

C'est un excellent outil pour la phase de relecture du projet de localisation. Crowdin mentionne que [Duplicated Words](https://store.crowdin.com/duplicated-words-custom) :

> Supprime chaque deuxième mot répété dans la traduction.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/duplicated-words.png)
_Mots en double._

Veuillez noter que cela fonctionne avec Crowdin Enterprise.

### Cohérence du format de l'heure (Time Format Consistency)

Écrire l'heure dans un format cohérent est également très important lorsque vous localisez un produit.

Crowdin [mentionne](https://store.crowdin.com/time-format-consistency) que :

> Cette vérification QA vérifie que les formats d'heure dans le texte source et traduit correspondent. Elle vérifie les formats d'heure au format 24 heures (HH:MM).

> La vérification QA donnera un résultat positif si le nombre et le format des instances d'heure sont cohérents entre le texte source et le texte traduit, et un résultat négatif s'il y a une incohérence.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/time-format-consistency.png)
_Cohérence du format de l'heure._

Veuillez noter que cela fonctionne avec Crowdin Enterprise.

### camelCase Consistency Check

Cette vérification d'assurance qualité vous aide à vous assurer que les noms de produits, les noms de marques ou d'autres noms qui doivent être écrits en camelCase conservent le même format dans la traduction.

Crowdin [mentionne](https://store.crowdin.com/camelcase-check) qu'elle :

> Valide que tous les mots en camelCase présents dans le texte source sont fidèlement conservés dans le texte traduit.

> Si un mot en camelCase du texte source n'est pas trouvé dans le texte traduit, la vérification échouera et en informera le traducteur avec un message détaillé.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/camelcase-consistency-check.png)
_Vérification de la cohérence camelCase._

### Plus d'applications et d'intégrations

Nous avons vu de nombreuses applications et intégrations utiles pour votre processus de localisation. Elles peuvent optimiser la productivité de votre équipe et vous aider à fournir des traductions de haute qualité.

Mais ce n'est que le début. Crowdin propose plus de 600 applications et intégrations pour votre projet. Vous pouvez trouver une liste complète sur le [Crowdin Store](https://store.crowdin.com/categories/all).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/crowdin-store-2.png)
_Le Crowdin Store._

Si vous cliquez dessus, vous trouverez plus de détails sur ce qu'elles font, comment elles le font, et vous pourriez même trouver le code source qui implémente la fonctionnalité.

Vous pouvez également les trier par pertinence, nom ou date.

Les outils dont vous avez besoin pour être plus productif et fournir des traductions de haute qualité à vos utilisateurs ne sont qu'à un clic.

## 🔹 Comment traduire un site web sur Crowdin

Beau travail ! Nous avons atteint une partie très importante du livre : comment traduire un site web sur Crowdin.

### Comment traduire un site web sur Crowdin

Il existe trois approches principales pour traduire un site web sur Crowdin :

* Intégrations.
* JS Proxy Translator.
* Crowdin In-context.

Puisqu'il existe de nombreuses technologies, frameworks et bibliothèques pour le développement web et que le processus d'internationalisation est très spécifique à la technologie, il est recommandé d'analyser toutes les options disponibles et de trouver celle qui fonctionne le mieux pour votre cas d'utilisation particulier.

### Intégrations

Le monde du développement web est incroyablement diversifié. Nous pouvons créer et héberger des sites web sur une variété de services et les développer à l'aide de différents outils.

Pour prendre en charge cette variété d'outils et de services, Crowdin a développé de nombreuses intégrations avec des plateformes externes pour importer votre texte et envoyer vos traductions au système de gestion de contenu (CMS) de votre choix.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/translate-website-1.png)
_Traduire un site web sur Crowdin._

Par exemple, vous pouvez traduire un site web à partir de WordPress, Webflow, Joomla et d'autres outils similaires.

Selon [Crowdin](https://crowdin.com/blog/2020/12/17/website-translation-with-crowdin) :

> Avec Crowdin, vous n'êtes pas limité à des services de création et d'hébergement de sites web spécifiques.

> Nous n'avons pas seulement 15 applications, dont [Wix](https://store.crowdin.com/wix-proxy-translator), [Ghost](https://store.crowdin.com/ghost-org-proxy-translator), [Squarespace](https://store.crowdin.com/squarespace-proxy-translator) et [Webflow](https://store.crowdin.com/webflow-proxy-translator), qui vous offrent le meilleur moyen de traduire un site web, mais une technologie de [JS Proxy](https://store.crowdin.com/js-proxy-translator) distincte qui vous aidera à localiser n'importe quel autre site web.

Essentiellement, ces technologies :

* Scannent vos pages web.
* Détectent le contenu qui peut être traduit (chaînes).
* Les extraient dans un format qui peut être localisé.
* Synchronisent les traductions avec votre projet original.

Il vous suffit d'ajouter un extrait de code JavaScript à votre code et vous serez prêt à commencer à traduire.

Voici quelques-unes des applications que vous pouvez installer pour commencer à traduire votre site web sur divers services externes :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/apps-for-translation.png)
_Une liste d'applications Crowdin que vous pouvez installer pour [traduire votre site web](https://crowdin.com/blog/2020/12/17/website-translation-with-crowdin)._

Si vous hébergez votre dépôt sur GitHub ou si vous utilisez GitHub Pages, vous pouvez également utiliser l'[intégration GitHub](https://store.crowdin.com/github) de Crowdin et la [GitHub Crowdin Action](https://store.crowdin.com/github-action) pour synchroniser automatiquement les fichiers et les traductions de votre site web.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/github-integrations.png)
_Intégrations GitHub._

### JS Proxy Translator

Les intégrations sont très utiles, mais Crowdin propose également une option qui peut vous aider à localiser n'importe quel site web, quel que soit le service où il est hébergé.

Cette approche de la localisation de sites web sur Crowdin s'appelle [JS Proxy Translator](https://store.crowdin.com/js-proxy-translator).

Crowdin mentionne qu'avec ce proxy, vous pouvez :

* Synchroniser vos sources et votre contenu traduit.
* Localiser votre site web avec un minimum d'effort.
* Extraire le texte source sans aucun codage.
* Traduire les méta-titres et les descriptions pour qu'ils soient optimisés pour le SEO.
* Planifier le moment de la synchronisation de vos traductions.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/js-proxy.png)
_JS Proxy Translator._

Voici deux captures d'écran officielles fournies par l'équipe Crowdin qui montrent les étapes requises pour configurer le JS Proxy Translator.

La première étape consiste à importer le contenu de votre site web. Il vous suffit de saisir l'URL de votre site et de spécifier si vous souhaitez synchroniser les fichiers sources manuellement ou quotidiennement en les important automatiquement une fois par jour.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-104.png)
_JS Proxy Translator (Partie 1). Image tirée de la [documentation Crowdin](https://store.crowdin.com/js-proxy-translator)._

Ensuite, une fois votre texte source traduit, vous pouvez publier les traductions sur votre site web.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-105.png)
_JS Proxy Translator (Partie 2). Image tirée de la [documentation Crowdin](https://store.crowdin.com/js-proxy-translator)._

L'équipe Crowdin [mentionne](https://store.crowdin.com/js-proxy-translator) que :

> Vous devez publier tout le contenu sur votre site web avant de le synchroniser avec votre projet pour la traduction.

Pour en savoir plus sur la façon de traduire un site web avec un JS Proxy sur Crowdin, consultez [ce tutoriel](https://www.youtube.com/watch?v=q_0byyBDRGI) créé par l'équipe Crowdin.

### In-Context pour le Web

La troisième approche de la localisation de sites web sur Crowdin consiste à traduire le texte directement dans le site web ou l'application web à l'aide de Crowdin In-Context.

L'équipe Crowdin [mentionne](https://store.crowdin.com/in-context) que :

> L'outil Crowdin In-Context permet de traduire des textes directement au sein de l'application web réelle. De cette manière, la meilleure qualité de traduction est maintenue.  
>   
> La localisation In-Context est liée au projet réel créé dans Crowdin, sous lequel les fichiers traduisibles sont stockés.  
>   
> Cet outil rend tous les textes de l'application web éditables. De plus, le processus de traduction est visible en temps réel. Même la partie dynamique de l'application et les chaînes qui contiennent des espaces réservés peuvent être traduites de cette manière.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/crowdin-in-context.png)
_Crowdin In-Context._

Vous pouvez le voir en action [ici](https://demo.crowdin.com/), dans la démo officielle de Crowdin :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/demo-website.png)
_Démo Crowdin In-Context._

Si vous vous connectez à votre compte Crowdin, vous verrez ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/demo-website-2.png)
_Démo Crowdin In-Context._

Vous pourrez cliquer sur chaque chaîne du site web pour la traduire et lorsque vous enregistrerez les traductions, elles seront synchronisées avec votre projet Crowdin.

**💡 Conseil :** Pour en savoir plus sur Crowdin In-Context, consultez [ce tutoriel](https://www.youtube.com/watch?v=ktfw7UsW3qw) créé par l'équipe Crowdin.

Ce sont trois approches différentes pour traduire un site web sur Crowdin. Choisir la bonne peut faire toute la différence pour votre équipe de localisation.

Maintenant que vous en savez plus sur les fonctionnalités les plus importantes de Crowdin, plongeons dans l'effort de traduction de freeCodeCamp comme exemple concret d'un projet de localisation mondial alimenté par les contributions d'une incroyable communauté de bénévoles.

## 🔹 L'effort de traduction de freeCodeCamp

🎉 Génial. Félicitations pour avoir atteint cette partie du livre. Cela prouve que vous êtes très intéressé par l'apprentissage de ces compétences.

Maintenant que vous savez comment traduire votre projet sur Crowdin, voyons comment l'incroyable communauté de freeCodeCamp traduit notre contenu dans de nombreuses langues du monde.

Nous verrons cela du point de vue d'un contributeur potentiel, en mettant l'accent sur la façon de traduire notre contenu sur Crowdin.

### Directives de contribution de freeCodeCamp

Si vous êtes un contributeur intéressé par rejoindre l'effort de traduction, par où devriez-vous commencer ?

Vous devriez commencer par lire nos [directives de contribution](https://contribute.freecodecamp.org/#/how-to-translate-files). Il s'agit d'un ensemble d'articles auxquels vous pouvez toujours vous référer si vous avez des questions sur la manière de nous rejoindre ou sur la manière de commencer à traduire et à relire.

Vous y trouverez :

* Un aperçu écrit de Crowdin.
* Comment démarrer.
* Comment sélectionner un projet et un fichier.
* Comment traduire les projets que nous avons sur Crowdin.
* Comment relire les traductions.
* Les meilleures pratiques de traduction, et plus encore !

Dans [cet article](https://contribute.freecodecamp.org/#/how-to-translate-files), vous trouverez des informations sur la manière de vous préparer aux contributions.

Nous recommandons :

* De lire [cette annonce](https://www.freecodecamp.org/news/help-translate-freecodecamp-language/) écrite par Quincy Larson, le fondateur de freeCodeCamp.
* De rejoindre le [forum de la communauté](https://forum.freecodecamp.org/c/contributors/3).
* De rejoindre notre [serveur de chat Discord](https://discord.gg/PRyKn3Vbay).

Notre [documentation](https://contribute.freecodecamp.org/#/how-to-translate-files) mentionne également que travailler avec une petite équipe peut être extrêmement utile pour rester motivé :

> Crowdin et d'autres outils facilitent la contribution aux traductions, mais c'est tout de même beaucoup de travail.  
>   
> Nous voulons que vous preniez plaisir à contribuer et que vous ne fassiez pas de burnout ou ne perdiez pas d'intérêt.  
>   
> Un petit groupe de 4 à 5 personnes est une bonne taille pour commencer votre créneau pour votre langue mondiale. Vous pouvez ensuite recruter encore plus d'amis pour rejoindre l'équipe.

Actuellement, nous avons plus de 30 des langues les plus parlées au monde activées sur notre projet Crowdin.

Certaines d'entre elles sont déployées sur la version en direct de freeCodeCamp. Il vous suffit de les sélectionner dans le menu déroulant pour voir automatiquement une nouvelle langue.

Si vous ne voyez pas vos langues listées, la documentation mentionne également que :

> Si vous souhaitez que nous incluions une nouvelle langue mondiale, nous vous recommandons de susciter l'enthousiasme de vos amis à ce sujet.  
>   
> Une fois que vous avez un petit groupe de personnes (au moins 4 ou 5) intéressées et engagées, nous pouvons organiser un appel. Nous vous expliquerons tous les détails et vous guiderons à travers certains des outils et processus.

Une fois que vous avez fini de lire cette partie des directives de contribution, vous pouvez commencer à contribuer.

Tout d'abord, jetons un coup d'œil aux différents rôles que vous pouvez avoir en tant que contributeur freeCodeCamp.

### Rôles pour le processus de localisation de freeCodeCamp

Vous pouvez contribuer à l'effort de traduction de freeCodeCamp en tant que traducteur ou relecteur.

Les traducteurs nous aident à traduire les fichiers du programme, la documentation et les éléments de l'interface utilisateur de freeCodeCamp comme les boutons et les étiquettes.

Les relecteurs s'assurent que les traductions sont cohérentes, uniformes dans le ton et exemptes de problèmes courants tels que les fautes de frappe.

### Responsables de langue (Language Leads)

Nos responsables de langue seront très heureux de vous accueillir dans notre effort de traduction :

* [Farhan Hasin Chowdhury](https://www.freecodecamp.org/news/author/farhanhasin/) ([@frhnhsin](https://twitter.com/frhnhsin)) dirige la communauté bengalie.
* [Miya Liu](https://www.freecodecamp.org/chinese/news/author/miyaliu/) ([@miyaliu666](https://twitter.com/miyaliu666)) dirige la communauté chinoise.
* [Dario Di Cillo](https://www.freecodecamp.org/italian/news/author/dario/) ([@_DarioDC](https://twitter.com/_dariodc)) dirige la communauté italienne.
* [Yoko Matsuda](https://www.freecodecamp.org/japanese/news/author/yoko/) ([@_sidemt](https://twitter.com/_sidemt)) dirige la communauté japonaise.
* [Alison Yoon](https://www.freecodecamp.org/korean/news/author/alison-yoon/) ([@aliyooncreative](https://twitter.com/aliyooncreative)) dirige la communauté coréenne.
* [Daniel Rosa](https://www.freecodecamp.org/portuguese/news/author/daniel/) ([@Daniel__Rosa](https://twitter.com/Daniel__Rosa)) dirige la communauté portugaise.
* [Nielda Karla Gonçalves de Melo](https://www.freecodecamp.org/portuguese/news/author/nielda/) ([@NieldaKarla](https://twitter.com/NieldaKarla)) dirige la communauté portugaise.
* [Rafael Hernandez](https://www.freecodecamp.org/espanol/news/author/rafael/) ([@RafaelDavisH](https://twitter.com/rafaeldavish)) dirige la communauté espagnole et le processus de localisation.
* [Estefania Cassingena Navone](https://www.freecodecamp.org/espanol/news/author/estefaniacn) ([@EstefaniaCassN](https://twitter.com/EstefaniaCassN)) dirige la chaîne YouTube espagnole.
* [Hillary Nyakundi](https://www.freecodecamp.org/news/author/larymak/) ([@larymak1](https://twitter.com/larymak1)) dirige la communauté swahili.
* [Anastasiia Buievych](https://www.freecodecamp.org/ukrainian/news/author/anastasiia/) ([@anisiangel](https://twitter.com/anisiangel?s=21&t=3yJxu9lXXPDyxB6WYhRsWg)) dirige la communauté ukrainienne.
* [Zaira Hira](https://www.freecodecamp.org/news/author/zaira/) ([@hira_zaira](https://twitter.com/hira_zaira)) dirige la communauté ourdoue.

### freeCodeCamp sur Crowdin

Comme je l'ai mentionné précédemment, Crowdin est la plateforme de traduction que nous utilisons. Il s'agit d'une plateforme de gestion de localisation où les individus, les équipes et les organisations peuvent localiser leurs ressources de manière efficace.

Pour accéder aux projets de freeCodeCamp sur Crowdin :

Rendez-vous sur [translate.freecodecamp.org](https://translate.freecodecamp.org/) et vous verrez le tableau de bord avec les projets sur lesquels nous nous concentrons actuellement :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/freecodecamp.png)
_freeCodeCamp.org sur Crowdin._

Nous avons trois projets principaux :

* [Coding Curriculum](https://translate.freecodecamp.org/curriculum)
* [Learn User Interface](https://translate.freecodecamp.org/learn-ui)
* [Contributing Documentation](https://translate.freecodecamp.org/contributing-docs)

Nous avons également d'autres projets sur Crowdin tels que News UI, Other Courses et Subtitles (Chinese).

### Comment choisir un projet et une langue

Une fois que vous êtes sur notre plateforme de traduction, vous devrez choisir un projet. Disons que vous choisissez de traduire le programme de codage.

Il vous suffit de cliquer sur le projet :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/freecodecamp-dashboard-crowdin.png)
_Cliquez sur le projet auquel vous souhaitez contribuer._

Une fois que vous aurez cliqué sur le projet, vous serez dirigé vers une liste de langues disponibles pour la traduction.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/project-in-crowdin.png)
_Liste des langues disponibles pour le projet Coding Curriculum._

Pour chaque langue, vous verrez :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/language.png)

* Son nom.
* Son code de langue.
* Une barre avec deux couleurs possibles. Le bleu représente la progression de la traduction et le vert représente la progression de la relecture.
* Vous pouvez également voir leurs pourcentages correspondants à droite.
* Le dernier nombre à droite représente le nombre de mots à traduire.

Vous trouverez également un panneau d'information sur la droite avec :

* Une brève description du projet.
* La langue source (anglais).
* Le nombre de contributeurs pour ce projet.
* Combien de mots sources existent dans le projet.
* Quand le projet a été créé et quand il a été actif pour la dernière fois.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/project-in-crowdin.png)
_Consultez les informations sur la droite (le panneau gris)._

Il est maintenant temps de choisir une langue.

Si vous cliquez sur la langue, vous serez dirigé vers la structure du projet avec tous les fichiers et dossiers disponibles pour la traduction.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/spanish-modern-files-crowdin.png)
_La structure du projet Coding Curriculum pour l'espagnol (moderne)._

#### Comment sélectionner un fichier

Pour accéder à l'éditeur de traduction et commencer à traduire, cliquez simplement sur le nom d'un fichier qui nécessite une traduction.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/selecting-a-file.png)
_Sélectionnez un fichier qui nécessite une traduction. Un fichier nécessite une traduction si la barre n'est pas complètement bleue (traduit) ou verte (relu)._

Veuillez noter que nous donnons généralement la priorité à la traduction des trois premières certifications.

💡 **Conseil :** si vous n'êtes pas connecté à votre compte Crowdin ou si vous n'avez pas encore créé votre compte Crowdin, vous serez invité à le faire lorsque vous cliquerez sur un fichier.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/creating-an-account.png)
_C'est l'écran où vous pouvez vous connecter à la plateforme de traduction de freeCodeCamp. Vous pouvez également vous inscrire pour créer votre compte Crowdin._

Si vous vous inscrivez pour un nouveau compte, vous devrez saisir votre e-mail, choisir votre nom d'utilisateur et votre mot de passe. Vous recevrez également un e-mail de Crowdin vous demandant de cliquer sur un lien pour vérifier votre adresse e-mail.

### L'éditeur de traduction

Félicitations. Vous avez maintenant votre compte Crowdin et vous êtes prêt à commencer à traduire le fichier que vous avez sélectionné.

Disons que vous avez cliqué sur le fichier `**build-a-drum-machine.md**` et que vous souhaitez le traduire en espagnol (moderne).

Vous verrez un écran similaire à celui-ci :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/the-translator-ui.png)
_L'éditeur de traduction. C'est ce que vous verrez lorsque vous cliquerez sur un fichier et que vous vous connecterez à votre compte Crowdin._

Si vous souhaitez en savoir plus sur le fonctionnement de l'éditeur, cliquez sur \"Next\" pour voir plus de conseils sur l'interface utilisateur, mais si vous souhaitez fermer ce court tutoriel, cliquez simplement sur le X en haut.

Voici les sept étapes du court tutoriel fourni par Crowdin au cas où vous souhaiteriez les conserver comme référence :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/tutorial-step-2.png)
_Collaborer sur les traductions en temps réel._

![Image](https://www.freecodecamp.org/news/content/images/2023/09/tutorial-step-3.png)
_Utiliser le contexte pour effectuer des traductions pertinentes._

![Image](https://www.freecodecamp.org/news/content/images/2023/09/tutorial-step-4.png)
_Prévisualiser les fichiers._

![Image](https://www.freecodecamp.org/news/content/images/2023/09/tutorial-step-5.png)
_Effectuer des traductions depuis n'importe quel appareil._

![Image](https://www.freecodecamp.org/news/content/images/2023/09/tutorial-step-6.png)
_Passer à la vue côte à côte pour réviser les traductions plus rapidement._

![Image](https://www.freecodecamp.org/news/content/images/2023/09/tutorial-step-7.png)
_C'est tout les amis ! C'est la septième et dernière étape du tutoriel._

Une fois la dernière étape atteinte, cliquez sur \"Close\" et vous serez dans l'éditeur de traduction.

C'est là que la magie opère. Vous pouvez commencer à traduire, enregistrer vos traductions, utiliser les traductions suggérées et les adapter, et même voter pour ou contre les traductions proposées.

Pour traduire une chaîne, cliquez simplement dessus ou enregistrez votre traduction actuelle pour passer à la chaîne suivante.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/translations-editor.png)
_L'éditeur de traductions._

![Image](https://www.freecodecamp.org/news/content/images/2023/09/translations-editor-copy.png)
_C'est ici que vous pouvez écrire et enregistrer votre traduction._

💡 **Conseil :** Vous pouvez également écrire des commentaires et les marquer comme des problèmes pour en informer le personnel de freeCodeCamp et les autres contributeurs.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/comments-sample.png)
_Vous pouvez écrire des commentaires pour des chaînes individuelles et les marquer comme des problèmes._

### Comment traduire l'interface Learn

Nous avons également des directives spécifiques pour traduire l'interface Learn.

Notre [documentation](https://contribute.freecodecamp.org/#/how-to-translate-files?id=translate-the-learn-interface) mentionne que :

> Notre interface `/learn` s'appuie sur des fichiers JSON chargés dans un plugin i18n pour générer le texte traduit. Cet effort de traduction est réparti entre Crowdin et GitHub.

Nous traduisons les fichiers `intro.json` et `translations.json` sur Crowdin. Si vous prévoyez de traduire des chaînes de ces fichiers, sachez que les informations de contexte fournies dans Crowdin peuvent être très utiles.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-68.png)
_Exemple des informations de contexte fournies par Crowdin ([source](https://contribute.freecodecamp.org/#/how-to-translate-files?id=on-crowdin))._

Certains fichiers ne peuvent pas être téléversés sur Crowdin, tels que `links.json`, `meta-tags.json`, `motivation.json` et `trending.json`. Ces fichiers sont généralement maintenus par les responsables de langue, mais si vous souhaitez aider avec ceux-ci, veuillez vous référer à [cet article](https://contribute.freecodecamp.org/#/language-lead-handbook).

### Comment traduire la documentation

La documentation est une autre ressource essentielle pour la mission de freeCodeCamp car nous pouvons partager des informations importantes, des étapes et des directives avec les contributeurs potentiels.

Nous avons certaines directives pour traduire notre documentation. Vous pouvez les [trouver ici](https://contribute.freecodecamp.org/#/how-to-translate-files?id=translate-documentation). Elles couvrent la manière de traduire les liens internes dans la documentation traduite.

### Meilleures pratiques

Pour tout projet, notre objectif devrait toujours être de suivre les meilleures pratiques, n'est-ce pas ? Voici quelques-unes des [meilleures pratiques](https://contribute.freecodecamp.org/#/how-to-translate-files?id=translation-best-practices) que vous devriez suivre pour traduire les ressources de freeCodeCamp :

* Ne traduisez pas le contenu à l'intérieur des balises `<code>`. Ces balises indiquent du texte qui se trouve dans le code et doit être laissé en anglais.
* N'ajoutez pas de contenu supplémentaire. Si vous estimez qu'un défi nécessite des modifications du contenu textuel ou des informations supplémentaires, vous devez proposer les modifications via un ticket GitHub ou une pull request modifiant le fichier anglais.
* Ne modifiez pas l'ordre du contenu.

### Comment devenir relecteur

Si vous rejoignez l'effort de localisation de freeCodeCamp, vous pouvez également [devenir relecteur](https://contribute.freecodecamp.org/#/how-to-proofread-files?id=becoming-a-proofreader).

Nous vous accorderons généralement l'accès à la relecture si vous contribuez à freeCodeCamp depuis un certain temps.

Si vous souhaitez postuler pour devenir relecteur, veuillez nous contacter dans notre [salle de chat pour contributeurs](https://discord.gg/PRyKn3Vbay).

💡 **Conseil :** Les relecteurs peuvent approuver leurs propres traductions. Cependant, nous vous conseillons de laisser un autre relecteur examiner vos propositions de traduction pour vous assurer qu'il n'y a pas d'erreurs ou de fautes de frappe.

### Comment relire les traductions

Lorsque vous devenez relecteur, vous disposez d'autorisations spéciales dans l'éditeur de traductions. Vous pourrez voir les traductions actuelles, les modifier et les approuver.

Vous devez tenir compte des scores de la communauté déterminés par les votes positifs et négatifs lorsque vous décidez quelles traductions approuver.

Lorsque vous approuvez une chaîne, le processus automatisé que nous avons configuré avec l'[intégration GitHub](https://contribute.freecodecamp.org/#/how-to-proofread-files?id=proofread-translations) sur Crowdin l'ajoutera à notre plateforme en direct :

> L'approbation d'une chaîne dans la vue de relecture la marquera comme terminée et elle sera téléchargée lors de notre prochain pull de Crowdin vers GitHub.

### Serveur de chat Discord pour les traducteurs

Si vous avez des questions ou si vous souhaitez rejoindre notre effort de traduction, vous êtes invité à rejoindre notre [serveur de chat Discord](https://contribute.freecodecamp.org/#/how-to-translate-files?id=prepare-yourself-for-contributions) pour les traducteurs.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/discord-chat-room.png)
_Notre serveur de chat Discord._

Une fois que vous aurez créé votre compte et rejoint le serveur, vous verrez un message de bienvenue avec le canal de localisation `**#start-here**`.

Excellent travail. Vous êtes maintenant prêt à commencer à traduire et à rejoindre l'effort de localisation de freeCodeCamp.

## Résumé

Félicitations ! Nous avons couvert de nombreux sujets liés à la localisation et vous en savez maintenant plus sur la manière de localiser vos ressources et vos plateformes pour atteindre les utilisateurs du monde entier.

Voici quelques points clés à retenir :

* Dans un monde globalisé où l'information est disponible en quelques clics, la localisation des produits, services et plateformes est essentielle si votre objectif est d'atteindre les utilisateurs du monde entier. Les adapter à différentes cultures ouvrira des portes à votre équipe, votre organisation et aux utilisateurs du monde entier.
* Crowdin est une puissante plateforme de gestion de localisation axée sur le fait de vous donner, à vous et à votre équipe, les outils dont vous avez besoin pour localiser des produits et des plateformes qui évoluent constamment.
* L'effort de localisation de freeCodeCamp est un exemple concret d'une communauté mondiale réunie par un objectif commun : fournir un accès gratuit à l'éducation dans le monde entier sans barrières linguistiques. Vous pouvez vous joindre à nous aussi.

J'espère que vous avez aimé ce livre sur les fondamentaux de la localisation. Vous êtes prêt à commencer à localiser votre plateforme. C'est le bon moment pour commencer. La localisation peut être exactement ce dont vous avez besoin pour atteindre une communauté mondiale d'utilisateurs.