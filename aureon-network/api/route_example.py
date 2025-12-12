from aureon_core.routing_engine import RoutingEngine
from aureon_network.transfer_switch import TransferSwitch

engine = RoutingEngine()
switch = TransferSwitch()

route = engine.route(100, "USD")
transfer = switch.execute(100, "USD")

print("Routing:", route)
print("Transfer:", transfer)
