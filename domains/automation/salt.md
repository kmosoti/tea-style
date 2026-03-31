# Salt

Salt fits well when configuration, targeting, and orchestration need to stay close to infrastructure reality.

## Preference
Use pillars and states deliberately. Keep data in configuration paths and keep execution logic in states or orchestration code.

## Anti-pattern
Salt logic that hides source-of-truth boundaries or duplicates state across layers.
