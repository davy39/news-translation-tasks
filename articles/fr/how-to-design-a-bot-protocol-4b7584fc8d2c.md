---
title: Comment concevoir un protocole de bot
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-04-21T21:11:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-design-a-bot-protocol-4b7584fc8d2c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xjG1GNLJJeikWDyBttJGzw.jpeg
tags:
- name: AI
  slug: ai
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: bots
  slug: bots
- name: Conversational UI
  slug: conversational-ui
- name: 'tech '
  slug: tech
seo_title: Comment concevoir un protocole de bot
seo_desc: 'By Alex Bunardzic

  One of the biggest fallacies about the present bot craze is that bots need to be
  capable of offering nuanced, sophisticated conversational experience (How does your
  bot say ‘ketchup’?). That sentiment is completely unsubstantiated, ...'
---

Par Alex Bunardzic

L'une des plus grandes idées fausses concernant l'engouement actuel pour les bots est que les bots doivent être capables d'offrir une expérience conversationnelle nuancée et sophistiquée ([Comment votre bot dit-il 'ketchup' ?](https://medium.com/hh-design/how-does-your-bot-say-ketchup-9bdc3fd3cb86#.4jacwzd65)). Ce sentiment est complètement infondé et est probablement basé sur le fait de voir trop de films de science-fiction hollywoodiens sophistiqués.

En réalité, les bots ne sont qu'une extension du comportement humain régulier que nous pouvons observer dans diverses situations sociales. Et parce que les bots sont une autre des nombreuses façons dont nous automatisons le traitement de l'information, ils obéissent aux mêmes contraintes que les autres produits logiciels. En un mot, les bots obéissent à un certain modèle de comportement connu sous le nom de _protocole de communication_.

#### Qu'est-ce qu'un protocole ?

Lorsque deux parties communiquent, elles le font en échangeant des messages. Ce processus de messagerie peut être primitif, comme l'envoi de signaux de fumée :

