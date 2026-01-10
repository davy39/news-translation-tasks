---
title: Qu'y a-t-il dans un nom ? Édition DevOps.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-29T22:00:43.000Z'
originalURL: https://freecodecamp.org/news/whats-in-a-name-devops-edition-c3f4e1f85dfb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*g7vToxOAkz-rfjtpHwgApg.jpeg
tags:
- name: coding
  slug: coding
- name: Devops
  slug: devops
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Qu'y a-t-il dans un nom ? Édition DevOps.
seo_desc: 'By Jon Goodall

  I’ve been working in DevOps for a while now, and I’ve yet to come across a tool
  that didn’t have something odd about its name. It’s either got a backstory, a meaning,
  or it’s Greek. I don’t know why, but I’d postulate that it’s because...'
---

Par Jon Goodall

Je travaille dans le domaine du DevOps depuis un certain temps, et je n'ai pas encore rencontré d'outil qui n'avait pas quelque chose d'étrange dans son nom. Soit il a une histoire, une signification, ou il est grec. Je ne sais pas pourquoi, mais je postulerais que c'est parce que le marché est complètement saturé d'outils, et vous **devez** faire en sorte que le vôtre se démarque, afin de pouvoir gagner de l'argent — soit avec l'outil lui-même, soit avec un package de support.

Avec cela en tête, j'ai pensé les traduire. Au cas où vous auriez un jour le malheur de devoir expliquer à quelqu'un du niveau C ("C" comme dans CEO, pas le juron), pourquoi vous essayez d'installer un poulpe.

Je les ai listés ici, et j'ai lié à l'explication, donc vous n'avez pas besoin de lire la liste. Mais faites-le, les stats sont un excellent boost pour l'ego.

