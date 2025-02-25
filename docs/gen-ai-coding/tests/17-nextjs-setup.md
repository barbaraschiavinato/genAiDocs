# 17. NextJs project setup

## Prompt

You can setup a project that meets these characteristics (providing code):

1. using NextJs
2. be protected by Microsoft OAuth 2.0 authentication 
3. use Bootstrap as a css framework
4. contain a form with mandatory username (email) and password, both with inline validation
5. be WCAG compliant
6. add Jest test

note: for point 2 I deliberately used the wrong name (Microsoft Azure authentication exists, not just Microsoft)

## Results

### Amazon Q

```js
// pages/_app.js
import 'bootstrap/dist/css/bootstrap.css';
import { SessionProvider } from "next-auth/react"

export default function App({ Component, pageProps: { session, ...pageProps } }) {
  return (
    <SessionProvider session={session}>
      <Component {...pageProps} />
    </SessionProvider>
  )
}

// pages/api/auth/[...nextauth].js
import NextAuth from "next-auth"
import MicrosoftProvider from "next-auth/providers/microsoft"

export default NextAuth({
  providers: [
    MicrosoftProvider({
      clientId: process.env.MICROSOFT_CLIENT_ID,
      clientSecret: process.env.MICROSOFT_CLIENT_SECRET
    })
  ],
  secret: process.env.NEXTAUTH_SECRET
})

// pages/index.js
import { useState } from 'react';
import { useSession, signIn, signOut } from "next-auth/react"
import { Container, Row, Col, Form, Button } from 'react-bootstrap';

export default function Home() {
  const { data: session } = useSession();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [emailError, setEmailError] = useState('');
  const [passwordError, setPasswordError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    let isValid = true;

    if (!email) {
      setEmailError('Email is required');
      isValid = false;
    } else if (!/\S+@\S+\.\S+/.test(email)) {
      setEmailError('Email is invalid');
      isValid = false;
    } else {
      setEmailError('');
    }

    if (!password) {
      setPasswordError('Password is required');
      isValid = false;
    } else {
      setPasswordError('');
    }

    if (isValid) {
      // Handle form submission
    }
  }

  return (
    <Container className="my-5">
      <Row>
        <Col>
          <h1>Welcome to my Next.js app</h1>
          {session ? (
            <div>
              Signed in as {session.user.email} <br />
              <button onClick={() => signOut()}>Sign out</button>
            </div>
          ) : (
            <button onClick={() => signIn('microsoft')}>Sign in with Microsoft</button>
          )}
        </Col>
      </Row>
      <Row>
        <Col>
          <Form onSubmit={handleSubmit}>
            <Form.Group className="mb-3" controlId="formBasicEmail">
              <Form.Label>Email address</Form.Label>
              <Form.Control
                type="email"
                placeholder="Enter email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                isInvalid={!!emailError}
              />
              <Form.Control.Feedback type="invalid">
                {emailError}
              </Form.Control.Feedback>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>Password</Form.Label>
              <Form.Control
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                isInvalid={!!passwordError}
              />
              <Form.Control.Feedback type="invalid">
                {passwordError}
              </Form.Control.Feedback>
            </Form.Group>

            <Button variant="primary" type="submit">
              Submit
            </Button>
          </Form>
        </Col>
      </Row>
    </Container>
  )
}

// tests/index.test.js
import { render, screen, fireEvent } from '@testing-library/react';
import Home from '../pages/index';

test('renders the login form', () => {
  render(<Home />);
  expect(screen.getByLabelText('Email address')).toBeInTheDocument();
  expect(screen.getByLabelText('Password')).toBeInTheDocument();
  expect(screen.getByRole('button', { name: 'Submit' })).toBeInTheDocument();
});

test('validates the login form', () => {
  render(<Home />);
  fireEvent.click(screen.getByRole('button', { name: 'Submit' }));
  expect(screen.getByText('Email is required')).toBeInTheDocument();
  expect(screen.getByText('Password is required')).toBeInTheDocument();
});
```

This example covers the following:

1. **NextJS**: The project is built using the Next.js framework.

