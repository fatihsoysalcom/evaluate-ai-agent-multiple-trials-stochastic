import random

# --- Configuration for our simulated AI Agent and Task ---
TARGET_SCORE = 100          # The goal the agent tries to achieve
MAX_STEPS = 10              # Maximum number of actions the agent can take
MIN_STEP_CHANGE = -5        # Minimum score change per action (stochastic element)
MAX_STEP_CHANGE = 15        # Maximum score change per action (stochastic element)
NUM_MULTIPLE_TRIALS = 1000  # Number of trials for robust evaluation

def run_single_agent_trial(trial_id, verbose=True):
    """Simulates one trial of an AI agent attempting to reach a target score.
    The agent's performance is stochastic due to random score changes at each step.
    """
    current_score = 0
    for step in range(MAX_STEPS):
        # This simulates the stochastic (random) behavior of an AI agent.
        # Even with the same starting conditions, the outcome of each step varies.
        change = random.randint(MIN_STEP_CHANGE, MAX_STEP_CHANGE)
        current_score += change
        if current_score >= TARGET_SCORE:
            break # Agent reached target early
    
    success = current_score >= TARGET_SCORE
    if verbose:
        print(f"  Trial {trial_id:4d}: Final Score = {current_score:4d}, Steps = {step+1:2d}, Success = {success}")
    return success, current_score

# --- Main Demonstration ---
if __name__ == "__main__":
    print("--- Demonstrating AI Agent Evaluation with Stochastic Behavior ---")
    print(f"Goal: An AI agent tries to reach a score of {TARGET_SCORE} within {MAX_STEPS} steps.")
    print(f"Each step introduces a random change to the score (between {MIN_STEP_CHANGE} and {MAX_STEP_CHANGE}).\n")

    # 1. Single Trial Evaluation (can be misleading)
    print("1. Running a SINGLE trial to evaluate the agent:")
    single_trial_success, single_trial_score = run_single_agent_trial(1, verbose=True)
    
    # This section highlights the core concept of the article:
    # A single trial's outcome might be an outlier due to random chance.
    print(f"\nObservation: A single trial resulted in {'SUCCESS' if single_trial_success else 'FAILURE'}.")
    print("This single outcome might be due to favorable or unfavorable random events ")
    print("and may not be representative of the agent's true, average capability.\n")

    # 2. Multiple Trials Evaluation (for more reliable assessment)
    print(f"2. Running {NUM_MULTIPLE_TRIALS} MULTIPLE trials to get a more reliable evaluation:")
    successful_trials = 0
    all_final_scores = []

    for i in range(NUM_MULTIPLE_TRIALS):
        # Running many trials helps average out the stochasticity.
        # This provides a more stable and trustworthy performance metric (e.g., success rate).
        success, final_score = run_single_agent_trial(i + 1, verbose=False) # Suppress verbose output for many trials
        if success:
            successful_trials += 1
        all_final_scores.append(final_score)
    
    success_rate = (successful_trials / NUM_MULTIPLE_TRIALS) * 100

    print(f"\n--- Evaluation Summary Over {NUM_MULTIPLE_TRIALS} Trials ---")
    print(f"Total Trials: {NUM_MULTIPLE_TRIALS}")
    print(f"Successful Trials: {successful_trials}")
    print(f"Failure Trials: {NUM_MULTIPLE_TRIALS - successful_trials}")
    # This is the key takeaway: multiple trials provide a robust success rate.
    print(f"Overall Success Rate: {success_rate:.2f}%") 
    print("\nConclusion: Running multiple trials provides a more robust and statistically significant ")
    print("assessment of the agent's performance, especially when stochasticity is involved. ")
    print("A single trial can be an outlier and lead to incorrect conclusions about the agent's reliability.")
