from autograde.parser import load_assignment
from autograde.engines.html_engine import HtmlEngine
import json

def main():

    assignment = load_assignment("examples/week1/assignment.yml")

    print("===================================")
    print(" AutoGrade Runner")
    print("===================================")

    print()
    print(f"Title  : {assignment['title']}")
    print(f"Engine : {assignment['engine']}")
    print()

    engine = HtmlEngine()

    result = engine.grade(
        assignment,
        "submissions/student1"
    )

    print("Results")
    print("-------")

    for test in result.tests:

        if test.passed:
            print(f"✓ {test.name} ({test.points} pts)")
        else:
            print(f"✗ {test.name} (0/{test.points} pts)")

    print()
    print(f"Total: {result.score}/{result.max_score}")

    with open("grade.json", "w", encoding="utf-8") as file:
        json.dump(
            {
                "score": result.score,
                "max_score": result.max_score,
                "tests": [
                    {
                        "name": test.name,
                        "passed": test.passed,
                        "points": test.points
                    }
                    for test in result.tests
                ]
            },
            file,
            indent=4
        )

    print()
    print("grade.json generated.")
    
if __name__ == "__main__":
    main()