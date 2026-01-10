---
title: Une erreur SSL s'est produite – Comment corriger l'erreur de vérification du
  certificat
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-07-06T17:51:46.000Z'
originalURL: https://freecodecamp.org/news/an-ssl-error-has-occurred-how-to-fix-certificate-verification-error
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/ssl.png
tags:
- name: Application Security
  slug: application-security
- name: information security
  slug: information-security
- name: Security
  slug: security
- name: SSL
  slug: ssl
- name: Windows
  slug: windows
seo_title: Une erreur SSL s'est produite – Comment corriger l'erreur de vérification
  du certificat
seo_desc: 'If you’re surfing the net and an SSL error occurs on a website you''re
  trying to visit, your browser will warn you by showing you an error messages or
  signal.

  This error is mostly caused by an expired or bad SSL certificate. It also occurs
  when the br...'
---

Si vous surfez sur le net et qu'une erreur SSL se produit sur un site web que vous essayez de visiter, votre navigateur vous avertira en affichant un message d'erreur ou un signal.

Cette erreur est principalement causée par un certificat SSL expiré ou invalide. Elle se produit également lorsque le navigateur ne peut pas vérifier la légitimité du certificat SSL d'un site web.

Ce message d'erreur pourrait être un géant comme ceci :
![Annotation-2022-07-06-111823](https://www.freecodecamp.org/news/content/images/2022/07/Annotation-2022-07-06-111823.png)

Le navigateur pourrait également vous montrer un signal dans la barre d'adresse comme ceci :
![ss1-1](https://www.freecodecamp.org/news/content/images/2022/07/ss1-1.png)

Dans cet article, je vais vous montrer ce qu'est un certificat SSL. Je vais également vous montrer comment corriger les erreurs SSL en tant que propriétaire de site et en tant qu'utilisateur.

## Ce que nous allons couvrir
- [Qu'est-ce que le SSL et pourquoi est-il utilisé ?](#heading-questce-que-le-ssl-et-pourquoi-estil-utilise)
- [Comment corriger l'erreur SSL en tant que propriétaire de site](#heading-comment-corriger-l-erreur-ssl-en-tant-que-proprietaire-de-site)
 - [Acheter un certificat SSL](#heading-acheter-un-certificat-ssl)
 - [Assurez-vous d'activer le SSL sur votre site web](#heading-assurez-vous-d-activer-le-ssl-sur-votre-site-web)
 - [Si votre site web est hébergé sur GitHub Pages…](#heading-si-votre-site-web-est-heberge-sur-github-pages)
 - [Si votre site web est hébergé sur Netlify…](#heading-si-votre-site-web-est-heberge-sur-netlify)
 - [Si votre site web est un site WordPress…](#heading-si-votre-site-web-est-un-site-wordpress)
 - [Contactez votre fournisseur d'hébergement](#heading-contactez-votre-fournisseur-d-hebergement)
- [Comment corriger l'erreur SSL en tant qu'utilisateur](#heading-comment-corriger-l-erreur-ssl-en-tant-qu-utilisateur)
 - [Assurez-vous que votre date et heure sont correctes](#heading-assurez-vous-que-votre-date-et-heure-sont-correctes)
 - [Effacer les SSL enregistrés sur votre ordinateur](#heading-effacer-les-ssl-enregistres-sur-votre-ordinateur)
 - [Effacer le cache et les cookies de votre navigateur](#heading-effacer-le-cache-et-les-cookies-de-votre-navigateur)
- [Réflexions finales](#heading-reflexions-finales)

## Qu'est-ce que le SSL et pourquoi est-il utilisé ?

SSL signifie "Secure Socket Layer" (couche de sockets sécurisée). Il s'agit de la technologie de sécurité standard internationale pour maintenir la sécurité du partage d'informations entre un site web et ses utilisateurs.

Dans le navigateur Chrome, lorsqu'un site web dispose d'un SSL valide, un cadenas verrouillé est affiché dans la barre d'adresse, indiquant que toute information que l'utilisateur partage avec ce site web est cryptée.
![ss2-1](https://www.freecodecamp.org/news/content/images/2022/07/ss2-1.png)

## Comment corriger l'erreur SSL en tant que propriétaire de site

Si vous êtes propriétaire d'un site et que vos utilisateurs se plaignent que votre site affiche des erreurs SSL, vous pouvez corriger le problème avec l'une des méthodes expliquées ci-dessous :

### Acheter un certificat SSL

Si votre site web n'a pas de certificat SSL installé, tout navigateur moderne utilisé par vos utilisateurs les avertira que votre site n'est pas sécurisé.

Dans ce cas, vous devriez acheter un certificat SSL auprès de l'un des fournisseurs disponibles.

Au fait, vous pouvez acheter un certificat SSL auprès d'entreprises qui vendent des noms de domaine. Vous pouvez également acheter un SSL auprès de [Sectigo](https://sectigo.com/) ou [SSLs](https://www.ssls.com/).

### Assurez-vous d'activer le SSL sur votre site web

Si vous avez acheté et installé un SSL mais que votre site web affiche toujours des erreurs SSL, cela pourrait se produire parce que vous n'avez pas activé le SSL sans le savoir.

### Si votre site web est hébergé sur GitHub Pages…

**Étape 1** : Accédez au dépôt de votre site et cliquez sur Paramètres :
![ss3-1](https://www.freecodecamp.org/news/content/images/2022/07/ss3-1.png)

**Étape 2** : Cliquez sur Pages dans la barre latérale de gauche :
![ss4-1](https://www.freecodecamp.org/news/content/images/2022/07/ss4-1.png)

**Étape 3** : Cochez « Appliquer HTTPS » :
![ss5-1](https://www.freecodecamp.org/news/content/images/2022/07/ss5-1.png)

Cela est requis pour les sites utilisant le domaine par défaut de GitHub (example.github.io).

Même si vous utilisez un domaine personnalisé, assurez-vous que cette case est cochée.

### Si votre site web est hébergé sur Netlify…

**Étape 1** : Cliquez sur le site avec une erreur SSL :
![ss6-1](https://www.freecodecamp.org/news/content/images/2022/07/ss6-1.png)

**Étape 2** : Cliquez sur « Paramètres du site » :
![ss7-1](https://www.freecodecamp.org/news/content/images/2022/07/ss7-1.png)

**Étape 3** : Cliquez sur « Gestion de domaine », puis sur HTTPS dans la barre latérale de gauche. Assurez-vous que le message « Votre site a HTTPS activé » est présent.
![ss8-1](https://www.freecodecamp.org/news/content/images/2022/07/ss8-1.png)

### Si votre site web est un site WordPress…
Si vous avez un site WordPress avec une erreur SSL, installez le [plugin Force SSL](https://wordpress.org/plugins/wp-force-ssl/) sur votre site web.
![ss9-1](https://www.freecodecamp.org/news/content/images/2022/07/ss9-1.png)

### Contactez votre fournisseur d'hébergement

Si toutes les méthodes discutées ci-dessus ne fonctionnent pas pour vous, vous devriez contacter le service client de votre fournisseur d'hébergement.

## Comment corriger l'erreur SSL en tant qu'utilisateur

Si vous visitez un site web et que vous obtenez des erreurs liées au SSL, il y a certaines choses que vous pouvez faire en tant qu'utilisateur. Cela est dû au fait que le problème n'est pas toujours causé par le site web – tant qu'un certificat SSL est installé sur le site web.

### Assurez-vous que votre date et heure sont correctes

Si la date et l'heure de votre ordinateur sont en avance ou en retard, le navigateur pourrait afficher une erreur liée au SSL.

Cela est dû au fait que les SSL ont des dates d'expiration. Ainsi, lorsque la date et l'heure de votre ordinateur sont en retard ou en avance, la vérification que votre navigateur effectue pour voir si le certificat SSL de ce site web est valide échouera.

Dans ce cas, le navigateur vous suggérera de changer votre date et heure.

### Effacer les SSL enregistrés sur votre ordinateur

Effacer les certificats SSL stockés par votre ordinateur peut corriger le problème pour vous.

La prochaine fois que vous visiterez ce site web avec l'erreur SSL, votre navigateur effectuera une nouvelle vérification pour révalider le SSL installé sur ce site web.

Pour effacer les SSL, appuyez sur le bouton Windows de votre clavier, recherchez « Options Internet » et cliquez sur le résultat de recherche Options Internet :
![ss13](https://www.freecodecamp.org/news/content/images/2022/07/ss13.png)

Passez à l'onglet Contenu et cliquez sur « Effacer l'état SSL » :
![ss14](https://www.freecodecamp.org/news/content/images/2022/07/ss14.png)

### Effacer le cache et les cookies de votre navigateur

Les informations SSL d'un site web dans le cache et les cookies de votre navigateur pourraient avoir expiré, donc si vous effacez les deux enregistrements, cela pourrait corriger le problème pour vous.

Pour effacer le cache et les cookies de Chrome, cliquez sur les 3 points verticaux dans le coin supérieur droit et sélectionnez Paramètres :
![ss10](https://www.freecodecamp.org/news/content/images/2022/07/ss10.png)

Passez à l'onglet Confidentialité et sécurité dans la barre latérale de gauche et sélectionnez « Effacer les données de navigation » :
![ss11](https://www.freecodecamp.org/news/content/images/2022/07/ss11.png)

Sélectionnez Cache et Cookies, puis cliquez sur « Effacer les données » :
![ss12](https://www.freecodecamp.org/news/content/images/2022/07/ss12.png)

Si vous utilisez un autre navigateur que Chrome, effacez le cache et les cookies du navigateur.

## Réflexions finales

En tant qu'administrateur ou propriétaire de site web, il est très important de vous assurer que le SSL est installé et fonctionne correctement sur votre site web. Sinon, cela pourrait non seulement affecter votre site web, mais aussi votre entreprise.

Si vous êtes un utilisateur, assurez-vous également que tout site web que vous visitez affiche l'icône de cadenas dans la barre d'adresse. Si ce n'est pas le cas, assurez-vous de ne pas partager d'informations sensibles comme les détails de carte et les mots de passe avec le site web.

Merci d'avoir lu.