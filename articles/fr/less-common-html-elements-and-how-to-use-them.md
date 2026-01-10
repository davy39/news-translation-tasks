---
title: Éléments HTML moins courants et comment les utiliser dans votre code
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2024-11-04T19:31:35.814Z'
originalURL: https://freecodecamp.org/news/less-common-html-elements-and-how-to-use-them
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1730747551049/73b334f4-7b4a-448a-bfae-8b95cffe6119.png
tags:
- name: HTML5
  slug: html5
- name: HTML
  slug: html
- name: Accessibility
  slug: accessibility
- name: Web Development
  slug: web-development
seo_title: Éléments HTML moins courants et comment les utiliser dans votre code
seo_desc: 'HTML has a lot of tags that many people use every day, like <div>, <p>,
  and <a>. But there are also some hidden gems that often go unnoticed. These tags
  can help make websites more engaging, accessible, and meaningful without much extra
  effort.

  In th...'
---

HTML possède de nombreuses balises que beaucoup de gens utilisent quotidiennement, comme `<div>`, `<p>`, et `<a>`. Mais il existe également des pépites cachées qui passent souvent inaperçues. Ces balises peuvent aider à rendre les sites web plus engageants, accessibles et significatifs sans trop d'effort supplémentaire.

Dans cet article, nous allons discuter d'un groupe d'éléments HTML uniques qui peuvent améliorer vos pages web. Ils offrent des fonctions spécifiques pour formater le texte, améliorer la lisibilité et ajouter des fonctionnalités interactives.

### Table des matières

