class Stock:
    stocks = ['jamt', 'lumber', 'Fire']

    def find(self, item):
        for stock in self.stocks:
            if item == stock:
                return True
        return False

    def remove(self, item):
        value = self.stocks.pop(item)
        if value == item:
            return True
        return False

    def add(self, name):
        self.stocks.append(name)
        return True

    def is_list_empty(self):
        if len(self.stocks) == 0:
            return True
        else:
            return False
