---
title: How to validate default and custom reactive forms in Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-01T17:50:28.000Z'
originalURL: https://freecodecamp.org/news/validating-reactive-forms-with-default-and-custom-form-field-validators-in-angular-5586dc51c4ae
coverImage: https://cdn-media-1.freecodecamp.org/images/1*I4kNKF1MI99L2iMqq0it-g.jpeg
tags:
- name: Angular
  slug: angular
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Luuk Gruijs

  When presenting forms to your users, it’s considered very user-friendly to give
  them immediate feedback on whether what they type is actually correct. Besides that,
  it could also limit the number of requests to the server. You would be...'
---

By Luuk Gruijs

When presenting forms to your users, it’s considered very user-friendly to give them immediate feedback on whether what they type is actually correct. Besides that, it could also limit the number of requests to the server. You would be able to catch 99% of the errors before submitting your form to the server.

![Image](https://cdn-media-1.freecodecamp.org/images/qLQsIH1hq10Ki5q5JGFTidYla1fKkVsR67EZ)
_Photo by [Unsplash](https://unsplash.com/photos/twukN12EN7c?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Simon Matzinger</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

When using reactive forms, Angular offers only a hand full of very generic validators. The default form field validators are:

* **min:** the value should be higher than a certain number.
* **max:** the value should be lower than a certain number.
* **required:** the value cannot be empty
* **requiredTrue:** the value must be true
* **email:** the value should be an email
* **minLength:** The value should contain a minimum amount of characters
* **maxLength:** The value should contain a maximum amount of characters

Chances are the above validators will not be able to match the requirements of your server. Therefore you cannot give the user the feedback they would like to get and help them submit a correct form. For this, you are going to need custom form field validators.

### Creating a custom form field validator

A form field validator is a function that takes your form control — the input field — and validates the value of that form control against a certain condition. This function either returns nothing when everything is ok or an object stating what went wrong.

A very common use case of a custom validator is to check whether the form matches the sanitization rules of the server. This means the validator checks if the characters your user puts into your form are allowed. Let’s create this form validator now.

### Building the form

To use this validator we need to create a form and define it there. For this purpose, we’re going to create a simple user signup form. We use the reactive way to create the form. It can be done like this:

The template can then look like this:

We now have a working reactive form. We, however, did not apply any form validation. To add form validation, we simply pass our validators into the form creation function like this:

We used the required and email validators from Angular. We also imported our custom created validateCharacters validator. The last thing we still have to do is present potential errors to our users.

### Presenting errors to the user

There are two moments when we want to present errors to our users: when the focus moves from one field to the other and right before the final form submission.

Let’s create a form service for this. This service could potentially look like this:

The `validateForm` method accepts the form to validate, a form errors object and a boolean on whether to check dirty fields or not. The function then loops over all the form controls and checks if there are errors on that control. If there are any, we find the correct error message that came from the `validationMessages` method and pass back the form errors object.

To use this error service in our components, we have to do the following:

Now the final step is to show the error messages in our template. We can do that like this:

If there any errors on one particular field, we show the message that’s in the `formErrors` object. Below is a full demo. Play around with the fields. Try to fill in characters like `!#$^` in the name field and see if our custom form validator works. If no errors appear, hit the signup button and see the success message.

### Conclusion

I hope this article helps you validate your forms and give your users a better experience when filling in the forms.

#### Looking for a job in Amsterdam?

I work for **Sytac** as a Senior front-end developer. We are looking for mid/senior developers that specialize in Angular, React, Java or Scala. Sytac is a very ambitious consultancy company in the Netherlands.

If you think you have what it takes to work with the best, send me an email on [luuk.gruijs@sytac.io](mailto:luuk.gruijs@sytac.io) and I’m happy to tell you more.

