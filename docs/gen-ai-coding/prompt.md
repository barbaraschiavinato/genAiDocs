# Well-Crafted Prompt

## Importance of a Well-Crafted Prompt for Code Generation

Creating a good prompt is key to getting the most out of generative AI tools for code generation. When your prompt is detailed and precise, it ensures the AI understands exactly what you need. This clarity reduces the chances of the AI generating irrelevant or incorrect code.

By specifying the framework, libraries, and specific functionalities, you guide the AI to produce code that fits your project requirements and expectations. This not only makes the code more relevant but also more accurate.

Detailing instructions on performance optimization, error handling, and modularization helps ensure the generated code is efficient, maintainable, and performs well. Including security practices and data handling requirements means the code will be safer and comply with necessary regulations.

When you provide clear guidelines for testing, error logging, and handling edge cases, you make sure the generated code is robust and reliable. This reduces the risk of bugs and vulnerabilities.

Specifying the use of the latest versions of libraries and frameworks helps keep your code future-proof, ensuring it stays compatible with upcoming changes and standards. A comprehensive prompt covers a wide range of technical, functional, and non-functional aspects, making sure the generated code is complete and ready for integration into your project.

## Ensuring Code Quality with Extra Risk Mitigations

Adding extra risk mitigations (highlighted on the previous page) helps tackle common problems that come with using generative AI tools.

By asking for compatibility with the latest library versions, we reduce the risk of generating outdated or deprecated code. Detailed requirements help minimize inaccuracies caused by incorrect or speculative information in the AI's training data.

Clear instructions and library names reduce the chances of the AI making incorrect assumptions or providing inaccurate autocomplete suggestions. Emphasizing validation and correctness ensures the AI-generated code adheres to current standards and avoids deprecated practices.

Detailed requirements prevent the AI from overgeneralizing, ensuring the generated code meets your project's specific needs. Explicitly asking for error handling, logging, and testing makes the code more robust and less prone to unnoticed errors.

Providing clear and detailed instructions helps the AI understand exactly what you need, reducing the likelihood of irrelevant or generic suggestions. Breaking down the requirements into smaller parts helps the AI process and understand the entire scope, even with token limitations.

Ensuring the AI can manage complex relationships within the codebase by providing detailed dependencies and interconnections helps mitigate the challenge of dealing with complexity and dependencies in long code.


## Considering Regional Conventions and Language Bias

To ensure the generated code adheres to regional conventions and mitigates language bias, the prompt should:

- **Use English for Prompts**: Leveraging English due to its prevalence in AI training data, technical terminology, and resources helps reduce biases and improve the accuracy and consistency of AI-generated code.
- **Avoid Ambiguous Terms**: Steer clear of terms that may have different interpretations in various languages or regions to prevent misunderstandings.
- **Specify Locale Settings**: Clearly define locale settings for applications to handle regional conventions accurately, such as currency, dates, and times.
- **Include Comments and Documentation**: Provide comments and documentation in the desired language and specify if the AI should consider regional best practices and conventions.
- **Be Language-Aware**: Recognize the influence of the prompt's language on the AI's assumptions and the conventions it follows, and adjust accordingly.

## Requirements to Create a Well-Crafted Prompt

### Comprehensive Requirements
- **Framework and Libraries**: By specifying Next.js, NextAuth.js, and Bootstrap, the prompt clearly defines the technology stack, reducing ambiguity about the foundational tools to be used.
- **Functionality**: Detailed requirements for form validation, WCAG compliance, and server-side rendering ensure that the core functionalities are well-defined and aligned with best practices.
- **Additional Requirements**: Including instructions for clear variable names, comments, performance optimization, error handling, and modularity promotes maintainable, efficient, and robust code.

### Risk Mitigation
- **Old Training Data**: By asking for compatibility with the latest versions of libraries, the prompt mitigates the risk of generating outdated or deprecated code.
- **Data Training Errors**: Specific functionality and requirements help minimize inaccuracies due to incorrect or speculative information in the AI's training data.
- **Autocompletion and Assumptions**: Clear instructions and library names reduce the likelihood of incorrect assumptions or autocomplete errors by the AI.
- **Lack of Real-Time Validation**: The prompt’s emphasis on validation and correctness ensures that the AI-generated code adheres to current standards and documentation.
- **Generalization from Existing Knowledge**: Detailed requirements prevent the AI from overgeneralizing and ensure that it meets the specific needs of the project.
- **No Error Checking**: Explicitly asking for error handling, logging, and testing ensures that the generated code is robust and less prone to unnoticed errors.
- **Precision in Prompting**: Clear and detailed instructions help the AI understand the exact requirements, reducing the likelihood of irrelevant or generic suggestions.
- **Context Limitations**: Breaking down the requirements into smaller, manageable parts helps the AI process and understand the entire scope, even with token limitations.
- **Complexity and Dependencies**: Providing detailed dependencies and interconnections ensures that the AI can manage complex relationships within the codebase.

