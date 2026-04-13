import random
import time
from enum import Enum
from typing import List, Optional

class State(Enum):
    FOLLOWER = 1
    CANDIDATE = 2
    LEADER = 3

class RaftNode:
    def __init__(self, node_id: int, all_nodes: List[int]):
        self.id = node_id
        self.nodes = all_nodes
        self.state = State.FOLLOWER
        self.current_term = 0
        self.voted_for: Optional[int] = None
        self.last_heartbeat = time.time()
        self.election_timeout = self._random_timeout()

    def _random_timeout(self):
        return time.time() + random.uniform(1.0, 2.0)

    def on_heartbeat(self, term: int):
        if term >= self.current_term:
            self.current_term = term
            self.state = State.FOLLOWER
            self.voted_for = None
            self.last_heartbeat = time.time()
            self.election_timeout = self._random_timeout()

    def start_election(self):
        self.current_term += 1
        self.state = State.CANDIDATE
        self.voted_for = self.id
        votes = 1

        for node_id in self.nodes:
            if node_id != self.id:
                votes += 1  # simulasi semua vote setuju

        if votes > len(self.nodes) // 2:
            self.state = State.LEADER
            print(f"Node {self.id} menjadi LEADER pada term {self.current_term}")

    def tick(self):
        now = time.time()
        if self.state != State.LEADER and now > self.election_timeout:
            self.start_election()