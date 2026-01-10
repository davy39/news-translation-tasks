---
title: Comment j'ai intégré un formulaire d'inscription à une liste de diffusion directement
  dans Medium en utilisant Google Forms
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2016-09-18T21:08:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-mailing-list-signup-to-your-medium-stories-using-google-forms-c717393b2f6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IOZC9nmYpJCaendKkOWHVw.jpeg
tags:
- name: Design
  slug: design
- name: marketing
  slug: marketing
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment j'ai intégré un formulaire d'inscription à une liste de diffusion
  directement dans Medium en utilisant Google Forms
seo_desc: 'There are a ton of paid tools for gathering email addresses here on Medium.
  And boy do they offer a lot of features.

  But what if you don’t care about those features?

  What if you just want your readers’ email addresses, and that’s all?

  That’s where Go...'
---

Il existe une tonne d'outils payants pour collecter des adresses e-mail ici sur Medium. Et ils offrent certainement beaucoup de fonctionnalités.

Mais que faire si vous ne vous souciez pas de ces fonctionnalités ?

Que faire si vous voulez simplement les adresses e-mail de vos lecteurs, et c'est tout ?

C'est là que Google Forms entre en jeu. Il est simple, gratuit et exporte directement en CSV.

Et contrairement aux outils payants, Medium supporte nativement l'intégration de Google Forms. Ainsi, si votre lecteur consulte votre histoire dans un navigateur, il verra le formulaire intégré directement dans l'article Medium.

Si votre lecteur consulte votre histoire dans l'application Medium Android ou iOS, il ne pourra pas voir l'intégration. Je recommande donc d'inclure également un lien qu'ils peuvent suivre pour accéder à votre formulaire.

Construisons ensemble un formulaire d'inscription à une liste de diffusion, puis intégrons-le dans une histoire Medium.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PcMQNWqTGIUv2TFdqyRVTg.png)
_C'est à cela que ressemblera le résultat final. J'intégrerai le formulaire en direct à la fin de cet article._

### Comment créer votre formulaire d'inscription avec Google Forms

#### Étape #1 : Créer le formulaire

