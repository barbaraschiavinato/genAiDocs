# 2. DOM Manipulation

## Prompt

Create a script that listens for a button click event and changes the text of a div element. This example will help you see how the tools suggest handling DOM events and provide an example of use and its test.

## Results

### Amazon Q

```html

<!DOCTYPE html>
<html>
<head>
  <title>Button Click Event Example</title>
</head>
<body>
  <button id="myButton">Click me</button>
  <div id="myDiv">This text will change</div>

  <script>
    // Get references to the button and div elements
    const button = document.getElementById('myButton');
    const div = document.getElementById('myDiv');

    // Add a click event listener to the button
    button.addEventListener('click', function() {
      // Change the text of the div element
      div.textContent = 'The text has been changed!';
    });
  </script>
</body>
</html>

```

In this example, we first get references to the button and div elements using their respective IDs. We then add a click event listener to the button using the `addEventListener()` method.

When the button is clicked, the event listener function is executed, which changes the text content of the div element using the `textContent` property.

To test this script, you can open the HTML file in a web browser and click the "Click me" button. You should see the text inside the div element change to "The text has been changed!".

This example demonstrates how to handle a DOM event (in this case, a button click) and update the content of an HTML element accordingly. The Fetch API example I provided earlier showed how to make an asynchronous API request and handle the response, which are also common tasks in web development.




### GitHub Copilot

Here's a simple JavaScript code snippet that listens for a button click event and changes the text of a div element:

```js
document.querySelector('#myButton').addEventListener('click', function() {
    document.querySelector('#myDiv').textContent = 'Button was clicked!';
});
```

In this code, `document.querySelector('#myButton')` selects the button with the id of 'myButton'. The `addEventListener` method is then called on this button to listen for 'click' events. When a 'click' event occurs, the function passed to `addEventListener` is called. This function selects the div with the id of 'myDiv' and changes its text content to 'Button was clicked!'.

To test this code, you can create a simple HTML file with a button and a div:

```html
<!DOCTYPE html>
<html>
<body>

<button id="myButton">Click me</button>

<div id="myDiv">Initial text</div>

<script src="yourScript.js"></script>

</body>
</html>
```

Replace "yourScript.js" with the path to the JavaScript file containing the above script. When you open this HTML file in a web browser and click the button, the text of the div should change.

### Axet Gaia


```js
// Get the button element
const button = document.querySelector('button');

// Get the div element
const div = document.querySelector('div');

// Add a click event listener to the button
button.addEventListener('click', () => {
  // Change the text of the div element
  div.textContent = 'New text';
});
```

**Explanation**


- We use `document.querySelector` to select the button and div elements from the DOM.
- We add a click event listener to the button using `addEventListener`.
- Inside the event listener, we change the text of the div element by setting its `textContent` property to the desired value.

This code follows best practices by:

- Using `querySelector` instead of `getElementById` to select elements, which allows for more flexibility in selecting elements.
- Separating the logic for selecting elements and adding event listeners into separate steps, which improves code readability and maintainability.
- Using arrow function syntax for the event listener, which provides a more concise and modern way of defining functions.
- Using `textContent` instead of `innerHTML` to set the text of the div element, which is more secure and prevents potential security vulnerabilities.

### ChatGpt 4

Here's a simple JavaScript script that demonstrates how to listen for a button click event and then changes the text of a div element based on that event. This example will provide insight into handling DOM events in JavaScript and can serve as a good test for code completion tools like GitHub Copilot or Amazon CodeWhisperer.

**JavaScript Script for DOM Manipulation**

First, let's define the HTML structure for the button and the div:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Button Click Example</title>
</head>
<body>
    <button id="changeTextButton">Change Text</button>
    <div id="displayText">Original Text</div>

    <script src="script.js"></script>
</body>
</html>
```

Next, create the JavaScript file named `script.js` that will contain the code to handle the button click:

```js
document.addEventListener('DOMContentLoaded', function () {
    const button = document.getElementById('changeTextButton');
    const textDiv = document.getElementById('displayText');

    button.addEventListener('click', function() {
        textDiv.textContent = 'Text changed after button click!';
    });
});
```

**Explanation**

- **HTML Setup**: The HTML contains a simple button with an ID `changeTextButton` and a div element with an ID `displayText` where the text will be displayed.
- **JavaScript Behavior**: The script waits until the DOM is fully loaded (`DOMContentLoaded` event). It then selects the button and the div using their IDs. An event listener is added to the button such that when it is clicked, the text content of the div changes to "Text changed after button click!".

**Testing the Script**

To test this script, follow these steps:

1. **Create HTML and JavaScript Files**: Save the HTML code in a file named `index.html` and the JavaScript code in a file named `script.js` in the same directory.
2. **Open the HTML File in a Browser**: Open the `index.html` file in any modern web browser. You should see a button labeled "Change Text" and a div displaying "Original Text".
3. **Interact with the Button**: Click on the button. The text inside the div should change to "Text changed after button click!" indicating that the script is working correctly.

This test verifies that the event listener is properly set up and that it correctly modifies the DOM in response to user interactions. It's a fundamental example of using JavaScript for interactive web pages.

### Meta.ai

Here is a simple script that listens for a button click event and changes the text of a div element:
HTML
// HTML
<button id="myButton">Click me!</button>
<div id="myDiv">Original text</div>

```js
const button = document.getElementById('myButton');
const div = document.getElementById('myDiv');

