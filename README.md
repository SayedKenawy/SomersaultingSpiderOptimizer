# Somersaulting Spider Optimizer (SSO)

A metaheuristic optimization algorithm inspired by the movement strategies of Somersaulting Spiders.  

## Description

Somersaulting Spider Optimizer (SSO) is a metaheuristic algorithm that mimics the unique behaviors of Somersaulting Spiders. The algorithm alternates between **somersaulting** (for global exploration) and **rolling** (for local exploitation), adaptively balancing both strategies to solve complex optimization problems.  
It is particularly suited for global optimization tasks in engineering, data science, and artificial intelligence.

## Features

- Somersaulting movement for enhanced exploration of the search space.
- Rolling movement for effective local search and exploitation.
- Adaptive energy-based mechanism to avoid stagnation.
- Can be applied to a wide range of continuous or discrete optimization problems.

## How It Works

1. **Initialization:** Generates a population of candidate solutions within defined bounds.
2. **Evaluation:** Measures the fitness of each candidate using the objective function.
3. **Somersaulting and Rolling:** Candidates move either by somersaulting (exploring new regions) or rolling (refining current solutions), based on their energy levels and search progress.
4. **Adaptation:** The algorithm adaptively updates the balance between exploration and exploitation to converge toward the global optimum.

## Usage

```python
from SSO import SSO

def objective_function(x):
    # Define your objective function here
    return sum(x**2)

lb = -10
ub = 10
dim = 30
SearchAgents_no = 30
Max_iter = 500

result = SSO(objective_function, lb, ub, dim, SearchAgents_no, Max_iter)
print("Best solution:", result.bestIndividual)
print("Best fitness:", result.best)
