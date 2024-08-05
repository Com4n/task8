import os
import random

def generate_matrix_string(rows, columns):
    return ''.join(random.choice('01') for _ in range(rows * columns))

def generate_test_file(file_path, num_lines, min_size=5):
    with open(file_path, 'w') as f:
        for _ in range(num_lines):
            rows = random.randint(min_size, min_size + 5)
            columns = random.randint(min_size, min_size + 5)
            matrix_string = generate_matrix_string(rows, columns)
            f.write(f'{rows}x{columns}:{matrix_string}\n')

if __name__ == '__main__':
    generate_test_file('mat.in', 100000)
