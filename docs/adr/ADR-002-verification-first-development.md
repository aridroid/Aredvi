# ADR-002 Verification First Development

## Status

Accepted

## Context

Traditional AI-assisted development often generates code without sufficient mechanisms to verify correctness.

This creates open-loop systems where humans become responsible for identifying failures, hallucinations, regressions, and specification drift.

AREDVI aims to adopt a verification-first engineering culture.

---

## Decision

Every feature, service, agent, workflow, and infrastructure component must define a verification strategy before implementation begins.

Verification may include:

* Type validation
* Contract validation
* Unit tests
* Integration tests
* Runtime validation
* Rule-based validation
* LLM-as-a-Judge
* Evaluation datasets

---

## Consequences

Development may initially be slower.

However:

* Quality improves
* Reliability improves
* Hallucinations decrease
* Regression risk decreases
* Production readiness increases

The system evolves as a closed-loop engineering platform rather than a code-generation project.
