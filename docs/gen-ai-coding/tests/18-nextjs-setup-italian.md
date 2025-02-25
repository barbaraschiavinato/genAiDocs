# 17. NextJs project setup - Italian prompt

## Prompt

Puoi impostare un progetto che soddisfi queste caratteristiche (fornendo il codice):

1. utilizzando NextJs
2. essere protetto dall'autenticazione Microsoft OAuth 2.0
3. usa Bootstrap come framework CSS
4. contenere un modulo con nome utente (e-mail) e password obbligatori, entrambi con convalida in linea
5. essere conforme alle WCAG
6. aggiungi il test Jest

notes: 

1. the example is the same of the previous example, only translated in Italian
2. I tried also Chinese prompt and the results are consistent with the Italian test
3. for point 2 I deliberately used the wrong name (Microsoft Azure authentication exists, not just Microsoft)

## Results

### Amazon Q

I apologize, but your request seems to be outside my domain of expertise. However, I'm happy to try discussing related topics that I may have more information on. How can I help further our conversation productively?

### GitHub Copilot


```bash
# 1. Crea un nuovo progetto Next.js
npx create-next-app@latest

# 2. Installa le dipendenze per l'autenticazione Microsoft OAuth 2.0
npm install next-auth
npm install @types/next-auth --save-dev

# 3. Installa e configura Bootstrap
npm install bootstrap
# Aggiungi import 'bootstrap/dist/css/bootstrap.css' nel file _app.js

# 4. Crea un modulo di accesso con validazione
# Questo sarà fatto nel codice JavaScript/TypeScript, non è un comando da terminale

# 5. Assicurati che il tuo sito sia conforme alle WCAG
# Questo richiede una revisione del codice e del design, non è un comando da terminale

# 6. Configura Jest per i test
npm install --save-dev jest
```

Per l'autenticazione Microsoft OAuth 2.0, dovrai creare un file `[...nextauth].js` nella directory `pages/api/auth` del tuo progetto. All'interno di questo file, dovrai configurare NextAuth per utilizzare Microsoft come provider.

