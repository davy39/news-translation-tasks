---
title: Briser le quatrième mur dans le logiciel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-03-02T01:24:12.000Z'
originalURL: https://freecodecamp.org/news/breaking-the-fourth-wall-in-software-d08a25df34b7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9HDxFkXqLFXNlf6uaml_kQ.jpeg
tags:
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: slack
  slug: slack
- name: technology
  slug: technology
- name: UX
  slug: ux
seo_title: Briser le quatrième mur dans le logiciel
seo_desc: 'By Alex Bunardzic

  Or, Everything Old Is New Again


  The phenomenon of breaking the fourth wall is well known in the world of theater
  and cinematography. The breaking of the so-called ‘fourth wall’ is typically brought
  about by one of the protagonists ...'
---

Par Alex Bunardzic

#### Ou, Tout ce qui est ancien est nouveau à nouveau

![Image](https://cdn-media-1.freecodecamp.org/images/1*9HDxFkXqLFXNlf6uaml_kQ.jpeg)

Le phénomène de [briser le quatrième mur](http://www.mentorless.com/2013/06/10/breaking-the-fourth-wall-an-homage-to-a-storytelling-technique/) est bien connu dans le monde du théâtre et de la cinématographie. La rupture du soi-disant « quatrième mur » est généralement provoquée par l'un des protagonistes du film qui se tourne soudainement vers la caméra et s'adresse au public, brisant ainsi l'illusion que nous assistons à un événement de la vie réelle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-ZLMEgqztZiLT10beiju4w.png)

Mais comment fonctionne la rupture du quatrième mur dans le logiciel ?

#### Premières interfaces homme-machine

Les premiers ordinateurs étaient grands, chers et capricieux. La manière dont les humains interagissaient avec les ordinateurs à cette époque était généralement en les alimentant avec une pile de [cartes perforées](https://en.wikipedia.org/wiki/Punched_card).

![Image](https://cdn-media-1.freecodecamp.org/images/1*BgavjyM1LTpWqUsQTWJsuA.jpeg)

#### Les premières interfaces étaient intimidantes

Vous aviez évidemment besoin d'un diplôme universitaire pour pouvoir opérer des ordinateurs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EUNOile3kX8oKD7IDha8yw.jpeg)

#### Les premières interfaces étaient maladroites

Beaucoup de boutons, d'interrupteurs, de cadrans et de leviers. Intimidant et maladroit.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rS0cq9kXkYbb5efnPpUvRA.jpeg)

#### Percée — Le texte !

La fin des années 1960 — le début des années 1970 a vu l'introduction du soi-disant terminal informatique. Émulant une machine à écrire pour entrer des commandes, puis affichant les résultats du texte évalué sur le moniteur qui ressemblait à un écran de télévision.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PN7kcdxanihRjkCkHq2ZyA.jpeg)

#### Le texte est intuitif

Pratiquement toutes les personnes trouvent le texte très intuitif — proche de la manière dont nous pensons et parlons. Il est beaucoup plus naturel de parler à la machine que de manipuler les boutons, basculer les interrupteurs et tirer les leviers (sans parler de perforer les cartes ou de réorganiser les circuits).

#### Mais les ordinateurs sont maladroits

Dans les premiers jours des ordinateurs, si vous tapiez une commande erronée ou utilisiez une syntaxe incorrecte, l'ordinateur faisait une crise. Des bêtes temperamentales !

![Image](https://cdn-media-1.freecodecamp.org/images/1*52wDsjDFZ1S5jv7daE8mMA.png)

#### Seules ces personnes savaient comment parler aux ordinateurs

Vous pouvez reconnaître certains visages sur la photo de groupe ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wRmlEjwtLIgpYLYYWqz4jg.jpeg)

#### Remplacer le texte par une interface graphique — La métaphore du bureau

Utiliser une représentation picturale pour protéger les personnes de devoir mémoriser des commandes et une syntaxe maladroites lors de l'utilisation des ordinateurs. L'idée était de présenter aux utilisateurs un décor familier — par exemple, leur bureau. Tout le monde est familier avec l'idée d'avoir un bureau avec des dossiers contenant des fichiers et aussi une corbeille à côté du bureau, etc.

Cette interface graphique (GUI) était considérée comme étant encore plus intuitive que le texte.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CPQOwLViIbTIuxjKgj4P2w.png)

#### Les GUI se sont rapidement transformées en quelque chose d'effrayant et non intuitif

Comment l'interface ci-dessous est-elle intuitive ? Elle est aussi frustrante que la syntaxe arcane et maladroite que les premiers ordinateurs exigeaient lors du traitement du texte.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PjCaq0Jgh-jyAaasASxPpg.png)

#### Une image vaut mille mots

Vrai. Mais que se passe-t-il si la plupart de ces mille mots sont du charabia ? Quelle est la valeur de cela ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*0rWYGl7qH1FMgXTRIQXGbQ.png)

#### En résumé : les gens trouvent les GUI frustrantes

Les GUI nous présentent généralement trop d'informations à la fois. Ensuite, c'est à nous de digérer tout cela et d'essayer d'en tirer un sens.

Les GUI tendent également à imposer une approche « une taille unique », qui n'est pas très centrée sur l'utilisateur.

#### Quelle est donc la solution ?

Et si, au lieu de ce tampon mal conçu constitué de représentation graphique intermédiaire, nous revenions au _texte brut_ ? Après tout, il est beaucoup plus facile de se concentrer et de suivre des fils de discussion simples que d'essayer de naviguer dans des GUI complexes et tortueuses.

#### Mais les ordinateurs sont fragiles et ne seront pas aussi indulgents que les GUI

Nous avons appris à dépendre des GUI comme nous dépendrions de roues d'entraînement. Installer des roues d'entraînement nous donne un sentiment de sécurité — nous ne pouvons pas tomber, et pourtant nous pouvons somehow avancer et atteindre notre destination.

#### On ne peut pas aller très loin avec des roues d'entraînement

Les roues d'entraînement sont bien pour pédaler dans notre jardin, mais nous ne pouvons pas les utiliser efficacement dans des situations de la vie réelle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vEw3R-I2eSOpR3-jSLHW0Q.jpeg)

#### Comment enlever les roues d'entraînement et apprendre à rouler correctement ?

Briser le quatrième mur !

Comment briser le quatrième mur ? Arrêter de pousser des pixels !

Comment pouvons-nous arrêter de pousser des pixels ?

#### Exemple frustrant

Supposons que nous commandons quelque chose en ligne. La semaine suivante, nous pouvons nous demander quel est le statut de notre commande (qui, pour une raison quelconque, n'est pas encore arrivée). Frustrés, nous ouvrons le navigateur, allons sur le magasin en ligne, nous connectons, puis essayons de naviguer jusqu'à la page _statut de la commande_.

Pour atteindre la page _statut de la commande_, nous devons naviguer à travers la jungle de menus déroutants, de mises en page changeantes, de liens mal stylisés (souvent à peine visibles sur la page), et ainsi de suite. Pour ajouter l'insulte à la blessure, ces éléments changent constamment, donc nous ne pouvons pas compter sur notre mémoire musculaire des sessions de navigation précédentes.

#### Exemple moins frustrant

Et si, au lieu de faire toutes les gymnastiques et acrobaties ci-dessus, nous faisons simplement ce qui suit :

Aller à la ligne de commande (par exemple dans [Messenger](https://www.messenger.com) ou [Slack](https://slack.com) etc.) et taper « _@nom_du_commerçant quel est le statut de ma commande ?_ »

De cette façon, nous laissons le service du commerçant (c'est-à-dire Amazon ou Etsy ou Ebay etc.) faire le travail à notre place.

Quelle est la plus intuitive des deux expériences de « vérifier le statut de la commande » ?

#### Devinez quoi — Nous venons de briser le quatrième mur dans le logiciel !

En renonçant à l'interface graphique, nous avons basculé vers l'interaction avec un service en ligne en utilisant du texte brut. Et cela semblait tout à fait naturel. Remarquez comment, en faisant cela, nous n'étions pas censés suivre une formation.

Comment est-ce possible ? Simple — au lieu d'interagir avec la machinerie informatique nue, nous avons contacté un [chatbot](https://www.chatbots.org/chatbot/) sophistiqué dont le rôle est de savoir comment analyser et interpréter le texte anglais courant.

#### Comment nous impliquer avec un chatbot ?

Nous l'_/invitons_ sur notre canal. Par exemple, supposons que nous découvrons qu'il existe un chatbot spécialisé dans les recommandations de restaurants. Nous souhaitons entrer en contact avec ce bot, et après avoir découvert le nom du bot (par exemple, _restobot_), nous « embauchons » ce bot pour qu'il travaille pour nous en tapant :

_/invite @restobot_

Une fois invité sur votre canal, ce bot restera toujours en ligne, écoutant attentivement pour que son nom soit mentionné.

#### Le bot est le tampon

De manière similaire à la façon dont une GUI était le tampon entre nous, utilisateurs humains, et la machinerie informatique froide et nue, les bots remplacent maintenant les GUI en tant que tampon chaud et flou. Les bots nous protègent de devoir traiter avec la machinerie capricieuse en traduisant nos commandes en anglais simple en quelque chose que les services informatiques sous-jacents peuvent comprendre et avec lesquels ils peuvent travailler.

#### Quelle est la proposition de valeur des bots ?

Les bots sont **_attentifs aux besoins humains_** et **_sensibles à la fragilité humaine_**.

#### Est-ce un changement révolutionnaire ?

Pas vraiment. C'est le résultat naturel des avancées que nous avons réalisées dans le domaine de l'interaction homme-machine. C'est donc davantage un changement évolutif.

En réalité, cette interface basée sur la conversation n'est pas si différente de l'utilisation des ordinateurs via des GUI. Parce que, si nous examinons de plus près ce qui se passe derrière la surface d'un traitement GUI typique, nous trouverons le scénario suivant :

* Un utilisateur veut demander à l'ordinateur de faire quelque chose
* L'utilisateur va à l'écran/page où il se voit présenter un ou plusieurs _champs de saisie_
* Ces champs de saisie, parfois appelés _zones de texte_, acceptent le texte de l'utilisateur
* La GUI écoute ensuite les gestes de l'utilisateur, tels que le geste « envoyer » ou « soumettre »
* Une fois que l'événement signalant le geste attendu se produit, la GUI se retourne et envoie du **_texte_** aux serveurs sous-jacents

#### Les GUI sont également basées sur le texte

De manière similaire à la façon dont les bots fonctionnent, les GUI possèdent également la connaissance de la manière de collecter du texte auprès des utilisateurs, puis de formuler les valeurs collectées en utilisant la syntaxe stricte que les ordinateurs back-end peuvent comprendre.

Alors, si c'est le cas, où les pixels entrent-ils en jeu ?

La plupart du temps, les pixels sont utilisés comme _décoration_. Ils habillent généralement l'écran, ou une page web, et l'habillent d'une robe qui semble plus familière aux utilisateurs. Par exemple, habiller un formulaire web pour qu'il ressemble à un formulaire papier.

Faire cela décompresse la tension que les utilisateurs peuvent ressentir lorsqu'ils tentent de travailler avec des ordinateurs. L'intention est de démystifier l'interaction et de la rendre similaire aux interactions quotidiennes que l'on peut rencontrer lors de la gestion de divers services non virtuels.

#### Supprimer les décorations pixelisées, et que nous reste-t-il ?

Un seul mot — _microcopie_.

Qu'est-ce que la _microcopie_ ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*j7jhl0iiIYca_3vIj5LuyA.png)

Dans l'exemple ci-dessus, la _microcopie_ est tout texte placé à côté du contrôle GUI. Dans un formulaire GUI, nous pouvons demander aux utilisateurs d'entrer leur numéro de téléphone. Souvent, les gens ne sont pas sûrs de vouloir le faire, et aussi pourquoi aurions-nous besoin de leurs informations personnelles ? Nous plaçons donc une phrase simple et directe entre parenthèses, juste à côté de la légende demandant le numéro de téléphone, expliquant le but de cette demande. Par exemple, « nous avons besoin de votre numéro de téléphone pour les questions liées à l'expédition ».

Ou, nous pouvons offrir une _microcopie_ un peu plus verbeuse, comme dans l'exemple ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*wbsLLL8TwN9EHY9w0PiVZQ.png)

#### Fil de conversation

Si nous imaginons supprimer tous les pixels et avec eux l'interface graphique, ce qui nous reste est un simple _fil de conversation_ qui est enregistré entre l'utilisateur et l'ordinateur.

#### Quels sont les avantages des interfaces conversationnelles ?

* Intuitif
* Sensible à la fragilité humaine (le bot essaiera de clarifier la demande humaine si elle n'est pas clairement comprise au départ)
* Familier (tout le monde est déjà complètement habitué à discuter avec sa famille, ses amis et ses collègues)
* Expérience cohérente sur tous les appareils (immune à toute préoccupation/problème lié aux mises en page, polices, couleurs, etc.)
* Garantit la pleine propriété de la conversation par l'utilisateur — le fil de discussion entièrement personnalisé est enregistré et appartient à l'utilisateur humain (transparence totale, audit complet)

#### Commerce conversationnel

Alors que nous entrons dans le monde post-web 2.0, le slogan universel « le contenu est roi » devient maintenant « le commerce est roi ». Dans le monde du web 2.0, lorsqu'un utilisateur effectue une transaction via une GUI, toutes les étapes qui se sont déroulées entre l'utilisateur et le service en ligne peuvent avoir été enregistrées par le service back-end, mais sont opaques pour l'utilisateur. Dans le monde du _commerce conversationnel_, chaque étape qui s'est déroulée entre l'utilisateur et le service en ligne est enregistrée dans le fil de conversation et appartient entièrement à l'utilisateur.

#### L'expérience de l'interface conversationnelle est similaire à l'expérience régulière du support client

De manière similaire à la façon dont appeler un numéro 1-800 était un canal de support client grand public avant l'émergence du web 2.0 et des applications mobiles, nous revenons à la conversation directe avec le support client. Seulement cette fois, au lieu d'être mis en attente indéfinie et forcé d'écouter une horrible musique d'ascenseur, nous conversons avec des bots qui sont toujours disponibles et beaucoup plus rapides et précis, plus détaillés que la main-d'œuvre humaine.

Et comme avec les scénarios 1-800, si notre appel pour une raison quelconque ne peut pas être résolu de manière satisfaisante, nous pouvons facilement _escalader_. Dans l'ancien régime, nous demandions au représentant du service client de parler à son superviseur, et dans le nouveau régime, nous demandons à l'agent bot de nous mettre en contact avec l'opérateur humain.

#### Créons notre propre bot maintenant !

Peut-être que la meilleure façon de comprendre cette transition de l'interface graphique à l'interface textuelle est de retrousser nos manches et de créer un bot à partir de zéro. Créer un bot est assez facile, car les outils nécessaires pour construire des bots ont été largement standardisés. Cependant, je pense que simplement créer un bot ne serait pas une démonstration efficace ni convaincante de l'importance du commerce conversationnel. C'est pourquoi je propose que nous apprenions ici non seulement comment créer un bot, mais aussi comment créer un bot capable de faire quelque chose d'utile pour nous.

Par exemple, créons un bot qui nous aidera à entrer en contact avec un service de commerce électronique en utilisant du texte brut comme interface utilisateur.

#### Créer un service de commerce en ligne d'abord

Pour faire court, créons un site de commerce électronique simple qui hébergera un inventaire de produits. Ces produits seront proposés à la vente, et certains des produits en vente seront également proposés à un prix réduit.

Nous utiliserons un framework de développement web à la pointe de la technologie ([Ruby on Rails](http://rubyonrails.org)) pour construire ce service. Si vous n'avez pas le framework Rails installé, veuillez vous référer au site Rails pour obtenir des instructions sur la façon de l'installer sur votre ordinateur.

Une fois installé, nous utilisons Rails pour créer un nouveau site. Ouvrez le terminal et tapez :

> rails new votre_nom_de_site

Rails créera alors le nouveau projet pour vous, et une fois que vous naviguez vers votre nouveau projet (en tapant _cd votre_nom_de_site_), vous êtes prêt à créer l'inventaire des produits à héberger sur le nouveau site. Nous allons créer une ressource appelée Product, et nous allons ensuite lui assigner plusieurs attributs :

> rails generate scaffold Product name:string price:decimal on_special:boolean discount_percentage:integer description:text

La commande ci-dessus créera la ressource appelée Product et implémentera les attributs du produit, tels que le nom du produit, son prix, s'il est en promotion ou non, et le pourcentage de réduction.

Il est maintenant temps de créer une base de données où l'inventaire des produits sera stocké. Nous le faisons en utilisant les spécifications qui ont été créées avec la commande précédente. La commande pour créer et installer la _base de données des produits_ est la suivante :

> rake db:migrate

La seule chose restante à faire est de démarrer le serveur et de vérifier que le site web que nous venons de créer fonctionne comme prévu :

> rails s

#### Maintenir l'inventaire des produits

Maintenant que nous avons créé notre base de données de produits et notre site web, nous devrions naviguer vers celui-ci et ajouter quelques produits. Ouvrez le navigateur web et accédez à l'URL _http://localhost:3000/products_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PmHQZb1yOtPz_zXyVVr1mw.png)

Bien sûr, la page d'inventaire des produits sera vide, car nous n'avons pas encore ajouté de produits. Faisons cela en cliquant sur le lien « Nouveau Produit ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*RfJg9_LeX-gmkYKWQ0vEcg.png)

Après avoir entré quelques valeurs, nous cliquons sur le bouton « Créer un produit » et le produit est maintenant ajouté à l'inventaire. Ajoutons quelques produits supplémentaires (en n'oubliant pas de cliquer sur la case à cocher « En promotion » pour certains d'entre eux).

![Image](https://cdn-media-1.freecodecamp.org/images/1*YDC7lrPbVtgGOjDBVVLJYQ.png)

Maintenant que nous avons plusieurs produits dans notre inventaire, il est temps de construire un bot de commerce conversationnel. Quelle sera l'utilité de ce bot ? Afin de garder les choses simples, nous doterons ce bot de la capacité de répondre aux commandes textuelles demandant des informations sur les produits qui sont en promotion.

#### Où notre bot vivra-t-il ?

Un bot doit être capable d'écouter les messages textuels arrivant des utilisateurs, et la meilleure façon de faire cela est d'ajouter le bot à une plateforme de messagerie. Actuellement, la plateforme de messagerie la plus attrayante pour ajouter des bots est [Slack](https://slack.com), nous allons donc l'utiliser pour démontrer comment construire un commerce conversationnel.

Inscrivez-vous sur Slack (si vous n'êtes pas déjà membre), puis allez à :

> [https://votreequipe.slack.com/services/new/bot](https://votreequipe.slack.com/services/new/bot)

![Image](https://cdn-media-1.freecodecamp.org/images/1*IJ5jy-PksVLWxlxTUSp5EQ.png)

On vous demandera de spécifier le nom de votre bot. Appelons notre bot « gofer ».

Après avoir cliqué sur le bouton « Ajouter l'intégration du bot », nous pourrons configurer notre gofer sur Slack. Premièrement, choisissons l'icône qui représentera notre bot. Je choisis mon robot préféré, Bender.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lpkWqgLIBMbpquZn-1b6lA.png)

Nous pouvons également ajouter le prénom et le nom du bot ainsi qu'une description détaillant les capacités du bot.

Après avoir enregistré l'intégration, nous remarquons le jeton API ; ce jeton est extrêmement important, car il permet l'intégration entre notre bot artisanale et la plateforme Slack. Copions la valeur de ce jeton API pour référence future.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fUUgAoumOA5Dwc_AmJd2ZA.png)

#### Dernière étape — Créer notre bot

Il est maintenant temps d'ouvrir le code source de notre site d'inventaire de produits de commerce électronique. Nous devons ajouter le bot à ce site, car le bot pourra utiliser les services intégrés à notre site d'inventaire et répondre aux questions provenant des utilisateurs de Slack.

La première chose que nous devons faire est de naviguer vers le dossier _config_ dans notre site _inventory de produits_ et de créer un nouveau fichier. Ce fichier contiendra le jeton API Slack. Nous pouvons nommer ce fichier comme nous le souhaitons ; je préfère garder son nom simple, donc je l'appelle _api.rb_. Ce fichier consistera en une seule ligne de code :

> ENV['SLACK_API_TOKEN']='xoxb-23830295172-r5CzhzDnUSZQfUfXWmR'

Ensuite, nous devons dire au framework Rails de charger ce jeton API pendant la phase d'initialisation. Nous ouvrons le fichier _config/environment.rb_, et ajoutons les deux lignes de code suivantes :

> api = File.join(Rails.root, 'api.rb')  
> load(api) if File.exists?(api)

Maintenant que nous avons déclaré le jeton API Slack et instruct Rails de le charger, nous devons ajouter notre bot au projet. La meilleure façon de le faire est de naviguer vers le dossier _app_, et de créer un nouveau dossier simplement nommé _bots_.

Créez un nouveau fichier dans le dossier _app/bots_, et nommez-le _real_time_messaging.rb_. Ce fichier traitera le thread utilisé pour que notre bot écoute les messages entrants. Ajoutez ces lignes au fichier, et enregistrez-le :

> $:.unshift File.dirname(__FILE__)

> Thread.abort_on_exception = true

> Thread.new do  
>  Gofer.run  
> end

Vous avez probablement remarqué que dans le fichier ci-dessus nous avons mentionné _Gofer_ ; nous avons réussi à nous avancer en mentionnant le bot que nous n'avons pas encore créé. Mais ce n'est pas grave, car nous ne sommes pas encore prêts à lancer le service bot écoutant sur le canal.

Le vrai défi maintenant est de comprendre comment créer notre bot nommé Gofer. Pour faire court, nous allons tricher ici en utilisant le service standard connu sous le nom de [Slack Ruby Bot](https://github.com/dblock/slack-ruby-bot). Utiliser ce service standard nous permet de gagner du temps qui aurait autrement été consacré au codage du traitement des sockets web de bas niveau, ce qui est un exercice assez complexe.

La manière la plus rapide de tirer parti de ce service standard est d'ouvrir le _Gemfile_ trouvé à la racine du projet, et d'y ajouter la ligne suivante :

> gem 'slack-ruby-bot'

Enregistrez le fichier, puis allez à la ligne de commande à la racine du projet et exécutez :

> bundle install

Lorsque l'installation est terminée, nous aurons intégré notre service standard Slack Ruby Bot, que nous utiliserons lors de la création de notre bot _Gofer_.

Mais avant de nous lancer dans la création de la logique du bot, nous devons compléter une étape supplémentaire liée à la plomberie sous-jacente nécessaire pour que le bot Slack fonctionne correctement. Naviguez vers le dossier _config/initializers_, et créez un nouveau fichier simplement appelé _bot.rb_. Il s'agit d'un fichier simple constitué d'une seule ligne de code :

> require File.join(Rails.root, 'app/bots/real_time_messaging')

Il indique simplement à Rails de charger le fichier _real_time_messaging.rb_ lors de l'initialisation. Et si nous regardons le contenu du fichier _real_time_messaging.rb_, nous verrons que, une fois le site web démarré, il exécutera également un thread responsable de l'exécution du bot _Gofer_.

Et enfin, passons à la création de la logique du bot ! Créez un nouveau fichier dans le dossier _app/bots_, et nommez-le _gofer.rb_. Ce fichier déclarera le bot _Gofer_ comme héritant de ses capacités du service standard que nous venons d'installer — _SlackRubyBot::Bot_.

> class Gofer< SlackRubyBot::Bot

Ce bot hérite de certaines capacités rudimentaires de _SlackRubyBot_, telles que la capacité de répondre aux commandes. Et ces commandes sont ce que nous allons enseigner à ce bot, en lui disant comment répondre à chaque commande qu'il reçoit.

Commençons par quelque chose d'extrêmement simple — enseignons à notre bot _Gofer_ comment gérer la commande « help ». Ajoutez la définition de commande suivante au fichier _gofer.rb_ :

> command 'help' do |bot, thread|  
>  bot.say(channel: thread.channel, text: "L'aide est en route.")  
> end

Cette commande va utiliser le bot pour qu'il affiche le texte « L'aide est en route. » sur le canal d'où il a été demandé de l'aide.

Enregistrez le fichier, allez à la ligne de commande et démarrez le serveur (_rails s_). Vous remarquerez maintenant des messages supplémentaires sur la ligne de commande lorsque le serveur démarre :

![Image](https://cdn-media-1.freecodecamp.org/images/1*OQIUlhZZXjXDj1nGPNZ3rQ.png)

Maintenant que notre bot _Gofer_ est connecté avec succès à notre équipe Slack, nous pouvons le tester. Allez sur votre équipe Slack, et vous verrez que le bot _gofer_ est en ligne (il y a une lumière de sémaphore verte à côté de son nom). Cliquez sur son nom, puis tapez « help ». Vous verrez que le bot répond immédiatement avec le texte que nous lui avons donné ci-dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rWMVuPBMqRqAeZqHFBD_Hw.png)

D'accord, bien, nous voyons donc que notre bot fonctionne. Mais comment faire pour qu'il nous dise quels produits sont proposés en promotion à l'instant ? Simple — nous ajoutons simplement une nouvelle commande (appelons-la « promo » pour simplifier) et instructons le bot de recueillir des informations sur les produits avec des prix réduits et de nous envoyer la liste.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Tey80HTwj1fi2aebg1DSFA.png)

Enregistrez le fichier, redémarrez le serveur, et basculez sur Slack pour demander à gofer ce qui est en promotion.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yeQLpX2AXEFRpWmUo_osuA.png)

Juste pour vérifier que le bot fonctionne bien en temps réel, allez à l'inventaire des produits et faites quelques changements. Par exemple, supprimez la réduction pour le Chapeau et ajoutez peut-être une réduction pour un autre produit. Après avoir fait cela et demandé à gofer ce qui est en promo, il vous donnera tous les derniers détails.

#### Conclusion

Les dernières tendances ont montré que de plus en plus de personnes tendent à passer la majorité de leur temps en ligne à discuter. Au début de l'année 2016, près d'un milliard d'utilisateurs actifs passent du temps sur Messenger et d'autres applications de chat. Alors que les gens s'habituent à envoyer des SMS à leurs amis, leur famille et leurs collègues, ils s'habituent également lentement à discuter avec des bots. Cette expérience offre une manière plus intuitive de faire les choses, et tous les signes indiquent que cette nouvelle façon d'interagir avec les ordinateurs est celle que les gens semblent préférer.

Nous avons tenté d'illustrer comment cette transition fonctionnera en guidant les lecteurs à travers une session pratique sur la création de leurs propres bots. Une fois le premier bot d'essai créé, nous réalisons que le ciel est la limite — il y a tant de choses utiles que ces bots peuvent faire, alors commençons !

#### Mise à jour

J'ai été invité par [RED Academy](http://www.redacademy.com) à donner une conférence sur le commerce conversationnel et la « révolution » des bots. La conférence a été enregistrée et peut être visionnée ci-dessous :

_Intrigué ? Vous voulez en savoir plus sur la révolution des bots ? Lisez des explications plus détaillées ici :_

[Comment construire un bot avec état](https://medium.com/bots-for-business/how-to-build-a-stateful-bot-a2703ff2d57b#.szcp08ze5)  
L'ère de l'auto-service touche à sa fin  
[Seul le manque d'UX est une bonne UX](https://medium.com/bots-for-business/https-medium-com-alexbunardzic-only-no-ux-is-good-ux-c24a7cbd12f4#.aqpbs89oj)  
[Arrêtez de construire des bots boiteux !](https://medium.com/bots-for-business/stop-building-lame-bots-b093dcd5f28b#.c3k9kcprv)  
[Quatre types de bots](https://chatbotsmagazine.com/four-types-of-bots-432501e79a2f#.9tuz1winx)  
[Y a-t-il un inconvénient aux interfaces conversationnelles ?](https://chatbotsmagazine.com/is-there-a-downside-to-conversational-interfaces-55bed7220c2f#.l43a0r4j4)  
[Les bots ne sont-ils qu'une mode ? Les GUI sont-elles vraiment supérieures ?](https://medium.com/@alexbunardzic/are-bots-just-a-fad-are-guis-really-superior-a1f52007d2b9#.a7zvp7kx2)  
[Comment concevoir un protocole de bot](https://medium.freecodecamp.com/how-to-design-a-bot-protocol-4b7584fc8d2c#.3d7xy2g5v)  
[Les bots sont les anti-apps](https://medium.com/bots-for-business/bots-are-the-anti-apps-869639cfa179#.gf5x3rw22)  
[Combien de NLP les bots ont-ils besoin ?](https://medium.com/bots-for-business/how-much-nlp-do-bots-need-a9fd55d64094#.9r83gcpve)  
[Les écrans sont pour la consommation, pas pour l'interaction](https://medium.com/bots-for-business/screens-are-for-consumption-not-for-interaction-6151fb8db6d7#.4qh22p38n)