1. [La balise `<q>` : Citations courtes en ligne](#heading-la-balise-q-citations-courtes-en-ligne)
   
2. [La balise `<s>` : Texte barré](#heading-la-balise-s-texte-barré)
   
3. [La balise `<mark>` : Texte surligné](#heading-la-balise-mark-texte-surligné)
   
4. [La balise `<ruby>` : Annotation de texte en langues asiatiques](#heading-la-balise-ruby-annotation-de-texte-en-langues-asiatiques)
   
5. [La balise `<time>` : Date et heure sémantiques](#heading-la-balise-time-date-et-heure-sémantiques)
   
6. [La balise `<bdi>` : Isolation de texte bidirectionnel](#heading-la-balise-bdi-isolation-de-texte-bidirectionnel)
   
7. [La balise `<dfn>` : Définition des termes](#heading-la-balise-dfn-définition-des-termes)
   
8. [La balise `<wbr>` : Opportunités de saut de ligne](#heading-la-balise-wbr-opportunités-de-saut-de-ligne)
   
9. [La balise `<ins>` : Texte inséré](#heading-la-balise-ins-texte-inséré)
   
10. [La balise `<del>` : Texte supprimé](#heading-la-balise-del-texte-supprimé)
   
11. [Conclusion](#heading-conclusion)
   

## La balise `<q>` : Citations courtes en ligne

La balise `<q>` est utilisée pour ajouter des citations courtes à l'intérieur d'un paragraphe. Elle aide à faire ressortir les citations et à les rendre plus faciles à repérer, sans interrompre le flux du texte. Cette balise ajoute automatiquement des guillemets autour du contenu.

### Description et syntaxe

La structure de base de la balise `<q>` est simple :

```html
<p>Elle a dit, <q>C'est incroyable !</q></p>
```

Cela s'affichera comme :  
*Elle a dit, « C'est incroyable ! »*

### Comment elle diffère de l'élément `<blockquote>`

La balise `<q>` est utilisée pour les citations courtes à l'intérieur d'une phrase. En revanche, l'élément `<blockquote>` est utilisé pour les citations plus longues qui nécessitent généralement leur propre espace ou paragraphe.

Par exemple :

```html
<blockquote>
  "Ceci est une longue citation qui nécessite son propre espace. Elle est différente d'une citation courte."
</blockquote>
```

Ce bloc apparaîtra avec une indentation et est destiné à mettre en évidence une plus grande partie de texte cité.

### Cas d'utilisation : Ajout de citations dans les paragraphes

La balise `<q>` est parfaite pour les cas où vous devez mentionner une citation dans une phrase sans la séparer trop. Par exemple, lorsque vous citez quelqu'un dans un article ou un billet de blog :

```html
<p>Le professeur a dit, <q>La pratique rend parfait</q>, pendant le cours.</p>
```

Dans ce cas, la balise `<q>` garde la citation courte et à l'intérieur du même paragraphe.

<center>
<p>Le professeur a dit, <q>La pratique rend parfait</q>, pendant le cours.</p>
</center>

### Compatibilité des navigateurs et conseils de style

La plupart des navigateurs modernes ajoutent automatiquement des guillemets au contenu à l'intérieur d'une balise `<q>`. Mais vous pouvez changer son apparence en utilisant CSS si nécessaire. Voici comment vous pouvez le styliser :

```css
q {
  quotes: "\00ab" "\00bb";
  font-style: italic;
}
```

Ce code changera les guillemets en marques de style français (\00ab et \00bb) et rendra la citation en italique.

%[https://codepen.io/joanayebola/pen/YzmNWGd] 

La plupart des navigateurs supportent la balise `<q>`, donc vous n'avez pas à vous soucier des problèmes de compatibilité pour les utilisateurs modernes. Mais les anciens navigateurs peuvent nécessiter des soins supplémentaires, alors testez toujours si votre audience utilise des versions plus anciennes.

## La balise `<s>` : Texte barré

La balise `<s>` est utilisée pour montrer du texte qui n'est plus correct, pertinent ou qui a été supprimé. Elle met une ligne au milieu du texte, que nous appelons un "barré". Cette balise est souvent utilisée pour indiquer quelque chose qui a été édité ou mis à jour.

### Explication et utilisation

La balise `<s>` est simple à utiliser. Il suffit de l'envelopper autour du texte que vous souhaitez barrer :

```html
<p>Ce produit était <s>50 $</s> maintenant seulement 30 $ !</p>
```

Cela s'affichera comme :  
*Ce produit était <s>50 $</s> maintenant seulement 30 $ !*

### Cas d'utilisation courants : Indiquer le contenu supprimé ou non pertinent

La balise `<s>` est idéale pour montrer les changements de prix, les modifications ou le contenu qui n'est plus valide. Par exemple :

**Mises à jour de prix :**

```html
<p><s>75 $</s> 50 $ (Offre limitée !)</p>
```

<center>
<p><s>75 $</s> 50 $ (Offre limitée !)</p>
</center>

**Corrections ou changements :**

```html
<p><s>Ancienne adresse du site web</s> Nouvelle adresse du site web</p>
```

<center>
<p><s>Ancienne adresse du site web</s> Nouvelle adresse du site web</p>
</center>

**Contenu qui n'est plus pertinent :**

```html
<p>Cette fonctionnalité est <s>plus disponible</s>.</p>
```

<center>
<p>Cette fonctionnalité est <s>plus disponible</s>.</p>
</center>

### Possibilités de style avec CSS

Vous pouvez personnaliser l'apparence du texte barré en utilisant CSS. Par exemple, vous pouvez changer la couleur de la ligne ou du texte :

```css
s {
  text-decoration: line-through;
  color: red;
}
```

Dans ce cas, le texte aura une ligne rouge, donnant plus d'emphase au fait qu'il a été barré.

%[https://codepen.io/joanayebola/pen/VwoPjWg] 

### Signification sémantique versus décoration visuelle

La balise `<s>` a une certaine signification sémantique. Elle représente généralement un contenu qui était autrefois valide mais qui est maintenant incorrect ou obsolète. C'est plus qu'un simple changement de style. Par exemple, elle est parfaite pour montrer les changements dans les documents juridiques, les corrections dans les billets de blog ou les mises à jour de prix.

D'autre part, si vous utilisez le barré simplement pour la décoration visuelle sans signifier que le texte est incorrect, il est préférable d'utiliser directement CSS, comme ceci :

```css
span.strike {
  text-decoration: line-through;
}
```

Et ensuite l'appliquer dans votre HTML :

```html
<p>Ce texte est <span class="strike">barré</span> juste pour le plaisir !</p>
```

Cette approche est purement pour le style et ne porte pas la même signification que la balise `<s>`.

## La balise `<mark>` : Texte surligné

La balise `<mark>` est utilisée pour surligner du texte. Elle aide à attirer l'attention sur certaines parties de votre contenu, les faisant ressortir. Par défaut, les navigateurs surlignent le texte avec un fond jaune lorsque la balise `<mark>` est utilisée.

### Objectif de la balise `<mark>`

La balise `<mark>` est idéale lorsque vous souhaitez mettre en évidence quelque chose d'important. Elle est souvent utilisée pour montrer les résultats de recherche, les changements récents ou tout texte nécessitant une attention particulière.

Voici un exemple de son fonctionnement :

```html
<p>Ceci est un <mark>mot surligné</mark>.</p>
```

Cela s'affichera comme :  
*Ceci est un* ***mot surligné*** *.*

### Bonnes pratiques pour utiliser `<mark>` pour l'emphase ou les résultats de recherche

**Mise en évidence des termes clés :** Si vous souhaitez mettre en évidence des mots ou des phrases importants dans un article ou un billet de blog, la balise `<mark>` est un moyen simple de le faire :

```html
<p>Le concept le plus important ici est <mark>l'efficacité</mark>.</p>
```

<center>
<p>Le concept le plus important ici est <mark>l'efficacité</mark>.</p>
</center>

**Résultats de recherche :** Lorsque vous affichez des résultats de recherche sur une page web, l'utilisation de la balise `<mark>` pour surligner les termes correspondants facilite la recherche des utilisateurs :

```html
<p>Votre recherche pour <mark>HTML</mark> a trouvé ces résultats :</p>
```

<center>
<p>Votre recherche pour <mark>HTML</mark> a trouvé ces résultats :</p>
</center>

**Mises à jour récentes :** Vous pouvez également utiliser la balise `<mark>` pour montrer les nouvelles mises à jour ou changements dans votre contenu :

```html
<p>Nous avons récemment ajouté la <mark>nouvelle fonctionnalité</mark> à l'application.</p>
```

<center>
<p>Nous avons récemment ajouté la <mark>nouvelle fonctionnalité</mark> à l'application.</p>
</center>

### Comment styliser le texte surligné efficacement

Bien que la couleur par défaut pour `<mark>` soit le jaune, vous pouvez la changer avec CSS pour correspondre au design de votre site web. Voici un exemple de personnalisation du texte surligné :

```css
mark {
  background-color: lightblue;
  color: black;
  padding: 2px;
}
```

Cela donnera au texte un fond bleu clair avec du texte noir.

%[https://codepen.io/joanayebola/pen/poMRbde] 

Si vous souhaitez que le texte se démarque encore plus, vous pouvez ajouter une bordure ou changer le style de la police :

```css
mark {
  background-color: yellow;
  color: black;
  font-weight: bold;
  border-radius: 4px;
}
```

Cela rendrait le texte surligné plus poli et plus visible.

%[https://codepen.io/joanayebola/pen/OJKWXzV] 

### Support des navigateurs et considérations d'accessibilité

La balise `<mark>` est supportée par tous les navigateurs modernes, donc vous ne rencontrerez aucun problème de compatibilité. Assurez-vous simplement que la couleur de fond que vous choisissez offre un contraste suffisant pour la lisibilité, surtout pour les utilisateurs ayant des déficiences visuelles.

Utiliser un fond clair avec du texte foncé est une bonne règle de base. Tester le contraste des couleurs garantit que le contenu surligné reste accessible à tous, y compris ceux utilisant des lecteurs d'écran.

## La balise `<ruby>` : Annotation de texte en langues asiatiques

La balise `<ruby>` est utilisée pour ajouter de petites annotations au texte, souvent vues dans les langues asiatiques comme le japonais ou le chinois. Ces annotations aident les lecteurs avec la prononciation ou la signification, surtout lorsque les caractères sont complexes ou peu familiers.

### Définition et cas d'utilisation pour `<ruby>`

Dans des langues comme le japonais, il est courant d'utiliser un petit guide au-dessus ou à côté des caractères pour montrer comment ils doivent être prononcés. La balise `<ruby>` associe le texte principal avec une petite annotation, généralement dans un script plus simple.

Voici un exemple de base :

```html
<ruby>漢 <rt>かん</rt> 字 <rt>じ</rt></ruby>
```

Cela montre les caractères kanji japonais *漢字* avec leur prononciation (furigana) affichée au-dessus ou à côté comme *かんじ* (kanji).

<center>
<ruby>漢 <rt>かん</rt> 字 <rt>じ</rt></ruby>
</center>

### L'importance des sous-éléments `<rp>` et `<rt>`

L'élément `<rt>` est utilisé à l'intérieur de la balise `<ruby>` pour définir l'annotation (comme la prononciation) pour le texte principal. Il signifie "texte ruby".

```html
<ruby>漢 <rt>かん</rt></ruby>
```

Cela affichera *漢* avec *かん* (kan) au-dessus comme annotation.

<center>
<ruby>漢 <rt>かん</rt></ruby>
</center>

L'élément `<rp>`, abréviation de "ruby parenthesis", est utilisé comme solution de repli pour les navigateurs qui ne supportent pas la balise `<ruby>`. Il enveloppe des caractères supplémentaires, tels que des parenthèses, autour du texte ruby pour montrer qu'il s'agit d'une annotation :

```html
<ruby>漢 <rp>(</rp><rt>かん</rt><rp>)</rp></ruby>
```

Si le navigateur ne supporte pas les annotations ruby, il affichera la prononciation à l'intérieur des parenthèses, comme ceci :  
*漢 (かん)*.

### Exemples pratiques : Annotations Ruby pour l'apprentissage des langues

La balise `<ruby>` est un outil utile pour les apprenants de langues. Elle peut afficher la prononciation pour des mots ou des caractères peu familiers directement au-dessus ou à côté. Cela facilite la lecture et l'apprentissage de nouveaux mots pour les débutants.

Par exemple, disons que vous voulez aider quelqu'un à apprendre le mot chinois pour "personne" :

```html
<ruby>人 <rt>rén</rt></ruby>
```

Cela montrerait *人* avec la prononciation *rén* au-dessus.

<center>
<ruby>人 <rt>rén</rt></ruby>
</center>

Pour des phrases plus longues :

```html
<p><ruby>我 <rt>wǒ</rt></ruby> <ruby>是 <rt>shì</rt></ruby> <ruby>学生 <rt>xuésheng</rt></ruby>.</p>
```

Cela aide les étudiants à voir à la fois les caractères et la prononciation correcte.

<center>
<p><ruby>我 <rt>wǒ</rt></ruby> <ruby>是 <rt>shì</rt></ruby> <ruby>学生 <rt>xuésheng</rt></ruby>.</p>
</center>

### Compatibilité multi-navigateurs et considérations de rendu

La balise `<ruby>` est supportée par la plupart des navigateurs modernes, mais les plus anciens peuvent ne pas la rendre correctement. C'est là que l'élément `<rp>` est utile, garantissant que les annotations restent lisibles si le navigateur ne supporte pas le texte ruby.

Pour l'accessibilité, assurez-vous que les annotations ont suffisamment d'espace autour d'elles pour qu'elles soient faciles à lire. Vous pouvez également utiliser CSS pour ajuster l'apparence des annotations :

```css
ruby rt {
  font-size: 0.75em;
  color: gray;
}
```

Cela rendra le texte ruby plus petit et d'une couleur différente pour le garder visuellement séparé du contenu principal.

%[https://codepen.io/joanayebola/pen/YzmNWLb] 

L'utilisation de `<ruby>` est un excellent moyen d'améliorer la lisibilité pour les apprenants de langues ou les lecteurs peu familiers avec certains scripts. N'oubliez pas de vérifier la compatibilité des navigateurs et d'ajouter des solutions de repli pour une meilleure expérience utilisateur sur différents appareils.

## La balise `<time>` : Date et heure sémantiques

La balise `<time>` est utilisée pour marquer les dates ou les heures dans un format lisible par machine. Elle aide les moteurs de recherche, les navigateurs et autres outils à reconnaître plus clairement les informations liées au temps, ce qui est utile pour améliorer la visibilité dans les résultats de recherche ou pour un meilleur traitement des données.

### Utilisation de la balise `<time>` pour les dates et heures lisibles par machine

Lorsque vous utilisez la balise `<time>`, elle permet de fournir des dates ou des heures faciles à lire à la fois par les personnes et les ordinateurs. Cela est particulièrement utile sur les blogs, les articles de presse ou les pages d'événements.

Voici un exemple :

```html
<p>Publié le <time datetime="2024-10-01">1er octobre 2024</time></p>
```

Le texte "1er octobre 2024" est ce que les utilisateurs verront, mais l'attribut `datetime` fournit une version lisible par machine de la date. Les moteurs de recherche peuvent maintenant interpréter facilement cette date.

<center>
<p>Publié le <time>1er octobre 2024</time></p>
</center>

Vous pouvez également utiliser la balise `<time>` pour afficher des heures :

```html
<p>L'événement commence à <time datetime="13:00">13h00</time>.</p>
```

Cela rend clair pour les utilisateurs et les machines quand l'événement a lieu.

<center>
<p>L'événement commence à <time>13h00</time>.</p>
</center>

### Comment `<time>` améliore le SEO et le traitement des données pour les détails des événements

Les moteurs de recherche s'appuient sur des données structurées pour mieux comprendre le contenu. La balise `<time>` leur donne une idée plus claire de quand les événements, les publications ou les échéances se produisent, améliorant la pertinence des résultats de recherche. Par exemple, les moteurs de recherche peuvent mieux afficher la date de publication d'un billet de blog ou l'heure d'un événement.

Pour une page d'événement, l'exemple suivant fournit à la fois des informations temporelles conviviales pour les humains et pour les machines :

```html
<p>Rejoignez-nous pour l'atelier le <time datetime="2024-12-15">15 décembre 2024</time> à <time datetime="15:30">15h30</time>.</p>
```

Les moteurs de recherche et les robots d'indexation peuvent alors extraire ces données et les utiliser pour créer des extraits enrichis dans les résultats de recherche, aidant l'événement à se faire remarquer.

### Exemples d'utilisation dans les articles, blogs et pages d'événements

Voici quelques exemples pratiques de l'utilisation de la balise `<time>` :

1. **Billets de blog :** Vous pouvez afficher quand un article a été publié ou mis à jour pour la dernière fois :
    
    ```html
    <p>Dernière mise à jour le <time datetime="2024-09-28">28 septembre 2024</time>.</p>
    ```
    
2. **Listes d'événements :** Les sites web d'événements peuvent utiliser la balise `<time>` pour lister quand un événement aura lieu :
    
    ```html
    <p>Notre prochaine rencontre aura lieu le <time datetime="2024-11-10">10 novembre 2024</time> à <time datetime="18:00">18h00</time>.</p>
    ```
    
3. **Dates limites :** Lorsque vous présentez des dates limites importantes, utilisez la balise `<time>` pour plus de clarté :
    
    ```html
    <p>Soumettez votre candidature avant le <time datetime="2024-10-30T23:59">30 octobre 2024, 23h59</time>.</p>
    ```
    

Dans tous ces exemples, l'attribut `datetime` garantit que les ordinateurs peuvent lire correctement les informations temporelles, tandis que les utilisateurs voient une version plus lisible.

### Support des navigateurs et accessibilité

La balise `<time>` est largement supportée par les navigateurs modernes. Elle améliore également l'accessibilité car les lecteurs d'écran peuvent interpréter la date et l'heure plus précisément, offrant une meilleure expérience pour les utilisateurs handicapés.

## La balise `<bdi>` : Isolation de texte bidirectionnel

La balise `<bdi>` signifie "isolation bidirectionnelle" et est utilisée pour prévenir les problèmes de direction de texte sur les sites multilingues. Cette balise est particulièrement utile lorsque vous travaillez avec du contenu qui inclut à la fois des langues de gauche à droite (LTR) et de droite à gauche (RTL).

### Rôle de la balise `<bdi>` dans les sites multilingues

Lorsque vous mélangez des langues avec différentes directions de texte, comme l'anglais (LTR) et l'arabe (RTL), le flux naturel du texte peut parfois devenir désordonné. La balise `<bdi>` aide à garder la mise en page du texte propre, en s'assurant que chaque portion de texte s'affiche correctement, quelle que soit la direction de la langue.

Par exemple, si vous souhaitez afficher une entrée utilisateur (comme un nom d'utilisateur) à côté d'un autre texte, et que vous ne savez pas dans quelle langue le nom d'utilisateur sera, vous pouvez utiliser `<bdi>` pour vous assurer qu'il ne perturbe pas le flux.

### Comment utiliser `<bdi>` pour prévenir les problèmes de direction de texte

La balise `<bdi>` enveloppe la partie du texte que vous souhaitez isoler, et elle empêche la direction du texte d'être affectée par le contenu environnant.

Voici un exemple simple :

```html
<p>Utilisateur <bdi>اسم</bdi> s'est connecté.</p>
```

Si le nom d'utilisateur est en arabe (qui se lit de droite à gauche), la balise `<bdi>` garantit que le reste de la phrase (qui est en anglais et se lit de gauche à droite) n'est pas perturbé. Sans la balise `<bdi>`, la phrase pourrait s'afficher incorrectement en raison du mélange des directions de texte.

Un autre exemple avec des nombres :

```html
<p>Numéro de facture : <bdi>#1234</bdi></p>
```

Si le numéro de facture inclut du texte ou des nombres dans différentes directions, la balise `<bdi>` garantit que la mise en forme reste correcte.

### Exemples de `<bdi>`

La balise `<bdi>` est couramment utilisée dans les applications multilingues, les plateformes de contenu généré par les utilisateurs et les sites web qui gèrent plusieurs langues à la fois. Par exemple, les sites web qui permettent aux utilisateurs de saisir des données, telles que des noms ou des adresses, peuvent utiliser `<bdi>` pour garantir un alignement de texte approprié.

Voici un exemple sur un forum :

```html
<p><bdi>مستخدم</bdi> a aimé votre publication !</p>
```

Sans `<bdi>`, le texte pourrait s'afficher de manière maladroite, mais avec lui, à la fois le nom d'utilisateur en arabe et le texte en anglais s'affichent correctement.

### Compatibilité des navigateurs

La balise `<bdi>` est supportée dans tous les navigateurs modernes, y compris Chrome, Firefox, Safari et Edge. C'est une solution légère, ne nécessite pas de style spécial et aide à garder la mise en page de votre contenu propre lorsque vous traitez du texte multilingue.

## La balise `<dfn>` : Définition des termes

La balise `<dfn>` est utilisée pour marquer la première instance d'un terme qui est défini dans une page web. Elle aide les lecteurs à reconnaître rapidement qu'un mot ou une phrase particulier est une définition, améliorant la clarté de votre contenu, surtout dans l'écriture technique.

### Comment utiliser `<dfn>` pour marquer les définitions

La balise `<dfn>` est simple à utiliser. Vous l'enveloppez autour du mot ou de la phrase que vous souhaitez définir. Typiquement, le terme apparaît près de l'explication de sa signification.

Exemple :

```html
<p>Le <dfn>DOM</dfn> (Document Object Model) est une interface de programmation pour les documents web.</p>
```

Ici, la balise `<dfn>` met en évidence que "DOM" est le terme défini.

<center>
<p>Le <dfn>DOM</dfn> (Document Object Model) est une interface de programmation pour les documents web.</p>
</center>

### Bonnes pratiques pour fournir des explications dans les articles

Lorsque vous utilisez la balise `<dfn>`, assurez-vous que le terme que vous définissez est suivi de près par son explication. Cela garde les choses claires et aide les lecteurs à connecter le terme avec sa signification immédiatement.

Il est également bon de n'utiliser `<dfn>` que la première fois qu'un terme est introduit, car le répéter plusieurs fois peut confondre le lecteur.

Par exemple, dans un article technique sur HTML :

```html
<p>L'<dfn>API</dfn> (Application Programming Interface) permet à différentes applications logicielles de communiquer entre elles. Une fois définie, une API peut simplifier de nombreuses tâches de développement web.</p>
```

Dans ce cas, "API" est défini lorsqu'il est mentionné pour la première fois, et les utilisations ultérieures de "API" n'ont plus besoin de la balise `<dfn>`.

### Comment `<dfn>` améliore la clarté du contenu technique

L'utilisation de la balise `<dfn>` dans l'écriture technique est un excellent moyen de rendre le contenu plus facile à suivre. Elle signale clairement aux lecteurs lorsque vous introduisez un nouveau terme, ce qui est particulièrement utile lorsque vous expliquez des idées complexes. Cela aide à améliorer la lisibilité et permet aux utilisateurs de saisir les concepts clés plus rapidement.

En marquant les définitions avec `<dfn>`, les moteurs de recherche et autres outils peuvent également mieux interpréter votre contenu, le rendant plus accessible. Par exemple, les glossaires techniques ou les sites éducatifs peuvent utiliser `<dfn>` pour faire ressortir leurs termes.

### Exemple de `<dfn>`

```html
<p>L'<dfn>URL</dfn> (Uniform Resource Locator) est l'adresse utilisée pour accéder à une ressource sur le web.</p>
```

Dans cette phrase, le lecteur est introduit au terme "URL", suivi d'une explication claire. Cette méthode d'introduction des termes avec la balise `<dfn>` aide à rendre le contenu technique beaucoup plus facile à lire et à comprendre, surtout pour ceux qui ne sont pas familiers avec le sujet.

## La balise `<wbr>` : Opportunités de saut de ligne

La balise `<wbr>` est utilisée pour suggérer où un mot ou une URL peut être divisé pour créer un saut de ligne si nécessaire. Cela est utile lorsque vous traitez avec des mots longs, des URL ou tout texte qui pourrait rompre la mise en page d'une page web.

### Qu'est-ce que la balise `<wbr>` et pourquoi est-elle essentielle pour les mots longs ou les URL

Parfois, les mots longs ou les URL peuvent perturber le design d'une page web en provoquant un défilement horizontal ou en rompant la mise en page. La balise `<wbr>` donne au navigateur un indice sur l'endroit où rompre le mot, mais seulement si nécessaire. Cela aide à garder le texte lisible et empêche le débordement.

Par exemple, si vous avez une URL longue, vous pouvez placer la balise `<wbr>` pour indiquer au navigateur où il peut rompre le texte :

```html
<p>Visitez notre site web à l'adresse https://www.example<wbr>.com/super/long-url-that-might-break-layout</p>
```

Si le navigateur doit rompre l'URL, il le fera après le `<wbr>`, garantissant que le design reste intact.

### Bonnes pratiques pour contrôler le retour à la ligne et le débordement de texte

La balise `<wbr>` doit être utilisée dans les endroits où le texte pourrait causer des problèmes de débordement, tels que les termes techniques longs, les adresses e-mail ou les URL. Mais ne l'utilisez pas trop, car des ruptures inutiles peuvent rendre le texte plus difficile à lire.

Voici un autre exemple avec un mot long :

```html
<p>Ce mot est trop long : anti<wbr>disestablishmentarianism.</p>
```

Si le mot devient trop long pour la ligne, le navigateur le divisera après "anti-" sans affecter la lisibilité.

En combinaison avec CSS, vous pouvez également contrôler le retour à la ligne et le débordement de texte pour de meilleurs résultats :

```css
p {
  word-wrap: break-word;
  overflow-wrap: break-word;
}
```

Ce CSS garantit que le texte se repliera proprement lorsque cela sera nécessaire, et l'utilisation de `<wbr>` peut donner plus de contrôle sur l'endroit où ces ruptures se produisent.

### Support des navigateurs pour `<wbr>` et défis potentiels

La balise `<wbr>` est supportée dans tous les principaux navigateurs, y compris Chrome, Firefox, Safari et Edge. Elle est légère et ne nécessite aucun style spécial pour fonctionner.

Mais une chose à surveiller est que l'utilisation excessive de la balise peut faire apparaître des ruptures de texte non naturelles si le contenu est redimensionné ou visualisé sur différents tailles d'écran.

Par exemple :

```html
<p>Contactez-nous à l'adresse longemail<wbr>@example<wbr>.com pour plus d'informations.</p>
```

Dans ce cas, vous pouvez éviter que les longues adresses e-mail ne causent de problèmes de mise en page, mais l'e-mail peut apparaître rompu à différents endroits en fonction de la largeur de l'écran.

Utilisez `<wbr>` lorsque vous anticipez de longues chaînes de texte qui peuvent ne pas se rompre naturellement, en gardant votre design propre et fonctionnel sur tous les appareils.

## La balise `<ins>` : Texte inséré

La balise `<ins>` est utilisée pour montrer le texte qui a été ajouté à un document. Cela est souvent utile pour suivre les modifications, les mises à jour ou les changements dans les documents. Elle est également accompagnée d'un soulignement par défaut pour mettre en évidence le nouveau contenu.

### Qu'est-ce que la balise `<ins>` et comment se compare-t-elle à la balise `<s>` ?

La balise `<ins>` est conçue pour marquer le contenu inséré, tandis que la balise `<s>` est utilisée pour le texte qui a été supprimé ou qui n'est plus pertinent. Les deux balises sont utiles lorsque vous devez montrer des changements dans un document, comme des mises à jour ou des révisions.

Exemple :

```html
<p>Ceci est le <ins>nouveau texte</ins> qui a été ajouté.</p>
<p>Ceci est le <s>ancien texte</s> qui n'est plus valide.</p>
```

Ici, la balise `<ins>` met en évidence ce qui a été ajouté, et la balise `<s>` montre ce qui a été barré comme obsolète.

<center>
<p>Ceci est le nouveau texte qui a été ajouté.</p>
<p>Ceci est le <s>ancien texte</s> qui n'est plus valide.</p>
</center>

### Utilisation dans le suivi des modifications de documents ou la gestion des versions

La balise `<ins>` est couramment utilisée lors de la gestion de documents nécessitant un contrôle de version ou où les modifications doivent être visibles. Par exemple, vous pouvez l'utiliser dans les plateformes d'écriture collaborative ou les documents juridiques pour montrer quelles parties ont été ajoutées.

Exemple de document avec des modifications :

```html
<p>Le contrat a été mis à jour pour inclure <ins>une clause supplémentaire</ins> sur la confidentialité des données.</p>
```

Cela rend clair pour le lecteur que la section sur "la confidentialité des données" a été récemment ajoutée.

Dans le développement de logiciels ou la gestion de contenu, vous pourriez utiliser la balise `<ins>` pour montrer le texte qui a été nouvellement introduit dans des fichiers sous contrôle de version, facilitant le suivi des modifications et des révisions au fil du temps.

### Options de style pour mettre en évidence les modifications

L'apparence par défaut de la balise `<ins>` est soulignée, mais vous pouvez la personnaliser en utilisant CSS pour une meilleure emphase, surtout si vous souhaitez que les modifications se démarquent davantage.

Voici comment vous pouvez styliser la balise `<ins>` avec différents effets visuels :

```css
ins {
  background-color: #d4edda;
  color: green;
  text-decoration: none; /* Supprime le soulignement par défaut */
}
```

Cela donnera au texte inséré une couleur verte et un fond vert clair, le rendant plus visible.

%[https://codepen.io/joanayebola/pen/wvVgWRz] 

Vous pouvez également ajouter différents styles comme une police en gras ou une bordure :

```css
ins {
  font-weight: bold;
  border-bottom: 2px solid green;
}
```

Ces options de style facilitent l'identification par les utilisateurs de ce qui a été ajouté ou modifié, améliorant la lisibilité et la transparence des modifications de documents.

Dans l'ensemble, la balise `<ins>` est un moyen simple mais efficace de suivre le contenu inséré, ce qui la rend très utile pour les documents techniques et les plateformes collaboratives où les révisions doivent être clairement visibles.

## La balise `<del>` : Texte supprimé

La balise `<del>` est utilisée pour montrer le texte qui a été supprimé ou retiré d'un document. Cette balise barre le texte par défaut, ce qui facilite l'identification de ce qui a été supprimé. Elle est particulièrement utile dans les situations où le suivi des modifications ou des révisions est nécessaire.

### Objectif et utilisation de la balise `<del>` pour le texte barré

Le principal rôle de la balise `<del>` est de montrer visuellement qu'un certain contenu a été supprimé. Elle est courante dans les documents, les articles ou le code où les modifications doivent être rendues visibles pour le lecteur. Le texte supprimé aura généralement un barré, indiquant qu'il n'est plus pertinent ou valide.

Exemple :

```html
<p>Ce produit coûte <del>50 $</del> 40 $ maintenant.</p>
```

Dans cet exemple, le changement de prix est clair. L'ancien prix (50 $) est barré, et le nouveau prix (40 $) suit immédiatement après.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1728749690070/6c971036-90b9-4bcb-9d74-1c13bd770750.png align="center")

### Comment elle peut être combinée avec `<ins>` pour suivre les révisions

La balise `<del>` peut être associée à la balise `<ins>` pour montrer à la fois le contenu supprimé et le contenu nouvellement ajouté, ce qui la rend parfaite pour suivre les modifications ou les révisions. Cela est très utile dans l'écriture collaborative, les documents juridiques ou toute situation où les modifications doivent être enregistrées clairement.

Exemple de suivi des révisions :

```html
<p>La réunion a été déplacée <del>lundi</del> <ins>mardi</ins>.</p>
```

Ici, il est facile de voir que "lundi" a été remplacé par "mardi", et le lecteur sait exactement ce qui a changé.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1728749828530/ee3f84d5-9e56-4f27-8ce3-6eac5a79a144.png align="center")

### Bonnes pratiques pour afficher et styliser le contenu supprimé

Par défaut, la balise `<del>` applique un barré au texte, mais vous pouvez le styliser davantage avec CSS pour le rendre plus visible ou pour répondre à vos besoins de design.

Voici un exemple de personnalisation de l'apparence du texte supprimé :

```css
del {
  color: red;
  text-decoration: line-through;
}
```

Cela fait apparaître le texte supprimé en rouge, attirant plus d'attention. Vous pouvez également le combiner avec un formatage supplémentaire, comme estomper le texte :

```css
del {
  color: gray;
  opacity: 0.7;
}
```

Ce style réduit l'emphase sur le contenu supprimé, le rendant moins distractif mais toujours visible pour les lecteurs.

%[https://codepen.io/joanayebola/pen/xxvgWNQ] 

La balise `<del>` offre un moyen simple et efficace de suivre et d'afficher les modifications, surtout lorsqu'elle est combinée avec la balise `<ins>`. Elle est essentielle pour garder les documents transparents et clairs pour quiconque examine les modifications ou les mises à jour.

## Conclusion

L'utilisation de ces éléments HTML uniques élargit les possibilités sur le web, ce qui aide à créer un contenu plus significatif et accessible. Des balises comme `<q>`, `<s>`, `<mark>`, `<ruby>`, `<time>`, `<bdi>`, `<dfn>`, `<wbr>`, `<ins>`, et `<del>` apportent chacune leurs propres avantages pour des tâches spécifiques. Ces éléments font plus que simplement styliser le texte ; ils ajoutent du contexte, améliorent les expériences utilisateur et améliorent la structure des documents.

L'utilisation correcte de ces balises rend non seulement vos pages web plus claires, mais améliore également la compatibilité entre les appareils et les moteurs de recherche. En appliquant ces éléments, réfléchissez à la manière dont chacun sert à la fois la présentation visuelle et la structure de l'information. Ils offrent des moyens simples mais puissants de rendre les sites web plus riches et plus faciles à comprendre, tout en bénéficiant à un large éventail d'utilisateurs.

Si vous avez des questions ou des suggestions, n'hésitez pas à me contacter sur [LinkedIn](https://ng.linkedin.com/in/joan-ayebola). Si vous avez apprécié ce contenu, envisagez de [m'offrir un café](https://www.buymeacoffee.com/joanayebola) pour soutenir la création de plus de contenus adaptés aux développeurs.