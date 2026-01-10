---
title: Qu'est-ce que l'Idempotence ? Expliqué avec des Exemples Concrets
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2024-02-29T00:44:58.000Z'
originalURL: https://freecodecamp.org/news/idempotence-explained
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/cover--2-.png
tags:
- name: idempotence
  slug: idempotence
- name: software development
  slug: software-development
seo_title: Qu'est-ce que l'Idempotence ? Expliqué avec des Exemples Concrets
seo_desc: 'Idempotence is a property of an operation that ensures that, if the operation
  is repeated once or more than once, you get the same result.

  Apply it once or more and the outcome''s the same, idempotence is the name.

  All rhyming aside, idempotence is an...'
---

L'idempotence est une propriété d'une opération qui garantit que, si l'opération est répétée une ou plusieurs fois, vous obtenez le même résultat.

Appliquez-la une fois ou plusieurs fois et le résultat est le même, l'idempotence est le nom.

Mis à part les rimes, l'idempotence est un concept important souvent utilisé dans la conception des objets du quotidien. Le principe sous-jacent de l'idempotence – où les actions répétées ne changent pas le résultat, au-delà de l'action initiale – a été appliqué implicitement ou explicitement à la fois au monde physique et au monde numérique de l'informatique en nuage et des applications logicielles.

Cet article vous montrera quelques exemples d'idempotence dans le monde physique, ainsi que la manière dont elle est utilisée dans les architectures logicielles pour construire des systèmes fiables et tolérants aux pannes.

## L'Idempotence dans le Monde Physique

Les boutons idempotents sont utilisés dans les systèmes du quotidien, comme les boutons de feux de circulation, le bouton d'arrêt des bus londoniens et les boutons d'appel d'ascenseur.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb07003d3-ffc7-4074-88d1-cee009fb7119_2374x1308.png align="left")

*Quelques exemples d'idempotence dans le monde physique : un bouton de feu de circulation pour piétons, un bouton d'arrêt dans un bus londonien et un bouton d'appel d'ascenseur.*

Appuyer plusieurs fois sur un bouton de feu de circulation ne fait pas changer le feu plus rapidement – il enregistre simplement le besoin d'un passage pour piétons une fois.

De même, appuyer sur le bouton d'arrêt d'un bus londonien signale au conducteur de s'arrêter à l'arrêt suivant – mais appuyer plusieurs fois ne change pas l'itinéraire du bus, ne fait pas s'arrêter le bus plus rapidement ou n'annule pas la demande d'arrêt initiale.

## Les Modèles d'Idempotence dans les Architectures Logicielles

Différents modèles d'idempotence sont utilisés dans les architectures logicielles. Nous allons discuter de deux modèles populaires ici.

### Conception d'API

Dans les API REST, les méthodes HTTP comme GET, HEAD, PUT et DELETE sont intrinsèquement idempotentes.

* GET : Utilisé pour récupérer des données d'un serveur. Plusieurs requêtes GET vers la même ressource sont sûres et doivent retourner les mêmes données, en supposant qu'aucun changement n'a été apporté à la ressource entre-temps.

* HEAD : Similaire à GET, mais il récupère uniquement les informations d'en-tête d'une ressource. Puisqu'il ne retourne pas de corps, il est intrinsèquement sûr et idempotent.

* PUT : Remplace la représentation actuelle d'une ressource par la charge utile de la requête. Répéter la même donnée vers le même point de terminaison de ressource laissera la ressource dans le même état.

* DELETE : Supprime une ressource. Supprimer la même ressource plusieurs fois donne le même résultat : la ressource est supprimée après la première requête réussie, et les requêtes DELETE suivantes retournent généralement un statut 404 Not Found ou 204 No Content, indiquant qu'il n'y a pas de ressource à supprimer.

Une opération POST n'est pas intrinsèquement idempotente, car elle est généralement utilisée pour créer des ressources. Mais certaines implémentations de POST peuvent être conçues pour être idempotentes.

Un bon exemple de cela est le modèle Post/Redirect/Get, également appelé modèle PRG. Ce modèle est particulièrement utile pour gérer les soumissions de formulaires et peut atténuer les problèmes causés par les utilisateurs qui actualisent ou marquent des pages qui modifient l'état du serveur. Examinons en détail comment cela fonctionne.

#### Comment Rendre une Opération POST Idempotente

Le diagramme de séquence ci-dessous explique comment le modèle PRG fonctionne pour prévenir les commandes en double dans une application web de commerce électronique :

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffdf24083-d54b-4c97-8607-bebe4955fe71_1044x774.png align="left")

*Diagramme de séquence montrant comment le modèle PRG fonctionne pour "convertir" une opération POST en une opération GET idempotente*

1. **Post** : Lorsque l'utilisateur soumet un formulaire pour passer une commande, le navigateur envoie une requête POST au serveur.

