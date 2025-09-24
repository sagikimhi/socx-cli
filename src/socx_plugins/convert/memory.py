from __future__ import annotations

from typing import TypedDict

from pydantic import BaseModel


class MemorySegment(BaseModel):
    origin: int
    """
    Origin/Base address of the address space.
    """

    length: int
    """
    Length/Size of the address space in bytes.
    """

    end: int
    """
    End/Highest memory address of the address space.
    """


class DynamicSymbol(BaseModel):
    name: str
    """
    Name identifier aliased with the symbol.
    """

    addr: int
    """
    Symbol start address in the relevant address space.
    """

    length: int
    """
    Total byte length symbol takes up in memory address space.
    """

    index: int
    """
    Index of symbol in symbol table.
    """


class SymbolTable(TypedDict):
    device: str
    """
    Name identifier of the device associated with the address space.
    """

    segment: MemorySegment
    """
    Address space memory adress specification.
    """

    symbols: list[DynamicSymbol]
    """
    Tuple listing of all dynamic symbols associated with the device and their
    mapping within the address space.
    """
