# Retrieval

![Retrieval](../img/data_connection-1.jpeg)

Many LLM applications require user-specific data that is not part of the model's training set. The primary way of accomplishing this is through Retrieval Augmented Generation (RAG). In this process, external data is retrieved and then passed to the LLM when doing the generation step.

LangChain provides all the building blocks for RAG applications - from simple to complex. This section of the documentation covers everything related to the retrieval step - e.g. the fetching of the data. Although this sounds simple, it can be subtly complex. This encompasses several key modules.



## Document loaders (load)
Load data from a source as `Documents` for later processing

Use document loaders to load data from a source as Document's. A `Document` is a piece of text and associated metadata. For example, there are document loaders for loading a simple `.txt` file, for loading the text contents of any web page, or even for loading a transcript of a YouTube video.

Document loaders provide a "load" method for loading data as documents from a configured source. They optionally implement a "lazy load" as well for lazily loading data into memory.

**Definition**:

- Document loaders are tools used to load data from various sources into `Document` objects, which contain both text and associated metadata.

**Purpose**:

- The purpose of document loaders is to facilitate the extraction of text and metadata from different sources (e.g., files, web pages, YouTube transcripts) and structure them in a consistent format for further processing.

**Components**:

1. **Source**: The origin of the data (e.g., `.txt` files, web pages).
2. **Load Method**: A method to load data from the source into `Document` objects.
3. **Lazy Load Method**: An optional method for loading data into memory on demand.

**Types**:

1. **Text File Loaders**: Loaders for reading text from files.
2. **Web Page Loaders**: Loaders for extracting text from web pages.
3. **Transcript Loaders**: Loaders for fetching and parsing video transcripts.

```python hl_lines="5 6"
# Python example

from langchain_community.document_loaders import TextLoader

loader = TextLoader("./index.md")
docs = loader.load()

```

```js hl_lines="5 6"
// JavaScript Example

import { TextLoader } from "langchain/document_loaders/fs/text";

const loader = new TextLoader("./index.md");
const docs = await loader.load()

```


## Text splitters (transform)
Transform source documents to better suit your application

Once you've loaded documents, you'll often want to transform them to better suit your application. The simplest example is you may want to split a long document into smaller chunks that can fit into your model's context window. LangChain has a number of built-in document transformers that make it easy to split, combine, filter, and otherwise manipulate documents.

When you want to deal with long pieces of text, it is necessary to split up that text into chunks. As simple as this sounds, there is a lot of potential complexity here. Ideally, you want to keep the semantically related pieces of text together. What "semantically related" means could depend on the type of text. This notebook showcases several ways to do that.

At a high level, text splitters work as following:

1. Split the text up into small, semantically meaningful chunks (often sentences).
1. Start combining these small chunks into a larger chunk until you reach a certain size (as measured by some function).
1. Once you reach that size, make that chunk its own piece of text and then start creating a new chunk of text with some overlap (to keep context between chunks).
That means there are two different axes along which you can customize your text splitter:

1. How the text is split
1. How the chunk size is measured

**Definition**:

- Text splitters are tools that divide a large piece of text into smaller, semantically meaningful chunks.

**Purpose**:

- The purpose of text splitters is to ensure that the text can fit into a model's context window and to maintain the semantic integrity of the text chunks.

**Components**:

1. **Separator**: The character or pattern used to split the text.
2. **Chunk Size**: The maximum size of each chunk.
3. **Chunk Overlap**: The overlap between chunks to maintain context.
4. **Length Function**: A function to measure the size of each chunk.

**Types**:

1. **Character Text Splitters**: Split text based on character count.
2. **Sentence Text Splitters**: Split text based on sentence boundaries.
3. **Paragraph Text Splitters**: Split text based on paragraph breaks.

```python hl_lines="9 12"

# Python example
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader

# Initialize the document loader
loader = TextLoader("./index.md")

# Initialize the text splitter
text_splitter = CharacterTextSplitter(separator="\n", chunk_size=200, chunk_overlap=0)

# Load the documents and split them into chunks
docs = loader.load_and_split(text_splitter=text_splitter)

```