2. **Redirect** : Après que le serveur a traité la requête POST (par exemple, passer la commande), il envoie une réponse de redirection au navigateur, généralement avec un code de statut HTTP 303/302, le dirigeant vers une nouvelle URL. Cette URL est généralement une page de confirmation de commande.

3. **Get** : Le navigateur envoie ensuite une requête GET à l'URL fournie par la redirection. L'utilisateur voit la page qui confirme sa commande ou le ramène à un état sûr où aucune commande en double ne peut être créée accidentellement.

L'avantage clé de l'utilisation du modèle PRG est qu'il transforme la requête POST en une requête GET, qui est idempotente. Cela signifie que l'actualisation de la page à la fin du processus ne provoquera pas la soumission de la même commande plus d'une fois, car l'actualisation ne répétera que la requête GET, et non la requête POST initiale qui a soumis la commande.

Ce modèle améliore l'expérience utilisateur en prévenant les erreurs courantes, telles que le double-clic sur un bouton de soumission ou l'actualisation de la page, créant des commandes en double indésirables.

Il rend également l'application plus robuste et conviviale, car les utilisateurs peuvent actualiser en toute sécurité la page de confirmation ou la marquer sans s'inquiéter de la duplication de la commande.

### Systèmes de File d'Attente de Messages

Une file d'attente de messages peut contribuer à rendre un système idempotent en garantissant que même si un message (représentant une requête) est livré plusieurs fois, l'opération qu'il déclenche est exécutée une seule fois, ou son effet est le même peu importe le nombre de fois où il est exécuté.

Cela est crucial dans les systèmes distribués où les défaillances réseau, les plantages système ou d'autres problèmes peuvent conduire à ce que le même message soit traité plusieurs fois.

Examinons un exemple qui implique de faire un paiement. Aucun client ne veut être accidentellement débité deux fois lors d'un achat, donc s'assurer que le système est idempotent est très important.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37b5e26b-6892-48c7-8aa8-eaa0c2a39be5_1784x1530.png align="left")

*Diagramme de séquence montrant comment une file d'attente de messages peut rendre un système idempotent et prévenir les paiements en double*

1. La file d'attente de messages envoie un message au système de paiement pour débiter un compte.

2. Ce message a un ID de Transaction unique. La Base de Données des ID Traités maintient un enregistrement des ID de Transaction qui ont été traités. Le Système de Paiement vérifie l'ID de Transaction par rapport à la Base de Données des ID Traités et vérifie si ce paiement a déjà été traité.

3. Si le message a un ID de transaction dans la Base de Données des ID Traités, il est ignoré et traité comme déjà traité. Le paiement a déjà été effectué et ne doit pas être répété. Le Système de Paiement envoie un accusé de réception (ACK) à la file d'attente pour l'informer que le message a été ignoré. La file d'attente de messages doit savoir que le message a été traité avant de supprimer le message de son côté.

4. Si le message n'a pas d'ID de Transaction dans la base de données des ID Traités, cela signifie que le paiement n'a pas été traité auparavant. Le paiement est donc traité et l'ID de transaction est ajouté à la Base de Données des ID Traités. Idéalement, ces deux étapes doivent être effectuées dans une seule [transaction atomique](https://lightcloud.substack.com/i/140524854/atomicity). Cela empêche un état indésirable où le paiement est traité mais l'ID de Transaction n'est jamais ajouté à la Base de Données des ID Traités en raison d'une défaillance de la base de données, d'un problème réseau ou de toute autre panne.

5. Dans la dernière étape, le Système de Paiement envoie un accusé de réception (ACK) à la file d'attente pour l'informer que le message a été traité avec succès. Cet accusé de réception informe la file d'attente que le message a été reçu, traité avec succès et n'a plus besoin d'être conservé dans la file d'attente pour une livraison future. Cela empêche le message d'être envoyé à nouveau, garantissant que le système est idempotent.

Dans cet exemple, le système garantit l'idempotence en :

* Vérifiant les ID de Transaction pour les nouveaux paiements par rapport à une base de données des paiements déjà effectués

* Envoyant l'accusé de réception à la file d'attente après que le message a été ignoré ou traité par le Système de Paiement. Ainsi, cela garantit que le même message n'est envoyé au Système de Paiement qu'une seule fois.

## Conclusion

L'idempotence résout un problème fondamental : comment gérer les opérations qui, intentionnellement ou par accident, peuvent être répétées ? L'idempotence garantit que, peu importe le nombre de fois où une opération est appliquée, le résultat reste le même après la première application, atténuant les risques associés aux actions répétées.

Le principe sous-jacent de l'idempotence est utilisé dans la conception des objets du quotidien avec lesquels nous interagissons dans le monde physique, des boutons de feux de circulation pour piétons aux boutons d'appel d'ascenseur.

Dans le monde abstrait de l'architecture logicielle, l'idempotence garantit que les opérations répétées ont le même effet que l'exécution de cette opération une seule fois. L'idempotence nous permet de construire des architectures fiables et tolérantes aux pannes.