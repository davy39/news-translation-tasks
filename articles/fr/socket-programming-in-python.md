---
title: Qu'est-ce que la programmation de sockets en Python ?
subtitle: ''
author: P S Mohammed Ali
co_authors: []
series: null
date: '2023-05-25T14:25:40.000Z'
originalURL: https://freecodecamp.org/news/socket-programming-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/ab_networks_network_8uds-1030x438-1.jpg
tags:
- name: computer network
  slug: computer-network
- name: Python
  slug: python
seo_title: Qu'est-ce que la programmation de sockets en Python ?
seo_desc: 'In this article, you will learn how to code a socket program in Python.
  But before that, let''s understand what a socket is and where you might use it.

  We can define a socket as a quick connection which allows the transmission of data
  between two proc...'
---

Dans cet article, vous apprendrez à coder un programme de socket en Python. Mais avant cela, comprenons ce qu'est un socket et où vous pourriez l'utiliser.

Nous pouvons définir un socket comme une connexion rapide qui permet la transmission de données entre deux processus sur la même machine ou sur des machines différentes via un réseau. Il est couramment utilisé dans l'interaction client-serveur, car les sockets permettent aux applications de communiquer en utilisant les mécanismes intégrés du matériel et du système d'exploitation.

De nombreux logiciels les plus utilisés aujourd'hui - y compris les navigateurs web, les logiciels de partage de fichiers et les applications de messagerie instantanée des réseaux sociaux comme WhatsApp et autres - dépendent fondamentalement du concept de sockets.

Habituellement, un programme de socket est composé de deux programmes principaux appelés le client et le serveur. Ici, le **client agit comme le demandeur**, où il demande certaines données. Le **serveur agit comme l'écouteur** et fournit au client les données demandées en réponse.

En Python, créer un programme client et serveur est une tâche simple, car Python dispose de nombreux modules intégrés pour aider à cela.

## Comment coder le serveur

Tout d'abord, codons notre programme serveur. Pour garder cela simple, supposons que le serveur écoute l'hôte sur un port particulier. Quelles que soient les données qu'il reçoit, il les imprime simplement et envoie quelques lettres ASCII aléatoires en réponse.

```python
# server.py
# Importation des modules intégrés nécessaires
import socket
import random
import string

# Création d'une instance de socket
server_object = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# Connexion au localhost
ip_address = '127.0.0.1'
port = 5555
server_object.bind((ip_address, port))
server_object.listen()

# Une fois que le client se connecte au port particulier, le serveur commence à accepter la demande.
connection_object, _ = server_object.accept()


if connection_object:
	# Connecté au client avec succès
    print("SERVEUR CONNECTÉ AU CLIENT")
    
    # Envoi du message initial au client
    connection_object.send(b"type the message")
    
    # Réception du message du client
    data_receive = connection_object.recv(1024)
    
    while data_receive != b'stop':
        print("{}: {}".format("MESSAGE DU CLIENT: ", data_receive.decode('utf-8')))
        server_input = random.choice(string.ascii_letters)
        connection_object.send(server_input.encode('utf-8'))
        data_receive = connection_object.recv(1024)
```

Dans le code ci-dessus, nous avons créé une instance de socket pour le serveur. Vous pouvez voir que `family=socket.AF_INET` définit la famille d'adresses que ce socket peut accepter - uniquement les adresses IPv4. Et `type=socket.SOCK_STREAM` définit que le socket n'accepte que les connexions TCP (Transmission Control Protocol).

Pour que l'instance de socket serveur écoute et accepte les demandes, elle a besoin d'une adresse IP et d'un port. Nous avons donc `ip_address = '127.0.0.1'` et `port = 5555`. Ici, nous avons localhost comme adresse IP car le serveur et le client résident sur la même machine.

À l'étape suivante, l'instance serveur `server_object` établit (lie) une adresse afin que les clients puissent l'utiliser pour trouver le serveur. La méthode `bind((ip_address,port))` attribue une adresse IP locale et un numéro de port à cette instance `server_object` explicitement car les programmes serveur écoutent sur le port publié `port`. Un port et une adresse IP locale doivent être attribués.

Il commence ensuite à écouter activement sur ce port particulier. Lorsque le client se connecte à ce port depuis le côté client, l'instance serveur accepte la demande de connexion du client. Il crée ensuite un nouvel `connection_object` et le retourne à l'instance serveur.

