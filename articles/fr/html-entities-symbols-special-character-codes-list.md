---
title: Entités HTML – Une liste des espaces HTML et autres symboles et codes de caractères
  spéciaux
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2020-05-25T18:08:51.000Z'
originalURL: https://freecodecamp.org/news/html-entities-symbols-special-character-codes-list
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ad4740569d1a4ca280b.jpg
tags:
- name: HTML
  slug: html
- name: reference
  slug: reference
seo_title: Entités HTML – Une liste des espaces HTML et autres symboles et codes de
  caractères spéciaux
seo_desc: 'Most ASCII characters have a special code you can use in HTML to make that
  character reliably appear.

  These HTML Entities are particularly helpful for, say, manually inserting whitespace
  into your HTML.

  Each of these codes starts with an ampersand an...'
---

La plupart des caractères ASCII ont un code spécial que vous pouvez utiliser en HTML pour faire apparaître ce caractère de manière fiable.

Ces entités HTML sont particulièrement utiles pour, par exemple, insérer manuellement des espaces dans votre HTML.

Chacun de ces codes commence par un esperluette et se termine par un point-virgule.

Vous pouvez utiliser ces codes n'importe où dans votre HTML pour créer ce caractère de manière fiable. Il devrait s'afficher de la même manière, indépendamment de la langue dans laquelle les navigateurs de vos utilisateurs sont configurés.

Certains de ces symboles ont des codes plus faciles à retenir. Par exemple, le caractère de la monnaie Euro (€) est `&euro;`

Là où c'était possible, j'ai utilisé ces codes plus faciles à retenir au lieu de leurs codes numériques.

## Comment utiliser le code de caractère d'espace insécable &nbsp;

Par exemple, si vous vouliez insérer un caractère d'espace, vous pourriez faire quelque chose comme ceci :

```html
<span>Superpouvoir :&nbsp;écoute</span>
```

Vous pouvez même insérer plusieurs de ces caractères à la suite pour créer un rembourrage de texte improvisé :

```html
<span>Superpouvoir :&nbsp;&nbsp;&nbsp;écoute</span>
```

## Comment faire un saut de ligne en HTML en utilisant le code de caractère de nouvelle ligne &#13;

Si vous vouliez forcer un saut de ligne :

```html
<p>Ceci est du texte de paragraphe et &#13; oops il y a une nouvelle ligne.</p>
```

Et oui, vous pouvez également utiliser plusieurs de ces caractères à la suite :

```html
<p>Ceci est du texte de paragraphe et &#13;&#13;&#13; oops il y a plusieurs nouvelles lignes.</p>
```

## Une liste complète des codes de caractères d'entités HTML couramment utilisés

Ci-dessous se trouve un tableau bien formaté en ASCII des symboles et caractères les plus couramment utilisés. Il m'a fallu un certain temps pour rassembler tous ces éléments et les faire bien paraître.

En tant que développeur, lorsque je recherche ces codes, j'obtiens souvent des résultats basés sur des images. Ceux-ci sont inaccessibles aux personnes souffrant de handicaps visuels et rendent difficile pour tout le monde la copie-collage des codes.

Donc, si vous trouvez cela utile, veuillez faire un lien vers cette page et la partager avec vos amis afin que plus de personnes puissent en bénéficier. 😊

