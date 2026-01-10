---
title: Comment gérer les processus Linux
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-02-03T00:07:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-manage-linux-processes
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/BB
seo_title: Comment gérer les processus Linux
---

Comment-gérer-les-processus-sous-Linux-.png
étiquettes:
- nom: Linux
  slug: linux
seo_title: null
seo_desc: "Nous suivons tous certains processus pour atteindre nos objectifs. De même, chaque système a ses propres processus pour accomplir des tâches. \nChaque programme ou commande qui s'exécute dans un système Linux est appelé un processus.\nDans ce tutoriel, explorons les processus et comment ..."
---

Nous suivons tous certains processus pour atteindre nos objectifs. De même, chaque système a ses propres processus pour accomplir des tâches. 

Chaque programme ou commande qui s'exécute dans un système Linux est appelé un processus.

Dans ce tutoriel, explorons les processus et comment nous pouvons les gérer sous Linux.

# Qu'est-ce qu'un processus Linux ?

Un processus est théoriquement appelé un programme en cours d'exécution. C'est essentiellement une tâche sur laquelle le système travaille actuellement. 

Chaque action que vous effectuez sur le système entraînera un nouveau processus. Par exemple, l'ouverture d'un navigateur initie un processus.

En termes simples, un processus est une instance d'un programme. L'action de l'utilisateur est transformée en une commande et un nouveau processus sera créé lors de l'exécution de la commande.

Les processus fonctionnent selon une hiérarchie parent-enfant. Comme le nom de la hiérarchie l'implique, un processus initié à partir d'une commande/programme est appelé le processus parent et le processus produit d'un processus parent est appelé le processus enfant.

## Types de processus Linux

Les processus sont classés en 2 types dans les distributions Linux :

1. Processus en premier plan
2. Processus en arrière-plan

### Processus en premier plan

Un processus qui nécessite que l'utilisateur le démarre à l'aide d'une commande de terminal ou d'un programme est appelé un processus en premier plan. Cela signifie que les processus en premier plan nécessitent un déclencheur d'entrée de la part de l'utilisateur. Ainsi, chaque processus en premier plan est déclenché manuellement.

Lorsque qu'un processus s'exécute en premier plan, les autres processus doivent attendre jusqu'à ce que le processus actuel se termine. 

Le meilleur exemple pour démontrer cela est via la commande `sleep`. La commande `sleep` ne permet pas à l'utilisateur d'interagir avec le terminal jusqu'à ce qu'un nombre donné de secondes se soit écoulé.

```
sleep 10
```

