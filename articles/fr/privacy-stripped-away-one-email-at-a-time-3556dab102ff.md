---
title: La vie privée supprimée, un email à la fois
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-01T12:25:52.000Z'
originalURL: https://freecodecamp.org/news/privacy-stripped-away-one-email-at-a-time-3556dab102ff
coverImage: https://cdn-media-1.freecodecamp.org/images/1*N05XSawg2UEm4CvdxD86CA.png
tags:
- name: politics
  slug: politics
- name: privacy
  slug: privacy
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: La vie privée supprimée, un email à la fois
seo_desc: 'By Chris Kubecka

  As the European Union General Data Protection Regulations (GDPR) looms, a privacy
  stripping email setting continues in widespread use around the world. It threatens
  sensitive communications that containing personally-identifiable inf...'
---

Par Chris Kubecka

Alors que le Règlement général sur la protection des données (GDPR) de l'Union européenne se profile, un paramètre d'email supprimant la vie privée continue d'être largement utilisé dans le monde. Il menace les communications sensibles contenant des informations personnelles identifiables, des propriétés intellectuelles, des informations financières et vos photos les plus intimes.

Vous pouvez vous connecter à un compte email pour l'utiliser, mais cela ne signifie pas que vos messages sont envoyés de manière sécurisée. Contrairement à l'assumption de confidentialité qu'un nom d'utilisateur et un mot de passe peuvent fournir, par défaut, les emails sont envoyés non chiffrés sauf s'ils sont explicitement ou opportunément sécurisés. Les normes technologiques des emails ont été écrites à une époque plus innocente, avant les graves préoccupations concernant la confidentialité.

La confidentialité des emails est devenue une préoccupation majeure pour le public de l'UE après les révélations de Prism. Soudain, le monde non technique de l'IT a commencé à comprendre à quel point le manque de chiffrement des emails pouvait être dommageable. Après les révélations de Snowden, des fournisseurs comme Gmail, Hotmail, des entreprises privées et bien d'autres ont décidé d'essayer de sécuriser les communications par email.

Configurer une sécurité explicite n'est pas facile. Cela nécessite une gestion des certificats et une surcharge.

La sécurité opportuniste peut aider à combler le vide. Chiffrez les emails partout où c'est possible, de manière opportuniste, avec un paramètre appelé Start-TLS. Cela chiffrera opportunément le contenu des emails pour empêcher l'écoute indiscrète. Le paramètre, appelé Start-TLS, peut fournir un niveau de base ou maintenir la protection de la confidentialité. Ce n'est pas une garantie, mais c'est utile, similaire au mouvement HTTPS Encrypt Everywhere.

D'un autre côté, il existe une configuration qui fait l'inverse, Strip-Start TLS. Ce paramètre de serveur email supprime tout chiffrement opportuniste des emails, les dépouillant, exposant le contenu de la conversation.

Pourquoi est-ce important ?

En 2014, l'[EFF](https://threatpost.com/eff-calls-out-isps-modifying-starttls-encryption-commands/109325/) a examiné un article de blog d'un ingénieur de Golden Frog VPN décrivant le problème. L'ingénieur ne pouvait plus envoyer et recevoir des emails chiffrés à un client parce qu'un fournisseur ISP avait appliqué le paramètre Strip Start-TLS. Laissant les communications exposées à l'écoute indiscrète. N'importe qui, outil de piratage, criminel, agence d'espionnage pourrait potentiellement lire les emails.

