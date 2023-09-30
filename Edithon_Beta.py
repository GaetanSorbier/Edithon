import tkinter as tk
from tkinter import filedialog
from tkinter.font import Font

def enregistrer_texte():
    texte = texte_entry.get("1.0", "end-1c")  # Récupère le texte de la zone de texte

    emplacement = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Fichiers texte", "*.txt")])

    if emplacement:
        with open(emplacement, "w") as fichier:
            fichier.write(texte)

def mettre_en_gras():
    texte_entry.tag_add("gras", texte_entry.index(tk.SEL_FIRST), texte_entry.index(tk.SEL_LAST))
    texte_entry.tag_config("gras", font=("Helvetica", taille_police.get(), "bold"))

def souligner():
    texte_entry.tag_add("souligne", texte_entry.index(tk.SEL_FIRST), texte_entry.index(tk.SEL_LAST))
    texte_entry.tag_config("souligne", underline=True)

def mettre_en_italique():
    texte_entry.tag_add("italique", texte_entry.index(tk.SEL_FIRST), texte_entry.index(tk.SEL_LAST))
    texte_entry.tag_config("italique", font=("Helvetica", taille_police.get(), "italic"))

def changer_taille_police():
    nouvelle_taille = taille_police.get()
    texte_entry.configure(font=("Helvetica", nouvelle_taille))

app = tk.Tk()
app.title("Edithon")

texte_label = tk.Label(app, text="Saisissez du texte :")
texte_label.pack()

texte_entry = tk.Text(app, height=10, width=40)
texte_entry.pack()

boutons_frame = tk.Frame(app)
boutons_frame.pack()

enregistrer_bouton = tk.Button(boutons_frame, text="Enregistrer", command=enregistrer_texte)
enregistrer_bouton.pack(side=tk.LEFT)

quitter_bouton = tk.Button(boutons_frame, text="Quitter", command=app.quit)
quitter_bouton.pack(side=tk.LEFT)

bouton_gras = tk.Button(boutons_frame, text="Mettre en Gras", command=mettre_en_gras)
bouton_gras.pack(side=tk.LEFT)

bouton_souligne = tk.Button(boutons_frame, text="Souligner", command=souligner)
bouton_souligne.pack(side=tk.LEFT)

bouton_italique = tk.Button(boutons_frame, text="Italique", command=mettre_en_italique)
bouton_italique.pack(side=tk.LEFT)

taille_police_label = tk.Label(app, text="Taille de la police :")
taille_police_label.pack()

taille_police = tk.StringVar()
taille_police.set("12")
taille_police_entry = tk.Entry(app, textvariable=taille_police)
taille_police_entry.pack()

appliquer_taille_bouton = tk.Button(app, text="Appliquer", command=changer_taille_police)
appliquer_taille_bouton.pack()

app.mainloop()
