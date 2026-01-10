---
title: Comment identifier les problèmes Internet de base avec la commande Ping
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-21T23:47:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-identify-basic-internet-problems-with-ping
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c73740569d1a4ca324c.jpg
tags:
- name: internet
  slug: internet
- name: Problem Solving
  slug: problem-solving
- name: toothbrush
  slug: toothbrush
seo_title: Comment identifier les problèmes Internet de base avec la commande Ping
seo_desc: "Next time you call your help desk, do you want to wow them with your networking\
  \ knowledge? Using a command called “ping”, built right into your existing Mac,\
  \ Windows, or Linux computer, will help identify basic connection problems. \nOkay,\
  \ this might ..."
---

La prochaine fois que vous appelerez votre service d'assistance, souhaitez-vous les impressionner avec vos connaissances en réseau ? L'utilisation d'une commande appelée « ping », intégrée directement dans votre Mac, Windows ou Linux existant, vous aidera à identifier les problèmes de connexion de base. 

D'accord, cela ne suffira peut-être pas à impressionner vos collègues, mais ils apprécieront que vous ayez commencé le processus de débogage. Et n'oubliez pas que votre personnel de support est spécialisé dans le débogage, alors suivez leurs instructions lorsqu'ils vous guident à travers la séquence de dépannage.

## **TL;DR :**

Vous pouvez utiliser la commande `ping` intégrée dans votre Mac OS X, Windows ou Linux pour identifier les problèmes de connectivité réseau de base. Cela peut vous aider à résoudre le problème et/ou à obtenir des informations de débogage précieuses comme première étape avant d'appeler le support. 

Lisez ci-dessous pour obtenir des détails sur la façon de lancer une fenêtre de ligne de commande et d'exécuter `ping` depuis votre Mac OS X ou votre machine Windows.

## **La commande `ping` :**