```js hl_lines="7 10 11 12 13 14 17"
// Javascript example

import { TextLoader } from "langchain/document_loaders/fs/text";
import { CharacterTextSplitter } from "langchain/text_splitter";

// Initialize the document loader
const loader = new TextLoader("index.md");

// Initialize the text splitter
const textSplitter = new CharacterTextSplitter({
  separator: "\n",
  chunk_size: 200,
  chunk_overlap: 0,
});

// Load the documents and split them into chunks
const docs = await loader.loadAndSplit(textSplitter)

```

## Embedding models (embed)
Create vector representations of a piece of text, allowing for natural language search


The Embeddings class is a class designed for interfacing with text embedding models. There are lots of embedding model providers (OpenAI, Cohere, Hugging Face, etc) - this class is designed to provide a standard interface for all of them.

Embeddings create a vector representation of a piece of text. This is useful because it means we can think about text in the vector space, and do things like semantic search where we look for pieces of text that are most similar in the vector space.

The base Embeddings class in LangChain provides two methods: one for embedding documents and one for embedding a query. The former takes as input multiple texts, while the latter takes a single text. The reason for having these as two separate methods is that some embedding providers have different embedding methods for documents (to be searched over) vs queries (the search query itself).

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
# Python example

from langchain_openai import OpenAIEmbeddings

embeddings_model = OpenAIEmbeddings(api_key=your_openai_api_key)

embeddings = embeddings_model.embed_documents(
    [
        "Hi there!",
        "Oh, hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!"
    ]
)
```
```js
// Javascript example

import { OpenAIEmbeddings } from "@langchain/openai";

const embeddingsModel = new OpenAIEmbeddings({ openAIApiKey: yourOpenAiApiKy });

const embedding = await embeddingsModel.embedDocuments([
    "Hi there!",
    "Oh, hello!",
    "What's your name?",
    "My friends call me World",
    "Hello World!"
])

```

## Vectorstores (store)
Interfaces for specialized databases that can search over unstructured data with natural language

One of the most common ways to store and search over unstructured data is to embed it and store the resulting embedding vectors, and then at query time to embed the unstructured query and retrieve the embedding vectors that are 'most similar' to the embedded query. A vector store takes care of storing embedded data and performing vector search for you.

- **Definition**: Databases or storage systems specifically designed to store and retrieve high-dimensional vectors (embeddings).
- **Purpose**: Enable efficient storage, indexing, and querying of vector data, facilitating tasks like nearest neighbor search and clustering.
- **Components**:

    - **Indexing**: Methods to efficiently index vector data for fast retrieval.
    - **Querying**: Mechanisms to query the stored vectors and retrieve the most relevant results.

- **Applications**:

    - **Semantic Search**: Quickly finding the most relevant documents or data points based on semantic similarity.
    - **Recommendation Systems**: Suggesting items that are similar to a given query.

- **Examples**:


```python hl_lines="21"
# Python example

from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# Initialize the document loader
loader = TextLoader("./index.md")

# Initialize the text splitter
text_splitter = CharacterTextSplitter(separator="\n", chunk_size=200, chunk_overlap=0)

# Load the documents and split them into chunks
docs = loader.load_and_split(text_splitter=text_splitter)

# Initialize the OpenAI embeddings
embeddings = OpenAIEmbeddings()

# Create the Chroma vector store
db = Chroma.from_documents(docs, embedding=embeddings, persist_directory="emb")

# Execute similarity search
result = db.similarity_search("What did the president say about Ketanji Brown Jackson")

print(result[0].page_content)


```


```js hl_lines="25 26 27"
// Javascript example

import { OpenAIEmbeddings } from "@langchain/openai";
import { TextLoader } from "langchain/document_loaders/fs/text";
import { CharacterTextSplitter } from "langchain/text_splitter";
import { Chroma } from "@langchain/community/vectorstores/chroma";

// Initialize the document loader
const loader = new TextLoader("index.md");

