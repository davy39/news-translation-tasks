---
title: Pratique d'entretien de codage JavaScript – Exemples de questions d'entretien
  et solutions
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-31T17:39:28.000Z'
originalURL: https://freecodecamp.org/news/javascript-coding-interview-practice
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/david-goggins-quotes-about-hard-work.jpeg
tags:
- name: coding interview
  slug: coding-interview
- name: interview
  slug: interview
- name: interview questions
  slug: interview-questions
- name: JavaScript
  slug: javascript
seo_title: Pratique d'entretien de codage JavaScript – Exemples de questions d'entretien
  et solutions
seo_desc: 'By Damla Erkiner

  David Goggins is an ultramarathon runner, a public speaker, a retired navy SEAL,
  and the author of the book ''Can''t Hurt Me: Master Your Mind and Defy the Odds''.
  He''s one of my role models because of his physical strength and mental r...'
---

Par Damla Erkiner

David Goggins est un ultramarathonien, un conférencier, un ancien Navy SEAL et l'auteur du livre '[**Can't Hurt Me: Master Your Mind and Defy the Odds**](https://www.amazon.com/Cant-Hurt-Me-Master-Your/dp/1544512287)'. Il est l'un de mes modèles en raison de sa force physique et de sa résilience mentale. 

Vous pourriez dire : "Attendez une seconde ! Nous avons compris. Cette personne est clairement l'épithome du succès. Mais il a des compétences non techniques. Alors pourquoi est-il pertinent pour les entretiens de codage JavaScript ?" 

Eh bien, si vous êtes prêt, explorons cela ensemble.

### Rocky Balboa comme mentor

En réponse à une question, David dit : 'Le film Rocky a changé ma vie.' Dans [ce discours de motivation](https://www.youtube.com/watch?v=dse1afiGbx4&t=193s), il fait référence à [cette scène](https://www.youtube.com/watch?v=25NmudB2fqg) (min 1.30-1.42) où le personnage fictif, Rocky - malgré le fait d'être battu par son adversaire dans le dernier round de boxe - refuse d'abandonner quoi qu'il arrive. 

David décrit ce moment particulier comme celui où Rocky - initialement dépeint comme un outsider par le scénariste - surmonte toutes les difficultés et impressionne son rival.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-280.png)
_[Source de l'illustration](https://www.amazon.com/Eye-Tiger-Rocky/dp/B004GY1FTQ)_



Admettons-le. Être un bon programmeur n'est pas si facile. Et surtout si vous êtes au début de votre carrière, les entretiens techniques peuvent être sérieusement intimidants. En bref, il pourrait être agréable d'adopter l'état d'esprit de David (et de Rocky). 

Avec ce genre de détermination et de confiance, vous êtes beaucoup moins susceptible de considérer l'abandon, quels que soient les types de défis auxquels vous êtes confronté dans votre merveilleux mais difficile parcours pour obtenir un emploi de développeur.

## Pourquoi les entretiens de codage sont difficiles

Lors des entretiens de codage, on s'attend à ce que vous résolviez des problèmes de codage avec certaines connaissances théoriques. Mais le piège est que vous devez le faire en temps réel, ce qui peut parfois effrayer les nouveaux développeurs. 

Il existe plusieurs types d'entretiens de codage. Mais le plus difficile est probablement l'entretien sur tableau blanc. Dans ces types d'entretiens, vous devez coder devant un futur employeur / un développeur logiciel senior.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-319.png)
_[Illustration par HackerRank](https://www.hackerrank.com/blog/virtual-whiteboarding-for-system-design-interviews/)_

Ces entretiens peuvent être particulièrement stressants car vous n'êtes généralement pas autorisé à avoir un ordinateur pour rechercher des concepts inconnus ou obtenir des extraits de code sur Internet. Vous n'avez qu'un marqueur pour résoudre la question sur un tableau blanc, comme le suggère le nom.

### Les entretiens reflètent-ils ce que vous ferez dans votre travail ?

Pas nécessairement. Alors pourquoi organisent-ils ces entretiens de codage effrayants ? Eh bien, la raison est de tester vos compétences en résolution de problèmes en général. Parfois, trouver la bonne réponse peut ne pas être si important. 

Ce qui compte, c'est la manière dont vous arrivez à cette conclusion / solution et les algorithmes que vous préférez utiliser en cours de route. En d'autres termes, votre capacité à fonctionner bien sous stress est testée par les entreprises technologiques. 

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-329.png)
_[Source de l'image](https://www.reddit.com/r/ProgrammerHumor/comments/l6wnvt/interview_vs_job/)_

Admettons-le. Vous rencontrerez de nombreuses situations stressantes dans votre futur travail, et la manière dont vous gérez certains problèmes est particulièrement cruciale. Par conséquent, votre futur employeur veut naturellement témoigner de première main si vous êtes la bonne personne pour le poste. 

## Quel est le but de ce tutoriel ?

Dans cet article, je vais vous guider à travers certains concepts populaires d'entretien JavaScript à travers des exemples. Je vais également faire de mon mieux pour vous montrer ce que les recruteurs / intervieweurs pourraient réellement rechercher chez un candidat pendant qu'il code devant eux. 

Pour faire simple, nous allons examiner certains modèles et essayer de résoudre les énigmes ensemble. 

À la fin de ce tutoriel, vous aurez probablement une idée sur un certain nombre de méthodes de tableau importantes. Mais surtout, vous découvrirez comment aborder certains défis de codage de la meilleure manière possible.

## Qu'est-ce que la méthode du Palais de la Mémoire ?

Avant de commencer, sachez simplement que dans les données d'exemple ci-dessous, j'ai utilisé intentionnellement les noms de certaines célébrités décédées afin que tous ces détails puissent être accrocheurs à long terme. 

Une technique ancienne appelée [le Palais de la Mémoire](https://www.wired.co.uk/article/memory-palace-technique-explained) dit clairement que plus les détails sont étranges, plus il est facile de s'en souvenir – et une histoire inventée / créer un contexte est encore plus efficace. 

Si vous essayez de visualiser la situation liée de manière vivante et d'associer les concepts de programmation donnés avec certains détails bizarres dans votre esprit, vous pourriez vous sentir moins stressé et confus lorsque vous verrez un problème similaire la prochaine fois. Cela pourrait être plus facile pour vous de créer des liens spécifiques et ainsi vous souvenir des choses facilement. C'est ainsi que fonctionnent nos cerveaux. 

Eh bien, même le personnage fictif '[Sherlock Holmes](https://www.smithsonianmag.com/arts-culture/secrets-sherlocks-mind-palace-180949567/)', l'homme le plus intelligent de la planète, bénéficie de cette méthode lorsqu'il résout des crimes compliqués – alors pourquoi pas nous ?

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-321.png)
_[Illustration par Savanahcat](https://www.deviantart.com/savanahcat/art/Mind-Palace-387601041)_

## Comment aborder les problèmes de codage

Dans notre entretien imaginaire, vous verrez que quatre musiciens extraordinaires du passé sont listés comme passagers d'un vol. Nous avons leurs choix alimentaires et le nombre de vols de correspondance qu'ils doivent prendre après leurs performances incroyables sur scène dans différentes parties du monde.

Disons, juste pour l'argument, que nos figures phénoménales (Freddie Mercury, Amy Winehouse, Kurt Cobain et Michael Jackson) sont sur le point de voler depuis différentes destinations vers Los Angeles juste pour pouvoir dîner ensemble dans un restaurant chic, car ils apprécient tellement la compagnie les uns des autres. 

Après tout, c'est notre propre palais de la mémoire, donc nous pouvons absolument faire ce que nous voulons dans nos esprits. Rappelez-vous que les détails inhabituels resteront mieux. C'est pourquoi j'essaie d'ajouter plus d'épices pour rendre les choses plus intéressantes. 

Cette méthode suggère explicitement de décrire chaque détail avec des adjectifs vivaces afin que vous puissiez les associer aux choses que vous prévoyez d'apprendre à long terme. 

Les [scientifiques](https://www.medicalnewstoday.com/articles/memory-loss#:~:text=Short%2Dterm%20memory%20is%20the,from%20a%20longer%20time%20ago.) disent que la mémoire à court terme et la mémoire à long terme fonctionnent très différemment. Pour faire simple, nous avons besoin d'un moyen de mettre tous ces concepts de base (pas nécessairement la syntaxe) sur la programmation dans notre mémoire à long terme. C'est pourquoi il peut être agréable de bénéficier de la méthode du palais de la mémoire dans notre parcours.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-326.png)
_[Source de l'image](https://www.nme.com/news/music/producer-goes-viral-for-mixing-nirvana-and-michael-jackson-songs-with-drill-beats-2747204)_

De plus, j'ai l'impression que vous pouvez imaginer ce scénario inhabituel avec un sourire sur le visage. Eh bien, ne serait-ce pas génial si ces âmes géniales avaient pu voir qu'elles aident maintenant nous / la communauté de programmation en tant qu'invités d'un article de freeCodeCamp ? 

### Exemples de questions d'entretien

Revenons cependant à la vie réelle. Rappelez-vous que vous êtes toujours en entretien et comme vous le voyez ci-dessous, trois questions d'affilée vous attendent.

```js

// Question principale : Obtenir les noms des passagers en utilisant les données fournies
// Partie bonus (a) - Retourner les végétariens/végétaliens
// Partie bonus (b) - Trier les passagers par le nombre de vols de correspondance en ordre décroissant

```

### Les données

Pour résoudre les énigmes, vous devez utiliser les données à l'intérieur du tableau d'objets suivant de manière pratique. 

Vous devrez certainement trouver les bons algorithmes et essayer de trouver la solution la plus efficace qui puisse satisfaire l'intervieweur. 

```js

const passengers = [
  {
    id: 1,
    passengerName: "Freddie Mercury",
    isVegetarianOrVegan: false,
    connectedFlights: 2,
  },
  {
    id: 2,
    passengerName: "Amy Winehouse",
    isVegetarianOrVegan: true,
    connectedFlights: 4,
  },
    {
    id: 3,
    passengerName: "Kurt Cobain",
    isVegetarianOrVegan: true,
    connectedFlights: 3,
  },
     {
    id: 3,
    passengerName: "Michael Jackson",
    isVegetarianOrVegan: true,
    connectedFlights: 1,
  },
];
```

Les questions ci-dessus ne sont en fait pas si difficiles. Mais la manière dont nous allons les traiter est une excellente opportunité de comparer des solutions alternatives pour un seul problème. À la fin de la journée, la qualité est ce qui compte pour les recruteurs / intervieweurs. 

### Question d'entretien 1 : Comment obtenir les noms des passagers 

Obtenons les noms des passagers comme demandé. La première solution est par une méthode de ['boucle for'](https://www.freecodecamp.org/news/javascript-for-loop-how-to-loop-through-an-array-in-js/). Nous devons donc d'abord utiliser un tableau vide pour y pousser les noms des passagers à la fin de la boucle. 

Ci-dessous, `[i]` représente le passager actuel et nous parcourons simplement le tableau 'passengers' pour accéder aux noms des passagers. Ensuite, nous devons les verrouiller dans notre tableau vide / passengerNames.

```js

const passengerNames = [];
for (let i = 0; i < passengers.length; i++) {
    passengerNames.push(passengers[i].passengerName)
}
console.log("passengers", passengerNames);

```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-331.png)
_<nr-sentence class="nr-s81" id="nr-s81" page="0">RÉSULTAT - utilisant 'for loop'</nr-sentence>_

D'accord, nous avons résolu l'énigme, mais est-ce suffisant ? Ou les intervieweurs pourraient-ils s'attendre à ce que vous trouviez une meilleure solution ?

### Solution alternative #1 :

Nous pouvons atteindre le résultat souhaité en utilisant la fonction '[forEach](https://www.freecodecamp.org/news/javascript-foreach-how-to-loop-through-an-array-in-js/)' également. Cette solution est même un peu meilleure que la précédente car il n'y a pas d'expression d'index dans celle-ci. 

```js
                 
const passengerNames = [];
passengers.forEach((passenger) => {
    passengerNames.push(passenger.passengerName);
})
```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-332.png)
_<nr-sentence class="nr-s89" id="nr-s89" page="0">RÉSULTAT - utilisant 'forEach'</nr-sentence>_

Pour bénéficier de 'forEach', nous avons besoin [d'une fonction de rappel](https://www.freecodecamp.org/news/what-is-a-callback-function-in-javascript-js-callbacks-example-tutorial/). Avec cet arrangement, nous sommes capables d'atteindre chaque passager dans la liste. Cependant, comme dans la solution précédente, nous avons d'abord besoin d'un tableau vide pour pousser les éléments / noms des passagers. 

Même si le résultat est le même, ce morceau de code est plus court. Écrire des codes plus propres est ce qui est – en fait – attendu de vous. 

En d'autres termes, non seulement la solution compte, mais aussi la manière dont vous y arrivez est évaluée par les recruteurs. Pour cette raison, il est bon de planifier votre action plutôt que d'écrire la première idée qui vous vient à l'esprit sur le tableau blanc.

### Solution alternative 2 :

Voici la meilleure solution. Nous pouvons également utiliser la fonction '[map](https://www.freecodecamp.org/news/javascript-map-how-to-use-the-js-map-function-array-method/)' pour résoudre le même problème. Voyons comment.

```js

const passengerNames = passengers.map((passenger) => passenger.passengerName); 
```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-333.png)
_<nr-sentence class="nr-s103" id="nr-s103" page="0">RÉSULTAT - utilisant 'map'</nr-sentence>_

La fonction map parcourt également le tableau et retourne un nouveau tableau pour chaque élément de la liste. Avec cette configuration, nous retournons simplement un seul élément, pas un objet. 

Le résultat sera à nouveau le même dans la console, mais votre code sera encore meilleur que le premier et le deuxième car cette fois, nous n'avons pas besoin de créer un tableau vide avant la tâche réelle. 

Voici la nourriture pour la pensée sur ce sujet. Ceux qui disent 'moins c'est plus' ont un point lorsqu'il s'agit d'écrire des codes. 

### Question d'entretien 2 : Comment obtenir les chanteurs végétariens/végétaliens 

Examinons maintenant le prochain défi. La nouvelle tâche nous demande d'obtenir uniquement les chanteurs végétariens/végétaliens de la liste des passagers tout en conservant le premier argument dans la section principale de la question. 

### Comment résoudre avec une 'boucle for'

Encore une fois, nous pouvons utiliser la même vieille 'boucle for' pour celle-ci également. Tout ce que nous devons faire est de vérifier s'il y a des chanteurs végétariens/végétaliens dans notre liste de passagers via une instruction 'if' à l'intérieur de notre fonction existante.

```js

const passengerNames = [];
for (let i = 0; i < passengers.length; i++) {
    if(passengers[i].isVegetarianOrVegan) {
    passengerNames.push(passengers[i].passengerName)
    }
}
console.log(passengerNames);

```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-334.png)
_<nr-sentence class="nr-s117" id="nr-s117" page="0">RÉSULTAT - utilisant 'for loop'</nr-sentence>_

Nous faisons cela avec la propriété `isVegetarianOrVegan` dans notre objet. Basiquement, ce que nous disons est ceci : si l'instruction pertinente est vraie (s'il y a des passagers végétariens/végétaliens dans la liste), poussez simplement ces éléments dans notre nouveau tableau. Le résultat nous donnera les noms de trois chanteurs car ceux-ci sont listés comme 'végétariens ou végétaliens' dans la partie des données. 

### Comment résoudre avec 'forEach'

En fait, la fonction 'forEach' gère le problème de manière similaire. Mais encore une fois, elle a trop de lignes de code comme vous le voyez ci-dessous, donc ce n'est pas la version idéale. 

```js

const passengerNames = [];
passengers.forEach((passenger) => {
      if (passenger.isVegetarianOrVegan)
        passengerNames.push(passenger.passengerName);
});

console.log(passengerNames);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-335.png)
_<nr-sentence class="nr-s126" id="nr-s126" page="0">RÉSULTAT / 'forEach'</nr-sentence>_

### Comment résoudre avec 'Filter' & 'Map'

Pour trouver la meilleure option, cette fois, nous allons utiliser deux méthodes différentes. Les fonctions '[filter](https://www.freecodecamp.org/news/javascript-array-filter-tutorial-how-to-iterate-through-elements-in-an-array/)' et 'map' vont – en quelque sorte – collaborer pour créer une meilleure logique lors de la résolution du problème donné. Examinons de près le snippet de code suivant maintenant.

```js

const passengerNames = passengers.filter((passenger) => passenger.isVegetarianOrVegan).map((passenger) => passenger.passengerName);

console.log(passengerNames);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-336.png)
_<nr-sentence class="nr-s133" id="nr-s133" page="0">RÉSULTAT / 'filter' + 'map'</nr-sentence>_

Avec la méthode filter, nous obtenons uniquement les passagers végétariens/végétaliens de notre tableau en premier lieu. Si elle trouve des passagers non végétariens/végétaliens (comme notre bien-aimé 'Freddie'), elle s'en débarrassera automatiquement. 

Brièvement, la première partie de l'équation, la méthode 'filter' fonctionnera simplement selon le modèle 'oui' ou 'non'. 

Ensuite, la fonction 'map' interviendra, nous donnant finalement un tout nouveau tableau montrant uniquement les passagers végétariens/végétaliens. 

Cette solution finale prouvera à votre futur employeur que vous savez vraiment ce que vous faites et que vous prenez les bonnes mesures pour devenir un développeur de premier plan.

### Question d'entretien #3 : Comment trier les passagers par vols de correspondance

La dernière section nous demande de trier la liste de nos passagers super cool par le nombre de vols de correspondance qu'ils prendront pour atteindre finalement Los Angeles. Voyons qui en a le plus et sera donc assez épuisé. 

Alerte spoiler ! Amy avec quatre vols de correspondance au total pourrait être un peu endormie lors de la réunion dans ce restaurant chic. Mais il ne fait aucun doute qu'elle va quelque part. 

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-322.png)
_[Source de l'image](https://variety.com/2022/music/global/amy-winehouse-freddie-mercury-john-lennon-tupac-shakur-bbc-studios-sales-1235196177/)_

En tout cas, ce dont nous avons besoin pour cette tâche est de savoir comment fonctionne la fonction '[sort](https://www.freecodecamp.org/news/javascript-array-sort-tutorial-how-to-use-js-sort-methods-with-code-examples/)'. 

Principalement, elle compare les éléments un par un et retourne quelque chose comme résultat. Dans notre cas, ce sera le nombre de vols de correspondance. Mais comment fait-elle cette comparaison ? Quelle est la logique derrière cela ?

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-343.png)
_[Source du code : MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)_

Les lignes de code ci-dessus sont assez claires en général. Grâce à la fonction 'sort', nous listons ces mois par ordre alphabétique. 

Eh bien, voici la grande question. Comment le code / système sait-il que 'a' est la première lettre de l'alphabet et que la liste commence donc par la lettre 'd' (décembre) ?

La raison est que la fonction 'sort' liste les choses par ordre croissant par défaut. Mais ne pouvons-nous pas changer ce paramètre ? Peut-être devons-nous lister les éléments par ordre décroissant. Bien sûr, nous pouvons. 

Voyons comment. Pour obtenir ce que nous voulons, nous pouvons utiliser les lettres 'a' et 'b' comme paramètres menant à différentes directions.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-338.png)
_[Source du code : MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)_

