class Sensor:

    old_state = False
    state = False
    has_changed = False

    def __init__(self):
        self.state = False

    def set_value(self, value):
        if value:
            self.set()
        else:
            self.reset()

    def get(self):
        return self.state
    
    def set(self):
        self.old_state = self.state
        self.state = True
        self.has_changed = self.old_state != self.state
    
    def reset(self):
        self.old_state = self.state
        self.state = False
        self.has_changed = self.old_state != self.state

    def toggle(self):
        self.state = not self.state
        self.has_changed = True
