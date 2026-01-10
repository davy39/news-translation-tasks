---
title: Metasploit pour les débutants — Un guide sur le puissant framework d'exploitation
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-01-22T00:12:40.389Z'
originalURL: https://freecodecamp.org/news/learn-metasploit-for-beginners
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1737504731562/ebce2299-d90e-4b17-a1b0-15b4dbe6d844.png
tags:
- name: metasploit
  slug: metasploit
- name: cybersecurity
  slug: cybersecurity
- name: Msfconsole
  slug: msfconsole
- name: payloads
  slug: payloads
- name: Exploitation
  slug: exploitation
- name: exploit
  slug: exploit
- name: pentesting
  slug: pentesting
seo_title: Metasploit pour les débutants — Un guide sur le puissant framework d'exploitation
seo_desc: 'If you’re starting your journey into penetration testing, you’ve likely
  heard of Metasploit.

  Metasploit is one of the most versatile tools in cybersecurity. It helps simplify
  vulnerability testing and exploitation.

  Metasploit helps us find and fix we...'
---

Si vous commencez votre voyage dans les tests d'intrusion, vous avez probablement entendu parler de [Metasploit](https://www.metasploit.com/).

Metasploit est l'un des outils les plus polyvalents en cybersécurité. Il aide à simplifier les tests de vulnérabilité et l'exploitation.

Metasploit nous aide à trouver et à corriger les faiblesses avant que des acteurs malveillants ne les exploitent. Dans ce tutoriel, vous apprendrez ce qu'est Metasploit, pourquoi il est utile et comment l'utiliser.

## **Qu'est-ce que Metasploit ?**

Metasploit est un framework open-source pour les tests d'intrusion.

Vous pouvez l'utiliser pour trouver des vulnérabilités, les exploiter et obtenir un accès à la cible.

Metasploit fournit une collection d'exploits, de charges utiles et d'outils d'aide. Il est souvent appelé le "couteau suisse" pour les testeurs d'intrusion.

Au lieu d'écrire vos propres scripts pour exploiter les vulnérabilités, Metasploit vous donne des modules pré-construits pour automatiser une grande partie de votre travail.

Un module est un morceau de code qui effectue une action. Ces actions peuvent inclure le balayage, l'exploitation ou tout ce qui aide à simplifier un test d'intrusion.

## **Pourquoi Metasploit est-il utile pour les testeurs d'intrusion ?**

Les testeurs d'intrusion tentent d'attaquer des réseaux, des applications et des systèmes pour vérifier leur sécurité. Metasploit aide à rendre ce travail plus facile de plusieurs manières.

Tout d'abord, il simplifie l'exploitation. Metasploit dispose d'une grande bibliothèque d'exploits qui nous permet d'attaquer rapidement les faiblesses connues dans les logiciels et les systèmes.

Ensuite, il aide à la reconnaissance et au balayage. Les outils de balayage de Metasploit recueillent des informations sur une cible, telles que les ports ouverts, les services en cours d'exécution et les vulnérabilités probables.

Après avoir pénétré, Metasploit fournit des fonctionnalités post-exploitation. Des outils comme Meterpreter permettent aux testeurs d'intrusion de maintenir l'accès, de collecter des données et de tester davantage les défenses.

Metasploit est également très flexible. Nous pouvons construire ou modifier des modules pour répondre à nos besoins spécifiques.

En bref, Metasploit nous permet de réaliser des tests de sécurité complets, de la recherche de vulnérabilités à leur exploitation.

## **Que sont les modules auxiliaires de Metasploit ?**

Les modules auxiliaires sont des outils d'aide dans Metasploit qui effectuent des tâches autres que l'exploitation.

Ils sont utilisés pour la reconnaissance, le balayage, le forçage brutal et plus encore. Ces modules flexibles peuvent vous aider à recueillir des informations précieuses sur une cible.

Par exemple, un module auxiliaire peut balayer un réseau à la recherche de ports ouverts, vérifier les services vulnérables ou tenter une connexion par force brute sur une application.

Voici une liste d'exemples de modules auxiliaires de Metasploit :

