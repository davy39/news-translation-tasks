---
title: Comment améliorer votre sécurité et votre confidentialité numériques – Meilleures
  pratiques pour les développeurs
subtitle: ''
author: Loki Privacy
co_authors: []
series: null
date: '2024-06-18T12:05:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-improve-your-digital-security-and-privacy
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/pexels-wdnet-101808.jpg
tags:
- name: best practices
  slug: best-practices
- name: privacy
  slug: privacy
- name: Security
  slug: security
seo_title: Comment améliorer votre sécurité et votre confidentialité numériques –
  Meilleures pratiques pour les développeurs
seo_desc: "These days, there are many different types of attacks that can jeopardize\
  \ your digital security and privacy. So it’s a good idea to stay up-to-date with\
  \ best practices to keep you safe online. \nBut it can be hard to understand exactly\
  \ how to do this...."
---

De nos jours, il existe de nombreux types d'attaques différentes qui peuvent compromettre votre sécurité et votre confidentialité numériques. Il est donc judicieux de rester à jour avec les meilleures pratiques pour vous protéger en ligne.

Mais il peut être difficile de comprendre exactement comment faire. J'ai donc créé ce tutoriel et cette [évaluation de la sécurité/confidentialité personnelle](https://loki2100.limesurvey.net/948232?lang=en), basée sur ce que j'ai appris en développant [Loki Privacy](https://lokiprivacy.com/). Ces ressources résument des milliers d'heures de pratique et de recherche en cinq étapes impactantes (et largement gratuites).

En suivant ces directives, vous pouvez vraiment améliorer votre sécurité et votre confidentialité numériques, et peut-être aider à atténuer une cyberattaque dévastatrice sur vos finances personnelles ou vos données.

## Voici ce que nous allons couvrir :

1. [Utiliser les identifiants avec sagesse](#heading-1-utiliser-les-identifiants-avec-sagesse)
2. [Choisir son navigateur avec sagesse](#heading-2-choisir-son-navigateur-avec-sagesse)
3. [Comprendre le chiffrement et ce qu'il signifie](#heading-3-comprendre-le-chiffrement-et-ce-quil-signifie)
4. [Comment vous dépensez votre argent en ligne laisse une trace](#heading-4-comment-vous-depensez-votre-argent-en-ligne-laisse-une-trace)
5. [Les appareils que vous utilisez comptent pour la confidentialité et la sécurité](#heading-5-les-appareils-que-vous-utilisez-comptent-pour-la-confidentialite-et-la-securite)

## 1 : Utiliser les identifiants avec sagesse

La première étape consiste à gérer correctement vos mots de passe et à ajouter une couche de sécurité avec l'authentification à deux facteurs.

De nos jours, les mots de passe numériques contrôlent une immense quantité de pouvoir et d'informations personnelles. Vous pouvez accéder à votre banque et/ou à vos économies avec eux, ou à des informations médicales critiques et personnelles vous concernant. Un grand pouvoir en tant qu'utilisateur d'Internet implique une grande responsabilité – et cela est vrai pour l'utilisation des mots de passe modernes.

### Utiliser un gestionnaire de mots de passe

Idéalement, les gestionnaires de mots de passe sont le meilleur système pour gérer vos identifiants. Ils offrent un chiffrement et une sécurité pour prévenir les accès indésirables, et ils sont capables de donner deux propriétés critiques aux bons mots de passe.

* Premièrement, ils vous donnent la possibilité de générer automatiquement des mots de passe et de vous connecter avec le gestionnaire de mots de passe si vous le choisissez. Cela aide à éviter le péché capital de la sécurité personnelle sur le web : la réutilisation de mots de passe sur plusieurs services. Si un service se fait pirater avec votre mot de passe et que vous le réutilisez sur le web, les pirates essaieront votre login/mot de passe sur le web, transformant potentiellement un piratage en plusieurs.
* Deuxièmement, les gestionnaires de mots de passe vous permettent de créer plus facilement des mots de passe plus longs et plus complexes.

De bonnes options sont des services comme 1Password et BitWarden. Vous pouvez héberger votre propre version de BitWarden sur votre propre serveur avec quelque chose comme StartOS [et l'implémentation open source de BitWarden, Vaultwarden](https://github.com/Start9Labs/vaultwarden-startos).

### Utiliser un mot de passe fort

Le nombre et le type de caractères dans votre mot de passe peuvent empêcher les attaques par force brute – c'est-à-dire, utiliser des machines pour deviner des combinaisons de lettres. La force d'un mot de passe dépend beaucoup de sa longueur. [Si vous utilisez 14-16 caractères](https://bitwarden.com/blog/how-long-should-my-password-be/) ou plus, il faudra des siècles à une machine pour essayer de deviner le mot de passe. Mais si vous utilisez 6 caractères ou moins, il est probable que votre mot de passe puisse être craqué en quelques secondes.

La force de votre mot de passe peut également s'améliorer si vous ajoutez des caractères spéciaux, variez la casse de majuscules à minuscules, et ajoutez des nombres – tout ce qui perturbe les machines qui passent par des combinaisons de caractères par routine, espérant avoir de la chance.

#### Exemples de mots de passe forts :

* 32 chaînes de caractères aléatoires, incluant idéalement des nombres et des caractères spéciaux
* Plusieurs mots enchaînés avec quelques nombres/caractères spéciaux pour faciliter la saisie manuelle

#### Exemples de mots de passe faibles :

* Combinaisons de mots et de nombres couramment utilisés et réutilisés, comme hello12
* Chaînes plus courtes comme 342yf – plus votre combinaison est courte, même si elle semble aléatoire, plus elle est facile à craquer par force brute
* Mots de passe que vous utilisez sur plusieurs services, peu importe leur force (si l'un des mots de passe est divulgué, il sera tenté avec tous vos services).

### Configurer l'authentification à deux facteurs

Vous devriez également ajouter une authentification à deux facteurs sur tous vos appareils, et idéalement les versions les plus fortes de celles-ci. Ainsi, même si l'un de vos mots de passe est craqué, cela n'aura pas d'importance – car les attaquants n'auront pas accès à un second facteur qui leur permettrait d'accéder à votre compte.

Vous voudrez également recevoir des notifications pour les tentatives de connexion échouées. Ainsi, vous saurez si quelqu'un a craqué votre mot de passe (et vous voudrez supprimer ce mot de passe de tous les services en ligne que vous utilisez actuellement.).

Normalement, cela serait une combinaison de ce qu'on appelle l'authentification à deux facteurs HOTP et TOTP.

HOTP et TOTP sont deux schémas différents de mots de passe à usage unique utilisés soit par des clés de sécurité matérielles, soit par des applications 2FA comme Google Authenticator. Vous l'aurez vu en action si vous utilisez un outil comme Aegis ou Raivo où vous obtenez des codes de réinitialisation que vous copiez et collez dans votre navigateur toutes les 30 secondes.

La différence entre les deux est que le schéma de code HOTP tend à être utilisé avec des clés de sécurité matérielles et s'incrémente par utilisation. Mais cela laisse une fenêtre de temps plus longue où un attaquant peut violer le code.

Les systèmes basés sur le temps ne vous donnent que entre 30 secondes et 60 secondes pour vous connecter avec le code, mais l'utilisateur dispose de suffisamment de temps pour réessayer les codes dans une fenêtre aussi courte. Certains des éléments les plus sécurisés combinent à la fois HOTP et une fenêtre basée sur le temps.

**À retenir** : Probablement les meilleures choses que vous pouvez faire pour votre sécurité numérique dès maintenant sont :

* Avoir un système de gestionnaire de mots de passe qui vous permet d'éviter la réutilisation de mots de passe
* Avoir une authentification à deux facteurs soit via une application (comme Aegis ou Raivo) soit, si vous êtes prêt à investir, une clé de sécurité matérielle comme une Yubico.

## 2 : Choisir son navigateur avec sagesse

Ensuite, vous voudrez réfléchir au navigateur que vous utilisez et aux données que vous révèlez sur vous-même.

### Utiliser un navigateur axé sur la sécurité

Le navigateur que vous utilisez pour accéder à Internet stocke des données sur vous et partage des données sur qui vous êtes et quels sont vos centres d'intérêt. Votre choix de navigateur et les extensions que vous chargez détermineront combien de suivi publicitaire vous autorisez, ainsi que le nombre de cookies.

Une installation par défaut de Firefox, Chrome ou Safari n'aura pas beaucoup de fonctionnalités préservant la confidentialité. Mais vous pouvez télécharger des extensions comme Privacy Badger, HTTPS Everywhere et uBlock Origin pour vous aider à mieux défendre votre confidentialité et votre sécurité en ligne.

Ces outils serviront de bloqueurs de scripts et de publicités, ainsi que de garantie que vous naviguerez sur des sites où vos données sont chiffrées – une considération importante lorsque nous arrivons au point 3.

### Envisager d'utiliser un VPN

De plus, si vous utilisez votre Internet régulier sans VPN ou sans utiliser un service comme Tor, vous révèlez probablement votre adresse IP et votre adresse MAC.

L'adresse IP est malléable, mais peut révéler approximativement où vous vous trouvez. IPInfo, par exemple, montre que vous pouvez lier une adresse IP [à votre emplacement](https://ipinfo.io/ip-address-information) avec la latitude et la longitude représentées, l'entreprise fournissant votre Internet, et peut-être l'entreprise qui possède l'adresse IP.

Votre adresse MAC est liée à votre appareil et est relativement statique. Lorsque vous utilisez un VPN ou Tor, vous pouvez montrer une adresse IP différente de celle liée à votre réseau domestique ou aux réseaux ouverts non sécurisés comme le WiFi de votre café local. Mais selon le VPN que vous utilisez, vous pourriez leur donner accès à chaque site que vous visitez – il est donc important de vous assurer que vous travaillez avec un fournisseur qui a une politique de non-journalisation comme MullvadVPN.

**À retenir** : Si vous êtes préoccupé par la confidentialité et la sécurité numériques, utilisez une variante de navigateur axée sur la confidentialité, que ce soit sur ordinateur ou sur mobile. Cela pourrait être quelque chose comme Librewolf et Duckduckgo sur mobile.

Votre moteur de recherche par défaut ne devrait pas être Google. Il devrait être Duckduckgo ou une variante plus axée sur la confidentialité (bien que notez que Duckduckgo servira toujours des publicités via l'échange de publicités de Microsoft).

Vous devriez également comprendre les implications de révéler votre adresse IP et votre adresse MAC. Assurez-vous d'évaluer si l'utilisation de Tor ou d'un VPN a du sens pour vous. Choisissez soigneusement le VPN que vous utilisez.

## 3 : Comprendre le chiffrement et ce qu'il signifie

Le terme "Chiffrement" est souvent utilisé à tort et à travers. Mais vous vous demandez peut-être comment cela vous concerne vraiment.

Eh bien, en matière de confidentialité et de sécurité numériques, comprendre la différence entre https:// et http://, le texte en clair vs le texte haché, et le chiffrement de bout en bout est très important.

### HTTP vs HTTPS

Commençons par https:// plutôt que http://. Pourquoi est-il important de savoir quel type de site vous consultez ?

HTTP alimente le web. Essentiellement, lorsque vous naviguez sur Internet, en coulisses, votre appareil effectue une série de requêtes HTTP vers les serveurs que vous lui indiquez. Cependant, avec le trafic http:// régulier, chaque fois que quelqu'un voit les requêtes et communications HTTP, [il peut voir le texte à l'intérieur](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/). Cela signifie que si vous envoyiez des mots de passe, des informations de carte de crédit ou d'autres communications sensibles, il serait trivial d'intercepter ces messages.

HTTPS, en revanche, signe HTTP avec des clés de chiffrement en utilisant [une méthode appelée TLS](https://www.freecodecamp.org/news/what-is-tls-transport-layer-security-encryption-explained-in-plain-english/). En bref, si vous utilisez https:// et naviguez partout avec https:// (ce qu'une extension comme HTTPS Everywhere peut aider à forcer), vous êtes moins susceptible de divulguer vos données aux attaquants.

### Texte en clair vs texte haché

Vous entendrez souvent parler de texte en clair vs texte haché lorsqu'il s'agit d'expliquer une faille de mot de passe. Le texte en clair signifie que si un attaquant obtient des données de mot de passe, il a votre mot de passe sous sa forme texte complète. Si c'est haché, cela signifie que l'attaquant obtiendra un ensemble de symboles qui ne sont pas votre mot de passe, mais peut-être qu'avec un peu de travail, ils peuvent obtenir votre mot de passe en texte brut.

Si un site web stocke vos mots de passe en texte clair, cela signifie que les attaquants qui obtiennent une base de données pleine de mots de passe pourront facilement utiliser ce stock immédiatement. Une fuite en texte clair signifie que vous devez changer vos mots de passe avec beaucoup plus d'urgence, bien que même si un mot de passe est haché, vous devriez toujours le changer.

Des services comme haveibeenpwned.com vous aideront à déterminer quelles fuites de mots de passe s'appliquent à un email – et il est bon de vérifier de temps en temps si vous avez des identifiants compromis (certains gestionnaires de mots de passe vérifieront automatiquement cela pour vous également.).

Le chiffrement de bout en bout est un terme technique qui semble complexe mais qui offre une promesse simple : dans la base de code, seul l'expéditeur et le destinataire d'un message pourront voir et déchiffrer le message original. Cela signifie que le service sur lequel les messages sont hébergés ne peut pas voir ce qui est transmis, et ne peut donc pas envoyer ces informations à quiconque.

Des services comme Signal offrent un chiffrement de bout en bout par défaut (y compris dans les chats de groupe) et sont considérés comme la référence. WhatsApp offre également un chiffrement de bout en bout par défaut, bien que son association avec Meta rende parfois les défenseurs de la confidentialité méfiants.

D'autres services offrent des variantes, mais vous devez les activer – par exemple, Telegram offre un chiffrement de bout en bout pour les "chats secrets", mais pas pour les chats de groupe et les chats privés non secrets.

**À retenir** : Assurez-vous de naviguer sur des sites https:// avec une extension de navigateur ([HTTPS Everywhere](https://www.eff.org/https-everywhere)). Vérifiez également si vos mots de passe ont été compromis et comment ils l'ont été avec [HaveIBeenPwned.com](https://haveibeenpwned.com/). Et restez fidèle au chiffrement de bout en bout sur les chats et les communications si vous voulez vous assurer que seules les personnes que vous souhaitez voir vos communications peuvent le faire.

## 4 : Comment vous dépensez votre argent en ligne laisse une trace

En ligne, un front pour la confidentialité numérique est la manière dont vous dépensez et possédez de l'argent. Dans le monde analogique, vous pouvez dépenser de l'argent liquide et être assuré qu'il est peu probable que votre transaction soit retracée jusqu'à vous.

Dans le monde numérique, cependant, vous avez le fardeau d'une carte de crédit ou de débit liée à votre adresse et à vos noms pour chaque transaction que vous effectuez. Bien que la sécurité en ligne ait été développée pour s'assurer que celles-ci ne fuient pas (bien qu'elles puissent encore et l'ont fait), il existe également de nouvelles façons de transiger en ligne avec une option (relativement) préservant la confidentialité : Bitcoin, Lightning Network.

Lightning Network est une technologie de deuxième couche construite sur Bitcoin qui n'enregistre pas son flux transactionnel entre les nœuds sur la chaîne, mais règle plutôt les ouvertures/fermetures de canaux sur celle-ci. Cela vous permet de transiger en Bitcoin rapidement, sans frais, et sans que chaque transaction n'apparaisse sur la chaîne Bitcoin.

Maintenant, les nuances de l'utilisation d'outils comme Lightning Network et Bitcoin de manière à préserver la confidentialité méritent une discussion beaucoup plus approfondie – mais soyez conscient qu'un compromis existe désormais.

Oui, l'utilisation de Bitcoin vous exposera à la diffusion de vos transactions sur un grand livre public, scanné par peut-être des millions de personnes. Mais cela vous permettra également de transiger avec l'adresse IP de votre choix, l'appareil de votre choix et l'identité de votre choix. C'est à vous de faire le travail et de déterminer si ce compromis en vaut la peine.

**À retenir** : Soyez conscient qu'il existe des alternatives à l'utilisation d'une carte de crédit ou de débit en ligne pour tous vos paiements, qui sont plus proches de la manière dont vous pourriez utiliser de l'argent liquide dans le monde analogique.

## 5 : Les appareils que vous utilisez comptent pour la confidentialité et la sécurité

Enfin, les appareils que vous utilisez comptent pour la confidentialité et la sécurité. Internet est un compromis : vous obtenez l'accès à de nombreux services différents, mais vous soumettez les appareils que vous utilisez pour accéder à ces services à l'émission et à la réception de données.

La plupart des ordinateurs portables et téléphones commercialisés ont des fonctionnalités de confidentialité et de sécurité intégrées. Un exemple de cela est les changements matériels qui rendent les iPhones récents plus résistants, ou les mises à jour de sécurité fréquentes pour le système d'exploitation en question, de Linux, Microsoft, à Mac, à iOS et Android.

Le compromis avec les appareils, cependant, tend à être le coût, le prix et la maintenance. En théorie, avoir un deuxième appareil à la fois sur ordinateur portable et mobile (pour les voyages, par exemple, pour éviter les saisies à la frontière) est idéal. Et vous pourriez vouloir expérimenter avec différents systèmes d'exploitation – par exemple, le GrapheneOS axé sur la confidentialité pour mobile, et System76 ou Pinebooks pour les ordinateurs portables basés sur Linux.

Vous pourriez même aller plus loin et décider d'expérimenter avec des serveurs domestiques pour exécuter vos propres services.

En fin de compte, le choix vous appartient : le coût de l'expérimentation ici peut être élevé en termes de temps et d'argent dépensés, mais peut en valoir la peine pour maintenir le contrôle sur vos propres appareils et données.

**À retenir** : Considérez les appareils que vous utilisez. Assurez-vous d'être à jour avec les mises à jour de sécurité, et déterminez comment et quels appareils vous souhaitez utiliser à l'avenir.

## Conclusion

Si vous êtes intéressé à en apprendre un peu plus sur la manière dont votre sécurité et votre confidentialité numériques se comparent, [cette évaluation](https://loki2100.limesurvey.net/948232?lang=en) vous aidera à déterminer votre niveau et à vous donner des recommandations spécifiques.

L'aspect le plus important de la sécurité et de la confidentialité numériques est d'être conscient des compromis, et de considérer et souvent réévaluer les meilleures pratiques dans un écosystème en évolution active.