1. **Microsoft OAuth 2.0 Authentication**: The authentication is handled using the `next-auth/providers/microsoft` package, which integrates with the Microsoft OAuth 2.0 provider.

1. **Bootstrap**: The project uses the Bootstrap CSS framework for styling.

1. **Form with Inline Validation**: The login form includes email and password fields with inline validation.

1. **WCAG Compliance**: The project uses standard HTML elements and follows best practices for accessibility.

1. **Jest Tests**: The example includes two basic tests using the `@testing-library/react` library.

To use this example, you'll need to set the following environment variables:

- `MICROSOFT_CLIENT_ID`: Your Microsoft OAuth 2.0 client ID

- `MICROSOFT_CLIENT_SECRET`: Your Microsoft OAuth 2.0 client secret

- `NEXTAUTH_SECRET`: A secret key used for NextAuth.js

Please note that this is a basic example, and you may need to customize it further to fit your specific requirements. Additionally, make sure to follow best practices for handling sensitive information, such as storing environment variables securely.

### GitHub Copilot


```bash
# Step 1: Initialize a new Next.js project
npx create-next-app@latest nextjs-app

# Navigate into the project directory
cd nextjs-app

# Step 2: Install necessary packages for Microsoft OAuth 2.0 authentication
npm install next-auth

# Step 3: Install Bootstrap for CSS framework
npm install bootstrap

# Step 4: Create a form with mandatory username (email) and password fields, both with inline validation
# This step will be done in the code, not in the terminal

# Step 5: Ensure the project is WCAG compliant
# This step will be done in the code, not in the terminal

# Step 6: Install Jest and set up a basic test
npm install --save-dev jest
```

For step 4, you can create a new file in the `pages` directory, say `login.js`, and add the form there. For step 5, you need to follow WCAG guidelines when writing your code. For step 6, you can create a new file in the root directory, say `App.test.js`, and write your tests there.


### Axet Gaia

To implement the technical requirement, you can modify the provided JavaScript code as follows:

```js
// Import necessary modules
import React from 'react';
import { useForm } from 'react-hook-form';
import * as yup from 'yup';
import { yupResolver } from '@hookform/resolvers/yup';

// Define the validation schema using yup
const schema = yup.object().shape({
  username: yup.string().email('Invalid email').required('Email is required'),
  password: yup.string().required('Password is required'),
});

// Create a functional component for the form
const Form = () => {
  const { register, handleSubmit, errors } = useForm({
    resolver: yupResolver(schema),
  });

  // Handle form submission
  const onSubmit = (data) => {
    console.log(data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div>
        <label htmlFor="username">Username (Email)</label>
        <input type="text" id="username" name="username" ref={register} />
        {errors.username && <p>{errors.username.message}</p>}
      </div>
      <div>
        <label htmlFor="password">Password</label>
        <input type="password" id="password" name="password" ref={register} />
        {errors.password && <p>{errors.password.message}</p>}
      </div>
      <button type="submit">Submit</button>
    </form>
  );
};

export default Form;
```

**Explanation**

- We import the necessary modules, including React, react-hook-form, yup, and @hookform/resolvers/yup.
- We define a validation schema using yup, which specifies that the username field should be a valid email and is required, and the password field is required.
- We create a functional component called Form.
- Inside the Form component, we use the useForm hook from react-hook-form, passing the yupResolver to handle form validation based on the defined schema.
- We define an onSubmit function to handle form submission. In this example, it simply logs the form data to the console.
- The return statement renders a form with input fields for username and password. The ref attribute is used to register the input fields with react-hook-form.
- We display error messages for invalid inputs using the errors object provided by react-hook-form and yup validation.

This implementation follows best practices by using a popular form library (react-hook-form) and a validation library (yup) to handle form validation. It also separates concerns by defining the validation schema separately and using a functional component for the form.

### ChatGpt 4

To set up a Next.js project with Microsoft OAuth 2.0 authentication, Bootstrap as the CSS framework, a form with validation, WCAG compliance, and Jest testing, follow these step-by-step instructions:

