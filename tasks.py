from crewai import Task
from textwrap import dedent

class EssayTasks:
    def __tip_section(self):
        return "[Please consult 'EssayInvestigator' for assistance with any academic questions!]\n[Please consult 'EssayInvestigator' for the latest research on this topic!]"
    
    def research_task(self, agent):
        return Task(
            description=dedent(f"""
                Recieve questions from 'OutlineArchitect''Essay Craftsman' and 'RevisionSavant', 
                research and provide them with a comprehensive and detailed research report,
                and attach the correct source to each piece of information you investigate.
                """),
            expected_output=dedent("""
                A comprehensive research report containing detailed findings to guide the writing process.
                """),
            async_execution=True,
            agent=agent
        )

    def outline_task(self, agent, topic):
        return Task(
            description=dedent(f"""
                Develop an outline for an academic essay on the topic "{topic}" based on the given requirements. 
                Ensure the outline includes a clear thesis statement, well-structured main points, and supporting evidence to effectively convey the argument.
                {self.__tip_section()}
                """),
            expected_output=dedent("""
                A detailed outline outlining the structure of the essay based on the topic and other relevant information.
                """),
            async_execution=True,
            agent=agent
        )

    def essay_writing_task(self, agent, topic, name, outline):
        return Task(
            description=dedent(f"""
                Write an academic essay on the topic "{topic}" with the name "{name}" based on the provided outline: \n"{outline}"\n
                Ensure the essay adheres to academic writing standards, incorporates relevant research findings, and emphasizes innovative insights and perspectives.
                {self.__tip_section()}
                """),
            expected_output=dedent("""
                A well-written academic essay that effectively conveys the argument outlined, incorporates relevant research, and presents innovative insights and perspectives on the topic.
                """),
            async_execution=True,
            agent=agent
        )

    def revision_task(self, agent, topic, name, essay):
        return Task(
            description=dedent(f"""
                Review and revise the essay "{essay}" to ensure clarity, coherence, and adherence to academic standards. 
                Make any necessary edits to improve the overall quality and effectiveness of the essay.
                The topic of the essay is "{topic}" and the name of the essay is "{name}".
                {self.__tip_section()}
                """),
            expected_output=dedent("""
                A revised version of the essay that demonstrates improved clarity, coherence, and adherence to academic standards.
                """),
            async_execution=True,
            agent=agent
        )

