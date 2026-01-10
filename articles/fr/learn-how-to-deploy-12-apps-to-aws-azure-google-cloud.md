---
title: Apprenez à déployer 12 applications sur AWS, Azure et Google Cloud
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-07-29T15:52:57.000Z'
originalURL: https://freecodecamp.org/news/learn-how-to-deploy-12-apps-to-aws-azure-google-cloud
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/12-apps.png
tags:
- name: Docker
  slug: docker
- name: youtube
  slug: youtube
seo_title: Apprenez à déployer 12 applications sur AWS, Azure et Google Cloud
seo_desc: 'Dockerizing an app makes it simpler to deploy.

  We just published a full course on the freeCodeCamp.org YouTube channel that will
  teach you how to deploy 12 apps to 3 popular hosting services.

  Scalable Scripts developed this course. They create course...'
---

Dockeriser une application la rend plus simple à déployer.

Nous venons de publier un cours complet sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à déployer 12 applications sur 3 services d'hébergement populaires.

Scalable Scripts a développé ce cours. Ils créent des cours sur toutes sortes de langages et de frameworks sur leur chaîne YouTube.

Dans ce cours, vous apprendrez à créer et à dockeriser les types d'applications suivants :

* Application React
* Application NodeJS
* Application VueJS
* Application NestJS
* Application Angular
* Application Golang
* Application Svelte
* Application Django
* Application Laravel
* Application .NET Core
* Application Spring Boot avec Kotlin
* Application Deno

Vous apprendrez ensuite à déployer ces applications sur :

* AWS
* Azure
* Google Cloud

