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

**Module 1: Project Kick-off & Environment Setup**
*   **Status:** Completed
*   **Objective:** Initialized GitHub repository, set up basic project structure, environment, and first web app component.
*   **Article:** "[Why Build an LLM Playground? A Hands-on Approach to AI Learning](articles/01-why-build-llm-playground.md)"
*   **Key Learnings:** Setting up project infrastructure, importance of virtual environments, initial web app scaffolding.
*   **Commit:** [Link to your Module 1 commit on GitHub] (e.g., `https://github.com/SitaRamSai/llm-journey/commit/YOUR_COMMIT_HASH_HERE`)

**Module 2: LLM Overview and Foundations**
*   **Status:** In Progress
*   **Objective:** Understand LLM basics, language modeling, and update the web app with a theoretical overview featuring a ByteByteGo-style diagram.
*   **Visual Aid:** ByteByteGo-style diagram explaining LLM Overview and Language Modeling.
*   **Key Learnings:** Core concept of language modeling, what "large" implies in LLMs, high-level function.
---

### **Step 4: Write the First Article**

Now, let's write our first article. Create a new file in the `articles` directory named `01-why-build-llm-playground.md`.

Here's a starting point for the content. Feel free to elaborate, add your own perspective, and make it engaging!

```markdown
# Why Build an LLM Playground? A Hands-on Approach to AI Learning

## Introduction
The world of Large Language Models (LLMs) is rapidly expanding, with new models and applications emerging almost daily. For many, the sheer volume of information can be overwhelming. How does one truly grasp the underlying principles beyond just using APIs? This project proposes a unique and deeply immersive answer: by building our own LLM Playground.

## Learning by Doing
The traditional approach to learning often involves reading theory, watching lectures, and perhaps solving some theoretical problems. While valuable, this can leave a gap in practical understanding. Our LLM Playground project aims to bridge this gap. Instead of just studying the Transformer architecture, we'll strive to visualize it. Instead of just reading about tokenization, we'll build a tool to tokenize text ourselves.

## What is an LLM Playground?
Imagine an interactive web application that allows us to explore, understand, and even experiment with the core components of an LLM. This "playground" will start simple, displaying basic concepts, and gradually evolve to include:
*   Visualizations of data processing (cleaning, tokenization)
*   Interactive diagrams of neural network architectures
*   Tools to experiment with text generation strategies
*   Conceptual demonstrations of fine-tuning and evaluation metrics

## The Journey Ahead
Our learning journey will be structured into modules, each focusing on a key aspect of LLM development, from data collection to post-training and evaluation. For every module, we will:
1.  **Understand the Theory:** Dive into the academic and practical concepts.
2.  **Build a Component:** Implement a feature or visualization in our LLM Playground.
3.  **Document Our Progress:** Write an article like this one, explaining our learnings.
4.  **Version Control:** Push our code and articles to GitHub, tracking our development.

## Why This Approach?
*   **Deep Understanding:** Building forces a deeper engagement with the material. You'll encounter and solve problems that solidify your knowledge.
*   **Practical Skills:** You'll gain hands-on experience with Python, web development basics, and fundamental AI libraries.
*   **Portfolio Piece:** The LLM Playground itself, along with the articles and GitHub history, will serve as a strong portfolio piece demonstrating your capabilities.
*   **Community Engagement:** Sharing progress on GitHub can invite feedback and collaboration.

## Conclusion
This project is more than just building an application; it's about embarking on an educational adventure. By actively constructing an LLM Playground, we aim to demystify LLMs, transform theoretical knowledge into practical skills, and create a valuable resource along the way. Join me as we begin this exciting journey!