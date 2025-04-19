# Chinook DB Natural Language Query Application

This application allows users to query the Chinook music database using natural language instead of SQL. Powered by OpenAI's language models and LangChain, it translates human questions into SQL queries and returns the results in a readable format.

## Prerequisites

- Python 3.7+
- OpenAI API key
- Chinook SQLite database

## Setup Instructions

1. **Clone the repository** (if you're using git)

2. **Install required dependencies**:

3. **Download the Chinook database**:
   - If not already included, download the Chinook SQLite database from [here](https://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip)
   - Extract and place the `chinook.db` file in the same directory as the application

4. **Set up your OpenAI API key** (choose one method):
   - Set as environment variable: `export OPENAI_API_KEY=your-api-key-here`
   - Or enter it directly in the application's sidebar when prompted

## Running the Application

1. Navigate to the application directory:
   ```
   cd /apps/learn_RAGs/codes/streamlit_io
   ```

2. Run the Streamlit application:
   ```
   streamlit run app_agent_prompttomakeSQL_openAI.py
   ```

3. Open your web browser and go to `http://localhost:8501` (or the URL provided in the terminal)

## Using the Application

1. If you haven't set your OpenAI API key as an environment variable, enter it in the sidebar
2. Choose a sample question from the dropdown or enter your own natural language query
3. Click "질문하기" (Ask Question) to process your query
4. View the results, including:
   - The original question
   - The answer to your query
   - The reasoning process that the AI used to generate the SQL query

## Sample Questions

The application includes several sample questions to get you started:
- "가장 많은 음악을 구매한 고객 10명을 보여주세요" (Show the top 10 customers who purchased the most music)
- "어떤 아티스트가 가장 많은 앨범을 가지고 있나요?" (Which artist has the most albums?)
- "장르별 트랙 수와 평균 가격을 알려주세요" (Show the number of tracks and average price by genre)
- And more...

## Troubleshooting

- Make sure the `chinook.db` file is in the same directory as the application
- Verify that your OpenAI API key is valid and has sufficient credits
- For complex queries, try rephrasing your question to be more specific
