---
title: Comment votre startup peut exploiter une infrastructure de qualité professionnelle
  pour moins de 200 $/mois
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-11-29T01:52:02.000Z'
originalURL: https://freecodecamp.org/news/how-your-startup-can-leverage-production-grade-infrastructure-for-less-than-200-month-15c3724038b4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*g1NvCuz2d_TnIWfp4Lj4Mw.jpeg
tags:
- name: Devops
  slug: devops
- name: SaaS
  slug: saas
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment votre startup peut exploiter une infrastructure de qualité professionnelle
  pour moins de 200 $/mois
seo_desc: 'By Jean-Paul Delimat

  Before you can launch a new service, you need infrastructure. You want reliability,
  scalability, and many other -ilities. But you don’t want to break the bank.

  I’ve gone through the process of launching several new services over ...'
---

Par Jean-Paul Delimat

Avant de pouvoir lancer un nouveau service, vous avez besoin d'une infrastructure. Vous voulez de la fiabilité, de la scalabilité et bien d'autres qualités. Mais vous ne voulez pas vous ruiner.

J'ai lancé plusieurs nouveaux services au cours des dernières années. À chaque fois, j'ai exploré les options disponibles.

Le but de cet article est de vous aider à vous concentrer sur la valeur que votre solution apporte à vos utilisateurs, tout en minimisant le temps et l'argent passés à vous passionner pour l'infrastructure.

Nous utiliserons des services d'hébergement clés en main pour tout, et l'objectif est que la facture soit inférieure à 200 $/mois.

Notez que je n'ai aucune affiliation — ni ne détiens aucune part — dans les produits ou services que je recommande dans cet article. J'aime simplement ce qu'ils font.

Commençons. Voici ce dont vous aurez besoin :

* Une API hautement disponible
* Une application web (sauf si votre service est purement une API ou est uniquement consommé dans une application mobile, un chatbot, etc.)
* Stockage de fichiers
* Deux environnements : un pour les tests et les démonstrations, et un pour la production
* Des outils pour surveiller votre plateforme de production
* La capacité de mettre à l'échelle dynamiquement vos serveurs de production

### Production VS Staging

Vous aurez besoin de deux environnements : un de production, que vos clients utiliseront réellement, et un de "staging", que votre équipe utilisera pour les tests et potentiellement pour démontrer des fonctionnalités bêta aux clients.

Le staging doit nécessiter une configuration minimale pour exécuter vos applications. Vous ne devriez pas avoir à vous soucier des tests de charge pour cela.

Votre environnement de production aura tous ses services équilibrés en charge, avec au moins deux instances de tout pour des raisons de fiabilité. Dans un instant, nous aborderons quelques outils basiques — mais complets — qui peuvent vous aider à atteindre une surveillance 24/7.

### Hébergement Back End

