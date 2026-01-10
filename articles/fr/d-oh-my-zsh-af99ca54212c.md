---
title: d’Oh My Zsh
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-03-23T06:17:23.000Z'
originalURL: https://freecodecamp.org/news/d-oh-my-zsh-af99ca54212c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EHjw8IcEy7KWymemWXXsCg.png
tags:
- name: coding
  slug: coding
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: d’Oh My Zsh
seo_desc: 'By Robby Russell

  How I unexpectedly built a monster of an open source project

  This wouldn’t be my first foray into open source software; nor my last.

  It was the summer of 2009. I found myself helping a coworker debug something in
  their terminal. As I...'
---

Par Robby Russell

#### Comment j'ai involontairement construit un monstre de projet open source

Ce ne serait pas ma première incursion dans les logiciels open source ; ni ma dernière.

C'était l'été 2009. Je me suis retrouvé à aider un collègue à déboguer quelque chose dans son terminal. Alors que j'essayais de taper quelques lignes de commande, j'ai remarqué que l'invite ne répondait pas aux raccourcis auxquels mon cerveau s'était habitué. Frustré, je m'exclamai, _"quand vas-tu enfin passer à Zsh ?!"_

(oui, j'étais ce type de collègue ennuyeux qui pointerait constamment que X était mieux que Y quand l'occasion se présentait. Avec le recul, je ne sais pas comment ils m'ont supporté... mais entre vous et moi, j'avais raison.)

> "quand vas-tu enfin passer à Zsh ?!"

À ce moment-là, j'utilisais Zsh quotidiennement depuis un peu plus de trois ans.

Quelques-uns de mes [amis #caboose](https://www.flickr.com/photos/19932288@N00/177403465) ont partagé quelques-unes de leurs configurations .zshrc dans notre canal IRC. Après quelques années, mon fichier .zshrc est devenu un nid de rat emmêlé. Honnêtement, je ne savais pas ce que ~30 % de la configuration faisait. Je faisais assez confiance à mes amis pour l'utiliser quand même. Ce que je savais, c'est que j'avais quelques détails sur les branches et le statut git, une coloration syntaxique pour quelques outils (c'est-à-dire, grep), une complétion automatique des chemins de fichiers sur les connexions SSH, et une poignée de raccourcis pour [Rake](https://github.com/ruby/rake) et [Capistrano](http://capistranorb.com/). Travailler sur une machine avec un profil Bash par défaut semblait remarquablement archaïque ; j'étais devenu dépendant de ces raccourcis.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oZ9acQ0aYPD10zmZDqEmQg.jpeg)
_Corinne est une développeuse front-end chez Planet Argon_

Quelques collègues étaient heureux de copier/coller le fichier .zshrc que j'ai partagé et de commencer à l'utiliser. D'autres ne l'ont pas fait parce qu'ils savaient que je ne savais pas ce que certaines parties faisaient. C'est juste.

Après quelques tentatives pour les convertir sans succès, j'ai opté pour une approche différente.

D'abord, j'ai réorganisé ma configuration .zshrc, ce qui impliquait de la diviser en une collection de fichiers plus petits. Mon raisonnement ici était que cela a) m'aiderait à mieux comprendre comment tous ces morceaux fonctionnaient tout en b) aidant à éduquer mes pairs lorsqu'ils liraient le code.

