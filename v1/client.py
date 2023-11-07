import pygame
import grpc
import game_pb2
import game_pb2_grpc
import threading
import sys

if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = input("Enter your name: ")

print(f"Welcome, {name}!")
# Initialize Pygame and create a window
pygame.init()
screen = pygame.display.set_mode((640, 480))

# gRPC channel and stub
channel = grpc.insecure_channel('localhost:50051')
stub = game_pb2_grpc.GameServiceStub(channel)

# Get unique player ID from the server
response = stub.JoinGame(game_pb2.JoinGameRequest(playerName=name))
player_id = response.playerId
other_players = {pos.id: pos for pos in response.otherPlayers}

# Initial position of the player's blob
x, y = 320, 240

def update_server_position(x, y):
    stub.UpdatePosition(game_pb2.Position(id=player_id, x=x, y=y))

def listen_for_updates():
    for update in stub.GetPositions(game_pb2.Position(id=player_id, x=x, y=y)):
        # Update the position of the other blobs
        other_players[update.id] = update

# Start a background thread to listen for updates from the server
threading.Thread(target=listen_for_updates, daemon=True).start()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the blob based on key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 1
    if keys[pygame.K_RIGHT]:
        x += 1
    if keys[pygame.K_UP]:
        y -= 1
    if keys[pygame.K_DOWN]:
        y += 1

    # Send the updated position to the server
    update_server_position(x, y)

    # Clear the screen
    screen.fill((0, 0, 0))
    
    # Draw the player's blob
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 10)

    # Draw other players' blobs
    for pos in other_players.values():
        pygame.draw.circle(screen, (0, 255, 0), (pos.x, pos.y), 10)

    pygame.display.flip()

pygame.quit()
