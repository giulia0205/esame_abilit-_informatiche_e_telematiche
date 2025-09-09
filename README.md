<<<<<<< HEAD
=======
esame_abilità_informatiche_e_telematiche
>>>>>>> 7707738 (esame)
Questo repository contiene le soluzioni agli esercizi dell’esame di scripting in Bash e in Python.

Esercizio 1

    Descrizione
        Lo script rename_files_with_date.sh svolge le seguenti operazioni:
            1. Crea 5 file dummy (dummy_file_1.txt, ..., dummy_file_5.txt) nella cartella corrente.
            2. Raccoglie in un array tutti i file (escludendo le directory e sé stesso).
            3. Mostra l’elenco dei file rilevati.
            4. Rinomina tutti i file aggiungendo la data corrente nel formato: YYYY-MM-DD-nomefile.ext.


    Come eseguire lo script
        Aprire il terminale ed entrare nella cartella Esercizio1:
            cd Esercizio1

        Rendere lo script eseguibile (solo la prima volta):
            chmod +x rename_files_with_date.sh

        Eseguire lo script:
            ./rename_files_with_date.sh


    Output previsto
        Esempio di output mostrato nel terminale:
            Creating dummy files...
            Files found in the current directory:
            dummy_file_1.txt
            dummy_file_2.txt
            dummy_file_3.txt
            dummy_file_4.txt
            dummy_file_5.txt
            Renaming files...
            Renamed 'dummy_file_1.txt' to '2025-09-07-dummy_file_1.txt'
            Renamed 'dummy_file_2.txt' to '2025-09-07-dummy_file_2.txt'
            ...
            Done!


    File inclusi
        rename_files_with_date.sh → script principale dello svolgimento dell’esercizio.




Esercizio 5

    Descrizione
        Questo script (sum_numbers.sh) esegue le seguenti operazioni:
            1. Crea un file vuoto chiamato numbers.txt.
            2. Scrive nel file una colonna contenente i numeri interi da 1 a 10.
            3. Calcola la somma dei numeri utilizzando il comando awk.
            4. Stampa il risultato della somma sul terminale.
        La somma può essere verificata tramite la formula di Gauss:
            n(n+1)/2 = 10×11/2 = 55


    Come eseguire lo script
        Aprire il terminale ed entrare nella cartella Esercizio5:
            cd Esercizio5
        
        Rendere lo script eseguibile (una sola volta):
            chmod +x sum_numbers.sh

        Eseguire lo script:
            ./sum_numbers.sh


    Output previsto
        La somma dei numeri da 1 a 10 è: 55


    File generati
        numbers.txt: file generato con i numeri da 1 a 10, uno per riga



Esercizio 6

    Descrizione
        Lo script update_memory.sh esegue le seguenti operazioni:
            1. Crea un file chiamato memory_config.txt con dei parametri di configurazione.
            2. Usa il comando awk per cercare la riga che inizia con MaxMem e modificare il suo valore da 512 a 1024.
            3. Sovrascrive il file con il contenuto aggiornato.
            4. Mostra un messaggio di conferma.
        Contenuto iniziale del file memory_config.txt
            c o n t r o l o f memory r e q u i r e m e n t s

            BoundaryLayerFactor 3 . 0
            MaxMem 512
            MaxMemPerParticle 240
            PredPeakFactor 0 . 8
        Dopo l'esecuzione dello script, il valore MaxMem sarà aggiornato a 1024.


    Come eseguire lo script
        Aprire il terminale e accedere alla cartella Esercizio6:
            cd Esercizio6

        Rendere lo script eseguibile (solo la prima volta):
            chmod +x update_memory.sh

        Eseguire lo script:
            ./update_memory.sh


    Output previsto
        Valore di MaxMem aggiornato a 1024 nel file 'memory_config.txt'


    Contenuto aggiornato del file:

        c o n t r o l o f memory r e q u i r e m e n t s

        BoundaryLayerFactor 3 . 0
        MaxMem 1024
        MaxMemPerParticle 240
        PredPeakFactor 0 . 8


    File inclusi
        memory_config.txt → file generato e modificato dallo script


Esercizio 8
<<<<<<< HEAD

=======
>>>>>>> 7707738 (esame)
    Descrizione
        Questo script (list_files.sh) esegue le seguenti operazioni:
            1. Accetta come argomento una directory.
            2. Verifica che la directory esista.
            3. Se la directory non esiste, mostra un messaggio di errore e termina con codice di errore.
            4. Entra nella directory specificata.
            5. Elenca:
                    a. Tutti i file regolari
                    b. Tutte le sottodirectory
                    c. Tutti i file vuoti


    Come eseguire lo script
        Aprire il terminale e accedere alla cartella Esercizio8:
            cd Esercizio8

        Rendere lo script eseguibile (una sola volta):
            chmod +x list_files.sh

        Eseguire lo script passando una directory come argomento:
            ./list_files.sh nome_della_directory


    Output previsto
        Se la directory esiste, il terminale mostrerà:
            a. I file regolari
            b. Le sottodirectory
            c. I file vuoti



Esercizio 9
<<<<<<< HEAD

=======
>>>>>>> 7707738 (esame)
    Descrizione
        Lo script Python haloss.py analizza i dati prodotti da una simulazione idrodinamica cosmologica a redshift z = 6.  
        Il file di input (`AGN.txt`) descrive le proprietà di aloni, contenenti materia oscura (DM), gas, stelle, e buchi neri (BH).
        L'analisi fornisce:
            1. Grafico della massa DM in funzione della massa barionica (gas + stelle) con fit lineare in scala log-log
            2. Massa totale vs distanza dalla struttura più massiva in scala log-log
            3. Istogramma della massa DM degli aloni con asse x in scala log
            4. Distribuzione spaziale proiettata degli aloni: 
                a. tre subplots corrispondenti alle proiezioni nei piani x-y, z-y e x-z
                b. il colore fa riferimento alla massa del gas
                c. la dimensione fa riferimento alla massa stellare   
            5. Relazione tra massa del buco nero e massa stellare in scala log-log con fit lineare (selezione per M_BH > 8 × 10⁵ M_sun/h)  
            6. Istogramma 2D cumulativo (massa vs distanza) per aloni massivi con calcolo della distanza rispetto ai 5 aloni con M > 3.07 × 10⁹ M_sun/h


    Come eseguire lo script
        Aprire il terminale e accedere alla cartella Esercizio9:
            cd Esercizio9

        Per eseguire l’analisi, lanciare lo script:
            python haloss.py AGN.txt


    File contenuti
        `AGN.txt`: File dati con le proprietà degli aloni
        `*.png`: Grafici generati dallo script 


    Note
        Le scale logaritmiche sono usate dove forniscono una rappresentazione più informativa dei dati.
        I valori nulli o negativi sono filtrati per evitare problemi in scala log.