![Image](https://lh6.googleusercontent.com/Utfn4bYW2zEfEniaJ4QpFXeMIC9Cru1Ex-2OyRKAk2iGo9b7UBhnEspS3STn7HNOHyfSr081dWR1YgIRYGzkAH5UhfceLH3Xt5RofCs-B71b125bJtKi8vKqRC-IsGWM6N2TVpCapSvkdFclakrqq2LY1zfn4kq2ECAaoL8LAApPoM3ZLKeJahVVCF4qQw)
_Commande terminal `sleep` s'exécutant en premier plan et bloquant l'entrée utilisateur_

Nous devons attendre 10 secondes pour accéder au terminal afin d'exécuter une autre commande.

### Processus en arrière-plan

Un processus qui s'exécute indépendamment de l'entrée utilisateur est appelé un processus en arrière-plan. Contrairement aux processus en premier plan, nous pouvons exécuter plusieurs processus en même temps dans un processus en arrière-plan. 

Pour exécuter un processus en arrière-plan, placez un esperluette (&) à la fin de la commande que vous utilisez pour démarrer le processus.

Voici un exemple rapide pour démontrer cela :

Exécutons la commande `sleep` dans un processus en arrière-plan. Elle s'exécutera en arrière-plan et nous rendra le terminal pour exécuter d'autres commandes. 

![Image](https://lh4.googleusercontent.com/99ky8Jj_UgNSPmaxJC1k7KOQdfbN-_hhRh31cfAxpyxECAvJFHJjuHSrRF03epnMcUn14p_-w6I4obtRHBLPmIefL8CWT14hYr4_7WI6H3t6lzOCQWJWtajR_MVFfSiP986loc_qhxToalcOttf99gr6pyGJDgGU80hu3sMkJpJLLNu-VgbKugMiNrqnqQ)
_Commande terminal exemple pour un processus en arrière-plan_

```
sleep 10 &
```

Maintenant, nous pouvons voir que la commande ci-dessus s'exécute en arrière-plan. Elle a créé un processus avec le `PID` (19003). Nous pouvons donc exécuter une autre commande simultanément (commande `pwd`). 

## Comment changer un processus en premier plan en processus en arrière-plan

Si nous démarrons un processus en premier plan et que nous souhaitons le placer en arrière-plan, nous pouvons le faire en utilisant la commande `bg`. Voyons comment changer le processus en premier plan en arrière-plan.

Si un processus est en cours d'exécution, appuyez sur la touche `CTRL+Z`. Cette commande suspendra le processus actuel.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-372.png)
_Sortie du processus en premier plan_

Ensuite, exécutez la commande `bg`. Elle prend un identifiant de processus comme argument et place le processus en arrière-plan. Si l'argument est vide, il placera le processus actuellement suspendu en arrière-plan.

```
bg <process_id>
```

```
bg
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-373.png)
_Sortie du processus en premier plan vers le processus en arrière-plan_

Nous pouvons voir la commande suspendue (`sudo apt update`) reprenant en arrière-plan.

# Comment lister les processus Linux

Avant de passer à la manière de faire cela, vous devez savoir pourquoi vous pourriez avoir besoin de connaître une liste de processus. Voici quelques raisons :

1. Pour savoir quel processus consomme plus de temps.
2. Pour savoir quel processus prend plus de mémoire et d'utilisation du CPU.
3. Pour connaître la commande déclenchée pour un processus en cours d'exécution.

Pour voir les processus qui s'exécutent actuellement, nous pouvons utiliser la commande `ps` (Process Status) :

```
ps
```

![Image](https://lh3.googleusercontent.com/J0zD8uwiQQbCmoI7kCWQu8MCcoXIfQ9jhpOBnuq3G6xd7qkDxhpRhNGdS7OsLNYuZwllm0eTfsZWNCpr-tlvac38QSduFblom0flRKFg72mmzdN-iEQcv9scx6vu_yjWpRAlIJGays6Y1rfwJpcB3lamtZow6fCIO8gMKTQ8zhcK3XNpA6AKmKcaZcdViA)
_Commande `ps` affichant la liste des processus en cours d'exécution_

Pour lister le résumé de tous les processus de chaque utilisateur connecté, nous pouvons utiliser la commande `w`. Cette commande est la combinaison des commandes `who`, `uptime` et `ps -a` sous Linux.

```
w
```

![Image](https://lh3.googleusercontent.com/ws5Ip77K3CiODb9gfhjRSP5VQgaegkcabCw_rFcREWfHCnBDYlevoosQagnJ4tNfIG__yAV2OIG_BjzPWdTPx9WF4tMF2PfdTixR0aYu-7oo6vFUASwz-ZiHYxamFJU_nHpKNOlRMsVIthGrVMJtTXATBybJBlHBuTld4F-94PXVOlWJhashtH_f9bkDcg)
_Commande `w` affichant la liste des processus de tous les utilisateurs_

## Comment lister les processus en vue arborescente

Lorsqu'un programme/commande s'exécute, il initie un processus principal appelé processus parent. Le processus parent peut dépendre d'une autre commande/programme qui créera un processus enfant. 

Voici un exemple de capture d'écran. 

![Image](https://lh5.googleusercontent.com/Dwa-k101f5l6-Sy3ec8BotbvFggPF4x_UjXdmWpc_YB7AsFb_iKXT-RAjzwA3GhXQI3wa5hdwRBr8hL3eUh4TnyKft_LCPgC0XYDOtLEYeRRBKBGrjZNw3m9irt3XUkaV_7y86LXdRNCssT_Qa1eclk)
_Processus enfants du processus parent (firefox)_

Dans la capture d'écran ci-dessus, Firefox est le processus parent et les autres processus sont ses processus enfants. 

Explorons comment lister le processus dans une structure en forme d'arbre. 

`pstree` est une commande Linux pour lister les processus en cours d'exécution de tous les utilisateurs dans une structure en forme d'arbre. Elle est utilisée comme une alternative plus visuelle à la commande `ps`.

```
pstree
```

![Image](https://lh6.googleusercontent.com/g1gTo5zkfs92067V3p01xndG6c3XOHPjpHJAZTeT1U4wP1DDLopuxPKlgunnTpFDGZwl5BFIbFuaN5oJoRtiSi9xJcKcQihn_hhNth8R_FKpOdjm-VlQzwO7435ZTmCb2GLXILPO444ZwMxz0ZQVRk4)
_Commande `pstree` listant les processus en vue arborescente_

Comme nous pouvons le voir, les processus en cours d'exécution sont sous forme d'arbre. Cela peut être utile pour visualiser les processus. 

L'ajout du drapeau `-p` avec la commande affichera chaque branche avec son identifiant de processus.

```
pstree -p
```

![Image](https://lh6.googleusercontent.com/elX0V2qolKRLEhXmJuPc549_YdTr80Vz5t60XRucXDrYC3_LFKKRDlB_-kP_uJSYvepwX3n6_XQ8jLvzMohI76-gfhSPDO7eD1KEexqRqEfw49K4E2ZpPodobGvnPA0paKsGXHdxDQ1CjVpfTOSduGI)
_Commande terminal affichant la liste des processus en vue arborescente avec PID_

Pour lister le(s) processus enfant(s) d'un processus particulier, passez l'identifiant de processus comme argument à la commande `pstree`. 

```
pstree 3149
```

![Image](https://lh5.googleusercontent.com/L_OeZYxLZCDFFxMqelMfvxXWc2g3eKbKlt4EPV1bPfUBGZ5-STfSv9gxSEOksHsWuufeniSgbGS1-w5DL9uzEuQhWRMb7MOXuKpIn3Nr40wBJbDQkOnswClwvLhY0f9o-fuxV_OUwUqY6gDIc6koa0Q)
_Listage des processus en vue arborescente pour un processus particulier_

Plus tôt, j'ai mentionné que la commande `pstree` liste les processus de tous les utilisateurs. Le passage du nom d'utilisateur avec la commande `pstree` liste uniquement les processus exécutés par l'utilisateur. 

```
pstree root
```

![Image](https://lh6.googleusercontent.com/zTEM4mk9LXPrkBs3KoJ4Y8eBzuH3blStmsX-bgk1ohMwad8LF6hsAXwzSx_aF1vDqE-SdyhhaBWQrNyeuRNN_QHCrU5SY2TFDjnfB1cKbROiBsEBQmLuiXrGPV53ZKJqUGaM6TIYosf3TT1Uk1py-Po)
_Listage des processus en vue arborescente pour un utilisateur particulier_

La capture d'écran ci-dessus montre les processus exécutés par l'utilisateur `root`.

## Comment voir les processus d'un programme particulier

De nombreux développeurs ont peut-être été confrontés au scénario suivant :

Lors de la réalisation de projets de développement web, nous utilisons des navigateurs comme Chrome, Firefox et autres pour vérifier la sortie avec différents navigateurs. 

Certains développeurs continueront à ouvrir les onglets et ne fermeront jamais ceux qui sont ouverts. En raison de la charge élevée (si 150+ onglets sont ouverts), les navigateurs ne répondront parfois pas 😣, ce qui entraînera le blocage du système. Le pire, c'est que nous ne pourrons pas fermer le navigateur 😀. 

Contrairement à Windows, nous n'avons pas de Gestionnaire des tâches sous Linux pour tuer le navigateur. 

Ce problème peut être résolu facilement sous Linux également. Voyons comment un expert Linux gère ce scénario. 

Nous savons que chaque programme (y compris le navigateur) s'exécute en tant que processus. Vous devez donc simplement trouver l'identifiant du processus et le tuer.

Voyons comment trouver l'identifiant du processus d'une commande/programme dont vous avez besoin.

Dans mon système, Chrome est en cours d'exécution. Maintenant, nous pouvons obtenir les PID de Chrome en exécutant la commande suivante : 

```
pidof chrome
```

![Image](https://lh3.googleusercontent.com/TUL8R945bAnPXPIZ61Cs6VKzDVLAoRiOGbfZWD-x4u_Jzja72eGqGTXJjC14lhNqa4uF2-jKT3ttOtBJ6f-rbaxqGtEQoI2yPPwanl1ieftWpqMTMFGCn11pfRl2q3s98rehfm0-X7353cJ5KkoM1j2zLxk1CKAM6X-4NMxr_14M0WWdStMC9QhfqbbRrg)
_Commande terminal pour trouver l'identifiant du processus de chrome_

## Comment tuer un processus

Il existe une commande appelée `kill` sous Linux qui est utilisée pour tuer n'importe quel processus en passant le PID (identifiant de processus) ou le nom du processus. 

Voici la syntaxe de la commande `kill` :

```
kill <pid/nom_du_processus>
```

Stockez le PID de Chrome et tuez-le en utilisant la commande kill :

```
a=$(pidof chrome)
kill $a
```

![Image](https://lh5.googleusercontent.com/KJP27zaj4YOe4BlWlDQskMlX5ymEUfdcATwD-yyD6LpORFMrV7uTC-E8AlvbmQXpTYNKnytLhAmBgORLpCYCRHeTVnjU9lQfIISxcmFpUJtY13rnnPJT5sdYBz3oPkgr9MnXjqx8F8wdU_bAZTM6EhffPLIA9GhD8lrI3o4ysM-QWZdDLptnyEeadAM9HA)
_Commande terminal pour tuer un processus_

La commande ci-dessus tuera le navigateur web Chrome.

## Comment lister tous les processus

Nous pouvons voir tous les processus Linux en utilisant la commande `top`. Elle montre les mises à jour en temps réel de chaque processus pour tous les utilisateurs.

```
top
```

![Image](https://lh6.googleusercontent.com/aDFrfxMKy6yydKH81T7o4S-Z5cV552h0qTq34UH_oUuzj-Oml8CQVlzc2rrBUMNCawgMTxxePSFiI0uCTAHWVUMqaxe__JIGJFCbTn8TRoYWqzoDFxeUfmLHH4tphdUr8DYGyLPx-1vfEP-ZaMzfSlLvcNx-qaGTqxSc9JepmJRmbE5Crd6EI52sOt6JRQ)
_Commande terminal affichant tous les processus en temps réel_

Comprenons l'en-tête pour comprendre les données sous-jacentes. 

* PID représente un identifiant de processus unique.
* USER représente le nom d'utilisateur du propriétaire de la tâche.
* PR représente la priorité du processus. Plus le nombre est bas, plus la priorité est élevée.
* NI représente une valeur Nice de la tâche. Une valeur Nice négative implique une priorité plus élevée, et une valeur Nice positive signifie une priorité plus basse.
* VIRT représente la mémoire virtuelle totale utilisée par la tâche.
* RES représente l'utilisation de la RAM d'un processus en kilo-octets.
* SHR représente la taille de la mémoire partagée (Ko) utilisée par un processus.
* S représente l'état du processus :  
- **D :** Sommeil ininterruptible  
- **R :** En cours d'exécution  
- **S :** En sommeil  
- **T :** Traçage (arrêté)  
- **Z :** Zombie
* CPU représente l'utilisation du CPU.
* MEM représente l'utilisation de la mémoire de la tâche.
* TIME représente le temps CPU.
* COMMAND représente la commande utilisée pour démarrer le processus.

Pour afficher les processus d'un utilisateur spécifique, nous devons utiliser le drapeau `-u` :

```
top -u <nom_utilisateur>
```

Pour voir les processus exécutés par l'utilisateur `gogosoon`, exécutez la commande suivante :

```
top -u gogosoon
```

![Image](https://lh4.googleusercontent.com/yDIUnMQBUbjn9xRm0E3pv7yITR_0Kx5bZrxL1L1jrm3dBa_9qidIG_uBpllEZp33BetqHcl6un4lRJR-BI8iXQL7QJE0eI4Q-4BI8vDhXT7arh7m5KPXAlCLMJEQoCCX0uL6RgA5elm3rjkDRVVanBk_djmIGtHbD-Xkf63HVjbtmmhdC39cx8AOANBHyg)
_Sortie terminal de tous les processus démarrés par l'utilisateur `gogosoon`_

Vous pourriez être confus en voyant la sortie de la ligne de commande 😀. Il sera un peu difficile de déboguer les processus en temps réel. 

Voici l'outil GUI pratique pour gérer les processus sous Linux. Mais nous devons l'installer manuellement. Cela fonctionnera plus comme le gestionnaire de tâches sous Windows.

```
sudo apt install gnome-system-monitor
```

Après l'installation, tapez simplement le nom du logiciel dans le terminal :

```
gnome-system-monitor
```

Cela ouvrira tous les processus dans une nouvelle fenêtre avec une interface graphique décente :

![Image](https://lh3.googleusercontent.com/_fiYn6xqNuqSEBnqVTkEWhOVPYKoFUxqCkEdE427eWJEsY7WTx1OwuD7p09PG0sZFqrhqdNpYCoM4vhDR7qNB1pe8-uvZVigTUJ0E6BxyU8lgoRzORm4HlihLVsHk1bXgMo0rwHyaGBoajQDb6WQU25NdDRO-U82sYrMg5kxJx7bJrxYKV5yrdlAN2xMcQ)
_Gnome-System-Monitor_

Lorsque nous faisons un clic droit sur un processus, il affichera les actions comme tuer, arrêter, terminer, etc.

L'onglet Ressources montre les utilitaires suivants :

1. Historique du CPU
2. Historique de la mémoire et du swap
3. Historique du réseau

![Image](https://lh3.googleusercontent.com/0IB18GszrBCvE8827Ml5XuxtXlMZFVbgs5PcZkEN99BIeVjO2BOaULR55yjlbLrYA-i9qURCF4JC8mpxOkZ4_HZLGTDjRUnW5jHdfKzoEBToSYvm95bs5FnQvHYgGYbhPalFXq8D2DONHZGlWM-g1XACnt_FxpN4q7Wr8DUogBsPeuMXXMluIw01z9YbFA)
_Graphique de l'historique du CPU_

![Image](https://lh5.googleusercontent.com/xSO96ReEMCKtAgc11bigR6jwThKyjlk0Fz8oZt6hXh5ld4Rt9WWIEtZ-TOrZJ0tQFfx-lnCnH3vJjTBjzfFEulCzcAJgJqeDh8XrK3Ul9iH9Yant3FAbtmWMx5A9FyGcvHydw2nL-JBTGoWcaxUUkoTAiFMgiIuDQW4PVuMYjswFJPERQManNjiADfQ61A)
_Graphique de l'historique de la mémoire et du swap_

![Image](https://lh4.googleusercontent.com/Vo_9BWdfg0i_mtnCOUennGxyXwqPP_EgaiGwK8Wli7SHAGXQdtbUzu4BElWCvNkpxLLan7y3NGnlaCICiMwnRJ513_gOntCbPwT9w87husha2v6TeDPw-ey0-F_t3wnq7qlN3q9IpScjaR5BDFHRiWd1ywaSSeV_xEl1FC0cotqXcytTl0vYwciJrQc6fQ)
_Graphique de l'historique du réseau_

Ces graphiques seront utiles pour déterminer la charge de votre système. 

## Conclusion

Dans cet article, vous avez appris les bases des processus sous Linux. J'espère que vous comprenez maintenant un peu mieux comment ils fonctionnent. Je vous recommande à tous d'essayer ces commandes dans votre système.  

Pour en savoir plus sur Linux, abonnez-vous à ma newsletter par e-mail sur mon [site](https://5minslearn.gogosoon.com/?ref=fcc_linux_processes) et suivez-moi sur les réseaux sociaux.