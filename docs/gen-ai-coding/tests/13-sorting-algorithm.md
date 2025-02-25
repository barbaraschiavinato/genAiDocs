# 13. Sorting Algorithm

## Prompt

Implement a `quicksort` algorithm in Typescript that sorts an array of integers in ascending order.

## Results

### Amazon Q

```typescript

function quickSort(arr: number[]): number[] {
  if (arr.length <= 1) {
    return arr;
  }

  const pivot = arr[Math.floor(arr.length / 2)];
  const left = [];
  const right = [];
  const middle = [];

  for (const item of arr) {
    if (item < pivot) {
      left.push(item);
    } else if (item > pivot) {
      right.push(item);
    } else {
      middle.push(item);
    }
  }

  return [...quickSort(left), ...middle, ...quickSort(right)];
}

// Example usage
const unsortedArray = [5, 2, 9, 1, 7, 3, 8, 4, 6];
const sortedArray = quickSort(unsortedArray);
console.log(sortedArray); // Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Here's how the `quickSort` function works:

1. If the input array has 0 or 1 elements, it is already sorted, so we return the array as is.
2. We choose the middle element of the array as the pivot.
3. We create three empty arrays: `left`, `right`, and `middle`. We'll use these to partition the input array based on the pivot.
4. We loop through the input array and add each element to the appropriate partition array based on its comparison to the pivot.
5. We recursively call `quickSort` on the left` and `right` partitions, and then concatenate the sorted `left`, `middle`, and `right` partitions to get the final sorted array.

The time complexity of `quicksort` is O(n log n) on average, but it can degrade to O(n^2) in the worst case (when the array is already sorted or reverse-sorted). The space complexity is O(log n) due to the recursive calls.

### GitHub Copilot

1. Define a function `quicksort` that takes an array of numbers as input.
2. If the array length is less than or equal to 1, return the array as it is already sorted.
3. Choose a pivot element from the array. This can be the first, last, or middle element.
4. Create two empty arrays: `less` and `greater`.
5. Iterate over the array, excluding the pivot. If an element is less than the pivot, push it to the `less` array. If it's greater, push it to the `greater` array.
6. Recursively apply the `quicksort` function to both `less` and `greater` arrays.
7. Concatenate the sorted `less` array, pivot, and sorted `greater` array to get the sorted array.

Here is the TypeScript code implementing the above plan:

```typescript
function quicksort(array: number[]): number[] {
    if (array.length <= 1) {
        return array;
    }

    const pivot = array[array.length - 1];
    const left = [];
    const right = [];

    for (let i = 0; i < array.length - 1; i++) {
        if (array[i] < pivot) {
            left.push(array[i]);
        } else {
            right.push(array[i]);
        }
    }

    return [...quicksort(left), pivot, ...quicksort(right)];
}
```

You can use this function to sort an array of integers in ascending order.

### Axet Gaia

Sure! Here's the JavaScript code for implementing the quicksort algorithm in TypeScript:

```typescript
/**
 * Quicksort algorithm implementation in TypeScript.
 * Sorts an array of integers in ascending order.
 * @param arr - The array to be sorted.
 * @returns The sorted array.
 */
function quicksort(arr: number[]): number[] {
  if (arr.length <= 1) {
    return arr;
  }

  const pivot = arr[arr.length - 1];
  const left = [];
  const right = [];

  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] < pivot) {
      left.push(arr[i]);
    } else {
      right.push(arr[i]);
    }
  }

  return [...quicksort(left), pivot, ...quicksort(right)];
}

// Example usage:
const unsortedArray = [5, 2, 9, 1, 7];
const sortedArray = quicksort(unsortedArray);
console.log(sortedArray); // Output: [1, 2, 5, 7, 9]
```

**Explanation**

