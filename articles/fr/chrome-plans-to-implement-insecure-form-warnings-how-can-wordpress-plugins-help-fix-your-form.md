---
title: Comment protéger votre site WordPress avec HTTPS en 5 étapes simples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-11T16:45:13.000Z'
originalURL: https://freecodecamp.org/news/chrome-plans-to-implement-insecure-form-warnings-how-can-wordpress-plugins-help-fix-your-form
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fb6718949c47664ed822a9f.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: WordPress
  slug: wordpress
seo_title: Comment protéger votre site WordPress avec HTTPS en 5 étapes simples
seo_desc: 'By Samuel Griffith

  The internet consists of a network made by different computers around the globe.
  Each website has an address on this network, expressed in syntax, starting with
  an HTTP or HTTPS.

  You may have seen these letters in the address bar o...'
---

Par Samuel Griffith

Internet est composé d'un réseau de différents ordinateurs à travers le monde. Chaque site web possède une adresse sur ce réseau, exprimée en syntaxe, commençant par HTTP ou HTTPS.

Vous avez peut-être vu ces lettres dans la barre d'adresse de votre navigateur web. Mais le point important est que les navigateurs web comme Chrome et Firefox durcissent les mesures contre les sites contenant HTTP ou des protocoles mixtes.

Si vous utilisez WordPress pour construire et héberger votre site web, vous avez peut-être remarqué que certains contenus de la page se chargent fréquemment via une connexion HTTP, provoquant l'apparition d'un avertissement.

Alors, comment vous assurer que votre site WordPress est sécurisé ?

## Qu'a HTTP à voir avec la sécurité du site web ?

HTTP signifie Hypertext Transfer Protocol, simplement compris comme un protocole de partage de données entre le visiteur du site et l'hôte.

HTTP est considéré comme non sécurisé car il est facile pour quiconque surveillant le réseau de voler vos données. À cause de cela, au lieu d'un cadenas vert, votre navigateur web affichera des icônes d'avertissement dans la barre d'adresse, indiquant que le site web n'est pas sécurisé.

HTTPS, en revanche, chiffré les requêtes et les réponses sur un réseau, le rendant ainsi plus sécurisé. Heureusement, vous pouvez facilement sécuriser votre site WordPress et résoudre le problème mentionné ci-dessus en passant à HTTPS en utilisant des plugins fournis par WordPress.

Les étapes suivantes aideront les utilisateurs de WordPress à établir une connexion HTTPS sécurisée pour leur site web.

## Étape 1 : Sauvegardez votre application

Avant d'apporter des modifications à votre application et à votre page, vous devez sauvegarder votre application WordPress.

Il y a de bonnes chances que toute modification apportée via le panneau d'administration cause des dommages irréversibles à vos données. Sauvegarder vos données peut vous aider à les récupérer en toute sécurité plus tard. Et au cas où vous souhaiteriez récupérer une ancienne version de votre site web, vous pouvez le faire également.

Vous pouvez choisir parmi de nombreuses options de sauvegarde. Assurez-vous simplement de considérer les avantages et les inconvénients des systèmes de sauvegarde hors ligne et en ligne avant d'en choisir un.

## Étape 2 : Connectez-vous à votre panneau d'administration WordPress

Pour apporter les modifications nécessaires, vous devez vous connecter à votre panneau d'administration WordPress.

Accédez au panneau d'administration en entrant l'URL de votre site web (www.abc.com) et en ajoutant (/wp-admin) à la fin dans la barre d'adresse. Cela ouvrira un panneau d'administration WordPress.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/wp-dashboard.jpg)
_[Source](https://www.inmotionhosting.com/support/edu/wordpress/logging-into-wordpress-dashboard/)_

Entrez votre nom d'utilisateur et votre mot de passe pour accéder au tableau de bord de votre site web en tant qu'administrateur. La connexion admin vous permet d'apporter des modifications et de construire votre site.

## Étape 3 : Téléchargez le plugin Really Simple SSL

Une fois que vous avez navigué sur le côté gauche de votre tableau de bord, vous devriez voir plusieurs options telles que accueil, pages, mises à jour, et ainsi de suite.

Faites défiler vers le bas pour trouver l'onglet Plugins. Cliquez sur Plugin puis sélectionnez Nouveau Plugin. Cela devrait ouvrir une page avec de nombreuses options de plugins.

Allez à la barre de recherche et tapez "really simple SSL". Vous trouverez un plugin du même nom avec un cadenas comme logo. Sélectionnez l'option installer le plugin.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/d18851ca8b03cceb690a34042c47dfe727bcf6a6.png)
_[Source](https://www.inmotionhosting.com/support/edu/wordpress/how-to-install-wp-really-simple-ssl-plugin/)_

## Étape 4 : Activez le plugin

Après avoir installé le plugin, vous pouvez ouvrir votre site web dans un nouvel onglet pour vérifier si l'icône non sécurisée apparaît dans la barre d'adresse.

Si vous constatez qu'elle n'est toujours pas résolue, retournez à la page des plugins. Là, vous verrez une option pour activer le plugin de force.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/Activate-SSL.png)
_[Source](https://www.inmotionhosting.com/support/edu/wordpress/how-to-install-wp-really-simple-ssl-plugin/)_

Vous pouvez ouvrir un nouvel onglet et visiter votre site web pour voir si le problème est maintenant résolu. Si ce n'est pas le cas, il peut être utile de vérifier si le téléchargement s'est déroulé correctement. Vous pouvez également désinstaller le plugin, redémarrer votre PC et essayer à nouveau.

## Étape 5 : Vérifiez et confirmez que votre site est sécurisé

Pour vous assurer que votre site WordPress est sécurisé, vous devez toujours vérifier et double-vérifier. Ouvrez votre site web et assurez-vous que l'icône de cadenas apparaît après un arrêt correct de votre PC.

De plus, vous pouvez vérifier si le plugin fonctionne depuis un autre appareil. Essayez de demander à un ami ou à un collègue d'ouvrir le site web depuis son ordinateur. Enfin, vérifiez si tous les composants et pages fonctionnent de manière optimale et que rien n'a été altéré sur le site web.

Par-dessus tout, vous devez constamment surveiller si le plugin fonctionne ou non. Les mises à jour du système, les mises à jour de l'application, l'ajout de nouveaux plugins et d'autres problèmes peuvent facilement altérer les fonctions du plugin.

## Conclusion

Le trafic constitue une métrique importante de croissance pour tout site web. Avec une sensibilisation accrue au piratage, aux logiciels malveillants, à la surveillance de masse et à la fraude en ligne, les audiences sont devenues méfiantes à l'égard de tout signe de danger.

Les navigateurs web suivent la tendance de la sécurité étanche pour une plus grande satisfaction client et apportent des modifications pour apaiser ses utilisateurs. En tant que petit poisson dans un vaste océan, il est toujours préférable de nager avec le courant.

De même, en tant que personne gérant un site web, vous devez vous assurer que votre site est sécurisé. Cela protège non seulement votre site web, mais aussi vos clients/audience, offrant une excellente expérience pour les deux parties.