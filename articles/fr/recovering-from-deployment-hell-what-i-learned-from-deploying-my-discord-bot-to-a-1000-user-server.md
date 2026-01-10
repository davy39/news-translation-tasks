---
title: Comment se remettre de l'Enfer du Déploiement – Ce que j'ai appris après que
  mon bot Discord a planté sur un serveur de 1000+ utilisateurs
subtitle: ''
author: Lynn Zheng
co_authors: []
series: null
date: '2021-06-04T20:41:29.000Z'
originalURL: https://freecodecamp.org/news/recovering-from-deployment-hell-what-i-learned-from-deploying-my-discord-bot-to-a-1000-user-server
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/Untitled126_20210603134910.PNG
tags:
- name: '#chatbots'
  slug: chatbots
- name: deployment
  slug: deployment
- name: discord
  slug: discord
- name: lessons learned
  slug: lessons-learned
- name: Life lessons
  slug: life-lessons
seo_title: Comment se remettre de l'Enfer du Déploiement – Ce que j'ai appris après
  que mon bot Discord a planté sur un serveur de 1000+ utilisateurs
seo_desc: 'I built a Discord AI Chatbot in my last blog post and then, to challenge
  myself, proceeded to stress-test it on a Discord server with 1,000+ users.

  In the first hour, Deployment Hell struck and I had to take the bot down for maintenance.
  Another hour...'
---

J'ai construit [un chatbot Discord IA dans mon dernier article de blog](https://www.freecodecamp.org/news/discord-ai-chatbot/) et ensuite, pour me lancer un défi, j'ai procédé à un test de stress sur un serveur Discord avec 1000+ utilisateurs.

Dans la première heure, l'Enfer du Déploiement a frappé et j'ai dû mettre le bot hors ligne pour maintenance. Une autre heure a passé et j'ai réussi à corriger mon bot et à le renvoyer.

Maintenant, mon bot est opérationnel et plus résistant que jamais. Quant à moi, j'ai survécu et même prospéré dans l'Enfer du Déploiement 🔥. Dans ce postmortem de déploiement, je vais vous montrer comment.

J'ai envoyé mon chatbot IA sur le serveur à 14h le 2 juin, et l'engouement a commencé à se rassembler autour de lui. La discussion a continué pendant un moment et tout était agréable et fluide.

À 15h20, tout a commencé à s'effondrer : Ma clé API de niveau gratuit a atteint sa limite horaire de requêtes, et je n'ai eu d'autre choix que de mettre le bot et le serveur hors ligne pour maintenance.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/IMG_0676.PNG align="left")

*Ne tenez pas compte des fautes de frappe dans mon message 😅 Cet incident m'a pris totalement au dépourvu*

Malgré avoir été frappé par l'Enfer du Déploiement dans la première heure du premier jour de la sortie de mon projet, je savais que je devais m'asseoir, prendre une profonde inspiration et me remettre de cet incident.

# Ce qui a bien fonctionné avec le déploiement

En premier lieu, je n'ai pas oublié de me féliciter pour ce qui a bien fonctionné malgré ce contretemps. Clairement, les gens étaient enthousiastes à l'idée de discuter avec mon chatbot, au point que nous avons dépassé la limite de taux.

De plus, dans la brève heure où j'ai observé les gens interagir avec mon bot en temps réel, j'ai découvert plusieurs bons choix de conception que j'ai faits consciemment, inconsciemment ou subconscemment.

## Éviter l'inflation des fonctionnalités à tout prix pendant le développement

J'ai initialement développé mon code pour un tutoriel, donc j'ai gardé mon code aussi simple et lisible que possible, sans fonctionnalités compliquées qui ne servent pas le cas d'utilisation principal de mon bot : discuter.

Cela dit, j'ai noté des **TODOs et des objectifs d'extension** dans mon code, espérant revenir à ceux-ci si nécessaire. Par exemple :

