---
title: Comment fonctionne l'appairage sécurisé Bluetooth LE ?
subtitle: ''
author: Nikheel Vishwas Savant
co_authors: []
series: null
date: '2025-09-14T07:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-does-bluetooth-le-secure-pairing-work
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1758637150173/ffd28cd9-88ac-4a9f-8e38-ec53bf18a388.png
tags:
- name: bluetooth
  slug: bluetooth
- name: handbook
  slug: handbook
seo_title: Comment fonctionne l'appairage sécurisé Bluetooth LE ?
seo_desc: 'The first time I tried to get a Bluetooth keyboard to connect to my laptop,
  it felt like the devices were having a private argument I wasn’t invited to. One
  second: “Pairing successful.” The next: “Connection failed.” No explanation, no
  apology. If y...'
---

La première fois que j'ai essayé de connecter un clavier Bluetooth à mon ordinateur portable, j'ai eu l'impression que les appareils avaient une dispute privée à laquelle je n'étais pas invité. Une seconde : « Appairage réussi ». La suivante : « Échec de la connexion ». Aucune explication, aucune excuse. Si vous vous êtes déjà demandé ce qui se passe réellement derrière cette roue qui tourne, vous n'êtes pas seul. Sous ce petit bouton « Appairer » se cache tout un rituel appelé l'appairage sécurisé LE (LE Secure Pairing), et c'est bien plus intéressant que ce que l'on pourrait croire.

## En résumé

