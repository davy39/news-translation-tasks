---
title: Apprendre Wireshark – Tutoriel sur les réseaux informatiques
subtitle: ''
author: Omer Rosenbaum
co_authors: []
series: null
date: '2023-01-23T23:35:33.000Z'
originalURL: https://freecodecamp.org/news/learn-wireshark-computer-networking
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/Computer-Networks-Ethernet--3-.png
tags:
- name: computer network
  slug: computer-network
- name: computer networking
  slug: computer-networking
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
seo_title: Apprendre Wireshark – Tutoriel sur les réseaux informatiques
seo_desc: 'In this post, you will learn about the single most important and useful
  tool in Computer Networks – Wireshark.

  This post relies on basic knowledge of computer networks. Be sure to check my previous
  post about the five layers model if you need a refre...'
---

Dans cet article, vous apprendrez à utiliser l'outil le plus important et le plus utile dans les réseaux informatiques – Wireshark.

Cet article repose sur des connaissances de base des réseaux informatiques. Assurez-vous de consulter mon [article précédent sur le modèle à cinq couches](https://www.freecodecamp.org/news/the-five-layers-model-explained/) si vous avez besoin d'un rappel.

# Qu'est-ce que Wireshark ?

Wireshark est un sniffer, ainsi qu'un analyseur de paquets.

Que signifie cela ?

Vous pouvez considérer un **sniffer** comme un appareil de mesure. Nous l'utilisons pour examiner ce qui se passe à l'intérieur d'un câble réseau, ou dans l'air si nous traitons avec un réseau sans fil. Un sniffer nous montre les données qui passent par notre carte réseau.

Mais Wireshark fait plus que cela. Un sniffer pourrait simplement afficher un flux de bits - des uns et des zéros, que la carte réseau voit. Wireshark est également un **analyseur de paquets** qui affiche de nombreuses données significatives sur les trames qu'il voit.

Wireshark est un outil open-source et gratuit, et est largement utilisé pour analyser le trafic réseau.

Wireshark peut être utile dans de nombreux cas. Il peut être utile pour déboguer des problèmes dans votre réseau, par exemple – si vous ne pouvez pas vous connecter d'un ordinateur à un autre, et que vous voulez comprendre ce qui se passe.

Il peut également aider les programmeurs. Par exemple, imaginez que vous implémentez un programme de chat entre deux clients, et que quelque chose ne fonctionne pas. Pour comprendre ce qui est exactement envoyé, vous pouvez utiliser Wireshark pour voir les données transmises sur le fil.

Alors, familiarisons-nous avec Wireshark.

# Comment télécharger et installer Wireshark

Commencez par télécharger Wireshark depuis son site officiel :

[https://www.wireshark.org/#download](https://www.wireshark.org/#download)

Suivez les instructions de l'installateur et vous devriez être prêt à l'emploi.

# Comment capturer le trafic avec Wireshark

Lancez Wireshark, et commencez par capturer quelques données. Pour cela, vous pouvez appuyer sur `Ctrl+K` (PC) ou `Cmd+K` (Mac) pour obtenir la fenêtre `Options de capture`. Notez que vous pouvez accéder à cette fenêtre de différentes manières. Vous pouvez aller dans `Capture->Options`. Alternativement, vous pouvez cliquer sur l'icône `Options de capture`.

Je vous encourage à utiliser les raccourcis clavier et à vous familiariser avec eux dès le départ, car ils vous permettront de gagner du temps et de travailler plus efficacement.

Donc, encore une fois, j'ai utilisé `Ctrl+K` (ou `Cmd+K`) et j'ai obtenu cet écran :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-208.png)
_La fenêtre `Options de capture` dans Wireshark (Source : [Brief](https://www.youtube.com/watch?v=nbTJXIdEzlo))_

Ici, nous pouvons voir une liste d'interfaces, et j'en ai plusieurs. Laquelle est pertinente ? Si vous n'êtes pas sûr à ce stade, vous pouvez regarder la colonne `Trafic`, et voir quelles interfaces ont actuellement du trafic.

Ici, nous pouvons voir que `Wi-Fi 3` a du trafic qui le traverse, car la ligne est haute. Sélectionnez l'interface réseau pertinente, puis appuyez sur `Entrée`, ou cliquez sur le bouton `Démarrer`.

Laissez Wireshark capturer le réseau pendant un moment, puis arrêtez la capture en utilisant `Ctrl+E` / `Cmd+E`. Encore une fois, cela peut être réalisé de différentes manières – comme aller dans `Capture->Arrêter` ou cliquer sur l'icône `Arrêter`.

Considérez les différentes sections :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-210.png)
_Les sections de Wireshark (Source : [Brief](https://www.youtube.com/watch?v=nbTJXIdEzlo))_

La section marquée en rouge inclut le menu de Wireshark, avec toutes sortes d'options intéressantes.

La barre d'outils principale est marquée en bleu, offrant un accès rapide à certains éléments du menu.

Ensuite, marquée en vert, se trouve le **filtre d'affichage**. Nous y reviendrons bientôt, car c'est l'une des fonctionnalités les plus importantes de Wireshark.

Puis suivent :

# Le volet de la liste des paquets

Le volet de la liste des paquets est marqué en orange. Il affiche un court résumé de chaque paquet capturé.

(Note : le terme Trame appartient à une séquence d'octets dans la [couche de liaison de données](https://www.freecodecamp.org/news/the-five-layers-model-explained/), tandis qu'un Paquet est une séquence d'octets de la [couche réseau](https://www.freecodecamp.org/news/the-five-layers-model-explained/). Dans cet article, j'utiliserai les termes de manière interchangeable, bien que pour être précis, chaque paquet est une trame, mais chaque trame n'est pas un paquet, car il existe des trames qui ne contiennent pas de données de la couche réseau.)

Comme vous pouvez le voir dans l'image ci-dessus, nous avons quelques colonnes ici :

NUMÉRO (No.) – Le numéro du paquet dans le fichier de capture. Ce numéro ne changera pas, même si nous utilisons des filtres. Ce n'est qu'un numéro séquentiel – la première trame que vous avez capturée obtient le numéro 1, la deuxième trame obtient le numéro 2, et ainsi de suite.

Heure – L'horodatage du paquet. Il montre combien de temps s'est écoulé depuis le tout premier paquet que nous avons capturé jusqu'à ce que nous capturions le paquet en question. Par conséquent, le temps pour le paquet numéro 1 est toujours 0.

Source – L'adresse d'où provient ce paquet. Ne vous inquiétez pas si vous ne comprenez pas encore le format des adresses, nous couvrirons les différentes adresses dans les futurs tutoriels.

Destination – L'adresse où ce paquet va.

Protocole – Le nom du protocole en version courte. Ce sera le protocole supérieur – c'est-à-dire, le protocole de la couche la plus élevée.

Longueur – La longueur de chaque paquet, en octets.

Info – Informations supplémentaires sur le contenu du paquet. Cela change selon le protocole.

En cliquant sur les paquets dans ce volet, vous contrôlez ce qui est affiché dans les deux autres volets que je vais maintenant décrire.

# Le volet des détails des paquets

Cliquez sur l'un des paquets capturés. Dans l'exemple ci-dessous, j'ai cliqué sur le paquet numéro 147 :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-211.png)
_Sélectionner un paquet spécifique change le volet des détails des paquets (Source : [Brief](https://www.youtube.com/watch?v=nbTJXIdEzlo))_

Maintenant, le **volet des détails des paquets** affiche le paquet sélectionné dans le volet de la liste des paquets en plus de détails. Vous pouvez voir les couches ici.

Dans l'exemple ci-dessus, nous avons Ethernet II comme deuxième couche, IPv4 comme troisième couche, UDP comme quatrième couche, et certaines données comme charge utile.

Lorsque nous cliquons sur une couche spécifique, nous voyons en fait l'**en-tête** de cette couche.

Remarquez que nous ne voyons pas la première couche seule. Pour rappel, la première couche est responsable de la **transmission d'un seul bit** – 0 ou 1 – sur le réseau (si vous avez besoin d'un rappel sur les différentes couches, [consultez cet article](https://www.freecodecamp.org/news/the-five-layers-model-explained/)).

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-215.png)
_Le volet des octets des paquets dans Wireshark (Source : [Brief](https://www.youtube.com/watch?v=nbTJXIdEzlo))_

Sous le volet des détails des paquets, nous avons le **volet des octets des paquets**. Il affiche les données du paquet sélectionné dans le volet de la liste des paquets. Ce sont les données réelles envoyées sur le fil. Nous pouvons voir les données en base hexadécimale, ainsi qu'en forme ASCII.

# Comment utiliser le filtre d'affichage

Wireshark a de nombreuses fonctions différentes, et aujourd'hui nous allons nous concentrer sur une chose – le filtre d'affichage.

Comme vous pouvez le voir, une fois que vous commencez à capturer des données, vous obtenez BEAUCOUP de trafic. Mais vous ne voulez définitivement pas tout regarder.

Rappelez-vous l'exemple précédent – utiliser Wireshark pour déboguer un programme de chat que vous avez implémenté. Dans ce cas, vous aimeriez voir le trafic lié au programme de chat uniquement.

Disons que je veux filtrer uniquement les messages envoyés par l'adresse source de la trame numéro 149 (`192.168.1.3`). Je couvrirai les adresses IP dans les futurs articles, mais pour l'instant, vous pouvez voir qu'elle se compose de quatre nombres, délimités par un point :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-217.png)
_Le `filtre d'affichage` dans Wireshark (Source : [Brief](https://www.youtube.com/watch?v=nbTJXIdEzlo))_

Maintenant, même si vous ne savez pas comment filtrer uniquement les paquets envoyés depuis cette adresse IP, vous pouvez utiliser Wireshark pour vous montrer comment cela se fait.

Pour cela, allez dans le champ de droite que vous souhaitez filtrer – dans ce cas, l'adresse IP source. Ensuite, cliquez avec le bouton droit -> et choisissez `filtre -> Appliquer comme filtre`.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-218.png)
_Application d'un filtre d'affichage (Source : [Brief](https://www.youtube.com/watch?v=nbTJXIdEzlo))_

Après avoir appliqué le filtre, vous ne voyez que les paquets qui ont été envoyés depuis cette adresse. De plus, vous pouvez regarder la ligne du filtre d'affichage et voir la commande utilisée. De cette manière, vous pouvez apprendre la syntaxe du filtre d'affichage (dans cet exemple, il s'agit de `ip.src` pour le champ d'adresse source IP) :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-219.png)
_Application d'un filtre d'affichage (Source : [Brief](https://www.youtube.com/watch?v=nbTJXIdEzlo))_

Maintenant, essayez de filtrer uniquement les paquets qui ont été envoyés depuis cette adresse, et **à** l'adresse `172.217.16.142` (comme dans la trame 130 dans l'image ci-dessus). Comment feriez-vous cela ?

Eh bien, vous pourriez aller dans le champ pertinent – dans ce cas, l'adresse IP de destination. Maintenant, cliquez avec le bouton droit -> `Appliquer comme filtre` -> et sélectionnez `...et Sélectionné` :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-220.png)
_Application d'un filtre d'affichage (Source : [Brief](https://www.youtube.com/watch?v=nbTJXIdEzlo))_

Si vous regardez la ligne du filtre d'affichage après avoir appliqué ce filtre :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-221.png)
_Application d'un filtre d'affichage (Source : [Brief](https://www.youtube.com/watch?v=nbTJXIdEzlo))_

Vous pouvez également apprendre que vous pouvez utiliser l'opérande `&&` afin d'effectuer un `et`. Vous pourriez également écrire le mot `and`, à la place, et obtenir le même résultat.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-222.png)
_Application de plusieurs conditions en utilisant `&&` ou `and` (Source : [Brief](https://www.youtube.com/watch?v=nbTJXIdEzlo))_

# Comment utiliser Wireshark pour rechercher l'utilitaire Ping

**Ping** est un utilitaire utile pour vérifier la connectivité des serveurs distants.

[Cette page](https://www.howtogeek.com/235101/10-ways-to-open-the-command-prompt-in-windows-10/) explique comment utiliser `ping` dans Windows, et [cette page](https://macpaw.com/how-to/use-terminal-on-mac) explique comment faire cela dans OSX.

Maintenant, nous pouvons essayer d'utiliser `ping <adresse>` en utilisant la ligne de commande. Par défaut, ping envoie `4` requêtes et attend une réponse **pong**. Si nous voulons qu'il envoie une seule requête, nous pourrions utiliser `-n 1` :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-224.png)
_Utilisation de la ligne de commande pour ping Google (Source : [Brief](https://www.youtube.com/watch?v=nbTJXIdEzlo))_

Vous pouvez voir que Google a répondu. Le temps qu'il a fallu pour que le message revienne était de 92 millisecondes. Nous apprendrons la signification de TTL dans les futurs articles.

Ping est utile pour déterminer si un service distant est disponible, et à quelle vitesse il est possible d'atteindre ce service. Si cela prend très longtemps pour atteindre un serveur fiable comme google.com, nous pourrions avoir un problème de connectivité.

## Essayez par vous-même

Maintenant, essayez d'utiliser Wireshark pour répondre aux questions suivantes :

1) Quel protocole l'utilitaire **ping** utilise-t-il ?

2) En utilisant uniquement Wireshark, calculez le RTT (Round Trip Time) – combien de temps il a fallu depuis l'envoi de votre requête ping jusqu'à la réception de la réponse ping ?

Ensuite, exécutez la commande suivante :

`ping -n 1 -l 342 www.google.com`

3) Quelle est la principale différence entre le paquet envoyé par cette commande et le paquet envoyé par la commande précédente ? Où dans Wireshark pouvez-vous voir cette différence, en inspectant les paquets ?

4) Quel est le contenu (données) fourni dans le paquet de requête ping ? Quel est le contenu fourni dans le paquet de réponse ping ?

## Résolvons cela ensemble

Donc, la première question est :

### Quel protocole l'utilitaire ping utilise-t-il ?

Pour répondre à cette question, commencez à capturer dans Wireshark, et exécutez simplement la commande `ping`. Arrêtez la capture, et considérez le volet des paquets :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-225.png)
_Capture pendant l'exécution de ping (source : [Brief](https://www.youtube.com/watch?v=B5iEmaZK9xI&t=2s))_

Wireshark marque les paquets comme `Echo (ping) request` et `Echo (ping) reply`.

En considérant ces paquets, nous pouvons voir qu'ils se composent de `Ethernet` pour la couche de liaison de données (bien que cela puisse différer d'un réseau à l'autre), `IPv4` comme couche réseau, puis `ICMP` comme protocole pour Ping lui-même. Donc la réponse que nous avons trouvée est : **ICMP**.

Question suivante :

### En utilisant uniquement Wireshark, calculez le Round Trip Time

En regardant les paquets capturés, nous pouvons voir la colonne `Time`, et soustraire le temps du paquet Pong (`7.888...`) du temps du paquet Ping (`7.796...`).

Donc dans ce cas, le RTT était de : **92 ms**. Bien sûr, la valeur peut être différente lorsque vous exécutez l'utilitaire `ping`.

### Quelle est la principale différence entre le paquet envoyé par cette commande et le paquet envoyé par la commande précédente ?

Pour la question numéro 3, on nous demande d'exécuter la commande suivante :

> ping -n 1 -l 342 www.google.com

En regardant la première exécution de `ping`, nous pouvons voir que la longueur des paquets est de `74` octets :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-225.png)
_Capture pendant l'exécution de ping (source : [Brief](https://www.youtube.com/watch?v=B5iEmaZK9xI&t=2s))_

En observant les paquets envoyés après avoir exécuté `ping` avec l'argument `-l 342`, nous pouvons voir que la valeur est plus grande :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-228.png)
_Capture pendant l'exécution de ping (source : [Brief](https://www.youtube.com/watch?v=B5iEmaZK9xI&t=2s))_

Donc la principale différence est la quantité d'octets envoyés comme données.

Question numéro quatre :

### Quel est le contenu (données) fourni dans le paquet de requête ping ?

### Quel est le contenu fourni dans le paquet de réponse ping ?

Cliquez sur le paquet de requête pour observer les données envoyées :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-230.png)
_Observation des données envoyées par l'utilitaire `ping` (source : [Brief](https://www.youtube.com/watch?v=B5iEmaZK9xI&t=2s))_

La réponse pour la requête ping est `a` à `w`, encore et encore.

En ce qui concerne la réponse ping – elle est la même que la requête.

# Résumé

Wireshark est un outil merveilleux pour toute personne travaillant avec les réseaux informatiques. Il peut vous aider à comprendre comment les protocoles fonctionnent et également vous aider à déboguer des applications ou des problèmes de réseau.

Comme vous l'avez vu, vous pouvez apprendre comment les choses fonctionnent en exécutant simplement Wireshark en arrière-plan tout en les utilisant, puis en inspectant le trafic. Avec cet outil à votre disposition, le ciel est la limite.

Dans les futurs tutoriels, nous nous appuierons également sur nos connaissances de Wireshark et l'utiliserons pour mieux comprendre divers concepts des réseaux informatiques.

## À propos de l'auteur

[Omer Rosenbaum](https://www.linkedin.com/in/omer-rosenbaum-034a08b9/) est le Chief Technology Officer de [Swimm](https://swimm.io/). Il est l'auteur de la chaîne [YouTube Brief](https://youtube.com/@BriefVid). Il est également un expert en formation cybernétique et fondateur de Checkpoint Security Academy. Il est l'auteur de [Computer Networks (en hébreu)](https://data.cyber.org.il/networks/networks.pdf). Vous pouvez le trouver sur [Twitter](https://twitter.com/Omer_Ros).

### Références supplémentaires

* [Liste de lecture sur les réseaux informatiques - sur ma chaîne Brief](https://www.youtube.com/playlist?list=PL9lx0DXCC4BMS7dB7vsrKI5wzFyVIk2Kg).
* [Site web de Wireshark](https://www.wireshark.org/).