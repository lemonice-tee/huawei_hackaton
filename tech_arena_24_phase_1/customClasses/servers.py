#!/usr/bin/env python3

class Server:

    def __init__(self, servGen, servType, releaseTime, purchasePrice, slotSize, energyCon, capacity, lifeExp, costMove, maintenance):
        self.servGen = servGen
        self.servType = servType
        self.releaseTime = releaseTime
        self.purchasePrice = float(purchasePrice)
        self.slotSize = int(slotSize)
        self.energyCon = int(energyCon)
        self.capacity = int(capacity)
        self.lifeExp = float(lifeExp)
        self.costMove = float(costMove)
        self.maintenance = float(maintenance)
    
    def __str__(self):
        output = []
        output.append(f"{'Server Generation':<20} {'Type':6} {'Purchase Price':>15} {'Slot Size':>10} {'EnergyCon':>10} {'Capacity':>10} {'Life Exp.':>10}  {'Cost to Move.':>15}  {'Maintenance.':>15}")

        output.append(f"{self.servGen:<20} {self.servType:<6} {self.purchasePrice:>15.2f} {self.slotSize:>10} {self.energyCon:>10} {self.capacity:>10} {self.lifeExp:>10.2f} {self.costMove:>15.2f} {self.maintenance:>16.2f}")

        return "\n".join(output)
