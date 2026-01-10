---
title: Comment trouver une clé de produit Windows 10
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2020-11-10T06:26:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-find-a-windows-10-product-key
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fc8850349c47664ed8290dd.jpg
tags:
- name: Windows
  slug: windows
- name: Windows 10
  slug: windows-10
seo_title: Comment trouver une clé de produit Windows 10
seo_desc: 'If you''re having trouble finding your Windows 10 product key, we''ve got
  you covered.

  In this quick tutorial we''ll go over what a Windows product key is, and I''ll share
  several ways to find the product key on modern Windows machines.

  What''s a Windows ...'
---

Si vous avez des difficultés à trouver votre clé de produit Windows 10, nous sommes là pour vous aider.

Dans ce tutoriel rapide, nous allons expliquer ce qu'est une clé de produit Windows et je vais partager plusieurs méthodes pour trouver la clé de produit sur les machines Windows modernes.

## Qu'est-ce qu'une clé de produit Windows 10 ?

Une clé de produit ou une licence Windows est un code à 25 chiffres utilisé pour activer votre installation de Windows.

Autrefois, pour trouver votre clé de produit Windows, il suffisait de chercher une étiquette quelque part sur la machine.

Généralement, vous pouviez trouver l'étiquette sur le côté d'un PC de bureau ou collée au bas d'un ordinateur portable :

![Photo d'une étiquette de clé de produit Windows 7](https://www.freecodecamp.org/news/content/images/2020/12/windows-7-product-key-sticker.jpg)
_Une étiquette de clé de produit Windows à l'ancienne – [Source](https://answers.microsoft.com/en-us/windows/forum/windows_10-win_licensing/how-to-find-your-windows-product-key/f032f08f-f114-46f6-ab81-b28004dd43a0)_

Ou si vous avez acheté une copie physique de Windows, votre clé de produit était incluse quelque part dans la boîte :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/windows-10-physical-product-key.png)
_Une étiquette de clé de produit Windows 10 - [Source](https://answers.microsoft.com/en-us/windows/forum/windows_10-win_licensing/how-to-find-your-windows-product-key/f032f08f-f114-46f6-ab81-b28004dd43a0)_

De nos jours, si vous achetez une version Windows 10 Famille ou Pro auprès du Microsoft Store ou d'un autre détaillant en ligne comme Amazon, elle inclura une copie numérique de votre clé de produit.

Mais si votre ordinateur est relativement neuf et qu'il est livré avec Windows préinstallé, vous vous demandez peut-être comment trouver votre clé – il n'y a probablement pas d'étiquette sur la machine, et le fabricant de l'ordinateur n'en a probablement pas inclus une dans la boîte.

Que vous ayez installé et activé Windows vous-même, ou qu'il soit préinstallé, votre clé de produit est stockée dans le [BIOS](https://www.freecodecamp.org/news/uefi-vs-bios/). Cela facilite grandement les choses si vous souhaitez un jour réinstaller ou mettre à niveau Windows – il n'y a pas d'étiquette sur la machine qui pourrait être endommagée, et pas de petite étiquette à perdre.

Néanmoins, il arrive que vous ayez besoin de votre clé de produit, par exemple si vous souhaitez transférer une licence Windows Famille ou Pro vers une autre machine.

Quelle que soit la raison, voici quelques méthodes pour obtenir votre clé de produit Windows 10.

## Comment obtenir votre clé de produit Windows 10 avec l'invite de commandes

Si vous souhaitez obtenir votre clé de produit à partir de Windows, le moyen le plus simple est de le faire via l'invite de commandes Windows.

Tout d'abord, appuyez sur la touche Windows, recherchez "cmd" et cliquez sur "Exécuter en tant qu'administrateur" :

![Capture d'écran de l'ouverture de l'invite de commandes en tant qu'administrateur](https://www.freecodecamp.org/news/content/images/2020/12/open-admin-command-prompt.jpg)

Ensuite, exécutez la commande suivante :

```
wmic path softwarelicensingservice get OA3xOriginalProductKey
```

Après cela, vous verrez votre clé de produit Windows 10 :

![Sortie de la commande wmic mentionnée ci-dessus](https://www.freecodecamp.org/news/content/images/2020/12/wmic-output.jpg)

Alternativement, vous pouvez exécuter cette commande dans le terminal de l'invite de commandes :

```
powershell "(Get-WmiObject -query ‘select * from SoftwareLicensingService’).OA3xOriginalProductKey"
```

![Sortie de la commande powershell mentionnée ci-dessus](https://www.freecodecamp.org/news/content/images/2020/12/powershell-output.jpg)

Ces deux commandes tentent de lire votre clé de produit Windows à partir de ce que l'on appelle le marqueur BIOS OA3. En d'autres termes, elles peuvent ne fonctionner que si Windows était préinstallé, et non si vous avez construit la machine vous-même et installé/activé Windows.

Si votre clé de produit n'est pas enregistrée dans votre BIOS/UEFI pour une raison quelconque, ces commandes généreront soit une erreur, soit retourneront une chaîne vide. Dans ce cas, ou si vous préférez une interface graphique, essayez la méthode suivante.

## Comment obtenir votre clé de produit Windows 10 avec un programme tiers

Il existe quelques outils comme [Belarc Advisor](https://www.belarc.com/products_belarc_advisor) ou [Magical Jelly Bean KeyFinder](https://www.magicaljellybean.com/keyfinder/) qui peuvent détecter votre clé de produit Windows.

Nous allons utiliser Magical Jelly Bean KeyFinder pour ce tutoriel parce que, eh bien – allez, ce nom, non ?

Tout ce que vous avez à faire est de télécharger et d'installer Magical Jelly Bean KeyFinder. Ensuite, ouvrez le programme KeyFinder pour voir votre clé de produit :

![Capture d'écran de la clé de produit Windows dans Magical Jellybean KeyFinder](https://www.freecodecamp.org/news/content/images/2020/12/magical-jellybean-keyfinder.jpg)

Une fois que vous avez copié votre clé de produit quelque part en sécurité, n'hésitez pas à désinstaller Magical Jelly Bean KeyFinder.

Voici donc quelques méthodes rapides pour trouver votre clé de produit Windows 10.

L'une de ces méthodes ou programmes a-t-elle fonctionné pour vous ? Avez-vous trouvé une autre façon d'obtenir votre clé de produit ? Faites-le moi savoir sur [Twitter](https://twitter.com/home).