```

+----------+--------+-----------------------------+
|  &code   | symbole |         description         |
+----------+--------+-----------------------------+
| &#33;    | !      | point d'exclamation         |
| &#34;    | "      | guillemet double            |
| &#35;    | #      | symbole dièse (octothorpe)  |
| &#36;    | $      | symbole dollar              |
| &#37;    | %      | symbole de pourcentage      |
| &#38;    | &      | esperluette                 |
| &#39;    | '      | apostrophe                  |
| &#40;    | (      | parenthèse gauche           |
| &#41;    | )      | parenthèse droite           |
| &#42;    | *      | astérisque                  |
| &#43;    | +      | symbole plus                |
| &#44;    | ,      | virgule                     |
| &#45;    | -      | trait d'union               |
| &#46;    | .      | point                       |
| &#47;    | /      | barre oblique               |
| &#48;    | 0      | le chiffre 0                |
| &#49;    | 1      | le chiffre 1                |
| &#50;    | 2      | le chiffre 2                |
| &#51;    | 3      | le chiffre 3                |
| &#52;    | 4      | le chiffre 4                |
| &#53;    | 5      | le chiffre 5                |
| &#54;    | 6      | le chiffre 6                |
| &#55;    | 7      | le chiffre 7                |
| &#56;    | 8      | le chiffre 8                |
| &#57;    | 9      | le chiffre 9                |
| &#58;    | :      | deux-points                 |
| &#59;    | ;      | point-virgule               |
| &#60;    | <      | symbole inférieur à         |
| &#61;    | =      | symbole égal                |
| &#62;    | >      | symbole supérieur à         |
| &#63;    | ?      | point d'interrogation       |
| &#64;    | @      | arobase                     |
| &#65;    | A      | A majuscule                 |
| &#66;    | B      | B majuscule                 |
| &#67;    | C      | C majuscule                 |
| &#68;    | D      | D majuscule                 |
| &#69;    | E      | E majuscule                 |
| &#70;    | F      | F majuscule                 |
| &#71;    | G      | G majuscule                 |
| &#72;    | H      | H majuscule                 |
| &#73;    | I      | I majuscule                 |
| &#74;    | J      | J majuscule                 |
| &#75;    | K      | K majuscule                 |
| &#76;    | L      | L majuscule                 |
| &#77;    | M      | M majuscule                 |
| &#78;    | N      | N majuscule                 |
| &#79;    | O      | O majuscule                 |
| &#80;    | P      | P majuscule                 |
| &#81;    | Q      | Q majuscule                 |
| &#82;    | R      | R majuscule                 |
| &#83;    | S      | S majuscule                 |
| &#84;    | T      | T majuscule                 |
| &#85;    | U      | U majuscule                 |
| &#86;    | V      | V majuscule                 |
| &#87;    | W      | W majuscule                 |
| &#88;    | X      | X majuscule                 |
| &#89;    | Y      | Y majuscule                 |
| &#90;    | Z      | Z majuscule                 |
| &#91;    | [      | crochet gauche              |
| &#92;    | \      | barre oblique inverse       |
| &#93;    | ]      | crochet droit               |
| &#94;    | ^      | circonflexe                 |
| &#95;    | _      | trait de soulignement       |
| &#96;    | `      | accent grave                |
| &#97;    | a      | a minuscule                 |
| &#98;    | b      | b minuscule                 |
| &#99;    | c      | c minuscule                 |
| &#100;   | d      | d minuscule                 |
| &#101;   | e      | e minuscule                 |
| &#102;   | f      | f minuscule                 |
| &#103;   | g      | g minuscule                 |
| &#104;   | h      | h minuscule                 |
| &#105;   | i      | i minuscule                 |
| &#106;   | j      | j minuscule                 |
| &#107;   | k      | k minuscule                 |
| &#108;   | l      | l minuscule                 |
| &#109;   | m      | m minuscule                 |
| &#110;   | n      | n minuscule                 |
| &#111;   | o      | o minuscule                 |
| &#112;   | p      | p minuscule                 |
| &#113;   | q      | q minuscule                 |
| &#114;   | r      | r minuscule                 |
| &#115;   | s      | s minuscule                 |
| &#116;   | t      | t minuscule                 |
| &#117;   | u      | u minuscule                 |
| &#118;   | v      | v minuscule                 |
| &#119;   | w      | w minuscule                 |
| &#120;   | x      | x minuscule                 |
| &#121;   | y      | y minuscule                 |
| &#122;   | z      | z minuscule                 |
| &#123;   | {      | accolade gauche             |
| &#124;   | |      | barre verticale             |
| &#125;   | }      | accolade droite             |
| &#126;   | ~      | tilde                       |
| &larr;   | ←      | flèche gauche               |
| &uarr;   | ↑      | flèche haut                 |
| &rarr;   | →      | flèche droite               |
| &darr;   | ↓      | flèche bas                  |
| &harr;   | ↔      | flèche gauche-droite        |
| &lArr;   | ⇐      | flèche double gauche        |
| &uArr;   | ⇑      | flèche double haut          |
| &rArr;   | ⇒      | flèche double droite        |
| &dArr;   | ⇓      | flèche double bas           |
| &hArr;   | ⇔      | flèche double gauche-droite |
| &lsquo;  | ‘      | guillemet simple gauche     |
| &rsquo;  | ’      | guillemet simple droit      |
| &ldquo;  | "      | guillemet double gauche     |
| &rdquo;  | "      | guillemet double droit      |
| &#8218;  | ‚      | guillemet simple bas        |
| &#8222;  | „      | guillemet double bas        |
| &ndash;  | –      | tiret en                    |
| &mdash;  | —      | tiret em                    |
| &nbsp;   |        | espace insécable            |
| &iexcl;  | ¡      | point d'exclamation inversé |
| &sect;   | §      | symbole de section          |
| &brvbar; | ¦      | barre verticale brisée      |
| &copy;   | ©      | symbole de copyright        |
| &reg;    | ®      | symbole de marque déposée  |
| &#8482;  | ™      | symbole de marque           |
| &cent;   | ¢      | symbole de cent             |
| &pound;  | £      | symbole de livre sterling   |
| &yen;    | ¥      | symbole de yen              |
| &euro;   | €      | symbole d'euro              |
| &plusmn; | ±      | symbole plus ou moins       |
| &micro;  | µ      | symbole micro (mu)          |
| &183;    | ·      | point médian                |
| &deg;    | °      | symbole de degré            |
| &sup1;   | ¹      | exposant un                 |
| &sup2;   | ²      | exposant deux (carré)       |
| &sup3;   | ³      | exposant trois (cube)       |
| &para;   | ¶      | symbole de paragraphe       |
| &middot; | ·      | point médian                |
| &frac14; | ¼      | fraction un quart           |
| &frac12; | ½      | fraction un demi            |
| &frac34; | ¾      | fraction trois quarts        |
| &iquest; | ¿      | point d'interrogation inversé |
| &#8224;  | †      | obèle                       |
| &#8225;  | ‡      | double obèle                |
| &#8226;  | •      | puce                        |
| &#8230;  | …      | points de suspension        |
+----------+--------+-----------------------------+
```