* [Docker](#048e)
* [Jenkins](#ee62)
* [Bamboo](#82c6)
* [Drone](#62ba)
* [GoCD](#b86d)
* [Octopus Deploy](#38b3)
* [Ansible](#d56a)
* [Chef](#d1be)
* [Puppet](#d90d)
* [TeamCity](#39cb)
* [UrbanCodeDeploy](#054b)
* [Consul](#356e)
* [Vagrant](#16aa)
* [Kafka](#4af7)
* [Kubernetes](#a7f7)
* [Terraform](#63f0)
* [Vault](#f8c4)
* [Sentinel](#d8c4)

**Docker**.

_L'outil_ : crée, fait fonctionner et gère des conteneurs.

_La signification_ : Les conteneurs sont à un moment donné dans un dock. Un "docker" est un raccourci occasionnel pour quelqu'un qui travaille dans un dock, avec des conteneurs.

**Jenkins**.

_L'outil_ : Outil d'intégration continue (CI) à usage général. Le CD a été retconné avec des plugins qui vous permettent d'écrire des pipelines (que j'apprécie particulièrement).

_La signification_ : Nom stéréotypé pour un majordome. Les majordomes gèrent les ménages et "font les choses" de manière générale. À ne pas confondre avec un valet (essentiellement l'équivalent masculin d'une femme de chambre). Il y a aussi beaucoup de définitions créatives sur UrbanDictionary, mais je refuse de lier cela (parce que sans doute quelqu'un m'enverra une facture pour cela).

**Bamboo**.

_L'outil_ : Outil CI/CD d'Atlassian. Fonctionne avec d'autres outils Atlassian (jira, bitbucket, etc.) beaucoup mieux que d'autres outils.

_La signification_ : Plante à croissance rapide, peu nutritive, les pandas en mangent beaucoup — celle-ci n'a pas de sens pour moi.

**Drone**.

_L'outil_ : Encore un autre outil CI/CD. Celui-ci fonctionne dans Docker, avec des pipelines écrits dans une version de docker compose. Je suppose que vous pourriez l'appeler "natif de conteneur", si vous voulez. Ils le font.

_La signification_ : Le nom propre pour la plupart des insectes "ouvriers". Et ce que chaque employé d'entreprise ressent plusieurs fois par jour. En tout cas, c'est ce que je ressens.

**GoCD**.

_L'outil_ : **ENCORE UN OUTIL CD.** Les noms étranges commencent à avoir plus de sens maintenant... (Cette définition est un peu injuste, car c'est en fait un très bon outil. Beaucoup de fonctionnalités intégrées, fonctionne très bien sur Kubernetes.)

_La signification_ : Il est écrit en GoLang. Vous pourriez le prendre pour signifier "Allez et faites du CD".

**Octopus Deploy**.

_L'outil_ : L'un des rares outils spécifiques de déploiement (en dehors de quelques outils de déploiement de bases de données) que j'ai rencontrés. L'argument de vente est qu'il vous évite d'écrire des scripts massifs. Cela fera le "gros du travail" pour vous. Je ne suis pas sûr d'acheter cela. Je ne suis pas sûr qu'ils le fassent non plus, car ils ont une méthode d'écriture de pipelines en tant que code.

_La signification_ : On dirait que quelqu'un a pensé être malin avec celui-ci — "un poulpe a des tentacules, nous appellerons nos agents distants des tentacules". Jolis graphiques de poulpe cependant.

**Ansible**.

_L'outil_ : Outil de gestion de configuration (il y en a quelques-uns dans la liste, et en essence, ils vous permettent tous de déterminer l'état d'un serveur en code). Utilise un fichier YAML (Yet Another Markup Language) pour stocker sa configuration. Les étapes sont exécutées séquentiellement par défaut, donc l'ordre est simple.

_La signification_ : Je pense que celui-ci est assez intelligent, si vous aimez la science-fiction.

> "Le nom d'Ansible vient à l'origine du livre Rocannon's World d'Ursula Le Guin, publié en 1966. Elle a utilisé le mot comme nom d'un dispositif de communication instantanée qui permettrait le contact sur de vastes distances interstellaires"

> [— https://h2g2.com/edited_entry/A1165501](https://h2g2.com/edited_entry/A1165501)

Je ne sais pas si c'était l'inspiration pour le nom, mais j'aime à penser que c'était le cas.

**Chef**.

_L'outil_ : Outil de gestion de configuration. Les étapes sont dans des "recettes". Très belle interface.

_La signification_ : Les chefs lisent des livres de cuisine ou créent des recettes pour obtenir le même résultat final à chaque fois (enfin, presque. Cela dépend du restaurant. Espérons que ce n'est pas le cas ici).

**Puppet**.

_L'outil_ : Outil de gestion de configuration (encore). L'IDE s'appelle "geppetto", ce qui est sympa. (Geppetto a fait Pinocchio, au cas où vous ne le sauriez pas. Je ne le savais pas jusqu'à ce que je le cherche).

_La signification_ : Vous contrôlez une marionnette sur un ensemble de ficelles depuis ailleurs. Puppet lui-même est cependant l'inverse la plupart du temps, car les cibles de déploiement demandent les changements.

**TeamCity**.

_L'outil_ : Outil CI/CD de JetBrains (qui fabriquent [Intellij](https://www.jetbrains.com/idea/) et une série d'autres outils).

_La signification_ : Euh. Oui. Aucune logique ou histoire intelligente ici que j'ai pu trouver. On dirait qu'il a été fait pour vendre à de grandes entreprises — ce que, pour être honnête, je peux comprendre.

**UrbanCodeDeploy**.

_L'outil_ : La version d'IBM d'un outil de déploiement. Le seul outil que j'ai trouvé qui n'a pas d'essai gratuit ou de téléchargement, donc je n'ai pas pu l'essayer.

_La signification_ : Je n'ai pas pu trouver de raison derrière celui-ci, donc je pense que c'est juste un nom.

**Consul**.

_L'outil_ : Magasin clé/valeur de Hashicorp. Belle CLI et API. Fait aussi la découverte de services, la vérification de santé et le DNS (via des agents).

_La signification_ : Celui-ci n'a absolument aucun sens pour moi. Un consul est un officiel nommé par un état pour vivre dans une ville étrangère et protéger les intérêts de l'état là-bas — par exemple, ils travaillent au consulat.

**Vagrant**.

_L'outil_ : Vous permet de créer des PC virtuels rapides et bon marché sur votre PC physique existant. Vous évite la douleur d'avoir à utiliser directement les outils VirtualBox/VMWare. Bien que vous deviez toujours les installer.

_La signification_ : Colloquialisme pour un mendiant errant. Si vous faites un peu de gymnastique mentale, vous pouvez voir où ils voulaient en venir — personne sans adresse fixe, PC virtuel sans domicile permanent.

**Kafka**.

_L'outil_ : Utilisé pour construire des flux de données en temps réel.

_La signification_ : Apparemment, il est nommé d'après [Franz Kafka](https://en.wikipedia.org/wiki/Franz_Kafka).

**Kubernetes** :

_L'outil_ : Kubernetes est un "outil d'orchestration de conteneurs". Ce qui se traduit par le fait qu'il contrôle de grandes quantités de conteneurs.

_La signification_ : Traduit librement du grec comme un timonier, ou pilote de port. Essentiellement un contrôleur. Oui, l'orthographe est un peu différente, mais vous pouvez voir la logique ici.

**Terraform**.

_L'outil_ : Infrastructure en tant que code de HashiCorp. Vous permet de créer n'importe quoi chez les principaux fournisseurs de cloud, et gère leur état. Ainsi, si quelqu'un change quelque chose à la main, terraform peut le corriger.

_La signification_ : Incontournable de la science-fiction. Changer l'environnement pour vous adapter. Nous (en tant qu'espèce) pourrions le faire à Mars (la planète, pas le chocolat) un jour.

**Vault**.

_L'outil_ : Garde les données en sécurité, seules les personnes connues ont les clés. Peut sceller/désceller/re-clé. Diverses politiques d'accès.

_La signification_ : Une autre analogie. Pas un coffre-fort hollywoodien avec une grande pièce derrière 1 énorme porte, mais plutôt un coffre avec beaucoup de coffres de dépôt de sécurité à l'intérieur. Pour une référence cinématographique, je choisirais "The Bank Job (2008)".

**Sentinel**.

_L'outil_ : Politiques en tant que code. Fonctionne avec d'autres outils HashiCorp (version entreprise, vous devez payer pour celui-ci) pour garantir qu'ils ne sont utilisés que de manière prédéfinie. Beaucoup de bons exemples sur leur site web, allez y jeter un coup d'œil.

_La signification_ : Les sentinelles gardent ou surveillent les choses pour s'assurer que les gens ne font pas ce qu'ils ne sont pas censés faire. Typiquement du personnel militaire.

#### Conclusion

Voilà, c'est tout pour l'instant, parce que je n'ai plus de cerveau. Si vous êtes arrivé à ce point, je suis impressionné. Si vous avez parcouru la liste pour voir s'il y avait une déclaration finale spirituelle "hi, *waves* ". Si vous vouliez seulement voir ce qu'était Sentinel et m'avez vu faire des signes, je ne vous en veux pas.

J'essaierai de publier une suite à un moment donné lorsque je trouverai/essaierai/utiliserai plus d'outils — particulièrement ceux avec des noms "étranges". Si vous en avez rencontré que j'ai manqués, ou si vous avez une meilleure raison/définition pour ceux que j'ai, laissez-moi un commentaire.

Espérons que cette liste (très sèche, assez ennuyeuse) vous évitera un peu de mal de tête, ou vous en donnera un, qui sait. Je promets que la prochaine fois j'écrirai sur quelque chose d'intéressant et peut-être que je m'énerverai un peu.