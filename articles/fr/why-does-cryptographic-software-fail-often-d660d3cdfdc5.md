---
title: Les nombreuses, nombreuses façons dont les logiciels cryptographiques peuvent
  échouer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-25T02:25:49.000Z'
originalURL: https://freecodecamp.org/news/why-does-cryptographic-software-fail-often-d660d3cdfdc5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eHaISV7BciMhq8o0AHmftg.png
tags:
- name: Cryptography
  slug: cryptography
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Les nombreuses, nombreuses façons dont les logiciels cryptographiques peuvent
  échouer
seo_desc: 'By Nabeel Yoosuf

  When cryptographic software fails, what’s to blame?

  Algorithms?

  Cryptography libraries?

  Apps incorrectly using those libraries?

  Or is it something else entirely?

  We rely on cryptographic algorithms and protocols every day for secure ...'
---

Par Nabeel Yoosuf

Lorsque les logiciels cryptographiques échouent, qui est à blâmer ?

Les algorithmes ?

Les bibliothèques cryptographiques ?

Les applications utilisant incorrectement ces bibliothèques ?

Ou est-ce quelque chose d'autre entièrement ?

Nous dépendons des algorithmes et protocoles cryptographiques chaque jour pour une communication sécurisée sur Internet. Nous pouvons accéder à nos comptes bancaires en ligne parce que la cryptographie nous protège. Nous pouvons envoyer des messages privés à nos amis parce que la cryptographie nous protège. Nous pouvons acheter et vendre des choses en utilisant des cartes de crédit et Bitcoin parce que la cryptographie nous protège.

Permettez-moi de vous donner un exemple concret. Lorsque vous consultez vos e-mails via votre navigateur préféré, la connexion entre votre navigateur et le serveur de messagerie est sécurisée à l'aide du protocole TLS (sécurité au niveau du transport), afin que personne ne puisse espionner vos e-mails ou les modifier en transit à votre insu.

En bref, sans cryptographie, l'Internet que nous connaissons aujourd'hui ne pourrait pas exister. La loi et l'ordre sur Internet dépendent de la cryptographie.

Mais cet outil sur lequel nous dépendons si fortement est également assez fragile. Nos logiciels cryptographiques nous déçoivent souvent. Parfois, ils nous déçoivent vraiment.

Avez-vous déjà pensé à pourquoi les logiciels cryptographiques — y compris les implémentations du protocole TLS — échouent encore et encore ?

Selon les rapports de Veracode sur l'état de la sécurité, nos logiciels cryptographiques sont tout aussi vulnérables qu'il y a deux ans.

