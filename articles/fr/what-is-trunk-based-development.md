---
title: Qu'est-ce que le Trunk Based Development ? Une approche différente du cycle
  de vie du développement logiciel
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2024-06-18T12:55:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-trunk-based-development
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/Trunk-based-development.png
tags:
- name: 'development process '
  slug: development-process
- name: Git
  slug: git
- name: software development
  slug: software-development
seo_title: Qu'est-ce que le Trunk Based Development ? Une approche différente du cycle
  de vie du développement logiciel
seo_desc: 'The Software Development Lifecycle (SDLC) is different at every company.

  The version control system used, peer review process, code review process, design
  review process, how you do CI, automated testing, and manual testing – all vary
  greatly dependi...'
---

Le **cycle de vie du développement logiciel** (**SDLC**) est différent dans chaque entreprise.

Le système de contrôle de version utilisé, le processus de révision par les pairs, le processus de révision de code, le processus de révision de conception, la manière dont vous faites l'intégration continue, les tests automatisés et les tests manuels  tout cela varie considérablement en fonction de l'endroit où vous travaillez.

La manière dont une entreprise planifie, écrit, construit, révise, déploie et publie des logiciels est optimisée pour son cas d'utilisation particulier, en gardant à l'esprit ses propres forces et faiblesses.

J'ai commencé à lire comment différentes grandes entreprises technologiques gèrent leurs cycles de vie du développement logiciel (**SDLC**) et j'ai entendu le terme **Trunk-Based Development** à plusieurs reprises. Il s'agit d'une pratique suivie par Google et j'étais curieux de savoir en quoi elle diffère de la manière dont la plupart des autres entreprises développent des logiciels.

## Deux façons différentes de gérer les branches

### Branching de release

Il existe deux approches courantes pour permettre à plusieurs développeurs de travailler sur une seule base de code.

La première que nous appellerons la méthode de **branching de release**. Je l'ai également vue appelée **feature branching**. Mais ces deux approches suivent le même schéma général.

