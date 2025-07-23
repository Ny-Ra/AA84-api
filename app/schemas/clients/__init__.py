"""
Clients domain schemas exports
"""
from .schemas import (
    # Client
    Client, ClientCreate, ClientUpdate, ClientBase, ClientLogin, ClientInDB,
    
    # Address
    Address, AddressCreate, AddressUpdate, AddressBase,
)

__all__ = [
    # Client
    "Client", "ClientCreate", "ClientUpdate", "ClientBase", "ClientLogin", "ClientInDB",
    
    # Address
    "Address", "AddressCreate", "AddressUpdate", "AddressBase",
]