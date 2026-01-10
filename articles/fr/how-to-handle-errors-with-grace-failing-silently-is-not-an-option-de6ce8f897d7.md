---
title: 'Comment gérer les erreurs avec grâce : échouer silencieusement n''est pas
  une option'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-15T18:09:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-errors-with-grace-failing-silently-is-not-an-option-de6ce8f897d7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eDuyL7l8N39gsDb-KFLtog.jpeg
tags:
- name: clean code
  slug: clean-code
- name: error handling
  slug: error-handling
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: 'Comment gérer les erreurs avec grâce : échouer silencieusement n''est
  pas une option'
seo_desc: 'By Rina Artstain

  I’ve never really had much of an opinion about error handling. This may come as
  a shock to people who know me as quite opinionated (in a good way!), but yeah. If
  I was coming into an existing code base I just did whatever they did be...'
---

Par Rina Artstain

Je n'ai jamais vraiment eu d'opinion tranchée sur la gestion des erreurs. Cela peut surprendre ceux qui me connaissent comme quelqu'un de plutôt opinionné (dans le bon sens !), mais c'est ainsi. Si je travaillais sur une base de code existante, je faisais simplement ce qui avait été fait avant, et si j'écrivais du code à partir de zéro, je faisais simplement ce qui me semblait juste à ce moment-là.

Lorsque j'ai récemment lu la section sur la gestion des erreurs dans [Clean Code](https://www.oreilly.com/library/view/clean-code/9780136083238/) d'Uncle Bob, c'était la première fois que je réfléchissais vraiment à ce sujet. Plus tard, je suis tombée sur un bug causé par un code qui échouait silencieusement, et j'ai réalisé qu'il était peut-être temps d'y réfléchir un peu plus. Je ne pourrai peut-être pas changer la façon dont les erreurs sont gérées dans toute la base de code sur laquelle je travaille, mais au moins je serai informée sur les approches existantes, leurs compromis, et, vous savez, j'aurai une opinion sur le sujet.

### **Attendez-vous à l'Inquisition espagnole**

La première étape pour gérer les erreurs est d'identifier quand une « erreur » n'en est pas une. Cela dépend bien sûr de la logique métier de votre application, mais en général, certaines erreurs sont évidentes et faciles à corriger.

