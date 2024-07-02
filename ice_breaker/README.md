# Ice Breaker
My hands-on practice with LangChain based on the [LangChain- Develop LLM powered applications with LangChain](https://www.udemy.com/share/108yCa3@zzGfocqzUizLBULtuHos6zu5H7QPdUSuGwjetIQ66Xubw_RTGHu4C6O_cjn3WVeKcQ==/) Udemy course by Eden Marco.

Ice Breaker is a simple LLM application that gets a full name as input and generates a short summary about the person based on the data fetched from the LinkedIn profile.

### Configuration
Before running the code, you need to install the following dependencies:
```bash
pip install -r requirements.txt
```

Then, sign up to the following third-party services and get the API keys:
1. [OpenAI](https://platform.openai.com/)
2. [ProxyCurl](https://proxycurl.com/)
3. [Tavily](https://tavily.com/)


And then add .env file under the root directory with the following content:
```
MOCK=False  # Set to True to work with mock data
MOCK_LINKEDIN_PROFILE_API_ENDPOINT=[optional: an accessible endpoint url returning a mocked linkedin profile json]

OPENAI_API_KEY=[your openai api key]
PROXYCURL_API_KEY=[proxycurl api key]
TAVILY_API_KEY=tvly-[tavily api key]
LANGSMITH_API_KEY=[langsmith api key]
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_PROJECT="ice_breaker"
```

### Execution
1. Run app.py
2. Go to http://localhost:8080
3. Enter your name and click on the button

