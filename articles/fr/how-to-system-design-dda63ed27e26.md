---
title: 'Réussir l''entretien sur la conception de systèmes : conseils d''un ingénieur
  logiciel de Twitter'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-19T19:40:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-system-design-dda63ed27e26
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BP4Kem7C3Sxd7xWWXkbypA.png
tags:
- name: Computer Science
  slug: computer-science
- name: education
  slug: education
- name: interview
  slug: interview
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: 'Réussir l''entretien sur la conception de systèmes : conseils d''un ingénieur
  logiciel de Twitter'
seo_desc: 'By Zhia Hwa Chong

  I recently wrote about how I landed offers from multiple top-tier tech companies.
  During my interview preparation process, I read up on a lot of material and prepared
  a set of notes on how to tackle system design problems. In this a...'
---

Par Zhia Hwa Chong

J'ai récemment écrit sur [comment j'ai obtenu des offres de plusieurs grandes entreprises technologiques](https://medium.freecodecamp.org/how-i-landed-offers-from-microsoft-amazon-and-twitter-without-an-ivy-league-degree-d62cfe286eb8). Pendant ma préparation aux entretiens, j'ai lu beaucoup de matériel et préparé un ensemble de notes sur la façon d'aborder les problèmes de conception de systèmes. Dans cet article, je souhaite partager ces conseils avec vous tous.

Si vous êtes un jeune diplômé sans expérience dans les systèmes distribués à grande échelle, ou même un ingénieur expérimenté avec des années d'expérience, cet article vous sera utile.

**Mise à jour (24/03/2019)** : Si vous souhaitez rejoindre un groupe d'étudiants pour en apprendre davantage sur la conception de systèmes, j'organise une petite classe ! Vous pouvez vous rendre sur ce [lien](http://bit.ly/interviewcourses) pour en savoir plus, ou visiter mon site web : [zhiachong.com](http://www.zhiachong.com) pour plus d'informations.

![Image](https://cdn-media-1.freecodecamp.org/images/SM68D2mI9L-wqSbYcQdRA6Ho5GmhEICbcpmD)
_Comment concevoir un système : Conseils d'un ingénieur logiciel de Twitter_

Cet article est divisé en quatre sections :

* Poser des questions de clarification
* Utiliser votre expérience
* Aborder un problème de manière systématique
* Tenir vos propres notes

### Poser des questions de clarification

Un objectif central d'un entretien sur la conception de systèmes est de **donner au candidat l'opportunité de démontrer ses connaissances.**

Il n'y a pas de réponses strictement bonnes ou mauvaises. Une bonne question de conception de système semble généralement très ambiguë, et la raison en est qu'elle est censée vous donner une chance de démontrer les éléments suivants :

* Comment vous pensez à l'espace problématique
* Comment vous pensez aux goulots d'étranglement
* Ce que vous pouvez faire pour éliminer ces goulots d'étranglement.

![Image](https://cdn-media-1.freecodecamp.org/images/LEWXpmsTQuJkgv8FjX8L5cOWo-KX0iN4SSjE)
_Comment concevoir cette boîte noire_

Imaginez que l'on vous demande de concevoir une boîte noire. Comment aborderiez-vous le problème ? Il n'y a pas de directives claires sur ce que vous devez construire ici, à part le fait que la boîte doit pouvoir contenir certains éléments.

L'une des stratégies les plus utiles que j'emploie personnellement est **de poser des questions de clarification**. Quelles sont les "bonnes" questions de clarification, demandez-vous ?

Une bonne question de clarification vous aide à atteindre un ou plusieurs des objectifs suivants :

1. Vous aide à réduire la portée de ce que vous devez faire
2. Vous aide à clarifier les attentes de l'utilisateur vis-à-vis du système
3. Vous donne une direction sur la manière de procéder
4. Vous informe des goulots d'étranglement/zonnes problématiques possibles

Dans l'exemple de la boîte noire, vous pourriez demander : "Eh bien, que contient la boîte ? Combien d'objets contient-elle ? Et qui est l'utilisateur prévu ?"

À cela, je pourrais répondre : construisons une boîte jaune avec un smiley dessus qui doit contenir au plus une balle de tennis. Ce n'est pas une balle de tennis ordinaire, cependant. Elle aura au moins 0,5 m de rayon et pèsera environ 1 kg. Elle est destinée à être enlacée, pas tenue, donc je ne veux pas de poignée dessus.

Voilà, c'est la boîte.

![Image](https://cdn-media-1.freecodecamp.org/images/UHd2UsV8aRy4tIppyukpJjVfqBz8PlEOKvjG)
_Ma boîte idéale avec un smiley_

**Posez toujours des questions de clarification.** Vous n'êtes pas jugé sur le fait d'avoir posé ou non une question spécifique pendant l'entretien, mais vous êtes jugé sur la manière dont vous pensez à l'espace problématique.

Par exemple, si je vous demandais de concevoir Twitter maintenant, comment feriez-vous ? Prenez quelques minutes pour y réfléchir, et peut-être même esquissez-le sur une feuille de papier. Allez aussi profondément et largement que possible, puis revenez à cet article. Mieux encore, vous pouvez **laisser vos notes dans les commentaires ci-dessous** et nous pourrons en discuter davantage.

Si vous ne l'avez pas encore réalisé, le résultat final de l'exercice ci-dessus donnerait des résultats significativement différents. Pour mon propre parcours, je pourrais approfondir la conception d'API et l'infrastructure backend. J'explorerais probablement aussi les problèmes spécifiques à l'iPhone, en raison de mon expérience. Je parlerais de la manière dont le client interagit avec les points de terminaison de la couche intermédiaire, de la manière dont la journalisation fonctionnerait, de la manière dont je concevrais le backend pour assurer un temps de fonctionnement, et ainsi de suite.

Ce sont des discussions très intéressantes que vous pouvez avoir avec un collègue, et c'est un signal très fort qu'un interviewer recherche.

### Utilisez votre expérience à votre avantage

Souvent, je vois des ingénieurs essayer de deviner ce que l'interviewer essaie de demander, puis adapter leurs réponses pour correspondre aux attentes.

Je décourage fortement quiconque de faire cela pour plusieurs raisons :

1. Chacun a un parcours unique. Dans un entretien sur la conception de systèmes, c'est une opportunité pour vous de démontrer quelles sont vos forces. Ne gaspillez pas cette opportunité en essayant de deviner ce que quelqu'un d'autre pourrait attendre de vous.
2. L'interviewer pourrait avoir hoché la tête en écoutant vos réponses, mais il aurait pu savoir que vous bluffez et ne réfléchissez pas réellement au problème.

Votre expérience et votre parcours peuvent varier largement par rapport au prochain candidat. Vous apportez un ensemble de valeurs et d'expertise à la table que personne d'autre ne peut apporter. **C'est ce qui fait de vous une personne précieuse et irremplaçable.** Peu importe le domaine dans lequel vous vous trouvez, les gens se soucient de ce que **vous** pouvez apporter.

### Aborder le problème de manière systématique

Maintenant, avec mon expertise en tête, il y a plusieurs choses auxquelles je pense lorsque je m'attaque à un nouveau système. Je vous recommande vivement de formuler un ensemble de critères ou d'étapes pour vous-même également.

Certaines des choses qui me viennent à l'esprit lorsque je travaille sur un nouveau système sont :

* Quel est l'objectif du système ?
* Qui sont les utilisateurs du système ?
* Quelle est l'échelle avec laquelle nous travaillons ?
* Est-ce un nouveau/ancien système ? Comment gérons-nous la versioning ?

Parmi d'autres...

Voyez-vous, mon ensemble de critères sera différent de celui d'un ingénieur front-end. J'utilise ces critères pour formuler une image dans ma tête, et ceux-ci guideront mon processus de prise de décision.

Armé de réponses à ces questions, je peux commencer à aborder le problème en question et le décomposer systématiquement en composants individuels.

Un bon exercice que j'aime faire est **comment concevoir un système de commande de café**. J'y ai pensé alors que j'étais assis chez Starbucks un jour, et j'ai réalisé qu'il serait bien si je pouvais commander un smoothie sur mon téléphone et le récupérer dans mon Starbucks local.

Mon esprit a commencé à aller dans diverses directions :

* Que fait cette machine à commander du café ?
* Si j'en construis une, puis-je la vendre à Starbucks, ou dois-je la vendre en marque blanche en tant que service ?
* Combien d'utilisateurs dois-je supporter si je la vends à Starbucks ?
* Alternativement, si je la vends en marque blanche, puis-je vendre l'interface à mon service de commande de café, puis aider les clients à construire un backend afin qu'ils puissent stocker les commandes sur leurs machines locales ?

![Image](https://cdn-media-1.freecodecamp.org/images/e-kBkdnLuGBAp4N3Saj9n-DRjxqtRdFOfo2a)
_Comment aborder ce problème_

Une fois que j'ai des réponses à ces questions, je peux enfin me faire une image complète de ce que fait mon service de commande de café. Voici à quoi ressemblerait **ma version** du service de commande de café :

Mon service de commande de café est un logiciel en tant que service ([SAAS](https://en.wikipedia.org/wiki/Software_as_a_service)). Il offre une interface pour que divers partenaires puissent s'y connecter.

* Il dispose d'une API, appelée _addCoffeeForMerchant_, qui insère le nom du café, le prix du café et les ingrédients du café.
* Il dispose d'une API GET, appelée _getCoffeesForMerchant_, qui retourne une liste de cafés pour un identifiant de marchand donné.
* L'identifiant de marchand est un identifiant unique (UUID) qui est généré en utilisant un mécanisme de hachage, ce qui peut être clarifié davantage avec le client.
* Le logiciel est optimisé pour les opérations en lecture seule, car la plupart de mes clients créent leur menu une fois et le lisent plusieurs fois au cours de la journée.
* Il dispose d'un mécanisme de mise en cache qui utilise la stratégie d'éviction [Least-Recently-Used (LRU)](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)), car si l'article du menu n'a pas été commandé depuis un certain temps, mon client ne se soucie pas s'il est légèrement plus lent à apparaître sur le menu.
* Au cas où l'un des magasins de données s'auto-détruirait, mon service de commande de café répliquera les données dans différents clusters sur la côte ouest et la côte est des États-Unis, car je cible uniquement le marché américain pour l'instant.

Alternativement, tout autre service de commande de café auquel vous pouvez penser serait également très probable. Il s'agit simplement de ce que vous optimisez. Je pense que ce sont des problèmes très intéressants, et c'est un excellent exercice mental pour garder l'esprit engagé.

### Tenir vos propres notes

En tant qu'ingénieur logiciel, c'est un processus sans fin d'apprentissage. Je vous recommande vivement d'utiliser soit Evernote, soit un [Moleskin](https://amzn.to/2IuEiPw) pour prendre des notes. Je porte personnellement un petit carnet pour les idées rapides que je dois noter, et je garde diverses autres choses sur Evernote chaque fois que je le peux.

J'ai un carnet nommé "Programmation" dans mon Evernote. Chaque fois que je tombe sur quelque chose de nouveau, ou d'intéressant, je le note dans mon carnet pour référence future.

Je passe en revue et attribue des étiquettes à ces nouvelles notes sur une base mensuelle ou trimestrielle pour m'assurer que les notes sont organisées. Par exemple, j'ai une étiquette "Conception" pour tout ce qui a trait à la conception de systèmes. Il pourrait s'agir de quelque chose comme un lien vers une vidéo YouTube que j'ai trouvée intéressante, ou un argument intéressant qu'un collègue a avancé et auquel je n'avais pas pensé.

Voici un exemple de ce à quoi ressemble l'une de mes notes :

![Image](https://cdn-media-1.freecodecamp.org/images/6i-NhLaPztQuLHNblUqbFPFr24qL-TKZYaYm)
_Désolé pour la mauvaise grammaire et les fautes de frappe :p_

L'une des choses que j'ai apprises récemment d'un collègue est que NoSQL est idéal pour le prototypage, car il n'est pas nécessaire de discuter des schémas avec d'autres équipes. Si je voulais changer le schéma, je peux le faire très rapidement avec une base de données NoSQL. C'était un apprentissage clé du travail que j'ai inséré dans mon carnet "Programmation".

Je divise mes notes en :

1. Conceptions de systèmes
2. Entretiens (expérience + revue des différents entretiens que j'ai eus dans le passé, regroupés par nom d'entreprise)
3. Petits conseils aléatoires, bon à savoir en informatique, comme des scripts bash utiles ou des astuces de ligne de commande
4. Lectures / vidéos YouTube

Toutes les notes ci-dessus vont sous "Programmation". Avec le temps, je trouve que j'ai une collection pseudo-organisée de choses que j'ai lues ou explorées dans le passé.

Comme quiconque me connaît sur un plan personnel, je ne suis pas une personne très organisée. Ainsi, je n'ai collecté que peut-être 10 - 15 % des choses, donc il reste beaucoup plus à faire.

Les connaissances et la pratique vont de pair pour s'améliorer dans la conception de systèmes. Si vous pensez que votre travail actuel ne vous offre pas l'opportunité de faire de la conception de systèmes, alors vous devriez soit en trouver un qui le fait, soit essayer de concevoir une petite partie d'une architecture existante de manière à ce qu'elle soit plus rapide, moins chère, plus robuste ou plus facile à modifier à l'avenir.

### Ressources que je recommande

[Intro à : Architecture et Conceptions de Systèmes](https://www.youtube.com/watch?v=ZgdS0EUmn70) - Excellent tutoriel YouTube d'un ancien ingénieur de Facebook sur la façon d'aborder les problèmes de conception de systèmes.

[Concevoir des applications intensives en données](https://amzn.to/2H1ULel) - Une autre bonne ressource pour apprendre à concevoir pour l'échelle. Il parle de diverses choses qu'un ingénieur logiciel typique prend pour acquises - comment fonctionnent les bases de données (mySQL et noSQL), quand utiliser chacune, les avantages et inconvénients de diverses techniques pour gérer l'échelle, etc. Je le recommande vivement ?

Entretiens simulés - Un environnement simulé qui imite l'entretien réel est extrêmement utile pour se préparer aux entretiens. Si vous pouvez trouver un ami pour le faire pour vous, alors je le recommande vivement. Je fais également des entretiens simulés, donc si vous êtes intéressé, n'hésitez pas à me contacter sur [zhiachong.com](http://www.zhiachong.com) !

[Ce que tout ingénieur logiciel devrait savoir sur l'abstraction unificatrice des données en temps réel](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying) - Une discussion très longue et technique sur les logs, les compromis. Je ne l'ai pas encore terminée, mais elle est fortement recommandée par un collègue.

[Evernote](https://www.evernote.com/referral/Registration.action?sig=3dbd8660e92a8ca68faeb24c552fd32a492c1e620fe4c77e45844685fed05492&uid=18085328) - La meilleure ? application de prise de notes que j'ai utilisée. Il existe de nombreux tutoriels sur la manière de tirer le meilleur parti d'Evernote. Je ne les ai pas encore suivis, simplement parce que je l'utilise comme un simple carnet. J'y enregistre tout ce que j'apprends, puis je les réorganise occasionnellement.

[Carnet Moleskin](https://amzn.to/2IuEiPw) - J'apprécie vraiment celui-ci. La qualité est extrêmement élevée. Le prix est légèrement plus élevé, mais comme je l'utilise quotidiennement, je le considère comme un bon investissement. Tenir un beau carnet dans mes mains tous les jours me donne plus envie d'écrire plus de notes.

[Pilot G2 (Noir)](https://amzn.to/2Gwb9qj) - De loin les meilleurs stylos que j'aie jamais utilisés, et les seuls que j'utiliserai. Je les achète en gros sur Amazon et les garde partout où je vais. J'en ai un dans mon sac à dos, un au bureau et un dans mon bureau à la maison pour toujours avoir un stylo à portée de main. Il écrit bien, l'encre coule doucement, et j'adore simplement la sensation d'écrire avec. Couplé avec le Moleskin, parfois je veux simplement prendre le G2 pour noter des choses aléatoires dessus parce que ces deux-là sont si parfaits ensemble.

[Comprendre l'entretien sur la conception de systèmes](https://www.educative.io/collection/5668639101419520/5649050225344512) — Celui-ci est recommandé par des amis. C'est un cours en ligne qui enseigne comment concevoir un système distribué en détail. C'est un cours de 79 $, cependant. Il y a un tarif pour les équipes. Si cela intéresse quelqu'un, je vérifierai avec eux pour voir s'il est possible de former un groupe pour une remise de groupe.

_Suivez-moi sur [Twitter](https://twitter.com/zhiachong), [Facebook](https://www.facebook.com/zhiachong.tech) et [LinkedIn](https://www.linkedin.com/in/zhiachong/). Inscrivez-vous à [ma liste de diffusion](http://eepurl.com/dnt9Sf) où j'envoie régulièrement des conseils, des astuces et des apprentissages du secteur._

_Si vous avez aimé cet article, commentez ci-dessous : **quel est votre conseil pour construire un système scalable et fiable ?**_