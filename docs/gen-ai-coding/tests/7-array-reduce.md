# 7. Array reduce

## Prompt

I have this array. I need to create a report of the total items sold and the total price avoiding products repetitions. 


```js
const lineItems = [
  { description: 'Eggs (Dozen)', quantity: 1, price: 3, total: 3 },
  { description: 'Cheese', quantity: 0.5, price: 5, total: 2.5 },
  { description: 'Butter', quantity: 2, price: 6, total: 12 },
  { description: 'Eggs (Dozen)', quantity: 4, price: 3, total: 12 },
];
```

## Results

### Amazon Q


Okay, let's tackle this step-by-step:

- We need to create an object that will store the total quantity and total price for each unique product. This will allow us to avoid repetitions.

- We'll iterate through the `lineItems` array and update the totals in the object as we go.

- Finally, we'll log out the report with the total items sold and total price for each unique product.

Here's the code to accomplish this:

```js
const report = {};

for (const item of lineItems) {
  const { description, quantity, price, total } = item;
  report[description].totalQuantity += quantity;
  report[description].totalPrice += total;
}

console.log('Product Report:');
for (const [product, stats] of Object.entries(report)) {
}

```

The key steps are:

1. Initialize an empty `report` object to store the totals.

2. Iterate through the `lineItems` array.

3. For each item, check if the `description` is already a key in the `report` object. If not, initialize it with `totalQuantity` and `totalPrice` properties.

4. Update the `totalQuantity` and `totalPrice` for the current `description`.

5. After the loop, iterate through the `report` object and log out the product details.

This will give you the following output:


```bash
Product Report:
Eggs (Dozen) - Total Quantity: 5, Total Price: $15.00
Cheese - Total Quantity: 0.5, Total Price: $2.50
Butter - Total Quantity: 2, Total Price: $12.00

```

The key benefit of this approach is that it avoids repetitions and calculates the totals for each unique product in the 
lineItems `array`.


### GitHub Copilot

To create a report of the total items sold and the total price avoiding product repetitions, you can use JavaScript's `reduce` function. This function can be used to transform an array into a single value. In this case, we'll transform the `lineItems` array into an object where each key is a product description and each value is an object containing the total quantity and total price for that product.

Here's the JavaScript code to do this:

```js
const report = lineItems.reduce((acc, item) => {
  if (!acc[item.description]) {
    acc[item.description] = { totalQuantity: 0, totalPrice: 0 };
  }
  acc[item.description].totalQuantity += item.quantity;
  acc[item.description].totalPrice += item.total;
  return acc;
}, {});

console.log(report);
```

This code will output an object like this:

```js
{
  'Eggs (Dozen)': { totalQuantity: 5, totalPrice: 15 },
  'Cheese': { totalQuantity: 0.5, totalPrice: 2.5 },
  'Butter': { totalQuantity: 2, totalPrice: 12 }
}
```

This object tells you the total quantity and total price for each product, without repeating products.

### Axet Gaia

Sure! Here's the JavaScript code that solves the problem while following best practices:

```js
const lineItems = [
  { description: 'Eggs (Dozen)', quantity: 1, price: 3, total: 3 },
  { description: 'Cheese', quantity: 0.5, price: 5, total: 2.5 },
  { description: 'Butter', quantity: 2, price: 6, total: 12 },
  { description: 'Eggs (Dozen)', quantity: 4, price: 3, total: 12 },
];

// Create an object to store the aggregated data
const report = {};

// Iterate over each line item
lineItems.forEach((item) => {
  // Check if the description already exists in the report object
  if (report[item.description]) {
    // If it exists, update the total quantity and price
    report[item.description].quantity += item.quantity;
    report[item.description].price += item.price;
  } else {
    // If it doesn't exist, add a new entry to the report object
    report[item.description] = {
      quantity: item.quantity,
      price: item.price,
    };
  }
});

// Print the report
console.log(report);
```

In this solution, we use an object called `report` to store the aggregated data. We iterate over each line item using the `forEach` method and check if the description already exists in the `report` object. If it does, we update the total quantity and price. If it doesn't, we add a new entry to the `report` object. Finally, we print the `report` object to see the result.

This solution avoids product repetitions by aggregating the quantity and price for items with the same description.

### ChatGpt 4

To generate a report of the total items sold and the total price for each product, while avoiding repetition of products in your list, you'll need to aggregate the data based on the product description. This involves summing the quantities and total prices for items with the same description.

Here's how you can do it in JavaScript:

**JavaScript Code to Aggregate Data**

```js
const lineItems = [
  { description: 'Eggs (Dozen)', quantity: 1, price: 3, total: 3 },
  { description: 'Cheese', quantity: 0.5, price: 5, total: 2.5 },
  { description: 'Butter', quantity: 2, price: 6, total: 12 },
  { description: 'Eggs (Dozen)', quantity: 4, price: 3, total: 12 },
];

function generateReport(items) {
  const report = items.reduce((acc, item) => {
    // Check if the item description already exists in the accumulator
    if (acc[item.description]) {
      // Update the existing entry
      acc[item.description].quantity += item.quantity;
      acc[item.description].total += item.total;
    } else {
      // Create a new entry
      acc[item.description] = {
        description: item.description,
        quantity: item.quantity,
        total: item.total,
        price: item.price
      };
    }
    return acc;
  }, {});

  return Object.values(report); // Convert the accumulated object back to an array
}

// Call the function and log the results
const reportItems = generateReport(lineItems);
console.log(reportItems);
```

