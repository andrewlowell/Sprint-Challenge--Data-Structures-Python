class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.storage[-1] == None:
      for i in range(self.capacity):
        if self.storage[i] == None:
          self.storage[i] = item
          break
    else:
      self.storage[self.current] = item
      self.current +=1
      if self.current == self.capacity:
        self.current = 0

  def get(self):
    to_return = []
    for i in range(self.capacity):
      if self.storage[i]:
        to_return.append(self.storage[i])
      else:
        break
    return to_return