De [Wikipedia](https://en.wikipedia.org/wiki/Opportunistic_TLS) « Opportunistic TLS est un mécanisme de [chiffrement opportuniste](https://en.wikipedia.org/wiki/Opportunistic_encryption). Parce que la poignée de main initiale a lieu en texte clair, un attaquant contrôlant le réseau peut modifier les messages du serveur via une [attaque de l'homme du milieu](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) pour faire croire que TLS n'est pas disponible (appelé une **attaque STRIPTLS**). La plupart des clients SMTP enverront alors l'email et éventuellement les mots de passe en texte clair, souvent sans notification à l'utilisateur. En particulier, de nombreuses connexions SMTP se produisent entre serveurs de messagerie, où la notification à l'utilisateur n'est pas pratique. »

Si quelqu'un doute de la valeur des communications par email, ou si des programmes comme Prism existent. En élaborant un cours intensif de piratage OSINT pour Security BSides LV 2017, quatre sous-domaines liés à Prism de la NSA sont apparus en utilisant un outil de reconnaissance basé sur le web.

![Image](https://cdn-media-1.freecodecamp.org/images/gb0f-qtIJNK7YPLCefjPoMwg0afXeBWVZQHn)
_Figure 1 Liste mise en évidence des sous-domaines de la NSA listant Prism en juillet 2017_

Les choses ont-elles beaucoup changé ces dernières années ? Malheureusement, non.

Même avec les lois existantes sur la protection des données en Europe, aux États-Unis et dans d'autres pays concernés, la configuration Strip Start TLS est largement utilisée.

L'utilisation de ce paramètre sans notification pourrait être contraire au bouclier de confidentialité des données UE-États-Unis. Plusieurs partenaires de l'UE basés aux États-Unis, dans le cadre de nouveaux accords sur le bouclier de confidentialité UE-États-Unis, utilisent le déchiffrement opportuniste des emails.

Le paramètre anti-confidentialité des emails troublant peut être facilement trouvé. En utilisant les balises Censys.io et deux outils basés sur Python : ZMAP et StripTLS.

Censys.io est un projet de recherche en sécurité basé sur le web, exploité par l'Université du Michigan et basé sur ZMAP. Une simple recherche a donné 11 641 résultats en quelques secondes, affichant de nombreux fournisseurs d'accès Internet et fournisseurs de messagerie utilisant la balise Strip Start-TLS. La balise est appliquée à un appareil en fonction des métadonnées, de la technologie utilisée et du comportement des communications.

![Image](https://cdn-media-1.freecodecamp.org/images/UHVE5HubcmhtIxZaTise15vvA1kGbfKy1c4V)
_Figure 2 Analyse mondiale de Censys.io Strip Start-TLS le 10 novembre 2017_

Les États-Unis retournent le plus haut pourcentage de systèmes de stripping sur Internet — plus de six fois la quantité de la Chine.

Il existe un patchwork déroutant de lois sur la confidentialité des données au niveau fédéral et étatique aux États-Unis. Cependant, la loi fédérale sur la portabilité et la responsabilité de l'assurance maladie (HIPAA) couvre largement la confidentialité des données médicales via une règle de confidentialité et de sécurité.

Deuxième sur la liste se trouve le Royaume-Uni, avec d'autres pays européens à ses côtés.

![Image](https://cdn-media-1.freecodecamp.org/images/9vScZaI4wiGZYl3ZplzmZ-X0MnuFlYyQe-jd)
_Figure 3 Rapport des principaux pays de Censys.io Strip Start-TLS le 10 novembre 2017_

En se concentrant sur le contenu européen, plus de trois mille serveurs de stripping d'emails sont trouvés, résultant en trop de points de données pour tenir sur la carte.

En retirant la Russie de la liste et en regardant uniquement les emplacements de l'UE GDPR, les cinq premiers sont : le Royaume-Uni, la France, l'Italie, l'Allemagne et les Pays-Bas.

Certaines de ces zones ont des lois existantes sur la protection des données, qui couvrent les emails et légifèrent contre la collecte généralisée de données et de communications.

![Image](https://cdn-media-1.freecodecamp.org/images/lvWwy5JLqv1MBYCYL3gPGqvlEwDRAkjQ83F3)
_Figure 4 Analyse européenne de Censys.io Strip Start-TLS le 10 novembre 2017_

![Image](https://cdn-media-1.freecodecamp.org/images/raoHPyeH0A5sSVNeTmaP0K83YXzOdTqkCqQq)
_Figure 5 Rapport des principaux pays européens de Censys.io Strip Start-TLS le 10 novembre 2017_

Le Royaume-Uni a mis en œuvre sa version des règlements sur la confidentialité des données, complète avec un pouvoir de sanction majeur. Les contrevenants risquent des pénalités financières possibles.

Cachés derrière les fournisseurs d'accès Internet et les fournisseurs de centres de données du Royaume-Uni se trouvent des banques, des institutions financières comme Rabobank et Santander, une agence de voyage. Conseils gouvernementaux, hébergement et autres fournisseurs de services Internet comme 1stdomains.co.uk et 1stdnsltd.co.uk.

![Image](https://cdn-media-1.freecodecamp.org/images/gbMDW8Y6pfH9FdfU4nB-ds71Br0i0Xvd6lON)
_Figure 6 Rapport des principaux fournisseurs de réseau du Royaume-Uni de Censys.io Strip Start-TLS le 10 novembre 2017_

BT, d'autre part, semble posséder et héberger plusieurs systèmes de stripping, comme le gouvernement thaïlandais.

La plupart des fournisseurs d'accès Internet de la liste possèdent et hébergent des systèmes de stripping de la sécurité des emails. De nombreux fournisseurs d'accès Internet en France, en Allemagne et en Italie possèdent des systèmes de stripping des emails.

![Image](https://cdn-media-1.freecodecamp.org/images/X1SHyRpNnw9RtvemAZYRSvTVgXhtQrJpM5BV)
_Figure 7 Systèmes détenus par BT au Royaume-Uni de Censys.io Strip Start TLS le 15 novembre 2017_

![Image](https://cdn-media-1.freecodecamp.org/images/lAVMLL7neT4sELdX6yJhIGdZ5Vb0S4WVgmzC)
_Figure 8 Systèmes de télécommunications du gouvernement thaïlandais de Censys.io Strip Start-TLS le 15 novembre 2017_

Actuellement, j'utilise les Pays-Bas comme base d'opérations. En zoomant sur les résultats néerlandais, 174 systèmes, certains exploités par des fournisseurs d'accès Internet, des fournisseurs d'hébergement web et des organisations privées dans le pays.

![Image](https://cdn-media-1.freecodecamp.org/images/uFQrRsJeFIFUU-09gGU74BfBoYgCewMGLQRj)
_Figure 9 Rapport des principaux fournisseurs de réseau néerlandais de Censys.io Strip Start-TLS le 10 novembre 2017_

Similaire à la Thaïlande et à d'autres pays de l'UE en tête de la liste des balises, la plupart des fournisseurs d'accès Internet semblent posséder et héberger des systèmes autonomes qui suppriment le chiffrement opportuniste des emails. KPN possède plusieurs actifs combinés à une politique de peering qui stipule que les pairs de données avec KPN doivent également peer le trafic vers les États-Unis chaque fois que possible.

![Image](https://cdn-media-1.freecodecamp.org/images/6QsfpctExK3HCHTipMQWdTq003eglkfzh5SF)
_Figure 10 Systèmes détenus par KPN Static aux Pays-Bas de Censys.io Strip Start TLS le 15 novembre 2017_

L'un des piliers du GDPR de l'UE est le consentement et la conscience de ce qui se passe avec les données. Le chiffrement semble reculer, pas avancer. La quantité surprenante de ces systèmes de stripping de la confidentialité des emails sur les réseaux européens, les fournisseurs d'accès Internet, l'hébergement web, les organisations privées et les transits de réseau Internet est troublante pour les personnes soucieuses de la confidentialité.

La plupart des gens ne savent pas que la sécurité des emails peut être rétrogradée, ou que des emails précédemment sécurisés peuvent être exposés. Jusqu'à ce que les régulateurs de données de l'UE prennent conscience et répriment l'utilisation illégitime de Strip Start-TLS. Le GDPR de l'UE est impossible à mettre en œuvre si la rétrogradation de la confidentialité et de la sécurité dans l'UE est activement vaincue à travers l'Internet européen.

Voici quelques références et outils que j'ai utilisés dans cet article :

* [Censys.io](https://censys.io)
* [StripTLS](https://github.com/tintinweb/striptls) outil python par tintinweb
* [ZMAP.io](https://zmap.io)