# Today I Learned

## Sat Oct 10

### Linux on Windows (Part 1)
- WSL2 runs real Ubuntu inside Windows; servers and Docker images run Linux, so I work the same way.
- `pwd` = where am I; `cd ~` = home (/home/abhin); `mkdir -p` = make a folder, no error if it exists.
- `ls -la` lists everything incl. hidden files; `.` = this folder, `..` = parent.
- `sudo` runs one command as admin; `apt` installs Ubuntu software.
- `explorer.exe .` opens the current Linux folder in Windows (without the dot it opens the normal Windows view).
- nano: Ctrl+O then Enter saves, Ctrl+X exits.

### Git and GitHub (Part 2)
- A change goes: working folder → staged (`add`) → committed (`commit`) → on GitHub (`push`).
- `status` shows what changed, `diff` shows exactly how, `log --oneline` shows history.
- `origin` is the name for my GitHub copy of the repo (the remote).
- SSH key: `.pub` is public and goes to GitHub; the private key never leaves my machine.

### Cursor, uv and tests (Part 3)
- Cursor must be connected to WSL (bottom-left says WSL: Ubuntu).
- uv manages Python, packages and projects; `pyproject.toml` = settings, `uv.lock` = exact versions (commit it).
- uv 0.13 made the src layout: code in `src/ticket_cli/`, imported as `ticket_cli`. No `main.py`, so run `uv run ticket-cli`.
- `ticket-cli = "ticket_cli:main"` means the command `ticket-cli` runs `main()`.
- `.gitignore` keeps `.venv/`, caches, data and secrets (`.env`, `.cursor/mcp.json`) out of Git. `.cursor/rules/` is fine to commit.
- A test calls my code and `assert`s the result.
- My bug: `tickets_cli` vs `ticket_cli`. For ModuleNotFoundError, compare the name letter by letter.
- ruff I001 = needs two blank lines after imports; `uv run ruff check . --fix` fixes it.

### Docker and the shell (Part 4)
- Image = blueprint, container = a running copy; `-it` = interactive, `--rm` = delete when it stops.
- A pipe `|` feeds one command's output into the next.
- `grep -r` also searches `.venv`; use `--exclude-dir=.venv`.
- setup.md = onboarding docs: anyone can rebuild the machine from it.

### Issues, PRs and branch protection (Part 5)
- Issue = what and why; branch = where work happens; PR = how it lands; `Closes #1` closes the issue on merge.
- Squash merge makes one commit on main, so delete the branch with `git branch -D`.
- "Review required, merging is blocked" = Require approvals was on. Solo, it must be off: you can't approve your own PR.
- Adding a PR to the project board creates a second card; the board is for issues only.
- TDD: write the test, watch it fail, write the code, watch it pass.

### Python and fake data (Part 6, in progress)
- Practised loops, dicts, `max(d, key=d.get)`, list comprehensions, `datetime.fromisoformat`, a small class.
- Faker generated 10,000 tickets; `wc -l` shows 10001 lines (header + rows).
- Generated data stays out of Git; the script that makes it goes in.

Open questions:
- (add anything you're unsure about)