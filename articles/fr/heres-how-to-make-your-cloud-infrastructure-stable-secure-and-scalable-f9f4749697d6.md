---
title: Voici comment rendre votre infrastructure cloud stable, sécurisée et évolutive.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-22T08:57:18.000Z'
originalURL: https://freecodecamp.org/news/heres-how-to-make-your-cloud-infrastructure-stable-secure-and-scalable-f9f4749697d6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eQuZJgwAnOfLXTag0G2NHA.png
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: Devops
  slug: devops
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Voici comment rendre votre infrastructure cloud stable, sécurisée et évolutive.
seo_desc: 'By Ben Sears

  Startup DevOps is hard

  There are a lot of things to worry about as a startup. Marketing, product development,
  keeping your team together. Everything tends to take the “Minimum viable” pattern
  of getting the bare minimum up so you don’t c...'
---

Par Ben Sears

### Le DevOps pour les startups est difficile

Il y a beaucoup de choses dont il faut se soucier en tant que startup. Le marketing, le développement de produits, la cohésion de l'équipe. Tout a tendance à suivre le modèle du « Minimum viable » consistant à mettre en place le strict minimum pour ne pas s'effondrer.

En tant qu'architecte cloud en entreprise, je sais de première main combien de travail peut être accompli dans le domaine du DevOps. En tant que fondateur de startup, je sais aussi le peu de temps que vous avez à consacrer aux choses — c'est plutôt comme si vous deviez consacrer du temps à tout en même temps.

L'infrastructure cloud a malheureusement aussi tendance à suivre cette règle, et toutes les « bonnes pratiques » du domaine ont tendance à suivre des modèles qui nécessitent un investissement en temps important, ce que les startups n'ont certainement pas.

Avec ce guide, j'espère vous donner un aperçu de ce à quoi peut ressembler une « infrastructure cloud minimale viable », en mettant l'accent sur la stabilité, la sécurité et l'évolutivité.

### Stabilité ?

Lorsque l'on examine la stabilité de votre infrastructure cloud, il y a quelques points clés sur lesquels se concentrer lors du développement d'une infrastructure cloud minimale viable. La restauration après une défaillance catastrophique, le redémarrage automatique et le fait de s'assurer qu'il y a suffisamment de ressources disponibles. Si vous vous concentrez sur ces trois points, vous devriez être dans une situation plutôt correcte en termes de disponibilité.

