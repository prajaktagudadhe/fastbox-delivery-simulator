# FastBox Delivery Simulator
Python logistics delivery simulator.

## Features
- JSON parsing
- Handles multiple input formats
- Euclidean distance calculation
- Assign nearest available agent
- Delivery tracking
- Distance reporting
- Top performer detection

## Assumptions
1. Warehouses may be:
   - list
   - dictionary

2. Agents may be:
   - list
   - dictionary

3. Package warehouse field may be:
   - warehouse_id
   - warehouse

4. If two agents are same distance:
   - alphabetical ID wins

5. Agent position updates after delivery

6. All packages are deliverable

## Run
```bash
python main.py