Simultanément, nous pouvons bénéficier de l'assistance de trois nombres : -1, +1, 0 comme vu ci-dessus. Lors du tri des éléments par ordre décroissant ou croissant ou de la recherche des valeurs égales, ils peuvent être assez pratiques. 

### Partie délicate de la fonction 'Sort'

Dans l'exemple suivant, la liste est triée par ordre croissant. Pourquoi est-ce ainsi ? Voici la raison. Lorsque nous retournons ces paramètres 'a' et 'b', nous utilisons cet ordre : 'a - b'. Cela nous donne des valeurs croissantes par défaut. 

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-339.png)
_[Source du code : MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)_

Cependant, si nous les échangeons et disons 'b - a', la liste sera vue en ordre décroissant cette fois. C'est la partie délicate lorsqu'il s'agit de la fonction 'sort'.

Dans l'exemple ci-dessus, la première version (fonction régulière) et la deuxième (fonction fléchée) sont en essence les mêmes, mais sachez simplement que les [fonctions fléchées](https://www.freecodecamp.org/news/arrow-function-javascript-tutorial-how-to-declare-a-js-function-with-the-new-es6-syntax/) sont arrivées avec [ES6](https://www.freecodecamp.org/news/these-are-the-features-in-es6-that-you-should-know-1411194c71cb/). 

