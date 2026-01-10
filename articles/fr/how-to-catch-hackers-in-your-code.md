---
title: Comment attraper les hackers dans votre code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-05T16:57:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-catch-hackers-in-your-code
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/How-to-Catch-Hackers-in-Your-Code.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Security
  slug: security
- name: software development
  slug: software-development
seo_title: Comment attraper les hackers dans votre code
seo_desc: "By Bedirhan Urgun\nWhat would you do if hackers were abusing your software\
  \ in production? \nThis is not a hypothetical question. They are probably doing\
  \ it right now. \nYou might be thinking about all the secure design choices you\
  \ have made, or preventa..."
---

Par Bedirhan Urgun

Que feriez-vous si des hackers exploitaient votre logiciel en production ? 

Ce n'est pas une question hypothétique. Ils le font probablement en ce moment même. 

Vous pensez peut-être à tous les choix de conception sécurisés que vous avez faits, ou aux techniques préventives que vous avez appliquées, donc il n'y a rien à craindre. 

Si c'est le cas, c'est bien – même s'il y a toujours des choses qui passent inaperçues, vous devez toujours penser à la sécurité de votre système. 

Mais il y a une **énorme différence** entre prévenir les bugs de sécurité et pardonner les tentatives malveillantes.

Et si nous attrapions et agissions contre les hackers qui tentent de s'introduire dans notre logiciel ? Dans cet article, je vais essayer de vous donner des exemples pratiques et simples pour détecter les comportements typiques des hackers dans votre code dès que possible.

## Pourquoi détecter les tentatives malveillantes ?

Prévenir les bugs de sécurité ne suffit-il pas ? Je vous entends dire : « Tant que j'écris du code sécurisé, je me moque que les hackers jouent avec mon logiciel ultra-sécurisé ou non. Alors, pourquoi devrais-je me soucier des tentatives malveillantes ? » 

Répondons d'abord à cette question valable.

Un logiciel quelque peu complexe est difficile à maintenir sécurisé en permanence. Plus de complexité signifie plus de faiblesses potentielles qu'un hacker peut exploiter pendant que vous concevez, implémentez, déployez ou maintenez le code.

