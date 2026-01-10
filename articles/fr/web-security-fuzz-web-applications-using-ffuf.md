---
title: Comment Fuzzer des Applications Web avec FFuf – Tutoriel de Sécurité Web
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2022-11-10T17:21:43.000Z'
originalURL: https://freecodecamp.org/news/web-security-fuzz-web-applications-using-ffuf
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/ffuf.png
tags:
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
- name: Web Security
  slug: web-security
seo_title: Comment Fuzzer des Applications Web avec FFuf – Tutoriel de Sécurité Web
seo_desc: 'Building strong authentication systems is crucial for web applications.
  Now that many businesses have a growing online presence, a malicious actor taking
  control of your website can be devastating.

  In this article, we will learn how to use Ffuf, a fa...'
---

Construire des systèmes d'authentification solides est crucial pour les applications web. Maintenant que de nombreuses entreprises ont une présence en ligne croissante, un acteur malveillant prenant le contrôle de votre site web peut être dévastateur.

Dans cet article, nous allons apprendre à utiliser Ffuf, un fuzzer web rapide écrit en Go. Vous apprendrez comment fuzzer pour trouver des répertoires et des fichiers et contourner l'authentification d'un site web en utilisant ffuf. Ensuite, vous apprendrez comment vous défendre contre ces types d'attaques.

Rappelez-vous – pour vous protéger, vous et vos sites web, il est utile de savoir comment un attaquant tenterait de s'infiltrer. Ainsi, vous pourrez plus efficacement les empêcher d'entrer.

**Note :** Avant de plonger dans l'utilisation de ffuf, je tiens à souligner que ce tutoriel est uniquement destiné à vous aider à vous défendre contre les attaques de fuzzing. Si vous utilisez ce matériel à des fins malveillantes, je ne suis pas responsable.

## Qu'est-ce que FFuf ?

