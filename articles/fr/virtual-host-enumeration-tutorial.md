---
title: Énumération des hôtes virtuels – Comment découvrir des actifs web cachés
subtitle: ''
author: Nairuz Abulhul
co_authors: []
series: null
date: '2023-12-13T18:48:10.000Z'
originalURL: https://freecodecamp.org/news/virtual-host-enumeration-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/nicolas-houdayer-BeRXM0Edn5A-unsplash.jpg
tags:
- name: penetration testing
  slug: penetration-testing
seo_title: Énumération des hôtes virtuels – Comment découvrir des actifs web cachés
seo_desc: When performing external penetration testing or bug bounty hunting, security
  experts explore the targeted system from various angles to collect as much information
  as possible and identify potential attack vectors. This involves identifying all
  the a...
---

Lors de la réalisation de tests de pénétration externes ou de chasse aux bugs, les experts en sécurité explorent le système ciblé sous divers angles pour collecter autant d'informations que possible et identifier les vecteurs d'attaque potentiels. Cela implique d'identifier tous les actifs, domaines et sous-domaines disponibles.

Lors de la phase de reconnaissance des tests, les testeurs passent du temps sur l'énumération des hôtes virtuels, qui est le processus de découverte de tous les hôtes virtuels associés à une adresse IP ou un domaine particulier. Cela les aide à trouver des actifs cachés ou non documentés qui pourraient être vulnérables ou mal configurés. 

Par exemple, ils pourraient trouver un hôte virtuel accessible sans authentification. Cela pourrait entraîner un accès non autorisé à des données sensibles.

