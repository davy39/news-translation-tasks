---
title: 'De quoi parler : Google Code-in 2017 avec Zulip !'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-13T21:04:59.000Z'
originalURL: https://freecodecamp.org/news/something-to-chat-about-google-code-in-2017-and-the-power-of-open-source-7efa4c9347ef
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_MRhZG1wYqg9PTFLFcre9w.png
tags:
- name: Google
  slug: google
- name: Life lessons
  slug: life-lessons
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: 'De quoi parler : Google Code-in 2017 avec Zulip !'
seo_desc: 'By Marco Burstein (skunkmb)

  Thoughts from a Winner of Google Code-in 2017


  Source code for a chess-playing Zulip chatbot

  My name is Marco Burstein, and last year I was a winner of Google Code-in 2017 with
  an organization called Zulip. With Google Cod...'
---

Par Marco Burstein (skunkmb)

#### Réflexions d'un gagnant de Google Code-in 2017

![Image](https://cdn-media-1.freecodecamp.org/images/Vk-LQi0CohHnaEZ6mRviSuZc83H8hSyy3aor)
_Code source pour un chatbot Zulip jouant aux échecs_

Je m'appelle Marco Burstein, et l'année dernière, j'ai été l'un des gagnants de Google Code-in 2017 avec une organisation appelée [Zulip](http://zulipchat.com). Avec Google Code-in 2018 [juste au coin de la rue](https://opensource.googleblog.com/2018/08/announcing-google-code-in-2018.html), j'ai pensé que ce serait un bon moment pour partager mon expérience de Google Code-in avec le monde !

### Alors, qu'est-ce que Google Code-in ?

![Image](https://cdn-media-1.freecodecamp.org/images/PORgIG3dTIbd0EoSH526caRZiAS865unuxoC)
_Le logo de Google Code-in_

Google Code-in (ou « GCI » en abrégé) est une compétition où des étudiants du monde entier contribuent à des projets open-source. Les étudiants de GCI accomplissent des tâches pour des organisations open-source (ou « orgs ») du 23 octobre au 12 décembre.

Une fois la compétition terminée, les organisations choisissent chacune six finalistes et deux grands gagnants. Chaque finaliste reçoit un sweat à édition limitée, et les gagnants se voient offrir un voyage tout compris au siège de Google en Californie !

Pour participer à Google Code-in, **vous n'avez pas besoin d'être programmeur** ! Google Code-in inclut plusieurs types de tâches différentes, y compris des tâches de programmation ainsi que de l'assurance qualité, de la sensibilisation, et plus encore.

#### Qu'est-ce que l'open-source ?

![Image](https://cdn-media-1.freecodecamp.org/images/1EL764RETQ6IFLycsrAvbFS0DyQuPylKtP0F)
_Un arbre peut représenter des concepts open-source comme les branches et les pull requests !_

L'épine dorsale de Google Code-in est le logiciel open-source. Essentiellement, un logiciel étant « open-source » signifie que **n'importe qui peut voir et modifier le code du projet**.

Souvent, les organisations utilisent des outils comme GitHub comme plateforme pour leur flux de travail open-source. Les étudiants apprendront à créer des _branches_ pour de nouvelles fonctionnalités, et acquerront de l'expérience en ouvrant des _pull requests_, où ils soumettent leurs branches au dépôt principal de l'organisation.

Tout au long de Google Code-in, les étudiants contribuent à ces organisations open-source de nombreuses manières différentes, comme l'ajout de nouvelles fonctionnalités, la correction de bugs, ou la réalisation de recherches.

#### Qui peut s'inscrire ?

![Image](https://cdn-media-1.freecodecamp.org/images/TMuJeuvN3brg9QRIhQ4exBWsfoApWsTTOAkC)
_Tout étudiant pré-universitaire peut participer à Google Code-in_

Google Code-in est ouvert à tous les étudiants pré-universitaires âgés de 13 à 17 ans. Chaque année, de plus en plus d'étudiants participent, avec 3 555 étudiants l'année dernière.

### Mon expérience avec Google Code-in

#### Choisir Zulip

![Image](https://cdn-media-1.freecodecamp.org/images/Ts8sAjMEzbaFf6ZJ3YWHhCaSwmTq-OzV1Lif)
_Le logo de Zulip_

Je me suis précipité vers mon ordinateur et j'ai tapé mon mot de passe. C'était le moment. Le jour était enfin arrivé : Google Code-in 2017 commençait ! J'attendais depuis des mois que GCI commence ; c'était maintenant ma chance de tester mes compétences en programmation, et peut-être de gagner un voyage au siège de Google en cours de route.

Avant le début de la compétition, j'ai étudié rigoureusement chaque organisation, m'assurant de savoir sur laquelle j'allais me concentrer. J'ai même fait un tableau pour m'aider à décider ! L'organisation que j'ai finie par choisir était [Zulip : « le chat de groupe le plus productif au monde »](https://zulipchat.com/) ; il utilise Python et Django en backend avec JavaScript en frontend. Zulip combine l'immédiateté du chat avec l'efficacité du fil de discussion de style email pour rendre les chats de groupe meilleurs que partout ailleurs. C'est aussi complètement gratuit !

Une fois que j'avais choisi mon organisation, j'étais prêt à commencer à accomplir des tâches.

#### Tâches et leçons en cours de route

![Image](https://cdn-media-1.freecodecamp.org/images/B3yp4GQ0bZ89GxsmnxTCueXO5hwlHB8rEbC3)
_J'ai travaillé sur un chatbot jouant aux échecs pour Zulip._

Tout au long de la compétition, avec le soutien des mentors et de l'équipe de Zulip, j'ai accompli de nombreuses tâches que je n'aurais même pas imaginées l'année précédente. Pendant la compétition, j'ai passé jour après jour à travailler, parfois sans même quitter mon pyjama ! L'une de mes préférées était ma [création d'un chatbot Zulip pour jouer aux échecs avec un utilisateur](https://github.com/zulip/python-zulip-api/pull/205). « Chessbot » supporte non seulement le jeu avec d'autres utilisateurs, mais aussi contre l'ordinateur lui-même via une connexion à un autre projet open source : [le moteur d'échecs Stockfish](https://github.com/official-stockfish/Stockfish). Après avoir écrit plus de 900 lignes de code, j'ai soumis un système de chessbot fonctionnel — bien qu'un peu buggé. Après des jours de retouches lors de sessions de revue de code avec mes mentors, chessbot a été accepté et fusionné.

Une autre tâche favorite était l'ajout d'une fonctionnalité Zulip qui traduirait automatiquement [les émoticônes (comme « :)` ») en emoji (comme « ? »)](https://github.com/zulip/zulip/pull/8081). Après plusieurs améliorations et changements tout au long du processus de revue avec mes mentors, ma fonctionnalité a été ajoutée en tant qu'option dans les paramètres de Zulip. C'était extrêmement satisfaisant d'ouvrir Zulip et de voir une option que j'avais aidé à créer !

Ces tâches m'ont montré **à quel point il peut être gratifiant de se challenger** ; de nombreuses tâches m'ont pris des jours à compléter, mais à la fin, j'ai ressenti une immense satisfaction et joie pour ce que j'avais accompli. De plus, ces tâches m'ont montré l'importance de la collaboration pendant le processus de programmation. Travailler sur des projets open-source m'a montré que **être aidé par les autres améliore considérablement la qualité de votre code**. Avant Google Code-in, je n'avais jamais fait de revue de code, mais à travers la création de chessbot, la fonctionnalité de traduction d'émoticônes, et plus encore, j'ai vu l'importance d'être aidé par les autres pour attraper les bugs et trouver des solutions.

En ayant des mentors, j'ai pu apprendre à écrire du code qui s'intègre dans un écosystème plus large, et travailler avec Zulip m'a montré la puissance de l'open source, à la fois pour créer des logiciels et pour rassembler les gens.

### Le voyage

![Image](https://cdn-media-1.freecodecamp.org/images/bRNc1FQTMmcbKvrepcXgCMD9FSSLbeGyJ9IK)
_Étudiants, mentors et parents chez Google !_

Le voyage du grand prix pour Google Code-in est un fantastique voyage à San Francisco, incluant une journée au Googleplex à Mountain View. J'ai passé un moment exceptionnel lors de ce voyage, et c'était honnêtement un rêve devenu réalité de pouvoir visiter le siège de Google. Je me suis senti extrêmement chanceux et excité de pouvoir voir le fonctionnement interne de l'entreprise technologique qui m'inspire tant.

![Image](https://cdn-media-1.freecodecamp.org/images/Pkt3wcXx23-vcx5ON9hQ5dEb9xVDpkDFiujS)
_Moi et l'un de mes mentors, Rohitt_

Alors qu'à San Francisco, j'ai pu rencontrer l'un de mes mentors Zulip [Rohitt](http://github.com/aero31aero) en personne après avoir passé des mois à communiquer avec lui sur Internet. Rohitt a été extrêmement accueillant et serviable envers moi pendant le processus GCI, et ce fut merveilleux d'avoir l'occasion de rencontrer quelqu'un qui a eu un impact si positif sur moi.

![Image](https://cdn-media-1.freecodecamp.org/images/YksywVgog78RiR4d5n6fYEFR9VeJBiu1vZUl)
_D'où viennent les autres gagnants_

Rencontrer les autres gagnants et mentors du monde entier était également fantastique. **Même si nous vivons dans des pays différents et parlons des langues différentes, nous avons tous été réunis par notre passion commune pour la technologie open-source.**

### Quelques conseils

![Image](https://cdn-media-1.freecodecamp.org/images/HBadIeExDbvvXSJnnguGw5SIvsvPLdjK6V5A)

Pour aider les nouveaux venus qui découvrent Google Code-in grâce à cet article, j'ai pensé inclure quelques conseils et astuces pour participer à GCI. Pour commencer, je recommande de se familiariser avec quelques outils importants utilisés par de nombreuses organisations open-source :

1. [**GitHub**](https://goo.gl/nqMPX9), où presque tout le code open source est hébergé en ligne. Il est essentiel de comprendre comment utiliser GitHub afin de soumettre du travail et obtenir des retours.
2. IRC, abréviation de **Internet Relay Chat**, qui est la manière dont de nombreuses organisations open source communiquent. Il existe plusieurs clients IRC différents, qui permettent de discuter avec toute autre personne utilisant le service. Vous pouvez consulter [ce guide réalisé par Google](https://goo.gl/amCmgZ) sur la façon de l'utiliser.

Pendant la compétition, je pense qu'il y a quelques points importants à garder à l'esprit pour être aussi performant que possible.

#### Rester fidèle à une organisation.

Faire des tâches pour une seule organisation exclusivement permet d'être beaucoup plus efficace, car vous utiliserez toujours le même écosystème de développement. Avec le temps, vous deviendrez de plus en plus à l'aise avec la structure du code source de votre organisation, ce qui augmentera votre productivité.

#### Être actif dans la communauté.

Les organisations aiment les étudiants qui sont dévoués et engagés. En étant actif dans la communauté, vous montrez votre engagement et votre intérêt pour l'organisation. Une façon d'être actif est de répondre aux questions des autres dans le chat IRC. Vous pourriez également laisser des commentaires ou des retours sur d'autres pull requests, ou faire du travail pour l'organisation en dehors des simples tâches GCI.

#### Faire des tâches difficiles.

Faire des tâches difficiles montre à votre organisation que vous êtes prêt à vous challenger en travaillant sur des choses en dehors de votre zone de confort. Les tâches difficiles sont également meilleures pour démontrer vos compétences, que ce soit en programmation, en design graphique, ou dans un autre domaine.

Cependant, notez que les règles de GCI stipulent que...

> Si vous essayez d'être finaliste ou de gagner un grand prix, vous devez être dans le **top vingt des participants ayant accompli le plus de tâches pour une organisation**.

Étant donné qu'une tâche difficile prend généralement plus de temps qu'une tâche facile, il est important d'avoir un équilibre entre les deux types afin de vous assurer d'être dans le top vingt pour votre organisation avant la fin de la compétition.

De plus, faire des tâches difficiles est plus bénéfique d'un point de vue apprentissage. Résoudre des problèmes plus difficiles vous aidera à vous améliorer en programmation, en design, ou dans toute autre compétence.

#### Être poli.

Soyez toujours poli et reconnaissant envers tous vos mentors **ainsi qu'envers vos camarades compétiteurs**. Les mentors consacrent leur temps et leur énergie à aider les étudiants à apprendre, il est donc important de montrer de la gratitude pour tout ce qu'ils font !

#### S'amuser !

Enfin, mais pas des moindres, amusez-vous ! Participer à Google Code-in est une expérience fantastique et une excellente façon d'apprendre de nouvelles choses. Il est important de faire un pas en arrière et de ne pas se concentrer uniquement sur la victoire pour **profiter de la compétition** !

Si vous n'êtes pas choisi comme gagnant, vous ne devriez pas être déçu ; au contraire, soyez heureux d'avoir pu participer et apprenez de vos erreurs. Vous pourrez participer à nouveau l'année prochaine !

_(Si vous voulez en savoir plus sur mes conseils, j'ai écrit un [article séparé](https://medium.com/@skunkmb/5-tips-to-win-google-code-in-f8e0d29499eb) qui approfondit mes conseils.)_

### Conclusion

![Image](https://cdn-media-1.freecodecamp.org/images/fNTqw9mJ8-inE4QzC0aJkmKwUnuOYsQKsi86)

En conclusion, je veux dire merci. Merci beaucoup à Zulip pour m'avoir mentoré et pour avoir été une communauté aussi incroyable à laquelle appartenir. J'apprécie vraiment tout le temps et les efforts que mes mentors ont consacrés à la révision de mes tâches et à m'aider à m'améliorer. J'ai hâte de continuer à contribuer à Zulip à l'avenir ! De plus, je veux remercier Google et l'équipe Google Open Source pour avoir organisé Google Code-in et pour nous avoir accueillis à San Francisco pour une semaine fabuleuse d'activités. Je me sens si reconnaissant d'avoir eu une opportunité aussi incroyable, que je me souviendrai sûrement pour le reste de ma vie.

Google Code-in m'a ouvert les yeux sur les logiciels open-source et m'a inspiré à être plus actif dans cette communauté. Je suis si heureux d'avoir pu contribuer à l'open-source grâce à cette compétition, et je sais que ce n'est que le début de mes aventures open-source.