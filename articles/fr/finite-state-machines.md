---
title: Machine à états finis expliquée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-06T22:37:00.000Z'
originalURL: https://freecodecamp.org/news/finite-state-machines
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e19740569d1a4ca3b56.jpg
tags:
- name: design patterns
  slug: design-patterns
- name: finite state machine
  slug: finite-state-machine
seo_title: Machine à états finis expliquée
seo_desc: 'The finite state machine (FSM) is a software design pattern where a given
  model transitions to other behavioral states through external input.

  Understanding the Finite State Machine

  A FSM is defined by its states, its initial state and the transition...'
---

La machine à états finis (FSM) est un modèle de conception logicielle où un modèle donné passe à d'autres états comportementaux par le biais d'une entrée externe.

## **Comprendre la machine à états finis**

Une FSM est définie par ses **états**, son **état initial** et les **transitions**.

La puissance de la FSM vient de la capacité à définir clairement différents _comportements_ dans différentes conditions. Habituellement, la FSM est utilisée avec des scripts comportementaux en boucle qui évaluent constamment la situation actuelle dans une boucle ou avec des événements.

Pour aider à se faire une image de la manière dont cela pourrait être appliqué, une machine à café sera utilisée comme exemple de machine à états finis. Nous aborderons également un diagramme d'états pour visualiser la FSM et fournir des exemples de code.

### **Diagramme d'états**

![Diagramme de la machine à états finis de la machine à café](https://raw.githubusercontent.com/arunma/blogimages/master/AkkaFSM/CoffeeMachineFSM.png)

Ce diagramme montre trois états possibles pour la machine à café :

* Open (Ouvert)
* ReadyToBuy (Prêt à acheter)
* PoweredOff (Éteint)

Les lignes entre ces états montrent quelles transitions sont possibles entre les états et dans quelle direction. Ces transitions ont des conditions pour savoir quand la FSM doit changer d'état.

* StartUpMachine De l'état PoweredOff à l'état Open, la machine doit démarrer. Cela se fait manuellement dans ce cas.
* deposit >= cost of coffee La FSM évalue le montant de l'argent déposé soit dans une boucle, soit lorsque le montant change (recommandé dans ce cas). Si vous déposez suffisamment d'argent dans la machine à café, la FSM passera de « Open » à « ReadyToBuy ».
* ShutdownMachine La machine passera automatiquement de Open à PoweredOff via la méthode ShutDownMachine si la condition « no more coffees left » est remplie.
* DispenseCoffee Dans l'état ReadyToBuy, l'utilisateur peut acheter un café, après quoi il sera préparé et distribué. La condition est lorsque l'événement BuyCoffee (!Lien vers le modèle d'observateur !) se déclenche. (non montré dans le diagramme)
* CancelCoffee Si l'utilisateur choisit d'annuler, la machine passera de ReadyToBuy à Open.
* ShutDownMachine La machine passera à l'état PoweredOff

## États

Dans chaque état, il y a un comportement défini qui ne sera exécuté que lorsque l'objet est dans cet état. Par exemple, pendant l'état PoweredOff, la machine à café ne préparera pas de café avant d'être mise sous tension. Pendant l'état Open, elle attendra soit qu'il y ait suffisamment d'argent inséré, soit que la commande d'arrêt soit donnée, soit qu'il n'y ait plus de café. Pendant cet état Open, elle peut effectuer des routines telles que le nettoyage, qui ne se produira pas dans d'autres états.

### **État initial**

Chaque FSM a un état initial, ce qui signifie l'état dans lequel elle commence lorsqu'elle est créée et doit être défini lors de la construction ou de l'instanciation. Bien sûr, il est possible de changer directement d'état si les conditions sont remplies.

### **Transitions**

Chaque état évalue constamment s'il doit passer à un autre état ou passera à un autre état en fonction d'un événement déclenché.

## **DFA et NFA**

Il existe deux types d'automates finis, Déterministes (DFA) et Non déterministes (NFA). Les deux acceptent les langues régulières et fonctionnent plus ou moins de la même manière décrite ci-dessus, mais avec quelques différences.

Un DFA accepte ou rejette une chaîne de symboles et ne produit qu'un seul calcul ou automate unique pour chaque chaîne d'entrée. *Déterministe* fait référence à l'unicité du calcul. Une machine à états finis est appelée DFA si elle respecte les règles suivantes :

1. Chacune de ses transitions est déterminée de manière *unique* par son état source et son symbole d'entrée
2. La lecture d'un symbole d'entrée est requise pour chaque transition d'état.

Un NFA n'a pas besoin de respecter ces restrictions, ce qui signifie que chaque DFA est également un NFA. Et puisque les deux ne reconnaissent que les langues régulières, chaque NFA peut être converti en un DFA équivalent en utilisant l'algorithme de construction de l'ensemble des puissances.

Alors, quels types de règles pouvons-nous nous attendre à trouver dans les NFA mais pas dans les DFA ?

1. Un NFA peut avoir une transition de *chaîne vide* (généralement désignée par un epsilon). Cela signifie que, lorsqu'il est dans un certain état avec un epsilon pour une règle de transition, la machine peut passer à l'état suivant sans lire de symbole d'entrée.
2. Dans un NFA, chaque paire d'état et de symbole de transition peut avoir plusieurs états de destination, contrairement aux destinations uniques des paires dans les DFA.
3. Chaque paire d'état et de symbole de transition produit une « branche » de calcul pour chacune de ses destinations possibles, créant ainsi une sorte de système multithread.
4. Un DFA rejettera la chaîne d'entrée s'il atterrit dans un état autre que l'état d'acceptation. Dans un NFA, nous avons seulement besoin d'une « branche » pour atterrir dans un état d'acceptation afin d'accepter la chaîne.

Si vous souhaitez en savoir plus, voici un [guide approfondi sur les machines à états](https://www.freecodecamp.org/news/state-machines-basics-of-computer-science-d42855debc66/).