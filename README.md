# 🏀 NCAA March Madness Tournament Picker

A simple Python-based March Madness bracket generator that weights picks by team seed. This tool provides a randomized, but seed-aware, tournament bracket — making your selections a little smarter than pure chance.

## 📖 Features

- Generates a complete NCAA March Madness bracket.
- Picks weighted by team seed (lower seeds have higher chances to advance).
- Runs quickly from the command line.
- No external dependencies — uses Python's built-in libraries only.

## 🛠️ Technologies

- **Python 3.12**
- No additional libraries or dependencies required.

## 📦 Installation & Usage

### Prerequisites:
- Python 3.12 installed on your machine.

### Clone the repository:
```bash
git clone https://github.com/statman9/ncaa_touranment_picker.git
cd ncaa_touranment_picker
```

### Run the picker
```bash
python main.py
```

### How It Works
The generator assigns a probability of advancing to each team based on their seed. Lower seeds (like #1 or #2) have a higher chance of winning a matchup, while underdogs still retain a chance for an upset. This adds a strategic element to your randomized bracket picks.

### Example Output
```yaml
Round of 64:
(1) South vs (16) South -> Winner: (1) South
(8) South vs (9) South -> Winner: (9) South
...
Champion: (1) South
```
