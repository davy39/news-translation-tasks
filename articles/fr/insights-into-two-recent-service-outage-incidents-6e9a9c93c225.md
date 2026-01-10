---
title: 'Rétrospective : les leçons que nous avons tirées de 2 pannes majeures de l''API'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-04-08T04:13:07.000Z'
originalURL: https://freecodecamp.org/news/insights-into-two-recent-service-outage-incidents-6e9a9c93c225
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gkNc8TL_ZIb6w6LzZTQIUQ.jpeg
tags:
- name: agile
  slug: agile
- name: Devops
  slug: devops
- name: management
  slug: management
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
seo_title: 'Rétrospective : les leçons que nous avons tirées de 2 pannes majeures
  de l''API'
seo_desc: 'By Cory Kennedy-Darby

  I belong to a team that provides internal services exposed through an API to various
  other teams within the company. These teams have become increasingly reliant on
  the services we provide.

  Without sounding egotistical, these se...'
---

Par Cory Kennedy-Darby

Je fais partie d'une équipe qui fournit des services internes exposés via une API à diverses autres équipes au sein de l'entreprise. Ces équipes sont devenues de plus en plus dépendantes des services que nous fournissons.

Sans vouloir paraître égocentrique, ces services sont probablement les plus critiques de l'entreprise. Lorsque ces services ne sont pas entièrement opérationnels et stables, cela impacte presque toutes les autres équipes et a un impact direct énorme sur les revenus.

En interne, les autres équipes de l'entreprise utilisant notre service sont référencées comme des « clients ». Pour des raisons de clarté, cet article traitera les termes « clients » et « équipes » comme interchangeables.

#### Mercredi — nous commençons à recevoir un volume énorme de requêtes

J'arrive au bureau, je prends un café et commence ma journée en vérifiant nos métriques et nos logs. La plupart des gens dans l'entreprise savaient déjà de la nuit précédente qu'il y avait eu quelques petits problèmes avec les équilibreurs de charge qui hébergent notre service. Mon manager veut que je me concentre sur une initiative importante et que j'envoie toutes les autres tâches sans rapport à lui.

Quelques heures après le début de ma journée, je remarque qu'un de nos emails de logs d'erreurs présente un pic massif dans une erreur de validation. Ces erreurs de validation n'ont rien de spécial. Nous les loggons pour notifier tout client qui nous envoie des paramètres de payload incorrects qui ne correspondent pas aux règles de validation.

L'équipe à laquelle j'appartiens n'avait déployé aucun changement, l'infrastructure était dans un état sain, et rien n'était hors de place de notre côté pour justifier une telle augmentation massive.

Mon manager avait clairement indiqué plus tôt que je devrais lui passer tout ce qui n'est pas lié à mon projet actuel sur lequel je travaille. Je réalise rapidement que j'ai fait une erreur lorsque je lui demande où je peux trouver le responsable de l'équipe qui nous envoie toutes ces erreurs de validation.

L'erreur est le moment où je lui pose cette question, il veut savoir pourquoi je demande cela. La version courte est qu'il voit cela comme un manque de concentration sur l'initiative, et explique qu'il s'occupera des erreurs de validation. Peu après notre conversation, je reçois un email me mettant en copie avec l'autre équipe pointant leur problème.

#### Soudain, la panique s'installe dans le bureau

Il y a une flopée d'emails concernant des problèmes avec notre service, et tout le monde pointe du doigt le problème précédent de la nuit dernière avec les équilibreurs de charge.

On me retire de l'initiative pour que je m'occupe de la tâche de traiter avec les opérations et l'équipe du centre de données pour gérer les équilibreurs de charge. Après quelques discussions, ils décident de commencer à rediriger des portions de notre trafic vers d'autres équilibreurs de charge.

Magiquement, les équilibreurs de charge commencent à se stabiliser.

#### Le calme avant la tempête

