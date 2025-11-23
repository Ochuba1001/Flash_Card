# Flash Card: French Language Study App

A simple, interactive Python application to help you study and memorize French vocabulary using digital flash cards.

## Features

- Practice your French with randomly generated flashcards.
- See the French word first, then flip to reveal the English translation.
- Track your progress: words you know are removed from the list.
- Data persists between sessions; continue where you left off.
- User-friendly graphical interface built with Tkinter.

## Screenshots

*Example imagery is included in the repo (`card_front.png`, `card_back.png`, `right.png`, `wrong.png`).*

## Requirements

- Python 3.x
- pandas
- tkinter (often included with standard Python installations)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Ochuba1001/Flash_Card.git
    cd Flash_Card
    ```

2. Install dependencies:
    ```bash
    pip install pandas
    ```

## Usage

Run the main Python script:

```bash
python main.py
```

- The app window will open showing a French word.
- Try to recall the English meaning.
- Wait 3 seconds (or click the ❌ if you don't know), and the card will flip to reveal the answer.
- Click the ✅ if you knew the word—this removes it from your queue.
- New progress is saved automatically in `new_word.csv`.

## File Descriptions

- `main.py` — The main program.
- `french_word.csv` — Contains the list of French-English word pairs.
- `new_word.csv` — (Auto-generated) Your personalized learning progress.
- `card_front.png`, `card_back.png`, `right.png`, `wrong.png` — GUI image assets.

## Target Audience

This project is designed for anyone looking to strengthen their French vocabulary, especially students or self-learners.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

## License

[MIT](LICENSE) (If you have a license file. Otherwise, add your chosen license.)

---

Happy learning!
