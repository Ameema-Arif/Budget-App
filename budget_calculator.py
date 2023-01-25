class Category:
    def __init__(self, categories):
        self.ledger = []
        self.category = categories

    def deposit(self, amount, description = ""):
        deposit = {"amount" : amount, "description" : description}
        self.ledger.append(deposit)

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount) == True:
            withdraw = {"amount" : -abs(amount), "description" : description}
            self.ledger.append(withdraw)
            return True
        else:
            return False

    def get_balance(self):
        for index in self.ledger:
            balance += index["amount"]
        return balance

    def transfer(self, t_amount, rcategory):
        if self.check_funds(t_amount) == True:
            withdraw = {"amount" : -abs(t_amount), "description" : "Transfer to %s"%rcategory}
            self.ledger.append(withdraw)
            deposit = {"amount" : t_amount, "description" : "Transfer from %s"%self.category}
            rcategory.ledger.append(deposit)
            return True
        else:
            return False

    def check_funds(self, amount):
        funds = 0
        for index in self.ledger:
            funds += index["amount"]

        if funds >= amount:
            return True
        else:
            return False

    def total_withdrawals(self):
        total_taken = 0
        for index in self.ledger:
            if index["amount"] < 0:
                total_taken += index["amount"]
            else:
                continue
        return total_taken
                

    def __str__(self):
        self.items = ""
        self.total = 0
        self.title = self.category.center(30, "*")+"\n"
        for index in self.ledger:
            self.items += (index["description"][0:23]).ljust(23) + ("%.2f" %index["amount"]).rjust(7) + "\n"
            self.total += index["amount"]
        self.ft = "Total: %f" %self.total
        return(self.title, self.items, self.ft)
