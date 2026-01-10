---
title: Writing OS-specific code in Electron
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
seo_title: null
seo_desc: 'By Maciej Cieślar

  One of the advantages of using Electron is that — since it’s cross-platform — we
  don’t have to worry about the operating system on which our application is going
  to be run.

  However, sometimes we need our code to be OS-specific if, f...'
---

By Maciej Cieślar

One of the advantages of using Electron is that — since it’s cross-platform — we don’t have to worry about the operating system on which our application is going to be run.

However, sometimes we need our code to be OS-specific if, for example, we are going to be using the command console or need to retrieve some information about the system.

Having to write multiple _ifs_ each time we want to have some functionality on a given OS seems like excess work. It quickly obfuscates the code, making it difficult to be understood and analyzed.

In order to keep the code clean and readable, we can create a little helper and remove the _ifs_ and any “OS-related” logic altogether.

### Implementing Platforms

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
  [MAC]: username => `Hi ${username}! You are using Mac.`,
  [WINDOWS]: username => `Hi ${username}! You are using Windows.`,
  [LINUX]: username => `Hi ${username}! You are using Linux.`,
  default: username => `Hi ${username}! You are using something different.`,
});

console.log(whatIsHeUsing('Maciej Cieslar')); // => Hi Maciej Cieslar! You are using Mac.
```

First, we see the _platforms_ object which contains names of all supported operating systems. It is made only for convenience. We can then use _platforms.WINDOWS_ instead of typing _‘WINDOWS’_ each time into our object with handlers we pass to the _byOS_ function.

Next, notice the _platformsNames_ object. The keys are the result of calling [_os.platform()_](https://nodejs.org/api/os.html#os_os_platform)_._ The values are the keys from the _platforms_ object. We simply map it to a more user-friendly name.

For example, when _os.platform()_ returns _win32,_ we map it to _platforms.WINDOWS_ by calling _platformsNames[os.platform()]_.

In _currentPlatform,_ we save the platform that we are using right now, so then we can match it against a given object with handlers.

### Implementing Releases

One might go even further and try to differentiate between releases of a given OS, for example, Windows 7, 8 and 10.

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
    [WIN7]: username => `Hi ${username}! You are using Windows 7.`,
    [WIN8]: username => `Hi ${username}! You are using Windows 8.`,
    [WIN10]: username => `Hi ${username}! You are using Windows 10.`,
  }),
});

console.log(whatWindowsIsHeUsing('Maciej Cieslar')); // => Hi Maciej Cieslar! You are using Windows 7.

```

Now we can use [_os.release()_](https://nodejs.org/api/os.html#os_os_release) to check for the system’s release.

We can split the resulting string and check the Windows version. A complete list can be found [here](https://stackoverflow.com/a/44916050/6569856). As for Linux/Mac, I didn’t really see how that could be useful, so I left it at _releases.ANY_.

In _whatWindowsIsHeUsing_ you can see that we are only checking for different Windows’ releases if we are running the app on Windows.

You can see the code in the [repository](https://github.com/maciejcieslar/os-specific-electron).

Thank you very much for reading! If you have better ideas on how to write OS specific code, share them down below!

If you have any questions or comments feel free to put them in the comment section below or send me a [message](https://www.mcieslar.com/contact).

Check out my [social media](https://www.maciejcieslar.com/about/)!

[Join my newsletter](http://eepurl.com/dAKhxb)!

_Originally published at [www.mcieslar.com](https://www.mcieslar.com/writing-os-specific-code-in-electron) on August 28, 2018._

