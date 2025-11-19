# ------------------- Player klasse (Deel 1) -------------------
class Player:
    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.name == other.name
        return False

    def __lt__(self, other):
        if isinstance(other, Player):
            return self.number < other.number
        return NotImplemented

    def __str__(self):
        return f"{self.name} ({self.number})"


# ------------------- Pass klasse (Deel 2) -------------------
class Pass:
    def __init__(self, sender: Player, receiver: Player, nr_of_times: int):
        self.sender = sender
        self.receiver = receiver
        self.nr_of_times = nr_of_times

    def get_weight(self):
        return self.nr_of_times

    def get_start(self):
        return self.sender

    def get_end(self):
        return self.receiver

    def __eq__(self, other):
        if isinstance(other, Pass):
            return self.sender == other.sender and self.receiver == other.receiver
        return False

    def __str__(self):
        return f"Pass from {self.sender.name} to {self.receiver.name}"


# ------------------- PassGraph klasse (Deel 3 + 4) -------------------
class PassGraph:
    def __init__(self, path_: str | None = None):
        self.players = []
        self.adj = {}
        if path_:
            self._load_from_txt(path_)

    # ------------------- Basisoperaties -------------------
    def add_player(self, player: Player):
        if not self.has_player(player):
            self.players.append(player)
            self.adj[player.name] = []

    def has_player(self, player_or_name):
        if isinstance(player_or_name, Player):
            return any(p.name == player_or_name.name for p in self.players)
        elif isinstance(player_or_name, str):
            return any(p.name == player_or_name for p in self.players)
        return False

    def get_player(self, name: str):
        for p in self.players:
            if p.name == name:
                return p
        return None

    def add_pass(self, sender: Player, receiver: Player, times: int = 1):
        if times <= 0:
            raise ValueError("Aantal passes moet positief zijn")
        if not self.has_player(sender) or not self.has_player(receiver):
            raise ValueError("Beide spelers moeten in de graaf aanwezig zijn")

        for p in self.adj[sender.name]:
            if p.receiver == receiver:
                p.nr_of_times += times
                return
        self.adj[sender.name].append(Pass(sender, receiver, times))

    def get_pass(self, sender_name: str, receiver_name: str):
        if sender_name in self.adj:
            for p in self.adj[sender_name]:
                if p.receiver.name == receiver_name:
                    return p
        return None

    def neighbors(self, sender_name: str):
        if sender_name in self.adj:
            return self.adj[sender_name]
        return []

    # ------------------- Analysefuncties -------------------
    def total_weight(self, subset: list[str] | None = None):
        if subset is None:
            subset = [p.name for p in self.players]
        total = 0
        for sender_name in subset:
            for p in self.neighbors(sender_name):
                if p.receiver.name in subset:
                    total += p.nr_of_times
        return total

    def pass_intensity(self, subset: list[str] | None = None) -> float:
        if subset is None:
            subset = [p.name for p in self.players]
        n = len(subset)
        if n < 2:
            return 0.0
        numerator = self.total_weight(subset)
        denominator = n * (n - 1)
        return numerator / denominator

    def top_pairs(self, k: int = 5):
        all_passes = []
        for sender_passes in self.adj.values():
            all_passes.extend(sender_passes)
        sorted_passes = sorted(all_passes, key=lambda p: p.nr_of_times, reverse=True)
        return sorted_passes[:k]

    def distribution_from(self, sender_name: str):
        if sender_name not in self.adj:
            return []
        dist = [(p.receiver.name, p.nr_of_times) for p in self.adj[sender_name]]
        dist.sort(key=lambda x: x[1], reverse=True)
        return dist

    # ------------------- Deel 4: Opslaan en inlezen -------------------
    def players_list(self):
        return self.players.copy()

    def passes_list(self):
        all_passes = []
        for sender_passes in self.adj.values():
            all_passes.extend(sender_passes)
        return all_passes

    def save_to_txt(self, path: str):
        with open(path, 'w', encoding='utf-8') as f:
            f.write("[PLAYERS]\n")
            for p in sorted(self.players, key=lambda x: x.name):
                f.write(f"{p.name};{p.number}\n")
            f.write("[PASSES]\n")
            for sender_name in sorted(self.adj.keys()):
                for p in self.adj[sender_name]:
                    f.write(f"{p.sender.name} -> {p.receiver.name} : {p.nr_of_times}\n")

    def _load_from_txt(self, path: str):
        if not os.path.exists(path):
            raise ValueError(f"Bestand {path} bestaat niet")
        current_section = None
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if line == "[PLAYERS]":
                    current_section = "players"
                    continue
                elif line == "[PASSES]":
                    current_section = "passes"
                    continue
                elif current_section is None:
                    raise ValueError(f"Ongeldige sectie in bestand: {line}")

                if current_section == "players":
                    if ";" not in line:
                        raise ValueError(f"Ongeldige spelerregel: {line}")
                    name, number = [x.strip() for x in line.split(";", 1)]
                    try:
                        number = int(number)
                    except:
                        raise ValueError(f"Rugnummer moet een int zijn: {line}")
                    self.add_player(Player(name, number))

                elif current_section == "passes":
                    if "->" not in line or ":" not in line:
                        raise ValueError(f"Ongeldige passregel: {line}")
                    sender_part, rest = line.split("->", 1)
                    receiver_part, nr_part = rest.split(":", 1)
                    sender_name = sender_part.strip()
                    receiver_name = receiver_part.strip()
                    try:
                        nr = int(nr_part.strip())
                        if nr <= 0:
                            raise ValueError
                    except:
                        raise ValueError(f"Pass aantal moet positief int zijn: {line}")
                    sender = self.get_player(sender_name)
                    receiver = self.get_player(receiver_name)
                    if sender is None or receiver is None:
                        raise ValueError(f"Pass verwijst naar onbekende speler: {line}")
                    self.add_pass(sender, receiver, nr)


