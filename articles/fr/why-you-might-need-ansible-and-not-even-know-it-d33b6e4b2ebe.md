---
title: Pourquoi vous pourriez avoir besoin d'Ansible sans même le savoir
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-10T10:39:43.000Z'
originalURL: https://freecodecamp.org/news/why-you-might-need-ansible-and-not-even-know-it-d33b6e4b2ebe
coverImage: https://cdn-media-1.freecodecamp.org/images/0*TP4UG0OLyN06mS39
tags:
- name: Devops
  slug: devops
- name: Productivity
  slug: productivity
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Pourquoi vous pourriez avoir besoin d'Ansible sans même le savoir
seo_desc: 'By Piotr Gaczkowski

  Configuring machines with shell scripts is terribly messy

  Do you want to start using Ansible? Are you already using it, but coming up against
  challenges? Even if you don’t fall into either category, don’t stop reading. I’m
  going t...'
---

Par Piotr Gaczkowski

#### Configurer des machines avec des scripts shell est terriblement désordonné

Voulez-vous commencer à utiliser Ansible ? L'utilisez-vous déjà, mais rencontrez-vous des défis ? Même si vous ne vous situez dans **aucune de ces catégories**, ne cessez pas de lire. Je vais vous montrer pourquoi vous pourriez réellement **avoir besoin** d'Ansible et comment en tirer le meilleur parti.

Le slogan d'Ansible est « simple IT automation ». C'est une description assez précise de ce qu'il fait. Dans son mode de fonctionnement le plus populaire (il en existe plusieurs), vous décrivez l'état souhaité de vos machines, et Ansible les manipule pour atteindre cet état. À ce stade, vous pourriez penser « oui, mais nous avons déjà des scripts shell pour cela ». Ansible, cependant, offre plusieurs avantages par rapport aux bons vieux scripts shell.

