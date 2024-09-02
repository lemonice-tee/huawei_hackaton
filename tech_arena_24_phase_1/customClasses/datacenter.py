#!/usr/bin/env python3

class Datacenter:

    def __init__(self, name, costEnergy, latency, slots):
        self.name = name
        self.costEnergy = float(costEnergy)
        self.latency = latency
        self.slots = int(slots)

        ### Additional default variables

        self.servers = {}
        self.cost = 0
        self.spent = 0

    def __str__(self):

        output = []

        # Header
        output.append(f"{'Datacenter':<15} {'Cost Energy':>12} {'Latency':>10} {'Slots':>10} {'Cost':>10} {'Spent':>10}")

        # Data
        output.append(f"{self.name:<15} {self.costEnergy:>12.2f} {self.latency:>10} {self.slots:>10} {self.cost:>10} {self.spent:>10.2f}")
        return "\n".join(output)
