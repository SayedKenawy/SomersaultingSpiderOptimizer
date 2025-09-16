"""
@authors: Ahmed Mohamed Zaki & El-Sayed M. El-Kenawy
"""

import random
import numpy
import time
from solution import solution

def SSO(objf, lb, ub, dim, SearchAgents_no, Max_iter):
    """
    Somersaulting Spider Optimizer (SSO) algorithm inspired by
    the kinematic and dynamic model of Cebrennus rechenbergi spider.
    
    Parameters:
    - objf: Objective function to optimize
    - lb: Lower bounds
    - ub: Upper bounds
    - dim: Number of dimensions
    - SearchAgents_no: Number of search agents
    - Max_iter: Maximum number of iterations
    
    The optimization is inspired by:
    - Somersaulting behavior for exploration
    - Rolling behavior for local search
    - Adaptive movement based on energy levels
    """
    
   
    def somersault_movement(current_pos, target_pos, bounds_l, bounds_u, intensity):
        """Simulate somersaulting movement towards target"""
        new_pos = current_pos.copy()
        direction = target_pos - current_pos
        
        for j in range(len(current_pos)):
            # Somersault rotation component
            rotation_angle = 2 * numpy.pi * random.random()
            rotation_factor = intensity * numpy.sin(rotation_angle)
            
            # Translation towards target
            translation_factor = 0.5 + 0.5 * random.random()
            
            # Combined movement
            new_pos[j] = current_pos[j] + rotation_factor * (bounds_u[j] - bounds_l[j]) * 0.1 + \
                        translation_factor * direction[j]
            
            # Ensure bounds
            new_pos[j] = numpy.clip(new_pos[j], bounds_l[j], bounds_u[j])
        
        return new_pos
    
    def rolling_movement(current_pos, bounds_l, bounds_u, radius_factor):
        """Simulate rolling movement for local exploration"""
        new_pos = current_pos.copy()
        
        for j in range(len(current_pos)):
            # Rolling radius based on search space
            roll_radius = radius_factor * (bounds_u[j] - bounds_l[j]) * 0.05
            
            # Random rolling direction
            roll_angle = 2 * numpy.pi * random.random()
            roll_displacement = roll_radius * numpy.cos(roll_angle)
            
            new_pos[j] = current_pos[j] + roll_displacement
            new_pos[j] = numpy.clip(new_pos[j], bounds_l[j], bounds_u[j])
        
        return new_pos
    
    # Initialize bounds as lists
    if not isinstance(lb, list):
        lb = [lb] * dim
    if not isinstance(ub, list):
        ub = [ub] * dim
    
    # Initialize spider positions
    Positions = numpy.zeros((SearchAgents_no, dim))
    for i in range(dim):
        Positions[:, i] = numpy.random.uniform(0, 1, SearchAgents_no) * (ub[i] - lb[i]) + lb[i]
    
    # Initialize spider properties
    spider_energy = numpy.ones(SearchAgents_no)  # Energy levels
    stagnation_counter = numpy.zeros(SearchAgents_no)  # Stagnation tracking
    personal_best_pos = Positions.copy()
    personal_best_fitness = numpy.full(SearchAgents_no, float('inf'))
    
    # Initialize solution tracking
    Convergence_curve = numpy.zeros(Max_iter)
    s = solution()
    
    print('SSO is optimizing "' + objf.__name__ + '"')
    timerStart = time.time()
    s.startTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    
    # Initialize global best
    best_score = float('inf')
    best_pos = numpy.zeros(dim)
    
    # Main optimization loop
    for t in range(Max_iter):
        # Calculate adaptive parameters
        exploration_factor = 1 - (t / Max_iter)  # Decreases over time
        exploitation_factor = t / Max_iter        # Increases over time
        
        # Evaluate all spiders
        for i in range(SearchAgents_no):
            # Ensure position bounds
            for j in range(dim):
                Positions[i, j] = numpy.clip(Positions[i, j], lb[j], ub[j])
            
            # Evaluate fitness
            fitness = objf(Positions[i, :])
            
            # Update personal best
            if fitness < personal_best_fitness[i]:
                personal_best_fitness[i] = fitness
                personal_best_pos[i] = Positions[i, :].copy()
                stagnation_counter[i] = 0
                spider_energy[i] = min(1.0, spider_energy[i] + 0.1)  # Increase energy
            else:
                stagnation_counter[i] += 1
                spider_energy[i] *= 0.95  # Decrease energy
            
            # Update global best
            if fitness < best_score:
                best_score = fitness
                best_pos = Positions[i, :].copy()
        
        # Update spider positions
        for i in range(SearchAgents_no):
            # Determine behavior based on energy and exploration factor
            behavior_threshold = exploration_factor * spider_energy[i]
            
            if random.random() < behavior_threshold:
                # Somersaulting behavior (exploration)
                if stagnation_counter[i] > 5:
                    # Aggressive somersault towards random position
                    random_target = numpy.array([random.uniform(lb[j], ub[j]) for j in range(dim)])
                    Positions[i] = somersault_movement(
                        Positions[i], random_target, lb, ub, 
                        0.8 * exploration_factor
                    )
                else:
                    # Directed somersault towards global best
                    Positions[i] = somersault_movement(
                        Positions[i], best_pos, lb, ub, 
                        0.6 * exploration_factor
                    )
            else:
                # Rolling behavior (exploitation)
                if random.random() < 0.5:
                    # Roll towards personal best
                    Positions[i] = rolling_movement(
                        Positions[i], lb, ub, 
                        exploitation_factor
                    )
                else:
                    # Traditional update towards global best
                    for j in range(dim):
                        r1 = random.random()
                        r2 = random.random()
                        
                        # Movement towards global best with random component
                        Positions[i, j] += r1 * (best_pos[j] - Positions[i, j]) + \
                                         r2 * (random.random() - 0.5) * (ub[j] - lb[j]) * 0.1
                        
                        # Ensure bounds
                        Positions[i, j] = numpy.clip(Positions[i, j], lb[j], ub[j])
            
            # Energy-based position adjustment
            if spider_energy[i] < 0.2:
                # Low energy: conservative movement
                for j in range(dim):
                    Positions[i, j] = 0.9 * Positions[i, j] + 0.1 * best_pos[j]
                    Positions[i, j] = numpy.clip(Positions[i, j], lb[j], ub[j])
                
                # Reset energy after rest
                spider_energy[i] = 1.0
        
        # Store convergence data
        Convergence_curve[t] = best_score
        
        # Print progress
        if t % 10 == 0:
            print(f"At iteration {t} the best fitness is {best_score}")
    
    # Finalize solution
    timerEnd = time.time()
    s.endTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime = timerEnd - timerStart
    s.convergence = Convergence_curve
    s.optimizer = "SSO"
    s.objfname = objf.__name__
    s.bestIndividual = best_pos
    s.best = best_score
    
    return s
