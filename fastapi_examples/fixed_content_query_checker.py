class FixedContentQueryChecker:
  def __init__(self, fixed_content: str):
    self.fixed_content = fixed_content

  def __call__(self, q: str = ''):
    if q:
      return self.fixed_content in q
    return False


checker = FixedContentQueryChecker('bar')
