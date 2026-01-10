---
title: Comment utiliser Amazon Simple Email Service (SES) pour remplacer votre serveur
  de messagerie basé sur un serveur
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2020-03-02T14:00:00.000Z'
originalURL: https://freecodecamp.org/news/aws-simple-email-service-email-server
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/email_square.svg
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: email
  slug: email
- name: servers
  slug: servers
seo_title: Comment utiliser Amazon Simple Email Service (SES) pour remplacer votre
  serveur de messagerie basé sur un serveur
seo_desc: "One fine day, for no discernible reason, my Ubuntu 18.04 business server\
  \ stopped forwarding mail to my Gmail address. \nJust the day before, the .forward\
  \ files I'd created in the home directories of the local server accounts I use for\
  \ email - like /ho..."
---

Un beau jour, sans raison apparente, mon serveur Ubuntu 18.04 [business server](https://bootstrap-it.com) a cessé de transférer les emails vers mon adresse Gmail. 

La veille, les fichiers .forward que j'avais créés dans les répertoires personnels des comptes locaux du serveur que j'utilise pour les emails - comme /home/office/.forward - redirigeaient joyeusement tous les emails destinés à mes adresses professionnelles vers mon compte Gmail d'utilisation quotidienne. Et puis, soudainement, ils ont arrêté.

Lorsque j'ai remarqué que quelque chose n'allait pas, j'ai immédiatement consulté les journaux de mon serveur. /var/log/mail.err affichait des messages charmants qui incluaient des choses comme :

```
status=deferred (delivery temporarily suspended: connect to alt2.gmail-smtp-in.l.google.com[219.8.202.27]:25: Connection timed out)
```

La vérification des boîtes aux lettres du serveur m'a indiqué que les emails arrivaient, mais que Postfix ne pouvait pas établir de connexion avec Gmail pour transférer les messages à mon adresse.

Naturellement, j'ai redémarré Postfix, mais cela n'a pas aidé.

```
sudo systemctl restart postfix
```

J'ai confirmé qu'il n'y avait rien qui bloquait les messages sortants de mon serveur sur le port 25 (SMTP). Ensuite, j'ai vérifié que mon domaine n'avait pas été blacklisté (il existe de [nombreux](https://mxtoolbox.com/domain) outils en ligne [tools](https://www.ultratools.com/tools/emailTest) qui peuvent le faire pour vous), et j'ai jeté un coup d'œil à l'état de mes enregistrements MX en exécutant dig depuis la ligne de commande :

```
dig MX bootstrap-it.com
```

Rien à faire. Tout semblait être en ordre.

Après quelques sessions de dépannage frustrantes, j'ai abandonné et j'ai décidé d'essayer quelque chose de complètement différent. 

En tant qu'architecte de solutions AWS et ayant co-écrit deux livres pour Wiley/Sybex sur AWS (l'un un [guide pour l'examen Cloud Practitioners](https://www.amazon.com/gp/product/1119490707/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1119490707&linkCode=as2&tag=projemun-20&linkId=c407a50c1752a2bc7d9ff3ea66ac8cdc) et l'autre pour l'[examen Solutions Architect Associate](https://www.amazon.com/Certified-Solutions-Architect-Study-Guide/dp/111950421X/ref=as_sl_pc_tf_til?tag=projemun-20&linkCode=w00&linkId=7c57304cbc082e8d089c86fda94aad7c&creativeASIN=111950421X)), ne devrais-je pas être prêt et capable de construire ma propre pile d'outils AWS qui gérera mes besoins en serveur de messagerie dans le cloud ?

Eh bien, il s'avère que j'étais à la fois prêt et - après des recherches sérieuses et des essais et erreurs - capable. Pour y parvenir, il faudrait :

* Créer un bucket S3 où les emails entrants seront stockés.
* Créer un sujet Simple Notification Service (SNS) pour m'envoyer une notification chaque fois qu'un nouvel email arrive.
* Configurer le service Amazon Simple Email Service (SES) pour prendre en charge mon domaine email (bootstrap-it.com) et gérer les emails entrants. Cela implique d'ajouter un enregistrement MX à Route 53 (où mes domaines sont gérés) et de pointer SES vers mon domaine ; d'ajouter et de vérifier chaque adresse email que je veux que SES contrôle ; puis de dire à SES d'envoyer les nouveaux messages à mon bucket S3 tout en déclenchant une alerte pour le sujet SNS.
* En supposant que vous souhaiterez également envoyer des messages email via le service, il est également judicieux de configurer SES pour signer vos messages sortants en utilisant DomainKeys Identified Mail (DKIM).

Je ne vais pas décrire toutes ces étapes en détail ici. Il existe une [excellente documentation](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email.html) disponible pour cela. Mais je vais brièvement mentionner quelques points douloureux que vous pourriez rencontrer.

Vous devrez ajouter un enregistrement MX à votre zone hébergée DNS pour chaque domaine que vous utilisez. Même si vos domaines sont gérés dans Amazon's Route 53, vous devrez fournir une valeur pour votre enregistrement. 

Ce que vous utilisez pour cette valeur dépendra de la région AWS où se trouve votre ressource SES. Dans mon cas, cela ressemblait à ceci :

```
10 inbound-smtp.us-east-1.amazonaws.com
```

Les notifications SNS arriveront dans une seule longue chaîne de texte contenant seulement quelques morceaux courts d'informations utiles mais difficiles à lire. Cela sera suffisant pour identifier le spam, mais vous aurez généralement besoin de plus d'informations que ce que vous trouverez ici. J'utilise les notifications comme un avertissement me disant qu'il y a un nouvel email dans mon bucket S3.

Visualiser les emails eux-mêmes dans votre bucket S3 via la console de gestion AWS n'est pas la fin du monde si cela ne se produit qu'une ou deux fois par mois. Mais s'ils arrivent plus rapidement que cela, vous devrez trouver un meilleur moyen d'accéder et de lire vos messages. 

Cependant, créer un protocole pour automatiser ce processus est vraiment un problème de système d'exploitation local qui nécessite un ensemble d'outils entièrement différent. J'ai résolu le problème pour moi en utilisant l'AWS CLI et un script Bash cool. Si vous souhaitez voir comment j'ai fait cela, [cliquez ici pour lire cet article](https://www.freecodecamp.org/news/bash-script-download-view-from-s3-bucket/).

_Il y a beaucoup plus de bonnes pratiques d'administration sous forme de livres, de cours et d'articles disponibles sur mon site [bootstrap-it.com](https://bootstrap-it.com).