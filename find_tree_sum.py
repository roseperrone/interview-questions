
class Node(object):
  def __init__(self, data, left, right):
    self.data = data
    self.left = left
    self.right = right


def all_paths_that_sum_to(target, head, path):
  '''
  Returns all paths thaht sum up to the target, either
  continuing the path, or beginning at a new node at head or below.
  '''
  if target < 0 or head is None:
    return []
  result = []

  path_sum = 0
  for node in path:
    path_sum += node.data


  intermediate_target = target - head.data
  if intermediate_target == 0:

  # paths not starting from the current node
  result.extend(all_paths_that_sum_to(target, head.right, [])
  result.extend(all_paths_that_sum_to(target, head.left, [])

  # paths continuing the current path
  path.append(head)

  if path_sum + head.data == target:
    result.append(head)
  else:
    result.extend(all_paths_that_sum_to(target, head.left, path)
    result.extend(all_paths_that_sum_to(target, head.right, path)
  return result


tree = something
paths = all_paths_that_sum_to(21, tree, [])
