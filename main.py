import sys
from crew import EquipeDeAnaliseFinanceiraIa

def run():
    inputs = {'empresa': 'Apple'}
    EquipeDeAnaliseFinanceiraIa().crew().kickoff(inputs=inputs)

def train():
    inputs = {'empresa': 'Apple'}
    EquipeDeAnaliseFinanceiraIa().crew().train(
        n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
    )

def replay():
    EquipeDeAnaliseFinanceiraIa().crew().replay(task_id=sys.argv[1])

def test():
    inputs = {'empresa': 'Apple'}
    EquipeDeAnaliseFinanceiraIa().crew().test(
        n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
    )

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