**Explanation**

1. **Data Structure Initialization**: We start by defining an array of `lineItems`, where each item is an object that includes the product's description, quantity, price, and the total price for that line item.

2. **Aggregation Logic**:
   - We use the `reduce` function to aggregate line item data into an object where each key is a unique product description.
   - If a product description already exists in the accumulator object, we add the current line item's quantity and total to the existing entry.
   - If a product description does not exist, we add a new key to the object with the initial quantity and total values.

3. **Result Formatting**:
   - After reducing all items, we convert the results stored in the object back into an array using `Object.values()`. This makes it easier to handle and display the results.
   - Each item in the resulting array shows the total quantity and total price for each product, without any repetition.

The resulting output of the script will be an array of objects, where each object contains the total quantities and prices summed up for products with the same description. This approach ensures that each product is listed only once with the correct totals, making it ideal for generating reports or summaries of sales data.

### Meta.ai

You can use a JavaScript object to keep track of the unique products and their total quantity and price. Here's an example:

```js
const report = {};

lineItems.forEach((item) => {
  if (!report[item.description]) {
    report[item.description] = { quantity: 0, price: 0 };
  }
  report[item.description].quantity += item.quantity;
  report[item.description].price += item.total;
});

console.log(report);

```

This will output:
```json
{
  "Eggs (Dozen)": { quantity: 5, price: 15 },
  "Cheese": { quantity: 0.5, price: 2.5 },
  "Butter": { quantity: 2, price: 12 }
}
```

Then, you can calculate the total items sold and total price:

```js
const totalItemsSold = Object.values(report).reduce((acc, curr) => acc + curr.quantity, 0);
const totalPrice = Object.values(report).reduce((acc, curr) => acc + curr.price, 0);

console.log(`Total items sold: ${totalItemsSold}`);
console.log(`Total price: ${totalPrice}`);

```
```
This will output:
Total items sold: 7.5
Total price: 29.5
```

Note that this assumes that the description property is the unique identifier for each product. If that's not the case, you may need to adjust the code accordingly.

### Gemini


```javascript
function generateSalesReport(lineItems) {
  // Use a Map to store product information (quantity and total price)
  const productReport = new Map();
  for (const item of lineItems) {
    const { description, quantity, price, total } = item;
    
    // Check if the product already exists in the Map
    if (productReport.has(description)) {
      // If it does, update the existing quantities and total price
      const existingProduct = productReport.get(description);
      existingProduct.quantity += quantity;
      existingProduct.total += total;
    } else {
      // If it doesn't, add a new entry for the product
      productReport.set(description, { quantity, total });
    }
  }

  // Generate the report header
  console.log("Sales Report:");

  // Loop through the Map entries and print product details
  for (const [product, info] of productReport.entries()) {
    console.log(`- ${product}: ${info.quantity} units, Total: $${info.total.toFixed(2)}`);
  }

  // Calculate and print the overall total items sold and total price
  const totalQuantity = [...productReport.values()].reduce((acc, cur) => acc + cur.quantity, 0);
  const totalPrice = [...productReport.values()].reduce((acc, cur) => acc + cur.total, 0);
  console.log(`\nTotal Items Sold: ${totalQuantity} units`);
  console.log(`Total Price: $${totalPrice.toFixed(2)}`);
}

generateSalesReport(lineItems);
```

**Explanation:**

1. **`generateSalesReport(lineItems)` function:** This function takes the `lineItems` array as input.
2. **`const productReport = new Map();`:** We create a Map object named `productReport` to store information about each product (description, quantity, and total price).
3. **`for (const item of lineItems) { ... }`:** This loop iterates through each item in the `lineItems` array.
4. **`const { description, quantity, price, total } = item;`:** We destructure the item object to access its properties for readability.
5. **`if (productReport.has(description)) { ... } else { ... }`:** This conditional block checks if the product (identified by its description) already exists in the `productReport` Map.
   - If it exists (`has(description)` returns true), we update the existing entry by adding the current item's quantity and total price to the corresponding values in the Map.
   - If it doesn't exist (`has(description)` returns false), we create a new entry in the Map for the product with its quantity and total price from the current item.
6. **`console.log("Sales Report:");`:** We print the report header.
7. **`for (const [product, info] of productReport.entries()) { ... }`:** This loop iterates through each key-value pair in the `productReport` Map.
   - `product` represents the product description (key).
   - `info` is an object containing the quantity and total price for that product (value).
   - Inside the loop, we print each product's details with quantity and total price formatted to two decimal places using `toFixed(2)`.
