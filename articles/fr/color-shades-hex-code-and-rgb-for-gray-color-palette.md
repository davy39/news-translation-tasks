---
title: Nuances de gris – Code Hex et RGB pour la palette de couleurs grises
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-11-24T23:47:39.000Z'
originalURL: https://freecodecamp.org/news/color-shades-hex-code-and-rgb-for-gray-color-palette
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/russn_fckr-krV5aS4jDjA-unsplash.jpg
tags:
- name: colors
  slug: colors
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Nuances de gris – Code Hex et RGB pour la palette de couleurs grises
seo_desc: 'Colors play an integral role in how usable and accessible your web design
  projects are.

  At times, they can even make or break a project.

  Having a color palette comprised of different shades and hues of a specific color
  can be really helpful. It helps...'
---

Les couleurs jouent un rôle intégral dans l'utilisabilité et l'accessibilité de vos projets de design web.

Parfois, elles peuvent même faire ou défaire un projet.

Avoir une palette de couleurs composée de différentes nuances et teintes d'une couleur spécifique peut être vraiment utile. Cela vous aide à visualiser comment vous pouvez combiner les couleurs que vous souhaitez ajouter à vos designs pour créer un effet harmonieux.

Cet article passe brièvement en revue comment ajouter des couleurs en HTML et montre un tableau avec différentes teintes de la couleur grise.