![Image](https://cdn-media-1.freecodecamp.org/images/UPQmbyBCXn5hZGWui5Wb0wPL8Pc-HptMOOHx)

La panique dans le bureau disparaît et tout redevient fluide. Après quelques heures, le problème semble réapparaître et une fois de plus notre service est compromis par un nombre énorme de requêtes.

**Ding !**

L'email de log d'erreurs arrive, et je remarque que ces erreurs de validation réapparaissent. J'avais été tellement concentré sur la gestion du centre de données que je n'avais pas remarqué qu'elles avaient cessé lorsque les équilibreurs de charge étaient devenus stables.

Attendez ! Je consulte notre tableau de bord Kibana pour voir nos requêtes au fil du temps et compare les horodatages des erreurs de validation et le nombre total de requêtes au fil du temps. Ils correspondent presque exactement.

Je suis assez confiant que c'est le problème, et je décide que je ne répète pas la même erreur que ce matin. Je demande à un collègue où se trouve l'autre équipe et je m'y rends armé de la connaissance de la corrélation entre les pics et le moment où tout devient instable.

En 10 minutes d'explication de la situation à l'autre équipe, ils réalisent que cela correspond exactement au moment où ils ont déployé une fonctionnalité, où ils l'ont désactivée, et où elle a été accidentellement redéployée.

Ils désactivent la fonctionnalité de leur côté, et notre service retrouve sa stabilité. La fonctionnalité qu'ils avaient déployée contenait un bug qui appelait notre service dans toutes les situations, même lorsque ce n'était pas nécessaire.

#### Lundi — ~600 % de requêtes en plus vers un endpoint

Le week-end passe, et il n'y avait eu aucun problème avec notre service depuis l'incident de mercredi. Le lundi commence normalement sans aucun problème, mais à la fin de la journée de travail, notre service commence à devenir instable.

En jetant un rapide coup d'œil aux événements Kibana et à nos logs d'accès, je remarque ce qui semble être une quantité folle de requêtes provenant d'une seule équipe. La même équipe que mercredi.

Je me précipite vers la zone de cette équipe dans l'entreprise et explique les détails, en demandant s'ils ont par erreur relancé la fonctionnalité boguée de mercredi.

Pour être sûr que la fonctionnalité n'avait pas été déployée à nouveau par erreur, ils ont examiné leurs logs de déploiement et vérifié sur git que la fonctionnalité n'avait pas été fusionnée par erreur dans une autre branche.

La fonctionnalité de mercredi n'avait pas été redéployée.

Je retourne à mon bureau et commence à discuter avec l'équipe des opérations du centre de données. La situation à ce stade est devenue grave en raison du temps pendant lequel le service a été impacté. L'équipe des opérations enquête, et je suis assis en attendant une réponse lorsque le VP des opérations arrive.

Il n'est clairement pas content car notre API impacte de nombreux produits et services qui proviennent du côté opérationnel de l'entreprise. Il a quelques questions sur le contournement de notre service, l'utilisation de certaines méthodes de repli, et une estimation du retour à la normale du service.

Quelques minutes de plus passent et tout se stabilise.

#### Résolu ? Pas à moins que je ne croie aux licornes et aux créatures mythiques

L'équipe des opérations du centre de données explique qu'une fonctionnalité sur notre serveur de staging provoquait le crash continu des processus de l'équilibreur de charge. Je conteste leur réponse car cette fonctionnalité avait fonctionné sans aucun problème pendant près de deux mois consécutifs. L'autre raison pour laquelle je n'étais pas prêt à accepter leur réponse était que j'avais remarqué sur notre tableau de bord Kibana que nos requêtes totales avaient presque quadruplé.

Il semblait trop fou qu'une fonctionnalité aussi stable sur nos serveurs de staging commence soudainement à causer de si grands problèmes.

#### Mardi — Les parties prenantes veulent des réponses

Mardi matin, mon manager me demande de fournir un aperçu clair des événements survenus lundi pour qu'il puisse rédiger un rapport d'incident pour les parties prenantes.

La nuit précédente, j'ai passé beaucoup de temps à réfléchir aux situations récentes et j'ai réalisé qu'un point de douleur significatif était l'utilisation de notre tableau de bord Kibana. Notre tableau de bord Kibana est amazing lorsque vous voulez voir toutes les requêtes, mais avec notre mappage actuel, il est difficile de creuser et d'isoler les requêtes d'un client spécifique.

Le problème ? Cela va prendre un peu de travail, personne ne m'a assigné à faire cela, et ce n'est pas la tâche originale qui m'a été donnée. Sur le moment, je décide que je vais construire cela. Les individus performants ne demandent pas la permission de faire leur travail. Ils vont et livrent des résultats.

> Les individus performants ne demandent pas la permission de faire leur travail. Ils vont et livrent des résultats.

> - Cory Darby

Je commence à bricoler un script qui utilise des expressions régulières avec notre Elasticsearch qui passe les résultats dans Highcharts. Pendant ce temps, notre CTO s'arrête pour demander à propos de la situation qui s'est déroulée lundi. J'explique qu'il n'y a aucune preuve pour le moment, mais que mon intuition, d'après ce que j'ai vu dans les logs, les graphiques et les métriques, est que le cache de l'autre équipe est mort. La mort du cache de l'autre équipe les forcerait à faire un nombre énorme de requêtes à notre service.

Il part pour obtenir des réponses de l'autre équipe, et je termine de bricoler le script. Ce n'est pas du code élégant, mais il fait le travail, et cela signifie que nous ne sommes plus dans le noir.

Juste 10 minutes après avoir terminé, notre CTO revient. Il explique que l'autre équipe ne trouve aucun problème de leur côté. À ce stade, je lui montre le graphique, qui montre chaque requête groupée par chaque équipe utilisant notre service :

![Image](https://cdn-media-1.freecodecamp.org/images/2M1TeGf4l6M5hQFzDKGxyYXqYMfG-hzZtn6I)
_Ce graphique montre toutes les requêtes vers notre service provenant de plus de 100 services clients._

Le pic géant dans le graphique ci-dessus est l'autre équipe qui venait d'expliquer que tout semblait sain de leur côté.

Une investigation plus poussée par l'autre équipe a montré qu'une nouvelle fonctionnalité qu'ils avaient lancée nécessitait une quantité significative de mise en cache. Les règles qu'ils ont en place avec leur cache étaient d'évincer les objets mis en cache les plus anciens pour faire de la place aux nouveaux. Les données évincées se sont avérées être toutes les données mises en cache pour notre service.

Leur cache fonctionnait, mais il n'avait plus aucune de nos données de service en cache. L'autre équipe nous sollicitait pour presque chaque requête.

### Domaines d'amélioration

Après tout incident majeur d'ingénierie, il est important de couvrir la cause, la solution, la prévention et les points de douleur que l'incident a exposés.

#### Métriques et surveillance perspicaces

Les clients utilisant nos services ont besoin de meilleures informations sur leur utilisation. De notre côté, nous fournirons des moyens plus faciles de creuser pour des métriques spécifiques.

Après ces événements, il est clair que nous devrons créer un véritable tableau de bord pour les clients et pour nous-mêmes. Le tableau de bord remplacera le script que j'ai construit pour pousser les données dans le graphique Highchart. Les graphiques du tableau de bord auront une surveillance des données reçues afin qu'ils puissent fournir les alertes les plus précoces.

#### Réduire les silos d'équipe

Idéalement, nous permettions à d'autres équipes de l'entreprise de pouvoir épingler des points sur le tableau de bord lorsqu'elles déploient dans leurs environnements de production. Si les requêtes d'une seule équipe augmentent substantiellement après un déploiement, le déploiement est probablement responsable de ce pic.

#### Communication

Pendant ces pannes, les parties prenantes ont créé beaucoup de distractions dans toute l'entreprise. Ces distractions prennent la forme d'emails, de messages de chat et d'individus se présentant dans l'espace de l'équipe pour demander des nouvelles du service.

Pour réduire le nombre de distractions, nous aurons un tableau de bord interne qui inclut le statut actuel et les événements au fur et à mesure qu'ils se déroulent. Les événements incluront l'heure de création, une description de la situation et une estimation du temps de rétablissement (si connu).

### Conclusion

Ce n'est jamais une question de « si » il y aura une panne. C'est une question de « quand ».

Chaque incident — peu importe sa taille — est une opportunité d'apprentissage pour empêcher que de telles choses ne se reproduisent, réduire leur impact négatif et être mieux préparé.

_Avis de non-responsabilité : Ce sont mes opinions, à moi seul, et elles ne reflètent pas celles de mon employeur._