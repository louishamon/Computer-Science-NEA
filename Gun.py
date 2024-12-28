class Gun():
    def __init__(self, new_damage, new_fire_rate):
        self.damage = new_damage
        self.fire_rate = new_fire_rate

    def get_damage(self): # getter method to return damage
        return self.damage
    
    def get_fire_rate(self): # getter method to return fire rate
        return self.fire_rate