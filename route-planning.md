# Planowanie ruchu - Raport  

Drugi etap projektu opierał się na rozwinięciu sposobu poruszania się agenta, przyjętej heurystyki oraz udoskonaleniu algorytmu a*.  

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

## Powyższe akcje w kodzie:  

### Pętla głównej strategii przeszukiwania:  

    def tic(self):
        if not self.actions:
            self._decideWhereMove()
        self._act()

    def _decideWhereMove(self):
        if not self.actions:
            self.actions.extend(self._pathFromTo(self.st, map.kitchenInteractionState()))
            self.actions.extend([0])

    def _pathFromTo(self, s, e):
        return aStar.find(s, e)

    def _act(self):
        a = self.actions.pop(0)
        if isinstance(a, state.State):
            self.st = a
        elif 0 == a:
            self.orders.append(map.k.orders.pop(0))
            print("Biore zamówienia: " + str(self.orders))
            numberWhat = self.orders.pop(0)
            print(str(numberWhat))
            print(str(map.tableInteractionState(numberWhat)))
            e = map.tableInteractionState(numberWhat)

            if isinstance(e, bool):
                print("Whoa mama!")
                return

            self.actions.extend(self._pathFromTo(self.st, e))
        elif 1 == a:
            print("Odkładam zamówienie")