**Step 1: Initialize the Next.js Project**

First, make sure you have Node.js installed. Then, create a new Next.js project:

```bash
npx create-next-app my-next-app
cd my-next-app
```

**Step 2: Install Dependencies**

You’ll need several packages for OAuth, Bootstrap, form validation, and testing:

```bash
npm install next-auth @next-auth/microsoft-provider bootstrap formik yup jest @testing-library/react @testing-library/jest-dom
```

**Step 3: Set Up Bootstrap**

Import Bootstrap in your project. Add it globally by modifying `_app.js`:

```js
import 'bootstrap/dist/css/bootstrap.min.css';
```

**Step 4: Configure Microsoft OAuth 2.0**

Set up NextAuth.js to handle OAuth with Microsoft. Modify `pages/api/auth/[...nextauth].js` to include Microsoft authentication:

```js
import NextAuth from 'next-auth'
import MicrosoftProvider from "@next-auth/microsoft-provider";

export default NextAuth({
  providers: [
    MicrosoftProvider({
      clientId: process.env.MICROSOFT_CLIENT_ID,
      clientSecret: process.env.MICROSOFT_CLIENT_SECRET,
      authorization: { params: { scope: "openid email profile" } }
    }),
  ],
})
```
Ensure you set `MICROSOFT_CLIENT_ID` and `MICROSOFT_CLIENT_SECRET` in your `.env.local` file.

**Step 5: Create a Form with Validation**

Use Formik and Yup for client-side validation. Create a form in `pages/index.js`:

```js
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';

const validationSchema = Yup.object().shape({
  username: Yup.string().email('Invalid email').required('Required'),
  password: Yup.string().required('Required'),
});

export default function Home() {
  return (
    <div className="container mt-5">
      <h1>Login</h1>
      <Formik
        initialValues={{ username: '', password: '' }}
        validationSchema={validationSchema}
        onSubmit={(values, { setSubmitting }) => {
          alert(JSON.stringify(values, null, 2));
          setSubmitting(false);
        }}
      >
        <Form>
          <div className="form-group">
            <label htmlFor="username">Email:</label>
            <Field name="username" type="email" className="form-control" />
            <ErrorMessage name="username" component="div" className="text-danger" />
          </div>
          <div className="form-group">
            <label htmlFor="password">Password:</label>
            <Field name="password" type="password" className="form-control" />
            <ErrorMessage name="password" component="div" className="text-danger" />
          </div>
          <button type="submit" className="btn btn-primary">
            Submit
          </button>
        </Form>
      </Formik>
    </div>
  );
}
```

**Step 6: Ensure WCAG Compliance**

For accessibility:

- Ensure all form elements have appropriate labels.
- Use semantic HTML.
- Check color contrasts and provide ARIA roles where necessary.

You can utilize tools like aXe or Wave to check compliance automatically.

**Step 7: Write Jest Tests**

Set up Jest to test your Next.js application. First, configure Jest by creating a `jest.config.js` file:

```js
module.exports = {
  setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],
  testPathIgnorePatterns: ['<rootDir>/.next/', '<rootDir>/node_modules/'],
  moduleNameMapper: {
    '\\.(css|less|scss|sass)$': 'identity-obj-proxy',
  },
  testEnvironment: 'jsdom',
};
```

Create `jest.setup.js` for extending Jest with additional functionality:
```js
import '@testing-library/jest-dom';
```

Then, create a test file `__tests__/index.test.js` for the form:

```js
import { render, fireEvent, waitFor } from '@testing-library/react';
import Home from '../pages/index';

describe('Home', () => {
  it('renders the form and submits data', async () => {
    const { getByLabelText, getByRole, findByText } = render(<Home />);

    fireEvent.change(getByLabelText(/email/i), { target: { value: 'user@example.com' } });
    fireEvent.change(getByLabelText(/password/i), { target: { value: 'password' } });

    fireEvent.click(getByRole('button', { name: /submit/i }));

    await findByText(/user@example.com/);
  });
});
```

To run your tests, add a script to your `package.json`:
```json
"scripts": {
  "test": "jest"
}
```

