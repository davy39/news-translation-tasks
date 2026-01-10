---
title: Écrire du code spécifique au système d'exploitation dans Electron
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-28T17:38:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-os-specific-code-in-electron-bf6379c62ff6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*285GZjmJQbn-VF6J-qKD3A.jpeg
tags:
- name: Electron
  slug: electron
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Écrire du code spécifique au système d'exploitation dans Electron
seo_desc: 'By Maciej Cieślar

  One of the advantages of using Electron is that — since it’s cross-platform — we
  don’t have to worry about the operating system on which our application is going
  to be run.

  However, sometimes we need our code to be OS-specific if, f...'
---

Par Maciej Cieślar

L'un des avantages de l'utilisation d'Electron est que — puisque c'est multiplateforme — nous n'avons pas à nous soucier du système d'exploitation sur lequel notre application va être exécutée.

Cependant, parfois nous avons besoin que notre code soit spécifique au système d'exploitation si, par exemple, nous allons utiliser la console de commande ou devons récupérer certaines informations sur le système.

Devoir écrire plusieurs _ifs_ chaque fois que nous voulons avoir une certaine fonctionnalité sur un système d'exploitation donné semble être un travail excessif. Cela obscurcit rapidement le code, le rendant difficile à comprendre et à analyser.

Afin de garder le code propre et lisible, nous pouvons créer un petit helper et supprimer les _ifs_ et toute logique « liée au système d'exploitation ».

### Implémentation des Plateformes

```javascript
const os = require('os');

const platforms = {
  WINDOWS: 'WINDOWS',
  MAC: 'MAC',
  LINUX: 'LINUX',
  SUN: 'SUN',
  OPENBSD: 'OPENBSD',
  ANDROID: 'ANDROID',
  AIX: 'AIX',
};

const platformsNames = {
  win32: platforms.WINDOWS,
  darwin: platforms.MAC,
  linux: platforms.LINUX,
  sunos: platforms.SUN,
  openbsd: platforms.OPENBSD,
  android: platforms.ANDROID,
  aix: platforms.AIX,
};

const currentPlatform = platformsNames[os.platform()];

const findHandlerOrDefault = (handlerName, dictionary) => {
  const handler = dictionary[handlerName];

  if (handler) {
    return handler;
  }

  if (dictionary.default) {
    return dictionary.default;
  }

  return () => null;
};

const byOS = findHandlerOrDefault.bind(null, currentPlatform);

// usage
const whatIsHeUsing = byOS({
  [MAC]: username => `Salut ${username}! Tu utilises Mac.`,
  [WINDOWS]: username => `Salut ${username}! Tu utilises Windows.`,
  [LINUX]: username => `Salut ${username}! Tu utilises Linux.`,
  default: username => `Salut ${username}! Tu utilises quelque chose de différent.`,
});

console.log(whatIsHeUsing('Maciej Cieslar')); // => Salut Maciej Cieslar! Tu utilises Mac.
```

Tout d'abord, nous voyons l'objet _platforms_ qui contient les noms de tous les systèmes d'exploitation supportés. Il est fait seulement pour la commodité. Nous pouvons ensuite utiliser _platforms.WINDOWS_ au lieu de taper _'WINDOWS'_ chaque fois dans notre objet avec les gestionnaires que nous passons à la fonction _byOS_.

Ensuite, remarquez l'objet _platformsNames_. Les clés sont le résultat de l'appel de [_os.platform()_](https://nodejs.org/api/os.html#os_os_platform). Les valeurs sont les clés de l'objet _platforms_. Nous le mappons simplement à un nom plus convivial.

Par exemple, lorsque _os.platform()_ retourne _win32_, nous le mappons à _platforms.WINDOWS_ en appelant _platformsNames[os.platform()]_.

Dans _currentPlatform_, nous sauvegardons la plateforme que nous utilisons actuellement, afin de pouvoir la faire correspondre à un objet donné avec des gestionnaires.

### Implémentation des Versions

On peut aller encore plus loin et essayer de différencier les versions d'un système d'exploitation donné, par exemple, Windows 7, 8 et 10.

```javascript
const os = require('os');

const releaseTest = {
  [platforms.WINDOWS]: (version) => {
    const [majorVersion, minorVersion] = version.split('.');

    // Windows 10 (10,0)
    if (majorVersion === '10') {
      return releases.WIN10;
    }

    // Windows 8.1 (6,3)
    // Windows 8 (6,2)
    // Windows 7 (6,1)
    if (majorVersion === '6') {
      if (minorVersion === '3' || minorVersion === '2') {
        return releases.WIN8;
      }

      return releases.WIN7;
    }

    return releases.WIN7;
  },
  [platforms.MAC]: () => releases.ANY,
  [platforms.LINUX]: () => releases.ANY,
};

const currentRelease = releaseTest[currentPlatform](os.release());

const byRelease = findHandlerOrDefault.bind(null, currentRelease);

// usage
const whatWindowsIsHeUsing = byOS({
  [WINDOWS]: byRelease({
    [WIN7]: username => `Salut ${username}! Tu utilises Windows 7.`,
    [WIN8]: username => `Salut ${username}! Tu utilises Windows 8.`,
    [WIN10]: username => `Salut ${username}! Tu utilises Windows 10.`,
  }),
});

console.log(whatWindowsIsHeUsing('Maciej Cieslar')); // => Salut Maciej Cieslar! Tu utilises Windows 7.

```

Maintenant, nous pouvons utiliser [_os.release()_](https://nodejs.org/api/os.html#os_os_release) pour vérifier la version du système.

Nous pouvons diviser la chaîne résultante et vérifier la version de Windows. Une liste complète peut être trouvée [ici](https://stackoverflow.com/a/44916050/6569856). En ce qui concerne Linux/Mac, je n'ai pas vraiment vu comment cela pourrait être utile, alors je l'ai laissé à _releases.ANY_.

Dans _whatWindowsIsHeUsing_, vous pouvez voir que nous vérifions uniquement les différentes versions de Windows si nous exécutons l'application sur Windows.

Vous pouvez voir le code dans le [dépôt](https://github.com/maciejcieslar/os-specific-electron).

Merci beaucoup d'avoir lu ! Si vous avez de meilleures idées sur la façon d'écrire du code spécifique au système d'exploitation, partagez-les ci-dessous !

Si vous avez des questions ou des commentaires, n'hésitez pas à les mettre dans la section des commentaires ci-dessous ou envoyez-moi un [message](https://www.mcieslar.com/contact).

Consultez mes [réseaux sociaux](https://www.maciejcieslar.com/about/) !

[Rejoignez ma newsletter](http://eepurl.com/dAKhxb) !

_Publié à l'origine sur [www.mcieslar.com](https://www.mcieslar.com/writing-os-specific-code-in-electron) le 28 août 2018._