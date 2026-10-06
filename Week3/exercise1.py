##---
### 🌟 Exercise 1: Currencies

#Implement dunder methods for a `Currency` class to handle string representation,
integer conversion, addition, and in-place addition.

#**Starter code:**

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}s"

    def __repr__(self):
        return f"{self.amount} {self.currency}s"

    def _int_(self):
        return self.amount
    
    def _add_self(other):
        
    

#**Implement these dunder methods:**

|  #`__str__` | `print(c1)` | Returns `"5 dollars"` (amount + currency + "s") |
#| `__repr__` | `repr(c1)` | Returns `"5 dollars"` |
##| `__int__` | `int(c1)` | Returns the amount as an integer |
#| `__add__` | `c1 + 5` or `c1 + c2` | Returns the **sum as an int** (not a Currency) |
#| `__iadd__` | `c1 += 5` or `c1 += c2` | Modifies amount **in place**, returns `self` |

**Rules:**
- When adding two Currencies, they must have the **same currency label**
- If currencies don't match → `raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")`
- `__add__` accepts `int` or `Currency` — anything else → `raise TypeError`

**Test with this code:**
```python
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))        # 5 dollars
print(int(c1))        # 5
print(repr(c1))       # 5 dollars
print(c1 + 5)         # 10
print(c1 + c2)        # 15
print(c1)             # 5 dollars

c1 += 5
print(c1)             # 10 dollars

c1 += c2
print(c1)             # 20 dollars

print(c1 + c3)        # TypeError: Cannot add between Currency type <dollar> and <shekel>

