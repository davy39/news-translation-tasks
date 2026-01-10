---
title: Qu'est-ce qu'un identifiant de processus ? Comment utiliser les PID pour la
  gestion des processus
subtitle: ''
author: Syeda Maham Fahim
co_authors: []
series: null
date: '2025-01-30T17:34:30.447Z'
originalURL: https://freecodecamp.org/news/what-is-a-process-id-process-management-tutorial
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1738252940529/8ee6969c-7a74-4b2f-bd33-f2d48332e8e0.png
tags:
- name: System administration
  slug: system-administration
- name: cmd
  slug: cmd
seo_title: Qu'est-ce qu'un identifiant de processus ? Comment utiliser les PID pour
  la gestion des processus
seo_desc: 'Have you ever wondered how a computer knows which program’s output to display,
  especially when multiple programs are running simultaneously? This is possible because
  of the Process ID (PID).

  A PID is a unique identifier that helps the operating syste...'
---

Vous êtes-vous déjà demandé comment un ordinateur sait quel programme afficher, surtout lorsque plusieurs programmes s'exécutent simultanément ? Cela est possible grâce à l'identifiant de processus (PID).

Un PID est un identifiant unique qui aide le système d'exploitation à suivre et à gérer les programmes en cours d'exécution.

Dans cet article, nous allons explorer ce qu'est un identifiant de processus (PID), pourquoi il est important et comment vous pouvez l'utiliser pour gérer les processus, y compris la terminaison d'un programme lorsque cela est nécessaire.

## Comprendre les PID : Comment un ordinateur identifie-t-il les programmes en cours d'exécution ?

Considérons deux scripts Python :

* `hello_maham.py` → `print("Hello Maham")`

* `hello_amna.py` → `print("Hello Amna")`

Comment l'ordinateur sait-il que `hello_maham.py` doit afficher "Hello Maham" et non "Hello Amna" de `hello_amna.py` ?

Si vous pensez que cela se produit magiquement, détrompez-vous ! Cela se produit grâce à quelque chose appelé **Process ID (PID)**.

Dans tout système d'exploitation, des processus s'exécutent constamment en arrière-plan pour exécuter des tâches. Qu'il s'agisse d'un programme que vous avez lancé manuellement ou d'une tâche système s'exécutant automatiquement, chacun de ces processus se voit attribuer un PID unique.

Décomposons cela davantage.

## Qu'est-ce qu'un identifiant de processus (PID) ?

Simplement,

> *Un* ***identifiant de processus (PID)*** *est un identifiant unique attribué à chaque processus s'exécutant dans un système d'exploitation.*

Comprenons ce qui se passe en arrière-plan.

Chaque fois qu'un programme s'exécute, quel que soit le langage, il a besoin de mémoire et de temps pour s'exécuter. Ainsi, lorsque vous exécutez un programme, le système d'exploitation crée un nouveau processus pour celui-ci. Pour identifier le programme, l'ordinateur lui attribue un identifiant unique - le **Process ID** - puis il commence l'exécution.

Revenons à notre exemple précédent :

* Lorsque vous exécutez `hello_maham.py`, le système lui attribue un PID unique.

* De même, lorsque vous exécutez `hello_amna.py`, il obtient son propre PID unique.

C'est pourquoi les sorties des deux scripts ne se chevauchent pas !

Maintenant, vous avez compris ? Chaque fois qu'un nouveau processus est créé, le système s'assure que chaque processus obtient un PID différent. Ce PID est utilisé par le système pour gérer et interagir avec les processus. On appelle cela **l'unicité des PID**

### Comment l'ordinateur gère-t-il cet identifiant ?

Vous vous demandez peut-être si l'ordinateur a des millions de PID ? Après tout, nous pourrions exécuter de nombreux programmes en même temps.

La réponse est **non**. Une fois qu'un processus se termine, le PID devient disponible pour une réutilisation. Cela signifie que les PID sont réutilisables et qu'il n'y a pas de pénurie.

### Mais pourquoi et quand ai-je besoin des PID ?

Maintenant que vous savez ce qu'est un PID, vous vous demandez peut-être : **Pourquoi ai-je besoin de cela ?**

Eh bien, les PID sont en fait très utiles pour les administrateurs système et les développeurs. Ils aident à :

**Les administrateurs système et les développeurs gèrent les processus**. Par exemple, si quelque chose ne fonctionne pas correctement, vous devez pouvoir trouver et arrêter le processus spécifique causant le problème, n'est-ce pas ?

Les PID sont également importants pour la **gestion des ressources**. Le système d'exploitation les utilise pour allouer de la mémoire et du temps CPU à chaque processus, afin qu'un seul programme ne monopolise pas tout.

## Comment trouver le PID d'un programme en cours d'exécution

