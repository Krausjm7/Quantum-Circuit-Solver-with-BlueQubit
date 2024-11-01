########## Quantum Circuit Solver - Circuit_1_30q_fixed.qasm - by Jamie Kraus 10/25/2024 ##########

# Importing necessary libraries
import bluequbit
from qiskit import QuantumCircuit
import pandas as pd
import matplotlib.pyplot as plt

# Initialize BlueQubit with API key
bq = bluequbit.init("YOUR_BLUEQUBIT_API_KEY")

# Loading the circuit from the .qasm file
qasm_file_path = "C:/Users/Jamie/BlueQubit Hackathon/circuit_1_30q_fixed.qasm"
with open(qasm_file_path, 'r') as f:
    qasm_content = f.read()

# Create a QuantumCircuit object from the .qasm file content
circuit = QuantumCircuit.from_qasm_str(qasm_content)

# Run the circuit on BlueQubit
result = bq.run(circuit)
counts = result.get_counts()

# Convert the results to a DataFrame for easy manipulation and visualization
df = pd.DataFrame(list(counts.items()), columns=['Bitstring', 'Probability'])

# Sort the DataFrame by probability in descending order
df = df.sort_values(by='Probability', ascending=False)

# Find the hidden bitstring with the highest probability
hidden_bitstring = max(counts, key=counts.get)

# Select the top N bitstrings for plotting
N = 20  # top probability bitstrings to visualize
top_df = df.head(N)

# Create the plot to visualize the bitstring probabilities
plt.figure(figsize=(10, 6))
bars = plt.bar(top_df['Bitstring'], top_df['Probability'], color='skyblue')
plt.xticks(rotation=90)  # Rotating the bitstring labels on the x-axis for readability
plt.xlabel('Bitstring')
plt.ylabel('Probability')
plt.title('Top Bitstring Probabilities')

# Highlight the hidden bitstring in red
for bar, bitstring in zip(bars, top_df['Bitstring']):
    if bitstring == hidden_bitstring:
        bar.set_color('red')

# Adjust layout for better fit and display the plot
plt.tight_layout()
plt.show()

# Print the hidden bitstring for reference
print(f"\nThe hidden bitstring is: {hidden_bitstring}")
