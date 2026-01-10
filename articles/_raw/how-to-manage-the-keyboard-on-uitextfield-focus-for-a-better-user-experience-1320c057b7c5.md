---
title: How to manage the keyboard on UITextField focus for a better user experience
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
seo_title: null
seo_desc: 'By Roland Leth

  A couple of posts ago I was writing about handling the Next button automatically.
  In this post I’d like to write about avoiding the keyboard automatically, in a manner
  that provides both a good user experience and a good developer expe...'
---

By Roland Leth

A couple of [posts](https://rolandleth.com/handling-the-next-button-automatically) ago I was writing about handling the Next button automatically. In this post I’d like to write about avoiding the keyboard automatically, in a manner that provides both a good user experience and a good developer experience.

Most apps have _some_ sort of form that needs to be filled, even if just a login/register, if not several forms. As a user, having the keyboard cover the text field I’m about to fill makes me sad — it’s a poor user experience. As developers, we’d like to solve this as easily as possible and have the solution be as reusable as possible.

What does a good user experience mean?

* The focused `UITextField` is brought above the keyboard on focus.
* The focused `UITextField` is “sent back” on dismiss.

What does a good developer experience mean? Everything should happen as automatically as possible, so we’ll go with a protocol once again. What does this protocol need to encapsulate?

* Observing the keyboard will show/hide notifications.
* On keyboard appearance, it needs to modify the `scrollView.contentInset` and `scrollView.contentOffset` in a way that brings the `UITextField` right above the keyboard.
* On keyboard disappearance, it needs to reset the inset and offset to previous values.

With this in mind, let’s build our protocol:

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

We need to constrain this protocol to be conformed to only by classes (1) because we’ll need to modify the two `preKeyboard` properties (3, 4). We’ll use them to know how to revert the `scrollView`’s inset and offset on keyboard dismissal. We’ll most likely implement this in a `UIViewController` anyway.

The protocol also needs to have a `scrollView` (2), otherwise this isn’t really … feasible (I guess it could be _doable_). Lastly, we need the method that will handle everything (5), but it just acts as a proxy for two helpers that we’ll implement in just a bit:

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

If the notification is not for `willShow`, or we can not parse the notification’s `userInfo`, bail out and reset the `scrollView`. If it is, increase the bottom inset by the keyboard’s height (3). As for (2), we find the current first responder with [a little trick](https://stackoverflow.com/a/40352519/793916) to call `updateContentOffsetOnTextFieldFocus(_:bottomCoveredArea:)` with, but we could also call it from our delegate’s `textFieldShouldBeginEditing(_:)`.

The first helper will update our two `preKeyboard` properties:

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

We will now update the protocol extension with a `Self: UIViewController` constraint (1), because we’ll need access to the window. This shouldn’t be an inconvenience, because this protocol will be most likely used by `UIViewController`s. However, another approach would be to replace all the `view.window` occurrences with `UIApplication.shared.keyWindow` or a variation of `UIApplication.shared.windows[yourIndex]`, in case you have a complex hierarchy.

We then calculate the `minY` for the keyboard (2) — we use a parameter for those cases where we have a custom `inputView` and we’ll call this from `textFieldShouldBeginEditing(_:)`, for example. We then check if our `preKeyboard` properties are `nil`. If they are, we assign the current values from the `scrollView` (3, 4). They might not be `nil` if we changed them prior to calling this method.

We then convert the `textField`’s `maxY` in the window’s coordinates (5) and add `10` to it (6), so we have a small padding between the field and the keyboard. If the `bottomLimit` is above the keyboard’s `minY`, do nothing, because the `textField` is already fully visible (7). If the `bottomLimit` is below the keyboard’s `minY`, calculate the difference between them (8) so we know how much to scroll the `scrollView` (9, 10) so that the `textField` will be visible.

The second helper resets our `scrollView` back to the initial values:

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

If we have no original insets/offset, do nothing; for example, a hardware keyboard is used (1). If we do, we reset the `scrollView` to its original, pre-keyboard values (2, 3) and `nil`-out the `preKeyboard` properties (4, 5).

![Image](https://cdn-media-1.freecodecamp.org/images/qxbcull6EPq0v6FFxYdbKqeDvXKNOvrSyY5T)
_Credits: [Unsplash.com](https://unsplash.com/@mervynckw" rel="noopener" target="_blank" title="">Mervyn</a> on <a href="https://unsplash.com/photos/RFXxBTHze_M" rel="noopener" target="_blank" title=")_

Using this may vary depending on your needs, but the usual scenario would go like this:

```
final class FormViewController: UIViewController, KeyboardListener {
```

```
   let scrollView = UIScrollView()      /* Or if you have a tableView:            private let tableView = UITableView()      var scrollView: UIScrollView {         return tableView      }   */
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
      // And that's it!   }
```

```
   // [...]
```

```
}
```

This was a lot of info, but we now have a nice ”keep the text field above the keyboard” logic. If we implement all of this alongside the [automatic Next button handling](https://rolandleth.com/handling-the-next-button-automatically), it will be like magic for our users.

Check out [this post](https://rolandleth.com/observing-and-broadcasting) about slightly automating this even further, by implementing the Broadcaster/Listener system and moving the observers in the `Broadcaster` itself. We wouldn’t need to add observers in our view controllers anymore, we’d just have to call `Broadcaster.shared.addListener(self)`.

As usual, I’d love to hear your thoughts @r[olandleth.](https://twitter.com/rolandleth)

_Originally published at [rolandleth.com](https://rolandleth.com/avoiding-the-keyboard-on-uitextfield-focus) on October 18, 2018._

