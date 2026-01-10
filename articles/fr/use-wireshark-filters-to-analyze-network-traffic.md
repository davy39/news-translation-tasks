---
title: Comment utiliser les filtres Wireshark pour analyser le trafic de votre réseau
subtitle: ''
author: Hang Hu
co_authors: []
series: null
date: '2025-04-03T12:49:20.923Z'
originalURL: https://freecodecamp.org/news/use-wireshark-filters-to-analyze-network-traffic
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1743684532493/cc26aa99-fc7a-4b47-ab16-60dac77561fd.png
tags:
- name: '#cybersecurity'
  slug: cybersecurity-1
- name: Wireshark
  slug: wireshark
- name: Linux
  slug: linux
seo_title: Comment utiliser les filtres Wireshark pour analyser le trafic de votre
  réseau
seo_desc: Wireshark is an open-source tool widely regarded as the gold standard for
  network packet analysis. It allows you to capture live network traffic or inspect
  pre-recorded capture files, breaking down the data into individual packets for detailed
  examin...
---

Wireshark est un outil open-source largement considéré comme la référence en matière d'analyse de paquets réseau. Il vous permet de capturer le trafic réseau en direct ou d'inspecter des fichiers de capture préenregistrés, en décomposant les données en paquets individuels pour un examen détaillé.

