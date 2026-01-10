---
title: Qu'est-ce que l'Open Source ? Comment contribuer aux projets OSS
subtitle: ''
author: Destiny Erhabor
co_authors: []
series: null
date: '2022-08-16T20:23:53.000Z'
originalURL: https://freecodecamp.org/news/what-is-open-source-software
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/pexels-ben-taylor-109998.jpg
tags:
- name: Collaboration
  slug: collaboration
- name: FOSS
  slug: foss
- name: GitHub
  slug: github
- name: open source
  slug: open-source
seo_title: Qu'est-ce que l'Open Source ? Comment contribuer aux projets OSS
seo_desc: "In this article, we'll talk about open source software. Open source software\
  \ is often considered free software. \nIn this article, I'll give a high-level explanation\
  \ of what open source software (OSS) really is, its advantages in the modern technologi..."
---

Dans cet article, nous parlerons des logiciels open source. Les logiciels open source sont souvent considérés comme des logiciels gratuits. 

Dans cet article, je vais donner une explication de haut niveau de ce qu'est vraiment le logiciel open source (OSS), ses avantages dans le monde technologique moderne, comment l'utiliser, et quelques bonnes pratiques à suivre lors de l'utilisation ou de la contribution à un projet OSS. 

Vous apprendrez des outils et techniques largement utilisés comme GitHub et l'intégration continue, ainsi que la licence à choisir et comment promouvoir la diversité dans les projets open source.

Vous aurez également l'occasion de faire vos premières contributions open source si vous ne l'avez pas déjà fait.

Les mainteneurs et les contributeurs aux projets open source devraient lire cet article.

## Table des matières

