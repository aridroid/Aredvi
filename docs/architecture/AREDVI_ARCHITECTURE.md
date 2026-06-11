# AREDVI ARCHITECTURE

## Project

AREDVI (Aredvi Picks)

Tagline:

"No tips. Just Aredvi."

---

# System Vision

Aredvi Picks is an AI-powered investment intelligence platform that continuously monitors the stock market, analyzes companies using multiple specialized agents, identifies high-conviction opportunities, explains every recommendation, and helps investors make data-driven decisions.

The platform is designed to be transparent, explainable, and verification-driven.

---

# High-Level Architecture

```text
Users
  ↓
React Frontend
  ↓
FastAPI Backend
  ↓
Agent Orchestration Layer (LangGraph)
  ↓
Analysis Agents
  ↓
Signal Fusion Engine
  ↓
Verification Layer
  ↓
Data Layer
  ↓
External Market Data Sources
```

---

# Core System Components

## 1. Frontend Layer

Technology:

* React

Responsibilities:

* User Authentication
* Dashboard
* Stock Discovery
* Watchlists
* Portfolio Tracking
* Alerts
* Research Assistant
* Screening History
* Sector Intelligence
* Backtesting Results

---

## 2. API Layer

Technology:

* FastAPI

Responsibilities:

* Authentication
* User Management
* Portfolio APIs
* Watchlist APIs
* Alert APIs
* Research APIs
* Screening APIs
* Agent Execution APIs

Acts as the gateway between frontend and backend systems.

---

## 3. Agent Orchestration Layer

Technology:

* LangGraph

Responsibilities:

* Agent Workflow Management
* State Management
* Agent Coordination
* Conditional Routing
* Multi-Agent Execution
* Verification Integration

This layer controls how agents collaborate.

---

# Analysis Agent Layer

AREDVI uses multiple specialized agents.

---

## Momentum Agent

Purpose:

Analyze market momentum.

Signals:

* 52-week highs
* Price momentum
* Trend strength
* Technical indicators
* Volume spikes

Output:

```text
Momentum Score
0-100
```

---

## Fundamental Growth Agent

Purpose:

Analyze business quality and growth.

Signals:

* Revenue Growth
* Profit Growth
* EPS Growth
* Quarterly Results
* Financial Health

Output:

```text
Fundamental Score
0-100
```

---

## News & Sentiment Agent

Purpose:

Analyze qualitative signals.

Signals:

* Company Announcements
* Exchange Filings
* News Coverage
* Social Sentiment
* Market Sentiment

Output:

```text
Sentiment Score
0-100
```

---

## Research Agent

Purpose:

Answer investor questions.

Examples:

* Why was this stock selected?
* Compare two companies.
* Summarize quarterly results.
* Explain company announcements.

Uses:

* RAG
* Vector Search
* LLM Reasoning

---

# Signal Fusion Engine

Purpose:

Combine outputs from all analysis agents.

Example:

```text
Momentum      85
Fundamental   90
Sentiment     88
```

Produces:

* Final AI Score
* Confidence Score
* Ranking Score

The Signal Fusion Engine determines whether a stock qualifies as an Aredvi Pick.

---

# Aredvi Picks Generator

Purpose:

Generate final investment opportunities.

Selection Criteria:

* Multiple signals agree
* Confidence threshold achieved
* Risk requirements satisfied

Output Categories:

* Selected Stocks
* Rejected Stocks
* Skipped Stocks

---

# Explainability Layer

Purpose:

Ensure every recommendation is transparent.

Displays:

* Why a stock was selected
* Why a stock was rejected
* Agent Scores
* Confidence Score
* Supporting Signals
* Risk Factors

No black-box recommendations are allowed.

---

# Verification Layer

Core Principle:

Trust Nothing. Verify Everything.

Responsibilities:

* Contract Validation
* Runtime Validation
* Rule Validation
* LLM Judge Evaluation
* Quality Assurance

Every recommendation must pass verification before being presented to users.

---

# Data Layer

## PostgreSQL

Stores:

* Users
* Portfolios
* Watchlists
* Screening Results
* Agent Scores
* Historical Performance
* Alert Configurations

---

## pgvector

Stores:

* Embeddings
* Research Documents
* Company Reports
* Earnings Summaries
* News Content

Supports:

* Semantic Search
* RAG Retrieval

---

## Redis

Stores:

* Cache
* Session Data
* Temporary Workflow State
* Rate Limiting Data

---

# RAG Architecture

Purpose:

Enable intelligent research and question answering.

Workflow:

```text
User Question
        ↓
Research Agent
        ↓
Embedding Search
        ↓
pgvector Retrieval
        ↓
Relevant Documents
        ↓
LLM
        ↓
Verified Response
```

Examples:

* Explain earnings results
* Summarize announcements
* Compare companies
* Explain why a stock was selected

---

# Market Intelligence Layer

Tracks:

* Stock Prices
* Market Data
* Financial Statements
* Corporate Actions
* Earnings Reports
* News Sources
* Institutional Activity
* Bulk Deals
* Block Deals

This layer continuously feeds data into analysis agents.

---

# Alerting System

Supports:

* New Aredvi Pick Alerts
* Momentum Breakout Alerts
* Institutional Activity Alerts
* News Alerts
* Watchlist Alerts

Delivery Channels:

* Email
* Push Notifications
* WhatsApp

---

# Portfolio Intelligence Layer

Provides:

* Portfolio Tracking
* Profit & Loss
* Risk Analysis
* Sector Exposure
* Performance Monitoring

---

# Backtesting Engine

Purpose:

Evaluate strategy effectiveness.

Metrics:

* Win Rate
* CAGR
* Sharpe Ratio
* Maximum Drawdown
* Risk/Reward Ratio

---

# Sector Intelligence Layer

Tracks:

* Sector Momentum
* Earnings Growth
* Capital Flow
* Institutional Interest

Examples:

* Banking
* IT
* Pharma
* Energy
* Defense

---

# Cloud Architecture

Infrastructure:

* AWS

Services:

* API Gateway
* Cognito
* Lambda
* SNS
* SQS
* EventBridge
* RDS PostgreSQL
* ECS/EKS
* CloudWatch

---

# Engineering Principles

1. Security First
2. Verification First
3. Contract First Agent Communication
4. Cost Aware Design
5. Explainability First
6. Production Before Demo

---

# Long-Term Goal

Build a production-grade AI-powered investment intelligence platform capable of:

* Discovering investment opportunities
* Monitoring markets continuously
* Explaining every recommendation
* Tracking institutional money flow
* Supporting investor research
* Delivering transparent AI-driven investment intelligence

without relying on opaque stock tips or black-box recommendations.
