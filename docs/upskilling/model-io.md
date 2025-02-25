# Model I/O

![Model I/O](../img/model_io-1.jpeg)

There are two main types of models that LangChain integrates with: LLMs and Chat Models. These are defined by their input and output types.


## Prompts (format)

A prompt for a language model is a set of instructions or input provided by a user to guide the model's response, helping it understand the context and generate relevant and coherent language-based output, such as answering questions, completing sentences, or engaging in a conversation.

- **Definition**: A class used to manage and structure prompts, ensuring consistency and reusability.
- **Purpose**: Helps in creating standardized prompts that can be reused across different parts of an application.
- **Components**:

    - **Template**: The core structure of the prompt, often including placeholders for dynamic data.
    - **Inputs**: The variables or data points that will be filled into the placeholders in the template.
  
- **Examples**: 


  ```python hl_lines="5 6 7 8"
  # Python Example
  from langchain.prompts import PromptTemplate

  # Define a prompt template
  prompt_template = PromptTemplate(
      template="You are an expert assistant. Answer the following question in detail:\n\nQuestion: {question}\n\nAnswer:",
      input_variables=["question"],
  )

  ```

  ```js hl_lines="5 6 7 8"
  // JavaScript Example
  import { PromptTemplate } from "@langchain/core/prompts"

  // Define a prompt template
  const promptTemplate = new PromptTemplate({
    template: "You are an expert assistant. Answer the following question in detail:\n\nQuestion: {question}\n\nAnswer:",
    inputVariables: ["question"],
  })
 
  ```

## Chat models (predict)

A chat model is a language model that uses chat messages as inputs and returns chat messages as outputs (as opposed to using plain text).

LangChain has integrations with many model providers (OpenAI, Cohere, Hugging Face, etc.) and exposes a standard interface to interact with all of these models.

LangChain allows you to use models in sync, async, batching and streaming modes and provides other features (e.g., caching) and more.

**Definition**:

- Chat models are specialized language models designed to generate conversational responses, simulating human-like dialogue.

**Purpose**:

- The purpose of chat models is to engage in interactive communication, providing responses that are contextually relevant and coherent within a conversational flow.

**Components**:

1. **Dialogue History**: The sequence of previous exchanges between the user and the model.
2. **Context Management**: Mechanisms to maintain and reference context throughout the conversation.
3. **Response Generation**: Algorithms and methods used to produce the model's replies.
4. **User Input**: The input or query provided by the user in the conversation.

**Types**:

1. **Open-domain Chat Models**: Capable of discussing a wide range of topics without a specific focus.
2. **Task-oriented Chat Models**: Designed to accomplish specific tasks, such as booking a ticket or answering customer service queries.

- **Examples**: 


  ```python hl_lines="5"
  # Python Example
  from langchain_openai import ChatOpenAI

  # Define a chat model
  chat_model = ChatOpenAI(openai_api_key=your_openai_api_key)

  ```

  ```js hl_lines="5 6 7"
  // JavaScript Example
  import { ChatOpenAI } from "@langchain/openai";

  // Define a chat model
  const chatModel = new ChatOpenAI({
    apiKey: yourOpenAiApiKey,
  });
 
  ```

## LLMs (predict)

Large Language Models (LLMs) are a core component of LangChain. LangChain does not serve its own LLMs, but rather provides a standard interface for interacting with many different LLMs. To be specific, this interface is one that takes as input a string and returns a string.

There are lots of LLM providers (OpenAI, Cohere, Hugging Face, etc) - the LLM class is designed to provide a standard interface for all of them.

**Definition**:

- Large Language Models (LLMs) are extensive machine learning models trained on vast amounts of text data to understand and generate human-like text.

**Purpose**:

- The purpose of LLMs is to leverage their understanding of language to perform various tasks such as text generation, translation, summarization, and answering questions.

**Components**:

1. **Training Data**: The large corpus of text data used to train the model.
2. **Architecture**: The underlying structure of the model, such as transformer networks.
3. **Parameters**: The variables within the model that are learned during training.
4. **Inference Mechanism**: The process by which the model generates output based on input data.

