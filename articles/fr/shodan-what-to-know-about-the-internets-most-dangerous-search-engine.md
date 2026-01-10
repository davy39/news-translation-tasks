---
title: Shodan – Ce qu'il faut savoir sur le moteur de recherche le plus dangereux
  d'Internet
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2024-09-10T17:43:12.373Z'
originalURL: https://freecodecamp.org/news/shodan-what-to-know-about-the-internets-most-dangerous-search-engine
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1725990169364/3181020e-abd0-4943-a461-830c2a416035.png
tags:
- name: hacking
  slug: hacking
- name: '#cybersecurity'
  slug: cybersecurity-1
- name: ethicalhacking
  slug: ethicalhacking
seo_title: Shodan – Ce qu'il faut savoir sur le moteur de recherche le plus dangereux
  d'Internet
seo_desc: 'Shodan is a search engine that discovers devices connected to the internet.
  In this article, we’ll look at why it’s both a valuable tool and a potential threat.

  When you hear the term “search engine,” your mind likely jumps to Google, Bing,
  or Yahoo....'
---

Shodan est un moteur de recherche qui découvre les appareils connectés à Internet. Dans cet article, nous verrons pourquoi c’est à la fois un outil précieux et une menace potentielle.

Quand vous entendez le terme « moteur de recherche », votre esprit se tourne probablement vers Google, Bing ou Yahoo. Ces plateformes sont familières pour la plupart d’entre nous, nous aidant à trouver des sites web, des images et des actualités.

