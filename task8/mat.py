import os
import re

def read_matrix(line):
    # Extract dimensions and matrix data
    dimensions, data = line.split(':')
    rows, columns = map(int, dimensions.split('x'))
    
    # Convert data to a 2D matrix
    matrix = []
    for r in range(rows):
        matrix.append(list(map(int, data[r*columns:(r+1)*columns])))
    
    return matrix, rows, columns

def count_isolated_ones(matrix, rows, columns):
    isolated_ones = 0
    for r in range(rows):
        for c in range(columns):
            if matrix[r][c] == 1:
                if ((r == 0 or matrix[r-1][c] == 0) and
                    (r == rows-1 or matrix[r+1][c] == 0) and
                    (c == 0 or matrix[r][c-1] == 0) and
                    (c == columns-1 or matrix[r][c+1] == 0)):
                    isolated_ones += 1
    return isolated_ones

def count_clusters(matrix, rows, columns, cluster_size):
    visited = [[False] * columns for _ in range(rows)]
    clusters = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= columns or matrix[r][c] == 0 or visited[r][c]:
            return 0
        visited[r][c] = True
        size = 1
        size += dfs(r-1, c)
        size += dfs(r+1, c)
        size += dfs(r, c-1)
        size += dfs(r, c+1)
        return size

    for r in range(rows):
        for c in range(columns):
            if matrix[r][c] == 1 and not visited[r][c]:
                if dfs(r, c) == cluster_size:
                    clusters += 1
    return clusters

def process_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            line = line.strip()
            if not line:
                continue
            matrix, rows, columns = read_matrix(line)
            isolated_ones = count_isolated_ones(matrix, rows, columns)
            clusters_of_two = count_clusters(matrix, rows, columns, 2)
            clusters_of_three = count_clusters(matrix, rows, columns, 3)
            outfile.write(f'{isolated_ones} {clusters_of_two} {clusters_of_three}\n')

if __name__ == '__main__':
    process_file('mat.in', 'mat.out')
