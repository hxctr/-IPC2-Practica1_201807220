class Nodo:
    def __init__(self, follow, value):
        self.set_next(follow)
        self.set_value(value)

    def set_next(self, follow):
        self.follow = follow

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.follow

    def get_value(self):
        return self.value

class SimplyLinkedList():
    def __init__(self):
        self.start = None
        self.end = None
    
    def is_empty(self):
        return self.start == None
    
    def enqueue(self, value):
        if self.is_empty():
            self.start = self.end = Nodo(None, value)
        else:
            self.end = Nodo(self.end, value) 
    
    def dequeue(self):
        if self.is_empty():
            return "Cola vacía - Totalidad de órdenes entregadas"
        elif self.start == self.end:
            tmp = self.start
            self.start = self.end = None
            return "Entregando pizza de: " + str(tmp.get_value())
        else:
            tmp2 = self.start

            tmp = self.end 
            while tmp.get_next() != tmp2:
                tmp = tmp.get_next()
            self.start = tmp
            tmp.set_next(None)
            return "Entregando pizza de: " + str(tmp2.get_value())
    
    def print_queue(self):
        tmp = self.end
        while tmp is not None:
            print('Pizza de ', tmp.get_value())
            tmp = tmp.get_next()