Tout d'abord, le playbook, qui décrit l'état souhaité, est déclaratif et écrit en [YAML](http://yaml.org/). Utiliser un playbook signifie que vous n'avez pas besoin de gérer vous-même le contrôle des erreurs et la vérification des conditions. Cela signifie également qu'aucune action ne sera entreprise si l'état est déjà satisfait (par exemple, `apt-get` ne s'exécutera pas si un paquet `nginx` est déjà installé).

Mais ce n'est qu'une partie de l'histoire.

L'autre chose qui rend Ansible si puissant est l'utilisation de modules. Au lieu de dépendre de nombreuses applications tierces (`sed`, `grep`, `jq`, `useradd`, `parted`, etc.) et de parser leur sortie, vous pouvez vous concentrer uniquement sur l'état lui-même. Cela signifie que, indépendamment des programmes d'espace utilisateur sous-jacents (`useradd`, `adduser`, Busybox, variantes BSD ou GNU), vous pouvez simplement spécifier une tâche universelle comme suit :

```yaml
– name: Créer l'utilisateur operator
  user:
    name: operator
    createhome: yes
    groups: wheel
    shell: /bin/sh
```

De la même manière que vous encapsuleriez des parties de votre script dans des bibliothèques séparées, Ansible adopte le concept de rôles. Les rôles décrivent des états particuliers d'une machine, ainsi que des variables possibles, des fichiers de configuration ou des templates. Ils sont aptement nommés, et la machine peut utiliser des rôles comme `docker`, `nginx`, et `python`, par exemple. Chacun de ceux-ci peut alors être testé en isolation et réutilisé dans tous vos projets. Ils peuvent également encapsuler des concepts plus abstraits comme le rôle [ansible-hardening](https://github.com/openstack/ansible-hardening) d'OpenStack, qui rend une cible un peu plus difficile à pirater.

**Et l'autre chose cool ?** Pour exécuter Ansible, vous n'avez besoin que de Python 2.6+ sur vos machines cibles et d'une connexion SSH ouverte. Il n'est pas nécessaire d'installer quoi que ce soit d'autre ! Cela signifie que vous êtes probablement prêt à commencer à utiliser Ansible tout de suite ! Préparez votre machine de contrôle en exécutant `brew install ansible` ou `pip install -user ansible` et suivez-moi.

### Déploiement en tant que Code

**Oubliez le README situé dans le répertoire racine du projet.** Il contient généralement tous les détails fastidieux sur la manière de déployer en staging ou en production. Avec Ansible, la documentation est dans le code. Elle est testable, réutilisable, et peut être exécutée par n'importe qui, tant que la personne a accès aux machines cibles. Cela forme également la base parfaite pour un pipeline de Déploiement Continu (CD).

S'assurer que votre application est toujours déployable peut également aider à éviter les catastrophes. Au lieu de chercher à comprendre quoi faire lorsque vos serveurs tombent en panne, vous modifiez simplement le fichier d'inventaire et effectuez un nouveau déploiement sur un nouvel ensemble de machines.

### Assurez-vous que votre équipe est prête pour le DevOps

Lorsque le déploiement fait partie de la base de code, il doit évoluer avec celle-ci. Assurez-vous que toute votre équipe est habilitée DevOps et comprend comment utiliser Ansible. La meilleure façon de faire cela est de fournir un environnement Vagrant afin que chaque développeur puisse tester le processus de déploiement localement.

Il est essentiel que vous testiez votre code de déploiement de la même manière que vous testez votre application. Chaque changement dans une application qui peut être pertinent pour le déploiement doit être reflété dans les modifications des fichiers Ansible. Par exemple, si vous ajoutez de nouveaux fichiers qui doivent être copiés sur le serveur, assurez-vous qu'il y a une tâche correspondante. Si une application commence à journaliser dans un répertoire particulier, assurez-vous qu'Ansible crée ce répertoire et définit les permissions appropriées.

### Il est facile de le faire fonctionner, plus difficile de le rendre maintenable

Ansible a aussi ses inconvénients. Ceux-ci ne sont pas nécessairement liés à l'outil lui-même, mais ils apparaissent occasionnellement. Même si Ansible a des [bonnes pratiques](http://docs.ansible.com/ansible/latest/playbooks_best_practices.html) bien documentées, celles-ci ne vous aident pas toujours à atteindre un objectif unique. Cela peut conduire à la création de solutions compliquées alors que des solutions simples suffiraient.

### Préférez les déploiements ponctuels

Même si l'une des fonctionnalités qu'Ansible annonce est l'[idempotence](https://stackoverflow.com/questions/1077412/what-is-an-idempotent-operation), il est encore assez facile d'écrire un playbook qui ne fonctionnera pas correctement. Par exemple, comment mettez-vous à jour un service de manière idempotente ? Vous ne pouvez pas, c'est contradictoire, ce qui signifie que vous devez sacrifier une chose pour en sauver une autre (une mise à jour, en l'occurrence).