Si vous êtes intéressé uniquement par la visualisation du tableau avec les différentes nuances de gris, [voici le lien vers celui-ci](#tableau).

## Comment écrire des couleurs en HTML

HTML (ou HyperText Markup Language) vous permet d'ajouter différents contenus à une page et de créer une structure.

Les titres, paragraphes, images et liens que vous voyez sur une page web sont tous du code HTML.

Tout le code HTML est écrit dans son propre fichier. Ce fichier a une extension `.html`.

Lorsque vous souhaitez styliser le contenu que vous avez ajouté avec HTML, vous utilisez CSS (ou Cascading Style Sheets).

Il est considéré comme une bonne pratique de garder le contenu et les styles séparés, et d'écrire le code HTML et CSS dans des fichiers différents. C'est ce qu'on appelle la *séparation des préoccupations*.

Ainsi, vous ajouterez votre code CSS dans un fichier avec l'extension `.css`.

Pour changer la couleur du texte, ou la couleur de premier plan des éléments, vous utilisez la propriété `color`.

Lorsque vous souhaitez changer la couleur de fond d'un élément, vous utilisez la propriété `background-color`.

### Codes Hex

Il existe plusieurs options parmi lesquelles vous pouvez choisir pour ajouter la couleur que vous souhaitez.

Certaines de ces options consistent à utiliser le nom de la couleur, le code HEX ou la valeur RGB qui correspond à une couleur spécifique.

Les codes HEX sont des caractères alphanumériques.

Un chiffre hexadécimal peut être l'une des 16 valeurs possibles, allant de 0 à 9 et de a à f.

Les codes sont précédés d'un `#`, comme par exemple : `#ffffff`, qui est la couleur blanche.

### Couleurs RGB

Les valeurs de couleur RGB sont parmi les modèles de couleurs les plus populaires et les plus largement utilisés.

Chaque couleur est une combinaison de Rouge, Vert et Bleu, chaque couleur allant de 0 (le plus bas) à 255 (le plus haut).

La syntaxe générale ressemble à ceci : `rgb(rouge, vert, bleu)`, comme dans cet exemple : `rgb(0, 0, 255)`.

Parce que les nombres pour les places Rouge et Vert sont 0 (ce qui signifie qu'il n'y a pas de couleur là), et que le nombre le plus élevé est la place Bleu, cela signifie que la couleur est un Bleu pur.

Voici un exemple utilisant les trois pour changer la couleur du texte d'un paragraphe en rouge.

Les trois règles auront exactement le même résultat visuellement :

```css
/* utilisant le nom de la couleur */
p {
color: red;
}

/* utilisant le code HEX pour le rouge */
p {
color:	#FF0000;
}

/* utilisant la valeur RGB pour le rouge */
p {
color: rgb(255,0,0);
}
```

Vous pouvez en apprendre plus sur les [codes HEX ici](https://www.freecodecamp.org/news/how-hex-code-colors-work-how-to-choose-colors-without-a-color-picker/) et les [couleurs RGB ici](https://www.freecodecamp.org/news/rgb-color-html-and-css-guide/).

## La palette de couleurs grises <a name="tableau"></a>

Ci-dessous se trouve un tableau avec un large spectre de certaines des nuances de gris reconnues en HTML, allant des plus foncées aux plus claires, avec leurs codes HEX et valeurs RGB respectifs.

Parcourez et choisissez n'importe quelle couleur à utiliser dans votre prochain projet de design web.

<table class="ws-table-all notranslate" >
<tr>
<th>Nuances de gris</th>
<th>Codes HEX</th>
<th>Valeurs RGB</th>
</tr>
    
    <tr>
    <td style="background-color:#111111; background-image: none;"></td>
    <td>#111111</td>
    <td>rgb(17, 17, 17)</td>
</tr>
    
    
    <tr>
    <td style="background-color:#121212; background-image: none;"></td>
    <td>#121212</td>
    <td>rgb(18, 18, 18)</td>
</tr>
    
    <tr>
    <td style="background-color:#161618; background-image: none;"></td>
    <td>#161618</td>
    <td>rgb(22, 22, 24)</td>
</tr>
    
    <tr>
    <td style="background-color:#181818; background-image: none;"></td>
    <td>#181818</td>
    <td>rgb(24, 24, 24)</td>
</tr>
    
    <tr>
    <td style="background-color:#212121; background-image: none;"></td>
    <td>#212121</td>
    <td>rgb(33, 33, 33)</td>
</tr>
    
    <tr>
    <td style="background-color:#212124; background-image: none;"></td>
    <td>#212124</td>
    <td>rgb(33, 33, 36)</td>
</tr>
    
    <tr>
    <td style="background-color:#242526; background-image: none;"></td>
    <td>#242526</td>
    <td>rgb(36, 37, 38)</td>
</tr>
    
    <tr>
    <td style="background-color:#282828; background-image: none;"></td>
    <td>#282828</td>
    <td>rgb(40, 40, 40)</td>
</tr>
    
    <tr>
    <td style="background-color:#2F4F4F; background-image: none;"></td>
    <td>#2F4F4F</td>
    <td>rgb(47,79,79)</td>
</tr>
    
    <tr>
    <td style="background-color:#333333; background-image: none;"></td>
    <td>#333333</td>
    <td>rgb(51, 51, 51)</td>
</tr>
    
    <tr>
    <td style="background-color:#36454F; background-image: none;"></td>
    <td>#36454F</td>
    <td>rgb(54, 69, 79)</td>
</tr>
    
    <tr>
    <td style="background-color:#3A3B3C; background-image: none;"></td>
    <td>#3A3B3C</td>
    <td>rgb(58, 59, 60)</td>
</tr>
    
<tr>
    <td style="background-color:#3B3B3B; background-image: none;"></td>
    <td>#3B3B3B</td>
    <td>rgb(59, 59, 59)</td>
</tr>
    
    <tr>
    <td style="background-color:#3D3D3D; background-image: none;"></td>
    <td>#3D3D3D</td>
    <td>rgb(61, 61, 61)</td>
</tr>
    
     <tr>
    <td style="background-color:#404040; background-image: none;"></td>
    <td>#404040</td>
    <td>rgb(64, 64, 64)</td>
</tr>
    
    <tr>
    <td style="background-color:#494848; background-image: none;"></td>
    <td>#494848</td>
    <td>rgb(73, 72, 72)</td>
</tr>

<tr>
    <td style="background-color:#525252; background-image: none;"></td>
    <td>#525252</td>
    <td>rgb(82, 82, 82)</td>
</tr>
    
    <tr>
    <td style="background-color:#555555; background-image: none;"></td>
    <td>#555555</td>
    <td>rgb(85, 85, 85)</td>
</tr>
    
     <tr>
    <td style="background-color:#6082B6; background-image: none;"></td>
    <td>#6082B6</td>
    <td>rgb(96, 130, 182)</td>
</tr>
    
    <tr>
    <td style="background-color:#616161; background-image: none;"></td>
    <td>#616161</td>
    <td>rgb(97, 97, 97)</td>
</tr>
    
    
    <tr>
    <td style="background-color:#636363; background-image: none;"></td>
    <td>#636363</td>
    <td>rgb(99, 99, 99)</td>
</tr>

 <tr>
    <td style="background-color:#6D6D64; background-image: none;"></td>
    <td>#6D6D64</td>
    <td>rgb(109, 109, 100)</td>
</tr>
    
    
 <tr>
    <td style="background-color:#696969; background-image: none;"></td>
    <td>#696969</td>
    <td>rgb(105, 105, 105)</td>
</tr>
    
    <tr>
    <td style="background-color:#708090; background-image: none;"></td>
    <td>#708090</td>
    <td>rgb(112, 128, 144)</td>
</tr>
    
    <tr>
    <td style="background-color:#71797E; background-image: none;"></td>
    <td>#71797E</td>
    <td>rgb(113, 121, 126)</td>
</tr>
    
    <tr>
    <td style="background-color:#7393B3; background-image: none;"></td>
    <td>#7393B3</td>
    <td>rgb(115, 147, 179)</td>
</tr>
    
    <tr>
    <td style="background-color:#777777; background-image: none;"></td>
    <td>#777777</td>
    <td>rgb(119, 119, 119)</td>
</tr>
    
    <tr>
    <td style="background-color:#778899; background-image: none;"></td>
    <td>#778899</td>
    <td>rgb(119,136,153</td>
</tr>
    
   <tr>
    <td style="background-color:#7E7E7E; background-image: none;"></td>
    <td>#7E7E7E</td>
    <td>rgb(126, 126, 126)</td>
</tr> 
    
 <tr>
    <td style="background-color:#808080; background-image: none;"></td>
    <td>#808080</td>
    <td>rgb(128, 128, 128)</td>
</tr>
    
    
    <tr>
    <td style="background-color:#818181; background-image: none;"></td>
    <td>#818181</td>
    <td>rgb(129, 129, 129)</td>
</tr>
    
    <tr>
    <td style="background-color:#818589; background-image: none;"></td>
    <td>#818589</td>
    <td>rgb(129, 133, 137)</td>
</tr>
    
    <tr>
    <td style="background-color:#848884; background-image: none;"></td>
    <td>#848884</td>
    <td>rgb(132, 136, 132)</td>
</tr>
    
    <tr>
    <td style="background-color:#888888; background-image: none;"></td>
    <td>#888888</td>
    <td>rgb(136, 136, 136)</td>
</tr>
    
    <tr>
    <td style="background-color:#899499; background-image: none;"></td>
    <td>#899499</td>
    <td>rgb(137, 148, 153)</td>
</tr>
    
    <tr>
    <td style="background-color:#8A9A5B; background-image: none;"></td>
    <td>#8A9A5B</td>
    <td>rgb(138, 154, 91)</td>
</tr>
    
    <tr>
    <td style="background-color:#8B8B81; background-image: none;"></td>
    <td>#8B8B81</td>
    <td>rgb(139, 139, 129)</td>
</tr>
    
    <tr>
    <td style="background-color:#8C8C8C; background-image: none;"></td>
    <td>#8C8C8C</td>
    <td>rgb(140, 140, 140)</td>
</tr>
    
      <tr>
    <td style="background-color:#909090; background-image: none;"></td>
    <td>#909090</td>
    <td>rgb(144, 144, 144)</td>
</tr>
    
    <tr>
    <td style="background-color:#979797; background-image: none;"></td>
    <td>#979797</td>
    <td>rgb(151, 151, 151)</td>
</tr>
    
    <tr>
    <td style="background-color:#999999; background-image: none;"></td>
    <td>#999999</td>
    <td>rgb(153,153,153)</td>
</tr>
    
  <tr>
    <td style="background-color:#A9A9A9; background-image: none;"></td>
    <td>#A9A9A9</td>
    <td>rgb(169, 169, 169)</td>
</tr>
    
     <tr>
    <td style="background-color:#AAAAAA; background-image: none;"></td>
    <td>#AAAAAA</td>
    <td>rgb(170, 170, 170)</td>
</tr>
    
     <tr>
    <td style="background-color:#AEAEAE; background-image: none;"></td>
    <td>#AEAEAE</td>
    <td>rgb(174, 174, 174)</td>
</tr>
    
    <tr>
    <td style="background-color:#B0B3B8; background-image: none;"></td>
    <td>#B0B3B8</td>
    <td>rgb(176, 179, 184)</td>
</tr>
    
     <tr>
    <td style="background-color:#B2BEB5; background-image: none;"></td>
    <td>#B2BEB5</td>
    <td>rgb(178, 190, 181)</td>
</tr>
    
     <tr>
    <td style="background-color:#B3B3B3; background-image: none;"></td>
    <td>#B3B3B3</td>
    <td>rgb(179, 179, 179)</td>
</tr>
    
     <tr>
    <td style="background-color:#B4B4B4; background-image: none;"></td>
    <td>#B4B4B4</td>
    <td>rgb(180, 180, 180)</td>
</tr>
    
     <tr>
    <td style="background-color:#BBBBBB; background-image: none;"></td>
    <td>#BBBBBB</td>
    <td>rgb(187, 187, 187)</td>
</tr>
    
    
     <tr>
    <td style="background-color:#BFBFBF; background-image: none;"></td>
    <td>#BFBFBF</td>
    <td>rgb(191, 191, 191)</td>
</tr>
    
    <tr>
    <td style="background-color:#C0C0C0; background-image: none;"></td>
    <td>#C0C0C0</td>
    <td>rgb(192, 192, 192)</td>
</tr>
    
    <tr>
    <td style="background-color:#C5C5C5; background-image: none;"></td>
    <td>#C5C5C5</td>
    <td>rgb(197, 197, 197)</td>
</tr>
    
    <tr>
    <td style="background-color:#CCCCCC; background-image: none;"></td>
    <td>#CCCCCC</td>
    <td>rgb(204, 204, 204)</td>
</tr>
    
    <tr>
    <td style="background-color:#D3D3D3; background-image: none;"></td>
    <td>#D3D3D3</td>
    <td>rgb(211, 211, 211)</td>
</tr>
    
     <tr>
    <td style="background-color:#D4D4D4; background-image: none;"></td>
    <td>#D4D4D4</td>
    <td>rgb(212, 212, 212)</td>
</tr>
    
     <tr>
    <td style="background-color:#DCDCDC; background-image: none;"></td>
    <td>#DCDCDC</td>
    <td>rgb(220,220,220)</td>
</tr>
    
    <tr>
    <td style="background-color:#DDDDDD; background-image: none;"></td>
    <td>#DDDDDD</td>
    <td>rgb(221, 221, 221)</td>
</tr>
    
    <tr>
    <td style="background-color:#E4E6EB; background-image: none;"></td>
    <td>#E4E6EB</td>
    <td>rgb(228, 230, 235)</td>
</tr>
    
     <tr>
    <td style="background-color:#E5E4E2; background-image: none;"></td>
    <td>#E5E4E2</td>
    <td>rgb(229, 228, 226)</td>
</tr>
    
    <tr>
    <td style="background-color:#EEEEEE; background-image: none;"></td>
    <td>#EEEEEE</td>
    <td>rgb(238, 238, 238)</td>
</tr>

    
    <tr>
    <td style="background-color:#F2F2F2; background-image: none;"></td>
    <td>#F2F2F2</td>
    <td>rgb(242, 242, 242)</td>
</tr>
    
    <tr>
    <td style="background-color:#F5F5F5; background-image: none;"></td>
    <td>#F5F5F5</td>
    <td>rgb(245, 245, 245)</td>
</tr>
</table>


## Conclusion

J'espère que vous avez trouvé cet article utile et que vous avez trouvé de l'inspiration pour votre prochain projet de design.

Si vous êtes intéressé à en apprendre plus sur CSS et le développement web front-end, consultez la certification de design web responsive de freeCodeCamp [ici](https://www.freecodecamp.org/learn/responsive-web-design/). Vous y construirez 5 projets pour votre portfolio tout en apprenant les fondamentaux du développement web.

Merci d'avoir lu et bon codage !