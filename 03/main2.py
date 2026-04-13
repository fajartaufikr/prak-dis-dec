import time
from raft_module import RaftNode

def simulate():
    node_ids = [1, 2, 3]
    nodes = [RaftNode(i, node_ids) for i in node_ids]

    for step in range(10):
        print(f"\n--- Step {step+1} ---")
        time.sleep(1)

        for node in nodes:
            node.tick()

        for node in nodes:
            print(f"Node {node.id}: {node.state.name} | Term {node.current_term}")

if __name__ == "__main__":
    print("Simulasi Raft Leader Election\n")
    simulate()