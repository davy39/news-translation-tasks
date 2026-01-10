---
title: Comment j'ai lancé mon premier projet SaaS en parallèle d'un emploi à temps
  plein
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-19T18:33:43.000Z'
originalURL: https://freecodecamp.org/news/how-i-shipped-my-first-saas-side-project-while-working-full-time-5ad33cf89121
coverImage: https://cdn-media-1.freecodecamp.org/images/0*VzFah4Lrwc4VuYsv.JPG
tags:
- name: Entrepreneurship
  slug: entrepreneurship
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment j'ai lancé mon premier projet SaaS en parallèle d'un emploi à temps
  plein
seo_desc: 'By Tigran Hakobyan

  This is my personal story of how I shipped my very first SaaS side-project while
  working full-time at Buffer. The goal of this article is to inspire you. If you’re
  someone like me who has a full-time job and wants to build a profit...'
---

Par Tigran Hakobyan

Voici mon histoire personnelle de la façon dont j'ai lancé [mon tout premier projet SaaS en parallèle](http://www.cronhub.io) tout en travaillant à temps plein chez Buffer. Le but de cet article est de vous inspirer. Si vous êtes comme moi, avec un emploi à temps plein et que vous souhaitez créer une entreprise secondaire rentable comme source de revenus, alors cette histoire pourrait vous parler.

Avec cet article, je veux montrer comment je n'ai pas "hustlé" ou surtravaillé et que j'ai tout de même réussi à lancer un vrai produit SaaS.

Je suis développeur web et j'ai la chance, en plus de jouer au football pendant mon temps libre, d'aimer coder et construire des projets web pour le plaisir. Récemment, j'ai créé [Booknshelf](http://booknshelf.com/) qui aide de nombreuses personnes à organiser leurs livres en ligne. Bien que travailler à temps plein ait un grand impact sur ma croissance en tant qu'ingénieur, certaines des compétences de développeur que j'ai acquises proviennent de mes projets personnels.

Ce n'est que l'année dernière que j'ai commencé à penser à avoir une source de revenus différente de mon emploi à temps plein. L'idée de dépendre d'un seul salaire est un peu effrayante. Je savais que j'avais les compétences et la passion pour trouver une solution.

J'ai décidé que je voulais créer une entreprise, probablement une entreprise en ligne compte tenu des compétences que je possède. L'autre déclencheur de ces pensées était que je voulais vivre et apprendre ce que signifie créer une entreprise. Je n'avais jamais dirigé d'entreprise de ma vie, alors je voyais cela comme une grande opportunité d'apprentissage, un chemin sur lequel je pourrais acquérir des compétences que je ne possède pas actuellement. La pire chose qui pourrait arriver serait que si j'échouais, je finirais tout de même avec de l'expérience et des tonnes d'apprentissages.

### Idée

Comme vous l'aurez peut-être deviné, la première chose que j'ai faite en tant que développeur a été de commencer à réfléchir à des idées. Les idées n'ont jamais été un problème pour moi, mais déterminer quelles idées étaient adaptées l'a toujours été. Cette fois, j'ai décidé d'essayer une approche différente et de vraiment réfléchir à l'idée avant de me lancer. Il y avait certains critères que je voulais appliquer à chaque idée.