Allez sur [https://forms.google.com](https://forms.google.com) et cliquez sur

![Image](https://cdn-media-1.freecodecamp.org/images/1*6ZL4XkJt5QoRKU3F0I-5Lg.png)

#### Étape #2 : Créer le champ de saisie

La première question sera par défaut "Choix multiples". Changez-la en "réponse courte"

![Image](https://cdn-media-1.freecodecamp.org/images/1*ndjGUXZvZZMBIsqBn6L9Pw.png)

#### Étape #3 : Ajouter des titres à votre formulaire et à votre question

![Image](https://cdn-media-1.freecodecamp.org/images/1*u44PEr7Jqb5q_Kapp4F84A.png)

#### Étape #4 : Ajouter une validation des données

Tout d'abord, activons la validation des données sur notre formulaire en cliquant sur le "⋯" dans le coin inférieur droit, puis sur "validation des données".

![Image](https://cdn-media-1.freecodecamp.org/images/1*Up1MrB8tT9N3-m1KCgtixg.png)

Maintenant, activons la correspondance par expression régulière pour nous assurer que vos lecteurs entrent une adresse e-mail valide.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mb0zOL0yqpTcePq8YB9sGw.png)

Voici l'expression régulière que j'utilise, que [emailregex.com](http://emailregex.com/) dit identifier une adresse e-mail valide 99,99 % du temps. Copiez et collez simplement ceci dans le champ d'expression régulière :

```
(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])
```

Si vous êtes curieux de savoir comment fonctionnent les expressions régulières et que vous souhaitez en apprendre davantage, [voici une leçon interactive](https://www.freecodecamp.com/challenges/sift-through-text-with-regular-expressions).

Je ne recommande pas de rendre cette question obligatoire, car cela ajoutera un astérisque rouge effrayant et indiquera "obligatoire". Cela pourrait donner à vos lecteurs l'impression incorrecte que vous exigez leur adresse e-mail. Vous pouvez facilement filtrer les réponses vides après coup.

#### Étape #5 : Assurez-vous qu'il est public

Cliquez sur l'icône d'engrenage en haut et vérifiez que votre e-mail n'est pas restreint aux personnes qui partagent le même domaine que votre adresse e-mail.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cU2S2VW-sJ4xwm0jXR1H4A.png)

#### Étape #6 : Ajoutez une touche de couleur. Pourquoi pas ?

Cliquez sur l'icône de palette dans le coin supérieur droit. Vous pouvez également télécharger une image si vous le souhaitez.

![Image](https://cdn-media-1.freecodecamp.org/images/1*eXJeXb09Wyjav3WIERqVQw.png)

### Maintenant, ajoutons votre formulaire d'inscription à Medium

Cliquez sur le bouton "envoyer" dans le coin supérieur droit de votre Google Form.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-OgJrreJbNZFuLUSlb5wxw.png)

Cliquez sur l'icône de lien en forme de chaîne, puis cliquez sur "raccourcir l'URL". Copiez l'URL, revenez à Medium, collez-la et appuyez sur Entrée.

Après un moment, Medium affichera une miniature de votre formulaire. Une fois que vous aurez cliqué sur le bouton de publication, votre formulaire sera intégré dans votre publication Medium et sera entièrement opérationnel.

Voilà ! Voici à quoi ressemble le mien :

Recevez 3 articles dignes d'être lus de ma part dans votre boîte de réception une fois par semaine. [Inscrivez-vous ici](https://goo.gl/forms/dsvfK1dRz5zePih02).

### Section bonus : Comment j'envoie mes e-mails

Voici le script que j'utilise actuellement pour envoyer mon e-mail hebdomadaire à environ 350 000 personnes :

[**FreeCodeCamp/massification**](https://github.com/FreeCodeCamp/massification)
[_massification - Un service d'e-mailing basé sur Amazon SES et Node_github.com](https://github.com/FreeCodeCamp/massification)

Ce script utilise Amazon SES pour une livraison optimale. Il coûte 0,01 $ par centaine d'e-mails, ce qui signifie que mon envoi d'e-mails hebdomadaire ne me coûte que 35 $.

Actuellement, le script prend environ 18 heures pour envoyer 350 000 e-mails. Mais il est entièrement open-source, donc si quelqu'un trouve un moyen de le rendre plus efficace, les pull requests sont les bienvenues.

Si vous êtes curieux, voici à quoi ressemble l'un de mes e-mails :

![Image](https://cdn-media-1.freecodecamp.org/images/1*OTtgoPkQ7Z8zfhrD2WS3PQ.png)

Et voici le JSON qui produit cet e-mail :

```json
{
 "subject": "Quelqu'un apprend à faire tomber internet.",
 "text": "Voici les trois liens de cette semaine qui valent votre temps :\n\n1. Quelqu'un apprend à faire tomber internet (3 minutes de lecture) : http://bit.ly/2cbR5um\n\n2. Depuis 25 ans, cet homme se bat pour rendre les informations publiques. Maintenant, il est poursuivi pour cela (25 minutes de lecture) : http://bit.ly/2cZzkM4\n\n3. GitHub a annoncé une tonne de nouvelles fonctionnalités de collaboration (6 minutes de lecture) : http://bit.ly/2cfZrPZ\n\nBonus : Je viens d'ajouter de nouveaux articles Free Code Camp à la boutique de notre communauté, y compris des t-shirts, des hoodies et des livres recommandés : http://bit.ly/2cz8Wai\n\n\nBonne programmation,\n\n- Quincy Larson\n\nEnseignant sur https://www.FreeCodeCamp.com\n\n\n\n\n\nSi cet e-mail vous dérange, vous pouvez gérer vos paramètres d'e-mail ici : https://www.freecodecamp.com/settings\n\nOu vous pouvez vous désabonner en un clic : https://www.freecodecamp.com/unsubscribe/<%= email %>"
}
```

Vous remarquerez que le lien bonus en bas dirige les lecteurs vers [la boutique de Free Code Camp](https://www.freecodecamp.com/shop). Cela facilite le soutien de notre communauté open source par les lecteurs et m'aide à compenser le coût de l'envoi de tous ces e-mails.

Vous remarquerez également que j'ai écrit une fonction de désabonnement rudimentaire mais fiable. Toute la logique derrière cela fonctionne sur les serveurs de Free Code Camp, où je maintient cette liste.

Vous devrez trouver vous-même une sorte de solution de désabonnement.

Si votre liste n'est pas très grande, vous pourriez simplement dire aux lecteurs de répondre "désabonner" s'ils ne veulent plus de vos e-mails, puis les supprimer manuellement de votre liste dans la feuille de calcul Google Docs.

Une autre chose que vous pourriez remarquer est que j'envoie des e-mails en texte brut, plutôt qu'en HTML.

Beaucoup de designers m'écrivent pour me proposer de créer un modèle HTML pour moi. Ce qu'ils ne réalisent pas, c'est que [les gens préfèrent les e-mails en texte brut plutôt que les e-mails en HTML](http://blog.hubspot.com/marketing/plain-text-vs-html-emails-data).

Ma théorie est que les amis ne vous envoient pas d'e-mails en HTML — ils écrivent simplement du texte. Vous êtes donc plus susceptible d'interpréter un e-mail en texte comme amical, et un e-mail en HTML comme du spam.

De plus, les e-mails en HTML soulèvent des problèmes d'accessibilité et de réactivité mobile que vous devriez gérer. Essayé de coder un modèle d'e-mail ? Ce n'est pas amusant.

Mon conseil est donc d'utiliser simplement du texte.

Et oui, j'ai fait des tests A/B moi-même et j'ai conclu que mes propres e-mails en texte performaient mieux que mes e-mails en HTML.

Je remercie donc ces designers pour leur offre, puis je leur demande s'ils pourraient plutôt aider à créer des [assets sous licence Creative Commons pour notre communauté](https://github.com/FreeCodeCamp/assets).

Enfin, vous remarquerez que j'utilise bit.ly pour gérer les analyses. Cela ne me donne pas de statistiques de réception/ouverture, mais cela me donne des statistiques de clics :

![Image](https://cdn-media-1.freecodecamp.org/images/1*GViH8Q_eXU5Af-Lst6mhAg.png)
_Mon tableau de bord Bit.ly des 30 derniers jours._

Si quelqu'un connaît un moyen fiable de suivre les statistiques de réception/ouverture avec du texte brut, faites-le moi savoir dans la section des commentaires.

### Et bien sûr, vous devez demander aux gens de s'inscrire 😉

Recevez 3 articles dignes d'être lus de ma part dans votre boîte de réception une fois par semaine. [Inscrivez-vous ici](https://goo.gl/forms/dsvfK1dRz5zePih02).

De plus, cliquez sur le ? ci-dessous pour que plus de personnes voient cet article ici sur Medium.

![Image](https://cdn-media-1.freecodecamp.org/images/1*31StU5CNIHk8VDkSHWO6nA.gif)