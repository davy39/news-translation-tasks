---
title: Pourquoi la sauvegarde de vos données est importante pour la sécurité informatique
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2021-01-06T18:55:04.000Z'
originalURL: https://freecodecamp.org/news/it-security-and-data-backups
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/backup-recovery.jpg
tags:
- name: Backup
  slug: backup
- name: cybersecurity
  slug: cybersecurity
- name: data
  slug: data
- name: information security
  slug: information-security
- name: Security
  slug: security
seo_title: Pourquoi la sauvegarde de vos données est importante pour la sécurité informatique
seo_desc: 'Early one recent morning my Linux workstation failed to boot. And just
  like that, all my work plans for the day ground to an immediate halt.

  This was the Linux workstation that was host to thirty years-worth of data: The
  original working drafts of al...'
---

Un matin récent, très tôt, mon poste de travail Linux a refusé de démarrer. Et tout à coup, tous mes plans de travail pour la journée se sont arrêtés net.

Il s'agissait du poste de travail Linux qui hébergeait trente années de données : les brouillons originaux de tous mes livres. Les versions maîtresses de mes vidéos de cours. Mes dossiers fiscaux, mes informations bancaires, mon coffre-fort de mots de passe et les clés d'accès à mon infrastructure cloud.

Étais-je surpris ? Pas particulièrement. La veille, j'avais du mal avec un package Python cassé et je savais qu'il y avait un risque que cela ne se termine pas bien la prochaine fois que je démarrerais la machine.

Étais-je ennuyé ? Oui.

Ai-je eu des sueurs froides en pensant à ce qui était perdu et si je pourrais un jour tout récupérer ? Non. Cela n'a jamais été une préoccupation.

En fait, dès que j'ai décidé que l'installation originale ne valait plus la peine d'être réparée, il ne m'a fallu qu'une heure environ pour tout remettre en marche. (Sans compter le temps qu'il m'a fallu pour me souvenir qu'un conflit matériel connu nécessitait que je désactive un pilote Nvidia non libre.)

Permettez-moi de souligner cela : j'ai effacé le disque corrompu, installé une copie propre d'Ubuntu Linux, et écrit des copies fraîches et fiables d'environ 20 Go de données sur la nouvelle installation en moins d'une heure.

Outre le fait d'avoir une connexion internet rapide en fibre optique, quel est mon secret ? Je sauvegarde constamment toutes mes données importantes sur plusieurs emplacements de stockage. Lorsque la catastrophe frappe, j'ai un protocole de récupération solide et testé en place.

Pour toutes les intentions et tous les buts, la partie poste de travail de ce protocole implique l'installation de mon système d'exploitation et ensuite, avec seulement deux ou trois commandes, la restauration de toutes mes données dans leur nouveau foyer. À partir de ce moment, je pourrai retourner au travail.

Je suis sûr que cette histoire vous a laissé submergé de soulagement et de sentiments chaleureux et sympathiques. Mais quel est le rapport avec la sécurité informatique ? Plus que vous ne pourriez l'imaginer.

Le fait est qu'il y a de nombreuses raisons pour lesquelles les discussions sur les sauvegardes appartiennent ici, mais si vous deviez vous limiter à une seule, ce scénario commun et opportun (adapté de mon récent livre "[Linux Security Fundamentals](https://www.amazon.com/dp/1119781469)" de Wiley/Sybex) serait celui-ci :

> _Imaginez que vous êtes responsable des systèmes informatiques alimentant les services municipaux de votre petite ville. Sans ces ordinateurs et leurs données, les travailleurs municipaux ne seront pas payés le mois prochain, la bibliothèque locale ne saura pas où se trouvent ses livres, les téléphones du système de communication du service d'urgence 911 ne sonneront pas, et le site d'information de la ville sera hors ligne._

> _Maintenant, imaginez que, un beau matin, vous vous connectez au serveur principal et vous êtes accueilli par la joyeuse nouvelle que toutes les données de vos systèmes ont été chiffrées par un pirate d'Europe de l'Est et qu'ils ne vous donneront pas la clé de déchiffrement pour restaurer votre accès à moins que vous ne leur payiez l'équivalent de quelques centaines de milliers de dollars en cryptomonnaie. Vous ne pensez pas que cela soit réaliste ? De grands hôpitaux, des services publics et des petites villes entières ont été mis à genoux par de telles attaques._

> _Quels sont vos choix ?_

