# 14. Unit Test with Jest

## Prompt

Write a Jest test for a JavaScript function named 'multiply' that takes two parameters and returns their product. The test should check if the function correctly multiplies 3 by 5.

## Results

### Amazon Q

```js

// multiply.js
function multiply(a, b) {
  return a * b;
}

module.exports = multiply;

// multiply.test.js
const multiply = require('./multiply');

test('multiplies 3 by 5', () => {
  expect(multiply(3, 5)).toBe(15);
});

```

Here's how the test works:

We define a `multiply` function in the `multiply.js` file that takes two parameters and returns their product.

We export the `multiply` function so that it can be used in other files.

In the `multiply.test.js` file, we import the `multiply` function using `require('./multiply')`.

We use the `test` function provided by Jest to define a test case. The first argument is a string that describes the test, and the second argument is a function that contains the actual test.

Inside the test function, we use the `expect` function provided by Jest to make an assertion about the output of the `multiply` function. In this case, we expect the result of `multiply(3, 5)` to be `15`.

To run the test, you can use the following command in your terminal:

```
npx jest multiply.test.js
```

This will run the test and display the results. If the test passes, you should see output similar to the following:

```
 PASS  ./multiply.test.js
  ✓ multiplies 3 by 5 (2 ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   0 total
Time:        0.178 s
Ran all test suites.

```

### GitHub Copilot


```javascript
// Assuming that the multiply function is defined in the same file
function multiply(a, b) {
  return a * b;
}

// Jest test
describe('multiply', () => {
  test('correctly multiplies 3 by 5', () => {
    expect(multiply(3, 5)).toBe(15);
  });
});
```

If the 'multiply' function is defined in a different module, you would need to import it into your test file:

```javascript
// Assuming that the multiply function is defined in a module named 'mathFunctions'
const { multiply } = require('./mathFunctions');

// Jest test
describe('multiply', () => {
  test('correctly multiplies 3 by 5', () => {
    expect(multiply(3, 5)).toBe(15);
  });
});
```

### Axet Gaia

Sure! Here's the JavaScript code for implementing the 'multiply' function and writing a Jest test for it:

```javascript
// Function to multiply two numbers
function multiply(a, b) {
  return a * b;
}

// Jest test for the multiply function
test('multiply function should correctly multiply 3 by 5', () => {
  // Arrange
  const num1 = 3;
  const num2 = 5;
  
  // Act
  const result = multiply(num1, num2);
  
  // Assert
  expect(result).toBe(15);
});
```

**Explanation**

- The `multiply` function takes two parameters `a` and `b` and returns their product using the `*` operator.
- The Jest test is written using the `test` function provided by Jest. It checks if the `multiply` function correctly multiplies 3 by 5 by comparing the result with the expected value using the `expect` function and the `toBe` matcher.

This code follows best practices for JavaScript by:

- Using descriptive function and variable names (`multiply`, `num1`, `num2`, `result`) to improve code readability.
- Separating the function implementation and the test code into separate sections for better organization.
- Using comments to provide short explanations of the code's purpose and functionality.

### ChatGpt 4

To write a Jest test for a JavaScript function named `multiply` that multiplies two parameters, you'll first need a function implementation and then the corresponding test. Below, I provide both the function definition and the Jest test case.

**Step 1: Function Implementation**

Create a file named `multiply.js` and define the `multiply` function as follows:

```javascript
// multiply.js
function multiply(a, b) {
    return a * b;
}

module.exports = multiply;
```

**Step 2: Writing Jest Test**

Create a test file named `multiply.test.js`. This file will contain the Jest test case to ensure that the `multiply` function works as expected, particularly that it correctly multiplies 3 by 5.

```javascript
// multiply.test.js
const multiply = require('./multiply');

describe('multiply function tests', () => {
    test('multiplies 3 and 5 to get 15', () => {
        expect(multiply(3, 5)).toBe(15);
    });
});
```

**Explanation**

- **Require Statement**: The `multiply` function is imported from the `multiply.js` file.
- **describe block**: Used to group together similar tests. In this case, all tests related to the `multiply` function are grouped.
- **test block**: Defines a single test. The description inside the test function explains what the test is expected to do — in this case, check if `multiply(3, 5)` returns 15.
- **expect and toBe**: `expect` is the Jest method used to test a value. `toBe` is a matcher that tests for exact equality, meaning it checks if `multiply(3, 5)` returns exactly 15.

**Running the Test**

To run this test, you'll need Node.js and Jest installed. If Jest is not installed, you can add it by running:
```bash
npm install --save-dev jest
```

Add the following script to your `package.json` to make running tests easier:
```json
"scripts": {
    "test": "jest"
}
```

Now, you can run the test by executing:
```bash
npm test
```

This setup will execute the Jest test runner, which will find your test in `multiply.test.js` and run it, reporting whether the test passed or failed based on the criteria you've set. This simple test ensures that your multiplication logic in the `multiply` function is correct for the given inputs.

### Meta.ai

Here is a Jest test for the multiply function:
```js
import { multiply } from './multiply';

describe('multiply', () => {
  it('returns the product of two numbers', () => {
    expect(multiply(3, 5)).toBe(15);
  });
});
```
Here's what's happening:

