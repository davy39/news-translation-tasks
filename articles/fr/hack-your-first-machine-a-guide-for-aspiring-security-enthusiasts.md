---
title: Piratez votre première machine – Un guide pour les passionnés de sécurité en
  herbe
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2024-10-03T21:22:23.113Z'
originalURL: https://freecodecamp.org/news/hack-your-first-machine-a-guide-for-aspiring-security-enthusiasts
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1727929072898/8ba47c55-8ca9-4255-8cf7-f6a27e403315.jpeg
tags:
- name: '#cybersecurity'
  slug: cybersecurity-1
- name: Security
  slug: security
- name: hacking
  slug: hacking
- name: Linux
  slug: linux
seo_title: Piratez votre première machine – Un guide pour les passionnés de sécurité
  en herbe
seo_desc: Hacking your first machine is a milestone for anyone interested in cybersecurity.
  You may have watched countless tutorials and read many articles. But hacking a machine
  and taking control of it is a wonderful and important experience for any aspiring...
---

Pirater votre première machine est une étape importante pour toute personne intéressée par la cybersécurité. Vous avez peut-être regardé d'innombrables tutoriels et lu de nombreux articles. Mais pirater une machine et en prendre le contrôle est une expérience merveilleuse et importante pour tout professionnel aspirant en cybersécurité.

Eh bien, je suis ici pour vous offrir cette expérience – gratuitement.

J'ai créé un laboratoire pratique avec TryHackMe (THM). [**TryHackMe**](https://tryhackme.com/) est une plateforme en ligne qui propose des laboratoires virtuels pour apprendre la cybersécurité.

THM simplifie les configurations complexes de machines virtuelles pour vous aider à pratiquer vos compétences. En utilisant THM, vous pouvez utiliser des machines directement depuis votre navigateur.

C'est un espace sûr pour pratiquer vos compétences. Vous devrez vous inscrire pour un compte gratuit pour travailler avec ce laboratoire, mais vous n'avez pas à acheter un plan premium.

Tout d'abord, je vais vous donner une introduction à la plateforme. Vous pourrez ensuite visiter le laboratoire et pirater votre première machine. Voici l'URL du laboratoire : [https://tryhackme.com/jr/SS\_HYFM](https://tryhackme.com/jr/SS_HYFM)

## Comment travailler avec TryHackMe

Pour pratiquer le piratage, vous avez besoin d'une cible et d'une machine d'attaque. THM fonctionne en créant des laboratoires isolés, également appelés "rooms". Chaque room a sa propre machine cible et sa machine d'attaque.

Chaque room est divisée en plusieurs tâches. Vous devez terminer une tâche et répondre à quelques questions pour passer à la tâche suivante. Une fois que vous avez terminé toutes les tâches, vous passez la room.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1727929124746/ec215a11-4efe-48fb-b1c7-e341be7e5bc0.png align="center")

Pour démarrer la machine cible, cliquez sur le bouton vert "Start machine". Une fois démarrée, donnez-lui quelques minutes pour afficher son adresse IP.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1727929152565/d0853ded-10a0-4c75-b03a-9e6962d666a3.png align="center")

La plupart des cibles n'auront pas d'interface graphique. Vous n'interagirez avec elles qu'en utilisant une adresse IP.

Maintenant, vous avez besoin d'une machine d'attaque. THM offre une machine virtuelle Kali à utiliser comme machine d'attaque. Kali est une version de Linux avec tous les outils dont vous avez besoin préinstallés. Aucun setup ou installation supplémentaire n'est nécessaire.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1727929209495/1d6234da-acc0-4c7e-81dd-70f2ef0d3888.png align="center")

Vous pouvez trouver le bouton "Start Attackbox" en haut à gauche. Il ouvrira la machine d'attaque en divisant votre écran.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1727929187803/10b8c5c6-a0bf-4f58-ab67-94cb3b4ad25f.png align="center")

### Tâches du laboratoire

Le laboratoire est divisé en cinq tâches :

