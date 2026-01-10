---
title: Qu'est-ce que la dette technique ? Et pourquoi presque toutes les startups
  en ont-elles ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-16T06:49:12.000Z'
originalURL: https://freecodecamp.org/news/what-is-technical-debt-and-why-do-most-startups-have-it-9a54458daabf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BefRx92AZqpvYnK8qbQekw.jpeg
tags:
- name: Entrepreneurship
  slug: entrepreneurship
- name: Life lessons
  slug: life-lessons
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Qu'est-ce que la dette technique ? Et pourquoi presque toutes les startups
  en ont-elles ?
seo_desc: 'By Trey Huffine

  Technical debt is any code added now that will take more work to fix at a later
  time — typically with the purpose of achieving rapid gains.

  Learn how to code with programming tutorials on gitconnected.com &gt;

  But what does that mean?...'
---

Par Trey Huffine

La dette technique est tout code ajouté maintenant qui nécessitera plus de travail pour être corrigé ultérieurement — généralement dans le but d'obtenir des gains rapides.

[**Apprenez à coder avec des tutoriels de programmation sur gitconnected.com &**](https://gitconnected.com/learn)gt;

Mais qu'est-ce que cela signifie ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*mOkmsSxjdGpDd1EHQqdB8Q.jpeg)

La dette technique est comme tout autre type de dette. Comparons-la à l'achat d'une maison. La plupart des gens n'ont pas des centaines de milliers de dollars en banque pour acheter une maison. Ainsi, les gens contractent un prêt hypothécaire. Les acheteurs doivent le rembourser au cours des 15 à 30 prochaines années avec des intérêts ajoutés. Si les acheteurs ne paient pas leur hypothèque à temps, ils perdent leur maison.

La dette technique n'est pas différente. Elle permet aux entreprises de créer des logiciels plus rapidement, en sachant qu'elles ralentiront le développement logiciel à l'avenir. Les entreprises seront finalement contraintes de passer plus de temps à corriger la dette que le temps qu'il leur a fallu pour produire la meilleure solution au début.

La solution optimale à tout problème de génie logiciel nécessite généralement un investissement important au départ. Il faut plus de temps pour écrire du code sans obtenir de résultats, et cela est fait avant que les résultats robustes et évolutifs ne soient réellement réalisés.

La dette technique peut créer une expérience éprouvante pour les développeurs et entraver l'évolutivité à long terme. Mais presque toutes les startups contractent une dette technique. Beaucoup l'utilisent comme catalyseur pour une croissance à court terme. La dette technique n'est donc pas toujours une mauvaise chose.

[**Coding News for Developers | gitconnected**](https://gitconnected.com)  
[_La page d'accueil des développeurs - rejoignez la communauté de programmation de gitconnected. Découvrez et partagez des actualités sur le code, avec...gitconnected.com](https://gitconnected.com)

### Comment savoir si quelque chose est en dette technique

La dette technique n'est pas seulement un concept abstrait. Elle peut être expliquée en termes concrets et représentée graphiquement. Une excellente analogie (ne m'en voulez pas pour celle-ci) est la [complexité algorithmique Big O](https://stackoverflow.com/questions/487258/what-is-a-plain-english-explanation-of-big-o-notation). À mesure que la taille d'une base de code augmente, nous pouvons mesurer l'effort requis pour ajouter de nouvelles fonctionnalités et/ou du code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6U_NG4w6g6YYyxPyG9Io_g.png)

Tout ce qui se trouve au-dessus de la ligne linéaire bleue O(n) est de la dette technique, et tout ce qui se trouve en dessous n'en est pas. Cela signifie que la dette technique rend l'écriture de code de plus en plus difficile à mesure que du code est ajouté.

Les solutions évolutives sous la ligne bleue sont généralement des abstractions, des bibliothèques et des outils qui facilitent la construction de logiciels. Les exemples peuvent aller de la création de fonctionnalités spécifiques à l'application comme des tableaux de bord internes à l'utilisation de bibliothèques et d'outils comme React ou Docker (imaginez à quel point il serait pénible de les reconstruire pour chaque projet). Les bons outils et abstractions peuvent agir comme des multiplicateurs d'impact, tandis que la dette technique est un diviseur d'impact.

Comme le montre le graphique, la dette technique peut initialement être la voie optimale, mais elle doit être refactorisée rapidement si la fonctionnalité de l'application doit réussir. Cela soutient le concept de startup consistant à lancer des idées rapidement sous forme de MVP, puis à les itérer et à les améliorer rapidement.

Déterminez d'abord quelles idées ont suscité de l'intérêt, puis construisez-les de manière itérative afin qu'elles puissent devenir évolutives. Une fonctionnalité peut être lancée en imposant une complexité `O(n²)` à la base de code (dette technique), mais peut être refactorisée en `O(n)` et `O(log n)` au fil du temps. Le `O(log n)` permet à une personne ou à une petite équipe de produire le même résultat qu'une équipe plus importante construisant de manière brute.

Après avoir atteint une taille d'entreprise et de base de code suffisante, vous avez atteint un point que j'ai défini comme le seuil d'évolutivité. À ce stade, les outils que vous avez construits par rapport à la récompense qu'ils rapportent nécessitent moins d'effort que l'approche linéaire. Vous ne devriez plus construire sur l'approche linéaire après avoir franchi ce seuil. Au lieu de cela, investissez dans du code qui vous permettra de produire plus de résultats tout en nécessitant moins de personnes et moins d'efforts.

Theoriquement, la solution linéaire `O(n)` n'est pas une dette technique. Pour chaque heure-homme supplémentaire que vous ajoutez, vous recevrez un gain équivalent. Cependant, cela ne fonctionne pas toujours en pratique. Le temps, l'argent et la volonté humaine sont des ressources limitées. Vous finirez par atteindre une limite au nombre de personnes que vous pouvez embaucher. Et l'épuisement professionnel des travailleurs sur des tâches répétitives est une réelle préoccupation. Les solutions logicielles qui semblent évoluer linéairement deviennent de la dette technique lorsqu'elles nécessitent des personnes pour les construire.

### Un exemple concret

Imaginez que vous construisez un nouveau service révolutionnaire, appelé Citybrook, qui crée des profils pour les villes. Identifiez cinq marchés clés qui vous intéressent, disons San Francisco, Seattle, Austin, New York et Nashville. Créez quelques pages web simples en utilisant du HTML et du CSS pur, puis trouvez une adéquation pour le produit sur le marché.

Supposons que les utilisateurs adorent le contenu. Toutes les villes des États-Unis vous supplient de créer des pages pour elles. Vous réalisez également que votre facture Amazon Web Services (AWS) va monter en flèche à cause de tout le trafic que vous recevez. Vous commencez donc à placer des publicités sur chaque page web en collant des liens pour différents marchands pour les différentes villes. Vous réalisez rapidement que la solution HTML simple ne va pas passer à l'échelle. C'est une complexité `O(n²)` car vous ne pouvez pas raisonnablement construire et maintenir une page HTML avec un contenu unique pour chaque ville.

Pour résoudre ce problème, vous utilisez [React](https://reactjs.org/) pour créer des templates pour vos pages et pour rendre du contenu dynamique. À ce stade, vous avez réduit la dette technique et rendu plus faisable l'évolution de votre entreprise. Vous pouvez maintenant allouer du temps à la génération de contenu plutôt qu'à la construction d'une page unique pour chaque ville.

Vous travaillez de longues heures avec votre équipe, dans le but de créer un profil pour chaque ville en quelques mois. Cependant, vous êtes devenu victime de votre propre succès. Des concurrents dans d'autres pays commencent à lancer leurs sites web, mais vous n'avez pas la capacité de vous étendre.

Au lieu de cela, vous essayez d'embaucher rapidement, mais vous ne pouvez pas suivre le rythme. Certaines villes demandent que leur contenu soit modifié, mais les annonceurs ne peuvent pas se permettre vos tarifs avec l'augmentation du trafic, leurs publicités doivent donc être remplacées. Créer et mettre à jour manuellement le profil de chaque ville n'a plus de sens. Il n'y a tout simplement pas assez de main-d'œuvre pour suivre l'échelle.

Ainsi, vous décidez de construire un tableau de bord pour permettre aux villes de créer et de mettre à jour leurs propres pages. Le nombre total de profils sur le site cesse temporairement de croître pendant le développement, mais compte tenu de votre popularité, vous ne perdez aucun client. Une fois terminé, l'ajout d'une nouvelle ville ne nécessite qu'un effort minimal. Au lieu de passer de nombreuses heures à rédiger du contenu, votre équipe n'a plus qu'à maintenir et construire l'outil pour donner de l'autonomie à vos clients.

Plus votre équipe s'agrandit, plus vous avez la capacité (et l'obligation) d'écrire du code blindé et de rembourser la dette technique qui vous a permis d'atteindre la taille que vous avez atteinte.

La dette technique multiplie les autres dettes techniques. Construire sur de la dette technique et/ou ajouter plus de dette provoque généralement une croissance exponentielle du mauvais code. Cela signifie que l'ajout de nouvelles fonctionnalités rend de plus en plus difficile le remboursement de la dette.

### Quand la dette technique est-elle acceptable ?

Les clients ne se soucient pas de l'apparence de votre code. Ils veulent juste votre produit. Une seule fonctionnalité parfaite qui n'a jamais été publiée et qui a échoué ne vaut rien par rapport à une startup bricolée qui possède une poignée de fonctionnalités vers lesquelles les utilisateurs gravitent.

Cette startup florissante peut ensuite itérer sur les fonctionnalités qui suscitent de l'intérêt et les affiner pour qu'elles deviennent plus évolutives. Une fois que la startup bricolée rencontre le succès, elle peut alors constituer son équipe d'ingénierie et rembourser la dette technique. Cela les positionnera pour un succès futur.

Le rendement de la dette technique doit être supérieur à la dette elle-même. C'est-à-dire que quoi que ce soit que vous soyez capable d'accomplir en acquérant la dette, cela doit avoir un impact plus grand que la dette elle-même.

La dette technique n'est pas une excuse pour être paresseux. Elle doit être utilisée tactiquement avec une vision à long terme en tête. Les startups doivent avancer rapidement et tester leurs idées sur le marché. Une fois qu'elles ont validé une idée, elles doivent chercher à comprendre le problème et les abstractions appropriées pour la mettre à l'échelle. Les entreprises doivent ensuite rembourser leur dette technique.

Contrairement à la croyance populaire, acquérir une dette technique peut en fait être la décision optimale dans de nombreux cas. La devise de Facebook pendant plusieurs années était "move fast and break things" (allez vite et cassez des choses).

L'[acquisition d'une dette technique](https://www.reddit.com/r/programming/comments/3r90iy/facebooks_code_quality_problem/) est un facteur énorme dans le fait que Facebook soit devenu le mastodonte qu'il est aujourd'hui. Mais cela pose aussi un problème dans la mesure où Facebook est difficile à maintenir à son échelle. La raison pour laquelle cela a fonctionné est qu'ils ont pu évoluer plus rapidement que la dette qu'ils ont acquise.

Ne contractez pas de dette technique pour le plaisir de le faire. Il faut de l'expérience, des erreurs et de la communication pour garder la dette technique sur la bonne voie. Cependant, comprenez que la gérer correctement peut être un puissant catalyseur de croissance. Souvent, la dette technique est la meilleure voie à suivre. Jusqu'à ce qu'elle ne le soit plus.

À ce stade, elle peut devenir le plus grand obstacle au progrès.

Comprenez-la, contrôlez-la et utilisez-la comme un outil, et elle vous aidera à bâtir votre startup.

_Si vous trouvez cet article utile, n'hésitez pas à cliquer sur_ ?. _S[uivez-moi](https://medium.com/@treyhuffine) pour plus d'articles sur React, Node.js, JavaScript et les logiciels open source. Vous pouvez également me trouver sur T[witter](https://twitter.com/treyhuffine) ou g[itconnected.](https://gitconnected.com/treyhuffine)_

[**gitconnected - La communauté pour les développeurs et les ingénieurs logiciels**](https://gitconnected.com)  
[_Rejoignez le seul réseau conçu pour les développeurs. Affichez votre portfolio, participez à des discussions et publiez des actualités tendances._gitconnected.com](https://gitconnected.com)