---
title: Attaques courantes sur SSL/TLS – et comment protéger votre système
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-29T21:17:07.000Z'
originalURL: https://freecodecamp.org/news/attacks-on-ssl-tls-and-how-to-protect-your-system
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/cybersecurity-by-Christiaan-Colen-creative-commons-free-to-use.jpeg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
- name: SSL
  slug: ssl
- name: TLS
  slug: tls
seo_title: Attaques courantes sur SSL/TLS – et comment protéger votre système
seo_desc: 'By Megan Kaczanowski

  The SSL and TLS protocols are frequently attacked. And understanding past attacks
  can inform your knowledge as a defender and help you secure current systems. It
  can also help you predict the direction of future attacks.

  So here''...'
---

Par Megan Kaczanowski

Les protocoles SSL et TLS sont fréquemment attaqués. Et comprendre les attaques passées peut informer vos connaissances en tant que défenseur et vous aider à sécuriser les systèmes actuels. Cela peut également vous aider à prédire la direction des attaques futures.

Voici donc un résumé de certaines des attaques les plus célèbres ciblant ces protocoles :

## Exploit de navigateur contre SSL/TLS (BEAST) :

BEAST (divulgué en 2011) permettait à un attaquant de type "man-in-the-middle" de découvrir des informations chiffrées à partir d'une session SSL/TLS. Il a impacté SSL 3.0 et TLS 1.0.

Cette attaque dépendait de l'implémentation du chiffrement par blocs utilisé par TLS. L'implémentation utilisait le mode CBC (Cipher Block Chaining). Cela implique d'effectuer un XOR sur chaque bloc de texte en clair (sauf le premier) avec le bloc précédent de texte chiffré, puis d'utiliser l'algorithme de chiffrement sur le bloc.

