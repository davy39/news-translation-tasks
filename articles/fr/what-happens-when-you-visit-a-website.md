---
title: Que se passe-t-il quand vous visitez un site web ? Le fonctionnement du Web
  expliqué
date: '2024-11-15T17:31:36.281Z'
author: Viviana Yanez
authorURL: https://www.freecodecamp.org/news/author/vivianay/
originalURL: https://freecodecamp.org/news/what-happens-when-you-visit-a-website
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1731682843488/32065460-190d-472f-9268-5b181430eef6.jpeg
tags:
- name: Web Development
  slug: web-development
- name: internet
  slug: internet
seo_desc: 'In this article, I’ll guide you through an overview of what happens when
  you navigate to a website using your browser.

  Whether you’re new to web development or have some experience, this post will help
  you gain a better understanding of how the web a...'
---


Dans cet article, je vais vous guider à travers une vue d'ensemble de ce qui se passe lorsque vous naviguez sur un site web à l'aide de votre navigateur.

<!-- more -->

Que vous soyez débutant en développement web ou que vous ayez déjà de l'expérience, cet article vous aidera à mieux comprendre le fonctionnement du Web et de ses technologies de base.

## Table des matières {#heading-table-des-matieres}

-   [Trouver une ressource : les URL][1]
    
-   [Correspondance entre IP et URL : la résolution DNS][2]
    
    -   [Qu'est-ce que le résolveur DNS ?][3]
        
    -   [Qu'est-ce que le serveur DNS racine ?][4]
        
    -   [Qu'est-ce que le serveur de domaine de premier niveau ?][5]
        
    -   [Serveur de noms faisant autorité][6]
        
-   [Établir une connexion : le modèle TCP/IP][7]
    
    -   [Comment fonctionne la connexion TCP ?][8]
        
    -   [Le three-way handshake TCP][9]
        
-   [Démarrer l'échange : communication client-serveur][10]
    
    -   [Qu'est-ce que le protocole HTTP ?][11]
        
    -   [Requête/Réponse HTTP][12]
        
    -   [HTTPS][13]
        
    -   [Time to First Byte][14]
        
-   [Des données aux pixels : le chemin critique du rendu][15]
    
    -   [Construction de l'arbre DOM][16]
        
    -   [Construction de l'arbre CSSOM][17]
        
    -   [Compilation et exécution JavaScript][18]
        
    -   [Construction de l'arbre d'accessibilité][19]
        
    -   [Arbre de rendu (Render tree)][20]
        
    -   [Layout][21]
        
    -   [Painting][22]
        
    -   [Une note sur l'hydratation JavaScript][23]
        
-   [Conclusion][24]
    

Avant d'entrer dans les détails de chaque étape du processus, passons en revue certains des concepts de base que nous allons aborder.

L'Internet est un immense réseau d'ordinateurs interconnectés. Le World Wide Web (ou Web) est construit sur cette technologie, tout comme d'autres services tels que le courrier électronique, les systèmes de messagerie instantanée ou le partage de fichiers, etc.

Les ordinateurs connectés à l'Internet sont soit des :

-   **Clients**, les appareils de l'utilisateur web et les logiciels que ces appareils utilisent pour accéder au Web.
    
-   **Serveurs**, des ordinateurs qui stockent des pages web, des sites ou des applications et les fichiers nécessaires à leur affichage dans le navigateur web ou les appareils de l'utilisateur.
    

## Trouver une ressource : les URL {#heading-trouver-une-ressource-les-url}

Chaque ressource stockée sur un serveur peut être localisée par les clients à l'aide de son URL valide associée. Voici un exemple d'URL valide :

![Exemple d'une URL valide, incluant son schéma, son autorité, le chemin vers la ressource, deux paramètres et une ancre.](https://cdn.hashnode.com/res/hashnode/image/upload/v1731414821178/970907db-f349-421e-b410-45f4ee978e0b.jpeg)

Vous savez peut-être déjà ce qu'est une URL, mais voyons en détail chacune de ses parties :

-   **Schéma (Scheme)** : La première partie d'une URL indique le protocole qui doit être utilisé pour récupérer la ressource. Les sites web utilisent les protocoles HTTP et HTTPS, mais nous verrons plus de détails à ce sujet plus tard. Le `:` après le schéma est ce qui le sépare de la partie suivante de l'URL.
    
-   **Autorité (Authority)** : cette partie est composée du nom de domaine et du numéro de port séparés par deux-points. Le port n'est obligatoire que lorsque les ports standard du protocole HTTP (80 pour HTTP et 443 pour HTTPS) ne sont pas utilisés par le serveur web. Le `//` avant le nom de domaine indique le début de l'autorité.
    
-   **Chemin vers la ressource (Path to resource)** : il s'agit du chemin abstrait ou physique vers la ressource sur le serveur web.
    
-   **Paramètres** : un ensemble de paires clé/valeur qui ajoutent des options supplémentaires à appliquer lors du retour de la ressource demandée. Ils sont séparés par un `&` et chaque serveur web a sa propre façon de gérer les paramètres. Cette section commence par `?`.
    
-   **Ancre (Anchor)** : Cette section, si elle est présente, commence par un `#` et est gérée par le navigateur pour afficher une partie spécifique du document retourné. Par exemple, elle peut pointer vers une section spécifique d'un document HTML.
    

Il se passe plusieurs choses lorsque vous tapez une URL dans la barre d'adresse de votre navigateur qui vous permettent de naviguer vers un site et d'interagir avec son contenu. Voyons chacune d'elles en détail.

## Correspondance entre IP et URL : la résolution DNS {#heading-correspondance-entre-ip-et-url-la-resolution-dns}

Alors qu'en tant qu'humains, nous préférons les noms de domaine composés de mots, les ordinateurs communiquent entre eux à l'aide d'adresses IP. Les adresses IP sont composées de chiffres et sont plus difficiles à mémoriser pour nos esprits humains. Le [Domain Name System][25] (**DNS**) est ce qui met en relation les noms de domaine et les adresses IP.

Lorsque vous tapez une URL, le navigateur regarde d'abord dans le cache local pour voir si les résultats de la recherche DNS sont déjà stockés. Ensuite, il vérifiera également dans le cache du système d'exploitation.

S'il n'y a pas de résultats stockés, le navigateur appellera alors le résolveur DNS pour tenter de trouver l'adresse IP associée au nom de domaine.

### Qu'est-ce que le résolveur DNS ? {#heading-qu-est-ce-que-le-resolveur-dns}

Le résolveur est généralement défini par le DNS de votre fournisseur d'accès Internet, bien que ce soit le choix par défaut de la plupart des gens, il est possible de le changer pour celui de Google, de Cloudflare ou tout autre de votre choix.

Encore une fois, le DNS du fournisseur peut avoir les résultats pour le nom de domaine stockés dans son cache ; sinon, il interrogera le serveur DNS racine.

### Qu'est-ce que le serveur DNS racine ? {#heading-qu-est-ce-que-le-serveur-dns-racine}

Le serveur DNS racine est un système qui pilote réellement l'ensemble de l'Internet. Il est composé de treize serveurs répartis sur toute la planète. Il renvoie à la requête du résolveur le serveur de domaine de premier niveau (TLD) correspondant au nom de domaine demandé.

À ce moment, le résolveur DNS mettra en cache l'IP de ce serveur de domaine de premier niveau afin de ne pas avoir à interroger à nouveau le serveur DNS racine pour celui-ci.

### Qu'est-ce que le serveur de domaine de premier niveau ? {#heading-qu-est-ce-que-le-serveur-de-domaine-de-premier-niveau}

Le serveur de [domaine de premier niveau][26] (**TLD** pour Top Level Domain) stocke les adresses IP des serveurs de noms faisant autorité pour le domaine que l'utilisateur recherche.

Dans l'URL `www.exampleurl.com`, le domaine de premier niveau est `.com`. Il en existe différents types, tels que les domaines de premier niveau génériques comme `.com` ou `.org`, les domaines de premier niveau de code de pays, généralement représentés par le code pays ISO à deux lettres, et plus encore.

Le TLD renvoie les serveurs de noms faisant autorité pour le domaine demandé. Une fois de plus, le résolveur DNS mettra les résultats en cache pour ne pas avoir à y revenir plus tard.

### Serveur de noms faisant autorité {#heading-serveur-de-noms-faisant-autorite}

Ce serveur contient les enregistrements DNS qui font correspondre les noms de domaine aux adresses IP. Il y a plus d'un serveur de noms attaché à n'importe quel domaine.

Il n'y a pas de mise en cache à ce stade, car le serveur de noms faisant autorité est l'autorité suprême et le dernier maillon de la chaîne de résolution DNS.

Si l'adresse IP est disponible, le serveur de noms faisant autorité répond à la requête du résolveur DNS avec l'adresse IP du nom de domaine. Si elle n'est pas disponible, il répondra par une erreur. Ensuite, le résolveur DNS stocke l'IP et la renvoie au navigateur du client.

Une fois la recherche DNS terminée et que le navigateur dispose de l'adresse IP, il peut tenter d'établir une connexion avec le serveur.

## Établir une connexion : le modèle TCP/IP {#heading-etablir-une-connexion-le-modele-tcp-ip}

La connexion entre le client et le serveur est établie à l'aide du [Transmission Control Protocol][27] (**TCP**) et de l'[Internet Protocol][28] (**IP**). Ces protocoles sont les principaux derrière le World Wide Web et d'autres technologies Internet, comme l'e-mail, et déterminent comment les données voyagent sur le réseau.

Le [modèle TCP/IP][29] est un framework utilisé pour organiser les différents protocoles impliqués dans l'Internet et d'autres communications réseau. La responsabilité principale de TCP/IP est de diviser les données en paquets et de les envoyer à leur destination finale, en veillant à ce que les paquets puissent être réassemblés à l'autre extrémité de la communication.

Ce processus suit un modèle à quatre couches, où les données voyagent dans une direction, puis dans la direction inverse lorsqu'elles atteignent la destination :

![Le modèle à quatre couches comprend la couche application, la couche transport, la couche internet et la couche réseau. Les données voyagent dans les deux sens à travers ces couches.](https://cdn.hashnode.com/res/hashnode/image/upload/v1731414848576/178ce64e-2216-487a-b142-c88c2125dcde.jpeg)

La couche transport garantit que les applications peuvent échanger des données en établissant des canaux de données. C'est également la couche qui établit le concept de ports réseau, un système de canaux de données numérotés alloués aux canaux de communication spécifiques dont les applications ont besoin.

La couche transport du modèle TCP/IP comprend deux protocoles qui sont les plus couramment utilisés sur Internet : le TCP et l'[User Datagram Protocol][30] (UDP).

Le TCP inclut certaines capacités qui le rendent prédominant sur la plupart des applications basées sur Internet telles que le Web, concentrons-nous donc sur lui.

### Comment fonctionne la connexion TCP ? {#heading-comment-fonctionne-la-connexion-tcp}

Le TCP permet de transférer les données de manière fiable et ordonnée vers leur destination. C'est un protocole orienté connexion, ce qui signifie que l'émetteur et le récepteur doivent s'accorder sur les paramètres de connexion avant d'établir réellement la connexion. Ce processus est connu sous le nom de procédure de handshake.

### Le three-way handshake TCP {#heading-le-three-way-handshake-tcp}

Le handshake est un moyen pour le client et le serveur d'établir une connexion sécurisée et de s'assurer que les deux parties sont synchronisées et prêtes à commencer à échanger des messages.

![Les trois étapes du handshake TCP.](https://cdn.hashnode.com/res/hashnode/image/upload/v1731414866173/6d66c360-2d2e-427b-8c8d-1555fdaa7197.jpeg)

Les trois étapes du handshake TCP comprennent :

1.  Le client informe le serveur qu'il souhaite établir une connexion en envoyant un paquet SYN (synchronize). Ce paquet spécifie un numéro de séquence avec lequel les segments suivants commenceront.
    
2.  Le serveur reçoit le SYN et répond par un segment SYN-ACK (synchronize-acknowledgment). Il inclut le numéro de séquence du serveur et un accusé de réception du numéro de séquence du client, incrémenté de un.
    
3.  Le client répond par un message ACK, accusant réception du numéro de séquence du serveur. À ce stade, la connexion est établie.
    

## Démarrer l'échange : communication client-serveur {#heading-demarrer-l-echange-communication-client-serveur}

Une fois la connexion TCP établie, le client et le serveur peuvent commencer à échanger des messages en utilisant le protocole HTTP.

### Qu'est-ce que le protocole HTTP ? {#heading-qu-est-ce-que-le-protocole-http}

L'[Hypertext Transfer Protocol][31] (**HTTP**) est le protocole de couche application le plus largement utilisé dans la suite TCP/IP, mais il est considéré comme non sécurisé, ce qui a conduit à un passage vers le HTTPS, qui utilise TLS au-dessus de TCP pour le chiffrement des données. Vous trouverez plus de détails à ce sujet plus tard.

Le navigateur commencera par envoyer un message de requête HTTP au serveur, demandant une copie du site sous la forme d'un fichier HTML. Le protocole HTTP peut transférer des fichiers comme HTML, CSS, JS, SVG, etc.

### Requête/Réponse HTTP {#heading-requete-reponse-http}

Il existe deux types de messages HTTP :

-   **Requêtes**, envoyées par le client au serveur pour déclencher une action.
    
-   **Réponses**, envoyées par le serveur au client en réponse à la requête précédente.
    

Les messages sont des documents en texte brut, structurés de manière précise déterminée par le protocole de communication, dans ce cas, le HTTP.

Les trois parties incluses dans une **requête HTTP** sont :

1.  **Ligne de requête (Request line)** : Comprend la méthode de requête, qui est un verbe définissant l'action à effectuer. Dans le cas que nous couvrons dans cet article, le navigateur fera une requête GET pour récupérer une page du serveur. La ligne de requête inclura également l'emplacement de la ressource, dans ce cas une URL, et la version du protocole utilisée.
    
2.  **En-tête de requête (Request header)** : Un ensemble de paires clé-valeur. Deux d'entre elles sont obligatoires. `Host` indique le nom de domaine à cibler, et `Connection` qui est toujours réglé sur close à moins qu'il ne doive rester ouvert. L'en-tête de requête se termine toujours par une ligne vide.
    
3.  **Corps de la requête (Request body)** : Est un champ optionnel qui permet d'envoyer des données au serveur.
    

Le serveur répondra à la requête par une réponse HTTP. Les réponses incluent des informations sur le statut de la requête et peuvent inclure la ressource ou les données demandées.

Les réponses HTTP sont structurées selon les parties suivantes :

1.  **Ligne de statut (Status line)** : Comprend la version du protocole utilisée, un code de statut et un texte de statut, avec une description lisible par l'homme du code de statut.
    
2.  **En-têtes (Headers)** : Un ensemble de paires clé-valeur qui peuvent être des en-têtes généraux, s'appliquant à l'ensemble du message ; des en-têtes de réponse, donnant des informations supplémentaires sur le statut du serveur ; ou des en-têtes de représentation, décrivant le format et l'encodage des données du message si elles sont présentes.
    
3.  **Corps (Body)** : Contient les données ou la ressource demandée. Si aucune donnée ou ressource n'est attendue par le client, la réponse n'inclura généralement pas de corps.
    

Lorsque la requête pour une page web est approuvée par le serveur, la réponse inclura un message `200 OK`. D'autres codes de réponse HTTP existants sont :

-   404 Not Found
    
-   403 Forbidden
    
-   301 Moved Permanently
    
-   500 Internal Server Error
    
-   304 Not Modified
    
-   401 Unauthorized
    

La réponse contiendra également une liste d'en-têtes HTTP et le corps de la réponse, incluant le code HTML correspondant à la page demandée.

### HTTPS {#heading-https}

L'[Hypertext Transfer Protocol Secure][32] (**HTTPS**) n'est pas un protocole différent, mais une extension du HTTP. On l'appelle généralement HTTP sur Transport Layer Security (**TLS**). Voyons ce que cela signifie exactement.

Le HTTP est le protocole utilisé pour la plupart des communications entre les navigateurs et les serveurs, mais il manque de sécurité. Toute donnée envoyée via HTTP peut potentiellement être visible par n'importe qui sur le réseau. C'est particulièrement risqué lorsque des données sensibles sont impliquées dans la connexion, comme des identifiants de connexion, des informations financières, des informations de santé, etc.

La motivation principale derrière le HTTPS est d'assurer la confidentialité des données, l'intégrité et l'identification. Cela signifie garantir que les données ne sont accessibles qu'à ceux auxquels elles sont destinées et qu'elles ne peuvent pas être interceptées ou modifiées par quiconque entre-temps. De plus, l'émetteur et le récepteur peuvent être identifiés comme étant ceux qu'ils prétendent être par une autorité légitime.

En HTTPS, les communications sont chiffrées à l'aide du protocole TLS, qui repose sur une infrastructure de clés publiques asymétriques. Il combine deux clés : une publique et une privée. Le serveur partage sa clé publique afin que le client puisse l'utiliser pour chiffrer des messages qui ne peuvent être déchiffrés que par la clé privée du serveur.

Pour établir une communication chiffrée, le client et le serveur doivent initier un autre handshake. Pendant le handshake, ils s'accordent sur la version de TLS à utiliser et sur la manière dont ils vont chiffrer les données et s'authentifier mutuellement pendant la connexion, un ensemble de règles connu sous le nom de suite de chiffrement (cipher suite).

![Étapes du handshake SSL.](https://cdn.hashnode.com/res/hashnode/image/upload/v1731414891509/541f6b6c-ad54-4301-834a-1056aea524c0.jpeg)

Ce handshake ou négociation TLS commence une fois qu'une connexion TCP a été établie, et comprend les étapes suivantes :

-   **Client hello** : Le navigateur envoie un message hello qui inclut toutes les versions de TLS et les suites de chiffrement supportées.
    
-   **Server Hello** : Le serveur répond avec la suite de chiffrement et la version TLS choisies, ainsi que son certificat SSL contenant la clé publique du serveur.
    
-   **Authentification et Pre-Master Key** : Le client vérifie le certificat SSL du serveur auprès de l'autorité de confiance correspondante, puis crée une pre-master key en utilisant la clé publique du serveur (partagée précédemment dans le certificat) et partage cette pre-master key avec le serveur.
    
-   **Déchiffrement de la Pre-master key** : La pre-master key ne peut être déchiffrée qu'à l'aide de la clé privée du serveur. Si le serveur est capable de la déchiffrer, le client et le serveur peuvent alors s'accorder sur un secret maître partagé (shared master secret) à utiliser pour la session.
    
-   **Client ChangeCipherSpec** : Le client crée une clé de session en utilisant le secret maître partagé et envoie au serveur tous les enregistrements précédemment échangés, cette fois chiffrés avec la clé de session.
    
-   **Server ChangeCipherSpec** : Si le serveur génère la clé de session correcte, il sera en mesure de déchiffrer le message et de vérifier l'enregistrement reçu. Le serveur envoie ensuite un enregistrement pour confirmer que le client dispose également des clés correctes.
    
-   **Connexion sécurisée établie** : Le handshake est terminé.
    

Une fois le handshake terminé, toute la communication entre le client et le serveur est protégée par un chiffrement symétrique utilisant la clé de session, et le navigateur peut effectuer la première requête HTTP GET pour le site.

### Time to First Byte {#heading-time-to-first-byte}

Une fois la requête du navigateur approuvée, le serveur enverra un message 200 OK ainsi que les en-têtes de réponse et le contenu demandé. S'agissant d'un site web, le contenu est probablement un document HTML.

Les données voyagent entre le client et le serveur divisées en une série de petits morceaux de données, appelés paquets de données. Cela facilite le remplacement des morceaux de données corrompus si nécessaire et permet également aux données de voyager vers et depuis différents endroits, permettant à plusieurs utilisateurs d'accéder aux données plus rapidement et en même temps.

Lorsque la première requête est faite par le client, le premier paquet qui arrive en réponse marque le [Time to First Byte][33] (**TTFB**), qui représente le temps écoulé entre le moment où la requête a été initiée et celui où le premier morceau de données a été reçu en réponse. Il inclura le temps pris pour la recherche DNS, le handshake TCP pour établir la connexion, et le handshake TLS si la requête est faite via HTTPS.

## Des données aux pixels : le chemin critique du rendu {#heading-des-donnees-aux-pixels-le-chemin-critique-du-rendu}

Le [Chemin critique du rendu][34] (**CRP** pour Critical Rendering Path) est une série d'étapes que le navigateur effectue pour transformer les données reçues du serveur en pixels sur l'écran. Il comprend la création du [Document Object Model][35] (**DOM**) et du [CSS Object Model][36] (**CSSOM**), l'**arbre de rendu** et le **layout**.

### Construction de l'arbre DOM {#heading-construction-de-l-arbre-dom}

Lorsque le premier morceau de données arrive, le navigateur commence le parsing du HTML. Le parsing signifie analyser et convertir un morceau de code d'entrée en une syntaxe et une représentation qui peuvent être interprétées par un runtime spécifique. Dans ce cas, le navigateur assemble les paquets de données reçus et parse le HTML, construisant une représentation du document sous forme d'arbre de nœuds connu sous le nom d'arbre DOM.

Chaque balise HTML du document est représentée comme un nœud dans l'arbre DOM. Les nœuds sont connectés à l'arbre DOM selon leur position hiérarchique dans le document, et la représentation de chaque nœud inclut toutes les informations pertinentes sur la balise.

Pour le code HTML suivant :

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>What Really Happens When You Navigate to a Website</title>
</head>
<body>
    <main>
        <header>
            <h1>What Really Happens When You Navigate to a Website</h1>
        </header>

        <section>
            <h2>Intro</h2>
            <p>
                Before entering into the details of every step included in the process, let's review some of the basic concepts we will be discussing throughout the blog.
            </p>
            <p>
                The Internet is a huge network of interconnected computers. The World Wide Web (aka web) is built on top of that technology, as well as other services such as email, chat systems, or file sharing.
            </p>

            <p>Computers connected to the internet are either:</p>
            <ul>
                <li>
                    <p>Clients, the web user's devices and the software that those devices use to access the web.</p>
                </li>
                <li>
                    <p>Servers, computers that store web pages, sites, or apps and the files they need to be displayed in the user's web browser or devices.</p>
                </li>
            </ul>
        </section>
    </main>

    <footer>
        <p>© 2024</p>
    </footer>
</body>
</html>
```

L'arbre DOM résultant ressemble à ce qui suit :

![L'arbre DOM inclut tous les éléments HTML, leur contenu et leurs relations hiérarchiques.](https://cdn.hashnode.com/res/hashnode/image/upload/v1731498370760/4267c646-145e-487c-83af-f97d6f8ce21d.jpeg)

Pendant le parsing du HTML, le navigateur effectue des requêtes supplémentaires pour les ressources rencontrées. Les fichiers CSS et les images sont des ressources non bloquantes, ce qui signifie que le parseur continuera sa tâche en attendant les ressources demandées. Mais si une balise `<script>` est trouvée, le parsing HTML s'arrêtera, impactant le temps du premier rendu.

### Construction de l'arbre CSSOM {#heading-construction-de-l-arbre-cssom}

Alors que le DOM contient toutes les informations sur le contenu de la page et sa hiérarchie, le CSSOM contient les informations sur la façon de styliser la page.

Dans le CSSOM, chaque élément HTML est associé à ses styles CSS correspondants. Le résultat est un arbre qui ne contient pas d'informations sur le contenu des éléments, mais sur la façon dont ils doivent être affichés.

Étant donné le code CSS suivant :

```
* {
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f9;
    color: #333;
}

main {
    padding: 20px;
    max-width: 800px;
    margin: 0 auto;
}

header {
    background-color: #005bbb;
    color: #ffffff;
    padding: 10px;
    text-align: center;
}

h1 {
    font-size: 24px;
}

section {
    margin-top: 20px;
}

h2 {
    font-size: 20px;
    color: #005bbb;
    display: none;
}

p {
    margin-bottom: 10px;
}

ul {
    margin-left: 20px;
    list-style-type: disc;
}

footer {
    margin-top: 40px;
    text-align: center;
    font-size: 14px;
    color: #555;
}
```

Lorsque le navigateur le traite, le CSSOM résultant ressemblera à ceci :

![L'arbre CSSOM inclut chaque élément HTML et ses styles correspondants.](https://cdn.hashnode.com/res/hashnode/image/upload/v1731496962735/f3cb0399-a9fb-48cc-8043-00608d1236db.jpeg)

Sa création n'est pas incrémentale, ce qui signifie que le navigateur arrête le rendu de la page jusqu'à ce qu'il ait traité tout le CSS.

Cela fonctionne ainsi car, comme son nom l'indique, les feuilles de style en cascade (**CSS**) appliquent les styles de haut en bas, ce qui signifie que les classes définies plus tard écrasent celles du début du document. Un document CSS doit être entièrement traité avant d'afficher quoi que ce soit à l'écran, car certaines classes peuvent changer.

### Compilation et exécution JavaScript {#heading-compilation-et-execution-javascript}

Pendant la création du CSSOM, le rendu est bloqué, mais le navigateur continue de télécharger tous les fichiers JavaScript qu'il rencontre.

Le JavaScript est également parsé, compilé et interprété par le navigateur, mais comme mentionné précédemment, il s'agit par défaut d'une ressource bloquant le parsing. Cela signifie que lorsque le navigateur rencontre une balise `<script>`, il arrête le parsing HTML et exécute le fichier avant de continuer. Les attributs `async` ou `defer` peuvent être utilisés pour éviter ce comportement, permettant au parsing de continuer pendant que la ressource est récupérée.

Une fois que le navigateur a terminé le parsing et exécuté tous les fichiers JavaScript susceptibles de modifier le DOM et le CSSOM, l'étape suivante consiste à construire l'arbre de rendu. Cependant, avant de voir cette étape en détail, prenons un moment pour nous concentrer sur l'arbre d'accessibilité.

### Construction de l'arbre d'accessibilité {#heading-construction-de-l-arbre-d-accessibilite}

Sur la base de la structure du site créée dans l'arbre DOM, le navigateur crée également un arbre d'accessibilité.

L'arbre d'accessibilité est une autre représentation du contenu du site, spécifiquement conçue pour permettre la navigation sur le site à l'aide de [technologies d'assistance][37].

Dans l'arbre d'accessibilité, chaque élément DOM est représenté comme un objet accessible, contenant les informations suivantes :

-   **Nom** : Un identifiant utilisé pour désigner l'élément.
    
-   **Description** : Informations supplémentaires sur l'élément.
    
-   **Rôle** : Le type d'élément dont il s'agit, lié à son utilisation prévue.
    
-   **État** et autres propriétés : Si l'élément est sujet à changement, il peut inclure son état actuel. Il peut également inclure d'autres propriétés spécifiant d'autres fonctionnalités.
    

Dans les principaux navigateurs web, vous pouvez accéder aux objets accessibles et à leurs informations en sélectionnant un nœud dans l'inspecteur d'arbre DOM, puis en naviguant vers l'onglet "Accessibilité".

![Une liste non ordonnée sélectionnée et l'onglet accessibilité dans Chrome Dev Tools.](https://cdn.hashnode.com/res/hashnode/image/upload/v1731578933460/0a8c7a78-c19a-4d19-a96a-fabd19772156.png)

![Une liste non ordonnée sélectionnée et l'onglet accessibilité dans Firefox Dev Tools.](https://cdn.hashnode.com/res/hashnode/image/upload/v1731579023128/85aeb312-1632-49c3-80cb-0d5db8ec8502.png)

Avoir un arbre d'accessibilité bien structuré est essentiel pour déterminer si un site sera navigable à l'aide de technologies d'assistance, faisant la différence entre l'inclusion et l'exclusion.

### Arbre de rendu (Render tree) {#heading-arbre-de-rendu}

Après avoir construit les arbres DOM, CSSOM et d'accessibilité, le navigateur construit l'arbre de rendu.

Cet arbre est une combinaison des arbres DOM et CSSOM. Le navigateur traite tous les nœuds et ne conserve que ceux qui sont visibles. Ensuite, il les combine avec leurs règles CSSOM correspondantes. Le résultat est une collection de tous les éléments visibles associés à leurs styles calculés.

Les nœuds non visibles, tels que les balises `<script>` ou `<meta>`, ainsi que les éléments cachés avec la propriété CSS `display: none`, ne sont pas inclus dans cet arbre.

![L'arbre de rendu est créé à partir des arbres DOM et CSSOM.](https://cdn.hashnode.com/res/hashnode/image/upload/v1731501603172/d3467e9a-e75b-4217-875b-58684edfdbc0.jpeg)

### Layout {#heading-layout}

Une fois l'arbre de rendu calculé, le navigateur exécute le layout. Dans ce processus, le navigateur calcule la position exacte et la taille que chaque élément occupera dans la page.

Ces calculs sont basés sur la taille du viewport, la zone du navigateur qui affichera réellement le contenu du site. La taille du viewport varie en fonction de la taille de l'écran de l'appareil, de la taille de la fenêtre du navigateur, des paramètres du système et d'autres conditions.

La sortie du layout est un modèle de boîte (box model) qui capture la taille et la position correspondant à chaque élément et objet présent dans l'arbre de rendu. Le navigateur commence à traiter le document généralement à partir de la balise `<body>` et parcourt tous ses descendants.

Après le calcul du layout, tout changement dans la taille ou la position d'un ou plusieurs éléments dans le document déclenchera de nouveaux calculs. Ces calculs suivants sont appelés reflows.

### Painting {#heading-painting}

Enfin, l'étape finale consiste à afficher la sortie du layout sur l'écran de l'utilisateur. Pendant la phase de painting ou de rastérisation, le navigateur convertit chaque élément de boîte du layout en pixels correspondants sur l'écran.

Une représentation visuelle de l'ensemble de la page est initialement rendue à l'écran, puis seules les zones affectées par des changements sont rendues à nouveau.

De nombreux facteurs impactent le temps nécessaire au navigateur pour effectuer cette étape, et il existe des outils qui aident les développeurs à mesurer et optimiser ce temps.

Après le painting, et avant que les utilisateurs ne puissent commencer à interagir avec le site web, le navigateur peut exécuter tout JavaScript qui a été différé à l'aide des attributs `defer` ou `async` pour éviter de bloquer le parsing HTML initial.

### Une note sur l'hydratation JavaScript {#heading-une-note-sur-l-hydratation-javascript}

Les étapes décrites ci-dessus montrent le processus de rendu de tout le code HTML, CSS et JavaScript du site web dans le navigateur. C'est ce qu'on appelle le Client-Side Rendering (CSR). Vous avez peut-être aussi entendu parler du Server-Side Rendering (SSR).

Le SSR consiste à rendre le contenu d'un site web lors de chaque requête et à le livrer au client sous forme de HTML prêt à être affiché dans le navigateur.

Lorsqu'un site est rendu en utilisant le CSR, tout le JavaScript est exécuté avant que la page ne soit rendue. En SSR, le HTML rendu par le serveur se charge et s'affiche rapidement dans le navigateur, mais le JavaScript doit toujours être envoyé au client pour permettre l'interaction de l'utilisateur.

L'hydratation JavaScript est le processus par lequel le JavaScript est ajouté à une page HTML rendue par le serveur pour la rendre interactive. Une fois que le HTML initial est servi et affiché dans le navigateur, le JavaScript "hydrate" le contenu statique, en attachant des écouteurs d'événements et en activant les fonctionnalités interactives.

## Conclusion {#heading-conclusion}

Tout au long de cet article, vous avez approfondi votre compréhension de ce qui se passe entre le moment où vous tapez une adresse web dans la barre d'adresse de votre navigateur et celui où vous accédez au contenu du site que vous recherchez.

Vous avez découvert les URL et la recherche DNS effectuée par le navigateur pour trouver l'adresse IP du site. Vous avez également appris comment les connexions sont établies entre le navigateur et les serveurs et comment ils communiquent.

Enfin, vous avez exploré ce qui se passe entre la réception du premier morceau de données du serveur et l'affichage du site sur votre écran, ainsi que des concepts clés tels que l'arbre d'accessibilité et le processus d'hydratation JavaScript.

J'espère que vous avez apprécié ce guide et qu'il vous a été utile. Merci de m'avoir lu !

[1]: #heading-trouver-une-ressource-les-url
[2]: #heading-correspondance-entre-ip-et-url-la-resolution-dns
[3]: #heading-qu-est-ce-que-le-resolveur-dns
[4]: #heading-qu-est-ce-que-le-serveur-dns-racine
[5]: #heading-qu-est-ce-que-le-serveur-de-domaine-de-premier-niveau
[6]: #heading-serveur-de-noms-faisant-autorite
[7]: #heading-etablir-une-connexion-le-modele-tcp-ip
[8]: #heading-comment-fonctionne-la-connexion-tcp
[9]: #heading-le-three-way-handshake-tcp
[10]: #heading-demarrer-l-echange-communication-client-serveur
[11]: #heading-qu-est-ce-que-le-protocole-http
[12]: #heading-requete-reponse-http
[13]: #heading-https
[14]: #heading-time-to-first-byte
[15]: #heading-des-donnees-aux-pixels-le-chemin-critique-du-rendu
[16]: #heading-construction-de-l-arbre-dom
[17]: #heading-construction-de-l-arbre-cssom
[18]: #heading-compilation-et-execution-javascript
[19]: #heading-construction-de-l-arbre-d-accessibilite
[20]: #heading-arbre-de-rendu
[21]: #heading-layout
[22]: #heading-painting
[23]: #heading-une-note-sur-l-hydratation-javascript
[24]: #heading-conclusion
[25]: https://en.wikipedia.org/wiki/Domain_Name_System
[26]: https://en.wikipedia.org/wiki/Top-level_domain
[27]: https://en.wikipedia.org/wiki/Transmission_Control_Protocol
[28]: https://en.wikipedia.org/wiki/Internet_Protocol
[29]: https://en.wikipedia.org/wiki/Internet_protocol_suite
[30]: https://en.wikipedia.org/wiki/User_Datagram_Protocol
[31]: https://en.wikipedia.org/wiki/HTTP
[32]: https://en.wikipedia.org/wiki/HTTPS
[33]: https://developer.mozilla.org/en-US/docs/Glossary/Time_to_first_byte
[34]: https://developer.mozilla.org/en-US/docs/Web/Performance/Critical_rendering_path
[35]: https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model
[36]: https://developer.mozilla.org/en-US/docs/Web/API/CSS_Object_Model
[37]: https://en.wikipedia.org/wiki/Web_accessibility#Assistive_technologies_used_for_web_browsing