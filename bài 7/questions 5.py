class AnimalShelter:
    def __init__(self):
        self.dog_queue = []
        self.cat_queue = []
        self.timestamp = 0

    def enqueue(self, animal_type):
        self.timestamp += 1
        animal = (animal_type, self.timestamp)
        if animal_type == "dog":
            self.dog_queue.append(animal)
        elif animal_type == "cat":
            self.cat_queue.append(animal)
        else:
            print("Invalid animal type")

    def dequeueAny(self):
        if not self.dog_queue and not self.cat_queue:
            print("Shelter is empty")
            return None
        elif not self.dog_queue:
            return self.cat_queue.pop(0)[0]
        elif not self.cat_queue:
            return self.dog_queue.pop(0)[0]
        else:
            return (self.dog_queue if self.dog_queue[0][1] < self.cat_queue[0][1] else self.cat_queue).pop(0)[0]

    def dequeueDog(self):
        if not self.dog_queue:
            print("No dogs available")
            return None
        return self.dog_queue.pop(0)[0]

    def dequeueCat(self):
        if not self.cat_queue:
            print("No cats available")
            return None
        return self.cat_queue.pop(0)[0]

shelter = AnimalShelter()
shelter.enqueue("dog")
shelter.enqueue("dog")
shelter.enqueue("cat")
shelter.enqueue("cat")
print("Dequeue any:", shelter.dequeueAny())
print("Dequeue dog:", shelter.dequeueDog())
print("Dequeue cat:", shelter.dequeueCat())
print("Dequeue any:", shelter.dequeueAny())
