---
title: Comment démarrer votre analyse en 1 heure
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-10T18:21:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-bootstrap-your-analytics-in-1-hour-cb3a549b4780
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xfavpsRMhnfgQbQ-7SkESg.png
tags:
- name: analytics
  slug: analytics
- name: business
  slug: business
- name: Data Science
  slug: data-science
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Comment démarrer votre analyse en 1 heure
seo_desc: 'By Tim Abraham

  Even though most startups understand how critical data is to their success, they
  tend to shy away from analytics — especially early on.

  This partially stems from the myth that if you want to have good analytics, you
  should carve out ar...'
---

Par Tim Abraham

Même si la plupart des startups comprennent à quel point les données sont cruciales pour leur succès, elles ont tendance à éviter l'analyse — surtout au début.

Cela provient en partie du mythe selon lequel, si vous voulez avoir de bonnes analyses, vous devriez consacrer environ 25 % de vos ressources d'ingénierie à cela. Pour un fondateur avec une vision, une distraction de 25 % de l'exécution de cette vision — en échange d'une meilleure compréhension de leur performance — n'en vaut tout simplement pas la peine.

Mais la mise en place de quelques analyses de base pour votre produit n'est pas aussi difficile que vous le pensez. Certaines loin de 25 % du budget d'ingénierie. Bien que ce chiffre puisse être vrai pour les entreprises matures avec de nombreux pipelines de données compliqués, une petite entreprise peut facilement mettre en place quelque chose avec des coûts minimaux.

**Pour le prouver, je vais vous montrer comment vous pouvez passer 1 heure à mettre en place un système qui devrait être adéquat pour les 6 prochains mois de la vie de votre entreprise.**

Tout d'abord, parlons de ce que je veux dire par "avoir des analyses". Je pense que les exigences minimales sont :

* Un accès simple à vos métriques clés pour tout le monde dans votre entreprise
* Un e-mail ou un message Slack nocturne avec les statistiques envoyé à votre équipe
* Quelques tableaux de bord hébergés à afficher sur les moniteurs du bureau
* Un endroit où n'importe qui dans votre entreprise peut explorer les données (indépendamment de l'acuité technique)

En d'autres termes, vous avez besoin de **métriques** et d'**un moyen de les diffuser dans toute votre organisation**. Commençons par la partie métriques.

### Vos métriques sont déjà dans votre base de données

