---
title: Comment utiliser Medusa pour des attaques par force brute multi-protocoles
  rapides – Tutoriel de sécurité
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2024-10-02T14:25:10.439Z'
originalURL: https://freecodecamp.org/news/how-to-use-medusa-for-fast-multi-protocol-brute-force-attacks-security-tutorial
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1727713757103/5146e802-f632-475a-9a3c-ea69827fbefe.jpeg
tags:
- name: Security
  slug: security
- name: '#cybersecurity'
  slug: cybersecurity-1
seo_title: Comment utiliser Medusa pour des attaques par force brute multi-protocoles
  rapides – Tutoriel de sécurité
seo_desc: 'As a pentester (a fancy term for an ethical hacker), you will often attack
  systems the same way a malicious hacker does. But your goal will be to find weaknesses
  – so teams can work to address them. One such system is password-based authentication.

  B...'
---

En tant que pentesteur (un terme sophistiqué pour désigner un hacker éthique), vous attaquerez souvent les systèmes de la même manière qu'un hacker malveillant. Mais votre objectif sera de trouver des faiblesses — afin que les équipes puissent s'efforcer de les corriger. L'un de ces systèmes est l'authentification par mot de passe.

Les attaques par force brute sont une méthode courante utilisée pour craquer des mots de passe. Elles fonctionnent en essayant de nombreuses combinaisons de noms d'utilisateur et de mots de passe.

Cela peut prendre du temps. Mais des outils comme Medusa peuvent aider. Ils rendent le processus plus rapide et plus efficace.

Dans cet article, nous allons apprendre à utiliser Medusa pour des attaques par force brute multi-protocoles rapides. Je vous guiderai à travers les bases de l'installation, de l'utilisation et quelques exemples pratiques.

**Note : Les attaques par force brute sont illégales à moins que vous n'ayez l'autorisation explicite de tester le système. Medusa est un outil puissant et peut facilement submerger un serveur s'il n'est pas utilisé avec précaution. Assurez-vous d'avoir l'autorisation du propriétaire du système avant de l'utiliser.**

## Qu'est-ce que Medusa ?

