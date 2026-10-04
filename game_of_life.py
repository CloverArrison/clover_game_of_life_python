# Author: Clover Arrison
# Assignment / Part: HW2
# Date due: 10/4/2026
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

import sys
class World:
    def __init__(self, world_file_name="life.txt", world_size= (0,0)):
        self.world_file_name = str(world_file_name)
        self.world_size = tuple(world_size)
        self.generation = 0
        self.world = self.initialize_world()

    def initialize_world(self):
        try:
            # Uses this so that if an error happens while opening or reading, the file is still closed
            with open(self.world_file_name, 'r') as f:
                # Makes a list, each index has one line of the file (without ending characters)
                list_lines = f.read().split()
            if not list_lines:
                raise InitializationError()
        except UnicodeDecodeError:
            raise InitializationError("Couldn't read input file")
        except IsADirectoryError:
            raise InitializationError("Input file should be a file not a directory")
        except FileNotFoundError:
            raise InitializationError("Input file not found")
        except OSError:
            raise InitializationError("Couldn't read input file")

        # Check if the world size is given by main
        if self.world_size == (0,0):
            # Use the number of lines and the length of the first line to find world size
            self.world_size = (len(list_lines[0]), len(list_lines))

        # Check that all lines are the same length
        for line in list_lines:
            if len(line) != self.world_size[0]:
                raise InitializationError("Input File is the wrong size")
        # Check that there are the correct number of lines
        if len(list_lines) != self.world_size[1]:
            raise InitializationError("Input File is the wrong size")

        # Make empty all dead world
        world = [[0] * self.world_size[0] for _ in range(self.world_size[1])]

        # Assign 1s and 0s to the empty world based off of characters in the input file
        for row in range(self.world_size[1]):
            for col in range(self.world_size[0]):
                char = list_lines[row][col]
                if char in "-*":
                    world[row][col] = int(char == '*')
                else:
                    raise InitializationError("Input file contains invalid character(s)")
        return world

    # Use what cells are alive or dead, updates world state
    def compute_next_generation(self):
        # Make empty all dead world to update the world state
        new_world = [[0] * self.world_size[0] for _ in range(self.world_size[1])]
        # For each cell find the new state
        for row in range(self.world_size[1]):
            for col in range(self.world_size[0]):
                new_world[row][col] = self.compute_cell(row, col)

        # Update world state and generation
        self.world = new_world
        self.generation += 1

    # Returns dead or alive based on game of life rules
    def compute_cell(self, row, col):
        count = self.count_neighbors(row, col)
        # Rules if the cell is alive
        if self.world[row][col]:
            if 2 <= count <= 3:
                return 1
            return 0
        # Rule if the cell is dead
        elif count == 3:
            return 1
        return 0

    # Returns the number of neighbors a cell has, accounts for boundaries
    def count_neighbors(self, row, col):
        count = 0
        # Iterate through the 9 cells in a 3x3 around the center cell
        for d_row in (-1, 0, 1):
            for r_col in (-1, 0, 1):
                # Skip the center cell
                if d_row == 0 and r_col == 0:
                    continue
                new_row = row + d_row
                new_col = col + r_col

                # Only add to the alive cells if not on a boundary
                if 0 <= new_row < self.world_size[1] and 0 <= new_col < self.world_size[0]:
                    count += self.world[new_row][new_col]

        return count

    # Returns a string of the world state and generation number
    def display_world(self):
        output = ""
        # Convert from 2D List to string
        for row in self.world:
            for cell in row:
                output += '*' if cell else '-'
            output += '\n'

        return output + "Generation: " + str(self.generation)

class InitializationError(Exception) :
    pass

def main():
    try:
        # Command Line Options
        if len(sys.argv) > 1:
            file = sys.argv[1]
            run_time = int(sys.argv[2]) if len(sys.argv) > 2 else int(input("Enter run time (positive int): "))

        # User Input Options
        else:
            file = input("Enter file name (enter for default): ")
            run_time = int(input("Enter run time (positive int): "))

        # Check if valid runtime
        if run_time <= 0:
            raise ValueError("Run time should be a positive integer")

        # Check if file path specified
        if file == "":
            game_world = World()
        else:
            game_world = World(file)

        # Print the initial world state (generation 0)
        print(game_world.display_world())

        # Run the game for n step and print each step
        for _ in range(1, run_time+1):
            game_world.compute_next_generation()
            print(game_world.display_world())


    except ValueError as e:
        print(e)
        print("Value Error: Try a different run time")
    except InitializationError as e:
        print(e)
        print("Initial File Error: Try a different file")
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt: Stoping")

if __name__ == "__main__":
    main()
