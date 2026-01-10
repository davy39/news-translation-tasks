---
title: Meilleures pratiques éprouvées pour la révision de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-24T07:39:00.000Z'
originalURL: https://freecodecamp.org/news/proven-code-review-best-practices
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/Code-Review-Best-Practice-2.png
tags:
- name: code review
  slug: code-review
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: Meilleures pratiques éprouvées pour la révision de code
seo_desc: 'By Michaela Greiler

  What are the code review best practices companies such as Microsoft follow to  ensure
  great code review feedback? How do you stay productive while doing code reviews?
  Learn proven code review best practices from Microsoft in this ...'
---

Par Michaela Greiler

Quelles sont les meilleures pratiques de révision de code suivies par des entreprises comme Microsoft pour garantir un [retour de qualité sur les révisions de code](https://www.michaelagreiler.com/great-code-review-feedback/) ? Comment rester productif tout en effectuant des révisions de code ? Découvrez les meilleures pratiques éprouvées de révision de code de Microsoft dans cet article.

Les avantages des révisions de code dépendent de la qualité des retours. Si elles sont bien menées, les révisions de code peuvent aider à maintenir une base de code de haute qualité. Cependant, si les équipes ne connaissent pas ou ne suivent pas les meilleures pratiques de révision de code, les développeurs peuvent rencontrer plusieurs [pièges courants](https://www.michaelagreiler.com/code-review-pitfalls-slow-down/). Dans le pire des cas, [la révision de code peut ralentir votre équipe](https://www.michaelagreiler.com/wp-content/uploads/2019/02/Code-Reviews-Do-Not-Find-Bugs.-How-the-Current-Code-Review-Best-Practice-Slows-Us-Down.pdf).

Je mène des recherches et travaille avec des équipes chez Microsoft depuis plusieurs années. Grâce à [plusieurs études à grande échelle](https://www.michaelagreiler.com/publications/), nous avons découvert un certain nombre de meilleures pratiques pour les révisions de code qui aident les équipes à rester productives et à [améliorer la valeur de leurs révisions](https://www.michaelagreiler.com/great-code-review-feedback/). Mais d'abord, commençons par le commencement. À quoi ressemble une révision de code ?

### Un processus typique de révision de code

Un [processus typique de révision de code basé sur des outils](https://www.michaelagreiler.com/code-reviews-at-microsoft-how-to-code-review-at-a-large-software-company/) commence lorsque l'ingénieur prépare le code pour la révision. Ensuite, il sélectionne les relecteurs pertinents pour les modifications apportées. Les relecteurs sont notifiés et donnent leur avis sur le code. L'auteur de la révision travaille sur les retours jusqu'à ce que toutes les parties soient satisfaites. Ensuite, le code est intégré à la base de code commune.

![Image](https://cdn-media-1.freecodecamp.org/images/0*ZOAaTZc1Z6XEK3Ri)

_Une révision de code typique basée sur des outils_

Pour que ce processus se déroule sans accroc et ne devienne pas un cauchemar, il est important de [comprendre les pièges des révisions de code](https://www.michaelagreiler.com/code-review-pitfalls-slow-down/) et quelles meilleures pratiques suivre pour les éviter.

Les principaux pièges des révisions de code sont :

* ne pas recevoir de retours utiles,
* ne pas avoir assez de temps pour effectuer des révisions de code,
* des révisions de code trop longues entraînant des temps d'attente excessifs.

Les meilleures pratiques de révision de code que je présente ci-dessous aident à contrer ces pièges en facilitant au maximum le travail des relecteurs. Elles aident également les relecteurs à se concentrer sur la fourniture de retours précieux.

### Meilleures pratiques pour les auteurs de code

Dans une révision de code, il y a deux parties prenantes différentes : l'auteur du code qui demande un retour et les relecteurs de code, qui examinent les modifications et fournissent des retours. Comme une révision de code commence avec l'auteur, je vais d'abord expliquer les meilleures pratiques pour les auteurs de code.

Pour mes abonnés par e-mail, j'ai préparé un **e-book exclusif sur la révision de code** incluant une checklist avec toutes les meilleures pratiques. J'ai également ajouté des insights bonus. Vous pouvez demander le [Code Review e-Book ici](https://www.michaelagreiler.com/code-review-e-book/).

### Lire attentivement les modifications

La première meilleure pratique est de lire attentivement les modifications de code avant de les soumettre pour révision. Il n'y a rien de pire que de demander à plusieurs développeurs d'examiner le code et de donner des retours sur des problèmes que vous auriez pu corriger vous-même.

Cela fait perdre du temps à tout le monde et cela peut vous donner une mauvaise image. Pour les futures révisions de code, les développeurs pourraient également être réticents à examiner votre code.

Assurez-vous donc d'utiliser un outil de révision de code ou un outil de diff qui peut mettre en évidence ce qui a changé entre cette version et la précédente. Comme le code est présenté différemment et que les passages modifiés sont mis en évidence, cela vous facilite la tâche pour réviser votre code vous-même avant de l'envoyer.

Souvent, vous verrez des changements que vous aviez oubliés ou des problèmes manquants mis en évidence que vous devriez corriger avant de demander à quelqu'un de les réviser.

[Le meilleur moment pour corriger les problèmes est avant que le code ne soit envoyé pour révision. (Cliquez pour tweeter).](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-pitfalls-slow-down/&text=Le%20meilleur%20moment%20pour%20corriger%20les%20problèmes%20est%20avant%20que%20le%20code%20ne%20soit%20envoyé%20pour%20révision.%20&via=mgreiler&related=mgreiler)

![Image](https://cdn-media-1.freecodecamp.org/images/1*dvvMg-MkjhWYFzbM-Rpekw.jpeg)

_Examinez attentivement votre code avant de le soumettre pour révision (Photo par [Marten Newhall](https://unsplash.com/photos/uAFjFsMS3YY?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/search/photos/magnifier?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText))_

### Visitez des changements petits et incrémentaux

En tant que développeur, vous devez toujours viser des changements petits, incrémentaux et cohérents. Cette meilleure pratique est utile lorsque vous travaillez avec des outils de contrôle de version, tels que git ou SVN.

Les petits changements de code incrémentaux sont également une pratique essentielle de révision de code, car les autres développeurs doivent pouvoir comprendre vos modifications en peu de temps.

_10 lignes de code = 10 problèmes._

_500 lignes de code = « ça a l'air bien. »_

_Révisions de code._

_- I Am Devloper (@iamdevloper)_ [_5 novembre 2013_](https://twitter.com/iamdevloper/status/397664295875805184?ref_src=twsrc%5Etfw)

Si plusieurs changements avec des objectifs différents se produisent dans une seule révision de code, [la tâche de révision de code devient plus difficile](https://www.michaelagreiler.com/code-review-pitfalls-slow-down/). Cela diminue également la capacité des relecteurs de code à repérer les problèmes. Dans plusieurs études, nous voyons que la valeur des retours de révision de code diminue avec la taille des modifications examinées.

D'un autre côté, vous voulez également vous assurer que les modifications sont cohérentes. Rarement, les modifications de code sont trop petites pour être envoyées. Cela arrive, mais pas souvent.

[La qualité et la valeur des retours de révision de code diminuent avec la taille des modifications. (Cliquez pour tweeter).](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-best-practices/&text=La%20qualité%20et%20la%20valeur%20des%20retours%20de%20révision%20de%20code%20diminuent%20avec%20la%20taille%20des%20modifications.%20&via=mgreiler&related=mgreiler)

### Regrouper les modifications liées

Une autre meilleure pratique de révision de code est de regrouper les modifications de code liées. Imaginez que vous prévoyez d'ajouter une nouvelle fonctionnalité, de corriger un bug dans une autre fonction et de refactoriser une classe. Dans ce cas, chacune de ces modifications doit faire l'objet d'une révision de code distincte. De cette manière, vous vous assurez que le but de la modification de code est clair pour les relecteurs. Un objectif clair facilite grandement la tâche de révision et augmente la valeur des retours.

### Décrire le but et la motivation de la modification

Une façon de s'assurer que vous investissez votre temps correctement lors de la préparation de la révision de code est d'écrire une description de ce que cette modification de code implique. Avec une petite note, vous aidez les relecteurs de code à comprendre le but de la modification de code et aussi pourquoi vous l'avez faite. Cette meilleure pratique de révision de code accélère le temps de révision, augmente la qualité et la valeur des retours, et améliore les taux de participation aux révisions de code.

![Image](https://cdn-media-1.freecodecamp.org/images/0*f-R3JWukTtkMA20T)

_La révision de code n'est pas un puzzle. Aidez les relecteurs à se concentrer sur les problèmes clés en décrivant la modification de code. (Photo par [Hans-Peter Gauster](https://unsplash.com/photos/3y1zF4hIPCg?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/search/photos/puzzle?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText))_

La révision de code n'est pas un puzzle. Aidez les relecteurs à se concentrer sur les problèmes clés en décrivant la modification de code. (Cliquez pour tweeter).

De manière intéressante, dans nos études, nous avons observé que les développeurs apprécient vraiment les descriptions des modifications de code. Ils souhaitent en fait que plus de personnes écrivent des descriptions. D'un autre côté, nous avons vu que les mêmes développeurs n'incluaient pas toujours de descriptions eux-mêmes.

Une raison à cela est que lorsque vous écrivez le code vous-même, vous êtes tellement impliqué dans le code que vous pensez qu'il est auto-explicatif. En fait, ce n'est pas le cas.

Et si vous n'aidez pas les relecteurs à comprendre le code, [ils ne pourront pas fournir de retours précieux](https://www.michaelagreiler.com/code-review-pitfalls-slow-down/).

Alors, écrivez la note, même si elle dit simplement : « Mis à jour le point de terminaison de l'API pour se conformer aux réglementations de sécurité ».

À quel point le travail de révision du code est-il devenu plus facile avec cette note ? N'oubliez pas, la révision de code n'est pas un puzzle !

[Même si la modification de code vous semble triviale, ajoutez une description, afin que les relecteurs sachent à quoi s'attendre (Cliquez pour tweeter).](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-best-practices/&text=Même%20si%20la%20modification%20de%20code%20vous%20semble%20triviale%2C%20ajoutez%20une%20description%2C%20afin%20que%20les%20relecteurs%20sachent%20à%20quoi%20s'attendre.&via=mgreiler&related=mgreiler)

### Exécuter les tests avant de soumettre une révision de code

Oui, prenez le temps d'exécuter les tests pour vos modifications de code. Les tests ne sont pas seulement une meilleure pratique d'ingénierie, mais aussi une meilleure pratique de révision de code. Parce que tester votre code garantit que le code fonctionne réellement avant de demander un retour.

De plus, cela montre que vous respectez le temps des relecteurs de code. Il est non seulement embarrassant d'envoyer du code qui, évidemment (comme le montrent les tests), ne fonctionne pas comme prévu, mais cela tue également la productivité de tout le monde. Alors, exécutez les tests d'abord !

### Automatiser ce qui peut être automatisé

L'un des principaux pièges des révisions de code est qu'elles prennent trop de temps. Il est donc préférable de suivre les pratiques de révision de code consistant à automatiser ce qui peut être automatisé.

Utilisez des vérificateurs de style, des vérificateurs de syntaxe et d'autres outils automatisés comme des outils d'analyse statique pour aider à améliorer le code. De cette manière, vous vous assurez que les relecteurs de code peuvent vraiment se concentrer sur la fourniture de retours précieux et n'ont pas besoin d'utiliser leur temps pour commenter des problèmes qui peuvent être trouvés automatiquement.

### Sauter les révisions inutiles

Vous avez bien lu. Certaines révisions peuvent être sautées. Évidemment, cela dépend des politiques de votre organisation, mais si elles le permettent, vous pourriez envisager de sauter les révisions de code.

Mais arrêtez-vous avant de partir et de dire à votre équipe que vous n'avez plus besoin de révisions de code. Sauter les révisions de code n'est conseillé que pour les modifications triviales qui ne changent pas la logique, comme les commentaires, les problèmes de formatage, le renommage de variables locales ou les corrections stylistiques.

[Sauter les révisions de code inutiles booste votre productivité. Cliquez pour tweeter.](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-best-practices/&text=Sauter%20les%20révisions%20de%20code%20inutiles%20booste%20votre%20productivité.&via=mgreiler&related=mgreiler)

### Ne pas sélectionner trop de relecteurs

Vous devez sélectionner le bon nombre de relecteurs pour votre modification de code. Si des nombres supérieurs à 4 personnes vous viennent à l'esprit, je vous invite à vous arrêter là. Parce qu'ajouter trop de développeurs aux révisions de code fait plus de mal que de bien.

Un problème est que si vous ajoutez trop de développeurs, chacun d'eux se sent moins responsable de donner des retours. Un autre problème est qu'ajouter plus de personnes que nécessaire diminue la productivité de votre équipe.

Certaines études suggèrent la meilleure pratique de révision de code consistant à ajouter seulement deux relecteurs actifs.

Pour certaines modifications de code, vous souhaitez que des experts supplémentaires, comme des experts en sécurité ou des développeurs d'autres équipes, examinent le code. Mais, plus souvent qu'autrement, deux relecteurs actifs suffisent.

De nombreux outils de révision de code permettent de notifier les développeurs sans les rendre obligatoires. Cela garantit qu'ils restent informés et sont conscients de ce qui se passe, mais supprime l'obligation pour eux de commenter votre code.

### Ajouter des relecteurs expérimentés pour obtenir des retours perspicaces

Des études ont montré que les retours les plus perspicaces proviennent des relecteurs qui ont déjà travaillé sur le code que vous allez modifier. Ce sont eux qui donnent les retours les plus perspicaces.

La fréquence à laquelle un relecteur a déjà révisé du code influence la capacité à donner des retours utiles. De même, les développeurs expérimentés et seniors tendent à donner de meilleurs retours de révision de code.

Mais, soyez attentif à la charge de travail des ingénieurs seniors, car ils tendent à être souvent ajoutés en tant que relecteurs.

[Les développeurs qui ont modifié ou révisé des parties du code auparavant donnent les retours de révision de code les plus précieux. (Cliquez pour tweeter).](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-best-practices/&text=Les%20développeurs%20qui%20ont%20modifié%20ou%20révisé%20des%20parties%20du%20code%20auparavant%20donnent%20les%20retours%20de%20révision%20de%20code%20les%20plus%20précieux.&via=mgreiler&related=mgreiler)

### Ajouter des développeurs juniors pour leur permettre d'apprendre

L'un des objectifs de la révision de code est la formation et l'apprentissage, alors n'oubliez pas d'inclure les développeurs juniors. Envisagez d'ajouter des relecteurs qui ne sont pas familiers avec la base de code, mais qui pourraient bénéficier des connaissances pour permettre la diffusion des savoirs.

### Notifier les personnes qui bénéficient de cette révision

Pour certaines personnes, comme les chefs de projet ou les responsables d'équipe, recevoir une notification sur les révisions de code (sans être réellement tenu de faire la révision de code) est bénéfique. Mais, vous devez prendre une décision consciente sur les personnes que vous allez notifier. Tout le monde ne se soucie pas ou ne devrait pas se soucier de votre révision de code.

### Ne notifiez pas trop de personnes

N'ajoutez pas tout le monde à la liste de notification. Ajoutez uniquement les personnes qui bénéficient réellement de l'information qu'une révision de code est en cours.

J'ai vu des équipes où chaque membre de l'équipe était ajouté à chacune des révisions de code de l'équipe élargie par défaut (+70 personnes). Cette pratique est comme n'ajouter personne à la liste. Ou dans le pire des cas, vous avez plusieurs de vos ingénieurs passant leur temps à parcourir des centaines de révisions de code pour déterminer si c'est pertinent pour eux.

### Prévenez les relecteurs avant la révision

Une pratique vraiment efficace de révision de code est de prévenir vos collègues à l'avance qu'ils recevront bientôt une révision de code. Cette pratique de révision de code réduit considérablement les temps de traitement.

Alors, faites-leur savoir qu'une révision de code arrive dès que possible.

[Prévenir les gens qu'une révision de code est en route peut accélérer le temps de révision. (Cliquez pour tweeter).](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-best-practices/&text=Prévenir%20les%20gens%20qu'une%20révision%20de%20code%20est%20en%20route%20peut%20accélérer%20le%20temps%20de%20révision.%20&via=mgreiler&related=mgreiler)

### Soyez ouvert aux changements suggérés

Recevoir des commentaires ou des retours inattendus peut vous rendre tendu et défensif. Essayez de vous préparer mentalement et travaillez sur votre capacité à être ouvert aux suggestions et à différents points de vue. Partez toujours du principe que le relecteur avait la meilleure intention.

Si certains retours vous ont mis mal à l'aise, essayez de régler les choses dès que possible. Parfois, il est bon d'avoir des conversations en face à face plus personnelles pour résoudre certains problèmes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oWg1z_ShPb7yfPB1G7VzSg.jpeg)

_Ne soyez pas défensif si vous êtes confronté à des retours inattendus. (Photo par [Sweet Ice Cream Photography](https://unsplash.com/photos/2VwP6rUzZQ0?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/search/photos/danger?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText))_

### Montrez du respect et de la gratitude envers les relecteurs

Les révisions de code se font et se défont avec la culture de retour de l'équipe. En tant qu'auteur de code, montrez de la gratitude et valorisez les retours reçus. Assurez-vous de considérer attentivement les retours des relecteurs et communiquez tout au long du cycle de retour.

Dites aux relecteurs quelles actions vous avez entreprises et quelles décisions vous avez prises en raison des retours reçus, de manière respectueuse.

[La révision de code se fait et se défait avec la qualité de la culture de retour de l'équipe. (Cliquez pour tweeter).](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-best-practices/&text=La%20révision%20de%20code%20se%20fait%20et%20se%20défait%20avec%20la%20qualité%20de%20la%20culture%20de%20retour%20de%20l'équipe.&via=mgreiler&related=mgreiler)

Mais, créer une grande culture de retour est une voie à double sens. Naturellement, les relecteurs de code influencent beaucoup la culture. Alors, examinons de près les meilleures pratiques de révision de code pour les relecteurs de code.

### Meilleures pratiques de révision de code pour les relecteurs de code

Être invité à donner un retour sur une révision de code est un honneur, alors assurez-vous de savoir [comment donner un retour précieux sur une révision de code](https://www.michaelagreiler.com/great-code-review-feedback/).

Lors des révisions de code, vous pouvez non seulement démontrer vos compétences et connaissances, mais aussi mentorat d'autres développeurs et contribuer au succès de l'équipe. Rien de pire que d'investir du temps dans des [révisions de code et de ne pas obtenir de retours précieux](https://www.michaelagreiler.com/code-review-pitfalls-slow-down/).

### Donner des retours respectueux et constructifs

Bien que cela semble évident, les révisions de code placent l'auteur du code dans une position vulnérable, alors vous devez en tenir compte. Votre travail est de donner des retours constructifs et précieux, mais aussi de le faire de manière respectueuse.

Surtout en utilisant des outils de révision de code, réfléchissez à la manière et au type de retour que vous donnez. Il est si facile de blesser les sentiments de quelqu'un, surtout sous forme écrite. Trop souvent, la pression du temps peut vous faire donner une réponse négligente qui peut être mal interprétée.

### Allez discuter en personne si nécessaire

Les outils de révision de code et les outils de chat nous permettent de communiquer avec nos pairs de manière asynchrone et sans effort. Mais il existe de nombreuses situations où une interaction humaine appropriée, en face à face ou par voix/vidéo, ne peut être battue.

Les problèmes complexes, par exemple, peuvent être résolus de manière beaucoup plus efficace et positive une fois que vous vous rendez chez votre collègue ou que vous l'appelez et en discutez personnellement. Il en va de même pour les questions contentieuses ou les sujets sensibles.

Peut-être est-il préférable d'écrire un e-mail privé ou de chercher une discussion personnelle avec l'auteur du code si vous pensez pouvoir blesser des sentiments ou faire perdre la face à l'ingénieur. Alors, chaque fois que vous êtes confronté à un problème complexe ou que vous pourriez blesser des sentiments, repensez à vos canaux de communication et agissez en conséquence.

### Assurer la traçabilité des décisions

Bien que les conversations moins traçables, comme en face à face ou en appels vidéo, puissent faire une grande différence pour la dynamique de l'équipe, il est important de documenter la discussion. Surtout le résultat de la révision de code doit être suivi pour référence future en utilisant des outils traçables tels que l'outil de révision de code.

L'outil de révision de code est le bon canal de communication pour toutes les questions simples, car il permet à toute l'équipe de suivre, et permet de rechercher les décisions et de comprendre le développement du code après coup.

![Image](https://cdn-media-1.freecodecamp.org/images/1*b9Y7gwaQTuwuJHHn0WnitQ.jpeg)

_Laisser des traces sur vos décisions et modifications aide à comprendre l'évolution du code (Photo par [Marten Bjork](https://unsplash.com/photos/GM9Xpgb0g98?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/search/photos/trace?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText))_

### Toujours expliquer pourquoi vous avez rejeté une modification

Soyons honnêtes. Avoir une modification de code rejetée n'est pas quelque chose que l'auteur du code appréciera. Il est donc important que vous soyez réfléchis et expliquiez votre rejet de manière polie, constructive et amicale.

Expliquer les raisons derrière votre décision aide non seulement l'auteur du code à apprendre et à grandir, mais aide également l'auteur à comprendre votre point de vue. Cela favorise également un dialogue continu avec l'auteur.

Dites à l'auteur du code exactement ce qu'elle doit faire pour que la modification soit acceptée.

[Si vous devez rejeter une modification de code, expliquez exactement ce qui doit se passer pour que la modification puisse être approuvée. (Cliquez pour tweeter).](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-best-practices/&text=Si%20vous%20devez%20rejeter%20une%20modification%20de%20code%2C%20expliquez%20exactement%20ce%20qui%20doit%20se%20passer%20pour%20que%20la%20modification%20puisse%20être%20approuvée.&via=mgreiler&related=mgreiler)

### Meilleures pratiques pour booster la productivité

Certains des plus grands défis lors des révisions de code, tant pour l'auteur du code que pour le relecteur, sont les contraintes de temps.

En tant que relecteur, vous pourriez trouver difficile de prendre du temps sur vos tâches quotidiennes pour réviser le code de vos pairs. Mais, les révisions de code peuvent être très bénéfiques pour vous et l'équipe si elles sont faites de la bonne manière.

### Intégrez la révision de code dans votre routine quotidienne

Structurez votre travail quotidien de manière à ce que vous réserviez du temps dédié uniquement pour les révisions de code. Par exemple, prévoyez de travailler sur les révisions de code tous les jours de 11h à 12h.

De cette manière, vous vous assurez de pouvoir compter le temps pour les révisions de code, et en faire également une activité anticipée pour vous et votre équipe. Cet horaire vous sera utile chaque fois que vous aurez une réflexion sur l'avancement de votre travail ou une évaluation de votre travail.

### Réduisez le multitâche car il tue la productivité

[Passer d'une tâche à une autre est coûteux](https://www.michaelagreiler.com/developer-productivity/). Savoir que vous ne vous arrêtez pas, quoi que vous fassiez, chaque fois qu'une révision de code arrive sur votre chemin, vous assure de pouvoir travailler de manière plus concentrée.

Les créneaux horaires qui fonctionnent dépendent de votre charge de travail, du nombre de révisions de code que vous devez effectuer ainsi que du moment où ces révisions arrivent normalement. Dans certains contextes, votre équipe bénéficie de deux (plus courts) temps de révision planifiés, comme le matin et avant de quitter le bureau. De cette manière, vos pairs n'ont pas à attendre trop longtemps pour vos retours.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WQJJWck316aARPb0jFk97w.png)

_Le multitâche tue la productivité (Photo par [Tim Gouw](https://unsplash.com/photos/1K9T5YiZ2WU?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/search/photos/problem?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText))_

[Le multitâche tue la productivité. Ayez donc des temps dédiés aux révisions de code.](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-best-practices/&text=%20Le%20multitâche%20tue%20la%20productivité.%20Ayez%20donc%20des%20temps%20dédiés%20aux%20révisions%20de%20code.%20%23codereview%20&via=mgreiler&related=mgreiler) [#codereview](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-best-practices/&text=%20Le%20multitâche%20tue%20la%20productivité.%20Ayez%20donc%20des%20temps%20dédiés%20aux%20révisions%20de%20code.%20%23codereview%20&via=mgreiler&related=mgreiler) [(Cliquez pour tweeter)](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-best-practices/&text=%20Le%20multitâche%20tue%20la%20productivité.%20Ayez%20donc%20des%20temps%20dédiés%20aux%20révisions%20de%20code.%20%23codereview%20&via=mgreiler&related=mgreiler)

### Donnez des retours en temps opportun

Il n'est pas conseillé de sauter directement dans une révision de code, chaque fois que les notifications apparaissent, en raison des coûts de changement de contexte. Pourtant, il présente plusieurs avantages pour vous et l'auteur du code de réviser le code en temps opportun.

Donner des retours dès que possible garantit que l'auteur du code n'est pas bloqué en attendant des retours. De plus, si l'auteur doit attendre trop longtemps, il devient plus difficile pour lui ou elle de se souvenir des modifications et d'incorporer les retours. N'oubliez pas que les longs temps d'attente sont un piège numéro un des [révisions de code](https://www.michaelagreiler.com/code-review-pitfalls-slow-down/).

Être l'un des premiers relecteurs (surtout s'il y en a plusieurs) garantit également que votre effort à examiner le code [ajoute réellement de la valeur](https://www.michaelagreiler.com/great-code-review-feedback/). Si vous êtes la cinquième personne à inspecter le code, les chances sont que vous n'allez plus ajouter de nouvelles perspectives. Si cela arrive fréquemment, vous devriez mettre en œuvre la meilleure pratique de révision de code pour sélectionner moins de relecteurs.

### Réviser fréquemment, pas en une seule fois

Les recherches montrent que vous pouvez donner des retours de meilleure qualité si vous réviser fréquemment et donc moins de modifications à la fois. Cela signifie que vous n'attendez pas que plusieurs révisions de code s'accumulent pour les examiner en une seule fois. Au lieu de cela, vous vous en tenez à votre horaire et réviser une révision de code (ou même des parties d'une si c'est une révision de code plus grande) à la fois.

Si les révisions de code sont généralement trop grandes et prennent trop de temps, vous pouvez suggérer les meilleures pratiques de révision de code pour des modifications petites, incrémentales et cohérentes aux auteurs de révisions de code.

[Donnez des retours de meilleure qualité aux révisions de code en ne les laissant pas s'accumuler. (Cliquez pour tweeter).](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-best-practices/&text=Donnez%20des%20retours%20de%20meilleure%20qualité%20aux%20révisions%20de%20code%20en%20ne%20les%20laissant%20pas%20s'accumuler.&via=mgreiler&related=mgreiler)

### Concentrez-vous sur les problèmes principaux, moins de chipotage

Votre objectif en tant que relecteur devrait être d'aider avec les problèmes principaux, tels que les bugs, les problèmes architecturaux, les problèmes structurels ou les problèmes qui entraîneront des problèmes de maintenabilité.

Évidemment, si vous voyez des fautes de frappe, des variables mal nommées ou des problèmes de style, vous pouvez également les signaler. Pourtant, ce n'est pas votre tâche principale et, compréhensiblement, [discuter des problèmes mineurs n'est pas précieux pour les auteurs de code.](https://www.michaelagreiler.com/code-review-pitfalls-slow-down/)

### Utilisez une checklist de révision

Une autre meilleure pratique de révision de code est d'utiliser une approche systématique pour les révisions de code. Une checklist de révision de code peut accélérer et améliorer vos performances de révision de code. Au lieu d'en créer une à partir de zéro, téléchargez une liste prête à l'emploi et personnalisez-la pour qu'elle corresponde aux pratiques de votre équipe et à vos besoins. Assurez-vous de rechercher une checklist adaptée à votre stack technologique.

### Checklist des meilleures pratiques de révision de code

Maintenant, vous connaissez toutes les meilleures pratiques de révision de code pour tirer le meilleur parti des révisions de code. Si vous avez aimé cet article, envisagez de vous abonner à ma liste de diffusion.

J'ai préparé un [Code Review e-Book exclusif](https://www.michaelagreiler.com/code-review-e-book/) pour mes abonnés par e-mail pour vous aider à vous souvenir des meilleures pratiques de révision de code. J'ai également ajouté d'autres insights et résumés sur les révisions de code. Obtenez les 12 pages d'insights sur les révisions de code maintenant. Pas encore abonné ? Inscrivez-vous simplement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HBwTGSldWHSf2u7yZ-8X1A.jpeg)

## Vous voulez en savoir plus sur les révisions de code ?

Consultez les [meilleures pratiques éprouvées de révision de code](https://www.michaelagreiler.com/code-review-best-practices/), apprenez quels [pièges de révision de code](https://www.michaelagreiler.com/code-review-pitfalls-slow-down/) vous devriez éviter, et comment [booster la valeur de vos révisions de code avec de grands retours](https://www.michaelagreiler.com/great-code-review-feedback/).

Pour **rester informé** et ne jamais manquer un article de blog, **inscrivez-vous** à ma liste de diffusion et obtenez le **e-book exclusif sur la révision de code**. Vous pouvez demander le [Code Review e-Book ici](https://www.michaelagreiler.com/code-review-e-book/).

### Vous me trouverez sur Twitter

[Connectons-nous sur Twitter](https://twitter.com/mgreiler) pour discuter des sujets d'ingénierie logicielle et des révisions de code.

---

_Publié à l'origine sur_ [_https://www.michaelagreiler.com_](https://www.michaelagreiler.com/code-review-best-practices/) _le 2 mai 2019._