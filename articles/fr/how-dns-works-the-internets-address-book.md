---
title: 'Comment fonctionne le DNS : Un guide pour comprendre l''annuaire d''Internet'
subtitle: ''
author: Dhruv Prajapati
co_authors: []
series: null
date: '2025-05-14T19:40:28.843Z'
originalURL: https://freecodecamp.org/news/how-dns-works-the-internets-address-book
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1747235471002/8fbe4d7e-f1cb-4faf-a6a5-8dcaf38d58f3.png
tags:
- name: dns
  slug: dns
- name: dns resolver
  slug: dns-resolver
- name: Domain Name System
  slug: domain-name-system
- name: dns server
  slug: dns-server
- name: internet
  slug: internet
seo_title: 'Comment fonctionne le DNS : Un guide pour comprendre l''annuaire d''Internet'
seo_desc: The Domain Name System (DNS) translates domain names (like example.com)
  into IP addresses (like 192.0.2.1) so we can easily access websites. In this guide,
  you’ll learn how DNS resolution starts, its step-by-step process, how caching works,
  and the r...
---

Le Domain Name System (DNS) traduit les noms de domaine (comme `example.com`) en adresses IP (comme `192.0.2.1`) afin que nous puissions accéder facilement aux sites web. Dans ce guide, vous apprendrez comment la résolution DNS commence, son processus étape par étape, le fonctionnement de la mise en cache et le rôle des serveurs racine, TLD et serveurs de noms autoritaires.

## Table des matières