button.addEventListener('click', () => {
  div.innerText = 'New text!';
});
```
This script uses the `addEventListener` method to listen for a click event on the button element. When the button is clicked, the event listener function is called, which changes the text content of the div element using the `innerText` property.

You can test this script by creating an HTML file with the above code and opening it in a browser. Clicking the button should change the text of the div element.

Note: This script uses the `addEventListener` method to handle the DOM event, which is a widely supported and best practice approach. The `getElementById` method is used to select the elements, which is a common way to interact with the DOM.

### Gemini

**HTML:**

```html
<button id="change-text-button">Change Text</button>
<div id="text-to-change">This is the initial text.</div>
```

**JavaScript:**

```javascript
const button = document.getElementById("change-text-button");
const textDiv = document.getElementById("text-to-change");

button.addEventListener("click", function() {
  textDiv.textContent = "The text has been changed!";
});
```

**Explanation:**

1. **HTML:**
    * We define a button with the ID "change-text-button" to trigger the text change.
    * We also define a div element with the ID "text-to-change" that holds the initial text.
2. **JavaScript:**
    * We use `document.getElementById` to get references to both the button and the div element.
    * We use `button.addEventListener` to attach a click event listener to the button.
    * Inside the event listener function:
        * We access the div element's text content using `textDiv.textContent`.
        * We update the text content with the new message "The text has been changed!".

**Testing the Script:**

1. Save the HTML and JavaScript code together in a file (e.g., index.html).
2. Open the file in a web browser.
3. Click the button. The text in the div element should change to the new message.

**Additional Notes:**

* This script uses a separate JavaScript file for better organization. You can include the script in the HTML using a `<script>` tag.
* You can further customize the new text displayed based on your needs.

This example demonstrates how the tools suggest handling DOM events by using `addEventListener` for attaching event listeners and accessing DOM elements using `document.getElementById`.


## Analysis

### Amazon Q
   - **Pros**: Provides a clear and complete HTML structure with embedded JavaScript that demonstrates basic DOM manipulation. Comments enhance readability and understanding.
   - **Cons**: Lacks any advanced JavaScript practices or error handling.
   - **Code Example**:
     ```html
     <!DOCTYPE html>
     <html>
     <head>
       <title>Button Click Event Example</title>
     </head>
     <body>
       <button id="myButton">Click me</button>
       <div id="myDiv">This text will change</div>

       <script>
         const button = document.getElementById('myButton');
         const div = document.getElementById('myDiv');
         button.addEventListener('click', function() {
           div.textContent = 'The text has been changed!';
         });
       </script>
     </body>
     </html>
     ```

### GitHub Copilot
   - **Pros**: Streamlines the process by using `querySelector`, which allows for more flexible CSS-like element selection.
   - **Cons**: Does not provide the full HTML context within the example, making it less standalone compared to others.
   - **Code Example**:
     ```js
     document.querySelector('#myButton').addEventListener('click', function() {
         document.querySelector('#myDiv').textContent = 'Button was clicked!';
     });
     ```

### Axet Gaia
   - **Pros**: Employs modern JavaScript syntax (arrow functions) and uses `querySelector` for element selection, which is a best practice for flexibility and readability.
   - **Cons**: The example assumes single instances of button and div, which might be restrictive or error-prone in a document with multiple buttons or divs.
   - **Code Example**:
     ```js
     const button = document.querySelector('button');
     const div = document.querySelector('div');
     button.addEventListener('click', () => {
       div.textContent = 'New text';
     });
     ```

### ChatGPT 4
   - **Pros**: Provides a comprehensive approach with an HTML structure and a JavaScript script that ensures the DOM is fully loaded before adding event listeners, using the `DOMContentLoaded` event.
   - **Cons**: More verbose than necessary for simple tasks, which could be simplified for smaller projects.
   - **Code Example**:
     ```html
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>Button Click Example</title>
     </head>
     <body>
         <button id="changeTextButton">Change Text</button>
         <div id="displayText">Original Text</div>

         <script src="script.js"></script>
     </body>
     </html>

     // script.js
     document.addEventListener('DOMContentLoaded', function () {
         const button = document.getElementById('changeTextButton');
         const textDiv = document.getElementById('displayText');
         button.addEventListener('click', function() {
             textDiv.textContent = 'Text changed after button click!';
         });
     });
     ```

### Meta.ai
   - **Pros**: Straightforward and functional approach using direct ID selectors and a concise event listener setup.
   - **Cons**: Similar to other entries but lacks additional safeguards such as checking if elements exist before adding event listeners.
   - **Code Example**:
     ```js
     const button = document.getElementById('myButton');
     const div = document.getElementById('myDiv');
     button.addEventListener('click', () => {
       div.innerText = 'New text!';
     });
     ```

### Gemini
   - **Pros**: Clear setup using `document.getElementById` and an event listener that changes the text content. Provides all necessary HTML and JavaScript in a cohesive snippet.
   - **Cons**: Relatively basic and does not introduce any advanced JavaScript techniques or error handling.
   - **Code Example**:
     ```html
     <button id="change-text-button">Change Text</button>
     <div id="text-to-change">This is the initial text.</div>

     <script>
     const button = document.getElementById("change-text-button");
     const textDiv = document.getElementById("text-to-change");

     button.addEventListener("click", function() {
       textDiv.textContent = "The text has been changed!";
     });
     </script>
     ```

## Conclusion

**Best Code**: **ChatGPT 4** stands out for its robustness, ensuring that the DOM is fully loaded before manipulation, which is critical for scripts included at the head of the document or in larger projects. It provides a comprehensive and well-structured example that is ready to be used in a production environment.

**Worst Code**: **Axet Gaia**, while employing modern JavaScript syntax, potentially creates issues in more complex DOM environments due to its general selectors. It would be more effective with specific selectors to avoid targeting unintended elements.