* [Qu'est-ce que l'OSS](#heading-quest-ce-que-loss)?
* [Qu'est-ce qu'un logiciel propriétaire](#heading-quest-ce-quun-logiciel-proprietaire)?
* [Modèles de gouvernance open source](#heading-modeles-de-gouvernance-open-source)
* [Pourquoi utiliser des projets open source (avantages)](#heading-pourquoi-utiliser-des-projets-open-source-avantages)?
* [Comment travailler sur un projet OSS](#heading-comment-travailler-sur-un-projet-oss)
* [Comment contribuer aux projets open source](#heading-comment-contribuer-aux-projets-open-source)
* [Conseils utiles pour contribuer](#heading-conseils-utiles-pour-contribuer)
* [Intégration et livraison continues](#heading-integration-et-livraison-continues)
* [Licences OSS et questions juridiques](#oss-licenses-and-legal-issues)
* [Comment choisir une licence pour votre projet OSS](#how-to-chose-a-license-for-your-oss-project)
* [Comment construire de meilleurs projets de logiciels open source](#heading-comment-construire-de-meilleurs-projets-de-logiciels-open-source)
* [Comprendre que le leadership n'est pas le contrôle](#heading-comprendre-que-le-leadership-nest-pas-le-controle)
* [Pourquoi de nombreux projets OSS échouent](#heading-pourquoi-de-nombreux-projets-oss-echouent)
* [Diversité dans l'OSS](#heading-diversite-dans-loss)
* [Comment utiliser GitHub pour héberger des projets OSS](#heading-comment-utiliser-github-pour-heberger-des-projets-oss)

# Qu'est-ce que l'OSS ?

OSS signifie Open Source Software. Ce type de logiciel a un code source librement accessible sous une licence qui vous permet d'examiner, de modifier et d'utiliser ce code sans restriction.

# Qu'est-ce qu'un logiciel propriétaire ?

Contrairement à l'OSS, de nombreuses entreprises utilisent plutôt des logiciels propriétaires. Seuls les propriétaires de logiciels propriétaires ont un accès complet au code source. Les partenaires de confiance peuvent inspecter le code une fois qu'ils ont signé un accord de non-divulgation.

Lors de l'utilisation de logiciels propriétaires, vous devez accepter une licence qui limite votre capacité à partager le produit.

# Modèles de gouvernance open source

Toute organisation qui veut réussir doit être organisée. Il est important de bien réfléchir à la manière dont l'organisation prend des décisions et à qui les prend. 

L'établissement d'un modèle de gouvernance aide à déterminer comment vous pouvez accomplir cela. Parlons de certains de ces modèles maintenant.

### Modèle de gouvernance dirigé par une entreprise

Dans ce modèle, le développement logiciel et la gestion des versions sont gérés par une seule entité. 

* Les contributions externes peuvent être demandées ou non.
* Les plans et les dates de sortie peuvent ne pas être divulgués publiquement, et les conversations non officielles peuvent ne pas être rendues publiques.
* Le logiciel est ouvert (c'est-à-dire public) lorsqu'il est publié. 
* Un exemple de ce modèle est Android par Google.

### Modèle de gouvernance de dictature bienveillante

Dans ce modèle, un individu a une influence dominante sur le logiciel – d'où le terme "dictateur" (mais dans un sens beaucoup plus positif ici).

* La qualité et l'efficacité du projet sont grandement influencées par l'intelligence et la capacité de gestion du dictateur
* À mesure qu'un projet mûrit, le mainteneur écrit moins de code, ce qui peut réduire les discussions et accélérer les progrès.
* Un exemple de ce type de gouvernance est Wikipedia

### Modèle de gouvernance du conseil d'administration (réglementation plus stricte)

* Toutes les discussions sont publiques via des listes de diffusion, et des choix collectifs sont pris.
* Le conseil d'administration décide qui peut contribuer et si le nouveau logiciel est accepté.
* Les versions sont parfois faites moins fréquemment, mais elles sont soigneusement déboguées. 
* Des exemples sont Debian et FreeBSD

# Pourquoi utiliser des projets open source (avantages)

Il y a plusieurs avantages à se lancer dans le développement open source. En voici quelques-uns :

* Vous collaborez avec d'autres contributeurs et obtenez souvent de meilleurs résultats
* Le code source est souvent plus sécurisé et de meilleure qualité 
* L'utilisation des bonnes pratiques OSS aide les développeurs à devenir meilleurs
* Cela réduit le coût de développement
* Cela diminue le temps de mise sur le marché
* Les clients peuvent faire confiance à la qualité car il n'y a pas de secrets et ils savent ce qu'ils obtiennent
* Vous aurez accès à une vaste gamme d'aides pédagogiques peu coûteuses ou gratuites pour l'éducation et l'apprentissage
* C'est un bon moyen d'introduire les débutants sur le lieu de travail

# Comment travailler sur un projet OSS

## Comment contribuer aux projets open source

Avant de contribuer à des projets open source, vous devriez faire quelques recherches sur le projet. Voici quelques façons de se préparer :

### Enquêtez sur le projet

Avant de commencer à travailler sur un projet, vous voudrez en apprendre davantage à son sujet. Tout d'abord, vous devez identifier et comprendre le flux de travail et les styles utilisés par le projet. Ensuite, vous devez déterminer l'étendue et la nature du travail à faire.

### Apprenez ses méthodes de communication

Identifiez comment les mainteneurs du projet communiquent, soit par le biais d'archives d'études, d'une liste de diffusion, ou de certains groupes en ligne ou plateformes de chat.

### Découvrez comment les contributions sont soumises

Les contributions au projet OSS peuvent prendre la forme d'une liste de diffusion, d'un email, ou – peut-être plus couramment – via le système de contrôle de version Git.

### Étudiez l'historique précédent du projet

Étudier l'historique du projet est toujours une bonne idée pour savoir comment il a commencé et comment il a été développé. Vérifiez si le projet offre des contributeurs expérimentés comme mentors.

### Soyez le concierge au début

Offrez vos services pour les tests, la recherche de bugs, etc., avant de commencer à soumettre du code. C'est sain pour les débutants et les personnes nouvelles dans le mode de vie OSS. Cela doit être une étape temporaire.

### Comprenez le langage du projet

Les gens s'intéressent souvent à l'apprentissage de nouveaux langages de programmation en participant à des projets open source qui utilisent ces langages. Mais n'utilisez pas le projet comme un moyen d'**apprendre le langage**.

Avant de penser à faire une contribution logicielle, vous devriez avoir une certaine familiarité avec le langage. La plupart des mainteneurs veulent uniquement des contributions qualifiées – ils n'ont probablement pas le temps de vous enseigner Python ou JavaScript, par exemple. 

Assurez-vous donc d'être compétent dans le ou les langages de programmation utilisés par le projet avant de contribuer. Ne commencez pas à apprendre avec un projet.

### Soyez respectueux

Être poli et respectueux est une partie intégrante de la communauté OSS car elle implique des personnes diverses. Évitez toujours les flammes et le trolling, car ils n'ont pas leur place dans la communauté open source.

### Trouvez un équilibre

Essayez d'atteindre un équilibre entre demander des commentaires et des suggestions tôt dans le processus et retarder vos demandes trop longtemps et surcharger les mainteneurs avec un tas de travail d'un coup.

### Étudiez et comprenez la structure du projet (ADN)

Très probablement, le projet a déjà une structure de leadership formelle ou informelle et une culture établie par la communauté.

Examinez le but du projet et l'impulsion derrière lui. Apprenez à connaître la taille ou la petite taille des contributions typiques, la vitalité de la communauté, et le type de licence utilisé.

## Conseils utiles pour contribuer

Pour réussir à faire des contributions aux projets open source, il y a quelques bonnes pratiques que vous pouvez suivre.

Tout d'abord, vous voudrez identifier les mainteneurs, leur travail et leurs techniques. Il y a des projets avec un seul mainteneur ou de nombreux mainteneurs pour des sous-systèmes individuels. 

Les mainteneurs ont diverses responsabilités également. Ils doivent être capables de comprendre et de réviser toutes les soumissions et de vérifier qu'elles n'ajoutent pas de complexité ou de défauts inutiles. Ils doivent également s'assurer que ces changements n'entrent pas en conflit avec le code existant.

Vous pouvez développer un rapport avec les mainteneurs du projet et les aider avec le débogage, la révision et d'autres tâches selon les besoins.

Il est également important, lorsque vous travaillez sur un projet, d'obtenir des retours tôt et de travailler en toute transparence.

Voici quelques autres conseils rapides à garder à l'esprit :

1. Le projet a probablement beaucoup d'histoire, alors vérifiez pour vous assurer que votre problème n'a pas déjà été résolu ou que quelqu'un d'autre n'a pas soumis une demande de tirage pour le corriger. Votre proposition pourrait être obsolète.
2. Ne proposez pas une nouvelle idée et laissez quelqu'un d'autre la réaliser. Cela montre que vous n'êtes pas engagé à contribuer.
3. Si vous n'êtes pas à l'aise avec le fait que d'autres personnes regardent souvent votre travail, l'OSS n'est peut-être pas le meilleur choix pour vous. Cependant, cela pourrait être une opportunité d'apprendre à recevoir des commentaires et des critiques constructives.
4. Contribuez un peu à la fois – ne faites pas un gros dépôt de code d'un seul coup.
5. Laissez votre ego à la porte. Vous recevrez parfois des critiques sévères et vous devez être capable d'intérioriser calmement les commentaires.
6. Ne discriminez pas les autres.
7. Soyez patient et travaillez à développer des relations professionnelles à long terme avec les autres dans la communauté OSS.

## Intégration et livraison continues 

Lorsque vous travaillez sur un projet OSS, il y aura probablement des directives établies pour la base de code afin de prévenir les conflits, puisque de nombreux contributeurs travailleront ensemble dessus. Les tests peuvent également aider à s'assurer que le code fonctionne comme il se doit.

### Qu'est-ce que l'intégration continue ?

Les techniques d'intégration continue aident à s'assurer que les tests sont effectués souvent et que tout problème ne restera pas découvert longtemps. L'IC aide également à s'assurer que les développeurs dispersés restent synchronisés, même s'ils collaborent à distance partout dans le monde.

Les différentes étapes de l'intégration continue sont l'intégration, la livraison et le déploiement.

* **Livraison continue** : Se traduit par la pratique d'avoir un processus de livraison ou de sortie rapide et automatique une fois les charges fusionnées, et il est publié pour construire des clients.
* **Déploiement continu** : Lorsque le produit est réellement publié pour les clients

Exemples de quelques outils d'intégration continue sont :

* Jenkins
* CircleCI
* GitLab
* Travis

![intégration et livraison continues](https://www.freecodecamp.org/news/content/images/2022/08/cd.png)
_**Processus d'intégration et de livraison continues**. crédits : [Ronak Kumar Samantray](https://substack.com/profile/2655972-ronak-kumar-samantray)_

### Quels avantages l'IC/CD ont-ils pour l'OSS ?

Lorsque plusieurs contributeurs travaillent sur divers aspects d'un projet à partir de diverses perspectives et lieux, il doit se réunir et ne pas être en conflit. De plus, la correction d'un problème ne doit pas entraîner l'émergence de nouveaux problèmes ailleurs. 

Pour accomplir tout cela, vous devez utiliser certains tests automatisés. Donc, lors des tests, vous devez prendre en compte de nombreux facteurs, tels que :

* Si vous pouvez mettre en œuvre des modifications qui se chevauchent en même temps.
* S'il y a des conflits.
* Si le projet peut toujours être compilé après l'application des modifications.
* Si vous apportez toutes les modifications nécessaires, pouvez-vous le livrer ?
* Fonctionne-t-il sur toutes les cibles possibles ?

En s'assurant que les tests sont constants, automatisés et effectués régulièrement, tout problème qui survient est rapidement corrigé, et les développeurs et les utilisateurs restent sur la même page. Et **l'intégration continue** s'assure que l'un de ces problèmes est minimisé.

## Licences OSS et questions juridiques

### Qu'est-ce qu'une licence open source ?

Une licence open source est un type de licence pour logiciel qui permet l'utilisation, la modification et/ou le partage du code source, du plan ou de la conception sous des conditions spécifiques.

Les utilisateurs finaux ou les développeurs peuvent examiner et modifier le code source, le plan ou la conception pour leurs propres cas d'utilisation, leur curiosité ou leurs besoins de dépannage. Bien que ce ne soit pas toujours le cas, les logiciels sous licence open source sont généralement offerts gratuitement.

Il existe deux types de licences logicielles que les projets OSS utilisent généralement :

* **Restrictive** – le logiciel reste ouvert, mais il impose des restrictions strictes sur toute tentative de créer des produits fermés propriétaires. Les modifications du code sont également mises à la disposition des futurs destinataires, comme la licence GPL.
* **Permissive** – ces licences n'exigent pas que les mises à jour et les modifications soient accessibles au public, comme les licences BSD et Apache.

Les entreprises devraient consulter des avocats, internes ou externes, pour s'assurer qu'elles ne violent pas les droits d'auteur et les licences lors de l'utilisation de code provenant de projets open source. 

Il existe de nombreuses licences différentes, alors soyez prudent. Mais une fois qu'une organisation établit des procédures opérationnelles standard appropriées, elle doit les suivre pour chaque projet. 

Les licences OSS aident à donner aux contributeurs une meilleure idée de la manière d'utiliser et de contribuer au code source.

### Licences les plus courantes

* Licence publique générale GNU (GPL) 
* Licence MIT
* Licence Apache 2.0
* Licence BSD 3-Clause "Nouvelle" ou "Révisée"
* Licence BSD 2-Clause "Simplifiée" ou "FreeBSD"
* Licence de bibliothèque GNU ou "Lesser" General Public License (LGPL)
* Licence publique Mozilla 2.0
* Licence de développement et de distribution commune

### Comment choisir une licence pour votre projet OSS

Il s'agit d'un choix crucial qui doit être soigneusement considéré car il peut être difficile ou même impossible de passer à une licence différente plus tard dans l'existence du projet.

Voici quelques éléments à considérer lors du choix d'une licence pour votre projet :

* Si vous avez besoin d'une licence simple et permissive, la licence MIT est succincte et directe. Elle donne aux utilisateurs un accès pratiquement illimité à votre projet. Des exemples de projets utilisant la licence MIT incluent .NET et Rails.
* Si vous êtes plus préoccupé par le partage des améliorations, presque tout peut être fait avec votre projet sous la licence GNU GPLv3, à l'exception de la diffusion de versions à code source fermé. Des exemples de projets utilisant cette licence incluent Ansible et Bash.

Lisez plus sur le choix de la meilleure licence pour votre projet [ici](http://oss-watch.ac.uk/apps/licdiff/) et [ici](https://choosealicense.com/).

# Comment construire de meilleurs projets de logiciels open source

## Comprendre que le leadership n'est pas le contrôle

Un leader efficace permet et encourage tous les participants à s'exprimer et à partager leurs idéaux tout en contribuant. Cela conduit souvent à un travail plus créatif et de haute qualité. Alors rappelez-vous : desserrez les rênes lorsque vous le pouvez.

Selon le paradigme de leadership bien connu appelé "Benevolent Dictator for Life" (BDFL), les contrôleurs d'un projet ne peuvent faire que tant s'ils prennent sans redonner par l'enseignement et la modération.

De plus, si vous êtes un mainteneur, assurez-vous de suivre une formation pour apprendre à être un bon leader. Avoir un bon mentor, par exemple, est vital pour vous aider à acquérir les informations et les compétences nécessaires pour devenir un bon mainteneur.

Si le mainteneur n'est pas utile ou soutien, les nouveaux participants au projet passeront souvent à un autre projet s'ils ne peuvent pas se connecter avec un contributeur expérimenté.

Et enfin, rappelez-vous qu'un projet open source ne peut pas réussir sans confiance. Les réputations se construisent avec le temps, et les nouveaux membres doivent être conscients du passé.

## Pourquoi de nombreux projets OSS échouent

La plupart des projets open source réussis ont commencé petits et ont grandi lentement. Il est souvent difficile de prédire quels projets seront réussis et lesquels ne le seront pas.

Certaines des raisons pour lesquelles les projets OSS échouent sont :

1. Ils essaient de faire la même chose que des programmes plus matures.
2. Ils n'ont pas de bon leadership.
3. Il y a un manque général d'intérêt pour leur produit/service.
4. Ils n'ont pas assez de développeurs
5. Ils n'ont pas la licence correcte.

Pour combattre ces problèmes, voici quelques éléments à garder à l'esprit :

* Assurez-vous d'avoir un bon et efficace leadership, car cela conduit à un travail plus créatif et de haute qualité.
* Assurez-vous que votre projet a une structure de gouvernance et une licence bien définies.
* Encouragez les développeurs travaillant sur votre projet en fournissant des ressources et des informations pour les aider à commencer à contribuer.

## Diversité dans l'OSS

Le mot "Open" dans les logiciels open source (OSS) peut être pris pour signifier un environnement accueillant et amical. Mais cela peut n'être qu'une fausse promesse si le projet ne cultive pas une atmosphère accueillante.

Il existe diverses formes de diversité, telles que la nationalité et la race, le sexe et l'identité de genre, la localisation régionale ou géographique, la politique et les systèmes de croyances, et ainsi de suite.

Il est important de respecter et de favoriser la diversité de toutes les manières possibles. Voici quelques façons de favoriser la diversité dans l'espace OSS :

* Respecter les croyances et les religions des gens
* Ne pas être partial envers les contributeurs pour des raisons liées à la race, au sexe, à l'identité de genre, à la localisation, aux croyances, etc.
* Valoriser les contributions de tous vos contributeurs et interagir avec eux chaque fois que possible.

## Comment utiliser GitHub pour héberger des projets OSS

Avant GitHub, les projets avaient besoin de leurs propres serveurs pour héberger des dépôts. Ils avaient également besoin de développeurs avec des compétences techniques étendues pour configurer, gérer et protéger l'intégrité des dépôts.

Les développeurs peuvent maintenant principalement se concentrer sur le code en utilisant GitHub ou d'autres services d'hébergement Git comme GitLab ou Bitbucket.

### Types de dépôts

Il existe deux types de dépôts sur Git :

* **Dépôts publics** accessibles à tous sur Internet.
* **Dépôts privés**, qui ne sont accessibles qu'à vous, aux personnes avec lesquelles vous partagez explicitement l'accès, et, pour les dépôts d'organisation, à certains membres de l'organisation.

### Pratique pratique utilisant GitHub pour la collaboration

Maintenant, nous allons passer par quelques étapes de base, qui, une fois maîtrisées, vous fourniront le superpouvoir ultime pour une collaboration efficace.

Nous comprendrons plus pleinement en construisant un site web de biographie de noms. Alors, plongeons :

**Voici le** [**Dépôt du projet**](https://github.com/Caesarsage/OSS-Contribution-Beginer.git) **pour que vous puissiez suivre.**

#### Étape 1 – Forker le dépôt

Cela permet de créer une copie du dépôt du projet dans votre compte GitHub pour plus d'accessibilité.

Ensuite, cliquez sur le **lien du projet ci-dessus**, puis forkez le dépôt. Pour forker un dépôt, cliquez sur le bouton fork en haut à droite du site web GitHub du dépôt.

![forker le dépôt](https://www.freecodecamp.org/news/content/images/2022/08/fork.jpg)
_forker le dépôt_

#### Étape 2 – Cloner le dépôt 

Le clonage consiste à créer une copie du code en ligne (votre dépôt) sur votre ordinateur local afin que vous puissiez travailler dessus à partir de là.

Le clonage du dépôt sur votre ordinateur est parfois appelé l'utilisation d'un "**dépôt local**".

Cliquez sur l'onglet code du projet forké sur votre GitHub, puis cliquez sur l'icône copier le code comme montré ci-dessous :

![cloner le dépôt](https://www.freecodecamp.org/news/content/images/2022/08/clone.jpg)
_cloner le dépôt_

Maintenant, allons sur votre ordinateur local. Ouvrez votre éditeur de code préféré (le mien est VSCode) et ouvrez le terminal intégré. Ensuite, collez le code que vous avez copié après une commande 'git clone' pour cloner ce dépôt de projet sur votre ordinateur local comme montré ci-dessous :

```git
git clone <votre-code-de-copie>
```

Maintenant, dans votre terminal, allez dans le dossier du projet généré avec le code ci-dessous :

```git
cd OSS-Contribution-Beginer

```

#### Étape 3 – Créer une branche à partir de votre dépôt local 

Les branches vous permettent de faire des modifications sans affecter le code des autres contributeurs et la branche principale. Il est toujours bon de créer votre propre branche lorsque vous contribuez à des projets.

Pour faire cela, c'est simple – il suffit d'écrire le code suivant :

```git
git branch 'nom-de-la-branche-que-vous-voulez'

par exemple, git branch caesar-name
```

Ensuite, vous pouvez passer à la branche que vous venez de créer :

```git
git checkout caesar-name

```

#### Étape 4 – Apporter des modifications au dépôt

Dans ce scénario, notre problème est de changer le [README.md](http://README.md) pour inclure votre nom, votre pseudonyme sur les réseaux sociaux et votre emoji préféré (vous pouvez parcourir comment obtenir des emojis markdown).

Faites défiler jusqu'en bas du fichier [README.md](http://README.md). Ajoutez votre nom, vos pseudos sociaux et votre emoji à la liste. Ensuite, enregistrez les modifications.

#### Étape 5 – AJOUTER et COMMITTER vos modifications

Ajouter et committer vos modifications est un moyen d'enregistrer les modifications que vous avez apportées dans votre dépôt Git local.

Pour y parvenir, dans votre terminal, exécutez les commandes suivantes :

```git
git add .

```

Ensuite, commitez le code :

```git
git commit -m "ajouté ma bio de nom"

```

#### Étape 6 – Poussez en ligne

Tout ce que nous avons fait dans **l'étape cinq** a été sur votre ordinateur local ou dépôt. Maintenant, il est temps de le pousser vers le dépôt en ligne original sur GitHub.

Vous pouvez faire cela avec les quelques lignes de code ci-dessous :

```git
git push origin -u 'nom-de-votre-branche'
par exemple
git push origin -u caesar-name
```

**Étape 7 – Faire une demande de tirage (PR)**

Vous pouvez informer les gens des modifications que vous avez poussées vers une branche dans un dépôt GitHub en faisant une demande de tirage.

Avant que vos modifications ne soient fusionnées dans la branche principale, vous pouvez examiner et valider les changements potentiels avec les collaborateurs et le mainteneur après avoir soumis une demande de tirage. Vous pouvez même ajouter des contributions de suivi.

Allez dans votre dépôt forké sur GitHub en ligne, voyez vos modifications récentes que vous venez de pousser, et cliquez sur comparer et tirer. Ensuite, cliquez sur le bouton créer une demande de tirage.

![demande de tirage](https://www.freecodecamp.org/news/content/images/2022/08/github-comparepr.png)
_Demande de tirage_

![demande de tirage](https://www.freecodecamp.org/news/content/images/2022/08/open-a-pull-request_crop.jpg)
_demande de tirage_

Hourra ! Félicitations. 🔥💥 Vous avez réussi à faire votre première contribution open source.

# Résumé

L'écosystème open source est vaste et intéressant, et vous pouvez bénéficier beaucoup de la collaboration avec les autres et de la réalisation de contributions.

Dans cet article, vous avez appris comment fonctionnent les projets open source, ce qu'il faut considérer lors du démarrage, comment contribuer et comment fonctionnent les différentes licences.

Comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau. Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/destiny-erhabor) ou [Twitter](https://twitter.com/caesar_sage).

À la vôtre et à la prochaine ! ✌️