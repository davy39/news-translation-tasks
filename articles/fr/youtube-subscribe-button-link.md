---
title: 'Bouton d''abonnement YouTube : Comment inciter les gens à s''abonner à votre
  chaîne depuis un lien'
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2020-10-05T17:23:15.000Z'
originalURL: https://freecodecamp.org/news/youtube-subscribe-button-link
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/freeCodeCamp_org_-_YouTube-1.jpg
tags:
- name: how-to
  slug: how-to
- name: social media
  slug: social-media
- name: youtube
  slug: youtube
seo_title: 'Bouton d''abonnement YouTube : Comment inciter les gens à s''abonner à
  votre chaîne depuis un lien'
seo_desc: 'Did you know you can prompt people to subscribe when they visit your channel?

  Here is what this will look like to someone who clicks the link on a laptop or desktop
  computer:


  YouTube will show a Confirm channel subscription message.

  And don''t worry ...'
---

Saviez-vous que vous pouvez inciter les gens à s'abonner lorsqu'ils visitent votre chaîne ?

Voici à quoi cela ressemblera pour quelqu'un qui clique sur le lien depuis un ordinateur portable ou de bureau :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/freeCodeCamp_org_-_YouTube.jpg)
_YouTube affichera un message de confirmation d'abonnement à la chaîne._

Et ne vous inquiétez pas – si quelqu'un est déjà abonné à votre chaîne lorsqu'il clique sur ce lien, il verra simplement votre chaîne normalement, sans le message de confirmation d'abonnement.

## Les deux méthodes pour inciter les gens à s'abonner directement à votre chaîne YouTube

Il existe deux méthodes principales que vous pouvez utiliser pour atteindre cet objectif d'inciter les gens à s'abonner directement à votre chaîne :

1. Un lien d'abonnement YouTube que vous pouvez utiliser partout – y compris sur les sites de réseaux sociaux et les outils de messagerie.
2. Un bouton d'abonnement YouTube que vous pouvez utiliser partout où vous pouvez intégrer du JavaScript, comme sur votre site web personnel.

## Comment créer votre propre lien d'abonnement YouTube

YouTube propose une fonctionnalité où vous pouvez simplement ajouter le paramètre `?sub_confirmation=1` à l'URL de votre chaîne YouTube.

Encore une fois, cela est parfait pour lier votre chaîne YouTube depuis les réseaux sociaux ou un autre endroit où vous n'avez pas la possibilité d'insérer du code pour un bouton d'abonnement propre.

Il existe deux types de chaînes sur YouTube :

1. Chaînes de type "Channel"
2. Chaînes de type "User"

En pratique, il n'y a pas de différence majeure entre ces types de chaînes. Elles utilisent simplement une structure d'URL légèrement différente.

### Comment créer un lien d'abonnement si votre chaîne YouTube est classée comme une "Channel"

Vous pouvez savoir si votre chaîne utilise la structure "channel" en visitant votre chaîne et en vérifiant si l'adresse contient le mot "channel".

Voici un exemple :

```
https://www.youtube.com/channel/freecodecamp
```

Voyez-vous le mot "channel" ici ? Dans ce cas, vous pouvez utiliser cette structure pour votre lien :

```
https://www.youtube.com/channel/<VOTRE_ID_DE_CHAÎNE>?sub_confirmation=1
```

Vous devez simplement remplacer `<VOTRE_ID_DE_CHAÎNE>` dans cette URL par l'ID de votre chaîne, que vous pouvez trouver en allant sur votre chaîne YouTube.

Il s'agira soit d'un nom personnalisé (dans ce cas, `freecodecamp`), soit d'une chaîne de caractères base-64 comme ceci : `UC0syIz79dzjMXIf5VdJ65EA`

Une fois que vous avez ajouté l'ID de votre chaîne à ce lien, vous êtes prêt. Les personnes qui cliquent sur ce lien seront non seulement redirigées vers votre chaîne, mais elles verront également l'invite de confirmation d'abonnement.

### Comment créer un lien d'abonnement si votre chaîne YouTube est classée comme un "User"

Certaines chaînes plus anciennes sont toujours configurées en tant qu'utilisateurs plutôt qu'en tant que chaînes. Vous pouvez savoir si votre chaîne utilise la structure "user" en visitant votre chaîne et en vérifiant si l'adresse contient le mot "user".

Voici un exemple :

```
https://www.youtube.com/user/thenewboston
```

Cette chaîne est configurée en tant qu'utilisateur.

Dans ce cas, vous utiliseriez cette structure :

```
https://www.youtube.com/user/<VOTRE_ID_DE_CHAÎNE>?sub_confirmation=1
```