```python
 # TODO: mettre en cache l'historique de chat dans la DB et le charger
 # TODO: après chaque entrée utilisateur et réponse du bot,
 # les ajouter à l'historique de conversation pour la prochaine requête
 ...
 # FIXME: mieux vaut rendre ce bloc try-except plus granulaire
```

Alors que j'observais les utilisateurs interagir avec le bot, je suis en fait soulagé de ne pas avoir implémenté la **fonctionnalité de cache mémoire**. Plusieurs utilisateurs discutaient avec le bot en même temps, chacun suivant leur propre fil de conversation. Si je devais suivre l'historique de conversation, je devrais créer un journal unique pour chaque utilisateur, compliquant davantage les opérations de la base de données.

## Respecter le principe du moindre privilège

Une chose que j'ai apprise dans mon cours de sécurité informatique est le principe du moindre privilège (PoLP) – accorder à une application le minimum d'accès dont elle a besoin pour faire son travail.

Mon chatbot n'a besoin que de deux permissions de sécurité de bas niveau : **Voir le canal** pour lire les messages des utilisateurs, et **Envoyer des messages textuels** pour répondre aux utilisateurs.

Bien sûr, j'aurais pu lui donner plus de permissions fantaisistes comme celles montrées ci-dessous dans l'image, au cas où il en aurait besoin. Mais cela aurait violé le PoLP et qui sait si mon bot défaillant ne ferait pas tomber autre chose avec lui lorsqu'il échoue ?

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Screen-Shot-2021-06-03-at-14.21.52-1.png align="left")

*Paramètres de permission pour les bots Discord*

## Autres observations du déploiement de mon bot

Malgré sa durée de vie éphémère, mon bot m'a offert une opportunité de mener une recherche utilisateur dans le monde réel. Il s'agit d'un serveur avec 1000+ utilisateurs, et non de mon serveur de développement confortable où mes amis et moi traîons et échangeons poliment des lignes avec le bot.

Ici, j'ai observé plusieurs comportements intéressants des utilisateurs :

* Les gens ont tendance à poser au bot des **questions ouvertes** plutôt que des **questions factuelles**. Parce que j'ai construit mon bot sur la base d'un personnage de jeu vidéo, lors du développement du modèle IA, j'étais soucieux de m'assurer que le modèle apprenne les informations canoniques sur le personnage, comme le nom, l'âge et le rôle dans le jeu. J'ai été soulagé de voir que les gens sont beaucoup plus curieux de connaître la préférence du personnage du bot pour la saveur de glace que leur lieu de naissance factuel.

* Les gens utilisent beaucoup d'emoticônes :), d'emojis 😃 et de GIFs lorsqu'ils envoient des messages. Cependant, ceux-ci seront probablement traités comme des jetons `<UNKNOWN>` dans le tokeniseur du modèle IA, ce qui signifie que je devrais **nettoyer** les entrées des utilisateurs.

J'ai également eu la chance de recevoir des retours directs de la part de personnes amicales sur le serveur. Une demande de fonctionnalité que j'ai reçue était de faire en sorte que le bot attache sa réponse au fil de message d'un utilisateur, au lieu de simplement déverser sa réponse dans le canal.

Enthousiasmé par l'engouement des gens et armé d'informations issues de la recherche utilisateur, j'étais prêt à corriger mon bot et à le renvoyer dès que possible.

# Ce que je devais corriger

En tant que bonne habitude de développement, j'ai gardé mon code bien organisé et modulaire, donc le passage du bot de production à mon bot de développement ne nécessite pas plus qu'un copier-coller de la clé API du bot de développement.

Une fois que j'ai été sur mon serveur de développement, je me suis assis pour identifier les types de problèmes que je devais résoudre.

## Plantages fatals

Le bug fatal qui m'a obligé à mettre mon bot hors ligne était que j'ai atteint la limite horaire de taux de l'API. J'ai pris l'approche évidente de garder une **redondance** dans mon système : Garder une clé API alternative, et une fois que la principale est épuisée, basculer vers l'alternative, puis revenir au début de l'heure.

