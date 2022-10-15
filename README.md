# Computational-Intelligence
we were applying some of the Computational Intelligence well-known techniques the Swarm Intelligence SI. A computational intelligent technique based on the collective behavior in decentralized, self-organized systems based on group behavior found in nature, no centralized control structures, provide heuristic to solve difficult problems, can be used in dynamic applications, and has been applied to wide variety of applications
![image](https://user-images.githubusercontent.com/114780478/195977082-9da86a3b-2eaa-4ae9-9628-31f5e1ad51b2.png)
![image](https://user-images.githubusercontent.com/114780478/195977092-f5def587-9c51-49a3-9b04-8c59db075b6f.png)


 





Code Overview
Illustrating the code’s variables and functions. Also, find attached below the final output and the final chart.
Variables:
•	x_id: Refers to particle's position.
•	v_id: Refers to Particle's Velocity.
•	pop_size: Refers to population size.
•	dim: Refers to the number of dimensions.
•	x_fitness: Refers to the particle's current position.
•	p_i: Refers to the particle's best position.
•	particle_bestFit: Refers to the particle's best position.
•	p_g: Refers to the best population for all.
•	global_bestFit: Refers to the best population for all.
•	Cognitive: Refers to the particle’s own best position.
•	Social: Refers to the best position found by the particle’s neighborhood.
•	numItr: Refers to the number of iterations (Stopping Criteria).

Functions:
•	Initializing Population
 
•	Calculating fitness for each particle using the objective function 
Max f (X1, X2) = sin (2X1 - 0.5 π) + 3cos (X2) + 0.5X1
Where -2 ≤ X1 ≤ 3 and -2 ≤ X2 ≤ 1
 



•	Updating the best position for the particle
 
•	Updating both the best position in all the population and its best fitness
 


•	Calculating the particle’s new velocity and position
 

Output:
 
[ 1.69028322e+70 -1.48549656e+34]
4.852533713018531e+69
