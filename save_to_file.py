from generate_land import ask_for_number, generate_land
# importing os functionality
import os

# using makedirs to mkdir and naming it output. exist_ok=true so the progame can run even with the output folder already existing.
os.makedirs("outputs", exist_ok=True)

noise_levels = [1, 5, 10, 20, 50, 100, 250, 500]

for nl in noise_levels:
  output = generate_land(200,200, nl)
  filename = os.path.join("outputs", f"noise-levels-{nl}.txt")

  with open(filename, "w") as f:
    f.write(output)