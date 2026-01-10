---
title: Comment les développeurs peuvent prévenir la fraude et arrêter les escrocs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-20T22:32:41.000Z'
originalURL: https://freecodecamp.org/news/how-developers-can-prevent-fraud-and-stop-scammers
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/48332996261_4f1a1657fc_b.jpg
tags:
- name: information security
  slug: information-security
- name: Security
  slug: security
seo_title: Comment les développeurs peuvent prévenir la fraude et arrêter les escrocs
seo_desc: "By Dmitry Dragilev\nOnline frauds and scams have shot past projections\
  \ in the last decade, and no one seems to be immune to them—including developers.\
  \ \nThe shift to serverless cloud management has opened doors for hackers to try\
  \ new attack surfaces an..."
---

Par Dmitry Dragilev

Les fraudes et escroqueries en ligne ont dépassé toutes les projections au cours de la dernière décennie, et personne ne semble être à l'abri, y compris les développeurs. 

Le passage à la gestion du cloud serverless a ouvert des portes aux pirates pour tester de nouvelles surfaces d'attaque, et l'impact est bien réel. [90 % des applications web sont vulnérables aux cybercriminels](https://www.freecodecamp.org/news/what-is-devsecops/https://www.freecodecamp.org/news/what-is-devsecops/), et la majorité de ces vulnérabilités proviennent de dépendances directes.

Grâce aux migrations vers le cloud, les équipes DevOps peuvent déployer des itérations de produits plus rapidement et améliorer les KPI de gestion client. Mais cela signifie aussi qu'elles perdent le contrôle sur l'infrastructure de code personnalisé et les serveurs. Les entreprises qui ont troqué la sécurité personnalisée pour l'efficacité du cloud sont aujourd'hui plus vulnérables aux cybercriminels.

Dans cet article, nous examinerons les escroqueries les plus courantes auxquelles les développeurs sont confrontés, leur fonctionnement et ce que les développeurs peuvent faire pour atténuer les risques.

## Qu'est-ce qu'une fraude ou une escroquerie ?

La fraude est une tentative illégale de tromper une personne, une entité ou une organisation pour obtenir l'accès à des actifs confidentiels. 

Les escroqueries (scams) sont les étapes plus petites qui aident les criminels à commettre des fraudes, et elles impliquent presque toujours de l'argent. 

Si vous avez été victime d'une escroquerie, il y a de fortes chances que vous ayez perdu de l'argent. Les fraudes, cependant, ne mènent pas toujours à une ruine financière immédiate, car leur impact peut être bien plus vaste que cela.

Les équipes DevOps sont de plus en plus vulnérables aux fraudes et aux escroqueries car celles-ci reposent sur la tromperie et l'ingénierie sociale. Étant donné que la gestion des accès est une faille de sécurité majeure du développement informatique moderne, les fraudeurs cherchent à obtenir les identifiants des développeurs pour compromettre les systèmes et voler de l'argent ou des informations.

## Quatre escroqueries courantes et leur fonctionnement

Aujourd'hui, les pirates utilisent des stratégies précises pour créer le plus grand impact possible. Ils sont passés de méthodes « éprouvées » à des attaques hautement ciblées et innovantes qui finissent par tromper même les victimes les plus sensibilisées à la sécurité, comme les développeurs.

Pour mieux comprendre comment elles fonctionnent, voici quelques exemples :

### 1. Attaques DDoS

Les attaques par déni de service distribué (DDoS) sont l'un des types de cyberattaques les plus courants qui affligent les développeurs aujourd'hui. Avec une attaque DDoS, les criminels tentent de submerger un réseau ou une application web en envoyant une quantité énorme de requêtes d'accès, ce qui finit par les paralyser. 

Comme la plupart des entreprises dépendent aujourd'hui de leur infrastructure numérique pour fonctionner, un site web ou une application hors ligne à un moment crucial peut entraîner des pertes massives, tant financières que réputationnelles.

Les [attaques DDoS](https://www.bigcommerce.com/blog/denial-of-service-attack/) utilisent des machines compromises et des appareils IoT comme zombies (ou bots) pour envoyer des millions de pings en un court laps de temps. Les attaquants peuvent cibler l'architecture du serveur en usurpant (spoofing) des paquets de données SYN, stresser les ressources logicielles en utilisant le flood HTTP, ou déverser un trafic massif sur le site web avec l'amplification DNS.

Comme il est difficile de distinguer les requêtes de botnets des requêtes authentiques, les victimes ont souvent du mal à séparer les deux. De plus, la nature distribuée de l'attaque signifie que le blocage d'une seule adresse IP ne résoudra pas le problème.

![Image](https://lh5.googleusercontent.com/JWZmINyPOstdWofeQ078TRQ8xDhYUzskB9-3RJpuSpyhhMpw-6JCMgucZ-3e1pC5pVTaThM7A6Kw-IgVToxVWCVEyGrcu-yJjvTYG4vDAZzsVxm9yjgpsVYdiYSA2wP80H6LB3eXzr6DJwFf1puTXeQ)
_Réponses TTL bizarres avec des valeurs étranges qui indiquent manifestement qu'elles ne proviennent pas du serveur d'origine, mais plutôt d'un appareil intermédiaire. [Source](https://blog.erratasec.com/2015/04/pin-pointing-chinas-attack-against.html)_

L'un des exemples les plus célèbres d'attaques DDoS a été l'attaque de 2015 contre GitHub par des assaillants chinois. Elle a commencé par l'injection de code JavaScript, exécuté par une société de télécommunications appelée China Unicom, dans les navigateurs utilisés pour visiter Baidu et les sites web utilisant Baidu Analytics. 

Le code malveillant a créé un botnet de navigateurs affectés et les a incités à envoyer une quantité massive de requêtes HTTP vers des pages GitHub spécifiques. L'attaque a duré cinq jours et de nombreuses parties de GitHub étaient inaccessibles. 

### 2. Escroqueries à la carte de crédit

Les équipes DevOps ont souvent une attitude laxiste envers la conformité financière, ce qui en fait une porte d'entrée pour les escroqueries à la carte de crédit. Ces types d'escroqueries cherchent soit à s'emparer des cartes de crédit des employés, soit à recueillir suffisamment de données pour mener des fraudes à la carte non présente (CNP).

Les [escroqueries à la carte de crédit peuvent se produire de plusieurs manières](https://www.aura.com/learn/credit-card-scams) et les attaquants testent sans cesse de nouvelles méthodes pour tromper leurs victimes. 

Cela peut commencer par un simple « shoulder surfing » (regarder par-dessus l'épaule) où un attaquant vous surveille pendant que vous saisissez votre code PIN, ou l'utilisation d'enregistreurs de frappe (keyloggers) avancés et de skimmers de cartes placés sur des distributeurs automatiques suspects. Les fausses associations caritatives et les récompenses fictives sont également des moyens populaires pour obtenir des détails de carte de crédit.

En plus de cela, les criminels peuvent utiliser des données d'identification personnelle (PII) pour demander une nouvelle carte de crédit ou solliciter des mises à jour de votre ancienne carte pour la bloquer. Ils peuvent aller jusqu'à intercepter des cartes dans le courrier ou agresser des victimes pour voler leurs cartes de crédit.

Même s'ils ne mettent pas la main sur votre carte physique, les fraudes CNP leur permettent d'effectuer d'énormes transactions en ligne, ce qui peut ruiner le score de crédit de la victime et mettre ses finances dans une situation difficile.

### 3. Fraude au trunking SIP

La communication d'entreprise moderne repose sur les [systèmes téléphoniques VoIP](https://www.nextiva.com/products/voip-phone-system.html) pour joindre les clients, les fournisseurs et les parties prenantes, et utilise la flexibilité omnicanale pour améliorer la productivité. Tout cela semble parfait sur le papier, mais la VoIP utilisée par les petites entreprises est souvent victime de la fraude au trunking SIP.

Le trunk SIP (Session Initiation Protocol) est la technologie qui connecte le système téléphonique existant d'une entreprise ou un PBX au cloud, permettant à la VoIP de fonctionner dans le monde entier. C'est une pièce technologique cruciale qui est souvent exploitée par les pirates. Voici comment cela se passe généralement :

* Les cybercriminels utilisent des scanners IP pour rechercher des systèmes téléphoniques vulnérables afin d'accéder aux trunks SIP.
* Ils volent des mots de passe ou utilisent des attaques par force brute sur des systèmes faibles.
* Une fois l'accès obtenu, les attaquants usurpent souvent les identifiants de l'appelant pour extraire des données sensibles telles que les détails de carte de crédit et de connexion, ou espionnent les textes et les appels sur les connexions IP publiques.
* En plus de cela, les attaquants peuvent commettre une fraude au péage en redirigeant les appels vers des [numéros de téléphone virtuels](https://www.nextiva.com/blog/what-is-a-virtual-phone-number.html) dans des territoires domestiques et internationaux surtaxés, et en volant les revenus générés par ces appels.

![Image](https://lh3.googleusercontent.com/qmcSLLBIb_MXtMDC-ajfsAKdfJ8bBkmJYHsQ3a3EoVXBLUy6dZZI7t4MivBQR01BoLZbxtp8WzHL82qHSP8iokj-8i28GGWj4mRpyerRL1ij1x0hZIexF-e0pDU6TpEBEuDORP2CoapU1FLQP0_4PY0)
_Twilio signale les appels frauduleux en utilisant leur base de données anti-fraude tierce. [Source](https://www.twilio.com/blog/2018/03/how-to-protect-your-account-from-toll-fraud-with-voice-dialing-geo-permissions.html)_

Si la fraude au trunking SIP n'est pas contrôlée, une entreprise peut perdre des milliers de dollars en quelques heures.

### 4. SIM Swapping

Le SIM swapping peut arriver à n'importe qui et les développeurs n'ont pas de protection supplémentaire contre ce type d'escroquerie. Le SIM swapping consiste à convaincre votre fournisseur de réseau de transférer votre SIM sur l'appareil de l'escroc, prenant ainsi le contrôle effectif de votre numéro de téléphone et de tout ce qui y est lié.

Le [SIM swapping ne se produit pas par hasard](https://www.aura.com/learn/how-to-prevent-sim-swapping) ; il nécessite une planification à long terme et de l'ingénierie sociale. Voici comment cela fonctionne :

* Un escroc appelle votre fournisseur de carte SIM et demande le transfert du numéro de téléphone en prétendant que l'appareil a été détruit ou volé.
* Le représentant demande alors une preuve d'identité pour authentifier le transfert, ce qui nécessite généralement des informations personnelles telles que l'adresse, l'e-mail, l'IMEI ou les quatre derniers chiffres de la carte de crédit.
* Si l'escroc parvient à prouver votre identité pour tromper l'opérateur, il peut activer une nouvelle carte SIM dans son propre téléphone.

C'est là que les stratégies à long terme entrent en jeu. Avant d'exécuter un SIM swapping, les attaquants utilisent des e-mails de phishing, des logiciels malveillants et des violations de données pour collecter des bribes de données personnelles et les assembler afin de convaincre le fournisseur de carte SIM.

![Image](https://lh6.googleusercontent.com/q6I7_Md5LIl7ladti5IWTOGlMD8nj2cHmBGOpH-Hcbm9LQm_QXTjIlgy5x1WqDZvBYM0n75XXqQiQB2BQccskFFAyGP16cn7-jcDkKx0mGJkAqcMSvI6NNTrHMHuIbqQmVSDIkTphkzgHOobLhi7VOs)
_Exemple de message texte d'escroquerie au SIM swapping. [Source](https://www.phonearena.com/news/Cops-bust-gang-that-used-stolen-SIM-cards-to-access-bank-accounts_id107701)_

Il y a quelques années, un employé mécontent de T-Mobile a exposé les données de clients à des pirates qui ont ensuite procédé à des échanges de SIM pour prendre le contrôle des comptes.

Une fois que les attaquants ont votre SIM, ils peuvent contourner l'authentification à deux facteurs (2FA) pour toutes les transactions et accéder à vos coordonnées bancaires, votre numéro de sécurité sociale et vos médias personnels. Le SIM swapping ouvre la porte à tous les types de crimes qui nécessitent votre numéro de téléphone.

## Comment le DevOps peut prévenir la fraude et les escroqueries

Les risques de sécurité sont nombreux, mais les développeurs connaissent bien ces concepts. En suivant quelques étapes, vous pouvez détecter, traiter et atténuer la plupart de ces escroqueries.

### Comment prévenir les attaques DDoS

Les attaques DDoS sont difficiles à distinguer sans nuire au trafic réel, ce qui rend l'atténuation complexe. Mais vous pouvez tout de même essayer quelques méthodes.

#### 1. Détecter les signes d'une attaque DDoS

Connaissez les symptômes des attaques DDoS pour les détecter tôt. Si un actif en ligne est soudainement lent ou ne répond plus, vous devrez peut-être chercher des signes de DDoS. Ceux-ci incluent :

* Un volume de trafic anormalement élevé à des heures inhabituelles de la journée.
* Des vagues de requêtes provenant de la même adresse IP, du même emplacement, du même appareil ou du même navigateur, et ciblant une page ou une partie spécifique de l'application.

Vous pouvez réagir rapidement si vous avez surveillé et documenté les schémas de trafic habituels de votre entreprise.

#### 2. Déployer des mesures anti-DDoS

Commencez par utiliser du matériel et des applications conçus pour prévenir les tentatives de DDoS et restaurer les actifs, en [décentralisant les centres de données et les serveurs](https://www.freecodecamp.org/news/how-to-manage-data-storage/), en utilisant un pare-feu d'application web (WAF) et en migrant vers le cloud pour augmenter la bande passante. 

AWS Shield Advanced est un service de protection DDoS géré, facile à configurer, capable de détecter et d'atténuer des attaques complexes et à grande échelle. 

En plus d'utiliser des outils anti-DDoS, vous devriez également combler les [failles de sécurité de votre réseau](https://www.algosec.com/resources/security-policy/) et pratiquer une cyber-hygiène quotidienne.

![Image](https://lh3.googleusercontent.com/KEsXtxDCDaRlXcQkDNq8AKHzcnIqvZfiHkKS2Sq0iXgmZ-myJ4aob6FLYf_lDWj3X_NhTsZKVC28wiXsF4Y26VSdpMJ4pc4gjPDP4VC9Xt7fdSnHkDEi5EQuSz7UbH-PbmER46qo-0AepFMsOnqK-rU)
_Exemple de configuration AWS pour l'atténuation des attaques DDoS. [Source](https://www.youtube.com/watch?v=hyGuV2e8SDw)_

#### 3. Avoir un plan de réponse DDoS en place pour prévenir d'autres dommages

Cela doit inclure des étapes documentées, une équipe bien préparée et des canaux de communication clairs pour les parties prenantes internes et externes. 

Les attaques DDoS multifactorielles modernes combinent plusieurs voies, donc plus vos plans sont complexes et approfondis, mieux vous pourrez protéger l'entreprise.

### Comment prévenir les escroqueries au trunking SIP

Le trunking SIP est une méthode courante de fraude téléphonique, mais vous disposez d'armes pour prévenir cela.

#### 1. Définir un tarif par défaut maximum pour les appels sortants afin de prévenir la fraude au péage

En fixant une limite au nombre d'appels, vous serez averti si votre entreprise dépasse ce seuil, ce qui vous permettra de surveiller les appels passés par des pirates.

En plus de cela, utilisez un [service VoIP](https://www.nextiva.com/solutions/small-business-phone-service.html) solide pour identifier les appels sortants et entrants et enregistrer autant d'informations que possible. Les pirates appelleront vers et depuis des numéros aléatoires, il devient donc plus facile pour vous de mettre en place un blocage d'appels pour les numéros suspects.

![Image](https://lh5.googleusercontent.com/49d4N6OJbwXWHNYsTiVUDk4WynrVv0O7tN3kD6aGB5B_-67KAaDnj2ODAQYzNQcXOX881MO0mbNPDh2vbDh819n4_KTI57AfkkiXTnrUsokQYH19ued4tTSNtHPVSxX4SU9-Kv2VO7ctjd2JWxXQkFA)
_Paramètres du fournisseur VOIP pour interdire les appels entrants présentant des caractéristiques de robocalls. [Source](https://telnyx.com/resources/add-rate-limits-outbound-profiles)_

#### 2. Activer l'authentification basée sur l'IP pour gérer l'accès au réseau

Avec cette option activée, les utilisateurs devront faire partie de votre réseau pour passer et recevoir des appels. Même si les adresses IP ne sont pas complètement cachées, vous serez averti de toute tentative d'intrusion dans votre réseau. En imposant une adresse IP statique, vous pouvez facilement configurer l'authentification basée sur l'IP et surveiller les appels.

#### 3. Renforcer la sécurité du PBX

Vous pouvez protéger votre système téléphonique en utilisant des mots de passe nouveaux et complexes, en les changeant régulièrement et en les stockant en toute sécurité, en installant correctement la configuration SBC et en utilisant TLS et SRTP pour des chiffrements supérieurs. En plus de cela, vous devriez également restreindre l'accès au matériel pour prévenir les violations de données.

### Comment prévenir les escroqueries à la carte de crédit

Les escroqueries à la carte de crédit peuvent ouvrir la boîte de Pandore et, en tant que développeur, vous devez être conscient des conséquences. Voici quelques étapes à suivre :

#### 1. Les employés utilisant des cartes de crédit d'entreprise sont les victimes les plus faciles

Vous pouvez les aider à atténuer les risques grâce à la formation. Une série de modules de formation et de séminaires fréquents devrait inclure l'identification des moyens par lesquels les détails de carte de crédit peuvent être volés (comme discuté plus haut) et la réactivité en cas de vol. 

Ces formations devraient également encourager les employés à n'accéder qu'à des sites HTTPS, à utiliser des VPN chaque fois qu'ils utilisent des appareils personnels ou le WiFi public, et les aider à identifier les logiciels malveillants et les tentatives de phishing. 

De plus, vous devriez utiliser un [service de protection contre l'usurpation d'identité](https://www.aura.com/learn/how-much-does-identity-theft-protection-cost) pour limiter les conséquences des escroqueries à la carte de crédit.

#### 2. En tant que développeur, vous êtes lié par des normes de conformité (et d'éthique) pour sécuriser les détails de carte de crédit des employés et des clients

Lors de l'écriture de code pour des logiciels destinés à traiter et stocker des cartes de crédit, vous devez répartir les tâches pour vous protéger et protéger l'entreprise. Peu de développeurs suivent les directives PCI DSS à cet égard et s'enferment dans des lourdeurs administratives de conformité.

Les sections 6, 7 et 8 de la [norme PCI DSS](https://www.pcisecuritystandards.org/resources-overview/) énoncent clairement les règles de révision du code par des tiers ainsi que la gestion des rôles et des accès. Le respect des normes de conformité et le fait de laisser les clés d'accès à l'administrateur sont des meilleures pratiques pour atténuer les escroqueries potentielles.

### Comment prévenir le SIM swapping

Le SIM swapping commence bien avant de convaincre les fournisseurs de cartes SIM d'activer une nouvelle SIM, c'est pourquoi vous devez prendre plusieurs mesures :

#### 1. Le phishing et d'autres méthodes d'ingénierie sociale sont utilisés pour vous imiter, soyez donc attentif à ces crimes

Soyez à l'affût des [e-mails de phishing](https://www.freecodecamp.org/news/how-to-recognize-phishing-email/) et des SMS, des injections de logiciels malveillants, des sites web compromis et des faux appels qui vous incitent à partager des détails personnels tels que les dates de naissance, les adresses physiques et électroniques, et les numéros de sécurité sociale. Les escrocs utilisent ces informations lors de l'appel à votre opérateur. 

Une autre façon de prévenir cela est de limiter la quantité de données personnelles que vous partagez en ligne. Voici un exemple d'e-mail de phishing bien conçu usurpant l'identité de PayPal. Il suffit de vérifier l'adresse de l'expéditeur pour repérer l'arnaque.

![Image](https://lh6.googleusercontent.com/loP48E4iNW0LGxX73HUtt-sA_Wzx2Fxq2WzYSY0BQW_m1mhZF6Li2SGfvgsbeIzafSiHzoldzX7CXhq_Vuup9hq4inQdgOJ1VGYfZj5oV8RuKQ1tkaFt1pQEHvvMONjt92FynXRpm4QyvtqQbIRwQck)
_Exemple d'une arnaque Paypal. [Source](https://www.pickr.com.au/how-to/2021/how-to-spot-a-paypal-phishing-email/)_

#### 2. Ne faites pas de votre numéro de téléphone l'élément central de votre sécurité

Comme le SMS n'est pas un mode de 2FA sécurisé en cas de vol d'appareil et de SIM swapping, utilisez la biométrie comme l'empreinte digitale ou l'identification faciale et des applications d'authentification comme Authy pour [protéger vos 2FA](https://www.freecodecamp.org/news/user-authentication-methods-explained/). 

En parlant d'applications tierces, vous devriez également utiliser un gestionnaire de mots de passe pour créer et maintenir des mots de passe alphanumériques uniques, complexes et de 14 caractères, afin de vous assurer que les attaquants ne peuvent pas utiliser vos informations personnelles pour deviner vos connexions.

#### 3. Activez les alertes pour que les banques puissent surveiller quand votre carte SIM est réactivée sur un appareil inconnu

Travaillez avec des entreprises qui utilisent des rappels (callbacks) pour vérifier les identités lors des transactions et n'oubliez pas d'activer le verrouillage par code PIN auprès de l'opérateur pour empêcher tout transfert non autorisé.

## Le mot de la fin

La cybercriminalité et les tactiques d'ingénierie sociale ont progressé à pas de géant, et les développeurs travaillant sur des projets critiques doivent s'assurer de ne pas devenir une faille de sécurité. 

En suivant les étapes ci-dessus, vous pouvez protéger votre employeur, vos collègues et vous-même contre les mauvaises surprises.