* Vous avez une plage de dates où la date « à » est avant la date « de » ? Inversez l'ordre.
* Vous avez un numéro de téléphone qui commence par + ou contient des tirets alors que vous ne vous attendez à aucun caractère spécial ? Supprimez-les.
* Une collection nulle pose problème ? Assurez-vous de l'initialiser avant d'y accéder (en utilisant [l'initialisation paresseuse](https://en.wikipedia.org/wiki/Lazy_initialization) ou dans le constructeur).

N'interrompez pas le flux de votre code pour des erreurs que vous pouvez corriger, et surtout, n'interrompez pas vos utilisateurs. Si vous pouvez comprendre le problème et le corriger vous-même — faites-le simplement.

![Image](https://cdn-media-1.freecodecamp.org/images/gMPEtUMvrcUzejIk2Qc1m2yjc-vPWBeLCqAU)
_Photo par [Unsplash](https://unsplash.com/photos/7DITOdv_Uxo?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Lance Anderson</a> sur <a href="https://unsplash.com/search/photos/expect?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### **Retourner Null ou d'autres valeurs magiques**

Les valeurs nulles, -1 où un nombre positif est attendu et d'autres valeurs de retour « magiques » — toutes ces pratiques déplacent la responsabilité de la vérification des erreurs vers l'appelant de la fonction. Ce n'est pas seulement un problème parce que cela entraîne une prolifération des vérifications d'erreurs, c'est aussi un problème parce que cela dépend des conventions et nécessite que votre utilisateur soit conscient des détails d'implémentation arbitraires.

Votre code sera rempli de blocs de code comme ceux-ci qui obscurcissent la logique de l'application :

```
return_value = possibly_return_a_magic_value()if return_value < 0:   handle_error()else:    do_something()
```

```
other_return_value = possibly_nullable_value()if other_return_value is None:   handle_null_value()else:   do_some_other_thing()
```

Même si votre langage dispose d'un système intégré de propagation des valeurs nulles — cela revient simplement à appliquer un correctif illisible à un code instable :

```
var item = returnSomethingWhichCouldBeNull();var result = item?.Property?.MaybeExists;if (result.HasValue){    DoSomething();}
```

> Passer des valeurs nulles aux méthodes est tout aussi problématique, et vous verrez souvent des méthodes commencer par quelques lignes de vérification que l'entrée est valide, mais cela est vraiment inutile. La plupart des langages modernes fournissent plusieurs outils qui vous permettent d'être explicite sur ce que vous attendez et de sauter ces vérifications encombrantes, par exemple, en définissant des paramètres comme non nuls ou avec un décorateur approprié.

### Codes d'erreur

Les codes d'erreur posent le même problème que les valeurs nulles et autres valeurs magiques, avec la complication supplémentaire de devoir, eh bien, gérer les codes d'erreur.

Vous pourriez décider de retourner le code d'erreur via un paramètre « out » :

```
int errorCode;var result = getSomething(out errorCode);if (errorCode != 0){    doSomethingWithResult(result);}
```

Vous pourriez choisir d'envelopper tous vos résultats dans une structure « Result » comme ceci (je suis très coupable de celle-ci, bien que cela ait été très utile pour les appels AJAX à l'époque) :

```
public class Result<T>{   public T Item { get; set; }   // Au moins "ErrorCode" est une énumération   public ErrorCode ErrorCode { get; set; } = ErrorCode.None;    public IsError { get { return ErrorCode != ErrorCode.None; } } }
```

```
public class UsingResultConstruct{   ...   var result = GetResult();   if (result.IsError)   {      switch (result.ErrorCode)      {         case ErrorCode.NetworkError:             HandleNetworkError();             break;         case ErrorCode.UserError:             HandleUserError();             break;         default:             HandleUnknownError();             break;      }   }   ActuallyDoSomethingWithResult(result);   ...}
```

Oui. C'est vraiment mauvais. La propriété Item pourrait encore être vide pour une raison quelconque, il n'y a aucune garantie réelle (en dehors de la convention) que lorsque le résultat ne contient pas d'erreur, vous pouvez accéder en toute sécurité à la propriété Item.

Après avoir terminé tout ce traitement, vous devez toujours traduire votre code d'erreur en un message d'erreur et faire quelque chose avec. Souvent, à ce stade, vous avez obscurci le problème original suffisamment pour ne pas avoir les détails exacts de ce qui s'est passé, donc vous ne pouvez même pas signaler l'erreur efficacement.

En plus de ce code horriblement et inutilement surcompliqué et illisible, un problème encore pire existe — si vous, ou quelqu'un d'autre, changez votre implémentation interne pour gérer un nouvel état invalide avec un nouveau code d'erreur, le code appelant n'aura **aucun moyen de savoir** qu'il doit gérer quelque chose qui a changé et **échouera** de manière imprévisible.

### Si au premier essai vous n'y arrivez pas, essayez, attrapez, enfin

Avant de continuer, cela pourrait être un bon moment pour mentionner que le fait que le code échoue silencieusement n'est pas une bonne chose. Échouer silencieusement signifie que les erreurs peuvent passer inaperçues pendant un certain temps avant d'exploser soudainement à des moments inconvenants et imprévisibles. Habituellement pendant le week-end. Les méthodes de gestion des erreurs précédentes vous **permettent** d'échouer silencieusement, donc peut-être, juste peut-être, qu'elles ne sont pas la meilleure façon de procéder.

![Image](https://cdn-media-1.freecodecamp.org/images/uJ6t46B9KpmPOCj1t9YGx48xEZcv-LSX-XdH)
_Photo par [Unsplash](https://unsplash.com/photos/iSTs6Lcu-Ek?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Scott Umstattd</a> sur <a href="https://unsplash.com/search/photos/spanish?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

À ce stade, si vous avez lu [Clean Code](https://www.oreilly.com/library/view/clean-code/9780136083238/), vous vous demandez probablement pourquoi quelqu'un ferait une de ces choses au lieu de simplement lancer une exception ? Si vous ne l'avez pas lu, vous pourriez penser que les exceptions sont la source de tous les maux. J'avais l'habitude de penser la même chose, mais maintenant je ne suis plus si sûre. Restez avec moi, voyons si nous pouvons nous mettre d'accord sur le fait que les exceptions ne sont pas toutes mauvaises, et pourraient même être assez utiles. Et si vous écrivez dans un langage sans exceptions ? Eh bien, c'est ce que c'est.

> _Une note intéressante, au moins pour moi, est que l'implémentation par défaut pour une nouvelle méthode C# est de lancer une NotImplementedException, tandis que la valeur par défaut pour une nouvelle méthode Python est « pass »._

> _Je ne suis pas sûre si c'est une convention C# ou simplement la façon dont mon Resharper était configuré, mais le résultat est essentiellement de configurer Python pour échouer silencieusement. Je me demande combien de développeurs ont passé une longue et triste session de débogage en essayant de comprendre ce qui se passait, pour finalement découvrir qu'ils avaient oublié d'implémenter une méthode de remplissage._

Mais attendez, vous pourriez facilement créer un fouillis encombré de vérifications d'erreurs et de lancers d'exceptions qui est assez similaire aux sections de vérification d'erreurs précédentes !

```
public MyDataObject UpdateSomething(MyDataObject toUpdate){    if (_dbConnection == null)    {         throw new DbConnectionError();    }    try    {        var newVersion = _dbConnection.Update(toUpdate);        if (newVersion == null)        {            return null;        }        MyDataObject result = new MyDataObject(newVersion);        return result;     }     catch (DbConnectionClosedException dbcc)     {         throw new DbConnectionError();     }     catch (MyDataObjectUnhappyException dou)     {         throw new MalformedDataException();     }     catch (Exception ex)     {         throw new UnknownErrorException();     }}
```

Ainsi, bien sûr, lancer des exceptions ne vous protégera pas d'un code illisible et ingérable. Vous devez appliquer le lancer d'exceptions comme une stratégie bien réfléchie. Si votre portée est trop grande, votre application pourrait se retrouver dans un état incohérent. Si votre portée est trop petite, vous vous retrouverez avec un fouillis encombré.

Mon approche à ce problème est la suivante :

**La cohérence est reine.** Vous devez vous assurer que votre application est toujours dans un état cohérent. Le code laid me rend triste, mais pas autant que les problèmes réels qui affectent les utilisateurs de ce que votre code fait réellement. Si cela signifie que vous devez envelopper chaque couple de lignes avec un bloc try/catch — cachez-les à l'intérieur d'une autre fonction.

```
def my_function():    try:        do_this()        do_that()    except:        something_bad_happened()    finally:        cleanup_resource()
```

**Consolidez les erreurs.** Il est acceptable que **vous** vous souciez des différents types d'erreurs qui doivent être gérées différemment, mais faites une faveur à vos utilisateurs et cachez cela en interne. Externement, lancez un seul type d'exception juste pour informer vos utilisateurs que quelque chose s'est mal passé. Ils ne devraient pas vraiment se soucier des détails, c'est votre responsabilité.

```
public MyDataObject UpdateSomething(MyDataObject toUpdate){    try    {                var newVersion = _dbConnection.Update(toUpdate);        MyDataObject result = new MyDataObject(newVersion);        return result;     }     catch (DbConnectionClosedException dbcc)     {         HandleDbConnectionClosed();         throw new UpdateMyDataObjectException();     }     catch (MyDataObjectUnhappyException dou)     {         RollbackVersion();         throw new UpdateMyDataObjectException();     }     catch (Exception ex)     {         throw new UpdateMyDataObjectException();     }}
```

**Attrapez tôt, attrapez souvent.** Attrapez vos exceptions aussi près de la source que possible, au niveau le plus bas possible. Maintenez la cohérence et cachez les détails (comme expliqué ci-dessus), puis essayez d'éviter de gérer les erreurs jusqu'au niveau le plus élevé de votre application. Espérons qu'il n'y ait pas trop de niveaux en cours de route. Si vous pouvez y parvenir, vous pourrez clairement séparer le flux normal de la logique de votre application du flux de gestion des erreurs, permettant à votre code d'être clair et concis sans mélanger les préoccupations.

```
def my_api():    try:        item = get_something_from_the_db()        new_version = do_something_to_item(item)        return new_version    except Exception as ex:        handle_high_level_exception(ex)
```

Merci d'avoir lu jusqu'ici, j'espère que cela a été utile ! De plus, je commence tout juste à former mes opinions sur ce sujet, donc je serais vraiment heureuse d'entendre quelle est votre stratégie pour gérer les erreurs. La section des commentaires est ouverte !