Bien que les fonctions fléchées aident les développeurs à écrire moins de code, vous ne pouvez pas les utiliser partout. (Lisez [ceci](https://www.freecodecamp.org/news/when-and-why-you-should-use-es6-arrow-functions-and-when-you-shouldnt-3d851d7f0b26/) pour savoir quand les utiliser.)

### Test de nos nouvelles connaissances

Devons-nous maintenant analyser la situation de nos passagers à travers notre nouvelle perspective ? Nous savons que la dernière tâche nous demande de trier le nombre de vols en ordre décroissant. Mais la configuration suivante fait le contraire. 

Elle ne peut nous donner la liste qu'en ordre croissant. Pourquoi ? C'est simplement à cause de l'ordre prédéfini (passenger1.connectedFlights - passenger2.connectedFlights) comme dans le cas de l'exemple a - b.

```js

 const numberOfFlights = passengers.sort(
  (passenger1, passenger2) =>
    passenger1.connectedFlights -  passenger2.connectedFlights 
); 
console.log(numberOfFlights);

```

Une fois que nous échangeons l'ordre (passenger2.connectedFlights - passenger1.connectedFlights) comme vous le voyez dans l'extrait de code suivant, notre problème sera résolu et la liste viendra en ordre décroissant. 

```js

 const numberOfFlights = passengers.sort(
  (passenger1, passenger2) =>
    passenger2.connectedFlights -  passenger1.connectedFlights 
); 
console.log(numberOfFlights);

```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-342.png)
_<nr-sentence class="nr-s189" id="nr-s189" page="0">RÉSULTAT - Ordre décroissant par le nombre de vols de correspondance / Michael est le plus chanceux :-)</nr-sentence>_

