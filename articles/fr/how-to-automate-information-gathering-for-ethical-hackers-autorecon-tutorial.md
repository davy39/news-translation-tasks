---
title: Comment automatiser la collecte d'informations pour les hackers éthiques —
  Tutoriel AutoRecon
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-04-24T15:09:02.904Z'
originalURL: https://freecodecamp.org/news/how-to-automate-information-gathering-for-ethical-hackers-autorecon-tutorial
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745507318904/b27dc949-dbbb-43c2-85e1-072f91f3971f.png
tags:
- name: ethicalhacking
  slug: ethicalhacking
- name: programming
  slug: programming-ciovqvfcb008mb253jrczo9ye
- name: hacking
  slug: hacking
- name: information gathering
  slug: information-gathering
- name: nmap
  slug: nmap
seo_title: Comment automatiser la collecte d'informations pour les hackers éthiques
  — Tutoriel AutoRecon
seo_desc: 'When you’re doing a penetration test, your first job is to understand the
  target.

  Before you touch a single exploit or send a single payload, you need to know what
  services are running, what ports are open, what technologies are in play, and where
  th...'
---

Lorsque vous effectuez un test de pénétration, votre première tâche est de comprendre la cible.

Avant de toucher à un seul exploit ou d'envoyer une seule charge utile, vous devez savoir quels services sont en cours d'exécution, quels ports sont ouverts, quelles technologies sont en jeu et où se trouvent les points faibles.

Cette phase est appelée **reconnaissance**. Elle peut prendre des heures, parfois même des jours, si vous la faites manuellement.

