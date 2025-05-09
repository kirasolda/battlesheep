## MVP

### Architecture

2 players -> 2 devices
- 1 device is the host
- opposite player does not know where the sheep are
- host starts the game and waits for the other player to join
- host can see his IP address and port in the UI
- host shares the IP address and port with the other player
- opposite player connects to the host and sends hello
- host receives hello and sends the field size and number of sheep and wolves
- opposite player receives field size and number of sheep and wolves
- host setups his own sheep and wolves in the field in his side
- host or the opposite player send ready message to each other
- once both players are ready, the game can start


### Game Loop

- after sync both players have start button or something
- but until it's decided who starts first, the game is paused
- how to decide who starts first?
- host and opposite player roll a virtual dice
- the player with the highest number starts first
- now we ublock the game for the first player
- ???? Should we allow moving sheep and wolves instead of shooting???? # TODO: Think about it.
- the player turns (shoot or move) and sends the action to the other player and his controls are blocked
- other player receives the action and updates his own field and replies with the result of the action (if needed)
- now the other player can take his turn
- game continues...

#### How to win?
- all sheep are dead
- if the game was started by player (first turn), the losing player can shoot one more time and if he hits last sheep of the opposite player, it's a draw
- otherwise, the game is over

### Implementation

#### Libraries

Proof of concept (POC) will be without GUI, just a console app:
- [requests](https://docs.python-requests.org/en/latest/) - for the network communication
- [fastapi](https://fastapi.tiangolo.com/) - for the API

Next step will be with GUI:
- [pygame](https://www.pygame.org/) - for the GUI

Following improvements later:
- [pydantic](https://pydantic-docs.helpmanual.io/) - for the data validation

#### Possible classes

- GameSession
    - am_i_a_host
    - status 
    - game_parametres
    - IP + port

- GameParametres
    - field_size
    - number and size_of_sheep

- Status
    - initial
    - waiting for opening
    - waiting for connection
    - sync(exchanging game parametres)
    - preparing
    - ready->dice
    - "my turn"/"opposite turn"
    - game over

- Sheep
    - position
    - size
    - is_alive
    - is_shot

- Player
   - nickname
   - field

- Field
    - size
    - sheep
