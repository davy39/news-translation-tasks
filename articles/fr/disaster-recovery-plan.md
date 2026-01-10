---
title: Comment créer un plan de reprise après sinistre pour votre équipe IT
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2020-05-14T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/disaster-recovery-plan
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b09740569d1a4ca2952.jpg
tags:
- name: insertone
  slug: insertone
- name: Disaster recovery
  slug: disaster-recovery
- name: incident management
  slug: incident-management
- name: RPO
  slug: rpo
seo_title: Comment créer un plan de reprise après sinistre pour votre équipe IT
seo_desc: "You know the old joke: there are two kinds of companies, those that've\
  \ been hit with IT disaster, and those who don't yet realize they've been hit with\
  \ IT disaster. \nBut what they all have in common is that there are plenty more\
  \ disasters to come. So..."
---

Vous connaissez la vieille blague : il existe deux types d'entreprises, celles qui ont été frappées par un sinistre informatique, et celles qui ne réalisent pas encore qu'elles ont été frappées par un sinistre informatique. 

Mais ce qu'elles ont toutes en commun, c'est qu'il y aura bien d'autres sinistres à venir. Alors demandez-vous si vous êtes prêt pour le prochain.

Cet article, basé sur mon [cours Pluralsight, Maintenance et Dépannage des Systèmes Linux](http://pluralsight.pxf.io/VMKQj), est destiné à vous faire réfléchir à ce que la création d'un protocole efficace nécessitera.

## Ce que vous devez avoir en place

Tout commence avec le **plan de continuité d'activité** (PCA). Il s'agit d'un plan formel destiné à définir les procédures qu'une organisation utiliserait pour assurer sa survie en cas d'urgence. 

Les PCA incluront généralement des sous-plans pour assurer la sécurité immédiate des employés et des clients, travailler à rétablir les opérations critiques précédemment désignées dès que possible et, finalement, rétablir les opérations normales complètes. 

De plus, un PCA efficace inclura également deux sous-plans spécifiques aux opérations IT : le protocole de gestion des incidents et le plan de reprise après sinistre.

Le **plan de reprise après sinistre** (PRA) vise à protéger l'infrastructure IT d'une organisation en cas de sinistre. Ses principaux objectifs sont de minimiser les dommages et de rétablir la fonctionnalité aussi rapidement que possible. 

La raison pour laquelle nous appelons cela un "plan" est qu'il ne fonctionnera tout simplement pas sans une préparation sérieuse au préalable. La protection de l'infrastructure, la détection des menaces et les protocoles correctifs sont des parties critiques du plan.

Un **Plan de Gestion des Incidents** (PGI) est destiné à traiter la menace spécifique des cyberattaques contre l'infrastructure IT. Ses objectifs sont de minimiser les dommages et d'éliminer la menace. 

Comme vous pouvez facilement le constater, il y aura un certain chevauchement entre votre PRA et votre PGI. Mais l'objectif principal de la reprise après sinistre est de remettre votre infrastructure sur pied, tandis que la gestion des incidents est beaucoup plus alignée avec le monde de la sécurité IT.

Pour le reste de cet article, nous allons examiner ce qui entre dans la création de plans de gestion des incidents et de reprise après sinistre et comment s'assurer que votre plan est solide et devrait, une fois exécuté, fonctionner réellement.

## Développement d'un Protocole de Gestion des Incidents

Puisque la gestion des incidents sera votre première réponse aux problèmes, nous commencerons par là. 

Le premier signe de problème peut venir d'un utilisateur qui remarque que quelque chose ne va pas avec le système. Ou, si vous avez fait un travail particulièrement bon en configurant votre infrastructure, cela peut aussi vous parvenir sous la forme d'une alerte automatisée déclenchée par un logiciel de surveillance.

Lorsque cette alerte arrive, ce sera le travail du technicien ou de l'administrateur de service de décider comment elle sera gérée et qui doit la gérer. 

L'escalade peut se faire par un appel téléphonique ou un email direct, un ticket soumis via un outil de collaboration comme Jira, ou en utilisant un outil dédié de Gestion des Informations et des Événements de Sécurité (SIEM).

Encore une fois, cependant, plus vous intégrez d'automatisation intelligente dans le processus, plus il sera rapide et efficace.

Quiconque se retrouve avec la responsabilité ultime coordonnera les efforts pour diagnostiquer et résoudre définitivement le problème. Idéalement, lorsque nécessaire, une telle coordination inclura les administrateurs, les développeurs et d'autres parties prenantes clés pour s'assurer que vous avez toutes les ressources nécessaires pour traiter le problème.

Lorsque tout sera terminé, une fois que vous aurez confirmé que le problème est résolu, vous voudrez clôturer l'incident en évaluant ce qui a mal tourné et ce qui a bien fonctionné, comment votre réponse aurait pu être meilleure, et comment vous pouvez retravailler les choses pour réduire le risque de répétition de l'incident.

Mais quel est le rapport avec l'administration IT ? Eh bien, les responsables IT doivent être capables de construire de la résilience dans leur infrastructure. 

Cela signifiera passer du temps sérieux à affiner leurs systèmes de surveillance logicielle afin qu'ils attrapent et vous alertent sur les vrais problèmes tout en émettant des alertes pour le moins de faux positifs possible. 

Et cela impliquera probablement aussi l'automatisation intelligente des systèmes de journalisation et de détection d'intrusion et, en général, avoir une bonne idée de ce à quoi les choses sont censées ressembler.

## Développement d'un Plan de Reprise après Sinistre

La planification de la reprise après sinistre nécessite de :

* Définir exactement ce que signifie la reprise
* Identifier les ressources nécessaires pour atteindre la reprise
* Convertir ces observations en un format de plan formel
* Communiquer le plan aux acteurs qui devront un jour le mettre en œuvre

Que signifie la **reprise** ? C'est lorsque votre infrastructure, pauvre et frappée, est revenue à l'état dans lequel elle se trouvait au moment où le sinistre a frappé. 

Ce dont vous aurez besoin pour revenir à ce point peut être défini en établissant un **Objectif de Temps de Reprise** (RTO) et un **Objectif de Point de Reprise** (RPO) qui correspondent aux besoins de votre organisation.

Un **Objectif de Temps de Reprise** représente le nombre maximum de minutes, d'heures ou de jours que votre organisation pourrait survivre à une interruption de service IT. Votre plan de reprise devra donc incorporer cette date limite dans ses protocoles.

Bien sûr, cela signifie que vous devrez avoir des membres de l'équipe disponibles pour se rendre au bureau même aux petites heures de la nuit assez rapidement pour faire une différence. 

Mais cela signifie aussi, par exemple, que si votre RTO est de six heures, mais que la restauration des données critiques à partir de vos sauvegardes prendrait un minimum de huit heures juste pour gérer le transfert, alors vous devrez repenser ces chiffres avant de valider le plan.

Un **Objectif de Point de Reprise** est la quantité de données de transaction que votre organisation pourrait se permettre de perdre pendant une interruption et survivre. 

Pour illustrer, un site web de commerce électronique qui traite normalement 25 transactions chaque minute pourrait, peut-être, se permettre de présenter des excuses et de rembourser 30 minutes de clients en colère se demandant pourquoi leurs cartes de crédit ont été facturées mais leurs trains électriques n'ont pas été livrés. Rembourser plus de 30 minutes, cependant, pourrait épuiser vos réserves financières au point que vous ne soyez plus viable.

Dans tous les cas, le calcul de RTO et de RPO précis et fiables est la manière dont vous fixez les limites dans lesquelles votre plan de reprise devra opérer. Ou, en d'autres termes, vous aurez défini ce que signifie la reprise.

Maintenant, qu'en est-il des **ressources** ? Par lesquelles j'entends les sauvegardes de données et, lorsque nécessaire, l'équipement physique dont vous aurez besoin pour remettre votre application sur pied. 

Pour que cela fonctionne, vous devrez décider d'un système de sauvegarde de l'infrastructure. Que vous choisissiez de faire des sauvegardes incrémentielles ou différentielles, sur site ou hors site, et sur un ou plusieurs types de supports, vous devrez cartographier exactement comment la reprise se déroulera et si elle respectera vos limites de RTO et de RPO.

Bien sûr, il n'y a pas de fin aux mauvaises choses qui peuvent arriver pour rendre ces plans totalement inutiles. Que se passe-t-il si votre centre de serveurs local brûle ? Que se passe-t-il s'il est perdu à cause d'un bouleversement politique ou d'une perturbation généralisée de l'alimentation ? 

Même si vous avez consciencieusement maintenu des sauvegardes de données à jour hors site, à quoi vous serviront-elles si votre matériel n'existe effectivement plus ?

Penser à toutes ces horreurs peut rendre la préparation d'un protocole de sauvegarde basé sur le cloud utilisant des plateformes comme AWS et Azure très attrayante. Les grands clouds publics ont les ressources pour distribuer leur infrastructure suffisamment largement pour qu'il soit virtuellement impossible que l'ensemble tombe jamais en panne.

Ainsi, vous pourriez, par exemple, maintenir un stockage de données répliqué de manière fiable sur une plateforme de cloud public qui reflète votre déploiement principal. Vous pourriez également concevoir un modèle d'infrastructure qui pourrait être chargé avec vos données de sauvegarde puis lancé à la demande pour prendre le relais en cas de panne. Parce que rien n'est maintenu en fonctionnement jusqu'à ce qu'il soit réellement nécessaire, cela peut prendre quelques bonnes minutes pour le mettre en vitesse.

Une conception de reprise en veille chaude pourrait maintenir vos données en fonctionnement 24/7 sur un nombre minimal de serveurs virtuels. En cas d'urgence, vous pouvez actionner l'interrupteur et l'auto-scaling de la plateforme démarrera toutes les instances dont vous aurez besoin. 

Vous pourriez configurer l'auto-scaling pour qu'il se déclenche lorsqu'il est activé par une alerte de votre système principal. Le cloud public présente des possibilités infinies, mais elles nécessitent toutes une planification et une préparation.

Un plan de reprise après sinistre solide doit être efficacement communiqué bien avant l'heure critique. En pratique, cela signifie qu'il sera tout rédigé, imprimé et distribué à chacun des acteurs clés qui mettront le plan en œuvre. 

Ce n'est pas pour dire que cela s'arrête là : ces acteurs auront bien sûr réellement lu le document et, idéalement, participeront à des simulations réalistes jusqu'à ce qu'ils soient confiants de pouvoir le faire fonctionner sous pression.

Que contient ce livre ?

* Une énumération de toutes les choses qui pourraient mal tourner et faire tomber votre système
* Un inventaire exact de ce que vous avez en fonctionnement dans votre salle serveur et de ce qui serait nécessaire pour le remplacer
* Les informations dont vous aurez besoin pour accéder et restaurer les données sauvegardées
* Une liste de contacts à jour des personnes qui seront responsables de chaque aspect du plan
* La séquence exacte des tâches et des événements qui composeront la reprise

C'est beaucoup de détails. Mais ce n'est qu'une goutte d'eau dans l'océan comparé à la quantité totale de préparation et de travail acharné qui entre dans la création d'un plan de reprise réel.

Mais pour l'instant, le point clé à retenir de ce module est simplement de garder tout cela à l'esprit. Pourquoi ? Parce que la prochaine fois que vous vous asseyez pour configurer un package de surveillance ou un framework d'administration, vous penserez aux protocoles de gestion des incidents et aux plans de reprise après sinistre et vous vous demanderez comment vous devriez les inclure dans votre configuration.

_Il y a beaucoup plus de bonnes pratiques d'administration sous forme de livres, de cours et d'articles disponibles sur mon site [bootstrap-it.com](https://bootstrap-it.com/)._