Vous devez simplement remplacer `<VOTRE_ID_DE_CHAÎNE>` dans cette URL par l'ID de votre chaîne. Il s'agira soit d'un nom personnalisé (dans ce cas, `thenewboston`), soit d'une chaîne de caractères base-64 comme ceci : [`UC0syIz79dzjMXIf5VdJ65EA`](https://www.youtube.com/channel/UC0syIz79dzjMXIf5VdJ65EA)

Une fois que vous avez ajouté l'ID de votre chaîne à ce lien, vous êtes prêt.

## Comment créer votre propre bouton d'abonnement YouTube

Très bien – voici la partie amusante. YouTube vous donne un moyen d'intégrer des boutons d'abonnement directement dans votre site web.

Voici à quoi ressemble l'un de ces boutons :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Configure_a_Button_-_-_YouTube_Subscribe_Button_-_-_Google_Developers.png)
_Ceci est une image statique qui mène à [une invite d'abonnement](https://www.youtube.com/c/freecodecamp?sub_confirmation=1)._

Et voici le code HTML intégrable que vous ajouteriez à votre blog. Notez que ce code importera la bibliothèque JavaScript `platform.js` de Google afin d'afficher dynamiquement le bouton et votre nombre actuel d'abonnés.

```
<script src="https://apis.google.com/js/platform.js"></script>

<div class="g-ytsubscribe" data-channelid="<VOTRE_ID_DE_CHAÎNE>" data-layout="full" data-theme="dark" data-count="default"></div>
```

Vous pouvez intégrer ce code. Assurez-vous de remplacer `<VOTRE_ID_DE_CHAÎNE>` par l'ID de la chaîne que vous voyez lorsque vous visitez votre page.

Si vous avez une URL de chaîne YouTube personnalisée comme `https://www.youtube.com/freecodecamp`, vous pourrez peut-être l'utiliser comme ID de votre chaîne, mais je trouve plus fiable d'utiliser l'ID complet de la chaîne de 24 caractères.

## Comment personnaliser votre bouton d'abonnement YouTube

Il existe deux autres façons de personnaliser votre bouton d'abonnement.

### Comment afficher le nom et le logo de votre chaîne dans votre bouton d'abonnement

Vous pouvez changer `data-layout` pour qu'il soit soit `default`, soit `full` (ce qui affichera le nom de votre chaîne et son icône).

Voici à quoi cela ressemble lorsque vous définissez `data-layout="default"` :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Configure_a_Button_-_-_YouTube_Subscribe_Button_-_-_Google_Developers-1.png)
_Ceci est une image statique qui mènerait à [une invite d'abonnement](https://www.youtube.com/c/freecodecamp?sub_confirmation=1)._

Et voici à quoi cela ressemble lorsque vous définissez `data-layout="full"` :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Configure_a_Button_-_-_YouTube_Subscribe_Button_-_-_Google_Developers.png)
_Ceci est une image statique qui mène à [une invite d'abonnement](https://www.youtube.com/c/freecodecamp?sub_confirmation=1)._

Vous pouvez également définir le thème sur sombre avec `data-theme="dark"`.

Et vous pouvez masquer complètement votre nombre d'abonnés avec `data-count="hidden"`. Si vous n'avez que quelques abonnés, vous pourriez vouloir masquer cela pendant quelques mois pendant que vous construisez une base de mille abonnés ou plus, pour éviter la "preuve sociale négative".

# Pourquoi je recommande les liens d'abonnement YouTube plutôt que les boutons d'abonnement YouTube

Il y a plusieurs raisons pour lesquelles je recommande d'utiliser l'approche par lien plutôt que ces boutons dynamiques.

1. Les bloqueurs de publicités, les pare-feu et les extensions de navigateur peuvent empêcher le bouton de s'afficher correctement ou de fonctionner correctement. Ce bouton implique de charger un fichier JavaScript depuis les CDN de Google, ce qui signifie qu'il ne s'affichera pas en Chine, par exemple, où Google est actuellement bloqué.
2. Il est difficile de contrôler le style de ces boutons, et ils peuvent finir par avoir mauvaise allure sur un appareil mobile.
3. Ces boutons peuvent poser des problèmes d'accessibilité. Le lien, en revanche, n'est qu'un lien, et est facile à utiliser pour les personnes utilisant des lecteurs d'écran ou d'autres outils d'assistance.

Mais Google supporte également ces boutons d'abonnement YouTube, donc c'est à vous de décider si vous souhaitez les utiliser.

## Un outil de personnalisation de bouton d'abonnement YouTube

Google propose un outil officiel pour personnaliser ces boutons d'abonnement YouTube. [Vous pouvez y accéder ici](https://developers.google.com/youtube/youtube_subscribe_button). Notez que vous devrez toujours avoir accès au HTML de la page où vous souhaitez intégrer ces boutons.

Merci d'avoir lu ce guide, et j'espère qu'il vous a aidé à comprendre comment fonctionnent ces liens et boutons d'abonnement YouTube, et comment vous pouvez les utiliser pour inciter davantage de personnes à s'abonner à votre chaîne.

Si vous souhaitez plus de conseils pour devenir un créateur YouTube à succès en général, vous pouvez apprendre de notre organisation à but non lucratif et de ses 5+ années d'expérimentation qui nous ont aidés à devenir la plus grande chaîne de programmation sur YouTube.

Voici notre [manuel YouTube gratuit, qui inclut également un cours vidéo d'1 heure](https://www.freecodecamp.org/news/how-to-start-a-software-youtube-channel/). Nous l'avons conçu en pensant aux créateurs axés sur le logiciel, mais de nombreuses techniques peuvent être appliquées à d'autres domaines. J'espère qu'il sera utile pour vous.

À votre santé.

– Quincy