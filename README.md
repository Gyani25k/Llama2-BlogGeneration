# Llama2 Blog Generator

This project is a simple and effective blog generator using the Llama2 model. It leverages various Python libraries to create a streamlined app for generating blog content.

## Why Llama2?

Llama2 is a powerful, open-source language model developed by Meta (formerly Facebook). It is designed to perform exceptionally well on a variety of natural language processing tasks, including text generation, summarization, and more. The 7B variant of Llama2 is particularly well-suited for projects like this due to its balance between model size and performance. It offers high-quality text generation without requiring excessive computational resources, making it an ideal choice for developing a blog generator.

## Why the GGML Model?

The GGML (Generalized Graph Modeling Language) version of Llama2 is optimized for running on consumer-grade hardware, such as CPUs. Unlike other variants that require GPUs to achieve decent performance, GGML models are quantized and structured in a way that allows for efficient CPU inference. This makes it accessible to a broader range of developers and users, allowing you to deploy the model without needing specialized hardware.

## Getting Started

### Prerequisites

- **Python 3.9** (Ensure you have Python 3.9 installed on your system)
- **Conda** (recommended for creating a virtual environment)
- **Git** (for cloning the repository)

### Download the Model

Download the Llama2 model from Hugging Face and place it in the `models` directory inside your project folder.

- **Model:** [Llama2-7B-Chat-GGML](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main)
- **Model Name:** `llama-2-7b-chat.ggmlv3.q8_0.bin`

### Project Structure

Create a project folder and set up the following structure:

```bash
Llama2-BlogGeneration/
│
├── models/
│   └── llama-2-7b-chat.ggmlv3.q8_0.bin
├── app.py
└── requirements.txt
```

### Installation

1. **Clone the Repository**

   You can fork and clone the repository:

   ```bash
   git clone https://github.com/Gyani25k/Llama2-BlogGeneration.git
   ```

2. **Create a Virtual Environment**

   Navigate to your project folder and create a virtual environment:

   ```bash
   conda create --name myenv python=3.9
   conda activate myenv
   ```

3. **Install Required Libraries**

   Install the necessary libraries by running:

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` includes:

   - `sentence-transformers`
   - `uvicorn`
   - `ctransformers`
   - `ipykernel`
   - `langchain`
   - `python-box`
   - `streamlit`

### Running the Application

1. **Open the `app.py` file**

   Edit the file if necessary to suit your configuration or additional requirements.

2. **Run the Application**

   Start the app using Streamlit:

   ```bash
   streamlit run app.py
   ```

## Additional Information

- **IDE Recommendation:** You can use any IDE, but Visual Studio Code (VSCode) is recommended for its integrated terminal and extensive support for Python.
- **Model Directory:** Ensure that the model is correctly placed in the `models` directory. The application won't run without the model.

## Contributing

If you wish to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request.
