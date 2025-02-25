# 3. Array Manipulation

## Prompt

This code should filter an array of numbers, returning only those that are even. This simple task checks how the tools manage array operations and provide an example of use and its test.

## Results

### Amazon Q

```js

function getEvenNumbers(numbers) {
  return numbers.filter(num => num % 2 === 0);
}

```
The `filter()` method takes a callback function as an argument, which is called for each element in the array. The callback function should return `true` if the element should be included in the new array, and `false` otherwise. 

In this case, the callback function checks if the current number `num` is even by using the modulo operator `%`
. If the remainder of `num` divided by 2 is 0, then the number is even, and the callback function returns `true`.
Here's an example of how to use the `getEvenNumbers()` function:

```js

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const evenNumbers = getEvenNumbers(numbers);
console.log(evenNumbers); // Output: [2, 4, 6, 8, 10]

```

To test this function, you can create a test suite using a testing framework like Jest or Mocha. Here's an example using Jest:

```js

test('getEvenNumbers should return only even numbers', () => {
  const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  const evenNumbers = getEvenNumbers(numbers);
  expect(evenNumbers).toEqual([2, 4, 6, 8, 10]);
});

```

This test checks that the `getEvenNumbers()` function correctly filters an array of numbers and returns only the even numbers.


### GitHub Copilot

Based on your description, here's a simple JavaScript function that filters an array to return only even numbers, along with a basic unit test using Jest.

```js
// Function to filter even numbers
function filterEvenNumbers(numbers) {
    return numbers.filter(number => number % 2 === 0);
}

// Jest unit test
test('filterEvenNumbers function', () => {
    expect(filterEvenNumbers([1, 2, 3, 4, 5])).toEqual([2, 4]);
});
```

This function uses the `filter` method of the Array prototype, which iterates over each element in the array and includes it in the returned array if the provided callback function returns `true`. In this case, the callback checks if the number is even by using the modulus operator (`%`). The unit test checks if the function correctly filters out odd numbers.

### Axet Gaia


```js
// Define an array of numbers
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Use the filter method to create a new array with only the even numbers
const evenNumbers = numbers.filter(number => number % 2 === 0);

// Print the result
console.log(evenNumbers);
```

**Explanation**

- We start by defining an array of numbers using the `const` keyword.
- Then, we use the `filter` method on the array to create a new array that only contains the even numbers. The `filter` method takes a callback function as an argument, which is executed for each element in the array. In this case, the callback function checks if the number is even by using the modulo operator (`%`) to check if the remainder of dividing the number by 2 is 0.
- Finally, we print the result using `console.log`.

This solution follows best practices by using modern JavaScript features like arrow functions and the `filter` method, which provide a concise and readable way to solve the problem.

### ChatGpt 4

Here's a simple JavaScript function that filters an array of numbers and returns only the even numbers. This example will help you see how code completion tools like GitHub Copilot and Amazon CodeWhisperer handle array operations.

**JavaScript Function to Filter Even Numbers**

```js
function filterEvenNumbers(numbers) {
    return numbers.filter(number => number % 2 === 0);
}

// Example usage
const arrayOfNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const evenNumbers = filterEvenNumbers(arrayOfNumbers);
console.log(evenNumbers);  // Output: [2, 4, 6, 8, 10]
```

**Explanation**

- **Function Definition**: `filterEvenNumbers` takes an array of numbers as input.
- **Filter Method**: It uses the `filter` method of the array, which iterates over each element in the array.
- **Callback Function**: The callback function for the `filter` method checks if a number is even (`number % 2 === 0`). If this condition is true, the number is included in the returned array.
- **Example Usage**: The function is demonstrated with an array of integers from 1 to 10.

**Testing the Function**

To test this function, you can run it in any JavaScript environment that supports ECMAScript 2015 (ES6) and later, such as modern web browsers or Node.js. Here's how you can quickly test it in a web browser:

1. **Open Your Browser**: Open your favorite browser that supports modern JavaScript features.
2. **Open Developer Tools**: Right-click on the page and select "Inspect" or use the shortcut `Ctrl+Shift+I` (or `Cmd+Option+I` on macOS) to open developer tools.
3. **Go to the Console Tab**: Click on the "Console" tab in the developer tools window.
4. **Paste and Run the Function**: Copy the `filterEvenNumbers` function code provided above and paste it into the console, then press Enter.
5. **View the Output**: After running the function, you should see `[2, 4, 6, 8, 10]` logged to the console.

This simple test will confirm that the function is correctly filtering the array to return only even numbers, demonstrating the function's ability to perform array operations effectively.

### Meta.ai

Here is a simple script that filters an array of numbers, returning only those that are even:

```js
// Function to filter even numbers
function filterEvenNumbers(arr) {
  return arr.filter(num => num % 2 === 0);
}

// Example usage
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const evenNumbers = filterEvenNumbers(numbers);

// Test
console.log(evenNumbers); // Output: [2, 4, 6, 8, 10]

```
This script defines a function `filterEvenNumbers` that takes an array of numbers as input and returns a new array with only the even numbers. The `filter` method is used with a callback function that checks if a number is even by using the modulo operator `(num % 2 === 0)`.

The example usage shows how to call the function with an array of numbers, and the test logs the resulting array of even numbers to the console.

