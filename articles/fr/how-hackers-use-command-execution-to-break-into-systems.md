---
title: Comment les pirates utilisent l'exécution de commandes pour s'introduire dans
  les systèmes
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2024-11-27T14:27:23.149Z'
originalURL: https://freecodecamp.org/news/how-hackers-use-command-execution-to-break-into-systems
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1732527958866/65644a19-376f-480b-a46e-d5f204ce9515.jpeg
tags:
- name: '#cybersecurity'
  slug: cybersecurity-1
- name: Commands
  slug: commands
- name: cyber attack
  slug: cyber-attack
- name: ethicalhacking
  slug: ethicalhacking
seo_title: Comment les pirates utilisent l'exécution de commandes pour s'introduire
  dans les systèmes
seo_desc: "When learning about cybersecurity, you’ll quickly realize that some vulnerabilities\
  \ are more dangerous than others. One of the most serious ones is called command\
  \ execution. \nHackers use it to run harmful commands on a system, gain access to\
  \ sensitiv..."
---

Lorsque vous apprenez la cybersécurité, vous réaliserez rapidement que certaines vulnérabilités sont plus dangereuses que d'autres. L'une des plus graves s'appelle **l'exécution de commandes**.

Les pirates l'utilisent pour exécuter des commandes malveillantes sur un système, accéder à des données sensibles, prendre le contrôle de serveurs, voire fermer des réseaux entiers.

Mais comment cela fonctionne-t-il vraiment ? Et pourquoi est-ce un si gros problème ? Décomposons cela en termes simples.

## Qu'est-ce que l'exécution de commandes ?

Imaginez un programme informatique qui vous permet de saisir quelque chose — comme une adresse de site web ou un nom de fichier — et qui effectue ensuite une action basée sur cette entrée.

Par exemple, un outil web pourrait vous permettre de taper un nom de domaine et d'exécuter une commande "ping" pour vérifier si le site est en ligne. Cela semble utile, n'est-ce pas ?

Voici où le problème commence : si le programme ne contrôle pas ou ne nettoie pas correctement ce que vous entrez, un pirate pourrait taper quelque chose d'inattendu — comme une commande qui supprime tous les fichiers du système.

Au lieu de faire uniquement ce pour quoi le programme a été conçu, la commande du pirate est exécutée comme si elle était légitime.

Examinons un exemple de mauvais code :

```plaintext
import os

def ping_host(domain):
    os.system(f"ping {domain}")
```

Voici ce qui se passe :

* Vous entrez un domaine comme "[example.com](http://example.com)".
  
* Le programme exécute la commande `ping` sur le système, qui envoie des messages de test à "[example.com](http://example.com)" pour vérifier s'il est accessible.
  

Le problème est que le programme ne limite pas ce que vous pouvez entrer. Si quelqu'un de malveillant entre quelque chose comme [`example.com`](http://example.com) `&& rm -rf /`, il pourrait exécuter à la fois la commande ping et la commande `rm -rf /`, qui efface tous les fichiers de l'ordinateur.

Ci-dessous se trouve un exemple d'injection de la commande `hostname` qui affiche les informations du système.