Mais il existe un autre moteur de recherche, dont la plupart des gens n’ont jamais entendu parler. Et il est bien plus puissant et dangereux. Il s’appelle [Shodan](https://www.shodan.io/).

Shodan est une base de données d'appareils en ligne, dont beaucoup ne sont pas destinés à être publics. Ce qui est effrayant avec Shodan, c’est qu'il peut aussi répertorier l'un de vos appareils.

Voyons ce qu'est Shodan, comment il fonctionne et pourquoi il représente à la fois un outil précieux et une menace potentielle.

### Qu'est-ce que Shodan ?

Shodan est un moteur de recherche qui découvre les appareils connectés à Internet. Cela inclut tout, des simples webcams et routeurs aux systèmes de contrôle industriel complexes.

Les moteurs de recherche traditionnels indexent des sites web. Shodan scanne Internet à la recherche d'appareils et les répertorie en fonction de leurs adresses IP, de leurs ports ouverts et d'autres données publiquement disponibles.

Shodan fonctionne en scannant Internet à l'aide de protocoles spécifiques pour identifier les appareils connectés. Il collecte toutes les informations sur l'appareil.

Celles-ci incluent les adresses IP, les ports ouverts et même les versions de logiciels utilisées. Ces données sont ensuite rendues consultables en permettant aux utilisateurs d'interroger la base de données. Vous pouvez rechercher des types d'appareils spécifiques ou des vulnérabilités à l'aide de l'interface utilisateur de Shodan ou de l'outil CLI.

Voyons comment vous pouvez utiliser Shodan via l'interface web et la ligne de commande.

### Comment utiliser l'interface web de Shodan

Allez sur [shodan.io](https://www.shodan.io) et créez un compte. Bien que certaines recherches soient possibles sans compte, vous devrez vous connecter pour accéder à la plupart des fonctionnalités.

De plus, vous aurez besoin d'un compte premium pour trouver la plupart des appareils, car les résultats du plan gratuit sont très limités.

![Shodan home page](https://cdn.hashnode.com/res/hashnode/image/upload/v1726210817675/e3c7f492-7b0d-4914-be7a-6cf8dc26524a.png align="left")

Sur la page d'accueil, vous verrez une simple barre de recherche. Vous pouvez taper des requêtes générales comme « default password » ou « webcam » pour voir ce que Shodan peut trouver.

Par exemple, taper « default password » listera les appareils avec des paramètres par défaut. Ils sont vulnérables aux accès non autorisés.

Shodan vous permet également de filtrer les résultats avec des paramètres spécifiques. Par exemple :

* **Rechercher des appareils spécifiques** : Si vous recherchez des webcams, vous pouvez taper « webcam country:US ». Cette requête retournera les webcams situées aux États-Unis.
    
* **Rechercher par adresse IP** : Pour voir les détails d'une IP spécifique, tapez l'adresse IP dans la barre de recherche.
    
* **Rechercher par port** : Pour trouver des appareils avec un port spécifique ouvert, utilisez une requête comme « port:22 ». Cela trouvera les appareils dont le service SSH (port 22) est exposé sur Internet.
    

Après avoir exécuté une recherche, Shodan présentera une liste d'appareils correspondants. Chaque résultat inclut l'adresse IP, les ports ouverts et le logiciel sur l'appareil.

Par exemple, une recherche pour « port:22 » pourrait trouver des serveurs SSH et leurs détails de configuration.

![Shodan search results](https://cdn.hashnode.com/res/hashnode/image/upload/v1726210856807/253a6a4c-e418-4a8f-ad3d-553a4a339686.png align="left")

### Comment utiliser l'interface en ligne de commande (CLI) de Shodan

Pour les utilisateurs avancés, Shodan propose une interface en ligne de commande (CLI). Elle permet de rechercher et d'automatiser des tâches.

**Note : L'utilisation de l'API peut être limitée en fonction de votre compte et vous devrez peut-être payer pour l'utiliser.**

Avant de pouvoir utiliser la CLI, vous devrez l'installer. Vous pouvez le faire en utilisant le gestionnaire de paquets de Python, pip. Ouvrez votre terminal et tapez ce qui suit :

```plaintext
pip install shodan
```

Une fois installé, vous pouvez vérifier si cela fonctionne en essayant la commande d'aide.

```plaintext
shodan -h
```

![Shodan help](https://cdn-images-1.medium.com/max/1600/1*j-AeWDwmtsLvczJEj1U2yQ.png align="left")

Maintenant, vous devez configurer votre CLI Shodan avec votre clé API. Vous pouvez trouver votre clé API sur votre [page de compte Shodan](https://account.shodan.io/). Pour la configurer, utilisez la commande suivante :

```plaintext
shodan init VOTRE_CLE_API
```

Vous pouvez maintenant commencer à chercher. Voici un exemple de recherche basique :

```plaintext
shodan search "default password"
```

Cette commande retournera les appareils ayant « default password » dans leurs bannières. Cela indique souvent de mauvaises pratiques de sécurité.

Vous pouvez rechercher des appareils avec des caractéristiques spécifiques comme précédemment :

```plaintext
shodan search "port:80 country:US"
```

Cette commande trouve les serveurs web (port 80) situés aux États-Unis.

Pour obtenir des informations détaillées sur une adresse IP spécifique, utilisez cette commande :

```plaintext
shodan host 8.8.8.8
```

Elle retournera toutes les données connues sur l'IP spécifiée, y compris les ports ouverts et les services détectés.

Pour voir plus de commandes ou déboguer des problèmes de CLI, [voici la documentation officielle de Shodan](https://help.shodan.io/command-line-interface/0-installation).

### Le bon, le mauvais et le dangereux

Shodan est une arme à double tranchant. C'est un outil puissant pour les professionnels de la cybersécurité. Il pose également des risques importants s'il est utilisé à des fins malveillantes.

Les équipes de sécurité utilisent Shodan pour trouver les appareils exposés au sein de leurs réseaux. Cela leur permet de corriger les vulnérabilités avant que quelqu'un ne puisse les exploiter.

Les chercheurs peuvent suivre les vulnérabilités ou les logiciels malveillants en surveillant les appareils sur Shodan.

Malheureusement, Shodan peut aussi être le rêve d'un hacker. Les hackers peuvent utiliser Shodan pour localiser les appareils exposés sur Internet. Ceux-ci incluent des webcams, des serveurs et même des systèmes de contrôle industriel.

Un fait inquiétant à propos de Shodan est sa capacité à trouver des systèmes de contrôle industriel. Un système de contrôle industriel (ICS) contrôle et surveille les processus industriels. C’est le « cerveau » derrière les machines dans les usines, les centrales électriques et les stations de traitement de l'eau.

Shodan a trouvé des milliers de systèmes de contrôle industriel (ICS) non sécurisés et connectés à Internet. Dans certains cas, ces systèmes n'avaient pas de mot de passe ou utilisaient des identifiants par défaut.

Shodan a également indexé des milliers de caméras de sécurité, de serveurs de bases de données et d'appareils IoT. Cela soulève de sérieuses préoccupations en matière de vie privée et de sécurité. Tous ces éléments peuvent être facilement exploités s'ils ne sont pas correctement sécurisés.

Pour protéger vos propres appareils, vous devez comprendre Shodan. Vous devez savoir comment il fonctionne et ce qu'il peut trouver.

Alors, comment empêcher Shodan d'exposer vos appareils ?

**1. Changez les identifiants par défaut** : Changez toujours les noms d'utilisateur et les mots de passe par défaut sur vos appareils.

2. **Utilisez des mots de passe complexes** : Évitez les mots de passe faibles. Utilisez un mélange de lettres, de chiffres et de symboles, et envisagez d'utiliser un gestionnaire de mots de passe.

3. **Désactivez les services inutiles** : Si votre appareil possède des services que vous n'utilisez pas, désactivez-les. Cela réduit le nombre de vulnérabilités potentielles.

## Conclusion

Shodan est un outil puissant. C'est un rappel que tout appareil connecté à Internet est potentiellement exposé. Il offre des informations utiles pour les experts en cybersécurité, mais aussi une opportunité pour les cybercriminels.

Savoir ce que Shodan peut faire devrait vous inciter à prendre la cybersécurité au sérieux. Dans un monde où tout est connecté, votre sécurité n'est aussi forte que votre appareil le plus faible. Restez informé, restez à jour et, surtout, restez en sécurité.

*Rejoignez la* [***newsletter Stealth Security***](https://www.stealthsecurity.sh/) *pour plus d'articles sur la cybersécurité offensive et défensive. Pour apprendre à bâtir une carrière en cybersécurité, consultez* [***The Hacker's Handbook***](https://book.stealthsecurity.sh/)*.*