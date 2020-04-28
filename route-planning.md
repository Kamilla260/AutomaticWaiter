# Planowanie ruchu - Raport  

Drugi etap projektu opierał się na rozwinięciu sposobu poruszania się agenta, przyjętej heurystyki oraz udoskonaleniu algorytmu a*.  

## Pętla główna strategii przeszukiwania oraz funkcja następnika

Aktualnie: 
  * agent roznosi po jedym zamówieniu do stolika i wraca do kuchni,
  * algorytm a* zwraca listę stanów gdzie odległość pomiędzy nimi, to jedna akcja.  

Pominięte zostało zwracanie akcji, ze względu na fakt, że po zwróceniu akcji przez algorytm a*, następuje jedynie jego sczytanie i wraz z aktualnym stanem następuje pobór następnego stanu i nadpisanego tego aktualnego.  

Agent sczytuje akcje, które mogą być stanami odpowiadającymi:
  * lewo,
  * prawo,
  * do przodu 
  
lub akcjami:
  * weź zamówienie,
  * dostarcz zamówienie.
