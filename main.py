from swarm import Swarm, Agent

client = Swarm()

def transfer_to_product_agent():
    return product_agent

def transfer_to_weather_agent():
    return weather_agent

triage_agent = Agent(
    name="Triage Agent",
    instructions="Analyze user queries and transfer to the appropriate specialized agent.",
    functions=[transfer_to_product_agent, transfer_to_weather_agent]
)

product_agent = Agent(
    name="Product Agent",
    instructions="You are an expert on our product catalog. We only have things for rainy days."
)

weather_agent = Agent(
    name="Weather Agent",
    instructions="You are a weather expert. It's sunny all day."
)

response = client.run(
    agent=triage_agent,
    messages=[{"role": "user", "content": "What are the best products?"}]
)

print(response.agent.name)  # used agent
print(response.messages[-1]["content"])  # agents response
