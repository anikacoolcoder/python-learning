import tkinter as tk
from tkinter import ttk

root = tk.Tk()

tree = ttk.Treeview(root)
tree.pack()

def refresh_tree():
  tree.delete(*tree.get_children())
  # repopulate tree
  tree.insert("", "end", text="Item 1")

btn = tk.Button(root, text="Refresh Tree", command=refresh_tree)
btn.pack()

root.mainloop()