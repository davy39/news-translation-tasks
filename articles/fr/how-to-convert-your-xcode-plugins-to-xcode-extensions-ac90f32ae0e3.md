---
title: Comment convertir vos plugins Xcode en extensions Xcode
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-11T18:15:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-your-xcode-plugins-to-xcode-extensions-ac90f32ae0e3
coverImage: https://cdn-media-1.freecodecamp.org/images/0*1koaW2o_S4P9h9-H.jpg
tags:
- name: iOS
  slug: ios
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Xcode
  slug: xcode
seo_title: Comment convertir vos plugins Xcode en extensions Xcode
seo_desc: 'By Khoa Pham

  Xcode is an indispensable IDE for iOS and macOS developers. From the early days,
  the ability to build and install custom plugins had given us a huge boost in productivity.
  It was not long before Apple introduced Xcode extension due to pr...'
---

Par Khoa Pham

Xcode est un IDE indispensable pour les développeurs iOS et macOS. Dès les premiers jours, la possibilité de créer et d'installer des plugins personnalisés nous a donné un énorme gain de productivité. Il n'a pas fallu longtemps avant qu'Apple n'introduise les extensions Xcode en raison de préoccupations de confidentialité.

J'ai créé quelques plugins et extensions Xcode comme [XcodeWay](https://github.com/onmyway133/XcodeWay), [XcodeColorSense](https://github.com/onmyway133/XcodeColorSense), [XcodeColorSense2](https://github.com/onmyway133/XcodeColorSense2), et [Xmas](https://github.com/onmyway133/Xmas). Ce fut une expérience enrichissante. J'ai beaucoup appris, et le gain de productivité que j'ai obtenu était considérable. Dans cet article, je vous explique comment j'ai converti mes plugins Xcode en extensions, et l'expérience que j'ai eue en le faisant.

### Mon premier plugin Xcode : XcodeWay

> Je choisis une personne paresseuse pour faire un travail difficile. Parce qu'une personne paresseuse trouvera un moyen facile de le faire

J'aime vraiment la citation ci-dessus de [Bill Gates](https://www.goodreads.com/quotes/568877-i-choose-a-lazy-person-to-do-a-hard-job). J'essaie d'éviter les tâches répétitives et ennuyeuses. Chaque fois que je me surprends à faire les mêmes tâches encore et encore, j'écris des scripts et des outils pour les automatiser. Cela prend un peu de temps, mais je serai un peu plus paresseux dans un avenir proche.

En plus de l'intérêt de créer des [frameworks et outils](https://github.com/onmyway133/blog/issues/5) open source, j'aime étendre l'IDE que j'utilise — principalement Xcode.

J'ai commencé le développement iOS en 2014. Je voulais un moyen rapide de naviguer vers de nombreux endroits directement depuis Xcode avec le contexte du projet actuel. Il y a de nombreuses fois où nous voulons :

* ouvrir le dossier du projet actuel dans le "Finder" pour modifier certains fichiers
* ouvrir le Terminal pour exécuter certaines commandes
* ouvrir le fichier actuel dans GitHub pour donner rapidement le lien à un collègue
* ou pour ouvrir d'autres dossiers comme les thèmes, les plugins, les extraits de code, les journaux des appareils.

Chaque petite économie de temps que nous faisons chaque jour compte.