- We import the `multiply` function from the `./multiply` module (assuming it's in the same directory).
- We define a test suite named multiply using the `describe` function from Jest.
- We define a test case named `returns` the `product` of `two numbers` using the it function from Jest.
- We call the `multiply` function with arguments 3 and 5 and expect the result to be 15 using the expect function from Jest.
- We use the toBe matcher to check if the result is equal to 15.

When you run this test with Jest, it will pass if the multiply function correctly returns the product of 3 and 5, which is 15.
Note: Make sure to replace ./multiply with the actual path to your multiply function module.

### Gemini


```javascript
test('multiply function multiplies two numbers correctly', () => {
  const result = multiply(3, 5);
  expect(result).toBe(15);
});

function multiply(a, b) {
  return a * b;
}
```

**Explanation:**

1. **`test` function:** We use the `test` function from Jest to define a test case.
2. **Test Description:** The first argument to `test` is a string describing what the test is verifying.
3. **Test Body:** The second argument is a callback function that contains the actual test logic.
   - We call the `multiply` function with arguments 3 and 5 and store the result in a variable `result`.
   - We use the `expect` function from Jest to make assertions about the result.
   - In this case, we expect the `result` to be equal to 15 using the `toBe` matcher.

4. **`multiply` Function:** This function is defined outside the test but needs to be available for the test to run. It simply multiplies the two arguments and returns the product. 

**Running the Test:**

Save this code in a file (e.g., multiply.test.js). You can run Jest from the terminal using `npm test` or `yarn test` (assuming you have Jest configured in your project). 

If the `multiply` function works as expected, the test should pass. If there's an error or the function doesn't return the correct result, the test will fail and provide information about the failure.


## Analysis

### Amazon Q
   - **Pros**: Clear and simple implementation. Includes both the function definition and the test in a very straightforward format.
   - **Cons**: Minimal context or advanced Jest features used, but sufficient for the task.
   - **Code Example**:
     ```javascript
     // multiply.js
     function multiply(a, b) {
       return a * b;
     }
     module.exports = multiply;

     // multiply.test.js
     const multiply = require('./multiply');
     test('multiplies 3 by 5', () => {
       expect(multiply(3, 5)).toBe(15);
     });
     ```

### GitHub Copilot
   - **Pros**: Similar to Amazon Q but introduces `describe` block for better organization of tests which is useful for larger test suites.
   - **Cons**: Slightly more verbose due to the `describe` block but no real cons for the complexity of the task.
   - **Code Example**:
     ```javascript
     describe('multiply', () => {
       test('correctly multiplies 3 by 5', () => {
         expect(multiply(3, 5)).toBe(15);
       });
     });
     ```

### Axet Gaia
   - **Pros**: Provides a clear explanation of the test structure and good use of Jest testing syntax. It also outlines the setup (`Arrange`), execution (`Act`), and assertion (`Assert`) phases explicitly which is good for understanding and maintaining tests.
   - **Cons**: Slightly verbose for a simple function test but beneficial for educational purposes.
   - **Code Example**:
     ```javascript
     test('multiply function should correctly multiply 3 by 5', () => {
       const num1 = 3;
       const num2 = 5;
       const result = multiply(num1, num2);
       expect(result).toBe(15);
     });
     ```

### ChatGPT 4
   - **Pros**: Comprehensive setup with complete instructions for setting up Jest, which is helpful for beginners. Uses modern JavaScript syntax with ES6 module imports.
   - **Cons**: Requires changes in project setup (like modifying `package.json`) which may not be necessary just for one test.
   - **Code Example**:
     ```javascript
     describe('multiply function tests', () => {
       test('multiplies 3 and 5 to get 15', () => {
         expect(multiply(3, 5)).toBe(15);
       });
     });
     ```

### Meta.ai
   - **Pros**: Simple and concise, using modern JavaScript import statements, assuming ES6 modules are enabled.
   - **Cons**: Less detail in terms of setup and execution which might be needed for complete beginners.
   - **Code Example**:
     ```javascript
     import { multiply } from './multiply';
     describe('multiply', () => {
       it('returns the product of two numbers', () => {
         expect(multiply(3, 5)).toBe(15);
       });
     });
     ```

### Gemini

- **Pros**: Gemini's test is exceptionally straightforward, combining the function definition and test in one file for easy readability and quick testing.
 - **Cons**: The lack of modularity, with the function and test combined, could complicate maintenance and scalability in larger projects.
 - **Code Example**:
   ```javascript
      test('multiply function multiplies two numbers correctly', () => {
      const result = multiply(3, 5);
      expect(result).toBe(15);
    });

    function multiply(a, b) {
      return a * b;
    }
   ```


## Conclusion

**Best Implementation**: **ChatGpt 4** offers a comprehensive guide that is very useful for beginners, providing detailed steps and a complete setup guide, making it easy to understand and implement.

**Worst Implementation**: Although there isn't a "worst" since all solutions effectively fulfill the task, the **Gemini** approach could be considered less suitable for professional or larger scale projects due to its lack of modularity and direct inclusion of business logic within the test file, potentially complicating future scalability and maintenance.
