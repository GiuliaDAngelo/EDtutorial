# Import the Brian2 library, which is designed for simulating spiking neural networks
from brian2 import *

# Set the backend for Matplotlib to 'TkAgg' to allow plotting with interactive windows
matplotlib.use('TkAgg')

# Start a new Brian2 simulation scope
start_scope()

# Set the number of neurons in the simulation to 100
N = 100

# Set the time constant (tau) of the neuron dynamics to 10 milliseconds (ms)
tau = 10*ms

# Define the maximum initial membrane potential (v0) for the neurons
v0_max = 3.

# Set the total simulation duration to 1000 milliseconds (1 second)
duration = 1000*ms

# Define the differential equation for neuron membrane potential (v) dynamics:
# dv/dt = (v0 - v) / tau : describes how the membrane potential (v) changes over time
# "v0" is a constant membrane potential parameter that varies for each neuron
# "v" has a refractory period during which the neuron does not respond to new inputs
eqs = '''
dv/dt = (v0-v)/tau : 1 (unless refractory)  # Membrane potential dynamics
v0 : 1  # Parameter representing the neuron's baseline membrane potential
'''

# Create a group of neurons (NeuronGroup) with 'N' neurons using the specified equation 'eqs'
# Neurons fire (generate a spike) when v > 1, and reset their membrane potential (v = 0) afterward
# Neurons are in a refractory period for 5 milliseconds after spiking
# The method='exact' solves the equations accurately at each time step
G = NeuronGroup(N, eqs, threshold='v>1', reset='v=0', refractory=5*ms, method='exact')

# Create a SpikeMonitor to record the spiking activity of the neurons in the group 'G'
M = SpikeMonitor(G)

# Set the baseline membrane potential (v0) for each neuron based on its index (i)
# The initial potential 'v0' is distributed between 0 and v0_max across all neurons
G.v0 = 'i*v0_max/(N-1)'

# Run the simulation for the specified duration (1000 ms)
run(duration)

# Plotting the results:
figure(figsize=(12,4))  # Create a figure with dimensions 12x4 inches

# First subplot: Plot the spiking activity of neurons
subplot(121)  # Create the first subplot (1 row, 2 columns, 1st plot)
plot(M.t/ms, M.i, '.k')  # Plot spike times (M.t) against neuron indices (M.i) as black dots
xlabel('Time (ms)')  # Label the x-axis as "Time (ms)"
ylabel('Neuron index')  # Label the y-axis as "Neuron index"

# Second subplot: Plot the firing rate of neurons as a function of their baseline potential v0
subplot(122)  # Create the second subplot (1 row, 2 columns, 2nd plot)
plot(G.v0, M.count/duration)  # Plot the baseline potential (G.v0) vs the firing rate (M.count/duration)
xlabel('v0')  # Label the x-axis as "v0"
ylabel('Firing rate (sp/s)')  # Label the y-axis as "Firing rate (spikes per second)"

# Print 'end' to indicate that the simulation and plotting are complete
print('end')
