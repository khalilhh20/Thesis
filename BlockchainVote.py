import hashlib
import json
from time import time


class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_votes = []

        # Create the genesis block
        self.new_block(previous_hash='1')

    def new_block(self, previous_hash):
        """
        Create a new Block in the Blockchain
        :param previous_hash: Hash of previous Block
        :return: New Block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'votes': self.current_votes,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of votes
        self.current_votes = []

        self.chain.append(block)
        return block

    def new_vote(self, candidate):
        """
        Create a new vote in the Blockchain
        :param candidate: Candidate name
        :return: Index of the Block that will hold this vote
        """

        self.current_votes.append({
            'candidate': candidate,
            'voter': 'anonymous'  # In real-world, this should be replaced with voter ID
        })

        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        Create a SHA-256 hash of a Block
        :param block: Block
        :return: String containing the hash
        """

        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


# Example usage:
if __name__ == "__main__":
    # Create a new Blockchain
    blockchain = Blockchain()

    # Vote for candidates
    blockchain.new_vote("Candidate A")
    blockchain.new_vote("Candidate B")
    blockchain.new_vote("Candidate A")

    # Mine the blocks
    last_block_hash = blockchain.hash(blockchain.last_block)
    blockchain.new_block(previous_hash=last_block_hash)

    # Output the blockchain
    for block in blockchain.chain:
        print(block)