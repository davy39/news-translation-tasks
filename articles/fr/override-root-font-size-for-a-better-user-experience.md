---
title: Comment remplacer la taille de police racine pour créer une meilleure expérience
  utilisateur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-23T15:14:55.000Z'
originalURL: https://freecodecamp.org/news/override-root-font-size-for-a-better-user-experience
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/root-font-size-article-image.jpeg
tags:
- name: Accessibility
  slug: accessibility
- name: user experience
  slug: user-experience
- name: ux design
  slug: ux-design
seo_title: Comment remplacer la taille de police racine pour créer une meilleure expérience
  utilisateur
seo_desc: "By Damla Erkiner\nBack in the day, web developers, front-end engineers,\
  \ and UI designers had a bit of an easier job. This is because they weren't expected\
  \ to rearrange their code and designs to fit so many different screen sizes. \n\
  But in today's world..."
---

Par Damla Erkiner

À l'époque, les développeurs web, les ingénieurs front-end et les designers UI avaient un travail un peu plus facile. Cela est dû au fait qu'ils n'étaient pas censés réorganiser leur code et leurs designs pour s'adapter à autant de tailles d'écran différentes. 

Mais dans le monde d'aujourd'hui, si vous prenez une décision qui ne prend pas en compte les techniques de design responsive, elle peut être vouée à l'échec. 

Après tout, personne ne veut visiter un site web pour regarder des formes étranges, des images déformées et du texte illisible. 

Le temps des gens est précieux et limité, particulièrement dans le monde rapide d'aujourd'hui. Une mauvaise expérience utilisateur sous la forme d'un design web non responsive peut vraiment nuire à une entreprise ou à une marque en un clin d'œil. 

