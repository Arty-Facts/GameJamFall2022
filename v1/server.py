from concurrent import futures
import grpc
import game_pb2
import game_pb2_grpc
from collections import defaultdict
import threading
import uuid

def generate_unique_id():
    return str(uuid.uuid4())

class GameService(game_pb2_grpc.GameServiceServicer):
    def __init__(self):
        self.positions = defaultdict(lambda: (0, 0))  # Default position for each blob
        self.clients = {}  # Map client ids to their gRPC connection
        self.lock = threading.Lock()

    def JoinGame(self, request, context):
        with self.lock:
            # Assign a new unique ID to the client
            client_id = generate_unique_id()
            self.clients[client_id] = context
            # Return the new ID and the positions of other blobs
            return game_pb2.JoinGameResponse(
                playerId=client_id,
                otherPlayers=[game_pb2.Position(id=pid, x=pos[0], y=pos[1]) for pid, pos in self.positions.items()]
            )

    def UpdatePosition(self, request, context):
        with self.lock:
            self.positions[request.id] = (request.x, request.y)
            # Broadcast the new position to all clients
            self.broadcast_position(request.id, request.x, request.y)
            return game_pb2.Position(id=request.id, x=request.x, y=request.y)
    
    def GetPositions(self, request_iterator, context):
        with self.lock:
            # Send the positions of all blobs to the client
            for cid, pos in self.positions.items():
                yield game_pb2.Position(id=cid, x=pos[0], y=pos[1])

    def broadcast_position(self, client_id, x, y):
        for cid, conn in self.clients.items():
            if cid != client_id:  # Don't send the update back to the client who moved
                try:
                    conn.send(game_pb2.Position(id=client_id, x=x, y=y))
                except:  # Handle disconnects
                    # Remove the client from the clients list
                    # del self.clients[cid]
                    print(f"Client {cid} disconnected")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    game_pb2_grpc.add_GameServiceServicer_to_server(GameService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()