Dans cet article, nous discuterons des différentes façons d'énumérer les hôtes virtuels et de collecter des informations à leur sujet. Nous utiliserons l'exercice [HTB Academy](https://academy.hackthebox.com/) du module _"Information Gathering – Web Edition"_ pour démontrer les étapes d'énumération.

Notez que ce tutoriel est à des fins éducatives uniquement. N'utilisez pas ces informations pour faire du mal – utilisez-les pour le bien afin de rendre vos projets plus sécurisés.

## Table des matières

* [Aperçu de l'hébergement virtuel](#heading-hebergement-virtuel)  
– [Hébergement basé sur IP](#heading-hebergement-base-sur-ip)  
– [Hébergement basé sur le nom](#heading-hebergement-base-sur-le-nom)
* [Énumération des hôtes virtuels](#heading-enumeration-des-hotes-virtuels)  
– [Ffuf](#heading-ffuf)  
– [Gobuster](#heading-gobuster)  
– [Curl](#heading-curl)
* [Post-énumération](#heading-post-enumeration)  
– [hakcheckurl](#heading-hakcheckurl)  
– [Eyewitness](#heading-eyewitness)

## Prérequis

Avant de commencer à énumérer les hôtes virtuels, nous devons installer certains outils pour nous aider. La plupart de ces outils fonctionnent sur Linux, comme Ubuntu et Kali Linux :

* Ffuf
* Gobuster
* Eyewitness 
* hakcheckurl

Si vous ne les avez pas installés, je couvrirai les étapes ci-dessous.

## Aperçu de l'hébergement virtuel

L'hébergement virtuel est une fonctionnalité qui permet à un seul serveur web d'héberger plusieurs sites web et de les faire apparaître comme s'ils étaient hébergés sur des serveurs séparés et individuels. Cela est généralement fait pour réduire les frais généraux de ressources et les coûts de fonctionnement.

Il existe deux types d'hébergement virtuel : basé sur IP et basé sur le nom.

### **Hébergement basé sur IP**

Ce type d'hébergement implique la configuration d'un serveur web pour héberger plusieurs sites web sur un seul serveur. Chaque site hébergé est associé à une adresse IP unique, qui peut être dédiée ou partagée en fonction de la configuration d'hébergement.

Lorsque l'utilisateur tente d'accéder à un site web, le serveur écoute la demande, résout le nom d'hôte entrant en son adresse IP correspondante, puis achemine la demande vers le site web approprié en fonction de cette adresse IP.

Une fois que le serveur identifie le site web visé en fonction de cette adresse IP, il sert le contenu associé à ce site web à l'utilisateur.

### **Hébergement basé sur le nom**

Ce type d'hébergement implique la configuration d'un serveur web pour héberger plusieurs sites web sur une seule adresse IP en utilisant différents noms de domaine. Chaque site web hébergé est généralement associé à un nom d'hôte unique, mais plusieurs noms d'hôte peuvent être liés à un seul site web.

Lorsque l'utilisateur demande à accéder à un site web, le serveur vérifie l'en-tête **"Host"** dans la requête HTTP pour déterminer quel site web l'utilisateur essaie d'atteindre. En fonction du nom d'hôte fourni dans l'en-tête Host, le serveur identifie le site web spécifique et sert le contenu associé à ce site web à l'utilisateur.

## Énumération des hôtes virtuels

### Ffuf

Ffuf est un outil écrit en Go qui peut être installé sur Kali Linux en exécutant `sudo apt-get install ffuf` ou [téléchargé depuis GitHub](https://github.com/ffuf/ffuf). Cet outil vous permet de personnaliser vos approches de fuzzing.

Pour commencer à rechercher des hôtes virtuels, nous devons passer l'adresse IP de la cible en utilisant le drapeau `-u` et le nom de domaine associé avec le drapeau `-H`, qui fait référence à l'en-tête Host.

Ensuite, placez le mot FUZZ au début du domaine pour indiquer la position de fuzzing.

Nous pouvons utiliser différentes listes de mots pour identifier les hôtes virtuels avec le drapeau `-w`. Une liste de mots populaire est la liste [namelist](https://github.com/danielmiessler/SecLists/blob/master/Discovery/DNS/namelist.txt) dans les listes de mots SecLists, tandis qu'une autre est la liste de mots [Kiterunner](https://wordlists.assetnote.io/) dans Assetnotes. 

```bash
ffuf -w namelist.txt -u http://10.129.184.109 -H "HOST: FUZZ.inlanefreight.htb".
```

Le fuzzing peut générer de nombreux résultats qui sont parfois difficiles à identifier comme valides ou invalides. Filtrer les résultats peut vous faire gagner du temps en triant la sortie. 

Vous pouvez filtrer une taille de réponse ou une liste de tailles en utilisant des virgules pour les séparer avec le drapeau `-fs` — comme `-fs 109, 208,`, et ainsi de suite.

```bash
fuf -w namelist.txt -u http://10.129.184.109 -H "HOST: FUZZ.inlanefreight.htb" -fs 10918
```

![Figure 01 – Montre Ffuf trouvant des hôtes virtuels avec les listes de mots fournies. r3d-buck3t.com](https://miro.medium.com/v2/resize:fit:770/1*LPtY56sezItdqxJjkmy7BQ.png)
_Figure 01 – Montre Ffuf trouvant des hôtes virtuels avec les listes de mots fournies._

Après la fin du fuzzing, nous sauvegardons la sortie dans un fichier. Ensuite, nous pouvons utiliser l'utilitaire `grep` pour rechercher dans le résultat les lignes qui contiennent le mot "FUZZ" dans le texte. Ci-dessous un exemple d'utilisation de grep pour trouver les lignes avec les sous-domaines identifiés.

```bash
cat vhosts | grep 

FUZZFUZZ:ap
FUZZ:app
FUZZ:citrix
```

Ensuite, nous pouvons rediriger la sortie de grep avec l'utilitaire `awk` pour extraire uniquement les sous-domaines identifiés en utilisant la commande print, suivie d'un signe dollar et du numéro de colonne. Cette commande entière peut être écrite en une ligne.

```bash
cat vhosts | grep FUZZ | awk '{print $3}'
```

En utilisant un court script bash, nous ajoutons notre nom de domaine original aux sous-domaines identifiés, comme vu dans la Figure 02.

```bash
for i in $(cat vhost1); do echo $i.inlanefreight.htb ; done > vhost1
```

![Figure 02 – Montre la sortie bash utilisée pour ajouter le nom de domaine aux sous-domaines. r3d-buck3t.com](https://miro.medium.com/v2/resize:fit:770/1*eTXWrUXGmHSwxhSw-kOW1w.png)
_Figure 02 – Montre la sortie bash utilisée pour ajouter le nom de domaine aux sous-domaines._

### Gobuster

Une autre façon d'énumérer les hôtes virtuels est avec l'outil Gobuster en utilisant l'option vhost. L'outil peut être installé sur Kali en exécutant `sudo apt-get install gobuster` ou [téléchargé depuis GitHub](https://github.com/OJ/gobuster).

Pour commencer le processus d'énumération, nous devons d'abord fournir l'adresse IP en utilisant le drapeau `-u` et spécifier une liste de mots avec le drapeau `-w`. Après cela, nous définissons le nom de domaine et la position où le fuzzing commence.

Dans Gobuster, nous définissons ces informations dans un fichier texte, appelé fichier de motif, qui est passé avec le drapeau `-p`. Vous pouvez voir un exemple de fichier de motif dans la Figure 03 ci-dessous. 

```bash
{GOBUSTER}.inlanefreight.htb
```

![Figure 03 montre le fichier de motif qui spécifie où commencer le fuzzing avec Gobuster. r3d-buck3t.com](https://miro.medium.com/v2/resize:fit:770/1*Lyysphn9mPs0YZtiKlcmzQ.png)
_Figure 03 montre le fichier de motif qui spécifie où commencer le fuzzing avec Gobuster._

Pour filtrer la sortie, nous utilisons le drapeau `--exclude-length` pour trier les tailles de réponse. Plusieurs tailles de réponse peuvent être séparées par des virgules. 

```bash
gobuster vhost -u http://10.129.118.153 -w namelist.txt -p pattern --exclude-length 301 -t 10
```

![Figure 04 – Montre l'utilisation de Gobuster pour énumérer les hôtes virtuels. r3d-buck3t.com](https://miro.medium.com/v2/resize:fit:770/1*uRxbEAEqMPflKomUCVnAeA.png)
_Figure 04 – Montre l'utilisation de Gobuster pour énumérer les hôtes virtuels._

### Curl

Nous pouvons obtenir le même résultat avec Curl et un peu de script bash. Le script ci-dessous lit le contenu du fichier _namelist_, qui sert de liste de mots, et imprime le message "Found Subdomain" pour chaque sous-domaine qu'il lit dans le fichier. 

```bash
cat namelist.txt | while read vhost; do echo "\n========\nFound Subdomain: ${vhost}\n=========";
```

Ensuite, la commande curl envoie des requêtes HTTP HEAD à l'adresse IP spécifiée (http://10.129.141.252), en passant les sous-domaines de la liste de mots dans l'en-tête Host.

La sortie est redirigée vers grep pour extraire la `Content-length` des réponses et l'enregistrer dans un fichier. 

```bash
curl -s -I http://10.129.141.252 -H "HOST: ${vhost}.inlanefreight.htb" | grep "Content-Length: "; done > output
```

![Figure 05 – montre l'identification des sous-domaines avec Curl. r3d-buck3t.com](https://miro.medium.com/v2/resize:fit:770/1*pKffK46ZlDRdXHKcNr53jA.png)
_Figure 05 – montre l'identification des sous-domaines avec Curl._

Pour rechercher dans la sortie, nous utilisons à nouveau la commande grep et filtrons les lignes qui contiennent le texte "Content-Length:". Ensuite, nous utilisons la commande `uniq` pour supprimer les lignes en double dans un fichier texte, et le drapeau `-c` pour compter le nombre de fois où chaque ligne unique apparaît.

```bash
cat output | grep "Content-Length:" | uniq -c
```

![Figure 06 – montre comment utiliser les commandes grep et uniq pour nettoyer la sortie de Curl. r3d-buck3t.com](https://miro.medium.com/v2/resize:fit:770/1*sMo_nLdQxbFCjcarkn8TpA.png)
_Figure 06 – montre comment utiliser les commandes grep et uniq pour nettoyer la sortie de Curl._

Si nous voulons extraire les sous-domaines du contenu, nous pouvons utiliser le drapeau `-B` pour afficher quelques lignes avant la correspondance. Dans cette commande, nous avons utilisé 4 lignes pour récupérer les noms de sous-domaines.

```bash
cat output | grep -B 4 "Content-Length: 103"
```

![Figure 07 – montre les sous-domaines extraits avec la commande grep et le drapeau -B. r3d-buck3t.com](https://miro.medium.com/v2/resize:fit:770/1*FIJCDeJakS_7BDHqOBMNsQ.png)
_Figure 07 – montre les sous-domaines extraits avec la commande grep et le drapeau -B._

## Post-énumération

Après avoir identifié les hôtes virtuels, nous ajoutons HTTP ou HTTPS pour générer une liste d'URLs. Nous pouvons utiliser un script bash en une ligne pour cela.

```bash
for i in $(cat vhost2); do echo "https://"$i; done > vhosts3
```

![Figure 08 montre l'utilisation d'un script bash pour ajouter HTTP/s à la liste des sous-domaines identifiés. r3d-buck3t.com](https://miro.medium.com/v2/resize:fit:770/1*drVIRyWTRBRHxciofAxEgg.png)
_Figure 08 – montre l'utilisation d'un script bash pour ajouter HTTP/s à la liste des sous-domaines identifiés._

Cette liste peut ensuite être utilisée avec d'autres outils comme hakcheckurl ou Eyewitness pour récupérer les codes de réponse HTTP afin de vérifier les pages web disponibles et capturer des captures d'écran.

### hakcheckurl

hakcheckurl est un outil écrit en Go par hakluke et est [disponible sur GitHub ici](https://github.com/hakluke/hakcheckurl). L'outil prend une liste d'URLs et retourne leurs codes de réponse HTTP correspondants.

Pour exécuter l'outil, vous devez avoir Go installé. [Suivez les étapes sur le site officiel de Go](https://go.dev/doc/install) pour l'installer dans un environnement Linux.

Après l'installation, clonez le dépôt hakcheckurl, construisez l'outil avec `go build`, et renommez-le en hakcheckurl.

```bash
git clone https://github.com/hakluke/hakcheckurl.git

go build ./main.go

# renommez l'outil en hakcheckurl au lieu de main
mv main hakcheckurl
```

![Figure 09 – montre l'outil hakcheckurl après l'exécution de la commande de construction. r3d-buck3t.com](https://miro.medium.com/v2/resize:fit:770/1*Mk8hTSH-K8jY0hun1us51Q.png)
_Figure 09 – montre l'outil hakcheckurl après l'exécution de la commande de construction._

Ensuite, nous utilisons l'outil hakcheckurl pour déterminer les codes de réponse HTTP pour chaque URL. Dans les résultats ci-dessous, vous pouvez voir que les URLs qui utilisaient le protocole HTTPS étaient inaccessibles, tandis que celles qui utilisaient le protocole HTTP ont retourné des codes de réponse 200. Cela indique que les pages web utilisant HTTP sont opérationnelles.

```bash
cat vhosts | ./hakcheckurl
```

![Figure 10 – montre la sortie de l'outil hakcheckurl. r3d-buck3t.com](https://miro.medium.com/v2/resize:fit:770/1*U_8wcxNez5sJvQ1mSteGEg.png)
_Figure 10 – montre la sortie de l'outil hakcheckurl._

### Eyewitness

Une fois que nous avons identifié les pages web que nous voulons inspecter, nous pouvons utiliser Eyewitness pour recueillir plus d'informations sur l'infrastructure sous-jacente et les technologies associées aux sites web ciblés.

Eyewitness est un outil créé par RedSiege qui peut capturer des captures d'écran, récupérer des informations d'en-tête et identifier les identifiants par défaut, si connus. Nous pouvons l'installer sur Kali avec `sudo apt-get install eyewitness` ou [le télécharger depuis GitHub](https://github.com/RedSiege/EyeWitness).

Pour exécuter Eyewitness, nous devons passer la liste des URLs en utilisant le drapeau `-f`. Ensuite, nous pouvons définir une chaîne User-Agent personnalisée pour les requêtes HTTP avec le drapeau `--user-agent`. Cela peut être utile pour simuler des requêtes provenant de différents navigateurs ou applications client.

Nous pouvons également spécifier des ports supplémentaires à vérifier avec les protocoles http et https en utilisant les drapeaux `--add-http-ports` et `--add-https-ports`. Cela indique à Eyewitness de se connecter à ces ports et de capturer des captures d'écran, le cas échéant.

```bash
eyewitness -f vhost2 --user-agent "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36" --add-http-ports 8080,8000,8088 --add-https-ports 8443,4433,4343
```

![Figure 11 – montre Eyewitness en cours d'exécution contre une liste d'URLs fournies. r3d-buck3t.com](https://miro.medium.com/v2/resize:fit:770/1*aw02AfYuaXLnfjVvUrcsuQ.png)
_Figure 11 – montre Eyewitness en cours d'exécution contre une liste d'URLs fournies._

Après son exécution, nous sommes invités à choisir d'ouvrir ou non le rapport qui a été créé. Si vous sélectionnez 'Y', le navigateur web par défaut ouvrira le rapport. Si vous choisissez 'N', le rapport sera enregistré sur votre appareil local.

![Image](https://miro.medium.com/v2/resize:fit:770/1*OxbNyxkTlmIboWAvqaMn2g.png)
_Figure 12 – montre le rapport HTML généré par Eyewitness._

## Conclusion

Avec cela, nous avons atteint la fin du tutoriel d'aujourd'hui. Tout au long de l'article, vous avez découvert et exploré divers outils pour énumérer les hôtes virtuels. Nous avons également discuté de la manière d'utiliser les résultats de ces outils pour élargir la surface d'attaque et obtenir des informations précieuses sur l'infrastructure de la cible.

Merci d'avoir pris le temps de lire cet article. J'ai également créé une fiche mémo pour vous sur [Notion](https://r3dbuck3t.notion.site/Virtual-Hosts-c20c70e7751441b4acdb71ec07693cc2?pvs=4) qui liste toutes les commandes que nous avons utilisées dans cet article.

### Ressources

* [Information Gathering – Web Edition – HTB Academy](https://academy.hackthebox.com/course/preview/information-gathering---web-edition)
* [Apache IP and Name Based Virtual Hosts Explained](https://linuxconfig.org/apache-ip-and-name-based-virtual-hosts-explained)
* [Assetnote Wordlists](https://wordlists.assetnote.io/)
* [SecLists Wordlists](https://github.com/danielmiessler/SecLists)