![Modules auxiliaires de Metasploit](https://cdn.hashnode.com/res/hashnode/image/upload/v1737559559020/41a5d517-4f98-4c5c-bd7f-0e9e3dfb4977.png align="center")

Vous pouvez voir que Metasploit dispose d'une gamme de modules auxiliaires, des scanners aux modules de force brute, qui aident à révéler et à exploiter les failles de sécurité.

## **Que sont les exploits de Metasploit ?**

Les exploits sont des scripts ou des programmes qui tirent parti des vulnérabilités dans les systèmes.

Ils aident un attaquant à obtenir un accès ou à effectuer des activités malveillantes. La bibliothèque de Metasploit comprend des centaines d'exploits, couvrant une large gamme de plateformes et de services.

Par exemple, si un système cible exécute une version obsolète de Samba, Metasploit peut avoir un exploit spécialement conçu pour exploiter cette vulnérabilité.

## **Que sont les charges utiles de Metasploit ?**

Les charges utiles sont des scripts qui s'exécutent sur le système cible après qu'un exploit a été exécuté avec succès.

Ils déterminent ce qui se passe ensuite — que vous ouvriez un shell inverse, ajoutiez une porte dérobée ou effectuiez une autre tâche post-exploitation.

Il existe deux principaux types de charges utiles :

1. **Charges utiles uniques** : Elles effectuent une seule tâche, comme la création d'un compte utilisateur sur la cible.

2. **Charges utiles étagées** : Elles téléchargent une charge utile plus grande par étapes, permettant des actions plus complexes.

L'une des charges utiles les plus couramment utilisées est `windows/meterpreter/reverse_tcp`, qui vous donne un shell de commande sur le système cible.

Les testeurs d'intrusion et les experts en sécurité utilisent des exploits pour découvrir les points faibles des réseaux et des systèmes. En testant ces failles de manière contrôlée, ils peuvent trouver des défauts avant que les attaquants ne le fassent. Une fois trouvées, ces failles sont corrigées ou patchées pour prévenir les dommages. Cette approche aide à protéger les données et maintient les systèmes plus sécurisés.

## **Qu'est-ce que Metasploit Meterpreter ?**

Meterpreter est une charge utile avancée et interactive dans Metasploit. Il vous permet d'interagir avec le système cible après l'avoir exploité.

Meterpreter est chargé directement dans la mémoire de la cible, ce qui le rend plus furtif que les charges utiles traditionnelles.

En utilisant Meterpreter, vous pouvez recueillir des détails sur le système d'exploitation, transférer des fichiers entre l'attaquant et la cible, et même exécuter des commandes directement sur la machine cible.

Vous pouvez également configurer une porte dérobée persistante pour maintenir l'accès même après un redémarrage du système.

Meterpreter est un outil puissant pour les activités post-exploitation, vous donnant un contrôle complet sur le système compromis.

## **Comment travailler avec** `msfconsole`

Obtenons une expérience pratique avec Metasploit.

`msfconsole` est l'interface en ligne de commande (CLI) pour Metasploit. C'est le moyen principal d'interagir avec le framework.

Metasploit est préinstallé dans Kali Linux. Si vous utilisez Kali Linux, vous pouvez trouver les [instructions d'installation ici](https://docs.rapid7.com/metasploit/installing-the-metasploit-framework/).

Après avoir installé Metasploit, lancez la console en tapant :

```plaintext
msfconsole
```

Une fois chargé, vous verrez une invite comme celle-ci

![msfconsole](https://cdn.hashnode.com/res/hashnode/image/upload/v1736776944033/519269c1-9124-4467-9257-4cbe693be0df.png align="center")

C'est ici que vous taperez des commandes pour interagir avec Metasploit. Essayons quelques commandes de base pour vous aider à démarrer.

### Commandes Metasploit

1. `help` : Si vous n'êtes pas sûr de ce qu'il faut faire, commencez par taper `help`. Cela affiche une liste des commandes disponibles ainsi que de brèves descriptions. Par exemple :

![commande d'aide de Metasploit](https://cdn.hashnode.com/res/hashnode/image/upload/v1736776984407/182a0f3c-0fb2-4880-85cf-cbd0baff6538.png align="center")

2. `search` : La commande de recherche nous aide à trouver des modules spécifiques, tels que des exploits ou des auxiliaires (modules d'aide). Par exemple, si vous cherchez des modules liés au balayage, vous taperiez :

```plaintext
msf6 > search scanner
```

![Recherche Metasploit](https://cdn.hashnode.com/res/hashnode/image/upload/v1736777096451/63c0087f-80dd-42a1-98c7-9459f53b7f5a.png align="center")

Metasploit affichera tous les modules qui correspondent au mot-clé scanner.

3. `info` : Vous pouvez utiliser la commande `info` pour en savoir plus sur un module, y compris ses options et son fonctionnement. Par exemple :

```plaintext
msf6 > info auxiliary/scanner/portscan/tcp
```

![Sortie de la commande info de Metasploit](https://cdn.hashnode.com/res/hashnode/image/upload/v1736777131375/c89a1e64-f96e-4fff-9f36-4dd5c1e7f20d.png align="center")

4. `use` : Pour utiliser un exploit ou un auxiliaire, nous pouvons simplement taper `use` avec le nom du module. Utilisons le module de balayage `auxiliary/scanner/portscan/tcp` qui balayera les ports TCP ouverts sur un serveur.

```plaintext
msf6> use auxiliary/scanner/portscan/tcp
```

5. `options` : Une fois que vous avez chargé un module avec la commande `use`, vous pouvez voir la liste des options en utilisant la commande `options`. Elle vous donnera la liste des options que vous pouvez définir pour ce module.

![Commande options de Metasploit](https://cdn.hashnode.com/res/hashnode/image/upload/v1736777161123/5e2b44bb-08ee-4489-a1c0-8d78070710b5.png align="center")

Par exemple, le paramètre RHOSTS est utilisé pour définir l'adresse IP de la cible pour le balayage. [`scanme.nmap.org`](http://scanme.nmap.org) nous permet d'exécuter des balayages de ports sur ce serveur, alors utilisons-le pour exécuter un balayage.

Obtenons l'adresse IP du serveur. Nous allons émettre une simple commande ping pour obtenir l'adresse IP du serveur.

![Commande ping](https://cdn.hashnode.com/res/hashnode/image/upload/v1736777193985/3c71c4b8-ab74-46bc-a613-3115b97eef6f.png align="center")

Nous pouvons voir que l'adresse IP du serveur est 45.33.32.156 (elle peut changer lorsque vous exécutez la commande ping). Maintenant, utilisons cette IP comme entrée pour le paramètre RHOSTS. Nous allons utiliser la commande `set` pour définir l'adresse IP.

```plaintext
msf6 auxiliary(scanner/portscan/tcp)> set RHOSTS 45.33.32.156
```

6. `run` : Pour exécuter un module, nous utilisons la commande `run`. Maintenant que nous avons défini l'adresse IP de la cible, exécutons le module pour voir si des ports sont ouverts.

![Balayage de ports Metasploit](https://cdn.hashnode.com/res/hashnode/image/upload/v1736777226150/9bab8d7b-9efb-4573-bcc9-1c355a468bf4.png align="center")

Comme vous pouvez le voir, nous avons trouvé 3 ports — 22, 80 et 9929. Des outils comme Nmap sont meilleurs pour le balayage de ports en profondeur, mais Metasploit offre des modules pour presque tous les segments d'un audit de cybersécurité.

7. `exit` : Lorsque vous avez terminé d'utiliser Metasploit, tapez simplement `exit` pour quitter la console.

La `msfconsole` est conviviale une fois que vous avez compris ces commandes de base. Prenez votre temps pour explorer et expérimenter avec l'aide de la commande `help`.

## **Conclusion**

Metasploit est l'un des outils les plus puissants dans la boîte à outils d'un testeur d'intrusion.

À mesure que vous vous familiarisez avec Metasploit, vous débloquerez tout son potentiel et obtiendrez des informations plus approfondies sur la manière dont les attaquants exploitent les systèmes — et comment vous pouvez vous défendre contre eux. Continuez à apprendre, restez curieux et utilisez toujours Metasploit de manière responsable !

Rejoignez notre [**Newsletter Hebdomadaire**](https://www.stealthsecurity.sh/) pour plus de tutoriels sur le Hacking Éthique. Pour des tutoriels vidéo sur la cybersécurité, consultez notre [**Chaîne YouTube**](https://www.youtube.com/@stealthsecurity_sh).