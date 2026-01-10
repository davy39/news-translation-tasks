---
title: Comment j'ai construit et lancé un chatbot en un week-end
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-26T09:01:36.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-and-launched-a-chatbot-over-the-weekend-ad8efc522f33
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jqRtqR-Cdozt2FjBzkY9_w.jpeg
tags:
- name: '#chatbots'
  slug: chatbots
- name: Facebook
  slug: facebook
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment j'ai construit et lancé un chatbot en un week-end
seo_desc: 'By Mike Williams

  Take your idea to functional bot in hours, get real user feedback, and launch before
  the weekend is over! ?


  _[Art Chatbot](http://www.artchatbot.com" rel="noopener" target="blank" title=")-
  Discover, learn about, and purchase artwor...'
---

Par Mike Williams

#### Passez de l'idée à un bot fonctionnel en quelques heures, obtenez des retours d'utilisateurs réels et lancez avant la fin du week-end ! ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*jqRtqR-Cdozt2FjBzkY9_w.jpeg)
_[Art Chatbot](http://www.artchatbot.com" rel="noopener" target="_blank" title=") - Découvrez, apprenez et achetez des œuvres d'art via Messenger_

Les chatbots ne sont pas nouveaux. Mais c'est une technologie que la plupart d'entre nous avons probablement lue, peut-être utilisée, et pourtant ne comprenons pas vraiment, simplement en raison du manque d'exposition quotidienne et prolongée.

Pendant des mois avant le vendredi dernier, j'avais enregistré des publications spécifiques sur les chatbots (comme [Chatbots Magazine](https://chatbotsmagazine.com)), aimé des publications Facebook sur les chatbots, et même voté pour certains sur [Product Hunt](https://www.producthunt.com/topics/bots).

Je voulais changer ma compréhension des chatbots et je me suis lancé le défi d'apprendre autant que possible pendant le week-end. J'avais décidé qu'il était temps de vraiment comprendre les chatbots en maîtrisant les fondamentaux et en construisant le mien.

#### Comme pour la plupart des projets et [entreprises que j'ai lancées](https://medium.com/thinkbox-io-stories/sharing-economy-scaled-to-hundreds-of-users-in-hours-70e4b8cc72eb), j'ai commencé par définir les éléments suivants :

* Calendrier : Dimanche était ma date limite puisque c'était un projet de week-end.
* Objectifs : Apprendre les outils existants pour les développeurs de chatbots que je pourrais utiliser pour tirer parti de la technologie et construire par-dessus (j'ai choisi [Chatfuel](http://www.chatfuel.com)). Cela me fournirait une compréhension fondamentale des chatbots.
* Résultat de succès : Construire un chatbot fonctionnel qui fait une chose bien, itérer sur les retours d'utilisateurs réels, et lancer.

Contrairement aux projets passés, je n'avais pas l'idée exacte en tête avant de prendre la décision de commencer.

J'avais une fenêtre ouverte sur mon ordinateur portable affichant une impression d'artiste limitée que je regardais (["Pablo Judicial" d'Alec Monopoly](https://artlife-gallery.myshopify.com/collections/alec-monopoly/products/alec-monopolys-pablo-judicial-diamonds-and-gold-serigraph-screenprint)). J'ai simplement tapé "art chatbot" dans Google pour voir s'il existait déjà un chatbot pour acheter des œuvres d'art.

À ma surprise, il n'y en avait pas. Je savais que ma passion pour l'art était le complément parfait pour mon désir de week-end de maîtriser les chatbots.

J'ai ensuite supprimé l'espace dans ma recherche et j'avais le nom "Art Chatbot" devant moi. 9 $ et quelques secondes plus tard, et j'avais aussi le [domaine](http://www.artchatbot.com).

Comme il était encore tôt samedi matin et que ce qui précède avait pris place en environ 30 minutes, j'avais une heure ou deux pour créer le logo (en utilisant le [créateur de logo Squarespace](https://logo.squarespace.com/)).

J'ai ensuite travaillé sur le branding lean pour les actifs sociaux ([Snappa](http://snappa.io)), et j'ai également créé la [page Facebook](https://www.facebook.com/Art-Chatbot-127359754533703/) (qui est requise pour construire et tester le bot puisque c'est un bot Facebook Messenger).

![Image](https://cdn-media-1.freecodecamp.org/images/1*SmZGCWKPumBbnH7km3fmMA.png)
_Logo Squarespace en quelques minutes, et gratuit !_

Maintenant que j'avais le logo, la couverture sociale, et que la page Facebook était en ligne, j'ai invité quelques amis à aimer la page.

J'ai reçu quelques messages en retour demandant ce que je faisais avec la page et commentant le nom et le logo. Et ainsi, en quelques minutes de mon exercice de branding lean, j'avais déjà quelques retours positifs !

Je leur ai ensuite dit ce que je construisais et je leur ai demandé s'ils pouvaient tester dans les heures suivantes au cours de ma construction.

Cela a conduit à des retours d'utilisateurs réels pendant que je construisais, afin que je puisse créer une conception et un flux conversationnels plus réalistes pour mon chatbot.

Après m'être installé sur [Chatfuel](http://www.chatfuel.com), j'ai regardé quelques tutoriels YouTube et utilisé certains des modèles fournis sur Chatfuel pour apprendre en modifiant (merci [Persona](http://personabots.com/) !).

J'ai réalisé que le processus est assez simple, et qu'il s'agit surtout du flux conversationnel et du parcours utilisateur.

#### J'ai ensuite complété l'exercice de définition suivant pour définir ce que j'allais construire :

1. Cartographier le flux conversationnel et le parcours utilisateur. Dans ce cas, il s'agissait pour un utilisateur de découvrir des artistes, de voir des œuvres d'art et d'acheter des œuvres d'art.
2. Définir la structure du bot. Dans Chatfuel, cela se fait par des "blocs", que j'ai créés pour chaque état principal, sous-états, destinations, requêtes et réponses.
3. Identifier et limiter la quantité de contenu que je vais afficher. Comme je construisais cela en quelques heures, il s'agissait davantage de l'expérience et de la validation, plutôt que de la robustesse que je pensais qu'il devrait avoir.

La construction réelle du bot dans Chatfuel a commencé à la deuxième étape avec les blocs. Il était maintenant samedi après-midi et je me sentais un peu submergé par les complexités ambitieuses que je m'étais initialement fixées pour construire.

Pour surmonter cela, j'ai supprimé certains des artistes, les œuvres d'art à montrer, et ensuite les œuvres d'art disponibles afin que je puisse me concentrer sur une meilleure expérience plutôt que d'essayer de tenir compte de la quantité.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wK8vVRCRUs8wN2DLySIcnw.png)
_Art Chatbot en cours de construction depuis le tableau de bord Chatfuel._

Avant la fin du samedi, j'avais terminé la version initiale d'Art Chatbot. J'avais des amis qui testaient le chatbot et fournissaient des retours réels, et toutes les pages sociales et les actifs étaient prêts à être lancés avant la fin du week-end.

Avec cette version initiale terminée, j'ai passé le dimanche en me sentant un peu moins limité par le temps. J'ai pu me concentrer davantage sur la préparation d'un lancement ainsi que sur l'itération continue du chatbot.

J'ai également commencé à implémenter des fonctionnalités d'IA de base dans le bot. J'ai envoyé des messages à quelques entreprises de technologie artistique pour demander quelles données étaient précieuses pour elles (sachant que je pouvais facilement les collecter). De cette façon, je pourrais être sur leur radar et éventuellement construire un chatbot qui avait une certaine valeur monétaire grâce aux données à l'avenir.

J'ai terminé la journée du dimanche en créant une page de destination rapide en utilisant [Instapage](http://instapg.es/jHPw7) et en l'optimisant pour un lancement sur Product Hunt que je ferais le lundi.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CdleOwKip2abI7x4ob8xww.png)
_Création d'une [page de destination](http://www.artchatbot.com" rel="noopener" target="_blank" title=") en quelques minutes en utilisant Instapage et le contenu que j'ai utilisé depuis les blocs du chatbot._

Pour pré-lancer le chatbot, j'ai également configuré [Botanalytics](http://botanalytics.co) (pour aider à surveiller, suivre et analyser les messages), posté dans des [groupes Facebook](https://www.facebook.com/groups/aichatbots/) pour générer des utilisateurs initiaux, et ensuite rédigé mon introduction pour Product Hunt que je posterais.

J'ai également utilisé un document Google pour créer tout le texte que je partagerais sur mes canaux sociaux. Ensuite, je pourrais simplement copier le texte, ajouter l'URL de Product Hunt, et partager sur les canaux le lundi.

Le résultat est qu'Art Chatbot a atteint 100 votes sur [Product Hunt](https://www.producthunt.com/posts/art-chatbot) et avait également envoyé plus de 1 800 messages à la fin de la journée.

Je n'ai pas seulement appris sur les chatbots, mais je suis plus confiant dans ma compréhension de la technologie grâce à un cas d'utilisation réel. J'ai également affiné ma capacité et le processus que j'ai utilisé pour construire et lancer un produit rapidement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1DXJ0pQAVXQcpgt7HnQ9Nw.png)
_De l'idée samedi au [Product Hunt](https://www.producthunt.com/posts/art-chatbot" rel="noopener" target="_blank" title=") lundi !_

Dans l'ensemble, je considère le projet de week-end comme un succès — et plus important encore, c'était rafraîchissant et amusant !

J'ai également essayé de "open source" tout ce qui concerne la construction d'Art Chatbot (je l'ai documenté sur mon [réseau social](http://www.instagram.com/yoroomie)) et la feuille de route du chatbot. Je continuerai à garder tout publiquement accessible (lien ci-dessous) pour toute personne intéressée à être impliquée ou à contribuer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*J6qc7NE2cp9ITd41vtrvMQ.png)
_Analytique du jour 2 suivant le lancement sur Product Hunt._

Art Chatbot Open Sourced ? [bit.ly/artchatbotopensource](http://bit.ly/artchatbotopensource)

Avec l'enthousiasme d'apprendre et en utilisant le processus ci-dessus, il est certainement possible pour chacun de construire son propre chatbot en un week-end ! ?

_N'hésitez pas à me tweeter avec vos questions, vos retours, et faites-moi savoir quand vous lancerez votre propre chatbot et je le vérifierai/retweeterai ! Vous pouvez également consulter mon chatbot personnel que j'ai créé après ce projet de week-end [ici](http://m.me/itsyoroomieofficial)._

### *Un remerciement spécial à [Avery Andon](https://www.instagram.com/averyandon/?hl=en) et [Art Life](https://artlife.com/) pour l'inspiration lors de la création d'Art Chatbot. Art Life est la galerie en ligne officielle pour les artistes et les œuvres d'art qui sont liées en tant qu'URL dans Art Chatbot.

_Préférez-vous voir une version vidéo de ceci avec plus de détails ? Regardez cette vidéo de 12 minutes où je partage plus :_