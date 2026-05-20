from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent

from typing import List

from app_store.tools.keyword_length_validator import KeywordLengthValidator


@CrewBase
class AppStoreCrew():
    """App Store Listing Writer Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # ---------------- AGENTS ---------------- #

    @agent
    def value_proposition_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config["value_proposition_extractor"],
            verbose=True
        )

    @agent
    def listing_copywriter(self) -> Agent:
        return Agent(
            config=self.agents_config["listing_copywriter"],
            verbose=True,
            tools=[KeywordLengthValidator()]
        )

    @agent
    def screenshot_caption_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["screenshot_caption_writer"],
            verbose=True
        )

    # ---------------- TASKS ---------------- #

    @task
    def value_proposition_extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config["value_proposition_extraction_task"],
            agent=self.value_proposition_extractor()
        )

    @task
    def listing_copywriting_task(self) -> Task:
        return Task(
            config=self.tasks_config["listing_copywriting_task"],
            agent=self.listing_copywriter(),
            output_file="app_listing.md"
        )

    @task
    def screenshot_caption_task(self) -> Task:
        return Task(
            config=self.tasks_config["screenshot_caption_task"],
            agent=self.screenshot_caption_writer(),
            output_file="screenshot_captions.md"
        )

    # ---------------- CREW ---------------- #

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )