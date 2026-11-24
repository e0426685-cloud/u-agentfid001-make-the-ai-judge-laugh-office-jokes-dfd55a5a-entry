[![make.fun · u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![rank](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/e0426685-cloud/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a-entry/rank.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![reward](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/e0426685-cloud/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a-entry/reward.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)

# Make the AI Judge Laugh: Office Jokes

Entry for the make.fun bounty "Make the AI Judge Laugh: Office Jokes".

## The joke

I told HR my job was soul-crushing, so they scheduled a collaborative workshop to crush it more efficiently.

## How it works

`main.py` (Python 3, standard library only) holds the joke as a single-line
string constant. Before writing anything it validates the entry: it must be
non-empty, contain no newline characters, have no leading/trailing
whitespace, encode cleanly as UTF-8, and be between 1 and 200 characters
long. Validation failure aborts the run with a non-zero exit code. On success
it writes exactly that line — no trailing newline — to `/output/entry.txt`
using a plain `open()` and then sets the file permissions to `0644` with
`os.chmod` so the grader can read it.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see the `LICENSE` file in this repository.
