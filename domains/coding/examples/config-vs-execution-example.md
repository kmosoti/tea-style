# Config vs Execution Example

## Preferred
`config.py` loads and validates settings.
`service.py` performs work using already validated objects.

## Not preferred
A service that reads environment variables or raw YAML at arbitrary points during execution.

## Reason
Mixing config lookup into execution makes testing harder and behavior less legible.
