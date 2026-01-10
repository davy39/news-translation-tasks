---
title: Comment surveiller l'activité de Stack Overflow dans Slack
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-10T16:01:01.000Z'
originalURL: https://freecodecamp.org/news/monitor-stack-overflow-activity-directly-into-slack-dc778913490f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tWzWtTvWgglmNujgAREraA.jpeg
tags:
- name: serverless
  slug: serverless
- name: slack
  slug: slack
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment surveiller l'activité de Stack Overflow dans Slack
seo_desc: 'By Nicolas Grenié

  Powered by a complete serverless stack


  _Group of Developer Advocates watching developers coding — Credits: [Pixabay](https://pixabay.com/en/meerkat-snout-baby-mammal-guard-275967/"
  rel="noopener" target="blank" title=")

  Developer A...'
---

Par Nicolas Grenié

#### Alimenté par une pile serverless complète

![Image](https://cdn-media-1.freecodecamp.org/images/lcvnNk4qwdIdxJPmXh9hKD1vqzfnvSJpdExY)
_Groupe de Developer Advocates observant des développeurs en train de coder — Crédits : [Pixabay](https://pixabay.com/en/meerkat-snout-baby-mammal-guard-275967/" rel="noopener" target="_blank" title=")_

Les Developer Advocates ou Evangelists sont souvent interrogés sur la manière dont ils mesurent le succès.

On pourrait soutenir que les ⭐️ de GitHub sur les dépôts sont formidables. Et Ash Hathaway partage ses réflexions [ici](https://medium.com/@ash_hathaway/developer-evangelism-and-github-metrics-7e1c0a9d2fe2).

D'autres pourraient dire que les questions sur Stack Overflow donnent une bonne idée de la popularité d'une API. Je serais d'accord avec cette affirmation.

Si vous n'avez pas de forum pour votre produit, les développeurs pourraient finir par poser des questions directement sur Stack Overflow.

Je ne recommanderais pas aux entreprises de rediriger toutes leurs questions de support là-bas ou de promouvoir leurs tags de marque, ce qui est simplement mauvais. Vous détournez une communauté pour vos propres besoins au lieu de contribuer à celle-ci.

#### Mais :

**Que se passe-t-il lorsque quelqu'un publie une question là-bas ?**  
**Comment êtes-vous notifié ?**  
**Comment pouvez-vous réagir rapidement ?**

D'après mon expérience, vous ne pouvez recevoir des notifications que lorsqu'il y a de nouvelles questions sur un tag particulier. Cela pourrait ne pas couvrir toutes les questions posées sur votre API.

Vous pouvez également utiliser des outils comme [Mention](http://mention.net/). Il couvre plus que Stack Overflow, mais ce n'est pas instantané.

Pour être plus réactif, j'ai bricolé quelque chose pour notre équipe chez [3scale](http://3scale.net/) il y a longtemps. Je l'ai récemment réécrit en utilisant des technologies serverless. Il surveille les questions sur **3scale** et les publie sur notre canal Slack **#support**. L'équipe de support peut ainsi intervenir rapidement et répondre.

Je souhaite partager ce projet afin que vous aussi puissiez surveiller Stack Overflow directement dans Slack.

### Les outils ?

Pour suivre la tendance de 2017, nous n'utiliserons que des technologies serverless, ce qui rendra cet outil gratuit à utiliser :  
- [AWS Lambda](https://aws.amazon.com/lambda/) pour héberger la logique de notre application  
- [FaunaDB](http://faunadb.com) pour stocker les bases de données  
- [Serverless Framework](http://serverless.com) pour simplifier les déploiements  
- [Slack](http://slack.com) pour être notifié lorsqu'une nouvelle question est posée

### La logique⚙️

L'[API Stack Exchange](https://api.stackexchange.com/docs) dispose d'un endpoint pour rechercher des questions. Vous pouvez rechercher un terme dans les tags, dans le titre, dans le corps de la question ou tout cela en même temps. Dans l'exemple, nous rechercherons dans tous les attributs.

Vous devriez créer une clé pour accéder à l'API Stack Exchange [ici](https://stackapps.com/apps/oauth/register).

Notre fonction appellera régulièrement cet endpoint pour vérifier s'il y a de nouvelles questions publiées. Nous utiliserons la fonctionnalité _Schedule Events_ offerte nativement par Lambda, qui se comporte de manière similaire à une tâche cron.

Nous stockerons les questions dans une base de données pour garder une trace de celles que nous avons déjà envoyées à Slack et éviter les doublons.

Si une question Stack Overflow n'est pas dans notre base de données, nous l'ajoutons à la base de données et envoyons les détails à Slack.

### FaunaDB

J'ai découvert [FaunaDB](http://faunadb.com) il y a quelques mois à [Gluecon](http://gluecon.com). Ils se présentent comme le premier moteur de base de données **serverless**. Tout est hébergé de leur côté. FaunaDB est une base de données distribuée mondialement qui ne nécessite aucune provision. La capacité est mesurée et disponible à la demande, vous ne payez donc que pour ce que vous utilisez.

Si vous êtes familier avec [Firebase](http://firebase.com), vous reconnaîtrez une structure de données similaire et des routes pour accéder aux ressources. Mais elle offre plus de fonctionnalités, ce qui facilite par exemple l'interrogation de la base de données.

![Image](https://cdn-media-1.freecodecamp.org/images/oF0Mv4Xyrex1TMvUMFbYR41PiAaka1Qg7umn)
_Exemple : Comment créer une entrée dans FaunaDB_

Pour cette application, vous aurez besoin d'une base de données, avec une classe **questions**. Nous ajouterons également un index **questions_by_id** sur les termes **data** et **question_id**. Cela nous permettra d'interroger la classe questions par l'ID de Stack Overflow.

Si vous êtes préoccupé par l'utilisation de votre base de données, vous pouvez ajouter un TTL à la classe **questions**. Cela supprimera automatiquement les instances plus anciennes que la valeur TTL.

Enfin, vous devrez créer une clé serveur pour la classe questions. Cette clé sera utilisée pour authentifier notre fonction auprès des serveurs FaunaDB.

![Image](https://cdn-media-1.freecodecamp.org/images/xMXM3OayubBR1aEXJq1pcW1aO3CuPP5fdJMy)
_Exemple : Comment récupérer une entrée dans FaunaDB_

### Slack

Pour publier sur Slack, nous aurons simplement besoin d'un webhook entrant. Créez-en un [ici](https://my.slack.com/services/new/incoming-webhook/).

### Configurer le projet

Assurez-vous d'avoir installé le [Framework Serverless](http://serverless.com) et configuré l'outil [AWS CLI](https://aws.amazon.com/cli/).

Vous pouvez maintenant cloner ce projet localement.

```
git clone git@github.com:picsoung/stackOverflowMonitor.gitcd stackOverflowMonitor
```

Dans `serverless.yml`, vous modifierez les variables d'environnement avec vos propres valeurs.

`FAUNADB_SECRET` est le secret que nous avons créé précédemment pour accéder à FaunaDB  
`STACK_EXCHANGE_KEY` est la clé API pour accéder à l'API Stack Exchange  
`SLACK_WEBHOOK_URL` est l'URL du webhook entrant Slack que vous avez créé   
`SLACK_CHANNEL` doit être un nom de canal existant dans votre équipe Slack tel que #support ou #stackoverflow  
`SEARCH_KEYWORD` est le mot-clé qui vous intéresse pour la surveillance, comme Node.js ou Angular2

Une fois que vous avez modifié toutes les variables avec vos propres valeurs, nous pouvons tester si tout fonctionne. Nous invoquons la fonction localement avec la commande suivante :

```
serverless invoke local — function getStackOverflowQuestions
```

Comme c'est la première fois que vous lancez la fonction, elle devrait publier un message sur votre canal Slack. Cela devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/5rLOupAnNseTvLkWvGUBnjUDjMNsLVTwVubk)
_À quoi devrait ressembler la notification dans votre canal Slack_

Si vous êtes satisfait du résultat, vous pouvez maintenant déployer la fonction avec la commande suivante :

```
serverless deploy
```

Par défaut, la fonction est appelée toutes les 20 minutes. Vous pouvez la personnaliser en modifiant la propriété schedule dans le fichier `serverless.yml`.

### Étendre le projet

Pour l'instant, nous ne surveillons qu'un seul terme. Vous pouvez lancer plusieurs instances de cette fonction pour surveiller plus de termes ou de tags sur Stack Overflow.

Si vous êtes intéressé par une solution en temps quasi réel, je vous encourage à consulter [Streamdata.io](http://streamdata.io/). Leurs outils transforment les API de pulling en API de streaming.

Si vous souhaitez des tableaux de bord agréables qui montrent à quel point votre communauté est active sur Stack Overflow, je recommande [Keen.io](http://keen.io/). Vous pouvez envoyer toutes vos données Stack Overflow là-bas. Keen offre une [variété de bibliothèques](https://keen.github.io/dashboards/) pour créer de beaux tableaux de bord.

Nous pouvons également ajouter plus de fonctionnalités dans Slack, comme des boutons ou des menus. Ainsi, les personnes peuvent revendiquer une question ou se voir attribuer une question à répondre.

### Conclusion

C'était un petit projet qui m'a permis de découvrir comment utiliser FaunaDB. Utiliser AWS Lambda est bien plus efficace que l'instance Heroku que j'avais dans le passé.

J'espère que vous avez trouvé cet exemple serverless utile. Le code est [ouvert](https://github.com/picsoung/stackoverflowmonitor) sur GitHub, alors n'hésitez pas à contribuer et à ajouter de nouvelles fonctionnalités.

Si vous travaillez pour une entreprise qui vend aux développeurs, je suis sûr que vous avez déjà entendu le "Soyez là où sont les développeurs."

Dans le monde en ligne, vous avez de bonnes chances de trouver des développeurs sur des sites comme Hackers News, Stack Overflow ou GitHub. Il est important de mesurer ce que les gens disent de votre produit ou de vos technologies sur ces sites.

C'était un petit projet qui m'a permis de découvrir comment utiliser FaunaDB. Utiliser AWS Lambda est bien plus efficace que l'instance Heroku que j'avais dans le passé.

J'espère que vous avez trouvé cet exemple serverless utile. Le code est [ouvert](https://github.com/picsoung/stackoverflowmonitor) sur GitHub, alors n'hésitez pas à contribuer et à ajouter de nouvelles fonctionnalités.