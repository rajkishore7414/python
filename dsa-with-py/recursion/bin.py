# Source - https://stackoverflow.com/a/9264811
# Posted by Andrew Clark, modified by community. See post 'Timeline' for change history
# Retrieved 2026-07-16, License - CC BY-SA 3.0

counter = 0

def increment():
  global counter
#   counter += 1
  counter = counter + 1
  print(counter)

increment()