L'appairage sécurisé Bluetooth LE est une courte cérémonie où deux inconnus deviennent des partenaires de confiance. D'abord, ils échangent leurs capacités, puis ils prouvent qu'ils partagent le même secret sans le prononcer à voix haute, et enfin ils se transmettent les clés à long terme qu'ils réutiliseront la prochaine fois. Le Gestionnaire de sécurité (Security Manager) dirige les opérations, L2CAP maintient le trafic dans des voies ordonnées, et AES-CMAC valide discrètement chaque étape. Des méthodes comme Just Works, Passkey Entry (Saisie de clé d'accès), Numeric Comparison (Comparaison numérique) et Out-of-Band (Hors-bande) sont choisies en fonction de ce que les appareils peuvent réellement faire, et non de ce que nous souhaiterions. Si vous voulez voir toute la danse, ouvrez une capture : les paquets s'alignent comme un dialogue — requête, réponse, confirmation, aléatoire, vérification, clés — et soudain, l'appairage cesse de ressembler à de la magie pour devenir une évidence.

## Dans ce guide, vous apprendrez

Vous ferez un tour d'horizon simple de la différence entre l'appairage (pairing) et la liaison (bonding), puis vous suivrez étape par étape comment les appareils LE négocient les fonctionnalités, créent un secret partagé et distribuent les bonnes clés pour des reconnexions rapides et sécurisées. Vous rencontrerez le Gestionnaire de sécurité et la couche L2CAP, verrez pourquoi différentes méthodes d'appairage apparaissent selon les situations, et comprendrez les petits assistants cryptographiques (f4, f5, f6, f7, g2, h6, h7) qui s'appuient sur AES-CMAC. Nous terminerons par une analyse Wireshark afin que vous puissiez faire correspondre chaque étape théorique aux paquets réels circulant sur le réseau.

## Table des matières

* [En résumé](#heading-en-resume)
    
* [Dans ce guide, vous apprendrez](#heading-dans-ce-guide-vous-apprendrez)
    
* [Appairage vs Liaison](#heading-appairage-vs-liaison)
    
* [Le Gestionnaire de sécurité (SM)](#heading-le-gestionnaire-de-securite-sm)
    
* [Couche L2CAP et canaux](#heading-couche-l2cap-et-canaux)
    
* [Méthodes d'appairage](#heading-methodes-dappairage)
    
* [Terminologies expliquées](#heading-terminologies-expliquees)
    
* [Les trois phases de l'appairage sécurisé LE](#heading-les-trois-phases-de-lappairage-securise-le)
    
* [Fonctions cryptographiques](#heading-fonctions-cryptographiques)
    
* [AES-CMAC : Le moteur de l'appairage sécurisé](#heading-aes-cmac-le-moteur-de-lappairage-securise)
    
* [Exemple Wireshark : Voir l'action en direct](#heading-exemple-wireshark-voir-laction-en-direct)
    
* [Conclusion](#heading-conclusion)
    

## Appairage vs Liaison

Voici une distinction qui m'a dérouté à mes débuts : l'appairage (pairing) versus la liaison (bonding). On dirait la même chose, n'est-ce pas ? Mais ça ne l'est pas. L'appairage est comme un premier rendez-vous — c'est cet échange initial, un peu maladroit, où les deux appareils disent : « Voici qui je suis, voici un secret que nous pouvons partager, essayons cela ». Une fois la soirée terminée, peut-être que vous ne vous reverrez plus jamais.

La liaison, en revanche, c'est quand vous décidez de sauvegarder vos numéros respectifs. Les appareils stockent les clés qu'ils ont échangées lors de l'appairage afin que, la prochaine fois qu'ils se rencontrent, ils n'aient pas besoin de repartir de zéro. C'est la différence entre se présenter à nouveau à chaque fête et entrer directement en disant : « Salut, la même chose que la dernière fois ? ».

## Le Gestionnaire de sécurité (SM)

![Relation entre le Gestionnaire de sécurité et le reste de l'architecture Bluetooth LE](https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-61/out/en/image/167f7fafea4f7b.png align="left")

Tout l'appairage et la liaison en BLE sont gérés par un protocole appelé le Gestionnaire de sécurité (Security Manager ou SM).

### Qu'est-ce que le Gestionnaire de sécurité ?

Si l'appairage Bluetooth était une pièce de théâtre, le Gestionnaire de sécurité en serait à la fois le metteur en scène et le script-boy. Rien ne se passe sur scène sans son approbation. Son rôle est de décider *comment* deux appareils vont s'accorder pour se faire confiance, et de s'assurer qu'ils suivent les règles sans sauter d'étape.

Mais qu'est-ce que cela signifie concrètement ? Le Gestionnaire de sécurité est un protocole intégré à la pile Bluetooth dont l'unique objectif est de gérer l'authentification, l'autorisation et la distribution des clés. Lorsque deux appareils se rencontrent pour la première fois, le SM prend le relais et pose une série de questions :

* Cet appareil nécessite-t-il une authentification, ou une simple poignée de main informelle suffit-elle ?
    
* L'appareil dispose-t-il d'un écran ou d'un clavier, ce qui permettrait des méthodes plus sécurisées comme la saisie de code d'accès (passkey) ?
    
* L'utilisateur se soucie-t-il de la protection contre les attaques de l'homme du milieu (man-in-the-middle), ou est-il acceptable de rester simple ?
    

Sur la base des réponses, il choisit la bonne méthode d'appairage. Si les deux appareils sont limités — par exemple, un capteur d'activité sans bouton et un smartphone — alors « Just Works » sera peut-être la seule option. Si au moins un appareil a des capacités d'entrée et de sortie, le SM peut passer à la « Numeric Comparison » ou à la « Passkey Entry », qui sont plus sûres.

![Échange de fonctionnalités d'appairage Bluetooth | Site web de la technologie Bluetooth®](https://www.bluetooth.com/wp-content/uploads/2016/03/screen-shot-03-25-16-at-0223-pm.png align="left")

Mais le Gestionnaire de sécurité ne s'arrête pas au choix de la méthode. Il gère également les clés elles-mêmes. Une fois que les appareils s'entendent sur un flux d'appairage, le SM supervise la génération de clés temporaires qui mèneront finalement à une clé à long terme (Long Term Key ou LTK). Cette clé devient la colonne vertébrale du chiffrement pour toutes les communications futures. Sans l'orchestration du SM, vous lanceriez pratiquement vos secrets en l'air en espérant que personne ne les attrape.

Un rôle souvent sous-estimé du SM est de s'assurer que les appareils ne font pas de fausses promesses. Par exemple, un gadget pourrait dire « Je supporte la saisie de code » — mais s'il n'a pas réellement de mécanisme d'entrée utilisable, le Gestionnaire de sécurité détectera ce décalage et s'adaptera en conséquence. C'est comme l'adulte dans la pièce qui s'assure que les enfants ne bluffent pas.

Voici la partie que je trouve fascinante : le SM est invisible pour nous en tant qu'utilisateurs. Nous ne voyons jamais de fenêtre contextuelle disant : « Au fait, le Gestionnaire de sécurité vient de choisir la comparaison numérique parce que votre ordinateur portable a un écran ». Tout se passe en arrière-plan, de sorte que lorsque nous cliquons sur « Appairer », le seul retour que nous recevons est le succès ou l'échec. Cette invisibilité est délibérée — le protocole est conçu pour éliminer les frictions. Mais cela signifie aussi que lorsque quelque chose *tourne mal*, on a l'impression que la magie cesse soudainement d'opérer.

Si l'on prend du recul, le Gestionnaire de sécurité est vraiment une question d'équilibre. Trop de friction — vous demander de taper des codes tout le temps — et les utilisateurs abandonneraient le Bluetooth par frustration. Trop peu de friction, et la sécurité s'effondre. Le SM marche sur cette corde raide, médiateur discret entre commodité et sécurité, prenant des décisions au nom de l'utilisateur et de l'appareil.

Et honnêtement, ce n'est pas parfait. Parfois, il fait des compromis que les puristes de la sécurité désapprouveraient (Just Works en est l'exemple évident). D'autres fois, il impose des méthodes qui semblent lourdes pour un utilisateur quotidien. Mais c'est le compromis inhérent au système : il ne cherche pas à vous offrir un secret de niveau militaire à chaque fois, il essaie de rendre l'utilisation quotidienne du Bluetooth à la fois pratique et suffisamment sûre.

## Couche L2CAP et canaux

![Génération et décodage de trames L2CAP Bluetooth LE - MATLAB & Simulink](https://www.mathworks.com/help/examples/bluetooth/win64/BLEL2CAPExample_01.png align="left")

Quand on parle de Bluetooth, on se concentre généralement sur les aspects visibles — écouteurs, montres connectées, autoradios. Mais en dessous se cache un système de plomberie qui maintient discrètement tout dans la bonne direction : L2CAP, ou Logical Link Control and Adaptation Protocol. Le nom peut paraître intimidant, mais dès que l'on visualise ce qu'il fait, il devient presque élégant.

Imaginez la communication Bluetooth comme une autoroute très fréquentée. Vous avez des camions transportant de lourdes charges (données audio), des motos se faufilant entre les files (petits messages de contrôle), et peut-être même un bus transportant des passagers (plusieurs applications utilisant la même connexion). Sans voies de circulation, cette autoroute serait un chaos — collisions partout, embouteillages, concert de klaxons. L2CAP est ce qui trace les lignes sur la route et dirige le trafic pour que chaque type de message sache exactement où aller.

Chaque canal dans L2CAP est comme une voie dédiée. Certains sont utilisés pour le protocole d'attributs (ATT), qui gère des opérations comme la lecture et l'écriture de caractéristiques d'un appareil Bluetooth. D'autres transportent des messages de sécurité — ce dont nous venons de parler avec l'appairage et le Gestionnaire de sécurité. D'autres encore sont réservés à des protocoles de plus haut niveau comme l'audio ou la vidéo. En donnant à chaque type de trafic son propre espace, L2CAP s'assure que votre flux de musique ne s'emmêle pas avec une mise à jour de firmware ou une notification de l'état de la batterie.

Voici un détail intéressant : L2CAP n'est pas seulement un agent de la circulation, c'est aussi un traducteur. Tous les appareils Bluetooth ne sont pas créés égaux — certains sont de minuscules capteurs envoyant quelques octets, d'autres sont des monstres audio diffusant des mégabits par seconde. L2CAP adapte les données des couches supérieures en une forme que la liaison radio de bas niveau peut gérer. Il découpe, réassemble et met en file d'attente les paquets pour qu'ils correspondent aux contraintes de la connexion physique. C'est comme une société de transport capable de gérer aussi bien des cartes postales que des conteneurs maritimes, en s'assurant qu'ils rentrent tous dans le même camion de livraison.

Et voici ce qui est intéressant pour les néophytes : vous ne « voyez » jamais L2CAP directement. Il n'y a pas « d'application L2CAP » sur votre téléphone. Mais chaque fois que vous connectez votre montre connectée et écoutez un podcast en même temps, L2CAP est en arrière-plan pour maintenir les deux conversations actives sans que l'une ne vienne gâcher la fête de l'autre. Sans lui, le Bluetooth donnerait l'impression d'essayer de parler à cinq personnes à la fois dans une pièce bondée sans aucune règle. Grâce à lui, chacun a son tour, et d'une manière ou d'une autre, tout fonctionne.

Le protocole permet même une fonctionnalité appelée CoC (Credit-Based Flow Control Channels), une façon élégante de dire que les appareils peuvent ouvrir des voies dynamiques spécifiques à une application selon les besoins. C'est comme si l'autoroute ajoutait magiquement une voie supplémentaire pendant l'heure de pointe. C'est pourquoi le Bluetooth moderne peut supporter des canaux de données personnalisés pour les applications tout en gérant les services de base de manière fluide.

Quand j'ai commencé à m'intéresser au L2CAP, cela ressemblait à l'un de ces acronymes que les ingénieurs utilisent pour avoir l'air intelligents. Mais quand j'ai réalisé que c'était la raison pour laquelle ma souris et mes écouteurs Bluetooth pouvaient coexister sur le même ordinateur sans se marcher sur les pieds, j'ai compris. Ce n'est pas glamour, mais c'est l'infrastructure silencieuse qui rend possibles toutes les expériences Bluetooth spectaculaires.

## Méthodes d'appairage

Si vous avez déjà appairé deux appareils Bluetooth et vous êtes demandé pourquoi on vous demande parfois de taper un code, alors que d'autres fois vous appuyez simplement sur « OK », ou que de temps en temps vous retenez votre souffle pendant que les deux écrans affichent le même nombre — ce n'est pas le fruit du hasard. Ce sont différentes méthodes d'appairage, et chacune a sa propre personnalité.

### Just Works

C'est la méthode la plus paresseuse (et la plus courante) de toutes. Comme son nom l'indique, « ça fonctionne, c'est tout ». Pas de codes, pas de confirmations, pas de drame. Deux appareils échangent une poignée de main et boum — ils sont connectés.

C'est fluide, mais il y a un piège : il n'y a aucune protection contre quelqu'un qui s'immiscerait dans cette poignée de main. C'est l'équivalent de laisser la porte de votre appartement déverrouillée parce que « franchement, qui va entrer ? ». C'est correct pour des gadgets sans importance, mais risqué si vous tenez à la sécurité.

### Passkey Entry (Saisie de clé d'accès)

La saisie de clé d'accès est plus stricte. Un appareil affiche un nombre à six chiffres, et vous le tapez sur l'autre. C'est comme vérifier la pièce d'identité de quelqu'un avant de le laisser entrer à la fête.

C'est ennuyeux si vous êtes pressé, mais bien plus sûr car un attaquant devrait deviner le code à six chiffres en temps réel, ce qui est improbable. Si vous avez déjà appairé un vieux clavier Bluetooth ou une Smart TV, vous avez probablement déjà tapé l'un de ces codes.

### Numeric Comparison (Comparaison numérique)

La comparaison numérique est le cousin moderne de la saisie de clé d'accès. Au lieu de taper quoi que ce soit, les deux appareils vous montrent le même nombre à six chiffres et vous demandent : « Est-ce que ça correspond ? ». Vous jetez un coup d'œil aux deux écrans, vous hochez la tête et vous appuyez sur « oui ».

C'est plus rapide, plus convivial, et cela bloque toujours les imposteurs. Imaginez rencontrer un ami dans une gare bondée et que vous portiez tous les deux le même chapeau ridicule dont vous aviez convenu — c'est une confirmation instantanée que vous avez trouvé la bonne personne.

### Out-of-Band (OOB - Hors-bande)

Et puis il y a l'Out-of-Band, le James Bond des méthodes d'appairage. Au lieu de crier des secrets via la liaison Bluetooth où n'importe qui pourrait écouter, les appareils utilisent un autre canal — le NFC est le plus populaire. Vous approchez votre téléphone d'une enceinte, la clé secrète transite par une voie privée, puis les appareils basculent sur le Bluetooth en sachant déjà qu'ils peuvent se faire confiance.

C'est élégant, sécurisé et un peu magique la première fois qu'on le voit. L'inconvénient est que tous les appareils n'ont pas de radio supplémentaire comme le NFC intégré, donc on ne rencontre pas l'OOB aussi souvent qu'on le souhaiterait.

Ce qui est fascinant, c'est la façon dont la méthode est choisie. Vous ne la choisissez généralement pas manuellement — le Gestionnaire de sécurité décide en fonction des capacités des appareils. Un capteur d'activité sans écran ne peut pas faire de comparaison numérique, il se replie donc sur « Just Works ». Un ordinateur portable et un smartphone, en revanche, peuvent facilement afficher des nombres correspondants. C'est comme deux personnes cherchant le meilleur moyen de communiquer : « Vous ne parlez pas français ? D'accord, parlons anglais ».

Chaque méthode a ses compromis. Just Works est fluide mais faible. Passkey Entry est sûr mais lourd. Numeric Comparison est le juste milieu idéal. Out-of-Band est sûr et transparent mais nécessite du matériel supplémentaire. Aucune n'est parfaite, mais ensemble, elles couvrent tout le spectre des appareils que nous utilisons réellement. Et honnêtement, c'est là tout le génie de l'appairage Bluetooth — il s'adapte juste assez à la situation, même si cela nous frustre occasionnellement avec un code à six chiffres de plus à taper.

## Terminologies expliquées

Avant de plonger dans les phases d'appairage, décortiquons certains termes que vous rencontrerez. Ces concepts constituent les briques de base de la sécurité Bluetooth LE.

### AES (Advanced Encryption Standard)

![Chiffrement AES : Qu'est-ce que c'est et comment protège-t-il vos données ?](https://content.nordlayer.com/uploads/How_encryption_works_1400x580_59f8b2cf11.webp align="left")

L'AES est l'algorithme de chiffrement qui travaille sous le capot. Vous lui donnez des données et une clé secrète, et il brouille les bits pour les rendre illisibles. Seul celui qui possède la même clé peut transformer ce bruit en information intelligible. En BLE, l'AES est le verrou sur la porte sur lequel tout le reste repose.

### CMAC (Cipher-based Message Authentication Code)

Le CMAC est la façon dont le Bluetooth signe ses messages. Imaginez sceller une enveloppe avec un tampon de cire que vous seul possédez ; si le tampon est incorrect, vous savez que la lettre a été altérée. Le CMAC ne chiffre pas le message — il prouve qu'il n'a pas été modifié et qu'il provient bien de l'expéditeur attendu.

### AES-CMAC

C'est simplement un CMAC construit à partir d'AES. Le Bluetooth réutilise cette primitive robuste pour confirmer des valeurs, dériver des clés et vérifier que les deux appareils ont calculé les mêmes secrets sans divulguer ces secrets à voix haute. C'est un couteau suisse ingénieux plutôt qu'un tiroir rempli d'outils disparates.

### Clé privée (Private Key)

Chaque appareil génère un immense nombre aléatoire et le garde pour lui. C'est la clé privée — jamais partagée, jamais montrée. C'est l'ingrédient qui permet à votre appareil de participer à l'échange de clés sans rien donner d'utile aux attaquants. Perdez-la, et vous perdez votre identité.

### Clé publique (Public Key)

À partir de la clé privée, un appareil dérive une clé partenaire qu'il peut partager en toute sécurité. Cette clé publique est diffusée pendant l'appairage afin que l'autre partie puisse effectuer les mêmes calculs de son côté. Tout le monde peut voir une clé publique ; personne ne peut l'utiliser pour usurper votre identité sans votre clé privée.

### ECDH (Elliptic Curve Diffie-Hellman)

![Analyse du protocole Elliptic Curve Diffie-Hellman](https://homecrew.dev/images/ecdh.png align="left")

L'ECDH est l'astuce utilisée par les deux appareils pour parvenir au même secret sans jamais envoyer ce secret par les ondes. Imaginez que vous et un ami mélangiez vos propres couleurs de peinture dans une même base — tout le monde voit la couleur finale, mais personne ne peut faire l'opération inverse pour deviner votre mélange exact. Ce résultat partagé devient le fondement du reste de l'appairage.

### Nonce

Un nonce est un nombre aléatoire utilisé une seule fois puis jeté. Chaque session d'appairage reçoit des nonces frais afin que d'anciens enregistrements ne puissent pas être rejoués pour tromper un appareil. Cela empêche la conversation d'aujourd'hui d'être confondue avec celle d'hier.

### LTK (Long Term Key - Clé à long terme)

Une fois la danse terminée, la LTK est la clé que les deux parties conservent pour les connexions futures. C'est la raison pour laquelle vos écouteurs se reconnectent instantanément sans renégocier depuis le début. Voyez cela comme le secret « à la prochaine fois » qui vous propulse directement dans un état sécurisé.

### IRK (Identity Resolving Key - Clé de résolution d'identité)

Pour protéger votre vie privée, de nombreux appareils BLE changent régulièrement leur adresse Bluetooth. L'IRK est la façon dont votre téléphone reconnaît toujours « son » appareil derrière ces masques changeants. Les étrangers voient du hasard ; votre partenaire lié peut discrètement mapper la nouvelle adresse à votre identité.

### CSRK (Connection Signature Resolving Key - Clé de résolution de signature de connexion)

Parfois, un minuscule capteur veut envoyer des données authentifiées sans activer le chiffrement complet de la liaison. La CSRK rend cela possible en permettant aux appareils de signer des paquets individuels afin que le récepteur puisse vérifier : « oui, cela vient bien de toi ». C'est une authenticité légère pour les gadgets bavards et à basse consommation.

## Les trois phases de l'appairage sécurisé LE

L'appairage en Bluetooth LE n'est pas une simple poignée de main. Il se déroule par étapes, et les schémas officiels utilisés par les ingénieurs pour le décrire montrent deux lignes de vie verticales (les appareils) avec des flèches allant et venant. À première vue, ces diagrammes ressemblent à un fouillis de termes cryptographiques, mais ils racontent simplement l'histoire de la façon dont deux étrangers deviennent des partenaires de confiance.

### **Phase 1 : Échange de fonctionnalités**

Dans les schémas, cette partie commence par des flèches étiquetées « Pairing Request » et « Pairing Response ». Un appareil se présente en envoyant des détails : « J'ai un écran », « Je n'ai pas de clavier », « Je souhaite une protection contre l'homme du milieu », « Je suis capable de distribuer ces clés ». L'autre appareil répond avec son propre profil.

En suivant ces flèches, vous regardez essentiellement les appareils négocier les règles du jeu. De cet échange découle le choix de la méthode d'appairage : Just Works, Numeric Comparison, Passkey ou Out-of-Band. Il décide également quelles clés seront transmises plus tard — comme l'IRK, la CSRK ou la LTK.

Visuellement, cette section du schéma est calme : quelques flèches croisées entre les appareils avec de petites notes sur les capacités. C'est l'étape « qui es-tu et que sais-tu faire ? ».

![Appairage initié par le Central](https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-61/out/en/image/167f7faff6e22b.png align="left")

### **Phase 2 : Génération de clés**

C'est ici que les flèches dans les schémas se multiplient soudainement — clés publiques, valeurs de confirmation (confirm), valeurs aléatoires (random). C'est le cœur de l'appairage, où les deux appareils passent des présentations à la preuve qu'ils peuvent réellement se faire confiance.

**Échange de clés publiques**  
Chaque appareil génère une paire de clés sur courbe elliptique (une clé privée et une clé publique). Ils envoient leurs moitiés publiques via la liaison, et à partir de ce moment, chaque côté peut calculer le même secret caché : la clé Diffie–Hellman (DHKey). Ce secret ne voyage jamais par les ondes, ce qui est tout l'intérêt — les deux appareils le dérivent indépendamment, et pourtant il correspond des deux côtés.

![Phase d'appairage 2 – Échange de clés publiques](https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-61/out/en/image/167f7faff8e6d3.png align="left")

**Valeurs de confirmation et aléatoires**  
Avant de révéler quoi que ce soit, chaque appareil génère un nonce aléatoire puis calcule une valeur de confirmation (essentiellement une somme de contrôle cryptographique) en utilisant ce nonce et la DHKey. Ils échangent d'abord les valeurs de confirmation. Ce n'est qu'ensuite qu'ils révèlent les nonces aléatoires. Une fois les nonces révélés, chaque appareil recalcule la valeur de confirmation et la compare à celle envoyée précédemment. Si elles correspondent, cela prouve qu'aucun des deux côtés ne bluffe et que tous deux ont réellement dérivé le même secret.

![Phase d'appairage 2, étape d'authentification 1, Comparaison Numérique réussie](https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-61/out/en/image/167f7faff955b1.png align="left")

**Fonctions de dérivation de clés**  
À ce stade, les deux appareils ont suffisamment d'éléments — la DHKey, les nonces aléatoires et certaines informations d'identité comme les adresses — pour passer par une série de fonctions basées sur AES (souvent étiquetées f5, f6, etc. dans les descriptions officielles). Ces fonctions génèrent des clés utilisables pour le chiffrement, l'identité et la signature. Selon que vous êtes en mode hérité (legacy) ou en mode connexions sécurisées, vous obtiendrez soit une clé à court terme (STK), soit directement une clé à long terme (LTK).

![Calcul de la clé à long terme](https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-61/out/en/image/167f7faffe707c.png align="left")

**Vérifications de la DHKey (DHKey Checks)**  
Voici le filet de sécurité supplémentaire. Dans les connexions sécurisées, après le calcul de la DHKey, les deux appareils effectuent ce qu'on appelle un « DHKey check ». Cela consiste à passer la DHKey dérivée, les nonces aléatoires et certaines données d'identité dans une autre fonction cryptographique. Chaque côté envoie le résultat à l'autre. Lorsqu'un appareil reçoit le contrôle DHKey de son partenaire, il recalcule la valeur attendue. Si les deux correspondent, c'est la preuve que les deux parties ont non seulement fait les calculs correctement, mais n'ont pas non plus été victimes d'une altération en cours de route.

![Phase d'appairage 2, étape d'authentification 2, vérifications DHKey](https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-61/out/en/image/167f7faffec8a1.png align="left")

Sur les schémas, vous verrez généralement cela sous forme de flèches étiquetées « DHKey Check » allant dans les deux directions, après l'échange des valeurs aléatoires. Sans cette étape, un attaquant pourrait être en mesure de tromper l'un des côtés en lui faisant croire qu'il possède un secret valide. Avec la vérification DHKey, les appareils verrouillent la certitude : soit nous avons tous les deux la même clé partagée, soit l'appairage échoue immédiatement.

Ainsi, la Phase 2 n'est pas qu'une seule étape. C'est une danse soigneusement chorégraphiée : échange de clés publiques, preuve par le calcul avec les valeurs de confirmation/aléatoires, dérivation de clés utilisables, puis double vérification de tout avec les contrôles DHKey. Ce n'est qu'après tout cela que les appareils se sentent suffisamment confiants pour passer au chiffrement et à la Phase 3.

### **Phase 3 : Distribution des clés**

Une fois le canal chiffré, les diagrammes montrent un nouvel ensemble de flèches avec des étiquettes comme « LTK », « IRK » et « CSRK ». C'est le moment où les appareils échangent les informations d'identification à long terme qui leur permettront de se reconnecter sans tout recommencer.

* La LTK permet de reprendre instantanément la communication chiffrée la prochaine fois.
    
* L'IRK permet à un partenaire de reconnaître un appareil même si son adresse Bluetooth change pour des raisons de confidentialité.
    
* La CSRK permet aux appareils de signer des messages individuels afin que l'autre partie soit sûre de leur authenticité.
    

Dans les schémas, cette partie vient toujours après un marqueur « Start Encryption » (Démarrer le chiffrement). C'est important — rien de sensible ne circule tant que le canal n'est pas déjà verrouillé. À partir de là, l'un ou les deux appareils remettent les clés, en fonction de ce qu'ils ont accepté de partager lors de la Phase 1.

Voyez cela comme si vous donniez à un ami de confiance non seulement la clé de votre maison, mais aussi le code de votre garage et peut-être celui de votre boîte aux lettres. Chaque information d'identification déverrouille une partie différente de votre relation, et parce qu'elles sont échangées de manière sécurisée, personne d'autre ne peut les copier.

![Distribution de clés spécifique au transport](https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-61/out/en/image/167f7fafff2255.png align="left")

## Fonctions cryptographiques

Les connexions sécurisées Bluetooth LE reposent sur une poignée de petits blocs de construction cryptographiques. Dans les diagrammes de flux officiels, vous verrez souvent des étiquettes comme f4 ou f6 attachées à des flèches ou des boîtes. Ce ne sont pas des noms aléatoires — ce sont les fonctions spécifiques basées sur AES définies pour l'appairage. Passons-les en revue une par une.

| **Fonction** | **Objectif** | **Étape d'utilisation** |
| --- | --- | --- |
| **f4** | Confirme les clés publiques | Phase 2 |
| **f5** | Dérive `MacKey` + `LTK` | Phase 2 |
| **f6** | Vérification de l'authentification | Phase 2 |
| **g2** | Valeur de comparaison numérique | Phase 2 |
| **h6** | Dérivation de clé héritée (STK) | Repli (fallback) hérité |
| **h7** | Dérivation de l'IRK | Phase 3 |

### `f4` : Confirmation de clé publique

```cpp
// f4 : confirmer l'échange de clés publiques
void f4(uint8_t *U, uint8_t *V, uint8_t *X, uint8_t Z, uint8_t *output) {
    uint8_t M[65];
    concat(M, U, V, X, Z);
    aes_cmac(U, M, sizeof(M), output);
}
```

Quand on regarde la fonction f4, elle prend quatre entrées : une clé U, une autre clé V, une valeur aléatoire X et une petite constante Z. U et V sont les clés publiques de courbe elliptique de 256 bits que les deux appareils ont échangées plus tôt dans le processus d'appairage. X est un nombre aléatoire fraîchement généré, unique à cette session, et Z est juste un discriminateur d'un octet pour éviter les collisions entre différentes utilisations de la même fonction. Le corps de f4 construit un message à partir de ces valeurs, puis le passe dans AES-CMAC en utilisant l'une des clés publiques comme clé CMAC. Le résultat est une valeur de confirmation. Cette valeur est envoyée avant que le X aléatoire ne soit révélé. Plus tard, quand X est envoyé, le partenaire peut recalculer f4 avec U, V, X et Z pour vérifier que la confirmation correspond, prouvant que l'expéditeur n'a pas changé son nombre aléatoire en cours de route.

### `f5` : Dérivation de MacKey + LTK

```cpp
void f5(uint8_t *W, uint8_t *N1, uint8_t *N2,
        uint8_t *A1, uint8_t *A2,
        uint8_t *MacKey, uint8_t *LTK) {
    uint8_t salt[16] = {0x6C,0x88,0x83,0xE6,0x93,0x04,0x4E,0xBF,
                        0x8C,0xD3,0x16,0xF0,0x2A,0xE0,0x8E,0xD3};
    uint8_t T[16];
    aes_cmac(salt, W, 32, T);

    aes_cmac(T, build_msg("btle", N1, N2, A1, A2, 0), 53, MacKey);
    aes_cmac(T, build_msg("btle", N1, N2, A1, A2, 1), 53, LTK);
}
```

La fonction f5 prend la clé brute Diffie–Hellman W, les deux nonces N1 et N2, ainsi que les deux adresses d'appareils A1 et A2. W est le grand secret partagé que les deux appareils ont dérivé de leur clé privée et de la clé publique de l'autre appareil, mais seul, il n'est pas assez structuré pour être utilisé directement. N1 et N2 sont les valeurs aléatoires choisies par chaque appareil pendant la session d'appairage, garantissant la fraîcheur. A1 et A2 sont les adresses Bluetooth de 48 bits de l'initiateur et du répondeur, incluses pour que les clés dérivées soient liées à ces appareils particuliers et non réutilisables ailleurs. La routine f5 dérive d'abord une clé temporaire à partir de W et d'un sel (salt) fixe, puis utilise AES-CMAC pour combiner les nonces et les adresses. Les sorties sont deux valeurs : MacKey, qui sera utilisée pour authentifier les contrôles DHKey, et la Long Term Key (LTK), qui chiffrera ultérieurement la liaison.

### `f6` : Vérification de l'authentification

```cpp
void f6(uint8_t *MacKey,
        uint8_t *N1, uint8_t *N2,
        uint8_t *R, uint8_t *IOcap,
        uint8_t *A1, uint8_t *A2,
        uint8_t *output) {
    uint8_t M[128];
    concat(M, N1, N2, R, IOcap, A1, A2);
    aes_cmac(MacKey, M, sizeof(M), output);
}
```

La fonction f6 accepte la MacKey ainsi que N1, N2, A1, A2, et une entrée appelée r, qui peut être soit le code d'accès à six chiffres dans Passkey Entry, soit une valeur zéro dans Numeric Comparison. Elle utilise également IOcap, qui encode le type d'entrée et de sortie dont dispose chaque appareil. Ensemble, ces entrées capturent le caractère aléatoire de la session, l'identité des appareils et les valeurs de confirmation au niveau humain. Le calcul AES-CMAC sur ces paramètres produit une valeur d'authentification. C'est cette valeur que chaque côté envoie comme vérification DHKey (DHKey check). Si les deux côtés calculent la même valeur, cela signifie que les entrées d'appairage et la clé partagée correspondent, et que personne ne s'est interposé.

### `g2` : Comparaison numérique (Numeric Comparison)

```cpp
uint32_t g2(uint8_t *U, uint8_t *V,
            uint8_t *X, uint8_t *Y) {
    uint8_t M[128];
    concat(M, U, V, Y, X);
    uint8_t out[16];
    aes_cmac(X, M, sizeof(M), out);

    return (out[0] | (out[1] << 8) | (out[2] << 16)) % 1000000;
}
```

La fonction g2 utilise à nouveau les clés publiques U et V, ainsi que les nonces X et Y des deux appareils. Son rôle est de produire le nombre à six chiffres que les humains comparent lors d'un appairage par comparaison numérique. Elle exécute AES-CMAC sur ces entrées, puis réduit la sortie à un nombre compris entre 000000 et 999999. Chaque appareil calcule le même nombre indépendamment, et l'utilisateur vérifie simplement que les deux écrans affichent la même chose. Les paramètres sont soigneusement choisis : U et V prouvent que les appareils sont bien ceux qui ont échangé les clés, tandis que X et Y assurent la fraîcheur spécifique à la session.

### `h6` : Dérivation de clé héritée (Legacy Key Derivation)

```cpp
void h6(uint8_t *W, const char *keyID, uint8_t *output) {
    aes_cmac(W, keyID, 4, output);
}
```

La fonction h6 prend une clé W et une courte chaîne d'identifiant. W peut être une clé de liaison (Link Key) héritée ou un autre secret préexistant, et la chaîne d'identifiant indique à h6 à quoi sert la nouvelle clé. La fonction exécute simplement AES-CMAC de l'identifiant en utilisant W comme clé. Le résultat est une clé dérivée prête à être utilisée dans des connexions sécurisées, adaptant ainsi efficacement une ancienne clé à un nouveau rôle.

### `h7` : Dérivation de l'IRK

```cpp
void h7(uint8_t *Salt, uint8_t *W, uint8_t *output) {
    aes_cmac(Salt, W, 16, output);
}
```

La fonction h7 est similaire, mais au lieu d'une chaîne d'identifiant, elle utilise un sel (salt). Elle prend W, souvent la DHKey, et exécute AES-CMAC avec le sel comme message. Le résultat est une nouvelle clé, généralement l'IRK qui permet à un appareil d'en résoudre un autre malgré ses changements d'adresses. L'utilisation d'un sel garantit que cette clé est différente des autres dérivées du même W, empêchant toute réutilisation accidentelle.

## AES-CMAC : Le moteur de l'appairage sécurisé

Au centre de toutes ces fonctions cryptographiques auxiliaires se trouve AES-CMAC. C'est le couteau suisse que l'appairage sécurisé Bluetooth LE utilise encore et encore pour prouver l'honnêteté, dériver de nouvelles clés et générer des valeurs d'authentification. Chaque fois que vous voyez f4, f5, f6, g2, h6 ou h7 dans le code, il s'agit en réalité de simples enveloppes intelligentes autour de AES-CMAC avec des entrées légèrement différentes.

### Pseudocode pour AES-CMAC

```c
#include <stdint.h>
#include <string.h>
#include "aes.h"   // Routine de chiffrement AES-128

#define BLOCK_SIZE 16

// Assistant de décalage à gauche
void leftshift(uint8_t *input, uint8_t *output) {
    uint8_t carry = 0;
    for (int i = BLOCK_SIZE-1; i >= 0; i--) {
        uint8_t val = input[i];
        output[i] = (val << 1) | carry;
        carry = (val & 0x80) ? 1 : 0;
    }
}

// Assistant XOR
void xor128(uint8_t *a, uint8_t *b, uint8_t *out) {
    for (int i = 0; i < BLOCK_SIZE; i++) out[i] = a[i] ^ b[i];
}

// Implémentation AES-CMAC
void aes_cmac(uint8_t *key, uint8_t *msg, size_t len, uint8_t *mac) {
    uint8_t L[BLOCK_SIZE], K1[BLOCK_SIZE], K2[BLOCK_SIZE];
    uint8_t zero[BLOCK_SIZE] = {0};

    // Étape 1 : Chiffrer AES 0 avec la clé
    aes_encrypt_block(key, zero, L);

    // Étape 2 : Générer les sous-clés
    leftshift(L, K1);
    if (L[0] & 0x80) K1[BLOCK_SIZE-1] ^= 0x87; // Constante Rb
    leftshift(K1, K2);
    if (K1[0] & 0x80) K2[BLOCK_SIZE-1] ^= 0x87;

    // Étape 3 : Diviser le message en blocs
    size_t n = (len + BLOCK_SIZE - 1) / BLOCK_SIZE;
    uint8_t last_block[BLOCK_SIZE];
    bool complete = (len % BLOCK_SIZE == 0);

    // Préparer le dernier bloc
    if (complete && n > 0) {
        xor128(&msg[(n-1)*BLOCK_SIZE], K1, last_block);
    } else {
        memset(last_block, 0, BLOCK_SIZE);
        memcpy(last_block, &msg[(n-1)*BLOCK_SIZE], len % BLOCK_SIZE);
        last_block[len % BLOCK_SIZE] = 0x80; // remplissage (padding)
        xor128(last_block, K2, last_block);
    }

    // Étape 4 : CBC-MAC sur tous les blocs
    uint8_t X[BLOCK_SIZE] = {0};
    uint8_t Y[BLOCK_SIZE];
    for (int i = 0; i < n-1; i++) {
        xor128(X, &msg[i*BLOCK_SIZE], Y);
        aes_encrypt_block(key, Y, X);
    }

    // Étape 5 : Traiter le dernier bloc
    xor128(X, last_block, Y);
    aes_encrypt_block(key, Y, mac);
}
```

L'algorithme lui-même prend deux éléments : une clé et un message. La clé est généralement quelque chose de significatif dans la session, comme une clé publique, le secret partagé Diffie–Hellman ou une MacKey précédemment dérivée. Le message est construit en concaténant des paramètres de session tels que des nonces aléatoires, des adresses d'appareils ou des identifiants de rôle. Le but est toujours le même : combiner ces valeurs en une courte étiquette (tag) qui prouve que les deux parties disposaient des mêmes entrées sans exposer les entrées elles-mêmes.

Le processus commence par l'exécution d'AES une fois sur un bloc composé uniquement de zéros en utilisant la clé fournie. Le résultat, appelé L, est utilisé pour générer deux sous-clés spéciales, K1 et K2. Cette étape est subtile mais cruciale. Tous les messages n'ont pas la même longueur, et le dernier bloc peut être parfaitement plein ou nécessiter un remplissage (padding). En préparant deux sous-clés à l'avance, AES-CMAC sait exactement comment traiter le bloc final. Si le dernier bloc est complet, on applique un XOR avec K1. S'il est incomplet, le bloc est rempli avec un seul octet 0x80 suivi de zéros, puis on applique un XOR avec K2. Cette astuce garantit qu'un message avec remplissage ne collisionne jamais avec un message sans remplissage.

Une fois le message divisé en morceaux de 16 octets, l'algorithme adopte un rythme régulier. Il prend le premier bloc, effectue un XOR avec un état initial (tout à zéro au début), puis le chiffre avec AES sous la clé. Le résultat devient le nouvel état. Le bloc suivant subit un XOR avec cet état et est à nouveau chiffré. Ce chaînage se poursuit jusqu'au dernier bloc, qui est traité avec K1 ou K2 selon que le remplissage était nécessaire ou non. Après le chiffrement final, l'état qui en ressort est l'étiquette CMAC.

Les paramètres du code prennent tout leur sens lorsqu'on les rapporte à ce flux. Le paramètre « key » est la clé AES choisie pour ce tour, qui peut être la clé publique dans f4, la DHKey dans f5 ou la MacKey dans f6. Le paramètre « message » correspond aux entrées pertinentes à cette étape — parfois une concaténation de nonces et d'adresses, parfois une courte chaîne d'identifiant, parfois les deux clés publiques plus une valeur aléatoire. Ensemble, ils capturent l'identité de cette session et de cet usage particulier. La sortie de AES-CMAC est toujours une valeur de 128 bits, mais des fonctions comme g2 la réduisent à six chiffres pour la lisibilité humaine.

De l'extérieur, cela ressemble à de la cryptographie de type « boîte noire », mais en pratique, AES-CMAC n'est qu'une manière disciplinée de plier ensemble une clé et un message jusqu'à obtenir une étiquette unique. Les deux appareils exécutent exactement les mêmes étapes avec exactement les mêmes entrées, de sorte qu'ils produiront la même étiquette si et seulement s'ils partageaient réellement les mêmes secrets de départ. C'est pourquoi cela fonctionne si bien comme fondation : c'est déterministe, résistant à l'altération et suffisamment polyvalent pour servir de générateur de valeur de confirmation, de fonction de dérivation de clé, d'assistant de comparaison numérique et d'adaptateur pour les clés héritées.

Ainsi, lorsque vous voyez un diagramme d'appairage rempli de flèches étiquetées Confirm, Random, DHKey Check ou distribution d'IRK, sachez qu'en coulisses, la plupart de ces flèches sont nées de AES-CMAC. C'est le moteur silencieux qui prend un méli-mélo de clés publiques, de nombres aléatoires et d'adresses pour les presser en une preuve de confiance compacte. Sans AES-CMAC, tout le flux d'appairage sécurisé ne tiendrait pas debout.

## Exemple Wireshark : Voir l'action en direct

Si vous capturez une connexion BLE avec Wireshark (ou en utilisant les journaux de snoop HCI Android/iOS), vous verrez ces messages du protocole de gestionnaire de sécurité (Security Manager Protocol ou SMP) transiter sur le canal L2CAP 0x0006. Parcourons une trace réelle et relions chaque paquet aux phases d'appairage et aux fonctions cryptographiques.

### 1. Pairing Request

```bash
> SMP Pairing Request
    IO Capability: DisplayYes
    OOB data: Not present
    AuthenticationReq: Bonding, MITM
    Max Encryption Key Size: 16
    Initiator Key Distribution: LTK, IRK
```

La trace commence généralement par une trame étiquetée « Pairing Request ». C'est le moment où un appareil se présente formellement. À l'intérieur du paquet, vous pouvez voir ses capacités d'E/S (IO), comme s'il dispose d'un écran ou d'un clavier, s'il prend en charge les données hors-bande (OOB), et s'il exige une protection renforcée contre les attaques de l'homme du milieu. Il annonce également les clés qu'il est prêt à distribuer plus tard, comme la LTK, l'IRK ou la CSRK. À partir de cette seule trame, vous pouvez déjà en apprendre beaucoup sur ce que l'appareil peut faire et quelles méthodes d'appairage sont envisageables.

### 2. Pairing Response

```bash
< SMP Pairing Response
    IO Capability: KeyboardOnly
    OOB data: Not present
    AuthenticationReq: Bonding, MITM
    Max Encryption Key Size: 16
    Responder Key Distribution: LTK
```

Peu après, le partenaire envoie une « Pairing Response ». Ce paquet est le miroir du premier, contenant ses propres capacités d'E/S, ses exigences de sécurité et sa distribution de clés prévue. En examinant la requête et la réponse ensemble, vous pouvez déduire quelle méthode d'appairage sera sélectionnée. Par exemple, si un côté n'a pas d'écran et l'autre n'a pas de clavier, les appareils se replieront sur « Just Works ». Si les deux peuvent afficher des nombres, la comparaison numérique devient une option. Cet échange est l'étape de négociation qui verrouille le déroulement de la suite.

### 3. Pairing Confirm (utilise `f4`)

```bash
> SMP Pairing Confirm
    Confirm Value: 0x9f3c2a5e...
```

Ensuite, vous verrez des paquets « Pairing Confirm » circuler sur la liaison. Ce sont les valeurs de confirmation générées par la fonction f4. Elles ne font que 16 octets et, seules, ressemblent à des données aléatoires. Mais en coulisses, elles lient la clé publique de l'appareil et son nombre aléatoire d'une manière que le partenaire pourra vérifier plus tard. À ce stade, aucun des deux appareils ne révèle encore son nombre aléatoire — la confirmation est comme sceller une réponse dans une enveloppe et la passer de l'autre côté de la table.

### 4. Pairing Random

```bash
> SMP Pairing Random
    Random Value: 0x82b14e6d...
```

Après les confirmations viennent les paquets « Pairing Random ». Chaque appareil révèle maintenant le nombre aléatoire qu'il a utilisé précédemment. Lorsqu'un côté reçoit le nombre aléatoire de l'autre, il le réinjecte dans f4 avec les clés publiques connues. Si le résultat correspond à la valeur de confirmation déjà envoyée, le contrôle est réussi. Sinon, l'appairage échoue ici même. Observer cela dans Wireshark est satisfaisant, car on voit les paires de paquets Confirm et Random s'aligner proprement en séquence.

### 5. Public Key Exchange

```bash
> SMP Pairing Public Key
    X: 0x04A1F...
    Y: 0x7B9D2...
```

Maintenant, vous verrez des trames « Pairing Public Key » dans les deux directions. Chaque appareil envoie sa clé publique de courbe elliptique, que Wireshark affiche sous forme de deux coordonnées de 256 bits. Ces valeurs ressemblent à de gros blocs hexadécimaux, mais ce sont les ingrédients dont chaque côté a besoin pour calculer localement le même secret Diffie–Hellman. Vous remarquerez peut-être des retransmissions si la liaison est parasitée, mais une fois les deux clés échangées, les appareils ont tout le nécessaire pour passer aux étapes de confirmation et d'aléatoire. Dans les connexions sécurisées, cet échange est obligatoire ; dans les flux hérités plus anciens, vous ne verrez pas ces paquets.

### 6. DHKey Check (utilise `f6`)

```bash
> SMP DHKey Check
    Check Value: 0xF12C...
```

Si les connexions sécurisées sont utilisées, l'étape suivante dans la trace est le « DHKey Check ». Ces messages proviennent de la fonction f6, qui combine le secret Diffie–Hellman, les valeurs aléatoires et les identités des appareils. Chaque côté calcule un contrôle DHKey et l'envoie. L'autre côté recalcule la même fonction et s'assure que les valeurs correspondent. Cette étape garantit que les deux parties ont non seulement dérivé le même secret partagé, mais aussi que rien n'a été altéré. Dans Wireshark, vous verrez deux trames DHKey Check échangées consécutivement.

### 7. Encryption Information

```bash
> HCI LE Start Encryption
    Rand: 0x123456...
    EDIV: 0x5678
    LTK:  0x89abcdef...
```

Une fois les vérifications réussies, le chiffrement commence et vous verrez « Encryption Information » suivi de « Master Identification » dans la liaison de style hérité. Le premier transporte le matériel de chiffrement à long terme, et le second inclut les valeurs nécessaires pour les reconnexions rapides futures. À ce stade, le contenu des paquets est chiffré dans la capture, sauf si vous avez fourni les clés à Wireshark.

### 8. Identity Information et Identity Address Information

Si l'échange d'identité a été convenu précédemment, ces messages apparaissent ensuite. « Identity Information » transporte la clé utilisée pour résoudre les adresses privées ultérieurement, et « Identity Address Information » fournit l'adresse d'identité de l'appareil. Ensemble, ils permettent à un partenaire de reconnaître l'appareil même lorsque son adresse Bluetooth change pour préserver sa confidentialité.

### 9. Signing Information

Certaines captures se terminent par « Signing Information ». Cela livre la clé utilisée pour signer les paquets de données afin qu'un appareil puisse prouver son identité sans activer le chiffrement complet à chaque fois, ce qui est pratique pour les capteurs à très faible consommation. Ce paquet conclut la distribution des clés et achève l'histoire de l'appairage que vous pouvez observer dans la trace.

## Conclusion

Si vous êtes arrivé jusqu'ici, vous pouvez probablement maintenant ressentir le rythme de l'appairage. Ce n'est plus une boîte noire ; c'est une petite cérémonie. D'abord les présentations, puis la poignée de main secrète, puis l'échange discret de clés de rechange pour la prochaine fois. Le Gestionnaire de sécurité conserve le script, L2CAP maintient tout le monde dans sa voie, et AES-CMAC fait le gros du travail en coulisses pendant que le public ne voit qu'une petite pression sur « Appairer ».

Ce qui ressemble à de l'hexadécimal aléatoire dans une capture est en réalité une série de promesses. Une confirmation qui dit : « Je ne bluffe pas ». Un aléatoire qui le prouve. Une vérification de la DHKey qui scelle l'accord. Les clés qui suivent sont moins des mots de passe que des amitiés : enregistrées une fois, réutilisées sans souci, assez solides pour survivre à un redémarrage ou à une semaine en mode avion.

Et la part humaine compte aussi. Just Works est pratique jusqu'à ce qu'il ne le soit plus. Numeric Comparison semble presque ludique, mais elle ferme la porte aux imposteurs. Out-of-Band est le signe de tête discret dans une pièce bondée. Choisir une méthode n'est pas une question de détails techniques ; c'est une question du type de confiance dont vos appareils ont besoin dans le contexte où ils vivent.

Ainsi, la prochaine fois qu'une invite d'appairage apparaîtra, ne vous contentez pas de cliquer. Imaginez les deux appareils se rapprocher, comparer leurs notes, faire leurs calculs et — seulement si tout concorde — décider de se souvenir l'un de l'autre. Ce petit nombre à six chiffres, cette simple pression sur un bouton, n'est que la surface d'une idée bien plus vaste : la confiance, acquise rapidement.

**Lectures complémentaires**

* [Spécification Bluetooth Core Vol 3, Part H : Security Manager](https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/host/security-manager-specification.html)
    
* [Standard AES-CMAC (NIST SP 800-38B)](https://csrc.nist.gov/publications/detail/sp/800-38b/final)
    
* [Introduction à la cryptographie sur les courbes elliptiques (ECC)](https://cryptobook.nakov.com/asymmetric-key-ciphers/elliptic-curve-cryptography-ecc)