# bhav 🌳

> A lightweight, Git-inspired version control system — built from scratch to understand how Git really works under the hood.

`bhav` lets you initialize repositories, stage files, commit changes, and view history — just like Git, but minimal and built for learning.

---

## ✨ Features

- 📦 Initialize a repository (`bhav init`)
- ➕ Stage files individually or all at once (`bhav add`)
- ✅ Commit staged changes with a message (`bhav commit`)
- 📜 View commit history (`bhav log`)

---

## 🚀 Installation

Clone the repository and install it in editable mode:

```bash
git clone https://github.com/<your-username>/bhav.git
cd bhav
pip install -e .
```

> The `-e` flag installs the package in "editable" mode, so any changes you make to the source code take effect immediately without reinstalling.

---

## 📖 Usage

### 1. Initialize a repository

Creates a new `bhav` repository in the current directory.

```bash
bhav init
```

### 2. Add files to the staging area

Stage a specific file:

```bash
bhav add FILENAME
```

Stage all files in the current directory:

```bash
bhav add .
```

### 3. Commit staged changes

Commit everything currently in the staging area with a message:

```bash
bhav commit -b "Your commit message"
```

### 4. View commit history

```bash
bhav log
```

---

## 🗂️ Example Workflow

```bash
mkdir my-project && cd my-project
bhav init
echo "Hello, bhav!" > hello.txt
bhav add hello.txt
bhav commit -b "Initial commit"
bhav log
```

---

## 🧩 Project Structure

```
bhav/
├── bhav/              # Core source code
│   ├── __init__.py
│   ├── cli.py         # Command-line interface
│   ├── init.py        # `bhav init` logic
│   ├── add.py         # `bhav add` logic
│   ├── commit.py      # `bhav commit` logic
│   └── log.py         # `bhav log` logic
├── setup.py           # Package configuration
├── README.md
└── tests/             # (planned)
```

> Update this section to match your actual folder layout.

---

## 🛣️ Roadmap

- [ ] `bhav status` — show staged vs. unstaged changes
- [ ] `bhav diff` — show changes between commits
- [ ] `bhav branch` — create and switch branches
- [ ] `bhav checkout` — restore files or switch commits
- [ ] `bhav merge` — merge branches
- [ ] `.bhavignore` support (like `.gitignore`)
- [ ] Remote support (push/pull to a server)
- [ ] Unit tests + CI pipeline

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes
4. Push to the branch and open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Your Name** — [@BhavneeshBanga](https://github.com/BhavneeshBanga)

Built as a learning project to understand the internals of Git.