* Je voulais résoudre un vrai problème, probablement quelque chose que je rencontrais personnellement
* Cela devait être pour un marché que je connais bien
* Cela ne devait pas être une nouvelle idée (ce n'est pas quelque chose qui va changer le monde)
* Cela pourrait devenir une entreprise

La règle d'or de toute idée est qu'elle doit résoudre un problème que les gens rencontrent. Dans le passé, j'avais ajouté tant d'idées à mes notes — il s'agissait donc de visiter le réservoir d'idées que j'avais sauvegardées.

![Image](https://cdn-media-1.freecodecamp.org/images/QcVMCLohkisTur3kYm5cQA4jBWJ-GUhhvuFz)

Je savais dès le début que je serais probablement plus réussi si je construisais quelque chose pour les développeurs, car je connais bien ce marché et la plupart de mes amis proches et de mes abonnés en ligne sont dans le domaine de la technologie. Je pourrais utiliser mon réseau et mon audience pour valider mon idée et obtenir des retours solides avant de m'engager dans quoi que ce soit.

Cela a vraiment filtré toutes mes idées pour n'en garder qu'une liste de 2 à 3 choses sur lesquelles je pourrais travailler. L'une des idées était quelque chose à laquelle je revenais sans cesse. C'était quelque chose que j'avais rencontré à la fois chez Buffer et pendant le travail sur mes précédents projets secondaires : une manière simple de surveiller les tâches cron planifiées.

Puisque l'un des domaines que je gère au travail est l'infrastructure de données analytiques, j'ai exécuté une douzaine de tâches cron en arrière-plan pour collecter les données analytiques quotidiennes pour nos clients. Cela doit être à jour. Le service de surveillance [Datadog](https://www.datadoghq.com/) que nous utilisons est vraiment excellent, mais il est principalement conçu pour surveiller les services ou serveurs continus. Je voulais un tableau de bord simple où je pourrais voir la liste de toutes mes tâches cron, leurs statuts et leurs journaux. Chaque jour, recevoir un rapport de toutes les tâches exécutées pour savoir que tout est sur la bonne voie.

Après avoir choisi cette idée, je voulais voir s'il existait des solutions sur le marché. Si c'était le cas, c'était un bon signe qu'il y avait une demande pour certains outils.

En fait, il y en avait quelques-unes sur le marché avec différents plans payants. Je ne voulais pas nécessairement construire quelque chose de complètement nouveau, car si je l'avais fait, il m'aurait été beaucoup plus difficile de définir et de valider le marché. Toutes les solutions existantes avaient des plans payants, donc je savais que les gens paieraient pour cela. Le prochain objectif était de valider si ma réflexion était correcte en construisant et en lançant le MVP initial.

### MVP

J'ai passé 2 mois à construire la version initiale de Cronhub (oui, je lui ai donné un nom). Quelque chose de viable que je pourrais envoyer à une poignée de mes amis et abonnés Twitter pour essayer. Pour le MVP, je voulais quelque chose de très simple mais aussi suffisamment précieux pour que les gens paient pour cela. Je sais que vous pourriez penser que deux mois est un long temps pour construire un MVP, mais je n'ai pas pris l'approche traditionnelle du "hustle". Au lieu de cela, j'ai :

* Travaillé seulement 1 à 2 heures chaque jour
* Dormi 8 heures chaque jour
* Regardé Netflix chaque fois que je le voulais
* Complètement reposé le week-end
* Utilisé la stack technologique avec laquelle je me sentais le plus à l'aise

Puisque j'ai un emploi à temps plein, je travaillais sur Cronhub généralement de 19h à 20h30. Je pourrais aussi travailler tôt le matin, mais je passe la plupart de mes matins à la salle de sport. Il y avait des jours où je me sentais mentalement très épuisé après le travail et je prenais les choses facilement, mais la plupart du temps je respectais ma routine.

Je savais que si je voulais terminer ce projet, je devais garder le rythme et m'engager chaque jour, même si c'était un petit changement (cela pouvait être un commit d'une seule ligne). La cohérence a toujours été super utile pour moi pour rester sur la bonne voie et livrer. J'ai utilisé Trello pour décomposer les tâches de mon projet en petites étapes.

![Image](https://cdn-media-1.freecodecamp.org/images/5XEJNRsYL6sFibO6DJF1oJt-7AEYt4b5pvf-)

J'ai essayé de rendre chaque tâche très petite pour pouvoir commencer et finir en une seule journée. Garder les tâches petites m'a aidé à livrer plus rapidement et à voir mes progrès quotidiens. Quand vous voyez des progrès, cela vous motive beaucoup et vous continuez. Je pense que c'est un tour de l'esprit. Travailler sur de grandes tâches vous ralentit et finalement vous abandonnez parce que vous vous ennuyez et vous voulez passer à autre chose.

Je n'ai jamais travaillé la nuit. Je suis allé me coucher vers 22h30 chaque jour et je me suis réveillé à 7h. Avoir un sommeil adéquat est ma priorité numéro un. Cela définit l'énergie mentale que j'ai pendant la journée et je ne peux pas la sacrifier. En plus de bien dormir, j'ai décidé de passer la plupart de mes week-ends à faire quelque chose de complètement différent comme jouer au football, regarder des films ou passer du temps avec des amis et de la famille. Même si j'aime coder, je sais qu'il est facile de s'épuiser. Les week-ends m'ont aidé à rafraîchir mon cerveau.

Je pense qu'en tant que développeur, vous voulez toujours utiliser les technologies les plus chaudes et les plus cool. Et c'est bien. Je veux cela aussi. Cependant, mon objectif était différent et je voulais construire et lancer Cronhub aussi vite que possible avec les technologies que je connaissais déjà. Je suis resté concentré sur mon objectif et j'ai utilisé Laravel et Vuejs. Cronhub est une application monopage utilisant Laravel pour le backend.

### Lancement de la version bêta fermée

Le 20 février, j'ai terminé le strict minimum de Cronhub et j'étais prêt à inviter le premier groupe d'adoptants précoces à l'essayer. Après mon tweet, environ 20 à 25 personnes m'ont contacté sur Twitter pour demander une invitation. Les retours que j'ai eus d'eux étaient super précieux.

![Image](https://cdn-media-1.freecodecamp.org/images/VLVa11ILNBYcGbe75C2rxfjabicFmgEAY9ea)

Il y avait quelques bugs signalés et de grandes suggestions de fonctionnalités que j'ai ajoutées à mon document de feedback. Garder une trace des retours des utilisateurs est une étape importante, car cela aide à identifier les modèles évidents auxquels vous pouvez vous référer lorsque vous prenez des décisions sur le produit.

Dans l'ensemble, la première impression et les retours étaient encourageants. Maintenant, je devais continuer à améliorer le produit et le préparer pour le premier lancement public. J'ai prévu le premier lancement public dans un mois.

### Lancement public

Après trois mois, je lance mon premier projet SaaS en parallèle au public. Youpi !

Bien sûr, je suis nerveux et je ne sais pas si cela va fonctionner ou non. Cependant, je sais que cela me rapproche d'un pas de mon objectif. L'objectif de faire de Cronhub une entreprise en ligne rentable où je peux apprendre et découvrir tous les secrets cachés de la gestion d'une entreprise. Après tout, quelle est la pire chose qui pourrait arriver ? J'apprendrais tellement !

Je sais peut-être que je suis trop concentré sur la rentabilité, mais après avoir construit quelques projets secondaires gratuitement dans le passé, je savais qu'il était temps pour moi de prendre mon temps un peu plus au sérieux. Le temps est l'actif le plus précieux que je possède et je veux le dépenser consciemment. Construire un produit payant est beaucoup plus motivant et cela vous pousse vers l'avant. De plus, maintenir des projets secondaires gratuitement est coûteux — je le sais par expérience.

### Leçons apprises

Les trois derniers mois ont été formidables pour la réflexion ainsi que pour évaluer ce qui a bien fonctionné et ce qui n'a pas fonctionné. Chaque fois que je construis un nouveau projet, c'est une nouvelle expérience d'apprentissage. Chaque projet est unique et nécessite un processus de réflexion différent autour du produit. En tant qu'ingénieur produit, je veux développer mon état d'esprit produit et cela aide.

Dans l'ensemble, j'ai appris de nombreuses leçons qui m'ont vraiment aidé à démarrer et à lancer une idée. Je veux partager les plus importantes avec vous.

* **Résoudre un problème que vous rencontrez personnellement**. C'est si important, car essentiellement vous construisez le produit pour vous-même, en vous gardant toujours à l'esprit. Cela rend beaucoup plus facile la prise de bonnes décisions sur le produit. Vous savez quelles questions vous devez poser et les chances sont plus grandes que vous posiez les bonnes questions.
* **Gardez vos tâches petites**. Lorsque vous décomposez votre projet en morceaux, essayez de les rendre plus petits. Une bonne façon de mesurer la taille de la tâche est de vous demander "Puis-je faire cette tâche en une journée ?" Si la réponse est "Non", alors c'est probablement une grande tâche et vous pouvez la décomposer davantage.
* **Dormez bien et reposez-vous**. Je ne peux pas assez insister sur l'importance d'un sommeil adéquat. Vous n'avez pas besoin de travailler la nuit. Concentrez-vous sur les progrès incrémentiels et les petits engagements quotidiens. Si vous ne prenez pas soin de vous, vous vous fatiguerez bientôt et finirez par abandonner.
* **Choisissez un marché que vous connaissez bien**. Je suis développeur et je connais bien ce marché. Je sais ce qu'il faut pour être développeur et comment les équipes de développeurs collaborent. Cela me donne un sens des choses qui fonctionneront et ne fonctionneront pas dans ce marché. Bien sûr, je peux encore me tromper, mais les chances sont beaucoup plus petites.
* **Parlez de votre projet**. C'est un défi pour moi et je m'adapte encore à cela. Je n'aime pas vraiment parler de moi. J'aime plus écouter. Ce n'est pas facile pour moi de parler du projet que je construis, car je suis un peu timide et je ne veux pas donner l'impression que je parle constamment de moi. Cependant, je sais que je dois faire connaître mon projet et le commercialiser. C'est ainsi que les autres le découvriront au début. Cet article en est un exemple.

### Pour conclure

Merci beaucoup d'avoir lu. J'espère que vous avez apprécié cette histoire et appris au moins une chose. J'adorerais avoir de vos nouvelles, alors n'hésitez pas à commenter avec vos questions. Vous pouvez me contacter sur [Twitter](https://twitter.com/@tiggreen) ou [m'envoyer un email](mailto:tigran@cronhub.io).

Si vous êtes développeur ou faites partie d'une équipe qui utilise des tâches cron, vous pouvez essayer [Cronhub](http://www.cronhub.io/) gratuitement. Utilisez le coupon "indiehackers" pour obtenir 20 % de réduction si vous passez au plan "Développeur".

[Cronhub est sur PH aujourd'hui](https://www.producthunt.com/posts/cronhub) si vous voulez me soutenir :)

Continuez à livrer — Tigran

*Initialement publié sur [www.indiehackers.com](https://www.indiehackers.com/@tigran/how-i-shipped-my-first-saas-side-project-while-working-full-time-42862e847b).*