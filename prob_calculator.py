import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for k,v in kwargs.items():
      for i in range(v):
        self.contents.append(k)

  def draw(self, amount):
    drawn = []
    if amount >= len(self.contents):
      return self.contents
    else:
      for i in range(amount):
        ball = self.contents.pop(random.randrange(len(self.contents)))
        drawn.append(ball)
      return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for exp in range(num_experiments):
    hat_cpy = copy.deepcopy(hat)
    drawn_balls = hat_cpy.draw(num_balls_drawn)
    passed = True
    for k,v in expected_balls.items():
      if drawn_balls.count(k) < v:
        passed = False
        break
    if passed:
      count += 1
  return count / num_experiments
