# Game of Thrones Network Demo

This is a demo of the Game of Thrones Network.
It is a good way to get started learning how to work with graph
databases and write GSQL.
The network comes from the first book of the Game of Thrones
books.  Each character in the book is represented by a vertex
in a graph.  Every time a person is mentioned in the book within
15 words of another person, a RELATED edge type is created.

The network contains 187 People vertices and 684 edges.
This is big enough to demonstrate the power of graph databases
but small enough to load quickly into a training database.