Vous pouvez utiliser Wireshark dans des scénarios tels que le dépannage des problèmes de performance réseau (par exemple, des connexions lentes ou des paquets perdus), l'investigation d'activités suspectes (comme la détection de logiciels malveillants ou d'accès non autorisés), ou l'apprentissage du fonctionnement des protocoles comme HTTP, TCP ou DNS dans des environnements réels.

Pour les débutants, pensez à Wireshark comme à une fenêtre sur le monde invisible de la communication réseau, révélant ce qui se passe en coulisses lorsque vous naviguez sur le web, envoyez un e-mail ou diffusez une vidéo. Sa puissance réside dans sa capacité à fournir des informations granulaires, ce qui en fait un outil indispensable pour les administrateurs réseau, les passionnés de cybersécurité et toute personne curieuse de savoir comment fonctionnent les réseaux.

Dans ce tutoriel, vous apprendrez à utiliser les filtres d'affichage de Wireshark pour analyser le trafic réseau et repérer les potentielles menaces de sécurité. Wireshark est un puissant analyseur de protocoles réseau capable de capturer et de disséquer les paquets réseau, ce qui est crucial pour les professionnels de la cybersécurité.

### Voici ce que nous allons couvrir :

* [Comment démarrer Wireshark et analyser le trafic réseau](#heading-comment-demarrer-wireshark-et-analyser-le-trafic-reseau)

* [Comment travailler avec les fichiers de capture réseau](#heading-comment-travailler-avec-les-fichiers-de-capture-reseau)

* [Comprendre l'interface de Wireshark](#heading-comprendre-linterface-de-wireshark)

* [Comprendre et appliquer les filtres d'affichage de base](#heading-comprendre-et-appliquer-les-filtres-daffichage-de-base)

* [Techniques de filtrage avancées](#heading-techniques-de-filtrage-avancees)

* [Analyser le trafic lié à la sécurité](#heading-analyser-le-trafic-lie-a-la-securite)

* [Analyser le trafic d'exemple et générer un nouveau trafic](#heading-analyser-le-trafic-dexemple-et-generer-un-nouveau-trafic)

## **Prérequis**

Avant de commencer, vous devez connaître la **syntaxe de base de Linux**. Vous pouvez l'apprendre via ce [Linux Skill Tree](https://labex.io/skilltrees/linux).

Ne vous inquiétez pas si vous êtes nouveau dans [**Wireshark**](https://labex.io/skilltrees/wireshark) – je vais tout expliquer au fur et à mesure.

## **Comment démarrer Wireshark et analyser le trafic réseau**

Dans cette étape, nous allons commencer à utiliser Wireshark. Tout d'abord, vous apprendrez à le lancer. Ensuite, vous capturerez le trafic réseau ou utiliserez un fichier d'exemple fourni pour l'analyse. Comprendre l'interface de Wireshark est crucial, car cela vous aide à visualiser et analyser les données des paquets.

### Installation de Wireshark sur Ubuntu 22.04

Avant de pouvoir commencer à utiliser Wireshark, vous devez l'installer. Ouvrez une fenêtre de terminal et exécutez les commandes suivantes :

```bash
sudo apt update
sudo apt install wireshark -y
```

### **Lancement de Wireshark**

Pour démarrer Wireshark, vous devez ouvrir une fenêtre de terminal. Vous pouvez le faire en cliquant sur l'icône du terminal dans la barre des tâches ou en appuyant sur `Ctrl+Alt+T`. Une fois le terminal ouvert, vous utiliserez une commande pour démarrer Wireshark. Dans le terminal, tapez la commande suivante et appuyez sur Entrée :

```bash
wireshark
```

Cette commande indique à votre système de démarrer l'application Wireshark. Après quelques secondes, Wireshark s'ouvrira. Vous devriez voir une fenêtre similaire à celle montrée ci-dessous :

![Exemple d'interface principale de Wireshark](https://cdn.hashnode.com/res/hashnode/image/upload/v1743385586635/78f76c20-c8d0-48d2-bdb7-17ff3f5fc261.png align="center")

## **Comment travailler avec les fichiers de capture réseau**

Pour cette partie du tutoriel, vous avez deux options :

### **Option 1 : Utiliser le fichier d'exemple fourni**

```bash
# Télécharger un fichier de capture de paquets d'exemple avec du trafic mixte
wget -q https://s3.amazonaws.com/tcpreplay-pcap-files/smallFlows.pcap -O /home/labex/project/sample.pcapng

# Assurez-vous que l'utilisateur a accès au fichier
chmod 644 /home/labex/project/sample.pcapng
```

J'ai préparé un fichier de capture d'exemple pour vous à `/home/labex/project/sample.pcapng`. Ce fichier contient divers types de trafic réseau que vous pouvez analyser.

Pour ouvrir ce fichier :

1. Dans Wireshark, allez dans Fichier > Ouvrir

2. Accédez à `/home/labex/project/sample.pcapng`

3. Cliquez sur "Ouvrir"

![Capture d'écran de l'ouverture de fichier dans Wireshark](https://cdn.hashnode.com/res/hashnode/image/upload/v1743385612148/dbeb3d39-db15-4363-a499-e8b527b43d84.png align="center")

Le fichier se chargera dans Wireshark, montrant divers paquets qui ont été capturés précédemment.

### **Option 2 : Capturer votre propre trafic**

Si vous préférez capturer votre propre trafic :

1. Dans la fenêtre principale de Wireshark, recherchez la liste des interfaces réseau disponibles.

2. Trouvez l'interface `eth1`. Dans cet environnement de laboratoire, `eth1` est l'interface réseau principale que nous utiliserons pour capturer les paquets.

3. Double-cliquez sur `eth1`. Cette action démarre immédiatement le processus de capture des paquets.

4. Générez du trafic réseau en ouvrant un nouveau terminal et en exécutant :

```bash
curl www.google.com
```

5. Une fois que vous avez capturé suffisamment de paquets (visez au moins 20-30 paquets), cliquez sur le bouton rouge "Arrêter" dans la barre d'outils de Wireshark.

## **Comprendre l'interface de Wireshark**

L'interface de Wireshark est divisée en trois panneaux principaux, chacun ayant un objectif spécifique :

1. **Liste des paquets (panneau supérieur)** : Ce panneau montre tous les paquets qui ont été capturés dans l'ordre où ils ont été reçus. Il vous donne un aperçu rapide du trafic capturé.

2. **Détails des paquets (panneau central)** : Lorsque vous sélectionnez un paquet dans le panneau supérieur, ce panneau central montre les détails de ce paquet dans un format hiérarchique. Il décompose la structure du paquet, montrant des informations comme les adresses IP source et de destination, les types de protocoles, et plus encore.

3. **Octets des paquets (panneau inférieur)** : Ce panneau affiche les octets bruts du paquet sélectionné au format hexadécimal. Il est utile pour une analyse approfondie, surtout lorsque vous devez examiner les données exactes transmises.

![Interface de Wireshark](https://cdn.hashnode.com/res/hashnode/image/upload/v1743386808927/2225da6c-a652-4886-bd7d-f3c94586c688.jpeg align="center")

Pour voir comment ces panneaux fonctionnent ensemble, cliquez sur différents paquets dans le panneau supérieur. Vous verrez les détails et les octets bruts correspondants se mettre à jour dans les panneaux central et inférieur.

## **Comprendre et appliquer les filtres d'affichage de base**

Dans cette étape, nous allons explorer les filtres d'affichage dans Wireshark. Les filtres d'affichage sont des outils essentiels lorsqu'il s'agit d'analyser le trafic réseau. Ils vous aident à vous concentrer sur des types spécifiques de paquets au lieu de devoir parcourir toutes les données capturées.

À la fin de cette section, vous saurez ce que sont les filtres d'affichage, pourquoi ils sont utiles, et comment appliquer des filtres de base pour isoler des types spécifiques de trafic réseau.

### **Que sont les filtres d'affichage ?**

Lorsque vous analysez le trafic réseau, examiner chaque paquet capturé peut être accablant. Vous souhaitez généralement vous concentrer sur des types spécifiques de paquets. C'est là que les filtres d'affichage de Wireshark interviennent. Ils vous permettent de n'afficher que les paquets qui répondent à certains critères. Cela rend le processus d'analyse beaucoup plus efficace car vous ne perdez pas de temps sur des données non pertinentes.

Les filtres d'affichage dans Wireshark utilisent une syntaxe spéciale. Cette syntaxe vous permet de filtrer les paquets en fonction de divers attributs tels que les protocoles, les adresses IP, les ports, et même le contenu des paquets. Comprendre cette syntaxe est la clé pour utiliser efficacement les filtres d'affichage.

### **Barre d'outils de filtrage**

Regardez en haut de la fenêtre de Wireshark. Vous remarquerez un champ de texte. Il peut être étiqueté "Appliquer un filtre d'affichage..." ou simplement afficher "Expression...". C'est l'endroit où vous entrerez vos filtres d'affichage. Une fois que vous avez entré un filtre et appuyé sur Entrée, Wireshark utilisera ce filtre pour n'afficher que les paquets pertinents.

![Emplacement de la barre d'outils de filtrage de Wireshark](https://cdn.hashnode.com/res/hashnode/image/upload/v1743385642595/018e9680-1c29-4168-9d60-975464722447.png align="center")

### **Filtres de protocole de base**

Commençons par un exemple simple. Supposons que vous souhaitez afficher uniquement le trafic HTTP. HTTP est le protocole utilisé pour la navigation web. Pour ce faire, vous entrerez un filtre dans la barre d'outils de filtrage. Tapez le filtre suivant, puis appuyez sur Entrée :

```plaintext
http
```

![Sortie du filtre HTTP de Wireshark](https://cdn.hashnode.com/res/hashnode/image/upload/v1743385678124/1dff7e49-13c5-439e-aeca-82b461b8727b.png align="center")

Après avoir appliqué ce filtre, Wireshark n'affichera que les paquets HTTP. Tous les autres paquets seront temporairement masqués. Vous remarquerez que la barre de filtre devient verte lorsque vous appliquez un filtre valide. C'est une indication visuelle que votre filtre fonctionne correctement.

La sortie doit maintenant montrer uniquement les paquets liés au trafic HTTP. Cela inclut généralement les requêtes web (lorsque vous demandez des informations à un site web) et les réponses (lorsque le site web vous envoie les informations). Si vous ne voyez aucun trafic HTTP dans le fichier d'exemple, vous pouvez essayer différents protocoles qui pourraient être présents, tels que TCP, UDP ou DNS :

```plaintext
tcp
```

Ou essayez de générer plus de trafic HTTP en exécutant la commande `curl` dans un terminal :

```bash
curl www.google.com
```

### **Filtres d'adresse IP**

Ensuite, filtrons le trafic en fonction des adresses IP. Une adresse IP est comme un identifiant unique pour un appareil sur un réseau. Tout d'abord, regardez votre liste de paquets. Vous verrez des colonnes étiquetées "Source" et "Destination". Ces colonnes montrent les adresses IP des appareils envoyant et recevant les paquets.

Une fois que vous avez identifié une adresse IP qui apparaît fréquemment dans votre capture (par exemple, disons que vous voyez `192.168.1.1`), vous pouvez l'utiliser pour créer un filtre. Tapez le filtre suivant dans la barre d'outils de filtrage pour voir uniquement les paquets de cette source :

```plaintext
ip.src == 192.168.3.131
```

![Exemple de filtre d'adresse IP dans Wireshark](https://cdn.hashnode.com/res/hashnode/image/upload/v1743385707141/8719b584-9498-4ecb-bf67-d354906626e0.png align="center")

Vous pouvez remplacer `192.168.3.131` par une adresse IP que vous voyez réellement dans votre capture. Après avoir appliqué ce filtre, seuls les paquets avec cette adresse IP source seront affichés.

Si vous souhaitez voir tous les paquets à nouveau, vous pouvez effacer le filtre actuel. Cliquez simplement sur le bouton "Effacer" (X) sur le côté droit de la barre de filtre.

### **Filtres de port**

De nombreux services réseau fonctionnent sur des ports spécifiques. Un port est comme une porte sur un appareil qui permet à des types spécifiques de trafic réseau d'entrer ou de sortir. Par exemple, HTTP utilise généralement le port 80.

Pour filtrer les paquets par numéro de port, vous pouvez utiliser le filtre suivant :

```plaintext
tcp.port == 80
```

Ce filtre affichera les paquets entrants et sortants qui utilisent le port TCP 80. Vous pouvez également essayer d'autres ports courants comme 443 (HTTPS) ou 53 (DNS) en fonction de ce qui est disponible dans votre capture.

### **Combinaison de filtres**

Vous pouvez rendre vos filtres plus puissants en les combinant à l'aide d'opérateurs logiques comme `and` et `or`. Par exemple, si vous souhaitez afficher uniquement le trafic HTTP qui utilise le port 80, vous pouvez utiliser le filtre suivant :

```plaintext
http and tcp.port == 80
```

![Exemple de filtre combiné dans Wireshark](https://cdn.hashnode.com/res/hashnode/image/upload/v1743385736030/8230d965-e822-4341-afa5-35239fbb6975.png align="center")

Essayez d'appliquer différentes combinaisons de filtres et observez comment les paquets affichés changent. N'oubliez pas, avant d'essayer un nouveau filtre, vous pouvez soit effacer le précédent en cliquant sur le bouton "Effacer", soit modifier le filtre existant directement dans la barre de filtre pour le compléter.

## **Techniques de filtrage avancées**

Dans cette partie, nous allons explorer comment créer des filtres plus sophistiqués pour une analyse détaillée du trafic réseau. En tant que débutant, vous pourriez vous demander pourquoi nous avons besoin de techniques de filtrage avancées. Eh bien, dans des scénarios réels, les fichiers de capture réseau peuvent être extrêmement volumineux, remplis de toutes sortes de trafic. Les techniques de filtrage avancées sont comme une loupe puissante pour les professionnels de la sécurité. Elles nous aident à repérer rapidement le trafic suspect ou important dans l'océan de données de ces grands fichiers de capture.

### **Filtres complexes avec plusieurs conditions**

Wireshark vous donne la possibilité de créer des filtres complexes en combinant plusieurs conditions. Cela est très utile lorsque vous souhaitez être plus précis dans votre analyse de trafic. Commençons par créer un filtre pour trouver les requêtes HTTP GET.

```plaintext
http.request.method == "GET"
```

Ce filtre est conçu pour afficher uniquement les paquets HTTP qui contiennent des requêtes GET. Lorsque vous appliquez ce filtre, vous verrez les paquets qui sont des requêtes envoyées aux serveurs web. La raison pour laquelle nous utilisons ce filtre est que les requêtes GET sont un type courant de requête HTTP utilisé pour récupérer des données d'un serveur. En isolant ces requêtes, nous pouvons nous concentrer sur les activités de récupération de données dans le réseau.

Si votre fichier d'exemple ne contient pas de requêtes HTTP GET, essayez ce filtre alternatif pour trouver les paquets TCP SYN qui indiquent des tentatives de connexion :

```plaintext
tcp.flags.syn == 1
```

Maintenant, rendons notre filtre plus spécifique. Nous allons ajouter une condition de port :

```plaintext
tcp.port == 80 and http.request.method == "GET"
```

Ce nouveau filtre montre uniquement les requêtes HTTP GET qui se produisent sur le port HTTP standard (80). Le port HTTP standard est largement utilisé pour le trafic web non chiffré. En ajoutant cette condition de port, nous restreignons notre recherche aux seules requêtes GET qui utilisent le canal de communication HTTP typique.

### **Filtrage basé sur la taille des paquets**

Les attaques réseau impliquent souvent des paquets de tailles inhabituelles. Les attaquants peuvent utiliser des paquets grands ou petits pour cacher des données malveillantes ou pour perturber le fonctionnement normal du réseau. Pour filtrer en fonction de la taille des paquets, nous utilisons une syntaxe spécifique :

```plaintext
tcp.len >= 100 and tcp.len <= 500
```

Ce filtre affiche les paquets TCP avec une longueur de charge utile comprise entre 100 et 500 octets. Vous pouvez ajuster ces valeurs selon vos besoins. Par exemple, si vous suspectez qu'une attaque implique des paquets plus grands, vous pouvez augmenter la limite supérieure. En filtrant en fonction de la taille des paquets, nous pouvons identifier des schémas de trafic anormaux qui pourraient indiquer une attaque.

### **Filtrage basé sur un contenu spécifique**

Vous pouvez également filtrer le trafic en fonction d'un contenu spécifique dans les paquets. Cela est très utile lorsque vous recherchez un trafic lié à un site web ou un service particulier. Par exemple, trouvons le trafic HTTP lié à un site web spécifique.

```plaintext
http.host contains "google"
```

![Filtre d'hôte HTTP de Wireshark](https://cdn.hashnode.com/res/hashnode/image/upload/v1743385773497/36b7bc2e-b7e9-4b68-9dc7-82e429c5ea01.png align="center")

Ce filtre montre uniquement le trafic HTTP où l'en-tête d'hôte contient "google". Vous pouvez remplacer "google" par n'importe quel domaine qui vous intéresse. L'en-tête d'hôte dans une requête HTTP indique au serveur quel site web le client essaie d'accéder. En filtrant en fonction de l'en-tête d'hôte, nous pouvons nous concentrer sur le trafic lié à un domaine spécifique.

Si votre fichier d'exemple n'a pas de trafic HTTP avec des en-têtes d'hôte, essayez ce filtre de contenu plus général :

```plaintext
frame contains "http"
```

### **Utilisation de l'opérateur "contains" pour la recherche de texte**

L'opérateur `contains` est un outil pratique pour rechercher des chaînes de texte spécifiques dans les paquets. Il nous permet de rechercher certains mots-clés dans les données des paquets.

```plaintext
frame contains "password"
```

Ce filtre montre les paquets contenant le mot "password" n'importe où dans les données du paquet. Cela peut être très utile pour détecter d'éventuels problèmes de sécurité. Par exemple, si des mots de passe sont envoyés en texte clair (ce qui est un grand risque de sécurité), ce filtre peut nous aider à repérer ces paquets.

Ou essayez ce filtre :

```plaintext
frame contains "login"
```

![Exemple de filtre de mot de passe dans Wireshark](https://cdn.hashnode.com/res/hashnode/image/upload/v1743385793822/024b4482-0b5d-4b20-985c-6263bd7f48d6.png align="center")

### **Négation des filtres**

Parfois, vous pourriez vouloir voir tout le trafic sauf certains types. C'est là que l'opérateur `not` intervient.

```plaintext
not arp
```

Ce filtre masque tous les paquets ARP. ARP (Address Resolution Protocol) est utilisé pour mapper les adresses IP aux adresses MAC dans un réseau local. Parfois, le trafic ARP peut être très courant et peut encombrer votre analyse. En utilisant l'opérateur `not`, vous pouvez exclure ce type de trafic et vous concentrer sur d'autres paquets plus pertinents.

### **Enregistrement et application de filtres en favoris**

Si vous utilisez fréquemment certains filtres, vous n'avez pas besoin de les taper à chaque fois. Vous pouvez les enregistrer en favoris. Voici comment faire :

1. Entrez un filtre dans la barre de filtre. C'est là que vous tapez les expressions de filtre que nous avons apprises.

2. Cliquez sur le bouton "+" sur le côté droit de la barre de filtre. Ce bouton est utilisé pour enregistrer le filtre actuel en tant que favoris.

3. Donnez un nom à votre filtre et cliquez sur "OK". Nommer le filtre le rend facile à identifier plus tard.

Une fois que vous avez enregistré votre filtre, vous pouvez l'appliquer en cliquant sur son nom dans le menu déroulant des filtres. Cela vous fait gagner du temps et des efforts, surtout lorsque vous effectuez des analyses répétées.

### **Exportation des paquets filtrés**

Après avoir filtré votre trafic pour n'afficher que les paquets d'intérêt, vous pourriez vouloir enregistrer uniquement ces paquets dans un nouveau fichier. Cela est utile pour partager des résultats spécifiques avec des collègues ou pour une analyse plus approfondie. Voici comment procéder :

1. Appliquez votre filtre souhaité. Assurez-vous d'avoir configuré le filtre pour n'afficher que les paquets que vous souhaitez enregistrer.

2. Cliquez sur Fichier > Exporter les paquets spécifiés. Cette option vous permet d'exporter un ensemble spécifique de paquets.

3. Assurez-vous que "Affichés" est sélectionné dans la section Plage de paquets. Cela garantit que seuls les paquets actuellement visibles (c'est-à-dire ceux qui correspondent à votre filtre) sont exportés.

4. Choisissez un nom de fichier et un emplacement. C'est là que vous décidez où enregistrer le nouveau fichier de capture et comment le nommer.

5. Cliquez sur "Enregistrer". Cela crée un nouveau fichier de capture contenant uniquement les paquets qui correspondaient à votre filtre.

## **Analyser le trafic lié à la sécurité**

Dans cette étape, nous allons nous concentrer sur l'utilisation des filtres Wireshark pour l'analyse de sécurité. L'analyse de sécurité est cruciale dans le monde de la cybersécurité car elle nous aide à repérer les activités potentiellement malveillantes dans le trafic réseau. À la fin de cette section, vous serez capable d'identifier divers types de menaces de sécurité en utilisant des filtres Wireshark spécifiques.

### **Identifier les activités de balayage de ports**

Le balayage de ports est une technique courante utilisée par les attaquants pour recueillir des informations sur un système cible. Les attaquants l'utilisent pour trouver des ports ouverts sur un réseau, qu'ils peuvent ensuite exploiter.

Pour détecter les balayages de ports potentiels, nous recherchons un grand nombre de tentatives de connexion provenant d'une seule source vers plusieurs ports.

Utilisons un filtre spécifique pour identifier de telles activités. Essayez ce filtre dans Wireshark :

```plaintext
tcp.flags.syn == 1 and tcp.flags.ack == 0
```

Ce filtre montre les paquets SYN sans le drapeau ACK. Dans une connexion TCP, le paquet SYN est le premier envoyé pour initier une connexion, et le paquet ACK est utilisé pour accuser réception de la connexion. Lorsque nous voyons beaucoup de paquets SYN sans ACK provenant d'une même source vers différents ports de destination, c'est une forte indication de balayage de ports.

### **Détecter le trafic DNS suspect**

Le tunneling DNS et d'autres attaques basées sur le DNS deviennent de plus en plus courants. Ces attaques utilisent le protocole DNS pour cacher des activités malveillantes, telles que l'exfiltration de données ou la communication de commande et de contrôle. Pour détecter de telles attaques, nous devons rechercher un trafic DNS inhabituel.

Utilisez ce filtre pour examiner les requêtes DNS :

```plaintext
dns
```

Une fois que vous avez appliqué ce filtre, recherchez des noms de domaine inhabituellement longs ou un volume élevé de requêtes DNS vers le même domaine. Ceux-ci pourraient être des signes d'exfiltration de données ou de communication de commande et de contrôle.

### **Identifier les tentatives de force brute de mot de passe**

Les attaques par force brute de mot de passe sont une méthode courante pour les attaquants d'obtenir un accès non autorisé à des services comme SSH ou FTP. Dans une attaque par force brute, l'attaquant essaie plusieurs combinaisons de mots de passe jusqu'à ce qu'il trouve la bonne.

Pour détecter les tentatives potentielles de force brute de mot de passe, nous pouvons filtrer les tentatives de connexion échouées. Utilisez ce filtre :

```plaintext
ftp contains "530" or ssh contains "Failed"
```

Ce filtre montre les paquets FTP et SSH qui contiennent des messages de réponse d'échec courants. Si vous voyez plusieurs échecs provenant de la même source, cela peut indiquer une tentative de force brute.

### **Analyser les réponses d'erreur HTTP**

Les attaques contre les applications web génèrent souvent des réponses d'erreur HTTP. Les attaquants peuvent essayer d'exploiter des vulnérabilités dans les applications web, et ces tentatives peuvent entraîner des réponses d'erreur du serveur.

Filtrez ces réponses d'erreur avec :

```plaintext
http.response.code >= 400
```

Ce filtre montre les paquets de réponse HTTP avec des codes d'état de 400 ou plus. Tous ces codes d'état représentent des réponses d'erreur. En examinant ces paquets, nous pouvons identifier les tentatives d'exploitation web.

### **Trouver des identifiants en texte clair**

Transmettre des identifiants en texte clair est un risque majeur pour la sécurité. Si un attaquant intercepte ces identifiants, il peut obtenir un accès non autorisé au système.

Pour détecter les identifiants en texte clair, utilisez ce filtre :

```plaintext
http contains "user" or http contains "pass" or http contains "login"
```

![Filtre de texte clair des identifiants de Wireshark](https://cdn.hashnode.com/res/hashnode/image/upload/v1743385832534/4c38654f-8ff0-4bc3-8bc6-0dd1161dc0f1.png align="center")

Ce filtre nous aide à trouver le trafic HTTP qui pourrait contenir des informations de connexion. Examinez attentivement les paquets qui correspondent à ce filtre pour identifier les risques potentiels pour la sécurité.

## **Analyser le trafic d'exemple et générer un nouveau trafic**

Maintenant que vous avez appris divers filtres axés sur la sécurité, il est temps de mettre vos connaissances en pratique. Vous pouvez soit analyser le fichier d'exemple fourni, soit générer et analyser un nouveau trafic.

### **Analyser le fichier d'exemple**

Si vous utilisez le fichier d'exemple fourni (`/home/labex/project/sample.pcapng`), essayez d'appliquer certains des filtres de sécurité que nous avons discutés pour identifier des motifs intéressants :

```plaintext
tcp.flags.syn == 1 and tcp.flags.ack == 0
```

Recherchez des motifs qui pourraient indiquer un balayage, des connexions suspectes ou d'autres préoccupations de sécurité.

### **Générer et analyser un nouveau trafic**

Alternativement, ouvrez une nouvelle fenêtre de terminal. Dans cette fenêtre, nous allons générer du trafic HTTP avec plusieurs requêtes. Exécutez les commandes suivantes :

```bash
for i in {1..5}; do
  curl -I www.google.com
  sleep 1
done
```

Ces commandes envoient cinq requêtes HTTP HEAD à `www.google.com` avec un intervalle d'une seconde entre chaque requête.

Ensuite, allez dans Wireshark et appliquez ce filtre pour trouver toutes les requêtes HTTP :

```plaintext
http.request
```

Ce filtre affichera toutes les requêtes HTTP dans le trafic capturé.

Parcourez ces paquets pour identifier les motifs du trafic HTTP normal. Remarquez les en-têtes, la fréquence des requêtes et d'autres détails.

Enfin, essayez de créer un filtre qui peut distinguer la navigation HTTP normale des outils de balayage automatisés. Par exemple :

```plaintext
http.request and !(http.user_agent contains "Mozilla")
```

![Filtre d'agent utilisateur HTTP de Wireshark](https://cdn.hashnode.com/res/hashnode/image/upload/v1743385858895/3feb916b-39ac-4ced-ab76-8597186cbbf0.png align="center")

Ce filtre montre les requêtes HTTP qui n'ont pas d'agents utilisateurs de navigateur. Puisque la plupart des navigations web normales sont effectuées à l'aide de navigateurs avec Mozilla dans l'agent utilisateur, les requêtes sans celui-ci pourraient indiquer des outils automatisés plutôt qu'une navigation normale.

En pratiquant ces techniques de filtrage axées sur la sécurité, vous développerez les compétences nécessaires pour identifier rapidement le trafic suspect dans les captures réseau du monde réel.

## **Conclusion**

Dans ce tutoriel, vous avez appris à utiliser les filtres d'affichage de Wireshark pour l'analyse du trafic réseau et l'identification des potentielles menaces de sécurité.

Vous avez commencé soit en travaillant avec un fichier de capture d'exemple fourni, soit en capturant le trafic réseau en direct et en vous familiarisant avec l'interface de Wireshark. Ensuite, vous avez maîtrisé les filtres d'affichage de base pour isoler des types spécifiques de trafic selon les protocoles, les adresses IP et les ports. Vous avez également perfectionné vos compétences avec des techniques de filtrage avancées, en combinant plusieurs conditions et en recherchant un contenu spécifique. Enfin, vous avez appliqué ces compétences dans des scénarios d'analyse de sécurité pour détecter des activités suspectes telles que le balayage de ports, l'exposition des identifiants et les attaques potentielles.

Ces compétences de filtrage Wireshark sont cruciales pour le dépannage efficace du réseau et l'analyse de sécurité. En isolant rapidement les paquets pertinents à partir de grandes captures, vous pouvez grandement réduire le temps nécessaire pour identifier et répondre aux problèmes de réseau et aux incidents de sécurité.

En continuant à pratiquer avec Wireshark, vous acquerrez une compréhension intuitive des protocoles réseau et des motifs de trafic, améliorant ainsi vos capacités globales en cybersécurité.

> Pour pratiquer les opérations de ce tutoriel, essayez le laboratoire pratique interactif : [Analyser le trafic réseau avec les filtres d'affichage de Wireshark](https://labex.io/labs/wireshark-analyze-network-traffic-with-wireshark-display-filters-415944?course=quick-start-with-wireshark)