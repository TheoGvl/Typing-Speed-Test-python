import flet as ft
import time
import random

def main(page: ft.Page):
    # Βασικές ρυθμίσεις
    page.title = "Τεστ Ταχύτητας Πληκτρολόγησης"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 600
    page.window.height = 650
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 30

    # Λίστα με τυχαίες προτάσεις χρησιμοποίησα Ai για να φτιάξω τις προτάσεις
    keimena = [
        "Ο προγραμματισμός είναι η τέχνη του να λύνεις προβλήματα.",
        "Η εξάσκηση κάνει τον δάσκαλο, ειδικά στην πληκτρολόγηση.",
        "Κάθε μεγάλο ταξίδι ξεκινάει με ένα μικρό βήμα προς τα εμπρός.",
        "Οι υπολογιστές είναι απίστευτα γρήγοροι αλλά εντελώς τυφλοί.",
        "Η ταχύτητα είναι σημαντική, αλλά η ακρίβεια είναι αυτή που ξεχωρίζει τον επαγγελματία.",
        "Μην φοβάσαι τα λάθη στον κώδικα, είναι απλά ευκαιρίες για να μάθεις κάτι νέο.",
        "Η τεχνητή νοημοσύνη αλλάζει τον τρόπο που ζούμε και εργαζόμαστε καθημερινά.",
        "Αν η αποσφαλμάτωση είναι η αφαίρεση λαθών, τότε ο προγραμματισμός είναι η προσθήκη τους.",
        "Ποτέ μην αφήνεις για αύριο ένα πρόβλημα που μπορείς να λύσεις σήμερα.",
        "Η γλώσσα προγραμματισμού Python πήρε το όνομά της από τους Monty Python και όχι από το φίδι.",
        "Η επιτυχία δεν είναι το κλειδί της ευτυχίας. Η ευτυχία είναι το κλειδί της επιτυχίας.",
        "Για να καταλάβεις την αναδρομή, πρέπει πρώτα να καταλάβεις την αναδρομή.",
        "Ο καλύτερος τρόπος για να προβλέψεις το μέλλον είναι να το δημιουργήσεις.",
        "Ένας αλγόριθμος είναι σαν μια συνταγή μαγειρικής, αλλά με αυστηρούς μαθηματικούς κανόνες.",
        "Τα δεδομένα είναι το νέο πετρέλαιο, αλλά η ανάλυσή τους είναι η μηχανή.",
        "Το διαδίκτυο είναι ο μεγαλύτερος κατάλογος πληροφοριών στην ιστορία της ανθρωπότητας.",
        "Κάθε πρόγραμμα έχει τουλάχιστον ένα bug και μπορεί να μειωθεί κατά μία γραμμή κώδικα.",
        "Η φαντασία είναι πιο σημαντική από τη γνώση, γιατί η γνώση είναι περιορισμένη.",
        "Δεν υπάρχει 'σύννεφο', είναι απλά ο υπολογιστής κάποιου άλλου.",
        "Ο χρόνος που αφιερώνεις στην οργάνωση του κώδικα θα σε γλιτώσει από ώρες πονοκεφάλου στο μέλλον.",
        "Η μάθηση είναι ένας θησαυρός που θα ακολουθεί τον ιδιοκτήτη του παντού.",
        "Η μεγαλύτερη απειλή για την ασφάλεια ενός συστήματος βρίσκεται ανάμεσα στην καρέκλα και το πληκτρολόγιο.",
        "Ένα καλό πρόγραμμα πρέπει να είναι σαν ένα καλό βιβλίο: ευανάγνωστο και με καθαρό νόημα.",
        "Το μόνο μέρος όπου η επιτυχία έρχεται πριν από την εργασία είναι στο λεξικό.",
    ]

    # Μεταβλητές που θα θυμάται το πρόγραμμα
    start_time = 0
    stoxos = ""

    # --- Όταν πατάμε 'Ξεκίνημα' ---
    def ksekinima(e):
        nonlocal start_time, stoxos
        
        # Διαλέγουμε τυχαίο κείμενο και το δείχνουμε
        stoxos = random.choice(keimena)
        keimeno_stoxos.value = stoxos
        
        # Ετοιμάζουμε το κουτί για να γράψει ο χρήστης
        input_text.value = ""
        input_text.disabled = False # Ξεκλειδώνει το κουτί
        
        apotelesma.value = "Γράψε το κείμενο και πάτα 'Ολοκλήρωση'!"
        apotelesma.color = ft.Colors.WHITE
        
        # Κρατάμε την ακριβή χρονική στιγμή που ξεκίνησε!
        start_time = time.time() 
        page.update()
        
        # Βάζει τον κέρσορα αυτόματα μέσα στο κουτί για να αρχίσεις να γράφεις κατευθείαν!
        input_text.focus() 

    # --- Όταν πατάμε 'Ολοκλήρωση' ---
    def oloklirosi(e):
        nonlocal start_time, stoxos
        
        # Αν κάποιος πατήσει ολοκλήρωση χωρίς να έχει ξεκινήσει
        if start_time == 0:
            return

        # Υπολογίζουμε πόσος χρόνος πέρασε
        end_time = time.time()
        time_taken = end_time - start_time
        
        # Διαβάζουμε τι έγραψε ο χρήστης
        user_text = input_text.value
        
        # Υπολογισμός WPM Μετράμε τα κενά για να βρούμε τις λέξεις
        words_typed = len(user_text.split()) 
        minutes = time_taken / 60
        # Αν τα λεπτά είναι πάνω από 0, κάνουμε τη διαίρεση
        wpm = round(words_typed / minutes) if minutes > 0 else 0
        
        # Υπολογισμός Ακρίβειας (%)
        correct_chars = 0
        # Το zip() ενώνει τα δύο κείμενα γράμμα-γράμμα για να τα συγκρίνουμε!
        for a, b in zip(user_text, stoxos):
            if a == b:
                correct_chars += 1
                
        max_len = max(len(user_text), len(stoxos))
        accuracy = round((correct_chars / max_len) * 100) if max_len > 0 else 0

        # --- Εμφάνιση Αποτελεσμάτων ---
        apotelesma.value = f"Χρόνος: {round(time_taken, 1)} δευτ. | Ταχύτητα: {wpm} WPM | Ακρίβεια: {accuracy}%"
        
        # Χρωματίζουμε ανάλογα με το πόσο καλά τα πήγε
        if accuracy == 100:
            apotelesma.color = ft.Colors.GREEN_400
        elif accuracy >= 80:
            apotelesma.color = ft.Colors.YELLOW_400
        else:
            apotelesma.color = ft.Colors.RED_400
            
        input_text.disabled = True # Ξανακλειδώνουμε το κουτί
        start_time = 0 # Μηδενίζουμε τον χρόνο
        page.update()

    # --- Στήσιμο Οθόνης ---
    titlos = ft.Text("Τεστ Ταχύτητας ", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_400)
    
    # Εδώ θα εμφανίζεται το κείμενο που πρέπει να γράψεις
    keimeno_stoxos = ft.Text(
        "Πάτα 'Ξεκίνημα' για να εμφανιστεί το κείμενο.", 
        size=22, 
        italic=True, 
        text_align=ft.TextAlign.CENTER,
        color=ft.Colors.YELLOW_200
    )
    
    # Το πεδίο που γράφεις
    input_text = ft.TextField(label="Πληκτρολόγησε εδώ...", multiline=True, min_lines=3, disabled=True)
    
    # Τα Κουμπιά
    btn_start = ft.Button("Ξεκίνημα ", on_click=ksekinima, icon=ft.Icons.PLAY_ARROW)
    btn_stop = ft.Button("Ολοκλήρωση ", on_click=oloklirosi, icon=ft.Icons.CHECK)
    koumpia_row = ft.Row([btn_start, btn_stop], alignment=ft.MainAxisAlignment.CENTER)
    
    # Το κείμενο του αποτελέσματος
    apotelesma = ft.Text("Περιμένω...", size=20, weight=ft.FontWeight.BOLD)

    # Προσθήκη όλων στη σελίδα
    page.add(
        titlos,
        ft.Divider(height=20, color="transparent"),
        keimeno_stoxos,
        ft.Divider(height=20, color="transparent"),
        input_text,
        ft.Divider(height=20, color="transparent"),
        koumpia_row,
        ft.Divider(height=20, color="transparent"),
        apotelesma
    )

ft.run(main)