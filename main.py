from init import *
from model import *
from function import save
from agents import EssayAgents
from tasks import EssayTasks
import os

class EssayCrew:
    def __init__(self, idea, name):
        self.idea = idea
        self.name = name
        self.model = using_model

    def run(self):
        agents = EssayAgents()
        tasks = EssayTasks()

        # Define agents
        abstract_writer = agents.abstract_writing_agent()
        introduction_writer = agents.introduction_writing_agent()
        system_composition_writer = agents.system_composition_writing_agent()
        system_principle_writer = agents.system_principle_writing_agent()
        result_analysis_writer = agents.result_analysis_writing_agent()
        innovation_points_writer = agents.innovation_points_writing_agent()
        market_prospect_writer = agents.market_prospect_writing_agent()
        conclusion_writer = agents.conclusion_writing_agent()
        bibliography_writer = agents.bibliography_writing_agent()

        # Define tasks
        abstract_task = tasks.abstract_writing_task(abstract_writer, self.idea, self.name)
        context = [abstract_task]
        introduction_task = tasks.introduction_writing_task(introduction_writer, self.idea, self.name, context)
        context = [context, introduction_task]
        system_composition_task = tasks.system_composition_writing_task(system_composition_writer, self.idea, self.name, context)
        context = [context, system_composition_task]
        system_principle_task = tasks.system_principle_writing_task(system_principle_writer, self.idea, self.name, context)
        context = [context, system_principle_task]
        result_analysis_task = tasks.result_analysis_writing_task(result_analysis_writer, self.idea, self.name, context)
        context = [context, result_analysis_task]
        innovation_points_task = tasks.innovation_points_writing_task(innovation_points_writer, self.idea, self.name, context)
        context = [context, innovation_points_task]
        market_prospect_task = tasks.market_prospect_writing_task(market_prospect_writer, self.idea, self.name, context)
        context = [context, market_prospect_task]
        conclusion_task = tasks.conclusion_writing_task(conclusion_writer, self.idea, self.name, context)
        context = [context, conclusion_task]
        bibliography_task = tasks.bibliography_writing_task(bibliography_writer, self.idea, self.name, context)
        
        # Define crew
        crew = Crew(
            agents=[abstract_writer, introduction_writer, system_composition_writer, system_principle_writer, result_analysis_writer, innovation_points_writer, market_prospect_writer, conclusion_writer, bibliography_writer],
            tasks=[abstract_task, introduction_task, system_composition_task, system_principle_task, result_analysis_task, innovation_points_task, market_prospect_task, conclusion_task, bibliography_task],
            manager_llm=self.model,
            process=Process.sequential,
            verbose=2,
        )

        # Run the crew
        crew.kickoff()
        save(abstract_task.output.raw_output, introduction_task.output.raw_output, system_composition_task.output.raw_output, system_principle_task.output.raw_output, result_analysis_task.output.raw_output, innovation_points_task.output.raw_output, market_prospect_task.output.raw_output, conclusion_task.output.raw_output, bibliography_task.output.raw_output, self.name)
        print(crew.usage_metrics)

def main_run(idea, name):
    essay_crew = EssayCrew(idea, name)
    result = essay_crew.run()
    return result

if __name__ == "__main__":
    print("## easyessay ##")
    print("---------------")
    idea = input(dedent("""What's your idea?"""))
    name = input(dedent("""Name the essay:"""))
    essay_crew = EssayCrew(idea, name)
    result = essay_crew.run()
    print("----------------------")
    print("######################")
    print("## Essay Completed! ##")
    print("######################\n")
