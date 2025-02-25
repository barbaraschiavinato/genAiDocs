# Langchain main concepts

## Key Concepts and Components

### 1. Prompt Templates

**PromptTemplate**:

- **Definition**: A class used to manage and structure prompts, ensuring consistency and reusability.
- **Purpose**: Helps in creating standardized prompts that can be reused across different parts of an application.
- **Components**:

    - **Template**: The core structure of the prompt, often including placeholders for dynamic data.
    - **Inputs**: The variables or data points that will be filled into the placeholders in the template.
  
- **Examples**: 


  ```python
  # Python Example
  from langchain.prompts import PromptTemplate

  # Define a prompt template
  prompt_template = PromptTemplate(
      template="You are an expert assistant. Answer the following question in detail:\n\nQuestion: {question}\n\nAnswer:",
      input_variables=["question"],
  )

  ```

  ```js
  // JavaScript Example
  import { PromptTemplate } from "@langchain/core/prompts"

  // Define a prompt template
  const promptTemplate = new PromptTemplate({
    template: "You are an expert assistant. Answer the following question in detail:\n\nQuestion: {question}\n\nAnswer:",
    inputVariables: ["question"],
  })
 
  ```

### 2. Chains

**Chains**:

- **Definition**: Sequences of operations where the output of one step serves as the input for the next.
- **Types**:

    - **Simple Chains**: Involve a single call to a language model.
    - **Complex Chains**: Involve multiple steps and can include logic and decision-making.

- **Components**:
  
    - **Links**: Individual steps or operations in the chain.
    - **Flow Control**: Logic that dictates the order and conditions under which steps are executed.

- **Examples**: A chain that first translates text and then summarizes it.


  ```python
  # Python Example
  from langchain.chat_models import ChatOpenAI
  from langchain.chains import LLMChain

  # Initialize the OpenAI model
  chat_model = ChatOpenAI(openai_api_key=your_openai_api_key)

  llm_chain = LLMChain(
    llm=chat_model,
    prompt=prompt_template
  )

  # Create a chain with the model and the prompt template (previous example)
  llm_chain = LLMChain(
    llm=chat_model,
    prompt=prompt_template
  )

  # Define the user's question
  question = "What are the key benefits of using blockchain technology in supply chain management?"

  # Generate a response using the chain
  response = llm_chain.invoke({"question": question})

  print(response["text"])


  ```

  ```js
  import { ChatOpenAI } from "@langchain/openai";
  import { LLMChain } from "langchain/chains";

  // Initialize the OpenAI model
  const chatModel = new ChatOpenAI({
    openAIApiKey: yourOpenAIApiKey,
  });

  // Create a chain with the model and the prompt template (previous example)
  const llmChain = new LLMChain({
    llm: chatModel,
    prompt: promptTemplate,
  });

  // Define the user's question
  const question = 'What are the key benefits of using blockchain technology in supply chain management?';

  // Generate a response using the chain
  llmChain.invoke({ question }).then((response) => {
    console.log(response.text);
  }).catch((error) => {
    console.error('Error generating response:', error);
  });
  ```


### 3. Agents

**Agents**:

- **Definition**: Autonomous entities that use LLMs to make decisions and perform tasks.
- **Types**:

    - **Action Agents**: Execute specific actions based on model outputs.
    - **Planning Agents**: Create plans or sequences of actions to achieve a goal.

- **Components**:

    - **Toolkits**: Collections of tools or APIs that agents can use.
    - **Memory**: Mechanisms for maintaining context or state across interactions.