La commande `ping` est un moyen simple de vérifier qu'un autre ordinateur peut recevoir des informations de votre part. L'auteur original, [Mike Muuss](https://en.wikipedia.org/wiki/Mike_Muuss), a en fait [nommé le programme d'après le son « ping »](https://en.wikipedia.org/wiki/Ping_%28networking_utility%29#History) qu'un sous-marin envoie pour détecter des objets dans l'eau. Si un écho du ping revient, cela signifie qu'il y a quelque chose là-bas. En fait, `ping` utilise la « [Internet Control Message Protocol Echo Request](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol) » comme partie de sa conception logicielle sous-jacente.

Dans sa forme la plus simple, la commande `ping` fournit deux informations précieuses : si le message a été renvoyé (`64 bytes from…`) et combien de temps il faut pour recevoir le message en retour (par exemple, `time=6.396 ms`). 

Selon le type d'ordinateur que vous utilisez, vous pouvez même obtenir un résumé contenant le minimum, le maximum, la moyenne et plus encore. 

Le temps de réponse est indiqué en « ms », ou milliseconde, soit 1/1000ème de seconde. Un temps de réponse de 10 ms ou moins est assez rapide, mais les valeurs sont souvent dans la plage des 100 ms. Au-dessus de 200 ms, vous remarquerez probablement que votre connexion est lente.

## **Quand tout va bien :**

Voici à quoi ressemble ma réponse `ping` sur mon ordinateur Mac OS X lorsque tout fonctionne normalement ici en Malaisie :

```text
MacBook-Pro:~ ajm$ ping Google.com
PING google.com (216.58.196.46): 56 data bytes
64 bytes from 216.58.196.46: icmp\_seq=0 ttl=55 time=6.396 ms
64 bytes from 216.58.196.46: icmp\_seq=1 ttl=55 time=6.368 ms
64 bytes from 216.58.196.46: icmp\_seq=2 ttl=55 time=26.773 ms
64 bytes from 216.58.196.46: icmp\_seq=3 ttl=55 time=6.984 ms
^C
--- google.com ping statistics ---
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 6.368/11.630/26.773/8.746 ms
```

Voici à quoi ressemble ma réponse `ping` sur un ordinateur Windows lorsque tout fonctionne bien :

```text
C:\Users\BJM>ping Google.com
Pinging google.com [216.58.196.46] with 32 bytes of data:
Reply from 216.58.196.46: bytes=32 time=6ms TTL=128
Reply from 216.58.196.46: bytes=32 time=15ms TTL=128
Reply from 216.58.196.46: bytes=32 time=6ms TTL=128
Reply from 216.58.196.46: bytes=32 time=6ms TTL=128
Ping statistics for 216.58.196.46:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 6ms, Maximum = 15ms, Average = 8ms
```

Vous pouvez voir dans ces exemples que la connexion est assez bonne avec des temps de réponse moyens inférieurs à 10 ms.

### **Quand quelque chose ne va pas (trois exemples) :**

Alors, que se passerait-il si je ne pouvais pas me connecter à `Google.com` ? Pour l'exemple #1, je simule une connexion réseau rompue sur mon Mac en débranchant mon routeur de la prise, et je relance la commande. La première chose que je remarque, c'est qu'il faut beaucoup plus de temps pour que la commande réponde :

```text
MacBook-Pro:~ ajm$ ping google.com
ping: cannot resolve google.com: Unknown host
MacBook-Pro:~ ajm$
```

Ou, pour l'exemple #2, selon la manière dont la connexion échoue :

```text
PING google.com (216.58.196.46): 56 data bytes
Request timeout for icmp\_seq 0
Request timeout for icmp\_seq 1
Request timeout for icmp\_seq 2
^C
```

Et parfois, si j'ai une connexion particulièrement instable, je verrai un mélange de ces messages. Pour l'exemple #3, je peux simuler cela en connectant mon ordinateur Mac à une connexion Wi-Fi publique qui se trouve de l'autre côté de la rue :

```text
PING google.com (216.58.196.206): 56 data bytes
64 bytes from 216.58.196.206: icmp\_seq=0 ttl=57 time=273.655 ms
64 bytes from 216.58.196.206: icmp\_seq=1 ttl=57 time=808.546 ms
64 bytes from 216.58.196.206: icmp\_seq=2 ttl=57 time=179.613 ms
Request timeout for icmp\_seq 3
Request timeout for icmp\_seq 4
64 bytes from 216.58.196.206: icmp\_seq=5 ttl=57 time=374.612 ms
Request timeout for icmp\_seq 6
ping: sendto: No route to host
Request timeout for icmp\_seq 7
ping: sendto: No route to host
Request timeout for icmp\_seq 8
^C
```

Dans le premier test, `ping` m'a indiqué que ma machine ne pouvait même pas trouver l'adresse Internet (IP `216.58.196.46`) pour `Google.com`. Dans le deuxième test, mon ordinateur se souvenait de l'adresse IP de Google, mais ne pouvait pas atteindre les serveurs Google (`Request timeout`). Dans le troisième test, `sendto: No route to host` signifie que le périphérique réseau sait où se trouvent les serveurs Google, mais que quelque chose le long du chemin numérique est rompu.

## **Utilisateurs Mac : Comment exécuter la commande `ping` :**

Sur un Mac, vous exécutez généralement `ping` depuis la ligne de commande du terminal. Pour démarrer le terminal, cliquez sur l'icône de la loupe Spotlight OS X dans le coin supérieur droit du bureau :

![Mac Spotlight](https://discourse-user-assets.s3.amazonaws.com/original/2X/9/924e9346b5f92fe41127f6b3e403f454773edae9.png)

Lorsque la fenêtre de recherche apparaît, tapez « terminal », surlignez « Terminal – Utilitaires » et double-cliquez (ou appuyez sur

return

) :

![Mac Terminal Launch](https://discourse-user-assets.s3.amazonaws.com/original/2X/9/976e1fb628c0d0bf2a6a9b57504305fd844716d4.png)

Cela lancera la fenêtre de commande du terminal, et vous pourrez entrer la commande `ping Google.com` montrée dans mes exemples :

![Mac Command Line](https://discourse-user-assets.s3.amazonaws.com/original/2X/0/05d1e4d360c14921f7bd7ab871358b956f1e7d03.png)

**Conseil important pour Mac** : La commande `ping` s'exécutera indéfiniment si vous ne lui dites pas de s'arrêter. Pour cela, appuyez sur la touche

`control`

(lower right on keyboard) et la touche

`c`

. Cela interrompra le test avec un Control-C (`^C`) et rendra le contrôle de la ligne de commande. Pour les utilisateurs Windows, la commande s'arrêtera d'elle-même après quelques itérations.

## **Utilisateurs Windows : Comment exécuter la commande `ping` :**

L'ouverture de l'invite de commande diffère entre les versions Windows 10, 8.1, 8 et 7 ; voici un excellent guide sur [Comment ouvrir l'invite de commande](http://pcsupport.about.com/od/commandlinereference/f/open-command-prompt.htm). Sur une machine Windows 7, par exemple, cliquez sur l'icône Windows « Démarrer » en bas à gauche, et sélectionnez « Invite de commande » et double-cliquez (ou appuyez sur

`enter`

) :

![Win Terminal Launch](https://discourse-user-assets.s3.amazonaws.com/original/2X/4/4e0b18755930ad0d64e6e38763f0b96054fd76fb.png)

Cela lancera la fenêtre de commande, et vous pourrez entrer la commande `ping Google.com` montrée dans les exemples :

![Win Command Line](https://discourse-user-assets.s3.amazonaws.com/original/2X/9/94d8ed91d29574497ad0f2eb2cd235050132851e.png)

Maintenant que vous savez comment utiliser la commande `ping`, vous pouvez effectuer un dépannage de base de votre connexion réseau. Avec un peu de créativité, vous pouvez travailler avec votre personnel de support informatique local ou vos connaissances sur la topologie de votre réseau et votre adresse IP (par exemple, `ping` le routeur, `ping` votre FAI) pour identifier davantage les problèmes de réseau.