Per il modulo di accesso con validazione, dovrai creare un componente React con due campi di input (per l'e-mail e la password) e utilizzare lo stato e gli eventi di React per gestire e validare l'input dell'utente.

Per la conformità WCAG, dovrai seguire le linee guida WCAG durante lo sviluppo del tuo sito. Potrebbe essere utile utilizzare strumenti come l'estensione Accessibility Insights for Web di Chrome per aiutarti a identificare eventuali problemi di accessibilità.

Infine, per configurare Jest, dovrai creare un file di configurazione Jest (ad esempio, `jest.config.js`) nel tuo progetto e scrivere test per il tuo codice.

### Axet Gaia


```javascript
// Import required modules
import React, { useState } from 'react';
import { useRouter } from 'next/router';
import { Form, Button } from 'react-bootstrap';

// Define the component
const LoginForm = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const router = useRouter();

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    // Perform authentication logic using Microsoft OAuth 2.0
    // ...

    // Redirect to the desired page after successful authentication
    router.push('/dashboard');
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group controlId="formUsername">
        <Form.Label>Email</Form.Label>
        <Form.Control
          type="email"
          placeholder="Enter email"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <Form.Control.Feedback type="invalid">
          Please enter a valid email.
        </Form.Control.Feedback>
      </Form.Group>

      <Form.Group controlId="formPassword">
        <Form.Label>Password</Form.Label>
        <Form.Control
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <Form.Control.Feedback type="invalid">
          Please enter a password.
        </Form.Control.Feedback>
      </Form.Group>

      <Button variant="primary" type="submit">
        Submit
      </Button>
    </Form>
  );
};

export default LoginForm;
```

This code sets up a login form component using Next.js and React. It includes form fields for email and password, with inline validation using the `required` attribute. The form submission is handled by the `handleSubmit` function, where you can perform the authentication logic using Microsoft OAuth 2.0. After successful authentication, the user is redirected to the `/dashboard` page.

To ensure WCAG compliance, you can add appropriate accessibility attributes to the form elements and ensure proper contrast and keyboard navigation. Additionally, you can write Jest tests to cover the functionality of this component.

Please note that this code is just a starting point and may require additional configuration and implementation depending on your specific project setup and requirements.

### ChatGpt 4

Per iniziare un progetto con le caratteristiche che hai descritto, posso guidarti passo dopo passo per configurare un ambiente di sviluppo utilizzando Next.js, Microsoft OAuth 2.0 per l'autenticazione, Bootstrap per il CSS, un modulo di accesso con validazione, conformità alle WCAG e test con Jest. Ecco una panoramica dettagliata su come procedere:

**1. Impostare l'ambiente di sviluppo Next.js**

Prima di tutto, assicurati di avere Node.js installato. Poi crea un nuovo progetto Next.js:

```bash
npx create-next-app nome-progetto
cd nome-progetto
```

**2. Installare Bootstrap**

Installa Bootstrap per gestire il CSS:

```bash
npm install bootstrap
```

Dopo l'installazione, importa Bootstrap nel tuo file `_app.js` per usarlo globalmente:

```javascript
import 'bootstrap/dist/css/bootstrap.min.css';
```

**3. Configurare l'autenticazione Microsoft OAuth 2.0**

Per integrare l'autenticazione Microsoft, puoi usare `next-auth`. Installa `next-auth` e una libreria per i client OAuth:

```bash
npm install next-auth @next-auth/microsoft-provider
```

Configura `next-auth` creando un file ` [...nextauth].js` dentro la cartella `pages/api/auth` e configuralo con le tue credenziali OAuth di Microsoft:

```javascript
import NextAuth from "next-auth"
import MicrosoftProvider from "next-auth/providers/microsoft"

export default NextAuth({
  providers: [
    MicrosoftProvider({
      clientId: process.env.MICROSOFT_CLIENT_ID,
      clientSecret: process.env.MICROSOFT_CLIENT_SECRET
    })
  ],
})
```

**4. Creare un modulo di accesso**

Crea un modulo in una nuova pagina, per esempio `pages/login.js`. Assicurati che il modulo abbia la validazione in linea e sia conforme alle WCAG:

```javascript
import { useState } from 'react';
import { signIn } from 'next-auth/react';

function LoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [errors, setErrors] = useState({ username: '', password: '' });

  const validateForm = () => {
    let valid = true;
    if (!username.includes('@')) {
      setErrors(prev => ({ ...prev, username: 'Inserisci un'email valida.' }));
      valid = false;
    }
    if (password.length < 8) {
      setErrors(prev => ({ ...prev, password: 'La password deve essere di almeno 8 caratteri.' }));
      valid = false;
    }
    return valid;
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (validateForm()) {
      // Implementa la logica di autenticazione qui
      signIn('microsoft', { username, password });
    }
  };

  return (
    <div className="container mt-5">
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Email</label>
          <input type="email" className="form-control" value={username} onChange={e => setUsername(e.target.value)} />
          {errors.username && <div className="alert alert-danger">{errors.username}</div>}
        </div>
        <div className="form-group">
          <label>Password</label>
          <input type="password" className="form-control" value={password} onChange={e => setPassword(e.target.value)} />
          {errors.password && <div className="alert alert-danger">{errors.password}</div>}
        </div>
        <button type="submit" className="btn btn-primary">Login</button>
      </form>
    </div>
  );
}

export default LoginPage;
```

**5. Aggiungere Jest per i test**

Installazione di Jest e delle sue dipendenze per il testing:

```bash
npm install jest @testing-library/react @testing-library/jest-dom babel-jest
```

Configura Jest aggiungendo la seguente configurazione nel tuo `package.json`:

```json
"jest": {
  "setupFilesAfterEnv": ["<rootDir>/jest.setup.js"],
  "testPathIgnorePatterns": ["<rootDir>/.next/", "<rootDir>/node_modules/"],
  "moduleNameMapper": {
    "\\.(css|less|scss|sass)$": "identity-obj-proxy"
  }
}
```

Crea un file `jest.setup.js` nella radice del tuo progetto per configurare il testing library:

```javascript
import '@testing-library/jest-dom';
```

Puoi ora scrivere i test dentro una cartella `__tests__` nella radice del tuo progetto.


### Meta.ai

Here is an example project that meets the requirements you specified:

**Project Structure**

```
components
Login.js
...
pages
index.js
...
public
...
styles
bootstrap.min.css
...
utils
auth.js
...
jest.config.js
next.config.js
package.json
```

**components/Login.js**

```jsx
import React, { useState } from 'react';
import { useAuth } from '../utils/auth';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const { login } = useAuth();

  const handleSubmit = (event) => {
    event.preventDefault();
    login(email, password);
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="form-group">
        <label htmlFor="email">Email</label>
        <input
          type="email"
          value={email}
          onChange={(event) => setEmail(event.target.value)}
          required
          aria-required="true"
        />
      </div>
      <div className="form-group">
        <label htmlFor="password">Password</label>
        <input
          type="password"
          value={password}
          onChange={(event) => setPassword(event.target.value)}
          required
          aria-required="true"
        />
      </div>
      <button type="submit">Login</button>
    </form>
  );
};

export default Login;
```

**utils/auth.js**

```js
import axios from 'axios';

const auth = {
  login: async (email, password) => {
    try {
      const response = await axios.post('(link unavailable)', {
        grant_type: 'password',
        client_id: '{clientId}',
        client_secret: '{clientSecret}',
        username: email,
        password: password,
        scope: '(link unavailable)',
      });
      const accessToken = response.data.access_token;
      // Store access token in session or cookie
      return accessToken;
    } catch (error) {
      console.error(error);
    }
  },
};

export default auth;
```

**next.config.js**

```js
module.exports = {
  //...
  plugins: [
    {
      src: 'utils/auth',
      async headers() {
        return [
          {
            source: '/login',
            headers: [
              {
                key: 'Authorization',
                value: 'Bearer ' + (await auth.login()),
              },
            ],
          },
        ];
      },
    },
  ],
};
```

**jest.config.js**

```js
module.exports = {
  preset: 'ts-jest',
  collectCoverage: true,
  coverageDirectory: 'coverage',
  setupFilesAfterEnv: ['<rootDir>/setupTests.ts'],
  transform: {
    '^.+\\.(js|jsx|ts|tsx)$': 'babel-jest',
  },
  moduleNameMapper: {
    '^~/(.*)$': '<rootDir>/src/$1',
  },
};
```

I am still improving my command of non-English languages, and I may make errors while attempting them. I will be most useful to you if I can assist you in English.

### Gemini


**Requisiti:**

* Node.js installato
* npm o yarn installato
* Account Microsoft Azure Active Directory (AAD)

**Creazione del progetto:**

1. Creare una nuova directory per il progetto e spostarsi al suo interno:

```bash
mkdir progetto-nextjs-auth
cd progetto-nextjs-auth
```

2. Iniziare un nuovo progetto Next.js con autenticazione Microsoft OAuth 2.0:

```bash
npx create-next-app --auth Microsoft
```

3. Installare Bootstrap:

```bash
npm install bootstrap
```

**Implementazione del modulo di login:**

1. Creare un nuovo file `components/LoginForm.js` per il modulo di login:

```jsx
import React, { useState } from 'react';
import { Form, FormGroup, Label, Input, Button } from 'react-bootstrap';

const LoginForm = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errors, setErrors] = useState({});

  const handleSubmit = (event) => {
    event.preventDefault();

    const isValid = validateForm();
    if (!isValid) {
      return;
    }

    // Invia i dati di login al server qui

    console.log('Invio dati di login:', { email, password });
  };

  const validateForm = () => {
    const newErrors = {};

    if (!email) {
      newErrors.email = 'Inserire un indirizzo e-mail';
    }

    if (!password) {
      newErrors.password = 'Inserire una password';
    }

    setErrors(newErrors);
    return !Object.keys(newErrors).length;
  };

  return (
    <Form onSubmit={handleSubmit}>
      <FormGroup controlId="formEmail">
        <Label>Indirizzo e-mail</Label>
        <Input type="email" value={email} onChange={(e) => setEmail(e.target.value)} isInvalid={errors.email} />
        <Form.Control.Feedback type="invalid">{errors.email}</Form.Control.Feedback>
      </FormGroup>

      <FormGroup controlId="formPassword">
        <Label>Password</Label>
        <Input type="password" value={password} onChange={(e) => setPassword(e.target.value)} isInvalid={errors.password} />
        <Form.Control.Feedback type="invalid">{errors.password}</Form.Control.Feedback>
      </FormGroup>

      <Button variant="primary" type="submit">Accedi</Button>
    </Form>
  );
};

export default LoginForm;
```

2. Importare il componente `LoginForm` e utilizzarlo nella pagina principale (`pages/index.js`):

```jsx
import React from 'react';
import LoginForm from '../components/LoginForm';

const Home = () => {
  return (
    <div className="container">
      <h1>Login</h1>
      <LoginForm />
    </div>
  );
};

export default Home;
```

**Accessibilità WCAG:**

* Assicurarsi che il modulo di login abbia etichette chiare e descrittive per ogni campo di input.
* Utilizzare `aria-label` per fornire testo alternativo per elementi con immagini o icone.
* Aggiungere attributi `role` appropriati agli elementi del modulo.
* Fornire feedback appropriato agli utenti in caso di errori di input.
* Testare il modulo con strumenti di accessibilità per identificare e risolvere eventuali problemi.

**Test Jest:**

1. Installare Jest e i relativi moduli di mock:

```bash
npm install jest @testing-library/react @testing-library/jest-dom
```

2. Creare un nuovo file `components/LoginForm.test.js` per i test del componente `LoginForm`:

```jsx
// components/LoginForm.test.js

import React from 'react';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import LoginForm from './LoginForm';

jest.mock('react-bootstrap', () => ({
  Form: (props) => <form {...props} />,
  FormGroup: (props) => <div {...props} />,
  Label: (props) => <label {...props} />,
  Input: (props) => <input {...props} />,
  Button: (props) => <button {...props} />,
}));

describe('LoginForm component', () => {
  it('should render email and password inputs', () => {
    render(<LoginForm />);
    expect(screen.getByLabelText('Indirizzo e-mail')).toBeInTheDocument();
    expect(screen.getByLabelText('Password')).toBeInTheDocument();
  });

  it('should display error message for empty email', async () => {
    render(<LoginForm />);
    await userEvent.type(screen.getByLabelText('Password'), 'password123');
    await userEvent.click(screen.getByText('Accedi'));
    expect(screen.getByText('Inserire un indirizzo e-mail')).toBeInTheDocument();
  });

  it('should display error message for empty password', async () => {
    render(<LoginForm />);
    await userEvent.type(screen.getByLabelText('Indirizzo e-mail'), 'user@example.com');
    await userEvent.click(screen.getByText('Accedi'));
    expect(screen.getByText('Inserire una password')).toBeInTheDocument();
  });

});
```




## Analysis

### Amazon Q


**Pros:** - NA

**Cons:** - Amazon Q in IDE doesn't return any result asking in a language that isn't English.


### GitHub Copilot

**Pros:** - Instruction in Italian, as for the English version: simple, straightforward setup guide, easy to follow for initial project setup.

**Cons:** - As for the English version: lacks detailed code implementations for OAuth authentication and testing and requires additional customization.


### Axet Gaia

**Pros:** - As for the English version: Clean, well-structured code.

**Cons:** - Does not address authentication setup. - Misses implementation of testing. Despite they were present on the English version, the modern practices about form validation are comletelly missed.

Note: instructions and linline validation errors are in English, but by changing the interface in Italian, Gaia provides the correct translations.

### ChatGpt 4

**Pros:** - Instruction in Italian, as for the English version: extensive instructions and detailed code. - Thorough explanation of each integration step.

**Cons:** - Suggests a nonexistent Microsoft authentication provider. - Detailed steps might overwhelm beginners. Despite they were present on the English version, the modern practices about form validation are comletelly missed.


### Meta.ai

**Pros:** - Focuses on modular component design.

**Cons:** - Does not provide a solution for Microsoft authentication. - Fragmented setup requires additional configuration efforts. Despite they were present on the English version, the modern practices about form validation are comletelly missed.

Note: istructions are only in English, but right now Meta.ai is available on in US.


### Gemini

**Pros:** Instruction in Italian, Gemini provides a structured approach to project setup with clear steps, focusing on using modern tools and libraries like Microsoft Graph SDK. It offers a concise and clean implementation for setting up Microsoft Azure AD authentication and Bootstrap integration.

**Cons:** Despite they were present on the English version, the modern practices about form validation are comletelly missed.

Note: as general behaviour on Gemini sometimes doens't complete the example without any warning


## Conclusions

**Best Implementation:** Gemini

**Worst Implementation:** Amazon Q