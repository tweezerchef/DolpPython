### Introduction

I am a warehouse manager, and I want to optimize the placement of goods to minimize retrieval time. I have a list of goods with their sizes and retrieval frequencies. The issue is that I'm not knowledgeable in either math or technology. I asked a friend where to start, and they said to ask an 'AI' to create something using Python, so here I am. I need a placement plan that tells me where to put each good in the warehouse.

The warehouse is divided into a grid with 2 "aisles", A and B. Each aisle is divided into 10 sections. There is a space between each and on all sides of the grid that allows a worker to retrieve items, but there is only one entrance to the warehouse that is on the center bottom edge of the grid.  Each good has a size; they are all the same width, but their height varies from 1-3 height units, and each section can hold a maximum of 4 height units.

Each good has a retrieval frequency, a positive integer indicating the number of times it is retrieved from the warehouse in a given time period. It also has a name, which is a string, an id, which is a positive integer, and a size, which is a positive integer between 1 and 3.

Right now, I have a list of goods with their sizes and retrieval frequencies. I need a placement plan that tells me where to put each good in the warehouse. I want to minimize the retrieval time, so I want to place the most frequently retrieved goods closest to the entrance.

### Summary of Code to Generate

1. Code must be in Python
2. Code must take a list of goods with their name, ID, size, and retrieval frequencies as input. Here is a snipped of the input:

```python
goods = [("HairDryer", 1, 3, 1), ("ToothBrush", 2, 1, 2), ("HeadSet", 3, 1, 3), ("Ipad", 4, 1, 4)]
```

3. Code must output a placement plan that tells me where to put each good in the warehouse. The output should be a dictionary with the good's name as the key and the location as the value. Here is a snippet of the output:

```python
placement_plan = {"HairDryer": "A1", "ToothBrush": "A1", "HeadSet": "B1", "Ipad": "B2"}
```

4. Use any common libraries, but explain why you chose them in the code.
5. The code should be well-documented and easy to understand, as I am not knowledgeable in either math or technology.
6. Once you have created the commented code, please return it as your response.
