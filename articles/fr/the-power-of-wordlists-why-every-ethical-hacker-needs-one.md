---
title: 'La puissance des listes de mots : pourquoi chaque hacker éthique en a besoin'
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2024-10-02T18:34:35.216Z'
originalURL: https://freecodecamp.org/news/the-power-of-wordlists-why-every-ethical-hacker-needs-one
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1727791638563/645b35c6-cf51-43dd-966c-09e0a5274c84.png
tags:
- name: Security
  slug: security
- name: '#cybersecurity'
  slug: cybersecurity-1
- name: ethicalhacking
  slug: ethicalhacking
- name: pentesting
  slug: pentesting
seo_title: 'La puissance des listes de mots : pourquoi chaque hacker éthique en a
  besoin'
seo_desc: 'Wordlists are a core component of brute-force attacks. Let''s learn what
  they are and how to use them.

  Imagine that you’re a security professional who’s performing a penetration test
  on a client’s website. Your job is to find potential weak points in ...'
---

Les listes de mots sont un composant central des attaques par force brute. Apprenons ce qu'elles sont et comment les utiliser.

Imaginez que vous êtes un professionnel de la sécurité effectuant un test de pénétration sur le site web d'un client. Votre travail consiste à trouver des points faibles potentiels dans leur sécurité. Après avoir exécuté quelques analyses de base, vous remarquez que le formulaire de connexion semble vulnérable.

Il manque une limitation de taux et des protections de mot de passe solides. Vous pourriez donc être en mesure d'essayer plusieurs mots de passe sans être bloqué. C'est là qu'une liste de mots entre en jeu.

Au lieu de deviner des mots de passe aléatoires un par un, vous pouvez utiliser une liste de mots pré-établie. La liste contiendra des milliers, voire des millions de mots de passe potentiels.

Vous pouvez combiner cette liste de mots avec un outil de force brute comme [Hydra](https://www.stealthsecurity.sh/p/hacking-hydra-practical-tutorial) pour effectuer une attaque. L'outil parcourt la liste de mots, testant chaque mot de passe contre le formulaire de connexion. Après un certain temps, vous trouvez une correspondance. Vous venez de craquer la connexion.

En tant que hacker éthique, vous informeriez le client de la politique de mot de passe faible. Vous pourriez ensuite suggérer des mesures de sécurité plus strictes pour éviter ce scénario. Mais cela montre à quel point les listes de mots peuvent être cruciales lorsqu'il s'agit d'exploiter des systèmes de connexion faibles.

Dans cet article, nous examinerons les listes de mots en détail. Nous couvrirons ce qu'elles sont et quelques cas d'utilisation, ainsi que quelques listes de mots populaires.

## Qu'est-ce que les listes de mots ?

Les listes de mots sont exactement ce à quoi elles ressemblent : des listes de mots. En cybersécurité, ces mots représentent des mots de passe, des noms d'utilisateur ou même des URL.

Les listes de mots peuvent être des collections simples de mots de passe courants comme "123456" ou "password". Ou elles peuvent être des listes personnalisées générées pour cibler des systèmes spécifiques.

Les testeurs de pénétration alimentent ces listes de mots dans des outils qui leur permettent de tester plusieurs entrées rapidement. Ces outils incluent des logiciels de craquage de mots de passe, des scripts de force brute ou des scanners de répertoires. La liste de mots sert de source d'entrée, essayant chaque mot contre la cible dans une tentative de trouver une correspondance.

## Comment les listes de mots sont-elles utilisées ?

Examinons quelques scénarios courants où les listes de mots peuvent être utiles.

### Craquage de mots de passe

L'une des utilisations les plus courantes des listes de mots est le craquage de mots de passe. Les attaquants alimentent une liste de mots dans des outils comme John the Ripper ou Hashcat. Ces outils testent ensuite chaque mot contre un hachage de mot de passe pour trouver une correspondance.

Supposons qu'un hacker trouve des mots de passe hachés à partir d'une base de données compromise. Ils peuvent utiliser une liste de mots pour tenter de inverser ces hachages en mots de passe d'origine.

Les pratiques de sécurité modernes encouragent les mots de passe complexes. Mais beaucoup de gens utilisent encore des mots de passe faibles et courants. Les listes de mots exploitent cette tendance humaine en incluant des mots de passe fréquemment utilisés.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1727791741753/79b4837b-f1e8-4af1-994f-ecd2e89075b6.png align="center")

