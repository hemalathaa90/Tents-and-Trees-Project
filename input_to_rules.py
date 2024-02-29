
def parse_input(input_str):
    lines = input_str.strip().split('\n')
    rows, cols = map(int, lines[0].split())
    puzzle = [line.split() for line in lines[1:-1]]
    row_counts = list(map(int, lines[-1].split()))
    return rows, cols, puzzle, row_counts

def generate_asp(rows, cols, puzzle, row_counts):
    asp_code = f"rows({rows}).\ncolumns({cols}).\n"

    # Generate tree and tent predicates
    for i, row in enumerate(puzzle, start=1):
        for j, cell in enumerate(row[0], start=1):
            if cell == 'T':
                asp_code += f"tree({i}, {j}).\n"
            elif cell.isdigit():
                count = int(cell)
                for k in range(count):
                    asp_code += f"tent({i}, {j+k}).\n"

    # Generate rowsum predicates
    for i, count in enumerate(row_counts, start=1):
        asp_code += f"rowsum({i}, {count}).\n"

    # Generate colsum predicates
    for j in range(1, cols + 1):
        col_counts = sum(1 for row in puzzle if row[0][j-1] == 'T')
        asp_code += f"colsum({j}, {col_counts}).\n"

    # Generate free predicates
    for i, row in enumerate(puzzle, start=1):
        for j, cell in enumerate(row[0], start=1):
            if cell == '.':
                asp_code += f"free({i}, {j}).\n"

    return asp_code

def parse_input_file(input_file):
    with open(input_file, 'r') as f:
        input_str = f.read()
    return parse_input(input_str)

def generate_asp_file(rows, cols, puzzle, row_counts, output_file):
    asp_code = generate_asp(rows, cols, puzzle, row_counts)
    with open(output_file, 'a') as f:
        f.write(asp_code)

# Usage example
input_file = 'input.txt'
output_file = 'constraints.lp'

rows, cols, puzzle, row_counts = parse_input_file(input_file)
generate_asp_file(rows, cols, puzzle, row_counts, output_file)
