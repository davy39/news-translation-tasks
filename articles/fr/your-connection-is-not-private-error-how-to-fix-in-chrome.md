---
title: Erreur "Votre connexion n'est pas privée" – Comment la corriger dans Chrome
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-07-07T16:03:17.000Z'
originalURL: https://freecodecamp.org/news/your-connection-is-not-private-error-how-to-fix-in-chrome
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/castle-1290860_1280.jpg
tags:
- name: browser
  slug: browser
- name: Google Chrome
  slug: chrome
- name: privacy
  slug: privacy
- name: SSL
  slug: ssl
seo_title: Erreur "Votre connexion n'est pas privée" – Comment la corriger dans Chrome
seo_desc: 'If you log on to a website and your browser shows the “Your connection
  is not private” error, the browser is trying to warn you to stay off the website.


  In that case, the browser has run a check on the SSL (secure socket layer) certificate
  and found...'
---

Si vous vous connectez à un site web et que votre navigateur affiche l'erreur "Votre connexion n'est pas privée", le navigateur essaie de vous avertir de ne pas accéder au site.
![Annotation-2022-07-06-111823-1](https://www.freecodecamp.org/news/content/images/2022/07/Annotation-2022-07-06-111823-1.png)

Dans ce cas, le navigateur a vérifié le certificat SSL (secure socket layer) et a trouvé un problème avec celui-ci – le SSL pourrait avoir expiré ou n'avoir jamais été installé.

Dans certains cas, le problème pourrait provenir de votre navigateur et non du site web. Ainsi, dans cet article, je vais vous montrer comment corriger l'erreur "Votre connexion n'est pas privée" sur un navigateur Chrome.

## Ce que nous allons couvrir
- [Comment corriger l'erreur "Votre connexion n'est pas privée" sur un navigateur Chrome](#heading-comment-corriger-l-erreur-votre-connexion-n-est-pas-privée-sur-un-navigateur-chrome)
 - [Recharger la page web](#heading-recharger-la-page-web) 
 - [Effacer le cache de Chrome](#heading-effacer-le-cache-de-chrome)
 - [Vérifier que la date et l'heure de votre ordinateur sont correctes](#heading-verifier-que-la-date-et-l-heure-de-votre-ordinateur-sont-correctes)
 - [Désactiver votre antivirus et votre VPN](#heading-desactiver-votre-antivirus-et-votre-vpn)
- [Réflexions finales](#heading-reflexions-finales)

## Comment corriger l'erreur "Votre connexion n'est pas privée" sur un navigateur Chrome


### Recharger la page web

La première chose que je vous conseille de faire est de recharger la page.

Recharger la page web est le vieux truc que tout le monde essaie s'il y a un problème avec cette page web. 

De plus, il est possible que des travaux liés au SSL soient en cours sur le site web, donc si vous attendez un moment et rechargez la page, le problème pourrait disparaître.

Si le rechargement ne résout pas le problème pour vous, passez aux autres solutions de cet article.


### Effacer le cache de Chrome

Les données SSL du site web dans le cache de votre navigateur Chrome pourraient avoir expiré. Ainsi, si vous effacez le cache, l'erreur pourrait disparaître.

Suivez les étapes ci-dessous pour effacer le cache de votre navigateur Chrome :

**Étape 1** : Cliquez sur les 3 points verticaux dans le coin supérieur droit et sélectionnez Paramètres :
![ss10-1](https://www.freecodecamp.org/news/content/images/2022/07/ss10-1.png)

**Étape 2** : Cliquez sur l'onglet "Confidentialité et sécurité" dans la barre latérale gauche et sélectionnez "Effacer les données de navigation" :
![ss11-1](https://www.freecodecamp.org/news/content/images/2022/07/ss11-1.png)

**Étape 3** : Sélectionnez Cache et Cookies, puis cliquez sur "Effacer les données" :
![ss12-1](https://www.freecodecamp.org/news/content/images/2022/07/ss12-1.png)


### Vérifier que la date et l'heure de votre ordinateur sont correctes

Si l'horloge de votre ordinateur est en retard ou en avance, votre navigateur affichera une erreur "Votre connexion n'est pas sécurisée".

De nos jours, le message d'erreur est devenu plus précis dans Chrome :
![Annotation-2022-06-06-072807](https://www.freecodecamp.org/news/content/images/2022/07/Annotation-2022-06-06-072807.png)

Dans ce cas, vous devez régler la date et l'heure de votre ordinateur sur les bonnes valeurs et les rendre automatiques, afin que rien ne les réajuste :
![ss](https://www.freecodecamp.org/news/content/images/2022/07/ss.png)
 

### Désactiver votre antivirus et votre VPN

Certains programmes antivirus avec des fonctionnalités d'analyse SSL peuvent faire en sorte que votre navigateur affiche l'erreur "Votre connexion n'est pas privée" s'ils détectent une irrégularité avec le certificat SSL d'un site web.

Dans le même ordre d'idées, un VPN (réseau privé virtuel) masque votre adresse IP et d'autres informations. Le problème est que la confidentialité qu'un VPN vous offre pourrait avoir un effet négatif sur le SSL de certains sites.

En raison de cela, vous devriez envisager de désactiver votre antivirus et vos programmes VPN, au moins temporairement, pour voir si cela corrige l'erreur.


## Réflexions finales

D'autres correctifs qui pourraient éliminer l'erreur "Votre connexion n'est pas privée" pour vous incluent :
- Essayer d'accéder à la page web en mode navigation privée. Dans Chrome, vous pouvez ouvrir un onglet de navigation privée en appuyant sur `CTRL` + `SHIFT` + `N`.
- Redémarrer votre routeur
- Redémarrer votre ordinateur
- Mettre à jour votre système d'exploitation

Si toutes les solutions échouent, le problème pourrait provenir du site web. Cela signifie qu'il y a un problème avec le certificat SSL du site web. Essayez donc de contacter l'administrateur du site. 

Si vous ne trouvez aucun administrateur à contacter, vous devriez éviter ce site web et vous assurer de ne pas partager d'informations sensibles avec le site.

Si vous êtes administrateur de site et que vos utilisateurs se plaignent de cette erreur, j'ai écrit [un article sur la façon de restaurer le SSL de votre site](https://www.freecodecamp.org/news/an-ssl-error-has-occurred-how-to-fix-certificate-verification-error/#howtofixsslerrorasasiteowner).