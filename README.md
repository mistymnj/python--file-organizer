
🗂️ Python File Organizer

Tired of a messy Downloads folder?

I built this Python script to clean my Downloads folder automatically. No more searching for files!

It sorts 400+ files in just 2 seconds.

---

✨ What It Does

| File Type | Goes To |
| :--- | :--- |
| 📸 .jpg, .png, .jpeg | Images Folder |
| 📄 .pdf, .docx, .txt | Documents Folder |
| 🎬 .mp4, .mkv | Videos Folder |
| 🎵 .mp3 | Music Folder |
| 📦 .zip, .rar | Zips Folder |

---

🚀 How To Run

**Step 1:** Download the code
```bash
git clone https://github.com/mistymnj/python--file-organizer.git
*Step 2:* Run it
python file.py
*Step 3:* That's it!
Your Downloads folder is now clean.

---

💻 Output Example
Cleaning: C:\Users\LENOVO\Downloads
Moved test.jpg -> Images
Moved notes.pdf -> Documents
Moved song.mp3 -> Music
Done! Folder Cleaned.
---

🛠️ Tech Used

- Python
- `os` - To work with folders
- `shutil` - To move files

No other libraries needed!

---

📚 What I Learned

1. How to use `os.listdir()` to read files
2. How to use `os.path` to find file types
3. How to use `shutil.move()` to move files
4. How to automate a boring daily task

---

⭐ Future Ideas

- [ ] Add GUI with Tkinter
- [ ] Add auto-run every day
- [ ] Add support for more file types

---

Made with ❤️ by mistymnj

If this helped you, please give it a ⭐ Star!