![Image](https://cdn-media-1.freecodecamp.org/images/hmrtVClqLTtO3gDgzZPZMvNK--mf9CGX4zE8)

Ou, il peut être plus avancé, moins désordonné, comme par exemple passer un appel téléphonique ou envoyer un message texte.

Indépendamment du mécanisme utilisé pour échanger des messages, ce qui est vraiment critique, c'est l'accord mutuel et la compréhension de toutes les parties impliquées concernant la signification de chaque message. Ce qui est d'une importance primordiale dans tous ces scénarios, c'est d'éviter les bavardages libres et désinvoltes.

Considérez un échange typique de messages qui se produit lorsqu'un pilote approche la tour de contrôle du trafic aérien. Il serait extrêmement dangereux dans de telles situations dangereuses de permettre au pilote et à l'opérateur de contrôle du trafic aérien de s'engager dans des discussions ouvertes et non structurées. Au lieu de cela, ils suivent un protocole de communication prédéterminé.

Chaque phrase prononcée par le pilote ou l'officier de contrôle du trafic se termine toujours par le mot-clé 'over'. Ce mot-clé signale à l'autre partie que la personne qui parlait a terminé de parler et écoute maintenant avec une attention totale. De plus, la personne qui écoutait commence toujours à parler avec le mot-clé 'roger' (ou 'roger so far'), signalant qu'elle a parfaitement compris ce que l'autre personne disait (parfois 'roger' peut être remplacé par 'wilco', impliquant 'will comply', signifiant que le message a été reçu clairement).

Comme il est assez évident dans l'exemple ci-dessus, le protocole de communication mis en œuvre dans des situations hautement dangereuses (comme l'atterrissage d'un avion) doit, par nécessité, être extrêmement contraint et rigide. Aucune déviation dans la syntaxe des messages échangés n'est autorisée. Le respect strict de ces règles assure une communication claire et sans entrave.

#### Protocoles dans des situations moins critiques

Toutes les situations où les gens communiquent ne sont pas aussi critiques et potentiellement dangereuses que l'atterrissage d'un avion. Pourtant, cela ne signifie pas nécessairement qu'il est acceptable de jeter toute prudence aux vents lorsque l'on traite des problèmes de communication dans des situations moins intenses.

Considérez un instant comment les gens communiquent lorsqu'ils traversent la frontière. À l'approche de la frontière, les voyageurs sont interrogés par l'agent de contrôle frontalier. C'est l'agent qui donne le ton de la conversation, et les voyageurs sont bien avisés de se conformer et de suivre les instructions de l'agent. Cela signifie répondre à toutes les questions avec des phrases courtes et précises, souvent avec des déclarations succinctes 'oui' ou 'non'. Un tel protocole établi de manière impromptue assure un passage frontalier fluide et efficace, tout en permettant aux agents de sécurité d'accomplir leurs tâches sans accroc.

La plupart des gens ne semblent pas avoir de problèmes à saisir de tels indices et suivent généralement le protocole impromptu proposé sans aucune difficulté.

Ou, considérons une situation encore moins critique, comme le protocole de communication qui se produit lorsque nous entrons dans une fonction sociale de quelque sorte (par exemple, une soirée au théâtre). En entrant dans le théâtre, nous sommes accueillis par le concierge. C'est le concierge qui donne le ton de la conversation, et la plupart des gens se conforment volontiers. Cette conformité assure un service fluide et efficace, car nous sommes accueillis et ensuite conduits dans le bâtiment. Quelques phrases courtes et courtoises sont échangées avant que nous soyons montrés à l'aire de vérification des manteaux et ensuite conduits à nos sièges.

#### Le protocole définit le ton de la conversation

Indépendamment de l'intensité ou de la détente de la conversation, il y a toujours un protocole de communication sous-jacent, souvent tacite. Même lorsque nous faisons des achats de loisir, nous remarquons comment la conversation entre les clients et le personnel obéit à un certain protocole de communication plus ou moins formel.

C'est généralement les personnes qui manquent de compétences sociales et qui désobéissent à ces protocoles tacites qui sont vues et jugées comme étant désagréables et déplaisantes. Nous voyons donc que le respect des protocoles préétablis est un signe de comportement bien ajusté.

C'est aussi généralement le côté servant de l'interaction (comme une réceptionniste au cabinet du médecin, ou un hôte à la fonction sociale, etc.) qui établit le protocole et le ton de la conversation. S'il y a des règles strictes qui doivent être injectées dans la conversation, de telles règles sont soulevées dès le début de la conversation. En soulevant des règles, la partie servante établit le ton formel de la conversation et est également responsable de la gestion de tout problème, exception et bizarrerie qui peut survenir pendant la session.

La chose importante à noter est à quel point cette définition préalable du ton nous semble naturelle et normale. Chaque fois que nous nous trouvons dans une situation où aucune règle tacite et aucun protocole spécifique n'ont été établis, nous avons tendance à nous sentir mal à l'aise, incertains de notre prochain mouvement.

#### Les bots doivent établir le protocole

Malgré certaines des récentes affirmations excitées et exagérées, l'émergence des bots dans le courant dominant n'est pas une avancée technologique révolutionnaire. Les bots grand public sont une simple extension évolutive de nos tentatives régulières et continues d'automatiser autant de tâches banales que possible.

En fait, les bots ne sont pas vraiment si différents des bonnes vieilles applications GUI. Rappelez-vous comment, chaque fois que nous nous connectons à une application GUI, nous obéissons à un certain protocole de communication. L'application donne le ton et nous guide à travers l'expérience. La seule différence entre les applications GUI et les bots est qu'avec le GUI (comme le nom l'indique), la plupart des messages qui nous sont présentés par le service sous-jacent sont picturaux/graphiques. Avec les bots, la plupart des messages présentés par le service sous-jacent sont textuels.