Le premier bloc est XORé avec un IV (vecteur d'initialisation). Une grande partie de la sécurité du mode dépend du fait que l'IV soit vraiment aléatoire. Mais TLS 1.0 ne générait pas d'IV aléatoires – il utilisait simplement le dernier bloc de texte chiffré du message précédent. Cela signifiait que toute personne capable d'espionner le trafic chiffré avait une copie de l'IV.

Un attaquant capable d'espionner le trafic chiffré pouvait lancer une attaque à texte clair choisi en devinant un bloc de données, en effectuant un XOR avec l'IV (connu) et le bloc précédent de texte chiffré, et en injectant le bloc créé dans la session. Cela permettait à l'attaquant de vérifier si l'ensemble du bloc était correct.

Étant donné cela, la faille était considérée comme largement théorique jusqu'à la sortie de BEAST. BEAST a trouvé un moyen de décaler les limites des blocs de chiffrement pour isoler un octet d'un message à la fois jusqu'à ce qu'il ait été deviné.

Cela, et le fait que les messages HTTP sont généralement standardisés de sorte qu'un attaquant saurait où dans le message des informations sensibles (comme le cookie de session) étaient transmises, permettait à un attaquant de compromettre un cookie de session par force brute.

Bien que l'attaque soit théoriquement extrêmement intéressante et ait généré beaucoup d'intérêt, elle ne fonctionne que si l'attaquant peut insérer du code malveillant dans une page et violer la politique de même origine. Si l'attaquant avait un tel accès à votre système, il aurait également un certain nombre d'attaques qu'il pourrait tenter, dont beaucoup sont beaucoup moins compliquées à exécuter.

### Mesures d'atténuation pour les attaques SSL/TLS :

1. (Le plus sûr) N'autoriser que TLS 1.1 ou 1.2 car ils ont corrigé la vulnérabilité. Cependant, à l'époque, la plupart des sites web et des navigateurs ne supportaient pas TLS 1.1 ou 1.2.

2. Comme TLS supportait à la fois un chiffrement par blocs et un chiffrement par flux, basculer vers le chiffrement par flux (RC4). Cependant, en 2013, il a été démontré que RC4 était non sécurisé, et en 2015, il a été officiellement interdit (par l'Internet Engineering Task Force, ou IETF).

3. Utiliser un autre mode de chiffrement par blocs. Malheureusement, TLS 1.0 ne supportait aucun autre mode.

4. Insérer des paquets de longueur 0. Essentiellement, comme un paquet de longueur 0 serait complété à la taille du bloc, il devient un paquet de simple remplissage pour l'expéditeur, mais est immédiatement rejeté par le destinataire. Ces blocs seraient utilisés comme IV pour le message suivant, résolvant le problème des IV non sécurisés. Cette option était largement inutilisée car elle causait des problèmes d'interopérabilité avec certaines piles SSL, notamment Internet Explorer 6.0. OpenSSL a implémenté cela, mais l'a désactivé par défaut.

5. Pratiquer la défense en profondeur pour empêcher les attaquants d'obtenir un accès de type "man-in-the-middle" à un réseau victime.

### Sources/Informations complémentaires :

* [Comment fonctionne l'attaque BEAST](https://www.netsparker.com/blog/web-security/how-the-beast-attack-works/)

* [Un guide illustré de l'attaque BEAST](https://commandlinefanatic.com/cgi-bin/showarticle.cgi?article=art027)

* [Article original sur BEAST](https://vnhacker.blogspot.com/2011/09/beast.html)

* [Une étude complète de BEAST, CRIME, TIME, BREACH, LUCKY 13 et des biais RC4](https://www.nccgroup.com/us/our-research/attacks-on-ssl/)

## Vulnérabilité Heartbleed :

Heartbleed (introduite en 2012/divulguée en avril 2014) était une vulnérabilité dans l'extension heartbeat de la bibliothèque OpenSSL (utilisée pour maintenir une connexion ouverte).

Cette bibliothèque est largement utilisée pour les serveurs exécutant Apache et NGINX (au moment de la divulgation, environ 17 % des sites web "sécurisés" (utilisant SSL/TLS) de l'internet étaient vulnérables), mais elle a impacté tout serveur dépendant de la version vulnérable d'OpenSSL.

Essentiellement, le client envoie un message au serveur qui contient la réponse qu'il demande et la taille de la réponse. Le serveur répondrait avec les données demandées dans la taille demandée (voir ci-dessous pour une explication de xkcd).

![Image](https://megankaczanowski.com/content/images/2020/12/Screen-Shot-2020-12-29-at-4.16.21-PM.png align="left")

La vulnérabilité était que le serveur ne vérifiait pas que la demande était effectivement de la même taille que sa taille déclarée. Si l'utilisateur envoyait une réponse demandée (par exemple 'bird') qui était plus courte que la longueur demandée (500 lettres), le serveur 'compléterait' la réponse avec des données de sa mémoire pour répondre à l'exigence de longueur, potentiellement en divulguant des informations sensibles de la mémoire.

![Image](https://megankaczanowski.com/content/images/2020/12/Screen-Shot-2020-12-29-at-4.16.31-PM.png align="left")

![Image](https://megankaczanowski.com/content/images/2020/12/Screen-Shot-2020-12-29-at-4.16.38-PM.png align="left")

*https://xkcd.com/1354/*

Ces données divulguées seraient non chiffrées et pourraient contenir n'importe quoi – des identifiants sensibles, des documents, etc.

Mais pour exploiter avec succès ce bug, plusieurs choses devaient se produire : le site devait avoir implémenté SSL, il devait exécuter une version vulnérable d'OpenSSL (les versions vulnérables étaient entre 1.0.1 et 1.0.1f), l'attaquant devait avoir eu accès à l'environnement entre la découverte de l'existence du bug et sa correction, et il devait y avoir eu quelque chose d'utile en mémoire au moment où l'attaquant a mené l'attaque. Cela est relativement plus difficile, bien que loin d'être impossible.

Malheureusement, comme l'exploitation ne laisse aucune trace anormale dans les journaux, il est difficile de savoir si ou combien de fois ce bug a été réellement exploité.

De plus, cela ne tient pas compte du danger qu'un attaquant ait des pcaps précédents du trafic et récupère la clé privée du site lors d'une attaque. Cela signifie qu'ils auraient pu déchiffrer de grandes quantités de données sensibles, provoquant une grave violation.

Si des agences de renseignement étaient capables de mener ce type d'attaque, il est probable qu'elle ne serait jamais rendue publique.

### Mesures d'atténuation pour Heartbleed :

* Mettre à niveau OpenSSL vers la dernière version, corrigeant la vulnérabilité (les versions vulnérables étaient entre 1.0.1 et 1.0.1f).

### Sources/Lectures complémentaires :

* [5 ans plus tard, la vulnérabilité Heartbleed toujours non corrigée](https://blog.malwarebytes.com/exploits-and-vulnerabilities/2019/09/everything-you-need-to-know-about-the-heartbleed-vulnerability/)

* [XKCD Heartbleed](https://xkcd.com/1354/)

* [Tout ce que vous devez savoir sur le bug Heartbleed](https://www.troyhunt.com/everything-you-need-to-know-about3/)

## Padding Oracle On Downgraded Legacy Encryption (POODLE) :

POODLE (divulgué en septembre 2014) a exploité une faille dans SSL 3.0. Afin de supporter les systèmes hérités, certains systèmes continuaient à offrir un support pour SSL 3.0, même s'il avait été remplacé par des versions plus récentes.

Pour que l'attaque réussisse, l'attaquant devait être capable de contrôler des parties du côté client de la connexion SSL et devait avoir une visibilité du texte chiffré résultant (la manière la plus courante d'avoir cet accès est d'agir en tant qu'homme du milieu).

Cette attaque, bien que puissante, nécessite une attaque séparée pour obtenir cet accès.

Lors d'une négociation de poignée de main typique, le client et le serveur travaillent ensemble pour trouver un protocole qui fonctionne pour les deux afin de communiquer. Ils commencent par le protocole le plus élevé qu'ils offrent tous les deux et descendent (donc le client peut offrir TLS 1.2, et le serveur peut répondre avec TLS 1.1).

Mais si la connexion échoue (soit à cause d'un attaquant, soit à cause d'un problème de connexion réseau), le serveur client rétrograde vers le protocole le plus bas qu'ils offrent, probablement SSL 3.0. Il s'agit d'une 'fonctionnalité' offerte afin que les serveurs et les clients à différents stades d'avancement puissent communiquer.

SSL 3.0 utilise soit RC4 (chiffrement par flux), soit un chiffrement par blocs en mode CBC pour le chiffrement. RC4 était bien connu, même à l'époque, pour avoir un certain nombre de failles, y compris le fait que si le même secret (comme un cookie) était envoyé à plusieurs reprises, de plus en plus d'informations à son sujet seraient divulguées.

Le mode CBC nécessite que la longueur du message soit un multiple de la taille du bloc ou que du remplissage soit utilisé pour satisfaire la condition de longueur. Cela signifie que le remplissage est fréquemment utilisé, et dans l'implémentation SSL 3.0, il n'est pas vérifié qu'il n'a pas changé pendant le transit.

Essentiellement, bien que le message soit haché avant l'envoi et à l'extrémité de réception, et que le hachage recompilé soit comparé pour garantir l'intégrité du message, le remplissage n'est pas inclus.

La seule spécification pour le remplissage est que le dernier octet doit être la longueur du remplissage. Par conséquent, un attaquant peut remplacer le remplissage et il sera toujours accepté, tant qu'il obtient le dernier chiffre correct.

Si un attaquant connaît l'emplacement des données qu'il essaie de déchiffrer (par exemple un cookie de session HTTP, qui est généralement envoyé dans la même partie du bloc chaque fois et est donc facile à localiser), il peut le copier dans le bloc final, remplaçant le remplissage.

Ensuite, le destinataire effectuera un XOR sur le bloc rempli avec le texte chiffré du bloc précédent (que l'attaquant peut voir) et n'acceptera les données que si le dernier octet correspond à la longueur du remplissage.

Essentiellement, cette attaque rend le forçage brut de SSL réalisable. Alors qu'il serait pratiquement impossible de forcer brut SSL sans aucune information, cette attaque permet de récupérer chaque octet après un maximum de 256 tentatives par octet. Cela signifie que, en quelques minutes, un attaquant pourrait compromettre un cookie de session ou d'autres informations sensibles.

### Mesures d'atténuation pour POODLE :

* Désactiver SSL 3.0 est la seule mesure d'atténuation complète de POODLE. Cependant, certains sites ne supportaient que SSL 3.0.

* Une alternative est d'utiliser la suite de chiffrement TLS\_FALLBACK\_SCV. Cette suite permet à un serveur de revenir à des protocoles antérieurs, mais plutôt que de passer immédiatement à SSL 3.0, le client peut spécifier une préférence. Un problème avec cette suite est qu'elle n'était pas largement supportée lorsqu'elle a été introduite (limitée principalement aux services Google). De plus, si la seule option supportée par le serveur est SSL 3.0, les attaques POODLE sont toujours possibles. Cependant, cela signifie qu'un attaquant ne peut pas forcer une rétrogradation sur une connexion avec un serveur qui supporte des protocoles alternatifs.

* Pratiquer la défense en profondeur pour empêcher les attaquants d'obtenir un accès de type "man-in-the-middle" à un réseau victime. Bien que l'attaque soit dangereuse, elle nécessite un accès de type "man-in-the-middle", ce qui la rend beaucoup plus difficile à exploiter que Heartbleed, exploitable à distance.

### Sources/Informations complémentaires :

* [Tout ce que vous devez savoir sur le bug POODLE](https://www.troyhunt.com/everything-you-need-to-know-about/)

* [Ce POODLE mord : Exploiter la rétrogradation SSL 3.0](https://templatelab.com/ssl-poodle/)

* [Qu'est-ce que l'attaque POODLE ?](https://www.acunetix.com/blog/web-security-zone/what-is-poodle-attack/)

* [Vulnérabilité du protocole SSL 3.0 de la CISA](https://us-cert.cisa.gov/ncas/alerts/TA14-290A)

## Conclusion

Comprendre les attaques passées sur TLS et SSL peut à la fois informer vos connaissances en tant que défenseur et vous aider à sécuriser vos systèmes.

Souvent, les systèmes sont obsolètes, ou des applications héritées peuvent nécessiter l'utilisation de protocoles obsolètes. Cela signifie que même des attaques plus anciennes peuvent réussir si les défenses ne sont pas appliquées de manière appropriée.

Dans de nombreux cas, travailler dans la sécurité d'entreprise nécessite d'avoir suffisamment d'informations pour prendre des décisions et des recommandations éclairées. Si, par exemple, une application héritée nécessite l'utilisation d'un protocole obsolète, la connaissance d'attaques comme POODLE et Heartbleed peut vous aider à faire des recommandations efficaces sur la manière de sécuriser cette application, plutôt que de faire des recommandations générales comme 'mettre à jour vers un protocole plus récent' (ce qui pourrait être impossible).

Typiquement, en tant qu'analyste de sécurité, vous essayez d'équilibrer les besoins de l'entreprise avec les capacités techniques, et de faire des recommandations basées sur le niveau de risque de l'organisation. Cela pourrait signifier dire qu'une application héritée ne devrait plus être exécutée, ou cela pourrait signifier faire des recommandations sur la manière de sécuriser l'application autant que possible, étant donné qu'elle doit utiliser un protocole non sécurisé.

Comprendre les attaques passées sur TLS/SSL peut également vous aider à prédire la direction des attaques futures. Depuis Heartbleed et POODLE (en 2014), nous avons vu des attaques comme FREAK et Logjam en 2015 et Sweet32 en 2016. Nous verrons probablement continuer à voir des attaques supplémentaires.

Comprendre les fondamentaux de la manière dont TLS et SSL fonctionnent, et comment ils ont été attaqués dans le passé peut vous aider à prédire ou à comprendre les attaques futures.

Photo de couverture : "cybersecurity" par Christian Colen