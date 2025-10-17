# 🐙 GitHub Repository Language Analysis

## 🎯 Project Goal
The objective of this project was to acquire real-world data from the GitHub Public API and analyze the programming language distribution across repositories belonging to a major organization. This demonstrates proficiency in API integration, JSON processing, data cleaning, and data visualization.

## ⚙️ Project Workflow & Skills Used
1.  **Data Acquisition:** Used the `requests` library to fetch JSON data from the GitHub API.
2.  **Data Cleaning:** Handled missing values (`None`) in the 'language' field using Pandas `.fillna()`.
3.  **Analysis:** Used `.groupby()` and `.size()` to calculate the frequency of each programming language.
4.  **Visualization:** Generated a bar chart using `matplotlib` to present the final distribution.

## 📊 Key Findings
The analysis revealed a dominant focus on **JavaScript** (9 repositories), indicating a strong emphasis on web-based client-side development and tooling. **Python** and **C++** (4 repositories each) form the foundation for backend infrastructure and high-performance applications.

## 📈 Visualization

*(You would paste the image of your final chart here if you were submitting this to a web page, or simply include the descriptive title)*

## 🛠️ How to Run the Code
1.  **Clone the Repository:**
    ```bash
    git clone [Paste the GitHub HTTPS URL here]
    ```
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Execute:** Run the primary script/notebook to reproduce the analysis.
