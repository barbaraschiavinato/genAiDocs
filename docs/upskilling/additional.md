# More
## Memory
![Memory](../img/memory.png)
Most LLM applications have a conversational interface. An essential component of a conversation is being able to refer to information introduced earlier in the conversation. At bare minimum, a conversational system should be able to access some window of past messages directly. A more complex system will need to have a world model that it is constantly updating, which allows it to do things like maintain information about entities and their relationships.

- **Definition**: Components that allow models to maintain state or context over a series of interactions.
- **Types**:

    - **Short-term Memory**: Context retained for a single interaction or session.
    - **Long-term Memory**: Persistent storage of information across multiple sessions.

- **Examples**:

    ```python
    # Python Example

    from langchain.prompts import (
        HumanMessagePromptTemplate,
        ChatPromptTemplate,
        MessagesPlaceholder,
    )
    from langchain.chat_models import ChatOpenAI
    from langchain.chains import LLMChain
    from langchain.memory import (
        ConversationSummaryMemory,
    )

    chat = ChatOpenAI(openai_api_key=your_openai_api_key)


    prompt = ChatPromptTemplate(
        input_variables=["content"],
        messages=[
            MessagesPlaceholder(variable_name="chat_history"),  # The `variable_name` here is what must align with memory
            HumanMessagePromptTemplate.from_template("{content}"),
        ],
    )

    # Notice that `"chat_history"` aligns with the MessagesPlaceholder name.
    # Notice that we `return_messages=True` to fit into the MessagesPlaceholder
    # By using ConversationBufferMemory the full conversation is sent back, ConversationSummaryMemory reduces the amount of token needed
    memory = ConversationSummaryMemory(
        memory_key="chat_history",
        return_messages=True,
        llm=chat,
    )

    chain = LLMChain(llm=chat, prompt=prompt, memory=memory, verbose=False)

    def create_chat(content):
        result = chain.invoke({"content": content})
        return result["text"]

    ```

    ```js
    // JavaScript Example

    import {
        HumanMessagePromptTemplate,
        ChatPromptTemplate,
        MessagesPlaceholder,
    } from "@langchain/core/prompts";

    import { ChatOpenAI } from "@langchain/openai";
    import { LLMChain } from "langchain/chains";
    import { ConversationSummaryMemory } from "langchain/memory";


    const chat = new ChatOpenAI({
        openAIApiKey: yourOpenAiApiKey,
    });

    const prompt = ChatPromptTemplate.fromMessages([
        new MessagesPlaceholder("chat_history"), // The `variable_name` here is what must align with memory
        HumanMessagePromptTemplate.fromTemplate("{content}"),
    ]);

    // Notice that `"chat_history"` aligns with the MessagesPlaceholder name.
    // Notice that we `returnMessages=true` to fit into the MessagesPlaceholder
    // By using ConversationBufferMemory the full conversation is sent back, ConversationSummaryMemory reduces the amount of token needed
    const memory = new ConversationSummaryMemory({
        memoryKey: "chat_history",
        returnMessages: true,
        llm: chat,
    });

    const chain = new LLMChain({ llm: chat, prompt, memory, verbose: false });

    export async function createChat(text) {
        return await chain
            .invoke({ content: text })
            .then((finalResult) => {
                return finalResult.text;
            })
            .catch((error) => {
                return `error ${error}`;
            });
    }

    ```

## Callbacks
LangChain provides a callbacks system that allows you to hook into the various stages of your LLM application. This is useful for logging, monitoring, streaming, and other tasks.

You can subscribe to these events by using the callbacks argument available throughout the API. This argument is list of handler objects, which are expected to implement one or more of the methods described below in more detail.




- **Definition**: Mechanisms that allow developers to hook into various stages of the chain execution process.
- **Uses**:

    - **Logging**: Recording information about the execution process.
    - **Monitoring**: Observing the performance and behavior of the system.
    - **Modifying Behavior**: Dynamically changing the execution based on certain conditions.

- **Examples**:


```python
# Python Example

from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain.callbacks.base import BaseCallbackHandler


class MyCallbackHandler(BaseCallbackHandler):
    name = "MyCallbackHandler"

    def on_chain_start(self, serialized, inputs, **kwargs):
        print('========= Chain start =========\n')
        print(f'Input: {inputs}\n')

    def on_chain_end(self, outputs, **kwargs):
        print('========= Chain end =========\n')
        print(f'Output: {outputs}\n')

    def on_llm_start(self, _llm, prompt, **kwargs):
        print('========= LLM start =========\n')
        print(f'Template: "{prompt}"\n')


    def on_llm_end(self, output, **kwargs):
        print('========= LLM end =========\n')
        print(f'Output: {output}\n')


handler = MyCallbackHandler()
llm = OpenAI()
prompt = PromptTemplate.from_template("Return the value of the calculation: 1 + {number} = ")

chain = prompt | llm
chain.invoke({"number": 4}, {"callbacks": [handler]})
```

```js
// JavaScript Example
 
import { OpenAI } from "@langchain/openai";
import { PromptTemplate } from "@langchain/core/prompts"
import { RunnableSequence } from "@langchain/core/runnables";


class MyCallbackHandler {
    name = "MyCallbackHandler";
    async handleLLMStart(_llm, prompt) {
        console.log('========= LLM start =========\n');
        console.log(`Template: "${prompt}"\n`)
    }
    async handleLLMEnd(output) {
        console.log('========= LLM end =========\n');
        console.log(`Answer: ${output.generations[0][0].text}\n`)
    }

    async handleChainStart(_chain, input) {
        console.log('========= Chain start =========\n');
        console.log(`Input: ${JSON.stringify(input)}\n`)
    }
    async handleChainEnd(outputs) {
        console.log('========= Chain end =========\n');
        console.log(`Output: ${JSON.stringify(outputs)}\n`)
    }

}

const handler = new MyCallbackHandler();
const llm = new OpenAI({ temperature: 0, callbacks: [handler], openAIApiKey: yourOpenAiApiKy });
const promptTemplate = PromptTemplate.fromTemplate("Return the value of the calculation: 1 + {number} =");
const chain = RunnableSequence.from([promptTemplate, llm]);
await chain.invoke({ number: 4 }, { callbacks: [handler] });


```

**Output**: 

```
========= Chain start =========

Input: {'number': 4}

========= Chain end =========

Output: text='Return the value of the calculation: 1 + 4 = '

========= LLM start =========

Template: "['Return the value of the calculation: 1 + 4 = ']"

========= LLM end =========

Output: generations=[[Generation(text='5', generation_info={'finish_reason': 'stop', 'logprobs': None})]] llm_output={'token_usage': {'total_tokens': 15, 'completion_tokens': 1, 'prompt_tokens': 14}, 'model_name': 'gpt-3.5-turbo-instruct'} run=None

========= Chain end =========

Output: 5

```