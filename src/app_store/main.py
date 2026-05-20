#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from app_store.crew import AppStoreCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    app_input = open("inputs/input.txt", "r").read()
    inputs = {
        'app_input': app_input
    }
    
    result = AppStoreCrew().crew().kickoff(inputs=inputs)

    value_prop = result.tasks_output[0].raw
    listing = result.tasks_output[1].raw
    captions = result.tasks_output[2].raw

    print("\n" + "=" * 60)
    print("VALUE PROPOSITION")
    print("=" * 60)
    print(value_prop)

    print("\n" + "=" * 60)
    print("APP STORE LISTING")
    print("=" * 60)
    print(listing)

    print("\n" + "=" * 60)
    print("SCREENSHOT CAPTIONS")
    print("=" * 60)
    print(captions)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        AppStoreCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AppStoreCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        AppStoreCrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
