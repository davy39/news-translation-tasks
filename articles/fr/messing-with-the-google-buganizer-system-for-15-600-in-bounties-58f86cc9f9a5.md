---
title: Comment j'ai piraté le système de suivi de bugs de Google lui-même pour 15
  600 $ en récompenses
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-30T15:00:09.000Z'
originalURL: https://freecodecamp.org/news/messing-with-the-google-buganizer-system-for-15-600-in-bounties-58f86cc9f9a5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*417vbJu3b_sEe3dOAwkNAg.png
tags:
- name: Google
  slug: google
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Comment j'ai piraté le système de suivi de bugs de Google lui-même pour
  15 600 $ en récompenses
seo_desc: 'By Alex Birsan

  Easy Bugs for Hard Cash

  Have you ever heard of the Google Issue Tracker? Probably not, unless you’re a Google
  employee or a developer who recently reported bugs in Google tools. And neither
  had I, until I noticed my vulnerability repor...'
---

Par Alex Birsan

#### Des bugs faciles pour de l'argent dur

Avez-vous déjà entendu parler du Google Issue Tracker ? Probablement pas, sauf si vous êtes un employé de Google ou un développeur qui a récemment signalé des bugs dans les outils Google. Et moi non plus, jusqu'à ce que je remarque que mes rapports de vulnérabilité étaient maintenant gérés en ouvrant un nouveau fil là-bas, en plus des notifications par email habituelles.

Alors j'ai immédiatement commencé à essayer de le casser.