C'est pourquoi chaque développeur devrait traiter ses produits et sites web comme des pierres précieuses dans son portfolio. Ce sont littéralement une partie de votre marque personnelle et vous ne voulez pas la ruiner avec de mauvais designs.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/responsive-webdesign-vs-non-responsive-webdesign.png)
_[Illustration par Forty One](https://www.fortyone.io/en/responsive-webdesign.html)_

Si vous voulez garantir une expérience utilisateur sans tracas, en tant que développeur web ou designer, vous êtes censé adopter certaines pratiques qui vous obligent à jouer avec la mise en page. De cette manière, chaque page que vous composez semble sophistiquée et est conviviale, quelle que soit la taille de l'écran. 

Ce processus de création de designs responsives est profondément lié à [l'architecture de contenu](https://www.madcapsoftware.com/blog/content-architecture-what-it-is-and-why-its-important/#:~:text=What%20is%20Content%20Architecture%3F,can%20affect%20the%20content%20architecture.). 

Il existe diverses techniques que vous pouvez utiliser pour faire sourire les utilisateurs potentiels de votre site web – ou au moins pour qu'ils ne se sentent pas frustrés – lorsqu'ils regardent leurs écrans. 

Celles-ci peuvent impliquer l'utilisation de media queries, de CSS Flexbox ou de CSS Grid. Cela étant dit, cet article considérera principalement une méthode qui est populaire parmi les développeurs web expérimentés. 

## Pourquoi devriez-vous ajuster la taille de police racine ?

En bref, cette technique cible la taille de police racine et elle a aussi à voir avec pourquoi vous choisissez les unités 'rem' avec cette configuration. Si vous êtes déjà curieux à ce sujet, plongeons-nous dedans.

Tout d'abord, vous devez savoir que la taille de police racine standard des navigateurs est de 16px. Cette valeur fixe est en unités 'px' par défaut. Mais les unités 'rem' comparées aux 'px' sont capables de créer des sites web plus responsives. Vous pouvez en lire plus à ce sujet dans [cet article](https://www.aleksandrhovhannisyan.com/blog/use-rems-for-font-size/). 

Donc, si nous essayons de convertir les valeurs px en rem, nous devrons faire quelques calculs. Supposons que nous voulons définir la taille de police d'un élément à 4px, mais nous voulons aussi qu'elle soit aussi responsive que possible. Pour la transformer en une valeur 'rem', nous devons la diviser par 16px et le résultat sera 0.25rem. [Un convertisseur en ligne](https://nekocalc.com/px-to-rem-converter) existe également à cette fin.

Tout serait parfait si nous avions un moyen de transformer chaque valeur 'px' en une valeur 'rem' plus facilement, maintenant que rem est considéré comme plus responsive. Voici comment nos rêves peuvent devenir réalité.

Au lieu de traiter avec de tels calculs fastidieux, nous pouvons définir la taille de police racine (HTML) à 62.5%. Dans ce cas, vous pouvez faire toutes les autres calculs automatiquement via le système. 

## Comment changer la taille de police racine

Plongeons dans les détails pour mieux comprendre la situation. Lorsque la taille de police racine/HTML est de 100%, la taille de police est de 16px par défaut. Mais, si vous la définissez à 62.5%, la nouvelle valeur racine sera de 10px. 

Maintenant, 10px (1rem) est beaucoup trop petit et est une recette pour le désastre en termes de bonne expérience utilisateur. Nous devons donc la définir à 1.6rem (16x) à nouveau dans le body. Tout semble identique en surface. Mais encore, cette fois, la nouvelle configuration rem sera plus responsive que celle de la version 'px'.

Maintenant, nous sommes capables de traduire toutes les valeurs en unités rem. Le point délicat ici est le calcul de la taille racine dans la section HTML. Maintenant, quelle que soit la taille que nous choisissons pour le body, elle sera remodelée conformément à la valeur prédéfinie dans la racine/HTML. Pour faire simple, la nouvelle valeur en pourcentage '62.5%' dans la section racine/html assure la transformation fluide de 'px' en 'rem'.

## Pourquoi nous préférons l'expression 'Pourcentage'

À ce stade, vous pourriez vous demander pourquoi nous optons pour l'expression en pourcentage (62.5%) avec les unités 'rem'. Pourquoi se donner tant de mal ? La version 'px' n'est-elle pas censée être la même ? Eh bien, pas tout à fait. 

Comme [certains développeurs sur Quora](https://www.quora.com/Why-is-the-CSS-technique-html-font-size-62-5-used-to-set-the-base-font-size-to-10px-Why-not-just-simply-say-html-font-size-10px) le suggèrent, les valeurs basées sur les pourcentages peuvent s'ajuster plus facilement par rapport aux nombres fixes. Cela signifie que non seulement les unités rem sont importantes, mais aussi la préférence pour les pourcentages dans la partie racine/HTML compte beaucoup dans cette configuration particulière.

La partie la plus efficace concernant le chiffre '62.5%' dans la racine est que même si le visiteur modifie la taille de police du navigateur, il pourra consulter la page correctement grâce à la configuration CSS associée. 

De plus, cela ne pose aucun problème en termes d'accessibilité car nous définissons également la taille de police du body à 1.6rem en plus de l'arrangement à 62.5% dans la section racine/HTML. De cette manière, nous nous assurons que ces deux nombres vont de pair, quelle que soit la taille de l'écran.

## Pourquoi l'accessibilité est importante

Il est important d'élaborer sur la question de l'accessibilité. Je crois qu'elle devrait être d'une importance capitale pour les développeurs web et les designers de tous horizons.

Des [recherches](https://websitesetup.org/websites-for-visually-impaired/) montrent que le nombre d'individus malvoyants est progressivement en augmentation, et il y a de nombreuses raisons à cela. Mais une chose est sûre : à l'ère des avancées technologiques de pointe, tout le monde devrait pouvoir profiter d'Internet et accéder à l'information grâce à certaines mesures d'accessibilité. Et l'application de techniques de design responsive appropriées est définitivement l'une d'entre elles. 

## Quel est le message significatif de Bruce Lawson ?

Je me souviens avoir regardé [une excellente conférence de Bruce Lawson](https://www.youtube.com/watch?v=tgXbbOirY8o), un expert en matière de normes web. Lors d'un bootcamp virtuel gratuit organisé par [Class Central](https://www.classcentral.com/) et freeCodeCamp l'année dernière, il était un conférencier invité. Il a expliqué très clairement pourquoi nous, en tant que développeurs web, sommes responsables de garder tout le monde inclus et de nous assurer que personne d'autre n'est laissé de côté lors du codage et/ou de la conception d'un site web.

%[https://www.youtube.com/watch?v=tgXbbOirY8o]

## Testons notre nouvelle configuration ?

Soyons plus spécifiques et imaginons un scénario. Supposons qu'un utilisateur malvoyant souhaite visiter la page web que vous avez conçue. Pour pouvoir tout voir plus clairement, il décide de faire quelques ajustements à la taille de police du navigateur à l'avance. Par exemple, il pourrait la définir à 18px, un peu plus grande que la taille standard (16px). 

Il est maintenant temps d'examiner de près le fragment de code suivant pour witness la fonctionnalité de la configuration orientée HTML et body du point de vue de cet individu.

```css
html {
    font-size: 62.5%;
}
body {
    font-size: 1.6rem;
}
```

En tant que développeur de cette page web, vous avez choisi '62.5%' pour le HTML et '1.6rem' pour le body comme taille de police initiale. Mais rappelez-vous que la taille de police du navigateur déterminée par l'utilisateur ci-dessus est maintenant de 18px, et non plus de 16px. Comment cela va-t-il fonctionner ? Cette personne sera-t-elle contrariée et quittera-t-elle la page en se sentant frustrée ou continuera-t-elle à surfer sur la page web sans problème ?

Voici la réponse. Une fois que la taille de police du navigateur est choisie à 18px par l'utilisateur, la taille de police sera instantanément recalculée à 11.25px (18px * 62.5%) par le système. En conséquence, la valeur pour le body sera de 18px (1.6rem * 11.25px) exactement comme demandé par cet utilisateur spécifique. Ainsi, cette personne ne sera pas affectée négativement par la situation simplement parce qu'elle souhaite voir la taille de police plus grande que la version standard. 

La bonne nouvelle est que tout cela sera recalculé automatiquement. Et grâce à la configuration basée sur les pourcentages et les rem, le texte sur la page web sera plus responsive et convivial.

## Plus d'expériences

Pour voir davantage les effets possibles de cette configuration, examinons maintenant comment les tailles de police des éléments/conteneurs principaux suivants fonctionneront pour notre utilisateur.

```css
html {
    font-size: 62.5%;
}
body {
    font-size: 1.6rem;
}
header {
    font-size: 3rem;
}
section {
    font-size: 2.5rem;
}
footer {
    font-size: 2.8rem;
}
```

Conformément à la nouvelle taille HTML (62.5% * 18px = 11.25px), la valeur recalculée de la taille de police de l'élément header sera de 33.75px (3rem * 11.25px). Celle de l'élément section sera d'environ 28px (2.5rem * 11.25px). Et enfin, la taille de police du footer sera de 31.5px (11.25px * 2.8rem) du point de vue de notre utilisateur imaginaire. 

En d'autres termes, avec le nouvel arrangement impliquant la taille de police du HTML et du body, tout le reste sera géré en douceur sous le capot sans que vous, en tant que développeur, ayez à effectuer des calculs séparés pour chaque élément.

## Cette méthode est-elle infaillible ?

Malgré le fait que la méthode utilisant la taille racine '62.5%', puisqu'il s'agit spécifiquement d'une valeur en pourcentage et de la préférence basée sur les rem dans la section body, nous donne une chance de jouer avec la taille de police générale de manière dynamique, elle n'est pas non plus sans risque et vous devez l'utiliser avec prudence (voir [cet article](https://www.joshwcomeau.com/css/surprising-truth-about-pixels-and-accessibility/) pour plus d'informations). 

Par exemple, cela peut entraîner [certains problèmes](https://css-tricks.com/forums/topic/62-5-font-size/) lorsque les valeurs 'em' sont préférées au lieu des valeurs 'rem'. De plus, cette technique ne redimensionne que le texte. Vous devrez donc utiliser d'autres astuces (par exemple, lorsque vous traitez la taille des images). 

Cela dit, le remplacement de la taille de police racine est toujours une pratique répandue préférée par [de nombreux développeurs](https://www.aleksandrhovhannisyan.com/blog/62-5-percent-font-size-trick/) dans le monde et elle peut être pratique si elle est utilisée avec soin. 

## Conclusion

En résumé, les concepts d'accessibilité, de design web responsive, de code maintenable et évolutif, et de performance web sont fondamentaux pour créer une expérience utilisateur solide. 

Peut-être qu'à l'avenir, quelqu'un trouvera une meilleure façon de gérer cela. Je voulais simplement partager avec vous les avantages et les inconvénients de l'ajustement de la taille de police racine. 

Même si vous ne prévoyez pas de l'utiliser du tout, l'un de vos coéquipiers pourrait l'adopter. Il est donc toujours bon d'être conscient des arguments pour et contre. 

Merci d'avoir lu. Si vous avez aimé cet article, l'une des meilleures façons de me soutenir est de le partager. Si vous avez des questions ou des commentaires, vous pouvez toujours me contacter via [LinkedIn](https://www.linkedin.com/in/damla-erkiner-000b76227/). Je serai plus qu'heureuse de vous aider avec vos questions. 

Bon codage !

**"Le savoir est une puissance." – Francis Bacon**