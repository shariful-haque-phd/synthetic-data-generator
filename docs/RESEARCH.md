# Research brief — Synthetic Data Generator

**Area:** Data Foundations & Engineering  
**Portfolio level:** Foundations

## Research problem

Creates a simple synthetic tabular dataset without copying rows verbatim. Numeric fields are sampled from clipped empirical distributions with noise; categorical fields are sampled from observed frequencies. The included comparison report measures distribution similarity and exact-row overlap.

## Question

How well does simple tabular resampling preserve distributions without reproducing sensitive records?

## Implementation scope

- Synthetic tabular data baseline

### Reproducible inputs and outputs

The current baseline uses `sample/source.csv`. The implementation consists of `src/generate_synthetic.py`. Execution records, where available, are retained in [`results/`](../results/).

## Evaluation plan

1. Establish a versioned data protocol, input schema and independent baseline.
2. Evaluate functional correctness and record both successful and failed cases.
3. Compare relevant outcomes under controlled input variations and fixed environment settings.
4. Measure resource use and execution time across replicates when meaningful.
5. Document limitations, data provenance and risks of deployment in consequential environments.

### Validity and scope

The included local inputs are not evidence of population-level accuracy or external impact. Any synthetic inputs, simulations, heuristics and estimated performance figures must remain explicitly identified. Future benchmarks should use representative datasets, appropriate baselines, pre-specified metrics and independently reviewed methods.

## Evidence

Refer to [the recorded run](RESULTS.md), or to [the original project instructions](ORIGINAL_README.md) where local execution is not established. No publication, patent, user adoption or real-world deployment is claimed.
