# LangChain Project

This project demonstrates the use of LangChain with OpenAI's ChatGPT model to generate reports and summaries.

## Features

- Generate detailed reports on specified topics
- Create summaries of the generated reports
- Uses LangChain's prompt templates for structured inputs

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install langchain langchain-openai python-dotenv
   ```
3. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the main script:

```
python chatmodel/output.py
```

This will generate a detailed report on black holes and then create a summary of that report.

## Project Structure

- `chatmodel/output.py`: Main script that demonstrates the use of LangChain with OpenAI's ChatGPT model

## License

MIT 