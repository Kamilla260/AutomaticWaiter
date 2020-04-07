# Środowisko agenta i reprezentacja wiedzy – Raport


## Temat projektu i podprojekty
Jako temat projektu obrany został Automatyczny kelner, który jest agentem, zgodnie z opisem:  
„Zadaniem automatycznego kelnera jest przyjmowanie zamówień i dostarczanie posiłków gościom. Agent rozpoznaje przygotowany w kuchni posiłek, a następnie na postawie historii zamówień wybiera stolik, do którego należy go dostarczyć.”

W dalszym etapie tworzenia projektu zostaną przedstawione dwa podprojekty indywidualne dotyczące metod uczenia:  
  * algorytmy genetyczne,  
  * drzewa decyzyjne.

## Środowisko
Projekt tworzony jest w języku Python przy użyciu biblioteki tkinter. 

Do tej pory zostały rozbudowane pliki:  
  * aStar.py – zawierający deklarację algorytmu a*,  
  * agent.py – definiujący zachowanie naszego agenta,  
  * map.py – określający środowisko agenta oraz obiekty,  
  * state.py – definiujący kierunki, położenie,   
  * main.py – odpowiedzialny za uruchomienie oraz określenie wyświetlanej grafiki.  
  
W folderze assests znajdują się wykorzystywane grafiki.

## Etap projektu
Projekt znajduje się w początkowej fazie tworzenia. Zaimplementowane zostało środowisko agenta oraz podstawowe założenia. Na tym etapie nie zostały jeszcze rozwinięte aspekty sztucznej inteligencji, które docelowo stanowią główne założenia projektu.  

Podczas tworzenia projektu został przeprowadzony test animacji: https://drive.google.com/open?id=1hjZTBw5KG8DYEDR41-XWf_Frn5yYsx3O. Po uruchomieniu projektu pojawia się środowisko z agentem, który przebywa z góry ustaloną trasę ruchu.  

Aktualnie środowisko agenta utworzone jest z siatki o wymiarach 19x10 oraz grafiki. Będzie ono z góry narzucone również w dalszych etapach rozwoju projektu. Nie jest dostępna konfiguracja wymiarów środowiska przy uruchamianiu. Na obecnym etapie wizerunek ślimaka traktowany jest jak ściana.


