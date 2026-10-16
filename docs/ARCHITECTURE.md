# Architecture — Synthetic Data Generator

```mermaid
flowchart LR
    A["source.csv"] --> B["generate_synthetic.py"]
    B --> C["synthetic.csv"]
```

## Inputs

- `sample/source.csv`

## Source files

- `src/generate_synthetic.py`

## Output

- `results/artifacts/synthetic.csv`

This representation is intended for source navigation. It does not imply a production deployment or undisclosed components. The editable diagram is available as [`architecture.mmd`](architecture.mmd).
