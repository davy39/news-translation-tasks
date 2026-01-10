---
title: Comment fonctionnent les branches Git
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-07-13T13:44:04.000Z'
originalURL: https://freecodecamp.org/news/how-git-branches-work
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/gitbranches.png
tags:
- name: Git
  slug: git
- name: youtube
  slug: youtube
seo_title: Comment fonctionnent les branches Git
seo_desc: 'Branches are one of Git''s most important concepts. And to master Git,
  it''s essential to have a thorough understanding of how branches work.

  We just released a tutorial about Git branches on the freeCodeCamp.org YouTube channel.

  You will learn about t...'
---

Les branches sont l'un des concepts les plus importants de Git. Et pour maîtriser Git, il est essentiel de bien comprendre comment fonctionnent les branches.

Nous venons de publier un tutoriel sur les branches Git sur la chaîne YouTube de freeCodeCamp.org.

Vous apprendrez les nombreuses actions que vous pouvez effectuer autour des branches - de la création et de la suppression à la publication, au renommage et à la comparaison. Ce tutoriel se concentre sur l'utilisation de Git avec la ligne de commande. Vous n'avez pas besoin de logiciel GUI pour suivre.

Ce tutoriel a été créé par Tobias Günther de Tower. Tower crée une puissante interface graphique Git pour Mac et Windows.

Voici ce qui est couvert dans le tutoriel :

* Les branches en tant que concept central dans Git
* Concepts de base : la branche HEAD
* Concepts de base : branches locales vs. branches distantes
* Création de nouvelles branches
* Changement de branches
* Renommage de branches
* Publication de branches
* Suivi de branches
* Tirer + pousser des branches
* Suppression de branches
* Fusion de branches
* Rebasing de branches
* Comparaison de branches
* Fiche mémo sur le travail avec les branches