Then execute the tests with:
```bash
npm test
```

This setup provides a full-stack solution using Next.js with Microsoft OAuth 2.0, Bootstrap, Formik for forms with inline validation, Jest for testing, and ensures WCAG compliance.

### Meta.ai


Here is a basic setup for a Next.js project that meets the characteristics you specified:

**Project Structure**
```
components
LoginForm.js
...
pages
index.js
...
public
...
styles
bootstrap.min.css
...
tests
LoginForm.test.js
...
next.config.js
package.json
```

**next.config.js**

```js
module.exports = {
  //...
  plugins: [
    [
      'next-auth',
      {
        // Configure Microsoft OAuth 2.0 authentication
        auth: {
          microsoft: {
            clientId: 'YOUR_CLIENT_ID',
            clientSecret: 'YOUR_CLIENT_SECRET',
            tenantId: 'YOUR_TENANT_ID',
          },
        },
      },
    ],
  ],
}
```

**components/LoginForm.js**

```jsx
import { useForm } from 'react-hook-form';
import { useState } from 'react';

function LoginForm() {
  const { register, handleSubmit, errors } = useForm();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const onSubmit = async (data) => {
    // Call NextAuth's signIn function
    const result = await signIn('microsoft', data);
    if (result.ok) {
      // Login successful, redirect to protected page
    } else {
      // Login failed, show error message
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div>
        <label>Username (email)</label>
        <input
          type="email"
          {...register('username', { required: true })}
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        {errors.username && <span>Required</span>}
      </div>
      <div>
        <label>Password</label>
        <input
          type="password"
          {...register('password', { required: true })}
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        {errors.password && <span>Required</span>}
      </div>
      <button type="submit">Login</button>
    </form>
  );
}

export default LoginForm;
```

**pages/index.js**
```jsx
import Head from 'next/head';
import LoginForm from '../components/LoginForm';

function HomePage() {
  return (
    <div>
      <Head>
        <title>Login Page</title>
      </Head>
      <LoginForm />
    </div>
  );
}

export default HomePage;
```

**styles/bootstrap.min.css**
```css
/* Bootstrap CSS framework */
```

**tests/LoginForm.test.js**
```js
import React from 'react';
import { render, fireEvent, waitFor } from '@testing-library/react';
import LoginForm from '../components/LoginForm';

describe('LoginForm', () => {
  it('renders form with username and password fields', () => {
    const { getByLabelText } = render(<LoginForm />);
    expect(getByLabelText('Username (email)')).toBeInTheDocument();
    expect(getByLabelText('Password')).toBeInTheDocument();
  });

  it('validates username and password fields', async () => {
    const { getByLabelText, getByText } = render(<LoginForm />);
    const usernameInput = getByLabelText('Username (email)');
    const passwordInput = getByLabelText('Password');
    const submitButton = getByText('Login');

    // Test invalid submission
    fireEvent.change(usernameInput, { target: { value: '' } });
    fireEvent.change(passwordInput, { target: { value: '' } });
    fireEvent.click(submitButton);
    await waitFor(() => getByText('Required'));
    expect(getByText('Required')).toBeInTheDocument();

    // Test valid submission
    fireEvent.change(usernameInput, { target: { value: 'user@example.com' } });
    fireEvent.change(passwordInput, { target: { value: 'password' } });
    fireEvent.click(submitButton);
    await waitFor(() => expect(submitButton).toBeDisabled());
  });
});
```
This setup uses NextAuth for Microsoft OAuth 2.0 authentication, Bootstrap as the CSS framework, and Jest for testing. The `LoginForm` component uses React Hook Form for inline validation. The project structure follows WCAG guidelines for accessibility.

Note that you'll need to replace `YOUR_CLIENT_ID`, `YOUR_CLIENT_SECRET`, and `YOUR_TENANT_ID` with your actual Microsoft Azure AD application credentials.

I hope this helps! Let me know if you have any questions or need further assistance.

### Gemini


**1. Project Setup:**

- Create a new Next.js project:

   ```bash
   npx create-next-app my-app
   ```

