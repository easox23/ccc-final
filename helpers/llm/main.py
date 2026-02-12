from dotenv import load_dotenv
from pydantic_ai import Agent

load_dotenv()


agent = Agent(
    'gateway/bedrock:amazon.nova-micro-v1:0'
)

result = agent.run_sync('Hello world!')
print(result)