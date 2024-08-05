# Sample Queries

## Count the number of Person Verticies

We will use the size() function:

```gsql
CREATE DISTRIBUTED QUERY countPeople() FOR GRAPH got Syntax V2{ 
  P = {Person.*};
  R = SELECT p FROM P:p;
  PRINT R.size();
}
```

## Results