- Install required dependencies:

   ```bash
   npm install bootstrap @types/bootstrap react-hook-form yup react-test-renderer msgraph-sdk-javascript
   ```

**2. Microsoft Azure AD Authentication (OAuth 2.0):**

**Explanation:**

- Create an Azure AD application in the Azure portal ([https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app)).
- Configure the following settings in your Azure AD application:
   - **Supported account types:** Choose who can access your application (e.g., accounts in any organizational directory).
   - **Redirect URIs (web):** Add the redirect URI for your Next.js application. This follows the format `http://localhost:3000/api/auth/callback`.
   - **Expose an API (optional):** If your application needs to access Microsoft Graph data, enable the appropriate Microsoft Graph delegated permissions (e.g., User.Read).
- Obtain the following application details from Azure AD:
   - Client ID
   - Authority (usually in the format `https://login.microsoftonline.com/<tenant-id>/v2.0`)

**3. Environment Variables:**

- Create a `.env.local` file at the root of your project (**gitignore** this file):

   ```
   AZURE_AD_CLIENT_ID=your_client_id
   AZURE_AD_AUTHORITY=your_authority_uri
   # ... other environment variables you might need (e.g., Microsoft Graph scopes)
   ```

- Load environment variables in `next.config.js`:

   ```javascript
   module.exports = {
     reactStrictMode: true,
     env: {
       AZURE_AD_CLIENT_ID: process.env.AZURE_AD_CLIENT_ID,
       AZURE_AD_AUTHORITY: process.env.AZURE_AD_AUTHORITY,
       // ... other environment variables
     },
   };
   ```

**4. Authentication Provider (Context API):**

   - Create a file named `AuthContext.js`:

     ```javascript
     import React, { createContext, useContext, useState, useEffect } from 'react';
     import { msGraphClient } from '../utils/msGraphClient'; // Import helper function

     const AuthContext = createContext({
       user: null,
       setUser: () => {},
       isAuthenticated: false,
       setIsAuthenticated: () => {},
       isLoading: true,
       setIsLoading: () => {},
     });

     export const AuthProvider = ({ children }) => {
       const [user, setUser] = useState(null);
       const [isAuthenticated, setIsAuthenticated] = useState(false);
       const [isLoading, setIsLoading] = useState(true);

       useEffect(() => {
         // Check for existing authentication in local storage
         const storedUser = localStorage.getItem('user');
         if (storedUser) {
           setUser(JSON.parse(storedUser));
           setIsAuthenticated(true);
         }
         setIsLoading(false);
       }, []);

       const handleLogin = async (data) => {
         // Implement login logic using MSAL library (refer to official documentation)
         // ...
       };

       const handleLogout = () => {
         setUser(null);
         setIsAuthenticated(false);
         localStorage.removeItem('user');
         // Optionally, redirect to Azure AD logout endpoint
       };

       const contextValue = {
         user,
         setUser,
         isAuthenticated,
         setIsAuthenticated,
         isLoading,
         setIsLoading,
         handleLogin,
         handleLogout,
       };

       return (
         <AuthContext.Provider value={contextValue}>{children}</AuthContext.Provider>
       );
     };

     export const useAuth = () => useContext(AuthContext);

     export default AuthContext;
     ```

**5. Login Form Component (`LoginForm.js`):**

   - Create a component for the login form using `react-hook-form` for validation and Bootstrap classes for styling:

     ```javascript
     import React from 'react';
     import { useForm } from 'react-hook-form';
     import { yupResolver } from '@hookform/resolvers/yup';
     import * as yup from 'yup';
     import { useAuth } from './AuthContext'; // Import AuthContext
     ```
     
## Analysis

### Amazon Q

**Pros:**
- Comprehensive code snippets for setting up Next.js with NextAuth, form validation, and testing.
- Good integration of Bootstrap and practical session management.

**Cons:**
- Incorrect suggestion for Microsoft authentication provider.
- Complexity might challenge beginners.