- The `quicksort` function takes an array of integers as input and returns the sorted array.
- If the array has only one element or is empty, it is already sorted, so we return it as is.
- We choose the last element of the array as the pivot.
- We create two empty arrays, `left` and `right`, to store the elements smaller and larger than the pivot, respectively.
- We iterate through the array, comparing each element to the pivot and pushing it into the appropriate array.
- Finally, we recursively call `quicksort` on the `left` and `right` arrays, and concatenate the sorted arrays with the pivot in between.

This implementation follows best practices for JavaScript, such as using `const` for variables that don't need to be reassigned, using arrow functions for concise code, and using TypeScript for type safety.

### ChatGpt 4

Below is an implementation of the Quicksort algorithm in TypeScript. This version of Quicksort uses the Lomuto partition scheme, which is a common method to choose the pivot element at the end of the array segment being sorted. This example demonstrates how to sort an array of integers in ascending order:

```typescript
function quicksort(array: number[], low: number, high: number): void {
    if (low < high) {
        let pivotIndex = partition(array, low, high);
        quicksort(array, low, pivotIndex - 1);
        quicksort(array, pivotIndex + 1, high);
    }
}

function partition(array: number[], low: number, high: number): number {
    const pivot = array[high];
    let i = low - 1;

    for (let j = low; j < high; j++) {
        if (array[j] < pivot) {
            i++;
            swap(array, i, j);
        }
    }
    swap(array, i + 1, high);
    return i + 1;
}

function swap(array: number[], index1: number, index2: number): void {
    const temp = array[index1];
    array[index1] = array[index2];
    array[index2] = temp;
}

// Example usage:
const arr = [10, 7, 8, 9, 1, 5];
quicksort(arr, 0, arr.length - 1);
console.log("Sorted array:", arr);
```

**Explanation**

- **quicksort function**: This is a recursive function that continues to sort the subarrays. It takes the array to be sorted, and the `low` and `high` indices as parameters, representing the current segment of the array that needs to be sorted.
- **partition function**: This function rearranges the elements in the current segment of the array based on their comparison with the pivot element. All elements less than the pivot are moved to the left of the pivot, and all greater elements are moved to the right.
- **swap function**: A helper function that swaps two elements in the array.
- **Example Usage**: The `arr` array is defined, and `quicksort` is called on it. After the sort, the array is logged to the console in its sorted order.

This Quicksort implementation is a classic example of divide-and-conquer algorithms, providing efficient average-case performance and is widely used in various applications.

### Meta.ai

Here is a TypeScript implementation of the quicksort algorithm:

```typescript
function quicksort(arr: number[]): number[] {
  if (arr.length <= 1) {
    return arr;
  }

  const pivot = arr[0];
  const less = [];
  const greater = [];

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] <= pivot) {
      less.push(arr[i]);
    } else {
      greater.push(arr[i]);
    }
  }

  return [...quicksort(less), pivot, ...quicksort(greater)];
}

// Example usage:
const arr = [5, 2, 8, 3, 1, 6, 4];
const sortedArr = quicksort(arr);
console.log(sortedArr); // [1, 2, 3, 4, 5, 6, 8]
```

Here's a brief explanation of the code:

- The `quicksort` function takes an array of integers as input and returns a sorted array.
- If the input array has only one element or is empty, we return it as it is already sorted.
- We choose the first element as the pivot.
- We create two arrays, less and greater, to store elements `less` `than` and `greater` than the pivot, respectively.
- We iterate through the input array, starting from the second element (index 1), and distribute elements into less and greater arrays based on their comparison with the pivot.
- We recursively call quicksort on less and greater arrays and concatenate the results with the pivot element in the middle.
- The spread operator (...) is used to flatten the recursive calls into a single array.
  
Note that this implementation uses the Lomuto partition scheme, which is a variation of the standard Hoare partition scheme that is slightly faster and more efficient in practice.

### Gemini


