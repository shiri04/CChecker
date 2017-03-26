
class function:

    properties = {}

    def __init__(self, index, text, start, end):
        self.index = index
        self.text = text
        self.start = start
        self.end = end

    def process(self, details={}):
        lines_list = self.text.split('\n')
        mid_pattern = r'(?P<ret>\w+\*{0,2})\s+(?P<name>\w+)\s*\((?P<args>.*?)\)'  # not handled case where pointer(*) is with function name
        first_line_pattern = before_pattern + mid_pattern + after_pattern
        match = re.search(first_line_pattern, lines_list[0].strip())
        self.name = match.group('name')
        self.rettype = match.group('ret')
        args = match.group('args')