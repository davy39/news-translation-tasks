---
title: Comment obtenir des arbres JSON faciles à lire avec cette extension Chrome
  gratuite (ou plugin Firefox)
subtitle: ''
author: Fatos Morina
co_authors: []
series: null
date: '2019-08-14T11:29:54.000Z'
originalURL: https://freecodecamp.org/news/untitleeasy-to-read-json-with-this-chrome-firefox-extensiond
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/0_9FUbCPtz2dGrBmIi.png
tags:
- name: chrome extension
  slug: chrome-extension
- name: json
  slug: json
seo_title: Comment obtenir des arbres JSON faciles à lire avec cette extension Chrome
  gratuite (ou plugin Firefox)
seo_desc: 'JSON is a very popular file format. Sometimes we may have a JSON object
  inside a browser tab that we need to read and this can be difficult.

  We may need to go and search for an online tool that turns it into an easy-to-read
  format so we can understan...'
---

[JSON](https://www.json.org/) est un format de fichier très populaire. Parfois, nous pouvons avoir un objet JSON dans un onglet de navigateur que nous devons lire et cela peut être difficile.

Nous devons peut-être aller chercher un outil en ligne qui le transforme en un format facile à lire pour que nous puissions le comprendre.

Maintenant, voici une extension Chrome et Firefox qui fait la mise en forme et rend vos JSON instantanément jolis à l'intérieur de votre navigateur, sans avoir à effectuer de nombreuses étapes inutiles.

Elle prend en charge JSON et JSONP et met en évidence la syntaxe afin que vous puissiez différencier les différents attributs et valeurs en conséquence. Elle offre également la possibilité de réduire les nœuds, des URL cliquables que vous pouvez ouvrir dans de nouveaux onglets, et vous voyez le JSON brut, non formaté.

Elle fonctionne avec n'importe quelle page JSON, quel que soit l'URL que vous avez ouverte. Elle fonctionne également avec des fichiers locaux, après l'avoir activée dans `chrome://extensions`. Vous pouvez inspecter le JSON en tapant `json` dans la console.

Vous pouvez installer l'extension en allant [ici pour Chrome](https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa?hl=en) et [ici pour Firefox](https://addons.mozilla.org/en-US/firefox/addon/basic-json-formatter/) puis la tester, par exemple, en visitant cette [réponse API](https://efa.mvv-muenchen.de/ng/XSLT_DM_REQUEST?outputFormat=JSON&language=en&stateless=1&coordOutputFormat=MRCV&useRealtime=1&zope_command=enquiry&type_dm=stop&name_dm=Zugspitzstra%C3%9Fe&itOptionsActive=1&ptOptionsActive=1&mergeDep=1&useAllStops=1&mode=direct&anyMaxSizeHitList=10000&useAllStops=1).

Voici à quoi cela ressemble, avant la mise en forme :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-134.png align="left")

Maintenant, regardez la belle réponse JSON que vous obtenez avec [JSON Formatter](https://github.com/callumlocke/json-formatter) :

![Image](https://cdn-images-1.medium.com/max/1600/1*c_9u3i-WVKnhGZsd5UZ6Rw.png align="left")

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-135.png align="left")

Voici un conseil pro : Maintenez la touche CTRL (ou CMD sur Mac) enfoncée tout en réduisant un arbre, si vous souhaitez réduire tous ses frères et sœurs également.

C'est un projet open-source, donc vous pouvez consulter son [code source sur GitHub](https://github.com/callumlocke/json-formatter).

Merci d'avoir lu.