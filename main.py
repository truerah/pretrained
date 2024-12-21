import numpy as np
import pandas as pd
import sys

def load(file_path):
    return pd.read_csv(file_path)

def topsis(data, weights, impacts):
   
    metrics = ['Cosine Similarity', 'Jaccard Similarity', 'Euclidean Distance', 'Manhattan Distance', 'BLEU Score', 'ROUGE Score', 'Perplexity']
    
    normalized_data = data[metrics] /  np.sqrt((data[metrics] ** 2).sum())

    for i, col in enumerate(metrics):
        normalized_data[col] *= weights[col]

        if impacts[col] == '-':
            normalized_data[col] *= -1

    ideal_best = normalized_data.max() 
    ideal_worst = normalized_data.min()  
    
    data['D_Ideal'] = np.sqrt(((normalized_data - ideal_best) ** 2).sum(axis=1))
    data['D_Anti'] = np.sqrt(((normalized_data - ideal_worst) ** 2).sum(axis=1))

    data['Performance_Score'] = data['D_Anti'] / (data['D_Ideal'] + data['D_Anti'])
    
    data['Rank'] = data['Performance_Score'].rank(ascending=False)

    return data[['Text', 'Models'] + metrics + ['Performance_Score', 'Rank']]

def main():
    try:
        if len(sys.argv) != 5:
            raise ValueError("Usage: python topsis.py <input_file> <weights> <impacts> <output_file>")
        
        input_file = sys.argv[1]
        weights_input = sys.argv[2]
        impacts_input = sys.argv[3]
        output_file = sys.argv[4]

        df = load(input_file)

        weights = list(map(float, weights_input.split(',')))
        if len(weights) != 7:
            raise ValueError("Weights must be provided for 7 metrics (Cosine Similarity, Jaccard Similarity, Euclidean Distance, Manhattan Distance, BLEU Score, ROUGE Score, Perplexity).")
        
        weights = [w / sum(weights) for w in weights]
        weights_dict = dict(zip(['Cosine Similarity', 'Jaccard Similarity', 'Euclidean Distance', 'Manhattan Distance', 'BLEU Score', 'ROUGE Score', 'Perplexity'], weights))

        impacts = impacts_input.split(',')
        if len(impacts) != 7:
            raise ValueError("Impacts must be provided for 7 metrics (Cosine Similarity, Jaccard Similarity, Euclidean Distance, Manhattan Distance, BLEU Score, ROUGE Score, Perplexity).")
        
        impacts_dict = dict(zip(['Cosine Similarity', 'Jaccard Similarity', 'Euclidean Distance', 'Manhattan Distance', 'BLEU Score', 'ROUGE Score', 'Perplexity'], impacts))

        results = pd.DataFrame()  
        for text, group in df.groupby('Text'):
            topsis_results = topsis(group, weights_dict, impacts_dict)
            results = pd.concat([results, topsis_results])

        results.to_csv(output_file, index=False)

        print(f"TOPSIS results saved to {output_file} successfully.")

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
