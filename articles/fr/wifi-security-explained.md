---
title: 'Clé WPA, WPA2, WPA3 et clé WEP : Explication de la sécurité Wi-Fi'
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2020-10-21T00:43:34.000Z'
originalURL: https://freecodecamp.org/news/wifi-security-explained
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/cover-4.png
tags:
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: Security
  slug: security
- name: wifi
  slug: wifi
seo_title: 'Clé WPA, WPA2, WPA3 et clé WEP : Explication de la sécurité Wi-Fi'
seo_desc: 'Setting up new Wi-Fi? Picking the type of password you need can seem like
  an arbitrary choice. After all, WEP, WPA, WPA2, and WPA3 all have mostly the same
  letters in them.

  A password is a password, so what’s the difference? About 60 seconds to billi...'
---

Configuration d'un nouveau Wi-Fi ? Choisir le type de mot de passe dont vous avez besoin peut sembler un choix arbitraire. Après tout, WEP, WPA, WPA2 et WPA3 ont tous à peu près les mêmes lettres.

Un mot de passe est un mot de passe, alors quelle est la différence ? Environ 60 secondes à des milliards d'années, comme il s'avère.

Toutes les cryptographies Wi-Fi ne sont pas créées égales. Explorons ce qui rend ces quatre acronymes si différents, et comment vous pouvez mieux protéger votre Wi-Fi à la maison et dans votre organisation.

## Wired Equivalent Privacy (WEP)

Au début, il y avait WEP.

