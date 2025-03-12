# QueryBot
QueryBot is an intelligent chatbot that allows users to interact with a database via natural language. The bot is designed to query, fetch, and summarize data from a variety of data sources, making it easy to get information without writing complex SQL queries.

<h1>Features</h1>
<br>Natural Language Interface: Users can interact with the database using simple conversational queries.
<br>Database Integration: Connects seamlessly to MySQL database.
<br>Data Summarization: Automatically summarizes large datasets or query results using AI-based summarization techniques.
<br>Custom Query Handling: Supports predefined queries and allows users to define their own queries.
<h1>Technologies Used</h1>
<br>LangChain: For building the natural language interface and connecting the chatbot to the database.
<br>ChatGroq: For text summarization and interaction handling.
<br>Streamlit: For building the user interface.
<br>Python: Primary programming language.
<h1>Installation</h1>
Clone the repository:

```bash
git clone https://github.com/your-username/querybot.git
```
Navigate to the project folder:

```bash
cd querybot
```
Install the required dependencies:

```bash
pip install -r requirements.txt
```
Set up your environment variables (for API keys, database credentials, etc.):

Create a .env file and add your credentials (e.g., GROQ_API_KEY, DB_USER, DB_PASSWORD, etc.).
Usage
Run the Streamlit app:

```bash
streamlit run app.py
```
Once the app is running, go to http://localhost:8501 in your browser.
Start chatting with QueryBot by typing your database-related queries in the input box. QueryBot will interact with the database and respond with the appropriate results.

<h1>Example Use Cases</h1>
<br>Querying data: Ask the bot to retrieve data based on certain conditions (e.g., "Show me all customers from New York").
<br>Summarizing results: If you get a large result set, the bot can summarize the data for easier understanding.
<br>Custom queries: Users can define custom queries in natural language, and the bot will adapt to generate the correct SQL query.
