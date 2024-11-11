from collections import deque

record = {}
tracker = deque()
manual = {1: "Rock", 2: "Paper", 3: "Scissors"}

def playerTurn():
    ans = 0
    while ans not in manual:
        try:
            print("Please enter 1, 2, or 3.")
            ans = int(input("| 1: Rock | 2: Paper | 3: Scissors |\n"))
        except ValueError:
            print("Invalid choice.")
    return ans

def recordUpdate(ans):
    tracker.append(ans)
    record[ans] = record.get(ans, 0) + 1
    if len(tracker) > 30:
        tracker.popleft()

def npcTurn():
    turn = max(record, key=record.get, default=0)
    return (turn % 3) + 1

def game(player, npc):
    print("\nYour Move:", manual[player])
    print("Computer Move:", manual[npc])
    if npc == player:
        return "It's a tie!"
    elif (player - npc) % 3 == 1:
        return "Player wins!"
    else:
        return "NPC wins!"

def main():
    rounds = int(input("Enter amount of rounds: "))

    for i in range(1, rounds+1):
        print("\nRound", i)
        pturn = playerTurn()
        recordUpdate(pturn)
        nturn = npcTurn()
        print(game(pturn, nturn))

if __name__ == '__main__':
    main()