// Initialize the text splitter
const textSplitter = new CharacterTextSplitter({
    separator: "\n",
    chunk_size: 200,
    chunk_overlap: 0,
});

// Load the documents and split them into chunks
const docs = await loader.loadAndSplit(textSplitter)

// Initialize the OpenAI embeddings
const embeddings = new OpenAIEmbeddings({ openAIApiKey: yourOpenAiApiKy })

// Create the Chroma vector store
const db = await Chroma.fromDocuments(docs, embeddings, {
    collectionName: "emb",
});

// Execute similarity search
const result = await db.similaritySearch("What did the president say about Ketanji Brown Jackson")

console.log(result[0].pageContent)

```

## Retrievers (retrieve)
More generic interfaces that return documents given an unstructured query

A retriever is an interface that returns documents given an unstructured query. It is more general than a vector store. A retriever does not need to be able to store documents, only to return (or retrieve) them. Vector stores can be used as the backbone of a retriever, but there are other types of retrievers as well.

Retrievers accept a string `query` as input and return a list of `Document`'s as output.

**Definition**:

- Retrievers are interfaces that return documents given an unstructured query. They do not necessarily store documents but focus on retrieving relevant documents based on the query.

**Purpose**:

- The purpose of retrievers is to fetch documents that are most relevant to a user's query, enabling efficient information retrieval from a large corpus.

**Components**:

1. **Query Processing**: The mechanism to interpret and process the input query.
2. **Document Retrieval**: The method to retrieve documents that match the query criteria.
3. **Integration with Models**: Ability to work with language models to refine search results.

**Types**:

1. **Vector Store Retrievers**: Use vector embeddings to find semantically similar documents.
2. **Keyword-Based Retrievers**: Use keyword matching to find relevant documents.
3. **Hybrid Retrievers**: Combine multiple methods to improve retrieval accuracy.

```python hl_lines="24 25 26 29"
# Python example

from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# Initialize the document loader
loader = TextLoader("./facts.txt")

# Initialize the text splitter
text_splitter = CharacterTextSplitter(separator="\n", chunk_size=200, chunk_overlap=0)

# Load the documents and split them into chunks
docs = loader.load_and_split(text_splitter=text_splitter)

# Initialize the OpenAI embeddings
embeddings = OpenAIEmbeddings()

# Create the Chroma vector store
db = Chroma.from_documents(docs, embedding=embeddings, persist_directory="emb")

# Initialize the retriever
retriever = db.as_retriever(
    search_type="similarity_score_threshold", search_kwargs={"score_threshold": 0.5}
)

# Invoke the retriever
result = retriever.invoke("What did the president say about Ketanji Brown Jackson")

print(result[0].page_content)
```

```js hl_lines="31 32 33 34 38"
// Javascript example

import { OpenAIEmbeddings } from "@langchain/openai";
import { TextLoader } from "langchain/document_loaders/fs/text";
import { CharacterTextSplitter } from "langchain/text_splitter";
import { Chroma } from "@langchain/community/vectorstores/chroma";

// Initialize the document loader
const loader = new TextLoader("./facts.txt");

// Initialize the text splitter
const textSplitter = new CharacterTextSplitter({
    separator: "\n",
    chunk_size: 200,
    chunk_overlap: 0,
});

// Load the documents and split them into chunks
const docs = await loader.loadAndSplit(textSplitter)

// Initialize the OpenAI embeddings
const embeddings = new OpenAIEmbeddings({ openAIApiKey: yourOpenAiApiKy })

// Create the Chroma vector store
const db = await Chroma.fromDocuments(docs, embeddings, {
    collectionName: "emb",
});


// Initialize the retriever
const retriever = db.asRetriever({
    searchType: "similarity_score_threshold",
    searchKwargs: { scoreThreshold: 0.5 },
})


// Invoke the retriever
const result = await retriever.invoke("What did the president say about Ketanji Brown Jackson")

console.log(result[0].pageContent)