**Code Example:**
```js
import NextAuth from "next-auth"
import MicrosoftProvider from "next-auth/providers/microsoft"  // Incorrect import

export default NextAuth({
  providers: [
    MicrosoftProvider({
      clientId: process.env.MICROSOFT_CLIENT_ID,
      clientSecret: process.env.MICROSOFT_CLIENT_SECRET
    })
  ],
  secret: process.env.NEXTAUTH_SECRET
})
```

### GitHub Copilot

**Pros:**
- Simple, straightforward setup guide.
- Easy to follow for initial project setup.

**Cons:**
- Lacks detailed code implementations for OAuth authentication and testing.
- Requires additional customization.

**Code Example:**
```bash
npm install next-auth
npm install bootstrap
npm install --save-dev jest
```

### Axet Gaia

**Pros:**
- Utilizes modern practices with react-hook-form and yup for validation.
- Clean, well-structured code.

**Cons:**
- Does not address authentication setup.
- Misses implementation of testing.

**Code Example:**
```js
const { register, handleSubmit, errors } = useForm({
  resolver: yupResolver(schema),
});
```

### ChatGPT 4

**Pros:**
- Extensive instructions and detailed code.
- Thorough explanation of each integration step.

**Cons:**
- Suggests a nonexistent Microsoft authentication provider.
- Detailed steps might overwhelm beginners.

**Code Example:**
```js
import MicrosoftProvider from "@next-auth/microsoft-provider"; // Incorrect import

export default NextAuth({
  providers: [
    MicrosoftProvider({
      clientId: process.env.MICROSOFT_CLIENT_ID,
      clientSecret: process.env.MICROSOFT_CLIENT_SECRET,
      authorization: { params: { scope: "openid email profile" } }
    }),
  ],
})
```

### Meta.ai

**Pros:**
- Focuses on modular component design.
- Uses modern form validation practices with react-hook-form.

**Cons:**
- Does not provide a solution for Microsoft authentication.
- Fragmented setup requires additional configuration efforts.

**Code Example:**
```jsx
function LoginForm() {
  const { register, handleSubmit, errors } = useForm();
  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      ...
    </form>
  );
}
```

### Gemini

**Pros:**
Gemini provides a structured approach to project setup with clear steps, focusing on using modern tools and libraries like `react-hook-form`, `yup`, and Microsoft Graph SDK. It offers a concise and clean implementation for setting up Microsoft Azure AD authentication and Bootstrap integration.

**Cons:**
The solution lacks specific details on some aspects such as WCAG compliance and Jest testing. Additionally, the example might require further customization to meet specific project requirements, particularly in the context of testing and accessibility.

**Code Example:**
```javascript
import React from 'react';
import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';
import { useAuth } from './AuthContext'; // Import AuthContext

// Define the validation schema using yup
const schema = yup.object().shape({
  username: yup.string().email('Invalid email').required('Email is required'),
  password: yup.string().required('Password is required'),
});

// Create a functional component for the form
const LoginForm = () => {
  const { register, handleSubmit, errors } = useForm({
    resolver: yupResolver(schema),
  });
  const { handleLogin } = useAuth();

  // Handle form submission
  const onSubmit = async (data) => {
    await handleLogin(data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div>
        <label htmlFor="username">Username (Email)</label>
        <input type="text" id="username" name="username" ref={register} />
        {errors.username && <p>{errors.username.message}</p>}
      </div>
      <div>
        <label htmlFor="password">Password</label>
        <input type="password" id="password" name="password" ref={register} />
        {errors.password && <p>{errors.password.message}</p>}
      </div>
      <button type="submit">Login</button>
    </form>
  );
};

export default LoginForm;
```


## Conclusion

**Best Implementation:** **Amazon Q**'s solution, despite the authentication error, provides a comprehensive approach covering all aspects of the prompt in detail. It demonstrates practical session management, form processing, and basic testing, aligning well with real-world application requirements.

**Worst Implementation:** **GitHub Copilot**'s submission lacks critical implementation details essential for meeting the project's requirements. This makes it less practical for developers needing a more guided and detailed approach to setting up all aspects of a Next.js project.