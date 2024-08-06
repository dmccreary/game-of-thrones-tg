# Customer 360 Data Model

Our data model is just a single vertex type called ```Person``` with a ```RELATED``` edge to itself (reflexive).
The Person has a single STRING attribute called ```name``` and the edge has an unsigned integer called ```weight```
that represents the number of times the two characters were mentioned within 15 words of each other.

![](./img/data-model.png)

![](./img/related-edge.png)
