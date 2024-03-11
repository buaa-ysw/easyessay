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
        essay_investigator = agents.EssayInvestigator()
        outline_architect = agents.OutlineArchitect()
        essay_craftsman = agents.EssayCraftsman()
        revision_savant = agents.RevisionSavant()

        # Define tasks
        research_task = tasks.research_task(essay_investigator, self.idea)
        outline_task = tasks.outline_task(outline_architect, self.idea)
        
        context = [outline_task]
        essay_writing_task = tasks.essay_writing_task(essay_craftsman, self.idea, self.name, context)
        
        context = [essay_writing_task]
        revision_task = tasks.revision_task(revision_savant, self.idea, self.name, context)
        
        # Define crew
        crew = Crew(
            agents=[essay_investigator, outline_architect, essay_craftsman, revision_savant],
            tasks=[research_task, outline_task, essay_writing_task, revision_task],
            manager_llm=self.model,
            process=Process.sequential,
            verbose=2,
        )

        result = crew.kickoff()
        save(research_task.output.raw_output, outline_task.output.raw_output, essay_writing_task.output.raw_output, result, self.name)
        print(crew.usage_metrics)
        return result

def main_run(idea, name):
    essay_crew = EssayCrew(idea, name)
    result = essay_crew.run()
    return result

if __name__ == "__main__":
    print("## easyessay ##")
    print("---------------")
    idea = input(dedent("""What's your idea?"""))
    name = input(dedent("""Name the essay:"""))
    result = main_run(idea, name)
    print("----------------------")
    print("######################")
    print("## Essay Completed! ##")
    print("######################\n")
    print(result)
