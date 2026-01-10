---
title: Comment construire un système de chat sécurisé simple en utilisant Netcat
subtitle: ''
author: Hang Hu
co_authors: []
series: null
date: '2024-10-24T13:18:08.419Z'
originalURL: https://freecodecamp.org/news/build-a-simple-secure-chat-system-with-netcat
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1729729356682/acf8ca42-3aaa-4ca1-9ebc-10f0f658c678.png
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Linux
  slug: linux
- name: Netcat
  slug: netcat
- name: shell
  slug: shell
- name: Ubuntu
  slug: ubuntu
seo_title: Comment construire un système de chat sécurisé simple en utilisant Netcat
seo_desc: 'In this hands-on tutorial, you''ll learn how to harness the power of Netcat
  to build practical networking tools.

  We’ll start with basic message transmission. Then you''ll progress to creating a
  file transfer system, and you’ll ultimately develop a secu...'
---

Dans ce tutoriel pratique, vous apprendrez à exploiter la puissance de Netcat pour construire des outils de mise en réseau pratiques.

Nous commencerons par la transmission de messages de base. Ensuite, vous progresserez vers la création d'un système de transfert de fichiers, et vous développerez finalement une application de chat sécurisée avec chiffrement.

Voici ce que nous allons couvrir :

* [Prérequis](#heading-prerequisites)

* [Installer Netcat](#heading-installation-netcat)

* [Votre première connexion réseau](#heading-votre-premiere-connexion-reseau)

* [Comment construire un outil de transfert de fichiers simple](#heading-comment-construire-un-outil-de-transfert-de-fichiers-simple)

* [Comment créer un système de chat sécurisé](#heading-comment-creer-un-systeme-de-chat-securise)

* [Conclusion](#heading-conclusion)

* [Pratiquez vos compétences](#heading-pratiquez-vos-competences)

## Prérequis

Avant de commencer, vous aurez besoin de :

* Un système basé sur Linux : je recommande Ubuntu. Alternativement, vous pouvez utiliser le [Terminal Linux en ligne](https://labex.io/tutorials/linux-online-linux-playground-372915) si vous n'avez pas Linux installé.

* Des connaissances de base du terminal (comment utiliser `cd` et `ls`)

Ne vous inquiétez pas si vous êtes nouveau dans le domaine de la mise en réseau - je vais tout expliquer au fur et à mesure !

## **Installer Netcat**

[Netcat](https://nc110.sourceforge.io/) est comme un "tuyau" numérique entre ordinateurs - tout ce que vous mettez à une extrémité sort à l'autre. Avant de commencer à l'utiliser, installons-le sur votre système.

Ouvrez votre terminal et exécutez ces commandes :

```bash
# Mettre à jour la liste des paquets de votre système
sudo apt update

# Installer Netcat
sudo apt install netcat -y
```

![Mettre à jour la liste des paquets de votre système](https://cdn.hashnode.com/res/hashnode/image/upload/v1729583277378/d5fb06c5-3163-4885-b163-2cdde4fa434b.png align="center")

Pour vérifier si l'installation a fonctionné, exécutez :

```bash
nc -h
```

Vous devriez voir un message commençant par "OpenBSD netcat". Si c'est le cas, c'est parfait ! Sinon, essayez de réexécuter les commandes d'installation.

![vérifier si l'installation a fonctionné](https://cdn.hashnode.com/res/hashnode/image/upload/v1729583329155/812f32b9-2ca7-41f6-aead-07ffacbf161c.png align="center")

## **Votre première connexion réseau**

Avant de plonger dans la construction d'outils, comprenons ce qu'est réellement une connexion réseau. Pensez-y comme à un appel téléphonique : une personne doit attendre l'appel (l'auditeur), et une autre personne doit passer l'appel (le connecteur).

En réseau, nous utilisons des "ports" pour établir ces connexions. Vous pouvez penser aux ports comme à différentes lignes téléphoniques - ils permettent à plusieurs conversations d'avoir lieu en même temps.

Essayons d'établir notre première connexion :

1. Ouvrez une fenêtre de terminal et créez un auditeur :

```bash
nc -l 12345
```

Qu'avons-nous fait ? Le `-l` indique à Netcat d'"écouter" une connexion, et `12345` est le numéro de port que nous avons choisi. Votre terminal semblera gelé - c'est normal ! Il attend que quelqu'un se connecte.

2. Ouvrez une autre fenêtre de terminal et connectez-vous à votre auditeur :

```bash
nc localhost 12345
```

Ici, `localhost` signifie "cet ordinateur" - nous nous connectons à nous-mêmes pour nous entraîner. Si vous souhaitez vous connecter à un autre ordinateur, vous pouvez remplacer `localhost` par son adresse IP.

Essayez maintenant de taper un message (comme "salut") dans l'une ou l'autre fenêtre et appuyez sur Entrée. Cool, non ? Le message apparaît dans l'autre fenêtre ! C'est exactement ainsi que fonctionne la communication réseau de base.

![établir notre première connexion](https://cdn.hashnode.com/res/hashnode/image/upload/v1729583496294/da70a4bc-5626-493c-8a52-385b708593f4.png align="center")

Pour arrêter la connexion, appuyez sur `Ctrl+C` dans les deux fenêtres.

### **Que vient-il de se passer ?**

Vous venez de créer votre première connexion réseau ! Le premier terminal était comme quelqu'un attendant près d'un téléphone, et le deuxième terminal était comme quelqu'un appelant ce téléphone. Lorsqu'ils se sont connectés, ils pouvaient s'envoyer des messages.

## **Comment construire un outil de transfert de fichiers simple**

Maintenant que nous comprenons les connexions de base, construisons quelque chose de plus utile : un outil pour transférer des fichiers entre ordinateurs.

Tout d'abord, créons un fichier de test à envoyer :

```bash
# Créer un fichier avec du contenu
echo "Ceci est mon message secret" > secret.txt
```

Pour transférer ce fichier, nous aurons besoin de deux terminaux à nouveau, mais cette fois nous les utiliserons différemment :

1. Dans le premier terminal, configurez le récepteur :

```bash
nc -l 12345 > received_file.txt
```

![transférer un fichier](https://cdn.hashnode.com/res/hashnode/image/upload/v1729583969994/d3159a2f-37f7-4cab-a23b-3788ed85876f.png align="center")

Cela indique à Netcat de :

* Écouter une connexion (`-l`)

* Enregistrer tout ce qu'il reçoit dans un fichier appelé `received_file.txt` (`>`)

2. Dans le deuxième terminal, envoyez le fichier :

```bash
nc localhost 12345 < secret.txt
```

![envoyer le fichier](https://cdn.hashnode.com/res/hashnode/image/upload/v1729583998676/ab865ded-626a-47aa-9df6-83e56aa5f5d1.png align="center")

Le `<` indique à Netcat d'envoyer le contenu de notre fichier.

3. Appuyez sur Ctrl+C dans les deux terminaux pour arrêter le transfert. Ensuite, vérifiez si cela a fonctionné :

```bash
cat received_file.txt
```

![fichier reçu](https://cdn.hashnode.com/res/hashnode/image/upload/v1729584030360/32fa9916-ffdb-49da-abcf-57569c9b2f79.png align="center")

Vous devriez voir votre message !

Cela ressemble à notre système de chat, mais au lieu de taper des messages, nous :

1. Prenons le contenu d'un fichier

2. L'envoyons à travers notre connexion réseau

3. Le sauvegardons dans un nouveau fichier à l'autre extrémité

Pensez-y comme à l'envoi d'un document par fax !

## **Comment créer un système de chat sécurisé**

Dans nos exemples précédents, tout était envoyé en texte clair - n'importe qui pouvait le lire s'il interceptait la connexion. Rendons cela plus sécurisé en ajoutant du chiffrement.

Tout d'abord, comprenons ce que fait le chiffrement :

* C'est comme mettre votre message dans une boîte verrouillée

* Seule une personne avec la bonne clé peut l'ouvrir

* Même si quelqu'un voit la boîte, il ne peut pas lire votre message

Nous allons créer deux scripts : un pour envoyer des messages et un pour les recevoir.

1. Créez le script de l'expéditeur :

```bash
nano secure_sender.sh
```

Copiez ce code dans le fichier :

```bash
#!/bin/bash

echo "Chat sécurisé - Tapez vos messages ci-dessous"
echo "Appuyez sur Ctrl+C pour quitter"

while true; do
  # Obtenir le message
  read message
  
  # Chiffrer et l'envoyer
  echo "$message" | openssl enc -aes-256-cbc -salt -base64 \
    -pbkdf2 -pass pass:chatpassword 2>/dev/null | \
    nc -N localhost 12345
done
```

Ce script va :

1. Lire les messages à partir de l'entrée utilisateur.

2. Les chiffrer en utilisant le chiffrement AES-256-CBC d'OpenSSL (une norme de chiffrement forte).

3. Envoyer le message chiffré au port spécifié.

Appuyez sur Ctrl+X, puis Y, puis Entrée pour sauvegarder.

![Créer le script de l'expéditeur](https://cdn.hashnode.com/res/hashnode/image/upload/v1729584825701/bcd3c3fb-5cd5-40f7-8105-14d1fff069ec.png align="center")

2. Créez le script du récepteur :

```bash
nano secure_receiver.sh
```

Copiez ce code :

```bash
#!/bin/bash

echo "En attente de messages..."

while true; do
  # Recevoir et déchiffrer les messages
  nc -l 12345 | openssl enc -aes-256-cbc -d -salt -base64 \
    -pbkdf2 -pass pass:chatpassword 2>/dev/null
done
```

Ce script va :

1. Écouter les messages entrants chiffrés.

2. Les déchiffrer en utilisant la même clé de chiffrement.

3. Afficher les messages déchiffrés.

Sauvegardez ce fichier également.

![Créer le script du récepteur](https://cdn.hashnode.com/res/hashnode/image/upload/v1729584787785/c1e329ad-cbbe-49e8-918f-25d683884972.png align="center")

3. Rendez les deux scripts exécutables :

```bash
chmod +x secure_sender.sh secure_receiver.sh
```

4. Essayez-le :

* Dans un terminal : `./secure_receiver.sh`

* Dans un autre terminal : `./secure_sender.sh`

Tapez un message dans le terminal de l'expéditeur. Le récepteur affichera votre message déchiffré !

![Tapez un message dans le terminal de l'expéditeur](https://cdn.hashnode.com/res/hashnode/image/upload/v1729584834464/1f902a94-3a79-404b-bc9f-af9d8d2471e0.png align="center")

### **Améliorer notre système de chat**

Maintenant que nous avons un système de chat de base fonctionnel, rendons-le plus convivial et informatif. Nous ajouterons des fonctionnalités comme des horodatages, des messages codés par couleur et des mises à jour de statut de chiffrement. Cette version améliorée vous aidera à mieux comprendre ce qui se passe pendant le processus de chiffrement et de transmission.

Si vous êtes à l'aise avec la version de base, essayez cette version améliorée :

1. Créez un script d'expéditeur amélioré (enregistrez-le sous `secure_sender_v2.sh`) :

```bash
#!/bin/bash

# Configurer les codes de couleur pour une meilleure visibilité
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${GREEN}Expéditeur de chat sécurisé - Démarré à $(date)${NC}"
echo -e "${BLUE}Tapez vos messages ci-dessous. Appuyez sur Ctrl+C pour quitter${NC}"
echo "----------------------------------------"

while true; do
    # Afficher l'invite avec l'horodatage
    echo -ne "${GREEN}[$(date +%H:%M:%S)]${NC} Votre message : "
    
    # Obtenir le message
    read message
    
    # Sauter si le message est vide
    if [ -z "$message" ]; then
        continue
    fi
    
    # Ajouter l'horodatage au message
    timestamped_message="[$(date +%H:%M:%S)] $message"
    
    # Afficher le statut du chiffrement
    echo -e "${BLUE}Chiffrement et envoi du message...${NC}"
    
    # Chiffrer et envoyer le message, en affichant la forme chiffrée
    encrypted=$(echo "$timestamped_message" | openssl enc -aes-256-cbc -salt -base64 \
        -pbkdf2 -iter 10000 -pass pass:chatpassword 2>/dev/null)
    
    echo -e "${BLUE}Forme chiffrée :${NC} ${encrypted:0:50}..." # Afficher les 50 premiers caractères
    echo "$encrypted" | nc -N localhost 12345
    
    echo -e "${GREEN}Message envoyé avec succès !${NC}"
    echo "----------------------------------------"
done
```

2. Créez un script de récepteur amélioré (enregistrez sous `secure_receiver_v2.sh`) :

```bash
#!/bin/bash

# Configurer les codes de couleur pour une meilleure visibilité
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}Récepteur de chat sécurisé - Démarré à $(date)${NC}"
echo -e "${BLUE}En attente de messages... Appuyez sur Ctrl+C pour quitter${NC}"
echo "----------------------------------------"

while true; do
    # Recevoir et afficher le message chiffré
    echo -e "${BLUE}En attente du prochain message...${NC}"
    
    encrypted=$(nc -l 12345)
    
    # Sauter si rien n'a été reçu
    if [ -z "$encrypted" ]; then
        continue
    fi
    
    echo -e "${YELLOW}Message chiffré reçu :${NC} ${encrypted:0:50}..." # Afficher les 50 premiers caractères
    echo -e "${BLUE}Déchiffrement...${NC}"
    
    # Déchiffrer et afficher le message
    decrypted=$(echo "$encrypted" | openssl enc -aes-256-cbc -d -salt -base64 \
        -pbkdf2 -iter 10000 -pass pass:chatpassword 2>/dev/null)
    
    # Vérifier si le déchiffrement a réussi
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}Message déchiffré :${NC} $decrypted"
    else
        echo -e "\033[0;31mErreur : Échec du déchiffrement du message${NC}"
    fi
    
    echo "----------------------------------------"
done
```

3. Rendez les scripts améliorés exécutables :

```bash
chmod +x secure_sender_v2.sh secure_receiver_v2.sh
```

Essayez d'exécuter les deux versions pour voir comment les commentaires supplémentaires vous aident à mieux comprendre le processus de chiffrement et de communication.

![Améliorer notre système de chat](https://cdn.hashnode.com/res/hashnode/image/upload/v1729585592733/01d25154-37a9-4c14-95ac-410c513956b9.png align="center")

La version améliorée (v2) apporte plusieurs améliorations :

* Sortie colorisée pour une meilleure lisibilité.

* Horodatages pour chaque message.

* Mises à jour de statut montrant le processus de chiffrement/déchiffrement.

* Gestion des erreurs pour les tentatives de déchiffrement échouées.

* Aperçu des messages chiffrés avant l'envoi/après la réception.

## Conclusion

Ce tutoriel vous a appris à utiliser Netcat comme un outil de mise en réseau polyvalent. Nous avons commencé par l'envoi de messages de base, progressé vers la construction d'un système de transfert de fichiers simple, puis créé un système de chat sécurisé avec chiffrement.

Vous avez acquis une expérience pratique avec :

* La configuration d'auditeurs et de connexions réseau

* Le transfert de fichiers de manière sécurisée entre systèmes

* La mise en œuvre du chiffrement de base pour une communication sécurisée

* L'ajout de fonctionnalités conviviales comme les horodatages et les mises à jour de statut

Les compétences que vous avez acquises ici constituent une base solide pour comprendre la communication réseau et peuvent être appliquées à des projets de mise en réseau plus complexes. Pour pratiquer les opérations de ce tutoriel, essayez [le laboratoire pratique interactif](https://labex.io/labs/linux-using-netcat-for-simple-network-communication-392039).

## **Pratiquez vos compétences**

Maintenant que vous avez appris les bases de Netcat et construit un système de chat sécurisé, mettons vos compétences à l'épreuve avec un scénario réel. Essayez le défi de laboratoire "[**Recevoir des messages en utilisant Netcat**](https://labex.io/labs/linux-receive-messages-using-netcat-392102)" où vous jouerez le rôle d'un analyste junior des communications interstellaires. Votre mission : intercepter et journaliser les signaux d'une civilisation extraterrestre en utilisant vos nouvelles connaissances sur Netcat.