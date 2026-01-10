---
title: Comment j'ai créé un bot Python pour se connecter automatiquement à un portail
  captif
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-18T16:45:08.000Z'
originalURL: https://freecodecamp.org/news/how-i-created-a-python-bot-to-automatically-log-into-a-captive-portal-3d4ba04dee9f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4fjLFJXN544emyaBHxpTuw.png
tags:
- name: automation
  slug: automation
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: selenium
  slug: selenium
- name: 'tech '
  slug: tech
seo_title: Comment j'ai créé un bot Python pour se connecter automatiquement à un
  portail captif
seo_desc: 'By Ritvik Khanna

  A step by step Python tutorial to build a login bot


  _Photo by [Unsplash](https://unsplash.com/photos/wbu4q8xk2Kc?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" title="">rawpixel on...'
---

Par Ritvik Khanna

#### Un tutoriel Python étape par étape pour créer un bot de connexion

![Image](https://cdn-media-1.freecodecamp.org/images/1*6yFHxD539Cg3wy8N5UJzfQ.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/wbu4q8xk2Kc?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">rawpixel</a> sur <a href="https://unsplash.com/search/photos/bot?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

De nos jours, Internet n'est pas un privilège, c'est une nécessité. Où que nous allions, nous avons besoin d'une connexion constante à Internet, que ce soit via un réseau Wi-Fi ou des données mobiles.

Imaginez que nous rejoignons une nouvelle université ou une organisation qui nous fournit Internet via le Wi-Fi. L'organisation peut mettre en place une page de connexion très courante pour l'authentification de leurs utilisateurs appelée [**Portail Captif**](https://en.wikipedia.org/wiki/Captive_portal) (également connu sous le nom de **Jardin Clos**).

Un portail captif est utilisé pour plusieurs raisons.

* Ils sont utilisés par les universités et les organisations pour limiter le nombre d'appareils connectés au réseau Wi-Fi à partir d'un compte/personne.
* Ils sont mis en place pour fournir l'accès à des services nécessitant une authentification, un paiement ou d'autres informations d'identification valides sur lesquelles le fournisseur de services et l'utilisateur conviennent de se conformer.

Il existe de nombreuses [raisons](https://ostec.blog/en/perimeter/captive-portal-what-is-it) et [avantages](https://www.teldat.com/blog/en/wi-fi-captive-portal-benefits/) à utiliser un portail captif, mais ce n'est pas le sujet de cet article.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4fjLFJXN544emyaBHxpTuw.png)
_Exemple d'un portail captif_

Mon entreprise avait mis en place un portail captif auquel les utilisateurs devaient se connecter pour pouvoir accéder à Internet. Dès que je me connectais au réseau sans fil, mon navigateur ouvrait automatiquement la page du portail captif et je devais entrer mon nom d'utilisateur et mon mot de passe pour pouvoir accéder à Internet. Mais il y avait un problème.

Bien que la mise en place d'un portail captif soit bonne pour la protection contre l'accès non autorisé à Internet, l'identification du trafic et la gestion des utilisateurs, elle offre une connexion contrôlée à chaque appareil pour garantir que tous les utilisateurs aient un accès adéquat. Un portail captif peut,

* Contrôler le nombre de terminaux par utilisateur
* Contrôler la consommation de bande passante et/ou la vitesse de téléchargement par session
* Restreindre le type de trafic autorisé et même spécifier la durée de délai d'expiration de la session

En raison de ces restrictions, si je mettais mon système en veille ou restais inactif pendant plus de quelques minutes, mon système était déconnecté du réseau. Par conséquent, après avoir dépassé le temps d'inactivité, je devais me reconnecter.

En tant que développeur logiciel ayant besoin d'une connectivité constante et mobile à Internet sur mon système, je devais entrer mon nom d'utilisateur et mon mot de passe encore et encore, ce qui rendait cela très fastidieux.

Et si, après avoir été déconnecté, je pouvais me connecter au portail captif avec un simple clic sur un bouton/icône de mon système ?

Cela devrait être faisable ! Plus besoin d'entrer un nom d'utilisateur puis un mot de passe qui, dans la plupart des cas, doit comporter 8 caractères et au moins une lettre majuscule, etc. Voyons comment nous pouvons faire cela.

#### Mise en œuvre

Même si vous êtes novice en programmation, cela devrait être assez facile. J'ai codé cela en langage de programmation Python. Python peut être téléchargé [ici](https://www.python.org/downloads/), et nous avons également besoin de Selenium qui peut être téléchargé [ici](https://www.seleniumhq.org/download/). Vous pouvez également faire `pip install selenium` (recommandé).

Maintenant, examinons le code.

Après avoir importé les bibliothèques nécessaires, nous devons spécifier les variables suivantes dans le code.

Permettez-moi de vous expliquer cela maintenant,

* Le lien _website_ n'est rien d'autre que le lien de la page de connexion ou le lien du portail captif contre lequel un utilisateur s'authentifierait
* _u_sername_ et _password_ sont ce que vous entrez pour vous connecter
* _element_for_username, element_for_password, element_for_submit_ sont les noms de l'élément dans le code HTML de la page de connexion

Permettez-moi de vous montrer comment les trouver.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NTHs3f2uSSINUKh2wHBgMA.gif)

Comme le montre la figure ci-dessus,

* Ouvrez _Inspecter l'élément_ selon votre navigateur.
* Recherchez l'élément HTML et copiez le nom de la balise d'entrée (dans l'exemple ci-dessus, c'est _user_name_).
* Faites de même pour trouver l'élément HTML pour le _mot de passe_ et le _bouton de soumission_.
* Ces chaînes seront la valeur pour votre _element_for_username, element_for_password, element_for_submit_.

La majeure partie du travail est faite !

> **Note :** Je travaille sur macOS, donc je vais implémenter le bot pour Safari. Pour Chrome et autres, utilisez Chrome via chromedriver.

Copiez ce code avec le reste du code et enregistrez-le en tant que fichier Python (.py). Exécutez le fichier en utilisant `python script.py`. Vous verrez le navigateur ouvrir automatiquement la page de connexion, entrer les détails et les soumettre. Vous n'avez même plus besoin de taper le nom d'utilisateur et le mot de passe. N'est-ce pas cool ?

> **Note :** Le code complet est disponible sur [GitHub](https://github.com/ritvikkhanna09/AutoLoginBot).

#### Utilisation d'Automator dans macOS pour créer une application (facultatif)

![Image](https://cdn-media-1.freecodecamp.org/images/1*GNjUpTXueGtPl3i_2rHmZA.png)

Dans macOS, vous pouvez créer une application qui peut suivre un ensemble spécifique de flux de travail pour toute tâche effectuée de manière répétée.

Dans cette section, je vais expliquer comment transformer le script Python ci-dessus en une application Automator. Cela permettra à l'utilisateur de se connecter au portail captif et de simplement cliquer sur le fichier de l'application Automator.

Maintenant, examinons les étapes pour mettre cela en œuvre :

Étape 1 : Ouvrez **Automator**. Créez un **nouveau service** ou **Fichier** &g**t;** Nouveau **> S**ervice

Étape 2 : Ajoutez une action "**Exécuter un script Shell**", définissez **Shell:** sur **/bin/bash** et **Passer l'entrée:** sur **en tant qu'arguments**. 

Étape 3 : Ajoutez maintenant le code bash comme indiqué ci-dessous. Enregistrez le fichier sur le bureau.

Étape 4 : Cliquez sur le fichier et voilà !

![Image](https://cdn-media-1.freecodecamp.org/images/1*963R-oTqqQ_bTib9IgSvYw.png)

Trouver une solution à un problème aussi simple que de taper quelque chose comme des identifiants de connexion de manière répétée peut être fait facilement. Une fois que vous connaissez l'énoncé du problème, trouver la solution est plus facile. J'espère que cet article vous a donné une idée de comment Selenium et Python fonctionnent et de la facilité de créer un bot Python.