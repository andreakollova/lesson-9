nazov_suboru = input("Zadaj názov súboru, do ktorého chceš zapísať svoj text:")
tvoj_text = input("Zadaj svoj text:")

nazov_suboru = open(nazov_suboru, "w")
nazov_suboru.writelines(tvoj_text)

nazov_suboru.close()
