# pyindependentreserve
Python client for Interacting with Independent Reserve API - The Bitcoin and Digital Currency Market

# Install 
pip install pyindependentreserve

# Usage
```python
$ python
>>> import independentreserve as ir
>>> connection = ir.PublicMethods()
>>> connection.get_valid_limit_order_types()
[u'LimitBid', u'LimitOffer'] 
```