[Medusa](https://www.kali.org/tools/medusa/) est un outil en ligne de commande open-source conçu pour le craquage rapide de mots de passe par force brute. Il prend en charge de nombreux protocoles, tels que FTP, SSH, HTTP, et d'autres.

Les professionnels de la sécurité utilisent Medusa pour identifier les mots de passe faibles ou par défaut. Les attaquants peuvent facilement exploiter ces mots de passe. En simulant une attaque par force brute, Medusa peut révéler des failles de sécurité, nous permettant de les corriger avant qu'une véritable attaque ne se produise.

La connexion parallèle de Medusa lui permet d'attaquer par force brute plusieurs cibles à la fois. C'est la clé de la rapidité de Medusa.

**Caractéristiques principales de Medusa :**

* **Multi-threadé** : Permet des tentatives de force brute simultanées et rapides.
    
* **Prend en charge de nombreux protocoles** : FTP, SSH, HTTP, RDP, MySQL, et plus encore.
    
* **Modulaire** : Vous pouvez facilement ajouter la prise en charge de nouveaux services ou protocoles.
    

Maintenant, plongeons dans l'installation et l'utilisation de Medusa.

## Comment installer Medusa

Medusa ne peut s'exécuter que sur Linux et Mac.

Pour Linux (Debian/Ubuntu), vous pouvez l'installer en utilisant le gestionnaire de paquets APT, comme ceci :

```plaintext
sudo apt install medusa
```

Pour Mac, vous pouvez utiliser Homebrew :

```plaintext
brew install medusa
```

Vous pouvez vérifier l'installation en tapant "medusa" dans votre terminal. S'il est installé correctement, cela affichera le menu d'aide de Medusa.

![Menu d'aide de Medusa](https://cdn.hashnode.com/res/hashnode/image/upload/v1727713805524/86b3bfa0-de7e-470d-8482-310a3aa5f37a.png align="center")

## Comment travailler avec Medusa

Après avoir installé Medusa, vous pouvez l'utiliser pour attaquer par force brute différents protocoles. Passons en revue la syntaxe de base et quelques cas d'utilisation courants.

La syntaxe générale de Medusa ressemble à ceci :

```plaintext
medusa -h [IP cible] -u [nom d'utilisateur] -P [liste de mots de passe] -M [module] -t [threads]
```

* `-h` : Spécifie l'hôte cible (adresse IP ou nom de domaine).
    
* `-u` : Définit le nom d'utilisateur à utiliser pendant l'attaque par force brute.
    
* `-P` : Spécifie le chemin vers le fichier de liste de mots de passe.
    
* `-M` : Sélectionne le module ou le protocole (tel que SSH, FTP ou HTTP).
    
* `-t` : Définit le nombre de threads pour les connexions parallèles (par défaut 16).
    

### Exemple 1 : Attaque par force brute sur SSH

Supposons que nous voulions attaquer par force brute une connexion SSH sur un serveur distant avec l'adresse IP `192.168.1.100`. Nous avons un nom d'utilisateur `admin` et une liste de mots de passe située à `/usr/share/wordlists/passwords.txt`.

La commande ressemblerait à ceci :

```plaintext
medusa -h 192.168.1.100 -u admin -P /usr/share/wordlists/passwords.txt -M ssh -t 10
```

Cette commande indique à Medusa de :

* Cibler `192.168.1.100`.
    
* Utiliser le module `ssh`.
    
* Tenter de se connecter en tant qu'utilisateur `admin`.
    
* Utiliser les mots de passe répertoriés dans le fichier `/usr/share/wordlists/passwords.txt`.
    
* Utiliser 10 threads parallèles pour une exécution plus rapide.
    

### Exemple 2 : Attaque par force brute sur FTP

Pour une attaque par force brute FTP, la commande est assez similaire. Imaginez que le serveur FTP soit à `192.168.1.105`, et que nous ciblions le nom d'utilisateur `user123` avec une liste de mots de passe.

Voici la commande :

```plaintext
medusa -h 192.168.1.105 -u user123 -P /usr/share/wordlists/passwords.txt -M ftp -t 8
```

Cette commande tentera de trouver le mot de passe pour `user123` en utilisant le protocole FTP. Elle utilisera 8 threads parallèles pour un résultat plus rapide.

### Exemple 3 : Force brute de connexion HTTP

Attaquer par force brute une page de connexion HTTP peut être un peu plus compliqué. Vous devez connaître les champs du formulaire pour le nom d'utilisateur et le mot de passe, et parfois, l'URL de l'action de connexion. Voici un exemple de force brute pour une connexion HTTP :

```plaintext
medusa -h example.com -U usernames.txt -P passwords.txt -M http -m FORM:/login.php:username_field=password_field -t 5
```

Dans cet exemple :

* `-U` : Spécifie une liste de noms d'utilisateur.
    
* `-m` : Spécifie un module personnalisé pour la force brute de formulaire HTTP. Le format est `FORM:[URL de l'action de connexion]:[champ utilisateur]=[champ mot de passe]`.
    
* `-t 5` : Exécute cinq threads parallèles.
    

Cette commande tentera de forcer la connexion pour les utilisateurs listés dans `usernames.txt` en utilisant les mots de passe de `passwords.txt` sur le formulaire HTTP situé à `/login.php`.

## Comment personnaliser les attaques Medusa

Medusa est hautement personnalisable. Vous pouvez tout contrôler, du nombre de threads à la liste de mots de passe et au comportement de l'attaque. Explorons quelques options de personnalisation.

### Personnalisation du nombre de threads

Le drapeau `-t` vous permet d'ajuster le nombre de threads utilisés par Medusa. Plus de threads signifient des attaques plus rapides, mais cela peut submerger la cible ou votre système.

Par exemple, pour utiliser 20 threads :

```plaintext
medusa -h 192.168.1.100 -u admin -P passwords.txt -M ssh -t 20
```

### Ciblage de plusieurs hôtes

Vous pouvez également cibler plusieurs hôtes en utilisant l'option `-H` avec un fichier contenant une liste d'IP. Par exemple :

```plaintext
medusa -H hosts.txt -u admin -P passwords.txt -M ssh -t 10
```

Dans ce cas, `hosts.txt` est un fichier qui contient une liste d'IP cibles. Medusa tentera de forcer les connexions SSH sur chacun de ces hôtes.

### Utilisation de plusieurs noms d'utilisateur

Si vous souhaitez essayer plusieurs noms d'utilisateur, vous pouvez utiliser l'option `-U` pour fournir un fichier listant les noms d'utilisateur :

```plaintext
medusa -h 192.168.1.100 -U users.txt -P passwords.txt -M ssh -t 10
```

Ceci testera chaque nom d'utilisateur dans `users.txt` par rapport à la cible, en utilisant les mots de passe de `passwords.txt`.

## Conclusion

Medusa est un outil polyvalent et puissant pour effectuer des attaques par force brute et identifier les mots de passe faibles. Vous pouvez cibler des services tels que SSH, FTP et HTTP, entre autres. Vous pouvez personnaliser l'attaque en ajustant le nombre de threads, en ciblant plusieurs hôtes ou en utilisant différentes listes de mots (wordlists).

J'espère que ce tutoriel vous a aidé à comprendre comment utiliser Medusa. Pour plus d'articles sur la cybersécurité, rejoignez notre newsletter gratuite [Stealth Security](https://www.stealthsecurity.sh/). Pour travailler avec Medusa et d'autres outils via des laboratoires pratiques, consultez notre communauté privée [The Hacker’s Hub](https://www.skool.com/hackershub).