**Types**:

1. **General-purpose LLMs**: Models like GPT-3 that can be adapted for a wide range of tasks.
2. **Domain-specific LLMs**: Models fine-tuned on specific domains like medical or legal text for specialized applications.
3. **Bilingual/Multilingual LLMs**: Models trained to understand and generate text in multiple languages.

- **Examples**: 

  ```python hl_lines="5"
  # Python Example
  from langchain_openai import OpenAI

  # Define a chat model
  llm = OpenAI(openai_api_key=your_openai_api_key)

  ```

  ```js hl_lines="5 6 7"
  // JavaScript Example
  import { OpenAI } from "@langchain/openai";

  // Define a chat model
  const llm = new OpenAI({
    apiKey: yourOpenAiApiKey,
  });
 
  ```


## Output Parsers (parse)

Output parsers are responsible for taking the output of an LLM and transforming it to a more suitable format. This is very useful when you are asking the LLM to generate any form of structured data.

Besides having a large collection of different types of output parsers, one distinguishing benefit of LangChain OutputParsers is that many of them support streaming.

Certainly! Here is the detailed breakdown for **Output Parsers** in LangChain, including their Definition, Purpose, Components, and Types:



**Definition**:

- Output parsers are tools that take the raw output generated by a language model (LLM) and transform it into a more structured and suitable format.

**Purpose**:

- The purpose of output parsers is to ensure that the output from an LLM can be easily consumed and utilized by other components or systems, especially when the output needs to be in a specific structured format.

**Components**:

1. **Parsing Logic**: The core logic that interprets and transforms the raw output into the desired format.
2. **Streaming Support**: The ability to process output incrementally as it is generated by the LLM, which is beneficial for handling large outputs or real-time data.
3. **Format Specification**: Definitions of the target format, such as JSON, XML, or custom data structures.
4. **Error Handling**: Mechanisms to handle and report errors during the parsing process.

**Types**:

1. **JSON Parsers**: Transform the output into JSON format, useful for APIs and data interchange.
2. **CSV Parsers**: Convert the output into CSV format, suitable for data analysis and spreadsheets.
3. **Custom Parsers**: Designed to transform the output into user-defined structures or formats.
4. **Streaming Parsers**: Handle the output in chunks as it is being generated, allowing for real-time processing and lower memory usage.


**Examples**: 


  ```python hl_lines="9 14 16"
  # Python Example

  from langchain.output_parsers import CommaSeparatedListOutputParser
  from langchain.prompts import PromptTemplate
  from langchain_openai import OpenAI

  llm = OpenAI(openai_api_key=your_openai_api_key)

  output_parser = CommaSeparatedListOutputParser()

  prompt = PromptTemplate(
      template="List 3 {things}.\n{format_instructions}",
      input_variables=["things"],
      partial_variables={"format_instructions": output_parser.get_format_instructions()})

  chain = prompt | llm | output_parser # RunnableSequence

  result = chain.invoke({"things": "sports that don't use balls"})

  print(result)
  ```

  ```js hl_lines="10 16 20"
  // JavaScript Example

  import { OpenAI } from "@langchain/openai";
  import { CommaSeparatedListOutputParser } from "langchain/output_parsers";
  import { PromptTemplate } from "@langchain/core/prompts"
  import { RunnableSequence } from "@langchain/core/runnables";

  const llm = new OpenAI({ openAIApiKey: yourOpenAiApiKy });

  const outputParser = new CommaSeparatedListOutputParser();

  const prompt = new PromptTemplate({
      template: "List 3 {things}",
      inputVariables: ["things"],
      partialVariables: {
          formatInstructions: outputParser.getFormatInstructions(),
      },
  });

  const chain = RunnableSequence.from([prompt, llm, outputParser]);

  const result = await chain.invoke({ things: "sports that don't use balls" });

  console.log(result);
  ```

 **Input**: 

  ```
  sports that don't use balls
  ```

 **Output**: 

  ```
  [ '1. Swimming\n2. Skateboarding\n3. Gymnastics' ]
  ```