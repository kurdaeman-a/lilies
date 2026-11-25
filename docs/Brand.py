"""Brand module for the online shop system."""

from typing import List

STATUS_ACTIVE = "active"
STATUS_INACTIVE = "inactive"
STATUS_EMPTY = "no items"


class Brand:
    """Represents a brand that groups items and is managed by managers."""

    def __init__(self, brand_id: int, brand_name: str) -> None:
        """Create a brand.

        Args:
            brand_id: Unique identifier of the brand.
            brand_name: Display name of the brand.
        """
        self._brand_id = brand_id
        self._brand_name = brand_name
        self._items: List["Item"] = []
        self._is_active = True

    @property
    def brand_id(self) -> int:
        """Return the brand's unique identifier."""
        return self._brand_id

    @property
    def brand_name(self) -> str:
        """Return the brand's name."""
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value: str) -> None:
        """Update the brand's name."""
        self._brand_name = value

    @property
    def items(self) -> List["Item"]:
        """Return a copy of the items that belong to this brand."""
        return list(self._items)

    def add_item(self, item: "Item") -> None:
        """Add an item to this brand (Brand 1 --- 1..* Item)."""
        if item not in self._items:
            self._items.append(item)

    def remove_item(self, item: "Item") -> None:
        """Remove an item from this brand if it exists."""
        if item in self._items:
            self._items.remove(item)

    def activate(self) -> None:
        """Mark the brand as active."""
        self._is_active = True

    def deactivate(self) -> None:
        """Mark the brand as inactive."""
        self._is_active = False

    def check_brand_status(self) -> str:
        """Return the current status of the brand.

        Returns:
            STATUS_INACTIVE if deactivated, STATUS_EMPTY if it has no
            items, otherwise STATUS_ACTIVE.
        """
        if not self._is_active:
            return STATUS_INACTIVE
        if not self._items:
            return STATUS_EMPTY
        return STATUS_ACTIVE

    def __repr__(self) -> str:
        """Return a developer-friendly representation of the brand."""
        return f"Brand(id={self._brand_id}, name={self._brand_name!r})"