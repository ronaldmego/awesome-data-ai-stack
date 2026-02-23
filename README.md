# Awesome Data & AI Stack [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of awesome Data, AI, and Agent tools — organized by agent anatomy and data stack layers. This collection represents real-world enterprise experience from deploying AI and data solutions at scale, with a unique perspective on the architectural patterns that actually work in production environments.

Unlike generic lists, this catalog focuses on the complete data-to-intelligence pipeline: from raw data ingestion through analytics, machine learning, and culminating in intelligent agents that can reason, act, and learn.

## Table of Contents

- [🤖 AI Agents & Frameworks](#-ai-agents--frameworks)
  - [💻 Vibe Coding & CLI Agents](#-vibe-coding--cli-agents)
  - [🔧 MCP Servers & Skills](#-mcp-servers--skills)
  - [🎯 Orchestration & Multi-Agent](#-orchestration--multi-agent)
  - [📝 Memory & RAG](#-memory--rag)
  - [💬 Conversational & Chat](#-conversational--chat)
  - [🌐 Browser & Web Agents](#-browser--web-agents)
  - [📚 Agent Resources & Guides](#-agent-resources--guides)
- [🎨 Avatar, Video & Image AI](#-avatar-video--image-ai)
- [📊 Data Engineering & Analytics](#-data-engineering--analytics)
- [🧠 ML & Data Science](#-ml--data-science)
- [🛠️ DevTools & Infrastructure](#️-devtools--infrastructure)
- [🌐 Web & Apps](#-web--apps)
- [📚 Learning & Reference](#-learning--reference)
- [🔍 OCR & Document Processing](#-ocr--document-processing)
- [📝 Content & Productivity](#-content--productivity)
- [Contributing](#contributing)
- [About](#about)

## 🤖 AI Agents & Frameworks

### 💻 Vibe Coding & CLI Agents

- [anthropics/claude-code](https://github.com/anthropics/claude-code) - Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster
- [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) - An open-source AI agent that brings the power of Gemini directly into your terminal
- [openai/codex](https://github.com/openai/codex) - Lightweight coding agent that runs in your terminal
- [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) - An open-source AI agent that lives in your terminal
- [bytedance/trae-agent](https://github.com/bytedance/trae-agent) - Trae Agent is an LLM-based agent for general purpose software engineering tasks
- [anomalyco/opencode](https://github.com/anomalyco/opencode) - The open source coding agent
- [HKUDS/DeepCode](https://github.com/HKUDS/DeepCode) - DeepCode: Open Agentic Coding (Paper2Code & Text2Web & Text2Backend)
- [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban) - Get 10X more out of Claude Code, Codex or any coding agent

### 🔧 MCP Servers & Skills

- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - A collection of MCP servers
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) - Model Context Protocol Servers
- [supabase-community/supabase-mcp](https://github.com/supabase-community/supabase-mcp) - Connect Supabase to your AI assistants
- [idosal/git-mcp](https://github.com/idosal/git-mcp) - Put an end to code hallucinations! GitMCP is a free, open-source, remote MCP server for any GitHub project
- [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) - A MCP for Claude Desktop / Claude Code / Windsurf / Cursor to build n8n workflows for you
- [firecrawl/firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server) - Official Firecrawl MCP Server - Adds powerful web scraping and search to Cursor, Claude and any other LLM clients
- [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox) - MCP Toolbox for Databases is an open source MCP server for databases
- [timescale/pg-aiguide](https://github.com/timescale/pg-aiguide) - MCP server and Claude plugin for Postgres skills and documentation
- [mongodb-js/mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server) - A Model Context Protocol server to connect to MongoDB databases and MongoDB Atlas Clusters
- [crystaldba/postgres-mcp](https://github.com/crystaldba/postgres-mcp) - Postgres MCP Pro provides configurable read/write access and performance analysis
- [leonardsellem/n8n-mcp-server](https://github.com/leonardsellem/n8n-mcp-server) - MCP server that provides tools and resources for interacting with n8n API
- [excalidraw/excalidraw-mcp](https://github.com/excalidraw/excalidraw-mcp) - Fast and streamable Excalidraw MCP App
- [upstash/context7](https://github.com/upstash/context7) - Context7 MCP Server -- Up-to-date code documentation for LLMs and AI code editors
- [mcp-use/mcp-use](https://github.com/mcp-use/mcp-use) - The fullstack MCP framework to develop MCP Apps for ChatGPT / Claude & MCP Servers for AI Agents
- [mindsdb/mindsdb](https://github.com/mindsdb/mindsdb) - Federated Query Engine for AI - The only MCP Server you'll ever need
- [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) - The fast, Pythonic way to build MCP servers and clients
- [coleam00/mcp-crawl4ai-rag](https://github.com/coleam00/mcp-crawl4ai-rag) - Web Crawling and RAG Capabilities for AI Agents and AI Coding Assistants
- [sadiuysal/crawl4ai-mcp-server](https://github.com/sadiuysal/crawl4ai-mcp-server) - A lightweight MCP server that exposes Crawl4AI web scraping capabilities
- [adhikasp/mcp-client-cli](https://github.com/adhikasp/mcp-client-cli) - A simple CLI to run LLM prompt and implement MCP client
- [adhikasp/mcp-git-ingest](https://github.com/adhikasp/mcp-git-ingest) - A MCP server that helps read GitHub repository structure and important files
- [antvis/mcp-server-chart](https://github.com/antvis/mcp-server-chart) - A visualization mcp & skills contains 25+ visual charts using @antvis
- [VikashLoomba/copilot-mcp](https://github.com/VikashLoomba/copilot-mcp) - A VSCode extension for finding and installing Agent Skills and MCP Apps
- [steipete/claude-code-mcp](https://github.com/steipete/claude-code-mcp) - Claude Code as one-shot MCP server to have an agent in your agent
- [supercorp-ai/supergateway](https://github.com/supercorp-ai/supergateway) - Run MCP stdio servers over SSE and SSE over stdio. AI gateway

### 🎯 Orchestration & Multi-Agent

- [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) - Framework for orchestrating role-playing, autonomous AI agents
- [langflow-ai/langflow](https://github.com/langflow-ai/langflow) - Langflow is a powerful tool for building and deploying AI-powered agents and workflows
- [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) - Build AI Agents, Visually
- [wshobson/agents](https://github.com/wshobson/agents) - Intelligent automation and multi-agent orchestration for Claude Code
- [The-Pocket/PocketFlow](https://github.com/The-Pocket/PocketFlow) - Pocket Flow: 100-line LLM framework. Let Agents build Agents!
- [MotiaDev/motia](https://github.com/MotiaDev/motia) - Multi-Language Backend Framework that unifies APIs, background jobs, queues, workflows, streams, and AI agents
- [simstudioai/sim](https://github.com/simstudioai/sim) - Build, deploy, and orchestrate AI agents. Sim is the central intelligence layer for your AI workforce
- [agno-agi/agno](https://github.com/agno-agi/agno) - The programming language for agentic software. Build, run, and manage multi-agent systems at scale
- [TransformerOptimus/SuperAGI](https://github.com/TransformerOptimus/SuperAGI) - A dev-first open source autonomous AI agent framework
- [Pythagora-io/gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) - The first real AI developer
- [Danau5tin/multi-agent-coding-system](https://github.com/Danau5tin/multi-agent-coding-system) - Reached #13 on Stanford's Terminal Bench leaderboard. Orchestrator, explorer & coder agents
- [docker/compose-for-agents](https://github.com/docker/compose-for-agents) - Build and run AI agents using Docker Compose
- [coleam00/ottomator-agents](https://github.com/coleam00/ottomator-agents) - All the open source AI Agents hosted on the oTTomator Live Agent Studio platform
- [coleam00/pydantic-ai-github-agent](https://github.com/coleam00/pydantic-ai-github-agent) - The agent built for AI Agents series on YouTube
- [coleam00/PydanticAI-Research-Agent](https://github.com/coleam00/PydanticAI-Research-Agent) - Pydantic AI Research Agent Built with the PRP Framework Template
- [kortix-ai/suna](https://github.com/kortix-ai/suna) - Kortix – build, manage and train AI Agents
- [The-Pocket/PocketFlow-Tutorial-Codebase-Knowledge](https://github.com/The-Pocket/PocketFlow-Tutorial-Codebase-Knowledge) - Pocket Flow: Codebase to Tutorial

### 📝 Memory & RAG

- [mem0ai/mem0](https://github.com/mem0ai/mem0) - Universal memory layer for AI Agents
- [getzep/graphiti](https://github.com/getzep/graphiti) - Build Real-Time Knowledge Graphs for AI Agents
- [topoteretes/cognee](https://github.com/topoteretes/cognee) - Knowledge Engine for AI Agent Memory in 6 lines of code
- [campfirein/cipher](https://github.com/campfirein/cipher) - Byterover Cipher is an opensource memory layer specifically designed for coding agents
- [infiniflow/ragflow](https://github.com/infiniflow/ragflow) - RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine
- [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) - RAG-Anything: All-in-One RAG Framework
- [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) - LightRAG: Simple and Fast Retrieval-Augmented Generation
- [raphaelmansuy/edgequake](https://github.com/raphaelmansuy/edgequake) - High-performance GraphRAG inspired from LightRag written in Rust
- [yichuan-w/LEANN](https://github.com/yichuan-w/LEANN) - RAG on Everything with LEANN. Enjoy 97% storage savings while running a fast, accurate, and 100% private RAG application
- [airweave-ai/airweave](https://github.com/airweave-ai/airweave) - Open-source context retrieval layer for AI agents

### 💬 Conversational & Chat

- [emcie-co/parlant](https://github.com/emcie-co/parlant) - LLM agents built for control. Designed for real-world use. Deployed in minutes
- [janhq/jan](https://github.com/janhq/jan) - Jan is an open source alternative to ChatGPT that runs 100% offline on your computer
- [openinterpreter/open-interpreter](https://github.com/openinterpreter/open-interpreter) - A natural language interface for computers
- [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) - The Frontend for Agents & Generative UI. React + Angular
- [ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui) - AG-UI: the Agent-User Interaction Protocol. Bring Agents into Frontend Applications
- [open-webui/open-webui](https://github.com/open-webui/open-webui) - User-friendly AI Interface (Supports Ollama, OpenAI API, ...)
- [Anything-LLM/anything-llm](https://github.com/Mintplex-Labs/anything-llm) - The all-in-one Desktop & Docker AI application with built-in RAG, AI agents
- [letta-ai/letta](https://github.com/letta-ai/letta) - Letta is the platform for building stateful agents: AI with advanced memory
- [Jackywine/Bella](https://github.com/Jackywine/Bella) - Bella is best
- [Doriandarko/kimi-writer](https://github.com/Doriandarko/kimi-writer) - AI writing agent powered by kimi-k2-thinking

### 🌐 Browser & Web Agents

- [browser-use/browser-use](https://github.com/browser-use/browser-use) - Make websites accessible for AI agents. Automate tasks online with ease
- [browserbase/stagehand](https://github.com/browserbase/stagehand) - The AI Browser Automation Framework
- [Fosowl/agenticSeek](https://github.com/Fosowl/agenticSeek) - Fully Local Manus AI. No APIs, No $200 monthly bills. Enjoy an autonomous agent that thinks, browses the web, and code
- [aaronjmars/opendia](https://github.com/aaronjmars/opendia) - Connect your browser to AI models. Just use Dia on Chrome, Arc or Firefox
- [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) - An autonomous agent that conducts deep research on any data using any LLM providers

### 📚 Agent Resources & Guides

- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - A curated list of awesome skills, hooks, slash-commands, agent orchestrators, applications, and plugins for Claude Code
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models
- [coleam00/context-engineering-intro](https://github.com/coleam00/context-engineering-intro) - Context engineering is the new vibe coding - it's the way to actually make AI coding assistants work
- [Cranot/claude-code-guide](https://github.com/Cranot/claude-code-guide) - The Complete Claude Code CLI Guide - Live & Auto-Updated Every 2 Days
- [coleam00/ai-agents-masterclass](https://github.com/coleam00/ai-agents-masterclass) - Follow along with my AI Agents Masterclass videos! All of the code I create and use in this series
- [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) - In-depth tutorials on LLMs, RAGs and real-world AI agent applications
- [SamurAIGPT/awesome-openclaw](https://github.com/SamurAIGPT/awesome-openclaw) - A curated list of awesome OpenClaw resources, tools, skills, tutorials, and articles
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) - A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows
- [BehiSecc/awesome-claude-skills](https://github.com/BehiSecc/awesome-claude-skills) - A curated list of Claude Skills
- [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) - A set of ready to use scientific skills for Claude
- [Kamalnrf/claude-plugins](https://github.com/Kamalnrf/claude-plugins) - Lightweight registry to discover, install, and manage all public Claude plugins and agent skills
- [anthropics/skills](https://github.com/anthropics/skills) - Public repository for Agent Skills
- [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) - Official, Anthropic-managed directory of high quality Claude Code Plugins
- [google-gemini/gemini-skills](https://github.com/google-gemini/gemini-skills) - Skills for the Gemini API, SDK and model/agent interactions
- [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) - CLI tool for configuring and monitoring Claude Code
- [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) - An AI-powered task-management system you can drop into Cursor, Lovable, Windsurf, Roo, and others
- [coleam00/Archon](https://github.com/coleam00/Archon) - Beta release of Archon OS - the knowledge and task management backbone for AI coding assistants
- [danielmiessler/Fabric](https://github.com/danielmiessler/Fabric) - Fabric is an open-source framework for augmenting humans using AI
- [openclaw/openclaw](https://github.com/openclaw/openclaw) - Your own personal AI assistant. Any OS. Any Platform. The lobster way

## 🎨 Avatar, Video & Image AI

- [jamiepine/voicebox](https://github.com/jamiepine/voicebox) - The open-source voice synthesis studio powered by Qwen3-TTS
- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) - The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface
- [ZeroLu/awesome-nanobanana-pro](https://github.com/ZeroLu/awesome-nanobanana-pro) - An awesome list of curated Nano Banana pro prompts and examples
- [PicoTrex/Awesome-Nano-Banana-images](https://github.com/PicoTrex/Awesome-Nano-Banana-images) - A curated collection of fun and creative examples generated with Nano Banana & Nano Banana Pro
- [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox) - SoTA open-source TTS
- [facefusion/facefusion-docker](https://github.com/facefusion/facefusion-docker) - Industry leading face manipulation platform
- [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) - Automate the process of making money online

## 📊 Data Engineering & Analytics

- [DataExpert-io/data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) - This is a repo with links to everything you'd ever want to learn about data engineering
- [dlt-hub/dlt](https://github.com/dlt-hub/dlt) - data load tool (dlt) is an open source Python library that makes data loading easy
- [igorbarinov/awesome-data-engineering](https://github.com/igorbarinov/awesome-data-engineering) - A curated list of data engineering tools for software developers
- [gunnarmorling/awesome-opensource-data-engineering](https://github.com/gunnarmorling/awesome-opensource-data-engineering) - An Awesome List of Open-Source Data Engineering Projects
- [Countly/countly-server](https://github.com/Countly/countly-server) - Countly is a privacy-first, AI-powered analytics and engagement platform
- [tensorlakeai/tensorlake](https://github.com/tensorlakeai/tensorlake) - Tensorlake is a Document Ingestion API and a serverless platform for building data processing
- [weaviate/elysia](https://github.com/weaviate/elysia) - Python package and backend for the Elysia platform app
- [mito-ds/mito](https://github.com/mito-ds/mito) - Jupyter extensions that help you write code faster: Context aware AI Chat, Autocomplete, and Spreadsheet
- [pixeltable/pixeltable](https://github.com/pixeltable/pixeltable) - Data Infrastructure providing a declarative, incremental approach for multimodal AI workloads
- [chartdb/chartdb](https://github.com/chartdb/chartdb) - Database diagrams editor that allows you to visualize and design your DB with a single query
- [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core) - dbt enables data analysts and engineers to transform their data using the same practices that software engineers use
- [valkey-io/valkey](https://github.com/valkey-io/valkey) - A flexible distributed key-value database that is optimized for caching and other realtime workloads
- [grafana/grafana](https://github.com/grafana/grafana) - The open and composable observability and data visualization platform
- [elastic/elasticsearch](https://github.com/elastic/elasticsearch) - Free and Open Source, Distributed, RESTful Search Engine
- [trinodb/trino](https://github.com/trinodb/trino) - Official repository of Trino, the distributed SQL query engine for big data
- [apache/superset](https://github.com/apache/superset) - Apache Superset is a Data Visualization and Data Exploration Platform
- [microsoft/data-formulator](https://github.com/microsoft/data-formulator) - Create rich visualizations with AI
- [vllm-project/vllm](https://github.com/vllm-project/vllm) - A high-throughput and memory-efficient inference and serving engine for LLMs
- [Openpanel-dev/openpanel](https://github.com/Openpanel-dev/openpanel) - OpenPanel is an open-source web and product analytics platform
- [Canner/WrenAI](https://github.com/Canner/WrenAI) - GenBI (Generative BI) queries any database in natural language, generates accurate SQL, charts
- [open-metadata/OpenMetadata](https://github.com/open-metadata/OpenMetadata) - OpenMetadata is a unified metadata platform for data discovery, data observability, and data governance
- [sinaptik-ai/pandas-ai](https://github.com/sinaptik-ai/pandas-ai) - Chat with your database or your datalake (SQL, CSV, parquet)
- [vanna-ai/vanna](https://github.com/vanna-ai/vanna) - Chat with your SQL database. Accurate Text-to-SQL Generation via LLMs using Agentic Retrieval
- [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) - Financial data platform for analysts, quants and AI agents
- [ganttrify](https://github.com/ganttrify/ganttrify) - Create beautiful Gantt charts with ggplot2
- [Avaiga/taipy](https://github.com/Avaiga/taipy) - Turns Data and AI algorithms into production-ready web applications in no time
- [mckinsey/vizro](https://github.com/mckinsey/vizro) - Vizro is a low-code toolkit for building high-quality data visualization apps

## 🧠 ML & Data Science

- [KalyanM45/AI-Project-Gallery](https://github.com/KalyanM45/AI-Project-Gallery) - Repository containing Artificial Intelligence Projects such as Machine Learning, Deep Learning and Generative AI
- [google/langextract](https://github.com/google/langextract) - A Python library for extracting structured information from unstructured text using LLMs
- [lyogavin/airllm](https://github.com/lyogavin/airllm) - AirLLM 70B inference with single 4GB GPU
- [ageron/handson-ml3](https://github.com/ageron/handson-ml3) - A series of Jupyter notebooks that walk you through the fundamentals of Machine Learning and Deep Learning
- [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) - DeepTutor: AI-Powered Personalized Learning Assistant
- [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners) - 10 Weeks, 20 Lessons, Data Science for All!
- [Sumanth077/ai-engineering-toolkit](https://github.com/Sumanth077/ai-engineering-toolkit) - A curated list of 100+ libraries and frameworks for AI engineers building with LLMs
- [microsoft/BitNet](https://github.com/microsoft/BitNet) - Official inference framework for 1-bit LLMs
- [cvs-health/uqlm](https://github.com/cvs-health/uqlm) - UQLM: Uncertainty Quantification for Language Models, is a Python package for UQ-based LLM hallucination detection
- [confident-ai/deepeval](https://github.com/confident-ai/deepeval) - The LLM Evaluation Framework
- [OpenBMB/MiniCPM-o](https://github.com/OpenBMB/MiniCPM-o) - A Gemini 2.5 Flash Level MLLM for Vision, Speech, and Full-Duplex Multimodal Live Streaming
- [mistralai/cookbook](https://github.com/mistralai/cookbook) - Mistral AI cookbook
- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) - All Algorithms implemented in Python
- [KalyanKS-NLP/llm-engineer-toolkit](https://github.com/KalyanKS-NLP/llm-engineer-toolkit) - A curated list of 120+ LLM libraries category wise
- [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) - The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data
- [academic/awesome-datascience](https://github.com/academic/awesome-datascience) - An awesome Data Science repository to learn and apply for real world problems
- [ujjwalkarn/Machine-Learning-Tutorials](https://github.com/ujjwalkarn/Machine-Learning-Tutorials) - machine learning and deep learning tutorials, articles and other resources
- [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) - 12 weeks, 26 lessons, 52 quizzes, classic Machine Learning for all
- [hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory) - Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)
- [Machine-Learning-Tokyo/Interactive_Tools](https://github.com/Machine-Learning-Tokyo/Interactive_Tools) - Interactive Tools for Machine Learning, Deep Learning and Math
- [rushter/MLAlgorithms](https://github.com/rushter/MLAlgorithms) - Minimal and clean examples of machine learning algorithms implementations
- [jivoi/awesome-ml-for-cybersecurity](https://github.com/jivoi/awesome-ml-for-cybersecurity) - Machine Learning for Cyber Security
- [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) - 21 Lessons, Get Started Building with Generative AI
- [roboticcam/machine-learning-notes](https://github.com/roboticcam/machine-learning-notes) - My continuously updated Machine Learning, Probabilistic Models and Deep Learning notes and demos
- [ml-tooling/ml-workspace](https://github.com/ml-tooling/ml-workspace) - All-in-one web-based IDE specialized for machine learning and data science
- [lukasmasuch/best-of-ml-python](https://github.com/lukasmasuch/best-of-ml-python) - A ranked list of awesome machine learning Python libraries. Updated weekly
- [d2l-ai/d2l-en](https://github.com/d2l-ai/d2l-en) - Interactive deep learning book with multi-framework code, math, and discussions
- [EthicalML/awesome-production-machine-learning](https://github.com/EthicalML/awesome-production-machine-learning) - A curated list of awesome open source libraries to deploy, monitor, version and scale your machine learning
- [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) - A curated list of awesome Machine Learning frameworks, libraries and software
- [eugeneyan/applied-ml](https://github.com/eugeneyan/applied-ml) - Papers & tech blogs by companies sharing their work on data science & machine learning in production
- [khangich/machine-learning-interview](https://github.com/khangich/machine-learning-interview) - Machine Learning Interviews from FAANG, Snapchat, LinkedIn
- [GokuMohandas/Made-With-ML](https://github.com/GokuMohandas/Made-With-ML) - Learn how to design, develop, deploy and iterate on production-grade ML applications
- [posit-dev/positron](https://github.com/posit-dev/positron) - Positron, a next-generation data science IDE
- [fixie-ai/ultravox](https://github.com/fixie-ai/ultravox) - A fast multimodal LLM for real-time voice
- [developersdigest/llm-answer-engine](https://github.com/developersdigest/llm-answer-engine) - Perplexity Inspired Answer Engine

## 🛠️ DevTools & Infrastructure

- [CapSoftware/Cap](https://github.com/CapSoftware/Cap) - Open source Loom alternative. Beautiful, shareable screen recordings
- [bitnami/containers](https://github.com/bitnami/containers) - Bitnami container images
- [kottster/kottster](https://github.com/kottster/kottster) - Instant Node.js admin panel. Secure, self-hosted, and easy to set up
- [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) - A list of Free Software network services and web applications which can be hosted on your own servers
- [coollabsio/coolify](https://github.com/coollabsio/coolify) - An open-source, self-hostable PaaS alternative to Vercel, Heroku & Netlify
- [herin7/gitforme](https://github.com/herin7/gitforme) - AI-powered GitHub code explorer — understand any repo in minutes, not days
- [coderamp-labs/gitingest](https://github.com/coderamp-labs/gitingest) - Replace 'hub' with 'ingest' in any GitHub URL to get a prompt-friendly extract of a codebase
- [ahmedkhaleel2004/gitdiagram](https://github.com/ahmedkhaleel2004/gitdiagram) - Free, simple, fast interactive diagrams for any GitHub repository
- [balena-io/open-balena](https://github.com/balena-io/open-balena) - Open source software to manage connected IoT devices at scale
- [enescingoz/awesome-n8n-templates](https://github.com/enescingoz/awesome-n8n-templates) - Supercharge your workflow automation with this curated collection of n8n templates
- [lucaswalter/n8n-ai-automations](https://github.com/lucaswalter/n8n-ai-automations) - Collection of n8n workflows, n8n templates, AI automations, and AI agents
- [Zie619/n8n-workflows](https://github.com/Zie619/n8n-workflows) - all of the workflows of n8n i could find
- [restyler/awesome-n8n](https://github.com/restyler/awesome-n8n) - Useful n8n resources: list of community nodes and tutorials
- [n8n-io/n8n](https://github.com/n8n-io/n8n) - Fair-code workflow automation platform with native AI capabilities
- [kuchin/awesome-cto](https://github.com/kuchin/awesome-cto) - A curated and opinionated list of resources for Chief Technology Officers

## 🌐 Web & Apps

- [TailAdmin/free-nextjs-admin-dashboard](https://github.com/TailAdmin/free-nextjs-admin-dashboard) - TailAdmin is a Next.js and Tailwind CSS free, open-source admin dashboard template
- [Nutlope/self.so](https://github.com/Nutlope/self.so) - LinkedIn -> personal site generator
- [toon-format/toon](https://github.com/toon-format/toon) - Token-Oriented Object Notation (TOON) – Compact, human-readable, schema-aware JSON for LLM prompts
- [superdesigndev/superdesign](https://github.com/superdesigndev/superdesign) - AI Product Design Agent - Open Source
- [iliane5/meridian](https://github.com/iliane5/meridian) - Meridian cuts through news noise by scraping hundreds of sources, analyzing stories with AI

## 📚 Learning & Reference

- [Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) - The 30 Days of Python programming challenge is a step-by-step guide to learn the Python programming language
- [Fechin/reference](https://github.com/Fechin/reference) - Share quick reference cheat sheet for developers
- [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) - freeCodeCamp.org's open-source codebase and curriculum
- [trekhleb/learn-python](https://github.com/trekhleb/learn-python) - Playground and cheatsheet for learning Python
- [addyosmani/gemini-cli-tips](https://github.com/addyosmani/gemini-cli-tips) - Gemini CLI Tips and Tricks
- [sindresorhus/awesome](https://github.com/sindresorhus/awesome) - Awesome lists about all kinds of interesting topics
- [public-apis/public-apis](https://github.com/public-apis/public-apis) - A collective list of free APIs

## 🔍 OCR & Document Processing

- [rednote-hilab/dots.ocr](https://github.com/rednote-hilab/dots.ocr) - Multilingual Document Layout Parsing in a Single Vision-Language Model
- [datalab-to/chandra](https://github.com/datalab-to/chandra) - OCR model that handles complex tables, forms, handwriting with full layout
- [google/A2UI](https://github.com/google/A2UI) - Advanced UI understanding model
- [ngafar/llama-scan](https://github.com/ngafar/llama-scan) - Transcribe PDFs with local LLMs
- [AnswerDotAI/clipmd](https://github.com/AnswerDotAI/clipmd) - Convert clipboard from HTML to MD
- [allenai/olmocr](https://github.com/allenai/olmocr) - Toolkit for linearizing PDFs for LLM datasets/training
- [deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR) - Contexts Optical Compression
- [bytedance/Dolphin](https://github.com/bytedance/Dolphin) - The official repo for "Dolphin: Document Image Parsing via Heterogeneous Anchor Prompting"
- [microsoft/markitdown](https://github.com/microsoft/markitdown) - Python tool for converting files and office documents to Markdown
- [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) - Open-source LLM Friendly Web Crawler & Scraper
- [docling-project/docling](https://github.com/docling-project/docling) - Get your documents ready for gen AI
- [jdepoix/youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) - This is a python API which allows you to get the transcript/subtitles for a given YouTube video

## 📝 Content & Productivity

- [HKUDS/Paper2Slides](https://github.com/HKUDS/Paper2Slides) - Paper2Slides: From Paper to Presentation in One Click
- [AsyncFuncAI/deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open) - Open Source DeepWiki: AI-Powered Wiki Generator for GitHub/Gitlab/Bitbucket Repositories

## Contributing

We welcome contributions! Please follow these guidelines:

1. **New additions**: Submit a pull request with your suggested repository
2. **Format**: Follow the existing format: `- [repo-name](url) - brief description`
3. **Quality over quantity**: Only submit high-quality, actively maintained repositories
4. **Categorization**: Choose the most appropriate category; suggest new ones if needed
5. **Description**: Keep descriptions concise and informative (1-2 lines max)

Before submitting:
- Ensure the repository is actively maintained
- Check that it's not already listed
- Verify the link works correctly
- Use the same format as existing entries

## About

Curated by [Ronald Mego](https://ronaldmego.com), Head of Data Analytics @ Millicom | Tigo. Built from hands-on experience deploying AI and data tools in enterprise environments.

This collection reflects real-world usage patterns and battle-tested solutions from building data platforms, implementing AI agents, and scaling ML operations across multinational telecommunications infrastructure. The focus is on tools that deliver production value, not just academic interest.

---

*Last updated: February 2026*