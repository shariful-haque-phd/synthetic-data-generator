# Privacy-Conscious Synthetic Data Generator

Creates a simple synthetic tabular dataset without copying rows verbatim. Numeric fields are sampled from clipped empirical distributions with noise; categorical fields are sampled from observed frequencies.

The included comparison report measures distribution similarity and exact-row overlap.

## Usage
```bash
pip install -r requirements.txt
python src/generate_synthetic.py sample/source.csv --rows 500 --output outputs/synthetic.csv
```

This is an educational baseline, not a formal privacy guarantee. For sensitive production data, use a validated privacy-preserving synthesis method and an appropriate risk assessment.
