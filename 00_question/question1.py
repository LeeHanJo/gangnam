class Account:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount}원이 입금되었습니다. 현재 잔액: {self.balance}원")
        else:
            print("입금 금액은 0보다 커야 합니다.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액이 부족하여 출금할 수 없습니다.")
        elif amount <= 0:
            print("출금 금액은 0보다 커야 합니다.")
        else:
            self.balance -= amount
            print(f"{amount}원이 출금되었습니다. 현재 잔액: {self.balance}원")

    def display_balance(self):
        print(f"{self.owner}님의 현재 잔액: {self.balance}원")

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, owner, initial_balance=0):
        if owner in self.accounts:
            print(f"{owner}님은 이미 계좌를 가지고 있습니다.")
        else:
            self.accounts[owner] = Account(owner, initial_balance)
            print(f"{owner}님의 계좌가 생성되었습니다. 초기 잔액: {initial_balance}원")

    def get_account(self, owner):
        if owner in self.accounts:
            return self.accounts[owner]
        else:
            print(f"{owner}님의 계좌를 찾을 수 없습니다.")
            return None

    def display_accounts(self):
        if self.accounts:
            print(f"{self.name} 은행의 계좌 목록:")
            for account in self.accounts.values():
                account.display_balance()
        else:
            print("현재 등록된 계좌가 없습니다.")

def main():
    bank = Bank("미래 은행")

    while True:
        print("\n옵션을 선택하세요:")
        print("1. 계좌 생성")
        print("2. 입금")
        print("3. 출금")
        print("4. 잔액 조회")
        print("5. 모든 계좌 조회")
        print("6. 종료")

        choice = input("선택: ")

        if choice == "1":
            owner = input("소유주 이름: ")
            initial_balance = int(input("초기 잔액: "))
            bank.create_account(owner, initial_balance)

        elif choice == "2":
            owner = input("소유주 이름: ")
            amount = int(input("입금 금액: "))
            account = bank.get_account(owner)
            if account:
                account.deposit(amount)

        elif choice == "3":
            owner = input("소유주 이름: ")
            amount = int(input("출금 금액: "))
            account = bank.get_account(owner)
            if account:
                account.withdraw(amount)

        elif choice == "4":
            owner = input("소유주 이름: ")
            account = bank.get_account(owner)
            if account:
                account.display_balance()

        elif choice == "5":
            bank.display_accounts()

        elif choice == "6":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
    