* _Vous pourriez payer la rançon et espérer que les attaquants tiennent leur promesse de déchiffrer vos données. Mais, historiquement, ils ne l'ont souvent pas fait. Les criminels ne sont pas connus pour être honnêtes._
* _Vous pourriez essayer d'utiliser des outils de déchiffrement fournis par de grandes entreprises de sécurité et des agences gouvernementales (comme_ [_https://noransom.kaspersky.com/_](https://noransom.kaspersky.com/) _) et espérer qu'ils fonctionneront sur votre système. C'est certainement une option valable, mais elle ne fonctionnera pas dans tous les cas._
* _Vous pourriez effacer vos systèmes et tout reconstruire à partir de zéro. Cela pourrait être extrêmement coûteux et prendre des mois à compléter._

> _Mais savez-vous comment vous pouvez arrêter l'attaque net et vous en sortir pratiquement indemne ? Si vous aviez des copies de sauvegarde complètes et à jour de vos systèmes (à la fois les données utilisateur et les systèmes d'application eux-mêmes), alors tout ce que vous aurez à faire est de tout reconstruire à partir de vos sauvegardes._

> _Dans le pire des cas, vous serez hors service pendant une heure ou deux, et peu de gens s'en apercevront. Encore mieux, vous pourriez planifier les choses vraiment bien en concevant une infrastructure de sauvegarde "chaude" toujours en marche, préconfigurée pour prendre le relais dès que le système principal tombe en panne. C'est ce qu'on appelle le basculement, et c'est le genre de plan qui peut faire de vous un grand héros et vous valoir une grosse augmentation._

> _Toujours pas sûr de ce que les sauvegardes ont à voir avec la sécurité ?_

Ce livre Linux Security Fundamentals décrit également comment assembler correctement toutes les parties dont votre plan de récupération aura besoin. Cela inclura une évaluation minutieuse de l'importance précise de vos données pour vous et pour l'organisation pour laquelle vous travaillez.

Voici comment mon livre décrit les RTO et les RPO :

> _À quel point "rapide" est assez rapide et à quel point "complet" est assez complet ? Cela dépendra des besoins opérationnels de votre organisation. Il est courant pour les administrateurs de mesurer leurs besoins en termes d'objectif de point de récupération (RPO) et d'objectif de temps de récupération (RTO). Un RPO est l'état du système dont vous avez besoin pour pouvoir récupérer et qui sera suffisamment actuel pour les exigences minimales de votre organisation. Ainsi, par exemple, si votre système récupéré contiendra des données incluant tout sauf la dernière heure précédant le crash, vous pourrez vous en sortir. Mais une perte de deux heures de données serait catastrophique ; la perte financière ou de réputation à laquelle vous seriez confronté serait trop sérieuse. Pour une telle organisation, vous feriez mieux de vous assurer d'avoir un RPO d'une heure ou moins._

> _Un RTO, en revanche, est une mesure de la rapidité avec laquelle vous devez remettre votre système en marche à pleine vitesse avant que de très mauvaises choses ne commencent à arriver à votre organisation._

> _À titre d'exemple, supposons que votre site de commerce électronique soit hors ligne pendant 12 heures. Vous perdrez une partie de votre activité, évidemment, mais vos analystes commerciaux vous disent que tout ce qui est inférieur à 48 heures est encore supportable. Plus de 48 heures, cependant, et les clients supposeront que vous êtes hors service pour de bon et se tourneront vers la concurrence (qui, toutes choses étant égales par ailleurs, sera Amazon)._

> _Par conséquent, lorsque vous planifiez votre régime de sauvegarde, vous prendrez en compte à la fois le RPO et le RTO. Vous devrez vous assurer qu'une nouvelle sauvegarde est effectuée dans le délai du RPO (par exemple, une heure) et également vous assurer que vous pouvez accéder à vos archives de sauvegarde et restaurer avec succès les données vers les applications en moins de temps que le RTO (48 heures, dans notre exemple)._

Bien sûr, les RTO et les RPO sont généralement appliqués aux charges de travail d'infrastructure d'entreprise. Mais, à de nombreux niveaux, le point sous-jacent peut également s'appliquer à nos propres postes de travail et ordinateurs portables bien-aimés.

Si vous prenez un peu de temps maintenant — aujourd'hui — pour planifier, créer et tester votre propre protocole de récupération, vous pouvez être sûr que, un jour prochain, vous vous remercierez vous-même.

_Vous pouvez trouver beaucoup plus de contenu technologique par_ [_David Clinton sur son site web._](https://bootstrap-it.com/davidclinton) _En particulier, vous pourriez apprécier son nouveau livre,_ [_Keeping Up: Backgrounders to all the big technology trends you can’t afford to ignore_](https://www.amazon.com/gp/product/B08HL9WQ1H/)_.