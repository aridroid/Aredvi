# ADR-003 Agent Communication Contracts

## Status

Accepted

---

## Context

Many Agentic AI systems exchange large natural language messages between agents.

Example:

Agent A generates a long text summary.

Agent B reads the summary.

Agent C reads another summary.

As workflows grow, this approach introduces several problems:

* Increased token consumption
* Information loss through repeated summarization
* Hallucination propagation
* Ambiguous agent responsibilities
* Difficult testing and validation
* Poor scalability

For a production-grade financial intelligence platform, agent communication must be deterministic, testable, and verifiable.

---

## Decision

AREDVI agents will communicate using structured contracts rather than free-form natural language whenever possible.

Contracts will be defined using Pydantic models.

Each agent must explicitly define:

* Input Contract
* Output Contract

Agents should exchange structured objects instead of large text summaries.

---

## Example

Instead of:

Agent A Output:

"Apple appears to have strong revenue growth, a healthy balance sheet, and moderate valuation risk..."

Agent B Input:

Reads the text and attempts to extract meaning.

Use:

```python
class CompanyAnalysis(BaseModel):
    ticker: str
    revenue_growth: float
    debt_ratio: float
    pe_ratio: float
    risk_score: int
```

Agent B receives a validated object instead of unstructured text.

---

## Benefits

### Reduced Token Cost

Structured data consumes fewer tokens than repeated summaries.

---

### Easier Validation

Contracts can be validated automatically using Pydantic.

---

### Lower Hallucination Risk

Agents consume verified fields rather than interpreting prose.

---

### Better Testing

Inputs and outputs can be unit tested without involving LLMs.

---

### Improved Observability

Agent interactions become easier to inspect and debug.

---

### Scalability

New agents can integrate through contract definitions rather than prompt engineering.

---

## Exceptions

Natural language may still be used:

* Final user-facing responses
* Report generation
* Explanation generation
* Reasoning traces when required

However, internal agent-to-agent communication should prefer structured contracts.

---

## Consequences

Development requires additional schema design effort.

However:

* Reliability improves
* Cost decreases
* Validation becomes easier
* Testing becomes easier
* Production readiness improves

AREDVI adopts a contract-first approach for agent communication.
