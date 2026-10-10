# Machine setup (Windows + WSL2)

Machine: AbhiPC, Windows + WSL2 Ubuntu. Linux user: `abhin`. All code lives in `~/code` (inside Linux, never under `/mnt/c`).

## 1. WSL2 and Ubuntu

Commands (PowerShell as admin):

```powershell
wsl --install        # then restart the PC and create the Ubuntu user
wsl -l -v            # check: Ubuntu, VERSION 2
```

Then in Ubuntu:

```bash
sudo apt update && sudo apt upgrade -y
mkdir -p ~/code
```

Windows Terminal: Settings → Startup → Default profile → Ubuntu.

Gotchas I hit:
- `explorer.exe` with no dot opens the normal Windows home view. Use `explorer.exe .` to open the current Linux folder.
- The sudo password shows nothing while typing; that's normal.
- If `wsl -l -v` shows VERSION 1: `wsl --set-version Ubuntu 2`.

## 2. Git and SSH key

Commands:

```bash
sudo apt install -y git
git config --global user.name "YOUR_NAME"
git config --global user.email "YOUR_EMAIL"
git config --global init.defaultBranch main
ssh-keygen -t ed25519 -C "YOUR_EMAIL"    # Enter for every prompt
cat ~/.ssh/id_ed25519.pub                # copy into GitHub → Settings → SSH and GPG keys
ssh -T git@github.com                    # type yes; expect "Hi YOUR_GITHUB!"
cd ~/code && git clone git@github.com:YOUR_GITHUB/supportpilot.git
```

Gotchas I hit:
- Clone with the `git@github.com:` (SSH) URL, not `https://`, or every push asks for a password.
- Never share `~/.ssh/id_ed25519` (no `.pub`): that's the private key.

## 3. Cursor connected to WSL

Steps:
1. Install Cursor on Windows from cursor.com and sign in.
2. From Ubuntu: `cd ~/code/supportpilot && cursor .`
3. Check the bottom-left corner says `WSL: Ubuntu`. If `cursor` isn't found: `Ctrl+Shift+P` → "Connect to WSL" → open `/home/abhin/code/supportpilot`.
4. Use Cursor's built-in terminal (`` Ctrl+` ``); it runs in Ubuntu.
5. Project rule lives in `.cursor/rules/learning.mdc` (committed). Never commit `.cursor/mcp.json` (can hold API keys).

## 4. uv and Python

Commands:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh    # installed uv 0.13.0 to ~/.local/bin
source ~/.bashrc
uv --version
cd ~/code/supportpilot && mkdir -p tools && cd tools
uv init --package ticket-cli    # src layout: code in src/ticket_cli/
cd ticket-cli
uv add --dev pytest ruff
uv run ticket-cli               # prints: Hello from ticket-cli!
uv run pytest
uv run ruff check . --fix
```

Gotchas I hit:
- uv 0.13 created the src layout (`src/ticket_cli/__init__.py`), so `uv run main.py` fails: there is no `main.py`. Run `uv run ticket-cli` instead.
- uv used the system Python 3.14 (`/usr/bin/python3.14`) and created `.venv` automatically.
- Imports use the package name `ticket_cli` (no "s"); the module file is `tickets.py`.
- After installing uv, the shell can't find it until `source ~/.bashrc` or a new terminal.
- `grep -r` searches `.venv` too; add `--exclude-dir=.venv`.

## 5. Docker Desktop

Settings changed:
- During install: Use WSL 2 instead of Hyper-V
- Settings → General: Use the WSL 2 based engine; Start Docker Desktop when you sign in
- Settings → Resources → WSL integration: Ubuntu on

Test command:

```bash
docker run hello-world    # expect "Hello from Docker!"
```

Gotcha: "Cannot connect to the Docker daemon" means Docker Desktop isn't running, or WSL integration is off.