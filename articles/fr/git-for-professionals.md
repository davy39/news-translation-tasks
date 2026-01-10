---
title: Git pour les Professionnels – Cours Gratuit de Contrôle de Version
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-09-30T15:29:20.000Z'
originalURL: https://freecodecamp.org/news/git-for-professionals
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/maxresdefault-3.jpeg
tags:
- name: Git
  slug: git
- name: youtube
  slug: youtube
seo_title: Git pour les Professionnels – Cours Gratuit de Contrôle de Version
seo_desc: 'Almost every software developer uses git. Many use it continually throughout
  the day. While you may already know the very basics of git, your productivity will
  be increased if you learn some advanced git concepts.

  We just released a git course on the...'
---

Presque tous les développeurs de logiciels utilisent git. Beaucoup l'utilisent continuellement tout au long de la journée. Bien que vous connaissiez peut-être déjà les bases de git, votre productivité sera augmentée si vous apprenez quelques concepts avancés de git.

Nous venons de publier un cours git sur la chaîne YouTube freeCodeCamp.org qui vous aidera à faire passer vos compétences git au niveau supérieur. 

Tobias Günther a créé ce cours. Il a de nombreuses années d'expérience avec git et a même cofondé Tower, une entreprise qui crée un client GUI pour git.

Dans ce cours, vous apprendrez quelques techniques avancées de git liées aux sujets suivants :

* Le commit parfait
* Les stratégies de branchement
* Les pull requests
* Les conflits de fusion
* Fusion vs. rebase

