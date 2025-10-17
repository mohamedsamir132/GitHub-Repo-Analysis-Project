import pandas as pd
import requests
import json
import matplotlib.pyplot as plt

# --- CONFIGURATION ---
# API endpoint for fetching repositories from the Google organization
GITHUB_API_URL = "https://api.github.com/orgs/google/repos"
OUTPUT_PLOT_FILENAME = "github_language_distribution.png"
OUTPUT_DATA_FILENAME = "language_counts.csv"


# --- TASK 1: DATA ACQUISITION ---

def fetch_github_repos(url):
    """Fetches repository data from the GitHub API and handles the response."""
    try:
        # 1. Send GET request to the API
        response = requests.get(url)
        
        # 2. Check for a successful status code (200 OK)
        if response.status_code == 200:
            # 3. Parse the JSON response into a Python list of dictionaries
            return response.json()
        else:
            print(f"Error fetching data: Status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API request: {e}")
        return None


# --- TASK 2 & 3: CLEANING, ANALYSIS, AND VISUALIZATION ---

def analyze_and_visualize_repos(repo_data):
    """Cleans the data, performs analysis, and generates a plot."""
    if not repo_data:
        print("Analysis stopped due to missing data.")
        return

    # 1. Convert the list of dictionaries into a Pandas DataFrame
    repo_df = pd.DataFrame(repo_data)

    # 2. Data Cleaning: Handle missing 'language' values
    # Repositories without a primary language (e.g., documentation) return None.
    repo_df["language"].fillna("Not Specified", inplace=True)

    # 3. Aggregation: Group by language and count the number of repositories
    # .size() efficiently counts the number of rows in each group.
    language_counts = repo_df.groupby("language").size()

    # 4. Sort results for better visualization and presentation
    language_counts = language_counts.sort_values(ascending=False)

    # 5. Output Data (for documentation/sharing)
    print("\n--- Language Distribution Data (Top 5) ---")
    print(language_counts.head(5).to_string())
    language_counts.to_csv(OUTPUT_DATA_FILENAME, header=['Repository Count'])


    # 6. Visualization: Create a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(language_counts.index, language_counts.values, color='skyblue')
    
    # Add labels and title
    plt.title("Number of Repositories by Primary Programming Language", fontsize=14)
    plt.xlabel("Programming Language", fontsize=12)
    plt.ylabel("Number of Repositories", fontsize=12)
    
    # Rotate x-axis labels for readability (especially for many languages)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout() # Adjust layout to prevent labels from being cut off
    
    # Save the figure to the project directory
    plt.savefig(OUTPUT_PLOT_FILENAME)
    print(f"\nSuccessfully saved plot to {OUTPUT_PLOT_FILENAME}")
    
    # Note: If running in a script, plt.show() would be here.
    # If running in a Jupyter environment, the plot will display automatically.


# --- MAIN EXECUTION BLOCK ---

if __name__ == "__main__":
    # Execute the primary function to get data
    data = fetch_github_repos(GITHUB_API_URL)
    
    # Execute the analysis and visualization function
    analyze_and_visualize_repos(data)