Mis à part cette solution de contournement, j'ai noté que cela était une solution à court terme. Si je dois correctement mettre à l'échelle mon système, je devrais faire une estimation du nombre de requêtes par heure, comme je vais en discuter à la fin de cette section.

## Nouvelles fonctionnalités pour l'utilisabilité

J'ai décidé de plusieurs nouvelles fonctionnalités qui rendront mon bot plus convivial. Voici quelques points forts :

* Comme l'ont suggéré certaines personnes du serveur, j'ai reprogrammé le bot pour qu'au lieu de déverser les réponses à différents messages des utilisateurs dans le canal, il réponde directement à chaque message de l'utilisateur dans le fil du message.

* J'ai nettoyé les entrées des utilisateurs en supprimant les emojis Unicode et les balises spécifiques à Discord `<:some_hilarious_gif>`. Cela limitera les jetons `<UNKNOWN>` que mon modèle IA recevra et l'aidera à générer de meilleures réponses.

* J'ai implémenté une commande magique `$ignore [message]` qui permet aux utilisateurs d'envoyer un message au canal sans déclencher de réponse du bot. Cette fonctionnalité vient de mon observation que, chaque fois que le bot dit quelque chose de drôle ou d'intelligent (ou les deux !), les utilisateurs font des remarques à ce sujet en envoyant un texte destiné à leurs amis (et non au bot) sur le canal. Il serait ennuyeux de recevoir une réponse du bot sur une remarque destinée à un ami. Par conséquent, j'espère que cette commande magique répondra à ce point de frustration des utilisateurs.

