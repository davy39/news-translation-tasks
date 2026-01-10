---
title: Comment faire en sorte que GitLab exécute des tâches périodiques pour vous
  en moins d'une minute
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-06T00:15:49.000Z'
originalURL: https://freecodecamp.org/news/56-seconds-to-get-gitlab-to-do-periodic-jobs-for-you-6a731b977559
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HHVkCUSmaGkFPTx06jjZKw.png
tags:
- name: Bitcoin
  slug: bitcoin
- name: GitLab
  slug: gitlab
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment faire en sorte que GitLab exécute des tâches périodiques pour vous
  en moins d'une minute
seo_desc: 'By Moe Ibrahim

  What would technology be without a computer doing periodic work?

  Whether it’s your phone constantly checking your inbox for you, or getting timely
  alerts for weather or flight delays.

  What about a bitcoin vs Canadian dollar price servi...'
---

Par Moe Ibrahim

Que serait la technologie sans un ordinateur effectuant un travail périodique ?

Qu'il s'agisse de votre téléphone vérifiant constamment votre boîte de réception, ou d'alertes opportunes pour la météo ou les retards de vol.

Et un service de prix du bitcoin contre le dollar canadien, en seulement 56 secondes ? Pas de _IFTTT_, pas de _Zapier_, mais pas non plus de langages de programmation — et pas de frameworks, pas de configuration de serveur ou de docker, pas de Raspberry Pi, pas d'AWS et pas de tests !

Pour rendre l'exemple aussi universel que possible, nous n'utiliserons que 2 lignes de commande :

* une pour obtenir le prix du bitcoin à partir d'une API
* et une autre pour le publier sur un autre service.

Bien sûr, vous pouvez rendre cela plus utile en publiant le prix sur Twitter, Twilio, Telegram, Slack, etc. Mais ici, nous le publierons simplement sur putsreq.com afin de pouvoir inspecter la requête POST.

Ensuite, nous utiliserons GitLab-CI pour planifier son exécution tous les jours.

> **Niveau** : Tous niveaux

> **Prérequis** : N'importe quel navigateur web

Commençons :

1. **Créez un compte gratuit** sur [gitlab.com](https://gitlab.com/users/sign_in) (20 secondes)

2. **Créez un nouveau projet** : Cliquez sur le bouton **_Nouveau projet_** pour créer un nouveau dépôt, et dans le champ de nom, tapez _periodic-job_ ou un autre nom. (9 secondes)

![Image](https://cdn-media-1.freecodecamp.org/images/erHlPeiJTmeTnQ4GoFSMtoYLR5V0zseO60H8)

Ensuite, enregistrez-le en cliquant sur **_Créer le projet_** (1 seconde).

![Image](https://cdn-media-1.freecodecamp.org/images/bzyB3KG6wmQ9Jc01n1FhAdyF6BBhCjC9pATv)

3. **Créez un fichier .gitlab-ci.yml dans ce nouveau projet** : Cliquez sur **_Nouveau fichier_**, copiez et collez le snippet suivant dans le fichier .gitlab-ci.yml, puis cliquez sur enregistrer (5 secondes)

![Image](https://cdn-media-1.freecodecamp.org/images/ojeKxdcQUHLAGUO0y8g517nuss9rsKANxpt-)

![Image](https://cdn-media-1.freecodecamp.org/images/sFPB53USK5EYEvXza-ZyruSj0c9Qp3fx5-1R)

```
test:
```

```
 script:
```

```
 - btc=$(curl https://min-api.cryptocompare.com/data/price?fsym=BTC\&tsyms=CAD)
```

```
- curl -i -X POST https://putsreq.com/wkDdMQWhaOyalisaIe49 — data 'price=CA$ "${btc//[0-9\.]/}"'
```

Ce sont essentiellement deux commandes simples. Ici, nous pouvons aller plus loin et ajouter

[_if [ $btc -ge 15000 -a $btc -lt 7000 ]; then_](https://hackernoon.com/71-seconds-to-build-your-free-custom-webhook-illustrated-step-by-step-7a09b9e240ba)

des conditions, ou même exécuter un fichier de script bash complet, mais gardons cela simple.

Cliquez sur le bouton **_Valider les modifications_**, et cela déclenchera la construction et l'exécution.

4. **Planifiez-le pour qu'il s'exécute tous les jours** : cliquez sur l'icône CI/CD pour développer le menu, et sélectionnez Planifications pour configurer un nom et un minuteur pour déclencher votre tâche périodique. (11 secondes)

![Image](https://cdn-media-1.freecodecamp.org/images/LPe0diYgDp3FtDob-daYQgz9yQp3NIbpcaB8)

![Image](https://cdn-media-1.freecodecamp.org/images/myy9E9YueotL6uCnQzIj64S7WvNZgH0nSvI9)
_cliquez sur le bouton **Nouvelle planification**_

![Image](https://cdn-media-1.freecodecamp.org/images/hORLN61TKEGqsCLm4Dus6l0mC0hEp1kDxc7i)
_Tapez un nom pour la nouvelle planification **daily-bitcoin-price-job**, sélectionnez pour l'exécuter quotidiennement puis cliquez sur **Enregistrer**_

![Image](https://cdn-media-1.freecodecamp.org/images/2dK2LU1YHfEwHK3Mhzs82VpHdR3uXncbyG-L)
_Votre tâche planifiée a été enregistrée_

5. Félicitations ! Vous avez terminé. Allez sur [ce lien dans putsreq.com](https://putsreq.com/wkDdMQWhaOyalisaIe49/inspect) pour le voir en action. (10 secondes)

![Image](https://cdn-media-1.freecodecamp.org/images/Yhx54rH7S8jocMDTd8NB0F6-RwySKIoDLT5Y)

Cette tâche s'exécutera tous les jours tant que vos 2000 minutes de construction gratuites par mois ne seront pas épuisées.

Nous n'avons même pas effleuré la surface de ce que nous pouvons faire avec GitLab-CI — pensez simplement à toutes les possibilités de l'utiliser pour créer des webhooks ou [le connecter à IFTTT](https://medium.com/@YYC_Ninja/99-seconds-to-make-bitcoin-call-your-phone-number-a8cbd9740f76) et Zapier, qui à leur tour le connecteraient à des centaines de services.

Dans [l'article suivant](https://medium.com/@YYC_Ninja/71-seconds-to-build-your-free-custom-webhook-illustrated-step-by-step-7a09b9e240ba), nous passerons en revue ce que nous venons de faire, et comment nous pouvons passer à la vitesse supérieure et créer un webhook et l'utiliser pour publier sur les réseaux sociaux.

Vous pouvez trouver [le code exemple ici](https://gitlab.com/ninjayoto/my-periodic-jobs/tree/master), et vous pouvez lire [les journaux de construction ici](https://gitlab.com/ninjayoto/my-periodic-jobs/-/jobs).