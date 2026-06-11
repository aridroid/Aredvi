# AREDVI MASTER ROADMAP

# Product Scope

## Product

AREDVI (Aredvi Picks)

Tagline:

"No tips. Just Aredvi."

---

## Product Vision

Aredvi Picks is an AI-powered investment intelligence platform that automatically discovers, analyzes, monitors, and explains investment opportunities using multiple specialized AI agents.

Unlike traditional stock tip platforms, Aredvi focuses on transparency, explainability, verification, and data-driven decision making.

The platform helps investors understand:

* Why a stock was selected
* Which signals contributed
* How confident the system is
* What risks exist
* How opportunities evolve over time

---

## Core Product Features

### Stock Discovery & Screening

* Automated Daily Stock Screening
* Momentum Analysis Agent
* Fundamental Growth Agent
* News & Sentiment Agent
* Signal Fusion Engine
* Aredvi Picks Generator
* Screening History

---

### Investment Intelligence

* Explainable AI Dashboard
* Institutional Activity Intelligence
* Bulk Deals Intelligence
* Block Deals Intelligence
* Market Footprint Tracking
* Sector Intelligence
* Sector Rotation Analysis

---

### Portfolio & Monitoring

* Watchlists
* Alerts & Notifications
* Portfolio Tracking
* Portfolio Analytics
* Risk Analyzer

---

### Research & Analysis

* AI Research Assistant
* Company Research Pages
* Research Report Generation
* Historical Signal Tracking
* Financial Data Insights

---

### Strategy Evaluation

* Backtesting Engine
* Performance Tracking
* Win Rate Analysis
* Risk/Reward Analysis

---

## User Types

### Retail Investor

Uses:

* Stock Discovery
* Watchlists
* Alerts
* Research Assistant

---

### Wealth Manager

Uses:

* Research Workflows
* Portfolio Analysis
* Client Reporting
* Market Intelligence

---

### Investment Clubs

Uses:

* Shared Watchlists
* Collaborative Research
* Weekly Stock Discussions

---

## Technical Objectives

While building Aredvi Picks, the project will teach and implement:

* Python
* Agentic AI Systems
* LangGraph
* FastAPI
* PostgreSQL
* pgvector
* Redis
* Embeddings
* Vector Search
* RAG
* Financial Data Engineering
* React
* Docker
* Kubernetes
* AWS
* Security Engineering
* Observability
* Event-Driven Architecture
* CI/CD
* Enterprise Software Design

---

## Phase 0 - Foundation ✅

Completed:

* Repository setup
* Documentation structure
* ADR process
* Verification Layer architecture
* Agent Communication Contracts
* Project Context document

Status:
Completed

---

## Phase 1 - Core Runtime

Goal:

Understand the computer science foundations behind Agentic AI and prepare the runtime architecture that will power Aredvi Picks.

Topics:

* Graphs
* Nodes
* Edges
* State
* State Transitions
* Workflows
* Agent Contracts
* Why LangGraph Exists

Deliverables:

* First graph implementation (without LangGraph)
* State model design
* Agent communication contract design

Status:
In Progress

### Day 1 Completed ✅

Completed:

* Graph fundamentals
* Nodes
* Edges
* State
* State transitions
* Agentic AI as State Machines
* Why LangGraph Exists

Verification:

* Can explain Graph = Nodes + Edges
* Can explain the purpose of Nodes and Edges
* Can explain State as workflow memory
* Can explain State Transitions
* Can explain why agents require state
* Can explain why Agentic AI is fundamentally a State Machine + LLM
* Can explain why LangGraph exists
* Can explain why LangGraph should be viewed as a state machine runtime

### Day 2 Completed ✅

Completed:

* Built first workflow graph conceptually
* Identified nodes and edges
* Designed first workflow state
* Simulated state transitions manually
* Understood graph execution lifecycle
* Understood graph runtime architecture

Verification:

* Can identify nodes in a workflow
* Can identify edges in a workflow
* Can define workflow state
* Can explain state transitions
* Can explain graph execution step-by-step
* Can explain why state persistence is required

