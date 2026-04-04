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

- [anthropics/claude-code ⭐105.2k](https://github.com/anthropics/claude-code) - Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster
- [google-gemini/gemini-cli ⭐100.0k](https://github.com/google-gemini/gemini-cli) - An open-source AI agent that brings the power of Gemini directly into your terminal
- [openai/codex ⭐72.4k](https://github.com/openai/codex) - Lightweight coding agent that runs in your terminal
- [QwenLM/qwen-code ⭐21.6k](https://github.com/QwenLM/qwen-code) - An open-source AI agent that lives in your terminal
- [bytedance/trae-agent ⭐11.2k](https://github.com/bytedance/trae-agent) - Trae Agent is an LLM-based agent for general purpose software engineering tasks
- [anomalyco/opencode ⭐135.5k](https://github.com/anomalyco/opencode) - The open source coding agent
- [HKUDS/DeepCode ⭐15.1k](https://github.com/HKUDS/DeepCode) - DeepCode: Open Agentic Coding (Paper2Code & Text2Web & Text2Backend)
- [BloopAI/vibe-kanban ⭐24.2k](https://github.com/BloopAI/vibe-kanban) - Get 10X more out of Claude Code, Codex or any coding agent
- [Yeachan-Heo/oh-my-claudecode ⭐23.0k](https://github.com/Yeachan-Heo/oh-my-claudecode) - Multi-agent orchestration for Claude Code. Zero learning curve — run parallel agents, define workflows, delegate tasks without learning internals
- [Gitlawb/openclaude ⭐10.5k](https://github.com/Gitlawb/openclaude) - Open-source Claude Code CLI for OpenAI, Gemini, DeepSeek, Ollama, and 200+ models via OpenAI-compatible APIs. Same terminal-first workflow, any provider

### 🔧 MCP Servers & Skills

- [punkpeye/awesome-mcp-servers ⭐84.1k](https://github.com/punkpeye/awesome-mcp-servers) - A collection of MCP servers
- [modelcontextprotocol/servers ⭐82.8k](https://github.com/modelcontextprotocol/servers) - Model Context Protocol Servers
- [supabase-community/supabase-mcp ⭐2.6k](https://github.com/supabase-community/supabase-mcp) - Connect Supabase to your AI assistants
- [idosal/git-mcp ⭐7.9k](https://github.com/idosal/git-mcp) - Put an end to code hallucinations! GitMCP is a free, open-source, remote MCP server for any GitHub project
- [czlonkowski/n8n-mcp ⭐17.3k](https://github.com/czlonkowski/n8n-mcp) - A MCP for Claude Desktop / Claude Code / Windsurf / Cursor to build n8n workflows for you
- [firecrawl/firecrawl-mcp-server ⭐5.9k](https://github.com/firecrawl/firecrawl-mcp-server) - Official Firecrawl MCP Server - Adds powerful web scraping and search to Cursor, Claude and any other LLM clients
- [googleapis/genai-toolbox ⭐13.6k](https://github.com/googleapis/genai-toolbox) - MCP Toolbox for Databases is an open source MCP server for databases
- [timescale/pg-aiguide ⭐1.7k](https://github.com/timescale/pg-aiguide) - MCP server and Claude plugin for Postgres skills and documentation
- [mongodb-js/mongodb-mcp-server ⭐987](https://github.com/mongodb-js/mongodb-mcp-server) - A Model Context Protocol server to connect to MongoDB databases and MongoDB Atlas Clusters
- [crystaldba/postgres-mcp ⭐2.5k](https://github.com/crystaldba/postgres-mcp) - Postgres MCP Pro provides configurable read/write access and performance analysis
- [leonardsellem/n8n-mcp-server ⭐1.6k](https://github.com/leonardsellem/n8n-mcp-server) - MCP server that provides tools and resources for interacting with n8n API
- [excalidraw/excalidraw-mcp ⭐3.7k](https://github.com/excalidraw/excalidraw-mcp) - Fast and streamable Excalidraw MCP App
- [upstash/context7 ⭐51.4k](https://github.com/upstash/context7) - Context7 MCP Server -- Up-to-date code documentation for LLMs and AI code editors
- [mcp-use/mcp-use ⭐9.6k](https://github.com/mcp-use/mcp-use) - The fullstack MCP framework to develop MCP Apps for ChatGPT / Claude & MCP Servers for AI Agents
- [mindsdb/mindsdb ⭐38.9k](https://github.com/mindsdb/mindsdb) - Federated Query Engine for AI - The only MCP Server you'll ever need
- [PrefectHQ/fastmcp ⭐24.2k](https://github.com/PrefectHQ/fastmcp) - The fast, Pythonic way to build MCP servers and clients
- [coleam00/mcp-crawl4ai-rag ⭐2.1k](https://github.com/coleam00/mcp-crawl4ai-rag) - Web Crawling and RAG Capabilities for AI Agents and AI Coding Assistants
- [sadiuysal/crawl4ai-mcp-server ⭐69](https://github.com/sadiuysal/crawl4ai-mcp-server) - A lightweight MCP server that exposes Crawl4AI web scraping capabilities
- [adhikasp/mcp-client-cli ⭐672](https://github.com/adhikasp/mcp-client-cli) - A simple CLI to run LLM prompt and implement MCP client
- [adhikasp/mcp-git-ingest ⭐302](https://github.com/adhikasp/mcp-git-ingest) - A MCP server that helps read GitHub repository structure and important files
- [antvis/mcp-server-chart ⭐3.9k](https://github.com/antvis/mcp-server-chart) - A visualization mcp & skills contains 25+ visual charts using @antvis
- [VikashLoomba/copilot-mcp ⭐482](https://github.com/VikashLoomba/copilot-mcp) - A VSCode extension for finding and installing Agent Skills and MCP Apps
- [steipete/claude-code-mcp ⭐1.2k](https://github.com/steipete/claude-code-mcp) - Claude Code as one-shot MCP server to have an agent in your agent
- [supercorp-ai/supergateway ⭐2.5k](https://github.com/supercorp-ai/supergateway) - Run MCP stdio servers over SSE and SSE over stdio. AI gateway
- [larksuite/cli ⭐6.5k](https://github.com/larksuite/cli) - Official Lark/Feishu CLI built for humans and AI Agents. 200+ commands, 20 Agent Skills covering Messenger, Docs, Base, Sheets, Calendar, Mail, Meetings and more
- [ronaldmego/openmetadata-mcp-agent](https://github.com/ronaldmego/openmetadata-mcp-agent) - Conversational AI agent for OpenMetadata data catalogs. 27 MCP tools (read + write) — ask in natural language, govern your metadata directly ⭐ OSS
- [ronaldmego/matomo-mcp-agent](https://github.com/ronaldmego/matomo-mcp-agent) - Talk to your Matomo analytics in natural language. MCP server + Streamlit chat UI powered by LangChain and Gemini ⭐ OSS

### 🎯 Orchestration & Multi-Agent

- [langchain-ai/deepagents ⭐18.7k](https://github.com/langchain-ai/deepagents) - Agent harness built with LangChain and LangGraph. Planning tool, filesystem backend, and sub-agent spawning out of the box
- [crewAIInc/crewAI ⭐47.8k](https://github.com/crewAIInc/crewAI) - Framework for orchestrating role-playing, autonomous AI agents
- [langflow-ai/langflow ⭐146.5k](https://github.com/langflow-ai/langflow) - Langflow is a powerful tool for building and deploying AI-powered agents and workflows
- [FlowiseAI/Flowise ⭐51.4k](https://github.com/FlowiseAI/Flowise) - Build AI Agents, Visually
- [wshobson/agents ⭐32.8k](https://github.com/wshobson/agents) - Intelligent automation and multi-agent orchestration for Claude Code
- [The-Pocket/PocketFlow ⭐10.3k](https://github.com/The-Pocket/PocketFlow) - Pocket Flow: 100-line LLM framework. Let Agents build Agents!
- [MotiaDev/motia ⭐15.2k](https://github.com/MotiaDev/motia) - Multi-Language Backend Framework that unifies APIs, background jobs, queues, workflows, streams, and AI agents
- [simstudioai/sim ⭐27.4k](https://github.com/simstudioai/sim) - Build, deploy, and orchestrate AI agents. Sim is the central intelligence layer for your AI workforce
- [agno-agi/agno ⭐39.1k](https://github.com/agno-agi/agno) - The programming language for agentic software. Build, run, and manage multi-agent systems at scale
- [ComposioHQ/agent-orchestrator ⭐5.7k](https://github.com/ComposioHQ/agent-orchestrator) - Spawn parallel AI coding agents, each in its own git worktree. Agents fix CI failures, address review comments, and open PRs autonomously. Agent-agnostic (Claude Code, Codex, Aider)
- [666ghj/MiroFish ⭐48.8k](https://github.com/666ghj/MiroFish) - Swarm intelligence engine that builds a high-fidelity digital world from real-world signals (news, policies, financial data) and simulates thousands of agents to predict future trajectories
- [TransformerOptimus/SuperAGI ⭐17.4k](https://github.com/TransformerOptimus/SuperAGI) - A dev-first open source autonomous AI agent framework
- [Pythagora-io/gpt-pilot ⭐33.8k](https://github.com/Pythagora-io/gpt-pilot) - The first real AI developer
- [Danau5tin/multi-agent-coding-system ⭐1.4k](https://github.com/Danau5tin/multi-agent-coding-system) - Reached #13 on Stanford's Terminal Bench leaderboard. Orchestrator, explorer & coder agents
- [docker/compose-for-agents ⭐900](https://github.com/docker/compose-for-agents) - Build and run AI agents using Docker Compose
- [coleam00/ottomator-agents ⭐5.5k](https://github.com/coleam00/ottomator-agents) - All the open source AI Agents hosted on the oTTomator Live Agent Studio platform
- [coleam00/pydantic-ai-github-agent ⭐65](https://github.com/coleam00/pydantic-ai-github-agent) - The agent built for AI Agents series on YouTube
- [coleam00/PydanticAI-Research-Agent ⭐131](https://github.com/coleam00/PydanticAI-Research-Agent) - Pydantic AI Research Agent Built with the PRP Framework Template
- [kortix-ai/suna ⭐19.6k](https://github.com/kortix-ai/suna) - Kortix – build, manage and train AI Agents
- [The-Pocket/PocketFlow-Tutorial-Codebase-Knowledge ⭐12.2k](https://github.com/The-Pocket/PocketFlow-Tutorial-Codebase-Knowledge) - Pocket Flow: Codebase to Tutorial
- [VRSEN/agency-swarm ⭐4.1k](https://github.com/VRSEN/agency-swarm) - Reliable Multi-Agent Orchestration Framework based on the IETF's agency-spec

### 📝 Memory & RAG

- [mem0ai/mem0 ⭐51.8k](https://github.com/mem0ai/mem0) - Universal memory layer for AI Agents
- [getzep/graphiti ⭐24.4k](https://github.com/getzep/graphiti) - Build Real-Time Knowledge Graphs for AI Agents
- [topoteretes/cognee ⭐14.9k](https://github.com/topoteretes/cognee) - Knowledge Engine for AI Agent Memory in 6 lines of code
- [campfirein/cipher ⭐3.6k](https://github.com/campfirein/cipher) - Byterover Cipher is an opensource memory layer specifically designed for coding agents
- [infiniflow/ragflow ⭐76.9k](https://github.com/infiniflow/ragflow) - RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine
- [HKUDS/RAG-Anything ⭐14.8k](https://github.com/HKUDS/RAG-Anything) - RAG-Anything: All-in-One RAG Framework
- [HKUDS/LightRAG ⭐31.5k](https://github.com/HKUDS/LightRAG) - LightRAG: Simple and Fast Retrieval-Augmented Generation
- [raphaelmansuy/edgequake ⭐1.6k](https://github.com/raphaelmansuy/edgequake) - High-performance GraphRAG inspired from LightRag written in Rust
- [yichuan-w/LEANN ⭐10.4k](https://github.com/yichuan-w/LEANN) - RAG on Everything with LEANN. Enjoy 97% storage savings while running a fast, accurate, and 100% private RAG application
- [airweave-ai/airweave ⭐6.2k](https://github.com/airweave-ai/airweave) - Open-source context retrieval layer for AI agents
- [abhigyanpatwari/GitNexus ⭐21.3k](https://github.com/abhigyanpatwari/GitNexus) - Zero-server code intelligence engine — client-side knowledge graph creator with built-in Graph RAG Agent for code exploration

### 💬 Conversational & Chat

- [emcie-co/parlant ⭐17.9k](https://github.com/emcie-co/parlant) - LLM agents built for control. Designed for real-world use. Deployed in minutes
- [janhq/jan ⭐41.4k](https://github.com/janhq/jan) - Jan is an open source alternative to ChatGPT that runs 100% offline on your computer
- [openinterpreter/open-interpreter ⭐63.0k](https://github.com/openinterpreter/open-interpreter) - A natural language interface for computers
- [CopilotKit/CopilotKit ⭐29.9k](https://github.com/CopilotKit/CopilotKit) - The Frontend for Agents & Generative UI. React + Angular
- [ag-ui-protocol/ag-ui ⭐12.8k](https://github.com/ag-ui-protocol/ag-ui) - AG-UI: the Agent-User Interaction Protocol. Bring Agents into Frontend Applications
- [open-webui/open-webui ⭐129.6k](https://github.com/open-webui/open-webui) - User-friendly AI Interface (Supports Ollama, OpenAI API, ...)
- [Anything-LLM/anything-llm ⭐57.4k](https://github.com/Mintplex-Labs/anything-llm) - The all-in-one Desktop & Docker AI application with built-in RAG, AI agents
- [letta-ai/letta ⭐21.9k](https://github.com/letta-ai/letta) - Letta is the platform for building stateful agents: AI with advanced memory
- [Jackywine/Bella ⭐6.4k](https://github.com/Jackywine/Bella) - Bella is best
- [Doriandarko/kimi-writer ⭐545](https://github.com/Doriandarko/kimi-writer) - AI writing agent powered by kimi-k2-thinking

### 🌐 Browser & Web Agents

- [browser-use/browser-use ⭐85.6k](https://github.com/browser-use/browser-use) - Make websites accessible for AI agents. Automate tasks online with ease
- [browserbase/stagehand ⭐21.8k](https://github.com/browserbase/stagehand) - The AI Browser Automation Framework
- [Fosowl/agenticSeek ⭐25.8k](https://github.com/Fosowl/agenticSeek) - Fully Local Manus AI. No APIs, No $200 monthly bills. Enjoy an autonomous agent that thinks, browses the web, and code
- [aaronjmars/opendia ⭐1.8k](https://github.com/aaronjmars/opendia) - Connect your browser to AI models. Just use Dia on Chrome, Arc or Firefox
- [assafelovic/gpt-researcher ⭐26.2k](https://github.com/assafelovic/gpt-researcher) - An autonomous agent that conducts deep research on any data using any LLM providers

### 🏠 Personal AI Assistants & Gateways

- [openclaw/openclaw ⭐345.5k](https://github.com/openclaw/openclaw) - Your own personal AI assistant. Any OS. Any Platform. The lobster way
- [paperclipai/paperclip ⭐44.5k](https://github.com/paperclipai/paperclip) - Open-source orchestration for zero-human companies. If OpenClaw is an employee, Paperclip is the company — org charts, budgets, goals, and agent coordination in one dashboard
- [NVIDIA/NemoClaw ⭐18.2k](https://github.com/NVIDIA/NemoClaw) - Run OpenClaw more securely inside NVIDIA OpenShell with managed inference and sandboxed isolation
- [NousResearch/hermes-agent ⭐22.2k](https://github.com/NousResearch/hermes-agent) - Self-improving AI agent with built-in learning loop, user modeling, and OpenClaw migration support

### 📚 Agent Resources & Guides

- [open-gitagent/gitagent ⭐2.5k](https://github.com/open-gitagent/gitagent) - Framework-agnostic, git-native standard for defining AI agents. Clone a repo, get an agent. Export to Claude Code, OpenAI, CrewAI, LangChain, and more
- [hesreallyhim/awesome-claude-code ⭐35.7k](https://github.com/hesreallyhim/awesome-claude-code) - A curated list of awesome skills, hooks, slash-commands, agent orchestrators, applications, and plugins for Claude Code
- [Shubhamsaboo/awesome-llm-apps ⭐104.3k](https://github.com/Shubhamsaboo/awesome-llm-apps) - Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models
- [coleam00/context-engineering-intro ⭐13.0k](https://github.com/coleam00/context-engineering-intro) - Context engineering is the new vibe coding - it's the way to actually make AI coding assistants work
- [Cranot/claude-code-guide ⭐2.6k](https://github.com/Cranot/claude-code-guide) - The Complete Claude Code CLI Guide - Live & Auto-Updated Every 2 Days
- [shanraisshan/claude-code-best-practice ⭐30.8k](https://github.com/shanraisshan/claude-code-best-practice) - Best practices and tips for Claude Code — agentic engineering patterns, vibe coding workflows
- [coleam00/ai-agents-masterclass ⭐3.3k](https://github.com/coleam00/ai-agents-masterclass) - Follow along with my AI Agents Masterclass videos! All of the code I create and use in this series
- [patchy631/ai-engineering-hub ⭐33.1k](https://github.com/patchy631/ai-engineering-hub) - In-depth tutorials on LLMs, RAGs and real-world AI agent applications
- [SamurAIGPT/awesome-openclaw ⭐851](https://github.com/SamurAIGPT/awesome-openclaw) - A curated list of awesome OpenClaw resources, tools, skills, tutorials, and articles
- [ComposioHQ/awesome-claude-skills ⭐50.5k](https://github.com/ComposioHQ/awesome-claude-skills) - A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows
- [BehiSecc/awesome-claude-skills ⭐8.1k](https://github.com/BehiSecc/awesome-claude-skills) - A curated list of Claude Skills
- [K-Dense-AI/claude-scientific-skills ⭐17.1k](https://github.com/K-Dense-AI/claude-scientific-skills) - A set of ready to use scientific skills for Claude
- [Kamalnrf/claude-plugins ⭐489](https://github.com/Kamalnrf/claude-plugins) - Lightweight registry to discover, install, and manage all public Claude plugins and agent skills
- [anthropics/skills ⭐109.0k](https://github.com/anthropics/skills) - Public repository for Agent Skills
- [anthropics/claude-plugins-official ⭐15.8k](https://github.com/anthropics/claude-plugins-official) - Official, Anthropic-managed directory of high quality Claude Code Plugins
- [google-gemini/gemini-skills ⭐3.1k](https://github.com/google-gemini/gemini-skills) - Skills for the Gemini API, SDK and model/agent interactions
- [davila7/claude-code-templates ⭐24.0k](https://github.com/davila7/claude-code-templates) - CLI tool for configuring and monitoring Claude Code
- [eyaltoledano/claude-task-master ⭐26.4k](https://github.com/eyaltoledano/claude-task-master) - An AI-powered task-management system you can drop into Cursor, Lovable, Windsurf, Roo, and others
- [coleam00/Archon ⭐13.9k](https://github.com/coleam00/Archon) - Beta release of Archon OS - the knowledge and task management backbone for AI coding assistants
- [danielmiessler/Fabric ⭐40.3k](https://github.com/danielmiessler/Fabric) - Fabric is an open-source framework for augmenting humans using AI


## 🏛️ Data Governance & Observability

- [open-metadata/OpenMetadata ⭐9.3k](https://github.com/open-metadata/OpenMetadata) - Unified metadata platform for data discovery, data observability, and data governance, powered by a central metadata repository
- [datahub-project/datahub ⭐11.8k](https://github.com/datahub-project/datahub) - The Metadata Platform for your Data and AI — data discovery, lineage, and governance at scale
- [OpenLineage/OpenLineage ⭐2.4k](https://github.com/OpenLineage/OpenLineage) - An open standard for metadata and lineage collection. Track data pipeline jobs, datasets, and runs
- [great-expectations/great_expectations ⭐11.3k](https://github.com/great-expectations/great_expectations) - The leading open-source data quality framework. Define, document, and validate data expectations
- [sodadata/soda-core ⭐2.3k](https://github.com/sodadata/soda-core) - Data quality testing and monitoring for SQL, Spark, and Pandas. Run checks directly in your pipelines
- [apache/atlas ⭐2.1k](https://github.com/apache/atlas) - Apache Atlas provides open metadata management and governance capabilities for organizations that need to build a catalog of their data assets
- [ronaldmego/agent-data-analyst](https://github.com/ronaldmego/agent-data-analyst) - AI data analyst that reads governance context (OpenMetadata) before running SQL. Profiles tables, classifies variables, detects anomalies — governance-informed analytics, 100% local ⭐ OSS

## 🛡️ AI Safety & Responsible AI

- [intuitem/ciso-assistant-community ⭐3.9k](https://github.com/intuitem/ciso-assistant-community) - One-stop-shop GRC platform for Risk Management, AppSec, Compliance & Audit, TPRM, Privacy. Supports 130+ frameworks: ISO 27001, NIST CSF, SOC 2, PCI DSS, GDPR, HIPAA, and more
- [guardrails-ai/guardrails ⭐6.6k](https://github.com/guardrails-ai/guardrails) - Adding guardrails to large language models. Validate and structure LLM outputs with programmable rules
- [NVIDIA/NeMo-Guardrails ⭐5.9k](https://github.com/NVIDIA/NeMo-Guardrails) - Open-source toolkit for easily adding programmable guardrails to LLM-based conversational AI
- [Trusted-AI/AIF360 ⭐2.8k](https://github.com/Trusted-AI/AIF360) - IBM AI Fairness 360 — comprehensive fairness metrics for datasets and ML models
- [microsoft/responsible-ai-toolbox ⭐1.7k](https://github.com/microsoft/responsible-ai-toolbox) - Responsible AI dashboard and tools for model and data exploration, error analysis, and fairness assessment
- [whylabs/langkit ⭐980](https://github.com/whylabs/langkit) - Open-source toolkit for monitoring Large Language Models — detect toxicity, hallucinations, and data quality issues

## 🎨 Avatar, Video & Image AI

- [jamiepine/voicebox ⭐14.4k](https://github.com/jamiepine/voicebox) - The open-source voice synthesis studio powered by Qwen3-TTS
- [Comfy-Org/ComfyUI ⭐107.6k](https://github.com/Comfy-Org/ComfyUI) - The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface
- [ZeroLu/awesome-nanobanana-pro ⭐9.6k](https://github.com/ZeroLu/awesome-nanobanana-pro) - An awesome list of curated Nano Banana pro prompts and examples
- [PicoTrex/Awesome-Nano-Banana-images ⭐21.9k](https://github.com/PicoTrex/Awesome-Nano-Banana-images) - A curated collection of fun and creative examples generated with Nano Banana & Nano Banana Pro
- [resemble-ai/chatterbox ⭐24.1k](https://github.com/resemble-ai/chatterbox) - SoTA open-source TTS
- [facefusion/facefusion-docker ⭐524](https://github.com/facefusion/facefusion-docker) - Industry leading face manipulation platform
- [FujiwaraChoki/MoneyPrinterV2 ⭐28.0k](https://github.com/FujiwaraChoki/MoneyPrinterV2) - Automate the process of making money online

## 📊 Data Engineering & Analytics
- [FalkorDB/QueryWeaver ⭐796](https://github.com/FalkorDB/QueryWeaver) - Open-source Text2SQL tool that transforms natural language into SQL using graph-powered schema understanding

- [DataExpert-io/data-engineer-handbook ⭐40.8k](https://github.com/DataExpert-io/data-engineer-handbook) - This is a repo with links to everything you'd ever want to learn about data engineering
- [dlt-hub/dlt ⭐5.2k](https://github.com/dlt-hub/dlt) - data load tool (dlt) is an open source Python library that makes data loading easy
- [igorbarinov/awesome-data-engineering ⭐8.4k](https://github.com/igorbarinov/awesome-data-engineering) - A curated list of data engineering tools for software developers
- [gunnarmorling/awesome-opensource-data-engineering ⭐3.1k](https://github.com/gunnarmorling/awesome-opensource-data-engineering) - An Awesome List of Open-Source Data Engineering Projects
- [Countly/countly-server ⭐5.8k](https://github.com/Countly/countly-server) - Countly is a privacy-first, AI-powered analytics and engagement platform
- [tensorlakeai/tensorlake ⭐895](https://github.com/tensorlakeai/tensorlake) - Tensorlake is a Document Ingestion API and a serverless platform for building data processing
- [weaviate/elysia ⭐1.9k](https://github.com/weaviate/elysia) - Python package and backend for the Elysia platform app
- [mito-ds/mito ⭐2.6k](https://github.com/mito-ds/mito) - Jupyter extensions that help you write code faster: Context aware AI Chat, Autocomplete, and Spreadsheet
- [pixeltable/pixeltable ⭐1.6k](https://github.com/pixeltable/pixeltable) - Data Infrastructure providing a declarative, incremental approach for multimodal AI workloads
- [chartdb/chartdb ⭐21.7k](https://github.com/chartdb/chartdb) - Database diagrams editor that allows you to visualize and design your DB with a single query
- [dbt-labs/dbt-core ⭐12.5k](https://github.com/dbt-labs/dbt-core) - dbt enables data analysts and engineers to transform their data using the same practices that software engineers use
- [valkey-io/valkey ⭐25.3k](https://github.com/valkey-io/valkey) - A flexible distributed key-value database that is optimized for caching and other realtime workloads
- [grafana/grafana ⭐72.9k](https://github.com/grafana/grafana) - The open and composable observability and data visualization platform
- [elastic/elasticsearch ⭐76.4k](https://github.com/elastic/elasticsearch) - Free and Open Source, Distributed, RESTful Search Engine
- [trinodb/trino ⭐12.7k](https://github.com/trinodb/trino) - Official repository of Trino, the distributed SQL query engine for big data
- [apache/superset ⭐72.2k](https://github.com/apache/superset) - Apache Superset is a Data Visualization and Data Exploration Platform
- [microsoft/data-formulator ⭐15.2k](https://github.com/microsoft/data-formulator) - Create rich visualizations with AI
- [vllm-project/vllm ⭐75.0k](https://github.com/vllm-project/vllm) - A high-throughput and memory-efficient inference and serving engine for LLMs
- [Openpanel-dev/openpanel ⭐5.6k](https://github.com/Openpanel-dev/openpanel) - OpenPanel is an open-source web and product analytics platform
- [Canner/WrenAI ⭐14.8k](https://github.com/Canner/WrenAI) - GenBI (Generative BI) queries any database in natural language, generates accurate SQL, charts
- [sinaptik-ai/pandas-ai ⭐23.4k](https://github.com/sinaptik-ai/pandas-ai) - Chat with your database or your datalake (SQL, CSV, parquet)
- [vanna-ai/vanna ⭐23.2k](https://github.com/vanna-ai/vanna) - Chat with your SQL database. Accurate Text-to-SQL Generation via LLMs using Agentic Retrieval
- [OpenBB-finance/OpenBB ⭐65.0k](https://github.com/OpenBB-finance/OpenBB) - Financial data platform for analysts, quants and AI agents
- [ganttrify](https://github.com/ganttrify/ganttrify) - Create beautiful Gantt charts with ggplot2
- [Avaiga/taipy ⭐19.1k](https://github.com/Avaiga/taipy) - Turns Data and AI algorithms into production-ready web applications in no time
- [mckinsey/vizro ⭐3.6k](https://github.com/mckinsey/vizro) - Vizro is a low-code toolkit for building high-quality data visualization apps

## 🧠 ML & Data Science

- [KalyanM45/AI-Project-Gallery ⭐4.6k](https://github.com/KalyanM45/AI-Project-Gallery) - Repository containing Artificial Intelligence Projects such as Machine Learning, Deep Learning and Generative AI
- [google/langextract ⭐35.0k](https://github.com/google/langextract) - A Python library for extracting structured information from unstructured text using LLMs
- [lyogavin/airllm ⭐14.7k](https://github.com/lyogavin/airllm) - AirLLM 70B inference with single 4GB GPU
- [HKUDS/DeepTutor ⭐11.0k](https://github.com/HKUDS/DeepTutor) - DeepTutor: AI-Powered Personalized Learning Assistant
- [Sumanth077/ai-engineering-toolkit ⭐3.0k](https://github.com/Sumanth077/ai-engineering-toolkit) - A curated list of 100+ libraries and frameworks for AI engineers building with LLMs
- [microsoft/BitNet ⭐37.0k](https://github.com/microsoft/BitNet) - Official inference framework for 1-bit LLMs
- [cvs-health/uqlm ⭐1.1k](https://github.com/cvs-health/uqlm) - UQLM: Uncertainty Quantification for Language Models, is a Python package for UQ-based LLM hallucination detection
- [confident-ai/deepeval ⭐14.4k](https://github.com/confident-ai/deepeval) - The LLM Evaluation Framework
- [google-research/timesfm ⭐14.0k](https://github.com/google-research/timesfm) - Time Series Foundation Model by Google Research. Pretrained for zero-shot forecasting, 200M params, available in BigQuery. ICML 2024 paper
- [OpenBMB/MiniCPM-o ⭐24.3k](https://github.com/OpenBMB/MiniCPM-o) - A Gemini 2.5 Flash Level MLLM for Vision, Speech, and Full-Duplex Multimodal Live Streaming
- [mistralai/cookbook ⭐2.2k](https://github.com/mistralai/cookbook) - Mistral AI cookbook
- [TheAlgorithms/Python ⭐219.2k](https://github.com/TheAlgorithms/Python) - All Algorithms implemented in Python
- [KalyanKS-NLP/llm-engineer-toolkit ⭐10.1k](https://github.com/KalyanKS-NLP/llm-engineer-toolkit) - A curated list of 120+ LLM libraries category wise
- [firecrawl/firecrawl ⭐102.8k](https://github.com/firecrawl/firecrawl) - The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data
- [academic/awesome-datascience ⭐28.7k](https://github.com/academic/awesome-datascience) - An awesome Data Science repository to learn and apply for real world problems
- [hiyouga/LlamaFactory ⭐69.4k](https://github.com/hiyouga/LlamaFactory) - Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)
- [Machine-Learning-Tokyo/Interactive_Tools ⭐2.8k](https://github.com/Machine-Learning-Tokyo/Interactive_Tools) - Interactive Tools for Machine Learning, Deep Learning and Math
- [rushter/MLAlgorithms ⭐11.0k](https://github.com/rushter/MLAlgorithms) - Minimal and clean examples of machine learning algorithms implementations
- [jivoi/awesome-ml-for-cybersecurity ⭐8.4k](https://github.com/jivoi/awesome-ml-for-cybersecurity) - Machine Learning for Cyber Security
- [roboticcam/machine-learning-notes ⭐9.6k](https://github.com/roboticcam/machine-learning-notes) - My continuously updated Machine Learning, Probabilistic Models and Deep Learning notes and demos
- [ml-tooling/ml-workspace ⭐3.5k](https://github.com/ml-tooling/ml-workspace) - All-in-one web-based IDE specialized for machine learning and data science
- [lukasmasuch/best-of-ml-python ⭐23.4k](https://github.com/lukasmasuch/best-of-ml-python) - A ranked list of awesome machine learning Python libraries. Updated weekly
- [EthicalML/awesome-production-machine-learning ⭐20.3k](https://github.com/EthicalML/awesome-production-machine-learning) - A curated list of awesome open source libraries to deploy, monitor, version and scale your machine learning
- [josephmisiti/awesome-machine-learning ⭐72.1k](https://github.com/josephmisiti/awesome-machine-learning) - A curated list of awesome Machine Learning frameworks, libraries and software
- [eugeneyan/applied-ml ⭐28.8k](https://github.com/eugeneyan/applied-ml) - Papers & tech blogs by companies sharing their work on data science & machine learning in production
- [GokuMohandas/Made-With-ML ⭐47.1k](https://github.com/GokuMohandas/Made-With-ML) - Learn how to design, develop, deploy and iterate on production-grade ML applications
- [posit-dev/positron ⭐4.0k](https://github.com/posit-dev/positron) - Positron, a next-generation data science IDE
- [fixie-ai/ultravox ⭐4.4k](https://github.com/fixie-ai/ultravox) - A fast multimodal LLM for real-time voice
- [developersdigest/llm-answer-engine ⭐5.0k](https://github.com/developersdigest/llm-answer-engine) - Perplexity Inspired Answer Engine
- [unslothai/notebooks ⭐5.1k](https://github.com/unslothai/notebooks) - Jupyter notebooks demonstrating LLM fine-tuning with Unsloth AI for efficient model training

📚 **New to ML?** Check out [Learning & Reference](#-learning--reference) for courses and tutorials.

## 🛠️ DevTools & Infrastructure

- [CapSoftware/Cap ⭐17.8k](https://github.com/CapSoftware/Cap) - Open source Loom alternative. Beautiful, shareable screen recordings
- [bitnami/containers ⭐4.4k](https://github.com/bitnami/containers) - Bitnami container images
- [kottster/kottster ⭐1.1k](https://github.com/kottster/kottster) - Instant Node.js admin panel. Secure, self-hosted, and easy to set up
- [awesome-selfhosted/awesome-selfhosted ⭐283.5k](https://github.com/awesome-selfhosted/awesome-selfhosted) - A list of Free Software network services and web applications which can be hosted on your own servers
- [coollabsio/coolify ⭐52.5k](https://github.com/coollabsio/coolify) - An open-source, self-hostable PaaS alternative to Vercel, Heroku & Netlify
- [herin7/gitforme ⭐381](https://github.com/herin7/gitforme) - AI-powered GitHub code explorer — understand any repo in minutes, not days
- [coderamp-labs/gitingest ⭐14.2k](https://github.com/coderamp-labs/gitingest) - Replace 'hub' with 'ingest' in any GitHub URL to get a prompt-friendly extract of a codebase
- [ahmedkhaleel2004/gitdiagram ⭐15.4k](https://github.com/ahmedkhaleel2004/gitdiagram) - Free, simple, fast interactive diagrams for any GitHub repository
- [balena-io/open-balena ⭐1.2k](https://github.com/balena-io/open-balena) - Open source software to manage connected IoT devices at scale
- [enescingoz/awesome-n8n-templates ⭐20.8k](https://github.com/enescingoz/awesome-n8n-templates) - Supercharge your workflow automation with this curated collection of n8n templates
- [lucaswalter/n8n-ai-automations ⭐1.4k](https://github.com/lucaswalter/n8n-ai-automations) - Collection of n8n workflows, n8n templates, AI automations, and AI agents
- [Zie619/n8n-workflows ⭐53.5k](https://github.com/Zie619/n8n-workflows) - all of the workflows of n8n i could find
- [microsoft/playwright-cli ⭐6.8k](https://github.com/microsoft/playwright-cli) - Command-line interface for Playwright, a browser automation tool with AI capabilities
- [restyler/awesome-n8n ⭐2.8k](https://github.com/restyler/awesome-n8n) - Useful n8n resources: list of community nodes and tutorials
- [n8n-io/n8n ⭐182.1k](https://github.com/n8n-io/n8n) - Fair-code workflow automation platform with native AI capabilities
- [kuchin/awesome-cto ⭐34.6k](https://github.com/kuchin/awesome-cto) - A curated and opinionated list of resources for Chief Technology Officers
- [AlexsJones/llmfit ⭐20.8k](https://github.com/AlexsJones/llmfit) - Right-size LLM models to your hardware. Detects CPU, RAM, GPU and scores models by quality, speed, fit and context. Supports Ollama, llama.cpp, MLX

## 🌐 Web & Apps

- [TailAdmin/free-nextjs-admin-dashboard ⭐2.4k](https://github.com/TailAdmin/free-nextjs-admin-dashboard) - TailAdmin is a Next.js and Tailwind CSS free, open-source admin dashboard template
- [Nutlope/self.so ⭐2.9k](https://github.com/Nutlope/self.so) - LinkedIn -> personal site generator
- [toon-format/toon ⭐23.6k](https://github.com/toon-format/toon) - Token-Oriented Object Notation (TOON) – Compact, human-readable, schema-aware JSON for LLM prompts
- [superdesigndev/superdesign ⭐6.3k](https://github.com/superdesigndev/superdesign) - AI Product Design Agent - Open Source
- [iliane5/meridian ⭐2.4k](https://github.com/iliane5/meridian) - Meridian cuts through news noise by scraping hundreds of sources, analyzing stories with AI

## 📚 Learning & Reference

*Educational resources, courses, and tutorials organized by topic.*

> **📖 Categorization Guide:** Courses, tutorials, and learning resources go here. Tools, frameworks, and production libraries belong in their respective technical categories (e.g., 🧠 ML & Data Science). See [Contributing](#contributing) for details.

### Data Science & ML
- [microsoft/ML-For-Beginners ⭐84.9k](https://github.com/microsoft/ML-For-Beginners) - 12 weeks, 26 lessons, 52 quizzes, classic Machine Learning for all
- [microsoft/Data-Science-For-Beginners ⭐34.7k](https://github.com/microsoft/Data-Science-For-Beginners) - 10 Weeks, 20 Lessons, Data Science for All!
- [ageron/handson-ml3 ⭐12.8k](https://github.com/ageron/handson-ml3) - A series of Jupyter notebooks that walk you through the fundamentals of Machine Learning and Deep Learning
- [d2l-ai/d2l-en ⭐28.5k](https://github.com/d2l-ai/d2l-en) - Interactive deep learning book with multi-framework code, math, and discussions
- [Avik-Jain/100-Days-Of-ML-Code ⭐50.2k](https://github.com/Avik-Jain/100-Days-Of-ML-Code) - 100 Days of Machine Learning Coding
- [mml-book/mml-book.github.io ⭐15.3k](https://github.com/mml-book/mml-book.github.io) - Companion webpage to the book "Mathematics For Machine Learning"
- [karpathy/nn-zero-to-hero ⭐21.2k](https://github.com/karpathy/nn-zero-to-hero) - Neural networks: zero to hero
- [ujjwalkarn/Machine-Learning-Tutorials ⭐17.7k](https://github.com/ujjwalkarn/Machine-Learning-Tutorials) - Machine learning and deep learning tutorials, articles and other resources
- [khangich/machine-learning-interview ⭐12.4k](https://github.com/khangich/machine-learning-interview) - Machine Learning Interviews from FAANG, Snapchat, LinkedIn

### AI & Agents
- [microsoft/generative-ai-for-beginners ⭐108.8k](https://github.com/microsoft/generative-ai-for-beginners) - 21 Lessons, Get Started Building with Generative AI
- [microsoft/ai-agents-for-beginners ⭐55.7k](https://github.com/microsoft/ai-agents-for-beginners) - 10 Lessons to Get Started Building AI Agents
- [dair-ai/Prompt-Engineering-Guide ⭐72.7k](https://github.com/dair-ai/Prompt-Engineering-Guide) - Guides, papers, lectures, notebooks and resources for prompt engineering
- [HandsOnLLM/Hands-On-Large-Language-Models ⭐24.7k](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models) - Official code repo for the O'Reilly Book - Hands-On Large Language Models
- [NirDiamant/GenAI_Agents ⭐20.9k](https://github.com/NirDiamant/GenAI_Agents) - This repository provides a comprehensive collection of tutorials and implementations for Generative AI Agents
- [NirDiamant/RAG_Techniques ⭐26.4k](https://github.com/NirDiamant/RAG_Techniques) - This repository provides a comprehensive collection of tutorials and implementations for Retrieval-Augmented Generation (RAG) systems
- [labmlai/annotated_deep_learning_papers](https://github.com/labmlai/annotated_deep_learning_papers) - Annotated Deep Learning Papers

### NLP & RL
- [keon/awesome-nlp ⭐18.4k](https://github.com/keon/awesome-nlp) - A curated list of resources dedicated to Natural Language Processing
- [aikorea/awesome-rl ⭐9.7k](https://github.com/aikorea/awesome-rl) - Reinforcement learning resources curated
- [FareedKhan-dev/all-rl-algorithms ⭐1.5k](https://github.com/FareedKhan-dev/all-rl-algorithms) - Implementations of all major Reinforcement Learning algorithms

### Programming & General
- [Asabeneh/30-Days-Of-Python ⭐60.4k](https://github.com/Asabeneh/30-Days-Of-Python) - The 30 Days of Python programming challenge is a step-by-step guide to learn the Python programming language
- [freeCodeCamp/freeCodeCamp ⭐440.5k](https://github.com/freeCodeCamp/freeCodeCamp) - freeCodeCamp.org's open-source codebase and curriculum
- [trekhleb/learn-python ⭐17.8k](https://github.com/trekhleb/learn-python) - Playground and cheatsheet for learning Python
- [Fechin/reference ⭐10.3k](https://github.com/Fechin/reference) - Share quick reference cheat sheet for developers
- [addyosmani/gemini-cli-tips ⭐2.3k](https://github.com/addyosmani/gemini-cli-tips) - Gemini CLI Tips and Tricks
- [sindresorhus/awesome ⭐451.1k](https://github.com/sindresorhus/awesome) - Awesome lists about all kinds of interesting topics
- [public-apis/public-apis ⭐418.3k](https://github.com/public-apis/public-apis) - A collective list of free APIs

## 🔍 OCR & Document Processing

- [rednote-hilab/dots.ocr ⭐8.2k](https://github.com/rednote-hilab/dots.ocr) - Multilingual Document Layout Parsing in a Single Vision-Language Model
- [datalab-to/chandra ⭐8.2k](https://github.com/datalab-to/chandra) - OCR model that handles complex tables, forms, handwriting with full layout
- [google/A2UI ⭐13.8k](https://github.com/google/A2UI) - Advanced UI understanding model
- [ngafar/llama-scan ⭐818](https://github.com/ngafar/llama-scan) - Transcribe PDFs with local LLMs
- [AnswerDotAI/clipmd ⭐220](https://github.com/AnswerDotAI/clipmd) - Convert clipboard from HTML to MD
- [allenai/olmocr ⭐17.1k](https://github.com/allenai/olmocr) - Toolkit for linearizing PDFs for LLM datasets/training
- [deepseek-ai/DeepSeek-OCR ⭐22.8k](https://github.com/deepseek-ai/DeepSeek-OCR) - Contexts Optical Compression
- [bytedance/Dolphin ⭐8.9k](https://github.com/bytedance/Dolphin) - The official repo for "Dolphin: Document Image Parsing via Heterogeneous Anchor Prompting"
- [microsoft/markitdown ⭐93.2k](https://github.com/microsoft/markitdown) - Python tool for converting files and office documents to Markdown
- [unclecode/crawl4ai ⭐63.2k](https://github.com/unclecode/crawl4ai) - Open-source LLM Friendly Web Crawler & Scraper
- [docling-project/docling ⭐56.9k](https://github.com/docling-project/docling) - Get your documents ready for gen AI
- [jdepoix/youtube-transcript-api ⭐7.2k](https://github.com/jdepoix/youtube-transcript-api) - This is a python API which allows you to get the transcript/subtitles for a given YouTube video

## 📝 Content & Productivity

- [HKUDS/Paper2Slides ⭐3.3k](https://github.com/HKUDS/Paper2Slides) - Paper2Slides: From Paper to Presentation in One Click
- [AsyncFuncAI/deepwiki-open ⭐15.3k](https://github.com/AsyncFuncAI/deepwiki-open) - Open Source DeepWiki: AI-Powered Wiki Generator for GitHub/Gitlab/Bitbucket Repositories

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