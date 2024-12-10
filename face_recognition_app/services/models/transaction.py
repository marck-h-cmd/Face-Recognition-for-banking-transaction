class Transaction:
    @staticmethod
    def get_collection():
        return Database.get_db()["transactions"]
    
    def __init__(self, transaction_id, from_account, to_account, amount, date, trans_type):
        self.transaction_id = transaction_id
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
        self.date = date
        self.trans_type = trans_type

    @staticmethod
    def insert(transaction_id, from_account, to_account, amount, date, trans_type):
        collection = Transaction.get_collection()
        return collection.insert_one({
            'transaction_id': transaction_id,
            'from_account': from_account,
            'to_account': to_account,
            'amount': amount,
            'date': date.strftime("%Y-%m-%d"),
            'trans_type': trans_type
        })

    @classmethod
    def find_by_transaction_id(cls, transaction_id):
        collection = cls.get_collection()
        transaction_data = collection.find_one({'transaction_id': transaction_id})
        return cls(
            transaction_data['transaction_id'], transaction_data['from_account'],
            transaction_data['to_account'], transaction_data['amount'],
            datetime.strptime(transaction_data['date'], "%Y-%m-%d"), 
            transaction_data['trans_type']
        ) if transaction_data else None

    @classmethod
    def list_all(cls):
        collection = cls.get_collection()
        transactions = []
        for transaction_data in collection.find():
            transactions.append(cls(
                transaction_data['transaction_id'], transaction_data['from_account'], 
                transaction_data['to_account'], transaction_data['amount'],
                datetime.strptime(transaction_data['date'], "%Y-%m-%d"), 
                transaction_data['trans_type']
            ))
        return transactions