Et si nous grattons la surface des applications GUI, nous réalisons que toutes ces représentations graphiques sont en réalité traduites en commandes textuelles puis envoyées au service back-end pour traitement. Par exemple, si je communique avec un bot, je peux dire : « Donnez-moi le statut de ma commande. » Et si je communique avec une application GUI, je peux cliquer/appuyer sur le lien « Statut de la commande », et cette action sera convertie par le navigateur en une déclaration textuelle — quelque chose comme « GET [http://domain.com/user/1/order?id=42](http://domain.com/user/1/order?id=42) HTTP/1.1 ». Dans les deux cas (GUI et bot), la réponse reviendra sous forme de texte. Même différence, vraiment.

La seule différence substantielle est que, lors de la communication avec les bots, je peux m'appuyer sur ma compréhension intuitive de la langue naturelle, tandis que si je voulais envoyer un message texte à l'application GUI, je devrais suivre une formation formelle sur la manière de formuler une chaîne syntaxiquement correcte que le service back-end comprendra.

Mais le point principal reste — les applications GUI et les bots établissent le protocole de communication et donnent le ton. Ce n'est définitivement pas l'utilisateur qui donne le ton. L'utilisateur obéit soit au protocole proposé et se conforme au ton de la conversation, soit abandonne par frustration toutes les tentatives de profiter du service disponible.

Cela peut sembler rude et inconsidéré au premier abord, mais c'est en réalité une bonne chose. Comme nous l'avons vu, une communication claire, sans ambiguïté et cohérente est absolument impossible sans établir des limites nettes en donnant le ton et en définissant quelques règles de base. Sinon, nous risquons de nous retrouver avec un système bavard et désordonné qui n'est bon ni pour les utilisateurs finaux ni pour les entreprises offrant les services.

#### Que valorisent les entreprises ?

Si vous êtes responsable de la gestion d'une entreprise, vous serez probablement d'accord avec l'énoncé selon lequel l'une des choses les plus importantes dans les affaires est la _prévisibilité_. Personne n'aime être dans une position d'incertitude, surtout si l'avenir de beaucoup d'autres personnes pourrait être en jeu.

C'est pourquoi il est de la plus haute importance que la confiance soit établie lors de l'offre de services d'automatisation à une entreprise. Tout service dans lequel une entreprise serait prête à investir doit offrir des assurances solides de prévisibilité et de répétabilité. En résumé, les services d'automatisation doivent offrir un comportement cohérent, constant et entièrement contrôlable.

C'est précisément à cause de telles valeurs commerciales primaires que les bots de service doivent être accompagnés de protocoles de communication entièrement définis et clairs qui établissent sans ambiguïté le ton de la conversation. En tant que constructeurs de bots, nous devons être en mesure de démontrer aux entreprises que nos bots sont entièrement prévisibles. Nous ne pouvons y parvenir qu'en démontrant comment ils présentent un comportement répétable et entièrement contrôlable.

#### Les bots suivent l'interaction de l'utilisateur

Un aspect important des bots qui les différencie des applications GUI traditionnelles est leur attention exclusive à l'utilisateur humain. Alors que les applications GUI ne se soucient pas de qui les utilise, les bots s'en soucient définitivement. Contrairement aux applications GUI, qui proposent une approche « taille unique » pour offrir des services automatisés, les bots proposent des services hautement personnalisés. La personnalisation est incarnée dans le fil de conversation qui se déroule entre l'utilisateur humain et le bot.

Malgré le fait que différents utilisateurs interagissent avec le même bot, l'historique de leur interaction est totalement unique. Il ne pourrait pas y avoir deux fils de discussion similaires, et la variété des échanges d'informations est sans fin.

Un autre point important est que les bots conservent la mémoire de chaque étape individuelle de chaque utilisateur individuel et peuvent rappeler et résumer ce qui s'est passé dans un contexte donné. Les applications GUI n'ont jamais été conçues avec des intentions similaires, ce qui les fait paraître vraiment rudimentaires, presque barbares en comparaison.

#### Bots et changement de contexte

Lorsque les humains communiquent, ils utilisent leurs compétences de bon sens pour signaler les uns aux autres lorsque le contexte de la conversation change. Par exemple, lors du premier contact, un contexte de courte durée (souvent appelé « rencontre et salutations ») s'établit. Ce contexte est généralement défini en utilisant des phrases d'ouverture courantes, telles que « Salut, comment ça va ? », « Bonjour ! », « Comment allez-vous ? », « Comment ça va ? », etc. Selon que la session de rencontre et de salutations se produit entre des étrangers ou entre de vieux amis, les phrases d'ouverture peuvent changer. Mais le ton général reste assez prévisible, tout comme l'intention tacite de mettre rapidement fin à la situation éphémère de rencontre et de salutations et de passer à une interaction plus concrète.

Suite à la salutation initiale, le contexte change généralement de manière très abrupte et ce changement est signalé par le changement de ton de la conversation. Selon que la rencontre est informelle, ou une session d'affaires ou même juridique plus formelle, le ton approprié prendra le dessus et prévaudra.

Un bot incapable de détecter et d'effectuer un changement de contexte similaire est un bot complètement inutile. Construire un bot capable de se comporter de manière simpliste, par réflexe, en maintenant toujours le même ton de conversation, n'attirera pas beaucoup d'attention parmi la base d'utilisateurs.

À cause de ce danger, nous devons établir quelques directives sur la manière de mettre en œuvre un protocole de bot robuste et viable.

#### Directives du protocole de bot

En général, tout bot offrant des expériences conversationnelles aux utilisateurs humains doit fournir quatre niveaux de protocole de communication :

1. _Protocole de commande_
2. _Protocole de mot-clé_
3. _Protocole de phrase structurée_
4. _Protocole libre (informel)_

Les quatre protocoles ci-dessus sont ordonnés en fonction de leur rigidité et de leur strictness — du plus contraint, strict et rigide (c'est-à-dire le protocole de commande) au moins strict et au moins formel (bavardage informel ou badinage).

#### Protocole de commande

Avec les commandes, nous revenons à l'interface de ligne de commande ([CLI](https://en.wikipedia.org/wiki/Command-line_interface)). L'utilisation d'une interface de ligne de commande est généralement le domaine des programmeurs informatiques et des administrateurs système. Cela nécessite un certain niveau de formation formelle, car les systèmes d'exploitation informatiques ne sont pas conçus avec des expériences conversationnelles en tête. La rigidité de la syntaxe des commandes est nécessaire pour que le système d'exploitation sous-jacent puisse exécuter les commandes avec le moins d'ambiguïté possible.

Dans le monde des bots, cette rigidité doit être adoucie car le public cible n'est pas composé de professionnels hautement formés. Les utilisateurs occasionnels ne doivent pas être censés savoir comment formuler des commandes syntaxiquement correctes. Un bot doit servir d'intermédiaire, ou de concierge. Cet intermédiaire doit être capable d'accepter les commandes émises par les utilisateurs. L'intermédiaire traduira ensuite les commandes dans une forme plus syntaxiquement correcte. Une forme syntaxiquement correcte est nécessaire pour la machinerie back-end afin qu'elle puisse traiter la demande sans risque d'introduire des effets secondaires indésirables.

Pour cette raison, les commandes offertes par les bots doivent être des commandes d'un seul mot. Sachant que les bots sont également censés répondre aux messages d'un seul mot qui peuvent ne pas être des commandes strictes, nous devons concevoir les commandes des bots de manière à ce qu'elles se distinguent immédiatement. Typiquement, cela signifie qu'une commande de bot doit être construite de manière à ce qu'elle commence par un caractère spécial. Par exemple, une commande demandant un rappel au bot sur les commandes qu'il comprend commencerait généralement par un caractère '/' (barre oblique). Il existe une différence sémantique entre dire 'help' et '/help'. Le premier message (un simple 'help') n'est pas interprété par un bot comme une commande. Le deuxième message (la soi-disant _commande slash_ '/help') est interprété par un bot comme une commande. Le résultat du traitement de cette commande serait très différent du résultat du traitement d'un simple message 'help'.

#### Protocole de mot-clé

Contrairement aux commandes de bot, les mots-clés sont des messages moins formalisés, moins stricts que les utilisateurs envoient au bot. Contrairement aux commandes de bot, la principale responsabilité des mots-clés est de gérer le changement de _contexte de conversation_.

Dans le cas des commandes de bot, il n'y a pas de changement de contexte — le bot reconnaît la commande et l'exécute simplement. L'utilisateur peut demander au bot de l'aide (_/help_) autant de fois qu'il le souhaite, le bot répondra toujours avec la même liste exacte de commandes qu'il comprend. Selon la nature de la commande émise par l'utilisateur, le bot peut demander une confirmation ultérieure. Mais il y aura toujours des commandes qui s'exécutent simplement de manière réflexe (par exemple, il serait absurde que le bot demande à l'utilisateur « Êtes-vous sûr de vouloir que j'exécute la commande _/help_ ? »).

Les mots-clés diffèrent des commandes en ce sens qu'ils sont destinés à alerter le bot que le contexte de la conversation a changé. Similaires aux commandes, les mots-clés sont formatés comme des instructions d'un seul mot, ponctuées d'un caractère spécial (généralement un caractère '@').

Par exemple, un utilisateur peut être en train de discuter avec le bot des meilleurs endroits pour déjeuner, lorsque l'utilisateur interrompt le contexte en disant « Bot, peux-tu vérifier avec mon @médecin quand elle est disponible pour un rendez-vous ? » Dans ce message, le mot _@médecin_ est le mot-clé qui déclenche la compréhension du bot que le contexte doit changer. À la réception du message contenant ce mot-clé, le bot changera le contexte de la discussion sur les endroits pour déjeuner à la recherche du prochain créneau disponible pour le rendez-vous chez le médecin.

Contrairement aux commandes, le protocole de communication par mots-clés implique souvent que le bot peut poser des questions ultérieures. Ces questions ultérieures, déclenchées par la présence du _@mot-clé_ préétabli, seront toujours posées dans le nouveau contexte établi. Dans l'exemple ci-dessus, puisque l'utilisateur a utilisé le mot-clé _@médecin_ et a changé brusquement le contexte, le bot peut répondre par une question ultérieure (ou une série de questions ultérieures, selon le cas).

Selon la manière dont le bot a été formé, la question de suivi peut être : « Est-ce une question urgente ? », ou elle pourrait être : « Est-il nécessaire que vous voyiez votre médecin ? Un autre médecin dans le cabinet serait-il acceptable, au cas où votre médecin serait absent ? » Ou, si le bot est simpliste, il peut simplement aller de l'avant et planifier le rendez-vous pour le premier créneau disponible, sans faire de consultation supplémentaire avec l'utilisateur.

#### Protocole de phrase structurée

Une conversation humaine typique consiste très rarement en des échanges brefs et monosyllabiques. La plupart du temps, nous conversons en échangeant divers idiomes et phrases qui servent de blocs de construction pour des phrases plus élaborées.

Afin de rendre l'expérience de discussion avec le bot intuitive et naturelle, nous devons permettre à nos bots de traiter des phrases courtes, et même des phrases courtes. Similaires aux commandes et aux mots-clés, ces phrases et phrases structurées doivent être prédéfinies et conçues par les créateurs de bots.

Parce que les idiomes et les phrases impliquent un ton plus décontracté de la conversation, le résultat de l'analyse d'une phrase structurée sera, par nécessité, moins déterministe que le résultat d'une commande ou d'un mot-clé unique. Si vous vous souvenez de la manière dont les entreprises froncent les sourcils face à l'imprévisibilité et aux résultats non déterministes, vous comprendrez plus facilement pourquoi nous préférons reléguer le traitement moins critique aux phrases structurées. Il va sans dire que moins un message envoyé au bot est structuré et formalisé, moins le bot sera capable de traiter le message de manière prévisible et déterministe.

Ici, nous tirons une ligne fine entre l'ouverture de nos services à un mode de communication plus décontracté et la qualité de service minimale garantie en termes de précision, d'exactitude, de justesse, de cohérence, de cohérence et de répétabilité. Reconnaissant l'importance du mode de communication décontracté, nous sommes néanmoins réticents lorsqu'il s'agit de déléguer un traitement critique à ces messages moins formalisés.

Une autre chose qui rend le traitement des phrases structurées important est la nécessité d'établir un rythme affirmé lors du traitement des demandes des utilisateurs. Si nous insistions pour rester uniquement dans les limites des commandes et mots-clés hautement formalisés, nous aboutirions en effet à des fils de conversation guindés. Les utilisateurs ne se sentiront pas obligés de revenir discuter avec les bots si la conversation semble si rigide et froide ; nous devons établir un flux et un rythme définitif qui maintiendront les utilisateurs engagés et finalement satisfaits de la qualité du service.

C'est pourquoi il est d'une importance primordiale de permettre à nos bots de traiter un certain nombre de phrases courantes que les gens ont tendance à utiliser dans le langage quotidien. Des phrases telles que « Que savez-vous sur... » ou « Pouvez-vous me parler de... » etc. sont des choses que nous utilisons tous tout au long de nos activités quotidiennes. Il est tout à fait normal et naturel d'envoyer des messages commençant par de telles phrases structurées. Les bots reconnaîtront alors que le message qu'ils ont reçu est formulé comme une demande d'information et traiteront cette demande en puisant profondément dans les ressources back-end.

Il est également naturel qu'une phrase moins officielle, comme « que savez-vous sur... », établisse un ton où la réponse n'a pas besoin d'être correcte à 100 %. L'intention générale de la conversation est beaucoup plus lâche que celle contenant une commande ou un mot-clé.

#### Protocole libre (informel)

Enfin, nous devons nous attendre à ce que les utilisateurs envoient des messages qui ne se conforment à aucun des trois protocoles ci-dessus. Il y aura de nombreux messages qui ne contiendront pas de commandes, de mots-clés, ni de phrases prédéfinies et structurées. C'est à nous, créateurs de bots, de décider comment traiter de tels messages non structurés.

Une façon de gérer de tels scénarios flous et non structurés est d'être honnête et de toujours répondre poliment par « Je ne sais pas », ou « Je ne suis pas sûr de comprendre ». C'est une échappatoire, c'est sûr, mais au moins c'est honnête à 100 %.

Cependant, si les bots répondent toujours à tous les messages non structurés par un « Je ne sais pas » brutal, ils perdront rapidement tout charisme et attractivité pour les utilisateurs. Il est donc beaucoup plus souhaitable de faire des tentatives pour rencontrer l'utilisateur à mi-chemin et d'essayer au moins de répondre à certains des messages non structurés.

Nous entrons maintenant dans un territoire parfois appelé « bavardage » ou « badinage ». Le badinage et le bavardage se produisent souvent dans la vie quotidienne, même dans certaines des situations les plus formalisées. Tant que nous formons nos bots à envoyer un signal clair aux utilisateurs que leurs réponses de bavardage aux messages non structurés sont également des messages légers et informels renvoyés aux utilisateurs, le risque d'être mal compris est minimisé.

C'est là que l'humour joue un rôle utile. Si la dose d'humour est appropriée, discuter avec des bots peut être assez amusant et divertissant. De plus, ajouter un peu de trivialités pourrait grandement contribuer à briser la glace et à maintenir le rythme toujours important de la conversation.

#### Éviter le terrier du lapin

Lorsque les bots sont engagés dans des discussions informelles avec les utilisateurs, il y a toujours un danger clair et présent que la concentration et l'élan puissent s'évanouir à tout moment. Atteindre une impasse dans la conversation n'est jamais souhaitable, nous devons donc prendre des mesures préventives pour éviter de descendre dans le terrier du lapin proverbial.

Les bots doivent être conçus pour suivre le bavardage informel avec l'utilisateur et détecter lorsque le bavardage atteint le point de non-retour tant redouté. Selon le contexte (et également le profil particulier de l'utilisateur), ce point de non-retour variera largement. En général, toute session de conversation qui se termine par beaucoup de messages informels, semi-plaisants et de bavardage général risque de devenir sans signification. Une fois que l'utilisateur prend conscience que son chat avec le bot n'est pas seulement sans signification mais aussi une perte de temps, l'utilisateur développera une tendance à éviter les interactions futures.

Ce qui peut être utile du point de vue du plan de conception du bot est de travailler sur l'allocation du « budget de bavardage » par fil de conversation. Ce « budget de bavardage » devrait être exprimable en nombre de messages informels consécutifs échangés entre l'utilisateur et le bot. Le « budget de bavardage » devrait également être configurable, afin que le bot puisse être calibré en temps réel, comme la situation l'exige.

Lorsque le fil de conversation donné épuise son « budget de bavardage », le bot doit briser la vitre proverbial et appuyer sur le bouton de panique proverbial. Cet événement qui déclenche le fil ne doit pas être visible pour l'utilisateur. Tout ce que fait le bot en appuyant sur le bouton de panique est d'émettre un message qui tentera de ramener la conversation sur un chemin plus structuré. Il existe de nombreuses façons possibles d'y parvenir, par exemple, une façon serait que le bot intervienne et rappelle poliment à l'utilisateur certains des services plus structurés disponibles pour eux. Le bot pourrait également à ce moment-là offrir un rappel sur les commandes disponibles, les mots-clés disponibles, ou même les phrases structurées courantes. C'est en fait un modèle comportemental très utile, car dans la plupart des cas, les utilisateurs ont certainement oublié ces détails ennuyeux.

Des phrases utiles telles que « Hé, saviez-vous que vous pouvez me demander de vous notifier de toute offre sur tel ou tel produit ? » pourraient être utilisées pour sortir la conversation des doldrums créés par l'envoi d'une blague trop lame.

#### Les bots doivent être non intrusifs

Alors que je construisais mes premiers bots et que je les testais dans la nature, j'ai remarqué que la plupart des gens auraient principalement du mal avec la question de la confiance. Une partie de ces problèmes était due au fait que les gens ne comprenaient tout simplement pas que les bots ne sont qu'une extension des services automatisés déjà existants.

À ma grande surprise, certaines personnes m'ont confié qu'elles n'aimaient pas le fait que le bot soit assis là, écoutant toutes leurs activités. Ils n'ont pas compris que les bots n'ont accès qu'aux messages qui leur sont envoyés directement, donc c'était un autre obstacle que j'ai dû surmonter pour les amener à essayer les bots.

Une façon que j'ai trouvée efficace pour apaiser les angoisses des gens concernant les bots est d'offrir un accord de niveau de service (SLA) très clair avec les bots. Dès que l'utilisateur approche un bot, c'est le devoir de ce bot d'expliquer à l'utilisateur que le bot n'aura accès qu'aux messages qui lui sont envoyés directement. De plus, il est utile que le bot explique très clairement qu'il n'enverra jamais de message à l'utilisateur à moins que l'utilisateur ne lui envoie d'abord un message.

#### Adhésion et désadhésion

De manière similaire à la façon dont le marché est réglementé pour nous donner, en tant que consommateurs, le pouvoir d'accepter ou de refuser d'être contactés par les entreprises (que ce soit par le biais du télémarketing ou du spam par e-mail, etc.), les bots doivent également offrir la même capacité. Par défaut, les bots ne sont pas censés nous envoyer de messages. Ils sont là uniquement pour répondre aux messages que nous leur envoyons.

Cependant, il existe de nombreux scénarios où nous, les utilisateurs finaux, bénéficierions d'être contactés par un bot. Mais pour que cela se produise, un bot doit être configuré pour demander explicitement à l'utilisateur la permission de lui envoyer le message de manière inattendue. De plus, il est de l'obligation du bot de permettre aux utilisateurs de définir leurs préférences quant au moment et à la manière dont le message provenant du bot doit être livré.

#### Conclusion

La seule façon pour que les bots soient adoptés par le marché dans son ensemble est d'établir un protocole de communication clair et prévisible. Dans cet article, j'ai soutenu qu'un protocole de bot peut et doit être nuancé, du plus rigide et contraint (commandes) au plus flexible et non contraint (bavardage).

Les raisons de cette contrainte résident dans le besoin pressant d'établir et de maintenir la prévisibilité, la répétabilité et la cohérence. Ces caractéristiques aident les entreprises à faire des projections et à planifier pour l'avenir, d'où le mépris répandu pour les bots qui sont « innovants », « créatifs », pleins de surprises (agréables et désagréables).

Sauf si nous construisons un bot qui offrirait une certaine valeur de divertissement (comme un bot humoriste, par exemple), nous devons nous assurer que notre bot met en œuvre un ensemble très strict de commandes, de mots-clés, de phrases structurées et d'autres fonctionnalités qui peuvent être démontrées de manière fiable aux utilisateurs.

_Intrigué ? Vous voulez en savoir plus sur la révolution des bots ? Lisez des explications plus détaillées ici :_

[L'ère de l'auto-service touche à sa fin](https://medium.freecodecamp.com/the-age-of-self-serve-is-coming-to-an-end-ae632f7151b2#.tjlvovkhc)

[Seul le No Ux est un bon UX](https://medium.com/bots-for-business/https-medium-com-alexbunardzic-only-no-ux-is-good-ux-c24a7cbd12f4#.aqpbs89oj)

[Arrêtez de construire des bots médiocres !](https://medium.com/bots-for-business/stop-building-lame-bots-b093dcd5f28b#.c3k9kcprv)

[Quatre types de bots](https://chatbotsmagazine.com/four-types-of-bots-432501e79a2f#.9tuz1winx)

[Y a-t-il un inconvénient aux interfaces conversationnelles ?](https://chatbotsmagazine.com/is-there-a-downside-to-conversational-interfaces-55bed7220c2f#.l43a0r4j4)

[Les bots ne sont-ils qu'une mode ? Les GUI sont-ils vraiment supérieurs ?](https://medium.com/@alexbunardzic/are-bots-just-a-fad-are-guis-really-superior-a1f52007d2b9#.a7zvp7kx2)

[Briser le quatrième mur dans le logiciel](https://medium.freecodecamp.com/breaking-the-fourth-wall-in-software-d08a25df34b7#.jvkf8g6e2)

[Les bots sont les anti-applications](https://medium.com/bots-for-business/bots-are-the-anti-apps-869639cfa179#.gf5x3rw22)

[Combien de NLP les bots ont-ils besoin ?](https://medium.com/bots-for-business/how-much-nlp-do-bots-need-a9fd55d64094#.9r83gcpve)

[Les écrans sont pour la consommation, pas pour l'interaction](https://medium.com/bots-for-business/screens-are-for-consumption-not-for-interaction-6151fb8db6d7#.4qh22p38n)