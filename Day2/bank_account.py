import logging

# Configuration du système de journalisation
logging.basicConfig(
    filename='bank.log',
    level=logging.INFO,
    format='%(levelname)s - %(message)s'
)

class BankAccount:
    """
    Classe représentant un compte bancaire simple avec des opérations de base
    comme le dépôt, le retrait et la vérification du solde.
    """
    
    def __init__(self, account_holder, balance=0.0):
        """
        Initialise un nouveau compte bancaire.
        
        Args:
            account_holder (str): Nom du titulaire du compte
            balance (float, optional): Solde initial du compte. Par défaut 0.0
        """
        self.account_holder = account_holder
        self.balance = balance
        logging.info(f"Nouveau compte créé pour {account_holder} | Solde initial: ${balance}")
    
    def deposit(self, amount):
        """
        Dépose un montant d'argent sur le compte.
        
        Args:
            amount (float): Montant à déposer
            
        Raises:
            ValueError: Si le montant est négatif
            
        Returns:
            float: Nouveau solde
        """
        if amount < 0:
            logging.error(f"Montant de dépôt invalide: ${amount}")
            raise ValueError("Le montant du dépôt ne peut pas être négatif")
        
        # Cas limite: dépôt de $0 ne change pas le solde
        if amount == 0:
            logging.info(f"Dépôt de $0 | Solde inchangé: ${self.balance}")
            return self.balance
            
        self.balance += amount
        logging.info(f"Dépôt: ${amount} | Nouveau solde: ${self.balance}")
        return self.balance
    
    def withdraw(self, amount):
        """
        Retire un montant d'argent du compte.
        
        Args:
            amount (float): Montant à retirer
            
        Raises:
            ValueError: Si le montant est négatif ou supérieur au solde disponible
            
        Returns:
            float: Nouveau solde
        """
        if amount < 0:
            logging.error(f"Montant de retrait invalide: ${amount}")
            raise ValueError("Le montant du retrait ne peut pas être négatif")
            
        if amount > self.balance:
            logging.warning(f"Fonds insuffisants pour le retrait: ${amount} | Solde actuel: ${self.balance}")
            raise ValueError("Fonds insuffisants pour effectuer ce retrait")
            
        self.balance -= amount
        logging.info(f"Retrait: ${amount} | Nouveau solde: ${self.balance}")
        return self.balance
    
    def get_balance(self):
        """
        Retourne le solde actuel du compte.
        
        Returns:
            float: Solde actuel
        """
        logging.info(f"Consultation de solde par {self.account_holder} | Solde: ${self.balance}")
        return self.balance