- **Examples**: A virtual assistant that schedules meetings based on user input.

  ```python
  # Python Example
  from langchain.agents import initialize_agent, load_tools, AgentType
  from langchain.chat_models import ChatOpenAI
  from langchain.tools import Tool

  # Initialize the OpenAI model
  chat_model = ChatOpenAI(openai_api_key=your_openai_api_key)

  # Define a simple function to be triggered by the agent
  def greet(name):
      return f"Hello, {name}!"

  # Wrap the function in a Tool
  greet_tool = Tool(
      name="greet",
      func=greet,
      description="Greets the user with their name. Use this tool when the input starts with 'greet <name>'."
  )

  # Load tools (in this case, only the greet tool)
  tools = [greet_tool]

  # Initialize the agent with the chat model and the tools
  agent = initialize_agent(
      tools=tools,
      llm=chat_model,
      agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
      verbose=True
  )

  # Define the user input
  input_text = "greet John"

  # Use the agent to process the input and perform actions
  response = agent.run(input_text)

  # Print the response
  print("Agent Response:")
  print(response)

  ```


  ```js
  // JavaScript Example
  import { LLMChain } from "langchain/chains";
  import { AgentExecutor } from "langchain/agents"
  import { ChatOpenAI } from "@langchain/openai";
  import { PromptTemplate } from "@langchain/core/prompts"


  // Load environment variables from .env file
  dotenv.config();

  // Initialize the OpenAI model
  const chatModel = new ChatOpenAI({
    openAIApiKey: yourOpenAIApiKey,
  });

  // Define a simple function to be triggered by the agent
  function greet(name) {
    return `Hello, ${name}!`;
  }

  // Define a prompt template for decision making
  const promptTemplate = new PromptTemplate({
    inputVariables: ['input'],
    template: 'You are a smart assistant. Decide whether to greet the user based on the input. If the input starts with "greet", call the greet function with the user\'s name. Otherwise, respond with a polite message.\n\nInput: {input}',
  });

  // Create a chain with the model and the prompt template
  const decisionChain = new LLMChain({
    llm: chatModel,
    prompt: promptTemplate,
  });

  // Define the input
  const inputText = 'greet John';

  // Use the decision chain to process the input and get a decision
  decisionChain.invoke({ input: inputText }).then((decisionResponse) => {
    const decision = decisionResponse.text.trim();

    if (decision.toLowerCase().includes('greet')) {
      const name = inputText.split(' ')[1];
      const result = greet(name);
      console.log('Result:');
      console.log(result);
    } else {
      console.log('Response:');
      console.log(decision);
    }
  }).catch((error) => {
    console.error('Error generating decision:', error);
  });

  ```

### 4. Memory

**Memory**:

- **Definition**: Components that allow models to maintain state or context over a series of interactions.
- **Types**:

    - **Short-term Memory**: Context retained for a single interaction or session.
    - **Long-term Memory**: Persistent storage of information across multiple sessions.

- **Examples**:
    - **Short-term Memory**: Used in a conversation to remember the last user query.
      ```python
      short_term_memory = "Last query was about weather."
      ```
    - **Long-term Memory**: Used to store user preferences for future interactions.
      ```python
      long_term_memory = {"user_preferences": {"language": "French"}}
      ```

  ```js
  // JavaScript Example
  class ChatMemory {
      constructor() {
          this.shortTermMemory = "";
          this.longTermMemory = {};
      }

      rememberShortTerm(context) {
          this.shortTermMemory = context;
      }

      rememberLongTerm(key, value) {
          this.longTermMemory[key] = value;
      }

      recallShortTerm() {
          return this.shortTermMemory;
      }

      recallLongTerm(key) {
          return this.longTermMemory[key];
      }
  }

  const memory = new ChatMemory();
  memory.rememberShortTerm("Last query was about weather.");
  memory.rememberLongTerm("user_preferences", { language: "French" });
  console.log(memory.recallShortTerm()); // Last query was about weather.
  console.log(memory.recallLongTerm("user_preferences")); // { language: "French" }
  ```

### 5. Embeddings

**Embeddings**:

- **Definition**: Dense vector representations of data that capture semantic meanings in a high-dimensional space.
- **Purpose**: Facilitate tasks like semantic search, clustering, and similarity detection by representing text or other data in a numerical format that preserves semantic relationships.

- **Types**:
    - **Word Embeddings**: Represent individual words.
    - **Sentence Embeddings**: Represent entire sentences or paragraphs.
    - **Document Embeddings**: Represent larger blocks of text, like documents or articles.

- **Applications**:

    - **Semantic Search**: Finding semantically similar documents or snippets.
    - **Clustering**: Grouping similar items together.
    - **Similarity Detection**: Measuring how similar two pieces of data are.