Ffuf est un fuzzer écrit dans le [langage de programmation Go](https://go.dev/).

Ffuf appartient à la phase d'exploitation dans le [cycle de vie du pentesting](https://exploitable.manishmshiva.com/ethical-hacking-lifecycle-five-stages-of-a-penetration-test-c201e8e5bbf7). C'est également l'outil de fuzzing open-source le plus rapide disponible sur le marché.

Mais avant de commencer à utiliser Ffuf, comprenons ce qu'est le fuzzing.

## Qu'est-ce que le Fuzzing ?

Le fuzzing est une méthode consistant à envoyer des données malformées ou anormales à un système afin de le faire mal se comporter d'une certaine manière, ce qui pourrait conduire à la découverte de vulnérabilités.

Trouver des fichiers cachés, envoyer des données aléatoires à des formulaires, ou même des tentatives de connexion à des applications web peuvent être considérés comme du fuzzing.

Vous pourriez alors vous demander « En quoi est-ce différent du Brute forcing ? ».

Le brute forcing peut être considéré comme une partie du fuzzing. Dans le brute force, l'attaquant utilise des données valides, par exemple, pour vérifier si une tentative de connexion fonctionne. Mais avec le Fuzzing, ils peuvent envoyer des données aléatoires pour briser le comportement attendu d'un système.

Par exemple, si vous utilisez un outil comme Ffuf et que vous le chargez avec des centaines de combinaisons nom d'utilisateur-mot de passe à essayer sur un site web, c'est du fuzzing. Et c'est exactement ce que nous allons faire en utilisant Ffuf.

Assurez-vous d'avoir une autorisation écrite si vous allez essayer cet outil sur un site web tiers.

## Comment Installer Ffuf et les Wordlists

Ffuf est pré-packagé avec la distribution Kali Linux. Si vous souhaitez installer Ffuf sur votre ordinateur personnel, [voici les instructions](http://ffuf.me/install).

Puisque Ffuf est écrit dans le langage de programmation Go, assurez-vous d'avoir le compilateur Go installé dans votre système avant d'essayer d'installer Ffuf.

Si vous êtes nouveau dans les wordlists, une wordlist est une liste de termes couramment utilisés. Cela peut être une [wordlist de mots de passe](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-100.txt), une [wordlist de noms d'utilisateur](https://github.com/danielmiessler/SecLists/blob/master/Usernames/Names/names.txt), une wordlist de sous-domaines, etc. Vous pouvez trouver beaucoup de [wordlists utiles ici](https://github.com/danielmiessler/SecLists).

Je vous recommande de télécharger [Seclists](https://github.com/danielmiessler/SecLists). Seclists est une collection de plusieurs types de listes utilisées lors des évaluations de sécurité. Cela inclut les noms d'utilisateur, les mots de passe, les URLs, etc. Si vous utilisez Kali Linux, vous pouvez trouver seclists sous /usr/share/wordlists.

Pour essayer cet outil en temps réel, vous pouvez soit utiliser votre propre site web, soit utiliser une application web de pratique comme [Damn Vulnerable Web app](https://github.com/digininja/DVWA) (DVWA). DVWA est une application web vulnérable intentionnellement mal configurée qui est utilisée par les testeurs d'intrusion pour pratiquer les attaques sur les applications web.

## Fuzzing avec Ffuf

Maintenant que vous comprenez ce qu'est le Fuzzing et les Wordlists, commençons à utiliser Ffuf.

Nous allons utiliser ffuf pour fuzzer l'application web afin de découvrir des répertoires, trouver des noms d'utilisateur, énumérer des hôtes virtuels, et même brute-forcer des combinaisons email/mot de passe.

Vous pouvez utiliser la commande d'aide (-h) si vous voulez rapidement consulter les options fournies par Ffuf. Cela est utile car vous n'avez pas à mémoriser toutes les options fournies par Ffuf.

```
ffuf -h
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-26.png)

N'oubliez pas que les paramètres URL (-u) et wordlist (-w) sont toujours requis.

Notez que j'utiliserai [http://localhost:3000](http://localhost:3000) pour mes exemples. Si vous configurez votre propre application web ou utilisez un site web existant, vous devez remplacer « localhost:3000 » par l'adresse IP ou le nom de domaine du site web.

### Comment Énumérer les URLs avec Ffuf

Voyons comment trouver certains chemins d'URL.

Trouver des URLs est utile, surtout si elles sont cachées pour ne pas être indexées publiquement. Nous utiliserons la [wordlist de contenu web](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/big.txt) de seclists pour fuzzer l'application web à la recherche d'URLs cachées.

Vous pouvez utiliser la commande suivante pour rechercher des URLs :

```
ffuf -u http://localhost:3000/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt
```

Ici, le mot-clé « FUZZ » est utilisé comme espace réservé. Ffuf essaiera d'atteindre l'URL en remplaçant le mot « FUZZ » par chaque mot de la wordlist.

Voici ce que j'ai trouvé à partir de DVWA :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-27.png)
_Résultat de la recherche d'URLs_

Intéressant. Vous pouvez voir que nous avons trouvé quelques emplacements (possiblement importants) comme /config, /docs, et /server-status.

Si une application web réelle avait des pages qui n'étaient liées nulle part mais utilisaient des noms standard, Ffuf les repérerait facilement.

### Comment Énumérer les Fichiers avec Ffuf

Et si vous voulez rechercher des fichiers spécifiques ? Heureusement, Ffuf nous fournit l'option d'extension (-e) que nous pouvons utiliser. Nous pouvons dire à Ffuf de rechercher uniquement les fichiers ayant certaines extensions – dans notre cas, .html, .php, et .txt.

Nous utiliserons la wordlist [raft-medium-words](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/raft-medium-words-lowercase.txt) pour cela. Voici la commande pour rechercher des fichiers spécifiques :

```
ffuf -u http://localhost:3000/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-medium-words-lowercase.txt -e .php,.html,.txt
```

Cette commande recherche tous les fichiers à la racine du domaine avec une extension .html, .php, et .txt. Voici le résultat de DVWA :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-28.png)
_Résultat de la recherche de fichiers spécifiques_

Nous avons trouvé une longue liste de fichiers. Même si certains fichiers ne sont pas servis sur l'application web (statut 403), nous pouvons apprendre qu'il y a des fichiers, simplement que nous ne pouvons pas encore y accéder.

Exécutons la même commande, mais maintenant, nous ne rechercherons que les fichiers accessibles au public. Nous utiliserons le drapeau de code de correspondance (-mc) pour ne rechercher que les fichiers avec un statut de 200.

Voici la commande :

```
ffuf -u http://localhost:3000/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-medium-words-lowercase.txt -e .php,.html,.txt -mc 200
```

Et voici le résultat.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-31.png)
_Fichiers accessibles au public_

Vous pouvez voir que nous avons trouvé quelques fichiers auxquels nous pouvons accéder. Le login.php semble intéressant, et nous l'utiliserons pour contourner l'authentification dans les sections suivantes.

### Comment Énumérer les Sous-Domaines avec Ffuf

Vous pouvez également rechercher des sous-domaines dans une application web en utilisant Ffuf.

Vous avez probablement deviné l'approche que nous allons utiliser. Nous allons remplacer le sous-domaine de l'URL par le mot « FUZZ » et essayer de rechercher des URLs qui sont actives.

Puisque mon application web est hébergée sur mon système local, elle ne contient aucun sous-domaine. Mais dans le monde réel, si vous voulez énumérer des sous-domaines, voici la commande. Vous pouvez utiliser la [wordlist de sous-domaines](https://github.com/danielmiessler/SecLists/blob/master/Discovery/DNS/subdomains-top1million-5000.txt) de seclists.

```
ffuf -u http://FUZZ.mydomain.com -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
```

### Comment Trouver des Noms d'Utilisateur avec Ffuf

Avez-vous été ennuyé lorsque les applications web ne vous disent pas si vous avez le mauvais nom d'utilisateur ou mot de passe ? Elles se contentent de vous dire « Cette combinaison ne fonctionne pas ».

Cela est fait pour protéger l'application web contre les attaques de fuzzing de nom d'utilisateur/email. Si les systèmes d'authentification vous donnent des informations spécifiques sur votre tentative de connexion, il devient plus facile pour les attaquants de brute forcer et de découvrir une liste de noms d'utilisateur ou d'emails.

Supposons que notre application web vous indique que vous avez le mauvais nom d'utilisateur avec le message « le nom d'utilisateur n'existe pas ». Nous pouvons utiliser ce message d'erreur pour trouver des noms d'utilisateur valides avec la commande suivante :

```
ffuf -w /usr/share/SecLists/Usernames/top-usernames-shortlist.txt -X POST -d "username=FUZZ&&password=x" -H "Content-Type: application/x-www-form-urlencoded" -u http://mydomain.com/login -mr "username already exists"
```

Ici, nous envoyons des requêtes POST à la page de connexion, avec les noms d'utilisateur fuzzés et un mot de passe factice pour vérifier si le message d'erreur attendu est retourné. Vous pouvez utiliser une [wordlist de noms d'utilisateur](https://github.com/danielmiessler/SecLists/blob/master/Usernames/top-usernames-shortlist.txt) de seclists pour le fuzzing.

Le drapeau -mr est utilisé pour faire correspondre une expression régulière. Vous pouvez avoir des expressions régulières compliquées ou un simple message de chaîne pour valider les requêtes.

Voici un exemple de réponse.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-32.png)

### Brute Forcing avec Ffuf

Maintenant, faisons un peu de brute forcing avec Ffuf. Nous allons essayer un tas de combinaisons courantes de nom d'utilisateur/mot de passe et voir si quelque chose fonctionne.

Si l'application web que vous testez utilise une combinaison d'email et de mot de passe, vous pouvez remplacer la wordlist de nom d'utilisateur par une wordlist d'email.

Pour cette attaque, nous avons besoin de deux paramètres : nom d'utilisateur et mot de passe. De plus, nous utiliserons deux wordlists : comme vous l'avez deviné, une wordlist de noms d'utilisateur et une wordlist de mots de passe.

En plus du placeholder par défaut **FUZZ**, Ffuf supporte l'utilisation de variables. Nous utiliserons donc W1 pour notre wordlist de noms d'utilisateur et W2 pour la wordlist de mots de passe.

Voici la commande :

```
ffuf -w usernames.txt:W1,/usr/share/wordlists/SecLists/Passwords/Common-Credentials/10-million-password-list-top-100.txt:W2 -X POST -d "username=W1&password=W2" -H "Content-Type: application/x-www-form-urlencoded" -u http://localhost:3000/login -fc 200
```

Si Ffuf trouve des combinaisons valides, vous verrez la combinaison dans les résultats. Vous pouvez également filtrer par codes de statut (par exemple, filtrer 400 ou rechercher 200) en utilisant les drapeaux -fc ou -mc pour réduire le bruit.

Voici un exemple de réponse.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-33.png)

C'était amusant, n'est-ce pas ? Nous pouvons trouver beaucoup d'informations intéressantes sur une application web sans utiliser un outil compliqué comme [Burpsuite](https://www.kali.org/tools/burpsuite/).

## Comment Protéger Votre Site du Fuzzing

Mais puisque nous ne sommes pas les attaquants malveillants, voyons comment se défendre contre le fuzzing.

Le moyen le plus simple de protéger votre site web contre les attaques de fuzzing est de faire attention au type de fichiers sur le serveur web. Si vous ne voulez pas que quelque chose soit trouvé, ne le mettez pas sur le serveur web.

Pour prévenir le contournement de l'authentification, il est important de ne pas permettre plusieurs tentatives de connexion. La plupart des sites web modernes ne permettent pas plus de 5 tentatives de connexion consécutives. Il est plus sécurisé de demander à vos utilisateurs de réinitialiser leurs mots de passe par email plutôt que de les laisser essayer plusieurs combinaisons.

Vous devez également faire attention aux messages d'erreur retournés en cas de tentatives échouées. Afficher que « L'email n'existe pas » ou « Le mot de passe n'est pas correct » permettra au pirate de savoir qu'un email ou un nom d'utilisateur existe. Cela ne fait que faciliter leur travail.

Enfin, vous pouvez utiliser des [Pare-feu d'Applications Web](https://www.cloudflare.com/en-gb/learning/ddos/glossary/web-application-firewall-waf/) (WAF) pour surveiller le trafic et bloquer les adresses IP suspectes. Les WAF ont également des options pour définir des alertes s'ils rencontrent des tentatives de brute forcing sur vos méthodes d'authentification.

## Résumé

Ffuf est un excellent outil à avoir dans votre boîte à outils de pentesting. C'est un fuzzer simple mais rapide qui facilite l'énumération des répertoires, la découverte des hôtes virtuels et le brute-forcing des applications web.

Ffuf dispose également de plus d'options qui vous aideront à rechercher des informations spécifiques. Il supporte les expressions régulières, la limitation du débit des requêtes et l'enregistrement de vos résultats dans un fichier.

J'espère que vous avez apprécié cet article. Vous pouvez [me contacter sur LinkedIn](https://www.linkedin.com/in/manishmshiva/) ou [lire plus d'articles sur mon blog](https://blog.manishmshiva.com/). Je vous retrouverai bientôt avec un autre article.