Puisque la tarte est bien plus délicieuse que les widgets, imaginons que vous venez de commencer [une entreprise de livraison de tartes](https://github.com/timabe/pies). Vous décidez que — au minimum — le succès de votre entreprise dépendra de :

1. Votre capacité à attirer des consommateurs potentiels de tartes
2. Votre capacité à vendre des tartes à ces consommateurs

![Image](https://cdn-media-1.freecodecamp.org/images/1*yPRxRb5UghNa-EZmeuuteg.png)
_Mmmm, des tartes_

Si vous pouvez faire croître de manière fiable à la fois 1 et 2, vous n'aurez pas trop d'autres choses à craindre. Vous décidez, sur cette base, de suivre :

1. Les nouvelles inscriptions d'utilisateurs
2. Les ventes de tartes
3. L'utilisation répétée

Vous savez que vous pouvez dériver quelques métriques plus intéressantes basées uniquement sur les données d'inscription des utilisateurs et de vente de tartes, mais pour l'instant, vous êtes satisfait de ces trois grandes métriques de haut niveau. Maintenant, comment les créer réellement ?

À ce stade, beaucoup de gens se tournent vers Google Analytics, Mixpanel ou un autre fournisseur d'analyse d'événements tiers. Bien que j'adore ces produits et que j'adore l'analyse d'événements, je pense également que cela fait partie des raisons pour lesquelles les startups en phase de démarrage reportent l'analyse. Les configurer correctement signifie du temps d'ingénierie consacré à quelque chose d'orthogonal au développement de votre produit principal.

Avant de faire valoir que l'équipe d'ingénierie consacre un cycle à instrumenter les inscriptions des utilisateurs et les ventes de tartes, considérez ceci : **ces métriques sont probablement déjà dans votre base de données d'application**. En d'autres termes, si vous construisez un produit pour livrer des tartes aux utilisateurs et que vous n'avez pas de table ou de collection de base de données pour stocker vos utilisateurs ou les tartes qu'ils ont commandées... eh bien, le manque d'analyse n'est pas votre plus grande préoccupation.

Rappelez-vous, un logiciel est essentiellement composé de données et de logique pour opérer sur ces données. Beaucoup ne réalisent pas que les données de votre application peuvent en fait être utilisées pour l'analyse également. Alors n'hésitez pas à mettre l'instrumentation de votre analyse d'événements dans le backlog et voyons combien nous pouvons accomplir avec juste votre base de données d'application.

Maintenant, comment obtenir ces métriques ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*PpCld0A2l3pM9dpq.)
_Elles sont "dans" la base de données ?_

### Metabase : Un outil d'analyse qui fonctionne avec votre base de données

Il existe de nombreuses façons de récupérer des informations d'une base de données, mais il n'y a qu'une seule façon la plus facile, et cet article parle des façons faciles.

Mon outil préféré que je recommande pour toute entreprise que je conseille est [Metabase](http://www.metabase.com/). Metabase est le moyen le plus rapide et le plus facile de partager des données et des analyses au sein de votre entreprise. Il est super simple à installer ou à déployer, fonctionne avec presque toutes les bases de données, et surtout, il est open source et 100 % gratuit — vous devriez donc définitivement l'essayer avant de vous tourner vers certaines des options payantes.

_Divulgation complète : Je travaille chez [expa](http://expa.com/), où Metabase a été lancé, et je suis conseiller pour l'entreprise. J'ai également, au cours de la dernière année, conseillé 8 différentes startups technologiques sur les données et les analyses et dans chaque cas, je leur ai recommandé Metabase. Elles continuent toutes à l'utiliser._

### Installation/Déploiement

Si vous êtes simplement en mode évaluation, je vous recommande de télécharger l'application mac de Metabase. Suivez leur [guide d'installation](http://www.metabase.com/docs/v0.20.3/setting-up-metabase.html), et vous êtes prêt à créer quelques métriques. Cependant, le déploiement de Metabase soit sur [Heroku](http://www.metabase.com/docs/v0.20.3/operations-guide/running-metabase-on-heroku.html) ou [AWS Elastic Beanstalk](http://www.metabase.com/docs/v0.20.3/operations-guide/running-metabase-on-elastic-beanstalk.html) (meilleur) est fortement recommandé, car vous obtiendrez une application persistante hébergée dans le cloud et toute votre équipe pourra l'utiliser.

Pour un guide complet sur le processus de déploiement, [consultez mon tutoriel vidéo](https://www.youtube.com/watch?v=wmJ02K8LIFk). La [documentation](http://www.metabase.com/docs/v0.20.3/operations-guide/start.html#installing-and-running-metabase) de Metabase est assez complète, également. Si vous êtes une personne non technique, vous devrez peut-être solliciter un ingénieur, surtout si votre base de données d'application est dans un VPC sur AWS.

À ce propos, il est également bon de créer une réplique de lecture de votre base de données d'application et de la connecter à Metabase. Ainsi, vous pouvez vous assurer que les requêtes lourdes ou en attente n'affecteront pas vos utilisateurs.

Une fois que vous avez déployé Metabase, inscrivez-vous et ajoutez vos identifiants de base de données. Ensuite, invitez les membres de votre équipe pour qu'ils puissent participer.

### Création de vos métriques

Croyez-le ou non, le reste est assez facile. La première chose que vous voudrez faire est de construire vos métriques. Dans le jargon de Metabase, ce sont des "Questions". Si vous êtes dans le commerce des tartes et que vous avez un schéma raisonnablement organisé, vous devriez pouvoir obtenir vos métriques clés avec seulement quelques clics. Aucune connaissance en SQL n'est requise, mais bien sûr, si vous aimez SQL, cette option est disponible.

Alors, construisez vos principales métriques et voyez si d'autres métriques intéressantes vous viennent à l'esprit. Bien que vous puissiez trouver [des centaines de personnes intelligentes qui vous diront de ne jamais faire un graphique en camembert](https://www.quora.com/How-and-why-are-pie-charts-considered-evil-by-data-visualization-experts), je ne vous en voudrai pas de faire un graphique en camembert basé sur la popularité des tartes. Si Metabase est la méta-base de données, il est seulement juste de rendre votre graphique en camembert méta.

### Finitions

Ensuite, vous voudrez configurer un e-mail quotidien avec les statistiques. Je ne sais pas ce qu'ils ont, mais tout le monde aime les e-mails quotidiens avec les statistiques. Metabase appelle cela des "Pulses", et vous permet même d'utiliser Slack si vous êtes trop cool pour les e-mails. Ajoutez les Questions que vous voulez envoyer, choisissez une heure et une fréquence (ce n'est pas obligatoirement quotidien, mais cela tend à être le plus utile) et une liste de destinataires ou un canal Slack et vous avez terminé.

Enfin, tout le monde aime voir de beaux tableaux de bord sur les moniteurs du bureau. Ne les laissez pas dans l'expectative. Créer un tableau de bord est également assez simple. Choisissez quelques Questions et organisez-les comme le permettent vos sensibilités de design. Chargez-le sur un moniteur externe que vous avez dans le bureau, puis mettez-le en plein écran.

### Récapitulatif

Vous venez de mettre en place une infrastructure d'analyse assez solide pour votre startup en environ une heure. Maintenant, toute votre équipe peut explorer votre base de données d'application, recevoir des e-mails nocturnes et consulter un tableau de bord à l'échelle de l'entreprise. Mieux encore, cette configuration devrait durer assez longtemps — au moins 6 mois, sauf si vous commencez à connaître une croissance folle (auquel cas, pas de plainte).

Prêt à essayer ? Sceptique quant à ma garantie d'une heure ? Consultez mes tutoriels YouTube, [partie 1](https://www.youtube.com/watch?v=wmJ02K8LIFk) et [partie 2](https://www.youtube.com/watch?v=Abza9SKoWPs), où je vous guiderai à travers tout ce que vous devez savoir.