Je vous recommande d'héberger votre API back-end sur Heroku. Il fonctionne avec la plupart des langages. Vous pouvez consulter la liste complète des langages pris en charge [ici](https://www.heroku.com/languages). Notez que bien qu'ASP.NET ne soit pas encore officiellement pris en charge, il existe des [build packs](https://github.com/friism/heroku-buildpack-mono) open source qui rendent cela possible.

Bien que certains développeurs puissent soutenir que les instances AWS EC2 brutes sont moins chères que les dynos Heroku, cela n'est vrai que lorsque l'on regarde le coût du serveur. Comme Heroku est beaucoup plus rapide à configurer et s'intègre plus facilement avec des services supplémentaires, vous économiserez des heures de travail de développement, ce qui devrait plus que compenser la différence de prix.

Commençons par créer un pipeline Heroku pour votre API avec deux étapes : staging et production. Vous déployez en poussant votre code vers l'application de staging. Ensuite, une fois que vous l'avez testé, vous "promouvez" une version du staging vers la production. Ce processus aidera à empêcher les déploiements défectueux d'atteindre vos serveurs de production — et finalement vos clients.

Votre pipeline ressemblera à ceci (lire plus de détails [ici](https://devcenter.heroku.com/articles/pipelines)):

![Image](https://cdn-media-1.freecodecamp.org/images/5URranzFELOtsqWxA1nmMtwzlM0h8fCTAl15)

Je vous recommande de commencer avec :

* 1 dyno hobby à 7 $/mois pour le staging
* 2 dynos standard-1X pour la production à 25 $/mois chacun

**Coût : 57 $/mois**

### Hébergement de la Base de Données

Si vous utilisez PostgreSQL, utilisez simplement le service de Heroku pour cela. Cela sera plus cohérent en termes de réseau, et vous aurez une seule ligne de facturation au lieu de deux.

Pour le cas plus générique, utilisez [Compose](http://www.compose.com). Les plans de ressources les plus bas sont plus que suffisants pour le stade précoce. Ajustez les ressources "style curseur" selon les besoins.

![Image](https://cdn-media-1.freecodecamp.org/images/hFhwW9Uzlj2M6Ke5uWY8aZjjiGbODtajIe2R)

Compose couvre les incontournables : basculement des nœuds, sauvegardes quotidiennes, chiffrement SSL et un panneau de surveillance de base.

Vous pourriez exécuter les bases de données de staging et de production sur un seul "déploiement" dans Compose. Mais pour garder vos données de production isolées et protégées contre la corruption par du code non testé, vous devriez utiliser deux bases de données séparées.

Pour les coûts, nous prenons MongoDB comme référence à 31 $/mois par déploiement (PostgreSQL serait à 27 $/mois).

**Coût : 62 $/mois**

Une note rapide sur l'utilisation de [mlab pour l'hébergement MongoDB](https://mlab.com) : Nous avons également commencé avec mlab. Nous avions un ensemble de réplicas dédié de 2 nœuds avec 1,7 Go de RAM et 40 Go SSD. Le tout pour le prix de 260 $/mois (180 $ pour le cluster lui-même et 80 $ juste pour activer SSL).

Le service était bon — surtout leur composant de surveillance, [telemetry](http://docs.mlab.com/monitoring/).

Mais après quelques mois de fonctionnement et quelques milliers d'utilisateurs, tous les graphiques montraient toujours moins de 10 % de consommation. Le cluster était surdimensionné et le serait pour quelque temps. Nous avons donc migré vers Compose et avons ajusté progressivement les ressources pour réduire les coûts.

### Hébergement Front End

Je recommande d'utiliser [Netlify](https://www.netlify.com/). C'est assez simple :

* connectez-vous avec votre compte BitBucket/GitHub/GitLab
* sélectionnez le dépôt et la branche à déployer
* définissez votre commande de build et le dossier de build que vous souhaitez servir

Pousser vers la bonne branche Git déclenchera votre build sur les serveurs de Netlify, puis le déployera automatiquement sur leur CDN. Vous pouvez lire plus sur le fonctionnement de tout cela [ici](https://www.netlify.com/docs/continuous-deployment/).

Il y a deux étapes supplémentaires :

* pointez votre DNS vers votre URL Netlify en utilisant un enregistrement CNAME
* activez SSL dans le panneau Netlify. Il provisionnera et déployera automatiquement un certificat TLS Let's Encrypt en quelques minutes.

Ensuite, créez des projets comme suit :

* un pour l'application de staging sur une branche git non-master
* un pour l'application de production pour votre branche git master

Utilisez le plan gratuit pour la plateforme de staging et le plan à 9 $/mois pour la plateforme de production. Vous passerez rapidement au plan à 49 $/mois pour intégrer votre équipe. Mais ce n'est pas nécessaire au début. Lorsque vous atteindrez des millions d'utilisateurs dans le monde, vous pourrez à nouveau mettre à niveau pour utiliser le CDN Geo-IP.

**Coût : 9 $/mois**

### Hébergement de Fichiers

Pour l'hébergement de fichiers, je recommande AWS S3 (Simple Storage Service). Créez deux buckets — un pour le staging et un pour la production.

Le contenu est distribué via le CDN AWS, et les données peuvent être stockées et récupérées de manière sécurisée. Vous trouverez plus de détails [ici](http://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html) sur la manière de configurer les buckets de manière sécurisée.

Les premiers 5 Go (maintenant même 15 Go, je pense) sont gratuits. Ensuite, le coût est de 0,03 $ par Go (au moins pour leur emplacement UE/Irlande). Donc, au début, vous n'aurez peut-être même rien à payer.

**Coût : 0 $/mois**

En aparté, je vous recommande d'envoyer les données directement à AWS S3 depuis votre application web pour alléger la charge sur votre API. Il existe de nombreux articles sur le web expliquant comment faire cela de manière sécurisée.

### Domaine et SSL

Obtenez un nom de domaine, qui pour la plupart des domaines de premier niveau coûtera moins de 50 $/an.

Ensuite, vous pouvez générer des certificats pour tous vos endpoints en utilisant [Let's Encrypt](https://letsencrypt.org/). Il fournit des certificats SSL activés par CA — qui sont approuvés par les principaux navigateurs — gratuitement.

**Coût : 50 $/an**

### Outils de Surveillance

Surveiller votre plateforme de production est essentiel. Vous devez savoir quand des erreurs se produisent pour pouvoir les corriger rapidement. Les utilisateurs ne feront pas l'effort de signaler les petits problèmes, mais leur impression de votre service sera néanmoins dégradée.

Une surveillance complète nécessite :

* Des logs API rotatifs avec détection proactive des lignes d'erreur
* Un rapport actif des exceptions et erreurs côté client et serveur
* Une surveillance de l'uptime
* Des métriques de performance sur votre API et votre base de données, afin de savoir quand mettre à l'échelle
* Un endroit central pour signaler toutes les erreurs afin de pouvoir agir rapidement

#### Slack

Vous pouvez utiliser Slack pour agréger tous les rapports d'erreur dans un seul hub de communication. Slack est conçu pour les équipes, mais si vous travaillez seul sur votre projet, ces outils seront votre équipe.

Créez un compte sur Slack et un canal appelé _#prod-errors_. Vous configurerez tous vos autres services pour signaler les erreurs sur Slack.

Une fois que vous aurez installé chaque application Slack des services et activé ses notifications pour le bureau et le mobile, vous serez prêt à partir.

C'est la version startup de la surveillance 24/7.

#### Logging

Je recommande [Papertrail](https://papertrailapp.com/) pour la gestion des logs. Il fournit :

* une console web simple pour les logs de tous vos dynos API
* une sauvegarde quotidienne de vos logs dans un emplacement de stockage séparé
* une configuration d'alerte, pour vous avertir lorsque nécessaire

Voici à quoi cela ressemble :

![Image](https://cdn-media-1.freecodecamp.org/images/gq3IJWMuYTkieZXj8BLibE-5QG0CakpXQEgc)

Pas très sexy au premier abord, mais au final, l'UX est proche d'une vraie console de serveur, donc cela fait le travail.

Ajoutez Papertrail comme un add-on pour vos applications Heroku de staging et de production. Utilisez le plan gratuit pour la plateforme de staging. Utilisez le plan "Fixa" à 7 $/mois pour la plateforme de production afin d'obtenir 50 Mo/jour de logs et un historique d'un an.

Configurez une alerte Papertrail pour pousser les lignes d'erreur vers votre canal Slack _#prod-errors_.

Faites attention. Les logs sont poussés de vos dynos vers les add-ons via un composant appelé [logplex](https://devcenter.heroku.com/articles/logplex). Si vous avez un algorithme qui produit des milliers de lignes en quelques millisecondes, logplex les abandonnera.

**Coût : 7 $/mois**

Alternatives : Vous pouvez brancher d'autres outils en un clic sur Heroku. Voir la liste complète [ici](https://elements.heroku.com/addons#logging).

Vous pouvez ajouter et supprimer des add-ons de logging sans redémarrer votre application, donc c'est assez sûr de jouer avec. Vous pouvez même tester plusieurs solutions en parallèle et les comparer.

À mon avis, d'autres systèmes de logging sont surdimensionnés au début. [Logentries](https://logentries.com) fournit des analyses avancées, mais seulement sur le plan à 89 $/mois. [Sumologic](https://www.sumologic.com/) est également un excellent outil, mais il n'est nécessaire que lorsque vous avez des millions d'utilisateurs. Il pourra alors détecter les changements dans les flux de logs et le comportement de l'application.

#### Sentry

Votre API, application web et applications mobiles doivent signaler les erreurs et exceptions à Sentry. L'intégration est clé en main. Il suffit de copier-coller quelques lignes dans votre projet, quelle que soit la technologie utilisée.

Configurez Sentry pour qu'il pousse également les erreurs vers votre canal Slack _#prod-errors_.

Le plan gratuit de Sentry est suffisant, car il permet 5 000 événements par jour. Donc, sauf si vous avez un bug dans une application mobile distribuée à des milliers d'utilisateurs, cela devrait suffire. Utilisez le premier plan payant à 29 $/mois si votre équipe compte au moins deux personnes, afin que tous les membres de votre équipe aient accès au portail.

**Coût : 29 $/mois**

#### Uptimerobot

C'est une vérification de santé pour savoir si votre service est en ligne.

Pour le configurer :

* configurez un endpoint pour votre API (et ajoutez un endpoint d'authentification libre comme _/version_ si nécessaire)
* configurez un endpoint pour votre application web dans son fichier index.html

Configurez Uptimerobot pour pousser les alertes de temps d'arrêt vers votre canal Slack _#prod-errors_.

Utilisez le plan gratuit (il n'y a qu'un plan gratuit à ce stade).

**Coût : 0 $/mois**

#### Librato

Heroku fournit des métriques décents pour votre API, mais elles sont limitées à trois jours d'historique. [Librato](https://www.librato.com/) a un historique plus long et un tableau de bord plus complet.

![Image](https://cdn-media-1.freecodecamp.org/images/0E3PRMC556EpUXkAxjp0po22X8JMD00c78fZ)

Configurez Librato comme un add-on pour vos applications Heroku :

* Utilisez le plan gratuit pour l'application de staging
* Utilisez le plan "Nickel" à 19 $/mois pour l'application de production, afin d'obtenir jusqu'à quatre semaines de profondeur sur les graphiques

Le [tarif de Librato avec Heroku](https://elements.heroku.com/addons/librato) est différent de celui du site web de Librato.

Cela est suffisant pour avoir un aperçu des performances de votre API. Mettez à l'échelle vos ressources à mesure que votre débit et votre temps de réponse augmentent, afin de réduire l'impact sur l'expérience utilisateur.

**Coût : 19 $/mois**

### Temps de payer la facture

Faisons le total de tous les coûts que j'ai identifiés jusqu'à présent :

* 57 $/mois pour le back-end sur Heroku
* 62 $/mois pour les bases de données sur Compose
* 9 $/mois pour les applications web sur Netlify
* 50 $/an pour le nom de domaine (divisé en ~4 $/mois)
* 55 $/mois pour la surveillance Papertrail/Sentry/Librato

**Total : 187 $/mois**

Nous avons atteint notre objectif de rester sous les 200 $/mois. Il nous reste encore 13 $/mois. Voyons si nous pouvons configurer notre stack d'ingénierie logicielle pour ce coût.

Nous pourrions utiliser :

* [Bitbucket](https://bitbucket.org) pour les dépôts Git. C'est moins tendance que GitHub, mais offre des dépôts privés gratuits
* [JIRA](https://www.atlassian.com/software/jira) peut servir de planificateur agile et de suivi des bugs pour 10 $/mois
* [CodeShip](https://codeship.com/) a un plan gratuit pour automatiser votre build API
* Google Apps ne coûte que 4 $/mois par compte. Utilisez un compte et des alias pour des choses comme [office@](mailto:office@mydomain.com), [support@](mailto:support@mydomain.com), [career@](mailto:career@mydomain.com). Ces adresses ont l'air bien, mais atteignent la même personne au stade le plus précoce d'une startup.

Je pourrais continuer ainsi, mais nous devrions nous arrêter ici puisque nous avons déjà dépassé le budget mensuel de 200 $ de 1 $.

### Conclusion

Si vous êtes un développeur et souhaitez lancer une startup SaaS ou un hobby, j'espère que cet article a montré que la partie infrastructure n'est pas si difficile si vous utilisez les bons outils.

Même si vous visez à devenir la prochaine grande chose, vous pouvez toujours économiser pendant votre phase de démarrage pour faire connaître votre produit.

**Concentrez-vous sur la valeur que vous apportez aux utilisateurs. Pas sur l'infrastructure.**

Les solutions fournies dans cet article évoluent jusqu'à des dizaines de milliers d'utilisateurs. Configurez-les correctement dès le début, et vous serez sur la bonne voie pour soutenir une croissance explosive des utilisateurs une fois que vous aurez atteint une traction. Je vous souhaite bonne chance pour atteindre ce point le plus rapidement possible.

Veuillez partager cela avec quiconque serait intéressé. Si vous aimez ce que vous avez lu, cliquez sur le bouton 💙 ci-dessous.