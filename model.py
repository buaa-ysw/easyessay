from crewai import Agent, Task, Crew, Process
from textwrap import dedent

import os
from dotenv import load_dotenv

# 模型导入
from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI

# 从langchain.agents导入工具 google_search_tool
# from langchain.agents import Tool
# from langchain_community.utilities import GoogleSerperAPIWrapper
# os.environ["SERPER_API_KEY"] = "f2262d553f5691749a5420e2a5d3a2b36c84aa62"
# search_tool = GoogleSerperAPIWrapper()
# google_search_tool = [Tool(name="Google Search", func=search_tool.run, description="Search-based queries")]

from crewai_tools import SerperDevTool, PDFSearchTool
os.environ["SERPER_API_KEY"] = "f2262d553f5691749a5420e2a5d3a2b36c84aa62" # serper.dev API key
web_search_tool = SerperDevTool()
pdf_search_tool_WirelessChargReview = PDFSearchTool(pdf="pdf\A Review on UAV Wireless Charging.pdf")
pdf_search_tool_WirelessPowerTransfer = PDFSearchTool(pdf="pdf\Wireless Power Transfer for 3D Printed Unmanned Aerial Vehicle.pdf")
pdf_search_tool_WirelessChargControl = PDFSearchTool(pdf="pdf\蛙跳式充电的无人机自主巡线...基于机器视觉的自动充电控制_刘杰荣.pdf")
pdf_search_tool_OurProjectProgress = PDFSearchTool(pdf="pdf\组会0114.pdf")

# 根据配置文件中的模型名字选择使用的模型 using_model
using_model_name = os.getenv("USING_MODEL")

if using_model_name == 'ollama_openhermes':
    using_model = Ollama(model="openhermes")
elif using_model_name == 'gpt-3.5-turbo':
    using_model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
    load_dotenv()
else:
    raise ValueError("Unsupported default model name")