![exemple d'injection de commande](https://cdn.hashnode.com/res/hashnode/image/upload/v1732528002391/f9316a04-a1be-4f28-8db0-73ebc757dd79.png align="center")

C'est en résumé l'exécution de commandes — lorsque l'entrée de l'utilisateur est mal utilisée pour exécuter des commandes système non prévues.

## Types d'attaques par exécution de commandes

Il existe deux principales façons pour les pirates d'utiliser l'exécution de commandes pour attaquer les systèmes : **l'injection de commandes** et **l'exécution de code à distance (RCE)**.

### Injection de commandes

Il s'agit du type d'attaque le plus facile. Les pirates "injectent" des commandes supplémentaires dans un programme en ajoutant du texte inattendu à un champ qui accepte l'entrée de l'utilisateur. L'exemple ci-dessus, où un pirate ajoute `&& rm -rf /` au nom de domaine, est un exemple classique d'injection de commandes.

Les pirates utilisent cette technique pour lire des fichiers sensibles, supprimer des données importantes ou voler des informations du système.

### Exécution de code à distance (RCE)

Il s'agit de la version la plus grave. Avec la RCE, un pirate n'exécute pas seulement des commandes — il peut télécharger et exécuter des scripts ou des programmes entiers sur le système.

C'est comme donner à un pirate les clés de votre ordinateur, lui permettant de faire tout ce qu'il veut.

Par exemple, imaginez qu'un attaquant télécharge un petit programme qui écoute secrètement ses commandes. Il pourrait alors utiliser ce programme pour installer un ransomware, espionner les utilisateurs ou prendre le contrôle total du système.

## Exemples réels d'attaques par exécution de commandes

Examinons quelques cas réels où les vulnérabilités d'exécution de commandes ont causé des dommages majeurs.

### Le bug Shellshock (2014)

Le [bug Shellshock](https://en.wikipedia.org/wiki/Shellshock_%28software_bug%29) était une vulnérabilité massive trouvée dans le shell Bash (un programme utilisé dans de nombreux systèmes basés sur Unix). Les pirates pouvaient injecter des commandes dans les variables d'environnement, trompant le système pour qu'il les exécute.

Shellshock a permis aux attaquants de prendre le contrôle de serveurs, de voler des données et de lancer des attaques à grande échelle. Cette vulnérabilité était si grave qu'elle a affecté des millions de systèmes dans le monde et a nécessité des correctifs immédiats.

### Faille de sécurité Cisco (2020)

En 2020, une vulnérabilité a été trouvée dans les [pare-feux de Cisco](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-asaftd-xss-multiple-FCB3vPZe.html). Cette faille permettait aux pirates d'exécuter des commandes sur les appareils à distance, prenant ainsi le contrôle total.

Puisque ces pare-feux sont utilisés pour protéger des réseaux sensibles, la vulnérabilité posait un risque majeur pour les entreprises et les organisations.

## Comment se protéger contre les attaques par exécution de commandes

Se protéger contre les vulnérabilités d'exécution de commandes consiste à suivre les bonnes pratiques.

1. **Toujours nettoyer les entrées utilisateur** — Considérez chaque entrée utilisateur comme une menace potentielle. Par exemple, si un formulaire demande un nom, un pirate pourrait entrer quelque chose comme `rm -rf /`. Pour empêcher cela, vous pouvez utiliser des fonctions qui suppriment les caractères dangereux.
  
2. **Éviter d'exécuter des commandes système** — Exécuter des commandes directement depuis votre application peut être risqué. Au lieu d'utiliser quelque chose comme `os.system('ls')` en Python, utilisez [`subprocess.run`](http://subprocess.run)`()` avec `shell=False`. Ainsi, même si quelqu'un essaie d'injecter des commandes nuisibles, elles ne s'exécuteront pas car le shell n'est pas impliqué.
  
3. **Limiter ce que les programmes peuvent faire** — Assurez-vous que vos programmes n'ont que les permissions dont ils ont vraiment besoin. Par exemple, si une application n'a pas besoin de modifier des fichiers système, ne lui donnez pas d'accès en écriture.
  
4. **Tout garder à jour** — Les pirates adorent les anciens logiciels car c'est comme une serrure cassée. En mettant à jour régulièrement votre système d'exploitation et vos bibliothèques, vous corrigez les vulnérabilités connues. Par exemple, le célèbre bug Shellshock dans Bash a affecté les systèmes obsolètes mais a été corrigé dans les versions ultérieures.
  
5. **Tester les vulnérabilités** — Avant que quelqu'un d'autre ne trouve les failles de votre système, testez-le vous-même. Des outils comme **Burp Suite** ou **OWASP ZAP** sont utiles pour le balayage automatisé. Par exemple, vous pouvez simuler des attaques pour voir comment votre application web réagit et corriger les problèmes avant qu'ils ne soient exploités.
  
6. **Surveiller vos journaux** — Les journaux sont comme des caméras de sécurité pour votre serveur. Si vous voyez quelque chose d'étrange, comme beaucoup de tentatives de connexion échouées ou des commandes que vous n'avez pas autorisées, c'est un signal d'alarme. Configurez des alertes pour détecter ces signes précocement.
  

En suivant ces meilleures pratiques, vous rendrez vos systèmes beaucoup plus difficiles à pirater.

## Résumé

Les vulnérabilités d'exécution de commandes sont l'un des outils les plus puissants que les pirates peuvent utiliser. En les exploitant, les attaquants peuvent contrôler complètement un système, voler des informations sensibles ou causer des dommages massifs. Comprendre cette vulnérabilité est une étape clé pour apprendre à défendre les systèmes.

*Vous voulez une expérience réelle en cybersécurité ? Essayez notre boot camp de cinq jours* [*Hacker's Headstart*](https://start.stealthsecurity.sh/)*. Bon piratage !*