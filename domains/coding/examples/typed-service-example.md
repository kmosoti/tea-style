# Typed Service Example

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class UserConfig:
    region: str
    timeout_seconds: int

class UserService:
    def __init__(self, config: UserConfig) -> None:
        self._config = config

    def run(self) -> str:
        return f"{self._config.region}:{self._config.timeout_seconds}"
```

## Point
The service consumes validated structure rather than loose input. That keeps execution logic simple.