![Illustration WEP](https://victoria.dev/blog/wpa-key-wpa2-wpa3-and-wep-key-wi-fi-security-explained/wep.png)

[Wired Equivalent Privacy](https://en.wikipedia.org/wiki/Wired_Equivalent_Privacy) est un algorithme de sécurité obsolète de 1997 qui était destiné à fournir une sécurité équivalente à une connexion filaire. "Obsolète" signifie, "Ne faisons plus cela."

Même lorsqu'il a été introduit pour la première fois, il était connu pour ne pas être aussi robuste qu'il aurait pu l'être, pour deux raisons :

* son mécanisme de cryptage sous-jacent, et
* la Seconde Guerre mondiale.

Pendant la Seconde Guerre mondiale, l'impact du décryptage (ou cryptanalyse) était [énorme](https://en.wikipedia.org/wiki/History_of_cryptography#World_War_II_cryptography). Les gouvernements ont réagi en tentant de garder leurs meilleures recettes secrètes à la maison.

Vers l'époque du WEP, les [restrictions du gouvernement américain sur l'exportation de la technologie cryptographique](https://en.wikipedia.org/wiki/Export_of_cryptography_from_the_United_States) ont amené les fabricants de points d'accès à limiter leurs appareils à un cryptage 64 bits. Bien que cela ait été porté plus tard à 128 bits, même cette forme de cryptage offrait une taille de clé possible très limitée.

Cela s'est avéré problématique pour le WEP. La petite taille de la clé a rendu plus facile le [forçage brutal](https://en.wikipedia.org/wiki/Brute-force_attack), surtout lorsque cette clé ne change pas souvent.

Le mécanisme de cryptage sous-jacent du WEP est le [chiffrement en flux RC4](https://en.wikipedia.org/wiki/RC4). Ce chiffrement a gagné en popularité grâce à sa vitesse et sa simplicité, mais cela avait un coût.

Ce n'est pas l'algorithme le plus robuste. Le WEP utilise une seule clé partagée parmi ses utilisateurs qui doit être saisie manuellement sur un appareil de point d'accès. (Quand avez-vous changé votre mot de passe Wi-Fi pour la dernière fois ? Exactement.)

Le WEP n'a pas aidé les choses non plus en concaténant simplement la clé avec le vecteur d'initialisation – ce qui signifie qu'il a simplement écrasé ses bits de sauce secrète ensemble et espéré le meilleur.

[Vecteur d'initialisation (IV)](https://en.wikipedia.org/wiki/Initialization_vector) : entrée de taille fixe dans un [algorithme cryptographique de bas niveau](https://en.wikipedia.org/wiki/Cryptographic_primitive), généralement aléatoire.

Combiné à l'utilisation de RC4, cela a rendu le WEP particulièrement vulnérable à l'[attaque par clé liée](https://en.wikipedia.org/wiki/Related-key_attack). Dans le cas du WEP 128 bits, votre mot de passe Wi-Fi peut être craqué par des outils publics en environ [60 secondes](https://shawnhogan.com/2006/08/how-to-crack-128-bit-wireless-networks.html) à [trois minutes](https://www.networkcomputing.com/wireless-infrastructure/fbi-teaches-lesson-how-break-wi-fi-networks).

Bien que certains appareils aient offert des variantes WEP 152 bits ou 256 bits, cela n'a pas réussi à résoudre les problèmes fondamentaux du mécanisme de cryptage sous-jacent du WEP.

Alors, oui. Ne faisons plus cela.

## Wi-Fi Protected Access (WPA)

![Illustration WPA](https://victoria.dev/blog/wpa-key-wpa2-wpa3-and-wep-key-wi-fi-security-explained/wpa.png)

Un nouveau standard intérimaire a cherché à "corriger" temporairement le problème de la (manque de) sécurité du WEP. Le nom [Wi-Fi Protected Access (WPA)](https://en.wikipedia.org/wiki/Wi-Fi_Protected_Access) sonne certainement plus sécurisé, donc c'est un bon début. Cependant, le WPA a d'abord commencé avec un autre nom, plus descriptif.

Ratifié dans un [standard IEEE 2004](https://en.wikipedia.org/wiki/IEEE_802.11i-2004), le [Temporal Key Integrity Protocol (TKIP)](https://en.wikipedia.org/wiki/Temporal_Key_Integrity_Protocol#Beck-Tews_attack) utilise une clé générée dynamiquement, par paquet. Chaque paquet envoyé a une clé temporelle unique de 128 bits, (Vous voyez ? Descriptif !) qui résout la susceptibilité aux attaques par clé liée causée par le mélange de clés partagées du WEP.

Le TKIP met également en œuvre d'autres mesures, telles qu'un [code d'authentification de message (MAC)](https://en.wikipedia.org/wiki/Message_authentication_code). Parfois appelé somme de contrôle, un MAC fournit un moyen cryptographique de vérifier que les messages n'ont pas été modifiés.

Dans le TKIP, un MAC invalide peut également déclencher un nouveau chiffrement de la clé de session. Si le point d'accès reçoit un MAC invalide deux fois en une minute, la tentative d'intrusion peut être contrée en changeant la clé qu'un attaquant essaie de craquer.

Malheureusement, afin de préserver la compatibilité avec le matériel existant que le WPA était censé "corriger", le TKIP a conservé l'utilisation du même mécanisme de cryptage sous-jacent que le WEP – le chiffrement en flux RC4.

Bien qu'il ait certainement amélioré les faiblesses du WEP, le TKIP s'est finalement avéré vulnérable à de nouvelles attaques qui [ont étendu les attaques précédentes sur le WEP](https://en.wikipedia.org/wiki/Temporal_Key_Integrity_Protocol#Security).

Ces attaques prennent un peu plus de temps à exécuter en comparaison : par exemple, [douze minutes](http://dl.aircrack-ng.org/breakingwepandwpa.pdf) dans le cas de l'une, et [52 heures](https://www.rc4nomore.com/) dans une autre. Cela est plus que suffisant, cependant, pour considérer le TKIP comme n'étant plus sécurisé.

Le WPA, ou TKIP, a depuis été également obsolète. Alors ne faisons plus cela non plus.

Ce qui nous amène à...

## Wi-Fi Protected Access II (WPA2)

![Illustration WPA2](https://victoria.dev/blog/wpa-key-wpa2-wpa3-and-wep-key-wi-fi-security-explained/wpa2.png)

Plutôt que de dépenser des efforts pour inventer un nom entièrement nouveau, le standard amélioré [Wi-Fi Protected Access II (WPA2)](https://en.wikipedia.org/wiki/Wi-Fi_Protected_Access#WPA2) se concentre plutôt sur l'utilisation d'un nouveau chiffrement sous-jacent.

Au lieu du chiffrement en flux RC4, le WPA2 utilise un chiffrement par blocs appelé [Advanced Encryption Standard (AES)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) pour former la base de son protocole de cryptage.

Le protocole lui-même, abrégé [CCMP](https://en.wikipedia.org/wiki/CCMP_(cryptography)), tire la plupart de sa sécurité de la longueur de son nom plutôt long (je plaisante) : Counter Mode Cipher Block Chaining Message Authentication Code Protocol, qui se raccourcit en Counter Mode CBC-MAC Protocol, ou CCM mode Protocol, ou CCMP. ?

Le [mode CCM](https://en.wikipedia.org/wiki/CCM_mode) est essentiellement une combinaison de quelques bonnes idées. Il fournit la confidentialité des données grâce au [mode CTR, ou mode compteur](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Counter_.28CTR.29). Pour simplifier à l'extrême, cela ajoute de la complexité aux données en texte clair en cryptant les valeurs successives d'une séquence de compte qui ne se répète pas.

Le CCM intègre également le [CBC-MAC](https://en.wikipedia.org/wiki/CBC-MAC), une méthode de chiffrement par blocs pour construire un MAC.

L'AES lui-même est sur de bonnes bases. La spécification AES a été établie en 2001 par le National Institute of Standards and Technology (NIST) des États-Unis. Ils ont fait leur choix après un processus de sélection compétitif de cinq ans au cours duquel quinze propositions de conceptions d'algorithmes ont été évaluées.

À la suite de ce processus, une famille de chiffrements appelée Rijndael (néerlandais) a été sélectionnée, et un sous-ensemble de ceux-ci est devenu l'AES.

Pendant la majeure partie de deux décennies, l'AES a été utilisé pour protéger le trafic Internet quotidien ainsi que [certains niveaux d'informations classifiées dans le gouvernement des États-Unis](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard#Security).

Bien que des [attaques possibles sur l'AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard#Known_attacks) aient été décrites, aucune n'a encore été prouvée comme étant pratique dans une utilisation réelle. L'attaque la plus rapide sur l'AES dans les connaissances publiques est une [attaque de récupération de clé](https://en.wikipedia.org/wiki/Key-recovery_attack) qui a amélioré le forçage brutal de l'AES d'un facteur d'environ quatre. Combien de temps cela prendrait-il ? Environ [des milliards d'années](https://web.archive.org/web/20150108165723/https://blog.agilebits.com/2011/08/18/aes-encryption-isnt-cracked/).

## Wi-Fi Protected Access III (WPA3)

![Illustration WPA3](https://victoria.dev/blog/wpa-key-wpa2-wpa3-and-wep-key-wi-fi-security-explained/wpa3.png)

La prochaine version de la trilogie WPA est [requise pour les nouveaux appareils](https://www.wi-fi.org/download.php?file=/sites/default/files/private/Certification_Overview_v5.2_0.pdf) depuis le 1er juillet 2020. Destiné à améliorer davantage la sécurité du WPA2, le [standard WPA3](https://www.wi-fi.org/news-events/newsroom/wi-fi-alliance-introduces-wi-fi-certified-wpa3-security) cherche à améliorer la sécurité des mots de passe en étant plus résistant aux attaques par liste de mots ou [attaques par dictionnaire](https://en.wikipedia.org/wiki/Dictionary_attack).

Contrairement à ses prédécesseurs, le WPA3 offrira également une [secret de transmission](https://en.wikipedia.org/wiki/Forward_secrecy). Cela ajoute l'avantage considérable de protéger les informations précédemment échangées même si une clé secrète à long terme est compromise.

Le secret de transmission est déjà fourni par des protocoles comme TLS en utilisant des clés asymétriques pour établir des clés partagées. Vous pouvez en apprendre [plus sur TLS dans cet article](https://www.freecodecamp.org/news/what-is-tls-transport-layer-security-encryption-explained-in-plain-english/).

Comme le WPA2 n'a pas été obsolète, le WPA2 et le WPA3 restent vos meilleurs choix pour la sécurité Wi-Fi.

## Si les autres ne sont pas bons, pourquoi sont-ils encore là ?

Vous vous demandez peut-être pourquoi votre point d'accès vous permet même de choisir une option autre que WPA2 ou WPA3. La raison probable est que vous utilisez du matériel hérité, c'est ce que les techniciens appellent le routeur de votre mère.

Puisque l'obsolescence du WEP et du WPA s'est produite plutôt récemment, il est possible dans les grandes organisations ainsi que chez vos parents de trouver du matériel plus ancien qui utilise encore ces protocoles. Même du matériel plus récent peut avoir un besoin commercial de supporter ces anciens protocoles.

Bien que je puisse vous convaincre d'investir dans un nouvel appareil Wi-Fi haut de gamme, la plupart des organisations sont une autre histoire. Malheureusement, beaucoup ne sont pas encore conscientes du rôle important que joue la cybersécurité dans la satisfaction des besoins des clients et l'augmentation de ce résultat net.

De plus, le passage à de nouveaux protocoles peut nécessiter du nouveau matériel interne ou des mises à jour de firmware. Surtout sur des systèmes complexes dans de grandes organisations, la mise à niveau des appareils peut être financièrement ou stratégiquement difficile.

## Améliorez votre sécurité Wi-Fi

Si c'est une option, choisissez WPA2 ou WPA3. La cybersécurité est un domaine qui évolue de jour en jour, et rester bloqué dans le passé peut avoir des conséquences désastreuses.

Si vous ne pouvez pas utiliser WPA2 ou WPA3, faites de votre mieux pour prendre des mesures de sécurité supplémentaires.

Le meilleur rapport qualité-prix est d'utiliser un réseau privé virtuel (VPN). Utiliser un VPN est une bonne idée quel que soit le type de cryptage Wi-Fi que vous avez. Sur un Wi-Fi ouvert (cafés) et en utilisant le WEP, il est tout simplement irresponsable de se passer d'un VPN.

C'est un peu comme crier vos coordonnées bancaires en commandant votre deuxième cappuccino.

![Une bande dessinée de crier vos coordonnées bancaires dans un café.](https://victoria.dev/blog/wpa-key-wpa2-wpa3-and-wep-key-wi-fi-security-explained/cafewifi.png)

Choisissez un fournisseur de VPN qui offre une fonctionnalité comme un interrupteur d'urgence qui bloque votre trafic réseau si votre VPN se déconnecte. Cela vous empêche de transmettre accidentellement des informations sur une connexion non sécurisée comme un Wi-Fi ouvert ou WEP. J'ai écrit plus sur mes trois principales considérations pour [choisir mon VPN dans cet article](https://victoria.dev/blog/vpn).

Lorsque cela est possible, assurez-vous de ne vous connecter qu'à des réseaux connus que vous ou votre organisation contrôlez.

De nombreuses attaques de cybersécurité sont exécutées lorsque les victimes se connectent à un point d'accès Wi-Fi public imité, également appelé attaque du jumeau maléfique, ou hameçonnage Wi-Fi.

Ces faux points d'accès sont facilement créés à l'aide de programmes et d'outils accessibles au public. Un VPN peut aider à atténuer les dommages causés par ces attaques, mais il est toujours préférable de ne pas prendre le risque.

Si vous voyagez souvent, envisagez d'acheter un point d'accès portable qui utilise un forfait de données cellulaires, ou d'utiliser des cartes SIM de données pour tous vos appareils.

## Bien plus que de simples acronymes

WEP, WPA, WPA2 et WPA3 signifient bien plus qu'un tas de lettres similaires – dans certains cas, c'est une différence de milliards d'années moins environ 60 secondes.

Sur une échelle de temps plus actuelle, j'espère vous avoir appris quelque chose de nouveau sur la sécurité de votre Wi-Fi et comment vous pouvez l'améliorer !

Si vous avez aimé cet article, j'adorerais le savoir. Rejoignez les milliers de personnes qui apprennent avec moi sur [victoria.dev](https://victoria.dev/) ! Visitez ou [abonnez-vous via RSS](https://victoria.dev/index.xml) pour plus de programmation, de cybersécurité et de blagues de papa en dessin animé.