![Image](https://cdn-media-1.freecodecamp.org/images/fe3A-m3hCNxrQMhkYQeuRcvTJB287TL-ot73)
_Veracode a classé les problèmes cryptographiques comme la vulnérabilité #2 trouvée dans les applications en 2015_

![Image](https://cdn-media-1.freecodecamp.org/images/H94qJr0QwDiVakmegPWDXbYSmRMMb9tZED-O)
_Veracode a de nouveau classé les problèmes cryptographiques comme la vulnérabilité #2 trouvée dans les applications en 2016_

Ces échecs sont-ils dus à des faiblesses dans les algorithmes cryptographiques sous-jacents ?

Eh bien, plusieurs attaques passées ([Apple iOS TLS](https://www.imperialviolet.org/2014/02/22/applebug.html), [WD self encrypting drives](http://hardwear.io/wp-content/uploads/2015/10/got-HW-crypto-slides_hardwear_gunnar-christian.pdf), [Heartbleed](https://www.us-cert.gov/ncas/alerts/TA14-098A), [WhatsApp messages](https://www.theguardian.com/technology/2017/jan/16/whatsapp-vulnerability-facebook), [Juniper's ScreenOS](https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=juniper%20screenos%20vulnerability), [DROWN](https://drownattack.com/), [Android N-encryption](http://karl-voit.at/2016/02/27/android-encryption/) et ainsi de suite) nous montrent que nos logiciels cryptographiques sont moins susceptibles d'être compromis en raison des faiblesses des algorithmes cryptographiques sous-jacents. En d'autres termes, la cryptanalyse est l'une des menaces les moins probables pour nos logiciels cryptographiques.

![Image](https://cdn-media-1.freecodecamp.org/images/9w3A4G6y-5zto71XmJxbTyDz8b5A6SwyVtaV)
_Un croquis de l'algorithme AES ([crédit image](http://www.moserware.com/2009/09/stick-figure-guide-to-advanced.html" rel="noopener" target="_blank" title=")) AKA pourquoi vous ne voulez pas créer votre propre cryptographie._

Avez-vous déjà entendu parler d'un attaquant brisant un algorithme de chiffrement AES 256 bits pour récupérer le secret caché à l'intérieur ? Aucun que je connaisse. (Bien sûr, si vous utilisez un protocole cryptographique obsolète vulnérable comme [DES](https://en.wikipedia.org/wiki/Data_Encryption_Standard) ou [RC4](http://www.securityweek.com/new-attack-rc4-based-ssltls-leverages-13-year-old-vulnerability), la cryptanalyse pourrait aider à briser le logiciel). Donc, si le coupable n'est pas la cryptanalyse, alors qu'est-ce que c'est ?

![Image](https://cdn-media-1.freecodecamp.org/images/aK1G79PpqMPtvs478FBokRR0Imh5j-1rDK3j)
_Votre sécurité n'est aussi bonne que son maillon le plus faible._

Eh bien, c'est tout sauf la cryptanalyse. En d'autres termes, la cryptanalyse n'est pas le maillon le plus faible des logiciels cryptographiques. Les mauvais acteurs utilisent de nombreux autres maillons faibles pour briser les logiciels cryptographiques.

### **Cause d'échec #1 : bugs dans les bibliothèques crypto**

Un exemple populaire est le bug Heartbleed.

![Image](https://cdn-media-1.freecodecamp.org/images/VwqT62a1y1lEhMiMcUkOwUnt7yaVV5a6pj5I)

Qu'est-ce qui ne va pas avec [Heartbleed](http://heartbleed.com/) ? Ce bug ([CVE-2014-0160](https://cve.mitre.org/cgi-bin/cvename.cgi?name=cve-2014-0160)) a été introduit en raison d'une implémentation incorrecte de l'extension TLS heartbeat dans OpenSSL (lire 66% de l'internet), qui est utilisé pour supporter TLS dans les serveurs web. Que fait cette extension ? Comme le suggère le nom, il s'agit d'une fonctionnalité de maintien en vie où une extrémité de la connexion envoie une charge utile de données arbitraires et l'autre extrémité est censée envoyer une copie exacte des données pour prouver que tout va bien.

Le bug s'est avéré être une vieille erreur de ne pas vérifier les limites avant `memcpy()` qui utilise des données non assainies. L'implémentation vulnérable d'OpenSSL [ne valide pas la longueur de la charge utile par rapport à la charge utile réelle](http://www.theregister.co.uk/2014/04/09/heartbleed_explained/). Un attaquant pourrait mentir sur la longueur et faire en sorte que la victime envoie plus d'octets depuis sa mémoire, comme le montre le diagramme suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/iukZ8VzrmG8b3MRRD6xad7xNMBJV186XrGzp)
_L'attaquant envoie une charge utile d'un seul octet mais définit la longueur à 65535 ; la victime copie aveuglément 65535 octets depuis sa mémoire et les renvoie à l'attaquant._

Cela a permis à l'attaquant d'obtenir des clés de session et d'autres informations secrètes (comme votre nom d'utilisateur et mot de passe) depuis n'importe quel site web actuellement dans la mémoire de votre navigateur.

Permettez-moi de vous montrer le code. Le correctif est essentiellement une vérification de limite ajoutée à la version corrigée 1.0.1g comme montré ci-dessous.

```
====== Code vulnérable =======/* Entrer le type de réponse, la longueur et copier la charge utile */*bp++ = TLS1_HB_RESPONSE;s2n(payload, bp);memcpy(bp, pl, payload);
```

```
====== Code corrigé =========hbtype = *p++;n2s(p, payload);if (1 + 2 + payload + 16 > s->s3->rrec.length)  return 0; /* ignorer silencieusement selon RFC 6520 sec. 4 */pl = p;
```

**Leçon apprise :** Toujours vérifier les limites de vos chaînes avant de les utiliser. L'assainissement est vital pour empêcher les mauvaises entrées de pénétrer dans votre système.

### **Cause d'échec #2 : systèmes d'exploitation et applications**

Vous vous souvenez probablement du bug "goto" d'Apple ([CVE-2014-1266](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-1266)) dans son implémentation SSL/TLS, divulgué en février 2014.

Le code d'Apple avec le bug "goto" :

```
1 static OSStatus2 SSLVerifySignedServerKeyExchange(SSLContext *ctx, bool isRsa,                                  SSLBuffer signedParams,3                       uint8_t *signature, UInt16 signatureLen)4 {5   OSStatus err;6 …78   if ((err = SSLHashSHA1.update(&hashCtx, &serverRandom)) != 0)9     goto fail;10  if ((err = SSLHashSHA1.update(&hashCtx, &signedParams)) != 0)11    goto fail;12    goto fail;13  if ((err = SSLHashSHA1.final(&hashCtx, &hashOut)) != 0)14    goto fail;15  …1617 fail:18   SSLFreeBuffer(&signedHashes);19   SSLFreeBuffer(&hashCtx);20   return err;21 }
```

Alors, quel est le problème ici ? L'instruction goto supplémentaire à la ligne 12 contourne toutes les vérifications de certificat pour les connexions SSL/TLS dans les appareils iOS et Mac. Cela rend les lignes 13 à 16 effectivement du code mort. Cette simple erreur d'implémentation accepte tout certificat invalide, rendant la connexion vulnérable aux attaques de type Man in the Middle.

J'étais curieux de savoir si les bugs d'implémentation dans les logiciels crypto sont plus dus à des bugs dans les bibliothèques crypto elles-mêmes qu'à la manière dont les applications les utilisent. Eh bien, [des chercheurs du MIT](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=0ahUKEwj--OSC7NrRAhXrJcAKHd2nDiEQFggbMAA&url=https%3A%2F%2Fpeople.csail.mit.edu%2Fnickolai%2Fpapers%2Flazar-cryptobugs.pdf&usg=AFQjCNGJvctaCQ8jDTUsZUgLX_AVl-LdKQ&sig2=P919CUo8W5fG7g7g1AroWQ) ont analysé 269 bugs cryptographiques signalés dans la base de données Common Vulnerabilities and Exposures entre janvier 2011 et mai 2014. Ils ont découvert que seulement 17 % des bugs sont causés par les bibliothèques crypto elles-mêmes. Les 83 % restants sont dus à une mauvaise utilisation des bibliothèques crypto par les développeurs d'applications.

Mais juste parce que la majorité des bugs sont dus à une mauvaise utilisation des bibliothèques crypto dans les applications, cela ne signifie pas que nous pouvons simplement blâmer les développeurs d'applications et continuer notre journée.

Il pourrait y avoir de nombreuses raisons derrière les statistiques ci-dessus sur la mauvaise utilisation de la crypto. Les bibliothèques crypto elles-mêmes peuvent ne pas fournir d'options par défaut sûres, peuvent ne pas avoir une documentation adéquate ou peuvent être difficiles à utiliser. De plus, de nombreux développeurs peuvent ne pas avoir une compréhension formelle de l'application de la cryptographie dans leurs logiciels, même s'ils sont experts en développement logiciel. Tout cela pourrait entraîner une mauvaise utilisation des bibliothèques crypto.

**Leçon apprise :** utilisez toujours des outils pour analyser votre code. Un outil d'analyse de code mort aurait dû détecter ce cas spécifique.

### **Cause d'échec #3 : mauvais design**

En 2015, des chercheurs ont découvert une série de problèmes dans les disques auto-chiffrants WD. Il y avait de graves défauts de conception dans leur utilisation des algorithmes cryptographiques. J'ai écrit à ce sujet dans un [précédent article](https://decentralize.today/encryption-is-useless-completely-useless-part-1-14a5e3bd069b#.h94ta28eu). Permettez-moi de montrer quelques défauts ici.

![Image](https://cdn-media-1.freecodecamp.org/images/ViJwzCkWz2D6nmxHoE4YQHOahxXMhkPzv-85)
_Architecture des disques auto-chiffrants WD_

Suivant les meilleures pratiques, WD a utilisé deux niveaux de clés pour chiffrer les documents stockés sur le disque — une clé principale KEK (Key Encryption Key) et une clé DEK (Data Encryption Key) par fichier. De plus, ils ont utilisé une fonction de dérivation de clé pour dériver les KEK à partir du mot de passe.

Mais la manière dont ils ont conçu la fonction de dérivation de clé elle-même était totalement non sécurisée. Ils ont utilisé un sel fixe et un nombre fixe d'itérations. Ainsi, elle était vulnérable aux attaques basées sur des tables de hachage pré-calculées. Les attaquants pouvaient récupérer les clés beaucoup plus rapidement qu'une attaque par force brute pure n'aurait pu le faire.

![Image](https://cdn-media-1.freecodecamp.org/images/xNOCC3T-Ejcup3h89XWOtgE103A8VD-2Hj3H)
_Algorithme de dérivation de clé vulnérable de WD_

Et si cette vulnérabilité n'était pas suffisante, WD a utilisé un générateur de nombres aléatoires médiocre pour générer les KEK. Il n'était pas seulement prévisible — il n'avait pas non plus assez de complexité (seulement 40 bits).

Les protocoles cryptographiques dépendent de manière critique des générateurs de nombres pseudo-aléatoires cryptographiquement sécurisés. Si ceux-ci ne sont pas suffisamment sécurisés, tout algorithme ou protocole cryptographique utilisant ces nombres aléatoires sera assez facile à briser.

![Image](https://cdn-media-1.freecodecamp.org/images/GrNo2Nf1RAlPVyTrANT0mmHLv9bAevCTSgAz)
_Générateur de nombres aléatoires faible de WD_

**Leçon apprise :** Ayez une bonne compréhension des constructions cryptographiques et connaissez leurs limitations. Suivez les meilleures pratiques de l'industrie pour la dérivation de clés.

### **Cause d'échec #4 : mauvaises configurations ou configurations par défaut non sécurisées**

![Image](https://cdn-media-1.freecodecamp.org/images/3-VGZNwxuYBBHi5dmH588z5M9lmD9YA9VlEb)
_Exploiter les faiblesses de SSLv2 ([source](https://drownattack.com/" rel="noopener" target="_blank" title="))_

L'[attaque DROWN](https://drownattack.com/drown-attack-paper.pdf) de rupture des connexions TLS via SSLv2 est un bon exemple de cela. Vous pouvez utiliser une connexion TLS assez sécurisée pour communiquer avec un serveur web, mais si le serveur web supporte toujours (ce qu'il ne devrait pas) l'ancien SSLv2, un attaquant peut l'exploiter pour briser la sécurité fournie par TLS et obtenir vos clés et autres informations sensibles.

SSLv2 est considéré depuis longtemps comme compromis, et aucun des clients aujourd'hui ne l'utilise pour des connexions sécurisées. Mais les chercheurs ont découvert que sur 36 millions de serveurs HTTPS qu'ils ont sondés, 6 millions (environ 17 %) supportaient encore SSLv2.

![Image](https://cdn-media-1.freecodecamp.org/images/DMIkoMXQS6V0KBwPI1whg2KPQTUkaFHYhADT)

La recherche ci-dessus révèle également une autre pratique paresseuse courante consistant à utiliser la même paire de clés sur différents serveurs d'une organisation. Elle montre comment même lorsqu'un serveur ne supporte que TLS, s'il y a d'autres serveurs supportant SSLv2 avec un certificat partagé, le serveur qui ne supporte que TLS est également vulnérable.

**Leçon apprise :** un système n'est aussi sécurisé que son maillon le plus faible. Essayez de protéger tous vos systèmes au moins de manière raisonnable.

### Il existe de nombreuses autres façons dont les logiciels cryptographiques peuvent échouer

Pouvez-vous penser à d'autres façons ?

Ils échouent à cause des utilisateurs. Comment ? Pensez aux attaques d'ingénierie sociale. [La violation de RSA SecureID est censée provenir de courriels de phishing exploitant les utilisateurs et une vulnérabilité zero-day](http://www.theregister.co.uk/2011/04/04/rsa_hack_howdunnit/).

Ils échouent à cause de modèles de menace irréalistes ([Casser les applications web construites sur des données chiffrées](https://eprint.iacr.org/2016/920.pdf)).

Ils échouent à cause du matériel ([Casser les technologies renforcées par le matériel telles que TPM avec des hyperviseurs](https://www.blackhat.com/docs/us-16/materials/us-16-Sharkey-Breaking-Hardware-Enforced-Security-With-Hypervisors.pdf)).

Ils échouent à cause des canaux auxiliaires ([Attaques par chronométrage sur les algorithmes RSA, DH et DSS](http://www.cryptography.com/resources/whitepapers/TimingAttacks.pdf)).

Comme vous pouvez le voir, les logiciels cryptographiques peuvent échouer pour de nombreuses raisons. Sommes-nous vraiment condamnés à ne jamais réussir les logiciels cryptographiques ? Ou pouvons-nous au moins réduire le nombre de ces échecs ? Pourquoi ne pouvons-nous pas apprendre du passé et éviter que les mêmes erreurs ne se reproduisent encore et encore ? Quels outils nous aideront à repérer la plupart de ces problèmes ?

Notre situation n'est en réalité pas si sombre. Il existe des moyens de prévenir la plupart des échecs discutés ci-dessus. Dans un prochain article, j'explorerai le sujet de la manière dont nous pouvons faire en sorte que les logiciels cryptographiques échouent moins souvent.

Merci d'avoir lu. Si vous avez trouvé cet article utile, cliquez sur le ? ci-dessous afin que d'autres puissent le voir sur Medium.

#### **Lectures complémentaires**

* [Aderson, Why cryptosystems fail, CCS 1993](http://Why Cryptosystems Fail - University of Cambridge Computer Laboratory)
* [Lazar et al., Why does cryptographic software fail? A case study and open problems, APSys, 2014](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwidioe4yOnRAhXIcBoKHYalBWAQFggbMAA&url=https%3A%2F%2Fpeople.csail.mit.edu%2Fnickolai%2Fpapers%2Flazar-cryptobugs.pdf&usg=AFQjCNGJvctaCQ8jDTUsZUgLX_AVl-LdKQ&sig2=jNxWe1fBL5LSymGIjNdhig)
* [Egele et al., An empirical study of cryptographic misuse in Android applications, CCS, 2013](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0ahUKEwi_093EyOnRAhXDQBoKHVyBDEkQFggnMAE&url=https%3A%2F%2Fcs.ucsb.edu%2F~chris%2Fresearch%2Fdoc%2Fccs13_cryptolint.pdf&usg=AFQjCNEmwGK1lobalVteyWAzgvzThSPafg&sig2=5eV_mxv-XvkdcjprP_7SMQ)