---
title: Comment j'ai utilisé le crowdsourcing pour aider les opérations de secours
  lors des inondations au Kerala.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-04T19:05:43.000Z'
originalURL: https://freecodecamp.org/news/how-i-used-crowdsourcing-to-help-kerala-floods-rescue-operations-12dc97c9a24b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wWP9CgjPGVglqTU2Arh3Tw.jpeg
tags:
- name: crowdsourcing
  slug: crowdsourcing
- name: Disaster Response
  slug: disaster-response
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment j'ai utilisé le crowdsourcing pour aider les opérations de secours
  lors des inondations au Kerala.
seo_desc: 'By Arnav Bansal

  Overnight, I made a website that let people discover urgent requests


  In August 2018, floods decimated the state of Kerala. One-sixth of its population
  was directly affected. The state incurred property damage worth $3B.

  I’m Arnav, an...'
---

Par Arnav Bansal

#### En une nuit, j'ai créé un site web qui permettait aux gens de découvrir des demandes urgentes

![Image](https://cdn-media-1.freecodecamp.org/images/RTrVKBeZKPcQc5wSd9JCvUgKBNGrPVSM2yut)

En août 2018, des [inondations](https://youtu.be/hzDDYwwDJ1E?t=23s) ont dévasté l'État du Kerala. Un sixième de sa population a été directement affecté. L'État a subi des dommages matériels d'une valeur de 3 milliards de dollars.

Je m'appelle [Arnav](https://twitter.com/itsarnavb), j'ai 18 ans et je viens de Bangalore où j'ai terminé mes études en mars. Pendant les inondations, je suis tombé sur le [Kerala Rescue Project](https://github.com/IEEEKeralaSection/rescuekerala/). Il s'agissait d'un mouvement de développeurs bénévoles résolvant des défis technologiques associés aux inondations du Kerala en utilisant le web.

Le [site web](https://keralarescue.in) offrait des services importants. Il collectait les demandes d'aide des victimes. Il aidait les bénévoles et les sauveteurs à les localiser et à trouver des camps de secours. Il fournissait des visualisations pour les forces d'intervention en cas de catastrophe.

Alors que j'explorais le projet sur GitHub et Slack, j'ai trouvé un problème spécifique que je pensais pouvoir résoudre.

### Trop de demandes

Suite à une inondation massive, la plus importante en 100 ans, il y avait un grand nombre de demandes d'aide.

J'ai vu de nouvelles demandes arriver chaque fois que j'actualisais un point de terminaison de l'API sur le site de secours. Lorsque je l'ai découvert pour la première fois, j'ai passé près d'une demi-heure à lire les demandes des gens.

Elles étaient détressantes. Des demandes concernant des personnes âgées, des malades et des blessés, des femmes enceintes et des nourrissons. Certaines signalant des bâtiments sur le point de s'effondrer ou des eaux de crue montantes. Certaines provenaient de personnes vivant ailleurs, incapables de joindre des parents au Kerala.

**Mais les demandes détressantes étaient noyées dans une mer de demandes qui ne semblaient pas immédiates ou qui contenaient peu de données.**

Et celles-ci n'étaient que celles en anglais. Je ne pouvais pas lire les demandes écrites en malayalam (la langue du Kerala).

Cela m'a amené à me demander : comment les demandes étaient-elles priorisées ? J'ai demandé autour de moi. Effectivement, les gens ont remarqué que c'était un vrai problème.

### Donner un sens aux données

J'ai pensé à deux approches pour déterminer l'urgence des demandes.

#### Traitement du langage naturel (NLP)

Des mots comme « Urgent », « Nourrisson », « Enceinte » ou « Piégé » indiquaient une urgence et pouvaient être utilisés pour classer les demandes.

Mais les données présentaient plusieurs problèmes : les demandes étaient en anglais et en malayalam. Et parfois, le malayalam était écrit avec l'alphabet anglais.

Beaucoup étaient écrites à la hâte.

Certains ont suggéré de traduire les demandes en anglais avant d'appliquer le NLP. Mais la traduction est imparfaite, et j'étais certain que cela ne fonctionnerait pas.

Et enfin, je pensais que l'urgence était largement contextuelle. Le NLP la gérerait-il bien ? L'analyse des sentiments existante peut vous dire si le texte est positif, négatif, heureux ou triste. Mais elle ne mesure pas l'urgence.

Et il n'y avait pas le temps de développer un nouveau modèle. Surtout, étant donné le problème de langue.

#### Crowdsourcing

J'étais certain que les gens consacreraient un peu de leur temps pour identifier les demandes urgentes.

Ils donneraient un sens aux informations suggérant une urgence que les ordinateurs ne sont pas bons à interpréter.

J'imaginais un site web qui récupérerait et afficherait les demandes du site de secours. Les bénévoles évalueraient l'urgence sur une échelle allant de _peu urgent_ à _critique_ (valeurs de 0 à 3), avec une option pour le spam (-1). Ils pourraient ignorer les demandes s'ils ne connaissaient pas la langue.

Alors je me suis mis au travail.

### Mise en œuvre

J'ai d'abord pensé à intégrer la fonctionnalité de crowdsourcing dans keralarescue.in

Le projet était open source. Beaucoup construisaient des outils séparés mais liés sur la même plateforme. Il était logique pour moi de construire directement dessus.

Mais j'avais quelques inquiétudes :

1. Je n'étais pas certain que l'idée fonctionnerait. Je ne voulais pas laisser un poids mort sur la plateforme dont beaucoup dépendaient.
2. La plateforme était écrite en Django, utilisant PostgreSQL. Je n'ai que peu de familiarité avec ceux-ci, et je ne voulais pas expérimenter-apprendre.
3. Le système de révision entraverait les itérations rapides.

J'ai donc décidé de créer mon outil indépendamment de la plateforme principale.

Si cela fonctionnait, je leur ferais fusionner mes données. Si cela échouait ? Eh bien.

#### Huile de minuit

Il était déjà environ 1 heure du matin. Je me suis fixé pour objectif d'avoir mon site en ligne dans les cinq heures, afin qu'il soit prêt lorsque les gens se réveilleraient.

Mon idée était d'utiliser le point de terminaison de l'API de keralarescue.in pour afficher les demandes d'aide. Bien sûr, je l'ai mis en cache de mon côté, afin de ne pas surcharger le site principal.

J'ai commencé à développer la plateforme. J'ai commencé par créer des modèles de données. Ensuite, j'ai travaillé sur les fonctions et les points de terminaison de l'API. Enfin, j'ai commencé à travailler sur le front-end. Ma stack comprenait Firebase et VueJS, pour des raisons de prototypage rapide.

Je prévoyais d'utiliser les [intervalles de confiance de Wilson](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Wilson_score_interval) pour évaluer les scores. (Utilisés pour le [tri par confiance sur Reddit](https://medium.com/hacking-and-gonzo/how-reddit-ranking-algorithms-work-ef111e33d0d9)) Ils représentent une amélioration par rapport aux simples moyennes, car ils tiennent compte du nombre de notations.

Mais j'étais pressé, alors j'ai décidé de mettre cela en œuvre plus tard. Sans données, cela n'était pas très utile.

« Simplicité » est un cliché. Mais j'ai trouvé que cela fonctionne. Les choses semblaient s'améliorer lorsque je réduisais la complexité. J'ai écrit des modèles de données simples. J'ai abandonné reCAPTCHA et l'authentification, en faisant l'hypothèse que je n'attirerais pas d'utilisateurs malveillants.

Vers 8 heures du matin, mon prototype était prêt. Et j'étais prêt à m'endormir. J'ai posté un lien sur GitHub et je suis allé me coucher juste au moment où la première visite arrivait sur Google Analytics.

Je n'ai eu aucun mal à m'endormir.

### Faire adhérer les gens

J'avais des utilisateurs.

Quand je me suis réveillé à midi, j'ai vérifié les analyses avant toute autre chose. ~30 visites. Et j'avais deux utilisateurs actuellement en ligne. De l'État du Kerala. *Woah*.

Les retours étaient positifs. Et j'avais recueilli pas mal de données. J'ai continué à améliorer ma plateforme tout au long de la journée.

* **J'ai supprimé l'option spam.** J'ai appris que les gens n'étaient pas sûrs des demandes qui étaient du spam. Beaucoup manquaient d'informations. Celles-ci pouvaient être des demandes parfaitement valides de personnes pressées, ou de personnes qui n'étaient pas à l'aise avec la technologie.
* **J'ai implémenté le score de Wilson.** J'ai créé un point de terminaison API qui retournait la valeur de confiance entre 0 et 1 basée sur toutes les notations des utilisateurs recueillies jusqu'à présent. L'idée était de faire en sorte que keralarescue.in utilise ce point de terminaison pour mettre à jour son jeu de données périodiquement. La valeur pouvait être utilisée pour trier et trouver les demandes les plus urgentes.
* **J'ai ajouté une page pour afficher les demandes urgentes.** Je voulais rendre cet outil utile le plus rapidement possible.

Vers 16 heures, j'ai décidé de l'annoncer sur Slack et GitHub.

Cela s'est avéré être un point d'inflexion, et pendant les heures suivantes, le site avait 20 à 30 utilisateurs en ligne. Ils venaient de toute l'Inde, et aussi des États-Unis. Les utilisateurs du Kerala ont continué à travailler tard dans la nuit, triant les demandes à 2 heures du matin.

J'ai remarqué que les gens étaient plus lents à noter les demandes que je ne l'avais anticipé.

Le lendemain soir, j'apprendrais pourquoi.

#### Le groupe de triage

Le lendemain, j'avais terminé la plupart du travail de développement. Beaucoup de gens ont commencé à me contacter. Ils aimaient mon projet, surtout l'interface simple.

En soirée, j'ai reçu un message direct sur Twitter de quelqu'un nommé Nishanth, me demandant si mon site web pouvait être utilisé pour **trier** les demandes. Nous avons eu un appel, et j'ai décrit comment les foules pouvaient aider à déterminer l'urgence des demandes.

Il m'a ajouté à un groupe WhatsApp de cent membres. Il s'avère que ces personnes formidables utilisaient mon site web d'une manière complètement différente.

Ils appelaient activement les demandeurs et obtenaient des mises à jour sur leur situation. Ils évaluaient l'urgence non pas sur le contenu textuel, mais en **conversant réellement avec les personnes affectées**. *WOAH*.

J'ai réalisé que ma base de données contenait des informations plus précieuses que je ne l'avais pensé. Nous aidions directement les bénévoles à atteindre les victimes. Des messages me remerciant pour mon travail affluaient sur mon téléphone.

### Perte de la source de données

Dans le projet principal, les gens se préparaient pour un grand événement. Le gouvernement du Kerala allait annoncer publiquement le site de secours. Un trafic important était à prévoir.

Le site principal offrait de nombreuses fonctionnalités. Des cartes thermiques des demandes, des dons, des camps de secours, la coordination des bénévoles, des annonces, vous voyez le genre.

J'ai développé un sérieux respect pour l'équipe dev-ops, car lorsque le trafic a frappé le site, ils ont travaillé toute la nuit pour le mettre à l'échelle.

Tout semblait fonctionner, sauf une chose : **ils ont supprimé le point de terminaison de l'API dont je dépendais.**

Maintenant, je savais que le point de terminaison que j'utilisais ne serait pas scalable. Il retournait toutes les demandes à la fois. Vers la fin de sa vie, il retournait un jeu de données de 10 Mo. Il était fait pour le développement, et non pour une utilisation en production.

Heureusement, mon site avait déjà un mécanisme de cache, donc il est resté opérationnel.

J'ai pris contact avec l'équipe. Ils construisaient une alternative. Mais ils avaient encore beaucoup à construire, alors j'ai essayé de ne pas insister.

Mon site a continué à fonctionner sans problème, et les groupes de triage (il y en avait plusieurs à ce stade) ont continué à opérer, bien que sans nouvelles données.

### Nouvelles fonctionnalités ?

À ce stade, j'ai commencé à réfléchir à des moyens de m'améliorer.

Le problème immédiat était l'afflux de grandes quantités de nouvelles données lorsque la route alternative serait disponible. Et quelles autres améliorations pourrais-je apporter ?

J'ai réfléchi à certaines fonctionnalités.

* **Cohortes basées sur le temps** : Assigner un certain pourcentage d'utilisateurs pour gérer exclusivement les nouvelles demandes. De même, assigner des utilisateurs à des sections de demandes plus anciennes.
* [**Filtres de Bloom**](https://www.jasondavies.com/bloomfilter/) : Ils sont un moyen efficace en espace pour tester l'appartenance à un ensemble. Je pourrais utiliser des filtres de Bloom pour tant de choses : m'assurer que nous avons épuisé toutes les demandes et limiter les visites répétées.
* **Mises à jour de statut** : Je pourrais construire une fonctionnalité pour que les gens mettent à jour le statut des demandes. C'était une construction triviale, et les gens la demandaient. Mais les personnes travaillant sur la plateforme principale m'ont dit qu'ils en construisaient déjà une.
* **Websockets** : Je pourrais diffuser de nouvelles demandes sur le site web en temps réel dès leur arrivée. Combiné avec les mises à jour de statut et les cohortes temporelles, nous obtiendrions des informations détaillées sur les demandes dès leur arrivée.

J'avais beaucoup d'idées concurrentes, et je n'étais pas sûr de ce qui pouvait être mis en œuvre à temps pour être utile.

### Conclusion

Le point de terminaison de l'API est revenu le lendemain. Il était maintenant paginé, retournant 300 demandes à la fois. J'ai rapidement écrit un script pour télécharger et maintenir un cache local en utilisant la nouvelle API.

Le nombre d'appels et de messages que je recevais a atteint un nouveau sommet. N'ayant jamais été employé auparavant, c'était un nouveau terrain. Les développeurs travaillant sur la plateforme principale me contactaient. Ils travaillaient à intégrer les données crowdsourcées — à la fois les évaluations d'urgence et les mises à jour de statut que nous collections.

À la fin de la journée, les gens des groupes de triage ont ressenti un changement.

La plupart des victimes qu'ils appelaient rapportaient avoir été secourues récemment. Il s'avère que les missions de secours sur le terrain avaient commencé.

C'était une excellente nouvelle. Vers 5 heures du matin, j'ai eu un appel avec Nishanth. Il était en contact avec des responsables gouvernementaux supervisant les opérations de secours. Nous avons emballé les données du site web et des feuilles de calcul, et nous les leur avons remises.

Alors que j'écris ceci, les victimes des inondations ont été secourues et transportées vers des camps de secours. Il y a de nouveaux défis impliquant la logistique entre les camps et l'aide arrivant de tout le pays.

### Leçons

* **Simplicité** : Beaucoup de gens m'ont envoyé des messages pour dire qu'ils aimaient mon site. Je ne suis pas designer, mais ma décision de garder l'UX simple a aidé les gens à adhérer plus rapidement.
* **Le calcul est bon marché** : Tout cela était hébergé sur Google Cloud Platform. Cela m'a coûté moins d'un dollar, couvert par mes crédits de niveau gratuit. Si j'avais su à quel point c'était bon marché, j'aurais construit une application lourde en backend.
* **Pivotement** : J'aurais aimé avoir complètement pivoté vers une plateforme de triage détaillée. Les bénévoles ont trouvé une solution de fortune, mais avec le recul, j'aurais préféré livrer la plateforme avec ces fonctionnalités.
* **Les réseaux sont importants** : Les gens voulaient aider. Le groupe initial de 30 personnes est passé en deux jours à un groupe de 230, alors que les gens faisaient appel à leurs amis et connaissances. Des gens se sont joints depuis le Kerala, le reste de l'Inde et du monde entier.

J'ai rencontré beaucoup de gens formidables. J'ai appris beaucoup, technique et autre. À travers tout cela, le sentiment le plus incroyable était celui d'être sur la même longueur d'onde que des milliers d'autres personnes.

Si mon travail mérite un article, le projet dont j'ai fait partie mérite un livre.

Quant à moi, je prends contact avec des personnes impliquées dans la réponse aux catastrophes pour apprendre de leur expérience et de leur expertise.

Un peu plus sur moi : je prends une année sabbatique pour me plonger dans l'économie crypto. J'ai acquis des compétences en développement web en 10e année, tout en organisant un hackathon à l'école.

J'envisage de développer un projet basé sur cela, mais avec de nombreuses autres idées que mes amis et moi avons eues depuis.

* _Ann Thomas, une bénévole des groupes de triage, a écrit sur son expérience [ici](https://mommysuitup.blogspot.com/2018/08/my-tryst-with-triage.html)_
* _Merci au Dr. Harikrishnan, au Dr. Nishanth, à Ajit Chandran, à Prasad Pillai, qui ont aidé à organiser les groupes de triage_