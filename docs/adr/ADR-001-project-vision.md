# ADR-001 Project Vision

## Status

Accepted

## Date

2026-06-01

## Context

The goal of AREDVI is to build Aredvi Picks, an AI-powered investment intelligence platform.

Most stock market platforms provide buy/sell recommendations without clearly explaining:

* Why a stock was selected
* What signals contributed to the recommendation
* How confident the system is
* What risks exist
* When conditions have changed

Investors often receive conclusions without transparency.

Aredvi Picks aims to provide a transparent, explainable, and data-driven investment research platform rather than a tip-based investing platform.

The project serves two purposes:

1. Build a real AI-powered investment intelligence platform.
2. Provide hands-on experience across the full software engineering lifecycle.

---

## Decision

AREDVI will be built as an AI-powered investment intelligence platform featuring:

### Core Product Features

* Automated Daily Stock Screening
* Momentum Analysis Agent
* Fundamental Growth Agent
* News & Sentiment Agent
* Signal Fusion Engine
* Aredvi Picks Generator
* Explainable AI Dashboard
* Screening History
* Institutional Activity Intelligence
* Bulk Deals Intelligence
* Market Footprint Tracking
* Watchlists
* Alerts & Notifications
* Portfolio Tracking
* Risk Analysis
* Backtesting Engine
* Sector Intelligence
* AI Research Assistant

---

## Technology Stack

AREDVI will be built using:

* LangGraph
* FastAPI
* PostgreSQL
* pgvector
* Redis
* React
* Docker
* Kubernetes
* AWS

---

## Architecture Priorities

The architecture will prioritize:

* Security
* Verification First Development
* Explainability
* Scalability
* Observability
* Cost Optimization
* Enterprise Engineering Practices

---

## Consequences

Development may be slower than typical tutorial projects.

However:

* The platform will reflect real-world production systems.
* Investment recommendations become explainable rather than opaque.
* Agent outputs become verifiable.
* Financial intelligence workflows become transparent.
* The project provides deep experience across software engineering, AI systems, data engineering, cloud infrastructure, and production operations.

AREDVI will prioritize transparency, verification, and explainability over black-box recommendations.