Devant leur prochaine question, _"comment faire pour que cela fonctionne sur ma machine ?"_, j'ai rédigé les premières [instructions d'installation](https://github.com/robbyrussell/oh-my-zsh/blob/5da20b9dddb1f7a9110675ded5df59c4c3ed1b83/README.textile).

Plus important encore, j'ai regroupé tous ces fichiers dans un tout nouveau dépôt git. Je pensais que si je le mettais sur Github, mes pairs pourraient collaborer avec moi pour l'améliorer.

Bien que ce ne soit pas un énorme bond en avant, c'était un pas au-dessus d'inviter les gens à copier/coller un fichier texte depuis [Pastie](http://pastie.org/).

Le 28 août 2009, [Oh My Zsh est né](https://github.com/robbyrussell/oh-my-zsh/tree/5da20b9dddb1f7a9110675ded5df59c4c3ed1b83).

![Image](https://cdn-media-1.freecodecamp.org/images/1*6I5hz65oHTa234aco8uD2g.jpeg)
_Une des premières versions publiques de Oh My Zsh. ([voir sur github](https://github.com/robbyrussell/oh-my-zsh/tree/5da20b9dddb1f7a9110675ded5df59c4c3ed1b83" rel="noopener" target="_blank" title="))_

#### ...mais, attendez une minute !! _Où sont les thèmes ? Où sont les plugins ? Les scripts d'installation ? Le logo ?_

Cela peut surprendre la plupart des utilisateurs de Oh My Zsh, mais aucune de ces fonctionnalités n'avait été envisagée. Mon objectif avec le projet n'était _pas_ de construire un framework pour maintenir les configurations Zsh mais de partager ma propre configuration avec mes collègues pour qu'ils utilisent Zsh.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pMhWn5hhf5-fB5olMP1Ung.jpeg)
_Patrick (à gauche) et Travis (à droite)_

En l'espace d'une journée après l'avoir partagé avec tous mes collègues, tout le monde chez [Planet Argon](http://www.planetargon.com/) était passé de Bash à Zsh.

**_Victoire ! ... ou du moins, c'est ce que je pensais._**

La première demande de fonctionnalité est arrivée le lendemain.

> "Comment puis-je personnaliser _MON_ invite ?"

Deux collègues m'ont demandé comment ils pouvaient personnaliser leur invite. Ils voulaient changer les couleurs et les informations affichées.

_Quoi ?! Mon invite n'était pas assez convaincante pour eux ?_ Si pointilleux. ;-)

Je leur ai indiqué le fichier prompt.zsh et leur ai dit qu'ils pouvaient le modifier.

Rapidement, cela est devenu un problème car ils avaient maintenant leur propre version de ce fichier. Par conséquent, cela ajouterait une certaine complexité si nous voulions tous partager certains de nos raccourcis et fonctionnalités, car nous aurions des conflits à gérer.

Hmm...

Ainsi, un jour après avoir annoncé Oh My Zsh sur mon blog, j'ai [commencé à introduire le concept initial des thèmes](https://github.com/robbyrussell/oh-my-zsh/commit/2c9f74b5c3f6910e7c66601008e9ddd0444b70c7).

![Image](https://cdn-media-1.freecodecamp.org/images/1*TvoQqeoh63DzFZYPgq9cBg.jpeg)
_Présentation du thème 'famous' robbyrussell au monde._

Pendant ce temps, j'ai reçu ma première pull-request externe de Geoff Garside pour ajouter [quelques alias pour TextMate](https://github.com/robbyrussell/oh-my-zsh/commit/7a7b0bc7f57ffabaa8e409975be4efe83e6eb924). (Remarquez comment cela a été directement ajouté dans un fichier aliases.zsh catch-all)

Un jour plus tard, [un autre thème](https://github.com/robbyrussell/oh-my-zsh/commit/f704193fd2732207c158aa3413e2ef9634e7b17f) a été envoyé. Groovy, j'ai [mieux fait d'ajouter un lien sur le README](https://github.com/robbyrussell/oh-my-zsh/commit/ebc6ce25aa2aa2c8957724b916711ceee3bb15ce) pour voir quelques [captures d'écran sur le wiki](https://github.com/robbyrussell/oh-my-zsh/wiki/themes).

En l'espace d'un mois, nous avions une douzaine de thèmes contribués au projet.

Cela est devenu un aspect vraiment populaire de Oh My Zsh et nous avons dû commencer à freiner l'acceptation des thèmes une fois que nous avons dépassé 100. (nous en sommes actuellement à ~140 et nous acceptons _rarement_ de nouveaux)

### Simplifier l'installation avec un installeur

Il m'est venu à l'esprit que l'installation initiale nécessitait que les gens exécutent une poignée de commandes. Plutôt que de demander aux gens de retaper et/ou de copier/coller une poignée de commandes, j'ai pensé qu'il serait plus efficace pour les deux parties (car cela réduirait les questions que mes collègues auraient lorsqu'ils rencontreraient un problème et/ou sauteraient une étape).

Un installeur est né.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DQHTqwRaONa61MXpa3ap5A.jpeg)
_Le script d'installation initial ([voir sur github](https://github.com/robbyrussell/oh-my-zsh/commit/71769107dbff230ec7607368f50f9ff93b88b581" rel="noopener" target="_blank" title="))_

Mes premières pensées étaient de faire gagner quelques étapes aux gens en automatisant l'installeur. Si tout le monde exécutait les mêmes commandes, alors nous pourrions réduire les erreurs humaines (sauter une commande, fautes de frappe, etc.). Je voulais aussi être attentif au fait que les gens pourraient passer de Bash ou d'une configuration Zsh existante bricolée. Pour les aider à un éventuel retour à l'ancien shell, nous avons fait une sauvegarde de leur fichier de configuration original. Enfin, nous avons changé leur shell par défaut pour Zsh.

> "Hourra ! Oh My Zsh a été installé."

Oh, oui. Comment les gens pourront-ils rester à jour avec les nouveaux changements du projet ?

Le lendemain, j'ai ajouté un script de mise à jour qui se rend dans le répertoire Oh My Zsh, récupère les mises à jour depuis le dépôt git, et vous ramène à votre répertoire de travail précédent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MT9v0xO25eQuhTtUrg1KAA.jpeg)
_Le script de mise à jour initial ([voir sur github](https://github.com/robbyrussell/oh-my-zsh/blob/1ec8a8848e5fa8f733af92f2c09387719e57e0d5/tools/upgrade.sh" rel="noopener" target="_blank" title="))_

Loin de la science des fusées.

Environ trois semaines plus tard, il est devenu évident que mes collègues ne suivaient pas manuellement toutes les nouvelles mises à jour du projet. Plutôt que de leur rappeler de le faire de temps en temps, j'ai ajouté une fonctionnalité qui inviterait périodiquement l'utilisateur à vérifier les mises à jour.

Jusqu'à ce point, cela semblait être le morceau de code le plus compliqué du projet. Je souhaite pouvoir me souvenir de qui m'a donné la grande idée d'utiliser une valeur d'époque ici.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8cD2EDIWdhNncwa_Q4k1VA.jpeg)
_Le premier auto-mise à jour ([voir sur github](https://github.com/robbyrussell/oh-my-zsh/commit/700a3f0badf89fc9bb5a8f54b5fd2e14aed2823d" rel="noopener" target="_blank" title="))_

À mon avis, c'était aussi le tournant pour le projet.

Bien qu'un petit nombre de personnes l'utilisaient, cette fonctionnalité permettrait à presque tous les utilisateurs de rester à jour sur les changements du projet et, plus important encore, de rester engagés. Lorsqu'ils exécuteraient la mise à jour, ils verraient une liste des fichiers modifiés et cela, subtilement, les introduirait à de nouvelles fonctionnalités... à la manière de, _"Je me demande à quoi ressemble ce thème..."_

Malheureusement, tout le monde n'a pas été fan.

Malgré quelques opposants vocaux au fil des ans, j'ai maintenu ma décision de garder cela comme paramètre par défaut.

En 2012, nous avons apporté un changement pour réduire la fréquence des invites de mise à jour automatique de 50 %.

La mise à jour automatique nous a permis de livrer de nouvelles fonctionnalités, des améliorations de performance et des corrections de bugs sans dépendre de tout le monde pour le faire manuellement. Je suis convaincu que cette fonctionnalité a aidé à maintenir la communauté engagée.

#### Ce Muffin a Besoin de Bonbons

Alors que le projet attirait beaucoup de thèmes, j'ai vraiment senti que le projet pourrait bénéficier d'une identité visuelle.

**Ma solution ? L'art ASCII.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*k9U-KOrPxao4RVA7Vgjm8A.jpeg)
_Je n'ai aucune idée de ce qui a inspiré le message de commit git._

Mon raisonnement ici était... bien sûr, vous obtenez un tas de raccourcis utiles et de thèmes lorsque vous commencez à utiliser Oh My Zsh, mais j'ai vraiment senti que la première impression après l'exécution de l'installeur était une opportunité de ravir les nouveaux utilisateurs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5pGRf0bye9kbfyZN8UZEMg.jpeg)

Des paillettes de bonbons sur le muffin... pour ainsi dire. (Je n'ai aucun souvenir de pourquoi j'ai écrit ce message de commit à l'époque. La référence m'échappe.)

![Image](https://cdn-media-1.freecodecamp.org/images/1*QrPTCyo_olmyjhxtTjO3fA.jpeg)
_Ce que le script de mise à jour affiche actuellement._

Les gens me demandent depuis un certain temps d'imprimer des t-shirts avec l'art ASCII. (nous le ferons probablement cet été — [suivez-nous sur twitter](https://twitter.com/ohmyzsh))

![Image](https://cdn-media-1.freecodecamp.org/images/1*k9eGe-BEObD_Gp40MvaN-A.jpeg)
_Becca Ward a conçu le logo_

#### Plugins

Dix mois après avoir ouvert le projet, les utilisateurs avaient commencé à demander la possibilité de ne pas tout charger. Par exemple, un développeur Python n'aurait peut-être pas besoin des alias liés à Rake et Capistrano comme le ferait un développeur Ruby.

Ainsi, nous avons [implémenté un système de plugins de base](https://github.com/robbyrussell/oh-my-zsh/commit/3cf9ab722e7c0829727f548c7d05a0d96055f707) qui permettrait aux gens de décider lesquels charger à l'initialisation en changeant une valeur dans .zshrc.

Lors de la sortie de cette fonctionnalité, il y avait cinq plugins inclus.

En quelques mois, j'ai commencé à recevoir des pull requests pour de nouvelles idées de plugins.

En l'espace d'un an, [j'avais accepté plus de 40 plugins](https://github.com/robbyrussell/oh-my-zsh/tree/9b63a03bcfb7a6c34281d7d905575c5647e9c8d2/plugins).

En deux ans ? [Plus de 70 plugins](https://github.com/robbyrussell/oh-my-zsh/tree/8b69c7f6a0c80c1c53505e17d356387b83e18efc/plugins).

Actuellement, nous avons des plugins pour adb, ant, apache2-macports, archlinux, autoenv, autojump, autopep8, aws, battery, bbedit, bgnotify, boot2docker, bower, branch, brew, brew-cask, bundler, bwana, cabal, cake, cakephp3, capistrano, cask, catimg, celery, chruby, chucknorris, cloudapp, codeclimate, coffee, colemak, colored-man-pages, colorize, command-not-found, common-aliases, compleat, composer, copydir, copyfile, cp, cpanm, debian, dircycle, dirhistory, dirpersist, django, dnf, docker, docker-compose, emacs, ember-cli, emoji, emoji-clock, emotty, encode64, extract, fabric, fancy-ctrl-z, fasd, fastfile, fbterm, fedora, forklift, frontend-search, gas, gem, git, git-extras, git-flow, git-flow-avh, git-hubflow, git-prompt, git-remote-branch, gitfast, github, gitignore, glassfish, gnu-utils, go, golang, gpg-agent, gradle, grails, grunt, gulp, heroku, history, history-substring-search, httpie, iwhois, jake-node, jhbuild, jira, jruby, jsontools, jump, kate, kitchen, knife, knife_ssh, laravel, laravel4, laravel5, last-working-dir, lein, lighthouse, lol, macports, man, marked2, mercurial, meteor, mix, mix-fast, mosh, mvn, mysql-macports, n98-magerun, nanoc, nmap, node, npm, nvm, nyan, osx, pass, paver, pep8, per-directory-history, perl, phing, pip, pj, pod, postgres, pow, powder, powify, profiles, pyenv, pylint, python, rails, rake, rake-fast, rand-quote, rbenv, rbfu, rebar, redis-cli, repo, rsync, ruby, rvm, safe-paste, sbt, scala, scd, screen, scw, sfffe, singlechar, spring, sprunge, ssh-agent, stack, sublime, sudo, supervisor, suse, svn, svn-fast-info, symfony, symfony2, systemadmin, systemd, taskwarrior, terminalapp, terminitor, terraform, textastic, textmate, thefuck, themes, thor, tmux, tmux-cssh, tmuxinator, torrent, tugboat, ubuntu, urltools, vagrant, vault, vi-mode, vim-interaction, virtualenv, virtualenvwrapper, vundle, wakeonlan, wd, web-search, wp-cli, xcode, yii, yii2, yum, z, zeus, zsh-navigation-tools, zsh_reload.

Au total... [214 plugins](https://github.com/robbyrussell/oh-my-zsh/tree/master/plugins). Je dois admettre que tout le monde n'a pas été impressionné par cela.

Je suis d'accord pour dire que cela pourrait être _considérablement_ amélioré.

Les quelques fois où j'y ai pensé, j'ai trouvé les approches proposées trop compliquées pour les gens qui ne sont pas encore familiers et/ou à l'aise avec le terminal. Peut-être une approche plus sophistiquée pour la version 2 du framework. (plus sur cela plus tard)

Il y a aussi eu une partie de moi qui a senti que ce projet ne serait d'intérêt pour les gens que pendant quelques années. À mesure que les utilisateurs gagneraient en expérience et/ou que la technologie évoluerait, le framework serait laissé de côté par de nouveaux projets brillants qui résoudraient les problèmes bien mieux que nous.

Je n'aurais jamais pensé que Oh My Zsh continuerait à prendre de l'ampleur près de sept ans plus tard.

Nous sommes le 22 mars 2016 et le [dépôt shell le plus tendance sur Github est](https://github.com/trending/bash)? (trouvez cela amusant que l'URL lise, "bash"... euh)

![Image](https://cdn-media-1.freecodecamp.org/images/1*nKEDfA4i1F7JUtmV7LWAwg.jpeg)
_"/les (40 nouvelles) étoiles semblent très différentes aujourd'hui.../"

D'où viennent tous ces nouveaux utilisateurs ? Je vous aime, les gens !

Bien que j'aie beaucoup d'histoires à partager (et que j'ai l'intention d'écrire plus sur ce sujet), je voulais m'adresser à ceux qui débattent de l'idée d'ouvrir un projet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FYWvq5YZRXLsLWamTXvhAQ.jpeg)
_Brian Middleton_

#### Huit Considérations Pour Votre Projet Open Source

**Ne commencez pas avec un objectif excessivement ambitieux.** Commencez votre projet avec un objectif simple et réalisable. À quoi ressemble le succès ? Dans mon scénario, je voulais que 1-2 personnes de mon équipe utilisent mes scripts. Le projet a été un succès en moins de 24 heures.

Tout le reste depuis a été un bonus.

**N'essayez pas de prévoir tous les scénarios.** Si je m'étais attardé sur certains détails à long terme pour le projet, Oh My Zsh n'aurait jamais vu le jour. Presque tout ce qui a été ajouté au projet est venu organiquement après la sortie initiale.

L'un des beaux aspects d'un projet open source est que votre base d'utilisateurs peut aider à le façonner.

**N'essayez pas de le rendre parfait.** Vous inquiéter de la façon dont les autres vont réagir à votre code ne devrait pas être votre plus grande préoccupation. Est-ce que cela fonctionne ? Comment se sentent-ils lorsqu'ils interagissent avec lui devrait être une préoccupation plus grande. Dans mon cas, j'ai eu quelques excellents contributeurs au fil des ans qui ont aidé à nettoyer et à améliorer la qualité du code que j'avais initialement publié.

Rarement quelqu'un a dit quelque chose de critique sur mon ancien code — peut-être qu'ils auraient dû, cependant. ;-)

**N'essayez pas d'être tout pour tout le monde.** Il y a eu quelques moments dans l'histoire du projet où nous avons atteint une croix des chemins. En particulier, il y a eu un moment où une reconstruction massive a été proposée, ce qui m'enthousiasmait beaucoup jusqu'à ce que je puisse comprendre certains des changements.

[**Proposition pour Simplifier OH-MY-ZSH · Problème #377 · robbyrussell/oh-my-zsh**](https://github.com/robbyrussell/oh-my-zsh/issues/377#issuecomment-4204013)

En conséquence, un fork a été rebaptisé et nous avons convenu de suivre des chemins différents. Tout le monde n'a pas été heureux avec ma décision ici, mais c'est pendant cette période qu'il est devenu clair (pour moi) que je voulais concentrer mon attention sur les gens qui n'étaient pas trop à l'aise avec le terminal et/ou git.

**Ne cessez pas de remercier les contributeurs.** Si quelqu'un aide votre projet, faites-lui savoir à quel point vous appréciez ses efforts. Je ne peux pas assez remercier mes contributeurs. L'une de mes plus grandes autocritiques liées à ce projet est que je n'ai pas été assez constant dans l'expression de ma gratitude.

Il y a [910 personnes du monde entier](https://github.com/robbyrussell/oh-my-zsh/network/members) qui ont leur code accepté dans la branche principale de Oh My Zsh au moment de l'écriture de ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/1*08x0ukNsdXSmR3yvtn9foA.png)
_C'est une liste si longue que Github ne peut même pas tous les lister._

En particulier, merci à **vous**. (vous savez qui vous êtes)

**N'oubliez pas la documentation.** Au fil des ans, la documentation des plugins et des fonctionnalités a été vitale pour aider à informer les utilisateurs sur la façon de tirer parti du framework.

Je souhaite que nous ayons adopté cette convention plusieurs années plus tôt.

Le fichier README sera le plus vu... alors faites-en sorte qu'il compte. Dans mon cas, j'ai choisi d'introduire les gens à ma personnalité et à mon humour sec.

Honnêtement, voir des tweets comme celui-ci signifie le monde pour moi.

**N'oubliez pas le reste de votre vie.** Encore une fois, je n'aurais jamais anticipé que le projet deviendrait ce qu'il est aujourd'hui.

Êtes-vous familier avec l'anecdote sur [la grenouille dans une casserole d'eau bouillante](https://en.wikipedia.org/wiki/Boiling_frog) ?

Cela m'a pris 3-4 ans, trop, pour enfin faire entrer une autre personne pour aider à maintenir le projet. Je continuais à penser que je pourrais rattraper toutes les pull requests et les problèmes ouverts. Ce que je me disais, c'est que les gens qui savent comment fork le projet peuvent faire leurs changements souhaités et travailler à partir de cela, donc examiner et approuver les pull requests est un plus plutôt qu'un besoin.

En pratique, c'est quelque part entre les deux. Je me sens un peu mal pour les anciennes pull requests qui traînent, mais je ne garde pas non plus Oh My Zsh comme l'un des projets les plus importants sur ma liste.

En dehors de Oh My Zsh, je dirige [une agence de 19 personnes](http://www.planetargon.com/), je joue de la guitare dans un groupe de post-rock instrumental, je siège au conseil d'administration d'une association locale pour sans-abri, je voyage beaucoup avec mon appareil photo, je fais de la moto, du vélo, et j'essaie de maintenir une vie sociale avec mes amis. Oh My Zsh s'insère quelque part parmi tout cela.

Ce n'est pas en haut de ma liste de priorités. Ce n'est pas en bas. C'est quelque part entre les deux. Ce n'est pas une excuse pour ne pas pouvoir suivre la communauté, mais plutôt un rappel que ces autres choses devraient aussi compter pour vous, si vous êtes sur le point de commencer votre propre projet.

#### (J'écrirai plus sur le sujet de diriger un projet open source avec des mainteneurs dans une autre histoire... ❤ [me suivez-vous ?](https://medium.com/@robbyrussell) ❤)

**N'oubliez pas de vous amuser.** Lorsque vous commencez votre projet, décidez si cela va être un travail sérieux ou un temps de jeu. Peut-être que cela peut être quelque part entre les deux.

Oh My Zsh a toujours été un projet de temps de jeu pour moi.

Savoir que l'un de mes projets ludiques a été et continue d'être apprécié par les gens est un sentiment merveilleux.

Certains pourraient l'appeler un _projet de passion_. **Moi, je l'appelle _temps de jeu_.**

#### Intéressé par mon projet open source amusant ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*EHjw8IcEy7KWymemWXXsCg.png)

Vous pouvez en apprendre plus sur [http://ohmyz.sh](http://ohmyz.sh/).

[Robby Russell](https://www.planetargon.com/about/robby-russell) est le VP de l'Ingénierie et un partenaire de [Planet Argon](https://www.planetargon.com/), une [firme de développement Ruby on Rails](https://www.planetargon.com/services/ruby-on-rails-development) basée à Portland, Oregon.

### Si vous avez aimé cet article, veuillez le recommander et/ou le partager. ❤

Vous utilisez déjà Oh My Zsh ? J'adorerais savoir comment vous en avez entendu parler.