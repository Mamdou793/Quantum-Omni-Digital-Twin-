# We are importing the logic FROM your new extension structure
from ext.quantum_omni_tool.quantum.omni.tool.logic import QuantumTool

# 1. Initialize the tool
my_tool = QuantumTool(stage_path="extension_output.usda")

# 2. Use the "Engine" to generate the grid
print("Step 1: " + my_tool.generate_grid(count=10))

# 3. Use the "Engine" to run the quantum measurement
stats = my_tool.run_measurement()

print("\n--- EXTENSION TEST REPORT ---")
print(f"Alpha States: {stats['Alpha']}")
print(f"Beta States:  {stats['Beta']}")
print("Check extension_output.usda to see the result!")