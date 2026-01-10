---
title: Guide du débutant pour l'optimisation de site web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-08T09:48:26.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-website-optimization-2185edca0b72
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xNt4aprSuOo2bdYg9F-6gw.jpeg
tags:
- name: Productivity
  slug: productivity
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Guide du débutant pour l'optimisation de site web
seo_desc: 'By Mario Hoyos

  I am a beginner, and I was able to achieve 99/100 in Google’s optimization ranking.
  If I can do it, you can too.

  If you’re like me, you like proof. So here are Google’s PageSpeed Insights results
  for hasslefreebeats, a website that I m...'
---

Par Mario Hoyos

Je suis un débutant, et j'ai réussi à obtenir 99/100 dans le classement d'optimisation de Google. Si j'ai pu le faire, vous le pouvez aussi.

Si vous êtes comme moi, vous aimez les preuves. Voici donc les résultats de [Google PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/) pour [hasslefreebeats](https://www.hasslefreebeats.com), un site web que je maintens et sur lequel j'ai récemment passé du temps à optimiser :

![Image](https://cdn-media-1.freecodecamp.org/images/zezZUe60TuNoOV7BQOmSolQoXAmdjqYXyr8Q)
_Une capture d'écran de mon score PageSpeed Insights._

Je suis assez fier de ces résultats, mais je tiens à souligner que je n'avais aucune idée de la façon d'optimiser un site web il y a seulement quelques semaines. Ce que je partage avec vous aujourd'hui est simplement le résultat de nombreuses recherches sur Google et de dépannages, des efforts que je souhaite vous épargner.

Cet article est divisé en sous-sections pour chaque optimisation, au cas où vous souhaiteriez sauter d'une section à l'autre.

Je ne suis en aucun cas un expert, mais je suis convaincu que si vous mettez en œuvre les techniques ci-dessous, vous verrez des résultats !

### Images

![Image](https://cdn-media-1.freecodecamp.org/images/OVVkYdYxj4rUdLyXLdX0fYA6tOCXO226f5cB)
_Image fournie par Pexels (et sûrement optimisée par Medium)._

En tant que développeur web débutant, les images n'étaient pas quelque chose à quoi je prêtais beaucoup d'attention. Je savais que l'ajout d'images de haute qualité à mon site web le rendrait plus professionnel, mais je ne me suis jamais arrêté pour considérer les effets qu'elles auraient sur le temps de chargement de ma page.

La principale chose que j'ai faite pour optimiser mes images a été de les compresser.

En y repensant, cela aurait dû être assez intuitif dès le départ, mais ce ne l'était pas pour moi, donc peut-être que ce ne l'est pas pour vous non plus.

Le service que j'ai utilisé pour compresser mes images était [Optimizilla](http://optimizilla.com/), un site web facile à utiliser où vous téléchargez vos images, sélectionnez le niveau de compression que vous souhaitez, puis téléchargez l'image compressée. J'ai vu des réductions de taille allant jusqu'à 70 % pour certaines de mes ressources, ce qui contribue grandement à des temps de chargement plus rapides.

Optimizilla est loin d'être le seul choix pour vos besoins de compression d'images. Certains logiciels open-source autonomes que vous pouvez utiliser sont [ImageOptim](https://imageoptim.com/mac) pour Mac ou [FileOptimizer](https://sourceforge.net/projects/nikkhokkho/files/FileOptimizer/) pour Windows. Si vous préférez compresser en utilisant des outils de construction, il existe des plugins [Gulp](https://www.npmjs.com/package/gulp-imagemin) et [WebPack](https://github.com/Klathmon/imagemin-webpack-plugin) qui devraient faire l'affaire. Peu importe la manière dont vous le faites, tant que vous le faites. Les gains de performance valent bien l'effort minimal.

Selon votre cas d'utilisation, il peut également être utile de regarder le format de vos fichiers. En général, le jpg sera plus petit que le png. La principale différence dans le choix de l'un ou de l'autre est de savoir si j'ai besoin de transparence derrière l'image : si j'ai besoin de transparence, j'utilise le png, sinon j'utilise le jpg. Vous pouvez approfondir les avantages et les inconvénients des deux [ici.](https://www.digitaltrends.com/photography/jpeg-vs-png-photo-format/)

De plus, Google a sorti un format webp qui est assez génial, mais comme il n'est pas encore supporté sur tous les navigateurs, je suis hésitant à l'utiliser. Restez à l'affût pour un support supplémentaire à l'avenir !

Je n'ai pas fait plus que compresser mes images pour obtenir les résultats que je vous ai montrés ci-dessus, mais si vous voulez optimiser davantage [voici un excellent article.](https://www.frontamentals.com/practical-guide-to-images)

### Vidéo

![Image](https://cdn-media-1.freecodecamp.org/images/pyCjB8NJV7cWOJ3rtxEKW0YsrrmW0icWFHvf)
_Photo par Terje Sollie de Pexels._

Je n'ai pas utilisé de vidéo dans aucun de mes projets actuels, donc je ne vais aborder ce sujet que brièvement car je ne me sens pas être la meilleure ressource pour cela, spécifiquement.

C'est l'une de ces situations où je laisserais probablement les professionnels faire le gros du travail. [Vimeo](http://Mock interview outline    background of company        What we do            — Match                                                                      What we're looking for            Entry level dev who can jump in and go to work            Quick learner            excited to build clean code    tell me about yourself        education        experience        tech stack familiarity            Go over each main piece of tech and ask about comfort and             familiarity with each piece        How do you stay up to date on new technologies?        What new technologies are you currently learning?        1. Tell me about the most recent project you worked on. What                 were your responsibilities?        2. What is semantic html?        3. What is the box model in css?            What CSS frameworks/libraries have you used?        4. What is the keyword 'this' used for?        5. What is a callback?        6. How do promises work in JavaScript?        7. What is a closure?        8. What is the prototype on objects?        9. What is rest?        1. Describe the react lifecycle        2. What is redux and why would we use it?     Whiteboarding Problem        Write a function that takes in a multi-dimensional array, finds the average of each array in the collection, and returns the sum of the averages.        What are your salary requirements?        What questions do you have for me?   At end of interviews, talk about JavaScript Fundamentals and using flash cards or something to remember and train on the concepts. Have enough know to give high level definition of concept, then enough in your pocket to give more including examples  Do you know what it is What's an example) offre une excellente plateforme pour héberger des vidéos où ils dégradent la qualité vidéo pour les connexions plus lentes et compressent vos vidéos pour optimiser les performances.

Vous pourriez également héberger vos vidéos sur YouTube et ensuite utiliser cet outil [youtube-dl](https://rg3.github.io/youtube-dl/) pour les télécharger depuis YouTube tout en configurant les vidéos selon les besoins de votre site web.

Pour d'autres solutions possibles, consultez [Brightcove](https://www.brightcove.com/en/), [Sprout](https://sproutvideo.com/) ou [Wistia](https://wistia.com/).

### Gzip

![Image](https://cdn-media-1.freecodecamp.org/images/IRfWI4Cv-mN4go0roOEw2pPR3VlCvCFmkONT)
_Comprenez-vous ? Zip ? Image fournie par Pexels._

Je n'avais aucune idée de ce qu'était le gzipping lorsque j'ai initialement déployé mon site web.

En bref, gzip est un format de compression de fichiers que la plupart des navigateurs comprennent et qui peut fonctionner en arrière-plan sans que l'utilisateur ait besoin de savoir que cela se produit.

Selon l'endroit où vous hébergez votre application, le gzipping peut être aussi simple que d'activer une option de configuration pour spécifier que vous souhaitez que votre serveur gzip les fichiers lorsqu'il les envoie. Dans mon cas, mon site web est hébergé sur Heroku, qui ne fournit pas cette option.

Il s'avère qu'il existe des packages pour ajouter explicitement la compression dans votre code serveur, ce qui vous permet de profiter des avantages du gzipping en échange de quelques lignes de code. En utilisant [ce](https://github.com/expressjs/compression) middleware de compression, [j'ai pu réduire la taille de mes bundles Javascript et CSS de 75%.](https://codeburst.io/how-i-decreased-the-size-of-my-heroku-app-by-75-1a4cf329b0ab)

Il est utile de vérifier si votre service d'hébergement propose une option gzip. Si ce n'est pas le cas, renseignez-vous sur la façon d'ajouter le gzipping à votre code côté serveur.

### Minification

![Image](https://cdn-media-1.freecodecamp.org/images/HEgC7zdae1AigTekOi6h4gLJvL5jsikRl4mH)
_Ananas minifié fourni par Pexels._

La minification est le processus de suppression des caractères inutiles du code sans affecter sa fonctionnalité (espaces blancs, caractères de nouvelle ligne, etc.). Cela vous permet de réduire la taille du fichier que vous transportez sur Internet. C'est également utile pour obfuscater votre code, ce qui rend plus difficile pour les pirates rusés de détecter les points faibles de la sécurité.

De nos jours, la minification est généralement effectuée dans le cadre du processus de construction avec Webpack ou Gulp ou une alternative. Ces outils de construction peuvent avoir une courbe d'apprentissage, cependant, donc si vous cherchez des alternatives plus faciles, Google recommande [HTML-Minifier pour HTML](https://github.com/kangax/html-minifier), [CSSNano pour CSS](https://github.com/ben-eb/cssnano), et [UglifyJS pour Javascript](https://github.com/mishoo/UglifyJS2).

### Mise en cache du navigateur

![Image](https://cdn-media-1.freecodecamp.org/images/zdsoMOxhnEdxS8Dqk66AcOM50hLjIyZdUYiv)
_Pas tout à fait comment le navigateur stocke les données, mais c'est aussi proche que j'ai pu obtenir. Fournie par Pexels._

Stocker des fichiers statiques dans le cache du navigateur est un moyen très efficace d'augmenter la vitesse de votre site web, surtout lors des visites répétées du même client. Je n'étais pas au courant, jusqu'à ce que Google me le dise, que certaines de mes ressources n'étaient pas mises en cache correctement en raison de l'absence d'en-têtes dans la réponse HTTP que j'envoyais depuis mon serveur.

Dès que ma page d'accueil est chargée, une requête est envoyée à mon serveur pour obtenir des données sur un tas de chansons qui sont ensuite rendues dans un lecteur de musique. Je ne mets pas souvent à jour les chansons sur ce site web, donc cela ne me dérange pas qu'un utilisateur vienne sur mon site web et voie les mêmes chansons que la dernière fois qu'il a visité, si cela peut rendre ma page un peu plus rapide pour lui.

Pour obtenir un gain de performance, j'ai ajouté le code suivant à l'objet de réponse de mon serveur (serveur Express/Node) :

```
res.append("Cache-Control", "max-age=604800000");
```

```
res.status(200).json(response);
```

Tout ce que je fais ici est d'ajouter un en-tête de contrôle de cache à ma réponse, qui indique qu'après une semaine (en millisecondes), les ressources doivent être retéléchargées. Si vous mettez à jour ces fichiers plus souvent, un max-age plus court pourrait être une bonne idée.

### **Réseau de distribution de contenu**

![Image](https://cdn-media-1.freecodecamp.org/images/uDwV3cw6CCHGF9gi2ifn6F5fAtjNxIeCCPOm)
_Image réelle d'un CDN, fournie par Pexels._

Un réseau de distribution de contenu, ou CDN, est un réseau qui permet aux utilisateurs du monde entier d'être géographiquement plus proches de votre contenu. Si un utilisateur doit charger une grande image depuis le Japon, mais que votre serveur est aux États-Unis, cela prendra plus de temps que si vous aviez un serveur à Tokyo.

Un CDN vous permet de tirer parti d'un tas de serveurs proxy situés dans le monde entier, permettant à votre contenu d'être chargé plus rapidement, peu importe où se trouve votre utilisateur final.

Je tiens à noter que j'ai pu obtenir les résultats que vous avez vus ci-dessus **avant** de mettre en œuvre un CDN — je voulais simplement les mentionner car aucun article sur l'optimisation de site web ne serait complet sans les mentionner. Avoir l'un de ces outils sur votre site web est impératif si vous prévoyez d'avoir un public mondial.

Certains CDN populaires incluent [CloudFront](https://aws.amazon.com/cloudfront/) et [CloudFlare](https://www.cloudflare.com/lp/ddos-a/?_bt=157293179478&_bk=cloudflare&_bm=e&_bn=g&gclid=CjwKCAiA_c7UBRAjEiwApCZi8Ri3kAEt3UraYPUFUQOMTG0Xz7WGCNRUri0UNtCOUAdUMJI8osxuDRoCTx8QAvD_BwE).

### Divers

Voici quelques conseils supplémentaires pour tirer encore plus de jus :

* Optimisez votre site web pour charger le contenu "above-the-fold" en premier afin d'augmenter la performance perçue de votre site. Une méthode courante pour cela est le [lazy-loading](https://en.wikipedia.org/wiki/Lazy_loading) des images qui n'apparaissent pas sur la page de destination.
* À moins que votre application ne dépende de JavaScript pour rendre le HTML, comme un site web construit avec Angular ou React, il est probablement sûr de charger vos balises de script en bas de la section body de votre fichier HTML. Cela pourrait affecter votre [time-to-interactive](https://developers.google.com/web/tools/lighthouse/audits/time-to-interactive), cependant, donc ce n'est PAS une technique que je recommanderais pour toutes les situations.

### En conclusion

Ce n'est que la partie émergée de l'iceberg en matière d'optimisation de votre site web. Selon la quantité de trafic que vous recevez et le service que vous fournissez, vous pourriez avoir des goulots d'étranglement de performance dans de nombreux domaines différents. Peut-être avez-vous besoin de plus de serveurs, peut-être avez-vous besoin d'un serveur avec plus de RAM, peut-être que votre triple boucle for imbriquée pourrait utiliser un peu de refactoring — qui sait ?

Il n'existe pas de solution universelle pour accélérer votre site, et vous devrez finalement prendre les meilleures décisions pour votre situation en fonction des mesures. Ne perdez pas votre temps à optimiser quelque chose qui n'a pas besoin d'être optimisé. Analysez la performance de votre site pour trouver les goulots d'étranglement, puis attaquez ceux-ci spécifiquement.

J'espère que vous avez trouvé quelque chose d'utile dans cet article ! Comme je l'ai mentionné, j'ai encore beaucoup à apprendre dans ce domaine. Si vous avez des conseils ou des recommandations supplémentaires, n'hésitez pas à les laisser dans les commentaires ci-dessous !

Si vous avez aimé cet article, n'hésitez pas à l'applaudir et à consulter :

* [Outils que j'aurais aimé connaître lorsque j'ai commencé à coder](https://medium.freecodecamp.org/tools-i-wish-i-had-known-about-when-i-started-coding-57849efd9248)
* [Outils que j'aurais aimé connaître lorsque j'ai commencé à coder : Revisité](https://medium.freecodecamp.org/tools-i-wish-i-had-known-about-when-i-started-coding-revisited-ffb715ffd23f)

De plus, suivez-moi sur [Twitter](https://twitter.com/marioahoyos).