```

## Indexing (organize)

Here, we will look at a basic indexing workflow using the LangChain indexing API.

The indexing API lets you load and keep in sync documents from any source into a vector store. Specifically, it helps:

Avoid writing duplicated content into the vector store
Avoid re-writing unchanged content
Avoid re-computing embeddings over unchanged content
All of which should save you time and money, as well as improve your vector search results.

Crucially, the indexing API will work even with documents that have gone through several transformation steps (e.g., via text chunking) with respect to the original source documents.

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

from chromadb import PersistentClient
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain.indexes import SQLRecordManager, index
from langchain_community.vectorstores import Chroma

# Initialize the document loader
loader = TextLoader("./facts.txt")

# Initialize the text splitter
text_splitter = CharacterTextSplitter(separator="\n", chunk_size=200, chunk_overlap=0)

# Load the documents and split them into chunks
docs = loader.load_and_split(text_splitter=text_splitter)

# Initialize the OpenAI embeddings
embeddings = OpenAIEmbeddings()

# Create the Chroma vector store
chroma_client = PersistentClient()
db = Chroma(client=chroma_client, collection_name="vector_database", embedding_function=embeddings)

# Initialize the record manager
record_manager = SQLRecordManager(
    namespace="chroma/vector_database", db_url="sqlite:///record_manager.db"
)
record_manager.create_schema()

# Create the vector database function
def create_vector_db():
    info = index(
        docs_source=docs,
        record_manager=record_manager,
        vector_store=db,
        cleanup="incremental",
        source_id_key="source",
        batch_size=2
    )
    return info

# Clear the vector database function
def clear_database():
    info = index(
        docs_source=[],
        record_manager=record_manager,
        vector_store=db,
        cleanup="full",
        source_id_key="source"
    )
    return info


clear_info = clear_database()
create_info = create_vector_db()

# Print the information about the database
print(f"clear info: {clear_info}, create info: {create_info}")

```

```js

// Javascript example

import { OpenAIEmbeddings } from "@langchain/openai";
import { TextLoader } from "langchain/document_loaders/fs/text";
import { CharacterTextSplitter } from "langchain/text_splitter";
import { Chroma } from "@langchain/community/vectorstores/chroma";
import { index } from "langchain/indexes";
import { SQLiteRecordManager } from "@langchain/community/indexes/sqlite";

// Initialize the document loader
const loader = new TextLoader("./facts.txt");

// Initialize the text splitter
const textSplitter = new CharacterTextSplitter({
    separator: "\n",
    chunk_size: 200,
    chunk_overlap: 0,
});

// Load the documents and split them into chunks
const docs = await loader.loadAndSplit(textSplitter)

// Initialize the OpenAI embeddings
const embeddings = new OpenAIEmbeddings({ openAIApiKey: yourOpenAiApiKy })


// Create the Chroma vector store
const db = await Chroma.fromDocuments(docs, embeddings, {
    collectionName: "vector_database",
});

// Initialize the record manager
const recordManager = new SQLiteRecordManager(
    "vector_database",
    {
        localPath: ":memory:",
    }
)
recordManager.createSchema()


// Create the vector database function
function createVectorDb() {
    const info = index({
        docsSource: docs,
        recordManager: recordManager,
        vectorStore: db,
        cleanup: "incremental",
        sourceIdKey: "source",
        batchSize: 2
    })
    return info
}

// Clear the vector database function
function clearDatabase() {
    const info = index({
        docsSource: [],
        recordManager: recordManager,
        vectorStore: db,
        cleanup: "full",
        sourceIdKey: "source"
    })
    return info
}

const clearInfo = await clearDatabase()
const createInfo = await createVectorDb()

// Print the information about the database
console.log(`clear info: ${JSON.stringify(clearInfo)}, create info: ${JSON.stringify(createInfo)}`)


```

 **Output**: 

```
clear info: {'num_added': 0, 'num_updated': 0, 'num_skipped': 0, 'num_deleted': 54}, 
create info: {'num_added': 54, 'num_updated': 0, 'num_skipped': 0, 'num_deleted': 0}
```