### Comprehensive Coverage
- The prompt covers a wide range of technical, functional, and non-functional aspects, ensuring that the generated code is complete, reliable, and maintainable.

### Detailed Explanations
- Asking for explanations where necessary ensures that developers can understand and validate the AI-generated code more easily, promoting transparency and knowledge transfer.

### Specific Requirements
- **Modularity and Reusability**: Ensures that the code is easy to maintain and extend.
- **Testing Coverage**: Comprehensive testing helps ensure that the code is reliable and bug-free.
- **Documentation**: Detailed documentation makes it easier for future developers to understand and work with the code.
- **Performance Optimization**: Ensures that the application runs efficiently.
- **Error Logging and Monitoring**: Helps in tracking and resolving issues in production.
- **Internationalization (i18n)**: Makes the application accessible to a global audience.
- **CI/CD Setup**: Automates testing, building, and deployment processes, improving development efficiency.
- **Accessibility Testing**: Ensures the application meets accessibility standards, making it usable for people with disabilities.

### Security and Compliance
- **Security**: Secure coding practices and handling of sensitive information protect the application from vulnerabilities.
- **Data Handling**: Proper handling of errors and sensitive information ensures data integrity and security.
- **Compliance**: Adhering to privacy regulations and documenting dependencies reduces legal and ethical risks.

### Future-Proofing
- By specifying the use of the latest versions of libraries and ensuring compatibility with current standards, the prompt helps future-proof the generated code against upcoming changes and deprecations.

## Well-Crafted Prompt example

```plaintext

Develop a Next.js web application with the following features and requirements:

1. **Framework and Libraries**:
   - Use Next.js (version 12) for the framework.
   - Integrate Azure Active Directory authentication using NextAuth.js (version 4).
   - Use Bootstrap (version 5) for styling.

2. **Functionality**:
   - Include a form with mandatory username (email) and password fields, both with inline validation.
   - Ensure the form is accessible and WCAG compliant.
   - Implement server-side rendering for initial page load.
   - Include basic unit tests with Jest for form validation and authentication flow.

3. **Additional Requirements**:
   - Use clear and descriptive variable and function names.
   - Add comments explaining the purpose of complex logic and code segments.
   - Optimize for performance and efficiency.
   - Ensure the code handles edge cases, such as invalid input or network failures.
   - Modularize the code with reusable components and functions.
   - Provide comprehensive testing coverage, including unit, integration, and end-to-end tests.
   - Include detailed documentation, such as comments and README files.
   - Implement error logging and monitoring.
   - Support internationalization (i18n) if applicable.
   - Set up continuous integration (CI) pipelines for automated testing, building, and deployment.
   - Perform automated accessibility testing to ensure WCAG compliance.

4. **Dependencies and Compatibility**:
   - Ensure compatibility with the latest versions of Next.js, NextAuth.js, and Bootstrap.
   - Avoid using deprecated or uncommon JavaScript features.
   - Validate the existence and correctness of external libraries and APIs used.

5. **Security**:
   - Implement secure coding practices, including input sanitization and protection against common vulnerabilities (e.g., XSS, CSRF).
   - Do not store sensitive data directly in localStorage; use secure cookies instead.

6. **Data Handling**:
   - Include error handling and logging for server-side operations.
   - Use environment variables for sensitive information like API keys and secrets.

7. **Compliance**:
   - Ensure the code complies with relevant privacy regulations (e.g., GDPR, CCPA).
   - Document any third-party dependencies and their licenses.

8. **Regional Conventions and Language Bias**:
   - Specify locale settings for dates, times, and currencies.
   - Ensure documentation and comments consider regional best practices and conventions.

**Input**: User data including username and password.
**Output**: A secure and functional login form with inline validation.
**Performance**: Ensure the login process completes within 500ms under normal load.
**Edge Cases**: Handle invalid email formats, weak passwords, and network failures gracefully.
**Security**: Must pass OWASP security checks.

```