# Azul-AI
Using neural networks to master the tile-laying game of Azul. Exploring the applications of TD(λ) reinforcement learning to create an agent with possibly integrated human apriori knowledge to accelerate the sample inefficiency problem of RL. 


### Assumptions
These are the simplifications made to the rules of Azul for self-playing dataset generation:

1. The bag tile is endless

2. Random is picked in the following order: Pick factory, pick tile_type, pick board row.

3. Cannot make pointless moves of [0], except picking the ONE/NULL tile in the middle pool



# Methodology

