---
title: Comment gérer le clavier lors de la mise au point sur UITextField pour une
  meilleure expérience utilisateur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-18T13:55:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-manage-the-keyboard-on-uitextfield-focus-for-a-better-user-experience-1320c057b7c5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YS8FnU0cwKiPCoxMATqQ-A.png
tags:
- name: iOS
  slug: ios
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: Comment gérer le clavier lors de la mise au point sur UITextField pour
  une meilleure expérience utilisateur
seo_desc: 'By Roland Leth

  A couple of posts ago I was writing about handling the Next button automatically.
  In this post I’d like to write about avoiding the keyboard automatically, in a manner
  that provides both a good user experience and a good developer expe...'
---

Par Roland Leth

Il y a quelques [articles](https://rolandleth.com/handling-the-next-button-automatically), j'écrivais sur la gestion automatique du bouton Suivant. Dans cet article, j'aimerais écrire sur l'évitement automatique du clavier, de manière à offrir à la fois une bonne expérience utilisateur et une bonne expérience développeur.

La plupart des applications ont _quelque_ sorte de formulaire à remplir, même s'il s'agit simplement d'une connexion/enregistrement, sinon plusieurs formulaires. En tant qu'utilisateur, avoir le clavier qui couvre le champ de texte que je m'apprête à remplir me rend triste — c'est une mauvaise expérience utilisateur. En tant que développeurs, nous aimerions résoudre cela aussi facilement que possible et avoir une solution aussi réutilisable que possible.

Qu'est-ce qu'une bonne expérience utilisateur signifie ?

* Le `UITextField` focalisé est placé au-dessus du clavier lors de la mise au point.
* Le `UITextField` focalisé est "renvoyé en arrière" lors de la disparition.

Qu'est-ce qu'une bonne expérience développeur signifie ? Tout devrait se passer aussi automatiquement que possible, donc nous allons utiliser un protocole une fois de plus. Que doit encapsuler ce protocole ?

* Observer le clavier affichera/masquera les notifications.
* À l'apparition du clavier, il doit modifier le `scrollView.contentInset` et le `scrollView.contentOffset` de manière à placer le `UITextField` juste au-dessus du clavier.
* À la disparition du clavier, il doit réinitialiser l'insertion et le décalage aux valeurs précédentes.

Avec cela en tête, construisons notre protocole :

```
protocol KeyboardListener: AnyObject { // 1
```

```
   var scrollView: UIScrollView { get } // 2   var contentOffsetPreKeyboardDisplay: CGPoint? { get set } // 3   var contentInsetPreKeyboardDisplay: UIEdgeInsets? { get set } // 4
```

```
   func keyboardChanged(with notification: Notification) // 5
```

```
}
```

Nous devons contraindre ce protocole à être conforme uniquement par des classes (1) car nous devrons modifier les deux propriétés `preKeyboard` (3, 4). Nous les utiliserons pour savoir comment réinitialiser l'insertion et le décalage du `scrollView` lors de la disparition du clavier. Nous implémenterons probablement cela dans un `UIViewController` de toute façon.

Le protocole doit également avoir un `scrollView` (2), sinon ce n'est pas vraiment... réalisable (je suppose que cela pourrait être _faisable_). Enfin, nous avons besoin de la méthode qui gérera tout (5), mais elle agit simplement comme un proxy pour deux aides que nous implémenterons dans un instant :

```
extension KeyboardListener {
```

```
   func keyboardChanged(with notification: Notification) {      guard         notification.name == UIResponder.keyboardWillShowNotification,         let rawFrameEnd = notification.userInfo?[UIResponder.keyboardFrameEndUserInfoKey],         let frameEnd = rawFrameEnd as? CGRect,         let duration = notification.userInfo?[UIResponder.keyboardAnimationDurationUserInfoKey] as? TimeInterval      else {         resetScrollView() // 1
```

```
         return      }
```

```
      if let currentTextField = UIResponder.current as? UITextField {         updateContentOffsetOnTextFieldFocus(currentTextField, bottomCoveredArea: frame.height) // 2      }
```

```
      scrollView.contentInset.bottom += frameEnd.height // 3   }
```

```
}
```

Si la notification n'est pas pour `willShow`, ou si nous ne pouvons pas analyser le `userInfo` de la notification, abandonnez et réinitialisez le `scrollView`. Si c'est le cas, augmentez l'insertion inférieure de la hauteur du clavier (3). En ce qui concerne (2), nous trouvons le premier répondant actuel avec [une petite astuce](https://stackoverflow.com/a/40352519/793916) pour appeler `updateContentOffsetOnTextFieldFocus(_:bottomCoveredArea:)`, mais nous pourrions également l'appeler depuis notre délégué `textFieldShouldBeginEditing(_:)`.

Le premier assistant mettra à jour nos deux propriétés `preKeyboard` :

```
extension KeyboardListener where Self: UIViewController { // 1
```

```
   func keyboardChanged(with notification: Notification) {      // [...]   }
```

```
   func updateContentOffsetOnTextFieldFocus(_ textField: UITextField, bottomCoveredArea: CGFloat) {      let projectedKeyboardY = view.window!.frame.minY - bottomCoveredArea // 2
```

```
      if contentInsetPreKeyboardDisplay == nil { // 3         contentInsetPreKeyboardDisplay = scrollView.contentInset      }      if contentOffsetPreKeyboardDisplay == nil { // 4         contentOffsetPreKeyboardDisplay = scrollView.contentOffset      }
```

```
      let textFieldFrameInWindow = view.window!.convert(textField.frame,                                                        from: textField.superview) // 5      let bottomLimit = textFieldFrameInWindow.maxY + 10 // 6
```

```
      guard bottomLimit > projectedKeyboardY else { return } // 7
```

```
      let delta = projectedKeyboardY - bottomLimit // 8      let newOffset = CGPoint(x: scrollView.contentOffset.x,                              y: scrollView.contentOffset.y - delta) // 9
```

```
      scrollView.setContentOffset(newOffset, animated: true) // 10   }
```

```
}
```

Nous allons maintenant mettre à jour l'extension de protocole avec une contrainte `Self: UIViewController` (1), car nous aurons besoin d'accéder à la fenêtre. Cela ne devrait pas être un inconvénient, car ce protocole sera probablement utilisé par des `UIViewController`. Cependant, une autre approche serait de remplacer toutes les occurrences de `view.window` par `UIApplication.shared.keyWindow` ou une variation de `UIApplication.shared.windows[yourIndex]`, au cas où vous auriez une hiérarchie complexe.

Nous calculons ensuite le `minY` pour le clavier (2) — nous utilisons un paramètre pour ces cas où nous avons une `inputView` personnalisée et nous appellerons cela depuis `textFieldShouldBeginEditing(_:)`, par exemple. Nous vérifions ensuite si nos propriétés `preKeyboard` sont `nil`. Si elles le sont, nous attribuons les valeurs actuelles du `scrollView` (3, 4). Elles pourraient ne pas être `nil` si nous les avons modifiées avant d'appeler cette méthode.

Nous convertissons ensuite le `maxY` du `textField` dans les coordonnées de la fenêtre (5) et ajoutons `10` à celui-ci (6), afin d'avoir un petit espacement entre le champ et le clavier. Si la `bottomLimit` est au-dessus du `minY` du clavier, ne faites rien, car le `textField` est déjà entièrement visible (7). Si la `bottomLimit` est en dessous du `minY` du clavier, calculez la différence entre eux (8) afin de savoir de combien faire défiler le `scrollView` (9, 10) pour que le `textField` soit visible.

Le deuxième assistant réinitialise notre `scrollView` aux valeurs initiales :

```
extension KeyboardListener where Self: UIViewController {
```

```
   func keyboardChanged(with notification: Notification) {      // [...]   }
```

```
   func updateContentOffsetOnTextFieldFocus(_ textField: UITextField, bottomCoveredArea: CGFloat) {      // [...]   }
```

```
   func resetScrollView() {      guard // 1         let originalInsets = contentInsetPreKeyboardDisplay,         let originalOffset = contentOffsetPreKeyboardDisplay      else { return }
```

```
      scrollView.contentInset = originalInsets // 2      scrollView.setContentOffset(originalOffset, animated: true) // 3
```

```
      contentInsetPreKeyboardDisplay = nil // 4      contentOffsetPreKeyboardDisplay = nil // 5   }
```

```
}
```

Si nous n'avons pas d'insertions/décalages originaux, ne faites rien ; par exemple, un clavier matériel est utilisé (1). Si nous en avons, nous réinitialisons le `scrollView` à ses valeurs originales, pré-clavier (2, 3) et mettons à `nil` les propriétés `preKeyboard` (4, 5).

![Image](https://cdn-media-1.freecodecamp.org/images/qxbcull6EPq0v6FFxYdbKqeDvXKNOvrSyY5T)
_Crédits : [Unsplash.com](https://unsplash.com/@mervynckw" rel="noopener" target="_blank" title="">Mervyn</a> sur <a href="https://unsplash.com/photos/RFXxBTHze_M" rel="noopener" target="_blank" title=")_

L'utilisation de cela peut varier en fonction de vos besoins, mais le scénario habituel serait le suivant :

```
final class FormViewController: UIViewController, KeyboardListener {
```

```
   let scrollView = UIScrollView()      /* Ou si vous avez une tableView :            private let tableView = UITableView()      var scrollView: UIScrollView {         return tableView      }   */
```

```
   // [...]
```

```
   override func viewDidLoad() {      super.videDidLoad()
```

```
      let center = NotificationCenter.default
```

```
      center.addObserver(forName: UIResponder.keyboardWillShowNotification, object: nil, queue: nil) { [weak self] notification in        self?.keyboardChanged(with: notification)      }
```

```
      center.addObserver(forName: UIResponder.keyboardWillHideNotification, object: nil, queue: nil) { [weak self] notification in        self?.keyboardChanged(with: notification)      }
```

```
      // Et c'est tout !   }
```

```
   // [...]
```

```
}
```

C'était beaucoup d'informations, mais nous avons maintenant une belle logique "garder le champ de texte au-dessus du clavier". Si nous implémentons tout cela avec la [gestion automatique du bouton Suivant](https://rolandleth.com/handling-the-next-button-automatically), ce sera comme de la magie pour nos utilisateurs.

Consultez [cet article](https://rolandleth.com/observing-and-broadcasting) sur l'automatisation encore plus poussée de cela, en implémentant le système Broadcaster/Listener et en déplaçant les observateurs dans le `Broadcaster` lui-même. Nous n'aurions plus besoin d'ajouter des observateurs dans nos contrôleurs de vue, nous devrions simplement appeler `Broadcaster.shared.addListener(self)`.

Comme d'habitude, j'aimerais avoir vos retours @r[olandleth.](https://twitter.com/rolandleth)

_Publié à l'origine sur [rolandleth.com](https://rolandleth.com/avoiding-the-keyboard-on-uitextfield-focus) le 18 octobre 2018._