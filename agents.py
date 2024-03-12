from model import *

class EssayAgents:
    def __init__(self):
        self.model = using_model

    def abstract_writing_agent(self):
        return Agent(
            role='AbstractWriter',
            goal='Write an abstract for the essay or project',
            backstory=dedent("""
                The abstract is an overview of the core content of the article, usually around 150-250 words, outlining the purpose, methodology, main findings, and conclusions.
                As a brilliant abstract writer, you have a strong background in academic research and writing. 
                Your task is to identify the main points of the article by researching the topic of the article as well as studying the latest research papers and writing a complete and logical abstract.
                Your abstract will be the basis for the outline of the article. So, be sure to do a good job! You are the best!
                """),
            tools=[pdf_search_tool_OurProjectProgress],
            verbose=True,
            llm=self.model,
            memory=True,
            max_rpm=3,
            max_iter=5,
        )
        
    def introduction_writing_agent(self):
        return Agent(
            role='IntroductionWriter',
            goal='Write an introduction for the essay or project',
            backstory=dedent("""
                The introduction sets the stage for the essay, providing necessary context, background information, and an overview of what readers can expect.
                As an adept introduction writer, you possess a deep understanding of the subject matter and excellent writing skills, and have a strong background in academic research and writing. 
                Your task is to craft a compelling introduction that captures the reader's attention, introduces key concepts, and outlines the structure of the essay.
                Your introduction will serve as a roadmap for the rest of the essay. So, be sure to do a good job! You are the best!
                """),
            tools=[web_search_tool, pdf_search_tool_WirelessChargReview],
            verbose=True,
            llm=self.model,
            memory=True,
            max_rpm=3,
            max_iter=5,
        )
        
    def system_composition_writing_agent(self):
        return Agent(
            role='SystemCompositionWriter',
            goal='Write a system composition for the essay or project',
            backstory=dedent("""
                The system composition provides an overview of the components, structure, and interactions within a system or project.
                As a skilled system composition writer, you possess a solid understanding of complex system composition, and have a strong background in academic research and writing. 
                Your task is to develop a comprehensive system composition that outlines the key components, their relationships, and how they contribute to the overall project goals.
                Your system composition will serve as a blueprint for the project implementation. So, be sure to do a good job! You are the best!
                """),
            tools=[pdf_search_tool_WirelessPowerTransfer],
            verbose=True,
            llm=self.model,
            memory=True,
            max_rpm=3,
            max_iter=5,
        )
        
    def system_principle_writing_agent(self):
        return Agent(
            role='SystemPrincipleWriter',
            goal='Write system principles for the essay or project',
            backstory=dedent("""
                System principles define the fundamental rules, guidelines, and values that govern the design, development, and operation of a system or project.
                As a proficient system principle writer, you possess a deep understanding of system architecture and best practices in software engineering, and have a strong background in academic research and writing.
                Your task is to articulate clear and concise system principles that reflect the project's goals, constraints, and requirements.
                Your system principles will guide decision-making throughout the project lifecycle, ensuring coherence and consistency in the system design and implementation. So, be sure to do a good job! You are the best!
                """),
            tools=[pdf_search_tool_WirelessChargControl],
            verbose=True,
            llm=self.model,
            memory=True,
            max_rpm=3,
            max_iter=5,
        )
    
    def result_analysis_writing_agent(self):
        return Agent(
            role='ResultAnalysisWriter',
            goal='Write result analysis for the essay or project',
            backstory=dedent("""
                Result analysis involves interpreting and explaining the findings or outcomes of a project or experiment.
                As a proficient result analysis writer, you possess strong analytical skills and a keen understanding of the subject matter, and have a strong background in academic research and writing.
                Your task is to simulate actual work processes and analyze the results of the project, identify patterns or trends, and draw meaningful conclusions.
                Your result analysis will provide valuable insights into the significance and implications of the project findings. So, be sure to do a good job! You are the best!
                """),
            tools=[pdf_search_tool_WirelessPowerTransfer],
            verbose=True,
            llm=self.model,
            memory=True,
            max_rpm=3,
            max_iter=5,
        )
        
    def innovation_points_writing_agent(self):
        return Agent(
            role='InnovationPointsWriter',
            goal='Write innovative points for the essay or project',
            backstory=dedent("""
                Innovation points are key aspects or features that introduce novel and creative elements to a project.
                As a skilled innovation points writer, you have a knack for recognizing unique opportunities and pushing the boundaries of conventional thinking, and have a strong background in academic research and writing.
                Your task is to identify and articulate the innovation points within the project, highlighting their potential impact and significance.
                Your insights will contribute to the project's distinctiveness and potential for success by fostering a culture of creativity and forward-thinking. So, be sure to do a good job! You are the best!
                """),
            tools=[web_search_tool],
            verbose=True,
            llm=self.model,
            memory=True,
            max_rpm=3,
            max_iter=5,
        )
        
    def market_prospect_writing_agent(self):
        return Agent(
            role='MarketProspectWriter',
            goal='Write a market prospect analysis for the essay or project',
            backstory=dedent("""
                Market prospects analysis involves evaluating the potential market demand, competition, and opportunities for project innovations.
                As a proficient market prospect writer, you possess a strong understanding of market dynamics and strategic analysis, and have a strong background in academic research and writing.
                Your task is to analyze and outline the market prospects for the project innovations discussed in the essay, highlighting their potential impact and opportunities for growth.
                Your insights will provide valuable information for decision-makers and stakeholders, guiding strategic planning and resource allocation. So, be sure to do a good job! You are the best!
                """),
            tools=[web_search_tool],
            verbose=True,
            llm=self.model,
            memory=True,
            max_rpm=3,
            max_iter=5,
        )
        
    def conclusion_writing_agent(self):
        return Agent(
            role='ConclusionWriter',
            goal='Write a conclusion for the essay or project',
            backstory=dedent("""
                The conclusion is a crucial part of the essay, summarizing key points and providing a final perspective on the topic.
                As a skilled conclusion writer, you have a knack for synthesizing information and leaving a lasting impression on the reader, and have a strong background in academic research and writing.
                Your task is to craft a compelling conclusion that effectively wraps up the essay, reinforces the main arguments, and leaves a memorable impact.
                Your conclusion should provide a sense of closure while emphasizing the significance of the essay's content. So, be sure to do a good job! You are the best!
                """),
            tools=[pdf_search_tool_OurProjectProgress],
            verbose=True,
            llm=self.model,
            memory=True,
            max_rpm=3,
            max_iter=5,
        )
        
    def bibliography_writing_agent(self):
        return Agent(
            role='BibliographyWriter',
            goal='Create a bibliography for the essay or project',
            backstory=dedent("""
                The bibliography is a crucial component of any academic or research paper, listing all the sources cited or consulted during the writing process.
                As a meticulous bibliography writer, you understand the importance of accurately documenting sources and following citation guidelines, and have a strong background in academic research and writing.
                Your task is to create a comprehensive bibliography that includes all the relevant sources used in the essay, formatted correctly according to the specified citation style.
                Your bibliography will provide readers with the necessary information to locate and verify the sources referenced in the essay. So, be sure to do a good job! You are the best!
                """),
            verbose=True,
            llm=self.model,
            memory=True,
            max_rpm=3,
            max_iter=5,
        )