#### 1. Présentation de la plateforme

Cette tâche vous donne une introduction au fonctionnement de la plateforme, similaire à la section ci-dessus. Une fois que vous avez démarré les deux machines virtuelles, vous pouvez tester la connexion en pingant la cible depuis l'Attackbox.

#### 2. Linux 101

Nous avons ajouté une tâche sur les commandes Linux de base. Même si vous êtes un utilisateur Linux expérimenté, cela peut vous aider à rafraîchir vos compétences. Voici les commandes avec lesquelles vous allez travailler.

* **whoami** — vous indique le nom d'utilisateur de l'utilisateur actuellement connecté.

* **pwd** — Affiche le chemin complet du répertoire actuel. Cela vous aide à suivre votre emplacement actuel dans le système.

* **clear** — efface l'écran

* **ls** — Liste les fichiers et répertoires dans le dossier actuel.

* **cat** — Affiche le contenu d'un fichier. Il peut également aider à créer de nouveaux fichiers. cat [nomdefichier] affichera le contenu d'un fichier. En utilisant l'opérateur >, cat > [nomdefichier] créera un nouveau fichier.

* **rm** — Supprime des fichiers ou des répertoires. Utile pour nettoyer les traces d'activités, comme la suppression des logs.

#### 3. Scanning avec Nmap

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1727929253716/10a18e13-8afe-4a4b-af18-cf4caff653ba.jpeg align="center")

[Nmap](https://www.stealthsecurity.sh/p/nmap-tutorial) (abréviation de Network Mapper) est un outil gratuit et open-source utilisé pour le scanning de ports. Il peut scanner les ports ouverts, identifier les services et même détecter le système d'exploitation de la cible.

Nmap vous aidera à scanner la cible en utilisant son adresse IP. Les informations de Nmap vous aideront à trouver des points d'entrée pour accéder à la cible.

#### 4. Brute-forcing avec Hydra

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1728308769373/c5d58a65-12f0-4cea-8248-37119ec77cd5.jpeg align="center")

Une fois que vous avez trouvé un point d'entrée, vous pouvez utiliser un outil de brute-force pour trouver le mot de passe. Dans cette cible, il y aura un port SSH ouvert. SSH est un protocole qui aide à se connecter à un serveur à distance.

Vous utiliserez [Hydra](https://www.stealthsecurity.sh/p/hacking-hydra-practical-tutorial) avec une liste de mots de passe pour pirater votre chemin vers le serveur cible. Une fois que vous avez trouvé le mot de passe, vous pouvez vous connecter à la cible en utilisant SSH. Voici la syntaxe pour utiliser SSH afin de se connecter à un serveur.

`ssh username@ip_address`

Il vous demandera ensuite le mot de passe. Une fois connecté à la cible, vous pouvez trouver un fichier texte appelé flag2.txt. Le contenu de ce fichier sera la réponse à la question finale du laboratoire.

#### 5. Conclusion

La tâche finale vous demandera votre feedback sur ce laboratoire. Faites-nous part de vos pensées et nous améliorerons ce laboratoire pour la prochaine personne.

### C'est parti

Allez sur [TryHackMe](https://tryhackme.com/?utm_source=www.stealthsecurity.sh&utm_medium=referral&utm_campaign=hack-your-first-machine) et inscrivez-vous pour un compte. Une fois que vous avez terminé, [cliquez ici](https://tryhackme.com/jr/SS_HYFM?utm_source=www.stealthsecurity.sh&utm_medium=referral&utm_campaign=hack-your-first-machine) pour accéder au laboratoire.

Bon piratage !

**Pour plus d'articles sur la cybersécurité, rejoignez notre newsletter gratuite** [**Stealth Security**](https://www.stealthsecurity.sh/)**. Pour apprendre les outils de piratage éthique en utilisant des laboratoires pratiques, consultez notre communauté privée** [**The Hacker's Hub**](https://www.skool.com/hackershub)**.**