C'est là qu'intervient [**Autorecon**](https://github.com/Tib3rius/AutoRecon).

## **Qu'est-ce qu'AutoRecon ?**

Autorecon est un outil qui automatise la plupart des travaux initiaux de reconnaissance. Ce n'est pas une boîte magique, mais c'en est proche.

Autorecon prend une liste d'IP ou de noms de domaine et exécute une série de scans prédéfinis. Ensuite, il organise la sortie de manière claire afin que vous ne perdiez pas de temps à analyser des fichiers Nmap bruts ou à relancer des commandes oubliées.

Si vous débutez dans le pentesting, que ce soit sur votre première boîte TryHackMe ou votre dixième laboratoire de pratique OSCP, Autorecon peut vous faire gagner beaucoup de temps. Voyons comment cela fonctionne.

## **Que fait exactement Autorecon ?**

À sa base, Autorecon fait trois choses :

1. **Exécute des scans Nmap** sur chaque IP ou nom d'hôte cible.

2. **Identifie les services** en cours d'exécution sur les ports ouverts.

3. **Exécute des outils d'énumération spécifiques** en fonction de ces services.

Disons que vous l'exécutez contre une IP qui a les ports 22 (SSH), 80 (HTTP) et 139/445 (SMB) ouverts. Autorecon va :

* Utiliser Nmap pour vérifier les versions et les scripts pour chaque port.

* Exécuter `nikto` ou `gobuster` sur le port 80.

* Exécuter `enum4linux` ou `smbmap` sur SMB.

* Stocker tout dans des dossiers organisés pour une revue ultérieure.

C'est ce que vous feriez manuellement, mais plus rapidement, plus proprement et sans oublier d'étapes.

## **Comment utiliser Autorecon**

Passons en revue un exemple rapide. Supposons que vous avez une cible à `10.129.8.143`.

Voici la commande de base :

```plaintext
autorecon 10.129.8.143
```

C'est tout. Pas de flags, pas de configuration supplémentaire. Autorecon s'occupe du reste. Pour comprendre ce qui se passe en arrière-plan, ajoutons le flag de verbosité `-v`.

Voici un exemple de résultat.

![Résultat du scan Autorecon](https://cdn.hashnode.com/res/hashnode/image/upload/v1745145447038/9132b17d-417e-464b-894e-fb68256e88f8.webp align="center")

En arrière-plan, il crée une structure de dossiers comme ceci :

```plaintext
results/
├── 10.129.8.143/
│   ├── scans/
│   │   ├── nmap/
│   │   └── gobuster/
│   ├── reports/
│   └── notes.txt
```

Vous trouverez les sorties complètes de Nmap, les résultats des outils spécifiques aux services, et même un endroit pour noter vos propres observations. Tout est prêt à l'emploi.

Si vous souhaitez scanner plusieurs cibles, passez simplement une liste :

```plaintext
autorecon targets.txt
```

Une fois qu'Autorecon a terminé un scan, allez dans le dossier `results/<IP>/scans/`. Commencez par les sorties Nmap.

Recherchez les ports ouverts et les services :

* **Port 80 ouvert ?** Vérifiez les sorties `gobuster` et `nikto` dans le dossier HTTP.

* **Ports SMB ouverts ?** Regardez dans les résultats `enum4linux` et `smbmap` pour trouver des lecteurs partagés ou des informations utilisateur.

* **Connexion FTP anonyme autorisée ?** Utilisez cet accès pour explorer les répertoires.

Ces découvertes vous donneront les prochaines étapes, comme naviguer sur un service web, créer une charge utile ou vérifier les exploits connus.

## **Pourquoi c'est important pour les débutants**

Si vous débutez dans le pentesting, l'une des parties les plus difficiles est de se souvenir de *tout* ce que vous êtes censé vérifier. Vous ouvrez un port, et vous pensez :

* "Attendez... Dois-je exécuter `enum4linux` sur ceci ?"

* "Quel était ce flag pour le scan Nmap agressif déjà ?"

* "Ai-je déjà vérifié ce service web avec `nikto` ?"

Autorecon vous enlève ce fardeau mental. Vous pouvez vous concentrer sur l'analyse, pas sur la surveillance des scans.

Et voici un autre avantage : cela vous aide à **apprendre le processus**.

Bien qu'Autorecon automatise la reconnaissance, il *vous montre chaque outil et commande* qu'il exécute. Vous pouvez ouvrir la sortie brute, lire les flags et comprendre *pourquoi* il a exécuté ces scans.

Exemple : Vous verrez qu'il exécute `nmap -sV -sC` pour la détection de version et les scripts. Cela aide les débutants à comprendre quels scans correspondent à quels services et pourquoi ils sont importants.

Au fur et à mesure qu'il s'exécute, vous verrez tous les outils et commandes qu'il utilise. Vous pouvez regarder les résultats bruts, voir ce qui a fonctionné et construire progressivement votre propre flux de travail.

## **Ce qu'il scanne (par défaut)**

Voici un aperçu rapide de ce qu'Autorecon exécute en fonction du port et du service :

**Nmap** :

* Scan rapide

* Scan complet des ports TCP

* Détection de service/version

* Scripts NSE

**HTTP/HTTPS** :

* `gobuster` (bruteforce de répertoires)

* `nikto` (scanner de vulnérabilités)

* `whatweb` (détection de technologies)

**SMB** :

* `enum4linux-ng`

* `smbmap`

* Scripts Nmap SMB

**FTP** :

* Vérification de la connexion anonyme

* Scripts Nmap FTP

**SSH** :

* Capture de bannière

* Vérification de la version SSH

Et ce n'est qu'un aperçu. Il gère également d'autres services, comme MySQL, SNMP, SMTP et même RPC.

## **Quand Autorecon est le plus utile**

Autorecon brille dans certaines situations :

* **Laboratoires de formation** : Vous obtenez une vue claire de votre cible avec une configuration minimale.

* **Préparation OSCP** : Il exécute les outils de reconnaissance exacts dont vous aurez besoin pour l'examen OSCP.

* **Tests de pénétration limités dans le temps** : Lorsque vous devez toucher plusieurs cibles rapidement, Autorecon maintient votre sortie cohérente et vous évite de tout retaper.

Mais ce n'est pas seulement une question de vitesse. C'est une question d'être minutieux. Avec un scan manuel, il est facile de manquer quelque chose de petit. Autorecon n'oublie pas.

## **Ce qu'Autorecon ne fait pas**

Autorecon n'est pas un outil d'exploitation. Il ne pirate rien pour vous. Il ne devine pas les identifiants ou ne contourne pas les pages de connexion.

Il est uniquement axé sur la reconnaissance. Cela signifie que vous devez toujours :

* Examiner les résultats des scans

* Analyser manuellement les services web (par exemple, naviguer sur le site, tester les entrées)

* Décider quels exploits ou charges utiles exécuter

De plus, il peut être bruyant. Si vous êtes dans un engagement réel où la discrétion compte, certains scans peuvent déclencher des alarmes. Dans ce cas, vous voudrez exécuter des commandes plus contrôlées manuellement.

## **Conseils pour utiliser Autorecon efficacement**

**Utilisez des flags pour contrôler les scans :**  
Pour augmenter la verbosité et ignorer les hôtes précédemment scannés :

```plaintext
autorecon -v --only-scans-dir 10.129.8.143
```

**Personnalisez les wordlists pour de meilleurs résultats :**  
Par défaut, Autorecon utilise des wordlists petites. Vous pouvez améliorer cela :

```plaintext
autorecon --dirbuster.wordlist /usr/share/seclists/Discovery/Web-Content/raft-medium-words.txt 10.129.8.143
```

Cela rend le bruteforce de répertoires plus efficace, surtout sur les cibles web.

**Ne sautez pas la sortie** : Lisez les fichiers Nmap, vérifiez les rapports HTML. Les outils ne pensent pas comme les humains. Vous devez toujours faire les liens.

## **Réflexions finales**

Autorecon ne remplace pas vos compétences, mais il aide à les renforcer. Au lieu de passer 30 minutes à taper des commandes de scan, vous pouvez exécuter une commande et commencer l'analyse en quelques minutes. Cela aide les débutants à rester concentrés et les professionnels à gagner du temps.

Donc, si vous en avez assez de relancer les mêmes scans Nmap encore et encore, ou si vous voulez simplement des résultats plus clairs et moins d'erreurs, laissez Autorecon faire le gros du travail, afin que vous puissiez vous concentrer sur la partie qui compte vraiment : casser des choses.

*Pour plus de tutoriels sur la cybersécurité,* [***rejoignez notre newsletter***](https://newsletter.stealthsecurity.sh/)*. Pour apprendre les bases de la cybersécurité offensive, consultez notre* [***Cours de démarrage en sécurité***](https://start.stealthsecurity.sh/)*.*