```typescript
function quicksort(arr: number[], low: number = 0, high: number = arr.length - 1): void {
  if (low < high) {
    const pivot = partition(arr, low, high);
    quicksort(arr, low, pivot - 1);
    quicksort(arr, pivot + 1, high);
  }
}

function partition(arr: number[], low: number, high: number): number {
  const pivot = arr[high];
  let i = low - 1;

  for (let j = low; j < high; j++) {
    if (arr[j] <= pivot) {
      i++;
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
  }

  [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];
  return i + 1;
}

// Example usage
const unsortedArray = [5, 3, 8, 2, 1, 4];
quicksort(unsortedArray);
console.log(unsortedArray); // Output: [1, 2, 3, 4, 5, 8]
```

**Explanation:**

1. **`quicksort` function:**
   - Takes an array of integers (`arr`), optional `low` and `high` indices (defaults to 0 and array length - 1).
   - Base case: If `low` is greater than or equal to `high`, the subarray is empty or has one element, so it's already sorted.
   - Recursive case:
     - Calls the `partition` function to choose a pivot element and partition the array around it.
     - Recursively sorts the left subarray (elements less than the pivot) from `low` to `pivot - 1`.
     - Recursively sorts the right subarray (elements greater than or equal to the pivot) from `pivot + 1` to `high`.

2. **`partition` function:**
   - Takes the array, `low`, and `high` indices.
   - Selects the last element (`arr[high]`) as the pivot.
   - Initializes a variable `i` to `low - 1` (index before the first element considered for swapping).
   - Loops through the array from `low` to `high - 1` (excluding the pivot):
     - If the current element (`arr[j]`) is less than or equal to the pivot, it belongs to the left subarray:
       - Increment `i`.
       - Swap the elements at `i` and `j`.
   - After the loop, the pivot element is in its final sorted position (`i + 1`). Swap the pivot with the element at `i + 1`.
   - Returns the index (`i + 1`) where the pivot is placed.

3. **Example Usage:**
   - Demonstrates how to call the `quicksort` function and print the sorted array.

**Note:**

- This implementation uses the first element (`arr[high]`) as the pivot. You can choose different pivot selection strategies (e.g., median-of-three) for potentially better performance in certain cases.
- Quicksort has an average time complexity of O(n log n) but can have a worst-case complexity of O(n^2) for already sorted or nearly sorted arrays. Consider using a different sorting algorithm for such cases. 



## Analysis

### Amazon Q
   - **Pros**: Implements the Quicksort algorithm effectively using a clear and common approach with the middle element as the pivot, which can help in balancing the partitions more evenly in varied datasets.
   - **Cons**: The specific choice of pivot (middle element) might not always prevent worst-case performance (O(n^2)) when the array is nearly sorted.
   - **Code Example**:
     ```typescript
     function quickSort(arr: number[]): number[] {
       if (arr.length <= 1) {
         return arr;
       }

       const pivot = arr[Math.floor(arr.length / 2)];
       const left = [];
       const right = [];
       const middle = [];

       for (const item of arr) {
         if (item < pivot) {
           left.push(item);
         } else if (item > pivot) {
           right.push(item);
         } else {
           middle.push(item);
         }
       }

       return [...quickSort(left), ...middle, ...quickSort(right)];
     }
     ```

### GitHub Copilot
   - **Pros**: Provides a straightforward implementation of the Quicksort algorithm that is easy to understand and use.
   - **Cons**: The pivot selection (last element) can lead to inefficient sorting (O(n^2)) under certain conditions, like already sorted arrays.
   - **Code Example**:
     ```typescript
     function quicksort(array: number[]): number[] {
       if (array.length <= 1) {
           return array;
       }

       const pivot = array[array.length - 1];
       const left = [];
       const right = [];

       for (let i = 0; i < array.length - 1; i++) {
           if (array[i] < pivot) {
               left.push(array[i]);
           } else {
               right.push(array[i]);
           }
       }

       return [...quicksort(left), pivot, ...quicksort(right)];
     }
     ```