# ------------------- Testscenario voor Deel 1 t/m 4 -------------------
if __name__ == "__main__":
    print("=== Test Deel 1: Player ===")
    player1 = Player("Eden Hazard", 10)
    player2 = Player("Moussa Dembele", 19)
    player3 = Player("Jan Vertonghen", 5)
    print(player1)
    print(player1 == Player("Eden Hazard", 7))  # True
    print(player1 < player2)  # True

    print("\n=== Test Deel 2: Pass ===")
    pass1 = Pass(player1, player2, 4)
    pass2 = Pass(player2, player3, 2)
    pass3 = Pass(player1, player2, 7)
    print(pass1)
    print(pass1 == pass2)  # False
    print(pass1 == pass3)  # True
    print(pass1.get_weight())  # 4

    print("\n=== Test Deel 3: PassGraph ===")
    g = PassGraph()
    for p in [player1, player2, player3, Player("Romelu Lukaku", 9)]:
        g.add_player(p)
    g.add_pass(player1, player2, 3)
    g.add_pass(player1, player3, 2)
    g.add_pass(player2, player1, 1)
    g.add_pass(player2, Player("Romelu Lukaku", 9), 4)
    g.add_pass(player3, Player("Romelu Lukaku", 9), 2)
    g.add_pass(Player("Romelu Lukaku", 9), player1, 1)

    print("Total weight:", g.total_weight())
    print("Pass intensity:", g.pass_intensity())
    print("Top pairs:")
    for p in g.top_pairs(3):
        print(p)
    print("Distribution from Eden Hazard:", g.distribution_from("Eden Hazard"))

    print("\n=== Test Deel 4: Save & Load ===")
    # Opslaan
    g.save_to_txt("team_test.txt")
    print("Graaf opgeslagen naar 'team_test.txt'")

    # Inlezen
    g2 = PassGraph("team_test.txt")
    print("Nieuwe graaf ingelezen:")
    for p in g2.passes_list():
        print(p, p.get_weight())
