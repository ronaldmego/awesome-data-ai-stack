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
  - [🏠 Personal AI Assistants & Gateways](#-personal-ai-assistants--gateways)
  - [📚 Agent Resources & Guides](#-agent-resources--guides)
- [🏛️ Data Governance & Observability](#️-data-governance--observability)
- [🛡️ AI Safety & Responsible AI](#️-ai-safety--responsible-ai)
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

- [anthropics/claude-code](https://github.com/anthropics/claude-code) - Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster ⭐ 105.2k
- [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) - An open-source AI agent that brings the power of Gemini directly into your terminal ⭐ 100.0k
- [openai/codex](https://github.com/openai/codex) - Lightweight coding agent that runs in your terminal ⭐ 72.4k
- [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) - An open-source AI agent that lives in your terminal ⭐ 21.6k
- [bytedance/trae-agent](https://github.com/bytedance/trae-agent) - Trae Agent is an LLM-based agent for general purpose software engineering tasks ⭐ 11.2k
- [anomalyco/opencode](https://github.com/anomalyco/opencode) - The open source coding agent ⭐ 135.5k
- [HKUDS/DeepCode](https://github.com/HKUDS/DeepCode) - DeepCode: Open Agentic Coding (Paper2Code & Text2Web & Text2Backend) ⭐ 15.1k
- [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban) - Get 10X more out of Claude Code, Codex or any coding agent ⭐ 24.2k

### 🔧 MCP Servers & Skills

- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - A collection of MCP servers ⭐ 84.1k
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) - Model Context Protocol Servers ⭐ 82.8k
- [supabase-community/supabase-mcp](https://github.com/supabase-community/supabase-mcp) - Connect Supabase to your AI assistants ⭐ 2.6k
- [idosal/git-mcp](https://github.com/idosal/git-mcp) - Put an end to code hallucinations! GitMCP is a free, open-source, remote MCP server for any GitHub project ⭐ 7.9k
- [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) - A MCP for Claude Desktop / Claude Code / Windsurf / Cursor to build n8n workflows for you ⭐ 17.3k
- [firecrawl/firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server) - Official Firecrawl MCP Server - Adds powerful web scraping and search to Cursor, Claude and any other LLM clients ⭐ 5.9k
- [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox) - MCP Toolbox for Databases is an open source MCP server for databases ⭐ 13.6k
- [timescale/pg-aiguide](https://github.com/timescale/pg-aiguide) - MCP server and Claude plugin for Postgres skills and documentation ⭐ 1.7k
- [mongodb-js/mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server) - A Model Context Protocol server to connect to MongoDB databases and MongoDB Atlas Clusters ⭐ 987
- [crystaldba/postgres-mcp](https://github.com/crystaldba/postgres-mcp) - Postgres MCP Pro provides configurable read/write access and performance analysis ⭐ 2.5k
- [leonardsellem/n8n-mcp-server](https://github.com/leonardsellem/n8n-mcp-server) - MCP server that provides tools and resources for interacting with n8n API ⭐ 1.6k
- [excalidraw/excalidraw-mcp](https://github.com/excalidraw/excalidraw-mcp) - Fast and streamable Excalidraw MCP App ⭐ 3.7k
- [upstash/context7](https://github.com/upstash/context7) - Context7 MCP Server -- Up-to-date code documentation for LLMs and AI code editors ⭐ 51.4k
- [mcp-use/mcp-use](https://github.com/mcp-use/mcp-use) - The fullstack MCP framework to develop MCP Apps for ChatGPT / Claude & MCP Servers for AI Agents ⭐ 9.6k
- [mindsdb/mindsdb](https://github.com/mindsdb/mindsdb) - Federated Query Engine for AI - The only MCP Server you'll ever need ⭐ 38.9k
- [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) - The fast, Pythonic way to build MCP servers and clients ⭐ 24.2k
- [coleam00/mcp-crawl4ai-rag](https://github.com/coleam00/mcp-crawl4ai-rag) - Web Crawling and RAG Capabilities for AI Agents and AI Coding Assistants ⭐ 2.1k
- [sadiuysal/crawl4ai-mcp-server](https://github.com/sadiuysal/crawl4ai-mcp-server) - A lightweight MCP server that exposes Crawl4AI web scraping capabilities ⭐ 69
- [adhikasp/mcp-client-cli](https://github.com/adhikasp/mcp-client-cli) - A simple CLI to run LLM prompt and implement MCP client ⭐ 672
- [adhikasp/mcp-git-ingest](https://github.com/adhikasp/mcp-git-ingest) - A MCP server that helps read GitHub repository structure and important files ⭐ 302
- [antvis/mcp-server-chart](https://github.com/antvis/mcp-server-chart) - A visualization mcp & skills contains 25+ visual charts using @antvis ⭐ 3.9k
- [VikashLoomba/copilot-mcp](https://github.com/VikashLoomba/copilot-mcp) - A VSCode extension for finding and installing Agent Skills and MCP Apps ⭐ 482
- [steipete/claude-code-mcp](https://github.com/steipete/claude-code-mcp) - Claude Code as one-shot MCP server to have an agent in your agent ⭐ 1.2k
- [supercorp-ai/supergateway](https://github.com/supercorp-ai/supergateway) - Run MCP stdio servers over SSE and SSE over stdio. AI gateway ⭐ 2.5k

### 🎯 Orchestration & Multi-Agent

- [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) - Agent harness built with LangChain and LangGraph. Planning tool, filesystem backend, and sub-agent spawning out of the box ⭐ 18.7k
- [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) - Framework for orchestrating role-playing, autonomous AI agents ⭐ 47.8k
- [langflow-ai/langflow](https://github.com/langflow-ai/langflow) - Langflow is a powerful tool for building and deploying AI-powered agents and workflows ⭐ 146.5k
- [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) - Build AI Agents, Visually ⭐ 51.4k
- [wshobson/agents](https://github.com/wshobson/agents) - Intelligent automation and multi-agent orchestration for Claude Code ⭐ 32.8k
- [The-Pocket/PocketFlow](https://github.com/The-Pocket/PocketFlow) - Pocket Flow: 100-line LLM framework. Let Agents build Agents! ⭐ 10.3k
- [MotiaDev/motia](https://github.com/MotiaDev/motia) - Multi-Language Backend Framework that unifies APIs, background jobs, queues, workflows, streams, and AI agents ⭐ 15.2k
- [simstudioai/sim](https://github.com/simstudioai/sim) - Build, deploy, and orchestrate AI agents. Sim is the central intelligence layer for your AI workforce ⭐ 27.4k
- [agno-agi/agno](https://github.com/agno-agi/agno) - The programming language for agentic software. Build, run, and manage multi-agent systems at scale ⭐ 39.1k
- [TransformerOptimus/SuperAGI](https://github.com/TransformerOptimus/SuperAGI) - A dev-first open source autonomous AI agent framework ⭐ 17.4k
- [Pythagora-io/gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) - The first real AI developer ⭐ 33.8k
- [Danau5tin/multi-agent-coding-system](https://github.com/Danau5tin/multi-agent-coding-system) - Reached #13 on Stanford's Terminal Bench leaderboard. Orchestrator, explorer & coder agents ⭐ 1.4k
- [docker/compose-for-agents](https://github.com/docker/compose-for-agents) - Build and run AI agents using Docker Compose ⭐ 900
- [coleam00/ottomator-agents](https://github.com/coleam00/ottomator-agents) - All the open source AI Agents hosted on the oTTomator Live Agent Studio platform ⭐ 5.5k
- [coleam00/pydantic-ai-github-agent](https://github.com/coleam00/pydantic-ai-github-agent) - The agent built for AI Agents series on YouTube ⭐ 65
- [coleam00/PydanticAI-Research-Agent](https://github.com/coleam00/PydanticAI-Research-Agent) - Pydantic AI Research Agent Built with the PRP Framework Template ⭐ 131
- [kortix-ai/suna](https://github.com/kortix-ai/suna) - Kortix – build, manage and train AI Agents ⭐ 19.6k
- [The-Pocket/PocketFlow-Tutorial-Codebase-Knowledge](https://github.com/The-Pocket/PocketFlow-Tutorial-Codebase-Knowledge) - Pocket Flow: Codebase to Tutorial ⭐ 12.2k
- [VRSEN/agency-swarm](https://github.com/VRSEN/agency-swarm) - Reliable Multi-Agent Orchestration Framework based on the IETF's agency-spec ⭐ 4.1k

### 📝 Memory & RAG

- [mem0ai/mem0](https://github.com/mem0ai/mem0) - Universal memory layer for AI Agents ⭐ 51.8k
- [getzep/graphiti](https://github.com/getzep/graphiti) - Build Real-Time Knowledge Graphs for AI Agents ⭐ 24.4k
- [topoteretes/cognee](https://github.com/topoteretes/cognee) - Knowledge Engine for AI Agent Memory in 6 lines of code ⭐ 14.9k
- [campfirein/cipher](https://github.com/campfirein/cipher) - Byterover Cipher is an opensource memory layer specifically designed for coding agents ⭐ 3.6k
- [infiniflow/ragflow](https://github.com/infiniflow/ragflow) - RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine ⭐ 76.9k
- [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) - RAG-Anything: All-in-One RAG Framework ⭐ 14.8k
- [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) - LightRAG: Simple and Fast Retrieval-Augmented Generation ⭐ 31.5k
- [raphaelmansuy/edgequake](https://github.com/raphaelmansuy/edgequake) - High-performance GraphRAG inspired from LightRag written in Rust ⭐ 1.6k
- [yichuan-w/LEANN](https://github.com/yichuan-w/LEANN) - RAG on Everything with LEANN. Enjoy 97% storage savings while running a fast, accurate, and 100% private RAG application ⭐ 10.4k
- [airweave-ai/airweave](https://github.com/airweave-ai/airweave) - Open-source context retrieval layer for AI agents ⭐ 6.2k
- [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) - Zero-server code intelligence engine — client-side knowledge graph creator with built-in Graph RAG Agent for code exploration ⭐ 21.3k

### 💬 Conversational & Chat

- [emcie-co/parlant](https://github.com/emcie-co/parlant) - LLM agents built for control. Designed for real-world use. Deployed in minutes ⭐ 17.9k
- [janhq/jan](https://github.com/janhq/jan) - Jan is an open source alternative to ChatGPT that runs 100% offline on your computer ⭐ 41.4k
- [openinterpreter/open-interpreter](https://github.com/openinterpreter/open-interpreter) - A natural language interface for computers ⭐ 63.0k
- [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) - The Frontend for Agents & Generative UI. React + Angular ⭐ 29.9k
- [ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui) - AG-UI: the Agent-User Interaction Protocol. Bring Agents into Frontend Applications ⭐ 12.8k
- [open-webui/open-webui](https://github.com/open-webui/open-webui) - User-friendly AI Interface (Supports Ollama, OpenAI API, ...) ⭐ 129.6k
- [Anything-LLM/anything-llm](https://github.com/Mintplex-Labs/anything-llm) - The all-in-one Desktop & Docker AI application with built-in RAG, AI agents ⭐ 57.4k
- [letta-ai/letta](https://github.com/letta-ai/letta) - Letta is the platform for building stateful agents: AI with advanced memory ⭐ 21.9k
- [Jackywine/Bella](https://github.com/Jackywine/Bella) - Bella is best ⭐ 6.4k
- [Doriandarko/kimi-writer](https://github.com/Doriandarko/kimi-writer) - AI writing agent powered by kimi-k2-thinking ⭐ 545

### 🌐 Browser & Web Agents

- [browser-use/browser-use](https://github.com/browser-use/browser-use) - Make websites accessible for AI agents. Automate tasks online with ease ⭐ 85.6k
- [browserbase/stagehand](https://github.com/browserbase/stagehand) - The AI Browser Automation Framework ⭐ 21.8k
- [Fosowl/agenticSeek](https://github.com/Fosowl/agenticSeek) - Fully Local Manus AI. No APIs, No $200 monthly bills. Enjoy an autonomous agent that thinks, browses the web, and code ⭐ 25.8k
- [aaronjmars/opendia](https://github.com/aaronjmars/opendia) - Connect your browser to AI models. Just use Dia on Chrome, Arc or Firefox ⭐ 1.8k
- [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) - An autonomous agent that conducts deep research on any data using any LLM providers ⭐ 26.2k

### 🏠 Personal AI Assistants & Gateways

- [openclaw/openclaw](https://github.com/openclaw/openclaw) - Your own personal AI assistant. Any OS. Any Platform. The lobster way ⭐ 345.5k
- [paperclipai/paperclip](https://github.com/paperclipai/paperclip) - Open-source orchestration for zero-human companies. If OpenClaw is an employee, Paperclip is the company — org charts, budgets, goals, and agent coordination in one dashboard ⭐ 44.5k
- [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) - Run OpenClaw more securely inside NVIDIA OpenShell with managed inference and sandboxed isolation ⭐ 18.2k
- [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) - Self-improving AI agent with built-in learning loop, user modeling, and OpenClaw migration support ⭐ 22.2k

### 📚 Agent Resources & Guides

- [open-gitagent/gitagent](https://github.com/open-gitagent/gitagent) - Framework-agnostic, git-native standard for defining AI agents. Clone a repo, get an agent. Export to Claude Code, OpenAI, CrewAI, LangChain, and more ⭐ 2.5k
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - A curated list of awesome skills, hooks, slash-commands, agent orchestrators, applications, and plugins for Claude Code ⭐ 35.7k
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models ⭐ 104.3k
- [coleam00/context-engineering-intro](https://github.com/coleam00/context-engineering-intro) - Context engineering is the new vibe coding - it's the way to actually make AI coding assistants work ⭐ 13.0k
- [Cranot/claude-code-guide](https://github.com/Cranot/claude-code-guide) - The Complete Claude Code CLI Guide - Live & Auto-Updated Every 2 Days ⭐ 2.6k
- [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) - Best practices and tips for Claude Code — agentic engineering patterns, vibe coding workflows ⭐ 30.8k
- [coleam00/ai-agents-masterclass](https://github.com/coleam00/ai-agents-masterclass) - Follow along with my AI Agents Masterclass videos! All of the code I create and use in this series ⭐ 3.3k
- [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) - In-depth tutorials on LLMs, RAGs and real-world AI agent applications ⭐ 33.1k
- [SamurAIGPT/awesome-openclaw](https://github.com/SamurAIGPT/awesome-openclaw) - A curated list of awesome OpenClaw resources, tools, skills, tutorials, and articles ⭐ 851
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) - A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows ⭐ 50.5k
- [BehiSecc/awesome-claude-skills](https://github.com/BehiSecc/awesome-claude-skills) - A curated list of Claude Skills ⭐ 8.1k
- [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) - A set of ready to use scientific skills for Claude ⭐ 17.1k
- [Kamalnrf/claude-plugins](https://github.com/Kamalnrf/claude-plugins) - Lightweight registry to discover, install, and manage all public Claude plugins and agent skills ⭐ 489
- [anthropics/skills](https://github.com/anthropics/skills) - Public repository for Agent Skills ⭐ 109.0k
- [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) - Official, Anthropic-managed directory of high quality Claude Code Plugins ⭐ 15.8k
- [google-gemini/gemini-skills](https://github.com/google-gemini/gemini-skills) - Skills for the Gemini API, SDK and model/agent interactions ⭐ 3.1k
- [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) - CLI tool for configuring and monitoring Claude Code ⭐ 24.0k
- [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) - An AI-powered task-management system you can drop into Cursor, Lovable, Windsurf, Roo, and others ⭐ 26.4k
- [coleam00/Archon](https://github.com/coleam00/Archon) - Beta release of Archon OS - the knowledge and task management backbone for AI coding assistants ⭐ 13.9k
- [danielmiessler/Fabric](https://github.com/danielmiessler/Fabric) - Fabric is an open-source framework for augmenting humans using AI ⭐ 40.3k


## 🏛️ Data Governance & Observability

- [open-metadata/OpenMetadata](https://github.com/open-metadata/OpenMetadata) - Unified metadata platform for data discovery, data observability, and data governance, powered by a central metadata repository ⭐ 9.3k
- [datahub-project/datahub](https://github.com/datahub-project/datahub) - The Metadata Platform for your Data and AI — data discovery, lineage, and governance at scale ⭐ 11.8k
- [OpenLineage/OpenLineage](https://github.com/OpenLineage/OpenLineage) - An open standard for metadata and lineage collection. Track data pipeline jobs, datasets, and runs ⭐ 2.4k
- [great-expectations/great_expectations](https://github.com/great-expectations/great_expectations) - The leading open-source data quality framework. Define, document, and validate data expectations ⭐ 11.3k
- [sodadata/soda-core](https://github.com/sodadata/soda-core) - Data quality testing and monitoring for SQL, Spark, and Pandas. Run checks directly in your pipelines ⭐ 2.3k
- [apache/atlas](https://github.com/apache/atlas) - Apache Atlas provides open metadata management and governance capabilities for organizations that need to build a catalog of their data assets ⭐ 2.1k

## 🛡️ AI Safety & Responsible AI

- [guardrails-ai/guardrails](https://github.com/guardrails-ai/guardrails) - Adding guardrails to large language models. Validate and structure LLM outputs with programmable rules ⭐ 6.6k
- [NVIDIA/NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) - Open-source toolkit for easily adding programmable guardrails to LLM-based conversational AI ⭐ 5.9k
- [Trusted-AI/AIF360](https://github.com/Trusted-AI/AIF360) - IBM AI Fairness 360 — comprehensive fairness metrics for datasets and ML models ⭐ 2.8k
- [microsoft/responsible-ai-toolbox](https://github.com/microsoft/responsible-ai-toolbox) - Responsible AI dashboard and tools for model and data exploration, error analysis, and fairness assessment ⭐ 1.7k
- [whylabs/langkit](https://github.com/whylabs/langkit) - Open-source toolkit for monitoring Large Language Models — detect toxicity, hallucinations, and data quality issues ⭐ 980

## 🎨 Avatar, Video & Image AI

- [jamiepine/voicebox](https://github.com/jamiepine/voicebox) - The open-source voice synthesis studio powered by Qwen3-TTS ⭐ 14.4k
- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) - The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface ⭐ 107.6k
- [ZeroLu/awesome-nanobanana-pro](https://github.com/ZeroLu/awesome-nanobanana-pro) - An awesome list of curated Nano Banana pro prompts and examples ⭐ 9.6k
- [PicoTrex/Awesome-Nano-Banana-images](https://github.com/PicoTrex/Awesome-Nano-Banana-images) - A curated collection of fun and creative examples generated with Nano Banana & Nano Banana Pro ⭐ 21.9k
- [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox) - SoTA open-source TTS ⭐ 24.1k
- [facefusion/facefusion-docker](https://github.com/facefusion/facefusion-docker) - Industry leading face manipulation platform ⭐ 524
- [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) - Automate the process of making money online ⭐ 28.0k

## 📊 Data Engineering & Analytics
- [FalkorDB/QueryWeaver](https://github.com/FalkorDB/QueryWeaver) - Open-source Text2SQL tool that transforms natural language into SQL using graph-powered schema understanding ⭐ 796

- [DataExpert-io/data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) - This is a repo with links to everything you'd ever want to learn about data engineering ⭐ 40.8k
- [dlt-hub/dlt](https://github.com/dlt-hub/dlt) - data load tool (dlt) is an open source Python library that makes data loading easy ⭐ 5.2k
- [igorbarinov/awesome-data-engineering](https://github.com/igorbarinov/awesome-data-engineering) - A curated list of data engineering tools for software developers ⭐ 8.4k
- [gunnarmorling/awesome-opensource-data-engineering](https://github.com/gunnarmorling/awesome-opensource-data-engineering) - An Awesome List of Open-Source Data Engineering Projects ⭐ 3.1k
- [Countly/countly-server](https://github.com/Countly/countly-server) - Countly is a privacy-first, AI-powered analytics and engagement platform ⭐ 5.8k
- [tensorlakeai/tensorlake](https://github.com/tensorlakeai/tensorlake) - Tensorlake is a Document Ingestion API and a serverless platform for building data processing ⭐ 895
- [weaviate/elysia](https://github.com/weaviate/elysia) - Python package and backend for the Elysia platform app ⭐ 1.9k
- [mito-ds/mito](https://github.com/mito-ds/mito) - Jupyter extensions that help you write code faster: Context aware AI Chat, Autocomplete, and Spreadsheet ⭐ 2.6k
- [pixeltable/pixeltable](https://github.com/pixeltable/pixeltable) - Data Infrastructure providing a declarative, incremental approach for multimodal AI workloads ⭐ 1.6k
- [chartdb/chartdb](https://github.com/chartdb/chartdb) - Database diagrams editor that allows you to visualize and design your DB with a single query ⭐ 21.7k
- [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core) - dbt enables data analysts and engineers to transform their data using the same practices that software engineers use ⭐ 12.5k
- [valkey-io/valkey](https://github.com/valkey-io/valkey) - A flexible distributed key-value database that is optimized for caching and other realtime workloads ⭐ 25.3k
- [grafana/grafana](https://github.com/grafana/grafana) - The open and composable observability and data visualization platform ⭐ 72.9k
- [elastic/elasticsearch](https://github.com/elastic/elasticsearch) - Free and Open Source, Distributed, RESTful Search Engine ⭐ 76.4k
- [trinodb/trino](https://github.com/trinodb/trino) - Official repository of Trino, the distributed SQL query engine for big data ⭐ 12.7k
- [apache/superset](https://github.com/apache/superset) - Apache Superset is a Data Visualization and Data Exploration Platform ⭐ 72.2k
- [microsoft/data-formulator](https://github.com/microsoft/data-formulator) - Create rich visualizations with AI ⭐ 15.2k
- [vllm-project/vllm](https://github.com/vllm-project/vllm) - A high-throughput and memory-efficient inference and serving engine for LLMs ⭐ 75.0k
- [Openpanel-dev/openpanel](https://github.com/Openpanel-dev/openpanel) - OpenPanel is an open-source web and product analytics platform ⭐ 5.6k
- [Canner/WrenAI](https://github.com/Canner/WrenAI) - GenBI (Generative BI) queries any database in natural language, generates accurate SQL, charts ⭐ 14.8k
- [sinaptik-ai/pandas-ai](https://github.com/sinaptik-ai/pandas-ai) - Chat with your database or your datalake (SQL, CSV, parquet) ⭐ 23.4k
- [vanna-ai/vanna](https://github.com/vanna-ai/vanna) - Chat with your SQL database. Accurate Text-to-SQL Generation via LLMs using Agentic Retrieval ⭐ 23.2k
- [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) - Financial data platform for analysts, quants and AI agents ⭐ 65.0k
- [ganttrify](https://github.com/ganttrify/ganttrify) - Create beautiful Gantt charts with ggplot2
- [Avaiga/taipy](https://github.com/Avaiga/taipy) - Turns Data and AI algorithms into production-ready web applications in no time ⭐ 19.1k
- [mckinsey/vizro](https://github.com/mckinsey/vizro) - Vizro is a low-code toolkit for building high-quality data visualization apps ⭐ 3.6k

## 🧠 ML & Data Science

- [KalyanM45/AI-Project-Gallery](https://github.com/KalyanM45/AI-Project-Gallery) - Repository containing Artificial Intelligence Projects such as Machine Learning, Deep Learning and Generative AI ⭐ 4.6k
- [google/langextract](https://github.com/google/langextract) - A Python library for extracting structured information from unstructured text using LLMs ⭐ 35.0k
- [lyogavin/airllm](https://github.com/lyogavin/airllm) - AirLLM 70B inference with single 4GB GPU ⭐ 14.7k
- [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) - DeepTutor: AI-Powered Personalized Learning Assistant ⭐ 11.0k
- [Sumanth077/ai-engineering-toolkit](https://github.com/Sumanth077/ai-engineering-toolkit) - A curated list of 100+ libraries and frameworks for AI engineers building with LLMs ⭐ 3.0k
- [microsoft/BitNet](https://github.com/microsoft/BitNet) - Official inference framework for 1-bit LLMs ⭐ 37.0k
- [cvs-health/uqlm](https://github.com/cvs-health/uqlm) - UQLM: Uncertainty Quantification for Language Models, is a Python package for UQ-based LLM hallucination detection ⭐ 1.1k
- [confident-ai/deepeval](https://github.com/confident-ai/deepeval) - The LLM Evaluation Framework ⭐ 14.4k
- [OpenBMB/MiniCPM-o](https://github.com/OpenBMB/MiniCPM-o) - A Gemini 2.5 Flash Level MLLM for Vision, Speech, and Full-Duplex Multimodal Live Streaming ⭐ 24.3k
- [mistralai/cookbook](https://github.com/mistralai/cookbook) - Mistral AI cookbook ⭐ 2.2k
- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) - All Algorithms implemented in Python ⭐ 219.2k
- [KalyanKS-NLP/llm-engineer-toolkit](https://github.com/KalyanKS-NLP/llm-engineer-toolkit) - A curated list of 120+ LLM libraries category wise ⭐ 10.1k
- [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) - The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data ⭐ 102.8k
- [academic/awesome-datascience](https://github.com/academic/awesome-datascience) - An awesome Data Science repository to learn and apply for real world problems ⭐ 28.7k
- [hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory) - Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024) ⭐ 69.4k
- [Machine-Learning-Tokyo/Interactive_Tools](https://github.com/Machine-Learning-Tokyo/Interactive_Tools) - Interactive Tools for Machine Learning, Deep Learning and Math ⭐ 2.8k
- [rushter/MLAlgorithms](https://github.com/rushter/MLAlgorithms) - Minimal and clean examples of machine learning algorithms implementations ⭐ 11.0k
- [jivoi/awesome-ml-for-cybersecurity](https://github.com/jivoi/awesome-ml-for-cybersecurity) - Machine Learning for Cyber Security ⭐ 8.4k
- [roboticcam/machine-learning-notes](https://github.com/roboticcam/machine-learning-notes) - My continuously updated Machine Learning, Probabilistic Models and Deep Learning notes and demos ⭐ 9.6k
- [ml-tooling/ml-workspace](https://github.com/ml-tooling/ml-workspace) - All-in-one web-based IDE specialized for machine learning and data science ⭐ 3.5k
- [lukasmasuch/best-of-ml-python](https://github.com/lukasmasuch/best-of-ml-python) - A ranked list of awesome machine learning Python libraries. Updated weekly ⭐ 23.4k
- [EthicalML/awesome-production-machine-learning](https://github.com/EthicalML/awesome-production-machine-learning) - A curated list of awesome open source libraries to deploy, monitor, version and scale your machine learning ⭐ 20.3k
- [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) - A curated list of awesome Machine Learning frameworks, libraries and software ⭐ 72.1k
- [eugeneyan/applied-ml](https://github.com/eugeneyan/applied-ml) - Papers & tech blogs by companies sharing their work on data science & machine learning in production ⭐ 28.8k
- [GokuMohandas/Made-With-ML](https://github.com/GokuMohandas/Made-With-ML) - Learn how to design, develop, deploy and iterate on production-grade ML applications ⭐ 47.1k
- [posit-dev/positron](https://github.com/posit-dev/positron) - Positron, a next-generation data science IDE ⭐ 4.0k
- [fixie-ai/ultravox](https://github.com/fixie-ai/ultravox) - A fast multimodal LLM for real-time voice ⭐ 4.4k
- [developersdigest/llm-answer-engine](https://github.com/developersdigest/llm-answer-engine) - Perplexity Inspired Answer Engine ⭐ 5.0k
- [unslothai/notebooks](https://github.com/unslothai/notebooks) - Jupyter notebooks demonstrating LLM fine-tuning with Unsloth AI for efficient model training ⭐ 5.1k

📚 **New to ML?** Check out [Learning & Reference](#-learning--reference) for courses and tutorials.

## 🛠️ DevTools & Infrastructure

- [CapSoftware/Cap](https://github.com/CapSoftware/Cap) - Open source Loom alternative. Beautiful, shareable screen recordings ⭐ 17.8k
- [bitnami/containers](https://github.com/bitnami/containers) - Bitnami container images ⭐ 4.4k
- [kottster/kottster](https://github.com/kottster/kottster) - Instant Node.js admin panel. Secure, self-hosted, and easy to set up ⭐ 1.1k
- [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) - A list of Free Software network services and web applications which can be hosted on your own servers ⭐ 283.5k
- [coollabsio/coolify](https://github.com/coollabsio/coolify) - An open-source, self-hostable PaaS alternative to Vercel, Heroku & Netlify ⭐ 52.5k
- [herin7/gitforme](https://github.com/herin7/gitforme) - AI-powered GitHub code explorer — understand any repo in minutes, not days ⭐ 381
- [coderamp-labs/gitingest](https://github.com/coderamp-labs/gitingest) - Replace 'hub' with 'ingest' in any GitHub URL to get a prompt-friendly extract of a codebase ⭐ 14.2k
- [ahmedkhaleel2004/gitdiagram](https://github.com/ahmedkhaleel2004/gitdiagram) - Free, simple, fast interactive diagrams for any GitHub repository ⭐ 15.4k
- [balena-io/open-balena](https://github.com/balena-io/open-balena) - Open source software to manage connected IoT devices at scale ⭐ 1.2k
- [enescingoz/awesome-n8n-templates](https://github.com/enescingoz/awesome-n8n-templates) - Supercharge your workflow automation with this curated collection of n8n templates ⭐ 20.8k
- [lucaswalter/n8n-ai-automations](https://github.com/lucaswalter/n8n-ai-automations) - Collection of n8n workflows, n8n templates, AI automations, and AI agents ⭐ 1.4k
- [Zie619/n8n-workflows](https://github.com/Zie619/n8n-workflows) - all of the workflows of n8n i could find ⭐ 53.5k
- [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) - Command-line interface for Playwright, a browser automation tool with AI capabilities ⭐ 6.8k
- [restyler/awesome-n8n](https://github.com/restyler/awesome-n8n) - Useful n8n resources: list of community nodes and tutorials ⭐ 2.8k
- [n8n-io/n8n](https://github.com/n8n-io/n8n) - Fair-code workflow automation platform with native AI capabilities ⭐ 182.1k
- [kuchin/awesome-cto](https://github.com/kuchin/awesome-cto) - A curated and opinionated list of resources for Chief Technology Officers ⭐ 34.6k
- [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) - Right-size LLM models to your hardware. Detects CPU, RAM, GPU and scores models by quality, speed, fit and context. Supports Ollama, llama.cpp, MLX ⭐ 20.8k

## 🌐 Web & Apps

- [TailAdmin/free-nextjs-admin-dashboard](https://github.com/TailAdmin/free-nextjs-admin-dashboard) - TailAdmin is a Next.js and Tailwind CSS free, open-source admin dashboard template ⭐ 2.4k
- [Nutlope/self.so](https://github.com/Nutlope/self.so) - LinkedIn -> personal site generator ⭐ 2.9k
- [toon-format/toon](https://github.com/toon-format/toon) - Token-Oriented Object Notation (TOON) – Compact, human-readable, schema-aware JSON for LLM prompts ⭐ 23.6k
- [superdesigndev/superdesign](https://github.com/superdesigndev/superdesign) - AI Product Design Agent - Open Source ⭐ 6.3k
- [iliane5/meridian](https://github.com/iliane5/meridian) - Meridian cuts through news noise by scraping hundreds of sources, analyzing stories with AI ⭐ 2.4k

## 📚 Learning & Reference

*Educational resources, courses, and tutorials organized by topic.*

> **📖 Categorization Guide:** Courses, tutorials, and learning resources go here. Tools, frameworks, and production libraries belong in their respective technical categories (e.g., 🧠 ML & Data Science). See [Contributing](#contributing) for details.

### Data Science & ML
- [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) - 12 weeks, 26 lessons, 52 quizzes, classic Machine Learning for all ⭐ 84.9k
- [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners) - 10 Weeks, 20 Lessons, Data Science for All! ⭐ 34.7k
- [ageron/handson-ml3](https://github.com/ageron/handson-ml3) - A series of Jupyter notebooks that walk you through the fundamentals of Machine Learning and Deep Learning ⭐ 12.8k
- [d2l-ai/d2l-en](https://github.com/d2l-ai/d2l-en) - Interactive deep learning book with multi-framework code, math, and discussions ⭐ 28.5k
- [Avik-Jain/100-Days-Of-ML-Code](https://github.com/Avik-Jain/100-Days-Of-ML-Code) - 100 Days of Machine Learning Coding ⭐ 50.2k
- [mml-book/mml-book.github.io](https://github.com/mml-book/mml-book.github.io) - Companion webpage to the book "Mathematics For Machine Learning" ⭐ 15.3k
- [karpathy/nn-zero-to-hero](https://github.com/karpathy/nn-zero-to-hero) - Neural networks: zero to hero ⭐ 21.2k
- [ujjwalkarn/Machine-Learning-Tutorials](https://github.com/ujjwalkarn/Machine-Learning-Tutorials) - Machine learning and deep learning tutorials, articles and other resources ⭐ 17.7k
- [khangich/machine-learning-interview](https://github.com/khangich/machine-learning-interview) - Machine Learning Interviews from FAANG, Snapchat, LinkedIn ⭐ 12.4k

### AI & Agents
- [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) - 21 Lessons, Get Started Building with Generative AI ⭐ 108.8k
- [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) - 10 Lessons to Get Started Building AI Agents ⭐ 55.7k
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) - Guides, papers, lectures, notebooks and resources for prompt engineering ⭐ 72.7k
- [HandsOnLLM/Hands-On-Large-Language-Models](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models) - Official code repo for the O'Reilly Book - Hands-On Large Language Models ⭐ 24.7k
- [NirDiamant/GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents) - This repository provides a comprehensive collection of tutorials and implementations for Generative AI Agents ⭐ 20.9k
- [NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) - This repository provides a comprehensive collection of tutorials and implementations for Retrieval-Augmented Generation (RAG) systems ⭐ 26.4k
- [labmlai/annotated_deep_learning_papers](https://github.com/labmlai/annotated_deep_learning_papers) - Annotated Deep Learning Papers

### NLP & RL
- [keon/awesome-nlp](https://github.com/keon/awesome-nlp) - A curated list of resources dedicated to Natural Language Processing ⭐ 18.4k
- [aikorea/awesome-rl](https://github.com/aikorea/awesome-rl) - Reinforcement learning resources curated ⭐ 9.7k
- [FareedKhan-dev/all-rl-algorithms](https://github.com/FareedKhan-dev/all-rl-algorithms) - Implementations of all major Reinforcement Learning algorithms ⭐ 1.5k

### Programming & General
- [Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) - The 30 Days of Python programming challenge is a step-by-step guide to learn the Python programming language ⭐ 60.4k
- [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) - freeCodeCamp.org's open-source codebase and curriculum ⭐ 440.5k
- [trekhleb/learn-python](https://github.com/trekhleb/learn-python) - Playground and cheatsheet for learning Python ⭐ 17.8k
- [Fechin/reference](https://github.com/Fechin/reference) - Share quick reference cheat sheet for developers ⭐ 10.3k
- [addyosmani/gemini-cli-tips](https://github.com/addyosmani/gemini-cli-tips) - Gemini CLI Tips and Tricks ⭐ 2.3k
- [sindresorhus/awesome](https://github.com/sindresorhus/awesome) - Awesome lists about all kinds of interesting topics ⭐ 451.1k
- [public-apis/public-apis](https://github.com/public-apis/public-apis) - A collective list of free APIs ⭐ 418.3k

## 🔍 OCR & Document Processing

- [rednote-hilab/dots.ocr](https://github.com/rednote-hilab/dots.ocr) - Multilingual Document Layout Parsing in a Single Vision-Language Model ⭐ 8.2k
- [datalab-to/chandra](https://github.com/datalab-to/chandra) - OCR model that handles complex tables, forms, handwriting with full layout ⭐ 8.2k
- [google/A2UI](https://github.com/google/A2UI) - Advanced UI understanding model ⭐ 13.8k
- [ngafar/llama-scan](https://github.com/ngafar/llama-scan) - Transcribe PDFs with local LLMs ⭐ 818
- [AnswerDotAI/clipmd](https://github.com/AnswerDotAI/clipmd) - Convert clipboard from HTML to MD ⭐ 220
- [allenai/olmocr](https://github.com/allenai/olmocr) - Toolkit for linearizing PDFs for LLM datasets/training ⭐ 17.1k
- [deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR) - Contexts Optical Compression ⭐ 22.8k
- [bytedance/Dolphin](https://github.com/bytedance/Dolphin) - The official repo for "Dolphin: Document Image Parsing via Heterogeneous Anchor Prompting" ⭐ 8.9k
- [microsoft/markitdown](https://github.com/microsoft/markitdown) - Python tool for converting files and office documents to Markdown ⭐ 93.2k
- [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) - Open-source LLM Friendly Web Crawler & Scraper ⭐ 63.2k
- [docling-project/docling](https://github.com/docling-project/docling) - Get your documents ready for gen AI ⭐ 56.9k
- [jdepoix/youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) - This is a python API which allows you to get the transcript/subtitles for a given YouTube video ⭐ 7.2k

## 📝 Content & Productivity

- [HKUDS/Paper2Slides](https://github.com/HKUDS/Paper2Slides) - Paper2Slides: From Paper to Presentation in One Click ⭐ 3.3k
- [AsyncFuncAI/deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open) - Open Source DeepWiki: AI-Powered Wiki Generator for GitHub/Gitlab/Bitbucket Repositories ⭐ 15.3k

## Contributing

We welcome contributions! Please follow these guidelines:

### Quick Rules
1. **New additions**: Submit a pull request with your suggested repository
2. **Format**: Follow the existing format: `- [repo-name](url) - brief description`
3. **Quality over quantity**: Only submit high-quality, actively maintained repositories
4. **Categorization**: See guide below ↓
5. **Description**: Keep descriptions concise and informative (1-2 lines max)

### Categorization Guide

| If the repo is... | Put it in... | Examples |
|-------------------|--------------|----------|
| **A course, tutorial, or learning resource** | 📚 [Learning & Reference](#-learning--reference) | `ML-For-Beginners`, `nn-zero-to-hero`, prompt engineering guides |
| **A tool or framework for production use** | Technical category (e.g., 🧠 ML & Data Science, 🤖 AI Agents) | `scikit-learn`, `crewAI`, `mem0` |
| **An awesome list** | Matching topic or 📚 Learning | `awesome-datascience`, `awesome-nlp` |
| **Reference/cheat sheets** | 📚 Learning & Reference → Reference | `reference`, `cheat-sheets` |

**Golden Rule:** One repo, one primary location. Learning resources → Learning. Tools → Technical categories. Cross-references are added automatically where relevant.

### Before submitting
- Ensure the repository is actively maintained
- Check that it's not already listed
- Verify the link works correctly
- Use the same format as existing entries
- Follow the categorization guide above

## About

Curated by [Ronald Mego](https://ronaldmego.com), Head of Data Analytics @ Millicom | Tigo. Built from hands-on experience deploying AI and data tools in enterprise environments.

This collection reflects real-world usage patterns and battle-tested solutions from building data platforms, implementing AI agents, and scaling ML operations across multinational telecommunications infrastructure. The focus is on tools that deliver production value, not just academic interest.

---

*Last updated: March 2026*