![Image](https://cdn-media-1.freecodecamp.org/images/5zdrwXUDE3LqKOdzz0Y3CCJLHVd0OvkcuBIc)

Alors, qu'est-ce que ce site exactement ? Selon la documentation, l'Issue Tracker (appelé en interne Buganizer System) est un outil utilisé en interne chez Google pour suivre les bugs et les demandes de fonctionnalités pendant le développement des produits. Il est disponible en dehors de Google pour être utilisé par des utilisateurs publics externes et des partenaires qui doivent collaborer avec les équipes Google sur des projets spécifiques.

En d'autres termes, lorsqu'une personne a un **problème** avec un produit Google, il va dans le **suivi des problèmes**. Cela a du sens, n'est-ce pas ? Nous, en tant qu'utilisateurs externes, ne voyons que la pointe de l'iceberg : un petit ensemble de catégories pré-approuvées, et des problèmes où quelqu'un chez Google a explicitement ajouté un compte externe, comme les **rapports de vulnérabilité**. Mais combien d'informations se cachent sous la surface ?

![Image](https://cdn-media-1.freecodecamp.org/images/CFgfsjB8Gal-3SyKq0vtArRPOVR5xhY659uv)

En observant les identifiants numériques attribués aux derniers fils publics, nous pouvons facilement estimer l'utilisation de cet outil en interne. Il y a environ **2000 à 3000 problèmes par heure** ouverts pendant les heures de travail à Mountain View, et seulement **0,1%** d'entre eux sont publics. Il semble qu'une fuite de données dans ce système aurait un impact assez important. Cassons-le !

### Tentative #1 : Obtenir un compte d'employé Google

L'une des premières choses que j'ai remarquées en découvrant le suivi des problèmes était la possibilité de participer aux discussions en envoyant des emails à une adresse spéciale, qui ressemble à ceci :

**buganizer-system+**_componentID_**+**_issueID_**@google.com**

(dans lequel _componentID_ est un nombre représentant une catégorie, et _issueID_ est un identifiant unique pour le fil auquel vous répondez)

Cela m'a rappelé une découverte récente appelée [le Ticket Trick](https://medium.freecodecamp.org/how-i-hacked-hundreds-of-companies-through-their-helpdesk-b7680ddc2d4c), qui permettait aux pirates d'infiltrer les systèmes de chat des organisations en exploitant ce type de système d'email. Considérant que c'est une adresse email **@google.com**, j'ai essayé de m'inscrire à l'équipe Slack de Google en l'utilisant, et la page de confirmation que j'ai obtenue semblait très prometteuse :

![Image](https://cdn-media-1.freecodecamp.org/images/b0-gtpqorm6i73pfQofHEim3r9PGNVX9IvUH)

Hélas, aucun email de Slack n'est jamais arrivé.

La meilleure chose à laquelle j'ai pu penser ensuite était d'obtenir un compte Google avec une adresse email principale **@google.com**, ce qui, je l'espérais, me donnerait quelques privilèges supplémentaires sur le Buganizer. S'inscrire à un tel compte depuis l'extérieur de Google n'était pas censé être autorisé :

![Image](https://cdn-media-1.freecodecamp.org/images/lGKxtS-uexq7P1jB9294kXADV5wM4a5s9Qgx)

Cependant, j'ai trouvé une méthode pour contourner ce filtre : si je m'inscrivais avec une autre fausse adresse email, mais que je ne confirmais pas le compte en cliquant sur un lien reçu par email, j'étais autorisé à changer mon adresse email sans aucune limitation. En utilisant cette méthode, j'ai changé l'email d'un nouveau compte Google en `**buganizer-system+123123+67111111@google.com**`**.**

Peu après, j'ai reçu l'email de confirmation en tant que message sur la page de problème correspondante :

![Image](https://cdn-media-1.freecodecamp.org/images/VWzwunVDR9leTK7k9wsKr9VUlpkKs4OfneZT)

Bien ! J'ai cliqué sur le lien de confirmation, je me suis connecté sur l'Issue Tracker, et...

![Image](https://cdn-media-1.freecodecamp.org/images/J22G5zmwFpEkMXCuaM5wn76CFlaWUo9NL3y8)

J'ai été redirigé vers la page de connexion d'entreprise. Et non, mes identifiants de compte Google ne fonctionnaient pas là-bas. Dommage.

Néanmoins, ce compte m'a donné beaucoup d'avantages supplémentaires dans d'autres endroits sur Internet, y compris la possibilité de [faire un tour](https://google.ridecell.com/request) (gratuitement, peut-être ?), donc c'était toujours un problème de sécurité qui ouvrait beaucoup de portes aux utilisateurs malveillants.

Accepté : **11 heures** | Récompense : **3 133,7 $** | Priorité : **P1**

### Tentative #2 : Être notifié des tickets internes

Une autre fonctionnalité de l'Issue Tracker qui a attiré mon attention pendant que je me familiarisais avec l'interface est la possibilité de _marquer d'une étoile_ les éléments. _Marquer d'une étoile_ un problème signifie que vous êtes intéressé par le problème discuté et que vous souhaitez recevoir des notifications par email chaque fois que quelqu'un ajoute un commentaire.

![Image](https://cdn-media-1.freecodecamp.org/images/3bUICO2Mvfct8zR3qtOL4Yh0gzStAVnCUDIS)

La chose intéressante que j'ai remarquée à propos de cette fonctionnalité était le manque distinct d'erreurs lors de l'utilisation sur des problèmes auxquels je n'avais pas accès. Les règles de contrôle d'accès ne semblaient jamais être appliquées sur ce point de terminaison, alors je me suis connecté à mon deuxième compte et j'ai essayé de marquer d'une étoile un rapport de vulnérabilité de mon compte principal en remplaçant l'ID du problème dans la requête. J'ai ensuite vu ce message, ce qui signifie que l'action avait réussi :

> 1 personne a marqué ce problème d'une étoile.

Pourrait-il être si facile d'espionner les vulnérabilités ouvertes de Google ? J'ai rapidement posté un commentaire sur le problème pour voir si mon compte d'attaquant fictif serait notifié.

![Image](https://cdn-media-1.freecodecamp.org/images/vSJk6ii1tRc5cn0ljK4tp1yyzfg3j0BbdHlh)

Mais encore une fois, aucun email n'est jamais arrivé.

Pour une raison que je ne peux vraiment pas me rappeler, j'ai décidé de faire quelques tests supplémentaires sur celui-ci. J'ai donc obtenu un ID de problème récent, et extrapolé une plage de quelques milliers d'IDs qui devraient coïncider avec les derniers problèmes dans la base de données. Je les ai ensuite tous marqués d'une étoile.

En quelques minutes, ma boîte de réception ressemblait à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/w9q-a7CF3poG65EDwuRxBZPtzWUMWOwqDtAA)

Ma première pensée en ouvrant la boîte de réception était « Jackpot ! ».

Cependant, après un examen plus approfondi, il n'y avait rien de particulièrement intéressant dans ces fils. Apparemment, je ne pouvais écouter que les conversations liées à la traduction, où les gens débattraient des meilleures façons de transmettre le sens d'une phrase dans différentes langues.

J'ai même envisagé de ne pas signaler cela pendant quelques heures, espérant trouver un moyen d'escalader la gravité. Finalement, j'ai réalisé que l'équipe de sécurité de Google serait probablement intéressée à trouver des méthodes de pivot possibles et des variantes, alors j'ai envoyé les détails.

Accepté : **5 heures** | Récompense : **5 000 $** | Priorité : **P0**

### Tentative #3 : Game over

Lorsque vous visitez l'Issue Tracker en tant qu'utilisateur externe, la plupart de ses fonctionnalités sont supprimées, vous laissant avec des privilèges extrêmement limités. Si vous voulez voir toutes les choses cool que les employés de Google peuvent faire, vous pouvez chercher des points de terminaison API dans les fichiers JavaScript. Certaines de ces fonctions sont complètement désactivées, d'autres sont simplement cachées dans l'interface.

Lors de la conception de cette version limitée du système, quelqu'un a été assez gentil pour laisser une méthode nous permettant de nous retirer de la liste des CC, au cas où nous perdrions de l'intérêt pour un problème ou ne voudrions plus recevoir d'emails à ce sujet. Cela pouvait être réalisé en envoyant une requête POST comme ceci :

```
POST /action/issues/bulk_edit HTTP/1.1
```

```
{   "issueIds":[      67111111,      67111112   ],   "actions":[      {         "fieldName":"ccs",         "value":"test@example.com",         "actionType":"REMOVE"      }   ]}
```

Cependant, j'ai remarqué quelques négligences ici qui ont conduit à un énorme problème :

1. **Contrôle d'accès inapproprié** : Il n'y avait pas de vérification explicite que l'utilisateur actuel avait réellement accès aux problèmes spécifiés dans `issueIds` avant d'essayer d'effectuer l'action donnée.
2. **Échec silencieux** : Si vous fournissiez une adresse email qui n'était pas actuellement dans la liste des CC, le point de terminaison retournerait un message indiquant que l'email avait été supprimé avec succès.
3. **Détails complets du problème dans la réponse** : Si aucune erreur ne survenait pendant l'action, une autre partie du système supposait que l'utilisateur avait les permissions appropriées. Ainsi, chaque détail concernant l'ID de problème donné serait retourné dans le corps de la réponse HTTP.

Je pouvais maintenant voir les détails de chaque problème dans la base de données en remplaçant `issueIds` dans la requête ci-dessus. Bingo !

J'ai seulement essayé de visualiser quelques IDs consécutifs, puis je me suis attaqué depuis un compte sans rapport pour confirmer la gravité de ce problème.

Oui, je pouvais voir les détails des rapports de vulnérabilité, ainsi que tout le reste hébergé sur le Buganizer.

Encore pire, je pouvais exfiltrer des données sur plusieurs tickets en une seule requête, donc la surveillance de toute l'activité interne en temps réel n'aurait probablement pas déclenché de limiteurs de débit.

J'ai rapidement envoyé les détails de l'exploit à Google, et leur équipe de sécurité a désactivé le point de terminaison affecté une heure plus tard. Temps de réponse impressionnant !

Accepté : **1 heure** | Récompense : **7 500 $** | Priorité : **P0**

Lorsque j'ai commencé à chasser cette fuite d'informations, j'ai supposé que ce serait le _Saint Graal_ des bugs de Google, car il divulgue des informations sur tous les autres bugs (par exemple, HackerOne paie un [minimum de 10 000 $](https://hackerone.com/security) pour quelque chose de similaire).

Mais après l'avoir trouvé, j'ai rapidement réalisé que l'impact serait minimisé, car toutes les vulnérabilités dangereuses sont neutralisées dans l'heure de toute façon.

Je suis très heureux de l'argent supplémentaire, et j'ai hâte de trouver des bugs dans d'autres produits Google.