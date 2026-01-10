---
title: Comment déboguer les erreurs dans votre code source
subtitle: ''
author: Mabel Obadoni
co_authors: []
series: null
date: '2023-02-24T23:37:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-debug-errors-in-your-source-code
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/Errors.png
tags:
- name: debugging
  slug: debugging
- name: error handling
  slug: error-handling
seo_title: Comment déboguer les erreurs dans votre code source
seo_desc: "The process of handling errors is known as debugging. It involves identifying\
  \ and removing errors from your program. \nIf you want to be an efficient programmer,\
  \ you'll want to cultivate your ability to debug code. It's one of the main skills\
  \ you'll n..."
---

Le processus de gestion des erreurs est connu sous le nom de débogage. Il implique d'identifier et de supprimer les erreurs de votre programme. 

Si vous voulez être un programmeur efficace, vous voudrez cultiver votre capacité à déboguer du code. C'est l'une des principales compétences dont vous aurez besoin en tant que développeur de logiciels ou programmeur. Cela signifie que vous devez également tout apprendre sur les erreurs. 🤷

Les erreurs peuvent prendre de nombreuses formes – d'une omission d'un point-virgule à un crash de base de données. Elles font toutes partie de l'expérience à la fois amère et douce de la programmation.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-126.png)

Quelle que soit votre étape en programmation, vous rencontrerez probablement au moins un type d'erreur lors du codage. L'erreur peut survenir lors de l'écriture du code, de son exécution ou même de son test. Et il existe généralement un remède spécifique à chaque erreur. Cela implique que toutes les erreurs ne sont pas gérées ou résolues de la même manière.

Les erreurs en programmation sont également appelées bugs. Ces bugs empêchent votre programme de faire ce qu'on lui demande. Une fois que vous avez compris les erreurs courantes, vous pourrez déterminer le bon traitement pour l'erreur que vous rencontrez. 

Pour déboguer les erreurs dans votre code source, vous devez comprendre :

* Les sources des erreurs dans votre code – Qu'est-ce qui cause exactement les erreurs affichées ?
* Les types d'erreurs – Maintenant que j'ai une erreur, de quel type est-elle ? Que dois-je faire pour effacer ces lignes rouges de mon écran ?

Cet article se concentrera sur la manière de répondre à ces questions.

## **D'où viennent les erreurs en codage ?**

La première étape pour trouver une solution est de connaître exactement la source du problème. Cela vous guidera pour suggérer ou construire une solution. Lorsque vous écrivez votre code dans le langage de programmation que vous utilisez, des erreurs peuvent survenir en raison de différents facteurs.

Les principales sources d'erreurs incluent :

### Erreurs humaines

Même si l'intelligence artificielle joue un rôle de plus en plus important dans de nombreuses opérations, le fait reste que les humains écrivent encore le code source. 

Les erreurs causées par l'omission, les lacunes de connaissances ou le manque de structure appropriée proviennent du développeur. 

Lorsque un développeur manque de connaissances techniques sur la syntaxe d'un langage particulier, il est inévitable qu'il y ait des erreurs dans le code source. Ou s'il veut dire une chose et en écrit une autre en code, le conflit de logique entraînera toujours une erreur.

Donc, avant de vous lancer dans le codage dans un langage quelconque, assurez-vous de comprendre la structure qui le sous-tend et les règles qui régissent ses programmes. Cela vous aidera à écrire moins d'erreurs dans votre code que vous devrez ensuite déboguer.

### Erreurs machine

Pour des problèmes tels que la faible mémoire, le peu d'espace de stockage et la lenteur de la vitesse de traitement du CPU, la machine joue également un rôle dans la causation des erreurs. En fait, une machine avec une mémoire lente peut causer des erreurs d'exécution (erreurs dues à une exécution lente du code).

Lorsque vous achetez un ordinateur, si vous le pouvez, assurez-vous d'en obtenir un qui correspond aux tâches que vous allez lui confier. Vous devriez également utiliser le stockage cloud et d'autres opérations cloud pour réduire les risques d'erreurs causées par votre machine.

### Erreurs procédurales

Résoudre un problème nécessite de suivre certaines méthodes. La programmation a sa méthodologie sous-jacente que vous devriez suivre autant que possible. 

C'est pourquoi des organismes de normalisation existent, comme le World Wide Web Consortium. Il garantit que certaines normes sont suivies lors du développement de programmes. 

Des erreurs peuvent survenir lorsque vous ignorez complètement les méthodes standard et essayez de manœuvrer à votre manière. Un tel code peut ne pas aller au-delà de votre machine car il peut ne pas être digne de production.

Étudiez les procédures pour construire et exploiter la solution que vous codez et essayez de les suivre.

## **Types d'erreurs de codage**

Les erreurs peuvent survenir indépendamment de votre niveau de compétence en programmation. Votre maîtrise du codage se manifeste lorsque vous pouvez déchiffrer en toute confiance le message d'erreur et déterminer le type d'erreur survenue. 

De nombreux langages de programmation ont des structures similaires, en particulier les langages de programmation orientés objet (comme Python et JavaScript). Ces similitudes de structure signifient qu'ils ont également des schémas d'erreurs similaires. 