![Image](https://cdn-media-1.freecodecamp.org/images/sHwS78xWfPUSKQ258Sz-O4cn6CzJ7fDoBltn)

#### Restauration après une défaillance catastrophique (Sauvegardes automatiques)

Vous connaissez le pire scénario — vous avez « briqué » votre serveur et votre disque. La solution minimale viable à cela est d'avoir des sauvegardes planifiées et automatisées afin d'éviter la perte de données.

Selon votre fournisseur de cloud, plusieurs options s'offrent à vous. Le snapshotting de disques est généralement le moyen le plus simple de mettre en œuvre un processus de sauvegarde minimal viable, mais des méthodes plus avancées (et plus stables) incluent des sauvegardes spécifiques aux bases de données (dump de la base de données) et des systèmes distribués.

* **AWS**  
Si vous utilisez Amazon, je vous recommande d'utiliser CloudWatch. Il vous permet de créer des tâches planifiées (telles que des snapshots automatiques) — [Voir ce guide](http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/TakeScheduledSnapshot.html)
* **GCP**  
Google vous permet également de planifier des snapshots — [Voir ce guide](https://cloud.google.com/compute/docs/disks/create-snapshots)
* **Cloud Agnostique**  
Vous ne voulez pas lier votre processus de sauvegarde à votre fournisseur de cloud ? Vos données les plus importantes seront la base de données et tous les fichiers téléchargés qui pourraient être fournis. Pour une base de données, vous devriez chercher à écrire un script qui dump périodiquement la base de données et envoie les données vers un emplacement sécurisé (bucket s3 privé, système de fichiers distribué, etc.). Cette méthode sera toutefois plus sujette aux erreurs qu'une méthode spécifique à la plateforme, alors soyez prudent.

![Image](https://cdn-media-1.freecodecamp.org/images/bZcnQNF1mZvbaJy2ZIh7udvZA-Rq02vPEPD8)

### 💡 **Assurez-vous de tester votre méthode de restauration de sauvegarde, sinon vous risquez [ce qui est arrivé à GitLab,](https://about.gitlab.com/2017/02/01/gitlab-dot-com-database-incident/) où leurs 5 méthodes de sauvegarde ont échoué parce qu'ils n'avaient jamais testé la restauration.**

#### Redémarrage automatique du service en cas de redémarrage du serveur

Le redémarrage automatique comporte deux parties. Premièrement, lorsque votre application plante, redémarre-t-elle ? Et deuxièmement, lorsque votre serveur redémarre, votre application démarre-t-elle automatiquement ?

**Crontab** — Crontab est un outil utile qui vous permet de planifier des tâches facilement. L'approche la plus simple pour démarrer automatiquement votre stack est peut-être de créer une tâche crontab qui s'exécute au redémarrage — [Voir ce guide sur la façon de procéder](https://www.cyberciti.biz/faq/linux-execute-cron-job-after-system-reboot/).

**/etc/init.d** — La plupart des systèmes prennent en charge les scripts init.d. Avec init.d, vous pouvez définir des scripts qui peuvent être lancés au démarrage et qui prennent également en charge les commandes **stop, start et status** (ex. `service start myscript`) pour vous donner plus de contrôle sur vos applications. C'est un peu plus complexe qu'un crontab, mais cela vous offre plus de fonctionnalités — [Voir ce post pour configurer un script init.d](https://unix.stackexchange.com/questions/20357/how-can-i-make-a-script-in-etc-init-d-start-at-boot).

Si vous êtes intéressé par les différences entre ces méthodes, consultez [ce post de Stack Exchange](https://unix.stackexchange.com/questions/188042/running-a-script-during-booting-startup-init-d-vs-cron-reboot).

#### Redémarrage automatique du service en cas de plantage de l'application

Les applications ne sont pas toujours stables et peuvent être sujettes à des plantages à des moments inopportuns. Un bon moyen de maintenir la stabilité est d'avoir un outil capable de redémarrer automatiquement.

* NodeJS — [Forever](https://github.com/foreverjs/forever) ou [PM2](https://github.com/Unitech/pm2)
* Général — [Consultez ce post sur la façon de redémarrer des processus à l'aide de scripts bash](https://stackoverflow.com/questions/696839/how-do-i-write-a-bash-script-to-restart-a-process-if-it-dies)

#### Assurez-vous toujours qu'il y a suffisamment de ressources disponibles

L'une des raisons les plus courantes d'indisponibilité des serveurs est le manque de ressources. J'ai vu des serveurs SQL s'arrêter par manque d'espace disque et des applications de production s'arrêter par manque de mémoire. La mise en place d'une surveillance des ressources est un bon moyen d'atténuer ce risque.

* **AWS** — [CloudWatch](https://aws.amazon.com/cloudwatch/) est un bon outil de surveillance. Vous pouvez configurer des alertes par e-mail sur des événements spécifiques.
* **GCP** — [Stackdriver monitoring](https://cloud.google.com/monitoring/) offre des fonctionnalités similaires et s'intègre également à des systèmes de messagerie comme Slack.
* **Cloud Agnostique** — Crontab est encore une fois utile pour ce genre de tâche, mais vous devrez écrire un script qui vérifiera les ressources système et enverra des e-mails lorsqu'elles atteindront votre seuil.

### ✨ Assurez-vous de documenter votre méthode de démarrage automatique et vos scripts de démarrage. Gardez le code dans un système de contrôle de version, sinon vous risquez des problèmes au moment de passer à l'échelle à cause d'un code mystérieux que vous auriez oublié.

### Sécurité ?

La sécurité est malheureusement négligée lorsqu'il s'agit de la philosophie MVP. Les gens ne voient tout simplement pas la valeur gagnée par rapport à l'investissement en temps nécessaire. C'est une forme de pari dangereux, car une brèche de sécurité pourrait entraîner une perte grave de données, de la confiance des clients et de temps. Voici quelques mesures de base que vous pouvez prendre pour commencer avec un état d'esprit axé sur la sécurité.

#### SSL

De nos jours, le SSL est pratiquement une exigence pour une application SaaS moderne, de nombreux utilisateurs refusant d'utiliser des applications sans support https. Des outils comme [Let’s Encrypt](https://letsencrypt.org/) rendent l'obtention de certificats facile et gratuite.

![Image](https://cdn-media-1.freecodecamp.org/images/64MZulnr1GS6W7wXNym7C6qPZWcKOqNzBtLq)

#### Sécurité du serveur

L'une des choses les plus importantes en matière de sécurité est de gérer correctement les serveurs. Voici quelques conseils de base que vous devriez garder à l'esprit.

* Les bases de données ne doivent pas être accessibles sur l'internet public.
* Gardez les applications et le système d'exploitation à jour. Il y a souvent des mises à jour de sécurité qui protègent votre serveur contre de nouvelles vulnérabilités.
* Fermez tous les ports sauf ceux qui sont absolument nécessaires.
* N'utilisez pas de noms d'utilisateur/mots de passe — l'utilisation de clés est beaucoup plus sûre.
* Ne donnez pas la clé root aux personnes qui ont besoin d'accéder à votre serveur. Créez de nouveaux comptes et demandez-leur de vous donner leur clé publique.

#### Gestion des secrets

Les clés API, les identifiants, les configurations et toutes les données sensibles doivent être gérés. J'hésite toujours à placer ce genre de données sur le cloud, non seulement parce que je ne sais pas ce que le fournisseur de cloud peut consulter, mais aussi parce que s'ils accèdent à mon compte, tous mes secrets deviennent exposés.

* Gardez autant de secrets que possible en local.
* Ne codez pas les secrets en dur dans votre application — créez des fichiers de configuration que vous pouvez stocker en dehors du code de l'application.
* Ne stockez pas de secrets dans un dépôt Github public (méfiez-vous du cloud en général).
* Évitez le texte brut lors du stockage des mots de passe des utilisateurs et de vos propres secrets.

### Évolutivité ?

### 🚀 Dans la plupart des cas, lorsqu'il s'agit d'évolutivité, **[vous n'allez pas en avoir besoin (](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it)au début).**

Si vous avez le temps, la volonté et les compétences (ou l'argent), consacrer des efforts à l'évolutivité pourrait vous apporter des avantages futurs. Sinon, je vous recommande de l'ignorer et de vous concentrer sur les deux points précédents.

Concentrez-vous sur la livraison de votre produit à vos 5 premiers clients, et non à vos 1 000 premiers. Le mieux que vous puissiez faire en matière de construction d'une infrastructure évolutive est de réfléchir aux principes de conception lors de la création de votre application, afin que cela ne demande pas trop de travail le moment venu de passer à l'échelle. Je devrais le savoir — je suis tombé dans le piège de la sur-ingénierie de nombreuses fois.

#### Conteneurisation

![Image](https://cdn-media-1.freecodecamp.org/images/-lKBBoCdygIIPz263C-rOmkTkHOIKKOCcMh9)
_Des outils comme Docker et Kubernetes sont excellents pour l'évolutivité_

Une victoire facile en matière d'évolution est de conteneuriser votre application. Consultez Docker pour un bon guide. Voici quelques conseils :

* Permettez la configuration de votre application via des variables d'environnement. Des éléments tels que les informations de la base de données et le nom d'utilisateur/mot de passe administrateur initial seront très utiles pour construire un pipeline CI/CD et automatiser le déploiement de votre application.
* Gardez autant d'état que possible hors de votre conteneur. Cela permettra des déploiements stateless via des outils comme Kubernetes.
* Installez vos modules dans le cadre du processus de build pour réduire les dépendances et la taille de l'image.

#### Gardez les configurations de vos serveurs bien documentées

Stockez tout dans un système de contrôle de version : configurations, scripts et procédures de préparation des serveurs. Cela vous sauvera lors du passage à l'échelle. J'ai dû gérer la mise à l'échelle d'applications nécessitant des serveurs configurés d'une manière très particulière, et si la documentation fait défaut, vous allez passer un sale quart d'heure.

### Conclusion

La mise en place et la maintenance d'une infrastructure cloud représentent beaucoup de travail. Les startups ont la tâche la plus difficile car elles n'ont pas de temps et, souvent, leurs compétences font défaut en matière de DevOps. Ce que vous pouvez faire, c'est vous concentrer sur l'essentiel. Sécurité, Stabilité et, si vous avez le temps, Évolutivité.

#### [ServiceBot](https://servicebot.io?ref=medium) vous aide à faire évoluer votre SaaS en automatisant les déploiements (CI/CD), en gérant vos abonnements et en supprimant les points de friction courants entre vous et vos clients. [Découvrez-le](https://servicebot.io)