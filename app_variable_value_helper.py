from Cards.card_types import CardColorType

class AppVariableValueHelper:
    """
    Helper class for storing and converting application-wide variables such as screen and card dimensions.

    Attributes:
        cardDecreaseWidthBy (float): Amount to decrease the card width by (default: 2).
        cardDecreasHeightBy (float): Amount to decrease the card height by (default: 2).
        cardHeight (float): Height of a card.
        cardWidth (float): Width of a card.
        screenHeight (float): Height of the application window.
        screenWidth (float): Width of the application window.
    """

    cardDecreaseWidthBy: float = 2
    cardDecreasHeightBy: float = 2
    cardHeight: float
    cardWidth: float
    screenHeight: float
    screenWidth: float
    
    def __init__(self, screenWidth: float, screenHeight: float):
        """
        Initializes the AppVariableValueHelper with screen and card dimensions.

        Args:
            screenWidth (float): Width of the application window.
            screenHeight (float): Height of the application window.
        """
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.cardHeight = 200
        self.cardWidth = 100
        
    def cardNameToColor(self, name: str) -> CardColorType:
        """
        Converts a card name string to its corresponding CardColorType enum value.

        Args:
            name (str): The name of the card color ("Acorns", "Balls", "Green", or other).

        Returns:
            CardColorType: The corresponding CardColorType enum value.
        """
        if name == "Acorns":
            return CardColorType.ACORN
        if name == "Balls":
            return CardColorType.BELL
        if name == "Green":
            return CardColorType.LEAF
        return CardColorType.HEART