En programmation, les erreurs les plus courantes sont :

### Erreurs de syntaxe

Le mot "syntaxe" signifie simplement arrangement. En programmation, la syntaxe est l'arrangement du code suivant un ensemble de règles ou de motifs. 

Tout comme en langue anglaise où les lettres sont disposées de A à Z, les langages de programmation ont également leur syntaxe que vous devrez suivre pour que le programme s'exécute sans heurts. 

Lorsque vous écrivez en anglais, par exemple, si vous ne suivez pas les règles de grammaire et de syntaxe de la langue, vos mots n'auront pas beaucoup de sens. Il en va de même en programmation : si vous ne respectez pas les règles de syntaxe du langage de programmation, vous obtiendrez une **erreur de syntaxe.**

Par conséquent, une erreur de syntaxe est cette erreur causée par la désobéissance aux règles régissant un langage particulier. Et le message d'erreur qui apparaît empêche votre programme de s'exécuter.

Les erreurs de syntaxe peuvent être causées par divers facteurs tels qu'une orthographe incorrecte, une ponctuation omise, une mauvaise utilisation des guillemets (" "), une déclaration incorrecte des variables et des valeurs, et plus encore.

Aussi petites que ces erreurs puissent paraître, elles peuvent casser votre code source si elles ne sont pas correctement résolues. Lorsque l'une de ces erreurs de syntaxe se produit, votre compilateur répond de deux manières :

* **Il met en évidence la ligne de code où l'erreur s'est produite :** Cela vous aidera à connaître l'endroit exact à vérifier pour votre erreur.
* **Il donne au moins une explication en une phrase du type d'erreur.**

Dans la plupart des cas, le compilateur indiquera qu'il s'agit d'une "erreur de syntaxe" et parfois pointera ce qui a été omis, inclus ou mal placé. Voici un exemple :

```reactjs
// importation des dépendances et composants requis
import { BrowserRouter as Router, Route, Switch,Redirect } from 'react-router-dom';
import './App.css';
import Home from './components/Home';
import About from './components/About';
import Projects from './components/Projects';
import Contact from './components/Contact';
import Nav from './components/Nav';


function App() {
  return (
    <div className='App'>
      <Router>
        {/* <Nav /> */}
        <Switch>
          <Route exact path='/'  component={Home}/>
          <Route  path='/About'  component={About} />
          <Route path='/Projects' component={Projects} />
          <Route path='/Contact'  component={Contact} />
          <Redirect to ="/" />
        
        </Switch>
      </Router>  
    </div>
```

L'extrait ci-dessus provient d'un projet React.js. Selon la syntaxe React, si vous déclarez un composant, vous devez l'utiliser, sinon il générera une erreur de syntaxe comme le montre la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/SC4.PNG)
_Erreur de syntaxe_

Dans l'exemple, le composant Nav a été déclaré dans l'ensemble des instructions d'importation mais il n'a pas été appelé dans l'instruction de routage. À cause de cela, il affiche un message d'erreur dans le terminal.

Les débutants en programmation rencontrent souvent des erreurs de syntaxe lorsqu'ils apprennent – surtout si vous jonglez entre deux langages différents en même temps. Avec une pratique constante, vous pouvez vous améliorer dans l'écriture de votre code source qui respecte les règles de syntaxe du langage que vous utilisez. 

### Erreurs de logique ou sémantiques

Un autre mot pour logique est raisonnement. L'écriture de code source pour tout programme nécessite beaucoup de raisonnement. N'oubliez pas que le codage est un moyen de fournir des solutions à des problèmes. Votre solution doit donc suivre la logique qui la guide.

Également appelée erreur sémantique, une erreur de logique est une erreur qui se produit lorsqu'un programme génère quelque chose de différent de ce qui était prévu. Chaque fois que votre programme se comporte d'une manière différente de ce que vous avez prévu, vous avez rencontré une erreur logique.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/SC21-1.png)

```python
import pandas as pd
import numpy as np
a = 5
b ="10"
print(c=a+b)

```

Dans l'exemple ci-dessus, il est clair que le compilateur n'a pas pu additionner une chaîne et un nombre car le nombre dans la chaîne n'a pas été implicitement converti en type de données **int**. 

Vous pouvez également voir qu'il y a une erreur de syntaxe dans ce programme lorsque vous regardez l'instruction **print()**. Vous pouvez déboguer l'erreur de logique en convertissant la chaîne en un type de données entier comme montré ci-dessous :

```python
import pandas as pd
import numpy as np
a = 5
b = Int("10")
print(c=a+b)
```

Contrairement à une erreur de syntaxe, une erreur de logique peut ne pas empêcher votre programme de s'exécuter. Au lieu de cela, il s'exécutera mais affichera une sortie incorrecte.

### Qu'est-ce qui cause les erreurs de logique ?

**Déclaration incorrecte du type de données :** En utilisant l'exemple ci-dessus, la deuxième variable est une chaîne à cause des guillemets qui l'entourent. Donc, le compilateur suppose que vous voulez placer les deux variables côte à côte. Assurez-vous toujours d'être méticuleux avec votre déclaration et conversion de type de données.

