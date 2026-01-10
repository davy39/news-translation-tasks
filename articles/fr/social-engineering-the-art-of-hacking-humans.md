---
title: Ingénierie sociale — L'art de pirater les humains
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2020-09-28T19:16:11.000Z'
originalURL: https://freecodecamp.org/news/social-engineering-the-art-of-hacking-humans
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/wall-2.jpeg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
- name: social engineering
  slug: social-engineering
seo_title: Ingénierie sociale — L'art de pirater les humains
seo_desc: 'Social engineering is the act of manipulating someone into divulging information
  or doing something that''s not usually in their best interest. In this article,
  we will look at a few common ways Social Engineers try to manipulate you.


  Disclaimer: My ...'
---

L'ingénierie sociale est l'acte de manipuler quelqu'un pour qu'il divulgue des informations ou fasse quelque chose qui n'est généralement pas dans son meilleur intérêt. Dans cet article, nous examinerons quelques méthodes courantes utilisées par les ingénieurs sociaux pour vous manipuler.

> _Avis de non-responsabilité : Mes articles sont purement éducatifs. Si vous les lisez et causez des dommages à quelqu'un, c'est de votre responsabilité. Je n'encourage aucune activité malveillante ou pratique de type "black hat". [Lisez le code de déontologie ici](https://www.sans.org/security-resources/ethics)._

Un type courant d'escroquerie est le [Prisonnier espagnol](https://en.wikipedia.org/wiki/Spanish_Prisoner), qui remonte au 18ème siècle et a de nombreuses incarnations modernes.

Il implique généralement quelqu'un qui est dans l'embarras et a besoin de votre aide pour accéder à sa fortune. Vous devez simplement transférer quelques milliers de dollars, puis ils vous rembourseront dix fois plus. Mais vous pouvez deviner comment cela se termine.

