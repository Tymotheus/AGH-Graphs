from src.objects.FlowNetwork import FlowNetwork
from src.objects.FlowNetworkManager import FlowNetworkManager


print("\n\n---------------------------------------- AD. 5.1 ----------------------------------------")

# BASIC FLOW NETWORK
fn = FlowNetwork()
print(fn)
fn.draw()

# FLOW NETWORK FROM FILE
fn2 = FlowNetwork('example_data/proj5_flow_network_yes.txt')
# fn2 = FlowNetwork('example_data/proj5_flow_network_no.txt')
# fn2 = FlowNetwork('example_data/proj5_flow_network_yes_not_equal_layers.txt')
print(fn2)
fn2.draw()

# RANDOM FLOW NETWORK


print("\n\n---------------------------------------- AD. 5.2 ----------------------------------------")