**Séquence incorrecte :** Supposons que vous écriviez, "Code love I to". Eh bien, cette phrase n'a aucun sens logique car les mots ne sont pas placés dans le bon ordre. 

Il en va de même pour les langages de programmation. Lorsque le code n'est pas séquentiel, le compilateur suppose à nouveau une signification pour votre code et vous donne ensuite une sortie différente de vos attentes. 

Par exemple, une fonction (en JavaScript) qui est déclarée localement sera disponible globalement en raison de la sémantique de la portée des fonctions JavaScript. Donc, si vous avez besoin de cette fonction particulière dans tout votre code source, il est préférable de la déclarer dans une portée globale.

La portée en JS signifie simplement l'emplacement d'une variable déclarée et comment elle peut être accessible. Une variable a une portée globale si elle peut être accessible n'importe où dans l'ensemble du code source. Une variable locale est limitée uniquement au bloc dans lequel elle est déclarée. La différence entre une variable globale et une variable locale est l'accessibilité.

```javascript
var age =prompt("Enter your age")

 if (age<18){
 console.log("you are a minor")
 }
 else{
 console.log("You are" + age + "years old")
 }
 
 
```

Dans l'extrait de code ci-dessus, la variable "age" est déclarée globalement, c'est pourquoi elle peut être appelée n'importe où dans l'ensemble du code source.

La séquence incorrecte est une erreur logique car les variables doivent être correctement déclarées si elles doivent être utilisées à plusieurs reprises. 

**Instruction conditionnelle, expression booléenne ou logique mal placée :** Les expressions logiques telles que if-else, do-while, et les autres sont les principales causes des erreurs logiques. Lorsqu'elles ne sont pas correctement placées, il y a toutes les chances d'obtenir une sortie incorrecte. La plupart des programmes reposent beaucoup sur les expressions logiques, vous devez donc savoir comment les utiliser.

Les erreurs logiques peuvent arriver à n'importe qui, quel que soit le niveau de compétence – tout comme toutes les erreurs. Passez donc du temps à bien réfléchir à votre logique avant de commencer à coder. Certains programmeurs vont jusqu'à dessiner un schéma pour souligner la logique qu'ils veulent pour leur programme.

### Erreur d'exécution

Chaque programme a un certain temps qu'il prend pour s'exécuter. En tant que programmeur, il est de votre devoir de vous assurer que votre programme se charge dans le temps le plus court possible. 

N'oubliez pas qu'un programme lent ne se vendra pas bien sur le marché. Personne ne veut une application qui "gaspille" leur temps, n'est-ce pas ?

Le temps d'exécution, en termes simples, est le temps nécessaire pour qu'un programme s'exécute ou fonctionne. Vous pouvez avoir votre code syntaxe bien écrit suivant une logique spécifiée et rencontrer des erreurs lors de l'exécution de votre programme. Ce problème est causé par une erreur d'exécution.

![Écran de PC montrant une alerte d'erreur](https://www.freecodecamp.org/news/content/images/2023/02/image-125.png)
_Un écran de PC montrant une alerte d'erreur_

Comme le montre l'image ci-dessus, les erreurs d'exécution peuvent survenir pendant l'exécution de votre programme – le temps entre l'interprétation de vos codes et l'affichage de la sortie requise.

Ces erreurs peuvent être causées par une variable non déclarée, une connexion Internet lente ou de nombreuses autres raisons au cours de l'exécution du code.

```javascript
const country = "Nigeria"
let indp = 1960
	function Election(){
    if ( country == "Nigeria"){
    console.log ( country + "had her "+ "independence in " + indp)
    }
    }
election()

```

Le code ci-dessus générera une erreur d'exécution car la fonction appelée est différente de celle déclarée.

#### Comment résoudre les erreurs d'exécution

La meilleure façon de résoudre les erreurs d'exécution est de les traiter en fonction de leur cause. Pour une variable non déclarée, assurez-vous que la variable est correctement déclarée en utilisant la bonne syntaxe et que la variable déclarée est la même que celle qui est appelée, comme illustré dans le bloc de code ci-dessous :

```javascript
let name = "Ayomide"
console.log (name + " " +" was my colleague")
```

En cas de faible mémoire, effacez votre cache et actualisez votre navigateur ou redémarrez votre ordinateur. 

Pour une mauvaise connexion Internet, changez de fournisseur de services Internet ou fermez certains onglets ouverts sur votre navigateur.

Dans les cas graves, sauvegardez votre code source et résolvez le problème matériel que votre ordinateur pourrait rencontrer.

## **Conclusion**

Les erreurs peuvent survenir dans n'importe quel programme, quel que soit le niveau de compétence du programmeur. Ce qui vous distingue, c'est votre capacité à trouver et à déboguer ces erreurs.

Plus vous déboguez d'erreurs, meilleur vous devenez dans l'écriture de code propre et performant. Soyez à l'affût de la prochaine ligne d'erreur et passez à l'action !