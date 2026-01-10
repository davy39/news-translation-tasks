---
title: Les serveurs web expliqués par la gestion d'une microbrasserie
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-26T05:51:37.000Z'
originalURL: https://freecodecamp.org/news/web-servers-explained-by-running-a-microbrewery-d40b9824f882
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sxUC3MzLY70akClqwjeV9g.jpeg
tags:
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: Les serveurs web expliqués par la gestion d'une microbrasserie
seo_desc: 'By Kevin Kononenko

  When you are just getting started with web development, you might wonder, “How exactly
  do all these new concepts connect to each other when someone types https://mysite.com
  into their browser?”

  Sure, you might know the difference b...'
---

Par Kevin Kononenko

Lorsque vous commencez à vous initier au développement web, vous pourriez vous demander, *« Comment tous ces nouveaux concepts se connectent-ils exactement les uns aux autres lorsqu'une personne tape [https://mysite.com](https://mysite.com) dans son navigateur ? »*

Bien sûr, vous connaissez peut-être [la différence entre le front-end et le back-end](https://blog.codeanalogies.com/2018/04/07/front-end-v-back-end-explained-by-waiting-tables-at-a-restaurant/), mais cela ne vous donne qu'une vue d'ensemble.

Pour vous aider, j'ai voulu créer un guide complet qui explique la connexion entre le côté client (le navigateur) et le côté serveur (plusieurs serveurs).

Par exemple, connaissez-vous la différence entre un serveur et une base de données ?

Voici l'affaire : le modèle client-serveur fonctionne un peu comme une microbrasserie. Et si vous pouvez comprendre les différentes parties d'une microbrasserie, alors vous pouvez comprendre les bases des serveurs web.

![Image](https://cdn-media-1.freecodecamp.org/images/0*IodX_wZgeMUkFXTZ.)

### Le modèle Client-Serveur

Dans cette microbrasserie, votre objectif est de vendre un grand volume de bière à des bars, des magasins de spiritueux et des supermarchés. Vous avez une variété de clients qui passeront de grandes commandes chaque semaine ou chaque mois.

Cela signifie que les clients appelleront votre équipe de vente ou enverront un e-mail de temps en temps avec une **demande**. Sur Internet, cela est connu sous le nom de **client**. Un client ne partage aucune de sa puissance de calcul avec les autres membres du réseau auquel il fait une demande. Il demande simplement un certain contenu ou une certaine fonctionnalité.

De l'autre côté de l'équation, votre équipe d'exploitation de la brasserie existe afin de pouvoir brasser de la bière qui répondra aux demandes des clients. Dans cette situation, ils sont le **serveur**. Cela signifie qu'ils attendent les demandes des clients et utilisent leur puissance de calcul pour partager les ressources appropriées en fonction de la **demande**.

Un exemple courant de client est un navigateur web comme Chrome. Les serveurs sont situés dans un endroit distant et sont gérés par des entreprises comme Amazon ([Amazon Web Services](https://en.wikipedia.org/wiki/Amazon_Web_Services)).

![Image](https://cdn-media-1.freecodecamp.org/images/0*FrW6HIGAUUKvm3TL.)

Vous pourriez penser que cela est unidimensionnel, comme *« oui, ce sont les bases de tout processus d'achat ! »* Mais comme vous le verrez dans un instant, cela peut devenir un peu plus compliqué à mesure que plus de parties entrent en jeu.

### Modèle Requête-Réponse

Comme vous pouvez le voir, chaque côté a des rôles différents dans le modèle client-serveur. Le client est le demandeur, et le serveur est le répondant.

Dans un exemple très basique, un supermarché pourrait envoyer une demande comme *« Nous avons besoin de 20 caisses de bière. »* À un moment donné dans le futur, votre microbrasserie enverra la réponse : la bière qui a été demandée.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Mf5a_y-d6_eW9-As.)

De même, des navigateurs comme Chrome envoient des demandes à des serveurs centralisés, qui retournent les données demandées. Par exemple, lorsque vous chargez une page comme _reddit.com_, un serveur doit envoyer une nouvelle version de la page d'accueil basée sur les dernières données de votes et de commentaires.

![Image](https://cdn-media-1.freecodecamp.org/images/0*e-iqoDjFBr0exMC9.)

Votre prochaine question pourrait être, *« Comment Internet gère-t-il ces demandes et réponses à grande échelle ? »*

Tout d'abord, chaque appareil connecté à un réseau (comme Internet) est appelé un **hôte**. Chaque hôte a une **adresse IP** unique pour l'identification. Un **serveur DNS** (nouveau type de serveur) connecte une URL comme reddit.com à l'adresse IP d'un serveur spécifique.

Lorsque vous tapez une URL comme reddit.com, vous ne vous connectez pas directement aux serveurs web de reddit. Au lieu de cela, vous vous connectez d'abord à ce serveur DNS, fourni par l'entreprise d'hébergement. Ce serveur **répond** ensuite à votre demande avec l'adresse spécifique d'un serveur reddit. Votre navigateur peut maintenant faire la demande au serveur de reddit.

Imaginez que vous êtes un supermarché passant votre première commande de bière à une microbrasserie. Vous ne pouvez pas simplement appeler l'étage de la brasserie et ordonner aux employés de livrer votre bière ! Au lieu de cela, vous appelez un commercial ou un agent de support qui s'assurera que vous comprenez comment fonctionne la logistique : quel distributeur ils utilisent, à quelle vitesse ils peuvent livrer, etc. L'agent commercial est comme le serveur DNS, car il partagera le processus pour compléter une commande.

Après avoir accepté tout cela, vous pouvez faire une demande à l'équipe de production, qui se spécialise dans la fabrication de bière.

![Image](https://cdn-media-1.freecodecamp.org/images/0*b-6Jajds1wwYJ-mn.)

Donc, dans l'ordre :

1. Un navigateur comme Chrome entre l'URL reddit.com
2. La demande va au serveur DNS, qui répond avec l'adresse IP d'un serveur reddit
3. Le navigateur fait maintenant la demande au serveur reddit
4. Le serveur reddit répond avec la page d'accueil

Cela s'appelle parfois *« [séparation des préoccupations](https://en.wikipedia.org/wiki/Separation_of_concerns) »*. Cela permet à chaque serveur d'exécuter une fonction spécialisée afin que chaque partie puisse fonctionner de manière optimale.

### Une explication des ports

Une microbrasserie ne gère pas qu'un seul type de demande ! Dans une semaine donnée, elle pourrait gérer :

* Les factures de ses fournisseurs (comme l'entreprise d'embouteillage, le fournisseur de houblon)
* Les commandes des clients (comme discuté ci-dessus)
* Les candidatures pour des emplois de nouveaux candidats

Chacun de ces types de demandes doit être adressé à une personne spécialisée dans la brasserie.

* Les factures vont au département comptable
* Les commandes vont à l'équipe des opérations
* Les candidatures pour des emplois vont au département des ressources humaines

![Image](https://cdn-media-1.freecodecamp.org/images/0*HMz9HG_Tlup_4eoF.)

Tout comme une microbrasserie, un serveur dispose de voies pour différents types de demandes. Celles-ci sont appelées [**ports**](https://en.wikipedia.org/wiki/Port_(computer_networking)). Voici quelques exemples courants de ports :

Port 25 : SMTP (acheminement des e-mails)

Port 80 : HTTP (demandes web comme décrit ci-dessus)

Port 143 : IMAP (gestion des e-mails)

Ces ports permettent aux **hôtes** sur Internet d'interagir de manière standardisée. S'il n'y avait pas de configuration de serveur commune, Internet ne pourrait pas fonctionner comme il le fait aujourd'hui. Au lieu de cela, cela forcerait une configuration personnalisée pour interagir avec les serveurs de différentes entreprises, ce qui rendrait plus difficile pour les utilisateurs finaux d'interagir de manière transparente et fluide comme ils le font aujourd'hui.

### Où intervient la base de données ?

Jusqu'à présent, nous avons couvert le chemin d'une seule demande à un serveur web. Du côté front-end, vous écrirez le code en JavaScript, et le serveur traitera la demande en utilisant un langage comme Python ou PHP, ou un framework comme Node.js.

Mais nous n'avons pas encore couvert la partie où la base de données entre en jeu ! La base de données est écrite en SQL ou MongoDB, ou dans une gamme d'autres langages utilisés pour construire des bases de données relationnelles. Cependant, elle n'est pas stockée sur le même serveur que nous avons utilisé jusqu'à présent.

Revenons à notre microbrasserie. Les matières premières utilisées pour fabriquer de la bière incluent :

* des bouteilles
* des capsules de bouteilles
* du houblon
* du malt
* de l'eau

Votre brasserie pourrait stocker de petites quantités de ces ingrédients sur place, mais elle utilise probablement aussi des entrepôts externes. Par exemple, vous ne voudriez pas avoir des milliers ou des dizaines de milliers de bouteilles qui traînent dans la brasserie. C'est excessif. Ces ingrédients sont un peu comme les informations stockées dans une **base de données**.

Cet entrepôt externe est un peu comme un serveur qui exécute spécifiquement une base de données, ou un **serveur de base de données**. Nous séparons également cette fonctionnalité pour la rendre aussi efficace que possible.

Une base de données est simplement une structure numérique qui stocke des données. Mais un serveur fournit tous les protocoles opérationnels qui permettent à cette base de données de participer à un réseau.

Donc, disons qu'un client passe une grosse commande de 1000 caisses de bière. La microbrasserie devra communiquer avec l'entrepôt pour livrer plus de bouteilles. C'est un autre cycle de demande-réponse !

![Image](https://cdn-media-1.freecodecamp.org/images/0*Ncors9an9_OVtz3w.)

Dans ce cas, un serveur agit à la fois comme un client ET un serveur. Il prend une demande d'un utilisateur final, mais envoie également une demande à un autre serveur par la suite. Sa réponse dépend de la réponse du serveur de base de données.

![Image](https://cdn-media-1.freecodecamp.org/images/0*JkMdifVfjooBS_mZ.)

L'utilisateur final ne voit rien de tout cela, bien sûr. De leur point de vue, ils ont envoyé une demande et reçu une réponse. Ils ne voient pas la communication du serveur en coulisses.

### Exemple réel de bases de données + serveurs

[Heroku](https://en.wikipedia.org/wiki/Heroku) est un service cloud qui permet aux développeurs web de déployer facilement leurs applications avec aussi peu de code et de gestion continue que possible. Il utilise des [conteneurs virtuels](https://en.wikipedia.org/wiki/Operating-system-level_virtualization), qui vous permettent de louer une fraction d'un serveur complet pour exécuter votre application. Mais c'est un sujet pour un autre tutoriel.

En tout cas, Heroku vous permet de pousser vos derniers commits en direct vers votre conteneur virtuel avec une simple commande : **git push heroku master**_._ Ensuite, ces changements seront mis en ligne après que vous ayez acheté un domaine auprès d'un service comme [Namecheap](http://namecheap.com/), et que vous l'ayez connecté à votre application Heroku.

Mais, si vous souhaitez utiliser une base de données avec votre application en direct (ce que vous ferez probablement), vous aurez toujours besoin d'une solution d'hébergement séparée pour cette base de données. Je recommande [ClearDB](https://devcenter.heroku.com/articles/cleardb), qui dispose d'une application dans le marketplace de Heroku. ClearDB propose une version gratuite généreuse qui s'adapte à mesure que votre base de données grandit.

Donc, si vous utilisez cette pile, voici à quoi ressemblerait le processus lorsqu'un utilisateur final fait une demande qui nécessite d'accéder à la base de données.

![Image](https://cdn-media-1.freecodecamp.org/images/0*2CxK5nkEzS9qZ8GW.)

### Obtenez les derniers tutoriels

Avez-vous apprécié cette explication ? Donnez-lui un *« clap »*, ou inscrivez-vous ici pour recevoir les derniers tutoriels :