Il y a deux concepts qui peuvent aider avec ce problème : [l'infrastructure jetable](http://www.conigliaro.org/disposable-not-immutable-infrastructure/) et [l'infrastructure immuable](https://www.oreilly.com/ideas/an-introduction-to-immutable-infrastructure). Les deux sont assez similaires du point de vue du déploiement. La première suppose qu'une machine peut être facilement jetée à tout moment après un déploiement réussi. Elle peut être reconfigurée dans le futur, mais rien ne vous empêche de la supprimer à tout moment. La seconde exige également qu'une machine ne change jamais sa configuration après avoir été provisionnée.

Les deux supposent que votre application est située derrière un équilibreur de charge (ou un proxy inverse). Un tel équilibreur de charge pourrait être hébergé soit en externe, soit en interne, indépendamment du reste de l'infrastructure. Les services qui composent votre application sont enregistrés dans l'équilibreur de charge. La configuration backend est mise à jour dynamiquement à mesure que les services arrivent et partent. Si vous souhaitez héberger l'équilibreur de charge vous-même, [confd](https://github.com/kelseyhightower/confd) ou [consul-template](https://github.com/hashicorp/consul-template) peuvent aider à la reconfiguration dynamique.

### Utiliser et réutiliser les rôles

Des questions comme quand et comment utiliser les rôles ou quels aspects devraient être configurables n'ont pas de réponses simples et univoques. D'après mon expérience, il est préférable de penser aux différents cas d'utilisation pour une machine particulière, puis d'encapsuler ces cas d'utilisation dans des rôles séparés qui peuvent non seulement être testés en isolation, mais aussi être réutilisés pour d'autres projets. Une telle réutilisation conduit également à une meilleure qualité de code grâce à une base de tests plus large.

### Une galaxie de possibilités

[Ansible Galaxy](https://galaxy.ansible.com/) fournit de nombreux modules que nous pouvons utiliser. Cela ressemble à Docker Hub ou NPM, où vous pouvez rechercher les parties pertinentes et les utiliser dans votre projet. Ils sont tous écrits en respectant une norme unique, ce qui signifie qu'ils devraient être facilement réutilisables. Malheureusement, ce n'est pas toujours le cas.

Plus d'une fois dans ma carrière, je suis tombé sur un module qui déclarait être compatible avec Debian mais qui n'avait été testé que sur Ubuntu. Cela peut ne pas poser de problème si vous pouvez choisir votre système d'exploitation de base. Cela peut signifier un travail supplémentaire pour le porter si vous souhaitez utiliser une infrastructure existante.

Le verrouillage des versions est un autre problème. Nous savons tous que les logiciels évoluent et que la compatibilité ascendante est rarement respectée. Lorsque les modules utilisent plusieurs dépendances, il est crucial que chaque dépendance soit décrite avec une étiquette de version exacte. De cette manière, nous pouvons éviter le problème d'installation d'un package dans la dernière version qui n'est plus compatible avec une autre partie du système.

En parlant de versions verrouillées, il est impossible d'éviter le sujet de la dégradation des logiciels. Les logiciels inutilisés se dégradent. Les hyperliens référencés peuvent devenir obsolètes, les versions peuvent être retirées, les services d'hébergement peuvent cesser de fonctionner. Même si un module utilise une version verrouillée, il peut devenir inutilisable s'il n'est pas régulièrement testé et mis à jour selon les besoins, ce qui nous amène à notre prochain sujet.

### Les tests sont difficiles — et chronophages

Ansible opère généralement sur des services système. Bien qu'il soit possible de tester certaines de ses fonctionnalités dans des conteneurs (par exemple, avec Docker), cette approche échouera généralement. Docker ne peut pas tester toutes les opérations du noyau ou les appels systemd, car ils n'existent pas dans son champ d'application. Pour tester correctement les playbooks Ansible, vous avez besoin de machines virtuelles. **Avez-vous remarqué le pluriel ?** **Bien, car il ne suffit pas de tester sur une seule machine virtuelle.**

La configuration de test la plus basique devrait utiliser une machine virtuelle propre, exécuter le playbook, vérifier les résultats, puis exécuter à nouveau le playbook pour vérifier les problèmes d'idempotence. Mais cela ne vous donne que des informations limitées. Vous ne savez toujours pas si le playbook sera réellement déployé en production. La machine cible ne sera pas nécessairement une machine virtuelle propre (sauf si vous utilisez déjà une infrastructure jetable).

Pour atténuer ce risque, il peut être judicieux d'avoir une machine virtuelle séparée qui pourrait servir de « mémoire à long terme ». Cette machine virtuelle, en revanche, ne serait pas nettoyée après chaque déploiement de test, mais permettrait aux changements de s'accumuler au fil du temps.

### Résumé

La meilleure façon de documenter le code est dans le code lui-même. En considérant cette simple déclaration, nous arrivons à une conclusion logique — la meilleure documentation de déploiement est le code de déploiement. Il existe de nombreux outils pour aider à atteindre cet objectif, Ansible en étant l'un d'eux. Personnellement, je le préfère à [Chef](https://www.chef.io/chef/) ou [Puppet](https://puppet.com/), mais je n'ai pas encore essayé [Salt](https://saltstack.com/) ou [StackStorm](https://stackstorm.com/).

Comme pour chaque outil que j'ai rencontré dans ma vie professionnelle, il a aussi ses inconvénients. Les connaître à l'avance devrait vous aider à éviter certains des problèmes sur lesquels je suis tombé. Espérons que tirer parti de mon expérience vous fera gagner du temps et vous évitera des frustrations dans votre propre travail.

> _Si vous aimez [ce que je crée](https://medium.com/@doomhammerng), envisagez de [vous abonner à Bit Better](http://eepurl.com/gcdRVb). C'est une newsletter communautaire avec des recommandations pour des livres, des articles, des outils et parfois de la musique._

_Publié à l'origine sur [https://www.iamondemand.com](http://www.iamondemand.com/blog/might-need-ansible-not-even-know/) le 10 août 2017._