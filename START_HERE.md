# START HERE

Everything you need for the Stock Insight Analyzer project is in this folder.

## What's inside

```
stock-insight-analyzer-project/
├── START_HERE.md              <-- you are here
├── Presentation.pptx          <-- your 14-slide class presentation
├── Demo_Script.docx           <-- what to say, slide by slide
└── stock-insight-analyzer/    <-- the Python project itself
    ├── main.py                <-- run this to start the program
    ├── README.md              <-- full project documentation
    ├── requirements.txt       <-- Python libraries to install
    ├── .gitignore
    ├── src/
    │   ├── __init__.py
    │   ├── fetch_data.py
    │   ├── indicators.py
    │   ├── analyzer.py
    │   ├── visualizer.py
    │   └── utils.py
    ├── reports/
    │   └── charts/            <-- sample charts (backup for the demo)
    └── data/
        └── sample_outputs/    <-- sample text reports (backup for the demo)
```

## Your checklist for tonight

1. **Open the `stock-insight-analyzer` folder in VS Code.**
2. **In the VS Code terminal, run:**
   ```
   pip install -r requirements.txt
   python main.py
   ```
   When prompted, type `AAPL` and press Enter. Confirm you see a summary,
   a recommendation, and that a chart gets saved.
3. **Open `Demo_Script.docx`** and read through it once aloud.
4. **Open `Presentation.pptx`** and skim the slides.

## Your checklist for the presentation

- Keep `Demo_Script.docx` open on your phone or printed next to your laptop.
- Start the slideshow, work through each slide using the script.
- On slide 13 (Live Demo), switch to the VS Code terminal, run `python main.py`,
  enter a ticker, and show the output + chart.
- If the wifi dies mid-demo, use the sample files in `reports/charts/` and
  `data/sample_outputs/` — the demo script explains exactly what to say.

Good luck.
