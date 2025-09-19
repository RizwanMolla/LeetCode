class Spreadsheet:

    def __init__(self, rows: int):
        # dictionary to store explicitly set values
        self.cells = {}
        self.rows = rows
        self.cols = 26  # A-Z

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        # reset means set to 0 (but can also just delete from dict)
        if cell in self.cells:
            del self.cells[cell]

    def getValue(self, formula: str) -> int:
        # remove leading '='
        expr = formula[1:]
        x, y = expr.split('+')

        def get_val(token: str) -> int:
            if token.isdigit():
                return int(token)
            return self.cells.get(token, 0)

        return get_val(x) + get_val(y)