* J'ai implémenté des commandes magiques pour les modérateurs du serveur afin qu'ils puissent interagir avec mon bot (l'arrêter ou le redémarrer) afin qu'ils puissent garder le bot sous contrôle sans avoir à accéder à mon serveur Repl.it. Cela facilite à la fois mon travail et le leur.

## Journalisation à l'épreuve du futur

Dans mon serveur de développement confortable, il y a peu de complexité, alors que sur ce serveur de 1000+ utilisateurs où 40% des utilisateurs sont en ligne à tout moment, la complexité explose.

Il y a plusieurs canaux en plus du canal de chat dédié à mon bot, plusieurs rôles d'utilisateurs et niveaux de permission, plusieurs utilisateurs tapant en même temps, et ainsi de suite.

Bien que je ne puisse certainement pas prévenir tous les scénarios de défaillance possibles, ce que je peux faire est de protéger la partie importante de mon code avec un bloc try-except et de journaliser toutes les informations qui pourraient révéler la cause d'une défaillance. Puisque les bugs du système en temps réel sont subtils et difficiles à reproduire, la journalisation me sauvera beaucoup de maux de tête à l'avenir.

```python
except Exception as e:
            print(e, 'Canal offensant', message.channel, 
            'Message offensant', message.content, 
            'Réponse du bot offensante', bot_response, 
            sep='\n', end='\n\n')
```

## Évolutivité

L'estimation sous certaines contraintes système est l'endroit où les statistiques de base et les heuristiques entrent en jeu. L'API d'inférence de modèle de Hugging Face impose deux limites à l'évolutivité de mon système :

1. Une limite de taux de 10k jetons (caractères) par heure, ce qui représente environ 300 requêtes.

2. Un quota de 30k jetons par mois pour les comptes de niveau gratuit, ce qui représente environ 900 requêtes.

> Vous vous demandez comment j'obtiens ces chiffres ? Fait amusant : 1) [10k caractères se situent entre 1430 et 2500 mots](https://capitalizemytitle.com/character-count/10000-characters/). Nous prendrons 2100 puisque les messages Discord utilisent généralement des mots simples et courts. 2) [La longueur moyenne d'un message texte est de 7 mots](https://crushhapp.com/texting-tidbits/the-average-text-message-length-is-around-7-words). 2100 / 7 = 300 messages

Après avoir traité ces chiffres, le fait que j'ai atteint la limite de taux horaire lors de la première heure de la sortie de mon bot est un exploit assez remarquable. Les gens sont clairement enthousiastes à propos de mon chatbot spirituel. 🤷‍♀️

Supposons que l'engouement retombe et que la vie continue, considérons maintenant un scénario hypothétique où 20 utilisateurs (2% des 1000+ sur le serveur) discutent régulièrement avec mon bot, chacun pour 25 lignes, dans les deux heures suivant le dîner. Cela produit un total de 500 requêtes en deux heures (ou 250 par heure), ce qui signifie que mon bot est à l'abri de la limite de taux horaire de 300.

Cependant, en un mois, 500 * 30 = 15 000 requêtes, 15 fois plus que mon quota de 900. Si mon bot est effectivement si populaire, je devrais passer à un plan d'abonnement de niveau supérieur pour m'assurer qu'il reste disponible.

## Du code de tutoriel au code de production

Comparé à mon code de tutoriel qui s'efforce d'être simple, lisible et éducatif, mon code de production est plus long, plus compliqué, mais aussi plus robuste.

# Ce qui fait un excellent projet parallèle

Ayant émergé de l'Enfer du Déploiement, comme mon bot, je suis plus résistant que jamais et j'ai gagné de nouvelles perspectives sur les principes et les défis de l'ingénierie logicielle dans le monde réel.

En guise de conclusion, je réfléchis à ce qui rend mon chatbot Discord IA si populaire. (Le 3 juin, un jour où il était opérationnel 24 heures sur 24, il avait déjà dépassé le quota mensuel de 30k sur mon compte et celui que j'ai emprunté à un ami, totalisant 2000+ messages. 🤔)

J'ai complété et poli divers projets parallèles qui ont reçu des retours positifs, mais aucun d'entre eux n'a été aussi populaire que celui-ci. En rétrospective, il n'est pas trop difficile de voir pourquoi.

Parmi les projets dont je suis le plus fier, j'ai construit [un moteur d'échecs](https://github.com/RuolinZheng08/renpy-chess) et [un moteur de jeu de rythme](https://github.com/RuolinZheng08/renpy-rhythm) pour [le moteur de développement de jeux Ren'Py Visual Novel (VN)](https://renpy.org/). Les deux sont notés 5 étoiles sur [itch.io](https://itch.io/), une plateforme populaire pour publier des jeux indépendants.

Ces projets, cependant, sont des moteurs open-source destinés aux développeurs pour les intégrer dans leurs jeux VN plus que des jeux autonomes qui peuvent divertir les joueurs pendant des heures.

En comparaison, mon chatbot Discord IA parvient à capturer chacun des éléments suivants qui distinguent un **excellent** projet parallèle d'un bon :

* **Public** : J'ai la chance d'avoir ce serveur amical avec 1000+ utilisateurs qui sont ouverts à l'expérimentation avec le bot et me fournissent des retours utiles.

* **Accessibilité** : Pour que les gens profitent de mon chatbot, ils n'ont rien de spécial à ajouter à leur routine - pas même ouvrir une nouvelle application web - ils se connectent simplement à Discord comme d'habitude, et voilà, le bot est là pour discuter !

* **Interactivité** : Sans composants interactifs, même le jeu visuellement le plus époustouflant échouera à retenir l'attention des joueurs. Rien à craindre pour mon chatbot cependant : Comme un ami fidèle, il a toujours quelque chose à dire chaque fois que vous avez besoin d'une bonne discussion.

Si vous souhaitez en savoir plus sur ma méthodologie pour travailler sur des projets parallèles, consultez mon précédent article de blog :

%[https://www.freecodecamp.org/news/how-i-built-my-one-person-open-source-project/] 

Consultez également mon tutoriel sur les chatbots !

%[https://www.freecodecamp.org/news/discord-ai-chatbot/] 

%[https://youtu.be/UBwvFuTC1ZE] 

Vous pouvez également essayer cela en JavaScript :

%[https://youtu.be/XR6JFRLxe5A]