* [Table des matières](#heading-table-des-matieres)
    
* [Le processus de résolution DNS](#heading-le-processus-de-resolution-dns)
    
* [Trouver le premier serveur DNS : Défauts, DHCP et paramètres manuels](#heading-trouver-le-premier-serveur-dns-defauts-dhcp-et-parametres-manuels)
    
* [Comment la résolution DNS alimente les requêtes réseau de votre application](#heading-comment-la-resolution-dns-alimente-les-requetes-reseau-de-votre-application)
    
    * [Vérification de l'IP valide](#heading-1-verification-de-lip-valide)
        
    * [Recherche dans le cache de l'application](#heading-2-recherche-dans-le-cache-de-lapplication)
        
    * [Vérification du cache du système d'exploitation](#heading-3-verification-du-cache-du-systeme-d-exploitation)
        
    * [Transmission au serveur DNS configuré](#heading-4-transmission-au-serveur-dns-configure)
        
    * [Résolution récursive à travers les serveurs](#heading-5-resolution-recursive-a-travers-les-serveurs)
        
* [Comprendre le rôle du résolveur récursif](#heading-comprendre-le-role-du-resolveur-recursif)
    
    * [Interaction entre le résolveur récursif et le serveur racine](#heading-interaction-entre-le-resolveur-recursif-et-le-serveur-racine)
        
    * [Interaction entre le résolveur récursif et le serveur TLD](#heading-interaction-entre-le-resolveur-recursif-et-le-serveur-tld)
        
    * [Interaction entre le résolveur récursif et le serveur de noms autoritaire](#heading-interaction-entre-le-resolveur-recursif-et-le-serveur-de-noms-autoritaire)
        
* [Bureaux d'enregistrement de domaines et configuration DNS pour les nouveaux domaines](#heading-bureaux-denregistrement-de-domaines-et-configuration-dns-pour-les-nouveaux-domaines)
    
    * [Qu'est-ce que les bureaux d'enregistrement de domaines ?](#heading-quest-ce-que-les-bureaux-denregistrement-de-domaines)
        
    * [Que se passe-t-il dans le système DNS lorsque vous achetez un nouveau domaine ?](#heading-que-se-passe-t-il-dans-le-systeme-dns-lorsque-vous-achetez-un-nouveau-domaine)
        
* [Conclusion](#heading-conclusion)
    

## Le processus de résolution DNS

Lorsque vous tapez un nom de domaine comme `example.com` dans votre navigateur, il charge le site web presque instantanément. Alors, comment fait-il cela ?

Eh bien, la résolution DNS le rend possible, agissant comme le GPS de l'internet pour transformer ce nom en une adresse IP (comme `192.0.2.1`) que les ordinateurs utilisent pour trouver les serveurs.

La résolution DNS fonctionne en envoyant une requête à travers une chaîne de serveurs DNS, chacun aidant à localiser l'adresse exacte. Ce processus commence par une étape cruciale : votre appareil doit savoir quel serveur DNS contacter en premier, soit un serveur défini automatiquement, soit un serveur choisi pour sa vitesse et sa fiabilité.

## Trouver le premier serveur DNS : Défauts, DHCP et paramètres manuels

Pour que le DNS fonctionne, un appareil doit connaître l'adresse IP d'au moins un serveur DNS. Cela est réalisé grâce à des **paramètres préconfigurés**, une **configuration automatique via DHCP** et une **configuration manuelle**.

Les appareils comme les routeurs, les smartphones et les ordinateurs sont souvent livrés avec des adresses IP de serveurs DNS codées en dur. Des exemples courants incluent Google Public DNS (`8.8.8.8`, `8.8.4.4`) et Cloudflare DNS (`1.1.1.1`). Ces serveurs servent de points de départ par défaut pour les requêtes DNS.

De plus, lorsqu'un appareil se connecte à un réseau (par exemple, le Wi-Fi domestique), un serveur DHCP (Dynamic Host Configuration Protocol) - généralement sur le routeur - attribue une adresse IP et des adresses de serveurs DNS. Celles-ci sont souvent fournies par le fournisseur d'accès à Internet (FAI), comme `75.75.75.75` de Comcast, mais peuvent être remplacées par des alternatives comme OpenDNS (`208.67.222.222`) ou Quad9 (`9.9.9.9`).

Les utilisateurs avancés peuvent spécifier manuellement les serveurs DNS. Les fournisseurs de DNS publics utilisent des adresses IP mémorables pour simplifier, comme `8.8.8.8` de Google (chiffres répétitifs), `1.1.1.1` de Cloudflare (séquence courte) ou `9.9.9.9` de Quad9 (chiffres répétitifs).

Cette conception garantit une opération transparente pour la plupart des utilisateurs, avec DHCP et des configurations par défaut, tout en permettant aux utilisateurs expérimentés de choisir des services DNS plus rapides ou axés sur la confidentialité.

## Comment la résolution DNS alimente les requêtes réseau de votre application

Lorsque qu'une application, comme un navigateur web ou un service backend, souhaite effectuer un appel réseau - tel qu'une requête HTTP pour charger une page web, un appel gRPC pour la communication entre microservices, ou une récupération d'API pour récupérer des données - elle déclenche une série de vérifications et de requêtes pour traduire un nom de domaine en une adresse IP. Ce processus est conçu pour l'efficacité, exploitant les caches et un réseau distribué de serveurs pour gérer l'échelle massive de l'internet.

### **1. Vérification de l'IP valide**

Le processus commence par vérifier si l'adresse de destination est déjà une adresse IP valide, comme `192.168.1.1`. Le système utilise une vérification regex pour confirmer cela. Si c'est une IP valide, aucune résolution DNS n'est nécessaire, et l'appel réseau se poursuit directement.

**Notez** que dans de rares cas, la résolution DNS est entièrement ignorée si une adresse IP est utilisée directement. Par exemple, un utilisateur pourrait taper manuellement une IP, comme 192.0.2.1, dans un navigateur au lieu d'un nom de domaine, bien que cela soit peu probable puisque les adresses IP sont difficiles à retenir par rapport aux noms comme example.com.

De même, certaines applications effectuent des appels réseau en utilisant directement des adresses IP, contournant ainsi le besoin de DNS. Bien que possible, ces scénarios sont peu courants en raison de la commodité des noms de domaine lisibles par l'homme.

### **2. Recherche dans le cache de l'application**

Si l'adresse de destination est un nom de domaine, comme `example.com`, l'application vérifie son propre cache DNS, si elle en a un.

Les navigateurs modernes comme Chrome et Firefox maintiennent des caches intégrés pour accélérer la navigation. Si la correspondance domaine-IP est trouvée ici, le processus s'arrête, et l'IP est utilisée pour l'appel réseau.

### **3. Vérification du cache du système d'exploitation**

Si le cache de l'application manque de la correspondance ou si l'application n'a pas de mécanisme de mise en cache, la requête passe au client DNS du système d'exploitation, également connu sous le nom de Résolveur Local.

Cela varie selon le système d'exploitation :

* Windows utilise [dnscache](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn593685\(v=ws.11\))
    
* macOS utilise [mDNSResponder](https://manp.gs/mac/8/mDNSResponder)
    
* Linux utilise le [Name Switch Service](https://www.man7.org/linux/man-pages/man5/nsswitch.conf.5.html)
    

Le client DNS vérifie deux endroits : le cache DNS au niveau du système d'exploitation, qui stocke les correspondances récentes domaine-IP, et le fichier hosts, un fichier local qui mappe manuellement les domaines aux IP (par exemple, `127.0.0.1 localhost`). Si la correspondance est trouvée dans l'un ou l'autre endroit, le processus s'arrête ici.

### **4. Transmission au serveur DNS configuré**

Si la correspondance reste non résolue, le client DNS envoie la requête à un serveur DNS configuré, comme le serveur du FAI ou un serveur public comme Google DNS (`8.8.8.8`) ou Cloudflare DNS (`1.1.1.1`). Ce serveur est un système complexe avec ses propres caches et un service de résolveur récursif, comme [BIND](https://www.isc.org/bind/) ou [Unbound](https://www.nlnetlabs.nl/projects/unbound/about/#:~:text=Unbound%20is%20a%20validating%2C%20recursive%2C%20caching%20DNS%20resolver.,DNS-over-HTTPS%20which%20allows%20clients%20to%20encrypt%20their%20communication.), qui prend en charge la requête.

#### Techniques de mise en cache

La mise en cache, en particulier dans les résolveurs récursifs, stocke les résultats des requêtes pour minimiser les recherches redondantes et accélérer les réponses pour les utilisateurs :

* **Cache du résolveur récursif** : Stocke les résultats des requêtes des serveurs racine, TLD et serveurs de noms autoritaires dans les résolveurs récursifs pour accélérer les réponses.
    
* **Cache négatif** : Stocke les réponses pour les domaines ou enregistrements inexistants afin d'éviter les requêtes répétées.
    
* **Cache de requête transmise** : Stocke les réponses des requêtes transmises à d'autres résolveurs ou serveurs DNS pour améliorer les performances.
    

Ces mécanismes de mise en cache minimisent les recherches externes ([RFC 1035](https://datatracker.ietf.org/doc/html/rfc1035)).

### **5. Résolution récursive à travers les serveurs**

Le résolveur récursif, un composant central d'un serveur DNS, est responsable de la résolution récursive pour traduire les noms de domaine comme `example.com` en adresses IP.

Comme les enregistrements DNS sont distribués sur plusieurs serveurs, le résolveur analyse le domaine et exécute une série de requêtes :

1. Il contacte un serveur racine, qui le dirige vers le serveur de domaine de premier niveau (TLD) (par exemple, pour .com).
    
2. Le serveur TLD pointe vers le serveur de noms autoritaire pour le domaine spécifique.
    
3. Le serveur autoritaire fournit l'adresse IP finale.
    

Cette approche distribuée assure l'évolutivité et la fiabilité ([RFC 1035](https://datatracker.ietf.org/doc/html/rfc1035)).

## Comprendre le rôle du résolveur récursif

Le résolveur récursif est le moteur derrière la résolution DNS, travaillant pour convertir un nom de domaine comme example.com en une adresse IP. Son parcours commence par interroger un serveur racine, la première étape pour naviguer dans la hiérarchie DNS afin de trouver l'adresse correcte.

### Interaction entre le résolveur récursif et le serveur racine

Pour comprendre cette interaction, explorons d'abord ce que sont les serveurs racine et leur rôle dans le DNS.

#### Exploration des serveurs racine

Les serveurs racine forment la base de la hiérarchie DNS, répondant aux requêtes pour les enregistrements de domaine de premier niveau (TLD) afin d'initier la résolution. Ils dirigent les résolveurs récursifs vers les serveurs TLD, permettant la recherche des adresses IP des domaines.

* Il existe **13 clusters de serveurs racine**, nommés a.root-servers.net à m.root-servers.net, exploités par 12 organisations (VeriSign en gère deux). Ces clusters distribuent les charges de requêtes DNS mondiales. En date du 10 mai 2025, 1 936 instances anycast assurent une haute disponibilité et une évolutivité, traitant des milliards de requêtes quotidiennes (Root Server Technical Operations Association).
    
* Chaque cluster utilise le **routage anycast**, partageant une seule adresse IP entre plusieurs serveurs mondiaux. Les requêtes sont acheminées vers l'instance la plus proche ou la moins chargée, réduisant la latence, améliorant la fiabilité et fournissant une redondance en cas de défaillance d'un serveur.
    
* Le **fichier root hints**, fourni par l'ICANN ([IANA](https://www.iana.org/domains/root/files)), liste les adresses IP des serveurs racine et est préchargé dans les résolveurs. Il permet les requêtes DNS initiales sans avoir besoin de résoudre les domaines des serveurs racine, évitant les dépendances circulaires et assurant la stabilité du système.
    

Le DNS a commencé avec seulement deux serveurs racine en 1983. À mesure que l'internet grandissait, plus de serveurs ont été ajoutés pour répondre à la demande. En 2002, le nombre a atteint 13, et le routage anycast a été proposé, permettant à plusieurs serveurs de fonctionner comme un seul cluster sous une seule adresse IP.

Depuis lors, le DNS a évolué en étendant ces 13 clusters pour répondre aux exigences mondiales ([RFC 882](https://datatracker.ietf.org/doc/html/rfc882), [Netnod](https://www.netnod.se/)). Pour une histoire détaillée, voir l'[archive de l'Institut DNS](https://dnsinstitute.com/dns-history/dns-root-hints-history/) et l'[Histoire des ROOT-SERVERS](https://icannwiki.org/History_of_ROOT-SERVERS).

#### Comment les résolveurs récursifs interrogent les serveurs racine

Le résolveur récursif initie la résolution en interrogeant un serveur racine pour les enregistrements TLD, s'appuyant sur plusieurs mécanismes pour assurer l'exactitude et l'efficacité.

* Il utilise le **fichier root hints**, la liste des adresses IP des serveurs racine de l'ICANN codée en dur dans les résolveurs (par exemple, BIND), pour éviter les dépendances circulaires.
    

* Les **requêtes de priming** récupèrent les IP des serveurs racine mises à jour au démarrage du résolveur ou à l'expiration du cache, assurant la fiabilité (RFC 8109).
    
* Le **fichier de zone racine**, la base de données de l'ICANN des TLD et de leurs serveurs de noms, est utilisé par les serveurs racine pour répondre avec les détails des TLD ([IANA](https://www.iana.org/domains/root/files)).
    

Lors de l'interrogation, le résolveur sélectionne un serveur racine et demande les enregistrements TLD (par exemple, pour `.com`). La réponse inclut les enregistrements **NS** (par exemple, `a.gtld-servers.net` pour `.com`) et les **enregistrements glue**, qui sont des enregistrements d'adresses IP (**A** ou **AAAA**) fournissant directement les IP des serveurs de noms TLD.

Les enregistrements glue sont cruciaux lorsque les domaines des serveurs de noms demandés sont dans le domaine interrogé (par exemple, `ns1.example.com` pour `example.com`), évitant la dépendance circulaire en fournissant l'IP sans résoudre le domaine.

Pour les requêtes TLD, les enregistrements glue sont toujours inclus, accélérant la résolution en évitant des recherches supplémentaires pour les domaines des serveurs de noms TLD comme `a.gtld-servers.net`, surtout pour les TLD occupés comme `.com` ([RFC 1035](https://datatracker.ietf.org/doc/html/rfc1035)).

### Interaction entre le résolveur récursif et le serveur TLD

Une fois que le résolveur récursif reçoit la réponse du serveur racine, y compris les enregistrements glue, il interroge un serveur de noms TLD (par exemple, `a.gtld-servers.net` pour `.com`). Les serveurs de noms TLD maintiennent des **fichiers de zone** listant les domaines sous leur TLD (par exemple, `example.com`) et leurs serveurs de noms.

Le serveur TLD répond par un renvoi, fournissant les enregistrements des serveurs de noms autoritaires (par exemple, `ns1.example.com` pour `example.com`). Si le domaine du serveur autoritaire est dans le domaine demandé (par exemple, `ns1.example.com`), les enregistrements glue sont inclus pour fournir l'IP directement, évitant la dépendance circulaire.

Le résolveur met en cache la réponse en fonction de son TTL pour accélérer les requêtes futures. Si le serveur TLD est inaccessible, le résolveur essaie un autre serveur TLD à partir de la réponse du serveur racine ([RFC 1035](https://datatracker.ietf.org/doc/html/rfc1035)).

### Interaction entre le résolveur récursif et le serveur de noms autoritaire

* Le résolveur récursif interroge ensuite le serveur de noms autoritaire (par exemple, `ns1.example.com`), qui maintient les fichiers de zone avec les enregistrements DNS comme **A**, **CNAME**, ou **MX** pour son domaine (par exemple, `example.com`).
    
* Le serveur retourne l'enregistrement demandé, comme un enregistrement A (par exemple, `192.0.2.1`), AAAA, CNAME, ou MX, selon la requête.
    
* Les enregistrements glue de la réponse TLD fournissent l'IP du serveur s'il est dans le domaine, évitant la dépendance circulaire.
    
* Le résolveur met en cache la réponse en fonction du TTL pour l'efficacité. Dans de rares cas, le serveur peut déléguer à un autre serveur autoritaire (par exemple, pour les sous-domaines), nécessitant des requêtes supplémentaires. Si inaccessible, le résolveur essaie un autre serveur autoritaire ([RFC 1035](https://datatracker.ietf.org/doc/html/rfc1035)).
    

Traditionnellement, les fichiers de zone pour les serveurs racine, TLD et autoritaires étaient des fichiers texte listant les domaines et leurs enregistrements DNS, guidant les requêtes à travers la hiérarchie DNS.

L'infrastructure DNS moderne a remplacé ceux-ci par des bases de données efficaces ou des bases de données en mémoire, utilisant des structures de données optimisées comme des tables de hachage ou des tries pour des recherches plus rapides et une meilleure évolutivité. Ce changement supporte le nombre croissant de TLD et les volumes élevés de requêtes sur tous les types de serveurs.

De même, la proposition de routage anycast, introduite pour améliorer la vitesse et la fiabilité en distribuant les instances de serveurs mondialement, a été conçue pour tous les serveurs de noms - racine, TLD et autoritaires.

Bien que les serveurs racine adoptent universellement l'anycast, assurant une faible latence et une redondance, tous les serveurs TLD et autoritaires ne le suivent pas strictement.

Certains TLD et serveurs autoritaires plus petits s'appuient sur l'unicast ou l'anycast limité en raison des coûts ou des contraintes opérationnelles, conduisant à des performances variées à travers la hiérarchie DNS.

Le diagramme suivant illustre le processus complet de résolution de noms de domaine, résumant les étapes décrites ci-dessus.

![Diagramme du système de résolution DNS](https://cdn.hashnode.com/res/hashnode/image/upload/v1746995157651/f0f9913b-a23a-4654-bea5-c9d8a8e4f7ca.png align="center")

L'image suivante montre la sortie de `dig +trace google.com`, démontrant le processus de résolution du serveur racine au serveur de noms autoritaire :

![Processus de résolution DNS en action utilisant l'outil dig](https://cdn.hashnode.com/res/hashnode/image/upload/v1747000331356/8735cac3-5a22-48c2-9691-62ed6d8fb885.png align="center")

## Bureaux d'enregistrement de domaines et configuration DNS pour les nouveaux domaines

### Qu'est-ce que les bureaux d'enregistrement de domaines ?

Les bureaux d'enregistrement de domaines ont été initialement établis pour gérer l'enregistrement des noms de domaine, permettant aux particuliers et aux organisations de sécuriser des noms uniques (par exemple, `example.com`) pour les sites web et les services en ligne. Ils agissent comme intermédiaires entre les propriétaires de domaines et les registres de domaines, qui maintiennent les bases de données autoritaires pour les domaines de premier niveau (TLD) comme `.com` ou `.org`.

Les registrars gèrent des tâches telles que l'enregistrement de domaines, leur renouvellement et la mise à jour des paramètres DNS, assurant une intégration transparente avec le système DNS mondial. De nombreux registrars offrent également des services supplémentaires comme l'hébergement web et les certificats SSL pour soutenir les opérations des sites web.

GoDaddy et Hostinger font partie des nombreux registrars, connus pour leurs plateformes conviviales et leurs offres de services complètes.

### Que se passe-t-il dans le système DNS lorsque vous achetez un nouveau domaine ?

Lorsque vous achetez un nouveau domaine (comme `example.com`) via un registrar comme GoDaddy ou Hostinger, les étapes suivantes se produisent dans le système DNS :

* **Étape 1 : Enregistrement auprès du registre** - Le registrar envoie les détails de votre domaine au registre pour le TLD (par exemple, VeriSign pour `.com`). Le registre ajoute le domaine à sa base de données, enregistrant le registrar comme l'entité gestionnaire et les serveurs de noms autoritaires (par exemple, `ns1.example.com`) que vous spécifiez.
    
* **Étape 2 : Configuration du serveur de noms** - Vous configurez les serveurs de noms du domaine dans le panneau de contrôle du registrar (par exemple, le Portfolio de domaines de GoDaddy ou le hPanel de Hostinger). Ces serveurs de noms, souvent fournis par le registrar ou le fournisseur d'hébergement (par exemple, `ns1.hostinger.com`), pointent vers le fichier de zone DNS qui contient les enregistrements DNS pour votre domaine.
    
* **Étape 3 : Configuration de la zone DNS** - Le fichier de zone DNS, géré là où les serveurs de noms pointent, est mis à jour avec des enregistrements DNS comme :
    
    * **Enregistrement A** : Mappe le domaine (par exemple, `example.com`) à l'adresse IP du serveur d'hébergement (par exemple, `192.0.2.1`).
        
    * **Enregistrement CNAME** : Aliase les sous-domaines (par exemple, `www.example.com`) vers un autre domaine.
        
    * **Enregistrement MX** : Dirige les emails vers les serveurs de messagerie.
        
    
    Si vous utilisez l'hébergement du registrar, ces enregistrements peuvent être définis automatiquement. Sinon, vous les configurez manuellement pour pointer vers l'IP de votre fournisseur d'hébergement.
    
* **Étape 4 : Propagation DNS** - Après la mise à jour des serveurs de noms ou des enregistrements DNS, les changements se propagent à travers le réseau DNS mondial, ce qui peut prendre 24 à 48 heures en raison de la mise en cache et des mises à jour des serveurs. Pendant cette période, votre site web peut ne pas être immédiatement accessible.
    
* **Étape 5 : Mise à jour du registre TLD** - Le registre met à jour ses enregistrements pour inclure les serveurs de noms du domaine, qui sont interrogés par les résolveurs récursifs lors des recherches DNS. Pour les domaines dont les serveurs de noms sont dans le même domaine (par exemple, `ns1.example.com` pour `example.com`), des enregistrements glue (adresses IP des serveurs de noms) sont enregistrés auprès du registre pour éviter les dépendances circulaires.
    

## Conclusion

Le Domain Name System (DNS) traduit les noms de domaine en adresses IP, rendant l'internet convivial. Il résout les requêtes efficacement grâce à un système hiérarchique et à la mise en cache, évoluant de quelques serveurs racine en 1983 à un réseau évolutif et basé sur l'anycast aujourd'hui.