This code demonstrates how to perform array filtering, which is a common task in programming, and shows how the tools handle array operations.

### Gemini


**JavaScript:**

```javascript
function filterEvenNumbers(numbers) {
  return numbers.filter(number => number % 2 === 0);
}
```

**Explanation:**

1. **`function filterEvenNumbers(numbers)`:** This defines a function named `filterEvenNumbers` that takes an array of numbers as input.
2. **`return numbers.filter(number => number % 2 === 0);`:**
   * This line uses the built-in `filter` method on the `numbers` array.
   * The `filter` method takes a callback function as an argument.
   * The callback function receives each element (`number`) from the array.
   * The condition `number % 2 === 0` checks if the number is even using the modulo operator (`%`).
   * If the condition is true, the element is included in the filtered array. Otherwise, it's excluded.
   * Finally, the `filter` method returns a new array containing only the even numbers.

**Example of Use:**

```javascript
const numbers = [1, 2, 3, 4, 5, 6];
const evenNumbers = filterEvenNumbers(numbers);
console.log(evenNumbers); // Output: [2, 4, 6]
```

**Test:**

```javascript
function testFilterEvenNumbers() {
  const numbers = [1, 2, 3, 4, 5, 6];
  const expectedEvenNumbers = [2, 4, 6];
  const actualEvenNumbers = filterEvenNumbers(numbers);

  // Test if the returned array is equal to the expected even numbers
  const testPassed = JSON.stringify(actualEvenNumbers) === JSON.stringify(expectedEvenNumbers);
  console.assert(testPassed, "filterEvenNumbers failed!");
}

testFilterEvenNumbers();
```

**Explanation of Test:**

1. **`testFilterEvenNumbers` function:** This function tests the `filterEvenNumbers` function.
2. It defines two variables:
   * `numbers`: An array containing a mix of even and odd numbers.
   * `expectedEvenNumbers`: The expected output – an array containing only the even numbers from `numbers`.
3. It calls `filterEvenNumbers` with the `numbers` array and stores the result in `actualEvenNumbers`.
4. It uses `JSON.stringify` to convert both arrays to JSON strings for comparison.
5. It uses `console.assert` to check if the stringified versions of `actualEvenNumbers` and `expectedEvenNumbers` are equal. If not, it logs an error message.

This example demonstrates how the tools manage array operations using the `filter` method and showcases a testing approach using `console.assert` for basic functionality verification.

## Analysis

### Amazon Q
   - **Pros**: Provides a clean and concise function that leverages the `filter()` method effectively, including thorough documentation and a practical test example using Jest.
   - **Cons**: No significant cons; it's a straightforward implementation.
   - **Code Example**:
     ```js
     function getEvenNumbers(numbers) {
       return numbers.filter(num => num % 2 === 0);
     }
     ```

### GitHub Copilot
   - **Pros**: Simple implementation with direct usage of `filter()`. Includes a Jest test which is good for understanding unit testing basics.
   - **Cons**: Lacks additional explanation or advanced usage examples.
   - **Code Example**:
     ```js
     function filterEvenNumbers(numbers) {
         return numbers.filter(number => number % 2 === 0);
     }
     ```

### Axet Gaia
   - **Pros**: Offers a straightforward use of the `filter()` method, immediately applying it within a script to demonstrate practical usage.
   - **Cons**: Does not encapsulate the functionality in a reusable function, limiting its application in larger or more complex applications.
   - **Code Example**:
     ```js
     const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
     const evenNumbers = numbers.filter(number => number % 2 === 0);
     console.log(evenNumbers);
     ```

### ChatGPT 4
   - **Pros**: Clearly defines the function and provides detailed steps on how to test it in various JavaScript environments, which is helpful for beginners.
   - **Cons**: Somewhat verbose but beneficial for educational purposes, especially for users unfamiliar with testing JavaScript in a browser.
   - **Code Example**:
     ```js
     function filterEvenNumbers(numbers) {
         return numbers.filter(number => number % 2 === 0);
     }
     ```

### Meta.ai
   - **Pros**: Provides a straightforward function that uses the `filter()` method efficiently, similar to other entries, with a clear example of usage.
   - **Cons**: Does not offer any unique or innovative approach beyond what is standard for this type of function.
   - **Code Example**:
     ```js
     function filterEvenNumbers(arr) {
       return arr.filter(num => num % 2 === 0);
     }
     ```

### Gemini
   - **Pros**: Implements the `filter()` method in a clean function format, providing a clear example of use and a detailed testing approach using `console.assert`, which is beneficial for debugging and learning.
   - **Cons**: The test example, while informative, may be unnecessarily complex for this simple function.
   - **Code Example**:
     ```javascript
     function filterEvenNumbers(numbers) {
       return numbers.filter(number => number % 2 === 0);
     }
     ```

## Conclusion

**Best Code**: **Amazon Q** stands out for its comprehensive approach, providing clear code implementation, usage example, and a well-documented test scenario. This makes it highly practical and educational, especially for those learning how to integrate such functions into applications and test them.

**Worst Code**: **Axet Gaia**, despite correct implementation, lacks functional encapsulation which is critical for reusability and integration into larger projects. It directly uses the `filter()` method in a script, which is less flexible for broader applications.