8. **`const totalQuantity = ...;`:** We calculate the total quantity of items sold by summing up the quantities of all products in the Map using `reduce`.
9. **`const totalPrice = ...;`:** We calculate the total price by summing up the total prices of all products in the Map using `reduce`.
10. **`console.log(...);`:** Finally, we print the overall total items sold and total price with proper formatting.
11. **`generateSalesReport(lineItems);`:** We call the `generateSalesReport` function with the `lineItems` array to execute the report generation.

This approach uses a Map to efficiently store and update product information, avoiding repetitions. It then iterates through the Map to generate the desired sales report format.

## Analysis

### Amazon Q
   - **Pros**: Demonstrates an attempt to aggregate data into a simple object, making logical use of JavaScript's object properties for direct access and update.
   - **Cons**: The implementation is flawed due to missing initialization for properties in the report object, leading to runtime errors when attempting to increment undefined properties.
   - **Code Example**:
     ```javascript
     const report = {};
     for (const item of lineItems) {
       const { description, quantity, total } = item;
       if (!report[description]) {
         report[description] = { totalQuantity: 0, totalPrice: 0 };
       }
       report[description].totalQuantity += quantity;
       report[description].totalPrice += total;
     }
     ```

### GitHub Copilot
   - **Pros**: Correctly uses JavaScript's `reduce` function to build an aggregated report, ensuring that each product is accounted for without duplication.
   - **Cons**: Minimal explanatory commentary, which might be needed for less experienced developers.
   - **Code Example**:
     ```javascript
     const report = lineItems.reduce((acc, item) => {
       if (!acc[item.description]) {
         acc[item.description] = { totalQuantity: 0, totalPrice: 0 };
       }
       acc[item.description].totalQuantity += item.quantity;
       acc[item.description].totalPrice += item.total;
       return acc;
     }, {});
     ```

### Axet Gaia
   - **Pros**: Employs a straightforward approach using a `forEach` loop, which is more readable for some developers.
   - **Cons**: Mismanages the data by incorrectly summing up the unit price rather than the total price, which can lead to inaccurate financial reports.
   - **Code Example**:
     ```javascript
     const report = {};
     lineItems.forEach((item) => {
       if (report[item.description]) {
         report[item.description].quantity += item.quantity;
         report[item.description].price += item.price; // Error in handling the price should focus on `total`, not `price`
       } else {
         report[item.description] = {
           quantity: item.quantity,
           price: item.total, // Incorrect initialization, should focus on total price
         };
       }
     });
     ```

### ChatGPT 4
   - **Pros**: Provides a comprehensive solution by encapsulating the logic in a function, enhancing reusability and clarity; includes clear instructions for usage.
   - **Cons**: The solution could be seen as overly verbose for this specific task but offers flexibility for further modification.
   - **Code Example**:
     ```javascript
     function generateReport(items) {
       return items.reduce((acc, item) => {
         if (!acc[item.description]) {
           acc[item.description] = { quantity: item.quantity, total: item.total };
         } else {
           acc[item.description].quantity += item.quantity;
           acc[item.description].total += item.total;
         }
         return acc;
       }, {});
     }
     const reportItems = generateReport(lineItems);
     console.log(reportItems);
     ```

### Meta.ai
   - **Pros**: Implements a simple iterative approach using `forEach`, correctly updating and initializing entries as needed.
   - **Cons**: Similar to other solutions, lacks detailed commentary which could aid in understanding the implementation.
   - **Code Example**:
     ```javascript
     const report = {};
     lineItems.forEach((item) => {
       if (!report[item.description]) {
         report[item.description] = { quantity: 0, price: 0 };
       }
       report[item.description].quantity += item.quantity;
       report[item.description].price += item.total;
     });
     ```

### Gemini
   - **Pros**: Utilizes a `Map` to store product data, which is a robust way to handle key-value pairs in JavaScript. This approach ensures that all operations on the product data are clear and properly isolated.
   - **Cons**: More complex than necessary for straightforward tasks but provides excellent structure for scalability and readability.
   - **Code Example**:
     ```javascript
     function generateSalesReport(lineItems) {
       const productReport = new Map();
       lineItems.forEach(item => {
         const { description, quantity, total } = item;
         if (!productReport.has(description)) {
           productReport.set(description, { quantity, total });
         } else {
           const product = productReport.get(description);
           product.quantity += quantity;
           product.total += total;
         }
       });
       return Array.from(productReport, ([description, data]) => ({ description, ...data }));
     }
     ```

## Conclusion

**Best Implementation**: **GitHub Copilot** provides the most robust solution using `reduce` effectively to aggregate the data into a single object with correct initializations and updates. It's concise, correct, and uses best practices.

**Worst Implementation**: **Axet Gaia**'s implementation, while attempting to solve the problem, incorrectly handles price calculations which could lead to significant errors in applications where financial accuracy is critical. 

**Note on Gemini**: The use of a `Map` object by Gemini offers a unique approach that provides excellent data integrity and readability, making it a strong contender for the best code practice in scenarios requiring detailed record management and future scalability.