J'ai pensé que ce serait une bonne idée d'écrire un plugin Xcode qui nous permet de faire toutes ces choses directement dans Xcode. Au lieu d'attendre que d'autres personnes le fassent, j'ai retroussé mes manches et j'ai écrit mon premier plugin Xcode — [XcodeWay](https://github.com/onmyway133/XcodeWay) — et je l'ai partagé en open source.

![Image](https://cdn-media-1.freecodecamp.org/images/UsaS2cDc3Lcvo0vcGZ2S3wTl9Dw7VXE4ZPlX)
_XcodeWay fonctionne en créant un menu sous `Editor` avec de nombreuses options pour naviguer vers d'autres endroits directement depuis Xcode. Cela semble simple, mais il y avait un travail difficile requis._

### Qu'est-ce que les plugins Xcode ?

Les plugins Xcode ne sont pas officiellement supportés par Xcode ou recommandés par Apple. Il n'y a pas de documentation à leur sujet. Les meilleurs endroits où nous pouvons apprendre à leur sujet sont via le code source des plugins existants et quelques tutoriels.

Un plugin Xcode est simplement un bundle de type `xcplugin` et est placé dans `~/Library/Application Support/Developer/Shared/Xcode/Plug-ins`. Xcode, lors du démarrage, chargera tous les plugins Xcode présents dans ce dossier. Les plugins s'exécutent dans le même processus que Xcode, donc ils peuvent faire tout ce que Xcode peut faire. Un bug dans un plugin peut provoquer un crash de Xcode.

Pour créer un plugin Xcode, créez un `macOS Bundle` avec une classe qui étend `NSObject`, et qui a un initialiseur qui accepte `NSBundle`, par exemple dans [Xmas](https://github.com/onmyway133/Xmas/blob/master/Xmas/Xmas.swift) :

![Image](https://cdn-media-1.freecodecamp.org/images/EzOyELe5LTOCRpAtu0BsioFmMluYXqP7jdTM)

```
class Xmas: NSObject {
```

```
  var bundle: NSBundle
```

```
  init(bundle: NSBundle) {    self.bundle = bundle    super.init()  }}
```

Dans `Info.plist`, nous devons :

* déclarer cette classe comme la classe d'entrée principale pour le plugin, et
* que ce bundle n'a pas d'UI, car nous créons des contrôles UI et les ajoutons à l'interface Xcode pendant l'exécution

```
<key>NSPrincipalClass</key><string>Xmas</string><key>XCPluginHasUI</key><false/>
```

Un autre problème avec les plugins Xcode est que nous devons continuellement mettre à jour `DVTPluginCompatibilityUUIDs`. Cela change chaque fois qu'une nouvelle version de Xcode sort. Sans mise à jour, Xcode refusera de charger le plugin.

### Ce que les plugins Xcode peuvent faire

De nombreux développeurs créent des plugins Xcode car ils manquent de fonctionnalités spécifiques trouvées dans d'autres IDE comme Sublime Text, AppCode ou Atom.

Puisque les plugins Xcode sont chargés dans le même processus que Xcode, ils peuvent faire tout ce que Xcode peut faire. La seule limite est notre imagination. Nous pouvons utiliser le runtime Objective C pour découvrir des frameworks et fonctions privés. Ensuite, LLDB et les points d'arrêt symboliques peuvent être utilisés pour inspecter le code en cours d'exécution et modifier leurs comportements. Nous pouvons également utiliser le swizzling pour changer l'implémentation de tout code en cours d'exécution. L'écriture de plugins Xcode est difficile — beaucoup de conjectures, et parfois une bonne connaissance de l'assembleur est requise.

À l'âge d'or des plugins, il y avait un gestionnaire de plugins populaire, qui était lui-même un plugin, appelé [Alcatraz](https://github.com/alcatraz/Alcatraz). Il pouvait installer d'autres plugins, ce qui consistait essentiellement à télécharger le fichier `xcplugin` et à le déplacer dans le dossier `Plug Ins`.

![Image](https://cdn-media-1.freecodecamp.org/images/RNeR70XwT9oTBQQxHiXMrkCfNK3EhaBzyhoh)

Pour avoir une idée de ce que les plugins peuvent faire, examinons quelques plugins populaires.

#### Xvim

Le premier de la liste est [Xvim](https://github.com/XVimProject/XVim), qui ajoute des raccourcis clavier Vim directement dans Xcode. Il supporte la plupart des raccourcis clavier que nous avions l'habitude d'avoir dans le Terminal.

![Image](https://cdn-media-1.freecodecamp.org/images/5uRzbVcVrF7YfLPfEFWaRaMM9V3ZPmi9kqvU)

#### SCXcodeMiniMap

Si vous regrettez le mode MiniMap dans Sublime Text, vous pouvez utiliser [SCXcodeMiniMap](https://github.com/stefanceriu/SCXcodeMiniMap) pour ajouter un panneau de carte à droite dans l'éditeur Xcode.

![Image](https://cdn-media-1.freecodecamp.org/images/epSJCC4KrLrDlqW5Q80t0tUeGSpyYZGRyMPU)

#### FuzzyAutocompletePlugin

Avant la version 9, Xcode n'avait pas de complétion automatique appropriée — elle était basée uniquement sur le préfixe. C'est là que [FuzzyAutocompletePlugin](https://github.com/FuzzyAutocomplete/FuzzyAutocompletePlugin) brillait. Il effectue une complétion automatique floue basée sur la fonctionnalité cachée `IDEOpenQuicklyPattern` dans Xcode.

![Image](https://cdn-media-1.freecodecamp.org/images/jDyipJzu0YigAbvz7gteWoc2HFcr3Cag2tNk)

#### KSImageNamed-Xcode

Pour afficher une image de bundle dans `UIImageView`, nous utilisons souvent la méthode `imageNamed`. Mais se souvenir exactement du nom du fichier image est difficile. [KSImageNamed-Xcode](https://github.com/ksuther/KSImageNamed-Xcode) est là pour aider. Vous obtiendrez une liste de noms d'images suggérés automatiquement lorsque vous commencez à taper.

![Image](https://cdn-media-1.freecodecamp.org/images/s4A8NgJ6afZV8E9kpeCZ6EH8KkZyNPtq6Pxs)

#### ColorSense-for-Xcode

Un autre problème pendant le développement est de travailler avec `UIColor`, qui utilise l'espace colorimétrique RGBA. Nous n'avons pas d'indicateur visuel de la couleur que nous spécifions, et la vérification manuelle peut être chronophage. Heureusement, il y a [ColorSense-for-Xcode](https://github.com/omz/ColorSense-for-Xcode) qui montre la couleur utilisée et le panneau de sélection de couleur pour choisir facilement la bonne couleur.

![Image](https://cdn-media-1.freecodecamp.org/images/rVjJEdtXDZ1eFDHejstEgDLtdllhDFCayaM3)

#### LinkedConsole

Dans AppCode, nous pouvons sauter à une ligne spécifique dans le fichier qui est journalisé dans la console. Si vous regrettez cette fonctionnalité dans Xcode, vous pouvez utiliser [LinkedConsole](https://github.com/krzysztofzablocki/LinkedConsole). Cela active les liens cliquables dans la console Xcode afin que nous puissions sauter à ce fichier instantanément.

![Image](https://cdn-media-1.freecodecamp.org/images/5Qwhb8nHh4GIdWQCtDIw-eajwUucu2tkExcf)

### Le travail difficile derrière les plugins Xcode

Créer un plugin Xcode n'est pas facile. Non seulement nous devons connaître la programmation macOS, mais nous devons également plonger profondément dans la hiérarchie des vues Xcode. Nous devons explorer les frameworks et API privés afin d'injecter la fonctionnalité que nous voulons.

Il y a très peu de tutoriels sur la façon de créer des plugins, mais heureusement, la plupart des plugins sont open source, donc nous pouvons comprendre comment ils fonctionnent. Puisque j'ai créé quelques plugins, je peux donner quelques détails techniques à leur sujet.

Les plugins Xcode sont généralement réalisés avec deux frameworks privés : `DVTKit` et `IDEKit`. Les frameworks système se trouvent dans `/System/Library/PrivateFrameworks`, mais les frameworks que Xcode utilise exclusivement sont sous `/Applications/Xcode.app/Contents/`, où vous pouvez trouver `Frameworks`, `OtherFrameworks` et `SharedFrameworks`.

Il y a un outil [class-dump](https://github.com/nygard/class-dump) qui peut générer des en-têtes à partir du bundle de l'application Xcode. Avec les noms de classe et les méthodes, vous pouvez appeler `NSClassFromString` pour obtenir la classe à partir du nom.

#### Swizzling du framework DVTBezelAlertPanel dans Xmas

Noël m'a toujours donné un sentiment spécial, alors j'ai décidé de créer [Xmas](https://github.com/onmyway133/Xmas), qui affiche une image de Noël aléatoire au lieu de la vue d'alerte par défaut. La classe utilisée pour rendre cette vue est [DVTBezelAlertPanel](https://github.com/luisobo/Xcode-RuntimeHeaders/blob/master/DVTKit/DVTBezelAlertPanel.h) dans le framework DVTKit. [Mon article sur la création de ce plugin est ici.](https://medium.com/fantageek/xmas-9522c2c88db3)

![Image](https://cdn-media-1.freecodecamp.org/images/sHzqA7m3ACnL-pRYeN7SfDfo0qilF06HoxQU)

Avec le runtime Objective C, il y a une technique appelée swizzling, qui peut changer et échanger l'implémentation et la signature de méthode de toute classe et méthode en cours d'exécution.

Ici, afin de changer le contenu de cette vue d'alerte, nous devons échanger l'[initialiseur](https://github.com/onmyway133/Xmas/blob/master/Xmas/Xmas.swift) `initWithIcon:message:parentWindow:duration:` avec notre propre méthode. Nous le faisons tôt en écoutant `NSApplicationDidFinishLaunchingNotification` qui est notifié lorsqu'un plugin macOS, dans ce cas Xcode, se lance.

```
class func swizzleMethods() {    guard let originalClass = NSClassFromString("DVTBezelAlertPanel") as? NSObject.Type else {        return    }
```

```
do {        try originalClass.jr_swizzleMethod("initWithIcon:message:parentWindow:duration:",            withMethod: "xmas_initWithIcon:message:parentWindow:duration:")    }    catch {        Swift.print("Swizzling failed")    }}
```

Au début, j'aimais tout faire en Swift. Mais il est délicat d'utiliser la méthode [swizzle init en Swift](https://stackoverflow.com/questions/34317766/how-to-swizzle-init-in-swift), donc le moyen le plus rapide est de le faire en [Objective C](https://github.com/onmyway133/xmas/blob/master/Xmas/NSObject%2BXmas.m). Ensuite, nous traversons simplement la hiérarchie des vues pour trouver le `NSVisualEffectView` dans `NSPanel` afin de mettre à jour l'image.

#### Interaction avec DVTSourceTextView dans XcodeColorSense

Je travaille principalement avec des couleurs hexadécimales et je veux un moyen rapide de voir la couleur. J'ai donc créé XcodeColorSense — il supporte les couleurs hexadécimales, RGBA et les couleurs nommées.

![Image](https://cdn-media-1.freecodecamp.org/images/yfDV0dfqfsURAljntQXt1LymFG1AztzKT5Xq)

L'idée est simple. Analyser la chaîne pour voir si l'utilisateur tape quelque chose lié à `UIColor`, et afficher une petite vue en superposition avec cette couleur en arrière-plan. La vue de texte que Xcode utilise est de type `DVTSourceTextView` dans le framework `DVTKit`. Nous devons également écouter `NSTextViewDidChangeSelectionNotification` qui est déclenché chaque fois que le contenu d'un `NSTextView` est [modifié](https://github.com/onmyway133/XcodeColorSense/blob/master/XcodeColorSense/XcodeColorSense.swift).

```
func listenNotification() {  NSNotificationCenter.defaultCenter().addObserver(self, selector: #selector(handleSelectionChange(_:)), name: NSTextViewDidChangeSelectionNotification, object: nil)}
```

```
func handleSelectionChange(note: NSNotification) {  guard let DVTSourceTextView = NSClassFromString("DVTSourceTextView") as? NSObject.Type,    object = note.object where object.isKindOfClass(DVTSourceTextView.self),    let textView = object as? NSTextView  else { return }
```

```
self.textView = textView}
```

J'avais une architecture Matcher afin que nous puissions détecter différents types de constructions `UIColor` — par exemple [HexMatcher](https://github.com/onmyway133/XcodeColorSense/blob/master/XcodeColorSense/Matcher/HexMatcher.swift).

```
public struct HexMatcher: Matcher {
```

```
func check(line: String, selectedText: String) -> (color: NSColor, range: NSRange)? {    let pattern1 = "\"#?[A-Fa-f0-9]{6}\""    let pattern2 = "0x[A-Fa-f0-9]{6}"
```

```
let ranges = [pattern1, pattern2].flatMap {      return Regex.check(line, pattern: $0)    }
```

```
guard let range = ranges.first      else { return nil }
```

```
let text = (line as NSString).substringWithRange(range).replace("0x", with: "").replace("\"", with: "")    let color = NSColor.hex(text)
```

```
return (color: color, range: range)  }}
```

Pour rendre la superposition, nous utilisons `NSColorWell` qui est bon pour afficher une vue avec un arrière-plan. La position est déterminée en appelant `firstRectForCharacterRange` et quelques conversions de points avec `convertRectFromScreen` et `convertRect`.

#### Utilisation de NSTask et IDEWorkspaceWindowController dans XcodeWay

Enfin, mon bien-aimé [XcodeWay](https://github.com/onmyway133/XcodeWay/tree/1.0).

J'ai remarqué que j'avais besoin d'aller à différents endroits depuis Xcode avec le contexte du projet actuel. J'ai donc créé XcodeWay comme un plugin qui ajoute de nombreuses options de menu pratiques sous `Window`.

![Image](https://cdn-media-1.freecodecamp.org/images/NWfrvwX1RWXLoUDS24gETXJ8PwZLf5J1bUCN)

Puisque le plugin s'exécute dans le même processus Xcode, il a accès au menu principal `NSApp.mainMenu?.itemWithTitle("Window")`. Là, nous pouvons modifier le menu. XcodeWay est conçu pour étendre facilement les fonctionnalités grâce à son protocole [Navigator](https://github.com/onmyway133/XcodeWay/blob/1.0/XcodeWay/Navigator/Navigator.swift).

```
@objc protocol Navigator: NSObjectProtocol {  func navigate()  var title: String { get }}
```

Pour les dossiers avec un chemin statique comme le profil de provisionnement `~/Library/MobileDevice/Provisioning Profiles` ou les données utilisateur `Developer/Xcode/UserData`, nous pouvons simplement construire l'`URL` et appeler `NSWorkspace.sharedWorkspace().openURL`. Pour les dossiers dynamiques qui varient en fonction du projet actuel, plus de travail doit être fait.

Comment ouvrir le dossier du projet actuel dans Finder ? Les informations sur le chemin du projet actuel sont conservées dans `IDEWorkspaceWindowController`. Il s'agit d'une classe qui gère les fenêtres d'espace de travail dans Xcode. Jetez un œil à [EnvironmentManager](https://github.com/onmyway133/XcodeWay/blob/1.0/XcodeWay/Helper/FTGEnvironmentManager.m) où nous utilisons [objc_getClass](https://developer.apple.com/documentation/objectivec/1418952-objc_getclass?language=objc) pour obtenir la définition de la classe à partir d'une chaîne.

```
self.IDEWorkspaceWindowControllerClass = objc_getClass("IDEWorkspaceWindowController");
```

```
NSArray *workspaceWindowControllers = [self.IDEWorkspaceWindowControllerClass valueForKey:@"workspaceWindowControllers"];
```

```
id workSpace = nil;
```

```
for (id controller in workspaceWindowControllers) {  if ([[controller valueForKey:@"window"] isEqual:[NSApp keyWindow]]) {    workSpace = [controller valueForKey:@"_workspace"];  }}
```

```
NSString * path = [[workSpace valueForKey:@"representingFilePath"] valueForKey:@"_pathString"];
```

Enfin, nous pouvons utiliser `valueForKey` pour obtenir la valeur de toute propriété que nous pensons exister. De cette façon, non seulement nous obtenons le [chemin du projet](https://github.com/onmyway133/XcodeWay/blob/1.0/XcodeWay/Navigator/FTGProjectFolderNavigator.m), mais nous obtenons également le chemin vers le fichier ouvert. Nous pouvons donc appeler `activateFileViewerSelectingURLs` sur `NSWorkspace` pour ouvrir Finder avec ce fichier sélectionné. Cela est pratique car les utilisateurs n'ont pas besoin de chercher ce fichier dans Finder.

De nombreuses fois, nous voulons exécuter certaines commandes Terminal dans le dossier du projet actuel. Pour y parvenir, nous pouvons utiliser `NSTask` avec le lanceur `/usr/bin/open` et les arguments `[@"-a", @"Terminal", projectFolderPath]`. iTerm, s'il est configuré correctement, ouvrira cela dans un nouvel onglet.

Les documents pour les applications iOS 7 sont placés dans l'emplacement fixe `iPhone Simulator` dans Application Support. Mais, à partir d'iOS 8, chaque application a un UUID unique et leurs [dossiers de documents](https://github.com/onmyway133/XcodeWay/blob/1.0/XcodeWay/Navigator/FTGSimulatorFolderNavigator.m) sont difficiles à prédire.

```
~/Library/Developer/CoreSimulator/Devices/1A2FF360-B0A6-8127-95F3-68A6AB0BCC78/data/Container/Data/Application/
```

Nous pouvons construire une carte et effectuer un suivi pour trouver l'ID généré pour le projet actuel, ou vérifier le plist dans chaque dossier pour comparer l'identifiant du bundle.

La solution rapide que j'ai trouvée était de rechercher le dossier le plus récemment mis à jour. Chaque fois que nous construisons le projet, ou apportons des modifications dans l'application, leur dossier de documents est mis à jour. C'est là que nous pouvons utiliser `NSFileModificationDate` pour trouver le dossier du projet actuel.

Il y a beaucoup de hacks lors de la création de plugins Xcode, mais les résultats sont gratifiants. Chaque minute que nous économisons chaque jour finit par économiser beaucoup de temps globalement.

### Sécurité et liberté

Un grand pouvoir implique de grandes responsabilités. Le fait que les plugins puissent faire tout ce qu'ils veulent sonne comme une alerte pour la sécurité. Fin 2015, il y a eu une attaque de malware en distribuant une version modifiée de Xcode, appelée [XcodeGhost](https://en.wikipedia.org/wiki/XcodeGhost), qui injecte du code malveillant dans toute application construite avec Xcode Ghost. Le malware est censé utiliser le mécanisme de plugin parmi d'autres choses.

Comme les applications iOS que nous téléchargeons depuis l'Appstore, les applications macOS comme Xcode sont [signées](https://developer.apple.com/support/code-signing/) par Apple lorsque nous les téléchargeons depuis le Mac Appstore ou via les liens de téléchargement officiels d'Apple.

**La signature de code de votre application** assure aux utilisateurs qu'elle provient d'une source connue et que l'application n'a pas été modifiée depuis sa dernière signature. Avant que votre application puisse intégrer des services d'application, être installée sur un appareil ou être soumise à l'App Store, elle doit être signée avec un [certificat](https://developer.apple.com/support/technical/certificates/) émis par Apple.

Pour éviter les malwares potentiels comme celui-ci, lors de la WWDC 2016, Apple a annoncé l'[Xcode Source Editor Extension](https://developer.apple.com/videos/play/wwdc2016/414/) comme le seul moyen de charger des extensions tierces dans Xcode. Cela signifie que, à partir de Xcode 8, les plugins ne peuvent plus être chargés.

#### Extension Source Editor

L'[Extension](https://developer.apple.com/app-extensions/) est l'approche recommandée pour ajouter des fonctionnalités de manière sûre et restreinte.

Les extensions d'application donnent aux utilisateurs accès à la fonctionnalité et au contenu de votre application dans tout iOS et macOS. Par exemple, votre application peut maintenant apparaître comme un widget sur l'écran Aujourd'hui, ajouter de nouveaux boutons dans la feuille d'Action, offrir des filtres photo dans l'application Photos, ou afficher un nouveau clavier personnalisé à l'échelle du système.

Pour l'instant, la seule extension pour Xcode est Source Editor, qui nous permet de lire et de modifier le contenu d'un fichier source, ainsi que de lire et de modifier la sélection de texte actuelle dans l'éditeur.

L'extension est une nouvelle cible et s'exécute dans un processus différent de Xcode. Cela est bien car elle ne peut pas altérer Xcode de quelque manière que ce soit autre que de se conformer à `XCSourceEditorCommand` pour modifier le contenu du document actuel.

```
protocol XCSourceEditorCommand {
```

```
  func perform(with invocation: XCSourceEditorCommandInvocation, completionHandler: @escaping (Error?) -> Void)}
```

![Image](https://cdn-media-1.freecodecamp.org/images/jfIwqKJH9VDhnI2H0JObOUPK8o0QlSstXqFR)

Xcode 8 a de nombreuses améliorations comme les nouvelles fonctionnalités de complétion de code, les littéraux d'image et de couleur Swift, et les extraits de code. Cela a conduit à la dépréciation de nombreux plugins Xcode. Pour certains plugins indispensables comme XVim, cela est insupportable pour certaines personnes. Certaines anciennes fonctionnalités de plugins ne peuvent pas être réalisées avec le système actuel d'extension Source Editor.

#### À moins que vous ne resigniez Xcode

Une solution de contournement pour contourner la restriction de Xcode 8 pour les plugins est de remplacer la signature existante de Xcode par une technique appelée [resign](https://github.com/XVimProject/XVim2/blob/master/SIGNING_Xcode.md). La resignature est très facile — nous devons simplement créer un certificat auto-signé et appeler la commande `codesign`. Après cela, Xcode devrait être en mesure de charger les plugins.

![Image](https://cdn-media-1.freecodecamp.org/images/95nZAgqJJKpYgm9nZT-INsndKwgDJYdl1QmD)

```
codesign -f -s MySelfSignedCertificate /Applications/Xcode.app
```

Il est, cependant, **impossible** de soumettre des applications construites avec Xcode resigné car la signature ne correspond pas à la version officielle de Xcode. Une solution est d'utiliser deux Xcodes : un officiel pour la distribution et un resigné pour le développement.

### Passage aux extensions Xcode

Les extensions Xcode sont la voie à suivre, donc j'ai commencé à convertir mes plugins en extensions. Pour Xmas, puisque cela modifie la hiérarchie des vues, cela ne peut pas devenir une extension.

#### Littéral de couleur dans XcodeColorSense2

Pour le sens des couleurs, j'ai réécrit l'extension à partir de zéro, et je l'ai appelée [XcodeColorSense2](https://github.com/onmyway133/XcodeColorSense2). Cela, bien sûr, ne peut pas afficher une superposition sur la vue de l'éditeur actuel. J'ai donc choisi d'utiliser le nouveau `Color literal` trouvé dans Xcode 8+.

![Image](https://cdn-media-1.freecodecamp.org/images/JoHeQ87KD4m-vTjhCoUy0Ua9XkaG4K9tdVj-)

La couleur est affichée dans une petite boîte. Il peut être difficile de distinguer les couleurs similaires, c'est pourquoi j'inclus également le nom. Le code consiste simplement à inspecter les `selections` et à analyser pour trouver la déclaration de couleur.

```
func perform(with invocation: XCSourceEditorCommandInvocation, completionHandler: @escaping (Error?) -> Void ) -> Void {    guard let selection = invocation.buffer.selections.firstObject as? XCSourceTextRange else {      completionHandler(nil)      return    }
```

```
let lineNumber = selection.start.line
```

```
guard lineNumber < invocation.buffer.lines.count,      let line = invocation.buffer.lines[lineNumber] as? String else {      completionHandler(nil)      return    }
```

```
guard let hex = findHex(string: line) else {      completionHandler(nil)      return    }
```

```
let newLine = process(line: line, hex: hex)
```

```
invocation.buffer.lines.replaceObject(at: lineNumber, with: newLine)
```

```
completionHandler(nil)  }}
```

La plupart des fonctionnalités sont intégrées dans mon framework [Farge](https://github.com/onmyway133/Farge), mais je ne trouve pas de moyen d'utiliser le [framework à l'intérieur de l'extension Xcode](https://stackoverflow.com/questions/43673353/how-to-use-framework-in-xcode-source-editor-extension).

Puisque la fonctionnalité de l'extension n'est accessible que via le menu Éditeur, nous pouvons personnaliser un raccourci clavier pour invoquer cet élément de menu. Par exemple, j'ai choisi `Cmd+Ctrl+S` pour afficher et masquer les informations de couleur.

![Image](https://cdn-media-1.freecodecamp.org/images/CznmGCwhrAIoo7eXrgN0EklxQy-L30pPVzXx)

Cela n'est, bien sûr, pas intuitif par rapport au plugin d'origine, mais c'est mieux que rien.

#### Comment déboguer les extensions Xcode

Travailler et déboguer les extensions est simple. Nous pouvons utiliser Xcode pour déboguer Xcode. La version déboguée de Xcode a une icône grise.

![Image](https://cdn-media-1.freecodecamp.org/images/hB3h0Rpjc97sVm1aQKU52yNjh5sHZvCCsq1n)

#### Comment installer les extensions Xcode

L'extension doit avoir une application macOS accompagnante. Celle-ci peut être distribuée sur le Mac Appstore ou auto-signée. [J'ai écrit un article sur la façon de faire cela](https://medium.com/fantageek/install-xcode-8-source-editor-extension-10c9849e33b0).

Toutes les extensions pour une application doivent être explicitement activées via les "Préférences Système".

![Image](https://cdn-media-1.freecodecamp.org/images/8pLbJHO2TO0HSsTKeUnT7xwyFdy-YrzkG5Xs)

L'extension Xcode ne fonctionne pour l'instant qu'avec l'éditeur, donc nous devons ouvrir un fichier source pour que le menu `Editor` ait un effet.

### AppleScript dans XcodeWay

Dans les extensions Xcode, `NSWorkspace`, `NSTask` et la construction de classes privées ne fonctionnent plus. Puisque j'ai utilisé Finder Sync Extension dans [FinderGo](https://github.com/onmyway133/FinderGo), j'ai pensé que je pourrais essayer le même script AppleScript pour l'extension Xcode.

[AppleScript](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html) est un langage de script créé par Apple. Il permet aux utilisateurs de contrôler directement les applications Macintosh scriptables, ainsi que certaines parties de macOS lui-même. Vous pouvez créer des scripts — des ensembles d'instructions écrites — pour automatiser les tâches répétitives, combiner des fonctionnalités de plusieurs applications scriptables et créer des flux de travail complexes.

Pour essayer AppleScript, vous pouvez utiliser l'application Script Editor intégrée dans macOS pour écrire des fonctions prototypes. La déclaration de fonction commence par `on` et se termine par `end`. Pour éviter les conflits potentiels avec les fonctions système, j'utilise généralement `my` comme préfixe. Voici comment je m'appuie sur System Events pour obtenir le répertoire personnel.

La terminologie de [scripting de l'interface utilisateur](https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/AutomatetheUserInterface.html) se trouve dans la "Suite de processus" du dictionnaire de scripting "System Events". Cette suite inclut la terminologie pour interagir avec la plupart des types d'éléments d'interface utilisateur, y compris :

* fenêtres
* boutons
* cases à cocher
* menus
* boutons radio
* champs de texte.

Dans System Events, la classe `process` représente une application en cours d'exécution.

![Image](https://cdn-media-1.freecodecamp.org/images/NXmx4UIXeqYxT4qUKrc7PoNnlkIg1tEZJbH6)

De nombreuses applications bien conçues supportent AppleScript en exposant certaines de leurs fonctionnalités, afin que celles-ci puissent être utilisées par d'autres applications. Voici comment j'obtiens la chanson actuelle de Spotify dans [Lyrics](https://github.com/onmyway133/Lyrics).

```
tell application "Spotify"  set trackId to id of current track as string  set trackName to name of current track as string  set artworkUrl to artwork url of current track as string  set artistName to artist of current track as string  set albumName to album of current track as string  return trackId & "---" & trackName & "---" & artworkUrl & "---" & artistName & "---" & albumNameend tell
```

Pour obtenir toutes les commandes possibles d'une certaine application, nous pouvons ouvrir le dictionnaire dans Script Editor. Là, nous pouvons apprendre quelles fonctions et paramètres sont supportés.

![Image](https://cdn-media-1.freecodecamp.org/images/8kuHy0Z79lJsdzFhn7NJuJ53iDX9cU7I30nH)

Si vous pensez que Objective C est difficile, AppleScript est beaucoup plus difficile. La syntaxe est verbeuse et sujette aux erreurs. Pour référence, voici le [fichier de script complet](https://github.com/onmyway133/XcodeWay/blob/master/XcodeWayExtensions/Script/XcodeWayScript.scpt) qui alimente XcodeWay.

Pour ouvrir un certain dossier, dites à `Finder` d'utiliser `POSIX file`. Je refactorise chaque fonctionnalité en fonction pour une meilleure réutilisation du code.

```
on myOpenFolder(myPath)tell application "Finder"activateopen myPath as POSIX fileend tellend myOpenFolder
```

Ensuite, pour exécuter AppleScript dans une application ou une extension macOS, nous devons construire un [descripteur AppleScript](https://github.com/onmyway133/XcodeWay/blob/master/XcodeWayExtensions/Helper/ScriptRunner.swift) avec le bon numéro de série de processus et les identifiants d'événement.

```
func eventDescriptior(functionName: String) -> NSAppleEventDescriptor {  var psn = ProcessSerialNumber(highLongOfPSN: 0, lowLongOfPSN: UInt32(kCurrentProcess))  let target = NSAppleEventDescriptor(    descriptorType: typeProcessSerialNumber,    bytes: &psn,    length: MemoryLayout<ProcessSerialNumber>.size  )
```

```
let event = NSAppleEventDescriptor(    eventClass: UInt32(kASAppleScriptSuite),    eventID: UInt32(kASSubroutineEvent),    targetDescriptor: target,    returnID: Int16(kAutoGenerateReturnID),    transactionID: Int32(kAnyTransactionID)  )
```

```
let function = NSAppleEventDescriptor(string: functionName)  event.setParam(function, forKeyword: AEKeyword(keyASSubroutineName))
```

```
return event}
```

D'autres tâches, comme la vérification du dépôt Git actuel, sont un peu plus délicates. De nombreuses fois, je veux partager le lien du fichier que je débogue avec un collègue distant, afin qu'ils sachent quel fichier je référence. Cela est possible en utilisant `shell script` dans `AppleScript`.

```
on myGitHubURL()set myPath to myProjectPath()set myConsoleOutput to (do shell script "cd " & quoted form of myPath & "; git remote -v")set myRemote to myGetRemote(myConsoleOutput)set myUrl to (do shell script "cd " & quoted form of myPath & "; git config --get remote." & quoted form of myRemote & ".url")set myUrlWithOutDotGit to myRemoveSubString(myUrl, ".git")end myGitHubURL
```

Nous pouvons utiliser `quoted` et la concaténation de chaînes pour former des chaînes. Heureusement, nous pouvons exposer le framework `Foundation` et certaines classes. Voici comment j'expose `NSString` pour tirer parti de toutes les fonctionnalités existantes. Écrire la manipulation de chaînes à partir de zéro en utilisant AppleScript pur prendrait beaucoup de temps.

```
use scripting additionsuse framework "Foundation"property NSString : a reference to current application's NSString
```

Avec cela, nous pouvons construire nos autres fonctions pour la gestion des chaînes.

```
on myRemoveLastPath(myPath)set myString to NSString's stringWithString:myPathset removedLastPathString to myString's stringByDeletingLastPathComponentremovedLastPathString as textend myRemoveLastPath
```

Une fonctionnalité intéressante que XcodeWay supporte est la capacité d'aller au répertoire de documents pour l'application actuelle dans le simulateur. Cela est pratique lorsque nous devons inspecter un document pour vérifier les données enregistrées ou mises en cache. Le répertoire est dynamique, il est donc difficile à détecter. Nous pouvons, cependant, trier le répertoire pour le plus récemment mis à jour. Voici comment nous enchaînons plusieurs commandes `shell scripts` pour trouver le dossier.

```
on myOpenDocument()set command1 to "cd ~/Library/Developer/CoreSimulator/Devices/;"set command2 to "cd `ls -t | head -n 1`/data/Containers/Data/Application;"set command3 to "cd `ls -t | head -n 1`/Documents;"set command4 to "open ."do shell script command1 & command2 & command3 & command4end myOpenDocument
```

Cette fonctionnalité m'a beaucoup aidé lors du développement de [Gallery](https://github.com/hyperoslo/Gallery) pour vérifier si les vidéos et les images téléchargées sont enregistrées au bon endroit.

Cependant, aucun des scripts ne semble fonctionner. Le scripting a toujours fait partie de macOS depuis 1993. Mais, avec l'avènement du Mac Appstore et les préoccupations de sécurité, AppleScript a finalement été restreint à la mi-2012. C'est à ce moment-là que le bac à sable des applications a été imposé.

#### App Sandbox

App Sandbox est une technologie de contrôle d'accès fournie dans macOS, appliquée au niveau du noyau. Elle est conçue pour limiter les dommages au système et aux données de l'utilisateur si une application est compromise. Les applications distribuées via le Mac App Store doivent adopter [App Sandbox](https://www.objc.io/issues/14-mac/sandbox-scripting/).

![Image](https://cdn-media-1.freecodecamp.org/images/JrY-Maab-l1wSen8kIgwgQqnqW9yd5gADtHi)

Pour qu'une extension Xcode soit chargée par Xcode, elle doit également supporter App Sandbox.

![Image](https://cdn-media-1.freecodecamp.org/images/aCULPMrfSJYeoPA33YmhW4Ml5vHqzH1wshZS)

Au début de l'application de App Sandbox, nous pouvions utiliser [App Sandbox Temporary Exception](https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/AppSandboxTemporaryExceptionEntitlements.html) pour accorder temporairement à notre application l'accès à Apple Script.

Cela n'est plus possible.

Le seul moyen pour AppleScript de s'exécuter est qu'il réside dans le dossier `~/Library/Application Scripts`.

![Image](https://cdn-media-1.freecodecamp.org/images/ZlpA42RZZeUmtl2oBgAXU2N2dGRostKLqilr)

#### Comment installer des scripts personnalisés

Les applications ou extensions macOS ne peuvent pas simplement installer des scripts dans les scripts d'application par elles-mêmes. Elles ont besoin du consentement de l'utilisateur.

Une façon possible de le faire est d'activer `Read/Write` et d'afficher une boîte de dialogue en utilisant `NSOpenPanel` pour demander à l'utilisateur de sélectionner le dossier pour installer nos scripts.

![Image](https://cdn-media-1.freecodecamp.org/images/UJAyb9UOLiljUuacRZxW7Vvm1U2fvldOMM0D)

Pour XcodeWay, j'ai choisi de fournir un [script d'installation shell](https://github.com/onmyway133/XcodeWay/blob/master/install.sh) afin que l'utilisateur ait un moyen rapide d'installer les scripts.

```
#!/bin/bash
```

```
set -euo pipefail
```

```
DOWNLOAD_URL=https://raw.githubusercontent.com/onmyway133/XcodeWay/master/XcodeWayExtensions/Script/XcodeWayScript.scptSCRIPT_DIR="${HOME}/Library/Application Scripts/com.fantageek.XcodeWayApp.XcodeWayExtensions"
```

```
mkdir -p "${SCRIPT_DIR}"curl $DOWNLOAD_URL -o "${SCRIPT_DIR}/XcodeWayScript.scpt"
```

AppleScript est très puissant. Tout cela est rendu explicite afin que l'utilisateur ait un contrôle complet sur les choses qui peuvent être faites.

Comme une extension, un script est exécuté de manière asynchrone dans un processus différent en utilisant [XPC](https://www.objc.io/issues/14-mac/xpc/) pour la communication inter-processus. Cela améliore la sécurité car un script n'a pas accès à l'espace d'adressage de notre application ou extension.

### Plus de sécurité dans macOS Mojave

Cette année, lors de la WWDC 2018, Apple a introduit macOS Mojave qui se concentre sur de nombreuses améliorations de sécurité. Dans [Vos applications et l'avenir de la sécurité macOS](https://developer.apple.com/videos/play/wwdc2018/702/), nous pouvons en apprendre davantage sur les nouvelles exigences de sécurité pour les applications macOS. L'une d'entre elles est la description d'utilisation pour AppleEvents.

> impossible de charger les exceptions info.plist (egpu overrides)

Nous avions l'habitude de déclarer la description d'utilisation pour de nombreuses permissions dans iOS, comme la bibliothèque de photos, la caméra et les notifications push. Maintenant, nous devons déclarer la description d'utilisation pour AppleEvents.

![Image](https://cdn-media-1.freecodecamp.org/images/qCcXKO1fvLMoI07d04f1UudrLxapIeglYZk0)
_Source : [https://www.felix-schwarz.org/blog/2018/08/new-apple-event-apis-in-macos-mojave](https://www.felix-schwarz.org/blog/2018/08/new-apple-event-apis-in-macos-mojave" rel="noopener" target="_blank" title=")_

La première fois que notre extension tente d'exécuter certaines commandes AppleScript, la boîte de dialogue ci-dessus s'affiche pour demander le consentement de l'utilisateur. L'utilisateur peut accorder ou refuser la permission, mais pour Xcode, veuillez dire oui ?

La solution pour nous est de déclarer `NSAppleEventsUsageDescription` dans notre cible d'application. Nous devons seulement déclarer dans la cible de l'application, pas dans la cible de l'extension.

```
<key>NSAppleEventsUsageDescription</key><string>Utiliser AppleScript pour ouvrir des dossiers</string>
```

### Où aller à partir de là

Ouf, merci d'avoir suivi un si long voyage. La création de frameworks et d'outils prend beaucoup de temps, surtout les plugins et les extensions — nous devons continuellement les changer pour les adapter aux nouveaux systèmes d'exploitation et aux exigences de sécurité. Mais c'est un processus gratifiant, car nous avons appris davantage et avons quelques outils pour économiser notre temps précieux.

Pour référence, voici mes extensions qui sont entièrement open source.

* [XcodeWay](https://github.com/onmyway133/XcodeWay)
* [XcodeColorSense2](https://github.com/onmyway133/XcodeColorSense2)

J'espère que vous trouverez quelque chose d'utile dans cet article. Voici quelques ressources pour explorer davantage les extensions Xcode :

* [Plugins Xcode par NSHipster](https://nshipster.com/xcode-plugins/)
* [Écrire un plugin Xcode en Swift](http://merowing.info/2015/12/writing-xcode-plugin-in-swift/)
* [Plugins Xcode 8 (Alcatraz) — La fin d'une ère](https://medium.com/rocknnull/xcode-8-plugins-alcatraz-the-end-of-an-era-ea6e63617d14)
* [Utilisation et extension de l'éditeur de source Xcode](https://developer.apple.com/videos/play/wwdc2016/414/)
* [Pourquoi dois-je resigner Xcode pour utiliser XVim2](https://github.com/XVimProject/XVim2/blob/master/why_resign_xcode.md)

Si vous aimez cet article, envisagez de visiter [mes autres articles](https://github.com/onmyway133/blog/issues/165) et [applications](https://onmyway133.github.io/) ?