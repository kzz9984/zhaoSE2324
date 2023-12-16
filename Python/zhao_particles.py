"""
Name: Kevin Zhao
Date: 12/16/23

File: zhao_particles.py

Purpose: Use a dictionary to return the subatomic particles that are
         most likely and least likely to be observed
"""

def main():

    # Define dictionary
    particles = {'neutron':0.55, 'proton':0.21,
                 'meson':0.03, 'muon':0.07,
                 'neutrino':0.14}
    
    # Define lists to store target particles    
    likeliest = []
    unlikeliest = []

    # Determine target particles
    for (key, value) in particles.items():      # Loop over key-value pairs
        if (value == max(particles.values())):  # Check for greatest probability
            likeliest.append(key)
        if (value == min(particles.values())):  # Check for least probability
            unlikeliest.append(key)

    return (f"Most likely to be observed:  {', '.join(likeliest)}\n" +
            f"Least likely to be observed: {', '.join(unlikeliest)}")


print(main())