Regardez le cours complet ci-dessous ou sur [la chaîne YouTube freeCodeCamp.org](https://youtu.be/Uszj_k0DGsg) (1 heure de visionnage).

%[https://youtu.be/Uszj_k0DGsg]

## Transcription

(générée automatiquement)

Ceci est un cours Git intermédiaire enseigné par Tobias Günther.

Il vous aidera à aller au-delà des bases de Git et à améliorer votre flux de travail Git.

Bonjour, amis de Free Code Camp, je m'appelle Tobias.

Et je vais améliorer vos connaissances Git aujourd'hui.

Il y a beaucoup de tutoriels pour débutants sur le contrôle de version avec Git.

Mais je vais vous aider à comprendre les concepts derrière de nombreuses choses dans git, comment créer le commit parfait, comment choisir une stratégie de branchement, ou comment fonctionnent vraiment les conflits de fusion.

Mon objectif est donc de vous donner plus de confiance lorsque vous travaillez avec git, et de vous rapprocher un peu plus de devenir un utilisateur avancé de Git.

Avant de commencer, un grand merci à l'équipe de Free Code Camp, merci beaucoup d'être dans cette mission d'enseigner aux gens comment coder.

Et merci de me permettre de contribuer un peu.

Quelques mots sur mon propre parcours, je fais partie de l'équipe derrière Tower, et Tower est un GUI de bureau pour git.

pour Mac et Windows, nous existons depuis plus de 10 ans maintenant, et avons aidé plus de 100 000 développeurs et designers à travailler plus facilement avec git, à devenir plus productifs avec git, et à faire moins d'erreurs.

Pour la session d'aujourd'hui, vous n'avez pas besoin d'avoir Tower installé, vous pouvez suivre sur la ligne de commande, aucun problème.

Très bien, commençons.

Alors parlons un peu de la façon de créer le commit parfait.

La première partie consiste à ajouter les bons changements, n'est-ce pas.

Et la deuxième partie consiste à composer un bon message de commit.

Alors commençons par ajouter des changements au commit.

Notre objectif ici est de créer un commit qui a du sens, qui n'inclut que les changements d'un seul sujet.

Et contrairement à la manière facile où nous entassons parfois toutes nos modifications locales actuelles dans le prochain commit.

Donc c'est la mauvaise chose que nous ne devrions pas faire.

Mais être sélectif et décider soigneusement ce qui doit aller dans le prochain commit est vraiment important.

C'est une meilleure façon de voir à quoi pourrait ressembler un meilleur commit, car il sépare différents sujets.

D'un autre côté, plus un commit devient grand.

Et plus les sujets sont mélangés dans le commit, plus il devient difficile à comprendre, tant pour vos collègues que pour vous-même à l'avenir.

Le concept de zone de staging de Git est vraiment utile dans ce contexte, il vous permet de sélectionner des fichiers spécifiques, ou même des parties de ces fichiers pour le prochain commit.

C'est ce que la zone de staging peut faire pour vous, vous pouvez vraiment sélectionner des fichiers individuels pour un commit, et même des parties de fichiers pour un commit et laisser les autres pour un futur commit.

Alors regardons un exemple pratique.

Et au cours des dernières heures, ou peut-être même des derniers jours, nous avons créé un tas de changements, disons git status ici.

Mais disons que tous ces changements ne concernent pas le même sujet.

Alors respectons cette règle d'or du contrôle de version qui consiste à ne combiner que les changements d'un même sujet dans un seul commit.

Et vous savez probablement déjà que pour inclure un fichier spécifique, nous pouvons simplement taper, git add et le nom du fichier.

Alors ajoutons ce fichier CSS ici.

Et voilà, et regardons de plus près un autre fichier index HTML et voyons quels changements il contient actuellement.

Nous pouvons utiliser git diff pour cela.

Et nous pouvons voir qu'il y a deux parties ou morceaux de changements pour le moment.

Et disons que le premier appartient au sujet du prochain commit, mais pas le second.

Alors ajoutons simplement la première partie à la zone de staging, nous pouvons faire cela.

Laissez-moi simplement quitter la sortie ici.

Nous pouvons faire cela avec le flag git add git add dash p.

P nous amène au niveau du patch, nous voulons décider au niveau du patch ce qu'il faut inclure et ce qu'il ne faut pas.

Et nous voulons faire cela avec index HTML.

Maintenant, Git parcourt chaque morceau de changements avec nous.

Et il nous pose une question simple.

Voulons-nous ajouter ce morceau ou ce bloc à la zone de staging ou non ? Ne vous inquiétez pas de toutes les autres réponses possibles que vous pouvez donner dans cette situation.

Je ne les connais pas.

Et je veux dormir la nuit pour nous.

Un simple y pour Oui, ou n pour non est suffisant.

Alors disons que celui-ci est en fait le sujet que nous voulons commiter.

Alors disons oui, nous voulons inclure cela.

Et, et pour le second, ce n'est pas le même sujet.

Alors laissons cela hors de la zone de staging pour le moment.

Alors si nous jetons un autre coup d'œil à git status, nous pouvons voir que des parties de index HTML seront incluses dans les prochaines modifications de commit à commiter, et d'autres parties seront laissées pour un futur commit.

Encore une fois, donc index HTML est listé deux fois, génial.

Créer un commit comme celui-ci de manière très granulaire, vous aidera à créer un historique de commit très précieux, facile à lire et à comprendre.

Et cela est crucial si vous voulez rester au top des choses.

Maintenant, parlons de la deuxième partie de la création de ce commit parfait.

Et cela consiste à fournir un excellent message de commit.

Nous commencerons par la ligne de sujet.

Bien sûr, les conventions sont différentes entre les équipes.

Mais généralement, le conseil est d'écrire quelque chose de très concis, moins de 80 caractères si possible.

Et le sujet doit être un résumé très bref de ce qui s'est passé.

Et voici un petit indice, si vous avez du mal à écrire quelque chose de court et concis, alors cela peut être une indication que vous avez mis trop de sujets différents dans ce commit, n'est-ce pas.

Alors allons à la ligne de commande.

Et si je tape maintenant, j'ai quelques changements contre la scène pour le prochain commit.

Si je tape git commit, j'aurai une fenêtre d'éditeur où je peux entrer un message de commit.

Et nous allons écrire quelque chose de simple, ajouter une capture pour l'inscription par email.

Si nous ajoutons une ligne vide après le sujet, git sait que nous écrivons le corps du message et avons de la place pour une explication beaucoup plus détaillée.

Voici quelques questions que vous pourriez vouloir répondre avec le corps de votre message de commit cette année, qu'est-ce qui est différent maintenant par rapport à avant, quelle est la raison du changement ? Et y a-t-il quelque chose à surveiller ou quelque chose de particulièrement remarquable à propos de ce commit.

Alors j'écrirai ma version de cela dans l'éditeur de texte ici.

Et voilà, alors sauvegardons et fermons cela.

Et le commit est fait.

Jetons un coup d'œil rapide à git log, et nous pouvons voir d'accord, donc c'est le dernier commit que nous venons de faire.

C'est le sujet, et c'est le corps du message.

En répondant à ces questions, vous rendez un énorme service à vos collègues et à votre futur moi, car cela aide à comprendre ce qui s'est exactement passé dans cette révision, et à quoi faire attention.

Parlons un peu des stratégies de branchement.

C'est un sujet important car Git vous laisse complètement libre de choisir comment vous voulez travailler avec les branches.

Il ne fournit que l'outil, mais vous et votre équipe êtes responsables de l'utiliser de la manière optimale.

Et cela nous amène à notre premier sujet : les conventions.

Si vous travaillez en équipe, vous devez établir une convention claire sur la manière dont vous voulez travailler avec les branches.

Et vous devez écrire cela quelque part où tout le monde peut y accéder.

Pourquoi votre équipe a-t-elle besoin d'une convention écrite, vous demandez-vous, car Git vous permet de créer des branches, mais il ne vous dit pas comment les utiliser, vous avez besoin d'une meilleure pratique écrite sur la manière de travailler ou sur la manière dont le travail est idéalement structuré dans votre équipe pour éviter les erreurs et les collisions.

Et cela dépend fortement de votre équipe et de la taille de l'équipe, de votre projet, et de la manière dont vous gérez les versions de votre logiciel.

Enfin, cela aide à intégrer de nouveaux membres de l'équipe.

Lorsque de nouvelles personnes rejoignent votre équipe, vous pouvez leur indiquer votre convention écrite et elles comprendront rapidement comment les branches sont gérées dans votre équipe.

Lorsque vous réfléchissez à la manière dont vous voulez travailler avec les branches, vous pensez automatiquement à la manière dont vous intégrez les changements et structurez les versions.

Ces sujets sont étroitement liés.

Pour vous aider à mieux comprendre vos options.

Simplifions un peu.

Je vais vous montrer deux versions extrêmes de la manière dont vous pourriez concevoir vos flux de travail de branchement.

Et la devise de la première est toujours intégrer le développement principal.

Intégrez toujours votre propre travail avec le travail de l'équipe.

C'est la devise ici.

Et voici à quoi cela pourrait ressembler.

Dans cet exemple, nous n'avons qu'une seule branche où tout le monde contribue avec leurs commits.

C'est un exemple vraiment simple, je doute qu'une équipe dans le monde réel ait une structure de branchement aussi simple.

Mais pour l'illustration, cet exemple extrême simplifié nous aide à comprendre les avantages et les inconvénients de ce modèle.

Donc, dans un modèle toujours intégrer, vous avez très peu de branches.

Et cela rend plus facile de garder une trace des choses dans votre projet.

Bien sûr, les commits dans ce modèle doivent également être relativement petits.

C'est une exigence naturelle car vous ne pouvez pas risquer de gros commits gonflés dans un environnement où les choses sont constamment intégrées dans le code de production.

Et cela signifie également que vous devez avoir un environnement de test de haute qualité configuré.

Encore une fois, la prémisse de ce modèle est que le code est intégré très rapidement dans votre ligne principale, votre code de production.

Et cela signifie que les normes de test et de QA dans votre équipe doivent être de premier ordre.

Si vous ne l'avez pas, ce modèle ne fonctionnera pas pour vous.

L'autre extrémité du spectre est lorsque plusieurs types de branches différents entrent en jeu.

Ici, les branches sont utilisées pour remplir différents rôles.

Les nouvelles fonctionnalités et les expériences sont conservées dans leurs propres branches.

Les versions peuvent être planifiées et gérées dans leurs propres branches.

Et même différents états dans votre flux de développement, comme la production, le développement, peuvent être représentés par des branches.

Rappelez-vous que tout cela dépend des besoins et des exigences de votre équipe et de votre projet, il est difficile de dire qu'une approche est meilleure que l'autre.

Et bien qu'un modèle comme celui-ci semble compliqué, c'est surtout une question de pratique et d'habitude.

Et comme je l'ai déjà dit, en réalité, la plupart des équipes travaillent quelque part entre ces extrêmes.

Maintenant, regardons de plus près deux types principaux de branches et comment elles sont utilisées.

Ces deux types de branches sont les branches à long terme et les branches à courte durée de vie.

La distinction entre une branche à long terme et une branche à courte durée de vie est l'une des plus larges que vous puissiez faire et très utile.

Alors commençons par parler des branches à long terme.

Chaque dépôt Git contient au moins une branche à long terme, généralement quelque chose appelé main ou master.

Mais il peut aussi y avoir d'autres branches à long terme dans votre projet, comme develop ou production ou staging.

Par exemple, toutes ces branches ont quelque chose en commun, elles existent tout au long du cycle de vie complet du projet.

J'ai déjà mentionné un exemple typique d'une telle branche à long terme.

Chaque projet a une branche principale comme master ou main.

Et un autre type de branches à long terme sont les branches d'intégration, souvent nommées develop ou staging.

Typiquement, ces branches représentent des états dans un processus de version ou de déploiement de projet.

Si votre code passe par différents états, par exemple, du développement au staging à la production, il est très logique de refléter la structure dans vos branches.

Et enfin, de nombreuses équipes ont une convention liée aux branches à long terme.

Typiquement, les commits ne sont jamais ajoutés directement à ces branches.

Les commits ne doivent arriver à la branche à long terme que par intégration.

En d'autres termes, par une fusion ou un rebase.

Il y a plusieurs raisons à une telle règle.

L'une a à voir avec la qualité.

Vous ne voulez pas ajouter du code non testé et non révisé à votre environnement de production, par exemple.

Et c'est pourquoi le code doit passer par différents états, tests et révisions avant d'arriver enfin en production.

Une autre raison pourrait être le regroupement et la planification des versions, vous pourriez vouloir publier du nouveau code par lots, peut-être même de manière très planifiée.

Et sans une telle règle.

Lorsque le code est directement commis dans des branches à long terme comme main, garder un œil sur ce qui est publié devient assez difficile.

Maintenant, l'autre type de branches sont les branches à courte durée de vie.

Et contrairement aux branches à long terme, elles sont créées pour certains objectifs, puis supprimées après avoir été intégrées.

Il y a de nombreuses raisons différentes de créer des branches à courte durée de vie.

Par exemple, lorsque vous commencez à travailler sur une nouvelle fonctionnalité, une correction de bug ou un refactoring, ou une expérience.

Et typiquement, une branche à courte durée de vie sera basée sur une branche à long terme.

Par exemple, lorsque vous commencez une nouvelle fonctionnalité, vous pourriez baser cette nouvelle fonctionnalité sur votre branche principale à long terme, par exemple, et après avoir fait quelques commits et terminé votre travail, vous voudrez probablement la réintégrer dans main.

Et après avoir fusionné ou rebasé en toute sécurité votre branche de fonctionnalité, elle peut être supprimée.

Et j'ai déjà dit que les stratégies de branchement seront différentes pour chaque équipe et chaque projet.

Cela dépend fortement de vos préférences, de la taille de votre équipe ou du type de projet.

Mais je voudrais vous donner un aperçu de deux stratégies de branchement assez populaires, et prendre les deux comme inspiration pour votre propre stratégie de branchement individuelle.

Commençons par GitHub flow.

GitHub prône un flux de travail extrêmement simple et léger.

Il n'a qu'une seule branche à long terme, la branche principale par défaut, et tout ce sur quoi vous travaillez activement est fait dans une branche séparée, une branche à courte durée de vie, peu importe si c'est une fonctionnalité, une correction de bug ou un refactoring.

Donc c'est une configuration très simple, très légère.

Un autre modèle très populaire s'appelle Git flow.

Et celui-ci offre un peu plus de structure mais aussi plus de règles à suivre.

La branche principale est un reflet de l'état actuel de la production.

L'autre branche à long terme est généralement appelée develop, et toute branche de fonctionnalité commence à partir de celle-ci et sera fusionnée à nouveau dans celle-ci.

Develop est également le point de départ pour toute nouvelle version, vous ouvrirez une nouvelle branche de version, ferez vos tests, commettrez toute correction de bug à cette branche de version.

Et une fois que vous êtes confiant qu'elle est prête pour la production, vous la fusionnez à nouveau dans main, vous ajouterez alors une étiquette pour cette version, commettrez sur Main, et fermerez la branche de version.

Comme vous pouvez le voir, Git flow définit assez quelques tâches et étapes dans le processus.

Dans Tower, le bon GUI de bureau que nous créons, nous aidons les utilisateurs en offrant ces tâches comme raccourcis dans l'application.

Et de cette façon, je peux vous montrer ici, donc vous avez toutes les actions les plus importantes que Git flow vous apporte.

Donc vous n'avez pas à vous souvenir de tous les morceaux et de ce que vous devez faire et de ce qui vient ensuite, ce qui constitue ces différentes étapes.

Donc si vous demandez à différentes équipes comment elles utilisent les branches, vous obtiendrez de nombreuses réponses différentes.

Il n'y a pas de modèle de branchement parfait que tout le monde devrait adopter.

Il s'agit davantage de comprendre votre projet, votre flux de travail de version et votre équipe, puis de modéliser un flux de travail de branchement qui vous soutient de la meilleure manière possible.

Parlons des pull requests.

Tout d'abord, vous devez comprendre que les pull requests ne sont pas une fonctionnalité principale de Git.

Elles sont fournies par votre plateforme d'hébergement Git, ce qui signifie qu'elles fonctionnent et semblent un peu différentes sur GitHub, GitLab, Bitbucket, Azure DevOps, ou ce que vous utilisez.

Mais les principes et idées de base sont toujours les mêmes.

Commençons par parler de pourquoi vous voudriez utiliser des pull requests.

En essence, elles sont un moyen de communiquer sur le code et de le réviser.

L'exemple parfait est lorsque vous avez terminé de travailler sur une fonctionnalité, sans une pull request, vous fusionneriez simplement votre code dans main, master ou une autre branche.

Et dans certains cas, cela peut être totalement acceptable.

Mais surtout lorsque vos changements sont un peu plus complexes ou un peu plus importants, vous pourriez vouloir qu'une deuxième paire d'yeux examine votre code.

Et c'est exactement pour cela que les pull requests ont été créées.

Avec les pull requests, vous pouvez inviter d'autres personnes à réviser votre travail et à vous donner des commentaires.

Et après quelques conversations sur le code, votre réviseur pourrait approuver la pull request et la fusionner dans une autre branche.

Outre cela, il y a un autre cas d'utilisation important pour les pull requests.

C'est un moyen de contribuer au code des dépôts auxquels vous n'avez pas accès en écriture, pensez à un dépôt open source populaire, vous pourriez avoir une idée pour améliorer quelque chose, mais vous n'êtes pas l'un des principaux contributeurs et vous n'êtes pas autorisé à pousser des commits dans leur dépôt.

C'est un autre cas d'utilisation pour les pull requests.

Et nous devons également parler des forks dans cette connexion, un fork est votre copie personnelle d'un dépôt git.

Et en revenant à notre exemple open source, vous pouvez forker le dépôt original.

Faire des changements dans votre version forkée et ouvrir une pull request pour inclure ces changements dans le dépôt original.

Et l'un des principaux contributeurs peut alors réviser vos changements et décider de les inclure ou non.

Je l'ai déjà mentionné.

Chaque plateforme Git a sa propre conception et compréhension de la manière dont les pull requests devraient fonctionner.

Et elles semblent un peu différentes sur GitHub, GitLab, Bitbucket ou Azure DevOps, ou ce que vous utilisez.

Alors voici un exemple, nous utiliserons l'interface GitHub.

Pour ce cas de test, utilisons le dépôt open source Ruby on Rails et voyons.

Très bien, nous voici sur GitHub sur le dépôt principal de Ruby on Rails.

Et en haut à droite, je peux forker ce dépôt, donc je peux créer ma propre version personnelle du dépôt.

Et sa base de code.

Et encore un rappel de pourquoi nous faisons cela, je n'ai pas accès pour pousser du code dans Ruby on Rails, dans le dépôt Ruby on Rails.

Et pour de bonnes raisons, bien sûr, car je ne suis pas un pro de Ruby on Rails.

Mais dans mon propre dépôt fork, je peux faire des changements, je peux faire tous les changements que je veux.

Alors je viens de le faire, j'ai forké le dépôt.

Et je peux maintenant simplement le cloner, je vais obtenir l'URL de clonage, puis sur la ligne de commande, git clone et l'URL distante.

Et nous allons, dans une seconde, quand ce clonage sera terminé, nous allons créer une branche et faire quelques changements.

Donc c'est aussi important de comprendre que les pull requests sont toujours basées sur des branches, pas sur des commits individuels.

Donc nous créons une nouvelle branche que nous demanderons plus tard à être incluse.

Et allons-y, allons dans rails, et ouvrons cela dans mon éditeur.

Et je vais simplement créer une branche git branch test et git checkout test.

Très bien, je suis maintenant sur une nouvelle branche et je peux faire un petit changement stupide, changeons quelque chose dans le fichier readme.

C'est un, un cadre d'application web génial, fermez cela.

Très bien, jetons un coup d'œil à nos changements.

git add README et git commit dash m petit changement stupide.

Donc nous avons maintenant fait quelques petits changements sur une branche séparée, et nous pouvons pousser cette branche vers notre propre dépôt distant, notre fork, donc git push set upstream origin tests test.

Et une fois que cela est disponible, d'accord, donc cela a fonctionné.

Donc nous avons maintenant créé les changements que nous pouvons demander à être inclus.

Une fois que je les ai poussés vers mon dépôt distant sur GitHub, je peux jeter un autre coup d'œil au dépôt dans le navigateur et voir ce qui s'est passé.

Et voilà, GitHub a remarqué que je viens de pousser quelque chose ici.

Et puisque c'est un fork d'un dépôt forké, GitHub a détecté mes changements, et me demande automatiquement si je veux créer une pull request avec ces changements.

Parce que dans un environnement forké, c'est surtout ce que vous voulez faire.

Et si je le fais, je peux proposer dans quelle branche ils devraient être intégrés.

Donc je vais commencer le processus de pull request ici.

Pour le moment, je propose d'intégrer mes changements de ma petite branche ici dans le fork vers la branche principale dans Rails, et disons que c'est bon.

Et je peux ajouter un commentaire.

Et je pourrais alors créer la pull request et le mainteneur du dépôt original serait alors notifié, et ils peuvent réviser mes changements, et éventuellement les intégrer.

Les conflits de fusion, personne ne les aime, mais ils sont un fait de la vie lorsque vous travaillez avec Git.

Et dans la plupart des cas, ils ne sont pas aussi tragiques que nous le pensons souvent.

Oh, nous allons parler de quand ils se produisent, de ce qu'ils sont réellement et de comment les résoudre.

Très bien, le nom le dit déjà.

Fusion.

Les conflits peuvent survenir lorsque vous intégrez lorsque vous fusionnez des changements provenant d'une source différente.

Mais gardez à l'esprit que l'intégration n'est pas limitée à la fusion de branches.

Les conflits peuvent également survenir lors du rebase interactif, lors de l'exécution d'un cherry pick ou d'un pull, ou même lors de la réapplication d'un stash, et toutes ces actions effectuent une sorte d'intégration et c'est à ce moment-là que les conflits de fusion peuvent survenir.

Bien sûr, ces actions ne résultent pas en un conflit de fusion à chaque fois, Dieu merci.

Mais quand exactement les conflits surviennent-ils, en fait, les capacités de fusion de Git sont l'une de ses meilleures caractéristiques et avantages.

La fusion de branches fonctionne sans effort la plupart du temps, car Git est généralement capable de comprendre les choses par lui-même.

Mais il y a des situations où des changements contradictoires ont été faits.

Et c'est à ce moment-là que la technologie ne peut tout simplement pas décider ce qui est juste ou faux.

Ces situations nécessitent une décision humaine.

Le classique est lorsque la même ligne de code exacte a été modifiée dans des commits sur deux branches différentes.

Git n'a aucun moyen de savoir quel changement vous préférez.

Il y a quelques autres situations similaires qui sont un peu moins courantes, par exemple, lorsqu'un fichier a été modifié dans une branche et supprimé dans une autre.

Mais le problème est toujours le même, les changements se contredisent lorsque vous travaillez avec un GUI de bureau comme Tower, cela peut faciliter les choses, surtout parce que c'est juste plus visuel, je peux sélectionner des choses ici.

Et cela m'aide à comprendre ce qui se passe réellement, je peux voir ces deux changements en conflit et je peux en sélectionner un ou les deux ou juste celui-ci et résoudre le conflit assez facilement.

Comment savez-vous qu'un conflit s'est produit ? Ne vous inquiétez pas, git vous le dira très clairement lorsqu'un conflit se sera produit.

Tout d'abord, il vous le fera savoir immédiatement dans la situation, par exemple, lorsqu'une fusion ou un rebase échoue avec un conflit.

Alors essayons cela.

En fait, nous avons quelque chose ici, provoquons un conflit de fusion.

Et je vais simplement essayer de fusionner dans developer vers ma branche principale.

Et voilà, automatiquement je peux voir que quelque chose ne va pas ici.

Conflit conflit conflit, la fusion automatique a échoué.

Donc vous pouvez voir que lorsque j'ai essayé d'effectuer la fusion, je suis tombé sur un conflit et git me dit instantanément le problème.

Mais même si j'avais manqué ces messages d'avertissement, je découvrirais le conflit la prochaine fois que je lancerais git status.

Alors faisons cela.

Et assez rapidement, vous avez cette catégorie de chemin non fusionné dans le statut ici.

En d'autres termes, ne vous inquiétez pas de ne pas remarquer les conflits de fusion, git s'assure que vous ne pouvez pas les ignorer.

Très bien, même si vous ne pouvez pas ignorer un conflit de fusion, vous devez vraiment le traiter avant de pouvoir continuer votre travail.

Traiter un conflit de fusion ne signifie pas nécessairement que vous devez le résoudre, vous pouvez aussi l'annuler.

Et cela est parfois très utile.

Alors gardez cela à l'esprit toujours, vous pouvez toujours annuler un conflit de fusion et revenir à l'état précédent.

Et cela est vrai même lorsque vous avez déjà commencé à résoudre certains des fichiers en conflit et que vous remarquez Oh mon dieu, je suis, je suis sur la mauvaise voie ici.

Même alors, lorsque vous vous trouvez dans une impasse, vous pouvez toujours annuler la fusion.

Et certaines commandes sont livrées avec une option d'annulation qui vous permet de faire exactement cela.

Les exemples les plus marquants sont Git merge, Uber abort, et Git rebase abort.

Donc dans notre exemple, ici, lorsque je trouve pourquoi je n'ai pas le temps de m'occuper de cela maintenant, ou j'ai résolu quelque chose de la mauvaise manière, je peux toujours taper Git merge dash dash abort ici, et git status me montre que je suis de retour à la normale.

Donc cela devrait vous donner la confiance que vous ne pouvez vraiment pas tout gâcher, vous pouvez toujours annuler, revenir à un état propre et réessayer, recommencer.

Alors voyons à quoi ressemble vraiment un conflit sous le capot, nous allons démystifier ces petits bugs.

Et, en même temps, vous aider à perdre le respect pour eux et à gagner un peu de confiance.

Alors comme exemple, regardons le contenu de l'un des fichiers en conflit.

Je vais provoquer ce conflit de fusion une fois de plus, et je peux voir que dans mon fichier index HTML, j'ai un conflit.

Alors regardons cela.

Et non, pas celui-ci.

Mais celui-ci.

Alors git a eu la gentillesse de marquer les zones problématiques dans le fichier.

Donc elles sont entourées de ces symboles ici.

C'est le début et c'est la fin de la zone problématique.

Donc le contenu qui vient après le premier marqueur, provient à l'origine de notre branche de travail actuelle, puis aligné avec quelques lignes égales, des signes égaux, séparent les deux changements en conflit.

Et enfin, celui-ci vient de l'autre branche qui est également affichée.

Donc dans ce cas, c'est assez simple.

Dans la branche develop où j'ai fait quelques changements, j'ai supprimé cet élément de liste, ces éléments de liste, et dans ma branche principale, je les ai changés.

Donc Git n'est pas sûr, vouliez-vous les changer ? Comme ça ? Ou vouliez-vous les supprimer ? Comme ici ? Et je dois dire à git, ce qui est correct et ce qui ne l'est pas.

D'accord, alors comment pouvez-vous résoudre un conflit, résoudre le conflit est en fait assez simple, nous devons nettoyer ces lignes.

Et après avoir terminé, le fichier doit avoir exactement l'apparence que nous voulons.

Donc il peut être nécessaire de parler au collègue qui a écrit les autres changements et de décider quel code est réellement correct, peut-être que c'est le nôtre, peut-être que c'est le leur, peut-être que c'est un mélange des deux.

Et ce processus de nettoyage du fichier, en s'assurant qu'il contient ce que nous voulons réellement.

Cela n'a pas besoin d'impliquer de magie, vous pouvez faire cela simplement en ouvrant votre éditeur de texte ou votre IDE et en faisant quelques changements.

Parfois, cependant, vous constaterez que ce n'est pas la manière la plus efficace, c'est là que des outils dédiés peuvent vous faire gagner un peu de temps et d'efforts.

Donc d'une part, il y a de bons GUI de bureau.

Certaines des interfaces graphiques pour git peuvent être utiles lors de la résolution de conflits, vous en avez déjà vu une.

Donc c'est Tower où vous pouvez voir ce qui s'est passé dans le conflit.

Et cela visualise le problème.

Et d'autre part, il y a des outils de fusion dédiés.

Pour des conflits plus compliqués, il peut être génial d'avoir un outil de fusion différent dédié à portée de main, vous pouvez configurer un outil de choix en utilisant la commande Git config.

Et puis en cas de conflit, vous pouvez simplement taper Git merge tool et l'avoir ouvrir le conflit, j'ai une application kaleidoscope installée sur mon Mac.

Donc essayons simplement cela Git merge tool.

Je l'ai configuré.

Donc le premier, comme vous pouvez le voir, est assez facile ou le second ici, error HTML a été supprimé.

Donc je n'ai pas besoin de voir cela, je dois simplement décider, est-ce que je veux le garder ou est-ce que je veux le supprimer.

Donc je vais rester avec la suppression.

Et pour le second, il y a vraiment du contenu dans le fichier, où il est logique d'ouvrir cet outil de fusion que j'ai configuré, je peux voir, bien, c'est le changement que j'ai fait.

Et c'est le changement qui vient d'une autre personne ou d'une branche différente.

Et à quoi je veux que cela ressemble et à quoi je voulais que cela ressemble, je peux choisir ces changements, ou ceux de cette année ou je peux faire mes propres changements ici.

Donc après avoir nettoyé le fichier, soit manuellement, soit dans un GUI de bureau, ou un outil de fusion, nous devons commiter cela comme tout autre changement.

Donc je peux l'enregistrer ici et dire que c'est résolu.

Et si je tape git status, je peux voir ces changements seraient commis, j'ai fait quelques changements ici dans index HTML, ceci est juste une copie de sécurité, vous pouvez configurer cela pour se produire également.

Donc vous pouvez toujours revenir au fichier original.

Mais je vais en fait juste commiter cela ici.

Et simplement en commettant les fichiers résolus, je signale à git que le conflit est terminé.

Et je peux continuer mon travail.

La plupart des développeurs comprennent qu'il est important d'utiliser des branches dans git, car avoir des conteneurs séparés pour votre travail est incroyablement utile.

Parlons un peu de l'intégration des branches, de la récupération de votre nouveau code dans une branche existante.

Il y a différentes façons de faire cela, et les deux plus courantes sont la fusion et le rebase.

Commençons par parler de la fusion et de son fonctionnement.

Lorsque Git effectue une fusion, il recherche trois commits.

Tout d'abord, le commit ancêtre commun.

Si vous suivez l'historique de deux branches dans un projet, elles ont toujours au moins un commit en commun.

À ce stade, les deux branches avaient le même contenu.

Et après cela, elles évoluent différemment.

Les autres commits intéressants sont les points de terminaison de chaque branche.

Rappelez-vous que le but d'une intégration est de combiner les états actuels de deux branches.

Donc les dernières révisions sont bien sûr importantes.

La combinaison de ces trois commits effectuera l'intégration que nous visons.

J'ai choisi un cas d'exemple très simple ici car l'une des deux branches, la branche a ici, n'a pas reçu de nouveaux commits après le branchement.

Donc son dernier commit est également l'ancêtre commun.

Dans ce cas, l'intégration est très simple, git peut simplement ajouter tous les nouveaux commits de la branche B au-dessus du commit ancêtre commun.

Et la forme la plus simple d'intégration est appelée une fusion rapide.

Les deux branches partagent alors exactement la même histoire.

Dans la plupart des cas, cependant, les deux branches évoluent différemment, bien sûr.

Et pour faire une intégration, git devra créer un nouveau commit qui contient les différences entre elles.

Et c'est ce que nous appelons un commit de fusion.

Normalement, un commit est soigneusement créé par un être humain à une unité significative qui n'enveloppe que des changements liés dans le message de commit fournit un contexte et des notes.

Maintenant, un commit de fusion est un peu différent.

Il n'est pas créé par un développeur, il est créé automatiquement par Git.

Et il n'enveloppe pas non plus un ensemble de changements liés.

Son but est de connecter deux branches comme un nœud.

Si vous voulez comprendre une opération de fusion après coup, vous devez jeter un coup d'œil à l'historique des deux branches et à leur historique de commit.

Maintenant, parlons de rebase.

Mais avant de commencer, laissez-moi souligner quelque chose : rebase n'est ni meilleur ni pire que merge.

Plus important encore, c'est différent.

Vous pouvez vivre une vie heureuse avec git en utilisant uniquement merge.

Mais rebase a ses avantages et ses inconvénients.

Donc savoir ce qu'il fait et quand il pourrait être utile est bien.

Très bien, rappelez-vous que nous venons de parler du commit de fusion automatique, certaines personnes préféreraient s'en passer, elles veulent que l'historique du projet ressemble à une ligne droite, sans aucun signe qu'il ait été divisé en plusieurs branches à un moment donné, même après que les branches aient été intégrées.

Et c'est ce qui se passe avec rebase.

Parcourons une opération de rebase étape par étape.

Le scénario est le même que dans l'exemple précédent, nous voulons intégrer les changements de la branche B dans la branche a.

Mais maintenant en utilisant rebase.

La commande Git réelle pour démarrer cela est vraiment simple.

C'est juste Git rebase et la branche.

Similaire à Git merge, nous disons simplement à git quelle branche nous voulons intégrer.

Mais jetons un coup d'œil derrière les scènes.

Tout d'abord, git supprimera tous les commits sur la branche a qui se sont produits après le commit ancêtre commun.

Mais ne vous inquiétez pas, il ne les jettera pas, vous pouvez penser à ces commits comme étant garés, sauvegardés quelque part temporairement.

Ensuite, git applique les nouveaux commits de la branche B.

Et à ce stade, temporairement, les deux branches se ressemblent exactement.

Mais dans l'étape finale, ces commits garés doivent être inclus, les nouveaux commits de la branche a, ils sont positionnés au-dessus des commits intégrés de la branche B, ils sont rebasés, comme vous pouvez le voir, et le résultat ressemble à un développement qui s'est déroulé en ligne droite, il n'y a pas de commit de fusion qui contient toutes les modifications combinées, nous préservons la structure de commit originale.

Il y a une autre chose, une chose importante à comprendre à propos de rebase, il réécrit l'historique des commits.

Alors regardez de près ce dernier diagramme ici.

Le commit c trois a un symbole astérisque, il a le même contenu que C trois, mais c'est effectivement un commit différent.

Parce qu'il a maintenant un nouveau parent avant le rebase.

Voir, un était son parent.

Et après le rebase, c'est C quatre sur lequel il a été rebasé, un commit n'a qu'une poignée de propriétés importantes comme l'auteur, la date, l'ensemble des changements et quel est son commit parent.

Et changer l'une de ces informations crée effectivement un commit complètement nouveau et avec un nouveau hash de commit.

Donc réécrire l'historique comme cela n'est pas un problème pour les commits qui n'ont pas été publiés ou poussés.

Mais si vous réécrivez des commits qui ont déjà été poussés vers un dépôt distant, vous pourriez avoir des problèmes.

Parce qu'un autre développeur pourrait avoir basé son travail sur le commit c trois original, qui n'est plus ici.

Donc terminons ce sujet avec une règle simple.

Ne réécrivez pas les commits que vous avez déjà poussés vers un dépôt partagé.

Des outils comme rebase, vous ne devriez les utiliser que pour nettoyer votre historique de commits local.

Par exemple, pour une branche de fonctionnalité sur laquelle vous avez travaillé pendant un certain temps, et avant de l'intégrer à nouveau dans une branche d'équipe, alors vous utilisez rebase pour cela, c'est pour cela que ces outils comme rebase ont été créés.

Très bien, c'est tout pour aujourd'hui.

Assurez-vous de consulter mon petit kit Git avancé.

Il est complètement gratuit.

C'est une petite collection de courtes vidéos sur de nombreux sujets Git avancés, des choses comme le rebase interactif, jusqu'aux stratégies de branchement, les conflits de fusion, les sous-modules, que sais-je.

C'est vraiment utile si vous voulez devenir plus productif avec Git et le contrôle de version.

Et encore une fois, c'est gratuit.

Plus de droits ? Amusez-vous et à bientôt ici sur la chaîne YouTube Free Code Camp.