- **Examples**:

  ```python
  # Python Example
  from sentence_transformers import SentenceTransformer
  model = SentenceTransformer('distilbert-base-nli-mean-tokens')
  embeddings = model.encode(["Hello, how are you?", "Hi, what's up?"])
  ```

  ```js
  // JavaScript Example
  const sentenceBert = require('sentence-transformers');

  async function getEmbeddings(texts) {
      const model = new sentenceBert.SentenceTransformer('distilbert-base-nli-mean-tokens');
      const embeddings = await model.encode(texts);
      return embeddings;
  }

  getEmbeddings(["Hello, how are you?", "Hi, what's up?"]).then(console.log);
  ```


### 6. Vector Stores

**Vector Stores**:

- **Definition**: Databases or storage systems specifically designed to store and retrieve high-dimensional vectors (embeddings).
- **Purpose**: Enable efficient storage, indexing, and querying of vector data, facilitating tasks like nearest neighbor search and clustering.
- **Components**:

    - **Indexing**: Methods to efficiently index vector data for fast retrieval.
    - **Querying**: Mechanisms to query the stored vectors and retrieve the most relevant results.

- **Applications**:

    - **Semantic Search**: Quickly finding the most relevant documents or data points based on semantic similarity.
    - **Recommendation Systems**: Suggesting items that are similar to a given query.

- **Examples**:


  ```python
  # Python Example
  from faiss import IndexFlatL2
  import numpy as np

  # Create a vector store
  vector_store = IndexFlatL2(768)  # 768 is the dimensionality of embeddings
  # Add vectors to the store
  vectors = np.array(embeddings, dtype=np.float32)
  vector_store.add(vectors)
  # Query the store
  D, I = vector_store.search(np.array([query_vector], dtype=np.float32), k=5)
  ```

  ```js
  // JavaScript Example
  const faiss = require('faiss');

  async function createVectorStore(embeddings) {
      const dimension = embeddings[0].length;
      const vectorStore = new faiss.IndexFlatL2(dimension);
      vectorStore.add(embeddings);
      return vectorStore;
  }

  async function queryVectorStore(vectorStore, queryEmbedding, k = 5) {
      const D, I = vectorStore.search(queryEmbedding, k);
      return { distances: D, indices: I };
  }

  (async () => {
      const embeddings = await getEmbeddings(["Hello, how are you?", "Hi, what's up?"]);
      const vectorStore = await createVectorStore(embeddings);
      const queryEmbedding = await getEmbeddings(["Hello!"]);
      const result = await queryVectorStore(vectorStore, queryEmbedding);
      console.log(result);
  })();
  ```

### 7. Indexes

**Indexes**:

- **Definition**: Structures that enable efficient retrieval of information relevant to user queries.
- **Types**:

    - **Document Indexes**: Organize and search large collections of text or data.
    - **Embedding-based Indexes**: Use vector representations of text for semantic search and retrieval.

- **Components**:

    - **Indexing**: The process of creating indexes from data.
    - **Searching**: Retrieving relevant information from indexes based on queries.

- **Examples**:


  ```python
  # Python Example
  document_index = create_document_index(docs)
  search_results = search_document_index(document_index, query)
  ```

  ```js
  // JavaScript Example
  const elasticlunr = require('elasticlunr');

  function createDocumentIndex(docs) {
      const index = elasticlunr(function () {
          this.addField('content');
          this.setRef('id');
      });

      docs.forEach((doc, id) => {
          index.addDoc({ id, content: doc });
      });

      return index;
  }

  function searchDocumentIndex(index, query) {
      return index.search(query, {
          fields: {
              content: { boost: 1 }
          }
      });
  }

  const docs = ["Hello, how are you?", "Hi, what's up?"];
  const documentIndex = createDocumentIndex(docs);
  const searchResults = searchDocumentIndex(documentIndex, "Hello");
  console.log(searchResults);
  ```

### 8. Callbacks

**Callbacks**:

- **Definition**: Mechanisms that allow developers to hook into various stages of the chain execution process.
- **Uses**:

    - **Logging**: Recording information about the execution process.
    - **Monitoring**: Observing the performance and behavior of the system.
    - **Modifying Behavior**: Dynamically changing the execution based on certain conditions.

- **Examples**:


  ```python
  # Python Example
  def log_callback(step, result):
      print(f"Step {step}: {result}")

  chain.add_callback(log_callback)
  ```

  ```js
  // JavaScript Example
  function logCallback(step, result) {
      console.log(`Step ${step}: ${result}`);
  }

  ```
