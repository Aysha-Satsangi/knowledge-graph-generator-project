## Knowledge Graph Generator Web App

![Demo](https://img.shields.io/badge/Status-Deployed-brightgreen)
[🔗 Live Demo](https://knowledge-graph-generator-project.onrender.com/)

This web application extracts key entities and relationships from user input in the form of **Text**, **PDF**, or **URL**, and generates an interactive **Knowledge Graph**. It utilizes advanced **Natural Language Processing (NLP)** techniques such as **spaCy**, **Named Entity Recognition (NER)**, and **dependency parsing**.

---

## Features

- Accepts input from:
  - Plain text
  - PDF file upload
  - URL of a web page
- Extracts:
  - Named Entities (Person, Organization, Location, etc.)
  - Contextual relationships
- Visualizes data as an interactive **Knowledge Graph**
- Displays structured **JSON output** of extracted entities
- Deployed on [Render](https://render.com/)

---

## Use Cases

- Educational tools for learning NLP & Knowledge Representation
- Semantic search and contextual web crawling
- Preprocessing pipeline for knowledge-based AI systems
- Research visualization

---

## Tech Stack

| Layer        | Technology                   |
|--------------|-------------------------------|
| Frontend     | HTML, CSS, JavaScript         |
| Backend      | Flask (Python)                |
| NLP Engine   | spaCy                         |
| File Parsing | PyMuPDF, BeautifulSoup        |
| Visualization| D3.js / Vis.js / NetworkX     |
| Deployment   | Render                        |

---

##  How It Works

1. **User Input**: Accepts either raw text, a PDF file, or a URL.
2. **Processing**:
   - Cleans and parses the input
   - Extracts named entities and syntactic dependencies using **spaCy**
   - Forms relations and connections between entities
3. **Output**:
   - Visualized interactive graph
   - Downloadable or viewable JSON format

---

## Local Setup

```bash
# Clone the repository
git clone https://github.com/your-username/knowledge-graph-generator.git
cd knowledge-graph-generator

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