### Axet Gaia
   - **Pros**: Provides a clear and well-commented implementation of the Quicksort algorithm that adheres to TypeScript standards.
   - **Cons**: Similar to GitHub Copilot’s solution, the pivot selection could lead to less optimal performance in worst-case scenarios.
   - **Code Example**:
     ```typescript
     function quicksort(arr: number[]): number[] {
       if (arr.length <= 1) {
         return arr;
       }

       const pivot = arr[arr.length - 1];
       const left = [];
       const right = [];

       for (let i = 0; i < arr.length - 1; i++) {
         if (arr[i] < pivot) {
           left.push(arr[i]);
         } else {
           right.push(arr[i]);
         }
       }

       return [...quicksort(left), pivot, ...quicksort(right)];
     }
     ```

### ChatGpt 4
   - **Pros**: Offers a detailed and traditional implementation of Quicksort, including in-place partitioning, which saves memory and is closer to the algorithm’s original intent.
   - **Cons**: The manual management of array indices can increase complexity and risk of errors; not using additional arrays for partitioning might be harder to understand for beginners.
   - **Code Example**:
     ```typescript
     function quicksort(array: number[], low: number, high: number): void {
         if (low < high) {
             let pivotIndex = partition(array, low, high);
             quicksort(array, low, pivotIndex - 1);
             quicksort(array, pivotIndex + 1, high);
         }
     }

     function partition(array: number[], low: number, high: number): number {
         const pivot = array[high];
         let i = low - 1;

         for (let j = low; j < high; j++) {
             if (array[j] < pivot) {
                 i++;
                 swap(array, i, j);
             }
         }
         swap(array, i + 1, high);
         return i + 1;
     }

     function swap(array: number[], index1: number, index2: number): void {
         const temp = array[index1];
         array[index1] = array[index2];
         array[index2] = temp;
     }
     ```

### Meta.ai
   - **Pros**: Simplifies the implementation by always using the first element as the pivot, which is intuitive and easy to understand.
   - **Cons**: Using the first element as the pivot could lead to poor performance on already sorted or nearly sorted data.
   - **Code Example**:
     ```typescript
     function quicksort(arr: number[]): number[] {
       if (arr.length <= 1) {
         return arr;
       }

       const pivot = arr[0];
       const less = [];
       const greater = [];

       for (let i = 1; i < arr.length; i++) {


         if (arr[i] <= pivot) {
           less.push(arr[i]);
         } else {
           greater.push(arr[i]);
         }
       }

       return [...quicksort(less), pivot, ...quicksort(greater)];
     }
     ```

### Gemini
   - **Pros**: Offers a concise implementation using Lomuto’s partition scheme which is generally easier to implement and understand than Hoare's partitioning.
   - **Cons**: The selection of the last element as the pivot can be problematic for already sorted arrays leading to O(n^2) time complexity.
   - **Code Example**:
     ```typescript
     function quicksort(arr: number[], low: number = 0, high: number = arr.length - 1): void {
       if (low < high) {
         const pivot = partition(arr, low, high);
         quicksort(arr, low, pivot - 1);
         quicksort(arr, pivot + 1, high);
       }
     }

     function partition(arr: number[], low: number, high: number): number {
       const pivot = arr[high];
       let i = low - 1;

       for (let j = low; j < high; j++) {
         if (arr[j] <= pivot) {
           i++;
           [arr[i], arr[j]] = [arr[j], arr[i]];
         }
       }

       [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];
       return i + 1;
     }
     ```

## Conclusion

**Best Implementation**: **ChatGpt 4** offers the most robust and traditionally accurate implementation of Quicksort, using in-place swapping which is more memory efficient and closer to the original algorithm.

**Worst Implementation**: While there isn’t a clear "worst" since all solutions effectively implement Quicksort, the implementations like **Meta.ai** and **Gemini** that consistently use the first or last element as a pivot might not perform optimally on already sorted or nearly sorted data.