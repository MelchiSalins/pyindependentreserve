"""
Independent Reserve features a JSON based API, that is comprised of Public and Private methods.

All API calls must be made over SSL to https://api.independentreserve.com .
Public methods do not require an authentication token and should be accessed via HTTP GET.
Private methods require a valid authentication token and must be accessed via HTTP POST.
Errors are returned to the caller as a HTTP 400 return code and a descriptive error message.
Ensure that the contentType of the your JSON POST request is set to 'application/json'.
Fiat currency amounts cannot have more than 2 decimal places, and XBT amounts cannot have more than 8 decimal places.
"""
from .public import *
from .authentication import *
from .private import *
from .websocket import *