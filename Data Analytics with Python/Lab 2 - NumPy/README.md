### AI with Machine Learning - Data Analytics Lab

**Lab 2: NumPy Practice**

1. **Create Arrays:**
   - Create an array of 10 zeros: `np.zeros(10)`.
   - Create an array of 10 ones: `np.ones(10)`.
   - Create an array of 10 fives: `np.full(10, 5)`.
   - Create an array of integers from 10 to 50: `np.arange(10, 51)`.
   - Create an array of even integers from 10 to 50: `np.arange(10, 51, 2)`.
   
2. **Create Matrices:**
   - Create a 3x3 matrix with values ranging from 0 to 8: `np.arange(9).reshape(3,3)`.
   - Create a 3x3 identity matrix: `np.eye(3)`.
   
3. **Generate Random Numbers:**
   - Generate a random number between 0 and 1: `np.random.rand(1)`.
   - Generate an array of 25 random numbers sampled from a standard normal distribution: `np.random.randn(25)`.
   
4. **Linearly Spaced Points:**
   - Create an array of 20 linearly spaced points between 0 and 1: `np.linspace(0, 1, 20)`.
   
5. **Numpy Indexing and Selection:**
   - Replicate specific matrix outputs using NumPy functions.
   
6. **Sum and Standard Deviation:**
   - Get the sum of all the values in a matrix: `np.sum(mat)`.
   - Get the standard deviation of the values in a matrix: `np.std(mat)`.
   - Get the sum of all the columns in a matrix: `np.sum(mat, axis=0)`.
