# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
  cooked_amount = time * temperature * pressure * COOKED_CONSTANT

  if desired_state == 'well-done' and cooked_amount >= WELL_DONE:
    return True
  elif desired_state == 'medium' and cooked_amount >= MEDIUM:
    return True
  else:
    return False