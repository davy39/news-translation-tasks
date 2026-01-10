---
title: CSS Font Family et polices Web Safe expliquées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-15T19:20:00.000Z'
originalURL: https://freecodecamp.org/news/web-safe-fonts
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c93740569d1a4ca32fe.jpg
tags:
- name: fonts
  slug: fonts
- name: toothbrush
  slug: toothbrush
seo_title: CSS Font Family et polices Web Safe expliquées
seo_desc: 'Web Safe Fonts

  Web safe fonts are fonts that are included with most operating systems, the implication
  of such high availability is that a designer can expect typography involving web
  safe fonts to appear exactly as intended to most users. Below are ...'
---

## **Polices Web Safe**

Les polices Web Safe sont des polices incluses avec la plupart des systèmes d'exploitation. Leur haute disponibilité implique qu'un designer peut s'attendre à ce que la typographie utilisant ces polices s'affiche exactement comme prévu pour la plupart des utilisateurs. Ci-dessous se trouvent des listes non exhaustives de certaines polices considérées comme Web Safe au moment de la rédaction, classées par familles de polices génériques CSS.

Polices serif Web Safe :

* Georgia
* Times New Roman

Polices sans-serif Web Safe :

* Arial
* Tahoma
* Trebuchet MS
* Verdana

Polices monospace Web Safe :

* Courier New

Il est important de noter que les piles de polices avec des options de repli, incluant une famille de polices générique, doivent encore être utilisées même si votre design n'utilise que des polices Web Safe. Par exemple :

```css
p {
  font-family: Tahoma, Arial, sans-serif;
}
```

#### **Une note sur les polices Web**

Le fait que certaines polices soient plus sûres que d'autres ne signifie pas que vous devez limiter vos designs à n'utiliser que des polices Web Safe. Les designs modernes avec CSS peuvent également tirer parti des polices Web pour garantir une typographie cohérente sur tous les systèmes d'exploitation.

## Plus d'informations sur les polices :

* [Comment charger correctement les polices Web](https://www.freecodecamp.org/news/web-fonts-in-2018-f191a48367e8/)
* [Superfamilles de polices Google](https://www.freecodecamp.org/news/low-hanging-design-fruit-why-you-should-use-google-font-superfamilies-1dae04b2fc50/)
* [Comment utiliser les polices Google dans votre prochain projet de design](https://www.freecodecamp.org/news/how-to-use-google-fonts-in-your-next-web-design-project-e1ad48f1adfa/)