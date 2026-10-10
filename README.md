
# The Impact of Social Media Advertising on University Students’ Online Shopping Behavior

## Authors
- Mukhantaikyzy Madina
- Shabdanbek Meruyert

## Overview
This project studies how social media advertising is related to university students' online shopping behavior. We focus on advertising exposure, perceived credibility, purchase intention, and purchase decisions.

## Research Questions
1. How do university students perceive and interact with social media advertising when shopping online?
2. How is exposure to social media advertising related to online purchase intentions?
3. How is perceived advertising credibility related to online purchase decisions?

## Research Method
We plan to conduct a quantitative survey among university students. We will use Python to check the collected data and calculate statistical measures.

The initial sample dataset is synthetic and is used only to test the pipeline.

## Planned Benchmarks

| Metric | Purpose |
|---|---|
| Spearman correlation | Measure associations between survey variables |
| Missing value rate | Check data completeness |
| Valid response rate | Check survey response quality |
| Execution time | Measure script runtime |

## Project Structure
- `src/` - Python scripts
- `data/sample/` - Small test dataset
- `configs/` - Experiment settings
- `docs/` - Methodology documents
- `results/` - Generated results

## System Requirements
- Python 3.12 or Docker
- Git for cloning the repository
- No external Python packages are required

## Quickstart Guide

This project includes a Python benchmark script that analyzes a small synthetic survey dataset.

### Option 1: Run with Docker

Requirements:
- Git
- Docker

Clone the repository:

```bash
git clone https://github.com/shabdanbekmeruert-commits/social-media-shopping-research.git
```

Open the project folder:

```bash
cd social-media-shopping-research
```

Build and run the Docker container:

```bash
docker build -t social-media-study . && docker run --rm social-media-study
```

### Option 2: Run with Python

Requirements:
- Python 3.12

If you have not cloned the repository yet, follow the cloning instructions above.

Run this command from the project root directory:

```bash
python src/benchmark.py
```

### Expected Output

The script reads the synthetic survey dataset from
`data/sample/survey_sample.csv`.

It calculates:
- Spearman correlation between advertising exposure and purchase intention
- Spearman correlation between advertising credibility and purchase intention
- Mean purchase intention
- Purchase decision rate
- Missing value rate
- Valid response rate
- Execution time

The results are displayed in the terminal and saved to:

`results/benchmark_results.json`

### Reproducibility

The experiment settings are stored in `configs/config.json`.

The Python version is specified in the Dockerfile. No external Python packages are required.

The sample dataset contains eight synthetic responses for testing purposes. It does not represent real research findings.

## Citation

Mukhantaikyzy, M., & Shabdanbek, M. (2026). The Impact of Social Media Advertising on University Students' Online Shopping Behavior. Research project.

## License

MIT License.