### Day 3 Completed ✅

Completed:

* Implemented first Graph class
* Implemented first Node class
* Implemented Runtime executor
* Implemented workflow state model
* Implemented state propagation
* Implemented START → END workflow execution
* Built first executable workflow
* Executed workflow successfully
* Verified state persistence across nodes

Verification:

* Nodes execute in sequence
* State survives node execution
* Runtime traverses graph correctly
* Runtime reaches END state
* Execution trace is observable
* State propagation verified

### Day 4 Current Task

Topics:

* Conditional Routing
* Dynamic Edge Selection
* Decision Nodes
* Branching Workflows
* State-driven execution paths

Deliverables:

* Conditional execution engine
* Branching workflow implementation
* Decision node implementation

Verification:

* Runtime selects correct path
* State drives routing decisions
* Different states produce different execution paths
* Workflow reaches correct END state
* Execution path is observable

---

## Phase 2 - LangGraph Fundamentals

Goal:

Build production-grade agent workflows using LangGraph.

Topics:

* LangGraph State
* Nodes
* Edges
* Conditional Routing
* Supervisors
* Human-in-the-loop
* Checkpointing

Deliverables:

* First working LangGraph application
* Multi-agent workflow
* Verification integration

Status:
Not Started

---

## Phase 3 - Backend Foundation

Goal:

Build API layer.

Topics:

* FastAPI
* Pydantic
* Dependency Injection
* API Versioning
* Authentication

Deliverables:

* Production API
* OpenAPI documentation
* Contract validation

Status:
Not Started

---

## Phase 4 - Data Layer

Goal:

Build persistence layer.

Topics:

* PostgreSQL
* pgvector
* Redis
* Embeddings
* Vector Search
* RAG Foundations

Deliverables:

* Database schema
* Vector search architecture
* Cache strategy
* Repository pattern

Status:
Not Started

---

## Phase 5 - Evaluation & Verification

Goal:

Build trust layer.

Topics:

* Unit tests
* Integration tests
* Runtime validation
* LLM Judge
* Evaluation datasets

Deliverables:

* Verification framework
* Evaluation pipeline

Status:
Not Started

---

## Phase 6 - Frontend

Goal:

Build React application.

Deliverables:

* React frontend
* API integration
* Authentication flows
* Dashboard UI
* Portfolio UI
* Watchlist UI
* Research Assistant UI

Status:
Not Started

---

## Phase 7 - Containerization

Goal:

Dockerize all services.

Deliverables:

* Backend container
* Frontend container
* Local development environment
* Docker Compose setup

Status:
Not Started

---

## Phase 8 - Kubernetes

Goal:

Deploy services using Kubernetes.

Deliverables:

* Kubernetes manifests
* Service discovery
* ConfigMaps
* Secrets management

Status:
Not Started

---

## Phase 9 - AWS Production Infrastructure

Goal:

Production deployment.

Topics:

* VPC
* IAM
* Security Groups
* Cognito
* API Gateway
* Lambda
* SNS
* SQS
* EventBridge
* ALB
* Auto Scaling

Deliverables:

* Production AWS environment
* Secure networking
* Identity management
* Event-driven infrastructure

Status:
Not Started

---

## Phase 10 - CI/CD & Observability

Goal:

Production operations.

Topics:

* GitHub Actions
* Monitoring
* Logging
* Tracing
* Alerting

Deliverables:

* CI/CD pipeline
* Centralized logging
* Distributed tracing
* Production monitoring

Status:
Not Started

---

# Architecture Decisions (ADRs)

Active ADRs:

* ADR-001 Project Vision
* ADR-002 Verification First Development
* ADR-003 Agent Communication Contracts

All future phases must comply with these ADRs.

---

# Engineering Principles

1. Security First
2. Verification First
3. Contract First Agent Communication
4. Cost Aware Design
5. Explainability First
6. Production Before Demo

---

# Current Phase

Phase 1 - Core Runtime

---

# Current Progress

Day 3 Completed

---

# Current Task

Day 4 - Conditional Routing and Dynamic Execution
