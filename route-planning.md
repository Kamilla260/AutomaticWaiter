# Planowanie ruchu - Raport  

Drugi etap projektu opierał się na rozwinięciu sposobu poruszania się agenta, przyjętej heurystyki oraz udoskonaleniu algorytmu a*.  

## Etap projektu  

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

Algorytm a* zakłada, że każdy z dwóch stanów jest drogą.  

Uwzględnienie kosztu przejścia powoduje, że wejście na ślimaka obecnego na grafice ma inny koszt niż poruszanie się po podłodze.
Możemy to dostrzec, ponieważ agent wchodzi na ślimaka położonego na prawym skraju, a resztę omija.  

Na obecnym etapie nie zostało jeszcze uwzględnione wyświetlanie zajętego stolika.

## Powyższe akcje w kodzie:  

### Główna strategia przeszukiwania:  

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

### Funkcja następnika  

    def _expandSmalest(nds, vst, goal):
        nd = nds.pop(_smalestIndex(nds))
        vst.append(nd.st)

    nxt = map.turnLeft(nd.st)
    if nxt not in vst:
        nds.append(Node(nxt, nd.distance + 1, nd.distance + 1 + _h(nxt, goal), nd))

    nxtR = map.turnRight(nd.st)
    if nxtR not in vst:
        nds.append(Node(nxtR, nd.distance + 1, nd.distance + 1 + _h(nxtR, goal), nd))

    nxtF = map.moveForward(nd.st)
    if nxtF:
        if nxtF[0] not in vst:
            nds.append(Node(nxtF[0], nd.distance + nxtF[1], nd.distance + nxtF[1] + _h(nxtF[0], goal), nd))
            
      
    def _smalestIndex(l):
        s = l[0]
        for i in l:
            if i.combined_heuristic < s.combined_heuristic:
                s = i
        return l.index(s)
            
            
        

### Przyjęta heurystyka  

    def _h(s, e):
         return math.sqrt((s.height-s.height)**2 + (e.width-e.width)**2)
