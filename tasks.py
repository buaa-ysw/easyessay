from crewai import Task
from textwrap import dedent

class EssayTasks:    
    def abstract_writing_task(self, agent, topic, name):
        return Task(
            description=dedent(f"""
                Write an abstract for the essay on the topic "{topic}" and the name "{name}".
                The abstract should provide a concise summary of the key points, methodology, main findings, and conclusions of the essay.
                """),
            expected_output=dedent("""
                A well-written abstract that effectively summarizes the key aspects of the essay's topic.
                """),
            agent=agent
        )
        
    def introduction_writing_task(self, agent, topic, name, context):
        return Task(
            description=dedent(f"""
                Write an introduction for the essay on the topic "{topic}" and the name "{name}".
                The introduction should set the stage for the essay, providing necessary context, background information, and an overview of what readers can expect.
                [!! What you write must be logically and content-wise consistent with the ABSTRACT !!]
                """),
            expected_output=dedent("""
                A well-written introduction that effectively introduces the topic and outlines the structure of the essay.
                """),
            agent=agent,
            context=context
        )
        
    def system_composition_writing_task(self, agent, topic, name, context):
        return Task(
            description=dedent(f"""
                Write a system composition for the essay on the topic "{topic}" and the name "{name}".
                The system composition should provide an overview of the components, structure, and interactions within the system or project.
                [!! What you write must be logically and content-wise consistent with the ABSTRACT and the INRTODUCTION !!]
                """),
            expected_output=dedent("""
                A well-written system composition that effectively outlines the key components and their relationships within the project.
                """),
            agent=agent,
            context=context
        )
        
    def system_principle_writing_task(self, agent, topic, name, context):
        return Task(
            description=dedent(f"""
                Write system principles for the essay on the topic "{topic}" and the name "{name}".
                System principles define the fundamental rules, guidelines, and values that govern the design, development, and operation of a system or project.
                [!! What you write must be logically and content-wise consistent with the ABSTRACT, INTRODUCTION, and SYSTEM COMPOSITION !!]
                """),
            expected_output=dedent("""
                A well-defined set of system principles that reflect the project's goals, constraints, and requirements, guiding decision-making and ensuring coherence in the system design and implementation.
                """),
            agent=agent,
            context=context
        )
        
    def result_analysis_writing_task(self, agent, topic, name, context):
        return Task(
            description=dedent(f"""
                Write a result analysis for the essay on the topic "{topic}" and the name "{name}".
                Result analysis involves interpreting and explaining the findings or outcomes of a project or experiment.
                [!! What you write must be logically and content-wise consistent with the ABSTRACT, INTRODUCTION, SYSTEM COMPOSITION, and SYSTEM PRINCIPLES !!]
                """),
            expected_output=dedent("""
                A well-written result analysis that effectively interprets and explains the findings or outcomes of the project, providing valuable insights and implications.
                """),
            agent=agent,
            context=context
        )
        
    def innovation_points_writing_task(self, agent, topic, name, context):
        return Task(
            description=dedent(f"""
                Identify and articulate innovation points for the essay on the topic "{topic}" and the name "{name}".
                Innovation points are key aspects or features that introduce novel and creative elements to a project.
                [!! What you write must be logically and content-wise consistent with the ABSTRACT, INTRODUCTION, SYSTEM COMPOSITION, SYSTEM PRINCIPLES, and RESULT ANALYSIS !!]
                """),
            expected_output=dedent("""
                A well-articulated set of innovation points that effectively highlight the novel and creative elements introduced by the project, showcasing its potential for innovation and impact.
                """),
            agent=agent,
            context=context
        )

    def market_prospect_writing_task(self, agent, topic, name, context):
        return Task(
            description=dedent(f"""
                Analyze and outline market prospects for the essay on the topic "{topic}" and the name "{name}".
                Market prospects analysis involves evaluating the potential market demand, competition, and opportunities for project innovations.
                [!! What you write must be logically and content-wise consistent with the ABSTRACT, INTRODUCTION, SYSTEM COMPOSITION, SYSTEM PRINCIPLES, RESULT ANALYSIS, and INNOVATION POINTS !!]
                """),
            expected_output=dedent("""
                A well-analyzed and outlined market prospects section that effectively evaluates the potential market demand, competition, and opportunities for project innovations, providing valuable insights for stakeholders.
                """),
            agent=agent,
            context=context
        )
        
    def conclusion_writing_task(self, agent, topic, name, context):
        return Task(
            description=dedent(f"""
                Write a conclusion for the essay on the topic "{topic}" and the name "{name}".
                The conclusion should effectively summarize the key points discussed in the essay and provide a final perspective on the topic.
                [!! What you write must be logically and content-wise consistent with the ABSTRACT, INTRODUCTION, SYSTEM COMPOSITION, SYSTEM PRINCIPLES, RESULT ANALYSIS, INNOVATION POINTS, and MARKET PROSPECTS !!]
                """),
            expected_output=dedent("""
                A well-written conclusion that effectively summarizes the key points discussed in the essay, provides a final perspective on the topic, and leaves a lasting impression on the reader.
                """),
            agent=agent,
            context=context
        )
        
    def bibliography_writing_task(self, agent, topic, name, context):
        return Task(
            description=dedent(f"""
                Create a bibliography for the essay on the topic "{topic}" and the name "{name}".
                The bibliography should list all the sources cited or consulted during the writing process, formatted correctly according to the specified citation style.
                [!! What you write must be logically and content-wise consistent with the ABSTRACT, INTRODUCTION, SYSTEM COMPOSITION, SYSTEM PRINCIPLES, RESULT ANALYSIS, INNOVATION POINTS, MARKET PROSPECTS, and CONCLUSION !!]
                """),
            expected_output=dedent("""
                A well-crafted bibliography that accurately documents all the sources cited or consulted during the writing process, formatted correctly according to the specified citation style.
                """),
            agent=agent,
            context=context
        )