Regardez le cours complet de 2 heures ci-dessous ou sur la [chaîne YouTube freeCodeCamp.org](https://youtu.be/-ANCcFQBk6I).

%[https://youtu.be/-ANCcFQBk6I]

## Transcription

(autotraduit)

Ce cours vous apprendra à déployer 10 des types d'applications les plus populaires sur les trois principaux fournisseurs de cloud.

Donc, si vous voulez apprendre à déployer un type spécifique d'application, ce cours est fait pour vous.

Dans cette vidéo, nous allons créer un conteneur Docker pour chacune de ces applications.

Et nous allons déployer le conteneur sur AWS et Google Cloud, le résultat sera le même pour toutes les applications.

Donc, consultez les timestamps de cette vidéo pour sélectionner votre langage ou framework préféré, puis sélectionnez votre plateforme de déploiement préférée.

Alors, commençons à déployer ces applications.

Dans cette vidéo, nous allons créer un conteneur de production pour cette application React.

Et nous allons la déployer sur Google Cloud, AWS et Azure.

Alors, commençons.

Tout d'abord, je vais créer un fichier appelé Dockerfile.

Et, bien sûr, assurez-vous d'avoir installé Docker sur votre machine.

Et dans le Dockerfile, nous devons commencer par le conteneur lui-même, quel type de conteneur sera-t-il, et nous commencerons par ce conteneur qui sera un conteneur node.

Et ici, je vais spécifier la version de node, je vais choisir la 15.4.

Et je vais le nommer build.

Je vais expliquer plus tard pourquoi je l'ai nommé ainsi.

Alors, commençons avec ce conteneur, nous devons spécifier le répertoire de travail.

Je vais l'appeler app.

Donc, vous pouvez mettre ce que vous voulez ici.

Et copions le package.json dans ce répertoire de travail.

Donc, cela signifie que nous devons copier ce package.json, donc le répertoire de travail ici.

Donc, beaucoup d'étoiles ici.

L'étoile signifie que nous pouvons mettre n'importe quoi entre package et JSON.

Cela signifie que nous allons copier package.json et aussi package-lock.json.

Donc, nous avons copié ces fichiers, puis nous devons exécuter npm install.

C'est assez explicite.

Donc, nous avons NPM déjà installé dans le conteneur parce que nous utilisons un environnement node ici.

C'est pourquoi c'est important.

Après avoir installé tous les packages, nous devons copier à nouveau tous les fichiers dans le répertoire de travail.

Donc, cela signifie que tous les autres fichiers doivent être copiés dans le répertoire de travail.

Et ensuite, nous devons construire le conteneur.

Donc, exécutez NPM run build.

Donc, si nous allons dans package.json, nous avons un script de build ici.

Et ce que cela va faire, c'est créer un dossier de distribution, donc exécutons cette commande NPM run build.

Donc, nous pouvons visualiser ce dossier.

Donc, nous avons un dossier build ici qui contiendra tous les fichiers nécessaires et nous avons terminé la première étape.

Donc, ce sera une construction Docker multi-étapes, ce qui signifie que nous aurons une autre étape, donc nous avons tous ces fichiers à l'intérieur de ce conteneur Docker, mais nous n'avons besoin que du dossier build, donc il n'est pas nécessaire de garder tous les autres, nous pouvons avoir un conteneur plus petit.

Et pour faire cela, nous devons ajouter un autre from ici et ce conteneur aura nginx, donc je vais prendre la dernière version.

Donc, si je veux la dernière version, je vais simplement ajouter nginx ici, ou je vais ajouter la version 1.19.

Et dans ce conteneur nginx, nous devons ajouter ici, je vais créer un autre répertoire nginx.

Et ici, je vais créer un fichier nginx.conf.

Et ici, je vais coller cette configuration, donc il y a beaucoup de texte.

Mais vous pouvez copier ce fichier dans le code source dans la description de la vidéo.

Donc, cela est nécessaire pour accéder directement au fichier index.html ici.

Donc, le build est index.html et tous les fichiers JavaScript dont nous avons besoin.

Donc, nous devons copier ce fichier dans ce conteneur nginx.

Donc, copiez nginx nginx.conf vers etc nginx nginx.conf.

Donc, nous avons ajouté notre propre configuration nginx, puis la deuxième étape est d'ajouter le dossier build à nginx.

html.

Donc, c'est pourquoi nous l'avons nommé build ici.

Donc, ici, je vais copier depuis build.

Donc, c'est une commande depuis ce conteneur ici, qui a ce dossier build, copiera app build, nous avons spécifié le répertoire de travail comme étant app.

Donc, il est logique que le dossier build soit app build.

Et nous devons copier cela depuis usr share nginx.

html.

Et c'est tout.

Donc, voici notre conteneur Docker pour construire cette application React en production.

Donc, pour l'exécuter, il suffit d'exécuter Docker build, je vais spécifier le nom pour ce conteneur.

Donc, pour spécifier le nom du conteneur, vous devez ajouter ici moins t.

Et le nom du conteneur, je vais le spécifier comme app lorsque nous avons besoin du contexte, qui est ce répertoire.

Donc, nous avons spécifié avec un point.

Et c'est tout.

Donc, nous allons construire ce Dockerfile.

Et nous allons lui attribuer un nom app.

Construisons-le.

Donc, il est en cours de construction.

Maintenant, le conteneur a été construit et est prêt à être déployé.

Mais avant de le déployer, voyons si cela fonctionne correctement.

En l'exécutant sur le navigateur, donc pour le faire, exécutez Docker run notre app, mais nous devons spécifier notre port.

Donc, moins p ici, et le port de notre conteneur sera ad.

Donc, cela s'exécutera sur le port 80.

Et c'est une partie de notre navigateur, donc notre boot ad fonctionnera sur ma machine.

Mais si cela ne fonctionne pas sur votre machine, vous pouvez mettre un autre port comme un jour, cela n'a pas d'importance.

Donc, je vais mettre ad ici.

Et cela exécutera notre conteneur Docker.

Maintenant, je vais aller sur mon navigateur ici, localhost, juste localhost, car 80 est le port par défaut.

Et nous pouvons voir notre react app.

Donc, nous avons créé un conteneur Docker à déployer maintenant.

Et maintenant, fermons cet ID car nous n'en avons plus besoin.

Dans cette vidéo, nous allons créer une simple application node et nous allons la déployer sur AWS, Azure et Google Cloud.

Donc, commençons par créer un terminal et écrire NPM init.

Donc, Oh, Pika tout par défaut, puis j'installerai Express.

Donc, je vais aussi créer un index.

Donc, un fichier JavaScript index.js.

Ici, je vais obtenir Express, donc const Express est égal à require Express.

Ensuite, je vais obtenir, d'accord, le premier app est égal à express et app a une requête GET vers la route principale, toutes les fonctions ici qui auront une requête et la réponse.

Et cela sera très simple, je vais simplement faire response send.

Bonjour, le monde.

C'est tout.

Donc, super simple.

À la fin, je vais écouter le Port 80.

Donc, je veux démarrer cette application.

Donc, c'est assez explicite, mais je vais démarrer cette application via un conteneur Docker.

À cause du Port 80 qui est juste localhost.

Et cela peut entrer en conflit avec votre navigateur.

Donc, créons un Dockerfile.

Le Dockerfile sera très simple.

Donc, nous avons besoin d'un environnement node.

Et la version est 15.4.

Donc, nous allons spécifier un répertoire de travail, je vais l'appeler app, puis nous allons copier le package.json.

Donc, package.json, copié dans le répertoire de travail ici.

Donc, en bref, c'est un point, beaucoup d'étoiles ici.

Donc, cela prendra package.json et aussi package-lock.json.

Donc, si nous faisons cela, cela copiera les deux, puis nous exécuterons npm install car nous obtenons de l'environnement node, puis je copierai tous les fichiers là.

Donc, le premier point signifie tous les fichiers ici, et le second est le répertoire de travail, puis la dernière commande est node index.js.

Et c'est tout.

Donc, voici notre Dockerfile.

Pour construire ce Dockerfile, nous devons d'abord nous assurer d'avoir installé Docker, puis exécuter Docker build, nous devons spécifier un nom pour cette construction Docker, je vais l'appeler app.

Donc, c'est une commande pour choisir un nom pour le conteneur Docker.

Et ensuite, nous devons mettre un point ici, ce qui signifie que c'est ce dossier ici, donc il sélectionnera ce Dockerfile.

Et maintenant, il est en cours de construction, une fois terminé, donc il est terminé.

Et maintenant, pour voir l'application sur notre navigateur ou sur Docker, nous devons spécifier le port que nous devons exécuter.

Donc, 80 est un port à l'intérieur du conteneur Docker.

Et ensuite, c'est notre application.

Donc, dans notre navigateur, sortie pour le huitième.

Donc, si nous exécutons cette commande et allons sur localhost Port 8888, nous verrons HelloWorld ici.

Donc, voici notre conteneur.

Et maintenant, commençons à le déployer sur AWS, Azure et Google Cloud.

Maintenant, fermons aussi cette fenêtre car nous n'en avons plus besoin.

Dans cette vidéo, nous allons créer un Dockerfile pour cette application Vue et déployer ce conteneur Docker sur AWS, Google Cloud et Azure.

Donc, commençons.

Créons un Dockerfile.

Donc, pour construire cette application, nous allons utiliser les constructions multi-étapes dans Docker, je vais vous expliquer ce que c'est. Donc, tout d'abord, nous devons commencer par node.

Et je vais mettre la version de node à cette version.

Et je vais le nommer build.

Donc, je vais expliquer plus tard pourquoi je l'ai nommé ainsi.

Tout d'abord, spécifions le répertoire de travail.

Je vais le nommer app.

Ensuite, copions le package.json dans app.

Donc, dans le répertoire de travail.

Le deuxième point signifie ce répertoire de travail, j'aimerais commencer ici.

Donc, cela obtiendra le package.json et aussi le package-lock.json.

Donc, après avoir obtenu ces fichiers, nous avons exécuté npm install pour installer les modules node, puis nous avons copié tous les fichiers dans le répertoire de travail.

Donc, tous ces fichiers seront copiés dans ce répertoire de travail.

Et ensuite, nous exécutons NPM run build.

Donc, cela construira cette application Vue dans le dossier de distribution.

Donc, si nous exécutons cette commande NPM run build, nous verrons un dossier de distribution créé ici.

Donc, c'est un dossier, et il aura un index.html, index, etc.

Donc, maintenant, ce que je vais faire, c'est ajouter un autre from ici.

Et je vais obtenir la version nginx 1.19, pourquoi j'ajoute un autre from ici.

Donc, c'est une construction multi-étapes, donc nous n'avons plus besoin de tous ces dossiers à l'intérieur du conteneur Docker, à l'intérieur du conteneur Docker, nous avons besoin uniquement du dossier de distribution, donc uniquement ce dossier.

Et pour faire cela, nous devons d'abord créer la première étape, qui contient tous les fichiers et le dossier de distribution.

Et ensuite, nous créons un autre from ici.

Et d'abord, nous avons besoin d'un fichier nginx.

Donc, nous allons utiliser nginx ici, créons un répertoire nginx.

Et à l'intérieur, je vais créer un fichier nginx.conf.

Ici, je vais coller ce code.

Donc, il y a beaucoup de code.

Mais je vais fournir le lien dans la description de cette vidéo.

Donc, vous pouvez obtenir ce code.

Et pour copier ce fichier nginx, nous sommes sur la copie nginx nginx.conf, nous devons le copier dans le dossier ETC nginx nginx.conf.

Donc, nous allons mettre ce fichier où, lorsque nous copierons depuis build.

C'est pourquoi je l'ai nommé ainsi.

Donc, une fois que nous avons terminé, nous avons une référence pour ce build.

Donc, à partir de ce build, nous voulons uniquement le dossier de distribution.

Donc, dans le dossier de distribution de l'application.

C'est pourquoi nous avons également nommé le répertoire de travail app, donc il est dans app et aussi le dossier de distribution.

Nous allons le copier vers usr share nginx.

html.

Et c'est tout.

Donc, à la fin, nous aurons un conteneur plus petit contenant uniquement HTML, JavaScript et des fichiers CSS.

Donc, exécutons ce conteneur.

Pour exécuter ce conteneur.

Assurez-vous d'abord d'avoir installé Docker et exécutez Docker build, nous devons spécifier le nom pour ce conteneur, notre appel est app.

Donc, si vous voulez nommer votre conteneur, quel que soit le nom que vous voulez, avec moins t et le nom ici, puis je vais mettre un point qui signifie que c'est ce dossier ici et il sélectionnera ce Dockerfile.

Donc, avec cela, notre Docker est en cours de construction.

Attendons qu'il soit terminé et donc il est construit maintenant, pour le voir sur le navigateur, nous devons l'exécuter.

Donc, autour de Docker, nous devons spécifier un port.

Donc, pour le voir sur notre navigateur, sortie de ce port vers notre navigateur.

Et cette application s'exécutera sur le port 80 puisque nous utilisons nginx ici, puis nous avons besoin du nom de notre conteneur qui est app, donc exécutons cela et il est en cours d'exécution maintenant.

Donc, si nous allons sur localhost Port 8888, nous verrons l'application Vue.

Donc, voici notre conteneur.

Et maintenant, je vais fermer cette fenêtre car nous n'en avons plus besoin.

Maintenant, déployons ce conteneur.

Dans cette vidéo, nous allons créer un conteneur Docker JS prêt pour la production.

Et nous allons pousser ce conteneur vers AWS, Google Cloud et Azure.

Donc, commençons.

Tout d'abord, je veux changer dans main.ts, le port ici pour ajouter, car tous nos conteneurs commenceront avec le Port 80.

Et maintenant, créons le Dockerfile.

Donc, assurez-vous également d'avoir installé Docker sur votre machine.

Donc, commençons la construction.

Donc, nous devons commencer par l'environnement node et la version 15.4.

Et je vais le nommer build.

Donc, c'est une construction Docker multi-étapes.

Je vais expliquer cela plus tard.

Tout d'abord, commençons par la première étape.

Donc, commençons par node 15.4.

Et que voulons-nous faire ici, spécifions un répertoire de travail app.

Et nous voulons copier le package.json dans l'application.

Donc, point min.

Donc, ce répertoire de travail, aussi, j'aimerais commencer ici.

Donc, si je devais commencer ici, cela obtiendrait package.json et aussi package-lock.json.

Donc, j'ai ajouté le package.json, maintenant exécutez NPM install.

Puisque nous sommes dans l'environnement node, cette commande NPM est disponible.

Après avoir terminé cela, nous voulons copier tout dans le répertoire de travail.

Donc, ce premier point signifie tous les fichiers ici, le deuxième point signifie ce répertoire de travail après avoir terminé NPM run build.

Donc, avec cela, nous construisons cette application nest js.

Donc, exécutons NPM run build ici et voyons ce qu'il génère.

Donc, cela générera ce dossier ici.

Donc, comme nous pouvons le voir, nous avons un dossier dist.

Et ici, nous avons tous les fichiers nécessaires.

Donc, afin d'exécuter cela en production, nous devons avoir ce dossier dist, et nous n'avons pas besoin des autres fichiers.

C'est pourquoi nous faisons une construction multi-étapes, car nous allons créer un autre environnement node ici à partir de node 15.4.

Aussi.

Et dans cet environnement node, nous allons spécifier à nouveau le répertoire de travail app.

Donc, ne confondez pas cela avec cela, car ce sont deux conteneurs différents.

Ensuite, nous allons copier ici, je vais copier uniquement le package.json, en fait, nous allons exécuter npm install, mais nous avons besoin uniquement des packages de production.

Donc, si nous allons dans package.json, nous avons des dépendances et des dépendances de développement, si nous l'exécutons comme cela, nous allons installer uniquement les dépendances.

Donc, il y a moins de packages ici.

Et ce package node sera plus petit que celui-ci.

Bien sûr, car nous avons moins de packages, puis nous allons copier depuis build, nous allons copier le dossier de distribution.

Donc, app dist.

Donc, app est le répertoire de travail ici.

C'est le dossier que nous venons de générer.

Et nous allons le copier vers l'utilisateur, partager nginx.

html.

Et c'est tout.

Donc, à la fin, nous allons exécuter la commande MPM run start prod.

Donc, c'est une version plus petite de celle-ci, car ce conteneur aura uniquement le dossier de distribution et les modules node, mais uniquement les packages de production, donc nous n'avons pas besoin de toutes ces fioles.

Donc, nous avons créé le conteneur de production prêt pour nest JS, exécutons-le.

Donc, pour l'exécuter, il suffit d'exécuter Docker build, nous devons spécifier le nom du conteneur, je vais l'appeler app.

Donc, si vous voulez nommer un conteneur, vous mettez moins t et le nom du conteneur.

Et le point signifie ce dossier, et il sélectionnera ce Dockerfile.

Donc, si nous exécutons cela, il construira notre application.

Non, attendons qu'il soit terminé.

Donc, il est terminé.

Maintenant, ce conteneur peut être poussé vers le cloud.

Mais d'abord, testons-le.

Donc, pour le tester, nous devons l'exécuter.

Donc, Docker run.

Et nous devons spécifier le port, le port à l'intérieur du conteneur Docker est 80.

Mais dans notre navigateur, nous pouvons mettre n'importe quel port que nous voulons.

Donc, sortie de ce port, et le nom du conteneur est app.

Donc, nous pouvons exécuter notre conteneur comme ceci, comme nous le voyons, il s'exécute avec succès, et nous pouvons aller sur localhost 8888.

Et nous pouvons voir HelloWorld ici, donc le conteneur est en cours d'exécution.

Maintenant, nous devons pousser ce conteneur de production vers le cloud.

Et je vais fermer cet ID ici car nous n'en avons plus besoin.

Dans cette vidéo, nous allons créer un conteneur Docker prêt pour la production pour une application Angular, puis nous allons pousser ce conteneur vers AWS, Azure et Google Cloud.

Donc, commençons.

Tout d'abord, créez un Dockerfile.

Assurez-vous également d'avoir installé Docker sur votre machine.

Donc, nous avons besoin de l'environnement ici.

Donc, nous avons besoin de l'environnement node.

Et la version que je vais mettre ici est 15.4.

Et je vais le nommer build.

Donc, nous allons faire une construction Docker multi-étapes, je vais expliquer cela plus tard.

Tout d'abord, concentrons-nous sur cette partie de node.

Cette partie ici, nous voulons construire notre application.

Commençons par le répertoire de travail.

Vous pouvez le nommer comme vous voulez, je vais l'appeler app, puis nous allons copier le package.json dans le répertoire de travail.

Donc, je vais ajouter aussi le point ici.

Donc, cela copiera le package.json et aussi le package-lock.json, ce point signifie ce répertoire de travail.

Donc, une fois que nous avons ces fichiers là, nous sommes sur npm install et puisque nous utilisons le conteneur node, nous avons npm disponible.

Donc, après l'avoir installé, nous devons le construire pour la production.

Donc, avant d'exécuter quoi que ce soit ici, je vais, je veux faire un changement, nous avons energy bill ici dans nos scripts, mais si nous voulons construire pour la production, nous devons ajouter prod ici.

Donc, ce que je vais faire, c'est ajouter un nouveau script prod et cela sera mg build prod comme ceci.

Donc, cela sera plus facile.

Et maintenant ici, je vais exécuter la commande NPM run prod.

Donc, cela construira notre application pour la production.

Donc, je vais exécuter cette commande ici aussi.

Et voyons quels fichiers elle génère, shop.

Maintenant, nous allons apprendre pourquoi je l'ai nommé ainsi.

Parce qu'une fois que nous exécutons NPM run prod, cela créera certains fichiers ici.

Et quand nous n'avons plus besoin de ces fichiers, nous avons besoin uniquement du dossier de distribution.

Donc, nous avons créé le build.

Donc, je ne suis pas sûr pourquoi mon application ne récupère pas les fichiers, peu importe.

Donc, ajoutons le nouveau from ici et cette fois, nous voulons avoir node, mais je vais ajouter nginx et la version sera 1.19.

Donc, ici, nous voulons lire node, nous allons simplement servir les fichiers HTML dont j'ai besoin pour rafraîchir, je ne suis pas sûr pourquoi ils se rechargent.

Donc, nous avons le dossier de distribution ici.

Et nous pouvons voir, nous avons index.html et ces fichiers.

Donc, il est situé dans le dossier de distribution, angular Docker.

C'est le nom de mon projet, d'ailleurs, vous pouvez nommer votre projet comme vous voulez.

Donc, maintenant, nous sommes sur nginx.

Nous avons aussi besoin d'un répertoire ici nginx.

Et j'ajouterai ici un fichier nginx.conf.

Ici, je vais coller ce code nginx.

Donc, je vais fournir ce code dans la description de cette vidéo.

Et allons au Dockerfile.

Je vais copier ici nginx nginx.conf.

Et nous allons copier cela vers edisi nginx nginx.

Ce calme.

Donc, point ici.

Donc, nous avons copié ce fichier dans cet autre conteneur.

Et maintenant, nous allons utiliser ce build ici.

Donc, comme je l'ai dit avant, nous n'avons plus besoin de ce virus, nous avons besoin uniquement du dossier de distribution, puisque cela servira le fichier index.html avec ces fichiers JavaScript construits.

Donc, pour cela, nous allons le copier depuis build, nous allons copier, nous avons le répertoire de travail est app ici.

Donc, depuis app, il y a un autre dossier ici, qui est angular Docker, dans mon cas, Angular, Docker.

Et nous allons le copier vers throw a lot of flesh just in case to user share nginx.

html.

Donc, de cette façon, ce conteneur était plus grand, puisque nous n'avons pas fait de modules et tous ces fichiers, mais celui-ci n'a que des fichiers HTML et JavaScript.

Donc, le conteneur plus petit est seulement nginx, qui sert uniquement ce fichier HTML.

Et nous avons besoin de ce moteur x, nous en avions besoin parce que lorsque nous allons à une URL spécifique, nous voulons rediriger tous vers l'index.html.

Donc, c'est cet emplacement.

Sinon, nous obtiendrons une erreur.

Donc, voici le Dockerfile.

Et maintenant, exécutons-le.

Donc, pour exécuter ce Dockerfile, exécutez Docker build, nous devons spécifier un nom pour ce Dockerfile pour chaque conteneur Docker.

Je vais spécifier le nom de l'application, mais vous pouvez le nommer comme vous voulez.

Et nous devons construire ce Dockerfile, donc nous devons l'ajouter comme un point ici.

Donc, maintenant, il est en cours de construction, attendons qu'il soit terminé.

Donc, il a échoué.

Parce que j'ai oublié une ligne ici entre npm install et NPM, run prod, qui est de copier tous les fichiers dans le répertoire de travail.

Donc, mon meilleur.

Donc, cela copiera tous ces fichiers dans ce répertoire de travail.

Et ensuite, nous devons construire pour la production.

Donc, maintenant que nous avons corrigé le problème, exécutons-le à nouveau.

Donc, maintenant, il a été construit avec succès.

Et maintenant, ce conteneur est prêt à être poussé vers le cloud.

Mais d'abord, voyons sur notre navigateur.

Donc, pour le voir sur notre navigateur, nous devons exécuter le conteneur.

Donc, Docker run, nous devons spécifier le port.

Donc, le port à l'intérieur du conteneur est 80.

Dans notre hôte local, nous pouvons mettre n'importe quel port que vous voulez, je vais mettre 8888, donc et ensuite, nous avons besoin du nom de notre conteneur, que nous avons nommé app.

Donc, c'est tout.

Si nous exécutons cela et allons sur notre navigateur, allons sur localhost 8888.

Et nous verrons l'application Angular en cours d'exécution.

Donc, c'était notre conteneur qui a été construit.

Maintenant, poussons ce conteneur vers le cloud dans nos vêtements.

Cet ID car nous ne l'utiliserons plus.

Dans cette vidéo, nous allons créer un fichier Docker prêt pour la production pour une application Go, et nous allons le pousser vers AWS, Google Cloud et Azure. Donc, commençons par exécuter go mod init.

Nous appellerons le projet Docker, cela n'a pas d'importance.

Donc, nous allons également utiliser le framework Go Fiber, nous voulons utiliser ce framework, mais nous allons simplement copier la partie HelloWorld, nous allons créer un fichier main.go.

Et donc, activons l'intégration ici, créons un fichier Go, main.

Le package, donc je vais le baser ici.

C'est notre fichier Go principal.

Et, bien sûr, obtenons également ce modèle de fibre ici.

Donc, go get cela.

Donc, nous l'avons obtenu, nous avons également fait notre go mod.

Donc, nous avons également obtenu certains, ceux-ci sont importants car nous devons les ajouter à Docker.

Donc, c'est notre application Go.

Maintenant, créons un Dockerfile.

Donc, je vais créer un fichier ici.

Dockerfile.

Assurez-vous également d'avoir Docker installé sur votre machine.

Donc, maintenant ici, nous devons spécifier l'environnement dans lequel ce conteneur sera construit.

Et ce sera un conteneur golang.

Donc, je vais mettre la version ici, qui est la dernière version pour cette fois est 1.16.

Et je vais ajouter Alpine ici, qui est une version de Linux, qui est la plus petite.

Et maintenant, spécifions un répertoire de travail, je vais l'appeler app, mais vous pouvez le nommer comme vous voulez.

Donc, le répertoire de travail est app, maintenant copions go mod dans le répertoire de l'application.

Donc, cet autre point signifie qu'il sera copié dans ce répertoire de travail.

Copions également go sum là.

Donc, nous avons copié cela, maintenant nous pouvons les télécharger.

Donc, pour les télécharger, nous devons exécuter la commande go mod download.

Donc, avec cela, tous les packages que nous allons installer ici, ils seront également téléchargés dans le conteneur Docker.

Après cela, nous devons copier tous les fichiers.

Donc, ce point signifie tous les fichiers ici, le second signifie que tous les fichiers seront copiés dans le répertoire de travail.

Donc, une fois que nous avons tout copié, nous exécutons go build et la sortie sera out, vous pouvez nommer la sortie comme vous voulez.

Et il apprendra sur ces fichiers ici.

Donc, nous pouvons également exécuter cette commande.

Maintenant, donc nous pouvons tester ce qu'il génère.

Donc, nous avons out et nous avons une distribution ici que nous pouvons utiliser.

Donc, maintenant que nous avons cela, c'est l'exécutable exact, nous exécutons la commande qui est simplement out, c'est tout.

Donc, vous pouvez le nommer comme vous voulez.

Je l'ai nommé cela.

Et simplement, nous allons exécuter ce fichier et je vais exécuter go app.

D'accord, une dernière chose que je vais faire, c'est que tous les backends doivent écouter le Port 80.

Donc, je ne veux pas écouter le Port 3000.

Je vais écouter le Port 80.

Mais ce sera le port à l'intérieur du conteneur Docker.

Donc, ne vous inquiétez pas si cela entre en conflit avec votre navigateur.

Donc, maintenant que nous avons tout construit, exécutons cela.

Donc, pour l'exécuter, exécutez Docker build, nous devons nommer le conteneur, je vais nommer le conteneur app.

Donc, pour nommer le conteneur, nous devons mettre moins t devant, puis nous devons ajouter un point ici, ce qui signifie qu'il recherchera ce dossier et exécutera ce Dockerfile.

Donc, construisons-le.

Et maintenant, il est en cours de construction.

Donc, il apprendra toutes ces commandes.

Et attendons qu'il soit terminé.

Donc, tout a été construit avec succès.

Et maintenant, nous pouvons pousser ce conteneur vers le cloud.

Mais avant, voyons sur notre navigateur si tout fonctionne bien, donc exécutez Docker run, nous devons spécifier le port.

Donc, le port à l'intérieur du conteneur Docker était ad.

Mais dans notre hôte local, nous pouvons mettre n'importe quel port que nous voulons, je vais mettre 8888.

Et ensuite, nous avons besoin du nom de notre conteneur, que nous avons appelé app.

Donc, comme vous pouvez le voir, l'application fiber est en cours d'exécution.

Et maintenant, si nous allons sur localhost Port 8888, nous verrons hello world ici.

Donc, nous avons construit avec succès le conteneur prêt pour la production pour golang.

Et maintenant, poussons-le vers le cloud.

Et je vais fermer cet ID car nous n'en avons plus besoin.

Dans cette vidéo, nous allons créer un conteneur Docker pour une application Laravel.

Et ensuite, nous allons pousser ce conteneur Docker vers AWS, Google Cloud et Azure.

Donc, commençons.

Tout d'abord, créez ici un Dockerfile.

Et bien sûr, assurez-vous d'avoir installé Docker sur votre machine.

Et ici, dans le Dockerfile, nous allons commencer par php, la version sera 7.4 FPM.

Donc, c'est le conteneur qui aura PHP déjà installé.

Nous devons encore installer certains autres packages.

Je vais les lister ici.

Donc, ce sont quelques bibliothèques que nous devons installer dans le VCS.

L'installation de composer car composer n'est pas déjà installé ici.

Et c'est une commande qui activera ces deux extensions dans notre fichier PHP.ini.

Donc, c'est tout.

Après avoir ajouté tout ce dont nous avons besoin, spécifions le répertoire de travail.

Je vais l'appeler app, nous devons copier composer.json dans le répertoire de travail.

Donc, cela signifie que ce point signifie que ce composer.json sera copié ici.

Et après avoir obtenu composer.json, nous devons exécuter composer install.

Et nous allons ajouter no scripts ici.

Donc, nous allons simplement installer tout ce dont composer a besoin.

Et nous allons exécuter ces scripts comme ceux-ci.

Donc, nous allons simplement installer tout et après cela, nous allons copier tous les fichiers ici dans le répertoire de travail.

Donc, maintenant nous avons tout et nous allons simplement exécuter la commande php artisan serve, nous devons spécifier aussi l'hôte qui sera 0.0.0.0 et aussi le port 80, donc nous n'avons pas besoin de mettre le port 80 ici, mais j'en ai besoin parce que je combine plusieurs vidéos, oui, et elles ont toutes le port 80.

Donc, nous avons terminé avec le Dockerfile, maintenant nous sommes prêts à le construire.

Donc, pour construire ce Dockerfile, exécutez Docker build, nous devons spécifier le nom pour cette construction Docker.

Et nous pouvons spécifier un nom en ajoutant moins t, le nom, je vais le mettre app, mais vous pouvez le nommer comme vous voulez, à la fin, point, service de contacts ici.

Et nous recherchons ce Dockerfile.

Donc, il apprendra ce Dockerfile, et maintenant il est en cours de construction, attendons qu'il soit terminé.

Donc, il est construit.

Maintenant, ce conteneur est prêt à être déployé sur le cloud.

Mais avant, testons-le sur notre navigateur pour voir si cela fonctionne.

Donc, pour l'exécuter sur notre navigateur ou sur Docker, nous devons spécifier un port.

Donc, le port à l'intérieur du conteneur Docker est 80.

Et dans notre navigateur, vous pouvez mettre n'importe quel port que vous voulez, sortie 8888.

Donc, à la fin, nous avons besoin du nom de notre conteneur, donc nous l'avons spécifié comme étant app.

Donc, c'est notre Docker run, et il est en cours d'exécution.

Donc, si nous allons sur le navigateur maintenant et allons sur localhost Port 8888, nous verrons l'application Laravel en cours d'exécution, donc le conteneur est en cours d'exécution.

Maintenant, poussons ce conteneur vers le cloud.

Aussi, je vais fermer cet ID car nous ne l'utiliserons plus.

Cette vidéo créera un conteneur Docker pour un projet .NET.

Et nous allons pousser ce projet vers AWS, Google Cloud et Azure.

Donc, commençons.

Tout d'abord, dans cette API Web, je vais apporter une petite modification, je vais supprimer ce contrôleur ici.

Et la route sera la route vide.

Et notre application retournera simplement la météo par défaut.

Donc, ce n'est pas important.

Ce qui est important, c'est de créer un nouveau Dockerfile, donc nouveau fichier, Dockerfile.

Donc, assurez-vous également d'avoir installé Docker sur votre machine.

Et commençons par from, nous avons besoin de l'image que nous voulons démarrer.

Donc, je vais écrire Microsoft Azure Container Registry microsoft.com slash dotnet.

Slash SDK.

Donc, nous allons commencer avec la version cinq.

Donc, c'est le conteneur qui démarrera et qui aura déjà installé le SDK.

Et je vais le nommer build.

Donc, ce sera une construction Docker multi-étapes.

Et je vais expliquer plus tard pourquoi je le nomme ainsi.

Donc, commençons par le répertoire de travail.

Je vais le nommer app, vous pouvez spécifier n'importe quel dossier que vous voulez, je vais le nommer comme ceci.

Et ici, nous allons copier le projet C#.

Donc, tout ce projet C#.

Comme ceci, et nous allons le copier dans le répertoire de travail.

Donc, ce projet sera copié dans ce point signifie ce répertoire de travail et après qu'il soit copié, nous allons exécuter la commande .NET restore.

Après avoir exécuté la copie, cette commande copiera tout dans ce dossier à nouveau.

Donc, cela obtiendra tous les fichiers ici.

Et il les copiera dans le répertoire de travail.

Et après avoir copié tous les fichiers, nous devons publier vers une DLL.

Donc, pour le faire, nous allons exécuter la commande .NET publish.

Nous devons spécifier release et dans la sortie sera dans le dossier out.

Et c'est tout pour la première étape.

Donc, exécutons cette commande dans notre machine locale pour voir ce que cela génère.

Donc, si nous exécutons cette commande, nous obtiendrons un dossier de sortie ici, où nous aurons beaucoup de fichiers.

Celui qui nous intéresse est cette DLL dotnet Docker.

Donc, nous nous intéressons uniquement à ce fichier, et nous pouvons ignorer tous les autres fichiers.

C'est pourquoi nous utilisons maintenant une construction multi-étapes, car cela contiendra tous les fichiers, et aussi la sortie.

Mais ce conteneur que nous allons construire maintenant, donc à partir de la copie de cette dotnet.

Et nous allons spécifier un ASP dotnet ici.

Ce conteneur aura le même répertoire de travail.

Mais ne confondez pas ce répertoire de travail avec celui-ci, car ce sont des conteneurs différents.

Et nous allons copier depuis le build, depuis ce build, nous allons copier app, qui est le répertoire de travail là.

out.

Donc, nous allons copier tout dans le dossier out vers ce point, qui est ce répertoire de travail.

Donc, nous avons créé un autre conteneur avec uniquement le dossier out, donc il est plus petit.

Et ce qui reste, c'est d'ajouter un point d'entrée .NET et il exécutera .NET Docker DLL.

Et c'est tout.

Donc, à la fin, nous avons un conteneur Docker plus léger, qui est juste une DLL, donc nous pouvons l'exécuter.

Donc, nous avons terminé avec ce Dockerfile.

Construisons-le.

Donc, pour construire un Dockerfile, exécutez Docker build.

Et nous voulons spécifier un nom pour cette construction Docker.

Et nous pouvons spécifier un nom en ajoutant moins t, app, c'est le nom que nous voulons construire.

Et nous allons ajouter le contexte qui est un point.

Cela exécutera ce Dockerfile.

Donc, il est en cours de construction, attendons qu'il soit terminé.

Donc, le conteneur a été construit.

Et maintenant, il est prêt à être poussé vers le cloud.

Mais avant, testons-le sur notre navigateur.

Pour le tester sur notre navigateur, nous devons exécuter ce conteneur, nous devons spécifier le port.

Donc, à l'intérieur du conteneur, le port est 80.

Mais dans notre hôte local, nous pouvons mettre n'importe quel port que nous voulons, sortie 8888.

Entrez le nom de notre conteneur était app.

Donc, exécutons cela.

Et il est en cours d'exécution avec succès maintenant.

Donc, si nous ouvrons notre navigateur et écrivons ici, localhost Port 8888.

Nous pouvons voir ce tableau JSON qui retourne cette prévision météo.

Donc, cela fonctionne bien.

Donc, ce conteneur a été construit.

Et maintenant, nous devons le pousser vers le cloud.

Je vais également fermer cet ID car nous n'en avons plus besoin.

Dans cette vidéo, nous allons créer un conteneur Docker pour une application Kotlin.

Et nous allons pousser ce conteneur vers AWS, Google Cloud et Azure.

Donc, commençons.

Tout d'abord, déplaçons ici le dossier de test et dans les ressources, je vais ajouter le port du serveur à AD, donc je veux que tous les conteneurs que je déploie s'exécutent sur le port 80 parce que je réutilise du contenu, mais vous pouvez le changer pour le port que vous voulez, cela n'a pas d'importance.

Donc, j'ai ajouté le Port 80 et aussi je vais ajouter un contrôleur ici.

Donc, beaucoup de répertoires de contrôleurs dans cela, je vais créer un nouveau fichier Kotlin.

Donc, home controller, donc ce sera une classe home controller et il aura une fonction Home.

Donc, ajoutons aussi un ici, cela devrait être un contrôleur de repos.

En fait, je vais tout coller, donc je ne veux pas l'importer à nouveau.

Donc, c'est notre contrôleur de maison, ce sera un contrôleur de repos, il n'aura qu'une seule méthode qui retournera hello world.

Donc, c'est tout.

Donc, c'est simple.

Et maintenant, nous voulons créer un conteneur Docker avec cette simple application.

Donc, créons un Dockerfile.

Donc, tout d'abord, assurez-vous d'avoir installé Docker sur votre machine.

Et ici, j'ajouterai depuis, nous avons besoin de l'environnement qui sera gradle.

Et la version sera sept, et le JDK sera huit.

Donc, c'est une version de ce gradle et dédié, je veux tout nommer cela comme build.

Donc, ce sera une construction Docker multi-étapes.

Je vais expliquer cela plus tard.

Pourquoi je le nomme ainsi.

Mais concentrons-nous d'abord sur cette partie.

Spécifions un répertoire de travail, je vais l'appeler app.

Donc, vous pouvez mettre n'importe quel nom que vous voulez ici.

Donc, tous les fichiers seront créés à l'intérieur de ce dossier maintenant, donc copions tout là.

Donc, ce premier point signifie tous ces fichiers, et le second signifie ce répertoire de travail.

Une fois que nous avons tout ajouté là, nous devons exécuter la commande dot flesh Gradle W, nous allons exécuter ce fichier build avec la trace de la pile.

Donc, cela générera un dossier build ici.

Laissez-nous voir.

Donc, si je lance Gradle w build ici.

Cela générera un dossier builder.

Donc, comme vous pouvez le voir, nous avons un dossier build maintenant.

Donc, ce que nous voulons ici, c'est d'aller dans les libs et c'est notre jar que nous voulons exécuter.

En fait, je vais supprimer ce snapshot pour supprimer ce snapshot, nous devons aller dans Gradle, build that gather that kotlin pour supprimer cela.

Donc, cela créera un nom plus court sans le snapshot.

Donc, nous n'avons pas besoin de connaître aucun de ces fichiers, sauf pour ces fichiers jar.

Donc, c'est pourquoi nous avons créé un modèle de construction multi-étapes, car maintenant nous pouvons créer un autre conteneur à partir de openjdk.

Et celui-ci sera plus petit, nous allons spécifier le même répertoire de travail.

Mais ce sont des conteneurs différents.

Donc, ne vous inquiétez pas s'ils ont le même nom.

Nous allons exposer le Port 80 car nous l'avons défini dans notre dossier source, puis nous allons le copier depuis là builder, nous allons copier ce chemin.

Donc, app build libs.

Et ensuite, nous avons besoin du nom du fichier.

Donc, je vais copier cela.

Mais nous n'avons pas besoin du snapshot.

Donc, nous supprimons ce snapshot.

Donc, cela sera comme ceci, ce jar.

Donc, ce sera le nom de la construction.

Et nous allons le copier dans ce répertoire de travail.

Et ce conteneur n'a que ce jar et nous allons simplement l'exécuter, donc la commande Java jar et ensuite ils vont copier ce nom.

Et c'est tout.

Donc, c'est un conteneur.

Commençons, exécutons-le et testons-le.

Donc, d'abord, nous devons le construire.

Donc, Docker build.

Nous devons spécifier le nom pour cette construction Docker.

Et nous pouvons le faire en ajoutant moins t.

Le nom du conteneur sera app.

Donc, nous avons ajouté cela et ensuite nous devons ajouter un point qui signifie que c'est ce contexte et qu'il exécutera ce Dockerfile.

Exécutons-le.

Donc, j'ai fait une erreur.

C'est build, j'ai oublié un clou ici.

Donc, maintenant tout fonctionne.

Attendons que cela soit terminé.

Donc, c'est terminé.

Maintenant, ce conteneur est prêt à être publié sur le cloud.

Mais avant, testons-le sur notre navigateur.

Pour le tester sur notre navigateur, nous devons exécuter le conteneur.

Donc, Docker run, nous devons spécifier le port, donc moins b, pas D.

et le port à l'intérieur du conteneur Docker est 80.

Mais dans notre hôte local, nous pouvons mettre ce que nous voulons, je vais mettre 8888.

Et le nom du conteneur était app.

Si nous l'exécutons comme ceci, il l'exécutera.

Donc, il fonctionne bien.

Maintenant, testons-le sur le navigateur, localhost Port 8888.

Nous pouvons voir HelloWorld ici, ce qui signifie que notre application fonctionne bien.

Maintenant, déployons cette application sur le cloud.

Et je vais fermer cet ID car nous n'en avons plus besoin.

Dans cette vidéo, nous allons créer un conteneur Docker pour une application Deno, et nous allons le pousser vers AWS, Google Cloud et Azure.

Donc, commençons.

Donc, assurez-vous d'abord d'avoir installé Deno.

Et je vais simplement copier ce code.

Je vais créer dans un répertoire vide ici, un fichier app.ts, et je vais coller ce code.

Donc, c'est vraiment simple, si nous exécutons cette application, alors autour des larmes, nous devons aussi ajouter le drapeau allow net.

Et comme nous pouvons le voir, il s'exécute sur le port 8000.

Donc, si nous allons ici, localhost Port 8000.

Nous verrons Hello, world.

Donc, c'est notre application Deno que nous allons pousser.

Et commençons maintenant par créer un Dockerfile.

Assurez-vous également d'avoir Docker installé sur votre machine.

Donc, cela sera super simple.

Nous devons venir de denoland.

Ils ne sont pas la dernière version, kerlin est actuellement 1.11.0.

Et nous devons spécifier un répertoire de travail app.

Et ensuite, nous allons copier tout là.

Donc, cette commande signifie que le copiera des DS vers ce répertoire de travail.

Et ce qui reste, c'est de Sibley autour de la commande que nous venons d'exécuter avant, qui est, nous n'avons pas besoin de spécifier qu'ils ne sont pas, mais nous allons autour.

Nous allons ajouter le drapeau.

Allow.

net et le fichier est app.ts.

Et c'est tout, super simple.

Aussi, je vais changer quelque chose ici.

Je veux le servir sur le Port 1000.

Mais je veux le servir sur le Port 80.

Parce que tous nos conteneurs Docker serviront sur le port 80.

Et c'est plus facile pour moi de combiner ces tutoriels, mais vous pouvez mettre le Port 1000, c'est totalement correct.

Maintenant que nous avons tout, exécutons ce Dockerfile, d'abord nous devons le construire.

Donc, pour le construire, exécutez Docker build, nous voulons, nous avons besoin du nom du conteneur.

Donc, nous avons spécifié par moins t et nous allons spécifier le nom du conteneur comme étant app et ensuite nous allons ajouter un point ici qui signifie que c'est ce contexte et qu'il sélectionnera ce Dockerfile.

Donc, construisons-le maintenant, il est en cours de construction, il sera rapide une fois qu'il a terminé de charger tout.

Donc, c'est terminé.

Maintenant, nous pouvons pousser ce conteneur vers le cloud.

Mais avant, testons-le à nouveau sur notre navigateur.

Et pour le tester, nous devons l'exécuter.

Donc, Docker run.

Cette fois, nous devons spécifier un port et le port arrière.

Donc, le port du conteneur est 80, comme nous l'avons dit, et dans le front end, nous pouvons mettre 8888, pas dans le front et dans notre hôte local.

Et ensuite, nous devons spécifier le nom de notre conteneur.

Donc, c'est une commande pour exécuter ce conteneur sur le Port 8888.

Donc, il est en cours de téléchargement à nouveau, car il s'exécute à l'intérieur du conteneur et je ne suis pas sûr pourquoi il a ce problème.

Maintenant.

Après l'avoir exécuté à nouveau, cela a fonctionné.

Je ne suis pas sûr pourquoi cela a échoué la première fois.

Et il dit un localhost ad ici, mais cela est à l'intérieur du conteneur Docker.

Notre hôte local maintenant, 1000 ne fonctionnera pas comme nous le voyons.

Mais notre port maintenant est 8888.

Et maintenant, nous pouvons voir Hello word.

Maintenant, ce HelloWorld s'exécute à l'intérieur du conteneur Docker.

Et c'est tout, nous avons terminé le conteneur Docker pour cette application Deno.

Maintenant, poussons-le vers le cloud.

Je vais également fermer cet ID car nous n'en avons plus besoin.

Donc, je suis connecté maintenant à ma console de gestion AWS.

Et nous allons pousser maintenant notre conteneur Docker vers le registre de conteneurs élastiques.

Donc, j'ai un raccourci ici, ou nous pouvons le rechercher.

Donc, allons au registre de conteneurs.

Et c'est un registre de conteneurs.

Vérifions les dépôts, donc nous n'avons aucun dépôt ou registres, nous devons en créer un.

Donc, nous allons pousser notre conteneur Docker ici pour avoir notre dépôt prêt.

Tout d'abord, avant de faire quoi que ce soit, assurez-vous d'installer l'AWS CLI, donc allez sur AWS amazon.com slash cli.

Et sur le côté droit ici, vous pouvez télécharger la version Windows, Mac OS ou Linux.

Donc, avec cela, vous aurez accès à votre terminal AWS et vous aurez plusieurs commandes que vous pouvez utiliser.

Donc, maintenant, connectons-nous d'abord au registre de conteneurs élastiques en utilisant cette commande.

Donc, AWS ECR est le registre de conteneurs élastiques.

C'est la commande pour se connecter.

C'est la région, la région US East deux pipe Docker login est le nom d'utilisateur qui sera AWS, le mot de passe, il sera généré par celui-ci.

Donc, c'est pourquoi son mot de passe SD, et cette autre URL est comme ceci, c'est notre ID d'utilisateur.

Donc, nous pouvons le trouver, si nous allons à notre compte, vous avez l'ID ici.

Donc, c'est tout.

Et le Docker dot ECR, c'est aussi la même région sur Amazon aws.com.

Exécutons cette commande.

Et nous nous sommes connectés avec succès.

Et maintenant, ce qui reste, c'est de pousser notre conteneur Docker vers le registre de conteneurs élastiques.

Donc, pour faire cela, nous devons faire Docker tag, le nom de notre conteneur était app.

Et je vais copier à nouveau cette URL.

Donc, nous devons cibler cette URL slash à la fin app, donc le nom doit être le même ici et cette URL sera utilisée beaucoup.

Donc, ciblons cela.

Et après l'avoir ciblé, nous devons le pousser.

Donc, supprimez le tag pour le pousser.

Et attendons qu'il soit terminé.

Donc, nous obtenons une erreur, le dépôt avec le nom app n'existe pas.

Donc, créons-le.

Nous sommes ici dans les dépôts et créons un dépôt.

Donc, c'est la même URL et ce sera app.

Donc, je vérifie juste la région si elle est la même.

Donc, ce sera un dépôt privé.

C'est le nom du dépôt.

Et je vais laisser les autres par défaut, créons ce dépôt.

Et nous l'avons créé.

Donc, poussons notre image maintenant, pas ici, ici, Docker push.

Et maintenant, il est en train de pousser.

Donc, cela prendra un certain temps, et l'image sera poussée vers le dépôt.

Donc, notre image a été poussée.

Donc, si nous allons à notre dépôt, nous avons une image ici, la taille et tout le reste.

Donc, nous avons notre image dans notre dépôt.

Je vais copier l'URL ici pour le dépôt, car nous en aurons besoin.

Et maintenant, allons au service de conteneurs Amazon, Elastic Container Service ECS.

Et ici, allez dans les clusters, et nous allons créer un cluster.

Donc, je vais sélectionner le cluster AWS fargate, car il s'occupera de la gestion du serveur pour nous.

Si vous voulez gérer votre serveur, sélectionnez cette autre option.

Mais cela est beaucoup plus facile si nous sélectionnons AWS fargate.

Donc, allons à l'étape suivante, le nom du cluster, donc mon app et je vais créer un VPC par défaut pour ce cluster.

Et je ne veux pas sélectionner autre chose.

Créons-le.

Et attendons que cela soit terminé.

Donc, le cluster est créé, cliquez sur Voir le cluster.

Et maintenant, nous avons besoin de la définition de la tâche.

Donc, allez dans les définitions de tâches.

Et créons une nouvelle définition de tâche.

Donc, je vais sélectionner fargate.

Étape suivante, le nom de la définition de tâche, je vais l'appeler app, le rôle, je vais sélectionner Aucun.

Et le modèle de réseau, sélectionnez le modèle par défaut.

Et pour la mémoire de la tâche, 0,5 gigaoctets, le CBO.

Donc, je vais sélectionner les versions minimales.

Et le conteneur ici, nous devons ajouter le conteneur que nous venons de copier.

Donc, ce conteneur et le nom du conteneur, il sera aussi app ici, nous devons configurer le port.

Donc, 80 était le port à l'intérieur du conteneur.

Donc, nous devons le mapper ici.

Et nous pouvons ajouter toutes nos configurations.

Mais je n'ajouterai aucune pensée.

Ajoutons cela.

Et nous avons ajouté notre conteneur là.

Et c'est tout, créons cette définition de tâche.

Donc, c'était réussi.

Et maintenant, allons à notre cluster.

Et ici, maintenant, nous pouvons créer notre service.

Donc, cela sera aussi un fargate, nous avons besoin de la définition de tâche que nous avons créée.

Donc, Amazon l'assignera automatiquement, nous avons besoin du nom du service.

Donc, app, donc nous avons beaucoup de apps avec des noms, le nombre de tâches, je vais sélectionner une mais vous pouvez sélectionner deux, cela créera deux conteneurs.

Un, il n'y aura qu'un seul conteneur.

Donc, je vais garder tout au minimum, mais vous pouvez sélectionner deux et tout devrait être correct maintenant.

Donc, allons à l'étape suivante, les sous-réseaux, je vais sélectionner l'une de ces options et aussi assigner une IP publique Oui, l'équilibreur de charge, je vais sélectionner Aucun.

Et l'étape suivante Oh, ici nous pouvons faire un auto-scaling, mais comme c'est un exemple, je ne vais pas faire d'auto-scaling.

Donc, ce sera juste un simple conteneur.

Revue, créer le service.

Donc, tout est créé.

Donc, allons à Voir le service.

Et cliquons ici.

Et le statut est en attente.

Attendons qu'il soit en cours d'exécution et ensuite, une fois terminé.

Nous aurons une IP publique, que nous verrons.

Attendons.

Donc, notre tâche est en cours d'exécution maintenant.

Et nous avons une IP publique pour elle.

Donc, je vais copier cette IP, ou visiter ici.

Et voici notre application.

Donc, c'est ainsi que nous déployons un conteneur Docker sur AWS fargate.

Merci d'avoir regardé cette vidéo.

N'oubliez pas de liker, partager et vous abonner.

Merci.

Donc, je suis connecté à mon portail Azure ici.

Et avant de créer quoi que ce soit, assurez-vous d'avoir installé l'Azure CLI.

Donc, téléchargez la bonne version pour votre machine et suivez les instructions, vous aurez accès à cette commande qui affichera ces options.

Donc, avant de revenir au portail Azure.

Et nous allons créer un registre de conteneurs.

Donc, nous n'avons encore aucun registre de conteneurs.

Donc, créons un registre de conteneurs.

Donc, je vais créer le registre de conteneurs ici, le groupe de ressources, j'ai un groupe de ressources de démonstration ici, que je rassemble simplement le nom.

Le nom du registre, je vais l'appeler app.

Donc, il doit avoir cinq caractères, donc je vais l'appeler myapp.

Oh, déjà des nouvelles pour mon conteneur.

D'accord, conteneur app.

Donc, quel nom n'est pas utilisé.

Donc, mycontainerapp, je vais utiliser ce nom.

Et pour l'emplacement, vous pouvez choisir votre emplacement pour ce SKU, je vais sélectionner la version de base.

Créons-le.

Et nous pouvons créer ce registre.

Et maintenant que nous avons créé notre registre, nous devons également nous connecter.

Donc, tout d'abord, nous devons nous connecter via USB ou comme ceci, c'est la connexion.

Donc, nous devons nous connecter à notre compte ici.

Et nous nous sommes connectés à MC soft Azure.

Donc, comme vous pouvez le voir, cela affiche ces données.

Donc, après nous être connectés, nous devons exécuter cette autre commande.

Donc, comme votre registre de conteneurs Azure, et ici nous avons besoin du nom, qui était qui était app.

Donc, copions-le aussi, oublié la ressource.

Et copions l'URL, qui est celle-ci.

Donc, nous n'avons pas besoin du suffixe.

Donc, connectons-nous.

Donc, cela nous permettra de pousser un conteneur Docker vers Azure.

Donc, nous nous sommes connectés avec succès.

Et maintenant que nous sommes connectés, nous pouvons pousser notre image pour pousser notre image.

Tout d'abord, nous devons la taguer.

Donc, Docker tag, le nom de notre conteneur est app.

Et je vais coller à nouveau cette URL, que j'ai copiée.

Et devons-nous ajouter un slash app.

Donc, c'est notre dépôt ici.

Donc, je rassemble cela.

Et après l'avoir tagué, nous devons le pousser.

Donc, poussons-le.

Et maintenant, il pousse notre conteneur vers le registre de conteneurs Azure.

Donc, attendons que cela soit terminé.

Donc, c'est terminé.

Maintenant, nous pouvons revenir.

Et ici, nous allons dans les dépôts.

C'est notre dépôt app.

Et ici, nous avons notre image.

Donc, c'est notre image.

Et ce que je vais faire ici, c'est que je vais copier ce nom de conteneur, donc je vais copier cela.

Et revenons à l'accueil.

Et créons maintenant une instance de conteneur.

Donc, créons une instance de conteneur.

Je vais sélectionner le même groupe de ressources.

Nous avons besoin du nom du conteneur.

Le nom du conteneur est app et nous devons sélectionner la source de l'image vers le registre de conteneurs Azure.

Et nous avons notre conteneur app.

Donc, nous devons activer l'admin ici.

Donc, cliquons sur en savoir plus.

Et nous devons exécuter cette commande.

Donc, je vais copier cette commande.

Et je vais l'exécuter ici.

Donc, nous avons besoin du nom ici, ou de notre ID directement.

Je ne suis pas sûr si nous avons besoin de mycontainerapp.

Donc, j'ai fait une erreur ici, il devrait être avec un m, pas deux M.

Donc, c'est activé.

Et maintenant, nous pouvons l'utiliser.

Donc, devons-nous rafraîchir ici, je vais rafraîchir.

Et je vais sélectionner ce groupe de ressources, je vais sélectionner app ici, registre, et maintenant il est sélectionné.

Donc, tout est correct, je vais changer la taille ici, je vais garder tout au minimum.

Donc, le point cinq est le minimum.

mémoire.

Donc, je vais sélectionner cela, revoir et créer.

Aussi, je pense, Oh, j'ai oublié quelque chose.

Donc, nous devons aussi aller dans la partie réseau.

Et nous devons mapper le Port 80.

Donc, par défaut, il est automatiquement mappé, donc nous n'avons rien à changer.

Mais si le port de votre conteneur est différent, nous devons sélectionner ici, l'autre port, donc ad est correct.

Et nous n'avons pas besoin de changer autre chose.

Créons-le.

Donc, le déploiement est en cours.

Le déploiement est terminé.

Donc, allons à la ressource.

Et nous avons une adresse IP publique ici.

Donc, nous pouvons copier cette adresse IP.

Et si nous allons à l'adresse IP, nous pouvons voir notre application déployée.

Donc, c'est ainsi que nous déployons un conteneur Docker sur une instance de conteneur Azure.

Merci d'avoir regardé cette vidéo, j'espère que vous aimez, partagez et abonnez-vous.

Merci.

Donc, je suis connecté à ma plateforme Google Cloud maintenant.

Et nous allons utiliser deux services, Container Registry et Cloud Run.

Donc, allons au Container Registry.

Et avant d'ajouter quoi que ce soit ici, nous devons installer le SDK Google Cloud.

Donc, assurez-vous de télécharger le bon installateur pour Mac OS, vous ne le chargez pas ici, aussi pour Windows et Linux, et assurez-vous également de l'ajouter à votre chemin.

Une fois terminé, vous pouvez utiliser G Cloud.

Donc, j'ai déjà mon G Cloud configuré.

Et maintenant, connectons-nous d'abord.

Donc, afin de pousser des conteneurs vers le registre de conteneurs Google Cloud, nous devons d'abord être connectés.

Donc, G Cloud, notre connexion.

Donc, cela se connectera avec notre compte Google Cloud.

Et nous allons tout autoriser.

Et maintenant, nous sommes connectés.

Si nous allons à notre terminal, nous verrons cela, donc je vais l'effacer maintenant.

Et maintenant, nous pouvons pousser notre image vers un dépôt Docker vers le registre de conteneurs.

Donc, tout d'abord, nous devons taguer l'image.

Donc, Docker tag, le nom de l'image est app.

Et nous allons cibler le registre de conteneurs Google Cloud.

Donc, gcr.io slash nous avons besoin du nom du projet.

Donc, si nous allons à notre plateforme cloud, cliquez sur notre projet ici.

Et c'est le nom de mon projet.

Donc, je vais copier cet ID ici.

Et je vais l'ajouter ici.

Donc, c'est notre ID de projet.

Et ensuite, nous avons besoin du nom de notre conteneur.

Donc, cela doit être le même que le dernier.

J'ai parlé de cela et ensuite nous devons le pousser, donc je vais supprimer cela et nous allons le pousser et cela va pousser le conteneur vers notre plateforme Google Cloud.

Donc, attendons que cela soit terminé.

Donc, l'image est poussée.

Maintenant, nous allons voir l'image ici.

Donc, dans le Container Registry, nous avons notre image d'application.

Et allons ici et copions l'URL.

Donc, je vais copier l'URL ici.

Parce que nous en aurons besoin.

Et allons maintenant à Cloud Run.

Donc, ici, nous devons créer un service.

Lorsque vous ajoutez le nom du service, je vais l'appeler app, la région, vous pouvez sélectionner votre propre région, nous avons besoin de l'URL de l'image du conteneur.

Donc, ici, nous pouvons la sélectionner directement.

Et c'est le dernier conteneur que nous avons poussé.

Donc, sélectionnez cela.

Et c'était notre conteneur.

Nous pouvons ajouter quelques paramètres avancés ici comme des variables, des secrets, etc.

Mais la seule chose que nous allons changer, c'est le port.

Donc, le port de notre conteneur est 80.

Donc, je vais mettre ad ici.

Et nous n'avons pas besoin de changer autre chose.

Suivant.

Donc, nous devons autoriser les invocations non authentifiées.

Donc, cela est public.

Et c'est tout.

Donc, créons cela.

Et attendons que cela soit terminé.

Donc, cela devrait être rapide.

Donc, c'est terminé, je ne suis pas sûr pourquoi j'ai fait une erreur ici.

Le port était 76.

Ici, il devrait être 80.

Et nous avons aussi une URL ici.

Si nous allons à l'URL, nous verrons notre application déployée.

Donc, c'était aussi simple.

C'est ainsi que nous déployons une application sur Google Cloud Run.

N'oubliez pas de liker, partager et vous abonner.

Merci.