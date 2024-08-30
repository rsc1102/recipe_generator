# Recipe Generator

A web application that provides AI-driven recipe creation based on user-input ingredients and preferences. This project leverages Python, Django, and the OpenAI API to offer personalized, real-time recipe suggestions.

## Table of Contents
- [Recipe Generator](#recipe-generator)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Technologies Used](#technologies-used)
  - [Installation](#installation)
  - [Usage](#usage)

## Introduction

The Recipe Generator is a Django-based web application that generates recipe suggestions based on the ingredients and preferences input by the user. It uses the OpenAI API to generate AI-driven recipes in real time, providing an intuitive user experience.

## Technologies Used

- **Python**
- **Django**
- **OpenAI API**

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rsc1102/recipe_generator.git
   cd recipe-generator
   ```
2. Set up a virtual environment:
   ```bash
    python3 -m venv env
    source env/bin/activate
   ```
3. Install dependencies:
   ```bash
    pip install -r requirements.txt
   ```
4. Set up environment variables: Create a .env file in the root directory and add your OpenAI API key:
   ```bash
    OPENAI_API_KEY=your_openai_api_key
   ```
5. Start the development server:
   ```bash
    python manage.py runserver
   ```

## Usage

Open your browser and navigate to http://127.0.0.1:8000/.