Regardez le cours complet sur [la chaîne YouTube de freeCodeCamp.org](https://youtu.be/e2IbNHi4uCI) (33 minutes de visionnage).

%[https://www.youtube.com/watch?v=e2IbNHi4uCI]

## Transcription

(générée automatiquement)

Les branches sont l'un des concepts les plus importants.

Dans ce cours, Tobias vous donnera une compréhension approfondie de comment fonctionnent les branches dans Git.

Et n'oubliez pas de cliquer sur le bouton s'abonner pour ne pas manquer nos excellents cours.

Bonjour les amis de Free Code Camp.

Je m'appelle Tobias et je vais expliquer comment travailler avec les branches dans Git.

L'un des sujets centraux et les plus importants dans Git et le contrôle de version est comment vous pouvez travailler de manière productive avec vos branches et ce que vous pouvez faire pour commencer.

Mais avant de commencer, laissez-moi rendre un énorme hommage aux gens de Free Code Camp pour enseigner aux gens comment coder gratuitement sur Internet.

Merci beaucoup d'être dans cette mission.

Et merci de me laisser aider un peu avec cette contribution.

Quelques mots sur mon parcours, je fais partie de l'équipe derrière Tower, Tower est une interface utilisateur graphique pour Git sur Mac et Windows.

Et nous existons depuis plus de 10 ans maintenant.

Et en ces 10 ans, nous avons aidé environ 100 000 personnes dans des entreprises grandes et petites, des freelances, chaque développeur dans chaque partie du monde, à travailler plus facilement avec le bon système de contrôle de version, à enlever le mal de tête de Git et à le rendre plus facile.

Cet atelier aujourd'hui ne sera pas sur Tower, ne vous inquiétez pas, vous n'avez pas besoin d'avoir Tower installé, nous ferons tout sur la ligne de commande.

Ainsi, vous pouvez suivre, peu importe ce que vous utilisez.

Alors avant de commencer, de quoi va-t-il s'agir ? Les branches sont l'un des concepts centraux dans Git.

Et il y a vraiment une quantité infinie de choses que vous pouvez faire avec elles, vous pouvez les créer et les supprimer, vous pouvez comparer, vous pouvez fusionner et rebaser, vous pouvez publier et suivre.

Nous parlons donc de toutes ces choses que vous pouvez faire avec vos branches.

Avant de plonger dans les détails, laissez-moi brièvement parler de deux concepts centraux qui sont mentionnés encore et encore.

L'un est la branche HEAD.

Si vous ne connaissez pas ce terme, c'est assez important.

C'est la branche actuellement active ou la branche cochée, vous pouvez avoir de nombreuses branches dans votre dépôt, mais vous ne pouvez en avoir qu'une seule active à un moment donné.

Ainsi, si vous tapez git status sur votre ligne de commande ou êtes dans une interface utilisateur graphique, vous verrez que vous êtes sur une certaine branche, dans cet exemple ici sur la branche master.

Ainsi, master est actuellement la branche HEAD, la branche active.

Et l'autre concept central est la distinction entre les branches locales et distantes.

Ainsi, lorsque nous travaillons avec des branches, nous sommes 99 % du temps ou 95 % du temps, nous travaillons avec des branches dans notre dépôt Git local, n'est-ce pas ? Les branches distantes dans votre GitHub, git lab, Bitbucket, en tant que votre DevOps, peu importe ce que vous avez, elles sont plus pour la synchronisation, n'est-ce pas, la majorité du travail réel se fait dans vos branches locales sur votre machine locale dans votre dépôt Git local.

D'accord, commençons par créer de nouvelles branches.

Bien.

Ainsi, avant de pouvoir travailler avec des branches, vous devrez d'abord en avoir dans votre dépôt.

Et pour créer une nouvelle branche, vous pouvez simplement utiliser la commande git branch et fournir le nom de votre branche.

Ainsi, ma nouvelle branche est le nom de cette nouvelle branche.

Et lorsque je le fais comme ça, en fournissant simplement un nom à la commande git branch, git supposera que je veux commencer ma nouvelle branche basée sur la révision actuellement cochée.

Ainsi, je vais créer une nouvelle branche sur la situation où j'en étais à ce point.

Ainsi, si je veux créer une nouvelle branche à une autre révision spécifique, disons, voyons quelles révisions nous avons dans ce dépôt.

Au fait, donc c'est cette tour, l'interface utilisateur graphique que nous créons.

Voici ma nouvelle branche, je viens de la créer.

Ainsi, cela a fonctionné, bonne nouvelle.

Si je veux créer ma branche sur une révision différente, disons que je veux commencer ici, je peux simplement copier le hachage de révision de ce commit ici.

Et ensuite sur la ligne de commande, je peux taper git branch, autre branche, c'est le nom et je voulais commencer sur cette révision ici.

D'accord, voyons ce que cela a fait.

D'accord, et nouvelle branche.

Ainsi, cela a fonctionné.

Et cela a commencé sur cette révision ici, n'est-ce pas ? Vous êtes assez flexible sur la manière dont vous voulez commencer vos branches.

Et encore une fois, comme je l'ai mentionné brièvement, dans cette zone de concept central il y a quelques secondes, vous ne pouvez créer de nouvelles branches que dans votre dépôt local, n'est-ce pas ? La création de branches dans un dépôt distant se fait en publiant une branche locale existante, donc je peux, je peux télécharger celles-ci ici, mais je ne peux pas créer une branche sur un dépôt distant, nous en parlerons plus tard.

Ou écrire git branch, soit sans mentionner une révision spécifique, puis ce sera votre révision actuelle, ou mentionner une révision spécifique pour commencer sur une révision spécifique.

D'accord, changer de branches, bien sûr, une autre action très importante que vous allez utiliser tout le temps.

Ainsi, la branche actuelle, la branche cochée, pour ainsi dire, la branche HEAD, définit le contexte dans lequel se trouve votre travail à ce moment.

Et les nouvelles commits seront créées dans les branches HEAD actuelles, elles seront créées dans ce contexte.

Et pour changer la branche sur laquelle vous travaillez actuellement.

Cela signifie cocher une autre branche ou changer de branche.

Et voyons comment nous pouvons faire cela.

Très bien, donc en ce moment, si je tape git status, je peux voir que je suis sur la branche main.

Ainsi, main est actuellement cochée, c'est ma branche HEAD.

Et si je veux que ce soit une autre branche, je peux taper git checkout.

Et comme nous avons tant de belles nouvelles branches, obtenir une nouvelle branche.

Et pendant que je suis passé à la branche, ma nouvelle branche, donc la commande git checkout est assez polyvalente.

Elle est utilisée pour tant de choses.

Ces dernières années, une nouvelle commande a été ajoutée à la palette de commandes Git, et je vous suggère de l'utiliser à l'avenir.

Parce que Git switch est uniquement pour ce but.

Il est uniquement pour changer de branches.

Ainsi, si nous voulons passer à la branche que nous avons créée, je peux taper Git switch, autre branche et git switch, comme je l'ai dit, est un peu plus ambigu.

Parce qu'il n'a que ce but.

git checkout est une commande avec beaucoup de significations.

Ainsi, je suis plus à l'aise avec Git switch, git checkout et git switch à nouveau.

Ainsi, vous pouvez voir dans une interface utilisateur graphique, c'est là que le pointeur HEAD pointe maintenant.

Ainsi, d'autres branches, actuellement la branche cochée, la branche active.

D'accord, numéro trois, renommer les branches, il est assez facile de mal taper le nom d'une branche ou de changer d'avis après coup.

Ainsi, ne vous inquiétez pas, vous pouvez renommer les branches, bien sûr, et git le rend assez facile pour renommer votre branche HEAD locale.

Faisons cela.

Ainsi, nous sommes actuellement sur.

Encore une fois, tapons git status pour nous assurer que nous sommes sur la branche autre branche.

Et si je ne suis pas satisfait de ce nom, je peux simplement le changer en utilisant git branch avec le paramètre dash m, puis fournir un nouveau nom.

Ainsi, meilleure branche, appelons-la comme ça.

Et regardez.

D'accord, je suis maintenant sur la branche, meilleure branche.

Et c'était assez facile.

Au cas où vous voudriez renommer une autre branche, pas la branche HEAD, pas la branche actuellement cochée, alors nous devons fournir le nom de l'ancienne branche pour rendre cela ambigu, donc en ce moment, nous avons, voyons quelles branches nous avons.

Nous utilisons git branch sans aucun paramètre.

Très bien, donc meilleure branche main et ma nouvelle branche.

Ainsi, disons que je veux renommer une branche non HEAD, une branche qui n'est pas actuellement cochée.

Disons que je veux renommer ma nouvelle branche ici.

Faisons un peu de place.

D'accord, donc renommons git branch, dash m, ma nouvelle branche et appelons-la ma meilleure branche.

Voyons si cela fonctionne.

git branch sans aucun paramètre vous montre quelles branches vous avez actuellement.

Et voilà, nous venons de changer le nom d'une branche non HEAD comme ceci.

Ainsi, ces commandes sont utilisées pour changer les noms des branches locales.

Si vous souhaitez renommer une branche distante, les choses sont un peu plus compliquées car Git ne vous permet pas de renommer des branches distantes.

Ainsi, en pratique, le renommage d'une branche distante peut être fait en supprimant l'ancienne et en poussant ou en publiant la nouvelle depuis votre dépôt local.

Prenons un autre exemple de ce que nous avons.

Ainsi, si je ne suis pas satisfait de l'origine, la mise en scène de ce nom ici, je peux le supprimer puis le retélécharger et je vous montrerai comment publier ou télécharger votre marque pour la première fois dans une seconde, afin que nous puissions voir comment cela fonctionne.

D'accord, renommer les branches avec la commande git branch dash M.

Et si vous avez une branche non HEAD que vous voulez renommer, fournissez l'ancien nom, puis le nouveau nom.

Cela concerne le renommage des branches distantes.

Et nous le ferons dans un moment où nous créons une nouvelle branche et la poussons pour la première fois.

Ainsi, nous pouvons faire deux choses en une.

D'accord, publier des branches.

Comme je l'ai déjà dit, il n'est pas vraiment possible de créer une nouvelle branche sur un dépôt distant.

Ce que nous pouvons faire, cependant, c'est republier une branche locale existante sur un dépôt distant.

Ainsi, nous pouvons télécharger ce que nous avons localement sur le serveur distant et ainsi le partager avec notre équipe, n'est-ce pas.

Voyons donc ce que nous avons et ce que nous pouvons publier.

D'accord, donc en ce moment, nous avons cette belle branche de téléchargement de fonctionnalités ici, et elle n'est pas présente sur le dépôt distant.

Ainsi, disons que je veux la publier pour la première fois, je veux la télécharger sur le serveur distant nommé origin.

Et faisons cela sur la ligne de commande.

Ainsi, je peux simplement utiliser git push dash u, je vais expliquer à quoi sert le drapeau u dans une seconde.

Sur le dépôt distant Origin, et c'est la branche de téléchargement de fonctionnalités.

Bien, cela a l'air bien.

D'accord, nous y voilà.

Nous venons de télécharger cette branche locale vers le dépôt distant.

Maintenant, nous allons parler de ce drapeau dash u ici en détail dans une seconde.

Mais pour vous donner l'essentiel, cela indique à Git d'établir une connexion de suivi.

Et cela signifie que pousser et tirer plus tard sera beaucoup, beaucoup, beaucoup, beaucoup plus facile à l'avenir.

Parlons donc de cela en détail.

Parce que le sujet des branches de suivi est vraiment important à comprendre.

Par défaut, les branches locales et distantes n'ont rien à voir les unes avec les autres, elles sont stockées et gérées comme des objets indépendants dans Git.

Mais dans la vie réelle, bien sûr, les branches locales et distantes ont souvent une relation entre elles.

Par exemple, une branche distante est souvent quelque chose comme une contrepartie d'une branche locale, n'est-ce pas ? Une telle relation peut être établie dans Git.

Ainsi, une branche, typiquement une branche distante, ou une branche locale, désolé, contrac.

Une autre, typiquement une branche distante.

Ainsi, dans ce petit diagramme ici, vous pouvez voir que nous avons une branche locale, elle s'appelle develop, et nous avons une branche distante sur le dépôt distant origin, qui s'appelle aussi develop, et bien sûr, je veux qu'elles aient une relation entre elles, elles sont les contreparties l'une de l'autre.

Et avec cette relation de suivi établie, lorsque je tire ou pousse plus tard, lorsque je pousse depuis ma branche locale ou tire depuis ma branche distante, je peux simplement utiliser les commandes Git vanilla, je peux utiliser git push et git pull sans aucun drapeau ou paramètre supplémentaire, car la connexion de suivi sait déjà dans le peut remplir le vide.

Ainsi, quelle branche sur quel dépôt distant je veux pousser ou tirer, par exemple, tout cela est déjà enregistré dans la connexion de suivi.

Et nous avons déjà utilisé une telle méthode pour établir cette connexion de suivi lorsque nous avons utilisé git push avec l'option u pour publier cette branche locale.

Et après cela, comme je l'ai dit, nous pouvons simplement utiliser git push sans mentionner le dépôt distant ou la branche cible ou la branche source, tout cela fonctionne.

Et cela fonctionne aussi dans l'autre sens.

Ainsi, ce que nous avons fait, c'est publier une branche locale vers un dépôt distant.

Mais nous pouvons aussi aller de l'avant et suivre ou télécharger une branche distante et l'amener vers le dépôt local, l'autre sens est aussi possible.

Et nous pouvons aussi établir une connexion de suivi comme cela.

Voyons donc ce que nous avons.

Ce serait le numéro cinq.

Et nous avons actuellement, une branche de connexion de fonctionnalités sur le dépôt distant qui n'est pas présente ici dans mes branches locales.

Ainsi, disons que quelqu'un d'autre a travaillé sur cette branche de connexion de fonctionnalités et que je veux rejoindre ce travail et travailler avec cette branche.

Ainsi, obtenons cette branche dans mes branches locales.

Et la façon de faire cela est soit d'utiliser git branch avec l'option dash dash track.

Et ce sera feature login.

Et cela provient de origin feature, login.

Ainsi, j'ai créé une branche locale appelée feature login, qui est basée sur origin feature login.

Et elles se connaissent, n'est-ce pas ? J'ai établi cette connexion de suivi, et voilà, nous l'avons maintenant localement.

Et dans une interface utilisateur graphique comme Tower, je peux voir que oui, il y a une connexion de suivi, n'est-ce pas, cette branche locale suit la branche distante.

Une autre façon de faire cela, eh bien, créons une autre branche feature, downloader, donc nous avons une autre branche locale qui n'est pas présente sur le dépôt distant.

Et nous allons la publier très rapidement.

Puis la supprimer d'ici de mes branches locales.

Bien, donc encore une fois, nous avons cette situation, je veux avoir cette branche feature downloader dans mes branches locales.

Et actuellement, elle n'est présente que sur le dépôt distant.

Ainsi, une autre façon de faire cela, au lieu de git branch dash dash track, est d'utiliser la commande git checkout.

Et encore une fois, avec l'option track, donc c'est la même chose.

Et je base cela sur origin feature, downloader.

Et en ne nommant pas une branche locale et en spécifiant simplement la branche de base distante, git utilise ce nom de branche pour le nom des branches locales, donc j'ai maintenant feature downloader ici à nouveau, même chose qu'avant, donc cela n'a pas vraiment d'importance si vous utilisez git branch dash dash track ou git checkout dash dash track, c'est juste une autre façon de faire cela.

D'accord, suivre les branches, très important, soit avec git branch, dash dash track, ou avec git checkout, dash dash track, tirer et pousser des branches.

Ainsi, une fois que vous avez correctement configuré votre connexion de suivi, tirer et pousser est vraiment simple et presque ennuyeux, en fait.

C'est pourquoi je vous suggère fortement de travailler avec les commandes que je vous ai montrées auparavant.

Lorsque vous publiez une branche locale avec git push dash, vous êtes lorsque vous suivez une branche distante de l'autre côté avec la commande git checkout dash track, car encore une fois, une fois cette connexion de suivi établie, tout ce que vous avez à faire est d'utiliser Git pull, et git push pour synchroniser vos branches, git pull pour télécharger de nouveaux commits depuis le dépôt distant probablement depuis vos collègues, et git push pour télécharger ou publier votre propre nouveau travail sur le serveur distant.

Vous n'avez pas besoin avec la configuration de la connexion de suivi, vous n'avez pas besoin de paramètres supplémentaires, vous n'avez pas besoin de spécifier le dépôt distant comme origin et la branche de base ou la branche cible et la branche source.

Juste git pull et git push suffisent.

C'est donc le vrai avantage d'utiliser ces connexions de suivi.

Prenons un autre exemple de ce que nous avons ici.

et voyons ce qui se passe.

D'accord, donc actuellement nous sommes sur la branche feature login.

Et un autre avantage d'avoir ces connexions de suivi configurées est que Git me dit si ma branche locale et la branche tract distante divergent.

Et cela signifie que prenons un autre exemple dans Tower et voyons à quoi cela ressemble.

Ainsi, cette branche feature login ici a de petits nombres ici.

Et cela signifie qu'un commit n'a pas encore été poussé.

Ainsi, la version distante de cette branche n'a pas un commit que j'ai produit localement.

Et dans l'autre sens.

Deux commits sont présents sur l'extrémité distante, probablement un collègue ou un coéquipier a fait quelques commits.

Et je ne les ai pas encore tirés.

Je ne les ai pas téléchargés.

C'est donc vraiment intéressant de rester sur la bonne voie et de comprendre comment les branches locales et distantes divergent s'il y a quelque chose que j'ai oublié de pousser ou que je n'ai pas encore poussé.

Ou s'il y a quelque chose que je dois tirer, je dois mettre à jour.

Et avec la ligne de commande avec la commande git branch, dash v, je peux obtenir les mêmes informations.

Ainsi, je vois que feature login est en avance d'un commit et en retard de deux commits. En avance signifie que j'ai un commit local qui n'a pas encore été poussé. En retard signifie que je suis en retard par rapport au dépôt distant.

Ainsi, il y a de nouveaux commits sur le dépôt distant que je n'ai pas encore tirés.

Des informations assez intéressantes pour comprendre où vous en êtes, comment vous agissez, à quel point vos données sont à jour, vous pourriez dire comment supprimer des branches, la plupart des branches ne sont pas destinées à vivre éternellement.

Et je vous encourage à faire un peu de ménage de temps en temps.

Et voici comment supprimer une branche locale.

C'est assez facile.

Ainsi, passons au numéro sept.

Et voyons ce que nous avons.

D'accord, feature uploader et main sont là.

La première chose à savoir est que vous ne pouvez pas supprimer la branche HEAD actuelle.

Ainsi, si je devais taper git branch, dash D et feature uploader, je recevrais un message d'erreur parce que, comme je l'ai dit, je peux supprimer les branches actuellement actives, c'est-à-dire actuellement HEAD.

Ainsi, d'abord, je devrais m'éloigner de cela, git switch main, rendre main ou une autre branche active.

Et ensuite, je pourrais utiliser git branch dash D, et feature uploader pour faire cela, uploader et supprimer la branche feature uploader.

Ainsi, cela a maintenant disparu, n'est-ce pas, je l'ai supprimé.

Dans certains cas, vous recevrez à nouveau un message d'erreur.

Parce que, disons que vous avez travaillé sur une branche de fonctionnalités locale pendant un certain temps, produit quelques commits, puis compris, d'accord, cela ne mène nulle part, je dois supprimer cela, vous avez produit de nouveaux commits qui ne sont présents nulle part ailleurs.

Et si vous essayez de supprimer cette branche, git dira, bien, soyez prudent, vous êtes sur le point de supprimer des données qui ne sont présentes nulle part ailleurs, ces commits n'ont pas été intégrés dans d'autres branches.

Ainsi, êtes-vous vraiment sûr et c'est là que vous devez utiliser l'option dash f force pour forcer la suppression.

Inutile de dire, je suppose que cela est une action assez destructive avec dash F pour forcer.

Ainsi, soyez prudent, vous aurez du mal à récupérer ces commits.

Vous pouvez ne pas vous inquiéter, mais cela a ses raisons pour lesquelles git vous avertit, ces commits sont présents nulle part ailleurs, êtes-vous sûr de vouloir supprimer cette branche.

Une autre chose que vous pourriez vouloir faire est de supprimer une branche distante.

Et comme vous le savez déjà, travailler avec des branches sur l'extrémité locale est différent de travailler sur l'extrémité distante.

Ainsi, c'est une commande différente, git branch.

Voyons d'abord ce que nous avons.

Ainsi, disons que nous voulons supprimer cette branche origin feature downloader ici sur le dépôt distant.

Et nous pouvons le faire en utilisant Git.

nettoyer un peu git push à nouveau, et je veux supprimer quelque chose de origin.

Le drapeau delete est utilisé ici pour feature down loader.

Et voyons, d'accord, boom, elle est partie.

Peut-être une autre chose importante à retenir est que lorsque vous supprimez une branche, peu importe si c'est une branche distante ou locale, gardez à l'esprit de vérifier si vous devriez supprimer sa branche contrepartie, écrire la branche de suivi.

Ainsi, par exemple, si vous avez supprimé une branche de fonctionnalités distante, il pourrait être logique de supprimer également sa branche de suivi locale.

De cette façon, vous vous assurez de ne pas être laissé avec beaucoup de branches obsolètes et un dépôt Git désordonné, bien sûr.

Ainsi, gardez toujours à l'esprit lorsque je supprime une branche, y a-t-il une branche contrepartie à l'autre extrémité, soit locale ou distante ? Et devrais-je la supprimer aussi ? Peut-être.

D'accord, supprimer sur le dépôt distant avec git push, et dash, dash, delete.

Fusionner des branches est un sujet assez intéressant.

La fusion est probablement le moyen le plus courant d'intégrer des changements.

Ainsi, essentiellement, vous apportez de nouveaux commits d'une autre branche dans votre branche HEAD actuelle.

C'est toujours la direction, n'est-ce pas ? Vous intégrer dans votre branche HEAD locale actuelle depuis une autre branche.

Et la fusion dans la plupart des cas est très facile dans Git et très simple, différente des autres systèmes de contrôle de version.

Ainsi, c'est l'une des raisons pour lesquelles il est si populaire.

Et essentiellement, cela nécessite simplement deux étapes.

Ainsi, d'abord, vous devez rendre active la branche que vous voulez recevoir les changements, celle qui devrait recevoir les changements, puis exécuter la commande de fusion avec le nom de la branche qui a les changements désirés.

Voyons ce que nous avons ici dans notre scénario d'exemple.

D'accord, donc en ce moment, Maine a un nouveau commit qui est celui-ci, titre de la page d'erreur corrigé.

Et uploader a aussi un commit différent, clarifier la règle de fond CSS.

Ainsi, ils ont divergé.

Et disons que je veux intégrer ce commit ici ou ces changements, les nouveaux commits sur feature upload dans main, n'est-ce pas, je veux apporter les nouveaux changements dans la branche main, alors je peux simplement passer à main, rendre main active, et ensuite simplement taper Git merge feature, qu'était-ce uploader ? Et voilà, j'obtiens un éditeur avec un pourquoi est-ce que, parce que la fusion produit le plus souvent, pas toujours, un commit de fusion, n'est-ce pas ? Pensez à cela comme un nœud qui combine ou qui connecte deux branches.

Et c'est un nouveau commit.

Ainsi, je peux fournir un nouveau message de commit.

Et je vais avec ce que Git fournit ici comme standard merge branch feature uploader.

Fermez simplement cela.

Et voyons ce qui s'est passé.

sur le mur principal, je viens de combiner ces deux branches et j'ai tous les changements ici des deux branches.

Ainsi, voici à quoi ressemble le résultat final.

Comme je l'ai dit, il y a ce commit de fusion ici qui combine les changements des deux branches.

Et il y a une autre façon d'intégrer les changements, et c'est le rebasing, donc c'est juste une alternative pour intégrer les commits d'une branche dans une autre.

Et il est très important de souligner que ce n'est pas mieux ou pire, ce n'est pas la version pro et la fusion est la version débutant, c'est simplement différent.

Si et quand vous utilisez le rebase, dépend principalement de vos préférences personnelles et des conventions de votre équipe et de la situation.

Ainsi, certaines équipes adorent le rebase, d'autres préfèrent la fusion, et certaines le font dans certains cas et pas dans d'autres.

Ainsi, ce n'est pas une question de mieux ou de pire, c'est important à comprendre.

Comparons donc la fusion et le rebase.

Ainsi, vous comprenez quelle est la différence.

Ainsi, voici la situation de départ, nous avons deux branches, nous avons la branche a et la branche B, et les deux ont des changements divergents, des changements différents.

Ainsi, nous avons quelques commits ici et un commit ici.

Et ils ont été bifurqués à ce point ici.

Maintenant, avec la fusion, vous avez déjà vu que nous recevrions ce commit de fusion à la fin, ce point de fusion ou ce nœud qui combine ces deux commits, en utilisant le rebase.

D'autre part, le résultat final sera assez différent.

Surtout parce qu'il n'y a pas de commit de fusion séparé qui sera créé, cette grande différence.

En utilisant le rebase.

Il apparaît comme si l'historique de développement s'était déroulé en ligne droite.

Il n'y a plus cette bifurcation, cela se produit, ou cela ressemble à une ligne droite.

Et cela a ses avantages et ses inconvénients.

Ainsi, c'est le résultat et la grande différence.

Et ensuite, le processus réel est assez simple.

Mais faisons cela en pratique.

C'est le cas numéro neuf.

Et voyons ce que nous avons.

D'accord, donc une situation assez similaire à avant, sur feature uploader, j'ai deux commits ici qui ne sont présents nulle part ailleurs.

Et sur Main, j'ai celui-ci qui n'est présent nulle part ailleurs.

Et disons que j'aimerais intégrer les changements de Maine dans ma branche feature uploader, n'est-ce pas.

Ainsi, la première étape serait de passer à feature uploader pour en faire la branche HEAD parce que, comme avec la fusion, je suis toujours en train d'intégrer dans ma branche HEAD.

Bien, la branche HEAD est celle qui est manipulée.

Je suis déjà sur feature uploader.

Ainsi, rien à faire ici.

Mais la deuxième étape est Git rebase.

Et je veux rebase sur Main.

Et c'était déjà tout.

Voyons ce qui s'est passé.

Maintenant, vous pouvez voir ce commit, titre de la page d'erreur corrigé, qui était sur Main, est maintenant aussi présent ici sur uploader.

Et comme vous pouvez le voir, il n'y a pas cette bifurcation, ce nœud de fusion, pas de commit de fusion.

Cela ressemble à une ligne droite.

Et c'est la grande différence entre la fusion et le rebase.

Encore une fois, si vous utilisez une interface utilisateur graphique comme Tower, vous pouvez simplement glisser-déposer pour fusionner ou si vous maintenez la touche Alt enfoncée, cela devient rebase.

Ainsi, ces actions sont assez simples dans une interface utilisateur graphique.

D'accord, et donc c'est le rebasing à nouveau, et le dernier cas ou la dernière action, comparer les branches, parfois c'est assez utile de comparer deux branches.

Ainsi, par exemple, avant de décider d'intégrer ou de supprimer une branche, vous voulez voir comment elle diffère d'une autre branche.

Contient-elle de nouveaux commits ? Ou non ? Ai-je encore besoin de ceux-ci ? Quelle est la différence ? Faisons cela en pratique.

Et voyons ce que nous avons.

Ainsi, une situation similaire à celle d'avant, feature uploader et main, ils ont divergé, ils ont des commits différents.

Et comparons cela et voyons ce qui est réellement différent entre eux.

Ainsi, je peux taper git log main double point feature uploader.

Et cela me montre quels commits sont dans notre branche feature uploader, mais pas dans notre branche main.

Et ainsi, je peux voir, d'accord, ces deux commits sont ici, mais pas ici.

Et cela signifierait aussi, bien sûr, si je les intégrais dans main, ces deux commits seraient inclus dans l'intégration.

Ainsi, je peux comprendre la différence entre ceux-ci.

Si je veux voir quelle est la différence entre une branche locale et une branche distante, je peux aussi faire la même chose, en fait.

Ainsi, comparons mon Maine local avec le Maine origin.

Et le processus est assez similaire.

git log, Maine.

Commençons par origin Maine, et Maine.

Et je peux voir, d'accord, j'ai un commit actuellement dans mon main local qui n'est pas présent dans ma branche distante origin main.

Ainsi, je sais.

D'accord, si je pousse maintenant, je téléchargerais ce commit ici parce qu'il n'est pas présent là.

D'accord.

Je pense que c'est tout pour aujourd'hui.

Pour vous aider à vous souvenir de ce que vous avez appris, j'ai préparé une petite fiche mémo sur ces sujets, sur toutes les différentes commandes que vous pouvez utiliser en ce qui concerne le travail avec les branches.

Sautez simplement sur Bitly et obtenez la fiche mémo des branches et téléchargez-la gratuitement.

Cela sera utile dans votre travail quotidien, j'en suis sûr.

Et vous pouvez télécharger la fiche mémo gratuitement comme vous le souhaitez.

J'espère qu'il y a un peu de nouvelles informations pour vous ici dans cet atelier et dans la fiche mémo.

Amusez-vous à créer, supprimer, renommer, suivre, pousser, tirer, comparer les branches et travailler avec Git.

Merci pour votre attention.

Prenez soin de vous.