Généralement via Git, les développeurs clonent tous la base de code (de sorte qu'ils aient tous des copies identiques sur leurs machines). Ensuite, ils créent une nouvelle branche de fonctionnalité/release basée sur `main`, et fusionnent au fur et à mesure que le travail est terminé. L'accent est mis ici sur le fait qu'ils ne fusionnent qu'une seule fois, à la fin, lorsque tout le travail est terminé  et ils fusionnent l'ensemble de la branche dans `main`.

Voici un aperçu de la manière dont les développeurs utilisent la méthode **Release Branch** :

![Image](https://www.freecodecamp.org/news/content/images/2024/06/ex1.png)
_**Développement par branching de release visualisé._

Les points blancs représentent les commits, et la ligne noire solide du bas est `main`. Il s'agit d'un exemple très simple, car les **branches de release** finissent souvent par avoir beaucoup plus de commits que ce que j'ai montré dans le diagramme (parfois des centaines).

Les développeurs créent une branche à partir de `main`, apportent leurs modifications, et ensuite, lorsqu'elles sont terminées/ont passé la QA du code, elles sont fusionnées dans `main`. C'est le **branching de release**.

### Trunk Based Development (TBD)

Le **T**runk-**B**ased **D**evelopment (TBD) est la deuxième approche. Ici, chaque développeur divise le travail qu'il va faire en petits lots et fusionne dans `main` (qui est souvent appelé le **trunk**) plusieurs fois.

Dans les petites équipes, ils ne créent généralement pas de branche et ne fusionnent pas la branche dans le trunk. Ils committent _directement_ dans le trunk sans branches.

Dans une équipe plus grande (avec des vérifications et des approbations nécessaires pour les MR), ils utilisent des branches _de courte durée_. Une **branche de release** avec 100 commits en TBD serait 10 demandes de fusion avec 10 commits chacune.

En TBD, leurs modifications de code ne restent généralement pas plus de quelques heures. Elles sont constamment fusionnées et intégrées avec le code que tout le monde écrit.

Jez Humble est un ingénieur en fiabilité des sites chez Google et auteur de [Continuous Delivery](https://www.amazon.com/dp/0321601912?tag=contindelive-20), qui dit "le branching n'est pas le problème, la fusion est le problème"  ce que TBD essaie précisément de résoudre.

Il vise à éviter les fusions douloureuses qui se produisent si souvent lorsqu'il est temps de fusionner des branches de longue durée qui ont des historiques divergents du trunk, ou même de fusionner plusieurs branches ensemble en une seule provenant de différentes équipes/développeurs avant de fusionner avec le trunk.

## **Le TBD fonctionne-t-il à grande échelle ?**

Dans une [conférence Google](https://www.youtube.com/watch?v=W71BTkUbdqE), Rachel Potvin, qui est une responsable ingénierie chez Google, a décrit une base de code qui a (en janvier 2015) :

* 1 milliard de fichiers
* 2 milliards de lignes de code
* 86 téraoctets de contenu
* 45 000 commits par jour de travail
* 15 millions de lignes modifiées dans 250 000 fichiers par semaine

Ils ont utilisé le TBD dans cette base de code et cela a très bien servi leurs cas d'utilisation. Comme Google est composé de nombreux ingénieurs talentueux (et surtout **expérimentés**), ils rompent rarement leurs builds.

Google dispose également d'un processus de QA de code très complet et strict (lisez à ce sujet [ici](https://www.freecodecamp.org/news/what-google-taught-me-about-code-reviews/)) qui, lorsqu'il est utilisé avec le TBD, permet une livraison rapide et efficace des logiciels.

Le TBD fonctionne également bien pour les méthodologies Agile où vous devez livrer des logiciels fréquemment pour obtenir des retours de vos consommateurs/clients. Vous pouvez intégrer en continu et obtenir un bon aperçu de l'état actuel de votre projet.

Discutons brièvement de quelques forces du TBD.

### Forces du TBD

* Les retours (qu'ils proviennent de la QA du code ou de la révision par les pairs) arrivent rapidement, car vous fusionnez quotidiennement. Cela peut vous empêcher de faire la mauvaise chose pendant 3 semaines, puis de recevoir des retours indiquant que votre travail n'est pas correct à la toute fin, ce qui vous fait manquer des délais.
* Il y a un avantage mental au TBD, où les développeurs ont l'impression que le trunk est **notre** code, plutôt que chacun ait ses propres branches de fonctionnalités et pense que cette branche est **mon** code. Cela peut favoriser une culture plus collaborative, augmentant la communication.
* Cela conduit à une intégration précoce avec tous les autres projets/tickets en cours et vous aide à promouvoir la réutilisation du code. Il est beaucoup plus difficile d'"utiliser du code" qui n'est pas fusionné dans `main` et vous ne savez pas quand il sera terminé. Cela évite également l'enfer des fusions lorsque votre branche de release de 9 mois doit être fusionnée dans le trunk.
* Les grands projets avec beaucoup de travail sont obligés d'être divisés en livrables plus petits. Cela est beaucoup mieux pour estimer les délais et aussi pour diviser votre code en morceaux modulaires.
* Lorsque de nombreux développeurs travaillent en isolation sur des branches de release, il peut être plus difficile de repérer les développeurs juniors en difficulté dans leur propre branche. Mais s'ils sont censés committer leur travail quotidiennement, vous pouvez surveiller leur production quotidienne et les aider lorsque cela est nécessaire.
* Le TBD s'intègre très bien avec l'intégration continue. Avec de nombreux petits commits incrémentiels pour un projet finalement terminé, vous obtenez une base de code toujours testée, toujours intégrée avec des fusions (minimales) horribles.

### Faiblesses du TBD

* L'un des défis de cette approche est que vous avez une chance accrue de casser le trunk, et d'empêcher beaucoup de gens de travailler. Vous devez vous assurer que vos commits exécutent des tests unitaires ainsi qu'un bon processus de révision de code pour ne pas perdre de temps à annuler des commits toute la journée.
* Votre historique de commits dans `main` sera probablement plus verbeux et il peut être plus difficile de voir si quelque chose ne va pas. Si vous êtes appelé à 3 heures du matin et qu'on vous demande de corriger un bug sur votre site de production avec des commits douteux qui ont été faits pendant les heures de travail, préféreriez-vous une journée avec 1 commit ou 200 commits ?
* Si vous n'avez pas un processus de build rapide, vous passerez beaucoup de temps à attendre que les choses se construisent pendant que votre équipe commite constamment.
* Souvent, avec le TBD, vous ajoutez incrémentalement du nouveau code pour faire quelque chose de nouveau, mais vous avez également besoin que les anciens "chemins" que vous remplacez fonctionnent toujours. Pour cette raison, vous devez vous appuyer sur des bascules de fonctionnalités (généralement à partir d'une base de données) pour activer et désactiver les choses. Cela peut ajouter un niveau supplémentaire de complexité avec le débogage.
* Un dernier défi peut être que, lorsque vous avez des commits constants, vous êtes constamment dans un état de churn. Vous devez vous assurer que votre équipe tire régulièrement du trunk et ne finit pas par se marcher sur les pieds en fusionnant les choses.

## Comment publier des logiciels avec le Trunk-Based Development

Les équipes utilisant le TBD auront généralement un processus de publication différent de celui d'une équipe utilisant des branches de fonctionnalités.

Généralement, si vous utilisez des branches de release, vous publiez `main` chaque fois que vous avez quelque chose qui est fusionné (tickets, projets terminés, etc.). Ou certaines équipes publient `main` selon un calendrier, comme une fois par semaine.

Voici un aperçu de la manière dont les équipes TBD effectuent leurs publications :

![Image](https://www.freecodecamp.org/news/content/images/2024/06/ex2.png)
_Aperçu du processus TBD_

En TBD, le branching est utilisé pour les releases afin de permettre à tout le monde de continuer à committer dans `main`.

Ils fournissent un "instantané" de votre base de code dans un état stable, prêt pour le déploiement et la publication.

La seule raison pour laquelle le diagramme TBD ci-dessus pourrait nécessiter des détails supplémentaires est lorsque quelque chose ne va pas avec la publication de prj-123. Ensuite, nous committons le résultat dans le trunk et nous cherry-pickons les commits dans notre branche de release pour la mettre dans un état fonctionnel dès que possible.

Certains endroits, s'ils publient régulièrement, ne créent même pas de branche et peuvent simplement publier le trunk chaque fois que cela est nécessaire. Cela dépend souvent de votre entreprise.

## **Conclusion**

Il existe un site entier basé sur la théorie et la pratique du TBD. N'hésitez pas à lire plus [ici](https://trunkbaseddevelopment.com/).

J'espère que cela a expliqué ce qu'est le **Trunk Based Development** et pourquoi il est utilisé. Cela aide certainement à atténuer certains des problèmes liés à la fusion de branches de longue durée contenant des réécritures majeures.

Je partage mes écrits sur [Twitter](https://twitter.com/kealanparr) si vous avez aimé cet article et souhaitez en voir plus.