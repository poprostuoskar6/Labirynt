import os
import base64
import sys
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def generuj_klucz(haslo: str, sol: bytes) -> bytes:
    """Generuje klucz szyfrujący na podstawie hasła i soli."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=sol,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(haslo.encode()))

def szyfruj_plik(plik_wejsciowy: str, plik_wyjsciowy: str, haslo: str) -> None:
    """Szyfruje plik za pomocą podanego hasła."""
    sol = os.urandom(16)  # Generuj losową sól
    klucz = generuj_klucz(haslo, sol)
    f = Fernet(klucz)
    with open(plik_wejsciowy, 'rb') as plik:
        dane = plik.read()
    zaszyfrowane_dane = f.encrypt(dane)
    with open(plik_wyjsciowy, 'wb') as plik:
        plik.write(sol + zaszyfrowane_dane)  # Zapisz sól i zaszyfrowane dane

def odszyfruj_plik(plik_wejsciowy: str, plik_wyjsciowy: str, haslo: str) -> None:
    """Odszyfrowuje plik za pomocą podanego hasła."""
    with open(plik_wejsciowy, 'rb') as plik:
        sol = plik.read(16)  # Odczytaj sól (pierwsze 16 bajtów)
        zaszyfrowane_dane = plik.read()
    klucz = generuj_klucz(haslo, sol)
    f = Fernet(klucz)
    odszyfrowane_dane = f.decrypt(zaszyfrowane_dane)
    with open(plik_wyjsciowy, 'wb') as plik:
        plik.write(odszyfrowane_dane)

def odszyfruj_plik_slownik(plik_wejsciowy: str, plik_wyjsciowy: str, slownik: str) -> bool:
    """Próbuje odszyfrować plik za pomocą słownika haseł."""
    with open(plik_wejsciowy, 'rb') as plik:
        sol = plik.read(16)
        zaszyfrowane_dane = plik.read()

    with open(slownik, 'r', encoding='latin-1') as plik_slownik:
        for haslo in plik_slownik:
            haslo = haslo.strip()
            try:
                klucz = generuj_klucz(haslo, sol)
                f = Fernet(klucz)
                odszyfrowane_dane = f.decrypt(zaszyfrowane_dane)
                with open(plik_wyjsciowy, 'wb') as plik:
                    plik.write(odszyfrowane_dane)
                print(f"Hasło znalezione: {haslo}")
                return True
            except:
                pass
    return False

def wyswietl_pomoc():
    """Wyświetla instrukcje użytkowania skryptu."""
    print("Użycie:")
    print("  python3 skrypt.py --help")
    print("  python3 skrypt.py -s <plik_wejściowy> <plik_wyjściowy> <hasło>")
    print("  python3 skrypt.py -o <plik_wejściowy> <plik_wyjściowy> <słownik>")
    print("\nOpcje:")
    print("  --help, -h: Wyświetla tę pomoc.")
    print("  -s: Szyfruje plik.")
    print("  -o: Odszyfrowuje plik za pomocą słownika.")
    print("\nPrzykłady:")
    print("  1. Szyfrowanie pliku:")
    print("     python3 skrypt.py -s plik.txt zaszyfrowany.txt mojehaslo")
    print("     * `plik.txt`: Plik do zaszyfrowania.")
    print("     * `zaszyfrowany.txt`: Nazwa pliku wynikowego.")
    print("     * `mojehaslo`: Hasło do szyfrowania.")
    print("  2. Odszyfrowywanie pliku za pomocą słownika:")
    print("     python3 skrypt.py -o zaszyfrowany.txt odszyfrowany.txt slownik.txt")
    print("     * `zaszyfrowany.txt`: Plik do odszyfrowania.")
    print("     * `odszyfrowany.txt`: Nazwa pliku wynikowego.")
    print("     * `slownik.txt`: Ścieżka do słownika haseł.")

if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        wyswietl_pomoc()
    elif "-s" in sys.argv:
        try:
            plik_wejsciowy = sys.argv[2]
            plik_wyjsciowy = sys.argv[3]
            haslo = sys.argv[4]
            szyfruj_plik(plik_wejsciowy, plik_wyjsciowy, haslo)
            print(f"Plik '{plik_wejsciowy}' został zaszyfrowany do '{plik_wyjsciowy}'.")
        except IndexError:
            print("Nieprawidłowe argumenty. Użyj --help, aby uzyskać pomoc.")
    elif "-o" in sys.argv:
        try:
            plik_wejsciowy = sys.argv[2]
            plik_wyjsciowy = sys.argv[3]
            slownik = sys.argv[4]
            if not odszyfruj_plik_slownik(plik_wejsciowy, plik_wyjsciowy, slownik):
                print("Nie znaleziono hasła w słowniku.")
        except IndexError:
            print("Nieprawidłowe argumenty. Użyj --help, aby uzyskać pomoc.")
    else:
        print("Użyj --help, aby uzyskać pomoc.")
