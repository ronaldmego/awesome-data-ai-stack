# Awesome Data & AI Stack [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of awesome Data, AI, and Agent tools — organized by agent anatomy and data stack layers. This collection represents real-world enterprise experience from deploying AI and data solutions at scale, with a unique perspective on the architectural patterns that actually work in production environments.

Unlike generic lists, this catalog focuses on the complete data-to-intelligence pipeline: from raw data ingestion through analytics, machine learning, and culminating in intelligent agents that can reason, act, and learn.

> **New:** Looking for tools to run your startup without hiring? Check out [Awesome Agentic Startup Stack](https://github.com/ronaldmego/awesome-agentic-startup-stack) — automation, marketing, content creation, and operations for founders.

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
- [🔬 Experimental / Early Stage](#-experimental--early-stage)
- [🏛️ Data Governance & Observability](#️-data-governance--observability)
- [🛡️ AI Safety & Responsible AI](#️-ai-safety--responsible-ai)
- [📊 Data Engineering & Analytics](#-data-engineering--analytics)
- [🧠 ML & Data Science](#-ml--data-science)
- [🛠️ DevTools & Infrastructure](#️-devtools--infrastructure)
- [📚 Learning & Reference](#-learning--reference)
- [🔍 OCR & Document Processing](#-ocr--document-processing)
- [Contributing](#contributing)
- [About](#about)

## 🤖 AI Agents & Frameworks

### 💻 Vibe Coding & CLI Agents

- [anthropics/claude-code `105.2k`](https://github.com/anthropics/claude-code) - Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster
- [google-gemini/gemini-cli `100.0k`](https://github.com/google-gemini/gemini-cli) - An open-source AI agent that brings the power of Gemini directly into your terminal
- [openai/codex `72.4k`](https://github.com/openai/codex) - Lightweight coding agent that runs in your terminal
- [QwenLM/qwen-code `21.6k`](https://github.com/QwenLM/qwen-code) - An open-source AI agent that lives in your terminal
- [bytedance/trae-agent `11.2k`](https://github.com/bytedance/trae-agent) - Trae Agent is an LLM-based agent for general purpose software engineering tasks
- [anomalyco/opencode `135.5k`](https://github.com/anomalyco/opencode) - The open source coding agent
- [HKUDS/DeepCode `15.1k`](https://github.com/HKUDS/DeepCode) - DeepCode: Open Agentic Coding (Paper2Code & Text2Web & Text2Backend)
- [BloopAI/vibe-kanban `24.2k`](https://github.com/BloopAI/vibe-kanban) - Get 10X more out of Claude Code, Codex or any coding agent
- [Yeachan-Heo/oh-my-claudecode `23.0k`](https://github.com/Yeachan-Heo/oh-my-claudecode) - Multi-agent orchestration for Claude Code
- [Gitlawb/openclaude `10.5k`](https://github.com/Gitlawb/openclaude) - Open-source Claude Code CLI for 200+ models

### 🔧 MCP Servers & Skills

- [punkpeye/awesome-mcp-servers `84.1k`](https://github.com/punkpeye/awesome-mcp-servers) - A collection of MCP servers
- [modelcontextprotocol/servers `82.8k`](https://github.com/modelcontextprotocol/servers) - Model Context Protocol Servers
- [supabase-community/supabase-mcp `2.6k`](https://github.com/supabase-community/supabase-mcp) - Connect Supabase to your AI assistants
- [idosal/git-mcp `7.9k`](https://github.com/idosal/git-mcp) - Remote MCP server for any GitHub project
- [firecrawl/firecrawl-mcp-server `5.9k`](https://github.com/firecrawl/firecrawl-mcp-server) - Web scraping and search MCP server
- [googleapis/genai-toolbox `13.6k`](https://github.com/googleapis/genai-toolbox) - MCP Toolbox for Databases
- [mongodb-js/mongodb-mcp-server `987`](https://github.com/mongodb-js/mongodb-mcp-server) - MCP server for MongoDB
- [crystaldba/postgres-mcp `2.5k`](https://github.com/crystaldba/postgres-mcp) - Postgres MCP with performance analysis
- [upstash/context7 `51.4k`](https://github.com/upstash/context7) - Up-to-date code documentation for LLMs
- [mindsdb/mindsdb `38.9k`](https://github.com/mindsdb/mindsdb) - Federated Query Engine for AI
- [PrefectHQ/fastmcp `24.2k`](https://github.com/PrefectHQ/fastmcp) - Fast, Pythonic way to build MCP servers
- [ronaldmego/openmetadata-mcp-agent](https://github.com/ronaldmego/openmetadata-mcp-agent) - Conversational AI agent for OpenMetadata ⭐ OSS
- [ronaldmego/matomo-mcp-agent](https://github.com/ronaldmego/matomo-mcp-agent) - Talk to Matomo analytics in natural language ⭐ OSS

### 🎯 Orchestration & Multi-Agent

- [langchain-ai/deepagents `18.7k`](https://github.com/langchain-ai/deepagents) - Agent harness with LangChain and LangGraph
- [crewAIInc/crewAI `47.8k`](https://github.com/crewAIInc/crewAI) - Framework for orchestrating autonomous AI agents
- [langflow-ai/langflow `146.5k`](https://github.com/langflow-ai/langflow) - Build AI agents visually. Also suitable for low-code business automation
- [FlowiseAI/Flowise `51.4k`](https://github.com/FlowiseAI/Flowise) - Build AI Agents, Visually
- [The-Pocket/PocketFlow `10.3k`](https://github.com/The-Pocket/PocketFlow) - 100-line LLM framework
- [MotiaDev/motia `15.2k`](https://github.com/MotiaDev/motia) - Multi-Language Backend Framework with AI agents
- [simstudioai/sim `27.4k`](https://github.com/simstudioai/sim) - Central intelligence layer for your AI workforce
- [agno-agi/agno `39.1k`](https://github.com/agno-agi/agno) - Programming language for agentic software
- [ComposioHQ/agent-orchestrator `5.7k`](https://github.com/ComposioHQ/agent-orchestrator) - Spawn parallel AI coding agents
- [Pythagora-io/gpt-pilot `33.8k`](https://github.com/Pythagora-io/gpt-pilot) - The first real AI developer
- [kortix-ai/suna `19.6k`](https://github.com/kortix-ai/suna) - Build, manage and train AI Agents
- [VRSEN/agency-swarm `4.1k`](https://github.com/VRSEN/agency-swarm) - Multi-Agent Orchestration Framework

### 📝 Memory & RAG

- [mem0ai/mem0 `51.8k`](https://github.com/mem0ai/mem0) - Universal memory layer for AI Agents
- [getzep/graphiti `24.4k`](https://github.com/getzep/graphiti) - Real-Time Knowledge Graphs for AI Agents
- [topoteretes/cognee `14.9k`](https://github.com/topoteretes/cognee) - Knowledge Engine for AI Agent Memory
- [infiniflow/ragflow `76.9k`](https://github.com/infiniflow/ragflow) - Leading open-source RAG engine
- [HKUDS/LightRAG `31.5k`](https://github.com/HKUDS/LightRAG) - Simple and Fast Retrieval-Augmented Generation
- [airweave-ai/airweave `6.2k`](https://github.com/airweave-ai/airweave) - Open-source context retrieval layer for AI agents

### 💬 Conversational & Chat

- [emcie-co/parlant `17.9k`](https://github.com/emcie-co/parlant) - LLM agents built for control
- [janhq/jan `41.4k`](https://github.com/janhq/jan) - Open source alternative to ChatGPT
- [openinterpreter/open-interpreter `63.0k`](https://github.com/openinterpreter/open-interpreter) - Natural language interface for computers
- [CopilotKit/CopilotKit `29.9k`](https://github.com/CopilotKit/CopilotKit) - Frontend for Agents & Generative UI
- [open-webui/open-webui `129.6k`](https://github.com/open-webui/open-webui) - User-friendly AI Interface
- [Anything-LLM/anything-llm `57.4k`](https://github.com/Mintplex-Labs/anything-llm) - All-in-one AI application with RAG
- [letta-ai/letta `21.9k`](https://github.com/letta-ai/letta) - Platform for building stateful agents

### 🌐 Browser & Web Agents

- [browser-use/browser-use `85.6k`](https://github.com/browser-use/browser-use) - Make websites accessible for AI agents
- [browserbase/stagehand `21.8k`](https://github.com/browserbase/stagehand) - AI Browser Automation Framework
- [assafelovic/gpt-researcher `26.2k`](https://github.com/assafelovic/gpt-researcher) - Autonomous research agent

### 🏠 Personal AI Assistants & Gateways

- [openclaw/openclaw `345.5k`](https://github.com/openclaw/openclaw) - Your own personal AI assistant
- [NVIDIA/NemoClaw `18.2k`](https://github.com/NVIDIA/NemoClaw) - OpenClaw in NVIDIA OpenShell
- [NousResearch/hermes-agent `22.2k`](https://github.com/NousResearch/hermes-agent) - Self-improving AI agent

### 📚 Agent Resources & Guides

- [hesreallyhim/awesome-claude-code `35.7k`](https://github.com/hesreallyhim/awesome-claude-code) - Curated list for Claude Code
- [Shubhamsaboo/awesome-llm-apps `104.3k`](https://github.com/Shubhamsaboo/awesome-llm-apps) - Collection of LLM apps
- [shanraisshan/claude-code-best-practice `30.8k`](https://github.com/shanraisshan/claude-code-best-practice) - Best practices for Claude Code
- [patchy631/ai-engineering-hub `33.1k`](https://github.com/patchy631/ai-engineering-hub) - Tutorials on LLMs and AI agents
- [anthropics/skills `109.0k`](https://github.com/anthropics/skills) - Public repository for Agent Skills
- [anthropics/claude-plugins-official `15.8k`](https://github.com/anthropics/claude-plugins-official) - Official Claude Code Plugins
- [google-gemini/gemini-skills `3.1k`](https://github.com/google-gemini/gemini-skills) - Skills for Gemini API
- [davila7/claude-code-templates `24.0k`](https://github.com/davila7/claude-code-templates) - CLI tool for Claude Code
- [eyaltoledano/claude-task-master `26.4k`](https://github.com/eyaltoledano/claude-task-master) - Task management for AI coding
- [danielmiessler/Fabric `40.3k`](https://github.com/danielmiessler/Fabric) - Framework for augmenting humans using AI

## 🔬 Experimental / Early Stage

Tools that are new, unproven, or exploring novel approaches. Use with caution — potential high reward, high volatility.

- [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) - Claude Code skill that cuts ~65% tokens via caveman-speak compression
- [getcompanion-ai/feynman](https://github.com/getcompanion-ai/feynman) - AI companion for self-awareness from your chat history
- [open-gitagent/gitagent](https://github.com/open-gitagent/gitagent) - AI agent framework for Git-based workflows — *Inmaduro, potencial interesante*

## 🏛️ Data Governance & Observability

- [open-metadata/OpenMetadata `9.3k`](https://github.com/open-metadata/OpenMetadata) - Unified metadata platform for data discovery and governance
- [datahub-project/datahub `11.8k`](https://github.com/datahub-project/datahub) - Metadata Platform for Data and AI
- [OpenLineage/OpenLineage `2.4k`](https://github.com/OpenLineage/OpenLineage) - Open standard for metadata and lineage
- [great-expectations/great_expectations `11.3k`](https://github.com/great-expectations/great_expectations) - Data quality framework
- [sodadata/soda-core `2.3k`](https://github.com/sodadata/soda-core) - Data quality testing and monitoring
- [ronaldmego/agent-data-analyst](https://github.com/ronaldmego/agent-data-analyst) - AI data analyst with governance context ⭐ OSS

## 🛡️ AI Safety & Responsible AI

- [intuitem/ciso-assistant-community `3.9k`](https://github.com/intuitem/ciso-assistant-community) - GRC platform for Risk Management and Compliance
- [guardrails-ai/guardrails `6.6k`](https://github.com/guardrails-ai/guardrails) - Adding guardrails to LLMs
- [NVIDIA/NeMo-Guardrails `5.9k`](https://github.com/NVIDIA/NeMo-Guardrails) - Programmable guardrails for conversational AI
- [Trusted-AI/AIF360 `2.8k`](https://github.com/Trusted-AI/AIF360) - IBM AI Fairness 360
- [microsoft/responsible-ai-toolbox `1.7k`](https://github.com/microsoft/responsible-ai-toolbox) - Responsible AI dashboard and tools

## 📊 Data Engineering & Analytics

- [DataExpert-io/data-engineer-handbook `40.8k`](https://github.com/DataExpert-io/data-engineer-handbook) - Everything about data engineering
- [dlt-hub/dlt `5.2k`](https://github.com/dlt-hub/dlt) - Data load tool
- [dbt-labs/dbt-core `12.5k`](https://github.com/dbt-labs/dbt-core) - Transform data using software engineering practices
- [valkey-io/valkey `25.3k`](https://github.com/valkey-io/valkey) - Distributed key-value database
- [grafana/grafana `72.9k`](https://github.com/grafana/grafana) - Observability and data visualization
- [elastic/elasticsearch `76.4k`](https://github.com/elastic/elasticsearch) - Distributed search engine
- [trinodb/trino `12.7k`](https://github.com/trinodb/trino) - Distributed SQL query engine
- [apache/superset `72.2k`](https://github.com/apache/superset) - Data Visualization and Exploration
- [vllm-project/vllm `75.0k`](https://github.com/vllm-project/vllm) - High-throughput LLM inference
- [Canner/WrenAI `14.8k`](https://github.com/Canner/WrenAI) - Generative BI with natural language
- [sinaptik-ai/pandas-ai `23.4k`](https://github.com/sinaptik-ai/pandas-ai) - Chat with your data
- [vanna-ai/vanna `23.2k`](https://github.com/vanna-ai/vanna) - Text-to-SQL with Agentic Retrieval
- [OpenBB-finance/OpenBB `65.0k`](https://github.com/OpenBB-finance/OpenBB) - Financial data platform
- [Avaiga/taipy `19.1k`](https://github.com/Avaiga/taipy) - Turn data into web applications
- [chartdb/chartdb `21.7k`](https://github.com/chartdb/chartdb) - Database diagrams from queries
- [mckinsey/vizro `3.6k`](https://github.com/mckinsey/vizro) - Low-code data visualization

## 🧠 ML & Data Science

- [google/langextract `35.0k`](https://github.com/google/langextract) - Extract structured info from text
- [microsoft/BitNet `37.0k`](https://github.com/microsoft/BitNet) - Inference for 1-bit LLMs
- [confident-ai/deepeval `14.4k`](https://github.com/confident-ai/deepeval) - LLM Evaluation Framework
- [google-research/timesfm `14.0k`](https://github.com/google-research/timesfm) - Time Series Foundation Model
- [mistralai/cookbook `2.2k`](https://github.com/mistralai/cookbook) - Mistral AI cookbook
- ~~[firecrawl/firecrawl `102.8k`](https://github.com/firecrawl/firecrawl) - Web Data API for AI~~ → Ver [Browser & Web Agents](#-browser--web-agents) y [MCP Servers](#-mcp-servers--skills)
- [academic/awesome-datascience `28.7k`](https://github.com/academic/awesome-datascience) - Data Science resources
- [hiyouga/LlamaFactory `69.4k`](https://github.com/hiyouga/LlamaFactory) - Fine-tuning 100+ LLMs
- [lukasmasuch/best-of-ml-python `23.4k`](https://github.com/lukasmasuch/best-of-ml-python) - Ranked ML Python libraries
- [EthicalML/awesome-production-machine-learning `20.3k`](https://github.com/EthicalML/awesome-production-machine-learning) - Production ML libraries
- [josephmisiti/awesome-machine-learning `72.1k`](https://github.com/josephmisiti/awesome-machine-learning) - ML frameworks and software
- [eugeneyan/applied-ml `28.8k`](https://github.com/eugeneyan/applied-ml) - ML in production papers
- [GokuMohandas/Made-With-ML `47.1k`](https://github.com/GokuMohandas/Made-With-ML) - Production-grade ML applications
- [posit-dev/positron `4.0k`](https://github.com/posit-dev/positron) - Next-generation data science IDE
- [unslothai/notebooks `5.1k`](https://github.com/unslothai/notebooks) - LLM fine-tuning notebooks

## 🛠️ DevTools & Infrastructure

- [midudev/autoskills `2.7k`](https://github.com/midudev/autoskills) - Auto-detects tech stack and installs AI agent skills. Built on skills.sh ecosystem
- [bitnami/containers `4.4k`](https://github.com/bitnami/containers) - Bitnami container images
- [awesome-selfhosted/awesome-selfhosted `283.5k`](https://github.com/awesome-selfhosted/awesome-selfhosted) - Self-hostable network services
- [coollabsio/coolify `52.5k`](https://github.com/coollabsio/coolify) - Self-hostable PaaS
- [coderamp-labs/gitingest `14.2k`](https://github.com/coderamp-labs/gitingest) - Prompt-friendly codebase extraction
- [ahmedkhaleel2004/gitdiagram `15.4k`](https://github.com/ahmedkhaleel2004/gitdiagram) - Interactive diagrams for GitHub repos
- [AlexsJones/llmfit `20.8k`](https://github.com/AlexsJones/llmfit) - Right-size LLMs to your hardware
- [safishamsi/graphify](https://github.com/safishamsi/graphify) - Convert code into knowledge graphs with Neo4j + interactive visualization

## 📚 Learning & Reference

- [microsoft/ML-For-Beginners `84.9k`](https://github.com/microsoft/ML-For-Beginners) - Classic Machine Learning
- [microsoft/Data-Science-For-Beginners `34.7k`](https://github.com/microsoft/Data-Science-For-Beginners) - Data Science course
- [microsoft/generative-ai-for-beginners `108.8k`](https://github.com/microsoft/generative-ai-for-beginners) - Generative AI
- [microsoft/ai-agents-for-beginners `55.7k`](https://github.com/microsoft/ai-agents-for-beginners) - Building AI Agents
- [dair-ai/Prompt-Engineering-Guide `72.7k`](https://github.com/dair-ai/Prompt-Engineering-Guide) - Prompt engineering resources
- [HandsOnLLM/Hands-On-Large-Language-Models `24.7k`](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models) - O'Reilly book repo
- [NirDiamant/GenAI_Agents `20.9k`](https://github.com/NirDiamant/GenAI_Agents) - Generative AI Agents tutorials
- [NirDiamant/RAG_Techniques `26.4k`](https://github.com/NirDiamant/RAG_Techniques) - RAG implementations
- [karpathy/nn-zero-to-hero `21.2k`](https://github.com/karpathy/nn-zero-to-hero) - Neural networks from scratch

## 🔍 OCR & Document Processing

- [datalab-to/chandra `8.2k`](https://github.com/datalab-to/chandra) - OCR for tables and forms
- [google/A2UI `13.8k`](https://github.com/google/A2UI) - Advanced UI understanding
- [allenai/olmocr `17.1k`](https://github.com/allenai/olmocr) - PDF linearization for LLMs
- [deepseek-ai/DeepSeek-OCR `22.8k`](https://github.com/deepseek-ai/DeepSeek-OCR) - Optical compression
- [bytedance/Dolphin `8.9k`](https://github.com/bytedance/Dolphin) - Document Image Parsing
- [microsoft/markitdown `93.2k`](https://github.com/microsoft/markitdown) - Files to Markdown
- [docling-project/docling `56.9k`](https://github.com/docling-project/docling) - Documents ready for gen AI

## Contributing

We welcome high-quality contributions. Please ensure repositories are actively maintained and production-ready.

## About

Curated by [Ronald Mego](https://ronaldmego.com), Head of Data Analytics @ Millicom | Tigo. Built from hands-on enterprise experience deploying AI and data solutions at scale.

For operational tools (marketing, automation, content), see [Awesome Agentic Startup Stack](https://github.com/ronaldmego/awesome-agentic-startup-stack).

---

*Last updated: April 2026*
