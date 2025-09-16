# Somersaulting Spider Optimizer (SSO)

The **Somersaulting Spider Optimizer (SSO)** is an advanced metaheuristic optimization algorithm inspired by the dynamic movement strategies observed in Somersaulting Spiders.  
By modeling their ability to alternate between high-mobility somersaults and agile rolling behaviors, SSO provides a robust framework for efficiently solving challenging optimization problems in both academic and industrial domains.

Developed and maintained by **Ahmed Mohamed Zaki** and **El-Sayed M. El-Kenawy**.

---

## Description

SSO belongs to the family of nature-inspired optimization algorithms, drawing on the behavioral ecology of Somersaulting Spiders.  
Unlike many classical optimization methods, SSO alternates between two biologically-inspired strategies—**somersaulting** (for global exploration) and **rolling** (for local exploitation)—allowing the algorithm to effectively balance diversification and intensification.  
This adaptive mechanism ensures effective performance on complex, high-dimensional optimization problems.

SSO is particularly well-suited for global optimization tasks found in engineering, machine learning, data science, artificial intelligence, operations research, and more.

---

## Features

- **Somersaulting Movement:**  
  Implements a global exploration strategy, enabling candidate solutions to traverse the search space and escape local optima.
- **Rolling Movement:**  
  Facilitates local search around promising regions, improving solution refinement and precision.
- **Adaptive Energy Mechanism:**  
  Each candidate is assigned an energy level that adapts based on progress, promoting diverse search behavior and avoiding stagnation.
- **Broad Applicability:**  
  Capable of handling both continuous and discrete optimization problems.
- **Modular Design:**  
  Easily integrated into existing projects by specifying an objective function and bounds.

---

## How It Works

1. **Initialization:**  
   Randomly generates a population of candidate solutions within user-defined bounds.
2. **Evaluation:**  
   Each candidate is evaluated using the user-provided objective function to determine its fitness.
3. **Somersaulting and Rolling:**  
   Candidates may perform a somersault (global exploration) or roll (local exploitation) based on their energy and performance, dynamically balancing exploration and exploitation.
4. **Adaptation:**  
   Energy levels and stagnation counters are updated each iteration, with candidates resting to regain energy if stagnation occurs.
5. **Convergence:**  
   The process repeats for a fixed number of iterations or until a stopping criterion is met. The algorithm returns the best solution found and a convergence curve.

---

## Usage

```python
from SSO import SSO

def objective_function(x):
    # Example: Sphere function
    return sum(x**2)

lb = -10
ub = 10
dim = 30
SearchAgents_no = 30
Max_iter = 500

result = SSO(objective_function, lb, ub, dim, SearchAgents_no, Max_iter)
print("Best solution found:", result.bestIndividual)
print("Best fitness value:", result.best)



---

## 📄 License

This project is licensed under the MIT License 

---



**⭐ Star this repository if you find SSO useful for your research or projects!**


