# LLM Journey: Learning AI by Building an LLM Playground

This repository documents my journey of learning about Large Language Models (LLMs) by building an interactive "LLM Playground" web application. Each major concept in the LLM curriculum will correspond to a new feature in the playground, an accompanying article, and a documented step-by-step progress on GitHub.

## Curriculum & Learning Path

We will cover the following topics in sequence, integrating them into the LLM Playground:

1.  **LLM Overview and Foundations**
    *   Pre-Training (Data collection, cleaning, tokenization)
    *   Architecture (neural networks, Transformers, GPT, Llama families)
    *   Text Generation (greedy, beam search, top-k, top-p)
2.  **Post-Training**
    *   Supervised Fine-Tuning (SFT)
    *   Reinforcement Learning and RLHF
3.  **Evaluation**
    *   Traditional metrics, task-specific benchmarks, human evaluation
4.  **Chatbots' Overall Design**

## Project Structure

*   `src/`: Contains the web application code for the LLM Playground.
    *   `index.html`: The main entry point for the web application.
    *   (Future: `app.py`, `static/`, `templates/` etc. for a Flask/Streamlit app)
*   `articles/`: Markdown files for articles explaining the concepts learned.
*   `requirements.txt`: Python dependencies for the project.

## How to Run the Playground (Current State)

1.  Clone the repository:
    `git clone https://github.com/SitaRamSai/llm-journey.git`
    `cd llm-journey`
2.  (Optional but Recommended) Create and activate a virtual environment:
    `python -m venv venv`
    *   `source venv/bin/activate` (macOS/Linux)
    *   `.\venv\Scripts\activate` (Windows)
3.  Navigate to the `src` directory:
    `cd src`
4.  Open `index.html` in your web browser.

## Progress Log (Module 1 in Progress)

## Progress Log

## Progress Log

## Progress Log

## Progress Log

**Module 1: Project Kick-off & Environment Setup**
*   **Status:** Completed
*   **Objective:** Initialized GitHub repository, set up basic project structure, environment, and first web app component.
*   **Article:** "[Why Build an LLM Playground? A Hands-on Approach to AI Learning](articles/01-why-build-llm-playground.md)"
*   **Key Learnings:** Setting up project infrastructure, importance of virtual environments, initial web app scaffolding.
*   **Commit:** [Link to your Module 1 commit on GitHub]

**Module 2: LLM Overview and Foundations**
*   **Status:** Completed
*   **Objective:** Understood LLM basics, language modeling, and updated the web app with a theoretical overview featuring a ByteByteGo-style diagram.
*   **Visual Aid:** ByteByteGo-style diagram explaining LLM Overview and Language Modeling.
*   **Key Learnings:** Core concept of language modeling, what "large" implies in LLMs, high-level function.
*   **Commit:** [Link to your Module 2 commit on GitHub]

**Module 3: Data Collection - The Fuel for LLMs**
*   **Status:** Completed
*   **Objective:** Understood data collection methods and challenges for LLMs, and updated the web app with a visual explanation.
*   **Visual Aid:** ByteByteGo-style diagram illustrating LLM Data Collection.
*   **Key Learnings:** Scale of LLM data, common sources (Common Crawl), challenges (noise, bias, quality).
*   **Commit:** [Link to your Module 3 commit on GitHub]

**Module 4: Data Cleaning - Refining the Raw**
*   **Status:** In Progress
*   **Objective:** Understand the necessity and techniques of data cleaning for LLMs, and update the web app with a visual explanation.
*   **Visual Aid:** ByteByteGo-style diagram illustrating the data cleaning pipeline.
*   **Key Learnings:** Importance of clean data, deduplication, boilerplate removal, low-quality filtering, influential datasets (RefinedWeb, Dolma, FineWeb).