### Peut-on aussi utiliser 'for loop' ou 'forEach' ?

Eh bien, oui et non. Les deux seraient des solutions de bas niveau pour cette question. 

Nous devons garder à l'esprit que la fonction de tri mute un tableau. C'est une sorte d'effet secondaire qui change le tableau original et cela pourrait être un problème si nous utilisons 'for loop' ou 'forEach' comme solution. 

Il existe bien sûr [des moyens](http://www.buginit.com/javascript/javascript-sort-without-mutating-array/) d'éviter la mutation dans la fonction de tri, mais dans notre exemple, cela conduira à plus de lignes de code, ce qui n'est pas du tout pratique.

## Conclusion

Nous avons commencé l'article avec David Goggins, le symbole de la résilience et de la détermination, alors terminons-le avec sa présence et ses idées inspirantes. 

Si vous arrivez à lire le livre de ce héros moderne ou à écouter l'un de ces célèbres épisodes de podcast (par exemple, [celui-ci](https://www.youtube.com/watch?v=5tSTk1083VY)) où il était un invité, vous comprendrez immédiatement qu'il n'est pas né comme ça. Plutôt, son secret réside dans le fait qu'il n'abandonne jamais, contre toute attente. 

Les entretiens de codage sont difficiles, mais si vous continuez à poursuivre vos objectifs en visualisant la scène de succès dans votre esprit encore et encore, cela sera - tôt ou tard - à vous. 

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-328.png)
_[Source de l'image](https://castromarina.info/david-goggins-inspirational-quotes)_

Merci beaucoup d'avoir lu cet article. Si vous avez aimé cet article, l'une des meilleures façons de me soutenir est de le partager. Si vous avez des questions ou des commentaires, vous pouvez toujours me contacter via [LinkedIn](https://www.linkedin.com/in/damla-erkiner-000b76227/). Je serai plus qu'heureuse de vous aider avec vos questions.

Bon codage !

**Le savoir est pouvoir.  Francis Bacon**