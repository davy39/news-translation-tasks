---
title: How to Validate Forms in React and React Native Using Yup and Formik
subtitle: ''
author: Grant Riordan
co_authors: []
series: null
date: '2024-06-24T19:51:14.000Z'
originalURL: https://freecodecamp.org/news/react-how-to-validate-user-input
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/1080_Template.png
tags:
- name: Form validations
  slug: form-validations
- name: forms
  slug: forms
- name: React
  slug: react
seo_title: null
seo_desc: 'Validation is a key part of development, regardless of what programming
  language you’re writing. Developers should always be validating user input, API
  parameters, and retrieved values.

  One of the most common elements where you’ll need to apply user ...'
---

Validation is a key part of development, regardless of what programming language you’re writing. Developers should always be validating user input, API parameters, and retrieved values.

One of the most common elements where you’ll need to apply user input validation is via a form. This could be a user sign up form, a contact us form, or a simple questionnaire.

## Outcomes of the Tutorial

By the end of this article , you will be able to:

* Understand common issues with form validation.
* How to utilise the Yup schema validation library alongside the Formik form library.
* How to build a form in React with full validation (same principles apply for React Native, with different component syntax).

## Contents

* [What is Validation](#heading-what-is-validation)?
* [The Object to Be Validated](#heading-the-object-to-be-validated)
* [Introducing Yup and Formik](#heading-introducing-yup-and-formik)
* [How to Add Validation to a Form](#heading-how-to-add-validation-to-a-form)
* [Conclusion](#heading-conclusion)

## What is Validation?

Validation is defined as:

> _the action of checking or proving the validity or accuracy of something._

But what does that mean in computer speak? This could be a multitude of things, but the premise still stands. You could be validating a variable value or an object against a pre-determined set of rules or regulations.

Examples of validation rules could be:

* Password must be at least 8 characters and contain a special character.
* Username must be unique.
* Date of birth must be received as a string, in a particular format, for example ISO8601

Let’s use the example of a user registration form on a website. 

## The Object to Be Validated

The form will comprise of several inputs to form a `UserRegistration` object. Like so‌:

```ts
interface UserRegistration {
  firstName: string;
  surname: string;
  email: string;
  dob: string;
}

```

Above is an interface (contract) for a `UserRegistration` object. It simply defines some key user information which needs to be collected, with all values being a `string` value.

While languages like TypeScript are useful for ensuring that we pass the correct types to functions throughout our application, they do not inherently validate the actual content or values within those types. TypeScript guarantees that a variable is of a specific type, such as a string or a number, but it does not verify if the content of that string or number meets specific criteria or constraints.

### What If We Didn't Validate the Values?

Ok, before we move onto how to validate, let's look at what could happen if we don't validate.

Without validation, a user could input the following values:

**Firstname**: 1231301‌  
‌**Surname**: Hello##test_101‌  
‌**Email**: user_123@@email.to@.com‌  
‌**DoB**: 10+12+1909

These values may **seem** perfectly acceptable, and your front end might allow them to be submitted without any issues. And the API will likely accept these values initially. 

But when the API attempts to parse these values (converting) during the request processing, it will encounter errors and fail to process the request correctly.

There are several negative consequences to this approach:

1. **Increased Server Load**: The front end is making multiple invalid requests to the server, which unnecessarily strains the server. This extra load could have been avoided.
2. **Potentially Higher Costs**: The cost of handling these invalid requests can increase significantly, depending on your hosting plan and server configuration. Each invalid request consumes server resources that could be used more efficiently.
3. **Poor User Experience (UX)**: Users will likely become frustrated if they repeatedly enter details, submit the form, and then receive error messages indicating that their inputs are invalid. This can lead to a negative perception of the application.

To mitigate these issues and reduce the number of invalid requests, we can implement 'client-side validation' to ensure that the data meets the required criteria before sending the API request.

## Introducing Yup and Formik

Yup and Formik are both libraries which you can add to any React or React Native application via npm or yarn.

Yup is a schema building library that allows you to build schemas for validation at runtime. It has a plethora of extension functions which can set rulesets, transform values, and return validation messages right out the box.

Let's take a look at an example of a Yup schema for our user form:‌

```ts
import * as Yup from 'yup';

// If using Typescript, you can utilise a wrapper function to enforce strict typing

const createYupSchema = <T extends object>(schema: Yup.ObjectSchema<T>): Yup.ObjectSchema<T> => schema;

export const userFormSchema = createYupSchema<UserInput>(
  Yup.object().shape({
    firstname: Yup.string().required('First name is required'),
    surname: Yup.string().required('Surname is required'),
    email: Yup.string().email('Invalid email format').required('Email is required'),
    dob: Yup.string().required('Date of Birth is required'),
  })
);

// JS Version
export const validationSchema = Yup.object({
  firstname: Yup.string().required('First name is required'),

  surname: Yup.string().required('Surname is required'),
  email: Yup.string().email('Invalid email format').required('Email is required'),
  dob: Yup.date().required('Date of Birth is required')
});
```

We're creating a Yup object (schema) which contains all of our Keys for our UserInput interface.

### Schema Parts:

* key: the key which will be used later for the name of our element (as we're using TypeScript, this needs to match the object key name).
* ruleset: for all keys, apply a ruleset. A ruleset must start with a typing declaration, that is `Yup.string()` or `Yup.number()` and so on. You can then chain your other validation functions. 

Using TypeScript ensures that we match the schema type to our interface types.

For example, if we try and do this:

```ts
firstname: Yup.date().required();
```

it will throw a TypeScript error complaining that `firstname` cannot be validated as if it was a date, as the type of firstname is a `string`.

### How to Add Validation to a Form

This is where our Formik library comes in and makes things much easier than validating a form and implementing error handling manually.

Formik is a library which encapsulates a `<Form/>` component. It allows us to create richer forms in React and React Native, giving us access to features like form state, error handling, validation, and processing of form submissions much more efficiently.

You can access a pre-built version of a UserForm utilising Yup, Formik, and React (Vite) at my GitHub [here](https://github.com/grant-dot-dev/fcc-yup-schema-validation). Simply clone the GitHub repository and follow the README.md instructions. ‌

```tsx
<Formik
        initialValues={initialValues}
        validationSchema={userFormSchema}
        onSubmit={onSubmit}
      >
        {({ isValid, dirty, isSubmitting }) => (
          <Form>
            <div className="form-control">
              <label htmlFor="firstName">First Name</label>
              <Field type="text" id="firstName" name="firstName" />
              <ErrorMessage name="firstName" component="div" className="error" />
            </div>

            <div className="form-control">
              <label htmlFor="surname">Surname</label>
              <Field type="text" id="surname" name="surname" />
              <ErrorMessage name="surname" component="div" className="error" />
            </div>

            <div className="form-control">
              <label htmlFor="email">Email</label>
              <Field type="email" id="email" name="email" />
              <ErrorMessage name="email" component="div" className="error" />
            </div>

            <div className="form-control">
              <label htmlFor="dob">Date of Birth</label>
              <Field type="date" id="dob" name="dob" />
              <ErrorMessage name="dob" component="div" className="error" />
            </div>

            <button type="submit" disabled={isSubmitting || !isValid}>Submit</button>
          </Form>
        )}
      </Formik>
```

In this code, we've utilsed the `<Formik/>` library component, which wraps around our standard `<Form/>`  element. We pass the following properties to the component:

* `**initialValues**` – these are the required initial values of your form (that is when the form renders what values your inputs will have).‌ 
* **`validationSchema` –** this is probably the most important for this tutorial. Bear in mind this is an optional property, as it's not needed to utilise the `<Formik/>` component, but for any validation it is. ‌  
‌‌  
‌We're going to import our `userFormSchema` we created in the previous step. This is going to tell the form, when validating inputs within this form utilise these schemas. ‌
* **`onSubmit`** – a straightforward function to run on clicking your button / submitting the form. The values of the form will automatically be passed to this function.‌

You can wrap the form within a "render prop" function also to utilise some of the exposed props from Formik within your form. You can learn about render props more [here](https://legacy.reactjs.org/docs/render-props.html).

```tsx
{({ isValid, isSubmitting }) => (
```

**Note:** This is not required if you don't want to utilise any of the underlying Formik properties within the form itself. You can simply remove and place your opening `<Form>` tag in its place. ‌  
‌‌  
‌But using this render prop allows you to access properties exposed from the Formik component within your `<Form/>` element. You can see that we are utilising the`isValid` and `isSubmitting` properties to control the state of our submit button.

Continuing on with analyzing the code:

* `**isValid**` – a boolean value which Formik controls based on our schema validation result.
* `**isSubmitting**` – A boolean flag indicating if a form is mid-submission. This flag is very useful when wanting to disable a button, to prevent multiple clicks meaning multiple submissions of the form.

We can use these values to control the enablement of the submit button like so:

```tsx
<button type="submit" disabled={isSubmitting || !isValid}>Submit</button>
```

### Input Fields

It's important to note that when using Formik and Yup, in order for the validation to work, the names of the input fields need to match the Yup schema keys exactly (case sensitive) – otherwise the validation rules won't be registered.

**Example:‌**

```tsx
<Field type="email" id="email" name="email" />
<ErrorMessage name="email" component="div" className="error" />
```

We've defined this field is to be used for an email input, and given it the matching `name` of "email" to our a userFormSchema definition.

Underneath, we code our Formik `<ErrorMessage/>` component, again passing in the name of '_email'_, matching our schema. Using the name property we are able to link our input, error message, and validation schemas all together. 

If there are any issues with validating the input field, the error message will show any defined error messages – otherwise it will fallback to a default message, e.g "_firstname is a required field_". This can be less user friendly, so I'd recommend always passing a custom message.

You'll also notice, that when we lose focus or when typing (after first validation has run), it will automatically run validation again. You can overwrite this functionality by setting the `validateOnBlur` and the `validateOnChange` flags (true / false).

As an example, it will look like this in its error state.:

![Image: Invalid Formik form showing error state](https://www.freecodecamp.org/news/content/images/2024/06/image-100.png)
_Image: Invalid Formik form showing error state_

‌Once we've entered values for all inputs, and our validation has passed (you can see the submit button is now enabled), we can submit.‌

![Image: Valid Formik form showing valid state](https://www.freecodecamp.org/news/content/images/2024/06/image-95.png)
_<div id="ember289" class="miw-100 tc bn form-text bg-transparent pr8 pl8 ember-view" data-kg-has-link-toolbar="true" data-koenig-dnd-disabled="true" style="box-sizing: border-box; padding-right: 3.2rem; padding-left: 3.2rem; border-style: none; border-width: 0px; transition: border-color 0.15s linear 0s; appearance: none; outline: none; min-width: 100%; background-color: transparent !important; text-align: center;"><div class="koenig-basic-html-input__editor-wrappper" style="box-sizing: border-box; cursor: text;"><div class="koenig-basic-html-input__editor __mobiledoc-editor" data-gramm="false" data-kg="editor" data-kg-allow-clickthrough="" data-placeholder="Type caption for image (optional)" spellcheck="true" contenteditable="true" style="box-sizing: border-box; position: relative; resize: none; min-height: 1em;"><p style="box-sizing: border-box; margin: 0px; position: relative; min-width: 100%; max-width: 100%; font-family: inherit; font-weight: inherit; line-height: inherit; font-size: inherit; letter-spacing: inherit;">Image: Valid User form with enabled submit button</p></div></div></div>_

### Further Validation and Formik Features‌ 

You've now seen how easy Yup and Formik can make creating a form. It has full validation and even error handling, meaning you can have a fully functioning user friendly form built in just a few minutes.

But what if you want to add more complex validation to a much larger / complicated form? Well, let's look at an example:

Let's say we want to validate that the date of birth provided ensures that the user is over the age of 18. We will also add a password field, which will have rules of:

* minimum of 6 letters
* contain a number
* contain a special character

#### DoB Extra Requirements

We can do this by chaining the `test()` function onto the `string()` function of the dob object within our schema.

The `test()` function allows us to test against custom logic. Update the `dob` parameter within the userFormSchema to the following:‌

```ts
dob: Yup.string()
      .required('Date of Birth is required')
      .test('is-older-than-18', 'You must be at least 18 years old', (value) => {
        if (!value) return false;

        // try to parse the value to date
        const parsedDate = parse(value, 'yyyy-MM-dd', new Date());
        if (!isValid(parsedDate)) return false;

        const today = new Date();
        const eighteenYearsAgo = subYears(today, 18);

        // check if date provided is before or the same as 18 years ago.
        return parsedDate <= eighteenYearsAgo;
      })
```

We now get the following error when trying to submit a date that is less than 18 years ago. ‌

![Image showing Invalid date input field due to failed date validation](https://www.freecodecamp.org/news/content/images/2024/06/image-99.png)
_Image: Invalid input field due to failed date validation_

#### Password Validation

For the password field validation, we can do something like this:‌

```ts
password: Yup.string()
    .required('This field is required')
    .min(6, 'Must be at least 6 characters')
    .matches(/[!@#$%^&*(),.?":{}|<>]/, 'Must contain at least one special character')
    .matches(/\d/, 'Must contain at least one number');
```

Here we use the `matches()` function, passing in a regular expression to assert against. You could combine these cases into one regular expression, but the benefit of keeping them separate is it allows you to pinpoint which validation rule is failing. It also allows for a more granular error message and maintenance should the rules change in the future.

### Other Useful Methods:

* `length()` – asserts the length of the string / number
* `positive()` – asserts the number type is a positive number
* `email()` – asserts that it is a valid email address
* `url()`  – asserts that it is a valid URL 
* `min()` / `max()` – asserts that the number is at least 'x' and less than 'y'
* `ensure()` – transforms `undefined` and `null` values to an empty string along with setting the `default` to an empty string.

## Conclusion

As you can see, the possibilities with Yup are vast. Then combine this with the Formik library, and you can have rich, efficient, and easy to use forms. 

This ease of use makes it so much quicker to get a form up and running on your web or mobile application, allowing you to focus on user experience, design, and business logic. 

As always feel free to reach and discuss this article with me on [Twitter](https://x.com/grantdotdev), and don't forget to drop me a follow to hear about future articles and dev tips.   


  