Jusqu'à présent, nous avons couvert les concepts théoriques. Maintenant, vous vous demandez peut-être : Comment trouver réellement le PID d'un programme sur mon ordinateur ?

Eh bien, voici quelques méthodes simples pour trouver le **PID** d'un programme en cours d'exécution en utilisant diverses commandes dans le terminal.

Notez que j'ai utilisé Bash pour exécuter la commande PID et inclus une capture d'écran pour celle-ci. Mais pour d'autres terminaux comme CMD et PowerShell, les commandes respectives sont mentionnées à la fin.

Certaines de ces méthodes incluent :

### 1. Utilisation de la commande `ps`

La commande `ps` affiche un instantané des processus en cours d'exécution et de leurs PID.

```bash
ps aux | grep <nom_du_programme>
```

Voici un exemple :

```bash
ps aux | grep python
```

Cette commande affichera tous les processus Python en cours d'exécution sur le système, ainsi que leurs PID.

![Processus Python en cours d'exécution plus leurs PID](https://cdn.hashnode.com/res/hashnode/image/upload/v1737914130884/686568b8-77d5-439d-a08b-61e18d4e5d56.png align="center")

### 2. Utilisation de la commande `top`

La commande `top` affiche des informations en temps réel sur les processus en cours d'exécution sur le système, y compris leurs PID.

```bash
top
```

Regardez sous la colonne **PID** pour trouver le processus qui vous intéresse.

![Résultat de l'exécution de la commande top](https://cdn.hashnode.com/res/hashnode/image/upload/v1737914189672/43f93890-2e06-42a8-b61b-9103227cf912.png align="center")

## Comment tuer un processus en utilisant son PID

Que faire si vous voulez **tuer** le programme ? Qu'il s'agisse d'une tâche cron ou d'un programme qui se comporte mal ou qui s'exécute trop longtemps, comment pouvez-vous l'arrêter en utilisant le PID ?

Passons en revue comment vous pouvez faire cela :

### 1. Utilisation de la commande `kill`

Pour terminer un processus, utilisez la commande `kill` suivie du PID :

```bash
kill <PID>
```

Voici un exemple :

```bash
kill 1234
```

Cette commande terminera proprement le processus avec le PID `1234`.

### 2. Utilisation de la commande `kill -9` (Forcer la terminaison)

Si le processus ne s'arrête pas après avoir utilisé la commande `kill` régulière, vous pouvez forcer sa terminaison en utilisant la commande `kill -9` :

```bash
kill -9 <PID>
```

Voici un exemple :

```bash
kill -9 1234
```

Cela termine de force le processus et contourne toute procédure d'arrêt qu'il pourrait avoir, alors assurez-vous de l'utiliser avec prudence.

## Comment arrêter les tâches Cron en utilisant un PID - Exemple pratique

Supposons que vous avez une tâche cron en cours d'exécution et qu'elle se comporte mal. Comment l'arrêter ?

Les tâches cron sont des tâches planifiées qui s'exécutent automatiquement à des intervalles spécifiques.

Si vous devez arrêter une tâche cron en cours d'exécution, vous pouvez utiliser le PID du processus exécutant la tâche cron.

### Arrêter une tâche Cron en cours d'exécution

Si vous devez arrêter une tâche cron en cours d'exécution, vous pouvez utiliser le PID du processus exécutant la tâche cron.

Voici comment tuer une tâche cron :

1. **Trouver le PID** : Utilisez la commande `ps` ou `pgrep` pour trouver le PID de la tâche cron. Exemple :

    ```bash
    ps aux | grep cron
    ```

2. **Tuer la tâche Cron** : Une fois que vous avez trouvé le PID de la tâche cron, utilisez la commande `kill` ou `kill -9` pour l'arrêter.

## Commandes pour d'autres terminaux :

Voici comment gérer les processus dans différents terminaux :

| Action | Commande CMD | Commande PowerShell | Commande Bash |
| --- | --- | --- | --- |
| **Lister tous les processus** | `tasklist` | `Get-Process` | `ps aux` |
| **Trouver un processus par nom** | `tasklist | findstr <nom>` | `Get-Process | where { $_.Name -like "*<nom>*" }` | `ps aux | grep <nom>` |
| **Tuer un processus par PID** | `taskkill /PID <PID>` | `Stop-Process -Id <PID>` | `kill <PID>` |
| **Forcer la terminaison d'un processus** | `taskkill /F /PID <PID>` | `Stop-Process -Id <PID> -Force` | `kill -9 <PID>` |

## Conclusion

Comprendre les **identifiants de processus** est essentiel pour gérer les processus sur votre ordinateur. Avec des commandes simples, vous pouvez facilement trouver et arrêter les processus problématiques, assurant ainsi un fonctionnement fluide du système.

Alors, restez maître de votre système avec les PID !

**Restez connecté — @syedamahamfahim 🐬**