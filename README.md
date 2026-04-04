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

- [anthropics/claude-code](https://github.com/anthropics/claude-code) `⭐105.2k` - Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster
- [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) `⭐100.0k` - An open-source AI agent that brings the power of Gemini directly into your terminal
- [openai/codex](https://github.com/openai/codex) `⭐72.4k` - Lightweight coding agent that runs in your terminal
- [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) `⭐21.6k` - An open-source AI agent that lives in your terminal
- [bytedance/trae-agent](https://github.com/bytedance/trae-agent) `⭐11.2k` - Trae Agent is an LLM-based agent for general purpose software engineering tasks
- [anomalyco/opencode](https://github.com/anomalyco/opencode) `⭐135.5k` - The open source coding agent
- [HKUDS/DeepCode](https://github.com/HKUDS/DeepCode) `⭐15.1k` - DeepCode: Open Agentic Coding (Paper2Code & Text2Web & Text2Backend)
- [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban) `⭐24.2k` - Get 10X more out of Claude Code, Codex or any coding agent
- [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) `⭐23.0k` - Multi-agent orchestration for Claude Code. Zero learning curve — run parallel agents, define workflows, delegate tasks without learning internals
- [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) `⭐10.5k` - Open-source Claude Code CLI for OpenAI, Gemini, DeepSeek, Ollama, and 200+ models via OpenAI-compatible APIs. Same terminal-first workflow, any provider

### 🔧 MCP Servers & Skills

- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) `⭐84.1k` - A collection of MCP servers
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) `⭐82.8k` - Model Context Protocol Servers
- [supabase-community/supabase-mcp](https://github.com/supabase-community/supabase-mcp) `⭐2.6k` - Connect Supabase to your AI assistants
- [idosal/git-mcp](https://github.com/idosal/git-mcp) `⭐7.9k` - Put an end to code hallucinations! GitMCP is a free, open-source, remote MCP server for any GitHub project
- [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) `⭐17.3k` - A MCP for Claude Desktop / Claude Code / Windsurf / Cursor to build n8n workflows for you
- [firecrawl/firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server) `⭐5.9k` - Official Firecrawl MCP Server - Adds powerful web scraping and search to Cursor, Claude and any other LLM clients
- [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox) `⭐13.6k` - MCP Toolbox for Databases is an open source MCP server for databases
- [timescale/pg-aiguide](https://github.com/timescale/pg-aiguide) `⭐1.7k` - MCP server and Claude plugin for Postgres skills and documentation
- [mongodb-js/mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server) `⭐987` - A Model Context Protocol server to connect to MongoDB databases and MongoDB Atlas Clusters
- [crystaldba/postgres-mcp](https://github.com/crystaldba/postgres-mcp) `⭐2.5k` - Postgres MCP Pro provides configurable read/write access and performance analysis
- [leonardsellem/n8n-mcp-server](https://github.com/leonardsellem/n8n-mcp-server) `⭐1.6k` - MCP server that provides tools and resources for interacting with n8n API
- [excalidraw/excalidraw-mcp](https://github.com/excalidraw/excalidraw-mcp) `⭐3.7k` - Fast and streamable Excalidraw MCP App
- [upstash/context7](https://github.com/upstash/context7) `⭐51.4k` - Context7 MCP Server -- Up-to-date code documentation for LLMs and AI code editors
- [mcp-use/mcp-use](https://github.com/mcp-use/mcp-use) `⭐9.6k` - The fullstack MCP framework to develop MCP Apps for ChatGPT / Claude & MCP Servers for AI Agents
- [mindsdb/mindsdb](https://github.com/mindsdb/mindsdb) `⭐38.9k` - Federated Query Engine for AI - The only MCP Server you'll ever need
- [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) `⭐24.2k` - The fast, Pythonic way to build MCP servers and clients
- [coleam00/mcp-crawl4ai-rag](https://github.com/coleam00/mcp-crawl4ai-rag) `⭐2.1k` - Web Crawling and RAG Capabilities for AI Agents and AI Coding Assistants
- [sadiuysal/crawl4ai-mcp-server](https://github.com/sadiuysal/crawl4ai-mcp-server) `⭐69` - A lightweight MCP server that exposes Crawl4AI web scraping capabilities
- [adhikasp/mcp-client-cli](https://github.com/adhikasp/mcp-client-cli) `⭐672` - A simple CLI to run LLM prompt and implement MCP client
- [adhikasp/mcp-git-ingest](https://github.com/adhikasp/mcp-git-ingest) `⭐302` - A MCP server that helps read GitHub repository structure and important files
- [antvis/mcp-server-chart](https://github.com/antvis/mcp-server-chart) `⭐3.9k` - A visualization mcp & skills contains 25+ visual charts using @antvis
- [VikashLoomba/copilot-mcp](https://github.com/VikashLoomba/copilot-mcp) `⭐482` - A VSCode extension for finding and installing Agent Skills and MCP Apps
- [steipete/claude-code-mcp](https://github.com/steipete/claude-code-mcp) `⭐1.2k` - Claude Code as one-shot MCP server to have an agent in your agent
- [supercorp-ai/supergateway](https://github.com/supercorp-ai/supergateway) `⭐2.5k` - Run MCP stdio servers over SSE and SSE over stdio. AI gateway
- [larksuite/cli](https://github.com/larksuite/cli) `⭐6.5k` - Official Lark/Feishu CLI built for humans and AI Agents. 200+ commands, 20 Agent Skills covering Messenger, Docs, Base, Sheets, Calendar, Mail, Meetings and more
- [ronaldmego/openmetadata-mcp-agent](https://github.com/ronaldmego/openmetadata-mcp-agent) - Conversational AI agent for OpenMetadata data catalogs. 27 MCP tools (read + write) — ask in natural language, govern your metadata directly ⭐ OSS
- [ronaldmego/matomo-mcp-agent](https://github.com/ronaldmego/matomo-mcp-agent) - Talk to your Matomo analytics in natural language. MCP server + Streamlit chat UI powered by LangChain and Gemini ⭐ OSS

### 🎯 Orchestration & Multi-Agent

- [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) `⭐18.7k` - Agent harness built with LangChain and LangGraph. Planning tool, filesystem backend, and sub-agent spawning out of the box
- [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) `⭐47.8k` - Framework for orchestrating role-playing, autonomous AI agents
- [langflow-ai/langflow](https://github.com/langflow-ai/langflow) `⭐146.5k` - Langflow is a powerful tool for building and deploying AI-powered agents and workflows
- [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) `⭐51.4k` - Build AI Agents, Visually
- [wshobson/agents](https://github.com/wshobson/agents) `⭐32.8k` - Intelligent automation and multi-agent orchestration for Claude Code
- [The-Pocket/PocketFlow](https://github.com/The-Pocket/PocketFlow) `⭐10.3k` - Pocket Flow: 100-line LLM framework. Let Agents build Agents!
- [MotiaDev/motia](https://github.com/MotiaDev/motia) `⭐15.2k` - Multi-Language Backend Framework that unifies APIs, background jobs, queues, workflows, streams, and AI agents
- [simstudioai/sim](https://github.com/simstudioai/sim) `⭐27.4k` - Build, deploy, and orchestrate AI agents. Sim is the central intelligence layer for your AI workforce
- [agno-agi/agno](https://github.com/agno-agi/agno) `⭐39.1k` - The programming language for agentic software. Build, run, and manage multi-agent systems at scale
- [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) `⭐5.7k` - Spawn parallel AI coding agents, each in its own git worktree. Agents fix CI failures, address review comments, and open PRs autonomously. Agent-agnostic (Claude Code, Codex, Aider)
- [666ghj/MiroFish](https://github.com/666ghj/MiroFish) `⭐48.8k` - Swarm intelligence engine that builds a high-fidelity digital world from real-world signals (news, policies, financial data) and simulates thousands of agents to predict future trajectories
- [TransformerOptimus/SuperAGI](https://github.com/TransformerOptimus/SuperAGI) `⭐17.4k` - A dev-first open source autonomous AI agent framework
- [Pythagora-io/gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) `⭐33.8k` - The first real AI developer
- [Danau5tin/multi-agent-coding-system](https://github.com/Danau5tin/multi-agent-coding-system) `⭐1.4k` - Reached #13 on Stanford's Terminal Bench leaderboard. Orchestrator, explorer & coder agents
- [docker/compose-for-agents](https://github.com/docker/compose-for-agents) `⭐900` - Build and run AI agents using Docker Compose
- [coleam00/ottomator-agents](https://github.com/coleam00/ottomator-agents) `⭐5.5k` - All the open source AI Agents hosted on the oTTomator Live Agent Studio platform
- [coleam00/pydantic-ai-github-agent](https://github.com/coleam00/pydantic-ai-github-agent) `⭐65` - The agent built for AI Agents series on YouTube
- [coleam00/PydanticAI-Research-Agent](https://github.com/coleam00/PydanticAI-Research-Agent) `⭐131` - Pydantic AI Research Agent Built with the PRP Framework Template
- [kortix-ai/suna](https://github.com/kortix-ai/suna) `⭐19.6k` - Kortix – build, manage and train AI Agents
- [The-Pocket/PocketFlow-Tutorial-Codebase-Knowledge](https://github.com/The-Pocket/PocketFlow-Tutorial-Codebase-Knowledge) `⭐12.2k` - Pocket Flow: Codebase to Tutorial
- [VRSEN/agency-swarm](https://github.com/VRSEN/agency-swarm) `⭐4.1k` - Reliable Multi-Agent Orchestration Framework based on the IETF's agency-spec

### 📝 Memory & RAG

- [mem0ai/mem0](https://github.com/mem0ai/mem0) `⭐51.8k` - Universal memory layer for AI Agents
- [getzep/graphiti](https://github.com/getzep/graphiti) `⭐24.4k` - Build Real-Time Knowledge Graphs for AI Agents
- [topoteretes/cognee](https://github.com/topoteretes/cognee) `⭐14.9k` - Knowledge Engine for AI Agent Memory in 6 lines of code
- [campfirein/cipher](https://github.com/campfirein/cipher) `⭐3.6k` - Byterover Cipher is an opensource memory layer specifically designed for coding agents
- [infiniflow/ragflow](https://github.com/infiniflow/ragflow) `⭐76.9k` - RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine
- [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) `⭐14.8k` - RAG-Anything: All-in-One RAG Framework
- [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) `⭐31.5k` - LightRAG: Simple and Fast Retrieval-Augmented Generation
- [raphaelmansuy/edgequake](https://github.com/raphaelmansuy/edgequake) `⭐1.6k` - High-performance GraphRAG inspired from LightRag written in Rust
- [yichuan-w/LEANN](https://github.com/yichuan-w/LEANN) `⭐10.4k` - RAG on Everything with LEANN. Enjoy 97% storage savings while running a fast, accurate, and 100% private RAG application
- [airweave-ai/airweave](https://github.com/airweave-ai/airweave) `⭐6.2k` - Open-source context retrieval layer for AI agents
- [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) `⭐21.3k` - Zero-server code intelligence engine — client-side knowledge graph creator with built-in Graph RAG Agent for code exploration

### 💬 Conversational & Chat

- [emcie-co/parlant](https://github.com/emcie-co/parlant) `⭐17.9k` - LLM agents built for control. Designed for real-world use. Deployed in minutes
- [janhq/jan](https://github.com/janhq/jan) `⭐41.4k` - Jan is an open source alternative to ChatGPT that runs 100% offline on your computer
- [openinterpreter/open-interpreter](https://github.com/openinterpreter/open-interpreter) `⭐63.0k` - A natural language interface for computers
- [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) `⭐29.9k` - The Frontend for Agents & Generative UI. React + Angular
- [ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui) `⭐12.8k` - AG-UI: the Agent-User Interaction Protocol. Bring Agents into Frontend Applications
- [open-webui/open-webui](https://github.com/open-webui/open-webui) `⭐129.6k` - User-friendly AI Interface (Supports Ollama, OpenAI API, ...)
- [Anything-LLM/anything-llm](https://github.com/Mintplex-Labs/anything-llm) `⭐57.4k` - The all-in-one Desktop & Docker AI application with built-in RAG, AI agents
- [letta-ai/letta](https://github.com/letta-ai/letta) `⭐21.9k` - Letta is the platform for building stateful agents: AI with advanced memory
- [Jackywine/Bella](https://github.com/Jackywine/Bella) `⭐6.4k` - Bella is best
- [Doriandarko/kimi-writer](https://github.com/Doriandarko/kimi-writer) `⭐545` - AI writing agent powered by kimi-k2-thinking

### 🌐 Browser & Web Agents

- [browser-use/browser-use](https://github.com/browser-use/browser-use) `⭐85.6k` - Make websites accessible for AI agents. Automate tasks online with ease
- [browserbase/stagehand](https://github.com/browserbase/stagehand) `⭐21.8k` - The AI Browser Automation Framework
- [Fosowl/agenticSeek](https://github.com/Fosowl/agenticSeek) `⭐25.8k` - Fully Local Manus AI. No APIs, No $200 monthly bills. Enjoy an autonomous agent that thinks, browses the web, and code
- [aaronjmars/opendia](https://github.com/aaronjmars/opendia) `⭐1.8k` - Connect your browser to AI models. Just use Dia on Chrome, Arc or Firefox
- [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) `⭐26.2k` - An autonomous agent that conducts deep research on any data using any LLM providers

### 🏠 Personal AI Assistants & Gateways

- [openclaw/openclaw](https://github.com/openclaw/openclaw) `⭐345.5k` - Your own personal AI assistant. Any OS. Any Platform. The lobster way
- [paperclipai/paperclip](https://github.com/paperclipai/paperclip) `⭐44.5k` - Open-source orchestration for zero-human companies. If OpenClaw is an employee, Paperclip is the company — org charts, budgets, goals, and agent coordination in one dashboard
- [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) `⭐18.2k` - Run OpenClaw more securely inside NVIDIA OpenShell with managed inference and sandboxed isolation
- [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) `⭐22.2k` - Self-improving AI agent with built-in learning loop, user modeling, and OpenClaw migration support

### 📚 Agent Resources & Guides

- [open-gitagent/gitagent](https://github.com/open-gitagent/gitagent) `⭐2.5k` - Framework-agnostic, git-native standard for defining AI agents. Clone a repo, get an agent. Export to Claude Code, OpenAI, CrewAI, LangChain, and more
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) `⭐35.7k` - A curated list of awesome skills, hooks, slash-commands, agent orchestrators, applications, and plugins for Claude Code
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) `⭐104.3k` - Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models
- [coleam00/context-engineering-intro](https://github.com/coleam00/context-engineering-intro) `⭐13.0k` - Context engineering is the new vibe coding - it's the way to actually make AI coding assistants work
- [Cranot/claude-code-guide](https://github.com/Cranot/claude-code-guide) `⭐2.6k` - The Complete Claude Code CLI Guide - Live & Auto-Updated Every 2 Days
- [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) `⭐30.8k` - Best practices and tips for Claude Code — agentic engineering patterns, vibe coding workflows
- [coleam00/ai-agents-masterclass](https://github.com/coleam00/ai-agents-masterclass) `⭐3.3k` - Follow along with my AI Agents Masterclass videos! All of the code I create and use in this series
- [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) `⭐33.1k` - In-depth tutorials on LLMs, RAGs and real-world AI agent applications
- [SamurAIGPT/awesome-openclaw](https://github.com/SamurAIGPT/awesome-openclaw) `⭐851` - A curated list of awesome OpenClaw resources, tools, skills, tutorials, and articles
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) `⭐50.5k` - A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows
- [BehiSecc/awesome-claude-skills](https://github.com/BehiSecc/awesome-claude-skills) `⭐8.1k` - A curated list of Claude Skills
- [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) `⭐17.1k` - A set of ready to use scientific skills for Claude
- [Kamalnrf/claude-plugins](https://github.com/Kamalnrf/claude-plugins) `⭐489` - Lightweight registry to discover, install, and manage all public Claude plugins and agent skills
- [anthropics/skills](https://github.com/anthropics/skills) `⭐109.0k` - Public repository for Agent Skills
- [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) `⭐15.8k` - Official, Anthropic-managed directory of high quality Claude Code Plugins
- [google-gemini/gemini-skills](https://github.com/google-gemini/gemini-skills) `⭐3.1k` - Skills for the Gemini API, SDK and model/agent interactions
- [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) `⭐24.0k` - CLI tool for configuring and monitoring Claude Code
- [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) `⭐26.4k` - An AI-powered task-management system you can drop into Cursor, Lovable, Windsurf, Roo, and others
- [coleam00/Archon](https://github.com/coleam00/Archon) `⭐13.9k` - Beta release of Archon OS - the knowledge and task management backbone for AI coding assistants
- [danielmiessler/Fabric](https://github.com/danielmiessler/Fabric) `⭐40.3k` - Fabric is an open-source framework for augmenting humans using AI


## 🏛️ Data Governance & Observability

- [open-metadata/OpenMetadata](https://github.com/open-metadata/OpenMetadata) `⭐9.3k` - Unified metadata platform for data discovery, data observability, and data governance, powered by a central metadata repository
- [datahub-project/datahub](https://github.com/datahub-project/datahub) `⭐11.8k` - The Metadata Platform for your Data and AI — data discovery, lineage, and governance at scale
- [OpenLineage/OpenLineage](https://github.com/OpenLineage/OpenLineage) `⭐2.4k` - An open standard for metadata and lineage collection. Track data pipeline jobs, datasets, and runs
- [great-expectations/great_expectations](https://github.com/great-expectations/great_expectations) `⭐11.3k` - The leading open-source data quality framework. Define, document, and validate data expectations
- [sodadata/soda-core](https://github.com/sodadata/soda-core) `⭐2.3k` - Data quality testing and monitoring for SQL, Spark, and Pandas. Run checks directly in your pipelines
- [apache/atlas](https://github.com/apache/atlas) `⭐2.1k` - Apache Atlas provides open metadata management and governance capabilities for organizations that need to build a catalog of their data assets
- [ronaldmego/agent-data-analyst](https://github.com/ronaldmego/agent-data-analyst) - AI data analyst that reads governance context (OpenMetadata) before running SQL. Profiles tables, classifies variables, detects anomalies — governance-informed analytics, 100% local ⭐ OSS

## 🛡️ AI Safety & Responsible AI

- [intuitem/ciso-assistant-community](https://github.com/intuitem/ciso-assistant-community) `⭐3.9k` - One-stop-shop GRC platform for Risk Management, AppSec, Compliance & Audit, TPRM, Privacy. Supports 130+ frameworks: ISO 27001, NIST CSF, SOC 2, PCI DSS, GDPR, HIPAA, and more
- [guardrails-ai/guardrails](https://github.com/guardrails-ai/guardrails) `⭐6.6k` - Adding guardrails to large language models. Validate and structure LLM outputs with programmable rules
- [NVIDIA/NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) `⭐5.9k` - Open-source toolkit for easily adding programmable guardrails to LLM-based conversational AI
- [Trusted-AI/AIF360](https://github.com/Trusted-AI/AIF360) `⭐2.8k` - IBM AI Fairness 360 — comprehensive fairness metrics for datasets and ML models
- [microsoft/responsible-ai-toolbox](https://github.com/microsoft/responsible-ai-toolbox) `⭐1.7k` - Responsible AI dashboard and tools for model and data exploration, error analysis, and fairness assessment
- [whylabs/langkit](https://github.com/whylabs/langkit) `⭐980` - Open-source toolkit for monitoring Large Language Models — detect toxicity, hallucinations, and data quality issues

## 🎨 Avatar, Video & Image AI

- [jamiepine/voicebox](https://github.com/jamiepine/voicebox) `⭐14.4k` - The open-source voice synthesis studio powered by Qwen3-TTS
- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) `⭐107.6k` - The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface
- [ZeroLu/awesome-nanobanana-pro](https://github.com/ZeroLu/awesome-nanobanana-pro) `⭐9.6k` - An awesome list of curated Nano Banana pro prompts and examples
- [PicoTrex/Awesome-Nano-Banana-images](https://github.com/PicoTrex/Awesome-Nano-Banana-images) `⭐21.9k` - A curated collection of fun and creative examples generated with Nano Banana & Nano Banana Pro
- [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox) `⭐24.1k` - SoTA open-source TTS
- [facefusion/facefusion-docker](https://github.com/facefusion/facefusion-docker) `⭐524` - Industry leading face manipulation platform
- [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) `⭐28.0k` - Automate the process of making money online

## 📊 Data Engineering & Analytics
- [FalkorDB/QueryWeaver](https://github.com/FalkorDB/QueryWeaver) `⭐796` - Open-source Text2SQL tool that transforms natural language into SQL using graph-powered schema understanding

- [DataExpert-io/data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) `⭐40.8k` - This is a repo with links to everything you'd ever want to learn about data engineering
- [dlt-hub/dlt](https://github.com/dlt-hub/dlt) `⭐5.2k` - data load tool (dlt) is an open source Python library that makes data loading easy
- [igorbarinov/awesome-data-engineering](https://github.com/igorbarinov/awesome-data-engineering) `⭐8.4k` - A curated list of data engineering tools for software developers
- [gunnarmorling/awesome-opensource-data-engineering](https://github.com/gunnarmorling/awesome-opensource-data-engineering) `⭐3.1k` - An Awesome List of Open-Source Data Engineering Projects
- [Countly/countly-server](https://github.com/Countly/countly-server) `⭐5.8k` - Countly is a privacy-first, AI-powered analytics and engagement platform
- [tensorlakeai/tensorlake](https://github.com/tensorlakeai/tensorlake) `⭐895` - Tensorlake is a Document Ingestion API and a serverless platform for building data processing
- [weaviate/elysia](https://github.com/weaviate/elysia) `⭐1.9k` - Python package and backend for the Elysia platform app
- [mito-ds/mito](https://github.com/mito-ds/mito) `⭐2.6k` - Jupyter extensions that help you write code faster: Context aware AI Chat, Autocomplete, and Spreadsheet
- [pixeltable/pixeltable](https://github.com/pixeltable/pixeltable) `⭐1.6k` - Data Infrastructure providing a declarative, incremental approach for multimodal AI workloads
- [chartdb/chartdb](https://github.com/chartdb/chartdb) `⭐21.7k` - Database diagrams editor that allows you to visualize and design your DB with a single query
- [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core) `⭐12.5k` - dbt enables data analysts and engineers to transform their data using the same practices that software engineers use
- [valkey-io/valkey](https://github.com/valkey-io/valkey) `⭐25.3k` - A flexible distributed key-value database that is optimized for caching and other realtime workloads
- [grafana/grafana](https://github.com/grafana/grafana) `⭐72.9k` - The open and composable observability and data visualization platform
- [elastic/elasticsearch](https://github.com/elastic/elasticsearch) `⭐76.4k` - Free and Open Source, Distributed, RESTful Search Engine
- [trinodb/trino](https://github.com/trinodb/trino) `⭐12.7k` - Official repository of Trino, the distributed SQL query engine for big data
- [apache/superset](https://github.com/apache/superset) `⭐72.2k` - Apache Superset is a Data Visualization and Data Exploration Platform
- [microsoft/data-formulator](https://github.com/microsoft/data-formulator) `⭐15.2k` - Create rich visualizations with AI
- [vllm-project/vllm](https://github.com/vllm-project/vllm) `⭐75.0k` - A high-throughput and memory-efficient inference and serving engine for LLMs
- [Openpanel-dev/openpanel](https://github.com/Openpanel-dev/openpanel) `⭐5.6k` - OpenPanel is an open-source web and product analytics platform
- [Canner/WrenAI](https://github.com/Canner/WrenAI) `⭐14.8k` - GenBI (Generative BI) queries any database in natural language, generates accurate SQL, charts
- [sinaptik-ai/pandas-ai](https://github.com/sinaptik-ai/pandas-ai) `⭐23.4k` - Chat with your database or your datalake (SQL, CSV, parquet)
- [vanna-ai/vanna](https://github.com/vanna-ai/vanna) `⭐23.2k` - Chat with your SQL database. Accurate Text-to-SQL Generation via LLMs using Agentic Retrieval
- [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) `⭐65.0k` - Financial data platform for analysts, quants and AI agents
- [ganttrify](https://github.com/ganttrify/ganttrify) - Create beautiful Gantt charts with ggplot2
- [Avaiga/taipy](https://github.com/Avaiga/taipy) `⭐19.1k` - Turns Data and AI algorithms into production-ready web applications in no time
- [mckinsey/vizro](https://github.com/mckinsey/vizro) `⭐3.6k` - Vizro is a low-code toolkit for building high-quality data visualization apps

## 🧠 ML & Data Science

- [KalyanM45/AI-Project-Gallery](https://github.com/KalyanM45/AI-Project-Gallery) `⭐4.6k` - Repository containing Artificial Intelligence Projects such as Machine Learning, Deep Learning and Generative AI
- [google/langextract](https://github.com/google/langextract) `⭐35.0k` - A Python library for extracting structured information from unstructured text using LLMs
- [lyogavin/airllm](https://github.com/lyogavin/airllm) `⭐14.7k` - AirLLM 70B inference with single 4GB GPU
- [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) `⭐11.0k` - DeepTutor: AI-Powered Personalized Learning Assistant
- [Sumanth077/ai-engineering-toolkit](https://github.com/Sumanth077/ai-engineering-toolkit) `⭐3.0k` - A curated list of 100+ libraries and frameworks for AI engineers building with LLMs
- [microsoft/BitNet](https://github.com/microsoft/BitNet) `⭐37.0k` - Official inference framework for 1-bit LLMs
- [cvs-health/uqlm](https://github.com/cvs-health/uqlm) `⭐1.1k` - UQLM: Uncertainty Quantification for Language Models, is a Python package for UQ-based LLM hallucination detection
- [confident-ai/deepeval](https://github.com/confident-ai/deepeval) `⭐14.4k` - The LLM Evaluation Framework
- [google-research/timesfm](https://github.com/google-research/timesfm) `⭐14.0k` - Time Series Foundation Model by Google Research. Pretrained for zero-shot forecasting, 200M params, available in BigQuery. ICML 2024 paper
- [OpenBMB/MiniCPM-o](https://github.com/OpenBMB/MiniCPM-o) `⭐24.3k` - A Gemini 2.5 Flash Level MLLM for Vision, Speech, and Full-Duplex Multimodal Live Streaming
- [mistralai/cookbook](https://github.com/mistralai/cookbook) `⭐2.2k` - Mistral AI cookbook
- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) `⭐219.2k` - All Algorithms implemented in Python
- [KalyanKS-NLP/llm-engineer-toolkit](https://github.com/KalyanKS-NLP/llm-engineer-toolkit) `⭐10.1k` - A curated list of 120+ LLM libraries category wise
- [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) `⭐102.8k` - The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data
- [academic/awesome-datascience](https://github.com/academic/awesome-datascience) `⭐28.7k` - An awesome Data Science repository to learn and apply for real world problems
- [hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory) `⭐69.4k` - Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)
- [Machine-Learning-Tokyo/Interactive_Tools](https://github.com/Machine-Learning-Tokyo/Interactive_Tools) `⭐2.8k` - Interactive Tools for Machine Learning, Deep Learning and Math
- [rushter/MLAlgorithms](https://github.com/rushter/MLAlgorithms) `⭐11.0k` - Minimal and clean examples of machine learning algorithms implementations
- [jivoi/awesome-ml-for-cybersecurity](https://github.com/jivoi/awesome-ml-for-cybersecurity) `⭐8.4k` - Machine Learning for Cyber Security
- [roboticcam/machine-learning-notes](https://github.com/roboticcam/machine-learning-notes) `⭐9.6k` - My continuously updated Machine Learning, Probabilistic Models and Deep Learning notes and demos
- [ml-tooling/ml-workspace](https://github.com/ml-tooling/ml-workspace) `⭐3.5k` - All-in-one web-based IDE specialized for machine learning and data science
- [lukasmasuch/best-of-ml-python](https://github.com/lukasmasuch/best-of-ml-python) `⭐23.4k` - A ranked list of awesome machine learning Python libraries. Updated weekly
- [EthicalML/awesome-production-machine-learning](https://github.com/EthicalML/awesome-production-machine-learning) `⭐20.3k` - A curated list of awesome open source libraries to deploy, monitor, version and scale your machine learning
- [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) `⭐72.1k` - A curated list of awesome Machine Learning frameworks, libraries and software
- [eugeneyan/applied-ml](https://github.com/eugeneyan/applied-ml) `⭐28.8k` - Papers & tech blogs by companies sharing their work on data science & machine learning in production
- [GokuMohandas/Made-With-ML](https://github.com/GokuMohandas/Made-With-ML) `⭐47.1k` - Learn how to design, develop, deploy and iterate on production-grade ML applications
- [posit-dev/positron](https://github.com/posit-dev/positron) `⭐4.0k` - Positron, a next-generation data science IDE
- [fixie-ai/ultravox](https://github.com/fixie-ai/ultravox) `⭐4.4k` - A fast multimodal LLM for real-time voice
- [developersdigest/llm-answer-engine](https://github.com/developersdigest/llm-answer-engine) `⭐5.0k` - Perplexity Inspired Answer Engine
- [unslothai/notebooks](https://github.com/unslothai/notebooks) `⭐5.1k` - Jupyter notebooks demonstrating LLM fine-tuning with Unsloth AI for efficient model training

📚 **New to ML?** Check out [Learning & Reference](#-learning--reference) for courses and tutorials.

## 🛠️ DevTools & Infrastructure

- [CapSoftware/Cap](https://github.com/CapSoftware/Cap) `⭐17.8k` - Open source Loom alternative. Beautiful, shareable screen recordings
- [bitnami/containers](https://github.com/bitnami/containers) `⭐4.4k` - Bitnami container images
- [kottster/kottster](https://github.com/kottster/kottster) `⭐1.1k` - Instant Node.js admin panel. Secure, self-hosted, and easy to set up
- [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) `⭐283.5k` - A list of Free Software network services and web applications which can be hosted on your own servers
- [coollabsio/coolify](https://github.com/coollabsio/coolify) `⭐52.5k` - An open-source, self-hostable PaaS alternative to Vercel, Heroku & Netlify
- [herin7/gitforme](https://github.com/herin7/gitforme) `⭐381` - AI-powered GitHub code explorer — understand any repo in minutes, not days
- [coderamp-labs/gitingest](https://github.com/coderamp-labs/gitingest) `⭐14.2k` - Replace 'hub' with 'ingest' in any GitHub URL to get a prompt-friendly extract of a codebase
- [ahmedkhaleel2004/gitdiagram](https://github.com/ahmedkhaleel2004/gitdiagram) `⭐15.4k` - Free, simple, fast interactive diagrams for any GitHub repository
- [balena-io/open-balena](https://github.com/balena-io/open-balena) `⭐1.2k` - Open source software to manage connected IoT devices at scale
- [enescingoz/awesome-n8n-templates](https://github.com/enescingoz/awesome-n8n-templates) `⭐20.8k` - Supercharge your workflow automation with this curated collection of n8n templates
- [lucaswalter/n8n-ai-automations](https://github.com/lucaswalter/n8n-ai-automations) `⭐1.4k` - Collection of n8n workflows, n8n templates, AI automations, and AI agents
- [Zie619/n8n-workflows](https://github.com/Zie619/n8n-workflows) `⭐53.5k` - all of the workflows of n8n i could find
- [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) `⭐6.8k` - Command-line interface for Playwright, a browser automation tool with AI capabilities
- [restyler/awesome-n8n](https://github.com/restyler/awesome-n8n) `⭐2.8k` - Useful n8n resources: list of community nodes and tutorials
- [n8n-io/n8n](https://github.com/n8n-io/n8n) `⭐182.1k` - Fair-code workflow automation platform with native AI capabilities
- [kuchin/awesome-cto](https://github.com/kuchin/awesome-cto) `⭐34.6k` - A curated and opinionated list of resources for Chief Technology Officers
- [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) `⭐20.8k` - Right-size LLM models to your hardware. Detects CPU, RAM, GPU and scores models by quality, speed, fit and context. Supports Ollama, llama.cpp, MLX

## 🌐 Web & Apps

- [TailAdmin/free-nextjs-admin-dashboard](https://github.com/TailAdmin/free-nextjs-admin-dashboard) `⭐2.4k` - TailAdmin is a Next.js and Tailwind CSS free, open-source admin dashboard template
- [Nutlope/self.so](https://github.com/Nutlope/self.so) `⭐2.9k` - LinkedIn -> personal site generator
- [toon-format/toon](https://github.com/toon-format/toon) `⭐23.6k` - Token-Oriented Object Notation (TOON) – Compact, human-readable, schema-aware JSON for LLM prompts
- [superdesigndev/superdesign](https://github.com/superdesigndev/superdesign) `⭐6.3k` - AI Product Design Agent - Open Source
- [iliane5/meridian](https://github.com/iliane5/meridian) `⭐2.4k` - Meridian cuts through news noise by scraping hundreds of sources, analyzing stories with AI

## 📚 Learning & Reference

*Educational resources, courses, and tutorials organized by topic.*

> **📖 Categorization Guide:** Courses, tutorials, and learning resources go here. Tools, frameworks, and production libraries belong in their respective technical categories (e.g., 🧠 ML & Data Science). See [Contributing](#contributing) for details.

### Data Science & ML
- [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) `⭐84.9k` - 12 weeks, 26 lessons, 52 quizzes, classic Machine Learning for all
- [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners) `⭐34.7k` - 10 Weeks, 20 Lessons, Data Science for All!
- [ageron/handson-ml3](https://github.com/ageron/handson-ml3) `⭐12.8k` - A series of Jupyter notebooks that walk you through the fundamentals of Machine Learning and Deep Learning
- [d2l-ai/d2l-en](https://github.com/d2l-ai/d2l-en) `⭐28.5k` - Interactive deep learning book with multi-framework code, math, and discussions
- [Avik-Jain/100-Days-Of-ML-Code](https://github.com/Avik-Jain/100-Days-Of-ML-Code) `⭐50.2k` - 100 Days of Machine Learning Coding
- [mml-book/mml-book.github.io](https://github.com/mml-book/mml-book.github.io) `⭐15.3k` - Companion webpage to the book "Mathematics For Machine Learning"
- [karpathy/nn-zero-to-hero](https://github.com/karpathy/nn-zero-to-hero) `⭐21.2k` - Neural networks: zero to hero
- [ujjwalkarn/Machine-Learning-Tutorials](https://github.com/ujjwalkarn/Machine-Learning-Tutorials) `⭐17.7k` - Machine learning and deep learning tutorials, articles and other resources
- [khangich/machine-learning-interview](https://github.com/khangich/machine-learning-interview) `⭐12.4k` - Machine Learning Interviews from FAANG, Snapchat, LinkedIn

### AI & Agents
- [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) `⭐108.8k` - 21 Lessons, Get Started Building with Generative AI
- [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) `⭐55.7k` - 10 Lessons to Get Started Building AI Agents
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) `⭐72.7k` - Guides, papers, lectures, notebooks and resources for prompt engineering
- [HandsOnLLM/Hands-On-Large-Language-Models](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models) `⭐24.7k` - Official code repo for the O'Reilly Book - Hands-On Large Language Models
- [NirDiamant/GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents) `⭐20.9k` - This repository provides a comprehensive collection of tutorials and implementations for Generative AI Agents
- [NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) `⭐26.4k` - This repository provides a comprehensive collection of tutorials and implementations for Retrieval-Augmented Generation (RAG) systems
- [labmlai/annotated_deep_learning_papers](https://github.com/labmlai/annotated_deep_learning_papers) - Annotated Deep Learning Papers

### NLP & RL
- [keon/awesome-nlp](https://github.com/keon/awesome-nlp) `⭐18.4k` - A curated list of resources dedicated to Natural Language Processing
- [aikorea/awesome-rl](https://github.com/aikorea/awesome-rl) `⭐9.7k` - Reinforcement learning resources curated
- [FareedKhan-dev/all-rl-algorithms](https://github.com/FareedKhan-dev/all-rl-algorithms) `⭐1.5k` - Implementations of all major Reinforcement Learning algorithms

### Programming & General
- [Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) `⭐60.4k` - The 30 Days of Python programming challenge is a step-by-step guide to learn the Python programming language
- [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) `⭐440.5k` - freeCodeCamp.org's open-source codebase and curriculum
- [trekhleb/learn-python](https://github.com/trekhleb/learn-python) `⭐17.8k` - Playground and cheatsheet for learning Python
- [Fechin/reference](https://github.com/Fechin/reference) `⭐10.3k` - Share quick reference cheat sheet for developers
- [addyosmani/gemini-cli-tips](https://github.com/addyosmani/gemini-cli-tips) `⭐2.3k` - Gemini CLI Tips and Tricks
- [sindresorhus/awesome](https://github.com/sindresorhus/awesome) `⭐451.1k` - Awesome lists about all kinds of interesting topics
- [public-apis/public-apis](https://github.com/public-apis/public-apis) `⭐418.3k` - A collective list of free APIs

## 🔍 OCR & Document Processing

- [rednote-hilab/dots.ocr](https://github.com/rednote-hilab/dots.ocr) `⭐8.2k` - Multilingual Document Layout Parsing in a Single Vision-Language Model
- [datalab-to/chandra](https://github.com/datalab-to/chandra) `⭐8.2k` - OCR model that handles complex tables, forms, handwriting with full layout
- [google/A2UI](https://github.com/google/A2UI) `⭐13.8k` - Advanced UI understanding model
- [ngafar/llama-scan](https://github.com/ngafar/llama-scan) `⭐818` - Transcribe PDFs with local LLMs
- [AnswerDotAI/clipmd](https://github.com/AnswerDotAI/clipmd) `⭐220` - Convert clipboard from HTML to MD
- [allenai/olmocr](https://github.com/allenai/olmocr) `⭐17.1k` - Toolkit for linearizing PDFs for LLM datasets/training
- [deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR) `⭐22.8k` - Contexts Optical Compression
- [bytedance/Dolphin](https://github.com/bytedance/Dolphin) `⭐8.9k` - The official repo for "Dolphin: Document Image Parsing via Heterogeneous Anchor Prompting"
- [microsoft/markitdown](https://github.com/microsoft/markitdown) `⭐93.2k` - Python tool for converting files and office documents to Markdown
- [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) `⭐63.2k` - Open-source LLM Friendly Web Crawler & Scraper
- [docling-project/docling](https://github.com/docling-project/docling) `⭐56.9k` - Get your documents ready for gen AI
- [jdepoix/youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) `⭐7.2k` - This is a python API which allows you to get the transcript/subtitles for a given YouTube video

## 📝 Content & Productivity

- [HKUDS/Paper2Slides](https://github.com/HKUDS/Paper2Slides) `⭐3.3k` - Paper2Slides: From Paper to Presentation in One Click
- [AsyncFuncAI/deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open) `⭐15.3k` - Open Source DeepWiki: AI-Powered Wiki Generator for GitHub/Gitlab/Bitbucket Repositories

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