L'une des listes de mots de passe les plus célèbres dans la communauté du hacking est Rockyou.txt. Elle contient 14 millions de mots de passe collectés après que le site [Rockyou.com](http://Rockyou.com) ait été piraté. [Voici la liste complète des mots](https://github.com/praetorian-inc/Hob0Rules/blob/master/wordlists/rockyou.txt.gz).

### Énumération des noms d'utilisateur

Dans certains systèmes, connaître le bon nom d'utilisateur est la moitié de la bataille. Les hackers utilisent souvent des listes de mots pour énumérer les noms d'utilisateur avant de tenter une attaque par mot de passe. Cela fonctionne en soumettant différents noms d'utilisateur à un formulaire de connexion et en observant la réponse du système.

Par exemple, certains systèmes retourneront un message d'erreur comme "Nom d'utilisateur non trouvé". Une liste de mots bien conçue de noms d'utilisateur vous permet de découvrir rapidement quels comptes existent.

Une liste de mots de noms d'utilisateur peut aider dans ce type de scénario. Elle n'a pas besoin d'être longue comme une liste de mots de passe. Mais une liste de noms d'utilisateur courants serait utile. [Voici une telle liste de mots](https://github.com/danielmiessler/SecLists/blob/master/Usernames/top-usernames-shortlist.txt).

### Énumération des répertoires et fichiers

Lors du test d'une application web, il est important de trouver des fichiers et répertoires cachés. Ils peuvent ne pas être listés publiquement. Et ces URL cachées peuvent révéler des informations sensibles ou des fonctionnalités cachées.

Des outils comme **Gobuster** ou **Dirbuster** utilisent des listes de mots pour automatiser ce processus. Ils essaient chaque mot dans la liste de mots comme un nom de répertoire ou de fichier potentiel.

Par exemple, tester une liste de mots sur un site web pourrait trouver un panneau d'administration caché à `/admin`, ou un fichier de sauvegarde à `/backup.zip`. Cela peut être utile pour trouver des expositions non intentionnelles.

[Voici un exemple de liste de mots de répertoire](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/directory-list-1.0.txt).

### Énumération des sous-domaines

L'énumération des sous-domaines consiste à trouver tous les sous-domaines associés à un site web cible. Comme les pages cachées, les sous-domaines peuvent également contenir des informations utiles et sensibles.

Par exemple, un produit sur [product.com](http://product.com) peut contenir un serveur de développement sur [dev.product.com](http://dev.product.com). Ou un panneau d'administration sur [admin.product.com](http://admin.product.com). Ces sous-domaines peuvent ne pas être aussi bien protégés que le site principal.

Des outils comme **Sublist3r** et **Amass** sont populaires pour cette tâche. [Voici une liste de mots de sous-domaines](https://github.com/danielmiessler/SecLists/blob/master/Discovery/DNS/subdomains-top1million-5000.txt) pour ces types d'attaques.

## Comment créer des listes de mots personnalisées

Parfois, les listes de mots générales ne suffisent pas. Pour des engagements spécifiques, il vaut la peine de créer votre propre liste de mots adaptée à la cible.

Par exemple, si vous effectuez un test de pénétration pour une entreprise, vous pourriez créer une liste de mots personnalisée pour cette entreprise. Elle peut contenir des noms d'employés, des noms de départements ou des termes pertinents uniques à cette entreprise.

Plusieurs outils vous aident à créer des listes de mots personnalisées.

* **CeWL (générateur de liste de mots personnalisée)**

génère des listes de mots en extrayant du texte d'un site web spécifique à la cible.
    
* **Crunch**

crée des listes de mots en mélangeant et en associant les caractères que vous fournissez.
    

## Conclusion

Les listes de mots sont des outils puissants que tout professionnel de la cybersécurité devrait avoir dans son arsenal. Elles simplifient des tâches complexes comme le craquage de mots de passe, la force brute et l'énumération de répertoires. La bonne liste de mots peut vous faire gagner des heures et aider à trouver des vulnérabilités rapidement et efficacement.

**Espérons que ce tutoriel vous a aidé à comprendre comment utiliser les listes de mots. Pour plus d'articles sur la cybersécurité, rejoignez notre newsletter gratuite** [**Stealth Security**](https://www.stealthsecurity.sh/)**. Pour apprendre le hacking en utilisant des laboratoires pratiques, consultez notre communauté privée** [**The Hacker's Hub**](https://www.skool.com/hackershub)**.**