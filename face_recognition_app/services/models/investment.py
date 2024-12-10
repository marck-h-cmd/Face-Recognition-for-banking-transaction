class Investment:
    @staticmethod
    def get_collection():
        return Database.get_db()["investments"]
    
    def __init__(self, investment_id, client_id, amount, invest_type, date, status):
        self.investment_id = investment_id
        self.client_id = client_id
        self.amount = amount
        self.invest_type = invest_type
        self.date = date
        self.status = status

    @staticmethod
    def insert(investment_id, client_id, amount, invest_type, date, status):
        collection = Investment.get_collection()
        return collection.insert_one({
            'investment_id': investment_id,
            'client_id': client_id,
            'amount': amount,
            'invest_type': invest_type,
            'date': date.strftime("%Y-%m-%d"),
            'status': status
        })

    @classmethod
    def find_by_investment_id(cls, investment_id):
        collection = cls.get_collection()
        investment_data = collection.find_one({'investment_id': investment_id})
        return cls(
            investment_data['investment_id'], investment_data['client_id'],
            investment_data['amount'], investment_data['invest_type'], 
            datetime.strptime(investment_data['date'], "%Y-%m-%d"),
            investment_data['status']
        ) if investment_data else None

    @classmethod
    def list_all(cls):
        collection = cls.get_collection()
        investments = []
        for investment_data in collection.find():
            investments.append(cls(
                investment_data['investment_id'], investment_data['client_id'], 
                investment_data['amount'], investment_data['invest_type'], 
                datetime.strptime(investment_data['date'], "%Y-%m-%d"),
                investment_data['status']
            ))
        return investments