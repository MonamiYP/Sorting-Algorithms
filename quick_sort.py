import numpy as np
import pygame

# Setting some parameters for the screen
WIDTH = 600
HEIGHT = 400
width = 4  # Width of the individual bars, minimum value 2
heightSize = int(WIDTH / width)  # Total number of bars
run = True

# Draw a screen using pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quick Sort Visualization")

# Create an array of random numbers representing the height of the bars
heights = np.random.randint(10, HEIGHT, heightSize)
# Colours
GREEN = (50, 255, 200)
BLUE = (0, 100, 255)
ORANGE = (255, 150, 40)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
# Create an array to assign colours to each bar (initial colour is ORANGE)
color_array = [ORANGE] * heightSize
# Change this to set the speed at which the bars are sorted
delay = 100


# Function to update the screen when it's called
def redraw():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((255, 255, 255))
    draw()
    pygame.display.update()


# Function that does that partition work:
# Given the array, start position and end position,
# Set the pivot to be the end number, index is set to be at the start in the beginning
# If start number is smaller than pivot value, swap number with the number in the index where pivot will end up in
# Therefore this means small number is sent to the left of the pivot
# Increase index where pivot is gonna end up in, in the end all the numbers smaller than the pivot will be on the left
def partition(arr, start, end):
    pygame.event.pump()
    index = start
    color_array[end] = BLUE # This one is the pivot
    pivotValue = arr[end]

    for i in range(start, end):
        color_array[i] = RED # Highlight the bar that is currently being evaluated in RED
        redraw()
        pygame.time.delay(delay)
        color_array[i] = ORANGE
        redraw()
        
        if arr[i] < pivotValue:
            color_array[i] = YELLOW # Highlight the bars that are going to be swapped in YELLOW
            color_array[index] = YELLOW
            redraw()
            pygame.time.delay(delay)
            arr[i], arr[index] = arr[index], arr[i] # Swap bars
            index += 1
            color_array[i] = ORANGE # Turn the bar colours back to ORANGE
            color_array[index-1] = ORANGE
            redraw()
            pygame.time.delay(delay)
            
    

    arr[end], arr[index] = arr[index], arr[end] # Swap the pivot and index so that pivot ends up in its final position
    color_array[index] = GREEN # Pivot is now sorted so it can be GREEN
    redraw()
    pygame.time.delay(delay)

    return index


# Function that sorts the array, does partition and sorts the left of the pivot and right of the pivot
# Does this recursively.
def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        
        quick_sort(arr, start, pivot - 1) # Recursive
        for i in range(pivot + 1):
            color_array[i] = GREEN
        quick_sort(arr, pivot + 1, end)
    color_array[end] = GREEN # Completed the sorting, everything is green


# Function that draws the bars
def draw():
    for i in range(heightSize):
        pygame.draw.rect(screen, color_array[i], (i * width, HEIGHT - heights[i], width, heights[i]))

# Code starts running here
while run:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n: # Press n key to request new sort
                heights = np.random.randint(1, HEIGHT, heightSize)
                color_array = [ORANGE] * heightSize
            if event.key == pygame.K_s: # Press s key to start sorting
                color_array = [ORANGE] * heightSize
                quick_sort(heights, 0, heightSize - 1)
    draw()
    pygame.display.update()

pygame.quit()
