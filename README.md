# Somersaulting Spider Optimizer (SSO)  

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)   [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  

---

The **Somersaulting Spider Optimizer (SSO)** is a novel metaheuristic optimization algorithm inspired by the dynamic movement strategies of somersaulting spiders.  
By simulating their ability to alternate between high-mobility somersaults and agile rolling behaviors, SSO provides a powerful framework for efficiently solving challenging optimization problems across academic and industrial domains.

---

## 📖 Description  

SSO belongs to the family of nature-inspired optimization algorithms, drawing inspiration from the behavioral ecology of somersaulting spiders.  
Unlike classical optimization methods, SSO alternates between two biologically inspired strategies—**somersaulting** (for global exploration) and **rolling** (for local exploitation)—allowing the algorithm to balance diversification and intensification effectively.  
This adaptive mechanism ensures strong performance on complex, high-dimensional optimization problems.  

SSO is particularly well-suited for global optimization tasks in:  

- Engineering  
- Machine Learning  
- Data Science  
- Artificial Intelligence  
- Operations Research  

---

## ✨ Features  

- **Somersaulting Movement** → Enables global exploration and avoids local optima.  
- **Rolling Movement** → Focuses on local exploitation and solution refinement.  
- **Adaptive Energy Mechanism** → Dynamic adaptation to prevent stagnation.  
- **Broad Applicability** → Handles both continuous and discrete optimization.  
- **Modular Design** → Easy integration with custom objective functions.  

---

## ⚙️ How It Works  

1. **Initialization** → Randomly generate candidate solutions.  
2. **Evaluation** → Compute fitness using the objective function.  
3. **Somersaulting & Rolling** → Alternate between global and local search.  
4. **Adaptation** → Update energy levels and stagnation counters.  
5. **Convergence** → Stop when iteration limit or stopping criterion is met.  

---

## 🚀 Usage  

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
```



## 📄 License

This project is licensed under the [MIT License](LICENSE).