Il existe des escroqueries similaires qui circulent sur Internet : l'escroquerie de l'IRS, les escroqueries à la loterie, et ainsi de suite. Celles-ci sont largement classées comme [escroqueries par avance de frais](https://en.wikipedia.org/wiki/Advance-fee_scam). Vous avez quelque chose qui vous attend, mais vous devez payer une avance pour le recevoir.

Pour la personne moyenne, cela peut sembler être des tentatives d'escroquerie mal exécutées. Mais ces escroqueries ont causé la perte de milliers de personnes de leur argent durement gagné. Dans certains cas, [leurs économies de toute une vie](https://www.youtube.com/watch?v=_1sRz6CHPFs&ab_channel=NEWSCENTERMaine).

Ce sont tous des exemples d'ingénierie sociale en action.

L'idée derrière l'ingénierie sociale est de tirer parti des tendances naturelles et des réactions émotionnelles d'une victime potentielle. La peur et l'avidité sont les émotions les plus vulnérables dont les ingénieurs sociaux tirent généralement parti.

Ci-dessous se trouve un excellent exemple d'une attaque réelle d'ingénierie sociale.

%[https://youtu.be/fHhNWAKw0bY]

## Types d'attaques d'ingénierie sociale

L'ingénierie sociale peut être largement classée en cinq types d'attaques basées sur le type d'approche utilisée pour manipuler une cible. Passons en revue chacune d'entre elles.

### Spamming (Email, Text, Whatsapp)

Le spamming implique l'envoi de messages à de grands groupes de personnes dont les informations de contact sont généralement obtenues par des méthodes néfastes. Le spamming est un terme général utilisé pour définir à la fois la diffusion de messages malveillants et non malveillants.

Le spamming non malveillant est utilisé par les annonceurs qui tentent de promouvoir leurs produits à des inconnus en leur envoyant des emails en masse. Leur motif n'est pas de causer des dommages, mais d'essayer de faire acheter leurs produits ou de promouvoir leurs services.

Le spamming malveillant inclut des messages qui tentent d'attirer les utilisateurs vers le site web de l'attaquant pour divulguer des informations personnelles. Ces informations sont ensuite utilisées pour élaborer des attaques de phishing/vishing ciblées contre la victime potentielle.

### Phishing (et Vishing)

Lorsque l'attaquant utilise des messages texte, des emails ou des appels vocaux (phishing vocal = vishing), cela s'appelle le Phishing.

Le phishing est utilisé pour faire croire à la cible qu'elle est contactée par une institution ou une entité légitime afin d'extraire des informations précieuses de la cible.

Si quelqu'un appelle votre entreprise en prétendant être votre fournisseur d'imprimantes, il pourrait être en mesure d'obtenir des informations spécifiques sur l'imprimante — le modèle, l'adresse IP (si connectée à Internet), et ainsi de suite.

Et une fois ces informations données, l'imprimante pourrait être attaquée afin d'obtenir un accès à votre réseau interne.

Les attaques de phishing par email sont également courantes. Un attaquant peut envoyer un email à quelqu'un dans votre entreprise en prétendant être Facebook. Une fois qu'un membre de l'équipe clique sur un lien, il se retrouvera sur une page qui ressemble à Facebook, lui demandant ses informations de connexion. Ces informations de connexion seront envoyées au serveur de l'attaquant après quoi il aura un accès complet au compte Facebook de la victime.

La principale différence entre le Phishing et l'Escroquerie est que les attaques de phishing sont très ciblées. L'attaquant sait qui il veut attaquer et quel type d'informations il recherche.

### Appâtage

L'appâtage implique la conception d'un piège et l'attente que la victime potentielle tombe dans le piège. Par exemple, si un attaquant dépose quelques clés USB dans le parking de votre entreprise, il y a des chances qu'un de vos employés essaie de la brancher sur son ordinateur pour vérifier le contenu de la clé USB.

Cela peut sembler stupide, mais il y a eu de nombreux cas où des astuces simples d'ingénieurs sociaux ont entraîné d'énormes violations de données corporatives. Il est généralement facile d'appâter les gens avec des escroqueries telles que les escroqueries par avance de frais qui circulent encore sur Internet, se nourrissant de personnes crédules.

Un autre type courant d'appâtage se trouve dans les logiciels piratés. L'attaquant intégrera un logiciel malveillant dans un système d'exploitation populaire ou un film pour que la victime le télécharge. Une fois que la victime télécharge et exécute le logiciel, le code malveillant s'exécute sur le système de la victime, et l'attaquant obtient un accès complet à la machine de la victime.

### PiggyBacking

Le PiggyBacking signifie utiliser quelqu'un d'autre pour attaquer une victime potentielle. L'attaquant utilisera un tiers (généralement innocent) qui a accès à la victime afin de mener une attaque de piggybacking.

Il existe de nombreuses variations de Piggybacking. Si un attaquant suit votre employé jusqu'à votre bureau en utilisant sa carte d'accès, cela s'appelle le tailgating.

Il y a eu de nombreux cas d'attaques de piggybacking, surtout pour des informations classifiées. Les entreprises fournisseurs qui fournissent du matériel/logiciel à des organisations gouvernementales sont généralement la cible d'attaques de piggybacking.

Une fois que ces fournisseurs sont compromis, il est facile d'attaquer l'institution cible puisque le fournisseur a déjà un niveau d'accès à la cible.

Le Piggybacking est également associé à certaines formes de [écoute active](https://whatis.techtarget.com/definition/wiretapping). L'attaquant utilisera une connexion légitime de la victime afin d'espionner le réseau.

[J'ai récemment écrit un article sur Wireshark que vous pourriez trouver intéressant.](https://medium.com/manishmshiva/wireshark-a-walkthrough-of-the-best-packet-analyzer-in-the-world-9af0358ed9a1)

### Water Holing

Le Water Holing prend en compte les actions de routine de la cible et utilise l'une de ces actions pour obtenir un accès non autorisé. Par exemple, un attaquant trouvera les sites web que la cible utilise quotidiennement et essaiera d'installer un logiciel malveillant sur l'un de ces sites.

Le nom "Water Holing" est dérivé du fait que les prédateurs dans la nature attendent souvent leurs proies près de leurs points d'eau communs.

Un exemple est la campagne [Holy Water de 2019](https://www.techrepublic.com/article/holy-water-watering-hole-attack-targets-visitors-of-certain-websites-with-malware), qui ciblait des groupes religieux et caritatifs asiatiques. Le site web a été compromis après quoi les visiteurs étaient invités à installer Adobe Flash sur leurs navigateurs.

Étant donné qu'Adobe Flash présente un certain nombre de vulnérabilités, il était facile pour les attaquants d'exécuter du code malveillant sur les machines des victimes. Les attaques par watering hole sont rares, mais elles posent une menace considérable car elles sont très difficiles à détecter.

## Se protéger de l'ingénierie sociale

Maintenant que nous avons vu les différents types d'approches utilisées par les ingénieurs sociaux, examinons comment nous pouvons nous protéger, nous et notre organisation, contre les attaques d'ingénierie sociale.

### Installer des filtres anti-spam et anti-email

Bien que les filtres anti-spam ne puissent pas attraper les attaques très ciblées, ils empêcheront la plupart des spams et des emails malveillants d'atteindre votre compte.

### Garder l'antivirus et le pare-feu à jour

De manière similaire aux filtres anti-spam, un logiciel antivirus à jour protégera contre la plupart des [virus, chevaux de Troie et logiciels malveillants](https://medium.com/manishmshiva/penetration-testing-100-terms-you-need-to-know-a723c38cd8c8) courants.

### Demander une vérification

Demandez toujours une vérification lorsqu'une personne vous appelle en prétendant représenter une organisation, par exemple votre banque. Ne partagez jamais de détails confidentiels tels que des numéros de carte de crédit ou des mots de passe par téléphone ou par email.

### Créer une sensibilisation

La meilleure façon de prévenir l'exploitation de votre organisation est de créer des programmes de sensibilisation à la sécurité. Éduquer vos employés est un excellent investissement à long terme pour garder votre entreprise en sécurité.

### Si cela semble trop beau pour être vrai, c'est probablement le cas

Enfin, si quelque chose semble trop beau pour être vrai, c'est généralement le cas. Ne faites jamais confiance à des inconnus promettant de vous rendre riche rapidement. Comme quelqu'un l'a dit un jour, "essayer de devenir riche rapidement est le moyen le plus rapide de perdre tout votre argent".

## Conclusion

Les ingénieurs sociaux sont des maîtres de la manipulation. À moins que les employés d'une entreprise ne soient formés à la sensibilisation à l'ingénierie sociale, il est très difficile pour eux d'éviter de tomber dans le piège d'un ingénieur social.

Les ingénieurs sociaux jouent avec les émotions des gens, généralement la peur et l'avidité. Donc, chaque fois que vous effectuez une action basée sur ces deux émotions, vous pourriez vouloir faire un pas en arrière et voir si vous êtes manipulé.

Il y a une célèbre conférence TED où quelqu'un a commencé une conversation avec un spammeur. [Regardez la vidéo complète ici](https://www.youtube.com/watch?v=LiLS7U7YIdc&ab_channel=EisseCatherineWade).

[**_Vous pouvez obtenir un résumé de mes articles_**](https://tinyletter.com/manishmshiva) _et des vidéos envoyés à votre email chaque lundi matin. Vous pouvez également_ [**_en apprendre plus sur moi_**](https://www.manishmshiva.com/) _ici._