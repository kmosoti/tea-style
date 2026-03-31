# Python Project Layout

```text
project/
  pyproject.toml
  README.md
  src/
    app/
      config.py
      interfaces.py
      factories.py
      services/
      models/
  tests/
```

## Why this layout
- configuration is visible
- interfaces and factories are easy to find
- execution logic stays under `src`
- tests follow the structure without mixing with runtime code
