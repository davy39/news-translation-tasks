---
title: La technologie ennuyeuse derrière une entreprise Internet à une seule personne
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-10T21:51:00.000Z'
originalURL: https://freecodecamp.org/news/the-boring-technology-behind-a-one-person-internet-company
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/1_83ZzjS6ZhVWvZdnoozElOw.png
tags:
- name: actor model
  slug: actor-model
- name: Entrepreneurship
  slug: entrepreneurship
- name: podcast
  slug: podcast
- name: 'solopreneur '
  slug: solopreneur
- name: Startups
  slug: startups
seo_title: La technologie ennuyeuse derrière une entreprise Internet à une seule personne
seo_desc: 'By Wenbin Fang

  Listen Notes is a podcast search engine and database. The technology behind Listen
  Notes is actually very very boring. No AI, no deep learning, no blockchain. “Any
  man who must say I am using AI is not using True AI” :)

  After reading t...'
---

Par Wenbin Fang

[Listen Notes](https://www.listennotes.com/) est un moteur de recherche et une base de données de podcasts. La technologie derrière Listen Notes est en réalité très très ennuyeuse. Pas d'IA, pas de deep learning, pas de blockchain. [Tout homme qui doit dire que j'utilise l'IA n'utilise pas la vraie IA](https://www.youtube.com/watch?v=4sJY7BTIuPY) :)

Après avoir lu cet article, vous devriez être en mesure de reproduire ce que j'ai construit pour Listen Notes ou de faire facilement quelque chose de similaire. Vous n'avez pas besoin d'embaucher beaucoup d'ingénieurs. Souvenez-vous, [quand Instagram a levé 57,5 millions de dollars et a été racheté par Facebook pour 1 milliard de dollars](https://www.crunchbase.com/organization/instagram#section-funding-rounds), ils n'avaient que [13 employés](https://www.businessinsider.com/instagram-employees-and-investors-2012-4)

et pas tous étaient ingénieurs. L'histoire d'Instagram s'est déroulée début 2012. Nous sommes en 2019 maintenant, il est plus possible que jamais de construire quelque chose de significatif avec une petite équipe d'ingénieurs

voire une seule personne.

Si vous n'avez pas encore utilisé Listen Notes, essayez-le maintenant :

[https://www.listennotes.com/](https://www.listennotes.com/)

### Aperçu

Commençons par les exigences ou les fonctionnalités de ce projet Listen Notes.

Listen Notes offre deux choses aux utilisateurs finaux :

* Un site web [ListenNotes.com](https://www.listennotes.com/) pour les auditeurs de podcasts. Il fournit un moteur de recherche, une base de données de podcasts, des playlists [Listen Later](https://www.listennotes.com/listen/?s=nav), des [Listen Clips](https://www.listennotes.com/clips/?s=nav) qui vous permettent de découper un segment de n'importe quel épisode de podcast, et des [Listen Alerts](https://www.listennotes.com/alerts) qui vous notifient lorsqu'un mot-clé spécifié est mentionné dans de nouveaux podcasts sur Internet.
* Des [API de recherche et de répertoire de podcasts](https://www.listennotes.com/api/) pour les développeurs. Nous devons suivre l'utilisation de l'API, recevoir de l'argent des utilisateurs payants, faire du support client, et plus encore.

Je fais tourner tout sur AWS. Il y a 20 serveurs de production (au 5 mai 2019) :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/1__HqlSoEW7JEDVnJ9rFSj7w.png)
_Les serveurs qui font tourner Listen Notes_

Vous pouvez facilement deviner ce que fait chaque serveur à partir du nom d'hôte.

* **production-web** sert le trafic web pour [ListenNotes.com](https://www.listennotes.com/).
* **production-api** sert le trafic API. Nous exécutons deux versions de l'API (au 4 mai 2019), ainsi v1api (la version héritée) et v2api (la nouvelle version).
* **production-db** exécute PostgreSQL (primaire et réplica)
* **production-es** exécute un cluster Elasticsearch.
* **production-worker** exécute des tâches de traitement hors ligne pour maintenir la base de données de podcasts toujours à jour et pour fournir certaines fonctionnalités magiques (par exemple, classement des résultats de recherche, recommandations d'épisodes/podcasts

).
* **production-lb** est le répartiteur de charge. J'exécute également Redis & RabbitMQ sur ce serveur, par commodité. Je sais que ce n'est pas idéal. Mais je ne suis pas une personne parfaite :)
* **production-pangu** est le serveur de type production que j'utilise parfois pour exécuter des scripts ponctuels et tester des changements. Quelle est la signification de [pangu](https://en.wikipedia.org/wiki/Pangu) ?

La plupart de ces serveurs peuvent être mis à l'échelle horizontalement. C'est pourquoi je les nomme _production-something1_, _production-something2_

. Il pourrait être très facile d'ajouter _production-something3_ et _production-something4_ à la flotte.

### Backend

L'ensemble du backend est écrit en Django / Python3. Le système d'exploitation choisi est Ubuntu.

J'utilise [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) pour servir le trafic web. Je place [NGINX](https://www.nginx.com/) devant les processus uWSGI, qui sert également de répartiteur de charge.

Le principal stockage de données est [PostgreSQL](https://www.postgresql.org/), avec lequel j'ai une grande expérience de développement et d'exploitation sur de nombreuses années

une technologie testée en conditions réelles est bonne, donc je peux dormir tranquillement la nuit. [Redis](https://redis.io/) est utilisé à diverses fins (par exemple, cache, statistiques,

). Il n'est pas difficile de deviner que [Elasticsearch](https://www.elastic.co/) est utilisé quelque part. Oui, j'utilise Elasticsearch pour indexer les podcasts et les épisodes et pour servir les requêtes de recherche, tout comme [la plupart](https://medium.com/netflix-techblog/tagged/elasticsearch) [des entreprises](https://engineeringblog.yelp.com/2017/06/moving-yelps-core-business-search-to-elasticsearch.html) [ennuyeuses](https://eng.uber.com/tag/elasticsearch/).

[Celery](http://www.celeryproject.org/) est utilisé pour le traitement hors ligne. Et [Celery Beat](http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html) est utilisé pour planifier les tâches, ce qui est similaire aux tâches Cron mais un peu plus agréable. Si à l'avenir Listen Notes gagne en traction et que Celery & Beat causent des problèmes de mise à l'échelle, je passerai probablement aux deux projets que j'ai réalisés pour mon ancien employeur : [ndkale](https://github.com/Nextdoor/ndkale) et [ndscheduler](https://github.com/Nextdoor/ndscheduler).

[Supervisord](http://supervisord.org/) est utilisé pour la gestion des processus sur chaque serveur.

Attendez, qu'en est-il de Docker / Kubernetes / serverless ? Non. Avec l'expérience, vous savez quand ne pas sur-ingénieriser. J'ai en fait fait quelques travaux précoces sur Docker pour mon ancien employeur en 2014, ce qui était bien pour une startup d'un milliard de dollars de taille moyenne mais peut être excessif pour une startup minuscule à une seule personne.

### Frontend

Le frontend web est principalement construit avec [React](https://reactjs.org/) + [Redux](https://redux.js.org/) + [Webpack](https://webpack.js.org/) + [ES](https://en.wikipedia.org/wiki/ECMAScript). Cela est assez standard de nos jours. Lors du déploiement en production, les bundles JS sont téléchargés sur [Amazon S3](https://aws.amazon.com/s3/) et servis via [CloudFront](https://aws.amazon.com/cloudfront/).

Sur [ListenNotes.com](https://www.listennotes.com/), la plupart des pages web sont rendues à moitié côté serveur ([Django template](https://docs.djangoproject.com/en/2.0/topics/templates/)) et à moitié côté client ([React](https://reactjs.org/)). La partie rendue côté serveur fournit un modèle de base d'une page web, et la partie rendue côté client est essentiellement une application web interactive. Mais quelques pages web sont rendues entièrement côté serveur, en raison de ma paresse à rendre les choses parfaites et de certains avantages potentiels pour le SEO.

#### Lecteur audio

J'utilise une version fortement modifiée de [react-media-player](https://github.com/souporserious/react-media-player) pour construire le lecteur audio sur ListenNotes.com, qui est utilisé à plusieurs endroits, y compris [Listen Notes Website](https://www.listennotes.com/p/321dd0ce5b974079bd3fc8d65d132912/), [Twitter embedded player](https://twitter.com/ListenHistoryFM/status/955913550605688832), et le lecteur intégré sur les sites web tiers :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/1_R9SqwWtGOKvL0MqOBvsMrA.png)
_Lecteur intégré sur les sites web tiers_

### API Podcast

Nous fournissons une API podcast simple et fiable aux développeurs. Construire l'API est similaire à construire [le site web](https://www.listennotes.com/). J'utilise la même pile Django/Python pour le backend, et ReactJs pour le frontend (par exemple, tableau de bord de l'API, documentation

).

![Image](https://www.freecodecamp.org/news/content/images/2019/06/1_6s_rx2FAKEJiHy7K6gEwdA.png)
_Tableau de bord de l'API Listen_

![Image](https://www.freecodecamp.org/news/content/images/2019/06/1_dYUinicZH-m6HZPpE1MXBg.png)
_Documentation de l'API Listen_

Pour l'API, nous devons suivre combien de requêtes un utilisateur utilise dans le cycle de facturation actuel, et facturer $$$ à la fin d'un cycle de facturation. Il n'est pas difficile d'imaginer que Redis est largement utilisé ici :)

### DevOps

#### Approvisionnement des machines et déploiement du code

J'utilise [Ansible](http://docs.ansible.com/) pour l'approvisionnement des machines. Basiquement, j'ai écrit un ensemble de fichiers yaml pour spécifier quel type de serveurs doit avoir quels fichiers de configuration et quel logiciel. Je peux lancer un serveur avec tous les fichiers de configuration corrects et tous les logiciels installés avec un seul bouton. Voici la structure de répertoire de ces fichiers yaml Ansible :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/1_oql35nt1Iak2FzniugFPSw.png)
_J'aurais pu faire un meilleur travail dans le nommage des choses. Mais encore une fois, c'est suffisamment bon pour maintenant._

J'utilise également Ansible pour déployer le code en production. Basiquement, j'ai un script wrapper _deploy.sh_ qui est exécuté sur macOS :

> _./deploy.sh production HEAD web_

Le script deploy.sh prend trois arguments :

* **Environnement** : production ou staging.
* **Version du dépôt listennotes** : HEAD signifie juste déployer la dernière version. Si un SHA d'un commit git est spécifié, alors il déployera une version spécifique du code

, ce qui est particulièrement utile lorsque je dois revenir en arrière après un mauvais déploiement.
* **Type de serveurs** : web, worker, api, ou all. Je n'ai pas besoin de déployer sur tous les serveurs en même temps. Parfois, je fais des changements sur le code Javascript, puis je dois juste déployer sur le web, sans toucher à l'API ou au worker.

Le processus de déploiement est principalement orchestré par des fichiers yaml Ansible, et bien sûr, c'est très simple :

* **Sur mon Macbook Pro**, si c'est pour déployer sur les serveurs web, alors construire les bundles Javascript et les télécharger sur S3.
* **Sur les serveurs cibles**, cloner le dépôt listennotes dans un dossier nommé avec un horodatage, vérifier la version spécifique, et installer les nouvelles dépendances Python si nécessaire.
* **Sur les serveurs cibles**, changer le lien symbolique vers le dossier nommé avec l'horodatage ci-dessus et redémarrer les serveurs via supervisorctl.

Comme vous pouvez le voir, je n'utilise pas ces outils CI fantaisistes. Juste des choses très simples qui fonctionnent réellement.

#### Surveillance et alertes

J'utilise [Datadog](https://www.datadoghq.com/) pour la surveillance et les alertes. J'ai quelques métriques de haut niveau dans un tableau de bord simple. Tout ce que je fais ici est de renforcer ma confiance lorsque je bidouille les serveurs de production.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/1_nrvlxilaFwNJtZDeGt01fQ.png)
_Tableau de bord Datadog pour Listen Notes, en décembre 2017._

Je connecte [Datadog](https://www.datadoghq.com/) à PagerDuty. Si quelque chose ne va pas, [PagerDuty](https://www.pagerduty.com/) m'enverra des alertes par appel téléphonique et SMS.

J'utilise également [Rollbar](https://rollbar.com/) pour surveiller la santé du code Django, qui attrapera les exceptions inattendues et me notifiera par e-mail et Slack également.

J'utilise beaucoup [Slack](https://slack.com/). Oui, c'est une entreprise à une seule personne, donc je n'utilise pas Slack pour communiquer avec des êtres humains. J'utilise Slack pour surveiller les événements intéressants au niveau de l'application. En plus d'intégrer Datadog et Rollbar avec Slack, j'utilise également [Slack incoming webhooks](https://api.slack.com/incoming-webhooks) dans le code backend de Listen Notes pour me notifier chaque fois qu'un utilisateur s'inscrit ou effectue certaines actions intéressantes (par exemple, ajouter ou supprimer des choses). C'est une pratique très courante dans les entreprises technologiques. Lorsque vous lisez certains livres sur l'histoire précoce d'Amazon ou de PayPal, vous saurez que les deux entreprises avaient un mécanisme de notification similaire : chaque fois qu'un utilisateur s'inscrivait, il y avait un son de ding pour notifier tout le monde dans le bureau.

Depuis son lancement début 2017, Listen Notes n'a pas eu de panne majeure (> 5 minutes) sauf pour [celle-ci](https://broadcast.listennotes.com/postmortem-on-apr-22-2018-outage-e5a87723d003). Je suis toujours très prudent et pratique dans ces choses opérationnelles. Les serveurs web sont significativement sur-approvisionnés, au cas où il y aurait un pic énorme dû à des événements de presse ou autre chose.

### Développement

Je travaille dans un espace de coworking [WeWork](https://refer.wework.com/i/WenbinFang) à San Francisco. Certaines personnes peuvent se demander pourquoi ne pas simplement travailler de chez soi ou de certains cafés aléatoires. Eh bien, je valorise beaucoup la productivité et je suis prêt à investir de l'argent dans la productivité. Je ne crois pas que passer plus de temps aide au développement logiciel (ou à tout type de travail de connaissance/créativité). Il est rare que je travaille plus de 8 heures par jour (Désolé, [les gens 996](https://www.nytimes.com/2019/04/29/technology/china-996-jack-ma.html)). Je veux faire compter chaque minute. Ainsi, un beau bureau privé et relativement cher est ce dont j'ai besoin :) Au lieu d'optimiser pour passer plus de temps et économiser de l'argent, j'optimise pour passer moins de temps et gagner de l'argent :)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/1_LqJym-17rqU-vyNzanCiVA.jpeg)
_Mon bureau chez WeWork_

J'utilise un MacBook Pro. J'exécute l'infrastructure (presque) identique à l'intérieur de [Vagrant](https://www.vagrantup.com/) + [VirtualBox](https://www.virtualbox.org/wiki/Downloads). J'utilise le même ensemble de fichiers yaml Ansible comme décrit ci-dessus pour approvisionner l'environnement de développement à l'intérieur de Vagrant.

Je souscris à la philosophie du [dépôt monolithique](https://danluu.com/monorepo/). Donc il y a un et un seul dépôt listennotes, contenant les scripts DevOps, le code frontend et backend. Ce dépôt listennotes est hébergé en tant que dépôt privé GitHub. Je fais tout le travail de développement sur la branche principale. J'utilise rarement les branches de fonctionnalités.

J'écris du code et exécute les serveurs de développement (Django runserver & webpack dev server) en utilisant [PyCharm](https://www.jetbrains.com/pycharm/). Oui, je sais, c'est ennuyeux. Après tout, ce n'est pas Visual Studio Code ou Atom ou quelque autre IDE cool. Mais PyCharm fonctionne très bien pour moi. Je suis old school.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/1_0qlv-bne1Ld2wuUxCeDFwQ.png)
_Mon PyCharm_

### Divers

Il y a un ensemble d'outils et de services utiles que j'utilise pour construire Listen Notes en tant que produit et entreprise :

* [iTerm2](https://www.iterm2.com/) et [tmux](https://github.com/tmux/tmux/wiki) pour les trucs de terminal.
* [Notion](https://www.notion.so/?r=d1e4526dd2924f4796cd10235cbe132e) pour les listes de choses à faire, wiki, prise de notes, documents de conception

.
* [G Suite](https://gsuite.google.com/) pour le compte email @listennotes.com, le calendrier, et autres services Google.
* [MailChimp](http://www.mailchimp.com/monkey-rewards/?utm_source=freemium_newsletter&utm_medium=email&utm_campaign=monkey_rewards&aid=da29e56f1e479faf6b4ef3f72&afl=1) pour envoyer la [newsletter mensuelle par email](https://us16.campaign-archive.com/home/?u=da29e56f1e479faf6b4ef3f72&id=ba72067923).
* [Amazon SES](https://aws.amazon.com/ses/) pour envoyer des emails transactionnels et certains emails marketing.
* [Gusto](https://gusto.com/r/wenbin) pour me payer et payer les contractants qui ne viennent pas d'Upwork.
* [Upwork](https://www.upwork.com/) pour trouver des contractants.
* [Google Ads Manager](https://admanager.google.com/home/) pour gérer les annonces de ventes directes et suivre les performances.
* [Carbon Ads](https://www.carbonads.net/) et [BuySellAds](https://www.buysellads.com/) pour les annonces de repli.
* [Cloudflare](https://www.cloudflare.com/) pour la gestion DNS, CDN, et pare-feu.
* [Zapier](https://zapier.com/) et [Trello](https://trello.com/) pour rationaliser le flux de travail des [interviews de podcasteurs](https://www.listennotes.com/interviews/).
* [Medium](https://broadcast.listennotes.com/) pour le blog de l'entreprise (évidemment).
* [Godaddy](https://www.godaddy.com/) et [Namecheap](https://www.namecheap.com/) pour les noms de domaine.
* [Stripe](https://stripe.com/) pour recevoir de l'argent des utilisateurs (principalement pour l'[API](https://www.listennotes.com/api/)).
* [Google speech-to-text API](https://cloud.google.com/speech-to-text/) pour transcrire les épisodes.
* [Kaiser Permanente](https://healthy.kaiserpermanente.org/) pour l'assurance santé.
* [Stripe Atlas](https://atlas.stripe.com/) pour incorporer Listen Notes, Inc.
* [Clerky](https://www.clerky.com/) pour générer des documents juridiques pour la levée de fonds (SAFE) et l'embauche de contractants qui ne viennent pas d'Upwork.
* [Quickbooks](https://www.referquickbooks.com/s/Wenbin) pour la comptabilité.
* [1password](https://1password.com/) pour gérer les identifiants de connexion pour des tonnes de services.
* [Brex](http://brex.com/signup?rc=oPLQ0ZQ) pour la carte de crédit

, vous pouvez obtenir des crédits AWS incrémentiels de 5000 $, qui peuvent être appliqués en plus des crédits AWS de WeWork ou Stripe Atlas.
* [Bonvoy Business Amex Card](http://refer.amex.us/WENBIFIUoH?XLINK=MYCP)

, vous pouvez gagner des points Marriott Bonvoy pour des hôtels de luxe et des vols. C'est le meilleur programme de points de carte de crédit pour voyager :)
* [Capital One Spark](https://www.capitalone.com/small-business-bank/) pour le compte courant.

### Gardez votre calme et continuez



Comme vous pouvez le voir, nous vivons dans une époque merveilleuse pour démarrer une entreprise. Il existe tant d'outils et de services prêts à l'emploi qui nous font gagner du temps et de l'argent et augmentent notre productivité. Il est plus possible que jamais de construire quelque chose d'utile pour le monde avec une petite équipe (ou même une seule personne), en utilisant une technologie simple et ennuyeuse.

Avec le temps, les entreprises deviennent de plus en plus petites. Vous n'avez pas besoin d'embaucher des tonnes d'employés à temps plein. Vous pouvez embaucher des services (SaaS) et des contractants à la demande pour faire les choses.

La plupart du temps, le plus grand obstacle à la construction et à la livraison de choses est la sur-réflexion. Et si ceci, et si cela. Mon ami, vous n'êtes pas important du tout. Tout le monde est occupé dans sa propre vie. Personne ne se soucie de vous et des choses que vous construisez, jusqu'à ce que vous prouviez que vous méritez l'attention des autres. Même si vous ratez le lancement initial du produit, peu de gens le remarqueront. [Pensez grand, commencez petit, agissez vite](https://hackernoon.com/think-big-start-small-act-fast-6fdab1f771ea). Il est absolument acceptable d'utiliser la technologie ennuyeuse et de commencer quelque chose de simple (même laid), tant que vous résolvez réellement des problèmes.

%[https://twitter.com/wenbinf/status/1082725746160746496?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1082725746160746496&ref_url=https%3A%2F%2Fbroadcast.listennotes.com%2Fmedia%2F622ba96d011f0ebfd9712504b7e353c3%3FpostId%3D56697c2e347b]

Il y a tellement de personnes de type [cargo-cult](http://stevemcconnell.com/articles/cargo-cult-software-engineering/) maintenant. Ignorez les bruits. Gardez votre calme et continuez.

---

Si vous n'avez pas encore utilisé Listen Notes, essayez-le maintenant :

[https://www.listennotes.com/](https://www.listennotes.com/)