Cet `connection_object` contient toutes les informations nécessaires sur le client et le serveur. Maintenant, nous utilisons cet `connection_object` pour envoyer un message du serveur au client. Nous imprimons donc un message `SERVEUR CONNECTÉ AU CLIENT` si le `connection_object` est créé avec succès.

Une fois que le `connection_object` est créé, l'instance envoie un message initial `type the message` en octets au client et reçoit la demande du client.

Dans la boucle `while`, l'instance de connexion `connection_object` imprime le message du client. Ensuite, en réponse, il envoie des lettres ASCII aléatoires et attend la demande du client. Cette boucle `while` s'exécutera dans le programme serveur jusqu'à ce que le client envoie le message de demande `stop`.

## Comment coder le client

Jusqu'à présent, nous avons vu le code côté serveur. Maintenant, codons le côté client qui est assez simple.

```python
# client.py

# importation du module socket
import socket

# création de l'instance socket
client_object = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# adresse IP cible et port
ip_address = '127.0.0.1'
port = 5555

# instance demandant une connexion à l'adresse et au port spécifiés
client_object.connect((ip_address,port))

# réception de la réponse du serveur
data_receive = client_object.recv(1024)

# si la réponse n'est pas nulle
if data_receive:
	# La connexion est réussie
    print("CLIENT CONNECTÉ AU SERVEUR")
    print(data_receive.decode('utf-8'))
    
    
    while data_receive:
    	# entrée utilisateur
        client_input = input().encode('utf-8')
        
        # envoi de la demande au serveur
        client_object.send(client_input)
        
        # réception de la réponse du serveur
        data_receive = client_object.recv(1024)
        if data_receive:
            print("{}: {}".format("SERVEUR",data_receive.decode('utf-8')))
```

Dans le code côté client, nous avons créé une instance de socket similaire `client_object`, l'adresse IP cible `ip_address` et le `port`, tout comme nous l'avons créé dans le programme côté serveur.

L'étape suivante consiste à utiliser l'instance `client_object` et à se connecter à l'adresse cible et au port respectifs en utilisant la méthode `connect()`.

Une fois la connexion réussie et que le `connection_object` est créé côté serveur, le serveur envoie la réponse `type the message` qui est stockée dans `data_receive` côté client.

Puisque le serveur a envoyé le message, nous utilisons ce message pour confirmer que la connexion est réussie. Nous imprimons donc `CLIENT CONNECTÉ AU SERVEUR` puis le message envoyé par le serveur `type the message`.

Dans la boucle `while`, nous donnons d'abord l'entrée dans une chaîne en utilisant la fonction intégrée `input()`. Ensuite, nous la convertissons en octets en utilisant la méthode `encode('utf-8')` et la stockons dans `client_input` (car les données ne peuvent être envoyées qu'en octets). Nous envoyons ensuite le `client_input` au serveur en utilisant `client_object.send(client_input)`.

Nous recevons les données de réponse du serveur après avoir envoyé la demande au serveur. Le serveur acceptera et donnera une réponse au client jusqu'à ce que l'utilisateur tape `stop` comme demande au serveur.

**Note :** Nous devons d'abord exécuter le programme serveur puis le programme client car lorsque le client souhaite se connecter à la cible, il doit y avoir un serveur à l'écoute, opérationnel.

Voici l'exécution de `server.py` puis de `client.py` :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/ff.PNG align="left")

*Côté gauche : Programme serveur, Côté droit : Programme client*

Comme vous pouvez le voir, une fois l'exécution démarrée, le serveur a affiché `SERVEUR CONNECTÉ AU CLIENT` pour que l'utilisateur sache qu'il fonctionne et a envoyé le message initial au client.

Du côté client, lorsque le client a reçu le message, il a affiché `CLIENT CONNECTÉ AU SERVEUR` et a également imprimé `type the message` reçu du client.

Puisque le client attend l'entrée de l'utilisateur, une fois que l'utilisateur a saisi l'entrée, il l'envoie au serveur et le serveur imprime le message du client. Il a ensuite envoyé la lettre ASCII aléatoire en réponse au client.

Le flux a bouclé jusqu'à ce que le client envoie le message `stop` comme demande au serveur. Une fois que le serveur a reçu la demande `stop`, il a terminé la session socket.

## Conclusion

Dans ce tutoriel, nous avons compris que le socket est l'une des technologies les plus fondamentales de la mise en réseau informatique et nous avons appris comment configurer un programme de socket en Python en utilisant le module socket dans les programmes côté client et côté serveur.