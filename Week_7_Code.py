# Game of Life
# Joshua Schoonmaker
# CIS_125

# Populate the world

def populate(petri_dish, h=80, w=22, R = True):
    import random
    for x in range(h):
            row = []
            for y in range(w):
                if R:
                    
                    row.append(random.randint(0, 1))
                else:
                    row.append(0)
            petri_dish.append(row)

# Display the world


def display(world, h = 22, w = 80):
    worldstring = ""
    for x in range(h):
        for y in range(w):
            if world[x][y] == 1:
                worldstring += "*"
            else:
                worldstring += " "
        worldstring += '\n'
    print(worldstring)


# Generate the world


def generation(petri_dish, h=22, w=80):
   
    new_world = []
    populate(new_world, h, w, False)
    
    n = 0    
    for x in range(1,h-1):
        for y in range(1,w-1):
            n = petri_dish[x-1][y-1] +  \
                petri_dish[x-1][y] +  \
                petri_dish[x-1][y+1] +  \
                petri_dish[x][y-1] +  \
                petri_dish[x][y+1] +  \
                petri_dish[x+1][y-1] +  \
                petri_dish[x+1][y] +  \
                petri_dish[x+1][y+1]

            
            if petri_dish[x][y] == 0:
                if n == 3:
                    new_world[x][y] = 1
                else:
                    new_world[x][y] = 0
            else: #(cell is alive)
                if n < 2 or n > 3:
                    new_world[x][y] = 0
                else:
                    new_world[x][y] = 1
    
    return new_world


def main():
    world = []
    height = 22
    width = 80
    populate(world, height, width)
    display(world, height, width)
    key = input("Press q to quit, any other key to continue: ")
    while key != 'q':
        world = generation(world, height, width)
        display(world, height, width)
        key = input("Press q to quit, any other key to continue: ")

    print("Goodbye")


if __name__ == '__main__':
    main()
