# Architecture Boundaries

## Purpose
Define how TEA expects code boundaries to be shaped before implementation details spread through a system.

## Core claim
Code is easier to reason about when callers depend on typed behavior contracts, not incidental internals.

## Knowledge hooks
- **Type**: domain doctrine
- **Domain**: coding
- **Concepts**: encapsulation, abstraction, protocols, dependency injection, typed models, pure functions
- **Use when**: designing modules, clients, services, or workflows that need stable boundaries

## Definitions
- **Encapsulation**: expose a clean interface and hide messy internals.
- **Abstraction**: represent essential behavior without binding callers to incidental details.
- **Protocol**: a behavior contract that does not require inheritance.
- **Dependency injection**: pass dependencies from the outside instead of constructing them deep inside logic.
- **Functional core**: pure logic that computes decisions without side effects.
- **Imperative shell**: edge code that performs I/O, mutation, logging, and external calls.
- **Invariant**: a rule that must always be true for a model, command, state, or workflow.

## Architecture / Mechanics
Use this boundary flow:

```text
raw external input
  -> validation and normalization
  -> typed domain model
  -> pure decision function
  -> command/result object
  -> side-effecting adapter or executor
```

The core should know domain concepts. It should not know transport details, CLI parsing, SDK quirks, or authentication mechanics.

## Patterns
- Use dataclasses, enums, and typed config instead of loose dictionaries.
- Use protocols for external clients and repositories.
- Inject clients, clocks, random sources, and config when they affect behavior.
- Keep mutation in adapters, executors, or application services.
- Separate commands that mutate from queries that read.
- Define meaningful error types instead of raising generic exceptions everywhere.
- Return result/evidence objects when stakeholders need proof of work.
- Use static analysis, tests, and schemas as guardrails for agent-assisted edits.

## Anti-patterns
- callers reaching through client internals
- service constructors that create every dependency themselves
- domain code importing HTTP clients, CLI parsers, or vendor SDKs
- functions that both compute a plan and mutate production
- boolean flag clusters that allow invalid combinations
- global state controlling environment, auth, dry-run, or target cluster
- vague modules named `utils.py`, `manager.py`, or `processor.py` without cohesive ownership

## Example
```python
from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class Host:
    name: str
    cluster: str
    role: str


class HostProvider(Protocol):
    def get_hosts(self, cluster_name: str) -> list[Host]:
        ...


class RepavePlanner:
    def __init__(self, hosts: HostProvider) -> None:
        self._hosts = hosts

    def plan_cluster(self, cluster_name: str) -> list[Host]:
        return sorted(self._hosts.get_hosts(cluster_name), key=lambda host: host.name)
```

The planner depends on host behavior, not on Salt, Splunk, CMDB, or static YAML.

## Related pages
- [principles.md](principles.md)
- [patterns.md](patterns.md)
- [examples/typed-service-example.md](examples/typed-service-example.md)
- [docs/doctrines/engineering-control-spine.md](../../docs/doctrines/engineering-control-spine.md)
