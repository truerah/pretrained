# TOPSIS Implementation for Pretrained Models with Text Similarity Metrics

This repository provides a Python-based implementation of the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS). The script evaluates pretrained models based on various text similarity and linguistic metrics to assist in multi-criteria decision-making. The method ranks models based on their similarity to an ideal solution.

---

## Features
- **Text Similarity Metrics**: Includes `Cosine Similarity`, `Jaccard Similarity`, `Euclidean Distance`, and `Manhattan Distance`.
- **Linguistic Metrics**: Includes `BLEU Score`, `ROUGE Score`, and `Perplexity`.
- **Decision-Making**: Applies the TOPSIS method to rank pretrained models effectively.
- **Customizable Weights and Impacts**: Specify the importance and direction (maximization or minimization) for each metric.

---

## Installation

To set up the environment for running the TOPSIS script, ensure Python 3.x is installed. Then, install the required dependencies using:

```bash
pip install pandas numpy
```

---

## Usage

Run the script from the command line using:

```bash
python topsis.py <input_file> <weights> <impacts> <output_file>
```

### Parameters:
- `<input_file>`: Path to the CSV file containing data for pretrained models.
- `<weights>`: Comma-separated weights assigned to each metric (7 metrics in total).
- `<impacts>`: Comma-separated signs for each metric (`+` for maximization, `-` for minimization).
- `<output_file>`: Path to save the output CSV file with rankings.

---

## Input Format

The input CSV file should have the following columns:
1. **Text**: Descriptive information or identifier for the data.
2. **Models**: Names of pretrained models being evaluated.
3. **Metrics**: Numeric values for the following seven metrics:
   - `Cosine Similarity`
   - `Jaccard Similarity`
   - `Euclidean Distance`
   - `Manhattan Distance`
   - `BLEU Score`
   - `ROUGE Score`
   - `Perplexity`

### Example:

| Text         | Models   | Cosine Similarity | Jaccard Similarity | Euclidean Distance | Manhattan Distance | BLEU Score | ROUGE Score | Perplexity |
|--------------|----------|-------------------|--------------------|--------------------|--------------------|------------|-------------|------------|
| Sentence A   | Model 1  | 0.85              | 0.78               | 0.12               | 0.25               | 0.67       | 0.74        | 5.4        |
| Sentence A   | Model 2  | 0.83              | 0.76               | 0.15               | 0.28               | 0.65       | 0.70        | 5.6        |

---

## Output Format

The output CSV file will contain the following columns:
1. **Text**: Descriptive information about the data.
2. **Models**: Names of pretrained models being evaluated.
3. **Metrics**: Original metrics from the input file.
4. **Performance_Score**: The calculated score using the TOPSIS method.
5. **Rank**: Rank assigned to each model based on the performance score.

### Example:

| Text         | Models   | Cosine Similarity | Jaccard Similarity | Euclidean Distance | Manhattan Distance | BLEU Score | ROUGE Score | Perplexity | Performance_Score | Rank |
|--------------|----------|-------------------|--------------------|--------------------|--------------------|------------|-------------|------------|--------------------|------|
| Sentence A   | Model 1  | 0.85              | 0.78               | 0.12               | 0.25               | 0.67       | 0.74        | 5.4        | 0.82               | 1    |
| Sentence A   | Model 2  | 0.83              | 0.76               | 0.15               | 0.28               | 0.65       | 0.70        | 5.6        | 0.78               | 2    |

---

## Example Command

```bash
python topsis.py pretrained_models.csv "0.2,0.2,0.15,0.15,0.1,0.1,0.1" "+,+,-,-,+,+,-" results.csv
```

- **Weights**: Assign higher importance to metrics like `Cosine Similarity` and `Jaccard Similarity` (0.2 each).
- **Impacts**: Maximize similarity scores (`+`) and minimize distance metrics (`-`).

---

## Output

After execution, the `results.csv` file will include performance scores and rankings for the models.

---

## License

This project is open-source and distributed under the MIT License. Feel free to use, modify, and distribute it as needed.

---

Let us know if you have any questions or need further assistance!