Regardez simplement les [nombres de CVE](https://www.cvedetails.com/browse-by-date.php) au fil des ans. C'est énorme :

![Image](https://lh4.googleusercontent.com/xHM7o5NKsWBrELAL-pjl90rlDxpHzIMz4e33OHzJLpl82tpJFEsaUVJ8_c5GFoxPHaJGtpk-s5qUZ8pJhghA-E71Z9xLdtqkf3SCUtfGR_8bPMdQXxx9p1tfr7NH1BZqepSDQJeG)
_Le nombre de bugs de sécurité publiés au fil des ans par cvedetails.com_

De plus, en raison de sa nature, un bug de sécurité n'est pas simplement un élément régulier dans votre backlog. Il y a des conséquences désagréables si une vulnérabilité est exploitée : une perte de confiance, une mauvaise réputation, ou même une perte financière.

Ainsi, des bonnes pratiques de sécurité telles que la [Norme de Vérification de la Sécurité des Applications OWASP (ASVS)](https://owasp.org/www-project-application-security-verification-standard/) ou les [Directives de Codage Sécurisé de Mozilla](https://wiki.mozilla.org/WebAppSec/Secure_Coding_Guidelines) existent afin d'aider les développeurs à produire des logiciels sécurisés.

Cependant, puisque de nouvelles façons de contourner les contrôles de sécurité existants ou de nouvelles faiblesses émergent presque quotidiennement, il y a un consensus au sein de la communauté de la sécurité que « Il n'y a pas de sécurité à 100 %. » Nous devons donc toujours être vigilants et réactifs aux nouvelles et améliorations en matière de sécurité. 

Il y a aussi une autre chose que nous pouvons faire pour assurer la sécurité des logiciels : remarquer les hackers le plus tôt possible, avant qu'ils ne fassent quelque chose que nous n'attendons pas ou même que nous ne connaissons pas. De plus, suivre leur comportement malveillant sur une longue période nous rend plus proactifs.

Il existe une notion populaire de [Centre des Opérations de Sécurité (SOC)](https://fr.wikipedia.org/wiki/Centre_des_op%C3%A9rations_de_s%C3%A9curit%C3%A9) dans ce sens – les SOC sont un type d'équipe dans une organisation qui est externalisée ou interne. Leur travail est de surveiller en continu l'état de sécurité de l'organisation. Ils le font en détectant, analysant et répondant aux incidents de cybersécurité. 

Les équipes SOC recherchent des activités anormales, y compris les anomalies de sécurité des logiciels. L'idée de remarquer et de répondre à une cyberattaque réussie ou échouée donne aux organisations un avantage contre les menaces, ce qui réduit finalement le temps de réponse aux attaques grâce à une surveillance continue.

Un SOC est fort seulement avec les riches et qualitatives entrées qu'il reçoit de différentes sources de composants IT. Puisque notre logiciel est également une partie importante de l'inventaire, les alarmes de sécurité appropriées dues aux comportements anormaux envoyées par notre logiciel aux équipes SOC sont inestimables.

## Comment vérifier les comportements anormaux

Voici un certain nombre de vérifications et de contrôles que nous pouvons implémenter dans notre code qui révèlent des comportements malveillants et anormaux. 

Avant de commencer, j'aimerais souligner que je ne présente pas de solutions compliquées comme le [Pare-feu d'Applications Web (WAF)](https://fr.wikipedia.org/wiki/Pare-feu_d%27application_web) ici. Au lieu de cela, je vais simplement essayer de vous montrer que des conditionnelles simples, une gestion intelligente des exceptions, et des actions similaires avec peu ou pas d'effort dans votre code peuvent vous aider à remarquer les comportements anormaux dès qu'ils se produisent. 

Commençons.

### Retour de longueur nulle ou null

La première action que nous pouvons prendre pour détecter une action malveillante est de vérifier les agrégats de longueur nulle ou les retours null. 

Voici un simple bloc de code pour illustrer le point :

```csharp
Receipt receipt = GetReceipt(transferId);
if (receipt == null)
{
    // que signifie cela ?
    // journaliser, notifier, alerter
}
```

Ici, nous essayons d'accéder au reçu d'un certain transfert fourni par nos utilisateurs finaux via le paramètre `transferId`. 

Afin d'empêcher quiconque d'accéder aux reçus de quelqu'un d'autre, supposons que dans la méthode `GetReceipt`, notre développeur est assez intelligent pour vérifier si le `transferId` appartient réellement à l'utilisateur actuel. 

Vérifier la propriété est une bonne pratique de sécurité.

Supposons en outre que nous sommes sûrs par conception que chaque transfert doit avoir au moins un reçu associé, donc ne pas en obtenir à l'exécution est suspect. Pourquoi ? Parce qu'obtenir un reçu vide signifie que le `transferId` fourni n'appartient à aucun transfert exécuté par l'utilisateur actuel. 

En d'autres termes, l'utilisateur actuel a fourni un `transferId` falsifié à notre code et attend de voir le contenu si ce `transferId` se trouve être lié à une transaction de quelqu'un d'autre. 

Et puisque nous avons le contrôle de propriété approprié, la méthode `GetReceipt` retourne un reçu vide ou null. C'est là que nous devons prendre certaines mesures de sécurité. 

Je n'entrerai pas dans les détails des actions de sécurité dans cet article. Cependant, la journalisation de sécurité et/ou l'envoi de notifications détaillées, les systèmes de gestion des informations et événements de sécurité ([SIEM](https://fr.wikipedia.org/wiki/Security_Information_and_Event_Management)) en sont deux.

Voici un autre exemple de la façon dont la vérification de la valeur nulle nous permet de saisir une tentative malveillante. 

Considérons que nous avons les trois points de terminaison suivants, `ShowReceipt`, `Success`, et `Error` :

```csharp
// Point de terminaison ShowReceipt
if(CurrentUser.Owns(receiptId))
{
   Session["receiptid"] = receiptId;
   redirect "Success";
}
else
{
    redirect "Error";
}
```

```csharp
// Point de terminaison Success
receiptId = Session["receiptid"];
return ReadReceipt(receiptId);
```

```csharp
// Point de terminaison Error
return "Error";
```

Ceci est une application simple qui montre le contenu d'un reçu d'utilisateur. 

Dans `ShowReceipt`, la première ligne est importante. Elle vérifie si l'utilisateur final nous envoie un `receiptId` valide pour voir son contenu. Sans ce contrôle, un utilisateur malveillant peut fournir n'importe quel `receiptId` et accéder au contenu.

L'emplacement de l'instruction dans la troisième ligne est tout aussi important, cependant. Si nous déplaçons cette ligne juste avant l'instruction if, cela ne casserait rien. Cependant, cela créerait le même problème de sécurité que nous essayions d'éviter en vérifiant si l'utilisateur final demande un reçu valide ou non. 

Veuillez prendre un moment pour vous assurer que vous comprenez pourquoi c'est le cas.

Maintenant, c'est une bonne idée que nous avons placé cette ligne au bon endroit et cela crée une autre opportunité de remarquer les tentatives malveillantes. Ensuite, dans le point de terminaison `Success`, que signifie-t-il si nous obtenons un `receiptId` null de la `Session` ? 

Cela signifie que quelqu'un appelle ce point de terminaison, juste après avoir fait une demande au point de terminaison `ShowReceipt` avec le `receiptId` de quelqu'un d'autre. Même s'ils ont obtenu une redirection `Error` en retour à cause de la vérification de propriété ! 

Bien sûr, avec le contrôle que nous avons à la première ligne, cela est impossible.

Ainsi, le point de terminaison `Success` est un bon endroit pour écrire une entrée de journal de sécurité et envoyer des notifications à nos solutions de surveillance lorsque nous obtenons un `receiptId` null de la `Session`.

```csharp
// Point de terminaison Success (Revisité)
receiptId = Session["receiptid"];
if(receiptId == null)
{
    // journaliser, notifier, alerter
}
return ReadReceipt(receiptId);
```

### Gestion des exceptions ciblées

La gestion des exceptions est peut-être le mécanisme le plus important pour les développeurs afin de répondre à toute condition anormale pendant l'exécution du programme. 

La plupart du temps, l'opportunité principale qu'elle offre est de nettoyer les ressources qui ont été empruntées, telles que les flux de fichiers/réseau ou les connexions de base de données en cas de problèmes inattendus. C'est un comportement de sécurité qui nous permet d'écrire des programmes plus fiables.

En parallèle, nous pouvons utiliser efficacement les exceptions d'exécution pour remarquer les tentatives malveillantes envers notre logiciel.

Voici quelques sources populaires de faiblesses où nous pouvons utiliser les exceptions associées pour remarquer un comportement suspect :  


* Désérialisation
* Cryptographie
* Analyse XML
* Expression régulière
* Opérations arithmétiques

La liste n'est pas complète, bien sûr. Et ici, je ne vais passer en revue que quelques-unes de ces API.

Commençons par les expressions régulières. Voici un bloc de code qui applique une méthode de validation stricte sur une entrée utilisateur :

```csharp
if(!Regex.IsMatch(query.Search, @"^([a-zA-Z0-9]+ ?)+$"))
{
    return RedirectToAction("Error");
}
```

Le motif d'expression régulière utilisé ici est un motif de liste blanche solide, ce qui signifie qu'il vérifie ce qui est attendu comme entrée. Pas l'autre façon non sécurisée qui consiste à vérifier ce qui est connu pour être mauvais. 

Cependant, voici une version beaucoup plus sécurisée du même bloc de code :

```csharp
if(!Regex.IsMatch(query.Search, @"^([a-zA-Z0-9]+ ?)+$", 
                  RegexOptions.Compiled, TimeSpan.FromSeconds(10)))
{
    return RedirectToAction("Error");
}
```

Il s'agit d'une version surchargée de la méthode `IsMatch` dont le dernier argument est la clé. 

Elle impose que l'exécution de l'expression régulière pendant l'exécution ne peut pas dépasser 10 secondes. Si c'est le cas, cela signifie que quelque chose de suspect se passe puisque le motif utilisé n'est pas si compliqué. 

Il existe une véritable faiblesse de sécurité qui pourrait être utilisée pour abuser de ce motif appelée [ReDoS](https://en.wikipedia.org/wiki/ReDoS), bien que je ne vais pas entrer dans les détails ici. Mais en bref, un utilisateur final peut envoyer la chaîne suivante comme paramètre de recherche et rendre notre backend misérable, en dépensant une quantité affreuse de puissance CPU en vain. 

Remarquez la marque de citation à la fin (et n'essayez pas cela en production !) :

==AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!==

La question est, que se passe-t-il lorsque le temps d'exécution dépasse réellement 10 secondes ? 

L'environnement .NET lance une exception, à savoir `RegexMatchTimeoutException`. Donc, si nous attrapons spécifiquement cette exception, nous avons maintenant l'opportunité de signaler cet incident suspect ou de faire quelque chose à ce sujet. 

Voici le bloc de code final à cette fin :

```csharp
try
{
    if(!Regex.IsMatch(query.Search, @"^([a-zA-Z0-9]+ ?)+$", 
                        RegexOptions.Compiled, TimeSpan.FromSeconds(10)))
    {
        return RedirectToAction("Error");
    }
}
catch(RegexMatchTimeoutException rmte)
{
    // journaliser, notifier, alerter
}
```

Une autre avenue importante où nous pouvons utiliser les exceptions est l'analyse XML. Voici un exemple de bloc de code :

```csharp
XmlReader xmlReader = XmlReader.Create(input);
var root = XDocument.Load(xmlReader, LoadOptions.PreserveWhitespace);
```

Le XML d'entrée est alimenté dans `XmlReader.Create`, puis nous obtenons l'élément racine. Les hackers peuvent abuser de ce morceau de code en fournissant certains fichiers XML malveillants, qui, lorsqu'ils sont analysés par le code ci-dessus, donnent la propriété de nos serveurs à eux. 

Effrayant, n'est-ce pas ? Le bug de sécurité est appelé [Attaque par Entité Externe XML](https://fr.wikipedia.org/wiki/Attaque_par_entit%C3%A9_externe_XML) (XXE), et comme avec l'exploitation des expressions régulières, je ne vais pas entrer dans tous les détails ici.

Cependant, afin de prévenir cette faiblesse super critique, nous ignorons l'utilisation des Définitions de Type de Document (DTD) via `XmlReaderSettings`. Ainsi, il n'y a plus de possibilité de bugs de sécurité XXE. 

Voici la version sécurisée :

```csharp
XmlReaderSettings settings = new XmlReaderSettings();
settings.DtdProcessing = DtdProcessing.Ignore;

XmlReader xmlReader = XmlReader.Create(input, settings);
var root = XDocument.Load(xmlReader, LoadOptions.PreserveWhitespace);
```

Nous pouvons laisser le code tel quel et passer à autre chose. Cependant, si un hacker essaie toujours d'abuser de cette attaque en vain, il est préférable que nous puissions attraper ce comportement et produire une alerte de sécurité inestimable :

```csharp
try
{
    XmlReaderSettings settings = new XmlReaderSettings();
    settings.DtdProcessing = DtdProcessing.Ignore;

    XmlReader xmlReader = XmlReader.Create(input, settings);
    var root = XDocument.Load(xmlReader, LoadOptions.PreserveWhitespace);
}
catch(XmlException xe)
{
    // journaliser, notifier, alerter
}
```

De plus, afin de prévenir les faux positifs, vous pouvez ==personnaliser davantage le bloc catch en utilisant le contenu du message fourni par l'instance `XmlException`.==

Il existe une bonne pratique de programmation générale qui interdit l'utilisation de types `Exception` génériques dans les blocs catch. Ce que nous avons montré est également un bon cas de soutien pour cela. Il en va de même pour une autre bonne pratique qui interdit l'utilisation de blocs catch vides, ce qui revient effectivement à ne rien faire lorsqu'un comportement anormal se produit dans notre code. 

Cependant, au lieu de blocs catch vides, nous avons ici une très bonne opportunité de réagir aux tentatives malveillantes.

### Normalisation des entrées

Par définition, la normalisation consiste à obtenir la forme la plus simple de quelque chose. En fait, la canonicalisation est le terme utilisé à cette fin. Mais il est difficile à prononcer, alors restons à la normalisation.

Bien sûr, « la forme la plus simple de quelque chose » est un peu abstrait. Que voulons-nous dire par « forme la plus simple » ? 

Il est toujours bon de montrer par l'exemple. Voici une chaîne :

==%3cscript%3e==

Selon l'[encodage URL](https://fr.wikipedia.org/wiki/Percent-encoding), cette chaîne n'est pas sous sa forme la plus simple. Parce que si nous appliquons le décodage URL, nous obtenons celle-ci :

==\<script\>==

C'est la forme la plus simple de la chaîne originale selon la norme de transformation de l'encodage URL. 

Comment savons-nous cela ? Nous le savons non pas parce qu'elle est compréhensible pour nous maintenant. Nous le savons parce que si nous appliquons à nouveau le décodage URL, nous obtiendrons la même chaîne :

==\<script\>==

Et cela signifie que le décodage URL ne la transforme plus avec succès. Nous avons atteint la forme la plus simple. La normalisation peut prendre plus d'une étape, car l'encodage peut avoir été appliqué plus d'une fois à l'origine.

L'encodage URL n'est qu'un exemple de la transformation utilisée pour la normalisation, ou en d'autres termes, le décodage. L'encodage HTML, l'encodage JavaScript et l'encodage CSS sont d'autres méthodes importantes d'encodage/décodage largement utilisées pour la normalisation. 

Au fil des ans, les attaquants trouvent des techniques authentiques pour contourner les systèmes de défense. Et l'une des techniques les plus répandues qu'ils utilisent est l'encodage. Ils utilisent des techniques d'encodage folles sur leurs entrées malveillantes originales, afin de tromper les défenses autour des applications. 

L'histoire est pleine de ces démonstrations, et vous pouvez lire les détails de l'une des plus célèbres appelée [l'attaque par points de l'IIS de Microsoft](https://fr.wikipedia.org/wiki/Attaque_par_travers%C3%A9e_de_r%C3%A9pertoire#Attaque_par_travers%C3%A9e_de_r%C3%A9pertoire_sur_Microsoft_Windows) qui a eu lieu au début des années 2000.

Puisque les hackers s'appuient substantiellement sur les techniques d'encodage lorsqu'ils envoient des entrées malveillantes, la normalisation peut être l'un des moyens les plus efficaces et faciles de les saisir.

Voici la règle d'or : nous appliquons récursivement le décodage URL/HTML/CSS/JavaScript à l'entrée utilisateur jusqu'à ce que la sortie ne change plus. Et si la sortie est une chaîne différente de l'entrée originale, cela signifie que nous avons peut-être une requête malveillante possible. 

Voici une version simplifiée de la légendaire [OWASP ESAPI Java](https://github.com/ESAPI/esapi-java-legacy/blob/develop/src/main/java/org/owasp/esapi/reference/DefaultEncoder.java#L147) qui implémente cette idée :

```java
int foundCount = 0;
boolean clean = false;
while(!clean)
{
    clean = true;
    // les codes que vous voulez ; URL/Javascript/HTML/...
    Iterator i = codecs.iterator();
    while (i.hasNext())
    {
        Codec codec = (Codec)i.next();
          String old = input;
          input = codec.decode(input);
          if (!old.equals(input))
         {
            if (clean)
           {
               foundCount++;
            }
            clean = false;
        }
    }
}
```

Lorsque le bloc de code se termine, si la valeur de `foundCount` est supérieure ou égale à 2, que signifie cela ? Cela signifie que quelqu'un envoie une entrée encodée multiple à notre application, et les chances que cela se produise sont vraiment rares. 

Les utilisateurs normaux n'envoient pas de chaînes encodées multiples à notre application. Il y a une forte probabilité que ce soit un utilisateur malveillant. Nous devons journaliser cet événement avec l'entrée originale pour une analyse plus approfondie.

Le mécanisme ci-dessus, bien que faisant partie du logiciel lui-même, fonctionne comme un filtre devant l'application. Il s'exécute sur chaque entrée non fiable et nous donne l'opportunité de connaître les tentatives malveillantes. 

Cependant, vous pouvez être suspicieux quant au délai supplémentaire que cette méthode de validation entraîne. Je comprends si vous ne voulez pas opter pour cela.

Voici un autre exemple d'utilisation de la normalisation comme moyen de saisir les tentatives malveillantes lors des téléchargements ou téléversements de fichiers. Considérez le code suivant :

```csharp
if (!String.IsNullOrEmpty(fileName))
{
    fileName = new FileInfo(fileName).Name;
    string path = @"E:\uploaded_files\" + fileName;
    if (File.Exists(path))
    {
        response.ContentType = "image/jpg";
        response.BinaryWrite(File.ReadAllBytes(path));
    }
}
```

Ici, nous obtenons un paramètre `fileName` de notre client, localisons l'image qu'il pointe, la lisons et présentons le contenu. C'est un exemple de téléchargement. Cela aurait également pu être un scénario de téléversement. 

Néanmoins, afin d'empêcher le client de manipuler le paramètre `fileName` à sa guise, nous utilisons la propriété `Name` de la classe `FileInfo`. Cela ne récupérera que la partie nom du `fileName`, même si le client nous envoie autre chose que ce que nous attendons (c'est-à-dire un nom de fichier avec des chemins falsifiés comme ci-dessous) :

==../../WebSites/Cross/Web.config==

Ici, le client malveillant veut lire le contenu d'un fichier `Web.Config` sensible en utilisant notre code. En obtenant uniquement la partie nom de fichier, nous nous débarrassons de cette possibilité. 

C'est bien, mais il y a encore quelque chose que nous pouvons faire :

```csharp
if (!String.IsNullOrEmpty(fileName))
{
    string normalizedFileName = new FileInfo(fileName).Name;
    if (normalizedFileName != fileName)
    {
        // journaliser, notifier, alerter
        response = ResponseStatus.Unauthorized;
    }

    string path = @"E:\uploaded_files\" + fileName;
    if (File.Exists(path))
    {
        response.ContentType = "image/jpg";
        response.BinaryWrite(File.ReadAllBytes(path));
    }
}
```

Nous comparons la version normalisée de `fileName` avec elle-même (l'entrée originale). Si elles diffèrent, cela signifie que quelqu'un essaie de nous envoyer un `fileName` manipulé et nous prenons les mesures appropriées. 

Normalement, le navigateur envoie simplement le nom du fichier téléversé dans sa forme la plus simple sans transformation.

Pour l'argument, nous n'avons peut-être même pas besoin d'utiliser le nom de fichier lorsque l'utilisateur téléverse un fichier. Nous pouvons générer un `GUID` et l'utiliser à la place. 

Néanmoins, appliquer ce contrôle au nom de fichier fourni compte toujours, car les hackers piqueront définitivement ce paramètre quoi qu'il arrive.

### Entrée invalide contre les listes blanches

La liste blanche consiste à « n'accepter que ce qui est attendu ». En d'autres termes, si nous rencontrons une entrée que nous n'attendons pas, nous la rejetons. 

Cette stratégie de validation des entrées est l'une des stratégies les plus sécurisées et efficaces que nous ayons à ce jour. En utilisant cette stratégie de manière cohérente dans votre logiciel, vous pouvez fermer de nombreuses voies connues et inconnues qu'un utilisateur malveillant peut utiliser pour vous attaquer. 

Cette façon de construire un logiciel est comme construire un château fermé avec seulement des portes soigneusement contrôlées s'ouvrant vers l'extérieur, si cela a un sens. 

D'accord, revenons à notre sujet.

Analysons la liste blanche avec un scénario simple. Supposons que nos utilisateurs ont la liberté de choisir leurs propres noms d'utilisateur spécifiques lors de l'inscription. Et avant de coder, en tant qu'exigence, nous avons été informés de l'apparence d'un nom d'utilisateur.

Ensuite, afin de nous conformer à cette exigence, nous pouvons facilement concevoir des règles rigides à appliquer contre l'entrée du nom d'utilisateur avant de l'accepter. Si l'entrée passe le test, nous la prenons. Sinon, nous rejetons l'entrée.

Les règles de la liste blanche peuvent prendre différentes formes, cependant. Certaines peuvent contenir une liste de valeurs codées en dur attendues, d'autres peuvent vérifier si l'entrée est un entier ou non. Et d'autres peuvent être sous la forme d'expressions régulières.

Voici un exemple d'expression régulière pour les noms d'utilisateur :

==\^\[a-zA-Z0-9]{4,15}$==

Cette expression régulière est un motif de liste blanche très rigide. Elle correspond à chaque chaîne dont les caractères ne sont rien d'autre que a-z, A-Z, ou 0-9. Non seulement cela, mais la longueur de l'entrée doit être d'un minimum de 4 caractères et d'un maximum de 15 caractères. 

Le chapeau au début et le caractère dollar à la fin de l'expression régulière indiquent que la correspondance doit se produire pour toute l'entrée.

Maintenant, supposons qu'à l'exécution nous obtenons l'entrée suivante qui ne passera pas notre test d'expression régulière :

==o'neal==

Cela signifie-t-il que notre logiciel est confronté à un hacker ? 

L'entrée semble inoffensive. Cependant, il pourrait également s'agir d'un utilisateur malveillant qui essaie simplement l'existence d'un bug de sécurité d'[injection SQL](https://fr.wikipedia.org/wiki/Injection_SQL) avant de passer à l'action, ce qui est également connu sous le nom de reconnaissance. 

Quoi qu'il en soit, il est toujours difficile de déduire une quelconque malice de ce cas particulier.

Cependant, nous pouvons toujours saisir les hackers en utilisant d'autres formes de listes blanches échouées, telles que des tentatives d'entrée échouées contre une liste de valeurs codées en dur attendues. 

Un excellent exemple est la norme [JSON Web Token (JWT)](https://fr.wikipedia.org/wiki/JSON_Web_Token). Nous utilisons JWT lorsque nous voulons que des tiers nous envoient une revendication que nous pouvons valider et ensuite faire confiance aux données à l'intérieur.

La norme a une structure JSON simple : un en-tête, un corps et une signature. L'en-tête contient comment cette revendication particulière doit être produite et donc validée. Le corps contient la revendication elle-même. La signature est là pour, eh bien, la validation.

Par exemple, lorsque nous obtenons le jeton suivant d'un tiers, tel qu'un utilisateur, nous le validons en utilisant l'algorithme qu'il présente dans la valeur de l'en-tête. 

Dans ce cas, le jeton lui-même nous dit que nous devons utiliser l'algorithme de hachage cryptographique [HMACSHA256](https://fr.wikipedia.org/wiki/HMAC) (HS256 dans le jeton est une version courte) sur les données de l'en-tête et du corps pour tester s'il produit la même signature donnée. 

Si elle produit la même valeur de signature, alors le jeton est authentique et nous pouvons faire confiance au corps :

```json
// En-tête
{
 "alg" : "HS256",
 "typ" : "JWT"
}
// Corps
{
  "userid": "johndoe@gmail.com",
  "name": "John Doe",
  "iat": 1516239022
}
// Signature
AflcxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5g
```

Il existe diverses bibliothèques externes que nous pouvons facilement utiliser pour produire et valider les JWT. Certaines d'entre elles avaient un bug de sécurité sérieux qui permettait à n'importe quel JWT d'être pris comme un jeton authentique. 

Voici ce qui n'allait pas avec ces bibliothèques. 

Que se passe-t-il lorsqu'un jeton que nous devons valider contient un en-tête comme ci-dessous ? Je présente simplement l'en-tête ici, mais il contient également des parties de corps et de signature :

```json
// En-tête
{
 "alg" : "None",
 "typ" : "JWT"
}
```

Il semble que pour ce jeton spécifique, certaines de ces bibliothèques de validation JWT acceptent simplement le corps tel quel sans aucune validation, car `None` indique qu'aucun algorithme n'est appliqué pour la production de signature. 

Pour mettre cela en perspective, cela signifie que n'importe quel utilisateur final peut nous envoyer n'importe quel `userid` à l'intérieur du jeton et nous n'appliquerons aucune validation contre celui-ci et les laisserons se connecter.

La meilleure façon d'éviter cela et des problèmes de sécurité similaires est de garder une liste valide d'algorithmes de notre côté. Dans ce cas, la liste peut contenir un seul algorithme valide. 

De plus, il est préférable de ne pas traiter l'algorithme que nous obtenons dans la partie en-tête du JSON Web Token, quel qu'il soit.

Mais comme vous l'avez peut-être déjà deviné, il y a une énorme opportunité ici. Nous pouvons simplement obtenir la valeur de l'algorithme de la partie en-tête et vérifier même si nous ne l'utiliserons pas. Si la valeur est autre chose que ce que nous attendons, disons HS256, cela signifie que quelqu'un nous manipule.

La même méthode peut être utilisée pour toute liste de valeurs codées en dur présentées à l'utilisateur final et dont nous attendons recevoir une en entrée. 

Par exemple, si nous fournissons une liste de villes dans une boîte de sélection, nous sommes sûrs que nous obtiendrons l'une d'entre elles lorsque le formulaire sera posté. Si nous obtenons une valeur complètement différente, il y a sûrement quelque chose qui ne va pas avec le comportement de l'utilisateur ou de l'outil automatisé auquel nous sommes confrontés.

### Actions contre l'AuthN et l'AuthZ

L'une des parties les plus critiques du logiciel du point de vue de la sécurité sont les mécanismes d'authentification et d'autorisation. Ce sont des endroits où nous imposons que seules les parties que nous connaissons accèdent à l'application et qu'elles accèdent à certaines parties dans leurs rôles. 

En d'autres termes, nos utilisateurs ne devraient pas utiliser certaines parties de notre application sans aucune validation d'identification et ils ne devraient pas accéder à des parties où ils n'ont aucun privilège.

Il existe divers scénarios d'attaque contre les deux mécanismes, cependant, le plus évident contre l'authentification est le forçage brutal. Il s'agit d'essayer un ensemble de justificatifs d'identité pré-remplis ou générés à la volée les uns après les autres dans l'espoir que l'un ou plusieurs d'entre eux fonctionneront. 

Bien sûr, il existe des moyens bien connus de prévenir de telles attaques : utiliser des [CAPTCHA](https://fr.wikipedia.org/wiki/CAPTCHA) ou appliquer une limitation de débit sur les adresses IP ou les noms d'utilisateur problématiques.

Habituellement, les attaques d'authentification sont bien connues et, lorsqu'elles sont remarquées, elles sont déjà journalisées et éventuellement alimentées dans les systèmes de surveillance de la sécurité.

Il en va de même pour les attaques contre l'autorisation. 

Il est facile de produire un journal de sécurité et une alarme lorsque notre application retourne une réponse 403 à nos utilisateurs. Cette réponse HTTP bien connue est l'indicateur d'un problème d'autorisation, il est donc judicieux de la journaliser. 

Cependant, les cas d'authentification et d'autorisation jusqu'à présent ont le potentiel de produire de fausses alarmes. Cependant, je vous encourage toujours à journaliser et à produire des alarmes chaque fois que ceux-ci se produisent.

Maintenant, concentrons-nous sur un cas plus solide. Chaque fois que nous utilisons des frameworks Model-View-Controller (MVC), nous utilisons la fonctionnalité de liaison automatique intégrée pour les paramètres de nos méthodes `Action`. Ainsi, le framework MVC que nous utilisons est responsable de la liaison des paramètres dans les requêtes HTTP à nos objets de modèle automatiquement. 

C'est un grand soulagement pour nous puisque obtenir chaque entrée utilisateur en utilisant les API de bas niveau d'un framework devient vraiment fastidieux après un certain temps.

Que se passe-t-il si cette liaison automatique devient trop permissive ? Supposons que nous avons un modèle `User`. Il aurait probablement au moins dix ou vingt champs membres. Mais pour plus de clarté, disons qu'il a un champ `FullName` et un champ `IsAdmin`. 

Le deuxième champ membre indiquera si un utilisateur particulier est administrateur ou non :

```csharp
public class User
{
    public string FullName { get; set; }
    public bool IsAdmin { get; set; }
}
```

Afin que les utilisateurs puissent mettre à jour leur propre profil, nous préparons une `View` incluant le formulaire et les liaisons appropriés. 

Enfin, lorsque le formulaire est soumis, une action de contrôleur liera automatiquement les paramètres HTTP à une instance de la classe `User`. Ensuite, peut-être qu'elle l'enregistrera dans la base de données comme ci-dessous :

```csharp
[HttpPost]
public Result Update(User user)
{
    UserRepository.Store(user);
    return View("Success");
}
```

Évidemment, ici, un utilisateur non administratif malveillant peut également définir les valeurs des membres de modèle indésirables, tels que `IsAdmin`. Puisque la liaison est automatique, notre utilisateur malveillant peut se rendre administrateur en demandant une simple requête HTTP POST à cette action !

En utilisant le modèle MVC, chaque modèle que nous utilisons dans les paramètres des méthodes d'action devient entièrement visible et modifiable par les utilisateurs finaux. 

La meilleure façon de prévenir cela est d'utiliser des `ViewModels` ou des objets DTO supplémentaires pour les `Views` et les `Actions` et d'inclure uniquement les champs autorisés. Par exemple, voici un `UserViewModel` qui ne contient que les champs modifiables de la classe de modèle `User`.

```csharp
public class UserViewModel
{
    public string FullName { get; set; }
}
```

Ainsi, l'utilisateur final, bien qu'il puisse ajouter un paramètre `IsAdmin` supplémentaire à la requête HTTP POST, cette valeur ne sera pas utilisée du tout pour entraîner un problème de sécurité. Excellent !

Mais attendez, il y a une opportunité en or ici pour saisir les hackers sophistiqués. Et si nous incluons toujours la propriété `IsAdmin` dans notre `UserViewModel`, mais que nous produisons un journal de sécurité et peut-être des alarmes lorsque le setter est appelé :

```csharp
public class UserViewModel
{
    public string FullName { get; set; }
    public bool IsAdmin
    {
        set
        {
            // journaliser, alerter, notifier
        }
    }
}
```

Assurez-vous simplement que nous n'utilisons pas ce champ membre lorsque nous créons une instance de la classe de modèle `User` à partir de cette instance `UserViewModel`.

### Divers

Il est impossible de lister ou de classer tous les cas possibles où nous pouvons placer nos petits contrôles pour remarquer les tentatives de piratage dès que possible. Cependant, voici quelques-unes des autres opportunités que nous avons :

* Si notre application fournit un flux d'actions qui doivent être suivies dans un ordre spécifique, alors tout ordre d'appel invalide indique un comportement anormal.
* Les attaques par injection sont l'une des catégories de bugs de sécurité les plus graves qui proviennent de code et de concaténation de données non sécurisés. Le Cross Site Scripting (XSS), l'injection SQL et la traversée de répertoires sont quelques bugs courants dans cette catégorie. Une fois que nous utilisons des constructions sécurisées comme les encodages contextuels, la validation par liste blanche et les instructions préparées, nous nous en débarrassons. Cependant, malheureusement, il n'existe pas de moyens simples et non basés sur des listes noires pour saisir les hackers qui tentent toujours d'exploiter ces bugs de sécurité une fois qu'ils sont corrigés.
* Mettre en place des pièges est également un moyen valide de capturer les tentatives malveillantes, mais je suis contre cela si l'effort prend un énorme temps ou est susceptible de produire de fausses alarmes. Par exemple, il est possible d'inclure des liens cachés (display:none) dans nos pages web et de déclencher la journalisation de sécurité lorsque ces liens sont accessibles par des scanners de sécurité automatisés (parce qu'ils essaient d'accéder à chaque lien qu'ils peuvent extraire). Cependant, cela peut également produire de fausses alarmes pour des crawlers légitimes, comme Google. Néanmoins, c'est un choix de conception et il existe de nombreux pièges qui peuvent être mis en place, tels que des paires de nom d'utilisateur et de mot de passe inexistantes mais faciles à deviner :
    - paires de nom d'utilisateur et de mot de passe, par exemple, l'infâme ==admin:admin==
    - chemins d'URL administratifs, par exemple, ==/admin==
    - en-têtes HTTP, paramètres, par exemple, ==IsAdmin==

## Conclusion

> « Pardonner, ce n'est pas approuver ce qui s'est passé. C'est choisir de s'élever au-dessus. » Robin Sharma

Il est naïvement impardonnable de laisser les tentatives malveillantes envers notre logiciel passer inaperçues alors que nous avons déjà les outils sous la main pour faire autrement. Le pardon est une qualité morale suprême, mais nous devons être au-dessus des activités risquées autour de notre code.

Malgré les facettes chaotiques du développement logiciel, développer un code sécurisé est une compétence de survie importante dans ce monde chargé de hackers. 

De plus, nous avons la chance d'améliorer cette compétence encore davantage en remarquant les activités malveillantes de manière précise dans notre code et en produisant des entrées de journal de sécurité et des alarmes pour les équipes SOC.

Faire quelque chose à propos des comportements malveillants dans notre code, comme vous l'avez lu dans cet article ==est juste l'une des erreurs de codage qui conduisent à l'abus des hackers.== Je vous encourage à vérifier ma [formation en ligne sur les erreurs de codage que les hackers exploitent](https://www.udemy.com/course/coding-mistakes-that-hackers-abuse/?referralCode=DB84A20CFA4F65DDE427) afin de maîtriser le reste d'entre elles.