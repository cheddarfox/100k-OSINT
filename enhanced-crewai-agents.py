from crewai import Agent, Task, Crew
from langchain.llms import OpenAI, Anthropic, VertexAI
from research_tools import research_tool

class EnhancedAgent(Agent):
    async def execute_task(self, task: Task) -> str:
        # Perform research using specialized tools
        search_results = await research_tool.comprehensive_search(task.description)
        
        # Combine the task description with the search results
        enhanced_prompt = f"{task.description}\n\nSearch Results:\n{search_results}"
        
        # Use the agent's language model to process the enhanced prompt
        response = self.llm(enhanced_prompt)
        
        return response

def create_research_crew(topic: str, depth: str):
    if depth == 'shallow':
        llm = OpenAI()
    elif depth == 'medium':
        llm = Anthropic()
    else:
        llm = VertexAI()

    researcher = EnhancedAgent(
        role="Researcher",
        goal="Conduct thorough research on the given topic",
        backstory="Expert researcher with access to various data sources",
        llm=llm
    )

    analyst = EnhancedAgent(
        role="Analyst",
        goal="Analyze research findings and draw insights",
        backstory="Data analyst specializing in OSINT",
        llm=llm
    )

    research_task = Task(
        description=f"Research the topic: {topic}",
        agent=researcher
    )

    analysis_task = Task(
        description="Analyze the research findings and summarize key points",
        agent=analyst
    )

    crew = Crew(
        agents=[researcher, analyst],
        tasks=[research_task, analysis_task],
        verbose=True
    )

    return crew
